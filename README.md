# solera1842-20200420

Streamlitとplotly、skleranのDockerの実装

'''venv)$pwd
/data_01/container/docker_streamlit
(.venv)$ ls
Dockerfile  docker-compose.yml  requirements.txt  src
(.venv)$ ls src
newly_confirmed_cases_daily.csv  st_covid19_line_plot.py
(.venv)$ docker ps
CONTAINER ID   IMAGE                  COMMAND   CREATED         STATUS         PORTS                    NAMES
362da490b391   docker_streamlit_web   "bash"    7 minutes ago   Up 7 minutes   0.0.0.0:8501->8501/tcp   docker_streamlit

ホスト側のDockerfileの場所から動かすスクリプトを実行
(.venv) $ docker exec docker_streamlit streamlit run st_covid19_line_plot.py
'''

実行後のコンソールからのメッセージ、ホストのブラウザからはlocalhost:8501を開く。
  You can now view your Streamlit app in your browser.
  Network URL: http://172.19.0.2:8501
  External URL: http://106.154.142.241:8501
  
ブラウザに実行したStreamlitのグラフのスクリプトが現れる。
