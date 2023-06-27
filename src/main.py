import itertools


def read_input_file(file_name):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        input_data = []
        for line in lines:
            input_data.append(line.replace('[', '').replace(']', '').replace(' ', '').split(','))
    return input_data


def get_comb_pairwise(combinations: list[tuple]):
    comb_pairwise: dict[tuple, list[tuple]] = {}
    for comb in combinations:
        comb_pairwise.setdefault(comb, list(itertools.combinations(itertools.chain(comb), 2)))

    return comb_pairwise


def generate_pairwise_combinations(input_data):
    combinations: list[tuple] = list(itertools.product(*input_data))
    pairwise: list[tuple] = list(itertools.combinations(itertools.chain(*input_data), 2))
    result: list[tuple] = []
    comb_pairwise: dict[tuple, list[tuple]] = get_comb_pairwise(combinations)
    for _ in pairwise:
        first_comb: tuple = list(comb_pairwise.keys())[0]
        first_comb_pir: list[tuple] = comb_pairwise[first_comb]
        if len(first_comb_pir) == 0:
            break
        curr_pir: set[tuple] = set()
        for pir in first_comb_pir:
            curr_pir.add(pir)

        for pir in curr_pir:
            for comb in comb_pairwise:
                if pir in comb_pairwise[comb]:
                    comb_pairwise[comb].remove(pir)

        result.append(first_comb)
        comb_pairwise = dict(sorted(comb_pairwise.items(), key=lambda x: len(x[1]), reverse=True))

    return result


def print_pairwise_combinations(combinations):
    for combination in combinations:
        print('  '.join(combination))


def main():
    input_data: list[list[str]] = read_input_file('input.txt')
    pairwise_combinations = generate_pairwise_combinations(input_data)
    print_pairwise_combinations(pairwise_combinations)


if __name__ == '__main__':
    main()
