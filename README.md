# Bioinformatics Algorithms

Welcome to my Bioinformatics Algorithms repository!

This repository serves as a centralized collection of my computational biology projects, scripts, and algorithms. Here, I implement mathematical and algorithmic solutions to analyze genomic data, solve motif-finding problems, and understand fundamental bioinformatics challenges.

## 📚 Current Projects

### 1. Finding the Origin of Replication (OriC)

**Directory:** `/Finding The Origin Of Replication`

A modular Python pipeline designed to locate the origin of replication (ori) in bacterial genomes (such as *Salmonella enterica*). The pipeline mimics how professional bioinformaticians combine macroscopic and microscopic DNA analysis techniques.

- **calculate_skew.py**: Reads a full genome and calculates the GC Skew (G - C) to find the global minimum—the macroscopic region where the DNA halves transition.  
- **creating_ori.py**: Safely extracts a 500-nucleotide search window centered around the minimum skew index(es) for targeted analysis.  
- **frequent_kmer.py**: Uses a sliding-window algorithm to find the most frequent k-mers (DnaA boxes), accounting for mutations (up to d mismatches) and reverse complements to aggregate a final binding site prediction.

**Key Features:**
- Efficient genome parsing and string manipulation
- GC Skew calculation for origin identification
- K-mer frequency analysis with mismatch tolerance
- Reverse complement handling

[📖 Full Documentation](Finding%20The%20Origin%20Of%20Replication/README.md)

---

### 2. Motif Enumeration Algorithm

**Directory:** `/Motif Enumeration Algorithm`

An implementation of the Motif Enumeration Algorithm to discover conserved sequence patterns (motifs) across multiple DNA sequences. The algorithm finds all **(k, d)-motifs**—k-length sequences that appear in all input strings with at most d mismatches.

**Key Files:**
- **MotifEnumeration.py**: Core algorithm that identifies motifs
- **Neighbors.py**: Generates k-mer neighborhoods within Hamming distance d
- **HammingDistance.py**: Calculates sequence similarity
- **main.py**: Command-line interface for running the algorithm

**Features:**
- Brute-force motif discovery
- Comprehensive neighborhood generation
- Hamming distance-based matching
- Batch processing support

**Time Complexity:** O(n × m × 4^k × m × k)

[📖 Full Documentation](Motif%20Enumeration%20Algorithm/README.md)

---

### 3. Median String Problem

**Directory:** `/Median String Problem`

A bioinformatics algorithm that solves the motif-finding problem by identifying the k-length DNA pattern that minimizes the total Hamming distance to all input sequences. This approach finds a "median" pattern that is most representative of a DNA sequence collection.

**Key Files:**
- **MedianString.py**: Core algorithm implementation
- **4K_DNACombinations.py**: Generates all possible k-length DNA patterns
- **distance.py**: Calculates Hamming distances and pattern-to-sequences distance
- **main.py**: Command-line interface for running the algorithm

**Features:**
- Brute-force pattern search
- Total distance minimization
- Efficient k-mer generation
- Hamming distance calculations

**Time Complexity:** O(4^k × n × m × k) where:
- k = pattern length
- n = number of DNA strings
- m = average length of DNA strings

[📖 Full Documentation](Median%20String%20Problem/README.md)

---

## 🧬 Skills & Concepts Demonstrated

- **Genomic String Manipulation**: Parsing FASTA/text files, reverse complements, and Hamming distance calculations.  
- **Algorithm Design**: Sliding window techniques, pattern matching, and optimization for large datasets (e.g., handling 5+ million nucleotide strings efficiently).  
- **Robust Data Handling**: Implementing edge-case safety checks (boundary checking for string slicing) and avoiding exponential memory explosions by utilizing Python `set()` structures.
- **Recursive Algorithms**: Efficient neighborhood generation using recursion with memoization patterns.
- **Bioinformatics Fundamentals**: Understanding of sequence analysis, motif discovery, and genomic features.

---

## 🚀 How to Use

Each project sub-directory contains its own specific instructions and scripts. Generally, you can run the Python files from your terminal:

```bash
# Example for the OriC pipeline:
python calculate_skew.py
python creating_ori.py
python frequent_kmer.py

# Example for Motif Enumeration:
python main.py

# Example for Median String Problem:
python main.py
```

**Note:** Datasets (like full bacterial genomes or sequence files) may need to be downloaded or placed in the appropriate directory to run the scripts.

---

## 📋 Repository Structure

```
Bioinformatics-Algorithms/
├── Finding The Origin Of Replication/
│   ├── calculate_skew.py
│   ├── creating_ori.py
│   ├── frequent_kmer.py
│   └── README.md
├── Motif Enumeration Algorithm/
│   ├── MotifEnumeration.py
│   ├── Neighbors.py
│   ├── HammingDistance.py
│   ├── main.py
│   ├── dataset_30302_8.txt
│   └── README.md
├── Median String Problem/
│   ├── 4K_DNACombinations.py
│   ├── MedianString.py
│   ├── distance.py
│   ├── main.py
│   ├── dataset_30304_9.txt
│   └── README.md
└── README.md
```

---

## 🔧 Requirements

- **Python 3.x**
- No external dependencies required
- Standard library only (os, sys, etc.)

---

## 📖 Learning Resources

These implementations follow concepts from:
- Bioinformatics Specialization (Coursera) - University of California, San Diego
- "Bioinformatics Algorithms: An Active Learning Approach" by Compeau & Pevzner

---

## 💡 Future Projects

Planned additions to this repository:
- Multiple Sequence Alignment (MSA)
- Hidden Markov Models (HMM) for sequence profiling
- De Bruijn Graph construction for sequence assembly
- RNA folding and secondary structure prediction

---

## 📧 Contact & Questions

Feel free to reach out if you have questions about any of the algorithms or implementations!

---

**Last Updated:** July 18, 2026
