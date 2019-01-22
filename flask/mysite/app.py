from flask import Flask, render_template, request
import os, csv
app = Flask(__name__)

    
@app.route("/")
def hello():
    return "Hello World!"


@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'
    
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)
    
@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)

@app.route('/fruits')
def fruits():
    fruits = ['apple','banana','mango','melon']
    return render_template('fruits.html', fruits = fruits)

@app.route('/send')
def send():
    return render_template('send.html')

# ex) requests.gets
# {‘who’: ‘민재님’. ‘message’: ‘볼링 치러가실래요?’}
@app.route('/receive')
def receive():
    name = request.args.get('who')
    message = request.args.get('message')

    with open('guestbook.csv','a', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['who','message'])
        writer.writerow({
            'who': name,
            'message':message
        })
    
    return render_template('receive.html', name_in_html=name, message_in_html=message, result=result)


@app.route('/guestbook')
def guestbook():
    result = []
    with open('guestbook.csv','r', encoding='utf8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)
        
    return render_template('guestbook.html', result_in_html = result)












if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)