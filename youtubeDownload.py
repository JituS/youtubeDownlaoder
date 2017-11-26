import pytube
inputLink = input()

def displayProgress(stream, chunk, file_handle, remainingBytes):
	if(remainingBytes % 100 == 0):
		print(int(file_handle.tell() * 100 / (file_handle.tell() + remainingBytes)),' %')

yt = pytube.YouTube(inputLink)
yt.register_progress_callback(displayProgress)
vids = yt.streams.filter(subtype = 'mp4',progressive = True).all()
for i in range(len(vids)):
	print('Choose vidio type')
	print(i, '. ', vids[i])

sno = int(input())
vids[sno].download()
print('completed !')
