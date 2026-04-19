from typing import Any, Collection

def lengther(out:list[Collection|str] | tuple[Collection|str] | dict[Any, Collection|str]) -> list[int] | tuple[int] | dict[Any, int]:
    """
    :out: *list[Collection|str] | tuple[Collection|str] | dict[Any, Collection|str]* The Collection of Collections (alredy processed) that is returned with lengths.

    :return: *list[int] | tuple[int] | dict[Any, int]* Returns the lengths of all the collections in data
    """
    original_type = type(out)
    
    if issubclass(original_type, dict):
        return [(o[0], len(o[1])) for o in list(out.items())]
    else:
        return [len(o) for o in out]

def elegantReturns(out:list[Collection|str] | tuple[Collection|str] | dict[Any, Collection|str], diagonostics:bool=True) -> None:
    for inx, i in enumerate(out):
        print(i)


def collectionSort(data:list[Collection] | dict[Any, Collection] | tuple[Collection], reverse:bool = False, group:bool|list[type] = False) -> list[Collection] | dict[Any, Collection] | tuple[Collection]:
    """
    Sorts collections by length.
    <br><br>

    :data: *list[Collection] | dict[Any, Collection] | tuple[Collection]* An ordered collection of other collections (duh)

    :reverse: *bool* Tells the function wether to sort the collections in descending order or not - set to False by default.

    :group: *bool | list[type]* Tells the function how to group the sorted items - set to False by default. If set to True,
    will group using [list, tuple, dict, range, set, frozenset, bytes, bytearray, memoryview]. You can set a custom list of types for the function to organise the sorted inputs.
    The function will remove invalid types and duplicates automatically.

    P.S. if your groups list ends up empty, the function resets it to [list, tuple, dict, range, set, frozenset, bytes, bytearray, memoryview].
    <br>
    P.S.S. if your list lacks some types, they will be added in automatically.
    <br><br>

    :return: An ordered collection - of the same type as the input collection - sorted in either ascending or descending order (by length)
    with the elements grouped as specified in the function call
    """
    try:
        if len(data) in [0,1]:
            return data
    except ValueError:
        pass

    original_type = type(data)
    items = list(data.items()) if issubclass(original_type, dict) else None
    data = list(data) if original_type != list else data

    if group is False:
        if items is not None:
            data = sorted(items, key=lambda x: len(x[1]), reverse=reverse)
        else:
            data = sorted(data, key=lambda x: len(x), reverse=reverse)

        return original_type(data) if original_type != list else data

    #SUBFUNCTION ZONE
    def sort_by_type(stuff:list) -> tuple[ list[Collection] ]:
        stuff = sorted(stuff, key=lambda x: len(x), reverse=reverse)
        type_buckets = {}
        for item in stuff:
            t = type(item)
            if t not in type_buckets:
                type_buckets[t] = [item]
            else:
                type_buckets[t].append(item)
        
        return type_buckets

    
    def sort_by_type_dict(stuff: list[tuple]) -> list[tuple]:
        stuff = sorted(stuff, key=lambda x: len(x[1]), reverse=reverse)
        type_buckets = {}
        for item in stuff:
            t = type(item[1])
            if t not in type_buckets:
                type_buckets[t] = [item]
            else:
                type_buckets[t].append(item)
        return type_buckets
    #END OF SUBFUNCTION ZONE


    if group is True:
        data = sort_by_type(data) if items is None else sort_by_type_dict(items)
        return original_type(data) if original_type != list else data
        
    else:
        #Clears duplicates & removes invalid types
        data = sort_by_type(data) if items is None else sort_by_type_dict(items)

        
        group = [list, tuple, dict, range, set, frozenset, bytes, bytearray, memoryview] if group in [ [], [Collection], Collection ] else list(dict.fromkeys(group))
        if group != [list, tuple, dict, range, set, frozenset, bytes, bytearray, memoryview]:
            group = [g for g in group if issubclass(g,  Collection) and g is not str] #invalid type removal
            group += [g for g in [list, tuple, dict, range, set, frozenset, bytes, bytearray, memoryview] if g not in group ]

        running = data
        data = [running[g] for g in group if g in running]

        if original_type == dict:
            return dict(item for bucket in data for item in bucket)
        else:
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
    method =  method.replace(' ','').lower()

    if method in ["a","alpha","alphabetical","alphabetically"]:
        if not issubclass(original_type, dict):
            data = sorted(data, reverse=reverse)
        else:
            data = sorted(items, key=lambda x: x[1], reverse=reverse)
        
        return original_type(data) if original_type != list else data

    elif method in ["l","len","length","lengthwise"]:
        if not issubclass(original_type, dict):
            data = sorted( [(len(d), d) for d in data], reverse=reverse )
        else:
            data = sorted( [(len(i[1]), i) for i in items], key=lambda x: x[0],  reverse=reverse )
        
        return original_type([d[1] for d in data]) if original_type != list else data
    
    else:
        raise NotImplementedError("Invalid string sorting method, use 'a' or don't specify for alphabetic sorting, use 'l' for lengthwise sorting. See function documentation for more options")

def hypersort(data:list|tuple|dict, reverse:bool=False, strMethod:str="l", group:bool|list[type]=False):
    """
    Orders a list of multiple types.
    <br><br>

    :data: A collection of... anything.
    :reverse: Tells the function wether or not to sort in descending order
    :strMethod: Tells the function how to sort strings,
    Inputs in ["a","alpha","alphabetical","alphabetically"] cause the function to sort alphabetically 
    Inputs in ["l","len","length","lengthwise"] cause the function to sort by length.
    :group: Tells the function how to group types. By default, its set to False, if set to True, will sort [str, bool, int, float, list, tuple, dict, set, bytes, bytearray, memoryview]
    """
    pass