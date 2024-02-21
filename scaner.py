from flask import Flask
import sqlite3, os, requests

def get_data_db(id = -1):
    db_name = ""
    db_con = sqlite3.connect(db_name)
    cursor = db_con.cursor()
    if (id == -1):
        cursor.execute("SELECT id, datetime, parse_request, parse_response  FROM connect")
    else:
        cursor.execute("SELECT id, datetime, parse_request, parse_response  FROM connect WHERE id=?", (id,))
    data = cursor.fetchall()
    db_con.close()
    return data

app = Flask(__name__)

@app.route('/')

def main_page():
    return 'Домашнее задание по курсу "Инструменты и техники безопасной разработки веб-приложений"\n Выполнил: AlfaIV'


@app.route('/requests')
def requests_page():
    return 'Вы запросили все данные'


@app.route('/requests/<int:id>')
def get_data(id):
    return f"Вы запросили данные с id {id}"

@app.route('/repeat/<int:id>')
def repeat_one_item_page(id):
    proxy_url = 'http://your-proxy-url.com'  # Замените на URL вашего прокси-сервера
    target_url = 'http://your-target-url.com'  # Замените на URL целевого сервера
    response = requests.get(target_url, proxies={'http': proxy_url, 'https': proxy_url})
    # return response.text
    return f"Вы запросили повторный запрос с id {id}"


@app.route('/scan/<int:id>')
def scan_page(id):
    filename = 'dicc.txt'
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            path_list = file.read()
    else:
        return f"Internal scaner error"
    
    return f"Вы запросили сканирование с id {id} </br> файл: {path_list}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')