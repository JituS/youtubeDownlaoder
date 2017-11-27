import pytube
inputLink = input()

def displayProgress(stream, chunk, file_handle, remainingBytes):
	if(remainingBytes % 100 == 0):
		print(int(file_handle.tell() * 100 / (file_handle.tell() + remainingBytes)),' %')

yt = pytube.YouTube(inputLink)
yt.register_on_progress_callback(displayProgress)
vids = yt.streams.filter(subtype = 'mp4',progressive = True).all()
print('Choose video type: ')
for i in range(len(vids)):
	print(i, '. ', vids[i])

sno = int(input())
vids[sno].download()
print('completed !')
