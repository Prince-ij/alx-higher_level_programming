#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    size = ((PyVarObject *)p)->ob_size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = ((PyListObject *)p)->ob_item[i];
        printf("Element %zd: ", i);

        if (PyBytes_Check(element))
        {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %zd\n", ((PyVarObject *)element)->ob_size);
            printf("  trying string: %s\n", ((PyBytesObject *)element)->ob_sval);

            printf("  first %zd bytes: ", ((PyVarObject *)element)->ob_size < 10 ? ((PyVarObject *)element)->ob_size : 10);
            for (Py_ssize_t j = 0; j < (((PyVarObject *)element)->ob_size < 10 ? ((PyVarObject *)element)->ob_size : 10); j++)
            {
                printf("%02x%c", ((PyBytesObject *)element)->ob_sval[j] & 0xff, j + 1 < (((PyVarObject *)element)->ob_size < 10 ? ((PyVarObject *)element)->ob_size : 10) ? ' ' : '\n');
            }
        }
        else if (PyLong_Check(element))
        {
            printf("int\n");
        }
        else if (PyFloat_Check(element))
        {
            printf("float\n");
        }
        else if (PyTuple_Check(element))
        {
            printf("tuple\n");
        }
        else if (PyList_Check(element))
        {
            printf("list\n");
        }
        else if (PyUnicode_Check(element))
        {
            printf("str\n");
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes: ", size < 10 ? size : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf("%02x%c", str[i] & 0xff, i + 1 < (size < 10 ? size : 10) ? ' ' : '\n');
    }
}
