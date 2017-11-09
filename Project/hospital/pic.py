import pickle

ob = open('test.p', 'wb')
v = int(7)
pickle.dump(v, ob)
ob.close()