"""
This is an example job that uses RDD to calculate pi.

This the just the python version of
https://github.com/apache/spark/blob/master/examples/src/main/scala/org/apache/spark/examples/SparkPi.scala
"""
import logging
import random

from pyspark import SparkContext


def pi_trial() -> int:
    # Center the circle
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    return 1 if (x ** 2 + y ** 2) <= 1 else 0


def main() -> None:
    logging.info("Starting pi caculation")
    spark = SparkContext.getOrCreate()

    slices = 32 * 32  # 32 slices and 32 tasks per slice
    work_per_slice = 100_000

    rdd = spark.parallelize(range(work_per_slice * slices), slices)
    trials = rdd.map(lambda x: pi_trial())

    pi = trials.sum() / (work_per_slice * slices) * 4

    logging.info(f"pi is estimated to be: {pi!r}")


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] %(asctime)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=logging.INFO,
    )
    main()
