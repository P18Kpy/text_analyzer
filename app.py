from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 
from textblob import Word
from textblob import TextBlob
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

from textblob import TextBlob,Word 
import random 
import time

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyse',methods=['POST'])
def analyse():
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		
		blob = TextBlob(rawtext)
		received_text2 = blob
		polarity, subjectivity = blob.sentiment
		blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity

		nouns = list()
		for tag in blob:
			if tag == 'NN':	
				nouns.append(lemmatizer.lemmatize(word))
				len_of_words = len(nouns)
				rand_words = random.sample(nouns,len(nouns))
				final_word = list()
				for item in rand_words:
					word = Word(item).pluralize()
					final_word.append(word)
					summary = final_word
					end = time.time()
					final_time = end-start


	return render_template('index.html',received_text = received_text2,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity)


if __name__ == '__main__':
	app.run(debug=True)