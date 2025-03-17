from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return "Backend Web Server using flask"

@app.route('/map')
def map():
    return render_template("uni_map.html")

def main():
    app.run(debug=True,host='0.0.0.0',port=5000)

if __name__=='__main__':
    main()