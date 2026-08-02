class HybridExpertSystem:
    def __init__(self):
        # 1. Facts (Working Memory)
        self.facts = {
            "User_Budget": None,
            "Primary_Use": None,
            "Portability_Need": None,
            "OS_Preference": None,
            "Software_Requirement": None,
            # Inferred facts
            "Required_GPU": None,
            "Performance_Tier": None,
            "Required_RAM": None,
            "Display_Quality": None,
            "Max_Weight": None,
            "Screen_Size": None,
            "Max_Price_Limit": None
        }
        
        # 2. Rules (Knowledge Base)
        # Each rule has a condition (antecedent) and an action (consequent)
        self.rules = [
            {
                "id": "Rule_1",
                "antecedent": lambda f: f["Primary_Use"] == "Gaming",
                "consequent": {"Required_GPU": "Dedicated_High_End", "Performance_Tier": "High"}
            },
            {
                "id": "Rule_2",
                "antecedent": lambda f: f["Primary_Use"] == "Content_Creation" or f["Software_Requirement"] == "Heavy_3D_Rendering",
                "consequent": {"Required_RAM": "16GB_or_more", "Display_Quality": "High_Color_Accuracy"}
            },
            {
                "id": "Rule_3",
                "antecedent": lambda f: f["Portability_Need"] == "High",
                "consequent": {"Max_Weight": "Under_3_lbs", "Screen_Size": "13_to_14_inch"}
            },
            {
                "id": "Rule_4",
                "antecedent": lambda f: f["User_Budget"] == "Low",
                "consequent": {"Max_Price_Limit": "600_USD", "Required_GPU": "Integrated"}
            }
        ]
        
        self.recommendations = []

    def gather_inputs(self):
        print("=== Laptop Recommendation Expert System (Forward & Backward Chaining) ===")
        print("Please enter your preferences:\n")

        self.facts["User_Budget"] = input("1. Budget (Low / Medium / High): ").strip().capitalize()
        self.facts["Primary_Use"] = input("2. Primary Use (Gaming / Office_Work / Content_Creation / Student): ").strip().title()
        self.facts["Portability_Need"] = input("3. Portability Need (High / Low): ").strip().capitalize()
        self.facts["OS_Preference"] = input("4. OS Preference (Windows / MacOS / Linux): ").strip().capitalize()
        self.facts["Software_Requirement"] = input("5. Software Requirement (Heavy_3D_Rendering / Standard_Office / Programming): ").strip().title()

    def forward_chaining(self):
        """Forward Chaining: Data-driven approach (Facts -> Rules -> Inferences)"""
        print("\n--- Running Forward Chaining Inference ---")
        inferred_something = True
        
        while inferred_something:
            inferred_something = False
            for rule in self.rules:
                try:
                    if rule["antecedent"](self.facts):
                        for key, val in rule["consequent"].items():
                            if self.facts[key] != val:
                                self.facts[key] = val
                                print(f"[Forward Chaining] Fired {rule['id']}: Set {key} = {val}")
                                inferred_something = True
                except Exception:
                    continue

    def backward_chaining_check(self, goal_key, goal_value):
        """Backward Chaining: Goal-driven approach (Hypothesis -> Check requirements)"""
        print(f"\n[Backward Chaining] Testing Goal: Is '{goal_key}' == '{goal_value}' achievable?")
        
        # If the fact is already true in working memory
        if self.facts.get(goal_key) == goal_value:
            print(f"-> Goal verified successfully via Working Memory: {goal_key} = {goal_value}")
            return True
            
        # Search rules that conclude this goal
        for rule in self.rules:
            if goal_key in rule["consequent"] and rule["consequent"][goal_key] == goal_value:
                print(f"-> Checking antecedent conditions for {rule['id']}...")
                # To prove this rule, we check if its antecedent evaluates to true with current/user facts
                try:
                    if rule["antecedent"](self.facts):
                        print(f"-> Goal '{goal_key} == {goal_value}' validated through {rule['id']}.")
                        return True
                except Exception:
                    continue
                    
        print(f"-> Goal '{goal_key} == {goal_value}' could not be proven.")
        return False

    def generate_recommendations(self):
        """5. Recommendation Engine using combined inferred facts and backward validation"""
        
        # Rule 5: Budget Student / Office User
        if (self.facts["Primary_Use"] in ["Student", "Office_Work"]) and self.facts["User_Budget"] == "Low":
            self.recommendations.append("Acer Aspire 5 or HP Chromebook")

        # Rule 6: High-End Gamers (Using Backward Chaining to verify Performance Tier)
        if self.facts["User_Budget"] == "High" and self.facts["OS_Preference"] == "Windows":
            is_high_perf = self.backward_chaining_check("Performance_Tier", "High")
            if is_high_perf:
                self.recommendations.append("ASUS ROG Zephyrus G14 / Lenovo Legion Pro")

        # Rule 7: Creative Professionals (Using Backward Chaining to verify Display Quality)
        if self.facts["OS_Preference"] == "MacOS":
            is_color_accurate = self.backward_chaining_check("Display_Quality", "High_Color_Accuracy")
            if is_color_accurate:
                self.recommendations.append("Apple MacBook Pro 16-inch (M-Series)")

        # Rule 8: Mobile Programmers
        if self.facts["Software_Requirement"] == "Programming" and self.facts["Portability_Need"] == "High" and self.facts["User_Budget"] == "Medium":
            self.recommendations.append("Dell XPS 13 or MacBook Air M2")

        # Fallback recommendations
        if not self.recommendations:
            if self.facts["User_Budget"] == "Medium":
                self.recommendations.append("General Mid-Range All-Rounder (e.g., Lenovo IdeaPad Pro)")
            elif self.facts["User_Budget"] == "High":
                self.recommendations.append("Premium Ultrabook (e.g., Microsoft Surface Laptop)")
            else:
                self.recommendations.append("Entry-Level Budget Laptop")

    def display_results(self):
        print("\n" + "="*50)
        print(" EXPERT SYSTEM RECOMMENDATION RESULTS ")
        print("="*50)
        print(f"-> User Budget: {self.facts['User_Budget']}")
        print(f"-> Primary Use: {self.facts['Primary_Use']}")
        print(f"-> Portability: {self.facts['Portability_Need']}")
        print(f"-> OS Preference: {self.facts['OS_Preference']}")
        print(f"-> Software Needed: {self.facts['Software_Requirement']}")
        print("-" * 50)
        print("Recommended Laptop(s):")
        for rec in set(self.recommendations):
            print(f" • {rec}")
        print("="*50)

if __name__ == "__main__":
    system = HybridExpertSystem()
    system.gather_inputs()
    system.forward_chaining()
    system.generate_recommendations()
    system.display_results()