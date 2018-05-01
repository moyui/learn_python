# -*- coding: utf-8 -*-
import os
import json
import random

class RandomRroxy(object):
    path = "./douban/pool.json"
    propath = os.path.abspath(path)
    with open(propath, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)

    def process_request(self, request, spider):
        proxy = random.choice(self.load_dict)
        request.meta['proxy'] = 'https://%s:%s' % (proxy['proxy_address'], proxy['proxy_port'])