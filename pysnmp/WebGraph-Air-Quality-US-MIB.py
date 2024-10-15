# SNMP MIB module (WebGraph-Air-Quality-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-Air-Quality-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:33 2024
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
_WtWebGraphAirQuality_ObjectIdentity = ObjectIdentity
wtWebGraphAirQuality = _WtWebGraphAirQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35)
)
_WtWebGraphAirQualityTemp_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityTemp = _WtWebGraphAirQualityTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1)
)


class _WtWebGraphAirQualitySensors_Type(Integer32):
    """Custom type wtWebGraphAirQualitySensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WtWebGraphAirQualitySensors_Type.__name__ = "Integer32"
_WtWebGraphAirQualitySensors_Object = MibScalar
wtWebGraphAirQualitySensors = _WtWebGraphAirQualitySensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 1),
    _WtWebGraphAirQualitySensors_Type()
)
wtWebGraphAirQualitySensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensors.setStatus("mandatory")
_WtWebGraphAirQualitySensorTable_Object = MibTable
wtWebGraphAirQualitySensorTable = _WtWebGraphAirQualitySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensorTable.setStatus("mandatory")
_WtWebGraphAirQualitySensorEntry_Object = MibTableRow
wtWebGraphAirQualitySensorEntry = _WtWebGraphAirQualitySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 2, 1)
)
wtWebGraphAirQualitySensorEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensorEntry.setStatus("mandatory")


class _WtWebGraphAirQualitySensorNo_Type(Integer32):
    """Custom type wtWebGraphAirQualitySensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphAirQualitySensorNo_Type.__name__ = "Integer32"
_WtWebGraphAirQualitySensorNo_Object = MibTableColumn
wtWebGraphAirQualitySensorNo = _WtWebGraphAirQualitySensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 2, 1, 1),
    _WtWebGraphAirQualitySensorNo_Type()
)
wtWebGraphAirQualitySensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensorNo.setStatus("mandatory")
_WtWebGraphAirQualityTempValueTable_Object = MibTable
wtWebGraphAirQualityTempValueTable = _WtWebGraphAirQualityTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValueTable.setStatus("mandatory")
_WtWebGraphAirQualityTempValueEntry_Object = MibTableRow
wtWebGraphAirQualityTempValueEntry = _WtWebGraphAirQualityTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 3, 1)
)
wtWebGraphAirQualityTempValueEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValueEntry.setStatus("mandatory")


class _WtWebGraphAirQualityTempValue_Type(OctetString):
    """Custom type wtWebGraphAirQualityTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAirQualityTempValue_Type.__name__ = "OctetString"
_WtWebGraphAirQualityTempValue_Object = MibTableColumn
wtWebGraphAirQualityTempValue = _WtWebGraphAirQualityTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 3, 1, 1),
    _WtWebGraphAirQualityTempValue_Type()
)
wtWebGraphAirQualityTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValue.setStatus("mandatory")
_WtWebGraphAirQualityBinaryTempValueTable_Object = MibTable
wtWebGraphAirQualityBinaryTempValueTable = _WtWebGraphAirQualityBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityBinaryTempValueTable.setStatus("mandatory")
_WtWebGraphAirQualityBinaryTempValueEntry_Object = MibTableRow
wtWebGraphAirQualityBinaryTempValueEntry = _WtWebGraphAirQualityBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 4, 1)
)
wtWebGraphAirQualityBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityBinaryTempValueEntry.setStatus("mandatory")
_WtWebGraphAirQualityBinaryTempValue_Type = Integer32
_WtWebGraphAirQualityBinaryTempValue_Object = MibTableColumn
wtWebGraphAirQualityBinaryTempValue = _WtWebGraphAirQualityBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 4, 1, 1),
    _WtWebGraphAirQualityBinaryTempValue_Type()
)
wtWebGraphAirQualityBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityBinaryTempValue.setStatus("mandatory")
_WtWebGraphAirQualityTempValuePktTable_Object = MibTable
wtWebGraphAirQualityTempValuePktTable = _WtWebGraphAirQualityTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValuePktTable.setStatus("mandatory")
_WtWebGraphAirQualityTempValuePktEntry_Object = MibTableRow
wtWebGraphAirQualityTempValuePktEntry = _WtWebGraphAirQualityTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 8, 1)
)
wtWebGraphAirQualityTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValuePktEntry.setStatus("mandatory")


class _WtWebGraphAirQualityTempValuePkt_Type(OctetString):
    """Custom type wtWebGraphAirQualityTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebGraphAirQualityTempValuePkt_Type.__name__ = "OctetString"
_WtWebGraphAirQualityTempValuePkt_Object = MibTableColumn
wtWebGraphAirQualityTempValuePkt = _WtWebGraphAirQualityTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 1, 8, 1, 1),
    _WtWebGraphAirQualityTempValuePkt_Type()
)
wtWebGraphAirQualityTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTempValuePkt.setStatus("mandatory")
_WtWebGraphAirQualitySessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualitySessCntrl = _WtWebGraphAirQualitySessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2)
)
_WtWebGraphAirQualitySessCntrlPassword_Type = OctetString
_WtWebGraphAirQualitySessCntrlPassword_Object = MibScalar
wtWebGraphAirQualitySessCntrlPassword = _WtWebGraphAirQualitySessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2, 1),
    _WtWebGraphAirQualitySessCntrlPassword_Type()
)
wtWebGraphAirQualitySessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySessCntrlPassword.setStatus("mandatory")


class _WtWebGraphAirQualitySessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphAirQualitySessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphAirQualitySessCntrl-NoSession", 0),
          ("wtWebGraphAirQualitySessCntrl-Session", 1))
    )


_WtWebGraphAirQualitySessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphAirQualitySessCntrlConfigMode_Object = MibScalar
wtWebGraphAirQualitySessCntrlConfigMode = _WtWebGraphAirQualitySessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2, 2),
    _WtWebGraphAirQualitySessCntrlConfigMode_Type()
)
wtWebGraphAirQualitySessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphAirQualitySessCntrlLogout_Type = Integer32
_WtWebGraphAirQualitySessCntrlLogout_Object = MibScalar
wtWebGraphAirQualitySessCntrlLogout = _WtWebGraphAirQualitySessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2, 3),
    _WtWebGraphAirQualitySessCntrlLogout_Type()
)
wtWebGraphAirQualitySessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySessCntrlLogout.setStatus("mandatory")
_WtWebGraphAirQualitySessCntrlAdminPassword_Type = OctetString
_WtWebGraphAirQualitySessCntrlAdminPassword_Object = MibScalar
wtWebGraphAirQualitySessCntrlAdminPassword = _WtWebGraphAirQualitySessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2, 4),
    _WtWebGraphAirQualitySessCntrlAdminPassword_Type()
)
wtWebGraphAirQualitySessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphAirQualitySessCntrlConfigPassword_Type = OctetString
_WtWebGraphAirQualitySessCntrlConfigPassword_Object = MibScalar
wtWebGraphAirQualitySessCntrlConfigPassword = _WtWebGraphAirQualitySessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 2, 5),
    _WtWebGraphAirQualitySessCntrlConfigPassword_Type()
)
wtWebGraphAirQualitySessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphAirQualityConfig_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityConfig = _WtWebGraphAirQualityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3)
)
_WtWebGraphAirQualityDevice_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityDevice = _WtWebGraphAirQualityDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1)
)
_WtWebGraphAirQualityText_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityText = _WtWebGraphAirQualityText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 1)
)
_WtWebGraphAirQualityDeviceName_Type = OctetString
_WtWebGraphAirQualityDeviceName_Object = MibScalar
wtWebGraphAirQualityDeviceName = _WtWebGraphAirQualityDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 1, 1),
    _WtWebGraphAirQualityDeviceName_Type()
)
wtWebGraphAirQualityDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDeviceName.setStatus("mandatory")
_WtWebGraphAirQualityDeviceText_Type = OctetString
_WtWebGraphAirQualityDeviceText_Object = MibScalar
wtWebGraphAirQualityDeviceText = _WtWebGraphAirQualityDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 1, 2),
    _WtWebGraphAirQualityDeviceText_Type()
)
wtWebGraphAirQualityDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDeviceText.setStatus("mandatory")
_WtWebGraphAirQualityDeviceLocation_Type = OctetString
_WtWebGraphAirQualityDeviceLocation_Object = MibScalar
wtWebGraphAirQualityDeviceLocation = _WtWebGraphAirQualityDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 1, 3),
    _WtWebGraphAirQualityDeviceLocation_Type()
)
wtWebGraphAirQualityDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDeviceLocation.setStatus("mandatory")
_WtWebGraphAirQualityDeviceContact_Type = OctetString
_WtWebGraphAirQualityDeviceContact_Object = MibScalar
wtWebGraphAirQualityDeviceContact = _WtWebGraphAirQualityDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 1, 4),
    _WtWebGraphAirQualityDeviceContact_Type()
)
wtWebGraphAirQualityDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDeviceContact.setStatus("mandatory")
_WtWebGraphAirQualityTimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityTimeDate = _WtWebGraphAirQualityTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2)
)
_WtWebGraphAirQualityTimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityTimeZone = _WtWebGraphAirQualityTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1)
)
_WtWebGraphAirQualityTzOffsetHrs_Type = Integer32
_WtWebGraphAirQualityTzOffsetHrs_Object = MibScalar
wtWebGraphAirQualityTzOffsetHrs = _WtWebGraphAirQualityTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 1),
    _WtWebGraphAirQualityTzOffsetHrs_Type()
)
wtWebGraphAirQualityTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAirQualityTzOffsetMin_Type = Integer32
_WtWebGraphAirQualityTzOffsetMin_Object = MibScalar
wtWebGraphAirQualityTzOffsetMin = _WtWebGraphAirQualityTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 2),
    _WtWebGraphAirQualityTzOffsetMin_Type()
)
wtWebGraphAirQualityTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAirQualityTzEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualityTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualityTzEnable_Object = MibScalar
wtWebGraphAirQualityTzEnable = _WtWebGraphAirQualityTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 3),
    _WtWebGraphAirQualityTzEnable_Type()
)
wtWebGraphAirQualityTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTzEnable.setStatus("mandatory")
_WtWebGraphAirQualityStTzOffsetHrs_Type = Integer32
_WtWebGraphAirQualityStTzOffsetHrs_Object = MibScalar
wtWebGraphAirQualityStTzOffsetHrs = _WtWebGraphAirQualityStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 4),
    _WtWebGraphAirQualityStTzOffsetHrs_Type()
)
wtWebGraphAirQualityStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzOffsetHrs.setStatus("mandatory")
_WtWebGraphAirQualityStTzOffsetMin_Type = Integer32
_WtWebGraphAirQualityStTzOffsetMin_Object = MibScalar
wtWebGraphAirQualityStTzOffsetMin = _WtWebGraphAirQualityStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 5),
    _WtWebGraphAirQualityStTzOffsetMin_Type()
)
wtWebGraphAirQualityStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzOffsetMin.setStatus("mandatory")


class _WtWebGraphAirQualityStTzEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualityStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityStTzEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualityStTzEnable_Object = MibScalar
wtWebGraphAirQualityStTzEnable = _WtWebGraphAirQualityStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 6),
    _WtWebGraphAirQualityStTzEnable_Type()
)
wtWebGraphAirQualityStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzEnable.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStartMonth based on Integer32"""
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
        *(("wtWebGraphAirQualityStartMonth-April", 4),
          ("wtWebGraphAirQualityStartMonth-August", 8),
          ("wtWebGraphAirQualityStartMonth-December", 12),
          ("wtWebGraphAirQualityStartMonth-February", 2),
          ("wtWebGraphAirQualityStartMonth-January", 1),
          ("wtWebGraphAirQualityStartMonth-July", 7),
          ("wtWebGraphAirQualityStartMonth-June", 6),
          ("wtWebGraphAirQualityStartMonth-March", 3),
          ("wtWebGraphAirQualityStartMonth-May", 5),
          ("wtWebGraphAirQualityStartMonth-November", 11),
          ("wtWebGraphAirQualityStartMonth-October", 10),
          ("wtWebGraphAirQualityStartMonth-September", 9))
    )


_WtWebGraphAirQualityStTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStartMonth_Object = MibScalar
wtWebGraphAirQualityStTzStartMonth = _WtWebGraphAirQualityStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 7),
    _WtWebGraphAirQualityStTzStartMonth_Type()
)
wtWebGraphAirQualityStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStartMonth.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStartMode_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStartMode based on Integer32"""
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
        *(("wtWebGraphAirQualityStartMode-first", 1),
          ("wtWebGraphAirQualityStartMode-fourth", 4),
          ("wtWebGraphAirQualityStartMode-last", 5),
          ("wtWebGraphAirQualityStartMode-second", 2),
          ("wtWebGraphAirQualityStartMode-third", 3))
    )


_WtWebGraphAirQualityStTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStartMode_Object = MibScalar
wtWebGraphAirQualityStTzStartMode = _WtWebGraphAirQualityStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 8),
    _WtWebGraphAirQualityStTzStartMode_Type()
)
wtWebGraphAirQualityStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStartMode.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStartWday_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStartWday based on Integer32"""
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
        *(("wtWebGraphAirQualityStartWday-Friday", 6),
          ("wtWebGraphAirQualityStartWday-Monday", 2),
          ("wtWebGraphAirQualityStartWday-Saturday", 7),
          ("wtWebGraphAirQualityStartWday-Sunday", 1),
          ("wtWebGraphAirQualityStartWday-Thursday", 4),
          ("wtWebGraphAirQualityStartWday-Tuesday", 3),
          ("wtWebGraphAirQualityStartWday-Wednesday", 5))
    )


_WtWebGraphAirQualityStTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStartWday_Object = MibScalar
wtWebGraphAirQualityStTzStartWday = _WtWebGraphAirQualityStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 9),
    _WtWebGraphAirQualityStTzStartWday_Type()
)
wtWebGraphAirQualityStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStartWday.setStatus("mandatory")
_WtWebGraphAirQualityStTzStartHrs_Type = Integer32
_WtWebGraphAirQualityStTzStartHrs_Object = MibScalar
wtWebGraphAirQualityStTzStartHrs = _WtWebGraphAirQualityStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 10),
    _WtWebGraphAirQualityStTzStartHrs_Type()
)
wtWebGraphAirQualityStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStartHrs.setStatus("mandatory")
_WtWebGraphAirQualityStTzStartMin_Type = Integer32
_WtWebGraphAirQualityStTzStartMin_Object = MibScalar
wtWebGraphAirQualityStTzStartMin = _WtWebGraphAirQualityStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 11),
    _WtWebGraphAirQualityStTzStartMin_Type()
)
wtWebGraphAirQualityStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStartMin.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStopMonth based on Integer32"""
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
        *(("wtWebGraphAirQualityStopMonth-April", 4),
          ("wtWebGraphAirQualityStopMonth-August", 8),
          ("wtWebGraphAirQualityStopMonth-December", 12),
          ("wtWebGraphAirQualityStopMonth-February", 2),
          ("wtWebGraphAirQualityStopMonth-January", 1),
          ("wtWebGraphAirQualityStopMonth-July", 7),
          ("wtWebGraphAirQualityStopMonth-June", 6),
          ("wtWebGraphAirQualityStopMonth-March", 3),
          ("wtWebGraphAirQualityStopMonth-May", 5),
          ("wtWebGraphAirQualityStopMonth-November", 11),
          ("wtWebGraphAirQualityStopMonth-October", 10),
          ("wtWebGraphAirQualityStopMonth-September", 9))
    )


_WtWebGraphAirQualityStTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStopMonth_Object = MibScalar
wtWebGraphAirQualityStTzStopMonth = _WtWebGraphAirQualityStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 12),
    _WtWebGraphAirQualityStTzStopMonth_Type()
)
wtWebGraphAirQualityStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStopMonth.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStopMode_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStopMode based on Integer32"""
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
        *(("wtWebGraphAirQualityStopMode-first", 1),
          ("wtWebGraphAirQualityStopMode-fourth", 4),
          ("wtWebGraphAirQualityStopMode-last", 5),
          ("wtWebGraphAirQualityStopMode-second", 2),
          ("wtWebGraphAirQualityStopMode-third", 3))
    )


_WtWebGraphAirQualityStTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStopMode_Object = MibScalar
wtWebGraphAirQualityStTzStopMode = _WtWebGraphAirQualityStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 13),
    _WtWebGraphAirQualityStTzStopMode_Type()
)
wtWebGraphAirQualityStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStopMode.setStatus("mandatory")


class _WtWebGraphAirQualityStTzStopWday_Type(Integer32):
    """Custom type wtWebGraphAirQualityStTzStopWday based on Integer32"""
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
        *(("wtWebGraphAirQualityStopWday-Friday", 6),
          ("wtWebGraphAirQualityStopWday-Monday", 2),
          ("wtWebGraphAirQualityStopWday-Saturday", 7),
          ("wtWebGraphAirQualityStopWday-Sunday", 1),
          ("wtWebGraphAirQualityStopWday-Thursday", 4),
          ("wtWebGraphAirQualityStopWday-Tuesday", 3),
          ("wtWebGraphAirQualityStopWday-Wednesday", 5))
    )


_WtWebGraphAirQualityStTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphAirQualityStTzStopWday_Object = MibScalar
wtWebGraphAirQualityStTzStopWday = _WtWebGraphAirQualityStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 14),
    _WtWebGraphAirQualityStTzStopWday_Type()
)
wtWebGraphAirQualityStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStopWday.setStatus("mandatory")
_WtWebGraphAirQualityStTzStopHrs_Type = Integer32
_WtWebGraphAirQualityStTzStopHrs_Object = MibScalar
wtWebGraphAirQualityStTzStopHrs = _WtWebGraphAirQualityStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 15),
    _WtWebGraphAirQualityStTzStopHrs_Type()
)
wtWebGraphAirQualityStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStopHrs.setStatus("mandatory")
_WtWebGraphAirQualityStTzStopMin_Type = Integer32
_WtWebGraphAirQualityStTzStopMin_Object = MibScalar
wtWebGraphAirQualityStTzStopMin = _WtWebGraphAirQualityStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 1, 16),
    _WtWebGraphAirQualityStTzStopMin_Type()
)
wtWebGraphAirQualityStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStTzStopMin.setStatus("mandatory")
_WtWebGraphAirQualityTimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityTimeServer = _WtWebGraphAirQualityTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 2)
)
_WtWebGraphAirQualityTimeServer1_Type = OctetString
_WtWebGraphAirQualityTimeServer1_Object = MibScalar
wtWebGraphAirQualityTimeServer1 = _WtWebGraphAirQualityTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 2, 1),
    _WtWebGraphAirQualityTimeServer1_Type()
)
wtWebGraphAirQualityTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTimeServer1.setStatus("mandatory")
_WtWebGraphAirQualityTimeServer2_Type = OctetString
_WtWebGraphAirQualityTimeServer2_Object = MibScalar
wtWebGraphAirQualityTimeServer2 = _WtWebGraphAirQualityTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 2, 2),
    _WtWebGraphAirQualityTimeServer2_Type()
)
wtWebGraphAirQualityTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTimeServer2.setStatus("mandatory")


class _WtWebGraphAirQualityTsEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualityTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityTsEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualityTsEnable_Object = MibScalar
wtWebGraphAirQualityTsEnable = _WtWebGraphAirQualityTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 2, 3),
    _WtWebGraphAirQualityTsEnable_Type()
)
wtWebGraphAirQualityTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTsEnable.setStatus("mandatory")
_WtWebGraphAirQualityTsSyncTime_Type = Integer32
_WtWebGraphAirQualityTsSyncTime_Object = MibScalar
wtWebGraphAirQualityTsSyncTime = _WtWebGraphAirQualityTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 2, 4),
    _WtWebGraphAirQualityTsSyncTime_Type()
)
wtWebGraphAirQualityTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityTsSyncTime.setStatus("mandatory")
_WtWebGraphAirQualityDeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityDeviceClock = _WtWebGraphAirQualityDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3)
)


class _WtWebGraphAirQualityClockHrs_Type(Integer32):
    """Custom type wtWebGraphAirQualityClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphAirQualityClockHrs_Type.__name__ = "Integer32"
_WtWebGraphAirQualityClockHrs_Object = MibScalar
wtWebGraphAirQualityClockHrs = _WtWebGraphAirQualityClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3, 1),
    _WtWebGraphAirQualityClockHrs_Type()
)
wtWebGraphAirQualityClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityClockHrs.setStatus("mandatory")


class _WtWebGraphAirQualityClockMin_Type(Integer32):
    """Custom type wtWebGraphAirQualityClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphAirQualityClockMin_Type.__name__ = "Integer32"
_WtWebGraphAirQualityClockMin_Object = MibScalar
wtWebGraphAirQualityClockMin = _WtWebGraphAirQualityClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3, 2),
    _WtWebGraphAirQualityClockMin_Type()
)
wtWebGraphAirQualityClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityClockMin.setStatus("mandatory")


class _WtWebGraphAirQualityClockDay_Type(Integer32):
    """Custom type wtWebGraphAirQualityClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphAirQualityClockDay_Type.__name__ = "Integer32"
_WtWebGraphAirQualityClockDay_Object = MibScalar
wtWebGraphAirQualityClockDay = _WtWebGraphAirQualityClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3, 3),
    _WtWebGraphAirQualityClockDay_Type()
)
wtWebGraphAirQualityClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityClockDay.setStatus("mandatory")


class _WtWebGraphAirQualityClockMonth_Type(Integer32):
    """Custom type wtWebGraphAirQualityClockMonth based on Integer32"""
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
        *(("wtWebGraphAirQualityClockMonth-April", 4),
          ("wtWebGraphAirQualityClockMonth-August", 8),
          ("wtWebGraphAirQualityClockMonth-December", 12),
          ("wtWebGraphAirQualityClockMonth-February", 2),
          ("wtWebGraphAirQualityClockMonth-January", 1),
          ("wtWebGraphAirQualityClockMonth-July", 7),
          ("wtWebGraphAirQualityClockMonth-June", 6),
          ("wtWebGraphAirQualityClockMonth-March", 3),
          ("wtWebGraphAirQualityClockMonth-May", 5),
          ("wtWebGraphAirQualityClockMonth-November", 11),
          ("wtWebGraphAirQualityClockMonth-October", 10),
          ("wtWebGraphAirQualityClockMonth-September", 9))
    )


_WtWebGraphAirQualityClockMonth_Type.__name__ = "Integer32"
_WtWebGraphAirQualityClockMonth_Object = MibScalar
wtWebGraphAirQualityClockMonth = _WtWebGraphAirQualityClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3, 4),
    _WtWebGraphAirQualityClockMonth_Type()
)
wtWebGraphAirQualityClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityClockMonth.setStatus("mandatory")


class _WtWebGraphAirQualityClockYear_Type(Integer32):
    """Custom type wtWebGraphAirQualityClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphAirQualityClockYear_Type.__name__ = "Integer32"
_WtWebGraphAirQualityClockYear_Object = MibScalar
wtWebGraphAirQualityClockYear = _WtWebGraphAirQualityClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 2, 3, 5),
    _WtWebGraphAirQualityClockYear_Type()
)
wtWebGraphAirQualityClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityClockYear.setStatus("mandatory")
_WtWebGraphAirQualityBasic_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityBasic = _WtWebGraphAirQualityBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3)
)
_WtWebGraphAirQualityNetwork_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityNetwork = _WtWebGraphAirQualityNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1)
)
_WtWebGraphAirQualityIpAddress_Type = IpAddress
_WtWebGraphAirQualityIpAddress_Object = MibScalar
wtWebGraphAirQualityIpAddress = _WtWebGraphAirQualityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 1),
    _WtWebGraphAirQualityIpAddress_Type()
)
wtWebGraphAirQualityIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityIpAddress.setStatus("mandatory")
_WtWebGraphAirQualitySubnetMask_Type = IpAddress
_WtWebGraphAirQualitySubnetMask_Object = MibScalar
wtWebGraphAirQualitySubnetMask = _WtWebGraphAirQualitySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 2),
    _WtWebGraphAirQualitySubnetMask_Type()
)
wtWebGraphAirQualitySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySubnetMask.setStatus("mandatory")
_WtWebGraphAirQualityGateway_Type = IpAddress
_WtWebGraphAirQualityGateway_Object = MibScalar
wtWebGraphAirQualityGateway = _WtWebGraphAirQualityGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 3),
    _WtWebGraphAirQualityGateway_Type()
)
wtWebGraphAirQualityGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGateway.setStatus("mandatory")
_WtWebGraphAirQualityDnsServer1_Type = OctetString
_WtWebGraphAirQualityDnsServer1_Object = MibScalar
wtWebGraphAirQualityDnsServer1 = _WtWebGraphAirQualityDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 4),
    _WtWebGraphAirQualityDnsServer1_Type()
)
wtWebGraphAirQualityDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDnsServer1.setStatus("mandatory")
_WtWebGraphAirQualityDnsServer2_Type = OctetString
_WtWebGraphAirQualityDnsServer2_Object = MibScalar
wtWebGraphAirQualityDnsServer2 = _WtWebGraphAirQualityDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 5),
    _WtWebGraphAirQualityDnsServer2_Type()
)
wtWebGraphAirQualityDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDnsServer2.setStatus("mandatory")
_WtWebGraphAirQualityAddConfig_Type = OctetString
_WtWebGraphAirQualityAddConfig_Object = MibScalar
wtWebGraphAirQualityAddConfig = _WtWebGraphAirQualityAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 1, 6),
    _WtWebGraphAirQualityAddConfig_Type()
)
wtWebGraphAirQualityAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAddConfig.setStatus("mandatory")
_WtWebGraphAirQualityHTTP_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityHTTP = _WtWebGraphAirQualityHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 2)
)
_WtWebGraphAirQualityStartup_Type = OctetString
_WtWebGraphAirQualityStartup_Object = MibScalar
wtWebGraphAirQualityStartup = _WtWebGraphAirQualityStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 2, 1),
    _WtWebGraphAirQualityStartup_Type()
)
wtWebGraphAirQualityStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityStartup.setStatus("mandatory")
_WtWebGraphAirQualityGetHeaderEnable_Type = OctetString
_WtWebGraphAirQualityGetHeaderEnable_Object = MibScalar
wtWebGraphAirQualityGetHeaderEnable = _WtWebGraphAirQualityGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 2, 2),
    _WtWebGraphAirQualityGetHeaderEnable_Type()
)
wtWebGraphAirQualityGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGetHeaderEnable.setStatus("mandatory")


class _WtWebGraphAirQualityHttpPort_Type(Integer32):
    """Custom type wtWebGraphAirQualityHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAirQualityHttpPort_Type.__name__ = "Integer32"
_WtWebGraphAirQualityHttpPort_Object = MibScalar
wtWebGraphAirQualityHttpPort = _WtWebGraphAirQualityHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 2, 3),
    _WtWebGraphAirQualityHttpPort_Type()
)
wtWebGraphAirQualityHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityHttpPort.setStatus("mandatory")
_WtWebGraphAirQualityMail_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityMail = _WtWebGraphAirQualityMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3)
)
_WtWebGraphAirQualityMailAdName_Type = OctetString
_WtWebGraphAirQualityMailAdName_Object = MibScalar
wtWebGraphAirQualityMailAdName = _WtWebGraphAirQualityMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 1),
    _WtWebGraphAirQualityMailAdName_Type()
)
wtWebGraphAirQualityMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailAdName.setStatus("mandatory")
_WtWebGraphAirQualityMailReply_Type = OctetString
_WtWebGraphAirQualityMailReply_Object = MibScalar
wtWebGraphAirQualityMailReply = _WtWebGraphAirQualityMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 2),
    _WtWebGraphAirQualityMailReply_Type()
)
wtWebGraphAirQualityMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailReply.setStatus("mandatory")
_WtWebGraphAirQualityMailServer_Type = OctetString
_WtWebGraphAirQualityMailServer_Object = MibScalar
wtWebGraphAirQualityMailServer = _WtWebGraphAirQualityMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 3),
    _WtWebGraphAirQualityMailServer_Type()
)
wtWebGraphAirQualityMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphAirQualityMailAuthentication_Type(OctetString):
    """Custom type wtWebGraphAirQualityMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityMailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphAirQualityMailAuthentication_Object = MibScalar
wtWebGraphAirQualityMailAuthentication = _WtWebGraphAirQualityMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 5),
    _WtWebGraphAirQualityMailAuthentication_Type()
)
wtWebGraphAirQualityMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailAuthentication.setStatus("mandatory")
_WtWebGraphAirQualityMailAuthUser_Type = OctetString
_WtWebGraphAirQualityMailAuthUser_Object = MibScalar
wtWebGraphAirQualityMailAuthUser = _WtWebGraphAirQualityMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 6),
    _WtWebGraphAirQualityMailAuthUser_Type()
)
wtWebGraphAirQualityMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailAuthUser.setStatus("mandatory")
_WtWebGraphAirQualityMailAuthPassword_Type = OctetString
_WtWebGraphAirQualityMailAuthPassword_Object = MibScalar
wtWebGraphAirQualityMailAuthPassword = _WtWebGraphAirQualityMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 7),
    _WtWebGraphAirQualityMailAuthPassword_Type()
)
wtWebGraphAirQualityMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailAuthPassword.setStatus("mandatory")
_WtWebGraphAirQualityMailPop3Server_Type = OctetString
_WtWebGraphAirQualityMailPop3Server_Object = MibScalar
wtWebGraphAirQualityMailPop3Server = _WtWebGraphAirQualityMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 3, 8),
    _WtWebGraphAirQualityMailPop3Server_Type()
)
wtWebGraphAirQualityMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMailPop3Server.setStatus("mandatory")
_WtWebGraphAirQualitySNMP_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualitySNMP = _WtWebGraphAirQualitySNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4)
)
_WtWebGraphAirQualitySnmpCommunityStringRead_Type = OctetString
_WtWebGraphAirQualitySnmpCommunityStringRead_Object = MibScalar
wtWebGraphAirQualitySnmpCommunityStringRead = _WtWebGraphAirQualitySnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 1),
    _WtWebGraphAirQualitySnmpCommunityStringRead_Type()
)
wtWebGraphAirQualitySnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphAirQualitySnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphAirQualitySnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphAirQualitySnmpCommunityStringReadWrite = _WtWebGraphAirQualitySnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 2),
    _WtWebGraphAirQualitySnmpCommunityStringReadWrite_Type()
)
wtWebGraphAirQualitySnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphAirQualitySystemTrapManagerIP_Type = OctetString
_WtWebGraphAirQualitySystemTrapManagerIP_Object = MibScalar
wtWebGraphAirQualitySystemTrapManagerIP = _WtWebGraphAirQualitySystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 3),
    _WtWebGraphAirQualitySystemTrapManagerIP_Type()
)
wtWebGraphAirQualitySystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphAirQualitySystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualitySystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualitySystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualitySystemTrapEnable_Object = MibScalar
wtWebGraphAirQualitySystemTrapEnable = _WtWebGraphAirQualitySystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 4),
    _WtWebGraphAirQualitySystemTrapEnable_Type()
)
wtWebGraphAirQualitySystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySystemTrapEnable.setStatus("mandatory")
_WtWebGraphAirQualitySnmpEnable_Type = OctetString
_WtWebGraphAirQualitySnmpEnable_Object = MibScalar
wtWebGraphAirQualitySnmpEnable = _WtWebGraphAirQualitySnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 5),
    _WtWebGraphAirQualitySnmpEnable_Type()
)
wtWebGraphAirQualitySnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySnmpEnable.setStatus("mandatory")
_WtWebGraphAirQualitySnmpCommunityStringTrap_Type = OctetString
_WtWebGraphAirQualitySnmpCommunityStringTrap_Object = MibScalar
wtWebGraphAirQualitySnmpCommunityStringTrap = _WtWebGraphAirQualitySnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 4, 6),
    _WtWebGraphAirQualitySnmpCommunityStringTrap_Type()
)
wtWebGraphAirQualitySnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphAirQualityUDP_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityUDP = _WtWebGraphAirQualityUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 5)
)


class _WtWebGraphAirQualityUdpPort_Type(Integer32):
    """Custom type wtWebGraphAirQualityUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAirQualityUdpPort_Type.__name__ = "Integer32"
_WtWebGraphAirQualityUdpPort_Object = MibScalar
wtWebGraphAirQualityUdpPort = _WtWebGraphAirQualityUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 5, 1),
    _WtWebGraphAirQualityUdpPort_Type()
)
wtWebGraphAirQualityUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityUdpPort.setStatus("mandatory")
_WtWebGraphAirQualityUdpEnable_Type = OctetString
_WtWebGraphAirQualityUdpEnable_Object = MibScalar
wtWebGraphAirQualityUdpEnable = _WtWebGraphAirQualityUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 5, 2),
    _WtWebGraphAirQualityUdpEnable_Type()
)
wtWebGraphAirQualityUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityUdpEnable.setStatus("mandatory")
_WtWebGraphAirQualitySyslog_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualitySyslog = _WtWebGraphAirQualitySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 6)
)
_WtWebGraphAirQualitySyslogServerIP_Type = OctetString
_WtWebGraphAirQualitySyslogServerIP_Object = MibScalar
wtWebGraphAirQualitySyslogServerIP = _WtWebGraphAirQualitySyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 6, 1),
    _WtWebGraphAirQualitySyslogServerIP_Type()
)
wtWebGraphAirQualitySyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySyslogServerIP.setStatus("mandatory")
_WtWebGraphAirQualitySyslogServerPort_Type = Integer32
_WtWebGraphAirQualitySyslogServerPort_Object = MibScalar
wtWebGraphAirQualitySyslogServerPort = _WtWebGraphAirQualitySyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 6, 2),
    _WtWebGraphAirQualitySyslogServerPort_Type()
)
wtWebGraphAirQualitySyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySyslogServerPort.setStatus("mandatory")


class _WtWebGraphAirQualitySyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualitySyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualitySyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualitySyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphAirQualitySyslogSystemMessagesEnable = _WtWebGraphAirQualitySyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 6, 3),
    _WtWebGraphAirQualitySyslogSystemMessagesEnable_Type()
)
wtWebGraphAirQualitySyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphAirQualitySyslogEnable_Type = OctetString
_WtWebGraphAirQualitySyslogEnable_Object = MibScalar
wtWebGraphAirQualitySyslogEnable = _WtWebGraphAirQualitySyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 6, 4),
    _WtWebGraphAirQualitySyslogEnable_Type()
)
wtWebGraphAirQualitySyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySyslogEnable.setStatus("mandatory")
_WtWebGraphAirQualityFTP_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityFTP = _WtWebGraphAirQualityFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7)
)
_WtWebGraphAirQualityFTPServerIP_Type = OctetString
_WtWebGraphAirQualityFTPServerIP_Object = MibScalar
wtWebGraphAirQualityFTPServerIP = _WtWebGraphAirQualityFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 1),
    _WtWebGraphAirQualityFTPServerIP_Type()
)
wtWebGraphAirQualityFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPServerIP.setStatus("mandatory")
_WtWebGraphAirQualityFTPServerControlPort_Type = Integer32
_WtWebGraphAirQualityFTPServerControlPort_Object = MibScalar
wtWebGraphAirQualityFTPServerControlPort = _WtWebGraphAirQualityFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 2),
    _WtWebGraphAirQualityFTPServerControlPort_Type()
)
wtWebGraphAirQualityFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPServerControlPort.setStatus("mandatory")
_WtWebGraphAirQualityFTPUserName_Type = OctetString
_WtWebGraphAirQualityFTPUserName_Object = MibScalar
wtWebGraphAirQualityFTPUserName = _WtWebGraphAirQualityFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 3),
    _WtWebGraphAirQualityFTPUserName_Type()
)
wtWebGraphAirQualityFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPUserName.setStatus("mandatory")
_WtWebGraphAirQualityFTPPassword_Type = OctetString
_WtWebGraphAirQualityFTPPassword_Object = MibScalar
wtWebGraphAirQualityFTPPassword = _WtWebGraphAirQualityFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 4),
    _WtWebGraphAirQualityFTPPassword_Type()
)
wtWebGraphAirQualityFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPPassword.setStatus("mandatory")
_WtWebGraphAirQualityFTPAccount_Type = OctetString
_WtWebGraphAirQualityFTPAccount_Object = MibScalar
wtWebGraphAirQualityFTPAccount = _WtWebGraphAirQualityFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 5),
    _WtWebGraphAirQualityFTPAccount_Type()
)
wtWebGraphAirQualityFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPAccount.setStatus("mandatory")
_WtWebGraphAirQualityFTPOption_Type = OctetString
_WtWebGraphAirQualityFTPOption_Object = MibScalar
wtWebGraphAirQualityFTPOption = _WtWebGraphAirQualityFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 6),
    _WtWebGraphAirQualityFTPOption_Type()
)
wtWebGraphAirQualityFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPOption.setStatus("mandatory")
_WtWebGraphAirQualityFTPEnable_Type = OctetString
_WtWebGraphAirQualityFTPEnable_Object = MibScalar
wtWebGraphAirQualityFTPEnable = _WtWebGraphAirQualityFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 7, 7),
    _WtWebGraphAirQualityFTPEnable_Type()
)
wtWebGraphAirQualityFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityFTPEnable.setStatus("mandatory")
_WtWebGraphAirQualityRSS_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityRSS = _WtWebGraphAirQualityRSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8)
)
_WtWebGraphAirQualityRSSChannelTitle_Type = OctetString
_WtWebGraphAirQualityRSSChannelTitle_Object = MibScalar
wtWebGraphAirQualityRSSChannelTitle = _WtWebGraphAirQualityRSSChannelTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 1),
    _WtWebGraphAirQualityRSSChannelTitle_Type()
)
wtWebGraphAirQualityRSSChannelTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelTitle.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelLink_Type = OctetString
_WtWebGraphAirQualityRSSChannelLink_Object = MibScalar
wtWebGraphAirQualityRSSChannelLink = _WtWebGraphAirQualityRSSChannelLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 2),
    _WtWebGraphAirQualityRSSChannelLink_Type()
)
wtWebGraphAirQualityRSSChannelLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelLink.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelDescription_Type = OctetString
_WtWebGraphAirQualityRSSChannelDescription_Object = MibScalar
wtWebGraphAirQualityRSSChannelDescription = _WtWebGraphAirQualityRSSChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 3),
    _WtWebGraphAirQualityRSSChannelDescription_Type()
)
wtWebGraphAirQualityRSSChannelDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelDescription.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelImage_Type = OctetString
_WtWebGraphAirQualityRSSChannelImage_Object = MibScalar
wtWebGraphAirQualityRSSChannelImage = _WtWebGraphAirQualityRSSChannelImage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 4),
    _WtWebGraphAirQualityRSSChannelImage_Type()
)
wtWebGraphAirQualityRSSChannelImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelImage.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelImageTitle_Type = OctetString
_WtWebGraphAirQualityRSSChannelImageTitle_Object = MibScalar
wtWebGraphAirQualityRSSChannelImageTitle = _WtWebGraphAirQualityRSSChannelImageTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 5),
    _WtWebGraphAirQualityRSSChannelImageTitle_Type()
)
wtWebGraphAirQualityRSSChannelImageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelImageTitle.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelImageLink_Type = OctetString
_WtWebGraphAirQualityRSSChannelImageLink_Object = MibScalar
wtWebGraphAirQualityRSSChannelImageLink = _WtWebGraphAirQualityRSSChannelImageLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 6),
    _WtWebGraphAirQualityRSSChannelImageLink_Type()
)
wtWebGraphAirQualityRSSChannelImageLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelImageLink.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelItemTitle_Type = OctetString
_WtWebGraphAirQualityRSSChannelItemTitle_Object = MibScalar
wtWebGraphAirQualityRSSChannelItemTitle = _WtWebGraphAirQualityRSSChannelItemTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 7),
    _WtWebGraphAirQualityRSSChannelItemTitle_Type()
)
wtWebGraphAirQualityRSSChannelItemTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelItemTitle.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelItemLink_Type = OctetString
_WtWebGraphAirQualityRSSChannelItemLink_Object = MibScalar
wtWebGraphAirQualityRSSChannelItemLink = _WtWebGraphAirQualityRSSChannelItemLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 8),
    _WtWebGraphAirQualityRSSChannelItemLink_Type()
)
wtWebGraphAirQualityRSSChannelItemLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelItemLink.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelItemDescription_Type = OctetString
_WtWebGraphAirQualityRSSChannelItemDescription_Object = MibScalar
wtWebGraphAirQualityRSSChannelItemDescription = _WtWebGraphAirQualityRSSChannelItemDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 9),
    _WtWebGraphAirQualityRSSChannelItemDescription_Type()
)
wtWebGraphAirQualityRSSChannelItemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelItemDescription.setStatus("mandatory")
_WtWebGraphAirQualityRSSChannelItemQuantity_Type = OctetString
_WtWebGraphAirQualityRSSChannelItemQuantity_Object = MibScalar
wtWebGraphAirQualityRSSChannelItemQuantity = _WtWebGraphAirQualityRSSChannelItemQuantity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 8, 10),
    _WtWebGraphAirQualityRSSChannelItemQuantity_Type()
)
wtWebGraphAirQualityRSSChannelItemQuantity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityRSSChannelItemQuantity.setStatus("mandatory")
_WtWebGraphAirQualityLedLights_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityLedLights = _WtWebGraphAirQualityLedLights_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 9)
)


class _WtWebGraphAirQualityLedLightsSensorSel_Type(OctetString):
    """Custom type wtWebGraphAirQualityLedLightsSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityLedLightsSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAirQualityLedLightsSensorSel_Object = MibScalar
wtWebGraphAirQualityLedLightsSensorSel = _WtWebGraphAirQualityLedLightsSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 9, 1),
    _WtWebGraphAirQualityLedLightsSensorSel_Type()
)
wtWebGraphAirQualityLedLightsSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLedLightsSensorSel.setStatus("mandatory")


class _WtWebGraphAirQualityLedLightsLimitGreen_Type(OctetString):
    """Custom type wtWebGraphAirQualityLedLightsLimitGreen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityLedLightsLimitGreen_Type.__name__ = "OctetString"
_WtWebGraphAirQualityLedLightsLimitGreen_Object = MibScalar
wtWebGraphAirQualityLedLightsLimitGreen = _WtWebGraphAirQualityLedLightsLimitGreen_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 9, 2),
    _WtWebGraphAirQualityLedLightsLimitGreen_Type()
)
wtWebGraphAirQualityLedLightsLimitGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLedLightsLimitGreen.setStatus("mandatory")


class _WtWebGraphAirQualityLedLightsLimitYellow_Type(OctetString):
    """Custom type wtWebGraphAirQualityLedLightsLimitYellow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityLedLightsLimitYellow_Type.__name__ = "OctetString"
_WtWebGraphAirQualityLedLightsLimitYellow_Object = MibScalar
wtWebGraphAirQualityLedLightsLimitYellow = _WtWebGraphAirQualityLedLightsLimitYellow_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 9, 3),
    _WtWebGraphAirQualityLedLightsLimitYellow_Type()
)
wtWebGraphAirQualityLedLightsLimitYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLedLightsLimitYellow.setStatus("mandatory")


class _WtWebGraphAirQualityLedLightsLimitRed_Type(OctetString):
    """Custom type wtWebGraphAirQualityLedLightsLimitRed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityLedLightsLimitRed_Type.__name__ = "OctetString"
_WtWebGraphAirQualityLedLightsLimitRed_Object = MibScalar
wtWebGraphAirQualityLedLightsLimitRed = _WtWebGraphAirQualityLedLightsLimitRed_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 3, 9, 4),
    _WtWebGraphAirQualityLedLightsLimitRed_Type()
)
wtWebGraphAirQualityLedLightsLimitRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLedLightsLimitRed.setStatus("mandatory")
_WtWebGraphAirQualityDatalogger_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityDatalogger = _WtWebGraphAirQualityDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 4)
)


class _WtWebGraphAirQualityLoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphAirQualityLoggerTimebase based on Integer32"""
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
        *(("wtWebGraphAirQualityDatalogger-15Min", 3),
          ("wtWebGraphAirQualityDatalogger-1Min", 1),
          ("wtWebGraphAirQualityDatalogger-5Min", 2),
          ("wtWebGraphAirQualityDatalogger-60Min", 4))
    )


_WtWebGraphAirQualityLoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphAirQualityLoggerTimebase_Object = MibScalar
wtWebGraphAirQualityLoggerTimebase = _WtWebGraphAirQualityLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 4, 1),
    _WtWebGraphAirQualityLoggerTimebase_Type()
)
wtWebGraphAirQualityLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLoggerTimebase.setStatus("mandatory")


class _WtWebGraphAirQualityLoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphAirQualityLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphAirQualityLoggerSensorSel_Object = MibScalar
wtWebGraphAirQualityLoggerSensorSel = _WtWebGraphAirQualityLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 4, 2),
    _WtWebGraphAirQualityLoggerSensorSel_Type()
)
wtWebGraphAirQualityLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityLoggerSensorSel.setStatus("mandatory")
_WtWebGraphAirQualityAlarm_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityAlarm = _WtWebGraphAirQualityAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5)
)


class _WtWebGraphAirQualityAlarmCount_Type(Integer32):
    """Custom type wtWebGraphAirQualityAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAirQualityAlarmCount_Type.__name__ = "Integer32"
_WtWebGraphAirQualityAlarmCount_Object = MibScalar
wtWebGraphAirQualityAlarmCount = _WtWebGraphAirQualityAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 1),
    _WtWebGraphAirQualityAlarmCount_Type()
)
wtWebGraphAirQualityAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmCount.setStatus("mandatory")
_WtWebGraphAirQualityAlarmIfTable_Object = MibTable
wtWebGraphAirQualityAlarmIfTable = _WtWebGraphAirQualityAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmIfTable.setStatus("mandatory")
_WtWebGraphAirQualityAlarmIfEntry_Object = MibTableRow
wtWebGraphAirQualityAlarmIfEntry = _WtWebGraphAirQualityAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 2, 1)
)
wtWebGraphAirQualityAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmIfEntry.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmNo_Type(Integer32):
    """Custom type wtWebGraphAirQualityAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphAirQualityAlarmNo_Type.__name__ = "Integer32"
_WtWebGraphAirQualityAlarmNo_Object = MibTableColumn
wtWebGraphAirQualityAlarmNo = _WtWebGraphAirQualityAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 2, 1, 1),
    _WtWebGraphAirQualityAlarmNo_Type()
)
wtWebGraphAirQualityAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmNo.setStatus("mandatory")
_WtWebGraphAirQualityAlarmTable_Object = MibTable
wtWebGraphAirQualityAlarmTable = _WtWebGraphAirQualityAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTable.setStatus("mandatory")
_WtWebGraphAirQualityAlarmEntry_Object = MibTableRow
wtWebGraphAirQualityAlarmEntry = _WtWebGraphAirQualityAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1)
)
wtWebGraphAirQualityAlarmEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmEntry.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphAirQualityAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityAlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphAirQualityAlarmTrigger_Object = MibTableColumn
wtWebGraphAirQualityAlarmTrigger = _WtWebGraphAirQualityAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 1),
    _WtWebGraphAirQualityAlarmTrigger_Type()
)
wtWebGraphAirQualityAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTrigger.setStatus("mandatory")
_WtWebGraphAirQualityAlarmMin_Type = OctetString
_WtWebGraphAirQualityAlarmMin_Object = MibTableColumn
wtWebGraphAirQualityAlarmMin = _WtWebGraphAirQualityAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 2),
    _WtWebGraphAirQualityAlarmMin_Type()
)
wtWebGraphAirQualityAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmMin.setStatus("mandatory")
_WtWebGraphAirQualityAlarmMax_Type = OctetString
_WtWebGraphAirQualityAlarmMax_Object = MibTableColumn
wtWebGraphAirQualityAlarmMax = _WtWebGraphAirQualityAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 3),
    _WtWebGraphAirQualityAlarmMax_Type()
)
wtWebGraphAirQualityAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmMax.setStatus("mandatory")
_WtWebGraphAirQualityAlarmHysteresis_Type = OctetString
_WtWebGraphAirQualityAlarmHysteresis_Object = MibTableColumn
wtWebGraphAirQualityAlarmHysteresis = _WtWebGraphAirQualityAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 4),
    _WtWebGraphAirQualityAlarmHysteresis_Type()
)
wtWebGraphAirQualityAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmHysteresis.setStatus("mandatory")
_WtWebGraphAirQualityAlarmDelay_Type = OctetString
_WtWebGraphAirQualityAlarmDelay_Object = MibTableColumn
wtWebGraphAirQualityAlarmDelay = _WtWebGraphAirQualityAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 5),
    _WtWebGraphAirQualityAlarmDelay_Type()
)
wtWebGraphAirQualityAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmDelay.setStatus("mandatory")
_WtWebGraphAirQualityAlarmInterval_Type = OctetString
_WtWebGraphAirQualityAlarmInterval_Object = MibTableColumn
wtWebGraphAirQualityAlarmInterval = _WtWebGraphAirQualityAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 6),
    _WtWebGraphAirQualityAlarmInterval_Type()
)
wtWebGraphAirQualityAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmInterval.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmEnable_Type(OctetString):
    """Custom type wtWebGraphAirQualityAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityAlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphAirQualityAlarmEnable_Object = MibTableColumn
wtWebGraphAirQualityAlarmEnable = _WtWebGraphAirQualityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 7),
    _WtWebGraphAirQualityAlarmEnable_Type()
)
wtWebGraphAirQualityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmEnable.setStatus("mandatory")
_WtWebGraphAirQualityAlarmEMailAddr_Type = OctetString
_WtWebGraphAirQualityAlarmEMailAddr_Object = MibTableColumn
wtWebGraphAirQualityAlarmEMailAddr = _WtWebGraphAirQualityAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 8),
    _WtWebGraphAirQualityAlarmEMailAddr_Type()
)
wtWebGraphAirQualityAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmEMailAddr.setStatus("mandatory")
_WtWebGraphAirQualityAlarmMailSubject_Type = OctetString
_WtWebGraphAirQualityAlarmMailSubject_Object = MibTableColumn
wtWebGraphAirQualityAlarmMailSubject = _WtWebGraphAirQualityAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 9),
    _WtWebGraphAirQualityAlarmMailSubject_Type()
)
wtWebGraphAirQualityAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmMailSubject.setStatus("mandatory")
_WtWebGraphAirQualityAlarmMailText_Type = OctetString
_WtWebGraphAirQualityAlarmMailText_Object = MibTableColumn
wtWebGraphAirQualityAlarmMailText = _WtWebGraphAirQualityAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 10),
    _WtWebGraphAirQualityAlarmMailText_Type()
)
wtWebGraphAirQualityAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmMailText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmManagerIP_Type = OctetString
_WtWebGraphAirQualityAlarmManagerIP_Object = MibTableColumn
wtWebGraphAirQualityAlarmManagerIP = _WtWebGraphAirQualityAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 11),
    _WtWebGraphAirQualityAlarmManagerIP_Type()
)
wtWebGraphAirQualityAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmManagerIP.setStatus("mandatory")
_WtWebGraphAirQualityAlarmTrapText_Type = OctetString
_WtWebGraphAirQualityAlarmTrapText_Object = MibTableColumn
wtWebGraphAirQualityAlarmTrapText = _WtWebGraphAirQualityAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 12),
    _WtWebGraphAirQualityAlarmTrapText_Type()
)
wtWebGraphAirQualityAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTrapText.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphAirQualityAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphAirQualityAlarmMailOptions_Object = MibTableColumn
wtWebGraphAirQualityAlarmMailOptions = _WtWebGraphAirQualityAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 13),
    _WtWebGraphAirQualityAlarmMailOptions_Type()
)
wtWebGraphAirQualityAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmMailOptions.setStatus("mandatory")
_WtWebGraphAirQualityAlarmTcpIpAddr_Type = OctetString
_WtWebGraphAirQualityAlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphAirQualityAlarmTcpIpAddr = _WtWebGraphAirQualityAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 14),
    _WtWebGraphAirQualityAlarmTcpIpAddr_Type()
)
wtWebGraphAirQualityAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphAirQualityAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAirQualityAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphAirQualityAlarmTcpPort_Object = MibTableColumn
wtWebGraphAirQualityAlarmTcpPort = _WtWebGraphAirQualityAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 15),
    _WtWebGraphAirQualityAlarmTcpPort_Type()
)
wtWebGraphAirQualityAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTcpPort.setStatus("mandatory")
_WtWebGraphAirQualityAlarmTcpText_Type = OctetString
_WtWebGraphAirQualityAlarmTcpText_Object = MibTableColumn
wtWebGraphAirQualityAlarmTcpText = _WtWebGraphAirQualityAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 16),
    _WtWebGraphAirQualityAlarmTcpText_Type()
)
wtWebGraphAirQualityAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTcpText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmClearMailSubject_Type = OctetString
_WtWebGraphAirQualityAlarmClearMailSubject_Object = MibTableColumn
wtWebGraphAirQualityAlarmClearMailSubject = _WtWebGraphAirQualityAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 17),
    _WtWebGraphAirQualityAlarmClearMailSubject_Type()
)
wtWebGraphAirQualityAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphAirQualityAlarmClearMailText_Type = OctetString
_WtWebGraphAirQualityAlarmClearMailText_Object = MibTableColumn
wtWebGraphAirQualityAlarmClearMailText = _WtWebGraphAirQualityAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 18),
    _WtWebGraphAirQualityAlarmClearMailText_Type()
)
wtWebGraphAirQualityAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmClearMailText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmClearTrapText_Type = OctetString
_WtWebGraphAirQualityAlarmClearTrapText_Object = MibTableColumn
wtWebGraphAirQualityAlarmClearTrapText = _WtWebGraphAirQualityAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 19),
    _WtWebGraphAirQualityAlarmClearTrapText_Type()
)
wtWebGraphAirQualityAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmClearTrapText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmClearTcpText_Type = OctetString
_WtWebGraphAirQualityAlarmClearTcpText_Object = MibTableColumn
wtWebGraphAirQualityAlarmClearTcpText = _WtWebGraphAirQualityAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 20),
    _WtWebGraphAirQualityAlarmClearTcpText_Type()
)
wtWebGraphAirQualityAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmClearTcpText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmDeltaTemp_Type = OctetString
_WtWebGraphAirQualityAlarmDeltaTemp_Object = MibTableColumn
wtWebGraphAirQualityAlarmDeltaTemp = _WtWebGraphAirQualityAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 21),
    _WtWebGraphAirQualityAlarmDeltaTemp_Type()
)
wtWebGraphAirQualityAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmDeltaTemp.setStatus("mandatory")
_WtWebGraphAirQualityAlarmRHMin_Type = OctetString
_WtWebGraphAirQualityAlarmRHMin_Object = MibTableColumn
wtWebGraphAirQualityAlarmRHMin = _WtWebGraphAirQualityAlarmRHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 22),
    _WtWebGraphAirQualityAlarmRHMin_Type()
)
wtWebGraphAirQualityAlarmRHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmRHMin.setStatus("mandatory")
_WtWebGraphAirQualityAlarmRHMax_Type = OctetString
_WtWebGraphAirQualityAlarmRHMax_Object = MibTableColumn
wtWebGraphAirQualityAlarmRHMax = _WtWebGraphAirQualityAlarmRHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 23),
    _WtWebGraphAirQualityAlarmRHMax_Type()
)
wtWebGraphAirQualityAlarmRHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmRHMax.setStatus("mandatory")
_WtWebGraphAirQualityAlarmRHHysteresis_Type = OctetString
_WtWebGraphAirQualityAlarmRHHysteresis_Object = MibTableColumn
wtWebGraphAirQualityAlarmRHHysteresis = _WtWebGraphAirQualityAlarmRHHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 24),
    _WtWebGraphAirQualityAlarmRHHysteresis_Type()
)
wtWebGraphAirQualityAlarmRHHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmRHHysteresis.setStatus("mandatory")
_WtWebGraphAirQualityAlarmAHMin_Type = OctetString
_WtWebGraphAirQualityAlarmAHMin_Object = MibTableColumn
wtWebGraphAirQualityAlarmAHMin = _WtWebGraphAirQualityAlarmAHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 25),
    _WtWebGraphAirQualityAlarmAHMin_Type()
)
wtWebGraphAirQualityAlarmAHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmAHMin.setStatus("mandatory")
_WtWebGraphAirQualityAlarmAHMax_Type = OctetString
_WtWebGraphAirQualityAlarmAHMax_Object = MibTableColumn
wtWebGraphAirQualityAlarmAHMax = _WtWebGraphAirQualityAlarmAHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 26),
    _WtWebGraphAirQualityAlarmAHMax_Type()
)
wtWebGraphAirQualityAlarmAHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmAHMax.setStatus("mandatory")
_WtWebGraphAirQualityAlarmSyslogIpAddr_Type = IpAddress
_WtWebGraphAirQualityAlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphAirQualityAlarmSyslogIpAddr = _WtWebGraphAirQualityAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 27),
    _WtWebGraphAirQualityAlarmSyslogIpAddr_Type()
)
wtWebGraphAirQualityAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphAirQualityAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphAirQualityAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphAirQualityAlarmSyslogPort_Object = MibTableColumn
wtWebGraphAirQualityAlarmSyslogPort = _WtWebGraphAirQualityAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 28),
    _WtWebGraphAirQualityAlarmSyslogPort_Type()
)
wtWebGraphAirQualityAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmSyslogPort.setStatus("mandatory")
_WtWebGraphAirQualityAlarmSyslogText_Type = OctetString
_WtWebGraphAirQualityAlarmSyslogText_Object = MibTableColumn
wtWebGraphAirQualityAlarmSyslogText = _WtWebGraphAirQualityAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 29),
    _WtWebGraphAirQualityAlarmSyslogText_Type()
)
wtWebGraphAirQualityAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmSyslogText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmSyslogClearText_Type = OctetString
_WtWebGraphAirQualityAlarmSyslogClearText_Object = MibTableColumn
wtWebGraphAirQualityAlarmSyslogClearText = _WtWebGraphAirQualityAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 30),
    _WtWebGraphAirQualityAlarmSyslogClearText_Type()
)
wtWebGraphAirQualityAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmFtpDataPort_Type = OctetString
_WtWebGraphAirQualityAlarmFtpDataPort_Object = MibTableColumn
wtWebGraphAirQualityAlarmFtpDataPort = _WtWebGraphAirQualityAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 31),
    _WtWebGraphAirQualityAlarmFtpDataPort_Type()
)
wtWebGraphAirQualityAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphAirQualityAlarmFtpFileName_Type = OctetString
_WtWebGraphAirQualityAlarmFtpFileName_Object = MibTableColumn
wtWebGraphAirQualityAlarmFtpFileName = _WtWebGraphAirQualityAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 32),
    _WtWebGraphAirQualityAlarmFtpFileName_Type()
)
wtWebGraphAirQualityAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmFtpFileName.setStatus("mandatory")
_WtWebGraphAirQualityAlarmFtpText_Type = OctetString
_WtWebGraphAirQualityAlarmFtpText_Object = MibTableColumn
wtWebGraphAirQualityAlarmFtpText = _WtWebGraphAirQualityAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 33),
    _WtWebGraphAirQualityAlarmFtpText_Type()
)
wtWebGraphAirQualityAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmFtpText.setStatus("mandatory")
_WtWebGraphAirQualityAlarmFtpClearText_Type = OctetString
_WtWebGraphAirQualityAlarmFtpClearText_Object = MibTableColumn
wtWebGraphAirQualityAlarmFtpClearText = _WtWebGraphAirQualityAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 34),
    _WtWebGraphAirQualityAlarmFtpClearText_Type()
)
wtWebGraphAirQualityAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphAirQualityAlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphAirQualityAlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityAlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphAirQualityAlarmFtpOption_Object = MibTableColumn
wtWebGraphAirQualityAlarmFtpOption = _WtWebGraphAirQualityAlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 35),
    _WtWebGraphAirQualityAlarmFtpOption_Type()
)
wtWebGraphAirQualityAlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmFtpOption.setStatus("mandatory")
_WtWebGraphAirQualityAlarmTimerCron_Type = OctetString
_WtWebGraphAirQualityAlarmTimerCron_Object = MibTableColumn
wtWebGraphAirQualityAlarmTimerCron = _WtWebGraphAirQualityAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 36),
    _WtWebGraphAirQualityAlarmTimerCron_Type()
)
wtWebGraphAirQualityAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmTimerCron.setStatus("mandatory")
_WtWebGraphAirQualityAlarmVocMax_Type = OctetString
_WtWebGraphAirQualityAlarmVocMax_Object = MibTableColumn
wtWebGraphAirQualityAlarmVocMax = _WtWebGraphAirQualityAlarmVocMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 37),
    _WtWebGraphAirQualityAlarmVocMax_Type()
)
wtWebGraphAirQualityAlarmVocMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmVocMax.setStatus("mandatory")
_WtWebGraphAirQualityAlarmVocHysteresis_Type = OctetString
_WtWebGraphAirQualityAlarmVocHysteresis_Object = MibTableColumn
wtWebGraphAirQualityAlarmVocHysteresis = _WtWebGraphAirQualityAlarmVocHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 38),
    _WtWebGraphAirQualityAlarmVocHysteresis_Type()
)
wtWebGraphAirQualityAlarmVocHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmVocHysteresis.setStatus("mandatory")
_WtWebGraphAirQualityAlarmName_Type = OctetString
_WtWebGraphAirQualityAlarmName_Object = MibTableColumn
wtWebGraphAirQualityAlarmName = _WtWebGraphAirQualityAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 39),
    _WtWebGraphAirQualityAlarmName_Type()
)
wtWebGraphAirQualityAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmName.setStatus("mandatory")
_WtWebGraphAirQualityAlarmActive_Type = OctetString
_WtWebGraphAirQualityAlarmActive_Object = MibTableColumn
wtWebGraphAirQualityAlarmActive = _WtWebGraphAirQualityAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 5, 3, 1, 40),
    _WtWebGraphAirQualityAlarmActive_Type()
)
wtWebGraphAirQualityAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlarmActive.setStatus("mandatory")
_WtWebGraphAirQualityGraphics_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityGraphics = _WtWebGraphAirQualityGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6)
)
_WtWebGraphAirQualityGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityGraphicsBase = _WtWebGraphAirQualityGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1)
)
_WtWebGraphAirQualityGraphicsBaseEnable_Type = OctetString
_WtWebGraphAirQualityGraphicsBaseEnable_Object = MibScalar
wtWebGraphAirQualityGraphicsBaseEnable = _WtWebGraphAirQualityGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 1),
    _WtWebGraphAirQualityGraphicsBaseEnable_Type()
)
wtWebGraphAirQualityGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsBaseWidth_Type = Integer32
_WtWebGraphAirQualityGraphicsBaseWidth_Object = MibScalar
wtWebGraphAirQualityGraphicsBaseWidth = _WtWebGraphAirQualityGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 2),
    _WtWebGraphAirQualityGraphicsBaseWidth_Type()
)
wtWebGraphAirQualityGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsBaseHeight_Type = Integer32
_WtWebGraphAirQualityGraphicsBaseHeight_Object = MibScalar
wtWebGraphAirQualityGraphicsBaseHeight = _WtWebGraphAirQualityGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 3),
    _WtWebGraphAirQualityGraphicsBaseHeight_Type()
)
wtWebGraphAirQualityGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphAirQualityGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphAirQualityGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAirQualityGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphAirQualityGraphicsBaseFrameColor_Object = MibScalar
wtWebGraphAirQualityGraphicsBaseFrameColor = _WtWebGraphAirQualityGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 4),
    _WtWebGraphAirQualityGraphicsBaseFrameColor_Type()
)
wtWebGraphAirQualityGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphAirQualityGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphAirQualityGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAirQualityGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphAirQualityGraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphAirQualityGraphicsBaseBackgroundColor = _WtWebGraphAirQualityGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 5),
    _WtWebGraphAirQualityGraphicsBaseBackgroundColor_Type()
)
wtWebGraphAirQualityGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsBasePollingrate_Type = Integer32
_WtWebGraphAirQualityGraphicsBasePollingrate_Object = MibScalar
wtWebGraphAirQualityGraphicsBasePollingrate = _WtWebGraphAirQualityGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 1, 6),
    _WtWebGraphAirQualityGraphicsBasePollingrate_Type()
)
wtWebGraphAirQualityGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityGraphicsSelect = _WtWebGraphAirQualityGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2)
)


class _WtWebGraphAirQualityGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphAirQualityGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphAirQualityGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphAirQualityGraphicsSelectDisplaySensorSel = _WtWebGraphAirQualityGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 1),
    _WtWebGraphAirQualityGraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphAirQualityGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphAirQualityGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebGraphAirQualityGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphAirQualityGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem = _WtWebGraphAirQualityGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 2),
    _WtWebGraphAirQualityGraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphAirQualitySensorColorTable_Object = MibTable
wtWebGraphAirQualitySensorColorTable = _WtWebGraphAirQualitySensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensorColorTable.setStatus("mandatory")
_WtWebGraphAirQualitySensorColorEntry_Object = MibTableRow
wtWebGraphAirQualitySensorColorEntry = _WtWebGraphAirQualitySensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 3, 1)
)
wtWebGraphAirQualitySensorColorEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualitySensorColorEntry.setStatus("mandatory")


class _WtWebGraphAirQualityGraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphAirQualityGraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebGraphAirQualityGraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphAirQualityGraphicsSensorColor_Object = MibTableColumn
wtWebGraphAirQualityGraphicsSensorColor = _WtWebGraphAirQualityGraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphAirQualityGraphicsSensorColor_Type()
)
wtWebGraphAirQualityGraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsSensorColor.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsSelectScale_Type = OctetString
_WtWebGraphAirQualityGraphicsSelectScale_Object = MibTableColumn
wtWebGraphAirQualityGraphicsSelectScale = _WtWebGraphAirQualityGraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphAirQualityGraphicsSelectScale_Type()
)
wtWebGraphAirQualityGraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsSelectScale.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityGraphicsScale = _WtWebGraphAirQualityGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3)
)
_WtWebGraphAirQualityGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphAirQualityGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphAirQualityGraphicsScaleAutoScaleEnable = _WtWebGraphAirQualityGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 1),
    _WtWebGraphAirQualityGraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphAirQualityGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphAirQualityGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphAirQualityGraphicsScaleAutoFitEnable = _WtWebGraphAirQualityGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 2),
    _WtWebGraphAirQualityGraphicsScaleAutoFitEnable_Type()
)
wtWebGraphAirQualityGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale1Min_Type = Integer32
_WtWebGraphAirQualityGraphicsScale1Min_Object = MibScalar
wtWebGraphAirQualityGraphicsScale1Min = _WtWebGraphAirQualityGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 3),
    _WtWebGraphAirQualityGraphicsScale1Min_Type()
)
wtWebGraphAirQualityGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale1Min.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale2Min_Type = Integer32
_WtWebGraphAirQualityGraphicsScale2Min_Object = MibScalar
wtWebGraphAirQualityGraphicsScale2Min = _WtWebGraphAirQualityGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 4),
    _WtWebGraphAirQualityGraphicsScale2Min_Type()
)
wtWebGraphAirQualityGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale2Min.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale3Min_Type = Integer32
_WtWebGraphAirQualityGraphicsScale3Min_Object = MibScalar
wtWebGraphAirQualityGraphicsScale3Min = _WtWebGraphAirQualityGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 5),
    _WtWebGraphAirQualityGraphicsScale3Min_Type()
)
wtWebGraphAirQualityGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale3Min.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale4Min_Type = Integer32
_WtWebGraphAirQualityGraphicsScale4Min_Object = MibScalar
wtWebGraphAirQualityGraphicsScale4Min = _WtWebGraphAirQualityGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 6),
    _WtWebGraphAirQualityGraphicsScale4Min_Type()
)
wtWebGraphAirQualityGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale4Min.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale1Max_Type = Integer32
_WtWebGraphAirQualityGraphicsScale1Max_Object = MibScalar
wtWebGraphAirQualityGraphicsScale1Max = _WtWebGraphAirQualityGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 7),
    _WtWebGraphAirQualityGraphicsScale1Max_Type()
)
wtWebGraphAirQualityGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale1Max.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale2Max_Type = Integer32
_WtWebGraphAirQualityGraphicsScale2Max_Object = MibScalar
wtWebGraphAirQualityGraphicsScale2Max = _WtWebGraphAirQualityGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 8),
    _WtWebGraphAirQualityGraphicsScale2Max_Type()
)
wtWebGraphAirQualityGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale2Max.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale3Max_Type = Integer32
_WtWebGraphAirQualityGraphicsScale3Max_Object = MibScalar
wtWebGraphAirQualityGraphicsScale3Max = _WtWebGraphAirQualityGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 9),
    _WtWebGraphAirQualityGraphicsScale3Max_Type()
)
wtWebGraphAirQualityGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale3Max.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale4Max_Type = Integer32
_WtWebGraphAirQualityGraphicsScale4Max_Object = MibScalar
wtWebGraphAirQualityGraphicsScale4Max = _WtWebGraphAirQualityGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 10),
    _WtWebGraphAirQualityGraphicsScale4Max_Type()
)
wtWebGraphAirQualityGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale4Max.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale1Unit_Type = OctetString
_WtWebGraphAirQualityGraphicsScale1Unit_Object = MibScalar
wtWebGraphAirQualityGraphicsScale1Unit = _WtWebGraphAirQualityGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 11),
    _WtWebGraphAirQualityGraphicsScale1Unit_Type()
)
wtWebGraphAirQualityGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale2Unit_Type = OctetString
_WtWebGraphAirQualityGraphicsScale2Unit_Object = MibScalar
wtWebGraphAirQualityGraphicsScale2Unit = _WtWebGraphAirQualityGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 12),
    _WtWebGraphAirQualityGraphicsScale2Unit_Type()
)
wtWebGraphAirQualityGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale3Unit_Type = OctetString
_WtWebGraphAirQualityGraphicsScale3Unit_Object = MibScalar
wtWebGraphAirQualityGraphicsScale3Unit = _WtWebGraphAirQualityGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 13),
    _WtWebGraphAirQualityGraphicsScale3Unit_Type()
)
wtWebGraphAirQualityGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphAirQualityGraphicsScale4Unit_Type = OctetString
_WtWebGraphAirQualityGraphicsScale4Unit_Object = MibScalar
wtWebGraphAirQualityGraphicsScale4Unit = _WtWebGraphAirQualityGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 1, 6, 3, 14),
    _WtWebGraphAirQualityGraphicsScale4Unit_Type()
)
wtWebGraphAirQualityGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityGraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphAirQualityPorts_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityPorts = _WtWebGraphAirQualityPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2)
)
_WtWebGraphAirQualityPortTable_Object = MibTable
wtWebGraphAirQualityPortTable = _WtWebGraphAirQualityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortTable.setStatus("mandatory")
_WtWebGraphAirQualityPortEntry_Object = MibTableRow
wtWebGraphAirQualityPortEntry = _WtWebGraphAirQualityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1)
)
wtWebGraphAirQualityPortEntry.setIndexNames(
    (0, "WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualitySensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortEntry.setStatus("mandatory")
_WtWebGraphAirQualityPortName_Type = OctetString
_WtWebGraphAirQualityPortName_Object = MibTableColumn
wtWebGraphAirQualityPortName = _WtWebGraphAirQualityPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 1),
    _WtWebGraphAirQualityPortName_Type()
)
wtWebGraphAirQualityPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortName.setStatus("mandatory")
_WtWebGraphAirQualityPortText_Type = OctetString
_WtWebGraphAirQualityPortText_Object = MibTableColumn
wtWebGraphAirQualityPortText = _WtWebGraphAirQualityPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 2),
    _WtWebGraphAirQualityPortText_Type()
)
wtWebGraphAirQualityPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortText.setStatus("mandatory")
_WtWebGraphAirQualityPortOffset1_Type = OctetString
_WtWebGraphAirQualityPortOffset1_Object = MibTableColumn
wtWebGraphAirQualityPortOffset1 = _WtWebGraphAirQualityPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 3),
    _WtWebGraphAirQualityPortOffset1_Type()
)
wtWebGraphAirQualityPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortOffset1.setStatus("mandatory")
_WtWebGraphAirQualityPortTemperature1_Type = OctetString
_WtWebGraphAirQualityPortTemperature1_Object = MibTableColumn
wtWebGraphAirQualityPortTemperature1 = _WtWebGraphAirQualityPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 4),
    _WtWebGraphAirQualityPortTemperature1_Type()
)
wtWebGraphAirQualityPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortTemperature1.setStatus("mandatory")
_WtWebGraphAirQualityPortOffset2_Type = OctetString
_WtWebGraphAirQualityPortOffset2_Object = MibTableColumn
wtWebGraphAirQualityPortOffset2 = _WtWebGraphAirQualityPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 5),
    _WtWebGraphAirQualityPortOffset2_Type()
)
wtWebGraphAirQualityPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortOffset2.setStatus("mandatory")
_WtWebGraphAirQualityPortTemperature2_Type = OctetString
_WtWebGraphAirQualityPortTemperature2_Object = MibTableColumn
wtWebGraphAirQualityPortTemperature2 = _WtWebGraphAirQualityPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 6),
    _WtWebGraphAirQualityPortTemperature2_Type()
)
wtWebGraphAirQualityPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortTemperature2.setStatus("mandatory")
_WtWebGraphAirQualityPortComment_Type = OctetString
_WtWebGraphAirQualityPortComment_Object = MibTableColumn
wtWebGraphAirQualityPortComment = _WtWebGraphAirQualityPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 2, 1, 1, 7),
    _WtWebGraphAirQualityPortComment_Type()
)
wtWebGraphAirQualityPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityPortComment.setStatus("mandatory")
_WtWebGraphAirQualityManufact_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityManufact = _WtWebGraphAirQualityManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3)
)
_WtWebGraphAirQualityMfName_Type = OctetString
_WtWebGraphAirQualityMfName_Object = MibScalar
wtWebGraphAirQualityMfName = _WtWebGraphAirQualityMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 1),
    _WtWebGraphAirQualityMfName_Type()
)
wtWebGraphAirQualityMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfName.setStatus("mandatory")
_WtWebGraphAirQualityMfAddr_Type = OctetString
_WtWebGraphAirQualityMfAddr_Object = MibScalar
wtWebGraphAirQualityMfAddr = _WtWebGraphAirQualityMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 2),
    _WtWebGraphAirQualityMfAddr_Type()
)
wtWebGraphAirQualityMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfAddr.setStatus("mandatory")
_WtWebGraphAirQualityMfHotline_Type = OctetString
_WtWebGraphAirQualityMfHotline_Object = MibScalar
wtWebGraphAirQualityMfHotline = _WtWebGraphAirQualityMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 3),
    _WtWebGraphAirQualityMfHotline_Type()
)
wtWebGraphAirQualityMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfHotline.setStatus("mandatory")
_WtWebGraphAirQualityMfInternet_Type = OctetString
_WtWebGraphAirQualityMfInternet_Object = MibScalar
wtWebGraphAirQualityMfInternet = _WtWebGraphAirQualityMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 4),
    _WtWebGraphAirQualityMfInternet_Type()
)
wtWebGraphAirQualityMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfInternet.setStatus("mandatory")
_WtWebGraphAirQualityMfDeviceTyp_Type = OctetString
_WtWebGraphAirQualityMfDeviceTyp_Object = MibScalar
wtWebGraphAirQualityMfDeviceTyp = _WtWebGraphAirQualityMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 5),
    _WtWebGraphAirQualityMfDeviceTyp_Type()
)
wtWebGraphAirQualityMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfDeviceTyp.setStatus("mandatory")
_WtWebGraphAirQualityMfOrderNo_Type = OctetString
_WtWebGraphAirQualityMfOrderNo_Object = MibScalar
wtWebGraphAirQualityMfOrderNo = _WtWebGraphAirQualityMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 3, 3, 6),
    _WtWebGraphAirQualityMfOrderNo_Type()
)
wtWebGraphAirQualityMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityMfOrderNo.setStatus("mandatory")
_WtWebGraphAirQualityDiag_ObjectIdentity = ObjectIdentity
wtWebGraphAirQualityDiag = _WtWebGraphAirQualityDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4)
)
_WtWebGraphAirQualityDiagErrorCount_Type = Integer32
_WtWebGraphAirQualityDiagErrorCount_Object = MibScalar
wtWebGraphAirQualityDiagErrorCount = _WtWebGraphAirQualityDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4, 1),
    _WtWebGraphAirQualityDiagErrorCount_Type()
)
wtWebGraphAirQualityDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDiagErrorCount.setStatus("mandatory")
_WtWebGraphAirQualityDiagBinaryError_Type = OctetString
_WtWebGraphAirQualityDiagBinaryError_Object = MibScalar
wtWebGraphAirQualityDiagBinaryError = _WtWebGraphAirQualityDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4, 2),
    _WtWebGraphAirQualityDiagBinaryError_Type()
)
wtWebGraphAirQualityDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDiagBinaryError.setStatus("mandatory")
_WtWebGraphAirQualityDiagErrorIndex_Type = Integer32
_WtWebGraphAirQualityDiagErrorIndex_Object = MibScalar
wtWebGraphAirQualityDiagErrorIndex = _WtWebGraphAirQualityDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4, 3),
    _WtWebGraphAirQualityDiagErrorIndex_Type()
)
wtWebGraphAirQualityDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDiagErrorIndex.setStatus("mandatory")
_WtWebGraphAirQualityDiagErrorMessage_Type = OctetString
_WtWebGraphAirQualityDiagErrorMessage_Object = MibScalar
wtWebGraphAirQualityDiagErrorMessage = _WtWebGraphAirQualityDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4, 4),
    _WtWebGraphAirQualityDiagErrorMessage_Type()
)
wtWebGraphAirQualityDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDiagErrorMessage.setStatus("mandatory")
_WtWebGraphAirQualityDiagErrorClear_Type = Integer32
_WtWebGraphAirQualityDiagErrorClear_Object = MibScalar
wtWebGraphAirQualityDiagErrorClear = _WtWebGraphAirQualityDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 4, 5),
    _WtWebGraphAirQualityDiagErrorClear_Type()
)
wtWebGraphAirQualityDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphAirQualityDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphAirQualityAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 31)
)
wtWebGraphAirQualityAlert1.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert1.setStatus(
        ""
    )

wtWebGraphAirQualityAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 32)
)
wtWebGraphAirQualityAlert2.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert2.setStatus(
        ""
    )

wtWebGraphAirQualityAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 33)
)
wtWebGraphAirQualityAlert3.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert3.setStatus(
        ""
    )

wtWebGraphAirQualityAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 34)
)
wtWebGraphAirQualityAlert4.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert4.setStatus(
        ""
    )

wtWebGraphAirQualityAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 35)
)
wtWebGraphAirQualityAlert5.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert5.setStatus(
        ""
    )

wtWebGraphAirQualityAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 36)
)
wtWebGraphAirQualityAlert6.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert6.setStatus(
        ""
    )

wtWebGraphAirQualityAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 37)
)
wtWebGraphAirQualityAlert7.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert7.setStatus(
        ""
    )

wtWebGraphAirQualityAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 38)
)
wtWebGraphAirQualityAlert8.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert8.setStatus(
        ""
    )

wtWebGraphAirQualityAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 91)
)
wtWebGraphAirQualityAlert9.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert9.setStatus(
        ""
    )

wtWebGraphAirQualityAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 92)
)
wtWebGraphAirQualityAlert10.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert10.setStatus(
        ""
    )

wtWebGraphAirQualityAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 93)
)
wtWebGraphAirQualityAlert11.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert11.setStatus(
        ""
    )

wtWebGraphAirQualityAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 94)
)
wtWebGraphAirQualityAlert12.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert12.setStatus(
        ""
    )

wtWebGraphAirQualityAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 95)
)
wtWebGraphAirQualityAlert13.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert13.setStatus(
        ""
    )

wtWebGraphAirQualityAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 96)
)
wtWebGraphAirQualityAlert14.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert14.setStatus(
        ""
    )

wtWebGraphAirQualityAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 97)
)
wtWebGraphAirQualityAlert15.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert15.setStatus(
        ""
    )

wtWebGraphAirQualityAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 98)
)
wtWebGraphAirQualityAlert16.setObjects(
    ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlert16.setStatus(
        ""
    )

wtWebGraphAirQualityAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 35, 0, 110)
)
wtWebGraphAirQualityAlertDiag.setObjects(
      *(("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityDiagErrorIndex"),
        ("WebGraph-Air-Quality-US-MIB", "wtWebGraphAirQualityDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphAirQualityAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Air-Quality-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphAirQuality": wtWebGraphAirQuality,
       "wtWebGraphAirQualityAlert1": wtWebGraphAirQualityAlert1,
       "wtWebGraphAirQualityAlert2": wtWebGraphAirQualityAlert2,
       "wtWebGraphAirQualityAlert3": wtWebGraphAirQualityAlert3,
       "wtWebGraphAirQualityAlert4": wtWebGraphAirQualityAlert4,
       "wtWebGraphAirQualityAlert5": wtWebGraphAirQualityAlert5,
       "wtWebGraphAirQualityAlert6": wtWebGraphAirQualityAlert6,
       "wtWebGraphAirQualityAlert7": wtWebGraphAirQualityAlert7,
       "wtWebGraphAirQualityAlert8": wtWebGraphAirQualityAlert8,
       "wtWebGraphAirQualityAlert9": wtWebGraphAirQualityAlert9,
       "wtWebGraphAirQualityAlert10": wtWebGraphAirQualityAlert10,
       "wtWebGraphAirQualityAlert11": wtWebGraphAirQualityAlert11,
       "wtWebGraphAirQualityAlert12": wtWebGraphAirQualityAlert12,
       "wtWebGraphAirQualityAlert13": wtWebGraphAirQualityAlert13,
       "wtWebGraphAirQualityAlert14": wtWebGraphAirQualityAlert14,
       "wtWebGraphAirQualityAlert15": wtWebGraphAirQualityAlert15,
       "wtWebGraphAirQualityAlert16": wtWebGraphAirQualityAlert16,
       "wtWebGraphAirQualityAlertDiag": wtWebGraphAirQualityAlertDiag,
       "wtWebGraphAirQualityTemp": wtWebGraphAirQualityTemp,
       "wtWebGraphAirQualitySensors": wtWebGraphAirQualitySensors,
       "wtWebGraphAirQualitySensorTable": wtWebGraphAirQualitySensorTable,
       "wtWebGraphAirQualitySensorEntry": wtWebGraphAirQualitySensorEntry,
       "wtWebGraphAirQualitySensorNo": wtWebGraphAirQualitySensorNo,
       "wtWebGraphAirQualityTempValueTable": wtWebGraphAirQualityTempValueTable,
       "wtWebGraphAirQualityTempValueEntry": wtWebGraphAirQualityTempValueEntry,
       "wtWebGraphAirQualityTempValue": wtWebGraphAirQualityTempValue,
       "wtWebGraphAirQualityBinaryTempValueTable": wtWebGraphAirQualityBinaryTempValueTable,
       "wtWebGraphAirQualityBinaryTempValueEntry": wtWebGraphAirQualityBinaryTempValueEntry,
       "wtWebGraphAirQualityBinaryTempValue": wtWebGraphAirQualityBinaryTempValue,
       "wtWebGraphAirQualityTempValuePktTable": wtWebGraphAirQualityTempValuePktTable,
       "wtWebGraphAirQualityTempValuePktEntry": wtWebGraphAirQualityTempValuePktEntry,
       "wtWebGraphAirQualityTempValuePkt": wtWebGraphAirQualityTempValuePkt,
       "wtWebGraphAirQualitySessCntrl": wtWebGraphAirQualitySessCntrl,
       "wtWebGraphAirQualitySessCntrlPassword": wtWebGraphAirQualitySessCntrlPassword,
       "wtWebGraphAirQualitySessCntrlConfigMode": wtWebGraphAirQualitySessCntrlConfigMode,
       "wtWebGraphAirQualitySessCntrlLogout": wtWebGraphAirQualitySessCntrlLogout,
       "wtWebGraphAirQualitySessCntrlAdminPassword": wtWebGraphAirQualitySessCntrlAdminPassword,
       "wtWebGraphAirQualitySessCntrlConfigPassword": wtWebGraphAirQualitySessCntrlConfigPassword,
       "wtWebGraphAirQualityConfig": wtWebGraphAirQualityConfig,
       "wtWebGraphAirQualityDevice": wtWebGraphAirQualityDevice,
       "wtWebGraphAirQualityText": wtWebGraphAirQualityText,
       "wtWebGraphAirQualityDeviceName": wtWebGraphAirQualityDeviceName,
       "wtWebGraphAirQualityDeviceText": wtWebGraphAirQualityDeviceText,
       "wtWebGraphAirQualityDeviceLocation": wtWebGraphAirQualityDeviceLocation,
       "wtWebGraphAirQualityDeviceContact": wtWebGraphAirQualityDeviceContact,
       "wtWebGraphAirQualityTimeDate": wtWebGraphAirQualityTimeDate,
       "wtWebGraphAirQualityTimeZone": wtWebGraphAirQualityTimeZone,
       "wtWebGraphAirQualityTzOffsetHrs": wtWebGraphAirQualityTzOffsetHrs,
       "wtWebGraphAirQualityTzOffsetMin": wtWebGraphAirQualityTzOffsetMin,
       "wtWebGraphAirQualityTzEnable": wtWebGraphAirQualityTzEnable,
       "wtWebGraphAirQualityStTzOffsetHrs": wtWebGraphAirQualityStTzOffsetHrs,
       "wtWebGraphAirQualityStTzOffsetMin": wtWebGraphAirQualityStTzOffsetMin,
       "wtWebGraphAirQualityStTzEnable": wtWebGraphAirQualityStTzEnable,
       "wtWebGraphAirQualityStTzStartMonth": wtWebGraphAirQualityStTzStartMonth,
       "wtWebGraphAirQualityStTzStartMode": wtWebGraphAirQualityStTzStartMode,
       "wtWebGraphAirQualityStTzStartWday": wtWebGraphAirQualityStTzStartWday,
       "wtWebGraphAirQualityStTzStartHrs": wtWebGraphAirQualityStTzStartHrs,
       "wtWebGraphAirQualityStTzStartMin": wtWebGraphAirQualityStTzStartMin,
       "wtWebGraphAirQualityStTzStopMonth": wtWebGraphAirQualityStTzStopMonth,
       "wtWebGraphAirQualityStTzStopMode": wtWebGraphAirQualityStTzStopMode,
       "wtWebGraphAirQualityStTzStopWday": wtWebGraphAirQualityStTzStopWday,
       "wtWebGraphAirQualityStTzStopHrs": wtWebGraphAirQualityStTzStopHrs,
       "wtWebGraphAirQualityStTzStopMin": wtWebGraphAirQualityStTzStopMin,
       "wtWebGraphAirQualityTimeServer": wtWebGraphAirQualityTimeServer,
       "wtWebGraphAirQualityTimeServer1": wtWebGraphAirQualityTimeServer1,
       "wtWebGraphAirQualityTimeServer2": wtWebGraphAirQualityTimeServer2,
       "wtWebGraphAirQualityTsEnable": wtWebGraphAirQualityTsEnable,
       "wtWebGraphAirQualityTsSyncTime": wtWebGraphAirQualityTsSyncTime,
       "wtWebGraphAirQualityDeviceClock": wtWebGraphAirQualityDeviceClock,
       "wtWebGraphAirQualityClockHrs": wtWebGraphAirQualityClockHrs,
       "wtWebGraphAirQualityClockMin": wtWebGraphAirQualityClockMin,
       "wtWebGraphAirQualityClockDay": wtWebGraphAirQualityClockDay,
       "wtWebGraphAirQualityClockMonth": wtWebGraphAirQualityClockMonth,
       "wtWebGraphAirQualityClockYear": wtWebGraphAirQualityClockYear,
       "wtWebGraphAirQualityBasic": wtWebGraphAirQualityBasic,
       "wtWebGraphAirQualityNetwork": wtWebGraphAirQualityNetwork,
       "wtWebGraphAirQualityIpAddress": wtWebGraphAirQualityIpAddress,
       "wtWebGraphAirQualitySubnetMask": wtWebGraphAirQualitySubnetMask,
       "wtWebGraphAirQualityGateway": wtWebGraphAirQualityGateway,
       "wtWebGraphAirQualityDnsServer1": wtWebGraphAirQualityDnsServer1,
       "wtWebGraphAirQualityDnsServer2": wtWebGraphAirQualityDnsServer2,
       "wtWebGraphAirQualityAddConfig": wtWebGraphAirQualityAddConfig,
       "wtWebGraphAirQualityHTTP": wtWebGraphAirQualityHTTP,
       "wtWebGraphAirQualityStartup": wtWebGraphAirQualityStartup,
       "wtWebGraphAirQualityGetHeaderEnable": wtWebGraphAirQualityGetHeaderEnable,
       "wtWebGraphAirQualityHttpPort": wtWebGraphAirQualityHttpPort,
       "wtWebGraphAirQualityMail": wtWebGraphAirQualityMail,
       "wtWebGraphAirQualityMailAdName": wtWebGraphAirQualityMailAdName,
       "wtWebGraphAirQualityMailReply": wtWebGraphAirQualityMailReply,
       "wtWebGraphAirQualityMailServer": wtWebGraphAirQualityMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphAirQualityMailAuthentication": wtWebGraphAirQualityMailAuthentication,
       "wtWebGraphAirQualityMailAuthUser": wtWebGraphAirQualityMailAuthUser,
       "wtWebGraphAirQualityMailAuthPassword": wtWebGraphAirQualityMailAuthPassword,
       "wtWebGraphAirQualityMailPop3Server": wtWebGraphAirQualityMailPop3Server,
       "wtWebGraphAirQualitySNMP": wtWebGraphAirQualitySNMP,
       "wtWebGraphAirQualitySnmpCommunityStringRead": wtWebGraphAirQualitySnmpCommunityStringRead,
       "wtWebGraphAirQualitySnmpCommunityStringReadWrite": wtWebGraphAirQualitySnmpCommunityStringReadWrite,
       "wtWebGraphAirQualitySystemTrapManagerIP": wtWebGraphAirQualitySystemTrapManagerIP,
       "wtWebGraphAirQualitySystemTrapEnable": wtWebGraphAirQualitySystemTrapEnable,
       "wtWebGraphAirQualitySnmpEnable": wtWebGraphAirQualitySnmpEnable,
       "wtWebGraphAirQualitySnmpCommunityStringTrap": wtWebGraphAirQualitySnmpCommunityStringTrap,
       "wtWebGraphAirQualityUDP": wtWebGraphAirQualityUDP,
       "wtWebGraphAirQualityUdpPort": wtWebGraphAirQualityUdpPort,
       "wtWebGraphAirQualityUdpEnable": wtWebGraphAirQualityUdpEnable,
       "wtWebGraphAirQualitySyslog": wtWebGraphAirQualitySyslog,
       "wtWebGraphAirQualitySyslogServerIP": wtWebGraphAirQualitySyslogServerIP,
       "wtWebGraphAirQualitySyslogServerPort": wtWebGraphAirQualitySyslogServerPort,
       "wtWebGraphAirQualitySyslogSystemMessagesEnable": wtWebGraphAirQualitySyslogSystemMessagesEnable,
       "wtWebGraphAirQualitySyslogEnable": wtWebGraphAirQualitySyslogEnable,
       "wtWebGraphAirQualityFTP": wtWebGraphAirQualityFTP,
       "wtWebGraphAirQualityFTPServerIP": wtWebGraphAirQualityFTPServerIP,
       "wtWebGraphAirQualityFTPServerControlPort": wtWebGraphAirQualityFTPServerControlPort,
       "wtWebGraphAirQualityFTPUserName": wtWebGraphAirQualityFTPUserName,
       "wtWebGraphAirQualityFTPPassword": wtWebGraphAirQualityFTPPassword,
       "wtWebGraphAirQualityFTPAccount": wtWebGraphAirQualityFTPAccount,
       "wtWebGraphAirQualityFTPOption": wtWebGraphAirQualityFTPOption,
       "wtWebGraphAirQualityFTPEnable": wtWebGraphAirQualityFTPEnable,
       "wtWebGraphAirQualityRSS": wtWebGraphAirQualityRSS,
       "wtWebGraphAirQualityRSSChannelTitle": wtWebGraphAirQualityRSSChannelTitle,
       "wtWebGraphAirQualityRSSChannelLink": wtWebGraphAirQualityRSSChannelLink,
       "wtWebGraphAirQualityRSSChannelDescription": wtWebGraphAirQualityRSSChannelDescription,
       "wtWebGraphAirQualityRSSChannelImage": wtWebGraphAirQualityRSSChannelImage,
       "wtWebGraphAirQualityRSSChannelImageTitle": wtWebGraphAirQualityRSSChannelImageTitle,
       "wtWebGraphAirQualityRSSChannelImageLink": wtWebGraphAirQualityRSSChannelImageLink,
       "wtWebGraphAirQualityRSSChannelItemTitle": wtWebGraphAirQualityRSSChannelItemTitle,
       "wtWebGraphAirQualityRSSChannelItemLink": wtWebGraphAirQualityRSSChannelItemLink,
       "wtWebGraphAirQualityRSSChannelItemDescription": wtWebGraphAirQualityRSSChannelItemDescription,
       "wtWebGraphAirQualityRSSChannelItemQuantity": wtWebGraphAirQualityRSSChannelItemQuantity,
       "wtWebGraphAirQualityLedLights": wtWebGraphAirQualityLedLights,
       "wtWebGraphAirQualityLedLightsSensorSel": wtWebGraphAirQualityLedLightsSensorSel,
       "wtWebGraphAirQualityLedLightsLimitGreen": wtWebGraphAirQualityLedLightsLimitGreen,
       "wtWebGraphAirQualityLedLightsLimitYellow": wtWebGraphAirQualityLedLightsLimitYellow,
       "wtWebGraphAirQualityLedLightsLimitRed": wtWebGraphAirQualityLedLightsLimitRed,
       "wtWebGraphAirQualityDatalogger": wtWebGraphAirQualityDatalogger,
       "wtWebGraphAirQualityLoggerTimebase": wtWebGraphAirQualityLoggerTimebase,
       "wtWebGraphAirQualityLoggerSensorSel": wtWebGraphAirQualityLoggerSensorSel,
       "wtWebGraphAirQualityAlarm": wtWebGraphAirQualityAlarm,
       "wtWebGraphAirQualityAlarmCount": wtWebGraphAirQualityAlarmCount,
       "wtWebGraphAirQualityAlarmIfTable": wtWebGraphAirQualityAlarmIfTable,
       "wtWebGraphAirQualityAlarmIfEntry": wtWebGraphAirQualityAlarmIfEntry,
       "wtWebGraphAirQualityAlarmNo": wtWebGraphAirQualityAlarmNo,
       "wtWebGraphAirQualityAlarmTable": wtWebGraphAirQualityAlarmTable,
       "wtWebGraphAirQualityAlarmEntry": wtWebGraphAirQualityAlarmEntry,
       "wtWebGraphAirQualityAlarmTrigger": wtWebGraphAirQualityAlarmTrigger,
       "wtWebGraphAirQualityAlarmMin": wtWebGraphAirQualityAlarmMin,
       "wtWebGraphAirQualityAlarmMax": wtWebGraphAirQualityAlarmMax,
       "wtWebGraphAirQualityAlarmHysteresis": wtWebGraphAirQualityAlarmHysteresis,
       "wtWebGraphAirQualityAlarmDelay": wtWebGraphAirQualityAlarmDelay,
       "wtWebGraphAirQualityAlarmInterval": wtWebGraphAirQualityAlarmInterval,
       "wtWebGraphAirQualityAlarmEnable": wtWebGraphAirQualityAlarmEnable,
       "wtWebGraphAirQualityAlarmEMailAddr": wtWebGraphAirQualityAlarmEMailAddr,
       "wtWebGraphAirQualityAlarmMailSubject": wtWebGraphAirQualityAlarmMailSubject,
       "wtWebGraphAirQualityAlarmMailText": wtWebGraphAirQualityAlarmMailText,
       "wtWebGraphAirQualityAlarmManagerIP": wtWebGraphAirQualityAlarmManagerIP,
       "wtWebGraphAirQualityAlarmTrapText": wtWebGraphAirQualityAlarmTrapText,
       "wtWebGraphAirQualityAlarmMailOptions": wtWebGraphAirQualityAlarmMailOptions,
       "wtWebGraphAirQualityAlarmTcpIpAddr": wtWebGraphAirQualityAlarmTcpIpAddr,
       "wtWebGraphAirQualityAlarmTcpPort": wtWebGraphAirQualityAlarmTcpPort,
       "wtWebGraphAirQualityAlarmTcpText": wtWebGraphAirQualityAlarmTcpText,
       "wtWebGraphAirQualityAlarmClearMailSubject": wtWebGraphAirQualityAlarmClearMailSubject,
       "wtWebGraphAirQualityAlarmClearMailText": wtWebGraphAirQualityAlarmClearMailText,
       "wtWebGraphAirQualityAlarmClearTrapText": wtWebGraphAirQualityAlarmClearTrapText,
       "wtWebGraphAirQualityAlarmClearTcpText": wtWebGraphAirQualityAlarmClearTcpText,
       "wtWebGraphAirQualityAlarmDeltaTemp": wtWebGraphAirQualityAlarmDeltaTemp,
       "wtWebGraphAirQualityAlarmRHMin": wtWebGraphAirQualityAlarmRHMin,
       "wtWebGraphAirQualityAlarmRHMax": wtWebGraphAirQualityAlarmRHMax,
       "wtWebGraphAirQualityAlarmRHHysteresis": wtWebGraphAirQualityAlarmRHHysteresis,
       "wtWebGraphAirQualityAlarmAHMin": wtWebGraphAirQualityAlarmAHMin,
       "wtWebGraphAirQualityAlarmAHMax": wtWebGraphAirQualityAlarmAHMax,
       "wtWebGraphAirQualityAlarmSyslogIpAddr": wtWebGraphAirQualityAlarmSyslogIpAddr,
       "wtWebGraphAirQualityAlarmSyslogPort": wtWebGraphAirQualityAlarmSyslogPort,
       "wtWebGraphAirQualityAlarmSyslogText": wtWebGraphAirQualityAlarmSyslogText,
       "wtWebGraphAirQualityAlarmSyslogClearText": wtWebGraphAirQualityAlarmSyslogClearText,
       "wtWebGraphAirQualityAlarmFtpDataPort": wtWebGraphAirQualityAlarmFtpDataPort,
       "wtWebGraphAirQualityAlarmFtpFileName": wtWebGraphAirQualityAlarmFtpFileName,
       "wtWebGraphAirQualityAlarmFtpText": wtWebGraphAirQualityAlarmFtpText,
       "wtWebGraphAirQualityAlarmFtpClearText": wtWebGraphAirQualityAlarmFtpClearText,
       "wtWebGraphAirQualityAlarmFtpOption": wtWebGraphAirQualityAlarmFtpOption,
       "wtWebGraphAirQualityAlarmTimerCron": wtWebGraphAirQualityAlarmTimerCron,
       "wtWebGraphAirQualityAlarmVocMax": wtWebGraphAirQualityAlarmVocMax,
       "wtWebGraphAirQualityAlarmVocHysteresis": wtWebGraphAirQualityAlarmVocHysteresis,
       "wtWebGraphAirQualityAlarmName": wtWebGraphAirQualityAlarmName,
       "wtWebGraphAirQualityAlarmActive": wtWebGraphAirQualityAlarmActive,
       "wtWebGraphAirQualityGraphics": wtWebGraphAirQualityGraphics,
       "wtWebGraphAirQualityGraphicsBase": wtWebGraphAirQualityGraphicsBase,
       "wtWebGraphAirQualityGraphicsBaseEnable": wtWebGraphAirQualityGraphicsBaseEnable,
       "wtWebGraphAirQualityGraphicsBaseWidth": wtWebGraphAirQualityGraphicsBaseWidth,
       "wtWebGraphAirQualityGraphicsBaseHeight": wtWebGraphAirQualityGraphicsBaseHeight,
       "wtWebGraphAirQualityGraphicsBaseFrameColor": wtWebGraphAirQualityGraphicsBaseFrameColor,
       "wtWebGraphAirQualityGraphicsBaseBackgroundColor": wtWebGraphAirQualityGraphicsBaseBackgroundColor,
       "wtWebGraphAirQualityGraphicsBasePollingrate": wtWebGraphAirQualityGraphicsBasePollingrate,
       "wtWebGraphAirQualityGraphicsSelect": wtWebGraphAirQualityGraphicsSelect,
       "wtWebGraphAirQualityGraphicsSelectDisplaySensorSel": wtWebGraphAirQualityGraphicsSelectDisplaySensorSel,
       "wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem": wtWebGraphAirQualityGraphicsSelectDisplayShowExtrem,
       "wtWebGraphAirQualitySensorColorTable": wtWebGraphAirQualitySensorColorTable,
       "wtWebGraphAirQualitySensorColorEntry": wtWebGraphAirQualitySensorColorEntry,
       "wtWebGraphAirQualityGraphicsSensorColor": wtWebGraphAirQualityGraphicsSensorColor,
       "wtWebGraphAirQualityGraphicsSelectScale": wtWebGraphAirQualityGraphicsSelectScale,
       "wtWebGraphAirQualityGraphicsScale": wtWebGraphAirQualityGraphicsScale,
       "wtWebGraphAirQualityGraphicsScaleAutoScaleEnable": wtWebGraphAirQualityGraphicsScaleAutoScaleEnable,
       "wtWebGraphAirQualityGraphicsScaleAutoFitEnable": wtWebGraphAirQualityGraphicsScaleAutoFitEnable,
       "wtWebGraphAirQualityGraphicsScale1Min": wtWebGraphAirQualityGraphicsScale1Min,
       "wtWebGraphAirQualityGraphicsScale2Min": wtWebGraphAirQualityGraphicsScale2Min,
       "wtWebGraphAirQualityGraphicsScale3Min": wtWebGraphAirQualityGraphicsScale3Min,
       "wtWebGraphAirQualityGraphicsScale4Min": wtWebGraphAirQualityGraphicsScale4Min,
       "wtWebGraphAirQualityGraphicsScale1Max": wtWebGraphAirQualityGraphicsScale1Max,
       "wtWebGraphAirQualityGraphicsScale2Max": wtWebGraphAirQualityGraphicsScale2Max,
       "wtWebGraphAirQualityGraphicsScale3Max": wtWebGraphAirQualityGraphicsScale3Max,
       "wtWebGraphAirQualityGraphicsScale4Max": wtWebGraphAirQualityGraphicsScale4Max,
       "wtWebGraphAirQualityGraphicsScale1Unit": wtWebGraphAirQualityGraphicsScale1Unit,
       "wtWebGraphAirQualityGraphicsScale2Unit": wtWebGraphAirQualityGraphicsScale2Unit,
       "wtWebGraphAirQualityGraphicsScale3Unit": wtWebGraphAirQualityGraphicsScale3Unit,
       "wtWebGraphAirQualityGraphicsScale4Unit": wtWebGraphAirQualityGraphicsScale4Unit,
       "wtWebGraphAirQualityPorts": wtWebGraphAirQualityPorts,
       "wtWebGraphAirQualityPortTable": wtWebGraphAirQualityPortTable,
       "wtWebGraphAirQualityPortEntry": wtWebGraphAirQualityPortEntry,
       "wtWebGraphAirQualityPortName": wtWebGraphAirQualityPortName,
       "wtWebGraphAirQualityPortText": wtWebGraphAirQualityPortText,
       "wtWebGraphAirQualityPortOffset1": wtWebGraphAirQualityPortOffset1,
       "wtWebGraphAirQualityPortTemperature1": wtWebGraphAirQualityPortTemperature1,
       "wtWebGraphAirQualityPortOffset2": wtWebGraphAirQualityPortOffset2,
       "wtWebGraphAirQualityPortTemperature2": wtWebGraphAirQualityPortTemperature2,
       "wtWebGraphAirQualityPortComment": wtWebGraphAirQualityPortComment,
       "wtWebGraphAirQualityManufact": wtWebGraphAirQualityManufact,
       "wtWebGraphAirQualityMfName": wtWebGraphAirQualityMfName,
       "wtWebGraphAirQualityMfAddr": wtWebGraphAirQualityMfAddr,
       "wtWebGraphAirQualityMfHotline": wtWebGraphAirQualityMfHotline,
       "wtWebGraphAirQualityMfInternet": wtWebGraphAirQualityMfInternet,
       "wtWebGraphAirQualityMfDeviceTyp": wtWebGraphAirQualityMfDeviceTyp,
       "wtWebGraphAirQualityMfOrderNo": wtWebGraphAirQualityMfOrderNo,
       "wtWebGraphAirQualityDiag": wtWebGraphAirQualityDiag,
       "wtWebGraphAirQualityDiagErrorCount": wtWebGraphAirQualityDiagErrorCount,
       "wtWebGraphAirQualityDiagBinaryError": wtWebGraphAirQualityDiagBinaryError,
       "wtWebGraphAirQualityDiagErrorIndex": wtWebGraphAirQualityDiagErrorIndex,
       "wtWebGraphAirQualityDiagErrorMessage": wtWebGraphAirQualityDiagErrorMessage,
       "wtWebGraphAirQualityDiagErrorClear": wtWebGraphAirQualityDiagErrorClear}
)
