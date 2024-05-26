import argparse
import runpy


def run_hello():
    module_name = "serverlessHelloCleanArch.lambda_handlers.hello_handler"
    runpy.run_module(module_name, run_name="__main__", alter_sys=True)


def run_bye():
    module_name = "serverlessHelloCleanArch.lambda_handlers.bye_handler"
    runpy.run_module(module_name, run_name="__main__", alter_sys=True)


def main():
    parser = argparse.ArgumentParser(description="My Project Runner")
    parser.add_argument(
        "command", choices=["hello", "bye"], help="Command to run"
    )
    args = parser.parse_args()

    if args.command == "hello":
        run_hello()
    elif args.command == "bye":
        run_bye()


if __name__ == "__main__":
    main()
