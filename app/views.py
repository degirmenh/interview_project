from app import app


@app.route("/")
def index():
    """
        Default view
    """
    return "<p>Hello! This is an interview projects</p>"

