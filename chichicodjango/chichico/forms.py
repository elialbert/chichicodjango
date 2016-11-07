from django import forms
from django.forms.widgets import CheckboxSelectMultiple

class VolunteerForm(forms.Form):
    name = forms.CharField(max_length=60, label="Name")
    phone_number = forms.CharField(max_length=60, label="Phone Number")
    email = forms.EmailField(label="Email")
    how_heard = forms.CharField(max_length=60, label="How did you hear about ChiChiCo?",widget=forms.Textarea)
    free_time = forms.CharField(max_length=60, label="What does your schedule look like (include days of week, time of day)? ",widget=forms.Textarea)

class RequestForm(forms.Form):
    org_name = forms.CharField(max_length=255, label="Organization Name")
    org_street_address = forms.CharField(max_length=255, label="Organization Street Address")
    org_city = forms.CharField(max_length=255, label="Organization City")
    org_state = forms.CharField(max_length=255, label="Organization State")
    org_zipcode = forms.CharField(max_length=255, label="Organization Zipcode")
    org_contact_name = forms.CharField(max_length=255, label="Contact Name")
    org_contact_phone = forms.CharField(max_length=255, label="Contact Phone")
    org_contact_email = forms.CharField(max_length=255, label="Contact Email")

    event_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    recurring = forms.MultipleChoiceField(label='This event is',choices=(('weekly','weekly'),('monthly','monthly'),('one_time','one-time'),('other','other')),widget=CheckboxSelectMultiple)
    when_volunteers = forms.CharField(label="When will you need volunteers?",widget=forms.Textarea)
    event_location = forms.CharField(label="Event Location (if different than organization address)",widget=forms.Textarea,required=False)
    number_kids = forms.IntegerField(label="How many kids do you expect will need childcare?**")
    approximate_ages = forms.CharField(max_length=255, label="Approximate ages")
    extra_help = forms.CharField(max_length=255, label="Will the organization provide any childcare help?")
    extra_provided = forms.MultipleChoiceField(label='Will any of the following be provided',choices=(('separate_space','separate space for childcare'),('board_games','board games or toys'),('snacks','snacks'),('television','television_and_movie_player'),('arts_and_crafts','arts and crafts materials')),widget=CheckboxSelectMultiple)

    extra_language_required = forms.CharField(max_length=255,label="Required non-english language for volunteers")

    extra_language_preferred = forms.CharField(max_length=255,label="Preferred non-english language for volunteers")
    extra_considerations = forms.CharField(required=False,widget=forms.Textarea)
