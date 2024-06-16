# Black-Scholes Option Pricing Model

This Python script calculates the price of a European call option using the Black-Scholes option pricing model. It includes a class definition for the derivative, a custom exception for input validation, and a function to compute the option price.

## Class Definition

### `Derivative`

This class represents a financial derivative with the following attributes:
- `underlying_price`: The current price of the underlying asset.
- `strike_price`: The strike price of the option.
- `time_to_maturity`: The time to maturity of the option (in years).
- `volatility`: The volatility of the underlying asset.
- `risk_free_rate`: The risk-free interest rate.

#### Example:
```python
my_derivative = Derivative(100.0, 95.0, 1.0, 0.2, 0.05)