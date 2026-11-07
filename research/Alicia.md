# How Investors Price MU and ASML — Alicia Yau

**Ticket #1** · Research cutoff: Nov 7, 2026 · Prices as of Fri Nov 6, 2026 closes (Nasdaq)

> TL;DR — Both companies are riding the AI chip build-out, but investors price them in opposite ways.
> **Micron** looks *very cheap* (~4.5x forward, ~9x trailing earnings) because the market assumes memory profits are near a cyclical peak.
> **ASML** looks *expensive* (~22x forward, ~35x trailing) because the market trusts its monopoly and multi-year backlog.
> Same industry, same AI demand driver, completely different multiples — that gap is the most useful lesson for our agent.

---

## 0. Basics I learned first (Reading List group 1)

| Concept | What it means | Why it matters here |
|---|---|---|
| **P/E (trailing)** | Price ÷ last 12 months of earnings per share | Backward-looking. For a company whose profits just jumped 9x (MU), trailing P/E lags reality. |
| **Forward P/E** | Price ÷ *expected* next-12-month EPS | What investors actually use for fast-changing companies. Depends heavily on whose estimate you trust. |
| **P/S (price-to-sales)** | Market cap ÷ revenue | Useful when earnings are distorted (peak/trough of a cycle). |
| **Gross / operating margin** | % of revenue left after production costs / after all operating costs | Shows pricing power. MU went from ~40% to 87% gross margin in a year → prices, not volume, drove profits. |
| **Free cash flow (FCF)** | Operating cash flow − capital spending | The cash a business actually generates. FCF yield = FCF ÷ market cap. |
| **DCF** | Value = sum of future free cash flows discounted back to today | The "theoretical" value. Very sensitive to growth and discount-rate assumptions — small input changes swing the answer a lot. |
| **Cyclical vs. secular** | Cyclical = profits rise and fall with supply/demand cycles; secular = steady long-term growth | **Investors deliberately give cyclicals LOW P/Es at the top of the cycle**, because they expect earnings to fall. This explains most of MU vs. ASML. |

---

## 1. Micron Technology (MU)

### What does it sell?
Memory chips. Two main products:
- **DRAM** (short-term working memory, incl. **HBM** — high-bandwidth memory stacked next to AI GPUs like Nvidia's). DRAM was ~$100.7B of $133.2B FY2026 revenue (**~76%**).
- **NAND** (long-term storage, e.g. SSDs in data centers and phones).
- Customers: cloud/hyperscalers, Nvidia (HBM), PC and phone makers, autos. Cloud Memory + Core Data Center ≈ **63% of Q4 revenue**.

Memory is a **commodity-ish product**: Micron, SK Hynix and Samsung make interchangeable chips, so prices swing with supply and demand.

### Key numbers (fiscal year ends early September)

| Metric | Value | Note |
|---|---|---|
| FY2026 revenue | **$133.2B** (+256% YoY) | FY2025 was $37.4B |
| Q4 FY26 revenue | $54.2B (+379% YoY, +31% QoQ) | 14-week quarter (53-week year) — flatters QoQ growth slightly |
| Q4 gross margin (non-GAAP) | **87.0%** | ~40 pts higher than a year earlier |
| Q4 operating margin | ~82% | |
| FY2026 EPS (non-GAAP) | **$75.52** (vs $8.29 FY25) | +811% |
| FY2026 adjusted FCF | $62.3B | Q4 alone $33.2B |
| Cash & investments | ~$73.5B | |
| Q1 FY27 guidance | Rev $61.5B ± $1.5B, GM ~86.25%, EPS $38.15 ± $1 | Beat consensus (~$56.5B rev / ~$36 EPS) |
| FY2027 capex | > $50B (raised) | New cleanrooms, capacity arrives late 2028+ |
| Customer contracts | 26 strategic customer agreements (up from 16), ~$150B remaining performance obligations; >75% of 2027 shipments committed | Key to the "is this time different?" debate |

### Valuation right now (price $690.00 close Nov 6, market cap ≈ $781B)

| Multiple | Value | How I got it |
|---|---|---|
| Trailing P/E | **~9.1x** | $690.00 ÷ $75.52 (Google Finance shows 9.3x using GAAP EPS) |
| Forward P/E (run-rate) | **~4.5x** | $690.00 ÷ ($38.15 × 4) |
| Forward P/E (analyst sources) | ~3.8x – 6x | Depends on whose FY27 estimate is used — sources disagree a lot |
| Trailing P/S | **~5.9x** | $781B ÷ $133.2B (was ~5x a year ago) |
| FCF yield | **~8.0%** | $62.3B ÷ $781B |
| S&P 500 forward P/E (for comparison) | ~19x | |
| MU's 10-yr average forward P/E | ~22x | |

**Interesting:** MU is *cheaper* on P/E than a year ago (22x a year ago → ~9x trailing now) even though the stock is still up a lot over the year — profits grew faster than the price. But it's *more expensive* on P/S (5x → 9x at end of Sept). That's the signature of a cyclical at a profit peak.

### What moved the stock in the past year? (+~273% over the year to Nov 2, before the Nov 5 crash)

| When | Event | Move |
|---|---|---|
| Dec 17, 2025 | FQ1 guidance far above estimates on HBM pricing | Shares up ~12% next morning (Frankfurt) |
| Early May 2026 | Wave of AI demand + memory shortage headlines | +32% in one week — best week since 2008 |
| Jun 25, 2026 | All-time closing high **$1,213** | |
| Sep 30, 2026 | Record Q4 + guidance beat | **Muted/mixed** reaction (sources conflict: ~flat after-hours vs. a big next-day gain). High "whisper" expectations (~$37 EPS) were already priced in |
| October 2026 | China's CXMT competition fears, AI-spending worries, profit-taking | Worst week of 2026 (~−19.5%); −22% for the month |
| Nov 2, 2026 | Japanese peer **Kioxia** gives weak outlook | MU −5.8% to $833.59 on someone else's news |
| Nov 4, 2026 | Continued memory-stock selling | MU −7.0% to $795.23 while the S&P 500 rose 1.6% |
| Nov 5, 2026 | Midterm election results raised fears that local opposition could slow U.S. data-center construction; Philadelphia Semiconductor Index −12% | MU **−18%** to $656.39 — down ~26% for the week |
| Nov 6, 2026 | Chip stocks rebound | MU +5.1% to **$690.00**; still ~45% below its 52-wk high of $1,255 |

**Main driver overall:** memory *prices*. AI servers need huge amounts of HBM/DRAM, supply can't grow fast (new fabs take years), so prices and margins exploded.

### Cheap or expensive? Why?
**Most investors think MU is "cheap for a reason."**
- **Bull case:** At ~4–6x forward earnings the stock already assumes a bust. Long-term contracts (with price floors/ceilings on ~¾ of contract revenue) and a supply shortage expected through 2027–28 could make earnings more durable than past cycles → the market may re-rate it higher. Micron is also expected to ramp up stock buybacks after Dec 9, when CHIPS Act buyback restrictions expire. Average analyst targets ≈ $1,400–1,630 depending on the source (more than double the current price).
- **Bear case:** Memory has always boomed and busted. Micron (and rivals) are spending >$50B to add capacity; when supply catches up, prices fall fast. One scenario analysis shows EPS dropping to ~$72 in a severe reversal (vs ~$150+ in the base case). Plus: CXMT competition, AI capex slowdown risk, $12.7B of customer deposits are refundable, inventory days at 129.
- **My take:** The low P/E is not a bargain signal by itself — for cyclicals, the time to worry is when P/E looks lowest. The key question is *how long margins stay near 87%.*

---

## 2. ASML Holding (ASML)

### What does it sell?
The machines that print chip patterns onto silicon wafers (**lithography**).
- **EUV** (extreme ultraviolet) machines — ASML is the **only company in the world** that makes them. Every leading-edge chip (Nvidia GPUs via TSMC, HBM via SK Hynix/Micron/Samsung) needs them. Low-NA EUV output ~65 systems in 2026 vs 44 in 2025.
- **High-NA EUV** — next generation; Intel is the early adopter. Real financial impact from 2028.
- **DUV** — older, cheaper lithography (big in China).
- **Installed Base Management (IBM)** — service, upgrades, and parts for machines already sold. Q3: €3.29B (~28% of sales, +68% YoY) — the steady, high-margin "razor blades."
- Customers: TSMC, Samsung, Intel, SK Hynix, Micron, Chinese fabs (~20% of sales).

### Key numbers (calendar year)

| Metric | Value | Note |
|---|---|---|
| Q3 2026 revenue | **€11.7B** (+55% YoY) | Systems €8.37B + IBM €3.29B; 113 new systems shipped |
| Q3 gross margin | **57.5%** | Up from 51.6% a year ago; beat guidance thanks to upgrades |
| Q3 net income | €5.0B (incl. ~€0.5B one-off gain on Mistral AI stake) | Strip it out → EPS ≈ €11.84 vs €12.95 reported |
| Q3 free cash flow | €11.35B | Boosted by customer prepayments (lumpy) |
| FY2026 guidance | **€44–45B**, GM ~56% | Was €34–39B in January → raised twice |
| Q4 guidance | €14.2–15.2B, GM ~57% | Midpoint ~26% above Q3 — steep ramp to execute |
| Backlog/demand | Record €13.2B bookings in Q4 2025; stopped reporting bookings in 2026; says 2027–28 supply **won't fully meet demand**; some customers want 2029–30 slots | Capacity +30% in 2027, studying more for 2028 |
| Buyback | Up to €12B through 2028 (~€4.1B used in Q3) | |

### Valuation right now (US shares $1,424.75 close Nov 6, market cap ≈ $549B)

| Multiple | Value | Source |
|---|---|---|
| Trailing P/E | **~35x** | Yahoo Finance at Nov 6 close; 5-yr median ~41x, range ~25x–67x |
| Forward P/E | **~22x** | TIKR's 24.6x at the Oct 30 close, scaled for the ~9% drop since (my estimate) |
| P/E on 2027 estimates | ~23x | MarketScreener's ~25x, scaled the same way (my estimate) |
| P/S | ~13x | De Belegger's ~14x, scaled the same way (my estimate) |
| Expected EPS growth | ~50%/yr for next 2 years (analysts) | → PEG ≈ 0.8 |

### What moved the stock in the past year? (+44% YTD as of Oct 30, before the Nov 5 selloff)

| When | Event | Move |
|---|---|---|
| Jan 28, 2026 | Record **€13.2B** Q4 bookings (≈2x estimates), €12B buyback, raised 2026 outlook; also announced it would stop reporting bookings | +7.5% to record €1,309 intraday |
| Jul 15, 2026 | Raised 2026 guidance to €43–45B; capacity +30% plan | (guidance-driven re-rating) |
| Oct 14, 2026 | Record Q3, margin beat, Q4 guide above consensus, "supply won't meet 2027–28 demand" | Split reaction: ~+2% in Amsterdam, ~−3.9% on Nasdaq — much of the good news was already priced in |
| Oct 30, 2026 | **Intel's** weak PC outlook triggered a global chip selloff | −6.1% to €1,413 on someone else's news |
| Nov 5, 2026 | Same midterm/data-center selloff that hit Micron | US shares **−9.3%** to $1,356.65 |
| Nov 6, 2026 | Chip stocks rebound | +5.0% to **$1,424.75**; ~29% below its 52-wk high of ~$2,000 (Jun 30) |

**Main driver overall:** expectations for chipmakers' capital spending. When TSMC/memory makers say they'll build more fabs, ASML's future orders go up.

### Cheap or expensive? Why?
**Most investors think ASML is "expensive but deserved" — debate is about how much is already priced in.**
- **Bull case:** Monopoly on EUV, sold out through 2028, pricing power, high-margin service business, ~50%/yr EPS growth → ~22x forward looks reasonable (PEG < 1). Average analyst target ≈ $2,140–2,200 (~50% upside).
- **Bear case:** Trailing ~35x already prices in a lot; some fair-value models call it overvalued. Risks: TSMC said it's being "prudent" for 2027; ~20% China exposure + possible U.S. DUV export limits; U.S. Section 232 tariffs (a Jan 2026 proclamation put 25% tariffs on certain advanced chips and left broader tariffs, which could cover chipmaking equipment, open depending on trade negotiations); equipment orders are lumpy; Q4 needs a big ramp.
- **My take:** ASML is priced like a quality *compounder*, not a cyclical, because its backlog and monopoly make earnings visible years ahead. The risk isn't the business — it's that the multiple compresses if chipmakers slow spending.

---

## 3. MU vs ASML side by side

| | Micron (MU) | ASML |
|---|---|---|
| Role in AI supply chain | Sells the memory chips | Sells the machines that make all chips |
| Competitive position | 1 of 3 (SK Hynix, Samsung) + CXMT rising | Monopoly in EUV |
| Revenue visibility | Months–1 yr (improving with contracts) | Multiple years (backlog, prepayments) |
| Forward P/E | ~4.5x | ~22x |
| Trailing P/E | ~9x | ~35x |
| Drop in the Nov 5 selloff | −18% | −9% |
| Gross margin | 87% (record, likely peak-ish) | 57.5% (rising) |
| Market's view | Cyclical at peak → discount | Durable compounder → premium |
| Biggest swing factor | Memory prices | Customer capex plans |

**Connection:** Micron is an ASML *customer*. Micron raising capex to >$50B is good news for ASML's orders — but also the very thing that could eventually crash memory prices for Micron.

---

## 4. 2–3 things I think our agent should look at

1. **Guidance & expectation surprises, not just reported results.**
   MU beat on every metric on Sep 30 but the stock barely moved because the "whisper" number was higher; ASML's biggest jump came from bookings ~2x estimates. Feature idea: compare company guidance vs. consensus (and vs. prior guidance), and track guidance-raise history (ASML: €34–39B → €43–45B → €44–45B).

2. **Cycle-aware valuation instead of a raw P/E.**
   A low P/E made MU look "cheap" right as it fell 22% in a month. Feature idea: flag cyclical stocks and show P/E alongside P/S, gross-margin vs. historical range, inventory days, and the industry's capex plans. A rule like "low P/E + record margins + rising industry capex = caution" would have helped.

3. **Peer & supply-chain read-through.**
   Both of my stocks had big recent one-day drops (MU −5.8% on Nov 2, ASML −6.1% on Oct 30) because of *another* company's earnings (Kioxia, Intel). Feature idea: build a relationship map (peers, customers, suppliers) so the agent links a peer's earnings/news to related tickers — e.g., memory peers → MU; TSMC/Intel/memory-maker capex → ASML. This could also feed our chart-pattern model as context for why a pattern formed. It should cover macro/policy news too: on Nov 5, fears about U.S. data-center restrictions after the midterms knocked MU down 18% and ASML down 9% in one day. Note that the cyclical stock (MU) fell twice as hard.

*(Bonus data note: ASML stopped reporting quarterly bookings in 2026 — our agent can't rely on a metric existing forever and should fall back on proxies like contract liabilities/customer prepayments.)*

---

## Sources
- [Micron Q4 FY26 summary — Quartr](https://quartr.com/events/micron-technology-inc-mu-q4-2026_3Yxg2NZC)
- [Micron Q4 FY26 post-call — Quartr](https://quartr.com/events/micron-technology-inc-mu-q4-2026-post-call_3Yxg2fmK)
- [Micron Q4 earnings analysis & FY27 stress test — INDmoney](https://www.indmoney.com/blog/us-stocks/micron-stock-q4-earnings-analysis-mu)
- [Micron Q4 vs estimates — XTB](https://www.xtb.com/en/market-analysis/record-after-record-micron-smashes-q4-results-server-overload-crashes-website-stock-surges-post-market)
- [What Just Happened To Micron Stock? (Nov 3) — Trefis](https://www.trefis.com/articles/622310/what-just-happened-to-micron-stock/2026-11-03)
- [Micron falls 5.8% (Nov 2) — Gotrade](https://www.heygotrade.com/en/news/micron-mu-stock-news-november-3-2026/)
- [Why Micron stock looks cheap — Nasdaq/Motley Fool](https://www.nasdaq.com/articles/why-micron-stock-looks-cheap-after-record-year)
- [Kioxia red flag for Micron — Barchart](https://www.barchart.com/story/news/3616480/1-japanese-company-just-waved-a-red-flag-for-micron-stock-how-to-play-it-here)
- [Micron best week since 2008 (May) — Barron's via Tiger](https://www.itiger.com/news/2634463085)
- [Micron sinks 7% while market rallies (Nov 4) — AskTraders](https://www.asktraders.com/analysis/micron-sinks-7-while-market-rallies/)
- [Micron buybacks after Dec 9, consensus target — MarketBeat](https://www.marketbeat.com/instant-alerts/price-micron-technology-nasdaq-mu-shares-down-58-whats-next-2026-11-02/)
- [Micron FY26 detail — Earnings Whispers](https://earningswhispers.com/article/MU/2609307205)
- [Micron rebounds after 18% crash (Nov 6) — GuruFocus via TradingView](https://www.tradingview.com/news/gurufocus:eb1e2f298094b:0-micron-stocks-rebound-8-06-after-18-crash-as-memory-names-bounce/)
- [Micron Nov 6 close — Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/11/06/stock-market-today-nov-6-micron-technology-jumps-as-chip-stocks-rebound-from-thursday-s-rout/)
- [Micron quote, market cap, P/E — Google Finance](https://www.google.com/finance/quote/MU:NASDAQ)
- [Micron worst week of 2026 — AllMind](https://allmind.ai/news/fef2e93bff0ed1fe9aa3906c30f89ab4ab52d168db54d27940ebb7e59a2006ce)
- [ASML Q3 2026 results — StorageNewsletter (press release)](https://www.storagenewsletter.com/?p=306155)
- [ASML Q3 earnings analysis — INDmoney](https://www.indmoney.com/blog/us-stocks/asml-stock-q3-earnings-analysis)
- [ASML Q3 guidance history — braindetox](https://braindetox.kr/en/posts/asml_orders_ai_investment_slowdown_2026.html)
- [ASML fell 6% in Intel's chip rout (Nov 2) — TIKR](https://www.tikr.com/blog/asml-fell-6-in-intels-chip-rout-its-ceo-says-supply-will-not-fully-meet-the-demand)
- [ASML valuation ratios — De Belegger](https://www.debelegger.nl/en/stock/ASML.AS)
- [ASML record bookings (Jan 28) — Fintool](https://fintool.com/news/asml-record-bookings-ai-demand)
- [ASML lifts outlook on record orders — Reuters via Yahoo](https://finance.yahoo.com/news/asml-q4-bookings-beat-expectations-061654428.html)
- [ASML quote, Nov 6 close, P/E — Yahoo Finance](https://sg.finance.yahoo.com/quote/ASML/)
- [ASML Nov 5 close — CNBC](https://www.cnbc.com/quotes/ASML)
- [ASML Q3 stock reaction — investingLive](https://investinglive.com/stocks/asml-says-2027-and-2028-supply-will-fall-short-of-demand-as-q3-sales-hit-a-record/)
- [ASML Q3 results at a glance — Beancount](https://beancount.io/blog/2026/10/20/asml-fy2026-q3-earnings-analysis)
- [ASML P/E estimates — MarketScreener](https://www.marketscreener.com/quote/stock/ASML-HOLDING-6268/)
- [Section 232 semiconductor proclamation (Jan 2026) — EY](https://taxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors)
- [Section 232 semiconductors summary — Perkins Coie via Mondaq](https://mondaq.com/unitedstates/international-trade-investment/1744466/presidential-action-on-semiconductors-and-critical-minerals-under-section-232)
