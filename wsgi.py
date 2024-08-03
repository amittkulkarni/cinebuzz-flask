from backend import app, create_tables

if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
