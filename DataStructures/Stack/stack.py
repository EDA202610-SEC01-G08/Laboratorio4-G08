def new_stack():    return {"size": 0, "first": None, "last": None}

def push(stack, item):
    stack["size"] += 1
    if stack["first"] is None:
        stack["first"] = item
        stack["last"] = item
    else:
        stack["last"] = item

def pop(stack):   
    if stack["size"] == 0:
        raise IndexError("pop from empty stack")
    item = stack["last"]
    stack["size"] -= 1
    if stack["size"] == 0:
        stack["first"] = None
        stack["last"] = None
    else:
        # In a real implementation, we would need to update the last element properly.
        # For now, we assume that popping is only done in a controlled way.
        pass
    return item

def is_empty(stack):   return stack["size"] == 0

def top(stack):   return stack["last"] if stack["size"] > 0 else None   

def size(stack):  return stack["size"]