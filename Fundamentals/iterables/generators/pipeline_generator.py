##################################################################
# GENERATOR => FUNCTION WITH AT LEAST ONE 'YIELD' STATEMENT !    #
##################################################################

from take_generator import take

from distinct_generator import distinct


def pipeline(iterable):
    """Start the pipeline

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'.
    """
    for item in iterable:
        yield item


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__  == '__main__':
    run_pipeline()