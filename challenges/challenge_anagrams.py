def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1: # se não reduzi o suficiente, continua
        mid = (start + end) // 2 # encontrando o meio
        merge_sort(list, start, mid) # dividindo as listas
        merge_sort(list, mid, end)
        merge(list, start, mid, end) # unindo as listas

    return list

def merge(list, start, mid, end):
    left = list[start:mid] # indexando a lista da esquerda
    right = list[mid:end] # indexando a lista da direita

    left_index, right_index = 0, 0 # as duas listas começarão do início

    for general_index in range(start, end): # percorrer sobre a lista inteira como se fosse uma
        if left_index >= len(left): # se os elementos da esquerda acabaram, preenche o restante com a lista da direita 
            list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right): # se os elementos da direita acabaram, preenche o restante com a lista da esquerda
            list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]: # se o elemento do topo da esquerda for menor que o da direita, ele será o escolhido
            list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list[general_index] = right[right_index] # caso o da direita seja menor, ele será o escolhido
            right_index = right_index + 1

# REFERENCIA: COURSE TRYBE

def is_anagram(first_string, second_string):
    
    string_1 = list(first_string.lower())
    string_2 = list(second_string.lower())

    string_1_sorted = merge_sort(string_1)
    string_2_sorted = merge_sort(string_2)

    if first_string == "" or second_string == "":
        return (
        "".join(string_1_sorted),
        "".join(string_2_sorted),
        False
    )
    
    return (
        "".join(string_1_sorted),
        "".join(string_2_sorted),
        string_1_sorted == string_2_sorted
    )
