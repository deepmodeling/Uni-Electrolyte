
cp docker/sources.list /etc/apt/sources.list

export SAMPLE_DATA_ROOT=/opt/sample-data
export LAUNCHING_ROOT=/app-dir
export TMPDIR=/app-dir/tmp

mkdir -p /app
#WORKDIR /app
#ADD requirements.txt requirements.txt
pip install -r requirements.txt -i  https://repo.mlops.dp.tech/repository/pypi-group/simple
pip install pydantic --upgrade
#ADD . ./
#ENTRYPOINT ["/app/run_service.sh"]

http://skut1130282.bohrium.tech:50000/