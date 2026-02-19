import pandas as pd
f = pd.read_csv("fear_greed_index.csv")
f['timestamp'] = pd.to_datetime(f['timestamp'], unit='s')
df = pd.read_csv("historical_data.csv")

# 2. Convert date (string DD-MM-YYYY → datetime)
f['date'] = pd.to_datetime(f['date'], format='%d-%m-%Y')
# 4. Choose one as the "daily key" (they should match)
# For example, use timestamp_date



f_daily = (
    f.groupby(f['date'])
     .mean(numeric_only=True)
     .reset_index()
)
f.to_csv("fear_greedupdated.csv", index=False)
df['Timestamp IST'] = pd.to_datetime(df['Timestamp IST'], format='%d-%m-%Y %H:%M')
df['Date'] = df['Timestamp IST'].dt.date
daily_summary = df.groupby('Date').agg({
    'Size Tokens':'sum',
    'Size USD':'sum',
    'Fee':'sum',
    'Closed PnL':'sum'
}).reset_index()
df['Timestamp UTC'] = df['Timestamp IST'].dt.tz_localize('Asia/Kolkata').dt.tz_convert('UTC')
df['Date UTC'] = df['Timestamp UTC'].dt.date
df.to_csv("traderupdated.csv", index=False)
# f['date'] = pd.to_datetime(f['date'], errors='coerce')
# f['timestamp'] = pd.to_datetime(f['timestamp'], unit='s')

# f_daily = f.groupby(f['date'].dt.date).mean(numeric_only=True).reset_index(inplace=False)
# f_daily.rename(columns={'date':'Date'}, inplace=True)
# print(f_daily)
# print(f['timestamp'])