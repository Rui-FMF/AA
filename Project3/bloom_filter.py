# Rui Fernandes
# Nmec: 92952
# Bloom Filter class adapted from professor's example

class BloomFilter:
    """ Bloom Filter """

    def __init__(self, m, k, hash_fun):
        """
            m, size of the vector
            k, number of hash functions to compute
            hash_fun, hash function to use
        """

        self.m = m

        # initialize the vector, i.e., the Bloom Filter
        # Despite being more apropriate to use a bitarray, could not do as such because there were dificulties in installing the bitarray library

        self.vector = [0] * m

        self.k = k

        self.hash_fun = hash_fun

        self.false_positive = 0     # for testing

    def insert(self, key):
        """ insert the key """

        for i in range(self.k):

            self.vector[self.hash_fun((key+str(i)).encode()) % self.m] = 1

    def check(self, key):
        """ check if key is contained """

        for i in range(self.k):

            if self.vector[self.hash_fun((key+str(i)).encode()) % self.m] == 0:

                return False    # the key doesn't exist

        return True             # the key can be in the data set

def main(args):

    return 0


if __name__ == '__main__':

    import sys
    sys.exit(main(sys.argv))
