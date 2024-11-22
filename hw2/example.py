from inktex.generators import Table
from inktex.generators import generate_table

from inktex.generators import Image
from inktex.generators import generate_image


def save_latex(latex: str, filename: str):
    with open(filename, "w") as file:
        file.write(latex)

def generate_latex(table: Table, image: Image) -> str:
    with open("data/latex_template.tex", "r") as file:
        latex_template = file.read()

    return latex_template.replace("TABLE_PLACEHOLDER", generate_table(table)) \
                            .replace("IMAGE_PLACEHOLDER", generate_image(image))


if __name__ == '__main__':
    table = Table(
        caption="My Targets",
        col_names=["Target", "Achievability"],
        rows=[
            ["Become a university graduate", 90],
            ["Fly to the Moon", 1],
            ["Learn to play the violon", 75]
        ]
    )

    image = Image(
        caption="Cats",
        filename="data/image.png",
        width_scale=0.8
    )

    latex = generate_latex(table, image)
    save_latex(latex, "artifacts/result.tex")
