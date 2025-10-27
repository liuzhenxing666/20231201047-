#!/usr/bin/env python3
"""
简单的API测试脚本，用于验证Django后端API是否正常工作
"""

import requests
import json

def test_api():
    base_url = "http://localhost:8000/api"
    
    print("=== Django百科项目API测试 ===")
    
    # 测试分类API
    print("\n1. 测试分类API...")
    try:
        response = requests.get(f"{base_url}/categories/")
        print(f"分类列表状态码: {response.status_code}")
        if response.status_code == 200:
            print("✓ 分类API测试通过")
        else:
            print(f"✗ 分类API测试失败: {response.text}")
    except Exception as e:
        print(f"✗ 分类API连接失败: {e}")
    
    # 测试词条API
    print("\n2. 测试词条API...")
    try:
        response = requests.get(f"{base_url}/entries/")
        print(f"词条列表状态码: {response.status_code}")
        if response.status_code == 200:
            print("✓ 词条API测试通过")
        else:
            print(f"✗ 词条API测试失败: {response.text}")
    except Exception as e:
        print(f"✗ 词条API连接失败: {e}")
    
    # 测试搜索API
    print("\n3. 测试搜索API...")
    try:
        response = requests.get(f"{base_url}/entries/search/?q=test")
        print(f"搜索API状态码: {response.status_code}")
        if response.status_code == 200:
            print("✓ 搜索API测试通过")
        else:
            print(f"✗ 搜索API测试失败: {response.text}")
    except Exception as e:
        print(f"✗ 搜索API连接失败: {e}")
    
    print("\n=== API测试完成 ===")
    print("\n注意：如果测试失败，请确保：")
    print("1. Django后端服务器正在运行 (http://localhost:8000)")
    print("2. 数据库已正确迁移 (python manage.py migrate)")
    print("3. CORS配置正确")

if __name__ == "__main__":
    test_api()