from flask import Flask, request, render_template
from NLP.src.test import prediction 


app = Flask(__name__)

def get_face(sentence):
	img_path = "neutral_face.png"
	result, pos_score, neu_score, neg_score  = prediction(sentence)
	score = neu_score
	if result == 'Positive':
		img_path = "positive_face.png"
		score = pos_score
	elif result == 'Negative':
		img_path = "negative_face.png"
		score = neg_score

	return render_template('index.html', face=img_path, score=score)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
    	output = request.form 
    	return get_face(output['sentence'])
    return render_template('index.html', face="neutral_face.png")

if __name__ == '__main__':
	app.run(host='0.0.0.0')