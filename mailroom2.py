donor_data = [('Charly', [100, 120, 110]), ('Andrew', [80, 90, 100]), ('Jacob', [400, 300, 350]),
              ('Charlie', [125, 100]), ('Jack', [75, 30])]

while True:
    prompt = input('\n'.join(("Please choose from below", "1: Send a Thank You", "2: Create a Report", "3: quit", ">>> ")))
    namedonor = [i[0] for i in donor_data]

    if prompt == '1':
        name = input('Enter your full name: ')
        while name.lower() == "list":
            print('\n'.join(namedonor))
            name = input('Enter your full name: ')
        donation = int(input("Donation amount:"))

        if name in namedonor:
            donor_data[namedonor.index(name)][1].append(donation)
        else:
            donor_data.append((name, [donation]))
        print(
            "Dear {0}, Thank you for your generous donation of {1:.2f}! We will be sure to put"
            " it to good use! Sincerely, Your Local Charity"
            .format(name, donation))

    elif prompt == '2':
        numdonor = [len(i[1]) for i in donor_data]
        totaldonation = [sum(i[1]) for i in donor_data]
        average = [sum(i[1])/len(i[1]) for i in donor_data]
        titles = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        data = [titles] + sorted(list(zip(namedonor, totaldonation, numdonor, average)), key=lambda x: x[1:], reverse=True)
        for i, d in enumerate(data):
            line = '| '.join(str(x).ljust(12) for x in d)
            print(line)
    else:
        quit()

