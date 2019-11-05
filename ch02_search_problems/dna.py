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


def binary_search(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    my_gene: Gene = string_to_gene(gene_str)
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    ggc: Codon = (Nucleotide.G, Nucleotide.G, Nucleotide.C)

    # Linear search: expecting (True, False)
    assert linear_search(my_gene, acg)      # O(n)
    assert not linear_search(my_gene, ggc)  # O(n)

    # Binary search: expecting (True, False)
    my_gene = sorted(my_gene)               # O(n log n)
    assert binary_search(my_gene, acg)      # O(log n)
    assert not binary_search(my_gene, ggc)  # O(log n)







