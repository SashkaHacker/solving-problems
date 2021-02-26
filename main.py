from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    user = User()
    user.surname = "Mask"
    user.name = "Ilon"
    user.age = 99
    user.position = "Братишка Илон"
    user.speciality = "Повелитель битка"
    user.adress = "Весь Марс"
    user.email = "geniy@ilon.mask"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()