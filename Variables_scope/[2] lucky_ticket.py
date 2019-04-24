# Lucky ticket

def lucky(ticket):
    global lastTicket
    if len(str(ticket)) < 6:
        ticket = '0'*(6-len(str(ticket))) + str(ticket)
    k = True
    lastTicket = str(lastTicket)
    ticket = str(ticket)
    if (int(lastTicket[0]) + int(lastTicket[1]) + int(lastTicket[2])) == (int(lastTicket[3]) + int(lastTicket[4]) + int(lastTicket[5])):
        if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
            k = False
            return 'Счастливый'
        else:
            k = False
            return 'Несчастливый'
    if k:
        return 'Несчастливый'

lastTicket = 123456
print(lucky(1000))

lastTicket = 123321
print(lucky(100001))
