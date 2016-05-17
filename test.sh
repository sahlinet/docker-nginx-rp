#export VHOST_1_SSL=True
export VHOST_1_SERVERNAME=a.sahli.net
export VHOST_1_SSL=True
export VHOST_1_PROXYCONF_home_proxy_pass=http://aaaa
export VHOST_1_PROXYCONF_home_location=/aaa

#export VHOST_2_SSL=True
export VHOST_2_SSL=False
export VHOST_2_SERVERNAME=b.sahli.net
export VHOST_2_PROXYCONF_home_proxy_pass=http://bbb
export VHOST_2_PROXYCONF_home_location=/bbb
export VHOST_2_PROXYCONF_static_proxy_pass=http://b2b2b2
export VHOST_2_PROXYCONF_static_location=/b2b2b2
export VHOST_2_PROXYCONF_admin_return=404
export VHOST_2_PROXYCONF_admin_location=/b2b2b2

python env2json.py | python -m json.tool
python env2json.py > env.json
j2 nginx.tmpl env.json > nginx.conf
echo "* Configuration start"
cat nginx.conf
echo "* Configuration done"