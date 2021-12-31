import requests
import time
from datetime import datetime
from lib.utils import get_property, read_json, send_email


def trigger_all_collections():
    response = requests.post(url='https://hubble.makemytrip.com:443/hubble/allCollections',
                             headers=read_json('resources/headers_allCollections.json'),
                             json=read_json('resources/payload_allCollections.json'),
                             verify=False)

    response.raise_for_status()
    return response


def trigger_force_sync_content(jit_content_id_list):
    base_uri = get_property('config.properties', 'contentManagerIpProd')
    payload = {
        'id': jit_content_id_list
    }

    response = requests.post(url='http://' + base_uri + '/hubble/contentmanager/forceSyncContent',
                             headers=read_json('resources/headers_forceSyncContent.json'),
                             json=payload)

    return response


if __name__ == '__main__':
    while True:
        # make a call to allCollections service and extract all the contentIds for 'Just In' from the response
        ac_parsed_json_resp = trigger_all_collections().json()
        contents_list = ac_parsed_json_resp['jitContent']['contents']
        content_id_list = list(map(lambda content: content.split('`')[0], contents_list))

        # make a call to forceSyncContent service and synchronize all the 'Just In' contents
        fsc_resp = trigger_force_sync_content(content_id_list)
        display_message = '[' + str(datetime.now()) + ']' \
                          + '\nStatus Code: ' + str(fsc_resp.status_code) + '\nResponse:\n' + fsc_resp.text + '\n\n'

        # on successful execution print the message, else print the error message and also deliver it via mail
        if fsc_resp.status_code == 200:
            print(display_message)
        else:
            print(display_message)
            send_email('qtest4433@gmail.com', 'makemytrip@123', 'defiant.dj04@gmail.com',
                       'forceSyncContent Service Failure Report', display_message)
            break

        # keep executing the same task for every N minutes
        delay_in_minutes = int(get_property('config.properties', 'delayInMins'))
        time.sleep(delay_in_minutes * 60)
