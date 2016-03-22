#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
import probability as p

def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]


def separate_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        separated.setdefault(vector[-1], [])
        separated[vector[-1]].append(vector)
    return separated


def summarize(dataset):
    return [(p.mean(attribute), p.std_dev(attribute)) for attribute in zip(*dataset)][:-1]


def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = {}
    for class_value, instances in separated.iteritems():
        summaries[class_value] = summarize(instances)
    return summaries

