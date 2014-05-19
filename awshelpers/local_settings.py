"""
Move to settings.py
Structured settings to create hosted zones easily

@ - variable that means the domain itself

- Example:
"""

type_name_1 = {
    "records_a":{
        "@":["destination_resource_hostedzone_id", "destination_resource_value"],
        "subdomain_1":["10.0.0.1"],
        "subdomain_2":["destination_resource_hostedzone_id", "destination_resource_value"]
    },
    "records_cname":{
        "subdomain_3":"destination_resource_value",
        "www":"@"
    },
    "records_mx":{
        "@":['10 xxxxx.sample.com.',
            '20 xxxxx.sample.com.',
            '30 xxxxx.sample.com.',
            '40 xxxxx.sample.com.',
            '50 xxxxx.sample.com.']
    }
}

type_name_2 = {
    "records_a":{
        "@":["8.8.8.8"],
        "subdomain_1":["10.1.1.1"],
        "subdomain_2":["destination_resource_hostedzone_id", "destination_resource_value"]
    },
    "records_cname":{
        "subdomain_3":"destination_resource_value",
        "www":"@"
    }
}

