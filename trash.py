from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#print help(datasets.fetch_mldata)
#print dir(datasets)

ds = datasets.load_digits()
#print digits.viewkeys()
#print digits.viewitems()
#print help(digits)
#print digits.data.shape
##print digits.target.shape
#print digits.target_names

#print help(digits)

#n_samples, n_features = digits.data.shape

#print n_samples
#print n_features
#print digits.data[0]

#X = digits.images.reshape((len(digits.images), -1))
#print X

rf = RandomForestClassifier(n_estimators = 50)
rf.fit(ds.data,ds.target)
print rf.score(ds.data,ds.target) 
 

