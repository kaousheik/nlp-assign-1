import math

from util import *

# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		relevant_docs = 0
		count = 0
		for id in query_doc_IDs_ordered:
				if k == count:
						break
				count += 1
				if id in true_doc_IDs:
						relevant_docs += 1
		precision = relevant_docs / k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		N = len(query_ids)
		count = 0
		for i, ids in enumerate(doc_IDs_ordered):
			
				true_ids = []
				while int(qrels[count]["query_num"]) == query_ids[i]:
						true_ids.append(int(qrels[count]["id"]))
						count += 1
						if count == len(qrels):
								break
			
				meanPrecision += self.queryPrecision(ids, query_ids[i], true_ids, k) / N
		
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		total_relevant_docs = len(true_doc_IDs)
		relevant_docs_retr = 0
		cur_relevant_docs_count = 0
		
		for id in query_doc_IDs_ordered:
				if cur_relevant_docs_count == k:
						break
			
				cur_relevant_docs_count += 1
				if id in true_doc_IDs:
						relevant_docs_retr +=1
			
		recall = relevant_docs_retr / total_relevant_docs
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		N = len(query_ids)
		count = 0
		for i,ids in enumerate(doc_IDs_ordered):
				true_ids = []
				while int(qrels[count]["query_num"]) == query_ids[i]:
						true_ids.append(int(qrels[count]["id"]))
						count += 1
						if count == len(qrels):
								break
				
				meanRecall += self.queryRecall(ids, query_ids[i], true_ids, k) / N
		
		return meanRecall

	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		if precision==0 or recall==0:
				fscore=0
		else:
				fscore = 1 / ( (1/precision) + (1/recall) )

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		N = len(query_ids)
		count = 0
		for i,ids in enumerate(doc_IDs_ordered):
				true_ids = []
				while int(qrels[count]["query_num"]) == query_ids[i]:
						true_ids.append(int(qrels[count]["id"]))
						count += 1
						if count == len(qrels):
								break
				
				meanFscore += self.queryFscore(ids, query_ids[i], true_ids, k) / N
		return meanFscore

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		relevance = [i for i in range(k)]
		doc_ids_cpy = []
		relevance_cpy = []
		
		for i,j in true_doc_IDs:
				doc_ids_cpy.append(i)
				relevance_cpy.append(j)
		
		for i, docID in enumerate(query_doc_IDs_ordered):
				try:
						index = doc_ids_cpy.index(docID)
						relevance[i] = relevance_cpy[index]
				except:
						relevance[i] = 0
				if i == k-1:
						break
				
		DCG  = 0
		IDCG = 0
		
		for i,rel in enumerate(relevance):
				DCG += rel/math.log((i+2),2)
		relevance.sort(reverse=True)
		for i,rel in enumerate(relevance):
				if rel == 0:
						break
				IDCG += rel/math.log((i+2),2) 
		
		nDCG = DCG/IDCG
		return nDCG

	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		N = len(query_ids)
		count = 0
		for i,ids in enumerate(doc_IDs_ordered):
				true_ids = []
				while int(qrels[count]["query_num"]) == query_ids[i]:
						true_ids.append(int(qrels[count]["id"]))
						count += 1
						if count == len(qrels):
								break
				
				meanNDCG += self.queryNDCG(ids, query_ids[i], true_ids, k) / N
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		retrieved_count = 0
		relavant_docs_count = 0
		precision_sum = 0
		
		for id in query_doc_IDs_ordered:
				retrieved_count += 1
				if id in true_doc_IDs:
						relavant_docs_count += 1
				precision_sum += relavant_docs_count / retrieved_count
			
				if retrieved_count == k:                                       
						break
		
		avgPrecision = precision_sum / max(relavant_docs_count,1)
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		N = len(query_ids)
		count = 0
		for i,ids in enumerate(doc_IDs_ordered):
				true_ids = []
				while int(qrels[count]["query_num"]) == query_ids[i]:
						true_ids.append(int(qrels[count]["id"]))
						count += 1
						if count == len(qrels):
								break
				
				meanAveragePrecision += self.queryAveragePrecision(ids, query_ids[i], true_ids, k) / N
		return meanAveragePrecision

