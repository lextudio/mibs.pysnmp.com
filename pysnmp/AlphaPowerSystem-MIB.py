# SNMP MIB module (AlphaPowerSystem-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AlphaPowerSystem-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:05 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alpha = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dcpower_ObjectIdentity = ObjectIdentity
dcpower = _Dcpower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4)
)
_DcPwrSysDevice_ObjectIdentity = ObjectIdentity
dcPwrSysDevice = _DcPwrSysDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1)
)
_DcPwrSysVariable_ObjectIdentity = ObjectIdentity
dcPwrSysVariable = _DcPwrSysVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1)
)


class _DcPwrSysChargeVolts_Type(Integer32):
    """Custom type dcPwrSysChargeVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysChargeVolts_Type.__name__ = "Integer32"
_DcPwrSysChargeVolts_Object = MibScalar
dcPwrSysChargeVolts = _DcPwrSysChargeVolts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 1),
    _DcPwrSysChargeVolts_Type()
)
dcPwrSysChargeVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysChargeVolts.setStatus("current")


class _DcPwrSysDischargeVolts_Type(Integer32):
    """Custom type dcPwrSysDischargeVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysDischargeVolts_Type.__name__ = "Integer32"
_DcPwrSysDischargeVolts_Object = MibScalar
dcPwrSysDischargeVolts = _DcPwrSysDischargeVolts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 2),
    _DcPwrSysDischargeVolts_Type()
)
dcPwrSysDischargeVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDischargeVolts.setStatus("current")


class _DcPwrSysChargeAmps_Type(Integer32):
    """Custom type dcPwrSysChargeAmps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysChargeAmps_Type.__name__ = "Integer32"
_DcPwrSysChargeAmps_Object = MibScalar
dcPwrSysChargeAmps = _DcPwrSysChargeAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 3),
    _DcPwrSysChargeAmps_Type()
)
dcPwrSysChargeAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysChargeAmps.setStatus("current")


class _DcPwrSysDischargeAmps_Type(Integer32):
    """Custom type dcPwrSysDischargeAmps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysDischargeAmps_Type.__name__ = "Integer32"
_DcPwrSysDischargeAmps_Object = MibScalar
dcPwrSysDischargeAmps = _DcPwrSysDischargeAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 4),
    _DcPwrSysDischargeAmps_Type()
)
dcPwrSysDischargeAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDischargeAmps.setStatus("current")


class _DcPwrSysMajorAlarm_Type(Integer32):
    """Custom type dcPwrSysMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysMajorAlarm_Type.__name__ = "Integer32"
_DcPwrSysMajorAlarm_Object = MibScalar
dcPwrSysMajorAlarm = _DcPwrSysMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 5),
    _DcPwrSysMajorAlarm_Type()
)
dcPwrSysMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMajorAlarm.setStatus("current")


class _DcPwrSysMinorAlarm_Type(Integer32):
    """Custom type dcPwrSysMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysMinorAlarm_Type.__name__ = "Integer32"
_DcPwrSysMinorAlarm_Object = MibScalar
dcPwrSysMinorAlarm = _DcPwrSysMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 1, 6),
    _DcPwrSysMinorAlarm_Type()
)
dcPwrSysMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMinorAlarm.setStatus("current")
_DcPwrSysString_ObjectIdentity = ObjectIdentity
dcPwrSysString = _DcPwrSysString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2)
)


class _DcPwrSysSiteName_Type(DisplayString):
    """Custom type dcPwrSysSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSiteName_Type.__name__ = "DisplayString"
_DcPwrSysSiteName_Object = MibScalar
dcPwrSysSiteName = _DcPwrSysSiteName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 1),
    _DcPwrSysSiteName_Type()
)
dcPwrSysSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSiteName.setStatus("current")


class _DcPwrSysSiteCity_Type(DisplayString):
    """Custom type dcPwrSysSiteCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSiteCity_Type.__name__ = "DisplayString"
_DcPwrSysSiteCity_Object = MibScalar
dcPwrSysSiteCity = _DcPwrSysSiteCity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 2),
    _DcPwrSysSiteCity_Type()
)
dcPwrSysSiteCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSiteCity.setStatus("current")


class _DcPwrSysSiteRegion_Type(DisplayString):
    """Custom type dcPwrSysSiteRegion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSiteRegion_Type.__name__ = "DisplayString"
_DcPwrSysSiteRegion_Object = MibScalar
dcPwrSysSiteRegion = _DcPwrSysSiteRegion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 3),
    _DcPwrSysSiteRegion_Type()
)
dcPwrSysSiteRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSiteRegion.setStatus("current")


class _DcPwrSysSiteCountry_Type(DisplayString):
    """Custom type dcPwrSysSiteCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSiteCountry_Type.__name__ = "DisplayString"
_DcPwrSysSiteCountry_Object = MibScalar
dcPwrSysSiteCountry = _DcPwrSysSiteCountry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 4),
    _DcPwrSysSiteCountry_Type()
)
dcPwrSysSiteCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSiteCountry.setStatus("current")


class _DcPwrSysContactName_Type(DisplayString):
    """Custom type dcPwrSysContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysContactName_Type.__name__ = "DisplayString"
_DcPwrSysContactName_Object = MibScalar
dcPwrSysContactName = _DcPwrSysContactName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 5),
    _DcPwrSysContactName_Type()
)
dcPwrSysContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysContactName.setStatus("current")


class _DcPwrSysPhoneNumber_Type(DisplayString):
    """Custom type dcPwrSysPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysPhoneNumber_Type.__name__ = "DisplayString"
_DcPwrSysPhoneNumber_Object = MibScalar
dcPwrSysPhoneNumber = _DcPwrSysPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 6),
    _DcPwrSysPhoneNumber_Type()
)
dcPwrSysPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysPhoneNumber.setStatus("current")


class _DcPwrSysSiteNumber_Type(DisplayString):
    """Custom type dcPwrSysSiteNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSiteNumber_Type.__name__ = "DisplayString"
_DcPwrSysSiteNumber_Object = MibScalar
dcPwrSysSiteNumber = _DcPwrSysSiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 7),
    _DcPwrSysSiteNumber_Type()
)
dcPwrSysSiteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSiteNumber.setStatus("current")


class _DcPwrSysSystemType_Type(DisplayString):
    """Custom type dcPwrSysSystemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSystemType_Type.__name__ = "DisplayString"
_DcPwrSysSystemType_Object = MibScalar
dcPwrSysSystemType = _DcPwrSysSystemType_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 8),
    _DcPwrSysSystemType_Type()
)
dcPwrSysSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSystemType.setStatus("current")


class _DcPwrSysSystemSerial_Type(DisplayString):
    """Custom type dcPwrSysSystemSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSystemSerial_Type.__name__ = "DisplayString"
_DcPwrSysSystemSerial_Object = MibScalar
dcPwrSysSystemSerial = _DcPwrSysSystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 9),
    _DcPwrSysSystemSerial_Type()
)
dcPwrSysSystemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSystemSerial.setStatus("current")


class _DcPwrSysSystemNumber_Type(DisplayString):
    """Custom type dcPwrSysSystemNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSystemNumber_Type.__name__ = "DisplayString"
_DcPwrSysSystemNumber_Object = MibScalar
dcPwrSysSystemNumber = _DcPwrSysSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 10),
    _DcPwrSysSystemNumber_Type()
)
dcPwrSysSystemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSystemNumber.setStatus("current")


class _DcPwrSysSoftwareVersion_Type(DisplayString):
    """Custom type dcPwrSysSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSoftwareVersion_Type.__name__ = "DisplayString"
_DcPwrSysSoftwareVersion_Object = MibScalar
dcPwrSysSoftwareVersion = _DcPwrSysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 11),
    _DcPwrSysSoftwareVersion_Type()
)
dcPwrSysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSoftwareVersion.setStatus("current")


class _DcPwrSysSoftwareTimestamp_Type(DisplayString):
    """Custom type dcPwrSysSoftwareTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysSoftwareTimestamp_Type.__name__ = "DisplayString"
_DcPwrSysSoftwareTimestamp_Object = MibScalar
dcPwrSysSoftwareTimestamp = _DcPwrSysSoftwareTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 2, 12),
    _DcPwrSysSoftwareTimestamp_Type()
)
dcPwrSysSoftwareTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysSoftwareTimestamp.setStatus("current")
_DcPwrSysTraps_ObjectIdentity = ObjectIdentity
dcPwrSysTraps = _DcPwrSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3)
)
_DcPwrSysTrap_ObjectIdentity = ObjectIdentity
dcPwrSysTrap = _DcPwrSysTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0)
)
_DcPwrSysOutputsTbl_ObjectIdentity = ObjectIdentity
dcPwrSysOutputsTbl = _DcPwrSysOutputsTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4)
)
_DcPwrSysRelayTbl_ObjectIdentity = ObjectIdentity
dcPwrSysRelayTbl = _DcPwrSysRelayTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1)
)


class _DcPwrSysRelayCount_Type(Integer32):
    """Custom type dcPwrSysRelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRelayCount_Type.__name__ = "Integer32"
_DcPwrSysRelayCount_Object = MibScalar
dcPwrSysRelayCount = _DcPwrSysRelayCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 1),
    _DcPwrSysRelayCount_Type()
)
dcPwrSysRelayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelayCount.setStatus("current")
_DcPwrSysRelayTable_Object = MibTable
dcPwrSysRelayTable = _DcPwrSysRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysRelayTable.setStatus("current")
_DcPwrSysRelayEntry_Object = MibTableRow
dcPwrSysRelayEntry = _DcPwrSysRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1)
)
dcPwrSysRelayEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysRelayIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysRelayEntry.setStatus("current")


class _DcPwrSysRelayIndex_Type(Integer32):
    """Custom type dcPwrSysRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRelayIndex_Type.__name__ = "Integer32"
_DcPwrSysRelayIndex_Object = MibTableColumn
dcPwrSysRelayIndex = _DcPwrSysRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1, 1),
    _DcPwrSysRelayIndex_Type()
)
dcPwrSysRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelayIndex.setStatus("current")


class _DcPwrSysRelayName_Type(DisplayString):
    """Custom type dcPwrSysRelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysRelayName_Type.__name__ = "DisplayString"
_DcPwrSysRelayName_Object = MibTableColumn
dcPwrSysRelayName = _DcPwrSysRelayName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1, 2),
    _DcPwrSysRelayName_Type()
)
dcPwrSysRelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelayName.setStatus("current")


class _DcPwrSysRelayIntegerValue_Type(Integer32):
    """Custom type dcPwrSysRelayIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysRelayIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysRelayIntegerValue_Object = MibTableColumn
dcPwrSysRelayIntegerValue = _DcPwrSysRelayIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1, 3),
    _DcPwrSysRelayIntegerValue_Type()
)
dcPwrSysRelayIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelayIntegerValue.setStatus("current")


class _DcPwrSysRelayStringValue_Type(DisplayString):
    """Custom type dcPwrSysRelayStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysRelayStringValue_Type.__name__ = "DisplayString"
_DcPwrSysRelayStringValue_Object = MibTableColumn
dcPwrSysRelayStringValue = _DcPwrSysRelayStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1, 4),
    _DcPwrSysRelayStringValue_Type()
)
dcPwrSysRelayStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelayStringValue.setStatus("current")


class _DcPwrSysRelaySeverity_Type(Integer32):
    """Custom type dcPwrSysRelaySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRelaySeverity_Type.__name__ = "Integer32"
_DcPwrSysRelaySeverity_Object = MibTableColumn
dcPwrSysRelaySeverity = _DcPwrSysRelaySeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 1, 2, 1, 5),
    _DcPwrSysRelaySeverity_Type()
)
dcPwrSysRelaySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRelaySeverity.setStatus("current")
_DcPwrSysAnalogOpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysAnalogOpTbl = _DcPwrSysAnalogOpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2)
)


class _DcPwrSysAnalogOpCount_Type(Integer32):
    """Custom type dcPwrSysAnalogOpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAnalogOpCount_Type.__name__ = "Integer32"
_DcPwrSysAnalogOpCount_Object = MibScalar
dcPwrSysAnalogOpCount = _DcPwrSysAnalogOpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 1),
    _DcPwrSysAnalogOpCount_Type()
)
dcPwrSysAnalogOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpCount.setStatus("current")
_DcPwrSysAnalogOpTable_Object = MibTable
dcPwrSysAnalogOpTable = _DcPwrSysAnalogOpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpTable.setStatus("current")
_DcPwrSysAnalogOpEntry_Object = MibTableRow
dcPwrSysAnalogOpEntry = _DcPwrSysAnalogOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1)
)
dcPwrSysAnalogOpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysAnalogOpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpEntry.setStatus("current")


class _DcPwrSysAnalogOpIndex_Type(Integer32):
    """Custom type dcPwrSysAnalogOpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAnalogOpIndex_Type.__name__ = "Integer32"
_DcPwrSysAnalogOpIndex_Object = MibTableColumn
dcPwrSysAnalogOpIndex = _DcPwrSysAnalogOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1, 1),
    _DcPwrSysAnalogOpIndex_Type()
)
dcPwrSysAnalogOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpIndex.setStatus("current")


class _DcPwrSysAnalogOpName_Type(DisplayString):
    """Custom type dcPwrSysAnalogOpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysAnalogOpName_Type.__name__ = "DisplayString"
_DcPwrSysAnalogOpName_Object = MibTableColumn
dcPwrSysAnalogOpName = _DcPwrSysAnalogOpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1, 2),
    _DcPwrSysAnalogOpName_Type()
)
dcPwrSysAnalogOpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpName.setStatus("current")


class _DcPwrSysAnalogOpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysAnalogOpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysAnalogOpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysAnalogOpIntegerValue_Object = MibTableColumn
dcPwrSysAnalogOpIntegerValue = _DcPwrSysAnalogOpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1, 3),
    _DcPwrSysAnalogOpIntegerValue_Type()
)
dcPwrSysAnalogOpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpIntegerValue.setStatus("current")


class _DcPwrSysAnalogOpStringValue_Type(DisplayString):
    """Custom type dcPwrSysAnalogOpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysAnalogOpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysAnalogOpStringValue_Object = MibTableColumn
dcPwrSysAnalogOpStringValue = _DcPwrSysAnalogOpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1, 4),
    _DcPwrSysAnalogOpStringValue_Type()
)
dcPwrSysAnalogOpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpStringValue.setStatus("current")


class _DcPwrSysAnalogOpSeverity_Type(Integer32):
    """Custom type dcPwrSysAnalogOpSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAnalogOpSeverity_Type.__name__ = "Integer32"
_DcPwrSysAnalogOpSeverity_Object = MibTableColumn
dcPwrSysAnalogOpSeverity = _DcPwrSysAnalogOpSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 4, 2, 2, 1, 5),
    _DcPwrSysAnalogOpSeverity_Type()
)
dcPwrSysAnalogOpSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAnalogOpSeverity.setStatus("current")
_DcPwrSysAlrmsTbl_ObjectIdentity = ObjectIdentity
dcPwrSysAlrmsTbl = _DcPwrSysAlrmsTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5)
)
_DcPwrSysRectAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysRectAlrmTbl = _DcPwrSysRectAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1)
)


class _DcPwrSysRectAlrmCount_Type(Integer32):
    """Custom type dcPwrSysRectAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRectAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysRectAlrmCount_Object = MibScalar
dcPwrSysRectAlrmCount = _DcPwrSysRectAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 1),
    _DcPwrSysRectAlrmCount_Type()
)
dcPwrSysRectAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmCount.setStatus("current")
_DcPwrSysRectAlrmTable_Object = MibTable
dcPwrSysRectAlrmTable = _DcPwrSysRectAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmTable.setStatus("current")
_DcPwrSysRectAlrmEntry_Object = MibTableRow
dcPwrSysRectAlrmEntry = _DcPwrSysRectAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1)
)
dcPwrSysRectAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmEntry.setStatus("current")


class _DcPwrSysRectAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysRectAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRectAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysRectAlrmIndex_Object = MibTableColumn
dcPwrSysRectAlrmIndex = _DcPwrSysRectAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1, 1),
    _DcPwrSysRectAlrmIndex_Type()
)
dcPwrSysRectAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmIndex.setStatus("current")


class _DcPwrSysRectAlrmName_Type(DisplayString):
    """Custom type dcPwrSysRectAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysRectAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysRectAlrmName_Object = MibTableColumn
dcPwrSysRectAlrmName = _DcPwrSysRectAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1, 2),
    _DcPwrSysRectAlrmName_Type()
)
dcPwrSysRectAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmName.setStatus("current")


class _DcPwrSysRectAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysRectAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysRectAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysRectAlrmIntegerValue_Object = MibTableColumn
dcPwrSysRectAlrmIntegerValue = _DcPwrSysRectAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1, 3),
    _DcPwrSysRectAlrmIntegerValue_Type()
)
dcPwrSysRectAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmIntegerValue.setStatus("current")


class _DcPwrSysRectAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysRectAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysRectAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysRectAlrmStringValue_Object = MibTableColumn
dcPwrSysRectAlrmStringValue = _DcPwrSysRectAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1, 4),
    _DcPwrSysRectAlrmStringValue_Type()
)
dcPwrSysRectAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmStringValue.setStatus("current")


class _DcPwrSysRectAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysRectAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRectAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysRectAlrmSeverity_Object = MibTableColumn
dcPwrSysRectAlrmSeverity = _DcPwrSysRectAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 1, 2, 1, 5),
    _DcPwrSysRectAlrmSeverity_Type()
)
dcPwrSysRectAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectAlrmSeverity.setStatus("current")
_DcPwrSysDigAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysDigAlrmTbl = _DcPwrSysDigAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2)
)


class _DcPwrSysDigAlrmCount_Type(Integer32):
    """Custom type dcPwrSysDigAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysDigAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysDigAlrmCount_Object = MibScalar
dcPwrSysDigAlrmCount = _DcPwrSysDigAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 1),
    _DcPwrSysDigAlrmCount_Type()
)
dcPwrSysDigAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmCount.setStatus("current")
_DcPwrSysDigAlrmTable_Object = MibTable
dcPwrSysDigAlrmTable = _DcPwrSysDigAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmTable.setStatus("current")
_DcPwrSysDigAlrmEntry_Object = MibTableRow
dcPwrSysDigAlrmEntry = _DcPwrSysDigAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1)
)
dcPwrSysDigAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysDigAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmEntry.setStatus("current")


class _DcPwrSysDigAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysDigAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysDigAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysDigAlrmIndex_Object = MibTableColumn
dcPwrSysDigAlrmIndex = _DcPwrSysDigAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1, 1),
    _DcPwrSysDigAlrmIndex_Type()
)
dcPwrSysDigAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmIndex.setStatus("current")


class _DcPwrSysDigAlrmName_Type(DisplayString):
    """Custom type dcPwrSysDigAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysDigAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysDigAlrmName_Object = MibTableColumn
dcPwrSysDigAlrmName = _DcPwrSysDigAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1, 2),
    _DcPwrSysDigAlrmName_Type()
)
dcPwrSysDigAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmName.setStatus("current")


class _DcPwrSysDigAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysDigAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysDigAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysDigAlrmIntegerValue_Object = MibTableColumn
dcPwrSysDigAlrmIntegerValue = _DcPwrSysDigAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1, 3),
    _DcPwrSysDigAlrmIntegerValue_Type()
)
dcPwrSysDigAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmIntegerValue.setStatus("current")


class _DcPwrSysDigAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysDigAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysDigAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysDigAlrmStringValue_Object = MibTableColumn
dcPwrSysDigAlrmStringValue = _DcPwrSysDigAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1, 4),
    _DcPwrSysDigAlrmStringValue_Type()
)
dcPwrSysDigAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmStringValue.setStatus("current")


class _DcPwrSysDigAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysDigAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysDigAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysDigAlrmSeverity_Object = MibTableColumn
dcPwrSysDigAlrmSeverity = _DcPwrSysDigAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 2, 2, 1, 5),
    _DcPwrSysDigAlrmSeverity_Type()
)
dcPwrSysDigAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigAlrmSeverity.setStatus("current")
_DcPwrSysCurrAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCurrAlrmTbl = _DcPwrSysCurrAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3)
)


class _DcPwrSysCurrAlrmCount_Type(Integer32):
    """Custom type dcPwrSysCurrAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCurrAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysCurrAlrmCount_Object = MibScalar
dcPwrSysCurrAlrmCount = _DcPwrSysCurrAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 1),
    _DcPwrSysCurrAlrmCount_Type()
)
dcPwrSysCurrAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmCount.setStatus("current")
_DcPwrSysCurrAlrmTable_Object = MibTable
dcPwrSysCurrAlrmTable = _DcPwrSysCurrAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmTable.setStatus("current")
_DcPwrSysCurrAlrmEntry_Object = MibTableRow
dcPwrSysCurrAlrmEntry = _DcPwrSysCurrAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1)
)
dcPwrSysCurrAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCurrAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmEntry.setStatus("current")


class _DcPwrSysCurrAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysCurrAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCurrAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysCurrAlrmIndex_Object = MibTableColumn
dcPwrSysCurrAlrmIndex = _DcPwrSysCurrAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1, 1),
    _DcPwrSysCurrAlrmIndex_Type()
)
dcPwrSysCurrAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmIndex.setStatus("current")


class _DcPwrSysCurrAlrmName_Type(DisplayString):
    """Custom type dcPwrSysCurrAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCurrAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysCurrAlrmName_Object = MibTableColumn
dcPwrSysCurrAlrmName = _DcPwrSysCurrAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1, 2),
    _DcPwrSysCurrAlrmName_Type()
)
dcPwrSysCurrAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmName.setStatus("current")


class _DcPwrSysCurrAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysCurrAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysCurrAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysCurrAlrmIntegerValue_Object = MibTableColumn
dcPwrSysCurrAlrmIntegerValue = _DcPwrSysCurrAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1, 3),
    _DcPwrSysCurrAlrmIntegerValue_Type()
)
dcPwrSysCurrAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmIntegerValue.setStatus("current")


class _DcPwrSysCurrAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysCurrAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCurrAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCurrAlrmStringValue_Object = MibTableColumn
dcPwrSysCurrAlrmStringValue = _DcPwrSysCurrAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1, 4),
    _DcPwrSysCurrAlrmStringValue_Type()
)
dcPwrSysCurrAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmStringValue.setStatus("current")


class _DcPwrSysCurrAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysCurrAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCurrAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysCurrAlrmSeverity_Object = MibTableColumn
dcPwrSysCurrAlrmSeverity = _DcPwrSysCurrAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 3, 2, 1, 5),
    _DcPwrSysCurrAlrmSeverity_Type()
)
dcPwrSysCurrAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCurrAlrmSeverity.setStatus("current")
_DcPwrSysVoltAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysVoltAlrmTbl = _DcPwrSysVoltAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4)
)


class _DcPwrSysVoltAlrmCount_Type(Integer32):
    """Custom type dcPwrSysVoltAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysVoltAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysVoltAlrmCount_Object = MibScalar
dcPwrSysVoltAlrmCount = _DcPwrSysVoltAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 1),
    _DcPwrSysVoltAlrmCount_Type()
)
dcPwrSysVoltAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmCount.setStatus("current")
_DcPwrSysVoltAlrmTable_Object = MibTable
dcPwrSysVoltAlrmTable = _DcPwrSysVoltAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmTable.setStatus("current")
_DcPwrSysVoltAlrmEntry_Object = MibTableRow
dcPwrSysVoltAlrmEntry = _DcPwrSysVoltAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1)
)
dcPwrSysVoltAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysVoltAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmEntry.setStatus("current")


class _DcPwrSysVoltAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysVoltAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysVoltAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysVoltAlrmIndex_Object = MibTableColumn
dcPwrSysVoltAlrmIndex = _DcPwrSysVoltAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1, 1),
    _DcPwrSysVoltAlrmIndex_Type()
)
dcPwrSysVoltAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmIndex.setStatus("current")


class _DcPwrSysVoltAlrmName_Type(DisplayString):
    """Custom type dcPwrSysVoltAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysVoltAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysVoltAlrmName_Object = MibTableColumn
dcPwrSysVoltAlrmName = _DcPwrSysVoltAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1, 2),
    _DcPwrSysVoltAlrmName_Type()
)
dcPwrSysVoltAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmName.setStatus("current")


class _DcPwrSysVoltAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysVoltAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysVoltAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysVoltAlrmIntegerValue_Object = MibTableColumn
dcPwrSysVoltAlrmIntegerValue = _DcPwrSysVoltAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1, 3),
    _DcPwrSysVoltAlrmIntegerValue_Type()
)
dcPwrSysVoltAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmIntegerValue.setStatus("current")


class _DcPwrSysVoltAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysVoltAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysVoltAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysVoltAlrmStringValue_Object = MibTableColumn
dcPwrSysVoltAlrmStringValue = _DcPwrSysVoltAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1, 4),
    _DcPwrSysVoltAlrmStringValue_Type()
)
dcPwrSysVoltAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmStringValue.setStatus("current")


class _DcPwrSysVoltAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysVoltAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysVoltAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysVoltAlrmSeverity_Object = MibTableColumn
dcPwrSysVoltAlrmSeverity = _DcPwrSysVoltAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 4, 2, 1, 5),
    _DcPwrSysVoltAlrmSeverity_Type()
)
dcPwrSysVoltAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysVoltAlrmSeverity.setStatus("current")
_DcPwrSysBattAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysBattAlrmTbl = _DcPwrSysBattAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5)
)


class _DcPwrSysBattAlrmCount_Type(Integer32):
    """Custom type dcPwrSysBattAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysBattAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysBattAlrmCount_Object = MibScalar
dcPwrSysBattAlrmCount = _DcPwrSysBattAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 1),
    _DcPwrSysBattAlrmCount_Type()
)
dcPwrSysBattAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmCount.setStatus("current")
_DcPwrSysBattAlrmTable_Object = MibTable
dcPwrSysBattAlrmTable = _DcPwrSysBattAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmTable.setStatus("current")
_DcPwrSysBattAlrmEntry_Object = MibTableRow
dcPwrSysBattAlrmEntry = _DcPwrSysBattAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1)
)
dcPwrSysBattAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysBattAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmEntry.setStatus("current")


class _DcPwrSysBattAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysBattAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysBattAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysBattAlrmIndex_Object = MibTableColumn
dcPwrSysBattAlrmIndex = _DcPwrSysBattAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1, 1),
    _DcPwrSysBattAlrmIndex_Type()
)
dcPwrSysBattAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmIndex.setStatus("current")


class _DcPwrSysBattAlrmName_Type(DisplayString):
    """Custom type dcPwrSysBattAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysBattAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysBattAlrmName_Object = MibTableColumn
dcPwrSysBattAlrmName = _DcPwrSysBattAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1, 2),
    _DcPwrSysBattAlrmName_Type()
)
dcPwrSysBattAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmName.setStatus("current")


class _DcPwrSysBattAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysBattAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysBattAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysBattAlrmIntegerValue_Object = MibTableColumn
dcPwrSysBattAlrmIntegerValue = _DcPwrSysBattAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1, 3),
    _DcPwrSysBattAlrmIntegerValue_Type()
)
dcPwrSysBattAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmIntegerValue.setStatus("current")


class _DcPwrSysBattAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysBattAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysBattAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysBattAlrmStringValue_Object = MibTableColumn
dcPwrSysBattAlrmStringValue = _DcPwrSysBattAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1, 4),
    _DcPwrSysBattAlrmStringValue_Type()
)
dcPwrSysBattAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmStringValue.setStatus("current")


class _DcPwrSysBattAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysBattAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysBattAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysBattAlrmSeverity_Object = MibTableColumn
dcPwrSysBattAlrmSeverity = _DcPwrSysBattAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 5, 2, 1, 5),
    _DcPwrSysBattAlrmSeverity_Type()
)
dcPwrSysBattAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysBattAlrmSeverity.setStatus("current")
_DcPwrSysTempAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysTempAlrmTbl = _DcPwrSysTempAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6)
)


class _DcPwrSysTempAlrmCount_Type(Integer32):
    """Custom type dcPwrSysTempAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysTempAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysTempAlrmCount_Object = MibScalar
dcPwrSysTempAlrmCount = _DcPwrSysTempAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 1),
    _DcPwrSysTempAlrmCount_Type()
)
dcPwrSysTempAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmCount.setStatus("current")
_DcPwrSysTempAlrmTable_Object = MibTable
dcPwrSysTempAlrmTable = _DcPwrSysTempAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmTable.setStatus("current")
_DcPwrSysTempAlrmEntry_Object = MibTableRow
dcPwrSysTempAlrmEntry = _DcPwrSysTempAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1)
)
dcPwrSysTempAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysTempAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmEntry.setStatus("current")


class _DcPwrSysTempAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysTempAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysTempAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysTempAlrmIndex_Object = MibTableColumn
dcPwrSysTempAlrmIndex = _DcPwrSysTempAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1, 1),
    _DcPwrSysTempAlrmIndex_Type()
)
dcPwrSysTempAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmIndex.setStatus("current")


class _DcPwrSysTempAlrmName_Type(DisplayString):
    """Custom type dcPwrSysTempAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysTempAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysTempAlrmName_Object = MibTableColumn
dcPwrSysTempAlrmName = _DcPwrSysTempAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1, 2),
    _DcPwrSysTempAlrmName_Type()
)
dcPwrSysTempAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmName.setStatus("current")


class _DcPwrSysTempAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysTempAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysTempAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysTempAlrmIntegerValue_Object = MibTableColumn
dcPwrSysTempAlrmIntegerValue = _DcPwrSysTempAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1, 3),
    _DcPwrSysTempAlrmIntegerValue_Type()
)
dcPwrSysTempAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmIntegerValue.setStatus("current")


class _DcPwrSysTempAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysTempAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysTempAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysTempAlrmStringValue_Object = MibTableColumn
dcPwrSysTempAlrmStringValue = _DcPwrSysTempAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1, 4),
    _DcPwrSysTempAlrmStringValue_Type()
)
dcPwrSysTempAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmStringValue.setStatus("current")


class _DcPwrSysTempAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysTempAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysTempAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysTempAlrmSeverity_Object = MibTableColumn
dcPwrSysTempAlrmSeverity = _DcPwrSysTempAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 6, 2, 1, 5),
    _DcPwrSysTempAlrmSeverity_Type()
)
dcPwrSysTempAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTempAlrmSeverity.setStatus("current")
_DcPwrSysCustomAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCustomAlrmTbl = _DcPwrSysCustomAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7)
)


class _DcPwrSysCustomAlrmCount_Type(Integer32):
    """Custom type dcPwrSysCustomAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCustomAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysCustomAlrmCount_Object = MibScalar
dcPwrSysCustomAlrmCount = _DcPwrSysCustomAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 1),
    _DcPwrSysCustomAlrmCount_Type()
)
dcPwrSysCustomAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmCount.setStatus("current")
_DcPwrSysCustomAlrmTable_Object = MibTable
dcPwrSysCustomAlrmTable = _DcPwrSysCustomAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmTable.setStatus("current")
_DcPwrSysCustomAlrmEntry_Object = MibTableRow
dcPwrSysCustomAlrmEntry = _DcPwrSysCustomAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1)
)
dcPwrSysCustomAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCustomAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmEntry.setStatus("current")


class _DcPwrSysCustomAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysCustomAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCustomAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysCustomAlrmIndex_Object = MibTableColumn
dcPwrSysCustomAlrmIndex = _DcPwrSysCustomAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1, 1),
    _DcPwrSysCustomAlrmIndex_Type()
)
dcPwrSysCustomAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmIndex.setStatus("current")


class _DcPwrSysCustomAlrmName_Type(DisplayString):
    """Custom type dcPwrSysCustomAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCustomAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysCustomAlrmName_Object = MibTableColumn
dcPwrSysCustomAlrmName = _DcPwrSysCustomAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1, 2),
    _DcPwrSysCustomAlrmName_Type()
)
dcPwrSysCustomAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmName.setStatus("current")


class _DcPwrSysCustomAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysCustomAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysCustomAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysCustomAlrmIntegerValue_Object = MibTableColumn
dcPwrSysCustomAlrmIntegerValue = _DcPwrSysCustomAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1, 3),
    _DcPwrSysCustomAlrmIntegerValue_Type()
)
dcPwrSysCustomAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmIntegerValue.setStatus("current")


class _DcPwrSysCustomAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysCustomAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCustomAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCustomAlrmStringValue_Object = MibTableColumn
dcPwrSysCustomAlrmStringValue = _DcPwrSysCustomAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1, 4),
    _DcPwrSysCustomAlrmStringValue_Type()
)
dcPwrSysCustomAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmStringValue.setStatus("current")


class _DcPwrSysCustomAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysCustomAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCustomAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysCustomAlrmSeverity_Object = MibTableColumn
dcPwrSysCustomAlrmSeverity = _DcPwrSysCustomAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 7, 2, 1, 5),
    _DcPwrSysCustomAlrmSeverity_Type()
)
dcPwrSysCustomAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomAlrmSeverity.setStatus("current")
_DcPwrSysMiscAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysMiscAlrmTbl = _DcPwrSysMiscAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8)
)


class _DcPwrSysMiscAlrmCount_Type(Integer32):
    """Custom type dcPwrSysMiscAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysMiscAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysMiscAlrmCount_Object = MibScalar
dcPwrSysMiscAlrmCount = _DcPwrSysMiscAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 1),
    _DcPwrSysMiscAlrmCount_Type()
)
dcPwrSysMiscAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmCount.setStatus("current")
_DcPwrSysMiscAlrmTable_Object = MibTable
dcPwrSysMiscAlrmTable = _DcPwrSysMiscAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmTable.setStatus("current")
_DcPwrSysMiscAlrmEntry_Object = MibTableRow
dcPwrSysMiscAlrmEntry = _DcPwrSysMiscAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1)
)
dcPwrSysMiscAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysMiscAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmEntry.setStatus("current")


class _DcPwrSysMiscAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysMiscAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysMiscAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysMiscAlrmIndex_Object = MibTableColumn
dcPwrSysMiscAlrmIndex = _DcPwrSysMiscAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1, 1),
    _DcPwrSysMiscAlrmIndex_Type()
)
dcPwrSysMiscAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmIndex.setStatus("current")


class _DcPwrSysMiscAlrmName_Type(DisplayString):
    """Custom type dcPwrSysMiscAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysMiscAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysMiscAlrmName_Object = MibTableColumn
dcPwrSysMiscAlrmName = _DcPwrSysMiscAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1, 2),
    _DcPwrSysMiscAlrmName_Type()
)
dcPwrSysMiscAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmName.setStatus("current")


class _DcPwrSysMiscAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysMiscAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysMiscAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysMiscAlrmIntegerValue_Object = MibTableColumn
dcPwrSysMiscAlrmIntegerValue = _DcPwrSysMiscAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1, 3),
    _DcPwrSysMiscAlrmIntegerValue_Type()
)
dcPwrSysMiscAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmIntegerValue.setStatus("current")


class _DcPwrSysMiscAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysMiscAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysMiscAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysMiscAlrmStringValue_Object = MibTableColumn
dcPwrSysMiscAlrmStringValue = _DcPwrSysMiscAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1, 4),
    _DcPwrSysMiscAlrmStringValue_Type()
)
dcPwrSysMiscAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmStringValue.setStatus("current")


class _DcPwrSysMiscAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysMiscAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysMiscAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysMiscAlrmSeverity_Object = MibTableColumn
dcPwrSysMiscAlrmSeverity = _DcPwrSysMiscAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 8, 2, 1, 5),
    _DcPwrSysMiscAlrmSeverity_Type()
)
dcPwrSysMiscAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysMiscAlrmSeverity.setStatus("current")
_DcPwrSysCtrlAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCtrlAlrmTbl = _DcPwrSysCtrlAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9)
)


class _DcPwrSysCtrlAlrmCount_Type(Integer32):
    """Custom type dcPwrSysCtrlAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCtrlAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysCtrlAlrmCount_Object = MibScalar
dcPwrSysCtrlAlrmCount = _DcPwrSysCtrlAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 1),
    _DcPwrSysCtrlAlrmCount_Type()
)
dcPwrSysCtrlAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmCount.setStatus("current")
_DcPwrSysCtrlAlrmTable_Object = MibTable
dcPwrSysCtrlAlrmTable = _DcPwrSysCtrlAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmTable.setStatus("current")
_DcPwrSysCtrlAlrmEntry_Object = MibTableRow
dcPwrSysCtrlAlrmEntry = _DcPwrSysCtrlAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1)
)
dcPwrSysCtrlAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCtrlAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmEntry.setStatus("current")


class _DcPwrSysCtrlAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysCtrlAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCtrlAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysCtrlAlrmIndex_Object = MibTableColumn
dcPwrSysCtrlAlrmIndex = _DcPwrSysCtrlAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1, 1),
    _DcPwrSysCtrlAlrmIndex_Type()
)
dcPwrSysCtrlAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmIndex.setStatus("current")


class _DcPwrSysCtrlAlrmName_Type(DisplayString):
    """Custom type dcPwrSysCtrlAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCtrlAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysCtrlAlrmName_Object = MibTableColumn
dcPwrSysCtrlAlrmName = _DcPwrSysCtrlAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1, 2),
    _DcPwrSysCtrlAlrmName_Type()
)
dcPwrSysCtrlAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmName.setStatus("current")


class _DcPwrSysCtrlAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysCtrlAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysCtrlAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysCtrlAlrmIntegerValue_Object = MibTableColumn
dcPwrSysCtrlAlrmIntegerValue = _DcPwrSysCtrlAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1, 3),
    _DcPwrSysCtrlAlrmIntegerValue_Type()
)
dcPwrSysCtrlAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmIntegerValue.setStatus("current")


class _DcPwrSysCtrlAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysCtrlAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCtrlAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCtrlAlrmStringValue_Object = MibTableColumn
dcPwrSysCtrlAlrmStringValue = _DcPwrSysCtrlAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1, 4),
    _DcPwrSysCtrlAlrmStringValue_Type()
)
dcPwrSysCtrlAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmStringValue.setStatus("current")


class _DcPwrSysCtrlAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysCtrlAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCtrlAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysCtrlAlrmSeverity_Object = MibTableColumn
dcPwrSysCtrlAlrmSeverity = _DcPwrSysCtrlAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 9, 2, 1, 5),
    _DcPwrSysCtrlAlrmSeverity_Type()
)
dcPwrSysCtrlAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCtrlAlrmSeverity.setStatus("current")
_DcPwrSysAdioAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysAdioAlrmTbl = _DcPwrSysAdioAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10)
)


class _DcPwrSysAdioAlrmCount_Type(Integer32):
    """Custom type dcPwrSysAdioAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAdioAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysAdioAlrmCount_Object = MibScalar
dcPwrSysAdioAlrmCount = _DcPwrSysAdioAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 1),
    _DcPwrSysAdioAlrmCount_Type()
)
dcPwrSysAdioAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmCount.setStatus("current")
_DcPwrSysAdioAlrmTable_Object = MibTable
dcPwrSysAdioAlrmTable = _DcPwrSysAdioAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmTable.setStatus("current")
_DcPwrSysAdioAlrmEntry_Object = MibTableRow
dcPwrSysAdioAlrmEntry = _DcPwrSysAdioAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1)
)
dcPwrSysAdioAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysAdioAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmEntry.setStatus("current")


class _DcPwrSysAdioAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysAdioAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAdioAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysAdioAlrmIndex_Object = MibTableColumn
dcPwrSysAdioAlrmIndex = _DcPwrSysAdioAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1, 1),
    _DcPwrSysAdioAlrmIndex_Type()
)
dcPwrSysAdioAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmIndex.setStatus("current")


class _DcPwrSysAdioAlrmName_Type(DisplayString):
    """Custom type dcPwrSysAdioAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysAdioAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysAdioAlrmName_Object = MibTableColumn
dcPwrSysAdioAlrmName = _DcPwrSysAdioAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1, 2),
    _DcPwrSysAdioAlrmName_Type()
)
dcPwrSysAdioAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmName.setStatus("current")


class _DcPwrSysAdioAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysAdioAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysAdioAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysAdioAlrmIntegerValue_Object = MibTableColumn
dcPwrSysAdioAlrmIntegerValue = _DcPwrSysAdioAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1, 3),
    _DcPwrSysAdioAlrmIntegerValue_Type()
)
dcPwrSysAdioAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmIntegerValue.setStatus("current")


class _DcPwrSysAdioAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysAdioAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysAdioAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysAdioAlrmStringValue_Object = MibTableColumn
dcPwrSysAdioAlrmStringValue = _DcPwrSysAdioAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1, 4),
    _DcPwrSysAdioAlrmStringValue_Type()
)
dcPwrSysAdioAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmStringValue.setStatus("current")


class _DcPwrSysAdioAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysAdioAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAdioAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysAdioAlrmSeverity_Object = MibTableColumn
dcPwrSysAdioAlrmSeverity = _DcPwrSysAdioAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 10, 2, 1, 5),
    _DcPwrSysAdioAlrmSeverity_Type()
)
dcPwrSysAdioAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAdioAlrmSeverity.setStatus("current")
_DcPwrSysConvAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysConvAlrmTbl = _DcPwrSysConvAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11)
)


class _DcPwrSysConvAlrmCount_Type(Integer32):
    """Custom type dcPwrSysConvAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysConvAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysConvAlrmCount_Object = MibScalar
dcPwrSysConvAlrmCount = _DcPwrSysConvAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 1),
    _DcPwrSysConvAlrmCount_Type()
)
dcPwrSysConvAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmCount.setStatus("current")
_DcPwrSysConvAlrmTable_Object = MibTable
dcPwrSysConvAlrmTable = _DcPwrSysConvAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmTable.setStatus("current")
_DcPwrSysConvAlrmEntry_Object = MibTableRow
dcPwrSysConvAlrmEntry = _DcPwrSysConvAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1)
)
dcPwrSysConvAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysConvAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmEntry.setStatus("current")


class _DcPwrSysConvAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysConvAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysConvAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysConvAlrmIndex_Object = MibTableColumn
dcPwrSysConvAlrmIndex = _DcPwrSysConvAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1, 1),
    _DcPwrSysConvAlrmIndex_Type()
)
dcPwrSysConvAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmIndex.setStatus("current")


class _DcPwrSysConvAlrmName_Type(DisplayString):
    """Custom type dcPwrSysConvAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysConvAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysConvAlrmName_Object = MibTableColumn
dcPwrSysConvAlrmName = _DcPwrSysConvAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1, 2),
    _DcPwrSysConvAlrmName_Type()
)
dcPwrSysConvAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmName.setStatus("current")


class _DcPwrSysConvAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysConvAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysConvAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysConvAlrmIntegerValue_Object = MibTableColumn
dcPwrSysConvAlrmIntegerValue = _DcPwrSysConvAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1, 3),
    _DcPwrSysConvAlrmIntegerValue_Type()
)
dcPwrSysConvAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmIntegerValue.setStatus("current")


class _DcPwrSysConvAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysConvAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysConvAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysConvAlrmStringValue_Object = MibTableColumn
dcPwrSysConvAlrmStringValue = _DcPwrSysConvAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1, 4),
    _DcPwrSysConvAlrmStringValue_Type()
)
dcPwrSysConvAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmStringValue.setStatus("current")


class _DcPwrSysConvAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysConvAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysConvAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysConvAlrmSeverity_Object = MibTableColumn
dcPwrSysConvAlrmSeverity = _DcPwrSysConvAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 11, 2, 1, 5),
    _DcPwrSysConvAlrmSeverity_Type()
)
dcPwrSysConvAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvAlrmSeverity.setStatus("current")
_DcPwrSysInvAlrmTbl_ObjectIdentity = ObjectIdentity
dcPwrSysInvAlrmTbl = _DcPwrSysInvAlrmTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12)
)


class _DcPwrSysInvAlrmCount_Type(Integer32):
    """Custom type dcPwrSysInvAlrmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysInvAlrmCount_Type.__name__ = "Integer32"
_DcPwrSysInvAlrmCount_Object = MibScalar
dcPwrSysInvAlrmCount = _DcPwrSysInvAlrmCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 1),
    _DcPwrSysInvAlrmCount_Type()
)
dcPwrSysInvAlrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmCount.setStatus("current")
_DcPwrSysInvAlrmTable_Object = MibTable
dcPwrSysInvAlrmTable = _DcPwrSysInvAlrmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmTable.setStatus("current")
_DcPwrSysInvAlrmEntry_Object = MibTableRow
dcPwrSysInvAlrmEntry = _DcPwrSysInvAlrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1)
)
dcPwrSysInvAlrmEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysInvAlrmIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmEntry.setStatus("current")


class _DcPwrSysInvAlrmIndex_Type(Integer32):
    """Custom type dcPwrSysInvAlrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysInvAlrmIndex_Type.__name__ = "Integer32"
_DcPwrSysInvAlrmIndex_Object = MibTableColumn
dcPwrSysInvAlrmIndex = _DcPwrSysInvAlrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1, 1),
    _DcPwrSysInvAlrmIndex_Type()
)
dcPwrSysInvAlrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmIndex.setStatus("current")


class _DcPwrSysInvAlrmName_Type(DisplayString):
    """Custom type dcPwrSysInvAlrmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysInvAlrmName_Type.__name__ = "DisplayString"
_DcPwrSysInvAlrmName_Object = MibTableColumn
dcPwrSysInvAlrmName = _DcPwrSysInvAlrmName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1, 2),
    _DcPwrSysInvAlrmName_Type()
)
dcPwrSysInvAlrmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmName.setStatus("current")


class _DcPwrSysInvAlrmIntegerValue_Type(Integer32):
    """Custom type dcPwrSysInvAlrmIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysInvAlrmIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysInvAlrmIntegerValue_Object = MibTableColumn
dcPwrSysInvAlrmIntegerValue = _DcPwrSysInvAlrmIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1, 3),
    _DcPwrSysInvAlrmIntegerValue_Type()
)
dcPwrSysInvAlrmIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmIntegerValue.setStatus("current")


class _DcPwrSysInvAlrmStringValue_Type(DisplayString):
    """Custom type dcPwrSysInvAlrmStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysInvAlrmStringValue_Type.__name__ = "DisplayString"
_DcPwrSysInvAlrmStringValue_Object = MibTableColumn
dcPwrSysInvAlrmStringValue = _DcPwrSysInvAlrmStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1, 4),
    _DcPwrSysInvAlrmStringValue_Type()
)
dcPwrSysInvAlrmStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmStringValue.setStatus("current")


class _DcPwrSysInvAlrmSeverity_Type(Integer32):
    """Custom type dcPwrSysInvAlrmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysInvAlrmSeverity_Type.__name__ = "Integer32"
_DcPwrSysInvAlrmSeverity_Object = MibTableColumn
dcPwrSysInvAlrmSeverity = _DcPwrSysInvAlrmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 5, 12, 2, 1, 5),
    _DcPwrSysInvAlrmSeverity_Type()
)
dcPwrSysInvAlrmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysInvAlrmSeverity.setStatus("current")
_DcPwrSysInputsTbl_ObjectIdentity = ObjectIdentity
dcPwrSysInputsTbl = _DcPwrSysInputsTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6)
)
_DcPwrSysDigIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysDigIpTbl = _DcPwrSysDigIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1)
)


class _DcPwrSysDigIpCount_Type(Integer32):
    """Custom type dcPwrSysDigIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysDigIpCount_Type.__name__ = "Integer32"
_DcPwrSysDigIpCount_Object = MibScalar
dcPwrSysDigIpCount = _DcPwrSysDigIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 1),
    _DcPwrSysDigIpCount_Type()
)
dcPwrSysDigIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigIpCount.setStatus("current")
_DcPwrSysDigIpTable_Object = MibTable
dcPwrSysDigIpTable = _DcPwrSysDigIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysDigIpTable.setStatus("current")
_DcPwrSysDigIpEntry_Object = MibTableRow
dcPwrSysDigIpEntry = _DcPwrSysDigIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2, 1)
)
dcPwrSysDigIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysDigIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysDigIpEntry.setStatus("current")


class _DcPwrSysDigIpIndex_Type(Integer32):
    """Custom type dcPwrSysDigIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysDigIpIndex_Type.__name__ = "Integer32"
_DcPwrSysDigIpIndex_Object = MibTableColumn
dcPwrSysDigIpIndex = _DcPwrSysDigIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2, 1, 1),
    _DcPwrSysDigIpIndex_Type()
)
dcPwrSysDigIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigIpIndex.setStatus("current")


class _DcPwrSysDigIpName_Type(DisplayString):
    """Custom type dcPwrSysDigIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysDigIpName_Type.__name__ = "DisplayString"
_DcPwrSysDigIpName_Object = MibTableColumn
dcPwrSysDigIpName = _DcPwrSysDigIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2, 1, 2),
    _DcPwrSysDigIpName_Type()
)
dcPwrSysDigIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigIpName.setStatus("current")


class _DcPwrSysDigIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysDigIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysDigIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysDigIpIntegerValue_Object = MibTableColumn
dcPwrSysDigIpIntegerValue = _DcPwrSysDigIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2, 1, 3),
    _DcPwrSysDigIpIntegerValue_Type()
)
dcPwrSysDigIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigIpIntegerValue.setStatus("current")


class _DcPwrSysDigIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysDigIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysDigIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysDigIpStringValue_Object = MibTableColumn
dcPwrSysDigIpStringValue = _DcPwrSysDigIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 1, 2, 1, 4),
    _DcPwrSysDigIpStringValue_Type()
)
dcPwrSysDigIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysDigIpStringValue.setStatus("current")
_DcPwrSysCntrlrIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCntrlrIpTbl = _DcPwrSysCntrlrIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2)
)


class _DcPwrSysCntrlrIpCount_Type(Integer32):
    """Custom type dcPwrSysCntrlrIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCntrlrIpCount_Type.__name__ = "Integer32"
_DcPwrSysCntrlrIpCount_Object = MibScalar
dcPwrSysCntrlrIpCount = _DcPwrSysCntrlrIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 1),
    _DcPwrSysCntrlrIpCount_Type()
)
dcPwrSysCntrlrIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpCount.setStatus("current")
_DcPwrSysCntrlrIpTable_Object = MibTable
dcPwrSysCntrlrIpTable = _DcPwrSysCntrlrIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpTable.setStatus("current")
_DcPwrSysCntrlrIpEntry_Object = MibTableRow
dcPwrSysCntrlrIpEntry = _DcPwrSysCntrlrIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2, 1)
)
dcPwrSysCntrlrIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCntrlrIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpEntry.setStatus("current")


class _DcPwrSysCntrlrIpIndex_Type(Integer32):
    """Custom type dcPwrSysCntrlrIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCntrlrIpIndex_Type.__name__ = "Integer32"
_DcPwrSysCntrlrIpIndex_Object = MibTableColumn
dcPwrSysCntrlrIpIndex = _DcPwrSysCntrlrIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2, 1, 1),
    _DcPwrSysCntrlrIpIndex_Type()
)
dcPwrSysCntrlrIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpIndex.setStatus("current")


class _DcPwrSysCntrlrIpName_Type(DisplayString):
    """Custom type dcPwrSysCntrlrIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCntrlrIpName_Type.__name__ = "DisplayString"
_DcPwrSysCntrlrIpName_Object = MibTableColumn
dcPwrSysCntrlrIpName = _DcPwrSysCntrlrIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2, 1, 2),
    _DcPwrSysCntrlrIpName_Type()
)
dcPwrSysCntrlrIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpName.setStatus("current")


class _DcPwrSysCntrlrIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysCntrlrIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysCntrlrIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysCntrlrIpIntegerValue_Object = MibTableColumn
dcPwrSysCntrlrIpIntegerValue = _DcPwrSysCntrlrIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2, 1, 3),
    _DcPwrSysCntrlrIpIntegerValue_Type()
)
dcPwrSysCntrlrIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpIntegerValue.setStatus("current")


class _DcPwrSysCntrlrIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysCntrlrIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCntrlrIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCntrlrIpStringValue_Object = MibTableColumn
dcPwrSysCntrlrIpStringValue = _DcPwrSysCntrlrIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 2, 2, 1, 4),
    _DcPwrSysCntrlrIpStringValue_Type()
)
dcPwrSysCntrlrIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCntrlrIpStringValue.setStatus("current")
_DcPwrSysRectIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysRectIpTbl = _DcPwrSysRectIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3)
)


class _DcPwrSysRectIpCount_Type(Integer32):
    """Custom type dcPwrSysRectIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRectIpCount_Type.__name__ = "Integer32"
_DcPwrSysRectIpCount_Object = MibScalar
dcPwrSysRectIpCount = _DcPwrSysRectIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 1),
    _DcPwrSysRectIpCount_Type()
)
dcPwrSysRectIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectIpCount.setStatus("current")
_DcPwrSysRectIpTable_Object = MibTable
dcPwrSysRectIpTable = _DcPwrSysRectIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysRectIpTable.setStatus("current")
_DcPwrSysRectIpEntry_Object = MibTableRow
dcPwrSysRectIpEntry = _DcPwrSysRectIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2, 1)
)
dcPwrSysRectIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysRectIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysRectIpEntry.setStatus("current")


class _DcPwrSysRectIpIndex_Type(Integer32):
    """Custom type dcPwrSysRectIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysRectIpIndex_Type.__name__ = "Integer32"
_DcPwrSysRectIpIndex_Object = MibTableColumn
dcPwrSysRectIpIndex = _DcPwrSysRectIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2, 1, 1),
    _DcPwrSysRectIpIndex_Type()
)
dcPwrSysRectIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectIpIndex.setStatus("current")


class _DcPwrSysRectIpName_Type(DisplayString):
    """Custom type dcPwrSysRectIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysRectIpName_Type.__name__ = "DisplayString"
_DcPwrSysRectIpName_Object = MibTableColumn
dcPwrSysRectIpName = _DcPwrSysRectIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2, 1, 2),
    _DcPwrSysRectIpName_Type()
)
dcPwrSysRectIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectIpName.setStatus("current")


class _DcPwrSysRectIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysRectIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysRectIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysRectIpIntegerValue_Object = MibTableColumn
dcPwrSysRectIpIntegerValue = _DcPwrSysRectIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2, 1, 3),
    _DcPwrSysRectIpIntegerValue_Type()
)
dcPwrSysRectIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectIpIntegerValue.setStatus("current")


class _DcPwrSysRectIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysRectIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysRectIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysRectIpStringValue_Object = MibTableColumn
dcPwrSysRectIpStringValue = _DcPwrSysRectIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 3, 2, 1, 4),
    _DcPwrSysRectIpStringValue_Type()
)
dcPwrSysRectIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysRectIpStringValue.setStatus("current")
_DcPwrSysCustomIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCustomIpTbl = _DcPwrSysCustomIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4)
)


class _DcPwrSysCustomIpCount_Type(Integer32):
    """Custom type dcPwrSysCustomIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCustomIpCount_Type.__name__ = "Integer32"
_DcPwrSysCustomIpCount_Object = MibScalar
dcPwrSysCustomIpCount = _DcPwrSysCustomIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 1),
    _DcPwrSysCustomIpCount_Type()
)
dcPwrSysCustomIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomIpCount.setStatus("current")
_DcPwrSysCustomIpTable_Object = MibTable
dcPwrSysCustomIpTable = _DcPwrSysCustomIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCustomIpTable.setStatus("current")
_DcPwrSysCustomIpEntry_Object = MibTableRow
dcPwrSysCustomIpEntry = _DcPwrSysCustomIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2, 1)
)
dcPwrSysCustomIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCustomIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCustomIpEntry.setStatus("current")


class _DcPwrSysCustomIpIndex_Type(Integer32):
    """Custom type dcPwrSysCustomIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCustomIpIndex_Type.__name__ = "Integer32"
_DcPwrSysCustomIpIndex_Object = MibTableColumn
dcPwrSysCustomIpIndex = _DcPwrSysCustomIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2, 1, 1),
    _DcPwrSysCustomIpIndex_Type()
)
dcPwrSysCustomIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomIpIndex.setStatus("current")


class _DcPwrSysCustomIpName_Type(DisplayString):
    """Custom type dcPwrSysCustomIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCustomIpName_Type.__name__ = "DisplayString"
_DcPwrSysCustomIpName_Object = MibTableColumn
dcPwrSysCustomIpName = _DcPwrSysCustomIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2, 1, 2),
    _DcPwrSysCustomIpName_Type()
)
dcPwrSysCustomIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomIpName.setStatus("current")


class _DcPwrSysgCustomIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysgCustomIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysgCustomIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysgCustomIpIntegerValue_Object = MibTableColumn
dcPwrSysgCustomIpIntegerValue = _DcPwrSysgCustomIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2, 1, 3),
    _DcPwrSysgCustomIpIntegerValue_Type()
)
dcPwrSysgCustomIpIntegerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPwrSysgCustomIpIntegerValue.setStatus("current")


class _DcPwrSysCustomIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysCustomIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCustomIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCustomIpStringValue_Object = MibTableColumn
dcPwrSysCustomIpStringValue = _DcPwrSysCustomIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 4, 2, 1, 4),
    _DcPwrSysCustomIpStringValue_Type()
)
dcPwrSysCustomIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCustomIpStringValue.setStatus("current")
_DcPwrSysConvIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysConvIpTbl = _DcPwrSysConvIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5)
)


class _DcPwrSysConvIpCount_Type(Integer32):
    """Custom type dcPwrSysConvIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysConvIpCount_Type.__name__ = "Integer32"
_DcPwrSysConvIpCount_Object = MibScalar
dcPwrSysConvIpCount = _DcPwrSysConvIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 1),
    _DcPwrSysConvIpCount_Type()
)
dcPwrSysConvIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvIpCount.setStatus("current")
_DcPwrSysConvIpTable_Object = MibTable
dcPwrSysConvIpTable = _DcPwrSysConvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysConvIpTable.setStatus("current")
_DcPwrSysConvIpEntry_Object = MibTableRow
dcPwrSysConvIpEntry = _DcPwrSysConvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2, 1)
)
dcPwrSysConvIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysConvIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysConvIpEntry.setStatus("current")


class _DcPwrSysConvIpIndex_Type(Integer32):
    """Custom type dcPwrSysConvIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysConvIpIndex_Type.__name__ = "Integer32"
_DcPwrSysConvIpIndex_Object = MibTableColumn
dcPwrSysConvIpIndex = _DcPwrSysConvIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2, 1, 1),
    _DcPwrSysConvIpIndex_Type()
)
dcPwrSysConvIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvIpIndex.setStatus("current")


class _DcPwrSysConvIpName_Type(DisplayString):
    """Custom type dcPwrSysConvIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysConvIpName_Type.__name__ = "DisplayString"
_DcPwrSysConvIpName_Object = MibTableColumn
dcPwrSysConvIpName = _DcPwrSysConvIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2, 1, 2),
    _DcPwrSysConvIpName_Type()
)
dcPwrSysConvIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvIpName.setStatus("current")


class _DcPwrSysConvIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysConvIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysConvIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysConvIpIntegerValue_Object = MibTableColumn
dcPwrSysConvIpIntegerValue = _DcPwrSysConvIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2, 1, 3),
    _DcPwrSysConvIpIntegerValue_Type()
)
dcPwrSysConvIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvIpIntegerValue.setStatus("current")


class _DcPwrSysConvIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysConvIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysConvIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysConvIpStringValue_Object = MibTableColumn
dcPwrSysConvIpStringValue = _DcPwrSysConvIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 5, 2, 1, 4),
    _DcPwrSysConvIpStringValue_Type()
)
dcPwrSysConvIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysConvIpStringValue.setStatus("current")
_DcPwrSysTimerIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysTimerIpTbl = _DcPwrSysTimerIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6)
)


class _DcPwrSysTimerIpCount_Type(Integer32):
    """Custom type dcPwrSysTimerIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysTimerIpCount_Type.__name__ = "Integer32"
_DcPwrSysTimerIpCount_Object = MibScalar
dcPwrSysTimerIpCount = _DcPwrSysTimerIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 1),
    _DcPwrSysTimerIpCount_Type()
)
dcPwrSysTimerIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimerIpCount.setStatus("current")
_DcPwrSysTimerIpTable_Object = MibTable
dcPwrSysTimerIpTable = _DcPwrSysTimerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysTimerIpTable.setStatus("current")
_DcPwrSysTimerIpEntry_Object = MibTableRow
dcPwrSysTimerIpEntry = _DcPwrSysTimerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2, 1)
)
dcPwrSysTimerIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysTimerIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysTimerIpEntry.setStatus("current")


class _DcPwrSysTimerIpIndex_Type(Integer32):
    """Custom type dcPwrSysTimerIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysTimerIpIndex_Type.__name__ = "Integer32"
_DcPwrSysTimerIpIndex_Object = MibTableColumn
dcPwrSysTimerIpIndex = _DcPwrSysTimerIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2, 1, 1),
    _DcPwrSysTimerIpIndex_Type()
)
dcPwrSysTimerIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimerIpIndex.setStatus("current")


class _DcPwrSysTimerIpName_Type(DisplayString):
    """Custom type dcPwrSysTimerIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysTimerIpName_Type.__name__ = "DisplayString"
_DcPwrSysTimerIpName_Object = MibTableColumn
dcPwrSysTimerIpName = _DcPwrSysTimerIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2, 1, 2),
    _DcPwrSysTimerIpName_Type()
)
dcPwrSysTimerIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimerIpName.setStatus("current")


class _DcPwrSysTimerIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysTimerIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysTimerIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysTimerIpIntegerValue_Object = MibTableColumn
dcPwrSysTimerIpIntegerValue = _DcPwrSysTimerIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2, 1, 3),
    _DcPwrSysTimerIpIntegerValue_Type()
)
dcPwrSysTimerIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimerIpIntegerValue.setStatus("current")


class _DcPwrSysTimerIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysTimerIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysTimerIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysTimerIpStringValue_Object = MibTableColumn
dcPwrSysTimerIpStringValue = _DcPwrSysTimerIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 6, 2, 1, 4),
    _DcPwrSysTimerIpStringValue_Type()
)
dcPwrSysTimerIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimerIpStringValue.setStatus("current")
_DcPwrSysCounterIpTbl_ObjectIdentity = ObjectIdentity
dcPwrSysCounterIpTbl = _DcPwrSysCounterIpTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7)
)


class _DcPwrSysCounterIpCount_Type(Integer32):
    """Custom type dcPwrSysCounterIpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCounterIpCount_Type.__name__ = "Integer32"
_DcPwrSysCounterIpCount_Object = MibScalar
dcPwrSysCounterIpCount = _DcPwrSysCounterIpCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 1),
    _DcPwrSysCounterIpCount_Type()
)
dcPwrSysCounterIpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCounterIpCount.setStatus("current")
_DcPwrSysCounterIpTable_Object = MibTable
dcPwrSysCounterIpTable = _DcPwrSysCounterIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    dcPwrSysCounterIpTable.setStatus("current")
_DcPwrSysCounterIpEntry_Object = MibTableRow
dcPwrSysCounterIpEntry = _DcPwrSysCounterIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2, 1)
)
dcPwrSysCounterIpEntry.setIndexNames(
    (0, "AlphaPowerSystem-MIB", "dcPwrSysCounterIpIndex"),
)
if mibBuilder.loadTexts:
    dcPwrSysCounterIpEntry.setStatus("current")


class _DcPwrSysCounterIpIndex_Type(Integer32):
    """Custom type dcPwrSysCounterIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysCounterIpIndex_Type.__name__ = "Integer32"
_DcPwrSysCounterIpIndex_Object = MibTableColumn
dcPwrSysCounterIpIndex = _DcPwrSysCounterIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2, 1, 1),
    _DcPwrSysCounterIpIndex_Type()
)
dcPwrSysCounterIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCounterIpIndex.setStatus("current")


class _DcPwrSysCounterIpName_Type(DisplayString):
    """Custom type dcPwrSysCounterIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DcPwrSysCounterIpName_Type.__name__ = "DisplayString"
_DcPwrSysCounterIpName_Object = MibTableColumn
dcPwrSysCounterIpName = _DcPwrSysCounterIpName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2, 1, 2),
    _DcPwrSysCounterIpName_Type()
)
dcPwrSysCounterIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCounterIpName.setStatus("current")


class _DcPwrSysCounterIpIntegerValue_Type(Integer32):
    """Custom type dcPwrSysCounterIpIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_DcPwrSysCounterIpIntegerValue_Type.__name__ = "Integer32"
_DcPwrSysCounterIpIntegerValue_Object = MibTableColumn
dcPwrSysCounterIpIntegerValue = _DcPwrSysCounterIpIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2, 1, 3),
    _DcPwrSysCounterIpIntegerValue_Type()
)
dcPwrSysCounterIpIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCounterIpIntegerValue.setStatus("current")


class _DcPwrSysCounterIpStringValue_Type(DisplayString):
    """Custom type dcPwrSysCounterIpStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysCounterIpStringValue_Type.__name__ = "DisplayString"
_DcPwrSysCounterIpStringValue_Object = MibTableColumn
dcPwrSysCounterIpStringValue = _DcPwrSysCounterIpStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 6, 7, 2, 1, 4),
    _DcPwrSysCounterIpStringValue_Type()
)
dcPwrSysCounterIpStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysCounterIpStringValue.setStatus("current")
_DcPwrExternalControls_ObjectIdentity = ObjectIdentity
dcPwrExternalControls = _DcPwrExternalControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 8)
)


class _DcPwrSysResyncAlarms_Type(Integer32):
    """Custom type dcPwrSysResyncAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysResyncAlarms_Type.__name__ = "Integer32"
_DcPwrSysResyncAlarms_Object = MibScalar
dcPwrSysResyncAlarms = _DcPwrSysResyncAlarms_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 8, 1),
    _DcPwrSysResyncAlarms_Type()
)
dcPwrSysResyncAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPwrSysResyncAlarms.setStatus("current")
_DcPwrVarbindNameReference_ObjectIdentity = ObjectIdentity
dcPwrVarbindNameReference = _DcPwrVarbindNameReference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 9)
)


class _DcPwrSysAlarmTriggerValue_Type(Integer32):
    """Custom type dcPwrSysAlarmTriggerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcPwrSysAlarmTriggerValue_Type.__name__ = "Integer32"
_DcPwrSysAlarmTriggerValue_Object = MibScalar
dcPwrSysAlarmTriggerValue = _DcPwrSysAlarmTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 9, 1),
    _DcPwrSysAlarmTriggerValue_Type()
)
dcPwrSysAlarmTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysAlarmTriggerValue.setStatus("current")


class _DcPwrSysTimeStamp_Type(DisplayString):
    """Custom type dcPwrSysTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcPwrSysTimeStamp_Type.__name__ = "DisplayString"
_DcPwrSysTimeStamp_Object = MibScalar
dcPwrSysTimeStamp = _DcPwrSysTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 9, 2),
    _DcPwrSysTimeStamp_Type()
)
dcPwrSysTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPwrSysTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

dcPwrSysAlarmActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 1)
)
dcPwrSysAlarmActiveTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"),
        ("AlphaPowerSystem-MIB", "dcPwrSysTimeStamp"),
        ("AlphaPowerSystem-MIB", "dcPwrSysAlarmTriggerValue"))
)
if mibBuilder.loadTexts:
    dcPwrSysAlarmActiveTrap.setStatus(
        "current"
    )

dcPwrSysAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 2)
)
dcPwrSysAlarmClearedTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"),
        ("AlphaPowerSystem-MIB", "dcPwrSysAlarmTriggerValue"))
)
if mibBuilder.loadTexts:
    dcPwrSysAlarmClearedTrap.setStatus(
        "current"
    )

dcPwrSysRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 3)
)
dcPwrSysRelayTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRelayIntegerValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRelayStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRelayIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRelaySeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"))
)
if mibBuilder.loadTexts:
    dcPwrSysRelayTrap.setStatus(
        "current"
    )

dcPwrSysComOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 4)
)
dcPwrSysComOKTrap.setObjects(
    ("AlphaPowerSystem-MIB", "dcPwrSysSiteName")
)
if mibBuilder.loadTexts:
    dcPwrSysComOKTrap.setStatus(
        "current"
    )

dcPwrSysComErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 5)
)
dcPwrSysComErrTrap.setObjects(
    ("AlphaPowerSystem-MIB", "dcPwrSysSiteName")
)
if mibBuilder.loadTexts:
    dcPwrSysComErrTrap.setStatus(
        "current"
    )

dcPwrSysAgentStartupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 6)
)
dcPwrSysAgentStartupTrap.setObjects(
    ("AlphaPowerSystem-MIB", "dcPwrSysSiteName")
)
if mibBuilder.loadTexts:
    dcPwrSysAgentStartupTrap.setStatus(
        "current"
    )

dcPwrSysAgentShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 7)
)
dcPwrSysAgentShutdownTrap.setObjects(
    ("AlphaPowerSystem-MIB", "dcPwrSysSiteName")
)
if mibBuilder.loadTexts:
    dcPwrSysAgentShutdownTrap.setStatus(
        "current"
    )

dcPwrSysMajorAlarmActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 8)
)
dcPwrSysMajorAlarmActiveTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"))
)
if mibBuilder.loadTexts:
    dcPwrSysMajorAlarmActiveTrap.setStatus(
        "current"
    )

dcPwrSysMajorAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 9)
)
dcPwrSysMajorAlarmClearedTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"))
)
if mibBuilder.loadTexts:
    dcPwrSysMajorAlarmClearedTrap.setStatus(
        "current"
    )

dcPwrSysMinorAlarmActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 10)
)
dcPwrSysMinorAlarmActiveTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"))
)
if mibBuilder.loadTexts:
    dcPwrSysMinorAlarmActiveTrap.setStatus(
        "current"
    )

dcPwrSysMinorAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 4, 1, 3, 0, 11)
)
dcPwrSysMinorAlarmClearedTrap.setObjects(
      *(("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmStringValue"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmIndex"),
        ("AlphaPowerSystem-MIB", "dcPwrSysRectAlrmSeverity"),
        ("AlphaPowerSystem-MIB", "dcPwrSysSiteName"))
)
if mibBuilder.loadTexts:
    dcPwrSysMinorAlarmClearedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AlphaPowerSystem-MIB",
    **{"alpha": alpha,
       "dcpower": dcpower,
       "dcPwrSysDevice": dcPwrSysDevice,
       "dcPwrSysVariable": dcPwrSysVariable,
       "dcPwrSysChargeVolts": dcPwrSysChargeVolts,
       "dcPwrSysDischargeVolts": dcPwrSysDischargeVolts,
       "dcPwrSysChargeAmps": dcPwrSysChargeAmps,
       "dcPwrSysDischargeAmps": dcPwrSysDischargeAmps,
       "dcPwrSysMajorAlarm": dcPwrSysMajorAlarm,
       "dcPwrSysMinorAlarm": dcPwrSysMinorAlarm,
       "dcPwrSysString": dcPwrSysString,
       "dcPwrSysSiteName": dcPwrSysSiteName,
       "dcPwrSysSiteCity": dcPwrSysSiteCity,
       "dcPwrSysSiteRegion": dcPwrSysSiteRegion,
       "dcPwrSysSiteCountry": dcPwrSysSiteCountry,
       "dcPwrSysContactName": dcPwrSysContactName,
       "dcPwrSysPhoneNumber": dcPwrSysPhoneNumber,
       "dcPwrSysSiteNumber": dcPwrSysSiteNumber,
       "dcPwrSysSystemType": dcPwrSysSystemType,
       "dcPwrSysSystemSerial": dcPwrSysSystemSerial,
       "dcPwrSysSystemNumber": dcPwrSysSystemNumber,
       "dcPwrSysSoftwareVersion": dcPwrSysSoftwareVersion,
       "dcPwrSysSoftwareTimestamp": dcPwrSysSoftwareTimestamp,
       "dcPwrSysTraps": dcPwrSysTraps,
       "dcPwrSysTrap": dcPwrSysTrap,
       "dcPwrSysAlarmActiveTrap": dcPwrSysAlarmActiveTrap,
       "dcPwrSysAlarmClearedTrap": dcPwrSysAlarmClearedTrap,
       "dcPwrSysRelayTrap": dcPwrSysRelayTrap,
       "dcPwrSysComOKTrap": dcPwrSysComOKTrap,
       "dcPwrSysComErrTrap": dcPwrSysComErrTrap,
       "dcPwrSysAgentStartupTrap": dcPwrSysAgentStartupTrap,
       "dcPwrSysAgentShutdownTrap": dcPwrSysAgentShutdownTrap,
       "dcPwrSysMajorAlarmActiveTrap": dcPwrSysMajorAlarmActiveTrap,
       "dcPwrSysMajorAlarmClearedTrap": dcPwrSysMajorAlarmClearedTrap,
       "dcPwrSysMinorAlarmActiveTrap": dcPwrSysMinorAlarmActiveTrap,
       "dcPwrSysMinorAlarmClearedTrap": dcPwrSysMinorAlarmClearedTrap,
       "dcPwrSysOutputsTbl": dcPwrSysOutputsTbl,
       "dcPwrSysRelayTbl": dcPwrSysRelayTbl,
       "dcPwrSysRelayCount": dcPwrSysRelayCount,
       "dcPwrSysRelayTable": dcPwrSysRelayTable,
       "dcPwrSysRelayEntry": dcPwrSysRelayEntry,
       "dcPwrSysRelayIndex": dcPwrSysRelayIndex,
       "dcPwrSysRelayName": dcPwrSysRelayName,
       "dcPwrSysRelayIntegerValue": dcPwrSysRelayIntegerValue,
       "dcPwrSysRelayStringValue": dcPwrSysRelayStringValue,
       "dcPwrSysRelaySeverity": dcPwrSysRelaySeverity,
       "dcPwrSysAnalogOpTbl": dcPwrSysAnalogOpTbl,
       "dcPwrSysAnalogOpCount": dcPwrSysAnalogOpCount,
       "dcPwrSysAnalogOpTable": dcPwrSysAnalogOpTable,
       "dcPwrSysAnalogOpEntry": dcPwrSysAnalogOpEntry,
       "dcPwrSysAnalogOpIndex": dcPwrSysAnalogOpIndex,
       "dcPwrSysAnalogOpName": dcPwrSysAnalogOpName,
       "dcPwrSysAnalogOpIntegerValue": dcPwrSysAnalogOpIntegerValue,
       "dcPwrSysAnalogOpStringValue": dcPwrSysAnalogOpStringValue,
       "dcPwrSysAnalogOpSeverity": dcPwrSysAnalogOpSeverity,
       "dcPwrSysAlrmsTbl": dcPwrSysAlrmsTbl,
       "dcPwrSysRectAlrmTbl": dcPwrSysRectAlrmTbl,
       "dcPwrSysRectAlrmCount": dcPwrSysRectAlrmCount,
       "dcPwrSysRectAlrmTable": dcPwrSysRectAlrmTable,
       "dcPwrSysRectAlrmEntry": dcPwrSysRectAlrmEntry,
       "dcPwrSysRectAlrmIndex": dcPwrSysRectAlrmIndex,
       "dcPwrSysRectAlrmName": dcPwrSysRectAlrmName,
       "dcPwrSysRectAlrmIntegerValue": dcPwrSysRectAlrmIntegerValue,
       "dcPwrSysRectAlrmStringValue": dcPwrSysRectAlrmStringValue,
       "dcPwrSysRectAlrmSeverity": dcPwrSysRectAlrmSeverity,
       "dcPwrSysDigAlrmTbl": dcPwrSysDigAlrmTbl,
       "dcPwrSysDigAlrmCount": dcPwrSysDigAlrmCount,
       "dcPwrSysDigAlrmTable": dcPwrSysDigAlrmTable,
       "dcPwrSysDigAlrmEntry": dcPwrSysDigAlrmEntry,
       "dcPwrSysDigAlrmIndex": dcPwrSysDigAlrmIndex,
       "dcPwrSysDigAlrmName": dcPwrSysDigAlrmName,
       "dcPwrSysDigAlrmIntegerValue": dcPwrSysDigAlrmIntegerValue,
       "dcPwrSysDigAlrmStringValue": dcPwrSysDigAlrmStringValue,
       "dcPwrSysDigAlrmSeverity": dcPwrSysDigAlrmSeverity,
       "dcPwrSysCurrAlrmTbl": dcPwrSysCurrAlrmTbl,
       "dcPwrSysCurrAlrmCount": dcPwrSysCurrAlrmCount,
       "dcPwrSysCurrAlrmTable": dcPwrSysCurrAlrmTable,
       "dcPwrSysCurrAlrmEntry": dcPwrSysCurrAlrmEntry,
       "dcPwrSysCurrAlrmIndex": dcPwrSysCurrAlrmIndex,
       "dcPwrSysCurrAlrmName": dcPwrSysCurrAlrmName,
       "dcPwrSysCurrAlrmIntegerValue": dcPwrSysCurrAlrmIntegerValue,
       "dcPwrSysCurrAlrmStringValue": dcPwrSysCurrAlrmStringValue,
       "dcPwrSysCurrAlrmSeverity": dcPwrSysCurrAlrmSeverity,
       "dcPwrSysVoltAlrmTbl": dcPwrSysVoltAlrmTbl,
       "dcPwrSysVoltAlrmCount": dcPwrSysVoltAlrmCount,
       "dcPwrSysVoltAlrmTable": dcPwrSysVoltAlrmTable,
       "dcPwrSysVoltAlrmEntry": dcPwrSysVoltAlrmEntry,
       "dcPwrSysVoltAlrmIndex": dcPwrSysVoltAlrmIndex,
       "dcPwrSysVoltAlrmName": dcPwrSysVoltAlrmName,
       "dcPwrSysVoltAlrmIntegerValue": dcPwrSysVoltAlrmIntegerValue,
       "dcPwrSysVoltAlrmStringValue": dcPwrSysVoltAlrmStringValue,
       "dcPwrSysVoltAlrmSeverity": dcPwrSysVoltAlrmSeverity,
       "dcPwrSysBattAlrmTbl": dcPwrSysBattAlrmTbl,
       "dcPwrSysBattAlrmCount": dcPwrSysBattAlrmCount,
       "dcPwrSysBattAlrmTable": dcPwrSysBattAlrmTable,
       "dcPwrSysBattAlrmEntry": dcPwrSysBattAlrmEntry,
       "dcPwrSysBattAlrmIndex": dcPwrSysBattAlrmIndex,
       "dcPwrSysBattAlrmName": dcPwrSysBattAlrmName,
       "dcPwrSysBattAlrmIntegerValue": dcPwrSysBattAlrmIntegerValue,
       "dcPwrSysBattAlrmStringValue": dcPwrSysBattAlrmStringValue,
       "dcPwrSysBattAlrmSeverity": dcPwrSysBattAlrmSeverity,
       "dcPwrSysTempAlrmTbl": dcPwrSysTempAlrmTbl,
       "dcPwrSysTempAlrmCount": dcPwrSysTempAlrmCount,
       "dcPwrSysTempAlrmTable": dcPwrSysTempAlrmTable,
       "dcPwrSysTempAlrmEntry": dcPwrSysTempAlrmEntry,
       "dcPwrSysTempAlrmIndex": dcPwrSysTempAlrmIndex,
       "dcPwrSysTempAlrmName": dcPwrSysTempAlrmName,
       "dcPwrSysTempAlrmIntegerValue": dcPwrSysTempAlrmIntegerValue,
       "dcPwrSysTempAlrmStringValue": dcPwrSysTempAlrmStringValue,
       "dcPwrSysTempAlrmSeverity": dcPwrSysTempAlrmSeverity,
       "dcPwrSysCustomAlrmTbl": dcPwrSysCustomAlrmTbl,
       "dcPwrSysCustomAlrmCount": dcPwrSysCustomAlrmCount,
       "dcPwrSysCustomAlrmTable": dcPwrSysCustomAlrmTable,
       "dcPwrSysCustomAlrmEntry": dcPwrSysCustomAlrmEntry,
       "dcPwrSysCustomAlrmIndex": dcPwrSysCustomAlrmIndex,
       "dcPwrSysCustomAlrmName": dcPwrSysCustomAlrmName,
       "dcPwrSysCustomAlrmIntegerValue": dcPwrSysCustomAlrmIntegerValue,
       "dcPwrSysCustomAlrmStringValue": dcPwrSysCustomAlrmStringValue,
       "dcPwrSysCustomAlrmSeverity": dcPwrSysCustomAlrmSeverity,
       "dcPwrSysMiscAlrmTbl": dcPwrSysMiscAlrmTbl,
       "dcPwrSysMiscAlrmCount": dcPwrSysMiscAlrmCount,
       "dcPwrSysMiscAlrmTable": dcPwrSysMiscAlrmTable,
       "dcPwrSysMiscAlrmEntry": dcPwrSysMiscAlrmEntry,
       "dcPwrSysMiscAlrmIndex": dcPwrSysMiscAlrmIndex,
       "dcPwrSysMiscAlrmName": dcPwrSysMiscAlrmName,
       "dcPwrSysMiscAlrmIntegerValue": dcPwrSysMiscAlrmIntegerValue,
       "dcPwrSysMiscAlrmStringValue": dcPwrSysMiscAlrmStringValue,
       "dcPwrSysMiscAlrmSeverity": dcPwrSysMiscAlrmSeverity,
       "dcPwrSysCtrlAlrmTbl": dcPwrSysCtrlAlrmTbl,
       "dcPwrSysCtrlAlrmCount": dcPwrSysCtrlAlrmCount,
       "dcPwrSysCtrlAlrmTable": dcPwrSysCtrlAlrmTable,
       "dcPwrSysCtrlAlrmEntry": dcPwrSysCtrlAlrmEntry,
       "dcPwrSysCtrlAlrmIndex": dcPwrSysCtrlAlrmIndex,
       "dcPwrSysCtrlAlrmName": dcPwrSysCtrlAlrmName,
       "dcPwrSysCtrlAlrmIntegerValue": dcPwrSysCtrlAlrmIntegerValue,
       "dcPwrSysCtrlAlrmStringValue": dcPwrSysCtrlAlrmStringValue,
       "dcPwrSysCtrlAlrmSeverity": dcPwrSysCtrlAlrmSeverity,
       "dcPwrSysAdioAlrmTbl": dcPwrSysAdioAlrmTbl,
       "dcPwrSysAdioAlrmCount": dcPwrSysAdioAlrmCount,
       "dcPwrSysAdioAlrmTable": dcPwrSysAdioAlrmTable,
       "dcPwrSysAdioAlrmEntry": dcPwrSysAdioAlrmEntry,
       "dcPwrSysAdioAlrmIndex": dcPwrSysAdioAlrmIndex,
       "dcPwrSysAdioAlrmName": dcPwrSysAdioAlrmName,
       "dcPwrSysAdioAlrmIntegerValue": dcPwrSysAdioAlrmIntegerValue,
       "dcPwrSysAdioAlrmStringValue": dcPwrSysAdioAlrmStringValue,
       "dcPwrSysAdioAlrmSeverity": dcPwrSysAdioAlrmSeverity,
       "dcPwrSysConvAlrmTbl": dcPwrSysConvAlrmTbl,
       "dcPwrSysConvAlrmCount": dcPwrSysConvAlrmCount,
       "dcPwrSysConvAlrmTable": dcPwrSysConvAlrmTable,
       "dcPwrSysConvAlrmEntry": dcPwrSysConvAlrmEntry,
       "dcPwrSysConvAlrmIndex": dcPwrSysConvAlrmIndex,
       "dcPwrSysConvAlrmName": dcPwrSysConvAlrmName,
       "dcPwrSysConvAlrmIntegerValue": dcPwrSysConvAlrmIntegerValue,
       "dcPwrSysConvAlrmStringValue": dcPwrSysConvAlrmStringValue,
       "dcPwrSysConvAlrmSeverity": dcPwrSysConvAlrmSeverity,
       "dcPwrSysInvAlrmTbl": dcPwrSysInvAlrmTbl,
       "dcPwrSysInvAlrmCount": dcPwrSysInvAlrmCount,
       "dcPwrSysInvAlrmTable": dcPwrSysInvAlrmTable,
       "dcPwrSysInvAlrmEntry": dcPwrSysInvAlrmEntry,
       "dcPwrSysInvAlrmIndex": dcPwrSysInvAlrmIndex,
       "dcPwrSysInvAlrmName": dcPwrSysInvAlrmName,
       "dcPwrSysInvAlrmIntegerValue": dcPwrSysInvAlrmIntegerValue,
       "dcPwrSysInvAlrmStringValue": dcPwrSysInvAlrmStringValue,
       "dcPwrSysInvAlrmSeverity": dcPwrSysInvAlrmSeverity,
       "dcPwrSysInputsTbl": dcPwrSysInputsTbl,
       "dcPwrSysDigIpTbl": dcPwrSysDigIpTbl,
       "dcPwrSysDigIpCount": dcPwrSysDigIpCount,
       "dcPwrSysDigIpTable": dcPwrSysDigIpTable,
       "dcPwrSysDigIpEntry": dcPwrSysDigIpEntry,
       "dcPwrSysDigIpIndex": dcPwrSysDigIpIndex,
       "dcPwrSysDigIpName": dcPwrSysDigIpName,
       "dcPwrSysDigIpIntegerValue": dcPwrSysDigIpIntegerValue,
       "dcPwrSysDigIpStringValue": dcPwrSysDigIpStringValue,
       "dcPwrSysCntrlrIpTbl": dcPwrSysCntrlrIpTbl,
       "dcPwrSysCntrlrIpCount": dcPwrSysCntrlrIpCount,
       "dcPwrSysCntrlrIpTable": dcPwrSysCntrlrIpTable,
       "dcPwrSysCntrlrIpEntry": dcPwrSysCntrlrIpEntry,
       "dcPwrSysCntrlrIpIndex": dcPwrSysCntrlrIpIndex,
       "dcPwrSysCntrlrIpName": dcPwrSysCntrlrIpName,
       "dcPwrSysCntrlrIpIntegerValue": dcPwrSysCntrlrIpIntegerValue,
       "dcPwrSysCntrlrIpStringValue": dcPwrSysCntrlrIpStringValue,
       "dcPwrSysRectIpTbl": dcPwrSysRectIpTbl,
       "dcPwrSysRectIpCount": dcPwrSysRectIpCount,
       "dcPwrSysRectIpTable": dcPwrSysRectIpTable,
       "dcPwrSysRectIpEntry": dcPwrSysRectIpEntry,
       "dcPwrSysRectIpIndex": dcPwrSysRectIpIndex,
       "dcPwrSysRectIpName": dcPwrSysRectIpName,
       "dcPwrSysRectIpIntegerValue": dcPwrSysRectIpIntegerValue,
       "dcPwrSysRectIpStringValue": dcPwrSysRectIpStringValue,
       "dcPwrSysCustomIpTbl": dcPwrSysCustomIpTbl,
       "dcPwrSysCustomIpCount": dcPwrSysCustomIpCount,
       "dcPwrSysCustomIpTable": dcPwrSysCustomIpTable,
       "dcPwrSysCustomIpEntry": dcPwrSysCustomIpEntry,
       "dcPwrSysCustomIpIndex": dcPwrSysCustomIpIndex,
       "dcPwrSysCustomIpName": dcPwrSysCustomIpName,
       "dcPwrSysgCustomIpIntegerValue": dcPwrSysgCustomIpIntegerValue,
       "dcPwrSysCustomIpStringValue": dcPwrSysCustomIpStringValue,
       "dcPwrSysConvIpTbl": dcPwrSysConvIpTbl,
       "dcPwrSysConvIpCount": dcPwrSysConvIpCount,
       "dcPwrSysConvIpTable": dcPwrSysConvIpTable,
       "dcPwrSysConvIpEntry": dcPwrSysConvIpEntry,
       "dcPwrSysConvIpIndex": dcPwrSysConvIpIndex,
       "dcPwrSysConvIpName": dcPwrSysConvIpName,
       "dcPwrSysConvIpIntegerValue": dcPwrSysConvIpIntegerValue,
       "dcPwrSysConvIpStringValue": dcPwrSysConvIpStringValue,
       "dcPwrSysTimerIpTbl": dcPwrSysTimerIpTbl,
       "dcPwrSysTimerIpCount": dcPwrSysTimerIpCount,
       "dcPwrSysTimerIpTable": dcPwrSysTimerIpTable,
       "dcPwrSysTimerIpEntry": dcPwrSysTimerIpEntry,
       "dcPwrSysTimerIpIndex": dcPwrSysTimerIpIndex,
       "dcPwrSysTimerIpName": dcPwrSysTimerIpName,
       "dcPwrSysTimerIpIntegerValue": dcPwrSysTimerIpIntegerValue,
       "dcPwrSysTimerIpStringValue": dcPwrSysTimerIpStringValue,
       "dcPwrSysCounterIpTbl": dcPwrSysCounterIpTbl,
       "dcPwrSysCounterIpCount": dcPwrSysCounterIpCount,
       "dcPwrSysCounterIpTable": dcPwrSysCounterIpTable,
       "dcPwrSysCounterIpEntry": dcPwrSysCounterIpEntry,
       "dcPwrSysCounterIpIndex": dcPwrSysCounterIpIndex,
       "dcPwrSysCounterIpName": dcPwrSysCounterIpName,
       "dcPwrSysCounterIpIntegerValue": dcPwrSysCounterIpIntegerValue,
       "dcPwrSysCounterIpStringValue": dcPwrSysCounterIpStringValue,
       "dcPwrExternalControls": dcPwrExternalControls,
       "dcPwrSysResyncAlarms": dcPwrSysResyncAlarms,
       "dcPwrVarbindNameReference": dcPwrVarbindNameReference,
       "dcPwrSysAlarmTriggerValue": dcPwrSysAlarmTriggerValue,
       "dcPwrSysTimeStamp": dcPwrSysTimeStamp}
)
