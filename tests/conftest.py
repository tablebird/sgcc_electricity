# tests/conftest.py
import sys
import os
import dotenv

# 获取项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))
scripts_path = os.path.join(project_root, '..', 'scripts')

# 将 scripts 目录加入 sys.path
sys.path.insert(0, scripts_path)

# 加载 .env 文件
dotenv.load_dotenv(dotenv_path="scripts/.env", verbose=True)