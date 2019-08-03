def get_called_list():
    f = open("called", "r")
    homes = f.readlines()
    f.close()
    return homes

def was_alerted(home):
    return home['id'] in get_called_list()
     
def set_alerted(home):
    f = open("called", "a")
    f.write(str(home['id']) + "\n") 
    f.close()
