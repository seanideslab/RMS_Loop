"""Small standard-library PNG plotting helpers for artifact figures.

The artifact intentionally avoids requiring a scientific plotting stack for the
baseline reviewer path. These helpers produce deterministic, lightweight PNG
charts using only the Python standard library.
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

Color = tuple[int, int, int]

WHITE: Color = (255, 255, 255)
BLACK: Color = (20, 20, 20)
BLUE: Color = (46, 114, 182)
ORANGE: Color = (221, 132, 82)
GREEN: Color = (85, 168, 104)
GRAY: Color = (190, 190, 190)


def _chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def _write_png(path: str, pixels: list[list[Color]]) -> None:
    height = len(pixels)
    width = len(pixels[0]) if height else 0
    raw = b"".join(b"\x00" + b"".join(bytes(px) for px in row) for row in pixels)
    png = b"\x89PNG\r\n\x1a\n"
    png += _chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    png += _chunk(b"IDAT", zlib.compress(raw, 9))
    png += _chunk(b"IEND", b"")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(png)


def _canvas(width: int, height: int, color: Color = WHITE) -> list[list[Color]]:
    return [[color for _ in range(width)] for _ in range(height)]


def _set_px(img: list[list[Color]], x: int, y: int, color: Color) -> None:
    if 0 <= y < len(img) and 0 <= x < len(img[0]):
        img[y][x] = color


def _line(img: list[list[Color]], x0: int, y0: int, x1: int, y1: int, color: Color = BLACK) -> None:
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        _set_px(img, x0, y0, color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def _rect(img: list[list[Color]], x0: int, y0: int, x1: int, y1: int, color: Color) -> None:
    for y in range(max(0, y0), min(len(img), y1 + 1)):
        for x in range(max(0, x0), min(len(img[0]), x1 + 1)):
            img[y][x] = color


def _axes(img: list[list[Color]], margin: int = 38) -> None:
    width, height = len(img[0]), len(img)
    _line(img, margin, height - margin, width - margin, height - margin, BLACK)
    _line(img, margin, margin, margin, height - margin, BLACK)
    for i in range(5):
        y = margin + i * (height - 2 * margin) // 4
        _line(img, margin - 3, y, margin + 3, y, GRAY)
        _line(img, margin, y, width - margin, y, (235, 235, 235))


def scatter(path: str, xs: list[float], ys: list[float], width: int = 640, height: int = 400) -> None:
    img = _canvas(width, height)
    margin = 42
    _axes(img, margin)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    for x, y in zip(xs, ys):
        px = margin + int((x - min_x) / max(max_x - min_x, 1e-9) * (width - 2 * margin))
        py = height - margin - int((y - min_y) / max(max_y - min_y, 1e-9) * (height - 2 * margin))
        _rect(img, px - 4, py - 4, px + 4, py + 4, BLUE)
    _write_png(path, img)


def bars(path: str, values: list[float], width: int = 640, height: int = 400) -> None:
    img = _canvas(width, height)
    margin = 42
    _axes(img, margin)
    max_v = max(values) if values else 1
    slot = (width - 2 * margin) / max(len(values), 1)
    for i, value in enumerate(values):
        x0 = int(margin + i * slot + slot * 0.2)
        x1 = int(margin + (i + 1) * slot - slot * 0.2)
        y0 = height - margin - int(value / max(max_v, 1e-9) * (height - 2 * margin))
        _rect(img, x0, y0, x1, height - margin - 1, ORANGE if i % 2 else GREEN)
    _write_png(path, img)


def line(path: str, values: list[float], width: int = 640, height: int = 400) -> None:
    img = _canvas(width, height)
    margin = 42
    _axes(img, margin)
    if len(values) < 2:
        _write_png(path, img)
        return
    min_v, max_v = min(values), max(values)
    points=[]
    for i, value in enumerate(values):
        x = margin + int(i / (len(values) - 1) * (width - 2 * margin))
        y = height - margin - int((value - min_v) / max(max_v - min_v, 1e-9) * (height - 2 * margin))
        points.append((x, y))
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        _line(img, x0, y0, x1, y1, BLUE)
    for x, y in points:
        _rect(img, x - 3, y - 3, x + 3, y + 3, BLUE)
    _write_png(path, img)
