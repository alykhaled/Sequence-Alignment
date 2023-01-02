import argparse
from localalign import localAllignment
from globalalign import globalAllignment

def cli():
    parser = argparse.ArgumentParser(
                        prog = 'Sequence Alignment',
                        description = 'Global/Local Align two sequences according to match,mismatch and gap scores',
                        epilog = 'Thanks')

    parser.add_argument('seq1')
    parser.add_argument('seq2')
    parser.add_argument('match')
    parser.add_argument('mismatch')
    parser.add_argument('gap')
    parser.add_argument('-l', '--local', action='store_true')

    args = parser.parse_args()
    seq1, seq2, match, mismatch, gap, local = args.seq1, args.seq2, int(args.match), int(args.mismatch), int(args.gap), args.local
    print("Sequence 1: ", seq1)
    print("Sequence 2: ", seq2)
    print("Match: ", match)
    print("Mismatch: ", mismatch)
    print("Gap: ", gap)

    # seq1 = "CTATTGACGTA"
    # seq2 = "CTATGAAA"
    # match = 5
    # mismatch = -2
    # gap = -4
    # local = False

    if local:
        print("Local Alignment")
        alignedSeq1, alignedSeq2 = localAllignment(match,mismatch,gap,seq1,seq2)
        print(alignedSeq1)
        print(alignedSeq2)
    else:
        print("Global Alignment")
        alignedSeq1, alignedSeq2 = globalAllignment(match,mismatch,gap,seq1,seq2)
        print(alignedSeq1)
        print(alignedSeq2)

