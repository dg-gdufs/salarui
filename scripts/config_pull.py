# encoding: utf-8

import os

def run():
    for i in os.listdir('config'):
        if not i.endswith('_default.py'):
            continue
        i = 'config/' + i
        with open(i,'r',encoding='utf-8') as input, open(i.replace('_default',''),'w',encoding='utf-8') as output:
            output.write(input.read())
    

# 拉取配置脚本
# python scripts/config_pull.py
if __name__ == "__main__":
    run()