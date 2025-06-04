from app import app, db

# Push application context so db.create_all() works
with app.app_context():
    db.create_all()
    print("✅ Database tables created")