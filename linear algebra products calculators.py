#################################################################
# FILE : ex3.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex3 2021
# DESCRIPTION: functions the required in the exercise description.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
# NOTES:
#################################################################


def input_list():
    """
    this function receives continues input of strings of numbers and builds a list with all of its numbers.
    :return: the list of the numbers inputted with their sum at the last.
    """
    sum_list = []
    input_list_helper(sum_list)
    if len(sum_list) == 0:
        return sum_list
    list_sum = 0
    for num in sum_list:
        list_sum += num
    sum_list.append(list_sum)
    return sum_list


def input_list_helper(sum_list):
    """
    this is a recursive helper function to insert the numbers inputted in the function above.
    :param sum_list: a list to insert the numbers in.
    :return: the list of the numbers inputted as strings.
    """
    input_str = input()
    if input_str == '':
        return sum_list
    sum_list.append(float(input_str))
    return input_list_helper(sum_list)


def inner_product(vec_1, vec_2):
    """
    this function calculate the inner product of any pair of vectors.
    :param vec_1: a list represent the first vector to multiply.
    :param vec_2: a list represent the second vector to multiply.
    :return: a scalar equals to the inner product of the two vectors.
    """
    if len(vec_1) != len(vec_1):
        return None
    elif len(vec_1) == 0 or len(vec_2) == 0:
        return 0
    if len(vec_1) == len(vec_2):
        return inner_product_helper(vec_1, vec_2)


def inner_product_helper(vec_1, vec_2):
    """
    this is a helper function to the function above, to calculate the inner product if needed.
    :param vec_1: a list represent the first vector to multiply.
    :param vec_2: a list represent the second vector to multiply.
    :return: a scalar equals to the inner product of the two vectors.
    """
    product = 0
    for i in range(len(vec_1)):
        product += vec_1[i] * vec_2[i]
    return product


def sequence_monotonicity(sequence):
    """
    this function checks whether a list is monotonic increasing or decreasing, strictly or non-strictly.
    :param sequence: a list represent set of numbers.
    :return: a list of 4 boolean values represent each definition correctness.
    """
    ans = [True, True, True, True]
    if len(sequence) <= 1:
        return ans
    for i in range(len(sequence) - 1):
        sequence_monotonicity_helper(sequence[i], sequence[i + 1], ans)
    return ans


def sequence_monotonicity_helper(num_1, num_2, ans):
    """
    this is a helper function to the function above to determine whether each one of the definitions is contradicted.
    :param num_1: one of the sequence numbers.
    :param num_2: the following number in the sequence.
    :param ans: a list of 4 boolean values represent each definition correctness.
    :return: a list of 4 boolean values represent each definition correctness.
    """
    if num_1 > num_2:
        ans[0], ans[1] = False, False
    elif num_1 < num_2:
        ans[2], ans[3] = False, False
    elif num_1 == num_2:
        ans[3], ans[1] = False, False


def monotonicity_inverse(def_bool):
    """
    this function return an example for a sequence the stands with the definition set if found.
    :param def_bool: a list of 4 boolean values represent each definition.
    :return: a set with example for a sequence the stands with the definition set if found, None otherwise.
    """
    if def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    elif def_bool == [True, False, False, False]:
        return [1, 2, 2, 4]
    elif def_bool == [False, False, True, False]:
        return [4, 2, 2, 1]
    elif def_bool == [False, False, True, True]:
        return [4, 3, 2, 1]
    elif def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    else:
        return None


def is_prime(n):
    """
    this function helps the function bellow to determine whether a number is prime, in a fast way.
    :param n: number to be checked.
    :return: True if the number is prime number, False otherwise.
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
            else:
                return True


def primes_for_asafi(n):
    """
    this function finds the first n prime numbers, and returns them as a list.
    :param n: number of first numbers required
    :return: a list of first n prime numbers.
    """
    primes_list = []
    if n == 0:
        return primes_list
    primes_list.append(2)
    if n == 1:
        return primes_list
    primes_list.append(3)
    if n == 2:
        return primes_list
    i = 5
    while len(primes_list) < n:
        if is_prime(i):
            primes_list.append(i)
        i += 2
    return primes_list


def sum_of_vectors(vec_lst):
    """
    this function calculates the vector which is the sum of the vectors it receives.
    :param vec_lst: list of vectors to be summed.
    :return: the vector represent the sum of the vectors inserted.
    """
    if len(vec_lst) == 0 or len(vec_lst[0]) == 0:
        return []
    output_vec = []
    for i in range(len(vec_lst[0])):
        sum_i = 0
        for vec in vec_lst:
            sum_i += vec[i]
        output_vec.append(sum_i)
    return output_vec


def num_of_orthogonal(vectors):
    """
    this function receives list of vectors and checks how manny of them are orthogonal pair.
    :param vectors: a list of vectors.
    :return: the number of orthogonal pairs in the vectors inserted.
    """
    all_orthogonal = 0
    orthogonal_track = []
    i = 0
    while i < len(vectors):
        for j in range(len(vectors)):
            if i != j and inner_product(vectors[i], vectors[j]) == 0 and (j, i) not in orthogonal_track:
                all_orthogonal += 1
                orthogonal_track.append((i, j))
        i += 1
    return all_orthogonal
