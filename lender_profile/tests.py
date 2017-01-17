"""Tests for lender_profile app."""
from django.test import TestCase
from django.contrib.auth.models import User
from lender_profile.models import PatronProfile
import factory


# Create your tests here.


class ProfileTestCase(TestCase):
    """Profile Model Test Runner."""

    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User

        username = factory.sequence(lambda n: "The Chosen {}".format(n))
        email = factory.LazyAttribute(
            lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
        )

    def setUp(self):
        """Populate database with 20 users for testing."""
        self.users = [self.UserFactory.build() for i in range(20)]

    def test_profile_is_made_when_user_is_saved(self):
        """Profiles are created and saved when a user is created and saved."""
        self.assertTrue(PatronProfile.objects.count() == 20)

    def test_profile_is_associated_with_actual_users(self):
        """Profiles are associated with a specific user when created."""
        profile = PatronProfile.objects.first()
        self.assertTrue(hasattr(profile, "user"))
        self.assertIsInstance(profile.user, User)

    def test_user_has_profile_attached(self):
        """Users have a specific profile associated with them when created."""
        user = self.users[0]
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, PatronProfile)
