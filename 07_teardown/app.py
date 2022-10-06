# your heading here
'''
Jacob Guo
SoftDev
2022-10-03

'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "RAAAAAAAAAA!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. Python, netlogo?
1. Division in Python and Java, website links
2. Maybe print into the terminal when run? 
3. Whatever __name__ is
4. Where ever app.run() puts its stuff - so something Flask related
5. Java, where u have an object (Object Oriented CODING) and u run a method on it
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 
 We decided to experiment with the lines in the code and see how it works.
 
 We replaced the "/" with any other char and realized the error message
 hinted us to the code leading to a website.
 
 
 
'''