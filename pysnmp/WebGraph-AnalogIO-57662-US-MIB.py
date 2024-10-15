# SNMP MIB module (WebGraph-AnalogIO-57662-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-AnalogIO-57662-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:35 2024
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
_WtWebGraphAnalog57662_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662 = _WtWebGraphAnalog57662_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29)
)
_WtWebGraphAnalog57662Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Inventory = _WtWebGraphAnalog57662Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1)
)


class _WtWebGraphAnalog57662Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalog57662Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57662Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662Sensors_Object = MibScalar
wtWebGraphAnalog57662Sensors = _WtWebGraphAnalog57662Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 1),
    _WtWebGraphAnalog57662Sensors_Type()
)
wtWebGraphAnalog57662Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Sensors.setStatus("mandatory")
_WtWebGraphAnalog57662SensorTable_Object = MibTable
wtWebGraphAnalog57662SensorTable = _WtWebGraphAnalog57662SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorTable.setStatus("mandatory")
_WtWebGraphAnalog57662SensorEntry_Object = MibTableRow
wtWebGraphAnalog57662SensorEntry = _WtWebGraphAnalog57662SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2, 1)
)
wtWebGraphAnalog57662SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57662SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57662SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662SensorNo_Object = MibTableColumn
wtWebGraphAnalog57662SensorNo = _WtWebGraphAnalog57662SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 2, 1, 1),
    _WtWebGraphAnalog57662SensorNo_Type()
)
wtWebGraphAnalog57662SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorNo.setStatus("mandatory")
_WtWebGraphAnalog57662ValuesTable_Object = MibTable
wtWebGraphAnalog57662ValuesTable = _WtWebGraphAnalog57662ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57662ValuesEntry_Object = MibTableRow
wtWebGraphAnalog57662ValuesEntry = _WtWebGraphAnalog57662ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3, 1)
)
wtWebGraphAnalog57662ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662Values_Type(OctetString):
    """Custom type wtWebGraphAnalog57662Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAnalog57662Values_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662Values_Object = MibTableColumn
wtWebGraphAnalog57662Values = _WtWebGraphAnalog57662Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 3, 1, 1),
    _WtWebGraphAnalog57662Values_Type()
)
wtWebGraphAnalog57662Values.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Values.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryValuesTable_Object = MibTable
wtWebGraphAnalog57662BinaryValuesTable = _WtWebGraphAnalog57662BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalog57662BinaryValuesEntry = _WtWebGraphAnalog57662BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4, 1)
)
wtWebGraphAnalog57662BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryValues_Type = Integer32
_WtWebGraphAnalog57662BinaryValues_Object = MibTableColumn
wtWebGraphAnalog57662BinaryValues = _WtWebGraphAnalog57662BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 1, 4, 1, 1),
    _WtWebGraphAnalog57662BinaryValues_Type()
)
wtWebGraphAnalog57662BinaryValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryValues.setStatus("mandatory")
_WtWebGraphAnalog57662SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662SessCntrl = _WtWebGraphAnalog57662SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2)
)
_WtWebGraphAnalog57662SessCntrlPassword_Type = OctetString
_WtWebGraphAnalog57662SessCntrlPassword_Object = MibScalar
wtWebGraphAnalog57662SessCntrlPassword = _WtWebGraphAnalog57662SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 1),
    _WtWebGraphAnalog57662SessCntrlPassword_Type()
)
wtWebGraphAnalog57662SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalog57662SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57662SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalog57662SessCntrl-NoSession", 0),
          ("wtWebGraphAnalog57662SessCntrl-Session", 1))
    )


_WtWebGraphAnalog57662SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalog57662SessCntrlConfigMode = _WtWebGraphAnalog57662SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 2),
    _WtWebGraphAnalog57662SessCntrlConfigMode_Type()
)
wtWebGraphAnalog57662SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalog57662SessCntrlLogout_Type = Integer32
_WtWebGraphAnalog57662SessCntrlLogout_Object = MibScalar
wtWebGraphAnalog57662SessCntrlLogout = _WtWebGraphAnalog57662SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 3),
    _WtWebGraphAnalog57662SessCntrlLogout_Type()
)
wtWebGraphAnalog57662SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalog57662SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalog57662SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalog57662SessCntrlAdminPassword = _WtWebGraphAnalog57662SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 4),
    _WtWebGraphAnalog57662SessCntrlAdminPassword_Type()
)
wtWebGraphAnalog57662SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalog57662SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalog57662SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalog57662SessCntrlConfigPassword = _WtWebGraphAnalog57662SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 2, 5),
    _WtWebGraphAnalog57662SessCntrlConfigPassword_Type()
)
wtWebGraphAnalog57662SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalog57662Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Config = _WtWebGraphAnalog57662Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3)
)
_WtWebGraphAnalog57662Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Device = _WtWebGraphAnalog57662Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1)
)
_WtWebGraphAnalog57662Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Text = _WtWebGraphAnalog57662Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1)
)
_WtWebGraphAnalog57662DeviceName_Type = OctetString
_WtWebGraphAnalog57662DeviceName_Object = MibScalar
wtWebGraphAnalog57662DeviceName = _WtWebGraphAnalog57662DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 1),
    _WtWebGraphAnalog57662DeviceName_Type()
)
wtWebGraphAnalog57662DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DeviceName.setStatus("mandatory")
_WtWebGraphAnalog57662DeviceText_Type = OctetString
_WtWebGraphAnalog57662DeviceText_Object = MibScalar
wtWebGraphAnalog57662DeviceText = _WtWebGraphAnalog57662DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 2),
    _WtWebGraphAnalog57662DeviceText_Type()
)
wtWebGraphAnalog57662DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DeviceText.setStatus("mandatory")
_WtWebGraphAnalog57662DeviceLocation_Type = OctetString
_WtWebGraphAnalog57662DeviceLocation_Object = MibScalar
wtWebGraphAnalog57662DeviceLocation = _WtWebGraphAnalog57662DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 3),
    _WtWebGraphAnalog57662DeviceLocation_Type()
)
wtWebGraphAnalog57662DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalog57662DeviceContact_Type = OctetString
_WtWebGraphAnalog57662DeviceContact_Object = MibScalar
wtWebGraphAnalog57662DeviceContact = _WtWebGraphAnalog57662DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 1, 4),
    _WtWebGraphAnalog57662DeviceContact_Type()
)
wtWebGraphAnalog57662DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DeviceContact.setStatus("mandatory")
_WtWebGraphAnalog57662TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662TimeDate = _WtWebGraphAnalog57662TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2)
)
_WtWebGraphAnalog57662TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662TimeZone = _WtWebGraphAnalog57662TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1)
)
_WtWebGraphAnalog57662TzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57662TzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57662TzOffsetHrs = _WtWebGraphAnalog57662TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 1),
    _WtWebGraphAnalog57662TzOffsetHrs_Type()
)
wtWebGraphAnalog57662TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57662TzOffsetMin_Type = Integer32
_WtWebGraphAnalog57662TzOffsetMin_Object = MibScalar
wtWebGraphAnalog57662TzOffsetMin = _WtWebGraphAnalog57662TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 2),
    _WtWebGraphAnalog57662TzOffsetMin_Type()
)
wtWebGraphAnalog57662TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57662TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662TzEnable_Object = MibScalar
wtWebGraphAnalog57662TzEnable = _WtWebGraphAnalog57662TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 3),
    _WtWebGraphAnalog57662TzEnable_Type()
)
wtWebGraphAnalog57662TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TzEnable.setStatus("mandatory")
_WtWebGraphAnalog57662StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalog57662StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalog57662StTzOffsetHrs = _WtWebGraphAnalog57662StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 4),
    _WtWebGraphAnalog57662StTzOffsetHrs_Type()
)
wtWebGraphAnalog57662StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalog57662StTzOffsetMin_Type = Integer32
_WtWebGraphAnalog57662StTzOffsetMin_Object = MibScalar
wtWebGraphAnalog57662StTzOffsetMin = _WtWebGraphAnalog57662StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 5),
    _WtWebGraphAnalog57662StTzOffsetMin_Type()
)
wtWebGraphAnalog57662StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662StTzEnable_Object = MibScalar
wtWebGraphAnalog57662StTzEnable = _WtWebGraphAnalog57662StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 6),
    _WtWebGraphAnalog57662StTzEnable_Type()
)
wtWebGraphAnalog57662StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStartMonth based on Integer32"""
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
        *(("wtWebGraphAnalog57662StartMonth-April", 4),
          ("wtWebGraphAnalog57662StartMonth-August", 8),
          ("wtWebGraphAnalog57662StartMonth-December", 12),
          ("wtWebGraphAnalog57662StartMonth-February", 2),
          ("wtWebGraphAnalog57662StartMonth-January", 1),
          ("wtWebGraphAnalog57662StartMonth-July", 7),
          ("wtWebGraphAnalog57662StartMonth-June", 6),
          ("wtWebGraphAnalog57662StartMonth-March", 3),
          ("wtWebGraphAnalog57662StartMonth-May", 5),
          ("wtWebGraphAnalog57662StartMonth-November", 11),
          ("wtWebGraphAnalog57662StartMonth-October", 10),
          ("wtWebGraphAnalog57662StartMonth-September", 9))
    )


_WtWebGraphAnalog57662StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStartMonth_Object = MibScalar
wtWebGraphAnalog57662StTzStartMonth = _WtWebGraphAnalog57662StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 7),
    _WtWebGraphAnalog57662StTzStartMonth_Type()
)
wtWebGraphAnalog57662StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStartMode based on Integer32"""
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
        *(("wtWebGraphAnalog57662StartMode-first", 1),
          ("wtWebGraphAnalog57662StartMode-fourth", 4),
          ("wtWebGraphAnalog57662StartMode-last", 5),
          ("wtWebGraphAnalog57662StartMode-second", 2),
          ("wtWebGraphAnalog57662StartMode-third", 3))
    )


_WtWebGraphAnalog57662StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStartMode_Object = MibScalar
wtWebGraphAnalog57662StTzStartMode = _WtWebGraphAnalog57662StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 8),
    _WtWebGraphAnalog57662StTzStartMode_Type()
)
wtWebGraphAnalog57662StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStartWday based on Integer32"""
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
        *(("wtWebGraphAnalog57662StartWday-Friday", 6),
          ("wtWebGraphAnalog57662StartWday-Monday", 2),
          ("wtWebGraphAnalog57662StartWday-Saturday", 7),
          ("wtWebGraphAnalog57662StartWday-Sunday", 1),
          ("wtWebGraphAnalog57662StartWday-Thursday", 4),
          ("wtWebGraphAnalog57662StartWday-Tuesday", 3),
          ("wtWebGraphAnalog57662StartWday-Wednesday", 5))
    )


_WtWebGraphAnalog57662StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStartWday_Object = MibScalar
wtWebGraphAnalog57662StTzStartWday = _WtWebGraphAnalog57662StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 9),
    _WtWebGraphAnalog57662StTzStartWday_Type()
)
wtWebGraphAnalog57662StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalog57662StTzStartHrs_Type = Integer32
_WtWebGraphAnalog57662StTzStartHrs_Object = MibScalar
wtWebGraphAnalog57662StTzStartHrs = _WtWebGraphAnalog57662StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 10),
    _WtWebGraphAnalog57662StTzStartHrs_Type()
)
wtWebGraphAnalog57662StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalog57662StTzStartMin_Type = Integer32
_WtWebGraphAnalog57662StTzStartMin_Object = MibScalar
wtWebGraphAnalog57662StTzStartMin = _WtWebGraphAnalog57662StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 11),
    _WtWebGraphAnalog57662StTzStartMin_Type()
)
wtWebGraphAnalog57662StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStopMonth based on Integer32"""
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
        *(("wtWebGraphAnalog57662StopMonth-April", 4),
          ("wtWebGraphAnalog57662StopMonth-August", 8),
          ("wtWebGraphAnalog57662StopMonth-December", 12),
          ("wtWebGraphAnalog57662StopMonth-February", 2),
          ("wtWebGraphAnalog57662StopMonth-January", 1),
          ("wtWebGraphAnalog57662StopMonth-July", 7),
          ("wtWebGraphAnalog57662StopMonth-June", 6),
          ("wtWebGraphAnalog57662StopMonth-March", 3),
          ("wtWebGraphAnalog57662StopMonth-May", 5),
          ("wtWebGraphAnalog57662StopMonth-November", 11),
          ("wtWebGraphAnalog57662StopMonth-October", 10),
          ("wtWebGraphAnalog57662StopMonth-September", 9))
    )


_WtWebGraphAnalog57662StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStopMonth_Object = MibScalar
wtWebGraphAnalog57662StTzStopMonth = _WtWebGraphAnalog57662StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 12),
    _WtWebGraphAnalog57662StTzStopMonth_Type()
)
wtWebGraphAnalog57662StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStopMode based on Integer32"""
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
        *(("wtWebGraphAnalog57662StopMode-first", 1),
          ("wtWebGraphAnalog57662StopMode-fourth", 4),
          ("wtWebGraphAnalog57662StopMode-last", 5),
          ("wtWebGraphAnalog57662StopMode-second", 2),
          ("wtWebGraphAnalog57662StopMode-third", 3))
    )


_WtWebGraphAnalog57662StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStopMode_Object = MibScalar
wtWebGraphAnalog57662StTzStopMode = _WtWebGraphAnalog57662StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 13),
    _WtWebGraphAnalog57662StTzStopMode_Type()
)
wtWebGraphAnalog57662StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalog57662StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalog57662StTzStopWday based on Integer32"""
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
        *(("wtWebGraphAnalog57662StopWday-Friday", 6),
          ("wtWebGraphAnalog57662StopWday-Monday", 2),
          ("wtWebGraphAnalog57662StopWday-Saturday", 7),
          ("wtWebGraphAnalog57662StopWday-Sunday", 1),
          ("wtWebGraphAnalog57662StopWday-Thursday", 4),
          ("wtWebGraphAnalog57662StopWday-Tuesday", 3),
          ("wtWebGraphAnalog57662StopWday-Wednesday", 5))
    )


_WtWebGraphAnalog57662StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662StTzStopWday_Object = MibScalar
wtWebGraphAnalog57662StTzStopWday = _WtWebGraphAnalog57662StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 14),
    _WtWebGraphAnalog57662StTzStopWday_Type()
)
wtWebGraphAnalog57662StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalog57662StTzStopHrs_Type = Integer32
_WtWebGraphAnalog57662StTzStopHrs_Object = MibScalar
wtWebGraphAnalog57662StTzStopHrs = _WtWebGraphAnalog57662StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 15),
    _WtWebGraphAnalog57662StTzStopHrs_Type()
)
wtWebGraphAnalog57662StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalog57662StTzStopMin_Type = Integer32
_WtWebGraphAnalog57662StTzStopMin_Object = MibScalar
wtWebGraphAnalog57662StTzStopMin = _WtWebGraphAnalog57662StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 1, 16),
    _WtWebGraphAnalog57662StTzStopMin_Type()
)
wtWebGraphAnalog57662StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalog57662TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662TimeServer = _WtWebGraphAnalog57662TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2)
)
_WtWebGraphAnalog57662TimeServer1_Type = OctetString
_WtWebGraphAnalog57662TimeServer1_Object = MibScalar
wtWebGraphAnalog57662TimeServer1 = _WtWebGraphAnalog57662TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 1),
    _WtWebGraphAnalog57662TimeServer1_Type()
)
wtWebGraphAnalog57662TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TimeServer1.setStatus("mandatory")
_WtWebGraphAnalog57662TimeServer2_Type = OctetString
_WtWebGraphAnalog57662TimeServer2_Object = MibScalar
wtWebGraphAnalog57662TimeServer2 = _WtWebGraphAnalog57662TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 2),
    _WtWebGraphAnalog57662TimeServer2_Type()
)
wtWebGraphAnalog57662TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalog57662TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662TsEnable_Object = MibScalar
wtWebGraphAnalog57662TsEnable = _WtWebGraphAnalog57662TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 3),
    _WtWebGraphAnalog57662TsEnable_Type()
)
wtWebGraphAnalog57662TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TsEnable.setStatus("mandatory")
_WtWebGraphAnalog57662TsSyncTime_Type = Integer32
_WtWebGraphAnalog57662TsSyncTime_Object = MibScalar
wtWebGraphAnalog57662TsSyncTime = _WtWebGraphAnalog57662TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 2, 4),
    _WtWebGraphAnalog57662TsSyncTime_Type()
)
wtWebGraphAnalog57662TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalog57662DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662DeviceClock = _WtWebGraphAnalog57662DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3)
)


class _WtWebGraphAnalog57662ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalog57662ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ClockHrs_Object = MibScalar
wtWebGraphAnalog57662ClockHrs = _WtWebGraphAnalog57662ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 1),
    _WtWebGraphAnalog57662ClockHrs_Type()
)
wtWebGraphAnalog57662ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalog57662ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalog57662ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ClockMin_Object = MibScalar
wtWebGraphAnalog57662ClockMin = _WtWebGraphAnalog57662ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 2),
    _WtWebGraphAnalog57662ClockMin_Type()
)
wtWebGraphAnalog57662ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ClockMin.setStatus("mandatory")


class _WtWebGraphAnalog57662ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalog57662ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ClockDay_Object = MibScalar
wtWebGraphAnalog57662ClockDay = _WtWebGraphAnalog57662ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 3),
    _WtWebGraphAnalog57662ClockDay_Type()
)
wtWebGraphAnalog57662ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ClockDay.setStatus("mandatory")


class _WtWebGraphAnalog57662ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ClockMonth based on Integer32"""
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
        *(("wtWebGraphAnalog57662ClockMonth-April", 4),
          ("wtWebGraphAnalog57662ClockMonth-August", 8),
          ("wtWebGraphAnalog57662ClockMonth-December", 12),
          ("wtWebGraphAnalog57662ClockMonth-February", 2),
          ("wtWebGraphAnalog57662ClockMonth-January", 1),
          ("wtWebGraphAnalog57662ClockMonth-July", 7),
          ("wtWebGraphAnalog57662ClockMonth-June", 6),
          ("wtWebGraphAnalog57662ClockMonth-March", 3),
          ("wtWebGraphAnalog57662ClockMonth-May", 5),
          ("wtWebGraphAnalog57662ClockMonth-November", 11),
          ("wtWebGraphAnalog57662ClockMonth-October", 10),
          ("wtWebGraphAnalog57662ClockMonth-September", 9))
    )


_WtWebGraphAnalog57662ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ClockMonth_Object = MibScalar
wtWebGraphAnalog57662ClockMonth = _WtWebGraphAnalog57662ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 4),
    _WtWebGraphAnalog57662ClockMonth_Type()
)
wtWebGraphAnalog57662ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalog57662ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57662ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ClockYear_Object = MibScalar
wtWebGraphAnalog57662ClockYear = _WtWebGraphAnalog57662ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 2, 3, 5),
    _WtWebGraphAnalog57662ClockYear_Type()
)
wtWebGraphAnalog57662ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ClockYear.setStatus("mandatory")
_WtWebGraphAnalog57662Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Basic = _WtWebGraphAnalog57662Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3)
)
_WtWebGraphAnalog57662Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Network = _WtWebGraphAnalog57662Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1)
)
_WtWebGraphAnalog57662IpAddress_Type = IpAddress
_WtWebGraphAnalog57662IpAddress_Object = MibScalar
wtWebGraphAnalog57662IpAddress = _WtWebGraphAnalog57662IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 1),
    _WtWebGraphAnalog57662IpAddress_Type()
)
wtWebGraphAnalog57662IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662IpAddress.setStatus("mandatory")
_WtWebGraphAnalog57662SubnetMask_Type = IpAddress
_WtWebGraphAnalog57662SubnetMask_Object = MibScalar
wtWebGraphAnalog57662SubnetMask = _WtWebGraphAnalog57662SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 2),
    _WtWebGraphAnalog57662SubnetMask_Type()
)
wtWebGraphAnalog57662SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SubnetMask.setStatus("mandatory")
_WtWebGraphAnalog57662Gateway_Type = IpAddress
_WtWebGraphAnalog57662Gateway_Object = MibScalar
wtWebGraphAnalog57662Gateway = _WtWebGraphAnalog57662Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 3),
    _WtWebGraphAnalog57662Gateway_Type()
)
wtWebGraphAnalog57662Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Gateway.setStatus("mandatory")
_WtWebGraphAnalog57662DnsServer1_Type = OctetString
_WtWebGraphAnalog57662DnsServer1_Object = MibScalar
wtWebGraphAnalog57662DnsServer1 = _WtWebGraphAnalog57662DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 4),
    _WtWebGraphAnalog57662DnsServer1_Type()
)
wtWebGraphAnalog57662DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DnsServer1.setStatus("mandatory")
_WtWebGraphAnalog57662DnsServer2_Type = OctetString
_WtWebGraphAnalog57662DnsServer2_Object = MibScalar
wtWebGraphAnalog57662DnsServer2 = _WtWebGraphAnalog57662DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 5),
    _WtWebGraphAnalog57662DnsServer2_Type()
)
wtWebGraphAnalog57662DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DnsServer2.setStatus("mandatory")
_WtWebGraphAnalog57662AddConfig_Type = OctetString
_WtWebGraphAnalog57662AddConfig_Object = MibScalar
wtWebGraphAnalog57662AddConfig = _WtWebGraphAnalog57662AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 1, 6),
    _WtWebGraphAnalog57662AddConfig_Type()
)
wtWebGraphAnalog57662AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AddConfig.setStatus("mandatory")
_WtWebGraphAnalog57662HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662HTTP = _WtWebGraphAnalog57662HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2)
)
_WtWebGraphAnalog57662Startup_Type = OctetString
_WtWebGraphAnalog57662Startup_Object = MibScalar
wtWebGraphAnalog57662Startup = _WtWebGraphAnalog57662Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 1),
    _WtWebGraphAnalog57662Startup_Type()
)
wtWebGraphAnalog57662Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Startup.setStatus("mandatory")
_WtWebGraphAnalog57662GetHeaderEnable_Type = OctetString
_WtWebGraphAnalog57662GetHeaderEnable_Object = MibScalar
wtWebGraphAnalog57662GetHeaderEnable = _WtWebGraphAnalog57662GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 2),
    _WtWebGraphAnalog57662GetHeaderEnable_Type()
)
wtWebGraphAnalog57662GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalog57662HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662HttpPort_Object = MibScalar
wtWebGraphAnalog57662HttpPort = _WtWebGraphAnalog57662HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 2, 3),
    _WtWebGraphAnalog57662HttpPort_Type()
)
wtWebGraphAnalog57662HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662HttpPort.setStatus("mandatory")
_WtWebGraphAnalog57662Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Mail = _WtWebGraphAnalog57662Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3)
)
_WtWebGraphAnalog57662MailAdName_Type = OctetString
_WtWebGraphAnalog57662MailAdName_Object = MibScalar
wtWebGraphAnalog57662MailAdName = _WtWebGraphAnalog57662MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 1),
    _WtWebGraphAnalog57662MailAdName_Type()
)
wtWebGraphAnalog57662MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailAdName.setStatus("mandatory")
_WtWebGraphAnalog57662MailReply_Type = OctetString
_WtWebGraphAnalog57662MailReply_Object = MibScalar
wtWebGraphAnalog57662MailReply = _WtWebGraphAnalog57662MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 2),
    _WtWebGraphAnalog57662MailReply_Type()
)
wtWebGraphAnalog57662MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailReply.setStatus("mandatory")
_WtWebGraphAnalog57662MailServer_Type = OctetString
_WtWebGraphAnalog57662MailServer_Object = MibScalar
wtWebGraphAnalog57662MailServer = _WtWebGraphAnalog57662MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 3),
    _WtWebGraphAnalog57662MailServer_Type()
)
wtWebGraphAnalog57662MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalog57662MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalog57662MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662MailAuthentication_Object = MibScalar
wtWebGraphAnalog57662MailAuthentication = _WtWebGraphAnalog57662MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 5),
    _WtWebGraphAnalog57662MailAuthentication_Type()
)
wtWebGraphAnalog57662MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalog57662MailAuthUser_Type = OctetString
_WtWebGraphAnalog57662MailAuthUser_Object = MibScalar
wtWebGraphAnalog57662MailAuthUser = _WtWebGraphAnalog57662MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 6),
    _WtWebGraphAnalog57662MailAuthUser_Type()
)
wtWebGraphAnalog57662MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalog57662MailAuthPassword_Type = OctetString
_WtWebGraphAnalog57662MailAuthPassword_Object = MibScalar
wtWebGraphAnalog57662MailAuthPassword = _WtWebGraphAnalog57662MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 7),
    _WtWebGraphAnalog57662MailAuthPassword_Type()
)
wtWebGraphAnalog57662MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalog57662MailPop3Server_Type = OctetString
_WtWebGraphAnalog57662MailPop3Server_Object = MibScalar
wtWebGraphAnalog57662MailPop3Server = _WtWebGraphAnalog57662MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 3, 8),
    _WtWebGraphAnalog57662MailPop3Server_Type()
)
wtWebGraphAnalog57662MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalog57662SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662SNMP = _WtWebGraphAnalog57662SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4)
)
_WtWebGraphAnalog57662SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalog57662SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalog57662SnmpCommunityStringRead = _WtWebGraphAnalog57662SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 1),
    _WtWebGraphAnalog57662SnmpCommunityStringRead_Type()
)
wtWebGraphAnalog57662SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalog57662SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalog57662SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalog57662SnmpCommunityStringReadWrite = _WtWebGraphAnalog57662SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 2),
    _WtWebGraphAnalog57662SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalog57662SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalog57662SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalog57662SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalog57662SystemTrapManagerIP = _WtWebGraphAnalog57662SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 3),
    _WtWebGraphAnalog57662SystemTrapManagerIP_Type()
)
wtWebGraphAnalog57662SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalog57662SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662SystemTrapEnable_Object = MibScalar
wtWebGraphAnalog57662SystemTrapEnable = _WtWebGraphAnalog57662SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 4),
    _WtWebGraphAnalog57662SystemTrapEnable_Type()
)
wtWebGraphAnalog57662SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalog57662SnmpEnable_Type = OctetString
_WtWebGraphAnalog57662SnmpEnable_Object = MibScalar
wtWebGraphAnalog57662SnmpEnable = _WtWebGraphAnalog57662SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 5),
    _WtWebGraphAnalog57662SnmpEnable_Type()
)
wtWebGraphAnalog57662SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalog57662SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalog57662SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalog57662SnmpCommunityStringTrap = _WtWebGraphAnalog57662SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 4, 6),
    _WtWebGraphAnalog57662SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalog57662SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalog57662UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662UDP = _WtWebGraphAnalog57662UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5)
)


class _WtWebGraphAnalog57662UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662UdpPort_Object = MibScalar
wtWebGraphAnalog57662UdpPort = _WtWebGraphAnalog57662UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5, 1),
    _WtWebGraphAnalog57662UdpPort_Type()
)
wtWebGraphAnalog57662UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662UdpPort.setStatus("mandatory")
_WtWebGraphAnalog57662UdpEnable_Type = OctetString
_WtWebGraphAnalog57662UdpEnable_Object = MibScalar
wtWebGraphAnalog57662UdpEnable = _WtWebGraphAnalog57662UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 5, 2),
    _WtWebGraphAnalog57662UdpEnable_Type()
)
wtWebGraphAnalog57662UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662UdpEnable.setStatus("mandatory")
_WtWebGraphAnalog57662Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Syslog = _WtWebGraphAnalog57662Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6)
)
_WtWebGraphAnalog57662SyslogServerIP_Type = OctetString
_WtWebGraphAnalog57662SyslogServerIP_Object = MibScalar
wtWebGraphAnalog57662SyslogServerIP = _WtWebGraphAnalog57662SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 1),
    _WtWebGraphAnalog57662SyslogServerIP_Type()
)
wtWebGraphAnalog57662SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalog57662SyslogServerPort_Type = Integer32
_WtWebGraphAnalog57662SyslogServerPort_Object = MibScalar
wtWebGraphAnalog57662SyslogServerPort = _WtWebGraphAnalog57662SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 2),
    _WtWebGraphAnalog57662SyslogServerPort_Type()
)
wtWebGraphAnalog57662SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalog57662SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalog57662SyslogSystemMessagesEnable = _WtWebGraphAnalog57662SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 3),
    _WtWebGraphAnalog57662SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalog57662SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalog57662SyslogEnable_Type = OctetString
_WtWebGraphAnalog57662SyslogEnable_Object = MibScalar
wtWebGraphAnalog57662SyslogEnable = _WtWebGraphAnalog57662SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 6, 4),
    _WtWebGraphAnalog57662SyslogEnable_Type()
)
wtWebGraphAnalog57662SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalog57662FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662FTP = _WtWebGraphAnalog57662FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7)
)
_WtWebGraphAnalog57662FTPServerIP_Type = OctetString
_WtWebGraphAnalog57662FTPServerIP_Object = MibScalar
wtWebGraphAnalog57662FTPServerIP = _WtWebGraphAnalog57662FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 1),
    _WtWebGraphAnalog57662FTPServerIP_Type()
)
wtWebGraphAnalog57662FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalog57662FTPServerControlPort_Type = Integer32
_WtWebGraphAnalog57662FTPServerControlPort_Object = MibScalar
wtWebGraphAnalog57662FTPServerControlPort = _WtWebGraphAnalog57662FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 2),
    _WtWebGraphAnalog57662FTPServerControlPort_Type()
)
wtWebGraphAnalog57662FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalog57662FTPUserName_Type = OctetString
_WtWebGraphAnalog57662FTPUserName_Object = MibScalar
wtWebGraphAnalog57662FTPUserName = _WtWebGraphAnalog57662FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 3),
    _WtWebGraphAnalog57662FTPUserName_Type()
)
wtWebGraphAnalog57662FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPUserName.setStatus("mandatory")
_WtWebGraphAnalog57662FTPPassword_Type = OctetString
_WtWebGraphAnalog57662FTPPassword_Object = MibScalar
wtWebGraphAnalog57662FTPPassword = _WtWebGraphAnalog57662FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 4),
    _WtWebGraphAnalog57662FTPPassword_Type()
)
wtWebGraphAnalog57662FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPPassword.setStatus("mandatory")
_WtWebGraphAnalog57662FTPAccount_Type = OctetString
_WtWebGraphAnalog57662FTPAccount_Object = MibScalar
wtWebGraphAnalog57662FTPAccount = _WtWebGraphAnalog57662FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 5),
    _WtWebGraphAnalog57662FTPAccount_Type()
)
wtWebGraphAnalog57662FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPAccount.setStatus("mandatory")
_WtWebGraphAnalog57662FTPOption_Type = OctetString
_WtWebGraphAnalog57662FTPOption_Object = MibScalar
wtWebGraphAnalog57662FTPOption = _WtWebGraphAnalog57662FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 6),
    _WtWebGraphAnalog57662FTPOption_Type()
)
wtWebGraphAnalog57662FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPOption.setStatus("mandatory")
_WtWebGraphAnalog57662FTPEnable_Type = OctetString
_WtWebGraphAnalog57662FTPEnable_Object = MibScalar
wtWebGraphAnalog57662FTPEnable = _WtWebGraphAnalog57662FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 7, 7),
    _WtWebGraphAnalog57662FTPEnable_Type()
)
wtWebGraphAnalog57662FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662FTPEnable.setStatus("mandatory")
_WtWebGraphAnalog57662Language_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Language = _WtWebGraphAnalog57662Language_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 8)
)
_WtWebGraphAnalog57662LanguageSelect_Type = OctetString
_WtWebGraphAnalog57662LanguageSelect_Object = MibScalar
wtWebGraphAnalog57662LanguageSelect = _WtWebGraphAnalog57662LanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 8, 1),
    _WtWebGraphAnalog57662LanguageSelect_Type()
)
wtWebGraphAnalog57662LanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662LanguageSelect.setStatus("mandatory")
_WtWebGraphAnalog57662Binary_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Binary = _WtWebGraphAnalog57662Binary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9)
)


class _WtWebGraphAnalog57662BinaryModeCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryModeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57662BinaryModeCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryModeCount_Object = MibScalar
wtWebGraphAnalog57662BinaryModeCount = _WtWebGraphAnalog57662BinaryModeCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 1),
    _WtWebGraphAnalog57662BinaryModeCount_Type()
)
wtWebGraphAnalog57662BinaryModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryModeCount.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryIfTable_Object = MibTable
wtWebGraphAnalog57662BinaryIfTable = _WtWebGraphAnalog57662BinaryIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryIfTable.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryIfEntry_Object = MibTableRow
wtWebGraphAnalog57662BinaryIfEntry = _WtWebGraphAnalog57662BinaryIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2, 1)
)
wtWebGraphAnalog57662BinaryIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryModeNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryModeNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalog57662BinaryModeNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryModeNo_Object = MibTableColumn
wtWebGraphAnalog57662BinaryModeNo = _WtWebGraphAnalog57662BinaryModeNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 2, 1, 1),
    _WtWebGraphAnalog57662BinaryModeNo_Type()
)
wtWebGraphAnalog57662BinaryModeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryModeNo.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTable_Object = MibTable
wtWebGraphAnalog57662BinaryTable = _WtWebGraphAnalog57662BinaryTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTable.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryEntry_Object = MibTableRow
wtWebGraphAnalog57662BinaryEntry = _WtWebGraphAnalog57662BinaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1)
)
wtWebGraphAnalog57662BinaryEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662BinaryModeNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryOperationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryOperationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryOperationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryOperationMode_Object = MibTableColumn
wtWebGraphAnalog57662BinaryOperationMode = _WtWebGraphAnalog57662BinaryOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 1),
    _WtWebGraphAnalog57662BinaryOperationMode_Type()
)
wtWebGraphAnalog57662BinaryOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryOperationMode.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpServerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpServerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpServerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpServerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerLocalPort = _WtWebGraphAnalog57662BinaryTcpServerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 2),
    _WtWebGraphAnalog57662BinaryTcpServerLocalPort_Type()
)
wtWebGraphAnalog57662BinaryTcpServerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpServerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryTcpServerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryTcpServerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryTcpServerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerInputTrigger = _WtWebGraphAnalog57662BinaryTcpServerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 3),
    _WtWebGraphAnalog57662BinaryTcpServerInputTrigger_Type()
)
wtWebGraphAnalog57662BinaryTcpServerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpServerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryTcpServerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryTcpServerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryTcpServerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerApplicationMode = _WtWebGraphAnalog57662BinaryTcpServerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 4),
    _WtWebGraphAnalog57662BinaryTcpServerApplicationMode_Type()
)
wtWebGraphAnalog57662BinaryTcpServerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpClientLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpClientLocalPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientLocalPort = _WtWebGraphAnalog57662BinaryTcpClientLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 5),
    _WtWebGraphAnalog57662BinaryTcpClientLocalPort_Type()
)
wtWebGraphAnalog57662BinaryTcpClientLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientServerPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpClientServerPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpClientServerPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientServerPort = _WtWebGraphAnalog57662BinaryTcpClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 6),
    _WtWebGraphAnalog57662BinaryTcpClientServerPort_Type()
)
wtWebGraphAnalog57662BinaryTcpClientServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientServerPort.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpClientServerIpAddr_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpClientServerIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientServerIpAddr = _WtWebGraphAnalog57662BinaryTcpClientServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 7),
    _WtWebGraphAnalog57662BinaryTcpClientServerIpAddr_Type()
)
wtWebGraphAnalog57662BinaryTcpClientServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientServerIpAddr.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpClientServerPassword_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpClientServerPassword_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientServerPassword = _WtWebGraphAnalog57662BinaryTcpClientServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 8),
    _WtWebGraphAnalog57662BinaryTcpClientServerPassword_Type()
)
wtWebGraphAnalog57662BinaryTcpClientServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientServerPassword.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpClientInactivity_Type = Integer32
_WtWebGraphAnalog57662BinaryTcpClientInactivity_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientInactivity = _WtWebGraphAnalog57662BinaryTcpClientInactivity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 9),
    _WtWebGraphAnalog57662BinaryTcpClientInactivity_Type()
)
wtWebGraphAnalog57662BinaryTcpClientInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientInactivity.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryTcpClientInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryTcpClientInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientInputTrigger = _WtWebGraphAnalog57662BinaryTcpClientInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 10),
    _WtWebGraphAnalog57662BinaryTcpClientInputTrigger_Type()
)
wtWebGraphAnalog57662BinaryTcpClientInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpClientInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpClientInterval_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientInterval = _WtWebGraphAnalog57662BinaryTcpClientInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 11),
    _WtWebGraphAnalog57662BinaryTcpClientInterval_Type()
)
wtWebGraphAnalog57662BinaryTcpClientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientInterval.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryTcpClientApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryTcpClientApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientApplicationMode = _WtWebGraphAnalog57662BinaryTcpClientApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 12),
    _WtWebGraphAnalog57662BinaryTcpClientApplicationMode_Type()
)
wtWebGraphAnalog57662BinaryTcpClientApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryUdpPeerLocalPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryUdpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryUdpPeerLocalPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryUdpPeerLocalPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerLocalPort = _WtWebGraphAnalog57662BinaryUdpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 13),
    _WtWebGraphAnalog57662BinaryUdpPeerLocalPort_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerLocalPort.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryUdpPeerRemotePort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryUdpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryUdpPeerRemotePort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryUdpPeerRemotePort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerRemotePort = _WtWebGraphAnalog57662BinaryUdpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 14),
    _WtWebGraphAnalog57662BinaryUdpPeerRemotePort_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerRemotePort.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr_Type = OctetString
_WtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr = _WtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 15),
    _WtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryUdpPeerInputTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryUdpPeerInputTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryUdpPeerInputTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryUdpPeerInputTrigger_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerInputTrigger = _WtWebGraphAnalog57662BinaryUdpPeerInputTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 16),
    _WtWebGraphAnalog57662BinaryUdpPeerInputTrigger_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerInputTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerInputTrigger.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryUdpPeerInterval_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryUdpPeerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalog57662BinaryUdpPeerInterval_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryUdpPeerInterval_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerInterval = _WtWebGraphAnalog57662BinaryUdpPeerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 17),
    _WtWebGraphAnalog57662BinaryUdpPeerInterval_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerInterval.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryUdpPeerApplicationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662BinaryUdpPeerApplicationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662BinaryUdpPeerApplicationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662BinaryUdpPeerApplicationMode_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerApplicationMode = _WtWebGraphAnalog57662BinaryUdpPeerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 18),
    _WtWebGraphAnalog57662BinaryUdpPeerApplicationMode_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerApplicationMode.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryConnectedPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryConnectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryConnectedPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryConnectedPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryConnectedPort = _WtWebGraphAnalog57662BinaryConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 19),
    _WtWebGraphAnalog57662BinaryConnectedPort_Type()
)
wtWebGraphAnalog57662BinaryConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryConnectedPort.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryConnectedIpAddr_Type = IpAddress
_WtWebGraphAnalog57662BinaryConnectedIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662BinaryConnectedIpAddr = _WtWebGraphAnalog57662BinaryConnectedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 20),
    _WtWebGraphAnalog57662BinaryConnectedIpAddr_Type()
)
wtWebGraphAnalog57662BinaryConnectedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryConnectedIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpServerClientHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpServerClientHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpServerClientHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpServerClientHttpPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerClientHttpPort = _WtWebGraphAnalog57662BinaryTcpServerClientHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 21),
    _WtWebGraphAnalog57662BinaryTcpServerClientHttpPort_Type()
)
wtWebGraphAnalog57662BinaryTcpServerClientHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerClientHttpPort.setStatus("mandatory")


class _WtWebGraphAnalog57662BinaryTcpClientServerHttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662BinaryTcpClientServerHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662BinaryTcpClientServerHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662BinaryTcpClientServerHttpPort_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientServerHttpPort = _WtWebGraphAnalog57662BinaryTcpClientServerHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 22),
    _WtWebGraphAnalog57662BinaryTcpClientServerHttpPort_Type()
)
wtWebGraphAnalog57662BinaryTcpClientServerHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientServerHttpPort.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpServerHysteresis1_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpServerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerHysteresis1 = _WtWebGraphAnalog57662BinaryTcpServerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 23),
    _WtWebGraphAnalog57662BinaryTcpServerHysteresis1_Type()
)
wtWebGraphAnalog57662BinaryTcpServerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpServerHysteresis2_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpServerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpServerHysteresis2 = _WtWebGraphAnalog57662BinaryTcpServerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 24),
    _WtWebGraphAnalog57662BinaryTcpServerHysteresis2_Type()
)
wtWebGraphAnalog57662BinaryTcpServerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpServerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpClientHysteresis1_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpClientHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientHysteresis1 = _WtWebGraphAnalog57662BinaryTcpClientHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 25),
    _WtWebGraphAnalog57662BinaryTcpClientHysteresis1_Type()
)
wtWebGraphAnalog57662BinaryTcpClientHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryTcpClientHysteresis2_Type = OctetString
_WtWebGraphAnalog57662BinaryTcpClientHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57662BinaryTcpClientHysteresis2 = _WtWebGraphAnalog57662BinaryTcpClientHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 26),
    _WtWebGraphAnalog57662BinaryTcpClientHysteresis2_Type()
)
wtWebGraphAnalog57662BinaryTcpClientHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryTcpClientHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryUdpPeerHysteresis1_Type = OctetString
_WtWebGraphAnalog57662BinaryUdpPeerHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerHysteresis1 = _WtWebGraphAnalog57662BinaryUdpPeerHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 27),
    _WtWebGraphAnalog57662BinaryUdpPeerHysteresis1_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57662BinaryUdpPeerHysteresis2_Type = OctetString
_WtWebGraphAnalog57662BinaryUdpPeerHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57662BinaryUdpPeerHysteresis2 = _WtWebGraphAnalog57662BinaryUdpPeerHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 3, 9, 3, 1, 28),
    _WtWebGraphAnalog57662BinaryUdpPeerHysteresis2_Type()
)
wtWebGraphAnalog57662BinaryUdpPeerHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662BinaryUdpPeerHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57662Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Datalogger = _WtWebGraphAnalog57662Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4)
)


class _WtWebGraphAnalog57662LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalog57662LoggerTimebase based on Integer32"""
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
        *(("wtWebGraphAnalog57662Datalogger-15Min", 5),
          ("wtWebGraphAnalog57662Datalogger-15Sec", 1),
          ("wtWebGraphAnalog57662Datalogger-1Min", 3),
          ("wtWebGraphAnalog57662Datalogger-30Sec", 2),
          ("wtWebGraphAnalog57662Datalogger-5Min", 4),
          ("wtWebGraphAnalog57662Datalogger-60Min", 6))
    )


_WtWebGraphAnalog57662LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662LoggerTimebase_Object = MibScalar
wtWebGraphAnalog57662LoggerTimebase = _WtWebGraphAnalog57662LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 1),
    _WtWebGraphAnalog57662LoggerTimebase_Type()
)
wtWebGraphAnalog57662LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalog57662LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57662LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662LoggerSensorSel_Object = MibScalar
wtWebGraphAnalog57662LoggerSensorSel = _WtWebGraphAnalog57662LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 2),
    _WtWebGraphAnalog57662LoggerSensorSel_Type()
)
wtWebGraphAnalog57662LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662LoggerSensorSel.setStatus("mandatory")


class _WtWebGraphAnalog57662DisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57662DisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662DisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662DisplaySensorSel_Object = MibScalar
wtWebGraphAnalog57662DisplaySensorSel = _WtWebGraphAnalog57662DisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 3),
    _WtWebGraphAnalog57662DisplaySensorSel_Type()
)
wtWebGraphAnalog57662DisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DisplaySensorSel.setStatus("mandatory")
_WtWebGraphAnalog57662SensorColorTable_Object = MibTable
wtWebGraphAnalog57662SensorColorTable = _WtWebGraphAnalog57662SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorColorTable.setStatus("mandatory")
_WtWebGraphAnalog57662SensorColorEntry_Object = MibTableRow
wtWebGraphAnalog57662SensorColorEntry = _WtWebGraphAnalog57662SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 4, 1)
)
wtWebGraphAnalog57662SensorColorEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorColorEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662SensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57662SensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57662SensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662SensorColor_Object = MibTableColumn
wtWebGraphAnalog57662SensorColor = _WtWebGraphAnalog57662SensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 4, 1, 1),
    _WtWebGraphAnalog57662SensorColor_Type()
)
wtWebGraphAnalog57662SensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorColor.setStatus("mandatory")
_WtWebGraphAnalog57662AutoScaleEnable_Type = OctetString
_WtWebGraphAnalog57662AutoScaleEnable_Object = MibScalar
wtWebGraphAnalog57662AutoScaleEnable = _WtWebGraphAnalog57662AutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 5),
    _WtWebGraphAnalog57662AutoScaleEnable_Type()
)
wtWebGraphAnalog57662AutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalog57662VerticalUpperLimit_Type = OctetString
_WtWebGraphAnalog57662VerticalUpperLimit_Object = MibScalar
wtWebGraphAnalog57662VerticalUpperLimit = _WtWebGraphAnalog57662VerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 6),
    _WtWebGraphAnalog57662VerticalUpperLimit_Type()
)
wtWebGraphAnalog57662VerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662VerticalUpperLimit.setStatus("mandatory")
_WtWebGraphAnalog57662VerticalLowerLimit_Type = OctetString
_WtWebGraphAnalog57662VerticalLowerLimit_Object = MibScalar
wtWebGraphAnalog57662VerticalLowerLimit = _WtWebGraphAnalog57662VerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 7),
    _WtWebGraphAnalog57662VerticalLowerLimit_Type()
)
wtWebGraphAnalog57662VerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662VerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphAnalog57662HorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphAnalog57662HorizontalZoom based on Integer32"""
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
        *(("wtWebGraphAnalog57662Zoom-25days", 6),
          ("wtWebGraphAnalog57662Zoom-25min", 1),
          ("wtWebGraphAnalog57662Zoom-30hrs", 4),
          ("wtWebGraphAnalog57662Zoom-5days", 5),
          ("wtWebGraphAnalog57662Zoom-5hrs", 3),
          ("wtWebGraphAnalog57662Zoom-75min", 2))
    )


_WtWebGraphAnalog57662HorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662HorizontalZoom_Object = MibScalar
wtWebGraphAnalog57662HorizontalZoom = _WtWebGraphAnalog57662HorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 4, 8),
    _WtWebGraphAnalog57662HorizontalZoom_Type()
)
wtWebGraphAnalog57662HorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662HorizontalZoom.setStatus("mandatory")
_WtWebGraphAnalog57662Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Alarm = _WtWebGraphAnalog57662Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5)
)


class _WtWebGraphAnalog57662AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57662AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57662AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662AlarmCount_Object = MibScalar
wtWebGraphAnalog57662AlarmCount = _WtWebGraphAnalog57662AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 1),
    _WtWebGraphAnalog57662AlarmCount_Type()
)
wtWebGraphAnalog57662AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmCount.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmIfTable_Object = MibTable
wtWebGraphAnalog57662AlarmIfTable = _WtWebGraphAnalog57662AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalog57662AlarmIfEntry = _WtWebGraphAnalog57662AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2, 1)
)
wtWebGraphAnalog57662AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalog57662AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57662AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662AlarmNo_Object = MibTableColumn
wtWebGraphAnalog57662AlarmNo = _WtWebGraphAnalog57662AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalog57662AlarmNo_Type()
)
wtWebGraphAnalog57662AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmNo.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmTable_Object = MibTable
wtWebGraphAnalog57662AlarmTable = _WtWebGraphAnalog57662AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTable.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmEntry_Object = MibTableRow
wtWebGraphAnalog57662AlarmEntry = _WtWebGraphAnalog57662AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1)
)
wtWebGraphAnalog57662AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalog57662AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTrigger = _WtWebGraphAnalog57662AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalog57662AlarmTrigger_Type()
)
wtWebGraphAnalog57662AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMin1_Type = OctetString
_WtWebGraphAnalog57662AlarmMin1_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMin1 = _WtWebGraphAnalog57662AlarmMin1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalog57662AlarmMin1_Type()
)
wtWebGraphAnalog57662AlarmMin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMin1.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMax1_Type = OctetString
_WtWebGraphAnalog57662AlarmMax1_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMax1 = _WtWebGraphAnalog57662AlarmMax1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalog57662AlarmMax1_Type()
)
wtWebGraphAnalog57662AlarmMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMax1.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmHysteresis1_Type = OctetString
_WtWebGraphAnalog57662AlarmHysteresis1_Object = MibTableColumn
wtWebGraphAnalog57662AlarmHysteresis1 = _WtWebGraphAnalog57662AlarmHysteresis1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalog57662AlarmHysteresis1_Type()
)
wtWebGraphAnalog57662AlarmHysteresis1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmHysteresis1.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmDelay_Type = OctetString
_WtWebGraphAnalog57662AlarmDelay_Object = MibTableColumn
wtWebGraphAnalog57662AlarmDelay = _WtWebGraphAnalog57662AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalog57662AlarmDelay_Type()
)
wtWebGraphAnalog57662AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmInterval_Type = OctetString
_WtWebGraphAnalog57662AlarmInterval_Object = MibTableColumn
wtWebGraphAnalog57662AlarmInterval = _WtWebGraphAnalog57662AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalog57662AlarmInterval_Type()
)
wtWebGraphAnalog57662AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662AlarmEnable_Object = MibTableColumn
wtWebGraphAnalog57662AlarmEnable = _WtWebGraphAnalog57662AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalog57662AlarmEnable_Type()
)
wtWebGraphAnalog57662AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalog57662AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalog57662AlarmEMailAddr = _WtWebGraphAnalog57662AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalog57662AlarmEMailAddr_Type()
)
wtWebGraphAnalog57662AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMailSubject_Type = OctetString
_WtWebGraphAnalog57662AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMailSubject = _WtWebGraphAnalog57662AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalog57662AlarmMailSubject_Type()
)
wtWebGraphAnalog57662AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMailText_Type = OctetString
_WtWebGraphAnalog57662AlarmMailText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMailText = _WtWebGraphAnalog57662AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalog57662AlarmMailText_Type()
)
wtWebGraphAnalog57662AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmManagerIP_Type = OctetString
_WtWebGraphAnalog57662AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalog57662AlarmManagerIP = _WtWebGraphAnalog57662AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalog57662AlarmManagerIP_Type()
)
wtWebGraphAnalog57662AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmTrapText_Type = OctetString
_WtWebGraphAnalog57662AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTrapText = _WtWebGraphAnalog57662AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalog57662AlarmTrapText_Type()
)
wtWebGraphAnalog57662AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalog57662AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMailOptions = _WtWebGraphAnalog57662AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalog57662AlarmMailOptions_Type()
)
wtWebGraphAnalog57662AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalog57662AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTcpIpAddr = _WtWebGraphAnalog57662AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalog57662AlarmTcpIpAddr_Type()
)
wtWebGraphAnalog57662AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTcpPort = _WtWebGraphAnalog57662AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalog57662AlarmTcpPort_Type()
)
wtWebGraphAnalog57662AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmTcpText_Type = OctetString
_WtWebGraphAnalog57662AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTcpText = _WtWebGraphAnalog57662AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalog57662AlarmTcpText_Type()
)
wtWebGraphAnalog57662AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalog57662AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalog57662AlarmClearMailSubject = _WtWebGraphAnalog57662AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalog57662AlarmClearMailSubject_Type()
)
wtWebGraphAnalog57662AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmClearMailText_Type = OctetString
_WtWebGraphAnalog57662AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmClearMailText = _WtWebGraphAnalog57662AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalog57662AlarmClearMailText_Type()
)
wtWebGraphAnalog57662AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalog57662AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmClearTrapText = _WtWebGraphAnalog57662AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalog57662AlarmClearTrapText_Type()
)
wtWebGraphAnalog57662AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalog57662AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmClearTcpText = _WtWebGraphAnalog57662AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalog57662AlarmClearTcpText_Type()
)
wtWebGraphAnalog57662AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMin2_Type = OctetString
_WtWebGraphAnalog57662AlarmMin2_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMin2 = _WtWebGraphAnalog57662AlarmMin2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalog57662AlarmMin2_Type()
)
wtWebGraphAnalog57662AlarmMin2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMin2.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmMax2_Type = OctetString
_WtWebGraphAnalog57662AlarmMax2_Object = MibTableColumn
wtWebGraphAnalog57662AlarmMax2 = _WtWebGraphAnalog57662AlarmMax2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalog57662AlarmMax2_Type()
)
wtWebGraphAnalog57662AlarmMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmMax2.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmHysteresis2_Type = OctetString
_WtWebGraphAnalog57662AlarmHysteresis2_Object = MibTableColumn
wtWebGraphAnalog57662AlarmHysteresis2 = _WtWebGraphAnalog57662AlarmHysteresis2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalog57662AlarmHysteresis2_Type()
)
wtWebGraphAnalog57662AlarmHysteresis2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmHysteresis2.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalog57662AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662AlarmSyslogIpAddr = _WtWebGraphAnalog57662AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalog57662AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalog57662AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalog57662AlarmSyslogPort = _WtWebGraphAnalog57662AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalog57662AlarmSyslogPort_Type()
)
wtWebGraphAnalog57662AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmSyslogText_Type = OctetString
_WtWebGraphAnalog57662AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmSyslogText = _WtWebGraphAnalog57662AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalog57662AlarmSyslogText_Type()
)
wtWebGraphAnalog57662AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalog57662AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmSyslogClearText = _WtWebGraphAnalog57662AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalog57662AlarmSyslogClearText_Type()
)
wtWebGraphAnalog57662AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalog57662AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalog57662AlarmFtpDataPort = _WtWebGraphAnalog57662AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalog57662AlarmFtpDataPort_Type()
)
wtWebGraphAnalog57662AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalog57662AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalog57662AlarmFtpFileName = _WtWebGraphAnalog57662AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalog57662AlarmFtpFileName_Type()
)
wtWebGraphAnalog57662AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmFtpText_Type = OctetString
_WtWebGraphAnalog57662AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmFtpText = _WtWebGraphAnalog57662AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalog57662AlarmFtpText_Type()
)
wtWebGraphAnalog57662AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalog57662AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalog57662AlarmFtpClearText = _WtWebGraphAnalog57662AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalog57662AlarmFtpClearText_Type()
)
wtWebGraphAnalog57662AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalog57662AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalog57662AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalog57662AlarmFtpOption = _WtWebGraphAnalog57662AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalog57662AlarmFtpOption_Type()
)
wtWebGraphAnalog57662AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalog57662AlarmTimerCron_Type = OctetString
_WtWebGraphAnalog57662AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalog57662AlarmTimerCron = _WtWebGraphAnalog57662AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalog57662AlarmTimerCron_Type()
)
wtWebGraphAnalog57662AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalog57662Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Graphics = _WtWebGraphAnalog57662Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6)
)
_WtWebGraphAnalog57662GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662GraphicsBase = _WtWebGraphAnalog57662GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1)
)
_WtWebGraphAnalog57662GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalog57662GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalog57662GraphicsBaseEnable = _WtWebGraphAnalog57662GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 1),
    _WtWebGraphAnalog57662GraphicsBaseEnable_Type()
)
wtWebGraphAnalog57662GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalog57662GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalog57662GraphicsBaseWidth = _WtWebGraphAnalog57662GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 2),
    _WtWebGraphAnalog57662GraphicsBaseWidth_Type()
)
wtWebGraphAnalog57662GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalog57662GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalog57662GraphicsBaseHeight = _WtWebGraphAnalog57662GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 3),
    _WtWebGraphAnalog57662GraphicsBaseHeight_Type()
)
wtWebGraphAnalog57662GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalog57662GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57662GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57662GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalog57662GraphicsBaseFrameColor = _WtWebGraphAnalog57662GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 4),
    _WtWebGraphAnalog57662GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalog57662GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalog57662GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57662GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57662GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalog57662GraphicsBaseBackgroundColor = _WtWebGraphAnalog57662GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 5),
    _WtWebGraphAnalog57662GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalog57662GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalog57662GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalog57662GraphicsBasePollingrate = _WtWebGraphAnalog57662GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 1, 6),
    _WtWebGraphAnalog57662GraphicsBasePollingrate_Type()
)
wtWebGraphAnalog57662GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662GraphicsSelect = _WtWebGraphAnalog57662GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2)
)


class _WtWebGraphAnalog57662GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel = _WtWebGraphAnalog57662GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 1),
    _WtWebGraphAnalog57662GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 2),
    _WtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalog57662SensorColor2Table_Object = MibTable
wtWebGraphAnalog57662SensorColor2Table = _WtWebGraphAnalog57662SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalog57662SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalog57662SensorColor2Entry = _WtWebGraphAnalog57662SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalog57662SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalog57662GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalog57662GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalog57662GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalog57662GraphicsSensorColor = _WtWebGraphAnalog57662GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalog57662GraphicsSensorColor_Type()
)
wtWebGraphAnalog57662GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalog57662GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalog57662GraphicsSelectScale = _WtWebGraphAnalog57662GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalog57662GraphicsSelectScale_Type()
)
wtWebGraphAnalog57662GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662GraphicsScale = _WtWebGraphAnalog57662GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3)
)
_WtWebGraphAnalog57662GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalog57662GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalog57662GraphicsScaleAutoScaleEnable = _WtWebGraphAnalog57662GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 1),
    _WtWebGraphAnalog57662GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalog57662GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalog57662GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalog57662GraphicsScaleAutoFitEnable = _WtWebGraphAnalog57662GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 2),
    _WtWebGraphAnalog57662GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalog57662GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalog57662GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale1Min = _WtWebGraphAnalog57662GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 3),
    _WtWebGraphAnalog57662GraphicsScale1Min_Type()
)
wtWebGraphAnalog57662GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalog57662GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale2Min = _WtWebGraphAnalog57662GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 4),
    _WtWebGraphAnalog57662GraphicsScale2Min_Type()
)
wtWebGraphAnalog57662GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalog57662GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale1Max = _WtWebGraphAnalog57662GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 7),
    _WtWebGraphAnalog57662GraphicsScale1Max_Type()
)
wtWebGraphAnalog57662GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalog57662GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale2Max = _WtWebGraphAnalog57662GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 8),
    _WtWebGraphAnalog57662GraphicsScale2Max_Type()
)
wtWebGraphAnalog57662GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalog57662GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale1Unit = _WtWebGraphAnalog57662GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 11),
    _WtWebGraphAnalog57662GraphicsScale1Unit_Type()
)
wtWebGraphAnalog57662GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalog57662GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalog57662GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalog57662GraphicsScale2Unit = _WtWebGraphAnalog57662GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 6, 3, 12),
    _WtWebGraphAnalog57662GraphicsScale2Unit_Type()
)
wtWebGraphAnalog57662GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalog57662Report_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Report = _WtWebGraphAnalog57662Report_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7)
)


class _WtWebGraphAnalog57662ReportCount_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalog57662ReportCount_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ReportCount_Object = MibScalar
wtWebGraphAnalog57662ReportCount = _WtWebGraphAnalog57662ReportCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 1),
    _WtWebGraphAnalog57662ReportCount_Type()
)
wtWebGraphAnalog57662ReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportCount.setStatus("mandatory")
_WtWebGraphAnalog57662ReportIfTable_Object = MibTable
wtWebGraphAnalog57662ReportIfTable = _WtWebGraphAnalog57662ReportIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportIfTable.setStatus("mandatory")
_WtWebGraphAnalog57662ReportIfEntry_Object = MibTableRow
wtWebGraphAnalog57662ReportIfEntry = _WtWebGraphAnalog57662ReportIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 2, 1)
)
wtWebGraphAnalog57662ReportIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662ReportNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportIfEntry.setStatus("mandatory")
_WtWebGraphAnalog57662ReportNo_Type = Integer32
_WtWebGraphAnalog57662ReportNo_Object = MibTableColumn
wtWebGraphAnalog57662ReportNo = _WtWebGraphAnalog57662ReportNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 2, 1, 1),
    _WtWebGraphAnalog57662ReportNo_Type()
)
wtWebGraphAnalog57662ReportNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportNo.setStatus("mandatory")
_WtWebGraphAnalog57662ReportTable_Object = MibTable
wtWebGraphAnalog57662ReportTable = _WtWebGraphAnalog57662ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTable.setStatus("mandatory")
_WtWebGraphAnalog57662ReportEntry_Object = MibTableRow
wtWebGraphAnalog57662ReportEntry = _WtWebGraphAnalog57662ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1)
)
wtWebGraphAnalog57662ReportEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662ReportNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportEntry.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662ReportEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662ReportEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662ReportEnable_Object = MibTableColumn
wtWebGraphAnalog57662ReportEnable = _WtWebGraphAnalog57662ReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 1),
    _WtWebGraphAnalog57662ReportEnable_Type()
)
wtWebGraphAnalog57662ReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportEnable.setStatus("mandatory")
_WtWebGraphAnalog57662ReportTimerCron_Type = OctetString
_WtWebGraphAnalog57662ReportTimerCron_Object = MibTableColumn
wtWebGraphAnalog57662ReportTimerCron = _WtWebGraphAnalog57662ReportTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 2),
    _WtWebGraphAnalog57662ReportTimerCron_Type()
)
wtWebGraphAnalog57662ReportTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTimerCron.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportMethodeEnable_Type(OctetString):
    """Custom type wtWebGraphAnalog57662ReportMethodeEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662ReportMethodeEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662ReportMethodeEnable_Object = MibTableColumn
wtWebGraphAnalog57662ReportMethodeEnable = _WtWebGraphAnalog57662ReportMethodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 3),
    _WtWebGraphAnalog57662ReportMethodeEnable_Type()
)
wtWebGraphAnalog57662ReportMethodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportMethodeEnable.setStatus("mandatory")
_WtWebGraphAnalog57662ReportEMailAddr_Type = OctetString
_WtWebGraphAnalog57662ReportEMailAddr_Object = MibTableColumn
wtWebGraphAnalog57662ReportEMailAddr = _WtWebGraphAnalog57662ReportEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 8),
    _WtWebGraphAnalog57662ReportEMailAddr_Type()
)
wtWebGraphAnalog57662ReportEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportEMailAddr.setStatus("mandatory")
_WtWebGraphAnalog57662ReportMailSubject_Type = OctetString
_WtWebGraphAnalog57662ReportMailSubject_Object = MibTableColumn
wtWebGraphAnalog57662ReportMailSubject = _WtWebGraphAnalog57662ReportMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 9),
    _WtWebGraphAnalog57662ReportMailSubject_Type()
)
wtWebGraphAnalog57662ReportMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57662ReportMailText_Type = OctetString
_WtWebGraphAnalog57662ReportMailText_Object = MibTableColumn
wtWebGraphAnalog57662ReportMailText = _WtWebGraphAnalog57662ReportMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 10),
    _WtWebGraphAnalog57662ReportMailText_Type()
)
wtWebGraphAnalog57662ReportMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportMailText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportManagerIP_Type = OctetString
_WtWebGraphAnalog57662ReportManagerIP_Object = MibTableColumn
wtWebGraphAnalog57662ReportManagerIP = _WtWebGraphAnalog57662ReportManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 11),
    _WtWebGraphAnalog57662ReportManagerIP_Type()
)
wtWebGraphAnalog57662ReportManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportManagerIP.setStatus("mandatory")
_WtWebGraphAnalog57662ReportTrapText_Type = OctetString
_WtWebGraphAnalog57662ReportTrapText_Object = MibTableColumn
wtWebGraphAnalog57662ReportTrapText = _WtWebGraphAnalog57662ReportTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 12),
    _WtWebGraphAnalog57662ReportTrapText_Type()
)
wtWebGraphAnalog57662ReportTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTrapText.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalog57662ReportMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662ReportMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662ReportMailOptions_Object = MibTableColumn
wtWebGraphAnalog57662ReportMailOptions = _WtWebGraphAnalog57662ReportMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 13),
    _WtWebGraphAnalog57662ReportMailOptions_Type()
)
wtWebGraphAnalog57662ReportMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportMailOptions.setStatus("mandatory")
_WtWebGraphAnalog57662ReportTcpIpAddr_Type = OctetString
_WtWebGraphAnalog57662ReportTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662ReportTcpIpAddr = _WtWebGraphAnalog57662ReportTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 14),
    _WtWebGraphAnalog57662ReportTcpIpAddr_Type()
)
wtWebGraphAnalog57662ReportTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ReportTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662ReportTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ReportTcpPort_Object = MibTableColumn
wtWebGraphAnalog57662ReportTcpPort = _WtWebGraphAnalog57662ReportTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 15),
    _WtWebGraphAnalog57662ReportTcpPort_Type()
)
wtWebGraphAnalog57662ReportTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTcpPort.setStatus("mandatory")
_WtWebGraphAnalog57662ReportTcpText_Type = OctetString
_WtWebGraphAnalog57662ReportTcpText_Object = MibTableColumn
wtWebGraphAnalog57662ReportTcpText = _WtWebGraphAnalog57662ReportTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 16),
    _WtWebGraphAnalog57662ReportTcpText_Type()
)
wtWebGraphAnalog57662ReportTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportTcpText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportClearMailSubject_Type = OctetString
_WtWebGraphAnalog57662ReportClearMailSubject_Object = MibTableColumn
wtWebGraphAnalog57662ReportClearMailSubject = _WtWebGraphAnalog57662ReportClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 17),
    _WtWebGraphAnalog57662ReportClearMailSubject_Type()
)
wtWebGraphAnalog57662ReportClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalog57662ReportClearMailText_Type = OctetString
_WtWebGraphAnalog57662ReportClearMailText_Object = MibTableColumn
wtWebGraphAnalog57662ReportClearMailText = _WtWebGraphAnalog57662ReportClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 18),
    _WtWebGraphAnalog57662ReportClearMailText_Type()
)
wtWebGraphAnalog57662ReportClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportClearMailText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportClearTrapText_Type = OctetString
_WtWebGraphAnalog57662ReportClearTrapText_Object = MibTableColumn
wtWebGraphAnalog57662ReportClearTrapText = _WtWebGraphAnalog57662ReportClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 19),
    _WtWebGraphAnalog57662ReportClearTrapText_Type()
)
wtWebGraphAnalog57662ReportClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportClearTrapText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportClearTcpText_Type = OctetString
_WtWebGraphAnalog57662ReportClearTcpText_Object = MibTableColumn
wtWebGraphAnalog57662ReportClearTcpText = _WtWebGraphAnalog57662ReportClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 20),
    _WtWebGraphAnalog57662ReportClearTcpText_Type()
)
wtWebGraphAnalog57662ReportClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportClearTcpText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportSyslogIpAddr_Type = OctetString
_WtWebGraphAnalog57662ReportSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalog57662ReportSyslogIpAddr = _WtWebGraphAnalog57662ReportSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 24),
    _WtWebGraphAnalog57662ReportSyslogIpAddr_Type()
)
wtWebGraphAnalog57662ReportSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalog57662ReportSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalog57662ReportSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalog57662ReportSyslogPort_Object = MibTableColumn
wtWebGraphAnalog57662ReportSyslogPort = _WtWebGraphAnalog57662ReportSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 25),
    _WtWebGraphAnalog57662ReportSyslogPort_Type()
)
wtWebGraphAnalog57662ReportSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportSyslogPort.setStatus("mandatory")
_WtWebGraphAnalog57662ReportSyslogText_Type = OctetString
_WtWebGraphAnalog57662ReportSyslogText_Object = MibTableColumn
wtWebGraphAnalog57662ReportSyslogText = _WtWebGraphAnalog57662ReportSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 26),
    _WtWebGraphAnalog57662ReportSyslogText_Type()
)
wtWebGraphAnalog57662ReportSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportSyslogText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportSyslogClearText_Type = OctetString
_WtWebGraphAnalog57662ReportSyslogClearText_Object = MibTableColumn
wtWebGraphAnalog57662ReportSyslogClearText = _WtWebGraphAnalog57662ReportSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 27),
    _WtWebGraphAnalog57662ReportSyslogClearText_Type()
)
wtWebGraphAnalog57662ReportSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportFtpDataPort_Type = OctetString
_WtWebGraphAnalog57662ReportFtpDataPort_Object = MibTableColumn
wtWebGraphAnalog57662ReportFtpDataPort = _WtWebGraphAnalog57662ReportFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 28),
    _WtWebGraphAnalog57662ReportFtpDataPort_Type()
)
wtWebGraphAnalog57662ReportFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalog57662ReportFtpFileName_Type = OctetString
_WtWebGraphAnalog57662ReportFtpFileName_Object = MibTableColumn
wtWebGraphAnalog57662ReportFtpFileName = _WtWebGraphAnalog57662ReportFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 29),
    _WtWebGraphAnalog57662ReportFtpFileName_Type()
)
wtWebGraphAnalog57662ReportFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportFtpFileName.setStatus("mandatory")
_WtWebGraphAnalog57662ReportFtpText_Type = OctetString
_WtWebGraphAnalog57662ReportFtpText_Object = MibTableColumn
wtWebGraphAnalog57662ReportFtpText = _WtWebGraphAnalog57662ReportFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 30),
    _WtWebGraphAnalog57662ReportFtpText_Type()
)
wtWebGraphAnalog57662ReportFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportFtpText.setStatus("mandatory")
_WtWebGraphAnalog57662ReportFtpClearText_Type = OctetString
_WtWebGraphAnalog57662ReportFtpClearText_Object = MibTableColumn
wtWebGraphAnalog57662ReportFtpClearText = _WtWebGraphAnalog57662ReportFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 31),
    _WtWebGraphAnalog57662ReportFtpClearText_Type()
)
wtWebGraphAnalog57662ReportFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalog57662ReportFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalog57662ReportFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662ReportFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662ReportFtpOption_Object = MibTableColumn
wtWebGraphAnalog57662ReportFtpOption = _WtWebGraphAnalog57662ReportFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 1, 7, 3, 1, 32),
    _WtWebGraphAnalog57662ReportFtpOption_Type()
)
wtWebGraphAnalog57662ReportFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662ReportFtpOption.setStatus("mandatory")
_WtWebGraphAnalog57662Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Ports = _WtWebGraphAnalog57662Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2)
)
_WtWebGraphAnalog57662PortTable_Object = MibTable
wtWebGraphAnalog57662PortTable = _WtWebGraphAnalog57662PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortTable.setStatus("mandatory")
_WtWebGraphAnalog57662PortEntry_Object = MibTableRow
wtWebGraphAnalog57662PortEntry = _WtWebGraphAnalog57662PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1)
)
wtWebGraphAnalog57662PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortEntry.setStatus("mandatory")
_WtWebGraphAnalog57662PortName_Type = OctetString
_WtWebGraphAnalog57662PortName_Object = MibTableColumn
wtWebGraphAnalog57662PortName = _WtWebGraphAnalog57662PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 1),
    _WtWebGraphAnalog57662PortName_Type()
)
wtWebGraphAnalog57662PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortName.setStatus("mandatory")
_WtWebGraphAnalog57662PortText_Type = OctetString
_WtWebGraphAnalog57662PortText_Object = MibTableColumn
wtWebGraphAnalog57662PortText = _WtWebGraphAnalog57662PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 2),
    _WtWebGraphAnalog57662PortText_Type()
)
wtWebGraphAnalog57662PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortText.setStatus("mandatory")
_WtWebGraphAnalog57662PortOffset1_Type = OctetString
_WtWebGraphAnalog57662PortOffset1_Object = MibTableColumn
wtWebGraphAnalog57662PortOffset1 = _WtWebGraphAnalog57662PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 3),
    _WtWebGraphAnalog57662PortOffset1_Type()
)
wtWebGraphAnalog57662PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortOffset1.setStatus("mandatory")
_WtWebGraphAnalog57662SetPoint1_Type = OctetString
_WtWebGraphAnalog57662SetPoint1_Object = MibTableColumn
wtWebGraphAnalog57662SetPoint1 = _WtWebGraphAnalog57662SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 4),
    _WtWebGraphAnalog57662SetPoint1_Type()
)
wtWebGraphAnalog57662SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SetPoint1.setStatus("mandatory")
_WtWebGraphAnalog57662PortOffset2_Type = OctetString
_WtWebGraphAnalog57662PortOffset2_Object = MibTableColumn
wtWebGraphAnalog57662PortOffset2 = _WtWebGraphAnalog57662PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 5),
    _WtWebGraphAnalog57662PortOffset2_Type()
)
wtWebGraphAnalog57662PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortOffset2.setStatus("mandatory")
_WtWebGraphAnalog57662SetPoint2_Type = OctetString
_WtWebGraphAnalog57662SetPoint2_Object = MibTableColumn
wtWebGraphAnalog57662SetPoint2 = _WtWebGraphAnalog57662SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 6),
    _WtWebGraphAnalog57662SetPoint2_Type()
)
wtWebGraphAnalog57662SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662SetPoint2.setStatus("mandatory")
_WtWebGraphAnalog57662PortComment_Type = OctetString
_WtWebGraphAnalog57662PortComment_Object = MibTableColumn
wtWebGraphAnalog57662PortComment = _WtWebGraphAnalog57662PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 7),
    _WtWebGraphAnalog57662PortComment_Type()
)
wtWebGraphAnalog57662PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortComment.setStatus("mandatory")


class _WtWebGraphAnalog57662PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalog57662PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalog57662PortSensorSelect = _WtWebGraphAnalog57662PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 8),
    _WtWebGraphAnalog57662PortSensorSelect_Type()
)
wtWebGraphAnalog57662PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalog57662PortUnit_Type = OctetString
_WtWebGraphAnalog57662PortUnit_Object = MibTableColumn
wtWebGraphAnalog57662PortUnit = _WtWebGraphAnalog57662PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 9),
    _WtWebGraphAnalog57662PortUnit_Type()
)
wtWebGraphAnalog57662PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortUnit.setStatus("mandatory")
_WtWebGraphAnalog57662PortScale0_Type = OctetString
_WtWebGraphAnalog57662PortScale0_Object = MibTableColumn
wtWebGraphAnalog57662PortScale0 = _WtWebGraphAnalog57662PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 10),
    _WtWebGraphAnalog57662PortScale0_Type()
)
wtWebGraphAnalog57662PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortScale0.setStatus("mandatory")
_WtWebGraphAnalog57662PortScale100_Type = OctetString
_WtWebGraphAnalog57662PortScale100_Object = MibTableColumn
wtWebGraphAnalog57662PortScale100 = _WtWebGraphAnalog57662PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 11),
    _WtWebGraphAnalog57662PortScale100_Type()
)
wtWebGraphAnalog57662PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortScale100.setStatus("mandatory")


class _WtWebGraphAnalog57662PortOutputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662PortOutputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662PortOutputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662PortOutputMode_Object = MibTableColumn
wtWebGraphAnalog57662PortOutputMode = _WtWebGraphAnalog57662PortOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 12),
    _WtWebGraphAnalog57662PortOutputMode_Type()
)
wtWebGraphAnalog57662PortOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortOutputMode.setStatus("mandatory")


class _WtWebGraphAnalog57662PortInputMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662PortInputMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662PortInputMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662PortInputMode_Object = MibTableColumn
wtWebGraphAnalog57662PortInputMode = _WtWebGraphAnalog57662PortInputMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 13),
    _WtWebGraphAnalog57662PortInputMode_Type()
)
wtWebGraphAnalog57662PortInputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortInputMode.setStatus("mandatory")
_WtWebGraphAnalog57662PortCompensationValue_Type = OctetString
_WtWebGraphAnalog57662PortCompensationValue_Object = MibTableColumn
wtWebGraphAnalog57662PortCompensationValue = _WtWebGraphAnalog57662PortCompensationValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 14),
    _WtWebGraphAnalog57662PortCompensationValue_Type()
)
wtWebGraphAnalog57662PortCompensationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortCompensationValue.setStatus("mandatory")


class _WtWebGraphAnalog57662PortCompensationMode_Type(OctetString):
    """Custom type wtWebGraphAnalog57662PortCompensationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalog57662PortCompensationMode_Type.__name__ = "OctetString"
_WtWebGraphAnalog57662PortCompensationMode_Object = MibTableColumn
wtWebGraphAnalog57662PortCompensationMode = _WtWebGraphAnalog57662PortCompensationMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 2, 1, 1, 15),
    _WtWebGraphAnalog57662PortCompensationMode_Type()
)
wtWebGraphAnalog57662PortCompensationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662PortCompensationMode.setStatus("mandatory")
_WtWebGraphAnalog57662Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Manufact = _WtWebGraphAnalog57662Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3)
)
_WtWebGraphAnalog57662MfName_Type = OctetString
_WtWebGraphAnalog57662MfName_Object = MibScalar
wtWebGraphAnalog57662MfName = _WtWebGraphAnalog57662MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 1),
    _WtWebGraphAnalog57662MfName_Type()
)
wtWebGraphAnalog57662MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfName.setStatus("mandatory")
_WtWebGraphAnalog57662MfAddr_Type = OctetString
_WtWebGraphAnalog57662MfAddr_Object = MibScalar
wtWebGraphAnalog57662MfAddr = _WtWebGraphAnalog57662MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 2),
    _WtWebGraphAnalog57662MfAddr_Type()
)
wtWebGraphAnalog57662MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfAddr.setStatus("mandatory")
_WtWebGraphAnalog57662MfHotline_Type = OctetString
_WtWebGraphAnalog57662MfHotline_Object = MibScalar
wtWebGraphAnalog57662MfHotline = _WtWebGraphAnalog57662MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 3),
    _WtWebGraphAnalog57662MfHotline_Type()
)
wtWebGraphAnalog57662MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfHotline.setStatus("mandatory")
_WtWebGraphAnalog57662MfInternet_Type = OctetString
_WtWebGraphAnalog57662MfInternet_Object = MibScalar
wtWebGraphAnalog57662MfInternet = _WtWebGraphAnalog57662MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 4),
    _WtWebGraphAnalog57662MfInternet_Type()
)
wtWebGraphAnalog57662MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfInternet.setStatus("mandatory")
_WtWebGraphAnalog57662MfDeviceTyp_Type = OctetString
_WtWebGraphAnalog57662MfDeviceTyp_Object = MibScalar
wtWebGraphAnalog57662MfDeviceTyp = _WtWebGraphAnalog57662MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 5),
    _WtWebGraphAnalog57662MfDeviceTyp_Type()
)
wtWebGraphAnalog57662MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalog57662MfOrderNo_Type = OctetString
_WtWebGraphAnalog57662MfOrderNo_Object = MibScalar
wtWebGraphAnalog57662MfOrderNo = _WtWebGraphAnalog57662MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 3, 3, 6),
    _WtWebGraphAnalog57662MfOrderNo_Type()
)
wtWebGraphAnalog57662MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalog57662Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalog57662Diag = _WtWebGraphAnalog57662Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4)
)
_WtWebGraphAnalog57662DiagErrorCount_Type = Integer32
_WtWebGraphAnalog57662DiagErrorCount_Object = MibScalar
wtWebGraphAnalog57662DiagErrorCount = _WtWebGraphAnalog57662DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 1),
    _WtWebGraphAnalog57662DiagErrorCount_Type()
)
wtWebGraphAnalog57662DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalog57662DiagBinaryError_Type = OctetString
_WtWebGraphAnalog57662DiagBinaryError_Object = MibScalar
wtWebGraphAnalog57662DiagBinaryError = _WtWebGraphAnalog57662DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 2),
    _WtWebGraphAnalog57662DiagBinaryError_Type()
)
wtWebGraphAnalog57662DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalog57662DiagErrorIndex_Type = Integer32
_WtWebGraphAnalog57662DiagErrorIndex_Object = MibScalar
wtWebGraphAnalog57662DiagErrorIndex = _WtWebGraphAnalog57662DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 3),
    _WtWebGraphAnalog57662DiagErrorIndex_Type()
)
wtWebGraphAnalog57662DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalog57662DiagErrorMessage_Type = OctetString
_WtWebGraphAnalog57662DiagErrorMessage_Object = MibScalar
wtWebGraphAnalog57662DiagErrorMessage = _WtWebGraphAnalog57662DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 4),
    _WtWebGraphAnalog57662DiagErrorMessage_Type()
)
wtWebGraphAnalog57662DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalog57662DiagErrorClear_Type = Integer32
_WtWebGraphAnalog57662DiagErrorClear_Object = MibScalar
wtWebGraphAnalog57662DiagErrorClear = _WtWebGraphAnalog57662DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 4, 5),
    _WtWebGraphAnalog57662DiagErrorClear_Type()
)
wtWebGraphAnalog57662DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalog57662Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 31)
)
wtWebGraphAnalog57662Alert1.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert1.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 32)
)
wtWebGraphAnalog57662Alert2.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert2.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 33)
)
wtWebGraphAnalog57662Alert3.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert3.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 34)
)
wtWebGraphAnalog57662Alert4.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert4.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 35)
)
wtWebGraphAnalog57662Alert5.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert5.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 36)
)
wtWebGraphAnalog57662Alert6.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert6.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 37)
)
wtWebGraphAnalog57662Alert7.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert7.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 38)
)
wtWebGraphAnalog57662Alert8.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert8.setStatus(
        ""
    )

wtWebGraphAnalog57662AlertReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 39)
)
wtWebGraphAnalog57662AlertReport.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlertReport.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 91)
)
wtWebGraphAnalog57662Alert9.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert9.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 92)
)
wtWebGraphAnalog57662Alert10.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert10.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 93)
)
wtWebGraphAnalog57662Alert11.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert11.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 94)
)
wtWebGraphAnalog57662Alert12.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert12.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 95)
)
wtWebGraphAnalog57662Alert13.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert13.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 96)
)
wtWebGraphAnalog57662Alert14.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert14.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 97)
)
wtWebGraphAnalog57662Alert15.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert15.setStatus(
        ""
    )

wtWebGraphAnalog57662Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 98)
)
wtWebGraphAnalog57662Alert16.setObjects(
    ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662Alert16.setStatus(
        ""
    )

wtWebGraphAnalog57662AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 29, 0, 110)
)
wtWebGraphAnalog57662AlertDiag.setObjects(
      *(("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662DiagErrorIndex"),
        ("WebGraph-AnalogIO-57662-US-MIB", "wtWebGraphAnalog57662DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalog57662AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIO-57662-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalog57662": wtWebGraphAnalog57662,
       "wtWebGraphAnalog57662Alert1": wtWebGraphAnalog57662Alert1,
       "wtWebGraphAnalog57662Alert2": wtWebGraphAnalog57662Alert2,
       "wtWebGraphAnalog57662Alert3": wtWebGraphAnalog57662Alert3,
       "wtWebGraphAnalog57662Alert4": wtWebGraphAnalog57662Alert4,
       "wtWebGraphAnalog57662Alert5": wtWebGraphAnalog57662Alert5,
       "wtWebGraphAnalog57662Alert6": wtWebGraphAnalog57662Alert6,
       "wtWebGraphAnalog57662Alert7": wtWebGraphAnalog57662Alert7,
       "wtWebGraphAnalog57662Alert8": wtWebGraphAnalog57662Alert8,
       "wtWebGraphAnalog57662AlertReport": wtWebGraphAnalog57662AlertReport,
       "wtWebGraphAnalog57662Alert9": wtWebGraphAnalog57662Alert9,
       "wtWebGraphAnalog57662Alert10": wtWebGraphAnalog57662Alert10,
       "wtWebGraphAnalog57662Alert11": wtWebGraphAnalog57662Alert11,
       "wtWebGraphAnalog57662Alert12": wtWebGraphAnalog57662Alert12,
       "wtWebGraphAnalog57662Alert13": wtWebGraphAnalog57662Alert13,
       "wtWebGraphAnalog57662Alert14": wtWebGraphAnalog57662Alert14,
       "wtWebGraphAnalog57662Alert15": wtWebGraphAnalog57662Alert15,
       "wtWebGraphAnalog57662Alert16": wtWebGraphAnalog57662Alert16,
       "wtWebGraphAnalog57662AlertDiag": wtWebGraphAnalog57662AlertDiag,
       "wtWebGraphAnalog57662Inventory": wtWebGraphAnalog57662Inventory,
       "wtWebGraphAnalog57662Sensors": wtWebGraphAnalog57662Sensors,
       "wtWebGraphAnalog57662SensorTable": wtWebGraphAnalog57662SensorTable,
       "wtWebGraphAnalog57662SensorEntry": wtWebGraphAnalog57662SensorEntry,
       "wtWebGraphAnalog57662SensorNo": wtWebGraphAnalog57662SensorNo,
       "wtWebGraphAnalog57662ValuesTable": wtWebGraphAnalog57662ValuesTable,
       "wtWebGraphAnalog57662ValuesEntry": wtWebGraphAnalog57662ValuesEntry,
       "wtWebGraphAnalog57662Values": wtWebGraphAnalog57662Values,
       "wtWebGraphAnalog57662BinaryValuesTable": wtWebGraphAnalog57662BinaryValuesTable,
       "wtWebGraphAnalog57662BinaryValuesEntry": wtWebGraphAnalog57662BinaryValuesEntry,
       "wtWebGraphAnalog57662BinaryValues": wtWebGraphAnalog57662BinaryValues,
       "wtWebGraphAnalog57662SessCntrl": wtWebGraphAnalog57662SessCntrl,
       "wtWebGraphAnalog57662SessCntrlPassword": wtWebGraphAnalog57662SessCntrlPassword,
       "wtWebGraphAnalog57662SessCntrlConfigMode": wtWebGraphAnalog57662SessCntrlConfigMode,
       "wtWebGraphAnalog57662SessCntrlLogout": wtWebGraphAnalog57662SessCntrlLogout,
       "wtWebGraphAnalog57662SessCntrlAdminPassword": wtWebGraphAnalog57662SessCntrlAdminPassword,
       "wtWebGraphAnalog57662SessCntrlConfigPassword": wtWebGraphAnalog57662SessCntrlConfigPassword,
       "wtWebGraphAnalog57662Config": wtWebGraphAnalog57662Config,
       "wtWebGraphAnalog57662Device": wtWebGraphAnalog57662Device,
       "wtWebGraphAnalog57662Text": wtWebGraphAnalog57662Text,
       "wtWebGraphAnalog57662DeviceName": wtWebGraphAnalog57662DeviceName,
       "wtWebGraphAnalog57662DeviceText": wtWebGraphAnalog57662DeviceText,
       "wtWebGraphAnalog57662DeviceLocation": wtWebGraphAnalog57662DeviceLocation,
       "wtWebGraphAnalog57662DeviceContact": wtWebGraphAnalog57662DeviceContact,
       "wtWebGraphAnalog57662TimeDate": wtWebGraphAnalog57662TimeDate,
       "wtWebGraphAnalog57662TimeZone": wtWebGraphAnalog57662TimeZone,
       "wtWebGraphAnalog57662TzOffsetHrs": wtWebGraphAnalog57662TzOffsetHrs,
       "wtWebGraphAnalog57662TzOffsetMin": wtWebGraphAnalog57662TzOffsetMin,
       "wtWebGraphAnalog57662TzEnable": wtWebGraphAnalog57662TzEnable,
       "wtWebGraphAnalog57662StTzOffsetHrs": wtWebGraphAnalog57662StTzOffsetHrs,
       "wtWebGraphAnalog57662StTzOffsetMin": wtWebGraphAnalog57662StTzOffsetMin,
       "wtWebGraphAnalog57662StTzEnable": wtWebGraphAnalog57662StTzEnable,
       "wtWebGraphAnalog57662StTzStartMonth": wtWebGraphAnalog57662StTzStartMonth,
       "wtWebGraphAnalog57662StTzStartMode": wtWebGraphAnalog57662StTzStartMode,
       "wtWebGraphAnalog57662StTzStartWday": wtWebGraphAnalog57662StTzStartWday,
       "wtWebGraphAnalog57662StTzStartHrs": wtWebGraphAnalog57662StTzStartHrs,
       "wtWebGraphAnalog57662StTzStartMin": wtWebGraphAnalog57662StTzStartMin,
       "wtWebGraphAnalog57662StTzStopMonth": wtWebGraphAnalog57662StTzStopMonth,
       "wtWebGraphAnalog57662StTzStopMode": wtWebGraphAnalog57662StTzStopMode,
       "wtWebGraphAnalog57662StTzStopWday": wtWebGraphAnalog57662StTzStopWday,
       "wtWebGraphAnalog57662StTzStopHrs": wtWebGraphAnalog57662StTzStopHrs,
       "wtWebGraphAnalog57662StTzStopMin": wtWebGraphAnalog57662StTzStopMin,
       "wtWebGraphAnalog57662TimeServer": wtWebGraphAnalog57662TimeServer,
       "wtWebGraphAnalog57662TimeServer1": wtWebGraphAnalog57662TimeServer1,
       "wtWebGraphAnalog57662TimeServer2": wtWebGraphAnalog57662TimeServer2,
       "wtWebGraphAnalog57662TsEnable": wtWebGraphAnalog57662TsEnable,
       "wtWebGraphAnalog57662TsSyncTime": wtWebGraphAnalog57662TsSyncTime,
       "wtWebGraphAnalog57662DeviceClock": wtWebGraphAnalog57662DeviceClock,
       "wtWebGraphAnalog57662ClockHrs": wtWebGraphAnalog57662ClockHrs,
       "wtWebGraphAnalog57662ClockMin": wtWebGraphAnalog57662ClockMin,
       "wtWebGraphAnalog57662ClockDay": wtWebGraphAnalog57662ClockDay,
       "wtWebGraphAnalog57662ClockMonth": wtWebGraphAnalog57662ClockMonth,
       "wtWebGraphAnalog57662ClockYear": wtWebGraphAnalog57662ClockYear,
       "wtWebGraphAnalog57662Basic": wtWebGraphAnalog57662Basic,
       "wtWebGraphAnalog57662Network": wtWebGraphAnalog57662Network,
       "wtWebGraphAnalog57662IpAddress": wtWebGraphAnalog57662IpAddress,
       "wtWebGraphAnalog57662SubnetMask": wtWebGraphAnalog57662SubnetMask,
       "wtWebGraphAnalog57662Gateway": wtWebGraphAnalog57662Gateway,
       "wtWebGraphAnalog57662DnsServer1": wtWebGraphAnalog57662DnsServer1,
       "wtWebGraphAnalog57662DnsServer2": wtWebGraphAnalog57662DnsServer2,
       "wtWebGraphAnalog57662AddConfig": wtWebGraphAnalog57662AddConfig,
       "wtWebGraphAnalog57662HTTP": wtWebGraphAnalog57662HTTP,
       "wtWebGraphAnalog57662Startup": wtWebGraphAnalog57662Startup,
       "wtWebGraphAnalog57662GetHeaderEnable": wtWebGraphAnalog57662GetHeaderEnable,
       "wtWebGraphAnalog57662HttpPort": wtWebGraphAnalog57662HttpPort,
       "wtWebGraphAnalog57662Mail": wtWebGraphAnalog57662Mail,
       "wtWebGraphAnalog57662MailAdName": wtWebGraphAnalog57662MailAdName,
       "wtWebGraphAnalog57662MailReply": wtWebGraphAnalog57662MailReply,
       "wtWebGraphAnalog57662MailServer": wtWebGraphAnalog57662MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalog57662MailAuthentication": wtWebGraphAnalog57662MailAuthentication,
       "wtWebGraphAnalog57662MailAuthUser": wtWebGraphAnalog57662MailAuthUser,
       "wtWebGraphAnalog57662MailAuthPassword": wtWebGraphAnalog57662MailAuthPassword,
       "wtWebGraphAnalog57662MailPop3Server": wtWebGraphAnalog57662MailPop3Server,
       "wtWebGraphAnalog57662SNMP": wtWebGraphAnalog57662SNMP,
       "wtWebGraphAnalog57662SnmpCommunityStringRead": wtWebGraphAnalog57662SnmpCommunityStringRead,
       "wtWebGraphAnalog57662SnmpCommunityStringReadWrite": wtWebGraphAnalog57662SnmpCommunityStringReadWrite,
       "wtWebGraphAnalog57662SystemTrapManagerIP": wtWebGraphAnalog57662SystemTrapManagerIP,
       "wtWebGraphAnalog57662SystemTrapEnable": wtWebGraphAnalog57662SystemTrapEnable,
       "wtWebGraphAnalog57662SnmpEnable": wtWebGraphAnalog57662SnmpEnable,
       "wtWebGraphAnalog57662SnmpCommunityStringTrap": wtWebGraphAnalog57662SnmpCommunityStringTrap,
       "wtWebGraphAnalog57662UDP": wtWebGraphAnalog57662UDP,
       "wtWebGraphAnalog57662UdpPort": wtWebGraphAnalog57662UdpPort,
       "wtWebGraphAnalog57662UdpEnable": wtWebGraphAnalog57662UdpEnable,
       "wtWebGraphAnalog57662Syslog": wtWebGraphAnalog57662Syslog,
       "wtWebGraphAnalog57662SyslogServerIP": wtWebGraphAnalog57662SyslogServerIP,
       "wtWebGraphAnalog57662SyslogServerPort": wtWebGraphAnalog57662SyslogServerPort,
       "wtWebGraphAnalog57662SyslogSystemMessagesEnable": wtWebGraphAnalog57662SyslogSystemMessagesEnable,
       "wtWebGraphAnalog57662SyslogEnable": wtWebGraphAnalog57662SyslogEnable,
       "wtWebGraphAnalog57662FTP": wtWebGraphAnalog57662FTP,
       "wtWebGraphAnalog57662FTPServerIP": wtWebGraphAnalog57662FTPServerIP,
       "wtWebGraphAnalog57662FTPServerControlPort": wtWebGraphAnalog57662FTPServerControlPort,
       "wtWebGraphAnalog57662FTPUserName": wtWebGraphAnalog57662FTPUserName,
       "wtWebGraphAnalog57662FTPPassword": wtWebGraphAnalog57662FTPPassword,
       "wtWebGraphAnalog57662FTPAccount": wtWebGraphAnalog57662FTPAccount,
       "wtWebGraphAnalog57662FTPOption": wtWebGraphAnalog57662FTPOption,
       "wtWebGraphAnalog57662FTPEnable": wtWebGraphAnalog57662FTPEnable,
       "wtWebGraphAnalog57662Language": wtWebGraphAnalog57662Language,
       "wtWebGraphAnalog57662LanguageSelect": wtWebGraphAnalog57662LanguageSelect,
       "wtWebGraphAnalog57662Binary": wtWebGraphAnalog57662Binary,
       "wtWebGraphAnalog57662BinaryModeCount": wtWebGraphAnalog57662BinaryModeCount,
       "wtWebGraphAnalog57662BinaryIfTable": wtWebGraphAnalog57662BinaryIfTable,
       "wtWebGraphAnalog57662BinaryIfEntry": wtWebGraphAnalog57662BinaryIfEntry,
       "wtWebGraphAnalog57662BinaryModeNo": wtWebGraphAnalog57662BinaryModeNo,
       "wtWebGraphAnalog57662BinaryTable": wtWebGraphAnalog57662BinaryTable,
       "wtWebGraphAnalog57662BinaryEntry": wtWebGraphAnalog57662BinaryEntry,
       "wtWebGraphAnalog57662BinaryOperationMode": wtWebGraphAnalog57662BinaryOperationMode,
       "wtWebGraphAnalog57662BinaryTcpServerLocalPort": wtWebGraphAnalog57662BinaryTcpServerLocalPort,
       "wtWebGraphAnalog57662BinaryTcpServerInputTrigger": wtWebGraphAnalog57662BinaryTcpServerInputTrigger,
       "wtWebGraphAnalog57662BinaryTcpServerApplicationMode": wtWebGraphAnalog57662BinaryTcpServerApplicationMode,
       "wtWebGraphAnalog57662BinaryTcpClientLocalPort": wtWebGraphAnalog57662BinaryTcpClientLocalPort,
       "wtWebGraphAnalog57662BinaryTcpClientServerPort": wtWebGraphAnalog57662BinaryTcpClientServerPort,
       "wtWebGraphAnalog57662BinaryTcpClientServerIpAddr": wtWebGraphAnalog57662BinaryTcpClientServerIpAddr,
       "wtWebGraphAnalog57662BinaryTcpClientServerPassword": wtWebGraphAnalog57662BinaryTcpClientServerPassword,
       "wtWebGraphAnalog57662BinaryTcpClientInactivity": wtWebGraphAnalog57662BinaryTcpClientInactivity,
       "wtWebGraphAnalog57662BinaryTcpClientInputTrigger": wtWebGraphAnalog57662BinaryTcpClientInputTrigger,
       "wtWebGraphAnalog57662BinaryTcpClientInterval": wtWebGraphAnalog57662BinaryTcpClientInterval,
       "wtWebGraphAnalog57662BinaryTcpClientApplicationMode": wtWebGraphAnalog57662BinaryTcpClientApplicationMode,
       "wtWebGraphAnalog57662BinaryUdpPeerLocalPort": wtWebGraphAnalog57662BinaryUdpPeerLocalPort,
       "wtWebGraphAnalog57662BinaryUdpPeerRemotePort": wtWebGraphAnalog57662BinaryUdpPeerRemotePort,
       "wtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr": wtWebGraphAnalog57662BinaryUdpPeerRemoteIpAddr,
       "wtWebGraphAnalog57662BinaryUdpPeerInputTrigger": wtWebGraphAnalog57662BinaryUdpPeerInputTrigger,
       "wtWebGraphAnalog57662BinaryUdpPeerInterval": wtWebGraphAnalog57662BinaryUdpPeerInterval,
       "wtWebGraphAnalog57662BinaryUdpPeerApplicationMode": wtWebGraphAnalog57662BinaryUdpPeerApplicationMode,
       "wtWebGraphAnalog57662BinaryConnectedPort": wtWebGraphAnalog57662BinaryConnectedPort,
       "wtWebGraphAnalog57662BinaryConnectedIpAddr": wtWebGraphAnalog57662BinaryConnectedIpAddr,
       "wtWebGraphAnalog57662BinaryTcpServerClientHttpPort": wtWebGraphAnalog57662BinaryTcpServerClientHttpPort,
       "wtWebGraphAnalog57662BinaryTcpClientServerHttpPort": wtWebGraphAnalog57662BinaryTcpClientServerHttpPort,
       "wtWebGraphAnalog57662BinaryTcpServerHysteresis1": wtWebGraphAnalog57662BinaryTcpServerHysteresis1,
       "wtWebGraphAnalog57662BinaryTcpServerHysteresis2": wtWebGraphAnalog57662BinaryTcpServerHysteresis2,
       "wtWebGraphAnalog57662BinaryTcpClientHysteresis1": wtWebGraphAnalog57662BinaryTcpClientHysteresis1,
       "wtWebGraphAnalog57662BinaryTcpClientHysteresis2": wtWebGraphAnalog57662BinaryTcpClientHysteresis2,
       "wtWebGraphAnalog57662BinaryUdpPeerHysteresis1": wtWebGraphAnalog57662BinaryUdpPeerHysteresis1,
       "wtWebGraphAnalog57662BinaryUdpPeerHysteresis2": wtWebGraphAnalog57662BinaryUdpPeerHysteresis2,
       "wtWebGraphAnalog57662Datalogger": wtWebGraphAnalog57662Datalogger,
       "wtWebGraphAnalog57662LoggerTimebase": wtWebGraphAnalog57662LoggerTimebase,
       "wtWebGraphAnalog57662LoggerSensorSel": wtWebGraphAnalog57662LoggerSensorSel,
       "wtWebGraphAnalog57662DisplaySensorSel": wtWebGraphAnalog57662DisplaySensorSel,
       "wtWebGraphAnalog57662SensorColorTable": wtWebGraphAnalog57662SensorColorTable,
       "wtWebGraphAnalog57662SensorColorEntry": wtWebGraphAnalog57662SensorColorEntry,
       "wtWebGraphAnalog57662SensorColor": wtWebGraphAnalog57662SensorColor,
       "wtWebGraphAnalog57662AutoScaleEnable": wtWebGraphAnalog57662AutoScaleEnable,
       "wtWebGraphAnalog57662VerticalUpperLimit": wtWebGraphAnalog57662VerticalUpperLimit,
       "wtWebGraphAnalog57662VerticalLowerLimit": wtWebGraphAnalog57662VerticalLowerLimit,
       "wtWebGraphAnalog57662HorizontalZoom": wtWebGraphAnalog57662HorizontalZoom,
       "wtWebGraphAnalog57662Alarm": wtWebGraphAnalog57662Alarm,
       "wtWebGraphAnalog57662AlarmCount": wtWebGraphAnalog57662AlarmCount,
       "wtWebGraphAnalog57662AlarmIfTable": wtWebGraphAnalog57662AlarmIfTable,
       "wtWebGraphAnalog57662AlarmIfEntry": wtWebGraphAnalog57662AlarmIfEntry,
       "wtWebGraphAnalog57662AlarmNo": wtWebGraphAnalog57662AlarmNo,
       "wtWebGraphAnalog57662AlarmTable": wtWebGraphAnalog57662AlarmTable,
       "wtWebGraphAnalog57662AlarmEntry": wtWebGraphAnalog57662AlarmEntry,
       "wtWebGraphAnalog57662AlarmTrigger": wtWebGraphAnalog57662AlarmTrigger,
       "wtWebGraphAnalog57662AlarmMin1": wtWebGraphAnalog57662AlarmMin1,
       "wtWebGraphAnalog57662AlarmMax1": wtWebGraphAnalog57662AlarmMax1,
       "wtWebGraphAnalog57662AlarmHysteresis1": wtWebGraphAnalog57662AlarmHysteresis1,
       "wtWebGraphAnalog57662AlarmDelay": wtWebGraphAnalog57662AlarmDelay,
       "wtWebGraphAnalog57662AlarmInterval": wtWebGraphAnalog57662AlarmInterval,
       "wtWebGraphAnalog57662AlarmEnable": wtWebGraphAnalog57662AlarmEnable,
       "wtWebGraphAnalog57662AlarmEMailAddr": wtWebGraphAnalog57662AlarmEMailAddr,
       "wtWebGraphAnalog57662AlarmMailSubject": wtWebGraphAnalog57662AlarmMailSubject,
       "wtWebGraphAnalog57662AlarmMailText": wtWebGraphAnalog57662AlarmMailText,
       "wtWebGraphAnalog57662AlarmManagerIP": wtWebGraphAnalog57662AlarmManagerIP,
       "wtWebGraphAnalog57662AlarmTrapText": wtWebGraphAnalog57662AlarmTrapText,
       "wtWebGraphAnalog57662AlarmMailOptions": wtWebGraphAnalog57662AlarmMailOptions,
       "wtWebGraphAnalog57662AlarmTcpIpAddr": wtWebGraphAnalog57662AlarmTcpIpAddr,
       "wtWebGraphAnalog57662AlarmTcpPort": wtWebGraphAnalog57662AlarmTcpPort,
       "wtWebGraphAnalog57662AlarmTcpText": wtWebGraphAnalog57662AlarmTcpText,
       "wtWebGraphAnalog57662AlarmClearMailSubject": wtWebGraphAnalog57662AlarmClearMailSubject,
       "wtWebGraphAnalog57662AlarmClearMailText": wtWebGraphAnalog57662AlarmClearMailText,
       "wtWebGraphAnalog57662AlarmClearTrapText": wtWebGraphAnalog57662AlarmClearTrapText,
       "wtWebGraphAnalog57662AlarmClearTcpText": wtWebGraphAnalog57662AlarmClearTcpText,
       "wtWebGraphAnalog57662AlarmMin2": wtWebGraphAnalog57662AlarmMin2,
       "wtWebGraphAnalog57662AlarmMax2": wtWebGraphAnalog57662AlarmMax2,
       "wtWebGraphAnalog57662AlarmHysteresis2": wtWebGraphAnalog57662AlarmHysteresis2,
       "wtWebGraphAnalog57662AlarmSyslogIpAddr": wtWebGraphAnalog57662AlarmSyslogIpAddr,
       "wtWebGraphAnalog57662AlarmSyslogPort": wtWebGraphAnalog57662AlarmSyslogPort,
       "wtWebGraphAnalog57662AlarmSyslogText": wtWebGraphAnalog57662AlarmSyslogText,
       "wtWebGraphAnalog57662AlarmSyslogClearText": wtWebGraphAnalog57662AlarmSyslogClearText,
       "wtWebGraphAnalog57662AlarmFtpDataPort": wtWebGraphAnalog57662AlarmFtpDataPort,
       "wtWebGraphAnalog57662AlarmFtpFileName": wtWebGraphAnalog57662AlarmFtpFileName,
       "wtWebGraphAnalog57662AlarmFtpText": wtWebGraphAnalog57662AlarmFtpText,
       "wtWebGraphAnalog57662AlarmFtpClearText": wtWebGraphAnalog57662AlarmFtpClearText,
       "wtWebGraphAnalog57662AlarmFtpOption": wtWebGraphAnalog57662AlarmFtpOption,
       "wtWebGraphAnalog57662AlarmTimerCron": wtWebGraphAnalog57662AlarmTimerCron,
       "wtWebGraphAnalog57662Graphics": wtWebGraphAnalog57662Graphics,
       "wtWebGraphAnalog57662GraphicsBase": wtWebGraphAnalog57662GraphicsBase,
       "wtWebGraphAnalog57662GraphicsBaseEnable": wtWebGraphAnalog57662GraphicsBaseEnable,
       "wtWebGraphAnalog57662GraphicsBaseWidth": wtWebGraphAnalog57662GraphicsBaseWidth,
       "wtWebGraphAnalog57662GraphicsBaseHeight": wtWebGraphAnalog57662GraphicsBaseHeight,
       "wtWebGraphAnalog57662GraphicsBaseFrameColor": wtWebGraphAnalog57662GraphicsBaseFrameColor,
       "wtWebGraphAnalog57662GraphicsBaseBackgroundColor": wtWebGraphAnalog57662GraphicsBaseBackgroundColor,
       "wtWebGraphAnalog57662GraphicsBasePollingrate": wtWebGraphAnalog57662GraphicsBasePollingrate,
       "wtWebGraphAnalog57662GraphicsSelect": wtWebGraphAnalog57662GraphicsSelect,
       "wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel": wtWebGraphAnalog57662GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem": wtWebGraphAnalog57662GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalog57662SensorColor2Table": wtWebGraphAnalog57662SensorColor2Table,
       "wtWebGraphAnalog57662SensorColor2Entry": wtWebGraphAnalog57662SensorColor2Entry,
       "wtWebGraphAnalog57662GraphicsSensorColor": wtWebGraphAnalog57662GraphicsSensorColor,
       "wtWebGraphAnalog57662GraphicsSelectScale": wtWebGraphAnalog57662GraphicsSelectScale,
       "wtWebGraphAnalog57662GraphicsScale": wtWebGraphAnalog57662GraphicsScale,
       "wtWebGraphAnalog57662GraphicsScaleAutoScaleEnable": wtWebGraphAnalog57662GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalog57662GraphicsScaleAutoFitEnable": wtWebGraphAnalog57662GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalog57662GraphicsScale1Min": wtWebGraphAnalog57662GraphicsScale1Min,
       "wtWebGraphAnalog57662GraphicsScale2Min": wtWebGraphAnalog57662GraphicsScale2Min,
       "wtWebGraphAnalog57662GraphicsScale1Max": wtWebGraphAnalog57662GraphicsScale1Max,
       "wtWebGraphAnalog57662GraphicsScale2Max": wtWebGraphAnalog57662GraphicsScale2Max,
       "wtWebGraphAnalog57662GraphicsScale1Unit": wtWebGraphAnalog57662GraphicsScale1Unit,
       "wtWebGraphAnalog57662GraphicsScale2Unit": wtWebGraphAnalog57662GraphicsScale2Unit,
       "wtWebGraphAnalog57662Report": wtWebGraphAnalog57662Report,
       "wtWebGraphAnalog57662ReportCount": wtWebGraphAnalog57662ReportCount,
       "wtWebGraphAnalog57662ReportIfTable": wtWebGraphAnalog57662ReportIfTable,
       "wtWebGraphAnalog57662ReportIfEntry": wtWebGraphAnalog57662ReportIfEntry,
       "wtWebGraphAnalog57662ReportNo": wtWebGraphAnalog57662ReportNo,
       "wtWebGraphAnalog57662ReportTable": wtWebGraphAnalog57662ReportTable,
       "wtWebGraphAnalog57662ReportEntry": wtWebGraphAnalog57662ReportEntry,
       "wtWebGraphAnalog57662ReportEnable": wtWebGraphAnalog57662ReportEnable,
       "wtWebGraphAnalog57662ReportTimerCron": wtWebGraphAnalog57662ReportTimerCron,
       "wtWebGraphAnalog57662ReportMethodeEnable": wtWebGraphAnalog57662ReportMethodeEnable,
       "wtWebGraphAnalog57662ReportEMailAddr": wtWebGraphAnalog57662ReportEMailAddr,
       "wtWebGraphAnalog57662ReportMailSubject": wtWebGraphAnalog57662ReportMailSubject,
       "wtWebGraphAnalog57662ReportMailText": wtWebGraphAnalog57662ReportMailText,
       "wtWebGraphAnalog57662ReportManagerIP": wtWebGraphAnalog57662ReportManagerIP,
       "wtWebGraphAnalog57662ReportTrapText": wtWebGraphAnalog57662ReportTrapText,
       "wtWebGraphAnalog57662ReportMailOptions": wtWebGraphAnalog57662ReportMailOptions,
       "wtWebGraphAnalog57662ReportTcpIpAddr": wtWebGraphAnalog57662ReportTcpIpAddr,
       "wtWebGraphAnalog57662ReportTcpPort": wtWebGraphAnalog57662ReportTcpPort,
       "wtWebGraphAnalog57662ReportTcpText": wtWebGraphAnalog57662ReportTcpText,
       "wtWebGraphAnalog57662ReportClearMailSubject": wtWebGraphAnalog57662ReportClearMailSubject,
       "wtWebGraphAnalog57662ReportClearMailText": wtWebGraphAnalog57662ReportClearMailText,
       "wtWebGraphAnalog57662ReportClearTrapText": wtWebGraphAnalog57662ReportClearTrapText,
       "wtWebGraphAnalog57662ReportClearTcpText": wtWebGraphAnalog57662ReportClearTcpText,
       "wtWebGraphAnalog57662ReportSyslogIpAddr": wtWebGraphAnalog57662ReportSyslogIpAddr,
       "wtWebGraphAnalog57662ReportSyslogPort": wtWebGraphAnalog57662ReportSyslogPort,
       "wtWebGraphAnalog57662ReportSyslogText": wtWebGraphAnalog57662ReportSyslogText,
       "wtWebGraphAnalog57662ReportSyslogClearText": wtWebGraphAnalog57662ReportSyslogClearText,
       "wtWebGraphAnalog57662ReportFtpDataPort": wtWebGraphAnalog57662ReportFtpDataPort,
       "wtWebGraphAnalog57662ReportFtpFileName": wtWebGraphAnalog57662ReportFtpFileName,
       "wtWebGraphAnalog57662ReportFtpText": wtWebGraphAnalog57662ReportFtpText,
       "wtWebGraphAnalog57662ReportFtpClearText": wtWebGraphAnalog57662ReportFtpClearText,
       "wtWebGraphAnalog57662ReportFtpOption": wtWebGraphAnalog57662ReportFtpOption,
       "wtWebGraphAnalog57662Ports": wtWebGraphAnalog57662Ports,
       "wtWebGraphAnalog57662PortTable": wtWebGraphAnalog57662PortTable,
       "wtWebGraphAnalog57662PortEntry": wtWebGraphAnalog57662PortEntry,
       "wtWebGraphAnalog57662PortName": wtWebGraphAnalog57662PortName,
       "wtWebGraphAnalog57662PortText": wtWebGraphAnalog57662PortText,
       "wtWebGraphAnalog57662PortOffset1": wtWebGraphAnalog57662PortOffset1,
       "wtWebGraphAnalog57662SetPoint1": wtWebGraphAnalog57662SetPoint1,
       "wtWebGraphAnalog57662PortOffset2": wtWebGraphAnalog57662PortOffset2,
       "wtWebGraphAnalog57662SetPoint2": wtWebGraphAnalog57662SetPoint2,
       "wtWebGraphAnalog57662PortComment": wtWebGraphAnalog57662PortComment,
       "wtWebGraphAnalog57662PortSensorSelect": wtWebGraphAnalog57662PortSensorSelect,
       "wtWebGraphAnalog57662PortUnit": wtWebGraphAnalog57662PortUnit,
       "wtWebGraphAnalog57662PortScale0": wtWebGraphAnalog57662PortScale0,
       "wtWebGraphAnalog57662PortScale100": wtWebGraphAnalog57662PortScale100,
       "wtWebGraphAnalog57662PortOutputMode": wtWebGraphAnalog57662PortOutputMode,
       "wtWebGraphAnalog57662PortInputMode": wtWebGraphAnalog57662PortInputMode,
       "wtWebGraphAnalog57662PortCompensationValue": wtWebGraphAnalog57662PortCompensationValue,
       "wtWebGraphAnalog57662PortCompensationMode": wtWebGraphAnalog57662PortCompensationMode,
       "wtWebGraphAnalog57662Manufact": wtWebGraphAnalog57662Manufact,
       "wtWebGraphAnalog57662MfName": wtWebGraphAnalog57662MfName,
       "wtWebGraphAnalog57662MfAddr": wtWebGraphAnalog57662MfAddr,
       "wtWebGraphAnalog57662MfHotline": wtWebGraphAnalog57662MfHotline,
       "wtWebGraphAnalog57662MfInternet": wtWebGraphAnalog57662MfInternet,
       "wtWebGraphAnalog57662MfDeviceTyp": wtWebGraphAnalog57662MfDeviceTyp,
       "wtWebGraphAnalog57662MfOrderNo": wtWebGraphAnalog57662MfOrderNo,
       "wtWebGraphAnalog57662Diag": wtWebGraphAnalog57662Diag,
       "wtWebGraphAnalog57662DiagErrorCount": wtWebGraphAnalog57662DiagErrorCount,
       "wtWebGraphAnalog57662DiagBinaryError": wtWebGraphAnalog57662DiagBinaryError,
       "wtWebGraphAnalog57662DiagErrorIndex": wtWebGraphAnalog57662DiagErrorIndex,
       "wtWebGraphAnalog57662DiagErrorMessage": wtWebGraphAnalog57662DiagErrorMessage,
       "wtWebGraphAnalog57662DiagErrorClear": wtWebGraphAnalog57662DiagErrorClear}
)
