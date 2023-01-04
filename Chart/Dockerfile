#Para dockerizar scripts
FROM python:3.8

WORKDIR /app
COPY requirements.txt requirements.txt
                #Local - Contenedor
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . app/
#Copiar todo

CMD bash -c "while true; do sleep 1; done"
#si se quiere que el contenedor se mantenga encendido