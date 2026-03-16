from django import forms


class DonationForm(forms.Form):
    amount = forms.DecimalField(
        label="Donation amount",
        min_value=1,
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"placeholder": "e.g. 25.00"}),
    )
    frequency = forms.ChoiceField(
        label="Frequency",
        choices=(
            ("once", "One-time"),
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
        ),
        widget=forms.RadioSelect,
    )
    name = forms.CharField(
        label="Full name",
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Optional"}),
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )
    message = forms.CharField(
        label="Message",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Optional note with your donation",
            }
        ),
    )


class VolunteerForm(forms.Form):
    name = forms.CharField(
        label="Full name",
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Your name"}),
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )
    availability = forms.ChoiceField(
        label="Availability",
        choices=(
            ("one_time", "One-time help"),
            ("weekly", "A few hours each week"),
            ("monthly", "A few hours each month"),
        ),
    )
    interests = forms.CharField(
        label="Areas you’d like to help with",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. events, outreach, logistics"}
        ),
    )
    message = forms.CharField(
        label="Message",
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Share any skills or ideas you’d like us to know about",
            }
        ),
    )

