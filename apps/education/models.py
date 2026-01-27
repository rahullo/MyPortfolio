"""
Education app models - Academic background
"""

from django.db import models


class Education(models.Model):
    """
    Educational qualifications
    """
    degree = models.CharField(max_length=200, help_text="e.g., Master of Computer Applications")
    field = models.CharField(max_length=200, help_text="Field of study")
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, help_text="CGPA obtained")
    max_cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=10.0, help_text="Maximum CGPA")
    start_date = models.DateField()
    end_date = models.DateField()
    order = models.IntegerField(default=0, help_text="Display order (0 = most recent)")

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    @property
    def cgpa_percentage(self):
        """Calculate CGPA as percentage"""
        return (self.cgpa / self.max_cgpa) * 100
