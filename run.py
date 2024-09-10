# Create the Flask app
from app import create_app


app = create_app()

if __name__ == '__main__':
    # Run the app on port 5000 and make it accessible externally
    app.run(debug=True, host='0.0.0.0', port=5000)
