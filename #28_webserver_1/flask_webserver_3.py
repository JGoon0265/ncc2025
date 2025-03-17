from flask import Flask, render_template, url_for, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string("""
    <html>
    <head>
        <title>Flask Server</title>
        <style>
            body {
                background: linear-gradient(90deg, red, orange, yellow, green, cyan, blue, violet);
                text-align: center;
                color: white;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 50px;
                text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
            }
            a {
                font-size: 25px;
                padding: 10px 20px;
                background-color: white;
                color: black;
                text-decoration: none;
                border-radius: 10px;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
                transition: 0.3s;
            }
            a:hover {
                background-color: yellow;
                color: red;
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <h1>🌈 와! 네클캠 3기 서버만들기 🌈</h1>
        <p>웹페이지 만들기 <strong>진.짜.겁.나.쉽.습.니.다 page</strong>!</p>
        <a href='/map'>Go to Map</a>

        <!-- 이미지 추가 -->
        <div class="image-container">
            <img src="{{ url_for('static', filename='12233.png') }}" alt="Random Image">
        </div>

    </body>
    </html>
    """)

@app.route('/map')
def map():
    return render_template("uni_map.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
