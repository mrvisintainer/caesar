import webapp2
import cgi
from caesar import encrypt

caesar_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 3: Formation-Caesar</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Caesar</a>
    </h1>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="caesar-rot" value="0">
                <p class="error"></p>
            </div>
            <br>
            <textarea type ="text" rows="8" cols="70" name="text">%(answer)s</textarea>
            <br>
            <input type="submit">
</body>
</html>
"""

ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text, rotation):
    answer = ""
    for char in text:
        answer += rotate_char(char, rotation)
    return answer

#def escape_html(e):
#    return cgi.escape(e, quote = True)

class Caesar(webapp2.RequestHandler):
    def write_form(self, answer=""):
        self.response.out.write(caesar_form % {"answer": answer})

    def get(self):
        self.write_form()

    def post(self):
        rotation = self.request.get("caesar-rot")
        rotation = int(rotation)
        text = self.request.get("text")
        answer = encrypt(cgi.escape(text, quote = True), rotation)
        self.write_form(answer)

app = webapp2.WSGIApplication([
    ('/', Caesar)
], debug=True)
