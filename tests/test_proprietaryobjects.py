import pytest
from BAC0.core.proprietary_objects.object import create_proprietary_object

from bacpypes.primitivedata import (
    Real,
    Boolean,
    CharacterString,
    Enumerated,
    Unsigned,
    Atomic,
    Date,
    Time,
    OctetString,
)
from bacpypes.object import (
    Object,
    DeviceObject,
    AnalogValueObject,
    AnalogInputObject,
    AnalogOutputObject,
    BinaryValueObject,
    BinaryInputObject,
    BinaryOutputObject,
    Property,
    register_object_type,
)
from bacpypes.constructeddata import (
    Any,
    Array,
    ArrayOf,
    List,
    ListOf,
    Choice,
    Element,
    Sequence,
)

MyDeviceProprietaryProperties = {
    "name": "MyDeviceProprietaryProperties",
    "vendor_id": 842,
    "objectType": "binaryValue",  # Yes the object type in question is of type binaryValue
    "bacpypes_type": BinaryValueObject,
    "properties": {
        "My_Constructed_Data": {"obj_id": 1234, "datatype": Array, "mutable": False},
    },
}

legacy = {
    "name": "MyDeviceProprietaryProperties",
    "vendor_id": 842,
    "objectType": "binaryValue",  # Yes the object type in question is of type binaryValue
    "bacpypes_type": BinaryValueObject,
    "properties": {
        "My_Constructed_Data": {"obj_id": 1234, "primitive": Array, "mutable": False},
    },
}

wrong = {
    "name": "MyDeviceProprietaryProperties",
    "vendor_id": 842,
    "objectType": "binaryValue",  # Yes the object type in question is of type binaryValue
    "bacpypes_type": BinaryValueObject,
    "properties": {
        "My_Constructed_Data": {"obj_id": 1234, "wrongname": Array, "mutable": False},
    },
}

no_vendor_id = {
    "name": "MyDeviceProprietaryProperties",
    "vendor_id": 0,
    "objectType": "binaryValue",  # Yes the object type in question is of type binaryValue
    "bacpypes_type": BinaryValueObject,
    "properties": {
        "My_Constructed_Data": {"obj_id": 1234, "wrongname": Array, "mutable": False},
    },
}


def test_create_object_using_datatype_keyname():
    create_proprietary_object(MyDeviceProprietaryProperties)


def test_create_object_using_primitive_keyname():
    create_proprietary_object(legacy)


def test_create_object_using_wrong_keyname():
    with pytest.raises(KeyError):
        create_proprietary_object(wrong)


def test_create_object_no_vendor_id():
    with pytest.raises(ValueError):
        create_proprietary_object(no_vendor_id)
