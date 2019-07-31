# coding=utf-8
import jenkins

# 获取jenkins连接
server = jenkins.Jenkins('http://jenkins.66123123.com', username='leading2018', password='leading201911')

# 上游项目构建完成后是否构建下游项目
UPSTREAM_CHANGES = 'true'

# 需要创建的job列表
service = ['authorization-service', 'file-service', 'location-service', 'product-service', 
            'supplier-service', 'user-service', 'warehouse-service', 'mapping-service', 'erp-old-service',
            'customer-service', 'elasticsearch-service', 'marketing-service',
            'mall-release-service', 'shoppe-release-service', 'mainsite-release-service', 'order-service',
            'bill-service', 'purchase-service', 'notice-service', 'statistics-service', 'timedtask-service',
            'mall-api-service', 'bidding-service', 'leading-openapi-gateway', 'leading-sync-elasticsearch']

base = ['leading-common', 'leading-datasource', 'leading-distributed-lock', 'leading-idempotent-component',
 'leading-parent-pom', 'leading-resource-base']

control = ['service-api-gateway', 'service-registry', 'turbine-dashboard', 'spring-boot-admin', 'configuration-server']

jobs_arr = base
gitlab_prefix = 'http://gitlab.66123123.com/leading-service/'
gitlab_suffix = '.git'
group_id = 'com.leading'
command = "curl -u &quot;admin:Harbor12345&quot; -X DELETE -H &quot;Content-Type: application/json&quot; &quot;http://harbor.66123123.com/api/repositories/library/"
for jobs_name in jobs_arr:
    # gitlab地址
    gitlab_url = gitlab_prefix + jobs_name + gitlab_suffix

    if 'datasource' in jobs_name:
        group_id = 'com.leading.db'

    if '123' in jobs_name:
        # with open('config-api-235.xml') as f:
        #     profile = f.read()
        # JOB_CONFIG_235 = profile.replace("GITLAB_URL", gitlab_url) \
        #     .replace("GROUP_ID", group_id) \
        #     .replace("JOB_NAME", jobs_name) \
        #     .replace("GOALS", "clean deploy -P dev") \
        #     .replace("SSH_CONFIG_NAME", "235") \
        #     .replace("SSH_CONFIG_COMMAND", "/home/leading/leading_redeploy.sh " + jobs_name) \
        #     .replace("GIT_BRANCH", "feature-initialization") \
        #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
        # server.create_job("235_" + jobs_name, JOB_CONFIG_235)
            
        # with open('config-api.xml') as f:
        #     profile = f.read()
        # JOB_CONFIG_DEV = profile.replace("GITLAB_URL", gitlab_url) \
        #     .replace("GROUP_ID", group_id) \
        #     .replace("JOB_NAME", jobs_name) \
        #     .replace("GOALS", "clean deploy -P alldev") \
        #     .replace("SSH_CONFIG_NAME", "dev") \
        #     .replace("SSH_CONFIG_COMMAND", "/home/dev/leading_redeploy.sh " + jobs_name) \
        #     .replace("GIT_BRANCH", "develop") \
        #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
        # server.create_job("DEV_" + jobs_name, JOB_CONFIG_DEV)

        # JOB_CONFIG_TEST = profile.replace("GITLAB_URL", gitlab_url) \
        #     .replace("GROUP_ID", group_id) \
        #     .replace("JOB_NAME", jobs_name) \
        #     .replace("GOALS", "clean deploy -P test") \
        #     .replace("SSH_CONFIG_NAME", "test") \
        #     .replace("SSH_CONFIG_COMMAND", "/home/test/leading_redeploy.sh " + jobs_name) \
        #     .replace("GIT_BRANCH", "release") \
        #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
        # server.create_job("TEST_" + jobs_name, JOB_CONFIG_TEST)

        # JOB_CONFIG_PP = profile.replace("GITLAB_URL", gitlab_url) \
        #     .replace("GROUP_ID", group_id) \
        #     .replace("JOB_NAME", jobs_name) \
        #     .replace("GOALS", "clean deploy -P pp") \
        #     .replace("SSH_CONFIG_NAME", "test") \
        #     .replace("SSH_CONFIG_COMMAND", "/home/test/leading_redeploy.sh " + jobs_name) \
        #     .replace("GIT_BRANCH", "release") \
        #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
        # server.create_job("PP_" + jobs_name, JOB_CONFIG_PP)

        # JOB_CONFIG_PROD = profile.replace("GITLAB_URL", gitlab_url) \
        #     .replace("GROUP_ID", group_id) \
        #     .replace("JOB_NAME", jobs_name) \
        #     .replace("GOALS", "clean deploy -P prod") \
        #     .replace("GIT_BRANCH", "release") \
        #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES)
        # server.create_job("PROD_" + jobs_name, JOB_CONFIG_PROD)
        continue
    else:
        try:
            # with open('config-235.xml') as f:
            #     profile = f.read()
            # command_latest = command + jobs_name + "-dev/tags/" + "latest" + "&quot; --insecure"
            # command_version = command + jobs_name + "-dev/tags/" + "${POM_VERSION}" + "&quot; --insecure"
            # JOB_CONFIG_235 = profile.replace("GITLAB_URL", gitlab_url) \
            #     .replace("GROUP_ID", group_id) \
            #     .replace("JOB_NAME", jobs_name) \
            #     .replace("GOALS", "clean package docker:build -Dmaven.test.skip=true -U -P dev") \
            #     .replace("SSH_CONFIG_NAME", "235") \
            #     .replace("SSH_CONFIG_COMMAND", "/home/leading/leading_redeploy.sh " + jobs_name + "-dev") \
            #     .replace("COMMAND", command_latest + " &amp;&amp; " + command_version) \
            #     .replace("GIT_BRANCH", "feature-initialization") \
            #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            #     .replace("TIME_OUT","1000000000")
            # print("235_" + jobs_name + " create success")
            # server.create_job("235_" + jobs_name, JOB_CONFIG_235)

            # with open('config.xml') as f:
            #     profile = f.read()
            # command_latest = command + jobs_name + "-alldev/tags/" + "latest" + "&quot; --insecure"
            # command_version = command + jobs_name + "-alldev/tags/" + "${POM_VERSION}" + "&quot; --insecure"
            # JOB_CONFIG_DEV = profile.replace("GITLAB_URL", gitlab_url) \
            #     .replace("GROUP_ID", group_id) \
            #     .replace("JOB_NAME", jobs_name) \
            #     .replace("GOALS", "clean package docker:build -Dmaven.test.skip=true -U -P alldev") \
            #     .replace("SSH_CONFIG_NAME", "dev") \
            #     .replace("SSH_CONFIG_COMMAND", "/home/dev/leading_redeploy.sh " + jobs_name + "-alldev") \
            #     .replace("COMMAND", command_latest + " &amp;&amp; " + command_version) \
            #     .replace("GIT_BRANCH", "develop") \
            #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            #     .replace("TIME_OUT","120000") \
            #     .replace("TIME_TASK", '''5 1 * * *
            #         25 12 * * *''')
            # print("DEV_" + jobs_name + " create success")
            # server.create_job("DEV_" + jobs_name, JOB_CONFIG_DEV)

            # command_latest = command + jobs_name + "-test/tags/" + "latest" + "&quot; --insecure"
            # command_version = command + jobs_name + "-test/tags/" + "${POM_VERSION}" + "&quot; --insecure"
            # JOB_CONFIG_TEST = profile.replace("GITLAB_URL", gitlab_url) \
            #     .replace("GROUP_ID", group_id) \
            #     .replace("JOB_NAME", jobs_name) \
            #     .replace("GOALS", "clean package docker:build -Dmaven.test.skip=true -U -P test") \
            #     .replace("SSH_CONFIG_NAME", "test") \
            #     .replace("SSH_CONFIG_COMMAND", "/home/test/leading_redeploy.sh " + jobs_name + "-test") \
            #     .replace("COMMAND", command_latest + " &amp;&amp; " + command_version) \
            #     .replace("GIT_BRANCH", "release") \
            #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            #     .replace("TIME_OUT","120000") \
            #     .replace("TIME_TASK", '''5 2 * * *
            #         45 12 * * *''')
            # print("TEST_" + jobs_name + " create success")
            # server.create_job("TEST_" + jobs_name, JOB_CONFIG_TEST)


            with open('config-pp.xml') as f:
                profile = f.read()
            command_latest = command + jobs_name + "-pp/tags/" + "latest" + "&quot; --insecure"
            command_version = command + jobs_name + "-pp/tags/" + "${POM_VERSION}" + "&quot; --insecure"
            JOB_CONFIG_PP = profile.replace("GITLAB_URL", gitlab_url) \
                .replace("GROUP_ID", group_id) \
                .replace("JOB_NAME", jobs_name) \
                .replace("GOALS", "clean package docker:build -Dmaven.test.skip=true -U -P pp") \
                .replace("SSH_CONFIG_NAME1", "pp1") \
                .replace("SSH_CONFIG_COMMAND1", "/home/pp1/leading_redeploy.sh " + jobs_name + "-pp") \
                .replace("SSH_CONFIG_NAME2", "pp2") \
                .replace("SSH_CONFIG_COMMAND2", "/home/pp2/leading_redeploy.sh " + jobs_name + "-pp") \
                .replace("COMMAND", command_latest + " &amp;&amp; " + command_version) \
                .replace("GIT_BRANCH", "release") \
                .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
                .replace("TIME_OUT","120000") \
                .replace("TIME_TASK", "5 3 * * *")
            print("PP_" + jobs_name + " create success")
            server.create_job("PP_" + jobs_name, JOB_CONFIG_PP)

            # with open('config.xml') as f:
            #     profile = f.read()
            # command_latest = command + jobs_name + "-prod/tags/" + "latest" + "&quot; --insecure"
            # command_version = command + jobs_name + "-prod/tags/" + "${POM_VERSION}" + "&quot; --insecure"
            # JOB_CONFIG_PROD = profile.replace("GITLAB_URL", gitlab_url) \
            #     .replace("GROUP_ID", group_id) \
            #     .replace("JOB_NAME", jobs_name) \
            #     .replace("GOALS", "clean package docker:build -Dmaven.test.skip=true -U -P prod") \
            #     .replace("SSH_CONFIG_NAME", "prod") \
            #     .replace("SSH_CONFIG_COMMAND", "/tmp/leading_redeploy.sh " + jobs_name + "-prod") \
            #     .replace("COMMAND", command_latest + " &amp;&amp; " + command_version) \
            #     .replace("GIT_BRANCH", "release") \
            #     .replace("UPSTREAM_CHANGES",UPSTREAM_CHANGES) \
            #     .replace("TIME_OUT","120000")
            # print("PROD_" + jobs_name + " create success")
            # server.create_job("PROD_" + jobs_name, JOB_CONFIG_PROD)
        except jenkins.JenkinsException:
            print("error,"+jobs_name+" Already Exist")
        continue