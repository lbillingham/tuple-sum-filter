"""
Central place to keep type-hints for this project.
We imagine that you'll be doing things like

```python
import {{package}}.types as t

def read_file(fname: t.Path)
```

We consider typing as optional and gradual.
If its not helping you or consumers of your API,
you may not want to add types to it

N.B. we are stuck with `Union[spam, ham]` rather that `spam | ham`
until we only support python>=3.10
"""
import typing as typ

Int = int
List = typ.List
Num = typ.Union[int, float]
PairsOfNums = typ.List[typ.Tuple[Num, Num]]
Sequence = typ.Sequence
