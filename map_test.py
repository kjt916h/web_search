from flask import Flask, render_template #追加

app = Flask(__name__)

@app.route('/maps')
def hello():
    #return name
    return render_template('map_api.html', title='flask test') #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
