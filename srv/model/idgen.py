last_id = 0
def new_id():
    # TODO: replace this with a global id
    # management saved somewhere in file
    # for now tho this will suffice
    global last_id
    last_id += 1
    return last_id
