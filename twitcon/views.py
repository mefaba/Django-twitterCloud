from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import json


tweetler = []

def index(request):
	context= { }
	if request.method == "POST":

		uploaded_file = request.FILES['tweetler']

		tweetdata = pd.read_csv(uploaded_file,encoding = "utf8")
		tweetler = []
		for i in tweetdata["text"]:
			tweetler.append(i)
		tweetler_notlist = ''.join(tweetler)
		tweetler_splited = tweetler_notlist.split()

	    #How to count repeated words=
		tweets_counted = {}
		for kelime in tweetler_splited:
			if kelime not in tweets_counted:
				tweets_counted[kelime] = 1
			elif kelime in tweets_counted:
				tweets_counted[kelime] +=1
		content_file = list(map(list, tweets_counted.items()))

		return render(request, 'upload.html', {'uploaded_file': uploaded_file, 'content_file': content_file})

	else:
		return render(request,'index.html',context)



# tweetdata = pd.read_csv("C:/Users/Mefa/Jupyter Workshop/Datasetler/twitter_archieve.csv",encoding = "utf8")
# def tweetclouder(tweetdata):
#     tweetler= []

#     for i in tweetdata["text"]:
#         tweetler.append(i)

#     tweetler_notlist = ''.join(tweetler)
#     tweetler_splited = tweetler_notlist.split()

#     #How to count repeated words=
#     tweets_counted = {}
#     for kelime in tweetler_splited:
#         if kelime not in tweets_counted:
#             tweets_counted[kelime] = 1
#         elif kelime in tweets_counted:
#             tweets_counted[kelime] +=1
#     ######### ############ ###########         
#     wc = WordCloud(max_words=1000, margin=2,
#                    random_state=1).generate_from_frequencies(tweets_counted, max_font_size=100)
#     wc.to_file("twitcloud.png")
#     # store default colored image
 


# def upload(request):
# 	if request.method == POST:

# 		uploaded_file = request.FILES('tweetler')
# 		fs = FileSystemStorage()
# 		fs.save(upload_file.name, uploaded_file)


# 		context= { }

# 	else:
# 		return render(request,'upload.html',context)

	    ######### ############ ###########         
		# tweets_json = json.dumps(tweets_counted)
		# tweets_json = json.dumps(thisdict)
		# content_file = tweets_json
		#wordcloud data = tweetclouder(tweetdata)
		#content_file = uploaded_file.read()
		#fs = FileSystemStorage()
		# fs.save(upload_file.name, uploaded_file)
		# if uploaded_file:

		# Create your views here.

# if request.method == 'POST':
#     file1 = request.FILES['file']
#     contentOfFile = file1.read()
#     if file1:
#         return render(request, 'blogapp/Statistics.html', {'file': file1, 'contentOfFile': contentOfFile})

		#content_file = csv.reader(uploaded_file)