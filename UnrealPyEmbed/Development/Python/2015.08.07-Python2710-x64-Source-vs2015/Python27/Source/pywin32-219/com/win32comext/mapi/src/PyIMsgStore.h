class PyIMsgStore : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIMsgStore);
static PyComTypeObject type;
static IMsgStore *GetI(PyObject *self);
	static PyObject *AbortSubmit(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
	static PyObject *CompareEntryIDs(PyObject *self, PyObject *args);
	static PyObject *GetReceiveFolderTable(PyObject *self, PyObject *args);
	static PyObject *GetReceiveFolder(PyObject *self, PyObject *args);
	static PyObject *OpenEntry(PyObject *self, PyObject *args);
protected:
	PyIMsgStore(IUnknown *);
	~PyIMsgStore();
};

