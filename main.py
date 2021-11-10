from Tests.crud_tests import test_crud
from Tests.discount_tests import test_discount
from Tests.dist_title_tests import test_all_dist_titles
from Tests.price_min_tests import test_all_min_price
from Tests.sort_test import test_price_sort
from Tests.type_change_tests import test_book_type_change
from Tests.undo_redo_tests import test_redo_undo
from UserInterface.UI import run_ui


def main():
    order_list = []
    test_crud()  # done
    test_discount()  # done
    test_book_type_change()  # done
    test_all_min_price()  # done
    test_price_sort()  # done
    test_all_dist_titles()  # done
    test_redo_undo()
    run_ui(order_list)
    # run_cli(order_list)


main()
