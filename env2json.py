import os
import re
import json


json_dict = {}

for k, v in os.environ.items():
    m = re.search("(PROXY_CONF.*)_([0-9]+)_(.*)", k)
    if m:
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

    else:
        pass

lopped_config = [v for k, v in json_dict.items()]
config = {
    'locations': lopped_config
}

for k, v in os.environ.items():
    config[k] = v


print json.dumps(config)
