import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import json
	
class MF():
    def __init__(self, R=np.array([
                        [5, 3, 0, 1],
                        [4, 0, 0, 1],
                        [1, 1, 0, 5],
                        [1, 0, 0, 4],
                        [0, 1, 5, 4],]),
                        K=34, alpha=0.1, beta=0.01, iterations=20):
        """
        Perform matrix factorization to predict empty
        entries in a matrix.
        
        Arguments
        - R (ndarray)   : user-item rating matrix
        - K (int)       : number of latent dimensions
        - alpha (float) : learning rate
        - beta (float)  : regularization parameter
        """
        
        self.R = R
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    def train(self):
        # Initialize user and item latent feature matrice
        self.P = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1./self.K, size=(self.num_items, self.K))
        
        # Initialize the biases
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.R[np.where(self.R != 0)])
        
        # Create a list of training samples
        self.samples = [
            (i, j, self.R[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.R[i, j] > 0
        ]
        
        # Perform stochastic gradient descent for number of iterations
        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            rmse = self.rmse()
            training_process.append((i, rmse))
            if (i+1) % 10 == 0:
                print("Iteration: %d ; error = %.4f" % (i+1, rmse))
        
        return training_process

    def rmse(self):
        """
        A function to compute the root mean square error
        """
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        n=0
        for x, y in zip(xs, ys):
            n=n+1
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return math.sqrt(error/n)

    def sgd(self):
        """
        Perform stochastic graident descent
        """
        for i, j, r in self.samples:
            # Computer prediction and error
            prediction = self.get_rating(i, j)
            e = (r - prediction)
            
            # Update biases
            self.b_u[i] += self.alpha * (2*e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (2*e - self.beta * self.b_i[j])
            
            # Create copy of row of P since we need to update it but use older values for update on Q
            P_i = np.copy(self.P[i,:])
            
            # Update user and item latent feature matrices
            for k in range(self.K):
                self.P[i,k]+=self.alpha * (2*e * self.Q[j,k] - self.beta * self.P[i,k])
            for k in range(self.K):
                self.Q[j,k] += self.alpha * (2*e * P_i[k] - self.beta * self.Q[j,k])

    def get_rating(self, i, j):
        """
        Get the predicted rating of user i and item j
        """
        prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        return prediction
    
    def full_matrix(self):
        """
        Computer the full matrix using the resultant biases, P and Q
        """
        return self.b + self.b_u[:,np.newaxis] + self.b_i[np.newaxis:,] + self.P.dot(self.Q.T)
    
    def newuser(self,ratings):
        newuserP = np.random.normal(scale=1./self.K, size=self.K)
        newuserbias = 0
        tp=[]
        for i0 in range(40):
            np.random.shuffle(ratings)
            for i in ratings:
                prediction = self.b + newuserbias + self.b_i[int(i[0])] + newuserP.dot(self.Q[int(i[0]), :].T)
                e = (i[1] - prediction)
                newuserbias+=self.alpha*(2*e-self.beta*self.b_i[int(i[0])])
                for k in range(self.K):
                    newuserP[k]+=self.alpha * (2*e * self.Q[int(i[0]),k] - self.beta * newuserP[k])
 

            predicted=self.b + newuserbias + self.b_i.T + newuserP.dot(self.Q.T)
            predicted=predicted.T
            error = 0
            n=0
            for i in range(len(ratings)):
                n=n+1
                error += (ratings[i][1]-predicted[i])*(ratings[i][1]-predicted[i])
            rmse=math.sqrt(error/n)
            tp.append((i0, rmse))
            if(rmse<0.7):
                break
        #x = [x for x, y in tp]
        #y = [y for x, y in tp]
        #plt.figure(figsize=((16,4)))
        #plt.plot(x, y)
        #plt.xticks(x, x)
        #plt.xlabel("Iterations")
        #plt.ylabel("Root mean Square Error")
        #plt.grid(axis="y")
        predicted=self.b + newuserbias + self.b_i.T + newuserP.dot(self.Q.T)
        predicted=predicted.T
        return predicted
    
    def savemodel(self):
        f= open("data/Factorized/Other.csv","w+")
        f.write(str("%.3f"%self.K)+"\n")
        f.write(str("%.3f"%self.alpha)+"\n")
        f.write(str("%.3f"%self.beta)+"\n")
        f.write(str("%.3f"%self.b)+"\n")
        f.close()
        np.savetxt("data/Factorized/Factorized.csv", mf.full_matrix(), fmt='%.3f',  delimiter=",")
        np.savetxt("data/Factorized/P.csv", mf.P, fmt='%.3f',  delimiter=",")
        np.savetxt("data/Factorized/Q.csv", mf.Q, fmt='%.3f',  delimiter=",")
        np.savetxt("data/Factorized/User_bias.csv", mf.b_u, fmt='%.3f',  delimiter=",")
        np.savetxt("data/Factorized/Item_bias.csv", mf.b_i, fmt='%.3f',  delimiter=",")
        
    def loadmodel(self):
        with open("data/Factorized/Other.csv") as f:
            mylist = f.read().splitlines()
        self.K=int(float(mylist[0]))
        self.alpha=float(mylist[1])
        self.beta=float(mylist[2])
        self.b=float(mylist[3])
        Tmp_df=pd.read_csv("data/Factorized/P.csv")
        self.P=Tmp_df.values
        Tmp_df=pd.read_csv("data/Factorized/Q.csv")
        self.Q=Tmp_df.values
        Tmp_df=pd.read_csv("data/Factorized/User_bias.csv")
        self.b_u=Tmp_df.values
        Tmp_df=pd.read_csv("data/Factorized/Item_bias.csv")
        self.b_i=Tmp_df.values



def setratings(User_ratings_df):
	Links_df=pd.read_csv("data/Start/links.csv")
	Links_df["impindex"]=Links_df.index
	Links_df.set_index('imdbId',inplace=True)
	User_ratings_df=pd.concat([User_ratings_df["Const"], User_ratings_df["Your Rating"]], axis=1)
	for i in User_ratings_df.index:
		User_ratings_df["Const"].loc[i]=int(User_ratings_df["Const"].loc[i][2:])
	User_ratings_df.set_index('Const', inplace=True)
	a=Links_df.index.values
	b=User_ratings_df.index.values.astype(int)
	c=np.intersect1d(a, b)
	d=np.empty([len(c),2])
	for i in range(len(c)):
		d[i,0]=Links_df["impindex"].loc[c[i]]
		d[i,1]=User_ratings_df["Your Rating"].loc[c[i]]/2
	return d
	
def factorize():
	R_df=pd.read_csv("data/Start/ratings.csv")
	R_df = R_df.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
	R=R_df.values
	mf = MF(R, K=34, alpha=0.02, beta=0.02, iterations=20)
	training_process = mf.train()
	mf.savemodel()
	print("P x Q:")
	print(mf.full_matrix())
	print()
	#x = [x for x, y in training_process]
	#y = [y for x, y in training_process]
	#plt.figure(figsize=((16,4)))
	#plt.plot(x, y)
	#plt.xticks(x, x)
	#plt.xlabel("Iterations")
	#plt.ylabel("Root mean Square Error")
	#plt.grid(axis="y")
	return mf
	
def finalfactorize():
	mf=factorize()
	mf.savemodel()
	
def getrecomendations():
	User_ratings_df=pd.read_csv("data/Users_ratings/ratings.csv", encoding = "ISO-8859-1")
	ratings=setratings(User_ratings_df)
	mf=MF()
	mf.loadmodel()
	recomendations=mf.newuser(ratings)
	for i in ratings:
		recomendations[int(i[0])][0]=0
	top=np.empty(10)
	for i in range(len(top)):
		max=0
		for j in range(len(recomendations)):
			if(recomendations[j][0]>recomendations[max][0]):
				max=j
		top[i]=max
		recomendations[max][0]=0
	Links_df=pd.read_csv("data/Start/links.csv")
	Movies_df=pd.read_csv("data/Start/movies.csv")
	topdata=[]    
	for i in range(len(top)):
		topdata.append(str(Links_df["imdbId"].loc[top[i]]))
	print(topdata)
	return json.dumps(topdata)



import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './data/Users_ratings'
ALLOWED_EXTENSIONS = set(['csv', 'json'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/results')
def results():
	return '''
			<!doctype html>
				<head>
					<title>
						OneTouchMovies
					</title>
					<link rel="stylesheet" href="'''+url_for('static', filename='otm1.css')+'''"/> 
				</head>
				<body onkeydown="return (event.keyCode != 116)">
					<div id="data">'''+str(getrecomendations())+'''</div>
					<div id="root" align="center">
						<script src="'''+url_for('static', filename='otm1.js')+'''"></script>
					</div>
				</body>
			</html>'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		#check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			#flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('results'))
	return '''
	<!doctype html>
		<head>
			<title>
				OneTouchMovies
			</title>
			<link rel="stylesheet" href="'''+url_for('static', filename='otm.css')+'''">
		</head>
		<body>
			<div id="root" align="center">
				<h1>Send your rating.csv file from imdb</h1>
				<form method=post enctype=multipart/form-data>
					<div class="upload-btn-wrapper">
					  <button class="btn">Choose a file</button>
					  <input type="file" name=file />
					</div><br>
					<div class="upload-btn-wrapper">
					  <button class="btn">Upload</button>
					  <input type="submit" value=Upload>
					</div>
				</form>
			</div>
		</body>
	</html>
	'''

from flask import send_from_directory

#@app.route('/ratings/<filename>')
#def uploaded_file(filename):
	#return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


#TO_DO
#0.Найти не битый movies.csv
#1.Переверстать
#2.Подумать, что делать, когда несколько файлов отправляются одновременно