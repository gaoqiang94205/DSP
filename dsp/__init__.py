from flask import Flask
from flask import request
from dsp.apptemplate import template
from dsp.auth import auth
from dsp.image import image
import etcd


dsp1 = Flask(__name__)

#ETCD
db = etcd.client.Client(
             host='0.0.0.0',
             port=2379,
             )


@dsp1.route('/')
def showname():
    return "DSP"


@dsp1.route('/index')
def index():
    return "index"


@dsp1.route('/dsp/auth/login',methods=['POST'])
def authlogin():
    print "login"
    print request.json
    return auth.login(request.json)


@dsp1.route('/dsp/auth/changepass',methods=['POST'])
def authchangepass():
    print "changepass"
    print request.json
    return auth.changepass(request.json)


@dsp1.route('/dsp/apptemplate/getall')
def templategetall():
    return  template.getall()


@dsp1.route('/dsp/apptemplate/get',methods=['POST'])
def templateget():
    return template.get(request.json)


@dsp1.route('/dsp/apptemplate/add',methods=['POST'])
def templateadd():
    return template.add(request.json)


@dsp1.route('/dsp/apptemplate/set',methods=['POST'])
def templateset():
    return template.set(request.json)


@dsp1.route('/dsp/apptemplate/delete',methods=['POST'])
def templatedelete():
    return template.delete(request.json)

@dsp1.route('/dsp/image/getall')
def imagegetall():
    return image.getall()

@dsp1.route('/dsp/image/delete')
def imagedelete():
    return image.delete()



