import json
import requests

def getall():
    allimages = []
    res = requests.get('http://0.0.0.0:5000/v2/_catalog')
    for iname in (json.loads(res.text).get('repositories')):
        tags = json.loads(requests.get('http://0.0.0.0:5000/v2/'+iname+'/tags/list').text).get('tags')
        try:
            for tag in tags:
                allimages.append(iname+':'+tag)
        except TypeError:
            print 'null'
    return json.dumps(allimages)

def delete():
    # name = data.get('imagename')
    # tag = data.get('tag')
    headers = {'accept':'application/vnd.docker.distribution.manifest.v2+json'}
    res1 = requests.get('http://0.0.0.0:5000/v2/owen/etcd/manifests/dao',headers = headers)
    digest = res1.headers.get('docker-content-digest')
    try:
        res2 = requests.delete('http://0.0.0.0:5000/v2/owen/etcd/manifests/'+digest)
    except TypeError:
        return 'false'
    return 'true'
