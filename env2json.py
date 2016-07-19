import os
import re
import json
import pprint


json_dict = {}

for k, v in os.environ.items():
    m_single = re.search("^(PROXYCONF.*)_([0-9]+)_(.*)$", k)
    m_multi = re.search("^VHOST_([0-9]+)_([A-Z]+)_([a-zA-Z0-9]+)_(.*)$", k)
    m_multisingle = re.search("^VHOST_([0-9]+)_([A-Z0-9]+)$", k)
    if m_single:
        m = m_single
        key = m.group(1)
        num = m.group(2)
        subkey = m.group(3)

        if num in json_dict:
                json_dict[num].update({
                    subkey: v
                })
        else:
            json_dict[num] = {
                subkey: v
            }
    elif m_multisingle:
        m = m_multisingle
        vhost_num = m.group(1)
        conf = m.group(2)
        if vhost_num in json_dict:
            json_dict[vhost_num][conf] = v
        else:
            json_dict[vhost_num] = {conf: v}
    elif m_multi:
        m = m_multi
        vhost_num = m.group(1)
        conf = m.group(2)
        location_num = m.group(3)
        location_key = m.group(4)

        if vhost_num in json_dict:
            if conf in json_dict[vhost_num]:
                if location_num in json_dict[vhost_num][conf]:
                    json_dict[vhost_num][conf][location_num].update({location_key: v})
                else:
                    json_dict[vhost_num][conf][location_num] = {location_key: v}
            else:
                json_dict[vhost_num][conf] = {location_num: {location_key: v}}
        else:
            json_dict[vhost_num] = {conf: {location_num: {location_key: v}}}

    else:
        pass

#print "***********"
#pprint.pprint(json_dict)
#print "***********"
looped_config = [v for k, v in json_dict.items()]
config = {
    'vhosts': looped_config
}

for k, v in os.environ.items():
#    if "SERVER" in k or "PROXY" in k:
        config[k] = v


print json.dumps(config, indent=4)
