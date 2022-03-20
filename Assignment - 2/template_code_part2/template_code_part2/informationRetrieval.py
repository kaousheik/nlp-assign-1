from util import *

# Add your import statements here
import numpy as np
import operator
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

		self.index = index
		D = len(docs)
		words_list = []

		for doc in docs:
				for sentence in doc:
						for word in sentence:
								words_list.append(word)

		self.list_unique = list(set(words_list))
		df = np.zeros(len(self.list_unique))
		TD_matrix = np.zeros([len(self.list_unique),len(docs)])

		for i, doc in enumerate(docs):
				for j, sentence in enumerate(doc):
						for word in sentence:
								try:
										TD_matrix[self.list_unique.index(word),i] += 1
								except:
										tmp = 0
		
		df = np.sum(TD_matrix > 0, axis=1)
		self.IDF = np.log(D/df)
		self.doc_weights = np.zeros([len(self.list_unique),len(docs)])

		for i in range(len(self.list_unique)):
				self.doc_weights[i,:] = self.IDF[i]*TD_matrix[i,:]


		index = {key: None for key in docIDs}
		for j in range(len(docs)): 
				index[docIDs[j]] = self.doc_weights[:,j]
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

		TQ_matrix = np.zeros([len(self.list_unique),len(queries)])
		for i, unique_word in enumerate(self.list_unique):
				for j, query in enumerate(queries):
						for k, sentence in enumerate(query):
								for word in sentence:
										if unique_word == word:
												TQ_matrix[i,j] += 1

		self.query_weights = np.zeros([len(self.list_unique),len(queries)])
		for i, unique_word in enumerate(self.list_unique):
				self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]

		id_docs = list(self.index.keys())
		doc_IDs_ordered  = list(range(len(queries)))
		for j in range(len(queries)):
				dict_cosine = {key: None for key in id_docs}
				for doc_id, doc_vector in self.index.items():
						a = doc_vector
						b = self.query_weights[:,j]
						dict_cosine[doc_id] = dot(a,b)/(norm(a)*norm(b))

				dc_sort = sorted(dict_cosine.items(),key = operator.itemgetter(1),reverse = True)
				doc_IDs_ordered[j] = [x for x, _ in dc_sort]
	
		return doc_IDs_ordered

