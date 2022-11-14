from flask import Flask, request

app = Flask(__name__)

@app. route('/get_log', methods=['POST'])
def get_log():
    logs = request.form['logs'] 


    with open('logs.txt', 'a') as f:
        f.write(f'{logs}\n')

    return {'result': True}

if __nane == {'result': True}:
    app.run(host='0.0.0.0')