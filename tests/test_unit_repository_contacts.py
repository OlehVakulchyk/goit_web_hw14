import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from goit_web_hw13.database.models import UserContact, User
from goit_web_hw13.schemas import ContactModel, ContactResponse
from goit_web_hw13.repository.contacts import (
    get_contacts,
    get_contact_by_id,
    get_search_contacts,
    get_contacts_by_bithday,
    get_contacts_by_email,
    create,
    remove,
    update,
)


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    # async def test_get_contacts(self):
    #     contacts = [UserContact(), UserContact(), UserContact()]
    #     self.session.query().filter_by().limit().offset().all.return_value = contacts
    #     result = await get_contacts(limit=10, offset=0, db=self.session, user=self.user)
    #     self.assertEqual(result, contacts)

    async def test_get_search_contacts(self):
        contacts = [UserContact(), UserContact(), UserContact()]
        self.session.query().filter_by().filter_by().limit().offset().all.return_value = [contacts[0]]
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_name='o ', 
                                           contact_surname=None)
        self.assertEqual(result, contacts[0])

    # async def test_get_contact_found(self):
    #     contact = UserContact()
    #     self.session.query().filter().first.return_value = contact
    #     result = await get_contact_by_id(contact_id=1, user=self.user, db=self.session)
    #     self.assertEqual(result, contact)

    # async def test_get_contact_not_found(self):
    #     self.session.query().filter().first.return_value = None
    #     result = await get_contact_by_id(contact_id=1, user=self.user, db=self.session)
    #     self.assertIsNone(result)

    # async def test_create_contact(self):
    #     body = ContactModel(
    #         name="test",
    #         surname="surtest",
    #         email="test@test.com",
    #         phone="+380(55)777-88-99",
    #         bithday="2023-06-02",
    #         information="test note",
    #     )
    #     # tags = [Tag(id=1, user_id=1), Tag(id=2, user_id=1)]
    #     # self.session.query().filter().all.return_value = tags
    #     result = await create(body=body, db=self.session, user=self.user)
    #     self.assertEqual(result.name, body.name)
    #     self.assertEqual(result.surname, body.surname)
    #     self.assertEqual(result.email, body.email)
    #     self.assertEqual(result.phone, body.phone)
    #     self.assertEqual(result.bithday, body.bithday)
    #     self.assertEqual(result.information, body.information)
    #     self.assertEqual(result.user_id, self.user.id)
    #     self.assertTrue(hasattr(result, "id"))
    #     self.assertTrue(hasattr(result, "created_at"))
    #     self.assertTrue(hasattr(result, "updated_at"))

    # async def test_remove_contact_found(self):
    #     contact = UserContact()
    #     self.session.query().filter().first.return_value = contact
    #     result = await remove(id=1, db=self.session, user=self.user)
    #     self.assertEqual(result, contact)

    # async def test_remove_contact_not_found(self):
    #     self.session.query().filter().first.return_value = None
    #     result = await remove(id=1, db=self.session, user=self.user)
    #     self.assertIsNone(result)

    # async def test_update_contact_found(self):
    #     body = ContactModel(
    #         name="test",
    #         surname="surtest",
    #         email="test@test.com",
    #         phone="+380(55)777-88-99",
    #         bithday="2023-06-02",
    #         information="test note",
    #     )
    #     contact = UserContact()
    #     self.session.query().filter().first.return_value = contact
    #     self.session.commit.return_value = None
    #     result = await update(id=1, body=body, db=self.session, user=self.user)
    #     self.assertEqual(result, contact)

    # async def test_update_contact_not_found(self):
    #     body = ContactModel(
    #         name="test",
    #         surname="surtest",
    #         email="test@test.com",
    #         phone="+380(55)777-88-99",
    #         bithday="2023-06-02",
    #         information="test note",
    #     )
    #     self.session.query().filter().first.return_value = None
    #     self.session.commit.return_value = None
    #     result = await update(id=1, body=body, db=self.session, user=self.user)
    #     self.assertIsNone(result)

    # async def test_update_status_note_found(self):
    #     body = NoteStatusUpdate(done=True)
    #     note = Note()
    #     self.session.query().filter().first.return_value = note
    #     self.session.commit.return_value = None
    #     result = await update_status_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertEqual(result, note)

    # async def test_update_status_note_not_found(self):
    #     body = NoteStatusUpdate(done=True)
    #     self.session.query().filter().first.return_value = None
    #     self.session.commit.return_value = None
    #     result = await update_status_note(note_id=1, body=body, user=self.user, db=self.session)
    #     self.assertIsNone(result)


if __name__ == "__main__":
    # print(131313)
    # BASE_DIR = ".."
    unittest.main()
