# Tuple Sum Filter

A library to play with filtering numeric sequences by sums of their pairs, triplets, etc.

Comes with a bonus CLI to demo the functionality.

## Approach

We're thinking of this mostly as a library with the CLI as only for demo purposes.
Ways you can see this in the code:

- logging should really handled by the consumer,
  - our `get_logger` should be something that is passed into the lib
- the CLI is pretty light on automated tests
- we use pretty loose production dependency pinning
  - rather than `pip freeze > requirements.txt` of a deployed app
  - we want to keep things loose so that consumers can keep installing us alongside other things
  - we should probably set up `tox`/`nox` test runs against v.latest of our dependencies

## Running the demo

in a fresh virtualenv

```sh
# install project and deps
pip install git+https://github.com/lbillingham/tuple-sum-filter.git

# create a suitable input file
echo "1721\n979\n366\n299\n675\n1456\n" > example.txt

# run the demo
filter_demo --input_file=example.txt --sum_target=2020 --dimension=2
```

you should see output like

```sh
checking for pairs of numbers that sum to 2020 in example.txt
Results pair (1721, 299) match: sum to 2020 and multiply to 514579
```

## Consuming the library

The main filtering functions are `pairs_that_sum_to` and `triplets_that_sum_to`.
They both have signatures `(numbers: Sequence[int|float], sum_target: int|float) -> things_that_passed_the_filter list[tuple]`.

There is also a file-reading helper `numbers_in_file` exported at the top level.


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
