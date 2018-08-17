#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

env = sys.argv[1]
var_num = len(sys.argv)
if var_num > 2:
    print 'just need  1 parameter!'
    sys.exit()
else:
    if env == 'dev':
        cmd = 'ansible-playbook -i hosts-dev assign-template-redis.yml -t assign -e "@envs/redis-dev.yml"'
        os.system(cmd)
    elif env == 'sit':
        cmd = 'ansible-playbook -i hosts-dev assign-template-redis.yml -t assign -e "@envs/redis-sit.yml"'
        os.system(cmd)
    elif env == 'prod':
        cmd = 'ansible-playbook -i hosts-prod assign-template-redis.yml -t assign -e "@envs/redis-prod.yml"'
        os.system(cmd)