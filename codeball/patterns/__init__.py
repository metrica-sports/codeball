from typing import Optional, List, Dict
from codeball.models import PatternEvent

class Pattern(object):
    def __init__(
        self, 
        name: str = None, 
        code: str = None, 
        events: list = [], 
        in_time: int = 0, 
        out_time: int = 0
    ):
    
        self.name = name
        self.code = code
        self.events = events
        self.in_time = in_time
        self.out_time =  out_time

    def run(self):
        pass