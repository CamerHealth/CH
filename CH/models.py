"""
CH models.
"""
from django.db.models import fields

from opal import models

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

class TODOItem(models.EpisodeSubrecord):
	job = fields.CharField(max_length=200)
	due_date = fields.DateField(blank=True, null=True)
	details = fields.TextField(blank=True, null=True)
	completed = fields.BooleanField(default=False)