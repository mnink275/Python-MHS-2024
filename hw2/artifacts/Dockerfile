FROM ubuntu:24.04

WORKDIR /latex

RUN apt-get update -y && \
    apt-get install texlive-latex-base -y && \
    apt install wget -y

RUN mkdir -p /miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda3/miniconda.sh && \
    bash /miniconda3/miniconda.sh -b -u -p /miniconda3 && \
    rm /miniconda3/miniconda.sh

ENV PATH="/miniconda3/bin:${PATH}"

RUN conda install ink275::inktex

CMD ["sh", "-c", "python3 example.py && pdflatex -output-directory=artifacts/ result.tex"]
