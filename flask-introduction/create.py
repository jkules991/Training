from app import db, app, Person

with app.app_context():
    db.drop_all()
    db.create_all()

testObject = Person(f_name="earl", l_name="Gray")

with app.app_context():
    db.session.add(testObject)
    db.session.commit()