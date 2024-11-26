import pytest
import tkinter as tk
from Calculator import add_toll_fields, montos, cantidades, root


print(add_toll_fields)
print(montos)
print(cantidades)
print(root)
@pytest.fixture(scope="module")
def setup_root():
    # global root
    # root = tk.Tk()
    # yield
    # root.destroy()
    add_toll_fields()

def test_add_monto_label_and_entry(setup_root):
    assert len(root.winfo_children()) == 8  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[4], tk.Label)
    assert root.winfo_children()[4].cget("text") == "Monto:"
    assert isinstance(root.winfo_children()[5], tk.Entry)

def test_add_cantidad_label_and_entry(setup_root):
    assert len(root.winfo_children()) == 8  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[6], tk.Label)
    assert root.winfo_children()[6].cget("text") == "Cantidad de peajes:"
    assert isinstance(root.winfo_children()[7], tk.Entry)

def test_append_to_montos_and_cantidades(setup_root):
    assert len(montos) == 1
    assert len(cantidades) == 1
    assert isinstance(montos[0], tk.Entry)
    assert isinstance(cantidades[0], tk.Entry)

#pytest.main()
