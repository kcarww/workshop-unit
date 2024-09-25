# pylint: disable=C0115,E0401,C0116,C0103,C0303,C0304,C0114,C0305
import unittest
from produto import Produto

class TestProduto(unittest.TestCase):

    def test_str(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(str(p), '1 - Arroz - R$ 5.00 - 10 unidades')
    
    def test_repr(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(repr(p), '1 - Arroz - R$ 5.00 - 10 unidades')
    
    def test_if_object_is_instance_of_produto(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertIsInstance(p, Produto)
        
        
    def test_if_codigo_field_is_int(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertIsInstance(p.codigo, int)
        
    def test_if_codigo_field_is_correct(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(p.codigo, 1)
        
        
    def test_if_nome_field_is_str(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertIsInstance(p.nome, str)
    
    def test_if_nome_field_is_correct(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(p.nome, 'Arroz')
        
    def test_if_preco_field_is_float(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertIsInstance(p.preco, float)
        
    def test_if_preco_field_is_correct(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(p.preco, 5.0)
        
    def test_if_quantidade_field_is_int(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertIsInstance(p.quantidade, int)
        
    def test_if_quantidade_field_is_correct(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        self.assertEqual(p.quantidade, 10)
        
    def test_if_object_available_is_false_when_deactivated(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        p.desativar()
        self.assertFalse(p.disponivel)
        
    
    def test_if_object_available_is_true_when_activated(self):
        p = Produto(1, 'Arroz', 5.0, 10)
        p.desativar()
        p.ativar()
        self.assertTrue(p.disponivel)

    # Testes de Validação

    def test_valida_codigo_invalido(self):
        with self.assertRaises(ValueError):
            Produto(-1, 'Arroz', 5.0, 10)

    def test_valida_codigo_zero(self):
        with self.assertRaises(ValueError):
            Produto(0, 'Arroz', 5.0, 10)

    def test_valida_nome_invalido(self):
        with self.assertRaises(ValueError):
            Produto(1, '', 5.0, 10)

    def test_valida_preco_invalido(self):
        with self.assertRaises(ValueError):
            Produto(1, 'Arroz', -5.0, 10)

    def test_valida_preco_zero(self):
        with self.assertRaises(ValueError):
            Produto(1, 'Arroz', 0.0, 10)

    def test_valida_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            Produto(1, 'Arroz', 5.0, -1)

