def to_rna(dna_strand):

    if dna_strand == '':
        return dna_strand

    rna_new = ''
    for i in dna_strand:
        if i == 'G':
            rna_new += 'C'
        if i == 'C':
            rna_new += 'G'
        if i == 'T':
            rna_new += 'A'
        if i == 'A':
            rna_new += 'U'

    return rna_new

p = to_rna("C")
print(p)

p = to_rna("ACGTGGTCTTAA")
print(p)