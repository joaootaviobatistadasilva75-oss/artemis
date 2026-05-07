from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    imagens = [
        "1.jpg",
        "2.webp",
        "3.jpg",
        "4.webp",
        "5.webp",
        "image1.png"
    ]

    return render_template('index.html', imagens=imagens)

if __name__ == '__main__':
    app.run(debug=True)