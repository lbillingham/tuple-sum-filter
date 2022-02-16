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