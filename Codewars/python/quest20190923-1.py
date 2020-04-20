# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python

# print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") == \
#             "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")
# h|m|s
import math

# strg = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
# # strg = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"
# strg = strg.split(',')
#
# # print(strg[0].split('|'))
# seconds = []
# for runner in strg:
#     seconds.append(float(runner.split('|')[2]) + \
#                    float(runner.split('|')[1]) * 60 + \
#                    float(runner.split('|')[0]) * 60 * 60)
#
# # print(seconds)
#
# range = max(seconds)-min(seconds)
# average = sum(seconds)/len(seconds)
#
# seconds_sorted = sorted(seconds)
#
# pos = math.floor((len(seconds)+1)/2)-1
# if (len(seconds) % 2) != 0: median = seconds_sorted[pos]
# else: median = 0.5*(seconds_sorted[pos]+seconds_sorted[pos+1])
#
# results = [range, average, median]
#
# strgs = []
# for result in results:
#     range = result/(60 * 60)
#     range_h = math.floor(range)
#     range_m = (range - range_h)*60
#     range_m = math.floor(range_m)
#     range_s = ((range - range_h)*60 - range_m)*60
#     range_s = math.floor(range_s)
#     strg = '{}|{}|{}'.format(range_h,range_m,range_s)
#     strgs.append(strg)
# print(strgs)
# print("Range: {} Average: {} Median: {}".format(strgs[0],strgs[1],strgs[2]))

def stat(measures):
    if len(measures) > 0:
        seconds = sorted([float(runner.split('|')[2]) + \
                   float(runner.split('|')[1]) * 60 + \
                   float(runner.split('|')[0]) * 60 * 60 for runner in measures.split(',')])

        # Calculate Stats
        range = max(seconds)-min(seconds)
        average = sum(seconds)/len(seconds)
        pos = math.floor((len(seconds)+1)/2)-1
        if (len(seconds) % 2) != 0: median = seconds[pos]
        else: median = 0.5*(seconds[pos]+seconds[pos+1])

        # Reformat Results
        results = [range, average, median]
        hhmmss = []
        for result in results:
            hh = math.floor(result/60**2)
            mm = math.floor(result/60) - math.floor(result/60**2)*60
            ss = math.floor(result - \
                (math.floor(result/60) - math.floor(result/60**2)*60)*60 - \
                (math.floor(result/60**2))*60**2)
            hh = '0'+ str(hh) if len(str(hh)) == 1 else str(hh)
            mm = '0'+ str(mm) if len(str(mm)) == 1 else str(mm)
            ss = '0'+ str(ss) if len(str(ss)) == 1 else str(ss)
            hhmmss.append('{}|{}|{}'.format(hh,mm,ss))

        return "Range: {} Average: {} Median: {}".format(hhmmss[0],hhmmss[1],hhmmss[2])
    if len(measures) == 0: return measures



    # print(range,average,median)
# stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")
stat("")
 # "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")










# range = range/(60 * 60)
# range_h = math.floor(range)
# range_m = (range - range_h)*60
# range_m = math.floor(range_m)
# range_s = ((range - range_h)*60 - range_m)*60
# range_s = math.floor(range_s)
# print(((range - range_h)*60 - range_m)*60)
# print(range_h,range_m,range_s)
