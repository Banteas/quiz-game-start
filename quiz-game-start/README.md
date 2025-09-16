# Quiz Game 🎮

A simple command-line **True/False Quiz Game** written in Python.  
The quiz uses trivia questions from the [Open Trivia Database](https://opentdb.com/).  

## 📌 Features
- Asks a series of True/False questions.
- Tracks your score as you play.
- Cleans up question text (HTML entities like `&quot;` → `"`).
- Ends with a final score summary.

## 🛠️ Technologies
- Python 3.x
- Built-in `html` module

## ▶️ How to Run
1. Clone this repository:
 ```
git clone https://github.com/your-username/quiz-game-start.git
cd quiz-game-start
   ```
## 📂 Project Structure
```
quiz-game-start/
│── data.py             # Contains quiz questions
│── main.py             # Entry point (game loop)
│── question_model.py   # Question class
│── quiz_brain.py       # Quiz logic
│── README.md           # Project documentation
```

## 📸 Example Gameplay
Q.1: Rabbits can see what's behind themselves without turning their heads. (True/False)?: True
Right! Your score is 1/1

Q.2: March 10th is also known as Mar10 Day. (True/False)?: False
Wrong, your score is 1/2

...
Your final score was: 7/10
