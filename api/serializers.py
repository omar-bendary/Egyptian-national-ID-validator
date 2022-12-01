from rest_framework import serializers
from .models import Person
from .helper.government_set import government_codes, GOVERNMENT_TABLE
from .helper.date_and_age import str_to_date, age


class NationalIDSerializer(serializers.ModelSerializer):
    nationalID = serializers.IntegerField()
    gender = serializers.SerializerMethodField()
    government = serializers.SerializerMethodField()
    birth_date = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    # Check that the National ID sent is a valid one.
    def validate_nationalID(self, nationalID):
        century_set = [2, 3]
        nationalID_str = str(nationalID)

        if int(nationalID_str[0]) == 2:
            century_segment = '19'
        elif int(nationalID_str[0]) == 3:
            century_segment = '20'

        birth_date = str_to_date(century_segment + nationalID_str[1:7])
        age_number = age(birth_date)

        if len(nationalID_str) != 14 or nationalID < 0:
            raise serializers.ValidationError(
                "National ID must be a 14 digits positive number")

        if int(nationalID_str[7:9]) not in government_codes or \
                int(nationalID_str[0]) not in century_set or \
                int(nationalID_str[3:5]) > 12 or \
                int(nationalID_str[5: 7]) > 31 or \
                age_number < 0:

            raise serializers.ValidationError(
                "Enter a valid National ID")

        return nationalID

    # Format the birthdate in readable way
    def get_birth_date(self, obj):
        return obj.birth_date.strftime("%d/%m/%Y")

    # Get a Person age

    def get_age(self, obj):
        return age(obj.birth_date)

    # Display the gender in readable way
    def get_gender(self, obj):
        return obj.get_gender_display()

    # Display the government in readable way
    def get_government(self, obj):
        government = GOVERNMENT_TABLE[int(obj.government)]
        return government

    def save(self, **kwargs):
        nationalID = self.validated_data['nationalID']
        nationalID_str = str(nationalID)

        try:
            # if the id already exits we get it
            self.instance = Person.objects.get(nationalID=nationalID)

        except Person.DoesNotExist:

            # Check the first digit to get the century range
            if int(nationalID_str[0]) == 2:
                century = 'Was Born in the century (1900-1999) '
                century_segment = '19'
            elif int(nationalID_str[0]) == 3:
                century = 'Was Born in the century (2000-2099) '
                century_segment = '20'

            # Check the gender depending on the 13th digit
            if int(nationalID_str[12]) % 2 == 0:
                gender = 'F'
            else:
                gender = 'M'

            # Check the government code against the government name
            government = int(nationalID_str[7:9])

            # Convert the date from string to date object
            birth_date = str_to_date((century_segment + nationalID_str[1:7]))

            # Create a new record for a person
            self.instance = Person.objects.create(
                nationalID=nationalID, birth_date=birth_date, government=government, gender=gender, century=century)

        return self.instance

    class Meta:
        model = Person
        fields = ['nationalID', 'birth_date', 'age',
                  'government', 'gender', 'century']
        read_only_fields = ('birth_date', 'age',
                            'government', 'gender', 'century')
