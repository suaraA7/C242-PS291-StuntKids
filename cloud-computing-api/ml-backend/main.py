from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Anda dapat mengatur host dan port sesuai kebutuhan
