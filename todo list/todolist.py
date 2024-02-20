from tkinter import *
class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('850x610+500+150')
        
        self.label = Label(self.root, text="To-Do-List-APP", font=('arial', 25, 'bold'), width=10, bd=5, bg='violet', fg="black")
        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text="Add Task", font=('arial', 18, 'bold'), width=10, bd=5, bg='violet', fg="black")
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text="Tasks", font=('arial', 18, 'bold'), width=10, bd=5, bg='violet', fg="black")
        self.label3.place(x=500, y=54)

        self.main_text = Listbox(self.root, height=12, bd=5, width=28, font=("arial", 20, "italic bold"))
        self.main_text.place(x=380, y=150)

        self.text = Text(self.root, bd=5, height=2, width=30, font=('arial', 10, 'bold'))
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font=("arial", 18, "bold italic"), width=10, bd=5, bg="violet", fg="black", command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font=("arial", 18, "bold italic"), width=10, bd=5, bg="violet", fg="black", command=self.delete)
        self.button2.place(x=30, y=250)

        self.button3 = Button(self.root, text="Display Tasks", font=("arial", 18, "bold italic"), width=15, bd=5, bg="violet", fg="black", command=self.display_tasks)
        self.button3.place(x=30, y=320)

        self.button4 = Button(self.root, text="Mark as Completed", font=("arial", 18, "bold italic"), width=20, bd=5, bg="violet", fg="black", command=self.mark_completed)
        self.button4.place(x=30, y=390)

        self.button5 = Button(self.root, text="Exit", font=("arial", 18, "bold italic"), width=10, bd=5, bg="violet", fg="black", command=self.exit_app)
        self.button5.place(x=30, y=460)

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)

        self.text.delete(1.0, END)

    def delete(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            self.main_text.delete(selected_index)
            with open("data.txt", 'r') as file:
                lines = file.readlines()

            with open("data.txt", 'w') as file:
                for i, line in enumerate(lines):
                    if i not in selected_index:
                        file.write(line)

    def display_tasks(self):
        self.main_text.delete(0, END)  # Clear the current tasks in the Listbox
        with open('data.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())

    def mark_completed(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            completed_task = self.main_text.get(selected_index)
            with open("completed_tasks.txt", "a") as file:
                file.write(completed_task + "\n")
            self.main_text.delete(selected_index)

    def exit_app(self):
        self.root.destroy()

def main():
    root = Tk()
    v1 = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()