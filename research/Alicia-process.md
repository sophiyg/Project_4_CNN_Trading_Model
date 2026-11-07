# Research Process Log — Ticket #1 (MU, ASML)

How the research in `research/alicia.md` was done, so teammates can reproduce or extend it.

## Step 1 — Break down the ticket
Turned the ticket into a checklist for each company:
- [x] What does it sell?
- [x] Which numbers do investors use to value it, and what are they now?
- [x] What moved the stock most in the past year?
- [x] Do investors think it's cheap or expensive, and why?
- [x] 2–3 things our agent should look at
- [x] README + questions/blockers

## Step 2 — Learn the basics
Reviewed P/E (trailing vs forward), P/S, margins, free cash flow, DCF, and the cyclical-vs-secular distinction. The last one ended up being the key to explaining why MU and ASML trade at such different multiples. Summarized in §0 of the write-up.

## Step 3 — Pull the latest fundamentals (primary results first)
| Company | Latest report | Searches used |
|---|---|---|
| MU | Fiscal Q4 2026 (reported Sep 30, 2026) | "Micron earnings fiscal Q4 2026 results guidance" |
| ASML | Q3 2026 (reported Oct 14, 2026) | "ASML Q3 2026 results bookings guidance" |

Rule I followed: prefer numbers that trace back to the company's own press release / earnings call (Quartr summaries, press-release reprints), then use analyst/news articles for interpretation.

## Step 4 — Pull current valuation and price
Searches: "Micron stock November 2026 valuation P/E", "ASML stock November 2026 valuation forward P/E", "Micron stock this week memory stocks Kioxia November 2026".
- MU price: $833.59 (Nov 2) → $795.23 (Nov 4) → final: **$690.00 (Nov 6 close)**, market cap ≈ $781B
- ASML price: €1,413 / $1,565.90 (Oct 30) → final: **$1,424.75 (Nov 6 close, Nasdaq)**, market cap ≈ $549B

## Step 5 — Calculate my own ratios (instead of trusting one site)
Sources disagreed on MU's forward P/E (5.5x–12x), so I computed it myself:

```
MU trailing P/E   = 690.00 / 75.52          = 9.1x
MU run-rate fwd PE = 690.00 / (38.15 × 4)   = 4.5x
MU FCF yield      = 62.31B / 780.7B         = 8.0%
MU P/S            = 780.7B / 133.19B        = 5.9x
ASML fwd P/E      = 24.6 × (1424.75/1565.90) = 22.4x  (scaled from TIKR's Oct 30 figure)
MU DRAM share     = 100.68B / 133.19B       = 76%
ASML Q4 guide vs Q3 = 14.7B / 11.66B − 1    = +26%
ASML service share  = 3.29B / 11.66B        = 28%
```
For ASML, trailing P/E comes from Yahoo Finance (~35x at Nov 6). Forward P/E, 2027 P/E and P/S came from data sites (TIKR, MarketScreener, De Belegger) as of Oct 30, so I scaled them down by the ~9% price drop since then.

## Step 6 — Build the "what moved the stock" timeline
Searched for the biggest single events: earnings dates, guidance changes, and large one-day moves (e.g. "ASML shares January 2026 record bookings stock jump"). Logged each event with date and % move.

Pattern noticed: the most recent big drops for **both** stocks came from *other* companies' news (Kioxia for MU, Intel for ASML) → became agent feature idea #3.

## Step 7 — Cheap vs. expensive
For each stock, collected the bull case and bear case from multiple outlets, then wrote my own take. Avoided relying on any single "fair value" model because they disagree widely and are very assumption-sensitive.

## Step 8 — Turn findings into agent features
Asked: "What would have helped someone predict or explain these moves?" → three features (guidance surprises, cycle-aware valuation, peer read-through).

## Step 9 — Check work
- Re-ran ratio arithmetic in Python.
- Cross-checked key figures across ≥2 sources (MU Q4 revenue/EPS: Quartr, XTB, Earnings Whispers; ASML Q3 revenue/margin: press release reprint, INDmoney, braindetox).
- Flagged conflicts instead of hiding them (MU's post-earnings reaction; forward P/E range).

## Step 10 — Fact-check pass and updates (Nov 7)
- Checked the Section 232 claim: the investigation ended with a Jan 14, 2026 proclamation (25% tariff on certain advanced chips; broader tariffs possible later). Rewrote that risk.
- Refreshed both prices to the Nov 6 closes and recomputed all ratios.
- Added the Nov 5 selloff (midterm results → data-center restriction fears; MU −18%, ASML −9%) and the Nov 6 rebound to both timelines.
- Corrected ASML's Oct 14 earnings reaction (split: up in Amsterdam, down on Nasdaq).
- Added Micron's expected buybacks after Dec 9 (CHIPS Act restriction ends).

## Known limitations
- No live price feed; numbers are a snapshot as of early Nov 2026.
- Some sources are secondary summaries of filings, not the filings themselves.
- This is a learning exercise, not investment advice.
