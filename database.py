from flask_sqlalchemy import SQLAlchemy

# Database instance
db = SQLAlchemy()

def init_db(app):
    """Initialize database with Flask app"""
    db.init_app(app)
    
def create_tables(app):
    """Create all database tables"""
    with app.app_context():
        db.create_all()
        
def drop_tables(app):
    """Drop all database tables"""
    with app.app_context():
        db.drop_all()
