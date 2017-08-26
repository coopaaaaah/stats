
from util.Parser import Parser
from util.Config import Config
from function.IQR import IQR
from function.SD import SD

def main():

    args = Parser().initilaize_arg_parser()
    config = Config().collect_config()

    if (args.function == 'iqr'):
        IQR().calc_iqr()
    elif (args.function == 'sd'):
        SD().calc_sd()
    else:
        print("Please provide a valid function. -h to see list of available options.")

main()
