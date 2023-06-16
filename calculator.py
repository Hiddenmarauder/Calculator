from tkinter import *
from flask import Flask, request, jsonify
from flask_cors import CORS

def evaluate_expression():
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except:
        expression.set("Error")

def button_click(number):
    current_expression = expression.get()
    expression.set(current_expression + str(number))

def clear_expression():
    expression.set("")

# Create the Tkinter window
window = Tk()
window.title("Calculator")

# Create a StringVar to store the expression
expression = StringVar()
expression.set("")

# Create the entry field for displaying the expression
entry = Entry(window, textvariable=expression, bd=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button click event handlers
button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, col in button_texts:
    button = Button(window, text=button_text, padx=20, pady=10, font=("Arial", 16), command=lambda number=button_text: button_click(number))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the clear button
clear_button = Button(window, text="C", padx=20, pady=10, font=("Arial", 16), command=clear_expression)
clear_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

# Create the evaluate button
evaluate_button = Button(window, text="=", padx=20, pady=10, font=("Arial", 16), command=evaluate_expression)
evaluate_button.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

# Start the Tkinter event loop
window.mainloop()



app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) to allow communication with the HTML file

@app.route('/evaluate', methods=['POST'])
def evaluate():
    expression = request.json['expression']
    try:
        result = eval(expression)
        return jsonify(result)
    except:
        return jsonify("Error")

if __name__ == '__main__':
    app.run(debug=True)
