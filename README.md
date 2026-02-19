Overview
This project analyzes trader behavior across different market sentiments using daily trading metrics and Fear & Greed sentiment data.  
It is divided into three parts: **Data Prep (Part A)**, **Analysis (Part B)**, and **Actionable Strategies (Part C)**.

⚙️ Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/anuragrawattt/Trader-behavior-insights.git
cd Trader-behavior-insights
```

How to Run
Part A — Data Preparation
Open notebooks/PartA.ipynb in Jupyter Notebook or VS Code.
This notebook cleans raw trades, handles duplicates, and generates daily metrics.

Part B — Sentiment Analysis
Run notebooks/PART-B.ipynb.
This merges metrics with sentiment data, compares performance across sentiment categories, and generates charts/tables.
Outputs are saved automatically into:
- outputs/charts/ (PNG plots)
- outputs/tables/ (CSV summaries)

Part C — Actionable Strategies
Open notebooks/PART-C.ipynb.
This notebook contains written insights and rules of thumb based on the analysis.
No code is required — just strategic recommendations.

📂 Project Structure
Trader-behavior-insights/
│── data/          # raw input files
│── notebooks/     # Part A, B, C notebooks
│── outputs/       # charts + tables
│── README.md      # overview + setup + insights

📊 ## Deliverables
## 📄 Summary

### Methodology
- Collected raw trading metrics (`daily_metrics.csv`) and sentiment data (`fear_greedupdated.csv`).
- Cleaned and standardized timestamps, handled duplicates, and ensured consistent formats.
- Merged datasets by date to align trader performance with sentiment classification.
- Aggregated metrics by sentiment categories (Extreme Fear, Fear, Neutral, Greed, Extreme Greed).
- Segmented traders by leverage, trade frequency, and consistency to identify behavioral patterns.
- Visualized results with bar plots and box plots, and exported summary tables for reproducibility.

### Insights
- **PnL & Win Rate:** Performance weakens during Fear days, while Greed days show slightly stronger outcomes.
- **Leverage:** Traders tend to use higher leverage in Greed conditions, amplifying both gains and risks.
- **Position Sizes:** USD exposure shrinks in Fear, but token counts don’t always shrink proportionally — hidden risk.
- **Bias:** Long positions dominate in Greed, shorts dominate in Fear, showing herd‑driven sentiment shifts.
- **Trader Segments:** Frequent traders smooth volatility better than infrequent ones; consistent traders outperform inconsistent ones.

### Strategy Recommendations
1. **Dynamic Position Scaling:** On Fear days, scale positions by token count rather than USD value to avoid hidden overexposure.  
2. **Bias‑Triggered Trade Caps:** When long/short bias exceeds 70%, cap trades in the dominant direction to prevent herd‑driven over‑concentration.  

These recommendations provide actionable rules of thumb that go beyond generic “reduce leverage” advice, offering unique safeguards tailored to observed data patterns.
Performance on Fear vs Greed Days
###Insights
- If PnL is lower on Fear days, it suggests traders struggle in risk‑off sentiment.
- If Win Rate drops on Fear days, it shows more losing trades.
- If Leverage is higher on Greed days, traders are more aggressive when sentiment is positive.

Behavior Changes Based on Sentiment
 ###Insights
- If trade frequency is higher on Greed days, traders chase opportunities.
- If long/short ratio shifts, it shows bias (e.g., more longs on Greed days).
- Larger Size USD on Greed days = traders risk more when confident.

### Insights
- **PnL & Win Rate:** Performance weakens during Fear days, while Greed days show slightly stronger outcomes.
- **Leverage:** Traders tend to use higher leverage in Greed conditions, amplifying both gains and risks.
- **Position Sizes:** USD exposure shrinks in Fear, but token counts don’t always shrink proportionally — hidden risk.
- **Bias:** Long positions dominate in Greed, shorts dominate in Fear, showing herd‑driven sentiment shifts.
- **Trader Segments:** Frequent traders smooth volatility better than infrequent ones; consistent traders outperform inconsistent ones.

  
