def greedy(items:list, max_cost:"Numeric", KEY_FUNCTION:"function") -> tuple:
    """
    Assumes max_cost >= 0
    KEY_FUNCTION maps elements of items to numbers
    """
    items_copy = sorted(items, key =  KEY_FUNCTION, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0

    for i in range(len(items_copy)):
        if(total_cost + items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()

    return (result, total_value) 