FROM python:3
COPY ./src/demoGql /usr/src/demoGql
WORKDIR /usr/src/demoGql
COPY requirements.txt /usr/src/demoGql
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}/usr/src"
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# docker run --name demo -d -p 8000:8000 demo-graphql-app