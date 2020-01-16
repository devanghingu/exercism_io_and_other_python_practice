def distance(strand_a, strand_b):
    strand_a,strand_b=strand_a.lower(),strand_b.lower()
    if(len(strand_a) != len(strand_b)):
        raise ValueError("DNA value length {0} does not match with {1}".format(strand_a,strand_b))
    return sum(list([1 for i,j in zip(strand_a,strand_b) if(i!=j)]))
    


print("hello world")
print(distance('asdf','addd'))