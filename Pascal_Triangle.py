def pascal_triangle(num):
    result = [[1]]

    for i in range(1, num):
        row = [1]

        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])

        row.append(1)
        result.append(row)

    return result


print(pascal_triangle(5))
