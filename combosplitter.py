with open('raw.txt','rt') as combo:
    with open('usernames.txt','wt') as x:
        with open('passwords.txt','wt') as y:
            for line in combo:
                combo = line.strip().split(':')
                x.write(combo[0] + '\n')
                y.write(combo[1] + '\n') 