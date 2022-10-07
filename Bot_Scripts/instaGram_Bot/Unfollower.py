import instabot

print(r"""
  _    _       ______    _ _
 | |  | |     |  ____|  | | |
 | |  | |_ __ | |__ ___ | | | _____      _____ _ __
 | |  | | '_ \|  __/ _ \| | |/ _ \ \ /\ / / _ \ '__|
 | |__| | | | | | | (_) | | | (_) \ V  V /  __/ |
  \____/|_| |_|_|  \___/|_|_|\___/ \_/\_/ \___|_|
""")
username = input("Enter your username : ")
password = input("Enter you password : ")

bot = instabot.Bot()
bot.login(username=username, password=password)


def unfollow():
    select = int(input('''
    1) Unfollow erveyone
    2) Unfollow non-followers
    3)List non-follower
    4)Exit
    \tSelect option : '''))

    if select == 1:
        bot.unfollow_everyone()
    elif select == 2:
        bot.unfollow_non_followers()
    elif select == 3:
        followers = bot.get_user_followers(username)
        followings = bot.get_user_following(username)
        for i in range(len(followings)):
            if followings[i] not in followers:
                print(bot.get_username_from_user_id(followings[i]))
    elif select == 4:
        exit()
    else:
        pass
    unfollow()


unfollow()
