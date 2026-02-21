class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)   # 👈 ye field
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)      # 👈 ye field