FROM python
WORKDIR /app
COPY . /app
CMD ["python3", "text_editor.py"]