import socket
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.title = 'Meu Título Personalizado' 

@app.route('/')
def home():
    return render_template('index.html', ips=ips, title='Meu Título Personalizado')

@app.route('/ping', methods=['POST'])
def ping():
    ip = request.form['ip']
    try:
        socket.create_connection((ip, 80), timeout=1)
        status = 'online'
    except Exception as e:
        status = 'offline'
    return jsonify({'status': status})

if __name__ == '__main__':
    ips = ['192.168.0.{}'.format(i) for i in range(1, 255)]
    app.run(debug=True)