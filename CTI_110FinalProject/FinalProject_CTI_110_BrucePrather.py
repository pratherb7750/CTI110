#This My Final Project for CTI-110.  It is a simple subnet calculator that will accept an integer input for the 4th
#octets of the given classless network and subnet mask. 
#CTI-110 - Final Project
#July 20
#Bruce Prather

def main():
    try:
        print ('THIS IS A SIMPLE SUBNET CALCULATOR THAT WILL HELP YOU CALCULATE SUBNETS IN THE LAST OCTET.')
        print()
        
        #get the first 3 octets of the network:
        net_addr= input('What are the first 3 octets of your network address? ')
        
        #get the last octet as an integer:
        last_oct= int(input('What is the last octet?(Do not include the decimal) '))
        
        #A network address must be either a 0 or an even number:
        #This will validate the last octet, if not valid program will start over.
            
        if is_valid_ntwk(last_oct) == False:
            print('This is not a vald subnet')
            print ("let's start over with the correct network data")
            main()
        

        print ()    

        #get the last octet of the subnet mask, (the first 2 is 255.255.255):
        sub_mask = int(input('What is the last octet of the subnet mask? '))
        
        #Make sure that the subnet mask is valid, if not the program will start over.
        if is_valid_subnet(sub_mask) == False:
            print('This not a valid subnet mask')

        if sub_mask == 0:
            print()
        elif last_oct % (256-sub_mask) ==0:
            print()
        
        else:
            print ('THIS IS NOT A LEGITIMATE NETWORK/SUBNET-MASK COMBINAION!')
            print ("let's start over with the correct network data")
            print()
            print()
            main()
            
            
            
        
        #this calculates the prefix, the increment, and the maximum amount of host allowed:
        prefix = maskToPref(sub_mask)
        incr = 2**(32-prefix)
        max_host= incr-2

        #show the network prefix            
        print ('Your network prefix is /',prefix)
        
        #show the maximum amount of host allowed on this network
        print ('The maximum amount of host that you are allowed is ' , max_host)
        host= int(input('How many usable host does your subnet require? '))

        #Do not allow input of too many host
        while host > max_host:
            print('That is too many host for your network')
            host= int(input('How many usable host does your subnet require? '))

        #Takes the amount of needed host and returns the valid range.
        incr = calc_incr(host)
        print ()

        #Inform the user of his valid subnet range.
        print('Your subnet is' , net_addr ,'.' , last_oct , 'thorough', net_addr ,'.' , last_oct + incr -1)

        print('That gives you' , incr - 2 , 'usable host for this network')


        

        #This determines the new last octet for the next network.
        last_oct= last_oct + incr
        print ()

        #If the new last octet is 255, Then there are no more subnets that can be created.
        if last_oct > 255:
            print ('There are no more sub-nets left in this range')
            print()

        #This tells the  user what his next network is.
        else:
            print ('The next network is ' , net_addr , '.' , last_oct)

        #This tells the user what his new prefix is and the subnet mask
        
            prefix = calc_prefix(incr)
            print ()
            print ('The new network prefix is /',prefix,'which is the subnet mask 255.255.255.' , 256 -(2**(32-prefix)))
            print()
        
        
        
              
    except:
        print('an error occured')

        
    #Give the user a choice to calculate another subnet or to exit the program
    doOver()


def maskToPref(mask):
    if mask == 0:
        pref = 24
    if mask == 128:
        pref = 25
    if mask == 192:
        pref = 26
    if mask == 224:
        pref = 27
    if mask == 240:
        pref = 28
    if mask == 248:
        pref = 29
    if mask == 252:
        pref = 30
    if mask == 254:
        pref = 31
    return pref

def calc_incr(host):
    if host > 126:
        incr = 256
    elif host < 127 and host > 62:
        incr = 128
    elif host < 63 and host > 30:
        incr = 64
    elif host < 31 and host > 14:
        incr = 32
    elif host < 15 and host > 6:
        incr = 16
    elif host < 7 and host > 2:
        incr = 8
    elif host == 2:
        incr = 4
    
    return incr

def calc_prefix(incr):
    if incr == 128:
        prefix = 25
    elif incr == 64:
        prefix = 26
    elif incr == 32:
        prefix = 27
    elif incr == 16:
        prefix = 28
    elif incr == 8:
        prefix = 29
    elif incr == 4:
        prefix = 30
    elif incr == 2:
        prefix = 31
    return prefix


def is_valid_subnet(sub_mask):
    if sub_mask==128:
        return True
    elif sub_mask==192:
        return True
    elif sub_mask==224:
        return True     
    elif sub_mask==240:
        return True
    elif sub_mask==248:
        return True
    elif sub_mask==252:
        return True   
    elif sub_mask==254:
        return True
    else:
        return False

def is_valid_ntwk(last_oct):
    
    
    if last_oct ==0:
    	return True
    elif last_oct % 2 ==0:
        return True
    else:
        return False




def doOver():
    doOver= input(str('Would you like to calculate another subnet? Please enter y or n  '))
    if doOver == 'y' or doOver == 'Y':
        print()
        print()
        main()
    else:
        print('Thanks for using the Subnet Calculator')
        print ('Please press return to EXIT')
        
exit
    

    


main()
