# SNMP MIB module (WebGraph-AnalogIO-57661-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-AnalogIO-57661-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wut_ObjectIdentity = ObjectIdentity
wut = _Wut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040)
)
_WtComServer_ObjectIdentity = ObjectIdentity
wtComServer = _WtComServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1)
)
_WtWebio_ObjectIdentity = ObjectIdentity
wtWebio = _WtWebio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2)
)
_WtWebGraphAnalog57661_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661 = _WtWebGraphAnalog57661_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28)
)
_WtWebGraphAnalog57661Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Inventory = _WtWebGraphAnalog57661Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1)
)


class _WtWebGraphAnalog57661Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalog57661Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57661Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661Sensors_Object = MibScalar
wtWebGraphAnalog57661Sensors = _WtWebGraphAnalog57661Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 1),
    _WtWebGraphAnalog57661Sensors_Type()
)
wtWebGraphAnalog57661Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Sensors.setStatus("mandatory")
_WtWebGraphAnalog57661SensorTable_Object = MibTable
wtWebGraphAnalog57661SensorTable = _WtWebGraphAnalog57661SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorTable.setStatus("mandatory")
_WtWebGraphAnalog57661SensorEntry_Object = MibTableRow
wtWebGraphAnalog57661SensorEntry = _WtWebGraphAnalog57661SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 2, 1)
)
wtWebGraphAnalog57661SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57661SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57661SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661SensorNo_Object = MibTableColumn
wtWebGraphAnalog57661SensorNo = _WtWebGraphAnalog57661SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 2, 1, 1),
    _WtWebGraphAnalog57661SensorNo_Type()
)
wtWebGraphAnalog57661SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorNo.setStatus("mandatory")
_WtWebGraphAnalog57661ValuesTable_Object = MibTable
wtWebGraphAnalog57661ValuesTable = _WtWebGraphAnalog57661ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57661ValuesEntry_Object = MibTableRow
wtWebGraphAnalog57661ValuesEntry = _WtWebGraphAnalog57661ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 3, 1)
)
wtWebGraphAnalog57661ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661Values_Type(OctetString):
    """Custom type wtWebGraphAnalog57661Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAnalog57661Values_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661Values_Object = MibTableColumn
wtWebGraphAnalog57661Values = _WtWebGraphAnalog57661Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 3, 1, 1),
    _WtWebGraphAnalog57661Values_Type()
)
wtWebGraphAnalog57661Values.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Values.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryValuesTable_Object = MibTable
wtWebGraphAnalog57661BinaryValuesTable = _WtWebGraphAnalog57661BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalog57661BinaryValuesEntry = _WtWebGraphAnalog57661BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 4, 1)
)
wtWebGraphAnalog57661BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryValues_Type = Integer32
_WtWebGraphAnalog57661BinaryValues_Object = MibTableColumn
wtWebGraphAnalog57661BinaryValues = _WtWebGraphAnalog57661BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 1, 4, 1, 1),
    _WtWebGraphAnalog57661BinaryValues_Type()
)
wtWebGraphAnalog57661BinaryValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryValues.setStatus("mandatory")
_WtWebGraphAnalog57661SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661SessCntrl = _WtWebGraphAnalog57661SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2)
)
_WtWebGraphAnalog57661SessCntrlPassword_Type = OctetString
_WtWebGraphAnalog57661SessCntrlPassword_Object = MibScalar
wtWebGraphAnalog57661SessCntrlPassword = _WtWebGraphAnalog57661SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2, 1),
    _WtWebGraphAnalog57661SessCntrlPassword_Type()
)
wtWebGraphAnalog57661SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalog57661SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57661SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661SessCntrl-NoSession", 0),
          ("wtWebGraphAnalog57661SessCntrl-Session", 1))
    )


_WtWebGraphAnalog57661SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalog57661SessCntrlConfigMode = _WtWebGraphAnalog57661SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2, 2),
    _WtWebGraphAnalog57661SessCntrlConfigMode_Type()
)
wtWebGraphAnalog57661SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalog57661SessCntrlLogout_Type = Integer32
_WtWebGraphAnalog57661SessCntrlLogout_Object = MibScalar
wtWebGraphAnalog57661SessCntrlLogout = _WtWebGraphAnalog57661SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2, 3),
    _WtWebGraphAnalog57661SessCntrlLogout_Type()
)
wtWebGraphAnalog57661SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalog57661SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalog57661SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalog57661SessCntrlAdminPassword = _WtWebGraphAnalog57661SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2, 4),
    _WtWebGraphAnalog57661SessCntrlAdminPassword_Type()
)
wtWebGraphAnalog57661SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalog57661SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalog57661SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalog57661SessCntrlConfigPassword = _WtWebGraphAnalog57661SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 2, 5),
    _WtWebGraphAnalog57661SessCntrlConfigPassword_Type()
)
wtWebGraphAnalog57661SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalog57661Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Config = _WtWebGraphAnalog57661Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3)
)
_WtWebGraphAnalog57661Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Device = _WtWebGraphAnalog57661Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1)
)
_WtWebGraphAnalog57661Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Text = _WtWebGraphAnalog57661Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 1)
)
_WtWebGraphAnalog57661DeviceName_Type = OctetString
_WtWebGraphAnalog57661DeviceName_Object = MibScalar
wtWebGraphAnalog57661DeviceName = _WtWebGraphAnalog57661DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 1, 1),
    _WtWebGraphAnalog57661DeviceName_Type()
)
wtWebGraphAnalog57661DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DeviceName.setStatus("mandatory")
_WtWebGraphAnalog57661DeviceText_Type = OctetString
_WtWebGraphAnalog57661DeviceText_Object = MibScalar
wtWebGraphAnalog57661DeviceText = _WtWebGraphAnalog57661DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 1, 2),
    _WtWebGraphAnalog57661DeviceText_Type()
)
wtWebGraphAnalog57661DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DeviceText.setStatus("mandatory")
_WtWebGraphAnalog57661DeviceLocation_Type = OctetString
_WtWebGraphAnalog57661DeviceLocation_Object = MibScalar
wtWebGraphAnalog57661DeviceLocation = _WtWebGraphAnalog57661DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 1, 3),
    _WtWebGraphAnalog57661DeviceLocation_Type()
)
wtWebGraphAnalog57661DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalog57661DeviceContact_Type = OctetString
_WtWebGraphAnalog57661DeviceContact_Object = MibScalar
wtWebGraphAnalog57661DeviceContact = _WtWebGraphAnalog57661DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 1, 4),
    _WtWebGraphAnalog57661DeviceContact_Type()
)
wtWebGraphAnalog57661DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DeviceContact.setStatus("mandatory")
_WtWebGraphAnalog57661TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661TimeDate = _WtWebGraphAnalog57661TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2)
)
_WtWebGraphAnalog57661TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661TimeZone = _WtWebGraphAnalog57661TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1)
)
_WtWebGraphAnalog57661TzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57661TzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57661TzOffsetHrs = _WtWebGraphAnalog57661TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 1),
    _WtWebGraphAnalog57661TzOffsetHrs_Type()
)
wtWebGraphAnalog57661TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57661TzOffsetMin_Type = Integer32
_WtWebGraphAnalog57661TzOffsetMin_Object = MibScalar
wtWebGraphAnalog57661TzOffsetMin = _WtWebGraphAnalog57661TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 2),
    _WtWebGraphAnalog57661TzOffsetMin_Type()
)
wtWebGraphAnalog57661TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57661TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661TzEnable_Object = MibScalar
wtWebGraphAnalog57661TzEnable = _WtWebGraphAnalog57661TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 3),
    _WtWebGraphAnalog57661TzEnable_Type()
)
wtWebGraphAnalog57661TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TzEnable.setStatus("mandatory")
_WtWebGraphAnalog57661StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57661StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57661StTzOffsetHrs = _WtWebGraphAnalog57661StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 4),
    _WtWebGraphAnalog57661StTzOffsetHrs_Type()
)
wtWebGraphAnalog57661StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57661StTzOffsetMin_Type = Integer32
_WtWebGraphAnalog57661StTzOffsetMin_Object = MibScalar
wtWebGraphAnalog57661StTzOffsetMin = _WtWebGraphAnalog57661StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 5),
    _WtWebGraphAnalog57661StTzOffsetMin_Type()
)
wtWebGraphAnalog57661StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661StTzEnable_Object = MibScalar
wtWebGraphAnalog57661StTzEnable = _WtWebGraphAnalog57661StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 6),
    _WtWebGraphAnalog57661StTzEnable_Type()
)
wtWebGraphAnalog57661StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StartMonth-April", 4),
          ("wtWebGraphAnalog57661StartMonth-August", 8),
          ("wtWebGraphAnalog57661StartMonth-December", 12),
          ("wtWebGraphAnalog57661StartMonth-February", 2),
          ("wtWebGraphAnalog57661StartMonth-January", 1),
          ("wtWebGraphAnalog57661StartMonth-July", 7),
          ("wtWebGraphAnalog57661StartMonth-June", 6),
          ("wtWebGraphAnalog57661StartMonth-March", 3),
          ("wtWebGraphAnalog57661StartMonth-May", 5),
          ("wtWebGraphAnalog57661StartMonth-November", 11),
          ("wtWebGraphAnalog57661StartMonth-October", 10),
          ("wtWebGraphAnalog57661StartMonth-September", 9))
    )


_WtWebGraphAnalog57661StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStartMonth_Object = MibScalar
wtWebGraphAnalog57661StTzStartMonth = _WtWebGraphAnalog57661StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 7),
    _WtWebGraphAnalog57661StTzStartMonth_Type()
)
wtWebGraphAnalog57661StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StartMode-first", 1),
          ("wtWebGraphAnalog57661StartMode-fourth", 4),
          ("wtWebGraphAnalog57661StartMode-last", 5),
          ("wtWebGraphAnalog57661StartMode-second", 2),
          ("wtWebGraphAnalog57661StartMode-third", 3))
    )


_WtWebGraphAnalog57661StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStartMode_Object = MibScalar
wtWebGraphAnalog57661StTzStartMode = _WtWebGraphAnalog57661StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 8),
    _WtWebGraphAnalog57661StTzStartMode_Type()
)
wtWebGraphAnalog57661StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStartWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StartWday-Friday", 6),
          ("wtWebGraphAnalog57661StartWday-Monday", 2),
          ("wtWebGraphAnalog57661StartWday-Saturday", 7),
          ("wtWebGraphAnalog57661StartWday-Sunday", 1),
          ("wtWebGraphAnalog57661StartWday-Thursday", 4),
          ("wtWebGraphAnalog57661StartWday-Tuesday", 3),
          ("wtWebGraphAnalog57661StartWday-Wednesday", 5))
    )


_WtWebGraphAnalog57661StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStartWday_Object = MibScalar
wtWebGraphAnalog57661StTzStartWday = _WtWebGraphAnalog57661StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 9),
    _WtWebGraphAnalog57661StTzStartWday_Type()
)
wtWebGraphAnalog57661StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalog57661StTzStartHrs_Type = Integer32
_WtWebGraphAnalog57661StTzStartHrs_Object = MibScalar
wtWebGraphAnalog57661StTzStartHrs = _WtWebGraphAnalog57661StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 10),
    _WtWebGraphAnalog57661StTzStartHrs_Type()
)
wtWebGraphAnalog57661StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalog57661StTzStartMin_Type = Integer32
_WtWebGraphAnalog57661StTzStartMin_Object = MibScalar
wtWebGraphAnalog57661StTzStartMin = _WtWebGraphAnalog57661StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 11),
    _WtWebGraphAnalog57661StTzStartMin_Type()
)
wtWebGraphAnalog57661StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStopMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StopMonth-April", 4),
          ("wtWebGraphAnalog57661StopMonth-August", 8),
          ("wtWebGraphAnalog57661StopMonth-December", 12),
          ("wtWebGraphAnalog57661StopMonth-February", 2),
          ("wtWebGraphAnalog57661StopMonth-January", 1),
          ("wtWebGraphAnalog57661StopMonth-July", 7),
          ("wtWebGraphAnalog57661StopMonth-June", 6),
          ("wtWebGraphAnalog57661StopMonth-March", 3),
          ("wtWebGraphAnalog57661StopMonth-May", 5),
          ("wtWebGraphAnalog57661StopMonth-November", 11),
          ("wtWebGraphAnalog57661StopMonth-October", 10),
          ("wtWebGraphAnalog57661StopMonth-September", 9))
    )


_WtWebGraphAnalog57661StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStopMonth_Object = MibScalar
wtWebGraphAnalog57661StTzStopMonth = _WtWebGraphAnalog57661StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 12),
    _WtWebGraphAnalog57661StTzStopMonth_Type()
)
wtWebGraphAnalog57661StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StopMode-first", 1),
          ("wtWebGraphAnalog57661StopMode-fourth", 4),
          ("wtWebGraphAnalog57661StopMode-last", 5),
          ("wtWebGraphAnalog57661StopMode-second", 2),
          ("wtWebGraphAnalog57661StopMode-third", 3))
    )


_WtWebGraphAnalog57661StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStopMode_Object = MibScalar
wtWebGraphAnalog57661StTzStopMode = _WtWebGraphAnalog57661StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 13),
    _WtWebGraphAnalog57661StTzStopMode_Type()
)
wtWebGraphAnalog57661StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalog57661StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57661StTzStopWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661StopWday-Friday", 6),
          ("wtWebGraphAnalog57661StopWday-Monday", 2),
          ("wtWebGraphAnalog57661StopWday-Saturday", 7),
          ("wtWebGraphAnalog57661StopWday-Sunday", 1),
          ("wtWebGraphAnalog57661StopWday-Thursday", 4),
          ("wtWebGraphAnalog57661StopWday-Tuesday", 3),
          ("wtWebGraphAnalog57661StopWday-Wednesday", 5))
    )


_WtWebGraphAnalog57661StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661StTzStopWday_Object = MibScalar
wtWebGraphAnalog57661StTzStopWday = _WtWebGraphAnalog57661StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 14),
    _WtWebGraphAnalog57661StTzStopWday_Type()
)
wtWebGraphAnalog57661StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalog57661StTzStopHrs_Type = Integer32
_WtWebGraphAnalog57661StTzStopHrs_Object = MibScalar
wtWebGraphAnalog57661StTzStopHrs = _WtWebGraphAnalog57661StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 15),
    _WtWebGraphAnalog57661StTzStopHrs_Type()
)
wtWebGraphAnalog57661StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalog57661StTzStopMin_Type = Integer32
_WtWebGraphAnalog57661StTzStopMin_Object = MibScalar
wtWebGraphAnalog57661StTzStopMin = _WtWebGraphAnalog57661StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 1, 16),
    _WtWebGraphAnalog57661StTzStopMin_Type()
)
wtWebGraphAnalog57661StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalog57661TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661TimeServer = _WtWebGraphAnalog57661TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 2)
)
_WtWebGraphAnalog57661TimeServer1_Type = OctetString
_WtWebGraphAnalog57661TimeServer1_Object = MibScalar
wtWebGraphAnalog57661TimeServer1 = _WtWebGraphAnalog57661TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 2, 1),
    _WtWebGraphAnalog57661TimeServer1_Type()
)
wtWebGraphAnalog57661TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TimeServer1.setStatus("mandatory")
_WtWebGraphAnalog57661TimeServer2_Type = OctetString
_WtWebGraphAnalog57661TimeServer2_Object = MibScalar
wtWebGraphAnalog57661TimeServer2 = _WtWebGraphAnalog57661TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 2, 2),
    _WtWebGraphAnalog57661TimeServer2_Type()
)
wtWebGraphAnalog57661TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalog57661TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661TsEnable_Object = MibScalar
wtWebGraphAnalog57661TsEnable = _WtWebGraphAnalog57661TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 2, 3),
    _WtWebGraphAnalog57661TsEnable_Type()
)
wtWebGraphAnalog57661TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TsEnable.setStatus("mandatory")
_WtWebGraphAnalog57661TsSyncTime_Type = Integer32
_WtWebGraphAnalog57661TsSyncTime_Object = MibScalar
wtWebGraphAnalog57661TsSyncTime = _WtWebGraphAnalog57661TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 2, 4),
    _WtWebGraphAnalog57661TsSyncTime_Type()
)
wtWebGraphAnalog57661TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalog57661DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661DeviceClock = _WtWebGraphAnalog57661DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3)
)


class _WtWebGraphAnalog57661ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalog57661ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ClockHrs_Object = MibScalar
wtWebGraphAnalog57661ClockHrs = _WtWebGraphAnalog57661ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3, 1),
    _WtWebGraphAnalog57661ClockHrs_Type()
)
wtWebGraphAnalog57661ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalog57661ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalog57661ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ClockMin_Object = MibScalar
wtWebGraphAnalog57661ClockMin = _WtWebGraphAnalog57661ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3, 2),
    _WtWebGraphAnalog57661ClockMin_Type()
)
wtWebGraphAnalog57661ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ClockMin.setStatus("mandatory")


class _WtWebGraphAnalog57661ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalog57661ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ClockDay_Object = MibScalar
wtWebGraphAnalog57661ClockDay = _WtWebGraphAnalog57661ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3, 3),
    _WtWebGraphAnalog57661ClockDay_Type()
)
wtWebGraphAnalog57661ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ClockDay.setStatus("mandatory")


class _WtWebGraphAnalog57661ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ClockMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661ClockMonth-April", 4),
          ("wtWebGraphAnalog57661ClockMonth-August", 8),
          ("wtWebGraphAnalog57661ClockMonth-December", 12),
          ("wtWebGraphAnalog57661ClockMonth-February", 2),
          ("wtWebGraphAnalog57661ClockMonth-January", 1),
          ("wtWebGraphAnalog57661ClockMonth-July", 7),
          ("wtWebGraphAnalog57661ClockMonth-June", 6),
          ("wtWebGraphAnalog57661ClockMonth-March", 3),
          ("wtWebGraphAnalog57661ClockMonth-May", 5),
          ("wtWebGraphAnalog57661ClockMonth-November", 11),
          ("wtWebGraphAnalog57661ClockMonth-October", 10),
          ("wtWebGraphAnalog57661ClockMonth-September", 9))
    )


_WtWebGraphAnalog57661ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ClockMonth_Object = MibScalar
wtWebGraphAnalog57661ClockMonth = _WtWebGraphAnalog57661ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3, 4),
    _WtWebGraphAnalog57661ClockMonth_Type()
)
wtWebGraphAnalog57661ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalog57661ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57661ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ClockYear_Object = MibScalar
wtWebGraphAnalog57661ClockYear = _WtWebGraphAnalog57661ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 2, 3, 5),
    _WtWebGraphAnalog57661ClockYear_Type()
)
wtWebGraphAnalog57661ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ClockYear.setStatus("mandatory")
_WtWebGraphAnalog57661Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Basic = _WtWebGraphAnalog57661Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3)
)
_WtWebGraphAnalog57661Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Network = _WtWebGraphAnalog57661Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1)
)
_WtWebGraphAnalog57661IpAddress_Type = IpAddress
_WtWebGraphAnalog57661IpAddress_Object = MibScalar
wtWebGraphAnalog57661IpAddress = _WtWebGraphAnalog57661IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 1),
    _WtWebGraphAnalog57661IpAddress_Type()
)
wtWebGraphAnalog57661IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661IpAddress.setStatus("mandatory")
_WtWebGraphAnalog57661SubnetMask_Type = IpAddress
_WtWebGraphAnalog57661SubnetMask_Object = MibScalar
wtWebGraphAnalog57661SubnetMask = _WtWebGraphAnalog57661SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 2),
    _WtWebGraphAnalog57661SubnetMask_Type()
)
wtWebGraphAnalog57661SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SubnetMask.setStatus("mandatory")
_WtWebGraphAnalog57661Gateway_Type = IpAddress
_WtWebGraphAnalog57661Gateway_Object = MibScalar
wtWebGraphAnalog57661Gateway = _WtWebGraphAnalog57661Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 3),
    _WtWebGraphAnalog57661Gateway_Type()
)
wtWebGraphAnalog57661Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Gateway.setStatus("mandatory")
_WtWebGraphAnalog57661DnsServer1_Type = OctetString
_WtWebGraphAnalog57661DnsServer1_Object = MibScalar
wtWebGraphAnalog57661DnsServer1 = _WtWebGraphAnalog57661DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 4),
    _WtWebGraphAnalog57661DnsServer1_Type()
)
wtWebGraphAnalog57661DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DnsServer1.setStatus("mandatory")
_WtWebGraphAnalog57661DnsServer2_Type = OctetString
_WtWebGraphAnalog57661DnsServer2_Object = MibScalar
wtWebGraphAnalog57661DnsServer2 = _WtWebGraphAnalog57661DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 5),
    _WtWebGraphAnalog57661DnsServer2_Type()
)
wtWebGraphAnalog57661DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DnsServer2.setStatus("mandatory")
_WtWebGraphAnalog57661AddConfig_Type = OctetString
_WtWebGraphAnalog57661AddConfig_Object = MibScalar
wtWebGraphAnalog57661AddConfig = _WtWebGraphAnalog57661AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 1, 6),
    _WtWebGraphAnalog57661AddConfig_Type()
)
wtWebGraphAnalog57661AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AddConfig.setStatus("mandatory")
_WtWebGraphAnalog57661HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661HTTP = _WtWebGraphAnalog57661HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 2)
)
_WtWebGraphAnalog57661Startup_Type = OctetString
_WtWebGraphAnalog57661Startup_Object = MibScalar
wtWebGraphAnalog57661Startup = _WtWebGraphAnalog57661Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 2, 1),
    _WtWebGraphAnalog57661Startup_Type()
)
wtWebGraphAnalog57661Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Startup.setStatus("mandatory")
_WtWebGraphAnalog57661GetHeaderEnable_Type = OctetString
_WtWebGraphAnalog57661GetHeaderEnable_Object = MibScalar
wtWebGraphAnalog57661GetHeaderEnable = _WtWebGraphAnalog57661GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 2, 2),
    _WtWebGraphAnalog57661GetHeaderEnable_Type()
)
wtWebGraphAnalog57661GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalog57661HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661HttpPort_Object = MibScalar
wtWebGraphAnalog57661HttpPort = _WtWebGraphAnalog57661HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 2, 3),
    _WtWebGraphAnalog57661HttpPort_Type()
)
wtWebGraphAnalog57661HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661HttpPort.setStatus("mandatory")
_WtWebGraphAnalog57661Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Mail = _WtWebGraphAnalog57661Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3)
)
_WtWebGraphAnalog57661MailAdName_Type = OctetString
_WtWebGraphAnalog57661MailAdName_Object = MibScalar
wtWebGraphAnalog57661MailAdName = _WtWebGraphAnalog57661MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 1),
    _WtWebGraphAnalog57661MailAdName_Type()
)
wtWebGraphAnalog57661MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailAdName.setStatus("mandatory")
_WtWebGraphAnalog57661MailReply_Type = OctetString
_WtWebGraphAnalog57661MailReply_Object = MibScalar
wtWebGraphAnalog57661MailReply = _WtWebGraphAnalog57661MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 2),
    _WtWebGraphAnalog57661MailReply_Type()
)
wtWebGraphAnalog57661MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailReply.setStatus("mandatory")
_WtWebGraphAnalog57661MailServer_Type = OctetString
_WtWebGraphAnalog57661MailServer_Object = MibScalar
wtWebGraphAnalog57661MailServer = _WtWebGraphAnalog57661MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 3),
    _WtWebGraphAnalog57661MailServer_Type()
)
wtWebGraphAnalog57661MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalog57661MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalog57661MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661MailAuthentication_Object = MibScalar
wtWebGraphAnalog57661MailAuthentication = _WtWebGraphAnalog57661MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 5),
    _WtWebGraphAnalog57661MailAuthentication_Type()
)
wtWebGraphAnalog57661MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalog57661MailAuthUser_Type = OctetString
_WtWebGraphAnalog57661MailAuthUser_Object = MibScalar
wtWebGraphAnalog57661MailAuthUser = _WtWebGraphAnalog57661MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 6),
    _WtWebGraphAnalog57661MailAuthUser_Type()
)
wtWebGraphAnalog57661MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalog57661MailAuthPassword_Type = OctetString
_WtWebGraphAnalog57661MailAuthPassword_Object = MibScalar
wtWebGraphAnalog57661MailAuthPassword = _WtWebGraphAnalog57661MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 7),
    _WtWebGraphAnalog57661MailAuthPassword_Type()
)
wtWebGraphAnalog57661MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalog57661MailPop3Server_Type = OctetString
_WtWebGraphAnalog57661MailPop3Server_Object = MibScalar
wtWebGraphAnalog57661MailPop3Server = _WtWebGraphAnalog57661MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 3, 8),
    _WtWebGraphAnalog57661MailPop3Server_Type()
)
wtWebGraphAnalog57661MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalog57661SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661SNMP = _WtWebGraphAnalog57661SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4)
)
_WtWebGraphAnalog57661SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalog57661SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalog57661SnmpCommunityStringRead = _WtWebGraphAnalog57661SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 1),
    _WtWebGraphAnalog57661SnmpCommunityStringRead_Type()
)
wtWebGraphAnalog57661SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalog57661SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalog57661SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalog57661SnmpCommunityStringReadWrite = _WtWebGraphAnalog57661SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 2),
    _WtWebGraphAnalog57661SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalog57661SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalog57661SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalog57661SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalog57661SystemTrapManagerIP = _WtWebGraphAnalog57661SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 3),
    _WtWebGraphAnalog57661SystemTrapManagerIP_Type()
)
wtWebGraphAnalog57661SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalog57661SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661SystemTrapEnable_Object = MibScalar
wtWebGraphAnalog57661SystemTrapEnable = _WtWebGraphAnalog57661SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 4),
    _WtWebGraphAnalog57661SystemTrapEnable_Type()
)
wtWebGraphAnalog57661SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalog57661SnmpEnable_Type = OctetString
_WtWebGraphAnalog57661SnmpEnable_Object = MibScalar
wtWebGraphAnalog57661SnmpEnable = _WtWebGraphAnalog57661SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 5),
    _WtWebGraphAnalog57661SnmpEnable_Type()
)
wtWebGraphAnalog57661SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalog57661SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalog57661SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalog57661SnmpCommunityStringTrap = _WtWebGraphAnalog57661SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 4, 6),
    _WtWebGraphAnalog57661SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalog57661SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalog57661UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661UDP = _WtWebGraphAnalog57661UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 5)
)


class _WtWebGraphAnalog57661UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661UdpPort_Object = MibScalar
wtWebGraphAnalog57661UdpPort = _WtWebGraphAnalog57661UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 5, 1),
    _WtWebGraphAnalog57661UdpPort_Type()
)
wtWebGraphAnalog57661UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661UdpPort.setStatus("mandatory")
_WtWebGraphAnalog57661UdpEnable_Type = OctetString
_WtWebGraphAnalog57661UdpEnable_Object = MibScalar
wtWebGraphAnalog57661UdpEnable = _WtWebGraphAnalog57661UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 5, 2),
    _WtWebGraphAnalog57661UdpEnable_Type()
)
wtWebGraphAnalog57661UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661UdpEnable.setStatus("mandatory")
_WtWebGraphAnalog57661Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Syslog = _WtWebGraphAnalog57661Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 6)
)
_WtWebGraphAnalog57661SyslogServerIP_Type = OctetString
_WtWebGraphAnalog57661SyslogServerIP_Object = MibScalar
wtWebGraphAnalog57661SyslogServerIP = _WtWebGraphAnalog57661SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 6, 1),
    _WtWebGraphAnalog57661SyslogServerIP_Type()
)
wtWebGraphAnalog57661SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalog57661SyslogServerPort_Type = Integer32
_WtWebGraphAnalog57661SyslogServerPort_Object = MibScalar
wtWebGraphAnalog57661SyslogServerPort = _WtWebGraphAnalog57661SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 6, 2),
    _WtWebGraphAnalog57661SyslogServerPort_Type()
)
wtWebGraphAnalog57661SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalog57661SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalog57661SyslogSystemMessagesEnable = _WtWebGraphAnalog57661SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 6, 3),
    _WtWebGraphAnalog57661SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalog57661SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalog57661SyslogEnable_Type = OctetString
_WtWebGraphAnalog57661SyslogEnable_Object = MibScalar
wtWebGraphAnalog57661SyslogEnable = _WtWebGraphAnalog57661SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 6, 4),
    _WtWebGraphAnalog57661SyslogEnable_Type()
)
wtWebGraphAnalog57661SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalog57661FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661FTP = _WtWebGraphAnalog57661FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7)
)
_WtWebGraphAnalog57661FTPServerIP_Type = OctetString
_WtWebGraphAnalog57661FTPServerIP_Object = MibScalar
wtWebGraphAnalog57661FTPServerIP = _WtWebGraphAnalog57661FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 1),
    _WtWebGraphAnalog57661FTPServerIP_Type()
)
wtWebGraphAnalog57661FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalog57661FTPServerControlPort_Type = Integer32
_WtWebGraphAnalog57661FTPServerControlPort_Object = MibScalar
wtWebGraphAnalog57661FTPServerControlPort = _WtWebGraphAnalog57661FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 2),
    _WtWebGraphAnalog57661FTPServerControlPort_Type()
)
wtWebGraphAnalog57661FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalog57661FTPUserName_Type = OctetString
_WtWebGraphAnalog57661FTPUserName_Object = MibScalar
wtWebGraphAnalog57661FTPUserName = _WtWebGraphAnalog57661FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 3),
    _WtWebGraphAnalog57661FTPUserName_Type()
)
wtWebGraphAnalog57661FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPUserName.setStatus("mandatory")
_WtWebGraphAnalog57661FTPPassword_Type = OctetString
_WtWebGraphAnalog57661FTPPassword_Object = MibScalar
wtWebGraphAnalog57661FTPPassword = _WtWebGraphAnalog57661FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 4),
    _WtWebGraphAnalog57661FTPPassword_Type()
)
wtWebGraphAnalog57661FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPPassword.setStatus("mandatory")
_WtWebGraphAnalog57661FTPAccount_Type = OctetString
_WtWebGraphAnalog57661FTPAccount_Object = MibScalar
wtWebGraphAnalog57661FTPAccount = _WtWebGraphAnalog57661FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 5),
    _WtWebGraphAnalog57661FTPAccount_Type()
)
wtWebGraphAnalog57661FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPAccount.setStatus("mandatory")
_WtWebGraphAnalog57661FTPOption_Type = OctetString
_WtWebGraphAnalog57661FTPOption_Object = MibScalar
wtWebGraphAnalog57661FTPOption = _WtWebGraphAnalog57661FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 6),
    _WtWebGraphAnalog57661FTPOption_Type()
)
wtWebGraphAnalog57661FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPOption.setStatus("mandatory")
_WtWebGraphAnalog57661FTPEnable_Type = OctetString
_WtWebGraphAnalog57661FTPEnable_Object = MibScalar
wtWebGraphAnalog57661FTPEnable = _WtWebGraphAnalog57661FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 7, 7),
    _WtWebGraphAnalog57661FTPEnable_Type()
)
wtWebGraphAnalog57661FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661FTPEnable.setStatus("mandatory")
_WtWebGraphAnalog57661Language_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Language = _WtWebGraphAnalog57661Language_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 8)
)
_WtWebGraphAnalog57661LanguageSelect_Type = OctetString
_WtWebGraphAnalog57661LanguageSelect_Object = MibScalar
wtWebGraphAnalog57661LanguageSelect = _WtWebGraphAnalog57661LanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 8, 1),
    _WtWebGraphAnalog57661LanguageSelect_Type()
)
wtWebGraphAnalog57661LanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661LanguageSelect.setStatus("mandatory")
_WtWebGraphAnalog57661Binary_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Binary = _WtWebGraphAnalog57661Binary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9)
)


class _WtWebGraphAnalog57661BinaryModeCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryModeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57661BinaryModeCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryModeCount_Object = MibScalar
wtWebGraphAnalog57661BinaryModeCount = _WtWebGraphAnalog57661BinaryModeCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 1),
    _WtWebGraphAnalog57661BinaryModeCount_Type()
)
wtWebGraphAnalog57661BinaryModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryModeCount.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryIfTable_Object = MibTable
wtWebGraphAnalog57661BinaryIfTable = _WtWebGraphAnalog57661BinaryIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryIfTable.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryIfEntry_Object = MibTableRow
wtWebGraphAnalog57661BinaryIfEntry = _WtWebGraphAnalog57661BinaryIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 2, 1)
)
wtWebGraphAnalog57661BinaryIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryModeNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryModeNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57661BinaryModeNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryModeNo_Object = MibTableColumn
wtWebGraphAnalog57661BinaryModeNo = _WtWebGraphAnalog57661BinaryModeNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 2, 1, 1),
    _WtWebGraphAnalog57661BinaryModeNo_Type()
)
wtWebGraphAnalog57661BinaryModeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryModeNo.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTable_Object = MibTable
wtWebGraphAnalog57661BinaryTable = _WtWebGraphAnalog57661BinaryTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTable.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryEntry_Object = MibTableRow
wtWebGraphAnalog57661BinaryEntry = _WtWebGraphAnalog57661BinaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1)
)
wtWebGraphAnalog57661BinaryEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryOperationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryOperationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryOperationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryOperationMode_Object = MibTableColumn
wtWebGraphAnalog57661BinaryOperationMode = _WtWebGraphAnalog57661BinaryOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 1),
    _WtWebGraphAnalog57661BinaryOperationMode_Type()
)
wtWebGraphAnalog57661BinaryOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryOperationMode.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpServerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpServerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpServerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpServerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerLocalPort = _WtWebGraphAnalog57661BinaryTcpServerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 2),
    _WtWebGraphAnalog57661BinaryTcpServerLocalPort_Type()
)
wtWebGraphAnalog57661BinaryTcpServerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpServerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryTcpServerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryTcpServerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryTcpServerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerInputTrigger = _WtWebGraphAnalog57661BinaryTcpServerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 3),
    _WtWebGraphAnalog57661BinaryTcpServerInputTrigger_Type()
)
wtWebGraphAnalog57661BinaryTcpServerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpServerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryTcpServerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryTcpServerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryTcpServerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerApplicationMode = _WtWebGraphAnalog57661BinaryTcpServerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 4),
    _WtWebGraphAnalog57661BinaryTcpServerApplicationMode_Type()
)
wtWebGraphAnalog57661BinaryTcpServerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpClientLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpClientLocalPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientLocalPort = _WtWebGraphAnalog57661BinaryTcpClientLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 5),
    _WtWebGraphAnalog57661BinaryTcpClientLocalPort_Type()
)
wtWebGraphAnalog57661BinaryTcpClientLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientServerPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpClientServerPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpClientServerPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientServerPort = _WtWebGraphAnalog57661BinaryTcpClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 6),
    _WtWebGraphAnalog57661BinaryTcpClientServerPort_Type()
)
wtWebGraphAnalog57661BinaryTcpClientServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientServerPort.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpClientServerIpAddr_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpClientServerIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientServerIpAddr = _WtWebGraphAnalog57661BinaryTcpClientServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 7),
    _WtWebGraphAnalog57661BinaryTcpClientServerIpAddr_Type()
)
wtWebGraphAnalog57661BinaryTcpClientServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientServerIpAddr.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpClientServerPassword_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpClientServerPassword_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientServerPassword = _WtWebGraphAnalog57661BinaryTcpClientServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 8),
    _WtWebGraphAnalog57661BinaryTcpClientServerPassword_Type()
)
wtWebGraphAnalog57661BinaryTcpClientServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientServerPassword.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpClientInactivity_Type = Integer32
_WtWebGraphAnalog57661BinaryTcpClientInactivity_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientInactivity = _WtWebGraphAnalog57661BinaryTcpClientInactivity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 9),
    _WtWebGraphAnalog57661BinaryTcpClientInactivity_Type()
)
wtWebGraphAnalog57661BinaryTcpClientInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientInactivity.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryTcpClientInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryTcpClientInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientInputTrigger = _WtWebGraphAnalog57661BinaryTcpClientInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 10),
    _WtWebGraphAnalog57661BinaryTcpClientInputTrigger_Type()
)
wtWebGraphAnalog57661BinaryTcpClientInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpClientInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpClientInterval_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientInterval = _WtWebGraphAnalog57661BinaryTcpClientInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 11),
    _WtWebGraphAnalog57661BinaryTcpClientInterval_Type()
)
wtWebGraphAnalog57661BinaryTcpClientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientInterval.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryTcpClientApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryTcpClientApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientApplicationMode = _WtWebGraphAnalog57661BinaryTcpClientApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 12),
    _WtWebGraphAnalog57661BinaryTcpClientApplicationMode_Type()
)
wtWebGraphAnalog57661BinaryTcpClientApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryUdpPeerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryUdpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryUdpPeerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryUdpPeerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerLocalPort = _WtWebGraphAnalog57661BinaryUdpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 13),
    _WtWebGraphAnalog57661BinaryUdpPeerLocalPort_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryUdpPeerRemotePort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryUdpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryUdpPeerRemotePort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryUdpPeerRemotePort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerRemotePort = _WtWebGraphAnalog57661BinaryUdpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 14),
    _WtWebGraphAnalog57661BinaryUdpPeerRemotePort_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerRemotePort.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr_Type = OctetString
_WtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr = _WtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 15),
    _WtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryUdpPeerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryUdpPeerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryUdpPeerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryUdpPeerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerInputTrigger = _WtWebGraphAnalog57661BinaryUdpPeerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 16),
    _WtWebGraphAnalog57661BinaryUdpPeerInputTrigger_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryUdpPeerInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryUdpPeerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57661BinaryUdpPeerInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryUdpPeerInterval_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerInterval = _WtWebGraphAnalog57661BinaryUdpPeerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 17),
    _WtWebGraphAnalog57661BinaryUdpPeerInterval_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerInterval.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryUdpPeerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661BinaryUdpPeerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661BinaryUdpPeerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661BinaryUdpPeerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerApplicationMode = _WtWebGraphAnalog57661BinaryUdpPeerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 18),
    _WtWebGraphAnalog57661BinaryUdpPeerApplicationMode_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryConnectedPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryConnectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryConnectedPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryConnectedPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryConnectedPort = _WtWebGraphAnalog57661BinaryConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 19),
    _WtWebGraphAnalog57661BinaryConnectedPort_Type()
)
wtWebGraphAnalog57661BinaryConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryConnectedPort.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryConnectedIpAddr_Type = IpAddress
_WtWebGraphAnalog57661BinaryConnectedIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661BinaryConnectedIpAddr = _WtWebGraphAnalog57661BinaryConnectedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 20),
    _WtWebGraphAnalog57661BinaryConnectedIpAddr_Type()
)
wtWebGraphAnalog57661BinaryConnectedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryConnectedIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpServerClientHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpServerClientHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpServerClientHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpServerClientHttpPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerClientHttpPort = _WtWebGraphAnalog57661BinaryTcpServerClientHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 21),
    _WtWebGraphAnalog57661BinaryTcpServerClientHttpPort_Type()
)
wtWebGraphAnalog57661BinaryTcpServerClientHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerClientHttpPort.setStatus("mandatory")


class _WtWebGraphAnalog57661BinaryTcpClientServerHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661BinaryTcpClientServerHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661BinaryTcpClientServerHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661BinaryTcpClientServerHttpPort_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientServerHttpPort = _WtWebGraphAnalog57661BinaryTcpClientServerHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 22),
    _WtWebGraphAnalog57661BinaryTcpClientServerHttpPort_Type()
)
wtWebGraphAnalog57661BinaryTcpClientServerHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientServerHttpPort.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpServerHysteresis1_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpServerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerHysteresis1 = _WtWebGraphAnalog57661BinaryTcpServerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 23),
    _WtWebGraphAnalog57661BinaryTcpServerHysteresis1_Type()
)
wtWebGraphAnalog57661BinaryTcpServerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpServerHysteresis2_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpServerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpServerHysteresis2 = _WtWebGraphAnalog57661BinaryTcpServerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 24),
    _WtWebGraphAnalog57661BinaryTcpServerHysteresis2_Type()
)
wtWebGraphAnalog57661BinaryTcpServerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpServerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpClientHysteresis1_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpClientHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientHysteresis1 = _WtWebGraphAnalog57661BinaryTcpClientHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 25),
    _WtWebGraphAnalog57661BinaryTcpClientHysteresis1_Type()
)
wtWebGraphAnalog57661BinaryTcpClientHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryTcpClientHysteresis2_Type = OctetString
_WtWebGraphAnalog57661BinaryTcpClientHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57661BinaryTcpClientHysteresis2 = _WtWebGraphAnalog57661BinaryTcpClientHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 26),
    _WtWebGraphAnalog57661BinaryTcpClientHysteresis2_Type()
)
wtWebGraphAnalog57661BinaryTcpClientHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryTcpClientHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryUdpPeerHysteresis1_Type = OctetString
_WtWebGraphAnalog57661BinaryUdpPeerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerHysteresis1 = _WtWebGraphAnalog57661BinaryUdpPeerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 27),
    _WtWebGraphAnalog57661BinaryUdpPeerHysteresis1_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57661BinaryUdpPeerHysteresis2_Type = OctetString
_WtWebGraphAnalog57661BinaryUdpPeerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57661BinaryUdpPeerHysteresis2 = _WtWebGraphAnalog57661BinaryUdpPeerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 3, 9, 3, 1, 28),
    _WtWebGraphAnalog57661BinaryUdpPeerHysteresis2_Type()
)
wtWebGraphAnalog57661BinaryUdpPeerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661BinaryUdpPeerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57661Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Datalogger = _WtWebGraphAnalog57661Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4)
)


class _WtWebGraphAnalog57661LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalog57661LoggerTimebase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661Datalogger-15Min", 5),
          ("wtWebGraphAnalog57661Datalogger-15Sec", 1),
          ("wtWebGraphAnalog57661Datalogger-1Min", 3),
          ("wtWebGraphAnalog57661Datalogger-30Sec", 2),
          ("wtWebGraphAnalog57661Datalogger-5Min", 4),
          ("wtWebGraphAnalog57661Datalogger-60Min", 6))
    )


_WtWebGraphAnalog57661LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661LoggerTimebase_Object = MibScalar
wtWebGraphAnalog57661LoggerTimebase = _WtWebGraphAnalog57661LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 1),
    _WtWebGraphAnalog57661LoggerTimebase_Type()
)
wtWebGraphAnalog57661LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalog57661LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57661LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661LoggerSensorSel_Object = MibScalar
wtWebGraphAnalog57661LoggerSensorSel = _WtWebGraphAnalog57661LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 2),
    _WtWebGraphAnalog57661LoggerSensorSel_Type()
)
wtWebGraphAnalog57661LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661LoggerSensorSel.setStatus("mandatory")


class _WtWebGraphAnalog57661DisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57661DisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661DisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661DisplaySensorSel_Object = MibScalar
wtWebGraphAnalog57661DisplaySensorSel = _WtWebGraphAnalog57661DisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 3),
    _WtWebGraphAnalog57661DisplaySensorSel_Type()
)
wtWebGraphAnalog57661DisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DisplaySensorSel.setStatus("mandatory")
_WtWebGraphAnalog57661SensorColorTable_Object = MibTable
wtWebGraphAnalog57661SensorColorTable = _WtWebGraphAnalog57661SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorColorTable.setStatus("mandatory")
_WtWebGraphAnalog57661SensorColorEntry_Object = MibTableRow
wtWebGraphAnalog57661SensorColorEntry = _WtWebGraphAnalog57661SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 4, 1)
)
wtWebGraphAnalog57661SensorColorEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorColorEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661SensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57661SensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57661SensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661SensorColor_Object = MibTableColumn
wtWebGraphAnalog57661SensorColor = _WtWebGraphAnalog57661SensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 4, 1, 1),
    _WtWebGraphAnalog57661SensorColor_Type()
)
wtWebGraphAnalog57661SensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorColor.setStatus("mandatory")
_WtWebGraphAnalog57661AutoScaleEnable_Type = OctetString
_WtWebGraphAnalog57661AutoScaleEnable_Object = MibScalar
wtWebGraphAnalog57661AutoScaleEnable = _WtWebGraphAnalog57661AutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 5),
    _WtWebGraphAnalog57661AutoScaleEnable_Type()
)
wtWebGraphAnalog57661AutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalog57661VerticalUpperLimit_Type = OctetString
_WtWebGraphAnalog57661VerticalUpperLimit_Object = MibScalar
wtWebGraphAnalog57661VerticalUpperLimit = _WtWebGraphAnalog57661VerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 6),
    _WtWebGraphAnalog57661VerticalUpperLimit_Type()
)
wtWebGraphAnalog57661VerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661VerticalUpperLimit.setStatus("mandatory")
_WtWebGraphAnalog57661VerticalLowerLimit_Type = OctetString
_WtWebGraphAnalog57661VerticalLowerLimit_Object = MibScalar
wtWebGraphAnalog57661VerticalLowerLimit = _WtWebGraphAnalog57661VerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 7),
    _WtWebGraphAnalog57661VerticalLowerLimit_Type()
)
wtWebGraphAnalog57661VerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661VerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphAnalog57661HorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphAnalog57661HorizontalZoom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57661Zoom-25days", 6),
          ("wtWebGraphAnalog57661Zoom-25min", 1),
          ("wtWebGraphAnalog57661Zoom-30hrs", 4),
          ("wtWebGraphAnalog57661Zoom-5days", 5),
          ("wtWebGraphAnalog57661Zoom-5hrs", 3),
          ("wtWebGraphAnalog57661Zoom-75min", 2))
    )


_WtWebGraphAnalog57661HorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661HorizontalZoom_Object = MibScalar
wtWebGraphAnalog57661HorizontalZoom = _WtWebGraphAnalog57661HorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 4, 8),
    _WtWebGraphAnalog57661HorizontalZoom_Type()
)
wtWebGraphAnalog57661HorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661HorizontalZoom.setStatus("mandatory")
_WtWebGraphAnalog57661Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Alarm = _WtWebGraphAnalog57661Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5)
)


class _WtWebGraphAnalog57661AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57661AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57661AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661AlarmCount_Object = MibScalar
wtWebGraphAnalog57661AlarmCount = _WtWebGraphAnalog57661AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 1),
    _WtWebGraphAnalog57661AlarmCount_Type()
)
wtWebGraphAnalog57661AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmCount.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmIfTable_Object = MibTable
wtWebGraphAnalog57661AlarmIfTable = _WtWebGraphAnalog57661AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalog57661AlarmIfEntry = _WtWebGraphAnalog57661AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 2, 1)
)
wtWebGraphAnalog57661AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57661AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57661AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661AlarmNo_Object = MibTableColumn
wtWebGraphAnalog57661AlarmNo = _WtWebGraphAnalog57661AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalog57661AlarmNo_Type()
)
wtWebGraphAnalog57661AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmNo.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmTable_Object = MibTable
wtWebGraphAnalog57661AlarmTable = _WtWebGraphAnalog57661AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTable.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmEntry_Object = MibTableRow
wtWebGraphAnalog57661AlarmEntry = _WtWebGraphAnalog57661AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1)
)
wtWebGraphAnalog57661AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57661AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTrigger = _WtWebGraphAnalog57661AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalog57661AlarmTrigger_Type()
)
wtWebGraphAnalog57661AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMin1_Type = OctetString
_WtWebGraphAnalog57661AlarmMin1_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMin1 = _WtWebGraphAnalog57661AlarmMin1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalog57661AlarmMin1_Type()
)
wtWebGraphAnalog57661AlarmMin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMin1.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMax1_Type = OctetString
_WtWebGraphAnalog57661AlarmMax1_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMax1 = _WtWebGraphAnalog57661AlarmMax1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalog57661AlarmMax1_Type()
)
wtWebGraphAnalog57661AlarmMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMax1.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmHysteresis1_Type = OctetString
_WtWebGraphAnalog57661AlarmHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57661AlarmHysteresis1 = _WtWebGraphAnalog57661AlarmHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalog57661AlarmHysteresis1_Type()
)
wtWebGraphAnalog57661AlarmHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmDelay_Type = OctetString
_WtWebGraphAnalog57661AlarmDelay_Object = MibTableColumn
wtWebGraphAnalog57661AlarmDelay = _WtWebGraphAnalog57661AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalog57661AlarmDelay_Type()
)
wtWebGraphAnalog57661AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmInterval_Type = OctetString
_WtWebGraphAnalog57661AlarmInterval_Object = MibTableColumn
wtWebGraphAnalog57661AlarmInterval = _WtWebGraphAnalog57661AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalog57661AlarmInterval_Type()
)
wtWebGraphAnalog57661AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661AlarmEnable_Object = MibTableColumn
wtWebGraphAnalog57661AlarmEnable = _WtWebGraphAnalog57661AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalog57661AlarmEnable_Type()
)
wtWebGraphAnalog57661AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalog57661AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalog57661AlarmEMailAddr = _WtWebGraphAnalog57661AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalog57661AlarmEMailAddr_Type()
)
wtWebGraphAnalog57661AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMailSubject_Type = OctetString
_WtWebGraphAnalog57661AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMailSubject = _WtWebGraphAnalog57661AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalog57661AlarmMailSubject_Type()
)
wtWebGraphAnalog57661AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMailText_Type = OctetString
_WtWebGraphAnalog57661AlarmMailText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMailText = _WtWebGraphAnalog57661AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalog57661AlarmMailText_Type()
)
wtWebGraphAnalog57661AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmManagerIP_Type = OctetString
_WtWebGraphAnalog57661AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalog57661AlarmManagerIP = _WtWebGraphAnalog57661AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalog57661AlarmManagerIP_Type()
)
wtWebGraphAnalog57661AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmTrapText_Type = OctetString
_WtWebGraphAnalog57661AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTrapText = _WtWebGraphAnalog57661AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalog57661AlarmTrapText_Type()
)
wtWebGraphAnalog57661AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalog57661AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMailOptions = _WtWebGraphAnalog57661AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalog57661AlarmMailOptions_Type()
)
wtWebGraphAnalog57661AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalog57661AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTcpIpAddr = _WtWebGraphAnalog57661AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalog57661AlarmTcpIpAddr_Type()
)
wtWebGraphAnalog57661AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTcpPort = _WtWebGraphAnalog57661AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalog57661AlarmTcpPort_Type()
)
wtWebGraphAnalog57661AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmTcpText_Type = OctetString
_WtWebGraphAnalog57661AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTcpText = _WtWebGraphAnalog57661AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalog57661AlarmTcpText_Type()
)
wtWebGraphAnalog57661AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalog57661AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalog57661AlarmClearMailSubject = _WtWebGraphAnalog57661AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalog57661AlarmClearMailSubject_Type()
)
wtWebGraphAnalog57661AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmClearMailText_Type = OctetString
_WtWebGraphAnalog57661AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmClearMailText = _WtWebGraphAnalog57661AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalog57661AlarmClearMailText_Type()
)
wtWebGraphAnalog57661AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalog57661AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmClearTrapText = _WtWebGraphAnalog57661AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalog57661AlarmClearTrapText_Type()
)
wtWebGraphAnalog57661AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalog57661AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmClearTcpText = _WtWebGraphAnalog57661AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalog57661AlarmClearTcpText_Type()
)
wtWebGraphAnalog57661AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMin2_Type = OctetString
_WtWebGraphAnalog57661AlarmMin2_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMin2 = _WtWebGraphAnalog57661AlarmMin2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalog57661AlarmMin2_Type()
)
wtWebGraphAnalog57661AlarmMin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMin2.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmMax2_Type = OctetString
_WtWebGraphAnalog57661AlarmMax2_Object = MibTableColumn
wtWebGraphAnalog57661AlarmMax2 = _WtWebGraphAnalog57661AlarmMax2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalog57661AlarmMax2_Type()
)
wtWebGraphAnalog57661AlarmMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmMax2.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmHysteresis2_Type = OctetString
_WtWebGraphAnalog57661AlarmHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57661AlarmHysteresis2 = _WtWebGraphAnalog57661AlarmHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalog57661AlarmHysteresis2_Type()
)
wtWebGraphAnalog57661AlarmHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalog57661AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661AlarmSyslogIpAddr = _WtWebGraphAnalog57661AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalog57661AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalog57661AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalog57661AlarmSyslogPort = _WtWebGraphAnalog57661AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalog57661AlarmSyslogPort_Type()
)
wtWebGraphAnalog57661AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmSyslogText_Type = OctetString
_WtWebGraphAnalog57661AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmSyslogText = _WtWebGraphAnalog57661AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalog57661AlarmSyslogText_Type()
)
wtWebGraphAnalog57661AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalog57661AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmSyslogClearText = _WtWebGraphAnalog57661AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalog57661AlarmSyslogClearText_Type()
)
wtWebGraphAnalog57661AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalog57661AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalog57661AlarmFtpDataPort = _WtWebGraphAnalog57661AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalog57661AlarmFtpDataPort_Type()
)
wtWebGraphAnalog57661AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalog57661AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalog57661AlarmFtpFileName = _WtWebGraphAnalog57661AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalog57661AlarmFtpFileName_Type()
)
wtWebGraphAnalog57661AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmFtpText_Type = OctetString
_WtWebGraphAnalog57661AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmFtpText = _WtWebGraphAnalog57661AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalog57661AlarmFtpText_Type()
)
wtWebGraphAnalog57661AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalog57661AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalog57661AlarmFtpClearText = _WtWebGraphAnalog57661AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalog57661AlarmFtpClearText_Type()
)
wtWebGraphAnalog57661AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalog57661AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalog57661AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalog57661AlarmFtpOption = _WtWebGraphAnalog57661AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalog57661AlarmFtpOption_Type()
)
wtWebGraphAnalog57661AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalog57661AlarmTimerCron_Type = OctetString
_WtWebGraphAnalog57661AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalog57661AlarmTimerCron = _WtWebGraphAnalog57661AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalog57661AlarmTimerCron_Type()
)
wtWebGraphAnalog57661AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalog57661Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Graphics = _WtWebGraphAnalog57661Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6)
)
_WtWebGraphAnalog57661GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661GraphicsBase = _WtWebGraphAnalog57661GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1)
)
_WtWebGraphAnalog57661GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalog57661GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalog57661GraphicsBaseEnable = _WtWebGraphAnalog57661GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 1),
    _WtWebGraphAnalog57661GraphicsBaseEnable_Type()
)
wtWebGraphAnalog57661GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalog57661GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalog57661GraphicsBaseWidth = _WtWebGraphAnalog57661GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 2),
    _WtWebGraphAnalog57661GraphicsBaseWidth_Type()
)
wtWebGraphAnalog57661GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalog57661GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalog57661GraphicsBaseHeight = _WtWebGraphAnalog57661GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 3),
    _WtWebGraphAnalog57661GraphicsBaseHeight_Type()
)
wtWebGraphAnalog57661GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalog57661GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57661GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57661GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalog57661GraphicsBaseFrameColor = _WtWebGraphAnalog57661GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 4),
    _WtWebGraphAnalog57661GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalog57661GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalog57661GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57661GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57661GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalog57661GraphicsBaseBackgroundColor = _WtWebGraphAnalog57661GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 5),
    _WtWebGraphAnalog57661GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalog57661GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalog57661GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalog57661GraphicsBasePollingrate = _WtWebGraphAnalog57661GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 1, 6),
    _WtWebGraphAnalog57661GraphicsBasePollingrate_Type()
)
wtWebGraphAnalog57661GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661GraphicsSelect = _WtWebGraphAnalog57661GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2)
)


class _WtWebGraphAnalog57661GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel = _WtWebGraphAnalog57661GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 1),
    _WtWebGraphAnalog57661GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 2),
    _WtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalog57661SensorColor2Table_Object = MibTable
wtWebGraphAnalog57661SensorColor2Table = _WtWebGraphAnalog57661SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalog57661SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalog57661SensorColor2Entry = _WtWebGraphAnalog57661SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalog57661SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalog57661GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57661GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57661GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalog57661GraphicsSensorColor = _WtWebGraphAnalog57661GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalog57661GraphicsSensorColor_Type()
)
wtWebGraphAnalog57661GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalog57661GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalog57661GraphicsSelectScale = _WtWebGraphAnalog57661GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalog57661GraphicsSelectScale_Type()
)
wtWebGraphAnalog57661GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661GraphicsScale = _WtWebGraphAnalog57661GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3)
)
_WtWebGraphAnalog57661GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalog57661GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalog57661GraphicsScaleAutoScaleEnable = _WtWebGraphAnalog57661GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 1),
    _WtWebGraphAnalog57661GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalog57661GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalog57661GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalog57661GraphicsScaleAutoFitEnable = _WtWebGraphAnalog57661GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 2),
    _WtWebGraphAnalog57661GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalog57661GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalog57661GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale1Min = _WtWebGraphAnalog57661GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 3),
    _WtWebGraphAnalog57661GraphicsScale1Min_Type()
)
wtWebGraphAnalog57661GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalog57661GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale2Min = _WtWebGraphAnalog57661GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 4),
    _WtWebGraphAnalog57661GraphicsScale2Min_Type()
)
wtWebGraphAnalog57661GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalog57661GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale1Max = _WtWebGraphAnalog57661GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 7),
    _WtWebGraphAnalog57661GraphicsScale1Max_Type()
)
wtWebGraphAnalog57661GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalog57661GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale2Max = _WtWebGraphAnalog57661GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 8),
    _WtWebGraphAnalog57661GraphicsScale2Max_Type()
)
wtWebGraphAnalog57661GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalog57661GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale1Unit = _WtWebGraphAnalog57661GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 11),
    _WtWebGraphAnalog57661GraphicsScale1Unit_Type()
)
wtWebGraphAnalog57661GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalog57661GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalog57661GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalog57661GraphicsScale2Unit = _WtWebGraphAnalog57661GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 6, 3, 12),
    _WtWebGraphAnalog57661GraphicsScale2Unit_Type()
)
wtWebGraphAnalog57661GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalog57661Report_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Report = _WtWebGraphAnalog57661Report_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7)
)


class _WtWebGraphAnalog57661ReportCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57661ReportCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ReportCount_Object = MibScalar
wtWebGraphAnalog57661ReportCount = _WtWebGraphAnalog57661ReportCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 1),
    _WtWebGraphAnalog57661ReportCount_Type()
)
wtWebGraphAnalog57661ReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportCount.setStatus("mandatory")
_WtWebGraphAnalog57661ReportIfTable_Object = MibTable
wtWebGraphAnalog57661ReportIfTable = _WtWebGraphAnalog57661ReportIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportIfTable.setStatus("mandatory")
_WtWebGraphAnalog57661ReportIfEntry_Object = MibTableRow
wtWebGraphAnalog57661ReportIfEntry = _WtWebGraphAnalog57661ReportIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 2, 1)
)
wtWebGraphAnalog57661ReportIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661ReportNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportIfEntry.setStatus("mandatory")
_WtWebGraphAnalog57661ReportNo_Type = Integer32
_WtWebGraphAnalog57661ReportNo_Object = MibTableColumn
wtWebGraphAnalog57661ReportNo = _WtWebGraphAnalog57661ReportNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 2, 1, 1),
    _WtWebGraphAnalog57661ReportNo_Type()
)
wtWebGraphAnalog57661ReportNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportNo.setStatus("mandatory")
_WtWebGraphAnalog57661ReportTable_Object = MibTable
wtWebGraphAnalog57661ReportTable = _WtWebGraphAnalog57661ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTable.setStatus("mandatory")
_WtWebGraphAnalog57661ReportEntry_Object = MibTableRow
wtWebGraphAnalog57661ReportEntry = _WtWebGraphAnalog57661ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1)
)
wtWebGraphAnalog57661ReportEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661ReportNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportEntry.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661ReportEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661ReportEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661ReportEnable_Object = MibTableColumn
wtWebGraphAnalog57661ReportEnable = _WtWebGraphAnalog57661ReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 1),
    _WtWebGraphAnalog57661ReportEnable_Type()
)
wtWebGraphAnalog57661ReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportEnable.setStatus("mandatory")
_WtWebGraphAnalog57661ReportTimerCron_Type = OctetString
_WtWebGraphAnalog57661ReportTimerCron_Object = MibTableColumn
wtWebGraphAnalog57661ReportTimerCron = _WtWebGraphAnalog57661ReportTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 2),
    _WtWebGraphAnalog57661ReportTimerCron_Type()
)
wtWebGraphAnalog57661ReportTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTimerCron.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportMethodeEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57661ReportMethodeEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661ReportMethodeEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661ReportMethodeEnable_Object = MibTableColumn
wtWebGraphAnalog57661ReportMethodeEnable = _WtWebGraphAnalog57661ReportMethodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 3),
    _WtWebGraphAnalog57661ReportMethodeEnable_Type()
)
wtWebGraphAnalog57661ReportMethodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportMethodeEnable.setStatus("mandatory")
_WtWebGraphAnalog57661ReportEMailAddr_Type = OctetString
_WtWebGraphAnalog57661ReportEMailAddr_Object = MibTableColumn
wtWebGraphAnalog57661ReportEMailAddr = _WtWebGraphAnalog57661ReportEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 8),
    _WtWebGraphAnalog57661ReportEMailAddr_Type()
)
wtWebGraphAnalog57661ReportEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportEMailAddr.setStatus("mandatory")
_WtWebGraphAnalog57661ReportMailSubject_Type = OctetString
_WtWebGraphAnalog57661ReportMailSubject_Object = MibTableColumn
wtWebGraphAnalog57661ReportMailSubject = _WtWebGraphAnalog57661ReportMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 9),
    _WtWebGraphAnalog57661ReportMailSubject_Type()
)
wtWebGraphAnalog57661ReportMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57661ReportMailText_Type = OctetString
_WtWebGraphAnalog57661ReportMailText_Object = MibTableColumn
wtWebGraphAnalog57661ReportMailText = _WtWebGraphAnalog57661ReportMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 10),
    _WtWebGraphAnalog57661ReportMailText_Type()
)
wtWebGraphAnalog57661ReportMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportMailText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportManagerIP_Type = OctetString
_WtWebGraphAnalog57661ReportManagerIP_Object = MibTableColumn
wtWebGraphAnalog57661ReportManagerIP = _WtWebGraphAnalog57661ReportManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 11),
    _WtWebGraphAnalog57661ReportManagerIP_Type()
)
wtWebGraphAnalog57661ReportManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportManagerIP.setStatus("mandatory")
_WtWebGraphAnalog57661ReportTrapText_Type = OctetString
_WtWebGraphAnalog57661ReportTrapText_Object = MibTableColumn
wtWebGraphAnalog57661ReportTrapText = _WtWebGraphAnalog57661ReportTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 12),
    _WtWebGraphAnalog57661ReportTrapText_Type()
)
wtWebGraphAnalog57661ReportTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTrapText.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalog57661ReportMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661ReportMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661ReportMailOptions_Object = MibTableColumn
wtWebGraphAnalog57661ReportMailOptions = _WtWebGraphAnalog57661ReportMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 13),
    _WtWebGraphAnalog57661ReportMailOptions_Type()
)
wtWebGraphAnalog57661ReportMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportMailOptions.setStatus("mandatory")
_WtWebGraphAnalog57661ReportTcpIpAddr_Type = OctetString
_WtWebGraphAnalog57661ReportTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661ReportTcpIpAddr = _WtWebGraphAnalog57661ReportTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 14),
    _WtWebGraphAnalog57661ReportTcpIpAddr_Type()
)
wtWebGraphAnalog57661ReportTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ReportTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661ReportTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ReportTcpPort_Object = MibTableColumn
wtWebGraphAnalog57661ReportTcpPort = _WtWebGraphAnalog57661ReportTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 15),
    _WtWebGraphAnalog57661ReportTcpPort_Type()
)
wtWebGraphAnalog57661ReportTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTcpPort.setStatus("mandatory")
_WtWebGraphAnalog57661ReportTcpText_Type = OctetString
_WtWebGraphAnalog57661ReportTcpText_Object = MibTableColumn
wtWebGraphAnalog57661ReportTcpText = _WtWebGraphAnalog57661ReportTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 16),
    _WtWebGraphAnalog57661ReportTcpText_Type()
)
wtWebGraphAnalog57661ReportTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportTcpText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportClearMailSubject_Type = OctetString
_WtWebGraphAnalog57661ReportClearMailSubject_Object = MibTableColumn
wtWebGraphAnalog57661ReportClearMailSubject = _WtWebGraphAnalog57661ReportClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 17),
    _WtWebGraphAnalog57661ReportClearMailSubject_Type()
)
wtWebGraphAnalog57661ReportClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57661ReportClearMailText_Type = OctetString
_WtWebGraphAnalog57661ReportClearMailText_Object = MibTableColumn
wtWebGraphAnalog57661ReportClearMailText = _WtWebGraphAnalog57661ReportClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 18),
    _WtWebGraphAnalog57661ReportClearMailText_Type()
)
wtWebGraphAnalog57661ReportClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportClearMailText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportClearTrapText_Type = OctetString
_WtWebGraphAnalog57661ReportClearTrapText_Object = MibTableColumn
wtWebGraphAnalog57661ReportClearTrapText = _WtWebGraphAnalog57661ReportClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 19),
    _WtWebGraphAnalog57661ReportClearTrapText_Type()
)
wtWebGraphAnalog57661ReportClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportClearTrapText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportClearTcpText_Type = OctetString
_WtWebGraphAnalog57661ReportClearTcpText_Object = MibTableColumn
wtWebGraphAnalog57661ReportClearTcpText = _WtWebGraphAnalog57661ReportClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 20),
    _WtWebGraphAnalog57661ReportClearTcpText_Type()
)
wtWebGraphAnalog57661ReportClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportClearTcpText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportSyslogIpAddr_Type = OctetString
_WtWebGraphAnalog57661ReportSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalog57661ReportSyslogIpAddr = _WtWebGraphAnalog57661ReportSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 24),
    _WtWebGraphAnalog57661ReportSyslogIpAddr_Type()
)
wtWebGraphAnalog57661ReportSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57661ReportSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57661ReportSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57661ReportSyslogPort_Object = MibTableColumn
wtWebGraphAnalog57661ReportSyslogPort = _WtWebGraphAnalog57661ReportSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 25),
    _WtWebGraphAnalog57661ReportSyslogPort_Type()
)
wtWebGraphAnalog57661ReportSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportSyslogPort.setStatus("mandatory")
_WtWebGraphAnalog57661ReportSyslogText_Type = OctetString
_WtWebGraphAnalog57661ReportSyslogText_Object = MibTableColumn
wtWebGraphAnalog57661ReportSyslogText = _WtWebGraphAnalog57661ReportSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 26),
    _WtWebGraphAnalog57661ReportSyslogText_Type()
)
wtWebGraphAnalog57661ReportSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportSyslogText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportSyslogClearText_Type = OctetString
_WtWebGraphAnalog57661ReportSyslogClearText_Object = MibTableColumn
wtWebGraphAnalog57661ReportSyslogClearText = _WtWebGraphAnalog57661ReportSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 27),
    _WtWebGraphAnalog57661ReportSyslogClearText_Type()
)
wtWebGraphAnalog57661ReportSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportFtpDataPort_Type = OctetString
_WtWebGraphAnalog57661ReportFtpDataPort_Object = MibTableColumn
wtWebGraphAnalog57661ReportFtpDataPort = _WtWebGraphAnalog57661ReportFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 28),
    _WtWebGraphAnalog57661ReportFtpDataPort_Type()
)
wtWebGraphAnalog57661ReportFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalog57661ReportFtpFileName_Type = OctetString
_WtWebGraphAnalog57661ReportFtpFileName_Object = MibTableColumn
wtWebGraphAnalog57661ReportFtpFileName = _WtWebGraphAnalog57661ReportFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 29),
    _WtWebGraphAnalog57661ReportFtpFileName_Type()
)
wtWebGraphAnalog57661ReportFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportFtpFileName.setStatus("mandatory")
_WtWebGraphAnalog57661ReportFtpText_Type = OctetString
_WtWebGraphAnalog57661ReportFtpText_Object = MibTableColumn
wtWebGraphAnalog57661ReportFtpText = _WtWebGraphAnalog57661ReportFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 30),
    _WtWebGraphAnalog57661ReportFtpText_Type()
)
wtWebGraphAnalog57661ReportFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportFtpText.setStatus("mandatory")
_WtWebGraphAnalog57661ReportFtpClearText_Type = OctetString
_WtWebGraphAnalog57661ReportFtpClearText_Object = MibTableColumn
wtWebGraphAnalog57661ReportFtpClearText = _WtWebGraphAnalog57661ReportFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 31),
    _WtWebGraphAnalog57661ReportFtpClearText_Type()
)
wtWebGraphAnalog57661ReportFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalog57661ReportFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalog57661ReportFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661ReportFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661ReportFtpOption_Object = MibTableColumn
wtWebGraphAnalog57661ReportFtpOption = _WtWebGraphAnalog57661ReportFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 1, 7, 3, 1, 32),
    _WtWebGraphAnalog57661ReportFtpOption_Type()
)
wtWebGraphAnalog57661ReportFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661ReportFtpOption.setStatus("mandatory")
_WtWebGraphAnalog57661Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Ports = _WtWebGraphAnalog57661Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2)
)
_WtWebGraphAnalog57661PortTable_Object = MibTable
wtWebGraphAnalog57661PortTable = _WtWebGraphAnalog57661PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortTable.setStatus("mandatory")
_WtWebGraphAnalog57661PortEntry_Object = MibTableRow
wtWebGraphAnalog57661PortEntry = _WtWebGraphAnalog57661PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1)
)
wtWebGraphAnalog57661PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortEntry.setStatus("mandatory")
_WtWebGraphAnalog57661PortName_Type = OctetString
_WtWebGraphAnalog57661PortName_Object = MibTableColumn
wtWebGraphAnalog57661PortName = _WtWebGraphAnalog57661PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 1),
    _WtWebGraphAnalog57661PortName_Type()
)
wtWebGraphAnalog57661PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortName.setStatus("mandatory")
_WtWebGraphAnalog57661PortText_Type = OctetString
_WtWebGraphAnalog57661PortText_Object = MibTableColumn
wtWebGraphAnalog57661PortText = _WtWebGraphAnalog57661PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 2),
    _WtWebGraphAnalog57661PortText_Type()
)
wtWebGraphAnalog57661PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortText.setStatus("mandatory")
_WtWebGraphAnalog57661PortOffset1_Type = OctetString
_WtWebGraphAnalog57661PortOffset1_Object = MibTableColumn
wtWebGraphAnalog57661PortOffset1 = _WtWebGraphAnalog57661PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 3),
    _WtWebGraphAnalog57661PortOffset1_Type()
)
wtWebGraphAnalog57661PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortOffset1.setStatus("mandatory")
_WtWebGraphAnalog57661SetPoint1_Type = OctetString
_WtWebGraphAnalog57661SetPoint1_Object = MibTableColumn
wtWebGraphAnalog57661SetPoint1 = _WtWebGraphAnalog57661SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 4),
    _WtWebGraphAnalog57661SetPoint1_Type()
)
wtWebGraphAnalog57661SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SetPoint1.setStatus("mandatory")
_WtWebGraphAnalog57661PortOffset2_Type = OctetString
_WtWebGraphAnalog57661PortOffset2_Object = MibTableColumn
wtWebGraphAnalog57661PortOffset2 = _WtWebGraphAnalog57661PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 5),
    _WtWebGraphAnalog57661PortOffset2_Type()
)
wtWebGraphAnalog57661PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortOffset2.setStatus("mandatory")
_WtWebGraphAnalog57661SetPoint2_Type = OctetString
_WtWebGraphAnalog57661SetPoint2_Object = MibTableColumn
wtWebGraphAnalog57661SetPoint2 = _WtWebGraphAnalog57661SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 6),
    _WtWebGraphAnalog57661SetPoint2_Type()
)
wtWebGraphAnalog57661SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661SetPoint2.setStatus("mandatory")
_WtWebGraphAnalog57661PortComment_Type = OctetString
_WtWebGraphAnalog57661PortComment_Object = MibTableColumn
wtWebGraphAnalog57661PortComment = _WtWebGraphAnalog57661PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 7),
    _WtWebGraphAnalog57661PortComment_Type()
)
wtWebGraphAnalog57661PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortComment.setStatus("mandatory")


class _WtWebGraphAnalog57661PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalog57661PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalog57661PortSensorSelect = _WtWebGraphAnalog57661PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 8),
    _WtWebGraphAnalog57661PortSensorSelect_Type()
)
wtWebGraphAnalog57661PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalog57661PortUnit_Type = OctetString
_WtWebGraphAnalog57661PortUnit_Object = MibTableColumn
wtWebGraphAnalog57661PortUnit = _WtWebGraphAnalog57661PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 9),
    _WtWebGraphAnalog57661PortUnit_Type()
)
wtWebGraphAnalog57661PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortUnit.setStatus("mandatory")
_WtWebGraphAnalog57661PortScale0_Type = OctetString
_WtWebGraphAnalog57661PortScale0_Object = MibTableColumn
wtWebGraphAnalog57661PortScale0 = _WtWebGraphAnalog57661PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 10),
    _WtWebGraphAnalog57661PortScale0_Type()
)
wtWebGraphAnalog57661PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortScale0.setStatus("mandatory")
_WtWebGraphAnalog57661PortScale100_Type = OctetString
_WtWebGraphAnalog57661PortScale100_Object = MibTableColumn
wtWebGraphAnalog57661PortScale100 = _WtWebGraphAnalog57661PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 11),
    _WtWebGraphAnalog57661PortScale100_Type()
)
wtWebGraphAnalog57661PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortScale100.setStatus("mandatory")


class _WtWebGraphAnalog57661PortOutputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661PortOutputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661PortOutputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661PortOutputMode_Object = MibTableColumn
wtWebGraphAnalog57661PortOutputMode = _WtWebGraphAnalog57661PortOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 12),
    _WtWebGraphAnalog57661PortOutputMode_Type()
)
wtWebGraphAnalog57661PortOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortOutputMode.setStatus("mandatory")


class _WtWebGraphAnalog57661PortInputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57661PortInputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57661PortInputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57661PortInputMode_Object = MibTableColumn
wtWebGraphAnalog57661PortInputMode = _WtWebGraphAnalog57661PortInputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 2, 1, 1, 13),
    _WtWebGraphAnalog57661PortInputMode_Type()
)
wtWebGraphAnalog57661PortInputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661PortInputMode.setStatus("mandatory")
_WtWebGraphAnalog57661Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Manufact = _WtWebGraphAnalog57661Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3)
)
_WtWebGraphAnalog57661MfName_Type = OctetString
_WtWebGraphAnalog57661MfName_Object = MibScalar
wtWebGraphAnalog57661MfName = _WtWebGraphAnalog57661MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 1),
    _WtWebGraphAnalog57661MfName_Type()
)
wtWebGraphAnalog57661MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfName.setStatus("mandatory")
_WtWebGraphAnalog57661MfAddr_Type = OctetString
_WtWebGraphAnalog57661MfAddr_Object = MibScalar
wtWebGraphAnalog57661MfAddr = _WtWebGraphAnalog57661MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 2),
    _WtWebGraphAnalog57661MfAddr_Type()
)
wtWebGraphAnalog57661MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfAddr.setStatus("mandatory")
_WtWebGraphAnalog57661MfHotline_Type = OctetString
_WtWebGraphAnalog57661MfHotline_Object = MibScalar
wtWebGraphAnalog57661MfHotline = _WtWebGraphAnalog57661MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 3),
    _WtWebGraphAnalog57661MfHotline_Type()
)
wtWebGraphAnalog57661MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfHotline.setStatus("mandatory")
_WtWebGraphAnalog57661MfInternet_Type = OctetString
_WtWebGraphAnalog57661MfInternet_Object = MibScalar
wtWebGraphAnalog57661MfInternet = _WtWebGraphAnalog57661MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 4),
    _WtWebGraphAnalog57661MfInternet_Type()
)
wtWebGraphAnalog57661MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfInternet.setStatus("mandatory")
_WtWebGraphAnalog57661MfDeviceTyp_Type = OctetString
_WtWebGraphAnalog57661MfDeviceTyp_Object = MibScalar
wtWebGraphAnalog57661MfDeviceTyp = _WtWebGraphAnalog57661MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 5),
    _WtWebGraphAnalog57661MfDeviceTyp_Type()
)
wtWebGraphAnalog57661MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalog57661MfOrderNo_Type = OctetString
_WtWebGraphAnalog57661MfOrderNo_Object = MibScalar
wtWebGraphAnalog57661MfOrderNo = _WtWebGraphAnalog57661MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 3, 3, 6),
    _WtWebGraphAnalog57661MfOrderNo_Type()
)
wtWebGraphAnalog57661MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalog57661Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57661Diag = _WtWebGraphAnalog57661Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4)
)
_WtWebGraphAnalog57661DiagErrorCount_Type = Integer32
_WtWebGraphAnalog57661DiagErrorCount_Object = MibScalar
wtWebGraphAnalog57661DiagErrorCount = _WtWebGraphAnalog57661DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4, 1),
    _WtWebGraphAnalog57661DiagErrorCount_Type()
)
wtWebGraphAnalog57661DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalog57661DiagBinaryError_Type = OctetString
_WtWebGraphAnalog57661DiagBinaryError_Object = MibScalar
wtWebGraphAnalog57661DiagBinaryError = _WtWebGraphAnalog57661DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4, 2),
    _WtWebGraphAnalog57661DiagBinaryError_Type()
)
wtWebGraphAnalog57661DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalog57661DiagErrorIndex_Type = Integer32
_WtWebGraphAnalog57661DiagErrorIndex_Object = MibScalar
wtWebGraphAnalog57661DiagErrorIndex = _WtWebGraphAnalog57661DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4, 3),
    _WtWebGraphAnalog57661DiagErrorIndex_Type()
)
wtWebGraphAnalog57661DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalog57661DiagErrorMessage_Type = OctetString
_WtWebGraphAnalog57661DiagErrorMessage_Object = MibScalar
wtWebGraphAnalog57661DiagErrorMessage = _WtWebGraphAnalog57661DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4, 4),
    _WtWebGraphAnalog57661DiagErrorMessage_Type()
)
wtWebGraphAnalog57661DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalog57661DiagErrorClear_Type = Integer32
_WtWebGraphAnalog57661DiagErrorClear_Object = MibScalar
wtWebGraphAnalog57661DiagErrorClear = _WtWebGraphAnalog57661DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 4, 5),
    _WtWebGraphAnalog57661DiagErrorClear_Type()
)
wtWebGraphAnalog57661DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalog57661Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 31)
)
wtWebGraphAnalog57661Alert1.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert1.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 32)
)
wtWebGraphAnalog57661Alert2.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert2.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 33)
)
wtWebGraphAnalog57661Alert3.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert3.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 34)
)
wtWebGraphAnalog57661Alert4.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert4.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 35)
)
wtWebGraphAnalog57661Alert5.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert5.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 36)
)
wtWebGraphAnalog57661Alert6.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert6.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 37)
)
wtWebGraphAnalog57661Alert7.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert7.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 38)
)
wtWebGraphAnalog57661Alert8.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert8.setStatus(
        ""
    )

wtWebGraphAnalog57661AlertReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 39)
)
wtWebGraphAnalog57661AlertReport.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlertReport.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 91)
)
wtWebGraphAnalog57661Alert9.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert9.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 92)
)
wtWebGraphAnalog57661Alert10.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert10.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 93)
)
wtWebGraphAnalog57661Alert11.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert11.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 94)
)
wtWebGraphAnalog57661Alert12.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert12.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 95)
)
wtWebGraphAnalog57661Alert13.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert13.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 96)
)
wtWebGraphAnalog57661Alert14.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert14.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 97)
)
wtWebGraphAnalog57661Alert15.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert15.setStatus(
        ""
    )

wtWebGraphAnalog57661Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 98)
)
wtWebGraphAnalog57661Alert16.setObjects(
    ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661Alert16.setStatus(
        ""
    )

wtWebGraphAnalog57661AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 28, 0, 110)
)
wtWebGraphAnalog57661AlertDiag.setObjects(
      *(("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661DiagErrorIndex"),
        ("WebGraph-AnalogIO-57661-US-MIB", "wtWebGraphAnalog57661DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57661AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIO-57661-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalog57661": wtWebGraphAnalog57661,
       "wtWebGraphAnalog57661Alert1": wtWebGraphAnalog57661Alert1,
       "wtWebGraphAnalog57661Alert2": wtWebGraphAnalog57661Alert2,
       "wtWebGraphAnalog57661Alert3": wtWebGraphAnalog57661Alert3,
       "wtWebGraphAnalog57661Alert4": wtWebGraphAnalog57661Alert4,
       "wtWebGraphAnalog57661Alert5": wtWebGraphAnalog57661Alert5,
       "wtWebGraphAnalog57661Alert6": wtWebGraphAnalog57661Alert6,
       "wtWebGraphAnalog57661Alert7": wtWebGraphAnalog57661Alert7,
       "wtWebGraphAnalog57661Alert8": wtWebGraphAnalog57661Alert8,
       "wtWebGraphAnalog57661AlertReport": wtWebGraphAnalog57661AlertReport,
       "wtWebGraphAnalog57661Alert9": wtWebGraphAnalog57661Alert9,
       "wtWebGraphAnalog57661Alert10": wtWebGraphAnalog57661Alert10,
       "wtWebGraphAnalog57661Alert11": wtWebGraphAnalog57661Alert11,
       "wtWebGraphAnalog57661Alert12": wtWebGraphAnalog57661Alert12,
       "wtWebGraphAnalog57661Alert13": wtWebGraphAnalog57661Alert13,
       "wtWebGraphAnalog57661Alert14": wtWebGraphAnalog57661Alert14,
       "wtWebGraphAnalog57661Alert15": wtWebGraphAnalog57661Alert15,
       "wtWebGraphAnalog57661Alert16": wtWebGraphAnalog57661Alert16,
       "wtWebGraphAnalog57661AlertDiag": wtWebGraphAnalog57661AlertDiag,
       "wtWebGraphAnalog57661Inventory": wtWebGraphAnalog57661Inventory,
       "wtWebGraphAnalog57661Sensors": wtWebGraphAnalog57661Sensors,
       "wtWebGraphAnalog57661SensorTable": wtWebGraphAnalog57661SensorTable,
       "wtWebGraphAnalog57661SensorEntry": wtWebGraphAnalog57661SensorEntry,
       "wtWebGraphAnalog57661SensorNo": wtWebGraphAnalog57661SensorNo,
       "wtWebGraphAnalog57661ValuesTable": wtWebGraphAnalog57661ValuesTable,
       "wtWebGraphAnalog57661ValuesEntry": wtWebGraphAnalog57661ValuesEntry,
       "wtWebGraphAnalog57661Values": wtWebGraphAnalog57661Values,
       "wtWebGraphAnalog57661BinaryValuesTable": wtWebGraphAnalog57661BinaryValuesTable,
       "wtWebGraphAnalog57661BinaryValuesEntry": wtWebGraphAnalog57661BinaryValuesEntry,
       "wtWebGraphAnalog57661BinaryValues": wtWebGraphAnalog57661BinaryValues,
       "wtWebGraphAnalog57661SessCntrl": wtWebGraphAnalog57661SessCntrl,
       "wtWebGraphAnalog57661SessCntrlPassword": wtWebGraphAnalog57661SessCntrlPassword,
       "wtWebGraphAnalog57661SessCntrlConfigMode": wtWebGraphAnalog57661SessCntrlConfigMode,
       "wtWebGraphAnalog57661SessCntrlLogout": wtWebGraphAnalog57661SessCntrlLogout,
       "wtWebGraphAnalog57661SessCntrlAdminPassword": wtWebGraphAnalog57661SessCntrlAdminPassword,
       "wtWebGraphAnalog57661SessCntrlConfigPassword": wtWebGraphAnalog57661SessCntrlConfigPassword,
       "wtWebGraphAnalog57661Config": wtWebGraphAnalog57661Config,
       "wtWebGraphAnalog57661Device": wtWebGraphAnalog57661Device,
       "wtWebGraphAnalog57661Text": wtWebGraphAnalog57661Text,
       "wtWebGraphAnalog57661DeviceName": wtWebGraphAnalog57661DeviceName,
       "wtWebGraphAnalog57661DeviceText": wtWebGraphAnalog57661DeviceText,
       "wtWebGraphAnalog57661DeviceLocation": wtWebGraphAnalog57661DeviceLocation,
       "wtWebGraphAnalog57661DeviceContact": wtWebGraphAnalog57661DeviceContact,
       "wtWebGraphAnalog57661TimeDate": wtWebGraphAnalog57661TimeDate,
       "wtWebGraphAnalog57661TimeZone": wtWebGraphAnalog57661TimeZone,
       "wtWebGraphAnalog57661TzOffsetHrs": wtWebGraphAnalog57661TzOffsetHrs,
       "wtWebGraphAnalog57661TzOffsetMin": wtWebGraphAnalog57661TzOffsetMin,
       "wtWebGraphAnalog57661TzEnable": wtWebGraphAnalog57661TzEnable,
       "wtWebGraphAnalog57661StTzOffsetHrs": wtWebGraphAnalog57661StTzOffsetHrs,
       "wtWebGraphAnalog57661StTzOffsetMin": wtWebGraphAnalog57661StTzOffsetMin,
       "wtWebGraphAnalog57661StTzEnable": wtWebGraphAnalog57661StTzEnable,
       "wtWebGraphAnalog57661StTzStartMonth": wtWebGraphAnalog57661StTzStartMonth,
       "wtWebGraphAnalog57661StTzStartMode": wtWebGraphAnalog57661StTzStartMode,
       "wtWebGraphAnalog57661StTzStartWday": wtWebGraphAnalog57661StTzStartWday,
       "wtWebGraphAnalog57661StTzStartHrs": wtWebGraphAnalog57661StTzStartHrs,
       "wtWebGraphAnalog57661StTzStartMin": wtWebGraphAnalog57661StTzStartMin,
       "wtWebGraphAnalog57661StTzStopMonth": wtWebGraphAnalog57661StTzStopMonth,
       "wtWebGraphAnalog57661StTzStopMode": wtWebGraphAnalog57661StTzStopMode,
       "wtWebGraphAnalog57661StTzStopWday": wtWebGraphAnalog57661StTzStopWday,
       "wtWebGraphAnalog57661StTzStopHrs": wtWebGraphAnalog57661StTzStopHrs,
       "wtWebGraphAnalog57661StTzStopMin": wtWebGraphAnalog57661StTzStopMin,
       "wtWebGraphAnalog57661TimeServer": wtWebGraphAnalog57661TimeServer,
       "wtWebGraphAnalog57661TimeServer1": wtWebGraphAnalog57661TimeServer1,
       "wtWebGraphAnalog57661TimeServer2": wtWebGraphAnalog57661TimeServer2,
       "wtWebGraphAnalog57661TsEnable": wtWebGraphAnalog57661TsEnable,
       "wtWebGraphAnalog57661TsSyncTime": wtWebGraphAnalog57661TsSyncTime,
       "wtWebGraphAnalog57661DeviceClock": wtWebGraphAnalog57661DeviceClock,
       "wtWebGraphAnalog57661ClockHrs": wtWebGraphAnalog57661ClockHrs,
       "wtWebGraphAnalog57661ClockMin": wtWebGraphAnalog57661ClockMin,
       "wtWebGraphAnalog57661ClockDay": wtWebGraphAnalog57661ClockDay,
       "wtWebGraphAnalog57661ClockMonth": wtWebGraphAnalog57661ClockMonth,
       "wtWebGraphAnalog57661ClockYear": wtWebGraphAnalog57661ClockYear,
       "wtWebGraphAnalog57661Basic": wtWebGraphAnalog57661Basic,
       "wtWebGraphAnalog57661Network": wtWebGraphAnalog57661Network,
       "wtWebGraphAnalog57661IpAddress": wtWebGraphAnalog57661IpAddress,
       "wtWebGraphAnalog57661SubnetMask": wtWebGraphAnalog57661SubnetMask,
       "wtWebGraphAnalog57661Gateway": wtWebGraphAnalog57661Gateway,
       "wtWebGraphAnalog57661DnsServer1": wtWebGraphAnalog57661DnsServer1,
       "wtWebGraphAnalog57661DnsServer2": wtWebGraphAnalog57661DnsServer2,
       "wtWebGraphAnalog57661AddConfig": wtWebGraphAnalog57661AddConfig,
       "wtWebGraphAnalog57661HTTP": wtWebGraphAnalog57661HTTP,
       "wtWebGraphAnalog57661Startup": wtWebGraphAnalog57661Startup,
       "wtWebGraphAnalog57661GetHeaderEnable": wtWebGraphAnalog57661GetHeaderEnable,
       "wtWebGraphAnalog57661HttpPort": wtWebGraphAnalog57661HttpPort,
       "wtWebGraphAnalog57661Mail": wtWebGraphAnalog57661Mail,
       "wtWebGraphAnalog57661MailAdName": wtWebGraphAnalog57661MailAdName,
       "wtWebGraphAnalog57661MailReply": wtWebGraphAnalog57661MailReply,
       "wtWebGraphAnalog57661MailServer": wtWebGraphAnalog57661MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalog57661MailAuthentication": wtWebGraphAnalog57661MailAuthentication,
       "wtWebGraphAnalog57661MailAuthUser": wtWebGraphAnalog57661MailAuthUser,
       "wtWebGraphAnalog57661MailAuthPassword": wtWebGraphAnalog57661MailAuthPassword,
       "wtWebGraphAnalog57661MailPop3Server": wtWebGraphAnalog57661MailPop3Server,
       "wtWebGraphAnalog57661SNMP": wtWebGraphAnalog57661SNMP,
       "wtWebGraphAnalog57661SnmpCommunityStringRead": wtWebGraphAnalog57661SnmpCommunityStringRead,
       "wtWebGraphAnalog57661SnmpCommunityStringReadWrite": wtWebGraphAnalog57661SnmpCommunityStringReadWrite,
       "wtWebGraphAnalog57661SystemTrapManagerIP": wtWebGraphAnalog57661SystemTrapManagerIP,
       "wtWebGraphAnalog57661SystemTrapEnable": wtWebGraphAnalog57661SystemTrapEnable,
       "wtWebGraphAnalog57661SnmpEnable": wtWebGraphAnalog57661SnmpEnable,
       "wtWebGraphAnalog57661SnmpCommunityStringTrap": wtWebGraphAnalog57661SnmpCommunityStringTrap,
       "wtWebGraphAnalog57661UDP": wtWebGraphAnalog57661UDP,
       "wtWebGraphAnalog57661UdpPort": wtWebGraphAnalog57661UdpPort,
       "wtWebGraphAnalog57661UdpEnable": wtWebGraphAnalog57661UdpEnable,
       "wtWebGraphAnalog57661Syslog": wtWebGraphAnalog57661Syslog,
       "wtWebGraphAnalog57661SyslogServerIP": wtWebGraphAnalog57661SyslogServerIP,
       "wtWebGraphAnalog57661SyslogServerPort": wtWebGraphAnalog57661SyslogServerPort,
       "wtWebGraphAnalog57661SyslogSystemMessagesEnable": wtWebGraphAnalog57661SyslogSystemMessagesEnable,
       "wtWebGraphAnalog57661SyslogEnable": wtWebGraphAnalog57661SyslogEnable,
       "wtWebGraphAnalog57661FTP": wtWebGraphAnalog57661FTP,
       "wtWebGraphAnalog57661FTPServerIP": wtWebGraphAnalog57661FTPServerIP,
       "wtWebGraphAnalog57661FTPServerControlPort": wtWebGraphAnalog57661FTPServerControlPort,
       "wtWebGraphAnalog57661FTPUserName": wtWebGraphAnalog57661FTPUserName,
       "wtWebGraphAnalog57661FTPPassword": wtWebGraphAnalog57661FTPPassword,
       "wtWebGraphAnalog57661FTPAccount": wtWebGraphAnalog57661FTPAccount,
       "wtWebGraphAnalog57661FTPOption": wtWebGraphAnalog57661FTPOption,
       "wtWebGraphAnalog57661FTPEnable": wtWebGraphAnalog57661FTPEnable,
       "wtWebGraphAnalog57661Language": wtWebGraphAnalog57661Language,
       "wtWebGraphAnalog57661LanguageSelect": wtWebGraphAnalog57661LanguageSelect,
       "wtWebGraphAnalog57661Binary": wtWebGraphAnalog57661Binary,
       "wtWebGraphAnalog57661BinaryModeCount": wtWebGraphAnalog57661BinaryModeCount,
       "wtWebGraphAnalog57661BinaryIfTable": wtWebGraphAnalog57661BinaryIfTable,
       "wtWebGraphAnalog57661BinaryIfEntry": wtWebGraphAnalog57661BinaryIfEntry,
       "wtWebGraphAnalog57661BinaryModeNo": wtWebGraphAnalog57661BinaryModeNo,
       "wtWebGraphAnalog57661BinaryTable": wtWebGraphAnalog57661BinaryTable,
       "wtWebGraphAnalog57661BinaryEntry": wtWebGraphAnalog57661BinaryEntry,
       "wtWebGraphAnalog57661BinaryOperationMode": wtWebGraphAnalog57661BinaryOperationMode,
       "wtWebGraphAnalog57661BinaryTcpServerLocalPort": wtWebGraphAnalog57661BinaryTcpServerLocalPort,
       "wtWebGraphAnalog57661BinaryTcpServerInputTrigger": wtWebGraphAnalog57661BinaryTcpServerInputTrigger,
       "wtWebGraphAnalog57661BinaryTcpServerApplicationMode": wtWebGraphAnalog57661BinaryTcpServerApplicationMode,
       "wtWebGraphAnalog57661BinaryTcpClientLocalPort": wtWebGraphAnalog57661BinaryTcpClientLocalPort,
       "wtWebGraphAnalog57661BinaryTcpClientServerPort": wtWebGraphAnalog57661BinaryTcpClientServerPort,
       "wtWebGraphAnalog57661BinaryTcpClientServerIpAddr": wtWebGraphAnalog57661BinaryTcpClientServerIpAddr,
       "wtWebGraphAnalog57661BinaryTcpClientServerPassword": wtWebGraphAnalog57661BinaryTcpClientServerPassword,
       "wtWebGraphAnalog57661BinaryTcpClientInactivity": wtWebGraphAnalog57661BinaryTcpClientInactivity,
       "wtWebGraphAnalog57661BinaryTcpClientInputTrigger": wtWebGraphAnalog57661BinaryTcpClientInputTrigger,
       "wtWebGraphAnalog57661BinaryTcpClientInterval": wtWebGraphAnalog57661BinaryTcpClientInterval,
       "wtWebGraphAnalog57661BinaryTcpClientApplicationMode": wtWebGraphAnalog57661BinaryTcpClientApplicationMode,
       "wtWebGraphAnalog57661BinaryUdpPeerLocalPort": wtWebGraphAnalog57661BinaryUdpPeerLocalPort,
       "wtWebGraphAnalog57661BinaryUdpPeerRemotePort": wtWebGraphAnalog57661BinaryUdpPeerRemotePort,
       "wtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr": wtWebGraphAnalog57661BinaryUdpPeerRemoteIpAddr,
       "wtWebGraphAnalog57661BinaryUdpPeerInputTrigger": wtWebGraphAnalog57661BinaryUdpPeerInputTrigger,
       "wtWebGraphAnalog57661BinaryUdpPeerInterval": wtWebGraphAnalog57661BinaryUdpPeerInterval,
       "wtWebGraphAnalog57661BinaryUdpPeerApplicationMode": wtWebGraphAnalog57661BinaryUdpPeerApplicationMode,
       "wtWebGraphAnalog57661BinaryConnectedPort": wtWebGraphAnalog57661BinaryConnectedPort,
       "wtWebGraphAnalog57661BinaryConnectedIpAddr": wtWebGraphAnalog57661BinaryConnectedIpAddr,
       "wtWebGraphAnalog57661BinaryTcpServerClientHttpPort": wtWebGraphAnalog57661BinaryTcpServerClientHttpPort,
       "wtWebGraphAnalog57661BinaryTcpClientServerHttpPort": wtWebGraphAnalog57661BinaryTcpClientServerHttpPort,
       "wtWebGraphAnalog57661BinaryTcpServerHysteresis1": wtWebGraphAnalog57661BinaryTcpServerHysteresis1,
       "wtWebGraphAnalog57661BinaryTcpServerHysteresis2": wtWebGraphAnalog57661BinaryTcpServerHysteresis2,
       "wtWebGraphAnalog57661BinaryTcpClientHysteresis1": wtWebGraphAnalog57661BinaryTcpClientHysteresis1,
       "wtWebGraphAnalog57661BinaryTcpClientHysteresis2": wtWebGraphAnalog57661BinaryTcpClientHysteresis2,
       "wtWebGraphAnalog57661BinaryUdpPeerHysteresis1": wtWebGraphAnalog57661BinaryUdpPeerHysteresis1,
       "wtWebGraphAnalog57661BinaryUdpPeerHysteresis2": wtWebGraphAnalog57661BinaryUdpPeerHysteresis2,
       "wtWebGraphAnalog57661Datalogger": wtWebGraphAnalog57661Datalogger,
       "wtWebGraphAnalog57661LoggerTimebase": wtWebGraphAnalog57661LoggerTimebase,
       "wtWebGraphAnalog57661LoggerSensorSel": wtWebGraphAnalog57661LoggerSensorSel,
       "wtWebGraphAnalog57661DisplaySensorSel": wtWebGraphAnalog57661DisplaySensorSel,
       "wtWebGraphAnalog57661SensorColorTable": wtWebGraphAnalog57661SensorColorTable,
       "wtWebGraphAnalog57661SensorColorEntry": wtWebGraphAnalog57661SensorColorEntry,
       "wtWebGraphAnalog57661SensorColor": wtWebGraphAnalog57661SensorColor,
       "wtWebGraphAnalog57661AutoScaleEnable": wtWebGraphAnalog57661AutoScaleEnable,
       "wtWebGraphAnalog57661VerticalUpperLimit": wtWebGraphAnalog57661VerticalUpperLimit,
       "wtWebGraphAnalog57661VerticalLowerLimit": wtWebGraphAnalog57661VerticalLowerLimit,
       "wtWebGraphAnalog57661HorizontalZoom": wtWebGraphAnalog57661HorizontalZoom,
       "wtWebGraphAnalog57661Alarm": wtWebGraphAnalog57661Alarm,
       "wtWebGraphAnalog57661AlarmCount": wtWebGraphAnalog57661AlarmCount,
       "wtWebGraphAnalog57661AlarmIfTable": wtWebGraphAnalog57661AlarmIfTable,
       "wtWebGraphAnalog57661AlarmIfEntry": wtWebGraphAnalog57661AlarmIfEntry,
       "wtWebGraphAnalog57661AlarmNo": wtWebGraphAnalog57661AlarmNo,
       "wtWebGraphAnalog57661AlarmTable": wtWebGraphAnalog57661AlarmTable,
       "wtWebGraphAnalog57661AlarmEntry": wtWebGraphAnalog57661AlarmEntry,
       "wtWebGraphAnalog57661AlarmTrigger": wtWebGraphAnalog57661AlarmTrigger,
       "wtWebGraphAnalog57661AlarmMin1": wtWebGraphAnalog57661AlarmMin1,
       "wtWebGraphAnalog57661AlarmMax1": wtWebGraphAnalog57661AlarmMax1,
       "wtWebGraphAnalog57661AlarmHysteresis1": wtWebGraphAnalog57661AlarmHysteresis1,
       "wtWebGraphAnalog57661AlarmDelay": wtWebGraphAnalog57661AlarmDelay,
       "wtWebGraphAnalog57661AlarmInterval": wtWebGraphAnalog57661AlarmInterval,
       "wtWebGraphAnalog57661AlarmEnable": wtWebGraphAnalog57661AlarmEnable,
       "wtWebGraphAnalog57661AlarmEMailAddr": wtWebGraphAnalog57661AlarmEMailAddr,
       "wtWebGraphAnalog57661AlarmMailSubject": wtWebGraphAnalog57661AlarmMailSubject,
       "wtWebGraphAnalog57661AlarmMailText": wtWebGraphAnalog57661AlarmMailText,
       "wtWebGraphAnalog57661AlarmManagerIP": wtWebGraphAnalog57661AlarmManagerIP,
       "wtWebGraphAnalog57661AlarmTrapText": wtWebGraphAnalog57661AlarmTrapText,
       "wtWebGraphAnalog57661AlarmMailOptions": wtWebGraphAnalog57661AlarmMailOptions,
       "wtWebGraphAnalog57661AlarmTcpIpAddr": wtWebGraphAnalog57661AlarmTcpIpAddr,
       "wtWebGraphAnalog57661AlarmTcpPort": wtWebGraphAnalog57661AlarmTcpPort,
       "wtWebGraphAnalog57661AlarmTcpText": wtWebGraphAnalog57661AlarmTcpText,
       "wtWebGraphAnalog57661AlarmClearMailSubject": wtWebGraphAnalog57661AlarmClearMailSubject,
       "wtWebGraphAnalog57661AlarmClearMailText": wtWebGraphAnalog57661AlarmClearMailText,
       "wtWebGraphAnalog57661AlarmClearTrapText": wtWebGraphAnalog57661AlarmClearTrapText,
       "wtWebGraphAnalog57661AlarmClearTcpText": wtWebGraphAnalog57661AlarmClearTcpText,
       "wtWebGraphAnalog57661AlarmMin2": wtWebGraphAnalog57661AlarmMin2,
       "wtWebGraphAnalog57661AlarmMax2": wtWebGraphAnalog57661AlarmMax2,
       "wtWebGraphAnalog57661AlarmHysteresis2": wtWebGraphAnalog57661AlarmHysteresis2,
       "wtWebGraphAnalog57661AlarmSyslogIpAddr": wtWebGraphAnalog57661AlarmSyslogIpAddr,
       "wtWebGraphAnalog57661AlarmSyslogPort": wtWebGraphAnalog57661AlarmSyslogPort,
       "wtWebGraphAnalog57661AlarmSyslogText": wtWebGraphAnalog57661AlarmSyslogText,
       "wtWebGraphAnalog57661AlarmSyslogClearText": wtWebGraphAnalog57661AlarmSyslogClearText,
       "wtWebGraphAnalog57661AlarmFtpDataPort": wtWebGraphAnalog57661AlarmFtpDataPort,
       "wtWebGraphAnalog57661AlarmFtpFileName": wtWebGraphAnalog57661AlarmFtpFileName,
       "wtWebGraphAnalog57661AlarmFtpText": wtWebGraphAnalog57661AlarmFtpText,
       "wtWebGraphAnalog57661AlarmFtpClearText": wtWebGraphAnalog57661AlarmFtpClearText,
       "wtWebGraphAnalog57661AlarmFtpOption": wtWebGraphAnalog57661AlarmFtpOption,
       "wtWebGraphAnalog57661AlarmTimerCron": wtWebGraphAnalog57661AlarmTimerCron,
       "wtWebGraphAnalog57661Graphics": wtWebGraphAnalog57661Graphics,
       "wtWebGraphAnalog57661GraphicsBase": wtWebGraphAnalog57661GraphicsBase,
       "wtWebGraphAnalog57661GraphicsBaseEnable": wtWebGraphAnalog57661GraphicsBaseEnable,
       "wtWebGraphAnalog57661GraphicsBaseWidth": wtWebGraphAnalog57661GraphicsBaseWidth,
       "wtWebGraphAnalog57661GraphicsBaseHeight": wtWebGraphAnalog57661GraphicsBaseHeight,
       "wtWebGraphAnalog57661GraphicsBaseFrameColor": wtWebGraphAnalog57661GraphicsBaseFrameColor,
       "wtWebGraphAnalog57661GraphicsBaseBackgroundColor": wtWebGraphAnalog57661GraphicsBaseBackgroundColor,
       "wtWebGraphAnalog57661GraphicsBasePollingrate": wtWebGraphAnalog57661GraphicsBasePollingrate,
       "wtWebGraphAnalog57661GraphicsSelect": wtWebGraphAnalog57661GraphicsSelect,
       "wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel": wtWebGraphAnalog57661GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem": wtWebGraphAnalog57661GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalog57661SensorColor2Table": wtWebGraphAnalog57661SensorColor2Table,
       "wtWebGraphAnalog57661SensorColor2Entry": wtWebGraphAnalog57661SensorColor2Entry,
       "wtWebGraphAnalog57661GraphicsSensorColor": wtWebGraphAnalog57661GraphicsSensorColor,
       "wtWebGraphAnalog57661GraphicsSelectScale": wtWebGraphAnalog57661GraphicsSelectScale,
       "wtWebGraphAnalog57661GraphicsScale": wtWebGraphAnalog57661GraphicsScale,
       "wtWebGraphAnalog57661GraphicsScaleAutoScaleEnable": wtWebGraphAnalog57661GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalog57661GraphicsScaleAutoFitEnable": wtWebGraphAnalog57661GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalog57661GraphicsScale1Min": wtWebGraphAnalog57661GraphicsScale1Min,
       "wtWebGraphAnalog57661GraphicsScale2Min": wtWebGraphAnalog57661GraphicsScale2Min,
       "wtWebGraphAnalog57661GraphicsScale1Max": wtWebGraphAnalog57661GraphicsScale1Max,
       "wtWebGraphAnalog57661GraphicsScale2Max": wtWebGraphAnalog57661GraphicsScale2Max,
       "wtWebGraphAnalog57661GraphicsScale1Unit": wtWebGraphAnalog57661GraphicsScale1Unit,
       "wtWebGraphAnalog57661GraphicsScale2Unit": wtWebGraphAnalog57661GraphicsScale2Unit,
       "wtWebGraphAnalog57661Report": wtWebGraphAnalog57661Report,
       "wtWebGraphAnalog57661ReportCount": wtWebGraphAnalog57661ReportCount,
       "wtWebGraphAnalog57661ReportIfTable": wtWebGraphAnalog57661ReportIfTable,
       "wtWebGraphAnalog57661ReportIfEntry": wtWebGraphAnalog57661ReportIfEntry,
       "wtWebGraphAnalog57661ReportNo": wtWebGraphAnalog57661ReportNo,
       "wtWebGraphAnalog57661ReportTable": wtWebGraphAnalog57661ReportTable,
       "wtWebGraphAnalog57661ReportEntry": wtWebGraphAnalog57661ReportEntry,
       "wtWebGraphAnalog57661ReportEnable": wtWebGraphAnalog57661ReportEnable,
       "wtWebGraphAnalog57661ReportTimerCron": wtWebGraphAnalog57661ReportTimerCron,
       "wtWebGraphAnalog57661ReportMethodeEnable": wtWebGraphAnalog57661ReportMethodeEnable,
       "wtWebGraphAnalog57661ReportEMailAddr": wtWebGraphAnalog57661ReportEMailAddr,
       "wtWebGraphAnalog57661ReportMailSubject": wtWebGraphAnalog57661ReportMailSubject,
       "wtWebGraphAnalog57661ReportMailText": wtWebGraphAnalog57661ReportMailText,
       "wtWebGraphAnalog57661ReportManagerIP": wtWebGraphAnalog57661ReportManagerIP,
       "wtWebGraphAnalog57661ReportTrapText": wtWebGraphAnalog57661ReportTrapText,
       "wtWebGraphAnalog57661ReportMailOptions": wtWebGraphAnalog57661ReportMailOptions,
       "wtWebGraphAnalog57661ReportTcpIpAddr": wtWebGraphAnalog57661ReportTcpIpAddr,
       "wtWebGraphAnalog57661ReportTcpPort": wtWebGraphAnalog57661ReportTcpPort,
       "wtWebGraphAnalog57661ReportTcpText": wtWebGraphAnalog57661ReportTcpText,
       "wtWebGraphAnalog57661ReportClearMailSubject": wtWebGraphAnalog57661ReportClearMailSubject,
       "wtWebGraphAnalog57661ReportClearMailText": wtWebGraphAnalog57661ReportClearMailText,
       "wtWebGraphAnalog57661ReportClearTrapText": wtWebGraphAnalog57661ReportClearTrapText,
       "wtWebGraphAnalog57661ReportClearTcpText": wtWebGraphAnalog57661ReportClearTcpText,
       "wtWebGraphAnalog57661ReportSyslogIpAddr": wtWebGraphAnalog57661ReportSyslogIpAddr,
       "wtWebGraphAnalog57661ReportSyslogPort": wtWebGraphAnalog57661ReportSyslogPort,
       "wtWebGraphAnalog57661ReportSyslogText": wtWebGraphAnalog57661ReportSyslogText,
       "wtWebGraphAnalog57661ReportSyslogClearText": wtWebGraphAnalog57661ReportSyslogClearText,
       "wtWebGraphAnalog57661ReportFtpDataPort": wtWebGraphAnalog57661ReportFtpDataPort,
       "wtWebGraphAnalog57661ReportFtpFileName": wtWebGraphAnalog57661ReportFtpFileName,
       "wtWebGraphAnalog57661ReportFtpText": wtWebGraphAnalog57661ReportFtpText,
       "wtWebGraphAnalog57661ReportFtpClearText": wtWebGraphAnalog57661ReportFtpClearText,
       "wtWebGraphAnalog57661ReportFtpOption": wtWebGraphAnalog57661ReportFtpOption,
       "wtWebGraphAnalog57661Ports": wtWebGraphAnalog57661Ports,
       "wtWebGraphAnalog57661PortTable": wtWebGraphAnalog57661PortTable,
       "wtWebGraphAnalog57661PortEntry": wtWebGraphAnalog57661PortEntry,
       "wtWebGraphAnalog57661PortName": wtWebGraphAnalog57661PortName,
       "wtWebGraphAnalog57661PortText": wtWebGraphAnalog57661PortText,
       "wtWebGraphAnalog57661PortOffset1": wtWebGraphAnalog57661PortOffset1,
       "wtWebGraphAnalog57661SetPoint1": wtWebGraphAnalog57661SetPoint1,
       "wtWebGraphAnalog57661PortOffset2": wtWebGraphAnalog57661PortOffset2,
       "wtWebGraphAnalog57661SetPoint2": wtWebGraphAnalog57661SetPoint2,
       "wtWebGraphAnalog57661PortComment": wtWebGraphAnalog57661PortComment,
       "wtWebGraphAnalog57661PortSensorSelect": wtWebGraphAnalog57661PortSensorSelect,
       "wtWebGraphAnalog57661PortUnit": wtWebGraphAnalog57661PortUnit,
       "wtWebGraphAnalog57661PortScale0": wtWebGraphAnalog57661PortScale0,
       "wtWebGraphAnalog57661PortScale100": wtWebGraphAnalog57661PortScale100,
       "wtWebGraphAnalog57661PortOutputMode": wtWebGraphAnalog57661PortOutputMode,
       "wtWebGraphAnalog57661PortInputMode": wtWebGraphAnalog57661PortInputMode,
       "wtWebGraphAnalog57661Manufact": wtWebGraphAnalog57661Manufact,
       "wtWebGraphAnalog57661MfName": wtWebGraphAnalog57661MfName,
       "wtWebGraphAnalog57661MfAddr": wtWebGraphAnalog57661MfAddr,
       "wtWebGraphAnalog57661MfHotline": wtWebGraphAnalog57661MfHotline,
       "wtWebGraphAnalog57661MfInternet": wtWebGraphAnalog57661MfInternet,
       "wtWebGraphAnalog57661MfDeviceTyp": wtWebGraphAnalog57661MfDeviceTyp,
       "wtWebGraphAnalog57661MfOrderNo": wtWebGraphAnalog57661MfOrderNo,
       "wtWebGraphAnalog57661Diag": wtWebGraphAnalog57661Diag,
       "wtWebGraphAnalog57661DiagErrorCount": wtWebGraphAnalog57661DiagErrorCount,
       "wtWebGraphAnalog57661DiagBinaryError": wtWebGraphAnalog57661DiagBinaryError,
       "wtWebGraphAnalog57661DiagErrorIndex": wtWebGraphAnalog57661DiagErrorIndex,
       "wtWebGraphAnalog57661DiagErrorMessage": wtWebGraphAnalog57661DiagErrorMessage,
       "wtWebGraphAnalog57661DiagErrorClear": wtWebGraphAnalog57661DiagErrorClear}
)
