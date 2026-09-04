def recommend_laptop(budget, use, portability, gaming, battery):
    if budget == "Low" and use == "Student":
        return "Chromebook"
    elif budget == "Medium" and use == "Office":
        return "Dell Inspiron"
    elif budget == "High" and use == "Programming":
        return "MacBook Pro"
    elif gaming == "Yes" and budget == "High":
        return "ASUS ROG"
    elif gaming == "Yes" and budget == "Medium":
        return "Acer Nitro 5"
    elif portability == "High" and battery == "Long":
        return "MacBook Air"
    elif battery == "Long" and budget == "Medium":
        return "LG Gram"
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