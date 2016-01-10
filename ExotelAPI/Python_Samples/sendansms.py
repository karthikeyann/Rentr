#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import requests

from settings import sid, token


def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })


if __name__ == '__main__':
    # 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
    # For promotional, this will be ignored by the SMS gateway
    # Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)
    r = send_message(sid, token,
        sms_from='09243422233',  # sms_from='8808891988',
        sms_to='09489244684', # sms_to='9052161119',
        #sms_body='Hi Karthik, Your house tour with HostMe has been allocated and confirmed for your Order ID. Your cab will pick you up. Amount  of Rs. 2999/- has been charged through your PayTM wallet. For further assistance please call 9998854321')
        sms_body='Hi Karthik, Your rent house tour slot has been allocated and confirmed for your Order ID: Uber booked with Bill Amount  2999. For further assistance please call 9998854321')
    print r.status_code
    pprint(r.json())
