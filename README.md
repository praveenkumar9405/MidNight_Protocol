# 🌃 Midnight Protocol: The Neon Syndicate (v1.0)

A text-based, noir-cyberpunk detective simulation game run entirely inside the Python terminal. You play as a freelance investigator tasked with solving a high-profile corporate disappearance case within a strict **24-hour in-game time limit**. 

Built entirely with zero external dependencies using clean **Object-Oriented Programming (OOP)**, modular design patterns, robust input validation, and custom error boundaries.

---

## 🎮 Core Gameplay Pillars & Scope

*   **Time Management (Resource Burn):** Time is your ultimate currency. Moving between city sectors, searching rooms, and interrogating suspects burns hours. Letting the clock hit zero triggers an automatic game-over state.
*   **Deductive Inventory (The Case File):** Instead of collecting standard gaming items like keys or health potions, your case notebook tracks string-based structural *clues* and evidence.
*   **Dynamic Interrogations:** Non-Player Characters (NPCs) change their dialogue patterns dynamically based on what evidence you have uncovered and stored inside your folder.
*   **Logic-Based Hacking:** Bypassing secure firewalls or decryption nodes requires passing a custom 3-digit cryptographic puzzle system.
*   **JSON Session Persistence:** Full functionality to export your current hour countdown, credibility profile metrics, and evidence state records to resume play later.

---

## 🌐 Game World Matrix Structure

1.  **The P.I. Safehouse:** Your base of operations. Allows you to review your collected evidence notebooks safely without consuming time.
2.  **The Executive Penthouse (Crime Scene):** The missing person's last known location. Contains high-value clues hidden inside the apartment.
3.  **The Neon Grid Club:** An underground techno-bar populated by informants, black-market traders, and primary suspects.
4.  **OmniCorp Headquarters:** The heavily guarded corporate skyscraper. Requires specific clearance keys or successful firewall terminal bypasses to access records.

---

## 🛠️ Installation & Execution

### Prerequisites
*   **Python 3.x** installed on your operating system.

### Running the Game Locally
1. Clone this repository to your desktop machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the project folder directory:
   ```bash
   cd MidNight_Protocol
   ```
3. Run the primary terminal execution boot script:
   ```bash
   python main.py
   ```

---

## 🤖 Terminal Command Interface Protocol

Once inside the game engine shell, type any of these valid instructions:
*   `status` - Display your detective profile, credibility, and time left.
*   `map` - Check available city network districts and travel hour costs.
*   `travel` - Transition your position to a different district node.
*   `search` - Thoroughly scan the current room for physical evidence records (Costs 2 hours).
*   `talk` - Interrogate local suspects present in your current district.
*   `casefile` - Open your notebook to inspect collected evidence data packets.
*   `hack` - Trigger the proxy bypass mini-game to manually clear security flags.
*   `save` - Export your active game progress directly to a local JSON archive.
*   `load` - Import and parse a previously generated JSON save state file.
*   `accuse` - Go to the department and close the case (**ENDGAME CRITICAL**).
*   `quit` - Disconnect from the matrix shell.

---

## 📂 Codebase File Architecture

*   `main.py` — The core system engine file. Handles continuous terminal command loops and exceptions.
*   `player.py` — Manages the player's identity tracking, statistics, and `CaseFile` storage.
*   `entities.py` — Houses the `NPC` interrogation blueprints and suspect character instantiations.
*   `locations.py` — Maps the structural matrix geography coordinates and clue hunting parameters.
*   `hacking.py` — Runs the logic-based Mastermind-style code-breaker firewall puzzle loop.
*   `exceptions.py` — Handles custom runtime error tracking rules (`TimeExpiredError`, etc.).
