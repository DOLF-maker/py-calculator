# include the library that you want
# the functions, basically the code

# build a Risk & Reward Ratio of Options


# User Inputs
def user_input():
    max_profit = float(input("What is the Max Profit: \n"))
    premium_paid = float(input("Enter Premium Paid: \n"))
    premium_gain = float(input("Enter Premium Gain: \n"))
    return max_profit, premium_paid, premium_gain

# Function Definition
def rrr_calculator(max_profit, premium_paid, premium_gain):
    max_loss = (premium_paid - premium_gain) * 100

    if max_loss == 0:
        return "Max Loss cannot be zero, failed to calculate RRR!"

    rrr = (max_profit / max_loss) * 100

    return {
        "Max Profit": max_profit,
        "Max Loss": max_loss,
        "RRR (%)": rrr
    }

# Main Execution
if __name__ == "__main__":
    # Get user inputs
    max_profit, premium_paid, premium_gain = user_input()
    
    # Calculate RRR
    result = rrr_calculator(max_profit, premium_paid, premium_gain)
    
    # Check and print results
    if isinstance(result, str):
        print(result)  # Print error message if max_loss is zero
    else:
        print(f"Max Profit: {result['Max Profit']}")
        print(f"Max Loss: {result['Max Loss']}")
        print(f"RRR (%): {result['RRR (%)']}")
