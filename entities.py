class NPC:
    def __init__(self, name, location_id, default_dialogue):
        self.name = name
        self.location_id = location_id
        self.default_dialogue = default_dialogue
        self.required_clue = None
        self.secret_dialogue = None
        self.is_alibi_broken = False

    def interrogate(self, player):
        print(f"\n 💬 You sit down across from {self.name}....")
        if self.is_alibi_broken:
            print(f"{self.name}: {self.secret_dialogue}")
            return
        if self.required_clue and self.required_clue in player.casefile.evidence:
            self.is_alibi_broken = True
            print(f"🕵️‍♂️ [PRESENT EVIDENCE]: You confront them with the {self.required_clue.upper()}")
            print(f"{self.name} turns pale and breaks down...")
            print(f"{self.name}: {self.secret_dialogue}")

            player.casefile.add_clue(
                f"confession_{self.name.lower()}", 
                f"Admitted lying about their alibi after being confronted with evidence."
            )
        else:
            print(f"{self.name}: {self.default_dialogue}")


def setup_characters():
        harper = NPC(
            "Director Harper", "4",
            "The executive's disappearance is tragic, but corporate operations must continue."
        )
        harper.required_clue = "financial_ledger"
        harper.secret_dialogue = "Fine! I authorized the transfers, but I was forced to. The exec found out!"

        aero = NPC(
            "Aero the Netrunner", "3",
            "Look, clean digital tracks cost money. I don't talk to cops for free."
        )
        aero.required_clue = "encrypted_usb"
        aero.secret_dialogue = "Whoa, where did you find that key? Okay, listen... that executive hired me to wipe his profile before he ran."

        return [harper, aero]
