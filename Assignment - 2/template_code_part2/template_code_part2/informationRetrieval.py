from util import *


# Add your import statements here
import operator
import numpy as np
from numpy import dot
from numpy.linalg import norm


class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		
		index = None

		#Fill in code here
		index = {}
		N = len(docs)
		words_list = []
		tmp = -1

		# list containing all the words in doc
		for doc in docs:
				for sentence in doc:
						for word in sentence:
								words_list.append(word)

		vis = {}
		for word in words_list:
				vis[word] = True
		self.vocab = [ word for word in vis ] # Vocab contains list of unique words in docs
		self.doc_weights = np.zeros([len(self.vocab),len(docs)])

		# Building vectors for doc
		df = np.zeros(len(self.vocab))
		TD_matrix = np.zeros([len(self.vocab),len(docs)])

		for i, doc in enumerate(docs):
				for sentence in doc:
						for word in sentence:
								try:
										TD_matrix[self.vocab.index(word),i] += 1
								except:
										tmp = 0
		
		df = np.sum(TD_matrix > 0, axis=1)
		self.IDF = np.log(N/df)

		for i in range(len(self.vocab)):
				self.doc_weights[i,:] = self.IDF[i]*TD_matrix[i,:]

		for i in range(len(docs)): 
				index[docIDs[i]] = self.doc_weights[:,i]
		
		self.index = index

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		doc_IDs_ordered  = [ i for i in range(len(queries)) ]
		TQ_matrix = np.zeros([len(self.vocab),len(queries)])

		# Building Query vector
		for i, vocab_word in enumerate(self.vocab):
				for j, query in enumerate(queries):
						for sentence in query:
								for word in sentence:
										if vocab_word == word:
												TQ_matrix[i,j] += 1

		self.query_weights = np.zeros([len(self.vocab),len(queries)])
		for i, vocab_word in enumerate(self.vocab):
				self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]

		# Taking cosine similarity between query and each doc
		for j in range(len(queries)):
				cos_sim = {}
				for doc_id, doc_vector in self.index.items():
						cos_sim[doc_id] = dot( doc_vector ,self.query_weights[:,j] )
						cos_sim[doc_id] /= (norm(doc_vector)*norm(self.query_weights[:,j]))

				dc_sort = sorted(cos_sim.items(), key = operator.itemgetter(1), reverse = True)
				doc_IDs_ordered[j] = [x for x, _ in dc_sort]
	
		return doc_IDs_ordered
