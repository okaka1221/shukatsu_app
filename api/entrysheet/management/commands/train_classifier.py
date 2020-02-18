from django.core.management.base import BaseCommand

from api.entrysheet.classification import Classifier

class Command(BaseCommand):
    """
    train data again after getting more data
    """

    def add_arguments(self, parser):
        parser.add_argument('-ts', type=float, default=0.2, help='test size')
        parser.add_argument('-e', type=int, default=50, help='epochs')
        parser.add_argument('-bs', type=int, default=3, help='batch size')
        parser.add_argument('-p', type=int, default=5, help='patience')

    def handle(self, *args, **options):
        classifier = Classifier()
        classifier.train(options['ts'], options['e'], options['bs'], options['p'])