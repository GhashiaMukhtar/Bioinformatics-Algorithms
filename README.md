**Bioinformatics Algorithms**

Welcome to my Bioinformatics Algorithms repository!

This repository serves as a centralized collection of my computational biology projects, scripts, and algorithms. Here, I implement mathematical and algorithmic solutions to analyze genomic data, search for biological motifs, and solve real-world bioinformatics challenges.

### Current Projects

**1. Finding the Origin of Replication (OriC)**

**Directory:** `/Finding The Origin Of Replication` (or your chosen sub-folder name)

A modular Python pipeline designed to locate the origin of replication (ori) in bacterial genomes (such as *Salmonella enterica*). The pipeline mimics how professional bioinformaticians combine macroscopic and microscopic search techniques.

- **calculate_skew.py**: Reads a full genome and calculates the GC Skew (G - C) to find the global minimum—the macroscopic region where the DNA halves transition.  
- **creating_ori.py**: Safely extracts a 500-nucleotide search window centered around the minimum skew index(es) for targeted analysis.  
- **frequent_kmer.py**: Uses a sliding-window algorithm to find the most frequent k-mers (DnaA boxes), accounting for mutations (up to d mismatches) and reverse complements to aggregate a final biological consensus.

### Skills & Concepts Demonstrated

- **Genomic String Manipulation**: Parsing FASTA/text files, reverse complements, and Hamming distance calculations.  
- **Algorithm Design**: Sliding window techniques, pattern matching, and optimization for large datasets (e.g., handling 5+ million nucleotide strings efficiently).  
- **Robust Data Handling**: Implementing edge-case safety checks (boundary checking for string slicing) and avoiding exponential memory explosions by utilizing Python `set()` structures.

### How to Use

Each project sub-directory contains its own specific instructions or scripts. Generally, you can run the Python files from your terminal:

```bash
# Example for the OriC pipeline:
python calculate_skew.py
python creating_ori.py
python frequent_kmer.py
```

**Note:** Datasets (like full bacterial genomes) may need to be downloaded from NCBI and placed in the appropriate directory to run the scripts.
