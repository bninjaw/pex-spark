pex_binary(
    entry_point="job.py",
    dependencies=[
        ":pyspark",
        ":lib",
    ],
)

python_sources(name="lib")

python_requirement(
    name="pyspark",
    requirements=[
        "pyspark==3.0.1",
    ],
)
