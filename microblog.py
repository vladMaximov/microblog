from app import app, db
from app.models import User, Post

# flask shell processor config
# export FLASK_APP=microblog.py
# export FLASK_DEBUG=1 Debug mode activation
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
