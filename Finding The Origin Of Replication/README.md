**Finding the Origin of Replication (OriC)**

This project contains a three-step Python pipeline to computationally locate the origin of replication (ori) in bacterial genomes, such as *Salmonella enterica*.

Rather than blindly searching the entire genome for DnaA boxes (which is computationally expensive and prone to false positives), this pipeline first uses GC Skew to narrow down the search region, and then applies a sliding window algorithm with mismatches and reverse complements to find the consensus DnaA boxes.

### 🧬 How It Works

**Step 1: `calculate_skew.py`**

- **What it does**: Reads the full genome string and calculates the running GC Skew (G - C). The biological origin of replication typically occurs at the global minimum of this skew.  
- **Output**: Identifies the exact index (or indices) of the global minimum skew.

**Step 2: `creating_ori.py`**

- **What it does**: Uses the minimum skew positions to extract the suspected ori region.  
- **Key Feature**: If the skew calculation finds multiple minimum points, this script uses boundary-safe slicing to extract a 500-nucleotide window centered around all minimums and concatenates them into a single master search string.  
- **Output**: Generates a text file named `possible_ori.txt` containing the targeted sequence(s).

**Step 3: `frequent_kmer.py`**

- **What it does**: Scans `possible_ori.txt` for the most frequent *k*-mers (*k*=9) while allowing for up to *d*=1 mismatches. It also groups votes for a sequence alongside its reverse complement, mimicking how DnaA proteins bind to double-stranded DNA.  
- **Output**: Prints the exact 9-mer sequences (the predicted DnaA boxes) that appear most frequently in the ori region.

### 🚀 Usage Instructions

1. Ensure your genome file (e.g., `Salmonella_enterica.txt`) is placed in this directory.  
2. Run the pipeline in the following order from your terminal:

```bash
# 1. Calculate the skew and find the minimum indices
python calculate_skew.py

# 2. Extract the 500-bp windows into possible_ori.txt
python creating_ori.py

# 3. Find the most frequent 9-mers with 1 mismatch + reverse complements
python frequent_kmer.py
```

### 📝 Input/Output Details

- **Input Data**: The scripts expect a standard `.txt` or `.fasta` file. The file reading logic automatically strips newline characters (`\n`) and converts the sequence to uppercase to ensure accurate matching.  
- **Algorithm Parameters**: By default, the final step searches for *k*=9 with *d*=1 mismatch. These parameters can be easily adjusted inside `frequent_kmer.py` for different biological use cases.
