donor_data = [('Charly',[100,120,110]),('Andrew',[80,90,100]),('Jacob',[400,300,350]),
              ('Charlie',[125, 100]), ('Jack',[75,30])]


def main():
    """
    The script should prompt the user (you) to choose from a menu of 3 actions:
    “Send a Thank You”, “Create a Report” or “quit”.
    :return:
    """
    while True:
        prompt = input('\n'.join(("Please choose from below","1: Thank You","2: Create a Report","3: quit",">>> ")))

        if prompt == '1':
            print('Your answer is {}'.format(prompt))
            name = input('Enter your full name: ')
            print('You entered {}'.format(name))
            while name.lower()=="list":
                print('\n'.join([i[0] for i in donor_data]))
                name = input('Enter your full name: ')
            donation = int(input("Donation amount:"))

            for i in range(len(donor_data)):
                if name in donor_data[i]:
                    donor_data[i][1].append(donation)
                elif name not in [i[0] for i in donor_data]:
                    donor_data.append((name, [donation]))
            print(
                "Dear {0}, Thank you for your generous donation of {1}! We will be sure to put"
                " it to good use! Sincerely, Your Local Charity".format(
                    name, "{0:.2f}".format(donation)))

        elif prompt == '2':
            print('You are asking to create a report')
            numdonor = []
            totaldonation = []
            namedonor = []
            average = []
            for i in donor_data:
                totaldonor = len(i[1])
                numdonor.append(totaldonor)
                v = sum(i[1])
                totaldonation.append(v)
                k = i[0]
                namedonor.append(k)
                avg = v / totaldonor
                average.append(avg)
            titles = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
            lst = sorted(list(zip(namedonor, totaldonation, numdonor, average)), key=lambda x: x[1:], reverse=True)
            data = [titles] + lst
            for i, d in enumerate(data):
                line = '| '.join(str(x).ljust(12) for x in d)
                print(line)
        else:
            quit()


if __name__ == '__main__':
    print(main())

