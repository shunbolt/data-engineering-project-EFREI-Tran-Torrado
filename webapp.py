from flask import Flask, request, render_template
app = Flask(__name__)

def get_face(sentence):
	img_path = "neutral_face.png"
	score = 0.5
	if sentence == 'I am happy':
		img_path = "positive_face.png"
		score = 1
	elif sentence == 'I am sad':
		img_path = "negative_face.png"
		score = 0

	return render_template('index.html', face=img_path, score=score)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
    	output = request.form 
    	return get_face(output['sentence'])
    return render_template('index.html', face="neutral_face.png")

if __name__ == '__main__':
	app.run(host='0.0.0.0')