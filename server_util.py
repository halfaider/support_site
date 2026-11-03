import urllib.parse

import requests

from .setup import *

SERVER_PLUGIN_DDNS = 'https://meta.sjva.me'
WEB_DIRECT_URL = 'http://52.78.103.230:49734'
try:
    if F.SystemModelSetting.get('ddns') == SERVER_PLUGIN_DDNS:
        SERVER_PLUGIN_DDNS = 'http://127.0.0.1:19999'
except:
    pass

class MetadataServerUtil(object):
    @classmethod
    def get_metadata(cls, code):
        try:
            url = f"{WEB_DIRECT_URL}/meta/get_meta.php?"
            url += urllib.parse.urlencode({'type':'meta', 'code':code})
            logger.warning(url)
            data = requests.get(url).json()
            if data['ret'] == 'success':
                return data['data']
        except Exception as exception:
            logger.error('metaserver connection fail.. get_metadata')


    @classmethod
    def set_metadata(cls, code, data, keyword):
        try:
            url = f'{SERVER_PLUGIN_DDNS}/server/normal/metadata/set'
            upload_id = F.PluginManager.get_plugin_instance('sjva').ModelSetting.get('sjva_id')
            param = {'code':code, 'data':json.dumps(data), 'user':upload_id, 'keyword':keyword}
            data = requests.post(url, data=param).json()
            if data['ret'] == 'success':
                logger.info('%s Data save success. Thanks!!!!', code)
        except Exception as exception:
            logger.error('metaserver connection fail.. set_metadata')


    @classmethod
    def get_meta_extra(cls, code):
        try:
            url = f"{WEB_DIRECT_URL}/meta/get_meta.php?"
            url += urllib.parse.urlencode({'type':'extra', 'code':code})
            data = requests.get(url).json()
            if data['ret'] == 'success':
                return data['data']
        except Exception as exception:
            logger.error('metaserver connection fail.. get_meta_extra')
