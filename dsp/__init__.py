from flask import Flask
from dsp.apptemplate import api
import etcd


dsp1 = Flask(__name__)

#ETCD
db = etcd.Client(
             host='0.0.0.0',
             port=2379,
             )


@dsp1.route('/')
def showname():
    return "DSP"


@dsp1.route('/index')
def index():
    return "index"


@dsp1.route('/dsp/apptemplate/api/getall')
def getall():
    try:
        a = db.read('/dsp/apptemplate/2048').value
        return a
    except etcd.EtcdKeyNotFound:
        # do something
        print "error"

@dsp1.route('/dsp/apptemplate/api/get')
def get():
    return "aaa"