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
