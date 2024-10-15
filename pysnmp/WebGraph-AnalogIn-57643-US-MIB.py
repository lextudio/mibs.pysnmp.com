# SNMP MIB module (WebGraph-AnalogIn-57643-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-AnalogIn-57643-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:36 2024
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
_WtWebGraphAnalogIn57643_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643 = _WtWebGraphAnalogIn57643_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12)
)
_WtWebGraphAnalogIn57643Inventory_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Inventory = _WtWebGraphAnalogIn57643Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1)
)


class _WtWebGraphAnalogIn57643Sensors_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643Sensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57643Sensors_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643Sensors_Object = MibScalar
wtWebGraphAnalogIn57643Sensors = _WtWebGraphAnalogIn57643Sensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 1),
    _WtWebGraphAnalogIn57643Sensors_Type()
)
wtWebGraphAnalogIn57643Sensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Sensors.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorTable_Object = MibTable
wtWebGraphAnalogIn57643SensorTable = _WtWebGraphAnalogIn57643SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorEntry_Object = MibTableRow
wtWebGraphAnalogIn57643SensorEntry = _WtWebGraphAnalogIn57643SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2, 1)
)
wtWebGraphAnalogIn57643SensorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643SensorNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643SensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAnalogIn57643SensorNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643SensorNo_Object = MibTableColumn
wtWebGraphAnalogIn57643SensorNo = _WtWebGraphAnalogIn57643SensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57643SensorNo_Type()
)
wtWebGraphAnalogIn57643SensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorNo.setStatus("mandatory")
_WtWebGraphAnalogIn57643ValuesTable_Object = MibTable
wtWebGraphAnalogIn57643ValuesTable = _WtWebGraphAnalogIn57643ValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643ValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57643ValuesEntry = _WtWebGraphAnalogIn57643ValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3, 1)
)
wtWebGraphAnalogIn57643ValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ValuesEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643Values_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643Values based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAnalogIn57643Values_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643Values_Object = MibTableColumn
wtWebGraphAnalogIn57643Values = _WtWebGraphAnalogIn57643Values_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57643Values_Type()
)
wtWebGraphAnalogIn57643Values.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Values.setStatus("mandatory")
_WtWebGraphAnalogIn57643BinaryValuesTable_Object = MibTable
wtWebGraphAnalogIn57643BinaryValuesTable = _WtWebGraphAnalogIn57643BinaryValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643BinaryValuesTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643BinaryValuesEntry_Object = MibTableRow
wtWebGraphAnalogIn57643BinaryValuesEntry = _WtWebGraphAnalogIn57643BinaryValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4, 1)
)
wtWebGraphAnalogIn57643BinaryValuesEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643BinaryValuesEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57643BinaryValues_Type = Integer32
_WtWebGraphAnalogIn57643BinaryValues_Object = MibTableColumn
wtWebGraphAnalogIn57643BinaryValues = _WtWebGraphAnalogIn57643BinaryValues_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 1, 4, 1, 1),
    _WtWebGraphAnalogIn57643BinaryValues_Type()
)
wtWebGraphAnalogIn57643BinaryValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643BinaryValues.setStatus("mandatory")
_WtWebGraphAnalogIn57643SessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643SessCntrl = _WtWebGraphAnalogIn57643SessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2)
)
_WtWebGraphAnalogIn57643SessCntrlPassword_Type = OctetString
_WtWebGraphAnalogIn57643SessCntrlPassword_Object = MibScalar
wtWebGraphAnalogIn57643SessCntrlPassword = _WtWebGraphAnalogIn57643SessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 1),
    _WtWebGraphAnalogIn57643SessCntrlPassword_Type()
)
wtWebGraphAnalogIn57643SessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAnalogIn57643SessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643SessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAnalogIn57643SessCntrl-NoSession", 0),
          ("wtWebGraphAnalogIn57643SessCntrl-Session", 1))
    )


_WtWebGraphAnalogIn57643SessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643SessCntrlConfigMode_Object = MibScalar
wtWebGraphAnalogIn57643SessCntrlConfigMode = _WtWebGraphAnalogIn57643SessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 2),
    _WtWebGraphAnalogIn57643SessCntrlConfigMode_Type()
)
wtWebGraphAnalogIn57643SessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAnalogIn57643SessCntrlLogout_Type = Integer32
_WtWebGraphAnalogIn57643SessCntrlLogout_Object = MibScalar
wtWebGraphAnalogIn57643SessCntrlLogout = _WtWebGraphAnalogIn57643SessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 3),
    _WtWebGraphAnalogIn57643SessCntrlLogout_Type()
)
wtWebGraphAnalogIn57643SessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SessCntrlLogout.setStatus("mandatory")
_WtWebGraphAnalogIn57643SessCntrlAdminPassword_Type = OctetString
_WtWebGraphAnalogIn57643SessCntrlAdminPassword_Object = MibScalar
wtWebGraphAnalogIn57643SessCntrlAdminPassword = _WtWebGraphAnalogIn57643SessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 4),
    _WtWebGraphAnalogIn57643SessCntrlAdminPassword_Type()
)
wtWebGraphAnalogIn57643SessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57643SessCntrlConfigPassword_Type = OctetString
_WtWebGraphAnalogIn57643SessCntrlConfigPassword_Object = MibScalar
wtWebGraphAnalogIn57643SessCntrlConfigPassword = _WtWebGraphAnalogIn57643SessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 2, 5),
    _WtWebGraphAnalogIn57643SessCntrlConfigPassword_Type()
)
wtWebGraphAnalogIn57643SessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57643Config_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Config = _WtWebGraphAnalogIn57643Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3)
)
_WtWebGraphAnalogIn57643Device_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Device = _WtWebGraphAnalogIn57643Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1)
)
_WtWebGraphAnalogIn57643Text_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Text = _WtWebGraphAnalogIn57643Text_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1)
)
_WtWebGraphAnalogIn57643DeviceName_Type = OctetString
_WtWebGraphAnalogIn57643DeviceName_Object = MibScalar
wtWebGraphAnalogIn57643DeviceName = _WtWebGraphAnalogIn57643DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 1),
    _WtWebGraphAnalogIn57643DeviceName_Type()
)
wtWebGraphAnalogIn57643DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DeviceName.setStatus("mandatory")
_WtWebGraphAnalogIn57643DeviceText_Type = OctetString
_WtWebGraphAnalogIn57643DeviceText_Object = MibScalar
wtWebGraphAnalogIn57643DeviceText = _WtWebGraphAnalogIn57643DeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 2),
    _WtWebGraphAnalogIn57643DeviceText_Type()
)
wtWebGraphAnalogIn57643DeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DeviceText.setStatus("mandatory")
_WtWebGraphAnalogIn57643DeviceLocation_Type = OctetString
_WtWebGraphAnalogIn57643DeviceLocation_Object = MibScalar
wtWebGraphAnalogIn57643DeviceLocation = _WtWebGraphAnalogIn57643DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 3),
    _WtWebGraphAnalogIn57643DeviceLocation_Type()
)
wtWebGraphAnalogIn57643DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DeviceLocation.setStatus("mandatory")
_WtWebGraphAnalogIn57643DeviceContact_Type = OctetString
_WtWebGraphAnalogIn57643DeviceContact_Object = MibScalar
wtWebGraphAnalogIn57643DeviceContact = _WtWebGraphAnalogIn57643DeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 1, 4),
    _WtWebGraphAnalogIn57643DeviceContact_Type()
)
wtWebGraphAnalogIn57643DeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DeviceContact.setStatus("mandatory")
_WtWebGraphAnalogIn57643TimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643TimeDate = _WtWebGraphAnalogIn57643TimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2)
)
_WtWebGraphAnalogIn57643TimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643TimeZone = _WtWebGraphAnalogIn57643TimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1)
)
_WtWebGraphAnalogIn57643TzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57643TzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57643TzOffsetHrs = _WtWebGraphAnalogIn57643TzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 1),
    _WtWebGraphAnalogIn57643TzOffsetHrs_Type()
)
wtWebGraphAnalogIn57643TzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57643TzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57643TzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57643TzOffsetMin = _WtWebGraphAnalogIn57643TzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 2),
    _WtWebGraphAnalogIn57643TzOffsetMin_Type()
)
wtWebGraphAnalogIn57643TzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57643TzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643TzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643TzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643TzEnable_Object = MibScalar
wtWebGraphAnalogIn57643TzEnable = _WtWebGraphAnalogIn57643TzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 3),
    _WtWebGraphAnalogIn57643TzEnable_Type()
)
wtWebGraphAnalogIn57643TzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TzEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzOffsetHrs_Type = Integer32
_WtWebGraphAnalogIn57643StTzOffsetHrs_Object = MibScalar
wtWebGraphAnalogIn57643StTzOffsetHrs = _WtWebGraphAnalogIn57643StTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 4),
    _WtWebGraphAnalogIn57643StTzOffsetHrs_Type()
)
wtWebGraphAnalogIn57643StTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzOffsetMin_Type = Integer32
_WtWebGraphAnalogIn57643StTzOffsetMin_Object = MibScalar
wtWebGraphAnalogIn57643StTzOffsetMin = _WtWebGraphAnalogIn57643StTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 5),
    _WtWebGraphAnalogIn57643StTzOffsetMin_Type()
)
wtWebGraphAnalogIn57643StTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643StTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643StTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643StTzEnable_Object = MibScalar
wtWebGraphAnalogIn57643StTzEnable = _WtWebGraphAnalogIn57643StTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 6),
    _WtWebGraphAnalogIn57643StTzEnable_Type()
)
wtWebGraphAnalogIn57643StTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStartMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StartMonth-April", 4),
          ("wtWebGraphAnalogIn57643StartMonth-August", 8),
          ("wtWebGraphAnalogIn57643StartMonth-December", 12),
          ("wtWebGraphAnalogIn57643StartMonth-February", 2),
          ("wtWebGraphAnalogIn57643StartMonth-January", 1),
          ("wtWebGraphAnalogIn57643StartMonth-July", 7),
          ("wtWebGraphAnalogIn57643StartMonth-June", 6),
          ("wtWebGraphAnalogIn57643StartMonth-March", 3),
          ("wtWebGraphAnalogIn57643StartMonth-May", 5),
          ("wtWebGraphAnalogIn57643StartMonth-November", 11),
          ("wtWebGraphAnalogIn57643StartMonth-October", 10),
          ("wtWebGraphAnalogIn57643StartMonth-September", 9))
    )


_WtWebGraphAnalogIn57643StTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStartMonth_Object = MibScalar
wtWebGraphAnalogIn57643StTzStartMonth = _WtWebGraphAnalogIn57643StTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 7),
    _WtWebGraphAnalogIn57643StTzStartMonth_Type()
)
wtWebGraphAnalogIn57643StTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStartMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStartMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StartMode-first", 1),
          ("wtWebGraphAnalogIn57643StartMode-fourth", 4),
          ("wtWebGraphAnalogIn57643StartMode-last", 5),
          ("wtWebGraphAnalogIn57643StartMode-second", 2),
          ("wtWebGraphAnalogIn57643StartMode-third", 3))
    )


_WtWebGraphAnalogIn57643StTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStartMode_Object = MibScalar
wtWebGraphAnalogIn57643StTzStartMode = _WtWebGraphAnalogIn57643StTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 8),
    _WtWebGraphAnalogIn57643StTzStartMode_Type()
)
wtWebGraphAnalogIn57643StTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStartMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStartWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StartWday-Friday", 6),
          ("wtWebGraphAnalogIn57643StartWday-Monday", 2),
          ("wtWebGraphAnalogIn57643StartWday-Saturday", 7),
          ("wtWebGraphAnalogIn57643StartWday-Sunday", 1),
          ("wtWebGraphAnalogIn57643StartWday-Thursday", 4),
          ("wtWebGraphAnalogIn57643StartWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57643StartWday-Wednesday", 5))
    )


_WtWebGraphAnalogIn57643StTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStartWday_Object = MibScalar
wtWebGraphAnalogIn57643StTzStartWday = _WtWebGraphAnalogIn57643StTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 9),
    _WtWebGraphAnalogIn57643StTzStartWday_Type()
)
wtWebGraphAnalogIn57643StTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStartWday.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzStartHrs_Type = Integer32
_WtWebGraphAnalogIn57643StTzStartHrs_Object = MibScalar
wtWebGraphAnalogIn57643StTzStartHrs = _WtWebGraphAnalogIn57643StTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 10),
    _WtWebGraphAnalogIn57643StTzStartHrs_Type()
)
wtWebGraphAnalogIn57643StTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStartHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzStartMin_Type = Integer32
_WtWebGraphAnalogIn57643StTzStartMin_Object = MibScalar
wtWebGraphAnalogIn57643StTzStartMin = _WtWebGraphAnalogIn57643StTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 11),
    _WtWebGraphAnalogIn57643StTzStartMin_Type()
)
wtWebGraphAnalogIn57643StTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStartMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStopMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StopMonth-April", 4),
          ("wtWebGraphAnalogIn57643StopMonth-August", 8),
          ("wtWebGraphAnalogIn57643StopMonth-December", 12),
          ("wtWebGraphAnalogIn57643StopMonth-February", 2),
          ("wtWebGraphAnalogIn57643StopMonth-January", 1),
          ("wtWebGraphAnalogIn57643StopMonth-July", 7),
          ("wtWebGraphAnalogIn57643StopMonth-June", 6),
          ("wtWebGraphAnalogIn57643StopMonth-March", 3),
          ("wtWebGraphAnalogIn57643StopMonth-May", 5),
          ("wtWebGraphAnalogIn57643StopMonth-November", 11),
          ("wtWebGraphAnalogIn57643StopMonth-October", 10),
          ("wtWebGraphAnalogIn57643StopMonth-September", 9))
    )


_WtWebGraphAnalogIn57643StTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStopMonth_Object = MibScalar
wtWebGraphAnalogIn57643StTzStopMonth = _WtWebGraphAnalogIn57643StTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 12),
    _WtWebGraphAnalogIn57643StTzStopMonth_Type()
)
wtWebGraphAnalogIn57643StTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStopMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStopMode based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StopMode-first", 1),
          ("wtWebGraphAnalogIn57643StopMode-fourth", 4),
          ("wtWebGraphAnalogIn57643StopMode-last", 5),
          ("wtWebGraphAnalogIn57643StopMode-second", 2),
          ("wtWebGraphAnalogIn57643StopMode-third", 3))
    )


_WtWebGraphAnalogIn57643StTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStopMode_Object = MibScalar
wtWebGraphAnalogIn57643StTzStopMode = _WtWebGraphAnalogIn57643StTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 13),
    _WtWebGraphAnalogIn57643StTzStopMode_Type()
)
wtWebGraphAnalogIn57643StTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStopMode.setStatus("mandatory")


class _WtWebGraphAnalogIn57643StTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643StTzStopWday based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643StopWday-Friday", 6),
          ("wtWebGraphAnalogIn57643StopWday-Monday", 2),
          ("wtWebGraphAnalogIn57643StopWday-Saturday", 7),
          ("wtWebGraphAnalogIn57643StopWday-Sunday", 1),
          ("wtWebGraphAnalogIn57643StopWday-Thursday", 4),
          ("wtWebGraphAnalogIn57643StopWday-Tuesday", 3),
          ("wtWebGraphAnalogIn57643StopWday-Wednesday", 5))
    )


_WtWebGraphAnalogIn57643StTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643StTzStopWday_Object = MibScalar
wtWebGraphAnalogIn57643StTzStopWday = _WtWebGraphAnalogIn57643StTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 14),
    _WtWebGraphAnalogIn57643StTzStopWday_Type()
)
wtWebGraphAnalogIn57643StTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStopWday.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzStopHrs_Type = Integer32
_WtWebGraphAnalogIn57643StTzStopHrs_Object = MibScalar
wtWebGraphAnalogIn57643StTzStopHrs = _WtWebGraphAnalogIn57643StTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 15),
    _WtWebGraphAnalogIn57643StTzStopHrs_Type()
)
wtWebGraphAnalogIn57643StTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStopHrs.setStatus("mandatory")
_WtWebGraphAnalogIn57643StTzStopMin_Type = Integer32
_WtWebGraphAnalogIn57643StTzStopMin_Object = MibScalar
wtWebGraphAnalogIn57643StTzStopMin = _WtWebGraphAnalogIn57643StTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 1, 16),
    _WtWebGraphAnalogIn57643StTzStopMin_Type()
)
wtWebGraphAnalogIn57643StTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643StTzStopMin.setStatus("mandatory")
_WtWebGraphAnalogIn57643TimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643TimeServer = _WtWebGraphAnalogIn57643TimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2)
)
_WtWebGraphAnalogIn57643TimeServer1_Type = OctetString
_WtWebGraphAnalogIn57643TimeServer1_Object = MibScalar
wtWebGraphAnalogIn57643TimeServer1 = _WtWebGraphAnalogIn57643TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 1),
    _WtWebGraphAnalogIn57643TimeServer1_Type()
)
wtWebGraphAnalogIn57643TimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TimeServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57643TimeServer2_Type = OctetString
_WtWebGraphAnalogIn57643TimeServer2_Object = MibScalar
wtWebGraphAnalogIn57643TimeServer2 = _WtWebGraphAnalogIn57643TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 2),
    _WtWebGraphAnalogIn57643TimeServer2_Type()
)
wtWebGraphAnalogIn57643TimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TimeServer2.setStatus("mandatory")


class _WtWebGraphAnalogIn57643TsEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643TsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643TsEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643TsEnable_Object = MibScalar
wtWebGraphAnalogIn57643TsEnable = _WtWebGraphAnalogIn57643TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 3),
    _WtWebGraphAnalogIn57643TsEnable_Type()
)
wtWebGraphAnalogIn57643TsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TsEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643TsSyncTime_Type = Integer32
_WtWebGraphAnalogIn57643TsSyncTime_Object = MibScalar
wtWebGraphAnalogIn57643TsSyncTime = _WtWebGraphAnalogIn57643TsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 2, 4),
    _WtWebGraphAnalogIn57643TsSyncTime_Type()
)
wtWebGraphAnalogIn57643TsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643TsSyncTime.setStatus("mandatory")
_WtWebGraphAnalogIn57643DeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643DeviceClock = _WtWebGraphAnalogIn57643DeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3)
)


class _WtWebGraphAnalogIn57643ClockHrs_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643ClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAnalogIn57643ClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643ClockHrs_Object = MibScalar
wtWebGraphAnalogIn57643ClockHrs = _WtWebGraphAnalogIn57643ClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 1),
    _WtWebGraphAnalogIn57643ClockHrs_Type()
)
wtWebGraphAnalogIn57643ClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ClockHrs.setStatus("mandatory")


class _WtWebGraphAnalogIn57643ClockMin_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643ClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAnalogIn57643ClockMin_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643ClockMin_Object = MibScalar
wtWebGraphAnalogIn57643ClockMin = _WtWebGraphAnalogIn57643ClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 2),
    _WtWebGraphAnalogIn57643ClockMin_Type()
)
wtWebGraphAnalogIn57643ClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ClockMin.setStatus("mandatory")


class _WtWebGraphAnalogIn57643ClockDay_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643ClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAnalogIn57643ClockDay_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643ClockDay_Object = MibScalar
wtWebGraphAnalogIn57643ClockDay = _WtWebGraphAnalogIn57643ClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 3),
    _WtWebGraphAnalogIn57643ClockDay_Type()
)
wtWebGraphAnalogIn57643ClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ClockDay.setStatus("mandatory")


class _WtWebGraphAnalogIn57643ClockMonth_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643ClockMonth based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643ClockMonth-April", 4),
          ("wtWebGraphAnalogIn57643ClockMonth-August", 8),
          ("wtWebGraphAnalogIn57643ClockMonth-December", 12),
          ("wtWebGraphAnalogIn57643ClockMonth-February", 2),
          ("wtWebGraphAnalogIn57643ClockMonth-January", 1),
          ("wtWebGraphAnalogIn57643ClockMonth-July", 7),
          ("wtWebGraphAnalogIn57643ClockMonth-June", 6),
          ("wtWebGraphAnalogIn57643ClockMonth-March", 3),
          ("wtWebGraphAnalogIn57643ClockMonth-May", 5),
          ("wtWebGraphAnalogIn57643ClockMonth-November", 11),
          ("wtWebGraphAnalogIn57643ClockMonth-October", 10),
          ("wtWebGraphAnalogIn57643ClockMonth-September", 9))
    )


_WtWebGraphAnalogIn57643ClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643ClockMonth_Object = MibScalar
wtWebGraphAnalogIn57643ClockMonth = _WtWebGraphAnalogIn57643ClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 4),
    _WtWebGraphAnalogIn57643ClockMonth_Type()
)
wtWebGraphAnalogIn57643ClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ClockMonth.setStatus("mandatory")


class _WtWebGraphAnalogIn57643ClockYear_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643ClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAnalogIn57643ClockYear_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643ClockYear_Object = MibScalar
wtWebGraphAnalogIn57643ClockYear = _WtWebGraphAnalogIn57643ClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 2, 3, 5),
    _WtWebGraphAnalogIn57643ClockYear_Type()
)
wtWebGraphAnalogIn57643ClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643ClockYear.setStatus("mandatory")
_WtWebGraphAnalogIn57643Basic_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Basic = _WtWebGraphAnalogIn57643Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3)
)
_WtWebGraphAnalogIn57643Network_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Network = _WtWebGraphAnalogIn57643Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1)
)
_WtWebGraphAnalogIn57643IpAddress_Type = IpAddress
_WtWebGraphAnalogIn57643IpAddress_Object = MibScalar
wtWebGraphAnalogIn57643IpAddress = _WtWebGraphAnalogIn57643IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 1),
    _WtWebGraphAnalogIn57643IpAddress_Type()
)
wtWebGraphAnalogIn57643IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643IpAddress.setStatus("mandatory")
_WtWebGraphAnalogIn57643SubnetMask_Type = IpAddress
_WtWebGraphAnalogIn57643SubnetMask_Object = MibScalar
wtWebGraphAnalogIn57643SubnetMask = _WtWebGraphAnalogIn57643SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 2),
    _WtWebGraphAnalogIn57643SubnetMask_Type()
)
wtWebGraphAnalogIn57643SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SubnetMask.setStatus("mandatory")
_WtWebGraphAnalogIn57643Gateway_Type = IpAddress
_WtWebGraphAnalogIn57643Gateway_Object = MibScalar
wtWebGraphAnalogIn57643Gateway = _WtWebGraphAnalogIn57643Gateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 3),
    _WtWebGraphAnalogIn57643Gateway_Type()
)
wtWebGraphAnalogIn57643Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Gateway.setStatus("mandatory")
_WtWebGraphAnalogIn57643DnsServer1_Type = OctetString
_WtWebGraphAnalogIn57643DnsServer1_Object = MibScalar
wtWebGraphAnalogIn57643DnsServer1 = _WtWebGraphAnalogIn57643DnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 4),
    _WtWebGraphAnalogIn57643DnsServer1_Type()
)
wtWebGraphAnalogIn57643DnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DnsServer1.setStatus("mandatory")
_WtWebGraphAnalogIn57643DnsServer2_Type = OctetString
_WtWebGraphAnalogIn57643DnsServer2_Object = MibScalar
wtWebGraphAnalogIn57643DnsServer2 = _WtWebGraphAnalogIn57643DnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 5),
    _WtWebGraphAnalogIn57643DnsServer2_Type()
)
wtWebGraphAnalogIn57643DnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DnsServer2.setStatus("mandatory")
_WtWebGraphAnalogIn57643AddConfig_Type = OctetString
_WtWebGraphAnalogIn57643AddConfig_Object = MibScalar
wtWebGraphAnalogIn57643AddConfig = _WtWebGraphAnalogIn57643AddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 1, 6),
    _WtWebGraphAnalogIn57643AddConfig_Type()
)
wtWebGraphAnalogIn57643AddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AddConfig.setStatus("mandatory")
_WtWebGraphAnalogIn57643HTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643HTTP = _WtWebGraphAnalogIn57643HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2)
)
_WtWebGraphAnalogIn57643Startup_Type = OctetString
_WtWebGraphAnalogIn57643Startup_Object = MibScalar
wtWebGraphAnalogIn57643Startup = _WtWebGraphAnalogIn57643Startup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 1),
    _WtWebGraphAnalogIn57643Startup_Type()
)
wtWebGraphAnalogIn57643Startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Startup.setStatus("mandatory")
_WtWebGraphAnalogIn57643GetHeaderEnable_Type = OctetString
_WtWebGraphAnalogIn57643GetHeaderEnable_Object = MibScalar
wtWebGraphAnalogIn57643GetHeaderEnable = _WtWebGraphAnalogIn57643GetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 2),
    _WtWebGraphAnalogIn57643GetHeaderEnable_Type()
)
wtWebGraphAnalogIn57643GetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57643HttpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643HttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57643HttpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643HttpPort_Object = MibScalar
wtWebGraphAnalogIn57643HttpPort = _WtWebGraphAnalogIn57643HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 2, 3),
    _WtWebGraphAnalogIn57643HttpPort_Type()
)
wtWebGraphAnalogIn57643HttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643HttpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643Mail_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Mail = _WtWebGraphAnalogIn57643Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3)
)
_WtWebGraphAnalogIn57643MailAdName_Type = OctetString
_WtWebGraphAnalogIn57643MailAdName_Object = MibScalar
wtWebGraphAnalogIn57643MailAdName = _WtWebGraphAnalogIn57643MailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 1),
    _WtWebGraphAnalogIn57643MailAdName_Type()
)
wtWebGraphAnalogIn57643MailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailAdName.setStatus("mandatory")
_WtWebGraphAnalogIn57643MailReply_Type = OctetString
_WtWebGraphAnalogIn57643MailReply_Object = MibScalar
wtWebGraphAnalogIn57643MailReply = _WtWebGraphAnalogIn57643MailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 2),
    _WtWebGraphAnalogIn57643MailReply_Type()
)
wtWebGraphAnalogIn57643MailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailReply.setStatus("mandatory")
_WtWebGraphAnalogIn57643MailServer_Type = OctetString
_WtWebGraphAnalogIn57643MailServer_Object = MibScalar
wtWebGraphAnalogIn57643MailServer = _WtWebGraphAnalogIn57643MailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 3),
    _WtWebGraphAnalogIn57643MailServer_Type()
)
wtWebGraphAnalogIn57643MailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAnalogIn57643MailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643MailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643MailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643MailAuthentication_Object = MibScalar
wtWebGraphAnalogIn57643MailAuthentication = _WtWebGraphAnalogIn57643MailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 5),
    _WtWebGraphAnalogIn57643MailAuthentication_Type()
)
wtWebGraphAnalogIn57643MailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailAuthentication.setStatus("mandatory")
_WtWebGraphAnalogIn57643MailAuthUser_Type = OctetString
_WtWebGraphAnalogIn57643MailAuthUser_Object = MibScalar
wtWebGraphAnalogIn57643MailAuthUser = _WtWebGraphAnalogIn57643MailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 6),
    _WtWebGraphAnalogIn57643MailAuthUser_Type()
)
wtWebGraphAnalogIn57643MailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailAuthUser.setStatus("mandatory")
_WtWebGraphAnalogIn57643MailAuthPassword_Type = OctetString
_WtWebGraphAnalogIn57643MailAuthPassword_Object = MibScalar
wtWebGraphAnalogIn57643MailAuthPassword = _WtWebGraphAnalogIn57643MailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 7),
    _WtWebGraphAnalogIn57643MailAuthPassword_Type()
)
wtWebGraphAnalogIn57643MailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailAuthPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57643MailPop3Server_Type = OctetString
_WtWebGraphAnalogIn57643MailPop3Server_Object = MibScalar
wtWebGraphAnalogIn57643MailPop3Server = _WtWebGraphAnalogIn57643MailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 3, 8),
    _WtWebGraphAnalogIn57643MailPop3Server_Type()
)
wtWebGraphAnalogIn57643MailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MailPop3Server.setStatus("mandatory")
_WtWebGraphAnalogIn57643SNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643SNMP = _WtWebGraphAnalogIn57643SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4)
)
_WtWebGraphAnalogIn57643SnmpCommunityStringRead_Type = OctetString
_WtWebGraphAnalogIn57643SnmpCommunityStringRead_Object = MibScalar
wtWebGraphAnalogIn57643SnmpCommunityStringRead = _WtWebGraphAnalogIn57643SnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 1),
    _WtWebGraphAnalogIn57643SnmpCommunityStringRead_Type()
)
wtWebGraphAnalogIn57643SnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAnalogIn57643SnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAnalogIn57643SnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAnalogIn57643SnmpCommunityStringReadWrite = _WtWebGraphAnalogIn57643SnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 2),
    _WtWebGraphAnalogIn57643SnmpCommunityStringReadWrite_Type()
)
wtWebGraphAnalogIn57643SnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAnalogIn57643SystemTrapManagerIP_Type = OctetString
_WtWebGraphAnalogIn57643SystemTrapManagerIP_Object = MibScalar
wtWebGraphAnalogIn57643SystemTrapManagerIP = _WtWebGraphAnalogIn57643SystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 3),
    _WtWebGraphAnalogIn57643SystemTrapManagerIP_Type()
)
wtWebGraphAnalogIn57643SystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAnalogIn57643SystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643SystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643SystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643SystemTrapEnable_Object = MibScalar
wtWebGraphAnalogIn57643SystemTrapEnable = _WtWebGraphAnalogIn57643SystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 4),
    _WtWebGraphAnalogIn57643SystemTrapEnable_Type()
)
wtWebGraphAnalogIn57643SystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SystemTrapEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643SnmpEnable_Type = OctetString
_WtWebGraphAnalogIn57643SnmpEnable_Object = MibScalar
wtWebGraphAnalogIn57643SnmpEnable = _WtWebGraphAnalogIn57643SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 5),
    _WtWebGraphAnalogIn57643SnmpEnable_Type()
)
wtWebGraphAnalogIn57643SnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SnmpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643SnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAnalogIn57643SnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAnalogIn57643SnmpCommunityStringTrap = _WtWebGraphAnalogIn57643SnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 4, 6),
    _WtWebGraphAnalogIn57643SnmpCommunityStringTrap_Type()
)
wtWebGraphAnalogIn57643SnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAnalogIn57643UDP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643UDP = _WtWebGraphAnalogIn57643UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5)
)


class _WtWebGraphAnalogIn57643UdpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643UdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57643UdpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643UdpPort_Object = MibScalar
wtWebGraphAnalogIn57643UdpPort = _WtWebGraphAnalogIn57643UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5, 1),
    _WtWebGraphAnalogIn57643UdpPort_Type()
)
wtWebGraphAnalogIn57643UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643UdpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643UdpEnable_Type = OctetString
_WtWebGraphAnalogIn57643UdpEnable_Object = MibScalar
wtWebGraphAnalogIn57643UdpEnable = _WtWebGraphAnalogIn57643UdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 5, 2),
    _WtWebGraphAnalogIn57643UdpEnable_Type()
)
wtWebGraphAnalogIn57643UdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643UdpEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643Syslog_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Syslog = _WtWebGraphAnalogIn57643Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6)
)
_WtWebGraphAnalogIn57643SyslogServerIP_Type = OctetString
_WtWebGraphAnalogIn57643SyslogServerIP_Object = MibScalar
wtWebGraphAnalogIn57643SyslogServerIP = _WtWebGraphAnalogIn57643SyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 1),
    _WtWebGraphAnalogIn57643SyslogServerIP_Type()
)
wtWebGraphAnalogIn57643SyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SyslogServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57643SyslogServerPort_Type = Integer32
_WtWebGraphAnalogIn57643SyslogServerPort_Object = MibScalar
wtWebGraphAnalogIn57643SyslogServerPort = _WtWebGraphAnalogIn57643SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 2),
    _WtWebGraphAnalogIn57643SyslogServerPort_Type()
)
wtWebGraphAnalogIn57643SyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SyslogServerPort.setStatus("mandatory")


class _WtWebGraphAnalogIn57643SyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643SyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643SyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643SyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAnalogIn57643SyslogSystemMessagesEnable = _WtWebGraphAnalogIn57643SyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 3),
    _WtWebGraphAnalogIn57643SyslogSystemMessagesEnable_Type()
)
wtWebGraphAnalogIn57643SyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643SyslogEnable_Type = OctetString
_WtWebGraphAnalogIn57643SyslogEnable_Object = MibScalar
wtWebGraphAnalogIn57643SyslogEnable = _WtWebGraphAnalogIn57643SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 6, 4),
    _WtWebGraphAnalogIn57643SyslogEnable_Type()
)
wtWebGraphAnalogIn57643SyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SyslogEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTP_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643FTP = _WtWebGraphAnalogIn57643FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7)
)
_WtWebGraphAnalogIn57643FTPServerIP_Type = OctetString
_WtWebGraphAnalogIn57643FTPServerIP_Object = MibScalar
wtWebGraphAnalogIn57643FTPServerIP = _WtWebGraphAnalogIn57643FTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 1),
    _WtWebGraphAnalogIn57643FTPServerIP_Type()
)
wtWebGraphAnalogIn57643FTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPServerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPServerControlPort_Type = Integer32
_WtWebGraphAnalogIn57643FTPServerControlPort_Object = MibScalar
wtWebGraphAnalogIn57643FTPServerControlPort = _WtWebGraphAnalogIn57643FTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 2),
    _WtWebGraphAnalogIn57643FTPServerControlPort_Type()
)
wtWebGraphAnalogIn57643FTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPServerControlPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPUserName_Type = OctetString
_WtWebGraphAnalogIn57643FTPUserName_Object = MibScalar
wtWebGraphAnalogIn57643FTPUserName = _WtWebGraphAnalogIn57643FTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 3),
    _WtWebGraphAnalogIn57643FTPUserName_Type()
)
wtWebGraphAnalogIn57643FTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPUserName.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPPassword_Type = OctetString
_WtWebGraphAnalogIn57643FTPPassword_Object = MibScalar
wtWebGraphAnalogIn57643FTPPassword = _WtWebGraphAnalogIn57643FTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 4),
    _WtWebGraphAnalogIn57643FTPPassword_Type()
)
wtWebGraphAnalogIn57643FTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPPassword.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPAccount_Type = OctetString
_WtWebGraphAnalogIn57643FTPAccount_Object = MibScalar
wtWebGraphAnalogIn57643FTPAccount = _WtWebGraphAnalogIn57643FTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 5),
    _WtWebGraphAnalogIn57643FTPAccount_Type()
)
wtWebGraphAnalogIn57643FTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPAccount.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPOption_Type = OctetString
_WtWebGraphAnalogIn57643FTPOption_Object = MibScalar
wtWebGraphAnalogIn57643FTPOption = _WtWebGraphAnalogIn57643FTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 6),
    _WtWebGraphAnalogIn57643FTPOption_Type()
)
wtWebGraphAnalogIn57643FTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPOption.setStatus("mandatory")
_WtWebGraphAnalogIn57643FTPEnable_Type = OctetString
_WtWebGraphAnalogIn57643FTPEnable_Object = MibScalar
wtWebGraphAnalogIn57643FTPEnable = _WtWebGraphAnalogIn57643FTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 3, 7, 7),
    _WtWebGraphAnalogIn57643FTPEnable_Type()
)
wtWebGraphAnalogIn57643FTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643FTPEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643Datalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Datalogger = _WtWebGraphAnalogIn57643Datalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4)
)


class _WtWebGraphAnalogIn57643LoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643LoggerTimebase based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643Datalogger-15Min", 3),
          ("wtWebGraphAnalogIn57643Datalogger-1Min", 1),
          ("wtWebGraphAnalogIn57643Datalogger-5Min", 2),
          ("wtWebGraphAnalogIn57643Datalogger-60Min", 4))
    )


_WtWebGraphAnalogIn57643LoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643LoggerTimebase_Object = MibScalar
wtWebGraphAnalogIn57643LoggerTimebase = _WtWebGraphAnalogIn57643LoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 1),
    _WtWebGraphAnalogIn57643LoggerTimebase_Type()
)
wtWebGraphAnalogIn57643LoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643LoggerTimebase.setStatus("mandatory")


class _WtWebGraphAnalogIn57643LoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643LoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643LoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643LoggerSensorSel_Object = MibScalar
wtWebGraphAnalogIn57643LoggerSensorSel = _WtWebGraphAnalogIn57643LoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 2),
    _WtWebGraphAnalogIn57643LoggerSensorSel_Type()
)
wtWebGraphAnalogIn57643LoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643LoggerSensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57643DisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643DisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643DisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643DisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57643DisplaySensorSel = _WtWebGraphAnalogIn57643DisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 3),
    _WtWebGraphAnalogIn57643DisplaySensorSel_Type()
)
wtWebGraphAnalogIn57643DisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DisplaySensorSel.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorColorTable_Object = MibTable
wtWebGraphAnalogIn57643SensorColorTable = _WtWebGraphAnalogIn57643SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorColorTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorColorEntry_Object = MibTableRow
wtWebGraphAnalogIn57643SensorColorEntry = _WtWebGraphAnalogIn57643SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4, 1)
)
wtWebGraphAnalogIn57643SensorColorEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorColorEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643SensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643SensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57643SensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643SensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57643SensorColor = _WtWebGraphAnalogIn57643SensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 4, 1, 1),
    _WtWebGraphAnalogIn57643SensorColor_Type()
)
wtWebGraphAnalogIn57643SensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57643AutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57643AutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57643AutoScaleEnable = _WtWebGraphAnalogIn57643AutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 5),
    _WtWebGraphAnalogIn57643AutoScaleEnable_Type()
)
wtWebGraphAnalogIn57643AutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643VerticalUpperLimit_Type = OctetString
_WtWebGraphAnalogIn57643VerticalUpperLimit_Object = MibScalar
wtWebGraphAnalogIn57643VerticalUpperLimit = _WtWebGraphAnalogIn57643VerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 6),
    _WtWebGraphAnalogIn57643VerticalUpperLimit_Type()
)
wtWebGraphAnalogIn57643VerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643VerticalUpperLimit.setStatus("mandatory")
_WtWebGraphAnalogIn57643VerticalLowerLimit_Type = OctetString
_WtWebGraphAnalogIn57643VerticalLowerLimit_Object = MibScalar
wtWebGraphAnalogIn57643VerticalLowerLimit = _WtWebGraphAnalogIn57643VerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 7),
    _WtWebGraphAnalogIn57643VerticalLowerLimit_Type()
)
wtWebGraphAnalogIn57643VerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643VerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphAnalogIn57643HorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643HorizontalZoom based on Integer32"""
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
        *(("wtWebGraphAnalogIn57643Zoom-25days", 6),
          ("wtWebGraphAnalogIn57643Zoom-25min", 1),
          ("wtWebGraphAnalogIn57643Zoom-30hrs", 4),
          ("wtWebGraphAnalogIn57643Zoom-5days", 5),
          ("wtWebGraphAnalogIn57643Zoom-5hrs", 3),
          ("wtWebGraphAnalogIn57643Zoom-75min", 2))
    )


_WtWebGraphAnalogIn57643HorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643HorizontalZoom_Object = MibScalar
wtWebGraphAnalogIn57643HorizontalZoom = _WtWebGraphAnalogIn57643HorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 4, 8),
    _WtWebGraphAnalogIn57643HorizontalZoom_Type()
)
wtWebGraphAnalogIn57643HorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643HorizontalZoom.setStatus("mandatory")
_WtWebGraphAnalogIn57643Alarm_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Alarm = _WtWebGraphAnalogIn57643Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5)
)


class _WtWebGraphAnalogIn57643AlarmCount_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643AlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57643AlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643AlarmCount_Object = MibScalar
wtWebGraphAnalogIn57643AlarmCount = _WtWebGraphAnalogIn57643AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 1),
    _WtWebGraphAnalogIn57643AlarmCount_Type()
)
wtWebGraphAnalogIn57643AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmCount.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmIfTable_Object = MibTable
wtWebGraphAnalogIn57643AlarmIfTable = _WtWebGraphAnalogIn57643AlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmIfTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmIfEntry_Object = MibTableRow
wtWebGraphAnalogIn57643AlarmIfEntry = _WtWebGraphAnalogIn57643AlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2, 1)
)
wtWebGraphAnalogIn57643AlarmIfEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmNo_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643AlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAnalogIn57643AlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643AlarmNo_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmNo = _WtWebGraphAnalogIn57643AlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAnalogIn57643AlarmNo_Type()
)
wtWebGraphAnalogIn57643AlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmNo.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmTable_Object = MibTable
wtWebGraphAnalogIn57643AlarmTable = _WtWebGraphAnalogIn57643AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmEntry_Object = MibTableRow
wtWebGraphAnalogIn57643AlarmEntry = _WtWebGraphAnalogIn57643AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1)
)
wtWebGraphAnalogIn57643AlarmEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmEntry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643AlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643AlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643AlarmTrigger_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTrigger = _WtWebGraphAnalogIn57643AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAnalogIn57643AlarmTrigger_Type()
)
wtWebGraphAnalogIn57643AlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTrigger.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmMin_Type = OctetString
_WtWebGraphAnalogIn57643AlarmMin_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmMin = _WtWebGraphAnalogIn57643AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAnalogIn57643AlarmMin_Type()
)
wtWebGraphAnalogIn57643AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmMin.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmMax_Type = OctetString
_WtWebGraphAnalogIn57643AlarmMax_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmMax = _WtWebGraphAnalogIn57643AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAnalogIn57643AlarmMax_Type()
)
wtWebGraphAnalogIn57643AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmMax.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmHysteresis_Type = OctetString
_WtWebGraphAnalogIn57643AlarmHysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmHysteresis = _WtWebGraphAnalogIn57643AlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAnalogIn57643AlarmHysteresis_Type()
)
wtWebGraphAnalogIn57643AlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmHysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmDelay_Type = OctetString
_WtWebGraphAnalogIn57643AlarmDelay_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmDelay = _WtWebGraphAnalogIn57643AlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAnalogIn57643AlarmDelay_Type()
)
wtWebGraphAnalogIn57643AlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmDelay.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmInterval_Type = OctetString
_WtWebGraphAnalogIn57643AlarmInterval_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmInterval = _WtWebGraphAnalogIn57643AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAnalogIn57643AlarmInterval_Type()
)
wtWebGraphAnalogIn57643AlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmInterval.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643AlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643AlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643AlarmEnable_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmEnable = _WtWebGraphAnalogIn57643AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAnalogIn57643AlarmEnable_Type()
)
wtWebGraphAnalogIn57643AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmEMailAddr_Type = OctetString
_WtWebGraphAnalogIn57643AlarmEMailAddr_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmEMailAddr = _WtWebGraphAnalogIn57643AlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAnalogIn57643AlarmEMailAddr_Type()
)
wtWebGraphAnalogIn57643AlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmMailSubject_Type = OctetString
_WtWebGraphAnalogIn57643AlarmMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmMailSubject = _WtWebGraphAnalogIn57643AlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAnalogIn57643AlarmMailSubject_Type()
)
wtWebGraphAnalogIn57643AlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmMailText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmMailText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmMailText = _WtWebGraphAnalogIn57643AlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAnalogIn57643AlarmMailText_Type()
)
wtWebGraphAnalogIn57643AlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmManagerIP_Type = OctetString
_WtWebGraphAnalogIn57643AlarmManagerIP_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmManagerIP = _WtWebGraphAnalogIn57643AlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAnalogIn57643AlarmManagerIP_Type()
)
wtWebGraphAnalogIn57643AlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmManagerIP.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmTrapText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTrapText = _WtWebGraphAnalogIn57643AlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAnalogIn57643AlarmTrapText_Type()
)
wtWebGraphAnalogIn57643AlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTrapText.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643AlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643AlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643AlarmMailOptions_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmMailOptions = _WtWebGraphAnalogIn57643AlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAnalogIn57643AlarmMailOptions_Type()
)
wtWebGraphAnalogIn57643AlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmMailOptions.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmTcpIpAddr_Type = OctetString
_WtWebGraphAnalogIn57643AlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTcpIpAddr = _WtWebGraphAnalogIn57643AlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAnalogIn57643AlarmTcpIpAddr_Type()
)
wtWebGraphAnalogIn57643AlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643AlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57643AlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643AlarmTcpPort_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTcpPort = _WtWebGraphAnalogIn57643AlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAnalogIn57643AlarmTcpPort_Type()
)
wtWebGraphAnalogIn57643AlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTcpPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmTcpText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTcpText = _WtWebGraphAnalogIn57643AlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAnalogIn57643AlarmTcpText_Type()
)
wtWebGraphAnalogIn57643AlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmClearMailSubject_Type = OctetString
_WtWebGraphAnalogIn57643AlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmClearMailSubject = _WtWebGraphAnalogIn57643AlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAnalogIn57643AlarmClearMailSubject_Type()
)
wtWebGraphAnalogIn57643AlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmClearMailText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmClearMailText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmClearMailText = _WtWebGraphAnalogIn57643AlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAnalogIn57643AlarmClearMailText_Type()
)
wtWebGraphAnalogIn57643AlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmClearMailText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmClearTrapText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmClearTrapText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmClearTrapText = _WtWebGraphAnalogIn57643AlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAnalogIn57643AlarmClearTrapText_Type()
)
wtWebGraphAnalogIn57643AlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmClearTcpText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmClearTcpText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmClearTcpText = _WtWebGraphAnalogIn57643AlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAnalogIn57643AlarmClearTcpText_Type()
)
wtWebGraphAnalogIn57643AlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAnalogIn57643Alarm2Min_Type = OctetString
_WtWebGraphAnalogIn57643Alarm2Min_Object = MibTableColumn
wtWebGraphAnalogIn57643Alarm2Min = _WtWebGraphAnalogIn57643Alarm2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAnalogIn57643Alarm2Min_Type()
)
wtWebGraphAnalogIn57643Alarm2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alarm2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57643Alarm2Max_Type = OctetString
_WtWebGraphAnalogIn57643Alarm2Max_Object = MibTableColumn
wtWebGraphAnalogIn57643Alarm2Max = _WtWebGraphAnalogIn57643Alarm2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAnalogIn57643Alarm2Max_Type()
)
wtWebGraphAnalogIn57643Alarm2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alarm2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57643Alarm2Hysteresis_Type = OctetString
_WtWebGraphAnalogIn57643Alarm2Hysteresis_Object = MibTableColumn
wtWebGraphAnalogIn57643Alarm2Hysteresis = _WtWebGraphAnalogIn57643Alarm2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAnalogIn57643Alarm2Hysteresis_Type()
)
wtWebGraphAnalogIn57643Alarm2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alarm2Hysteresis.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmSyslogIpAddr_Type = OctetString
_WtWebGraphAnalogIn57643AlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmSyslogIpAddr = _WtWebGraphAnalogIn57643AlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAnalogIn57643AlarmSyslogIpAddr_Type()
)
wtWebGraphAnalogIn57643AlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAnalogIn57643AlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAnalogIn57643AlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAnalogIn57643AlarmSyslogPort_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmSyslogPort = _WtWebGraphAnalogIn57643AlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAnalogIn57643AlarmSyslogPort_Type()
)
wtWebGraphAnalogIn57643AlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmSyslogText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmSyslogText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmSyslogText = _WtWebGraphAnalogIn57643AlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAnalogIn57643AlarmSyslogText_Type()
)
wtWebGraphAnalogIn57643AlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmSyslogText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmSyslogClearText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmSyslogClearText = _WtWebGraphAnalogIn57643AlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAnalogIn57643AlarmSyslogClearText_Type()
)
wtWebGraphAnalogIn57643AlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmFtpDataPort_Type = OctetString
_WtWebGraphAnalogIn57643AlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmFtpDataPort = _WtWebGraphAnalogIn57643AlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAnalogIn57643AlarmFtpDataPort_Type()
)
wtWebGraphAnalogIn57643AlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmFtpFileName_Type = OctetString
_WtWebGraphAnalogIn57643AlarmFtpFileName_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmFtpFileName = _WtWebGraphAnalogIn57643AlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAnalogIn57643AlarmFtpFileName_Type()
)
wtWebGraphAnalogIn57643AlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmFtpText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmFtpText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmFtpText = _WtWebGraphAnalogIn57643AlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAnalogIn57643AlarmFtpText_Type()
)
wtWebGraphAnalogIn57643AlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmFtpText.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmFtpClearText_Type = OctetString
_WtWebGraphAnalogIn57643AlarmFtpClearText_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmFtpClearText = _WtWebGraphAnalogIn57643AlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAnalogIn57643AlarmFtpClearText_Type()
)
wtWebGraphAnalogIn57643AlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAnalogIn57643AlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643AlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643AlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643AlarmFtpOption_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmFtpOption = _WtWebGraphAnalogIn57643AlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAnalogIn57643AlarmFtpOption_Type()
)
wtWebGraphAnalogIn57643AlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmFtpOption.setStatus("mandatory")
_WtWebGraphAnalogIn57643AlarmTimerCron_Type = OctetString
_WtWebGraphAnalogIn57643AlarmTimerCron_Object = MibTableColumn
wtWebGraphAnalogIn57643AlarmTimerCron = _WtWebGraphAnalogIn57643AlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAnalogIn57643AlarmTimerCron_Type()
)
wtWebGraphAnalogIn57643AlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlarmTimerCron.setStatus("mandatory")
_WtWebGraphAnalogIn57643Graphics_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Graphics = _WtWebGraphAnalogIn57643Graphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6)
)
_WtWebGraphAnalogIn57643GraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643GraphicsBase = _WtWebGraphAnalogIn57643GraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1)
)
_WtWebGraphAnalogIn57643GraphicsBaseEnable_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsBaseEnable_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBaseEnable = _WtWebGraphAnalogIn57643GraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 1),
    _WtWebGraphAnalogIn57643GraphicsBaseEnable_Type()
)
wtWebGraphAnalogIn57643GraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsBaseWidth_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsBaseWidth_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBaseWidth = _WtWebGraphAnalogIn57643GraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 2),
    _WtWebGraphAnalogIn57643GraphicsBaseWidth_Type()
)
wtWebGraphAnalogIn57643GraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsBaseHeight_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsBaseHeight_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBaseHeight = _WtWebGraphAnalogIn57643GraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 3),
    _WtWebGraphAnalogIn57643GraphicsBaseHeight_Type()
)
wtWebGraphAnalogIn57643GraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAnalogIn57643GraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643GraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57643GraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643GraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBaseFrameColor = _WtWebGraphAnalogIn57643GraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 4),
    _WtWebGraphAnalogIn57643GraphicsBaseFrameColor_Type()
)
wtWebGraphAnalogIn57643GraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAnalogIn57643GraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57643GraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643GraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor = _WtWebGraphAnalogIn57643GraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 5),
    _WtWebGraphAnalogIn57643GraphicsBaseBackgroundColor_Type()
)
wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsBasePollingrate_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsBasePollingrate_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsBasePollingrate = _WtWebGraphAnalogIn57643GraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 1, 6),
    _WtWebGraphAnalogIn57643GraphicsBasePollingrate_Type()
)
wtWebGraphAnalogIn57643GraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643GraphicsSelect = _WtWebGraphAnalogIn57643GraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2)
)


class _WtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel = _WtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 1),
    _WtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem = _WtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 2),
    _WtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorColor2Table_Object = MibTable
wtWebGraphAnalogIn57643SensorColor2Table = _WtWebGraphAnalogIn57643SensorColor2Table_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorColor2Table.setStatus("mandatory")
_WtWebGraphAnalogIn57643SensorColor2Entry_Object = MibTableRow
wtWebGraphAnalogIn57643SensorColor2Entry = _WtWebGraphAnalogIn57643SensorColor2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAnalogIn57643SensorColor2Entry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SensorColor2Entry.setStatus("mandatory")


class _WtWebGraphAnalogIn57643GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAnalogIn57643GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643GraphicsSensorColor_Object = MibTableColumn
wtWebGraphAnalogIn57643GraphicsSensorColor = _WtWebGraphAnalogIn57643GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAnalogIn57643GraphicsSensorColor_Type()
)
wtWebGraphAnalogIn57643GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsSelectScale_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsSelectScale_Object = MibTableColumn
wtWebGraphAnalogIn57643GraphicsSelectScale = _WtWebGraphAnalogIn57643GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAnalogIn57643GraphicsSelectScale_Type()
)
wtWebGraphAnalogIn57643GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643GraphicsScale = _WtWebGraphAnalogIn57643GraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3)
)
_WtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable = _WtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 1),
    _WtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable = _WtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 2),
    _WtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale1Min_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale1Min_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale1Min = _WtWebGraphAnalogIn57643GraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 3),
    _WtWebGraphAnalogIn57643GraphicsScale1Min_Type()
)
wtWebGraphAnalogIn57643GraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale2Min_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale2Min_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale2Min = _WtWebGraphAnalogIn57643GraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 4),
    _WtWebGraphAnalogIn57643GraphicsScale2Min_Type()
)
wtWebGraphAnalogIn57643GraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale3Min_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale3Min_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale3Min = _WtWebGraphAnalogIn57643GraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 5),
    _WtWebGraphAnalogIn57643GraphicsScale3Min_Type()
)
wtWebGraphAnalogIn57643GraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale3Min.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale4Min_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale4Min_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale4Min = _WtWebGraphAnalogIn57643GraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 6),
    _WtWebGraphAnalogIn57643GraphicsScale4Min_Type()
)
wtWebGraphAnalogIn57643GraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale4Min.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale1Max_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale1Max_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale1Max = _WtWebGraphAnalogIn57643GraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 7),
    _WtWebGraphAnalogIn57643GraphicsScale1Max_Type()
)
wtWebGraphAnalogIn57643GraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale2Max_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale2Max_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale2Max = _WtWebGraphAnalogIn57643GraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 8),
    _WtWebGraphAnalogIn57643GraphicsScale2Max_Type()
)
wtWebGraphAnalogIn57643GraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale3Max_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale3Max_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale3Max = _WtWebGraphAnalogIn57643GraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 9),
    _WtWebGraphAnalogIn57643GraphicsScale3Max_Type()
)
wtWebGraphAnalogIn57643GraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale3Max.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale4Max_Type = Integer32
_WtWebGraphAnalogIn57643GraphicsScale4Max_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale4Max = _WtWebGraphAnalogIn57643GraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 10),
    _WtWebGraphAnalogIn57643GraphicsScale4Max_Type()
)
wtWebGraphAnalogIn57643GraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale4Max.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale1Unit_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScale1Unit_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale1Unit = _WtWebGraphAnalogIn57643GraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 11),
    _WtWebGraphAnalogIn57643GraphicsScale1Unit_Type()
)
wtWebGraphAnalogIn57643GraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale2Unit_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScale2Unit_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale2Unit = _WtWebGraphAnalogIn57643GraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 12),
    _WtWebGraphAnalogIn57643GraphicsScale2Unit_Type()
)
wtWebGraphAnalogIn57643GraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale3Unit_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScale3Unit_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale3Unit = _WtWebGraphAnalogIn57643GraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 13),
    _WtWebGraphAnalogIn57643GraphicsScale3Unit_Type()
)
wtWebGraphAnalogIn57643GraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57643GraphicsScale4Unit_Type = OctetString
_WtWebGraphAnalogIn57643GraphicsScale4Unit_Object = MibScalar
wtWebGraphAnalogIn57643GraphicsScale4Unit = _WtWebGraphAnalogIn57643GraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 1, 6, 3, 14),
    _WtWebGraphAnalogIn57643GraphicsScale4Unit_Type()
)
wtWebGraphAnalogIn57643GraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643GraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphAnalogIn57643Ports_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Ports = _WtWebGraphAnalogIn57643Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2)
)
_WtWebGraphAnalogIn57643PortTable_Object = MibTable
wtWebGraphAnalogIn57643PortTable = _WtWebGraphAnalogIn57643PortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortTable.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortEntry_Object = MibTableRow
wtWebGraphAnalogIn57643PortEntry = _WtWebGraphAnalogIn57643PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1)
)
wtWebGraphAnalogIn57643PortEntry.setIndexNames(
    (0, "WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643SensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortEntry.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortName_Type = OctetString
_WtWebGraphAnalogIn57643PortName_Object = MibTableColumn
wtWebGraphAnalogIn57643PortName = _WtWebGraphAnalogIn57643PortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 1),
    _WtWebGraphAnalogIn57643PortName_Type()
)
wtWebGraphAnalogIn57643PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortName.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortText_Type = OctetString
_WtWebGraphAnalogIn57643PortText_Object = MibTableColumn
wtWebGraphAnalogIn57643PortText = _WtWebGraphAnalogIn57643PortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 2),
    _WtWebGraphAnalogIn57643PortText_Type()
)
wtWebGraphAnalogIn57643PortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortText.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortOffset1_Type = OctetString
_WtWebGraphAnalogIn57643PortOffset1_Object = MibTableColumn
wtWebGraphAnalogIn57643PortOffset1 = _WtWebGraphAnalogIn57643PortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 3),
    _WtWebGraphAnalogIn57643PortOffset1_Type()
)
wtWebGraphAnalogIn57643PortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortOffset1.setStatus("mandatory")
_WtWebGraphAnalogIn57643SetPoint1_Type = OctetString
_WtWebGraphAnalogIn57643SetPoint1_Object = MibTableColumn
wtWebGraphAnalogIn57643SetPoint1 = _WtWebGraphAnalogIn57643SetPoint1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 4),
    _WtWebGraphAnalogIn57643SetPoint1_Type()
)
wtWebGraphAnalogIn57643SetPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SetPoint1.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortOffset2_Type = OctetString
_WtWebGraphAnalogIn57643PortOffset2_Object = MibTableColumn
wtWebGraphAnalogIn57643PortOffset2 = _WtWebGraphAnalogIn57643PortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 5),
    _WtWebGraphAnalogIn57643PortOffset2_Type()
)
wtWebGraphAnalogIn57643PortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortOffset2.setStatus("mandatory")
_WtWebGraphAnalogIn57643SetPoint2_Type = OctetString
_WtWebGraphAnalogIn57643SetPoint2_Object = MibTableColumn
wtWebGraphAnalogIn57643SetPoint2 = _WtWebGraphAnalogIn57643SetPoint2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 6),
    _WtWebGraphAnalogIn57643SetPoint2_Type()
)
wtWebGraphAnalogIn57643SetPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643SetPoint2.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortComment_Type = OctetString
_WtWebGraphAnalogIn57643PortComment_Object = MibTableColumn
wtWebGraphAnalogIn57643PortComment = _WtWebGraphAnalogIn57643PortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 7),
    _WtWebGraphAnalogIn57643PortComment_Type()
)
wtWebGraphAnalogIn57643PortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortComment.setStatus("mandatory")


class _WtWebGraphAnalogIn57643PortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphAnalogIn57643PortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAnalogIn57643PortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphAnalogIn57643PortSensorSelect_Object = MibTableColumn
wtWebGraphAnalogIn57643PortSensorSelect = _WtWebGraphAnalogIn57643PortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 8),
    _WtWebGraphAnalogIn57643PortSensorSelect_Type()
)
wtWebGraphAnalogIn57643PortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortSensorSelect.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortUnit_Type = OctetString
_WtWebGraphAnalogIn57643PortUnit_Object = MibTableColumn
wtWebGraphAnalogIn57643PortUnit = _WtWebGraphAnalogIn57643PortUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 9),
    _WtWebGraphAnalogIn57643PortUnit_Type()
)
wtWebGraphAnalogIn57643PortUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortUnit.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortScale0_Type = OctetString
_WtWebGraphAnalogIn57643PortScale0_Object = MibTableColumn
wtWebGraphAnalogIn57643PortScale0 = _WtWebGraphAnalogIn57643PortScale0_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 10),
    _WtWebGraphAnalogIn57643PortScale0_Type()
)
wtWebGraphAnalogIn57643PortScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortScale0.setStatus("mandatory")
_WtWebGraphAnalogIn57643PortScale100_Type = OctetString
_WtWebGraphAnalogIn57643PortScale100_Object = MibTableColumn
wtWebGraphAnalogIn57643PortScale100 = _WtWebGraphAnalogIn57643PortScale100_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 2, 1, 1, 11),
    _WtWebGraphAnalogIn57643PortScale100_Type()
)
wtWebGraphAnalogIn57643PortScale100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643PortScale100.setStatus("mandatory")
_WtWebGraphAnalogIn57643Manufact_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Manufact = _WtWebGraphAnalogIn57643Manufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3)
)
_WtWebGraphAnalogIn57643MfName_Type = OctetString
_WtWebGraphAnalogIn57643MfName_Object = MibScalar
wtWebGraphAnalogIn57643MfName = _WtWebGraphAnalogIn57643MfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 1),
    _WtWebGraphAnalogIn57643MfName_Type()
)
wtWebGraphAnalogIn57643MfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfName.setStatus("mandatory")
_WtWebGraphAnalogIn57643MfAddr_Type = OctetString
_WtWebGraphAnalogIn57643MfAddr_Object = MibScalar
wtWebGraphAnalogIn57643MfAddr = _WtWebGraphAnalogIn57643MfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 2),
    _WtWebGraphAnalogIn57643MfAddr_Type()
)
wtWebGraphAnalogIn57643MfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfAddr.setStatus("mandatory")
_WtWebGraphAnalogIn57643MfHotline_Type = OctetString
_WtWebGraphAnalogIn57643MfHotline_Object = MibScalar
wtWebGraphAnalogIn57643MfHotline = _WtWebGraphAnalogIn57643MfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 3),
    _WtWebGraphAnalogIn57643MfHotline_Type()
)
wtWebGraphAnalogIn57643MfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfHotline.setStatus("mandatory")
_WtWebGraphAnalogIn57643MfInternet_Type = OctetString
_WtWebGraphAnalogIn57643MfInternet_Object = MibScalar
wtWebGraphAnalogIn57643MfInternet = _WtWebGraphAnalogIn57643MfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 4),
    _WtWebGraphAnalogIn57643MfInternet_Type()
)
wtWebGraphAnalogIn57643MfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfInternet.setStatus("mandatory")
_WtWebGraphAnalogIn57643MfDeviceTyp_Type = OctetString
_WtWebGraphAnalogIn57643MfDeviceTyp_Object = MibScalar
wtWebGraphAnalogIn57643MfDeviceTyp = _WtWebGraphAnalogIn57643MfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 5),
    _WtWebGraphAnalogIn57643MfDeviceTyp_Type()
)
wtWebGraphAnalogIn57643MfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfDeviceTyp.setStatus("mandatory")
_WtWebGraphAnalogIn57643MfOrderNo_Type = OctetString
_WtWebGraphAnalogIn57643MfOrderNo_Object = MibScalar
wtWebGraphAnalogIn57643MfOrderNo = _WtWebGraphAnalogIn57643MfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 3, 3, 6),
    _WtWebGraphAnalogIn57643MfOrderNo_Type()
)
wtWebGraphAnalogIn57643MfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643MfOrderNo.setStatus("mandatory")
_WtWebGraphAnalogIn57643Diag_ObjectIdentity = ObjectIdentity
wtWebGraphAnalogIn57643Diag = _WtWebGraphAnalogIn57643Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4)
)
_WtWebGraphAnalogIn57643DiagErrorCount_Type = Integer32
_WtWebGraphAnalogIn57643DiagErrorCount_Object = MibScalar
wtWebGraphAnalogIn57643DiagErrorCount = _WtWebGraphAnalogIn57643DiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 1),
    _WtWebGraphAnalogIn57643DiagErrorCount_Type()
)
wtWebGraphAnalogIn57643DiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DiagErrorCount.setStatus("mandatory")
_WtWebGraphAnalogIn57643DiagBinaryError_Type = OctetString
_WtWebGraphAnalogIn57643DiagBinaryError_Object = MibScalar
wtWebGraphAnalogIn57643DiagBinaryError = _WtWebGraphAnalogIn57643DiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 2),
    _WtWebGraphAnalogIn57643DiagBinaryError_Type()
)
wtWebGraphAnalogIn57643DiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DiagBinaryError.setStatus("mandatory")
_WtWebGraphAnalogIn57643DiagErrorIndex_Type = Integer32
_WtWebGraphAnalogIn57643DiagErrorIndex_Object = MibScalar
wtWebGraphAnalogIn57643DiagErrorIndex = _WtWebGraphAnalogIn57643DiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 3),
    _WtWebGraphAnalogIn57643DiagErrorIndex_Type()
)
wtWebGraphAnalogIn57643DiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DiagErrorIndex.setStatus("mandatory")
_WtWebGraphAnalogIn57643DiagErrorMessage_Type = OctetString
_WtWebGraphAnalogIn57643DiagErrorMessage_Object = MibScalar
wtWebGraphAnalogIn57643DiagErrorMessage = _WtWebGraphAnalogIn57643DiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 4),
    _WtWebGraphAnalogIn57643DiagErrorMessage_Type()
)
wtWebGraphAnalogIn57643DiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DiagErrorMessage.setStatus("mandatory")
_WtWebGraphAnalogIn57643DiagErrorClear_Type = Integer32
_WtWebGraphAnalogIn57643DiagErrorClear_Object = MibScalar
wtWebGraphAnalogIn57643DiagErrorClear = _WtWebGraphAnalogIn57643DiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 4, 5),
    _WtWebGraphAnalogIn57643DiagErrorClear_Type()
)
wtWebGraphAnalogIn57643DiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643DiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAnalogIn57643Alert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 31)
)
wtWebGraphAnalogIn57643Alert1.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert1.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 32)
)
wtWebGraphAnalogIn57643Alert2.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert2.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 33)
)
wtWebGraphAnalogIn57643Alert3.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert3.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 34)
)
wtWebGraphAnalogIn57643Alert4.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert4.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 35)
)
wtWebGraphAnalogIn57643Alert5.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert5.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 36)
)
wtWebGraphAnalogIn57643Alert6.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert6.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 37)
)
wtWebGraphAnalogIn57643Alert7.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert7.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 38)
)
wtWebGraphAnalogIn57643Alert8.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert8.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 91)
)
wtWebGraphAnalogIn57643Alert9.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert9.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 92)
)
wtWebGraphAnalogIn57643Alert10.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert10.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 93)
)
wtWebGraphAnalogIn57643Alert11.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert11.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 94)
)
wtWebGraphAnalogIn57643Alert12.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert12.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 95)
)
wtWebGraphAnalogIn57643Alert13.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert13.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 96)
)
wtWebGraphAnalogIn57643Alert14.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert14.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 97)
)
wtWebGraphAnalogIn57643Alert15.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert15.setStatus(
        ""
    )

wtWebGraphAnalogIn57643Alert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 98)
)
wtWebGraphAnalogIn57643Alert16.setObjects(
    ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643AlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643Alert16.setStatus(
        ""
    )

wtWebGraphAnalogIn57643AlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 12, 0, 110)
)
wtWebGraphAnalogIn57643AlertDiag.setObjects(
      *(("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643DiagErrorIndex"),
        ("WebGraph-AnalogIn-57643-US-MIB", "wtWebGraphAnalogIn57643DiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAnalogIn57643AlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-AnalogIn-57643-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAnalogIn57643": wtWebGraphAnalogIn57643,
       "wtWebGraphAnalogIn57643Alert1": wtWebGraphAnalogIn57643Alert1,
       "wtWebGraphAnalogIn57643Alert2": wtWebGraphAnalogIn57643Alert2,
       "wtWebGraphAnalogIn57643Alert3": wtWebGraphAnalogIn57643Alert3,
       "wtWebGraphAnalogIn57643Alert4": wtWebGraphAnalogIn57643Alert4,
       "wtWebGraphAnalogIn57643Alert5": wtWebGraphAnalogIn57643Alert5,
       "wtWebGraphAnalogIn57643Alert6": wtWebGraphAnalogIn57643Alert6,
       "wtWebGraphAnalogIn57643Alert7": wtWebGraphAnalogIn57643Alert7,
       "wtWebGraphAnalogIn57643Alert8": wtWebGraphAnalogIn57643Alert8,
       "wtWebGraphAnalogIn57643Alert9": wtWebGraphAnalogIn57643Alert9,
       "wtWebGraphAnalogIn57643Alert10": wtWebGraphAnalogIn57643Alert10,
       "wtWebGraphAnalogIn57643Alert11": wtWebGraphAnalogIn57643Alert11,
       "wtWebGraphAnalogIn57643Alert12": wtWebGraphAnalogIn57643Alert12,
       "wtWebGraphAnalogIn57643Alert13": wtWebGraphAnalogIn57643Alert13,
       "wtWebGraphAnalogIn57643Alert14": wtWebGraphAnalogIn57643Alert14,
       "wtWebGraphAnalogIn57643Alert15": wtWebGraphAnalogIn57643Alert15,
       "wtWebGraphAnalogIn57643Alert16": wtWebGraphAnalogIn57643Alert16,
       "wtWebGraphAnalogIn57643AlertDiag": wtWebGraphAnalogIn57643AlertDiag,
       "wtWebGraphAnalogIn57643Inventory": wtWebGraphAnalogIn57643Inventory,
       "wtWebGraphAnalogIn57643Sensors": wtWebGraphAnalogIn57643Sensors,
       "wtWebGraphAnalogIn57643SensorTable": wtWebGraphAnalogIn57643SensorTable,
       "wtWebGraphAnalogIn57643SensorEntry": wtWebGraphAnalogIn57643SensorEntry,
       "wtWebGraphAnalogIn57643SensorNo": wtWebGraphAnalogIn57643SensorNo,
       "wtWebGraphAnalogIn57643ValuesTable": wtWebGraphAnalogIn57643ValuesTable,
       "wtWebGraphAnalogIn57643ValuesEntry": wtWebGraphAnalogIn57643ValuesEntry,
       "wtWebGraphAnalogIn57643Values": wtWebGraphAnalogIn57643Values,
       "wtWebGraphAnalogIn57643BinaryValuesTable": wtWebGraphAnalogIn57643BinaryValuesTable,
       "wtWebGraphAnalogIn57643BinaryValuesEntry": wtWebGraphAnalogIn57643BinaryValuesEntry,
       "wtWebGraphAnalogIn57643BinaryValues": wtWebGraphAnalogIn57643BinaryValues,
       "wtWebGraphAnalogIn57643SessCntrl": wtWebGraphAnalogIn57643SessCntrl,
       "wtWebGraphAnalogIn57643SessCntrlPassword": wtWebGraphAnalogIn57643SessCntrlPassword,
       "wtWebGraphAnalogIn57643SessCntrlConfigMode": wtWebGraphAnalogIn57643SessCntrlConfigMode,
       "wtWebGraphAnalogIn57643SessCntrlLogout": wtWebGraphAnalogIn57643SessCntrlLogout,
       "wtWebGraphAnalogIn57643SessCntrlAdminPassword": wtWebGraphAnalogIn57643SessCntrlAdminPassword,
       "wtWebGraphAnalogIn57643SessCntrlConfigPassword": wtWebGraphAnalogIn57643SessCntrlConfigPassword,
       "wtWebGraphAnalogIn57643Config": wtWebGraphAnalogIn57643Config,
       "wtWebGraphAnalogIn57643Device": wtWebGraphAnalogIn57643Device,
       "wtWebGraphAnalogIn57643Text": wtWebGraphAnalogIn57643Text,
       "wtWebGraphAnalogIn57643DeviceName": wtWebGraphAnalogIn57643DeviceName,
       "wtWebGraphAnalogIn57643DeviceText": wtWebGraphAnalogIn57643DeviceText,
       "wtWebGraphAnalogIn57643DeviceLocation": wtWebGraphAnalogIn57643DeviceLocation,
       "wtWebGraphAnalogIn57643DeviceContact": wtWebGraphAnalogIn57643DeviceContact,
       "wtWebGraphAnalogIn57643TimeDate": wtWebGraphAnalogIn57643TimeDate,
       "wtWebGraphAnalogIn57643TimeZone": wtWebGraphAnalogIn57643TimeZone,
       "wtWebGraphAnalogIn57643TzOffsetHrs": wtWebGraphAnalogIn57643TzOffsetHrs,
       "wtWebGraphAnalogIn57643TzOffsetMin": wtWebGraphAnalogIn57643TzOffsetMin,
       "wtWebGraphAnalogIn57643TzEnable": wtWebGraphAnalogIn57643TzEnable,
       "wtWebGraphAnalogIn57643StTzOffsetHrs": wtWebGraphAnalogIn57643StTzOffsetHrs,
       "wtWebGraphAnalogIn57643StTzOffsetMin": wtWebGraphAnalogIn57643StTzOffsetMin,
       "wtWebGraphAnalogIn57643StTzEnable": wtWebGraphAnalogIn57643StTzEnable,
       "wtWebGraphAnalogIn57643StTzStartMonth": wtWebGraphAnalogIn57643StTzStartMonth,
       "wtWebGraphAnalogIn57643StTzStartMode": wtWebGraphAnalogIn57643StTzStartMode,
       "wtWebGraphAnalogIn57643StTzStartWday": wtWebGraphAnalogIn57643StTzStartWday,
       "wtWebGraphAnalogIn57643StTzStartHrs": wtWebGraphAnalogIn57643StTzStartHrs,
       "wtWebGraphAnalogIn57643StTzStartMin": wtWebGraphAnalogIn57643StTzStartMin,
       "wtWebGraphAnalogIn57643StTzStopMonth": wtWebGraphAnalogIn57643StTzStopMonth,
       "wtWebGraphAnalogIn57643StTzStopMode": wtWebGraphAnalogIn57643StTzStopMode,
       "wtWebGraphAnalogIn57643StTzStopWday": wtWebGraphAnalogIn57643StTzStopWday,
       "wtWebGraphAnalogIn57643StTzStopHrs": wtWebGraphAnalogIn57643StTzStopHrs,
       "wtWebGraphAnalogIn57643StTzStopMin": wtWebGraphAnalogIn57643StTzStopMin,
       "wtWebGraphAnalogIn57643TimeServer": wtWebGraphAnalogIn57643TimeServer,
       "wtWebGraphAnalogIn57643TimeServer1": wtWebGraphAnalogIn57643TimeServer1,
       "wtWebGraphAnalogIn57643TimeServer2": wtWebGraphAnalogIn57643TimeServer2,
       "wtWebGraphAnalogIn57643TsEnable": wtWebGraphAnalogIn57643TsEnable,
       "wtWebGraphAnalogIn57643TsSyncTime": wtWebGraphAnalogIn57643TsSyncTime,
       "wtWebGraphAnalogIn57643DeviceClock": wtWebGraphAnalogIn57643DeviceClock,
       "wtWebGraphAnalogIn57643ClockHrs": wtWebGraphAnalogIn57643ClockHrs,
       "wtWebGraphAnalogIn57643ClockMin": wtWebGraphAnalogIn57643ClockMin,
       "wtWebGraphAnalogIn57643ClockDay": wtWebGraphAnalogIn57643ClockDay,
       "wtWebGraphAnalogIn57643ClockMonth": wtWebGraphAnalogIn57643ClockMonth,
       "wtWebGraphAnalogIn57643ClockYear": wtWebGraphAnalogIn57643ClockYear,
       "wtWebGraphAnalogIn57643Basic": wtWebGraphAnalogIn57643Basic,
       "wtWebGraphAnalogIn57643Network": wtWebGraphAnalogIn57643Network,
       "wtWebGraphAnalogIn57643IpAddress": wtWebGraphAnalogIn57643IpAddress,
       "wtWebGraphAnalogIn57643SubnetMask": wtWebGraphAnalogIn57643SubnetMask,
       "wtWebGraphAnalogIn57643Gateway": wtWebGraphAnalogIn57643Gateway,
       "wtWebGraphAnalogIn57643DnsServer1": wtWebGraphAnalogIn57643DnsServer1,
       "wtWebGraphAnalogIn57643DnsServer2": wtWebGraphAnalogIn57643DnsServer2,
       "wtWebGraphAnalogIn57643AddConfig": wtWebGraphAnalogIn57643AddConfig,
       "wtWebGraphAnalogIn57643HTTP": wtWebGraphAnalogIn57643HTTP,
       "wtWebGraphAnalogIn57643Startup": wtWebGraphAnalogIn57643Startup,
       "wtWebGraphAnalogIn57643GetHeaderEnable": wtWebGraphAnalogIn57643GetHeaderEnable,
       "wtWebGraphAnalogIn57643HttpPort": wtWebGraphAnalogIn57643HttpPort,
       "wtWebGraphAnalogIn57643Mail": wtWebGraphAnalogIn57643Mail,
       "wtWebGraphAnalogIn57643MailAdName": wtWebGraphAnalogIn57643MailAdName,
       "wtWebGraphAnalogIn57643MailReply": wtWebGraphAnalogIn57643MailReply,
       "wtWebGraphAnalogIn57643MailServer": wtWebGraphAnalogIn57643MailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAnalogIn57643MailAuthentication": wtWebGraphAnalogIn57643MailAuthentication,
       "wtWebGraphAnalogIn57643MailAuthUser": wtWebGraphAnalogIn57643MailAuthUser,
       "wtWebGraphAnalogIn57643MailAuthPassword": wtWebGraphAnalogIn57643MailAuthPassword,
       "wtWebGraphAnalogIn57643MailPop3Server": wtWebGraphAnalogIn57643MailPop3Server,
       "wtWebGraphAnalogIn57643SNMP": wtWebGraphAnalogIn57643SNMP,
       "wtWebGraphAnalogIn57643SnmpCommunityStringRead": wtWebGraphAnalogIn57643SnmpCommunityStringRead,
       "wtWebGraphAnalogIn57643SnmpCommunityStringReadWrite": wtWebGraphAnalogIn57643SnmpCommunityStringReadWrite,
       "wtWebGraphAnalogIn57643SystemTrapManagerIP": wtWebGraphAnalogIn57643SystemTrapManagerIP,
       "wtWebGraphAnalogIn57643SystemTrapEnable": wtWebGraphAnalogIn57643SystemTrapEnable,
       "wtWebGraphAnalogIn57643SnmpEnable": wtWebGraphAnalogIn57643SnmpEnable,
       "wtWebGraphAnalogIn57643SnmpCommunityStringTrap": wtWebGraphAnalogIn57643SnmpCommunityStringTrap,
       "wtWebGraphAnalogIn57643UDP": wtWebGraphAnalogIn57643UDP,
       "wtWebGraphAnalogIn57643UdpPort": wtWebGraphAnalogIn57643UdpPort,
       "wtWebGraphAnalogIn57643UdpEnable": wtWebGraphAnalogIn57643UdpEnable,
       "wtWebGraphAnalogIn57643Syslog": wtWebGraphAnalogIn57643Syslog,
       "wtWebGraphAnalogIn57643SyslogServerIP": wtWebGraphAnalogIn57643SyslogServerIP,
       "wtWebGraphAnalogIn57643SyslogServerPort": wtWebGraphAnalogIn57643SyslogServerPort,
       "wtWebGraphAnalogIn57643SyslogSystemMessagesEnable": wtWebGraphAnalogIn57643SyslogSystemMessagesEnable,
       "wtWebGraphAnalogIn57643SyslogEnable": wtWebGraphAnalogIn57643SyslogEnable,
       "wtWebGraphAnalogIn57643FTP": wtWebGraphAnalogIn57643FTP,
       "wtWebGraphAnalogIn57643FTPServerIP": wtWebGraphAnalogIn57643FTPServerIP,
       "wtWebGraphAnalogIn57643FTPServerControlPort": wtWebGraphAnalogIn57643FTPServerControlPort,
       "wtWebGraphAnalogIn57643FTPUserName": wtWebGraphAnalogIn57643FTPUserName,
       "wtWebGraphAnalogIn57643FTPPassword": wtWebGraphAnalogIn57643FTPPassword,
       "wtWebGraphAnalogIn57643FTPAccount": wtWebGraphAnalogIn57643FTPAccount,
       "wtWebGraphAnalogIn57643FTPOption": wtWebGraphAnalogIn57643FTPOption,
       "wtWebGraphAnalogIn57643FTPEnable": wtWebGraphAnalogIn57643FTPEnable,
       "wtWebGraphAnalogIn57643Datalogger": wtWebGraphAnalogIn57643Datalogger,
       "wtWebGraphAnalogIn57643LoggerTimebase": wtWebGraphAnalogIn57643LoggerTimebase,
       "wtWebGraphAnalogIn57643LoggerSensorSel": wtWebGraphAnalogIn57643LoggerSensorSel,
       "wtWebGraphAnalogIn57643DisplaySensorSel": wtWebGraphAnalogIn57643DisplaySensorSel,
       "wtWebGraphAnalogIn57643SensorColorTable": wtWebGraphAnalogIn57643SensorColorTable,
       "wtWebGraphAnalogIn57643SensorColorEntry": wtWebGraphAnalogIn57643SensorColorEntry,
       "wtWebGraphAnalogIn57643SensorColor": wtWebGraphAnalogIn57643SensorColor,
       "wtWebGraphAnalogIn57643AutoScaleEnable": wtWebGraphAnalogIn57643AutoScaleEnable,
       "wtWebGraphAnalogIn57643VerticalUpperLimit": wtWebGraphAnalogIn57643VerticalUpperLimit,
       "wtWebGraphAnalogIn57643VerticalLowerLimit": wtWebGraphAnalogIn57643VerticalLowerLimit,
       "wtWebGraphAnalogIn57643HorizontalZoom": wtWebGraphAnalogIn57643HorizontalZoom,
       "wtWebGraphAnalogIn57643Alarm": wtWebGraphAnalogIn57643Alarm,
       "wtWebGraphAnalogIn57643AlarmCount": wtWebGraphAnalogIn57643AlarmCount,
       "wtWebGraphAnalogIn57643AlarmIfTable": wtWebGraphAnalogIn57643AlarmIfTable,
       "wtWebGraphAnalogIn57643AlarmIfEntry": wtWebGraphAnalogIn57643AlarmIfEntry,
       "wtWebGraphAnalogIn57643AlarmNo": wtWebGraphAnalogIn57643AlarmNo,
       "wtWebGraphAnalogIn57643AlarmTable": wtWebGraphAnalogIn57643AlarmTable,
       "wtWebGraphAnalogIn57643AlarmEntry": wtWebGraphAnalogIn57643AlarmEntry,
       "wtWebGraphAnalogIn57643AlarmTrigger": wtWebGraphAnalogIn57643AlarmTrigger,
       "wtWebGraphAnalogIn57643AlarmMin": wtWebGraphAnalogIn57643AlarmMin,
       "wtWebGraphAnalogIn57643AlarmMax": wtWebGraphAnalogIn57643AlarmMax,
       "wtWebGraphAnalogIn57643AlarmHysteresis": wtWebGraphAnalogIn57643AlarmHysteresis,
       "wtWebGraphAnalogIn57643AlarmDelay": wtWebGraphAnalogIn57643AlarmDelay,
       "wtWebGraphAnalogIn57643AlarmInterval": wtWebGraphAnalogIn57643AlarmInterval,
       "wtWebGraphAnalogIn57643AlarmEnable": wtWebGraphAnalogIn57643AlarmEnable,
       "wtWebGraphAnalogIn57643AlarmEMailAddr": wtWebGraphAnalogIn57643AlarmEMailAddr,
       "wtWebGraphAnalogIn57643AlarmMailSubject": wtWebGraphAnalogIn57643AlarmMailSubject,
       "wtWebGraphAnalogIn57643AlarmMailText": wtWebGraphAnalogIn57643AlarmMailText,
       "wtWebGraphAnalogIn57643AlarmManagerIP": wtWebGraphAnalogIn57643AlarmManagerIP,
       "wtWebGraphAnalogIn57643AlarmTrapText": wtWebGraphAnalogIn57643AlarmTrapText,
       "wtWebGraphAnalogIn57643AlarmMailOptions": wtWebGraphAnalogIn57643AlarmMailOptions,
       "wtWebGraphAnalogIn57643AlarmTcpIpAddr": wtWebGraphAnalogIn57643AlarmTcpIpAddr,
       "wtWebGraphAnalogIn57643AlarmTcpPort": wtWebGraphAnalogIn57643AlarmTcpPort,
       "wtWebGraphAnalogIn57643AlarmTcpText": wtWebGraphAnalogIn57643AlarmTcpText,
       "wtWebGraphAnalogIn57643AlarmClearMailSubject": wtWebGraphAnalogIn57643AlarmClearMailSubject,
       "wtWebGraphAnalogIn57643AlarmClearMailText": wtWebGraphAnalogIn57643AlarmClearMailText,
       "wtWebGraphAnalogIn57643AlarmClearTrapText": wtWebGraphAnalogIn57643AlarmClearTrapText,
       "wtWebGraphAnalogIn57643AlarmClearTcpText": wtWebGraphAnalogIn57643AlarmClearTcpText,
       "wtWebGraphAnalogIn57643Alarm2Min": wtWebGraphAnalogIn57643Alarm2Min,
       "wtWebGraphAnalogIn57643Alarm2Max": wtWebGraphAnalogIn57643Alarm2Max,
       "wtWebGraphAnalogIn57643Alarm2Hysteresis": wtWebGraphAnalogIn57643Alarm2Hysteresis,
       "wtWebGraphAnalogIn57643AlarmSyslogIpAddr": wtWebGraphAnalogIn57643AlarmSyslogIpAddr,
       "wtWebGraphAnalogIn57643AlarmSyslogPort": wtWebGraphAnalogIn57643AlarmSyslogPort,
       "wtWebGraphAnalogIn57643AlarmSyslogText": wtWebGraphAnalogIn57643AlarmSyslogText,
       "wtWebGraphAnalogIn57643AlarmSyslogClearText": wtWebGraphAnalogIn57643AlarmSyslogClearText,
       "wtWebGraphAnalogIn57643AlarmFtpDataPort": wtWebGraphAnalogIn57643AlarmFtpDataPort,
       "wtWebGraphAnalogIn57643AlarmFtpFileName": wtWebGraphAnalogIn57643AlarmFtpFileName,
       "wtWebGraphAnalogIn57643AlarmFtpText": wtWebGraphAnalogIn57643AlarmFtpText,
       "wtWebGraphAnalogIn57643AlarmFtpClearText": wtWebGraphAnalogIn57643AlarmFtpClearText,
       "wtWebGraphAnalogIn57643AlarmFtpOption": wtWebGraphAnalogIn57643AlarmFtpOption,
       "wtWebGraphAnalogIn57643AlarmTimerCron": wtWebGraphAnalogIn57643AlarmTimerCron,
       "wtWebGraphAnalogIn57643Graphics": wtWebGraphAnalogIn57643Graphics,
       "wtWebGraphAnalogIn57643GraphicsBase": wtWebGraphAnalogIn57643GraphicsBase,
       "wtWebGraphAnalogIn57643GraphicsBaseEnable": wtWebGraphAnalogIn57643GraphicsBaseEnable,
       "wtWebGraphAnalogIn57643GraphicsBaseWidth": wtWebGraphAnalogIn57643GraphicsBaseWidth,
       "wtWebGraphAnalogIn57643GraphicsBaseHeight": wtWebGraphAnalogIn57643GraphicsBaseHeight,
       "wtWebGraphAnalogIn57643GraphicsBaseFrameColor": wtWebGraphAnalogIn57643GraphicsBaseFrameColor,
       "wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor": wtWebGraphAnalogIn57643GraphicsBaseBackgroundColor,
       "wtWebGraphAnalogIn57643GraphicsBasePollingrate": wtWebGraphAnalogIn57643GraphicsBasePollingrate,
       "wtWebGraphAnalogIn57643GraphicsSelect": wtWebGraphAnalogIn57643GraphicsSelect,
       "wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel": wtWebGraphAnalogIn57643GraphicsSelectDisplaySensorSel,
       "wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem": wtWebGraphAnalogIn57643GraphicsSelectDisplayShowExtrem,
       "wtWebGraphAnalogIn57643SensorColor2Table": wtWebGraphAnalogIn57643SensorColor2Table,
       "wtWebGraphAnalogIn57643SensorColor2Entry": wtWebGraphAnalogIn57643SensorColor2Entry,
       "wtWebGraphAnalogIn57643GraphicsSensorColor": wtWebGraphAnalogIn57643GraphicsSensorColor,
       "wtWebGraphAnalogIn57643GraphicsSelectScale": wtWebGraphAnalogIn57643GraphicsSelectScale,
       "wtWebGraphAnalogIn57643GraphicsScale": wtWebGraphAnalogIn57643GraphicsScale,
       "wtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable": wtWebGraphAnalogIn57643GraphicsScaleAutoScaleEnable,
       "wtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable": wtWebGraphAnalogIn57643GraphicsScaleAutoFitEnable,
       "wtWebGraphAnalogIn57643GraphicsScale1Min": wtWebGraphAnalogIn57643GraphicsScale1Min,
       "wtWebGraphAnalogIn57643GraphicsScale2Min": wtWebGraphAnalogIn57643GraphicsScale2Min,
       "wtWebGraphAnalogIn57643GraphicsScale3Min": wtWebGraphAnalogIn57643GraphicsScale3Min,
       "wtWebGraphAnalogIn57643GraphicsScale4Min": wtWebGraphAnalogIn57643GraphicsScale4Min,
       "wtWebGraphAnalogIn57643GraphicsScale1Max": wtWebGraphAnalogIn57643GraphicsScale1Max,
       "wtWebGraphAnalogIn57643GraphicsScale2Max": wtWebGraphAnalogIn57643GraphicsScale2Max,
       "wtWebGraphAnalogIn57643GraphicsScale3Max": wtWebGraphAnalogIn57643GraphicsScale3Max,
       "wtWebGraphAnalogIn57643GraphicsScale4Max": wtWebGraphAnalogIn57643GraphicsScale4Max,
       "wtWebGraphAnalogIn57643GraphicsScale1Unit": wtWebGraphAnalogIn57643GraphicsScale1Unit,
       "wtWebGraphAnalogIn57643GraphicsScale2Unit": wtWebGraphAnalogIn57643GraphicsScale2Unit,
       "wtWebGraphAnalogIn57643GraphicsScale3Unit": wtWebGraphAnalogIn57643GraphicsScale3Unit,
       "wtWebGraphAnalogIn57643GraphicsScale4Unit": wtWebGraphAnalogIn57643GraphicsScale4Unit,
       "wtWebGraphAnalogIn57643Ports": wtWebGraphAnalogIn57643Ports,
       "wtWebGraphAnalogIn57643PortTable": wtWebGraphAnalogIn57643PortTable,
       "wtWebGraphAnalogIn57643PortEntry": wtWebGraphAnalogIn57643PortEntry,
       "wtWebGraphAnalogIn57643PortName": wtWebGraphAnalogIn57643PortName,
       "wtWebGraphAnalogIn57643PortText": wtWebGraphAnalogIn57643PortText,
       "wtWebGraphAnalogIn57643PortOffset1": wtWebGraphAnalogIn57643PortOffset1,
       "wtWebGraphAnalogIn57643SetPoint1": wtWebGraphAnalogIn57643SetPoint1,
       "wtWebGraphAnalogIn57643PortOffset2": wtWebGraphAnalogIn57643PortOffset2,
       "wtWebGraphAnalogIn57643SetPoint2": wtWebGraphAnalogIn57643SetPoint2,
       "wtWebGraphAnalogIn57643PortComment": wtWebGraphAnalogIn57643PortComment,
       "wtWebGraphAnalogIn57643PortSensorSelect": wtWebGraphAnalogIn57643PortSensorSelect,
       "wtWebGraphAnalogIn57643PortUnit": wtWebGraphAnalogIn57643PortUnit,
       "wtWebGraphAnalogIn57643PortScale0": wtWebGraphAnalogIn57643PortScale0,
       "wtWebGraphAnalogIn57643PortScale100": wtWebGraphAnalogIn57643PortScale100,
       "wtWebGraphAnalogIn57643Manufact": wtWebGraphAnalogIn57643Manufact,
       "wtWebGraphAnalogIn57643MfName": wtWebGraphAnalogIn57643MfName,
       "wtWebGraphAnalogIn57643MfAddr": wtWebGraphAnalogIn57643MfAddr,
       "wtWebGraphAnalogIn57643MfHotline": wtWebGraphAnalogIn57643MfHotline,
       "wtWebGraphAnalogIn57643MfInternet": wtWebGraphAnalogIn57643MfInternet,
       "wtWebGraphAnalogIn57643MfDeviceTyp": wtWebGraphAnalogIn57643MfDeviceTyp,
       "wtWebGraphAnalogIn57643MfOrderNo": wtWebGraphAnalogIn57643MfOrderNo,
       "wtWebGraphAnalogIn57643Diag": wtWebGraphAnalogIn57643Diag,
       "wtWebGraphAnalogIn57643DiagErrorCount": wtWebGraphAnalogIn57643DiagErrorCount,
       "wtWebGraphAnalogIn57643DiagBinaryError": wtWebGraphAnalogIn57643DiagBinaryError,
       "wtWebGraphAnalogIn57643DiagErrorIndex": wtWebGraphAnalogIn57643DiagErrorIndex,
       "wtWebGraphAnalogIn57643DiagErrorMessage": wtWebGraphAnalogIn57643DiagErrorMessage,
       "wtWebGraphAnalogIn57643DiagErrorClear": wtWebGraphAnalogIn57643DiagErrorClear}
)
