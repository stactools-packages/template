FROM continuumio/miniconda3

RUN conda update conda && conda install pip

COPY environment.yml /tmp/environment.yml
RUN conda env update -f /tmp/environment.yml -n base && rm /tmp/environment.yml

COPY . /tmp/stactools-subpackage
RUN cd /tmp/stactools-subpackage && pip install . && rm -rf /tmp/stactools-subpackage

ENTRYPOINT [ "python", "-m", "stactools.cli" ]
