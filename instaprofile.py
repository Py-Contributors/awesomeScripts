from instaloader import*      #pip install installer

bot = instaloader.Instaloader()   
username=input()                    #paste the username of which you want to download profile pic 
bot.download_profile(username,profile_pic_only=True)
