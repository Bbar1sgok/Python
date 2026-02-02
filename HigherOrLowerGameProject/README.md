# Higher–Lower Game (Python)

A console-based Higher–Lower style game written in Python.  
The player is shown two public figures and must guess which one has more followers.

---

## 🎮 How the Game Works

1. Two random accounts are selected from the dataset.
2. The player chooses **A** or **B** based on who they think has more followers.
3. If the answer is correct, the score increases.
4. If the answer is wrong, the game ends.
5. If both accounts have the same follower count, the round is treated as **neutral**
   and the player still gains a point.
6. The player can exit the game anytime by pressing **0**.

---

## 🧠 Game Logic Design

- Input validation is handled in a separate function.
- The comparison logic is isolated inside a controller function.
- Edge cases (same account selected twice) are handled explicitly.
- Tie situations are handled intentionally as a neutral win.

This structure keeps the code readable, testable, and easy to extend.

---

## 🛠 Technologies Used

- Python 3
- Standard Library (`random`)
- Modular design with external data and ASCII art files

---

## 📂 Project Structure
