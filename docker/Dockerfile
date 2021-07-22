ARG STACTOOLS_VERSION=latest
FROM ghcr.io/stac-utils/stactools:$STACTOOLS_VERSION

WORKDIR /opt/stactools-ephemeral

# For caching purposes, install dependencies but remove the actual ephemeral
COPY pyproject.toml setup.cfg ./
COPY src/stactools/ephemeral/__init__.py src/stactools/ephemeral/
RUN pip install . \
    && rm -r /opt/conda/lib/python3.8/site-packages/stactools/ephemeral

COPY src ./src
RUN pip install .
