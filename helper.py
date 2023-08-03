import json

def dumper(arg):
    def json_default(arg):
        return f"{arg.__class__}"
        # if isinstance(arg, datetime.datetime) or isinstance(arg, Enum):
        #     return "{}".format(arg)
        raise TypeError(arg)

    # return json.dumps(data, sort_keys=True, default=json_default, indent=2)
    print(json.dumps(arg, sort_keys=True, default=json_default, indent=2))