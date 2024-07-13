# Usar una imagen base de Python 3.12.2
FROM python:3.12.2-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . /app/

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "proyectois.wsgi:application"]

# Comando para ejecutar la aplicación
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]