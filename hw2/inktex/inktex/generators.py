from dataclasses import dataclass

@dataclass
class Table:
    caption: str
    col_names: list
    rows: list

def generate_table(table: Table) -> str:
    cols_count = len(table.col_names)

    latex_table = [
        r"\begin{table}[ht!]",
        r"\centering",
        r"\begin{tabular}{" + "|".join(["c"] * cols_count) + "}",
        r"\\\hline"
    ]

    latex_table.append("&".join(table.col_names) + r"\\\hline")

    rows = "\n".join(
        " & ".join(map(str, row)) + (r"\\" if idx != len(table.rows) - 1 else "")
        for idx, row in enumerate(table.rows)
    )

    latex_table.extend([
        rows,
        r"\end{tabular}",
        r"\caption{" + table.caption + "}",
        r"\end{table}"
    ])

    return "\n".join(latex_table)

@dataclass
class Image:
    caption: str
    filename: str
    width_scale: float

def generate_image(image: Image) -> str:
    latex_image = [
        r"\begin{figure}[ht!]",
        r"\centering",
        r"\includegraphics[width=" + f"{image.width_scale}" + r"\linewidth]" + "{" + image.filename + "}",
        r"\caption{" + image.caption + "}",
        r"\end{figure}"
    ]
    
    return "\n".join(latex_image)
