from flask import Flask
import random

app = Flask(__name__)

mystery_num = random.randint(0, 9)


@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMngxbzRxb2V3bTUycXVzZ2dicHZmYWFqNHk5NDI5eGVlMTF"
            "saDg1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PoOwDh60P8NDh7ksl7/giphy.gif'>")


@app.route("/<int:num>")
def number(num):
    if num < mystery_num:
        return ('<h1 style="color:red">Too low, Try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnlicXpsdDcweGRoOTVzZmFsNzRvM3l5bGJoNWZ0dnJt'
                'ZnlxYzk5MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m3SYKzhmod1IY/giphy.gif">')
    elif num > mystery_num:
        return ('<h1 style="color:purple">Too high, Try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzlod3F6Y203dXpwMGZxdXRzczQ1c3BobTBpMmhzZHFw'
                'b29oemptMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Qumf2QovTD4QxHPjy5/giphy.gif">')
    else:
        return ('<h1 style="color:green">You got it!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjc4NjVseTdxbWRxYjA4aXE0Y3NpeDFsNnlheWFnZnBxen'
                'NhaWUzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/he43oHTj5D008/giphy.gif">')


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
