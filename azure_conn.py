def update(doc):
    global i__P
    doc['ip']=i__P
    import azure.cosmos.cosmos_client as cosmos_client
    url = 'https://proctorapp.documents.azure.com:443/'
    key = 'hH34800uTN7tR9XDRnR4qZKizfuc3re1sVKYa9cracu7wIzuQeFRaCIj8YlpCh9HM9JOBX1lSIoL8gQLMV02hQ=='
    client1 = cosmos_client.CosmosClient(url, {'masterKey': key})
    database = client1.get_database_client('student')
    container = database.get_container_client('user')
    container.upsert_item(doc)

def connect():
	from pydocumentdb import document_client
	uri = 'https://proctorapp.documents.azure.com:443/'
	key = 'hH34800uTN7tR9XDRnR4qZKizfuc3re1sVKYa9cracu7wIzuQeFRaCIj8YlpCh9HM9JOBX1lSIoL8gQLMV02hQ=='

	client = document_client.DocumentClient(uri, {'masterKey': key})

	db_id = 'student'
	db_query = "select * from r where r.id = '{0}'".format(db_id)
	db = list(client.QueryDatabases(db_query))[0]
	db_link = db['_self']
	return db_link,client
	#coll_id = 'user'
	#coll_query = "select * from r where r.id = '{0}'".format(coll_id)
	#coll = list(client.QueryCollections(db_link, coll_query))[0]
	#coll_link = coll['_self']
	#print(coll_link)

	#doc_id = '180800107075'
	#doc_qry = "select * from r where r.username = '{0}'".format(doc_id)
	#doc = list(client.QueryDocuments(coll_link, doc_qry,{ "enableCrossPartitionQuery": True }))[0]
	#doc_link = doc['_self']
	#print(doc_link)
	#print(doc)
	#print(doc["sem"])

	#coll_id1 = 'exam'
	#coll_query1 = "select * from r where r.id = '{0}'".format(coll_id1)
	#coll1 = list(client.QueryCollections(db_link, coll_query1))[0]
	#coll_link1 = coll1['_self']
	#print(coll_link1)
	#doc1_id = doc["sem"]
	#doc1_qry = "select * from r where r.sem = '{0}'".format(doc1_id)
	#doc1 = list(client.QueryDocuments(coll_link1, doc1_qry,{ "enableCrossPartitionQuery": True }))[0]
	#doc1_link = doc1['_self']
	#print(doc1_link)
	#print(doc1)

db_link,client=connect()

