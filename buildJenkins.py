# coding=utf-8
import jenkins

# 获取jenkins连接
server = jenkins.Jenkins('http://jenkins.66123123.com', username='leading2018', password='leading201911')

service = ['authorization-service', 'file-service', 'location-service', 'product-service', 
            'supplier-service', 'user-service', 'warehouse-service', 'mapping-service', 'erp-old-service',
            'customer-service', 'elasticsearch-service', 'marketing-service',
            'mall-release-service', 'shoppe-release-service', 'mainsite-release-service', 'order-service',
            'bill-service', 'purchase-service', 'notice-service', 'statistics-service', 'timedtask-service']

base = ['leading-common', 'leading-datasource', 'leading-distributed-lock', 'leading-idempotent-component',
 'leading-parent-pom', 'leading-resource-base']

control = ['service-api-gateway', 'service-registry', 'turbine-dashboard', 'spring-boot-admin', 'configuration-server']

jobs_arr = service+control


for job in jobs_arr:
	try: 
		server.build_job("DEV_" + job)
		server.build_job("TEST_" + job)
		server.build_job("PP_" + job)
	except jenkins.NotFoundException:
		print("error,"+job+" Not Found")
	else:
		continue

# del_job = server.delete_job('DEV_leading-erp-frontend')