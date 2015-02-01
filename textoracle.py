import random
import os
textslist = os.listdir('texts')

import os
os.system('clear')

person_counter = random.randint(0,1)
counter = 0
good_guess = 0

for x in range(0,20):

    while good_guess == 0:
    
        chosentext = random.choice(textslist)
        
        from nltk import sent_tokenize
        text = open("texts/" + chosentext, "r")
        newtext = text.read()
        text.close()
        
        wholetext = sent_tokenize(newtext)
        
        import random
        import string
    
        # Choose random place in context
        contextrand = random.randint(10, len(wholetext))
        #print contextrand # Print chosen random number
        
        # Choose context from tokenized large file
        sentences_of_context = 1
        context = wholetext[contextrand:contextrand + sentences_of_context]
        
        # Choose and format selection sentence.
        initialpick = str(context[sentences_of_context / 2])
        initialpick = initialpick.replace('\n', ' ').replace('\r', '')
        #print initialpick + '\n'
        
        # Format selection context.
        context = ' '.join(context)
        context = context.replace('\n', ' ').replace('\r', '')
        #print context     
                
        initialpick = str(initialpick)
        initialpick = initialpick.translate(string.maketrans("\n\r", "  "))
    
    ### Create the blanks
    
        correctlength = 0
        wordattempts = 0
        desired_length = 7
        
        while correctlength == 0 and wordattempts < 5 and desired_length > 3:
    
            cellwords = ''.join(c if c.isalnum() else ' ' for c in initialpick).split()
            count = len(cellwords)
            #print initialpick
            #print cellwords
            #print count
            
            randword = random.randint(1,(count + 1)) - 2
            #print randword
    
            #print 'Randword = ' + str(randword) 
                
            sentquestion = initialpick
            wordattempts += 1
    
            #print 'Attempts: ' + str(wordattempts)        
            ##print chosentext
            #print 'Number of words in sentence: ' + str(count) 
            ##print sentquestion
            #print 'Chosen word: ' + str(cellwords[randword])
            
            if wordattempts == 4:
                    desired_length -= 1
                    wordattempts = 0
                                                                                        
            if len(cellwords[randword]) > desired_length:
                sentquestion = sentquestion.replace(cellwords[randword], "_________")    
                correctlength = 1
                        
        print '\n' + sentquestion
    
        if person_counter %2 == 0:
            persons_turn = 'Emily'
        else:
            persons_turn = 'Christian'
        
        guess = raw_input (persons_turn + ', What is your guess: ')
        person_counter += 1 # Change name

        if guess == 'x':
            import sys
            sys.exit()
        print '            Answer: ' + cellwords[randword] + '\n'      
    
        text = chosentext.replace('.txt', '') 
        print text + '\n' 
    
        print initialpick
        
        if guess == '':
            break
        
        if person_counter %2 == 0:
            persons_turn = 'Emily'
        else:
            persons_turn = 'Christian'
        
        question = raw_input (persons_turn + ', What is your question: ')  
        person_counter += 1 # Change name
        if question == 'x':
            import sys
            sys.exit()                         
        
        answer = ''
        pastnum = 0
        futnum = 0
        indentcount = 0
        
        #print '\n' + context
    
        if person_counter %2 == 0:
            persons_turn = 'Emily'
        else:
            persons_turn = 'Christian'           
                
        while answer == '':
            
            #print "Random Context #: " + str(contextrand)
            #print "Sentences of Context: " + str(sentences_of_context)
    
            # Double the size of the context
    
            import os
            os.system('clear')
            
            print text
            
            #if indentcount %5 == 4:
            #    print '\n\n'
            
            #for x in range(0,counter)
            #    context = wholetext[(contextrand - para * x):(contextrand + futnum)]
            #   
            #    for y in range(0,counter %3)
                    

            textblock0 = contextrand
            textblock1 = textblock0
            textblock2 = textblock0 + 2*futnum + 1          
            textblock3 = textblock0 + 2*futnum + 3        
            context = wholetext[textblock1:textblock2]
            #print counter
            #print 'Textblock 1 ' + str(textblock1)
            #print 'Textblock 2 ' + str(textblock2)
            #print 'Futnum : ' + str(futnum)
            context = ' '.join(context)
            context = context.replace('\n', ' ').replace('\r', ' ')
            print '\n' + context + '\n'
            
            context = wholetext[textblock2:textblock3]
            context = ' '.join(context)
            context = context.replace('\n', ' ').replace('\r', ' ')            
            #print 'Textblock 3 ' + str(textblock3)
            #print 'Textblock 4 ' + str(textblock4)
            #print 'Futnum :' + str(futnum)
            print context
            #if indentcount > 4:
            #    context.insert(5, '\n')    
            
            futnum += 1                         
    
            answer = raw_input(persons_turn + ", "+ question + ' ')    
            
            if answer != '':
                person_counter += 1
                if person_counter %2 == 0:
                    persons_turn = 'Emily'
                else:
                    persons_turn = 'Christian'    
                break
                
            counter += 1
            #indentcount += 1
            
            #print '\n'   
                    
            ## Choose and format selection sentence.
            #additionalpick = str(context[sentences_of_context / 2])
            #additionalpick = initialpick.replace('\n', ' ').replace('\r', '')
            
            #print '[Type m for more context]'
    
        
        #print text     
        
        context = wholetext[textblock1:textblock3]
        context = ' '.join(context)
        context = context.replace('\n', ' ').replace('\r', ' ')
        
        answers_file = open('answers_file.txt','a')
        answers_file.write('\n' + sentquestion + '\n\n' 
        + '     Guess: ' + guess + '\n' 
        + '     Answer:' + cellwords[randword] +  '\n\n'
        + '   ' + context + '\n\n'
        + '   ' + text + '\n\n'
        + '     Question: ' + question + '\n'
        + '     Answer: ' + answer + '\n')
    
        answers_file.close()  

