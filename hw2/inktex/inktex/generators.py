from dataclasses import dataclass

@dataclass
class Table:
    caption: str
    col_names: list
    rows: list

def generate_table(table: Table) -> str:
    cols_count = len(table.col_names)

    table_template = r"""
\begin{table}[ht!]
\centering
\begin{tabular}"""

    table_template += f"{{{"|".join(["c"] * cols_count)}}}\n"
    table_template += f"{"&".join(table.col_names)}" +  r"\\\hline" + "\n"
    for idx, row in enumerate(table.rows):
        table_template += f"{"&".join([str(cell) for cell in row])}"
        if idx != len(table.rows) - 1:
            table_template += r"\\"
        table_template += "\n" 

    table_template += r"""
\end{tabular}
\caption{""" + table.caption + r"""}
\end{table}
"""

    return table_template

@dataclass
class Image:
    caption: str
    filename: str
    width_scale: float

def generate_image(image: Image) -> str:
    image_template = r"""
\begin{figure}[ht!]
\centering
\includegraphics[width=WIDTH_SCALE\linewidth]{FILENAME}
\caption{CAPTION}
\end{figure}
"""
    image_template = image_template.replace("WIDTH_SCALE", str(image.width_scale))
    image_template = image_template.replace("FILENAME", image.filename)
    image_template = image_template.replace("CAPTION", image.caption)

    return image_template
