import pytest
import tkinter as tk
from Calculator import add_toll_fields, montos, cantidades, root


print(add_toll_fields)
print(montos)
print(cantidades)
print(root)
@pytest.fixture
def setup_root():
    global root
    root = tk.Tk()
    yield
    root.destroy()

def test_add_monto_label_and_entry(setup_root):
    add_toll_fields()
    assert len(root.winfo_children()) == 4  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[0], tk.Label)
    assert root.winfo_children()[0].cget("text") == "Monto:"
    assert isinstance(root.winfo_children()[1], tk.Entry)

def test_add_cantidad_label_and_entry(setup_root):
    add_toll_fields()
    assert len(root.winfo_children()) == 4  # 2 labels, 2 entries
    assert isinstance(root.winfo_children()[2], tk.Label)
    assert root.winfo_children()[2].cget("text") == "Cantidad de peajes:"
    assert isinstance(root.winfo_children()[3], tk.Entry)

def test_append_to_montos_and_cantidades(setup_root):
    add_toll_fields()
    assert len(montos) == 1
    assert len(cantidades) == 1
    assert isinstance(montos[0], tk.Entry)
    assert isinstance(cantidades[0], tk.Entry)

#pytest.main()