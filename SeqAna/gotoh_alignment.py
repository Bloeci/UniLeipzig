import numpy as np
from dataclasses import dataclass


@dataclass
class Scores:
    """
    Define all Scores for the Gotoh-Algorithm
    """
    match: float = 1
    mismatch: float = -1
    gap_opening: float = -1.5
    gap_extension: float = -0.3


class AlgorithmenMatrix:
    """
    Create different matrix
    Parameter:
    seq1 : String - First Sequence
    seq2 : String - Second Sequence
    matType: String - L/R/M = Left (gap in row), Right (gap in col), Main (gap in row & col)
    """
    def __init__(self, seq1, seq2, matType):
        self.row = len(seq1)
        self.col = len(seq2)
        self.seq1 = seq1
        self.seq2 = seq2
        self.matType = matType
        self.mat = np.zeros((self.row+1, self.col+1))

    def createMatrix(self):
        if self.matType == "L":
            self.mat[1:, 0] = [(Scores.gap_opening + i * Scores.gap_extension) for i in range(self.row)]
        if self.matType == "R":
            self.mat[0, 1:] = [(Scores.gap_opening + i * Scores.gap_extension) for i in range(self.col)]
        if self.matType == "M":
            self.mat[1:, 0] = [(Scores.gap_opening + i * Scores.gap_extension) for i in range(self.row)]
            self.mat[0, 1:] = [(Scores.gap_opening + i * Scores.gap_extension) for i in range(self.col)]

    def printMat(self):
        print(self.mat)
        return True


def matchScore(charA, charB):
    if charA == charB:
        return Scores.match
    else:
        return Scores.mismatch


def GotohAlignment(L, R, M):
    for n in range(1, M.row+1):
        for m in range(1, M.col+1):
            L.mat[n, m] = max(M.mat[n, m-1] + Scores.gap_opening, L.mat[n, m-1] + Scores.gap_extension)
            R.mat[n, m] = max(M.mat[n-1, m] + Scores.gap_opening, R.mat[n-1, m] + Scores.gap_extension)
            M.mat[n, m] = max(M.mat[n-1, m-1] + matchScore(M.seq1[n-1], M.seq2[m-1]), L.mat[n, m], R.mat[n, m])


def BacktrackMain(n, m, L, R, M, align1, align2):
    if n == 0:
        while m > 0:
            align1 = align1 + "-"
            align2 = align2 + M.seq2[m-1]
            m = m-1

    if m == 0:
        while n > 0:
            align1 = align1 + M.seq1[n-1]
            align2 = align2 + "-"
            n = n-1

    if n == 0 or m == 0:
        print(align1[::-1])
        print(align2[::-1])
        return True

    # Cases
    elif M.mat[n, m] == (M.mat[n-1, m-1] + matchScore(M.seq1[n-1], M.seq2[m-1])):
        align1 = align1 + M.seq1[n-1]
        align2 = align2 + M.seq2[m-1]
        BacktrackMain(n-1, m-1, L, R, M, align1, align2)

    elif M.mat[n, m] == R.mat[n, m]:
        BacktrackRight(n, m, L, R, M, align1, align2)

    elif M.mat[n, m] == L.mat[n, m]:
        BacktrackLeft(n, m, L, R, M, align1, align2)


def BacktrackLeft(n, m, L, R, M, align1, align2):
    if m == 0:
        BacktrackMain(n, m, L, R, M, align1, align2)

    align1 = align1 + "-"
    align2 = align2 + M.seq2[m-1]

    if L.mat[n, m] == (L.mat[n, m-1] + Scores.gap_extension):
        BacktrackLeft(n, m-1, L, R, M, align1, align2)
    elif L.mat[n, m] == (M.mat[n, m-1] + Scores.gap_opening):
        BacktrackMain(n, m-1, L, R, M, align1, align2)


def BacktrackRight(n, m, L, R, M, align1, align2):
    if n == 0:
        BacktrackMain(n, m, L, R, M, align1, align2)

    align1 = align1 + M.seq1[n-1]
    align2 = align2 + "-"

    if R.mat[n, m] == (R.mat[n-1, m] + Scores.gap_extension):
        BacktrackRight(n-1, m, L, R, M, align1, align2)
    elif R.mat[n, m] == (M.mat[n-1, m] + Scores.gap_opening):
        BacktrackMain(n-1, m, L, R, M, align1, align2)


def main():
    seq1, seq2 = ["ABCABCABCCCCGACGTTGAGCTCTC", "CTTTTCACCCTT"]

    L = AlgorithmenMatrix(seq1, seq2, 'L')
    R = AlgorithmenMatrix(seq1, seq2, 'R')
    M = AlgorithmenMatrix(seq1, seq2, 'M')
    L.createMatrix()
    R.createMatrix()
    M.createMatrix()

    # Algorithm for matrix calculations
    GotohAlignment(L, R, M)

    # Backtrack
    BacktrackMain(M.row, M.col, L, R, M, "", "")


if __name__ == "__main__":
    main()
