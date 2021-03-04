from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'welcome to our newsletter..-)'


if __name__ == '__main__':
    app.run()

print("hiiiii")