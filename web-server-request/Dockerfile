#Para dockerizar scripts
FROM python:3.10

WORKDIR /app
COPY requirements.txt requirements.txt
                #Local - Contenedor
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . app/
#Copiar todo

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
#se lanzará el servidor en uvicorn

#CMD bash -c "while true; do sleep 1; done"
#si se quiere que el contenedor se mantenga encendido