from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    db_sess = db_session.create_session()
    dic = {}
    lst = []
    for job in db_sess.query(Jobs).all():
        colich = job.collaborators.split(", ")
        id_lid = job.team_leader
        lst.append([colich])
        dic[colich] = id_lid
    for i in max(lst)


if __name__ == '__main__':
    main()
