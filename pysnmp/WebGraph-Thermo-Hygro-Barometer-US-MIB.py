# SNMP MIB module (WebGraph-Thermo-Hygro-Barometer-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-Thermo-Hygro-Barometer-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:38 2024
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
_WtWebGraphThermoBaro_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaro = _WtWebGraphThermoBaro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37)
)
_WtWebGraphThermoBaroTemp_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroTemp = _WtWebGraphThermoBaroTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1)
)


class _WtWebGraphThermoBaroSensors_Type(Integer32):
    """Custom type wtWebGraphThermoBaroSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermoBaroSensors_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroSensors_Object = MibScalar
wtWebGraphThermoBaroSensors = _WtWebGraphThermoBaroSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 1),
    _WtWebGraphThermoBaroSensors_Type()
)
wtWebGraphThermoBaroSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensors.setStatus("mandatory")
_WtWebGraphThermoBaroSensorTable_Object = MibTable
wtWebGraphThermoBaroSensorTable = _WtWebGraphThermoBaroSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensorTable.setStatus("mandatory")
_WtWebGraphThermoBaroSensorEntry_Object = MibTableRow
wtWebGraphThermoBaroSensorEntry = _WtWebGraphThermoBaroSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 2, 1)
)
wtWebGraphThermoBaroSensorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensorEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroSensorNo_Type(Integer32):
    """Custom type wtWebGraphThermoBaroSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermoBaroSensorNo_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroSensorNo_Object = MibTableColumn
wtWebGraphThermoBaroSensorNo = _WtWebGraphThermoBaroSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 2, 1, 1),
    _WtWebGraphThermoBaroSensorNo_Type()
)
wtWebGraphThermoBaroSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensorNo.setStatus("mandatory")
_WtWebGraphThermoBaroTempValueTable_Object = MibTable
wtWebGraphThermoBaroTempValueTable = _WtWebGraphThermoBaroTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValueTable.setStatus("mandatory")
_WtWebGraphThermoBaroTempValueEntry_Object = MibTableRow
wtWebGraphThermoBaroTempValueEntry = _WtWebGraphThermoBaroTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 3, 1)
)
wtWebGraphThermoBaroTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValueEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroTempValue_Type(OctetString):
    """Custom type wtWebGraphThermoBaroTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphThermoBaroTempValue_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroTempValue_Object = MibTableColumn
wtWebGraphThermoBaroTempValue = _WtWebGraphThermoBaroTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 3, 1, 1),
    _WtWebGraphThermoBaroTempValue_Type()
)
wtWebGraphThermoBaroTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValue.setStatus("mandatory")
_WtWebGraphThermoBaroBinaryTempValueTable_Object = MibTable
wtWebGraphThermoBaroBinaryTempValueTable = _WtWebGraphThermoBaroBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroBinaryTempValueTable.setStatus("mandatory")
_WtWebGraphThermoBaroBinaryTempValueEntry_Object = MibTableRow
wtWebGraphThermoBaroBinaryTempValueEntry = _WtWebGraphThermoBaroBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 4, 1)
)
wtWebGraphThermoBaroBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroBinaryTempValueEntry.setStatus("mandatory")
_WtWebGraphThermoBaroBinaryTempValue_Type = Integer32
_WtWebGraphThermoBaroBinaryTempValue_Object = MibTableColumn
wtWebGraphThermoBaroBinaryTempValue = _WtWebGraphThermoBaroBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 4, 1, 1),
    _WtWebGraphThermoBaroBinaryTempValue_Type()
)
wtWebGraphThermoBaroBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroBinaryTempValue.setStatus("mandatory")
_WtWebGraphThermoBaroTempValuePktTable_Object = MibTable
wtWebGraphThermoBaroTempValuePktTable = _WtWebGraphThermoBaroTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValuePktTable.setStatus("mandatory")
_WtWebGraphThermoBaroTempValuePktEntry_Object = MibTableRow
wtWebGraphThermoBaroTempValuePktEntry = _WtWebGraphThermoBaroTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 8, 1)
)
wtWebGraphThermoBaroTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValuePktEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroTempValuePkt_Type(OctetString):
    """Custom type wtWebGraphThermoBaroTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphThermoBaroTempValuePkt_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroTempValuePkt_Object = MibTableColumn
wtWebGraphThermoBaroTempValuePkt = _WtWebGraphThermoBaroTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 1, 8, 1, 1),
    _WtWebGraphThermoBaroTempValuePkt_Type()
)
wtWebGraphThermoBaroTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTempValuePkt.setStatus("mandatory")
_WtWebGraphThermoBaroSessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroSessCntrl = _WtWebGraphThermoBaroSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2)
)
_WtWebGraphThermoBaroSessCntrlPassword_Type = OctetString
_WtWebGraphThermoBaroSessCntrlPassword_Object = MibScalar
wtWebGraphThermoBaroSessCntrlPassword = _WtWebGraphThermoBaroSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2, 1),
    _WtWebGraphThermoBaroSessCntrlPassword_Type()
)
wtWebGraphThermoBaroSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSessCntrlPassword.setStatus("mandatory")


class _WtWebGraphThermoBaroSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphThermoBaroSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphThermoBaroSessCntrl-NoSession", 0),
          ("wtWebGraphThermoBaroSessCntrl-Session", 1))
    )


_WtWebGraphThermoBaroSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroSessCntrlConfigMode_Object = MibScalar
wtWebGraphThermoBaroSessCntrlConfigMode = _WtWebGraphThermoBaroSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2, 2),
    _WtWebGraphThermoBaroSessCntrlConfigMode_Type()
)
wtWebGraphThermoBaroSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphThermoBaroSessCntrlLogout_Type = Integer32
_WtWebGraphThermoBaroSessCntrlLogout_Object = MibScalar
wtWebGraphThermoBaroSessCntrlLogout = _WtWebGraphThermoBaroSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2, 3),
    _WtWebGraphThermoBaroSessCntrlLogout_Type()
)
wtWebGraphThermoBaroSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSessCntrlLogout.setStatus("mandatory")
_WtWebGraphThermoBaroSessCntrlAdminPassword_Type = OctetString
_WtWebGraphThermoBaroSessCntrlAdminPassword_Object = MibScalar
wtWebGraphThermoBaroSessCntrlAdminPassword = _WtWebGraphThermoBaroSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2, 4),
    _WtWebGraphThermoBaroSessCntrlAdminPassword_Type()
)
wtWebGraphThermoBaroSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphThermoBaroSessCntrlConfigPassword_Type = OctetString
_WtWebGraphThermoBaroSessCntrlConfigPassword_Object = MibScalar
wtWebGraphThermoBaroSessCntrlConfigPassword = _WtWebGraphThermoBaroSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 2, 5),
    _WtWebGraphThermoBaroSessCntrlConfigPassword_Type()
)
wtWebGraphThermoBaroSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphThermoBaroConfig_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroConfig = _WtWebGraphThermoBaroConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3)
)
_WtWebGraphThermoBaroDevice_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroDevice = _WtWebGraphThermoBaroDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1)
)
_WtWebGraphThermoBaroText_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroText = _WtWebGraphThermoBaroText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 1)
)
_WtWebGraphThermoBaroDeviceName_Type = OctetString
_WtWebGraphThermoBaroDeviceName_Object = MibScalar
wtWebGraphThermoBaroDeviceName = _WtWebGraphThermoBaroDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 1, 1),
    _WtWebGraphThermoBaroDeviceName_Type()
)
wtWebGraphThermoBaroDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDeviceName.setStatus("mandatory")
_WtWebGraphThermoBaroDeviceText_Type = OctetString
_WtWebGraphThermoBaroDeviceText_Object = MibScalar
wtWebGraphThermoBaroDeviceText = _WtWebGraphThermoBaroDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 1, 2),
    _WtWebGraphThermoBaroDeviceText_Type()
)
wtWebGraphThermoBaroDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDeviceText.setStatus("mandatory")
_WtWebGraphThermoBaroDeviceLocation_Type = OctetString
_WtWebGraphThermoBaroDeviceLocation_Object = MibScalar
wtWebGraphThermoBaroDeviceLocation = _WtWebGraphThermoBaroDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 1, 3),
    _WtWebGraphThermoBaroDeviceLocation_Type()
)
wtWebGraphThermoBaroDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDeviceLocation.setStatus("mandatory")
_WtWebGraphThermoBaroDeviceContact_Type = OctetString
_WtWebGraphThermoBaroDeviceContact_Object = MibScalar
wtWebGraphThermoBaroDeviceContact = _WtWebGraphThermoBaroDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 1, 4),
    _WtWebGraphThermoBaroDeviceContact_Type()
)
wtWebGraphThermoBaroDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDeviceContact.setStatus("mandatory")
_WtWebGraphThermoBaroTimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroTimeDate = _WtWebGraphThermoBaroTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2)
)
_WtWebGraphThermoBaroTimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroTimeZone = _WtWebGraphThermoBaroTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1)
)
_WtWebGraphThermoBaroTzOffsetHrs_Type = Integer32
_WtWebGraphThermoBaroTzOffsetHrs_Object = MibScalar
wtWebGraphThermoBaroTzOffsetHrs = _WtWebGraphThermoBaroTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 1),
    _WtWebGraphThermoBaroTzOffsetHrs_Type()
)
wtWebGraphThermoBaroTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermoBaroTzOffsetMin_Type = Integer32
_WtWebGraphThermoBaroTzOffsetMin_Object = MibScalar
wtWebGraphThermoBaroTzOffsetMin = _WtWebGraphThermoBaroTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 2),
    _WtWebGraphThermoBaroTzOffsetMin_Type()
)
wtWebGraphThermoBaroTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermoBaroTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroTzEnable_Object = MibScalar
wtWebGraphThermoBaroTzEnable = _WtWebGraphThermoBaroTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 3),
    _WtWebGraphThermoBaroTzEnable_Type()
)
wtWebGraphThermoBaroTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTzEnable.setStatus("mandatory")
_WtWebGraphThermoBaroStTzOffsetHrs_Type = Integer32
_WtWebGraphThermoBaroStTzOffsetHrs_Object = MibScalar
wtWebGraphThermoBaroStTzOffsetHrs = _WtWebGraphThermoBaroStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 4),
    _WtWebGraphThermoBaroStTzOffsetHrs_Type()
)
wtWebGraphThermoBaroStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermoBaroStTzOffsetMin_Type = Integer32
_WtWebGraphThermoBaroStTzOffsetMin_Object = MibScalar
wtWebGraphThermoBaroStTzOffsetMin = _WtWebGraphThermoBaroStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 5),
    _WtWebGraphThermoBaroStTzOffsetMin_Type()
)
wtWebGraphThermoBaroStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroStTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroStTzEnable_Object = MibScalar
wtWebGraphThermoBaroStTzEnable = _WtWebGraphThermoBaroStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 6),
    _WtWebGraphThermoBaroStTzEnable_Type()
)
wtWebGraphThermoBaroStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzEnable.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStartMonth based on Integer32"""
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
        *(("wtWebGraphThermoBaroStartMonth-April", 4),
          ("wtWebGraphThermoBaroStartMonth-August", 8),
          ("wtWebGraphThermoBaroStartMonth-December", 12),
          ("wtWebGraphThermoBaroStartMonth-February", 2),
          ("wtWebGraphThermoBaroStartMonth-January", 1),
          ("wtWebGraphThermoBaroStartMonth-July", 7),
          ("wtWebGraphThermoBaroStartMonth-June", 6),
          ("wtWebGraphThermoBaroStartMonth-March", 3),
          ("wtWebGraphThermoBaroStartMonth-May", 5),
          ("wtWebGraphThermoBaroStartMonth-November", 11),
          ("wtWebGraphThermoBaroStartMonth-October", 10),
          ("wtWebGraphThermoBaroStartMonth-September", 9))
    )


_WtWebGraphThermoBaroStTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStartMonth_Object = MibScalar
wtWebGraphThermoBaroStTzStartMonth = _WtWebGraphThermoBaroStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 7),
    _WtWebGraphThermoBaroStTzStartMonth_Type()
)
wtWebGraphThermoBaroStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStartMonth.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStartMode_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStartMode based on Integer32"""
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
        *(("wtWebGraphThermoBaroStartMode-first", 1),
          ("wtWebGraphThermoBaroStartMode-fourth", 4),
          ("wtWebGraphThermoBaroStartMode-last", 5),
          ("wtWebGraphThermoBaroStartMode-second", 2),
          ("wtWebGraphThermoBaroStartMode-third", 3))
    )


_WtWebGraphThermoBaroStTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStartMode_Object = MibScalar
wtWebGraphThermoBaroStTzStartMode = _WtWebGraphThermoBaroStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 8),
    _WtWebGraphThermoBaroStTzStartMode_Type()
)
wtWebGraphThermoBaroStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStartMode.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStartWday_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStartWday based on Integer32"""
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
        *(("wtWebGraphThermoBaroStartWday-Friday", 6),
          ("wtWebGraphThermoBaroStartWday-Monday", 2),
          ("wtWebGraphThermoBaroStartWday-Saturday", 7),
          ("wtWebGraphThermoBaroStartWday-Sunday", 1),
          ("wtWebGraphThermoBaroStartWday-Thursday", 4),
          ("wtWebGraphThermoBaroStartWday-Tuesday", 3),
          ("wtWebGraphThermoBaroStartWday-Wednesday", 5))
    )


_WtWebGraphThermoBaroStTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStartWday_Object = MibScalar
wtWebGraphThermoBaroStTzStartWday = _WtWebGraphThermoBaroStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 9),
    _WtWebGraphThermoBaroStTzStartWday_Type()
)
wtWebGraphThermoBaroStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStartWday.setStatus("mandatory")
_WtWebGraphThermoBaroStTzStartHrs_Type = Integer32
_WtWebGraphThermoBaroStTzStartHrs_Object = MibScalar
wtWebGraphThermoBaroStTzStartHrs = _WtWebGraphThermoBaroStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 10),
    _WtWebGraphThermoBaroStTzStartHrs_Type()
)
wtWebGraphThermoBaroStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStartHrs.setStatus("mandatory")
_WtWebGraphThermoBaroStTzStartMin_Type = Integer32
_WtWebGraphThermoBaroStTzStartMin_Object = MibScalar
wtWebGraphThermoBaroStTzStartMin = _WtWebGraphThermoBaroStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 11),
    _WtWebGraphThermoBaroStTzStartMin_Type()
)
wtWebGraphThermoBaroStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStartMin.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStopMonth based on Integer32"""
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
        *(("wtWebGraphThermoBaroStopMonth-April", 4),
          ("wtWebGraphThermoBaroStopMonth-August", 8),
          ("wtWebGraphThermoBaroStopMonth-December", 12),
          ("wtWebGraphThermoBaroStopMonth-February", 2),
          ("wtWebGraphThermoBaroStopMonth-January", 1),
          ("wtWebGraphThermoBaroStopMonth-July", 7),
          ("wtWebGraphThermoBaroStopMonth-June", 6),
          ("wtWebGraphThermoBaroStopMonth-March", 3),
          ("wtWebGraphThermoBaroStopMonth-May", 5),
          ("wtWebGraphThermoBaroStopMonth-November", 11),
          ("wtWebGraphThermoBaroStopMonth-October", 10),
          ("wtWebGraphThermoBaroStopMonth-September", 9))
    )


_WtWebGraphThermoBaroStTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStopMonth_Object = MibScalar
wtWebGraphThermoBaroStTzStopMonth = _WtWebGraphThermoBaroStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 12),
    _WtWebGraphThermoBaroStTzStopMonth_Type()
)
wtWebGraphThermoBaroStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStopMonth.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStopMode_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStopMode based on Integer32"""
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
        *(("wtWebGraphThermoBaroStopMode-first", 1),
          ("wtWebGraphThermoBaroStopMode-fourth", 4),
          ("wtWebGraphThermoBaroStopMode-last", 5),
          ("wtWebGraphThermoBaroStopMode-second", 2),
          ("wtWebGraphThermoBaroStopMode-third", 3))
    )


_WtWebGraphThermoBaroStTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStopMode_Object = MibScalar
wtWebGraphThermoBaroStTzStopMode = _WtWebGraphThermoBaroStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 13),
    _WtWebGraphThermoBaroStTzStopMode_Type()
)
wtWebGraphThermoBaroStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStopMode.setStatus("mandatory")


class _WtWebGraphThermoBaroStTzStopWday_Type(Integer32):
    """Custom type wtWebGraphThermoBaroStTzStopWday based on Integer32"""
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
        *(("wtWebGraphThermoBaroStopWday-Friday", 6),
          ("wtWebGraphThermoBaroStopWday-Monday", 2),
          ("wtWebGraphThermoBaroStopWday-Saturday", 7),
          ("wtWebGraphThermoBaroStopWday-Sunday", 1),
          ("wtWebGraphThermoBaroStopWday-Thursday", 4),
          ("wtWebGraphThermoBaroStopWday-Tuesday", 3),
          ("wtWebGraphThermoBaroStopWday-Wednesday", 5))
    )


_WtWebGraphThermoBaroStTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroStTzStopWday_Object = MibScalar
wtWebGraphThermoBaroStTzStopWday = _WtWebGraphThermoBaroStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 14),
    _WtWebGraphThermoBaroStTzStopWday_Type()
)
wtWebGraphThermoBaroStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStopWday.setStatus("mandatory")
_WtWebGraphThermoBaroStTzStopHrs_Type = Integer32
_WtWebGraphThermoBaroStTzStopHrs_Object = MibScalar
wtWebGraphThermoBaroStTzStopHrs = _WtWebGraphThermoBaroStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 15),
    _WtWebGraphThermoBaroStTzStopHrs_Type()
)
wtWebGraphThermoBaroStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStopHrs.setStatus("mandatory")
_WtWebGraphThermoBaroStTzStopMin_Type = Integer32
_WtWebGraphThermoBaroStTzStopMin_Object = MibScalar
wtWebGraphThermoBaroStTzStopMin = _WtWebGraphThermoBaroStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 1, 16),
    _WtWebGraphThermoBaroStTzStopMin_Type()
)
wtWebGraphThermoBaroStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStTzStopMin.setStatus("mandatory")
_WtWebGraphThermoBaroTimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroTimeServer = _WtWebGraphThermoBaroTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 2)
)
_WtWebGraphThermoBaroTimeServer1_Type = OctetString
_WtWebGraphThermoBaroTimeServer1_Object = MibScalar
wtWebGraphThermoBaroTimeServer1 = _WtWebGraphThermoBaroTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 2, 1),
    _WtWebGraphThermoBaroTimeServer1_Type()
)
wtWebGraphThermoBaroTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTimeServer1.setStatus("mandatory")
_WtWebGraphThermoBaroTimeServer2_Type = OctetString
_WtWebGraphThermoBaroTimeServer2_Object = MibScalar
wtWebGraphThermoBaroTimeServer2 = _WtWebGraphThermoBaroTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 2, 2),
    _WtWebGraphThermoBaroTimeServer2_Type()
)
wtWebGraphThermoBaroTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTimeServer2.setStatus("mandatory")


class _WtWebGraphThermoBaroTsEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroTsEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroTsEnable_Object = MibScalar
wtWebGraphThermoBaroTsEnable = _WtWebGraphThermoBaroTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 2, 3),
    _WtWebGraphThermoBaroTsEnable_Type()
)
wtWebGraphThermoBaroTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTsEnable.setStatus("mandatory")
_WtWebGraphThermoBaroTsSyncTime_Type = Integer32
_WtWebGraphThermoBaroTsSyncTime_Object = MibScalar
wtWebGraphThermoBaroTsSyncTime = _WtWebGraphThermoBaroTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 2, 4),
    _WtWebGraphThermoBaroTsSyncTime_Type()
)
wtWebGraphThermoBaroTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroTsSyncTime.setStatus("mandatory")
_WtWebGraphThermoBaroDeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroDeviceClock = _WtWebGraphThermoBaroDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3)
)


class _WtWebGraphThermoBaroClockHrs_Type(Integer32):
    """Custom type wtWebGraphThermoBaroClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphThermoBaroClockHrs_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroClockHrs_Object = MibScalar
wtWebGraphThermoBaroClockHrs = _WtWebGraphThermoBaroClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3, 1),
    _WtWebGraphThermoBaroClockHrs_Type()
)
wtWebGraphThermoBaroClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroClockHrs.setStatus("mandatory")


class _WtWebGraphThermoBaroClockMin_Type(Integer32):
    """Custom type wtWebGraphThermoBaroClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphThermoBaroClockMin_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroClockMin_Object = MibScalar
wtWebGraphThermoBaroClockMin = _WtWebGraphThermoBaroClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3, 2),
    _WtWebGraphThermoBaroClockMin_Type()
)
wtWebGraphThermoBaroClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroClockMin.setStatus("mandatory")


class _WtWebGraphThermoBaroClockDay_Type(Integer32):
    """Custom type wtWebGraphThermoBaroClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphThermoBaroClockDay_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroClockDay_Object = MibScalar
wtWebGraphThermoBaroClockDay = _WtWebGraphThermoBaroClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3, 3),
    _WtWebGraphThermoBaroClockDay_Type()
)
wtWebGraphThermoBaroClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroClockDay.setStatus("mandatory")


class _WtWebGraphThermoBaroClockMonth_Type(Integer32):
    """Custom type wtWebGraphThermoBaroClockMonth based on Integer32"""
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
        *(("wtWebGraphThermoBaroClockMonth-April", 4),
          ("wtWebGraphThermoBaroClockMonth-August", 8),
          ("wtWebGraphThermoBaroClockMonth-December", 12),
          ("wtWebGraphThermoBaroClockMonth-February", 2),
          ("wtWebGraphThermoBaroClockMonth-January", 1),
          ("wtWebGraphThermoBaroClockMonth-July", 7),
          ("wtWebGraphThermoBaroClockMonth-June", 6),
          ("wtWebGraphThermoBaroClockMonth-March", 3),
          ("wtWebGraphThermoBaroClockMonth-May", 5),
          ("wtWebGraphThermoBaroClockMonth-November", 11),
          ("wtWebGraphThermoBaroClockMonth-October", 10),
          ("wtWebGraphThermoBaroClockMonth-September", 9))
    )


_WtWebGraphThermoBaroClockMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroClockMonth_Object = MibScalar
wtWebGraphThermoBaroClockMonth = _WtWebGraphThermoBaroClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3, 4),
    _WtWebGraphThermoBaroClockMonth_Type()
)
wtWebGraphThermoBaroClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroClockMonth.setStatus("mandatory")


class _WtWebGraphThermoBaroClockYear_Type(Integer32):
    """Custom type wtWebGraphThermoBaroClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphThermoBaroClockYear_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroClockYear_Object = MibScalar
wtWebGraphThermoBaroClockYear = _WtWebGraphThermoBaroClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 2, 3, 5),
    _WtWebGraphThermoBaroClockYear_Type()
)
wtWebGraphThermoBaroClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroClockYear.setStatus("mandatory")
_WtWebGraphThermoBaroBasic_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroBasic = _WtWebGraphThermoBaroBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3)
)
_WtWebGraphThermoBaroNetwork_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroNetwork = _WtWebGraphThermoBaroNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1)
)
_WtWebGraphThermoBaroIpAddress_Type = IpAddress
_WtWebGraphThermoBaroIpAddress_Object = MibScalar
wtWebGraphThermoBaroIpAddress = _WtWebGraphThermoBaroIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 1),
    _WtWebGraphThermoBaroIpAddress_Type()
)
wtWebGraphThermoBaroIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroIpAddress.setStatus("mandatory")
_WtWebGraphThermoBaroSubnetMask_Type = IpAddress
_WtWebGraphThermoBaroSubnetMask_Object = MibScalar
wtWebGraphThermoBaroSubnetMask = _WtWebGraphThermoBaroSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 2),
    _WtWebGraphThermoBaroSubnetMask_Type()
)
wtWebGraphThermoBaroSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSubnetMask.setStatus("mandatory")
_WtWebGraphThermoBaroGateway_Type = IpAddress
_WtWebGraphThermoBaroGateway_Object = MibScalar
wtWebGraphThermoBaroGateway = _WtWebGraphThermoBaroGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 3),
    _WtWebGraphThermoBaroGateway_Type()
)
wtWebGraphThermoBaroGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGateway.setStatus("mandatory")
_WtWebGraphThermoBaroDnsServer1_Type = OctetString
_WtWebGraphThermoBaroDnsServer1_Object = MibScalar
wtWebGraphThermoBaroDnsServer1 = _WtWebGraphThermoBaroDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 4),
    _WtWebGraphThermoBaroDnsServer1_Type()
)
wtWebGraphThermoBaroDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDnsServer1.setStatus("mandatory")
_WtWebGraphThermoBaroDnsServer2_Type = OctetString
_WtWebGraphThermoBaroDnsServer2_Object = MibScalar
wtWebGraphThermoBaroDnsServer2 = _WtWebGraphThermoBaroDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 5),
    _WtWebGraphThermoBaroDnsServer2_Type()
)
wtWebGraphThermoBaroDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDnsServer2.setStatus("mandatory")
_WtWebGraphThermoBaroAddConfig_Type = OctetString
_WtWebGraphThermoBaroAddConfig_Object = MibScalar
wtWebGraphThermoBaroAddConfig = _WtWebGraphThermoBaroAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 1, 6),
    _WtWebGraphThermoBaroAddConfig_Type()
)
wtWebGraphThermoBaroAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAddConfig.setStatus("mandatory")
_WtWebGraphThermoBaroHTTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroHTTP = _WtWebGraphThermoBaroHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 2)
)
_WtWebGraphThermoBaroStartup_Type = OctetString
_WtWebGraphThermoBaroStartup_Object = MibScalar
wtWebGraphThermoBaroStartup = _WtWebGraphThermoBaroStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 2, 1),
    _WtWebGraphThermoBaroStartup_Type()
)
wtWebGraphThermoBaroStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroStartup.setStatus("mandatory")
_WtWebGraphThermoBaroGetHeaderEnable_Type = OctetString
_WtWebGraphThermoBaroGetHeaderEnable_Object = MibScalar
wtWebGraphThermoBaroGetHeaderEnable = _WtWebGraphThermoBaroGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 2, 2),
    _WtWebGraphThermoBaroGetHeaderEnable_Type()
)
wtWebGraphThermoBaroGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGetHeaderEnable.setStatus("mandatory")


class _WtWebGraphThermoBaroHttpPort_Type(Integer32):
    """Custom type wtWebGraphThermoBaroHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoBaroHttpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroHttpPort_Object = MibScalar
wtWebGraphThermoBaroHttpPort = _WtWebGraphThermoBaroHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 2, 3),
    _WtWebGraphThermoBaroHttpPort_Type()
)
wtWebGraphThermoBaroHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroHttpPort.setStatus("mandatory")
_WtWebGraphThermoBaroMail_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroMail = _WtWebGraphThermoBaroMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3)
)
_WtWebGraphThermoBaroMailAdName_Type = OctetString
_WtWebGraphThermoBaroMailAdName_Object = MibScalar
wtWebGraphThermoBaroMailAdName = _WtWebGraphThermoBaroMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 1),
    _WtWebGraphThermoBaroMailAdName_Type()
)
wtWebGraphThermoBaroMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailAdName.setStatus("mandatory")
_WtWebGraphThermoBaroMailReply_Type = OctetString
_WtWebGraphThermoBaroMailReply_Object = MibScalar
wtWebGraphThermoBaroMailReply = _WtWebGraphThermoBaroMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 2),
    _WtWebGraphThermoBaroMailReply_Type()
)
wtWebGraphThermoBaroMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailReply.setStatus("mandatory")
_WtWebGraphThermoBaroMailServer_Type = OctetString
_WtWebGraphThermoBaroMailServer_Object = MibScalar
wtWebGraphThermoBaroMailServer = _WtWebGraphThermoBaroMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 3),
    _WtWebGraphThermoBaroMailServer_Type()
)
wtWebGraphThermoBaroMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphThermoBaroMailAuthentication_Type(OctetString):
    """Custom type wtWebGraphThermoBaroMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroMailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroMailAuthentication_Object = MibScalar
wtWebGraphThermoBaroMailAuthentication = _WtWebGraphThermoBaroMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 5),
    _WtWebGraphThermoBaroMailAuthentication_Type()
)
wtWebGraphThermoBaroMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailAuthentication.setStatus("mandatory")
_WtWebGraphThermoBaroMailAuthUser_Type = OctetString
_WtWebGraphThermoBaroMailAuthUser_Object = MibScalar
wtWebGraphThermoBaroMailAuthUser = _WtWebGraphThermoBaroMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 6),
    _WtWebGraphThermoBaroMailAuthUser_Type()
)
wtWebGraphThermoBaroMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailAuthUser.setStatus("mandatory")
_WtWebGraphThermoBaroMailAuthPassword_Type = OctetString
_WtWebGraphThermoBaroMailAuthPassword_Object = MibScalar
wtWebGraphThermoBaroMailAuthPassword = _WtWebGraphThermoBaroMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 7),
    _WtWebGraphThermoBaroMailAuthPassword_Type()
)
wtWebGraphThermoBaroMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailAuthPassword.setStatus("mandatory")
_WtWebGraphThermoBaroMailPop3Server_Type = OctetString
_WtWebGraphThermoBaroMailPop3Server_Object = MibScalar
wtWebGraphThermoBaroMailPop3Server = _WtWebGraphThermoBaroMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 3, 8),
    _WtWebGraphThermoBaroMailPop3Server_Type()
)
wtWebGraphThermoBaroMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMailPop3Server.setStatus("mandatory")
_WtWebGraphThermoBaroSNMP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroSNMP = _WtWebGraphThermoBaroSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4)
)
_WtWebGraphThermoBaroSnmpCommunityStringRead_Type = OctetString
_WtWebGraphThermoBaroSnmpCommunityStringRead_Object = MibScalar
wtWebGraphThermoBaroSnmpCommunityStringRead = _WtWebGraphThermoBaroSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 1),
    _WtWebGraphThermoBaroSnmpCommunityStringRead_Type()
)
wtWebGraphThermoBaroSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphThermoBaroSnmpCommunityStringReadWrite = _WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 2),
    _WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Type()
)
wtWebGraphThermoBaroSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphThermoBaroSystemTrapManagerIP_Type = OctetString
_WtWebGraphThermoBaroSystemTrapManagerIP_Object = MibScalar
wtWebGraphThermoBaroSystemTrapManagerIP = _WtWebGraphThermoBaroSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 3),
    _WtWebGraphThermoBaroSystemTrapManagerIP_Type()
)
wtWebGraphThermoBaroSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphThermoBaroSystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroSystemTrapEnable_Object = MibScalar
wtWebGraphThermoBaroSystemTrapEnable = _WtWebGraphThermoBaroSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 4),
    _WtWebGraphThermoBaroSystemTrapEnable_Type()
)
wtWebGraphThermoBaroSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSystemTrapEnable.setStatus("mandatory")
_WtWebGraphThermoBaroSnmpEnable_Type = OctetString
_WtWebGraphThermoBaroSnmpEnable_Object = MibScalar
wtWebGraphThermoBaroSnmpEnable = _WtWebGraphThermoBaroSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 5),
    _WtWebGraphThermoBaroSnmpEnable_Type()
)
wtWebGraphThermoBaroSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSnmpEnable.setStatus("mandatory")
_WtWebGraphThermoBaroSnmpCommunityStringTrap_Type = OctetString
_WtWebGraphThermoBaroSnmpCommunityStringTrap_Object = MibScalar
wtWebGraphThermoBaroSnmpCommunityStringTrap = _WtWebGraphThermoBaroSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 4, 6),
    _WtWebGraphThermoBaroSnmpCommunityStringTrap_Type()
)
wtWebGraphThermoBaroSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphThermoBaroUDP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroUDP = _WtWebGraphThermoBaroUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 5)
)


class _WtWebGraphThermoBaroUdpPort_Type(Integer32):
    """Custom type wtWebGraphThermoBaroUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoBaroUdpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroUdpPort_Object = MibScalar
wtWebGraphThermoBaroUdpPort = _WtWebGraphThermoBaroUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 5, 1),
    _WtWebGraphThermoBaroUdpPort_Type()
)
wtWebGraphThermoBaroUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroUdpPort.setStatus("mandatory")
_WtWebGraphThermoBaroUdpEnable_Type = OctetString
_WtWebGraphThermoBaroUdpEnable_Object = MibScalar
wtWebGraphThermoBaroUdpEnable = _WtWebGraphThermoBaroUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 5, 2),
    _WtWebGraphThermoBaroUdpEnable_Type()
)
wtWebGraphThermoBaroUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroUdpEnable.setStatus("mandatory")
_WtWebGraphThermoBaroSyslog_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroSyslog = _WtWebGraphThermoBaroSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 6)
)
_WtWebGraphThermoBaroSyslogServerIP_Type = OctetString
_WtWebGraphThermoBaroSyslogServerIP_Object = MibScalar
wtWebGraphThermoBaroSyslogServerIP = _WtWebGraphThermoBaroSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 6, 1),
    _WtWebGraphThermoBaroSyslogServerIP_Type()
)
wtWebGraphThermoBaroSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSyslogServerIP.setStatus("mandatory")
_WtWebGraphThermoBaroSyslogServerPort_Type = Integer32
_WtWebGraphThermoBaroSyslogServerPort_Object = MibScalar
wtWebGraphThermoBaroSyslogServerPort = _WtWebGraphThermoBaroSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 6, 2),
    _WtWebGraphThermoBaroSyslogServerPort_Type()
)
wtWebGraphThermoBaroSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSyslogServerPort.setStatus("mandatory")


class _WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphThermoBaroSyslogSystemMessagesEnable = _WtWebGraphThermoBaroSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 6, 3),
    _WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type()
)
wtWebGraphThermoBaroSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphThermoBaroSyslogEnable_Type = OctetString
_WtWebGraphThermoBaroSyslogEnable_Object = MibScalar
wtWebGraphThermoBaroSyslogEnable = _WtWebGraphThermoBaroSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 6, 4),
    _WtWebGraphThermoBaroSyslogEnable_Type()
)
wtWebGraphThermoBaroSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSyslogEnable.setStatus("mandatory")
_WtWebGraphThermoBaroFTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroFTP = _WtWebGraphThermoBaroFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7)
)
_WtWebGraphThermoBaroFTPServerIP_Type = OctetString
_WtWebGraphThermoBaroFTPServerIP_Object = MibScalar
wtWebGraphThermoBaroFTPServerIP = _WtWebGraphThermoBaroFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 1),
    _WtWebGraphThermoBaroFTPServerIP_Type()
)
wtWebGraphThermoBaroFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPServerIP.setStatus("mandatory")
_WtWebGraphThermoBaroFTPServerControlPort_Type = Integer32
_WtWebGraphThermoBaroFTPServerControlPort_Object = MibScalar
wtWebGraphThermoBaroFTPServerControlPort = _WtWebGraphThermoBaroFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 2),
    _WtWebGraphThermoBaroFTPServerControlPort_Type()
)
wtWebGraphThermoBaroFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPServerControlPort.setStatus("mandatory")
_WtWebGraphThermoBaroFTPUserName_Type = OctetString
_WtWebGraphThermoBaroFTPUserName_Object = MibScalar
wtWebGraphThermoBaroFTPUserName = _WtWebGraphThermoBaroFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 3),
    _WtWebGraphThermoBaroFTPUserName_Type()
)
wtWebGraphThermoBaroFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPUserName.setStatus("mandatory")
_WtWebGraphThermoBaroFTPPassword_Type = OctetString
_WtWebGraphThermoBaroFTPPassword_Object = MibScalar
wtWebGraphThermoBaroFTPPassword = _WtWebGraphThermoBaroFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 4),
    _WtWebGraphThermoBaroFTPPassword_Type()
)
wtWebGraphThermoBaroFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPPassword.setStatus("mandatory")
_WtWebGraphThermoBaroFTPAccount_Type = OctetString
_WtWebGraphThermoBaroFTPAccount_Object = MibScalar
wtWebGraphThermoBaroFTPAccount = _WtWebGraphThermoBaroFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 5),
    _WtWebGraphThermoBaroFTPAccount_Type()
)
wtWebGraphThermoBaroFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPAccount.setStatus("mandatory")
_WtWebGraphThermoBaroFTPOption_Type = OctetString
_WtWebGraphThermoBaroFTPOption_Object = MibScalar
wtWebGraphThermoBaroFTPOption = _WtWebGraphThermoBaroFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 6),
    _WtWebGraphThermoBaroFTPOption_Type()
)
wtWebGraphThermoBaroFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPOption.setStatus("mandatory")
_WtWebGraphThermoBaroFTPEnable_Type = OctetString
_WtWebGraphThermoBaroFTPEnable_Object = MibScalar
wtWebGraphThermoBaroFTPEnable = _WtWebGraphThermoBaroFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 7, 7),
    _WtWebGraphThermoBaroFTPEnable_Type()
)
wtWebGraphThermoBaroFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroFTPEnable.setStatus("mandatory")
_WtWebGraphThermoBaroRSS_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroRSS = _WtWebGraphThermoBaroRSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8)
)
_WtWebGraphThermoBaroRSSChannelTitle_Type = OctetString
_WtWebGraphThermoBaroRSSChannelTitle_Object = MibScalar
wtWebGraphThermoBaroRSSChannelTitle = _WtWebGraphThermoBaroRSSChannelTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 1),
    _WtWebGraphThermoBaroRSSChannelTitle_Type()
)
wtWebGraphThermoBaroRSSChannelTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelTitle.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelLink_Type = OctetString
_WtWebGraphThermoBaroRSSChannelLink_Object = MibScalar
wtWebGraphThermoBaroRSSChannelLink = _WtWebGraphThermoBaroRSSChannelLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 2),
    _WtWebGraphThermoBaroRSSChannelLink_Type()
)
wtWebGraphThermoBaroRSSChannelLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelLink.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelDescription_Type = OctetString
_WtWebGraphThermoBaroRSSChannelDescription_Object = MibScalar
wtWebGraphThermoBaroRSSChannelDescription = _WtWebGraphThermoBaroRSSChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 3),
    _WtWebGraphThermoBaroRSSChannelDescription_Type()
)
wtWebGraphThermoBaroRSSChannelDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelDescription.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelImage_Type = OctetString
_WtWebGraphThermoBaroRSSChannelImage_Object = MibScalar
wtWebGraphThermoBaroRSSChannelImage = _WtWebGraphThermoBaroRSSChannelImage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 4),
    _WtWebGraphThermoBaroRSSChannelImage_Type()
)
wtWebGraphThermoBaroRSSChannelImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelImage.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelImageTitle_Type = OctetString
_WtWebGraphThermoBaroRSSChannelImageTitle_Object = MibScalar
wtWebGraphThermoBaroRSSChannelImageTitle = _WtWebGraphThermoBaroRSSChannelImageTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 5),
    _WtWebGraphThermoBaroRSSChannelImageTitle_Type()
)
wtWebGraphThermoBaroRSSChannelImageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelImageTitle.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelImageLink_Type = OctetString
_WtWebGraphThermoBaroRSSChannelImageLink_Object = MibScalar
wtWebGraphThermoBaroRSSChannelImageLink = _WtWebGraphThermoBaroRSSChannelImageLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 6),
    _WtWebGraphThermoBaroRSSChannelImageLink_Type()
)
wtWebGraphThermoBaroRSSChannelImageLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelImageLink.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelItemTitle_Type = OctetString
_WtWebGraphThermoBaroRSSChannelItemTitle_Object = MibScalar
wtWebGraphThermoBaroRSSChannelItemTitle = _WtWebGraphThermoBaroRSSChannelItemTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 7),
    _WtWebGraphThermoBaroRSSChannelItemTitle_Type()
)
wtWebGraphThermoBaroRSSChannelItemTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelItemTitle.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelItemLink_Type = OctetString
_WtWebGraphThermoBaroRSSChannelItemLink_Object = MibScalar
wtWebGraphThermoBaroRSSChannelItemLink = _WtWebGraphThermoBaroRSSChannelItemLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 8),
    _WtWebGraphThermoBaroRSSChannelItemLink_Type()
)
wtWebGraphThermoBaroRSSChannelItemLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelItemLink.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelItemDescription_Type = OctetString
_WtWebGraphThermoBaroRSSChannelItemDescription_Object = MibScalar
wtWebGraphThermoBaroRSSChannelItemDescription = _WtWebGraphThermoBaroRSSChannelItemDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 9),
    _WtWebGraphThermoBaroRSSChannelItemDescription_Type()
)
wtWebGraphThermoBaroRSSChannelItemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelItemDescription.setStatus("mandatory")
_WtWebGraphThermoBaroRSSChannelItemQuantity_Type = OctetString
_WtWebGraphThermoBaroRSSChannelItemQuantity_Object = MibScalar
wtWebGraphThermoBaroRSSChannelItemQuantity = _WtWebGraphThermoBaroRSSChannelItemQuantity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 8, 10),
    _WtWebGraphThermoBaroRSSChannelItemQuantity_Type()
)
wtWebGraphThermoBaroRSSChannelItemQuantity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroRSSChannelItemQuantity.setStatus("mandatory")
_WtWebGraphThermoBaroLanguage_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroLanguage = _WtWebGraphThermoBaroLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 9)
)
_WtWebGraphThermoBaroLanguageSelect_Type = OctetString
_WtWebGraphThermoBaroLanguageSelect_Object = MibScalar
wtWebGraphThermoBaroLanguageSelect = _WtWebGraphThermoBaroLanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 3, 9, 1),
    _WtWebGraphThermoBaroLanguageSelect_Type()
)
wtWebGraphThermoBaroLanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroLanguageSelect.setStatus("mandatory")
_WtWebGraphThermoBaroDatalogger_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroDatalogger = _WtWebGraphThermoBaroDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 4)
)


class _WtWebGraphThermoBaroLoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphThermoBaroLoggerTimebase based on Integer32"""
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
        *(("wtWebGraphThermoBaroDatalogger-15Min", 3),
          ("wtWebGraphThermoBaroDatalogger-1Min", 1),
          ("wtWebGraphThermoBaroDatalogger-5Min", 2),
          ("wtWebGraphThermoBaroDatalogger-60Min", 4))
    )


_WtWebGraphThermoBaroLoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroLoggerTimebase_Object = MibScalar
wtWebGraphThermoBaroLoggerTimebase = _WtWebGraphThermoBaroLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 4, 1),
    _WtWebGraphThermoBaroLoggerTimebase_Type()
)
wtWebGraphThermoBaroLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroLoggerTimebase.setStatus("mandatory")


class _WtWebGraphThermoBaroLoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphThermoBaroLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroLoggerSensorSel_Object = MibScalar
wtWebGraphThermoBaroLoggerSensorSel = _WtWebGraphThermoBaroLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 4, 2),
    _WtWebGraphThermoBaroLoggerSensorSel_Type()
)
wtWebGraphThermoBaroLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroLoggerSensorSel.setStatus("mandatory")
_WtWebGraphThermoBaroAlarm_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroAlarm = _WtWebGraphThermoBaroAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5)
)


class _WtWebGraphThermoBaroAlarmCount_Type(Integer32):
    """Custom type wtWebGraphThermoBaroAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermoBaroAlarmCount_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroAlarmCount_Object = MibScalar
wtWebGraphThermoBaroAlarmCount = _WtWebGraphThermoBaroAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 1),
    _WtWebGraphThermoBaroAlarmCount_Type()
)
wtWebGraphThermoBaroAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmCount.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmIfTable_Object = MibTable
wtWebGraphThermoBaroAlarmIfTable = _WtWebGraphThermoBaroAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmIfTable.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmIfEntry_Object = MibTableRow
wtWebGraphThermoBaroAlarmIfEntry = _WtWebGraphThermoBaroAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 2, 1)
)
wtWebGraphThermoBaroAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmIfEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmNo_Type(Integer32):
    """Custom type wtWebGraphThermoBaroAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermoBaroAlarmNo_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroAlarmNo_Object = MibTableColumn
wtWebGraphThermoBaroAlarmNo = _WtWebGraphThermoBaroAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 2, 1, 1),
    _WtWebGraphThermoBaroAlarmNo_Type()
)
wtWebGraphThermoBaroAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmNo.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmTable_Object = MibTable
wtWebGraphThermoBaroAlarmTable = _WtWebGraphThermoBaroAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTable.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmEntry_Object = MibTableRow
wtWebGraphThermoBaroAlarmEntry = _WtWebGraphThermoBaroAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1)
)
wtWebGraphThermoBaroAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphThermoBaroAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroAlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroAlarmTrigger_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTrigger = _WtWebGraphThermoBaroAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 1),
    _WtWebGraphThermoBaroAlarmTrigger_Type()
)
wtWebGraphThermoBaroAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTrigger.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmMin_Type = OctetString
_WtWebGraphThermoBaroAlarmMin_Object = MibTableColumn
wtWebGraphThermoBaroAlarmMin = _WtWebGraphThermoBaroAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 2),
    _WtWebGraphThermoBaroAlarmMin_Type()
)
wtWebGraphThermoBaroAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmMin.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmMax_Type = OctetString
_WtWebGraphThermoBaroAlarmMax_Object = MibTableColumn
wtWebGraphThermoBaroAlarmMax = _WtWebGraphThermoBaroAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 3),
    _WtWebGraphThermoBaroAlarmMax_Type()
)
wtWebGraphThermoBaroAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmMax.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmHysteresis_Type = OctetString
_WtWebGraphThermoBaroAlarmHysteresis_Object = MibTableColumn
wtWebGraphThermoBaroAlarmHysteresis = _WtWebGraphThermoBaroAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 4),
    _WtWebGraphThermoBaroAlarmHysteresis_Type()
)
wtWebGraphThermoBaroAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmHysteresis.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmDelay_Type = OctetString
_WtWebGraphThermoBaroAlarmDelay_Object = MibTableColumn
wtWebGraphThermoBaroAlarmDelay = _WtWebGraphThermoBaroAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 5),
    _WtWebGraphThermoBaroAlarmDelay_Type()
)
wtWebGraphThermoBaroAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmDelay.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmInterval_Type = OctetString
_WtWebGraphThermoBaroAlarmInterval_Object = MibTableColumn
wtWebGraphThermoBaroAlarmInterval = _WtWebGraphThermoBaroAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 6),
    _WtWebGraphThermoBaroAlarmInterval_Type()
)
wtWebGraphThermoBaroAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmInterval.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmEnable_Type(OctetString):
    """Custom type wtWebGraphThermoBaroAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroAlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroAlarmEnable_Object = MibTableColumn
wtWebGraphThermoBaroAlarmEnable = _WtWebGraphThermoBaroAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 7),
    _WtWebGraphThermoBaroAlarmEnable_Type()
)
wtWebGraphThermoBaroAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmEnable.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmEMailAddr_Type = OctetString
_WtWebGraphThermoBaroAlarmEMailAddr_Object = MibTableColumn
wtWebGraphThermoBaroAlarmEMailAddr = _WtWebGraphThermoBaroAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 8),
    _WtWebGraphThermoBaroAlarmEMailAddr_Type()
)
wtWebGraphThermoBaroAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmEMailAddr.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmMailSubject_Type = OctetString
_WtWebGraphThermoBaroAlarmMailSubject_Object = MibTableColumn
wtWebGraphThermoBaroAlarmMailSubject = _WtWebGraphThermoBaroAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 9),
    _WtWebGraphThermoBaroAlarmMailSubject_Type()
)
wtWebGraphThermoBaroAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmMailSubject.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmMailText_Type = OctetString
_WtWebGraphThermoBaroAlarmMailText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmMailText = _WtWebGraphThermoBaroAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 10),
    _WtWebGraphThermoBaroAlarmMailText_Type()
)
wtWebGraphThermoBaroAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmMailText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmManagerIP_Type = OctetString
_WtWebGraphThermoBaroAlarmManagerIP_Object = MibTableColumn
wtWebGraphThermoBaroAlarmManagerIP = _WtWebGraphThermoBaroAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 11),
    _WtWebGraphThermoBaroAlarmManagerIP_Type()
)
wtWebGraphThermoBaroAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmManagerIP.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmTrapText_Type = OctetString
_WtWebGraphThermoBaroAlarmTrapText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTrapText = _WtWebGraphThermoBaroAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 12),
    _WtWebGraphThermoBaroAlarmTrapText_Type()
)
wtWebGraphThermoBaroAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTrapText.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphThermoBaroAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroAlarmMailOptions_Object = MibTableColumn
wtWebGraphThermoBaroAlarmMailOptions = _WtWebGraphThermoBaroAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 13),
    _WtWebGraphThermoBaroAlarmMailOptions_Type()
)
wtWebGraphThermoBaroAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmMailOptions.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmTcpIpAddr_Type = OctetString
_WtWebGraphThermoBaroAlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTcpIpAddr = _WtWebGraphThermoBaroAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 14),
    _WtWebGraphThermoBaroAlarmTcpIpAddr_Type()
)
wtWebGraphThermoBaroAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphThermoBaroAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoBaroAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroAlarmTcpPort_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTcpPort = _WtWebGraphThermoBaroAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 15),
    _WtWebGraphThermoBaroAlarmTcpPort_Type()
)
wtWebGraphThermoBaroAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTcpPort.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmTcpText_Type = OctetString
_WtWebGraphThermoBaroAlarmTcpText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTcpText = _WtWebGraphThermoBaroAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 16),
    _WtWebGraphThermoBaroAlarmTcpText_Type()
)
wtWebGraphThermoBaroAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTcpText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmClearMailSubject_Type = OctetString
_WtWebGraphThermoBaroAlarmClearMailSubject_Object = MibTableColumn
wtWebGraphThermoBaroAlarmClearMailSubject = _WtWebGraphThermoBaroAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 17),
    _WtWebGraphThermoBaroAlarmClearMailSubject_Type()
)
wtWebGraphThermoBaroAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmClearMailText_Type = OctetString
_WtWebGraphThermoBaroAlarmClearMailText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmClearMailText = _WtWebGraphThermoBaroAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 18),
    _WtWebGraphThermoBaroAlarmClearMailText_Type()
)
wtWebGraphThermoBaroAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmClearMailText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmClearTrapText_Type = OctetString
_WtWebGraphThermoBaroAlarmClearTrapText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmClearTrapText = _WtWebGraphThermoBaroAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 19),
    _WtWebGraphThermoBaroAlarmClearTrapText_Type()
)
wtWebGraphThermoBaroAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmClearTrapText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmClearTcpText_Type = OctetString
_WtWebGraphThermoBaroAlarmClearTcpText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmClearTcpText = _WtWebGraphThermoBaroAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 20),
    _WtWebGraphThermoBaroAlarmClearTcpText_Type()
)
wtWebGraphThermoBaroAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmClearTcpText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmDeltaTemp_Type = OctetString
_WtWebGraphThermoBaroAlarmDeltaTemp_Object = MibTableColumn
wtWebGraphThermoBaroAlarmDeltaTemp = _WtWebGraphThermoBaroAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 21),
    _WtWebGraphThermoBaroAlarmDeltaTemp_Type()
)
wtWebGraphThermoBaroAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmDeltaTemp.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmRHMin_Type = OctetString
_WtWebGraphThermoBaroAlarmRHMin_Object = MibTableColumn
wtWebGraphThermoBaroAlarmRHMin = _WtWebGraphThermoBaroAlarmRHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 22),
    _WtWebGraphThermoBaroAlarmRHMin_Type()
)
wtWebGraphThermoBaroAlarmRHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmRHMin.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmRHMax_Type = OctetString
_WtWebGraphThermoBaroAlarmRHMax_Object = MibTableColumn
wtWebGraphThermoBaroAlarmRHMax = _WtWebGraphThermoBaroAlarmRHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 23),
    _WtWebGraphThermoBaroAlarmRHMax_Type()
)
wtWebGraphThermoBaroAlarmRHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmRHMax.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmRHHysteresis_Type = OctetString
_WtWebGraphThermoBaroAlarmRHHysteresis_Object = MibTableColumn
wtWebGraphThermoBaroAlarmRHHysteresis = _WtWebGraphThermoBaroAlarmRHHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 24),
    _WtWebGraphThermoBaroAlarmRHHysteresis_Type()
)
wtWebGraphThermoBaroAlarmRHHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmRHHysteresis.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmAHMin_Type = OctetString
_WtWebGraphThermoBaroAlarmAHMin_Object = MibTableColumn
wtWebGraphThermoBaroAlarmAHMin = _WtWebGraphThermoBaroAlarmAHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 25),
    _WtWebGraphThermoBaroAlarmAHMin_Type()
)
wtWebGraphThermoBaroAlarmAHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmAHMin.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmAHMax_Type = OctetString
_WtWebGraphThermoBaroAlarmAHMax_Object = MibTableColumn
wtWebGraphThermoBaroAlarmAHMax = _WtWebGraphThermoBaroAlarmAHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 26),
    _WtWebGraphThermoBaroAlarmAHMax_Type()
)
wtWebGraphThermoBaroAlarmAHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmAHMax.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmSyslogIpAddr_Type = IpAddress
_WtWebGraphThermoBaroAlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphThermoBaroAlarmSyslogIpAddr = _WtWebGraphThermoBaroAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 27),
    _WtWebGraphThermoBaroAlarmSyslogIpAddr_Type()
)
wtWebGraphThermoBaroAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphThermoBaroAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoBaroAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphThermoBaroAlarmSyslogPort_Object = MibTableColumn
wtWebGraphThermoBaroAlarmSyslogPort = _WtWebGraphThermoBaroAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 28),
    _WtWebGraphThermoBaroAlarmSyslogPort_Type()
)
wtWebGraphThermoBaroAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmSyslogPort.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmSyslogText_Type = OctetString
_WtWebGraphThermoBaroAlarmSyslogText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmSyslogText = _WtWebGraphThermoBaroAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 29),
    _WtWebGraphThermoBaroAlarmSyslogText_Type()
)
wtWebGraphThermoBaroAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmSyslogText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmSyslogClearText_Type = OctetString
_WtWebGraphThermoBaroAlarmSyslogClearText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmSyslogClearText = _WtWebGraphThermoBaroAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 30),
    _WtWebGraphThermoBaroAlarmSyslogClearText_Type()
)
wtWebGraphThermoBaroAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmFtpDataPort_Type = OctetString
_WtWebGraphThermoBaroAlarmFtpDataPort_Object = MibTableColumn
wtWebGraphThermoBaroAlarmFtpDataPort = _WtWebGraphThermoBaroAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 31),
    _WtWebGraphThermoBaroAlarmFtpDataPort_Type()
)
wtWebGraphThermoBaroAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmFtpFileName_Type = OctetString
_WtWebGraphThermoBaroAlarmFtpFileName_Object = MibTableColumn
wtWebGraphThermoBaroAlarmFtpFileName = _WtWebGraphThermoBaroAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 32),
    _WtWebGraphThermoBaroAlarmFtpFileName_Type()
)
wtWebGraphThermoBaroAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmFtpFileName.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmFtpText_Type = OctetString
_WtWebGraphThermoBaroAlarmFtpText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmFtpText = _WtWebGraphThermoBaroAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 33),
    _WtWebGraphThermoBaroAlarmFtpText_Type()
)
wtWebGraphThermoBaroAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmFtpText.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmFtpClearText_Type = OctetString
_WtWebGraphThermoBaroAlarmFtpClearText_Object = MibTableColumn
wtWebGraphThermoBaroAlarmFtpClearText = _WtWebGraphThermoBaroAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 34),
    _WtWebGraphThermoBaroAlarmFtpClearText_Type()
)
wtWebGraphThermoBaroAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphThermoBaroAlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphThermoBaroAlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroAlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroAlarmFtpOption_Object = MibTableColumn
wtWebGraphThermoBaroAlarmFtpOption = _WtWebGraphThermoBaroAlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 35),
    _WtWebGraphThermoBaroAlarmFtpOption_Type()
)
wtWebGraphThermoBaroAlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmFtpOption.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmTimerCron_Type = OctetString
_WtWebGraphThermoBaroAlarmTimerCron_Object = MibTableColumn
wtWebGraphThermoBaroAlarmTimerCron = _WtWebGraphThermoBaroAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 36),
    _WtWebGraphThermoBaroAlarmTimerCron_Type()
)
wtWebGraphThermoBaroAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmTimerCron.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmName_Type = OctetString
_WtWebGraphThermoBaroAlarmName_Object = MibTableColumn
wtWebGraphThermoBaroAlarmName = _WtWebGraphThermoBaroAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 39),
    _WtWebGraphThermoBaroAlarmName_Type()
)
wtWebGraphThermoBaroAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmName.setStatus("mandatory")
_WtWebGraphThermoBaroAlarmActive_Type = OctetString
_WtWebGraphThermoBaroAlarmActive_Object = MibTableColumn
wtWebGraphThermoBaroAlarmActive = _WtWebGraphThermoBaroAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 5, 3, 1, 40),
    _WtWebGraphThermoBaroAlarmActive_Type()
)
wtWebGraphThermoBaroAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlarmActive.setStatus("mandatory")
_WtWebGraphThermoBaroGraphics_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroGraphics = _WtWebGraphThermoBaroGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6)
)
_WtWebGraphThermoBaroGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroGraphicsBase = _WtWebGraphThermoBaroGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1)
)
_WtWebGraphThermoBaroGraphicsBaseEnable_Type = OctetString
_WtWebGraphThermoBaroGraphicsBaseEnable_Object = MibScalar
wtWebGraphThermoBaroGraphicsBaseEnable = _WtWebGraphThermoBaroGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 1),
    _WtWebGraphThermoBaroGraphicsBaseEnable_Type()
)
wtWebGraphThermoBaroGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsBaseWidth_Type = Integer32
_WtWebGraphThermoBaroGraphicsBaseWidth_Object = MibScalar
wtWebGraphThermoBaroGraphicsBaseWidth = _WtWebGraphThermoBaroGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 2),
    _WtWebGraphThermoBaroGraphicsBaseWidth_Type()
)
wtWebGraphThermoBaroGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsBaseHeight_Type = Integer32
_WtWebGraphThermoBaroGraphicsBaseHeight_Object = MibScalar
wtWebGraphThermoBaroGraphicsBaseHeight = _WtWebGraphThermoBaroGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 3),
    _WtWebGraphThermoBaroGraphicsBaseHeight_Type()
)
wtWebGraphThermoBaroGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphThermoBaroGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphThermoBaroGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphThermoBaroGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroGraphicsBaseFrameColor_Object = MibScalar
wtWebGraphThermoBaroGraphicsBaseFrameColor = _WtWebGraphThermoBaroGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 4),
    _WtWebGraphThermoBaroGraphicsBaseFrameColor_Type()
)
wtWebGraphThermoBaroGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphThermoBaroGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphThermoBaroGraphicsBaseBackgroundColor = _WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 5),
    _WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type()
)
wtWebGraphThermoBaroGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsBasePollingrate_Type = Integer32
_WtWebGraphThermoBaroGraphicsBasePollingrate_Object = MibScalar
wtWebGraphThermoBaroGraphicsBasePollingrate = _WtWebGraphThermoBaroGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 1, 6),
    _WtWebGraphThermoBaroGraphicsBasePollingrate_Type()
)
wtWebGraphThermoBaroGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroGraphicsSelect = _WtWebGraphThermoBaroGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2)
)


class _WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel = _WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 1),
    _WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem = _WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 2),
    _WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphThermoBaroSensorColorTable_Object = MibTable
wtWebGraphThermoBaroSensorColorTable = _WtWebGraphThermoBaroSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensorColorTable.setStatus("mandatory")
_WtWebGraphThermoBaroSensorColorEntry_Object = MibTableRow
wtWebGraphThermoBaroSensorColorEntry = _WtWebGraphThermoBaroSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 3, 1)
)
wtWebGraphThermoBaroSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroSensorColorEntry.setStatus("mandatory")


class _WtWebGraphThermoBaroGraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphThermoBaroGraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphThermoBaroGraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphThermoBaroGraphicsSensorColor_Object = MibTableColumn
wtWebGraphThermoBaroGraphicsSensorColor = _WtWebGraphThermoBaroGraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphThermoBaroGraphicsSensorColor_Type()
)
wtWebGraphThermoBaroGraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsSensorColor.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsSelectScale_Type = OctetString
_WtWebGraphThermoBaroGraphicsSelectScale_Object = MibTableColumn
wtWebGraphThermoBaroGraphicsSelectScale = _WtWebGraphThermoBaroGraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphThermoBaroGraphicsSelectScale_Type()
)
wtWebGraphThermoBaroGraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsSelectScale.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroGraphicsScale = _WtWebGraphThermoBaroGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3)
)
_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable = _WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 1),
    _WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphThermoBaroGraphicsScaleAutoFitEnable = _WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 2),
    _WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Type()
)
wtWebGraphThermoBaroGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale1Min_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale1Min_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale1Min = _WtWebGraphThermoBaroGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 3),
    _WtWebGraphThermoBaroGraphicsScale1Min_Type()
)
wtWebGraphThermoBaroGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale1Min.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale2Min_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale2Min_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale2Min = _WtWebGraphThermoBaroGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 4),
    _WtWebGraphThermoBaroGraphicsScale2Min_Type()
)
wtWebGraphThermoBaroGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale2Min.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale3Min_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale3Min_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale3Min = _WtWebGraphThermoBaroGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 5),
    _WtWebGraphThermoBaroGraphicsScale3Min_Type()
)
wtWebGraphThermoBaroGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale3Min.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale4Min_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale4Min_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale4Min = _WtWebGraphThermoBaroGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 6),
    _WtWebGraphThermoBaroGraphicsScale4Min_Type()
)
wtWebGraphThermoBaroGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale4Min.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale1Max_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale1Max_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale1Max = _WtWebGraphThermoBaroGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 7),
    _WtWebGraphThermoBaroGraphicsScale1Max_Type()
)
wtWebGraphThermoBaroGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale1Max.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale2Max_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale2Max_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale2Max = _WtWebGraphThermoBaroGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 8),
    _WtWebGraphThermoBaroGraphicsScale2Max_Type()
)
wtWebGraphThermoBaroGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale2Max.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale3Max_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale3Max_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale3Max = _WtWebGraphThermoBaroGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 9),
    _WtWebGraphThermoBaroGraphicsScale3Max_Type()
)
wtWebGraphThermoBaroGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale3Max.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale4Max_Type = Integer32
_WtWebGraphThermoBaroGraphicsScale4Max_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale4Max = _WtWebGraphThermoBaroGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 10),
    _WtWebGraphThermoBaroGraphicsScale4Max_Type()
)
wtWebGraphThermoBaroGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale4Max.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale1Unit_Type = OctetString
_WtWebGraphThermoBaroGraphicsScale1Unit_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale1Unit = _WtWebGraphThermoBaroGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 11),
    _WtWebGraphThermoBaroGraphicsScale1Unit_Type()
)
wtWebGraphThermoBaroGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale2Unit_Type = OctetString
_WtWebGraphThermoBaroGraphicsScale2Unit_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale2Unit = _WtWebGraphThermoBaroGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 12),
    _WtWebGraphThermoBaroGraphicsScale2Unit_Type()
)
wtWebGraphThermoBaroGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale3Unit_Type = OctetString
_WtWebGraphThermoBaroGraphicsScale3Unit_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale3Unit = _WtWebGraphThermoBaroGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 13),
    _WtWebGraphThermoBaroGraphicsScale3Unit_Type()
)
wtWebGraphThermoBaroGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphThermoBaroGraphicsScale4Unit_Type = OctetString
_WtWebGraphThermoBaroGraphicsScale4Unit_Object = MibScalar
wtWebGraphThermoBaroGraphicsScale4Unit = _WtWebGraphThermoBaroGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 1, 6, 3, 14),
    _WtWebGraphThermoBaroGraphicsScale4Unit_Type()
)
wtWebGraphThermoBaroGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroGraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphThermoBaroPorts_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroPorts = _WtWebGraphThermoBaroPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2)
)
_WtWebGraphThermoBaroPortTable_Object = MibTable
wtWebGraphThermoBaroPortTable = _WtWebGraphThermoBaroPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortTable.setStatus("mandatory")
_WtWebGraphThermoBaroPortEntry_Object = MibTableRow
wtWebGraphThermoBaroPortEntry = _WtWebGraphThermoBaroPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1)
)
wtWebGraphThermoBaroPortEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortEntry.setStatus("mandatory")
_WtWebGraphThermoBaroPortName_Type = OctetString
_WtWebGraphThermoBaroPortName_Object = MibTableColumn
wtWebGraphThermoBaroPortName = _WtWebGraphThermoBaroPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 1),
    _WtWebGraphThermoBaroPortName_Type()
)
wtWebGraphThermoBaroPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortName.setStatus("mandatory")
_WtWebGraphThermoBaroPortText_Type = OctetString
_WtWebGraphThermoBaroPortText_Object = MibTableColumn
wtWebGraphThermoBaroPortText = _WtWebGraphThermoBaroPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 2),
    _WtWebGraphThermoBaroPortText_Type()
)
wtWebGraphThermoBaroPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortText.setStatus("mandatory")
_WtWebGraphThermoBaroPortOffset1_Type = OctetString
_WtWebGraphThermoBaroPortOffset1_Object = MibTableColumn
wtWebGraphThermoBaroPortOffset1 = _WtWebGraphThermoBaroPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 3),
    _WtWebGraphThermoBaroPortOffset1_Type()
)
wtWebGraphThermoBaroPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortOffset1.setStatus("mandatory")
_WtWebGraphThermoBaroPortTemperature1_Type = OctetString
_WtWebGraphThermoBaroPortTemperature1_Object = MibTableColumn
wtWebGraphThermoBaroPortTemperature1 = _WtWebGraphThermoBaroPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 4),
    _WtWebGraphThermoBaroPortTemperature1_Type()
)
wtWebGraphThermoBaroPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortTemperature1.setStatus("mandatory")
_WtWebGraphThermoBaroPortOffset2_Type = OctetString
_WtWebGraphThermoBaroPortOffset2_Object = MibTableColumn
wtWebGraphThermoBaroPortOffset2 = _WtWebGraphThermoBaroPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 5),
    _WtWebGraphThermoBaroPortOffset2_Type()
)
wtWebGraphThermoBaroPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortOffset2.setStatus("mandatory")
_WtWebGraphThermoBaroPortTemperature2_Type = OctetString
_WtWebGraphThermoBaroPortTemperature2_Object = MibTableColumn
wtWebGraphThermoBaroPortTemperature2 = _WtWebGraphThermoBaroPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 6),
    _WtWebGraphThermoBaroPortTemperature2_Type()
)
wtWebGraphThermoBaroPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortTemperature2.setStatus("mandatory")
_WtWebGraphThermoBaroPortComment_Type = OctetString
_WtWebGraphThermoBaroPortComment_Object = MibTableColumn
wtWebGraphThermoBaroPortComment = _WtWebGraphThermoBaroPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 1, 1, 7),
    _WtWebGraphThermoBaroPortComment_Type()
)
wtWebGraphThermoBaroPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortComment.setStatus("mandatory")
_WtWebGraphThermoBaroPortAltidude_Type = OctetString
_WtWebGraphThermoBaroPortAltidude_Object = MibScalar
wtWebGraphThermoBaroPortAltidude = _WtWebGraphThermoBaroPortAltidude_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 2, 2),
    _WtWebGraphThermoBaroPortAltidude_Type()
)
wtWebGraphThermoBaroPortAltidude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroPortAltidude.setStatus("mandatory")
_WtWebGraphThermoBaroManufact_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroManufact = _WtWebGraphThermoBaroManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3)
)
_WtWebGraphThermoBaroMfName_Type = OctetString
_WtWebGraphThermoBaroMfName_Object = MibScalar
wtWebGraphThermoBaroMfName = _WtWebGraphThermoBaroMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 1),
    _WtWebGraphThermoBaroMfName_Type()
)
wtWebGraphThermoBaroMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfName.setStatus("mandatory")
_WtWebGraphThermoBaroMfAddr_Type = OctetString
_WtWebGraphThermoBaroMfAddr_Object = MibScalar
wtWebGraphThermoBaroMfAddr = _WtWebGraphThermoBaroMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 2),
    _WtWebGraphThermoBaroMfAddr_Type()
)
wtWebGraphThermoBaroMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfAddr.setStatus("mandatory")
_WtWebGraphThermoBaroMfHotline_Type = OctetString
_WtWebGraphThermoBaroMfHotline_Object = MibScalar
wtWebGraphThermoBaroMfHotline = _WtWebGraphThermoBaroMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 3),
    _WtWebGraphThermoBaroMfHotline_Type()
)
wtWebGraphThermoBaroMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfHotline.setStatus("mandatory")
_WtWebGraphThermoBaroMfInternet_Type = OctetString
_WtWebGraphThermoBaroMfInternet_Object = MibScalar
wtWebGraphThermoBaroMfInternet = _WtWebGraphThermoBaroMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 4),
    _WtWebGraphThermoBaroMfInternet_Type()
)
wtWebGraphThermoBaroMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfInternet.setStatus("mandatory")
_WtWebGraphThermoBaroMfDeviceTyp_Type = OctetString
_WtWebGraphThermoBaroMfDeviceTyp_Object = MibScalar
wtWebGraphThermoBaroMfDeviceTyp = _WtWebGraphThermoBaroMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 5),
    _WtWebGraphThermoBaroMfDeviceTyp_Type()
)
wtWebGraphThermoBaroMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfDeviceTyp.setStatus("mandatory")
_WtWebGraphThermoBaroMfOrderNo_Type = OctetString
_WtWebGraphThermoBaroMfOrderNo_Object = MibScalar
wtWebGraphThermoBaroMfOrderNo = _WtWebGraphThermoBaroMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 3, 3, 6),
    _WtWebGraphThermoBaroMfOrderNo_Type()
)
wtWebGraphThermoBaroMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroMfOrderNo.setStatus("mandatory")
_WtWebGraphThermoBaroDiag_ObjectIdentity = ObjectIdentity
wtWebGraphThermoBaroDiag = _WtWebGraphThermoBaroDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4)
)
_WtWebGraphThermoBaroDiagErrorCount_Type = Integer32
_WtWebGraphThermoBaroDiagErrorCount_Object = MibScalar
wtWebGraphThermoBaroDiagErrorCount = _WtWebGraphThermoBaroDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4, 1),
    _WtWebGraphThermoBaroDiagErrorCount_Type()
)
wtWebGraphThermoBaroDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDiagErrorCount.setStatus("mandatory")
_WtWebGraphThermoBaroDiagBinaryError_Type = OctetString
_WtWebGraphThermoBaroDiagBinaryError_Object = MibScalar
wtWebGraphThermoBaroDiagBinaryError = _WtWebGraphThermoBaroDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4, 2),
    _WtWebGraphThermoBaroDiagBinaryError_Type()
)
wtWebGraphThermoBaroDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDiagBinaryError.setStatus("mandatory")
_WtWebGraphThermoBaroDiagErrorIndex_Type = Integer32
_WtWebGraphThermoBaroDiagErrorIndex_Object = MibScalar
wtWebGraphThermoBaroDiagErrorIndex = _WtWebGraphThermoBaroDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4, 3),
    _WtWebGraphThermoBaroDiagErrorIndex_Type()
)
wtWebGraphThermoBaroDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDiagErrorIndex.setStatus("mandatory")
_WtWebGraphThermoBaroDiagErrorMessage_Type = OctetString
_WtWebGraphThermoBaroDiagErrorMessage_Object = MibScalar
wtWebGraphThermoBaroDiagErrorMessage = _WtWebGraphThermoBaroDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4, 4),
    _WtWebGraphThermoBaroDiagErrorMessage_Type()
)
wtWebGraphThermoBaroDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDiagErrorMessage.setStatus("mandatory")
_WtWebGraphThermoBaroDiagErrorClear_Type = Integer32
_WtWebGraphThermoBaroDiagErrorClear_Object = MibScalar
wtWebGraphThermoBaroDiagErrorClear = _WtWebGraphThermoBaroDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 4, 5),
    _WtWebGraphThermoBaroDiagErrorClear_Type()
)
wtWebGraphThermoBaroDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphThermoBaroAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 31)
)
wtWebGraphThermoBaroAlert1.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert1.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 32)
)
wtWebGraphThermoBaroAlert2.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert2.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 33)
)
wtWebGraphThermoBaroAlert3.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert3.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 34)
)
wtWebGraphThermoBaroAlert4.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert4.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 35)
)
wtWebGraphThermoBaroAlert5.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert5.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 36)
)
wtWebGraphThermoBaroAlert6.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert6.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 37)
)
wtWebGraphThermoBaroAlert7.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert7.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 38)
)
wtWebGraphThermoBaroAlert8.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert8.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 91)
)
wtWebGraphThermoBaroAlert9.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert9.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 92)
)
wtWebGraphThermoBaroAlert10.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert10.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 93)
)
wtWebGraphThermoBaroAlert11.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert11.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 94)
)
wtWebGraphThermoBaroAlert12.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert12.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 95)
)
wtWebGraphThermoBaroAlert13.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert13.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 96)
)
wtWebGraphThermoBaroAlert14.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert14.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 97)
)
wtWebGraphThermoBaroAlert15.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert15.setStatus(
        ""
    )

wtWebGraphThermoBaroAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 98)
)
wtWebGraphThermoBaroAlert16.setObjects(
    ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlert16.setStatus(
        ""
    )

wtWebGraphThermoBaroAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 37, 0, 110)
)
wtWebGraphThermoBaroAlertDiag.setObjects(
      *(("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroDiagErrorIndex"),
        ("WebGraph-Thermo-Hygro-Barometer-US-MIB", "wtWebGraphThermoBaroDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphThermoBaroAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermo-Hygro-Barometer-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphThermoBaro": wtWebGraphThermoBaro,
       "wtWebGraphThermoBaroAlert1": wtWebGraphThermoBaroAlert1,
       "wtWebGraphThermoBaroAlert2": wtWebGraphThermoBaroAlert2,
       "wtWebGraphThermoBaroAlert3": wtWebGraphThermoBaroAlert3,
       "wtWebGraphThermoBaroAlert4": wtWebGraphThermoBaroAlert4,
       "wtWebGraphThermoBaroAlert5": wtWebGraphThermoBaroAlert5,
       "wtWebGraphThermoBaroAlert6": wtWebGraphThermoBaroAlert6,
       "wtWebGraphThermoBaroAlert7": wtWebGraphThermoBaroAlert7,
       "wtWebGraphThermoBaroAlert8": wtWebGraphThermoBaroAlert8,
       "wtWebGraphThermoBaroAlert9": wtWebGraphThermoBaroAlert9,
       "wtWebGraphThermoBaroAlert10": wtWebGraphThermoBaroAlert10,
       "wtWebGraphThermoBaroAlert11": wtWebGraphThermoBaroAlert11,
       "wtWebGraphThermoBaroAlert12": wtWebGraphThermoBaroAlert12,
       "wtWebGraphThermoBaroAlert13": wtWebGraphThermoBaroAlert13,
       "wtWebGraphThermoBaroAlert14": wtWebGraphThermoBaroAlert14,
       "wtWebGraphThermoBaroAlert15": wtWebGraphThermoBaroAlert15,
       "wtWebGraphThermoBaroAlert16": wtWebGraphThermoBaroAlert16,
       "wtWebGraphThermoBaroAlertDiag": wtWebGraphThermoBaroAlertDiag,
       "wtWebGraphThermoBaroTemp": wtWebGraphThermoBaroTemp,
       "wtWebGraphThermoBaroSensors": wtWebGraphThermoBaroSensors,
       "wtWebGraphThermoBaroSensorTable": wtWebGraphThermoBaroSensorTable,
       "wtWebGraphThermoBaroSensorEntry": wtWebGraphThermoBaroSensorEntry,
       "wtWebGraphThermoBaroSensorNo": wtWebGraphThermoBaroSensorNo,
       "wtWebGraphThermoBaroTempValueTable": wtWebGraphThermoBaroTempValueTable,
       "wtWebGraphThermoBaroTempValueEntry": wtWebGraphThermoBaroTempValueEntry,
       "wtWebGraphThermoBaroTempValue": wtWebGraphThermoBaroTempValue,
       "wtWebGraphThermoBaroBinaryTempValueTable": wtWebGraphThermoBaroBinaryTempValueTable,
       "wtWebGraphThermoBaroBinaryTempValueEntry": wtWebGraphThermoBaroBinaryTempValueEntry,
       "wtWebGraphThermoBaroBinaryTempValue": wtWebGraphThermoBaroBinaryTempValue,
       "wtWebGraphThermoBaroTempValuePktTable": wtWebGraphThermoBaroTempValuePktTable,
       "wtWebGraphThermoBaroTempValuePktEntry": wtWebGraphThermoBaroTempValuePktEntry,
       "wtWebGraphThermoBaroTempValuePkt": wtWebGraphThermoBaroTempValuePkt,
       "wtWebGraphThermoBaroSessCntrl": wtWebGraphThermoBaroSessCntrl,
       "wtWebGraphThermoBaroSessCntrlPassword": wtWebGraphThermoBaroSessCntrlPassword,
       "wtWebGraphThermoBaroSessCntrlConfigMode": wtWebGraphThermoBaroSessCntrlConfigMode,
       "wtWebGraphThermoBaroSessCntrlLogout": wtWebGraphThermoBaroSessCntrlLogout,
       "wtWebGraphThermoBaroSessCntrlAdminPassword": wtWebGraphThermoBaroSessCntrlAdminPassword,
       "wtWebGraphThermoBaroSessCntrlConfigPassword": wtWebGraphThermoBaroSessCntrlConfigPassword,
       "wtWebGraphThermoBaroConfig": wtWebGraphThermoBaroConfig,
       "wtWebGraphThermoBaroDevice": wtWebGraphThermoBaroDevice,
       "wtWebGraphThermoBaroText": wtWebGraphThermoBaroText,
       "wtWebGraphThermoBaroDeviceName": wtWebGraphThermoBaroDeviceName,
       "wtWebGraphThermoBaroDeviceText": wtWebGraphThermoBaroDeviceText,
       "wtWebGraphThermoBaroDeviceLocation": wtWebGraphThermoBaroDeviceLocation,
       "wtWebGraphThermoBaroDeviceContact": wtWebGraphThermoBaroDeviceContact,
       "wtWebGraphThermoBaroTimeDate": wtWebGraphThermoBaroTimeDate,
       "wtWebGraphThermoBaroTimeZone": wtWebGraphThermoBaroTimeZone,
       "wtWebGraphThermoBaroTzOffsetHrs": wtWebGraphThermoBaroTzOffsetHrs,
       "wtWebGraphThermoBaroTzOffsetMin": wtWebGraphThermoBaroTzOffsetMin,
       "wtWebGraphThermoBaroTzEnable": wtWebGraphThermoBaroTzEnable,
       "wtWebGraphThermoBaroStTzOffsetHrs": wtWebGraphThermoBaroStTzOffsetHrs,
       "wtWebGraphThermoBaroStTzOffsetMin": wtWebGraphThermoBaroStTzOffsetMin,
       "wtWebGraphThermoBaroStTzEnable": wtWebGraphThermoBaroStTzEnable,
       "wtWebGraphThermoBaroStTzStartMonth": wtWebGraphThermoBaroStTzStartMonth,
       "wtWebGraphThermoBaroStTzStartMode": wtWebGraphThermoBaroStTzStartMode,
       "wtWebGraphThermoBaroStTzStartWday": wtWebGraphThermoBaroStTzStartWday,
       "wtWebGraphThermoBaroStTzStartHrs": wtWebGraphThermoBaroStTzStartHrs,
       "wtWebGraphThermoBaroStTzStartMin": wtWebGraphThermoBaroStTzStartMin,
       "wtWebGraphThermoBaroStTzStopMonth": wtWebGraphThermoBaroStTzStopMonth,
       "wtWebGraphThermoBaroStTzStopMode": wtWebGraphThermoBaroStTzStopMode,
       "wtWebGraphThermoBaroStTzStopWday": wtWebGraphThermoBaroStTzStopWday,
       "wtWebGraphThermoBaroStTzStopHrs": wtWebGraphThermoBaroStTzStopHrs,
       "wtWebGraphThermoBaroStTzStopMin": wtWebGraphThermoBaroStTzStopMin,
       "wtWebGraphThermoBaroTimeServer": wtWebGraphThermoBaroTimeServer,
       "wtWebGraphThermoBaroTimeServer1": wtWebGraphThermoBaroTimeServer1,
       "wtWebGraphThermoBaroTimeServer2": wtWebGraphThermoBaroTimeServer2,
       "wtWebGraphThermoBaroTsEnable": wtWebGraphThermoBaroTsEnable,
       "wtWebGraphThermoBaroTsSyncTime": wtWebGraphThermoBaroTsSyncTime,
       "wtWebGraphThermoBaroDeviceClock": wtWebGraphThermoBaroDeviceClock,
       "wtWebGraphThermoBaroClockHrs": wtWebGraphThermoBaroClockHrs,
       "wtWebGraphThermoBaroClockMin": wtWebGraphThermoBaroClockMin,
       "wtWebGraphThermoBaroClockDay": wtWebGraphThermoBaroClockDay,
       "wtWebGraphThermoBaroClockMonth": wtWebGraphThermoBaroClockMonth,
       "wtWebGraphThermoBaroClockYear": wtWebGraphThermoBaroClockYear,
       "wtWebGraphThermoBaroBasic": wtWebGraphThermoBaroBasic,
       "wtWebGraphThermoBaroNetwork": wtWebGraphThermoBaroNetwork,
       "wtWebGraphThermoBaroIpAddress": wtWebGraphThermoBaroIpAddress,
       "wtWebGraphThermoBaroSubnetMask": wtWebGraphThermoBaroSubnetMask,
       "wtWebGraphThermoBaroGateway": wtWebGraphThermoBaroGateway,
       "wtWebGraphThermoBaroDnsServer1": wtWebGraphThermoBaroDnsServer1,
       "wtWebGraphThermoBaroDnsServer2": wtWebGraphThermoBaroDnsServer2,
       "wtWebGraphThermoBaroAddConfig": wtWebGraphThermoBaroAddConfig,
       "wtWebGraphThermoBaroHTTP": wtWebGraphThermoBaroHTTP,
       "wtWebGraphThermoBaroStartup": wtWebGraphThermoBaroStartup,
       "wtWebGraphThermoBaroGetHeaderEnable": wtWebGraphThermoBaroGetHeaderEnable,
       "wtWebGraphThermoBaroHttpPort": wtWebGraphThermoBaroHttpPort,
       "wtWebGraphThermoBaroMail": wtWebGraphThermoBaroMail,
       "wtWebGraphThermoBaroMailAdName": wtWebGraphThermoBaroMailAdName,
       "wtWebGraphThermoBaroMailReply": wtWebGraphThermoBaroMailReply,
       "wtWebGraphThermoBaroMailServer": wtWebGraphThermoBaroMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphThermoBaroMailAuthentication": wtWebGraphThermoBaroMailAuthentication,
       "wtWebGraphThermoBaroMailAuthUser": wtWebGraphThermoBaroMailAuthUser,
       "wtWebGraphThermoBaroMailAuthPassword": wtWebGraphThermoBaroMailAuthPassword,
       "wtWebGraphThermoBaroMailPop3Server": wtWebGraphThermoBaroMailPop3Server,
       "wtWebGraphThermoBaroSNMP": wtWebGraphThermoBaroSNMP,
       "wtWebGraphThermoBaroSnmpCommunityStringRead": wtWebGraphThermoBaroSnmpCommunityStringRead,
       "wtWebGraphThermoBaroSnmpCommunityStringReadWrite": wtWebGraphThermoBaroSnmpCommunityStringReadWrite,
       "wtWebGraphThermoBaroSystemTrapManagerIP": wtWebGraphThermoBaroSystemTrapManagerIP,
       "wtWebGraphThermoBaroSystemTrapEnable": wtWebGraphThermoBaroSystemTrapEnable,
       "wtWebGraphThermoBaroSnmpEnable": wtWebGraphThermoBaroSnmpEnable,
       "wtWebGraphThermoBaroSnmpCommunityStringTrap": wtWebGraphThermoBaroSnmpCommunityStringTrap,
       "wtWebGraphThermoBaroUDP": wtWebGraphThermoBaroUDP,
       "wtWebGraphThermoBaroUdpPort": wtWebGraphThermoBaroUdpPort,
       "wtWebGraphThermoBaroUdpEnable": wtWebGraphThermoBaroUdpEnable,
       "wtWebGraphThermoBaroSyslog": wtWebGraphThermoBaroSyslog,
       "wtWebGraphThermoBaroSyslogServerIP": wtWebGraphThermoBaroSyslogServerIP,
       "wtWebGraphThermoBaroSyslogServerPort": wtWebGraphThermoBaroSyslogServerPort,
       "wtWebGraphThermoBaroSyslogSystemMessagesEnable": wtWebGraphThermoBaroSyslogSystemMessagesEnable,
       "wtWebGraphThermoBaroSyslogEnable": wtWebGraphThermoBaroSyslogEnable,
       "wtWebGraphThermoBaroFTP": wtWebGraphThermoBaroFTP,
       "wtWebGraphThermoBaroFTPServerIP": wtWebGraphThermoBaroFTPServerIP,
       "wtWebGraphThermoBaroFTPServerControlPort": wtWebGraphThermoBaroFTPServerControlPort,
       "wtWebGraphThermoBaroFTPUserName": wtWebGraphThermoBaroFTPUserName,
       "wtWebGraphThermoBaroFTPPassword": wtWebGraphThermoBaroFTPPassword,
       "wtWebGraphThermoBaroFTPAccount": wtWebGraphThermoBaroFTPAccount,
       "wtWebGraphThermoBaroFTPOption": wtWebGraphThermoBaroFTPOption,
       "wtWebGraphThermoBaroFTPEnable": wtWebGraphThermoBaroFTPEnable,
       "wtWebGraphThermoBaroRSS": wtWebGraphThermoBaroRSS,
       "wtWebGraphThermoBaroRSSChannelTitle": wtWebGraphThermoBaroRSSChannelTitle,
       "wtWebGraphThermoBaroRSSChannelLink": wtWebGraphThermoBaroRSSChannelLink,
       "wtWebGraphThermoBaroRSSChannelDescription": wtWebGraphThermoBaroRSSChannelDescription,
       "wtWebGraphThermoBaroRSSChannelImage": wtWebGraphThermoBaroRSSChannelImage,
       "wtWebGraphThermoBaroRSSChannelImageTitle": wtWebGraphThermoBaroRSSChannelImageTitle,
       "wtWebGraphThermoBaroRSSChannelImageLink": wtWebGraphThermoBaroRSSChannelImageLink,
       "wtWebGraphThermoBaroRSSChannelItemTitle": wtWebGraphThermoBaroRSSChannelItemTitle,
       "wtWebGraphThermoBaroRSSChannelItemLink": wtWebGraphThermoBaroRSSChannelItemLink,
       "wtWebGraphThermoBaroRSSChannelItemDescription": wtWebGraphThermoBaroRSSChannelItemDescription,
       "wtWebGraphThermoBaroRSSChannelItemQuantity": wtWebGraphThermoBaroRSSChannelItemQuantity,
       "wtWebGraphThermoBaroLanguage": wtWebGraphThermoBaroLanguage,
       "wtWebGraphThermoBaroLanguageSelect": wtWebGraphThermoBaroLanguageSelect,
       "wtWebGraphThermoBaroDatalogger": wtWebGraphThermoBaroDatalogger,
       "wtWebGraphThermoBaroLoggerTimebase": wtWebGraphThermoBaroLoggerTimebase,
       "wtWebGraphThermoBaroLoggerSensorSel": wtWebGraphThermoBaroLoggerSensorSel,
       "wtWebGraphThermoBaroAlarm": wtWebGraphThermoBaroAlarm,
       "wtWebGraphThermoBaroAlarmCount": wtWebGraphThermoBaroAlarmCount,
       "wtWebGraphThermoBaroAlarmIfTable": wtWebGraphThermoBaroAlarmIfTable,
       "wtWebGraphThermoBaroAlarmIfEntry": wtWebGraphThermoBaroAlarmIfEntry,
       "wtWebGraphThermoBaroAlarmNo": wtWebGraphThermoBaroAlarmNo,
       "wtWebGraphThermoBaroAlarmTable": wtWebGraphThermoBaroAlarmTable,
       "wtWebGraphThermoBaroAlarmEntry": wtWebGraphThermoBaroAlarmEntry,
       "wtWebGraphThermoBaroAlarmTrigger": wtWebGraphThermoBaroAlarmTrigger,
       "wtWebGraphThermoBaroAlarmMin": wtWebGraphThermoBaroAlarmMin,
       "wtWebGraphThermoBaroAlarmMax": wtWebGraphThermoBaroAlarmMax,
       "wtWebGraphThermoBaroAlarmHysteresis": wtWebGraphThermoBaroAlarmHysteresis,
       "wtWebGraphThermoBaroAlarmDelay": wtWebGraphThermoBaroAlarmDelay,
       "wtWebGraphThermoBaroAlarmInterval": wtWebGraphThermoBaroAlarmInterval,
       "wtWebGraphThermoBaroAlarmEnable": wtWebGraphThermoBaroAlarmEnable,
       "wtWebGraphThermoBaroAlarmEMailAddr": wtWebGraphThermoBaroAlarmEMailAddr,
       "wtWebGraphThermoBaroAlarmMailSubject": wtWebGraphThermoBaroAlarmMailSubject,
       "wtWebGraphThermoBaroAlarmMailText": wtWebGraphThermoBaroAlarmMailText,
       "wtWebGraphThermoBaroAlarmManagerIP": wtWebGraphThermoBaroAlarmManagerIP,
       "wtWebGraphThermoBaroAlarmTrapText": wtWebGraphThermoBaroAlarmTrapText,
       "wtWebGraphThermoBaroAlarmMailOptions": wtWebGraphThermoBaroAlarmMailOptions,
       "wtWebGraphThermoBaroAlarmTcpIpAddr": wtWebGraphThermoBaroAlarmTcpIpAddr,
       "wtWebGraphThermoBaroAlarmTcpPort": wtWebGraphThermoBaroAlarmTcpPort,
       "wtWebGraphThermoBaroAlarmTcpText": wtWebGraphThermoBaroAlarmTcpText,
       "wtWebGraphThermoBaroAlarmClearMailSubject": wtWebGraphThermoBaroAlarmClearMailSubject,
       "wtWebGraphThermoBaroAlarmClearMailText": wtWebGraphThermoBaroAlarmClearMailText,
       "wtWebGraphThermoBaroAlarmClearTrapText": wtWebGraphThermoBaroAlarmClearTrapText,
       "wtWebGraphThermoBaroAlarmClearTcpText": wtWebGraphThermoBaroAlarmClearTcpText,
       "wtWebGraphThermoBaroAlarmDeltaTemp": wtWebGraphThermoBaroAlarmDeltaTemp,
       "wtWebGraphThermoBaroAlarmRHMin": wtWebGraphThermoBaroAlarmRHMin,
       "wtWebGraphThermoBaroAlarmRHMax": wtWebGraphThermoBaroAlarmRHMax,
       "wtWebGraphThermoBaroAlarmRHHysteresis": wtWebGraphThermoBaroAlarmRHHysteresis,
       "wtWebGraphThermoBaroAlarmAHMin": wtWebGraphThermoBaroAlarmAHMin,
       "wtWebGraphThermoBaroAlarmAHMax": wtWebGraphThermoBaroAlarmAHMax,
       "wtWebGraphThermoBaroAlarmSyslogIpAddr": wtWebGraphThermoBaroAlarmSyslogIpAddr,
       "wtWebGraphThermoBaroAlarmSyslogPort": wtWebGraphThermoBaroAlarmSyslogPort,
       "wtWebGraphThermoBaroAlarmSyslogText": wtWebGraphThermoBaroAlarmSyslogText,
       "wtWebGraphThermoBaroAlarmSyslogClearText": wtWebGraphThermoBaroAlarmSyslogClearText,
       "wtWebGraphThermoBaroAlarmFtpDataPort": wtWebGraphThermoBaroAlarmFtpDataPort,
       "wtWebGraphThermoBaroAlarmFtpFileName": wtWebGraphThermoBaroAlarmFtpFileName,
       "wtWebGraphThermoBaroAlarmFtpText": wtWebGraphThermoBaroAlarmFtpText,
       "wtWebGraphThermoBaroAlarmFtpClearText": wtWebGraphThermoBaroAlarmFtpClearText,
       "wtWebGraphThermoBaroAlarmFtpOption": wtWebGraphThermoBaroAlarmFtpOption,
       "wtWebGraphThermoBaroAlarmTimerCron": wtWebGraphThermoBaroAlarmTimerCron,
       "wtWebGraphThermoBaroAlarmName": wtWebGraphThermoBaroAlarmName,
       "wtWebGraphThermoBaroAlarmActive": wtWebGraphThermoBaroAlarmActive,
       "wtWebGraphThermoBaroGraphics": wtWebGraphThermoBaroGraphics,
       "wtWebGraphThermoBaroGraphicsBase": wtWebGraphThermoBaroGraphicsBase,
       "wtWebGraphThermoBaroGraphicsBaseEnable": wtWebGraphThermoBaroGraphicsBaseEnable,
       "wtWebGraphThermoBaroGraphicsBaseWidth": wtWebGraphThermoBaroGraphicsBaseWidth,
       "wtWebGraphThermoBaroGraphicsBaseHeight": wtWebGraphThermoBaroGraphicsBaseHeight,
       "wtWebGraphThermoBaroGraphicsBaseFrameColor": wtWebGraphThermoBaroGraphicsBaseFrameColor,
       "wtWebGraphThermoBaroGraphicsBaseBackgroundColor": wtWebGraphThermoBaroGraphicsBaseBackgroundColor,
       "wtWebGraphThermoBaroGraphicsBasePollingrate": wtWebGraphThermoBaroGraphicsBasePollingrate,
       "wtWebGraphThermoBaroGraphicsSelect": wtWebGraphThermoBaroGraphicsSelect,
       "wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel": wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel,
       "wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem": wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem,
       "wtWebGraphThermoBaroSensorColorTable": wtWebGraphThermoBaroSensorColorTable,
       "wtWebGraphThermoBaroSensorColorEntry": wtWebGraphThermoBaroSensorColorEntry,
       "wtWebGraphThermoBaroGraphicsSensorColor": wtWebGraphThermoBaroGraphicsSensorColor,
       "wtWebGraphThermoBaroGraphicsSelectScale": wtWebGraphThermoBaroGraphicsSelectScale,
       "wtWebGraphThermoBaroGraphicsScale": wtWebGraphThermoBaroGraphicsScale,
       "wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable": wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable,
       "wtWebGraphThermoBaroGraphicsScaleAutoFitEnable": wtWebGraphThermoBaroGraphicsScaleAutoFitEnable,
       "wtWebGraphThermoBaroGraphicsScale1Min": wtWebGraphThermoBaroGraphicsScale1Min,
       "wtWebGraphThermoBaroGraphicsScale2Min": wtWebGraphThermoBaroGraphicsScale2Min,
       "wtWebGraphThermoBaroGraphicsScale3Min": wtWebGraphThermoBaroGraphicsScale3Min,
       "wtWebGraphThermoBaroGraphicsScale4Min": wtWebGraphThermoBaroGraphicsScale4Min,
       "wtWebGraphThermoBaroGraphicsScale1Max": wtWebGraphThermoBaroGraphicsScale1Max,
       "wtWebGraphThermoBaroGraphicsScale2Max": wtWebGraphThermoBaroGraphicsScale2Max,
       "wtWebGraphThermoBaroGraphicsScale3Max": wtWebGraphThermoBaroGraphicsScale3Max,
       "wtWebGraphThermoBaroGraphicsScale4Max": wtWebGraphThermoBaroGraphicsScale4Max,
       "wtWebGraphThermoBaroGraphicsScale1Unit": wtWebGraphThermoBaroGraphicsScale1Unit,
       "wtWebGraphThermoBaroGraphicsScale2Unit": wtWebGraphThermoBaroGraphicsScale2Unit,
       "wtWebGraphThermoBaroGraphicsScale3Unit": wtWebGraphThermoBaroGraphicsScale3Unit,
       "wtWebGraphThermoBaroGraphicsScale4Unit": wtWebGraphThermoBaroGraphicsScale4Unit,
       "wtWebGraphThermoBaroPorts": wtWebGraphThermoBaroPorts,
       "wtWebGraphThermoBaroPortTable": wtWebGraphThermoBaroPortTable,
       "wtWebGraphThermoBaroPortEntry": wtWebGraphThermoBaroPortEntry,
       "wtWebGraphThermoBaroPortName": wtWebGraphThermoBaroPortName,
       "wtWebGraphThermoBaroPortText": wtWebGraphThermoBaroPortText,
       "wtWebGraphThermoBaroPortOffset1": wtWebGraphThermoBaroPortOffset1,
       "wtWebGraphThermoBaroPortTemperature1": wtWebGraphThermoBaroPortTemperature1,
       "wtWebGraphThermoBaroPortOffset2": wtWebGraphThermoBaroPortOffset2,
       "wtWebGraphThermoBaroPortTemperature2": wtWebGraphThermoBaroPortTemperature2,
       "wtWebGraphThermoBaroPortComment": wtWebGraphThermoBaroPortComment,
       "wtWebGraphThermoBaroPortAltidude": wtWebGraphThermoBaroPortAltidude,
       "wtWebGraphThermoBaroManufact": wtWebGraphThermoBaroManufact,
       "wtWebGraphThermoBaroMfName": wtWebGraphThermoBaroMfName,
       "wtWebGraphThermoBaroMfAddr": wtWebGraphThermoBaroMfAddr,
       "wtWebGraphThermoBaroMfHotline": wtWebGraphThermoBaroMfHotline,
       "wtWebGraphThermoBaroMfInternet": wtWebGraphThermoBaroMfInternet,
       "wtWebGraphThermoBaroMfDeviceTyp": wtWebGraphThermoBaroMfDeviceTyp,
       "wtWebGraphThermoBaroMfOrderNo": wtWebGraphThermoBaroMfOrderNo,
       "wtWebGraphThermoBaroDiag": wtWebGraphThermoBaroDiag,
       "wtWebGraphThermoBaroDiagErrorCount": wtWebGraphThermoBaroDiagErrorCount,
       "wtWebGraphThermoBaroDiagBinaryError": wtWebGraphThermoBaroDiagBinaryError,
       "wtWebGraphThermoBaroDiagErrorIndex": wtWebGraphThermoBaroDiagErrorIndex,
       "wtWebGraphThermoBaroDiagErrorMessage": wtWebGraphThermoBaroDiagErrorMessage,
       "wtWebGraphThermoBaroDiagErrorClear": wtWebGraphThermoBaroDiagErrorClear}
)
