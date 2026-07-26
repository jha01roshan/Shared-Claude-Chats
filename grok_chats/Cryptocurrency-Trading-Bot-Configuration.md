# Cryptocurrency Trading Bot Configuration

- Source: https://grok.com/share/bGVnYWN5_c8ebd344-b4e9-4b2b-9ce1-aa6d3f1fb508
- Created: 2025-04-21
- Messages: 2

---

## Human

const ccxt = require('ccxt');
const dhive = require('@hiveio/dhive');
const SSC = require('sscjs');

// Configuration
const CONFIG = {
  CLIENT_ID: 'YOUR_API_KEY_HERE', // Replace with your ProBit API Key
  CLIENT_SECRET: 'YOUR_API_SECRET_HERE', // Replace with your ProBit API Secret
  PAIR: 'BLURT/BTC',
  QUANTITY: 10000,
  NUM_ORDERS_PER_SIDE: 5,
  MAX_ORDERS_PER_SIDE: 20,
  PRICE_SPREAD: 0.025,
  ORDER_SPACING: 0.01,
  MIN_TICK_SIZE: 0.00000001,
  TICK_INTERVAL_MS: 60000,
  POOL_ID: 158,
  HIVE_ENGINE_RPC: 'https://api.hive-engine.com/rpc',
  HIVE_NODE: 'https://api.hive.blog',
};

// Initialize ProBit exchange instance
const exchange = new ccxt.probit({
  apiKey: CONFIG.CLIENT_ID,
  secret: CONFIG.CLIENT_SECRET,
  enableRateLimit: true,
});

// Initialize dhive client for Hive blockchain
const hiveClient = new dhive.Client(CONFIG.HIVE_NODE);

// Initialize SSCJS for Hive-Engine
const ssc = new SSC(CONFIG.HIVE_ENGINE_RPC);

// Function to authenticate with ProBit
async function authenticateProbit() {
  try {
    console.log('Authenticating with ProBit...');
    await exchange.signIn();
    console.log('ProBit authentication successful.');
    return true;
  } catch (error) {
    console.error('ProBit authentication failed:', error.message);
    console.error(`Please verify CLIENT_ID and CLIENT_SECRET in bot.js. Go to probit.com > API Management, create a new key with Trade permissions, and update bot.js.`);
    return false;
  }
}

// Function to check ProBit account balance for multiple orders
async function checkBalance(quantity, buyPrice, sellPrice, numBuyOrders, numSellOrders, existingBuyOrders, existingSellOrders) {
  try {
    const balance = await exchange.fetchBalance();
    const btcBalance = balance.free['BTC'] || 0;
    const blurtBalance = balance.free['BLURT'] || 0;
    const buyOrdersNeeded = Math.max(0, numBuyOrders - existingBuyOrders.length);
    const sellOrdersNeeded = Math.max(0, numSellOrders - existingSellOrders.length);
    const buyCost = quantity * buyPrice * buyOrdersNeeded; // BTC needed for new buy orders
    const sellAmount = quantity * sellOrdersNeeded; // BLURT needed for new sell orders

    console.log(`[DEBUG] Balance: ${btcBalance} BTC, ${blurtBalance} BLURT`);

    if (buyOrdersNeeded > 0 && btcBalance < buyCost) {
      console.error(`Insufficient BTC balance: ${btcBalance} BTC available, ${buyCost} BTC needed for ${buyOrdersNeeded} buy orders.`);
      return false;
    }
    if (sellOrdersNeeded > 0 && blurtBalance < sellAmount) {
      console.error(`Insufficient BLURT balance: ${blurtBalance} BLURT available, ${sellAmount} BLURT needed for ${sellOrdersNeeded} sell orders.`);
      return false;
    }
    return true;
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return checkBalance(quantity, buyPrice, sellPrice, numBuyOrders, numSellOrders, existingBuyOrders, existingSellOrders);
      }
    }
    console.error('Error checking balance:', error.message);
    return false;
  }
}

// Function to fetch SWAP.BLURT:SWAP.BTC pool price
async function getBlurtBtcPoolData() {
  try {
    const result = await ssc.find('marketpools', 'pools', { _id: CONFIG.POOL_ID }, 1, 0, []);
    if (!result || result.length === 0) {
      console.log(`[${new Date().toISOString()}] No Diesel Pool found for _id: ${CONFIG.POOL_ID} (SWAP.BLURT:SWAP.BTC)`);
      return null;
    }

    const pool = result[0];
    const blurtQuantity = Number(pool.baseQuantity);
    const btcQuantity = Number(pool.quoteQuantity);
    const blurtPerBtc = blurtQuantity / btcQuantity;
    const btcPoolPrice = 1 / blurtPerBtc;

    console.log(`[DEBUG] Pool Data: baseQuantity=${blurtQuantity}, quoteQuantity=${btcQuantity}, BLURT/BTC=${blurtPerBtc}`);

    return { blurtPerBtc, btcPoolPrice };
  } catch (error) {
    console.error('Error fetching SWAP.BLURT:SWAP.BTC pool:', error.message);
    return null;
  }
}

// Function to format price to human-readable
function formatPrice(price, isBlurtPerBtc = false) {
  if (!price) return 'Unavailable';
  if (isBlurtPerBtc) {
    return Number(price.toFixed(4)).toString();
  }
  return Number(price.toFixed(8)).toString();
}

// Function to fetch and log ticker data for BLURT-BTC
async function getMarketPrice(pair) {
  try {
    if (!(await authenticateProbit())) {
      return null;
    }

    const ticker = await exchange.fetchTicker(pair);
    const probitPrice = ticker.last;
    const probitBlurtPerBtc = probitPrice ? 1 / probitPrice : null;
    const timestamp = new Date().toLocaleString();

    const poolData = await getBlurtBtcPoolData();
    const poolBlurtPerBtc = poolData ? poolData.blurtPerBtc : null;
    const poolPrice = poolData ? poolData.btcPoolPrice : null;

    console.log(`[${timestamp}] ProBit ${pair} Price: ${formatPrice(probitBlurtPerBtc, true)} BLURT/BTC`);
    console.log(`[${timestamp}] Hive-Engine SWAP.BLURT:SWAP.BTC Pool Price: ${formatPrice(poolBlurtPerBtc, true)} BLURT/BTC`);

    return { probitBlurtPerBtc, poolPrice, poolBlurtPerBtc };
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return getMarketPrice(pair);
      }
    }
    console.error('Error fetching price:', error.message);
    return null;
  }
}

// Function to manage open orders
async function manageOpenOrders(pair, maxOrdersPerSide) {
  try {
    if (!(await authenticateProbit())) {
      return { buyOrders: [], sellOrders: [] };
    }

    const openOrders = await exchange.fetchOpenOrders(pair);
    const buyOrders = openOrders.filter(order => order.side === 'buy');
    const sellOrders = openOrders.filter(order => order.side === 'sell');

    if (buyOrders.length > maxOrdersPerSide) {
      const sortedBuyOrders = buyOrders.sort((a, b) => a.timestamp - b.timestamp);
      const excessBuyOrders = sortedBuyOrders.slice(0, buyOrders.length - maxOrdersPerSide);
      for (const order of excessBuyOrders) {
        await exchange.cancelOrder(order.id, pair);
        console.log(`Cancelled excess buy order ${order.id} at ${formatPrice(order.price)} BTC`);
      }
    }

    if (sellOrders.length > maxOrdersPerSide) {
      const sortedSellOrders = sellOrders.sort((a, b) => a.timestamp - b.timestamp);
      const excessSellOrders = sortedSellOrders.slice(0, sellOrders.length - maxOrdersPerSide);
      for (const order of excessSellOrders) {
        await exchange.cancelOrder(order.id, pair);
        console.log(`Cancelled excess sell order ${order.id} at ${formatPrice(order.price)} BTC`);
      }
    }

    return { buyOrders, sellOrders };
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return manageOpenOrders(pair, maxOrdersPerSide);
      }
    }
    console.error('Error managing open orders:', error.message);
    return { buyOrders: [], sellOrders: [] };
  }
}

// Function to place up to 5 limit buy and 5 sell orders
async function placeLimitOrders(pair, poolPrice, quantity, numOrders) {
  try {
    if (!(await authenticateProbit())) {
      console.log('Authentication failed. Skipping order placement.');
      return false;
    }

    let baseBuyPrice = poolPrice * (1 - CONFIG.PRICE_SPREAD);
    let baseSellPrice = poolPrice * (1 + CONFIG.PRICE_SPREAD);

    if (baseSellPrice < baseBuyPrice * (1 + CONFIG.ORDER_SPACING)) {
      baseSellPrice = baseBuyPrice * (1 + CONFIG.ORDER_SPACING);
      console.log(`Adjusted base sell price to ${formatPrice(baseSellPrice)} BTC to maintain ${CONFIG.ORDER_SPACING * 100}% spacing`);
    }

    baseBuyPrice = Math.max(baseBuyPrice, CONFIG.MIN_TICK_SIZE);
    baseSellPrice = Math.max(baseSellPrice, CONFIG.MIN_TICK_SIZE);

    const { buyOrders, sellOrders } = await manageOpenOrders(pair, CONFIG.MAX_ORDERS_PER_SIDE);

    if (!(await checkBalance(quantity, baseBuyPrice, baseSellPrice, numOrders, numOrders, buyOrders, sellOrders))) {
      console.log('Insufficient balance. Skipping order placement.');
      return false;
    }

    const sortedBuyOrders = buyOrders.sort((a, b) => b.price - a.price);
    const sortedSellOrders = sellOrders.sort((a, b) => a.price - b.price);

    const buyOrdersNeeded = Math.max(0, numOrders - sortedBuyOrders.length);
    let buyPrices = [];
    let currentBuyPrice = sortedBuyOrders.length > 0 ? sortedBuyOrders[sortedBuyOrders.length - 1].price * (1 - CONFIG.ORDER_SPACING) : baseBuyPrice;
    for (let i = 0; i < buyOrdersNeeded; i++) {
      currentBuyPrice = i === 0 ? currentBuyPrice : currentBuyPrice * (1 - CONFIG.ORDER_SPACING);
      currentBuyPrice = Math.max(currentBuyPrice, CONFIG.MIN_TICK_SIZE);
      buyPrices.push(currentBuyPrice);
    }

    const sellOrdersNeeded = Math.max(0, numOrders - sortedSellOrders.length);
    let sellPrices = [];
    let currentSellPrice = sortedSellOrders.length > 0 ? sortedSellOrders[sortedSellOrders.length - 1].price * (1 + CONFIG.ORDER_SPACING) : baseSellPrice;
    for (let i = 0; i < sellOrdersNeeded; i++) {
      currentSellPrice = i === 0 ? currentSellPrice : currentSellPrice * (1 + CONFIG.ORDER_SPACING);
      currentSellPrice = Math.max(currentSellPrice, CONFIG.MIN_TICK_SIZE);
      sellPrices.push(currentSellPrice);
    }

    const highestBuyPrice = sortedBuyOrders.length > 0 ? sortedBuyOrders[0].price : buyPrices.length > 0 ? buyPrices[0] : baseBuyPrice;
    if (sellPrices.length > 0 && sellPrices[0] < highestBuyPrice * (1 + CONFIG.ORDER_SPACING)) {
      sellPrices = sellPrices.map(price => highestBuyPrice * (1 + CONFIG.ORDER_SPACING) * (price / sellPrices[0]));
      console.log(`Adjusted sell prices to maintain ${CONFIG.ORDER_SPACING * 100}% spacing from highest buy price`);
    }

    for (const buyPrice of buyPrices) {
      if (buyOrders.length >= CONFIG.MAX_ORDERS_PER_SIDE) {
        console.log(`Max buy orders (${CONFIG.MAX_ORDERS_PER_SIDE}) reached. Stopping buy order placement.`);
        break;
      }
      const buyPriceExists = buyOrders.some(order => Math.abs(order.price - buyPrice) < 0.0000000001);
      if (!buyPriceExists) {
        const buyOrder = await exchange.createLimitBuyOrder(pair, quantity, buyPrice);
        console.log(`Placed limit buy order for ${quantity} BLURT at ${formatPrice(buyPrice)} BTC`);
        buyOrders.push({ price: buyPrice, side: 'buy' });
      } else {
        console.log(`Buy price ${formatPrice(buyPrice)} BTC exists. Skipping.`);
      }
    }

    for (const sellPrice of sellPrices) {
      if (sellOrders.length >= CONFIG.MAX_ORDERS_PER_SIDE) {
        console.log(`Max sell orders (${CONFIG.MAX_ORDERS_PER_SIDE}) reached. Stopping sell order placement.`);
        break;
      }
      const sellPriceExists = sellOrders.some(order => Math.abs(order.price - sellPrice) < 0.0000000001);
      if (!sellPriceExists) {
        const sellOrder = await exchange.createLimitSellOrder(pair, quantity, sellPrice);
        console.log(`Placed limit sell order for ${quantity} BLURT at ${formatPrice(sellPrice)} BTC`);
        sellOrders.push({ price: sellPrice, side: 'sell' });
      } else {
        console.log(`Sell price ${formatPrice(sellPrice)} BTC exists. Skipping.`);
      }
    }

    if (buyPrices.length === 0 && sellPrices.length === 0) {
      console.log(`No new orders needed. Current orders satisfy ${numOrders} buy and ${numOrders} sell requirement.`);
    }

    return true;
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return placeLimitOrders(pair, poolPrice, quantity, numOrders);
      }
    }
    console.error('Error placing limit orders:', error.message);
    if (error.message.includes('INVALID_ARGUMENT') && error.message.includes('cost')) {
      console.error(`Order cost too low. Ensure quantity * price ≥ ${CONFIG.MIN_TICK_SIZE} BTC (ProBit minimum).`);
    }
    return false;
  }
}

// Main bot logic for BLURT-BTC
async function runBot() {
  try {
    if (!(await authenticateProbit())) {
      console.error('Cannot start bot due to authentication failure.');
      return;
    }

    await exchange.loadMarkets();
    console.log(`Connected to ProBit. Markets loaded. Trading pair ${CONFIG.PAIR} available.`);
  } catch (error) {
    console.error('Failed to connect to ProBit:', error.message);
    return;
  }

  while (true) {
    const priceData = await getMarketPrice(CONFIG.PAIR);

    if (priceData && priceData.poolPrice) {
      const poolPrice = priceData.poolPrice;
      console.log(`Checking for new limit orders at pool price ${formatPrice(priceData.poolBlurtPerBtc, true)} BLURT/BTC (${formatPrice(poolPrice)} BTC)...`);
      const success = await placeLimitOrders(CONFIG.PAIR, poolPrice, CONFIG.QUANTITY, CONFIG.NUM_ORDERS_PER_SIDE);
      if (!success) {
        console.log('Order placement failed. Will retry on next tick.');
      }
    } else {
      console.log('No valid pool price. Skipping order placement until next tick.');
    }

    await new Promise(resolve => setTimeout(resolve, CONFIG.TICK_INTERVAL_MS));
  }
}

// Start the bot
console.log(`Starting ProBit trading bot for ${CONFIG.PAIR} (limit orders based on pool price) using CCXT...`);
runBot().catch(error => {
  console.error('Bot crashed:', error.message);
}); - print the entire code and explain how this bot works + setup instructions

---

## Assistant

Below is the complete code for the ProBit trading bot, followed by a detailed explanation of how it works and setup instructions.

### Complete Code

```javascript
const ccxt = require('ccxt');
const dhive = require('@hiveio/dhive');
const SSC = require('sscjs');

// Configuration
const CONFIG = {
  CLIENT_ID: 'YOUR_API_KEY_HERE', // Replace with your ProBit API Key
  CLIENT_SECRET: 'YOUR_API_SECRET_HERE', // Replace with your ProBit API Secret
  PAIR: 'BLURT/BTC',
  QUANTITY: 10000,
  NUM_ORDERS_PER_SIDE: 5,
  MAX_ORDERS_PER_SIDE: 20,
  PRICE_SPREAD: 0.025,
  ORDER_SPACING: 0.01,
  MIN_TICK_SIZE: 0.00000001,
  TICK_INTERVAL_MS: 60000,
  POOL_ID: 158,
  HIVE_ENGINE_RPC: 'https://api.hive-engine.com/rpc',
  HIVE_NODE: 'https://api.hive.blog',
};

// Initialize ProBit exchange instance
const exchange = new ccxt.probit({
  apiKey: CONFIG.CLIENT_ID,
  secret: CONFIG.CLIENT_SECRET,
  enableRateLimit: true,
});

// Initialize dhive client for Hive blockchain
const hiveClient = new dhive.Client(CONFIG.HIVE_NODE);

// Initialize SSCJS for Hive-Engine
const ssc = new SSC(CONFIG.HIVE_ENGINE_RPC);

// Function to authenticate with ProBit
async function authenticateProbit() {
  try {
    console.log('Authenticating with ProBit...');
    await exchange.signIn();
    console.log('ProBit authentication successful.');
    return true;
  } catch (error) {
    console.error('ProBit authentication failed:', error.message);
    console.error(`Please verify CLIENT_ID and CLIENT_SECRET in bot.js. Go to probit.com > API Management, create a new key with Trade permissions, and update bot.js.`);
    return false;
  }
}

// Function to check ProBit account balance for multiple orders
async function checkBalance(quantity, buyPrice, sellPrice, numBuyOrders, numSellOrders, existingBuyOrders, existingSellOrders) {
  try {
    const balance = await exchange.fetchBalance();
    const btcBalance = balance.free['BTC'] || 0;
    const blurtBalance = balance.free['BLURT'] || 0;
    const buyOrdersNeeded = Math.max(0, numBuyOrders - existingBuyOrders.length);
    const sellOrdersNeeded = Math.max(0, numSellOrders - existingSellOrders.length);
    const buyCost = quantity * buyPrice * buyOrdersNeeded; // BTC needed for new buy orders
    const sellAmount = quantity * sellOrdersNeeded; // BLURT needed for new sell orders

    console.log(`[DEBUG] Balance: ${btcBalance} BTC, ${blurtBalance} BLURT`);

    if (buyOrdersNeeded > 0 && btcBalance < buyCost) {
      console.error(`Insufficient BTC balance: ${btcBalance} BTC available, ${buyCost} BTC needed for ${buyOrdersNeeded} buy orders.`);
      return false;
    }
    if (sellOrdersNeeded > 0 && blurtBalance < sellAmount) {
      console.error(`Insufficient BLURT balance: ${blurtBalance} BLURT available, ${sellAmount} BLURT needed for ${sellOrdersNeeded} sell orders.`);
      return false;
    }
    return true;
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return checkBalance(quantity, buyPrice, sellPrice, numBuyOrders, numSellOrders, existingBuyOrders, existingSellOrders);
      }
    }
    console.error('Error checking balance:', error.message);
    return false;
  }
}

// Function to fetch SWAP.BLURT:SWAP.BTC pool price
async function getBlurtBtcPoolData() {
  try {
    const result = await ssc.find('marketpools', 'pools', { _id: CONFIG.POOL_ID }, 1, 0, []);
    if (!result || result.length === 0) {
      console.log(`[${new Date().toISOString()}] No Diesel Pool found for _id: ${CONFIG.POOL_ID} (SWAP.BLURT:SWAP.BTC)`);
      return null;
    }

    const pool = result[0];
    const blurtQuantity = Number(pool.baseQuantity);
    const btcQuantity = Number(pool.quoteQuantity);
    const blurtPerBtc = blurtQuantity / btcQuantity;
    const btcPoolPrice = 1 / blurtPerBtc;

    console.log(`[DEBUG] Pool Data: baseQuantity=${blurtQuantity}, quoteQuantity=${btcQuantity}, BLURT/BTC=${blurtPerBtc}`);

    return { blurtPerBtc, btcPoolPrice };
  } catch (error) {
    console.error('Error fetching SWAP.BLURT:SWAP.BTC pool:', error.message);
    return null;
  }
}

// Function to format price to human-readable
function formatPrice(price, isBlurtPerBtc = false)Sat Apr 26 14:30:45 2025
  if (!price) return 'Unavailable';
  if (isBlurtPerBtc) {
    return Number(price.toFixed(4)).toString();
  }
  return Number(price.toFixed(8)).toString();
}

// Function to fetch and log ticker data for BLURT-BTC
async function getMarketPrice(pair) {
  try {
    if (!(await authenticateProbit())) {
      return null;
    }

    const ticker = await exchange.fetchTicker(pair);
    const probitPrice = ticker.last;
    const probitBlurtPerBtc = probitPrice ? 1 / probitPrice : null;
    const timestamp = new Date().toLocaleString();

    const poolData = await getBlurtBtcPoolData();
    const poolBlurtPerBtc = poolData ? poolData.blurtPerBtc : null;
    const poolPrice = poolData ? poolData.btcPoolPrice : null;

    console.log(`[${timestamp}] ProBit ${pair} Price: ${formatPrice(probitBlurtPerBtc, true)} BLURT/BTC`);
    console.log(`[${timestamp}] Hive-Engine SWAP.BLURT:SWAP.BTC Pool Price: ${formatPrice(poolBlurtPerBtc, true)} BLURT/BTC`);

    return { probitBlurtPerBtc, poolPrice, poolBlurtPerBtc };
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return getMarketPrice(pair);
      }
    }
    console.error('Error fetching price:', error.message);
    return null;
  }
}

// Function to manage open orders
async function manageOpenOrders(pair, maxOrdersPerSide) {
  try {
    if (!(await authenticateProbit())) {
      return { buyOrders: [], sellOrders: [] };
    }

    const openOrders = await exchange.fetchOpenOrders(pair);
    const buyOrders = openOrders.filter(order => order.side === 'buy');
    const sellOrders = openOrders.filter(order => order.side === 'sell');

    if (buyOrders.length > maxOrdersPerSide) {
      const sortedBuyOrders = buyOrders.sort((a, b) => a.timestamp - b.timestamp);
      const excessBuyOrders = sortedBuyOrders.slice(0, buyOrders.length - maxOrdersPerSide);
      for (const order of excessBuyOrders) {
        await exchange.cancelOrder(order.id, pair);
        console.log(`Cancelled excess buy order ${order.id} at ${formatPrice(order.price)} BTC`);
      }
    }

    if (sellOrders.length > maxOrdersPerSide) {
      const sortedSellOrders = sellOrders.sort((a, b) => a.timestamp - b.timestamp);
      const excessSellOrders = sortedSellOrders.slice(0, sellOrders.length - maxOrdersPerSide);
      for (const order of excessSellOrders) {
        await exchange.cancelOrder(order.id, pair);
        console.log(`Cancelled excess sell order ${order.id} at ${formatPrice(order.price)} BTC`);
      }
    }

    return { buyOrders, sellOrders };
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return manageOpenOrders(pair, maxOrdersPerSide);
      }
    }
    console.error('Error managing open orders:', error.message);
    return { buyOrders: [], sellOrders: [] };
  }
}

// Function to place up to 5 limit buy and 5 sell orders
async function placeLimitOrders(pair, poolPrice, quantity, numOrders) {
  try {
    if (!(await authenticateProBit())) {
      console.log('Authentication failed. Skipping order placement.');
      return false;
    }

    let baseBuyPrice = poolPrice * (1 - CONFIG.PRICE_SPREAD);
    let baseSellPrice = poolPrice * (1 + CONFIG.PRICE_SPREAD);

    if (baseSellPrice < baseBuyPrice * (1 + CONFIG.ORDER_SPACING)) {
      baseSellPrice = baseBuyPrice * (1 + CONFIG.ORDER_SPACING);
      console.log(`Adjusted base sell price to ${formatPrice(baseSellPrice)} BTC to maintain ${CONFIG.ORDER_SPACING * 100}% spacing`);
    }

    baseBuyPrice = Math.max(baseBuyPrice, CONFIG.MIN_TICK_SIZE);
    baseSellPrice = Math.max(baseSellPrice, CONFIG.MIN_TICK_SIZE);

    const { buyOrders, sellOrders } = await manageOpenOrders(pair, CONFIG.MAX_ORDERS_PER_SIDE);

    if (!(await checkBalance(quantity, baseBuyPrice, baseSellPrice, numOrders, numOrders, buyOrders, sellOrders))) {
      console.log('Insufficient balance. Skipping order placement.');
      return false;
    }

    const sortedBuyOrders = buyOrders.sort((a, b) => b.price - a.price);
    const sortedSellOrders = sellOrders.sort((a, b) => a.price - b.price);

    const buyOrdersNeeded = Math.max(0, numOrders - sortedBuyOrders.length);
    let buyPrices = [];
    let currentBuyPrice = sortedBuyOrders.length > 0 ? sortedBuyOrders[sortedBuyOrders.length - 1].price * (1 - CONFIG.ORDER_SPACING) : baseBuyPrice;
    for (let i = 0; i < buyOrdersNeeded; i++) {
      currentBuyPrice = i === 0 ? currentBuyPrice : currentBuyPrice * (1 - CONFIG.ORDER_SPACING);
      currentBuyPrice = Math.max(currentBuyPrice, CONFIG.MIN_TICK_SIZE);
      buyPrices.push(currentBuyPrice);
    }

    const sellOrdersNeeded = Math.max(0, numOrders - sortedSellOrders.length);
    let sellPrices = [];
    let currentSellPrice = sortedSellOrders.length > 0 ? sortedSellOrders[sortedSellOrders.length - 1].price * (1 + CONFIG.ORDER_SPACING) : baseSellPrice;
    for (let i = 0; i < sellOrdersNeeded; i++) {
      currentSellPrice = i === 0 ? currentSellPrice : currentSellPrice * (1 + CONFIG.ORDER_SPACING);
      currentSellPrice = Math.max(currentSellPrice, CONFIG.MIN_TICK_SIZE);
      sellPrices.push(currentSellPrice);
    }

    const highestBuyPrice = sortedBuyOrders.length > 0 ? sortedBuyOrders[0].price : buyPrices.length > 0 ? buyPrices[0] : baseBuyPrice;
    if (sellPrices.length > 0 && sellPrices[0] < highestBuyPrice * (1 + CONFIG.ORDER_SPACING)) {
      sellPrices = sellPrices.map(price => highestBuyPrice * (1 + CONFIG.ORDER_SPACING) * (price / sellPrices[0]));
      console.log(`Adjusted sell prices to maintain ${CONFIG.ORDER_SPACING * 100}% spacing from highest buy price`);
    }

    for (const buyPrice of buyPrices) {
      if (buyOrders.length >= CONFIG.MAX_ORDERS_PER_SIDE) {
        console.log(`Max buy orders (${CONFIG.MAX_ORDERS_PER_SIDE}) reached. Stopping buy order placement.`);
        break;
      }
      const buyPriceExists = buyOrders.some(order => Math.abs(order.price - buyPrice) < 0.0000000001);
      if (!buyPriceExists) {
        const buyOrder = await exchange.createLimitBuyOrder(pair, quantity, buyPrice);
        console.log(`Placed limit buy order for ${quantity} BLURT at ${formatPrice(buyPrice)} BTC`);
        buyOrders.push({ price: buyPrice, side: 'buy' });
      } else {
        console.log(`Buy price ${formatPrice(buyPrice)} BTC exists. Skipping.`);
      }
    }

    for (const sellPrice of sellPrices) {
      if (sellOrders.length >= CONFIG.MAX_ORDERS_PER_SIDE) {
        console.log(`Max sell orders (${CONFIG.MAX_ORDERS_PER_SIDE}) reached. Stopping sell order placement.`);
        break;
      }
      const sellPriceExists = sellOrders.some(order => Math.abs(order.price - sellPrice) < 0.0000000001);
      if (!sellPriceExists) {
        const sellOrder = await exchange.createLimitSellOrder(pair, quantity, sellPrice);
        console.log(`Placed limit sell order for ${quantity} BLURT at ${formatPrice(sellPrice)} BTC`);
        sellOrders.push({ price: sellPrice, side: 'sell' });
      } else {
        console.log(`Sell price ${formatPrice(sellPrice)} BTC exists. Skipping.`);
      }
    }

    if (buyPrices.length === 0 && sellPrices.length === 0) {
      console.log(`No new orders needed. Current orders satisfy ${numOrders} buy and ${numOrders} sell requirement.`);
    }

    return true;
  } catch (error) {
    if (error.message.includes('access token expired')) {
      console.log('Access token expired. Attempting to re-authenticate...');
      if (await authenticateProbit()) {
        return placeLimitOrders(pair, poolPrice, quantity, numOrders);
      }
    }
    console.error('Error placing limit orders:', error.message);
    if (error.message.includes('INVALID_ARGUMENT') && error.message.includes('cost')) {
      console.error(`Order cost too low. Ensure quantity * price ≥ ${CONFIG.MIN_TICK_SIZE} BTC (ProBit minimum).`);
    }
    return false;
  }
}

// Main bot logic for BLURT-BTC
async function runBot() {
  try {
    if (!(await authenticateProbit())) {
      console.error('Cannot start bot due to authentication failure.');
      return;
    }

    await exchange.loadMarkets();
    console.log(`Connected to ProBit. Markets loaded. Trading pair ${CONFIG.PAIR} available.`);
  } catch (error) {
    console.error('Failed to connect to ProBit:', error.message);
    return;
  }

  while (true) {
    const priceData = await getMarketPrice(CONFIG.PAIR);

    if (priceData && priceData.poolPrice) {
      const poolPrice = priceData.poolPrice;
      console.log(`Checking for new limit orders at pool price ${formatPrice(priceData.poolBlurtPerBtc, true)} BLURT/BTC (${formatPrice(poolPrice)} BTC)...`);
      const success = await placeLimitOrders(CONFIG.PAIR, poolPrice, CONFIG.QUANTITY, CONFIG.NUM_ORDERS_PER_SIDE);
      if (!success) {
        console.log('Order placement failed. Will retry on next tick.');
      }
    } else {
      console.log('No valid pool price. Skipping order placement until next tick.');
    }

    await new Promise(resolve => setTimeout(resolve, CONFIG.TICK_INTERVAL_MS));
  }
}

// Start the bot
console.log(`Starting ProBit trading bot for ${CONFIG.PAIR} (limit orders based on pool price) using CCXT...`);
runBot().catch(error => {
  console.error('Bot crashed:', error.message);
});
```

### How the Bot Works

This bot is designed to trade the BLURT/BTC pair on the ProBit exchange using the CCXT library, with pricing based on the SWAP.BLURT:SWAP.BTC liquidity pool on Hive-Engine. It places and manages limit buy and sell orders to provide liquidity around the pool price, effectively acting as a market-making bot. Here's a detailed breakdown of its functionality:

1. **Configuration**:
   - The `CONFIG` object defines key parameters:
     - `CLIENT_ID` and `CLIENT_SECRET`: ProBit API credentials.
     - `PAIR`: Trading pair (BLURT/BTC).
     - `QUANTITY`: Amount of BLURT per order (10,000).
     - `NUM_ORDERS_PER_SIDE`: Number of buy/sell orders to maintain (5 each).
     - `MAX_ORDERS_PER_SIDE`: Maximum open orders per side (20).
     - `PRICE_SPREAD`: Percentage spread from pool price (2.5%).
     - `ORDER_SPACING`: Price spacing between orders (1%).
     - `MIN_TICK_SIZE`: Minimum price increment (0.00000001 BTC).
     - `TICK_INTERVAL_MS`: Time between cycles (60 seconds).
     - `POOL_ID`: Hive-Engine pool ID (158 for SWAP.BLURT:SWAP.BTC).
     - `HIVE_ENGINE_RPC` and `HIVE_NODE`: API endpoints.

2. **Initialization**:
   - **ProBit**: Uses CCXT to connect to ProBit with API credentials and rate limiting.
   - **Hive**: Uses `dhive` for Hive blockchain interaction and `sscjs` for Hive-Engine.

3. **Authentication**:
   - The `authenticateProbit` function signs into ProBit using API credentials. It handles authentication failures and provides instructions to verify credentials.

4. **Balance Checking**:
   - The `checkBalance` function ensures sufficient BTC and BLURT for new orders:
     - Calculates BTC needed for buy orders (`quantity * buyPrice * numBuyOrders`).
     - Calculates BLURT needed for sell orders (`quantity * numSellOrders`).
     - Re-authenticates if the access token expires.

5. **Pool Price Fetching**:
   - The `getBlurtBtcPoolData` function retrieves the SWAP.BLURT:SWAP.BTC pool data from Hive-Engine:
     - Fetches base (BLURT) and quote (BTC) quantities.
     - Calculates `blurtPerBtc` (BLURT/BTC) and `btcPoolPrice` (BTC/BLURT).

6. **Market Price Fetching**:
   - The `getMarketPrice` function:
     - Fetches the latest BLURT/BTC ticker from ProBit.
     - Retrieves pool price from `getBlurtBtcPoolData`.
     - Logs both prices for monitoring.
     - Handles token expiration by re-authenticating.

7. **Order Management**:
   - The `manageOpenOrders` function:
     - Fetches open orders for BLURT/BTC.
     - Cancels excess orders (older orders first) if exceeding `MAX_ORDERS_PER_SIDE`.
     - Returns current buy and sell orders.

8. **Order Placement**:
   - The `placeLimitOrders` function:
     - Calculates base buy/sell prices based on pool price ± `PRICE_SPREAD`.
     - Ensures `ORDER_SPACING` between buy/sell prices.
     - Checks balance for new orders.
     - Determines additional buy/sell orders needed to reach `NUM_ORDERS_PER_SIDE`.
     - Places new limit orders with prices spaced by `ORDER_SPACING`:
       - Buy prices decrease from the base buy price.
       - Sell prices increase from the base sell price.
     - Avoids duplicate prices and respects `MAX_ORDERS_PER_SIDE`.
     - Adjusts sell prices to maintain spacing from the highest buy price.
     - Handles errors (e.g., token expiration, insufficient balance, minimum order cost).

9. **Main Loop**:
   - The `runBot` function:
     - Authenticates and loads ProBit markets.
     - Runs an infinite loop every `TICK_INTERVAL_MS` (60 seconds):
       - Fetches market and pool prices.
       - Places limit orders if a valid pool price exists.
       - Retries on failure.

10. **Error Handling**:
    - Handles token expiration by re-authenticating.
    - Logs detailed errors (e.g., insufficient balance, invalid order cost).
    - Continues running on non-fatal errors, retrying on the next tick.

### Strategy
- The bot maintains a balanced order book with up to 5 buy and 5 sell orders, spaced 1% apart, within a 2.5% spread of the Hive-Engine pool price.
- It acts as a market maker, profiting from the spread when orders are filled.
- It ensures liquidity by replacing filled orders and canceling excess orders.

### Setup Instructions

1. **Prerequisites**:
   - **Node.js**: Install Node.js (v14 or later) from [nodejs.org](https://nodejs.org).
   - **ProBit Account**: Create an account on [ProBit](https://www.probit.com).
   - **Funds**: Deposit BTC and BLURT to your ProBit account.

2. **Install Dependencies**:
   - Create a project directory and initialize a Node.js project:
     ```bash
     mkdir probit-bot
     cd probit-bot
     npm init -y
     ```
   - Install required packages:
     ```bash
     npm install ccxt @hiveio/dhive sscjs
     ```

3. **Create API Key**:
   - Log in to [ProBit](https://www.probit.com).
   - Go to **API Management** and create a new API key with **Trade** permissions.
   - Copy the **API Key** and **Secret Key**.

4. **Configure the Bot**:
   - Save the code as `bot.js`.
   - Replace `YOUR_API_KEY_HERE` and `YOUR_API_SECRET_HERE` in the `CONFIG` object with your ProBit API key and secret.
   - Adjust other `CONFIG` parameters if needed (e.g., `QUANTITY`, `PRICE_SPREAD`).

5. **Run the Bot**:
   - Execute the bot:
     ```bash
     node bot.js
     ```
   - The bot will authenticate, connect to ProBit, and start placing orders every 60 seconds.

6. **Monitor Output**:
   - Check console logs for authentication status, balance checks, pool prices, and order placements.
   - Address errors (e.g., insufficient balance, invalid API keys).

7. **Optional Enhancements**:
   - **Logging**: Add a logging library (e.g., `winston`) for persistent logs.
   - **Environment Variables**: Store `CLIENT_ID` and `CLIENT_SECRET` in a `.env` file using `dotenv`.
   - **Error Notifications**: Integrate with a notification service (e.g., Telegram, Discord) for critical errors.
   - **Testing**: Test with small `QUANTITY` values to avoid large losses.

### Notes
- **Risk**: Trading bots carry financial risks. Test thoroughly and monitor closely.
- **API Limits**: ProBit has rate limits. The `enableRateLimit: true` setting helps avoid bans.
- **Pool ID**: Verify `POOL_ID: 158` is correct for SWAP.BLURT:SWAP.BTC on Hive-Engine.
- **Maintenance**: Update API endpoints (`HIVE_ENGINE_RPC`, `HIVE_NODE`) if they change.

This bot provides a robust framework for market-making on ProBit, leveraging Hive-Engine pool prices for pricing accuracy. Adjust parameters based on your trading strategy and risk tolerance.
