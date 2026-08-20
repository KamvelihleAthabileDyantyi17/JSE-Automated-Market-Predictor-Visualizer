# 📈 JSE Automated Market Predictor & Visualizer

## Overview
An automated Extract, Transform, Load (ETL) pipeline and technical analysis tool designed to track Johannesburg Stock Exchange (JSE) equities and international markets. 

Built to run autonomously in a Linux environment, this system fetches daily closing data, calculates momentum indicators (like RSI and Moving Averages), and generates a color-coded Excel dashboard with embedded charts to highlight potential buy/sell signals without manual intervention.

## 🛠 Tech Stack
* **Language:** Python 3
* **Data Processing:** `pandas`, `pandas_ta` (Technical Analysis)
* **API/Data Ingestion:** `yfinance` (Yahoo Finance API)
* **Visualization/Output:** `xlsxwriter` (Automated Excel generation)
* **Automation:** Bash (Shell Scripting), Linux Cron

## 🚀 Features
* **Automated Data Ingestion:** Uses the `yfinance` API to pull daily historical and closing prices for specified ticker symbols (e.g., `NPN.JO`, `SBK.JO`).
* **Technical Analysis Engine:** 
  * Calculates the 50-day and 200-day Simple Moving Averages (SMA) to identify Golden Crosses.
  * Computes the Relative Strength Index (RSI) to flag "Oversold" (<30) or "Overbought" (>70) conditions.
* **Algorithmic Signal Generation:** Assigns a "Strong Buy", "Hold", or "Sell" label to each equity based on the calculated technical indicators.
* **Visual Excel Dashboard:** Dynamically generates a `.xlsx` report featuring bar charts, line graphs, and conditional formatting (Green for buy signals, Red for risk) directly from Python.
* **Hands-Off Execution:** A master Bash script (`run_analyzer.sh`) activates the virtual environment, executes the Python logic, archives the generated report with a timestamp, and logs system errors. Scheduled via Cron to run every weekday at 17:30 SAST.

## 📂 Project Structure
```text


├── .github/                     # GitHub configuration/workflows
├── .venv/                       # Your local Python virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   ├── .gitignore
│   └── pyvenv.cfg
├── reports/                     # Output directory for daily dashboards
│   ├── JSE_Market_Report_2026-08-11.csv
│   └── JSE_Market_Report_2026-08-11.xlsx
├── src/                         # Main source code directory
│   ├── __pycache__/             # Compiled Python files
│   │   └── excel_generator.cpython-314.pyc
│   ├── analyzer.py              # Main Python script for data fetching & logic
│   ├── config.json              # List of tickers to track
│   ├── excel_generator.py       # Builds the dashboard
│   └── test.py                  # Environment/connection test script
├── EnviromentSetup.png          # Setup reference image
├── jse_predictor_logo.png       # Project branding/logo
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
