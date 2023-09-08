import pytest

from src.models.restaurant import Restaurant


class TestRestaurant:

    @pytest.fixture
    def restaurant_setup(self):
        # Create a restaurant instance and return it
        return Restaurant("Fishmonger", "Regional food")

    @pytest.mark.parametrize('expected_result',
                             ['This restaurant serves regional food\n'
                              'This restaurant is serving 0 customers since it opened.\n'])
    def test_describe_restaurant(self, restaurant_setup, expected_result, capsys):
        # Setup
        restaurant = restaurant_setup

        # Call
        restaurant.describe_restaurant()
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('initial_open_status, expected_result', [(False, 'Fishmonger, its open!\n'),
                                                                      (True, 'Fishmonger, its open!\n')])
    def test_open_restaurant(self, restaurant_setup, initial_open_status, expected_result, capsys):
        # Setup
        restaurant = restaurant_setup
        restaurant.open = initial_open_status

        # Call
        restaurant.open_restaurant()
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('initial_open_status, expected_result', [(True, 'Fishmonger, it is closed!\n'),
                                                                      (False, 'Fishmonger,It is currently closed!\n')])
    def test_close_restaurant(self, restaurant_setup, initial_open_status, expected_result, capsys):
        # Setup
        restaurant = restaurant_setup
        restaurant.open = initial_open_status

        # Call
        restaurant.close_restaurant()
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('initial_open_status, number_served, expected_result',
                             [(True, 10, 'This restaurant is serving 10 customers since it opened.\n'),
                              (True, '', 'Enter a valid value (integer)'
                                         ' for the number of customers served.\n'),
                              (True, 'um', ' Enter a valid value (integer)'
                                           ' for the number of customers served.\n'),
                              (False, 15, 'Fishmonger, it is closed!\n')])
    def test_set_number_served(self, restaurant_setup, initial_open_status, number_served, expected_result, capsys):
        # Setup
        restaurant = restaurant_setup
        restaurant.open = initial_open_status

        # Call
        restaurant.set_number_served(number_served)
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('initial_open_status, number_served, inbrunettent, expected_result',
                             [(True, 50, 10, 'The restaurant is only serving 60 diners since it opened.\n'),
                              (True, 50, '', ' Enter a valid value (integer)'
                                             ' for the number of customers served.\n'),
                              (True, 50, 'um', 'Enter a valid value (integer)'
                                               ' for the number of customers served.\n'),
                              (False, 50, 15, 'Fishmonger, closed!!\n')])
    def test_inbrunettent_number_served(self, restaurant_setup, initial_open_status,
                                        number_served, inbrunettent, expected_result, capsys):
        # Setup
        restaurant = restaurant_setup
        restaurant.open = initial_open_status
        restaurant.number_served = number_served

        # Call
        restaurant.inbrunettent_number_served(inbrunettent)
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result
