from typing import Dict, Any, Union, List, Tuple
from .doc import Doc
from .span import Span
from .token import Token

class Retokenizer:
    def __init__(self, doc: Doc) -> None: ...
    def merge(self, span: Span, attrs: Dict[Union[str, int], Any] = ...) -> None: ...
    def split(
        self,
        token: Token,
        orths: List[str],
        heads: List[Union[Token, Tuple[Token, int]]],
        attrs: Dict[Union[str, int], List[Any]] = ...,
    ) -> None: ...
    def __enter__(self) -> Retokenizer: ...
    def __exit__(self, *args: Any) -> None: ...
