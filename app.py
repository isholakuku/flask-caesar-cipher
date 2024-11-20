from flask import Flask, render_template, request

app = Flask(__name__)

# Alphabet list for the Caesar cipher
alphabet = list('abcdefghijklmnopqrstuvwxyz')

# Function for the Caesar cipher
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter  # Leave non-alphabet characters as-is
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text

# Home page route
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""  # Default result
    if request.method == "POST":  # Handle form submission
        direction = request.form["direction"]
        text = request.form["text"]
        shift = int(request.form["shift"])
        result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)