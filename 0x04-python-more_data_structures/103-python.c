#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *element;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %zd: ", i);

        if (PyBytes_Check(element))
        {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %zd\n", PyBytes_Size(element));
            printf("  trying string: %s\n", PyBytes_AsString(element));

            printf("  first %zd bytes: ", (PyBytes_Size(element) < 10) ? PyBytes_Size(element) : 10);
            unsigned char *str = (unsigned char *)PyBytes_AsString(element);
            for (Py_ssize_t j = 0; j < ((PyBytes_Size(element) < 10) ? PyBytes_Size(element) : 10); j++)
            {
                printf("%02x%c", str[j], (j + 1 < ((PyBytes_Size(element) < 10) ? PyBytes_Size(element) : 10)) ? ' ' : '\n');
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
    unsigned char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes: ", (size < 10) ? size : 10);
    for (i = 0; i < ((size < 10) ? size : 10); i++)
    {
        printf("%02x%c", str[i], (i + 1 < ((size < 10) ? size : 10)) ? ' ' : '\n');
    }
}
