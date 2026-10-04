import os
import sys
from player import Detective
from entities import setup_characters
from locations import setup_world
from hacking import run_hacking_minigame
from exceptions import MidNightProtocolException, TimeExpiredError, CredibilityRuinedError, LocationLockedError

def clear_screen():
    """ Clear the terminal screen  for a Clean UI Feel"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_help():
    """ Print the available terminal commands. """
    print("\n" + "=" * 40)
    print("🤖 TERMINAL COMMAND INTERFACE")
    print("=" * 40)
    print(" • status      - Display your detective profile and time left.")
    print(" • map         - Check available districts and destination costs.")
    print(" • travel      - Move to a different district.")
    print(" • search      - Thoroughly scan the current room for evidence (Costs 2 hrs).")
    print(" • talk        - Interrogate suspects present in this district.")
    print(" • casefile    - Open your notebook to inspect collected evidence.")
    print(" • hack        - Attempt to bypass firewalls if you are stuck.")
    print(" • accuse      - Go to the department and close the game (ENDGAME).")
    print(" • quit        - Abort the investigation.")
    print("=" * 40)


def main():
    clear_screen()
    print("=" * 60)
    print("       🌃 WELCOME TO MIDNIGHT PROTOCOL: THE NEON SYNDICATE 🌃")
    print("=" * 60)

    player_name = input("🕵️‍♂️ Enter your Detective name: ").strip()
    if not player_name:
        player_name = "JD_Praveen"

    # Intialize the core engines
    player = Detective(player_name)
    world_map = setup_world()
    suspects = setup_characters()

    # Start at the Detectice's safehouse (ID: "1")
    current_location = world_map["1"]

    clear_screen()
    display_help()


    # Main Game Loop
    while True:
        try:
            # Continual global resource checks
            if player.hours_left <= 0:
                raise TimeExpiredError()
            if player.credibility <= 0:
                raise CredibilityRuinedError()

            print(f"\n📍 CURRENT LOCATION: {current_location.name.upper()}")
            cmd = input("⚡ MN_PROTOCOL//> ").strip().lower()

            if cmd == "quit":
                print(f"\n🔌 Disconnecting from the matrix... GoodBye!")
                break
            elif cmd == "help":
                display_help()
            elif cmd == "status":
                player.display_status()
            elif cmd == "casefile":
                player.casefile.display()
            elif cmd == "map":
                print("\n" + "=" * 50)
                print("🌐 AVAILABLE NETWORK DISTRICTS")
                print("=" * 50)
                for loc_id, loc in world_map.items():
                    status = "🔒 LOCKED" if loc.is_locked else "🔓 OPEN"
                    print(f" [{loc_id}] {loc.name} ({status}) | Travel Cost: {loc.travel_cost} hrs")
                    print(f"     Description: {loc.description}")
                print("=" * 50)

            elif cmd == "travel":
                print("\nWhere do you want to route travel to?")
                for loc_id, loc in world_map.items():
                    print(f" [{loc_id}] - [{loc.name}]")

                choice = input("Enter District ID: ").strip()
                if choice not in world_map:
                    print("❌ INVALID NODE: That district path does not exist.")
                    continue

                target_location = world_map[choice]

                if target_location.is_locked:
                    # Logic: If player has the "confession_aero_the_netrunner", they can pass OmniCorp HQ
                    if choice == "4" and "confession_aero_the_netrunner" in player.case_file.evidence:
                        print("\n🔓 ACCESS GRANTED: You use Aero's decrypted profile keys to bypass OmniCorp's gates!")
                        target_location.is_locked = False
                    else:
                        raise LocationLockedError(target_location.name)

                # Deduct time and travel
                cost = target_location.travel_cost
                if player.spend_time(cost):
                    current_location = target_location
                    print(f"\n🚀 Transiting to {current_location.name}... Consumed {cost} hour(s).")
                else:
                    raise TimeExpiredError()

            elif cmd == "search":
                current_location.search_room(player)

            elif cmd == "talk":
                # Find NPCs in the current room ID
                current_id = "1"
                for k, v in world_map.items():
                    if v == current_location:
                        current_id = k
                local_npcs = [npc for npc in suspects if npc.location_id == current_id]

                if not local_npcs:
                    print("\n💨 There is no one around in this district to talk to.")
                    continue

                print("\nSuspects present in this area:")
                for idx, npc in enumerate(local_npcs):
                    print(f" [{idx + 1}] {npc.name}")

                npc_choice = input("Select suspect number to interrogate: ").strip()
                if not npc_choice.isdigit() or int(npc_choice) < 1 or int(npc_choice) > len(local_npcs):
                    print("❌ Invalid selection.")
                    continue

                chosen_npc = local_npcs[int(npc_choice) - 1]
                chosen_npc.interrogate(player)

            elif cmd == "hack":
                # Let player hack a firewall to extract information or unlock gates manually
                print("\n🔗 Booting up remote proxy exploit...")
                success = run_hacking_minigame(player)
                if success:
                    # Reward: Player breaks down OmniCorp security grid directly via the hack!
                    if world_map["4"].is_locked:
                        world_map["4"].is_locked = False
                        print("📡 REMOTE TRACE SUCCESSFUL: OmniCorp HQ security mainframes are now compromised and UNLOCKED!")
                    else:
                        print("💾 DATA NODE SNIFFED: Firewall bypassed, but no further locked networks found.")

            elif cmd == "accuse":
                 # Trigger Endgame Phase Sequence
                print("\n" + "🚨 " * 10)
                print("      CRITICAL DOSSIER SUBMISSION: FINAL ACCUSATION")
                print("" + "🚨 " * 10)
                print("You stand before the Bureau Chief. A wrong accusation completely ruins your career.")
                
                print("\nWho is the real architect behind the executive's disappearance?")
                print(" [1] Director Harper (Corporate Insider)")
                print(" [2] Aero the Netrunner (Digital Mercenary)")

                suspect_pick = input("Select suspect [1-2]: ").strip()

                if suspect_pick == "1":
                    # Harper is guilty, but we need both pieces of evidence to prove it!
                    has_ledger = "financial_ledger" in player.case_file.evidence
                    has_confession = "confession_director_harper" in player.case_file.evidence

                    if has_ledger and has_confession:
                        print("\n🏆 CASE CLOSED SUCCESFULLY! 🏆")
                        print("You lay down the Financial Ledger and Director Harper's signed confession.")
                        print("The board is cornered. Harper breaks into tears as tactical officers move in.")
                        print(f"Outstanding job, Detective {player.name}! You saved the sector from corporate warfare.")
                        print(f"Final Stats -> Remaining Time: {player.hours_left} hrs | Credibility: {player.credibility}%")
                        sys.exit(0)
                    else:
                        print("\n❌ CASE DISMISSED: You accused Harper, but lacked the hard evidence to support it!")
                        player.credibility -= 50
                        print("The corporate lawyers laughed you out of court. Lose 50% Credibility.")
                else:
                    print("\n❌ WRONG ACCUSATION: Aero was hired to clear data tracks, but didn't organize the kidnap!")
                    player.credibility -= 50
                    print("Your false lead allowed the real criminal to slip away. Lose 50% Credibility.")

            else:
                print("⚠️ SYSTEM COMMAND ERROR: Unknown syntax protocol. Type 'help' for valid parameters.")

        # Custom Exception State Handling Catch Blocks
        except TimeExpiredError as e:
            print(f"\n{e.message}")
            print("💀 GAME OVER: The case went cold. You failed to expose the Syndicate.")
            sys.exit(0)
            
        except CredibilityRuinedError as e:
            print(f"\n{e.message}")
            print("💀 GAME OVER: Your reputation is ruined. Hand over your badge.")
            sys.exit(0)
            
        except LocationLockedError as e:
            print(f"\n{e.message}")
            print("💡 HINT: Interrogate suspects or use the 'hack' system to get access clearances.")

        except MidNightProtocolException as e:
            print(f"\n⚠️ SYSTEM ANOMALY: {e.message}")

if __name__ == "__main__":
    main()




   




                   


