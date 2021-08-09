# Docker streamlit, plotly, sklearn
# Base Image: Python3 
FROM python:3

# pip upgrade
ENV TERM xterm
RUN apt-get update && apt-get upgrade -y

# upgrade pip 
RUN pip install --upgrade pip && pip install --upgrade setuptools 

# python library

# mkdir root/src
RUN mkdir -p /root/src
COPY requirements.txt /root/src

# WORKDIR
WORKDIR /root/src

# ファイルコピー
# COPY requirements.txt /root/src 
COPY src/ /root/src/ 

# python library
RUN pip install -r requirements.txt

# port
EXPOSE 8501

# python 
# CMD ["streamlit", "run", "helloworld.py"]
# CMD ["streamlit", "run", "st_covid19_line_plot.py"]
CMD ["bash"]
