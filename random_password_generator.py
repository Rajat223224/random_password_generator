import tkinter as tk
import random
import string

# define the window
root = tk.Tk()
root.title("Password Generator")

# define the labels
label1 = tk.Label(root, text="Password Length:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Generated Password:")
label2.grid(row=1, column=0, padx=10, pady=10)

# define the entry boxes
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# define the password generator function
def generate_password():
    length = int(entry1.get())
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    entry2.delete(0, tk.END)
    entry2.insert(0, password)

# define the generate button
button1 = tk.Button(root, text="Generate", command=generate_password)
button1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# run the program
root.mainloop()
