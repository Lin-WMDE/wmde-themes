#!/usr/bin/env python3
"""Draw the frames of the WMDE boot splash spinner.

The spinner is the Windows boot one: five white dots chasing each other round a circle,
slow at the top, fast at the bottom. Plymouth's two-step module plays
throbber-0001.png .. throbber-NNNN.png in a loop, so this writes those, next to itself in
wmde/. The frames are committed; the package build does not run this.

    python3 render.py

The logo, bgrt-fallback.png, is rendered from the settings app's WMDE logo:

    rsvg-convert -w 160 -h 160 ../../wmde-settings/resources/wmde-logo.svg -o wmde/bgrt-fallback.png
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw

SIZE = 40  # frame side, px
RADIUS = 15.0  # circle the dots run along, px from the centre
DOT = 2.2  # dot radius, px
DOTS = 5
LAG = 0.06  # how far each dot trails the one ahead, in loop fractions
FRAMES = 60
SUPERSAMPLE = 8

OUT = Path(__file__).resolve().parent / "wmde"


def travel(t: float) -> float:
    """Fraction of the circle covered at loop time t: slow at the top, fast at the bottom."""
    return t - math.sin(2 * math.pi * t) / (2 * math.pi) * 0.85


def frame(index: int) -> Image.Image:
    side = SIZE * SUPERSAMPLE
    image = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    centre = side / 2
    t = index / FRAMES
    for dot in range(DOTS):
        # Start at twelve o'clock and run clockwise.
        angle = 2 * math.pi * travel((t - dot * LAG) % 1.0) - math.pi / 2
        x = centre + RADIUS * SUPERSAMPLE * math.cos(angle)
        y = centre + RADIUS * SUPERSAMPLE * math.sin(angle)
        r = DOT * SUPERSAMPLE
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, 255))
    return image.resize((SIZE, SIZE), Image.LANCZOS)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("throbber-*.png"):
        old.unlink()
    for index in range(FRAMES):
        frame(index).save(OUT / f"throbber-{index + 1:04d}.png", optimize=True)


if __name__ == "__main__":
    main()
