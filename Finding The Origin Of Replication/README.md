# Finding the Origin of Replication (OriC)

## Overview

This project contains a three-step Python pipeline to computationally locate the origin of replication (ori) in bacterial genomes, such as *Salmonella enterica*. Rather than blindly searching the entire genome for DnaA boxes (which is computationally expensive and prone to false positives), this pipeline first uses GC Skew to narrow down the search region, then identifies the most frequent k-mers in that region.

## Description

The origin of replication (ori) is a specific region in bacterial genomes where DNA replication begins. This project implements a professional bioinformatician's approach: combining **macroscopic** insights (GC Skew analysis) with **microscopic** analysis (k-mer frequency).

The pipeline works in three coordinated steps:
1. Identify the macroscopic region using GC Skew
2. Extract a targeted window around the minimum skew
3. Discover the microscopic signatures (DnaA boxes) within that region

## 🧬 How It Works

### Step 1: Calculate GC Skew (`calculate_skew.py`)

**What it does:** 
- Reads the full genome string and calculates the running GC Skew (G - C)
- The biological origin of replication typically occurs at the global minimum of this skew
- This is based on the observation that replication is asymmetrical, creating compositional bias in leading vs. lagging strands

**Output:** 
- Identifies the exact index (or indices) of the global minimum skew
- Provides both the minimum value and its position(s)

**Algorithm:**
```
For each nucleotide in genome:
  if nucleotide == 'G': increment skew
  if nucleotide == 'C': decrement skew
Track minimum value and its position
```

---

### Step 2: Extract OriC Region (`creating_ori.py`)

**What it does:** 
- Uses the minimum skew positions to extract the suspected ori region
- Extracts a 500-nucleotide window centered around the minimum skew index

**Key Feature:** 
- If the skew calculation finds multiple minimum points, this script uses boundary-safe slicing to extract a 500-nucleotide window centered around all minimums and concatenates them
- Prevents index out-of-bounds errors with intelligent boundary checking

**Output:** 
- Generates a text file named `possible_ori.txt` containing the targeted sequence(s)

---

### Step 3: Find Frequent K-mers (`frequent_kmer.py`)

**What it does:** 
- Scans `possible_ori.txt` for the most frequent *k*-mers (*k*=9) while allowing for up to *d*=1 mismatches
- Groups votes for a sequence alongside its reverse complement (accounting for both DNA strands)
- DnaA boxes are the binding sites where the DnaA protein initiates replication

**Output:** 
- Prints the exact 9-mer sequences (the predicted DnaA boxes) that appear most frequently in the ori region

**Algorithm Features:**
- Sliding-window k-mer extraction
- Hamming distance-based mismatch tolerance
- Reverse complement aggregation (both strands considered)

---

## 🚀 Usage Instructions

### Prerequisites

1. Ensure your genome file (e.g., `Salmonella_enterica.txt`) is placed in this directory
2. The file should contain a continuous DNA sequence (ATCG characters only)

### Running the Pipeline

Run the pipeline in the following order from your terminal:

```bash
# Step 1: Calculate the skew and find the minimum indices
python calculate_skew.py

# Step 2: Extract the 500-bp windows into possible_ori.txt
python creating_ori.py

# Step 3: Find the most frequent 9-mers with 1 mismatch + reverse complements
python frequent_kmer.py
```

Each script will prompt you for input or generate intermediate files automatically.

---

## 📝 Input/Output Details

### Input Data

The scripts expect a standard `.txt` or `.fasta` file. The file reading logic automatically:
- Strips newline characters (`\n`)
- Converts the sequence to uppercase
- Ensures accurate processing regardless of formatting

**Expected format:**
```
ATCGATCGATCGATCGATCG...
```

### Output Files

1. **calculate_skew.py** → Terminal output
   - Displays: minimum skew value and index/indices

2. **creating_ori.py** → `possible_ori.txt`
   - Contains: 500-bp (or multi-window) extracted sequence(s)

3. **frequent_kmer.py** → Terminal output
   - Displays: Most frequent 9-mers (DnaA boxes) with occurrence counts

### Algorithm Parameters

By default, the pipeline uses:
- **k** = 9 (k-mer length)
- **d** = 1 (maximum mismatches)
- **window** = 500 nucleotides

These parameters can be easily adjusted inside each script for different biological use cases:
- Smaller k values = more k-mers (faster, less specific)
- Larger k values = fewer k-mers (slower, more specific)
- Adjusting d changes mismatch tolerance

---

## 🧪 Example Workflow

**Input:** Genome file with 5 million nucleotides

**Step 1 Output:**
```
Minimum skew: -15
Position(s): 3923456
```

**Step 2 Output:**
- `possible_ori.txt` created with 500bp region around position 3923456

**Step 3 Output:**
```
ATGATCATGA appears 13 times (including reverse complement)
TCGATCGATC appears 12 times
ATCGATCGAT appears 11 times
```

---

## 🔬 Biological Background

### What is OriC?

The Origin of Replication (OriC) is where DNA replication begins in bacteria. It typically:
- Is 200-300 bp in length
- Contains multiple DnaA boxes (9-11 bp consensus sequences)
- Shows compositional bias due to asymmetric replication
- Is highly conserved across strains

### What are DnaA Boxes?

DnaA boxes are:
- Short DNA sequences (~9 bp) where DnaA protein binds
- Multiple DnaA boxes cluster in the ori region
- Recognized by their consensus sequence
- Essential for initiating DNA replication

### Why GC Skew?

DNA replication is asymmetrical:
- Leading strand: continuous synthesis (has more C's)
- Lagging strand: discontinuous synthesis (has more G's)
- At replication origin, there's a transition point
- This creates a detectable minimum in GC Skew

---

## 📊 Algorithm Complexity

- **Time Complexity:** O(n + m × k) where:
  - n = genome length (for skew calculation)
  - m = ori length
  - k = k-mer length

- **Space Complexity:** O(4^k) for storing k-mer frequencies

---

## 💡 Skills & Concepts Demonstrated

- **Genomic String Manipulation**: Reverse complements, sequence parsing
- **Algorithmic Optimization**: Efficient sliding window, hash-based storage
- **File I/O**: Reading various genomic formats
- **Bioinformatics Theory**: Understanding of replication mechanics
- **Edge-Case Handling**: Boundary checking, multiple minima handling

---

## 🔧 Requirements

- **Python 3.x**
- No external dependencies (uses only Python standard library)

---

## 📚 References & Further Reading

- Compeau & Pevzner - "Bioinformatics Algorithms: An Active Learning Approach"
- DnaA protein structure and binding: NCBI/PubMed
- GC Skew analysis: Published genomic studies

---

## 📧 Notes

- This implementation is suitable for bacterial genomes (typically 1-10 million bp)
- For eukaryotic genomes, multiple origins complicate the analysis
- Results may vary based on sequencing quality and assembly gaps
- Always validate computational predictions with experimental evidence

---

**Last Updated:** July 18, 2026
