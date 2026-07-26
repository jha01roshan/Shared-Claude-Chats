# Calculating Jill's 2026 federal income tax

- Source: https://claude.ai/share/ef62408a-6502-4d70-82be-6ea46a4a4cc3
- Author: Harry
- Created: 2026-03-20
- Messages: 4

---

## Human

Please solve this tax quiz. Jill, single, age 63, has these incomes in 2026: 

$30,000 from Social Security; 
$10,000 from interest and pre-tax IRA withdrawals; 
$37,000 from qualified dividends and long-term capital gains; and
$1,000 from muni bond interest.

Jill contributes $4,400 to her HSA and donates $1,500 in cash to charities. What's Jill's federal income tax in 2026? 

It's important to calculate it accurately. Please use tax amounts only for 2026 and only from official IRS sources.

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have all the official 2026 figures I need. Here's the full step-by-step solution.

---

## Jill's 2026 Federal Income Tax

### Key 2026 Parameters (IRS Official Sources)

| Item | Amount |
|---|---|
| Standard deduction, single | $16,100 |
| Additional std. deduction, age 65+ | $2,050 — **Jill is 63, does NOT qualify** |
| OBBBA senior deduction | $6,000 — **age 65+ only, Jill does NOT qualify** |
| HSA self-only contribution limit | $4,400 ✓ (Jill's contribution hits it exactly) |
| 10% bracket | $0–$12,400 |
| 12% bracket | $12,401–$50,400 |
| 0% LTCG rate threshold | Taxable income ≤ $49,450 |
| 15% LTCG rate | $49,451 and above (until the 20% threshold) |

---

### Step 1 — Income Classification

| Source | Amount | Type |
|---|---|---|
| Social Security | $30,000 | Potentially taxable (see Step 2) |
| Interest + IRA withdrawals | $10,000 | Ordinary income |
| Qualified dividends + LTCG | $37,000 | Preferentially taxed |
| Muni bond interest | $1,000 | **Federal tax-exempt** (but counts in SS formula) |

---

### Step 2 — Taxable Social Security (IRC §86)

**Provisional income** = (non-SS income − above-line deductions) + muni interest + ½ SS

> = ($10,000 + $37,000 − $4,400 HSA) + $1,000 + $15,000 = **$58,600**

Provisional income > $34,000 threshold → up to 85% of SS is taxable.

**Formula (upper tier):**
> Taxable SS = min(85% × $30,000 , &nbsp; 85% × ($58,600 − $34,000) + 50% × $9,000)
> = min($25,500 , $20,910 + $4,500)
> = min($25,500 , **$25,410**)
> = **$25,410**

---

### Step 3 — Adjusted Gross Income (AGI)

| | |
|---|---|
| Ordinary income (interest + IRA) | $10,000 |
| Taxable Social Security | $25,410 |
| Qualified dividends + LTCG | $37,000 |
| **Gross income** | **$72,410** |
| Less: HSA deduction (above-the-line) | −$4,400 |
| **AGI** | **$68,010** |

*(Muni bond interest and the $1,500 charitable donation are not in AGI — the donation is an itemized deduction, which Jill won't use.)*

---

### Step 4 — Deductions

Jill is 63, so no age-65+ add-on.

- Standard deduction: **$16,100**
- Itemized deductions: $1,500 (charity only) — *far less than standard deduction, so she takes the standard*

---

### Step 5 — Taxable Income

| | |
|---|---|
| AGI | $68,010 |
| Less: standard deduction | −$16,100 |
| **Taxable income** | **$51,910** |

**Composition** (deductions reduce ordinary income first):
- Ordinary income: $35,410 − $20,500 (HSA + std. deduction) = **$14,910**
- LTCG / Qualified dividends: **$37,000**
- Total: **$51,910** ✓

---

### Step 6 — Tax on Ordinary Income ($14,910)

| Bracket | Income | Rate | Tax |
|---|---|---|---|
| 10% | $12,400 | 10% | $1,240.00 |
| 12% | $2,510 ($14,910 − $12,400) | 12% | $301.20 |
| **Total ordinary tax** | | | **$1,541.20** |

---

### Step 7 — Tax on LTCG / Qualified Dividends ($37,000)

The LTCG stacks *on top of* ordinary income: it occupies taxable income from $14,910 → $51,910.

- 0% rate ceiling: **$49,450**
- LTCG in 0% bracket: $49,450 − $14,910 = **$34,540** → $0 tax
- LTCG in 15% bracket: $51,910 − $49,450 = **$2,460** → $369 tax

| Rate | Amount | Tax |
|---|---|---|
| 0% | $34,540 | $0 |
| 15% | $2,460 | **$369.00** |

---

### Step 8 — Other Taxes

- **AMT**: Exemption ~$90,000 (single); Jill's income is far below — **no AMT**
- **NIIT (3.8%)**: Applies only above $200,000 MAGI — **no NIIT**

---

### Final Answer

| Component | Tax |
|---|---|
| Tax on ordinary income | $1,541.20 |
| Tax on LTCG / qualified dividends | $369.00 |
| **Total federal income tax** | **$1,910** |

---

### A Few Notable Observations

The $1,500 charitable donation provides **zero federal tax benefit** since Jill uses the standard deduction, and it isn't deductible above the line. If Jill were 65 instead of 63, she'd gain both the $2,050 additional standard deduction *and* the new $6,000 OBBBA senior deduction (subject to phase-out), which would dramatically reduce her tax. The LTCG/QD income is very tax-efficient here — only $2,460 out of $37,000 is taxed (at 15%), with the bulk sheltered by the 0% bracket.

---

## Human

I heard that cash donations are deductible for people using the standard deduction, starting in 2026, up to a limit.

---

## Assistant

```
This block is not supported on your current device yet.
```

You're right, and I missed that — good catch. The OBBBA created a new deduction for this starting in 2026.

Beginning in the 2026 tax year, non-itemizers can deduct cash donations to certain charities — up to **$1,000 for single filers** or $2,000 for married couples filing jointly. Donations to Donor-Advised Funds and supporting organizations don't qualify, but direct cash gifts to public charities do.

There's one important nuance for Jill's calculation: this deduction doesn't reduce your AGI — unlike the HSA deduction. It reduces taxable income, but sits below the AGI line (similar in position to the standard deduction). This means it doesn't affect the Social Security taxability calculation we already ran.

### Revised Calculation

Jill donated $1,500 in cash, so she can deduct **$1,000** (the single-filer cap).

| | |
|---|---|
| AGI (unchanged) | $68,010 |
| Less: standard deduction | −$16,100 |
| Less: non-itemizer charitable deduction | −$1,000 |
| **Revised taxable income** | **$50,910** |

**Composition:**
- Ordinary income: $14,910 − $1,000 = **$13,910**
- LTCG/QD: **$37,000**

**Tax on ordinary income ($13,910):**
- 10% × $12,400 = $1,240.00
- 12% × $1,510 = $181.20
- Subtotal: **$1,421.20**

**Tax on LTCG ($37,000), stacked from $13,910 → $50,910:**
- 0% rate up to $49,450: $49,450 − $13,910 = $35,540 → **$0**
- 15% rate: $50,910 − $49,450 = $1,460 → **$219.00**

### Revised Federal Income Tax: **$1,640**

The $1,000 charitable deduction saves Jill $270 in tax (the $1,000 deduction reduces ordinary income taxed at 12% for $120, and shifts $1,000 of LTCG from the 15% bracket down to the 0% bracket for another $150). Not huge, but real money for a straightforward cash donation.
