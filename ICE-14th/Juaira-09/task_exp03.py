# ==========================================
# Rule-Based Expert System for Laptop Recommendation
# ==========================================

# -------- FACTS --------
facts = {
    "gaming": False,
    "programming": True,
    "video_editing": False,
    "budget_high": False,
    "portable": True,
    "student": True
}

print("Initial Facts:")
for fact, value in facts.items():
    print(f"{fact} = {value}")

# -------- PRODUCTION RULES --------
rules = [
    # Rule 1
    ("gaming", lambda f: f["gaming"], "Need High GPU"),

    # Rule 2
    ("video_editing", lambda f: f["video_editing"], "Need High RAM"),

    # Rule 3
    ("programming", lambda f: f["programming"], "Need SSD"),

    # Rule 4
    ("portable", lambda f: f["portable"], "Need Lightweight"),

    # Rule 5
    ("budget_high", lambda f: f["budget_high"], "Premium Laptop"),

    # Rule 6
    ("student", lambda f: f["student"], "Budget Laptop"),

    # Rule 7
    ("Gaming Laptop",
     lambda f: "Need High GPU" in f,
     "Gaming Laptop"),

    # Rule 8
    ("Ultrabook",
     lambda f: "Need SSD" in f and "Need Lightweight" in f,
     "Ultrabook")
]

# ==========================================
# FORWARD CHAINING
# ==========================================
print("\n----- Forward Chaining -----")

new_fact_added = True

while new_fact_added:
    new_fact_added = False

    for name, condition, conclusion in rules:
        if condition(facts) and conclusion not in facts:
            facts[conclusion] = True
            print("Rule Fired ->", conclusion)
            new_fact_added = True

print("\nFacts After Forward Chaining:")
for fact in facts:
    print("-", fact)

# ==========================================
# BACKWARD CHAINING
# ==========================================

print("\n----- Backward Chaining -----")

def backward(goal):
    if goal in facts:
        return True

    for name, condition, conclusion in rules:
        if conclusion == goal:
            if condition(facts):
                facts[goal] = True
                return True

    return False

goal = "Ultrabook"

if backward(goal):
    print(goal, "is proved.")
else:
    print(goal, "cannot be proved.")

# ==========================================
# FINAL RECOMMENDATION
# ==========================================

print("\n----- Laptop Recommendation -----")

if "Gaming Laptop" in facts:
    print("Recommendation: Gaming Laptop")
elif "Ultrabook" in facts:
    print("Recommendation: Ultrabook")
elif "Premium Laptop" in facts:
    print("Recommendation: Premium Business Laptop")
elif "Budget Laptop" in facts:
    print("Recommendation: Budget Student Laptop")
else:
    print("Recommendation: Standard Laptop")
