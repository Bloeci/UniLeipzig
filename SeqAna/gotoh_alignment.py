import numpy as np
import sys
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


class GotohAlgorithm:
    """
    Perform the Gotoh-Algorithm for 2 Sequences to align both
    (high cost for gap opening, small for extension)
    ---------------------------------------------------------
    Parameter:
    seq1 : String - First Sequence
    seq2 : String - Second Sequence
    Output:
        ...
    """
    def __init__(self, seq1, seq2, score=False):
        self.seq1 = seq1
        self.seq2 = seq2
        self.row = len(seq1)
        self.col = len(seq2)
        self.choice_score = score

        self.gap_op = Scores.gap_opening
        self.gap_ex = Scores.gap_extension

        # Create all 3 Matrices
        mat_main = np.zeros((self.row+1, self.col+1))
        mat_main[1:, 0] = [(self.gap_op + self.gap_ex * i) for i in range(self.row)]
        mat_main[0, 1:] = [(self.gap_op + self.gap_ex * i) for i in range(self.col)]
        self.mat_main = mat_main

        # Gaps costs in first ROW
        mat_left = np.zeros((self.row+1, self.col+1))
        mat_left[1:, 0] = [(self.gap_op + self.gap_ex * i) for i in range(self.row)]
        self.mat_left = mat_left

        # Gaps costs in first Column
        mat_right = np.zeros((self.row+1, self.col+1))
        mat_right[0, 1:] = [(self.gap_op + self.gap_ex * i) for i in range(self.col)]
        self.mat_right = mat_right

    @staticmethod
    def MatchCase(x, y):
        return Scores.match if (x == y) else Scores.mismatch

    # Calculate Scores for "Right" Matrix (gap cost in Row)
    def ScoreRight(self, n, m):
        A = self.mat_main[n-1, m] + self.gap_op
        R = self.mat_right[n-1, m] + self.gap_ex
        return max(A, R)

    # Calculate Scores for "Left" Matrix (gap extension in Column)
    def ScoreLeft(self, n, m):
        A = self.mat_main[n, m-1] + self.gap_op
        L = self.mat_left[n, m-1] + self.gap_ex
        return max(A, L)

    # Calculate Scores for "Main" Matrix (gap extension in row and col)
    def ScoreMain(self, n, m):
        A = self.mat_main[n-1, m-1] + self.MatchCase(self.seq1[n-1], self.seq2[m-1])
        return max(A, self.mat_left[n, m], self.mat_right[n, m])

    def CalculateScoreMat(self):
        for m in range(1, self.col+1):
            for n in range(1, self.row+1):
                self.mat_right[n, m] = self.ScoreRight(n, m)
                self.mat_left[n, m] = self.ScoreLeft(n, m)
                self.mat_main[n, m] = self.ScoreMain(n, m)

        if self.choice_score:
            self.PrintMat(self.mat_main, "Main Matrix")
            self.PrintMat(self.mat_left, "Left Matrix")
            self.PrintMat(self.mat_right, "Right Matrix")

        max_score = max(self.mat_main[-1, -1], self.mat_left[-1, -1], self.mat_right[-1, -1])
        print("Best Score:\t", round(max_score, 2))

    def PrintMat(self, mat, name):
        # Needs an np.array as input
        print("Score " + name)
        n_str1 = "-" + self.seq1
        print("\t -\t", "\t ".join([i for i in self.seq2]))
        for n in range(self.row+1):
            out = ""
            out += n_str1[n] + "\t"
            for m in range(self.col+1):
                if mat[n, m] >= 0:
                    out += " "
                out += str(round(mat[n, m], 2)) + "\t"
            print(out)
        print(60*"=")

    def MatTraceback(self):
        pass


if __name__ == "__main__":
    if len(sys.argv) > 2:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
    else:
        # Example Strings
        str1 = "ACCC"
        str2 = "AGCTCTC"

    try:
        opt = sys.argv[-1]
        if (opt == "-s") or (opt == "--score"):
            opt = True
    except IndexError:
        opt = False

    alignment = GotohAlgorithm(str1, str2, opt)
    alignment.CalculateScoreMat()
