"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from polls.models import Poll

class PollModelTest(TestCase):
    def test_creating_a_new_poll_and_saving_it_to_the_database(self):
        # start by creating a new Poll object with its "question" set
        poll = Poll()
        poll.question = "What's up?"
        poll.pub_date = timezone.now()

        # check we can save it to the database
        poll.save()

        # now check we can find it in the database again
        all_polls_in_database = Poll.objects.all()
        self.assertEquals(len(all_polls_in_database), 1)
        only_poll_in_database = all_polls_in_database[0]
        self.assertEquals(only_poll_in_database, poll)

        # and check that it's saved its two attributes: question and pub_date
        self.assertEquals(only_poll_in_database.question, "What's up?")
        self.assertEquals(only_poll_in_database.pub_date, poll.pub_date)        
        
    def test_verbose_name_for_pub_date(self):
        for field in Poll._meta.fields:
            if field.name ==  'pub_date':
                self.assertEquals(field.verbose_name, 'Date published')    
                
    def test_poll_objects_are_named_after_their_question(self):
        p = Poll()
        p.question = 'How is babby formed?'
        self.assertEquals(unicode(p), 'How is babby formed?')                