from flask import Flask, render_template, request

cw929 = Flask(__name__)

@cw929.route('/')
def root():
  return render_template("form.html")

@cw929.route('/response', methods=['POST','GET'])
def response():
    name = 'default'
    if request.method == 'POST':
        name = request.form['username']
    else:
        name = request.args['username']
    return render_template("response.html", input = name, method = request.method)

if __name__ == '__main__':
  cw929.debug = True
  cw929.run()
