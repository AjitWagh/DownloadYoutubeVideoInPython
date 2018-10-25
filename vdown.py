from pytube import YouTube

SAVE_PATH = "/home/sagar/Ajit/Python/Youtube/VIDEOS"
links = open('links.txt','r')

for l in links:
	get_true = True
	while get_true:
		try:
			yt = YouTube(l)
		except:
			print("Connection Error") 
			continue
	mp4files = yt.streams.filter(progressive=True ,file_extension='mp4').all()
	try:
		print(yt.filename)
		print(mp4files[-1])
	except:
		pass
	video = mp4files[-1]
	try:
		video.download(output_path=SAVE_PATH)
	except:
		print("Some error")
    print('Task Completed')
		



