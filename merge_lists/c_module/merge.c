#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

long * merge(long *x, long *y) {
    long i, j;
    long result[sizeof x + sizeof y];
    while (i < sizeof x && j < sizeof y){
	if (x[i] < y[j]) {
	    result[i+j] = x[i];
	    i++;
	}
	else {
	    result[i+j] = y[j];
	    j++;
	}
    }
    if (i < sizeof x) {
	while (j < sizeof y){
	    result[i+j] = y[j];
	    y++;
	}
    }
    else {
	while (i < sizeof x){
	    result[i+j] = x[i];
	    i++;
	}
    }

    return result;
}

static PyObject *merge_lists(PyObject *self, PyObject *args)
{
    double m, b;
    PyObject *x_obj, *y_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddOOO", &m, &b, &x_obj, &y_obj))
        return NULL;

    /* Interpret the input objects as numpy arrays. */
    PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (x_array == NULL || y_array == NULL) {
        Py_XDECREF(x_array);
        Py_XDECREF(y_array);
        return NULL;
    }

    /* How many data points are there? */
    int N = (int)PyArray_DIM(x_array, 0);

    /* Get pointers to the data as C-types. */
    long *x    = (long*)PyArray_DATA(x_array);
    long *y    = (long*)PyArray_DATA(y_array);

    /* Call the external C function to compute the chi-squared. */
    long * value = merge(x, y);
    /* Clean up. */
    Py_DECREF(x_array);
    Py_DECREF(y_array);

    /* Build the output tuple */
    PyObject *ret = Py_BuildValue("d", value);
    return ret;
}

// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition 
static PyMethodDef myMethods[] = {
    { "merge", merge, METH_NOARGS, "Does a merge of two sorted lists" },
    { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef merge = {
    PyModuleDef_HEAD_INIT,
    "merge",
    "Test Module",
    -1,
    myMethods
};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit_merge(void)
{
    return PyModule_Create(&merge);
}
