# Motif Enumeration Algorithm

## Overview

This folder contains an implementation of the **Motif Enumeration Algorithm**, a bioinformatics algorithm used to find conserved sequence patterns (motifs) across multiple DNA sequences.

## Description

The Motif Enumeration Algorithm identifies all **(k, d)-motifs** in a collection of DNA strings. A **(k, d)-motif** is a k-length sequence that appears in every string of the collection with at most d mismatches (substitutions).

This implementation uses a **brute-force approach** with the Neighbors function to generate all possible k-mers within the allowed Hamming distance and checks their presence in all input sequences.

## Files

### Core Modules

- **MotifEnumeration.py** - Main algorithm implementation
  - `MotifEnumeration(Dna, k, d)` - Finds all (k, d)-motifs in DNA sequences

- **Neighbors.py** - Generates k-mer neighborhood
  - `Neighbors(pattern, d)` - Returns all k-mers within Hamming distance d from a pattern

- **HammingDistance.py** - Calculates sequence similarity
  - `HammingDistance(p, q)` - Computes the number of mismatches between two sequences

### Execution

- **main.py** - Entry point for running the algorithm
  - Reads input from a file
  - Outputs results to `motif.txt`

### Data

- **dataset_30302_8.txt** - Sample input dataset
- **motif.txt** - Output file containing discovered motifs

## Usage

### Input Format

The input file should have:
- **First line:** Two space-separated integers `k` and `d`
  - `k`: length of the motif to find
  - `d`: maximum number of mismatches allowed
- **Remaining lines:** DNA sequences (one per line)

Example:
```
3 1
ACGT
TACG
TGCA
```

### Running the Algorithm

```bash
python main.py
```

When prompted, enter the path to your input file:
```
Enter file path: dataset_30302_8.txt
```

The program will output discovered motifs to `motif.txt`.

## How It Works

1. **Extract k-mers** from the first DNA sequence
2. **Generate neighbors** for each k-mer (all sequences within Hamming distance d)
3. **Check presence** of each neighbor in all other DNA sequences
4. **Collect valid motifs** that appear in every sequence with at most d mismatches
5. **Save results** to output file

## Algorithm Complexity

- **Time Complexity:** O(n × m × 4^k × m × k) where:
  - n = number of sequences
  - m = length of sequences
  - k = motif length
  
- **Space Complexity:** O(4^k) for storing the neighborhood

## Example

**Input:**
```
3 1
ACGT
TACG
TGCA
```

**Output:** 
Motifs that appear in all sequences with at most 1 mismatch

## Requirements

- Python 3.x
- No external dependencies

## Notes

- This is a brute-force implementation suitable for small k values (typically k ≤ 12)
- For larger datasets, consider more efficient algorithms like MEME or Gibbs sampling
- All DNA sequences should contain only valid nucleotides (A, C, G, T)
