# Greedy Motif Search

This folder contains a simple implementation of the Greedy Motif Search algorithm (with and without pseudocounts) for finding k-mer motifs in a collection of DNA strings.

## Files

- `main.py` — CLI entry point. Reads an input file and runs `GreedyMotifSearchWithPseudocounts`. Prints each winning k-mer on its own line.
- `GreedyMotif.py` — Implements the two Greedy Motif Search variants:
  - `GreedyMotifSearchWithPseudocounts(Dna, k, t)` — builds profiles using pseudocounts (+1 for each nucleotide) when estimating column probabilities.
  - `GreedyMotifSearch(Dna, k, t)` — builds profiles without pseudocounts (uses raw frequencies).
- `Profile.py` — Profile-building helpers:
  - `BuildProfile(Motifs)` — frequency profile without pseudocounts (returns column frequencies).
  - `BuildProfileWithPseudocounts(Motifs)` — profile with +1 pseudocount for each nucleotide per column.
- `ProbableKmer.py` — `ProfileMostProbableKmer(string, k, profile)` selects the k-mer in `string` with highest probability under `profile`.
- `Score.py` — `Score(Motifs)` computes the motif score (sum of Hamming distances from the consensus column-wise).
- `dataset_30306_9.txt` — example dataset included in the repo.

## Functions (without pseudocounts)

The repository offers versions of key routines that do not use pseudocounts. These are useful when you want to work with raw column frequencies rather than smoothed estimates.

- `BuildProfile(Motifs)`
  - Input: list of strings `Motifs` (all of length `k`).
  - Output: a profile dict mapping each nucleotide `'A'`, `'C'`, `'G'`, `'T'` to a list of length `k` containing the column frequencies (counts divided by number of motifs `t`).
  - Note: this does not add pseudocounts; if a nucleotide never appears in a column, its frequency in that column will be 0.

- `GreedyMotifSearch(Dna, k, t)`
  - Input: `Dna` — list of `t` DNA strings, `k` — k-mer length, `t` — number of strings.
  - Behavior: runs the greedy motif search using `BuildProfile` (raw frequencies) to construct profiles while extending motifs.
  - Output: list of `t` k-mers (one chosen from each DNA string) that achieved the best score found by the greedy algorithm.

Use the no-pseudocounts variants when you explicitly want raw frequencies; otherwise the pseudocount variants (`BuildProfileWithPseudocounts`, `GreedyMotifSearchWithPseudocounts`) help avoid zero probabilities and provide more stable behavior on small datasets.

## Usage

1. From the repository root run:

   python "Greedy Motif Search/main.py"

2. When prompted, supply the dataset path (for example: `Greedy Motif Search/dataset_30306_9.txt`).

3. The script expects first line with two integers `k t` (k-mer length and number of DNA strings), and the following whitespace-separated tokens are treated as the t DNA strings (A/C/G/T). Example input format:

````
4 5
GCGTTCAG... 
AATGCC...
... (each DNA string separated by whitespace or newline)
````

4. Output: one winning k-mer per line. If you prefer a single space-separated line of winners, replace the printing loop in `main.py` with `print(" ".join(winners))`.

## Recommendations

- Input validation: ensure the DNA strings are of length >= k and contain only A/C/G/T.
- If you want deterministic or alternative tie-breaking, update `ProfileMostProbableKmer` accordingly.
- Consider adding unit tests for `Score`, `BuildProfile`, `BuildProfileWithPseudocounts`, and `ProfileMostProbableKmer` for future maintenance.
