from flask import Flask
import psycopg2, os, requests

db_name = "connect"
user = "python"
pasword = "python"

def get_data_db(id = -1):
    global db_name, user, pasword
    try:
        db_con = psycopg2.connect(database=db_name, user=user, password=pasword, host="127.0.0.1", port="5432")
        cursor = db_con.cursor()
        if (id == -1):
            cursor.execute("SELECT id, datetime, parse_request, parse_response  FROM connect")
        else:
            cursor.execute("SELECT id, datetime, parse_request, parse_response  FROM connect WHERE id=%s", (id,))
        data = cursor.fetchall()
        db_con.close()
        return data
    except Exception as err:
        print("DataBase error:", str(err))

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Домашнее задание по курсу "Инструменты и техники безопасной разработки веб-приложений"\n Выполнил: AlfaIV'


@app.route('/requests')
def requests_page():
    main_str = '<h3>Вы запросили все данные</h3></br>'

    data_from_db = get_data_db()
    prepared_data = ""

    for data in data_from_db:
        prepared_data += '</br>' + " ". join(str(data))
        prepared_data += '</br>'

    return main_str + prepared_data


@app.route('/requests/<int:id>')
def get_data(id):
    main_str = f'<h3>Вы запросили данные с id {id}</h3></br>'
    prepared_data = ""
    prepared_data += '</br>' + " ". join(str(get_data_db(id)))
    print(get_data_db(id))
    prepared_data += '</br>'
    return main_str + prepared_data

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