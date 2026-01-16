FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN echo 'export PS1="\[\033[1;32m\]\u@\h:\w\$\[\033[0m\] "' >> /etc/bash.bashrc
ENV HF_HOME=/tmp/.huggingface
EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
