
def read_config(file_name):

    config = {}
    
    with open(file_name) as file:
        for line in file:
            line = line.split('#')[0]
            if line not in ('','\n'):
                line = line.split()
                param = line[0]
                if param not in config:
                    config[param] = {}
                desc = line[1]
                config[param][desc] = line[2:]

    return config