FROM continuumio/miniconda3

RUN conda update conda && conda install pip

COPY environment.yml /tmp/environment.yml
RUN conda env update -f /tmp/environment.yml -n base && rm /tmp/environment.yml

COPY . /tmp/stactools-package
RUN cd /tmp/stactools-package && pip install . && rm -rf /tmp/stactools-package

ENTRYPOINT [ "python", "-m", "stactools.cli" ]
