def solution(citations):
    # h index를 이해하는 것이 문제이다.
    for index, citation in enumerate(sorted(citations, reverse=True)):
        if index >= citation:
            return index
    return len(citations)
