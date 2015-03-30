import pickle
import glob
from recs.make_db_pickle_recs import pathfolder

for filename in glob.glob(pathfolder + '*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open(pathfolder + 'sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
