# 使用官方 Python 映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 安裝系統依賴，這些是 Playwright 運行所需的
RUN apt-get update && apt-get install -y \
    libx11-dev \
    libxcomposite1 \
    libxrandr2 \
    libgtk-3-0 \
    libgbm-dev \
    libasound2 \
    libnss3 \
    libxss1 \
    libxtst6 \
    && rm -rf /var/lib/apt/lists/*

# 複製本地文件到 Docker 容器中
COPY . /app/

# 安裝 Python 依賴
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 安裝 Playwright 瀏覽器和依賴
RUN playwright install --with-deps

# 開放容器的 8000 端口
EXPOSE 8000

# 設置容器啟動時執行的命令
CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0", "--port", "8000"]
