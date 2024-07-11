# -*- coding: utf-8 -*-
# Updated By: Shrrey

import sys
if sys.version_info.major == 2:
    py_version = 2
else:
    py_version = 3
from sdk import installtimenew, util
from sdk.singular import payloadsignature, getHash2
from datetime import datetime
import time, random, json, uuid
from collections import OrderedDict
false=False
true=True

#########################################################
#           Campaign Data : dictionary                  #
#                                                       #
#   Contains App's predefined strings like app versions,#
#   package name, sdk and retention information, etc    #
#########################################################
campaign_data = {
    'package_name'       : 'action.game.knife.hit.ma',
    'app_size'           :  80,
    'app_name'           : "Classic Knife Game",
    'app_version_name'   : '1.7S1',  
    'app_version_code'   : '8',
    # 'ctr'                : 6,
    'no_referrer'        : False,
    'device_targeting'   : True,
    'supported_countries': 'WW',
    'supported_os'       : '12.0',
    'tracker'            : ['singular'],
    'singular'  : {
        'user_agent'     : 'Singular/SDK-v12.0.8.PROD',
        'sdk'            : 'Singular/v12.0.8',
        'key'               : 'timesinternet',
        'secret'            : 'NmecPMtU',
    },
    'country'   :[('USA',50),('India', 3),('Malaysia', 4),('Indonesia', 1),('Thailand', 2), ('Egypt',1), ('Russia',6), ('USA',10), ('SaudiArabia',1), ('SouthAfrica',1), ('Israel',2), ('Kenya',1), ('Nigeria',1), ('Pakistan',2), ('Qatar',1), ('Brazil',3), ('Mexico',4), ('Canada',5),("UK", 30), ("HongKong",5), ("Spain", 4), ("France",4), ("Australia", 5)],
    'retention' :{
        1:85,2:82,3:80,4:78,5:75,6:72,7:70,8:68,9:65,10:60,11:55,12:50,13:45,14:40,15:35,16:33,17:30,18:28,19:26,20:20,21:19,22:18,23:17,24:16,25:15,26:14,27:13,28:12,29:11,30:10,31:9,32:8,33:7,34:6,35:5
    }
}

#########################################################
#               install() : method                      #
#               parameter : app_data,device_data        #
#                                                       #
#   Contains method calls to simulate App's behaviour   #
#   when the App was openned for first time             #
#########################################################

def install(app_data, device_data):
    ###########     INITIALIZE      ############
    # print "Please wait installing..."

    installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')
    app_data['app_lang'] = "En"

    global start_s
    start_s = str(int(app_data.get('times').get('install_complete_time')*1000))

    if not app_data.get('singular_install_id'):
        app_data['singular_install_id'] = str(uuid.uuid4())
    
    app_data['singular_time']=time.time()

    # temp = util.register_user(country=device_data.get('locale').get('country'))
    
    num = 5
    while(num > 0):
        req = firebase_install()
        response = util.execute_request(**req)
        try:
            result = json.loads(response.get('data'))
            app_data['fid'] = result.get('fid')
            break
        except:
            pass
        num -= 1
    
    if not app_data.get('fid'):
        if not app_data.get('fiddler_app_test'):
            util.firebase_error(device_data.get('locale').get('country'))
    
    call = apsalarStart(campaign_data, app_data, device_data)
    util.execute_request(**call)

    # call = apsalarResolve(campaign_data, app_data, device_data)
    # app_data['api_hit_time']=time.time()
    # util.execute_request(**call)

    # print '----------------------------- APSALAR EVENT --------------------------__LicensingStatus---'
    eve_val={"e":json.dumps({"responseCode":"0","signedData":"0|"+str(random.randint(-9999999999,9999999999))+"|"+campaign_data.get('package_name')+"|"+campaign_data.get('app_version_code')+"|ANlOHQPlAWLOtl4SSc1D3hjwTK4RRebU1Q==|"+str(int(time.time()*1000))+":VT=9223372036854775807","signature":"{}==".format(''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+') for i in range(342))),"is_revenue_event":False}, separators = (',',':'))}
    request = apsalar_event(campaign_data, app_data, device_data,event_name='__LicensingStatus',value=eve_val)
    util.execute_request(**request)
    # time.sleep(random.randint(2,5))

    num = random.randint(1,4)
    while(num > 0):
        revenue = random.choice([0.023756,0.002767,0.00322,0.002574])
        event_value = {"e": json.dumps({"ad_platform":"AdMob","ad_currency":"USD","ad_revenue":revenue,"r":revenue,"pcc":"USD","is_admon_revenue":True,"is_revenue_event":True,"ad_mediation_platform":"com.google.ads.mediation.admob.AdMobAdapter","ad_unit_id":"ca-app-pub-2908838260276046/{}".format(util.get_random_string('decimal',10))}, separators = (',',':'))}
        pack_data = apsalar_event(campaign_data, app_data, device_data, event_name = '__ADMON_USER_LEVEL_REVENUE__', value = event_value)
        util.execute_request(**pack_data)

        num -= 1

    return {'status':True}

#########################################################
#            Open      : Methods                        #
#            parameter : app_data,device_data           #
#                                                       #
#    Contains method calls to simulate App's behaviour  #
#      when the App was openned after first-open        #
#########################################################

def open(app_data, device_data,day=1):

    if app_data.get('times'):
        # installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')

        if not app_data.get('app_lang'):
            app_data['app_lang'] = "En"

        if not app_data.get('singular_install_id'):
            app_data['singular_install_id'] = str(uuid.uuid4())

        global start_s
        start_s = str(int(time.time()*1000))

        app_data['singular_time']=time.time()

        call = apsalarStart(campaign_data, app_data, device_data, isopen=True)
        util.execute_request(**call)

        num = random.randint(1,4)
        while(num > 0):
            revenue = random.choice([0.023756,0.002767,0.00322,0.002574])
            event_value = {"e": json.dumps({"ad_platform":"AdMob","ad_currency":"USD","ad_revenue":revenue,"r":revenue,"pcc":"USD","is_admon_revenue":True,"is_revenue_event":True,"ad_mediation_platform":"com.google.ads.mediation.admob.AdMobAdapter","ad_unit_id":"ca-app-pub-2908838260276046/{}".format(util.get_random_string('decimal',10))}, separators = (',',':'))}
            pack_data = apsalar_event(campaign_data, app_data, device_data, event_name = '__ADMON_USER_LEVEL_REVENUE__', value = event_value)
            util.execute_request(**pack_data)

            num -= 1

    return {'status':True}
#################################################
#                                               #
#           AppSalar Resolve funcation          #
#                                               #
#################################################

def apsalarResolve(campaign_data, app_data, device_data):
    url = 'https://sdk-api-v1.singular.net/api/v1/resolve'
    method = 'post'
    headers = {
        'User-Agent':campaign_data.get('singular').get('user_agent'),#'Singular/SDK-v9.2.5.PROD',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json',
    }

    data_dict = {
        "a":campaign_data.get('singular').get('key'),
        "c":"wifi",
        "i":campaign_data.get('package_name'),
        "k":"AIFA",
        "lag":str(generateLag()),
        "p":"Android",
        "pi":"1",
        "rt":"json",
        "u":device_data.get('adid'),
        "v":device_data.get('os_version'),
    }

    params = OrderedDict(sorted(data_dict.items()))
    for i in params.keys():
        if params.get(i) == None:
            del params[i]

    app_data['singular_time']=time.time()

    # params = params.replace(' ','+')
    h = getHash2(params,campaign_data.get('singular').get('secret'))
    params['h'] = h
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': params, 'data': json.dumps({})}


#################################################
#                                               #
#           AppSalar Start funcation            #
#                                               #
#################################################

def apsalarStart(campaign_data, app_data, device_data,call=1,isopen=False):
    url = "https://sdk-api-v1.singular.net/api/v1/start"
    method = 'post'
    headers = {
        'User-Agent': campaign_data.get('singular').get('user_agent'),#'Singular/SDK-v9.2.5.PROD', #'Singular/SDK-v9.0.4.PROD',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json'
    }
    start_s = str(int(time.time()*1000))

    data_dict = {
        "a":campaign_data.get('singular').get('key'),
        "ab":device_data.get('cpu_abi',"armeabi"),
        "aifa":device_data.get('adid'),
        # "andi": device_data.get('android_id'),
        "asid_scope":2,
        "asid_timeinterval":round(random.uniform(0,1),3),
        "av":campaign_data.get('app_version_name'),
        "br":device_data.get('brand'),
        "c":"wifi",
        "current_device_time":str(int(time.time()*1000)),
        "ddl_enabled":"false",
        # "ddl_to":"60",
        "de":device_data.get('device'),
        "device_type":"phone",
        "device_user_agent":get_ua(device_data),
        "dnt":"0",
        "event_index":"0",
        "i":campaign_data.get('package_name'),
        "install_ref": json.dumps({"installBeginTimestampServerSeconds":int(app_data.get('times').get('download_end_time'))-random.randint(2,4),"installVersion":campaign_data.get('app_version_name'),"referrer":app_data.get('referrer'),"clickTimestampSeconds":int(app_data.get('times').get('click_time')),"referrer_source":"service","current_device_time":int(time.time()),"clickTimestampServerSeconds":int(app_data.get('times').get('click_time'))-random.randint(2,4),"installBeginTimestampSeconds":int(app_data.get('times').get('download_end_time'))}),
        "install_ref_timeinterval": round(random.uniform(0,1),3),
        "install_time":str(int(app_data.get('times').get('download_end_time')*1000)),
        "is":"true",
        "k":"AIFA",
        "lag":str(generateLag()),
        "lc":device_data.get('locale').get('language'),
        "ma":device_data.get('manufacturer'),
        "mo":device_data.get('model'),
        "n":campaign_data.get('app_name'),
        "p":"Android",
        "pr":device_data.get('product'),
        "rt":"json",
        "s":str(start_s),
        "sdk":campaign_data.get('singular').get('version'),
        "singular_install_id":app_data.get('singular_install_id'),
        "src":"com.android.vending",
        "u":device_data.get('adid'),
        "update_time":str(int(app_data.get('times').get('download_end_time')*1000)),
        "v":device_data.get('os_version')
    }

    if isopen:
        data_dict['is'] = 'false'
    
    data_dict = OrderedDict(sorted(data_dict.items()))
    for i in data_dict.keys():
        if data_dict.get(i) == None:
            del data_dict[i]

    h = getHash2(data_dict,campaign_data.get('singular').get('secret'))
    data_dict['h'] = h
    return {'url': url, 'httpmethod': method, 'headers': headers, 'params': data_dict, 'data': json.dumps({})}

#################################################
#                                               #
#           AppSalar Event funcation            #
#                                               #
#################################################

def apsalar_event(campaign_data, app_data, device_data,event_name='',value='',custom_user_id=False):

    cal_seq(app_data)

    url = "https://sdk-api-v1.singular.net/api/v1/event"

    method = 'post'

    headers = {
        'User-Agent': campaign_data.get('singular').get('user_agent'),#'Singular/SDK-v9.2.5.PROD',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip'
    }

    t = str(time.time()-app_data.get('singular_time'))[:-8]

    data_dict = {
        "a":campaign_data.get('singular').get('key'),
        "aifa":device_data.get('adid'),#"ee81b619-c3ee-4c49-82ad-f70fce157d1f",
        # "andi": device_data.get('android_id'),
        "av":campaign_data.get('app_version_name'),
        "c":"wifi",
        "event_index":str(app_data.get('seq')),
        "i":campaign_data.get('package_name'),
        "k":"AIFA",
        "lag":str(generateLag()),#"0.032",
        "n":str(event_name),
        "p":"Android",
        "rt":"json",
        "s":str(start_s),
        "sdk":campaign_data.get('singular').get('sdk'),
        "seq":str(app_data.get('seq')),
        "singular_install_id":app_data.get('singular_install_id'),#"a6afffe5-d9e0-4298-b715-27a81d517794",
        "t":str(t),#"14.222",
        "u":device_data.get('adid')#"ee81b619-c3ee-4c49-82ad-f70fce157d1f",
    }

    data_dict = OrderedDict(sorted(data_dict.items()))
    for i in data_dict.keys():
        if data_dict.get(i) == None:
            del data_dict[i]

    # params = params.replace(' ','+')
    h = getHash2(data_dict,campaign_data.get('singular').get('secret'))
    data_dict['h'] = h

    q = json.dumps(value,separators=(',',':')) # Your payload dict

    jsonsignature = payloadsignature(q,campaign_data.get('singular').get('secret'))
    # print(jsonsignature)
    # print(payloadsignature(q,campaign_data.get('singular').get('secret')))
    # exit()
    data = {
        'payload':q,
        'signature': jsonsignature
    }
    return { 'url': url, 'httpmethod': method, 'headers': headers, 'params': data_dict, 'data': json.dumps(data,separators=(',',':'))}

def firebase_install():
    url = 'https://firebaseinstallations.googleapis.com/v1/projects/knifehit-b3bff/installations'
    httpmethod='post'
    headers= {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Android-Package": campaign_data.get('package_name'),
        "x-firebase-client": "H4sIAAAAAAAAAEWQzW7CMBCEXyXyGTuxXYmWVyEclniTWvgH2duICvHuLE1I5dvnmdnZvYtvhEJnBKricLwLmDCROIjRF5RDLti3plNW6eaSKfjUt1p9Kt01kFzJ3snok6zuwjLT_JkgQfglP1RGWvFb8DhEBlaZN1gDGH41Dmc_oDwXhn1bIdafNL1pgsgtKkEJhLfbNtknZiFg6dshR7ViNWNy_t8ds8Ow2ZfRqxPI58Q19Z5r2i33yh9jLlx3URO3qtdciJW8utpvSs6ckJb1rRU74YDwdUdhOvMhOy1tJ06P007MWCoP48Ma8XgC4zuLL3UBAAA",
        "X-Android-Cert": "33945DE75E939AE79D06B08EC74FE809B7DD5129",
        "x-goog-api-key": "AIzaSyDHH64DhLrr16fhSvXD6XTbQFMN6V5eXEo",
        "Accept-Encoding": "gzip",
        'User-Agent': campaign_data.get('singular').get('user_agent')
    }

    data={"fid":util.get_fid(),"appId":"1:632830746723:android:1e1fdce78dd3d6d9b19856","authVersion":"FIS_v2","sdkVersion":"a:17.1.3"}
    params={}

    return {"url": url, "httpmethod": httpmethod, "headers": headers, "params": params, "data": json.dumps(data,separators=(',',':'))}
#####################################################
#                                                   #
#           Apsalar Utility function                #
#                                                   #
#####################################################

def generateLag():
    return (random.randint(40,300)*0.001)

def custom_user_id_create(app_data):
    if not app_data.get('custom_user_id'):
        app_data['custom_user_id']= '12035'+ str(random.randint(1000,9999))
        # raise Exception('please enter custom_user_id')

def cal_seq(app_data):
    if not app_data.get('seq'):
        app_data['seq'] = 1
    else:
        app_data['seq'] = app_data.get('seq')+1
    return app_data.get('seq')

def get_country():
    weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
    country_list     = [val for val, cnt in weighted_choices for i in range(cnt)]
    return random.choice(country_list)

def get_retention(day):
    return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0

def def_sec(app_data,device_data):
    timez = device_data.get('timezone')
    sec   = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
    if int(timez) < 0:
        sec = (-1) * sec
    if not app_data.get('sec'):
        app_data['sec'] = sec

def get_ua(device_data):
    if int(device_data.get("sdk")) >=19:
        return 'Dalvik/2.1.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'
    else:
        return 'Dalvik/1.6.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'

def def_(app_data,paramName):
    if not app_data.get(paramName):
        app_data[paramName] = 0

def inc_(app_data,paramName):
    def_(app_data,paramName)
    app_data[paramName] += 1
