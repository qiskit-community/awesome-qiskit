"""Awesome list generator entrypoint.

Example of CLI usage:
```
python manager.py generate_readme
```
"""

import fire

from awesome_qiskit.manager import Manager


if __name__ == "__main__":
    fire.Fire(Manager)
