from pytube import YouTube
#function to import the Python Pytube library 

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    #command will automatically download the highest resolution available

    try:
        youtubeObject.download()
    except:
        print("An error has occurred, please fix it")
        #implemented the Try and Except to return an error message if the download fails

    print("Download is completed successfully, now you can enjoy Music")
    #it will print out that the download is completed successfully.


link = input("Enter the YouTube video link: ")
Download(link)

