# SNMP MIB module (WebGraph-AnalogIn-57644-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-AnalogIn-57644-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:37 2024
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
_WtWebGraphAnalogIn57644_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644 = _WtWebGraphAnalogIn57644_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12)
)
_WtWebGraphAnalogIn57644Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Inventory = _WtWebGraphAnalogIn57644Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1)
)


class _WtWebGraphAnalogIn57644Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57644Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644Sensors_Object = MibScalar
wtWebGraphAnalogIn57644Sensors = _WtWebGraphAnalogIn57644Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 1),
    _WtWebGraphAnalogIn57644Sensors_Type()
)
wtWebGraphAnalogIn57644Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Sensors.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorTable_Object = MibTable
wtWebGraphAnalogIn57644SensorTable = _WtWebGraphAnalogIn57644SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorEntry_Object = MibTableRow
wtWebGraphAnalogIn57644SensorEntry = _WtWebGraphAnalogIn57644SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2, 1)
)
wtWebGraphAnalogIn57644SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57644SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644SensorNo_Object = MibTableColumn
wtWebGraphAnalogIn57644SensorNo = _WtWebGraphAnalogIn57644SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57644SensorNo_Type()
)
wtWebGraphAnalogIn57644SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorNo.setStatus("mandatory")
_WtWebGraphAnalogIn57644ValuesTable_Object = MibTable
wtWebGraphAnalogIn57644ValuesTable = _WtWebGraphAnalogIn57644ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644ValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57644ValuesEntry = _WtWebGraphAnalogIn57644ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3, 1)
)
wtWebGraphAnalogIn57644ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644Values_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAnalogIn57644Values_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644Values_Object = MibTableColumn
wtWebGraphAnalogIn57644Values = _WtWebGraphAnalogIn57644Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57644Values_Type()
)
wtWebGraphAnalogIn57644Values.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Values.setStatus("mandatory")
_WtWebGraphAnalogIn57644BinaryValuesTable_Object = MibTable
wtWebGraphAnalogIn57644BinaryValuesTable = _WtWebGraphAnalogIn57644BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57644BinaryValuesEntry = _WtWebGraphAnalogIn57644BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4, 1)
)
wtWebGraphAnalogIn57644BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57644BinaryValues_Type = Integer32
_WtWebGraphAnalogIn57644BinaryValues_Object = MibTableColumn
wtWebGraphAnalogIn57644BinaryValues = _WtWebGraphAnalogIn57644BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4, 1, 1),
    _WtWebGraphAnalogIn57644BinaryValues_Type()
)
wtWebGraphAnalogIn57644BinaryValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644BinaryValues.setStatus("mandatory")
_WtWebGraphAnalogIn57644SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644SessCntrl = _WtWebGraphAnalogIn57644SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2)
)
_WtWebGraphAnalogIn57644SessCntrlPassword_Type = OctetString
_WtWebGraphAnalogIn57644SessCntrlPassword_Object = MibScalar
wtWebGraphAnalogIn57644SessCntrlPassword = _WtWebGraphAnalogIn57644SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 1),
    _WtWebGraphAnalogIn57644SessCntrlPassword_Type()
)
wtWebGraphAnalogIn57644SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalogIn57644SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalogIn57644SessCntrl-NoSession", 0),
          ("wtWebGraphAnalogIn57644SessCntrl-Session", 1))
    )


_WtWebGraphAnalogIn57644SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalogIn57644SessCntrlConfigMode = _WtWebGraphAnalogIn57644SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 2),
    _WtWebGraphAnalogIn57644SessCntrlConfigMode_Type()
)
wtWebGraphAnalogIn57644SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalogIn57644SessCntrlLogout_Type = Integer32
_WtWebGraphAnalogIn57644SessCntrlLogout_Object = MibScalar
wtWebGraphAnalogIn57644SessCntrlLogout = _WtWebGraphAnalogIn57644SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 3),
    _WtWebGraphAnalogIn57644SessCntrlLogout_Type()
)
wtWebGraphAnalogIn57644SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalogIn57644SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalogIn57644SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalogIn57644SessCntrlAdminPassword = _WtWebGraphAnalogIn57644SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 4),
    _WtWebGraphAnalogIn57644SessCntrlAdminPassword_Type()
)
wtWebGraphAnalogIn57644SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57644SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalogIn57644SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalogIn57644SessCntrlConfigPassword = _WtWebGraphAnalogIn57644SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 5),
    _WtWebGraphAnalogIn57644SessCntrlConfigPassword_Type()
)
wtWebGraphAnalogIn57644SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57644Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Config = _WtWebGraphAnalogIn57644Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3)
)
_WtWebGraphAnalogIn57644Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Device = _WtWebGraphAnalogIn57644Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1)
)
_WtWebGraphAnalogIn57644Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Text = _WtWebGraphAnalogIn57644Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1)
)
_WtWebGraphAnalogIn57644DeviceName_Type = OctetString
_WtWebGraphAnalogIn57644DeviceName_Object = MibScalar
wtWebGraphAnalogIn57644DeviceName = _WtWebGraphAnalogIn57644DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 1),
    _WtWebGraphAnalogIn57644DeviceName_Type()
)
wtWebGraphAnalogIn57644DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DeviceName.setStatus("mandatory")
_WtWebGraphAnalogIn57644DeviceText_Type = OctetString
_WtWebGraphAnalogIn57644DeviceText_Object = MibScalar
wtWebGraphAnalogIn57644DeviceText = _WtWebGraphAnalogIn57644DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 2),
    _WtWebGraphAnalogIn57644DeviceText_Type()
)
wtWebGraphAnalogIn57644DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DeviceText.setStatus("mandatory")
_WtWebGraphAnalogIn57644DeviceLocation_Type = OctetString
_WtWebGraphAnalogIn57644DeviceLocation_Object = MibScalar
wtWebGraphAnalogIn57644DeviceLocation = _WtWebGraphAnalogIn57644DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 3),
    _WtWebGraphAnalogIn57644DeviceLocation_Type()
)
wtWebGraphAnalogIn57644DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalogIn57644DeviceContact_Type = OctetString
_WtWebGraphAnalogIn57644DeviceContact_Object = MibScalar
wtWebGraphAnalogIn57644DeviceContact = _WtWebGraphAnalogIn57644DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 4),
    _WtWebGraphAnalogIn57644DeviceContact_Type()
)
wtWebGraphAnalogIn57644DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DeviceContact.setStatus("mandatory")
_WtWebGraphAnalogIn57644TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644TimeDate = _WtWebGraphAnalogIn57644TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2)
)
_WtWebGraphAnalogIn57644TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644TimeZone = _WtWebGraphAnalogIn57644TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1)
)
_WtWebGraphAnalogIn57644TzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57644TzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57644TzOffsetHrs = _WtWebGraphAnalogIn57644TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57644TzOffsetHrs_Type()
)
wtWebGraphAnalogIn57644TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57644TzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57644TzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57644TzOffsetMin = _WtWebGraphAnalogIn57644TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 2),
    _WtWebGraphAnalogIn57644TzOffsetMin_Type()
)
wtWebGraphAnalogIn57644TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57644TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644TzEnable_Object = MibScalar
wtWebGraphAnalogIn57644TzEnable = _WtWebGraphAnalogIn57644TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 3),
    _WtWebGraphAnalogIn57644TzEnable_Type()
)
wtWebGraphAnalogIn57644TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TzEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57644StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57644StTzOffsetHrs = _WtWebGraphAnalogIn57644StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 4),
    _WtWebGraphAnalogIn57644StTzOffsetHrs_Type()
)
wtWebGraphAnalogIn57644StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57644StTzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57644StTzOffsetMin = _WtWebGraphAnalogIn57644StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 5),
    _WtWebGraphAnalogIn57644StTzOffsetMin_Type()
)
wtWebGraphAnalogIn57644StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644StTzEnable_Object = MibScalar
wtWebGraphAnalogIn57644StTzEnable = _WtWebGraphAnalogIn57644StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 6),
    _WtWebGraphAnalogIn57644StTzEnable_Type()
)
wtWebGraphAnalogIn57644StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStartMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StartMonth-April", 4),
          ("wtWebGraphAnalogIn57644StartMonth-August", 8),
          ("wtWebGraphAnalogIn57644StartMonth-December", 12),
          ("wtWebGraphAnalogIn57644StartMonth-February", 2),
          ("wtWebGraphAnalogIn57644StartMonth-January", 1),
          ("wtWebGraphAnalogIn57644StartMonth-July", 7),
          ("wtWebGraphAnalogIn57644StartMonth-June", 6),
          ("wtWebGraphAnalogIn57644StartMonth-March", 3),
          ("wtWebGraphAnalogIn57644StartMonth-May", 5),
          ("wtWebGraphAnalogIn57644StartMonth-November", 11),
          ("wtWebGraphAnalogIn57644StartMonth-October", 10),
          ("wtWebGraphAnalogIn57644StartMonth-September", 9))
    )


_WtWebGraphAnalogIn57644StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStartMonth_Object = MibScalar
wtWebGraphAnalogIn57644StTzStartMonth = _WtWebGraphAnalogIn57644StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 7),
    _WtWebGraphAnalogIn57644StTzStartMonth_Type()
)
wtWebGraphAnalogIn57644StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStartMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StartMode-first", 1),
          ("wtWebGraphAnalogIn57644StartMode-fourth", 4),
          ("wtWebGraphAnalogIn57644StartMode-last", 5),
          ("wtWebGraphAnalogIn57644StartMode-second", 2),
          ("wtWebGraphAnalogIn57644StartMode-third", 3))
    )


_WtWebGraphAnalogIn57644StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStartMode_Object = MibScalar
wtWebGraphAnalogIn57644StTzStartMode = _WtWebGraphAnalogIn57644StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 8),
    _WtWebGraphAnalogIn57644StTzStartMode_Type()
)
wtWebGraphAnalogIn57644StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStartWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StartWday-Friday", 6),
          ("wtWebGraphAnalogIn57644StartWday-Monday", 2),
          ("wtWebGraphAnalogIn57644StartWday-Saturday", 7),
          ("wtWebGraphAnalogIn57644StartWday-Sunday", 1),
          ("wtWebGraphAnalogIn57644StartWday-Thursday", 4),
          ("wtWebGraphAnalogIn57644StartWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57644StartWday-Wednesday", 5))
    )


_WtWebGraphAnalogIn57644StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStartWday_Object = MibScalar
wtWebGraphAnalogIn57644StTzStartWday = _WtWebGraphAnalogIn57644StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 9),
    _WtWebGraphAnalogIn57644StTzStartWday_Type()
)
wtWebGraphAnalogIn57644StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzStartHrs_Type = Integer32
_WtWebGraphAnalogIn57644StTzStartHrs_Object = MibScalar
wtWebGraphAnalogIn57644StTzStartHrs = _WtWebGraphAnalogIn57644StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 10),
    _WtWebGraphAnalogIn57644StTzStartHrs_Type()
)
wtWebGraphAnalogIn57644StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzStartMin_Type = Integer32
_WtWebGraphAnalogIn57644StTzStartMin_Object = MibScalar
wtWebGraphAnalogIn57644StTzStartMin = _WtWebGraphAnalogIn57644StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 11),
    _WtWebGraphAnalogIn57644StTzStartMin_Type()
)
wtWebGraphAnalogIn57644StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStopMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StopMonth-April", 4),
          ("wtWebGraphAnalogIn57644StopMonth-August", 8),
          ("wtWebGraphAnalogIn57644StopMonth-December", 12),
          ("wtWebGraphAnalogIn57644StopMonth-February", 2),
          ("wtWebGraphAnalogIn57644StopMonth-January", 1),
          ("wtWebGraphAnalogIn57644StopMonth-July", 7),
          ("wtWebGraphAnalogIn57644StopMonth-June", 6),
          ("wtWebGraphAnalogIn57644StopMonth-March", 3),
          ("wtWebGraphAnalogIn57644StopMonth-May", 5),
          ("wtWebGraphAnalogIn57644StopMonth-November", 11),
          ("wtWebGraphAnalogIn57644StopMonth-October", 10),
          ("wtWebGraphAnalogIn57644StopMonth-September", 9))
    )


_WtWebGraphAnalogIn57644StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStopMonth_Object = MibScalar
wtWebGraphAnalogIn57644StTzStopMonth = _WtWebGraphAnalogIn57644StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 12),
    _WtWebGraphAnalogIn57644StTzStopMonth_Type()
)
wtWebGraphAnalogIn57644StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStopMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StopMode-first", 1),
          ("wtWebGraphAnalogIn57644StopMode-fourth", 4),
          ("wtWebGraphAnalogIn57644StopMode-last", 5),
          ("wtWebGraphAnalogIn57644StopMode-second", 2),
          ("wtWebGraphAnalogIn57644StopMode-third", 3))
    )


_WtWebGraphAnalogIn57644StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStopMode_Object = MibScalar
wtWebGraphAnalogIn57644StTzStopMode = _WtWebGraphAnalogIn57644StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 13),
    _WtWebGraphAnalogIn57644StTzStopMode_Type()
)
wtWebGraphAnalogIn57644StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57644StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644StTzStopWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644StopWday-Friday", 6),
          ("wtWebGraphAnalogIn57644StopWday-Monday", 2),
          ("wtWebGraphAnalogIn57644StopWday-Saturday", 7),
          ("wtWebGraphAnalogIn57644StopWday-Sunday", 1),
          ("wtWebGraphAnalogIn57644StopWday-Thursday", 4),
          ("wtWebGraphAnalogIn57644StopWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57644StopWday-Wednesday", 5))
    )


_WtWebGraphAnalogIn57644StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644StTzStopWday_Object = MibScalar
wtWebGraphAnalogIn57644StTzStopWday = _WtWebGraphAnalogIn57644StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 14),
    _WtWebGraphAnalogIn57644StTzStopWday_Type()
)
wtWebGraphAnalogIn57644StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzStopHrs_Type = Integer32
_WtWebGraphAnalogIn57644StTzStopHrs_Object = MibScalar
wtWebGraphAnalogIn57644StTzStopHrs = _WtWebGraphAnalogIn57644StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 15),
    _WtWebGraphAnalogIn57644StTzStopHrs_Type()
)
wtWebGraphAnalogIn57644StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57644StTzStopMin_Type = Integer32
_WtWebGraphAnalogIn57644StTzStopMin_Object = MibScalar
wtWebGraphAnalogIn57644StTzStopMin = _WtWebGraphAnalogIn57644StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 16),
    _WtWebGraphAnalogIn57644StTzStopMin_Type()
)
wtWebGraphAnalogIn57644StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalogIn57644TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644TimeServer = _WtWebGraphAnalogIn57644TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2)
)
_WtWebGraphAnalogIn57644TimeServer1_Type = OctetString
_WtWebGraphAnalogIn57644TimeServer1_Object = MibScalar
wtWebGraphAnalogIn57644TimeServer1 = _WtWebGraphAnalogIn57644TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 1),
    _WtWebGraphAnalogIn57644TimeServer1_Type()
)
wtWebGraphAnalogIn57644TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TimeServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57644TimeServer2_Type = OctetString
_WtWebGraphAnalogIn57644TimeServer2_Object = MibScalar
wtWebGraphAnalogIn57644TimeServer2 = _WtWebGraphAnalogIn57644TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 2),
    _WtWebGraphAnalogIn57644TimeServer2_Type()
)
wtWebGraphAnalogIn57644TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalogIn57644TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644TsEnable_Object = MibScalar
wtWebGraphAnalogIn57644TsEnable = _WtWebGraphAnalogIn57644TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 3),
    _WtWebGraphAnalogIn57644TsEnable_Type()
)
wtWebGraphAnalogIn57644TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TsEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644TsSyncTime_Type = Integer32
_WtWebGraphAnalogIn57644TsSyncTime_Object = MibScalar
wtWebGraphAnalogIn57644TsSyncTime = _WtWebGraphAnalogIn57644TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 4),
    _WtWebGraphAnalogIn57644TsSyncTime_Type()
)
wtWebGraphAnalogIn57644TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalogIn57644DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644DeviceClock = _WtWebGraphAnalogIn57644DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3)
)


class _WtWebGraphAnalogIn57644ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalogIn57644ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644ClockHrs_Object = MibScalar
wtWebGraphAnalogIn57644ClockHrs = _WtWebGraphAnalogIn57644ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 1),
    _WtWebGraphAnalogIn57644ClockHrs_Type()
)
wtWebGraphAnalogIn57644ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalogIn57644ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalogIn57644ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644ClockMin_Object = MibScalar
wtWebGraphAnalogIn57644ClockMin = _WtWebGraphAnalogIn57644ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 2),
    _WtWebGraphAnalogIn57644ClockMin_Type()
)
wtWebGraphAnalogIn57644ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ClockMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57644ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalogIn57644ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644ClockDay_Object = MibScalar
wtWebGraphAnalogIn57644ClockDay = _WtWebGraphAnalogIn57644ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 3),
    _WtWebGraphAnalogIn57644ClockDay_Type()
)
wtWebGraphAnalogIn57644ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ClockDay.setStatus("mandatory")


class _WtWebGraphAnalogIn57644ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644ClockMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644ClockMonth-April", 4),
          ("wtWebGraphAnalogIn57644ClockMonth-August", 8),
          ("wtWebGraphAnalogIn57644ClockMonth-December", 12),
          ("wtWebGraphAnalogIn57644ClockMonth-February", 2),
          ("wtWebGraphAnalogIn57644ClockMonth-January", 1),
          ("wtWebGraphAnalogIn57644ClockMonth-July", 7),
          ("wtWebGraphAnalogIn57644ClockMonth-June", 6),
          ("wtWebGraphAnalogIn57644ClockMonth-March", 3),
          ("wtWebGraphAnalogIn57644ClockMonth-May", 5),
          ("wtWebGraphAnalogIn57644ClockMonth-November", 11),
          ("wtWebGraphAnalogIn57644ClockMonth-October", 10),
          ("wtWebGraphAnalogIn57644ClockMonth-September", 9))
    )


_WtWebGraphAnalogIn57644ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644ClockMonth_Object = MibScalar
wtWebGraphAnalogIn57644ClockMonth = _WtWebGraphAnalogIn57644ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 4),
    _WtWebGraphAnalogIn57644ClockMonth_Type()
)
wtWebGraphAnalogIn57644ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57644ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalogIn57644ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644ClockYear_Object = MibScalar
wtWebGraphAnalogIn57644ClockYear = _WtWebGraphAnalogIn57644ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 5),
    _WtWebGraphAnalogIn57644ClockYear_Type()
)
wtWebGraphAnalogIn57644ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644ClockYear.setStatus("mandatory")
_WtWebGraphAnalogIn57644Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Basic = _WtWebGraphAnalogIn57644Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3)
)
_WtWebGraphAnalogIn57644Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Network = _WtWebGraphAnalogIn57644Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1)
)
_WtWebGraphAnalogIn57644IpAddress_Type = IpAddress
_WtWebGraphAnalogIn57644IpAddress_Object = MibScalar
wtWebGraphAnalogIn57644IpAddress = _WtWebGraphAnalogIn57644IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57644IpAddress_Type()
)
wtWebGraphAnalogIn57644IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644IpAddress.setStatus("mandatory")
_WtWebGraphAnalogIn57644SubnetMask_Type = IpAddress
_WtWebGraphAnalogIn57644SubnetMask_Object = MibScalar
wtWebGraphAnalogIn57644SubnetMask = _WtWebGraphAnalogIn57644SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 2),
    _WtWebGraphAnalogIn57644SubnetMask_Type()
)
wtWebGraphAnalogIn57644SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SubnetMask.setStatus("mandatory")
_WtWebGraphAnalogIn57644Gateway_Type = IpAddress
_WtWebGraphAnalogIn57644Gateway_Object = MibScalar
wtWebGraphAnalogIn57644Gateway = _WtWebGraphAnalogIn57644Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 3),
    _WtWebGraphAnalogIn57644Gateway_Type()
)
wtWebGraphAnalogIn57644Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Gateway.setStatus("mandatory")
_WtWebGraphAnalogIn57644DnsServer1_Type = OctetString
_WtWebGraphAnalogIn57644DnsServer1_Object = MibScalar
wtWebGraphAnalogIn57644DnsServer1 = _WtWebGraphAnalogIn57644DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 4),
    _WtWebGraphAnalogIn57644DnsServer1_Type()
)
wtWebGraphAnalogIn57644DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DnsServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57644DnsServer2_Type = OctetString
_WtWebGraphAnalogIn57644DnsServer2_Object = MibScalar
wtWebGraphAnalogIn57644DnsServer2 = _WtWebGraphAnalogIn57644DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 5),
    _WtWebGraphAnalogIn57644DnsServer2_Type()
)
wtWebGraphAnalogIn57644DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DnsServer2.setStatus("mandatory")
_WtWebGraphAnalogIn57644AddConfig_Type = OctetString
_WtWebGraphAnalogIn57644AddConfig_Object = MibScalar
wtWebGraphAnalogIn57644AddConfig = _WtWebGraphAnalogIn57644AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 6),
    _WtWebGraphAnalogIn57644AddConfig_Type()
)
wtWebGraphAnalogIn57644AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AddConfig.setStatus("mandatory")
_WtWebGraphAnalogIn57644HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644HTTP = _WtWebGraphAnalogIn57644HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2)
)
_WtWebGraphAnalogIn57644Startup_Type = OctetString
_WtWebGraphAnalogIn57644Startup_Object = MibScalar
wtWebGraphAnalogIn57644Startup = _WtWebGraphAnalogIn57644Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 1),
    _WtWebGraphAnalogIn57644Startup_Type()
)
wtWebGraphAnalogIn57644Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Startup.setStatus("mandatory")
_WtWebGraphAnalogIn57644GetHeaderEnable_Type = OctetString
_WtWebGraphAnalogIn57644GetHeaderEnable_Object = MibScalar
wtWebGraphAnalogIn57644GetHeaderEnable = _WtWebGraphAnalogIn57644GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 2),
    _WtWebGraphAnalogIn57644GetHeaderEnable_Type()
)
wtWebGraphAnalogIn57644GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57644HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57644HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644HttpPort_Object = MibScalar
wtWebGraphAnalogIn57644HttpPort = _WtWebGraphAnalogIn57644HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 3),
    _WtWebGraphAnalogIn57644HttpPort_Type()
)
wtWebGraphAnalogIn57644HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644HttpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Mail = _WtWebGraphAnalogIn57644Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3)
)
_WtWebGraphAnalogIn57644MailAdName_Type = OctetString
_WtWebGraphAnalogIn57644MailAdName_Object = MibScalar
wtWebGraphAnalogIn57644MailAdName = _WtWebGraphAnalogIn57644MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 1),
    _WtWebGraphAnalogIn57644MailAdName_Type()
)
wtWebGraphAnalogIn57644MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailAdName.setStatus("mandatory")
_WtWebGraphAnalogIn57644MailReply_Type = OctetString
_WtWebGraphAnalogIn57644MailReply_Object = MibScalar
wtWebGraphAnalogIn57644MailReply = _WtWebGraphAnalogIn57644MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 2),
    _WtWebGraphAnalogIn57644MailReply_Type()
)
wtWebGraphAnalogIn57644MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailReply.setStatus("mandatory")
_WtWebGraphAnalogIn57644MailServer_Type = OctetString
_WtWebGraphAnalogIn57644MailServer_Object = MibScalar
wtWebGraphAnalogIn57644MailServer = _WtWebGraphAnalogIn57644MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 3),
    _WtWebGraphAnalogIn57644MailServer_Type()
)
wtWebGraphAnalogIn57644MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57644MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644MailAuthentication_Object = MibScalar
wtWebGraphAnalogIn57644MailAuthentication = _WtWebGraphAnalogIn57644MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 5),
    _WtWebGraphAnalogIn57644MailAuthentication_Type()
)
wtWebGraphAnalogIn57644MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalogIn57644MailAuthUser_Type = OctetString
_WtWebGraphAnalogIn57644MailAuthUser_Object = MibScalar
wtWebGraphAnalogIn57644MailAuthUser = _WtWebGraphAnalogIn57644MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 6),
    _WtWebGraphAnalogIn57644MailAuthUser_Type()
)
wtWebGraphAnalogIn57644MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalogIn57644MailAuthPassword_Type = OctetString
_WtWebGraphAnalogIn57644MailAuthPassword_Object = MibScalar
wtWebGraphAnalogIn57644MailAuthPassword = _WtWebGraphAnalogIn57644MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 7),
    _WtWebGraphAnalogIn57644MailAuthPassword_Type()
)
wtWebGraphAnalogIn57644MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57644MailPop3Server_Type = OctetString
_WtWebGraphAnalogIn57644MailPop3Server_Object = MibScalar
wtWebGraphAnalogIn57644MailPop3Server = _WtWebGraphAnalogIn57644MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 8),
    _WtWebGraphAnalogIn57644MailPop3Server_Type()
)
wtWebGraphAnalogIn57644MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalogIn57644SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644SNMP = _WtWebGraphAnalogIn57644SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4)
)
_WtWebGraphAnalogIn57644SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalogIn57644SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalogIn57644SnmpCommunityStringRead = _WtWebGraphAnalogIn57644SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 1),
    _WtWebGraphAnalogIn57644SnmpCommunityStringRead_Type()
)
wtWebGraphAnalogIn57644SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalogIn57644SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalogIn57644SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalogIn57644SnmpCommunityStringReadWrite = _WtWebGraphAnalogIn57644SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 2),
    _WtWebGraphAnalogIn57644SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalogIn57644SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalogIn57644SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalogIn57644SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalogIn57644SystemTrapManagerIP = _WtWebGraphAnalogIn57644SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 3),
    _WtWebGraphAnalogIn57644SystemTrapManagerIP_Type()
)
wtWebGraphAnalogIn57644SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalogIn57644SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644SystemTrapEnable_Object = MibScalar
wtWebGraphAnalogIn57644SystemTrapEnable = _WtWebGraphAnalogIn57644SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 4),
    _WtWebGraphAnalogIn57644SystemTrapEnable_Type()
)
wtWebGraphAnalogIn57644SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644SnmpEnable_Type = OctetString
_WtWebGraphAnalogIn57644SnmpEnable_Object = MibScalar
wtWebGraphAnalogIn57644SnmpEnable = _WtWebGraphAnalogIn57644SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 5),
    _WtWebGraphAnalogIn57644SnmpEnable_Type()
)
wtWebGraphAnalogIn57644SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalogIn57644SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalogIn57644SnmpCommunityStringTrap = _WtWebGraphAnalogIn57644SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 6),
    _WtWebGraphAnalogIn57644SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalogIn57644SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalogIn57644UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644UDP = _WtWebGraphAnalogIn57644UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5)
)


class _WtWebGraphAnalogIn57644UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57644UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644UdpPort_Object = MibScalar
wtWebGraphAnalogIn57644UdpPort = _WtWebGraphAnalogIn57644UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5, 1),
    _WtWebGraphAnalogIn57644UdpPort_Type()
)
wtWebGraphAnalogIn57644UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644UdpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644UdpEnable_Type = OctetString
_WtWebGraphAnalogIn57644UdpEnable_Object = MibScalar
wtWebGraphAnalogIn57644UdpEnable = _WtWebGraphAnalogIn57644UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5, 2),
    _WtWebGraphAnalogIn57644UdpEnable_Type()
)
wtWebGraphAnalogIn57644UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644UdpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Syslog = _WtWebGraphAnalogIn57644Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6)
)
_WtWebGraphAnalogIn57644SyslogServerIP_Type = OctetString
_WtWebGraphAnalogIn57644SyslogServerIP_Object = MibScalar
wtWebGraphAnalogIn57644SyslogServerIP = _WtWebGraphAnalogIn57644SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 1),
    _WtWebGraphAnalogIn57644SyslogServerIP_Type()
)
wtWebGraphAnalogIn57644SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57644SyslogServerPort_Type = Integer32
_WtWebGraphAnalogIn57644SyslogServerPort_Object = MibScalar
wtWebGraphAnalogIn57644SyslogServerPort = _WtWebGraphAnalogIn57644SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 2),
    _WtWebGraphAnalogIn57644SyslogServerPort_Type()
)
wtWebGraphAnalogIn57644SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalogIn57644SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalogIn57644SyslogSystemMessagesEnable = _WtWebGraphAnalogIn57644SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 3),
    _WtWebGraphAnalogIn57644SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalogIn57644SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644SyslogEnable_Type = OctetString
_WtWebGraphAnalogIn57644SyslogEnable_Object = MibScalar
wtWebGraphAnalogIn57644SyslogEnable = _WtWebGraphAnalogIn57644SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 4),
    _WtWebGraphAnalogIn57644SyslogEnable_Type()
)
wtWebGraphAnalogIn57644SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644FTP = _WtWebGraphAnalogIn57644FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7)
)
_WtWebGraphAnalogIn57644FTPServerIP_Type = OctetString
_WtWebGraphAnalogIn57644FTPServerIP_Object = MibScalar
wtWebGraphAnalogIn57644FTPServerIP = _WtWebGraphAnalogIn57644FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 1),
    _WtWebGraphAnalogIn57644FTPServerIP_Type()
)
wtWebGraphAnalogIn57644FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPServerControlPort_Type = Integer32
_WtWebGraphAnalogIn57644FTPServerControlPort_Object = MibScalar
wtWebGraphAnalogIn57644FTPServerControlPort = _WtWebGraphAnalogIn57644FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 2),
    _WtWebGraphAnalogIn57644FTPServerControlPort_Type()
)
wtWebGraphAnalogIn57644FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPUserName_Type = OctetString
_WtWebGraphAnalogIn57644FTPUserName_Object = MibScalar
wtWebGraphAnalogIn57644FTPUserName = _WtWebGraphAnalogIn57644FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 3),
    _WtWebGraphAnalogIn57644FTPUserName_Type()
)
wtWebGraphAnalogIn57644FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPUserName.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPPassword_Type = OctetString
_WtWebGraphAnalogIn57644FTPPassword_Object = MibScalar
wtWebGraphAnalogIn57644FTPPassword = _WtWebGraphAnalogIn57644FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 4),
    _WtWebGraphAnalogIn57644FTPPassword_Type()
)
wtWebGraphAnalogIn57644FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPAccount_Type = OctetString
_WtWebGraphAnalogIn57644FTPAccount_Object = MibScalar
wtWebGraphAnalogIn57644FTPAccount = _WtWebGraphAnalogIn57644FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 5),
    _WtWebGraphAnalogIn57644FTPAccount_Type()
)
wtWebGraphAnalogIn57644FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPAccount.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPOption_Type = OctetString
_WtWebGraphAnalogIn57644FTPOption_Object = MibScalar
wtWebGraphAnalogIn57644FTPOption = _WtWebGraphAnalogIn57644FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 6),
    _WtWebGraphAnalogIn57644FTPOption_Type()
)
wtWebGraphAnalogIn57644FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPOption.setStatus("mandatory")
_WtWebGraphAnalogIn57644FTPEnable_Type = OctetString
_WtWebGraphAnalogIn57644FTPEnable_Object = MibScalar
wtWebGraphAnalogIn57644FTPEnable = _WtWebGraphAnalogIn57644FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 7),
    _WtWebGraphAnalogIn57644FTPEnable_Type()
)
wtWebGraphAnalogIn57644FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644FTPEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Datalogger = _WtWebGraphAnalogIn57644Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4)
)


class _WtWebGraphAnalogIn57644LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644LoggerTimebase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalogIn57644Datalogger-15Min", 3),
          ("wtWebGraphAnalogIn57644Datalogger-1Min", 1),
          ("wtWebGraphAnalogIn57644Datalogger-5Min", 2),
          ("wtWebGraphAnalogIn57644Datalogger-60Min", 4))
    )


_WtWebGraphAnalogIn57644LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644LoggerTimebase_Object = MibScalar
wtWebGraphAnalogIn57644LoggerTimebase = _WtWebGraphAnalogIn57644LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 1),
    _WtWebGraphAnalogIn57644LoggerTimebase_Type()
)
wtWebGraphAnalogIn57644LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalogIn57644LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644LoggerSensorSel_Object = MibScalar
wtWebGraphAnalogIn57644LoggerSensorSel = _WtWebGraphAnalogIn57644LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 2),
    _WtWebGraphAnalogIn57644LoggerSensorSel_Type()
)
wtWebGraphAnalogIn57644LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644LoggerSensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57644DisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644DisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644DisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644DisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57644DisplaySensorSel = _WtWebGraphAnalogIn57644DisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 3),
    _WtWebGraphAnalogIn57644DisplaySensorSel_Type()
)
wtWebGraphAnalogIn57644DisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DisplaySensorSel.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorColorTable_Object = MibTable
wtWebGraphAnalogIn57644SensorColorTable = _WtWebGraphAnalogIn57644SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorColorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorColorEntry_Object = MibTableRow
wtWebGraphAnalogIn57644SensorColorEntry = _WtWebGraphAnalogIn57644SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4, 1)
)
wtWebGraphAnalogIn57644SensorColorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorColorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644SensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644SensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57644SensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644SensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57644SensorColor = _WtWebGraphAnalogIn57644SensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4, 1, 1),
    _WtWebGraphAnalogIn57644SensorColor_Type()
)
wtWebGraphAnalogIn57644SensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57644AutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57644AutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57644AutoScaleEnable = _WtWebGraphAnalogIn57644AutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 5),
    _WtWebGraphAnalogIn57644AutoScaleEnable_Type()
)
wtWebGraphAnalogIn57644AutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644VerticalUpperLimit_Type = OctetString
_WtWebGraphAnalogIn57644VerticalUpperLimit_Object = MibScalar
wtWebGraphAnalogIn57644VerticalUpperLimit = _WtWebGraphAnalogIn57644VerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 6),
    _WtWebGraphAnalogIn57644VerticalUpperLimit_Type()
)
wtWebGraphAnalogIn57644VerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644VerticalUpperLimit.setStatus("mandatory")
_WtWebGraphAnalogIn57644VerticalLowerLimit_Type = OctetString
_WtWebGraphAnalogIn57644VerticalLowerLimit_Object = MibScalar
wtWebGraphAnalogIn57644VerticalLowerLimit = _WtWebGraphAnalogIn57644VerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 7),
    _WtWebGraphAnalogIn57644VerticalLowerLimit_Type()
)
wtWebGraphAnalogIn57644VerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644VerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphAnalogIn57644HorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644HorizontalZoom based on Integer32"""
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
        *(("wtWebGraphAnalogIn57644Zoom-25days", 6),
          ("wtWebGraphAnalogIn57644Zoom-25min", 1),
          ("wtWebGraphAnalogIn57644Zoom-30hrs", 4),
          ("wtWebGraphAnalogIn57644Zoom-5days", 5),
          ("wtWebGraphAnalogIn57644Zoom-5hrs", 3),
          ("wtWebGraphAnalogIn57644Zoom-75min", 2))
    )


_WtWebGraphAnalogIn57644HorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644HorizontalZoom_Object = MibScalar
wtWebGraphAnalogIn57644HorizontalZoom = _WtWebGraphAnalogIn57644HorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 8),
    _WtWebGraphAnalogIn57644HorizontalZoom_Type()
)
wtWebGraphAnalogIn57644HorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644HorizontalZoom.setStatus("mandatory")
_WtWebGraphAnalogIn57644Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Alarm = _WtWebGraphAnalogIn57644Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5)
)


class _WtWebGraphAnalogIn57644AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57644AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644AlarmCount_Object = MibScalar
wtWebGraphAnalogIn57644AlarmCount = _WtWebGraphAnalogIn57644AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 1),
    _WtWebGraphAnalogIn57644AlarmCount_Type()
)
wtWebGraphAnalogIn57644AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmCount.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmIfTable_Object = MibTable
wtWebGraphAnalogIn57644AlarmIfTable = _WtWebGraphAnalogIn57644AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalogIn57644AlarmIfEntry = _WtWebGraphAnalogIn57644AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2, 1)
)
wtWebGraphAnalogIn57644AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57644AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644AlarmNo_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmNo = _WtWebGraphAnalogIn57644AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalogIn57644AlarmNo_Type()
)
wtWebGraphAnalogIn57644AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmNo.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmTable_Object = MibTable
wtWebGraphAnalogIn57644AlarmTable = _WtWebGraphAnalogIn57644AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmEntry_Object = MibTableRow
wtWebGraphAnalogIn57644AlarmEntry = _WtWebGraphAnalogIn57644AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1)
)
wtWebGraphAnalogIn57644AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTrigger = _WtWebGraphAnalogIn57644AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalogIn57644AlarmTrigger_Type()
)
wtWebGraphAnalogIn57644AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmMin_Type = OctetString
_WtWebGraphAnalogIn57644AlarmMin_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmMin = _WtWebGraphAnalogIn57644AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalogIn57644AlarmMin_Type()
)
wtWebGraphAnalogIn57644AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmMin.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmMax_Type = OctetString
_WtWebGraphAnalogIn57644AlarmMax_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmMax = _WtWebGraphAnalogIn57644AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalogIn57644AlarmMax_Type()
)
wtWebGraphAnalogIn57644AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmMax.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmHysteresis_Type = OctetString
_WtWebGraphAnalogIn57644AlarmHysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmHysteresis = _WtWebGraphAnalogIn57644AlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalogIn57644AlarmHysteresis_Type()
)
wtWebGraphAnalogIn57644AlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmHysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmDelay_Type = OctetString
_WtWebGraphAnalogIn57644AlarmDelay_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmDelay = _WtWebGraphAnalogIn57644AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalogIn57644AlarmDelay_Type()
)
wtWebGraphAnalogIn57644AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmInterval_Type = OctetString
_WtWebGraphAnalogIn57644AlarmInterval_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmInterval = _WtWebGraphAnalogIn57644AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalogIn57644AlarmInterval_Type()
)
wtWebGraphAnalogIn57644AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644AlarmEnable_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmEnable = _WtWebGraphAnalogIn57644AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalogIn57644AlarmEnable_Type()
)
wtWebGraphAnalogIn57644AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalogIn57644AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmEMailAddr = _WtWebGraphAnalogIn57644AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalogIn57644AlarmEMailAddr_Type()
)
wtWebGraphAnalogIn57644AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmMailSubject_Type = OctetString
_WtWebGraphAnalogIn57644AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmMailSubject = _WtWebGraphAnalogIn57644AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalogIn57644AlarmMailSubject_Type()
)
wtWebGraphAnalogIn57644AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmMailText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmMailText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmMailText = _WtWebGraphAnalogIn57644AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalogIn57644AlarmMailText_Type()
)
wtWebGraphAnalogIn57644AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmManagerIP_Type = OctetString
_WtWebGraphAnalogIn57644AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmManagerIP = _WtWebGraphAnalogIn57644AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalogIn57644AlarmManagerIP_Type()
)
wtWebGraphAnalogIn57644AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmTrapText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTrapText = _WtWebGraphAnalogIn57644AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalogIn57644AlarmTrapText_Type()
)
wtWebGraphAnalogIn57644AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmMailOptions = _WtWebGraphAnalogIn57644AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalogIn57644AlarmMailOptions_Type()
)
wtWebGraphAnalogIn57644AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalogIn57644AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTcpIpAddr = _WtWebGraphAnalogIn57644AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalogIn57644AlarmTcpIpAddr_Type()
)
wtWebGraphAnalogIn57644AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57644AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTcpPort = _WtWebGraphAnalogIn57644AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalogIn57644AlarmTcpPort_Type()
)
wtWebGraphAnalogIn57644AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmTcpText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTcpText = _WtWebGraphAnalogIn57644AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalogIn57644AlarmTcpText_Type()
)
wtWebGraphAnalogIn57644AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalogIn57644AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmClearMailSubject = _WtWebGraphAnalogIn57644AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalogIn57644AlarmClearMailSubject_Type()
)
wtWebGraphAnalogIn57644AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmClearMailText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmClearMailText = _WtWebGraphAnalogIn57644AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalogIn57644AlarmClearMailText_Type()
)
wtWebGraphAnalogIn57644AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmClearTrapText = _WtWebGraphAnalogIn57644AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalogIn57644AlarmClearTrapText_Type()
)
wtWebGraphAnalogIn57644AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmClearTcpText = _WtWebGraphAnalogIn57644AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalogIn57644AlarmClearTcpText_Type()
)
wtWebGraphAnalogIn57644AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57644Alarm2Min_Type = OctetString
_WtWebGraphAnalogIn57644Alarm2Min_Object = MibTableColumn
wtWebGraphAnalogIn57644Alarm2Min = _WtWebGraphAnalogIn57644Alarm2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalogIn57644Alarm2Min_Type()
)
wtWebGraphAnalogIn57644Alarm2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alarm2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57644Alarm2Max_Type = OctetString
_WtWebGraphAnalogIn57644Alarm2Max_Object = MibTableColumn
wtWebGraphAnalogIn57644Alarm2Max = _WtWebGraphAnalogIn57644Alarm2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalogIn57644Alarm2Max_Type()
)
wtWebGraphAnalogIn57644Alarm2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alarm2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57644Alarm2Hysteresis_Type = OctetString
_WtWebGraphAnalogIn57644Alarm2Hysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57644Alarm2Hysteresis = _WtWebGraphAnalogIn57644Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalogIn57644Alarm2Hysteresis_Type()
)
wtWebGraphAnalogIn57644Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alarm2Hysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalogIn57644AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmSyslogIpAddr = _WtWebGraphAnalogIn57644AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalogIn57644AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalogIn57644AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57644AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57644AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57644AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmSyslogPort = _WtWebGraphAnalogIn57644AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalogIn57644AlarmSyslogPort_Type()
)
wtWebGraphAnalogIn57644AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmSyslogText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmSyslogText = _WtWebGraphAnalogIn57644AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalogIn57644AlarmSyslogText_Type()
)
wtWebGraphAnalogIn57644AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmSyslogClearText = _WtWebGraphAnalogIn57644AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalogIn57644AlarmSyslogClearText_Type()
)
wtWebGraphAnalogIn57644AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalogIn57644AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmFtpDataPort = _WtWebGraphAnalogIn57644AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalogIn57644AlarmFtpDataPort_Type()
)
wtWebGraphAnalogIn57644AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalogIn57644AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmFtpFileName = _WtWebGraphAnalogIn57644AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalogIn57644AlarmFtpFileName_Type()
)
wtWebGraphAnalogIn57644AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmFtpText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmFtpText = _WtWebGraphAnalogIn57644AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalogIn57644AlarmFtpText_Type()
)
wtWebGraphAnalogIn57644AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalogIn57644AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmFtpClearText = _WtWebGraphAnalogIn57644AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalogIn57644AlarmFtpClearText_Type()
)
wtWebGraphAnalogIn57644AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalogIn57644AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmFtpOption = _WtWebGraphAnalogIn57644AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalogIn57644AlarmFtpOption_Type()
)
wtWebGraphAnalogIn57644AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalogIn57644AlarmTimerCron_Type = OctetString
_WtWebGraphAnalogIn57644AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalogIn57644AlarmTimerCron = _WtWebGraphAnalogIn57644AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalogIn57644AlarmTimerCron_Type()
)
wtWebGraphAnalogIn57644AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalogIn57644Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Graphics = _WtWebGraphAnalogIn57644Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6)
)
_WtWebGraphAnalogIn57644GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644GraphicsBase = _WtWebGraphAnalogIn57644GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1)
)
_WtWebGraphAnalogIn57644GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBaseEnable = _WtWebGraphAnalogIn57644GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 1),
    _WtWebGraphAnalogIn57644GraphicsBaseEnable_Type()
)
wtWebGraphAnalogIn57644GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBaseWidth = _WtWebGraphAnalogIn57644GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 2),
    _WtWebGraphAnalogIn57644GraphicsBaseWidth_Type()
)
wtWebGraphAnalogIn57644GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBaseHeight = _WtWebGraphAnalogIn57644GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 3),
    _WtWebGraphAnalogIn57644GraphicsBaseHeight_Type()
)
wtWebGraphAnalogIn57644GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalogIn57644GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57644GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBaseFrameColor = _WtWebGraphAnalogIn57644GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 4),
    _WtWebGraphAnalogIn57644GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalogIn57644GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalogIn57644GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57644GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor = _WtWebGraphAnalogIn57644GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 5),
    _WtWebGraphAnalogIn57644GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsBasePollingrate = _WtWebGraphAnalogIn57644GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 6),
    _WtWebGraphAnalogIn57644GraphicsBasePollingrate_Type()
)
wtWebGraphAnalogIn57644GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644GraphicsSelect = _WtWebGraphAnalogIn57644GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2)
)


class _WtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel = _WtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 1),
    _WtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 2),
    _WtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorColor2Table_Object = MibTable
wtWebGraphAnalogIn57644SensorColor2Table = _WtWebGraphAnalogIn57644SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalogIn57644SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalogIn57644SensorColor2Entry = _WtWebGraphAnalogIn57644SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalogIn57644SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalogIn57644GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57644GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57644GraphicsSensorColor = _WtWebGraphAnalogIn57644GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalogIn57644GraphicsSensorColor_Type()
)
wtWebGraphAnalogIn57644GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalogIn57644GraphicsSelectScale = _WtWebGraphAnalogIn57644GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalogIn57644GraphicsSelectScale_Type()
)
wtWebGraphAnalogIn57644GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644GraphicsScale = _WtWebGraphAnalogIn57644GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3)
)
_WtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable = _WtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 1),
    _WtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable = _WtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 2),
    _WtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale1Min = _WtWebGraphAnalogIn57644GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 3),
    _WtWebGraphAnalogIn57644GraphicsScale1Min_Type()
)
wtWebGraphAnalogIn57644GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale2Min = _WtWebGraphAnalogIn57644GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 4),
    _WtWebGraphAnalogIn57644GraphicsScale2Min_Type()
)
wtWebGraphAnalogIn57644GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale3Min_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale3Min_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale3Min = _WtWebGraphAnalogIn57644GraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 5),
    _WtWebGraphAnalogIn57644GraphicsScale3Min_Type()
)
wtWebGraphAnalogIn57644GraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale3Min.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale4Min_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale4Min_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale4Min = _WtWebGraphAnalogIn57644GraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 6),
    _WtWebGraphAnalogIn57644GraphicsScale4Min_Type()
)
wtWebGraphAnalogIn57644GraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale4Min.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale1Max = _WtWebGraphAnalogIn57644GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 7),
    _WtWebGraphAnalogIn57644GraphicsScale1Max_Type()
)
wtWebGraphAnalogIn57644GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale2Max = _WtWebGraphAnalogIn57644GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 8),
    _WtWebGraphAnalogIn57644GraphicsScale2Max_Type()
)
wtWebGraphAnalogIn57644GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale3Max_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale3Max_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale3Max = _WtWebGraphAnalogIn57644GraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 9),
    _WtWebGraphAnalogIn57644GraphicsScale3Max_Type()
)
wtWebGraphAnalogIn57644GraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale3Max.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale4Max_Type = Integer32
_WtWebGraphAnalogIn57644GraphicsScale4Max_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale4Max = _WtWebGraphAnalogIn57644GraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 10),
    _WtWebGraphAnalogIn57644GraphicsScale4Max_Type()
)
wtWebGraphAnalogIn57644GraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale4Max.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale1Unit = _WtWebGraphAnalogIn57644GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 11),
    _WtWebGraphAnalogIn57644GraphicsScale1Unit_Type()
)
wtWebGraphAnalogIn57644GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale2Unit = _WtWebGraphAnalogIn57644GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 12),
    _WtWebGraphAnalogIn57644GraphicsScale2Unit_Type()
)
wtWebGraphAnalogIn57644GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale3Unit_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScale3Unit_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale3Unit = _WtWebGraphAnalogIn57644GraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 13),
    _WtWebGraphAnalogIn57644GraphicsScale3Unit_Type()
)
wtWebGraphAnalogIn57644GraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57644GraphicsScale4Unit_Type = OctetString
_WtWebGraphAnalogIn57644GraphicsScale4Unit_Object = MibScalar
wtWebGraphAnalogIn57644GraphicsScale4Unit = _WtWebGraphAnalogIn57644GraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 14),
    _WtWebGraphAnalogIn57644GraphicsScale4Unit_Type()
)
wtWebGraphAnalogIn57644GraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644GraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57644Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Ports = _WtWebGraphAnalogIn57644Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2)
)
_WtWebGraphAnalogIn57644PortTable_Object = MibTable
wtWebGraphAnalogIn57644PortTable = _WtWebGraphAnalogIn57644PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortTable.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortEntry_Object = MibTableRow
wtWebGraphAnalogIn57644PortEntry = _WtWebGraphAnalogIn57644PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1)
)
wtWebGraphAnalogIn57644PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortName_Type = OctetString
_WtWebGraphAnalogIn57644PortName_Object = MibTableColumn
wtWebGraphAnalogIn57644PortName = _WtWebGraphAnalogIn57644PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 1),
    _WtWebGraphAnalogIn57644PortName_Type()
)
wtWebGraphAnalogIn57644PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortName.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortText_Type = OctetString
_WtWebGraphAnalogIn57644PortText_Object = MibTableColumn
wtWebGraphAnalogIn57644PortText = _WtWebGraphAnalogIn57644PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 2),
    _WtWebGraphAnalogIn57644PortText_Type()
)
wtWebGraphAnalogIn57644PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortText.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortOffset1_Type = OctetString
_WtWebGraphAnalogIn57644PortOffset1_Object = MibTableColumn
wtWebGraphAnalogIn57644PortOffset1 = _WtWebGraphAnalogIn57644PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 3),
    _WtWebGraphAnalogIn57644PortOffset1_Type()
)
wtWebGraphAnalogIn57644PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortOffset1.setStatus("mandatory")
_WtWebGraphAnalogIn57644SetPoint1_Type = OctetString
_WtWebGraphAnalogIn57644SetPoint1_Object = MibTableColumn
wtWebGraphAnalogIn57644SetPoint1 = _WtWebGraphAnalogIn57644SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 4),
    _WtWebGraphAnalogIn57644SetPoint1_Type()
)
wtWebGraphAnalogIn57644SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SetPoint1.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortOffset2_Type = OctetString
_WtWebGraphAnalogIn57644PortOffset2_Object = MibTableColumn
wtWebGraphAnalogIn57644PortOffset2 = _WtWebGraphAnalogIn57644PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 5),
    _WtWebGraphAnalogIn57644PortOffset2_Type()
)
wtWebGraphAnalogIn57644PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortOffset2.setStatus("mandatory")
_WtWebGraphAnalogIn57644SetPoint2_Type = OctetString
_WtWebGraphAnalogIn57644SetPoint2_Object = MibTableColumn
wtWebGraphAnalogIn57644SetPoint2 = _WtWebGraphAnalogIn57644SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 6),
    _WtWebGraphAnalogIn57644SetPoint2_Type()
)
wtWebGraphAnalogIn57644SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644SetPoint2.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortComment_Type = OctetString
_WtWebGraphAnalogIn57644PortComment_Object = MibTableColumn
wtWebGraphAnalogIn57644PortComment = _WtWebGraphAnalogIn57644PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 7),
    _WtWebGraphAnalogIn57644PortComment_Type()
)
wtWebGraphAnalogIn57644PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortComment.setStatus("mandatory")


class _WtWebGraphAnalogIn57644PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57644PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57644PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57644PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalogIn57644PortSensorSelect = _WtWebGraphAnalogIn57644PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 8),
    _WtWebGraphAnalogIn57644PortSensorSelect_Type()
)
wtWebGraphAnalogIn57644PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortUnit_Type = OctetString
_WtWebGraphAnalogIn57644PortUnit_Object = MibTableColumn
wtWebGraphAnalogIn57644PortUnit = _WtWebGraphAnalogIn57644PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 9),
    _WtWebGraphAnalogIn57644PortUnit_Type()
)
wtWebGraphAnalogIn57644PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortUnit.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortScale0_Type = OctetString
_WtWebGraphAnalogIn57644PortScale0_Object = MibTableColumn
wtWebGraphAnalogIn57644PortScale0 = _WtWebGraphAnalogIn57644PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 10),
    _WtWebGraphAnalogIn57644PortScale0_Type()
)
wtWebGraphAnalogIn57644PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortScale0.setStatus("mandatory")
_WtWebGraphAnalogIn57644PortScale100_Type = OctetString
_WtWebGraphAnalogIn57644PortScale100_Object = MibTableColumn
wtWebGraphAnalogIn57644PortScale100 = _WtWebGraphAnalogIn57644PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 11),
    _WtWebGraphAnalogIn57644PortScale100_Type()
)
wtWebGraphAnalogIn57644PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644PortScale100.setStatus("mandatory")
_WtWebGraphAnalogIn57644Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Manufact = _WtWebGraphAnalogIn57644Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3)
)
_WtWebGraphAnalogIn57644MfName_Type = OctetString
_WtWebGraphAnalogIn57644MfName_Object = MibScalar
wtWebGraphAnalogIn57644MfName = _WtWebGraphAnalogIn57644MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 1),
    _WtWebGraphAnalogIn57644MfName_Type()
)
wtWebGraphAnalogIn57644MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfName.setStatus("mandatory")
_WtWebGraphAnalogIn57644MfAddr_Type = OctetString
_WtWebGraphAnalogIn57644MfAddr_Object = MibScalar
wtWebGraphAnalogIn57644MfAddr = _WtWebGraphAnalogIn57644MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 2),
    _WtWebGraphAnalogIn57644MfAddr_Type()
)
wtWebGraphAnalogIn57644MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57644MfHotline_Type = OctetString
_WtWebGraphAnalogIn57644MfHotline_Object = MibScalar
wtWebGraphAnalogIn57644MfHotline = _WtWebGraphAnalogIn57644MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 3),
    _WtWebGraphAnalogIn57644MfHotline_Type()
)
wtWebGraphAnalogIn57644MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfHotline.setStatus("mandatory")
_WtWebGraphAnalogIn57644MfInternet_Type = OctetString
_WtWebGraphAnalogIn57644MfInternet_Object = MibScalar
wtWebGraphAnalogIn57644MfInternet = _WtWebGraphAnalogIn57644MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 4),
    _WtWebGraphAnalogIn57644MfInternet_Type()
)
wtWebGraphAnalogIn57644MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfInternet.setStatus("mandatory")
_WtWebGraphAnalogIn57644MfDeviceTyp_Type = OctetString
_WtWebGraphAnalogIn57644MfDeviceTyp_Object = MibScalar
wtWebGraphAnalogIn57644MfDeviceTyp = _WtWebGraphAnalogIn57644MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 5),
    _WtWebGraphAnalogIn57644MfDeviceTyp_Type()
)
wtWebGraphAnalogIn57644MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalogIn57644MfOrderNo_Type = OctetString
_WtWebGraphAnalogIn57644MfOrderNo_Object = MibScalar
wtWebGraphAnalogIn57644MfOrderNo = _WtWebGraphAnalogIn57644MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 6),
    _WtWebGraphAnalogIn57644MfOrderNo_Type()
)
wtWebGraphAnalogIn57644MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalogIn57644Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57644Diag = _WtWebGraphAnalogIn57644Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4)
)
_WtWebGraphAnalogIn57644DiagErrorCount_Type = Integer32
_WtWebGraphAnalogIn57644DiagErrorCount_Object = MibScalar
wtWebGraphAnalogIn57644DiagErrorCount = _WtWebGraphAnalogIn57644DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 1),
    _WtWebGraphAnalogIn57644DiagErrorCount_Type()
)
wtWebGraphAnalogIn57644DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalogIn57644DiagBinaryError_Type = OctetString
_WtWebGraphAnalogIn57644DiagBinaryError_Object = MibScalar
wtWebGraphAnalogIn57644DiagBinaryError = _WtWebGraphAnalogIn57644DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 2),
    _WtWebGraphAnalogIn57644DiagBinaryError_Type()
)
wtWebGraphAnalogIn57644DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalogIn57644DiagErrorIndex_Type = Integer32
_WtWebGraphAnalogIn57644DiagErrorIndex_Object = MibScalar
wtWebGraphAnalogIn57644DiagErrorIndex = _WtWebGraphAnalogIn57644DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 3),
    _WtWebGraphAnalogIn57644DiagErrorIndex_Type()
)
wtWebGraphAnalogIn57644DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalogIn57644DiagErrorMessage_Type = OctetString
_WtWebGraphAnalogIn57644DiagErrorMessage_Object = MibScalar
wtWebGraphAnalogIn57644DiagErrorMessage = _WtWebGraphAnalogIn57644DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 4),
    _WtWebGraphAnalogIn57644DiagErrorMessage_Type()
)
wtWebGraphAnalogIn57644DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalogIn57644DiagErrorClear_Type = Integer32
_WtWebGraphAnalogIn57644DiagErrorClear_Object = MibScalar
wtWebGraphAnalogIn57644DiagErrorClear = _WtWebGraphAnalogIn57644DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 5),
    _WtWebGraphAnalogIn57644DiagErrorClear_Type()
)
wtWebGraphAnalogIn57644DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalogIn57644Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 31)
)
wtWebGraphAnalogIn57644Alert1.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert1.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 32)
)
wtWebGraphAnalogIn57644Alert2.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert2.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 33)
)
wtWebGraphAnalogIn57644Alert3.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert3.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 34)
)
wtWebGraphAnalogIn57644Alert4.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert4.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 35)
)
wtWebGraphAnalogIn57644Alert5.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert5.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 36)
)
wtWebGraphAnalogIn57644Alert6.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert6.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 37)
)
wtWebGraphAnalogIn57644Alert7.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert7.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 38)
)
wtWebGraphAnalogIn57644Alert8.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert8.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 91)
)
wtWebGraphAnalogIn57644Alert9.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert9.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 92)
)
wtWebGraphAnalogIn57644Alert10.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert10.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 93)
)
wtWebGraphAnalogIn57644Alert11.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert11.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 94)
)
wtWebGraphAnalogIn57644Alert12.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert12.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 95)
)
wtWebGraphAnalogIn57644Alert13.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert13.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 96)
)
wtWebGraphAnalogIn57644Alert14.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert14.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 97)
)
wtWebGraphAnalogIn57644Alert15.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert15.setStatus(
        ""
    )

wtWebGraphAnalogIn57644Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 98)
)
wtWebGraphAnalogIn57644Alert16.setObjects(
    ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644Alert16.setStatus(
        ""
    )

wtWebGraphAnalogIn57644AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 110)
)
wtWebGraphAnalogIn57644AlertDiag.setObjects(
      *(("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644DiagErrorIndex"),
        ("WebGraph-AnalogIn-57644-US-MIB", "wtWebGraphAnalogIn57644DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57644AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIn-57644-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalogIn57644": wtWebGraphAnalogIn57644,
       "wtWebGraphAnalogIn57644Alert1": wtWebGraphAnalogIn57644Alert1,
       "wtWebGraphAnalogIn57644Alert2": wtWebGraphAnalogIn57644Alert2,
       "wtWebGraphAnalogIn57644Alert3": wtWebGraphAnalogIn57644Alert3,
       "wtWebGraphAnalogIn57644Alert4": wtWebGraphAnalogIn57644Alert4,
       "wtWebGraphAnalogIn57644Alert5": wtWebGraphAnalogIn57644Alert5,
       "wtWebGraphAnalogIn57644Alert6": wtWebGraphAnalogIn57644Alert6,
       "wtWebGraphAnalogIn57644Alert7": wtWebGraphAnalogIn57644Alert7,
       "wtWebGraphAnalogIn57644Alert8": wtWebGraphAnalogIn57644Alert8,
       "wtWebGraphAnalogIn57644Alert9": wtWebGraphAnalogIn57644Alert9,
       "wtWebGraphAnalogIn57644Alert10": wtWebGraphAnalogIn57644Alert10,
       "wtWebGraphAnalogIn57644Alert11": wtWebGraphAnalogIn57644Alert11,
       "wtWebGraphAnalogIn57644Alert12": wtWebGraphAnalogIn57644Alert12,
       "wtWebGraphAnalogIn57644Alert13": wtWebGraphAnalogIn57644Alert13,
       "wtWebGraphAnalogIn57644Alert14": wtWebGraphAnalogIn57644Alert14,
       "wtWebGraphAnalogIn57644Alert15": wtWebGraphAnalogIn57644Alert15,
       "wtWebGraphAnalogIn57644Alert16": wtWebGraphAnalogIn57644Alert16,
       "wtWebGraphAnalogIn57644AlertDiag": wtWebGraphAnalogIn57644AlertDiag,
       "wtWebGraphAnalogIn57644Inventory": wtWebGraphAnalogIn57644Inventory,
       "wtWebGraphAnalogIn57644Sensors": wtWebGraphAnalogIn57644Sensors,
       "wtWebGraphAnalogIn57644SensorTable": wtWebGraphAnalogIn57644SensorTable,
       "wtWebGraphAnalogIn57644SensorEntry": wtWebGraphAnalogIn57644SensorEntry,
       "wtWebGraphAnalogIn57644SensorNo": wtWebGraphAnalogIn57644SensorNo,
       "wtWebGraphAnalogIn57644ValuesTable": wtWebGraphAnalogIn57644ValuesTable,
       "wtWebGraphAnalogIn57644ValuesEntry": wtWebGraphAnalogIn57644ValuesEntry,
       "wtWebGraphAnalogIn57644Values": wtWebGraphAnalogIn57644Values,
       "wtWebGraphAnalogIn57644BinaryValuesTable": wtWebGraphAnalogIn57644BinaryValuesTable,
       "wtWebGraphAnalogIn57644BinaryValuesEntry": wtWebGraphAnalogIn57644BinaryValuesEntry,
       "wtWebGraphAnalogIn57644BinaryValues": wtWebGraphAnalogIn57644BinaryValues,
       "wtWebGraphAnalogIn57644SessCntrl": wtWebGraphAnalogIn57644SessCntrl,
       "wtWebGraphAnalogIn57644SessCntrlPassword": wtWebGraphAnalogIn57644SessCntrlPassword,
       "wtWebGraphAnalogIn57644SessCntrlConfigMode": wtWebGraphAnalogIn57644SessCntrlConfigMode,
       "wtWebGraphAnalogIn57644SessCntrlLogout": wtWebGraphAnalogIn57644SessCntrlLogout,
       "wtWebGraphAnalogIn57644SessCntrlAdminPassword": wtWebGraphAnalogIn57644SessCntrlAdminPassword,
       "wtWebGraphAnalogIn57644SessCntrlConfigPassword": wtWebGraphAnalogIn57644SessCntrlConfigPassword,
       "wtWebGraphAnalogIn57644Config": wtWebGraphAnalogIn57644Config,
       "wtWebGraphAnalogIn57644Device": wtWebGraphAnalogIn57644Device,
       "wtWebGraphAnalogIn57644Text": wtWebGraphAnalogIn57644Text,
       "wtWebGraphAnalogIn57644DeviceName": wtWebGraphAnalogIn57644DeviceName,
       "wtWebGraphAnalogIn57644DeviceText": wtWebGraphAnalogIn57644DeviceText,
       "wtWebGraphAnalogIn57644DeviceLocation": wtWebGraphAnalogIn57644DeviceLocation,
       "wtWebGraphAnalogIn57644DeviceContact": wtWebGraphAnalogIn57644DeviceContact,
       "wtWebGraphAnalogIn57644TimeDate": wtWebGraphAnalogIn57644TimeDate,
       "wtWebGraphAnalogIn57644TimeZone": wtWebGraphAnalogIn57644TimeZone,
       "wtWebGraphAnalogIn57644TzOffsetHrs": wtWebGraphAnalogIn57644TzOffsetHrs,
       "wtWebGraphAnalogIn57644TzOffsetMin": wtWebGraphAnalogIn57644TzOffsetMin,
       "wtWebGraphAnalogIn57644TzEnable": wtWebGraphAnalogIn57644TzEnable,
       "wtWebGraphAnalogIn57644StTzOffsetHrs": wtWebGraphAnalogIn57644StTzOffsetHrs,
       "wtWebGraphAnalogIn57644StTzOffsetMin": wtWebGraphAnalogIn57644StTzOffsetMin,
       "wtWebGraphAnalogIn57644StTzEnable": wtWebGraphAnalogIn57644StTzEnable,
       "wtWebGraphAnalogIn57644StTzStartMonth": wtWebGraphAnalogIn57644StTzStartMonth,
       "wtWebGraphAnalogIn57644StTzStartMode": wtWebGraphAnalogIn57644StTzStartMode,
       "wtWebGraphAnalogIn57644StTzStartWday": wtWebGraphAnalogIn57644StTzStartWday,
       "wtWebGraphAnalogIn57644StTzStartHrs": wtWebGraphAnalogIn57644StTzStartHrs,
       "wtWebGraphAnalogIn57644StTzStartMin": wtWebGraphAnalogIn57644StTzStartMin,
       "wtWebGraphAnalogIn57644StTzStopMonth": wtWebGraphAnalogIn57644StTzStopMonth,
       "wtWebGraphAnalogIn57644StTzStopMode": wtWebGraphAnalogIn57644StTzStopMode,
       "wtWebGraphAnalogIn57644StTzStopWday": wtWebGraphAnalogIn57644StTzStopWday,
       "wtWebGraphAnalogIn57644StTzStopHrs": wtWebGraphAnalogIn57644StTzStopHrs,
       "wtWebGraphAnalogIn57644StTzStopMin": wtWebGraphAnalogIn57644StTzStopMin,
       "wtWebGraphAnalogIn57644TimeServer": wtWebGraphAnalogIn57644TimeServer,
       "wtWebGraphAnalogIn57644TimeServer1": wtWebGraphAnalogIn57644TimeServer1,
       "wtWebGraphAnalogIn57644TimeServer2": wtWebGraphAnalogIn57644TimeServer2,
       "wtWebGraphAnalogIn57644TsEnable": wtWebGraphAnalogIn57644TsEnable,
       "wtWebGraphAnalogIn57644TsSyncTime": wtWebGraphAnalogIn57644TsSyncTime,
       "wtWebGraphAnalogIn57644DeviceClock": wtWebGraphAnalogIn57644DeviceClock,
       "wtWebGraphAnalogIn57644ClockHrs": wtWebGraphAnalogIn57644ClockHrs,
       "wtWebGraphAnalogIn57644ClockMin": wtWebGraphAnalogIn57644ClockMin,
       "wtWebGraphAnalogIn57644ClockDay": wtWebGraphAnalogIn57644ClockDay,
       "wtWebGraphAnalogIn57644ClockMonth": wtWebGraphAnalogIn57644ClockMonth,
       "wtWebGraphAnalogIn57644ClockYear": wtWebGraphAnalogIn57644ClockYear,
       "wtWebGraphAnalogIn57644Basic": wtWebGraphAnalogIn57644Basic,
       "wtWebGraphAnalogIn57644Network": wtWebGraphAnalogIn57644Network,
       "wtWebGraphAnalogIn57644IpAddress": wtWebGraphAnalogIn57644IpAddress,
       "wtWebGraphAnalogIn57644SubnetMask": wtWebGraphAnalogIn57644SubnetMask,
       "wtWebGraphAnalogIn57644Gateway": wtWebGraphAnalogIn57644Gateway,
       "wtWebGraphAnalogIn57644DnsServer1": wtWebGraphAnalogIn57644DnsServer1,
       "wtWebGraphAnalogIn57644DnsServer2": wtWebGraphAnalogIn57644DnsServer2,
       "wtWebGraphAnalogIn57644AddConfig": wtWebGraphAnalogIn57644AddConfig,
       "wtWebGraphAnalogIn57644HTTP": wtWebGraphAnalogIn57644HTTP,
       "wtWebGraphAnalogIn57644Startup": wtWebGraphAnalogIn57644Startup,
       "wtWebGraphAnalogIn57644GetHeaderEnable": wtWebGraphAnalogIn57644GetHeaderEnable,
       "wtWebGraphAnalogIn57644HttpPort": wtWebGraphAnalogIn57644HttpPort,
       "wtWebGraphAnalogIn57644Mail": wtWebGraphAnalogIn57644Mail,
       "wtWebGraphAnalogIn57644MailAdName": wtWebGraphAnalogIn57644MailAdName,
       "wtWebGraphAnalogIn57644MailReply": wtWebGraphAnalogIn57644MailReply,
       "wtWebGraphAnalogIn57644MailServer": wtWebGraphAnalogIn57644MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalogIn57644MailAuthentication": wtWebGraphAnalogIn57644MailAuthentication,
       "wtWebGraphAnalogIn57644MailAuthUser": wtWebGraphAnalogIn57644MailAuthUser,
       "wtWebGraphAnalogIn57644MailAuthPassword": wtWebGraphAnalogIn57644MailAuthPassword,
       "wtWebGraphAnalogIn57644MailPop3Server": wtWebGraphAnalogIn57644MailPop3Server,
       "wtWebGraphAnalogIn57644SNMP": wtWebGraphAnalogIn57644SNMP,
       "wtWebGraphAnalogIn57644SnmpCommunityStringRead": wtWebGraphAnalogIn57644SnmpCommunityStringRead,
       "wtWebGraphAnalogIn57644SnmpCommunityStringReadWrite": wtWebGraphAnalogIn57644SnmpCommunityStringReadWrite,
       "wtWebGraphAnalogIn57644SystemTrapManagerIP": wtWebGraphAnalogIn57644SystemTrapManagerIP,
       "wtWebGraphAnalogIn57644SystemTrapEnable": wtWebGraphAnalogIn57644SystemTrapEnable,
       "wtWebGraphAnalogIn57644SnmpEnable": wtWebGraphAnalogIn57644SnmpEnable,
       "wtWebGraphAnalogIn57644SnmpCommunityStringTrap": wtWebGraphAnalogIn57644SnmpCommunityStringTrap,
       "wtWebGraphAnalogIn57644UDP": wtWebGraphAnalogIn57644UDP,
       "wtWebGraphAnalogIn57644UdpPort": wtWebGraphAnalogIn57644UdpPort,
       "wtWebGraphAnalogIn57644UdpEnable": wtWebGraphAnalogIn57644UdpEnable,
       "wtWebGraphAnalogIn57644Syslog": wtWebGraphAnalogIn57644Syslog,
       "wtWebGraphAnalogIn57644SyslogServerIP": wtWebGraphAnalogIn57644SyslogServerIP,
       "wtWebGraphAnalogIn57644SyslogServerPort": wtWebGraphAnalogIn57644SyslogServerPort,
       "wtWebGraphAnalogIn57644SyslogSystemMessagesEnable": wtWebGraphAnalogIn57644SyslogSystemMessagesEnable,
       "wtWebGraphAnalogIn57644SyslogEnable": wtWebGraphAnalogIn57644SyslogEnable,
       "wtWebGraphAnalogIn57644FTP": wtWebGraphAnalogIn57644FTP,
       "wtWebGraphAnalogIn57644FTPServerIP": wtWebGraphAnalogIn57644FTPServerIP,
       "wtWebGraphAnalogIn57644FTPServerControlPort": wtWebGraphAnalogIn57644FTPServerControlPort,
       "wtWebGraphAnalogIn57644FTPUserName": wtWebGraphAnalogIn57644FTPUserName,
       "wtWebGraphAnalogIn57644FTPPassword": wtWebGraphAnalogIn57644FTPPassword,
       "wtWebGraphAnalogIn57644FTPAccount": wtWebGraphAnalogIn57644FTPAccount,
       "wtWebGraphAnalogIn57644FTPOption": wtWebGraphAnalogIn57644FTPOption,
       "wtWebGraphAnalogIn57644FTPEnable": wtWebGraphAnalogIn57644FTPEnable,
       "wtWebGraphAnalogIn57644Datalogger": wtWebGraphAnalogIn57644Datalogger,
       "wtWebGraphAnalogIn57644LoggerTimebase": wtWebGraphAnalogIn57644LoggerTimebase,
       "wtWebGraphAnalogIn57644LoggerSensorSel": wtWebGraphAnalogIn57644LoggerSensorSel,
       "wtWebGraphAnalogIn57644DisplaySensorSel": wtWebGraphAnalogIn57644DisplaySensorSel,
       "wtWebGraphAnalogIn57644SensorColorTable": wtWebGraphAnalogIn57644SensorColorTable,
       "wtWebGraphAnalogIn57644SensorColorEntry": wtWebGraphAnalogIn57644SensorColorEntry,
       "wtWebGraphAnalogIn57644SensorColor": wtWebGraphAnalogIn57644SensorColor,
       "wtWebGraphAnalogIn57644AutoScaleEnable": wtWebGraphAnalogIn57644AutoScaleEnable,
       "wtWebGraphAnalogIn57644VerticalUpperLimit": wtWebGraphAnalogIn57644VerticalUpperLimit,
       "wtWebGraphAnalogIn57644VerticalLowerLimit": wtWebGraphAnalogIn57644VerticalLowerLimit,
       "wtWebGraphAnalogIn57644HorizontalZoom": wtWebGraphAnalogIn57644HorizontalZoom,
       "wtWebGraphAnalogIn57644Alarm": wtWebGraphAnalogIn57644Alarm,
       "wtWebGraphAnalogIn57644AlarmCount": wtWebGraphAnalogIn57644AlarmCount,
       "wtWebGraphAnalogIn57644AlarmIfTable": wtWebGraphAnalogIn57644AlarmIfTable,
       "wtWebGraphAnalogIn57644AlarmIfEntry": wtWebGraphAnalogIn57644AlarmIfEntry,
       "wtWebGraphAnalogIn57644AlarmNo": wtWebGraphAnalogIn57644AlarmNo,
       "wtWebGraphAnalogIn57644AlarmTable": wtWebGraphAnalogIn57644AlarmTable,
       "wtWebGraphAnalogIn57644AlarmEntry": wtWebGraphAnalogIn57644AlarmEntry,
       "wtWebGraphAnalogIn57644AlarmTrigger": wtWebGraphAnalogIn57644AlarmTrigger,
       "wtWebGraphAnalogIn57644AlarmMin": wtWebGraphAnalogIn57644AlarmMin,
       "wtWebGraphAnalogIn57644AlarmMax": wtWebGraphAnalogIn57644AlarmMax,
       "wtWebGraphAnalogIn57644AlarmHysteresis": wtWebGraphAnalogIn57644AlarmHysteresis,
       "wtWebGraphAnalogIn57644AlarmDelay": wtWebGraphAnalogIn57644AlarmDelay,
       "wtWebGraphAnalogIn57644AlarmInterval": wtWebGraphAnalogIn57644AlarmInterval,
       "wtWebGraphAnalogIn57644AlarmEnable": wtWebGraphAnalogIn57644AlarmEnable,
       "wtWebGraphAnalogIn57644AlarmEMailAddr": wtWebGraphAnalogIn57644AlarmEMailAddr,
       "wtWebGraphAnalogIn57644AlarmMailSubject": wtWebGraphAnalogIn57644AlarmMailSubject,
       "wtWebGraphAnalogIn57644AlarmMailText": wtWebGraphAnalogIn57644AlarmMailText,
       "wtWebGraphAnalogIn57644AlarmManagerIP": wtWebGraphAnalogIn57644AlarmManagerIP,
       "wtWebGraphAnalogIn57644AlarmTrapText": wtWebGraphAnalogIn57644AlarmTrapText,
       "wtWebGraphAnalogIn57644AlarmMailOptions": wtWebGraphAnalogIn57644AlarmMailOptions,
       "wtWebGraphAnalogIn57644AlarmTcpIpAddr": wtWebGraphAnalogIn57644AlarmTcpIpAddr,
       "wtWebGraphAnalogIn57644AlarmTcpPort": wtWebGraphAnalogIn57644AlarmTcpPort,
       "wtWebGraphAnalogIn57644AlarmTcpText": wtWebGraphAnalogIn57644AlarmTcpText,
       "wtWebGraphAnalogIn57644AlarmClearMailSubject": wtWebGraphAnalogIn57644AlarmClearMailSubject,
       "wtWebGraphAnalogIn57644AlarmClearMailText": wtWebGraphAnalogIn57644AlarmClearMailText,
       "wtWebGraphAnalogIn57644AlarmClearTrapText": wtWebGraphAnalogIn57644AlarmClearTrapText,
       "wtWebGraphAnalogIn57644AlarmClearTcpText": wtWebGraphAnalogIn57644AlarmClearTcpText,
       "wtWebGraphAnalogIn57644Alarm2Min": wtWebGraphAnalogIn57644Alarm2Min,
       "wtWebGraphAnalogIn57644Alarm2Max": wtWebGraphAnalogIn57644Alarm2Max,
       "wtWebGraphAnalogIn57644Alarm2Hysteresis": wtWebGraphAnalogIn57644Alarm2Hysteresis,
       "wtWebGraphAnalogIn57644AlarmSyslogIpAddr": wtWebGraphAnalogIn57644AlarmSyslogIpAddr,
       "wtWebGraphAnalogIn57644AlarmSyslogPort": wtWebGraphAnalogIn57644AlarmSyslogPort,
       "wtWebGraphAnalogIn57644AlarmSyslogText": wtWebGraphAnalogIn57644AlarmSyslogText,
       "wtWebGraphAnalogIn57644AlarmSyslogClearText": wtWebGraphAnalogIn57644AlarmSyslogClearText,
       "wtWebGraphAnalogIn57644AlarmFtpDataPort": wtWebGraphAnalogIn57644AlarmFtpDataPort,
       "wtWebGraphAnalogIn57644AlarmFtpFileName": wtWebGraphAnalogIn57644AlarmFtpFileName,
       "wtWebGraphAnalogIn57644AlarmFtpText": wtWebGraphAnalogIn57644AlarmFtpText,
       "wtWebGraphAnalogIn57644AlarmFtpClearText": wtWebGraphAnalogIn57644AlarmFtpClearText,
       "wtWebGraphAnalogIn57644AlarmFtpOption": wtWebGraphAnalogIn57644AlarmFtpOption,
       "wtWebGraphAnalogIn57644AlarmTimerCron": wtWebGraphAnalogIn57644AlarmTimerCron,
       "wtWebGraphAnalogIn57644Graphics": wtWebGraphAnalogIn57644Graphics,
       "wtWebGraphAnalogIn57644GraphicsBase": wtWebGraphAnalogIn57644GraphicsBase,
       "wtWebGraphAnalogIn57644GraphicsBaseEnable": wtWebGraphAnalogIn57644GraphicsBaseEnable,
       "wtWebGraphAnalogIn57644GraphicsBaseWidth": wtWebGraphAnalogIn57644GraphicsBaseWidth,
       "wtWebGraphAnalogIn57644GraphicsBaseHeight": wtWebGraphAnalogIn57644GraphicsBaseHeight,
       "wtWebGraphAnalogIn57644GraphicsBaseFrameColor": wtWebGraphAnalogIn57644GraphicsBaseFrameColor,
       "wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor": wtWebGraphAnalogIn57644GraphicsBaseBackgroundColor,
       "wtWebGraphAnalogIn57644GraphicsBasePollingrate": wtWebGraphAnalogIn57644GraphicsBasePollingrate,
       "wtWebGraphAnalogIn57644GraphicsSelect": wtWebGraphAnalogIn57644GraphicsSelect,
       "wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel": wtWebGraphAnalogIn57644GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem": wtWebGraphAnalogIn57644GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalogIn57644SensorColor2Table": wtWebGraphAnalogIn57644SensorColor2Table,
       "wtWebGraphAnalogIn57644SensorColor2Entry": wtWebGraphAnalogIn57644SensorColor2Entry,
       "wtWebGraphAnalogIn57644GraphicsSensorColor": wtWebGraphAnalogIn57644GraphicsSensorColor,
       "wtWebGraphAnalogIn57644GraphicsSelectScale": wtWebGraphAnalogIn57644GraphicsSelectScale,
       "wtWebGraphAnalogIn57644GraphicsScale": wtWebGraphAnalogIn57644GraphicsScale,
       "wtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable": wtWebGraphAnalogIn57644GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable": wtWebGraphAnalogIn57644GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalogIn57644GraphicsScale1Min": wtWebGraphAnalogIn57644GraphicsScale1Min,
       "wtWebGraphAnalogIn57644GraphicsScale2Min": wtWebGraphAnalogIn57644GraphicsScale2Min,
       "wtWebGraphAnalogIn57644GraphicsScale3Min": wtWebGraphAnalogIn57644GraphicsScale3Min,
       "wtWebGraphAnalogIn57644GraphicsScale4Min": wtWebGraphAnalogIn57644GraphicsScale4Min,
       "wtWebGraphAnalogIn57644GraphicsScale1Max": wtWebGraphAnalogIn57644GraphicsScale1Max,
       "wtWebGraphAnalogIn57644GraphicsScale2Max": wtWebGraphAnalogIn57644GraphicsScale2Max,
       "wtWebGraphAnalogIn57644GraphicsScale3Max": wtWebGraphAnalogIn57644GraphicsScale3Max,
       "wtWebGraphAnalogIn57644GraphicsScale4Max": wtWebGraphAnalogIn57644GraphicsScale4Max,
       "wtWebGraphAnalogIn57644GraphicsScale1Unit": wtWebGraphAnalogIn57644GraphicsScale1Unit,
       "wtWebGraphAnalogIn57644GraphicsScale2Unit": wtWebGraphAnalogIn57644GraphicsScale2Unit,
       "wtWebGraphAnalogIn57644GraphicsScale3Unit": wtWebGraphAnalogIn57644GraphicsScale3Unit,
       "wtWebGraphAnalogIn57644GraphicsScale4Unit": wtWebGraphAnalogIn57644GraphicsScale4Unit,
       "wtWebGraphAnalogIn57644Ports": wtWebGraphAnalogIn57644Ports,
       "wtWebGraphAnalogIn57644PortTable": wtWebGraphAnalogIn57644PortTable,
       "wtWebGraphAnalogIn57644PortEntry": wtWebGraphAnalogIn57644PortEntry,
       "wtWebGraphAnalogIn57644PortName": wtWebGraphAnalogIn57644PortName,
       "wtWebGraphAnalogIn57644PortText": wtWebGraphAnalogIn57644PortText,
       "wtWebGraphAnalogIn57644PortOffset1": wtWebGraphAnalogIn57644PortOffset1,
       "wtWebGraphAnalogIn57644SetPoint1": wtWebGraphAnalogIn57644SetPoint1,
       "wtWebGraphAnalogIn57644PortOffset2": wtWebGraphAnalogIn57644PortOffset2,
       "wtWebGraphAnalogIn57644SetPoint2": wtWebGraphAnalogIn57644SetPoint2,
       "wtWebGraphAnalogIn57644PortComment": wtWebGraphAnalogIn57644PortComment,
       "wtWebGraphAnalogIn57644PortSensorSelect": wtWebGraphAnalogIn57644PortSensorSelect,
       "wtWebGraphAnalogIn57644PortUnit": wtWebGraphAnalogIn57644PortUnit,
       "wtWebGraphAnalogIn57644PortScale0": wtWebGraphAnalogIn57644PortScale0,
       "wtWebGraphAnalogIn57644PortScale100": wtWebGraphAnalogIn57644PortScale100,
       "wtWebGraphAnalogIn57644Manufact": wtWebGraphAnalogIn57644Manufact,
       "wtWebGraphAnalogIn57644MfName": wtWebGraphAnalogIn57644MfName,
       "wtWebGraphAnalogIn57644MfAddr": wtWebGraphAnalogIn57644MfAddr,
       "wtWebGraphAnalogIn57644MfHotline": wtWebGraphAnalogIn57644MfHotline,
       "wtWebGraphAnalogIn57644MfInternet": wtWebGraphAnalogIn57644MfInternet,
       "wtWebGraphAnalogIn57644MfDeviceTyp": wtWebGraphAnalogIn57644MfDeviceTyp,
       "wtWebGraphAnalogIn57644MfOrderNo": wtWebGraphAnalogIn57644MfOrderNo,
       "wtWebGraphAnalogIn57644Diag": wtWebGraphAnalogIn57644Diag,
       "wtWebGraphAnalogIn57644DiagErrorCount": wtWebGraphAnalogIn57644DiagErrorCount,
       "wtWebGraphAnalogIn57644DiagBinaryError": wtWebGraphAnalogIn57644DiagBinaryError,
       "wtWebGraphAnalogIn57644DiagErrorIndex": wtWebGraphAnalogIn57644DiagErrorIndex,
       "wtWebGraphAnalogIn57644DiagErrorMessage": wtWebGraphAnalogIn57644DiagErrorMessage,
       "wtWebGraphAnalogIn57644DiagErrorClear": wtWebGraphAnalogIn57644DiagErrorClear}
)
