FROM registry.dp.tech/mlops/workbench-base:0.0.1-alpha

ADD docker/sources.list /etc/apt/sources.list

ENV SAMPLE_DATA_ROOT=/opt/sample-data
ENV LAUNCHING_ROOT=/app-dir
ENV TMPDIR=/app-dir/tmp

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN  pip install pydantic --upgrade
ADD . ./
ENTRYPOINT ["/app/run_service.sh"]

