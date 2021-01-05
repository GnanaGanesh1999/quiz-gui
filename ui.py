from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Quizzer")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(
            text=f"Score : {self.quiz.score}",
            fg="#ffffff",
            bg=THEME_COLOR,
            pady=10,
            font=("Courier", 13)
        )
        self.score_label.grid(column=1, row=0)
        self.quote_container = Canvas(width="300", height=250)
        self.question_text = self.quote_container.create_text(
            150,
            125,
            text="Sample Text",
            font=("Arial", 17, "italic"),
            fill=THEME_COLOR,
            width=275
        )
        self.quote_container.grid(column=0, row=1, columnspan=2, pady=50)
        right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_img, command=self.is_answer_true)
        self.right_btn .grid(column=0, row=2)
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_img, command=self.is_answer_false)
        self.wrong_btn .grid(column=1, row=2)
        self.get_next_question()
        self.root.mainloop()

    def get_next_question(self):
        self.quote_container.config(bg="white")
        if self.quiz.still_has_questions():
            ques_text = self.quiz.next_question()
            self.quote_container.itemconfig(self.question_text, text=ques_text, fill=THEME_COLOR)
        else:
            self.quote_container.itemconfig(
                self.question_text,
                text="You've finished the quiz.",
                fill=THEME_COLOR
            )
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def is_answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.quote_container.config(bg="green")
        else:
            self.quote_container.config(bg="red")
        self.score_label.config(text=f"Score : {self.quiz.score}")
        self.quote_container.itemconfig(self.question_text, fill="white")
        self.root.after(1000, self.get_next_question)
