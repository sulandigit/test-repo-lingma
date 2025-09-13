#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hello import hello_world, greet

def main():
    """主函数"""
    print("欢迎使用测试程序!")
    hello_world()
    greet("用户")

if __name__ == "__main__":
    main()