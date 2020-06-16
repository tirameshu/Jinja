from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template("main.html", my_string="Wheee", my_list=[0, 1, 2, 3, 4, 5])

if __name__=='__main__': # to conduct unit test, demo, etc
    app.run(debug=True)
