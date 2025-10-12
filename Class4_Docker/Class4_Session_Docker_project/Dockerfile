FROM python
# mkdir /app ; cd /app
WORKDIR /app  

# pwd -> /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# this is when image run as container
CMD ["python", "app.py"]