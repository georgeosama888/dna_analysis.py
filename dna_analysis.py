dna_sequence = "ATGCGTATCGGATCGATTACG"
sequence_length = len(dna_sequence)

nucleotide_counts = {
    "A": 0,
    "T": 0,
    "G": 0,
    "C": 0
}

valid_bases = ["A", "T", "G", "C"]

print("Sequence:", dna_sequence)
print("Sequence length:", sequence_length)

for nucleotide in dna_sequence:
    if nucleotide in valid_bases:
        nucleotide_counts[nucleotide] += 1
    else:
        print("invalid base found:", nucleotide)

bases = list(nucleotide_counts.keys())

index = 0

while index < len(bases):
    base = bases[index]
    print(base, ":" ,nucleotide_counts[base])
    index += 1

def calculate_gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_percentage = (g_count + c_count) / len(sequence) *100

    return gc_percentage

gc_content = calculate_gc_content(dna_sequence)
print("GC Content:", round(gc_content, 2), "%")