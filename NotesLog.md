# Notes log

If, for some reason, you wanted to follow what is going on in my brain whist I'm doing this:
you're in the right place.

Welcome :wave: (but also commiserations)

## Do the dumb thing 1st

I reckon we'll be going through low-hundreds of numbers.
So we're talking ~1e5 pairs and ~1e7 triplets.
In the grand scheme of things thats not _too_ much work
and I reckon we'll be through the triplets in well sub-second.

So lets do the dumb thing 1st and not worry about performance
for now

> Premature optimization is the root of all evil

and all that.

## Should we support `floats` ?

All the examples are integers. Theoretically we could support `floats` too.
Though we might run into some weird `float` "equality" bugs.

## should we support multiple matches

Again all the examples seem to have a single match.
But I think we should support multiple matches,
there will be a bit of a perf downside in the case of a
single match because we won't do an early return.

But we're not going for performance yet.

So

the floating point thing finally hit us for `sqrt(2)`, in hindsight
maybe pi and e are inlined somehow like smaller ints.

I've got around it by changing the comparison, but its going to
be slower

## performance

eugh that it pretty bad ~0.4 for the triplets version

```sh
$ make benchmark
tests/performance_check.py ..                                                                                                                                [100%]

------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_input1_pairs          5.4665 (1.0)        6.2297 (1.0)        5.6687 (1.0)      0.1018 (1.0)        5.6575 (1.0)      0.1289 (1.0)          47;3  176.4077 (1.0)         172           1
test_input1_triplets     384.6154 (70.36)    386.5000 (62.04)    385.4776 (68.00)    0.8287 (8.14)     385.4333 (68.13)    1.5047 (11.67)         2;0    2.5942 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## if you want to go faster

We're going to have to break apart the itertools into the underlying nested loops
before we can mess with the aglo.

but 1st lets split out the float-y bits of the tests, because i think we might want to
make it easier to stop supporting floats and lose those tests.

wow, even just replacing the `math.isclose` in favor of simple `==`
gets us a ~30% speed up on the (`int` only) benchmarks.

```sh
$ make benchmark
tests/performance_check.py ..                                                                                                      [100%]

------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_input1_pairs          2.8727 (1.0)        4.2386 (1.0)        3.1265 (1.0)      0.1638 (1.0)        3.1067 (1.0)      0.1888 (1.0)          78;9  319.8414 (1.0)         326           1
test_input1_triplets     211.6325 (73.67)    213.3950 (50.35)    212.4042 (67.94)    0.6555 (4.00)     212.2717 (68.33)    0.8081 (4.28)          2;0    4.7080 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
=========================================================== 2 passed in 3.59s ============================================================
```

but this does make some of our floaty tests fail.

## simple nested loops for pairwise

looks like we're seeing an perf improvement over itertools just by breaking out into loops for the pairs
roughly the same speedup we got by dropping float support, but we're back using `math.isclose`

```sh
tests/performance_check.py ..                                                                                                                                                     [100%]

------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_input1_pairs          3.0859 (1.0)        6.3263 (1.0)        3.4614 (1.0)      0.2696 (1.0)        3.4232 (1.0)      0.2591 (1.0)          44;6  288.8998 (1.0)         298           1
test_input1_triplets     392.5019 (127.19)   394.4756 (62.36)    393.5971 (113.71)   0.8023 (2.98)     393.7625 (115.03)   1.2974 (5.01)          2;0    2.5407 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
=================================================================================== 2 passed in 4.87s ===================================================================================
```

and now we've moved the triplets to nested loops too

```sh
tests/performance_check.py ..                                                                                                                                                                                              [100%]


------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in ms)             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_input1_pairs          4.6867 (1.0)        9.1275 (1.0)        5.5921 (1.0)      0.8257 (1.0)        5.3198 (1.0)      0.8444 (1.0)         23;12  178.8246 (1.0)         193           1
test_input1_triplets     371.6804 (79.31)    376.8461 (41.29)    374.2332 (66.92)    2.3729 (2.87)     373.5280 (70.21)    4.3788 (5.19)          3;0    2.6721 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
======================================================================================================= 2 passed in 4.81s ========================================================================================================
```