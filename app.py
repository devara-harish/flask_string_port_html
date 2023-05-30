from flask import Flask,render_template

FAO=Flask(__name__)

@FAO.route('/wish')
def wish():
    return "hello world"


@FAO.route('/hello/<name>/')
def hello(name):
    return f'helloo good evening {name}'



@FAO.route('/first')
def first():
    return render_template('first.html')

@FAO.route('/render')
def render():
    return render_template('render.html',name='harish',age=24)





if __name__=='__main__':
    FAO.run(debug=True,port=5001)