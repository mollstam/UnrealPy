class PyIExchangeManageStore : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIExchangeManageStore);
static PyComTypeObject type;
static IExchangeManageStore *GetI(PyObject *self);
	static PyObject *CreateStoreEntryID(PyObject *self, PyObject *args);
protected:
	PyIExchangeManageStore(IUnknown *);
	~PyIExchangeManageStore();
};

