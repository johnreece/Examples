import pickle

x = [1,2,3,4,["a","b"]]
fh = open("test","w")
pickle.dump(x,fh)
fh.close()
fh = open("test","r")
y = pickle.load(fh)
print y