from typing import Any, Collection

def numberSort(data:list[bool|int|float] | dict[Any, bool|int|float] | tuple[bool|int|float], reverse:bool = False, group:bool|list[type] = False) -> list[bool|int|float] | dict[bool|int|float] | tuple[bool|int|float]:
    """
    Sorts numbers.
    <br><br>
    :data: *list[bool|int|float] | dict[Any, bool|int|float] | tuple[bool|int|float]* An ordered collection (i.e. no sets) of numbers (booleans, integers & floats)
    :reverse: *bool* Tells the function wether to sort in descending order or not (set to False by default)
    :group: *bool | list[type]* You can group different types together, by default, it's set to False, but if set to True,
    the function will return booleans, then integers, then floats - [bool, int, float].
    Optionally, you can specify the order of grouping using a custom list. Invalid types and duplicates are cleared automatically.
    P.S. An empty list will result in the default grouping order being returned [bool, int, float]. 
    Any missing types in the group list will be added in automatically.

    :return: *list[bool|int|float] | dict[Any, bool|int|float] | tuple[bool|int|float]* An ordered collection in the original type given in the data input 
    sorted and grouped as specified by the reverse and group prameters. 
    """

    try: #Tries to return a collection that when worked on, returns itself and is genuinely a waste of computation time
        if len(data) in [0,1]:
            return data
    except TypeError:
        pass

    original_type = type(data)

    data = list(data) if original_type != list else data
    items = list(data.items()) if original_type == dict else None

    if not group: #Returns the sorted data in the input collection (keeps dict key-value pairs intact btw)
        if original_type != dict:
            return original_type(sorted( data, reverse=reverse )) if original_type == tuple else data
        else:
            return original_type(sorted(items, key=lambda x: x[1], reverse=reverse))
    
    elif group: #Returns the sorted data in the input collection and groups booleans, then integers then floats.
        #group = [bool, int, float]
        if original_type != dict:
            data = sorted(data, reverse=reverse)
            data = [ [d for d in data if isinstance(d, bool)], [d for d in data if isinstance(d, int) and not isinstance(d, bool)], [d for d in data if isinstance(d, float)] ]
            data = data[0] + data[1] + data[2]
            return original_type(data) if original_type != list else data

        else:
            items = sorted(items, key=lambda x: x[1], reverse=reverse)
            data = [ [d for d in items if isinstance(d[1], bool)], [d for d in items if isinstance(d[1], int) and not isinstance(d[1], bool)], [d for d in items if isinstance(d[1], float)] ] #Seperates thekey-value pairs by checking the type of the values
            return original_type(data[0] + data[1] + data[2])
    
    else: #Returns the data in the input collection, grouped as specified by the user
        group = list(dict.fromkeys(group))
        group = [g for g in group if g in [bool, int, float] ] if group != [] else [bool, int, float]

        if original_type == dict:
            items = sorted(items, key=lambda x: x[1], reverse=reverse)
            #Seperates key-value pairs by checking the type of the values
            bool_list = [i for i in items if isinstance(i[1], bool)]
            int_list = [i for i in items if isinstance(i[1], int) and not isinstance(i[1], bool)]
            float_list = [i for i in items if isinstance(i[1], float)]

        else:
            data = sorted(data, reverse=reverse)
            bool_list = [d for d in data if isinstance(d, bool)]
            int_list = [d for d in data if isinstance(d, int) and not isinstance(d, bool)]
            float_list = [d for d in data if isinstance(d, float)]

        running = {
            bool: bool_list,
            int: int_list,
            float: float_list
        }
        
        data = []
        for g in running.keys():  #appends missing values if there are missing values
            if g not in group:
                group.append(g)
        for i in group:
            data += running[i]

        if original_type != dict:
            return original_type(data) if original_type != list else data
        else:
            return original_type(data)


def collectionSort(data:list[Collection] | dict[Any, Collection] | tuple[Collection], reverse:bool = False, group:bool|list[type] = False) -> list[Collection] | dict[Any, Collection] | tuple[Collection]:
    """
    Sorts collections by length.
    <br><br>
    :data: *list[Collection] | dict[Any, Collection] | tuple[Collection]* An ordered collection of other collections (duh)
    :reverse: *bool* Tells the function wether to sort the collections in descending order or not - set to False by default.
    :group: *bool | list[type]* Tells the function how to group the sorted items - set to False by default. If set to True,
    will group using [list, tuple, dict, set]. You can set a custom list of types for the function to organise the sorted inputs.
    The function will remove invalid types and duplicates automatically.
    P.S. if your groups list ends up empty , the function resets it to [list, tuple, dict, set].
    P.S.S. if your list lacks some types, they will be added in automatically.

    :return: An ordered collection - of the same type as the input collection - sorted in either ascending or descending order (by length)
    with the elements grouped as specified in the function call
    """
    original_type = type(data)

    try:
        if len(data) in [0,1]:
            return data
    except ValueError:
        pass

    data = list(data) if original_type == tuple else data
    items = list(data.items()) if original_type == dict else None

    if group == False:
        data = sorted(data, key=lambda x: len(x), reverse=reverse) if original_type != dict else sorted(items, key=lambda x: len(x[1]), reverse=reverse)
        return original_type(data) if original_type != list else data

    #SUBFUNCTION ZONE
    def sort_by_type(stuff:list) -> tuple[ list[Collection] ]:
        stuff = [(len(s), s) for s in stuff]
        stuff = sorted(stuff, key=lambda x: x[0], reverse=reverse)

        list_list = [l[1] for l in stuff if isinstance(l[1], list)] #lol
        tuple_list = [t[1] for t in stuff if isinstance(t[1], tuple)]
        dict_list = [d[1] for d in stuff if isinstance(d[1], dict)]
        set_list = [s[1] for s in stuff if isinstance(s[1], set)]
        return list_list, tuple_list, dict_list, set_list
    
    def sort_by_type_dict(stuff:list[tuple]) -> tuple[ list[Collection] ]:
        stuff = sorted(stuff, key=lambda x: len(x[1]), reverse=reverse)

        list_list = [l for l in stuff if isinstance(l[1], list)] #lol
        tuple_list = [t for t in stuff if isinstance(t[1], tuple)]
        dict_list = [d for d in stuff if isinstance(d[1], dict)]
        set_list = [s for s in stuff if isinstance(s[1], set)]
        return list_list, tuple_list, dict_list, set_list
    #END OF SUBFUNCTION ZONE

    
    if group == True:
        #group = [list, tuple, dict, set]

        data = sort_by_type(data) if original_type != dict else sort_by_type_dict(items)
        data = data[0] + data[1] + data[2] + data[3]
        print(data)
        print(type(data))
        print(" ")
        return original_type(data) if original_type != list else data
        
    else:
        #Clears duplicates & removes invalid types
        data = sort_by_type(data) if original_type != dict else sort_by_type_dict(items)

        group = dict.fromkeys(group)
        group = [g for g in group if g in [list, tuple, dict, set] ] if group != [] else [list, tuple, dict, set]
        running = {
            list: data[0],
            tuple: data[1],
            dict: data[2],
            set: data[3]
        }
        for g in running.keys():  #appends missing values to the groups list
            if g not in group:
                group.append(g)

        data = []
        for i in group:
            data += running[i]

        return original_type(data) if original_type != list else data

def strSort(data: list[str] | tuple[str] | dict[Any, str], reverse:bool=False, method:str="a"):
    """
    Sorts strings by length or contents.
    <br><br>
    :data: *list[str] | tuple[str] | dict[Any, str]* An ordered collection of strings.
    :reverse: *bool* Tells the function wether or not to sort in descending order, set to False by default
    :method: *str* Tells the function wether to sort by length or alphabetically, it is, by default, set to sort alphabetically.
    Inputs in ["a","alpha","alphabetical","alphabetically"] cause the function to sort alphabetically 
    Inputs in ["l","len","length","lengthwise"] cause the function to sort by length.
    Anything else will cause an error
    """
    original_type = type(data)

    data = list(data) if original_type == tuple else data
    items = list(data.items()) if original_type == dict else None

    if method.replace(' ','').lower() in ["a","alpha","alphabetical","alphabetically"]:
        if original_type != dict:
            data = sorted(data, reverse=reverse)
            return original_type(data) if original_type != list else data
        else:
            data = sorted(items, key=lambda x: x[1], reverse=reverse)
            return original_type(data)

    elif method.replace(' ','').lower() in ["l","len","length","lengthwise"]:
        if original_type != dict:
            data = [(len(d), d) for d in data]
            data = sorted(data, reverse=reverse)
            data = original_type([d[1] for d in data]) if original_type != list else data
            return data
        else:
            data = [(len(i[1]), i) for i in items]
            data = sorted(data, key=lambda x: x[0], reverse=reverse)
            data = [d[1] for d in data]
            return original_type(data)
    
    else:
        raise NotImplementedError("Invalid string sorting method, use 'a' or don't specify for alphabetic sorting, use 'l' for lengthwise sorting. See function documentation for more options")

def hypersort(data:list|tuple|dict, reverse:bool=False, strMethod:str="l", group:bool|list[type]=False):
    pass