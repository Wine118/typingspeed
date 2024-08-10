import time
from tkinter import *
from tkinter import END

# Creating the window using tkinter
window = Tk()

# The size of the window is defined
window.geometry("800x650")
window.title("Typing Speed Test")

# The passage to be typed
passage = ("In a world where technology and information flow ceaselessly, "
           "the ability to communicate effectively is more important than ever. "
           "Typing is not just a skill; it is a gateway to productivity and creativity. "
           "By mastering the art of typing, we open doors to endless possibilities, "
           "where thoughts and ideas can be transformed into words with speed and precision. "
           "Whether you're writing an email, composing a report, or simply jotting down your thoughts, "
           "the speed at which you type can make a significant difference in how efficiently you can share your message with the world.")

# Text widget for the user to type in
user_input_text = Text(window, height=10, width=80, wrap="word", font=("Times New Roman", 14))
user_input_text.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="w")

# Global variable to store the start time
start_time = None

# Function to start timing when typing begins
def start_typing(event):
    global start_time
    if start_time is None:
        start_time = time.time()  # Record the time when typing starts

# Function to calculate typing speed
def calculate_typing_speed(event=None):
    global start_time
    if start_time is None:
        result_label.config(text="Please start typing first.")
        return

    end_time = time.time()
    time_taken = end_time - start_time  # in seconds
    time_taken_minutes = time_taken / 60  # convert to minutes

    user_input = user_input_text.get("1.0", END).strip()
    word_count = len(user_input.split())
    typing_speed = word_count / time_taken_minutes

    result_label.config(text=f"Time taken: {time_taken:.2f} seconds\nTyping Speed: {typing_speed:.2f} WPM")

    # Reset start_time for the next test
    start_time = None

# Function to clear the text and reset everything
def clear():
    user_input_text.delete("1.0", END)
    global start_time
    start_time = None  # Reset the start time
    result_label.config(text="The result is ")

heading_label = Label(window, text="Your Typing Speed Tester", wraplength=750, justify="left", font=("Times New Roman", 24, "bold"))
heading_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="w")

subheading_label = Label(window, text="To test your typing speed, write the below passage as much as you can and hit enter", wraplength=750, justify="left", font=("Times New Roman", 16))
subheading_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Display the passage
passage_label = Label(window, text=passage, wraplength=750, justify="left", font=("Times New Roman", 14))
passage_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Label to display the results
result_label = Label(window, text="The result is", font=("Times New Roman", 16))
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Button to clear the text and reset
delete_button = Button(window, text="Restart", command=clear, width=12, bg='grey')
delete_button.grid(row=5, column=2, padx=10, pady=10, sticky="w")

# Bind any keypress to start timing
user_input_text.bind("<KeyPress>", start_typing)

# Bind the "Enter" key to calculate typing speed
user_input_text.bind("<Return>", calculate_typing_speed)

# Run the tkinter window
window.mainloop()
