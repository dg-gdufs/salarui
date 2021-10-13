# coding=utf-8

import time
import os
import re
from fire import Fire

from config.host_config import LOG_DEFAULT_HOME

def run(days_ago=1):
    up_time = int(time.time()) - 86400*days_ago
    if not os.path.exists(LOG_DEFAULT_HOME):
        print("path not found")
        return
    for i in os.listdir(LOG_DEFAULT_HOME):
        file_time = re.findall(r"\[(.*?)\]", i)
        if not file_time:
            continue
        file_time = time.mktime(time.strptime(file_time[0].split(' ')[0],"%Y-%m-%d"))
        if file_time < up_time:
            os.remove("./logs/" + i)
    print("clean success")

# 定时清理log文件
# python -m scripts.log_clean
if __name__ == "__main__":
    Fire(run)