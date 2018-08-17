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
    if env == 'perf':
        cmd = 'ansible-playbook -i hosts-perf assign-template-eloan.yml -t assign -e "@envs/eloan-perf.yml"'
        os.system(cmd)
    elif env == 'dev':
        cmd = 'ansible-playbook -i hosts-dev assign-template-eloan.yml -t assign -e "@envs/eloan-dev.yml"'
        os.system(cmd)
    elif env == 'prod':
        cmd = 'ansible-playbook -i hosts-prod assign-template-eloan.yml -t assign -e "@envs/eloan-prod.yml"'
        os.system(cmd)
    elif env == 'dev-refactor':
        cmd = 'ansible-playbook -i hosts-dev assign-template-eloan.yml -t assign -e "@envs/eloan-dev-refactor.yml"'
        os.system(cmd)
