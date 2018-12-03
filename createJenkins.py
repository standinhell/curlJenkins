# coding=utf-8
import jenkins

# 获取jenkins连接
server = jenkins.Jenkins('http://jenkins.66123123.com', username='leading2018', password='leading2018')

# 上游项目构建完成后是否构建下游项目
UPSTREAM_CHANGES = 'true'

# 需要创建的job列表
jobs_arr = ['authorization-service', 'authorization-service-api', 'configuration-server', 'file-service',
            'file-service-api', 'leading-common', 'leading-datasource', 'leading-distributed-lock',
            'leading-idempotent-component', 'leading-parent-pom', 'leading-resource-base', 'location-service',
            'location-service-api', 'product-service', 'product-service-api', 'service-api-gateway', 'service-registry',
            'supplier-service', 'supplier-service-api', 'turbine-dashboard', 'user-service', 'user-service-api',
            'warehouse-service', 'warehouse-service-api', 'mapping-service-api', 'mapping-service', 'erp-old-service', 'organization-service-api',
            'organization-service', 'customer-service-api', 'customer-service']
gitlab_prefix = 'http://gitlab.66123123.com/leading-service/'
gitlab_suffix = '.git'
group_id = 'com.leading'
for jobs_name in jobs_arr:
    # gitlab地址
    gitlab_url = gitlab_prefix + jobs_name + gitlab_suffix

    if 'datasource' in jobs_name:
        group_id = 'com.leading.db'

    if '-service-api' in jobs_name or 'leading' in jobs_name:
        with open('config-api.xml') as f:
            profile = f.read()
        GOALS = 'clean deploy'
        JOB_CONFIG_235 = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "235") \
            .replace("SSH_CONFIG_COMMAND", "/home/leading/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "feature-initialization") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
            

        JOB_CONFIG_DEV = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "dev") \
            .replace("SSH_CONFIG_COMMAND", "/home/dev/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "feature-initialization") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)

        JOB_CONFIG_TEST = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "test") \
            .replace("SSH_CONFIG_COMMAND", "/home/test/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "develop") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)

        server.create_job("235_" + jobs_name, JOB_CONFIG_235)
        server.create_job("DEV_" + jobs_name, JOB_CONFIG_DEV)
        server.create_job("TEST_" + jobs_name, JOB_CONFIG_TEST)
    else:
        with open('config.xml') as f:
            profile = f.read()
        GOALS = 'clean package docker:build -Dmaven.test.skip=true -U'
        JOB_CONFIG_235 = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "235") \
            .replace("SSH_CONFIG_COMMAND", "/home/leading/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "feature-initialization") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            .replace("TIME_OUT","1000000000")

        JOB_CONFIG_DEV = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "dev") \
            .replace("SSH_CONFIG_COMMAND", "/home/dev/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "feature-initialization") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            .replace("TIME_OUT","120000")

        JOB_CONFIG_TEST = profile.replace("GITLAB_URL", gitlab_url) \
            .replace("GROUP_ID", group_id) \
            .replace("JOB_NAME", jobs_name) \
            .replace("GOALS", GOALS) \
            .replace("SSH_CONFIG_NAME", "test") \
            .replace("SSH_CONFIG_COMMAND", "/home/test/leading_redeploy.sh " + jobs_name) \
            .replace("GIT_BRANCH", "develop") \
            .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            .replace("TIME_OUT","120000")

        server.create_job("235_" + jobs_name, JOB_CONFIG_235)
        server.create_job("DEV_" + jobs_name, JOB_CONFIG_DEV)
        server.create_job("TEST_" + jobs_name, JOB_CONFIG_TEST)