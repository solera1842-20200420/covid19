# solera1842-20200420

Streamlitとplotlyのグラフ表示のDocker

ディレクトリ構成

```
$ pwd
docker_streamlit_app

$ tree .
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── src
│   ├── data
│   │   └── newly_confirmed_cases_daily.csv
│   └── st_covid19_line_plot.py
├── streamlit_py3
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── src
│       ├── data
│       │   └── cluster_events_weekly.csv
│       └── st_cluster_events_jp.py
└── streamlit_ubuntu20
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── src
```

``` venv)$pwd
/data_01/container/docker_streamlit_app
```
ビルド
```
$ docker-compose build
```
コンテナ起動
```
$ docker-compose up -d
```
ホストのブラウザからlocalhost:8501を開くと、Streamlitのグラフのスクリプトが現れる。

停止
```
$ docker-compose stop
```

次回以降の起動
```
$ docker-compose start
```

1.グラフ表示コンテナ
```
(.venv)$ ls
 Dockerfile  docker-compose.yml  requirements.txt  src

$ pwd
docker_streamlit_app
$ cat Dockerfile |grep FROM
FROM ubuntu:20.04

$ cat Dockerfile |tail -n2
ENTRYPOINT ["streamlit", "run"]
CMD ["st_covid19_line_plot.py"]
```
2.サブディレクトリ

2-1.グラフ表示スクリプトなしのStreamlitとplotlyのdocker
Baseイメージ: ubuntu
```
$ pwd
$ docker_streamlit_app/streamlit_ubuntu20
$ cat Dockerfile |tail -n2
# python 
CMD ["bash"]

```
2-2.グラフ表示コンテナ
streamlit_py3
Baseイメージ: python3
```
$ pwd
docker_streamlit_app/streamlit_py3
$ cat Dockerfile |grep FROM
FROM python:3

$ cat Dockerfile |tail -n2
ENTRYPOINT ["streamlit", "run"]
CMD ["st_cluster_events_jp.py"]
```
