#include <Python.h>
#include "../include/stat_fncs.h"

static PyObject* frequency_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    return Py_BuildValue("d", Frequency(buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* block_frequency_adapter(PyObject *self, PyObject *args)
{
    int block_size;
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "iy*", &block_size, &buffer))
        return NULL;
    return Py_BuildValue("d", BlockFrequency(block_size, buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* runs_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    return Py_BuildValue("d", Runs(buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* longest_run_of_ones_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    return Py_BuildValue("d", LongestRunOfOnes(buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* rank_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    return Py_BuildValue("d", Rank(buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* discrete_fourier_transform_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    double ret;
    ret = DiscreteFourierTransform(buffer.len, (BitSequence*)buffer.buf);
    if (ret == -1)
        return PyErr_NoMemory();
    return Py_BuildValue("d", ret);
}

static PyObject* non_overlapping_template_matchings_adapter(PyObject *self, PyObject *args) {
    int template_length;
    Py_buffer buffer;
    if (!PyArg_ParseTuple(args, "iy*", &template_length, &buffer))
        return NULL;
    double ret;
    ret = NonOverlappingTemplateMatchings(template_length, buffer.len, buffer.buf);
    if (ret == -1) {
        PyErr_SetString(PyExc_ValueError, "Lambda is non-positive.");
        return NULL;
    }
    if (ret == -2) {
        PyErr_SetString(PyExc_ValueError, "Templates could not be found.");
        return NULL;
    }
    if (ret == -3) {
        return PyErr_NoMemory();
    }
    return Py_BuildValue("d", ret);
}

static PyObject* overlapping_template_matchings_adapter(PyObject *self, PyObject *args) {
    int template_length;
    Py_buffer buffer;
    if (!PyArg_ParseTuple(args, "iy*", &template_length, &buffer))
        return NULL;
    double ret;
    ret = OverlappingTemplateMatchings(template_length, buffer.len, buffer.buf);
    if (ret == -1) {
        return PyErr_NoMemory();
    }
    return Py_BuildValue("d", ret);
}

static PyObject* universal_adapter(PyObject *self, PyObject *args) {
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    double ret;
    ret = Universal(buffer.len, buffer.buf);
    if (ret == -1) {
        PyErr_SetString(PyExc_ValueError, "L must be an integer in {6, 7, ..., 16}.");
        return NULL;
    }
    if (ret == -2) {
        PyErr_SetString(PyExc_ValueError, "Q must be greater than 10 * pow(2, L).");
        return NULL;
    }
    if (ret == -3) {
        return PyErr_NoMemory();
    }
    return Py_BuildValue("d", ret);
}

static PyObject* linear_complexity_adapter(PyObject *self, PyObject *args) {
    int template_length;
    Py_buffer buffer;
    if (!PyArg_ParseTuple(args, "iy*", &template_length, &buffer))
        return NULL;
    double ret;
    ret = LinearComplexity(template_length, buffer.len, buffer.buf);
    if (ret == -1) {
        return PyErr_NoMemory();
    }
    return Py_BuildValue("d", ret);
}

static PyObject* serial_adapter(PyObject *self, PyObject *args) {
    int block_length;
    Py_buffer buffer;
    if (!PyArg_ParseTuple(args, "iy*", &block_length, &buffer))
        return NULL;
    double ret;
    ret = Serial(block_length, buffer.len, buffer.buf);
    if (ret == -1) {
        return PyErr_NoMemory();
    }
    return Py_BuildValue("d", ret);
}

static PyObject* approximate_entropy_adapter(PyObject *self, PyObject *args)
{
    int block_size;
    double p_value;
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "iy*", &block_size, &buffer))
        return NULL;
    double ret;
    ret = ApproximateEntropy(block_size, buffer.len, buffer.buf);
    if (ret == -1)
        return PyErr_NoMemory();
    if (ret == -2) {
        PyErr_SetString(PyExc_ValueError, "The block size exceeds recommended value.");
        return NULL;
    }

    return Py_BuildValue("d", ret);
}

static PyObject* cumulative_sums_adapter(PyObject *self, PyObject *args)
{
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    return Py_BuildValue("d", CumulativeSums(buffer.len, (BitSequence*)buffer.buf));
}

static PyObject* random_excursions_adapter(PyObject *self, PyObject *args) {
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    double ret;
    ret = RandomExcursions(buffer.len, buffer.buf);
    if (ret == -1)
        return PyErr_NoMemory();
    if (ret == -2) {
        PyErr_SetString(PyExc_ValueError, "Exceeding the max. number of cycles expected.");
        return NULL;
    }
    if (ret == -3) {
        PyErr_SetString(PyExc_ValueError, "Insufficient number of cycles.");
        return NULL;
    }
    return Py_BuildValue("d", ret);
}

static PyObject* random_excursions_variant_adapter(PyObject *self, PyObject *args) {
    Py_buffer buffer;
    if(!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;
    double ret;
    ret = RandomExcursionsVariant(buffer.len, buffer.buf);
    if (ret == -1)
        return PyErr_NoMemory();
    if (ret == -2) {
        PyErr_SetString(PyExc_ValueError, "Exceeding the max. number of cycles expected.");
        return NULL;
    }
    if (ret == -3) {
        PyErr_SetString(PyExc_ValueError, "Insufficient number of cycles.");
        return NULL;
    }
    return Py_BuildValue("d", ret);
}

// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition
static PyMethodDef myMethods[] = {
        { "frequency", frequency_adapter, METH_VARARGS, "Frequency Test" },
        { "block_frequency", block_frequency_adapter, METH_VARARGS, "Block Frequency Test" },
        { "runs", runs_adapter, METH_VARARGS, "Runs Test" },
        { "longest_run_of_ones", longest_run_of_ones_adapter, METH_VARARGS, "Longest Run of Ones Test" },
        { "rank", rank_adapter, METH_VARARGS, "Binary Matrix Rank Test" },
        { "discrete_fourier_transform", discrete_fourier_transform_adapter, METH_VARARGS,
          "Discrete Fourier Transform (Spectral) Test" },
        { "non_overlapping_template_matchings", non_overlapping_template_matchings_adapter, METH_VARARGS,
          "Non-overlapping Template Matching Test" },
        { "overlapping_template_matchings", overlapping_template_matchings_adapter, METH_VARARGS,
          "Overlapping Template Matching Test" },
        { "universal", universal_adapter, METH_VARARGS, "Maurer's \"Universal Statistical\" Test" },
        { "linear_complexity", linear_complexity_adapter, METH_VARARGS, "Linear Complexity Test" },
        { "serial", serial_adapter, METH_VARARGS, "Serial Test" },
        { "approximate_entropy", approximate_entropy_adapter, METH_VARARGS, "Approximate Entropy Test"},
        { "cumulative_sums", cumulative_sums_adapter, METH_VARARGS, "Cumulative Sums Test" },
        { "random_excursions", random_excursions_adapter, METH_VARARGS, "Random Excursions Test" },
        { "random_excursions_variant", random_excursions_variant_adapter, METH_VARARGS,
          "Random Excursions Variant Test" },
        { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef sp80022suite = {
        PyModuleDef_HEAD_INIT,
        "myModule",
        "Test Module",
        -1,
        myMethods
};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit_sp80022suite(void)
{
    return PyModule_Create(&sp80022suite);
}
