___all__ = ['UUIDS']


class Immutable(type):

    def __call__(*args):
        raise Exception("You can't create instance of immutable object")

    def __setattr__(*args):
        raise Exception("You can't modify immutable object")


class UUIDS(object):

    __metaclass__ = Immutable

    BASE = "0000%s-0000-1000-8000-00805f9b34fb"

    SERVICE_MIBAND1 = BASE % 'fee0'
    SERVICE_MIBAND2 = BASE % 'fee1'

    SERVICE_ALERT = BASE % '1802'
    SERVICE_ALERT_NOTIFICATION = BASE % '1811'
    SERVICE_HEART_RATE = BASE % '180d'
    SERVICE_DEVICE_INFO = BASE % '180a'

    #attr handle = 0x0001, end grp handle = 0x0007 uuid: 00001800-0000-1000-8000-00805f9b34fb   @UUID_SERVICE_GENERIC_ACCESS
    #attr handle = 0x0008, end grp handle = 0x000b uuid: 00001801-0000-1000-8000-00805f9b34fb   @UUID_SERVICE_GENERIC_ATTRIBUTE
    #attr handle = 0x000c, end grp handle = 0x0016 uuid: 0000180a-0000-1000-8000-00805f9b34fb   @SERVICE_DEVICE_INFO
    #attr handle = 0x0017, end grp handle = 0x001c uuid: 00001530-0000-3512-2118-0009af100700   @UUID_SERVICE_FIRMWARE
    #attr handle = 0x001d, end grp handle = 0x0023 uuid: 00001811-0000-1000-8000-00805f9b34fb   @SERVICE_ALERT_NOTIFICATION
    #attr handle = 0x0024, end grp handle = 0x0026 uuid: 00001802-0000-1000-8000-00805f9b34fb   @SERVICE_ALERT
    #attr handle = 0x0027, end grp handle = 0x002c uuid: 0000180d-0000-1000-8000-00805f9b34fb   @SERVICE_HEART_RATE
    #attr handle = 0x002d, end grp handle = 0x0051 uuid: 0000fee0-0000-1000-8000-00805f9b34fb   @SERVICE_MIBAND1
    #attr handle = 0x0052, end grp handle = 0x0066 uuid: 0000fee1-0000-1000-8000-00805f9b34fb   @SERVICE_MIBAND2

    #handle = 0x0002, char properties = 0x02, char value handle = 0x0003, uuid = 00002a00-0000-1000-8000-00805f9b34fb
    #handle = 0x0004, char properties = 0x02, char value handle = 0x0005, uuid = 00002a01-0000-1000-8000-00805f9b34fb
    #handle = 0x0006, char properties = 0x02, char value handle = 0x0007, uuid = 00002a04-0000-1000-8000-00805f9b34fb
    #handle = 0x0009, char properties = 0x22, char value handle = 0x000a, uuid = 00002a05-0000-1000-8000-00805f9b34fb
    #handle = 0x000d, char properties = 0x02, char value handle = 0x000e, uuid = 00002a25-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_SERIAL
    #handle = 0x000f, char properties = 0x02, char value handle = 0x0010, uuid = 00002a27-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_HRDW_REVISION
    #handle = 0x0011, char properties = 0x02, char value handle = 0x0012, uuid = 00002a28-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_REVISION
    #handle = 0x0013, char properties = 0x02, char value handle = 0x0014, uuid = 00002a23-0000-1000-8000-00805f9b34fb
    #handle = 0x0015, char properties = 0x02, char value handle = 0x0016, uuid = 00002a50-0000-1000-8000-00805f9b34fb
    #handle = 0x0018, char properties = 0x18, char value handle = 0x0019, uuid = 00001531-0000-3512-2118-0009af100700   @fw_ctrl
    #handle = 0x001b, char properties = 0x04, char value handle = 0x001c, uuid = 00001532-0000-3512-2118-0009af100700   @fw_data
    #handle = 0x001e, char properties = 0x08, char value handle = 0x001f, uuid = 00002a46-0000-1000-8000-00805f9b34fb
    #handle = 0x0021, char properties = 0x1a, char value handle = 0x0022, uuid = 00002a44-0000-1000-8000-00805f9b34fb
    #handle = 0x0025, char properties = 0x04, char value handle = 0x0026, uuid = 00002a06-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_ALERT
    #handle = 0x0028, char properties = 0x10, char value handle = 0x0029, uuid = 00002a37-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_HEART_RATE_MEASURE
    #handle = 0x002b, char properties = 0x0a, char value handle = 0x002c, uuid = 00002a39-0000-1000-8000-00805f9b34fb   @CHARACTERISTIC_HEART_RATE_CONTROL
    #handle = 0x002e, char properties = 0x1a, char value handle = 0x002f, uuid = 00002a2b-0000-1000-8000-00805f9b34fb
    #handle = 0x0031, char properties = 0x16, char value handle = 0x0032, uuid = 00000020-0000-3512-2118-0009af100700
    #handle = 0x0034, char properties = 0x14, char value handle = 0x0035, uuid = 00000001-0000-3512-2118-0009af100700   @CHARACTERISTIC_SENSOR
    #handle = 0x0037, char properties = 0x10, char value handle = 0x0038, uuid = 00000002-0000-3512-2118-0009af100700   @CHARACTERISTIC_HZ
    #handle = 0x003a, char properties = 0x14, char value handle = 0x003b, uuid = 00000003-0000-3512-2118-0009af100700   @CHARACTERISTIC_CONFIGURATION
    #handle = 0x003d, char properties = 0x16, char value handle = 0x003e, uuid = 00002a04-0000-1000-8000-00805f9b34fb
    #handle = 0x0040, char properties = 0x14, char value handle = 0x0041, uuid = 00000004-0000-3512-2118-0009af100700   @CHARACTERISTIC_FETCH
    #handle = 0x0043, char properties = 0x10, char value handle = 0x0044, uuid = 00000005-0000-3512-2118-0009af100700   @CHARACTERISTIC_ACTIVITY_DATA
    #handle = 0x0046, char properties = 0x12, char value handle = 0x0047, uuid = 00000006-0000-3512-2118-0009af100700   @CHARACTERISTIC_BATTERY
    #handle = 0x0049, char properties = 0x12, char value handle = 0x004a, uuid = 00000007-0000-3512-2118-0009af100700   @CHARACTERISTIC_STEPS
    #handle = 0x004c, char properties = 0x18, char value handle = 0x004d, uuid = 00000008-0000-3512-2118-0009af100700   @CHARACTERISTIC_USER_SETTINGS
    #handle = 0x004f, char properties = 0x10, char value handle = 0x0050, uuid = 00000010-0000-3512-2118-0009af100700   @CHARACTERISTIC_DEVICEEVENT
    #handle = 0x0053, char properties = 0x16, char value handle = 0x0054, uuid = 00000009-0000-3512-2118-0009af100700   @CHARACTERISTIC_AUTH
    #handle = 0x0056, char properties = 0x08, char value handle = 0x0057, uuid = 0000fedd-0000-1000-8000-00805f9b34fb
    #handle = 0x0058, char properties = 0x02, char value handle = 0x0059, uuid = 0000fede-0000-1000-8000-00805f9b34fb
    #handle = 0x005a, char properties = 0x02, char value handle = 0x005b, uuid = 0000fedf-0000-1000-8000-00805f9b34fb
    #handle = 0x005c, char properties = 0x0a, char value handle = 0x005d, uuid = 0000fed0-0000-1000-8000-00805f9b34fb
    #handle = 0x005e, char properties = 0x0a, char value handle = 0x005f, uuid = 0000fed1-0000-1000-8000-00805f9b34fb
    #handle = 0x0060, char properties = 0x02, char value handle = 0x0061, uuid = 0000fed2-0000-1000-8000-00805f9b34fb
    #handle = 0x0062, char properties = 0x0a, char value handle = 0x0063, uuid = 0000fed3-0000-1000-8000-00805f9b34fb
    #handle = 0x0064, char properties = 0x1a, char value handle = 0x0065, uuid = 0000fec1-0000-3512-2118-0009af100700

    CHARACTERISTIC_HZ = "00000002-0000-3512-2118-0009af100700"
    CHARACTERISTIC_SENSOR = "00000001-0000-3512-2118-0009af100700"
    CHARACTERISTIC_AUTH = "00000009-0000-3512-2118-0009af100700"
    CHARACTERISTIC_HEART_RATE_MEASURE = "00002a37-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_HEART_RATE_CONTROL = "00002a39-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_ALERT = "00002a06-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_BATTERY = "00000006-0000-3512-2118-0009af100700"
    CHARACTERISTIC_STEPS = "00000007-0000-3512-2118-0009af100700"
    CHARACTERISTIC_LE_PARAMS = BASE % "FF09"
    CHARACTERISTIC_REVISION = 0x2a28
    CHARACTERISTIC_SERIAL = 0x2a25
    CHARACTERISTIC_HRDW_REVISION = 0x2a27
    CHARACTERISTIC_CONFIGURATION = "00000003-0000-3512-2118-0009af100700"
    CHARACTERISTIC_DEVICEEVENT = "00000010-0000-3512-2118-0009af100700"

    CHARACTERISTIC_CURRENT_TIME = BASE % '2A2B'
    CHARACTERISTIC_AGE = BASE % '2A80'
    CHARACTERISTIC_USER_SETTINGS = "00000008-0000-3512-2118-0009af100700"

    CHARACTERISTIC_ACTIVITY_DATA = "00000005-0000-3512-2118-0009af100700"
    CHARACTERISTIC_FETCH = "00000004-0000-3512-2118-0009af100700"

    NOTIFICATION_DESCRIPTOR = 0x2902


class AUTH_STATES(object):

    __metaclass__ = Immutable

    AUTH_OK = "Auth ok"
    AUTH_FAILED = "Auth failed"
    ENCRIPTION_KEY_FAILED = "Encryption key auth fail, sending new key"
    KEY_SENDING_FAILED = "Key sending failed"
    REQUEST_RN_ERROR = "Something went wrong when requesting the random number"


class ALERT_TYPES(object):

    __metaclass__ = Immutable

    NONE = b'\x00'
    MESSAGE = b'\x01'
    PHONE = b'\x02'


class QUEUE_TYPES(object):

    __metaclass__ = Immutable

    HEART = 'heart'
    RAW_ACCEL = 'raw_accel'
    RAW_HEART = 'raw_heart'
    BUTTON = 'button'
