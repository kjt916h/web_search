from flask import Flask,request, render_template, Markup
import os
import googlemap_test

app = Flask(__name__)

@app.template_filter('cr')
def cr(arg):
    return Markup(arg.replace('\n', '<br>'))

@app.route('/', methods=['GET'])
def get():
	return render_template('map_search.html', \
        title = 'Web Computing Assignment', \
		subtitle = '最寄りの施設・駅の検索', \
		message = "現在地から近い施設名を入力してください。\n下のラジオボタンで検索したい店を選ぶことができます。", \
        results = "ここに結果が表示されます")

@app.route('/', methods=['POST'])
def post():
    name = request.form['choice']
    if name == "駅":
        search_type = "station"
    else:
        search_type = "food"
    return render_template('map_search.html', \
        title = 'Web Computing Assignment', \
		subtitle = '最寄りの施設・駅の検索', \
	    message = '現在地から近い施設名を入力してください。\n下のラジオボタンで検索したい店を選ぶことができます。', \
        message2 = request.form["place"] + 'の近くの' + request.form["choice"] + 'の検索結果を表示します', \
        results = googlemap_test.search(request.form["place"], search_type, distance=request.form["sel"]))



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)