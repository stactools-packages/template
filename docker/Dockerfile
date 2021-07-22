ARG STACTOOLS_VERSION=latest
FROM ghcr.io/stac-utils/stactools:$STACTOOLS_VERSION

ARG DOCKER_PROJ_DIR_PARTIAL
ARG DOCKER_WORKDIR
WORKDIR $DOCKER_WORKDIR

# For caching purposes, install dependencies but remove the actual package
COPY pyproject.toml setup.cfg ./
COPY src/$DOCKER_PROJ_DIR_PARTIAL/__init__.py src/$DOCKER_PROJ_DIR_PARTIAL/
RUN pip install . \
    && rm -r /opt/conda/lib/python3.8/site-packages/$DOCKER_PROJ_DIR_PARTIAL

COPY src ./src
RUN pip install .
