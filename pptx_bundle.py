"""pptx_bundle -- generated; do not edit. Bundles pptx_builder for Relevance.ai."""

# === brand.py ===
"""TAAI brand constants for pptx_builder.

This module is intentionally a flat dict-only export. The same dict will
be inlined into the Relevance.ai Python step in Plan 2; keeping it as a
plain Python literal here ensures clean copy-paste.
"""

BRAND = {
    "primary": "1A2747",
    "accents": {
        "mint":    "2EC4B6",
        "coral":   "E76F51",
        "mustard": "E9C46A",
        "sand":    "C9B79C",
        "sage":    "8AA67F",
    },
    "text": {
        "primary":   "1A2747",
        "secondary": "55617A",
        "inverse":   "FFFFFF",
    },
    "fonts": {
        "header": "Georgia",
        "body":   "Calibri",
        "mono":   "Consolas",
    },
    "sizes_pt": {
        "title":          54,
        "heading":        32,
        "body":           18,
        "footer":         10,
        "statement":      44,
        "stat":           88,
        "pillar_heading": 20,
        "section_number": 96,
    },
    "slide_dimensions_in": {
        "width":  13.333,
        "height": 7.5,
    },
    "footer": {
        "show_on": [
            "single_statement", "two_up", "pillars_3", "pillars_4",
            "process_flow", "compare_contrast", "stat_callout", "quote",
            "chart", "data_table", "stat_doughnut", "quadrant_grid",
            "callout_box", "recap",
        ],
        # title and section_divider intentionally omitted.
    },
    "severity_palette": {
        "info":     "55617A",
        "positive": "2EC4B6",
        "warning":  "E9C46A",
        "critical": "E76F51",
    },
}

# === palette.py ===
"""Layout positioning metadata.

Each layout entry holds the geometric data renderers need (margins,
column counts, etc.). Renderers in `pptx_builder.layouts.*` consume
these to position shapes.

All measurements in inches. Slide is 13.333 x 7.5 (16:9).
"""

_DEFAULT_MARGIN = {"left": 0.75, "right": 0.75, "top": 0.6, "bottom": 0.6}

PALETTE = {
    "title": {
        "margin_in": _DEFAULT_MARGIN,
        "accent_block": {"left": 0.0, "top": 0.0, "width": 0.4, "height": 7.5},
        "title_box":    {"left": 0.9, "top": 2.4, "width": 11.5, "height": 1.6},
        "promise_box":  {"left": 0.9, "top": 4.2, "width": 11.5, "height": 1.0},
        "byline_box":   {"left": 0.9, "top": 5.6, "width": 11.5, "height": 0.5},
    },
    "section_divider": {
        "margin_in": _DEFAULT_MARGIN,
        "accent_block": {"left": 0.0, "top": 0.0, "width": 13.333, "height": 1.0},
        "number_box":   {"left": 0.75, "top": 2.0, "width": 4.0, "height": 2.5},
        "title_box":    {"left": 0.75, "top": 4.8, "width": 11.5, "height": 1.4},
    },
    "single_statement": {
        "margin_in": _DEFAULT_MARGIN,
        "statement_box": {"left": 1.5, "top": 2.5, "width": 10.333, "height": 2.5},
    },
    "two_up": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "body_box":    {"left": 0.75, "top": 1.7, "width": 5.7, "height": 5.2},
        "right_box":   {"left": 6.95, "top": 1.7, "width": 5.6, "height": 5.2},
    },
    "pillars_3": {
        "margin_in": _DEFAULT_MARGIN,
        "pillar_count": 3,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "columns":     {"top": 1.9, "icon_h": 0.6, "heading_h": 0.7, "body_h": 4.0, "gap": 0.4},
    },
    "pillars_4": {
        "margin_in": _DEFAULT_MARGIN,
        "pillar_count": 4,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "columns":     {"top": 1.9, "icon_h": 0.5, "heading_h": 0.7, "body_h": 4.0, "gap": 0.3},
    },
    "process_flow": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "chain":       {"top": 2.5, "height": 2.0, "gap": 0.25, "min": 4, "max": 6},
        "detail_top":  4.8,
    },
    "compare_contrast": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "left_label":  {"left": 0.75, "top": 1.7, "width": 5.7, "height": 0.6},
        "left_body":   {"left": 0.75, "top": 2.4, "width": 5.7, "height": 4.5},
        "right_label": {"left": 6.95, "top": 1.7, "width": 5.6, "height": 0.6},
        "right_body":  {"left": 6.95, "top": 2.4, "width": 5.6, "height": 4.5},
    },
    "stat_callout": {
        "margin_in": _DEFAULT_MARGIN,
        "stat_box":    {"left": 0.75, "top": 1.5, "width": 11.833, "height": 3.0},
        "unit_box":    {"left": 0.75, "top": 4.5, "width": 11.833, "height": 0.7},
        "context_box": {"left": 0.75, "top": 5.4, "width": 11.833, "height": 1.4},
    },
    "quote": {
        "margin_in": _DEFAULT_MARGIN,
        "mark_box":        {"left": 0.75, "top": 0.8, "width": 2.0, "height": 1.5},
        "quote_box":       {"left": 0.75, "top": 2.0, "width": 11.833, "height": 3.2},
        "attribution_box": {"left": 0.75, "top": 5.4, "width": 11.833, "height": 0.7},
    },
    "chart": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "chart_box":   {"left": 0.75, "top": 1.7, "width": 11.833, "height": 4.6},
        "caption_box": {"left": 0.75, "top": 6.4, "width": 11.833, "height": 0.5},
    },
    "recap": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box":     {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "takeaways_box":   {"left": 0.75, "top": 1.7, "width": 7.5, "height": 4.5},
        "next_step_box":   {"left": 8.5, "top": 1.7, "width": 4.0, "height": 4.5},
        "signoff_box":     {"left": 0.75, "top": 6.5, "width": 11.833, "height": 0.5},
    },
    "data_table": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "table_box":   {"left": 0.75, "top": 1.7, "width": 11.833, "height": 4.8},
        "max_rows": 5,
        "max_cols": 4,
    },
    "stat_doughnut": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box":   {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "doughnut_top":  1.9,
        "doughnut_size": 3.2,
        "doughnut_count": 3,
        "label_top": 5.4,
    },
    "quadrant_grid": {
        "margin_in": _DEFAULT_MARGIN,
        "heading_box": {"left": 0.75, "top": 0.6, "width": 11.833, "height": 0.9},
        "grid_left": 1.5, "grid_top": 1.9,
        "cell_width": 5.0, "cell_height": 2.4, "cell_gap": 0.3,
    },
    "callout_box": {
        "margin_in": _DEFAULT_MARGIN,
        "container":   {"left": 1.0, "top": 1.8, "width": 11.333, "height": 4.5},
        "heading_box": {"left": 1.4, "top": 2.0, "width": 10.5, "height": 0.8},
        "body_box":    {"left": 1.4, "top": 3.0, "width": 10.5, "height": 3.0},
    },
}

# === helpers.py ===
"""Shared utilities for layout renderers."""

from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


def hex_to_rgb(hex_str):
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def resolve_colour(brand, accent, role):
    """Map a role name to a hex string using brand + accent name.

    Roles:
      accent           -> brand.accents[accent]
      primary          -> brand.primary
      inverse          -> brand.text.inverse
      text_primary     -> brand.text.primary
      text_secondary   -> brand.text.secondary
    """
    if role == "accent":
        return brand["accents"][accent]
    if role == "primary":
        return brand["primary"]
    if role == "inverse":
        return brand["text"]["inverse"]
    if role.startswith("text_"):
        return brand["text"][role[len("text_"):]]
    if role in brand["text"]:
        return brand["text"][role]
    raise ValueError(f"Unknown colour role: {role!r}")


def resolve_severity_colour(brand, severity):
    return brand["severity_palette"][severity]


def add_text_box(
    slide,
    left_in, top_in, width_in, height_in,
    text,
    font_family,
    size_pt,
    colour_hex,
    align=None,
    anchor="top",
    bold=False,
):
    tb = slide.shapes.add_textbox(
        Inches(left_in), Inches(top_in),
        Inches(width_in), Inches(height_in),
    )
    tf = tb.text_frame
    tf.word_wrap = True
    if anchor == "middle":
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    elif anchor == "bottom":
        tf.vertical_anchor = MSO_ANCHOR.BOTTOM
    else:
        tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.text = text or ""
    if align == "center":
        p.alignment = PP_ALIGN.CENTER
    elif align == "right":
        p.alignment = PP_ALIGN.RIGHT
    else:
        p.alignment = PP_ALIGN.LEFT
    if p.runs:
        run = p.runs[0]
        run.font.name = font_family
        run.font.size = Pt(size_pt)
        run.font.color.rgb = hex_to_rgb(colour_hex)
        run.font.bold = bold
    return tb


def add_filled_rect(slide, left_in, top_in, width_in, height_in, fill_hex, line=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left_in), Inches(top_in),
        Inches(width_in), Inches(height_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    if not line:
        shape.line.fill.background()
    return shape


def add_rounded_rect(slide, left_in, top_in, width_in, height_in, fill_hex, line=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left_in), Inches(top_in),
        Inches(width_in), Inches(height_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    if not line:
        shape.line.fill.background()
    return shape


def add_oval(slide, left_in, top_in, width_in, height_in, fill_hex, line=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(left_in), Inches(top_in),
        Inches(width_in), Inches(height_in),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    if not line:
        shape.line.fill.background()
    return shape

# === layouts/title.py ===
"""title layout: typography hero + left-edge accent block."""




def _render_title(slide, spec, brand, accent):
    layout = PALETTE["title"]

    a = layout["accent_block"]
    add_filled_rect(slide, a["left"], a["top"], a["width"], a["height"],
                    fill_hex=brand["accents"][accent])

    t = layout["title_box"]
    add_text_box(
        slide,
        t["left"], t["top"], t["width"], t["height"],
        text=spec["title"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["title"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    p = layout["promise_box"]
    add_text_box(
        slide,
        p["left"], p["top"], p["width"], p["height"],
        text=spec["promise"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
    )

    b = layout["byline_box"]
    add_text_box(
        slide,
        b["left"], b["top"], b["width"], b["height"],
        text=spec["byline"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=resolve_colour(brand, accent, "accent"),
    )

# === layouts/section_divider.py ===
"""section_divider layout: accent band, large numeral, section title."""




def _render_section_divider(slide, spec, brand, accent):
    layout = PALETTE["section_divider"]

    a = layout["accent_block"]
    add_filled_rect(slide, a["left"], a["top"], a["width"], a["height"],
                    fill_hex=brand["accents"][accent])

    n = layout["number_box"]
    add_text_box(
        slide,
        n["left"], n["top"], n["width"], n["height"],
        text=f"{spec['section_number']:02d}",
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["section_number"],
        colour_hex=resolve_colour(brand, accent, "accent"),
        bold=True,
    )

    t = layout["title_box"]
    add_text_box(
        slide,
        t["left"], t["top"], t["width"], t["height"],
        text=spec["title"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["title"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

# === layouts/single_statement.py ===
"""single_statement layout: one centred line, big type, lots of white space."""




def _render_single_statement(slide, spec, brand, accent):
    layout = PALETTE["single_statement"]
    box = layout["statement_box"]
    add_text_box(
        slide,
        box["left"], box["top"], box["width"], box["height"],
        text=spec["statement"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["statement"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        align="center",
        anchor="middle",
    )

# === layouts/two_up.py ===
"""two_up layout: heading across the top, body on the left, configurable
right-side block: quote / stat / diagram-placeholder / mini-chart caption.
"""




def _render_right_quote(slide, box, content, brand, accent):
    add_text_box(
        slide,
        box["left"], box["top"], box["width"], box["height"] - 0.8,
        text=f"“{content['quote']}”",
        font_family=brand["fonts"]["header"],
        size_pt=24,
        colour_hex=resolve_colour(brand, accent, "text_primary"),
    )
    add_text_box(
        slide,
        box["left"], box["top"] + box["height"] - 0.7,
        box["width"], 0.5,
        text=f"— {content['attribution']}",
        font_family=brand["fonts"]["body"],
        size_pt=14,
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
    )


def _render_right_stat(slide, box, content, brand, accent):
    add_text_box(
        slide,
        box["left"], box["top"], box["width"], 2.0,
        text=f"{content['stat']}{content.get('unit', '')}",
        font_family=brand["fonts"]["header"],
        size_pt=72,
        colour_hex=resolve_colour(brand, accent, "accent"),
        bold=True,
        anchor="middle",
    )
    add_text_box(
        slide,
        box["left"], box["top"] + 2.2,
        box["width"], box["height"] - 2.2,
        text=content["context"],
        font_family=brand["fonts"]["body"],
        size_pt=16,
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
    )


def _render_right_diagram(slide, box, content, brand, accent):
    add_text_box(
        slide,
        box["left"], box["top"], box["width"], box["height"],
        text=content.get("caption", "[diagram placeholder]"),
        font_family=brand["fonts"]["body"],
        size_pt=16,
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
        align="center",
        anchor="middle",
    )


_RIGHT_RENDERERS = {
    "quote":   _render_right_quote,
    "stat":    _render_right_stat,
    "diagram": _render_right_diagram,
    "chart":   _render_right_diagram,
}


def _render_two_up(slide, spec, brand, accent):
    layout = PALETTE["two_up"]

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    b = layout["body_box"]
    add_text_box(
        slide,
        b["left"], b["top"], b["width"], b["height"],
        text=spec["body"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
    )

    r = layout["right_box"]
    right_type = spec.get("right_block_type", "diagram")
    renderer = _RIGHT_RENDERERS.get(right_type, _render_right_diagram)
    renderer(slide, r, spec["right_block_content"], brand, accent)

# === layouts/pillars.py ===
"""pillars layout: heading across top, N equal-width columns below."""



def _render_pillars(slide, spec, brand, accent):
    layout_id = spec["layout"]
    layout = PALETTE[layout_id]
    count = layout["pillar_count"]
    pillars = spec["pillars"]
    if len(pillars) != count:
        raise ValueError(
            f"{layout_id} expects {count} pillars, spec has {len(pillars)}"
        )

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    cols = layout["columns"]
    slide_w = brand["slide_dimensions_in"]["width"]
    margin = layout["margin_in"]
    total_w = slide_w - margin["left"] - margin["right"]
    gap = cols["gap"]
    pillar_w = (total_w - gap * (count - 1)) / count

    pillar_heading_size = brand["sizes_pt"]["pillar_heading"]
    body_size = brand["sizes_pt"]["body"] if count == 3 else 14

    for i, pillar in enumerate(pillars):
        x = margin["left"] + i * (pillar_w + gap)

        icon_size = cols["icon_h"]
        add_filled_rect(
            slide, x, cols["top"], icon_size, icon_size,
            fill_hex=brand["accents"][accent],
        )
        add_text_box(
            slide, x, cols["top"], icon_size, icon_size,
            text=str(pillar.get("icon_glyph", "")),
            font_family=brand["fonts"]["header"],
            size_pt=int(icon_size * 36),
            colour_hex=resolve_colour(brand, accent, "inverse"),
            bold=True,
            align="center", anchor="middle",
        )

        head_top = cols["top"] + icon_size + 0.15
        add_text_box(
            slide, x, head_top, pillar_w, cols["heading_h"],
            text=pillar["heading"],
            font_family=brand["fonts"]["header"],
            size_pt=pillar_heading_size,
            colour_hex=resolve_colour(brand, accent, "text_primary"),
            bold=True,
        )

        body_top = head_top + cols["heading_h"] + 0.1
        add_text_box(
            slide, x, body_top, pillar_w, cols["body_h"],
            text=pillar["body"],
            font_family=brand["fonts"]["body"],
            size_pt=body_size,
            colour_hex=resolve_colour(brand, accent, "text_primary"),
        )

# === layouts/process_flow.py ===
"""process_flow layout: heading + 4-6 rounded-rectangle steps in a row."""

from pptx.util import Pt
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN



def _render_process_flow(slide, spec, brand, accent):
    layout = PALETTE["process_flow"]
    steps = spec["steps"]
    n = len(steps)
    if not (layout["chain"]["min"] <= n <= layout["chain"]["max"]):
        raise ValueError(
            f"process_flow needs {layout['chain']['min']}-{layout['chain']['max']} steps, got {n}"
        )

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    margin = layout["margin_in"]
    slide_w = brand["slide_dimensions_in"]["width"]
    total_w = slide_w - margin["left"] - margin["right"]
    gap = layout["chain"]["gap"]
    box_w = (total_w - gap * (n - 1)) / n
    top = layout["chain"]["top"]
    h_box = layout["chain"]["height"]

    for i, step in enumerate(steps):
        x = margin["left"] + i * (box_w + gap)
        rect = add_rounded_rect(slide, x, top, box_w, h_box,
                                fill_hex=brand["accents"][accent])
        tf = rect.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = step["label"]
        p.alignment = PP_ALIGN.CENTER
        if p.runs:
            r = p.runs[0]
            r.font.name = brand["fonts"]["header"]
            r.font.size = Pt(brand["sizes_pt"]["pillar_heading"])
            r.font.bold = True
            r.font.color.rgb = hex_to_rgb(brand["text"]["inverse"])

        add_text_box(
            slide, x, layout["detail_top"], box_w, 1.5,
            text=step.get("detail", ""),
            font_family=brand["fonts"]["body"],
            size_pt=14,
            colour_hex=resolve_colour(brand, accent, "text_secondary"),
            align="center", anchor="top",
        )

# === layouts/compare_contrast.py ===
"""compare_contrast layout: heading + two parallel labelled bullet columns."""




def _bullet_lines(points):
    return "\n".join(f"• {p}" for p in points)


def _render_compare_contrast(slide, spec, brand, accent):
    layout = PALETTE["compare_contrast"]

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    for side in ("left", "right"):
        label_box = layout[f"{side}_label"]
        body_box = layout[f"{side}_body"]
        add_text_box(
            slide,
            label_box["left"], label_box["top"], label_box["width"], label_box["height"],
            text=spec[f"{side}_label"],
            font_family=brand["fonts"]["header"],
            size_pt=brand["sizes_pt"]["pillar_heading"],
            colour_hex=resolve_colour(brand, accent, "accent"),
            bold=True,
        )
        add_text_box(
            slide,
            body_box["left"], body_box["top"], body_box["width"], body_box["height"],
            text=_bullet_lines(spec[f"{side}_points"]),
            font_family=brand["fonts"]["body"],
            size_pt=brand["sizes_pt"]["body"],
            colour_hex=resolve_colour(brand, accent, "text_primary"),
        )

# === layouts/stat_callout.py ===
"""stat_callout layout: hero number with unit + context line."""




def _render_stat_callout(slide, spec, brand, accent):
    layout = PALETTE["stat_callout"]

    s = layout["stat_box"]
    add_text_box(
        slide,
        s["left"], s["top"], s["width"], s["height"],
        text=f"{spec['stat']}{spec.get('unit', '')}",
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["stat"],
        colour_hex=resolve_colour(brand, accent, "accent"),
        align="center", anchor="middle",
        bold=True,
    )

    c = layout["context_box"]
    add_text_box(
        slide,
        c["left"], c["top"], c["width"], c["height"],
        text=spec["context"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
        align="center",
    )

# === layouts/quote.py ===
"""quote layout: oversized opening quote mark + quote body + attribution."""




def _render_quote(slide, spec, brand, accent):
    layout = PALETTE["quote"]

    m = layout["mark_box"]
    add_text_box(
        slide,
        m["left"], m["top"], m["width"], m["height"],
        text="“",
        font_family=brand["fonts"]["header"],
        size_pt=180,
        colour_hex=resolve_colour(brand, accent, "accent"),
        bold=True,
    )

    q = layout["quote_box"]
    add_text_box(
        slide,
        q["left"], q["top"], q["width"], q["height"],
        text=spec["quote"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
    )

    a = layout["attribution_box"]
    add_text_box(
        slide,
        a["left"], a["top"], a["width"], a["height"],
        text=f"— {spec['attribution']}",
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
    )

# === layouts/chart.py ===
"""chart layout: heading + native PowerPoint chart (BAR/LINE/COLUMN) + caption."""

from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches




_CHART_TYPE_MAP = {
    "bar":    XL_CHART_TYPE.BAR_CLUSTERED,
    "column": XL_CHART_TYPE.COLUMN_CLUSTERED,
    "line":   XL_CHART_TYPE.LINE,
}


def _render_chart(slide, spec, brand, accent):
    layout = PALETTE["chart"]

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    chart_box = layout["chart_box"]
    chart_type = _CHART_TYPE_MAP.get(spec.get("chart_type", "bar"), XL_CHART_TYPE.BAR_CLUSTERED)
    data = spec["chart_data"]
    chart_data = CategoryChartData()
    chart_data.categories = data["categories"]
    for series in data["series"]:
        chart_data.add_series(series["name"], series["values"])
    slide.shapes.add_chart(
        chart_type,
        Inches(chart_box["left"]), Inches(chart_box["top"]),
        Inches(chart_box["width"]), Inches(chart_box["height"]),
        chart_data,
    )

    c = layout["caption_box"]
    add_text_box(
        slide,
        c["left"], c["top"], c["width"], c["height"],
        text=spec.get("caption", ""),
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["footer"],
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
    )

# === layouts/recap.py ===
"""recap layout: bulleted takeaways + next-step pointer + signoff line."""




def _render_recap(slide, spec, brand, accent):
    layout = PALETTE["recap"]

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text="Takeaways",
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    t = layout["takeaways_box"]
    bullets = "\n".join(f"• {item}" for item in spec["takeaways"])
    add_text_box(
        slide,
        t["left"], t["top"], t["width"], t["height"],
        text=bullets,
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
    )

    n = layout["next_step_box"]
    add_text_box(
        slide,
        n["left"], n["top"], n["width"], 0.5,
        text="Next step",
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["pillar_heading"],
        colour_hex=resolve_colour(brand, accent, "accent"),
        bold=True,
    )
    add_text_box(
        slide,
        n["left"], n["top"] + 0.6, n["width"], n["height"] - 0.6,
        text=spec["next_step"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
    )

    s = layout["signoff_box"]
    add_text_box(
        slide,
        s["left"], s["top"], s["width"], s["height"],
        text="Teachers Assistant AI",
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["footer"],
        colour_hex=resolve_colour(brand, accent, "text_secondary"),
        align="right",
    )

# === layouts/data_table.py ===
"""data_table layout: heading + native PowerPoint table.

Limits: 5 rows x 4 cols (validated). Header row tinted with accent;
emphasis cells get a soft accent fill.
"""

from pptx.util import Inches, Pt




def _render_data_table(slide, spec, brand, accent):
    layout = PALETTE["data_table"]
    columns = spec["columns"]
    rows = spec["rows"]
    if len(rows) > layout["max_rows"]:
        raise ValueError(f"data_table: {len(rows)} rows exceeds max {layout['max_rows']}")
    if len(columns) > layout["max_cols"]:
        raise ValueError(f"data_table: {len(columns)} columns exceeds max {layout['max_cols']}")

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    tb = layout["table_box"]
    table_shape = slide.shapes.add_table(
        rows=len(rows) + 1, cols=len(columns),
        left=Inches(tb["left"]), top=Inches(tb["top"]),
        width=Inches(tb["width"]), height=Inches(tb["height"]),
    )
    table = table_shape.table

    accent_hex = brand["accents"][accent]
    inverse_hex = brand["text"]["inverse"]
    text_primary_hex = brand["text"]["primary"]

    for i, col in enumerate(columns):
        cell = table.cell(0, i)
        cell.text = col
        cell.fill.solid()
        cell.fill.fore_color.rgb = hex_to_rgb(accent_hex)
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.name = brand["fonts"]["header"]
                run.font.size = Pt(14)
                run.font.bold = True
                run.font.color.rgb = hex_to_rgb(inverse_hex)

    emphasis = {tuple(c) for c in spec.get("emphasis_cells", [])}
    for r_idx, row in enumerate(rows):
        for c_idx, value in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = str(value)
            if (r_idx, c_idx) in emphasis:
                cell.fill.solid()
                cell.fill.fore_color.rgb = hex_to_rgb(brand["text"]["inverse"])
            for para in cell.text_frame.paragraphs:
                for run in para.runs:
                    run.font.name = brand["fonts"]["body"]
                    run.font.size = Pt(12)
                    run.font.color.rgb = hex_to_rgb(text_primary_hex)

# === layouts/stat_doughnut.py ===
"""stat_doughnut layout: heading + 3 side-by-side doughnut charts."""

from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches




def _render_stat_doughnut(slide, spec, brand, accent):
    layout = PALETTE["stat_doughnut"]

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    margin = layout["margin_in"]
    slide_w = brand["slide_dimensions_in"]["width"]
    total_w = slide_w - margin["left"] - margin["right"]
    n = layout["doughnut_count"]
    size = layout["doughnut_size"]
    gap = (total_w - size * n) / (n - 1) if n > 1 else 0

    doughnuts = spec["doughnuts"]
    if len(doughnuts) != n:
        raise ValueError(f"stat_doughnut needs {n} entries, got {len(doughnuts)}")

    for i, d in enumerate(doughnuts):
        x = margin["left"] + i * (size + gap)
        y = layout["doughnut_top"]

        chart_data = CategoryChartData()
        chart_data.categories = [d["label"], "rest"]
        chart_data.add_series("share", [d["percent"], 100 - d["percent"]])
        slide.shapes.add_chart(
            XL_CHART_TYPE.DOUGHNUT,
            Inches(x), Inches(y), Inches(size), Inches(size),
            chart_data,
        )

        role = d.get("accent_role", "info")
        colour_hex = (
            resolve_severity_colour(brand, role)
            if role != "neutral"
            else resolve_colour(brand, accent, "accent")
        )
        add_text_box(
            slide, x, y + size + 0.05, size, 0.5,
            text=f"{d['percent']}%",
            font_family=brand["fonts"]["header"],
            size_pt=28,
            colour_hex=colour_hex,
            bold=True,
            align="center",
        )

        add_text_box(
            slide, x, layout["label_top"], size, 0.6,
            text=d["label"],
            font_family=brand["fonts"]["body"],
            size_pt=brand["sizes_pt"]["body"],
            colour_hex=resolve_colour(brand, accent, "text_primary"),
            align="center",
        )

# === layouts/quadrant_grid.py ===
"""quadrant_grid layout: heading + 2x2 grid of numbered cells."""



def _render_quadrant_grid(slide, spec, brand, accent):
    layout = PALETTE["quadrant_grid"]
    cells = spec["cells"]
    if len(cells) != 4:
        raise ValueError(f"quadrant_grid needs 4 cells, got {len(cells)}")

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=resolve_colour(brand, accent, "text_primary"),
        bold=True,
    )

    cw = layout["cell_width"]
    ch = layout["cell_height"]
    gap = layout["cell_gap"]
    gl = layout["grid_left"]
    gt = layout["grid_top"]

    positions = [
        (gl,           gt),
        (gl + cw + gap, gt),
        (gl,           gt + ch + gap),
        (gl + cw + gap, gt + ch + gap),
    ]

    cell_fill_hex = brand["text"]["inverse"]
    border_hex    = brand["accents"][accent]

    for (x, y), cell in zip(positions, cells):
        rect = add_rounded_rect(slide, x, y, cw, ch, fill_hex=cell_fill_hex, line=True)
        rect.line.color.rgb = hex_to_rgb(border_hex)

        add_text_box(
            slide, x + 0.15, y + 0.1, 1.0, 1.0,
            text=str(cell["number"]),
            font_family=brand["fonts"]["header"],
            size_pt=48,
            colour_hex=resolve_colour(brand, accent, "accent"),
            bold=True,
        )

        add_text_box(
            slide, x + 1.2, y + 0.3, cw - 1.4, 0.6,
            text=cell["label"],
            font_family=brand["fonts"]["header"],
            size_pt=brand["sizes_pt"]["pillar_heading"],
            colour_hex=resolve_colour(brand, accent, "text_primary"),
            bold=True,
        )

        add_text_box(
            slide, x + 0.3, y + 1.1, cw - 0.6, ch - 1.2,
            text=cell["body"],
            font_family=brand["fonts"]["body"],
            size_pt=brand["sizes_pt"]["body"],
            colour_hex=resolve_colour(brand, accent, "text_primary"),
        )

# === layouts/callout_box.py ===
"""callout_box layout: severity-keyed tinted container with heading + body."""



def _render_callout_box(slide, spec, brand, accent):
    layout = PALETTE["callout_box"]
    severity = spec.get("severity", "info")
    severity_hex = resolve_severity_colour(brand, severity)

    c = layout["container"]
    add_filled_rect(slide, c["left"], c["top"], c["width"], c["height"],
                    fill_hex=severity_hex)

    text_colour = resolve_colour(brand, accent, "inverse") if severity in (
        "critical", "positive", "warning"
    ) else resolve_colour(brand, accent, "text_primary")

    h = layout["heading_box"]
    add_text_box(
        slide,
        h["left"], h["top"], h["width"], h["height"],
        text=spec["heading"],
        font_family=brand["fonts"]["header"],
        size_pt=brand["sizes_pt"]["heading"],
        colour_hex=text_colour,
        bold=True,
    )

    b = layout["body_box"]
    add_text_box(
        slide,
        b["left"], b["top"], b["width"], b["height"],
        text=spec["body"],
        font_family=brand["fonts"]["body"],
        size_pt=brand["sizes_pt"]["body"],
        colour_hex=text_colour,
    )

# === renderer.py ===
"""render_deck — entry point.

Takes a deck spec (Director-produced + per-slide content from Section
branches) and returns a pptx.Presentation object. Caller is responsible
for saving it.
"""

from pptx import Presentation
from pptx.util import Inches



_RENDERERS = {
    "title":            _render_title,
    "section_divider":  _render_section_divider,
    "single_statement": _render_single_statement,
    "two_up":           _render_two_up,
    "pillars_3":        _render_pillars,
    "pillars_4":        _render_pillars,
    "process_flow":     _render_process_flow,
    "compare_contrast": _render_compare_contrast,
    "stat_callout":     _render_stat_callout,
    "quote":            _render_quote,
    "chart":            _render_chart,
    "recap":            _render_recap,
    "data_table":       _render_data_table,
    "stat_doughnut":    _render_stat_doughnut,
    "quadrant_grid":    _render_quadrant_grid,
    "callout_box":      _render_callout_box,
}


def _add_dark_background(slide, brand):
    add_filled_rect(slide, 0, 0,
                    brand["slide_dimensions_in"]["width"],
                    brand["slide_dimensions_in"]["height"],
                    fill_hex=brand["primary"])


def render_deck(spec, theme="light", accent="mint", brand=None):
    """Render a deck.

    Args:
        spec: dict with keys deck_title, footer_text, sections, slides.
        theme: "light" or "dark".
        accent: one of brand.accents keys.
        brand: optional BRAND override (mostly for tests).
    Returns:
        pptx.Presentation object.
    """
    brand = brand or BRAND
    if accent not in brand["accents"]:
        raise ValueError(f"Unknown accent: {accent!r}")
    if theme not in ("light", "dark"):
        raise ValueError(f"Unknown theme: {theme!r}")

    prs = Presentation()
    prs.slide_width  = Inches(brand["slide_dimensions_in"]["width"])
    prs.slide_height = Inches(brand["slide_dimensions_in"]["height"])

    slides = sorted(spec["slides"], key=lambda s: s["position"])
    blank = prs.slide_layouts[6]

    for slide_spec in slides:
        slide = prs.slides.add_slide(blank)
        if theme == "dark":
            _add_dark_background(slide, brand)
        layout_id = slide_spec["layout"]
        renderer = _RENDERERS.get(layout_id)
        if renderer is None:
            raise ValueError(f"Unknown layout: {layout_id!r}")
        renderer(slide, slide_spec, brand=brand, accent=accent)

        notes = slide_spec.get("presenter_notes", "")
        slide.notes_slide.notes_text_frame.text = notes

    return prs
