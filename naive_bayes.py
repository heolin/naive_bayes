#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import utils
import corpus
import argparse
import probability as p

#Dla każdego feature zrób rozkład prawdopodobieństwa opisany przez średnią i odchylenie standardowe (jeżeli używamy prawdopodobieństwa gaussa) i naucz się tego dla każdej klasy.
#Potem dla wektora wejściowego sprawdzaj dla każdej wartości z feature jakie prawdopodobieństwo ma dana wartość z wektora wejściowego na podstawie rozkładu prawdopodobieństwa wyuczonego dla danej klasy.
#Wymnóż wszystkie te prawdopodobieństwa (bo zdarzenia sią niezależne)
#Wybierz klase o największym prawdopodobieństwie

def calculate_class_probabilities(summaries, input_vector):
    probabilities = {}
    for class_value, class_summaries in summaries.iteritems():
        probabilities[class_value] = 1
        for i in xrange(len(class_summaries)):
            mean, std_dev = class_summaries[i]
            x = input_vector[i]
            probabilities[class_value] *= p.gauss_probability(x, mean, std_dev)
    return probabilities


def predict(summaries, input_vector):
    probabilities = calculate_class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.iteritems():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label


def predict_set(summaries, input_set):
    predictions = []
    for i in range(len(input_set)):
        result = predict(summaries, input_set[i])
        predictions.append(result)
    return predictions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', help="Input csv file with data.")
    args = parser.parse_args()

    dataset = utils.load_csv(args.input_file)
    train_set, test_set = corpus.split_dataset(dataset, 0.67)
    separated = corpus.separate_by_class(train_set)
    summaries = corpus.summarize_by_class(train_set)
    predictions = predict_set(summaries, test_set)
    accuracy = utils.get_accuracy(test_set, predictions)
    print('Accuracy: {0}%').format(accuracy)

if __name__ == "__main__":
    main()
