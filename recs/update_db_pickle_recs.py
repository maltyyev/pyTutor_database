import pickle

suefile = open('../sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open('../sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()

tomfile = open('../tom.pkl', 'rb')
tom = pickle.load(tomfile)
tomfile.close()
tom['name'] = 'Thomas Edison'
tomfile = open('../tom.pkl', 'wb')
pickle.dump(tom, tomfile)
tomfile.close()