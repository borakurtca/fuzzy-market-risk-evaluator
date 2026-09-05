# Fuzzy Logic Market Risk Evaluator

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-0.4.2-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

##  Business Overview
In volatile financial markets, risk is rarely binary. Traditional algorithmic trading rules often fail to capture the nuances of market sentiment and price fluctuations. 

This project implements a **Fuzzy Logic Control System** to quantify market uncertainty. By bridging the gap between raw quantitative data (volatility) and qualitative human psychology (news sentiment), it generates a definitive **Risk Score (0-100)**. This pipeline serves as an advanced feature engineering module, designed to feed deterministic risk metrics into downstream machine learning architectures.

## Architecture & Use Case
The engine is structured to process intraday market data for commodities (e.g., COPPER, BRENTOIL, GOLD) fetched via APIs like Hyperliquid, combined with real-time NLP sentiment analysis. 

*   **Input 1: Market Volatility (0-100):** Represents standard deviation or price fluctuations.
*   **Input 2: News Sentiment (-1.0 to 1.0):** Processed RSS feed sentiment scores.
*   **Output: Risk Score (0-100):** A defuzzified, actionable metric generated through centroid calculation.

**Integration Vision:** The resulting Risk Score is optimized to be injected as a high-value feature into predictive models, such as **XGBoost regression engines**, to enhance commodity price forecasting accuracy.

##  Key Features
*   **Non-Linear Decision Making:** Replaces rigid `if-else` thresholds with fluid membership functions (Low, Medium, High).
*   **Expert Rule Encoding:** Encapsulates human analyst logic into mathematical IF-THEN fuzzy rules.
*   **Feature Engineering Pipeline:** Transforms raw, disjointed data into a single, standardized risk metric.

##  Visualizing the Logic
https://github.com/borakurtca/fuzzy-market-risk-evaluator/edit/main/README.md#:~:text=Figure_1.png

##  Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/fuzzy-market-risk-evaluator.git](https://github.com/yourusername/fuzzy-market-risk-evaluator.git)
   cd fuzzy-market-risk-evaluator
