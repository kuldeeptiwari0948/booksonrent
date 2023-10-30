FROM python:3.12.0
RUN pip install Django==3.2
RUN pip install setuptools
COPY . code
WORKDIR /code
EXPOSE 8000
ENTRYPOINT ["python", "book_rental/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]