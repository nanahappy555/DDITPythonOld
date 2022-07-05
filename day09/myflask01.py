from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_servlet():
    return 'hello flask'

@app.route('/para')
def para():
    p = request.args.to_dict() # {"a":"555"}
    # p = request.args.get('a') # 555 # 매개변수에 'p'라고 써도 실행은 되지만 None이라고 나옴
    return f'parameter : {p}'

if __name__ == '__main__':
    app.run()
    
    