from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Backend Web Server!"

def main():
    app.run(debug=True,port=80)

if __name__=='__main__':
    main()