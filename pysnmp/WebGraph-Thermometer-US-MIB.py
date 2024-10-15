# SNMP MIB module (WebGraph-Thermometer-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-Thermometer-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:41 2024
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
_WtWebioAn1Graph_ObjectIdentity = ObjectIdentity
wtWebioAn1Graph = _WtWebioAn1Graph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8)
)
_WtWebioAn1GraphTemp_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphTemp = _WtWebioAn1GraphTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1)
)


class _WtWebioAn1GraphSensors_Type(Integer32):
    """Custom type wtWebioAn1GraphSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphSensors_Type.__name__ = "Integer32"
_WtWebioAn1GraphSensors_Object = MibScalar
wtWebioAn1GraphSensors = _WtWebioAn1GraphSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 1),
    _WtWebioAn1GraphSensors_Type()
)
wtWebioAn1GraphSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensors.setStatus("mandatory")
_WtWebioAn1GraphSensorTable_Object = MibTable
wtWebioAn1GraphSensorTable = _WtWebioAn1GraphSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorTable.setStatus("mandatory")
_WtWebioAn1GraphSensorEntry_Object = MibTableRow
wtWebioAn1GraphSensorEntry = _WtWebioAn1GraphSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 2, 1)
)
wtWebioAn1GraphSensorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorEntry.setStatus("mandatory")


class _WtWebioAn1GraphSensorNo_Type(Integer32):
    """Custom type wtWebioAn1GraphSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphSensorNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphSensorNo_Object = MibTableColumn
wtWebioAn1GraphSensorNo = _WtWebioAn1GraphSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 2, 1, 1),
    _WtWebioAn1GraphSensorNo_Type()
)
wtWebioAn1GraphSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorNo.setStatus("mandatory")
_WtWebioAn1GraphTempValueTable_Object = MibTable
wtWebioAn1GraphTempValueTable = _WtWebioAn1GraphTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphTempValueEntry_Object = MibTableRow
wtWebioAn1GraphTempValueEntry = _WtWebioAn1GraphTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 3, 1)
)
wtWebioAn1GraphTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphTempValueEntry.setStatus("mandatory")


class _WtWebioAn1GraphTempValue_Type(OctetString):
    """Custom type wtWebioAn1GraphTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebioAn1GraphTempValue_Type.__name__ = "OctetString"
_WtWebioAn1GraphTempValue_Object = MibTableColumn
wtWebioAn1GraphTempValue = _WtWebioAn1GraphTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 3, 1, 1),
    _WtWebioAn1GraphTempValue_Type()
)
wtWebioAn1GraphTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTempValue.setStatus("mandatory")
_WtWebioAn1GraphBinaryTempValueTable_Object = MibTable
wtWebioAn1GraphBinaryTempValueTable = _WtWebioAn1GraphBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphBinaryTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphBinaryTempValueEntry_Object = MibTableRow
wtWebioAn1GraphBinaryTempValueEntry = _WtWebioAn1GraphBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 4, 1)
)
wtWebioAn1GraphBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphBinaryTempValueEntry.setStatus("mandatory")
_WtWebioAn1GraphBinaryTempValue_Type = Integer32
_WtWebioAn1GraphBinaryTempValue_Object = MibTableColumn
wtWebioAn1GraphBinaryTempValue = _WtWebioAn1GraphBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 1, 4, 1, 1),
    _WtWebioAn1GraphBinaryTempValue_Type()
)
wtWebioAn1GraphBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphBinaryTempValue.setStatus("mandatory")
_WtWebioAn1GraphSessCntrl_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphSessCntrl = _WtWebioAn1GraphSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2)
)
_WtWebioAn1GraphSessCntrlPassword_Type = OctetString
_WtWebioAn1GraphSessCntrlPassword_Object = MibScalar
wtWebioAn1GraphSessCntrlPassword = _WtWebioAn1GraphSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2, 1),
    _WtWebioAn1GraphSessCntrlPassword_Type()
)
wtWebioAn1GraphSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSessCntrlPassword.setStatus("mandatory")


class _WtWebioAn1GraphSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebioAn1GraphSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphSessCntrl-NoSession", 0),
          ("wtWebioAn1GraphSessCntrl-Session", 1))
    )


_WtWebioAn1GraphSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphSessCntrlConfigMode_Object = MibScalar
wtWebioAn1GraphSessCntrlConfigMode = _WtWebioAn1GraphSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2, 2),
    _WtWebioAn1GraphSessCntrlConfigMode_Type()
)
wtWebioAn1GraphSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSessCntrlConfigMode.setStatus("mandatory")
_WtWebioAn1GraphSessCntrlLogout_Type = Integer32
_WtWebioAn1GraphSessCntrlLogout_Object = MibScalar
wtWebioAn1GraphSessCntrlLogout = _WtWebioAn1GraphSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2, 3),
    _WtWebioAn1GraphSessCntrlLogout_Type()
)
wtWebioAn1GraphSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSessCntrlLogout.setStatus("mandatory")
_WtWebioAn1GraphSessCntrlAdminPassword_Type = OctetString
_WtWebioAn1GraphSessCntrlAdminPassword_Object = MibScalar
wtWebioAn1GraphSessCntrlAdminPassword = _WtWebioAn1GraphSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2, 4),
    _WtWebioAn1GraphSessCntrlAdminPassword_Type()
)
wtWebioAn1GraphSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSessCntrlAdminPassword.setStatus("mandatory")
_WtWebioAn1GraphSessCntrlConfigPassword_Type = OctetString
_WtWebioAn1GraphSessCntrlConfigPassword_Object = MibScalar
wtWebioAn1GraphSessCntrlConfigPassword = _WtWebioAn1GraphSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 2, 5),
    _WtWebioAn1GraphSessCntrlConfigPassword_Type()
)
wtWebioAn1GraphSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSessCntrlConfigPassword.setStatus("mandatory")
_WtWebioAn1GraphConfig_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphConfig = _WtWebioAn1GraphConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3)
)
_WtWebioAn1GraphDevice_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphDevice = _WtWebioAn1GraphDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1)
)
_WtWebioAn1GraphText_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphText = _WtWebioAn1GraphText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 1)
)
_WtWebioAn1GraphDeviceName_Type = OctetString
_WtWebioAn1GraphDeviceName_Object = MibScalar
wtWebioAn1GraphDeviceName = _WtWebioAn1GraphDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 1, 1),
    _WtWebioAn1GraphDeviceName_Type()
)
wtWebioAn1GraphDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDeviceName.setStatus("mandatory")
_WtWebioAn1GraphDeviceText_Type = OctetString
_WtWebioAn1GraphDeviceText_Object = MibScalar
wtWebioAn1GraphDeviceText = _WtWebioAn1GraphDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 1, 2),
    _WtWebioAn1GraphDeviceText_Type()
)
wtWebioAn1GraphDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDeviceText.setStatus("mandatory")
_WtWebioAn1GraphDeviceLocation_Type = OctetString
_WtWebioAn1GraphDeviceLocation_Object = MibScalar
wtWebioAn1GraphDeviceLocation = _WtWebioAn1GraphDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 1, 3),
    _WtWebioAn1GraphDeviceLocation_Type()
)
wtWebioAn1GraphDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDeviceLocation.setStatus("mandatory")
_WtWebioAn1GraphDeviceContact_Type = OctetString
_WtWebioAn1GraphDeviceContact_Object = MibScalar
wtWebioAn1GraphDeviceContact = _WtWebioAn1GraphDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 1, 4),
    _WtWebioAn1GraphDeviceContact_Type()
)
wtWebioAn1GraphDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDeviceContact.setStatus("mandatory")
_WtWebioAn1GraphTimeDate_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphTimeDate = _WtWebioAn1GraphTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2)
)
_WtWebioAn1GraphTimeZone_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphTimeZone = _WtWebioAn1GraphTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1)
)
_WtWebioAn1GraphTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphTzOffsetHrs = _WtWebioAn1GraphTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 1),
    _WtWebioAn1GraphTzOffsetHrs_Type()
)
wtWebioAn1GraphTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphTzOffsetMin_Type = Integer32
_WtWebioAn1GraphTzOffsetMin_Object = MibScalar
wtWebioAn1GraphTzOffsetMin = _WtWebioAn1GraphTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 2),
    _WtWebioAn1GraphTzOffsetMin_Type()
)
wtWebioAn1GraphTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphTzEnable_Object = MibScalar
wtWebioAn1GraphTzEnable = _WtWebioAn1GraphTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 3),
    _WtWebioAn1GraphTzEnable_Type()
)
wtWebioAn1GraphTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTzEnable.setStatus("mandatory")
_WtWebioAn1GraphStTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphStTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphStTzOffsetHrs = _WtWebioAn1GraphStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 4),
    _WtWebioAn1GraphStTzOffsetHrs_Type()
)
wtWebioAn1GraphStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphStTzOffsetMin_Type = Integer32
_WtWebioAn1GraphStTzOffsetMin_Object = MibScalar
wtWebioAn1GraphStTzOffsetMin = _WtWebioAn1GraphStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 5),
    _WtWebioAn1GraphStTzOffsetMin_Type()
)
wtWebioAn1GraphStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphStTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphStTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphStTzEnable_Object = MibScalar
wtWebioAn1GraphStTzEnable = _WtWebioAn1GraphStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 6),
    _WtWebioAn1GraphStTzEnable_Type()
)
wtWebioAn1GraphStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzEnable.setStatus("mandatory")


class _WtWebioAn1GraphStTzStartMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStartMonth based on Integer32"""
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
        *(("wtWebioAn1GraphStartMonth-April", 4),
          ("wtWebioAn1GraphStartMonth-August", 8),
          ("wtWebioAn1GraphStartMonth-December", 12),
          ("wtWebioAn1GraphStartMonth-February", 2),
          ("wtWebioAn1GraphStartMonth-January", 1),
          ("wtWebioAn1GraphStartMonth-July", 7),
          ("wtWebioAn1GraphStartMonth-June", 6),
          ("wtWebioAn1GraphStartMonth-March", 3),
          ("wtWebioAn1GraphStartMonth-May", 5),
          ("wtWebioAn1GraphStartMonth-November", 11),
          ("wtWebioAn1GraphStartMonth-October", 10),
          ("wtWebioAn1GraphStartMonth-September", 9))
    )


_WtWebioAn1GraphStTzStartMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStartMonth_Object = MibScalar
wtWebioAn1GraphStTzStartMonth = _WtWebioAn1GraphStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 7),
    _WtWebioAn1GraphStTzStartMonth_Type()
)
wtWebioAn1GraphStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStartMonth.setStatus("mandatory")


class _WtWebioAn1GraphStTzStartMode_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStartMode based on Integer32"""
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
        *(("wtWebioAn1GraphStartMode-first", 1),
          ("wtWebioAn1GraphStartMode-fourth", 4),
          ("wtWebioAn1GraphStartMode-last", 5),
          ("wtWebioAn1GraphStartMode-second", 2),
          ("wtWebioAn1GraphStartMode-third", 3))
    )


_WtWebioAn1GraphStTzStartMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStartMode_Object = MibScalar
wtWebioAn1GraphStTzStartMode = _WtWebioAn1GraphStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 8),
    _WtWebioAn1GraphStTzStartMode_Type()
)
wtWebioAn1GraphStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStartMode.setStatus("mandatory")


class _WtWebioAn1GraphStTzStartWday_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStartWday based on Integer32"""
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
        *(("wtWebioAn1GraphStartWday-Friday", 6),
          ("wtWebioAn1GraphStartWday-Monday", 2),
          ("wtWebioAn1GraphStartWday-Saturday", 7),
          ("wtWebioAn1GraphStartWday-Sunday", 1),
          ("wtWebioAn1GraphStartWday-Thursday", 4),
          ("wtWebioAn1GraphStartWday-Tuesday", 3),
          ("wtWebioAn1GraphStartWday-Wednesday", 5))
    )


_WtWebioAn1GraphStTzStartWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStartWday_Object = MibScalar
wtWebioAn1GraphStTzStartWday = _WtWebioAn1GraphStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 9),
    _WtWebioAn1GraphStTzStartWday_Type()
)
wtWebioAn1GraphStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStartWday.setStatus("mandatory")
_WtWebioAn1GraphStTzStartHrs_Type = Integer32
_WtWebioAn1GraphStTzStartHrs_Object = MibScalar
wtWebioAn1GraphStTzStartHrs = _WtWebioAn1GraphStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 10),
    _WtWebioAn1GraphStTzStartHrs_Type()
)
wtWebioAn1GraphStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStartHrs.setStatus("mandatory")
_WtWebioAn1GraphStTzStartMin_Type = Integer32
_WtWebioAn1GraphStTzStartMin_Object = MibScalar
wtWebioAn1GraphStTzStartMin = _WtWebioAn1GraphStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 11),
    _WtWebioAn1GraphStTzStartMin_Type()
)
wtWebioAn1GraphStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStartMin.setStatus("mandatory")


class _WtWebioAn1GraphStTzStopMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStopMonth based on Integer32"""
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
        *(("wtWebioAn1GraphStopMonth-April", 4),
          ("wtWebioAn1GraphStopMonth-August", 8),
          ("wtWebioAn1GraphStopMonth-December", 12),
          ("wtWebioAn1GraphStopMonth-February", 2),
          ("wtWebioAn1GraphStopMonth-January", 1),
          ("wtWebioAn1GraphStopMonth-July", 7),
          ("wtWebioAn1GraphStopMonth-June", 6),
          ("wtWebioAn1GraphStopMonth-March", 3),
          ("wtWebioAn1GraphStopMonth-May", 5),
          ("wtWebioAn1GraphStopMonth-November", 11),
          ("wtWebioAn1GraphStopMonth-October", 10),
          ("wtWebioAn1GraphStopMonth-September", 9))
    )


_WtWebioAn1GraphStTzStopMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStopMonth_Object = MibScalar
wtWebioAn1GraphStTzStopMonth = _WtWebioAn1GraphStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 12),
    _WtWebioAn1GraphStTzStopMonth_Type()
)
wtWebioAn1GraphStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStopMonth.setStatus("mandatory")


class _WtWebioAn1GraphStTzStopMode_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStopMode based on Integer32"""
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
        *(("wtWebioAn1GraphStopMode-first", 1),
          ("wtWebioAn1GraphStopMode-fourth", 4),
          ("wtWebioAn1GraphStopMode-last", 5),
          ("wtWebioAn1GraphStopMode-second", 2),
          ("wtWebioAn1GraphStopMode-third", 3))
    )


_WtWebioAn1GraphStTzStopMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStopMode_Object = MibScalar
wtWebioAn1GraphStTzStopMode = _WtWebioAn1GraphStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 13),
    _WtWebioAn1GraphStTzStopMode_Type()
)
wtWebioAn1GraphStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStopMode.setStatus("mandatory")


class _WtWebioAn1GraphStTzStopWday_Type(Integer32):
    """Custom type wtWebioAn1GraphStTzStopWday based on Integer32"""
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
        *(("wtWebioAn1GraphStopWday-Friday", 6),
          ("wtWebioAn1GraphStopWday-Monday", 2),
          ("wtWebioAn1GraphStopWday-Saturday", 7),
          ("wtWebioAn1GraphStopWday-Sunday", 1),
          ("wtWebioAn1GraphStopWday-Thursday", 4),
          ("wtWebioAn1GraphStopWday-Tuesday", 3),
          ("wtWebioAn1GraphStopWday-Wednesday", 5))
    )


_WtWebioAn1GraphStTzStopWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphStTzStopWday_Object = MibScalar
wtWebioAn1GraphStTzStopWday = _WtWebioAn1GraphStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 14),
    _WtWebioAn1GraphStTzStopWday_Type()
)
wtWebioAn1GraphStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStopWday.setStatus("mandatory")
_WtWebioAn1GraphStTzStopHrs_Type = Integer32
_WtWebioAn1GraphStTzStopHrs_Object = MibScalar
wtWebioAn1GraphStTzStopHrs = _WtWebioAn1GraphStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 15),
    _WtWebioAn1GraphStTzStopHrs_Type()
)
wtWebioAn1GraphStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStopHrs.setStatus("mandatory")
_WtWebioAn1GraphStTzStopMin_Type = Integer32
_WtWebioAn1GraphStTzStopMin_Object = MibScalar
wtWebioAn1GraphStTzStopMin = _WtWebioAn1GraphStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 1, 16),
    _WtWebioAn1GraphStTzStopMin_Type()
)
wtWebioAn1GraphStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStTzStopMin.setStatus("mandatory")
_WtWebioAn1GraphTimeServer_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphTimeServer = _WtWebioAn1GraphTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 2)
)
_WtWebioAn1GraphTimeServer1_Type = OctetString
_WtWebioAn1GraphTimeServer1_Object = MibScalar
wtWebioAn1GraphTimeServer1 = _WtWebioAn1GraphTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 2, 1),
    _WtWebioAn1GraphTimeServer1_Type()
)
wtWebioAn1GraphTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTimeServer1.setStatus("mandatory")
_WtWebioAn1GraphTimeServer2_Type = OctetString
_WtWebioAn1GraphTimeServer2_Object = MibScalar
wtWebioAn1GraphTimeServer2 = _WtWebioAn1GraphTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 2, 2),
    _WtWebioAn1GraphTimeServer2_Type()
)
wtWebioAn1GraphTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTimeServer2.setStatus("mandatory")


class _WtWebioAn1GraphTsEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphTsEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphTsEnable_Object = MibScalar
wtWebioAn1GraphTsEnable = _WtWebioAn1GraphTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 2, 3),
    _WtWebioAn1GraphTsEnable_Type()
)
wtWebioAn1GraphTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTsEnable.setStatus("mandatory")
_WtWebioAn1GraphTsSyncTime_Type = Integer32
_WtWebioAn1GraphTsSyncTime_Object = MibScalar
wtWebioAn1GraphTsSyncTime = _WtWebioAn1GraphTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 2, 4),
    _WtWebioAn1GraphTsSyncTime_Type()
)
wtWebioAn1GraphTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphTsSyncTime.setStatus("mandatory")
_WtWebioAn1GraphDeviceClock_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphDeviceClock = _WtWebioAn1GraphDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3)
)


class _WtWebioAn1GraphClockHrs_Type(Integer32):
    """Custom type wtWebioAn1GraphClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebioAn1GraphClockHrs_Type.__name__ = "Integer32"
_WtWebioAn1GraphClockHrs_Object = MibScalar
wtWebioAn1GraphClockHrs = _WtWebioAn1GraphClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3, 1),
    _WtWebioAn1GraphClockHrs_Type()
)
wtWebioAn1GraphClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphClockHrs.setStatus("mandatory")


class _WtWebioAn1GraphClockMin_Type(Integer32):
    """Custom type wtWebioAn1GraphClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebioAn1GraphClockMin_Type.__name__ = "Integer32"
_WtWebioAn1GraphClockMin_Object = MibScalar
wtWebioAn1GraphClockMin = _WtWebioAn1GraphClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3, 2),
    _WtWebioAn1GraphClockMin_Type()
)
wtWebioAn1GraphClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphClockMin.setStatus("mandatory")


class _WtWebioAn1GraphClockDay_Type(Integer32):
    """Custom type wtWebioAn1GraphClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebioAn1GraphClockDay_Type.__name__ = "Integer32"
_WtWebioAn1GraphClockDay_Object = MibScalar
wtWebioAn1GraphClockDay = _WtWebioAn1GraphClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3, 3),
    _WtWebioAn1GraphClockDay_Type()
)
wtWebioAn1GraphClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphClockDay.setStatus("mandatory")


class _WtWebioAn1GraphClockMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphClockMonth based on Integer32"""
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
        *(("wtWebioAn1GraphClockMonth-April", 4),
          ("wtWebioAn1GraphClockMonth-August", 8),
          ("wtWebioAn1GraphClockMonth-December", 12),
          ("wtWebioAn1GraphClockMonth-February", 2),
          ("wtWebioAn1GraphClockMonth-January", 1),
          ("wtWebioAn1GraphClockMonth-July", 7),
          ("wtWebioAn1GraphClockMonth-June", 6),
          ("wtWebioAn1GraphClockMonth-March", 3),
          ("wtWebioAn1GraphClockMonth-May", 5),
          ("wtWebioAn1GraphClockMonth-November", 11),
          ("wtWebioAn1GraphClockMonth-October", 10),
          ("wtWebioAn1GraphClockMonth-September", 9))
    )


_WtWebioAn1GraphClockMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphClockMonth_Object = MibScalar
wtWebioAn1GraphClockMonth = _WtWebioAn1GraphClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3, 4),
    _WtWebioAn1GraphClockMonth_Type()
)
wtWebioAn1GraphClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphClockMonth.setStatus("mandatory")


class _WtWebioAn1GraphClockYear_Type(Integer32):
    """Custom type wtWebioAn1GraphClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebioAn1GraphClockYear_Type.__name__ = "Integer32"
_WtWebioAn1GraphClockYear_Object = MibScalar
wtWebioAn1GraphClockYear = _WtWebioAn1GraphClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 2, 3, 5),
    _WtWebioAn1GraphClockYear_Type()
)
wtWebioAn1GraphClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphClockYear.setStatus("mandatory")
_WtWebioAn1GraphBasic_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphBasic = _WtWebioAn1GraphBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3)
)
_WtWebioAn1GraphNetwork_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNetwork = _WtWebioAn1GraphNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1)
)
_WtWebioAn1GraphIpAddress_Type = IpAddress
_WtWebioAn1GraphIpAddress_Object = MibScalar
wtWebioAn1GraphIpAddress = _WtWebioAn1GraphIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 1),
    _WtWebioAn1GraphIpAddress_Type()
)
wtWebioAn1GraphIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphIpAddress.setStatus("mandatory")
_WtWebioAn1GraphSubnetMask_Type = IpAddress
_WtWebioAn1GraphSubnetMask_Object = MibScalar
wtWebioAn1GraphSubnetMask = _WtWebioAn1GraphSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 2),
    _WtWebioAn1GraphSubnetMask_Type()
)
wtWebioAn1GraphSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSubnetMask.setStatus("mandatory")
_WtWebioAn1GraphGateway_Type = IpAddress
_WtWebioAn1GraphGateway_Object = MibScalar
wtWebioAn1GraphGateway = _WtWebioAn1GraphGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 3),
    _WtWebioAn1GraphGateway_Type()
)
wtWebioAn1GraphGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphGateway.setStatus("mandatory")
_WtWebioAn1GraphDnsServer1_Type = OctetString
_WtWebioAn1GraphDnsServer1_Object = MibScalar
wtWebioAn1GraphDnsServer1 = _WtWebioAn1GraphDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 4),
    _WtWebioAn1GraphDnsServer1_Type()
)
wtWebioAn1GraphDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDnsServer1.setStatus("mandatory")
_WtWebioAn1GraphDnsServer2_Type = OctetString
_WtWebioAn1GraphDnsServer2_Object = MibScalar
wtWebioAn1GraphDnsServer2 = _WtWebioAn1GraphDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 5),
    _WtWebioAn1GraphDnsServer2_Type()
)
wtWebioAn1GraphDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDnsServer2.setStatus("mandatory")
_WtWebioAn1GraphAddConfig_Type = OctetString
_WtWebioAn1GraphAddConfig_Object = MibScalar
wtWebioAn1GraphAddConfig = _WtWebioAn1GraphAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 1, 6),
    _WtWebioAn1GraphAddConfig_Type()
)
wtWebioAn1GraphAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAddConfig.setStatus("mandatory")
_WtWebioAn1GraphHTML_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphHTML = _WtWebioAn1GraphHTML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 2)
)
_WtWebioAn1GraphMail_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphMail = _WtWebioAn1GraphMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3)
)
_WtWebioAn1GraphMailAdName_Type = OctetString
_WtWebioAn1GraphMailAdName_Object = MibScalar
wtWebioAn1GraphMailAdName = _WtWebioAn1GraphMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 1),
    _WtWebioAn1GraphMailAdName_Type()
)
wtWebioAn1GraphMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailAdName.setStatus("mandatory")
_WtWebioAn1GraphMailReply_Type = OctetString
_WtWebioAn1GraphMailReply_Object = MibScalar
wtWebioAn1GraphMailReply = _WtWebioAn1GraphMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 2),
    _WtWebioAn1GraphMailReply_Type()
)
wtWebioAn1GraphMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailReply.setStatus("mandatory")
_WtWebioAn1GraphMailServer_Type = OctetString
_WtWebioAn1GraphMailServer_Object = MibScalar
wtWebioAn1GraphMailServer = _WtWebioAn1GraphMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 3),
    _WtWebioAn1GraphMailServer_Type()
)
wtWebioAn1GraphMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebioAn1GraphMailAuthentication_Type(OctetString):
    """Custom type wtWebioAn1GraphMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphMailAuthentication_Type.__name__ = "OctetString"
_WtWebioAn1GraphMailAuthentication_Object = MibScalar
wtWebioAn1GraphMailAuthentication = _WtWebioAn1GraphMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 5),
    _WtWebioAn1GraphMailAuthentication_Type()
)
wtWebioAn1GraphMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailAuthentication.setStatus("mandatory")
_WtWebioAn1GraphMailAuthUser_Type = OctetString
_WtWebioAn1GraphMailAuthUser_Object = MibScalar
wtWebioAn1GraphMailAuthUser = _WtWebioAn1GraphMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 6),
    _WtWebioAn1GraphMailAuthUser_Type()
)
wtWebioAn1GraphMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailAuthUser.setStatus("mandatory")
_WtWebioAn1GraphMailAuthPassword_Type = OctetString
_WtWebioAn1GraphMailAuthPassword_Object = MibScalar
wtWebioAn1GraphMailAuthPassword = _WtWebioAn1GraphMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 7),
    _WtWebioAn1GraphMailAuthPassword_Type()
)
wtWebioAn1GraphMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailAuthPassword.setStatus("mandatory")
_WtWebioAn1GraphMailPop3Server_Type = OctetString
_WtWebioAn1GraphMailPop3Server_Object = MibScalar
wtWebioAn1GraphMailPop3Server = _WtWebioAn1GraphMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 3, 8),
    _WtWebioAn1GraphMailPop3Server_Type()
)
wtWebioAn1GraphMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMailPop3Server.setStatus("mandatory")
_WtWebioAn1GraphSNMP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphSNMP = _WtWebioAn1GraphSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4)
)
_WtWebioAn1GraphSnmpCommunityStringRead_Type = OctetString
_WtWebioAn1GraphSnmpCommunityStringRead_Object = MibScalar
wtWebioAn1GraphSnmpCommunityStringRead = _WtWebioAn1GraphSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 1),
    _WtWebioAn1GraphSnmpCommunityStringRead_Type()
)
wtWebioAn1GraphSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSnmpCommunityStringRead.setStatus("mandatory")
_WtWebioAn1GraphSnmpCommunityStringReadWrite_Type = OctetString
_WtWebioAn1GraphSnmpCommunityStringReadWrite_Object = MibScalar
wtWebioAn1GraphSnmpCommunityStringReadWrite = _WtWebioAn1GraphSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 2),
    _WtWebioAn1GraphSnmpCommunityStringReadWrite_Type()
)
wtWebioAn1GraphSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebioAn1GraphSystemTrapManagerIP_Type = OctetString
_WtWebioAn1GraphSystemTrapManagerIP_Object = MibScalar
wtWebioAn1GraphSystemTrapManagerIP = _WtWebioAn1GraphSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 3),
    _WtWebioAn1GraphSystemTrapManagerIP_Type()
)
wtWebioAn1GraphSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSystemTrapManagerIP.setStatus("mandatory")


class _WtWebioAn1GraphSystemTrapEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphSystemTrapEnable_Object = MibScalar
wtWebioAn1GraphSystemTrapEnable = _WtWebioAn1GraphSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 4),
    _WtWebioAn1GraphSystemTrapEnable_Type()
)
wtWebioAn1GraphSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSystemTrapEnable.setStatus("mandatory")
_WtWebioAn1GraphSnmpEnable_Type = OctetString
_WtWebioAn1GraphSnmpEnable_Object = MibScalar
wtWebioAn1GraphSnmpEnable = _WtWebioAn1GraphSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 5),
    _WtWebioAn1GraphSnmpEnable_Type()
)
wtWebioAn1GraphSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSnmpEnable.setStatus("mandatory")
_WtWebioAn1GraphSnmpCommunityStringTrap_Type = OctetString
_WtWebioAn1GraphSnmpCommunityStringTrap_Object = MibScalar
wtWebioAn1GraphSnmpCommunityStringTrap = _WtWebioAn1GraphSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 4, 6),
    _WtWebioAn1GraphSnmpCommunityStringTrap_Type()
)
wtWebioAn1GraphSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebioAn1GraphUDP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphUDP = _WtWebioAn1GraphUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 5)
)


class _WtWebioAn1GraphUdpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphUdpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphUdpPort_Object = MibScalar
wtWebioAn1GraphUdpPort = _WtWebioAn1GraphUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 5, 1),
    _WtWebioAn1GraphUdpPort_Type()
)
wtWebioAn1GraphUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphUdpPort.setStatus("mandatory")
_WtWebioAn1GraphUdpEnable_Type = OctetString
_WtWebioAn1GraphUdpEnable_Object = MibScalar
wtWebioAn1GraphUdpEnable = _WtWebioAn1GraphUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 5, 2),
    _WtWebioAn1GraphUdpEnable_Type()
)
wtWebioAn1GraphUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphUdpEnable.setStatus("mandatory")
_WtWebioAn1GraphSyslog_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphSyslog = _WtWebioAn1GraphSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 6)
)
_WtWebioAn1GraphSyslogServerIP_Type = OctetString
_WtWebioAn1GraphSyslogServerIP_Object = MibScalar
wtWebioAn1GraphSyslogServerIP = _WtWebioAn1GraphSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 6, 1),
    _WtWebioAn1GraphSyslogServerIP_Type()
)
wtWebioAn1GraphSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSyslogServerIP.setStatus("mandatory")
_WtWebioAn1GraphSyslogServerPort_Type = Integer32
_WtWebioAn1GraphSyslogServerPort_Object = MibScalar
wtWebioAn1GraphSyslogServerPort = _WtWebioAn1GraphSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 6, 2),
    _WtWebioAn1GraphSyslogServerPort_Type()
)
wtWebioAn1GraphSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSyslogServerPort.setStatus("mandatory")


class _WtWebioAn1GraphSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphSyslogSystemMessagesEnable_Object = MibScalar
wtWebioAn1GraphSyslogSystemMessagesEnable = _WtWebioAn1GraphSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 6, 3),
    _WtWebioAn1GraphSyslogSystemMessagesEnable_Type()
)
wtWebioAn1GraphSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebioAn1GraphSyslogEnable_Type = OctetString
_WtWebioAn1GraphSyslogEnable_Object = MibScalar
wtWebioAn1GraphSyslogEnable = _WtWebioAn1GraphSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 6, 4),
    _WtWebioAn1GraphSyslogEnable_Type()
)
wtWebioAn1GraphSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSyslogEnable.setStatus("mandatory")
_WtWebioAn1GraphFTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphFTP = _WtWebioAn1GraphFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7)
)
_WtWebioAn1GraphFTPServerIP_Type = OctetString
_WtWebioAn1GraphFTPServerIP_Object = MibScalar
wtWebioAn1GraphFTPServerIP = _WtWebioAn1GraphFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 1),
    _WtWebioAn1GraphFTPServerIP_Type()
)
wtWebioAn1GraphFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPServerIP.setStatus("mandatory")
_WtWebioAn1GraphFTPServerControlPort_Type = Integer32
_WtWebioAn1GraphFTPServerControlPort_Object = MibScalar
wtWebioAn1GraphFTPServerControlPort = _WtWebioAn1GraphFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 2),
    _WtWebioAn1GraphFTPServerControlPort_Type()
)
wtWebioAn1GraphFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPServerControlPort.setStatus("mandatory")
_WtWebioAn1GraphFTPUserName_Type = OctetString
_WtWebioAn1GraphFTPUserName_Object = MibScalar
wtWebioAn1GraphFTPUserName = _WtWebioAn1GraphFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 3),
    _WtWebioAn1GraphFTPUserName_Type()
)
wtWebioAn1GraphFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPUserName.setStatus("mandatory")
_WtWebioAn1GraphFTPPassword_Type = OctetString
_WtWebioAn1GraphFTPPassword_Object = MibScalar
wtWebioAn1GraphFTPPassword = _WtWebioAn1GraphFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 4),
    _WtWebioAn1GraphFTPPassword_Type()
)
wtWebioAn1GraphFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPPassword.setStatus("mandatory")
_WtWebioAn1GraphFTPAccount_Type = OctetString
_WtWebioAn1GraphFTPAccount_Object = MibScalar
wtWebioAn1GraphFTPAccount = _WtWebioAn1GraphFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 5),
    _WtWebioAn1GraphFTPAccount_Type()
)
wtWebioAn1GraphFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPAccount.setStatus("mandatory")
_WtWebioAn1GraphFTPOption_Type = OctetString
_WtWebioAn1GraphFTPOption_Object = MibScalar
wtWebioAn1GraphFTPOption = _WtWebioAn1GraphFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 6),
    _WtWebioAn1GraphFTPOption_Type()
)
wtWebioAn1GraphFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPOption.setStatus("mandatory")
_WtWebioAn1GraphFTPEnable_Type = OctetString
_WtWebioAn1GraphFTPEnable_Object = MibScalar
wtWebioAn1GraphFTPEnable = _WtWebioAn1GraphFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 7, 7),
    _WtWebioAn1GraphFTPEnable_Type()
)
wtWebioAn1GraphFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphFTPEnable.setStatus("mandatory")
_WtWebioAn1GraphHTTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphHTTP = _WtWebioAn1GraphHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 8)
)
_WtWebioAn1GraphStartup_Type = OctetString
_WtWebioAn1GraphStartup_Object = MibScalar
wtWebioAn1GraphStartup = _WtWebioAn1GraphStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 8, 1),
    _WtWebioAn1GraphStartup_Type()
)
wtWebioAn1GraphStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphStartup.setStatus("mandatory")
_WtWebioAn1GraphGetHeaderEnable_Type = OctetString
_WtWebioAn1GraphGetHeaderEnable_Object = MibScalar
wtWebioAn1GraphGetHeaderEnable = _WtWebioAn1GraphGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 8, 2),
    _WtWebioAn1GraphGetHeaderEnable_Type()
)
wtWebioAn1GraphGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphGetHeaderEnable.setStatus("mandatory")


class _WtWebioAn1GraphHttpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphHttpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphHttpPort_Object = MibScalar
wtWebioAn1GraphHttpPort = _WtWebioAn1GraphHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 3, 8, 3),
    _WtWebioAn1GraphHttpPort_Type()
)
wtWebioAn1GraphHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphHttpPort.setStatus("mandatory")
_WtWebioAn1GraphDatalogger_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphDatalogger = _WtWebioAn1GraphDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4)
)


class _WtWebioAn1GraphLoggerTimebase_Type(Integer32):
    """Custom type wtWebioAn1GraphLoggerTimebase based on Integer32"""
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
        *(("wtWebioAn1GraphDatalogger-15Min", 3),
          ("wtWebioAn1GraphDatalogger-1Min", 1),
          ("wtWebioAn1GraphDatalogger-5Min", 2),
          ("wtWebioAn1GraphDatalogger-60Min", 4))
    )


_WtWebioAn1GraphLoggerTimebase_Type.__name__ = "Integer32"
_WtWebioAn1GraphLoggerTimebase_Object = MibScalar
wtWebioAn1GraphLoggerTimebase = _WtWebioAn1GraphLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 1),
    _WtWebioAn1GraphLoggerTimebase_Type()
)
wtWebioAn1GraphLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphLoggerTimebase.setStatus("mandatory")


class _WtWebioAn1GraphLoggerSensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphLoggerSensorSel_Object = MibScalar
wtWebioAn1GraphLoggerSensorSel = _WtWebioAn1GraphLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 2),
    _WtWebioAn1GraphLoggerSensorSel_Type()
)
wtWebioAn1GraphLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphLoggerSensorSel.setStatus("mandatory")


class _WtWebioAn1GraphDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphDisplaySensorSel = _WtWebioAn1GraphDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 3),
    _WtWebioAn1GraphDisplaySensorSel_Type()
)
wtWebioAn1GraphDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDisplaySensorSel.setStatus("mandatory")
_WtWebioAn1GraphSensorColorTable_Object = MibTable
wtWebioAn1GraphSensorColorTable = _WtWebioAn1GraphSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphSensorColorEntry_Object = MibTableRow
wtWebioAn1GraphSensorColorEntry = _WtWebioAn1GraphSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 4, 1)
)
wtWebioAn1GraphSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphSensorColor_Object = MibTableColumn
wtWebioAn1GraphSensorColor = _WtWebioAn1GraphSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 4, 1, 1),
    _WtWebioAn1GraphSensorColor_Type()
)
wtWebioAn1GraphSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphSensorColor.setStatus("mandatory")
_WtWebioAn1GraphAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphAutoScaleEnable = _WtWebioAn1GraphAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 5),
    _WtWebioAn1GraphAutoScaleEnable_Type()
)
wtWebioAn1GraphAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphVerticalUpperLimit_Type = OctetString
_WtWebioAn1GraphVerticalUpperLimit_Object = MibScalar
wtWebioAn1GraphVerticalUpperLimit = _WtWebioAn1GraphVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 6),
    _WtWebioAn1GraphVerticalUpperLimit_Type()
)
wtWebioAn1GraphVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphVerticalUpperLimit.setStatus("mandatory")
_WtWebioAn1GraphVerticalLowerLimit_Type = OctetString
_WtWebioAn1GraphVerticalLowerLimit_Object = MibScalar
wtWebioAn1GraphVerticalLowerLimit = _WtWebioAn1GraphVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 7),
    _WtWebioAn1GraphVerticalLowerLimit_Type()
)
wtWebioAn1GraphVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphVerticalLowerLimit.setStatus("mandatory")


class _WtWebioAn1GraphHorizontalZoom_Type(Integer32):
    """Custom type wtWebioAn1GraphHorizontalZoom based on Integer32"""
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
        *(("wtWebioAn1GraphZoom-25days", 6),
          ("wtWebioAn1GraphZoom-25min", 1),
          ("wtWebioAn1GraphZoom-30hrs", 4),
          ("wtWebioAn1GraphZoom-5days", 5),
          ("wtWebioAn1GraphZoom-5hrs", 3),
          ("wtWebioAn1GraphZoom-75min", 2))
    )


_WtWebioAn1GraphHorizontalZoom_Type.__name__ = "Integer32"
_WtWebioAn1GraphHorizontalZoom_Object = MibScalar
wtWebioAn1GraphHorizontalZoom = _WtWebioAn1GraphHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 4, 8),
    _WtWebioAn1GraphHorizontalZoom_Type()
)
wtWebioAn1GraphHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphHorizontalZoom.setStatus("mandatory")
_WtWebioAn1GraphAlarm_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphAlarm = _WtWebioAn1GraphAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5)
)


class _WtWebioAn1GraphAlarmCount_Type(Integer32):
    """Custom type wtWebioAn1GraphAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphAlarmCount_Type.__name__ = "Integer32"
_WtWebioAn1GraphAlarmCount_Object = MibScalar
wtWebioAn1GraphAlarmCount = _WtWebioAn1GraphAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 1),
    _WtWebioAn1GraphAlarmCount_Type()
)
wtWebioAn1GraphAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmCount.setStatus("mandatory")
_WtWebioAn1GraphAlarmIfTable_Object = MibTable
wtWebioAn1GraphAlarmIfTable = _WtWebioAn1GraphAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmIfTable.setStatus("mandatory")
_WtWebioAn1GraphAlarmIfEntry_Object = MibTableRow
wtWebioAn1GraphAlarmIfEntry = _WtWebioAn1GraphAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 2, 1)
)
wtWebioAn1GraphAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmIfEntry.setStatus("mandatory")


class _WtWebioAn1GraphAlarmNo_Type(Integer32):
    """Custom type wtWebioAn1GraphAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphAlarmNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphAlarmNo_Object = MibTableColumn
wtWebioAn1GraphAlarmNo = _WtWebioAn1GraphAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 2, 1, 1),
    _WtWebioAn1GraphAlarmNo_Type()
)
wtWebioAn1GraphAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmNo.setStatus("mandatory")
_WtWebioAn1GraphAlarmTable_Object = MibTable
wtWebioAn1GraphAlarmTable = _WtWebioAn1GraphAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTable.setStatus("mandatory")
_WtWebioAn1GraphAlarmEntry_Object = MibTableRow
wtWebioAn1GraphAlarmEntry = _WtWebioAn1GraphAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1)
)
wtWebioAn1GraphAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmEntry.setStatus("mandatory")


class _WtWebioAn1GraphAlarmTrigger_Type(OctetString):
    """Custom type wtWebioAn1GraphAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphAlarmTrigger_Type.__name__ = "OctetString"
_WtWebioAn1GraphAlarmTrigger_Object = MibTableColumn
wtWebioAn1GraphAlarmTrigger = _WtWebioAn1GraphAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 1),
    _WtWebioAn1GraphAlarmTrigger_Type()
)
wtWebioAn1GraphAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTrigger.setStatus("mandatory")
_WtWebioAn1GraphAlarmMin_Type = OctetString
_WtWebioAn1GraphAlarmMin_Object = MibTableColumn
wtWebioAn1GraphAlarmMin = _WtWebioAn1GraphAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 2),
    _WtWebioAn1GraphAlarmMin_Type()
)
wtWebioAn1GraphAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmMin.setStatus("mandatory")
_WtWebioAn1GraphAlarmMax_Type = OctetString
_WtWebioAn1GraphAlarmMax_Object = MibTableColumn
wtWebioAn1GraphAlarmMax = _WtWebioAn1GraphAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 3),
    _WtWebioAn1GraphAlarmMax_Type()
)
wtWebioAn1GraphAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmMax.setStatus("mandatory")
_WtWebioAn1GraphAlarmHysteresis_Type = OctetString
_WtWebioAn1GraphAlarmHysteresis_Object = MibTableColumn
wtWebioAn1GraphAlarmHysteresis = _WtWebioAn1GraphAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 4),
    _WtWebioAn1GraphAlarmHysteresis_Type()
)
wtWebioAn1GraphAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmHysteresis.setStatus("mandatory")
_WtWebioAn1GraphAlarmDelay_Type = OctetString
_WtWebioAn1GraphAlarmDelay_Object = MibTableColumn
wtWebioAn1GraphAlarmDelay = _WtWebioAn1GraphAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 5),
    _WtWebioAn1GraphAlarmDelay_Type()
)
wtWebioAn1GraphAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmDelay.setStatus("mandatory")
_WtWebioAn1GraphAlarmInterval_Type = OctetString
_WtWebioAn1GraphAlarmInterval_Object = MibTableColumn
wtWebioAn1GraphAlarmInterval = _WtWebioAn1GraphAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 6),
    _WtWebioAn1GraphAlarmInterval_Type()
)
wtWebioAn1GraphAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmInterval.setStatus("mandatory")


class _WtWebioAn1GraphAlarmEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphAlarmEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphAlarmEnable_Object = MibTableColumn
wtWebioAn1GraphAlarmEnable = _WtWebioAn1GraphAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 7),
    _WtWebioAn1GraphAlarmEnable_Type()
)
wtWebioAn1GraphAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmEnable.setStatus("mandatory")
_WtWebioAn1GraphAlarmEMailAddr_Type = OctetString
_WtWebioAn1GraphAlarmEMailAddr_Object = MibTableColumn
wtWebioAn1GraphAlarmEMailAddr = _WtWebioAn1GraphAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 8),
    _WtWebioAn1GraphAlarmEMailAddr_Type()
)
wtWebioAn1GraphAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmEMailAddr.setStatus("mandatory")
_WtWebioAn1GraphAlarmMailSubject_Type = OctetString
_WtWebioAn1GraphAlarmMailSubject_Object = MibTableColumn
wtWebioAn1GraphAlarmMailSubject = _WtWebioAn1GraphAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 9),
    _WtWebioAn1GraphAlarmMailSubject_Type()
)
wtWebioAn1GraphAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmMailSubject.setStatus("mandatory")
_WtWebioAn1GraphAlarmMailText_Type = OctetString
_WtWebioAn1GraphAlarmMailText_Object = MibTableColumn
wtWebioAn1GraphAlarmMailText = _WtWebioAn1GraphAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 10),
    _WtWebioAn1GraphAlarmMailText_Type()
)
wtWebioAn1GraphAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmMailText.setStatus("mandatory")
_WtWebioAn1GraphAlarmManagerIP_Type = OctetString
_WtWebioAn1GraphAlarmManagerIP_Object = MibTableColumn
wtWebioAn1GraphAlarmManagerIP = _WtWebioAn1GraphAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 11),
    _WtWebioAn1GraphAlarmManagerIP_Type()
)
wtWebioAn1GraphAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmManagerIP.setStatus("mandatory")
_WtWebioAn1GraphAlarmTrapText_Type = OctetString
_WtWebioAn1GraphAlarmTrapText_Object = MibTableColumn
wtWebioAn1GraphAlarmTrapText = _WtWebioAn1GraphAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 12),
    _WtWebioAn1GraphAlarmTrapText_Type()
)
wtWebioAn1GraphAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTrapText.setStatus("mandatory")


class _WtWebioAn1GraphAlarmMailOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphAlarmMailOptions_Object = MibTableColumn
wtWebioAn1GraphAlarmMailOptions = _WtWebioAn1GraphAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 13),
    _WtWebioAn1GraphAlarmMailOptions_Type()
)
wtWebioAn1GraphAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmMailOptions.setStatus("mandatory")
_WtWebioAn1GraphAlarmTcpIpAddr_Type = OctetString
_WtWebioAn1GraphAlarmTcpIpAddr_Object = MibTableColumn
wtWebioAn1GraphAlarmTcpIpAddr = _WtWebioAn1GraphAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 14),
    _WtWebioAn1GraphAlarmTcpIpAddr_Type()
)
wtWebioAn1GraphAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphAlarmTcpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphAlarmTcpPort_Object = MibTableColumn
wtWebioAn1GraphAlarmTcpPort = _WtWebioAn1GraphAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 15),
    _WtWebioAn1GraphAlarmTcpPort_Type()
)
wtWebioAn1GraphAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTcpPort.setStatus("mandatory")
_WtWebioAn1GraphAlarmTcpText_Type = OctetString
_WtWebioAn1GraphAlarmTcpText_Object = MibTableColumn
wtWebioAn1GraphAlarmTcpText = _WtWebioAn1GraphAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 16),
    _WtWebioAn1GraphAlarmTcpText_Type()
)
wtWebioAn1GraphAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTcpText.setStatus("mandatory")
_WtWebioAn1GraphAlarmClearMailSubject_Type = OctetString
_WtWebioAn1GraphAlarmClearMailSubject_Object = MibTableColumn
wtWebioAn1GraphAlarmClearMailSubject = _WtWebioAn1GraphAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 17),
    _WtWebioAn1GraphAlarmClearMailSubject_Type()
)
wtWebioAn1GraphAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmClearMailSubject.setStatus("mandatory")
_WtWebioAn1GraphAlarmClearMailText_Type = OctetString
_WtWebioAn1GraphAlarmClearMailText_Object = MibTableColumn
wtWebioAn1GraphAlarmClearMailText = _WtWebioAn1GraphAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 18),
    _WtWebioAn1GraphAlarmClearMailText_Type()
)
wtWebioAn1GraphAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmClearMailText.setStatus("mandatory")
_WtWebioAn1GraphAlarmClearTrapText_Type = OctetString
_WtWebioAn1GraphAlarmClearTrapText_Object = MibTableColumn
wtWebioAn1GraphAlarmClearTrapText = _WtWebioAn1GraphAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 19),
    _WtWebioAn1GraphAlarmClearTrapText_Type()
)
wtWebioAn1GraphAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmClearTrapText.setStatus("mandatory")
_WtWebioAn1GraphAlarmClearTcpText_Type = OctetString
_WtWebioAn1GraphAlarmClearTcpText_Object = MibTableColumn
wtWebioAn1GraphAlarmClearTcpText = _WtWebioAn1GraphAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 20),
    _WtWebioAn1GraphAlarmClearTcpText_Type()
)
wtWebioAn1GraphAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmClearTcpText.setStatus("mandatory")
_WtWebioAn1GraphAlarmSyslogIpAddr_Type = IpAddress
_WtWebioAn1GraphAlarmSyslogIpAddr_Object = MibTableColumn
wtWebioAn1GraphAlarmSyslogIpAddr = _WtWebioAn1GraphAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 21),
    _WtWebioAn1GraphAlarmSyslogIpAddr_Type()
)
wtWebioAn1GraphAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebioAn1GraphAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphAlarmSyslogPort_Object = MibTableColumn
wtWebioAn1GraphAlarmSyslogPort = _WtWebioAn1GraphAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 22),
    _WtWebioAn1GraphAlarmSyslogPort_Type()
)
wtWebioAn1GraphAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmSyslogPort.setStatus("mandatory")
_WtWebioAn1GraphAlarmSyslogText_Type = OctetString
_WtWebioAn1GraphAlarmSyslogText_Object = MibTableColumn
wtWebioAn1GraphAlarmSyslogText = _WtWebioAn1GraphAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 23),
    _WtWebioAn1GraphAlarmSyslogText_Type()
)
wtWebioAn1GraphAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmSyslogText.setStatus("mandatory")
_WtWebioAn1GraphAlarmSyslogClearText_Type = OctetString
_WtWebioAn1GraphAlarmSyslogClearText_Object = MibScalar
wtWebioAn1GraphAlarmSyslogClearText = _WtWebioAn1GraphAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 24),
    _WtWebioAn1GraphAlarmSyslogClearText_Type()
)
wtWebioAn1GraphAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmSyslogClearText.setStatus("mandatory")
_WtWebioAn1GraphAlarmFtpDataPort_Type = OctetString
_WtWebioAn1GraphAlarmFtpDataPort_Object = MibTableColumn
wtWebioAn1GraphAlarmFtpDataPort = _WtWebioAn1GraphAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 25),
    _WtWebioAn1GraphAlarmFtpDataPort_Type()
)
wtWebioAn1GraphAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmFtpDataPort.setStatus("mandatory")
_WtWebioAn1GraphAlarmFtpFileName_Type = OctetString
_WtWebioAn1GraphAlarmFtpFileName_Object = MibTableColumn
wtWebioAn1GraphAlarmFtpFileName = _WtWebioAn1GraphAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 26),
    _WtWebioAn1GraphAlarmFtpFileName_Type()
)
wtWebioAn1GraphAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmFtpFileName.setStatus("mandatory")
_WtWebioAn1GraphAlarmFtpText_Type = OctetString
_WtWebioAn1GraphAlarmFtpText_Object = MibTableColumn
wtWebioAn1GraphAlarmFtpText = _WtWebioAn1GraphAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 27),
    _WtWebioAn1GraphAlarmFtpText_Type()
)
wtWebioAn1GraphAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmFtpText.setStatus("mandatory")
_WtWebioAn1GraphAlarmFtpClearText_Type = OctetString
_WtWebioAn1GraphAlarmFtpClearText_Object = MibTableColumn
wtWebioAn1GraphAlarmFtpClearText = _WtWebioAn1GraphAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 28),
    _WtWebioAn1GraphAlarmFtpClearText_Type()
)
wtWebioAn1GraphAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmFtpClearText.setStatus("mandatory")


class _WtWebioAn1GraphAlarmFtpOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphAlarmFtpOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphAlarmFtpOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphAlarmFtpOptions_Object = MibScalar
wtWebioAn1GraphAlarmFtpOptions = _WtWebioAn1GraphAlarmFtpOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 29),
    _WtWebioAn1GraphAlarmFtpOptions_Type()
)
wtWebioAn1GraphAlarmFtpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmFtpOptions.setStatus("mandatory")
_WtWebioAn1GraphAlarmTimerCron_Type = OctetString
_WtWebioAn1GraphAlarmTimerCron_Object = MibTableColumn
wtWebioAn1GraphAlarmTimerCron = _WtWebioAn1GraphAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 1, 5, 3, 1, 30),
    _WtWebioAn1GraphAlarmTimerCron_Type()
)
wtWebioAn1GraphAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlarmTimerCron.setStatus("mandatory")
_WtWebioAn1GraphPorts_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPorts = _WtWebioAn1GraphPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2)
)
_WtWebioAn1GraphPortTable_Object = MibTable
wtWebioAn1GraphPortTable = _WtWebioAn1GraphPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortTable.setStatus("mandatory")
_WtWebioAn1GraphPortEntry_Object = MibTableRow
wtWebioAn1GraphPortEntry = _WtWebioAn1GraphPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1)
)
wtWebioAn1GraphPortEntry.setIndexNames(
    (0, "WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortEntry.setStatus("mandatory")
_WtWebioAn1GraphPortName_Type = OctetString
_WtWebioAn1GraphPortName_Object = MibTableColumn
wtWebioAn1GraphPortName = _WtWebioAn1GraphPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 1),
    _WtWebioAn1GraphPortName_Type()
)
wtWebioAn1GraphPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortName.setStatus("mandatory")
_WtWebioAn1GraphPortText_Type = OctetString
_WtWebioAn1GraphPortText_Object = MibTableColumn
wtWebioAn1GraphPortText = _WtWebioAn1GraphPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 2),
    _WtWebioAn1GraphPortText_Type()
)
wtWebioAn1GraphPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortText.setStatus("mandatory")
_WtWebioAn1GraphPortOffset1_Type = OctetString
_WtWebioAn1GraphPortOffset1_Object = MibTableColumn
wtWebioAn1GraphPortOffset1 = _WtWebioAn1GraphPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 3),
    _WtWebioAn1GraphPortOffset1_Type()
)
wtWebioAn1GraphPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortOffset1.setStatus("mandatory")
_WtWebioAn1GraphPortTemperature1_Type = OctetString
_WtWebioAn1GraphPortTemperature1_Object = MibTableColumn
wtWebioAn1GraphPortTemperature1 = _WtWebioAn1GraphPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 4),
    _WtWebioAn1GraphPortTemperature1_Type()
)
wtWebioAn1GraphPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortTemperature1.setStatus("mandatory")
_WtWebioAn1GraphPortOffset2_Type = OctetString
_WtWebioAn1GraphPortOffset2_Object = MibTableColumn
wtWebioAn1GraphPortOffset2 = _WtWebioAn1GraphPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 5),
    _WtWebioAn1GraphPortOffset2_Type()
)
wtWebioAn1GraphPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortOffset2.setStatus("mandatory")
_WtWebioAn1GraphPortTemperature2_Type = OctetString
_WtWebioAn1GraphPortTemperature2_Object = MibTableColumn
wtWebioAn1GraphPortTemperature2 = _WtWebioAn1GraphPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 6),
    _WtWebioAn1GraphPortTemperature2_Type()
)
wtWebioAn1GraphPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortTemperature2.setStatus("mandatory")
_WtWebioAn1GraphPortComment_Type = OctetString
_WtWebioAn1GraphPortComment_Object = MibTableColumn
wtWebioAn1GraphPortComment = _WtWebioAn1GraphPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 2, 1, 1, 7),
    _WtWebioAn1GraphPortComment_Type()
)
wtWebioAn1GraphPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortComment.setStatus("mandatory")
_WtWebioAn1GraphManufact_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphManufact = _WtWebioAn1GraphManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3)
)
_WtWebioAn1GraphMfName_Type = OctetString
_WtWebioAn1GraphMfName_Object = MibScalar
wtWebioAn1GraphMfName = _WtWebioAn1GraphMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 1),
    _WtWebioAn1GraphMfName_Type()
)
wtWebioAn1GraphMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfName.setStatus("mandatory")
_WtWebioAn1GraphMfAddr_Type = OctetString
_WtWebioAn1GraphMfAddr_Object = MibScalar
wtWebioAn1GraphMfAddr = _WtWebioAn1GraphMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 2),
    _WtWebioAn1GraphMfAddr_Type()
)
wtWebioAn1GraphMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfAddr.setStatus("mandatory")
_WtWebioAn1GraphMfHotline_Type = OctetString
_WtWebioAn1GraphMfHotline_Object = MibScalar
wtWebioAn1GraphMfHotline = _WtWebioAn1GraphMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 3),
    _WtWebioAn1GraphMfHotline_Type()
)
wtWebioAn1GraphMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfHotline.setStatus("mandatory")
_WtWebioAn1GraphMfInternet_Type = OctetString
_WtWebioAn1GraphMfInternet_Object = MibScalar
wtWebioAn1GraphMfInternet = _WtWebioAn1GraphMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 4),
    _WtWebioAn1GraphMfInternet_Type()
)
wtWebioAn1GraphMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfInternet.setStatus("mandatory")
_WtWebioAn1GraphMfDeviceTyp_Type = OctetString
_WtWebioAn1GraphMfDeviceTyp_Object = MibScalar
wtWebioAn1GraphMfDeviceTyp = _WtWebioAn1GraphMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 5),
    _WtWebioAn1GraphMfDeviceTyp_Type()
)
wtWebioAn1GraphMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfDeviceTyp.setStatus("mandatory")
_WtWebioAn1GraphMfOrderNo_Type = OctetString
_WtWebioAn1GraphMfOrderNo_Object = MibScalar
wtWebioAn1GraphMfOrderNo = _WtWebioAn1GraphMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 3, 6),
    _WtWebioAn1GraphMfOrderNo_Type()
)
wtWebioAn1GraphMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphMfOrderNo.setStatus("mandatory")
_WtWebioAn1GraphDiag_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphDiag = _WtWebioAn1GraphDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4)
)
_WtWebioAn1GraphDiagErrorCount_Type = Integer32
_WtWebioAn1GraphDiagErrorCount_Object = MibScalar
wtWebioAn1GraphDiagErrorCount = _WtWebioAn1GraphDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4, 1),
    _WtWebioAn1GraphDiagErrorCount_Type()
)
wtWebioAn1GraphDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDiagErrorCount.setStatus("mandatory")
_WtWebioAn1GraphDiagBinaryError_Type = OctetString
_WtWebioAn1GraphDiagBinaryError_Object = MibScalar
wtWebioAn1GraphDiagBinaryError = _WtWebioAn1GraphDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4, 2),
    _WtWebioAn1GraphDiagBinaryError_Type()
)
wtWebioAn1GraphDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDiagBinaryError.setStatus("mandatory")
_WtWebioAn1GraphDiagErrorIndex_Type = Integer32
_WtWebioAn1GraphDiagErrorIndex_Object = MibScalar
wtWebioAn1GraphDiagErrorIndex = _WtWebioAn1GraphDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4, 3),
    _WtWebioAn1GraphDiagErrorIndex_Type()
)
wtWebioAn1GraphDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDiagErrorIndex.setStatus("mandatory")
_WtWebioAn1GraphDiagErrorMessage_Type = OctetString
_WtWebioAn1GraphDiagErrorMessage_Object = MibScalar
wtWebioAn1GraphDiagErrorMessage = _WtWebioAn1GraphDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4, 4),
    _WtWebioAn1GraphDiagErrorMessage_Type()
)
wtWebioAn1GraphDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDiagErrorMessage.setStatus("mandatory")
_WtWebioAn1GraphDiagErrorClear_Type = Integer32
_WtWebioAn1GraphDiagErrorClear_Object = MibScalar
wtWebioAn1GraphDiagErrorClear = _WtWebioAn1GraphDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 3, 4, 5),
    _WtWebioAn1GraphDiagErrorClear_Type()
)
wtWebioAn1GraphDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebioAn1GraphAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 31)
)
wtWebioAn1GraphAlert1.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert1.setStatus(
        ""
    )

wtWebioAn1GraphAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 32)
)
wtWebioAn1GraphAlert2.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert2.setStatus(
        ""
    )

wtWebioAn1GraphAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 33)
)
wtWebioAn1GraphAlert3.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert3.setStatus(
        ""
    )

wtWebioAn1GraphAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 34)
)
wtWebioAn1GraphAlert4.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert4.setStatus(
        ""
    )

wtWebioAn1GraphAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 35)
)
wtWebioAn1GraphAlert5.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert5.setStatus(
        ""
    )

wtWebioAn1GraphAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 36)
)
wtWebioAn1GraphAlert6.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert6.setStatus(
        ""
    )

wtWebioAn1GraphAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 37)
)
wtWebioAn1GraphAlert7.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert7.setStatus(
        ""
    )

wtWebioAn1GraphAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 38)
)
wtWebioAn1GraphAlert8.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert8.setStatus(
        ""
    )

wtWebioAn1GraphAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 91)
)
wtWebioAn1GraphAlert9.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert9.setStatus(
        ""
    )

wtWebioAn1GraphAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 92)
)
wtWebioAn1GraphAlert10.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert10.setStatus(
        ""
    )

wtWebioAn1GraphAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 93)
)
wtWebioAn1GraphAlert11.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert11.setStatus(
        ""
    )

wtWebioAn1GraphAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 94)
)
wtWebioAn1GraphAlert12.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert12.setStatus(
        ""
    )

wtWebioAn1GraphAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 95)
)
wtWebioAn1GraphAlert13.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert13.setStatus(
        ""
    )

wtWebioAn1GraphAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 96)
)
wtWebioAn1GraphAlert14.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert14.setStatus(
        ""
    )

wtWebioAn1GraphAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 97)
)
wtWebioAn1GraphAlert15.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert15.setStatus(
        ""
    )

wtWebioAn1GraphAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 98)
)
wtWebioAn1GraphAlert16.setObjects(
    ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlert16.setStatus(
        ""
    )

wtWebioAn1GraphAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 8, 0, 110)
)
wtWebioAn1GraphAlertDiag.setObjects(
      *(("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphDiagErrorIndex"),
        ("WebGraph-Thermometer-US-MIB", "wtWebioAn1GraphDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermometer-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebioAn1Graph": wtWebioAn1Graph,
       "wtWebioAn1GraphAlert1": wtWebioAn1GraphAlert1,
       "wtWebioAn1GraphAlert2": wtWebioAn1GraphAlert2,
       "wtWebioAn1GraphAlert3": wtWebioAn1GraphAlert3,
       "wtWebioAn1GraphAlert4": wtWebioAn1GraphAlert4,
       "wtWebioAn1GraphAlert5": wtWebioAn1GraphAlert5,
       "wtWebioAn1GraphAlert6": wtWebioAn1GraphAlert6,
       "wtWebioAn1GraphAlert7": wtWebioAn1GraphAlert7,
       "wtWebioAn1GraphAlert8": wtWebioAn1GraphAlert8,
       "wtWebioAn1GraphAlert9": wtWebioAn1GraphAlert9,
       "wtWebioAn1GraphAlert10": wtWebioAn1GraphAlert10,
       "wtWebioAn1GraphAlert11": wtWebioAn1GraphAlert11,
       "wtWebioAn1GraphAlert12": wtWebioAn1GraphAlert12,
       "wtWebioAn1GraphAlert13": wtWebioAn1GraphAlert13,
       "wtWebioAn1GraphAlert14": wtWebioAn1GraphAlert14,
       "wtWebioAn1GraphAlert15": wtWebioAn1GraphAlert15,
       "wtWebioAn1GraphAlert16": wtWebioAn1GraphAlert16,
       "wtWebioAn1GraphAlertDiag": wtWebioAn1GraphAlertDiag,
       "wtWebioAn1GraphTemp": wtWebioAn1GraphTemp,
       "wtWebioAn1GraphSensors": wtWebioAn1GraphSensors,
       "wtWebioAn1GraphSensorTable": wtWebioAn1GraphSensorTable,
       "wtWebioAn1GraphSensorEntry": wtWebioAn1GraphSensorEntry,
       "wtWebioAn1GraphSensorNo": wtWebioAn1GraphSensorNo,
       "wtWebioAn1GraphTempValueTable": wtWebioAn1GraphTempValueTable,
       "wtWebioAn1GraphTempValueEntry": wtWebioAn1GraphTempValueEntry,
       "wtWebioAn1GraphTempValue": wtWebioAn1GraphTempValue,
       "wtWebioAn1GraphBinaryTempValueTable": wtWebioAn1GraphBinaryTempValueTable,
       "wtWebioAn1GraphBinaryTempValueEntry": wtWebioAn1GraphBinaryTempValueEntry,
       "wtWebioAn1GraphBinaryTempValue": wtWebioAn1GraphBinaryTempValue,
       "wtWebioAn1GraphSessCntrl": wtWebioAn1GraphSessCntrl,
       "wtWebioAn1GraphSessCntrlPassword": wtWebioAn1GraphSessCntrlPassword,
       "wtWebioAn1GraphSessCntrlConfigMode": wtWebioAn1GraphSessCntrlConfigMode,
       "wtWebioAn1GraphSessCntrlLogout": wtWebioAn1GraphSessCntrlLogout,
       "wtWebioAn1GraphSessCntrlAdminPassword": wtWebioAn1GraphSessCntrlAdminPassword,
       "wtWebioAn1GraphSessCntrlConfigPassword": wtWebioAn1GraphSessCntrlConfigPassword,
       "wtWebioAn1GraphConfig": wtWebioAn1GraphConfig,
       "wtWebioAn1GraphDevice": wtWebioAn1GraphDevice,
       "wtWebioAn1GraphText": wtWebioAn1GraphText,
       "wtWebioAn1GraphDeviceName": wtWebioAn1GraphDeviceName,
       "wtWebioAn1GraphDeviceText": wtWebioAn1GraphDeviceText,
       "wtWebioAn1GraphDeviceLocation": wtWebioAn1GraphDeviceLocation,
       "wtWebioAn1GraphDeviceContact": wtWebioAn1GraphDeviceContact,
       "wtWebioAn1GraphTimeDate": wtWebioAn1GraphTimeDate,
       "wtWebioAn1GraphTimeZone": wtWebioAn1GraphTimeZone,
       "wtWebioAn1GraphTzOffsetHrs": wtWebioAn1GraphTzOffsetHrs,
       "wtWebioAn1GraphTzOffsetMin": wtWebioAn1GraphTzOffsetMin,
       "wtWebioAn1GraphTzEnable": wtWebioAn1GraphTzEnable,
       "wtWebioAn1GraphStTzOffsetHrs": wtWebioAn1GraphStTzOffsetHrs,
       "wtWebioAn1GraphStTzOffsetMin": wtWebioAn1GraphStTzOffsetMin,
       "wtWebioAn1GraphStTzEnable": wtWebioAn1GraphStTzEnable,
       "wtWebioAn1GraphStTzStartMonth": wtWebioAn1GraphStTzStartMonth,
       "wtWebioAn1GraphStTzStartMode": wtWebioAn1GraphStTzStartMode,
       "wtWebioAn1GraphStTzStartWday": wtWebioAn1GraphStTzStartWday,
       "wtWebioAn1GraphStTzStartHrs": wtWebioAn1GraphStTzStartHrs,
       "wtWebioAn1GraphStTzStartMin": wtWebioAn1GraphStTzStartMin,
       "wtWebioAn1GraphStTzStopMonth": wtWebioAn1GraphStTzStopMonth,
       "wtWebioAn1GraphStTzStopMode": wtWebioAn1GraphStTzStopMode,
       "wtWebioAn1GraphStTzStopWday": wtWebioAn1GraphStTzStopWday,
       "wtWebioAn1GraphStTzStopHrs": wtWebioAn1GraphStTzStopHrs,
       "wtWebioAn1GraphStTzStopMin": wtWebioAn1GraphStTzStopMin,
       "wtWebioAn1GraphTimeServer": wtWebioAn1GraphTimeServer,
       "wtWebioAn1GraphTimeServer1": wtWebioAn1GraphTimeServer1,
       "wtWebioAn1GraphTimeServer2": wtWebioAn1GraphTimeServer2,
       "wtWebioAn1GraphTsEnable": wtWebioAn1GraphTsEnable,
       "wtWebioAn1GraphTsSyncTime": wtWebioAn1GraphTsSyncTime,
       "wtWebioAn1GraphDeviceClock": wtWebioAn1GraphDeviceClock,
       "wtWebioAn1GraphClockHrs": wtWebioAn1GraphClockHrs,
       "wtWebioAn1GraphClockMin": wtWebioAn1GraphClockMin,
       "wtWebioAn1GraphClockDay": wtWebioAn1GraphClockDay,
       "wtWebioAn1GraphClockMonth": wtWebioAn1GraphClockMonth,
       "wtWebioAn1GraphClockYear": wtWebioAn1GraphClockYear,
       "wtWebioAn1GraphBasic": wtWebioAn1GraphBasic,
       "wtWebioAn1GraphNetwork": wtWebioAn1GraphNetwork,
       "wtWebioAn1GraphIpAddress": wtWebioAn1GraphIpAddress,
       "wtWebioAn1GraphSubnetMask": wtWebioAn1GraphSubnetMask,
       "wtWebioAn1GraphGateway": wtWebioAn1GraphGateway,
       "wtWebioAn1GraphDnsServer1": wtWebioAn1GraphDnsServer1,
       "wtWebioAn1GraphDnsServer2": wtWebioAn1GraphDnsServer2,
       "wtWebioAn1GraphAddConfig": wtWebioAn1GraphAddConfig,
       "wtWebioAn1GraphHTML": wtWebioAn1GraphHTML,
       "wtWebioAn1GraphMail": wtWebioAn1GraphMail,
       "wtWebioAn1GraphMailAdName": wtWebioAn1GraphMailAdName,
       "wtWebioAn1GraphMailReply": wtWebioAn1GraphMailReply,
       "wtWebioAn1GraphMailServer": wtWebioAn1GraphMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebioAn1GraphMailAuthentication": wtWebioAn1GraphMailAuthentication,
       "wtWebioAn1GraphMailAuthUser": wtWebioAn1GraphMailAuthUser,
       "wtWebioAn1GraphMailAuthPassword": wtWebioAn1GraphMailAuthPassword,
       "wtWebioAn1GraphMailPop3Server": wtWebioAn1GraphMailPop3Server,
       "wtWebioAn1GraphSNMP": wtWebioAn1GraphSNMP,
       "wtWebioAn1GraphSnmpCommunityStringRead": wtWebioAn1GraphSnmpCommunityStringRead,
       "wtWebioAn1GraphSnmpCommunityStringReadWrite": wtWebioAn1GraphSnmpCommunityStringReadWrite,
       "wtWebioAn1GraphSystemTrapManagerIP": wtWebioAn1GraphSystemTrapManagerIP,
       "wtWebioAn1GraphSystemTrapEnable": wtWebioAn1GraphSystemTrapEnable,
       "wtWebioAn1GraphSnmpEnable": wtWebioAn1GraphSnmpEnable,
       "wtWebioAn1GraphSnmpCommunityStringTrap": wtWebioAn1GraphSnmpCommunityStringTrap,
       "wtWebioAn1GraphUDP": wtWebioAn1GraphUDP,
       "wtWebioAn1GraphUdpPort": wtWebioAn1GraphUdpPort,
       "wtWebioAn1GraphUdpEnable": wtWebioAn1GraphUdpEnable,
       "wtWebioAn1GraphSyslog": wtWebioAn1GraphSyslog,
       "wtWebioAn1GraphSyslogServerIP": wtWebioAn1GraphSyslogServerIP,
       "wtWebioAn1GraphSyslogServerPort": wtWebioAn1GraphSyslogServerPort,
       "wtWebioAn1GraphSyslogSystemMessagesEnable": wtWebioAn1GraphSyslogSystemMessagesEnable,
       "wtWebioAn1GraphSyslogEnable": wtWebioAn1GraphSyslogEnable,
       "wtWebioAn1GraphFTP": wtWebioAn1GraphFTP,
       "wtWebioAn1GraphFTPServerIP": wtWebioAn1GraphFTPServerIP,
       "wtWebioAn1GraphFTPServerControlPort": wtWebioAn1GraphFTPServerControlPort,
       "wtWebioAn1GraphFTPUserName": wtWebioAn1GraphFTPUserName,
       "wtWebioAn1GraphFTPPassword": wtWebioAn1GraphFTPPassword,
       "wtWebioAn1GraphFTPAccount": wtWebioAn1GraphFTPAccount,
       "wtWebioAn1GraphFTPOption": wtWebioAn1GraphFTPOption,
       "wtWebioAn1GraphFTPEnable": wtWebioAn1GraphFTPEnable,
       "wtWebioAn1GraphHTTP": wtWebioAn1GraphHTTP,
       "wtWebioAn1GraphStartup": wtWebioAn1GraphStartup,
       "wtWebioAn1GraphGetHeaderEnable": wtWebioAn1GraphGetHeaderEnable,
       "wtWebioAn1GraphHttpPort": wtWebioAn1GraphHttpPort,
       "wtWebioAn1GraphDatalogger": wtWebioAn1GraphDatalogger,
       "wtWebioAn1GraphLoggerTimebase": wtWebioAn1GraphLoggerTimebase,
       "wtWebioAn1GraphLoggerSensorSel": wtWebioAn1GraphLoggerSensorSel,
       "wtWebioAn1GraphDisplaySensorSel": wtWebioAn1GraphDisplaySensorSel,
       "wtWebioAn1GraphSensorColorTable": wtWebioAn1GraphSensorColorTable,
       "wtWebioAn1GraphSensorColorEntry": wtWebioAn1GraphSensorColorEntry,
       "wtWebioAn1GraphSensorColor": wtWebioAn1GraphSensorColor,
       "wtWebioAn1GraphAutoScaleEnable": wtWebioAn1GraphAutoScaleEnable,
       "wtWebioAn1GraphVerticalUpperLimit": wtWebioAn1GraphVerticalUpperLimit,
       "wtWebioAn1GraphVerticalLowerLimit": wtWebioAn1GraphVerticalLowerLimit,
       "wtWebioAn1GraphHorizontalZoom": wtWebioAn1GraphHorizontalZoom,
       "wtWebioAn1GraphAlarm": wtWebioAn1GraphAlarm,
       "wtWebioAn1GraphAlarmCount": wtWebioAn1GraphAlarmCount,
       "wtWebioAn1GraphAlarmIfTable": wtWebioAn1GraphAlarmIfTable,
       "wtWebioAn1GraphAlarmIfEntry": wtWebioAn1GraphAlarmIfEntry,
       "wtWebioAn1GraphAlarmNo": wtWebioAn1GraphAlarmNo,
       "wtWebioAn1GraphAlarmTable": wtWebioAn1GraphAlarmTable,
       "wtWebioAn1GraphAlarmEntry": wtWebioAn1GraphAlarmEntry,
       "wtWebioAn1GraphAlarmTrigger": wtWebioAn1GraphAlarmTrigger,
       "wtWebioAn1GraphAlarmMin": wtWebioAn1GraphAlarmMin,
       "wtWebioAn1GraphAlarmMax": wtWebioAn1GraphAlarmMax,
       "wtWebioAn1GraphAlarmHysteresis": wtWebioAn1GraphAlarmHysteresis,
       "wtWebioAn1GraphAlarmDelay": wtWebioAn1GraphAlarmDelay,
       "wtWebioAn1GraphAlarmInterval": wtWebioAn1GraphAlarmInterval,
       "wtWebioAn1GraphAlarmEnable": wtWebioAn1GraphAlarmEnable,
       "wtWebioAn1GraphAlarmEMailAddr": wtWebioAn1GraphAlarmEMailAddr,
       "wtWebioAn1GraphAlarmMailSubject": wtWebioAn1GraphAlarmMailSubject,
       "wtWebioAn1GraphAlarmMailText": wtWebioAn1GraphAlarmMailText,
       "wtWebioAn1GraphAlarmManagerIP": wtWebioAn1GraphAlarmManagerIP,
       "wtWebioAn1GraphAlarmTrapText": wtWebioAn1GraphAlarmTrapText,
       "wtWebioAn1GraphAlarmMailOptions": wtWebioAn1GraphAlarmMailOptions,
       "wtWebioAn1GraphAlarmTcpIpAddr": wtWebioAn1GraphAlarmTcpIpAddr,
       "wtWebioAn1GraphAlarmTcpPort": wtWebioAn1GraphAlarmTcpPort,
       "wtWebioAn1GraphAlarmTcpText": wtWebioAn1GraphAlarmTcpText,
       "wtWebioAn1GraphAlarmClearMailSubject": wtWebioAn1GraphAlarmClearMailSubject,
       "wtWebioAn1GraphAlarmClearMailText": wtWebioAn1GraphAlarmClearMailText,
       "wtWebioAn1GraphAlarmClearTrapText": wtWebioAn1GraphAlarmClearTrapText,
       "wtWebioAn1GraphAlarmClearTcpText": wtWebioAn1GraphAlarmClearTcpText,
       "wtWebioAn1GraphAlarmSyslogIpAddr": wtWebioAn1GraphAlarmSyslogIpAddr,
       "wtWebioAn1GraphAlarmSyslogPort": wtWebioAn1GraphAlarmSyslogPort,
       "wtWebioAn1GraphAlarmSyslogText": wtWebioAn1GraphAlarmSyslogText,
       "wtWebioAn1GraphAlarmSyslogClearText": wtWebioAn1GraphAlarmSyslogClearText,
       "wtWebioAn1GraphAlarmFtpDataPort": wtWebioAn1GraphAlarmFtpDataPort,
       "wtWebioAn1GraphAlarmFtpFileName": wtWebioAn1GraphAlarmFtpFileName,
       "wtWebioAn1GraphAlarmFtpText": wtWebioAn1GraphAlarmFtpText,
       "wtWebioAn1GraphAlarmFtpClearText": wtWebioAn1GraphAlarmFtpClearText,
       "wtWebioAn1GraphAlarmFtpOptions": wtWebioAn1GraphAlarmFtpOptions,
       "wtWebioAn1GraphAlarmTimerCron": wtWebioAn1GraphAlarmTimerCron,
       "wtWebioAn1GraphPorts": wtWebioAn1GraphPorts,
       "wtWebioAn1GraphPortTable": wtWebioAn1GraphPortTable,
       "wtWebioAn1GraphPortEntry": wtWebioAn1GraphPortEntry,
       "wtWebioAn1GraphPortName": wtWebioAn1GraphPortName,
       "wtWebioAn1GraphPortText": wtWebioAn1GraphPortText,
       "wtWebioAn1GraphPortOffset1": wtWebioAn1GraphPortOffset1,
       "wtWebioAn1GraphPortTemperature1": wtWebioAn1GraphPortTemperature1,
       "wtWebioAn1GraphPortOffset2": wtWebioAn1GraphPortOffset2,
       "wtWebioAn1GraphPortTemperature2": wtWebioAn1GraphPortTemperature2,
       "wtWebioAn1GraphPortComment": wtWebioAn1GraphPortComment,
       "wtWebioAn1GraphManufact": wtWebioAn1GraphManufact,
       "wtWebioAn1GraphMfName": wtWebioAn1GraphMfName,
       "wtWebioAn1GraphMfAddr": wtWebioAn1GraphMfAddr,
       "wtWebioAn1GraphMfHotline": wtWebioAn1GraphMfHotline,
       "wtWebioAn1GraphMfInternet": wtWebioAn1GraphMfInternet,
       "wtWebioAn1GraphMfDeviceTyp": wtWebioAn1GraphMfDeviceTyp,
       "wtWebioAn1GraphMfOrderNo": wtWebioAn1GraphMfOrderNo,
       "wtWebioAn1GraphDiag": wtWebioAn1GraphDiag,
       "wtWebioAn1GraphDiagErrorCount": wtWebioAn1GraphDiagErrorCount,
       "wtWebioAn1GraphDiagBinaryError": wtWebioAn1GraphDiagBinaryError,
       "wtWebioAn1GraphDiagErrorIndex": wtWebioAn1GraphDiagErrorIndex,
       "wtWebioAn1GraphDiagErrorMessage": wtWebioAn1GraphDiagErrorMessage,
       "wtWebioAn1GraphDiagErrorClear": wtWebioAn1GraphDiagErrorClear}
)
