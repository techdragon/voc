from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BoolTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = True
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = True
            print(x.attr)
            print('Done.')
            """)


class UnaryBoolOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
    ]


class BinaryBoolOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',
        'test_and_int',

        'test_eq_class',
        'test_eq_complex',
        'test_eq_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',

        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',
        'test_or_int',

        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_int',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',

        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_frozenset',
        'test_true_divide_list',
        'test_true_divide_None',
        'test_true_divide_NotImplemented',
        'test_true_divide_range',
        'test_true_divide_set',
        'test_true_divide_slice',
        'test_true_divide_str',
        'test_true_divide_tuple',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
        'test_xor_int',
    ]


class InplaceBoolOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_float',
        'test_add_frozenset',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',
        'test_and_int',

        'test_floor_divide_bool',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_float',
        'test_floor_divide_frozenset',
        'test_floor_divide_int',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_modulo_bool',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_float',
        'test_multiply_frozenset',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',
        'test_or_int',

        'test_power_bool',
        'test_power_class',
        'test_power_complex',
        'test_power_float',
        'test_power_frozenset',
        'test_power_int',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subtract_bool',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_float',
        'test_subtract_frozenset',
        'test_subtract_int',

        'test_true_divide_bool',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_float',
        'test_true_divide_frozenset',
        'test_true_divide_int',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
        'test_xor_int',
    ]
