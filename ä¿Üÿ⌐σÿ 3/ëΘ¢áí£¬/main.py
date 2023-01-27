from Brute_Force import Brute_Force
from LCS import LCS_sub_sequence
from itertools import combinations
import random
import time

if __name__ == "__main__":

    NumberOfSequences = 10  # number of sequences
    LengthOfSequences = 3  # length of a sequence
    pool = ["A", "C", "G", "T"]  # pool of letters

    dna = list()  # generate random sequences
    for x in range(NumberOfSequences):
        sequence = str()
        for y in range(LengthOfSequences):
            random_index = random.randint(0, len(pool) - 1)
            sequence = "".join([sequence, pool[random_index]])
        dna.append(sequence)

    print("\nDNA Sequences are:", *dna, sep='\n')  # final random sequences

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

    print("Brute Force: ", *final_sequence_brute, sep='\n')
    end1 = time.time()

    # start = time.time()
    # final_sequence_lcs = list()
    # sequence_found_lcs_length_brute = 0
    # comb = combinations(dna, 2)
    #
    # for a, b in comb:
    #     max, sequence_found_lcs = LCS_sub_sequence(a, b)
    #
    #     if max > sequence_found_lcs_length_brute:
    #         final_sequence_lcs = list()
    #         final_sequence_lcs.append((a, b, sequence_found_lcs, max))
    #         sequence_found_lcs_length_brute = max
    #
    #     elif max == sequence_found_lcs_length_brute:
    #         final_sequence_lcs.append((a, b, sequence_found_lcs, max))
    #
    # print('\n')
    #
    # print("LCS : ", *final_sequence_lcs, sep='\n')
    #
    # end = time.time()

    print("Time spent for Brute Force method : " + str(end1 - start1))
    # print("\nTime spent for LCS method : " + str(end - start))
