# Add your import statements here
from nltk.stem import WordNetLemmatizer

from util import *


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		# Fill in code here
    # We are doing Lemmatization as mentioned in previous question
		lemmatizer  = WordNetLemmatizer()
		
		for sentence in text:
			lemmatizedSentence = []
			for word in sentence:
				lemmatizedWord = lemmatizer.lemmatize(word)
				lemmatizedSentence.append(lemmatizedWord)
			reducedText.append(lemmatizedSentence)

		return reducedText


