stocks={
    'AMZN':3380,
    'AAPL':121,
    'MSFT':219,
    'BIIB':280,
    'QDEL':266,
    'LVGO':144
}
new_stocks= {symbol : price*1.02 for (symbol,price) in stocks.items()}
print(new_stocks)