FROM continuumio/miniconda3 as base

COPY environment.yml ./
RUN conda update conda && \
  conda env update -f environment.yml -n base && \
  conda clean -af


FROM base as dependencies

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=never \
  UV_PYTHON=python3.12 \
  UV_PROJECT_ENVIRONMENT=/opt/venv \
  PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-ephemeral
COPY --from=base /opt/conda /opt/conda
COPY pyproject.toml ./
COPY src/stactools/ephemeral/__init__.py src/stactools/ephemeral/
RUN apt-get -y -q update \
  && apt-get -y -q install build-essential \
  && rm -rf /var/lib/apt/lists/
RUN uv sync --no-install-project --no-editable


FROM dependencies as builder

ENV UV_LINK_MODE=copy \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=never \
  UV_PYTHON=python3.12 \
  UV_PROJECT_ENVIRONMENT=/opt/venv \
  PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-ephemeral
COPY --from=base /opt/conda /opt/conda
COPY --from=dependencies /opt/venv /opt/venv
COPY pyproject.toml ./
COPY src ./src
RUN uv sync --no-dev --no-editable
WORKDIR /
RUN rm -rf /opt/stactools-ephemeral
CMD [ "stac", "ephemeralcmd" ]


FROM dependencies as dev-dependencies

ENV UV_LINK_MODE=copy \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=never \
  UV_PYTHON=python3.12 \
  UV_PROJECT_ENVIRONMENT=/opt/venv \
  PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-ephemeral
COPY --from=dependencies /opt/venv /opt/venv
COPY pyproject.toml .
RUN uv sync \
  && git init


FROM dev-dependencies as dev-builder

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-ephemeral
COPY --from=base /opt/conda /opt/conda
COPY --from=dependencies /opt/venv /opt/venv
COPY . .
CMD [ "stac", "ephemeralcmd" ]
