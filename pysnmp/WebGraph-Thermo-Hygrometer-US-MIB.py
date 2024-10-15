# SNMP MIB module (WebGraph-Thermo-Hygrometer-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-Thermo-Hygrometer-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:39 2024
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
_WtWebGraphThermHygro_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygro = _WtWebGraphThermHygro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9)
)
_WtWebGraphThermHygroTemp_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroTemp = _WtWebGraphThermHygroTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1)
)


class _WtWebGraphThermHygroSensors_Type(Integer32):
    """Custom type wtWebGraphThermHygroSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermHygroSensors_Type.__name__ = "Integer32"
_WtWebGraphThermHygroSensors_Object = MibScalar
wtWebGraphThermHygroSensors = _WtWebGraphThermHygroSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 1),
    _WtWebGraphThermHygroSensors_Type()
)
wtWebGraphThermHygroSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensors.setStatus("mandatory")
_WtWebGraphThermHygroSensorTable_Object = MibTable
wtWebGraphThermHygroSensorTable = _WtWebGraphThermHygroSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorTable.setStatus("mandatory")
_WtWebGraphThermHygroSensorEntry_Object = MibTableRow
wtWebGraphThermHygroSensorEntry = _WtWebGraphThermHygroSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 2, 1)
)
wtWebGraphThermHygroSensorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorEntry.setStatus("mandatory")


class _WtWebGraphThermHygroSensorNo_Type(Integer32):
    """Custom type wtWebGraphThermHygroSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermHygroSensorNo_Type.__name__ = "Integer32"
_WtWebGraphThermHygroSensorNo_Object = MibTableColumn
wtWebGraphThermHygroSensorNo = _WtWebGraphThermHygroSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 2, 1, 1),
    _WtWebGraphThermHygroSensorNo_Type()
)
wtWebGraphThermHygroSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorNo.setStatus("mandatory")
_WtWebGraphThermHygroTempValueTable_Object = MibTable
wtWebGraphThermHygroTempValueTable = _WtWebGraphThermHygroTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTempValueTable.setStatus("mandatory")
_WtWebGraphThermHygroTempValueEntry_Object = MibTableRow
wtWebGraphThermHygroTempValueEntry = _WtWebGraphThermHygroTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 3, 1)
)
wtWebGraphThermHygroTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTempValueEntry.setStatus("mandatory")


class _WtWebGraphThermHygroTempValue_Type(OctetString):
    """Custom type wtWebGraphThermHygroTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphThermHygroTempValue_Type.__name__ = "OctetString"
_WtWebGraphThermHygroTempValue_Object = MibTableColumn
wtWebGraphThermHygroTempValue = _WtWebGraphThermHygroTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 3, 1, 1),
    _WtWebGraphThermHygroTempValue_Type()
)
wtWebGraphThermHygroTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTempValue.setStatus("mandatory")
_WtWebGraphThermHygroBinaryTempValueTable_Object = MibTable
wtWebGraphThermHygroBinaryTempValueTable = _WtWebGraphThermHygroBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroBinaryTempValueTable.setStatus("mandatory")
_WtWebGraphThermHygroBinaryTempValueEntry_Object = MibTableRow
wtWebGraphThermHygroBinaryTempValueEntry = _WtWebGraphThermHygroBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 4, 1)
)
wtWebGraphThermHygroBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroBinaryTempValueEntry.setStatus("mandatory")
_WtWebGraphThermHygroBinaryTempValue_Type = Integer32
_WtWebGraphThermHygroBinaryTempValue_Object = MibTableColumn
wtWebGraphThermHygroBinaryTempValue = _WtWebGraphThermHygroBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 1, 4, 1, 1),
    _WtWebGraphThermHygroBinaryTempValue_Type()
)
wtWebGraphThermHygroBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroBinaryTempValue.setStatus("mandatory")
_WtWebGraphThermHygroSessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroSessCntrl = _WtWebGraphThermHygroSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2)
)
_WtWebGraphThermHygroSessCntrlPassword_Type = OctetString
_WtWebGraphThermHygroSessCntrlPassword_Object = MibScalar
wtWebGraphThermHygroSessCntrlPassword = _WtWebGraphThermHygroSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2, 1),
    _WtWebGraphThermHygroSessCntrlPassword_Type()
)
wtWebGraphThermHygroSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSessCntrlPassword.setStatus("mandatory")


class _WtWebGraphThermHygroSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphThermHygroSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphThermHygroSessCntrl-NoSession", 0),
          ("wtWebGraphThermHygroSessCntrl-Session", 1))
    )


_WtWebGraphThermHygroSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphThermHygroSessCntrlConfigMode_Object = MibScalar
wtWebGraphThermHygroSessCntrlConfigMode = _WtWebGraphThermHygroSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2, 2),
    _WtWebGraphThermHygroSessCntrlConfigMode_Type()
)
wtWebGraphThermHygroSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphThermHygroSessCntrlLogout_Type = Integer32
_WtWebGraphThermHygroSessCntrlLogout_Object = MibScalar
wtWebGraphThermHygroSessCntrlLogout = _WtWebGraphThermHygroSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2, 3),
    _WtWebGraphThermHygroSessCntrlLogout_Type()
)
wtWebGraphThermHygroSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSessCntrlLogout.setStatus("mandatory")
_WtWebGraphThermHygroSessCntrlAdminPassword_Type = OctetString
_WtWebGraphThermHygroSessCntrlAdminPassword_Object = MibScalar
wtWebGraphThermHygroSessCntrlAdminPassword = _WtWebGraphThermHygroSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2, 4),
    _WtWebGraphThermHygroSessCntrlAdminPassword_Type()
)
wtWebGraphThermHygroSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphThermHygroSessCntrlConfigPassword_Type = OctetString
_WtWebGraphThermHygroSessCntrlConfigPassword_Object = MibScalar
wtWebGraphThermHygroSessCntrlConfigPassword = _WtWebGraphThermHygroSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 2, 5),
    _WtWebGraphThermHygroSessCntrlConfigPassword_Type()
)
wtWebGraphThermHygroSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphThermHygroConfig_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroConfig = _WtWebGraphThermHygroConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3)
)
_WtWebGraphThermHygroDevice_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroDevice = _WtWebGraphThermHygroDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1)
)
_WtWebGraphThermHygroText_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroText = _WtWebGraphThermHygroText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 1)
)
_WtWebGraphThermHygroDeviceName_Type = OctetString
_WtWebGraphThermHygroDeviceName_Object = MibScalar
wtWebGraphThermHygroDeviceName = _WtWebGraphThermHygroDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 1, 1),
    _WtWebGraphThermHygroDeviceName_Type()
)
wtWebGraphThermHygroDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDeviceName.setStatus("mandatory")
_WtWebGraphThermHygroDeviceText_Type = OctetString
_WtWebGraphThermHygroDeviceText_Object = MibScalar
wtWebGraphThermHygroDeviceText = _WtWebGraphThermHygroDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 1, 2),
    _WtWebGraphThermHygroDeviceText_Type()
)
wtWebGraphThermHygroDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDeviceText.setStatus("mandatory")
_WtWebGraphThermHygroDeviceLocation_Type = OctetString
_WtWebGraphThermHygroDeviceLocation_Object = MibScalar
wtWebGraphThermHygroDeviceLocation = _WtWebGraphThermHygroDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 1, 3),
    _WtWebGraphThermHygroDeviceLocation_Type()
)
wtWebGraphThermHygroDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDeviceLocation.setStatus("mandatory")
_WtWebGraphThermHygroDeviceContact_Type = OctetString
_WtWebGraphThermHygroDeviceContact_Object = MibScalar
wtWebGraphThermHygroDeviceContact = _WtWebGraphThermHygroDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 1, 4),
    _WtWebGraphThermHygroDeviceContact_Type()
)
wtWebGraphThermHygroDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDeviceContact.setStatus("mandatory")
_WtWebGraphThermHygroTimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroTimeDate = _WtWebGraphThermHygroTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2)
)
_WtWebGraphThermHygroTimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroTimeZone = _WtWebGraphThermHygroTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1)
)
_WtWebGraphThermHygroTzOffsetHrs_Type = Integer32
_WtWebGraphThermHygroTzOffsetHrs_Object = MibScalar
wtWebGraphThermHygroTzOffsetHrs = _WtWebGraphThermHygroTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 1),
    _WtWebGraphThermHygroTzOffsetHrs_Type()
)
wtWebGraphThermHygroTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermHygroTzOffsetMin_Type = Integer32
_WtWebGraphThermHygroTzOffsetMin_Object = MibScalar
wtWebGraphThermHygroTzOffsetMin = _WtWebGraphThermHygroTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 2),
    _WtWebGraphThermHygroTzOffsetMin_Type()
)
wtWebGraphThermHygroTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermHygroTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroTzEnable_Object = MibScalar
wtWebGraphThermHygroTzEnable = _WtWebGraphThermHygroTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 3),
    _WtWebGraphThermHygroTzEnable_Type()
)
wtWebGraphThermHygroTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTzEnable.setStatus("mandatory")
_WtWebGraphThermHygroStTzOffsetHrs_Type = Integer32
_WtWebGraphThermHygroStTzOffsetHrs_Object = MibScalar
wtWebGraphThermHygroStTzOffsetHrs = _WtWebGraphThermHygroStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 4),
    _WtWebGraphThermHygroStTzOffsetHrs_Type()
)
wtWebGraphThermHygroStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermHygroStTzOffsetMin_Type = Integer32
_WtWebGraphThermHygroStTzOffsetMin_Object = MibScalar
wtWebGraphThermHygroStTzOffsetMin = _WtWebGraphThermHygroStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 5),
    _WtWebGraphThermHygroStTzOffsetMin_Type()
)
wtWebGraphThermHygroStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermHygroStTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroStTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroStTzEnable_Object = MibScalar
wtWebGraphThermHygroStTzEnable = _WtWebGraphThermHygroStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 6),
    _WtWebGraphThermHygroStTzEnable_Type()
)
wtWebGraphThermHygroStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzEnable.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStartMonth based on Integer32"""
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
        *(("wtWebGraphThermHygroStartMonth-April", 4),
          ("wtWebGraphThermHygroStartMonth-August", 8),
          ("wtWebGraphThermHygroStartMonth-December", 12),
          ("wtWebGraphThermHygroStartMonth-February", 2),
          ("wtWebGraphThermHygroStartMonth-January", 1),
          ("wtWebGraphThermHygroStartMonth-July", 7),
          ("wtWebGraphThermHygroStartMonth-June", 6),
          ("wtWebGraphThermHygroStartMonth-March", 3),
          ("wtWebGraphThermHygroStartMonth-May", 5),
          ("wtWebGraphThermHygroStartMonth-November", 11),
          ("wtWebGraphThermHygroStartMonth-October", 10),
          ("wtWebGraphThermHygroStartMonth-September", 9))
    )


_WtWebGraphThermHygroStTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStartMonth_Object = MibScalar
wtWebGraphThermHygroStTzStartMonth = _WtWebGraphThermHygroStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 7),
    _WtWebGraphThermHygroStTzStartMonth_Type()
)
wtWebGraphThermHygroStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStartMonth.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStartMode_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStartMode based on Integer32"""
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
        *(("wtWebGraphThermHygroStartMode-first", 1),
          ("wtWebGraphThermHygroStartMode-fourth", 4),
          ("wtWebGraphThermHygroStartMode-last", 5),
          ("wtWebGraphThermHygroStartMode-second", 2),
          ("wtWebGraphThermHygroStartMode-third", 3))
    )


_WtWebGraphThermHygroStTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStartMode_Object = MibScalar
wtWebGraphThermHygroStTzStartMode = _WtWebGraphThermHygroStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 8),
    _WtWebGraphThermHygroStTzStartMode_Type()
)
wtWebGraphThermHygroStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStartMode.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStartWday_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStartWday based on Integer32"""
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
        *(("wtWebGraphThermHygroStartWday-Friday", 6),
          ("wtWebGraphThermHygroStartWday-Monday", 2),
          ("wtWebGraphThermHygroStartWday-Saturday", 7),
          ("wtWebGraphThermHygroStartWday-Sunday", 1),
          ("wtWebGraphThermHygroStartWday-Thursday", 4),
          ("wtWebGraphThermHygroStartWday-Tuesday", 3),
          ("wtWebGraphThermHygroStartWday-Wednesday", 5))
    )


_WtWebGraphThermHygroStTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStartWday_Object = MibScalar
wtWebGraphThermHygroStTzStartWday = _WtWebGraphThermHygroStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 9),
    _WtWebGraphThermHygroStTzStartWday_Type()
)
wtWebGraphThermHygroStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStartWday.setStatus("mandatory")
_WtWebGraphThermHygroStTzStartHrs_Type = Integer32
_WtWebGraphThermHygroStTzStartHrs_Object = MibScalar
wtWebGraphThermHygroStTzStartHrs = _WtWebGraphThermHygroStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 10),
    _WtWebGraphThermHygroStTzStartHrs_Type()
)
wtWebGraphThermHygroStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStartHrs.setStatus("mandatory")
_WtWebGraphThermHygroStTzStartMin_Type = Integer32
_WtWebGraphThermHygroStTzStartMin_Object = MibScalar
wtWebGraphThermHygroStTzStartMin = _WtWebGraphThermHygroStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 11),
    _WtWebGraphThermHygroStTzStartMin_Type()
)
wtWebGraphThermHygroStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStartMin.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStopMonth based on Integer32"""
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
        *(("wtWebGraphThermHygroStopMonth-April", 4),
          ("wtWebGraphThermHygroStopMonth-August", 8),
          ("wtWebGraphThermHygroStopMonth-December", 12),
          ("wtWebGraphThermHygroStopMonth-February", 2),
          ("wtWebGraphThermHygroStopMonth-January", 1),
          ("wtWebGraphThermHygroStopMonth-July", 7),
          ("wtWebGraphThermHygroStopMonth-June", 6),
          ("wtWebGraphThermHygroStopMonth-March", 3),
          ("wtWebGraphThermHygroStopMonth-May", 5),
          ("wtWebGraphThermHygroStopMonth-November", 11),
          ("wtWebGraphThermHygroStopMonth-October", 10),
          ("wtWebGraphThermHygroStopMonth-September", 9))
    )


_WtWebGraphThermHygroStTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStopMonth_Object = MibScalar
wtWebGraphThermHygroStTzStopMonth = _WtWebGraphThermHygroStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 12),
    _WtWebGraphThermHygroStTzStopMonth_Type()
)
wtWebGraphThermHygroStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStopMonth.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStopMode_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStopMode based on Integer32"""
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
        *(("wtWebGraphThermHygroStopMode-first", 1),
          ("wtWebGraphThermHygroStopMode-fourth", 4),
          ("wtWebGraphThermHygroStopMode-last", 5),
          ("wtWebGraphThermHygroStopMode-second", 2),
          ("wtWebGraphThermHygroStopMode-third", 3))
    )


_WtWebGraphThermHygroStTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStopMode_Object = MibScalar
wtWebGraphThermHygroStTzStopMode = _WtWebGraphThermHygroStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 13),
    _WtWebGraphThermHygroStTzStopMode_Type()
)
wtWebGraphThermHygroStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStopMode.setStatus("mandatory")


class _WtWebGraphThermHygroStTzStopWday_Type(Integer32):
    """Custom type wtWebGraphThermHygroStTzStopWday based on Integer32"""
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
        *(("wtWebGraphThermHygroStopWday-Friday", 6),
          ("wtWebGraphThermHygroStopWday-Monday", 2),
          ("wtWebGraphThermHygroStopWday-Saturday", 7),
          ("wtWebGraphThermHygroStopWday-Sunday", 1),
          ("wtWebGraphThermHygroStopWday-Thursday", 4),
          ("wtWebGraphThermHygroStopWday-Tuesday", 3),
          ("wtWebGraphThermHygroStopWday-Wednesday", 5))
    )


_WtWebGraphThermHygroStTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphThermHygroStTzStopWday_Object = MibScalar
wtWebGraphThermHygroStTzStopWday = _WtWebGraphThermHygroStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 14),
    _WtWebGraphThermHygroStTzStopWday_Type()
)
wtWebGraphThermHygroStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStopWday.setStatus("mandatory")
_WtWebGraphThermHygroStTzStopHrs_Type = Integer32
_WtWebGraphThermHygroStTzStopHrs_Object = MibScalar
wtWebGraphThermHygroStTzStopHrs = _WtWebGraphThermHygroStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 15),
    _WtWebGraphThermHygroStTzStopHrs_Type()
)
wtWebGraphThermHygroStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStopHrs.setStatus("mandatory")
_WtWebGraphThermHygroStTzStopMin_Type = Integer32
_WtWebGraphThermHygroStTzStopMin_Object = MibScalar
wtWebGraphThermHygroStTzStopMin = _WtWebGraphThermHygroStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 1, 16),
    _WtWebGraphThermHygroStTzStopMin_Type()
)
wtWebGraphThermHygroStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStTzStopMin.setStatus("mandatory")
_WtWebGraphThermHygroTimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroTimeServer = _WtWebGraphThermHygroTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 2)
)
_WtWebGraphThermHygroTimeServer1_Type = OctetString
_WtWebGraphThermHygroTimeServer1_Object = MibScalar
wtWebGraphThermHygroTimeServer1 = _WtWebGraphThermHygroTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 2, 1),
    _WtWebGraphThermHygroTimeServer1_Type()
)
wtWebGraphThermHygroTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTimeServer1.setStatus("mandatory")
_WtWebGraphThermHygroTimeServer2_Type = OctetString
_WtWebGraphThermHygroTimeServer2_Object = MibScalar
wtWebGraphThermHygroTimeServer2 = _WtWebGraphThermHygroTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 2, 2),
    _WtWebGraphThermHygroTimeServer2_Type()
)
wtWebGraphThermHygroTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTimeServer2.setStatus("mandatory")


class _WtWebGraphThermHygroTsEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroTsEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroTsEnable_Object = MibScalar
wtWebGraphThermHygroTsEnable = _WtWebGraphThermHygroTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 2, 3),
    _WtWebGraphThermHygroTsEnable_Type()
)
wtWebGraphThermHygroTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTsEnable.setStatus("mandatory")
_WtWebGraphThermHygroTsSyncTime_Type = Integer32
_WtWebGraphThermHygroTsSyncTime_Object = MibScalar
wtWebGraphThermHygroTsSyncTime = _WtWebGraphThermHygroTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 2, 4),
    _WtWebGraphThermHygroTsSyncTime_Type()
)
wtWebGraphThermHygroTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroTsSyncTime.setStatus("mandatory")
_WtWebGraphThermHygroDeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroDeviceClock = _WtWebGraphThermHygroDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3)
)


class _WtWebGraphThermHygroClockHrs_Type(Integer32):
    """Custom type wtWebGraphThermHygroClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphThermHygroClockHrs_Type.__name__ = "Integer32"
_WtWebGraphThermHygroClockHrs_Object = MibScalar
wtWebGraphThermHygroClockHrs = _WtWebGraphThermHygroClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3, 1),
    _WtWebGraphThermHygroClockHrs_Type()
)
wtWebGraphThermHygroClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroClockHrs.setStatus("mandatory")


class _WtWebGraphThermHygroClockMin_Type(Integer32):
    """Custom type wtWebGraphThermHygroClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphThermHygroClockMin_Type.__name__ = "Integer32"
_WtWebGraphThermHygroClockMin_Object = MibScalar
wtWebGraphThermHygroClockMin = _WtWebGraphThermHygroClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3, 2),
    _WtWebGraphThermHygroClockMin_Type()
)
wtWebGraphThermHygroClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroClockMin.setStatus("mandatory")


class _WtWebGraphThermHygroClockDay_Type(Integer32):
    """Custom type wtWebGraphThermHygroClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphThermHygroClockDay_Type.__name__ = "Integer32"
_WtWebGraphThermHygroClockDay_Object = MibScalar
wtWebGraphThermHygroClockDay = _WtWebGraphThermHygroClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3, 3),
    _WtWebGraphThermHygroClockDay_Type()
)
wtWebGraphThermHygroClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroClockDay.setStatus("mandatory")


class _WtWebGraphThermHygroClockMonth_Type(Integer32):
    """Custom type wtWebGraphThermHygroClockMonth based on Integer32"""
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
        *(("wtWebGraphThermHygroClockMonth-April", 4),
          ("wtWebGraphThermHygroClockMonth-August", 8),
          ("wtWebGraphThermHygroClockMonth-December", 12),
          ("wtWebGraphThermHygroClockMonth-February", 2),
          ("wtWebGraphThermHygroClockMonth-January", 1),
          ("wtWebGraphThermHygroClockMonth-July", 7),
          ("wtWebGraphThermHygroClockMonth-June", 6),
          ("wtWebGraphThermHygroClockMonth-March", 3),
          ("wtWebGraphThermHygroClockMonth-May", 5),
          ("wtWebGraphThermHygroClockMonth-November", 11),
          ("wtWebGraphThermHygroClockMonth-October", 10),
          ("wtWebGraphThermHygroClockMonth-September", 9))
    )


_WtWebGraphThermHygroClockMonth_Type.__name__ = "Integer32"
_WtWebGraphThermHygroClockMonth_Object = MibScalar
wtWebGraphThermHygroClockMonth = _WtWebGraphThermHygroClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3, 4),
    _WtWebGraphThermHygroClockMonth_Type()
)
wtWebGraphThermHygroClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroClockMonth.setStatus("mandatory")


class _WtWebGraphThermHygroClockYear_Type(Integer32):
    """Custom type wtWebGraphThermHygroClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphThermHygroClockYear_Type.__name__ = "Integer32"
_WtWebGraphThermHygroClockYear_Object = MibScalar
wtWebGraphThermHygroClockYear = _WtWebGraphThermHygroClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 2, 3, 5),
    _WtWebGraphThermHygroClockYear_Type()
)
wtWebGraphThermHygroClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroClockYear.setStatus("mandatory")
_WtWebGraphThermHygroBasic_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroBasic = _WtWebGraphThermHygroBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3)
)
_WtWebGraphThermHygroNetwork_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroNetwork = _WtWebGraphThermHygroNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1)
)
_WtWebGraphThermHygroIpAddress_Type = IpAddress
_WtWebGraphThermHygroIpAddress_Object = MibScalar
wtWebGraphThermHygroIpAddress = _WtWebGraphThermHygroIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 1),
    _WtWebGraphThermHygroIpAddress_Type()
)
wtWebGraphThermHygroIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroIpAddress.setStatus("mandatory")
_WtWebGraphThermHygroSubnetMask_Type = IpAddress
_WtWebGraphThermHygroSubnetMask_Object = MibScalar
wtWebGraphThermHygroSubnetMask = _WtWebGraphThermHygroSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 2),
    _WtWebGraphThermHygroSubnetMask_Type()
)
wtWebGraphThermHygroSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSubnetMask.setStatus("mandatory")
_WtWebGraphThermHygroGateway_Type = IpAddress
_WtWebGraphThermHygroGateway_Object = MibScalar
wtWebGraphThermHygroGateway = _WtWebGraphThermHygroGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 3),
    _WtWebGraphThermHygroGateway_Type()
)
wtWebGraphThermHygroGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroGateway.setStatus("mandatory")
_WtWebGraphThermHygroDnsServer1_Type = OctetString
_WtWebGraphThermHygroDnsServer1_Object = MibScalar
wtWebGraphThermHygroDnsServer1 = _WtWebGraphThermHygroDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 4),
    _WtWebGraphThermHygroDnsServer1_Type()
)
wtWebGraphThermHygroDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDnsServer1.setStatus("mandatory")
_WtWebGraphThermHygroDnsServer2_Type = OctetString
_WtWebGraphThermHygroDnsServer2_Object = MibScalar
wtWebGraphThermHygroDnsServer2 = _WtWebGraphThermHygroDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 5),
    _WtWebGraphThermHygroDnsServer2_Type()
)
wtWebGraphThermHygroDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDnsServer2.setStatus("mandatory")
_WtWebGraphThermHygroAddConfig_Type = OctetString
_WtWebGraphThermHygroAddConfig_Object = MibScalar
wtWebGraphThermHygroAddConfig = _WtWebGraphThermHygroAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 1, 6),
    _WtWebGraphThermHygroAddConfig_Type()
)
wtWebGraphThermHygroAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAddConfig.setStatus("mandatory")
_WtWebGraphThermHygroHTTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroHTTP = _WtWebGraphThermHygroHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 2)
)
_WtWebGraphThermHygroStartup_Type = OctetString
_WtWebGraphThermHygroStartup_Object = MibScalar
wtWebGraphThermHygroStartup = _WtWebGraphThermHygroStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 2, 1),
    _WtWebGraphThermHygroStartup_Type()
)
wtWebGraphThermHygroStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroStartup.setStatus("mandatory")
_WtWebGraphThermHygroGetHeaderEnable_Type = OctetString
_WtWebGraphThermHygroGetHeaderEnable_Object = MibScalar
wtWebGraphThermHygroGetHeaderEnable = _WtWebGraphThermHygroGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 2, 2),
    _WtWebGraphThermHygroGetHeaderEnable_Type()
)
wtWebGraphThermHygroGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroGetHeaderEnable.setStatus("mandatory")


class _WtWebGraphThermHygroHttpPort_Type(Integer32):
    """Custom type wtWebGraphThermHygroHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermHygroHttpPort_Type.__name__ = "Integer32"
_WtWebGraphThermHygroHttpPort_Object = MibScalar
wtWebGraphThermHygroHttpPort = _WtWebGraphThermHygroHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 2, 3),
    _WtWebGraphThermHygroHttpPort_Type()
)
wtWebGraphThermHygroHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroHttpPort.setStatus("mandatory")
_WtWebGraphThermHygroMail_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroMail = _WtWebGraphThermHygroMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3)
)
_WtWebGraphThermHygroMailAdName_Type = OctetString
_WtWebGraphThermHygroMailAdName_Object = MibScalar
wtWebGraphThermHygroMailAdName = _WtWebGraphThermHygroMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 1),
    _WtWebGraphThermHygroMailAdName_Type()
)
wtWebGraphThermHygroMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailAdName.setStatus("mandatory")
_WtWebGraphThermHygroMailReply_Type = OctetString
_WtWebGraphThermHygroMailReply_Object = MibScalar
wtWebGraphThermHygroMailReply = _WtWebGraphThermHygroMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 2),
    _WtWebGraphThermHygroMailReply_Type()
)
wtWebGraphThermHygroMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailReply.setStatus("mandatory")
_WtWebGraphThermHygroMailServer_Type = OctetString
_WtWebGraphThermHygroMailServer_Object = MibScalar
wtWebGraphThermHygroMailServer = _WtWebGraphThermHygroMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 3),
    _WtWebGraphThermHygroMailServer_Type()
)
wtWebGraphThermHygroMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphThermHygroMailAuthentication_Type(OctetString):
    """Custom type wtWebGraphThermHygroMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroMailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphThermHygroMailAuthentication_Object = MibScalar
wtWebGraphThermHygroMailAuthentication = _WtWebGraphThermHygroMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 5),
    _WtWebGraphThermHygroMailAuthentication_Type()
)
wtWebGraphThermHygroMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailAuthentication.setStatus("mandatory")
_WtWebGraphThermHygroMailAuthUser_Type = OctetString
_WtWebGraphThermHygroMailAuthUser_Object = MibScalar
wtWebGraphThermHygroMailAuthUser = _WtWebGraphThermHygroMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 6),
    _WtWebGraphThermHygroMailAuthUser_Type()
)
wtWebGraphThermHygroMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailAuthUser.setStatus("mandatory")
_WtWebGraphThermHygroMailAuthPassword_Type = OctetString
_WtWebGraphThermHygroMailAuthPassword_Object = MibScalar
wtWebGraphThermHygroMailAuthPassword = _WtWebGraphThermHygroMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 7),
    _WtWebGraphThermHygroMailAuthPassword_Type()
)
wtWebGraphThermHygroMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailAuthPassword.setStatus("mandatory")
_WtWebGraphThermHygroMailPop3Server_Type = OctetString
_WtWebGraphThermHygroMailPop3Server_Object = MibScalar
wtWebGraphThermHygroMailPop3Server = _WtWebGraphThermHygroMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 3, 8),
    _WtWebGraphThermHygroMailPop3Server_Type()
)
wtWebGraphThermHygroMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMailPop3Server.setStatus("mandatory")
_WtWebGraphThermHygroSNMP_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroSNMP = _WtWebGraphThermHygroSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4)
)
_WtWebGraphThermHygroSnmpCommunityStringRead_Type = OctetString
_WtWebGraphThermHygroSnmpCommunityStringRead_Object = MibScalar
wtWebGraphThermHygroSnmpCommunityStringRead = _WtWebGraphThermHygroSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 1),
    _WtWebGraphThermHygroSnmpCommunityStringRead_Type()
)
wtWebGraphThermHygroSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphThermHygroSnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphThermHygroSnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphThermHygroSnmpCommunityStringReadWrite = _WtWebGraphThermHygroSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 2),
    _WtWebGraphThermHygroSnmpCommunityStringReadWrite_Type()
)
wtWebGraphThermHygroSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphThermHygroSystemTrapManagerIP_Type = OctetString
_WtWebGraphThermHygroSystemTrapManagerIP_Object = MibScalar
wtWebGraphThermHygroSystemTrapManagerIP = _WtWebGraphThermHygroSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 3),
    _WtWebGraphThermHygroSystemTrapManagerIP_Type()
)
wtWebGraphThermHygroSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphThermHygroSystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroSystemTrapEnable_Object = MibScalar
wtWebGraphThermHygroSystemTrapEnable = _WtWebGraphThermHygroSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 4),
    _WtWebGraphThermHygroSystemTrapEnable_Type()
)
wtWebGraphThermHygroSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSystemTrapEnable.setStatus("mandatory")
_WtWebGraphThermHygroSnmpEnable_Type = OctetString
_WtWebGraphThermHygroSnmpEnable_Object = MibScalar
wtWebGraphThermHygroSnmpEnable = _WtWebGraphThermHygroSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 5),
    _WtWebGraphThermHygroSnmpEnable_Type()
)
wtWebGraphThermHygroSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSnmpEnable.setStatus("mandatory")
_WtWebGraphThermHygroSnmpCommunityStringTrap_Type = OctetString
_WtWebGraphThermHygroSnmpCommunityStringTrap_Object = MibScalar
wtWebGraphThermHygroSnmpCommunityStringTrap = _WtWebGraphThermHygroSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 4, 6),
    _WtWebGraphThermHygroSnmpCommunityStringTrap_Type()
)
wtWebGraphThermHygroSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphThermHygroUDP_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroUDP = _WtWebGraphThermHygroUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 5)
)


class _WtWebGraphThermHygroUdpPort_Type(Integer32):
    """Custom type wtWebGraphThermHygroUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermHygroUdpPort_Type.__name__ = "Integer32"
_WtWebGraphThermHygroUdpPort_Object = MibScalar
wtWebGraphThermHygroUdpPort = _WtWebGraphThermHygroUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 5, 1),
    _WtWebGraphThermHygroUdpPort_Type()
)
wtWebGraphThermHygroUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroUdpPort.setStatus("mandatory")
_WtWebGraphThermHygroUdpEnable_Type = OctetString
_WtWebGraphThermHygroUdpEnable_Object = MibScalar
wtWebGraphThermHygroUdpEnable = _WtWebGraphThermHygroUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 5, 2),
    _WtWebGraphThermHygroUdpEnable_Type()
)
wtWebGraphThermHygroUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroUdpEnable.setStatus("mandatory")
_WtWebGraphThermHygroSyslog_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroSyslog = _WtWebGraphThermHygroSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 6)
)
_WtWebGraphThermHygroSyslogServerIP_Type = OctetString
_WtWebGraphThermHygroSyslogServerIP_Object = MibScalar
wtWebGraphThermHygroSyslogServerIP = _WtWebGraphThermHygroSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 6, 1),
    _WtWebGraphThermHygroSyslogServerIP_Type()
)
wtWebGraphThermHygroSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSyslogServerIP.setStatus("mandatory")
_WtWebGraphThermHygroSyslogServerPort_Type = Integer32
_WtWebGraphThermHygroSyslogServerPort_Object = MibScalar
wtWebGraphThermHygroSyslogServerPort = _WtWebGraphThermHygroSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 6, 2),
    _WtWebGraphThermHygroSyslogServerPort_Type()
)
wtWebGraphThermHygroSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSyslogServerPort.setStatus("mandatory")


class _WtWebGraphThermHygroSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroSyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphThermHygroSyslogSystemMessagesEnable = _WtWebGraphThermHygroSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 6, 3),
    _WtWebGraphThermHygroSyslogSystemMessagesEnable_Type()
)
wtWebGraphThermHygroSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphThermHygroSyslogEnable_Type = OctetString
_WtWebGraphThermHygroSyslogEnable_Object = MibScalar
wtWebGraphThermHygroSyslogEnable = _WtWebGraphThermHygroSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 6, 4),
    _WtWebGraphThermHygroSyslogEnable_Type()
)
wtWebGraphThermHygroSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSyslogEnable.setStatus("mandatory")
_WtWebGraphThermHygroFTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroFTP = _WtWebGraphThermHygroFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7)
)
_WtWebGraphThermHygroFTPServerIP_Type = OctetString
_WtWebGraphThermHygroFTPServerIP_Object = MibScalar
wtWebGraphThermHygroFTPServerIP = _WtWebGraphThermHygroFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 1),
    _WtWebGraphThermHygroFTPServerIP_Type()
)
wtWebGraphThermHygroFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPServerIP.setStatus("mandatory")
_WtWebGraphThermHygroFTPServerControlPort_Type = Integer32
_WtWebGraphThermHygroFTPServerControlPort_Object = MibScalar
wtWebGraphThermHygroFTPServerControlPort = _WtWebGraphThermHygroFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 2),
    _WtWebGraphThermHygroFTPServerControlPort_Type()
)
wtWebGraphThermHygroFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPServerControlPort.setStatus("mandatory")
_WtWebGraphThermHygroFTPUserName_Type = OctetString
_WtWebGraphThermHygroFTPUserName_Object = MibScalar
wtWebGraphThermHygroFTPUserName = _WtWebGraphThermHygroFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 3),
    _WtWebGraphThermHygroFTPUserName_Type()
)
wtWebGraphThermHygroFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPUserName.setStatus("mandatory")
_WtWebGraphThermHygroFTPPassword_Type = OctetString
_WtWebGraphThermHygroFTPPassword_Object = MibScalar
wtWebGraphThermHygroFTPPassword = _WtWebGraphThermHygroFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 4),
    _WtWebGraphThermHygroFTPPassword_Type()
)
wtWebGraphThermHygroFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPPassword.setStatus("mandatory")
_WtWebGraphThermHygroFTPAccount_Type = OctetString
_WtWebGraphThermHygroFTPAccount_Object = MibScalar
wtWebGraphThermHygroFTPAccount = _WtWebGraphThermHygroFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 5),
    _WtWebGraphThermHygroFTPAccount_Type()
)
wtWebGraphThermHygroFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPAccount.setStatus("mandatory")
_WtWebGraphThermHygroFTPOption_Type = OctetString
_WtWebGraphThermHygroFTPOption_Object = MibScalar
wtWebGraphThermHygroFTPOption = _WtWebGraphThermHygroFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 6),
    _WtWebGraphThermHygroFTPOption_Type()
)
wtWebGraphThermHygroFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPOption.setStatus("mandatory")
_WtWebGraphThermHygroFTPEnable_Type = OctetString
_WtWebGraphThermHygroFTPEnable_Object = MibScalar
wtWebGraphThermHygroFTPEnable = _WtWebGraphThermHygroFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 3, 7, 7),
    _WtWebGraphThermHygroFTPEnable_Type()
)
wtWebGraphThermHygroFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroFTPEnable.setStatus("mandatory")
_WtWebGraphThermHygroDatalogger_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroDatalogger = _WtWebGraphThermHygroDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4)
)


class _WtWebGraphThermHygroLoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphThermHygroLoggerTimebase based on Integer32"""
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
        *(("wtWebGraphThermHygroDatalogger-15Min", 3),
          ("wtWebGraphThermHygroDatalogger-1Min", 1),
          ("wtWebGraphThermHygroDatalogger-5Min", 2),
          ("wtWebGraphThermHygroDatalogger-60Min", 4))
    )


_WtWebGraphThermHygroLoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphThermHygroLoggerTimebase_Object = MibScalar
wtWebGraphThermHygroLoggerTimebase = _WtWebGraphThermHygroLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 1),
    _WtWebGraphThermHygroLoggerTimebase_Type()
)
wtWebGraphThermHygroLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroLoggerTimebase.setStatus("mandatory")


class _WtWebGraphThermHygroLoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphThermHygroLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermHygroLoggerSensorSel_Object = MibScalar
wtWebGraphThermHygroLoggerSensorSel = _WtWebGraphThermHygroLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 2),
    _WtWebGraphThermHygroLoggerSensorSel_Type()
)
wtWebGraphThermHygroLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroLoggerSensorSel.setStatus("mandatory")


class _WtWebGraphThermHygroDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphThermHygroDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermHygroDisplaySensorSel_Object = MibScalar
wtWebGraphThermHygroDisplaySensorSel = _WtWebGraphThermHygroDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 3),
    _WtWebGraphThermHygroDisplaySensorSel_Type()
)
wtWebGraphThermHygroDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDisplaySensorSel.setStatus("mandatory")
_WtWebGraphThermHygroSensorColorTable_Object = MibTable
wtWebGraphThermHygroSensorColorTable = _WtWebGraphThermHygroSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorColorTable.setStatus("mandatory")
_WtWebGraphThermHygroSensorColorEntry_Object = MibTableRow
wtWebGraphThermHygroSensorColorEntry = _WtWebGraphThermHygroSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 4, 1)
)
wtWebGraphThermHygroSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorColorEntry.setStatus("mandatory")


class _WtWebGraphThermHygroSensorColor_Type(OctetString):
    """Custom type wtWebGraphThermHygroSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphThermHygroSensorColor_Type.__name__ = "OctetString"
_WtWebGraphThermHygroSensorColor_Object = MibTableColumn
wtWebGraphThermHygroSensorColor = _WtWebGraphThermHygroSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 4, 1, 1),
    _WtWebGraphThermHygroSensorColor_Type()
)
wtWebGraphThermHygroSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroSensorColor.setStatus("mandatory")
_WtWebGraphThermHygroAutoScaleEnable_Type = OctetString
_WtWebGraphThermHygroAutoScaleEnable_Object = MibScalar
wtWebGraphThermHygroAutoScaleEnable = _WtWebGraphThermHygroAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 5),
    _WtWebGraphThermHygroAutoScaleEnable_Type()
)
wtWebGraphThermHygroAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAutoScaleEnable.setStatus("mandatory")
_WtWebGraphThermHygroVerticalUpperLimit_Type = OctetString
_WtWebGraphThermHygroVerticalUpperLimit_Object = MibScalar
wtWebGraphThermHygroVerticalUpperLimit = _WtWebGraphThermHygroVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 6),
    _WtWebGraphThermHygroVerticalUpperLimit_Type()
)
wtWebGraphThermHygroVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroVerticalUpperLimit.setStatus("mandatory")
_WtWebGraphThermHygroVerticalLowerLimit_Type = OctetString
_WtWebGraphThermHygroVerticalLowerLimit_Object = MibScalar
wtWebGraphThermHygroVerticalLowerLimit = _WtWebGraphThermHygroVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 7),
    _WtWebGraphThermHygroVerticalLowerLimit_Type()
)
wtWebGraphThermHygroVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroVerticalLowerLimit.setStatus("mandatory")


class _WtWebGraphThermHygroHorizontalZoom_Type(Integer32):
    """Custom type wtWebGraphThermHygroHorizontalZoom based on Integer32"""
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
        *(("wtWebGraphThermHygroZoom-25days", 6),
          ("wtWebGraphThermHygroZoom-25min", 1),
          ("wtWebGraphThermHygroZoom-30hrs", 4),
          ("wtWebGraphThermHygroZoom-5days", 5),
          ("wtWebGraphThermHygroZoom-5hrs", 3),
          ("wtWebGraphThermHygroZoom-75min", 2))
    )


_WtWebGraphThermHygroHorizontalZoom_Type.__name__ = "Integer32"
_WtWebGraphThermHygroHorizontalZoom_Object = MibScalar
wtWebGraphThermHygroHorizontalZoom = _WtWebGraphThermHygroHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 4, 8),
    _WtWebGraphThermHygroHorizontalZoom_Type()
)
wtWebGraphThermHygroHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroHorizontalZoom.setStatus("mandatory")
_WtWebGraphThermHygroAlarm_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroAlarm = _WtWebGraphThermHygroAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5)
)


class _WtWebGraphThermHygroAlarmCount_Type(Integer32):
    """Custom type wtWebGraphThermHygroAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermHygroAlarmCount_Type.__name__ = "Integer32"
_WtWebGraphThermHygroAlarmCount_Object = MibScalar
wtWebGraphThermHygroAlarmCount = _WtWebGraphThermHygroAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 1),
    _WtWebGraphThermHygroAlarmCount_Type()
)
wtWebGraphThermHygroAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmCount.setStatus("mandatory")
_WtWebGraphThermHygroAlarmIfTable_Object = MibTable
wtWebGraphThermHygroAlarmIfTable = _WtWebGraphThermHygroAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmIfTable.setStatus("mandatory")
_WtWebGraphThermHygroAlarmIfEntry_Object = MibTableRow
wtWebGraphThermHygroAlarmIfEntry = _WtWebGraphThermHygroAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 2, 1)
)
wtWebGraphThermHygroAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmIfEntry.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmNo_Type(Integer32):
    """Custom type wtWebGraphThermHygroAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermHygroAlarmNo_Type.__name__ = "Integer32"
_WtWebGraphThermHygroAlarmNo_Object = MibTableColumn
wtWebGraphThermHygroAlarmNo = _WtWebGraphThermHygroAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 2, 1, 1),
    _WtWebGraphThermHygroAlarmNo_Type()
)
wtWebGraphThermHygroAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmNo.setStatus("mandatory")
_WtWebGraphThermHygroAlarmTable_Object = MibTable
wtWebGraphThermHygroAlarmTable = _WtWebGraphThermHygroAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTable.setStatus("mandatory")
_WtWebGraphThermHygroAlarmEntry_Object = MibTableRow
wtWebGraphThermHygroAlarmEntry = _WtWebGraphThermHygroAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1)
)
wtWebGraphThermHygroAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmEntry.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphThermHygroAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroAlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphThermHygroAlarmTrigger_Object = MibTableColumn
wtWebGraphThermHygroAlarmTrigger = _WtWebGraphThermHygroAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 1),
    _WtWebGraphThermHygroAlarmTrigger_Type()
)
wtWebGraphThermHygroAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTrigger.setStatus("mandatory")
_WtWebGraphThermHygroAlarmMin_Type = OctetString
_WtWebGraphThermHygroAlarmMin_Object = MibTableColumn
wtWebGraphThermHygroAlarmMin = _WtWebGraphThermHygroAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 2),
    _WtWebGraphThermHygroAlarmMin_Type()
)
wtWebGraphThermHygroAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmMin.setStatus("mandatory")
_WtWebGraphThermHygroAlarmMax_Type = OctetString
_WtWebGraphThermHygroAlarmMax_Object = MibTableColumn
wtWebGraphThermHygroAlarmMax = _WtWebGraphThermHygroAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 3),
    _WtWebGraphThermHygroAlarmMax_Type()
)
wtWebGraphThermHygroAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmMax.setStatus("mandatory")
_WtWebGraphThermHygroAlarmHysteresis_Type = OctetString
_WtWebGraphThermHygroAlarmHysteresis_Object = MibTableColumn
wtWebGraphThermHygroAlarmHysteresis = _WtWebGraphThermHygroAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 4),
    _WtWebGraphThermHygroAlarmHysteresis_Type()
)
wtWebGraphThermHygroAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmHysteresis.setStatus("mandatory")
_WtWebGraphThermHygroAlarmDelay_Type = OctetString
_WtWebGraphThermHygroAlarmDelay_Object = MibTableColumn
wtWebGraphThermHygroAlarmDelay = _WtWebGraphThermHygroAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 5),
    _WtWebGraphThermHygroAlarmDelay_Type()
)
wtWebGraphThermHygroAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmDelay.setStatus("mandatory")
_WtWebGraphThermHygroAlarmInterval_Type = OctetString
_WtWebGraphThermHygroAlarmInterval_Object = MibTableColumn
wtWebGraphThermHygroAlarmInterval = _WtWebGraphThermHygroAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 6),
    _WtWebGraphThermHygroAlarmInterval_Type()
)
wtWebGraphThermHygroAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmInterval.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmEnable_Type(OctetString):
    """Custom type wtWebGraphThermHygroAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroAlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphThermHygroAlarmEnable_Object = MibTableColumn
wtWebGraphThermHygroAlarmEnable = _WtWebGraphThermHygroAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 7),
    _WtWebGraphThermHygroAlarmEnable_Type()
)
wtWebGraphThermHygroAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmEnable.setStatus("mandatory")
_WtWebGraphThermHygroAlarmEMailAddr_Type = OctetString
_WtWebGraphThermHygroAlarmEMailAddr_Object = MibTableColumn
wtWebGraphThermHygroAlarmEMailAddr = _WtWebGraphThermHygroAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 8),
    _WtWebGraphThermHygroAlarmEMailAddr_Type()
)
wtWebGraphThermHygroAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmEMailAddr.setStatus("mandatory")
_WtWebGraphThermHygroAlarmMailSubject_Type = OctetString
_WtWebGraphThermHygroAlarmMailSubject_Object = MibTableColumn
wtWebGraphThermHygroAlarmMailSubject = _WtWebGraphThermHygroAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 9),
    _WtWebGraphThermHygroAlarmMailSubject_Type()
)
wtWebGraphThermHygroAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmMailSubject.setStatus("mandatory")
_WtWebGraphThermHygroAlarmMailText_Type = OctetString
_WtWebGraphThermHygroAlarmMailText_Object = MibTableColumn
wtWebGraphThermHygroAlarmMailText = _WtWebGraphThermHygroAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 10),
    _WtWebGraphThermHygroAlarmMailText_Type()
)
wtWebGraphThermHygroAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmMailText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmManagerIP_Type = OctetString
_WtWebGraphThermHygroAlarmManagerIP_Object = MibTableColumn
wtWebGraphThermHygroAlarmManagerIP = _WtWebGraphThermHygroAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 11),
    _WtWebGraphThermHygroAlarmManagerIP_Type()
)
wtWebGraphThermHygroAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmManagerIP.setStatus("mandatory")
_WtWebGraphThermHygroAlarmTrapText_Type = OctetString
_WtWebGraphThermHygroAlarmTrapText_Object = MibTableColumn
wtWebGraphThermHygroAlarmTrapText = _WtWebGraphThermHygroAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 12),
    _WtWebGraphThermHygroAlarmTrapText_Type()
)
wtWebGraphThermHygroAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTrapText.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphThermHygroAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphThermHygroAlarmMailOptions_Object = MibTableColumn
wtWebGraphThermHygroAlarmMailOptions = _WtWebGraphThermHygroAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 13),
    _WtWebGraphThermHygroAlarmMailOptions_Type()
)
wtWebGraphThermHygroAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmMailOptions.setStatus("mandatory")
_WtWebGraphThermHygroAlarmTcpIpAddr_Type = OctetString
_WtWebGraphThermHygroAlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphThermHygroAlarmTcpIpAddr = _WtWebGraphThermHygroAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 14),
    _WtWebGraphThermHygroAlarmTcpIpAddr_Type()
)
wtWebGraphThermHygroAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphThermHygroAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermHygroAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphThermHygroAlarmTcpPort_Object = MibTableColumn
wtWebGraphThermHygroAlarmTcpPort = _WtWebGraphThermHygroAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 15),
    _WtWebGraphThermHygroAlarmTcpPort_Type()
)
wtWebGraphThermHygroAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTcpPort.setStatus("mandatory")
_WtWebGraphThermHygroAlarmTcpText_Type = OctetString
_WtWebGraphThermHygroAlarmTcpText_Object = MibTableColumn
wtWebGraphThermHygroAlarmTcpText = _WtWebGraphThermHygroAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 16),
    _WtWebGraphThermHygroAlarmTcpText_Type()
)
wtWebGraphThermHygroAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTcpText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmClearMailSubject_Type = OctetString
_WtWebGraphThermHygroAlarmClearMailSubject_Object = MibTableColumn
wtWebGraphThermHygroAlarmClearMailSubject = _WtWebGraphThermHygroAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 17),
    _WtWebGraphThermHygroAlarmClearMailSubject_Type()
)
wtWebGraphThermHygroAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphThermHygroAlarmClearMailText_Type = OctetString
_WtWebGraphThermHygroAlarmClearMailText_Object = MibTableColumn
wtWebGraphThermHygroAlarmClearMailText = _WtWebGraphThermHygroAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 18),
    _WtWebGraphThermHygroAlarmClearMailText_Type()
)
wtWebGraphThermHygroAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmClearMailText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmClearTrapText_Type = OctetString
_WtWebGraphThermHygroAlarmClearTrapText_Object = MibTableColumn
wtWebGraphThermHygroAlarmClearTrapText = _WtWebGraphThermHygroAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 19),
    _WtWebGraphThermHygroAlarmClearTrapText_Type()
)
wtWebGraphThermHygroAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmClearTrapText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmClearTcpText_Type = OctetString
_WtWebGraphThermHygroAlarmClearTcpText_Object = MibTableColumn
wtWebGraphThermHygroAlarmClearTcpText = _WtWebGraphThermHygroAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 20),
    _WtWebGraphThermHygroAlarmClearTcpText_Type()
)
wtWebGraphThermHygroAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmClearTcpText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmDeltaTemp_Type = OctetString
_WtWebGraphThermHygroAlarmDeltaTemp_Object = MibTableColumn
wtWebGraphThermHygroAlarmDeltaTemp = _WtWebGraphThermHygroAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 21),
    _WtWebGraphThermHygroAlarmDeltaTemp_Type()
)
wtWebGraphThermHygroAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmDeltaTemp.setStatus("mandatory")
_WtWebGraphThermHygroAlarmRHMin_Type = OctetString
_WtWebGraphThermHygroAlarmRHMin_Object = MibTableColumn
wtWebGraphThermHygroAlarmRHMin = _WtWebGraphThermHygroAlarmRHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 22),
    _WtWebGraphThermHygroAlarmRHMin_Type()
)
wtWebGraphThermHygroAlarmRHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmRHMin.setStatus("mandatory")
_WtWebGraphThermHygroAlarmRHMax_Type = OctetString
_WtWebGraphThermHygroAlarmRHMax_Object = MibTableColumn
wtWebGraphThermHygroAlarmRHMax = _WtWebGraphThermHygroAlarmRHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 23),
    _WtWebGraphThermHygroAlarmRHMax_Type()
)
wtWebGraphThermHygroAlarmRHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmRHMax.setStatus("mandatory")
_WtWebGraphThermHygroAlarmRHHysteresis_Type = OctetString
_WtWebGraphThermHygroAlarmRHHysteresis_Object = MibTableColumn
wtWebGraphThermHygroAlarmRHHysteresis = _WtWebGraphThermHygroAlarmRHHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 24),
    _WtWebGraphThermHygroAlarmRHHysteresis_Type()
)
wtWebGraphThermHygroAlarmRHHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmRHHysteresis.setStatus("mandatory")
_WtWebGraphThermHygroAlarmAHMin_Type = OctetString
_WtWebGraphThermHygroAlarmAHMin_Object = MibTableColumn
wtWebGraphThermHygroAlarmAHMin = _WtWebGraphThermHygroAlarmAHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 25),
    _WtWebGraphThermHygroAlarmAHMin_Type()
)
wtWebGraphThermHygroAlarmAHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmAHMin.setStatus("mandatory")
_WtWebGraphThermHygroAlarmAHMax_Type = OctetString
_WtWebGraphThermHygroAlarmAHMax_Object = MibTableColumn
wtWebGraphThermHygroAlarmAHMax = _WtWebGraphThermHygroAlarmAHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 26),
    _WtWebGraphThermHygroAlarmAHMax_Type()
)
wtWebGraphThermHygroAlarmAHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmAHMax.setStatus("mandatory")
_WtWebGraphThermHygroAlarmSyslogIpAddr_Type = IpAddress
_WtWebGraphThermHygroAlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphThermHygroAlarmSyslogIpAddr = _WtWebGraphThermHygroAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 27),
    _WtWebGraphThermHygroAlarmSyslogIpAddr_Type()
)
wtWebGraphThermHygroAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphThermHygroAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermHygroAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphThermHygroAlarmSyslogPort_Object = MibTableColumn
wtWebGraphThermHygroAlarmSyslogPort = _WtWebGraphThermHygroAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 28),
    _WtWebGraphThermHygroAlarmSyslogPort_Type()
)
wtWebGraphThermHygroAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmSyslogPort.setStatus("mandatory")
_WtWebGraphThermHygroAlarmSyslogText_Type = OctetString
_WtWebGraphThermHygroAlarmSyslogText_Object = MibTableColumn
wtWebGraphThermHygroAlarmSyslogText = _WtWebGraphThermHygroAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 29),
    _WtWebGraphThermHygroAlarmSyslogText_Type()
)
wtWebGraphThermHygroAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmSyslogText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmSyslogClearText_Type = OctetString
_WtWebGraphThermHygroAlarmSyslogClearText_Object = MibTableColumn
wtWebGraphThermHygroAlarmSyslogClearText = _WtWebGraphThermHygroAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 30),
    _WtWebGraphThermHygroAlarmSyslogClearText_Type()
)
wtWebGraphThermHygroAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmFtpDataPort_Type = OctetString
_WtWebGraphThermHygroAlarmFtpDataPort_Object = MibTableColumn
wtWebGraphThermHygroAlarmFtpDataPort = _WtWebGraphThermHygroAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 31),
    _WtWebGraphThermHygroAlarmFtpDataPort_Type()
)
wtWebGraphThermHygroAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphThermHygroAlarmFtpFileName_Type = OctetString
_WtWebGraphThermHygroAlarmFtpFileName_Object = MibTableColumn
wtWebGraphThermHygroAlarmFtpFileName = _WtWebGraphThermHygroAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 32),
    _WtWebGraphThermHygroAlarmFtpFileName_Type()
)
wtWebGraphThermHygroAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmFtpFileName.setStatus("mandatory")
_WtWebGraphThermHygroAlarmFtpText_Type = OctetString
_WtWebGraphThermHygroAlarmFtpText_Object = MibTableColumn
wtWebGraphThermHygroAlarmFtpText = _WtWebGraphThermHygroAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 33),
    _WtWebGraphThermHygroAlarmFtpText_Type()
)
wtWebGraphThermHygroAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmFtpText.setStatus("mandatory")
_WtWebGraphThermHygroAlarmFtpClearText_Type = OctetString
_WtWebGraphThermHygroAlarmFtpClearText_Object = MibTableColumn
wtWebGraphThermHygroAlarmFtpClearText = _WtWebGraphThermHygroAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 34),
    _WtWebGraphThermHygroAlarmFtpClearText_Type()
)
wtWebGraphThermHygroAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphThermHygroAlarmFtpOptions_Type(OctetString):
    """Custom type wtWebGraphThermHygroAlarmFtpOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroAlarmFtpOptions_Type.__name__ = "OctetString"
_WtWebGraphThermHygroAlarmFtpOptions_Object = MibScalar
wtWebGraphThermHygroAlarmFtpOptions = _WtWebGraphThermHygroAlarmFtpOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 35),
    _WtWebGraphThermHygroAlarmFtpOptions_Type()
)
wtWebGraphThermHygroAlarmFtpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmFtpOptions.setStatus("mandatory")
_WtWebGraphThermHygroAlarmTimerCron_Type = OctetString
_WtWebGraphThermHygroAlarmTimerCron_Object = MibTableColumn
wtWebGraphThermHygroAlarmTimerCron = _WtWebGraphThermHygroAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 1, 5, 3, 1, 36),
    _WtWebGraphThermHygroAlarmTimerCron_Type()
)
wtWebGraphThermHygroAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlarmTimerCron.setStatus("mandatory")
_WtWebGraphThermHygroPorts_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroPorts = _WtWebGraphThermHygroPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2)
)
_WtWebGraphThermHygroPortTable_Object = MibTable
wtWebGraphThermHygroPortTable = _WtWebGraphThermHygroPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortTable.setStatus("mandatory")
_WtWebGraphThermHygroPortEntry_Object = MibTableRow
wtWebGraphThermHygroPortEntry = _WtWebGraphThermHygroPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1)
)
wtWebGraphThermHygroPortEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortEntry.setStatus("mandatory")
_WtWebGraphThermHygroPortName_Type = OctetString
_WtWebGraphThermHygroPortName_Object = MibTableColumn
wtWebGraphThermHygroPortName = _WtWebGraphThermHygroPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 1),
    _WtWebGraphThermHygroPortName_Type()
)
wtWebGraphThermHygroPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortName.setStatus("mandatory")
_WtWebGraphThermHygroPortText_Type = OctetString
_WtWebGraphThermHygroPortText_Object = MibTableColumn
wtWebGraphThermHygroPortText = _WtWebGraphThermHygroPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 2),
    _WtWebGraphThermHygroPortText_Type()
)
wtWebGraphThermHygroPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortText.setStatus("mandatory")
_WtWebGraphThermHygroPortOffset1_Type = OctetString
_WtWebGraphThermHygroPortOffset1_Object = MibTableColumn
wtWebGraphThermHygroPortOffset1 = _WtWebGraphThermHygroPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 3),
    _WtWebGraphThermHygroPortOffset1_Type()
)
wtWebGraphThermHygroPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortOffset1.setStatus("mandatory")
_WtWebGraphThermHygroPortTemperature1_Type = OctetString
_WtWebGraphThermHygroPortTemperature1_Object = MibTableColumn
wtWebGraphThermHygroPortTemperature1 = _WtWebGraphThermHygroPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 4),
    _WtWebGraphThermHygroPortTemperature1_Type()
)
wtWebGraphThermHygroPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortTemperature1.setStatus("mandatory")
_WtWebGraphThermHygroPortOffset2_Type = OctetString
_WtWebGraphThermHygroPortOffset2_Object = MibTableColumn
wtWebGraphThermHygroPortOffset2 = _WtWebGraphThermHygroPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 5),
    _WtWebGraphThermHygroPortOffset2_Type()
)
wtWebGraphThermHygroPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortOffset2.setStatus("mandatory")
_WtWebGraphThermHygroPortTemperature2_Type = OctetString
_WtWebGraphThermHygroPortTemperature2_Object = MibTableColumn
wtWebGraphThermHygroPortTemperature2 = _WtWebGraphThermHygroPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 6),
    _WtWebGraphThermHygroPortTemperature2_Type()
)
wtWebGraphThermHygroPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortTemperature2.setStatus("mandatory")
_WtWebGraphThermHygroPortComment_Type = OctetString
_WtWebGraphThermHygroPortComment_Object = MibTableColumn
wtWebGraphThermHygroPortComment = _WtWebGraphThermHygroPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 7),
    _WtWebGraphThermHygroPortComment_Type()
)
wtWebGraphThermHygroPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortComment.setStatus("mandatory")


class _WtWebGraphThermHygroPortSensorSelect_Type(OctetString):
    """Custom type wtWebGraphThermHygroPortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphThermHygroPortSensorSelect_Type.__name__ = "OctetString"
_WtWebGraphThermHygroPortSensorSelect_Object = MibScalar
wtWebGraphThermHygroPortSensorSelect = _WtWebGraphThermHygroPortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 2, 1, 1, 8),
    _WtWebGraphThermHygroPortSensorSelect_Type()
)
wtWebGraphThermHygroPortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroPortSensorSelect.setStatus("mandatory")
_WtWebGraphThermHygroManufact_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroManufact = _WtWebGraphThermHygroManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3)
)
_WtWebGraphThermHygroMfName_Type = OctetString
_WtWebGraphThermHygroMfName_Object = MibScalar
wtWebGraphThermHygroMfName = _WtWebGraphThermHygroMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 1),
    _WtWebGraphThermHygroMfName_Type()
)
wtWebGraphThermHygroMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfName.setStatus("mandatory")
_WtWebGraphThermHygroMfAddr_Type = OctetString
_WtWebGraphThermHygroMfAddr_Object = MibScalar
wtWebGraphThermHygroMfAddr = _WtWebGraphThermHygroMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 2),
    _WtWebGraphThermHygroMfAddr_Type()
)
wtWebGraphThermHygroMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfAddr.setStatus("mandatory")
_WtWebGraphThermHygroMfHotline_Type = OctetString
_WtWebGraphThermHygroMfHotline_Object = MibScalar
wtWebGraphThermHygroMfHotline = _WtWebGraphThermHygroMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 3),
    _WtWebGraphThermHygroMfHotline_Type()
)
wtWebGraphThermHygroMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfHotline.setStatus("mandatory")
_WtWebGraphThermHygroMfInternet_Type = OctetString
_WtWebGraphThermHygroMfInternet_Object = MibScalar
wtWebGraphThermHygroMfInternet = _WtWebGraphThermHygroMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 4),
    _WtWebGraphThermHygroMfInternet_Type()
)
wtWebGraphThermHygroMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfInternet.setStatus("mandatory")
_WtWebGraphThermHygroMfDeviceTyp_Type = OctetString
_WtWebGraphThermHygroMfDeviceTyp_Object = MibScalar
wtWebGraphThermHygroMfDeviceTyp = _WtWebGraphThermHygroMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 5),
    _WtWebGraphThermHygroMfDeviceTyp_Type()
)
wtWebGraphThermHygroMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfDeviceTyp.setStatus("mandatory")
_WtWebGraphThermHygroMfOrderNo_Type = OctetString
_WtWebGraphThermHygroMfOrderNo_Object = MibScalar
wtWebGraphThermHygroMfOrderNo = _WtWebGraphThermHygroMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 3, 3, 6),
    _WtWebGraphThermHygroMfOrderNo_Type()
)
wtWebGraphThermHygroMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroMfOrderNo.setStatus("mandatory")
_WtWebGraphThermHygroDiag_ObjectIdentity = ObjectIdentity
wtWebGraphThermHygroDiag = _WtWebGraphThermHygroDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4)
)
_WtWebGraphThermHygroDiagErrorCount_Type = Integer32
_WtWebGraphThermHygroDiagErrorCount_Object = MibScalar
wtWebGraphThermHygroDiagErrorCount = _WtWebGraphThermHygroDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4, 1),
    _WtWebGraphThermHygroDiagErrorCount_Type()
)
wtWebGraphThermHygroDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDiagErrorCount.setStatus("mandatory")
_WtWebGraphThermHygroDiagBinaryError_Type = OctetString
_WtWebGraphThermHygroDiagBinaryError_Object = MibScalar
wtWebGraphThermHygroDiagBinaryError = _WtWebGraphThermHygroDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4, 2),
    _WtWebGraphThermHygroDiagBinaryError_Type()
)
wtWebGraphThermHygroDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDiagBinaryError.setStatus("mandatory")
_WtWebGraphThermHygroDiagErrorIndex_Type = Integer32
_WtWebGraphThermHygroDiagErrorIndex_Object = MibScalar
wtWebGraphThermHygroDiagErrorIndex = _WtWebGraphThermHygroDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4, 3),
    _WtWebGraphThermHygroDiagErrorIndex_Type()
)
wtWebGraphThermHygroDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDiagErrorIndex.setStatus("mandatory")
_WtWebGraphThermHygroDiagErrorMessage_Type = OctetString
_WtWebGraphThermHygroDiagErrorMessage_Object = MibScalar
wtWebGraphThermHygroDiagErrorMessage = _WtWebGraphThermHygroDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4, 4),
    _WtWebGraphThermHygroDiagErrorMessage_Type()
)
wtWebGraphThermHygroDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDiagErrorMessage.setStatus("mandatory")
_WtWebGraphThermHygroDiagErrorClear_Type = Integer32
_WtWebGraphThermHygroDiagErrorClear_Object = MibScalar
wtWebGraphThermHygroDiagErrorClear = _WtWebGraphThermHygroDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 4, 5),
    _WtWebGraphThermHygroDiagErrorClear_Type()
)
wtWebGraphThermHygroDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphThermHygroDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphThermHygroAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 31)
)
wtWebGraphThermHygroAlert1.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert1.setStatus(
        ""
    )

wtWebGraphThermHygroAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 32)
)
wtWebGraphThermHygroAlert2.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert2.setStatus(
        ""
    )

wtWebGraphThermHygroAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 33)
)
wtWebGraphThermHygroAlert3.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert3.setStatus(
        ""
    )

wtWebGraphThermHygroAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 34)
)
wtWebGraphThermHygroAlert4.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert4.setStatus(
        ""
    )

wtWebGraphThermHygroAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 35)
)
wtWebGraphThermHygroAlert5.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert5.setStatus(
        ""
    )

wtWebGraphThermHygroAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 36)
)
wtWebGraphThermHygroAlert6.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert6.setStatus(
        ""
    )

wtWebGraphThermHygroAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 37)
)
wtWebGraphThermHygroAlert7.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert7.setStatus(
        ""
    )

wtWebGraphThermHygroAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 38)
)
wtWebGraphThermHygroAlert8.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert8.setStatus(
        ""
    )

wtWebGraphThermHygroAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 91)
)
wtWebGraphThermHygroAlert9.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert9.setStatus(
        ""
    )

wtWebGraphThermHygroAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 92)
)
wtWebGraphThermHygroAlert10.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert10.setStatus(
        ""
    )

wtWebGraphThermHygroAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 93)
)
wtWebGraphThermHygroAlert11.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert11.setStatus(
        ""
    )

wtWebGraphThermHygroAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 94)
)
wtWebGraphThermHygroAlert12.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert12.setStatus(
        ""
    )

wtWebGraphThermHygroAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 95)
)
wtWebGraphThermHygroAlert13.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert13.setStatus(
        ""
    )

wtWebGraphThermHygroAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 96)
)
wtWebGraphThermHygroAlert14.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert14.setStatus(
        ""
    )

wtWebGraphThermHygroAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 97)
)
wtWebGraphThermHygroAlert15.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert15.setStatus(
        ""
    )

wtWebGraphThermHygroAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 98)
)
wtWebGraphThermHygroAlert16.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlert16.setStatus(
        ""
    )

wtWebGraphThermHygroAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 9, 0, 110)
)
wtWebGraphThermHygroAlertDiag.setObjects(
      *(("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroDiagErrorIndex"),
        ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermHygroDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphThermHygroAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermo-Hygrometer-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphThermHygro": wtWebGraphThermHygro,
       "wtWebGraphThermHygroAlert1": wtWebGraphThermHygroAlert1,
       "wtWebGraphThermHygroAlert2": wtWebGraphThermHygroAlert2,
       "wtWebGraphThermHygroAlert3": wtWebGraphThermHygroAlert3,
       "wtWebGraphThermHygroAlert4": wtWebGraphThermHygroAlert4,
       "wtWebGraphThermHygroAlert5": wtWebGraphThermHygroAlert5,
       "wtWebGraphThermHygroAlert6": wtWebGraphThermHygroAlert6,
       "wtWebGraphThermHygroAlert7": wtWebGraphThermHygroAlert7,
       "wtWebGraphThermHygroAlert8": wtWebGraphThermHygroAlert8,
       "wtWebGraphThermHygroAlert9": wtWebGraphThermHygroAlert9,
       "wtWebGraphThermHygroAlert10": wtWebGraphThermHygroAlert10,
       "wtWebGraphThermHygroAlert11": wtWebGraphThermHygroAlert11,
       "wtWebGraphThermHygroAlert12": wtWebGraphThermHygroAlert12,
       "wtWebGraphThermHygroAlert13": wtWebGraphThermHygroAlert13,
       "wtWebGraphThermHygroAlert14": wtWebGraphThermHygroAlert14,
       "wtWebGraphThermHygroAlert15": wtWebGraphThermHygroAlert15,
       "wtWebGraphThermHygroAlert16": wtWebGraphThermHygroAlert16,
       "wtWebGraphThermHygroAlertDiag": wtWebGraphThermHygroAlertDiag,
       "wtWebGraphThermHygroTemp": wtWebGraphThermHygroTemp,
       "wtWebGraphThermHygroSensors": wtWebGraphThermHygroSensors,
       "wtWebGraphThermHygroSensorTable": wtWebGraphThermHygroSensorTable,
       "wtWebGraphThermHygroSensorEntry": wtWebGraphThermHygroSensorEntry,
       "wtWebGraphThermHygroSensorNo": wtWebGraphThermHygroSensorNo,
       "wtWebGraphThermHygroTempValueTable": wtWebGraphThermHygroTempValueTable,
       "wtWebGraphThermHygroTempValueEntry": wtWebGraphThermHygroTempValueEntry,
       "wtWebGraphThermHygroTempValue": wtWebGraphThermHygroTempValue,
       "wtWebGraphThermHygroBinaryTempValueTable": wtWebGraphThermHygroBinaryTempValueTable,
       "wtWebGraphThermHygroBinaryTempValueEntry": wtWebGraphThermHygroBinaryTempValueEntry,
       "wtWebGraphThermHygroBinaryTempValue": wtWebGraphThermHygroBinaryTempValue,
       "wtWebGraphThermHygroSessCntrl": wtWebGraphThermHygroSessCntrl,
       "wtWebGraphThermHygroSessCntrlPassword": wtWebGraphThermHygroSessCntrlPassword,
       "wtWebGraphThermHygroSessCntrlConfigMode": wtWebGraphThermHygroSessCntrlConfigMode,
       "wtWebGraphThermHygroSessCntrlLogout": wtWebGraphThermHygroSessCntrlLogout,
       "wtWebGraphThermHygroSessCntrlAdminPassword": wtWebGraphThermHygroSessCntrlAdminPassword,
       "wtWebGraphThermHygroSessCntrlConfigPassword": wtWebGraphThermHygroSessCntrlConfigPassword,
       "wtWebGraphThermHygroConfig": wtWebGraphThermHygroConfig,
       "wtWebGraphThermHygroDevice": wtWebGraphThermHygroDevice,
       "wtWebGraphThermHygroText": wtWebGraphThermHygroText,
       "wtWebGraphThermHygroDeviceName": wtWebGraphThermHygroDeviceName,
       "wtWebGraphThermHygroDeviceText": wtWebGraphThermHygroDeviceText,
       "wtWebGraphThermHygroDeviceLocation": wtWebGraphThermHygroDeviceLocation,
       "wtWebGraphThermHygroDeviceContact": wtWebGraphThermHygroDeviceContact,
       "wtWebGraphThermHygroTimeDate": wtWebGraphThermHygroTimeDate,
       "wtWebGraphThermHygroTimeZone": wtWebGraphThermHygroTimeZone,
       "wtWebGraphThermHygroTzOffsetHrs": wtWebGraphThermHygroTzOffsetHrs,
       "wtWebGraphThermHygroTzOffsetMin": wtWebGraphThermHygroTzOffsetMin,
       "wtWebGraphThermHygroTzEnable": wtWebGraphThermHygroTzEnable,
       "wtWebGraphThermHygroStTzOffsetHrs": wtWebGraphThermHygroStTzOffsetHrs,
       "wtWebGraphThermHygroStTzOffsetMin": wtWebGraphThermHygroStTzOffsetMin,
       "wtWebGraphThermHygroStTzEnable": wtWebGraphThermHygroStTzEnable,
       "wtWebGraphThermHygroStTzStartMonth": wtWebGraphThermHygroStTzStartMonth,
       "wtWebGraphThermHygroStTzStartMode": wtWebGraphThermHygroStTzStartMode,
       "wtWebGraphThermHygroStTzStartWday": wtWebGraphThermHygroStTzStartWday,
       "wtWebGraphThermHygroStTzStartHrs": wtWebGraphThermHygroStTzStartHrs,
       "wtWebGraphThermHygroStTzStartMin": wtWebGraphThermHygroStTzStartMin,
       "wtWebGraphThermHygroStTzStopMonth": wtWebGraphThermHygroStTzStopMonth,
       "wtWebGraphThermHygroStTzStopMode": wtWebGraphThermHygroStTzStopMode,
       "wtWebGraphThermHygroStTzStopWday": wtWebGraphThermHygroStTzStopWday,
       "wtWebGraphThermHygroStTzStopHrs": wtWebGraphThermHygroStTzStopHrs,
       "wtWebGraphThermHygroStTzStopMin": wtWebGraphThermHygroStTzStopMin,
       "wtWebGraphThermHygroTimeServer": wtWebGraphThermHygroTimeServer,
       "wtWebGraphThermHygroTimeServer1": wtWebGraphThermHygroTimeServer1,
       "wtWebGraphThermHygroTimeServer2": wtWebGraphThermHygroTimeServer2,
       "wtWebGraphThermHygroTsEnable": wtWebGraphThermHygroTsEnable,
       "wtWebGraphThermHygroTsSyncTime": wtWebGraphThermHygroTsSyncTime,
       "wtWebGraphThermHygroDeviceClock": wtWebGraphThermHygroDeviceClock,
       "wtWebGraphThermHygroClockHrs": wtWebGraphThermHygroClockHrs,
       "wtWebGraphThermHygroClockMin": wtWebGraphThermHygroClockMin,
       "wtWebGraphThermHygroClockDay": wtWebGraphThermHygroClockDay,
       "wtWebGraphThermHygroClockMonth": wtWebGraphThermHygroClockMonth,
       "wtWebGraphThermHygroClockYear": wtWebGraphThermHygroClockYear,
       "wtWebGraphThermHygroBasic": wtWebGraphThermHygroBasic,
       "wtWebGraphThermHygroNetwork": wtWebGraphThermHygroNetwork,
       "wtWebGraphThermHygroIpAddress": wtWebGraphThermHygroIpAddress,
       "wtWebGraphThermHygroSubnetMask": wtWebGraphThermHygroSubnetMask,
       "wtWebGraphThermHygroGateway": wtWebGraphThermHygroGateway,
       "wtWebGraphThermHygroDnsServer1": wtWebGraphThermHygroDnsServer1,
       "wtWebGraphThermHygroDnsServer2": wtWebGraphThermHygroDnsServer2,
       "wtWebGraphThermHygroAddConfig": wtWebGraphThermHygroAddConfig,
       "wtWebGraphThermHygroHTTP": wtWebGraphThermHygroHTTP,
       "wtWebGraphThermHygroStartup": wtWebGraphThermHygroStartup,
       "wtWebGraphThermHygroGetHeaderEnable": wtWebGraphThermHygroGetHeaderEnable,
       "wtWebGraphThermHygroHttpPort": wtWebGraphThermHygroHttpPort,
       "wtWebGraphThermHygroMail": wtWebGraphThermHygroMail,
       "wtWebGraphThermHygroMailAdName": wtWebGraphThermHygroMailAdName,
       "wtWebGraphThermHygroMailReply": wtWebGraphThermHygroMailReply,
       "wtWebGraphThermHygroMailServer": wtWebGraphThermHygroMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphThermHygroMailAuthentication": wtWebGraphThermHygroMailAuthentication,
       "wtWebGraphThermHygroMailAuthUser": wtWebGraphThermHygroMailAuthUser,
       "wtWebGraphThermHygroMailAuthPassword": wtWebGraphThermHygroMailAuthPassword,
       "wtWebGraphThermHygroMailPop3Server": wtWebGraphThermHygroMailPop3Server,
       "wtWebGraphThermHygroSNMP": wtWebGraphThermHygroSNMP,
       "wtWebGraphThermHygroSnmpCommunityStringRead": wtWebGraphThermHygroSnmpCommunityStringRead,
       "wtWebGraphThermHygroSnmpCommunityStringReadWrite": wtWebGraphThermHygroSnmpCommunityStringReadWrite,
       "wtWebGraphThermHygroSystemTrapManagerIP": wtWebGraphThermHygroSystemTrapManagerIP,
       "wtWebGraphThermHygroSystemTrapEnable": wtWebGraphThermHygroSystemTrapEnable,
       "wtWebGraphThermHygroSnmpEnable": wtWebGraphThermHygroSnmpEnable,
       "wtWebGraphThermHygroSnmpCommunityStringTrap": wtWebGraphThermHygroSnmpCommunityStringTrap,
       "wtWebGraphThermHygroUDP": wtWebGraphThermHygroUDP,
       "wtWebGraphThermHygroUdpPort": wtWebGraphThermHygroUdpPort,
       "wtWebGraphThermHygroUdpEnable": wtWebGraphThermHygroUdpEnable,
       "wtWebGraphThermHygroSyslog": wtWebGraphThermHygroSyslog,
       "wtWebGraphThermHygroSyslogServerIP": wtWebGraphThermHygroSyslogServerIP,
       "wtWebGraphThermHygroSyslogServerPort": wtWebGraphThermHygroSyslogServerPort,
       "wtWebGraphThermHygroSyslogSystemMessagesEnable": wtWebGraphThermHygroSyslogSystemMessagesEnable,
       "wtWebGraphThermHygroSyslogEnable": wtWebGraphThermHygroSyslogEnable,
       "wtWebGraphThermHygroFTP": wtWebGraphThermHygroFTP,
       "wtWebGraphThermHygroFTPServerIP": wtWebGraphThermHygroFTPServerIP,
       "wtWebGraphThermHygroFTPServerControlPort": wtWebGraphThermHygroFTPServerControlPort,
       "wtWebGraphThermHygroFTPUserName": wtWebGraphThermHygroFTPUserName,
       "wtWebGraphThermHygroFTPPassword": wtWebGraphThermHygroFTPPassword,
       "wtWebGraphThermHygroFTPAccount": wtWebGraphThermHygroFTPAccount,
       "wtWebGraphThermHygroFTPOption": wtWebGraphThermHygroFTPOption,
       "wtWebGraphThermHygroFTPEnable": wtWebGraphThermHygroFTPEnable,
       "wtWebGraphThermHygroDatalogger": wtWebGraphThermHygroDatalogger,
       "wtWebGraphThermHygroLoggerTimebase": wtWebGraphThermHygroLoggerTimebase,
       "wtWebGraphThermHygroLoggerSensorSel": wtWebGraphThermHygroLoggerSensorSel,
       "wtWebGraphThermHygroDisplaySensorSel": wtWebGraphThermHygroDisplaySensorSel,
       "wtWebGraphThermHygroSensorColorTable": wtWebGraphThermHygroSensorColorTable,
       "wtWebGraphThermHygroSensorColorEntry": wtWebGraphThermHygroSensorColorEntry,
       "wtWebGraphThermHygroSensorColor": wtWebGraphThermHygroSensorColor,
       "wtWebGraphThermHygroAutoScaleEnable": wtWebGraphThermHygroAutoScaleEnable,
       "wtWebGraphThermHygroVerticalUpperLimit": wtWebGraphThermHygroVerticalUpperLimit,
       "wtWebGraphThermHygroVerticalLowerLimit": wtWebGraphThermHygroVerticalLowerLimit,
       "wtWebGraphThermHygroHorizontalZoom": wtWebGraphThermHygroHorizontalZoom,
       "wtWebGraphThermHygroAlarm": wtWebGraphThermHygroAlarm,
       "wtWebGraphThermHygroAlarmCount": wtWebGraphThermHygroAlarmCount,
       "wtWebGraphThermHygroAlarmIfTable": wtWebGraphThermHygroAlarmIfTable,
       "wtWebGraphThermHygroAlarmIfEntry": wtWebGraphThermHygroAlarmIfEntry,
       "wtWebGraphThermHygroAlarmNo": wtWebGraphThermHygroAlarmNo,
       "wtWebGraphThermHygroAlarmTable": wtWebGraphThermHygroAlarmTable,
       "wtWebGraphThermHygroAlarmEntry": wtWebGraphThermHygroAlarmEntry,
       "wtWebGraphThermHygroAlarmTrigger": wtWebGraphThermHygroAlarmTrigger,
       "wtWebGraphThermHygroAlarmMin": wtWebGraphThermHygroAlarmMin,
       "wtWebGraphThermHygroAlarmMax": wtWebGraphThermHygroAlarmMax,
       "wtWebGraphThermHygroAlarmHysteresis": wtWebGraphThermHygroAlarmHysteresis,
       "wtWebGraphThermHygroAlarmDelay": wtWebGraphThermHygroAlarmDelay,
       "wtWebGraphThermHygroAlarmInterval": wtWebGraphThermHygroAlarmInterval,
       "wtWebGraphThermHygroAlarmEnable": wtWebGraphThermHygroAlarmEnable,
       "wtWebGraphThermHygroAlarmEMailAddr": wtWebGraphThermHygroAlarmEMailAddr,
       "wtWebGraphThermHygroAlarmMailSubject": wtWebGraphThermHygroAlarmMailSubject,
       "wtWebGraphThermHygroAlarmMailText": wtWebGraphThermHygroAlarmMailText,
       "wtWebGraphThermHygroAlarmManagerIP": wtWebGraphThermHygroAlarmManagerIP,
       "wtWebGraphThermHygroAlarmTrapText": wtWebGraphThermHygroAlarmTrapText,
       "wtWebGraphThermHygroAlarmMailOptions": wtWebGraphThermHygroAlarmMailOptions,
       "wtWebGraphThermHygroAlarmTcpIpAddr": wtWebGraphThermHygroAlarmTcpIpAddr,
       "wtWebGraphThermHygroAlarmTcpPort": wtWebGraphThermHygroAlarmTcpPort,
       "wtWebGraphThermHygroAlarmTcpText": wtWebGraphThermHygroAlarmTcpText,
       "wtWebGraphThermHygroAlarmClearMailSubject": wtWebGraphThermHygroAlarmClearMailSubject,
       "wtWebGraphThermHygroAlarmClearMailText": wtWebGraphThermHygroAlarmClearMailText,
       "wtWebGraphThermHygroAlarmClearTrapText": wtWebGraphThermHygroAlarmClearTrapText,
       "wtWebGraphThermHygroAlarmClearTcpText": wtWebGraphThermHygroAlarmClearTcpText,
       "wtWebGraphThermHygroAlarmDeltaTemp": wtWebGraphThermHygroAlarmDeltaTemp,
       "wtWebGraphThermHygroAlarmRHMin": wtWebGraphThermHygroAlarmRHMin,
       "wtWebGraphThermHygroAlarmRHMax": wtWebGraphThermHygroAlarmRHMax,
       "wtWebGraphThermHygroAlarmRHHysteresis": wtWebGraphThermHygroAlarmRHHysteresis,
       "wtWebGraphThermHygroAlarmAHMin": wtWebGraphThermHygroAlarmAHMin,
       "wtWebGraphThermHygroAlarmAHMax": wtWebGraphThermHygroAlarmAHMax,
       "wtWebGraphThermHygroAlarmSyslogIpAddr": wtWebGraphThermHygroAlarmSyslogIpAddr,
       "wtWebGraphThermHygroAlarmSyslogPort": wtWebGraphThermHygroAlarmSyslogPort,
       "wtWebGraphThermHygroAlarmSyslogText": wtWebGraphThermHygroAlarmSyslogText,
       "wtWebGraphThermHygroAlarmSyslogClearText": wtWebGraphThermHygroAlarmSyslogClearText,
       "wtWebGraphThermHygroAlarmFtpDataPort": wtWebGraphThermHygroAlarmFtpDataPort,
       "wtWebGraphThermHygroAlarmFtpFileName": wtWebGraphThermHygroAlarmFtpFileName,
       "wtWebGraphThermHygroAlarmFtpText": wtWebGraphThermHygroAlarmFtpText,
       "wtWebGraphThermHygroAlarmFtpClearText": wtWebGraphThermHygroAlarmFtpClearText,
       "wtWebGraphThermHygroAlarmFtpOptions": wtWebGraphThermHygroAlarmFtpOptions,
       "wtWebGraphThermHygroAlarmTimerCron": wtWebGraphThermHygroAlarmTimerCron,
       "wtWebGraphThermHygroPorts": wtWebGraphThermHygroPorts,
       "wtWebGraphThermHygroPortTable": wtWebGraphThermHygroPortTable,
       "wtWebGraphThermHygroPortEntry": wtWebGraphThermHygroPortEntry,
       "wtWebGraphThermHygroPortName": wtWebGraphThermHygroPortName,
       "wtWebGraphThermHygroPortText": wtWebGraphThermHygroPortText,
       "wtWebGraphThermHygroPortOffset1": wtWebGraphThermHygroPortOffset1,
       "wtWebGraphThermHygroPortTemperature1": wtWebGraphThermHygroPortTemperature1,
       "wtWebGraphThermHygroPortOffset2": wtWebGraphThermHygroPortOffset2,
       "wtWebGraphThermHygroPortTemperature2": wtWebGraphThermHygroPortTemperature2,
       "wtWebGraphThermHygroPortComment": wtWebGraphThermHygroPortComment,
       "wtWebGraphThermHygroPortSensorSelect": wtWebGraphThermHygroPortSensorSelect,
       "wtWebGraphThermHygroManufact": wtWebGraphThermHygroManufact,
       "wtWebGraphThermHygroMfName": wtWebGraphThermHygroMfName,
       "wtWebGraphThermHygroMfAddr": wtWebGraphThermHygroMfAddr,
       "wtWebGraphThermHygroMfHotline": wtWebGraphThermHygroMfHotline,
       "wtWebGraphThermHygroMfInternet": wtWebGraphThermHygroMfInternet,
       "wtWebGraphThermHygroMfDeviceTyp": wtWebGraphThermHygroMfDeviceTyp,
       "wtWebGraphThermHygroMfOrderNo": wtWebGraphThermHygroMfOrderNo,
       "wtWebGraphThermHygroDiag": wtWebGraphThermHygroDiag,
       "wtWebGraphThermHygroDiagErrorCount": wtWebGraphThermHygroDiagErrorCount,
       "wtWebGraphThermHygroDiagBinaryError": wtWebGraphThermHygroDiagBinaryError,
       "wtWebGraphThermHygroDiagErrorIndex": wtWebGraphThermHygroDiagErrorIndex,
       "wtWebGraphThermHygroDiagErrorMessage": wtWebGraphThermHygroDiagErrorMessage,
       "wtWebGraphThermHygroDiagErrorClear": wtWebGraphThermHygroDiagErrorClear}
)
