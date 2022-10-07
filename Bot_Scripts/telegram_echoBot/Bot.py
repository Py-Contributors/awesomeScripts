import requests

bot_API = 'PAST_BOT_API_HERE'

previous_update_id = None

try:
    print('Bot is Up running now...')
    while(True):
        message = requests.get(
            f'https://api.telegram.org/bot{bot_API}/getUpdates'
        ).json()
        update_id = message['result'][-1]['update_id']
        if update_id != previous_update_id:
            user = str(message['result'][-1]['message']['from']['id'])
            replay_message = message['result'][-1]['message']['text']
            requests.get((
                'https://api.telegram.org/bot' + bot_API
                + '/sendMessage?chat_id=' + user
                + '&text=' + replay_message
            ))
            previous_update_id = update_id
except message.status == 404:
    print('Somthing Wrong......!!!!!!!!')
