# USD → INR Exchange Rate
Automatically fetches and publishes the current USD to INR exchange rate in this README every hour, powered by ExchangeRate-API and GitHub Actions.

 
**Date:** 

| Base | Target | Rate  |
|:----:|:------:|:-----:|
| USD  | INR    | 85.4301 |

## 🚀 Features

- **Hourly Updates** via a scheduled GitHub Action  
- **Pair Conversion** using ExchangeRate-API’s `/pair` endpoint  
- **Jinja2 Templating** for clean, maintainable README generation  
- **Secure**: API key stored in GitHub Secrets (`EXCHANGE_API_KEY`)  
- **Zero Maintenance**: commits & pushes only when the rate changes 
