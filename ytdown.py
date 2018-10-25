#importing the module
from pytube import YouTube

#where to save
SAVE_PATH = "/home/sagar/Ajit/Python/Youtube/VIDEOS"

#link of the video to be downloaded
links = open('links.txt','r')

for l in links:
	get_true = True
	while get_true:
		try:
			#object creation using YouTube which was imported in the beginning 
			yt = YouTube(l)
			#get_true = False
		except:
			print("Connection Error") #to handle exception
			continue
	#import pdb; pdb.set_trace()

	#filters out all the files with "mp4" extension
	mp4files = yt.streams.filter(progressive=True ,file_extension='mp4').all()
	try:
		print(yt.filename)
		print(mp4files[-1])
	except:
		pass
	video = mp4files[-1]
	# video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		video.download(output_path=SAVE_PATH)
	except:
		print("Some error")
print('Task Completed')
		



