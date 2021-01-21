from src.main import create_app
app = create_app()


@app.route('/')
def welcome():
    return 'Flask Alchemy Starter'


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
