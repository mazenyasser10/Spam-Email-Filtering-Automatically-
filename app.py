#File for GUI

import tkinter as tk
from spam_filter import SpamFilter

sf = SpamFilter()

# Training Data
sf.train_from_csv(r"C:\Users\pc\Downloads\spam.csv")

# GUI
root = tk.Tk()
root.title("Spam Filter")


def check_email():
    email_text = text_box.get("1.0", tk.END)
    result = sf.predict(email_text)
    result_label.config(text=f"Result: {result}")


tk.Label(root, text="Paste your e-mail:").pack()

text_box = tk.Text(root, height=15, width=60)
text_box.pack()

tk.Button(root, text="Check", command=check_email).pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
