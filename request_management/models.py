from django.db import models
from django.urls import reverse

class NewUserRequest(models.Model):

    id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(
        'auth.User',
        on_delete=models.DO_NOTHING,
    )
    for_firstname = models.CharField(max_length=50)
    for_lastname = models.CharField(max_length=50)

    start_date = models.DateField(auto_now=True)
    
    class Campuse(models.TextChoices):
        VALENDAR = 'VAL', ('Valendar')
        DUESSELDORF = 'DUS', ('Düsseldorf')
    campus = models.CharField(
        max_length=3,
        choices=Campuse,
        default=Campuse.VALENDAR)
    
    department = models.CharField(max_length=10, default='')
    job_title = models.CharField(max_length=20)
    office = models.CharField(max_length=10)
    supervisor = models.CharField(max_length=20)
    network_access = models.TextField(default='not needed')
    mail_distribution_lists = models.TextField(default='not needed')
    addtional_email = models.TextField(default='not needed')
    mystudies = models.BooleanField(default=False)
    ac5 = models.BooleanField(default=False)
    moodle = models.BooleanField(default=False)
    otrs = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New User Request by {self.requested_by} for {self.for_firstname} {self.for_lastname} on {self.created.date()}"
    
    def get_absolute_url(self):
        return reverse("NURDetail", kwargs={"pk": self.pk})
    
    def get_title(self):
        return f"New User Request by {self.requested_by} for {self.for_firstname} {self.for_lastname} on {self.created.date()}"
    
    def get_info(self):
        return f"{self.job_title} in {self.department} on {self.start_date}"
    
    



