def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(input_list, element):
    input_list.append(element)
    return input_list

def add_element_to_start_of_list(input_list, element):
    input_list.insert(0, element)
    return input_list

def remove_element_from_end_of_list(input_list):
    if input_list:
        input_list.pop()
    return input_list

def remove_element_from_start_of_list(input_list):
    if input_list:
        input_list.pop(0)
    return input_list

def retrieve_first_element_from_list(input_list):
    if input_list:
        return input_list[0]
    else:
        return None

def retrieve_element_from_index(input_list, index):
    if 0 <= index < len(input_list):
        return input_list[index]
    else:
        return None

def retrieve_last_element_from_list(input_list):
    if input_list:
        return input_list[-1]
    else:
        return None
