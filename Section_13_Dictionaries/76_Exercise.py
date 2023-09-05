"""
Exercise No. 76

The following dictionary is given:

    project_ids = {
        '01': 'open',
        '02': 'in progress',
        '03': 'in progress',
        '04': 'completed',
    }

Extract a list of unique values (sorted alphabetically) from the project_ids dictionary and print it to the console.

Expected result:

    ['completed', 'in progress', 'open']
"""
# Solution I
project_ids = {
    '01': 'open',
    '02': 'in progress',
    '03': 'in progress',
    '04': 'completed',
}

print(sorted(set(project_ids.values())))


# Solution II
project_ids = {
    '01': 'open',
    '02': 'in progress',
    '03': 'in progress',
    '04': 'completed',
}

result = list(set(project_ids.values()))
result.sort()
print(result)
