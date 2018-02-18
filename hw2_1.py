def calculate_probability_of_no_coincident(number_of_things_to_be_chosen, possible_outcome):
    probability_of_no_coincident = 1.0

    if number_of_things_to_be_chosen > 1:
        for i in range(2, number_of_things_to_be_chosen + 1):
            probability_of_no_coincident = \
                (1.0 - ((i - 1) / float(possible_outcome))) * probability_of_no_coincident
    
    return probability_of_no_coincident


def main():
    possible_outcome = int(raw_input("Number of possible outcome: "))
    number_of_things_to_be_chosen = int(raw_input("Number of things to be chosen arbitrarily: "))

    probability_of_no_coincident = \
        calculate_probability_of_no_coincident(number_of_things_to_be_chosen, possible_outcome)
    
    output_format = "The probability of n chosen things are difference is {}"
    print output_format.format(probability_of_no_coincident)


if __name__ == '__main__':
    main()