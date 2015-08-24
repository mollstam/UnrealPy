class PyIMAPISession : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIMAPISession);
static PyComTypeObject type;
static IMAPISession *GetI(PyObject *self);
	static PyObject *OpenProfileSection(PyObject *self, PyObject *args);
	static PyObject *OpenAddressBook(PyObject *self, PyObject *args);
	static PyObject *Logoff(PyObject *self, PyObject *args);
	static PyObject *GetStatusTable(PyObject *self, PyObject *args);
	static PyObject *GetMsgStoresTable(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
	static PyObject *CompareEntryIDs(PyObject *self, PyObject *args);
	static PyObject *Unadvise(PyObject *self, PyObject *args);
	static PyObject *Advise(PyObject *self, PyObject *args);
	static PyObject *QueryIdentity(PyObject *self, PyObject *args);
	static PyObject *OpenMsgStore(PyObject *self, PyObject *args);
	static PyObject *OpenEntry(PyObject *self, PyObject *args);
protected:
	PyIMAPISession(IUnknown *);
	~PyIMAPISession();
};

