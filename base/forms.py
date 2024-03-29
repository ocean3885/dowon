from django.forms import ModelForm
from django import forms
import datetime
from .models import Submit, Person, User


class SignupForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['phonnumber']
        widgets = {
            "phonnumber": forms.TextInput(
                attrs={
                    "placeholder": "전화번호",
                }
            ),
        }

    def signup(self, request, user):
        user.phonnumber = self.cleaned_data['phonnumber']
        user.save()
        # 이미생성된 신청서 중 가입유저 전화번호와 같은 신청서의 빈 유저필드를 가입유저로 변경
        obj = Submit.objects.filter(phonnumber=user.phonnumber)
        if obj:
            for i in obj:
                i.user = user
                i.save()

    def clean_phonnumber(self, *args, **kwargs):
        phonnumber = self.cleaned_data.get("phonnumber")
        if len(phonnumber) < 10:
            raise forms.ValidationError("'010'을 포함하여 10자리 이상의 숫자로 입력해주시기 바랍니다.")
        if phonnumber.isdigit():
            return phonnumber
        else:
            raise forms.ValidationError("'-'하이픈을 제외하고 숫자로만 입력해주시기 바랍니다.")


class JmSubmitForm(ModelForm):

    field_order = ['name', 'phonnumber', 'visit', 'wantdate', 'email',
                   'adress', 'first_name_ch', 'fav_name', 'avoid_name',
                   'parents_name', 'description']

    class Meta:
        model = Submit
        exclude = ['category', 'complete', 'user', 'process']
        labels = {
            "phonnumber": "전화번호 ",
            "name": "이 름 ",
            "visit": "상담방법 ",
            "wantdate": "상담희망일 ",
            "first_name_ch": "성씨(한자) ",
            "avoid_name": "피하고싶은 이름 ",
            "fav_name": "희망하는 이름 ",
            "adress": "주 소 ",
            "description": "추가요청사항 ",
            "email": "이메일 ",
            "parents_name": "부모님 성함 ",
        }
        widgets = {
            "phonnumber": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "전화번호를 입력하세요",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "신청인 이름을 입력하세요",
                }
            ),
            "wantdate": forms.TextInput(
                attrs={
                    "placeholder": "예) 2023년 5월 25일",
                }
            ),
            "first_name_ch": forms.TextInput(
                attrs={
                    "placeholder": "예) 金,李,朴 or 김해김,영월엄",
                }
            ),
            "parents_name": forms.TextInput(
                attrs={
                    "placeholder": "예) 부-이수일,모-심순애",
                }
            ),
            "avoid_name": forms.TextInput(
                attrs={
                    "placeholder": "예) 친척이름,지인이름 등",
                }
            ),
            "fav_name": forms.TextInput(
                attrs={
                    "placeholder": "작명시 선호하는 이름 유형 참고",
                }
            ),
            "adress": forms.TextInput(
                attrs={
                    "placeholder": "인증서를 우편으로 받아보실 경우 필요",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "예) dwnaming@google.com",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "작명시 추가로 참고할 내용 남겨주세요",
                }
            ),
        }

    def clean_phonnumber(self, *args, **kwargs):
        phonnumber = self.cleaned_data.get("phonnumber")
        if len(phonnumber) < 10:
            raise forms.ValidationError("'010'을 포함하여 10자리 이상의 숫자로 입력해주시기 바랍니다.")
        if phonnumber.isdigit():
            return phonnumber
        else:
            raise forms.ValidationError("'-'하이픈을 제외하고 숫자로만 입력해주시기 바랍니다.")


class PersonForm(ModelForm):

    today = datetime.date.today()
    YEAR_CHOICES = []
    for r in range(1940, (today.year+1)):
        YEAR_CHOICES.append((r, r))
    YEAR_CHOICES.reverse()
    year = forms.ChoiceField(widget=forms.Select, choices=YEAR_CHOICES,
                             initial=today.year, label="태어난 년(年) ", required=True)

    MONTH_CHOICES = []
    for r in range(1, 13):
        MONTH_CHOICES.append((r, r))
    month = forms.ChoiceField(widget=forms.Select, choices=MONTH_CHOICES,
                              initial=today.month, label="태어난 월(月) ")

    DAY_CHOICES = []
    for r in range(1, 32):
        DAY_CHOICES.append((r, r))

    day = forms.ChoiceField(widget=forms.Select, choices=DAY_CHOICES,
                            initial=today.day, label="태어난 일(日) ")

    GEN_CHOICES = [("남", "남"), ("여", "여")]
    gen = forms.ChoiceField(widget=forms.RadioSelect,
                            choices=GEN_CHOICES, label="성 별 ")
    SL_CHOICES = [("양력", "양력"), ("음력", "음력"), ("음력윤달", "음력윤달")]
    sl = forms.ChoiceField(widget=forms.RadioSelect,
                           choices=SL_CHOICES, label="양력/음력 ")

    class Meta:

        model = Person
        exclude = ['submit', 'name']
        labels = {
            "time": "태어난 시간 ",
        }


class GmSubmitForm(ModelForm):

    field_order = ['name', 'phonnumber', 'visit', 'wantdate', 'email',
                   'adress', 'first_name_ch', 'fav_name', 'avoid_name',
                   'parents_name', 'description']

    class Meta:
        model = Submit
        exclude = ['category', 'complete', 'user', 'process']
        labels = {
            "phonnumber": "전화번호 ",
            "name": "이 름 ",
            "visit": "상담방법 ",
            "wantdate": "상담희망일 ",
            "first_name_ch": "성씨(한자) ",
            "avoid_name": "피하고싶은 이름 ",
            "fav_name": "희망하는 이름 ",
            "adress": "주 소 ",
            "description": "추가요청사항 ",
            "email": "이메일 ",
            "parents_name": "부모님 성함 ",
        }
        widgets = {
            "phonnumber": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "전화번호를 입력하세요",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "개명신청인 이름을 입력하세요",
                }
            ),
            "wantdate": forms.TextInput(
                attrs={
                    "placeholder": "예) 2023년 5월 25일",
                }
            ),
            "first_name_ch": forms.TextInput(
                attrs={
                    "placeholder": "예) 金,李,朴 or 김해김,영월엄",
                }
            ),
            "parents_name": forms.TextInput(
                attrs={
                    "placeholder": "예) 부-이수일,모-심순애",
                }
            ),
            "avoid_name": forms.TextInput(
                attrs={
                    "placeholder": "예) 친척이름,지인이름 등",
                }
            ),
            "fav_name": forms.TextInput(
                attrs={
                    "placeholder": "개명시 선호하는 이름 유형 참고",
                }
            ),
            "adress": forms.TextInput(
                attrs={
                    "placeholder": "인증서를 우편으로 받아보실 경우 필요",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "예) dwnaming@google.com",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "개명시 추가로 참고할 내용 남겨주세요",
                }
            ),
        }

        def clean_phonnumber(self, *args, **kwargs):
            phonnumber = self.cleaned_data.get("phonnumber")
            if len(phonnumber) < 10:
                raise forms.ValidationError(
                    "'010'을 포함하여 10자리 이상의 숫자로 입력해주시기 바랍니다."
                )
            if phonnumber.isdigit():
                return phonnumber
            else:
                raise forms.ValidationError("'-'하이픈을 제외하고 숫자로만 입력해주시기 바랍니다.")


class SjSubmitForm(ModelForm):
    CAT_CHOICES = [("사주상담", "사주상담"), ("궁합", "궁합")]
    category = forms.ChoiceField(widget=forms.RadioSelect,
                                 choices=CAT_CHOICES, label="사주/궁합 ")

    class Meta:
        model = Submit
        fields = ['category', 'name', 'phonnumber', 'visit',
                  'wantdate', 'email', 'description']
        labels = {
            "phonnumber": "전화번호 ",
            "name": "이 름 ",
            "description": "상담요청사항 ",
            "email": "이메일 ",
            "visit": "상담방법 ",
            "wantdate": "상담희망일 ",
        }
        widgets = {
            "phonnumber": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "전화번호를 입력하세요",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "상담신청인 이름을 입력하세요",
                }
            ),
            "wantdate": forms.TextInput(
                attrs={
                    "placeholder": "예) 2023년 5월 25일",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "예) dwnaming@google.com",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "상담신청 내용을 자세히 남겨주세요",
                }
            ),
        }

        def clean_phonnumber(self, *args, **kwargs):
            phonnumber = self.cleaned_data.get("phonnumber")
            if len(phonnumber) < 10:
                raise forms.ValidationError(
                    "'010'을 포함하여 10자리 이상의 숫자로 입력해주시기 바랍니다."
                )
            if phonnumber.isdigit():
                return phonnumber
            else:
                raise forms.ValidationError("'-'하이픈을 제외하고 숫자로만 입력해주시기 바랍니다.")


class SjPersonForm(PersonForm):

    field_order = ['name', 'sl', 'gen', 'year', 'month', 'day', 'time']

    class Meta:
        exclude = ['submit']
        labels = {
            "time": "태어난 시간 ",
            "name": "대상자 이름 ",
        }

