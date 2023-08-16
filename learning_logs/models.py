from django.db import models


# Create your models here.
class Topic(models.Model):
    """ A topic the user is learning about."""
    objects = None
    text = models.CharField(max_length=200)  # Recording the title of the Topic with a max length of 200 characters
    date_added = models.DateTimeField(auto_now_add=True)  # Recording the date and time that a topic was created

    # automatically using auto_now_add=True

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
