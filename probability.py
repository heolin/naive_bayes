#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import operator
import math

def mean(l):
    return sum(l) / float(len(l))

def median(l):
    id1 = int(math.floor(len(l)/float(2)))
    id2 = id1
    if len(l) % 2 == 0:
        id2 -= 1
    l_sorted = sorted(l)
    return float(l_sorted[id1] + l_sorted[id2]) / float(2)

def std_dev(l):
    m = mean(l)
    s = sum([(xi - m)**2 for xi in l])
    sn = math.sqrt(s/float(len(l)))
    return sn

def mean_error(l):
    m = mean(l)
    s = sum([abs(xi - m) for xi in l])
    return s/float(len(l))

def var(l):
    m = mean(l)
    s = sum([(xi - m)**2 for xi in l])
    return s/float(len(l))

def geo_mean(l):
    return reduce(operator.mul, l, 1) ** (float(1)/float(len(l)))

def weighted_mean(l, w):
    ww = float(sum(w))
    return sum([a * b for a, b in zip(l, w)]) / ww

def gauss_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def main():
    l = [850, 870, 950, 1000, 1050, 1080, 1090, 2700, 2900, 7200]
    print "mean: ", mean(l)
    print "median: ", median(l)
    print "mean_error: ", mean_error(l)
    print "var: ", var(l)
    print "std_dev:", std_dev(l)

if __name__ == "__main__":
    main()

