import yfinance as yf
import requests
import pandas as pd
import time

API_KEY = 'GaflY5JLJfvrueuBGmtZiGNock8W0oq1'

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN',
           'JPM', 'V', 'WMT', 'TSLA', 'UNH', 'XOM']


def get_json_safe(url):
    try:
        r = requests.get(url)
        if r.status_code == 200 and r.text.strip().startswith('['):
            return r.json()
        else:
            print(f" Bad response or empty data from URL: {url}")
            return []
    except Exception as e:
        print(f" Error fetching {url}: {e}")
        return []


def get_fundamentals(ticker):
    profile_url = f'https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={API_KEY}'
    income_url = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit=1&apikey={API_KEY}'
    balance_url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit=1&apikey={API_KEY}'
    cash_url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit=1&apikey={API_KEY}'

    profile = get_json_safe(profile_url)
    income = get_json_safe(income_url)
    balance = get_json_safe(balance_url)
    cash = get_json_safe(cash_url)

    if not profile or not income or not balance or not cash:
        return None  # Skip if anything is empty

    return {
        'ticker': ticker,
        'price': profile[0].get('price', None),
        'pe': profile[0].get('pe', None),
        'pb': profile[0].get('priceToBookRatio', None),
        'roe': profile[0].get('returnOnEquity', None),
        'debt_equity': profile[0].get('debtToEquity', None),
        'fcf': cash[0].get('freeCashFlow', None),
        'net_income': income[0].get('netIncome', None),
        'equity': balance[0].get('totalStockholdersEquity', None)
    }


def score_stock(data):
    if not data:
        return 0

    score = 0
    try:
        if data['pe'] is not None and data['pe'] < 15:
            score += 1
        if data['pb'] is not None and data['pb'] < 1.5:
            score += 1
        if data['roe'] is not None and data['roe'] > 15:
            score += 1
        if data['debt_equity'] is not None and data['debt_equity'] < 0.5:
            score += 1
        if data['fcf'] is not None and data['fcf'] > 0:
            score += 1
    except:
        pass

    return score


results = []
print("Fetching and scoring stocks...\n")

for ticker in tickers:
    print(f"{ticker}")
    data = get_fundamentals(ticker)
    if data:
        data['score'] = score_stock(data)
        results.append(data)
    else:
        print(f"Skipping {ticker} due to incomplete data.")
    time.sleep(1)  # Avoid API rate limits

# Results
df = pd.DataFrame(results)
df_sorted = df.sort_values(by='score', ascending=False)
print("\n Top Value Picks:")
print(df_sorted[['ticker', 'score', 'pe', 'pb',
      'roe', 'debt_equity', 'fcf']].head(5))
