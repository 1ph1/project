from flask import Flask
app = Flask(__name__)
print("aboba")

@app.route('/')
def test():
    return "МАТВЕЙ ГДЕ РОУТЫ"

if __name__ == "__main__":
    app.run()
