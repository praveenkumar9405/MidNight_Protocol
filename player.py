# Manages the clues and evidence collected by the detective.
class CaseFile:
    def __init__(self):
        self.evidence = {}

    def add_clue(self, clue_id, description):
        if clue_id not in self.evidence:
            self.evidence[clue_id] = description
            print(f"\n🔍 [NEW EVIDENCE ADDED TO THE CASE FILE]: {clue_id.upper()}")
            return True

        else:
            print(f"\n📝 You already noted down the details for: {clue_id.upper()}")
            return False
        
    def display(self):
        print("\n" + "=" * 40)
        print("📂 CURRENT CASE FILE EVIDENCE")
        print("=" * 40)

        if not self.evidence:
            print(" [The board is empty. No evidence collected yet.]")

        for clue_id, desc in self.evidence.items():
            print(f" • {clue_id.upper()}: {desc}")
        print("=" * 40)

# Manages the player's status, resources, and evidence tracking.
class Detective:
    def __init__(self, name):
        self.name = name
        self.hours_left = 24        # Our primary resource countdown
        self.credibility = 100      # Social Currency (Ruined if 0%)
        self.casefile = CaseFile()

    def display_status(self):
        print(f"\n 🕵️‍♂️ Detective: {self.name}")
        print(f"🕒 Time Remaining: {self.hours_left} Hours")
        print(f"🤝 Professional Credibility: {self.credibility}")

    def spend_time(self, amount):
        self.hours_left -= amount
        if self.hours_left <= 0:
            self.hours_left = 0
            return False
        return True
