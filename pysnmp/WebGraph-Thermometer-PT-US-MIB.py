# SNMP MIB module (WebGraph-Thermometer-PT-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebGraph-Thermometer-PT-US-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:40 2024
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
_WtWebioAn1GraphPt_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPt = _WtWebioAn1GraphPt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17)
)
_WtWebioAn1GraphPtTemp_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtTemp = _WtWebioAn1GraphPtTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1)
)


class _WtWebioAn1GraphPtSensors_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSensors_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSensors_Object = MibScalar
wtWebioAn1GraphPtSensors = _WtWebioAn1GraphPtSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 1),
    _WtWebioAn1GraphPtSensors_Type()
)
wtWebioAn1GraphPtSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensors.setStatus("mandatory")
_WtWebioAn1GraphPtSensorTable_Object = MibTable
wtWebioAn1GraphPtSensorTable = _WtWebioAn1GraphPtSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorTable.setStatus("mandatory")
_WtWebioAn1GraphPtSensorEntry_Object = MibTableRow
wtWebioAn1GraphPtSensorEntry = _WtWebioAn1GraphPtSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 2, 1)
)
wtWebioAn1GraphPtSensorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSensorNo_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSensorNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSensorNo_Object = MibTableColumn
wtWebioAn1GraphPtSensorNo = _WtWebioAn1GraphPtSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 2, 1, 1),
    _WtWebioAn1GraphPtSensorNo_Type()
)
wtWebioAn1GraphPtSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorNo.setStatus("mandatory")
_WtWebioAn1GraphPtTempValueTable_Object = MibTable
wtWebioAn1GraphPtTempValueTable = _WtWebioAn1GraphPtTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphPtTempValueEntry_Object = MibTableRow
wtWebioAn1GraphPtTempValueEntry = _WtWebioAn1GraphPtTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 3, 1)
)
wtWebioAn1GraphPtTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValueEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtTempValue_Type(OctetString):
    """Custom type wtWebioAn1GraphPtTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebioAn1GraphPtTempValue_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtTempValue_Object = MibTableColumn
wtWebioAn1GraphPtTempValue = _WtWebioAn1GraphPtTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 3, 1, 1),
    _WtWebioAn1GraphPtTempValue_Type()
)
wtWebioAn1GraphPtTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValue.setStatus("mandatory")
_WtWebioAn1GraphPtBinaryTempValueTable_Object = MibTable
wtWebioAn1GraphPtBinaryTempValueTable = _WtWebioAn1GraphPtBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtBinaryTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphPtBinaryTempValueEntry_Object = MibTableRow
wtWebioAn1GraphPtBinaryTempValueEntry = _WtWebioAn1GraphPtBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 4, 1)
)
wtWebioAn1GraphPtBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtBinaryTempValueEntry.setStatus("mandatory")
_WtWebioAn1GraphPtBinaryTempValue_Type = Integer32
_WtWebioAn1GraphPtBinaryTempValue_Object = MibTableColumn
wtWebioAn1GraphPtBinaryTempValue = _WtWebioAn1GraphPtBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 4, 1, 1),
    _WtWebioAn1GraphPtBinaryTempValue_Type()
)
wtWebioAn1GraphPtBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtBinaryTempValue.setStatus("mandatory")
_WtWebioAn1GraphPtTempValuePktTable_Object = MibTable
wtWebioAn1GraphPtTempValuePktTable = _WtWebioAn1GraphPtTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValuePktTable.setStatus("mandatory")
_WtWebioAn1GraphPtTempValuePktEntry_Object = MibTableRow
wtWebioAn1GraphPtTempValuePktEntry = _WtWebioAn1GraphPtTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 8, 1)
)
wtWebioAn1GraphPtTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValuePktEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtTempValuePkt_Type(OctetString):
    """Custom type wtWebioAn1GraphPtTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebioAn1GraphPtTempValuePkt_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtTempValuePkt_Object = MibTableColumn
wtWebioAn1GraphPtTempValuePkt = _WtWebioAn1GraphPtTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 1, 8, 1, 1),
    _WtWebioAn1GraphPtTempValuePkt_Type()
)
wtWebioAn1GraphPtTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTempValuePkt.setStatus("mandatory")
_WtWebioAn1GraphPtSessCntrl_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSessCntrl = _WtWebioAn1GraphPtSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2)
)
_WtWebioAn1GraphPtSessCntrlPassword_Type = OctetString
_WtWebioAn1GraphPtSessCntrlPassword_Object = MibScalar
wtWebioAn1GraphPtSessCntrlPassword = _WtWebioAn1GraphPtSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2, 1),
    _WtWebioAn1GraphPtSessCntrlPassword_Type()
)
wtWebioAn1GraphPtSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSessCntrlPassword.setStatus("mandatory")


class _WtWebioAn1GraphPtSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphPtSessCntrl-NoSession", 0),
          ("wtWebioAn1GraphPtSessCntrl-Session", 1))
    )


_WtWebioAn1GraphPtSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSessCntrlConfigMode_Object = MibScalar
wtWebioAn1GraphPtSessCntrlConfigMode = _WtWebioAn1GraphPtSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2, 2),
    _WtWebioAn1GraphPtSessCntrlConfigMode_Type()
)
wtWebioAn1GraphPtSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSessCntrlConfigMode.setStatus("mandatory")
_WtWebioAn1GraphPtSessCntrlLogout_Type = Integer32
_WtWebioAn1GraphPtSessCntrlLogout_Object = MibScalar
wtWebioAn1GraphPtSessCntrlLogout = _WtWebioAn1GraphPtSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2, 3),
    _WtWebioAn1GraphPtSessCntrlLogout_Type()
)
wtWebioAn1GraphPtSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSessCntrlLogout.setStatus("mandatory")
_WtWebioAn1GraphPtSessCntrlAdminPassword_Type = OctetString
_WtWebioAn1GraphPtSessCntrlAdminPassword_Object = MibScalar
wtWebioAn1GraphPtSessCntrlAdminPassword = _WtWebioAn1GraphPtSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2, 4),
    _WtWebioAn1GraphPtSessCntrlAdminPassword_Type()
)
wtWebioAn1GraphPtSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSessCntrlAdminPassword.setStatus("mandatory")
_WtWebioAn1GraphPtSessCntrlConfigPassword_Type = OctetString
_WtWebioAn1GraphPtSessCntrlConfigPassword_Object = MibScalar
wtWebioAn1GraphPtSessCntrlConfigPassword = _WtWebioAn1GraphPtSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 2, 5),
    _WtWebioAn1GraphPtSessCntrlConfigPassword_Type()
)
wtWebioAn1GraphPtSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSessCntrlConfigPassword.setStatus("mandatory")
_WtWebioAn1GraphPtConfig_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtConfig = _WtWebioAn1GraphPtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3)
)
_WtWebioAn1GraphPtDevice_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtDevice = _WtWebioAn1GraphPtDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1)
)
_WtWebioAn1GraphPtText_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtText = _WtWebioAn1GraphPtText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 1)
)
_WtWebioAn1GraphPtDeviceName_Type = OctetString
_WtWebioAn1GraphPtDeviceName_Object = MibScalar
wtWebioAn1GraphPtDeviceName = _WtWebioAn1GraphPtDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 1, 1),
    _WtWebioAn1GraphPtDeviceName_Type()
)
wtWebioAn1GraphPtDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDeviceName.setStatus("mandatory")
_WtWebioAn1GraphPtDeviceText_Type = OctetString
_WtWebioAn1GraphPtDeviceText_Object = MibScalar
wtWebioAn1GraphPtDeviceText = _WtWebioAn1GraphPtDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 1, 2),
    _WtWebioAn1GraphPtDeviceText_Type()
)
wtWebioAn1GraphPtDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDeviceText.setStatus("mandatory")
_WtWebioAn1GraphPtDeviceLocation_Type = OctetString
_WtWebioAn1GraphPtDeviceLocation_Object = MibScalar
wtWebioAn1GraphPtDeviceLocation = _WtWebioAn1GraphPtDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 1, 3),
    _WtWebioAn1GraphPtDeviceLocation_Type()
)
wtWebioAn1GraphPtDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDeviceLocation.setStatus("mandatory")
_WtWebioAn1GraphPtDeviceContact_Type = OctetString
_WtWebioAn1GraphPtDeviceContact_Object = MibScalar
wtWebioAn1GraphPtDeviceContact = _WtWebioAn1GraphPtDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 1, 4),
    _WtWebioAn1GraphPtDeviceContact_Type()
)
wtWebioAn1GraphPtDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDeviceContact.setStatus("mandatory")
_WtWebioAn1GraphPtTimeDate_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtTimeDate = _WtWebioAn1GraphPtTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2)
)
_WtWebioAn1GraphPtTimeZone_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtTimeZone = _WtWebioAn1GraphPtTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1)
)
_WtWebioAn1GraphPtTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphPtTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphPtTzOffsetHrs = _WtWebioAn1GraphPtTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 1),
    _WtWebioAn1GraphPtTzOffsetHrs_Type()
)
wtWebioAn1GraphPtTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphPtTzOffsetMin_Type = Integer32
_WtWebioAn1GraphPtTzOffsetMin_Object = MibScalar
wtWebioAn1GraphPtTzOffsetMin = _WtWebioAn1GraphPtTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 2),
    _WtWebioAn1GraphPtTzOffsetMin_Type()
)
wtWebioAn1GraphPtTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphPtTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtTzEnable_Object = MibScalar
wtWebioAn1GraphPtTzEnable = _WtWebioAn1GraphPtTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 3),
    _WtWebioAn1GraphPtTzEnable_Type()
)
wtWebioAn1GraphPtTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTzEnable.setStatus("mandatory")
_WtWebioAn1GraphPtStTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphPtStTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphPtStTzOffsetHrs = _WtWebioAn1GraphPtStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 4),
    _WtWebioAn1GraphPtStTzOffsetHrs_Type()
)
wtWebioAn1GraphPtStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphPtStTzOffsetMin_Type = Integer32
_WtWebioAn1GraphPtStTzOffsetMin_Object = MibScalar
wtWebioAn1GraphPtStTzOffsetMin = _WtWebioAn1GraphPtStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 5),
    _WtWebioAn1GraphPtStTzOffsetMin_Type()
)
wtWebioAn1GraphPtStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtStTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtStTzEnable_Object = MibScalar
wtWebioAn1GraphPtStTzEnable = _WtWebioAn1GraphPtStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 6),
    _WtWebioAn1GraphPtStTzEnable_Type()
)
wtWebioAn1GraphPtStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStartMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStartMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtStartMonth-April", 4),
          ("wtWebioAn1GraphPtStartMonth-August", 8),
          ("wtWebioAn1GraphPtStartMonth-December", 12),
          ("wtWebioAn1GraphPtStartMonth-February", 2),
          ("wtWebioAn1GraphPtStartMonth-January", 1),
          ("wtWebioAn1GraphPtStartMonth-July", 7),
          ("wtWebioAn1GraphPtStartMonth-June", 6),
          ("wtWebioAn1GraphPtStartMonth-March", 3),
          ("wtWebioAn1GraphPtStartMonth-May", 5),
          ("wtWebioAn1GraphPtStartMonth-November", 11),
          ("wtWebioAn1GraphPtStartMonth-October", 10),
          ("wtWebioAn1GraphPtStartMonth-September", 9))
    )


_WtWebioAn1GraphPtStTzStartMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStartMonth_Object = MibScalar
wtWebioAn1GraphPtStTzStartMonth = _WtWebioAn1GraphPtStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 7),
    _WtWebioAn1GraphPtStTzStartMonth_Type()
)
wtWebioAn1GraphPtStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStartMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStartMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStartMode based on Integer32"""
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
        *(("wtWebioAn1GraphPtStartMode-first", 1),
          ("wtWebioAn1GraphPtStartMode-fourth", 4),
          ("wtWebioAn1GraphPtStartMode-last", 5),
          ("wtWebioAn1GraphPtStartMode-second", 2),
          ("wtWebioAn1GraphPtStartMode-third", 3))
    )


_WtWebioAn1GraphPtStTzStartMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStartMode_Object = MibScalar
wtWebioAn1GraphPtStTzStartMode = _WtWebioAn1GraphPtStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 8),
    _WtWebioAn1GraphPtStTzStartMode_Type()
)
wtWebioAn1GraphPtStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStartMode.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStartWday_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStartWday based on Integer32"""
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
        *(("wtWebioAn1GraphPtStartWday-Friday", 6),
          ("wtWebioAn1GraphPtStartWday-Monday", 2),
          ("wtWebioAn1GraphPtStartWday-Saturday", 7),
          ("wtWebioAn1GraphPtStartWday-Sunday", 1),
          ("wtWebioAn1GraphPtStartWday-Thursday", 4),
          ("wtWebioAn1GraphPtStartWday-Tuesday", 3),
          ("wtWebioAn1GraphPtStartWday-Wednesday", 5))
    )


_WtWebioAn1GraphPtStTzStartWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStartWday_Object = MibScalar
wtWebioAn1GraphPtStTzStartWday = _WtWebioAn1GraphPtStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 9),
    _WtWebioAn1GraphPtStTzStartWday_Type()
)
wtWebioAn1GraphPtStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStartWday.setStatus("mandatory")
_WtWebioAn1GraphPtStTzStartHrs_Type = Integer32
_WtWebioAn1GraphPtStTzStartHrs_Object = MibScalar
wtWebioAn1GraphPtStTzStartHrs = _WtWebioAn1GraphPtStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 10),
    _WtWebioAn1GraphPtStTzStartHrs_Type()
)
wtWebioAn1GraphPtStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStartHrs.setStatus("mandatory")
_WtWebioAn1GraphPtStTzStartMin_Type = Integer32
_WtWebioAn1GraphPtStTzStartMin_Object = MibScalar
wtWebioAn1GraphPtStTzStartMin = _WtWebioAn1GraphPtStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 11),
    _WtWebioAn1GraphPtStTzStartMin_Type()
)
wtWebioAn1GraphPtStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStartMin.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStopMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStopMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtStopMonth-April", 4),
          ("wtWebioAn1GraphPtStopMonth-August", 8),
          ("wtWebioAn1GraphPtStopMonth-December", 12),
          ("wtWebioAn1GraphPtStopMonth-February", 2),
          ("wtWebioAn1GraphPtStopMonth-January", 1),
          ("wtWebioAn1GraphPtStopMonth-July", 7),
          ("wtWebioAn1GraphPtStopMonth-June", 6),
          ("wtWebioAn1GraphPtStopMonth-March", 3),
          ("wtWebioAn1GraphPtStopMonth-May", 5),
          ("wtWebioAn1GraphPtStopMonth-November", 11),
          ("wtWebioAn1GraphPtStopMonth-October", 10),
          ("wtWebioAn1GraphPtStopMonth-September", 9))
    )


_WtWebioAn1GraphPtStTzStopMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStopMonth_Object = MibScalar
wtWebioAn1GraphPtStTzStopMonth = _WtWebioAn1GraphPtStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 12),
    _WtWebioAn1GraphPtStTzStopMonth_Type()
)
wtWebioAn1GraphPtStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStopMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStopMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStopMode based on Integer32"""
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
        *(("wtWebioAn1GraphPtStopMode-first", 1),
          ("wtWebioAn1GraphPtStopMode-fourth", 4),
          ("wtWebioAn1GraphPtStopMode-last", 5),
          ("wtWebioAn1GraphPtStopMode-second", 2),
          ("wtWebioAn1GraphPtStopMode-third", 3))
    )


_WtWebioAn1GraphPtStTzStopMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStopMode_Object = MibScalar
wtWebioAn1GraphPtStTzStopMode = _WtWebioAn1GraphPtStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 13),
    _WtWebioAn1GraphPtStTzStopMode_Type()
)
wtWebioAn1GraphPtStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStopMode.setStatus("mandatory")


class _WtWebioAn1GraphPtStTzStopWday_Type(Integer32):
    """Custom type wtWebioAn1GraphPtStTzStopWday based on Integer32"""
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
        *(("wtWebioAn1GraphPtStopWday-Friday", 6),
          ("wtWebioAn1GraphPtStopWday-Monday", 2),
          ("wtWebioAn1GraphPtStopWday-Saturday", 7),
          ("wtWebioAn1GraphPtStopWday-Sunday", 1),
          ("wtWebioAn1GraphPtStopWday-Thursday", 4),
          ("wtWebioAn1GraphPtStopWday-Tuesday", 3),
          ("wtWebioAn1GraphPtStopWday-Wednesday", 5))
    )


_WtWebioAn1GraphPtStTzStopWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtStTzStopWday_Object = MibScalar
wtWebioAn1GraphPtStTzStopWday = _WtWebioAn1GraphPtStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 14),
    _WtWebioAn1GraphPtStTzStopWday_Type()
)
wtWebioAn1GraphPtStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStopWday.setStatus("mandatory")
_WtWebioAn1GraphPtStTzStopHrs_Type = Integer32
_WtWebioAn1GraphPtStTzStopHrs_Object = MibScalar
wtWebioAn1GraphPtStTzStopHrs = _WtWebioAn1GraphPtStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 15),
    _WtWebioAn1GraphPtStTzStopHrs_Type()
)
wtWebioAn1GraphPtStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStopHrs.setStatus("mandatory")
_WtWebioAn1GraphPtStTzStopMin_Type = Integer32
_WtWebioAn1GraphPtStTzStopMin_Object = MibScalar
wtWebioAn1GraphPtStTzStopMin = _WtWebioAn1GraphPtStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 1, 16),
    _WtWebioAn1GraphPtStTzStopMin_Type()
)
wtWebioAn1GraphPtStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStTzStopMin.setStatus("mandatory")
_WtWebioAn1GraphPtTimeServer_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtTimeServer = _WtWebioAn1GraphPtTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 2)
)
_WtWebioAn1GraphPtTimeServer1_Type = OctetString
_WtWebioAn1GraphPtTimeServer1_Object = MibScalar
wtWebioAn1GraphPtTimeServer1 = _WtWebioAn1GraphPtTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 2, 1),
    _WtWebioAn1GraphPtTimeServer1_Type()
)
wtWebioAn1GraphPtTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTimeServer1.setStatus("mandatory")
_WtWebioAn1GraphPtTimeServer2_Type = OctetString
_WtWebioAn1GraphPtTimeServer2_Object = MibScalar
wtWebioAn1GraphPtTimeServer2 = _WtWebioAn1GraphPtTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 2, 2),
    _WtWebioAn1GraphPtTimeServer2_Type()
)
wtWebioAn1GraphPtTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTimeServer2.setStatus("mandatory")


class _WtWebioAn1GraphPtTsEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtTsEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtTsEnable_Object = MibScalar
wtWebioAn1GraphPtTsEnable = _WtWebioAn1GraphPtTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 2, 3),
    _WtWebioAn1GraphPtTsEnable_Type()
)
wtWebioAn1GraphPtTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTsEnable.setStatus("mandatory")
_WtWebioAn1GraphPtTsSyncTime_Type = Integer32
_WtWebioAn1GraphPtTsSyncTime_Object = MibScalar
wtWebioAn1GraphPtTsSyncTime = _WtWebioAn1GraphPtTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 2, 4),
    _WtWebioAn1GraphPtTsSyncTime_Type()
)
wtWebioAn1GraphPtTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtTsSyncTime.setStatus("mandatory")
_WtWebioAn1GraphPtDeviceClock_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtDeviceClock = _WtWebioAn1GraphPtDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3)
)


class _WtWebioAn1GraphPtClockHrs_Type(Integer32):
    """Custom type wtWebioAn1GraphPtClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebioAn1GraphPtClockHrs_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtClockHrs_Object = MibScalar
wtWebioAn1GraphPtClockHrs = _WtWebioAn1GraphPtClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3, 1),
    _WtWebioAn1GraphPtClockHrs_Type()
)
wtWebioAn1GraphPtClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtClockHrs.setStatus("mandatory")


class _WtWebioAn1GraphPtClockMin_Type(Integer32):
    """Custom type wtWebioAn1GraphPtClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebioAn1GraphPtClockMin_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtClockMin_Object = MibScalar
wtWebioAn1GraphPtClockMin = _WtWebioAn1GraphPtClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3, 2),
    _WtWebioAn1GraphPtClockMin_Type()
)
wtWebioAn1GraphPtClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtClockMin.setStatus("mandatory")


class _WtWebioAn1GraphPtClockDay_Type(Integer32):
    """Custom type wtWebioAn1GraphPtClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebioAn1GraphPtClockDay_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtClockDay_Object = MibScalar
wtWebioAn1GraphPtClockDay = _WtWebioAn1GraphPtClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3, 3),
    _WtWebioAn1GraphPtClockDay_Type()
)
wtWebioAn1GraphPtClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtClockDay.setStatus("mandatory")


class _WtWebioAn1GraphPtClockMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtClockMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtClockMonth-April", 4),
          ("wtWebioAn1GraphPtClockMonth-August", 8),
          ("wtWebioAn1GraphPtClockMonth-December", 12),
          ("wtWebioAn1GraphPtClockMonth-February", 2),
          ("wtWebioAn1GraphPtClockMonth-January", 1),
          ("wtWebioAn1GraphPtClockMonth-July", 7),
          ("wtWebioAn1GraphPtClockMonth-June", 6),
          ("wtWebioAn1GraphPtClockMonth-March", 3),
          ("wtWebioAn1GraphPtClockMonth-May", 5),
          ("wtWebioAn1GraphPtClockMonth-November", 11),
          ("wtWebioAn1GraphPtClockMonth-October", 10),
          ("wtWebioAn1GraphPtClockMonth-September", 9))
    )


_WtWebioAn1GraphPtClockMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtClockMonth_Object = MibScalar
wtWebioAn1GraphPtClockMonth = _WtWebioAn1GraphPtClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3, 4),
    _WtWebioAn1GraphPtClockMonth_Type()
)
wtWebioAn1GraphPtClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtClockMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtClockYear_Type(Integer32):
    """Custom type wtWebioAn1GraphPtClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebioAn1GraphPtClockYear_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtClockYear_Object = MibScalar
wtWebioAn1GraphPtClockYear = _WtWebioAn1GraphPtClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 2, 3, 5),
    _WtWebioAn1GraphPtClockYear_Type()
)
wtWebioAn1GraphPtClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtClockYear.setStatus("mandatory")
_WtWebioAn1GraphPtBasic_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtBasic = _WtWebioAn1GraphPtBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3)
)
_WtWebioAn1GraphPtNetwork_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtNetwork = _WtWebioAn1GraphPtNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1)
)
_WtWebioAn1GraphPtIpAddress_Type = IpAddress
_WtWebioAn1GraphPtIpAddress_Object = MibScalar
wtWebioAn1GraphPtIpAddress = _WtWebioAn1GraphPtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 1),
    _WtWebioAn1GraphPtIpAddress_Type()
)
wtWebioAn1GraphPtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtIpAddress.setStatus("mandatory")
_WtWebioAn1GraphPtSubnetMask_Type = IpAddress
_WtWebioAn1GraphPtSubnetMask_Object = MibScalar
wtWebioAn1GraphPtSubnetMask = _WtWebioAn1GraphPtSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 2),
    _WtWebioAn1GraphPtSubnetMask_Type()
)
wtWebioAn1GraphPtSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSubnetMask.setStatus("mandatory")
_WtWebioAn1GraphPtGateway_Type = IpAddress
_WtWebioAn1GraphPtGateway_Object = MibScalar
wtWebioAn1GraphPtGateway = _WtWebioAn1GraphPtGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 3),
    _WtWebioAn1GraphPtGateway_Type()
)
wtWebioAn1GraphPtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGateway.setStatus("mandatory")
_WtWebioAn1GraphPtDnsServer1_Type = OctetString
_WtWebioAn1GraphPtDnsServer1_Object = MibScalar
wtWebioAn1GraphPtDnsServer1 = _WtWebioAn1GraphPtDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 4),
    _WtWebioAn1GraphPtDnsServer1_Type()
)
wtWebioAn1GraphPtDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDnsServer1.setStatus("mandatory")
_WtWebioAn1GraphPtDnsServer2_Type = OctetString
_WtWebioAn1GraphPtDnsServer2_Object = MibScalar
wtWebioAn1GraphPtDnsServer2 = _WtWebioAn1GraphPtDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 5),
    _WtWebioAn1GraphPtDnsServer2_Type()
)
wtWebioAn1GraphPtDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDnsServer2.setStatus("mandatory")
_WtWebioAn1GraphPtAddConfig_Type = OctetString
_WtWebioAn1GraphPtAddConfig_Object = MibScalar
wtWebioAn1GraphPtAddConfig = _WtWebioAn1GraphPtAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 1, 6),
    _WtWebioAn1GraphPtAddConfig_Type()
)
wtWebioAn1GraphPtAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAddConfig.setStatus("mandatory")
_WtWebioAn1GraphPtHTTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtHTTP = _WtWebioAn1GraphPtHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 2)
)
_WtWebioAn1GraphPtStartup_Type = OctetString
_WtWebioAn1GraphPtStartup_Object = MibScalar
wtWebioAn1GraphPtStartup = _WtWebioAn1GraphPtStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 2, 1),
    _WtWebioAn1GraphPtStartup_Type()
)
wtWebioAn1GraphPtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtStartup.setStatus("mandatory")
_WtWebioAn1GraphPtGetHeaderEnable_Type = OctetString
_WtWebioAn1GraphPtGetHeaderEnable_Object = MibScalar
wtWebioAn1GraphPtGetHeaderEnable = _WtWebioAn1GraphPtGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 2, 2),
    _WtWebioAn1GraphPtGetHeaderEnable_Type()
)
wtWebioAn1GraphPtGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGetHeaderEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtHttpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtHttpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtHttpPort_Object = MibScalar
wtWebioAn1GraphPtHttpPort = _WtWebioAn1GraphPtHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 2, 3),
    _WtWebioAn1GraphPtHttpPort_Type()
)
wtWebioAn1GraphPtHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtHttpPort.setStatus("mandatory")
_WtWebioAn1GraphPtMail_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtMail = _WtWebioAn1GraphPtMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3)
)
_WtWebioAn1GraphPtMailAdName_Type = OctetString
_WtWebioAn1GraphPtMailAdName_Object = MibScalar
wtWebioAn1GraphPtMailAdName = _WtWebioAn1GraphPtMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 1),
    _WtWebioAn1GraphPtMailAdName_Type()
)
wtWebioAn1GraphPtMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailAdName.setStatus("mandatory")
_WtWebioAn1GraphPtMailReply_Type = OctetString
_WtWebioAn1GraphPtMailReply_Object = MibScalar
wtWebioAn1GraphPtMailReply = _WtWebioAn1GraphPtMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 2),
    _WtWebioAn1GraphPtMailReply_Type()
)
wtWebioAn1GraphPtMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailReply.setStatus("mandatory")
_WtWebioAn1GraphPtMailServer_Type = OctetString
_WtWebioAn1GraphPtMailServer_Object = MibScalar
wtWebioAn1GraphPtMailServer = _WtWebioAn1GraphPtMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 3),
    _WtWebioAn1GraphPtMailServer_Type()
)
wtWebioAn1GraphPtMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailServer.setStatus("mandatory")
_WtWebioAn1GraphPtMailEnable_Type = OctetString
_WtWebioAn1GraphPtMailEnable_Object = MibScalar
wtWebioAn1GraphPtMailEnable = _WtWebioAn1GraphPtMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 4),
    _WtWebioAn1GraphPtMailEnable_Type()
)
wtWebioAn1GraphPtMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtMailAuthentication_Type(OctetString):
    """Custom type wtWebioAn1GraphPtMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtMailAuthentication_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtMailAuthentication_Object = MibScalar
wtWebioAn1GraphPtMailAuthentication = _WtWebioAn1GraphPtMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 5),
    _WtWebioAn1GraphPtMailAuthentication_Type()
)
wtWebioAn1GraphPtMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailAuthentication.setStatus("mandatory")
_WtWebioAn1GraphPtMailAuthUser_Type = OctetString
_WtWebioAn1GraphPtMailAuthUser_Object = MibScalar
wtWebioAn1GraphPtMailAuthUser = _WtWebioAn1GraphPtMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 6),
    _WtWebioAn1GraphPtMailAuthUser_Type()
)
wtWebioAn1GraphPtMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailAuthUser.setStatus("mandatory")
_WtWebioAn1GraphPtMailAuthPassword_Type = OctetString
_WtWebioAn1GraphPtMailAuthPassword_Object = MibScalar
wtWebioAn1GraphPtMailAuthPassword = _WtWebioAn1GraphPtMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 7),
    _WtWebioAn1GraphPtMailAuthPassword_Type()
)
wtWebioAn1GraphPtMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailAuthPassword.setStatus("mandatory")
_WtWebioAn1GraphPtMailPop3Server_Type = OctetString
_WtWebioAn1GraphPtMailPop3Server_Object = MibScalar
wtWebioAn1GraphPtMailPop3Server = _WtWebioAn1GraphPtMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 3, 8),
    _WtWebioAn1GraphPtMailPop3Server_Type()
)
wtWebioAn1GraphPtMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMailPop3Server.setStatus("mandatory")
_WtWebioAn1GraphPtSNMP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSNMP = _WtWebioAn1GraphPtSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4)
)
_WtWebioAn1GraphPtSnmpCommunityStringRead_Type = OctetString
_WtWebioAn1GraphPtSnmpCommunityStringRead_Object = MibScalar
wtWebioAn1GraphPtSnmpCommunityStringRead = _WtWebioAn1GraphPtSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 1),
    _WtWebioAn1GraphPtSnmpCommunityStringRead_Type()
)
wtWebioAn1GraphPtSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSnmpCommunityStringRead.setStatus("mandatory")
_WtWebioAn1GraphPtSnmpCommunityStringReadWrite_Type = OctetString
_WtWebioAn1GraphPtSnmpCommunityStringReadWrite_Object = MibScalar
wtWebioAn1GraphPtSnmpCommunityStringReadWrite = _WtWebioAn1GraphPtSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 2),
    _WtWebioAn1GraphPtSnmpCommunityStringReadWrite_Type()
)
wtWebioAn1GraphPtSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebioAn1GraphPtSystemTrapManagerIP_Type = OctetString
_WtWebioAn1GraphPtSystemTrapManagerIP_Object = MibScalar
wtWebioAn1GraphPtSystemTrapManagerIP = _WtWebioAn1GraphPtSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 3),
    _WtWebioAn1GraphPtSystemTrapManagerIP_Type()
)
wtWebioAn1GraphPtSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSystemTrapManagerIP.setStatus("mandatory")


class _WtWebioAn1GraphPtSystemTrapEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSystemTrapEnable_Object = MibScalar
wtWebioAn1GraphPtSystemTrapEnable = _WtWebioAn1GraphPtSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 4),
    _WtWebioAn1GraphPtSystemTrapEnable_Type()
)
wtWebioAn1GraphPtSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSystemTrapEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSnmpEnable_Type = OctetString
_WtWebioAn1GraphPtSnmpEnable_Object = MibScalar
wtWebioAn1GraphPtSnmpEnable = _WtWebioAn1GraphPtSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 5),
    _WtWebioAn1GraphPtSnmpEnable_Type()
)
wtWebioAn1GraphPtSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSnmpEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSnmpCommunityStringTrap_Type = OctetString
_WtWebioAn1GraphPtSnmpCommunityStringTrap_Object = MibScalar
wtWebioAn1GraphPtSnmpCommunityStringTrap = _WtWebioAn1GraphPtSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 4, 6),
    _WtWebioAn1GraphPtSnmpCommunityStringTrap_Type()
)
wtWebioAn1GraphPtSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebioAn1GraphPtUDP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtUDP = _WtWebioAn1GraphPtUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 5)
)


class _WtWebioAn1GraphPtUdpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtUdpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtUdpPort_Object = MibScalar
wtWebioAn1GraphPtUdpPort = _WtWebioAn1GraphPtUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 5, 1),
    _WtWebioAn1GraphPtUdpPort_Type()
)
wtWebioAn1GraphPtUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtUdpPort.setStatus("mandatory")
_WtWebioAn1GraphPtUdpEnable_Type = OctetString
_WtWebioAn1GraphPtUdpEnable_Object = MibScalar
wtWebioAn1GraphPtUdpEnable = _WtWebioAn1GraphPtUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 5, 2),
    _WtWebioAn1GraphPtUdpEnable_Type()
)
wtWebioAn1GraphPtUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtUdpEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSyslog_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSyslog = _WtWebioAn1GraphPtSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 6)
)
_WtWebioAn1GraphPtSyslogServerIP_Type = OctetString
_WtWebioAn1GraphPtSyslogServerIP_Object = MibScalar
wtWebioAn1GraphPtSyslogServerIP = _WtWebioAn1GraphPtSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 6, 1),
    _WtWebioAn1GraphPtSyslogServerIP_Type()
)
wtWebioAn1GraphPtSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSyslogServerIP.setStatus("mandatory")
_WtWebioAn1GraphPtSyslogServerPort_Type = Integer32
_WtWebioAn1GraphPtSyslogServerPort_Object = MibScalar
wtWebioAn1GraphPtSyslogServerPort = _WtWebioAn1GraphPtSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 6, 2),
    _WtWebioAn1GraphPtSyslogServerPort_Type()
)
wtWebioAn1GraphPtSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSyslogServerPort.setStatus("mandatory")


class _WtWebioAn1GraphPtSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSyslogSystemMessagesEnable_Object = MibScalar
wtWebioAn1GraphPtSyslogSystemMessagesEnable = _WtWebioAn1GraphPtSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 6, 3),
    _WtWebioAn1GraphPtSyslogSystemMessagesEnable_Type()
)
wtWebioAn1GraphPtSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSyslogEnable_Type = OctetString
_WtWebioAn1GraphPtSyslogEnable_Object = MibScalar
wtWebioAn1GraphPtSyslogEnable = _WtWebioAn1GraphPtSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 6, 4),
    _WtWebioAn1GraphPtSyslogEnable_Type()
)
wtWebioAn1GraphPtSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSyslogEnable.setStatus("mandatory")
_WtWebioAn1GraphPtFTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtFTP = _WtWebioAn1GraphPtFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7)
)
_WtWebioAn1GraphPtFTPServerIP_Type = OctetString
_WtWebioAn1GraphPtFTPServerIP_Object = MibScalar
wtWebioAn1GraphPtFTPServerIP = _WtWebioAn1GraphPtFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 1),
    _WtWebioAn1GraphPtFTPServerIP_Type()
)
wtWebioAn1GraphPtFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPServerIP.setStatus("mandatory")
_WtWebioAn1GraphPtFTPServerControlPort_Type = Integer32
_WtWebioAn1GraphPtFTPServerControlPort_Object = MibScalar
wtWebioAn1GraphPtFTPServerControlPort = _WtWebioAn1GraphPtFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 2),
    _WtWebioAn1GraphPtFTPServerControlPort_Type()
)
wtWebioAn1GraphPtFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPServerControlPort.setStatus("mandatory")
_WtWebioAn1GraphPtFTPUserName_Type = OctetString
_WtWebioAn1GraphPtFTPUserName_Object = MibScalar
wtWebioAn1GraphPtFTPUserName = _WtWebioAn1GraphPtFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 3),
    _WtWebioAn1GraphPtFTPUserName_Type()
)
wtWebioAn1GraphPtFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPUserName.setStatus("mandatory")
_WtWebioAn1GraphPtFTPPassword_Type = OctetString
_WtWebioAn1GraphPtFTPPassword_Object = MibScalar
wtWebioAn1GraphPtFTPPassword = _WtWebioAn1GraphPtFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 4),
    _WtWebioAn1GraphPtFTPPassword_Type()
)
wtWebioAn1GraphPtFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPPassword.setStatus("mandatory")
_WtWebioAn1GraphPtFTPAccount_Type = OctetString
_WtWebioAn1GraphPtFTPAccount_Object = MibScalar
wtWebioAn1GraphPtFTPAccount = _WtWebioAn1GraphPtFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 5),
    _WtWebioAn1GraphPtFTPAccount_Type()
)
wtWebioAn1GraphPtFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPAccount.setStatus("mandatory")
_WtWebioAn1GraphPtFTPOption_Type = OctetString
_WtWebioAn1GraphPtFTPOption_Object = MibScalar
wtWebioAn1GraphPtFTPOption = _WtWebioAn1GraphPtFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 6),
    _WtWebioAn1GraphPtFTPOption_Type()
)
wtWebioAn1GraphPtFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPOption.setStatus("mandatory")
_WtWebioAn1GraphPtFTPEnable_Type = OctetString
_WtWebioAn1GraphPtFTPEnable_Object = MibScalar
wtWebioAn1GraphPtFTPEnable = _WtWebioAn1GraphPtFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 7, 7),
    _WtWebioAn1GraphPtFTPEnable_Type()
)
wtWebioAn1GraphPtFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtFTPEnable.setStatus("mandatory")
_WtWebioAn1GraphPtLanguage_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtLanguage = _WtWebioAn1GraphPtLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 9)
)
_WtWebioAn1GraphPtLanguageSelect_Type = OctetString
_WtWebioAn1GraphPtLanguageSelect_Object = MibScalar
wtWebioAn1GraphPtLanguageSelect = _WtWebioAn1GraphPtLanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 3, 9, 1),
    _WtWebioAn1GraphPtLanguageSelect_Type()
)
wtWebioAn1GraphPtLanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtLanguageSelect.setStatus("mandatory")
_WtWebioAn1GraphPtDatalogger_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtDatalogger = _WtWebioAn1GraphPtDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4)
)


class _WtWebioAn1GraphPtLoggerTimebase_Type(Integer32):
    """Custom type wtWebioAn1GraphPtLoggerTimebase based on Integer32"""
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
        *(("wtWebioAn1GraphPtDatalogger-15Min", 3),
          ("wtWebioAn1GraphPtDatalogger-1Min", 1),
          ("wtWebioAn1GraphPtDatalogger-5Min", 2),
          ("wtWebioAn1GraphPtDatalogger-60Min", 4))
    )


_WtWebioAn1GraphPtLoggerTimebase_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtLoggerTimebase_Object = MibScalar
wtWebioAn1GraphPtLoggerTimebase = _WtWebioAn1GraphPtLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 1),
    _WtWebioAn1GraphPtLoggerTimebase_Type()
)
wtWebioAn1GraphPtLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtLoggerTimebase.setStatus("mandatory")


class _WtWebioAn1GraphPtLoggerSensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtLoggerSensorSel_Object = MibScalar
wtWebioAn1GraphPtLoggerSensorSel = _WtWebioAn1GraphPtLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 2),
    _WtWebioAn1GraphPtLoggerSensorSel_Type()
)
wtWebioAn1GraphPtLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtLoggerSensorSel.setStatus("mandatory")


class _WtWebioAn1GraphPtDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphPtDisplaySensorSel = _WtWebioAn1GraphPtDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 3),
    _WtWebioAn1GraphPtDisplaySensorSel_Type()
)
wtWebioAn1GraphPtDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDisplaySensorSel.setStatus("mandatory")
_WtWebioAn1GraphPtSensorColorTable_Object = MibTable
wtWebioAn1GraphPtSensorColorTable = _WtWebioAn1GraphPtSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphPtSensorColorEntry_Object = MibTableRow
wtWebioAn1GraphPtSensorColorEntry = _WtWebioAn1GraphPtSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 4, 1)
)
wtWebioAn1GraphPtSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSensorColor_Object = MibTableColumn
wtWebioAn1GraphPtSensorColor = _WtWebioAn1GraphPtSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 4, 1, 1),
    _WtWebioAn1GraphPtSensorColor_Type()
)
wtWebioAn1GraphPtSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSensorColor.setStatus("mandatory")
_WtWebioAn1GraphPtAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphPtAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphPtAutoScaleEnable = _WtWebioAn1GraphPtAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 5),
    _WtWebioAn1GraphPtAutoScaleEnable_Type()
)
wtWebioAn1GraphPtAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphPtVerticalUpperLimit_Type = OctetString
_WtWebioAn1GraphPtVerticalUpperLimit_Object = MibScalar
wtWebioAn1GraphPtVerticalUpperLimit = _WtWebioAn1GraphPtVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 6),
    _WtWebioAn1GraphPtVerticalUpperLimit_Type()
)
wtWebioAn1GraphPtVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtVerticalUpperLimit.setStatus("mandatory")
_WtWebioAn1GraphPtVerticalLowerLimit_Type = OctetString
_WtWebioAn1GraphPtVerticalLowerLimit_Object = MibScalar
wtWebioAn1GraphPtVerticalLowerLimit = _WtWebioAn1GraphPtVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 7),
    _WtWebioAn1GraphPtVerticalLowerLimit_Type()
)
wtWebioAn1GraphPtVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtVerticalLowerLimit.setStatus("mandatory")


class _WtWebioAn1GraphPtHorizontalZoom_Type(Integer32):
    """Custom type wtWebioAn1GraphPtHorizontalZoom based on Integer32"""
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
        *(("wtWebioAn1GraphPtZoom-25days", 6),
          ("wtWebioAn1GraphPtZoom-25min", 1),
          ("wtWebioAn1GraphPtZoom-30hrs", 4),
          ("wtWebioAn1GraphPtZoom-5days", 5),
          ("wtWebioAn1GraphPtZoom-5hrs", 3),
          ("wtWebioAn1GraphPtZoom-75min", 2))
    )


_WtWebioAn1GraphPtHorizontalZoom_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtHorizontalZoom_Object = MibScalar
wtWebioAn1GraphPtHorizontalZoom = _WtWebioAn1GraphPtHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 4, 8),
    _WtWebioAn1GraphPtHorizontalZoom_Type()
)
wtWebioAn1GraphPtHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtHorizontalZoom.setStatus("mandatory")
_WtWebioAn1GraphPtAlarm_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtAlarm = _WtWebioAn1GraphPtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5)
)


class _WtWebioAn1GraphPtAlarmCount_Type(Integer32):
    """Custom type wtWebioAn1GraphPtAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphPtAlarmCount_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtAlarmCount_Object = MibScalar
wtWebioAn1GraphPtAlarmCount = _WtWebioAn1GraphPtAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 1),
    _WtWebioAn1GraphPtAlarmCount_Type()
)
wtWebioAn1GraphPtAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmCount.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmIfTable_Object = MibTable
wtWebioAn1GraphPtAlarmIfTable = _WtWebioAn1GraphPtAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmIfTable.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmIfEntry_Object = MibTableRow
wtWebioAn1GraphPtAlarmIfEntry = _WtWebioAn1GraphPtAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 2, 1)
)
wtWebioAn1GraphPtAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmIfEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmNo_Type(Integer32):
    """Custom type wtWebioAn1GraphPtAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphPtAlarmNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtAlarmNo_Object = MibTableColumn
wtWebioAn1GraphPtAlarmNo = _WtWebioAn1GraphPtAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 2, 1, 1),
    _WtWebioAn1GraphPtAlarmNo_Type()
)
wtWebioAn1GraphPtAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmNo.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmTable_Object = MibTable
wtWebioAn1GraphPtAlarmTable = _WtWebioAn1GraphPtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTable.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmEntry_Object = MibTableRow
wtWebioAn1GraphPtAlarmEntry = _WtWebioAn1GraphPtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1)
)
wtWebioAn1GraphPtAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmTrigger_Type(OctetString):
    """Custom type wtWebioAn1GraphPtAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtAlarmTrigger_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtAlarmTrigger_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTrigger = _WtWebioAn1GraphPtAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 1),
    _WtWebioAn1GraphPtAlarmTrigger_Type()
)
wtWebioAn1GraphPtAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTrigger.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmMin_Type = OctetString
_WtWebioAn1GraphPtAlarmMin_Object = MibTableColumn
wtWebioAn1GraphPtAlarmMin = _WtWebioAn1GraphPtAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 2),
    _WtWebioAn1GraphPtAlarmMin_Type()
)
wtWebioAn1GraphPtAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmMin.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmMax_Type = OctetString
_WtWebioAn1GraphPtAlarmMax_Object = MibTableColumn
wtWebioAn1GraphPtAlarmMax = _WtWebioAn1GraphPtAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 3),
    _WtWebioAn1GraphPtAlarmMax_Type()
)
wtWebioAn1GraphPtAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmMax.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmHysteresis_Type = OctetString
_WtWebioAn1GraphPtAlarmHysteresis_Object = MibTableColumn
wtWebioAn1GraphPtAlarmHysteresis = _WtWebioAn1GraphPtAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 4),
    _WtWebioAn1GraphPtAlarmHysteresis_Type()
)
wtWebioAn1GraphPtAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmHysteresis.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmDelay_Type = OctetString
_WtWebioAn1GraphPtAlarmDelay_Object = MibTableColumn
wtWebioAn1GraphPtAlarmDelay = _WtWebioAn1GraphPtAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 5),
    _WtWebioAn1GraphPtAlarmDelay_Type()
)
wtWebioAn1GraphPtAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmDelay.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmInterval_Type = OctetString
_WtWebioAn1GraphPtAlarmInterval_Object = MibTableColumn
wtWebioAn1GraphPtAlarmInterval = _WtWebioAn1GraphPtAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 6),
    _WtWebioAn1GraphPtAlarmInterval_Type()
)
wtWebioAn1GraphPtAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmInterval.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtAlarmEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtAlarmEnable_Object = MibTableColumn
wtWebioAn1GraphPtAlarmEnable = _WtWebioAn1GraphPtAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 7),
    _WtWebioAn1GraphPtAlarmEnable_Type()
)
wtWebioAn1GraphPtAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmEnable.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmEMailAddr_Type = OctetString
_WtWebioAn1GraphPtAlarmEMailAddr_Object = MibTableColumn
wtWebioAn1GraphPtAlarmEMailAddr = _WtWebioAn1GraphPtAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 8),
    _WtWebioAn1GraphPtAlarmEMailAddr_Type()
)
wtWebioAn1GraphPtAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmEMailAddr.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmMailSubject_Type = OctetString
_WtWebioAn1GraphPtAlarmMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtAlarmMailSubject = _WtWebioAn1GraphPtAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 9),
    _WtWebioAn1GraphPtAlarmMailSubject_Type()
)
wtWebioAn1GraphPtAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmMailText_Type = OctetString
_WtWebioAn1GraphPtAlarmMailText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmMailText = _WtWebioAn1GraphPtAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 10),
    _WtWebioAn1GraphPtAlarmMailText_Type()
)
wtWebioAn1GraphPtAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmMailText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmManagerIP_Type = OctetString
_WtWebioAn1GraphPtAlarmManagerIP_Object = MibTableColumn
wtWebioAn1GraphPtAlarmManagerIP = _WtWebioAn1GraphPtAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 11),
    _WtWebioAn1GraphPtAlarmManagerIP_Type()
)
wtWebioAn1GraphPtAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmManagerIP.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmTrapText_Type = OctetString
_WtWebioAn1GraphPtAlarmTrapText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTrapText = _WtWebioAn1GraphPtAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 12),
    _WtWebioAn1GraphPtAlarmTrapText_Type()
)
wtWebioAn1GraphPtAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTrapText.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmMailOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphPtAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtAlarmMailOptions_Object = MibTableColumn
wtWebioAn1GraphPtAlarmMailOptions = _WtWebioAn1GraphPtAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 13),
    _WtWebioAn1GraphPtAlarmMailOptions_Type()
)
wtWebioAn1GraphPtAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmMailOptions.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmTcpIpAddr_Type = OctetString
_WtWebioAn1GraphPtAlarmTcpIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTcpIpAddr = _WtWebioAn1GraphPtAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 14),
    _WtWebioAn1GraphPtAlarmTcpIpAddr_Type()
)
wtWebioAn1GraphPtAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmTcpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtAlarmTcpPort_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTcpPort = _WtWebioAn1GraphPtAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 15),
    _WtWebioAn1GraphPtAlarmTcpPort_Type()
)
wtWebioAn1GraphPtAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTcpPort.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmTcpText_Type = OctetString
_WtWebioAn1GraphPtAlarmTcpText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTcpText = _WtWebioAn1GraphPtAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 16),
    _WtWebioAn1GraphPtAlarmTcpText_Type()
)
wtWebioAn1GraphPtAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmClearMailSubject_Type = OctetString
_WtWebioAn1GraphPtAlarmClearMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtAlarmClearMailSubject = _WtWebioAn1GraphPtAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 17),
    _WtWebioAn1GraphPtAlarmClearMailSubject_Type()
)
wtWebioAn1GraphPtAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmClearMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmClearMailText_Type = OctetString
_WtWebioAn1GraphPtAlarmClearMailText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmClearMailText = _WtWebioAn1GraphPtAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 18),
    _WtWebioAn1GraphPtAlarmClearMailText_Type()
)
wtWebioAn1GraphPtAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmClearMailText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmClearTrapText_Type = OctetString
_WtWebioAn1GraphPtAlarmClearTrapText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmClearTrapText = _WtWebioAn1GraphPtAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 19),
    _WtWebioAn1GraphPtAlarmClearTrapText_Type()
)
wtWebioAn1GraphPtAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmClearTrapText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmClearTcpText_Type = OctetString
_WtWebioAn1GraphPtAlarmClearTcpText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmClearTcpText = _WtWebioAn1GraphPtAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 20),
    _WtWebioAn1GraphPtAlarmClearTcpText_Type()
)
wtWebioAn1GraphPtAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmClearTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmSyslogIpAddr_Type = IpAddress
_WtWebioAn1GraphPtAlarmSyslogIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtAlarmSyslogIpAddr = _WtWebioAn1GraphPtAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 21),
    _WtWebioAn1GraphPtAlarmSyslogIpAddr_Type()
)
wtWebioAn1GraphPtAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtAlarmSyslogPort_Object = MibTableColumn
wtWebioAn1GraphPtAlarmSyslogPort = _WtWebioAn1GraphPtAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 22),
    _WtWebioAn1GraphPtAlarmSyslogPort_Type()
)
wtWebioAn1GraphPtAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmSyslogPort.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmSyslogText_Type = OctetString
_WtWebioAn1GraphPtAlarmSyslogText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmSyslogText = _WtWebioAn1GraphPtAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 23),
    _WtWebioAn1GraphPtAlarmSyslogText_Type()
)
wtWebioAn1GraphPtAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmSyslogText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmSyslogClearText_Type = OctetString
_WtWebioAn1GraphPtAlarmSyslogClearText_Object = MibScalar
wtWebioAn1GraphPtAlarmSyslogClearText = _WtWebioAn1GraphPtAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 24),
    _WtWebioAn1GraphPtAlarmSyslogClearText_Type()
)
wtWebioAn1GraphPtAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmSyslogClearText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmFtpDataPort_Type = OctetString
_WtWebioAn1GraphPtAlarmFtpDataPort_Object = MibTableColumn
wtWebioAn1GraphPtAlarmFtpDataPort = _WtWebioAn1GraphPtAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 25),
    _WtWebioAn1GraphPtAlarmFtpDataPort_Type()
)
wtWebioAn1GraphPtAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmFtpDataPort.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmFtpFileName_Type = OctetString
_WtWebioAn1GraphPtAlarmFtpFileName_Object = MibTableColumn
wtWebioAn1GraphPtAlarmFtpFileName = _WtWebioAn1GraphPtAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 26),
    _WtWebioAn1GraphPtAlarmFtpFileName_Type()
)
wtWebioAn1GraphPtAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmFtpFileName.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmFtpText_Type = OctetString
_WtWebioAn1GraphPtAlarmFtpText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmFtpText = _WtWebioAn1GraphPtAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 27),
    _WtWebioAn1GraphPtAlarmFtpText_Type()
)
wtWebioAn1GraphPtAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmFtpText.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmFtpClearText_Type = OctetString
_WtWebioAn1GraphPtAlarmFtpClearText_Object = MibTableColumn
wtWebioAn1GraphPtAlarmFtpClearText = _WtWebioAn1GraphPtAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 28),
    _WtWebioAn1GraphPtAlarmFtpClearText_Type()
)
wtWebioAn1GraphPtAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmFtpClearText.setStatus("mandatory")


class _WtWebioAn1GraphPtAlarmFtpOption_Type(OctetString):
    """Custom type wtWebioAn1GraphPtAlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtAlarmFtpOption_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtAlarmFtpOption_Object = MibTableColumn
wtWebioAn1GraphPtAlarmFtpOption = _WtWebioAn1GraphPtAlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 29),
    _WtWebioAn1GraphPtAlarmFtpOption_Type()
)
wtWebioAn1GraphPtAlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmFtpOption.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmTimerCron_Type = OctetString
_WtWebioAn1GraphPtAlarmTimerCron_Object = MibTableColumn
wtWebioAn1GraphPtAlarmTimerCron = _WtWebioAn1GraphPtAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 30),
    _WtWebioAn1GraphPtAlarmTimerCron_Type()
)
wtWebioAn1GraphPtAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmTimerCron.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmDeltaTemp_Type = OctetString
_WtWebioAn1GraphPtAlarmDeltaTemp_Object = MibTableColumn
wtWebioAn1GraphPtAlarmDeltaTemp = _WtWebioAn1GraphPtAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 31),
    _WtWebioAn1GraphPtAlarmDeltaTemp_Type()
)
wtWebioAn1GraphPtAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmDeltaTemp.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmName_Type = OctetString
_WtWebioAn1GraphPtAlarmName_Object = MibTableColumn
wtWebioAn1GraphPtAlarmName = _WtWebioAn1GraphPtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 39),
    _WtWebioAn1GraphPtAlarmName_Type()
)
wtWebioAn1GraphPtAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmName.setStatus("mandatory")
_WtWebioAn1GraphPtAlarmActive_Type = OctetString
_WtWebioAn1GraphPtAlarmActive_Object = MibTableColumn
wtWebioAn1GraphPtAlarmActive = _WtWebioAn1GraphPtAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 5, 3, 1, 40),
    _WtWebioAn1GraphPtAlarmActive_Type()
)
wtWebioAn1GraphPtAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlarmActive.setStatus("mandatory")
_WtWebioAn1GraphPtGraphics_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtGraphics = _WtWebioAn1GraphPtGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6)
)
_WtWebioAn1GraphPtGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtGraphicsBase = _WtWebioAn1GraphPtGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1)
)
_WtWebioAn1GraphPtGraphicsBaseEnable_Type = OctetString
_WtWebioAn1GraphPtGraphicsBaseEnable_Object = MibScalar
wtWebioAn1GraphPtGraphicsBaseEnable = _WtWebioAn1GraphPtGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 1),
    _WtWebioAn1GraphPtGraphicsBaseEnable_Type()
)
wtWebioAn1GraphPtGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBaseEnable.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsBaseWidth_Type = Integer32
_WtWebioAn1GraphPtGraphicsBaseWidth_Object = MibScalar
wtWebioAn1GraphPtGraphicsBaseWidth = _WtWebioAn1GraphPtGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 2),
    _WtWebioAn1GraphPtGraphicsBaseWidth_Type()
)
wtWebioAn1GraphPtGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBaseWidth.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsBaseHeight_Type = Integer32
_WtWebioAn1GraphPtGraphicsBaseHeight_Object = MibScalar
wtWebioAn1GraphPtGraphicsBaseHeight = _WtWebioAn1GraphPtGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 3),
    _WtWebioAn1GraphPtGraphicsBaseHeight_Type()
)
wtWebioAn1GraphPtGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBaseHeight.setStatus("mandatory")


class _WtWebioAn1GraphPtGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtGraphicsBaseFrameColor_Object = MibScalar
wtWebioAn1GraphPtGraphicsBaseFrameColor = _WtWebioAn1GraphPtGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 4),
    _WtWebioAn1GraphPtGraphicsBaseFrameColor_Type()
)
wtWebioAn1GraphPtGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebioAn1GraphPtGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtGraphicsBaseBackgroundColor_Object = MibScalar
wtWebioAn1GraphPtGraphicsBaseBackgroundColor = _WtWebioAn1GraphPtGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 5),
    _WtWebioAn1GraphPtGraphicsBaseBackgroundColor_Type()
)
wtWebioAn1GraphPtGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsBasePollingrate_Type = Integer32
_WtWebioAn1GraphPtGraphicsBasePollingrate_Object = MibScalar
wtWebioAn1GraphPtGraphicsBasePollingrate = _WtWebioAn1GraphPtGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 1, 6),
    _WtWebioAn1GraphPtGraphicsBasePollingrate_Type()
)
wtWebioAn1GraphPtGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsBasePollingrate.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtGraphicsSelect = _WtWebioAn1GraphPtGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2)
)


class _WtWebioAn1GraphPtGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel = _WtWebioAn1GraphPtGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 1),
    _WtWebioAn1GraphPtGraphicsSelectDisplaySensorSel_Type()
)
wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem = _WtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 2),
    _WtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem_Type()
)
wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebioAn1GraphPt2SensorColorTable_Object = MibTable
wtWebioAn1GraphPt2SensorColorTable = _WtWebioAn1GraphPt2SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPt2SensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphPt2SensorColorEntry_Object = MibTableRow
wtWebioAn1GraphPt2SensorColorEntry = _WtWebioAn1GraphPt2SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 3, 1)
)
wtWebioAn1GraphPt2SensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPt2SensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPt2GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPt2GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPt2GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPt2GraphicsSensorColor_Object = MibTableColumn
wtWebioAn1GraphPt2GraphicsSensorColor = _WtWebioAn1GraphPt2GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 3, 1, 1),
    _WtWebioAn1GraphPt2GraphicsSensorColor_Type()
)
wtWebioAn1GraphPt2GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPt2GraphicsSensorColor.setStatus("mandatory")
_WtWebioAn1GraphPt2GraphicsSelectScale_Type = OctetString
_WtWebioAn1GraphPt2GraphicsSelectScale_Object = MibTableColumn
wtWebioAn1GraphPt2GraphicsSelectScale = _WtWebioAn1GraphPt2GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 2, 3, 1, 2),
    _WtWebioAn1GraphPt2GraphicsSelectScale_Type()
)
wtWebioAn1GraphPt2GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPt2GraphicsSelectScale.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtGraphicsScale = _WtWebioAn1GraphPtGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3)
)
_WtWebioAn1GraphPtGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphPtGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphPtGraphicsScaleAutoScaleEnable = _WtWebioAn1GraphPtGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 1),
    _WtWebioAn1GraphPtGraphicsScaleAutoScaleEnable_Type()
)
wtWebioAn1GraphPtGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebioAn1GraphPtGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebioAn1GraphPtGraphicsScaleAutoFitEnable = _WtWebioAn1GraphPtGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 2),
    _WtWebioAn1GraphPtGraphicsScaleAutoFitEnable_Type()
)
wtWebioAn1GraphPtGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale1Min_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale1Min_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale1Min = _WtWebioAn1GraphPtGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 3),
    _WtWebioAn1GraphPtGraphicsScale1Min_Type()
)
wtWebioAn1GraphPtGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale1Min.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale2Min_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale2Min_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale2Min = _WtWebioAn1GraphPtGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 4),
    _WtWebioAn1GraphPtGraphicsScale2Min_Type()
)
wtWebioAn1GraphPtGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale2Min.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale3Min_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale3Min_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale3Min = _WtWebioAn1GraphPtGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 5),
    _WtWebioAn1GraphPtGraphicsScale3Min_Type()
)
wtWebioAn1GraphPtGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale3Min.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale4Min_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale4Min_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale4Min = _WtWebioAn1GraphPtGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 6),
    _WtWebioAn1GraphPtGraphicsScale4Min_Type()
)
wtWebioAn1GraphPtGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale4Min.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale1Max_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale1Max_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale1Max = _WtWebioAn1GraphPtGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 7),
    _WtWebioAn1GraphPtGraphicsScale1Max_Type()
)
wtWebioAn1GraphPtGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale1Max.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale2Max_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale2Max_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale2Max = _WtWebioAn1GraphPtGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 8),
    _WtWebioAn1GraphPtGraphicsScale2Max_Type()
)
wtWebioAn1GraphPtGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale2Max.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale3Max_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale3Max_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale3Max = _WtWebioAn1GraphPtGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 9),
    _WtWebioAn1GraphPtGraphicsScale3Max_Type()
)
wtWebioAn1GraphPtGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale3Max.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale4Max_Type = Integer32
_WtWebioAn1GraphPtGraphicsScale4Max_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale4Max = _WtWebioAn1GraphPtGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 10),
    _WtWebioAn1GraphPtGraphicsScale4Max_Type()
)
wtWebioAn1GraphPtGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale4Max.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale1Unit_Type = OctetString
_WtWebioAn1GraphPtGraphicsScale1Unit_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale1Unit = _WtWebioAn1GraphPtGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 11),
    _WtWebioAn1GraphPtGraphicsScale1Unit_Type()
)
wtWebioAn1GraphPtGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale1Unit.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale2Unit_Type = OctetString
_WtWebioAn1GraphPtGraphicsScale2Unit_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale2Unit = _WtWebioAn1GraphPtGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 12),
    _WtWebioAn1GraphPtGraphicsScale2Unit_Type()
)
wtWebioAn1GraphPtGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale2Unit.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale3Unit_Type = OctetString
_WtWebioAn1GraphPtGraphicsScale3Unit_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale3Unit = _WtWebioAn1GraphPtGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 13),
    _WtWebioAn1GraphPtGraphicsScale3Unit_Type()
)
wtWebioAn1GraphPtGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale3Unit.setStatus("mandatory")
_WtWebioAn1GraphPtGraphicsScale4Unit_Type = OctetString
_WtWebioAn1GraphPtGraphicsScale4Unit_Object = MibScalar
wtWebioAn1GraphPtGraphicsScale4Unit = _WtWebioAn1GraphPtGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 1, 6, 3, 14),
    _WtWebioAn1GraphPtGraphicsScale4Unit_Type()
)
wtWebioAn1GraphPtGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtGraphicsScale4Unit.setStatus("mandatory")
_WtWebioAn1GraphPtPorts_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtPorts = _WtWebioAn1GraphPtPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2)
)
_WtWebioAn1GraphPtPortTable_Object = MibTable
wtWebioAn1GraphPtPortTable = _WtWebioAn1GraphPtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortTable.setStatus("mandatory")
_WtWebioAn1GraphPtPortEntry_Object = MibTableRow
wtWebioAn1GraphPtPortEntry = _WtWebioAn1GraphPtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1)
)
wtWebioAn1GraphPtPortEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortEntry.setStatus("mandatory")
_WtWebioAn1GraphPtPortName_Type = OctetString
_WtWebioAn1GraphPtPortName_Object = MibTableColumn
wtWebioAn1GraphPtPortName = _WtWebioAn1GraphPtPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 1),
    _WtWebioAn1GraphPtPortName_Type()
)
wtWebioAn1GraphPtPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortName.setStatus("mandatory")
_WtWebioAn1GraphPtPortText_Type = OctetString
_WtWebioAn1GraphPtPortText_Object = MibTableColumn
wtWebioAn1GraphPtPortText = _WtWebioAn1GraphPtPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 2),
    _WtWebioAn1GraphPtPortText_Type()
)
wtWebioAn1GraphPtPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortText.setStatus("mandatory")
_WtWebioAn1GraphPtPortOffset1_Type = OctetString
_WtWebioAn1GraphPtPortOffset1_Object = MibTableColumn
wtWebioAn1GraphPtPortOffset1 = _WtWebioAn1GraphPtPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 3),
    _WtWebioAn1GraphPtPortOffset1_Type()
)
wtWebioAn1GraphPtPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortOffset1.setStatus("mandatory")
_WtWebioAn1GraphPtPortTemperature1_Type = OctetString
_WtWebioAn1GraphPtPortTemperature1_Object = MibTableColumn
wtWebioAn1GraphPtPortTemperature1 = _WtWebioAn1GraphPtPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 4),
    _WtWebioAn1GraphPtPortTemperature1_Type()
)
wtWebioAn1GraphPtPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortTemperature1.setStatus("mandatory")
_WtWebioAn1GraphPtPortOffset2_Type = OctetString
_WtWebioAn1GraphPtPortOffset2_Object = MibTableColumn
wtWebioAn1GraphPtPortOffset2 = _WtWebioAn1GraphPtPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 5),
    _WtWebioAn1GraphPtPortOffset2_Type()
)
wtWebioAn1GraphPtPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortOffset2.setStatus("mandatory")
_WtWebioAn1GraphPtPortTemperature2_Type = OctetString
_WtWebioAn1GraphPtPortTemperature2_Object = MibTableColumn
wtWebioAn1GraphPtPortTemperature2 = _WtWebioAn1GraphPtPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 6),
    _WtWebioAn1GraphPtPortTemperature2_Type()
)
wtWebioAn1GraphPtPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortTemperature2.setStatus("mandatory")
_WtWebioAn1GraphPtPortComment_Type = OctetString
_WtWebioAn1GraphPtPortComment_Object = MibTableColumn
wtWebioAn1GraphPtPortComment = _WtWebioAn1GraphPtPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 7),
    _WtWebioAn1GraphPtPortComment_Type()
)
wtWebioAn1GraphPtPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortComment.setStatus("mandatory")


class _WtWebioAn1GraphPtPortSensorSelect_Type(OctetString):
    """Custom type wtWebioAn1GraphPtPortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtPortSensorSelect_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtPortSensorSelect_Object = MibTableColumn
wtWebioAn1GraphPtPortSensorSelect = _WtWebioAn1GraphPtPortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 2, 1, 1, 8),
    _WtWebioAn1GraphPtPortSensorSelect_Type()
)
wtWebioAn1GraphPtPortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtPortSensorSelect.setStatus("mandatory")
_WtWebioAn1GraphPtManufact_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtManufact = _WtWebioAn1GraphPtManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3)
)
_WtWebioAn1GraphPtMfName_Type = OctetString
_WtWebioAn1GraphPtMfName_Object = MibScalar
wtWebioAn1GraphPtMfName = _WtWebioAn1GraphPtMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 1),
    _WtWebioAn1GraphPtMfName_Type()
)
wtWebioAn1GraphPtMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfName.setStatus("mandatory")
_WtWebioAn1GraphPtMfAddr_Type = OctetString
_WtWebioAn1GraphPtMfAddr_Object = MibScalar
wtWebioAn1GraphPtMfAddr = _WtWebioAn1GraphPtMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 2),
    _WtWebioAn1GraphPtMfAddr_Type()
)
wtWebioAn1GraphPtMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfAddr.setStatus("mandatory")
_WtWebioAn1GraphPtMfHotline_Type = OctetString
_WtWebioAn1GraphPtMfHotline_Object = MibScalar
wtWebioAn1GraphPtMfHotline = _WtWebioAn1GraphPtMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 3),
    _WtWebioAn1GraphPtMfHotline_Type()
)
wtWebioAn1GraphPtMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfHotline.setStatus("mandatory")
_WtWebioAn1GraphPtMfInternet_Type = OctetString
_WtWebioAn1GraphPtMfInternet_Object = MibScalar
wtWebioAn1GraphPtMfInternet = _WtWebioAn1GraphPtMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 4),
    _WtWebioAn1GraphPtMfInternet_Type()
)
wtWebioAn1GraphPtMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfInternet.setStatus("mandatory")
_WtWebioAn1GraphPtMfDeviceTyp_Type = OctetString
_WtWebioAn1GraphPtMfDeviceTyp_Object = MibScalar
wtWebioAn1GraphPtMfDeviceTyp = _WtWebioAn1GraphPtMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 5),
    _WtWebioAn1GraphPtMfDeviceTyp_Type()
)
wtWebioAn1GraphPtMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfDeviceTyp.setStatus("mandatory")
_WtWebioAn1GraphPtMfOrderNo_Type = OctetString
_WtWebioAn1GraphPtMfOrderNo_Object = MibScalar
wtWebioAn1GraphPtMfOrderNo = _WtWebioAn1GraphPtMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 3, 3, 6),
    _WtWebioAn1GraphPtMfOrderNo_Type()
)
wtWebioAn1GraphPtMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtMfOrderNo.setStatus("mandatory")
_WtWebioAn1GraphPtDiag_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtDiag = _WtWebioAn1GraphPtDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4)
)
_WtWebioAn1GraphPtDiagErrorCount_Type = Integer32
_WtWebioAn1GraphPtDiagErrorCount_Object = MibScalar
wtWebioAn1GraphPtDiagErrorCount = _WtWebioAn1GraphPtDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4, 1),
    _WtWebioAn1GraphPtDiagErrorCount_Type()
)
wtWebioAn1GraphPtDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDiagErrorCount.setStatus("mandatory")
_WtWebioAn1GraphPtDiagBinaryError_Type = OctetString
_WtWebioAn1GraphPtDiagBinaryError_Object = MibScalar
wtWebioAn1GraphPtDiagBinaryError = _WtWebioAn1GraphPtDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4, 2),
    _WtWebioAn1GraphPtDiagBinaryError_Type()
)
wtWebioAn1GraphPtDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDiagBinaryError.setStatus("mandatory")
_WtWebioAn1GraphPtDiagErrorIndex_Type = Integer32
_WtWebioAn1GraphPtDiagErrorIndex_Object = MibScalar
wtWebioAn1GraphPtDiagErrorIndex = _WtWebioAn1GraphPtDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4, 3),
    _WtWebioAn1GraphPtDiagErrorIndex_Type()
)
wtWebioAn1GraphPtDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDiagErrorIndex.setStatus("mandatory")
_WtWebioAn1GraphPtDiagErrorMessage_Type = OctetString
_WtWebioAn1GraphPtDiagErrorMessage_Object = MibScalar
wtWebioAn1GraphPtDiagErrorMessage = _WtWebioAn1GraphPtDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4, 4),
    _WtWebioAn1GraphPtDiagErrorMessage_Type()
)
wtWebioAn1GraphPtDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDiagErrorMessage.setStatus("mandatory")
_WtWebioAn1GraphPtDiagErrorClear_Type = Integer32
_WtWebioAn1GraphPtDiagErrorClear_Object = MibScalar
wtWebioAn1GraphPtDiagErrorClear = _WtWebioAn1GraphPtDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 4, 5),
    _WtWebioAn1GraphPtDiagErrorClear_Type()
)
wtWebioAn1GraphPtDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtDiagErrorClear.setStatus("mandatory")
_WtWebioAn1GraphPtSw_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSw = _WtWebioAn1GraphPtSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23)
)
_WtWebioAn1GraphPtSwTemp_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwTemp = _WtWebioAn1GraphPtSwTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1)
)


class _WtWebioAn1GraphPtSwSensors_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSwSensors_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwSensors_Object = MibScalar
wtWebioAn1GraphPtSwSensors = _WtWebioAn1GraphPtSwSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 1),
    _WtWebioAn1GraphPtSwSensors_Type()
)
wtWebioAn1GraphPtSwSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensors.setStatus("mandatory")
_WtWebioAn1GraphPtSwSensorTable_Object = MibTable
wtWebioAn1GraphPtSwSensorTable = _WtWebioAn1GraphPtSwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSensorEntry_Object = MibTableRow
wtWebioAn1GraphPtSwSensorEntry = _WtWebioAn1GraphPtSwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 2, 1)
)
wtWebioAn1GraphPtSwSensorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwSensorNo_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSwSensorNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwSensorNo_Object = MibTableColumn
wtWebioAn1GraphPtSwSensorNo = _WtWebioAn1GraphPtSwSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 2, 1, 1),
    _WtWebioAn1GraphPtSwSensorNo_Type()
)
wtWebioAn1GraphPtSwSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorNo.setStatus("mandatory")
_WtWebioAn1GraphPtSwTempValueTable_Object = MibTable
wtWebioAn1GraphPtSwTempValueTable = _WtWebioAn1GraphPtSwTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwTempValueEntry_Object = MibTableRow
wtWebioAn1GraphPtSwTempValueEntry = _WtWebioAn1GraphPtSwTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 3, 1)
)
wtWebioAn1GraphPtSwTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValueEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwTempValue_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebioAn1GraphPtSwTempValue_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwTempValue_Object = MibTableColumn
wtWebioAn1GraphPtSwTempValue = _WtWebioAn1GraphPtSwTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 3, 1, 1),
    _WtWebioAn1GraphPtSwTempValue_Type()
)
wtWebioAn1GraphPtSwTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValue.setStatus("mandatory")
_WtWebioAn1GraphPtSwBinaryTempValueTable_Object = MibTable
wtWebioAn1GraphPtSwBinaryTempValueTable = _WtWebioAn1GraphPtSwBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwBinaryTempValueEntry_Object = MibTableRow
wtWebioAn1GraphPtSwBinaryTempValueEntry = _WtWebioAn1GraphPtSwBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 4, 1)
)
wtWebioAn1GraphPtSwBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryTempValueEntry.setStatus("mandatory")
_WtWebioAn1GraphPtSwBinaryTempValue_Type = Integer32
_WtWebioAn1GraphPtSwBinaryTempValue_Object = MibTableColumn
wtWebioAn1GraphPtSwBinaryTempValue = _WtWebioAn1GraphPtSwBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 4, 1, 1),
    _WtWebioAn1GraphPtSwBinaryTempValue_Type()
)
wtWebioAn1GraphPtSwBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryTempValue.setStatus("mandatory")


class _WtWebioAn1GraphPtSwOutputs_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSwOutputs_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwOutputs_Object = MibScalar
wtWebioAn1GraphPtSwOutputs = _WtWebioAn1GraphPtSwOutputs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 5),
    _WtWebioAn1GraphPtSwOutputs_Type()
)
wtWebioAn1GraphPtSwOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwOutputs.setStatus("mandatory")
_WtWebioAn1GraphPtSwOutputTable_Object = MibTable
wtWebioAn1GraphPtSwOutputTable = _WtWebioAn1GraphPtSwOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 6)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwOutputTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwOutputEntry_Object = MibTableRow
wtWebioAn1GraphPtSwOutputEntry = _WtWebioAn1GraphPtSwOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 6, 1)
)
wtWebioAn1GraphPtSwOutputEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwOutputNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwOutputEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwOutputNo_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwOutputNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphPtSwOutputNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwOutputNo_Object = MibTableColumn
wtWebioAn1GraphPtSwOutputNo = _WtWebioAn1GraphPtSwOutputNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 6, 1, 1),
    _WtWebioAn1GraphPtSwOutputNo_Type()
)
wtWebioAn1GraphPtSwOutputNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwOutputNo.setStatus("mandatory")
_WtWebioAn1GraphPtSwBinaryOutputValueTable_Object = MibTable
wtWebioAn1GraphPtSwBinaryOutputValueTable = _WtWebioAn1GraphPtSwBinaryOutputValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 7)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryOutputValueTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwBinaryOutputValueEntry_Object = MibTableRow
wtWebioAn1GraphPtSwBinaryOutputValueEntry = _WtWebioAn1GraphPtSwBinaryOutputValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 7, 1)
)
wtWebioAn1GraphPtSwBinaryOutputValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwOutputNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryOutputValueEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwBinaryOutputValue_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwBinaryOutputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphPtSwBinaryOutput-OFF", 0),
          ("wtWebioAn1GraphPtSwBinaryOutput-ON", 1))
    )


_WtWebioAn1GraphPtSwBinaryOutputValue_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwBinaryOutputValue_Object = MibTableColumn
wtWebioAn1GraphPtSwBinaryOutputValue = _WtWebioAn1GraphPtSwBinaryOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 7, 1, 1),
    _WtWebioAn1GraphPtSwBinaryOutputValue_Type()
)
wtWebioAn1GraphPtSwBinaryOutputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwBinaryOutputValue.setStatus("mandatory")
_WtWebioAn1GraphPtSwTempValuePktTable_Object = MibTable
wtWebioAn1GraphPtSwTempValuePktTable = _WtWebioAn1GraphPtSwTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValuePktTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwTempValuePktEntry_Object = MibTableRow
wtWebioAn1GraphPtSwTempValuePktEntry = _WtWebioAn1GraphPtSwTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 8, 1)
)
wtWebioAn1GraphPtSwTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValuePktEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwTempValuePkt_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WtWebioAn1GraphPtSwTempValuePkt_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwTempValuePkt_Object = MibTableColumn
wtWebioAn1GraphPtSwTempValuePkt = _WtWebioAn1GraphPtSwTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 1, 8, 1, 1),
    _WtWebioAn1GraphPtSwTempValuePkt_Type()
)
wtWebioAn1GraphPtSwTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTempValuePkt.setStatus("mandatory")
_WtWebioAn1GraphPtSwSessCntrl_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwSessCntrl = _WtWebioAn1GraphPtSwSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2)
)
_WtWebioAn1GraphPtSwSessCntrlPassword_Type = OctetString
_WtWebioAn1GraphPtSwSessCntrlPassword_Object = MibScalar
wtWebioAn1GraphPtSwSessCntrlPassword = _WtWebioAn1GraphPtSwSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2, 1),
    _WtWebioAn1GraphPtSwSessCntrlPassword_Type()
)
wtWebioAn1GraphPtSwSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSessCntrlPassword.setStatus("mandatory")


class _WtWebioAn1GraphPtSwSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphPtSwSessCntrl-NoSession", 0),
          ("wtWebioAn1GraphPtSwSessCntrl-Session", 1))
    )


_WtWebioAn1GraphPtSwSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwSessCntrlConfigMode_Object = MibScalar
wtWebioAn1GraphPtSwSessCntrlConfigMode = _WtWebioAn1GraphPtSwSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2, 2),
    _WtWebioAn1GraphPtSwSessCntrlConfigMode_Type()
)
wtWebioAn1GraphPtSwSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSessCntrlConfigMode.setStatus("mandatory")
_WtWebioAn1GraphPtSwSessCntrlLogout_Type = Integer32
_WtWebioAn1GraphPtSwSessCntrlLogout_Object = MibScalar
wtWebioAn1GraphPtSwSessCntrlLogout = _WtWebioAn1GraphPtSwSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2, 3),
    _WtWebioAn1GraphPtSwSessCntrlLogout_Type()
)
wtWebioAn1GraphPtSwSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSessCntrlLogout.setStatus("mandatory")
_WtWebioAn1GraphPtSwSessCntrlAdminPassword_Type = OctetString
_WtWebioAn1GraphPtSwSessCntrlAdminPassword_Object = MibScalar
wtWebioAn1GraphPtSwSessCntrlAdminPassword = _WtWebioAn1GraphPtSwSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2, 4),
    _WtWebioAn1GraphPtSwSessCntrlAdminPassword_Type()
)
wtWebioAn1GraphPtSwSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSessCntrlAdminPassword.setStatus("mandatory")
_WtWebioAn1GraphPtSwSessCntrlConfigPassword_Type = OctetString
_WtWebioAn1GraphPtSwSessCntrlConfigPassword_Object = MibScalar
wtWebioAn1GraphPtSwSessCntrlConfigPassword = _WtWebioAn1GraphPtSwSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 2, 5),
    _WtWebioAn1GraphPtSwSessCntrlConfigPassword_Type()
)
wtWebioAn1GraphPtSwSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSessCntrlConfigPassword.setStatus("mandatory")
_WtWebioAn1GraphPtSwConfig_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwConfig = _WtWebioAn1GraphPtSwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3)
)
_WtWebioAn1GraphPtSwDevice_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwDevice = _WtWebioAn1GraphPtSwDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1)
)
_WtWebioAn1GraphPtSwText_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwText = _WtWebioAn1GraphPtSwText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 1)
)
_WtWebioAn1GraphPtSwDeviceName_Type = OctetString
_WtWebioAn1GraphPtSwDeviceName_Object = MibScalar
wtWebioAn1GraphPtSwDeviceName = _WtWebioAn1GraphPtSwDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 1, 1),
    _WtWebioAn1GraphPtSwDeviceName_Type()
)
wtWebioAn1GraphPtSwDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDeviceName.setStatus("mandatory")
_WtWebioAn1GraphPtSwDeviceText_Type = OctetString
_WtWebioAn1GraphPtSwDeviceText_Object = MibScalar
wtWebioAn1GraphPtSwDeviceText = _WtWebioAn1GraphPtSwDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 1, 2),
    _WtWebioAn1GraphPtSwDeviceText_Type()
)
wtWebioAn1GraphPtSwDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDeviceText.setStatus("mandatory")
_WtWebioAn1GraphPtSwDeviceLocation_Type = OctetString
_WtWebioAn1GraphPtSwDeviceLocation_Object = MibScalar
wtWebioAn1GraphPtSwDeviceLocation = _WtWebioAn1GraphPtSwDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 1, 3),
    _WtWebioAn1GraphPtSwDeviceLocation_Type()
)
wtWebioAn1GraphPtSwDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDeviceLocation.setStatus("mandatory")
_WtWebioAn1GraphPtSwDeviceContact_Type = OctetString
_WtWebioAn1GraphPtSwDeviceContact_Object = MibScalar
wtWebioAn1GraphPtSwDeviceContact = _WtWebioAn1GraphPtSwDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 1, 4),
    _WtWebioAn1GraphPtSwDeviceContact_Type()
)
wtWebioAn1GraphPtSwDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDeviceContact.setStatus("mandatory")
_WtWebioAn1GraphPtSwTimeDate_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwTimeDate = _WtWebioAn1GraphPtSwTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2)
)
_WtWebioAn1GraphPtSwTimeZone_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwTimeZone = _WtWebioAn1GraphPtSwTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1)
)
_WtWebioAn1GraphPtSwTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphPtSwTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphPtSwTzOffsetHrs = _WtWebioAn1GraphPtSwTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 1),
    _WtWebioAn1GraphPtSwTzOffsetHrs_Type()
)
wtWebioAn1GraphPtSwTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphPtSwTzOffsetMin_Type = Integer32
_WtWebioAn1GraphPtSwTzOffsetMin_Object = MibScalar
wtWebioAn1GraphPtSwTzOffsetMin = _WtWebioAn1GraphPtSwTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 2),
    _WtWebioAn1GraphPtSwTzOffsetMin_Type()
)
wtWebioAn1GraphPtSwTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphPtSwTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwTzEnable_Object = MibScalar
wtWebioAn1GraphPtSwTzEnable = _WtWebioAn1GraphPtSwTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 3),
    _WtWebioAn1GraphPtSwTzEnable_Type()
)
wtWebioAn1GraphPtSwTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTzEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphPtSwStTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphPtSwStTzOffsetHrs = _WtWebioAn1GraphPtSwStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 4),
    _WtWebioAn1GraphPtSwStTzOffsetHrs_Type()
)
wtWebioAn1GraphPtSwStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzOffsetMin_Type = Integer32
_WtWebioAn1GraphPtSwStTzOffsetMin_Object = MibScalar
wtWebioAn1GraphPtSwStTzOffsetMin = _WtWebioAn1GraphPtSwStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 5),
    _WtWebioAn1GraphPtSwStTzOffsetMin_Type()
)
wtWebioAn1GraphPtSwStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwStTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwStTzEnable_Object = MibScalar
wtWebioAn1GraphPtSwStTzEnable = _WtWebioAn1GraphPtSwStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 6),
    _WtWebioAn1GraphPtSwStTzEnable_Type()
)
wtWebioAn1GraphPtSwStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStartMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStartMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStartMonth-April", 4),
          ("wtWebioAn1GraphPtSwStartMonth-August", 8),
          ("wtWebioAn1GraphPtSwStartMonth-December", 12),
          ("wtWebioAn1GraphPtSwStartMonth-February", 2),
          ("wtWebioAn1GraphPtSwStartMonth-January", 1),
          ("wtWebioAn1GraphPtSwStartMonth-July", 7),
          ("wtWebioAn1GraphPtSwStartMonth-June", 6),
          ("wtWebioAn1GraphPtSwStartMonth-March", 3),
          ("wtWebioAn1GraphPtSwStartMonth-May", 5),
          ("wtWebioAn1GraphPtSwStartMonth-November", 11),
          ("wtWebioAn1GraphPtSwStartMonth-October", 10),
          ("wtWebioAn1GraphPtSwStartMonth-September", 9))
    )


_WtWebioAn1GraphPtSwStTzStartMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStartMonth_Object = MibScalar
wtWebioAn1GraphPtSwStTzStartMonth = _WtWebioAn1GraphPtSwStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 7),
    _WtWebioAn1GraphPtSwStTzStartMonth_Type()
)
wtWebioAn1GraphPtSwStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStartMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStartMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStartMode based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStartMode-first", 1),
          ("wtWebioAn1GraphPtSwStartMode-fourth", 4),
          ("wtWebioAn1GraphPtSwStartMode-last", 5),
          ("wtWebioAn1GraphPtSwStartMode-second", 2),
          ("wtWebioAn1GraphPtSwStartMode-third", 3))
    )


_WtWebioAn1GraphPtSwStTzStartMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStartMode_Object = MibScalar
wtWebioAn1GraphPtSwStTzStartMode = _WtWebioAn1GraphPtSwStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 8),
    _WtWebioAn1GraphPtSwStTzStartMode_Type()
)
wtWebioAn1GraphPtSwStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStartMode.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStartWday_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStartWday based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStartWday-Friday", 6),
          ("wtWebioAn1GraphPtSwStartWday-Monday", 2),
          ("wtWebioAn1GraphPtSwStartWday-Saturday", 7),
          ("wtWebioAn1GraphPtSwStartWday-Sunday", 1),
          ("wtWebioAn1GraphPtSwStartWday-Thursday", 4),
          ("wtWebioAn1GraphPtSwStartWday-Tuesday", 3),
          ("wtWebioAn1GraphPtSwStartWday-Wednesday", 5))
    )


_WtWebioAn1GraphPtSwStTzStartWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStartWday_Object = MibScalar
wtWebioAn1GraphPtSwStTzStartWday = _WtWebioAn1GraphPtSwStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 9),
    _WtWebioAn1GraphPtSwStTzStartWday_Type()
)
wtWebioAn1GraphPtSwStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStartWday.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzStartHrs_Type = Integer32
_WtWebioAn1GraphPtSwStTzStartHrs_Object = MibScalar
wtWebioAn1GraphPtSwStTzStartHrs = _WtWebioAn1GraphPtSwStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 10),
    _WtWebioAn1GraphPtSwStTzStartHrs_Type()
)
wtWebioAn1GraphPtSwStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStartHrs.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzStartMin_Type = Integer32
_WtWebioAn1GraphPtSwStTzStartMin_Object = MibScalar
wtWebioAn1GraphPtSwStTzStartMin = _WtWebioAn1GraphPtSwStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 11),
    _WtWebioAn1GraphPtSwStTzStartMin_Type()
)
wtWebioAn1GraphPtSwStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStartMin.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStopMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStopMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStopMonth-April", 4),
          ("wtWebioAn1GraphPtSwStopMonth-August", 8),
          ("wtWebioAn1GraphPtSwStopMonth-December", 12),
          ("wtWebioAn1GraphPtSwStopMonth-February", 2),
          ("wtWebioAn1GraphPtSwStopMonth-January", 1),
          ("wtWebioAn1GraphPtSwStopMonth-July", 7),
          ("wtWebioAn1GraphPtSwStopMonth-June", 6),
          ("wtWebioAn1GraphPtSwStopMonth-March", 3),
          ("wtWebioAn1GraphPtSwStopMonth-May", 5),
          ("wtWebioAn1GraphPtSwStopMonth-November", 11),
          ("wtWebioAn1GraphPtSwStopMonth-October", 10),
          ("wtWebioAn1GraphPtSwStopMonth-September", 9))
    )


_WtWebioAn1GraphPtSwStTzStopMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStopMonth_Object = MibScalar
wtWebioAn1GraphPtSwStTzStopMonth = _WtWebioAn1GraphPtSwStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 12),
    _WtWebioAn1GraphPtSwStTzStopMonth_Type()
)
wtWebioAn1GraphPtSwStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStopMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStopMode_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStopMode based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStopMode-first", 1),
          ("wtWebioAn1GraphPtSwStopMode-fourth", 4),
          ("wtWebioAn1GraphPtSwStopMode-last", 5),
          ("wtWebioAn1GraphPtSwStopMode-second", 2),
          ("wtWebioAn1GraphPtSwStopMode-third", 3))
    )


_WtWebioAn1GraphPtSwStTzStopMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStopMode_Object = MibScalar
wtWebioAn1GraphPtSwStTzStopMode = _WtWebioAn1GraphPtSwStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 13),
    _WtWebioAn1GraphPtSwStTzStopMode_Type()
)
wtWebioAn1GraphPtSwStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStopMode.setStatus("mandatory")


class _WtWebioAn1GraphPtSwStTzStopWday_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwStTzStopWday based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwStopWday-Friday", 6),
          ("wtWebioAn1GraphPtSwStopWday-Monday", 2),
          ("wtWebioAn1GraphPtSwStopWday-Saturday", 7),
          ("wtWebioAn1GraphPtSwStopWday-Sunday", 1),
          ("wtWebioAn1GraphPtSwStopWday-Thursday", 4),
          ("wtWebioAn1GraphPtSwStopWday-Tuesday", 3),
          ("wtWebioAn1GraphPtSwStopWday-Wednesday", 5))
    )


_WtWebioAn1GraphPtSwStTzStopWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwStTzStopWday_Object = MibScalar
wtWebioAn1GraphPtSwStTzStopWday = _WtWebioAn1GraphPtSwStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 14),
    _WtWebioAn1GraphPtSwStTzStopWday_Type()
)
wtWebioAn1GraphPtSwStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStopWday.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzStopHrs_Type = Integer32
_WtWebioAn1GraphPtSwStTzStopHrs_Object = MibScalar
wtWebioAn1GraphPtSwStTzStopHrs = _WtWebioAn1GraphPtSwStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 15),
    _WtWebioAn1GraphPtSwStTzStopHrs_Type()
)
wtWebioAn1GraphPtSwStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStopHrs.setStatus("mandatory")
_WtWebioAn1GraphPtSwStTzStopMin_Type = Integer32
_WtWebioAn1GraphPtSwStTzStopMin_Object = MibScalar
wtWebioAn1GraphPtSwStTzStopMin = _WtWebioAn1GraphPtSwStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 1, 16),
    _WtWebioAn1GraphPtSwStTzStopMin_Type()
)
wtWebioAn1GraphPtSwStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStTzStopMin.setStatus("mandatory")
_WtWebioAn1GraphPtSwTimeServer_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwTimeServer = _WtWebioAn1GraphPtSwTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 2)
)
_WtWebioAn1GraphPtSwTimeServer1_Type = OctetString
_WtWebioAn1GraphPtSwTimeServer1_Object = MibScalar
wtWebioAn1GraphPtSwTimeServer1 = _WtWebioAn1GraphPtSwTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 2, 1),
    _WtWebioAn1GraphPtSwTimeServer1_Type()
)
wtWebioAn1GraphPtSwTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTimeServer1.setStatus("mandatory")
_WtWebioAn1GraphPtSwTimeServer2_Type = OctetString
_WtWebioAn1GraphPtSwTimeServer2_Object = MibScalar
wtWebioAn1GraphPtSwTimeServer2 = _WtWebioAn1GraphPtSwTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 2, 2),
    _WtWebioAn1GraphPtSwTimeServer2_Type()
)
wtWebioAn1GraphPtSwTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTimeServer2.setStatus("mandatory")


class _WtWebioAn1GraphPtSwTsEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwTsEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwTsEnable_Object = MibScalar
wtWebioAn1GraphPtSwTsEnable = _WtWebioAn1GraphPtSwTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 2, 3),
    _WtWebioAn1GraphPtSwTsEnable_Type()
)
wtWebioAn1GraphPtSwTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTsEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwTsSyncTime_Type = Integer32
_WtWebioAn1GraphPtSwTsSyncTime_Object = MibScalar
wtWebioAn1GraphPtSwTsSyncTime = _WtWebioAn1GraphPtSwTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 2, 4),
    _WtWebioAn1GraphPtSwTsSyncTime_Type()
)
wtWebioAn1GraphPtSwTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwTsSyncTime.setStatus("mandatory")
_WtWebioAn1GraphPtSwDeviceClock_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwDeviceClock = _WtWebioAn1GraphPtSwDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3)
)


class _WtWebioAn1GraphPtSwClockHrs_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebioAn1GraphPtSwClockHrs_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwClockHrs_Object = MibScalar
wtWebioAn1GraphPtSwClockHrs = _WtWebioAn1GraphPtSwClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3, 1),
    _WtWebioAn1GraphPtSwClockHrs_Type()
)
wtWebioAn1GraphPtSwClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwClockHrs.setStatus("mandatory")


class _WtWebioAn1GraphPtSwClockMin_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebioAn1GraphPtSwClockMin_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwClockMin_Object = MibScalar
wtWebioAn1GraphPtSwClockMin = _WtWebioAn1GraphPtSwClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3, 2),
    _WtWebioAn1GraphPtSwClockMin_Type()
)
wtWebioAn1GraphPtSwClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwClockMin.setStatus("mandatory")


class _WtWebioAn1GraphPtSwClockDay_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebioAn1GraphPtSwClockDay_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwClockDay_Object = MibScalar
wtWebioAn1GraphPtSwClockDay = _WtWebioAn1GraphPtSwClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3, 3),
    _WtWebioAn1GraphPtSwClockDay_Type()
)
wtWebioAn1GraphPtSwClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwClockDay.setStatus("mandatory")


class _WtWebioAn1GraphPtSwClockMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwClockMonth based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwClockMonth-April", 4),
          ("wtWebioAn1GraphPtSwClockMonth-August", 8),
          ("wtWebioAn1GraphPtSwClockMonth-December", 12),
          ("wtWebioAn1GraphPtSwClockMonth-February", 2),
          ("wtWebioAn1GraphPtSwClockMonth-January", 1),
          ("wtWebioAn1GraphPtSwClockMonth-July", 7),
          ("wtWebioAn1GraphPtSwClockMonth-June", 6),
          ("wtWebioAn1GraphPtSwClockMonth-March", 3),
          ("wtWebioAn1GraphPtSwClockMonth-May", 5),
          ("wtWebioAn1GraphPtSwClockMonth-November", 11),
          ("wtWebioAn1GraphPtSwClockMonth-October", 10),
          ("wtWebioAn1GraphPtSwClockMonth-September", 9))
    )


_WtWebioAn1GraphPtSwClockMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwClockMonth_Object = MibScalar
wtWebioAn1GraphPtSwClockMonth = _WtWebioAn1GraphPtSwClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3, 4),
    _WtWebioAn1GraphPtSwClockMonth_Type()
)
wtWebioAn1GraphPtSwClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwClockMonth.setStatus("mandatory")


class _WtWebioAn1GraphPtSwClockYear_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebioAn1GraphPtSwClockYear_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwClockYear_Object = MibScalar
wtWebioAn1GraphPtSwClockYear = _WtWebioAn1GraphPtSwClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 2, 3, 5),
    _WtWebioAn1GraphPtSwClockYear_Type()
)
wtWebioAn1GraphPtSwClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwClockYear.setStatus("mandatory")
_WtWebioAn1GraphPtSwBasic_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwBasic = _WtWebioAn1GraphPtSwBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3)
)
_WtWebioAn1GraphPtSwNetwork_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwNetwork = _WtWebioAn1GraphPtSwNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1)
)
_WtWebioAn1GraphPtSwIpAddress_Type = IpAddress
_WtWebioAn1GraphPtSwIpAddress_Object = MibScalar
wtWebioAn1GraphPtSwIpAddress = _WtWebioAn1GraphPtSwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 1),
    _WtWebioAn1GraphPtSwIpAddress_Type()
)
wtWebioAn1GraphPtSwIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwIpAddress.setStatus("mandatory")
_WtWebioAn1GraphPtSwSubnetMask_Type = IpAddress
_WtWebioAn1GraphPtSwSubnetMask_Object = MibScalar
wtWebioAn1GraphPtSwSubnetMask = _WtWebioAn1GraphPtSwSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 2),
    _WtWebioAn1GraphPtSwSubnetMask_Type()
)
wtWebioAn1GraphPtSwSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSubnetMask.setStatus("mandatory")
_WtWebioAn1GraphPtSwGateway_Type = IpAddress
_WtWebioAn1GraphPtSwGateway_Object = MibScalar
wtWebioAn1GraphPtSwGateway = _WtWebioAn1GraphPtSwGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 3),
    _WtWebioAn1GraphPtSwGateway_Type()
)
wtWebioAn1GraphPtSwGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGateway.setStatus("mandatory")
_WtWebioAn1GraphPtSwDnsServer1_Type = OctetString
_WtWebioAn1GraphPtSwDnsServer1_Object = MibScalar
wtWebioAn1GraphPtSwDnsServer1 = _WtWebioAn1GraphPtSwDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 4),
    _WtWebioAn1GraphPtSwDnsServer1_Type()
)
wtWebioAn1GraphPtSwDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDnsServer1.setStatus("mandatory")
_WtWebioAn1GraphPtSwDnsServer2_Type = OctetString
_WtWebioAn1GraphPtSwDnsServer2_Object = MibScalar
wtWebioAn1GraphPtSwDnsServer2 = _WtWebioAn1GraphPtSwDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 5),
    _WtWebioAn1GraphPtSwDnsServer2_Type()
)
wtWebioAn1GraphPtSwDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDnsServer2.setStatus("mandatory")
_WtWebioAn1GraphPtSwAddConfig_Type = OctetString
_WtWebioAn1GraphPtSwAddConfig_Object = MibScalar
wtWebioAn1GraphPtSwAddConfig = _WtWebioAn1GraphPtSwAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 1, 6),
    _WtWebioAn1GraphPtSwAddConfig_Type()
)
wtWebioAn1GraphPtSwAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAddConfig.setStatus("mandatory")
_WtWebioAn1GraphPtSwHTTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwHTTP = _WtWebioAn1GraphPtSwHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 2)
)
_WtWebioAn1GraphPtSwStartup_Type = OctetString
_WtWebioAn1GraphPtSwStartup_Object = MibScalar
wtWebioAn1GraphPtSwStartup = _WtWebioAn1GraphPtSwStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 2, 1),
    _WtWebioAn1GraphPtSwStartup_Type()
)
wtWebioAn1GraphPtSwStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwStartup.setStatus("mandatory")
_WtWebioAn1GraphPtSwGetHeaderEnable_Type = OctetString
_WtWebioAn1GraphPtSwGetHeaderEnable_Object = MibScalar
wtWebioAn1GraphPtSwGetHeaderEnable = _WtWebioAn1GraphPtSwGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 2, 2),
    _WtWebioAn1GraphPtSwGetHeaderEnable_Type()
)
wtWebioAn1GraphPtSwGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGetHeaderEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtSwHttpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwHttpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwHttpPort_Object = MibScalar
wtWebioAn1GraphPtSwHttpPort = _WtWebioAn1GraphPtSwHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 2, 3),
    _WtWebioAn1GraphPtSwHttpPort_Type()
)
wtWebioAn1GraphPtSwHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwHttpPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwMail_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwMail = _WtWebioAn1GraphPtSwMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3)
)
_WtWebioAn1GraphPtSwMailAdName_Type = OctetString
_WtWebioAn1GraphPtSwMailAdName_Object = MibScalar
wtWebioAn1GraphPtSwMailAdName = _WtWebioAn1GraphPtSwMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 1),
    _WtWebioAn1GraphPtSwMailAdName_Type()
)
wtWebioAn1GraphPtSwMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailAdName.setStatus("mandatory")
_WtWebioAn1GraphPtSwMailReply_Type = OctetString
_WtWebioAn1GraphPtSwMailReply_Object = MibScalar
wtWebioAn1GraphPtSwMailReply = _WtWebioAn1GraphPtSwMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 2),
    _WtWebioAn1GraphPtSwMailReply_Type()
)
wtWebioAn1GraphPtSwMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailReply.setStatus("mandatory")
_WtWebioAn1GraphPtSwMailServer_Type = OctetString
_WtWebioAn1GraphPtSwMailServer_Object = MibScalar
wtWebioAn1GraphPtSwMailServer = _WtWebioAn1GraphPtSwMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 3),
    _WtWebioAn1GraphPtSwMailServer_Type()
)
wtWebioAn1GraphPtSwMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebioAn1GraphPtSwMailAuthentication_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwMailAuthentication_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwMailAuthentication_Object = MibScalar
wtWebioAn1GraphPtSwMailAuthentication = _WtWebioAn1GraphPtSwMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 5),
    _WtWebioAn1GraphPtSwMailAuthentication_Type()
)
wtWebioAn1GraphPtSwMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailAuthentication.setStatus("mandatory")
_WtWebioAn1GraphPtSwMailAuthUser_Type = OctetString
_WtWebioAn1GraphPtSwMailAuthUser_Object = MibScalar
wtWebioAn1GraphPtSwMailAuthUser = _WtWebioAn1GraphPtSwMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 6),
    _WtWebioAn1GraphPtSwMailAuthUser_Type()
)
wtWebioAn1GraphPtSwMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailAuthUser.setStatus("mandatory")
_WtWebioAn1GraphPtSwMailAuthPassword_Type = OctetString
_WtWebioAn1GraphPtSwMailAuthPassword_Object = MibScalar
wtWebioAn1GraphPtSwMailAuthPassword = _WtWebioAn1GraphPtSwMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 7),
    _WtWebioAn1GraphPtSwMailAuthPassword_Type()
)
wtWebioAn1GraphPtSwMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailAuthPassword.setStatus("mandatory")
_WtWebioAn1GraphPtSwMailPop3Server_Type = OctetString
_WtWebioAn1GraphPtSwMailPop3Server_Object = MibScalar
wtWebioAn1GraphPtSwMailPop3Server = _WtWebioAn1GraphPtSwMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 3, 8),
    _WtWebioAn1GraphPtSwMailPop3Server_Type()
)
wtWebioAn1GraphPtSwMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMailPop3Server.setStatus("mandatory")
_WtWebioAn1GraphPtSwSNMP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwSNMP = _WtWebioAn1GraphPtSwSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4)
)
_WtWebioAn1GraphPtSwSnmpCommunityStringRead_Type = OctetString
_WtWebioAn1GraphPtSwSnmpCommunityStringRead_Object = MibScalar
wtWebioAn1GraphPtSwSnmpCommunityStringRead = _WtWebioAn1GraphPtSwSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 1),
    _WtWebioAn1GraphPtSwSnmpCommunityStringRead_Type()
)
wtWebioAn1GraphPtSwSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSnmpCommunityStringRead.setStatus("mandatory")
_WtWebioAn1GraphPtSwSnmpCommunityStringReadWrite_Type = OctetString
_WtWebioAn1GraphPtSwSnmpCommunityStringReadWrite_Object = MibScalar
wtWebioAn1GraphPtSwSnmpCommunityStringReadWrite = _WtWebioAn1GraphPtSwSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 2),
    _WtWebioAn1GraphPtSwSnmpCommunityStringReadWrite_Type()
)
wtWebioAn1GraphPtSwSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebioAn1GraphPtSwSystemTrapManagerIP_Type = OctetString
_WtWebioAn1GraphPtSwSystemTrapManagerIP_Object = MibScalar
wtWebioAn1GraphPtSwSystemTrapManagerIP = _WtWebioAn1GraphPtSwSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 3),
    _WtWebioAn1GraphPtSwSystemTrapManagerIP_Type()
)
wtWebioAn1GraphPtSwSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSystemTrapManagerIP.setStatus("mandatory")


class _WtWebioAn1GraphPtSwSystemTrapEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwSystemTrapEnable_Object = MibScalar
wtWebioAn1GraphPtSwSystemTrapEnable = _WtWebioAn1GraphPtSwSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 4),
    _WtWebioAn1GraphPtSwSystemTrapEnable_Type()
)
wtWebioAn1GraphPtSwSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSystemTrapEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSnmpEnable_Type = OctetString
_WtWebioAn1GraphPtSwSnmpEnable_Object = MibScalar
wtWebioAn1GraphPtSwSnmpEnable = _WtWebioAn1GraphPtSwSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 5),
    _WtWebioAn1GraphPtSwSnmpEnable_Type()
)
wtWebioAn1GraphPtSwSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSnmpEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSnmpCommunityStringTrap_Type = OctetString
_WtWebioAn1GraphPtSwSnmpCommunityStringTrap_Object = MibScalar
wtWebioAn1GraphPtSwSnmpCommunityStringTrap = _WtWebioAn1GraphPtSwSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 4, 6),
    _WtWebioAn1GraphPtSwSnmpCommunityStringTrap_Type()
)
wtWebioAn1GraphPtSwSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebioAn1GraphPtSwUDP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwUDP = _WtWebioAn1GraphPtSwUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 5)
)


class _WtWebioAn1GraphPtSwUdpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwUdpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwUdpPort_Object = MibScalar
wtWebioAn1GraphPtSwUdpPort = _WtWebioAn1GraphPtSwUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 5, 1),
    _WtWebioAn1GraphPtSwUdpPort_Type()
)
wtWebioAn1GraphPtSwUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwUdpPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwUdpEnable_Type = OctetString
_WtWebioAn1GraphPtSwUdpEnable_Object = MibScalar
wtWebioAn1GraphPtSwUdpEnable = _WtWebioAn1GraphPtSwUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 5, 2),
    _WtWebioAn1GraphPtSwUdpEnable_Type()
)
wtWebioAn1GraphPtSwUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwUdpEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSyslog_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwSyslog = _WtWebioAn1GraphPtSwSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 6)
)
_WtWebioAn1GraphPtSwSyslogServerIP_Type = OctetString
_WtWebioAn1GraphPtSwSyslogServerIP_Object = MibScalar
wtWebioAn1GraphPtSwSyslogServerIP = _WtWebioAn1GraphPtSwSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 6, 1),
    _WtWebioAn1GraphPtSwSyslogServerIP_Type()
)
wtWebioAn1GraphPtSwSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSyslogServerIP.setStatus("mandatory")
_WtWebioAn1GraphPtSwSyslogServerPort_Type = Integer32
_WtWebioAn1GraphPtSwSyslogServerPort_Object = MibScalar
wtWebioAn1GraphPtSwSyslogServerPort = _WtWebioAn1GraphPtSwSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 6, 2),
    _WtWebioAn1GraphPtSwSyslogServerPort_Type()
)
wtWebioAn1GraphPtSwSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSyslogServerPort.setStatus("mandatory")


class _WtWebioAn1GraphPtSwSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwSyslogSystemMessagesEnable_Object = MibScalar
wtWebioAn1GraphPtSwSyslogSystemMessagesEnable = _WtWebioAn1GraphPtSwSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 6, 3),
    _WtWebioAn1GraphPtSwSyslogSystemMessagesEnable_Type()
)
wtWebioAn1GraphPtSwSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSyslogEnable_Type = OctetString
_WtWebioAn1GraphPtSwSyslogEnable_Object = MibScalar
wtWebioAn1GraphPtSwSyslogEnable = _WtWebioAn1GraphPtSwSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 6, 4),
    _WtWebioAn1GraphPtSwSyslogEnable_Type()
)
wtWebioAn1GraphPtSwSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSyslogEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwFTP = _WtWebioAn1GraphPtSwFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7)
)
_WtWebioAn1GraphPtSwFTPServerIP_Type = OctetString
_WtWebioAn1GraphPtSwFTPServerIP_Object = MibScalar
wtWebioAn1GraphPtSwFTPServerIP = _WtWebioAn1GraphPtSwFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 1),
    _WtWebioAn1GraphPtSwFTPServerIP_Type()
)
wtWebioAn1GraphPtSwFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPServerIP.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPServerControlPort_Type = Integer32
_WtWebioAn1GraphPtSwFTPServerControlPort_Object = MibScalar
wtWebioAn1GraphPtSwFTPServerControlPort = _WtWebioAn1GraphPtSwFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 2),
    _WtWebioAn1GraphPtSwFTPServerControlPort_Type()
)
wtWebioAn1GraphPtSwFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPServerControlPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPUserName_Type = OctetString
_WtWebioAn1GraphPtSwFTPUserName_Object = MibScalar
wtWebioAn1GraphPtSwFTPUserName = _WtWebioAn1GraphPtSwFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 3),
    _WtWebioAn1GraphPtSwFTPUserName_Type()
)
wtWebioAn1GraphPtSwFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPUserName.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPPassword_Type = OctetString
_WtWebioAn1GraphPtSwFTPPassword_Object = MibScalar
wtWebioAn1GraphPtSwFTPPassword = _WtWebioAn1GraphPtSwFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 4),
    _WtWebioAn1GraphPtSwFTPPassword_Type()
)
wtWebioAn1GraphPtSwFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPPassword.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPAccount_Type = OctetString
_WtWebioAn1GraphPtSwFTPAccount_Object = MibScalar
wtWebioAn1GraphPtSwFTPAccount = _WtWebioAn1GraphPtSwFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 5),
    _WtWebioAn1GraphPtSwFTPAccount_Type()
)
wtWebioAn1GraphPtSwFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPAccount.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPOption_Type = OctetString
_WtWebioAn1GraphPtSwFTPOption_Object = MibScalar
wtWebioAn1GraphPtSwFTPOption = _WtWebioAn1GraphPtSwFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 6),
    _WtWebioAn1GraphPtSwFTPOption_Type()
)
wtWebioAn1GraphPtSwFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPOption.setStatus("mandatory")
_WtWebioAn1GraphPtSwFTPEnable_Type = OctetString
_WtWebioAn1GraphPtSwFTPEnable_Object = MibScalar
wtWebioAn1GraphPtSwFTPEnable = _WtWebioAn1GraphPtSwFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 7, 7),
    _WtWebioAn1GraphPtSwFTPEnable_Type()
)
wtWebioAn1GraphPtSwFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwFTPEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwLanguage_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwLanguage = _WtWebioAn1GraphPtSwLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 9)
)
_WtWebioAn1GraphPtSwLanguageSelect_Type = OctetString
_WtWebioAn1GraphPtSwLanguageSelect_Object = MibScalar
wtWebioAn1GraphPtSwLanguageSelect = _WtWebioAn1GraphPtSwLanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 3, 9, 1),
    _WtWebioAn1GraphPtSwLanguageSelect_Type()
)
wtWebioAn1GraphPtSwLanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwLanguageSelect.setStatus("mandatory")
_WtWebioAn1GraphPtSwDatalogger_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwDatalogger = _WtWebioAn1GraphPtSwDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4)
)


class _WtWebioAn1GraphPtSwLoggerTimebase_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwLoggerTimebase based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwDatalogger-15Min", 3),
          ("wtWebioAn1GraphPtSwDatalogger-1Min", 1),
          ("wtWebioAn1GraphPtSwDatalogger-5Min", 2),
          ("wtWebioAn1GraphPtSwDatalogger-60Min", 4))
    )


_WtWebioAn1GraphPtSwLoggerTimebase_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwLoggerTimebase_Object = MibScalar
wtWebioAn1GraphPtSwLoggerTimebase = _WtWebioAn1GraphPtSwLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 1),
    _WtWebioAn1GraphPtSwLoggerTimebase_Type()
)
wtWebioAn1GraphPtSwLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwLoggerTimebase.setStatus("mandatory")


class _WtWebioAn1GraphPtSwLoggerSensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwLoggerSensorSel_Object = MibScalar
wtWebioAn1GraphPtSwLoggerSensorSel = _WtWebioAn1GraphPtSwLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 2),
    _WtWebioAn1GraphPtSwLoggerSensorSel_Type()
)
wtWebioAn1GraphPtSwLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwLoggerSensorSel.setStatus("mandatory")


class _WtWebioAn1GraphPtSwDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphPtSwDisplaySensorSel = _WtWebioAn1GraphPtSwDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 3),
    _WtWebioAn1GraphPtSwDisplaySensorSel_Type()
)
wtWebioAn1GraphPtSwDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDisplaySensorSel.setStatus("mandatory")
_WtWebioAn1GraphPtSwSensorColorTable_Object = MibTable
wtWebioAn1GraphPtSwSensorColorTable = _WtWebioAn1GraphPtSwSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwSensorColorEntry_Object = MibTableRow
wtWebioAn1GraphPtSwSensorColorEntry = _WtWebioAn1GraphPtSwSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 4, 1)
)
wtWebioAn1GraphPtSwSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtSwSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwSensorColor_Object = MibTableColumn
wtWebioAn1GraphPtSwSensorColor = _WtWebioAn1GraphPtSwSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 4, 1, 1),
    _WtWebioAn1GraphPtSwSensorColor_Type()
)
wtWebioAn1GraphPtSwSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwSensorColor.setStatus("mandatory")
_WtWebioAn1GraphPtSwAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphPtSwAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphPtSwAutoScaleEnable = _WtWebioAn1GraphPtSwAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 5),
    _WtWebioAn1GraphPtSwAutoScaleEnable_Type()
)
wtWebioAn1GraphPtSwAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwVerticalUpperLimit_Type = OctetString
_WtWebioAn1GraphPtSwVerticalUpperLimit_Object = MibScalar
wtWebioAn1GraphPtSwVerticalUpperLimit = _WtWebioAn1GraphPtSwVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 6),
    _WtWebioAn1GraphPtSwVerticalUpperLimit_Type()
)
wtWebioAn1GraphPtSwVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwVerticalUpperLimit.setStatus("mandatory")
_WtWebioAn1GraphPtSwVerticalLowerLimit_Type = OctetString
_WtWebioAn1GraphPtSwVerticalLowerLimit_Object = MibScalar
wtWebioAn1GraphPtSwVerticalLowerLimit = _WtWebioAn1GraphPtSwVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 7),
    _WtWebioAn1GraphPtSwVerticalLowerLimit_Type()
)
wtWebioAn1GraphPtSwVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwVerticalLowerLimit.setStatus("mandatory")


class _WtWebioAn1GraphPtSwHorizontalZoom_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwHorizontalZoom based on Integer32"""
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
        *(("wtWebioAn1GraphPtSwZoom-25days", 6),
          ("wtWebioAn1GraphPtSwZoom-25min", 1),
          ("wtWebioAn1GraphPtSwZoom-30hrs", 4),
          ("wtWebioAn1GraphPtSwZoom-5days", 5),
          ("wtWebioAn1GraphPtSwZoom-5hrs", 3),
          ("wtWebioAn1GraphPtSwZoom-75min", 2))
    )


_WtWebioAn1GraphPtSwHorizontalZoom_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwHorizontalZoom_Object = MibScalar
wtWebioAn1GraphPtSwHorizontalZoom = _WtWebioAn1GraphPtSwHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 4, 8),
    _WtWebioAn1GraphPtSwHorizontalZoom_Type()
)
wtWebioAn1GraphPtSwHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwHorizontalZoom.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarm_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwAlarm = _WtWebioAn1GraphPtSwAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5)
)


class _WtWebioAn1GraphPtSwAlarmCount_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphPtSwAlarmCount_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwAlarmCount_Object = MibScalar
wtWebioAn1GraphPtSwAlarmCount = _WtWebioAn1GraphPtSwAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 1),
    _WtWebioAn1GraphPtSwAlarmCount_Type()
)
wtWebioAn1GraphPtSwAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmCount.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmIfTable_Object = MibTable
wtWebioAn1GraphPtSwAlarmIfTable = _WtWebioAn1GraphPtSwAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmIfTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmIfEntry_Object = MibTableRow
wtWebioAn1GraphPtSwAlarmIfEntry = _WtWebioAn1GraphPtSwAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 2, 1)
)
wtWebioAn1GraphPtSwAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmIfEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmNo_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphPtSwAlarmNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwAlarmNo_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmNo = _WtWebioAn1GraphPtSwAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 2, 1, 1),
    _WtWebioAn1GraphPtSwAlarmNo_Type()
)
wtWebioAn1GraphPtSwAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmNo.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmTable_Object = MibTable
wtWebioAn1GraphPtSwAlarmTable = _WtWebioAn1GraphPtSwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmEntry_Object = MibTableRow
wtWebioAn1GraphPtSwAlarmEntry = _WtWebioAn1GraphPtSwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1)
)
wtWebioAn1GraphPtSwAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmTrigger_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwAlarmTrigger_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwAlarmTrigger_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTrigger = _WtWebioAn1GraphPtSwAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 1),
    _WtWebioAn1GraphPtSwAlarmTrigger_Type()
)
wtWebioAn1GraphPtSwAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTrigger.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmMin_Type = OctetString
_WtWebioAn1GraphPtSwAlarmMin_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmMin = _WtWebioAn1GraphPtSwAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 2),
    _WtWebioAn1GraphPtSwAlarmMin_Type()
)
wtWebioAn1GraphPtSwAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmMin.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmMax_Type = OctetString
_WtWebioAn1GraphPtSwAlarmMax_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmMax = _WtWebioAn1GraphPtSwAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 3),
    _WtWebioAn1GraphPtSwAlarmMax_Type()
)
wtWebioAn1GraphPtSwAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmMax.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmHysteresis_Type = OctetString
_WtWebioAn1GraphPtSwAlarmHysteresis_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmHysteresis = _WtWebioAn1GraphPtSwAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 4),
    _WtWebioAn1GraphPtSwAlarmHysteresis_Type()
)
wtWebioAn1GraphPtSwAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmHysteresis.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmDelay_Type = OctetString
_WtWebioAn1GraphPtSwAlarmDelay_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmDelay = _WtWebioAn1GraphPtSwAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 5),
    _WtWebioAn1GraphPtSwAlarmDelay_Type()
)
wtWebioAn1GraphPtSwAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmDelay.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmInterval_Type = OctetString
_WtWebioAn1GraphPtSwAlarmInterval_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmInterval = _WtWebioAn1GraphPtSwAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 6),
    _WtWebioAn1GraphPtSwAlarmInterval_Type()
)
wtWebioAn1GraphPtSwAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmInterval.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwAlarmEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwAlarmEnable_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmEnable = _WtWebioAn1GraphPtSwAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 7),
    _WtWebioAn1GraphPtSwAlarmEnable_Type()
)
wtWebioAn1GraphPtSwAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmEMailAddr_Type = OctetString
_WtWebioAn1GraphPtSwAlarmEMailAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmEMailAddr = _WtWebioAn1GraphPtSwAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 8),
    _WtWebioAn1GraphPtSwAlarmEMailAddr_Type()
)
wtWebioAn1GraphPtSwAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmEMailAddr.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmMailSubject_Type = OctetString
_WtWebioAn1GraphPtSwAlarmMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmMailSubject = _WtWebioAn1GraphPtSwAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 9),
    _WtWebioAn1GraphPtSwAlarmMailSubject_Type()
)
wtWebioAn1GraphPtSwAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmMailText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmMailText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmMailText = _WtWebioAn1GraphPtSwAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 10),
    _WtWebioAn1GraphPtSwAlarmMailText_Type()
)
wtWebioAn1GraphPtSwAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmMailText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmManagerIP_Type = OctetString
_WtWebioAn1GraphPtSwAlarmManagerIP_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmManagerIP = _WtWebioAn1GraphPtSwAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 11),
    _WtWebioAn1GraphPtSwAlarmManagerIP_Type()
)
wtWebioAn1GraphPtSwAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmManagerIP.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmTrapText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmTrapText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTrapText = _WtWebioAn1GraphPtSwAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 12),
    _WtWebioAn1GraphPtSwAlarmTrapText_Type()
)
wtWebioAn1GraphPtSwAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTrapText.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmMailOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwAlarmMailOptions_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmMailOptions = _WtWebioAn1GraphPtSwAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 13),
    _WtWebioAn1GraphPtSwAlarmMailOptions_Type()
)
wtWebioAn1GraphPtSwAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmMailOptions.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmTcpIpAddr_Type = OctetString
_WtWebioAn1GraphPtSwAlarmTcpIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTcpIpAddr = _WtWebioAn1GraphPtSwAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 14),
    _WtWebioAn1GraphPtSwAlarmTcpIpAddr_Type()
)
wtWebioAn1GraphPtSwAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmTcpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwAlarmTcpPort_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTcpPort = _WtWebioAn1GraphPtSwAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 15),
    _WtWebioAn1GraphPtSwAlarmTcpPort_Type()
)
wtWebioAn1GraphPtSwAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTcpPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmTcpText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmTcpText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTcpText = _WtWebioAn1GraphPtSwAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 16),
    _WtWebioAn1GraphPtSwAlarmTcpText_Type()
)
wtWebioAn1GraphPtSwAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmClearMailSubject_Type = OctetString
_WtWebioAn1GraphPtSwAlarmClearMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmClearMailSubject = _WtWebioAn1GraphPtSwAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 17),
    _WtWebioAn1GraphPtSwAlarmClearMailSubject_Type()
)
wtWebioAn1GraphPtSwAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmClearMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmClearMailText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmClearMailText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmClearMailText = _WtWebioAn1GraphPtSwAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 18),
    _WtWebioAn1GraphPtSwAlarmClearMailText_Type()
)
wtWebioAn1GraphPtSwAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmClearMailText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmClearTrapText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmClearTrapText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmClearTrapText = _WtWebioAn1GraphPtSwAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 19),
    _WtWebioAn1GraphPtSwAlarmClearTrapText_Type()
)
wtWebioAn1GraphPtSwAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmClearTrapText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmClearTcpText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmClearTcpText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmClearTcpText = _WtWebioAn1GraphPtSwAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 20),
    _WtWebioAn1GraphPtSwAlarmClearTcpText_Type()
)
wtWebioAn1GraphPtSwAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmClearTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmSyslogIpAddr_Type = IpAddress
_WtWebioAn1GraphPtSwAlarmSyslogIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmSyslogIpAddr = _WtWebioAn1GraphPtSwAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 21),
    _WtWebioAn1GraphPtSwAlarmSyslogIpAddr_Type()
)
wtWebioAn1GraphPtSwAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwAlarmSyslogPort_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmSyslogPort = _WtWebioAn1GraphPtSwAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 22),
    _WtWebioAn1GraphPtSwAlarmSyslogPort_Type()
)
wtWebioAn1GraphPtSwAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmSyslogPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmSyslogText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmSyslogText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmSyslogText = _WtWebioAn1GraphPtSwAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 23),
    _WtWebioAn1GraphPtSwAlarmSyslogText_Type()
)
wtWebioAn1GraphPtSwAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmSyslogText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmSyslogClearText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmSyslogClearText_Object = MibScalar
wtWebioAn1GraphPtSwAlarmSyslogClearText = _WtWebioAn1GraphPtSwAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 24),
    _WtWebioAn1GraphPtSwAlarmSyslogClearText_Type()
)
wtWebioAn1GraphPtSwAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmSyslogClearText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmFtpDataPort_Type = OctetString
_WtWebioAn1GraphPtSwAlarmFtpDataPort_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmFtpDataPort = _WtWebioAn1GraphPtSwAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 25),
    _WtWebioAn1GraphPtSwAlarmFtpDataPort_Type()
)
wtWebioAn1GraphPtSwAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmFtpDataPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmFtpFileName_Type = OctetString
_WtWebioAn1GraphPtSwAlarmFtpFileName_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmFtpFileName = _WtWebioAn1GraphPtSwAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 26),
    _WtWebioAn1GraphPtSwAlarmFtpFileName_Type()
)
wtWebioAn1GraphPtSwAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmFtpFileName.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmFtpText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmFtpText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmFtpText = _WtWebioAn1GraphPtSwAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 27),
    _WtWebioAn1GraphPtSwAlarmFtpText_Type()
)
wtWebioAn1GraphPtSwAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmFtpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmFtpClearText_Type = OctetString
_WtWebioAn1GraphPtSwAlarmFtpClearText_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmFtpClearText = _WtWebioAn1GraphPtSwAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 28),
    _WtWebioAn1GraphPtSwAlarmFtpClearText_Type()
)
wtWebioAn1GraphPtSwAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmFtpClearText.setStatus("mandatory")


class _WtWebioAn1GraphPtSwAlarmFtpOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwAlarmFtpOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwAlarmFtpOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwAlarmFtpOptions_Object = MibScalar
wtWebioAn1GraphPtSwAlarmFtpOptions = _WtWebioAn1GraphPtSwAlarmFtpOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 29),
    _WtWebioAn1GraphPtSwAlarmFtpOptions_Type()
)
wtWebioAn1GraphPtSwAlarmFtpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmFtpOptions.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmTimerCron_Type = OctetString
_WtWebioAn1GraphPtSwAlarmTimerCron_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmTimerCron = _WtWebioAn1GraphPtSwAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 30),
    _WtWebioAn1GraphPtSwAlarmTimerCron_Type()
)
wtWebioAn1GraphPtSwAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmTimerCron.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmDeltaTemp_Type = OctetString
_WtWebioAn1GraphPtSwAlarmDeltaTemp_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmDeltaTemp = _WtWebioAn1GraphPtSwAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 31),
    _WtWebioAn1GraphPtSwAlarmDeltaTemp_Type()
)
wtWebioAn1GraphPtSwAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmDeltaTemp.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmName_Type = OctetString
_WtWebioAn1GraphPtSwAlarmName_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmName = _WtWebioAn1GraphPtSwAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 39),
    _WtWebioAn1GraphPtSwAlarmName_Type()
)
wtWebioAn1GraphPtSwAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmName.setStatus("mandatory")
_WtWebioAn1GraphPtSwAlarmActive_Type = OctetString
_WtWebioAn1GraphPtSwAlarmActive_Object = MibTableColumn
wtWebioAn1GraphPtSwAlarmActive = _WtWebioAn1GraphPtSwAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 5, 3, 1, 40),
    _WtWebioAn1GraphPtSwAlarmActive_Type()
)
wtWebioAn1GraphPtSwAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlarmActive.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphics_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwGraphics = _WtWebioAn1GraphPtSwGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6)
)
_WtWebioAn1GraphPtSwGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwGraphicsBase = _WtWebioAn1GraphPtSwGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1)
)
_WtWebioAn1GraphPtSwGraphicsBaseEnable_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsBaseEnable_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBaseEnable = _WtWebioAn1GraphPtSwGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 1),
    _WtWebioAn1GraphPtSwGraphicsBaseEnable_Type()
)
wtWebioAn1GraphPtSwGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBaseEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsBaseWidth_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsBaseWidth_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBaseWidth = _WtWebioAn1GraphPtSwGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 2),
    _WtWebioAn1GraphPtSwGraphicsBaseWidth_Type()
)
wtWebioAn1GraphPtSwGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBaseWidth.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsBaseHeight_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsBaseHeight_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBaseHeight = _WtWebioAn1GraphPtSwGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 3),
    _WtWebioAn1GraphPtSwGraphicsBaseHeight_Type()
)
wtWebioAn1GraphPtSwGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBaseHeight.setStatus("mandatory")


class _WtWebioAn1GraphPtSwGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtSwGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwGraphicsBaseFrameColor_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBaseFrameColor = _WtWebioAn1GraphPtSwGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 4),
    _WtWebioAn1GraphPtSwGraphicsBaseFrameColor_Type()
)
wtWebioAn1GraphPtSwGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebioAn1GraphPtSwGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtSwGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwGraphicsBaseBackgroundColor_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor = _WtWebioAn1GraphPtSwGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 5),
    _WtWebioAn1GraphPtSwGraphicsBaseBackgroundColor_Type()
)
wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsBasePollingrate_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsBasePollingrate_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsBasePollingrate = _WtWebioAn1GraphPtSwGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 1, 6),
    _WtWebioAn1GraphPtSwGraphicsBasePollingrate_Type()
)
wtWebioAn1GraphPtSwGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsBasePollingrate.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwGraphicsSelect = _WtWebioAn1GraphPtSwGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2)
)


class _WtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel = _WtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 1),
    _WtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel_Type()
)
wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem = _WtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 2),
    _WtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem_Type()
)
wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebioAn1GraphPtSw2SensorColorTable_Object = MibTable
wtWebioAn1GraphPtSw2SensorColorTable = _WtWebioAn1GraphPtSw2SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSw2SensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphPtSw2SensorColorEntry_Object = MibTableRow
wtWebioAn1GraphPtSw2SensorColorEntry = _WtWebioAn1GraphPtSw2SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 3, 1)
)
wtWebioAn1GraphPtSw2SensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSw2SensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSw2GraphicsSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSw2GraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WtWebioAn1GraphPtSw2GraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSw2GraphicsSensorColor_Object = MibTableColumn
wtWebioAn1GraphPtSw2GraphicsSensorColor = _WtWebioAn1GraphPtSw2GraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 3, 1, 1),
    _WtWebioAn1GraphPtSw2GraphicsSensorColor_Type()
)
wtWebioAn1GraphPtSw2GraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSw2GraphicsSensorColor.setStatus("mandatory")
_WtWebioAn1GraphPtSw2GraphicsSelectScale_Type = OctetString
_WtWebioAn1GraphPtSw2GraphicsSelectScale_Object = MibTableColumn
wtWebioAn1GraphPtSw2GraphicsSelectScale = _WtWebioAn1GraphPtSw2GraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 2, 3, 1, 2),
    _WtWebioAn1GraphPtSw2GraphicsSelectScale_Type()
)
wtWebioAn1GraphPtSw2GraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSw2GraphicsSelectScale.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwGraphicsScale = _WtWebioAn1GraphPtSwGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3)
)
_WtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable = _WtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 1),
    _WtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable_Type()
)
wtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable = _WtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 2),
    _WtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable_Type()
)
wtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale1Min_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale1Min_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale1Min = _WtWebioAn1GraphPtSwGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 3),
    _WtWebioAn1GraphPtSwGraphicsScale1Min_Type()
)
wtWebioAn1GraphPtSwGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale1Min.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale2Min_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale2Min_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale2Min = _WtWebioAn1GraphPtSwGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 4),
    _WtWebioAn1GraphPtSwGraphicsScale2Min_Type()
)
wtWebioAn1GraphPtSwGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale2Min.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale3Min_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale3Min_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale3Min = _WtWebioAn1GraphPtSwGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 5),
    _WtWebioAn1GraphPtSwGraphicsScale3Min_Type()
)
wtWebioAn1GraphPtSwGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale3Min.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale4Min_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale4Min_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale4Min = _WtWebioAn1GraphPtSwGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 6),
    _WtWebioAn1GraphPtSwGraphicsScale4Min_Type()
)
wtWebioAn1GraphPtSwGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale4Min.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale1Max_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale1Max_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale1Max = _WtWebioAn1GraphPtSwGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 7),
    _WtWebioAn1GraphPtSwGraphicsScale1Max_Type()
)
wtWebioAn1GraphPtSwGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale1Max.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale2Max_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale2Max_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale2Max = _WtWebioAn1GraphPtSwGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 8),
    _WtWebioAn1GraphPtSwGraphicsScale2Max_Type()
)
wtWebioAn1GraphPtSwGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale2Max.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale3Max_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale3Max_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale3Max = _WtWebioAn1GraphPtSwGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 9),
    _WtWebioAn1GraphPtSwGraphicsScale3Max_Type()
)
wtWebioAn1GraphPtSwGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale3Max.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale4Max_Type = Integer32
_WtWebioAn1GraphPtSwGraphicsScale4Max_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale4Max = _WtWebioAn1GraphPtSwGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 10),
    _WtWebioAn1GraphPtSwGraphicsScale4Max_Type()
)
wtWebioAn1GraphPtSwGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale4Max.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale1Unit_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScale1Unit_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale1Unit = _WtWebioAn1GraphPtSwGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 11),
    _WtWebioAn1GraphPtSwGraphicsScale1Unit_Type()
)
wtWebioAn1GraphPtSwGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale1Unit.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale2Unit_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScale2Unit_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale2Unit = _WtWebioAn1GraphPtSwGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 12),
    _WtWebioAn1GraphPtSwGraphicsScale2Unit_Type()
)
wtWebioAn1GraphPtSwGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale2Unit.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale3Unit_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScale3Unit_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale3Unit = _WtWebioAn1GraphPtSwGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 13),
    _WtWebioAn1GraphPtSwGraphicsScale3Unit_Type()
)
wtWebioAn1GraphPtSwGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale3Unit.setStatus("mandatory")
_WtWebioAn1GraphPtSwGraphicsScale4Unit_Type = OctetString
_WtWebioAn1GraphPtSwGraphicsScale4Unit_Object = MibScalar
wtWebioAn1GraphPtSwGraphicsScale4Unit = _WtWebioAn1GraphPtSwGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 6, 3, 14),
    _WtWebioAn1GraphPtSwGraphicsScale4Unit_Type()
)
wtWebioAn1GraphPtSwGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwGraphicsScale4Unit.setStatus("mandatory")
_WtWebioAn1GraphPtSwReport_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwReport = _WtWebioAn1GraphPtSwReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7)
)


class _WtWebioAn1GraphPtSwReportCount_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphPtSwReportCount_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwReportCount_Object = MibScalar
wtWebioAn1GraphPtSwReportCount = _WtWebioAn1GraphPtSwReportCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 1),
    _WtWebioAn1GraphPtSwReportCount_Type()
)
wtWebioAn1GraphPtSwReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportCount.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportIfTable_Object = MibTable
wtWebioAn1GraphPtSwReportIfTable = _WtWebioAn1GraphPtSwReportIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportIfTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportIfEntry_Object = MibTableRow
wtWebioAn1GraphPtSwReportIfEntry = _WtWebioAn1GraphPtSwReportIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 2, 1)
)
wtWebioAn1GraphPtSwReportIfEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwReportNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportIfEntry.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportNo_Type = Integer32
_WtWebioAn1GraphPtSwReportNo_Object = MibTableColumn
wtWebioAn1GraphPtSwReportNo = _WtWebioAn1GraphPtSwReportNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 2, 1, 1),
    _WtWebioAn1GraphPtSwReportNo_Type()
)
wtWebioAn1GraphPtSwReportNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportNo.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportTable_Object = MibTable
wtWebioAn1GraphPtSwReportTable = _WtWebioAn1GraphPtSwReportTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportEntry_Object = MibTableRow
wtWebioAn1GraphPtSwReportEntry = _WtWebioAn1GraphPtSwReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1)
)
wtWebioAn1GraphPtSwReportEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwReportNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportEntry.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwReportEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwReportEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwReportEnable_Object = MibTableColumn
wtWebioAn1GraphPtSwReportEnable = _WtWebioAn1GraphPtSwReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 1),
    _WtWebioAn1GraphPtSwReportEnable_Type()
)
wtWebioAn1GraphPtSwReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportTimerCron_Type = OctetString
_WtWebioAn1GraphPtSwReportTimerCron_Object = MibTableColumn
wtWebioAn1GraphPtSwReportTimerCron = _WtWebioAn1GraphPtSwReportTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 2),
    _WtWebioAn1GraphPtSwReportTimerCron_Type()
)
wtWebioAn1GraphPtSwReportTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTimerCron.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportMethodeEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwReportMethodeEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwReportMethodeEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwReportMethodeEnable_Object = MibTableColumn
wtWebioAn1GraphPtSwReportMethodeEnable = _WtWebioAn1GraphPtSwReportMethodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 3),
    _WtWebioAn1GraphPtSwReportMethodeEnable_Type()
)
wtWebioAn1GraphPtSwReportMethodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportMethodeEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportEMailAddr_Type = OctetString
_WtWebioAn1GraphPtSwReportEMailAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwReportEMailAddr = _WtWebioAn1GraphPtSwReportEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 8),
    _WtWebioAn1GraphPtSwReportEMailAddr_Type()
)
wtWebioAn1GraphPtSwReportEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportEMailAddr.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportMailSubject_Type = OctetString
_WtWebioAn1GraphPtSwReportMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtSwReportMailSubject = _WtWebioAn1GraphPtSwReportMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 9),
    _WtWebioAn1GraphPtSwReportMailSubject_Type()
)
wtWebioAn1GraphPtSwReportMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportMailText_Type = OctetString
_WtWebioAn1GraphPtSwReportMailText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportMailText = _WtWebioAn1GraphPtSwReportMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 10),
    _WtWebioAn1GraphPtSwReportMailText_Type()
)
wtWebioAn1GraphPtSwReportMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportMailText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportManagerIP_Type = OctetString
_WtWebioAn1GraphPtSwReportManagerIP_Object = MibTableColumn
wtWebioAn1GraphPtSwReportManagerIP = _WtWebioAn1GraphPtSwReportManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 11),
    _WtWebioAn1GraphPtSwReportManagerIP_Type()
)
wtWebioAn1GraphPtSwReportManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportManagerIP.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportTrapText_Type = OctetString
_WtWebioAn1GraphPtSwReportTrapText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportTrapText = _WtWebioAn1GraphPtSwReportTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 12),
    _WtWebioAn1GraphPtSwReportTrapText_Type()
)
wtWebioAn1GraphPtSwReportTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTrapText.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportMailOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwReportMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwReportMailOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwReportMailOptions_Object = MibTableColumn
wtWebioAn1GraphPtSwReportMailOptions = _WtWebioAn1GraphPtSwReportMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 13),
    _WtWebioAn1GraphPtSwReportMailOptions_Type()
)
wtWebioAn1GraphPtSwReportMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportMailOptions.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportTcpIpAddr_Type = OctetString
_WtWebioAn1GraphPtSwReportTcpIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwReportTcpIpAddr = _WtWebioAn1GraphPtSwReportTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 14),
    _WtWebioAn1GraphPtSwReportTcpIpAddr_Type()
)
wtWebioAn1GraphPtSwReportTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTcpIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportTcpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwReportTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwReportTcpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwReportTcpPort_Object = MibTableColumn
wtWebioAn1GraphPtSwReportTcpPort = _WtWebioAn1GraphPtSwReportTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 15),
    _WtWebioAn1GraphPtSwReportTcpPort_Type()
)
wtWebioAn1GraphPtSwReportTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTcpPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportTcpText_Type = OctetString
_WtWebioAn1GraphPtSwReportTcpText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportTcpText = _WtWebioAn1GraphPtSwReportTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 16),
    _WtWebioAn1GraphPtSwReportTcpText_Type()
)
wtWebioAn1GraphPtSwReportTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportClearMailSubject_Type = OctetString
_WtWebioAn1GraphPtSwReportClearMailSubject_Object = MibTableColumn
wtWebioAn1GraphPtSwReportClearMailSubject = _WtWebioAn1GraphPtSwReportClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 17),
    _WtWebioAn1GraphPtSwReportClearMailSubject_Type()
)
wtWebioAn1GraphPtSwReportClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportClearMailSubject.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportClearMailText_Type = OctetString
_WtWebioAn1GraphPtSwReportClearMailText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportClearMailText = _WtWebioAn1GraphPtSwReportClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 18),
    _WtWebioAn1GraphPtSwReportClearMailText_Type()
)
wtWebioAn1GraphPtSwReportClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportClearMailText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportClearTrapText_Type = OctetString
_WtWebioAn1GraphPtSwReportClearTrapText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportClearTrapText = _WtWebioAn1GraphPtSwReportClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 19),
    _WtWebioAn1GraphPtSwReportClearTrapText_Type()
)
wtWebioAn1GraphPtSwReportClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportClearTrapText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportClearTcpText_Type = OctetString
_WtWebioAn1GraphPtSwReportClearTcpText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportClearTcpText = _WtWebioAn1GraphPtSwReportClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 20),
    _WtWebioAn1GraphPtSwReportClearTcpText_Type()
)
wtWebioAn1GraphPtSwReportClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportClearTcpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportSyslogIpAddr_Type = OctetString
_WtWebioAn1GraphPtSwReportSyslogIpAddr_Object = MibTableColumn
wtWebioAn1GraphPtSwReportSyslogIpAddr = _WtWebioAn1GraphPtSwReportSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 24),
    _WtWebioAn1GraphPtSwReportSyslogIpAddr_Type()
)
wtWebioAn1GraphPtSwReportSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportSyslogPort_Type(Integer32):
    """Custom type wtWebioAn1GraphPtSwReportSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphPtSwReportSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphPtSwReportSyslogPort_Object = MibTableColumn
wtWebioAn1GraphPtSwReportSyslogPort = _WtWebioAn1GraphPtSwReportSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 25),
    _WtWebioAn1GraphPtSwReportSyslogPort_Type()
)
wtWebioAn1GraphPtSwReportSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportSyslogPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportSyslogText_Type = OctetString
_WtWebioAn1GraphPtSwReportSyslogText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportSyslogText = _WtWebioAn1GraphPtSwReportSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 26),
    _WtWebioAn1GraphPtSwReportSyslogText_Type()
)
wtWebioAn1GraphPtSwReportSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportSyslogText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportSyslogClearText_Type = OctetString
_WtWebioAn1GraphPtSwReportSyslogClearText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportSyslogClearText = _WtWebioAn1GraphPtSwReportSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 27),
    _WtWebioAn1GraphPtSwReportSyslogClearText_Type()
)
wtWebioAn1GraphPtSwReportSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportSyslogClearText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportFtpDataPort_Type = OctetString
_WtWebioAn1GraphPtSwReportFtpDataPort_Object = MibTableColumn
wtWebioAn1GraphPtSwReportFtpDataPort = _WtWebioAn1GraphPtSwReportFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 28),
    _WtWebioAn1GraphPtSwReportFtpDataPort_Type()
)
wtWebioAn1GraphPtSwReportFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportFtpDataPort.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportFtpFileName_Type = OctetString
_WtWebioAn1GraphPtSwReportFtpFileName_Object = MibTableColumn
wtWebioAn1GraphPtSwReportFtpFileName = _WtWebioAn1GraphPtSwReportFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 29),
    _WtWebioAn1GraphPtSwReportFtpFileName_Type()
)
wtWebioAn1GraphPtSwReportFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportFtpFileName.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportFtpText_Type = OctetString
_WtWebioAn1GraphPtSwReportFtpText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportFtpText = _WtWebioAn1GraphPtSwReportFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 30),
    _WtWebioAn1GraphPtSwReportFtpText_Type()
)
wtWebioAn1GraphPtSwReportFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportFtpText.setStatus("mandatory")
_WtWebioAn1GraphPtSwReportFtpClearText_Type = OctetString
_WtWebioAn1GraphPtSwReportFtpClearText_Object = MibTableColumn
wtWebioAn1GraphPtSwReportFtpClearText = _WtWebioAn1GraphPtSwReportFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 31),
    _WtWebioAn1GraphPtSwReportFtpClearText_Type()
)
wtWebioAn1GraphPtSwReportFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportFtpClearText.setStatus("mandatory")


class _WtWebioAn1GraphPtSwReportFtpOption_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwReportFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwReportFtpOption_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwReportFtpOption_Object = MibTableColumn
wtWebioAn1GraphPtSwReportFtpOption = _WtWebioAn1GraphPtSwReportFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 1, 7, 3, 1, 32),
    _WtWebioAn1GraphPtSwReportFtpOption_Type()
)
wtWebioAn1GraphPtSwReportFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwReportFtpOption.setStatus("mandatory")
_WtWebioAn1GraphPtSwPorts_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwPorts = _WtWebioAn1GraphPtSwPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2)
)
_WtWebioAn1GraphPtSwPortTable_Object = MibTable
wtWebioAn1GraphPtSwPortTable = _WtWebioAn1GraphPtSwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortEntry_Object = MibTableRow
wtWebioAn1GraphPtSwPortEntry = _WtWebioAn1GraphPtSwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1)
)
wtWebioAn1GraphPtSwPortEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortEntry.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortName_Type = OctetString
_WtWebioAn1GraphPtSwPortName_Object = MibTableColumn
wtWebioAn1GraphPtSwPortName = _WtWebioAn1GraphPtSwPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 1),
    _WtWebioAn1GraphPtSwPortName_Type()
)
wtWebioAn1GraphPtSwPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortName.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortText_Type = OctetString
_WtWebioAn1GraphPtSwPortText_Object = MibTableColumn
wtWebioAn1GraphPtSwPortText = _WtWebioAn1GraphPtSwPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 2),
    _WtWebioAn1GraphPtSwPortText_Type()
)
wtWebioAn1GraphPtSwPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortText.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOffset1_Type = OctetString
_WtWebioAn1GraphPtSwPortOffset1_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOffset1 = _WtWebioAn1GraphPtSwPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 3),
    _WtWebioAn1GraphPtSwPortOffset1_Type()
)
wtWebioAn1GraphPtSwPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOffset1.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortTemperature1_Type = OctetString
_WtWebioAn1GraphPtSwPortTemperature1_Object = MibTableColumn
wtWebioAn1GraphPtSwPortTemperature1 = _WtWebioAn1GraphPtSwPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 4),
    _WtWebioAn1GraphPtSwPortTemperature1_Type()
)
wtWebioAn1GraphPtSwPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortTemperature1.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOffset2_Type = OctetString
_WtWebioAn1GraphPtSwPortOffset2_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOffset2 = _WtWebioAn1GraphPtSwPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 5),
    _WtWebioAn1GraphPtSwPortOffset2_Type()
)
wtWebioAn1GraphPtSwPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOffset2.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortTemperature2_Type = OctetString
_WtWebioAn1GraphPtSwPortTemperature2_Object = MibTableColumn
wtWebioAn1GraphPtSwPortTemperature2 = _WtWebioAn1GraphPtSwPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 6),
    _WtWebioAn1GraphPtSwPortTemperature2_Type()
)
wtWebioAn1GraphPtSwPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortTemperature2.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortComment_Type = OctetString
_WtWebioAn1GraphPtSwPortComment_Object = MibTableColumn
wtWebioAn1GraphPtSwPortComment = _WtWebioAn1GraphPtSwPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 7),
    _WtWebioAn1GraphPtSwPortComment_Type()
)
wtWebioAn1GraphPtSwPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortComment.setStatus("mandatory")


class _WtWebioAn1GraphPtSwPortSensorSelect_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwPortSensorSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwPortSensorSelect_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwPortSensorSelect_Object = MibScalar
wtWebioAn1GraphPtSwPortSensorSelect = _WtWebioAn1GraphPtSwPortSensorSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 8),
    _WtWebioAn1GraphPtSwPortSensorSelect_Type()
)
wtWebioAn1GraphPtSwPortSensorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortSensorSelect.setStatus("mandatory")


class _WtWebioAn1GraphPtSwPortSensorUnit_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwPortSensorUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwPortSensorUnit_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwPortSensorUnit_Object = MibTableColumn
wtWebioAn1GraphPtSwPortSensorUnit = _WtWebioAn1GraphPtSwPortSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 1, 1, 9),
    _WtWebioAn1GraphPtSwPortSensorUnit_Type()
)
wtWebioAn1GraphPtSwPortSensorUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortSensorUnit.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOutputTable_Object = MibTable
wtWebioAn1GraphPtSwPortOutputTable = _WtWebioAn1GraphPtSwPortOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputTable.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOutputEntry_Object = MibTableRow
wtWebioAn1GraphPtSwPortOutputEntry = _WtWebioAn1GraphPtSwPortOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1)
)
wtWebioAn1GraphPtSwPortOutputEntry.setIndexNames(
    (0, "WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwOutputNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputEntry.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOutputName_Type = OctetString
_WtWebioAn1GraphPtSwPortOutputName_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOutputName = _WtWebioAn1GraphPtSwPortOutputName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1, 1),
    _WtWebioAn1GraphPtSwPortOutputName_Type()
)
wtWebioAn1GraphPtSwPortOutputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputName.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOutputText_Type = OctetString
_WtWebioAn1GraphPtSwPortOutputText_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOutputText = _WtWebioAn1GraphPtSwPortOutputText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1, 2),
    _WtWebioAn1GraphPtSwPortOutputText_Type()
)
wtWebioAn1GraphPtSwPortOutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputText.setStatus("mandatory")


class _WtWebioAn1GraphPtSwPortOutputPolarity_Type(OctetString):
    """Custom type wtWebioAn1GraphPtSwPortOutputPolarity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPtSwPortOutputPolarity_Type.__name__ = "OctetString"
_WtWebioAn1GraphPtSwPortOutputPolarity_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOutputPolarity = _WtWebioAn1GraphPtSwPortOutputPolarity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1, 3),
    _WtWebioAn1GraphPtSwPortOutputPolarity_Type()
)
wtWebioAn1GraphPtSwPortOutputPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputPolarity.setStatus("mandatory")
_WtWebioAn1GraphPtSwPortOutputComment_Type = OctetString
_WtWebioAn1GraphPtSwPortOutputComment_Object = MibTableColumn
wtWebioAn1GraphPtSwPortOutputComment = _WtWebioAn1GraphPtSwPortOutputComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1, 4),
    _WtWebioAn1GraphPtSwPortOutputComment_Type()
)
wtWebioAn1GraphPtSwPortOutputComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwPortOutputComment.setStatus("mandatory")


class _WtWebioAn1GraphPortOutputResetEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphPortOutputResetEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtWebioAn1GraphPortOutputResetEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphPortOutputResetEnable_Object = MibTableColumn
wtWebioAn1GraphPortOutputResetEnable = _WtWebioAn1GraphPortOutputResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 2, 3, 1, 5),
    _WtWebioAn1GraphPortOutputResetEnable_Type()
)
wtWebioAn1GraphPortOutputResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPortOutputResetEnable.setStatus("mandatory")
_WtWebioAn1GraphPtSwManufact_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwManufact = _WtWebioAn1GraphPtSwManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3)
)
_WtWebioAn1GraphPtSwMfName_Type = OctetString
_WtWebioAn1GraphPtSwMfName_Object = MibScalar
wtWebioAn1GraphPtSwMfName = _WtWebioAn1GraphPtSwMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 1),
    _WtWebioAn1GraphPtSwMfName_Type()
)
wtWebioAn1GraphPtSwMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfName.setStatus("mandatory")
_WtWebioAn1GraphPtSwMfAddr_Type = OctetString
_WtWebioAn1GraphPtSwMfAddr_Object = MibScalar
wtWebioAn1GraphPtSwMfAddr = _WtWebioAn1GraphPtSwMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 2),
    _WtWebioAn1GraphPtSwMfAddr_Type()
)
wtWebioAn1GraphPtSwMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfAddr.setStatus("mandatory")
_WtWebioAn1GraphPtSwMfHotline_Type = OctetString
_WtWebioAn1GraphPtSwMfHotline_Object = MibScalar
wtWebioAn1GraphPtSwMfHotline = _WtWebioAn1GraphPtSwMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 3),
    _WtWebioAn1GraphPtSwMfHotline_Type()
)
wtWebioAn1GraphPtSwMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfHotline.setStatus("mandatory")
_WtWebioAn1GraphPtSwMfInternet_Type = OctetString
_WtWebioAn1GraphPtSwMfInternet_Object = MibScalar
wtWebioAn1GraphPtSwMfInternet = _WtWebioAn1GraphPtSwMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 4),
    _WtWebioAn1GraphPtSwMfInternet_Type()
)
wtWebioAn1GraphPtSwMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfInternet.setStatus("mandatory")
_WtWebioAn1GraphPtSwMfDeviceTyp_Type = OctetString
_WtWebioAn1GraphPtSwMfDeviceTyp_Object = MibScalar
wtWebioAn1GraphPtSwMfDeviceTyp = _WtWebioAn1GraphPtSwMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 5),
    _WtWebioAn1GraphPtSwMfDeviceTyp_Type()
)
wtWebioAn1GraphPtSwMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfDeviceTyp.setStatus("mandatory")
_WtWebioAn1GraphPtSwMfOrderNo_Type = OctetString
_WtWebioAn1GraphPtSwMfOrderNo_Object = MibScalar
wtWebioAn1GraphPtSwMfOrderNo = _WtWebioAn1GraphPtSwMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 3, 3, 6),
    _WtWebioAn1GraphPtSwMfOrderNo_Type()
)
wtWebioAn1GraphPtSwMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwMfOrderNo.setStatus("mandatory")
_WtWebioAn1GraphPtSwDiag_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphPtSwDiag = _WtWebioAn1GraphPtSwDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4)
)
_WtWebioAn1GraphPtSwDiagErrorCount_Type = Integer32
_WtWebioAn1GraphPtSwDiagErrorCount_Object = MibScalar
wtWebioAn1GraphPtSwDiagErrorCount = _WtWebioAn1GraphPtSwDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4, 1),
    _WtWebioAn1GraphPtSwDiagErrorCount_Type()
)
wtWebioAn1GraphPtSwDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDiagErrorCount.setStatus("mandatory")
_WtWebioAn1GraphPtSwDiagBinaryError_Type = OctetString
_WtWebioAn1GraphPtSwDiagBinaryError_Object = MibScalar
wtWebioAn1GraphPtSwDiagBinaryError = _WtWebioAn1GraphPtSwDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4, 2),
    _WtWebioAn1GraphPtSwDiagBinaryError_Type()
)
wtWebioAn1GraphPtSwDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDiagBinaryError.setStatus("mandatory")
_WtWebioAn1GraphPtSwDiagErrorIndex_Type = Integer32
_WtWebioAn1GraphPtSwDiagErrorIndex_Object = MibScalar
wtWebioAn1GraphPtSwDiagErrorIndex = _WtWebioAn1GraphPtSwDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4, 3),
    _WtWebioAn1GraphPtSwDiagErrorIndex_Type()
)
wtWebioAn1GraphPtSwDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDiagErrorIndex.setStatus("mandatory")
_WtWebioAn1GraphPtSwDiagErrorMessage_Type = OctetString
_WtWebioAn1GraphPtSwDiagErrorMessage_Object = MibScalar
wtWebioAn1GraphPtSwDiagErrorMessage = _WtWebioAn1GraphPtSwDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4, 4),
    _WtWebioAn1GraphPtSwDiagErrorMessage_Type()
)
wtWebioAn1GraphPtSwDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDiagErrorMessage.setStatus("mandatory")
_WtWebioAn1GraphPtSwDiagErrorClear_Type = Integer32
_WtWebioAn1GraphPtSwDiagErrorClear_Object = MibScalar
wtWebioAn1GraphPtSwDiagErrorClear = _WtWebioAn1GraphPtSwDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 4, 5),
    _WtWebioAn1GraphPtSwDiagErrorClear_Type()
)
wtWebioAn1GraphPtSwDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebioAn1GraphPtAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 31)
)
wtWebioAn1GraphPtAlert1.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert1.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 32)
)
wtWebioAn1GraphPtAlert2.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert2.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 33)
)
wtWebioAn1GraphPtAlert3.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert3.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 34)
)
wtWebioAn1GraphPtAlert4.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert4.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 35)
)
wtWebioAn1GraphPtAlert5.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert5.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 36)
)
wtWebioAn1GraphPtAlert6.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert6.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 37)
)
wtWebioAn1GraphPtAlert7.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert7.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 38)
)
wtWebioAn1GraphPtAlert8.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert8.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 91)
)
wtWebioAn1GraphPtAlert9.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert9.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 92)
)
wtWebioAn1GraphPtAlert10.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert10.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 93)
)
wtWebioAn1GraphPtAlert11.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert11.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 94)
)
wtWebioAn1GraphPtAlert12.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert12.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 95)
)
wtWebioAn1GraphPtAlert13.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert13.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 96)
)
wtWebioAn1GraphPtAlert14.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert14.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 97)
)
wtWebioAn1GraphPtAlert15.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert15.setStatus(
        ""
    )

wtWebioAn1GraphPtAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 98)
)
wtWebioAn1GraphPtAlert16.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlert16.setStatus(
        ""
    )

wtWebioAn1GraphPtAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 17, 0, 110)
)
wtWebioAn1GraphPtAlertDiag.setObjects(
      *(("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtDiagErrorIndex"),
        ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtAlertDiag.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 31)
)
wtWebioAn1GraphPtSwAlert1.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert1.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 32)
)
wtWebioAn1GraphPtSwAlert2.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert2.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 33)
)
wtWebioAn1GraphPtSwAlert3.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert3.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 34)
)
wtWebioAn1GraphPtSwAlert4.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert4.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 35)
)
wtWebioAn1GraphPtSwAlert5.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert5.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 36)
)
wtWebioAn1GraphPtSwAlert6.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert6.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 37)
)
wtWebioAn1GraphPtSwAlert7.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert7.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 38)
)
wtWebioAn1GraphPtSwAlert8.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert8.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 91)
)
wtWebioAn1GraphPtSwAlert9.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert9.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 92)
)
wtWebioAn1GraphPtSwAlert10.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert10.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 93)
)
wtWebioAn1GraphPtSwAlert11.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert11.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 94)
)
wtWebioAn1GraphPtSwAlert12.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert12.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 95)
)
wtWebioAn1GraphPtSwAlert13.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert13.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 96)
)
wtWebioAn1GraphPtSwAlert14.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert14.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 97)
)
wtWebioAn1GraphPtSwAlert15.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert15.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 98)
)
wtWebioAn1GraphPtSwAlert16.setObjects(
    ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlert16.setStatus(
        ""
    )

wtWebioAn1GraphPtSwAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 23, 0, 110)
)
wtWebioAn1GraphPtSwAlertDiag.setObjects(
      *(("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwDiagErrorIndex"),
        ("WebGraph-Thermometer-PT-US-MIB", "wtWebioAn1GraphPtSwDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphPtSwAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermometer-PT-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebioAn1GraphPt": wtWebioAn1GraphPt,
       "wtWebioAn1GraphPtAlert1": wtWebioAn1GraphPtAlert1,
       "wtWebioAn1GraphPtAlert2": wtWebioAn1GraphPtAlert2,
       "wtWebioAn1GraphPtAlert3": wtWebioAn1GraphPtAlert3,
       "wtWebioAn1GraphPtAlert4": wtWebioAn1GraphPtAlert4,
       "wtWebioAn1GraphPtAlert5": wtWebioAn1GraphPtAlert5,
       "wtWebioAn1GraphPtAlert6": wtWebioAn1GraphPtAlert6,
       "wtWebioAn1GraphPtAlert7": wtWebioAn1GraphPtAlert7,
       "wtWebioAn1GraphPtAlert8": wtWebioAn1GraphPtAlert8,
       "wtWebioAn1GraphPtAlert9": wtWebioAn1GraphPtAlert9,
       "wtWebioAn1GraphPtAlert10": wtWebioAn1GraphPtAlert10,
       "wtWebioAn1GraphPtAlert11": wtWebioAn1GraphPtAlert11,
       "wtWebioAn1GraphPtAlert12": wtWebioAn1GraphPtAlert12,
       "wtWebioAn1GraphPtAlert13": wtWebioAn1GraphPtAlert13,
       "wtWebioAn1GraphPtAlert14": wtWebioAn1GraphPtAlert14,
       "wtWebioAn1GraphPtAlert15": wtWebioAn1GraphPtAlert15,
       "wtWebioAn1GraphPtAlert16": wtWebioAn1GraphPtAlert16,
       "wtWebioAn1GraphPtAlertDiag": wtWebioAn1GraphPtAlertDiag,
       "wtWebioAn1GraphPtTemp": wtWebioAn1GraphPtTemp,
       "wtWebioAn1GraphPtSensors": wtWebioAn1GraphPtSensors,
       "wtWebioAn1GraphPtSensorTable": wtWebioAn1GraphPtSensorTable,
       "wtWebioAn1GraphPtSensorEntry": wtWebioAn1GraphPtSensorEntry,
       "wtWebioAn1GraphPtSensorNo": wtWebioAn1GraphPtSensorNo,
       "wtWebioAn1GraphPtTempValueTable": wtWebioAn1GraphPtTempValueTable,
       "wtWebioAn1GraphPtTempValueEntry": wtWebioAn1GraphPtTempValueEntry,
       "wtWebioAn1GraphPtTempValue": wtWebioAn1GraphPtTempValue,
       "wtWebioAn1GraphPtBinaryTempValueTable": wtWebioAn1GraphPtBinaryTempValueTable,
       "wtWebioAn1GraphPtBinaryTempValueEntry": wtWebioAn1GraphPtBinaryTempValueEntry,
       "wtWebioAn1GraphPtBinaryTempValue": wtWebioAn1GraphPtBinaryTempValue,
       "wtWebioAn1GraphPtTempValuePktTable": wtWebioAn1GraphPtTempValuePktTable,
       "wtWebioAn1GraphPtTempValuePktEntry": wtWebioAn1GraphPtTempValuePktEntry,
       "wtWebioAn1GraphPtTempValuePkt": wtWebioAn1GraphPtTempValuePkt,
       "wtWebioAn1GraphPtSessCntrl": wtWebioAn1GraphPtSessCntrl,
       "wtWebioAn1GraphPtSessCntrlPassword": wtWebioAn1GraphPtSessCntrlPassword,
       "wtWebioAn1GraphPtSessCntrlConfigMode": wtWebioAn1GraphPtSessCntrlConfigMode,
       "wtWebioAn1GraphPtSessCntrlLogout": wtWebioAn1GraphPtSessCntrlLogout,
       "wtWebioAn1GraphPtSessCntrlAdminPassword": wtWebioAn1GraphPtSessCntrlAdminPassword,
       "wtWebioAn1GraphPtSessCntrlConfigPassword": wtWebioAn1GraphPtSessCntrlConfigPassword,
       "wtWebioAn1GraphPtConfig": wtWebioAn1GraphPtConfig,
       "wtWebioAn1GraphPtDevice": wtWebioAn1GraphPtDevice,
       "wtWebioAn1GraphPtText": wtWebioAn1GraphPtText,
       "wtWebioAn1GraphPtDeviceName": wtWebioAn1GraphPtDeviceName,
       "wtWebioAn1GraphPtDeviceText": wtWebioAn1GraphPtDeviceText,
       "wtWebioAn1GraphPtDeviceLocation": wtWebioAn1GraphPtDeviceLocation,
       "wtWebioAn1GraphPtDeviceContact": wtWebioAn1GraphPtDeviceContact,
       "wtWebioAn1GraphPtTimeDate": wtWebioAn1GraphPtTimeDate,
       "wtWebioAn1GraphPtTimeZone": wtWebioAn1GraphPtTimeZone,
       "wtWebioAn1GraphPtTzOffsetHrs": wtWebioAn1GraphPtTzOffsetHrs,
       "wtWebioAn1GraphPtTzOffsetMin": wtWebioAn1GraphPtTzOffsetMin,
       "wtWebioAn1GraphPtTzEnable": wtWebioAn1GraphPtTzEnable,
       "wtWebioAn1GraphPtStTzOffsetHrs": wtWebioAn1GraphPtStTzOffsetHrs,
       "wtWebioAn1GraphPtStTzOffsetMin": wtWebioAn1GraphPtStTzOffsetMin,
       "wtWebioAn1GraphPtStTzEnable": wtWebioAn1GraphPtStTzEnable,
       "wtWebioAn1GraphPtStTzStartMonth": wtWebioAn1GraphPtStTzStartMonth,
       "wtWebioAn1GraphPtStTzStartMode": wtWebioAn1GraphPtStTzStartMode,
       "wtWebioAn1GraphPtStTzStartWday": wtWebioAn1GraphPtStTzStartWday,
       "wtWebioAn1GraphPtStTzStartHrs": wtWebioAn1GraphPtStTzStartHrs,
       "wtWebioAn1GraphPtStTzStartMin": wtWebioAn1GraphPtStTzStartMin,
       "wtWebioAn1GraphPtStTzStopMonth": wtWebioAn1GraphPtStTzStopMonth,
       "wtWebioAn1GraphPtStTzStopMode": wtWebioAn1GraphPtStTzStopMode,
       "wtWebioAn1GraphPtStTzStopWday": wtWebioAn1GraphPtStTzStopWday,
       "wtWebioAn1GraphPtStTzStopHrs": wtWebioAn1GraphPtStTzStopHrs,
       "wtWebioAn1GraphPtStTzStopMin": wtWebioAn1GraphPtStTzStopMin,
       "wtWebioAn1GraphPtTimeServer": wtWebioAn1GraphPtTimeServer,
       "wtWebioAn1GraphPtTimeServer1": wtWebioAn1GraphPtTimeServer1,
       "wtWebioAn1GraphPtTimeServer2": wtWebioAn1GraphPtTimeServer2,
       "wtWebioAn1GraphPtTsEnable": wtWebioAn1GraphPtTsEnable,
       "wtWebioAn1GraphPtTsSyncTime": wtWebioAn1GraphPtTsSyncTime,
       "wtWebioAn1GraphPtDeviceClock": wtWebioAn1GraphPtDeviceClock,
       "wtWebioAn1GraphPtClockHrs": wtWebioAn1GraphPtClockHrs,
       "wtWebioAn1GraphPtClockMin": wtWebioAn1GraphPtClockMin,
       "wtWebioAn1GraphPtClockDay": wtWebioAn1GraphPtClockDay,
       "wtWebioAn1GraphPtClockMonth": wtWebioAn1GraphPtClockMonth,
       "wtWebioAn1GraphPtClockYear": wtWebioAn1GraphPtClockYear,
       "wtWebioAn1GraphPtBasic": wtWebioAn1GraphPtBasic,
       "wtWebioAn1GraphPtNetwork": wtWebioAn1GraphPtNetwork,
       "wtWebioAn1GraphPtIpAddress": wtWebioAn1GraphPtIpAddress,
       "wtWebioAn1GraphPtSubnetMask": wtWebioAn1GraphPtSubnetMask,
       "wtWebioAn1GraphPtGateway": wtWebioAn1GraphPtGateway,
       "wtWebioAn1GraphPtDnsServer1": wtWebioAn1GraphPtDnsServer1,
       "wtWebioAn1GraphPtDnsServer2": wtWebioAn1GraphPtDnsServer2,
       "wtWebioAn1GraphPtAddConfig": wtWebioAn1GraphPtAddConfig,
       "wtWebioAn1GraphPtHTTP": wtWebioAn1GraphPtHTTP,
       "wtWebioAn1GraphPtStartup": wtWebioAn1GraphPtStartup,
       "wtWebioAn1GraphPtGetHeaderEnable": wtWebioAn1GraphPtGetHeaderEnable,
       "wtWebioAn1GraphPtHttpPort": wtWebioAn1GraphPtHttpPort,
       "wtWebioAn1GraphPtMail": wtWebioAn1GraphPtMail,
       "wtWebioAn1GraphPtMailAdName": wtWebioAn1GraphPtMailAdName,
       "wtWebioAn1GraphPtMailReply": wtWebioAn1GraphPtMailReply,
       "wtWebioAn1GraphPtMailServer": wtWebioAn1GraphPtMailServer,
       "wtWebioAn1GraphPtMailEnable": wtWebioAn1GraphPtMailEnable,
       "wtWebioAn1GraphPtMailAuthentication": wtWebioAn1GraphPtMailAuthentication,
       "wtWebioAn1GraphPtMailAuthUser": wtWebioAn1GraphPtMailAuthUser,
       "wtWebioAn1GraphPtMailAuthPassword": wtWebioAn1GraphPtMailAuthPassword,
       "wtWebioAn1GraphPtMailPop3Server": wtWebioAn1GraphPtMailPop3Server,
       "wtWebioAn1GraphPtSNMP": wtWebioAn1GraphPtSNMP,
       "wtWebioAn1GraphPtSnmpCommunityStringRead": wtWebioAn1GraphPtSnmpCommunityStringRead,
       "wtWebioAn1GraphPtSnmpCommunityStringReadWrite": wtWebioAn1GraphPtSnmpCommunityStringReadWrite,
       "wtWebioAn1GraphPtSystemTrapManagerIP": wtWebioAn1GraphPtSystemTrapManagerIP,
       "wtWebioAn1GraphPtSystemTrapEnable": wtWebioAn1GraphPtSystemTrapEnable,
       "wtWebioAn1GraphPtSnmpEnable": wtWebioAn1GraphPtSnmpEnable,
       "wtWebioAn1GraphPtSnmpCommunityStringTrap": wtWebioAn1GraphPtSnmpCommunityStringTrap,
       "wtWebioAn1GraphPtUDP": wtWebioAn1GraphPtUDP,
       "wtWebioAn1GraphPtUdpPort": wtWebioAn1GraphPtUdpPort,
       "wtWebioAn1GraphPtUdpEnable": wtWebioAn1GraphPtUdpEnable,
       "wtWebioAn1GraphPtSyslog": wtWebioAn1GraphPtSyslog,
       "wtWebioAn1GraphPtSyslogServerIP": wtWebioAn1GraphPtSyslogServerIP,
       "wtWebioAn1GraphPtSyslogServerPort": wtWebioAn1GraphPtSyslogServerPort,
       "wtWebioAn1GraphPtSyslogSystemMessagesEnable": wtWebioAn1GraphPtSyslogSystemMessagesEnable,
       "wtWebioAn1GraphPtSyslogEnable": wtWebioAn1GraphPtSyslogEnable,
       "wtWebioAn1GraphPtFTP": wtWebioAn1GraphPtFTP,
       "wtWebioAn1GraphPtFTPServerIP": wtWebioAn1GraphPtFTPServerIP,
       "wtWebioAn1GraphPtFTPServerControlPort": wtWebioAn1GraphPtFTPServerControlPort,
       "wtWebioAn1GraphPtFTPUserName": wtWebioAn1GraphPtFTPUserName,
       "wtWebioAn1GraphPtFTPPassword": wtWebioAn1GraphPtFTPPassword,
       "wtWebioAn1GraphPtFTPAccount": wtWebioAn1GraphPtFTPAccount,
       "wtWebioAn1GraphPtFTPOption": wtWebioAn1GraphPtFTPOption,
       "wtWebioAn1GraphPtFTPEnable": wtWebioAn1GraphPtFTPEnable,
       "wtWebioAn1GraphPtLanguage": wtWebioAn1GraphPtLanguage,
       "wtWebioAn1GraphPtLanguageSelect": wtWebioAn1GraphPtLanguageSelect,
       "wtWebioAn1GraphPtDatalogger": wtWebioAn1GraphPtDatalogger,
       "wtWebioAn1GraphPtLoggerTimebase": wtWebioAn1GraphPtLoggerTimebase,
       "wtWebioAn1GraphPtLoggerSensorSel": wtWebioAn1GraphPtLoggerSensorSel,
       "wtWebioAn1GraphPtDisplaySensorSel": wtWebioAn1GraphPtDisplaySensorSel,
       "wtWebioAn1GraphPtSensorColorTable": wtWebioAn1GraphPtSensorColorTable,
       "wtWebioAn1GraphPtSensorColorEntry": wtWebioAn1GraphPtSensorColorEntry,
       "wtWebioAn1GraphPtSensorColor": wtWebioAn1GraphPtSensorColor,
       "wtWebioAn1GraphPtAutoScaleEnable": wtWebioAn1GraphPtAutoScaleEnable,
       "wtWebioAn1GraphPtVerticalUpperLimit": wtWebioAn1GraphPtVerticalUpperLimit,
       "wtWebioAn1GraphPtVerticalLowerLimit": wtWebioAn1GraphPtVerticalLowerLimit,
       "wtWebioAn1GraphPtHorizontalZoom": wtWebioAn1GraphPtHorizontalZoom,
       "wtWebioAn1GraphPtAlarm": wtWebioAn1GraphPtAlarm,
       "wtWebioAn1GraphPtAlarmCount": wtWebioAn1GraphPtAlarmCount,
       "wtWebioAn1GraphPtAlarmIfTable": wtWebioAn1GraphPtAlarmIfTable,
       "wtWebioAn1GraphPtAlarmIfEntry": wtWebioAn1GraphPtAlarmIfEntry,
       "wtWebioAn1GraphPtAlarmNo": wtWebioAn1GraphPtAlarmNo,
       "wtWebioAn1GraphPtAlarmTable": wtWebioAn1GraphPtAlarmTable,
       "wtWebioAn1GraphPtAlarmEntry": wtWebioAn1GraphPtAlarmEntry,
       "wtWebioAn1GraphPtAlarmTrigger": wtWebioAn1GraphPtAlarmTrigger,
       "wtWebioAn1GraphPtAlarmMin": wtWebioAn1GraphPtAlarmMin,
       "wtWebioAn1GraphPtAlarmMax": wtWebioAn1GraphPtAlarmMax,
       "wtWebioAn1GraphPtAlarmHysteresis": wtWebioAn1GraphPtAlarmHysteresis,
       "wtWebioAn1GraphPtAlarmDelay": wtWebioAn1GraphPtAlarmDelay,
       "wtWebioAn1GraphPtAlarmInterval": wtWebioAn1GraphPtAlarmInterval,
       "wtWebioAn1GraphPtAlarmEnable": wtWebioAn1GraphPtAlarmEnable,
       "wtWebioAn1GraphPtAlarmEMailAddr": wtWebioAn1GraphPtAlarmEMailAddr,
       "wtWebioAn1GraphPtAlarmMailSubject": wtWebioAn1GraphPtAlarmMailSubject,
       "wtWebioAn1GraphPtAlarmMailText": wtWebioAn1GraphPtAlarmMailText,
       "wtWebioAn1GraphPtAlarmManagerIP": wtWebioAn1GraphPtAlarmManagerIP,
       "wtWebioAn1GraphPtAlarmTrapText": wtWebioAn1GraphPtAlarmTrapText,
       "wtWebioAn1GraphPtAlarmMailOptions": wtWebioAn1GraphPtAlarmMailOptions,
       "wtWebioAn1GraphPtAlarmTcpIpAddr": wtWebioAn1GraphPtAlarmTcpIpAddr,
       "wtWebioAn1GraphPtAlarmTcpPort": wtWebioAn1GraphPtAlarmTcpPort,
       "wtWebioAn1GraphPtAlarmTcpText": wtWebioAn1GraphPtAlarmTcpText,
       "wtWebioAn1GraphPtAlarmClearMailSubject": wtWebioAn1GraphPtAlarmClearMailSubject,
       "wtWebioAn1GraphPtAlarmClearMailText": wtWebioAn1GraphPtAlarmClearMailText,
       "wtWebioAn1GraphPtAlarmClearTrapText": wtWebioAn1GraphPtAlarmClearTrapText,
       "wtWebioAn1GraphPtAlarmClearTcpText": wtWebioAn1GraphPtAlarmClearTcpText,
       "wtWebioAn1GraphPtAlarmSyslogIpAddr": wtWebioAn1GraphPtAlarmSyslogIpAddr,
       "wtWebioAn1GraphPtAlarmSyslogPort": wtWebioAn1GraphPtAlarmSyslogPort,
       "wtWebioAn1GraphPtAlarmSyslogText": wtWebioAn1GraphPtAlarmSyslogText,
       "wtWebioAn1GraphPtAlarmSyslogClearText": wtWebioAn1GraphPtAlarmSyslogClearText,
       "wtWebioAn1GraphPtAlarmFtpDataPort": wtWebioAn1GraphPtAlarmFtpDataPort,
       "wtWebioAn1GraphPtAlarmFtpFileName": wtWebioAn1GraphPtAlarmFtpFileName,
       "wtWebioAn1GraphPtAlarmFtpText": wtWebioAn1GraphPtAlarmFtpText,
       "wtWebioAn1GraphPtAlarmFtpClearText": wtWebioAn1GraphPtAlarmFtpClearText,
       "wtWebioAn1GraphPtAlarmFtpOption": wtWebioAn1GraphPtAlarmFtpOption,
       "wtWebioAn1GraphPtAlarmTimerCron": wtWebioAn1GraphPtAlarmTimerCron,
       "wtWebioAn1GraphPtAlarmDeltaTemp": wtWebioAn1GraphPtAlarmDeltaTemp,
       "wtWebioAn1GraphPtAlarmName": wtWebioAn1GraphPtAlarmName,
       "wtWebioAn1GraphPtAlarmActive": wtWebioAn1GraphPtAlarmActive,
       "wtWebioAn1GraphPtGraphics": wtWebioAn1GraphPtGraphics,
       "wtWebioAn1GraphPtGraphicsBase": wtWebioAn1GraphPtGraphicsBase,
       "wtWebioAn1GraphPtGraphicsBaseEnable": wtWebioAn1GraphPtGraphicsBaseEnable,
       "wtWebioAn1GraphPtGraphicsBaseWidth": wtWebioAn1GraphPtGraphicsBaseWidth,
       "wtWebioAn1GraphPtGraphicsBaseHeight": wtWebioAn1GraphPtGraphicsBaseHeight,
       "wtWebioAn1GraphPtGraphicsBaseFrameColor": wtWebioAn1GraphPtGraphicsBaseFrameColor,
       "wtWebioAn1GraphPtGraphicsBaseBackgroundColor": wtWebioAn1GraphPtGraphicsBaseBackgroundColor,
       "wtWebioAn1GraphPtGraphicsBasePollingrate": wtWebioAn1GraphPtGraphicsBasePollingrate,
       "wtWebioAn1GraphPtGraphicsSelect": wtWebioAn1GraphPtGraphicsSelect,
       "wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel": wtWebioAn1GraphPtGraphicsSelectDisplaySensorSel,
       "wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem": wtWebioAn1GraphPtGraphicsSelectDisplayShowExtrem,
       "wtWebioAn1GraphPt2SensorColorTable": wtWebioAn1GraphPt2SensorColorTable,
       "wtWebioAn1GraphPt2SensorColorEntry": wtWebioAn1GraphPt2SensorColorEntry,
       "wtWebioAn1GraphPt2GraphicsSensorColor": wtWebioAn1GraphPt2GraphicsSensorColor,
       "wtWebioAn1GraphPt2GraphicsSelectScale": wtWebioAn1GraphPt2GraphicsSelectScale,
       "wtWebioAn1GraphPtGraphicsScale": wtWebioAn1GraphPtGraphicsScale,
       "wtWebioAn1GraphPtGraphicsScaleAutoScaleEnable": wtWebioAn1GraphPtGraphicsScaleAutoScaleEnable,
       "wtWebioAn1GraphPtGraphicsScaleAutoFitEnable": wtWebioAn1GraphPtGraphicsScaleAutoFitEnable,
       "wtWebioAn1GraphPtGraphicsScale1Min": wtWebioAn1GraphPtGraphicsScale1Min,
       "wtWebioAn1GraphPtGraphicsScale2Min": wtWebioAn1GraphPtGraphicsScale2Min,
       "wtWebioAn1GraphPtGraphicsScale3Min": wtWebioAn1GraphPtGraphicsScale3Min,
       "wtWebioAn1GraphPtGraphicsScale4Min": wtWebioAn1GraphPtGraphicsScale4Min,
       "wtWebioAn1GraphPtGraphicsScale1Max": wtWebioAn1GraphPtGraphicsScale1Max,
       "wtWebioAn1GraphPtGraphicsScale2Max": wtWebioAn1GraphPtGraphicsScale2Max,
       "wtWebioAn1GraphPtGraphicsScale3Max": wtWebioAn1GraphPtGraphicsScale3Max,
       "wtWebioAn1GraphPtGraphicsScale4Max": wtWebioAn1GraphPtGraphicsScale4Max,
       "wtWebioAn1GraphPtGraphicsScale1Unit": wtWebioAn1GraphPtGraphicsScale1Unit,
       "wtWebioAn1GraphPtGraphicsScale2Unit": wtWebioAn1GraphPtGraphicsScale2Unit,
       "wtWebioAn1GraphPtGraphicsScale3Unit": wtWebioAn1GraphPtGraphicsScale3Unit,
       "wtWebioAn1GraphPtGraphicsScale4Unit": wtWebioAn1GraphPtGraphicsScale4Unit,
       "wtWebioAn1GraphPtPorts": wtWebioAn1GraphPtPorts,
       "wtWebioAn1GraphPtPortTable": wtWebioAn1GraphPtPortTable,
       "wtWebioAn1GraphPtPortEntry": wtWebioAn1GraphPtPortEntry,
       "wtWebioAn1GraphPtPortName": wtWebioAn1GraphPtPortName,
       "wtWebioAn1GraphPtPortText": wtWebioAn1GraphPtPortText,
       "wtWebioAn1GraphPtPortOffset1": wtWebioAn1GraphPtPortOffset1,
       "wtWebioAn1GraphPtPortTemperature1": wtWebioAn1GraphPtPortTemperature1,
       "wtWebioAn1GraphPtPortOffset2": wtWebioAn1GraphPtPortOffset2,
       "wtWebioAn1GraphPtPortTemperature2": wtWebioAn1GraphPtPortTemperature2,
       "wtWebioAn1GraphPtPortComment": wtWebioAn1GraphPtPortComment,
       "wtWebioAn1GraphPtPortSensorSelect": wtWebioAn1GraphPtPortSensorSelect,
       "wtWebioAn1GraphPtManufact": wtWebioAn1GraphPtManufact,
       "wtWebioAn1GraphPtMfName": wtWebioAn1GraphPtMfName,
       "wtWebioAn1GraphPtMfAddr": wtWebioAn1GraphPtMfAddr,
       "wtWebioAn1GraphPtMfHotline": wtWebioAn1GraphPtMfHotline,
       "wtWebioAn1GraphPtMfInternet": wtWebioAn1GraphPtMfInternet,
       "wtWebioAn1GraphPtMfDeviceTyp": wtWebioAn1GraphPtMfDeviceTyp,
       "wtWebioAn1GraphPtMfOrderNo": wtWebioAn1GraphPtMfOrderNo,
       "wtWebioAn1GraphPtDiag": wtWebioAn1GraphPtDiag,
       "wtWebioAn1GraphPtDiagErrorCount": wtWebioAn1GraphPtDiagErrorCount,
       "wtWebioAn1GraphPtDiagBinaryError": wtWebioAn1GraphPtDiagBinaryError,
       "wtWebioAn1GraphPtDiagErrorIndex": wtWebioAn1GraphPtDiagErrorIndex,
       "wtWebioAn1GraphPtDiagErrorMessage": wtWebioAn1GraphPtDiagErrorMessage,
       "wtWebioAn1GraphPtDiagErrorClear": wtWebioAn1GraphPtDiagErrorClear,
       "wtWebioAn1GraphPtSw": wtWebioAn1GraphPtSw,
       "wtWebioAn1GraphPtSwAlert1": wtWebioAn1GraphPtSwAlert1,
       "wtWebioAn1GraphPtSwAlert2": wtWebioAn1GraphPtSwAlert2,
       "wtWebioAn1GraphPtSwAlert3": wtWebioAn1GraphPtSwAlert3,
       "wtWebioAn1GraphPtSwAlert4": wtWebioAn1GraphPtSwAlert4,
       "wtWebioAn1GraphPtSwAlert5": wtWebioAn1GraphPtSwAlert5,
       "wtWebioAn1GraphPtSwAlert6": wtWebioAn1GraphPtSwAlert6,
       "wtWebioAn1GraphPtSwAlert7": wtWebioAn1GraphPtSwAlert7,
       "wtWebioAn1GraphPtSwAlert8": wtWebioAn1GraphPtSwAlert8,
       "wtWebioAn1GraphPtSwAlert9": wtWebioAn1GraphPtSwAlert9,
       "wtWebioAn1GraphPtSwAlert10": wtWebioAn1GraphPtSwAlert10,
       "wtWebioAn1GraphPtSwAlert11": wtWebioAn1GraphPtSwAlert11,
       "wtWebioAn1GraphPtSwAlert12": wtWebioAn1GraphPtSwAlert12,
       "wtWebioAn1GraphPtSwAlert13": wtWebioAn1GraphPtSwAlert13,
       "wtWebioAn1GraphPtSwAlert14": wtWebioAn1GraphPtSwAlert14,
       "wtWebioAn1GraphPtSwAlert15": wtWebioAn1GraphPtSwAlert15,
       "wtWebioAn1GraphPtSwAlert16": wtWebioAn1GraphPtSwAlert16,
       "wtWebioAn1GraphPtSwAlertDiag": wtWebioAn1GraphPtSwAlertDiag,
       "wtWebioAn1GraphPtSwTemp": wtWebioAn1GraphPtSwTemp,
       "wtWebioAn1GraphPtSwSensors": wtWebioAn1GraphPtSwSensors,
       "wtWebioAn1GraphPtSwSensorTable": wtWebioAn1GraphPtSwSensorTable,
       "wtWebioAn1GraphPtSwSensorEntry": wtWebioAn1GraphPtSwSensorEntry,
       "wtWebioAn1GraphPtSwSensorNo": wtWebioAn1GraphPtSwSensorNo,
       "wtWebioAn1GraphPtSwTempValueTable": wtWebioAn1GraphPtSwTempValueTable,
       "wtWebioAn1GraphPtSwTempValueEntry": wtWebioAn1GraphPtSwTempValueEntry,
       "wtWebioAn1GraphPtSwTempValue": wtWebioAn1GraphPtSwTempValue,
       "wtWebioAn1GraphPtSwBinaryTempValueTable": wtWebioAn1GraphPtSwBinaryTempValueTable,
       "wtWebioAn1GraphPtSwBinaryTempValueEntry": wtWebioAn1GraphPtSwBinaryTempValueEntry,
       "wtWebioAn1GraphPtSwBinaryTempValue": wtWebioAn1GraphPtSwBinaryTempValue,
       "wtWebioAn1GraphPtSwOutputs": wtWebioAn1GraphPtSwOutputs,
       "wtWebioAn1GraphPtSwOutputTable": wtWebioAn1GraphPtSwOutputTable,
       "wtWebioAn1GraphPtSwOutputEntry": wtWebioAn1GraphPtSwOutputEntry,
       "wtWebioAn1GraphPtSwOutputNo": wtWebioAn1GraphPtSwOutputNo,
       "wtWebioAn1GraphPtSwBinaryOutputValueTable": wtWebioAn1GraphPtSwBinaryOutputValueTable,
       "wtWebioAn1GraphPtSwBinaryOutputValueEntry": wtWebioAn1GraphPtSwBinaryOutputValueEntry,
       "wtWebioAn1GraphPtSwBinaryOutputValue": wtWebioAn1GraphPtSwBinaryOutputValue,
       "wtWebioAn1GraphPtSwTempValuePktTable": wtWebioAn1GraphPtSwTempValuePktTable,
       "wtWebioAn1GraphPtSwTempValuePktEntry": wtWebioAn1GraphPtSwTempValuePktEntry,
       "wtWebioAn1GraphPtSwTempValuePkt": wtWebioAn1GraphPtSwTempValuePkt,
       "wtWebioAn1GraphPtSwSessCntrl": wtWebioAn1GraphPtSwSessCntrl,
       "wtWebioAn1GraphPtSwSessCntrlPassword": wtWebioAn1GraphPtSwSessCntrlPassword,
       "wtWebioAn1GraphPtSwSessCntrlConfigMode": wtWebioAn1GraphPtSwSessCntrlConfigMode,
       "wtWebioAn1GraphPtSwSessCntrlLogout": wtWebioAn1GraphPtSwSessCntrlLogout,
       "wtWebioAn1GraphPtSwSessCntrlAdminPassword": wtWebioAn1GraphPtSwSessCntrlAdminPassword,
       "wtWebioAn1GraphPtSwSessCntrlConfigPassword": wtWebioAn1GraphPtSwSessCntrlConfigPassword,
       "wtWebioAn1GraphPtSwConfig": wtWebioAn1GraphPtSwConfig,
       "wtWebioAn1GraphPtSwDevice": wtWebioAn1GraphPtSwDevice,
       "wtWebioAn1GraphPtSwText": wtWebioAn1GraphPtSwText,
       "wtWebioAn1GraphPtSwDeviceName": wtWebioAn1GraphPtSwDeviceName,
       "wtWebioAn1GraphPtSwDeviceText": wtWebioAn1GraphPtSwDeviceText,
       "wtWebioAn1GraphPtSwDeviceLocation": wtWebioAn1GraphPtSwDeviceLocation,
       "wtWebioAn1GraphPtSwDeviceContact": wtWebioAn1GraphPtSwDeviceContact,
       "wtWebioAn1GraphPtSwTimeDate": wtWebioAn1GraphPtSwTimeDate,
       "wtWebioAn1GraphPtSwTimeZone": wtWebioAn1GraphPtSwTimeZone,
       "wtWebioAn1GraphPtSwTzOffsetHrs": wtWebioAn1GraphPtSwTzOffsetHrs,
       "wtWebioAn1GraphPtSwTzOffsetMin": wtWebioAn1GraphPtSwTzOffsetMin,
       "wtWebioAn1GraphPtSwTzEnable": wtWebioAn1GraphPtSwTzEnable,
       "wtWebioAn1GraphPtSwStTzOffsetHrs": wtWebioAn1GraphPtSwStTzOffsetHrs,
       "wtWebioAn1GraphPtSwStTzOffsetMin": wtWebioAn1GraphPtSwStTzOffsetMin,
       "wtWebioAn1GraphPtSwStTzEnable": wtWebioAn1GraphPtSwStTzEnable,
       "wtWebioAn1GraphPtSwStTzStartMonth": wtWebioAn1GraphPtSwStTzStartMonth,
       "wtWebioAn1GraphPtSwStTzStartMode": wtWebioAn1GraphPtSwStTzStartMode,
       "wtWebioAn1GraphPtSwStTzStartWday": wtWebioAn1GraphPtSwStTzStartWday,
       "wtWebioAn1GraphPtSwStTzStartHrs": wtWebioAn1GraphPtSwStTzStartHrs,
       "wtWebioAn1GraphPtSwStTzStartMin": wtWebioAn1GraphPtSwStTzStartMin,
       "wtWebioAn1GraphPtSwStTzStopMonth": wtWebioAn1GraphPtSwStTzStopMonth,
       "wtWebioAn1GraphPtSwStTzStopMode": wtWebioAn1GraphPtSwStTzStopMode,
       "wtWebioAn1GraphPtSwStTzStopWday": wtWebioAn1GraphPtSwStTzStopWday,
       "wtWebioAn1GraphPtSwStTzStopHrs": wtWebioAn1GraphPtSwStTzStopHrs,
       "wtWebioAn1GraphPtSwStTzStopMin": wtWebioAn1GraphPtSwStTzStopMin,
       "wtWebioAn1GraphPtSwTimeServer": wtWebioAn1GraphPtSwTimeServer,
       "wtWebioAn1GraphPtSwTimeServer1": wtWebioAn1GraphPtSwTimeServer1,
       "wtWebioAn1GraphPtSwTimeServer2": wtWebioAn1GraphPtSwTimeServer2,
       "wtWebioAn1GraphPtSwTsEnable": wtWebioAn1GraphPtSwTsEnable,
       "wtWebioAn1GraphPtSwTsSyncTime": wtWebioAn1GraphPtSwTsSyncTime,
       "wtWebioAn1GraphPtSwDeviceClock": wtWebioAn1GraphPtSwDeviceClock,
       "wtWebioAn1GraphPtSwClockHrs": wtWebioAn1GraphPtSwClockHrs,
       "wtWebioAn1GraphPtSwClockMin": wtWebioAn1GraphPtSwClockMin,
       "wtWebioAn1GraphPtSwClockDay": wtWebioAn1GraphPtSwClockDay,
       "wtWebioAn1GraphPtSwClockMonth": wtWebioAn1GraphPtSwClockMonth,
       "wtWebioAn1GraphPtSwClockYear": wtWebioAn1GraphPtSwClockYear,
       "wtWebioAn1GraphPtSwBasic": wtWebioAn1GraphPtSwBasic,
       "wtWebioAn1GraphPtSwNetwork": wtWebioAn1GraphPtSwNetwork,
       "wtWebioAn1GraphPtSwIpAddress": wtWebioAn1GraphPtSwIpAddress,
       "wtWebioAn1GraphPtSwSubnetMask": wtWebioAn1GraphPtSwSubnetMask,
       "wtWebioAn1GraphPtSwGateway": wtWebioAn1GraphPtSwGateway,
       "wtWebioAn1GraphPtSwDnsServer1": wtWebioAn1GraphPtSwDnsServer1,
       "wtWebioAn1GraphPtSwDnsServer2": wtWebioAn1GraphPtSwDnsServer2,
       "wtWebioAn1GraphPtSwAddConfig": wtWebioAn1GraphPtSwAddConfig,
       "wtWebioAn1GraphPtSwHTTP": wtWebioAn1GraphPtSwHTTP,
       "wtWebioAn1GraphPtSwStartup": wtWebioAn1GraphPtSwStartup,
       "wtWebioAn1GraphPtSwGetHeaderEnable": wtWebioAn1GraphPtSwGetHeaderEnable,
       "wtWebioAn1GraphPtSwHttpPort": wtWebioAn1GraphPtSwHttpPort,
       "wtWebioAn1GraphPtSwMail": wtWebioAn1GraphPtSwMail,
       "wtWebioAn1GraphPtSwMailAdName": wtWebioAn1GraphPtSwMailAdName,
       "wtWebioAn1GraphPtSwMailReply": wtWebioAn1GraphPtSwMailReply,
       "wtWebioAn1GraphPtSwMailServer": wtWebioAn1GraphPtSwMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebioAn1GraphPtSwMailAuthentication": wtWebioAn1GraphPtSwMailAuthentication,
       "wtWebioAn1GraphPtSwMailAuthUser": wtWebioAn1GraphPtSwMailAuthUser,
       "wtWebioAn1GraphPtSwMailAuthPassword": wtWebioAn1GraphPtSwMailAuthPassword,
       "wtWebioAn1GraphPtSwMailPop3Server": wtWebioAn1GraphPtSwMailPop3Server,
       "wtWebioAn1GraphPtSwSNMP": wtWebioAn1GraphPtSwSNMP,
       "wtWebioAn1GraphPtSwSnmpCommunityStringRead": wtWebioAn1GraphPtSwSnmpCommunityStringRead,
       "wtWebioAn1GraphPtSwSnmpCommunityStringReadWrite": wtWebioAn1GraphPtSwSnmpCommunityStringReadWrite,
       "wtWebioAn1GraphPtSwSystemTrapManagerIP": wtWebioAn1GraphPtSwSystemTrapManagerIP,
       "wtWebioAn1GraphPtSwSystemTrapEnable": wtWebioAn1GraphPtSwSystemTrapEnable,
       "wtWebioAn1GraphPtSwSnmpEnable": wtWebioAn1GraphPtSwSnmpEnable,
       "wtWebioAn1GraphPtSwSnmpCommunityStringTrap": wtWebioAn1GraphPtSwSnmpCommunityStringTrap,
       "wtWebioAn1GraphPtSwUDP": wtWebioAn1GraphPtSwUDP,
       "wtWebioAn1GraphPtSwUdpPort": wtWebioAn1GraphPtSwUdpPort,
       "wtWebioAn1GraphPtSwUdpEnable": wtWebioAn1GraphPtSwUdpEnable,
       "wtWebioAn1GraphPtSwSyslog": wtWebioAn1GraphPtSwSyslog,
       "wtWebioAn1GraphPtSwSyslogServerIP": wtWebioAn1GraphPtSwSyslogServerIP,
       "wtWebioAn1GraphPtSwSyslogServerPort": wtWebioAn1GraphPtSwSyslogServerPort,
       "wtWebioAn1GraphPtSwSyslogSystemMessagesEnable": wtWebioAn1GraphPtSwSyslogSystemMessagesEnable,
       "wtWebioAn1GraphPtSwSyslogEnable": wtWebioAn1GraphPtSwSyslogEnable,
       "wtWebioAn1GraphPtSwFTP": wtWebioAn1GraphPtSwFTP,
       "wtWebioAn1GraphPtSwFTPServerIP": wtWebioAn1GraphPtSwFTPServerIP,
       "wtWebioAn1GraphPtSwFTPServerControlPort": wtWebioAn1GraphPtSwFTPServerControlPort,
       "wtWebioAn1GraphPtSwFTPUserName": wtWebioAn1GraphPtSwFTPUserName,
       "wtWebioAn1GraphPtSwFTPPassword": wtWebioAn1GraphPtSwFTPPassword,
       "wtWebioAn1GraphPtSwFTPAccount": wtWebioAn1GraphPtSwFTPAccount,
       "wtWebioAn1GraphPtSwFTPOption": wtWebioAn1GraphPtSwFTPOption,
       "wtWebioAn1GraphPtSwFTPEnable": wtWebioAn1GraphPtSwFTPEnable,
       "wtWebioAn1GraphPtSwLanguage": wtWebioAn1GraphPtSwLanguage,
       "wtWebioAn1GraphPtSwLanguageSelect": wtWebioAn1GraphPtSwLanguageSelect,
       "wtWebioAn1GraphPtSwDatalogger": wtWebioAn1GraphPtSwDatalogger,
       "wtWebioAn1GraphPtSwLoggerTimebase": wtWebioAn1GraphPtSwLoggerTimebase,
       "wtWebioAn1GraphPtSwLoggerSensorSel": wtWebioAn1GraphPtSwLoggerSensorSel,
       "wtWebioAn1GraphPtSwDisplaySensorSel": wtWebioAn1GraphPtSwDisplaySensorSel,
       "wtWebioAn1GraphPtSwSensorColorTable": wtWebioAn1GraphPtSwSensorColorTable,
       "wtWebioAn1GraphPtSwSensorColorEntry": wtWebioAn1GraphPtSwSensorColorEntry,
       "wtWebioAn1GraphPtSwSensorColor": wtWebioAn1GraphPtSwSensorColor,
       "wtWebioAn1GraphPtSwAutoScaleEnable": wtWebioAn1GraphPtSwAutoScaleEnable,
       "wtWebioAn1GraphPtSwVerticalUpperLimit": wtWebioAn1GraphPtSwVerticalUpperLimit,
       "wtWebioAn1GraphPtSwVerticalLowerLimit": wtWebioAn1GraphPtSwVerticalLowerLimit,
       "wtWebioAn1GraphPtSwHorizontalZoom": wtWebioAn1GraphPtSwHorizontalZoom,
       "wtWebioAn1GraphPtSwAlarm": wtWebioAn1GraphPtSwAlarm,
       "wtWebioAn1GraphPtSwAlarmCount": wtWebioAn1GraphPtSwAlarmCount,
       "wtWebioAn1GraphPtSwAlarmIfTable": wtWebioAn1GraphPtSwAlarmIfTable,
       "wtWebioAn1GraphPtSwAlarmIfEntry": wtWebioAn1GraphPtSwAlarmIfEntry,
       "wtWebioAn1GraphPtSwAlarmNo": wtWebioAn1GraphPtSwAlarmNo,
       "wtWebioAn1GraphPtSwAlarmTable": wtWebioAn1GraphPtSwAlarmTable,
       "wtWebioAn1GraphPtSwAlarmEntry": wtWebioAn1GraphPtSwAlarmEntry,
       "wtWebioAn1GraphPtSwAlarmTrigger": wtWebioAn1GraphPtSwAlarmTrigger,
       "wtWebioAn1GraphPtSwAlarmMin": wtWebioAn1GraphPtSwAlarmMin,
       "wtWebioAn1GraphPtSwAlarmMax": wtWebioAn1GraphPtSwAlarmMax,
       "wtWebioAn1GraphPtSwAlarmHysteresis": wtWebioAn1GraphPtSwAlarmHysteresis,
       "wtWebioAn1GraphPtSwAlarmDelay": wtWebioAn1GraphPtSwAlarmDelay,
       "wtWebioAn1GraphPtSwAlarmInterval": wtWebioAn1GraphPtSwAlarmInterval,
       "wtWebioAn1GraphPtSwAlarmEnable": wtWebioAn1GraphPtSwAlarmEnable,
       "wtWebioAn1GraphPtSwAlarmEMailAddr": wtWebioAn1GraphPtSwAlarmEMailAddr,
       "wtWebioAn1GraphPtSwAlarmMailSubject": wtWebioAn1GraphPtSwAlarmMailSubject,
       "wtWebioAn1GraphPtSwAlarmMailText": wtWebioAn1GraphPtSwAlarmMailText,
       "wtWebioAn1GraphPtSwAlarmManagerIP": wtWebioAn1GraphPtSwAlarmManagerIP,
       "wtWebioAn1GraphPtSwAlarmTrapText": wtWebioAn1GraphPtSwAlarmTrapText,
       "wtWebioAn1GraphPtSwAlarmMailOptions": wtWebioAn1GraphPtSwAlarmMailOptions,
       "wtWebioAn1GraphPtSwAlarmTcpIpAddr": wtWebioAn1GraphPtSwAlarmTcpIpAddr,
       "wtWebioAn1GraphPtSwAlarmTcpPort": wtWebioAn1GraphPtSwAlarmTcpPort,
       "wtWebioAn1GraphPtSwAlarmTcpText": wtWebioAn1GraphPtSwAlarmTcpText,
       "wtWebioAn1GraphPtSwAlarmClearMailSubject": wtWebioAn1GraphPtSwAlarmClearMailSubject,
       "wtWebioAn1GraphPtSwAlarmClearMailText": wtWebioAn1GraphPtSwAlarmClearMailText,
       "wtWebioAn1GraphPtSwAlarmClearTrapText": wtWebioAn1GraphPtSwAlarmClearTrapText,
       "wtWebioAn1GraphPtSwAlarmClearTcpText": wtWebioAn1GraphPtSwAlarmClearTcpText,
       "wtWebioAn1GraphPtSwAlarmSyslogIpAddr": wtWebioAn1GraphPtSwAlarmSyslogIpAddr,
       "wtWebioAn1GraphPtSwAlarmSyslogPort": wtWebioAn1GraphPtSwAlarmSyslogPort,
       "wtWebioAn1GraphPtSwAlarmSyslogText": wtWebioAn1GraphPtSwAlarmSyslogText,
       "wtWebioAn1GraphPtSwAlarmSyslogClearText": wtWebioAn1GraphPtSwAlarmSyslogClearText,
       "wtWebioAn1GraphPtSwAlarmFtpDataPort": wtWebioAn1GraphPtSwAlarmFtpDataPort,
       "wtWebioAn1GraphPtSwAlarmFtpFileName": wtWebioAn1GraphPtSwAlarmFtpFileName,
       "wtWebioAn1GraphPtSwAlarmFtpText": wtWebioAn1GraphPtSwAlarmFtpText,
       "wtWebioAn1GraphPtSwAlarmFtpClearText": wtWebioAn1GraphPtSwAlarmFtpClearText,
       "wtWebioAn1GraphPtSwAlarmFtpOptions": wtWebioAn1GraphPtSwAlarmFtpOptions,
       "wtWebioAn1GraphPtSwAlarmTimerCron": wtWebioAn1GraphPtSwAlarmTimerCron,
       "wtWebioAn1GraphPtSwAlarmDeltaTemp": wtWebioAn1GraphPtSwAlarmDeltaTemp,
       "wtWebioAn1GraphPtSwAlarmName": wtWebioAn1GraphPtSwAlarmName,
       "wtWebioAn1GraphPtSwAlarmActive": wtWebioAn1GraphPtSwAlarmActive,
       "wtWebioAn1GraphPtSwGraphics": wtWebioAn1GraphPtSwGraphics,
       "wtWebioAn1GraphPtSwGraphicsBase": wtWebioAn1GraphPtSwGraphicsBase,
       "wtWebioAn1GraphPtSwGraphicsBaseEnable": wtWebioAn1GraphPtSwGraphicsBaseEnable,
       "wtWebioAn1GraphPtSwGraphicsBaseWidth": wtWebioAn1GraphPtSwGraphicsBaseWidth,
       "wtWebioAn1GraphPtSwGraphicsBaseHeight": wtWebioAn1GraphPtSwGraphicsBaseHeight,
       "wtWebioAn1GraphPtSwGraphicsBaseFrameColor": wtWebioAn1GraphPtSwGraphicsBaseFrameColor,
       "wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor": wtWebioAn1GraphPtSwGraphicsBaseBackgroundColor,
       "wtWebioAn1GraphPtSwGraphicsBasePollingrate": wtWebioAn1GraphPtSwGraphicsBasePollingrate,
       "wtWebioAn1GraphPtSwGraphicsSelect": wtWebioAn1GraphPtSwGraphicsSelect,
       "wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel": wtWebioAn1GraphPtSwGraphicsSelectDisplaySensorSel,
       "wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem": wtWebioAn1GraphPtSwGraphicsSelectDisplayShowExtrem,
       "wtWebioAn1GraphPtSw2SensorColorTable": wtWebioAn1GraphPtSw2SensorColorTable,
       "wtWebioAn1GraphPtSw2SensorColorEntry": wtWebioAn1GraphPtSw2SensorColorEntry,
       "wtWebioAn1GraphPtSw2GraphicsSensorColor": wtWebioAn1GraphPtSw2GraphicsSensorColor,
       "wtWebioAn1GraphPtSw2GraphicsSelectScale": wtWebioAn1GraphPtSw2GraphicsSelectScale,
       "wtWebioAn1GraphPtSwGraphicsScale": wtWebioAn1GraphPtSwGraphicsScale,
       "wtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable": wtWebioAn1GraphPtSwGraphicsScaleAutoScaleEnable,
       "wtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable": wtWebioAn1GraphPtSwGraphicsScaleAutoFitEnable,
       "wtWebioAn1GraphPtSwGraphicsScale1Min": wtWebioAn1GraphPtSwGraphicsScale1Min,
       "wtWebioAn1GraphPtSwGraphicsScale2Min": wtWebioAn1GraphPtSwGraphicsScale2Min,
       "wtWebioAn1GraphPtSwGraphicsScale3Min": wtWebioAn1GraphPtSwGraphicsScale3Min,
       "wtWebioAn1GraphPtSwGraphicsScale4Min": wtWebioAn1GraphPtSwGraphicsScale4Min,
       "wtWebioAn1GraphPtSwGraphicsScale1Max": wtWebioAn1GraphPtSwGraphicsScale1Max,
       "wtWebioAn1GraphPtSwGraphicsScale2Max": wtWebioAn1GraphPtSwGraphicsScale2Max,
       "wtWebioAn1GraphPtSwGraphicsScale3Max": wtWebioAn1GraphPtSwGraphicsScale3Max,
       "wtWebioAn1GraphPtSwGraphicsScale4Max": wtWebioAn1GraphPtSwGraphicsScale4Max,
       "wtWebioAn1GraphPtSwGraphicsScale1Unit": wtWebioAn1GraphPtSwGraphicsScale1Unit,
       "wtWebioAn1GraphPtSwGraphicsScale2Unit": wtWebioAn1GraphPtSwGraphicsScale2Unit,
       "wtWebioAn1GraphPtSwGraphicsScale3Unit": wtWebioAn1GraphPtSwGraphicsScale3Unit,
       "wtWebioAn1GraphPtSwGraphicsScale4Unit": wtWebioAn1GraphPtSwGraphicsScale4Unit,
       "wtWebioAn1GraphPtSwReport": wtWebioAn1GraphPtSwReport,
       "wtWebioAn1GraphPtSwReportCount": wtWebioAn1GraphPtSwReportCount,
       "wtWebioAn1GraphPtSwReportIfTable": wtWebioAn1GraphPtSwReportIfTable,
       "wtWebioAn1GraphPtSwReportIfEntry": wtWebioAn1GraphPtSwReportIfEntry,
       "wtWebioAn1GraphPtSwReportNo": wtWebioAn1GraphPtSwReportNo,
       "wtWebioAn1GraphPtSwReportTable": wtWebioAn1GraphPtSwReportTable,
       "wtWebioAn1GraphPtSwReportEntry": wtWebioAn1GraphPtSwReportEntry,
       "wtWebioAn1GraphPtSwReportEnable": wtWebioAn1GraphPtSwReportEnable,
       "wtWebioAn1GraphPtSwReportTimerCron": wtWebioAn1GraphPtSwReportTimerCron,
       "wtWebioAn1GraphPtSwReportMethodeEnable": wtWebioAn1GraphPtSwReportMethodeEnable,
       "wtWebioAn1GraphPtSwReportEMailAddr": wtWebioAn1GraphPtSwReportEMailAddr,
       "wtWebioAn1GraphPtSwReportMailSubject": wtWebioAn1GraphPtSwReportMailSubject,
       "wtWebioAn1GraphPtSwReportMailText": wtWebioAn1GraphPtSwReportMailText,
       "wtWebioAn1GraphPtSwReportManagerIP": wtWebioAn1GraphPtSwReportManagerIP,
       "wtWebioAn1GraphPtSwReportTrapText": wtWebioAn1GraphPtSwReportTrapText,
       "wtWebioAn1GraphPtSwReportMailOptions": wtWebioAn1GraphPtSwReportMailOptions,
       "wtWebioAn1GraphPtSwReportTcpIpAddr": wtWebioAn1GraphPtSwReportTcpIpAddr,
       "wtWebioAn1GraphPtSwReportTcpPort": wtWebioAn1GraphPtSwReportTcpPort,
       "wtWebioAn1GraphPtSwReportTcpText": wtWebioAn1GraphPtSwReportTcpText,
       "wtWebioAn1GraphPtSwReportClearMailSubject": wtWebioAn1GraphPtSwReportClearMailSubject,
       "wtWebioAn1GraphPtSwReportClearMailText": wtWebioAn1GraphPtSwReportClearMailText,
       "wtWebioAn1GraphPtSwReportClearTrapText": wtWebioAn1GraphPtSwReportClearTrapText,
       "wtWebioAn1GraphPtSwReportClearTcpText": wtWebioAn1GraphPtSwReportClearTcpText,
       "wtWebioAn1GraphPtSwReportSyslogIpAddr": wtWebioAn1GraphPtSwReportSyslogIpAddr,
       "wtWebioAn1GraphPtSwReportSyslogPort": wtWebioAn1GraphPtSwReportSyslogPort,
       "wtWebioAn1GraphPtSwReportSyslogText": wtWebioAn1GraphPtSwReportSyslogText,
       "wtWebioAn1GraphPtSwReportSyslogClearText": wtWebioAn1GraphPtSwReportSyslogClearText,
       "wtWebioAn1GraphPtSwReportFtpDataPort": wtWebioAn1GraphPtSwReportFtpDataPort,
       "wtWebioAn1GraphPtSwReportFtpFileName": wtWebioAn1GraphPtSwReportFtpFileName,
       "wtWebioAn1GraphPtSwReportFtpText": wtWebioAn1GraphPtSwReportFtpText,
       "wtWebioAn1GraphPtSwReportFtpClearText": wtWebioAn1GraphPtSwReportFtpClearText,
       "wtWebioAn1GraphPtSwReportFtpOption": wtWebioAn1GraphPtSwReportFtpOption,
       "wtWebioAn1GraphPtSwPorts": wtWebioAn1GraphPtSwPorts,
       "wtWebioAn1GraphPtSwPortTable": wtWebioAn1GraphPtSwPortTable,
       "wtWebioAn1GraphPtSwPortEntry": wtWebioAn1GraphPtSwPortEntry,
       "wtWebioAn1GraphPtSwPortName": wtWebioAn1GraphPtSwPortName,
       "wtWebioAn1GraphPtSwPortText": wtWebioAn1GraphPtSwPortText,
       "wtWebioAn1GraphPtSwPortOffset1": wtWebioAn1GraphPtSwPortOffset1,
       "wtWebioAn1GraphPtSwPortTemperature1": wtWebioAn1GraphPtSwPortTemperature1,
       "wtWebioAn1GraphPtSwPortOffset2": wtWebioAn1GraphPtSwPortOffset2,
       "wtWebioAn1GraphPtSwPortTemperature2": wtWebioAn1GraphPtSwPortTemperature2,
       "wtWebioAn1GraphPtSwPortComment": wtWebioAn1GraphPtSwPortComment,
       "wtWebioAn1GraphPtSwPortSensorSelect": wtWebioAn1GraphPtSwPortSensorSelect,
       "wtWebioAn1GraphPtSwPortSensorUnit": wtWebioAn1GraphPtSwPortSensorUnit,
       "wtWebioAn1GraphPtSwPortOutputTable": wtWebioAn1GraphPtSwPortOutputTable,
       "wtWebioAn1GraphPtSwPortOutputEntry": wtWebioAn1GraphPtSwPortOutputEntry,
       "wtWebioAn1GraphPtSwPortOutputName": wtWebioAn1GraphPtSwPortOutputName,
       "wtWebioAn1GraphPtSwPortOutputText": wtWebioAn1GraphPtSwPortOutputText,
       "wtWebioAn1GraphPtSwPortOutputPolarity": wtWebioAn1GraphPtSwPortOutputPolarity,
       "wtWebioAn1GraphPtSwPortOutputComment": wtWebioAn1GraphPtSwPortOutputComment,
       "wtWebioAn1GraphPortOutputResetEnable": wtWebioAn1GraphPortOutputResetEnable,
       "wtWebioAn1GraphPtSwManufact": wtWebioAn1GraphPtSwManufact,
       "wtWebioAn1GraphPtSwMfName": wtWebioAn1GraphPtSwMfName,
       "wtWebioAn1GraphPtSwMfAddr": wtWebioAn1GraphPtSwMfAddr,
       "wtWebioAn1GraphPtSwMfHotline": wtWebioAn1GraphPtSwMfHotline,
       "wtWebioAn1GraphPtSwMfInternet": wtWebioAn1GraphPtSwMfInternet,
       "wtWebioAn1GraphPtSwMfDeviceTyp": wtWebioAn1GraphPtSwMfDeviceTyp,
       "wtWebioAn1GraphPtSwMfOrderNo": wtWebioAn1GraphPtSwMfOrderNo,
       "wtWebioAn1GraphPtSwDiag": wtWebioAn1GraphPtSwDiag,
       "wtWebioAn1GraphPtSwDiagErrorCount": wtWebioAn1GraphPtSwDiagErrorCount,
       "wtWebioAn1GraphPtSwDiagBinaryError": wtWebioAn1GraphPtSwDiagBinaryError,
       "wtWebioAn1GraphPtSwDiagErrorIndex": wtWebioAn1GraphPtSwDiagErrorIndex,
       "wtWebioAn1GraphPtSwDiagErrorMessage": wtWebioAn1GraphPtSwDiagErrorMessage,
       "wtWebioAn1GraphPtSwDiagErrorClear": wtWebioAn1GraphPtSwDiagErrorClear}
)
