def convert(amount: float, rate: float) -> float:

    #invalid input types
    if not isinstance(amount, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Amount and rate must be numerical values.")
    
    #invalid amounts
    if amount is None or rate is None:
        raise ValueError("Amount and rate cannot be None.")
    
    #amounts are positive numbers
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    elif amount == 0:
        return 0.0
    
    #rate is greater than zero
    if rate <= 0:
        raise ValueError("Rate must be over zero.")

    return amount * rate
