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
        cmd = 'ansible-playbook -i hosts-dev assign-template-lbpm.yml -t assign -e "@envs/lbpm-dev.yml"'
        os.system(cmd)
    elif env == 'sit':
        cmd = 'ansible-playbook -i hosts-dev assign-template-lbpm.yml -t assign -e "@envs/lbpm-sit.yml"'
        os.system(cmd)
    elif env == 'prod':
        cmd = 'ansible-playbook -i hosts-prod assign-template-lbpm.yml -t assign -e "@envs/lbpm-prod.yml"'
        os.system(cmd)