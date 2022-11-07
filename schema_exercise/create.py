from app import db, app, Owners, Cars

with app.app_context():
    db.drop_all()
    db.create_all()

tiffany = Owners(first_name='Tiffany', last_name='Parker')

car1 = Cars(number_plate="1234567", ownersbr=tiffany)
car2 = Cars(number_plate="7654321", ownersbr=tiffany)
car2 = Cars(number_plate="7654345", ownersbr=tiffany)

print(tiffany.cars)
print(car1.ownersbr.first_name, car2.ownersbr.last_name)

# with app.app_context():
#     db.session.add(testObject)
#     db.session.commit()