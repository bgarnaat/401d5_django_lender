"""Tests for lender_profile app."""
from django.test import TestCase
from user.contrib.auth.models import User
from lender_profile.models import PatronProfile
import factory


# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence(lambda n: "The Chosen {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.user.replace(" ", ""))
    )


class ProfileTestCase(TestCase):
    """Profile Model Test Runner."""

    def setUp(self):
        """Appropriate setup for appropriate test."""
        self.foo = "bar"
        self.users = [UserFactory.build() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """."""
        self.assertTrue(PatronProfile.objects.count() == 20)

    def test_profile_is_associated_with_actual_users(self):
        """."""
        profile = PatronProfile.objects.first()
        self.assertTrue(hasattr(profile, "user"))
        self.assertIsInstance(profile.user, User)

    def test_user_has_profile_attached(self):
        """."""
        user = self.users[0]
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, PatronProfile)