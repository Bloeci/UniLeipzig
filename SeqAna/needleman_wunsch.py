import numpy as np
import time


# Determine the Score between Char X and Char Y
def match_score(char1, char2, match, mismatch):
    return [match if (char1 == char2) else mismatch]


# Algorithm for Alignment
def NeedlemanWunsch(seq1, seq2, show_score=True, match=1, mismatch=-1, gap=-1):
    start = time.time()

    #  Create Score-Matrix (row,col) + 1, Fill first Row and Column with Numbers
    score = np.zeros((len(seq1) + 1, len(seq2) + 1))
    score[:, 0] = [i * gap for i in range(score.shape[0])]
    score[0, :] = [i * gap for i in range(score.shape[1])]

    # Get Score Matrix
    for i in range(1, score.shape[0]):
        for j in range(1, score.shape[1]):
            # seq1[i-1] -> loop starts with 1 -> count at 0 for string
            diag = score[i - 1, j - 1] + match_score(seq1[i - 1], seq2[j - 1], match, mismatch)
            hori = score[i, j - 1] + gap
            vert = score[i - 1, j] + gap
            # Determine max Score
            score[i, j] = max(diag, vert, hori)

    # Backtrack the Way
    align1 = ""  # Seq1 filler
    align2 = ""  # Seq2 filler
    operations = ""

    a, b = len(seq1), len(seq2)
    while (a > 0) and (b > 0):
        # Get numbers in Box (2x2), current_loc = bottom-right
        current_score = score[a, b]
        diag = score[a - 1, b - 1]
        hori = score[a, b - 1]
        vert = score[a - 1, b]

        # Look where we came from, Check Diagonal
        if current_score == diag + match_score(seq1[a - 1], seq2[b - 1], match, mismatch):
            if seq1[a - 1] == seq2[b - 1]:
                operations += "*"
            else:
                operations += ":"
            align1 += seq1[a - 1]
            align2 += seq2[b - 1]
            a -= 1
            b -= 1
        # Check horizontal
        elif current_score == hori + gap:
            operations += "-"
            align1 += "-"
            align2 += seq2[b - 1]
            b -= 1
        # Check vertical
        elif current_score == vert + gap:
            operations += "-"
            align1 += seq1[a - 1]
            align2 += "-"
            a -= 1

    # Go to top-left-corner
    # a = ScoreMat-Row, Gaps in Seq2
    while a > 0:
        align1 += seq1[a - 1]
        align2 += "-"
        operations += "-"
        a -= 1
    # b = ScoreMat-Col, Gaps in Seq1
    while b > 0:
        align1 += "-"
        align2 += seq2[b - 1]
        operations += "-"
        b -= 1

    # Reverse both strings and operations
    align1 = align1[::-1]
    align2 = align2[::-1]
    operations = operations[::-1]

    # Output
    if show_score:
        print("Score-Matrix\n", score, "\n")
    max_length = max(len(align1), len(align2))
    print("Alignment", "".join(["=" for _ in range(max_length - 1)]))
    print("Seq1:\t", align1)
    print("Seq2:\t", align2)
    print("Align:\t", operations)

    end = time.time()
    print("Time Result {}".format(end - start))


def AlignSemiglobal(seq1, seq2, match, mismatch, gap):
    # Guarantee that seq1 > seq2 and n > m
    if len(seq1) > len(seq2):
        n, m = len(seq1), len(seq2)
        seq1, seq2 = seq1, seq2
    else:
        n, m = len(seq2), len(seq1)
        seq1, seq2 = seq2, seq1

    # Initialize Score-Mat
    score_mat = np.zeros((m+1, n+1))
    score_mat[0,:] = 0
    pass


if __name__ == "__main__":
    str1 = "ACGAGCGGAGGAG"
    str2 = "GGCGAAG"

    # str1, str2, match, mismatch, gap
    NeedlemanWunsch(str2, str1, show_score=True)
