from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#маршрут для подтверждения Яндекса
@app.route('/yandex_ee4e99d668bda113.html')
def yandex_verify():
    return send_from_directory('.', 'yandex_ee4e99d668bda113.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
