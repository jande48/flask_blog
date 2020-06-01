from flask import Flask, render_template
app=Flask(__name__)

post= [
    {
        'author': 'Michael Scott',
        'title': 'Past and Future of the Paper Industry',
        'content': 'As you know, I am the district manager of Dunker Mifflin.',
        'date_posted': 'April 1, 1985'
    },
    {
        'author': 'Jim',
        'title': 'Why Working at Dunker Mifflin is terrible',
        'content': 'Michael scott is worst.',
        'date_posted': 'April 2, 1985'
    }

]

@app.route("/")
def hello():
    return render_template('home.html',posts=post)

# This means that if we run this program with python, debug will be true, but in a prod server it will be false
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/about")
def about():
    return render_template('about.html',title="The About Title")