import itertools
def transpose(input_line):
    input_line = (input_line.split("\n"))
    
    max_length = 0
    for items in input_line:
        if len(items) > max_length:
            max_length = len(items)

    for items in range(len(input_line)):
        if len(input_line[items]) != max_length:
            input_line[items] = input_line[items] + " "*(max_length-len(input_line[items]))
    
    result = []
    for item in range(len(input_line[0])):
        
        for x in range(len(input_line)):
            try:
                result[item] +=(input_line[x][item])
            except IndexError:
                result.append(input_line[x][item])
    if len(result) > 0:
        result[len(result)-1] = result[len(result)-1].rstrip()
    return("\n".join(result))