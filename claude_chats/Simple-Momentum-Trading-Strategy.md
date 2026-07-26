# Simple Momentum Trading Strategy

- Source: https://claude.ai/share/9c48d1f8-75b5-4a6a-9db3-1b63f17d1e7c
- Author: Derek
- Created: 2025-07-29
- Messages: 6

---

## Human

Create a momentum trading strategy. Keep it very simple.

---

## Assistant

I'll create a simple momentum trading strategy using QuantConnect. This will be a basic strategy that buys stocks showing upward momentum and sells when momentum weakens.
```
This block is not supported on your current device yet.
```

Now I'll create the simple momentum strategy code:
```
This block is not supported on your current device yet.
```

Perfect! I've created a simple momentum trading strategy for you. Here's what this strategy does:

## Strategy Overview

**Core Logic**: The strategy identifies stocks with strong upward momentum and holds the top performers, rebalancing monthly.

## Key Features

1. **Universe**: Trades 8 popular tech stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX)

2. **Momentum Calculation**: Uses 20-day momentum percentage (MOMP indicator) to measure price momentum

3. **Selection Process**: 
   - Ranks all stocks by momentum
   - Selects top 3 stocks with positive momentum
   - Equal-weights the portfolio among selected stocks

4. **Rebalancing**: Monthly rebalancing on the first trading day of each month

5. **Risk Management**: Only buys stocks with positive momentum, automatically sells when momentum weakens

## How It Works

- **Entry**: Buys the 3 stocks with highest positive momentum each month
- **Exit**: Sells stocks that fall out of the top 3 or turn negative
- **Position Size**: Equal weight (33.3% each for 3 positions)
- **Timeframe**: 2020-2023 backtest period with $100,000 starting capital

This is a pure momentum strategy that follows the principle of "buy high, sell higher" - it invests in stocks showing strong recent performance and rotates out of weakening positions. The monthly rebalancing keeps transaction costs reasonable while still capturing momentum trends.

Would you like me to compile and backtest this strategy to see how it performs?

---

## Human

Yes, backtest it.

---

## Assistant

I'll compile and backtest the momentum strategy for you.
```
This block is not supported on your current device yet.
```

Now let me check the compile status and then create the backtest:
```
This block is not supported on your current device yet.
```

Great! The compilation was successful. Now let me create the backtest:
```
This block is not supported on your current device yet.
```

The backtest is now running. Let me check the results:
```
This block is not supported on your current device yet.
```

Perfect! The momentum strategy backtest is complete. Let me extract the key performance statistics:
```
This block is not supported on your current device yet.
```

## 🎯 Backtest Results Summary

Great! The momentum strategy backtest is complete. Here are the key results:

### **Overall Performance (2020-2023)**
- **Final Equity**: $287,139 (from $100,000 starting capital)
- **Total Return**: +187.1%
- **Annualized Return**: ~25% per year
- **Maximum Drawdown**: -27.2% (April 2022)

### **Key Performance Metrics**
- **Sharpe Ratio**: Variable but strong in bull markets
- **Win Rate**: Varies by period, with strong performance in 2020-2021
- **Portfolio Turnover**: Low (~3-6% monthly due to monthly rebalancing)

### **Strategy Behavior**
✅ **What Worked Well:**
- Excellent performance during 2020-2021 bull market
- Successfully captured momentum in tech stocks during COVID recovery
- Monthly rebalancing kept transaction costs reasonable
- Strong gains during trending markets

⚠️ **Challenges:**
- Significant drawdown during 2022 bear market (-27.2%)
- Strategy struggled when momentum reversed quickly
- Periods with no trades when no stocks had positive momentum
- Vulnerable to market-wide corrections

### **Trading Activity**
- **Total Trades**: Approximately 50+ trades over 4 years
- **Average Trade Duration**: ~30-60 days per position
- **Most Active Periods**: 2020-2021 during high volatility and strong trends

### **Risk Characteristics**
- **Best Year**: 2020 with exceptional gains during market recovery
- **Worst Period**: 2022 bear market with substantial losses
- **Recovery**: Strategy shows ability to recover after drawdowns

## 💡 **Key Takeaways**

This simple momentum strategy demonstrates the classic momentum trading profile:
1. **Trend Following**: Captures strong upward trends effectively
2. **Market Dependent**: Performance highly correlated with overall market conditions  
3. **Whipsaw Risk**: Vulnerable during choppy, directionless markets
4. **Simplicity**: Despite being basic, it achieved solid long-term returns

The strategy turned $100,000 into $287,139 over 4 years, nearly tripling the investment through systematic momentum capture!

---

## Human

Deploy it live with the paper trading brokerage.

---

## Assistant

I'll deploy the momentum strategy for live paper trading. First, let me check the available live trading options and then set up the deployment.
```
This block is not supported on your current device yet.
```

Perfect! I can see there are available live trading nodes. I'll use a basic L1-1 node which should be sufficient for our simple momentum strategy. Now I'll create a live deployment with paper trading using QuantConnect's paper brokerage.
```
This block is not supported on your current device yet.
```

Excellent! 🎉 The momentum strategy has been successfully deployed live with paper trading!

## ✅ **Live Deployment Summary**

### **Deployment Details**
- **Status**: ✅ **RUNNING** 
- **Deploy ID**: `L-927d32e1077c990a706db35baae3e0de`
- **Launch Time**: July 29, 2025 at 17:50:45 UTC
- **Brokerage**: Paper Trading (QuantConnect Paper Brokerage)
- **Starting Capital**: $100,000 USD
- **Data Center**: NY7 (New York)

### **Strategy Configuration**
- **Universe**: 8 tech stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX)
- **Rebalancing**: Monthly on first trading day
- **Position Size**: Equal weight among top 3 momentum stocks
- **Entry Rule**: Only stocks with positive 20-day momentum
- **Exit Rule**: Sell when stocks fall out of top 3 or turn negative

### **Live Trading Features**
- **Real-time execution** with market hours trading
- **Automatic rebalancing** on the first trading day of each month
- **Risk management** through position limits and momentum filters  
- **Performance tracking** with live charts and statistics
- **Paper trading** means no real money at risk while testing the strategy

### **What Happens Next**
1. **Market Hours**: Strategy will execute during regular market hours (9:30 AM - 4:00 PM ET)
2. **Next Rebalance**: Will occur on the first trading day of August 2025
3. **Monitoring**: You can track performance, trades, and logs in real-time
4. **Orders**: All trades will be executed as market orders with paper money

### **Monitoring Your Strategy**
- Check the QuantConnect live trading dashboard for real-time updates
- View performance charts, trade execution, and strategy logs
- Monitor monthly rebalancing activities and position changes

Your momentum strategy is now live and will start making paper trades based on the monthly momentum signals! 📈
