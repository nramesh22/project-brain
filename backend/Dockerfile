FROM python:3.11-slim

# Install OS deps for building wheels if needed
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# (Optional) If you WANT to compile languages manually
# RUN git clone https://github.com/tree-sitter/tree-sitter-python vendor/tree-sitter-python
# RUN python3 - << 'EOF'
# from tree_sitter import Language
# Language.build_library(
#     'build/my-languages.so',
#     ['vendor/tree-sitter-python']
# )
# EOF

RUN ls -l /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8800"]