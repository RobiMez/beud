
from typing import List
import inspect , sys
from .colors import P,C
p = P()
c = C()


class exporter:
    def __init__(self, sysmods) -> None:
        # export our functions and handlers
        self.handlerfunctions = [
            obj for name, obj in sysmods
            if (inspect.isfunction(obj) and
                name.endswith('hlr'))]
        # dunder handlers holds our handlers
        self.__handlers__ = []
        for hfunc in self.handlerfunctions:
            p = P
            c = C
            p.o(c.green, (f"{c.green}Registering handler : {hfunc.__name__}\n{c.blue}Type : {c.bold}{hfunc.hlr.__class__.__name__}"))

            self.__handlers__.append(hfunc.hlr)
    def export(self) -> List:
        return self.__handlers__
