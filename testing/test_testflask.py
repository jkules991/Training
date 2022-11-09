from flask_testing import TestCase

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            'SQLALCHEMY_DATABASE_URI' = 'sqlite:///',
            DEBUG=True
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        for subj in ['Jankins', 'Pythud', 'Flop']:
            subjects = Subjects(subject_name=subj)
            db.session.add(subjects)
            data1 = {'Melon':2, 'Derp':1, 'Madman':}

    def tearDown(self):
        pass


