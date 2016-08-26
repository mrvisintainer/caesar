import webapp2
import re
import cgi

signup_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 3: Formation-Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Signup</h1>
        <form method="post">
            <div>
                <label for="username">Username&emsp;&emsp;&ensp;</label>
                <input type="text" name="username" value="%(username)s">
                <div style="color:red">%(error)s</div>
            </div>
            <div>
                <label for="password">Password&emsp;&emsp;&ensp;&nbsp;</label>
                <input type="password" name="password" value="">
                <p class="error"></p>
            </div>
            <div>
                <label for="verify">Verify Password</label>
                <input type="password" name="verify" value="">
                <p class="error"></p>
            </div>
            <div>
                <label for="email">Email (optional)</label>
                <input type="text" name="email" value="%(email)s">
                <p class="error"></p>
            </div>
            <input type="submit">
</body>
</html>
"""

welcome_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 3: Formation-Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    "<h1><strong>Welcome, " + %(username)s + "!</strong></h1>"
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(webapp2.RequestHandler):
    def write_form(self, error="", username="", email=""):
        self.response.out.write(signup_form % {"error": error,
                                               "username": username,
                                               "email": email})

    def get(self):
        self.write_form()
'''
        error_element_u = "<p class='error'>" + error + "</p>" if error else ""
        error_element_p = "<p class='error'>" + error + "</p>" if error else ""
        error_element_v = "<p class='error'>" + error + "</p>" if error else ""
        error_element_e = "<p class='error'>" + error + "</p>" if error else ""
'''
    def post(self):
        have_error = False
        username = valid_username(self.request.get('username'))
        password = valid_password(self.request.get('password'))
        verify = self.request.get('verify')
        email = valid_email(self.request.get('email'))
        error = self.request.get("error")

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            error = "For shame, that's not a valid username!"
            error_element_u = cgi.escape(error, quote=True)
            have_error = True
            self.redirect('/?error=' + error)

        if not valid_password(password):
            error = "Your password is awful, and you are awful"
            error_element_p = cgi.escape(error, quote=True)
            have_error = True
            self.redirect('/?error=' + error)
        elif password != verify:
            error = "Really? I won't swipe right until you prove you can match!"
            error_element_v = cgi.escape(error, quote=True)
            have_error = True
            self.redirect('/?error=' + error)

        if not valid_email(email):
            error = "What, are you bashful? I may want to get in touch!"
            error_element_e = cgi.escape(error, quote=True)
            have_error = True
            self.redirect('/?error=' + error)

        if have_error != True:
            self.redirect('/welcome?username=' + username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.write(welcome_form)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome', Welcome)
], debug=True)
'''import webapp2
import re
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 3: Formation-Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Signup</h1>
"""

page_footer = """
</body>
</html>
"""

welcome_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Assignment 3: Formation-Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

welcome_footer = """
</body>
</html>
"""
ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ARAB_NUMERALS = "0123456789_"

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    for char in username:
        if char != ALPHABET_LOWERCASE or ALPHABET_UPPERCASE or ARAB_NUMERALS:
            return False
    return True

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    if len(password) < 3 or len(password) > 20:
        return False
    for char in password:
        if char != ALPHABET_LOWERCASE or ALPHABET_UPPERCASE or ARAB_NUMERALS:
            return False
    return True

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    for char in email:
        if char != '@'
    return not email or EMAIL_RE.match(email)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(webapp2.RequestHandler):
    def get(self):
        signup_form = """
        <form method="post">
            <div>
                <label for="username">Username&emsp;&emsp;&ensp;</label>
                <input type="text" name="username" value="">
                <p class="error"></p>
                <label for="password">Password&emsp;&emsp;&ensp;&nbsp;</label>
                <input type="password" name="password" value="">
                <p class="error"></p>
            </div>
            <div>
                <label for="verify">Verify Password</label>
                <input type="password" name="verify" value="">
                <h2 class="error"></h2>
            </div>
            <div>
                <label for="email">Email (optional)</label>
                <input type="text" name="email" value="">
                <h2 class="error"></h2>
            </div>
            <input type="submit">
        """

        error = self.request.get("error")
        error_element_u = "<p class='error'>" + error + "</p>" if error else ""
        error_element_p = "<p class='error'>" + error + "</p>" if error else ""
        error_element_v = "<h2 class='error'>" + error + "</h2>" if error else ""
        error_element_e = "<h2 class='error'>" + error + "</h2>" if error else ""

        main_content = signup_form + error_element_u + error_element_p + error_element_v + error_element_e
        response = page_header + main_content + page_footer
        self.response.write(response)
'''
'''
class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome_user = "<h1><strong>Welcome, " + username + "!</strong></h1>"
        response = welcome_header + welcome_user + welcome_footer
        if valid_username(username):
            self.response.write(response)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome', Welcome)
], debug=True)
'''
