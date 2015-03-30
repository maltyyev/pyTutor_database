from working_with_pickle.make_db_pickle import loadDbase, storeDbase

db = loadDbase()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Thomas Edison'

storeDbase(db)
