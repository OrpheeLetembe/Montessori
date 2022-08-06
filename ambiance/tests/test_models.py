from ambiance.models import Environment

import pytest


@pytest.mark.django_db
def test_user_str():

    """
    Testing whether Ambiance's __str__ method is implemented properly
    """

    ambiance = Environment.objects.create(
        name='Terre',
        year='2022/2023'
    )

    assert str(ambiance) == f'{ambiance.name}-{ambiance.year}'
