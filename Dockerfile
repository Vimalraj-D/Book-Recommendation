FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# HuggingFace spaces uses port 7860
EXPOSE 7860

# Run the flask app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]