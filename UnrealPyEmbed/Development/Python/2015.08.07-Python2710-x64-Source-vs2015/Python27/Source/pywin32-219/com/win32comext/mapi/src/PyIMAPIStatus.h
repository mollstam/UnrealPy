class PyIMAPIStatus : public PyIMAPIProp
{
public:
MAKE_PYCOM_CTOR(PyIMAPIStatus);
static PyComTypeObject type;
static IMAPIStatus *GetI(PyObject *self);
	static PyObject *FlushQueues(PyObject *self, PyObject *args);
	static PyObject *ValidateState(PyObject *self, PyObject *args);
	static PyObject *SettingsDialog(PyObject *self, PyObject *args);
	static PyObject *ChangePassword(PyObject *self, PyObject *args);
protected:
	PyIMAPIStatus(IUnknown *);
	~PyIMAPIStatus();
};

