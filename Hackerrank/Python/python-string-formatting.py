# Start Logging
import qlogger as ql
ql.start_logging(__file__)


# Run Code
try:
    def print_formatted(number):

        # richtige ergebnisse, aber nicht richtig eingerueckt :(
        # for i in range(1,number+1):
        #     # pos_o = oct(i).find('o') # int(str(oct(i).find('o')))
        #     # pos_h = hex(i).find('x') # int(str(hex(i).find('x')))
        #     # pos_b = bin(i).find('b')
        #     # print(i, oct(i)[pos_o+1:], hex(i)[pos_h+1:], bin(i)[pos_b+1:])
        #     print('{} {} {} {}'.format(i,
        #     oct(i)[oct(i).find('o')+1:],
        #     hex(i)[hex(i).find('x')+1:],
        #     bin(i)[bin(i).find('b')+1:]).center(0))
         n = number
         width = len("{0:b}".format(n))
         for i in range(1,n+1):
           print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


    if __name__ == '__main__':
        n = int(input())
        print_formatted(n)


# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
    print('Updating Monitor')


# # best practice
# n = int(raw_input())
# width = len("{0:b}".format(n))
# for i in xrange(1,n+1):
#   print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
