import pickle
f = open('my.pck','wb')
v='1'
pickle.dump(v,f)
f.close()