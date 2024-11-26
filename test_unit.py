import pytest
import tkinter as tk
from Calculator import add_toll_fields, montos, cantidades, root


print(add_toll_fields)
print(montos)
print(cantidades)
print(root)
@pytest.fixture
def setup_root():
    # global root
    # root = tk.Tk()
    # yield
    # root.destroy()
    pass

def test_add_monto_label_and_entry(setup_root):
    add_toll_fields()
    assert len(root.winfo_children()) == 8  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[4], tk.Label)
    assert root.winfo_children()[4].cget("text") == "Monto:"
    assert isinstance(root.winfo_children()[5], tk.Entry)

def test_add_cantidad_label_and_entry(setup_root):
    add_toll_fields()
    assert len(root.winfo_children()) == 12  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[6], tk.Label)
    assert root.winfo_children()[6].cget("text") == "Cantidad de peajes:"
    assert isinstance(root.winfo_children()[7], tk.Entry)

def test_append_to_montos_and_cantidades(setup_root):
    add_toll_fields()
    assert len(montos) == 3
    assert len(cantidades) == 3
    assert isinstance(montos[0], tk.Entry)
    assert isinstance(cantidades[0], tk.Entry)

#pytest.main()
