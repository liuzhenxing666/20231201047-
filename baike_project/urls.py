"""baike_project URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def welcome_page(request):
    """简单的欢迎页面"""
    # 使用双花括号来转义CSS中的花括号
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>百科系统 - 欢迎</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .links {{ margin-top: 20px; }}
            .links a {{ display: inline-block; margin: 10px; padding: 10px 20px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; }}
            .links a:hover {{ background: #2980b9; }}
            .api-info {{ background: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 百科系统 - 欢迎页面</h1>
            <p>Django后端服务器正在正常运行！</p>
            
            <div class="api-info">
                <h3>📊 可用API接口：</h3>
                <ul>
                    <li><strong>分类管理</strong>: <a href="/api/categories/">/api/categories/</a></li>
                    <li><strong>词条管理</strong>: <a href="/api/entries/">/api/entries/</a></li>
                    <li><strong>管理员后台</strong>: <a href="/admin/">/admin/</a></li>
                </ul>
            </div>
            
            <div class="links">
                <a href="/api/categories/">查看分类列表</a>
                <a href="/api/entries/">查看词条列表</a>
                <a href="/admin/">管理员后台</a>
                <a href="/test/">前端测试页面</a>
            </div>
            
            <p style="margin-top: 30px; color: #666;">服务器时间: {server_time}</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content.format(server_time=request.build_absolute_uri()))

def simple_test_page(request):
    """前端测试页面"""
    # 读取simple_test.html文件内容
    import os
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'simple_test.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("测试页面文件未找到", status=404)

urlpatterns = [
    path('', welcome_page, name='welcome'),
    path('test/', simple_test_page, name='test'),
    path('admin/', admin.site.urls),
    path('api/', include('encyclopedia.urls')),
]