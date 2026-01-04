# 🎮 Rock-Paper-Scissors (GUI Edition)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modern **Desktop Application** for the classic Rock-Paper-Scissors game. This project moves beyond simple scripts, implementing a full Graphical User Interface (GUI) using Python's `tkinter` and Object-Oriented Programming (OOP) principles.

---

## ✨ Key Features

* **🖥️ Interactive GUI**: Features a clean windowed interface with buttons and emoji visuals.
* **🧩 Object-Oriented Architecture**: Game logic and UI are encapsulated in a scalable class structure.
* **⚡ Event-Driven Design**: Utilizes callback functions to handle user interactions dynamically.
* **📊 Live Scoreboard**: Updates game stats in real-time without refreshing the application.
* **🤖 Randomized AI**: Computer moves are generated unpredictably using Python's `random` module.

---

## 📐 Architecture (UML Diagram)

The application follows a cohesive **Class-Based Design**. The `RockPaperScissorsGUI` class manages both the *Application State* (scores, logic) and the *Presentation Layer* (widgets, updates).

```mermaid
classDiagram
    class RockPaperScissorsGUI {
        -root : Tk
        -moves : dict
        -valid_choices : list
        -scores : dict
        +__init__(root)
        +setup_ui()
        +play_round(user_choice)
        +determine_winner(user, computer) String
        +update_display(user, computer, winner)
        +reset_game()
    }