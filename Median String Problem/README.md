# Median String Problem

## Overview
The Median String Problem is a bioinformatics algorithm that finds the most similar pattern to a collection of DNA strings. It solves the motif-finding problem by identifying a k-length DNA sequence that minimizes the total Hamming distance to all input sequences.

## Problem Description
Given:
- A collection of DNA strings
- A pattern length `k`

Find:
- A k-length pattern that minimizes the sum of minimum Hamming distances to each DNA string

## Algorithm
The solution uses a brute-force approach:
1. Generate all possible 4^k DNA patterns of length k
2. For each pattern, calculate its total distance to all DNA strings
3. Return the pattern with the minimum total distance

### Time Complexity
- **O(4^k × n × m × k)** where:
  - k = pattern length
  - n = number of DNA strings
  - m = average length of DNA strings

## Files

### `main.py`
Entry point of the program. Reads input from a file and outputs the median string.

**Usage:**
```bash
python main.py
Enter file path: dataset_30304_9.txt
```

### `MedianString.py`
Core algorithm implementation. Contains the `MedianString(Dna, k)` function that returns the optimal pattern.

**Functions:**
- `MedianString(Dna, k)` - Finds and returns the median string for a given DNA collection

### `4K_DNACombinations.py`
Generates all possible DNA sequences of a given length.

**Functions:**
- `AllStrings(k)` - Recursively generates all 4^k possible k-length DNA combinations

### `distance.py`
Calculates the distance between a pattern and a collection of DNA strings.

**Functions:**
- `hamming_distance(seq1, seq2)` - Computes Hamming distance between two sequences
- `DistanceBetweenPatternAndStrings(Pattern, Dna)` - Computes total distance from pattern to all DNA strings

### `dataset_30304_9.txt`
Sample input file containing test data.

**Format:**
```
k
DNA_string_1
DNA_string_2
...
DNA_string_n
```

## Input Format
The input file should contain:
- First line: `k` (the pattern length)
- Following lines: DNA sequences (one per line, uppercase letters A, C, G, T)

**Example:**
```
4
TCGGACACGTT
GATTGTAGGCG
CCATCGTAGGA
```

## Output
The program outputs the median string (k-length DNA pattern that minimizes total Hamming distance).

**Example Output:**
```
TCGA
```

## Dependencies
- Python 3.x
- No external libraries required

## Example Execution

```bash
$ python main.py
Enter file path: dataset_30304_9.txt
ACGT
```

## How to Run
1. Prepare an input file with the required format
2. Run `main.py`:
   ```bash
   python main.py
   ```
3. Enter the path to your input file when prompted
4. The median string will be displayed

## Notes
- All DNA sequences in the input should be uppercase
- The algorithm will convert input to uppercase automatically
- The brute-force approach is suitable for small k values (typically k ≤ 12)
- For larger k values, consider using optimized motif-finding algorithms

## References
- Bioinformatics Algorithms Course materials
- Problem from: https://www.coursera.org/
