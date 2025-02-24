from model import calculate_volatility, get_options
from download_parse import load_data


def main():
    print("Black-Scholes Model")
    # Iterate over the stocks "APPL" and "MSFT" and "GOOGL" first iteration 1 year
    for stock in ["AAPL", "MSFT", "GOOGL"]:
        # Load data
        df = load_data(stock, "2020-01-01", "2021-01-01")

        # Calculate volatility
        daily_volatility, annualized_volatility = calculate_volatility(df, stock)

        # Print results
        print(f"Daily Volatility for {stock}: {daily_volatility}")
        print(f"Annualized Volatility for {stock}: {annualized_volatility}")

        # Calculate options
        option = get_options(
            df[stock].iloc[-1],
            1,
            df[stock].iloc[-1] + (df[stock].iloc[-1] * 0.07),
            0.05,
            annualized_volatility,
        )
        option = option + df[stock].iloc[-1]
        print(f"Option price for {stock}: {option}")

        if stock == "AAPL":
            # Market price
            market_price = 170
        elif stock == "MSFT":
            market_price = 270
        else:
            market_price = 120

        # Absolute difference
        absolute_diff = abs(option - market_price)

        # Percentage difference
        percentage_diff = (absolute_diff / market_price) * 100

        print(f"Absolute Difference: {absolute_diff}")
        print(f"Percentage Difference: {percentage_diff:.2f}%")

    for stock in ["AAPL", "MSFT", "GOOGL"]:
        # Load data
        df = load_data(stock, "2021-01-01", "2022-01-01")

        # Calculate volatility
        daily_volatility, annualized_volatility = calculate_volatility(df, stock)

        # Print results
        print(f"Daily Volatility for {stock}: {daily_volatility}")
        print(f"Annualized Volatility for {stock}: {annualized_volatility}")

        # Calculate options
        option = get_options(
            df[stock].iloc[-1],
            1,
            df[stock].iloc[-1] + (df[stock].iloc[-1] * 0.07),
            0.05,
            annualized_volatility,
        )
        option = option + df[stock].iloc[-1]
        print(f"Option price for {stock}: {option}")

        if stock == "AAPL":
            # Market price
            market_price = 175
        elif stock == "MSFT":
            market_price = 360
        else:
            market_price = 170

        # Absolute difference
        absolute_diff = abs(option - market_price)

        # Percentage difference
        percentage_diff = (absolute_diff / market_price) * 100

        print(f"Absolute Difference: {absolute_diff}")
        print(f"Percentage Difference: {percentage_diff:.2f}%")

    for stock in ["AAPL", "MSFT", "GOOGL"]:
        # Load data
        df = load_data(stock, "2022-01-01", "2023-01-01")

        # Calculate volatility
        daily_volatility, annualized_volatility = calculate_volatility(df, stock)

        # Print results
        print(f"Daily Volatility for {stock}: {daily_volatility}")
        print(f"Annualized Volatility for {stock}: {annualized_volatility}")

        # Calculate options
        option = get_options(
            df[stock].iloc[-1],
            1,
            df[stock].iloc[-1] + (df[stock].iloc[-1] * 0.07),
            0.05,
            annualized_volatility,
        )
        option = option + df[stock].iloc[-1]
        print(f"Option price for {stock}: {option}")

        if stock == "AAPL":
            # Market price
            market_price = 250
        elif stock == "MSFT":
            market_price = 360
        else:
            market_price = 190

        # Absolute difference
        absolute_diff = abs(option - market_price)

        # Percentage difference
        percentage_diff = (absolute_diff / market_price) * 100

        print(f"Absolute Difference: {absolute_diff}")
        print(f"Percentage Difference: {percentage_diff:.2f}%")


if __name__ == "__main__":
    main()
