#Ahmed Mousa: 201601381
#Eman Adel: 201902302
#These functions are for taking file names, reading, writing, and closing files
def inputfile():
    return input('Enter input file name: ')
def openinput(x):
    return open(x, 'r')
def readinput(x):
    return x.read()
def outputfile():
    return input('Enter output file name: ')
def openoutput(x):
    return open(x, 'w')
def closefile(x):
    return x.close()
#A function to remove new lines in the input files:
def removenew(x):
    if x == '\n':
        return ''
    else:
        return x
#This function checks whether the input sequence is valid:
def validsequence(x):
    c = 0
    for i in range(len(x)):
        if menu == 1 or menu == 4:
            if x[i] not in '35\'ATCG':
                c += 1
        elif menu == 2 or menu == 3:
            if x[i] not in '35\'AUCG':
                c += 1
    if (not (x[0:2] == '3\'' and x[-1:-3:-1] == '\'5')) and (not (x[0:2] == '5\'' and x[-1:-3:-1] == '\'3')):
        c += 1
    if menu == 3:
        if not(x[0:2] == '5\'' and x[-1:-3:-1] == '\'3'):
            c += 1
    if c > 0:
        print('Invalid input sequence! Or empty input file.\n'
                    'Sequence should not contain the following:\n'
                  '- Small letters\n'
                  '- Invalid base letters, including Uracil in DNA or Thymine in RNA\n'
                  '- Numbers or symbols in non-terminals\n'
                  '- Numbers or symbols other than 5\' and 3\' in terminals\n'
                  '- 3\' terminal at the beginning of translated sequence instead of 5\'')
    return c
#This function is for formatting the output in file and program:
def format(x, y):
    for i in range(len(x)):
        if (i+1) % y == 0:
            print(x[i])
            outfile.write(f'{x[i]}\n')
        else:
            print(x[i], end = '')
            outfile.write(x[i])
    print('')
#while loop for repetition unknown times:
Cont = 'y'
while Cont == 'y':
#The program starts executing by showing the menu:
    menu = int(input('Choose the desired option: \n'
                     '1- DNA transcription, 2- Reverse transcription, 3- RNA translation, 4- Get complementary DNA strand: '))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4:
        menu = int(input('Error! Please enter a valid option: '))
#First this code module for transcription, reverse transcription or complementary DNA:
    if menu == 1 or menu == 2 or menu == 4:
#Terminal function to reverse input terminals in the output
        def terminal(x):
            if x == "3":
                return "5"
            elif x == "5":
                return "3"
            elif x == "'":
                return "'"
            else:
                return''
#Functions for transcription and reverse transcription. They turn the base into its correspondent.
        def transcription(x):
            if x == 'A':
                return 'U'
            elif x == 'T':
                return 'A'
            elif x == 'G':
                return 'C'
            elif x == 'C':
                return 'G'
            else:
                return ''
        def retranscription(x):
            if x == 'A':
                return 'T'
            elif x == 'U':
                return 'A'
            elif x == 'G':
                return 'C'
            elif x == 'C':
                return 'G'
            else:
                return''
#Function for getting the complementary DNA starnd:
        def complement(x):
            if x == 'A':
                return 'T'
            elif x == 'T':
                return 'A'
            elif x == 'G':
                return 'C'
            elif x == 'C':
                return 'G'
            else:
                return ''
#The program takes input file names and opens them for reading:
        inname = inputfile()
        infile = openinput(inname)
        inputseq = readinput(infile)
        inputmodified = ''
#Removing new lines and checking validity of input:
        for i in inputseq:
            inputmodified += removenew(i)
        while validsequence(inputmodified) > 0:
            inname = inputfile()
            infile = openinput(inname)
            inputseq = readinput(infile)
            inputmodified = ''
            for i in inputseq:
                inputmodified += removenew(i)
            validsequence(inputmodified)
#Taking output file name and opening it for writing:
        outname = outputfile()
        outfile = openoutput(outname)
        outputseq = ""
#The printed and written phrases, and functions diverge between transcription and reverse transcription
        f = int(input('Enter characters per output line: '))
        if menu == 1:
            outfile.write('RNA transcript:\n')
            print('DNA sequence is:\n ', inputmodified)
            print('RNA transcript: ')
            for i in inputmodified:
                outputseq += terminal(i)
                outputseq += transcription(i)
        elif menu == 2:
            outfile.write('DNA sequence:\n')
            print('RNA transcript is:\n', inputmodified)
            print('DNA sequence: ')
            for i in inputmodified:
                outputseq += terminal(i)
                outputseq += retranscription(i)
        elif menu == 4:
            outfile.write('Complementary DNA strand:\n')
            print('Input DNA: ', inputmodified)
            print('Complementary DNA: ')
            for i in inputmodified:
                outputseq += terminal(i)
                outputseq += complement(i)
#Output part where output is printed in program and file:
        format(outputseq, f)
        closefile(infile)
        closefile(outfile)
#This is the translation part:
    if menu == 3:
#This function reads the codon and returns the corresponding one-letter amino acid
        def codon(x):
            if x == 'UAA' or x == 'UGA' or x == 'UAG':
                return ''
            elif x == 'GCU' or x == 'GCC' or x == 'GCA' or x == 'GCG':
                return 'A'
            elif x == 'CGU' or x == 'CGC' or x == 'CGA' or x == 'CGG' or x == 'AGA' or x == 'AGG':
                return 'R'
            elif x == 'AAU' or x == 'AAC':
                return 'N'
            elif x == 'GAU' or x == 'GAC':
                return 'D'
            elif x == 'UGU' or x == 'UGC':
                return 'C'
            elif x == 'CAA' or x == 'CAG':
                return 'Q'
            elif x == 'GAA' or x == 'GAG':
                return 'E'
            elif x == 'GGU' or x == 'GGC' or x == 'GGA' or x == 'GGG':
                return 'G'
            elif x == 'CAU' or x == 'CAC':
                return 'H'
            elif x == 'AUU' or x == 'AUC' or x == 'AUA':
                return 'I'
            elif x == 'CUU' or x == 'CUC' or x == 'CUA' or x == 'CUG' or x == 'UUA' or x == 'UUG':
                return 'L'
            elif x == 'AAA' or x == 'AAG':
                return 'K'
            elif x == 'AUG':
                return 'M'
            elif x == 'UUU' or x == 'UUC':
                return 'F'
            elif x == 'CCU' or x == 'CCC' or x == 'CCA' or x == 'CCG':
                return 'P'
            elif x == 'UCU' or x == 'UCC' or x == 'UCA' or x == 'UCG' or x == 'AGU' or x == 'AGC':
                return 'S'
            elif x == 'ACU' or x == 'ACC' or x == 'ACA' or x == 'ACG':
                return 'T'
            elif x == 'UGG':
                return 'W'
            elif x == 'UAU' or x == 'UAC':
                return 'Y'
            elif x == 'GUU' or x == 'GUC' or x == 'GUA' or x == 'GUG':
                return 'V'
#This function removes 3' and 5' terminal if entered:
        def removeterminal(x):
            if x == "3":
                return ''
            elif x == "5":
                return ''
            elif x == "'":
                return ''
            else:
                return x
#The program takes input file name and opens for reading:
        inname = inputfile()
        infile = openinput(inname)
        inputseq = readinput(infile)
        inputmodified = ''
#Removing new lines and checking validity of input:
        for i in inputseq:
            inputmodified += removenew(i)
        while validsequence(inputmodified) > 0:
            inname = inputfile()
            infile = openinput(inname)
            inputseq = readinput(infile)
            inputmodified = ''
            for i in inputseq:
                inputmodified += removenew(i)
            validsequence(inputmodified)
#Removing terminal from input sequence:
        rna = ""
        for i in inputmodified:
            rna += removeterminal(i)
#Taking output file name and opening it for writing:
        ptnseq = ""
        outname = outputfile()
        outfile = openoutput(outname)
#This part translates the RNA sequence:
        for i in range(0, len(rna), 3):
            ptnseq += codon(rna[i:i+3])
            if codon(rna[i:i+3]) == '':
                break
#Check whether the sequence is translated properly or a stop codon is in the middle:
        if len(ptnseq) < (len(rna)/3-1):
            print(f'Stop codon after: {len(ptnseq)*3} bases.')
            outfile.write(f'Stop codon after: {len(ptnseq)*3} bases.\n')
#Output part where output is printed in program and file:
        f = int(input('Enter characters per output line: '))
        print('RNA sequence is:\n', inputmodified)
        print('Protein sequence:')
        outfile.write('Protein sequence:\n')
        format(ptnseq, f)
        closefile(infile)
        closefile(outfile)
#The user is asked if they wish to continue:
    Cont = input('Continue? y/n: ')
    while Cont != 'y' and Cont != 'n':
        Cont = input('Error! Enter y/n: ')

