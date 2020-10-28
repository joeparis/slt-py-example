import yaml

handle = None
try:
    handle = open("nick.yml", "r")
    data = yaml.safe_load(handle)
    print(data)
except yaml.YAMLError as error:
    print(error)
finally:
    if handle:
        handle.close()
