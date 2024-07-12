#-*- coding: utf-8 -*-
# created by him@nshu
import sys,base64
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime,timedelta
from sdk import installtimenew, util, NameLists
import clicker, Config
from sdk import NameLists
from hashlib import sha1
import time, random, json, string, urllib, uuid, hashlib
from spicipher import af_cipher
from requests import Request
from collections import OrderedDict
false = False
true = True
null = None


campaign_data = {
   'package_name' : 'ae.ahb.digital',
   'app_name' : 'Al Hilal Digital',
   'app_version_name' : '1.7.0(3.4.0-20174)', #1.3.7%283.0.7-13352%29 #1.4.9(3.1.9-15289) #1.5.1(3.2.1-15689) #1.6.9(3.3.9-19976)
   'app_version_code' : '20174', #8000270 #15289 #15689 #17715
   'tracker' : ['adjust'],
   'supported_os' : '8',
   'supported_countries' : 'WW',
#    'link' : 'http://track.crossway.rocks/click?offer_id=62cc2d758dca71693d697f90&aff_id=5&adv_id=5ee4b9d4c6e0c7051126c421&aff_sub1={aff_click_id}&aff_sub2={gaid}&aff_sub3={idfa}&aff_sub6={app_name}&source=j1233',
   'app_size' : 64,
   'adjust' : {'sdk': 'android4.28.5', 'app_token': 'vh15nt7wmu4g'},
   'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
   'retention' : {1: 85, 2: 82, 3: 78, 4: 75, 5: 70, 6: 66, 7: 62, 8: 58, 9: 55, 10: 50, 11: 48, 12: 45, 13: 40, 14: 39, 15: 38, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
	}
adjust_data = {"url": "app.adjust.com", "sdkclient": "android4.28.5", "Content": "application/x-www-form-urlencoded", "initiated_by": "backend"}

session_data = {"gps_adid_attempt": "1", "country": "US", "api_level": "28", "event_buffering_enabled": "1", "hardware_name": "ONEPLUS+A3003_16_191104", "app_version": "1.3.7%283.0.7-13352%29", "app_token": "vh15nt7wmu4g", "installed_at": "2022-10-10T15%3A54%3A19.182Z%2B0530", "created_at": "2022-10-10T15%3A59%3A33.056Z%2B0530", "device_type": "phone", "language": "en", "gps_adid": "19ac7eff-d8c3-4359-a324-311f55f9d6fe", "connectivity_type": "1", "device_manufacturer": "OnePlus", "display_width": "1080", "device_name": "ONEPLUS+A3003", "needs_response_details": "1", "os_build": "PKQ1.181203.001", "updated_at": "2022-10-10T15%3A54%3A19.182Z%2B0530", "cpu_type": "arm64-v8a", "screen_size": "normal", "screen_format": "long", "gps_adid_src": "service", "os_version": "9", "android_uuid": "1becece3-baaa-4540-9933-8db8e56ee069", "environment": "production", "screen_density": "high", "attribution_deeplink": "1", "session_count": "1", "display_height": "1920", "package_name": "ae.ahb.digital", "os_name": "android", "network_type": "0", "ui_mode": "1", "tracking_enabled": "1", "sent_at": "2022-10-10T15%3A59%3A33.161Z%2B0530"}

sdk_click_data = {"gps_adid_attempt": "1", "country": "US", "api_level": "28", "event_buffering_enabled": "1", "hardware_name": "ONEPLUS+A3003_16_191104", "app_version": "1.3.7%283.0.7-13352%29", "app_token": "vh15nt7wmu4g", "installed_at": "2022-10-10T15%3A54%3A19.182Z%2B0530", "session_length": "0", "created_at": "2022-10-10T15%3A59%3A33.175Z%2B0530", "device_type": "phone", "language": "en", "gps_adid": "19ac7eff-d8c3-4359-a324-311f55f9d6fe", "referrer_api": "google", "source": "install_referrer", "connectivity_type": "1", "device_manufacturer": "OnePlus", "display_width": "1080", "time_spent": "0", "device_name": "ONEPLUS+A3003", "needs_response_details": "1", "os_build": "PKQ1.181203.001", "updated_at": "2022-10-10T15%3A54%3A19.182Z%2B0530", "click_time": "2022-10-10T15%3A52%3A49.000Z%2B0530", "cpu_type": "arm64-v8a", "install_version": "1.3.7%283.0.7-13352%29", "screen_size": "normal", "screen_format": "long", "gps_adid_src": "service", "subsession_count": "1", "click_time_server": "2022-10-10T15%3A52%3A49.000Z%2B0530", "os_version": "9", "google_play_instant": "0", "install_begin_time_server": "2022-10-10T15%3A52%3A53.000Z%2B0530", "android_uuid": "1becece3-baaa-4540-9933-8db8e56ee069", "referrer": "adjust_reftag%3DcwsunZ0e6C7Dn%26utm_source%3DArabyadds-2022%25285%2529%26utm_campaign%3DJUL_2022%26utm_content%3D324_5.MTES94527", "environment": "production", "screen_density": "high", "attribution_deeplink": "1", "install_begin_time": "2022-10-10T15%3A52%3A54.000Z%2B0530", "session_count": "1", "display_height": "1920", "package_name": "ae.ahb.digital", "os_name": "android", "network_type": "0", "ui_mode": "1", "tracking_enabled": "1", "sent_at": "2022-10-10T15%3A59%3A33.213Z%2B0530"}

atribution_data = {"initiated_by": "backend", "gps_adid_attempt": "1", "api_level": "28", "event_buffering_enabled": "1", "app_version": "1.3.7(3.0.7-13352)", "app_token": "vh15nt7wmu4g", "os_version": "9", "created_at": "2022-10-10T15%3A59%3A48.541Z%2B0530", "device_type": "phone", "gps_adid": "19ac7eff-d8c3-4359-a324-311f55f9d6fe", "android_uuid": "1becece3-baaa-4540-9933-8db8e56ee069", "device_name": "ONEPLUS%20A3003", "environment": "production", "needs_response_details": "1", "attribution_deeplink": "1", "package_name": "ae.ahb.digital", "os_name": "android", "ui_mode": "1", "gps_adid_src": "service", "tracking_enabled": "1", "sent_at": "2022-10-10T15%3A59%3A48.599Z%2B0530"}

event_data = []

events_details = []




def install(app_data, device_data):
    # print "Please wait installing..."
    installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')

    if not app_data.get('sec'):
        timez=device_data.get('timezone')    
        sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
        if int(timez) < 0:
            sec = (-1) * sec
        app_data['sec'] = sec
    # user = util.register_user(country=device_data.get('locale').get('country'))
    # req = locationData.getLocation(device_data.get('locale').get('country'))

    if not app_data.get('android_uuid'):
        app_data['android_uuid']=str(uuid.uuid4())


    app_data['fid']=random.choice(['c','d','e','f'])+''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(21))

    req = firebase_installations(app_data,device_data)
    res= util.execute_request(**req)


    # print 'Session'
    req = adjust_session(app_data, device_data)
    util.execute_request(**req)


    # print 'Sdk_click'
    req = adjust_sdk_click( app_data, device_data)
    util.execute_request(**req)
    time.sleep(random.randint(1,5))



    if adjust_data.get('sdk_info'):
        req = adjust_sdk_info(app_data,device_data)
        util.execute_request(**req)



    # print 'Attribution'
    req = adjust_attribution(app_data, device_data)
    util.execute_request(**req)








    #  For update in events pls write from her....................................................

    # req = adjust_events(app_data,device_data,event_token='',)
    # util.execute_request(**req)
    # time.sleep(random.randint(1,5))




    return {'status':True}  
#============================================================================================================================
def open(app_data, device_data, day =1):
	

	if app_data.get('times'):
		# print 'Session'
		req = adjust_session(app_data, device_data)
		util.execute_request(**req)


	return {'status':True}

#==================================================================================================================================================================================
def firebase_installations( app_data, device_data ):
	method = "post"
	url ='https://firebaseinstallations.googleapis.com/v1/projects/ahb-digital-bank/installations'

	headers = {
    'Content-Type':"application/json",
    'Accept':"application/json",
    'Cache-Control':"no-cache",
    'X-Android-Package':"ae.ahb.digital",
    'x-firebase-client-log-type':"3",
    'X-Android-Cert':"4CDA6B1B03C63ED570D9EAA119F7D1F4780E39E8",
    'x-goog-api-key':"AIzaSyAXwkwFmlZCdtKBnHSnNnOImxQJxf6K3_U",
    'Connection':"Keep-Alive",
    'Accept-Encoding':"gzip",
    'x-firebase-client':"fire-cls/18.2.6 fire-core-ktx/20.0.0 fire-core/20.0.0 fire-dl-ktx/19.1.1 fire-android/28 fire-perf-ktx/19.1.1 fire-perf/19.1.1 fire-fcm-ktx/21.0.1 device-brand/xiaomi android-platform/ fire-abt/20.0.0 fire-cfg-ktx/20.0.4 device-name/violet device-model/violet android-target-sdk/31 fire-cls-ktx/18.2.6 fire-rc/20.0.4 kotlin/1.6.10 android-min-sdk/24 fire-iid/21.0.1 android-installer/com.android.vending fire-installations/17.0.0 fire-fcm/20.1.7_1p fire-analytics/18.0.2 fire-analytics-ktx/18.0.2",
    'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build'))

	}

	data ={
		"fid": app_data.get('fid'),
        "appId": "1:154465065455:android:9af150763f095516c03e1a",
        "authVersion": "FIS_v2",
        "sdkVersion": "a:17.0.0"
	}
	
	return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}

def adjust_session( app_data, device_data):

	url='https://'+adjust_data.get('url')+'/session'
	
	httpmethod='post'

	app_data['session_started']=int(time.time())

	if not app_data.get('session_count'):
		app_data['session_count'] = 1
	else:
		app_data['session_count'] +=1
	
	headers={
			'Client-SDK':campaign_data.get('adjust').get('sdk'),
			'Content-Type':'application/x-www-form-urlencoded',
			'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
			'Accept-Encoding':'gzip'
	}

	params={}

	data={
		'android_uuid':app_data.get('android_uuid'),
		'api_level':device_data.get('sdk'),
		'app_token':campaign_data.get('adjust').get('app_token'),
		'app_version':campaign_data.get('app_version_name'),
		'attribution_deeplink':1,
		'connectivity_type':1,
		'country':device_data.get('locale').get('country'),
		'cpu_type':device_data.get('cpu'),
		'created_at':(datetime.utcfromtimestamp(time.time()-random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'device_manufacturer':device_data.get('manufacturer'),
		'device_name':device_data.get('model'),
		'device_type':device_data.get('device_type'),
		'display_height':device_data.get('resolution').split('x')[-2],
		'display_width':device_data.get('resolution').split('x')[-1],
		'environment':'production',
		'event_buffering_enabled':0,
		# 'fb_id':app_data.get('fb_id'),
		'gps_adid':device_data.get('adid'),
		'gps_adid_src':'service',
		"gps_adid_attempt": 1,
		'hardware_name':device_data.get('hardware'),
		'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'language':device_data.get('locale').get('language'),
		'needs_response_details':1,
		'network_type':0,
		'os_build':device_data.get('build'),
		'os_name':'android',
		'os_version':device_data.get('os_version'),
		'package_name':campaign_data.get('package_name'),
		'screen_density':get_screen_density(device_data),
		'screen_format':get_screen_format(device_data),
		'screen_size':'normal',
		'sent_at':(datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'session_count':app_data.get('session_count'),
		'tracking_enabled':1,
		'updated_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		# "vm_isa":device_data.get('cpu')[:-4]
	}

	if session_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if session_data.get('app_secret'):
		data['app_secret'] = session_data.get('app_secret')
	
	if session_data.get('ui_mode'):
		data['ui_mode'] = 1
	if session_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')



	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')
	app_data['subsession']=1
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'session')

	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#====================================================================================

def adjust_sdk_click(app_data,device_data):

	url='https://'+adjust_data.get('url')+'/sdk_click'
	httpmethod='post'
	app_data['session_started']=int(time.time())
	headers={
			'Client-SDK': campaign_data.get('adjust').get('sdk'),
			'Content-Type':'application/x-www-form-urlencoded',
			'User-Agent': 'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
		'Accept-Encoding':'gzip',

	}

	params={}

	
	data={
			'android_uuid':app_data.get('android_uuid'),
			'api_level':device_data.get('sdk'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'app_version':campaign_data.get('app_version_name'),
			'attribution_deeplink':1,
			'connectivity_type':1,
			# 'click_time':        datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
			# "click_time_server": datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
			'country':device_data.get('locale').get('country'),
			'cpu_type':device_data.get('cpu'),
			'created_at':(datetime.utcfromtimestamp(time.time()-random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'device_manufacturer':device_data.get('manufacturer'),
			'device_name':device_data.get('model'),
			'device_type':device_data.get('device_type'),
			'display_height':device_data.get('resolution').split('x')[-2],
			'display_width':device_data.get('resolution').split('x')[-1],
			'environment':'production',
			'event_buffering_enabled':0,
			'google_play_instant':0,
			'gps_adid_attempt':1,
			# 'fb_id':app_data.get('fb_id'),
			'gps_adid':device_data.get('adid'),
			'gps_adid_src':'service',
			'hardware_name':device_data.get('hardware'),
			'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			# "install_begin_time":datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
			# "install_begin_time_server":	datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
			# 'install_version':campaign_data.get('app_version_name'),
			'language':device_data.get('locale').get('language'),
			'needs_response_details':1,
			'network_type':0,
			'os_build':device_data.get('build'),
			'os_name':'android',
			'os_version':device_data.get('os_version'),
			'package_name':campaign_data.get('package_name'),
			'referrer':app_data.get('referrer') or 'adjust_reftag=cLSIUNmcJLB72&utm_source=OMD_Inmotion-IV_AHB_AlwaysOnMay23_Set1&utm_campaign=unknown&utm_content=mobketing',
			# 'referrer_api':'google',
			'screen_density':get_screen_density(device_data),
			'screen_format':get_screen_format(device_data),
			'screen_size':'normal',
			'sent_at':(datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'session_count':app_data.get('session_count'),
			'session_length':int(time.time())- app_data.get('session_started'),
			'source':'install_referrer',
			'subsession_count':subsession(app_data),
			'time_spent':time_spent(app_data),
			'tracking_enabled':1,
			'updated_at': datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone') or None,
			# "vm_isa":device_data.get('cpu')[:-4]
	}

	if sdk_click_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if sdk_click_data.get('app_secret'):
		data['app_secret'] = sdk_click_data.get('app_secret')
	
	if sdk_click_data.get('ui_mode'):
		data['ui_mode'] = 1
	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')



	if sdk_click_data.get('click_time'):
		data['click_time'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

	if sdk_click_data.get('click_time_server'):
		data['click_time_server'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

	if sdk_click_data.get('install_begin_time'):
		data['install_begin_time'] = datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone')
	if sdk_click_data.get('install_begin_time_server'):
		data['install_begin_time_server'] =datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),

			
	if sdk_click_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')

	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')

	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')

	if sdk_click_data.get('referrer_api'):
		data['referrer_api'] = sdk_click_data.get('referrer_api')

	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_click')

	# data['click_time_server'] = datetime.utcfromtimestamp(int(app_data.get('times').get('click_time')) +  timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
	# data['install_begin_time_server'] = datetime.utcfromtimestamp((app_data.get('times').get('download_begin_time')+app_data.get('sec')) + timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#==================================================================================

def adjust_attribution(app_data,device_data,initiated_by=None):

	url='https://'+adjust_data.get('url')+'/attribution'

	httpmethod='get'

	headers={
		'Client-SDK':campaign_data.get('adjust').get('sdk'),
		'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
		'Accept-Encoding':'gzip',
	}

	params={
			'android_uuid':app_data.get('android_uuid'),
			'api_level':device_data.get('sdk'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'app_version':campaign_data.get('app_version_name'),
			# 'app_secret':campaign_data.get('adjust').get('app_secret'),
			'attribution_deeplink':1,
			'created_at':(datetime.utcfromtimestamp(time.time()-random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'device_name':device_data.get('model'),
			'device_type':device_data.get('device_type'),
			'environment':'production',
			'event_buffering_enabled':0,
			'gps_adid':device_data.get('adid'),
			'gps_adid_src':'service',     
			'gps_adid_attempt':1,
			# 'fb_id':app_data.get('fb_id'),
			'initiated_by':initiated_by,
			'needs_response_details':1,
			'os_name':'android',
			'os_version':device_data.get('os_version'),
			'package_name':campaign_data.get('package_name'),
			'tracking_enabled':1,
			# 'secret_id':'2',
			'sent_at':(datetime.utcfromtimestamp(time.time()+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			# 'session_count':app_data.get('session_count'),
	}

	if atribution_data.get('app_secret'):
		params['app_secret'] = atribution_data.get('app_secret')
	if atribution_data.get('secret_id'):
		params['secret_id'] = atribution_data.get('secret_id')
	if atribution_data.get('initiated_by'):
		params['initiated_by'] = atribution_data.get('initiated_by')
	if atribution_data.get('ui_mode'):
		params['ui_mode'] = 1
	if app_data.get('pushtoken'):
		params['push_token'] = app_data.get('pushtoken')



	data=None
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(params.get('created_at'),params.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'attribution')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#====================================================================================
def adjust_sdk_info(app_data,device_data):

	url='https://'+adjust_data.get('url')+'/sdk_info'

	httpmethod='post'
	pushtoken(app_data)
	headers={
		'Client-SDK':campaign_data.get('adjust').get('sdk'),
		'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
		'Accept-Encoding':'gzip',
	}

	data={
			# 'android_uuid':app_data.get('android_uuid'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'attribution_deeplink':1,
			'created_at':(datetime.utcfromtimestamp(time.time()-random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'environment':'production',
			'event_buffering_enabled':0,
			'gps_adid':device_data.get('adid'),
			# 'gps_adid_src':'service',  
			# 'gps_xadid_attempt':1,
			'needs_response_details':1,
			"push_token":app_data.get('pushtoken'),
			"source":"push",
			'tracking_enabled':1,
			'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
	}
	if adjust_data.get('sdk_info'):
		if sdk_info_data.get('android_uuid'):
			data['android_uuid'] = app_data.get('android_uuid')
		if sdk_info_data.get('gps_adid_attempt'):
			data['gps_adid_attempt'] = sdk_info_data.get('gps_adid_attempt')
		if sdk_info_data.get('gps_xadid_attempt'):
			data['gps_xadid_attempt'] = sdk_info_data.get('gps_xadid_attempt')





	params=None
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'sdk_info')
	
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}





#========================================================================================================================================================================


def adjust_events(app_data,device_data,event_token=None,callback = None,patner= None):

	url='https://'+adjust_data.get('url')+'/event'

	httpmethod='post'

	headers={
			'Client-SDK':campaign_data.get('adjust').get('sdk'),
			'User-Agent':'Dalvik/{0} (Linux; U; Android {1}; {2} Build/{3})'.format('2.1.0', device_data.get('os_version'), device_data.get('model'), device_data.get('build')),
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept-Encoding':'gzip',    
	}

	params=None

	
	if not app_data.get('event_count'):
		app_data['event_count']=1
	else:
		app_data['event_count']=app_data['event_count']+1

	# print(app_data)

	data={
		'android_uuid':app_data.get('android_uuid'),
		'api_level':device_data.get('sdk'),
		'app_token':campaign_data.get('adjust').get('app_token'),
		'app_version':campaign_data.get('app_version_name'),
		'attribution_deeplink':1,
		'connectivity_type':1,
		'country':device_data.get('locale').get('country'),
		'cpu_type':device_data.get('cpu'),
		# 'callback_params':json.dumps(callback),
		'created_at':(datetime.utcfromtimestamp(time.time()-random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'device_manufacturer':device_data.get('manufacturer'),
		'device_name':device_data.get('model'),
		'device_type':device_data.get('device_type'),
		'display_height':device_data.get('resolution').split('x')[-2],
		'display_width':device_data.get('resolution').split('x')[-1],
		'environment':'production',
		'event_buffering_enabled':0,
		'event_count':app_data.get('event_count'),
		'event_token':event_token,
		'gps_adid':device_data.get('adid'),
		'gps_adid_attempt':'1',
		'gps_adid_src':'service',
		# 'fb_id':app_data.get('fb_id'),
		'hardware_name':device_data.get('hardware'),
		'language':device_data.get('locale').get('language'),
		'needs_response_details':1,
		'network_type':0,
		'os_build':device_data.get('build'),
		'os_name':'android',
		'os_version':device_data.get('os_version'),
		'package_name':campaign_data.get('package_name'),
		'partner_params' : patner,
		# 'push_token' : push_token,
		# "partner_params":partner_params,
		'screen_density':get_screen_density(device_data),
		'screen_format':get_screen_format(device_data),
		'session_count':app_data.get('session_count'),
		'session_length':int(time.time())-app_data.get('session_started'),
		'screen_size':'normal',
		'subsession_count':subsession(app_data),
		'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'time_spent':time_spent(app_data),
		'tracking_enabled':1,
		#  "vm_isa":device_data.get('cpu')[:-4]

	}


	if event_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if event_data.get('app_secret'):
		data['app_secret'] = event_data.get('app_secret')
	
	if event_data.get('ui_mode'):
		data['ui_mode'] = 1
	if event_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')


	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')

	if callback:
		data['callback_params'] = json.dumps(callback)
	if patner:
		data['partner_params'] = json.dumps(patner)

	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'event')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#============================================================================================

def get_auth(created_at,activity_kind, app_secret,gps_adid , source =''):
	string = created_at+activity_kind+source+app_secret+gps_adid
	sign = hashlib.sha256(string).hexdigest()
	if source:
		return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid source app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)
	return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)



def time_spent(app_data):
	if not app_data.get('time_spent'):
		app_data['time_spent'] = str(0)
	else:
		app_data['time_spent'] = int(app_data.get('time_spent')) + (int(time.time()) - app_data.get('session_started'))

	return app_data.get('time_spent')

def subsession(app_data):
	possibility = [True]*30+[False]*70
	random.shuffle(possibility)
	if random.choice(possibility):
		if not app_data.get('subsession'):
			app_data['subsession']=1
		else:
			app_data['subsession']+=1
	return app_data.get('subsession')

def get_screen_density(device_data):
	dpi = int(device_data.get('dpi'))
	if dpi >= 320:
		return 'high'
	elif dpi >= 180:
		return 'medium'
	else:
		return 'low'
		
def get_screen_format(device_data):
	resolution = device_data.get('resolution')
	b = resolution.split('x')
	c = float(b[1])/float(b[0])
	if c >= 1.77:
		return 'long'
	else:
		return 'normal'

def pushtoken(app_data):
	if not app_data.get('pushtoken'):
		app_data['pushtoken']=util.get_random_string('hex',64)


def get_country():
	weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
	country_list = [val for val, cnt in weighted_choices for i in range(cnt)]
	return random.choice(country_list)

def get_retention(day):
	return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0

def click(device_data=None, camp_type='market', camp_plat = 'android'):

	package_name = campaign_data.get('package_name')
	serial        = device_data.get('serial')
	agent_id      = Config.AGENTID
	random_number = random.randint(1,10)
	source_id     = ""
	if random_number < 5:
		source_id = "728"
	elif random_number < 8:
		source_id = "517"
	elif random_number < 9:
		source_id = "604"
	else:
		source_id = "386"
	st = device_data.get("device_id", str(int(time.time()*1000)))
	link = campaign_data['link']
	link = link.format(dp2=st,agent=agent_id,source=source_id,device_serial=serial,gaid=device_data.get('adid'))
	return clicker.click(link, device_data, camp_type, camp_plat, 'url=', package_name)









#######################################################################################



	