from app import app, init_db
application = app  # EB uses 'application' as the WSGI entry point

if __name__ == '__main__':
    init_db()
    application.run(host='0.0.0.0', port=5000, debug=True)