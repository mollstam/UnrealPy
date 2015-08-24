class PyIProfAdmin : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIProfAdmin);
static PyComTypeObject type;
static IProfAdmin *GetI(PyObject *self);
	static PyObject *AdminServices(PyObject *self, PyObject *args);
	static PyObject *SetDefaultProfile(PyObject *self, PyObject *args);
	static PyObject *RenameProfile(PyObject *self, PyObject *args);
	static PyObject *CopyProfile(PyObject *self, PyObject *args);
	static PyObject *ChangeProfilePassword(PyObject *self, PyObject *args);
	static PyObject *DeleteProfile(PyObject *self, PyObject *args);
	static PyObject *GetProfileTable(PyObject *self, PyObject *args);
	static PyObject *CreateProfile(PyObject *self, PyObject *args);
	static PyObject *GetLastError(PyObject *self, PyObject *args);
protected:
	PyIProfAdmin(IUnknown *);
	~PyIProfAdmin();
};

