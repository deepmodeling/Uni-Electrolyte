from functools import partial
from dataclasses import asdict as _asdict
from datetime import date, datetime
from enum import Enum


def launching_factory(for_orm_update, obj):
    res = {}
    for k, v in obj:
        if for_orm_update and k == "updated_at":
            v = datetime.now().isoformat()
        elif isinstance(v, datetime):
            v = v.isoformat()
        elif isinstance(v, date):
            v = v.isoformat()
        elif isinstance(v, Enum):
            v = v.value
        res[k] = v
    return res


def asdict(obj, dict_factory=launching_factory, for_orm_update=True):
    return _asdict(obj, dict_factory=partial(dict_factory, for_orm_update))
