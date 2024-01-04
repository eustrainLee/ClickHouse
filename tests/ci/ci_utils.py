#!/usr/bin/env python3


class WithIter(type):
    def __iter__(cls):
        return (v for k, v in cls.__dict__.items() if not k.startswith("_"))
