import decimal
import json
from string import ascii_letters

import pymysql
from flask import render_template, Flask
from pymysql.cursors import DictCursor

host = 'localhost'
user = 'root'
password = 'nastyadoska01'
db = 'cse_calculator'


site = Flask(__name__)


def fetch_one_wrapper(method):
    """Monkey patch функции cursor.fetchone()
    Заменяет все decimal.Decimal на int
    """
    def wrapper(*args, **kwargs):
        row = method(*args, **kwargs)
        if row is not None:
            for key, value in row.items():
                if isinstance(value, decimal.Decimal):
                    row[key] = int(value)
            return row
        else:
            return None

    return wrapper


def fetch_all_wrapper(method):
    """Monkey patch функции cursor.fetchall()
    Заменяет все decimal.Decimal на int
    """
    def wrapper(*args, **kwargs):
        rows = method(*args, **kwargs)
        result = []
        for row in rows:
            for key, value in row.items():
                if isinstance(value, decimal.Decimal):
                    row[key] = int(value)
            result.append(row)
        return result

    return wrapper


def get_mysql_cursor():
    connection = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8mb4', cursorclass=DictCursor, autocommit=True)
    cursor = connection.cursor()
    cursor.fetchone = fetch_one_wrapper(cursor.fetchone)
    cursor.fetchall = fetch_all_wrapper(cursor.fetchall)
    return cursor


def get_mysql_cursor_with_connection():
    connection = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8mb4', cursorclass=DictCursor, autocommit=True)
    cursor = connection.cursor()
    cursor.fetchone = fetch_one_wrapper(cursor.fetchone)
    cursor.fetchall = fetch_all_wrapper(cursor.fetchall)
    return connection, cursor


def is_float(number):
    try:
        float(number)
        return True
    except:
        return False


subjects_translations = {
    'math': 'Математика (профильная)',
    'rus': 'Русский язык',
    'it': 'Информатика и ИКТ',
    'phys': 'Физика',
    'ss': 'Обществознание',
    'hist': 'История',
    'eng': 'Иностранный язык'
}


@site.route('/')
def index():
    return render_template("index.html")


@site.route('/institute/all', methods=['GET'])
def all_institutes():
    cur = get_mysql_cursor()
    cur.execute('SELECT naming, institute FROM specialties')
    your_mama = cur.fetchall()
    cur.close()
    return json.dumps(your_mama)


@site.route('/institute/<string:institution_id>', methods=['GET'])
def get_institute(institution_id):
    assert all(x in ascii_letters for x in institution_id)
    cur = get_mysql_cursor()
    cur.execute(f'SELECT naming, institute FROM specialties WHERE institution_id  = "{institution_id}"')
    your_mama = cur.fetchall()
    cur.close()
    return json.dumps(your_mama)


@site.route('/get-specialties', methods=['GET'])
def get_cse(average_score, subjects):
    if type(subjects) is str:
        subjects = [subjects]
    assert all(x in ascii_letters for x in subjects)
    assert is_float(average_score)
    cur = get_mysql_cursor()
    if 'math' in subjects:
        cur.execute(f'''
            SELECT naming, institute
            FROM specialties
            WHERE
                average_score = "{average_score}"
                AND subjects LIKE "%{subjects_translations[subjects[0]]}%"
                AND subjects LIKE "%{subjects_translations[subjects[1]]}%"
        ''')
    else:
        cur.execute(f'''
            SELECT naming, institute 
            FROM specialties 
            WHERE 
                average_score = "{average_score}" 
                AND subjects LIKE "%{subjects_translations[subjects[0]]}%"
        ''')

    your_mama = cur.fetchall()
    cur.close()
    return json.dumps(your_mama)


# @site.route('/institute/<string:speciality_id>/', methods=['GET'])
# def get_institute(karto4ka):
#     assert all(x in '0123456789' for x in speciality_id)
#     cur = get_mysql_cursor()
#     cur.execute(f'SELECT naming, institute FROM specialties WHERE id = "{speciality_id}"')
#     your_mama = cur.fetchone()
#     cur.close()
#     return json.dumps(your_mama)

if __name__ == "__main__":
    site.run(debug=True)


# jaga_jaga(
#     {
#         "title": "Программная инженерия",
#         "desc": "Вы будете учить физику :).",
#         "points": 100.98,
#         "subjects": ["Просто Физика", "Продвинутая Физика", "Классная Физика"],
#         "placeCount": "20/5",
#         "moneyType": "Бюджет / Коммерция",
#         "period": "4 года",
#         "cost": "99999 999 в год"
#     }
# )