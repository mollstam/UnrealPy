class PyIMAPIFolder : public PyIMAPIContainer
{
public:
MAKE_PYCOM_CTOR(PyIMAPIFolder);
static PyComTypeObject type;
static IMAPIFolder *GetI(PyObject *self);
	static PyObject *EmptyFolder(PyObject *self, PyObject *args);
	static PyObject *DeleteMessages(PyObject *self, PyObject *args);
	static PyObject *CopyMessages(PyObject *self, PyObject *args);
	static PyObject *CreateMessage(PyObject *self, PyObject *args);
	static PyObject *CreateFolder(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
protected:
	PyIMAPIFolder(IUnknown *);
	~PyIMAPIFolder();
};

