import math

# Define a class for the derivative
class Derivative:
    def __init__(self, underlying_price, strike_price, time_to_maturity, volatility, risk_free_rate):
        self.underlying_price = underlying_price
        self.strike_price = strike_price
        self.time_to_maturity = time_to_maturity
        self.volatility = volatility
        self.risk_free_rate = risk_free_rate

# Custom exception for input validation
class InvalidInput(Exception):
    pass

# Pricing function using Black-Scholes model for European call option
def black_scholes(derivative):
    if any(param <= 0 for param in [derivative.underlying_price, derivative.strike_price,
                                    derivative.time_to_maturity, derivative.volatility, derivative.risk_free_rate]):
        raise InvalidInput("Invalid input: parameters must be positive")

    d1 = (math.log(derivative.underlying_price / derivative.strike_price) +
          (derivative.risk_free_rate + 0.5 * derivative.volatility ** 2) * derivative.time_to_maturity) / \
         (derivative.volatility * math.sqrt(derivative.time_to_maturity))
    d2 = d1 - derivative.volatility * math.sqrt(derivative.time_to_maturity)

    call_price = derivative.underlying_price * normal_cdf(d1) - \
                 derivative.strike_price * math.exp(-derivative.risk_free_rate * derivative.time_to_maturity) * normal_cdf(d2)

    return call_price

# Standard normal cumulative distribution function (approximation)
def normal_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

# Example usage
my_derivative = Derivative(100.0, 95.0, 1.0, 0.2, 0.05)

try:
    option_price = black_scholes(my_derivative)
    print(f"Option Price: {option_price:.2f}")
except InvalidInput as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")