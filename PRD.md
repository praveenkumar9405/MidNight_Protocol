# 📄  Product Requirement Document (PRD)
## Project Name: *Midnight Protocol: The Neon Syndicate*
**Author:** JD_PRAVEEN KUMAR 
**Target Platform:** Cross-platform Terminal / Command Line Interface (CLI)  
**Language:** Python 3.x (No external dependencies required)

---

## 1. Executive Summary & Objective
**Midnight Protocol** is a text-based, noir-cyberpunk detective simulation game. The player takes on the role of a freelance investigator tasked with solving a high-profile corporate disappearance case within a strict **24-hour in-game time limit**. 

The technical objective of this project is to build a full-featured, crash-resistant Python application using **Object-Oriented Programming (OOP)**, **modular design patterns**, and **robust input validation**.

---

## 2. Core Gameplay Pillars & Scope
*   **Time Management (Resource Burn):** Time is the primary resource. Moving between city sectors, searching rooms, and interrogating suspects drains hours. Running out of time triggers an automatic game-over state.
*   **Deductive Inventory (The Case File):** Instead of collecting standard items like keys or potions, the player’s inventory tracks string-based structural *clues* and evidence.
*   **Dynamic Interrogation System:** Non-Player Characters (NPCs) change their dialogue patterns dynamically based on what evidence the player has uncovered and stored in their inventory.
*   **Logic-Based Hacking Mini-Games:** Bypassing security firewalls or decryption tools requires passing string manipulation or number-guessing logic puzzles.

---

## 3. Game World Architecture & Locations
The game consists of **four primary locations** connected through a routing engine:
1.  **The P.I. Safehouse:** The home base. Allows the player to review their entire Case File evidence board without spending time.
2.  **The Executive Penthouse (Crime Scene):** The missing person's last known location. Contains physical clues and a locked personal terminal.
3.  **The Neon Grid Club:** An underground techno-bar populated by informants, black-market traders, and primary suspects.
4.  **OmniCorp Headquarters:** The heavily guarded corporate office. Requires specific clearance keys or successful terminal bypasses to access restricted records.

---

## 4. Entity Specifications (OOP Blueprint)

### A. The Detective (Player Engine)
*   **Attributes:** `name` (String), `hours_left` (Integer, max 24), `credibility` (Integer, percentage), `current_location` (Object).
*   **Methods:** `travel()`, `investigate()`, `accuse_suspect()`.

### B. Suspects & Informants (NPC Engine)
*   **Attributes:** `name` (String), `alibi_broken` (Boolean), `required_clue` (String).
*   **Behavior:** If `required_clue` is present in the player's inventory, the NPC unlocks an alternative, truthful dialogue tier. Otherwise, they repeat a deceptive alibi string.

---

## 5. User Interface (UI) & Command Structure
The interface simulates a clean, monospaced terminal computer screen. The system must use a consistent text layout (e.g., using `===` headers and clean indentation).

### Valid Universal Player Inputs:
*   `help` - Shows a dictionary list of valid situational commands.
*   `check case` - Displays all logged evidence currently saved inside the inventory.
*   `status` - Prints current hours remaining and credibility levels.
*   `travel` - Prompts a list of accessible city sectors.
*   `search` - Scans the current room environment for physical objects/terminals.

---

## 6. Non-Functional & Technical Requirements
*   **Zero Dependencies:** The entire game loop must run utilizing Python’s built-in libraries (`os`, `sys`, `random`, `json`, `time`).
*   **Crash Prevention (Input Validation):** All user commands must be cleaned using `.strip().lower()`. Empty returns, symbols, or out-of-bounds array requests must be caught cleanly using validation loops without ever raising unhandled runtime errors.
*   **Persistence (Optional Stretch Goal):** Ability to export the current game state to a `.json` file to allow saving and loading progress.
