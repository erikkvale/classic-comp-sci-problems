"""
Module applying search algorithms and related data structures to DNA sequencing
and bioinformatics

Nucleotides: A, C, G, T
Codon: Combination of any three nucleotides
Gene: Composition of codons
"""
from enum import IntEnum
from typing import Tuple, List

# Type aliases
Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

# Play gene
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        else:
            codon: Codon = (
                Nucleotide[s[i]],
                Nucleotide[s[i+1]],
                Nucleotide[s[i+2]],
            )
            gene.append(codon)
    return gene


def linear_search(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


if __name__ == "__main__":
    gene: Gene = string_to_gene(gene_str)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    ggc: Codon = (Nucleotide.G, Nucleotide.G, Nucleotide.C)
    print(linear_search(gene, acg))
    print(linear_search(gene, ggc))







