import sys
import pickle

def list_pickler(my_list):
    f=open("mypickle.pkl",'wb')
    pickle.dump(my_list,f)
    f.close()
def unpickler(list):
    f=open("mypickle.pkl",'rb')
    my_list=pickle.load(f)
    f.close() 
    return my_list

