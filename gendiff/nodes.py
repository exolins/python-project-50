# nodes.#nodes.
from collections import namedtuple
from enum import IntEnum

class NodeStatus(IntEnum):
    same = 1
    new = 2
    removed = 3
    updated = 4

Node = namedtuple("Node", ("key": str(), "status": NodeStatus, "old_value"))
# Node = namedtuple("Node", ("key", "marker", "old_value", "new_value"))
Branch = namedtuple("Branch", ("key", "marker", "childrens"))
