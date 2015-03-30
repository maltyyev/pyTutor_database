import pickle
from recs.make_db_pickle_recs import pathfolder

suefile = open(pathfolder + 'sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open(pathfolder + 'sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()

tomfile = open(pathfolder + 'tom.pkl', 'rb')
tom = pickle.load(tomfile)
tomfile.close()
tom['name'] = 'Thomas Edison'
tomfile = open(pathfolder + 'tom.pkl', 'wb')
pickle.dump(tom, tomfile)
tomfile.close()