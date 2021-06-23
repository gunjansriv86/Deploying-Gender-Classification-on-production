from sklearn.base import BaseEstimator,TransformerMixin
import syllables
import phonetics
import re
import numpy

class NameFeature(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.features=numpy.vectorize(self.features)
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        return self.features(X)
    def features(self,X):
        return ({
            'first-letter':X[0],
            'first-2letter':X[:2],
            'first-3letter':X[:3],
            'last-letter':X[-1],
            'last-2letter':X[-2:],
            'last-3letter':X[-3:],
            'namelength':len(X),
            'startswithvowel':1 if X[0] in 'aeiou' else 0,
            'endwithvowel':1 if X[-1] in 'aeiou' else 0,
            'noofsyllable':syllables.estimate(X),
            #'soundex':phonetics.soundex(name)
            'metaphone':phonetics.metaphone(X)
            #'nys':ph.nysiis(name)
            #'count':cnt
        })

class CleanName(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.getfirstname=numpy.vectorize(self.getfirstname)
        pass

    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        return self.getfirstname(X)
    
    def getfirstname(self,X):
        #remove names starting with 'cust', cust-019292020 etc
        try:
            if len(X)<3 or X[:4]=='cust':
                X='noname'

            #split the name , sometime firstname column also has surname
            
            X=X.split()[0]
            
            #remove occurences xxxxx,zzzzz,---,.....,@@ etc
            X=''.join(re.findall('[x|z|-]*([a-zA-Z]+?)[z|x|-]*',X))

            if not X.isalpha():
                X='noname'
            if len(X)<3:
                X='noname'
        except:
            print(X)
        return X