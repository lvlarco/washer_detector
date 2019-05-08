import requests
import config


def send_ifttt_request(event):
    """Sends event to IFTTT"""
    maker_url = 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'.format(event, config.API_KEY)
    print("Sending request to IFTTT")
    return requests.post(maker_url)

def main():
    event = 'washer_stopped_sms'
    # event = 'washer_stopped_notification'
    send_ifttt_request(event)


main()






