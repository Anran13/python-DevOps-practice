import fire
import pkgutil
import importlib


def find_and_run_plugins(plugin_prefix):
    plugins = {}
    print(f"Discovering plugins with prefix: {plugin_prefix}")

    # 發現並載入外掛
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    # 執行外掛
    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()


if __name__ == '__main__':
    fire.Fire()

# execute in terminal with:
# python chap3-7.py --help
# To run plugins, use:
# python chap3-7.py find_and_run_plugins --plugin_prefix=plugin_
# python chap3-7.py find_and_run_plugins plugin_math_
