from flask import Flask, render_template, redirect, request

app = Flask(__name__, static_folder='static')



#-------------- Routes------------ #
@app.route('/')
def index():
    return render_template('index.html')




#--------Run-------#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)