import pickle
from initdata import bob, sue, tom

pathfolder = '../dbs/recs/'

if __name__ == '__main__':
    for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
        recfile = open(pathfolder + key + '.pkl', 'wb')
        pickle.dump(record, recfile)
        recfile.close()
