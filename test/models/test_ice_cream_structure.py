import pytest

from src.models.ice_cream_structure import IceCreamStand


class TestIceCreamStand:

    do_not_have_in_stock = []
    have_in_stock = ['cupuaçu', 'tapioca', 'brunette']

    @pytest.fixture
    def setup_ice_cream_structure(self, stock):
        return IceCreamStand('Magnum', 'ice creams', stock)

    @pytest.fixture
    def setup_ice_cream_structure_no_stock(self):
        return IceCreamStand('Magnum', 'ice creams', [])

    @pytest.mark.parametrize('stock, expected_result',
                             [(have_in_stock, '\n available ice cream flavors:'
                              '\n\t-cupuaçu\n\t-tapioca\n\t-brunette\n'),
                              (do_not_have_in_stock, 'currently out of stock!\n')])
    def test_flavors_available(self, setup_ice_cream_structure, stock, expected_result, capsys):
        # Setup
        ice_cream_parlor = setup_ice_cream_structure

        # Call
        ice_cream_parlor.flavors_available()
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('stock, flavor, expected_result',
                             [(have_in_stock, 'cupuaçu', 'We currently have cupuaçu\n'),
                              (have_in_stock, '', 'enter a valid flavor.\n'),
                              (have_in_stock, 'watermelon',
                               'We don t have watermelon at the moment!\n'),
                              (do_not_have_in_stock, 'cupuaçu',
                               'Currently out of stock!\n'),
                              (do_not_have_in_stock, '',
                               'We are currently out of stock!\n'),
                              (do_not_have_in_stock, 'watermelon', 'out of stock!\n')])
    def test_find_flavor(self, setup_ice_cream_structure, flavor, expected_result, capsys):
        # Setup
        ice_cream_parlor = setup_ice_cream_structure

        # Call
        ice_cream_parlor.find_flavor(flavor)
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result

    @pytest.mark.parametrize('stock, flavor, expected_result',
                             [(have_in_stock, 'watermelon', 'watermelon added to stock!\n'),
                              (have_in_stock, 'tapioca',
                               'tapioca now available!\n'),
                              (have_in_stock, '', 'enter a valid flavor.\n'),
                              (do_not_have_in_stock, 'watermelon',
                               'watermelon added to stock!\n'),
                              (do_not_have_in_stock, '', 'enter a valid flavor\n')])
    def test_add_flavor(self, setup_ice_cream_structure, flavor, expected_result, capsys):
        # Setup
        ice_cream_parlor = setup_ice_cream_structure

        # Call
        ice_cream_parlor.add_flavor(flavor)
        captured = capsys.readouterr()
        result = captured.out

        # Assessment
        assert result == expected_result
