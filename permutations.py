"""Code to generate permutations of a string."""


def helper(string, chosen, output):
    if not string:
        output.append(chosen)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            helper(rem, chosen + [string[i]], output)


def permutation(string):
    output = []
    helper(string, [], output)
    return output
