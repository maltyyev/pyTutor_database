from files.make_db_file import loadDbase, storeDbase

db = loadDbase()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Thomas Edison'
storeDbase(db)
