# SNMP MIB module (CISCO-CEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CEF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:22 2024
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

(CefAdjLinkType,
 CefAdjacencySource,
 CefAdminStatus,
 CefCCAction,
 CefCCStatus,
 CefCCType,
 CefFailureReason,
 CefForwardingElementSpecialType,
 CefIpVersion,
 CefMplsLabelList,
 CefOperStatus,
 CefPathType,
 CefPrefixSearchState) = mibBuilder.importSymbols(
    "CISCO-CEF-TC",
    "CefAdjLinkType",
    "CefAdjacencySource",
    "CefAdminStatus",
    "CefCCAction",
    "CefCCStatus",
    "CefCCType",
    "CefFailureReason",
    "CefForwardingElementSpecialType",
    "CefIpVersion",
    "CefMplsLabelList",
    "CefOperStatus",
    "CefPathType",
    "CefPrefixSearchState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsVpnId,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnId")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCefMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492)
)
ciscoCefMIB.setRevisions(
        ("2006-01-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCefMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCefMIBNotifs = _CiscoCefMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 0)
)
_CiscoCefMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCefMIBObjects = _CiscoCefMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1)
)
_CefFIB_ObjectIdentity = ObjectIdentity
cefFIB = _CefFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1)
)
_CefFIBSummary_ObjectIdentity = ObjectIdentity
cefFIBSummary = _CefFIBSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 1)
)
_CefFIBSummaryTable_Object = MibTable
cefFIBSummaryTable = _CefFIBSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cefFIBSummaryTable.setStatus("current")
_CefFIBSummaryEntry_Object = MibTableRow
cefFIBSummaryEntry = _CefFIBSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 1, 1, 1)
)
cefFIBSummaryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
)
if mibBuilder.loadTexts:
    cefFIBSummaryEntry.setStatus("current")
_CefFIBIpVersion_Type = CefIpVersion
_CefFIBIpVersion_Object = MibTableColumn
cefFIBIpVersion = _CefFIBIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 1, 1, 1, 1),
    _CefFIBIpVersion_Type()
)
cefFIBIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefFIBIpVersion.setStatus("current")
_CefFIBSummaryFwdPrefixes_Type = Unsigned32
_CefFIBSummaryFwdPrefixes_Object = MibTableColumn
cefFIBSummaryFwdPrefixes = _CefFIBSummaryFwdPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 1, 1, 1, 2),
    _CefFIBSummaryFwdPrefixes_Type()
)
cefFIBSummaryFwdPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFIBSummaryFwdPrefixes.setStatus("current")
_CefPrefixTable_Object = MibTable
cefPrefixTable = _CefPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cefPrefixTable.setStatus("current")
_CefPrefixEntry_Object = MibTableRow
cefPrefixEntry = _CefPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1)
)
cefPrefixEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefPrefixType"),
    (0, "CISCO-CEF-MIB", "cefPrefixAddr"),
    (0, "CISCO-CEF-MIB", "cefPrefixLen"),
)
if mibBuilder.loadTexts:
    cefPrefixEntry.setStatus("current")
_CefPrefixType_Type = InetAddressType
_CefPrefixType_Object = MibTableColumn
cefPrefixType = _CefPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 1),
    _CefPrefixType_Type()
)
cefPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefPrefixType.setStatus("current")
_CefPrefixAddr_Type = InetAddress
_CefPrefixAddr_Object = MibTableColumn
cefPrefixAddr = _CefPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 2),
    _CefPrefixAddr_Type()
)
cefPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefPrefixAddr.setStatus("current")
_CefPrefixLen_Type = InetAddressPrefixLength
_CefPrefixLen_Object = MibTableColumn
cefPrefixLen = _CefPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 3),
    _CefPrefixLen_Type()
)
cefPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefPrefixLen.setStatus("current")
_CefPrefixForwardingInfo_Type = SnmpAdminString
_CefPrefixForwardingInfo_Object = MibTableColumn
cefPrefixForwardingInfo = _CefPrefixForwardingInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 4),
    _CefPrefixForwardingInfo_Type()
)
cefPrefixForwardingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixForwardingInfo.setStatus("current")
_CefPrefixPkts_Type = Counter32
_CefPrefixPkts_Object = MibTableColumn
cefPrefixPkts = _CefPrefixPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 5),
    _CefPrefixPkts_Type()
)
cefPrefixPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixPkts.setUnits("packets")
_CefPrefixHCPkts_Type = Counter64
_CefPrefixHCPkts_Object = MibTableColumn
cefPrefixHCPkts = _CefPrefixHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 6),
    _CefPrefixHCPkts_Type()
)
cefPrefixHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixHCPkts.setUnits("packets")
_CefPrefixBytes_Type = Counter32
_CefPrefixBytes_Object = MibTableColumn
cefPrefixBytes = _CefPrefixBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 7),
    _CefPrefixBytes_Type()
)
cefPrefixBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixBytes.setUnits("bytes")
_CefPrefixHCBytes_Type = Counter64
_CefPrefixHCBytes_Object = MibTableColumn
cefPrefixHCBytes = _CefPrefixHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 8),
    _CefPrefixHCBytes_Type()
)
cefPrefixHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixHCBytes.setUnits("bytes")
_CefPrefixInternalNRPkts_Type = Counter32
_CefPrefixInternalNRPkts_Object = MibTableColumn
cefPrefixInternalNRPkts = _CefPrefixInternalNRPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 9),
    _CefPrefixInternalNRPkts_Type()
)
cefPrefixInternalNRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixInternalNRPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixInternalNRPkts.setUnits("packets")
_CefPrefixInternalNRHCPkts_Type = Counter64
_CefPrefixInternalNRHCPkts_Object = MibTableColumn
cefPrefixInternalNRHCPkts = _CefPrefixInternalNRHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 10),
    _CefPrefixInternalNRHCPkts_Type()
)
cefPrefixInternalNRHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixInternalNRHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixInternalNRHCPkts.setUnits("packets")
_CefPrefixInternalNRBytes_Type = Counter32
_CefPrefixInternalNRBytes_Object = MibTableColumn
cefPrefixInternalNRBytes = _CefPrefixInternalNRBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 11),
    _CefPrefixInternalNRBytes_Type()
)
cefPrefixInternalNRBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixInternalNRBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixInternalNRBytes.setUnits("bytes")
_CefPrefixInternalNRHCBytes_Type = Counter64
_CefPrefixInternalNRHCBytes_Object = MibTableColumn
cefPrefixInternalNRHCBytes = _CefPrefixInternalNRHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 12),
    _CefPrefixInternalNRHCBytes_Type()
)
cefPrefixInternalNRHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixInternalNRHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixInternalNRHCBytes.setUnits("bytes")
_CefPrefixExternalNRPkts_Type = Counter32
_CefPrefixExternalNRPkts_Object = MibTableColumn
cefPrefixExternalNRPkts = _CefPrefixExternalNRPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 13),
    _CefPrefixExternalNRPkts_Type()
)
cefPrefixExternalNRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixExternalNRPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixExternalNRPkts.setUnits("packets")
_CefPrefixExternalNRHCPkts_Type = Counter64
_CefPrefixExternalNRHCPkts_Object = MibTableColumn
cefPrefixExternalNRHCPkts = _CefPrefixExternalNRHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 14),
    _CefPrefixExternalNRHCPkts_Type()
)
cefPrefixExternalNRHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixExternalNRHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixExternalNRHCPkts.setUnits("packets")
_CefPrefixExternalNRBytes_Type = Counter32
_CefPrefixExternalNRBytes_Object = MibTableColumn
cefPrefixExternalNRBytes = _CefPrefixExternalNRBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 15),
    _CefPrefixExternalNRBytes_Type()
)
cefPrefixExternalNRBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixExternalNRBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixExternalNRBytes.setUnits("bytes")
_CefPrefixExternalNRHCBytes_Type = Counter64
_CefPrefixExternalNRHCBytes_Object = MibTableColumn
cefPrefixExternalNRHCBytes = _CefPrefixExternalNRHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 2, 1, 16),
    _CefPrefixExternalNRHCBytes_Type()
)
cefPrefixExternalNRHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPrefixExternalNRHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefPrefixExternalNRHCBytes.setUnits("bytes")
_CefLMPrefixSpinLock_Type = TestAndIncr
_CefLMPrefixSpinLock_Object = MibScalar
cefLMPrefixSpinLock = _CefLMPrefixSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 3),
    _CefLMPrefixSpinLock_Type()
)
cefLMPrefixSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefLMPrefixSpinLock.setStatus("current")
_CefLMPrefixTable_Object = MibTable
cefLMPrefixTable = _CefLMPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cefLMPrefixTable.setStatus("current")
_CefLMPrefixEntry_Object = MibTableRow
cefLMPrefixEntry = _CefLMPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1)
)
cefLMPrefixEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefLMPrefixDestAddrType"),
    (0, "CISCO-CEF-MIB", "cefLMPrefixDestAddr"),
)
if mibBuilder.loadTexts:
    cefLMPrefixEntry.setStatus("current")
_CefLMPrefixDestAddrType_Type = InetAddressType
_CefLMPrefixDestAddrType_Object = MibTableColumn
cefLMPrefixDestAddrType = _CefLMPrefixDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 1),
    _CefLMPrefixDestAddrType_Type()
)
cefLMPrefixDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefLMPrefixDestAddrType.setStatus("current")
_CefLMPrefixDestAddr_Type = InetAddress
_CefLMPrefixDestAddr_Object = MibTableColumn
cefLMPrefixDestAddr = _CefLMPrefixDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 2),
    _CefLMPrefixDestAddr_Type()
)
cefLMPrefixDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefLMPrefixDestAddr.setStatus("current")
_CefLMPrefixState_Type = CefPrefixSearchState
_CefLMPrefixState_Object = MibTableColumn
cefLMPrefixState = _CefLMPrefixState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 3),
    _CefLMPrefixState_Type()
)
cefLMPrefixState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefLMPrefixState.setStatus("current")
_CefLMPrefixAddr_Type = InetAddress
_CefLMPrefixAddr_Object = MibTableColumn
cefLMPrefixAddr = _CefLMPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 4),
    _CefLMPrefixAddr_Type()
)
cefLMPrefixAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefLMPrefixAddr.setStatus("current")
_CefLMPrefixLen_Type = InetAddressPrefixLength
_CefLMPrefixLen_Object = MibTableColumn
cefLMPrefixLen = _CefLMPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 5),
    _CefLMPrefixLen_Type()
)
cefLMPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefLMPrefixLen.setStatus("current")
_CefLMPrefixRowStatus_Type = RowStatus
_CefLMPrefixRowStatus_Object = MibTableColumn
cefLMPrefixRowStatus = _CefLMPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 4, 1, 6),
    _CefLMPrefixRowStatus_Type()
)
cefLMPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefLMPrefixRowStatus.setStatus("current")
_CefPathTable_Object = MibTable
cefPathTable = _CefPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cefPathTable.setStatus("current")
_CefPathEntry_Object = MibTableRow
cefPathEntry = _CefPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1)
)
cefPathEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefPrefixType"),
    (0, "CISCO-CEF-MIB", "cefPrefixAddr"),
    (0, "CISCO-CEF-MIB", "cefPrefixLen"),
    (0, "CISCO-CEF-MIB", "cefPathId"),
)
if mibBuilder.loadTexts:
    cefPathEntry.setStatus("current")


class _CefPathId_Type(Integer32):
    """Custom type cefPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CefPathId_Type.__name__ = "Integer32"
_CefPathId_Object = MibTableColumn
cefPathId = _CefPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1, 1),
    _CefPathId_Type()
)
cefPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefPathId.setStatus("current")
_CefPathType_Type = CefPathType
_CefPathType_Object = MibTableColumn
cefPathType = _CefPathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1, 2),
    _CefPathType_Type()
)
cefPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPathType.setStatus("current")
_CefPathInterface_Type = InterfaceIndexOrZero
_CefPathInterface_Object = MibTableColumn
cefPathInterface = _CefPathInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1, 3),
    _CefPathInterface_Type()
)
cefPathInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPathInterface.setStatus("current")
_CefPathNextHopAddr_Type = InetAddress
_CefPathNextHopAddr_Object = MibTableColumn
cefPathNextHopAddr = _CefPathNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1, 4),
    _CefPathNextHopAddr_Type()
)
cefPathNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPathNextHopAddr.setStatus("current")
_CefPathRecurseVrfName_Type = MplsVpnId
_CefPathRecurseVrfName_Object = MibTableColumn
cefPathRecurseVrfName = _CefPathRecurseVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 1, 5, 1, 5),
    _CefPathRecurseVrfName_Type()
)
cefPathRecurseVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPathRecurseVrfName.setStatus("current")
_CefAdj_ObjectIdentity = ObjectIdentity
cefAdj = _CefAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2)
)
_CefAdjSummary_ObjectIdentity = ObjectIdentity
cefAdjSummary = _CefAdjSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1)
)
_CefAdjSummaryTable_Object = MibTable
cefAdjSummaryTable = _CefAdjSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cefAdjSummaryTable.setStatus("current")
_CefAdjSummaryEntry_Object = MibTableRow
cefAdjSummaryEntry = _CefAdjSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1)
)
cefAdjSummaryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefAdjSummaryLinkType"),
)
if mibBuilder.loadTexts:
    cefAdjSummaryEntry.setStatus("current")
_CefAdjSummaryLinkType_Type = CefAdjLinkType
_CefAdjSummaryLinkType_Object = MibTableColumn
cefAdjSummaryLinkType = _CefAdjSummaryLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1, 1),
    _CefAdjSummaryLinkType_Type()
)
cefAdjSummaryLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefAdjSummaryLinkType.setStatus("current")
_CefAdjSummaryComplete_Type = Unsigned32
_CefAdjSummaryComplete_Object = MibTableColumn
cefAdjSummaryComplete = _CefAdjSummaryComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1, 2),
    _CefAdjSummaryComplete_Type()
)
cefAdjSummaryComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjSummaryComplete.setStatus("current")
_CefAdjSummaryIncomplete_Type = Unsigned32
_CefAdjSummaryIncomplete_Object = MibTableColumn
cefAdjSummaryIncomplete = _CefAdjSummaryIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1, 3),
    _CefAdjSummaryIncomplete_Type()
)
cefAdjSummaryIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjSummaryIncomplete.setStatus("current")
_CefAdjSummaryFixup_Type = Unsigned32
_CefAdjSummaryFixup_Object = MibTableColumn
cefAdjSummaryFixup = _CefAdjSummaryFixup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1, 4),
    _CefAdjSummaryFixup_Type()
)
cefAdjSummaryFixup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjSummaryFixup.setStatus("current")
_CefAdjSummaryRedirect_Type = Unsigned32
_CefAdjSummaryRedirect_Object = MibTableColumn
cefAdjSummaryRedirect = _CefAdjSummaryRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 1, 1, 1, 5),
    _CefAdjSummaryRedirect_Type()
)
cefAdjSummaryRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjSummaryRedirect.setStatus("current")
_CefAdjTable_Object = MibTable
cefAdjTable = _CefAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cefAdjTable.setStatus("current")
_CefAdjEntry_Object = MibTableRow
cefAdjEntry = _CefAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1)
)
cefAdjEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CEF-MIB", "cefAdjNextHopAddrType"),
    (0, "CISCO-CEF-MIB", "cefAdjNextHopAddr"),
    (0, "CISCO-CEF-MIB", "cefAdjConnId"),
    (0, "CISCO-CEF-MIB", "cefAdjSummaryLinkType"),
)
if mibBuilder.loadTexts:
    cefAdjEntry.setStatus("current")
_CefAdjNextHopAddrType_Type = InetAddressType
_CefAdjNextHopAddrType_Object = MibTableColumn
cefAdjNextHopAddrType = _CefAdjNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 1),
    _CefAdjNextHopAddrType_Type()
)
cefAdjNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefAdjNextHopAddrType.setStatus("current")
_CefAdjNextHopAddr_Type = InetAddress
_CefAdjNextHopAddr_Object = MibTableColumn
cefAdjNextHopAddr = _CefAdjNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 2),
    _CefAdjNextHopAddr_Type()
)
cefAdjNextHopAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefAdjNextHopAddr.setStatus("current")


class _CefAdjConnId_Type(Unsigned32):
    """Custom type cefAdjConnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CefAdjConnId_Type.__name__ = "Unsigned32"
_CefAdjConnId_Object = MibTableColumn
cefAdjConnId = _CefAdjConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 3),
    _CefAdjConnId_Type()
)
cefAdjConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefAdjConnId.setStatus("current")
_CefAdjSource_Type = CefAdjacencySource
_CefAdjSource_Object = MibTableColumn
cefAdjSource = _CefAdjSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 4),
    _CefAdjSource_Type()
)
cefAdjSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjSource.setStatus("current")
_CefAdjEncap_Type = SnmpAdminString
_CefAdjEncap_Object = MibTableColumn
cefAdjEncap = _CefAdjEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 5),
    _CefAdjEncap_Type()
)
cefAdjEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjEncap.setStatus("current")
_CefAdjFixup_Type = SnmpAdminString
_CefAdjFixup_Object = MibTableColumn
cefAdjFixup = _CefAdjFixup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 6),
    _CefAdjFixup_Type()
)
cefAdjFixup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjFixup.setStatus("current")


class _CefAdjMTU_Type(Unsigned32):
    """Custom type cefAdjMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CefAdjMTU_Type.__name__ = "Unsigned32"
_CefAdjMTU_Object = MibTableColumn
cefAdjMTU = _CefAdjMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 7),
    _CefAdjMTU_Type()
)
cefAdjMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjMTU.setStatus("current")
if mibBuilder.loadTexts:
    cefAdjMTU.setUnits("bytes")
_CefAdjForwardingInfo_Type = SnmpAdminString
_CefAdjForwardingInfo_Object = MibTableColumn
cefAdjForwardingInfo = _CefAdjForwardingInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 8),
    _CefAdjForwardingInfo_Type()
)
cefAdjForwardingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjForwardingInfo.setStatus("current")
_CefAdjPkts_Type = Counter32
_CefAdjPkts_Object = MibTableColumn
cefAdjPkts = _CefAdjPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 9),
    _CefAdjPkts_Type()
)
cefAdjPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefAdjPkts.setUnits("packets")
_CefAdjHCPkts_Type = Counter64
_CefAdjHCPkts_Object = MibTableColumn
cefAdjHCPkts = _CefAdjHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 10),
    _CefAdjHCPkts_Type()
)
cefAdjHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    cefAdjHCPkts.setUnits("packets")
_CefAdjBytes_Type = Counter32
_CefAdjBytes_Object = MibTableColumn
cefAdjBytes = _CefAdjBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 11),
    _CefAdjBytes_Type()
)
cefAdjBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefAdjBytes.setUnits("bytes")
_CefAdjHCBytes_Type = Counter64
_CefAdjHCBytes_Object = MibTableColumn
cefAdjHCBytes = _CefAdjHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 2, 2, 1, 12),
    _CefAdjHCBytes_Type()
)
cefAdjHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefAdjHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    cefAdjHCBytes.setUnits("bytes")
_CefFE_ObjectIdentity = ObjectIdentity
cefFE = _CefFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3)
)
_CefFESelectionTable_Object = MibTable
cefFESelectionTable = _CefFESelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cefFESelectionTable.setStatus("current")
_CefFESelectionEntry_Object = MibTableRow
cefFESelectionEntry = _CefFESelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1)
)
cefFESelectionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFESelectionName"),
    (0, "CISCO-CEF-MIB", "cefFESelectionId"),
)
if mibBuilder.loadTexts:
    cefFESelectionEntry.setStatus("current")


class _CefFESelectionName_Type(SnmpAdminString):
    """Custom type cefFESelectionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CefFESelectionName_Type.__name__ = "SnmpAdminString"
_CefFESelectionName_Object = MibTableColumn
cefFESelectionName = _CefFESelectionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 1),
    _CefFESelectionName_Type()
)
cefFESelectionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefFESelectionName.setStatus("current")


class _CefFESelectionId_Type(Integer32):
    """Custom type cefFESelectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CefFESelectionId_Type.__name__ = "Integer32"
_CefFESelectionId_Object = MibTableColumn
cefFESelectionId = _CefFESelectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 2),
    _CefFESelectionId_Type()
)
cefFESelectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefFESelectionId.setStatus("current")
_CefFESelectionSpecial_Type = CefForwardingElementSpecialType
_CefFESelectionSpecial_Object = MibTableColumn
cefFESelectionSpecial = _CefFESelectionSpecial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 3),
    _CefFESelectionSpecial_Type()
)
cefFESelectionSpecial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionSpecial.setStatus("current")
_CefFESelectionLabels_Type = CefMplsLabelList
_CefFESelectionLabels_Object = MibTableColumn
cefFESelectionLabels = _CefFESelectionLabels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 4),
    _CefFESelectionLabels_Type()
)
cefFESelectionLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionLabels.setStatus("current")
_CefFESelectionAdjLinkType_Type = CefAdjLinkType
_CefFESelectionAdjLinkType_Object = MibTableColumn
cefFESelectionAdjLinkType = _CefFESelectionAdjLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 5),
    _CefFESelectionAdjLinkType_Type()
)
cefFESelectionAdjLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionAdjLinkType.setStatus("current")
_CefFESelectionAdjInterface_Type = InterfaceIndexOrZero
_CefFESelectionAdjInterface_Object = MibTableColumn
cefFESelectionAdjInterface = _CefFESelectionAdjInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 6),
    _CefFESelectionAdjInterface_Type()
)
cefFESelectionAdjInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionAdjInterface.setStatus("current")
_CefFESelectionAdjNextHopAddrType_Type = InetAddressType
_CefFESelectionAdjNextHopAddrType_Object = MibTableColumn
cefFESelectionAdjNextHopAddrType = _CefFESelectionAdjNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 7),
    _CefFESelectionAdjNextHopAddrType_Type()
)
cefFESelectionAdjNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionAdjNextHopAddrType.setStatus("current")
_CefFESelectionAdjNextHopAddr_Type = InetAddress
_CefFESelectionAdjNextHopAddr_Object = MibTableColumn
cefFESelectionAdjNextHopAddr = _CefFESelectionAdjNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 8),
    _CefFESelectionAdjNextHopAddr_Type()
)
cefFESelectionAdjNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionAdjNextHopAddr.setStatus("current")


class _CefFESelectionAdjConnId_Type(Unsigned32):
    """Custom type cefFESelectionAdjConnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CefFESelectionAdjConnId_Type.__name__ = "Unsigned32"
_CefFESelectionAdjConnId_Object = MibTableColumn
cefFESelectionAdjConnId = _CefFESelectionAdjConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 9),
    _CefFESelectionAdjConnId_Type()
)
cefFESelectionAdjConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionAdjConnId.setStatus("current")
_CefFESelectionVrfName_Type = MplsVpnId
_CefFESelectionVrfName_Object = MibTableColumn
cefFESelectionVrfName = _CefFESelectionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 10),
    _CefFESelectionVrfName_Type()
)
cefFESelectionVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionVrfName.setStatus("current")


class _CefFESelectionWeight_Type(Unsigned32):
    """Custom type cefFESelectionWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CefFESelectionWeight_Type.__name__ = "Unsigned32"
_CefFESelectionWeight_Object = MibTableColumn
cefFESelectionWeight = _CefFESelectionWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 3, 1, 1, 11),
    _CefFESelectionWeight_Type()
)
cefFESelectionWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefFESelectionWeight.setStatus("current")
_CefGlobal_ObjectIdentity = ObjectIdentity
cefGlobal = _CefGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4)
)
_CefCfgTable_Object = MibTable
cefCfgTable = _CefCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cefCfgTable.setStatus("current")
_CefCfgEntry_Object = MibTableRow
cefCfgEntry = _CefCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1)
)
cefCfgEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
)
if mibBuilder.loadTexts:
    cefCfgEntry.setStatus("current")
_CefCfgAdminState_Type = CefAdminStatus
_CefCfgAdminState_Object = MibTableColumn
cefCfgAdminState = _CefCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 1),
    _CefCfgAdminState_Type()
)
cefCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgAdminState.setStatus("current")
_CefCfgOperState_Type = CefOperStatus
_CefCfgOperState_Object = MibTableColumn
cefCfgOperState = _CefCfgOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 2),
    _CefCfgOperState_Type()
)
cefCfgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCfgOperState.setStatus("current")
_CefCfgDistributionAdminState_Type = CefAdminStatus
_CefCfgDistributionAdminState_Object = MibTableColumn
cefCfgDistributionAdminState = _CefCfgDistributionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 3),
    _CefCfgDistributionAdminState_Type()
)
cefCfgDistributionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgDistributionAdminState.setStatus("current")
_CefCfgDistributionOperState_Type = CefOperStatus
_CefCfgDistributionOperState_Object = MibTableColumn
cefCfgDistributionOperState = _CefCfgDistributionOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 4),
    _CefCfgDistributionOperState_Type()
)
cefCfgDistributionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCfgDistributionOperState.setStatus("current")


class _CefCfgAccountingMap_Type(Bits):
    """Custom type cefCfgAccountingMap based on Bits"""
    namedValues = NamedValues(
        *(("nonRecursive", 0),
          ("perPrefix", 1),
          ("prefixLength", 2))
    )

_CefCfgAccountingMap_Type.__name__ = "Bits"
_CefCfgAccountingMap_Object = MibTableColumn
cefCfgAccountingMap = _CefCfgAccountingMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 5),
    _CefCfgAccountingMap_Type()
)
cefCfgAccountingMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgAccountingMap.setStatus("current")


class _CefCfgLoadSharingAlgorithm_Type(Integer32):
    """Custom type cefCfgLoadSharingAlgorithm based on Integer32"""
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
        *(("none", 1),
          ("original", 2),
          ("tunnel", 3),
          ("universal", 4))
    )


_CefCfgLoadSharingAlgorithm_Type.__name__ = "Integer32"
_CefCfgLoadSharingAlgorithm_Object = MibTableColumn
cefCfgLoadSharingAlgorithm = _CefCfgLoadSharingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 6),
    _CefCfgLoadSharingAlgorithm_Type()
)
cefCfgLoadSharingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgLoadSharingAlgorithm.setStatus("current")


class _CefCfgLoadSharingID_Type(Unsigned32):
    """Custom type cefCfgLoadSharingID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_CefCfgLoadSharingID_Type.__name__ = "Unsigned32"
_CefCfgLoadSharingID_Object = MibTableColumn
cefCfgLoadSharingID = _CefCfgLoadSharingID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 7),
    _CefCfgLoadSharingID_Type()
)
cefCfgLoadSharingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgLoadSharingID.setStatus("current")
_CefCfgTrafficStatsLoadInterval_Type = Unsigned32
_CefCfgTrafficStatsLoadInterval_Object = MibTableColumn
cefCfgTrafficStatsLoadInterval = _CefCfgTrafficStatsLoadInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 8),
    _CefCfgTrafficStatsLoadInterval_Type()
)
cefCfgTrafficStatsLoadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgTrafficStatsLoadInterval.setStatus("current")
if mibBuilder.loadTexts:
    cefCfgTrafficStatsLoadInterval.setUnits("seconds")


class _CefCfgTrafficStatsUpdateRate_Type(Unsigned32):
    """Custom type cefCfgTrafficStatsUpdateRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_CefCfgTrafficStatsUpdateRate_Type.__name__ = "Unsigned32"
_CefCfgTrafficStatsUpdateRate_Object = MibTableColumn
cefCfgTrafficStatsUpdateRate = _CefCfgTrafficStatsUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 1, 1, 9),
    _CefCfgTrafficStatsUpdateRate_Type()
)
cefCfgTrafficStatsUpdateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCfgTrafficStatsUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    cefCfgTrafficStatsUpdateRate.setUnits("seconds")
_CefResourceTable_Object = MibTable
cefResourceTable = _CefResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cefResourceTable.setStatus("current")
_CefResourceEntry_Object = MibTableRow
cefResourceEntry = _CefResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 2, 1)
)
cefResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefResourceEntry.setStatus("current")
_CefResourceMemoryUsed_Type = Gauge32
_CefResourceMemoryUsed_Object = MibTableColumn
cefResourceMemoryUsed = _CefResourceMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 2, 1, 1),
    _CefResourceMemoryUsed_Type()
)
cefResourceMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefResourceMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    cefResourceMemoryUsed.setUnits("bytes")
_CefResourceFailureReason_Type = CefFailureReason
_CefResourceFailureReason_Object = MibTableColumn
cefResourceFailureReason = _CefResourceFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 4, 2, 1, 2),
    _CefResourceFailureReason_Type()
)
cefResourceFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefResourceFailureReason.setStatus("current")
_CefInterface_ObjectIdentity = ObjectIdentity
cefInterface = _CefInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5)
)
_CefIntTable_Object = MibTable
cefIntTable = _CefIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cefIntTable.setStatus("current")
_CefIntEntry_Object = MibTableRow
cefIntEntry = _CefIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5, 1, 1)
)
cefIntEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cefIntEntry.setStatus("current")


class _CefIntSwitchingState_Type(Integer32):
    """Custom type cefIntSwitchingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cefDisabled", 3),
          ("cefEnabled", 1),
          ("distCefEnabled", 2))
    )


_CefIntSwitchingState_Type.__name__ = "Integer32"
_CefIntSwitchingState_Object = MibTableColumn
cefIntSwitchingState = _CefIntSwitchingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5, 1, 1, 1),
    _CefIntSwitchingState_Type()
)
cefIntSwitchingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefIntSwitchingState.setStatus("current")


class _CefIntLoadSharing_Type(Integer32):
    """Custom type cefIntLoadSharing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perDestination", 2),
          ("perPacket", 1))
    )


_CefIntLoadSharing_Type.__name__ = "Integer32"
_CefIntLoadSharing_Object = MibTableColumn
cefIntLoadSharing = _CefIntLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5, 1, 1, 2),
    _CefIntLoadSharing_Type()
)
cefIntLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefIntLoadSharing.setStatus("current")


class _CefIntNonrecursiveAccouting_Type(Integer32):
    """Custom type cefIntNonrecursiveAccouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_CefIntNonrecursiveAccouting_Type.__name__ = "Integer32"
_CefIntNonrecursiveAccouting_Object = MibTableColumn
cefIntNonrecursiveAccouting = _CefIntNonrecursiveAccouting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 5, 1, 1, 3),
    _CefIntNonrecursiveAccouting_Type()
)
cefIntNonrecursiveAccouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefIntNonrecursiveAccouting.setStatus("current")
_CefPeer_ObjectIdentity = ObjectIdentity
cefPeer = _CefPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6)
)
_CefPeerTable_Object = MibTable
cefPeerTable = _CefPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cefPeerTable.setStatus("current")
_CefPeerEntry_Object = MibTableRow
cefPeerEntry = _CefPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 1, 1)
)
cefPeerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "entPeerPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefPeerEntry.setStatus("current")
_EntPeerPhysicalIndex_Type = PhysicalIndex
_EntPeerPhysicalIndex_Object = MibTableColumn
entPeerPhysicalIndex = _EntPeerPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 1, 1, 1),
    _EntPeerPhysicalIndex_Type()
)
entPeerPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPeerPhysicalIndex.setStatus("current")


class _CefPeerOperState_Type(Integer32):
    """Custom type cefPeerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peerDisabled", 1),
          ("peerHold", 3),
          ("peerUp", 2))
    )


_CefPeerOperState_Type.__name__ = "Integer32"
_CefPeerOperState_Object = MibTableColumn
cefPeerOperState = _CefPeerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 1, 1, 2),
    _CefPeerOperState_Type()
)
cefPeerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPeerOperState.setStatus("current")
_CefPeerNumberOfResets_Type = Counter32
_CefPeerNumberOfResets_Object = MibTableColumn
cefPeerNumberOfResets = _CefPeerNumberOfResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 1, 1, 3),
    _CefPeerNumberOfResets_Type()
)
cefPeerNumberOfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPeerNumberOfResets.setStatus("current")
_CefPeerFIBTable_Object = MibTable
cefPeerFIBTable = _CefPeerFIBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cefPeerFIBTable.setStatus("current")
_CefPeerFIBEntry_Object = MibTableRow
cefPeerFIBEntry = _CefPeerFIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 2, 1)
)
cefPeerFIBEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "entPeerPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
)
if mibBuilder.loadTexts:
    cefPeerFIBEntry.setStatus("current")


class _CefPeerFIBOperState_Type(Integer32):
    """Custom type cefPeerFIBOperState based on Integer32"""
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
        *(("peerFIBDown", 1),
          ("peerFIBReloadRequest", 3),
          ("peerFIBReloading", 4),
          ("peerFIBSynced", 5),
          ("peerFIBUp", 2))
    )


_CefPeerFIBOperState_Type.__name__ = "Integer32"
_CefPeerFIBOperState_Object = MibTableColumn
cefPeerFIBOperState = _CefPeerFIBOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 6, 2, 1, 1),
    _CefPeerFIBOperState_Type()
)
cefPeerFIBOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefPeerFIBOperState.setStatus("current")
_CefCC_ObjectIdentity = ObjectIdentity
cefCC = _CefCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7)
)
_CefCCGlobalTable_Object = MibTable
cefCCGlobalTable = _CefCCGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cefCCGlobalTable.setStatus("current")
_CefCCGlobalEntry_Object = MibTableRow
cefCCGlobalEntry = _CefCCGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1)
)
cefCCGlobalEntry.setIndexNames(
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
)
if mibBuilder.loadTexts:
    cefCCGlobalEntry.setStatus("current")
_CefCCGlobalAutoRepairEnabled_Type = TruthValue
_CefCCGlobalAutoRepairEnabled_Object = MibTableColumn
cefCCGlobalAutoRepairEnabled = _CefCCGlobalAutoRepairEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 1),
    _CefCCGlobalAutoRepairEnabled_Type()
)
cefCCGlobalAutoRepairEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCGlobalAutoRepairEnabled.setStatus("current")
_CefCCGlobalAutoRepairDelay_Type = Unsigned32
_CefCCGlobalAutoRepairDelay_Object = MibTableColumn
cefCCGlobalAutoRepairDelay = _CefCCGlobalAutoRepairDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 2),
    _CefCCGlobalAutoRepairDelay_Type()
)
cefCCGlobalAutoRepairDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCGlobalAutoRepairDelay.setStatus("current")
if mibBuilder.loadTexts:
    cefCCGlobalAutoRepairDelay.setUnits("seconds")
_CefCCGlobalAutoRepairHoldDown_Type = Unsigned32
_CefCCGlobalAutoRepairHoldDown_Object = MibTableColumn
cefCCGlobalAutoRepairHoldDown = _CefCCGlobalAutoRepairHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 3),
    _CefCCGlobalAutoRepairHoldDown_Type()
)
cefCCGlobalAutoRepairHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCGlobalAutoRepairHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    cefCCGlobalAutoRepairHoldDown.setUnits("seconds")
_CefCCGlobalErrorMsgEnabled_Type = TruthValue
_CefCCGlobalErrorMsgEnabled_Object = MibTableColumn
cefCCGlobalErrorMsgEnabled = _CefCCGlobalErrorMsgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 4),
    _CefCCGlobalErrorMsgEnabled_Type()
)
cefCCGlobalErrorMsgEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCGlobalErrorMsgEnabled.setStatus("current")


class _CefCCGlobalFullScanAction_Type(CefCCAction):
    """Custom type cefCCGlobalFullScanAction based on CefCCAction"""


_CefCCGlobalFullScanAction_Object = MibTableColumn
cefCCGlobalFullScanAction = _CefCCGlobalFullScanAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 5),
    _CefCCGlobalFullScanAction_Type()
)
cefCCGlobalFullScanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCGlobalFullScanAction.setStatus("current")
_CefCCGlobalFullScanStatus_Type = CefCCStatus
_CefCCGlobalFullScanStatus_Object = MibTableColumn
cefCCGlobalFullScanStatus = _CefCCGlobalFullScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 1, 1, 6),
    _CefCCGlobalFullScanStatus_Type()
)
cefCCGlobalFullScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCCGlobalFullScanStatus.setStatus("current")
_CefCCTypeTable_Object = MibTable
cefCCTypeTable = _CefCCTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cefCCTypeTable.setStatus("current")
_CefCCTypeEntry_Object = MibTableRow
cefCCTypeEntry = _CefCCTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1)
)
cefCCTypeEntry.setIndexNames(
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
    (0, "CISCO-CEF-MIB", "cefCCType"),
)
if mibBuilder.loadTexts:
    cefCCTypeEntry.setStatus("current")
_CefCCType_Type = CefCCType
_CefCCType_Object = MibTableColumn
cefCCType = _CefCCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 1),
    _CefCCType_Type()
)
cefCCType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefCCType.setStatus("current")
_CefCCEnabled_Type = TruthValue
_CefCCEnabled_Object = MibTableColumn
cefCCEnabled = _CefCCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 2),
    _CefCCEnabled_Type()
)
cefCCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCEnabled.setStatus("current")
_CefCCCount_Type = Unsigned32
_CefCCCount_Object = MibTableColumn
cefCCCount = _CefCCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 3),
    _CefCCCount_Type()
)
cefCCCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCCount.setStatus("current")
_CefCCPeriod_Type = Unsigned32
_CefCCPeriod_Object = MibTableColumn
cefCCPeriod = _CefCCPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 4),
    _CefCCPeriod_Type()
)
cefCCPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefCCPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cefCCPeriod.setUnits("seconds")
_CefCCQueriesSent_Type = Counter32
_CefCCQueriesSent_Object = MibTableColumn
cefCCQueriesSent = _CefCCQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 5),
    _CefCCQueriesSent_Type()
)
cefCCQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCCQueriesSent.setStatus("current")
_CefCCQueriesIgnored_Type = Counter32
_CefCCQueriesIgnored_Object = MibTableColumn
cefCCQueriesIgnored = _CefCCQueriesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 6),
    _CefCCQueriesIgnored_Type()
)
cefCCQueriesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCCQueriesIgnored.setStatus("current")
_CefCCQueriesChecked_Type = Counter32
_CefCCQueriesChecked_Object = MibTableColumn
cefCCQueriesChecked = _CefCCQueriesChecked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 7),
    _CefCCQueriesChecked_Type()
)
cefCCQueriesChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCCQueriesChecked.setStatus("current")
_CefCCQueriesIterated_Type = Counter32
_CefCCQueriesIterated_Object = MibTableColumn
cefCCQueriesIterated = _CefCCQueriesIterated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 2, 1, 8),
    _CefCCQueriesIterated_Type()
)
cefCCQueriesIterated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefCCQueriesIterated.setStatus("current")
_CefInconsistencyRecordTable_Object = MibTable
cefInconsistencyRecordTable = _CefInconsistencyRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cefInconsistencyRecordTable.setStatus("current")
_CefInconsistencyRecordEntry_Object = MibTableRow
cefInconsistencyRecordEntry = _CefInconsistencyRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1)
)
cefInconsistencyRecordEntry.setIndexNames(
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
    (0, "CISCO-CEF-MIB", "cefInconsistencyRecId"),
)
if mibBuilder.loadTexts:
    cefInconsistencyRecordEntry.setStatus("current")


class _CefInconsistencyRecId_Type(Integer32):
    """Custom type cefInconsistencyRecId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CefInconsistencyRecId_Type.__name__ = "Integer32"
_CefInconsistencyRecId_Object = MibTableColumn
cefInconsistencyRecId = _CefInconsistencyRecId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 1),
    _CefInconsistencyRecId_Type()
)
cefInconsistencyRecId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefInconsistencyRecId.setStatus("current")
_CefInconsistencyPrefixType_Type = InetAddressType
_CefInconsistencyPrefixType_Object = MibTableColumn
cefInconsistencyPrefixType = _CefInconsistencyPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 2),
    _CefInconsistencyPrefixType_Type()
)
cefInconsistencyPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyPrefixType.setStatus("current")
_CefInconsistencyPrefixAddr_Type = InetAddress
_CefInconsistencyPrefixAddr_Object = MibTableColumn
cefInconsistencyPrefixAddr = _CefInconsistencyPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 3),
    _CefInconsistencyPrefixAddr_Type()
)
cefInconsistencyPrefixAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyPrefixAddr.setStatus("current")
_CefInconsistencyPrefixLen_Type = InetAddressPrefixLength
_CefInconsistencyPrefixLen_Object = MibTableColumn
cefInconsistencyPrefixLen = _CefInconsistencyPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 4),
    _CefInconsistencyPrefixLen_Type()
)
cefInconsistencyPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyPrefixLen.setStatus("current")
_CefInconsistencyVrfName_Type = MplsVpnId
_CefInconsistencyVrfName_Object = MibTableColumn
cefInconsistencyVrfName = _CefInconsistencyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 5),
    _CefInconsistencyVrfName_Type()
)
cefInconsistencyVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyVrfName.setStatus("current")
_CefInconsistencyCCType_Type = CefCCType
_CefInconsistencyCCType_Object = MibTableColumn
cefInconsistencyCCType = _CefInconsistencyCCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 6),
    _CefInconsistencyCCType_Type()
)
cefInconsistencyCCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyCCType.setStatus("current")
_CefInconsistencyEntity_Type = EntPhysicalIndexOrZero
_CefInconsistencyEntity_Object = MibTableColumn
cefInconsistencyEntity = _CefInconsistencyEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 7),
    _CefInconsistencyEntity_Type()
)
cefInconsistencyEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyEntity.setStatus("current")


class _CefInconsistencyReason_Type(Integer32):
    """Custom type cefInconsistencyReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checksumErr", 2),
          ("missing", 1),
          ("unknown", 3))
    )


_CefInconsistencyReason_Type.__name__ = "Integer32"
_CefInconsistencyReason_Object = MibTableColumn
cefInconsistencyReason = _CefInconsistencyReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 3, 1, 8),
    _CefInconsistencyReason_Type()
)
cefInconsistencyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyReason.setStatus("current")
_EntLastInconsistencyDetectTime_Type = TimeStamp
_EntLastInconsistencyDetectTime_Object = MibScalar
entLastInconsistencyDetectTime = _EntLastInconsistencyDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 4),
    _EntLastInconsistencyDetectTime_Type()
)
entLastInconsistencyDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLastInconsistencyDetectTime.setStatus("current")


class _CefInconsistencyReset_Type(CefCCAction):
    """Custom type cefInconsistencyReset based on CefCCAction"""


_CefInconsistencyReset_Object = MibScalar
cefInconsistencyReset = _CefInconsistencyReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 5),
    _CefInconsistencyReset_Type()
)
cefInconsistencyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefInconsistencyReset.setStatus("current")
_CefInconsistencyResetStatus_Type = CefCCStatus
_CefInconsistencyResetStatus_Object = MibScalar
cefInconsistencyResetStatus = _CefInconsistencyResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 7, 6),
    _CefInconsistencyResetStatus_Type()
)
cefInconsistencyResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefInconsistencyResetStatus.setStatus("current")
_CefStats_ObjectIdentity = ObjectIdentity
cefStats = _CefStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8)
)
_CefStatsPrefixLenTable_Object = MibTable
cefStatsPrefixLenTable = _CefStatsPrefixLenTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cefStatsPrefixLenTable.setStatus("current")
_CefStatsPrefixLenEntry_Object = MibTableRow
cefStatsPrefixLenEntry = _CefStatsPrefixLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1)
)
cefStatsPrefixLenEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
    (0, "CISCO-CEF-MIB", "cefStatsPrefixLen"),
)
if mibBuilder.loadTexts:
    cefStatsPrefixLenEntry.setStatus("current")
_CefStatsPrefixLen_Type = InetAddressPrefixLength
_CefStatsPrefixLen_Object = MibTableColumn
cefStatsPrefixLen = _CefStatsPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 1),
    _CefStatsPrefixLen_Type()
)
cefStatsPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefStatsPrefixLen.setStatus("current")
_CefStatsPrefixQueries_Type = Counter32
_CefStatsPrefixQueries_Object = MibTableColumn
cefStatsPrefixQueries = _CefStatsPrefixQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 2),
    _CefStatsPrefixQueries_Type()
)
cefStatsPrefixQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixQueries.setStatus("current")
_CefStatsPrefixHCQueries_Type = Counter64
_CefStatsPrefixHCQueries_Object = MibTableColumn
cefStatsPrefixHCQueries = _CefStatsPrefixHCQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 3),
    _CefStatsPrefixHCQueries_Type()
)
cefStatsPrefixHCQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixHCQueries.setStatus("current")
_CefStatsPrefixInserts_Type = Counter32
_CefStatsPrefixInserts_Object = MibTableColumn
cefStatsPrefixInserts = _CefStatsPrefixInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 4),
    _CefStatsPrefixInserts_Type()
)
cefStatsPrefixInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixInserts.setStatus("current")
_CefStatsPrefixHCInserts_Type = Counter64
_CefStatsPrefixHCInserts_Object = MibTableColumn
cefStatsPrefixHCInserts = _CefStatsPrefixHCInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 5),
    _CefStatsPrefixHCInserts_Type()
)
cefStatsPrefixHCInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixHCInserts.setStatus("current")
_CefStatsPrefixDeletes_Type = Counter32
_CefStatsPrefixDeletes_Object = MibTableColumn
cefStatsPrefixDeletes = _CefStatsPrefixDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 6),
    _CefStatsPrefixDeletes_Type()
)
cefStatsPrefixDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixDeletes.setStatus("current")
_CefStatsPrefixHCDeletes_Type = Counter64
_CefStatsPrefixHCDeletes_Object = MibTableColumn
cefStatsPrefixHCDeletes = _CefStatsPrefixHCDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 7),
    _CefStatsPrefixHCDeletes_Type()
)
cefStatsPrefixHCDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixHCDeletes.setStatus("current")
_CefStatsPrefixElements_Type = Gauge32
_CefStatsPrefixElements_Object = MibTableColumn
cefStatsPrefixElements = _CefStatsPrefixElements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 8),
    _CefStatsPrefixElements_Type()
)
cefStatsPrefixElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixElements.setStatus("current")
_CefStatsPrefixHCElements_Type = CounterBasedGauge64
_CefStatsPrefixHCElements_Object = MibTableColumn
cefStatsPrefixHCElements = _CefStatsPrefixHCElements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 1, 1, 9),
    _CefStatsPrefixHCElements_Type()
)
cefStatsPrefixHCElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefStatsPrefixHCElements.setStatus("current")
_CefSwitchingStatsTable_Object = MibTable
cefSwitchingStatsTable = _CefSwitchingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cefSwitchingStatsTable.setStatus("current")
_CefSwitchingStatsEntry_Object = MibTableRow
cefSwitchingStatsEntry = _CefSwitchingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1)
)
cefSwitchingStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CEF-MIB", "cefFIBIpVersion"),
    (0, "CISCO-CEF-MIB", "cefSwitchingIndex"),
)
if mibBuilder.loadTexts:
    cefSwitchingStatsEntry.setStatus("current")


class _CefSwitchingIndex_Type(Integer32):
    """Custom type cefSwitchingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CefSwitchingIndex_Type.__name__ = "Integer32"
_CefSwitchingIndex_Object = MibTableColumn
cefSwitchingIndex = _CefSwitchingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 1),
    _CefSwitchingIndex_Type()
)
cefSwitchingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefSwitchingIndex.setStatus("current")


class _CefSwitchingPath_Type(SnmpAdminString):
    """Custom type cefSwitchingPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CefSwitchingPath_Type.__name__ = "SnmpAdminString"
_CefSwitchingPath_Object = MibTableColumn
cefSwitchingPath = _CefSwitchingPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 2),
    _CefSwitchingPath_Type()
)
cefSwitchingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingPath.setStatus("current")
_CefSwitchingDrop_Type = Counter32
_CefSwitchingDrop_Object = MibTableColumn
cefSwitchingDrop = _CefSwitchingDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 3),
    _CefSwitchingDrop_Type()
)
cefSwitchingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingDrop.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingDrop.setUnits("packets")
_CefSwitchingHCDrop_Type = Counter64
_CefSwitchingHCDrop_Object = MibTableColumn
cefSwitchingHCDrop = _CefSwitchingHCDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 4),
    _CefSwitchingHCDrop_Type()
)
cefSwitchingHCDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingHCDrop.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingHCDrop.setUnits("packets")
_CefSwitchingPunt_Type = Counter32
_CefSwitchingPunt_Object = MibTableColumn
cefSwitchingPunt = _CefSwitchingPunt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 5),
    _CefSwitchingPunt_Type()
)
cefSwitchingPunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingPunt.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingPunt.setUnits("packets")
_CefSwitchingHCPunt_Type = Counter64
_CefSwitchingHCPunt_Object = MibTableColumn
cefSwitchingHCPunt = _CefSwitchingHCPunt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 6),
    _CefSwitchingHCPunt_Type()
)
cefSwitchingHCPunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingHCPunt.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingHCPunt.setUnits("packets")
_CefSwitchingPunt2Host_Type = Counter32
_CefSwitchingPunt2Host_Object = MibTableColumn
cefSwitchingPunt2Host = _CefSwitchingPunt2Host_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 7),
    _CefSwitchingPunt2Host_Type()
)
cefSwitchingPunt2Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingPunt2Host.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingPunt2Host.setUnits("packets")
_CefSwitchingHCPunt2Host_Type = Counter64
_CefSwitchingHCPunt2Host_Object = MibTableColumn
cefSwitchingHCPunt2Host = _CefSwitchingHCPunt2Host_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 8, 2, 1, 8),
    _CefSwitchingHCPunt2Host_Type()
)
cefSwitchingHCPunt2Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefSwitchingHCPunt2Host.setStatus("current")
if mibBuilder.loadTexts:
    cefSwitchingHCPunt2Host.setUnits("packets")
_CefNotifCntl_ObjectIdentity = ObjectIdentity
cefNotifCntl = _CefNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9)
)
_CefResourceFailureNotifEnable_Type = TruthValue
_CefResourceFailureNotifEnable_Object = MibScalar
cefResourceFailureNotifEnable = _CefResourceFailureNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9, 1),
    _CefResourceFailureNotifEnable_Type()
)
cefResourceFailureNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefResourceFailureNotifEnable.setStatus("current")
_CefPeerStateChangeNotifEnable_Type = TruthValue
_CefPeerStateChangeNotifEnable_Object = MibScalar
cefPeerStateChangeNotifEnable = _CefPeerStateChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9, 2),
    _CefPeerStateChangeNotifEnable_Type()
)
cefPeerStateChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefPeerStateChangeNotifEnable.setStatus("current")
_CefPeerFIBStateChangeNotifEnable_Type = TruthValue
_CefPeerFIBStateChangeNotifEnable_Object = MibScalar
cefPeerFIBStateChangeNotifEnable = _CefPeerFIBStateChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9, 3),
    _CefPeerFIBStateChangeNotifEnable_Type()
)
cefPeerFIBStateChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefPeerFIBStateChangeNotifEnable.setStatus("current")


class _CefNotifThrottlingInterval_Type(Integer32):
    """Custom type cefNotifThrottlingInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_CefNotifThrottlingInterval_Type.__name__ = "Integer32"
_CefNotifThrottlingInterval_Object = MibScalar
cefNotifThrottlingInterval = _CefNotifThrottlingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9, 4),
    _CefNotifThrottlingInterval_Type()
)
cefNotifThrottlingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefNotifThrottlingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cefNotifThrottlingInterval.setUnits("seconds")
_CefInconsistencyNotifEnable_Type = TruthValue
_CefInconsistencyNotifEnable_Object = MibScalar
cefInconsistencyNotifEnable = _CefInconsistencyNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 1, 9, 5),
    _CefInconsistencyNotifEnable_Type()
)
cefInconsistencyNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefInconsistencyNotifEnable.setStatus("current")
_CiscoCefMIBConform_ObjectIdentity = ObjectIdentity
ciscoCefMIBConform = _CiscoCefMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2)
)
_CefMIBGroups_ObjectIdentity = ObjectIdentity
cefMIBGroups = _CefMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1)
)
_CefMIBCompliances_ObjectIdentity = ObjectIdentity
cefMIBCompliances = _CefMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 2)
)

# Managed Objects groups

cefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1, 1)
)
cefGroup.setObjects(
      *(("CISCO-CEF-MIB", "cefFIBSummaryFwdPrefixes"),
        ("CISCO-CEF-MIB", "cefPrefixForwardingInfo"),
        ("CISCO-CEF-MIB", "cefPrefixPkts"),
        ("CISCO-CEF-MIB", "cefPrefixBytes"),
        ("CISCO-CEF-MIB", "cefPrefixInternalNRPkts"),
        ("CISCO-CEF-MIB", "cefPrefixInternalNRBytes"),
        ("CISCO-CEF-MIB", "cefPrefixExternalNRPkts"),
        ("CISCO-CEF-MIB", "cefPrefixExternalNRBytes"),
        ("CISCO-CEF-MIB", "cefLMPrefixSpinLock"),
        ("CISCO-CEF-MIB", "cefLMPrefixState"),
        ("CISCO-CEF-MIB", "cefLMPrefixAddr"),
        ("CISCO-CEF-MIB", "cefLMPrefixLen"),
        ("CISCO-CEF-MIB", "cefLMPrefixRowStatus"),
        ("CISCO-CEF-MIB", "cefPathType"),
        ("CISCO-CEF-MIB", "cefPathInterface"),
        ("CISCO-CEF-MIB", "cefPathNextHopAddr"),
        ("CISCO-CEF-MIB", "cefPathRecurseVrfName"),
        ("CISCO-CEF-MIB", "cefAdjSummaryComplete"),
        ("CISCO-CEF-MIB", "cefAdjSummaryIncomplete"),
        ("CISCO-CEF-MIB", "cefAdjSummaryFixup"),
        ("CISCO-CEF-MIB", "cefAdjSummaryRedirect"),
        ("CISCO-CEF-MIB", "cefAdjSource"),
        ("CISCO-CEF-MIB", "cefAdjEncap"),
        ("CISCO-CEF-MIB", "cefAdjFixup"),
        ("CISCO-CEF-MIB", "cefAdjMTU"),
        ("CISCO-CEF-MIB", "cefAdjForwardingInfo"),
        ("CISCO-CEF-MIB", "cefAdjPkts"),
        ("CISCO-CEF-MIB", "cefAdjBytes"),
        ("CISCO-CEF-MIB", "cefFESelectionSpecial"),
        ("CISCO-CEF-MIB", "cefFESelectionLabels"),
        ("CISCO-CEF-MIB", "cefFESelectionAdjLinkType"),
        ("CISCO-CEF-MIB", "cefFESelectionAdjInterface"),
        ("CISCO-CEF-MIB", "cefFESelectionAdjNextHopAddrType"),
        ("CISCO-CEF-MIB", "cefFESelectionAdjNextHopAddr"),
        ("CISCO-CEF-MIB", "cefFESelectionAdjConnId"),
        ("CISCO-CEF-MIB", "cefFESelectionVrfName"),
        ("CISCO-CEF-MIB", "cefFESelectionWeight"),
        ("CISCO-CEF-MIB", "cefCfgAdminState"),
        ("CISCO-CEF-MIB", "cefCfgOperState"),
        ("CISCO-CEF-MIB", "cefCfgAccountingMap"),
        ("CISCO-CEF-MIB", "cefCfgLoadSharingAlgorithm"),
        ("CISCO-CEF-MIB", "cefCfgLoadSharingID"),
        ("CISCO-CEF-MIB", "cefCfgTrafficStatsLoadInterval"),
        ("CISCO-CEF-MIB", "cefCfgTrafficStatsUpdateRate"),
        ("CISCO-CEF-MIB", "cefResourceMemoryUsed"),
        ("CISCO-CEF-MIB", "cefResourceFailureReason"),
        ("CISCO-CEF-MIB", "cefIntSwitchingState"),
        ("CISCO-CEF-MIB", "cefIntLoadSharing"),
        ("CISCO-CEF-MIB", "cefIntNonrecursiveAccouting"),
        ("CISCO-CEF-MIB", "cefStatsPrefixQueries"),
        ("CISCO-CEF-MIB", "cefStatsPrefixInserts"),
        ("CISCO-CEF-MIB", "cefStatsPrefixDeletes"),
        ("CISCO-CEF-MIB", "cefStatsPrefixElements"),
        ("CISCO-CEF-MIB", "cefSwitchingPath"),
        ("CISCO-CEF-MIB", "cefSwitchingDrop"),
        ("CISCO-CEF-MIB", "cefSwitchingPunt"),
        ("CISCO-CEF-MIB", "cefSwitchingPunt2Host"))
)
if mibBuilder.loadTexts:
    cefGroup.setStatus("current")

cefDistributedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1, 2)
)
cefDistributedGroup.setObjects(
      *(("CISCO-CEF-MIB", "cefCfgDistributionAdminState"),
        ("CISCO-CEF-MIB", "cefCfgDistributionOperState"),
        ("CISCO-CEF-MIB", "cefPeerOperState"),
        ("CISCO-CEF-MIB", "cefPeerNumberOfResets"),
        ("CISCO-CEF-MIB", "cefPeerFIBOperState"),
        ("CISCO-CEF-MIB", "cefCCGlobalAutoRepairEnabled"),
        ("CISCO-CEF-MIB", "cefCCGlobalAutoRepairDelay"),
        ("CISCO-CEF-MIB", "cefCCGlobalAutoRepairHoldDown"),
        ("CISCO-CEF-MIB", "cefCCGlobalErrorMsgEnabled"),
        ("CISCO-CEF-MIB", "cefCCGlobalFullScanStatus"),
        ("CISCO-CEF-MIB", "cefCCGlobalFullScanAction"),
        ("CISCO-CEF-MIB", "cefCCEnabled"),
        ("CISCO-CEF-MIB", "cefCCCount"),
        ("CISCO-CEF-MIB", "cefCCPeriod"),
        ("CISCO-CEF-MIB", "cefCCQueriesSent"),
        ("CISCO-CEF-MIB", "cefCCQueriesIgnored"),
        ("CISCO-CEF-MIB", "cefCCQueriesChecked"),
        ("CISCO-CEF-MIB", "cefCCQueriesIterated"),
        ("CISCO-CEF-MIB", "entLastInconsistencyDetectTime"),
        ("CISCO-CEF-MIB", "cefInconsistencyPrefixType"),
        ("CISCO-CEF-MIB", "cefInconsistencyPrefixAddr"),
        ("CISCO-CEF-MIB", "cefInconsistencyPrefixLen"),
        ("CISCO-CEF-MIB", "cefInconsistencyVrfName"),
        ("CISCO-CEF-MIB", "cefInconsistencyCCType"),
        ("CISCO-CEF-MIB", "cefInconsistencyEntity"),
        ("CISCO-CEF-MIB", "cefInconsistencyReason"),
        ("CISCO-CEF-MIB", "cefInconsistencyReset"),
        ("CISCO-CEF-MIB", "cefInconsistencyResetStatus"))
)
if mibBuilder.loadTexts:
    cefDistributedGroup.setStatus("current")

cefHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1, 3)
)
cefHCStatsGroup.setObjects(
      *(("CISCO-CEF-MIB", "cefPrefixHCPkts"),
        ("CISCO-CEF-MIB", "cefPrefixHCBytes"),
        ("CISCO-CEF-MIB", "cefPrefixInternalNRHCPkts"),
        ("CISCO-CEF-MIB", "cefPrefixInternalNRHCBytes"),
        ("CISCO-CEF-MIB", "cefPrefixExternalNRHCPkts"),
        ("CISCO-CEF-MIB", "cefPrefixExternalNRHCBytes"),
        ("CISCO-CEF-MIB", "cefAdjHCPkts"),
        ("CISCO-CEF-MIB", "cefAdjHCBytes"),
        ("CISCO-CEF-MIB", "cefStatsPrefixHCQueries"),
        ("CISCO-CEF-MIB", "cefStatsPrefixHCInserts"),
        ("CISCO-CEF-MIB", "cefStatsPrefixHCDeletes"),
        ("CISCO-CEF-MIB", "cefStatsPrefixHCElements"),
        ("CISCO-CEF-MIB", "cefSwitchingHCDrop"),
        ("CISCO-CEF-MIB", "cefSwitchingHCPunt"),
        ("CISCO-CEF-MIB", "cefSwitchingHCPunt2Host"))
)
if mibBuilder.loadTexts:
    cefHCStatsGroup.setStatus("current")

cefNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1, 5)
)
cefNotifCntlGroup.setObjects(
      *(("CISCO-CEF-MIB", "cefResourceFailureNotifEnable"),
        ("CISCO-CEF-MIB", "cefPeerStateChangeNotifEnable"),
        ("CISCO-CEF-MIB", "cefPeerFIBStateChangeNotifEnable"),
        ("CISCO-CEF-MIB", "cefNotifThrottlingInterval"),
        ("CISCO-CEF-MIB", "cefInconsistencyNotifEnable"))
)
if mibBuilder.loadTexts:
    cefNotifCntlGroup.setStatus("current")


# Notification objects

cefResourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 0, 1)
)
cefResourceFailure.setObjects(
    ("CISCO-CEF-MIB", "cefResourceFailureReason")
)
if mibBuilder.loadTexts:
    cefResourceFailure.setStatus(
        "current"
    )

cefPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 0, 2)
)
cefPeerStateChange.setObjects(
    ("CISCO-CEF-MIB", "cefPeerOperState")
)
if mibBuilder.loadTexts:
    cefPeerStateChange.setStatus(
        "current"
    )

cefPeerFIBStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 0, 3)
)
cefPeerFIBStateChange.setObjects(
    ("CISCO-CEF-MIB", "cefPeerFIBOperState")
)
if mibBuilder.loadTexts:
    cefPeerFIBStateChange.setStatus(
        "current"
    )

cefInconsistencyDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 0, 4)
)
cefInconsistencyDetection.setObjects(
    ("CISCO-CEF-MIB", "entLastInconsistencyDetectTime")
)
if mibBuilder.loadTexts:
    cefInconsistencyDetection.setStatus(
        "current"
    )


# Notifications groups

cefNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 1, 6)
)
cefNotificationGroup.setObjects(
      *(("CISCO-CEF-MIB", "cefResourceFailure"),
        ("CISCO-CEF-MIB", "cefPeerStateChange"),
        ("CISCO-CEF-MIB", "cefPeerFIBStateChange"),
        ("CISCO-CEF-MIB", "cefInconsistencyDetection"))
)
if mibBuilder.loadTexts:
    cefNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cefMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 492, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cefMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CEF-MIB",
    **{"ciscoCefMIB": ciscoCefMIB,
       "ciscoCefMIBNotifs": ciscoCefMIBNotifs,
       "cefResourceFailure": cefResourceFailure,
       "cefPeerStateChange": cefPeerStateChange,
       "cefPeerFIBStateChange": cefPeerFIBStateChange,
       "cefInconsistencyDetection": cefInconsistencyDetection,
       "ciscoCefMIBObjects": ciscoCefMIBObjects,
       "cefFIB": cefFIB,
       "cefFIBSummary": cefFIBSummary,
       "cefFIBSummaryTable": cefFIBSummaryTable,
       "cefFIBSummaryEntry": cefFIBSummaryEntry,
       "cefFIBIpVersion": cefFIBIpVersion,
       "cefFIBSummaryFwdPrefixes": cefFIBSummaryFwdPrefixes,
       "cefPrefixTable": cefPrefixTable,
       "cefPrefixEntry": cefPrefixEntry,
       "cefPrefixType": cefPrefixType,
       "cefPrefixAddr": cefPrefixAddr,
       "cefPrefixLen": cefPrefixLen,
       "cefPrefixForwardingInfo": cefPrefixForwardingInfo,
       "cefPrefixPkts": cefPrefixPkts,
       "cefPrefixHCPkts": cefPrefixHCPkts,
       "cefPrefixBytes": cefPrefixBytes,
       "cefPrefixHCBytes": cefPrefixHCBytes,
       "cefPrefixInternalNRPkts": cefPrefixInternalNRPkts,
       "cefPrefixInternalNRHCPkts": cefPrefixInternalNRHCPkts,
       "cefPrefixInternalNRBytes": cefPrefixInternalNRBytes,
       "cefPrefixInternalNRHCBytes": cefPrefixInternalNRHCBytes,
       "cefPrefixExternalNRPkts": cefPrefixExternalNRPkts,
       "cefPrefixExternalNRHCPkts": cefPrefixExternalNRHCPkts,
       "cefPrefixExternalNRBytes": cefPrefixExternalNRBytes,
       "cefPrefixExternalNRHCBytes": cefPrefixExternalNRHCBytes,
       "cefLMPrefixSpinLock": cefLMPrefixSpinLock,
       "cefLMPrefixTable": cefLMPrefixTable,
       "cefLMPrefixEntry": cefLMPrefixEntry,
       "cefLMPrefixDestAddrType": cefLMPrefixDestAddrType,
       "cefLMPrefixDestAddr": cefLMPrefixDestAddr,
       "cefLMPrefixState": cefLMPrefixState,
       "cefLMPrefixAddr": cefLMPrefixAddr,
       "cefLMPrefixLen": cefLMPrefixLen,
       "cefLMPrefixRowStatus": cefLMPrefixRowStatus,
       "cefPathTable": cefPathTable,
       "cefPathEntry": cefPathEntry,
       "cefPathId": cefPathId,
       "cefPathType": cefPathType,
       "cefPathInterface": cefPathInterface,
       "cefPathNextHopAddr": cefPathNextHopAddr,
       "cefPathRecurseVrfName": cefPathRecurseVrfName,
       "cefAdj": cefAdj,
       "cefAdjSummary": cefAdjSummary,
       "cefAdjSummaryTable": cefAdjSummaryTable,
       "cefAdjSummaryEntry": cefAdjSummaryEntry,
       "cefAdjSummaryLinkType": cefAdjSummaryLinkType,
       "cefAdjSummaryComplete": cefAdjSummaryComplete,
       "cefAdjSummaryIncomplete": cefAdjSummaryIncomplete,
       "cefAdjSummaryFixup": cefAdjSummaryFixup,
       "cefAdjSummaryRedirect": cefAdjSummaryRedirect,
       "cefAdjTable": cefAdjTable,
       "cefAdjEntry": cefAdjEntry,
       "cefAdjNextHopAddrType": cefAdjNextHopAddrType,
       "cefAdjNextHopAddr": cefAdjNextHopAddr,
       "cefAdjConnId": cefAdjConnId,
       "cefAdjSource": cefAdjSource,
       "cefAdjEncap": cefAdjEncap,
       "cefAdjFixup": cefAdjFixup,
       "cefAdjMTU": cefAdjMTU,
       "cefAdjForwardingInfo": cefAdjForwardingInfo,
       "cefAdjPkts": cefAdjPkts,
       "cefAdjHCPkts": cefAdjHCPkts,
       "cefAdjBytes": cefAdjBytes,
       "cefAdjHCBytes": cefAdjHCBytes,
       "cefFE": cefFE,
       "cefFESelectionTable": cefFESelectionTable,
       "cefFESelectionEntry": cefFESelectionEntry,
       "cefFESelectionName": cefFESelectionName,
       "cefFESelectionId": cefFESelectionId,
       "cefFESelectionSpecial": cefFESelectionSpecial,
       "cefFESelectionLabels": cefFESelectionLabels,
       "cefFESelectionAdjLinkType": cefFESelectionAdjLinkType,
       "cefFESelectionAdjInterface": cefFESelectionAdjInterface,
       "cefFESelectionAdjNextHopAddrType": cefFESelectionAdjNextHopAddrType,
       "cefFESelectionAdjNextHopAddr": cefFESelectionAdjNextHopAddr,
       "cefFESelectionAdjConnId": cefFESelectionAdjConnId,
       "cefFESelectionVrfName": cefFESelectionVrfName,
       "cefFESelectionWeight": cefFESelectionWeight,
       "cefGlobal": cefGlobal,
       "cefCfgTable": cefCfgTable,
       "cefCfgEntry": cefCfgEntry,
       "cefCfgAdminState": cefCfgAdminState,
       "cefCfgOperState": cefCfgOperState,
       "cefCfgDistributionAdminState": cefCfgDistributionAdminState,
       "cefCfgDistributionOperState": cefCfgDistributionOperState,
       "cefCfgAccountingMap": cefCfgAccountingMap,
       "cefCfgLoadSharingAlgorithm": cefCfgLoadSharingAlgorithm,
       "cefCfgLoadSharingID": cefCfgLoadSharingID,
       "cefCfgTrafficStatsLoadInterval": cefCfgTrafficStatsLoadInterval,
       "cefCfgTrafficStatsUpdateRate": cefCfgTrafficStatsUpdateRate,
       "cefResourceTable": cefResourceTable,
       "cefResourceEntry": cefResourceEntry,
       "cefResourceMemoryUsed": cefResourceMemoryUsed,
       "cefResourceFailureReason": cefResourceFailureReason,
       "cefInterface": cefInterface,
       "cefIntTable": cefIntTable,
       "cefIntEntry": cefIntEntry,
       "cefIntSwitchingState": cefIntSwitchingState,
       "cefIntLoadSharing": cefIntLoadSharing,
       "cefIntNonrecursiveAccouting": cefIntNonrecursiveAccouting,
       "cefPeer": cefPeer,
       "cefPeerTable": cefPeerTable,
       "cefPeerEntry": cefPeerEntry,
       "entPeerPhysicalIndex": entPeerPhysicalIndex,
       "cefPeerOperState": cefPeerOperState,
       "cefPeerNumberOfResets": cefPeerNumberOfResets,
       "cefPeerFIBTable": cefPeerFIBTable,
       "cefPeerFIBEntry": cefPeerFIBEntry,
       "cefPeerFIBOperState": cefPeerFIBOperState,
       "cefCC": cefCC,
       "cefCCGlobalTable": cefCCGlobalTable,
       "cefCCGlobalEntry": cefCCGlobalEntry,
       "cefCCGlobalAutoRepairEnabled": cefCCGlobalAutoRepairEnabled,
       "cefCCGlobalAutoRepairDelay": cefCCGlobalAutoRepairDelay,
       "cefCCGlobalAutoRepairHoldDown": cefCCGlobalAutoRepairHoldDown,
       "cefCCGlobalErrorMsgEnabled": cefCCGlobalErrorMsgEnabled,
       "cefCCGlobalFullScanAction": cefCCGlobalFullScanAction,
       "cefCCGlobalFullScanStatus": cefCCGlobalFullScanStatus,
       "cefCCTypeTable": cefCCTypeTable,
       "cefCCTypeEntry": cefCCTypeEntry,
       "cefCCType": cefCCType,
       "cefCCEnabled": cefCCEnabled,
       "cefCCCount": cefCCCount,
       "cefCCPeriod": cefCCPeriod,
       "cefCCQueriesSent": cefCCQueriesSent,
       "cefCCQueriesIgnored": cefCCQueriesIgnored,
       "cefCCQueriesChecked": cefCCQueriesChecked,
       "cefCCQueriesIterated": cefCCQueriesIterated,
       "cefInconsistencyRecordTable": cefInconsistencyRecordTable,
       "cefInconsistencyRecordEntry": cefInconsistencyRecordEntry,
       "cefInconsistencyRecId": cefInconsistencyRecId,
       "cefInconsistencyPrefixType": cefInconsistencyPrefixType,
       "cefInconsistencyPrefixAddr": cefInconsistencyPrefixAddr,
       "cefInconsistencyPrefixLen": cefInconsistencyPrefixLen,
       "cefInconsistencyVrfName": cefInconsistencyVrfName,
       "cefInconsistencyCCType": cefInconsistencyCCType,
       "cefInconsistencyEntity": cefInconsistencyEntity,
       "cefInconsistencyReason": cefInconsistencyReason,
       "entLastInconsistencyDetectTime": entLastInconsistencyDetectTime,
       "cefInconsistencyReset": cefInconsistencyReset,
       "cefInconsistencyResetStatus": cefInconsistencyResetStatus,
       "cefStats": cefStats,
       "cefStatsPrefixLenTable": cefStatsPrefixLenTable,
       "cefStatsPrefixLenEntry": cefStatsPrefixLenEntry,
       "cefStatsPrefixLen": cefStatsPrefixLen,
       "cefStatsPrefixQueries": cefStatsPrefixQueries,
       "cefStatsPrefixHCQueries": cefStatsPrefixHCQueries,
       "cefStatsPrefixInserts": cefStatsPrefixInserts,
       "cefStatsPrefixHCInserts": cefStatsPrefixHCInserts,
       "cefStatsPrefixDeletes": cefStatsPrefixDeletes,
       "cefStatsPrefixHCDeletes": cefStatsPrefixHCDeletes,
       "cefStatsPrefixElements": cefStatsPrefixElements,
       "cefStatsPrefixHCElements": cefStatsPrefixHCElements,
       "cefSwitchingStatsTable": cefSwitchingStatsTable,
       "cefSwitchingStatsEntry": cefSwitchingStatsEntry,
       "cefSwitchingIndex": cefSwitchingIndex,
       "cefSwitchingPath": cefSwitchingPath,
       "cefSwitchingDrop": cefSwitchingDrop,
       "cefSwitchingHCDrop": cefSwitchingHCDrop,
       "cefSwitchingPunt": cefSwitchingPunt,
       "cefSwitchingHCPunt": cefSwitchingHCPunt,
       "cefSwitchingPunt2Host": cefSwitchingPunt2Host,
       "cefSwitchingHCPunt2Host": cefSwitchingHCPunt2Host,
       "cefNotifCntl": cefNotifCntl,
       "cefResourceFailureNotifEnable": cefResourceFailureNotifEnable,
       "cefPeerStateChangeNotifEnable": cefPeerStateChangeNotifEnable,
       "cefPeerFIBStateChangeNotifEnable": cefPeerFIBStateChangeNotifEnable,
       "cefNotifThrottlingInterval": cefNotifThrottlingInterval,
       "cefInconsistencyNotifEnable": cefInconsistencyNotifEnable,
       "ciscoCefMIBConform": ciscoCefMIBConform,
       "cefMIBGroups": cefMIBGroups,
       "cefGroup": cefGroup,
       "cefDistributedGroup": cefDistributedGroup,
       "cefHCStatsGroup": cefHCStatsGroup,
       "cefNotifCntlGroup": cefNotifCntlGroup,
       "cefNotificationGroup": cefNotificationGroup,
       "cefMIBCompliances": cefMIBCompliances,
       "cefMIBCompliance": cefMIBCompliance}
)
