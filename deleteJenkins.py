# coding=utf-8
import jenkins

# 获取jenkins连接
server = jenkins.Jenkins('http://jenkins.66123123.com', username='', password='')

jobs = server.get_all_jobs()

jobs_str = '['
for job in jobs:
    jobs_str = jobs_str + '\'' + job['name'] + '\','
    del_job = server.delete_job(job['name'])
jobs_str = jobs_str[:-1] + ']'
