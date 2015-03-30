from working_with_file.make_db_file import loadDbase

db = loadDbase()

for key in db:
    print(key, '=>\n ', db[key])

print(db['sue']['name'])
