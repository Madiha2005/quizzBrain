# from question_model import Question
# from data import question_data
#
# question_bank = []
#
# for question in question_data:
#     quest_text=question ["text"]
#     quest_ans = question ["answer"]
#     new_quest= Question(quest_text,quest_ans)
#     question_bank.append(new_quest)
#
# print(question_bank)
# from data import question_data as qa
import tkinter as tk
from tkinter import messagebox  # Import messagebox from tkinter
import json


def retrieve_passGUI():
    root = tk.Tk()
    root.title("Password Generator System")
    root.geometry("455x300")

    application = tk.Label(root, text="Application")
    user = tk.Label(root, text="Username")
    password = tk.Label(root, text="Password")
    application.grid(row=0, column=0)
    user.grid(row=1, column=0)
    password.grid(row=2, column=0)

    appvalue = tk.StringVar()
    uservalue = tk.StringVar()
    passvalue = tk.StringVar()

    appentry = tk.Entry(root, textvariable=appvalue)
    userentry = tk.Entry(root, textvariable=uservalue)
    passentry = tk.Entry(root, textvariable=passvalue)

    appentry.grid(row=0, column=1)
    userentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)

    def goBack():
        root.destroy()

    shift = 6

    def caesar(text, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890*@#$%&'
        result = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift) % 42
                result += alphabet[new_position]
                print(type(text))
            else:
                result += letter
        return result

    def retrieve_passwords():
        app_name = appvalue.get()
        user_name = uservalue.get()
        if not app_name:
            messagebox.showerror("Error", "Application name is empty")
        elif not user_name:
            messagebox.showerror("Error", "User name is empty")
        elif not password:
            messagebox.showerror("Error", "Password is empty")

        else:
            try:
                with open('passwords.json', 'r') as file:
                    data = json.load(file)
                    if app_name in data and user_name in data[app_name]:
                        encoded_password = data[app_name][user_name]
                        decoded_password = caesar(encoded_password, shift)
                        passvalue.set(decoded_password)
                    else:
                        messagebox.showerror("Error", "Password not found for this application and user")
            except (FileNotFoundError, json.JSONDecodeError):
                messagebox.showerror("Error", "Password not found or invalid")

    tk.Button(root, text="Retrieve Password", command=retrieve_passwords).grid(row=4, column=1)
    tk.Button(root, text="Back", command=goBack).grid(row=4, column=0)

    root.mainloop()


if __name__ == "__main__":
    retrieve_passGUI()
