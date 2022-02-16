# Tuple Sum Filter

A library to play with filtering numeric sequences by sums of their pairs, triplets, etc.

Comes with a bonus CLI to demo the functionality

## Developing

Run the following to install the project (and dev dependencies) into your active virtualenv:

```bash
make dev_install
```

day-to-day development tasks can be orchestrated via `make`

- dependency management
- test/lint/typecheck running
- coverage reporting
- run `make` without any arguments to see a list

There is a CI suite which runs lint and test on several python versions.
We don't run typechecking as a gate in CI because we think that
turns a sometimes-useful tool into a [Goodhart target](https://en.wikipedia.org/wiki/Goodhart%27s_law).

--

:cookie: :scissors: cookiecut from lbillingham's python-cli-template
