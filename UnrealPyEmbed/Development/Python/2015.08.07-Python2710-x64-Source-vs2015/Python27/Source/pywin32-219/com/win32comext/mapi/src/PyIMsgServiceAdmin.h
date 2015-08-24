class PyIMsgServiceAdmin : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIMsgServiceAdmin);
static PyComTypeObject type;
static IMsgServiceAdmin *GetI(PyObject *self);
	static PyObject *AdminProviders(PyObject *self, PyObject *args);
	static PyObject *OpenProfileSection(PyObject *self, PyObject *args);
	static PyObject *RenameMsgService(PyObject *self, PyObject *args);
	static PyObject *DeleteMsgService(PyObject *self, PyObject *args);
	static PyObject *GetProviderTable(PyObject *self, PyObject *args);
	static PyObject *GetMsgServiceTable(PyObject *self, PyObject *args);
	static PyObject *ConfigureMsgService(PyObject *self, PyObject *args);
	static PyObject *CreateMsgService(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
protected:
	PyIMsgServiceAdmin(IUnknown *);
	~PyIMsgServiceAdmin();
};

