"""
Rule-Based Expert System for Laptop Recommendation

Facts:
1. Budget
2. Primary Use
3. Portability
4. Gaming Requirement
5. Battery Life Requirement

Production Rules:
1. If budget is Low and use is Student -> Chromebook
2. If budget is Medium and use is Office -> Dell Inspiron
3. If budget is High and use is Programming -> MacBook Pro
4. If gaming is Yes and budget is High -> ASUS ROG
5. If gaming is Yes and budget is Medium -> Acer Nitro 5
6. If portability is High and battery is Long -> MacBook Air
7. If battery is Long and budget is Medium -> LG Gram
8. Otherwise -> HP Pavilion
"""

def recommend_laptop(budget, use, portability, gaming, battery):
    """
    Returns a laptop recommendation based on user preferences.
    """

    # Rule 1
    if budget == "Low" and use == "Student":
        return "Chromebook"

    # Rule 2
    elif budget == "Medium" and use == "Office":
        return "Dell Inspiron"

    # Rule 3
    elif budget == "High" and use == "Programming":
        return "MacBook Pro"

    # Rule 4
    elif gaming == "Yes" and budget == "High":
        return "ASUS ROG"

    # Rule 5
    elif gaming == "Yes" and budget == "Medium":
        return "Acer Nitro 5"

    # Rule 6
    elif portability == "High" and battery == "Long":
        return "MacBook Air"

    # Rule 7
    elif battery == "Long" and budget == "Medium":
        return "LG Gram"

    # Rule 8
    else:
        return "HP Pavilion"


def main():
    print("=" * 45)
    print("     Laptop Recommendation Expert System")
    print("=" * 45)

    print("\nEnter the following details:")

    budget = input("Budget (Low/Medium/High): ").title()
    use = input("Primary Use (Student/Office/Programming): ").title()
    portability = input("Portability (Low/High): ").title()
    gaming = input("Gaming? (Yes/No): ").title()
    battery = input("Battery Life (Short/Long): ").title()

    recommendation = recommend_laptop(
        budget,
        use,
        portability,
        gaming,
        battery
    )

    print("\n" + "=" * 45)
    print("Recommended Laptop:", recommendation)
    print("=" * 45)


if __name__ == "__main__":
    main()