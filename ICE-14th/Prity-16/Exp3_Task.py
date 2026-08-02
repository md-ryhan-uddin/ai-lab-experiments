# ==========================================================
# AI TASK
# Rule-Based Expert System for Laptop Recommendation
# Using Facts, Production Rules, Forward Chaining
# and Backward Chaining
# ==========================================================

print("=" * 65)
print("      SMART LAPTOP RECOMMENDATION EXPERT SYSTEM")
print("=" * 65)

# -------------------------------
# FACTS (User Preferences)
# -------------------------------
facts = {}

facts["budget"] = input("Enter Budget (low/medium/high): ").lower()
facts["purpose"] = input("Enter Purpose (student/programming/gaming/office/content): ").lower()
facts["portability"] = input("Need High Portability? (yes/no): ").lower()
facts["battery"] = input("Need Long Battery? (yes/no): ").lower()
facts["os"] = input("Preferred OS (windows/linux/mac): ").lower()

print("\nFACTS")
for key, value in facts.items():
    print(f"{key} = {value}")

# ---------------------------------------------------------
# Production Rules
# ---------------------------------------------------------
rules = [

("Rule 1",
 lambda f: f["budget"]=="high" and f["purpose"]=="gaming",
 "ASUS ROG Zephyrus G16"),

("Rule 2",
 lambda f: f["budget"]=="medium" and f["purpose"]=="gaming",
 "Lenovo LOQ 15"),

("Rule 3",
 lambda f: f["budget"]=="low" and f["purpose"]=="student",
 "Acer Aspire 5"),

("Rule 4",
 lambda f: f["purpose"]=="office" and f["battery"]=="yes",
 "MacBook Air M3"),

("Rule 5",
 lambda f: f["purpose"]=="programming" and f["os"]=="windows",
 "Dell XPS 15"),

("Rule 6",
 lambda f: f["purpose"]=="programming" and f["os"]=="linux",
 "Lenovo ThinkPad E14"),

("Rule 7",
 lambda f: f["purpose"]=="content",
 "MacBook Pro M4"),

("Rule 8",
 lambda f: f["portability"]=="yes",
 "ASUS ZenBook 14 OLED")

]

# ---------------------------------------------------------
# Forward Chaining
# ---------------------------------------------------------
print("\n" + "=" * 65)
print("FORWARD CHAINING")
print("=" * 65)

recommendation = None
fired_rule = None

for rule_name, condition, laptop in rules:
    if condition(facts):
        print(rule_name, "FIRED")
        recommendation = laptop
        fired_rule = rule_name
        break

if recommendation is None:
    recommendation = "HP Pavilion 15"
    fired_rule = "Default Rule"

print("\nForward Chaining Result")
print("Recommendation :", recommendation)

# ---------------------------------------------------------
# Backward Chaining
# ---------------------------------------------------------
print("\n" + "=" * 65)
print("BACKWARD CHAINING")
print("=" * 65)

goal = recommendation

found = False

for rule_name, condition, laptop in rules:
    if laptop == goal:
        if condition(facts):
            print("Goal Verified :", goal)
            print("Matched Rule :", rule_name)
            found = True
            break

if not found:
    print("Goal verified using Default Rule.")

# ---------------------------------------------------------
# Final Recommendation
# ---------------------------------------------------------
print("\n" + "=" * 65)
print("FINAL RECOMMENDATION")
print("=" * 65)

print("Recommended Laptop :", recommendation)
print("Decision Rule :", fired_rule)

print("\nThank you for using the Expert System.")