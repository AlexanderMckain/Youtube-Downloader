import pytube

url = input("Enter Youtube Video URL:")
OnlyAudio = input("Get audio only version y/n:")
outputfilename = input("Output file name:")
yt = pytube.YouTube(url)

if OnlyAudio == "y":
    yt.streams.get_audio_only().download(output_path="./output", filename=outputfilename + ".mp3")
    print("downloaded audio from", url)
else:
    yt.streams.get_highest_resolution().download(output_path="./output",filename=outputfilename + ".mp4")
    print("downloaded video from", url)