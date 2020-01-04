from typing import List, Tuple


def is_stable_match(match: List[Tuple[int, int]], pref_a: List[List[int]], pref_b: List[List[int]]) -> bool:
    """

    @param match: A match which each match is represented by: (index, match[index]), where index is a player from
    group A, and match[index] is a player from group B
    @param pref_a: preferences for each players in the group A, the value that player i (from group A) give to player j
    (in group B) is pref_a[i][j], where 1<= value <= m
    @param pref_b: preferences for each players in the group A, the value that player i (from group B) give to player j
    (in group A) is pref_b[i][j], where 1<= value <= m
    for each players in the group B @return: True if the match is stable, False otherwise

    #Example in class where: Tomer = 0, Shlomo = 1, Raphi = 2
                            Aviva = 0, Batya = 1, Galia = 2
    >>> is_stable_match([(0, 2), (1, 1), (2, 0)], [[1, 3, 2], [3, 2, 1], [3, 1, 2]], [[1, 2, 3], [1, 3, 2],[2, 3, 1]])
    True
    """
    for i in range(len(pref_b)):  # for each player in group A
        for j in range(len(pref_b)):  # for each player in group A
            if (i, j) not in match:  # if they are not matched, then we need to check if they are unstable couple
                match_i = [match for match in match if match[0] == i][0][1]  # the match for i
                match_j = [match for match in match if match[1] == j][0][0]  # the match for j
                # if i prefers j over what he matched with and j prefers i over what he match with, then match is not
                # stable
                if pref_a[i][j] > pref_a[i][match_i] and pref_b[j][i] > pref_b[j][match_j]:
                    return False

    return True
