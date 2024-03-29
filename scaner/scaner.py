from flask import Flask
import psycopg2, os, requests

db_name = "connect"
user = "python"
pasword = "python"
# host = "127.0.0.1"
db_host = "db"
server_host = "0.0.0.0"
# server_host = '127.0.0.1'

def get_data_db(id = -1):
    global db_name, user, pasword, db_host
    try:
        db_con = psycopg2.connect(database=db_name, user=user, password=pasword, host=db_host, port="5432")
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
        return "DataBase error:" + str(err)
    


app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h3>Домашнее задание по курсу "Инструменты и техники безопасной разработки веб-приложений"</h3></br>Выполнил: AlfaIV'


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
    main_str = f'<h3>Вы запросили повторный запрос с id {id}</h3></br>'
    
    try:
        # print(get_data_db(id))
        target_url = get_data_db(id)[0][2]['path']
    except Exception as err:
        print("URL error:", str(err))
        return main_str +  "</br>URL error:" + str(err)
    
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    try:
        response = requests.get(target_url, proxies=proxies)
    except Exception as err:
        print("get request error:", str(err))
        return main_str +  "</br>get request error:" + str(err) 
    
    return main_str + f"</br> request send on url: {target_url}"


@app.route('/scan/<int:id>')
def scan_page(id):
    main_str = f'<h3>Вы запросили сканирование с id {id}</h3></br>'
    respponse_data = ''

    try:
        # print(get_data_db(id))
        url = get_data_db(id)[0][2]['path']
    except Exception as err:
        print("URL error:", str(err))
        return main_str +  "</br>URL error:" + str(err)

    filename = 'dicc.txt'

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            # for line in file:
            for i in range(10):
                line = file.readline()
                target_url = url + line.strip()
                print(target_url)
                try:
                    response = requests.get(target_url)
                except Exception as err:
                    print("get request error:", str(err))
                    return main_str +  "</br>get request error:" + str(err) 
                try:
                    if response.status_code != 404:
                        respponse_data += f'</br>Запрос по адресу: {target_url}   Вернул статус ответа: {response.status_code}</br> Тело ответа: {response.text}'
                except Exception as err:
                    print("get response error:", str(err)) 

    else:
        return main_str + '</br>Нет файла со списком для скана!'
    
    return main_str


if __name__ == '__main__':
    app.run(host=server_host, port='8000')