
from util.Parser import Parser
from util.Config import Config
from function.IQR import IQR

def main():

    args = Parser().initilaize_arg_parser()
    config = Config().collect_config()

    if (args.function == 'iqr'):
        IQR().calc_iqr()
    else:
        print("Please provide a valid function. -h to see list of available options.")

main()
