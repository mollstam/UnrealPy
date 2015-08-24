class PyIMAPITable : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIMAPITable);
static PyComTypeObject type;
static IMAPITable *GetI(PyObject *self);
	static PyObject *Unadvise(PyObject *self, PyObject *args);
	static PyObject *SortTable(PyObject *self, PyObject *args);
	static PyObject *FindRow(PyObject *self, PyObject *args);
	static PyObject *Restrict(PyObject *self, PyObject *args);
	static PyObject *CreateBookmark(PyObject *self, PyObject *args);
	static PyObject *FreeBookmark(PyObject *self, PyObject *args);
	static PyObject *Abort(PyObject *self, PyObject *args);
	static PyObject *QueryColumns(PyObject *self, PyObject *args);
	static PyObject *QueryPosition(PyObject *self, PyObject *args);
	static PyObject *GetStatus(PyObject *self, PyObject *args);
	static PyObject *SetColumns(PyObject *self, PyObject *args);
	static PyObject *QueryRows(PyObject *self, PyObject *args);
	static PyObject *GetRowCount(PyObject *self, PyObject *args);
	static PyObject *SeekRowApprox(PyObject *self, PyObject *args);
	static PyObject *SeekRow(PyObject *self, PyObject *args);
	static PyObject *Advise(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
protected:
	PyIMAPITable(IUnknown *);
	~PyIMAPITable();
};

