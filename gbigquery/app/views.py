from django.shortcuts import render,HttpResponse
from google.cloud import bigquery
from google.oauth2 import service_account
from django.http import JsonResponse
import json


#**********************Step 4. "Pause Ad" AND "Unpause Ad"  *********************

def addSetUnset(self, client, customer_id, ad_group_id, ad_id, ad_status='PAUSED'):
    
    ad_group_ad_service = client.get_service("AdGroupAdService")

    ad_group_ad_operation = client.get_type("AdGroupAdOperation")

    ad_group_ad = ad_group_ad_operation.update
    ad_group_ad.resource_name = ad_group_ad_service.ad_group_ad_path(
        customer_id, ad_group_id, ad_id
    )
    
    if ad_status == 'ENABLED':
     ad_group_ad.status = client.enums.AdGroupStatusEnum.ENABLED
    else:
     ad_group_ad.status = client.enums.AdGroupStatusEnum.PAUSED
        
    client.copy_from(
        ad_group_ad_operation.update_mask,
        protobuf_helpers.field_mask(None, ad_group_ad._pb),
    )

    ad_group_ad_response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=customer_id, operations=[ad_group_ad_operation]
    )

    print(
        f"Paused ad group ad {ad_group_ad_response.results[0].resource_name}."
    )
    
    
#**********************Step 4. Update Ad attributes (any two)  *********************
    
def update(self,cost,acquisition):
    
	try:
		credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
		#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
		project_id = 'marketing-373208'
		client = bigquery.Client(credentials= credentials,project=project_id)
		query_job1 = client.query("UPDATE `marketing-373208.marketing.GoogleAd` SET cost="+str(cost)+", acquisition="+str(acquisition)+" WHERE id=2")
		results1 = query_job1.result() # Wait for the job to complete.
		#print(results1.total_rows)
		return JsonResponse({'arg':"Yes"})
		#return HttpResponse("Record has been updated successfully")
		#return total_revenue / total_marketing_costs
	except:
		return JsonResponse({'arg':"No"})


#**********************Step 3. Return on ad spend (ROAS) grouped  on date *********************
 
def roas(self):
    
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)
	query_job = client.query("""
	SELECT (select SUM(revenue)/SUM(marketing_costs) FROM `marketing-373208.marketing.GoogleAd` where date=date), date FROM `marketing-373208.marketing.GoogleAd` GROUP BY date """)

	results = query_job.result() # Wait for the job to complete.
	
	for data in results:
		# update Fields
		query_job1 = client.query("UPDATE `marketing-373208.marketing.GoogleAd` SET ROAS = "+str(data[0])+" WHERE date IN ('"+str(data[1])+"')")
		results1 = query_job1.result() # Wait for the job to complete.
	
	return HttpResponse("ROAS")
    #return total_revenue / total_marketing_costs

#**********************Step 3. Cost per click grouped  on date *********************

def cpc(self):
	
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)
	query_job = client.query("""
	SELECT (select SUM(cost)/SUM(clicks) FROM `marketing-373208.marketing.GoogleAd` where date=date), date FROM `marketing-373208.marketing.GoogleAd` GROUP BY date """)
	results = query_job.result() # Wait for the job to complete.
	
	for data in results:
		
		# update  Fields
		query_job1 = client.query("UPDATE `marketing-373208.marketing.GoogleAd` SET CPC = "+str(data[0])+" WHERE date IN ('"+str(data[1])+"')")
		#job_config.use_legacy_sql = True
		results1 = query_job1.result() # Wait for the job to complete.
	#return total_cost / total_clicks	
	return HttpResponse("CPC")

    
#**********************Step 3. Cost per action grouped on date *********************

def cpa(self):
    
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)
	query_job = client.query("""
	SELECT (select SUM(cost)/SUM(acquisition) FROM `marketing-373208.marketing.GoogleAd` where date=date), date FROM `marketing-373208.marketing.GoogleAd` GROUP BY date """)
	#job_config.use_legacy_sql = True
	results = query_job.result() # Wait for the job to complete.
	
	for data in results:
		
		# update CPA Fields
		query_job1 = client.query("UPDATE `marketing-373208.marketing.GoogleAd` SET CPA = "+str(data[0])+" WHERE date IN ('"+str(data[1])+"')")
		#job_config.use_legacy_sql = True
		results1 = query_job1.result() # Wait for the job to complete.
		
	return HttpResponse("CPA")
    #return total_cost / total_acquisitions
    
#**********************Step 3.6 Create a table "GoogleAds" *********************

def create_table(self):
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)
 
	table_id = bigquery.Table.from_string("marketing-373208.marketing.GoogleAd")

	schema = [
		bigquery.SchemaField("id", "INTEGER",mode="REQUIRED"),
   		bigquery.SchemaField("date", "DATETIME", mode="REQUIRED"),
		bigquery.SchemaField("channel", "STRING", mode="REQUIRED"),
		bigquery.SchemaField("cost", "INTEGER", mode="REQUIRED"),
		bigquery.SchemaField("acquisition", "INTEGER", mode="REQUIRED"),
  		bigquery.SchemaField("clicks", "INTEGER", mode="REQUIRED"),
		bigquery.SchemaField("revenue", "INTEGER", mode="REQUIRED"),
		bigquery.SchemaField("marketing_costs", "INTEGER", mode="REQUIRED"),
		bigquery.SchemaField("CPA", "FLOAT64"),
		bigquery.SchemaField("CPC", "FLOAT64"),
		bigquery.SchemaField("ROAS", "FLOAT64"),
		
	]

	table = bigquery.Table(table_id, schema=schema)
	table = client.create_table(table)
	return HttpResponse("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))


#**********************Step 3.7 Insert Dummy Data into "GoogleAds" table *********************
    
def insert_rows(self):
    
    #******************Create Connection***************************
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)
  
	table_id = bigquery.Table.from_string("marketing-373208.marketing.GoogleAd")
	for no in range(11,20):
		rows_to_insert = [
			{u"id": no, u"date": "2022-06-04 14:44:00", u"channel": "www.demo.com", u"cost": 12+no,'acquisition':13+no,'clicks':14+no,'revenue':15+no,'marketing_costs':16+no,'CPA':0,'CPC':0,'ROAS':0},
		]
		errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    
	if errors == []:
  		return HttpResponse("New rows have been added.")
	else:
		return HttpResponse("Encountered errors while inserting rows: {}".format(errors))
	
#********************** Check connection and get data *********************

def index(self):
   
    credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
    project_id = 'marketing-373208'
    client = bigquery.Client(credentials= credentials,project=project_id)
    query_job = client.query("""
	SELECT * FROM `marketing-373208.marketing.TableA` LIMIT 1000 """)
	#job_config.use_legacy_sql = True
    results = query_job.result() # Wait for the job to complete.
    #for data in results:
    # print(data)
    return HttpResponse('Testing Here')


#************************** List all dataset ********************************
def list_datasets(self):
	credentials = service_account.Credentials.from_service_account_file('marketing-373208-6ceee8361535.json')
	#credentials = service_account.Credentials.from_service_account_file('itnsgroup-4dc81c5ef1a4.json')
	project_id = 'marketing-373208'
	client = bigquery.Client(credentials= credentials,project=project_id)

	datasets = list(client.list_datasets())  # Make an API request.
	project = client.project

	if datasets:
		print("Datasets in project {}:".format(project))
		for dataset in datasets:
			print("\t{}".format(dataset.dataset_id))
	else:
		return HttpResponse("{} project does not contain any datasets.".format(project))
