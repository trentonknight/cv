#!/usr/bin/env python3
import math
import random
from pathlib import Path

WIDTH = 1200
HEIGHT = 1600
GRID_W = 180
GRID_H = 240
LEVELS = 34
INDEX_EVERY = 5

PINE = "#1b4332"
HUNTER = "#c85a17"


def hash2(ix: int, iy: int, seed: int) -> float:
    n = ix * 374761393 + iy * 668265263 + seed * 1442695041
    n = (n ^ (n >> 13)) * 1274126177
    return ((n ^ (n >> 16)) & 0xFFFFFFFF) / 0xFFFFFFFF


def smoothstep(t: float) -> float:
    return t * t * (3.0 - 2.0 * t)


def value_noise(x: float, y: float, seed: int) -> float:
    ix = math.floor(x)
    iy = math.floor(y)
    fx = smoothstep(x - ix)
    fy = smoothstep(y - iy)

    v00 = hash2(ix, iy, seed)
    v10 = hash2(ix + 1, iy, seed)
    v01 = hash2(ix, iy + 1, seed)
    v11 = hash2(ix + 1, iy + 1, seed)

    nx0 = v00 + (v10 - v00) * fx
    nx1 = v01 + (v11 - v01) * fx
    return nx0 + (nx1 - nx0) * fy


def fbm(nx: float, ny: float, seed: int) -> float:
    """Multi-octave terrain field with directional ridge tilt."""
    amp = 1.0
    freq = 2.4
    total = 0.0
    norm = 0.0
    for octave in range(4):
        n = value_noise(nx * freq, ny * freq, seed + octave * 97)
        # Fold noise slightly to create sharper ridge crests & valleys
        ridge = 1.0 - abs(2.0 * n - 1.0)
        blended = 0.65 * n + 0.35 * ridge
        total += blended * amp
        norm += amp
        amp *= 0.5
        freq *= 2.05

    # Gentle diagonal terrain gradient across the sheet
    slope = 0.22 * nx - 0.14 * ny
    return (total / norm) + slope


def lerp(a: float, b: float, t: float) -> float:
    if abs(b - a) < 1e-9:
        return a
    return a + (b - a) * max(0.0, min(1.0, t))


def marching_squares_segments(grid: list[list[float]], threshold: float) -> list[tuple[float, float, float, float]]:
    """Extract contour line segments at a single elevation threshold."""
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    sx = WIDTH / cols
    sy = HEIGHT / rows
    segments: list[tuple[float, float, float, float]] = []

    for r in range(rows):
        y0 = r * sy
        y1 = (r + 1) * sy
        for c in range(cols):
            x0 = c * sx
            x1 = (c + 1) * sx

            tl = grid[r][c]
            tr = grid[r][c + 1]
            br = grid[r + 1][c + 1]
            bl = grid[r + 1][c]

            mask = 0
            if tl >= threshold:
                mask |= 1
            if tr >= threshold:
                mask |= 2
            if br >= threshold:
                mask |= 4
            if bl >= threshold:
                mask |= 8

            if mask == 0 or mask == 15:
                continue

            top = (lerp(x0, x1, (threshold - tl) / (tr - tl)), y0)
            right = (x1, lerp(y0, y1, (threshold - tr) / (br - tr)))
            bottom = (lerp(x0, x1, (threshold - bl) / (br - bl)), y1)
            left = (x0, lerp(y0, y1, (threshold - tl) / (bl - tl)))

            case_map = {
                1: [(left, top)],
                2: [(top, right)],
                3: [(left, right)],
                4: [(right, bottom)],
                5: [(left, top), (right, bottom)],
                6: [(top, bottom)],
                7: [(left, bottom)],
                8: [(bottom, left)],
                9: [(top, bottom)],
                10: [(top, right), (bottom, left)],
                11: [(top, right)],
                12: [(left, right)],
                13: [(top, right)],
                14: [(left, top)],
            }

            for p1, p2 in case_map.get(mask, []):
                segments.append((p1[0], p1[1], p2[0], p2[1]))

    return segments


def stitch_polylines(segments: list[tuple[float, float, float, float]]) -> list[list[tuple[float, float]]]:
    """Connect adjacent segments into smooth polylines."""
    unused = list(segments)
    polylines: list[list[tuple[float, float]]] = []
    eps = 0.5

    def close(a: tuple[float, float], b: tuple[float, float]) -> bool:
        return abs(a[0] - b[0]) < eps and abs(a[1] - b[1]) < eps

    while unused:
        x1, y1, x2, y2 = unused.pop()
        line = [(round(x1, 1), round(y1, 1)), (round(x2, 1), round(y2, 1))]

        extended = True
        while extended:
            extended = False
            for i in range(len(unused) - 1, -1, -1):
                sx1, sy1, sx2, sy2 = unused[i]
                p_start = (sx1, sy1)
                p_end = (sx2, sy2)
                if close(line[-1], p_start):
                    line.append((round(sx2, 1), round(sy2, 1)))
                    unused.pop(i)
                    extended = True
                elif close(line[-1], p_end):
                    line.append((round(sx1, 1), round(sy1, 1)))
                    unused.pop(i)
                    extended = True
                elif close(line[0], p_end):
                    line.insert(0, (round(sx1, 1), round(sy1, 1)))
                    unused.pop(i)
                    extended = True
                elif close(line[0], p_start):
                    line.insert(0, (round(sx2, 1), round(sy2, 1)))
                    unused.pop(i)
                    extended = True

        if len(line) >= 3:
            polylines.append(line)

    return polylines


def build_svg(seed: int, out_file: Path) -> int:
    grid = [
        [fbm(c / GRID_W, r / GRID_H, seed) for c in range(GRID_W + 1)]
        for r in range(GRID_H + 1)
    ]

    min_v = min(min(row) for row in grid)
    max_v = max(max(row) for row in grid)
    pad = (max_v - min_v) * 0.08

    lines_out: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">',
        "  <style>",
        "    .topo-minor {",
        f"      stroke: {PINE};",
        "      stroke-opacity: 0.20;",
        "      stroke-width: 1;",
        "      stroke-linecap: round;",
        "      stroke-linejoin: round;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "    .topo-index {",
        f"      stroke: {HUNTER};",
        "      stroke-opacity: 0.28;",
        "      stroke-width: 1.5;",
        "      stroke-linecap: round;",
        "      stroke-linejoin: round;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "  </style>",
    ]

    total_paths = 0
    for idx in range(1, LEVELS):
        t = min_v + pad + ((max_v - min_v - 2 * pad) * (idx / LEVELS))
        segs = marching_squares_segments(grid, t)
        polys = stitch_polylines(segs)
        cls = "topo-index" if idx % INDEX_EVERY == 0 else "topo-minor"

        for pts in polys:
            d = "M " + " L ".join(f"{x},{y}" for x, y in pts)
            lines_out.append(f'  <path class="{cls}" d="{d}" />')
            total_paths += 1

    lines_out.append("</svg>")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    return total_paths


if __name__ == "__main__":
    seed = random.randint(1, 99999)
    target = Path(__file__).resolve().parent.parent / "assets" / "img" / "topo.svg"
    count = build_svg(seed, target)
    print(f"Seed {seed}: wrote {count} contour paths to {target}")

