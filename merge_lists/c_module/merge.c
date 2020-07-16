#include <Python.h>
#include <numpy/arrayobject.h>
#include <stdio.h>
#include <stdlib.h>

void merge(long x[], long y[], long size_x, long size_y, long result[]) {
    long i = 0;
    long j = 0;
    while (i < size_x && j < size_y){
	if (x[i] <= y[j]) {
	    result[i+j] = x[i];
	    i++;
	}
	else {
	    result[i+j] = y[j];
	    j++;
	}
    }
    while (i < size_x){
	result[i+j] = x[i];
	i++;
    }
    while (j < size_y){
	result[i+j] = y[j];
	j++;
    }
}

static PyObject *cmerge_cmerge(PyObject *self, PyObject *args) {
    PyObject *x_obj, *y_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "OO", &x_obj, &y_obj))
        return NULL;

    /* Interpret the input objects as numpy arrays. */
    PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_INT, NPY_IN_ARRAY);
    PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_INT, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (x_array == NULL || y_array == NULL) {
        Py_XDECREF(x_array);
        Py_XDECREF(y_array);
        return NULL;
    }

    /* How many data points are there? */
    int N = (int)PyArray_DIM(x_array, 0);
    int M = (int)PyArray_DIM(y_array, 0);

    /* Get pointers to the data as C-types. */
    long *x    = (long*)PyArray_DATA(x_array);
    long *y    = (long*)PyArray_DATA(y_array);

    /* Call the external C function to compute the chi-squared. */
    long value[N+M];
    merge(x, y, N, M, value);

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
static PyMethodDef cmerge_methods[] = {
    { "cmerge", cmerge_cmerge, METH_VARARGS, "Merge two sorted lists on int." },
    { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef cmerge = {
    PyModuleDef_HEAD_INIT,
    "cmerge",
    "Module for cmerge.",
    -1,
    cmerge_methods
};

// Initializes our module using our above struct
/* PyMODINIT_FUNC PyInit_cmerge(void) */
PyMODINIT_FUNC init_cmerge(void)
{
    /* PyModule_Create(&cmerge); */
    PyObject *m = Py_InitModule3("cmerge", cmerge_methods, "Docs");
    if (m == NULL)
	return;
    import_array();
}

