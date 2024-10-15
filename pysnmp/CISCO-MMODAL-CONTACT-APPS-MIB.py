# SNMP MIB module (CISCO-MMODAL-CONTACT-APPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MMODAL-CONTACT-APPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressDNS,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMmodalContactAppsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664)
)
ciscoMmodalContactAppsMIB.setRevisions(
        ("2008-07-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmmcaIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CmmcaServiceType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bre", 5),
          ("cm", 1),
          ("icmgw", 6),
          ("mpa", 4),
          ("ra", 8),
          ("rda", 7),
          ("rm", 2),
          ("rs", 9),
          ("wa", 3))
    )



class CmmcaServiceStatus(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("inService", 3),
          ("inServiceCritical", 5),
          ("inServiceWarning", 4),
          ("outOfService", 7),
          ("partialService", 6),
          ("starting", 2),
          ("stopped", 9),
          ("stopping", 8),
          ("unknown", 10))
    )



class CmmcaNextNodeStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("unavailable", 3),
          ("unknown", 1))
    )



class CmmcaConditionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conditionCritical", 2),
          ("conditionWarn", 1))
    )



class CmmcaSystemConditionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("statusCritical", 3),
          ("statusNormal", 1),
          ("statusWarning", 2))
    )



class CmmcaSeverityLevel(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMmodalContactAppsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMmodalContactAppsMIBNotifs = _CiscoMmodalContactAppsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 0)
)
_CiscoMmodalContactAppsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMmodalContactAppsMIBObjects = _CiscoMmodalContactAppsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1)
)
_CmmcaGeneralInfo_ObjectIdentity = ObjectIdentity
cmmcaGeneralInfo = _CmmcaGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1)
)
_CmmcaServerName_Type = InetAddressDNS
_CmmcaServerName_Object = MibScalar
cmmcaServerName = _CmmcaServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 1),
    _CmmcaServerName_Type()
)
cmmcaServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaServerName.setStatus("current")
_CmmcaDescription_Type = SnmpAdminString
_CmmcaDescription_Object = MibScalar
cmmcaDescription = _CmmcaDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 2),
    _CmmcaDescription_Type()
)
cmmcaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDescription.setStatus("current")
_CmmcaVersion_Type = SnmpAdminString
_CmmcaVersion_Object = MibScalar
cmmcaVersion = _CmmcaVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 3),
    _CmmcaVersion_Type()
)
cmmcaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaVersion.setStatus("current")
_CmmcaStartTime_Type = DateAndTime
_CmmcaStartTime_Object = MibScalar
cmmcaStartTime = _CmmcaStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 4),
    _CmmcaStartTime_Type()
)
cmmcaStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaStartTime.setStatus("current")
_CmmcaTimeZoneName_Type = SnmpAdminString
_CmmcaTimeZoneName_Object = MibScalar
cmmcaTimeZoneName = _CmmcaTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 5),
    _CmmcaTimeZoneName_Type()
)
cmmcaTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTimeZoneName.setStatus("current")


class _CmmcaTimeZoneOffsetHours_Type(Integer32):
    """Custom type cmmcaTimeZoneOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_CmmcaTimeZoneOffsetHours_Type.__name__ = "Integer32"
_CmmcaTimeZoneOffsetHours_Object = MibScalar
cmmcaTimeZoneOffsetHours = _CmmcaTimeZoneOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 6),
    _CmmcaTimeZoneOffsetHours_Type()
)
cmmcaTimeZoneOffsetHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTimeZoneOffsetHours.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTimeZoneOffsetHours.setUnits("hours")


class _CmmcaTimeZoneOffsetMinutes_Type(Integer32):
    """Custom type cmmcaTimeZoneOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-59, 59),
    )


_CmmcaTimeZoneOffsetMinutes_Type.__name__ = "Integer32"
_CmmcaTimeZoneOffsetMinutes_Object = MibScalar
cmmcaTimeZoneOffsetMinutes = _CmmcaTimeZoneOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 7),
    _CmmcaTimeZoneOffsetMinutes_Type()
)
cmmcaTimeZoneOffsetMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTimeZoneOffsetMinutes.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTimeZoneOffsetMinutes.setUnits("minutes")
_CmmcaOpsConsoleURL_Type = CiscoURLString
_CmmcaOpsConsoleURL_Object = MibScalar
cmmcaOpsConsoleURL = _CmmcaOpsConsoleURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 8),
    _CmmcaOpsConsoleURL_Type()
)
cmmcaOpsConsoleURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaOpsConsoleURL.setStatus("current")


class _CmmcaLocalDeviceType_Type(Integer32):
    """Custom type cmmcaLocalDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("reporting", 2),
          ("runtime", 1))
    )


_CmmcaLocalDeviceType_Type.__name__ = "Integer32"
_CmmcaLocalDeviceType_Object = MibScalar
cmmcaLocalDeviceType = _CmmcaLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 9),
    _CmmcaLocalDeviceType_Type()
)
cmmcaLocalDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaLocalDeviceType.setStatus("current")


class _CmmcaEnableNotifications_Type(TruthValue):
    """Custom type cmmcaEnableNotifications based on TruthValue"""


_CmmcaEnableNotifications_Object = MibScalar
cmmcaEnableNotifications = _CmmcaEnableNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 10),
    _CmmcaEnableNotifications_Type()
)
cmmcaEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmcaEnableNotifications.setStatus("current")
_CmmcaSystemConditionStatus_Type = CmmcaSystemConditionStatus
_CmmcaSystemConditionStatus_Object = MibScalar
cmmcaSystemConditionStatus = _CmmcaSystemConditionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 11),
    _CmmcaSystemConditionStatus_Type()
)
cmmcaSystemConditionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionStatus.setStatus("current")
_CmmcaSystemStatus_Type = CmmcaServiceStatus
_CmmcaSystemStatus_Object = MibScalar
cmmcaSystemStatus = _CmmcaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 12),
    _CmmcaSystemStatus_Type()
)
cmmcaSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemStatus.setStatus("current")
_CmmcaClusterInfoTable_Object = MibTable
cmmcaClusterInfoTable = _CmmcaClusterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cmmcaClusterInfoTable.setStatus("current")
_CmmcaClusterInfoEntry_Object = MibTableRow
cmmcaClusterInfoEntry = _CmmcaClusterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1)
)
cmmcaClusterInfoEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaClusterInfoEntry.setStatus("current")


class _CmmcaDeviceIndex_Type(Integer32):
    """Custom type cmmcaDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CmmcaDeviceIndex_Type.__name__ = "Integer32"
_CmmcaDeviceIndex_Object = MibTableColumn
cmmcaDeviceIndex = _CmmcaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 1),
    _CmmcaDeviceIndex_Type()
)
cmmcaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmcaDeviceIndex.setStatus("current")
_CmmcaDeviceName_Type = SnmpAdminString
_CmmcaDeviceName_Object = MibTableColumn
cmmcaDeviceName = _CmmcaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 2),
    _CmmcaDeviceName_Type()
)
cmmcaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceName.setStatus("current")
_CmmcaDeviceDescription_Type = SnmpAdminString
_CmmcaDeviceDescription_Object = MibTableColumn
cmmcaDeviceDescription = _CmmcaDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 3),
    _CmmcaDeviceDescription_Type()
)
cmmcaDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceDescription.setStatus("current")


class _CmmcaDeviceType_Type(Integer32):
    """Custom type cmmcaDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reporting", 2),
          ("runtime", 1),
          ("unknown", 3))
    )


_CmmcaDeviceType_Type.__name__ = "Integer32"
_CmmcaDeviceType_Object = MibTableColumn
cmmcaDeviceType = _CmmcaDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 4),
    _CmmcaDeviceType_Type()
)
cmmcaDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceType.setStatus("current")


class _CmmcaDeviceStatus_Type(Integer32):
    """Custom type cmmcaDeviceStatus based on Integer32"""
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
        *(("local", 2),
          ("remotedown", 4),
          ("remoteup", 3),
          ("unknown", 1))
    )


_CmmcaDeviceStatus_Type.__name__ = "Integer32"
_CmmcaDeviceStatus_Object = MibTableColumn
cmmcaDeviceStatus = _CmmcaDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 5),
    _CmmcaDeviceStatus_Type()
)
cmmcaDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceStatus.setStatus("current")
_CmmcaDeviceInetAddressType_Type = InetAddressType
_CmmcaDeviceInetAddressType_Object = MibTableColumn
cmmcaDeviceInetAddressType = _CmmcaDeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 6),
    _CmmcaDeviceInetAddressType_Type()
)
cmmcaDeviceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceInetAddressType.setStatus("current")
_CmmcaDeviceInetAddress_Type = InetAddress
_CmmcaDeviceInetAddress_Object = MibTableColumn
cmmcaDeviceInetAddress = _CmmcaDeviceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 7),
    _CmmcaDeviceInetAddress_Type()
)
cmmcaDeviceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaDeviceInetAddress.setStatus("current")
_CmmcaClusterId_Type = SnmpAdminString
_CmmcaClusterId_Object = MibTableColumn
cmmcaClusterId = _CmmcaClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 13, 1, 8),
    _CmmcaClusterId_Type()
)
cmmcaClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaClusterId.setStatus("current")
_CmmcaNextNodeTable_Object = MibTable
cmmcaNextNodeTable = _CmmcaNextNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cmmcaNextNodeTable.setStatus("current")
_CmmcaNextNodeEntry_Object = MibTableRow
cmmcaNextNodeEntry = _CmmcaNextNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1)
)
cmmcaNextNodeEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeIndex"),
)
if mibBuilder.loadTexts:
    cmmcaNextNodeEntry.setStatus("current")


class _CmmcaNextNodeIndex_Type(Integer32):
    """Custom type cmmcaNextNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CmmcaNextNodeIndex_Type.__name__ = "Integer32"
_CmmcaNextNodeIndex_Object = MibTableColumn
cmmcaNextNodeIndex = _CmmcaNextNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 1),
    _CmmcaNextNodeIndex_Type()
)
cmmcaNextNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmcaNextNodeIndex.setStatus("current")
_CmmcaNextNodeName_Type = SnmpAdminString
_CmmcaNextNodeName_Object = MibTableColumn
cmmcaNextNodeName = _CmmcaNextNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 2),
    _CmmcaNextNodeName_Type()
)
cmmcaNextNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaNextNodeName.setStatus("current")
_CmmcaNextNodeType_Type = SnmpAdminString
_CmmcaNextNodeType_Object = MibTableColumn
cmmcaNextNodeType = _CmmcaNextNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 3),
    _CmmcaNextNodeType_Type()
)
cmmcaNextNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaNextNodeType.setStatus("current")
_CmmcaNextNodeIpAddrType_Type = InetAddressType
_CmmcaNextNodeIpAddrType_Object = MibTableColumn
cmmcaNextNodeIpAddrType = _CmmcaNextNodeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 4),
    _CmmcaNextNodeIpAddrType_Type()
)
cmmcaNextNodeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaNextNodeIpAddrType.setStatus("current")
_CmmcaNextNodeIpAddr_Type = InetAddress
_CmmcaNextNodeIpAddr_Object = MibTableColumn
cmmcaNextNodeIpAddr = _CmmcaNextNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 5),
    _CmmcaNextNodeIpAddr_Type()
)
cmmcaNextNodeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaNextNodeIpAddr.setStatus("current")
_CmmcaNextNodeStatus_Type = CmmcaNextNodeStatus
_CmmcaNextNodeStatus_Object = MibTableColumn
cmmcaNextNodeStatus = _CmmcaNextNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 14, 1, 6),
    _CmmcaNextNodeStatus_Type()
)
cmmcaNextNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaNextNodeStatus.setStatus("current")
_CmmcaSystemConditionTable_Object = MibTable
cmmcaSystemConditionTable = _CmmcaSystemConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cmmcaSystemConditionTable.setStatus("current")
_CmmcaSystemConditionEntry_Object = MibTableRow
cmmcaSystemConditionEntry = _CmmcaSystemConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1)
)
cmmcaSystemConditionEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionIndex"),
)
if mibBuilder.loadTexts:
    cmmcaSystemConditionEntry.setStatus("current")


class _CmmcaSystemConditionIndex_Type(Integer32):
    """Custom type cmmcaSystemConditionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CmmcaSystemConditionIndex_Type.__name__ = "Integer32"
_CmmcaSystemConditionIndex_Object = MibTableColumn
cmmcaSystemConditionIndex = _CmmcaSystemConditionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 1),
    _CmmcaSystemConditionIndex_Type()
)
cmmcaSystemConditionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmcaSystemConditionIndex.setStatus("current")


class _CmmcaSystemConditionId_Type(Integer32):
    """Custom type cmmcaSystemConditionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmmcaSystemConditionId_Type.__name__ = "Integer32"
_CmmcaSystemConditionId_Object = MibTableColumn
cmmcaSystemConditionId = _CmmcaSystemConditionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 2),
    _CmmcaSystemConditionId_Type()
)
cmmcaSystemConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionId.setStatus("current")
_CmmcaSystemConditionSeverity_Type = CmmcaConditionStatus
_CmmcaSystemConditionSeverity_Object = MibTableColumn
cmmcaSystemConditionSeverity = _CmmcaSystemConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 3),
    _CmmcaSystemConditionSeverity_Type()
)
cmmcaSystemConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionSeverity.setStatus("current")
_CmmcaSystemConditionDescription_Type = SnmpAdminString
_CmmcaSystemConditionDescription_Object = MibTableColumn
cmmcaSystemConditionDescription = _CmmcaSystemConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 4),
    _CmmcaSystemConditionDescription_Type()
)
cmmcaSystemConditionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionDescription.setStatus("current")
_CmmcaSystemConditionTimeStamp_Type = DateAndTime
_CmmcaSystemConditionTimeStamp_Object = MibTableColumn
cmmcaSystemConditionTimeStamp = _CmmcaSystemConditionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 5),
    _CmmcaSystemConditionTimeStamp_Type()
)
cmmcaSystemConditionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionTimeStamp.setStatus("current")
_CmmcaSystemConditionMessage_Type = SnmpAdminString
_CmmcaSystemConditionMessage_Object = MibTableColumn
cmmcaSystemConditionMessage = _CmmcaSystemConditionMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 1, 15, 1, 6),
    _CmmcaSystemConditionMessage_Type()
)
cmmcaSystemConditionMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaSystemConditionMessage.setStatus("current")
_CmmcaLicenseInfo_ObjectIdentity = ObjectIdentity
cmmcaLicenseInfo = _CmmcaLicenseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 2)
)
_CmmcaRtLicensesAvailable_Type = Gauge32
_CmmcaRtLicensesAvailable_Object = MibScalar
cmmcaRtLicensesAvailable = _CmmcaRtLicensesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 2, 1),
    _CmmcaRtLicensesAvailable_Type()
)
cmmcaRtLicensesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtLicensesAvailable.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtLicensesAvailable.setUnits("agents")
_CmmcaTotalLicensesConfigured_Type = Gauge32
_CmmcaTotalLicensesConfigured_Object = MibScalar
cmmcaTotalLicensesConfigured = _CmmcaTotalLicensesConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 2, 2),
    _CmmcaTotalLicensesConfigured_Type()
)
cmmcaTotalLicensesConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTotalLicensesConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTotalLicensesConfigured.setUnits("agents")
_CmmcaThreadPool_ObjectIdentity = ObjectIdentity
cmmcaThreadPool = _CmmcaThreadPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3)
)
_CmmcaTPoolRtIdleThreads_Type = Gauge32
_CmmcaTPoolRtIdleThreads_Object = MibScalar
cmmcaTPoolRtIdleThreads = _CmmcaTPoolRtIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3, 1),
    _CmmcaTPoolRtIdleThreads_Type()
)
cmmcaTPoolRtIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTPoolRtIdleThreads.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTPoolRtIdleThreads.setUnits("threads")
_CmmcaTPoolRtRunningThreads_Type = Gauge32
_CmmcaTPoolRtRunningThreads_Object = MibScalar
cmmcaTPoolRtRunningThreads = _CmmcaTPoolRtRunningThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3, 2),
    _CmmcaTPoolRtRunningThreads_Type()
)
cmmcaTPoolRtRunningThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTPoolRtRunningThreads.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTPoolRtRunningThreads.setUnits("threads")
_CmmcaTPoolRtCoreThreads_Type = Gauge32
_CmmcaTPoolRtCoreThreads_Object = MibScalar
cmmcaTPoolRtCoreThreads = _CmmcaTPoolRtCoreThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3, 3),
    _CmmcaTPoolRtCoreThreads_Type()
)
cmmcaTPoolRtCoreThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTPoolRtCoreThreads.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTPoolRtCoreThreads.setUnits("threads")
_CmmcaTPoolRtMaxThreadsAvail_Type = Unsigned32
_CmmcaTPoolRtMaxThreadsAvail_Object = MibScalar
cmmcaTPoolRtMaxThreadsAvail = _CmmcaTPoolRtMaxThreadsAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3, 4),
    _CmmcaTPoolRtMaxThreadsAvail_Type()
)
cmmcaTPoolRtMaxThreadsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTPoolRtMaxThreadsAvail.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTPoolRtMaxThreadsAvail.setUnits("threads")
_CmmcaTPoolRtMaxThreadsUsed_Type = Counter32
_CmmcaTPoolRtMaxThreadsUsed_Object = MibScalar
cmmcaTPoolRtMaxThreadsUsed = _CmmcaTPoolRtMaxThreadsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 3, 5),
    _CmmcaTPoolRtMaxThreadsUsed_Type()
)
cmmcaTPoolRtMaxThreadsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaTPoolRtMaxThreadsUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaTPoolRtMaxThreadsUsed.setUnits("threads")
_CmmcaRuntimeInfo_ObjectIdentity = ObjectIdentity
cmmcaRuntimeInfo = _CmmcaRuntimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4)
)
_CmmcaEnvRtMaxMemUsed_Type = CounterBasedGauge64
_CmmcaEnvRtMaxMemUsed_Object = MibScalar
cmmcaEnvRtMaxMemUsed = _CmmcaEnvRtMaxMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 1),
    _CmmcaEnvRtMaxMemUsed_Type()
)
cmmcaEnvRtMaxMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtMaxMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtMaxMemUsed.setUnits("bytes")
_CmmcaEnvRtCurrMemUsed_Type = CounterBasedGauge64
_CmmcaEnvRtCurrMemUsed_Object = MibScalar
cmmcaEnvRtCurrMemUsed = _CmmcaEnvRtCurrMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 2),
    _CmmcaEnvRtCurrMemUsed_Type()
)
cmmcaEnvRtCurrMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrMemUsed.setUnits("bytes")
_CmmcaEnvRtMaxMemAvail_Type = CounterBasedGauge64
_CmmcaEnvRtMaxMemAvail_Object = MibScalar
cmmcaEnvRtMaxMemAvail = _CmmcaEnvRtMaxMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 3),
    _CmmcaEnvRtMaxMemAvail_Type()
)
cmmcaEnvRtMaxMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtMaxMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtMaxMemAvail.setUnits("bytes")
_CmmcaEnvRtCurrMemAvail_Type = CounterBasedGauge64
_CmmcaEnvRtCurrMemAvail_Object = MibScalar
cmmcaEnvRtCurrMemAvail = _CmmcaEnvRtCurrMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 4),
    _CmmcaEnvRtCurrMemAvail_Type()
)
cmmcaEnvRtCurrMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrMemAvail.setUnits("bytes")
_CmmcaEnvRtCurrThreadsInUse_Type = Gauge32
_CmmcaEnvRtCurrThreadsInUse_Object = MibScalar
cmmcaEnvRtCurrThreadsInUse = _CmmcaEnvRtCurrThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 5),
    _CmmcaEnvRtCurrThreadsInUse_Type()
)
cmmcaEnvRtCurrThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrThreadsInUse.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtCurrThreadsInUse.setUnits("threads")
_CmmcaEnvMaxThreadsUsed_Type = Unsigned32
_CmmcaEnvMaxThreadsUsed_Object = MibScalar
cmmcaEnvMaxThreadsUsed = _CmmcaEnvMaxThreadsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 6),
    _CmmcaEnvMaxThreadsUsed_Type()
)
cmmcaEnvMaxThreadsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvMaxThreadsUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvMaxThreadsUsed.setUnits("threads")
_CmmcaEnvRtUpTime_Type = Counter64
_CmmcaEnvRtUpTime_Object = MibScalar
cmmcaEnvRtUpTime = _CmmcaEnvRtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 7),
    _CmmcaEnvRtUpTime_Type()
)
cmmcaEnvRtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaEnvRtUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaEnvRtUpTime.setUnits("milliseconds")
_CmmcaRtMsgQMemPercentUsage_Type = Gauge32
_CmmcaRtMsgQMemPercentUsage_Object = MibScalar
cmmcaRtMsgQMemPercentUsage = _CmmcaRtMsgQMemPercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 8),
    _CmmcaRtMsgQMemPercentUsage_Type()
)
cmmcaRtMsgQMemPercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtMsgQMemPercentUsage.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtMsgQMemPercentUsage.setUnits("percentage")
_CmmcaMaxMsgQMemAvail_Type = CounterBasedGauge64
_CmmcaMaxMsgQMemAvail_Object = MibScalar
cmmcaMaxMsgQMemAvail = _CmmcaMaxMsgQMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 9),
    _CmmcaMaxMsgQMemAvail_Type()
)
cmmcaMaxMsgQMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMaxMsgQMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMaxMsgQMemAvail.setUnits("bytes")
_CmmcaRtCongested_Type = TruthValue
_CmmcaRtCongested_Object = MibScalar
cmmcaRtCongested = _CmmcaRtCongested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 4, 10),
    _CmmcaRtCongested_Type()
)
cmmcaRtCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtCongested.setStatus("current")
_CmmcaServices_ObjectIdentity = ObjectIdentity
cmmcaServices = _CmmcaServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5)
)
_CmmcaServiceTable_Object = MibTable
cmmcaServiceTable = _CmmcaServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cmmcaServiceTable.setStatus("current")
_CmmcaServiceEntry_Object = MibTableRow
cmmcaServiceEntry = _CmmcaServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1)
)
cmmcaServiceEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaServiceEntry.setStatus("current")


class _CmmcaServiceIndex_Type(CmmcaIndex):
    """Custom type cmmcaServiceIndex based on CmmcaIndex"""
    subtypeSpec = CmmcaIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CmmcaServiceIndex_Type.__name__ = "CmmcaIndex"
_CmmcaServiceIndex_Object = MibTableColumn
cmmcaServiceIndex = _CmmcaServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 1),
    _CmmcaServiceIndex_Type()
)
cmmcaServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmcaServiceIndex.setStatus("current")
_CmmcaServiceType_Type = CmmcaServiceType
_CmmcaServiceType_Object = MibTableColumn
cmmcaServiceType = _CmmcaServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 2),
    _CmmcaServiceType_Type()
)
cmmcaServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaServiceType.setStatus("current")
_CmmcaServiceName_Type = SnmpAdminString
_CmmcaServiceName_Object = MibTableColumn
cmmcaServiceName = _CmmcaServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 3),
    _CmmcaServiceName_Type()
)
cmmcaServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaServiceName.setStatus("current")
_CmmcaServiceStatus_Type = CmmcaServiceStatus
_CmmcaServiceStatus_Object = MibTableColumn
cmmcaServiceStatus = _CmmcaServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 4),
    _CmmcaServiceStatus_Type()
)
cmmcaServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaServiceStatus.setStatus("current")


class _CmmcaServiceIntPeriod_Type(Gauge32):
    """Custom type cmmcaServiceIntPeriod based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_CmmcaServiceIntPeriod_Type.__name__ = "Gauge32"
_CmmcaServiceIntPeriod_Object = MibTableColumn
cmmcaServiceIntPeriod = _CmmcaServiceIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 5),
    _CmmcaServiceIntPeriod_Type()
)
cmmcaServiceIntPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaServiceIntPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaServiceIntPeriod.setUnits("minutes")
_CmmcaRtRoutingDomain_Type = SnmpAdminString
_CmmcaRtRoutingDomain_Object = MibTableColumn
cmmcaRtRoutingDomain = _CmmcaRtRoutingDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 6),
    _CmmcaRtRoutingDomain_Type()
)
cmmcaRtRoutingDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtRoutingDomain.setStatus("current")
_CmmcaRtLogLevel_Type = CmmcaSeverityLevel
_CmmcaRtLogLevel_Object = MibTableColumn
cmmcaRtLogLevel = _CmmcaRtLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 7),
    _CmmcaRtLogLevel_Type()
)
cmmcaRtLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtLogLevel.setStatus("current")
_CmmcaRtTraceMask_Type = SnmpAdminString
_CmmcaRtTraceMask_Object = MibTableColumn
cmmcaRtTraceMask = _CmmcaRtTraceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 8),
    _CmmcaRtTraceMask_Type()
)
cmmcaRtTraceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtTraceMask.setStatus("current")
_CmmcaRtMessageThroughput_Type = Gauge32
_CmmcaRtMessageThroughput_Object = MibTableColumn
cmmcaRtMessageThroughput = _CmmcaRtMessageThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 9),
    _CmmcaRtMessageThroughput_Type()
)
cmmcaRtMessageThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtMessageThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtMessageThroughput.setUnits("messages per second")
_CmmcaRtUptime_Type = Counter64
_CmmcaRtUptime_Object = MibTableColumn
cmmcaRtUptime = _CmmcaRtUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 10),
    _CmmcaRtUptime_Type()
)
cmmcaRtUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtUptime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtUptime.setUnits("seconds")
_CmmcaRtMsgReceived_Type = Counter64
_CmmcaRtMsgReceived_Object = MibTableColumn
cmmcaRtMsgReceived = _CmmcaRtMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 11),
    _CmmcaRtMsgReceived_Type()
)
cmmcaRtMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtMsgReceived.setUnits("messages")
_CmmcaMaxThreadsAvailable_Type = Unsigned32
_CmmcaMaxThreadsAvailable_Object = MibTableColumn
cmmcaMaxThreadsAvailable = _CmmcaMaxThreadsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 12),
    _CmmcaMaxThreadsAvailable_Type()
)
cmmcaMaxThreadsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMaxThreadsAvailable.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMaxThreadsAvailable.setUnits("threads")
_CmmcaRtThreadsInUse_Type = Gauge32
_CmmcaRtThreadsInUse_Object = MibTableColumn
cmmcaRtThreadsInUse = _CmmcaRtThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 5, 1, 1, 13),
    _CmmcaRtThreadsInUse_Type()
)
cmmcaRtThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRtThreadsInUse.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRtThreadsInUse.setUnits("threads")
_CmmcaServiceInfo_ObjectIdentity = ObjectIdentity
cmmcaServiceInfo = _CmmcaServiceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6)
)
_CmmcaRmTable_Object = MibTable
cmmcaRmTable = _CmmcaRmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cmmcaRmTable.setStatus("current")
_CmmcaRmEntry_Object = MibTableRow
cmmcaRmEntry = _CmmcaRmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1)
)
cmmcaRmEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaRmEntry.setStatus("current")
_CmmcaRmRtAgentsLoggedIn_Type = Gauge32
_CmmcaRmRtAgentsLoggedIn_Object = MibTableColumn
cmmcaRmRtAgentsLoggedIn = _CmmcaRmRtAgentsLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 1),
    _CmmcaRmRtAgentsLoggedIn_Type()
)
cmmcaRmRtAgentsLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsLoggedIn.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsLoggedIn.setUnits("agents")
_CmmcaRmRtAgentsOnCalls_Type = Gauge32
_CmmcaRmRtAgentsOnCalls_Object = MibTableColumn
cmmcaRmRtAgentsOnCalls = _CmmcaRmRtAgentsOnCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 2),
    _CmmcaRmRtAgentsOnCalls_Type()
)
cmmcaRmRtAgentsOnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsOnCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsOnCalls.setUnits("agents")
_CmmcaRmRtAgentsReserved_Type = Gauge32
_CmmcaRmRtAgentsReserved_Object = MibTableColumn
cmmcaRmRtAgentsReserved = _CmmcaRmRtAgentsReserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 3),
    _CmmcaRmRtAgentsReserved_Type()
)
cmmcaRmRtAgentsReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsReserved.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsReserved.setUnits("agents")
_CmmcaRmRtAgentsWrapUp_Type = Gauge32
_CmmcaRmRtAgentsWrapUp_Object = MibTableColumn
cmmcaRmRtAgentsWrapUp = _CmmcaRmRtAgentsWrapUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 4),
    _CmmcaRmRtAgentsWrapUp_Type()
)
cmmcaRmRtAgentsWrapUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsWrapUp.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsWrapUp.setUnits("agents")
_CmmcaRmRtAgentsReady_Type = Gauge32
_CmmcaRmRtAgentsReady_Object = MibTableColumn
cmmcaRmRtAgentsReady = _CmmcaRmRtAgentsReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 5),
    _CmmcaRmRtAgentsReady_Type()
)
cmmcaRmRtAgentsReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsReady.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsReady.setUnits("agents")
_CmmcaRmRtAgentsNoQueue_Type = Gauge32
_CmmcaRmRtAgentsNoQueue_Object = MibTableColumn
cmmcaRmRtAgentsNoQueue = _CmmcaRmRtAgentsNoQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 6),
    _CmmcaRmRtAgentsNoQueue_Type()
)
cmmcaRmRtAgentsNoQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsNoQueue.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmRtAgentsNoQueue.setUnits("agents")
_CmmcaRmAggNumOffersAccept_Type = Counter64
_CmmcaRmAggNumOffersAccept_Object = MibTableColumn
cmmcaRmAggNumOffersAccept = _CmmcaRmAggNumOffersAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 7),
    _CmmcaRmAggNumOffersAccept_Type()
)
cmmcaRmAggNumOffersAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersAccept.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersAccept.setUnits("offers")
_CmmcaRmIntNumOffersAccept_Type = Gauge32
_CmmcaRmIntNumOffersAccept_Object = MibTableColumn
cmmcaRmIntNumOffersAccept = _CmmcaRmIntNumOffersAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 8),
    _CmmcaRmIntNumOffersAccept_Type()
)
cmmcaRmIntNumOffersAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersAccept.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersAccept.setUnits("offers")
_CmmcaRmAggNumOffersReject_Type = Counter64
_CmmcaRmAggNumOffersReject_Object = MibTableColumn
cmmcaRmAggNumOffersReject = _CmmcaRmAggNumOffersReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 9),
    _CmmcaRmAggNumOffersReject_Type()
)
cmmcaRmAggNumOffersReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersReject.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersReject.setUnits("offers")
_CmmcaRmIntNumOffersReject_Type = Gauge32
_CmmcaRmIntNumOffersReject_Object = MibTableColumn
cmmcaRmIntNumOffersReject = _CmmcaRmIntNumOffersReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 10),
    _CmmcaRmIntNumOffersReject_Type()
)
cmmcaRmIntNumOffersReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersReject.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersReject.setUnits("offers")
_CmmcaRmAggNumOffersTimedOut_Type = Counter64
_CmmcaRmAggNumOffersTimedOut_Object = MibTableColumn
cmmcaRmAggNumOffersTimedOut = _CmmcaRmAggNumOffersTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 11),
    _CmmcaRmAggNumOffersTimedOut_Type()
)
cmmcaRmAggNumOffersTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersTimedOut.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmAggNumOffersTimedOut.setUnits("offers")
_CmmcaRmIntNumOffersTimedOut_Type = Gauge32
_CmmcaRmIntNumOffersTimedOut_Object = MibTableColumn
cmmcaRmIntNumOffersTimedOut = _CmmcaRmIntNumOffersTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 1, 1, 12),
    _CmmcaRmIntNumOffersTimedOut_Type()
)
cmmcaRmIntNumOffersTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersTimedOut.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRmIntNumOffersTimedOut.setUnits("offers")
_CmmcaCmTable_Object = MibTable
cmmcaCmTable = _CmmcaCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cmmcaCmTable.setStatus("current")
_CmmcaCmEntry_Object = MibTableRow
cmmcaCmEntry = _CmmcaCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1)
)
cmmcaCmEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaCmEntry.setStatus("current")
_CmmcaCmRtNumActiveCalls_Type = Gauge32
_CmmcaCmRtNumActiveCalls_Object = MibTableColumn
cmmcaCmRtNumActiveCalls = _CmmcaCmRtNumActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 1),
    _CmmcaCmRtNumActiveCalls_Type()
)
cmmcaCmRtNumActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumActiveCalls.setUnits("calls")
_CmmcaCmRtNumCallTrying_Type = Gauge32
_CmmcaCmRtNumCallTrying_Object = MibTableColumn
cmmcaCmRtNumCallTrying = _CmmcaCmRtNumCallTrying_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 2),
    _CmmcaCmRtNumCallTrying_Type()
)
cmmcaCmRtNumCallTrying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTrying.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTrying.setUnits("calls")
_CmmcaCmRtNumCallRingBack_Type = Gauge32
_CmmcaCmRtNumCallRingBack_Object = MibTableColumn
cmmcaCmRtNumCallRingBack = _CmmcaCmRtNumCallRingBack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 3),
    _CmmcaCmRtNumCallRingBack_Type()
)
cmmcaCmRtNumCallRingBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallRingBack.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallRingBack.setUnits("calls")
_CmmcaCmRtNumCallConnecting_Type = Gauge32
_CmmcaCmRtNumCallConnecting_Object = MibTableColumn
cmmcaCmRtNumCallConnecting = _CmmcaCmRtNumCallConnecting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 4),
    _CmmcaCmRtNumCallConnecting_Type()
)
cmmcaCmRtNumCallConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallConnecting.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallConnecting.setUnits("calls")
_CmmcaCmRtNumCallConnected_Type = Gauge32
_CmmcaCmRtNumCallConnected_Object = MibTableColumn
cmmcaCmRtNumCallConnected = _CmmcaCmRtNumCallConnected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 5),
    _CmmcaCmRtNumCallConnected_Type()
)
cmmcaCmRtNumCallConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallConnected.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallConnected.setUnits("calls")
_CmmcaCmRtNumCallInitial_Type = Gauge32
_CmmcaCmRtNumCallInitial_Object = MibTableColumn
cmmcaCmRtNumCallInitial = _CmmcaCmRtNumCallInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 6),
    _CmmcaCmRtNumCallInitial_Type()
)
cmmcaCmRtNumCallInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallInitial.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallInitial.setUnits("calls")
_CmmcaCmAggNumCallArrivals_Type = Counter64
_CmmcaCmAggNumCallArrivals_Object = MibTableColumn
cmmcaCmAggNumCallArrivals = _CmmcaCmAggNumCallArrivals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 7),
    _CmmcaCmAggNumCallArrivals_Type()
)
cmmcaCmAggNumCallArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggNumCallArrivals.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggNumCallArrivals.setUnits("calls")
_CmmcaCmIntNumCallArrivals_Type = Gauge32
_CmmcaCmIntNumCallArrivals_Object = MibTableColumn
cmmcaCmIntNumCallArrivals = _CmmcaCmIntNumCallArrivals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 8),
    _CmmcaCmIntNumCallArrivals_Type()
)
cmmcaCmIntNumCallArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntNumCallArrivals.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntNumCallArrivals.setUnits("calls")
_CmmcaCmRtNumCallRejecting_Type = Gauge32
_CmmcaCmRtNumCallRejecting_Object = MibTableColumn
cmmcaCmRtNumCallRejecting = _CmmcaCmRtNumCallRejecting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 9),
    _CmmcaCmRtNumCallRejecting_Type()
)
cmmcaCmRtNumCallRejecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallRejecting.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallRejecting.setUnits("calls")
_CmmcaCmRtNumCallTransferring_Type = Gauge32
_CmmcaCmRtNumCallTransferring_Object = MibTableColumn
cmmcaCmRtNumCallTransferring = _CmmcaCmRtNumCallTransferring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 10),
    _CmmcaCmRtNumCallTransferring_Type()
)
cmmcaCmRtNumCallTransferring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTransferring.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTransferring.setUnits("calls")
_CmmcaCmRtNumCallTerminating_Type = Gauge32
_CmmcaCmRtNumCallTerminating_Object = MibTableColumn
cmmcaCmRtNumCallTerminating = _CmmcaCmRtNumCallTerminating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 11),
    _CmmcaCmRtNumCallTerminating_Type()
)
cmmcaCmRtNumCallTerminating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTerminating.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmRtNumCallTerminating.setUnits("calls")
_CmmcaCmAggAvgCallDurationTime_Type = Gauge32
_CmmcaCmAggAvgCallDurationTime_Object = MibTableColumn
cmmcaCmAggAvgCallDurationTime = _CmmcaCmAggAvgCallDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 12),
    _CmmcaCmAggAvgCallDurationTime_Type()
)
cmmcaCmAggAvgCallDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallDurationTime.setUnits("seconds")
_CmmcaCmIntAvgCallDurationTime_Type = Gauge32
_CmmcaCmIntAvgCallDurationTime_Object = MibTableColumn
cmmcaCmIntAvgCallDurationTime = _CmmcaCmIntAvgCallDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 13),
    _CmmcaCmIntAvgCallDurationTime_Type()
)
cmmcaCmIntAvgCallDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallDurationTime.setUnits("seconds")
_CmmcaCmAggMaxCallDurationTime_Type = Integer32
_CmmcaCmAggMaxCallDurationTime_Object = MibTableColumn
cmmcaCmAggMaxCallDurationTime = _CmmcaCmAggMaxCallDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 14),
    _CmmcaCmAggMaxCallDurationTime_Type()
)
cmmcaCmAggMaxCallDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallDurationTime.setUnits("seconds")
_CmmcaCmIntMaxCallDurationTime_Type = Integer32
_CmmcaCmIntMaxCallDurationTime_Object = MibTableColumn
cmmcaCmIntMaxCallDurationTime = _CmmcaCmIntMaxCallDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 15),
    _CmmcaCmIntMaxCallDurationTime_Type()
)
cmmcaCmIntMaxCallDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallDurationTime.setUnits("seconds")
_CmmcaCmAggMaxCallDurationTimeDt_Type = DateAndTime
_CmmcaCmAggMaxCallDurationTimeDt_Object = MibTableColumn
cmmcaCmAggMaxCallDurationTimeDt = _CmmcaCmAggMaxCallDurationTimeDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 16),
    _CmmcaCmAggMaxCallDurationTimeDt_Type()
)
cmmcaCmAggMaxCallDurationTimeDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallDurationTimeDt.setStatus("current")
_CmmcaCmIntMaxCallDurationTimeDt_Type = DateAndTime
_CmmcaCmIntMaxCallDurationTimeDt_Object = MibTableColumn
cmmcaCmIntMaxCallDurationTimeDt = _CmmcaCmIntMaxCallDurationTimeDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 17),
    _CmmcaCmIntMaxCallDurationTimeDt_Type()
)
cmmcaCmIntMaxCallDurationTimeDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallDurationTimeDt.setStatus("current")
_CmmcaCmAggAvgCallInQueueTime_Type = Gauge32
_CmmcaCmAggAvgCallInQueueTime_Object = MibTableColumn
cmmcaCmAggAvgCallInQueueTime = _CmmcaCmAggAvgCallInQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 18),
    _CmmcaCmAggAvgCallInQueueTime_Type()
)
cmmcaCmAggAvgCallInQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallInQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallInQueueTime.setUnits("seconds")
_CmmcaCmIntAvgCallInQueueTime_Type = Gauge32
_CmmcaCmIntAvgCallInQueueTime_Object = MibTableColumn
cmmcaCmIntAvgCallInQueueTime = _CmmcaCmIntAvgCallInQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 19),
    _CmmcaCmIntAvgCallInQueueTime_Type()
)
cmmcaCmIntAvgCallInQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallInQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallInQueueTime.setUnits("seconds")
_CmmcaCmAggMaxCallInQueueTime_Type = Integer32
_CmmcaCmAggMaxCallInQueueTime_Object = MibTableColumn
cmmcaCmAggMaxCallInQueueTime = _CmmcaCmAggMaxCallInQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 20),
    _CmmcaCmAggMaxCallInQueueTime_Type()
)
cmmcaCmAggMaxCallInQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallInQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallInQueueTime.setUnits("seconds")
_CmmcaCmIntMaxCallInQueueTime_Type = Integer32
_CmmcaCmIntMaxCallInQueueTime_Object = MibTableColumn
cmmcaCmIntMaxCallInQueueTime = _CmmcaCmIntMaxCallInQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 21),
    _CmmcaCmIntMaxCallInQueueTime_Type()
)
cmmcaCmIntMaxCallInQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallInQueueTime.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallInQueueTime.setUnits("seconds")
_CmmcaCmAggMaxCallInQueueTimeDt_Type = DateAndTime
_CmmcaCmAggMaxCallInQueueTimeDt_Object = MibTableColumn
cmmcaCmAggMaxCallInQueueTimeDt = _CmmcaCmAggMaxCallInQueueTimeDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 22),
    _CmmcaCmAggMaxCallInQueueTimeDt_Type()
)
cmmcaCmAggMaxCallInQueueTimeDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallInQueueTimeDt.setStatus("current")
_CmmcaCmIntMaxCallInQueueTimeDt_Type = DateAndTime
_CmmcaCmIntMaxCallInQueueTimeDt_Object = MibTableColumn
cmmcaCmIntMaxCallInQueueTimeDt = _CmmcaCmIntMaxCallInQueueTimeDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 23),
    _CmmcaCmIntMaxCallInQueueTimeDt_Type()
)
cmmcaCmIntMaxCallInQueueTimeDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntMaxCallInQueueTimeDt.setStatus("current")
_CmmcaCmAggAvgCallArrivalRate_Type = Gauge32
_CmmcaCmAggAvgCallArrivalRate_Object = MibTableColumn
cmmcaCmAggAvgCallArrivalRate = _CmmcaCmAggAvgCallArrivalRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 24),
    _CmmcaCmAggAvgCallArrivalRate_Type()
)
cmmcaCmAggAvgCallArrivalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallArrivalRate.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggAvgCallArrivalRate.setUnits("calls per minute")
_CmmcaCmAggMaxCallArrivalRate_Type = Integer32
_CmmcaCmAggMaxCallArrivalRate_Object = MibTableColumn
cmmcaCmAggMaxCallArrivalRate = _CmmcaCmAggMaxCallArrivalRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 25),
    _CmmcaCmAggMaxCallArrivalRate_Type()
)
cmmcaCmAggMaxCallArrivalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallArrivalRate.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallArrivalRate.setUnits("calls per minute")
_CmmcaCmAggMaxCallArrivalRateDt_Type = DateAndTime
_CmmcaCmAggMaxCallArrivalRateDt_Object = MibTableColumn
cmmcaCmAggMaxCallArrivalRateDt = _CmmcaCmAggMaxCallArrivalRateDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 26),
    _CmmcaCmAggMaxCallArrivalRateDt_Type()
)
cmmcaCmAggMaxCallArrivalRateDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmAggMaxCallArrivalRateDt.setStatus("current")
_CmmcaCmIntAvgCallArrivalRate_Type = Gauge32
_CmmcaCmIntAvgCallArrivalRate_Object = MibTableColumn
cmmcaCmIntAvgCallArrivalRate = _CmmcaCmIntAvgCallArrivalRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 2, 1, 27),
    _CmmcaCmIntAvgCallArrivalRate_Type()
)
cmmcaCmIntAvgCallArrivalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallArrivalRate.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaCmIntAvgCallArrivalRate.setUnits("calls per minute")
_CmmcaRdaTable_Object = MibTable
cmmcaRdaTable = _CmmcaRdaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cmmcaRdaTable.setStatus("current")
_CmmcaRdaEntry_Object = MibTableRow
cmmcaRdaEntry = _CmmcaRdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1)
)
cmmcaRdaEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaRdaEntry.setStatus("current")
_CmmcaRdaAggNumMsgProc_Type = Counter64
_CmmcaRdaAggNumMsgProc_Object = MibTableColumn
cmmcaRdaAggNumMsgProc = _CmmcaRdaAggNumMsgProc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 1),
    _CmmcaRdaAggNumMsgProc_Type()
)
cmmcaRdaAggNumMsgProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumMsgProc.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumMsgProc.setUnits("messages")
_CmmcaRdaIntNumMsgProc_Type = CounterBasedGauge64
_CmmcaRdaIntNumMsgProc_Object = MibTableColumn
cmmcaRdaIntNumMsgProc = _CmmcaRdaIntNumMsgProc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 2),
    _CmmcaRdaIntNumMsgProc_Type()
)
cmmcaRdaIntNumMsgProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumMsgProc.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumMsgProc.setUnits("messages")
_CmmcaRdaAggNumSuccessPresenceNotifications_Type = Counter64
_CmmcaRdaAggNumSuccessPresenceNotifications_Object = MibTableColumn
cmmcaRdaAggNumSuccessPresenceNotifications = _CmmcaRdaAggNumSuccessPresenceNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 3),
    _CmmcaRdaAggNumSuccessPresenceNotifications_Type()
)
cmmcaRdaAggNumSuccessPresenceNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumSuccessPresenceNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumSuccessPresenceNotifications.setUnits("notifications")
_CmmcaRdaIntNumSuccessPresenceNotifications_Type = CounterBasedGauge64
_CmmcaRdaIntNumSuccessPresenceNotifications_Object = MibTableColumn
cmmcaRdaIntNumSuccessPresenceNotifications = _CmmcaRdaIntNumSuccessPresenceNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 4),
    _CmmcaRdaIntNumSuccessPresenceNotifications_Type()
)
cmmcaRdaIntNumSuccessPresenceNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumSuccessPresenceNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumSuccessPresenceNotifications.setUnits("notifications")
_CmmcaRdaRtNumActiveClients_Type = Gauge32
_CmmcaRdaRtNumActiveClients_Object = MibTableColumn
cmmcaRdaRtNumActiveClients = _CmmcaRdaRtNumActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 5),
    _CmmcaRdaRtNumActiveClients_Type()
)
cmmcaRdaRtNumActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumActiveClients.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumActiveClients.setUnits("clients")
_CmmcaRdaRtNumOutStandingOfferTasks_Type = Gauge32
_CmmcaRdaRtNumOutStandingOfferTasks_Object = MibTableColumn
cmmcaRdaRtNumOutStandingOfferTasks = _CmmcaRdaRtNumOutStandingOfferTasks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 6),
    _CmmcaRdaRtNumOutStandingOfferTasks_Type()
)
cmmcaRdaRtNumOutStandingOfferTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumOutStandingOfferTasks.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumOutStandingOfferTasks.setUnits("tasks")
_CmmcaRdaAggNumUnSuccessPresenceNotifications_Type = Counter64
_CmmcaRdaAggNumUnSuccessPresenceNotifications_Object = MibTableColumn
cmmcaRdaAggNumUnSuccessPresenceNotifications = _CmmcaRdaAggNumUnSuccessPresenceNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 7),
    _CmmcaRdaAggNumUnSuccessPresenceNotifications_Type()
)
cmmcaRdaAggNumUnSuccessPresenceNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumUnSuccessPresenceNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaAggNumUnSuccessPresenceNotifications.setUnits("notifications")
_CmmcaRdaIntNumUnSuccessPresenceNotifications_Type = CounterBasedGauge64
_CmmcaRdaIntNumUnSuccessPresenceNotifications_Object = MibTableColumn
cmmcaRdaIntNumUnSuccessPresenceNotifications = _CmmcaRdaIntNumUnSuccessPresenceNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 8),
    _CmmcaRdaIntNumUnSuccessPresenceNotifications_Type()
)
cmmcaRdaIntNumUnSuccessPresenceNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumUnSuccessPresenceNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaIntNumUnSuccessPresenceNotifications.setUnits("notifications")
_CmmcaRdaRtNumInactiveClients_Type = Gauge32
_CmmcaRdaRtNumInactiveClients_Object = MibTableColumn
cmmcaRdaRtNumInactiveClients = _CmmcaRdaRtNumInactiveClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 3, 1, 9),
    _CmmcaRdaRtNumInactiveClients_Type()
)
cmmcaRdaRtNumInactiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumInactiveClients.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRdaRtNumInactiveClients.setUnits("clients")
_CmmcaBreTable_Object = MibTable
cmmcaBreTable = _CmmcaBreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cmmcaBreTable.setStatus("current")
_CmmcaBreEntry_Object = MibTableRow
cmmcaBreEntry = _CmmcaBreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1)
)
cmmcaBreEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaBreEntry.setStatus("current")
_CmmcaBreAggLoadedScripts_Type = Counter32
_CmmcaBreAggLoadedScripts_Object = MibTableColumn
cmmcaBreAggLoadedScripts = _CmmcaBreAggLoadedScripts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 1),
    _CmmcaBreAggLoadedScripts_Type()
)
cmmcaBreAggLoadedScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggLoadedScripts.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggLoadedScripts.setUnits("scripts")
_CmmcaBreAggDistinctScripts_Type = Counter32
_CmmcaBreAggDistinctScripts_Object = MibTableColumn
cmmcaBreAggDistinctScripts = _CmmcaBreAggDistinctScripts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 2),
    _CmmcaBreAggDistinctScripts_Type()
)
cmmcaBreAggDistinctScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggDistinctScripts.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggDistinctScripts.setUnits("scripts")
_CmmcaBreRtActiveScripts_Type = Gauge32
_CmmcaBreRtActiveScripts_Object = MibTableColumn
cmmcaBreRtActiveScripts = _CmmcaBreRtActiveScripts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 3),
    _CmmcaBreRtActiveScripts_Type()
)
cmmcaBreRtActiveScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreRtActiveScripts.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreRtActiveScripts.setUnits("scripts")
_CmmcaBreRtCurrentInstances_Type = Gauge32
_CmmcaBreRtCurrentInstances_Object = MibTableColumn
cmmcaBreRtCurrentInstances = _CmmcaBreRtCurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 4),
    _CmmcaBreRtCurrentInstances_Type()
)
cmmcaBreRtCurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreRtCurrentInstances.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreRtCurrentInstances.setUnits("instances")
_CmmcaBreAggMaxConcurrentInstances_Type = Counter32
_CmmcaBreAggMaxConcurrentInstances_Object = MibTableColumn
cmmcaBreAggMaxConcurrentInstances = _CmmcaBreAggMaxConcurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 5),
    _CmmcaBreAggMaxConcurrentInstances_Type()
)
cmmcaBreAggMaxConcurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggMaxConcurrentInstances.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggMaxConcurrentInstances.setUnits("instances")
_CmmcaBreIntMaxConcurrentInstances_Type = Gauge32
_CmmcaBreIntMaxConcurrentInstances_Object = MibTableColumn
cmmcaBreIntMaxConcurrentInstances = _CmmcaBreIntMaxConcurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 6),
    _CmmcaBreIntMaxConcurrentInstances_Type()
)
cmmcaBreIntMaxConcurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntMaxConcurrentInstances.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntMaxConcurrentInstances.setUnits("instances")
_CmmcaBreAggMaxConcurrentInstancesDt_Type = DateAndTime
_CmmcaBreAggMaxConcurrentInstancesDt_Object = MibTableColumn
cmmcaBreAggMaxConcurrentInstancesDt = _CmmcaBreAggMaxConcurrentInstancesDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 7),
    _CmmcaBreAggMaxConcurrentInstancesDt_Type()
)
cmmcaBreAggMaxConcurrentInstancesDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggMaxConcurrentInstancesDt.setStatus("current")
_CmmcaBreIntMaxConcurrentInstancesDt_Type = DateAndTime
_CmmcaBreIntMaxConcurrentInstancesDt_Object = MibTableColumn
cmmcaBreIntMaxConcurrentInstancesDt = _CmmcaBreIntMaxConcurrentInstancesDt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 8),
    _CmmcaBreIntMaxConcurrentInstancesDt_Type()
)
cmmcaBreIntMaxConcurrentInstancesDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntMaxConcurrentInstancesDt.setStatus("current")
_CmmcaBreAggAvgConcurrentInstances_Type = Gauge32
_CmmcaBreAggAvgConcurrentInstances_Object = MibTableColumn
cmmcaBreAggAvgConcurrentInstances = _CmmcaBreAggAvgConcurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 9),
    _CmmcaBreAggAvgConcurrentInstances_Type()
)
cmmcaBreAggAvgConcurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggAvgConcurrentInstances.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggAvgConcurrentInstances.setUnits("instances")
_CmmcaBreIntAvgConcurrentInstances_Type = Gauge32
_CmmcaBreIntAvgConcurrentInstances_Object = MibTableColumn
cmmcaBreIntAvgConcurrentInstances = _CmmcaBreIntAvgConcurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 10),
    _CmmcaBreIntAvgConcurrentInstances_Type()
)
cmmcaBreIntAvgConcurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntAvgConcurrentInstances.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntAvgConcurrentInstances.setUnits("instances")
_CmmcaBreAggTotalInstanceInitiations_Type = Counter64
_CmmcaBreAggTotalInstanceInitiations_Object = MibTableColumn
cmmcaBreAggTotalInstanceInitiations = _CmmcaBreAggTotalInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 11),
    _CmmcaBreAggTotalInstanceInitiations_Type()
)
cmmcaBreAggTotalInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalInstanceInitiations.setUnits("initiations")
_CmmcaBreIntTotalInstanceInitiations_Type = CounterBasedGauge64
_CmmcaBreIntTotalInstanceInitiations_Object = MibTableColumn
cmmcaBreIntTotalInstanceInitiations = _CmmcaBreIntTotalInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 12),
    _CmmcaBreIntTotalInstanceInitiations_Type()
)
cmmcaBreIntTotalInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalInstanceInitiations.setUnits("initiations")
_CmmcaBreAggTotalContactInstanceInitiations_Type = Counter64
_CmmcaBreAggTotalContactInstanceInitiations_Object = MibTableColumn
cmmcaBreAggTotalContactInstanceInitiations = _CmmcaBreAggTotalContactInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 13),
    _CmmcaBreAggTotalContactInstanceInitiations_Type()
)
cmmcaBreAggTotalContactInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalContactInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalContactInstanceInitiations.setUnits("initiations")
_CmmcaBreIntTotalContactInstanceInitiations_Type = CounterBasedGauge64
_CmmcaBreIntTotalContactInstanceInitiations_Object = MibTableColumn
cmmcaBreIntTotalContactInstanceInitiations = _CmmcaBreIntTotalContactInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 14),
    _CmmcaBreIntTotalContactInstanceInitiations_Type()
)
cmmcaBreIntTotalContactInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalContactInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalContactInstanceInitiations.setUnits("initiations")
_CmmcaBreAggTotalResourceInstanceInitiations_Type = Counter64
_CmmcaBreAggTotalResourceInstanceInitiations_Object = MibTableColumn
cmmcaBreAggTotalResourceInstanceInitiations = _CmmcaBreAggTotalResourceInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 15),
    _CmmcaBreAggTotalResourceInstanceInitiations_Type()
)
cmmcaBreAggTotalResourceInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalResourceInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalResourceInstanceInitiations.setUnits("initiations")
_CmmcaBreIntTotalResourceInstanceInitiations_Type = CounterBasedGauge64
_CmmcaBreIntTotalResourceInstanceInitiations_Object = MibTableColumn
cmmcaBreIntTotalResourceInstanceInitiations = _CmmcaBreIntTotalResourceInstanceInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 16),
    _CmmcaBreIntTotalResourceInstanceInitiations_Type()
)
cmmcaBreIntTotalResourceInstanceInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalResourceInstanceInitiations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalResourceInstanceInitiations.setUnits("initiations")
_CmmcaBreAggTotalInstanceTerminations_Type = Counter64
_CmmcaBreAggTotalInstanceTerminations_Object = MibTableColumn
cmmcaBreAggTotalInstanceTerminations = _CmmcaBreAggTotalInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 17),
    _CmmcaBreAggTotalInstanceTerminations_Type()
)
cmmcaBreAggTotalInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalInstanceTerminations.setUnits("terminations")
_CmmcaBreIntTotalInstanceTerminations_Type = CounterBasedGauge64
_CmmcaBreIntTotalInstanceTerminations_Object = MibTableColumn
cmmcaBreIntTotalInstanceTerminations = _CmmcaBreIntTotalInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 18),
    _CmmcaBreIntTotalInstanceTerminations_Type()
)
cmmcaBreIntTotalInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalInstanceTerminations.setUnits("terminations")
_CmmcaBreAggTotalContactInstanceTerminations_Type = Counter64
_CmmcaBreAggTotalContactInstanceTerminations_Object = MibTableColumn
cmmcaBreAggTotalContactInstanceTerminations = _CmmcaBreAggTotalContactInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 19),
    _CmmcaBreAggTotalContactInstanceTerminations_Type()
)
cmmcaBreAggTotalContactInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalContactInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalContactInstanceTerminations.setUnits("terminations")
_CmmcaBreIntTotalContactInstanceTerminations_Type = CounterBasedGauge64
_CmmcaBreIntTotalContactInstanceTerminations_Object = MibTableColumn
cmmcaBreIntTotalContactInstanceTerminations = _CmmcaBreIntTotalContactInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 20),
    _CmmcaBreIntTotalContactInstanceTerminations_Type()
)
cmmcaBreIntTotalContactInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalContactInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalContactInstanceTerminations.setUnits("terminations")
_CmmcaBreAggTotalResourceInstanceTerminations_Type = Counter64
_CmmcaBreAggTotalResourceInstanceTerminations_Object = MibTableColumn
cmmcaBreAggTotalResourceInstanceTerminations = _CmmcaBreAggTotalResourceInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 21),
    _CmmcaBreAggTotalResourceInstanceTerminations_Type()
)
cmmcaBreAggTotalResourceInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalResourceInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalResourceInstanceTerminations.setUnits("terminations")
_CmmcaBreIntTotalResourceInstanceTerminations_Type = CounterBasedGauge64
_CmmcaBreIntTotalResourceInstanceTerminations_Object = MibTableColumn
cmmcaBreIntTotalResourceInstanceTerminations = _CmmcaBreIntTotalResourceInstanceTerminations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 22),
    _CmmcaBreIntTotalResourceInstanceTerminations_Type()
)
cmmcaBreIntTotalResourceInstanceTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalResourceInstanceTerminations.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalResourceInstanceTerminations.setUnits("terminations")
_CmmcaBreAggTotalAbnormalEndings_Type = Counter64
_CmmcaBreAggTotalAbnormalEndings_Object = MibTableColumn
cmmcaBreAggTotalAbnormalEndings = _CmmcaBreAggTotalAbnormalEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 23),
    _CmmcaBreAggTotalAbnormalEndings_Type()
)
cmmcaBreAggTotalAbnormalEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalEndings.setUnits("endings")
_CmmcaBreIntTotalAbnormalEndings_Type = CounterBasedGauge64
_CmmcaBreIntTotalAbnormalEndings_Object = MibTableColumn
cmmcaBreIntTotalAbnormalEndings = _CmmcaBreIntTotalAbnormalEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 24),
    _CmmcaBreIntTotalAbnormalEndings_Type()
)
cmmcaBreIntTotalAbnormalEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalEndings.setUnits("endings")
_CmmcaBreAggTotalAbnormalContactEndings_Type = Counter64
_CmmcaBreAggTotalAbnormalContactEndings_Object = MibTableColumn
cmmcaBreAggTotalAbnormalContactEndings = _CmmcaBreAggTotalAbnormalContactEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 25),
    _CmmcaBreAggTotalAbnormalContactEndings_Type()
)
cmmcaBreAggTotalAbnormalContactEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalContactEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalContactEndings.setUnits("endings")
_CmmcaBreIntTotalAbnormalContactEndings_Type = CounterBasedGauge64
_CmmcaBreIntTotalAbnormalContactEndings_Object = MibTableColumn
cmmcaBreIntTotalAbnormalContactEndings = _CmmcaBreIntTotalAbnormalContactEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 26),
    _CmmcaBreIntTotalAbnormalContactEndings_Type()
)
cmmcaBreIntTotalAbnormalContactEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalContactEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalContactEndings.setUnits("endings")
_CmmcaBreAggTotalAbnormalResourceEndings_Type = Counter64
_CmmcaBreAggTotalAbnormalResourceEndings_Object = MibTableColumn
cmmcaBreAggTotalAbnormalResourceEndings = _CmmcaBreAggTotalAbnormalResourceEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 27),
    _CmmcaBreAggTotalAbnormalResourceEndings_Type()
)
cmmcaBreAggTotalAbnormalResourceEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalResourceEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreAggTotalAbnormalResourceEndings.setUnits("endings")
_CmmcaBreIntTotalAbnormalResourceEndings_Type = CounterBasedGauge64
_CmmcaBreIntTotalAbnormalResourceEndings_Object = MibTableColumn
cmmcaBreIntTotalAbnormalResourceEndings = _CmmcaBreIntTotalAbnormalResourceEndings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 4, 1, 28),
    _CmmcaBreIntTotalAbnormalResourceEndings_Type()
)
cmmcaBreIntTotalAbnormalResourceEndings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalResourceEndings.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaBreIntTotalAbnormalResourceEndings.setUnits("endings")
_CmmcaWaTable_Object = MibTable
cmmcaWaTable = _CmmcaWaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cmmcaWaTable.setStatus("current")
_CmmcaWaEntry_Object = MibTableRow
cmmcaWaEntry = _CmmcaWaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1)
)
cmmcaWaEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaWaEntry.setStatus("current")
_CmmcaWaRtAssignmentQueCount_Type = Gauge32
_CmmcaWaRtAssignmentQueCount_Object = MibTableColumn
cmmcaWaRtAssignmentQueCount = _CmmcaWaRtAssignmentQueCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 1),
    _CmmcaWaRtAssignmentQueCount_Type()
)
cmmcaWaRtAssignmentQueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtAssignmentQueCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtAssignmentQueCount.setUnits("none")
_CmmcaWaRtAttributeDefCount_Type = Gauge32
_CmmcaWaRtAttributeDefCount_Object = MibTableColumn
cmmcaWaRtAttributeDefCount = _CmmcaWaRtAttributeDefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 2),
    _CmmcaWaRtAttributeDefCount_Type()
)
cmmcaWaRtAttributeDefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeDefCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeDefCount.setUnits("none")
_CmmcaWaRtSelectionStrategyCount_Type = Gauge32
_CmmcaWaRtSelectionStrategyCount_Object = MibTableColumn
cmmcaWaRtSelectionStrategyCount = _CmmcaWaRtSelectionStrategyCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 3),
    _CmmcaWaRtSelectionStrategyCount_Type()
)
cmmcaWaRtSelectionStrategyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtSelectionStrategyCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtSelectionStrategyCount.setUnits("none")
_CmmcaWaRtSkillCount_Type = Gauge32
_CmmcaWaRtSkillCount_Object = MibTableColumn
cmmcaWaRtSkillCount = _CmmcaWaRtSkillCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 4),
    _CmmcaWaRtSkillCount_Type()
)
cmmcaWaRtSkillCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtSkillCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtSkillCount.setUnits("none")
_CmmcaWaAggTotalConfigErrors_Type = Counter64
_CmmcaWaAggTotalConfigErrors_Object = MibTableColumn
cmmcaWaAggTotalConfigErrors = _CmmcaWaAggTotalConfigErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 5),
    _CmmcaWaAggTotalConfigErrors_Type()
)
cmmcaWaAggTotalConfigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggTotalConfigErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggTotalConfigErrors.setUnits("none")
_CmmcaWaAggCancelResourceRequestReceived_Type = Counter64
_CmmcaWaAggCancelResourceRequestReceived_Object = MibTableColumn
cmmcaWaAggCancelResourceRequestReceived = _CmmcaWaAggCancelResourceRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 6),
    _CmmcaWaAggCancelResourceRequestReceived_Type()
)
cmmcaWaAggCancelResourceRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelResourceRequestReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelResourceRequestReceived.setUnits("messages")
_CmmcaWaAggResourceRequestReceived_Type = Counter64
_CmmcaWaAggResourceRequestReceived_Object = MibTableColumn
cmmcaWaAggResourceRequestReceived = _CmmcaWaAggResourceRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 7),
    _CmmcaWaAggResourceRequestReceived_Type()
)
cmmcaWaAggResourceRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceRequestReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceRequestReceived.setUnits("messages")
_CmmcaWaAggResourceResponseSent_Type = Counter64
_CmmcaWaAggResourceResponseSent_Object = MibTableColumn
cmmcaWaAggResourceResponseSent = _CmmcaWaAggResourceResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 8),
    _CmmcaWaAggResourceResponseSent_Type()
)
cmmcaWaAggResourceResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceResponseSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceResponseSent.setUnits("messages")
_CmmcaWaAggCancelWorkRequestReceived_Type = Counter64
_CmmcaWaAggCancelWorkRequestReceived_Object = MibTableColumn
cmmcaWaAggCancelWorkRequestReceived = _CmmcaWaAggCancelWorkRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 9),
    _CmmcaWaAggCancelWorkRequestReceived_Type()
)
cmmcaWaAggCancelWorkRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelWorkRequestReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelWorkRequestReceived.setUnits("messages")
_CmmcaWaAggOfferTaskAcceptedSent_Type = Counter64
_CmmcaWaAggOfferTaskAcceptedSent_Object = MibTableColumn
cmmcaWaAggOfferTaskAcceptedSent = _CmmcaWaAggOfferTaskAcceptedSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 10),
    _CmmcaWaAggOfferTaskAcceptedSent_Type()
)
cmmcaWaAggOfferTaskAcceptedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskAcceptedSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskAcceptedSent.setUnits("messages")
_CmmcaWaAggOfferTaskCancelledSent_Type = Counter64
_CmmcaWaAggOfferTaskCancelledSent_Object = MibTableColumn
cmmcaWaAggOfferTaskCancelledSent = _CmmcaWaAggOfferTaskCancelledSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 11),
    _CmmcaWaAggOfferTaskCancelledSent_Type()
)
cmmcaWaAggOfferTaskCancelledSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskCancelledSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskCancelledSent.setUnits("messages")
_CmmcaWaAggOfferTaskResponseReceived_Type = Counter64
_CmmcaWaAggOfferTaskResponseReceived_Object = MibTableColumn
cmmcaWaAggOfferTaskResponseReceived = _CmmcaWaAggOfferTaskResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 12),
    _CmmcaWaAggOfferTaskResponseReceived_Type()
)
cmmcaWaAggOfferTaskResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskResponseReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskResponseReceived.setUnits("messages")
_CmmcaWaAggOfferTaskSent_Type = Counter64
_CmmcaWaAggOfferTaskSent_Object = MibTableColumn
cmmcaWaAggOfferTaskSent = _CmmcaWaAggOfferTaskSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 13),
    _CmmcaWaAggOfferTaskSent_Type()
)
cmmcaWaAggOfferTaskSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggOfferTaskSent.setUnits("messages")
_CmmcaWaAggResyncResourceResponseAckSent_Type = Counter64
_CmmcaWaAggResyncResourceResponseAckSent_Object = MibTableColumn
cmmcaWaAggResyncResourceResponseAckSent = _CmmcaWaAggResyncResourceResponseAckSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 14),
    _CmmcaWaAggResyncResourceResponseAckSent_Type()
)
cmmcaWaAggResyncResourceResponseAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceResponseAckSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceResponseAckSent.setUnits("messages")
_CmmcaWaAggResyncResourceResponseReceived_Type = Counter64
_CmmcaWaAggResyncResourceResponseReceived_Object = MibTableColumn
cmmcaWaAggResyncResourceResponseReceived = _CmmcaWaAggResyncResourceResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 15),
    _CmmcaWaAggResyncResourceResponseReceived_Type()
)
cmmcaWaAggResyncResourceResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceResponseReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceResponseReceived.setUnits("messages")
_CmmcaWaAggResyncResourceSent_Type = Counter64
_CmmcaWaAggResyncResourceSent_Object = MibTableColumn
cmmcaWaAggResyncResourceSent = _CmmcaWaAggResyncResourceSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 16),
    _CmmcaWaAggResyncResourceSent_Type()
)
cmmcaWaAggResyncResourceSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResyncResourceSent.setUnits("messages")
_CmmcaWaAggWorkRequestReceived_Type = Counter64
_CmmcaWaAggWorkRequestReceived_Object = MibTableColumn
cmmcaWaAggWorkRequestReceived = _CmmcaWaAggWorkRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 17),
    _CmmcaWaAggWorkRequestReceived_Type()
)
cmmcaWaAggWorkRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggWorkRequestReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggWorkRequestReceived.setUnits("messages")
_CmmcaWaAggQueueEventSent_Type = Counter64
_CmmcaWaAggQueueEventSent_Object = MibTableColumn
cmmcaWaAggQueueEventSent = _CmmcaWaAggQueueEventSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 18),
    _CmmcaWaAggQueueEventSent_Type()
)
cmmcaWaAggQueueEventSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggQueueEventSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggQueueEventSent.setUnits("messages")
_CmmcaWaAggWorkRequestCanceledSent_Type = Counter64
_CmmcaWaAggWorkRequestCanceledSent_Object = MibTableColumn
cmmcaWaAggWorkRequestCanceledSent = _CmmcaWaAggWorkRequestCanceledSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 19),
    _CmmcaWaAggWorkRequestCanceledSent_Type()
)
cmmcaWaAggWorkRequestCanceledSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggWorkRequestCanceledSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggWorkRequestCanceledSent.setUnits("messages")
_CmmcaWaAggWRIFailureResponseSent_Type = Counter64
_CmmcaWaAggWRIFailureResponseSent_Object = MibTableColumn
cmmcaWaAggWRIFailureResponseSent = _CmmcaWaAggWRIFailureResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 20),
    _CmmcaWaAggWRIFailureResponseSent_Type()
)
cmmcaWaAggWRIFailureResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggWRIFailureResponseSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggWRIFailureResponseSent.setUnits("messages")
_CmmcaWaAggRRIFailureResponseSent_Type = Counter64
_CmmcaWaAggRRIFailureResponseSent_Object = MibTableColumn
cmmcaWaAggRRIFailureResponseSent = _CmmcaWaAggRRIFailureResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 21),
    _CmmcaWaAggRRIFailureResponseSent_Type()
)
cmmcaWaAggRRIFailureResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggRRIFailureResponseSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggRRIFailureResponseSent.setUnits("messages")
_CmmcaWaAggResourceResponseCanceledSent_Type = Counter64
_CmmcaWaAggResourceResponseCanceledSent_Object = MibTableColumn
cmmcaWaAggResourceResponseCanceledSent = _CmmcaWaAggResourceResponseCanceledSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 22),
    _CmmcaWaAggResourceResponseCanceledSent_Type()
)
cmmcaWaAggResourceResponseCanceledSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceResponseCanceledSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggResourceResponseCanceledSent.setUnits("messages")
_CmmcaWaAggCancelQueueEventSent_Type = Counter64
_CmmcaWaAggCancelQueueEventSent_Object = MibTableColumn
cmmcaWaAggCancelQueueEventSent = _CmmcaWaAggCancelQueueEventSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 23),
    _CmmcaWaAggCancelQueueEventSent_Type()
)
cmmcaWaAggCancelQueueEventSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelQueueEventSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggCancelQueueEventSent.setUnits("messages")
_CmmcaWaAggMessageSentError_Type = Counter64
_CmmcaWaAggMessageSentError_Object = MibTableColumn
cmmcaWaAggMessageSentError = _CmmcaWaAggMessageSentError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 24),
    _CmmcaWaAggMessageSentError_Type()
)
cmmcaWaAggMessageSentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaAggMessageSentError.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaAggMessageSentError.setUnits("messages")
_CmmcaWaRtResourceCriteriaCount_Type = Gauge32
_CmmcaWaRtResourceCriteriaCount_Object = MibTableColumn
cmmcaWaRtResourceCriteriaCount = _CmmcaWaRtResourceCriteriaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 25),
    _CmmcaWaRtResourceCriteriaCount_Type()
)
cmmcaWaRtResourceCriteriaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceCriteriaCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceCriteriaCount.setUnits("criteria")
_CmmcaWaRtSelectionStrategyAttrCount_Type = Gauge32
_CmmcaWaRtSelectionStrategyAttrCount_Object = MibTableColumn
cmmcaWaRtSelectionStrategyAttrCount = _CmmcaWaRtSelectionStrategyAttrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 26),
    _CmmcaWaRtSelectionStrategyAttrCount_Type()
)
cmmcaWaRtSelectionStrategyAttrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtSelectionStrategyAttrCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtSelectionStrategyAttrCount.setUnits("attributes")
_CmmcaWaRtAttributeCriteriaCount_Type = Gauge32
_CmmcaWaRtAttributeCriteriaCount_Object = MibTableColumn
cmmcaWaRtAttributeCriteriaCount = _CmmcaWaRtAttributeCriteriaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 27),
    _CmmcaWaRtAttributeCriteriaCount_Type()
)
cmmcaWaRtAttributeCriteriaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeCriteriaCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeCriteriaCount.setUnits("criteria")
_CmmcaWaRtResourceCount_Type = Gauge32
_CmmcaWaRtResourceCount_Object = MibTableColumn
cmmcaWaRtResourceCount = _CmmcaWaRtResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 28),
    _CmmcaWaRtResourceCount_Type()
)
cmmcaWaRtResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceCount.setUnits("resources")
_CmmcaWaRtAttributeValueCount_Type = Gauge32
_CmmcaWaRtAttributeValueCount_Object = MibTableColumn
cmmcaWaRtAttributeValueCount = _CmmcaWaRtAttributeValueCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 29),
    _CmmcaWaRtAttributeValueCount_Type()
)
cmmcaWaRtAttributeValueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeValueCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtAttributeValueCount.setUnits("values")
_CmmcaWaRtSkillCompetencyCount_Type = Gauge32
_CmmcaWaRtSkillCompetencyCount_Object = MibTableColumn
cmmcaWaRtSkillCompetencyCount = _CmmcaWaRtSkillCompetencyCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 30),
    _CmmcaWaRtSkillCompetencyCount_Type()
)
cmmcaWaRtSkillCompetencyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtSkillCompetencyCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtSkillCompetencyCount.setUnits("competencies")
_CmmcaWaRtResourceMemberCount_Type = Gauge32
_CmmcaWaRtResourceMemberCount_Object = MibTableColumn
cmmcaWaRtResourceMemberCount = _CmmcaWaRtResourceMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 31),
    _CmmcaWaRtResourceMemberCount_Type()
)
cmmcaWaRtResourceMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceMemberCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtResourceMemberCount.setUnits("members")
_CmmcaWaRtTotalResourceCount_Type = Gauge32
_CmmcaWaRtTotalResourceCount_Object = MibTableColumn
cmmcaWaRtTotalResourceCount = _CmmcaWaRtTotalResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 32),
    _CmmcaWaRtTotalResourceCount_Type()
)
cmmcaWaRtTotalResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalResourceCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalResourceCount.setUnits("resources")
_CmmcaWaRtTotalContactCount_Type = Gauge32
_CmmcaWaRtTotalContactCount_Object = MibTableColumn
cmmcaWaRtTotalContactCount = _CmmcaWaRtTotalContactCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 33),
    _CmmcaWaRtTotalContactCount_Type()
)
cmmcaWaRtTotalContactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalContactCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalContactCount.setUnits("contacts")
_CmmcaWaRtTotalResourceManagerCount_Type = Gauge32
_CmmcaWaRtTotalResourceManagerCount_Object = MibTableColumn
cmmcaWaRtTotalResourceManagerCount = _CmmcaWaRtTotalResourceManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 34),
    _CmmcaWaRtTotalResourceManagerCount_Type()
)
cmmcaWaRtTotalResourceManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalResourceManagerCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalResourceManagerCount.setUnits("services")
_CmmcaWaRtTotalContactManagerCount_Type = Gauge32
_CmmcaWaRtTotalContactManagerCount_Object = MibTableColumn
cmmcaWaRtTotalContactManagerCount = _CmmcaWaRtTotalContactManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 5, 1, 35),
    _CmmcaWaRtTotalContactManagerCount_Type()
)
cmmcaWaRtTotalContactManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalContactManagerCount.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaWaRtTotalContactManagerCount.setUnits("services")
_CmmcaMpaTable_Object = MibTable
cmmcaMpaTable = _CmmcaMpaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cmmcaMpaTable.setStatus("current")
_CmmcaMpaEntry_Object = MibTableRow
cmmcaMpaEntry = _CmmcaMpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1)
)
cmmcaMpaEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaMpaEntry.setStatus("current")
_CmmcaMpaAggNewCalls_Type = Counter64
_CmmcaMpaAggNewCalls_Object = MibTableColumn
cmmcaMpaAggNewCalls = _CmmcaMpaAggNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 1),
    _CmmcaMpaAggNewCalls_Type()
)
cmmcaMpaAggNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggNewCalls.setUnits("calls")
_CmmcaMpaAggConnectsRcv_Type = Counter64
_CmmcaMpaAggConnectsRcv_Object = MibTableColumn
cmmcaMpaAggConnectsRcv = _CmmcaMpaAggConnectsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 2),
    _CmmcaMpaAggConnectsRcv_Type()
)
cmmcaMpaAggConnectsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggConnectsRcv.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggConnectsRcv.setUnits("connects")
_CmmcaMpaAggAvgLatency_Type = Gauge32
_CmmcaMpaAggAvgLatency_Object = MibTableColumn
cmmcaMpaAggAvgLatency = _CmmcaMpaAggAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 3),
    _CmmcaMpaAggAvgLatency_Type()
)
cmmcaMpaAggAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggAvgLatency.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggAvgLatency.setUnits("milliseconds")
_CmmcaMpaAggFailedInvites_Type = Counter64
_CmmcaMpaAggFailedInvites_Object = MibTableColumn
cmmcaMpaAggFailedInvites = _CmmcaMpaAggFailedInvites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 4),
    _CmmcaMpaAggFailedInvites_Type()
)
cmmcaMpaAggFailedInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggFailedInvites.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggFailedInvites.setUnits("invitations")
_CmmcaMpaAggFailedReinvites_Type = Counter64
_CmmcaMpaAggFailedReinvites_Object = MibTableColumn
cmmcaMpaAggFailedReinvites = _CmmcaMpaAggFailedReinvites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 5),
    _CmmcaMpaAggFailedReinvites_Type()
)
cmmcaMpaAggFailedReinvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggFailedReinvites.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggFailedReinvites.setUnits("invitations")
_CmmcaMpaAggTotalCalls_Type = Counter64
_CmmcaMpaAggTotalCalls_Object = MibTableColumn
cmmcaMpaAggTotalCalls = _CmmcaMpaAggTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 6),
    _CmmcaMpaAggTotalCalls_Type()
)
cmmcaMpaAggTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalCalls.setUnits("calls")
_CmmcaMpaRtIncomingCalls_Type = Gauge32
_CmmcaMpaRtIncomingCalls_Object = MibTableColumn
cmmcaMpaRtIncomingCalls = _CmmcaMpaRtIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 7),
    _CmmcaMpaRtIncomingCalls_Type()
)
cmmcaMpaRtIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtIncomingCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtIncomingCalls.setUnits("calls")
_CmmcaMpaRtOutgoingCalls_Type = Gauge32
_CmmcaMpaRtOutgoingCalls_Object = MibTableColumn
cmmcaMpaRtOutgoingCalls = _CmmcaMpaRtOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 8),
    _CmmcaMpaRtOutgoingCalls_Type()
)
cmmcaMpaRtOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtOutgoingCalls.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtOutgoingCalls.setUnits("calls")
_CmmcaMpaRtActiveClientSessions_Type = Gauge32
_CmmcaMpaRtActiveClientSessions_Object = MibTableColumn
cmmcaMpaRtActiveClientSessions = _CmmcaMpaRtActiveClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 9),
    _CmmcaMpaRtActiveClientSessions_Type()
)
cmmcaMpaRtActiveClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveClientSessions.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveClientSessions.setUnits("sessions")
_CmmcaMpaAggTotalClientsRegistered_Type = Counter64
_CmmcaMpaAggTotalClientsRegistered_Object = MibTableColumn
cmmcaMpaAggTotalClientsRegistered = _CmmcaMpaAggTotalClientsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 10),
    _CmmcaMpaAggTotalClientsRegistered_Type()
)
cmmcaMpaAggTotalClientsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalClientsRegistered.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalClientsRegistered.setUnits("sessions")
_CmmcaMpaAggInstantMessagesSent_Type = Counter64
_CmmcaMpaAggInstantMessagesSent_Object = MibTableColumn
cmmcaMpaAggInstantMessagesSent = _CmmcaMpaAggInstantMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 11),
    _CmmcaMpaAggInstantMessagesSent_Type()
)
cmmcaMpaAggInstantMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggInstantMessagesSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggInstantMessagesSent.setUnits("messages")
_CmmcaMpaAggInstantMessagesReceived_Type = Counter64
_CmmcaMpaAggInstantMessagesReceived_Object = MibTableColumn
cmmcaMpaAggInstantMessagesReceived = _CmmcaMpaAggInstantMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 12),
    _CmmcaMpaAggInstantMessagesReceived_Type()
)
cmmcaMpaAggInstantMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggInstantMessagesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggInstantMessagesReceived.setUnits("messages")
_CmmcaMpaAggPresenceUpdatesReceived_Type = Counter64
_CmmcaMpaAggPresenceUpdatesReceived_Object = MibTableColumn
cmmcaMpaAggPresenceUpdatesReceived = _CmmcaMpaAggPresenceUpdatesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 13),
    _CmmcaMpaAggPresenceUpdatesReceived_Type()
)
cmmcaMpaAggPresenceUpdatesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggPresenceUpdatesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggPresenceUpdatesReceived.setUnits("updates")
_CmmcaMpaAggPresenceUpdatesBytesRcv_Type = Counter64
_CmmcaMpaAggPresenceUpdatesBytesRcv_Object = MibTableColumn
cmmcaMpaAggPresenceUpdatesBytesRcv = _CmmcaMpaAggPresenceUpdatesBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 14),
    _CmmcaMpaAggPresenceUpdatesBytesRcv_Type()
)
cmmcaMpaAggPresenceUpdatesBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggPresenceUpdatesBytesRcv.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggPresenceUpdatesBytesRcv.setUnits("bytes")
_CmmcaMpaRtActiveRegisteredSipAddresses_Type = Gauge32
_CmmcaMpaRtActiveRegisteredSipAddresses_Object = MibTableColumn
cmmcaMpaRtActiveRegisteredSipAddresses = _CmmcaMpaRtActiveRegisteredSipAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 15),
    _CmmcaMpaRtActiveRegisteredSipAddresses_Type()
)
cmmcaMpaRtActiveRegisteredSipAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveRegisteredSipAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveRegisteredSipAddresses.setUnits("addresses")
_CmmcaMpaRtActiveSipControlAddresses_Type = Gauge32
_CmmcaMpaRtActiveSipControlAddresses_Object = MibTableColumn
cmmcaMpaRtActiveSipControlAddresses = _CmmcaMpaRtActiveSipControlAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 16),
    _CmmcaMpaRtActiveSipControlAddresses_Type()
)
cmmcaMpaRtActiveSipControlAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveSipControlAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveSipControlAddresses.setUnits("addresses")
_CmmcaMpaRtActiveIMAddresses_Type = Gauge32
_CmmcaMpaRtActiveIMAddresses_Object = MibTableColumn
cmmcaMpaRtActiveIMAddresses = _CmmcaMpaRtActiveIMAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 17),
    _CmmcaMpaRtActiveIMAddresses_Type()
)
cmmcaMpaRtActiveIMAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveIMAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveIMAddresses.setUnits("addresses")
_CmmcaMpaRtActiveMonitoredPresenceAddresses_Type = Gauge32
_CmmcaMpaRtActiveMonitoredPresenceAddresses_Object = MibTableColumn
cmmcaMpaRtActiveMonitoredPresenceAddresses = _CmmcaMpaRtActiveMonitoredPresenceAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 18),
    _CmmcaMpaRtActiveMonitoredPresenceAddresses_Type()
)
cmmcaMpaRtActiveMonitoredPresenceAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveMonitoredPresenceAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveMonitoredPresenceAddresses.setUnits("addresses")
_CmmcaMpaAggTotalRegisteredSipAddresses_Type = Counter64
_CmmcaMpaAggTotalRegisteredSipAddresses_Object = MibTableColumn
cmmcaMpaAggTotalRegisteredSipAddresses = _CmmcaMpaAggTotalRegisteredSipAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 19),
    _CmmcaMpaAggTotalRegisteredSipAddresses_Type()
)
cmmcaMpaAggTotalRegisteredSipAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalRegisteredSipAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalRegisteredSipAddresses.setUnits("addresses")
_CmmcaMpaAggTotalSipControlAddressesRegistered_Type = Counter64
_CmmcaMpaAggTotalSipControlAddressesRegistered_Object = MibTableColumn
cmmcaMpaAggTotalSipControlAddressesRegistered = _CmmcaMpaAggTotalSipControlAddressesRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 20),
    _CmmcaMpaAggTotalSipControlAddressesRegistered_Type()
)
cmmcaMpaAggTotalSipControlAddressesRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalSipControlAddressesRegistered.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalSipControlAddressesRegistered.setUnits("addresses")
_CmmcaMpaAggTotalIMAddressesRegistered_Type = Counter64
_CmmcaMpaAggTotalIMAddressesRegistered_Object = MibTableColumn
cmmcaMpaAggTotalIMAddressesRegistered = _CmmcaMpaAggTotalIMAddressesRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 21),
    _CmmcaMpaAggTotalIMAddressesRegistered_Type()
)
cmmcaMpaAggTotalIMAddressesRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalIMAddressesRegistered.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalIMAddressesRegistered.setUnits("addresses")
_CmmcaMpaAggTotalMonitoredPresenceAddressesRegistered_Type = Counter64
_CmmcaMpaAggTotalMonitoredPresenceAddressesRegistered_Object = MibTableColumn
cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered = _CmmcaMpaAggTotalMonitoredPresenceAddressesRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 22),
    _CmmcaMpaAggTotalMonitoredPresenceAddressesRegistered_Type()
)
cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered.setUnits("addresses")
_CmmcaMpaRtActiveInteractions_Type = Gauge32
_CmmcaMpaRtActiveInteractions_Object = MibTableColumn
cmmcaMpaRtActiveInteractions = _CmmcaMpaRtActiveInteractions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 23),
    _CmmcaMpaRtActiveInteractions_Type()
)
cmmcaMpaRtActiveInteractions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveInteractions.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActiveInteractions.setUnits("interactions")
_CmmcaMpaRtActivePublishAddresses_Type = Gauge32
_CmmcaMpaRtActivePublishAddresses_Object = MibTableColumn
cmmcaMpaRtActivePublishAddresses = _CmmcaMpaRtActivePublishAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 24),
    _CmmcaMpaRtActivePublishAddresses_Type()
)
cmmcaMpaRtActivePublishAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtActivePublishAddresses.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtActivePublishAddresses.setUnits("addresses")
_CmmcaMpaRtTotalPublishAddressesRegistered_Type = Gauge32
_CmmcaMpaRtTotalPublishAddressesRegistered_Object = MibTableColumn
cmmcaMpaRtTotalPublishAddressesRegistered = _CmmcaMpaRtTotalPublishAddressesRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 6, 1, 25),
    _CmmcaMpaRtTotalPublishAddressesRegistered_Type()
)
cmmcaMpaRtTotalPublishAddressesRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaMpaRtTotalPublishAddressesRegistered.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaMpaRtTotalPublishAddressesRegistered.setUnits("addresses")
_CmmcaRaTable_Object = MibTable
cmmcaRaTable = _CmmcaRaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7)
)
if mibBuilder.loadTexts:
    cmmcaRaTable.setStatus("current")
_CmmcaRaEntry_Object = MibTableRow
cmmcaRaEntry = _CmmcaRaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1)
)
cmmcaRaEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaRaEntry.setStatus("current")
_CmmcaRaAggMsgReceived_Type = Counter64
_CmmcaRaAggMsgReceived_Object = MibTableColumn
cmmcaRaAggMsgReceived = _CmmcaRaAggMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 1),
    _CmmcaRaAggMsgReceived_Type()
)
cmmcaRaAggMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggMsgReceived.setUnits("messages")
_CmmcaRaAggMsgSent_Type = Counter64
_CmmcaRaAggMsgSent_Object = MibTableColumn
cmmcaRaAggMsgSent = _CmmcaRaAggMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 2),
    _CmmcaRaAggMsgSent_Type()
)
cmmcaRaAggMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggMsgSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggMsgSent.setUnits("messages")
_CmmcaRaAggContactDetailMesgReceived_Type = Counter64
_CmmcaRaAggContactDetailMesgReceived_Object = MibTableColumn
cmmcaRaAggContactDetailMesgReceived = _CmmcaRaAggContactDetailMesgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 3),
    _CmmcaRaAggContactDetailMesgReceived_Type()
)
cmmcaRaAggContactDetailMesgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailMesgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailMesgReceived.setUnits("messages")
_CmmcaRaAggContactDetailMesgDispatched_Type = Counter64
_CmmcaRaAggContactDetailMesgDispatched_Object = MibTableColumn
cmmcaRaAggContactDetailMesgDispatched = _CmmcaRaAggContactDetailMesgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 4),
    _CmmcaRaAggContactDetailMesgDispatched_Type()
)
cmmcaRaAggContactDetailMesgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailMesgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailMesgDispatched.setUnits("messages")
_CmmcaRaAggContactDetailAttribMsgDispatched_Type = Counter64
_CmmcaRaAggContactDetailAttribMsgDispatched_Object = MibTableColumn
cmmcaRaAggContactDetailAttribMsgDispatched = _CmmcaRaAggContactDetailAttribMsgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 5),
    _CmmcaRaAggContactDetailAttribMsgDispatched_Type()
)
cmmcaRaAggContactDetailAttribMsgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailAttribMsgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactDetailAttribMsgDispatched.setUnits("messages")
_CmmcaRaAggContactSegDetailMsgReceived_Type = Counter64
_CmmcaRaAggContactSegDetailMsgReceived_Object = MibTableColumn
cmmcaRaAggContactSegDetailMsgReceived = _CmmcaRaAggContactSegDetailMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 6),
    _CmmcaRaAggContactSegDetailMsgReceived_Type()
)
cmmcaRaAggContactSegDetailMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegDetailMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegDetailMsgReceived.setUnits("messages")
_CmmcaRaAggContactSegDetailMesgDispatched_Type = Counter64
_CmmcaRaAggContactSegDetailMesgDispatched_Object = MibTableColumn
cmmcaRaAggContactSegDetailMesgDispatched = _CmmcaRaAggContactSegDetailMesgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 7),
    _CmmcaRaAggContactSegDetailMesgDispatched_Type()
)
cmmcaRaAggContactSegDetailMesgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegDetailMesgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegDetailMesgDispatched.setUnits("messages")
_CmmcaRaAggContactSegMediaDetailMsgDispatched_Type = Counter64
_CmmcaRaAggContactSegMediaDetailMsgDispatched_Object = MibTableColumn
cmmcaRaAggContactSegMediaDetailMsgDispatched = _CmmcaRaAggContactSegMediaDetailMsgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 8),
    _CmmcaRaAggContactSegMediaDetailMsgDispatched_Type()
)
cmmcaRaAggContactSegMediaDetailMsgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegMediaDetailMsgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggContactSegMediaDetailMsgDispatched.setUnits("messages")
_CmmcaRaAggResourceTaskDetailMsgReceived_Type = Counter64
_CmmcaRaAggResourceTaskDetailMsgReceived_Object = MibTableColumn
cmmcaRaAggResourceTaskDetailMsgReceived = _CmmcaRaAggResourceTaskDetailMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 9),
    _CmmcaRaAggResourceTaskDetailMsgReceived_Type()
)
cmmcaRaAggResourceTaskDetailMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceTaskDetailMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceTaskDetailMsgReceived.setUnits("messages")
_CmmcaRaAggResourceTaskDetailMsgDispatched_Type = Counter64
_CmmcaRaAggResourceTaskDetailMsgDispatched_Object = MibTableColumn
cmmcaRaAggResourceTaskDetailMsgDispatched = _CmmcaRaAggResourceTaskDetailMsgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 10),
    _CmmcaRaAggResourceTaskDetailMsgDispatched_Type()
)
cmmcaRaAggResourceTaskDetailMsgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceTaskDetailMsgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceTaskDetailMsgDispatched.setUnits("messages")
_CmmcaRaAggTaskStateChangeMsgReceived_Type = Counter64
_CmmcaRaAggTaskStateChangeMsgReceived_Object = MibTableColumn
cmmcaRaAggTaskStateChangeMsgReceived = _CmmcaRaAggTaskStateChangeMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 11),
    _CmmcaRaAggTaskStateChangeMsgReceived_Type()
)
cmmcaRaAggTaskStateChangeMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggTaskStateChangeMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggTaskStateChangeMsgReceived.setUnits("messages")
_CmmcaRaAggResourceStateChngMesgReceived_Type = Counter64
_CmmcaRaAggResourceStateChngMesgReceived_Object = MibTableColumn
cmmcaRaAggResourceStateChngMesgReceived = _CmmcaRaAggResourceStateChngMesgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 12),
    _CmmcaRaAggResourceStateChngMesgReceived_Type()
)
cmmcaRaAggResourceStateChngMesgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceStateChngMesgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceStateChngMesgReceived.setUnits("messages")
_CmmcaRaAggResourceStateChngMsgDispatched_Type = Counter64
_CmmcaRaAggResourceStateChngMsgDispatched_Object = MibTableColumn
cmmcaRaAggResourceStateChngMsgDispatched = _CmmcaRaAggResourceStateChngMsgDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 13),
    _CmmcaRaAggResourceStateChngMsgDispatched_Type()
)
cmmcaRaAggResourceStateChngMsgDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceStateChngMsgDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggResourceStateChngMsgDispatched.setUnits("messages")
_CmmcaRaAggVersionResponseRecieved_Type = Counter64
_CmmcaRaAggVersionResponseRecieved_Object = MibTableColumn
cmmcaRaAggVersionResponseRecieved = _CmmcaRaAggVersionResponseRecieved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 14),
    _CmmcaRaAggVersionResponseRecieved_Type()
)
cmmcaRaAggVersionResponseRecieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggVersionResponseRecieved.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggVersionResponseRecieved.setUnits("messages")
_CmmcaRaAggVersionRequestDispatched_Type = Counter64
_CmmcaRaAggVersionRequestDispatched_Object = MibTableColumn
cmmcaRaAggVersionRequestDispatched = _CmmcaRaAggVersionRequestDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 15),
    _CmmcaRaAggVersionRequestDispatched_Type()
)
cmmcaRaAggVersionRequestDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggVersionRequestDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggVersionRequestDispatched.setUnits("messages")
_CmmcaRaAggNodeSyncDispatched_Type = Counter64
_CmmcaRaAggNodeSyncDispatched_Object = MibTableColumn
cmmcaRaAggNodeSyncDispatched = _CmmcaRaAggNodeSyncDispatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 7, 1, 16),
    _CmmcaRaAggNodeSyncDispatched_Type()
)
cmmcaRaAggNodeSyncDispatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRaAggNodeSyncDispatched.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRaAggNodeSyncDispatched.setUnits("messages")
_CmmcaRsTable_Object = MibTable
cmmcaRsTable = _CmmcaRsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8)
)
if mibBuilder.loadTexts:
    cmmcaRsTable.setStatus("current")
_CmmcaRsEntry_Object = MibTableRow
cmmcaRsEntry = _CmmcaRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1)
)
cmmcaRsEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaRsEntry.setStatus("current")
_CmmcaRsAggTotalContactDetailRecords_Type = Counter64
_CmmcaRsAggTotalContactDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalContactDetailRecords = _CmmcaRsAggTotalContactDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 1),
    _CmmcaRsAggTotalContactDetailRecords_Type()
)
cmmcaRsAggTotalContactDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactDetailRecords.setUnits("records")
_CmmcaRsAggTotalContactDetailAttributeRecords_Type = Counter64
_CmmcaRsAggTotalContactDetailAttributeRecords_Object = MibTableColumn
cmmcaRsAggTotalContactDetailAttributeRecords = _CmmcaRsAggTotalContactDetailAttributeRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 2),
    _CmmcaRsAggTotalContactDetailAttributeRecords_Type()
)
cmmcaRsAggTotalContactDetailAttributeRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactDetailAttributeRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactDetailAttributeRecords.setUnits("records")
_CmmcaRsAggTotalContactSegmentDetailRecords_Type = Counter64
_CmmcaRsAggTotalContactSegmentDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalContactSegmentDetailRecords = _CmmcaRsAggTotalContactSegmentDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 3),
    _CmmcaRsAggTotalContactSegmentDetailRecords_Type()
)
cmmcaRsAggTotalContactSegmentDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactSegmentDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactSegmentDetailRecords.setUnits("records")
_CmmcaRsAggTotalResourceTaskDetailRecords_Type = Counter64
_CmmcaRsAggTotalResourceTaskDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalResourceTaskDetailRecords = _CmmcaRsAggTotalResourceTaskDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 4),
    _CmmcaRsAggTotalResourceTaskDetailRecords_Type()
)
cmmcaRsAggTotalResourceTaskDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalResourceTaskDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalResourceTaskDetailRecords.setUnits("records")
_CmmcaRsAggTotalResourceEventDetailRecords_Type = Counter64
_CmmcaRsAggTotalResourceEventDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalResourceEventDetailRecords = _CmmcaRsAggTotalResourceEventDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 5),
    _CmmcaRsAggTotalResourceEventDetailRecords_Type()
)
cmmcaRsAggTotalResourceEventDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalResourceEventDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalResourceEventDetailRecords.setUnits("records")
_CmmcaRsAggTotalAssignmentQueDetailRecords_Type = Counter64
_CmmcaRsAggTotalAssignmentQueDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalAssignmentQueDetailRecords = _CmmcaRsAggTotalAssignmentQueDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 6),
    _CmmcaRsAggTotalAssignmentQueDetailRecords_Type()
)
cmmcaRsAggTotalAssignmentQueDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalAssignmentQueDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalAssignmentQueDetailRecords.setUnits("records")
_CmmcaRsAggTotalAssignmentQueAttribRecords_Type = Counter64
_CmmcaRsAggTotalAssignmentQueAttribRecords_Object = MibTableColumn
cmmcaRsAggTotalAssignmentQueAttribRecords = _CmmcaRsAggTotalAssignmentQueAttribRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 7),
    _CmmcaRsAggTotalAssignmentQueAttribRecords_Type()
)
cmmcaRsAggTotalAssignmentQueAttribRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalAssignmentQueAttribRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalAssignmentQueAttribRecords.setUnits("records")
_CmmcaRsAggTotalContactSegmentMediaDetailRecords_Type = Counter64
_CmmcaRsAggTotalContactSegmentMediaDetailRecords_Object = MibTableColumn
cmmcaRsAggTotalContactSegmentMediaDetailRecords = _CmmcaRsAggTotalContactSegmentMediaDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 8),
    _CmmcaRsAggTotalContactSegmentMediaDetailRecords_Type()
)
cmmcaRsAggTotalContactSegmentMediaDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactSegmentMediaDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalContactSegmentMediaDetailRecords.setUnits("records")
_CmmcaRsAggTotalDBWrites_Type = Counter64
_CmmcaRsAggTotalDBWrites_Object = MibTableColumn
cmmcaRsAggTotalDBWrites = _CmmcaRsAggTotalDBWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 9),
    _CmmcaRsAggTotalDBWrites_Type()
)
cmmcaRsAggTotalDBWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalDBWrites.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsAggTotalDBWrites.setUnits("writes")
_CmmcaRsIntContactDetailRecords_Type = Gauge32
_CmmcaRsIntContactDetailRecords_Object = MibTableColumn
cmmcaRsIntContactDetailRecords = _CmmcaRsIntContactDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 10),
    _CmmcaRsIntContactDetailRecords_Type()
)
cmmcaRsIntContactDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntContactDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntContactDetailRecords.setUnits("records")
_CmmcaRsIntContactDetailAttribRecords_Type = Gauge32
_CmmcaRsIntContactDetailAttribRecords_Object = MibTableColumn
cmmcaRsIntContactDetailAttribRecords = _CmmcaRsIntContactDetailAttribRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 11),
    _CmmcaRsIntContactDetailAttribRecords_Type()
)
cmmcaRsIntContactDetailAttribRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntContactDetailAttribRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntContactDetailAttribRecords.setUnits("records")
_CmmcaRsIntContactSegmentDetailRecords_Type = Gauge32
_CmmcaRsIntContactSegmentDetailRecords_Object = MibTableColumn
cmmcaRsIntContactSegmentDetailRecords = _CmmcaRsIntContactSegmentDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 12),
    _CmmcaRsIntContactSegmentDetailRecords_Type()
)
cmmcaRsIntContactSegmentDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntContactSegmentDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntContactSegmentDetailRecords.setUnits("records")
_CmmcaRsIntResourceTaskDetailRecords_Type = Gauge32
_CmmcaRsIntResourceTaskDetailRecords_Object = MibTableColumn
cmmcaRsIntResourceTaskDetailRecords = _CmmcaRsIntResourceTaskDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 13),
    _CmmcaRsIntResourceTaskDetailRecords_Type()
)
cmmcaRsIntResourceTaskDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntResourceTaskDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntResourceTaskDetailRecords.setUnits("records")
_CmmcaRsIntResourceEventDetailRecords_Type = Gauge32
_CmmcaRsIntResourceEventDetailRecords_Object = MibTableColumn
cmmcaRsIntResourceEventDetailRecords = _CmmcaRsIntResourceEventDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 14),
    _CmmcaRsIntResourceEventDetailRecords_Type()
)
cmmcaRsIntResourceEventDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntResourceEventDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntResourceEventDetailRecords.setUnits("records")
_CmmcaRsIntAssignmentQueDetailRecords_Type = Gauge32
_CmmcaRsIntAssignmentQueDetailRecords_Object = MibTableColumn
cmmcaRsIntAssignmentQueDetailRecords = _CmmcaRsIntAssignmentQueDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 15),
    _CmmcaRsIntAssignmentQueDetailRecords_Type()
)
cmmcaRsIntAssignmentQueDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntAssignmentQueDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntAssignmentQueDetailRecords.setUnits("records")
_CmmcaRsIntAssignmentQueAttribRecords_Type = Gauge32
_CmmcaRsIntAssignmentQueAttribRecords_Object = MibTableColumn
cmmcaRsIntAssignmentQueAttribRecords = _CmmcaRsIntAssignmentQueAttribRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 16),
    _CmmcaRsIntAssignmentQueAttribRecords_Type()
)
cmmcaRsIntAssignmentQueAttribRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntAssignmentQueAttribRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntAssignmentQueAttribRecords.setUnits("records")
_CmmcaRsIntContactSegmentMediaDetailRecords_Type = Gauge32
_CmmcaRsIntContactSegmentMediaDetailRecords_Object = MibTableColumn
cmmcaRsIntContactSegmentMediaDetailRecords = _CmmcaRsIntContactSegmentMediaDetailRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 17),
    _CmmcaRsIntContactSegmentMediaDetailRecords_Type()
)
cmmcaRsIntContactSegmentMediaDetailRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntContactSegmentMediaDetailRecords.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntContactSegmentMediaDetailRecords.setUnits("records")
_CmmcaRsIntDBWrites_Type = Gauge32
_CmmcaRsIntDBWrites_Object = MibTableColumn
cmmcaRsIntDBWrites = _CmmcaRsIntDBWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 18),
    _CmmcaRsIntDBWrites_Type()
)
cmmcaRsIntDBWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsIntDBWrites.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsIntDBWrites.setUnits("writes")
_CmmcaRsRtDBStatus_Type = SnmpAdminString
_CmmcaRsRtDBStatus_Object = MibTableColumn
cmmcaRsRtDBStatus = _CmmcaRsRtDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 19),
    _CmmcaRsRtDBStatus_Type()
)
cmmcaRsRtDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtDBStatus.setStatus("current")
_CmmcaRsRtNumberActiveDBUserSessions_Type = Gauge32
_CmmcaRsRtNumberActiveDBUserSessions_Object = MibTableColumn
cmmcaRsRtNumberActiveDBUserSessions = _CmmcaRsRtNumberActiveDBUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 20),
    _CmmcaRsRtNumberActiveDBUserSessions_Type()
)
cmmcaRsRtNumberActiveDBUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtNumberActiveDBUserSessions.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtNumberActiveDBUserSessions.setUnits("sessions")
_CmmcaRsDBSizeAllocated_Type = CounterBasedGauge64
_CmmcaRsDBSizeAllocated_Object = MibTableColumn
cmmcaRsDBSizeAllocated = _CmmcaRsDBSizeAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 21),
    _CmmcaRsDBSizeAllocated_Type()
)
cmmcaRsDBSizeAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsDBSizeAllocated.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsDBSizeAllocated.setUnits("bytes")
_CmmcaRsRtDBSpaceUsed_Type = CounterBasedGauge64
_CmmcaRsRtDBSpaceUsed_Object = MibTableColumn
cmmcaRsRtDBSpaceUsed = _CmmcaRsRtDBSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 22),
    _CmmcaRsRtDBSpaceUsed_Type()
)
cmmcaRsRtDBSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtDBSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtDBSpaceUsed.setUnits("bytes")
_CmmcaRsRtDBSpaceFree_Type = CounterBasedGauge64
_CmmcaRsRtDBSpaceFree_Object = MibTableColumn
cmmcaRsRtDBSpaceFree = _CmmcaRsRtDBSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 23),
    _CmmcaRsRtDBSpaceFree_Type()
)
cmmcaRsRtDBSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtDBSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtDBSpaceFree.setUnits("bytes")
_CmmcaRsRtDBPercentUsed_Type = Gauge32
_CmmcaRsRtDBPercentUsed_Object = MibTableColumn
cmmcaRsRtDBPercentUsed = _CmmcaRsRtDBPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 24),
    _CmmcaRsRtDBPercentUsed_Type()
)
cmmcaRsRtDBPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtDBPercentUsed.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtDBPercentUsed.setUnits("percentage")
_CmmcaRsRtDBPercentFree_Type = Gauge32
_CmmcaRsRtDBPercentFree_Object = MibTableColumn
cmmcaRsRtDBPercentFree = _CmmcaRsRtDBPercentFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 25),
    _CmmcaRsRtDBPercentFree_Type()
)
cmmcaRsRtDBPercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtDBPercentFree.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtDBPercentFree.setUnits("percentage")
_CmmcaRsRtTransactionLogSize_Type = CounterBasedGauge64
_CmmcaRsRtTransactionLogSize_Object = MibTableColumn
cmmcaRsRtTransactionLogSize = _CmmcaRsRtTransactionLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 8, 1, 26),
    _CmmcaRsRtTransactionLogSize_Type()
)
cmmcaRsRtTransactionLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaRsRtTransactionLogSize.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaRsRtTransactionLogSize.setUnits("bytes")
_CmmcaIcmgwTable_Object = MibTable
cmmcaIcmgwTable = _CmmcaIcmgwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9)
)
if mibBuilder.loadTexts:
    cmmcaIcmgwTable.setStatus("current")
_CmmcaIcmgwEntry_Object = MibTableRow
cmmcaIcmgwEntry = _CmmcaIcmgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1)
)
cmmcaIcmgwEntry.setIndexNames(
    (0, "CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIndex"),
)
if mibBuilder.loadTexts:
    cmmcaIcmgwEntry.setStatus("current")
_CmmcaIcmgwAggSocketConnects_Type = Counter64
_CmmcaIcmgwAggSocketConnects_Object = MibTableColumn
cmmcaIcmgwAggSocketConnects = _CmmcaIcmgwAggSocketConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 1),
    _CmmcaIcmgwAggSocketConnects_Type()
)
cmmcaIcmgwAggSocketConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggSocketConnects.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggSocketConnects.setUnits("sockets")
_CmmcaIcmgwAggSocketDisconnects_Type = Counter64
_CmmcaIcmgwAggSocketDisconnects_Object = MibTableColumn
cmmcaIcmgwAggSocketDisconnects = _CmmcaIcmgwAggSocketDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 2),
    _CmmcaIcmgwAggSocketDisconnects_Type()
)
cmmcaIcmgwAggSocketDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggSocketDisconnects.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggSocketDisconnects.setUnits("sockets")
_CmmcaIcmgwAggACMIBytesSent_Type = Counter64
_CmmcaIcmgwAggACMIBytesSent_Object = MibTableColumn
cmmcaIcmgwAggACMIBytesSent = _CmmcaIcmgwAggACMIBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 3),
    _CmmcaIcmgwAggACMIBytesSent_Type()
)
cmmcaIcmgwAggACMIBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIBytesSent.setUnits("bytes")
_CmmcaIcmgwAggACMIBytesRcvd_Type = Counter64
_CmmcaIcmgwAggACMIBytesRcvd_Object = MibTableColumn
cmmcaIcmgwAggACMIBytesRcvd = _CmmcaIcmgwAggACMIBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 4),
    _CmmcaIcmgwAggACMIBytesRcvd_Type()
)
cmmcaIcmgwAggACMIBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIBytesRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIBytesRcvd.setUnits("bytes")
_CmmcaIcmgwAggACMIMsgsSent_Type = Counter64
_CmmcaIcmgwAggACMIMsgsSent_Object = MibTableColumn
cmmcaIcmgwAggACMIMsgsSent = _CmmcaIcmgwAggACMIMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 5),
    _CmmcaIcmgwAggACMIMsgsSent_Type()
)
cmmcaIcmgwAggACMIMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIMsgsSent.setUnits("messages")
_CmmcaIcmgwAggACMIMsgsRcvd_Type = Counter64
_CmmcaIcmgwAggACMIMsgsRcvd_Object = MibTableColumn
cmmcaIcmgwAggACMIMsgsRcvd = _CmmcaIcmgwAggACMIMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 6),
    _CmmcaIcmgwAggACMIMsgsRcvd_Type()
)
cmmcaIcmgwAggACMIMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggACMIMsgsRcvd.setUnits("messages")
_CmmcaIcmgwRtACMIOutQueueDepth_Type = Gauge32
_CmmcaIcmgwRtACMIOutQueueDepth_Object = MibTableColumn
cmmcaIcmgwRtACMIOutQueueDepth = _CmmcaIcmgwRtACMIOutQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 7),
    _CmmcaIcmgwRtACMIOutQueueDepth_Type()
)
cmmcaIcmgwRtACMIOutQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtACMIOutQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtACMIOutQueueDepth.setUnits("messages")
_CmmcaIcmgwRtACMIOutQueueWait_Type = Gauge32
_CmmcaIcmgwRtACMIOutQueueWait_Object = MibTableColumn
cmmcaIcmgwRtACMIOutQueueWait = _CmmcaIcmgwRtACMIOutQueueWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 8),
    _CmmcaIcmgwRtACMIOutQueueWait_Type()
)
cmmcaIcmgwRtACMIOutQueueWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtACMIOutQueueWait.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtACMIOutQueueWait.setUnits("milliseconds")
_CmmcaIcmgwRtAgentsMonitored_Type = Gauge32
_CmmcaIcmgwRtAgentsMonitored_Object = MibTableColumn
cmmcaIcmgwRtAgentsMonitored = _CmmcaIcmgwRtAgentsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 9),
    _CmmcaIcmgwRtAgentsMonitored_Type()
)
cmmcaIcmgwRtAgentsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtAgentsMonitored.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtAgentsMonitored.setUnits("agents")
_CmmcaIcmgwRtAqsMonitored_Type = Gauge32
_CmmcaIcmgwRtAqsMonitored_Object = MibTableColumn
cmmcaIcmgwRtAqsMonitored = _CmmcaIcmgwRtAqsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 10),
    _CmmcaIcmgwRtAqsMonitored_Type()
)
cmmcaIcmgwRtAqsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtAqsMonitored.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtAqsMonitored.setUnits("queues")
_CmmcaIcmgwRtRoutesMonitored_Type = Gauge32
_CmmcaIcmgwRtRoutesMonitored_Object = MibTableColumn
cmmcaIcmgwRtRoutesMonitored = _CmmcaIcmgwRtRoutesMonitored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 11),
    _CmmcaIcmgwRtRoutesMonitored_Type()
)
cmmcaIcmgwRtRoutesMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtRoutesMonitored.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtRoutesMonitored.setUnits("routes")
_CmmcaIcmgwRtPendingQueryAgentStateDlgs_Type = Gauge32
_CmmcaIcmgwRtPendingQueryAgentStateDlgs_Object = MibTableColumn
cmmcaIcmgwRtPendingQueryAgentStateDlgs = _CmmcaIcmgwRtPendingQueryAgentStateDlgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 12),
    _CmmcaIcmgwRtPendingQueryAgentStateDlgs_Type()
)
cmmcaIcmgwRtPendingQueryAgentStateDlgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingQueryAgentStateDlgs.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingQueryAgentStateDlgs.setUnits("dialogues")
_CmmcaIcmgwRtPendingGetContactDetailDlgs_Type = Gauge32
_CmmcaIcmgwRtPendingGetContactDetailDlgs_Object = MibTableColumn
cmmcaIcmgwRtPendingGetContactDetailDlgs = _CmmcaIcmgwRtPendingGetContactDetailDlgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 13),
    _CmmcaIcmgwRtPendingGetContactDetailDlgs_Type()
)
cmmcaIcmgwRtPendingGetContactDetailDlgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingGetContactDetailDlgs.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingGetContactDetailDlgs.setUnits("dialogues")
_CmmcaIcmgwAggQueryAgentStateTimeouts_Type = Counter64
_CmmcaIcmgwAggQueryAgentStateTimeouts_Object = MibTableColumn
cmmcaIcmgwAggQueryAgentStateTimeouts = _CmmcaIcmgwAggQueryAgentStateTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 14),
    _CmmcaIcmgwAggQueryAgentStateTimeouts_Type()
)
cmmcaIcmgwAggQueryAgentStateTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggQueryAgentStateTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggQueryAgentStateTimeouts.setUnits("timeouts")
_CmmcaIcmgwAggGetContactDetailTimeouts_Type = Counter64
_CmmcaIcmgwAggGetContactDetailTimeouts_Object = MibTableColumn
cmmcaIcmgwAggGetContactDetailTimeouts = _CmmcaIcmgwAggGetContactDetailTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 15),
    _CmmcaIcmgwAggGetContactDetailTimeouts_Type()
)
cmmcaIcmgwAggGetContactDetailTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggGetContactDetailTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwAggGetContactDetailTimeouts.setUnits("timeouts")
_CmmcaIcmgwRtQueryAgentStateDelay_Type = Gauge32
_CmmcaIcmgwRtQueryAgentStateDelay_Object = MibTableColumn
cmmcaIcmgwRtQueryAgentStateDelay = _CmmcaIcmgwRtQueryAgentStateDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 16),
    _CmmcaIcmgwRtQueryAgentStateDelay_Type()
)
cmmcaIcmgwRtQueryAgentStateDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtQueryAgentStateDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtQueryAgentStateDelay.setUnits("milliseconds")
_CmmcaIcmgwRtGetContactDetailDelay_Type = Gauge32
_CmmcaIcmgwRtGetContactDetailDelay_Object = MibTableColumn
cmmcaIcmgwRtGetContactDetailDelay = _CmmcaIcmgwRtGetContactDetailDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 17),
    _CmmcaIcmgwRtGetContactDetailDelay_Type()
)
cmmcaIcmgwRtGetContactDetailDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtGetContactDetailDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtGetContactDetailDelay.setUnits("milliseconds")
_CmmcaIcmgwRtPendingCallTermEvents_Type = Gauge32
_CmmcaIcmgwRtPendingCallTermEvents_Object = MibTableColumn
cmmcaIcmgwRtPendingCallTermEvents = _CmmcaIcmgwRtPendingCallTermEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 6, 9, 1, 18),
    _CmmcaIcmgwRtPendingCallTermEvents_Type()
)
cmmcaIcmgwRtPendingCallTermEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingCallTermEvents.setStatus("current")
if mibBuilder.loadTexts:
    cmmcaIcmgwRtPendingCallTermEvents.setUnits("messages")
_CmmcaNotificationInfo_ObjectIdentity = ObjectIdentity
cmmcaNotificationInfo = _CmmcaNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7)
)
_CmmcaEventMessageId_Type = Unsigned32
_CmmcaEventMessageId_Object = MibScalar
cmmcaEventMessageId = _CmmcaEventMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 1),
    _CmmcaEventMessageId_Type()
)
cmmcaEventMessageId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventMessageId.setStatus("current")
_CmmcaEventHostName_Type = SnmpAdminString
_CmmcaEventHostName_Object = MibScalar
cmmcaEventHostName = _CmmcaEventHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 2),
    _CmmcaEventHostName_Type()
)
cmmcaEventHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventHostName.setStatus("current")
_CmmcaEventAppName_Type = SnmpAdminString
_CmmcaEventAppName_Object = MibScalar
cmmcaEventAppName = _CmmcaEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 3),
    _CmmcaEventAppName_Type()
)
cmmcaEventAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventAppName.setStatus("current")
_CmmcaEventMessageName_Type = SnmpAdminString
_CmmcaEventMessageName_Object = MibScalar
cmmcaEventMessageName = _CmmcaEventMessageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 4),
    _CmmcaEventMessageName_Type()
)
cmmcaEventMessageName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventMessageName.setStatus("current")


class _CmmcaEventState_Type(Integer32):
    """Custom type cmmcaEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("raise", 1))
    )


_CmmcaEventState_Type.__name__ = "Integer32"
_CmmcaEventState_Object = MibScalar
cmmcaEventState = _CmmcaEventState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 5),
    _CmmcaEventState_Type()
)
cmmcaEventState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventState.setStatus("current")
_CmmcaEventSeverity_Type = CmmcaSeverityLevel
_CmmcaEventSeverity_Object = MibScalar
cmmcaEventSeverity = _CmmcaEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 6),
    _CmmcaEventSeverity_Type()
)
cmmcaEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventSeverity.setStatus("current")
_CmmcaEventTimestamp_Type = DateAndTime
_CmmcaEventTimestamp_Object = MibScalar
cmmcaEventTimestamp = _CmmcaEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 7),
    _CmmcaEventTimestamp_Type()
)
cmmcaEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventTimestamp.setStatus("current")
_CmmcaEventText_Type = SnmpAdminString
_CmmcaEventText_Object = MibScalar
cmmcaEventText = _CmmcaEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 1, 7, 8),
    _CmmcaEventText_Type()
)
cmmcaEventText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmcaEventText.setStatus("current")
_CiscoMmodalContactAppsMIBConform_ObjectIdentity = ObjectIdentity
ciscoMmodalContactAppsMIBConform = _CiscoMmodalContactAppsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2)
)
_CiscoMmodalContactAppsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMmodalContactAppsMIBCompliances = _CiscoMmodalContactAppsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 1)
)
_CiscoMmodalContactAppsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMmodalContactAppsMIBGroups = _CiscoMmodalContactAppsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2)
)

# Managed Objects groups

cmmcaGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 1)
)
cmmcaGeneralInfoGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServerName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDescription"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaVersion"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaStartTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTimeZoneName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTimeZoneOffsetHours"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTimeZoneOffsetMinutes"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaOpsConsoleURL"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaLocalDeviceType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnableNotifications"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceDescription"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceInetAddressType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaDeviceInetAddress"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaClusterId"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeIpAddr"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeIpAddrType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaNextNodeStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionId"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionSeverity"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionDescription"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionTimeStamp"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaSystemConditionMessage"))
)
if mibBuilder.loadTexts:
    cmmcaGeneralInfoGroup.setStatus("current")

cmmcaLicenseInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 2)
)
cmmcaLicenseInfoGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtLicensesAvailable"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTotalLicensesConfigured"))
)
if mibBuilder.loadTexts:
    cmmcaLicenseInfoGroup.setStatus("current")

cmmcaThreadPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 3)
)
cmmcaThreadPoolGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTPoolRtIdleThreads"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTPoolRtRunningThreads"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTPoolRtCoreThreads"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTPoolRtMaxThreadsAvail"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaTPoolRtMaxThreadsUsed"))
)
if mibBuilder.loadTexts:
    cmmcaThreadPoolGroup.setStatus("current")

cmmcaRuntimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 4)
)
cmmcaRuntimeInfoGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtMaxMemUsed"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtCurrMemUsed"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtMaxMemAvail"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtCurrMemAvail"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtCurrThreadsInUse"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvMaxThreadsUsed"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEnvRtUpTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtMsgQMemPercentUsage"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMaxMsgQMemAvail"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtCongested"))
)
if mibBuilder.loadTexts:
    cmmcaRuntimeInfoGroup.setStatus("current")

cmmcaServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 5)
)
cmmcaServiceGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceType"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaServiceIntPeriod"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtRoutingDomain"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtLogLevel"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtTraceMask"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtMessageThroughput"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtUptime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtMsgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMaxThreadsAvailable"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRtThreadsInUse"))
)
if mibBuilder.loadTexts:
    cmmcaServiceGroup.setStatus("current")

cmmcaRmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 6)
)
cmmcaRmGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsLoggedIn"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsOnCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsReserved"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsWrapUp"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsReady"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmRtAgentsNoQueue"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmAggNumOffersAccept"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmIntNumOffersAccept"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmAggNumOffersReject"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmIntNumOffersReject"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmAggNumOffersTimedOut"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRmIntNumOffersTimedOut"))
)
if mibBuilder.loadTexts:
    cmmcaRmGroup.setStatus("current")

cmmcaCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 7)
)
cmmcaCmGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumActiveCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallTrying"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallRingBack"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallConnecting"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallConnected"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggNumCallArrivals"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntNumCallArrivals"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallRejecting"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallTransferring"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallTerminating"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggAvgCallDurationTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntAvgCallDurationTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallDurationTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntMaxCallDurationTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallDurationTimeDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntMaxCallDurationTimeDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggAvgCallInQueueTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntAvgCallInQueueTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallInQueueTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntMaxCallInQueueTime"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallInQueueTimeDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntMaxCallInQueueTimeDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggAvgCallArrivalRate"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallArrivalRate"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmAggMaxCallArrivalRateDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmRtNumCallInitial"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaCmIntAvgCallArrivalRate"))
)
if mibBuilder.loadTexts:
    cmmcaCmGroup.setStatus("current")

cmmcaRdaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 8)
)
cmmcaRdaGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaAggNumMsgProc"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaIntNumMsgProc"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaAggNumSuccessPresenceNotifications"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaIntNumSuccessPresenceNotifications"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaRtNumActiveClients"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaRtNumOutStandingOfferTasks"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaAggNumUnSuccessPresenceNotifications"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaIntNumUnSuccessPresenceNotifications"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRdaRtNumInactiveClients"))
)
if mibBuilder.loadTexts:
    cmmcaRdaGroup.setStatus("current")

cmmcaBreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 9)
)
cmmcaBreGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggLoadedScripts"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggDistinctScripts"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreRtActiveScripts"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreRtCurrentInstances"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggMaxConcurrentInstances"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntMaxConcurrentInstances"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggMaxConcurrentInstancesDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntMaxConcurrentInstancesDt"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggAvgConcurrentInstances"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntAvgConcurrentInstances"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalContactInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalContactInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalResourceInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalResourceInstanceInitiations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalContactInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalContactInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalResourceInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalResourceInstanceTerminations"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalAbnormalEndings"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalAbnormalEndings"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalAbnormalContactEndings"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalAbnormalContactEndings"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreAggTotalAbnormalResourceEndings"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaBreIntTotalAbnormalResourceEndings"))
)
if mibBuilder.loadTexts:
    cmmcaBreGroup.setStatus("current")

cmmcaWaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 10)
)
cmmcaWaGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtAssignmentQueCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtAttributeDefCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtSelectionStrategyCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtSkillCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggTotalConfigErrors"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggCancelResourceRequestReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResourceRequestReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResourceResponseSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggCancelWorkRequestReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggOfferTaskAcceptedSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggOfferTaskCancelledSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggOfferTaskResponseReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggOfferTaskSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResyncResourceResponseAckSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResyncResourceResponseReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResyncResourceSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggWorkRequestReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggQueueEventSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggWorkRequestCanceledSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggWRIFailureResponseSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggRRIFailureResponseSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggResourceResponseCanceledSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggCancelQueueEventSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaAggMessageSentError"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtResourceCriteriaCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtSelectionStrategyAttrCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtAttributeCriteriaCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtResourceCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtAttributeValueCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtSkillCompetencyCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtResourceMemberCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtTotalResourceCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtTotalContactCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtTotalResourceManagerCount"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaWaRtTotalContactManagerCount"))
)
if mibBuilder.loadTexts:
    cmmcaWaGroup.setStatus("current")

cmmcaMpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 11)
)
cmmcaMpaGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggNewCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggConnectsRcv"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggAvgLatency"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggFailedInvites"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggFailedReinvites"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtIncomingCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtOutgoingCalls"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveClientSessions"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalClientsRegistered"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggInstantMessagesSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggInstantMessagesReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggPresenceUpdatesReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggPresenceUpdatesBytesRcv"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveRegisteredSipAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveSipControlAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveIMAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveMonitoredPresenceAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalRegisteredSipAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalSipControlAddressesRegistered"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalIMAddressesRegistered"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActiveInteractions"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtActivePublishAddresses"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMpaRtTotalPublishAddressesRegistered"))
)
if mibBuilder.loadTexts:
    cmmcaMpaGroup.setStatus("current")

cmmcaRaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 12)
)
cmmcaRaGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggMsgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggMsgSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactDetailMesgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactDetailMesgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactDetailAttribMsgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactSegDetailMsgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactSegDetailMesgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggContactSegMediaDetailMsgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggResourceTaskDetailMsgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggResourceTaskDetailMsgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggTaskStateChangeMsgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggResourceStateChngMesgReceived"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggResourceStateChngMsgDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggVersionResponseRecieved"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggVersionRequestDispatched"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRaAggNodeSyncDispatched"))
)
if mibBuilder.loadTexts:
    cmmcaRaGroup.setStatus("current")

cmmcaRsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 13)
)
cmmcaRsGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalContactDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalContactDetailAttributeRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalContactSegmentDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalResourceTaskDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalResourceEventDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalAssignmentQueDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalAssignmentQueAttribRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalContactSegmentMediaDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsAggTotalDBWrites"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntContactDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntContactDetailAttribRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntContactSegmentDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntResourceTaskDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntResourceEventDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntAssignmentQueDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntAssignmentQueAttribRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntContactSegmentMediaDetailRecords"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsIntDBWrites"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtDBStatus"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtNumberActiveDBUserSessions"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsDBSizeAllocated"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtDBSpaceUsed"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtDBSpaceFree"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtDBPercentUsed"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtDBPercentFree"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaRsRtTransactionLogSize"))
)
if mibBuilder.loadTexts:
    cmmcaRsGroup.setStatus("current")

cmmcaIcmgwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 14)
)
cmmcaIcmgwGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggSocketConnects"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggSocketDisconnects"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggACMIBytesSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggACMIBytesRcvd"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggACMIMsgsSent"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggACMIMsgsRcvd"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtACMIOutQueueDepth"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtACMIOutQueueWait"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtAgentsMonitored"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtAqsMonitored"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtRoutesMonitored"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtPendingQueryAgentStateDlgs"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtPendingGetContactDetailDlgs"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggQueryAgentStateTimeouts"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwAggGetContactDetailTimeouts"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtQueryAgentStateDelay"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtGetContactDetailDelay"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaIcmgwRtPendingCallTermEvents"))
)
if mibBuilder.loadTexts:
    cmmcaIcmgwGroup.setStatus("current")

cmmcaNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 15)
)
cmmcaNotificationInfoGroup.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventMessageId"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventHostName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventAppName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventMessageName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventState"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventSeverity"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventTimestamp"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventText"))
)
if mibBuilder.loadTexts:
    cmmcaNotificationInfoGroup.setStatus("current")


# Notification objects

cmmcaMIBEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 0, 1)
)
cmmcaMIBEvent.setObjects(
      *(("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventMessageId"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventHostName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventAppName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventMessageName"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventState"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventSeverity"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventTimestamp"),
        ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaEventText"))
)
if mibBuilder.loadTexts:
    cmmcaMIBEvent.setStatus(
        "current"
    )


# Notifications groups

cmmcaEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 2, 16)
)
cmmcaEventsGroup.setObjects(
    ("CISCO-MMODAL-CONTACT-APPS-MIB", "cmmcaMIBEvent")
)
if mibBuilder.loadTexts:
    cmmcaEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMmodalContactAppsMIBComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 664, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMmodalContactAppsMIBComplianceRev.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MMODAL-CONTACT-APPS-MIB",
    **{"CmmcaIndex": CmmcaIndex,
       "CmmcaServiceType": CmmcaServiceType,
       "CmmcaServiceStatus": CmmcaServiceStatus,
       "CmmcaNextNodeStatus": CmmcaNextNodeStatus,
       "CmmcaConditionStatus": CmmcaConditionStatus,
       "CmmcaSystemConditionStatus": CmmcaSystemConditionStatus,
       "CmmcaSeverityLevel": CmmcaSeverityLevel,
       "ciscoMmodalContactAppsMIB": ciscoMmodalContactAppsMIB,
       "ciscoMmodalContactAppsMIBNotifs": ciscoMmodalContactAppsMIBNotifs,
       "cmmcaMIBEvent": cmmcaMIBEvent,
       "ciscoMmodalContactAppsMIBObjects": ciscoMmodalContactAppsMIBObjects,
       "cmmcaGeneralInfo": cmmcaGeneralInfo,
       "cmmcaServerName": cmmcaServerName,
       "cmmcaDescription": cmmcaDescription,
       "cmmcaVersion": cmmcaVersion,
       "cmmcaStartTime": cmmcaStartTime,
       "cmmcaTimeZoneName": cmmcaTimeZoneName,
       "cmmcaTimeZoneOffsetHours": cmmcaTimeZoneOffsetHours,
       "cmmcaTimeZoneOffsetMinutes": cmmcaTimeZoneOffsetMinutes,
       "cmmcaOpsConsoleURL": cmmcaOpsConsoleURL,
       "cmmcaLocalDeviceType": cmmcaLocalDeviceType,
       "cmmcaEnableNotifications": cmmcaEnableNotifications,
       "cmmcaSystemConditionStatus": cmmcaSystemConditionStatus,
       "cmmcaSystemStatus": cmmcaSystemStatus,
       "cmmcaClusterInfoTable": cmmcaClusterInfoTable,
       "cmmcaClusterInfoEntry": cmmcaClusterInfoEntry,
       "cmmcaDeviceIndex": cmmcaDeviceIndex,
       "cmmcaDeviceName": cmmcaDeviceName,
       "cmmcaDeviceDescription": cmmcaDeviceDescription,
       "cmmcaDeviceType": cmmcaDeviceType,
       "cmmcaDeviceStatus": cmmcaDeviceStatus,
       "cmmcaDeviceInetAddressType": cmmcaDeviceInetAddressType,
       "cmmcaDeviceInetAddress": cmmcaDeviceInetAddress,
       "cmmcaClusterId": cmmcaClusterId,
       "cmmcaNextNodeTable": cmmcaNextNodeTable,
       "cmmcaNextNodeEntry": cmmcaNextNodeEntry,
       "cmmcaNextNodeIndex": cmmcaNextNodeIndex,
       "cmmcaNextNodeName": cmmcaNextNodeName,
       "cmmcaNextNodeType": cmmcaNextNodeType,
       "cmmcaNextNodeIpAddrType": cmmcaNextNodeIpAddrType,
       "cmmcaNextNodeIpAddr": cmmcaNextNodeIpAddr,
       "cmmcaNextNodeStatus": cmmcaNextNodeStatus,
       "cmmcaSystemConditionTable": cmmcaSystemConditionTable,
       "cmmcaSystemConditionEntry": cmmcaSystemConditionEntry,
       "cmmcaSystemConditionIndex": cmmcaSystemConditionIndex,
       "cmmcaSystemConditionId": cmmcaSystemConditionId,
       "cmmcaSystemConditionSeverity": cmmcaSystemConditionSeverity,
       "cmmcaSystemConditionDescription": cmmcaSystemConditionDescription,
       "cmmcaSystemConditionTimeStamp": cmmcaSystemConditionTimeStamp,
       "cmmcaSystemConditionMessage": cmmcaSystemConditionMessage,
       "cmmcaLicenseInfo": cmmcaLicenseInfo,
       "cmmcaRtLicensesAvailable": cmmcaRtLicensesAvailable,
       "cmmcaTotalLicensesConfigured": cmmcaTotalLicensesConfigured,
       "cmmcaThreadPool": cmmcaThreadPool,
       "cmmcaTPoolRtIdleThreads": cmmcaTPoolRtIdleThreads,
       "cmmcaTPoolRtRunningThreads": cmmcaTPoolRtRunningThreads,
       "cmmcaTPoolRtCoreThreads": cmmcaTPoolRtCoreThreads,
       "cmmcaTPoolRtMaxThreadsAvail": cmmcaTPoolRtMaxThreadsAvail,
       "cmmcaTPoolRtMaxThreadsUsed": cmmcaTPoolRtMaxThreadsUsed,
       "cmmcaRuntimeInfo": cmmcaRuntimeInfo,
       "cmmcaEnvRtMaxMemUsed": cmmcaEnvRtMaxMemUsed,
       "cmmcaEnvRtCurrMemUsed": cmmcaEnvRtCurrMemUsed,
       "cmmcaEnvRtMaxMemAvail": cmmcaEnvRtMaxMemAvail,
       "cmmcaEnvRtCurrMemAvail": cmmcaEnvRtCurrMemAvail,
       "cmmcaEnvRtCurrThreadsInUse": cmmcaEnvRtCurrThreadsInUse,
       "cmmcaEnvMaxThreadsUsed": cmmcaEnvMaxThreadsUsed,
       "cmmcaEnvRtUpTime": cmmcaEnvRtUpTime,
       "cmmcaRtMsgQMemPercentUsage": cmmcaRtMsgQMemPercentUsage,
       "cmmcaMaxMsgQMemAvail": cmmcaMaxMsgQMemAvail,
       "cmmcaRtCongested": cmmcaRtCongested,
       "cmmcaServices": cmmcaServices,
       "cmmcaServiceTable": cmmcaServiceTable,
       "cmmcaServiceEntry": cmmcaServiceEntry,
       "cmmcaServiceIndex": cmmcaServiceIndex,
       "cmmcaServiceType": cmmcaServiceType,
       "cmmcaServiceName": cmmcaServiceName,
       "cmmcaServiceStatus": cmmcaServiceStatus,
       "cmmcaServiceIntPeriod": cmmcaServiceIntPeriod,
       "cmmcaRtRoutingDomain": cmmcaRtRoutingDomain,
       "cmmcaRtLogLevel": cmmcaRtLogLevel,
       "cmmcaRtTraceMask": cmmcaRtTraceMask,
       "cmmcaRtMessageThroughput": cmmcaRtMessageThroughput,
       "cmmcaRtUptime": cmmcaRtUptime,
       "cmmcaRtMsgReceived": cmmcaRtMsgReceived,
       "cmmcaMaxThreadsAvailable": cmmcaMaxThreadsAvailable,
       "cmmcaRtThreadsInUse": cmmcaRtThreadsInUse,
       "cmmcaServiceInfo": cmmcaServiceInfo,
       "cmmcaRmTable": cmmcaRmTable,
       "cmmcaRmEntry": cmmcaRmEntry,
       "cmmcaRmRtAgentsLoggedIn": cmmcaRmRtAgentsLoggedIn,
       "cmmcaRmRtAgentsOnCalls": cmmcaRmRtAgentsOnCalls,
       "cmmcaRmRtAgentsReserved": cmmcaRmRtAgentsReserved,
       "cmmcaRmRtAgentsWrapUp": cmmcaRmRtAgentsWrapUp,
       "cmmcaRmRtAgentsReady": cmmcaRmRtAgentsReady,
       "cmmcaRmRtAgentsNoQueue": cmmcaRmRtAgentsNoQueue,
       "cmmcaRmAggNumOffersAccept": cmmcaRmAggNumOffersAccept,
       "cmmcaRmIntNumOffersAccept": cmmcaRmIntNumOffersAccept,
       "cmmcaRmAggNumOffersReject": cmmcaRmAggNumOffersReject,
       "cmmcaRmIntNumOffersReject": cmmcaRmIntNumOffersReject,
       "cmmcaRmAggNumOffersTimedOut": cmmcaRmAggNumOffersTimedOut,
       "cmmcaRmIntNumOffersTimedOut": cmmcaRmIntNumOffersTimedOut,
       "cmmcaCmTable": cmmcaCmTable,
       "cmmcaCmEntry": cmmcaCmEntry,
       "cmmcaCmRtNumActiveCalls": cmmcaCmRtNumActiveCalls,
       "cmmcaCmRtNumCallTrying": cmmcaCmRtNumCallTrying,
       "cmmcaCmRtNumCallRingBack": cmmcaCmRtNumCallRingBack,
       "cmmcaCmRtNumCallConnecting": cmmcaCmRtNumCallConnecting,
       "cmmcaCmRtNumCallConnected": cmmcaCmRtNumCallConnected,
       "cmmcaCmRtNumCallInitial": cmmcaCmRtNumCallInitial,
       "cmmcaCmAggNumCallArrivals": cmmcaCmAggNumCallArrivals,
       "cmmcaCmIntNumCallArrivals": cmmcaCmIntNumCallArrivals,
       "cmmcaCmRtNumCallRejecting": cmmcaCmRtNumCallRejecting,
       "cmmcaCmRtNumCallTransferring": cmmcaCmRtNumCallTransferring,
       "cmmcaCmRtNumCallTerminating": cmmcaCmRtNumCallTerminating,
       "cmmcaCmAggAvgCallDurationTime": cmmcaCmAggAvgCallDurationTime,
       "cmmcaCmIntAvgCallDurationTime": cmmcaCmIntAvgCallDurationTime,
       "cmmcaCmAggMaxCallDurationTime": cmmcaCmAggMaxCallDurationTime,
       "cmmcaCmIntMaxCallDurationTime": cmmcaCmIntMaxCallDurationTime,
       "cmmcaCmAggMaxCallDurationTimeDt": cmmcaCmAggMaxCallDurationTimeDt,
       "cmmcaCmIntMaxCallDurationTimeDt": cmmcaCmIntMaxCallDurationTimeDt,
       "cmmcaCmAggAvgCallInQueueTime": cmmcaCmAggAvgCallInQueueTime,
       "cmmcaCmIntAvgCallInQueueTime": cmmcaCmIntAvgCallInQueueTime,
       "cmmcaCmAggMaxCallInQueueTime": cmmcaCmAggMaxCallInQueueTime,
       "cmmcaCmIntMaxCallInQueueTime": cmmcaCmIntMaxCallInQueueTime,
       "cmmcaCmAggMaxCallInQueueTimeDt": cmmcaCmAggMaxCallInQueueTimeDt,
       "cmmcaCmIntMaxCallInQueueTimeDt": cmmcaCmIntMaxCallInQueueTimeDt,
       "cmmcaCmAggAvgCallArrivalRate": cmmcaCmAggAvgCallArrivalRate,
       "cmmcaCmAggMaxCallArrivalRate": cmmcaCmAggMaxCallArrivalRate,
       "cmmcaCmAggMaxCallArrivalRateDt": cmmcaCmAggMaxCallArrivalRateDt,
       "cmmcaCmIntAvgCallArrivalRate": cmmcaCmIntAvgCallArrivalRate,
       "cmmcaRdaTable": cmmcaRdaTable,
       "cmmcaRdaEntry": cmmcaRdaEntry,
       "cmmcaRdaAggNumMsgProc": cmmcaRdaAggNumMsgProc,
       "cmmcaRdaIntNumMsgProc": cmmcaRdaIntNumMsgProc,
       "cmmcaRdaAggNumSuccessPresenceNotifications": cmmcaRdaAggNumSuccessPresenceNotifications,
       "cmmcaRdaIntNumSuccessPresenceNotifications": cmmcaRdaIntNumSuccessPresenceNotifications,
       "cmmcaRdaRtNumActiveClients": cmmcaRdaRtNumActiveClients,
       "cmmcaRdaRtNumOutStandingOfferTasks": cmmcaRdaRtNumOutStandingOfferTasks,
       "cmmcaRdaAggNumUnSuccessPresenceNotifications": cmmcaRdaAggNumUnSuccessPresenceNotifications,
       "cmmcaRdaIntNumUnSuccessPresenceNotifications": cmmcaRdaIntNumUnSuccessPresenceNotifications,
       "cmmcaRdaRtNumInactiveClients": cmmcaRdaRtNumInactiveClients,
       "cmmcaBreTable": cmmcaBreTable,
       "cmmcaBreEntry": cmmcaBreEntry,
       "cmmcaBreAggLoadedScripts": cmmcaBreAggLoadedScripts,
       "cmmcaBreAggDistinctScripts": cmmcaBreAggDistinctScripts,
       "cmmcaBreRtActiveScripts": cmmcaBreRtActiveScripts,
       "cmmcaBreRtCurrentInstances": cmmcaBreRtCurrentInstances,
       "cmmcaBreAggMaxConcurrentInstances": cmmcaBreAggMaxConcurrentInstances,
       "cmmcaBreIntMaxConcurrentInstances": cmmcaBreIntMaxConcurrentInstances,
       "cmmcaBreAggMaxConcurrentInstancesDt": cmmcaBreAggMaxConcurrentInstancesDt,
       "cmmcaBreIntMaxConcurrentInstancesDt": cmmcaBreIntMaxConcurrentInstancesDt,
       "cmmcaBreAggAvgConcurrentInstances": cmmcaBreAggAvgConcurrentInstances,
       "cmmcaBreIntAvgConcurrentInstances": cmmcaBreIntAvgConcurrentInstances,
       "cmmcaBreAggTotalInstanceInitiations": cmmcaBreAggTotalInstanceInitiations,
       "cmmcaBreIntTotalInstanceInitiations": cmmcaBreIntTotalInstanceInitiations,
       "cmmcaBreAggTotalContactInstanceInitiations": cmmcaBreAggTotalContactInstanceInitiations,
       "cmmcaBreIntTotalContactInstanceInitiations": cmmcaBreIntTotalContactInstanceInitiations,
       "cmmcaBreAggTotalResourceInstanceInitiations": cmmcaBreAggTotalResourceInstanceInitiations,
       "cmmcaBreIntTotalResourceInstanceInitiations": cmmcaBreIntTotalResourceInstanceInitiations,
       "cmmcaBreAggTotalInstanceTerminations": cmmcaBreAggTotalInstanceTerminations,
       "cmmcaBreIntTotalInstanceTerminations": cmmcaBreIntTotalInstanceTerminations,
       "cmmcaBreAggTotalContactInstanceTerminations": cmmcaBreAggTotalContactInstanceTerminations,
       "cmmcaBreIntTotalContactInstanceTerminations": cmmcaBreIntTotalContactInstanceTerminations,
       "cmmcaBreAggTotalResourceInstanceTerminations": cmmcaBreAggTotalResourceInstanceTerminations,
       "cmmcaBreIntTotalResourceInstanceTerminations": cmmcaBreIntTotalResourceInstanceTerminations,
       "cmmcaBreAggTotalAbnormalEndings": cmmcaBreAggTotalAbnormalEndings,
       "cmmcaBreIntTotalAbnormalEndings": cmmcaBreIntTotalAbnormalEndings,
       "cmmcaBreAggTotalAbnormalContactEndings": cmmcaBreAggTotalAbnormalContactEndings,
       "cmmcaBreIntTotalAbnormalContactEndings": cmmcaBreIntTotalAbnormalContactEndings,
       "cmmcaBreAggTotalAbnormalResourceEndings": cmmcaBreAggTotalAbnormalResourceEndings,
       "cmmcaBreIntTotalAbnormalResourceEndings": cmmcaBreIntTotalAbnormalResourceEndings,
       "cmmcaWaTable": cmmcaWaTable,
       "cmmcaWaEntry": cmmcaWaEntry,
       "cmmcaWaRtAssignmentQueCount": cmmcaWaRtAssignmentQueCount,
       "cmmcaWaRtAttributeDefCount": cmmcaWaRtAttributeDefCount,
       "cmmcaWaRtSelectionStrategyCount": cmmcaWaRtSelectionStrategyCount,
       "cmmcaWaRtSkillCount": cmmcaWaRtSkillCount,
       "cmmcaWaAggTotalConfigErrors": cmmcaWaAggTotalConfigErrors,
       "cmmcaWaAggCancelResourceRequestReceived": cmmcaWaAggCancelResourceRequestReceived,
       "cmmcaWaAggResourceRequestReceived": cmmcaWaAggResourceRequestReceived,
       "cmmcaWaAggResourceResponseSent": cmmcaWaAggResourceResponseSent,
       "cmmcaWaAggCancelWorkRequestReceived": cmmcaWaAggCancelWorkRequestReceived,
       "cmmcaWaAggOfferTaskAcceptedSent": cmmcaWaAggOfferTaskAcceptedSent,
       "cmmcaWaAggOfferTaskCancelledSent": cmmcaWaAggOfferTaskCancelledSent,
       "cmmcaWaAggOfferTaskResponseReceived": cmmcaWaAggOfferTaskResponseReceived,
       "cmmcaWaAggOfferTaskSent": cmmcaWaAggOfferTaskSent,
       "cmmcaWaAggResyncResourceResponseAckSent": cmmcaWaAggResyncResourceResponseAckSent,
       "cmmcaWaAggResyncResourceResponseReceived": cmmcaWaAggResyncResourceResponseReceived,
       "cmmcaWaAggResyncResourceSent": cmmcaWaAggResyncResourceSent,
       "cmmcaWaAggWorkRequestReceived": cmmcaWaAggWorkRequestReceived,
       "cmmcaWaAggQueueEventSent": cmmcaWaAggQueueEventSent,
       "cmmcaWaAggWorkRequestCanceledSent": cmmcaWaAggWorkRequestCanceledSent,
       "cmmcaWaAggWRIFailureResponseSent": cmmcaWaAggWRIFailureResponseSent,
       "cmmcaWaAggRRIFailureResponseSent": cmmcaWaAggRRIFailureResponseSent,
       "cmmcaWaAggResourceResponseCanceledSent": cmmcaWaAggResourceResponseCanceledSent,
       "cmmcaWaAggCancelQueueEventSent": cmmcaWaAggCancelQueueEventSent,
       "cmmcaWaAggMessageSentError": cmmcaWaAggMessageSentError,
       "cmmcaWaRtResourceCriteriaCount": cmmcaWaRtResourceCriteriaCount,
       "cmmcaWaRtSelectionStrategyAttrCount": cmmcaWaRtSelectionStrategyAttrCount,
       "cmmcaWaRtAttributeCriteriaCount": cmmcaWaRtAttributeCriteriaCount,
       "cmmcaWaRtResourceCount": cmmcaWaRtResourceCount,
       "cmmcaWaRtAttributeValueCount": cmmcaWaRtAttributeValueCount,
       "cmmcaWaRtSkillCompetencyCount": cmmcaWaRtSkillCompetencyCount,
       "cmmcaWaRtResourceMemberCount": cmmcaWaRtResourceMemberCount,
       "cmmcaWaRtTotalResourceCount": cmmcaWaRtTotalResourceCount,
       "cmmcaWaRtTotalContactCount": cmmcaWaRtTotalContactCount,
       "cmmcaWaRtTotalResourceManagerCount": cmmcaWaRtTotalResourceManagerCount,
       "cmmcaWaRtTotalContactManagerCount": cmmcaWaRtTotalContactManagerCount,
       "cmmcaMpaTable": cmmcaMpaTable,
       "cmmcaMpaEntry": cmmcaMpaEntry,
       "cmmcaMpaAggNewCalls": cmmcaMpaAggNewCalls,
       "cmmcaMpaAggConnectsRcv": cmmcaMpaAggConnectsRcv,
       "cmmcaMpaAggAvgLatency": cmmcaMpaAggAvgLatency,
       "cmmcaMpaAggFailedInvites": cmmcaMpaAggFailedInvites,
       "cmmcaMpaAggFailedReinvites": cmmcaMpaAggFailedReinvites,
       "cmmcaMpaAggTotalCalls": cmmcaMpaAggTotalCalls,
       "cmmcaMpaRtIncomingCalls": cmmcaMpaRtIncomingCalls,
       "cmmcaMpaRtOutgoingCalls": cmmcaMpaRtOutgoingCalls,
       "cmmcaMpaRtActiveClientSessions": cmmcaMpaRtActiveClientSessions,
       "cmmcaMpaAggTotalClientsRegistered": cmmcaMpaAggTotalClientsRegistered,
       "cmmcaMpaAggInstantMessagesSent": cmmcaMpaAggInstantMessagesSent,
       "cmmcaMpaAggInstantMessagesReceived": cmmcaMpaAggInstantMessagesReceived,
       "cmmcaMpaAggPresenceUpdatesReceived": cmmcaMpaAggPresenceUpdatesReceived,
       "cmmcaMpaAggPresenceUpdatesBytesRcv": cmmcaMpaAggPresenceUpdatesBytesRcv,
       "cmmcaMpaRtActiveRegisteredSipAddresses": cmmcaMpaRtActiveRegisteredSipAddresses,
       "cmmcaMpaRtActiveSipControlAddresses": cmmcaMpaRtActiveSipControlAddresses,
       "cmmcaMpaRtActiveIMAddresses": cmmcaMpaRtActiveIMAddresses,
       "cmmcaMpaRtActiveMonitoredPresenceAddresses": cmmcaMpaRtActiveMonitoredPresenceAddresses,
       "cmmcaMpaAggTotalRegisteredSipAddresses": cmmcaMpaAggTotalRegisteredSipAddresses,
       "cmmcaMpaAggTotalSipControlAddressesRegistered": cmmcaMpaAggTotalSipControlAddressesRegistered,
       "cmmcaMpaAggTotalIMAddressesRegistered": cmmcaMpaAggTotalIMAddressesRegistered,
       "cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered": cmmcaMpaAggTotalMonitoredPresenceAddressesRegistered,
       "cmmcaMpaRtActiveInteractions": cmmcaMpaRtActiveInteractions,
       "cmmcaMpaRtActivePublishAddresses": cmmcaMpaRtActivePublishAddresses,
       "cmmcaMpaRtTotalPublishAddressesRegistered": cmmcaMpaRtTotalPublishAddressesRegistered,
       "cmmcaRaTable": cmmcaRaTable,
       "cmmcaRaEntry": cmmcaRaEntry,
       "cmmcaRaAggMsgReceived": cmmcaRaAggMsgReceived,
       "cmmcaRaAggMsgSent": cmmcaRaAggMsgSent,
       "cmmcaRaAggContactDetailMesgReceived": cmmcaRaAggContactDetailMesgReceived,
       "cmmcaRaAggContactDetailMesgDispatched": cmmcaRaAggContactDetailMesgDispatched,
       "cmmcaRaAggContactDetailAttribMsgDispatched": cmmcaRaAggContactDetailAttribMsgDispatched,
       "cmmcaRaAggContactSegDetailMsgReceived": cmmcaRaAggContactSegDetailMsgReceived,
       "cmmcaRaAggContactSegDetailMesgDispatched": cmmcaRaAggContactSegDetailMesgDispatched,
       "cmmcaRaAggContactSegMediaDetailMsgDispatched": cmmcaRaAggContactSegMediaDetailMsgDispatched,
       "cmmcaRaAggResourceTaskDetailMsgReceived": cmmcaRaAggResourceTaskDetailMsgReceived,
       "cmmcaRaAggResourceTaskDetailMsgDispatched": cmmcaRaAggResourceTaskDetailMsgDispatched,
       "cmmcaRaAggTaskStateChangeMsgReceived": cmmcaRaAggTaskStateChangeMsgReceived,
       "cmmcaRaAggResourceStateChngMesgReceived": cmmcaRaAggResourceStateChngMesgReceived,
       "cmmcaRaAggResourceStateChngMsgDispatched": cmmcaRaAggResourceStateChngMsgDispatched,
       "cmmcaRaAggVersionResponseRecieved": cmmcaRaAggVersionResponseRecieved,
       "cmmcaRaAggVersionRequestDispatched": cmmcaRaAggVersionRequestDispatched,
       "cmmcaRaAggNodeSyncDispatched": cmmcaRaAggNodeSyncDispatched,
       "cmmcaRsTable": cmmcaRsTable,
       "cmmcaRsEntry": cmmcaRsEntry,
       "cmmcaRsAggTotalContactDetailRecords": cmmcaRsAggTotalContactDetailRecords,
       "cmmcaRsAggTotalContactDetailAttributeRecords": cmmcaRsAggTotalContactDetailAttributeRecords,
       "cmmcaRsAggTotalContactSegmentDetailRecords": cmmcaRsAggTotalContactSegmentDetailRecords,
       "cmmcaRsAggTotalResourceTaskDetailRecords": cmmcaRsAggTotalResourceTaskDetailRecords,
       "cmmcaRsAggTotalResourceEventDetailRecords": cmmcaRsAggTotalResourceEventDetailRecords,
       "cmmcaRsAggTotalAssignmentQueDetailRecords": cmmcaRsAggTotalAssignmentQueDetailRecords,
       "cmmcaRsAggTotalAssignmentQueAttribRecords": cmmcaRsAggTotalAssignmentQueAttribRecords,
       "cmmcaRsAggTotalContactSegmentMediaDetailRecords": cmmcaRsAggTotalContactSegmentMediaDetailRecords,
       "cmmcaRsAggTotalDBWrites": cmmcaRsAggTotalDBWrites,
       "cmmcaRsIntContactDetailRecords": cmmcaRsIntContactDetailRecords,
       "cmmcaRsIntContactDetailAttribRecords": cmmcaRsIntContactDetailAttribRecords,
       "cmmcaRsIntContactSegmentDetailRecords": cmmcaRsIntContactSegmentDetailRecords,
       "cmmcaRsIntResourceTaskDetailRecords": cmmcaRsIntResourceTaskDetailRecords,
       "cmmcaRsIntResourceEventDetailRecords": cmmcaRsIntResourceEventDetailRecords,
       "cmmcaRsIntAssignmentQueDetailRecords": cmmcaRsIntAssignmentQueDetailRecords,
       "cmmcaRsIntAssignmentQueAttribRecords": cmmcaRsIntAssignmentQueAttribRecords,
       "cmmcaRsIntContactSegmentMediaDetailRecords": cmmcaRsIntContactSegmentMediaDetailRecords,
       "cmmcaRsIntDBWrites": cmmcaRsIntDBWrites,
       "cmmcaRsRtDBStatus": cmmcaRsRtDBStatus,
       "cmmcaRsRtNumberActiveDBUserSessions": cmmcaRsRtNumberActiveDBUserSessions,
       "cmmcaRsDBSizeAllocated": cmmcaRsDBSizeAllocated,
       "cmmcaRsRtDBSpaceUsed": cmmcaRsRtDBSpaceUsed,
       "cmmcaRsRtDBSpaceFree": cmmcaRsRtDBSpaceFree,
       "cmmcaRsRtDBPercentUsed": cmmcaRsRtDBPercentUsed,
       "cmmcaRsRtDBPercentFree": cmmcaRsRtDBPercentFree,
       "cmmcaRsRtTransactionLogSize": cmmcaRsRtTransactionLogSize,
       "cmmcaIcmgwTable": cmmcaIcmgwTable,
       "cmmcaIcmgwEntry": cmmcaIcmgwEntry,
       "cmmcaIcmgwAggSocketConnects": cmmcaIcmgwAggSocketConnects,
       "cmmcaIcmgwAggSocketDisconnects": cmmcaIcmgwAggSocketDisconnects,
       "cmmcaIcmgwAggACMIBytesSent": cmmcaIcmgwAggACMIBytesSent,
       "cmmcaIcmgwAggACMIBytesRcvd": cmmcaIcmgwAggACMIBytesRcvd,
       "cmmcaIcmgwAggACMIMsgsSent": cmmcaIcmgwAggACMIMsgsSent,
       "cmmcaIcmgwAggACMIMsgsRcvd": cmmcaIcmgwAggACMIMsgsRcvd,
       "cmmcaIcmgwRtACMIOutQueueDepth": cmmcaIcmgwRtACMIOutQueueDepth,
       "cmmcaIcmgwRtACMIOutQueueWait": cmmcaIcmgwRtACMIOutQueueWait,
       "cmmcaIcmgwRtAgentsMonitored": cmmcaIcmgwRtAgentsMonitored,
       "cmmcaIcmgwRtAqsMonitored": cmmcaIcmgwRtAqsMonitored,
       "cmmcaIcmgwRtRoutesMonitored": cmmcaIcmgwRtRoutesMonitored,
       "cmmcaIcmgwRtPendingQueryAgentStateDlgs": cmmcaIcmgwRtPendingQueryAgentStateDlgs,
       "cmmcaIcmgwRtPendingGetContactDetailDlgs": cmmcaIcmgwRtPendingGetContactDetailDlgs,
       "cmmcaIcmgwAggQueryAgentStateTimeouts": cmmcaIcmgwAggQueryAgentStateTimeouts,
       "cmmcaIcmgwAggGetContactDetailTimeouts": cmmcaIcmgwAggGetContactDetailTimeouts,
       "cmmcaIcmgwRtQueryAgentStateDelay": cmmcaIcmgwRtQueryAgentStateDelay,
       "cmmcaIcmgwRtGetContactDetailDelay": cmmcaIcmgwRtGetContactDetailDelay,
       "cmmcaIcmgwRtPendingCallTermEvents": cmmcaIcmgwRtPendingCallTermEvents,
       "cmmcaNotificationInfo": cmmcaNotificationInfo,
       "cmmcaEventMessageId": cmmcaEventMessageId,
       "cmmcaEventHostName": cmmcaEventHostName,
       "cmmcaEventAppName": cmmcaEventAppName,
       "cmmcaEventMessageName": cmmcaEventMessageName,
       "cmmcaEventState": cmmcaEventState,
       "cmmcaEventSeverity": cmmcaEventSeverity,
       "cmmcaEventTimestamp": cmmcaEventTimestamp,
       "cmmcaEventText": cmmcaEventText,
       "ciscoMmodalContactAppsMIBConform": ciscoMmodalContactAppsMIBConform,
       "ciscoMmodalContactAppsMIBCompliances": ciscoMmodalContactAppsMIBCompliances,
       "ciscoMmodalContactAppsMIBComplianceRev": ciscoMmodalContactAppsMIBComplianceRev,
       "ciscoMmodalContactAppsMIBGroups": ciscoMmodalContactAppsMIBGroups,
       "cmmcaGeneralInfoGroup": cmmcaGeneralInfoGroup,
       "cmmcaLicenseInfoGroup": cmmcaLicenseInfoGroup,
       "cmmcaThreadPoolGroup": cmmcaThreadPoolGroup,
       "cmmcaRuntimeInfoGroup": cmmcaRuntimeInfoGroup,
       "cmmcaServiceGroup": cmmcaServiceGroup,
       "cmmcaRmGroup": cmmcaRmGroup,
       "cmmcaCmGroup": cmmcaCmGroup,
       "cmmcaRdaGroup": cmmcaRdaGroup,
       "cmmcaBreGroup": cmmcaBreGroup,
       "cmmcaWaGroup": cmmcaWaGroup,
       "cmmcaMpaGroup": cmmcaMpaGroup,
       "cmmcaRaGroup": cmmcaRaGroup,
       "cmmcaRsGroup": cmmcaRsGroup,
       "cmmcaIcmgwGroup": cmmcaIcmgwGroup,
       "cmmcaNotificationInfoGroup": cmmcaNotificationInfoGroup,
       "cmmcaEventsGroup": cmmcaEventsGroup}
)
