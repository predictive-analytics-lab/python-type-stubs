# pyright: strict

from typing import Optional

from PIL.Image import Image

def add(image1: Image, image2: Image, scale: float = ..., offset: float = ...) -> Image: ...

def add_modulo(image1: Image, image2: Image) -> Image: ...

def blend(image1: Image, image2: Image, alpha: float) -> Image: ...

def composite(image1: Image, image2: Image, mask: Image) -> Image: ...

def constant(image: Image, value: int) -> Image: ...

def darker(image1: Image, image2: Image) -> Image: ...

def difference(image1: Image, image2: Image) -> Image: ...

def duplicate(image: Image) -> Image: ...

def invert(image: Image) -> Image: ...

def lighter(image1: Image, image2: Image) -> Image: ...

def logical_and(image1: Image, image2: Image) -> Image: ...

def logical_or(image1: Image, image2: Image) -> Image: ...

def logical_xor(image1: Image, image2: Image) -> Image: ...

def multiply(image1: Image, image2: Image) -> Image: ...

def offset(image: Image, xoffset: int, yoffset: Optional[int]) -> Image: ...

def screen(image1: Image, image2: Image) -> Image: ...

def subtract(image1: Image, image2: Image, scale: float = ..., offset: float = ...) -> Image: ...

def subtract_modulo(image1: Image, image2: Image) -> Image: ...
