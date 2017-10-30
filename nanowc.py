#!/usr/bin/python3

import hashlib
import requests

from datetime import datetime
from subprocess import run
from subprocess import PIPE

if __name__ == "__main__":

    if datetime.now().month == 11:
        with open("/home/the-hawk/.nanocount", 'r') as secret:
            key = secret.read().strip().encode('utf-8')

        name = b'the-hawk'
        count = run(['/home/the-hawk/nanowrimo/build', 'wc'],
                    stdout=PIPE).stdout.strip()

        print(f'NaNoWriMo is in session. Reporting {int(count)} words.')

        h = hashlib.sha1()
        h.update(key)
        h.update(name)
        h.update(count)

        payload = {'hash': h.hexdigest(),
                   'name': name.decode('utf-8'),
                   'wordcount': count.decode('utf-8')}

        response = requests.put("http://nanowrimo.org/api/wordcount", payload)
        print("IF YOU ARE SEEING THIS, YOU HAVEN'T FINISHED TESTING THIS!!!")
    else:
        print("NaNoWriMo not in session. Skipping word count update.")