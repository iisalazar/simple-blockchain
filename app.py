from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain
from wtforms import Form, StringField

blockchain = Blockchain()

class DataForm(Form):
	data = StringField('Data')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	form = DataForm(request.form)
	return render_template("home.html", blocks=blockchain.blocks, form=form)


@app.route('/add_to_blockchain', methods=['POST'])
def add_to_blockchain():
	data = request.form.to_dict()
	blockchain.generate_next_block(data['block-data'])
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)