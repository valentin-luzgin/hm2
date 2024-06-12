def return_dict_containing_key_passed_to_function(list_of_states: list, state: str = "EXECUTED") -> list:
    """возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию
    значение."""
    new_list = []
    for i in list_of_states:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_dicts_by_date(data: list, reverse: bool = True) -> list:
    """возвращает отсортированный по времени список"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
