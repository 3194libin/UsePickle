import pickle
my_list = [12,45.1,'哈哈',['another list]']]
pickle_file = open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()