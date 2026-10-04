# represents a physical city or room within the city
class Location:
    def __init__(self, name, description, travel_cost = 2):
        self.name = name
        self.description = description
        self.travel_cost = travel_cost
        self.clues_hidden = {}
        self.is_locked = False

    def search_room(self, player):
        print(f"\n 🕵️‍♂️ You conduct a thorough search of the {self.name}")
        if not self.clues_hidden:
            print("You look carefully, but find nothing new of value")
            return
        clues_found = list(self.clues_hidden.keys())
        for clue_id in clues_found:
            desc = self.clues_hidden[clues_id]
            success = player.case_file.add_clue(clue_id, desc)
            if success:
                del self.clues_hidden[clue_id]


# Generates the game locations and hides clues inside them
def setup_world():
        safehouse = Location(
            "P.I. Safehouse",
            "Your neon-lit office. A corkboard sits on the wall with red strings.",
            travel_cost = 0)

        penthouse = Location(
            "Executive Petnhouse",
            "The upscale apartment where the excecutives was last seen. everything is untouched.",
        )

        club = Location(
            "Neon Grid Club",
            "A loud techno-bar flooded with synth music and holographic displays."
            )
        omnicorp = Location(
            "Omnicorp HQ",
            "The massive, Cold monolithic headquarters of the tech syndicate."
        )

        omnicorp.is_locked = True   # High security Area

        # Hide Specific clue data inside each room's dict
        penthouse.clues_hidden["Encrypted_USB"] = (
            "A secure thumb drive found inside a hollowed-out book on the desk."
        )
        penthouse.clues_hidden["Shattered glass"] = (
            "Micro-fractures on the balcony door showing signs of foreced entry."
        )
        club.clues_hidden["hacker_alias"] = (
            "A bartender mentions a netrunner named 'Aero' was tracking the exec's bank account."
        )
        omnicorp.clues_hidden["Financial_ledger"] = (
            "A core database file showing massive illegal transfers to an offshore grid account."
        )

        world_map = {
            "1": safehouse,
            "2": penthouse,
            "3": club,
            "4": omnicorp
        }

        return world_map





