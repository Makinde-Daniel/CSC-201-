def get_tax_brackets():
    """Return the tax brackets for different filing statuses.
    
    Returns:
        dict: A dictionary where keys are status codes and values are lists of
              (upper_limit, tax_rate) tuples for each tax bracket.
    """
    return {
        0: [  # Single
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
        ],
        1: [  # Married filing jointly / Qualified widow(er)
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
        ],
        2: [  # Married filing separately
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (float("inf"), 0.35)
        ],
        3: [  # Head of household
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (float("inf"), 0.35)
        ]
    }

def compute_tax(status, income):
    if not 0 <= status <= 3:
        raise ValueError("Invalid filing status. Must be between 0 and 3.")
    if income < 0:
        raise ValueError("Income cannot be negative.")
    if income == 0:
        return 0.0
        
    brackets = get_tax_brackets()
    tax = 0.0
    previous_limit = 0.0

    for limit, rate in brackets[status]:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return round(tax, 2)  # Round to nearest cent

def get_valid_status():
    while True:
        try:
            status = int(input("Enter filing status (0-3): "))
            if 0 <= status <= 3:
                return status
            print("Error: Status must be between 0 and 3.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_income():
    """Prompt user for a valid income amount."""
    while True:
        try:
            income = float(input("Enter taxable income: $"))
            if income >= 0:
                return income
            print("Error: Income cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("Tax Calculator")
    print("=" * 40)
    print("Filing Status:")
    print("0 - Single")
    print("1 - Married filing jointly or qualified widow(er)")
    print("2 - Married filing separately")
    print("3 - Head of household")
    print("-" * 40)
    
    try:
        status = get_valid_status()
        income = get_valid_income()
        
        tax = compute_tax(status, income)
        
        print("\n" + "=" * 40)
        print(f"Filing Status: {['Single', 'Married filing jointly', 'Married filing separately', 'Head of household'][status]}")
        print(f"Taxable Income: ${income:,.2f}")
        print(f"\nTotal Tax Owed: ${tax:,.2f}")
        print("=" * 40)
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
