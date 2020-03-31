def to_rna(dna_strand):
    """ Return RNA String given DNA String """
    dna={'G':'C','C':'G','T':'A','A':'U'}
    rna=[]
    [rna.append(dna[val]) for val in dna_strand]
    return "".join(rna)

