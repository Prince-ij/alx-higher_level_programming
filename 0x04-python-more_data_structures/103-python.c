#include <Python.h>

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
        printf("Element %ld: ", i);
        if (PyBytes_Check(element))
        {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(element));
            printf("  trying string: %s\n", PyBytes_AsString(element));
            printf("  first 10 bytes: ");
            for (size_t j = 0; j < 10 && j < PyBytes_Size(element); j++)
            {
                printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
            }
            printf("\n");
        }
        else if (PyFloat_Check(element))
        {
            printf("float\n");
        }
        else if (PyList_Check(element))
        {
            printf("list\n");
        }
        else if (PyTuple_Check(element))
        {
            printf("tuple\n");
        }
        else if (PyLong_Check(element))
        {
            printf("int\n");
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

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < size; i++)
    {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
