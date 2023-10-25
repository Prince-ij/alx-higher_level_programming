#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *buffer;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size < 10 ? size + 1 : 10);
    printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

    printf("  first %ld bytes: ", size < 10 ? size : 10);
    buffer = PyBytes_AsString(p);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x%c", (unsigned char)buffer[i], i + 1 < 10 ? ' ' : '\n');
    }
}

void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
