# Greedy Motif Search

This folder contains a simple implementation of the Greedy Motif Search algorithm (with and without pseudocounts) for finding k-mer motifs in a collection of DNA strings.

## Files

- `main.py` — CLI entry point. Reads an input file and runs GreedyMotifSearchWithPseudocounts. Prints each winning k-mer on its own line.
- `GreedyMotif.py` — Implements the two Greedy Motif Search variants:
  - `GreedyMotifSearchWithPseudocounts(Dna, k, t)` — builds profiles using pseudocounts.
  - `GreedyMotifSearch(Dna, k, t)` — builds profiles without pseudocounts.
- `Profile.py` — Profile-building helpers:
  - `BuildProfile(Motifs)` — frequency profile (no pseudocounts).
  - `BuildProfileWithPseudocounts(Motifs)` — profile with +1 pseudocount for each nucleotide.
- `ProbableKmer.py` — `ProfileMostProbableKmer(string, k, profile)` selects the k-mer in `string` with highest probability under `profile`.
- `Score.py` — `Score(Motifs)` computes the motif score (sum of Hamming distances from the consensus column-wise).
- `dataset_30306_9.txt` — example dataset (kept in the repo).

## Usage

1. From the repository root run:

   python "Greedy Motif Search/main.py"

2. When prompted, supply the dataset path (for example: `Greedy Motif Search/dataset_30306_9.txt`).

3. The script reads the first line expecting two integers `k t` (k-mer length and number of DNA strings), and the following lines are treated as DNA strings (whitespace separated). Example input format:

````
4 5
GCGTTCAG... 
AATGCC...
... (each DNA string separated by whitespace or newline)
````

4. Output: one winning k-mer per line (the motif found from each DNA string for the best-scoring motif set).

## Notes on fixes and checks performed

- Fixed a NameError: `GreedyMotifSearch` previously called `BuildProfile` but `Profile.py` only defined `BuildProfileWithPseudocounts`. I added `BuildProfile` and kept the pseudocounts variant.
- Updated `GreedyMotif.py` to import `BuildProfile` and to copy motif lists when assigning `BestMotifs` (to avoid aliasing issues).
- Fixed `main.py` printing: it now prints each motif string directly (previously used `" ".join(motif)` which would space out characters).
- Performed a final static check for common errors (indexing, empty inputs, and nucleotide keys). The code assumes:
  - `Dna` is a non-empty list of strings containing only A/C/G/T.
  - Each DNA string has length >= k.

You may want to add input validation (non-empty Dna, valid characters, lengths) and unit tests for `Score`, `BuildProfile`, and `ProfileMostProbableKmer`.

## Example

Run the included dataset and you should see k-mers printed, one per line. If you prefer a single space-separated line of motifs instead, open `main.py` and replace the printing loop with:

```python
print(" ".join(winners))
```

## Contact

If you want me to additionally add unit tests, type hints, or CI checks, I can add them in follow-up commits.
