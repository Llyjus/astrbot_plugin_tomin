def numpy_system_dependencies_check():

    try:
        import numpy

    except Exception as e:

        msg ="numpy 不可用，程序无法继续运行。\n numpy 本身应已在插件启动时被安装。\n请参考 README.md 安装 numpy 系统依赖。"
        
        raise RuntimeError(msg) from e
