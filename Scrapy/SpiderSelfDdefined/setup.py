#coding:utf-8

#parse_requirements 的作用是读取项目下的requirements.txt文件，获取里面依赖项并自动安装
try:
    #pip <= 10.0
    from pip.req import parse_requirements
except:
    # pip > 10.0
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup


# with open(join(dirname(__file__), './VERSION.txt'), 'rb') as f:
#     version = f.read().decode('ascii').strip()
with open("./version.txt", "r") as f:
    version = f.read()
    """
        版本号
        作为一个合格的模块，应该要有版本号哦
    """
setup(
    name='SpiderAssassin',    # 模块名称
    version=version, # 版本号
    description='A mini spider framework, like Scrapy',    # 描述
    packages=find_packages(exclude=[]),  # 导入项目下所有的包 (exclude=[]表示排除)
    author='AssassinHotstrip',  # 作者
    author_email='your@email.com', # 作者邮箱
    license='Apache License v2',   # 软件发行协议APL，可以自行指定 GPL BSD APL等
    package_data={'': ['*.*']}, # 包的数据为 任意文件名.r任意后缀名
    url='#',  # 企业网址
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],# 读取文件获取所需的运行环境并自行安装
    zip_safe=False, # 在Windows下卸载不会报错
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix, Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ],
)
