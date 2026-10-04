import random

def run_hacking_minigame(player):
    """
    Triggers a Firewall-Hacking Minigame.
    The player must guess a unique 3-digit security node bypass key.
    Each attemp costs the detective time.
    """
    print("\n"+"=" * 50)
    print("      🌐 INITIATING CYBER-DECRYPTOR v4.02")
    print("=" * 50)
    print("🔒 TARGET: OmniCorp Remote Security Node")
    print("⚠️ WARNING: Every firewall probe will consume 1 HOUR.")
    print("💡 HINT: Guess the 3-digit bypass key (Digits 1-9, no duplicates).")
    print("   • 'Node Link' = Correct digit in the correct position.")
    print("   • 'Data Leak' = Correct digit but in the wrong position.")
    print("=" * 50)


    # Generate 3 unique random numbers between 1 and 9
    digits = list(range(1, 10))
    random.shuffle(digits)
    secret_code = [str(d) for d in digits[:3]]

    attempts = 0
    while True:
        if player.hours_left <= 0:
            print("\n❌ SYSTEM LOCKED: You ran out of time before cracking the node!")
            return False

        guess = input(f"\n[{player.hours_left} hrs remaining] Enter 3-digit probe code (or type 'abort'): ").strip().lower()
        if guess == 'abort':
            print("🔌 Connection terminated by user.")
            return False

        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3 or '0' in guess:
            print("⚠️ INVALID PROTOCOL: Code must be exactly 3 unique digits between 1 and 9.")
            continue

        player.spend_time(1)
        attempts += 1

        # Evaluate the guess
        node_links = 0      # Right digit, Right place
        data_leaks = 0      # Right digit, Wrong Place


        for i in range(3):
            if guess[i] == secret_code[i]:
                node_links += 1
            elif guess[i] in secret_code:
                data_leaks += 1

        # Print visual matrix feedback
        print(f"📊 FEEDBACK -> [🔒 Node Links: {node_links}] | [⚠️ Data Leaks: {data_leaks}]")

        # Win Conditions
        if node_links == 3:
            print("\n🟢 ACCESS GRANTED: Firewall bypassed successfully!")
            print(f"🔓 Node decrypted in {attempts} attempt(s).")
            return True

# Simple test environment block
if __name__ == "__main__":
    # Dummy mock class just to test the file independently
    class MockPlayer:
        def __init__(self):
            self.hours_left = 24
        def spend_time(self, amt):
            self.hours_left -= amt
            
    p = MockPlayer()
    run_hacking_minigame(p)
        

