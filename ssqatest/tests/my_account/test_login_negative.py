import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        print('****************')
        print('TEST LOGIN NON EXISTING')
        print('****************')

        my_account = MyAccountSignedOut(self.driver)

        my_account.go_to_my_account()
        my_account.input_login_username('afgajkntiqt@test.com')
        my_account.input_login_password('afgajkntiqt')
        my_account.click_login_button()

        expected_error_msg = 'Unknown email address. Check again or try your username.'

        my_account.wait_until_error_is_displayed(expected_error_msg)

