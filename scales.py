import sys, time

#Create two lists
sharp_notes = ['C' , 'C#', 'D', 'D#', 'E', 'F', 'F#' , 'G', 'G#', 'A', 'A#', 'B']*3
flat_notes = ['C' , 'Db', 'D', 'Eb', 'E', 'F', 'Gb' , 'G', 'Ab', 'A', 'Bb', 'B']*3

#Get user input and verify it
tmp = int(input("Select: \n        (1) Sharps \n        (2) Flats \nEnter: "))

#Set the scale in use to the users input
if tmp == 1:
    whole_notes = sharp_notes
if tmp == 2:
    whole_notes = flat_notes

def main():
    while True:
        #Reset Scale for looping issues
        scale = 0

        #Get the scale input
        scale = int(input("Select Scale: \n      (1) Chromatic          (5) Minor \n      (2) Major Penatonic    (6) Blues Scale\n      (3) Minor Penatonic    (7) Melodic Minor\n      (4) Major              (8) Harmonic Minor\nEnter: "))

        #Scale input check
        if scale not in range(9):
            print('Invalid Input')
            print('Quitting', end='')
            for i in range(3):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(.2)
            quit()

        #Get the root input and check it to meet all conditions
        root_k = input("Select Root Note: " + str(whole_notes[0:12]) + "\nEnter: ")
        if type(root_k) != str:
            print('Invalid Input')
            print('Quitting', end='')
            for i in range(3):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(.2)
            quit()

        #Capatalize it the send it to the root input_check
        root_k = root_k.capitalize()
        input_check(root_k)
        
        #Chromatic Scale
        if scale == 1:
            print(root_k)
            print(get_chrom(root_k))

        #Maj Pent
        if scale == 2:
            print(get_maj_pent(root_k))
        
        #Min Pent
        if scale == 3:
            print(get_min_pent(root_k))

        #Maj Scale
        if scale == 4:
            print(get_maj(root_k))

        #Minor Scale
        if scale == 5:
            print(get_min(root_k))

        #Blues Scale
        if scale == 6:
            print(get_blues(root_k))

        #MM Scale
        if scale == 7:
            print(get_melodic_min(root_k))

        #HM Scale
        if scale == 8:
            print(get_harmonic_min(root_k))

        
        time.sleep(2.5)

def get_chrom(root):
    return "The " + str(root) + " Chromatic Scale: " + str(whole_notes[whole_notes.index(root): whole_notes.index(root) + 12])
    
def get_maj_pent(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Major Penatonic Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 2] + ' ' + whole_notes[ind+ 4] + ' ' +  whole_notes[ind + 7] + ' ' + whole_notes[ind + 9])
    return nm + notes

def get_min_pent(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Minor Penatonic Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 3] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 10] )
    return nm + notes

def get_maj(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Major Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 2] + ' ' + whole_notes[ind + 4] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 9] + ' ' + whole_notes[ind + 11] )
    return nm + notes

def get_min(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Minor Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 2] + ' ' + whole_notes[ind + 3] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 8] + ' ' + whole_notes[ind + 10] )
    return nm + notes

def get_blues(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Blues Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 3] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 6] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 10])
    return nm + notes

def get_melodic_min(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Melodic Minor Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 2] + ' ' + whole_notes[ind + 3] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 9] + ' ' + whole_notes[ind + 11])
    return nm + notes

def get_harmonic_min(root):
    ind = whole_notes.index(root)
    nm = 'The ' + str(root) + ' Harmonic Minor Scale: '
    notes = str(whole_notes[ind] + ' ' + whole_notes[ind + 2] + ' ' + whole_notes[ind + 3] + ' ' + whole_notes[ind + 5] + ' ' + whole_notes[ind + 7] + ' ' + whole_notes[ind + 8]+ ' ' + whole_notes[ind + 11])
    return nm + notes

def input_check(root):
    if root not in whole_notes:
        print('Invalid Input')
        print('Quitting', end='')
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.2)
        quit()


if __name__ == '__main__':
    main()

