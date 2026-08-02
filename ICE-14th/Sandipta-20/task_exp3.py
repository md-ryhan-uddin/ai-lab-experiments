# ==========================================================
#        LAPTOP RECOMMENDATION EXPERT SYSTEM
#      Rule-Based AI using Forward & Backward Chaining
# ==========================================================

# ---------------------------
# USER FACTS
# ---------------------------
user_data = {}

print("=" * 70)
print("         RULE-BASED LAPTOP RECOMMENDATION SYSTEM")
print("=" * 70)

user_data["budget"] = input("Enter Budget (Low/Medium/High): ").lower().strip()
user_data["purpose"] = input("Purpose (Gaming/Programming/Office/Design): ").lower().strip()
user_data["portable"] = input("Need a Portable Laptop? (yes/no): ").lower().strip()
user_data["battery"] = input("Need Good Battery Backup? (yes/no): ").lower().strip()
user_data["storage"] = input("Need Large Storage? (yes/no): ").lower().strip()

# ==========================================================
# KNOWLEDGE BASE (Production Rules)
# ==========================================================

knowledge_base = [

    {
        "rule_no": 1,
        "if": {"budget": "low", "purpose": "office"},
        "then": "Acer Aspire 3"
    },

    {
        "rule_no": 2,
        "if": {"budget": "medium", "purpose": "programming"},
        "then": "Lenovo ThinkPad E14"
    },

    {
        "rule_no": 3,
        "if": {"budget": "high", "purpose": "programming"},
        "then": "Apple MacBook Pro"
    },

    {
        "rule_no": 4,
        "if": {"budget": "medium", "purpose": "gaming"},
        "then": "ASUS TUF Gaming A15"
    },

    {
        "rule_no": 5,
        "if": {"budget": "high", "purpose": "gaming"},
        "then": "ASUS ROG Strix G16"
    },

    {
        "rule_no": 6,
        "if": {"budget": "high", "purpose": "design"},
        "then": "Dell XPS 15"
    },

    {
        "rule_no": 7,
        "if": {"portable": "yes", "battery": "yes"},
        "then": "MacBook Air M3"
    },

    {
        "rule_no": 8,
        "if": {"budget": "medium", "storage": "yes"},
        "then": "HP Pavilion 15 (1TB SSD)"
    },

    {
        "rule_no": 9,
        "if": {"budget": "low", "purpose": "programming"},
        "then": "Lenovo IdeaPad Slim 3"
    },

    {
        "rule_no": 10,
        "if": {"budget": "medium", "purpose": "office"},
        "then": "Dell Inspiron 15"
    }

]

# ==========================================================
# FORWARD CHAINING
# ==========================================================

print("\n" + "=" * 70)
print("FORWARD CHAINING PROCESS")
print("=" * 70)

matched_rules = []

for item in knowledge_base:

    if all(user_data.get(key) == value for key, value in item["if"].items()):
        matched_rules.append(item)

if matched_rules:

    for result in matched_rules:
        print(f"Rule {result['rule_no']} Activated")
        print(f"Recommended Laptop : {result['then']}")
        print("-" * 45)

else:
    print("No matching rule was found.")

# ==========================================================
# BACKWARD CHAINING
# ==========================================================

print("\n" + "=" * 70)
print("BACKWARD CHAINING PROCESS")
print("=" * 70)

target = input(
    "\nEnter Laptop Name to Verify:\n"
    "(Acer Aspire 3, Lenovo ThinkPad E14, Apple MacBook Pro,\n"
    "ASUS TUF Gaming A15, ASUS ROG Strix G16, Dell XPS 15,\n"
    "MacBook Air M3, HP Pavilion 15 (1TB SSD),\n"
    "Lenovo IdeaPad Slim 3, Dell Inspiron 15)\n\n"
    "Laptop: "
).lower().strip()

rule_found = False

for item in knowledge_base:

    if item["then"].lower() == target:

        rule_found = True
        print("\nRequired Conditions:\n")

        success = True

        for key, value in item["if"].items():

            if user_data.get(key) == value:
                print(f"{key.capitalize()} : {value} ✔")

            else:
                print(f"{key.capitalize()} should be '{value}' ✘")
                success = False

        if success:
            print("\nGoal Successfully Verified.")
            print("Recommendation is Correct.")

        else:
            print("\nVerification Failed.")

        break

if not rule_found:
    print("This laptop does not exist in the Knowledge Base.")

# ==========================================================
# FINAL OUTPUT
# ==========================================================

print("\n" + "=" * 70)
print("FINAL LAPTOP RECOMMENDATION")
print("=" * 70)

if matched_rules:

    print("Recommended Laptop(s):\n")

    for laptop in matched_rules:
        print(f"Rule {laptop['rule_no']} : {laptop['then']}")

else:
    print("No exact rule matched.")
    print("Default Recommendation: Lenovo IdeaPad 5")

print("\nThank you for using the Laptop Recommendation Expert System!")