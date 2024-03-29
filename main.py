from Brute_Force import Brute_Force
from LCS import Compute_LCS
from itertools import combinations
import random
import time
import sys

if __name__ == "__main__":

    # How to run: Run py main.py X Y where X is the number of sequences and Y is the length of each sequence to be generated.

    # X
    NumberOfSequences = int(sys.argv[1])
    # Y
    LengthOfSequences = int(sys.argv[2])

    pool = ["A", "C", "G", "T"]  # pool of letters

    dna = list()  # generate random sequences
    for x in range(NumberOfSequences):
        sequence = str()
        for y in range(LengthOfSequences):
            random_index = random.randint(0, len(pool) - 1)
            sequence = "".join([sequence, pool[random_index]])
        dna.append(sequence)

    print("\nDNA Sequences are : ")  # final random sequences
    print("-------------------")
    print(*dna, sep='\n')

    start1 = time.time()
    comb = combinations(dna, 2)  # get all possible combinations between sequences

    final_sequence_brute = list()
    final_length_brute = 0

    for a, b in comb:  # perform brute force on generated sequences and get the common sequences with max length
        sequence_found_brute = Brute_Force(a, b)
        sequence_found_brute = sequence_found_brute[::-1]
        sequence_length_brute = len(sequence_found_brute)

        if sequence_length_brute > final_length_brute:
            final_sequence_brute = list()
            final_sequence_brute.append(("sequence a is: " + str(a), "sequence b is: " + str(b),
                                         "common sequence found is: " + str(sequence_found_brute),
                                         "length is : " + str(sequence_length_brute)))
            final_length_brute = sequence_length_brute

        elif sequence_length_brute == final_length_brute:
            final_sequence_brute.append(("sequence a is: " + str(a), "sequence b is: " + str(b),
                                         "common sequence found is: " + str(sequence_found_brute),
                                         "length is : " + str(sequence_length_brute)))

    print('\n')

    print("Brute Force : ")
    print("-------------")
    print(*final_sequence_brute, sep='\n')
    end1 = time.time()

    start = time.time()
    final_sequence_lcs = list()
    final_length_lcs = 0
    comb = combinations(dna, 2)

    for a, b in comb:
        sequence_length_lcs, sequence_found_lcs = Compute_LCS(a, b)

        if sequence_length_lcs > final_length_lcs:
            final_sequence_lcs = list()
            final_sequence_lcs.append(("sequence a is: " + str(a), "sequence b is: " + str(b),
                                       "common sequence found is: " + str(sequence_found_lcs),
                                       "length is : " + str(sequence_length_lcs)))
            final_length_lcs = sequence_length_lcs

        elif sequence_length_lcs == final_length_lcs:
            final_sequence_lcs.append(("sequence a is: " + str(a), "sequence b is: " + str(b),
                                       "common sequence found is: " + str(sequence_found_lcs),
                                       "length is : " + str(sequence_length_lcs)))

    print('\n')

    print("LCS : ")
    print("-----")
    print(*final_sequence_lcs, sep='\n')

    end = time.time()

    print('\n')

    print("Time spent for Brute Force method : ", end="")
    print(round(end1 - start1, 2))
    print("---------------------------------------")
    print('\n')
    print("Time spent for LCS method : ", end="")
    print(round(end - start, 2))
    print("-------------------------------")
