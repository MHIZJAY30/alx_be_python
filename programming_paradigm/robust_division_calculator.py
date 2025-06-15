def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Try performing division
        result = num / den
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: please enter numeric values only."
    
    except Exception as e:
        return f"Unexpected error: {str(e)}"