
# Laziness and Infinite

    # Just in Time Computation

    # Infinite (or large) sequences
        # sensor readings
        # mathematical series
        # massive files



# Free tools
from itertools import islice, count

# Check is_prime function
from utils import is_prime

# Creating a sequence with the first 1000 prime numbers with islice(), count() & is_prime()
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

# Print all the numbers on the console with single input, because it's generator
print(list(thousand_primes))

# Print the sum of all numbers
print(sum(list(thousand_primes)))