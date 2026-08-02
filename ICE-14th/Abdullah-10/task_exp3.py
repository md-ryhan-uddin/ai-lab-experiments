# ==============================================================
# RULE-BASED EXPERT SYSTEM FOR LAPTOP RECOMMENDATION
# Using User Preferences
# ==============================================================
# Components:
# 1. Facts
# 2. Production Rules
# 3. Forward Chaining
# 4. Backward Chaining
# 5. Recommendation
# ==============================================================

# -----------------------------
# FACTS
# -----------------------------
facts = {}

print("=" * 65)
print("      RULE-BASED EXPERT SYSTEM FOR LAPTOP RECOMMENDATION")
print("=" * 65)

facts["budget"] = input("Budget (Low/Medium/High): ").strip().lower()
facts["purpose"] = input("Purpose (Gaming/Programming/Office/Design): ").strip().lower()
facts["portability"] = input("Need Portability? (yes/no): ").strip().lower()
facts["battery"] = input("Need Long Battery Life? (yes/no): ").strip().lower()
facts["storage"] = input("Need High Storage? (yes/no): ").strip().lower()

# ==============================================================
# PRODUCTION RULES
# ==============================================================

rules = [

    {
        "id": 1,
        "conditions": {"budget": "low", "purpose": "office"},
        "recommendation": "Acer Aspire 3"
    },

    {
        "id": 2,
        "conditions": {"budget": "medium", "purpose": "programming"},
        "recommendation": "Lenovo ThinkPad E14"
    },

    {
        "id": 3,
        "conditions": {"budget": "high", "purpose": "programming"},
        "recommendation": "Apple MacBook Pro"
    },

    {
        "id": 4,
        "conditions": {"budget": "medium", "purpose": "gaming"},
        "recommendation": "ASUS TUF Gaming A15"
    },

    {
        "id": 5,
        "conditions": {"budget": "high", "purpose": "gaming"},
        "recommendation": "ASUS ROG Strix G16"
    },

    {
        "id": 6,
        "conditions": {"budget": "high", "purpose": "design"},
        "recommendation": "Dell XPS 15"
    },

    {
        "id": 7,
        "conditions": {"portability": "yes", "battery": "yes"},
        "recommendation": "MacBook Air M3"
    },

    {
        "id": 8,
        "conditions": {"storage": "yes", "budget": "medium"},
        "recommendation": "HP Pavilion 15 (1TB SSD)"
    },

    {
        "id": 9,
        "conditions": {"budget": "low", "purpose": "programming"},
        "recommendation": "Lenovo IdeaPad Slim 3"
    },

    {
        "id": 10,
        "conditions": {"budget": "medium", "purpose": "office"},
        "recommendation": "Dell Inspiron 15"
    }

]

# ==============================================================
# FORWARD CHAINING
# ==============================================================

print("\n" + "=" * 65)
print("FORWARD CHAINING")
print("=" * 65)

forward_results = []

for rule in rules:

    match = True

    for key, value in rule["conditions"].items():

        if facts.get(key) != value:
            match = False
            break

    if match:
        forward_results.append(rule)

if forward_results:

    for rule in forward_results:

        print(f"Rule {rule['id']} Fired")
        print("Recommendation:", rule["recommendation"])
        print("-" * 40)

else:

    print("No rule matched.")

# ==============================================================
# BACKWARD CHAINING
# ==============================================================

print("\n" + "=" * 65)
print("BACKWARD CHAINING")
print("=" * 65)

goal = input(
    "Enter laptop to verify "
    "(Acer Aspire 3 / Lenovo ThinkPad E14 / Apple MacBook Pro / "
    "ASUS TUF Gaming A15 / ASUS ROG Strix G16 / Dell XPS 15 / "
    "MacBook Air M3 / HP Pavilion 15 (1TB SSD) / "
    "Lenovo IdeaPad Slim 3 / Dell Inspiron 15): "
).strip().lower()

found = False

for rule in rules:

    if rule["recommendation"].lower() == goal:

        found = True

        print("\nChecking Required Facts...\n")

        satisfied = True

        for key, value in rule["conditions"].items():

            if facts.get(key) == value:

                print(f"{key.capitalize()} = {value} ✓")

            else:

                print(f"{key.capitalize()} should be {value} ✗")
                satisfied = False

        if satisfied:

            print("\nGoal Achieved!")
            print("Recommendation is VALID.")

        else:

            print("\nGoal NOT Achieved.")

        break

if not found:

    print("Laptop not found in Knowledge Base.")

# ==============================================================
# FINAL RECOMMENDATION
# ==============================================================

print("\n" + "=" * 65)
print("FINAL RECOMMENDATION")
print("=" * 65)

if forward_results:

    print("Best Recommendation(s):\n")

    for rule in forward_results:

        print(f"Rule {rule['id']} -> {rule['recommendation']}")

else:

    print("No exact recommendation found.")
    print("Suggested Laptop: Lenovo IdeaPad 5")

print("\nThank you for using the Laptop Expert System!")