import dsp
import etcd
import json

def getall():
    allapptemplate = []
    try:
        directory = dsp.db.get('/dsp/apptemplate')
        for result in directory.children:
            allapptemplate.append (result.key[17:])
        print json.dumps(allapptemplate)
        return json.dumps(allapptemplate)

    except etcd.EtcdValueError:
        return "value error"
    except etcd.EtcdKeyError:
        return "key error"

def get(data):
    name = data.get("name")
    dbkey = '/dsp/apptemplate/' + name
    try:
        tem = dsp.db.read(dbkey).value
        return tem
    except etcd.EtcdKeyError:
        return "key error"

def add(data):
    name = data.get("name")
    dbkey = '/dsp/apptemplate/' + name
    try:
        dsp.db.set(dbkey,data)
    except etcd.EtcdKeyError:
        return "key error"
    except etcd.EtcdValueError:
        return "value error"
    return "true"

def set(data):
    name = data.get("name")
    dbkey = '/dsp/apptemplate/' + name
    try:
        dsp.db.set(dbkey, data)
    except etcd.EtcdKeyError:
        return "key error"
    except etcd.EtcdValueError:
        return "value error"
    return "true"

def delete(data):
    name = data.get("name")
    dbkey = '/dsp/apptemplate/' + name
    try:
        dsp.db.delete(dbkey)
    except etcd.EtcdKeyError:
        return "key error"
    except etcd.EtcdValueError:
        return "value error"
    return "true"
