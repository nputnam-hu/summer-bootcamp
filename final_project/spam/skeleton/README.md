# Summer Bootcamp Final Project: spam

## Instalation
Run in your terminal:
```bash
$ wget https://github.com/nputnam-hu/summer-bootcamp/edit/master/final_project/spam/spam_skeleton.zip # (or just download the file via github)
$ unzip spam_skeleton.zip
$ rm spam_skeleton.zip
$ mv spam_skeleton spam
$ cd spam
$ chmod a+x setup.sh
$ ./setup.sh
```
This will install all of the dependices you need and download the training data for you in the corpus/ directory

Next, go to [this guide made by google](https://developers.google.com/gmail/api/quickstart/python) and go through step 1 _only_.  This will get your gmail account linked together with the app. Once you have have the client_secret.json in the spam/ directory, run in your terminal:
```
$ python email_getter.py
```
This should open up a google window that will let you enter in your login credentials and authorize your app.  If not, it should happen the first time you try to use the app with the code you have written.

## Motivation
**Email** spam, also known as **junk email**, is a type of electronic spam where unsolicited messages are sent by email.  Essentially since email existed, so did spam, and with spam often came offensive content, scams, and malware.  As a result, significant effort has been put in by email companies such as Google to algorithmically detect spam and filter it away from user's regular inboxes.

While initial efforts were crude, in recent years google has implemented advanced machine learning algorithms that use statistical methods and raw computing power to algorithmically detect spam email with a high degree of precision.  Using the python module, `nltk`, we can attempt ourselves to build a machine-learning-based program to determine if a given email message is spam or not by _training_ on the data provided for you in the corpus directory.  If you look inside you'll see two directories: spam, which is self-explanatory, and ham, which is the industry jargon for non-spam email that should go to the user.  Inside each of those directories are hundreds of thousands of examples of each type of email, taking from the company Enron between 2001 and 2004.  We will have to read all of this data correctly into python and then feed it into our **classifier** which will then be able to given an email try to guess whether it's spam or ham.

In addition, we will also be using gmail's API to get the perfect test subject for our practice spam filter: our own emails (and spam emails) which will let us see how well the program stacks up against the algorithms google has running.  Remember API stands for **Aplication Programmer Interface** and is how we can communicate with other programs in our program.  In this case, we will work through the gmail API (for more info see: [Resources](https://github.com/nputnam-hu/summer-bootcamp/tree/master/final_project/spam/skeleton#resources)) to get the content of the email message from the given gmail account and format it such that our classifier can classify it.

To get started coding, go on to the Problems section!

## Problems
#### `spam_classifier.py`
##### `load_data()`
This function has already been started for you: it currently iterates through each file and checks if it is in the `ham` or `spam` subdirectory of the `corpus` directory, however it does nothing else!  You need to properly read the data in from the final, [tokenize](https://www.techopedia.com/definition/13698/tokenization) the emails found in the file, and then format it to correctly be read by our classifier. (hint: the word_tokenize function from [this](http://www.nltk.org/api/nltk.tokenize.html) nltk module should be useful)

To do this you will need to define the [`cast_todict`](https://github.com/nputnam-hu/summer-bootcamp/tree/master/final_project/spam/skeleton#cast_todict) function and run it on our tokenized array of words. Finally, we must store the new dict as a [tuple](https://www.tutorialspoint.com/python3/python_tuples.htm) along with the string to indicate whether the data is 'ham' or 'spam'.

Finally we need to save all of this data in 2 lists, one for ham and one for spam, and return both lists so that the data can be used in the [`get_classifier()`](https://github.com/nputnam-hu/summer-bootcamp/tree/master/final_project/spam/skeleton#get_classifier) function
##### `cast_todict()`
This function feeds a list of words into a dict where all the values map to True (important for NaiveBayesClassifier)
  example input->output:
  ```
  ['apple', 'bannana', 'carrot'] -> {'apple':True,'bannana':True,'carrot':True}
  ['Alice', 'Alice', 'Alice', 'Bob'] -> {'Alice':True,'Bob':True}
  ```
##### `get_classifier()`
This function needs to ultimately return our classifier.  To create our classifier, we will employ the `NaiveBayesClassifier.train()`method which given a list of tuples formated as described in `load_data()` will create our classifier for us.  But before we can feed in our training data we have to do a couple of things:
1. Combine our ham and spam lists gotten from load_data() 
2. Shuffle them (maybe with the help of python's built-in `random` module) randomly so the classifier isn't biased by order
3. Split up our shuffled list into a training and test part (a good proportion is 70% training, 30% testing).  You will have to think about how this splitting up process will look in the python code.
Now you can feed the training part of the list to `NaiveBayesClassifier.train()` and the testing part can be used with the accuracy method to test our classifier.

##### `main()`
Once you have the `email_getter.py` code working, main should import the `get_email()` function, tokenize/format them so we can pass them into our classifier and then use the `.classify()` method to categorize the email as ham or spam.  Finally, it should write all of the ham emails to a file called `ham.txt` and all of the spam files to a file called `spam.txt`. 

#### `email_getter.py`
##### `get_credentials()`
get_credentials is a function provided for you that should correctly integrate the app with the gmail API.  You shouldn't have to modify this function.
##### `get_emails()`
Get emails should get all of the emails from the user email account and pass them into [`clean()`](https://github.com/nputnam-hu/summer-bootcamp/tree/master/final_project/spam/skeleton#clean) to properly format them.  To do this, it is important to know that the service variable is a class with several useful methods.  You can find the documentation [here](https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest), but you will probably want to use the `service.users().messages().list` method to get all the mail ids, and then the `service.users().messages().get` method to get individual emails by id.  `get_emails` should ultimately return this list of email bodies, after they have been passed into clean()
##### `clean()`
Python has a built-in email type that is overly complicated for our purposes, we just want to strip the message body and return that.  Clean takes in an email_message (which in turn is taken from the gmail services class method) and returns the message body stripped of unwanted characters such as `\r`, `\n` and '>' that will clutter up our email files and add noise to the prediction.  The code to get the email body has been provided for you, but you will have to strip those bad characters from the body string and then return the body
##### `main()`
This function should be removed, it's only there to allow for easy set-up of the gmail authentication

## Resources
- [Getting Gmail API set up](https://developers.google.com/gmail/api/quickstart/python)
- [Gmail python SDK docs](https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/)
- [nltk Documentation](http://www.nltk.org/)
- [Interesting paper on the subject](http://ats.cs.ut.ee/u/kt/hw/spam/spam.pdf)
