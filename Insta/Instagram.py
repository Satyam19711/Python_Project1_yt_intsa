import instaloader
 
profile_name = input("Enter your Instagram Profile name: ")


print("Downloading profile pic...")


instaloader.Instaloader().download_profile(profile_name, profile_pic_only= True)
print("Download Completed, Now you can see the profile picture")


print("Downloading all posts...")


instaloader.Instaloader().download_profile(profile_name, profile_pic_only= False)
print("Download Completed, Now you can see all the posts of this ID")

