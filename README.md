# Django百度百科风格简易项目

一个基于Django REST Framework和Vue.js的简易百科知识分享平台。

## 项目特性

- **后端API**: Django REST Framework提供完整的RESTful API
- **前端界面**: Vue.js 3构建的现代化单页面应用
- **响应式设计**: 支持各种设备屏幕尺寸
- **搜索功能**: 支持词条标题和内容的全文搜索
- **分类管理**: 词条分类管理功能
- **CRUD操作**: 完整的词条创建、读取、更新、删除功能

## 技术栈

### 后端
- Django 4.2.7
- Django REST Framework 3.14.0
- SQLite数据库
- CORS支持

### 前端
- Vue.js 3.3.4
- Vue Router 4.2.4
- Axios HTTP客户端
- 响应式CSS设计

## 项目结构

```
django_baike_project/
├── baike_project/                 # Django项目目录
│   ├── settings.py               # 项目配置
│   ├── urls.py                   # 主URL路由
│   └── wsgi.py                   # WSGI配置
├── encyclopedia/                  # Django应用目录
│   ├── models.py                 # 数据模型
│   ├── views.py                  # 视图逻辑
│   ├── serializers.py           # API序列化器
│   ├── urls.py                   # API路由
│   └── admin.py                  # 管理员配置
├── frontend/                      # Vue前端目录
│   ├── public/
│   ├── src/
│   │   ├── components/           # Vue组件
│   │   │   ├── common/           # 公共组件
│   │   │   └── entries/          # 词条相关组件
│   │   ├── views/                # 页面组件
│   │   ├── router/               # 路由配置
│   │   ├── services/            # API服务
│   │   └── App.vue              # 主应用组件
│   ├── package.json              # 前端依赖
│   └── vue.config.js            # Vue配置
├── requirements.txt              # Python依赖
├── manage.py                     # Django管理脚本
├── start_backend.bat             # 后端启动脚本
├── start_frontend.bat            # 前端启动脚本
└── README.md                    # 项目说明
```

## 快速开始

### 1. 环境准备

#### 安装Node.js（前端开发需要）
1. 访问 [Node.js官网](https://nodejs.org/) 下载并安装Node.js LTS版本
2. 安装完成后，在命令行中验证安装：
```bash
node --version
npm --version
```

### 2. 安装依赖

#### 后端依赖
```bash
pip install -r requirements.txt
```

#### 前端依赖
```bash
cd frontend
npm install
```

### 2. 初始化数据库

```bash
python manage.py migrate
python manage.py createsuperuser  # 创建管理员账户（可选）
```

### 3. 启动项目

#### 方法一：使用批处理脚本（推荐）

1. 双击 `start_backend.bat` 启动后端服务器（端口8000）
2. 双击 `start_frontend.bat` 启动前端开发服务器（端口8080）

#### 方法二：手动启动

启动后端：
```bash
python manage.py runserver 0.0.0.0:8000
```

启动前端：
```bash
cd frontend
npm run serve
```

### 4. 访问应用

- 前端应用：http://localhost:8080
- 后端API：http://localhost:8000/api/
- 管理员界面：http://localhost:8000/admin/ （需要先创建超级用户）

## API接口

### 分类接口
- `GET /api/categories/` - 获取分类列表
- `POST /api/categories/` - 创建分类
- `GET /api/categories/{id}/` - 获取分类详情
- `PUT /api/categories/{id}/` - 更新分类
- `DELETE /api/categories/{id}/` - 删除分类

### 词条接口
- `GET /api/entries/` - 获取词条列表
- `POST /api/entries/` - 创建词条
- `GET /api/entries/{id}/` - 获取词条详情
- `PUT /api/entries/{id}/` - 更新词条
- `DELETE /api/entries/{id}/` - 删除词条
- `GET /api/entries/search/?q={query}` - 搜索词条
- `GET /api/entries/by_category/?category_id={id}` - 按分类获取词条

## 功能说明

### 首页
- 项目介绍和欢迎页面
- 快速导航到词条列表

### 词条列表
- 显示所有词条的网格布局
- 实时搜索功能
- 创建新词条按钮
- 点击词条卡片查看详情

### 词条详情
- 显示词条完整内容
- 编辑功能（需要登录）
- 分类标签显示
- 创建时间和作者信息

### 词条表单
- 创建和编辑词条的模态框
- 标题、摘要、内容编辑
- 分类选择（多选）
- 表单验证

## 开发说明

### 后端开发
- 使用Django REST Framework构建API
- 支持CORS跨域请求
- 使用SQLite数据库（可替换为MySQL/PostgreSQL）
- 包含完整的管理员界面

### 前端开发
- Vue 3 Composition API
- 组件化开发
- 响应式设计
- Axios HTTP请求封装

## 部署说明

### 生产环境部署
1. 修改 `settings.py` 中的 `DEBUG = False`
2. 配置生产数据库
3. 收集静态文件：`python manage.py collectstatic`
4. 使用Gunicorn或uWSGI部署Django应用
5. 构建前端：`npm run build`
6. 配置Nginx反向代理

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。