def bananas_counting(min_quantity, max_quantity):
    preresults = []
    for number in range(min_quantity, max_quantity):
        if (number-1) % 3 == 0:
            preresults.append(number)
    def night_deviding(babanas):
        results = []
        for quantity in babanas:
            checking_quantity = quantity
            for _ in range(3):
                checking_quantity = (checking_quantity-1) / 3 * 2
            if (checking_quantity-1) % 3 == 0:
                # if we know from task that there is only one possible decision
                # we just can return quantity variable (delete results list and delete loop from line 22)
                results.append(quantity)
        return results
    return night_deviding(preresults)


if __name__ == '__main__':
    results = bananas_counting(50, 100)
    for result in results:
        print(result)
