import dsp
import etcd
import json



def login(data):
    username = data.get('username')
    password = data.get('password')
    dbkey = "/dsp/auth/"+ username
    try :
        realpass = dsp.db.get(dbkey).value
    except etcd.EtcdKeyError:
        return "false"
    if (realpass == password):
        return "true"
    return "false"

def changepass(data):
    username = data.get('username')
    newpass = data.get('newpass')

    dbkey = "/dsp/auth/" + username
    try :
        dsp.db.set(dbkey, newpass)
    except etcd.EtcdKeyError:
        return "false"
    return "true"

