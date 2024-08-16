import tkinter as tk
from tkinter import messagebox, filedialog

def choose_file():
    file_choice = filedialog.askopenfilename()
    target_file = open(file_choice, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    messagebox.showinfo(message=f"There are {word_count} words")

def word_counter_v2(): #updated word counter function to work with tkinter widgets
    file_path = entry.get()
    target_file = open(file_path, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    messagebox.showinfo(message=f"There are {word_count} words")

root = tk.Tk() #creates the main window (blank)
root.geometry('500x350') #sets the size of the main window
root.title("Word Counter") #adds a title to the main window
label = tk.Label(root, text="Enter the file path:") #creates a label that can have designated parameters and text
entry = tk.Entry(root, width=50) #creates an entry field to collect text from the user
word_count_button = tk.Button(root, text="Count Words",command=word_counter_v2) #creates a clickable button that can be customised
choose_file_button = tk.Button(root, text="Choose a file", command=choose_file)
exit_button = tk.Button(root, text="Quit Program", command=root.destroy)

label.pack()
entry.pack()
word_count_button.pack()
choose_file_button.pack()
exit_button.pack()

root.mainloop()