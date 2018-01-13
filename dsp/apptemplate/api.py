from dsp import db
from dsp import dsp1
import etcd
import simplejson


# @dsp1.route('/dsp/apptemplate/api/getall')
# def getall():
#     try:
#         a = db.read('/dsp/apptemplate/2048').value
#         return a
#     except etcd.EtcdKeyNotFound:
#         # do something
#         print "error"