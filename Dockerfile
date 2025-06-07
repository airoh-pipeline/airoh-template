FROM python:3.10-slim

LABEL maintainer="Lune Bellec <lune.bellec@gmail.com>"

# Switch to notebook user
USER $NB_UID

# Copy project code
COPY . . 

# Setup environment via user-editable script
RUN pip install -r setup.txt && \
    invoke setup
