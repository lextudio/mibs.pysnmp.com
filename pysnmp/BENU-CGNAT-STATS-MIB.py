# SNMP MIB module (BENU-CGNAT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-CGNAT-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:49 2024
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

benuCgnatStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9)
)
benuCgnatStatsMIB.setRevisions(
        ("2017-01-24 00:00",
         "2017-01-04 00:00",
         "2016-12-22 00:00",
         "2015-01-27 00:00",
         "2014-12-10 00:00",
         "2014-11-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BCgnatNotifications_ObjectIdentity = ObjectIdentity
bCgnatNotifications = _BCgnatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0)
)
if mibBuilder.loadTexts:
    bCgnatNotifications.setStatus("current")
_BCgnatMIBObjects_ObjectIdentity = ObjectIdentity
bCgnatMIBObjects = _BCgnatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    bCgnatMIBObjects.setStatus("current")
_BCgnatAuthStatsTable_Object = MibTable
bCgnatAuthStatsTable = _BCgnatAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    bCgnatAuthStatsTable.setStatus("current")
_BCgnatAuthStatsEntry_Object = MibTableRow
bCgnatAuthStatsEntry = _BCgnatAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1)
)
bCgnatAuthStatsEntry.setIndexNames(
    (0, "BENU-CGNAT-STATS-MIB", "bCgnatAuthStatsIndex"),
)
if mibBuilder.loadTexts:
    bCgnatAuthStatsEntry.setStatus("current")
_BCgnatAuthStatsIndex_Type = Integer32
_BCgnatAuthStatsIndex_Object = MibTableColumn
bCgnatAuthStatsIndex = _BCgnatAuthStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 1),
    _BCgnatAuthStatsIndex_Type()
)
bCgnatAuthStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bCgnatAuthStatsIndex.setStatus("current")
_BCgnatAuthProfileName_Type = DisplayString
_BCgnatAuthProfileName_Object = MibTableColumn
bCgnatAuthProfileName = _BCgnatAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 2),
    _BCgnatAuthProfileName_Type()
)
bCgnatAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthProfileName.setStatus("current")
_BCgnatAuthDomainPublicIpZeroCount_Type = Counter64
_BCgnatAuthDomainPublicIpZeroCount_Object = MibTableColumn
bCgnatAuthDomainPublicIpZeroCount = _BCgnatAuthDomainPublicIpZeroCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 3),
    _BCgnatAuthDomainPublicIpZeroCount_Type()
)
bCgnatAuthDomainPublicIpZeroCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDomainPublicIpZeroCount.setStatus("current")
_BCgnatAuthDomainNoFreePortCount_Type = Counter64
_BCgnatAuthDomainNoFreePortCount_Object = MibTableColumn
bCgnatAuthDomainNoFreePortCount = _BCgnatAuthDomainNoFreePortCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 4),
    _BCgnatAuthDomainNoFreePortCount_Type()
)
bCgnatAuthDomainNoFreePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDomainNoFreePortCount.setStatus("current")
_BCgnatAuthFlowAddSuccessCount_Type = Counter64
_BCgnatAuthFlowAddSuccessCount_Object = MibTableColumn
bCgnatAuthFlowAddSuccessCount = _BCgnatAuthFlowAddSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 5),
    _BCgnatAuthFlowAddSuccessCount_Type()
)
bCgnatAuthFlowAddSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowAddSuccessCount.setStatus("current")
_BCgnatAuthFlowAddFailureCount_Type = Counter64
_BCgnatAuthFlowAddFailureCount_Object = MibTableColumn
bCgnatAuthFlowAddFailureCount = _BCgnatAuthFlowAddFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 6),
    _BCgnatAuthFlowAddFailureCount_Type()
)
bCgnatAuthFlowAddFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowAddFailureCount.setStatus("current")
_BCgnatAuthTimerAllocFailureCount_Type = Counter64
_BCgnatAuthTimerAllocFailureCount_Object = MibTableColumn
bCgnatAuthTimerAllocFailureCount = _BCgnatAuthTimerAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 7),
    _BCgnatAuthTimerAllocFailureCount_Type()
)
bCgnatAuthTimerAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthTimerAllocFailureCount.setStatus("current")
_BCgnatAuthFlowDeleteSuccessCount_Type = Counter64
_BCgnatAuthFlowDeleteSuccessCount_Object = MibTableColumn
bCgnatAuthFlowDeleteSuccessCount = _BCgnatAuthFlowDeleteSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 8),
    _BCgnatAuthFlowDeleteSuccessCount_Type()
)
bCgnatAuthFlowDeleteSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeleteSuccessCount.setStatus("current")
_BCgnatAuthFlowDeleteFailureCount_Type = Counter64
_BCgnatAuthFlowDeleteFailureCount_Object = MibTableColumn
bCgnatAuthFlowDeleteFailureCount = _BCgnatAuthFlowDeleteFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 9),
    _BCgnatAuthFlowDeleteFailureCount_Type()
)
bCgnatAuthFlowDeleteFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeleteFailureCount.setStatus("current")
_BCgnatAuthUnsupportedL4DropCount_Type = Counter64
_BCgnatAuthUnsupportedL4DropCount_Object = MibTableColumn
bCgnatAuthUnsupportedL4DropCount = _BCgnatAuthUnsupportedL4DropCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 10),
    _BCgnatAuthUnsupportedL4DropCount_Type()
)
bCgnatAuthUnsupportedL4DropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUnsupportedL4DropCount.setStatus("current")
_BCgnatAuthNatflowSyncFailureCount_Type = Counter64
_BCgnatAuthNatflowSyncFailureCount_Object = MibTableColumn
bCgnatAuthNatflowSyncFailureCount = _BCgnatAuthNatflowSyncFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 11),
    _BCgnatAuthNatflowSyncFailureCount_Type()
)
bCgnatAuthNatflowSyncFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthNatflowSyncFailureCount.setStatus("current")
_BCgnatAuthIcmpIdAllocSuccessCount_Type = Counter64
_BCgnatAuthIcmpIdAllocSuccessCount_Object = MibTableColumn
bCgnatAuthIcmpIdAllocSuccessCount = _BCgnatAuthIcmpIdAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 12),
    _BCgnatAuthIcmpIdAllocSuccessCount_Type()
)
bCgnatAuthIcmpIdAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthIcmpIdAllocSuccessCount.setStatus("current")
_BCgnatAuthTcpPortAllocSuccessCount_Type = Counter64
_BCgnatAuthTcpPortAllocSuccessCount_Object = MibTableColumn
bCgnatAuthTcpPortAllocSuccessCount = _BCgnatAuthTcpPortAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 13),
    _BCgnatAuthTcpPortAllocSuccessCount_Type()
)
bCgnatAuthTcpPortAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthTcpPortAllocSuccessCount.setStatus("current")
_BCgnatAuthUdpPortAllocSuccessCount_Type = Counter64
_BCgnatAuthUdpPortAllocSuccessCount_Object = MibTableColumn
bCgnatAuthUdpPortAllocSuccessCount = _BCgnatAuthUdpPortAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 14),
    _BCgnatAuthUdpPortAllocSuccessCount_Type()
)
bCgnatAuthUdpPortAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUdpPortAllocSuccessCount.setStatus("current")
_BCgnatAuthIcmpIdAllocFailureCount_Type = Counter64
_BCgnatAuthIcmpIdAllocFailureCount_Object = MibTableColumn
bCgnatAuthIcmpIdAllocFailureCount = _BCgnatAuthIcmpIdAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 15),
    _BCgnatAuthIcmpIdAllocFailureCount_Type()
)
bCgnatAuthIcmpIdAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthIcmpIdAllocFailureCount.setStatus("current")
_BCgnatAuthTcpPortAllocFailureCount_Type = Counter64
_BCgnatAuthTcpPortAllocFailureCount_Object = MibTableColumn
bCgnatAuthTcpPortAllocFailureCount = _BCgnatAuthTcpPortAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 16),
    _BCgnatAuthTcpPortAllocFailureCount_Type()
)
bCgnatAuthTcpPortAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthTcpPortAllocFailureCount.setStatus("current")
_BCgnatAuthUdpPortAllocFailureCount_Type = Counter64
_BCgnatAuthUdpPortAllocFailureCount_Object = MibTableColumn
bCgnatAuthUdpPortAllocFailureCount = _BCgnatAuthUdpPortAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 17),
    _BCgnatAuthUdpPortAllocFailureCount_Type()
)
bCgnatAuthUdpPortAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUdpPortAllocFailureCount.setStatus("current")
_BCgnatAuthIcmpIdReleaseSuccessCount_Type = Counter64
_BCgnatAuthIcmpIdReleaseSuccessCount_Object = MibTableColumn
bCgnatAuthIcmpIdReleaseSuccessCount = _BCgnatAuthIcmpIdReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 18),
    _BCgnatAuthIcmpIdReleaseSuccessCount_Type()
)
bCgnatAuthIcmpIdReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthIcmpIdReleaseSuccessCount.setStatus("current")
_BCgnatAuthTcpPortReleaseSuccessCount_Type = Counter64
_BCgnatAuthTcpPortReleaseSuccessCount_Object = MibTableColumn
bCgnatAuthTcpPortReleaseSuccessCount = _BCgnatAuthTcpPortReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 19),
    _BCgnatAuthTcpPortReleaseSuccessCount_Type()
)
bCgnatAuthTcpPortReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthTcpPortReleaseSuccessCount.setStatus("current")
_BCgnatAuthUdpPortReleaseSuccessCount_Type = Counter64
_BCgnatAuthUdpPortReleaseSuccessCount_Object = MibTableColumn
bCgnatAuthUdpPortReleaseSuccessCount = _BCgnatAuthUdpPortReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 20),
    _BCgnatAuthUdpPortReleaseSuccessCount_Type()
)
bCgnatAuthUdpPortReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUdpPortReleaseSuccessCount.setStatus("current")
_BCgnatAuthIcmpIdReleaseFailureCount_Type = Counter64
_BCgnatAuthIcmpIdReleaseFailureCount_Object = MibTableColumn
bCgnatAuthIcmpIdReleaseFailureCount = _BCgnatAuthIcmpIdReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 21),
    _BCgnatAuthIcmpIdReleaseFailureCount_Type()
)
bCgnatAuthIcmpIdReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthIcmpIdReleaseFailureCount.setStatus("current")
_BCgnatAuthTcpPortReleaseFailureCount_Type = Counter64
_BCgnatAuthTcpPortReleaseFailureCount_Object = MibTableColumn
bCgnatAuthTcpPortReleaseFailureCount = _BCgnatAuthTcpPortReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 22),
    _BCgnatAuthTcpPortReleaseFailureCount_Type()
)
bCgnatAuthTcpPortReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthTcpPortReleaseFailureCount.setStatus("current")
_BCgnatAuthUdpPortReleaseFailureCount_Type = Counter64
_BCgnatAuthUdpPortReleaseFailureCount_Object = MibTableColumn
bCgnatAuthUdpPortReleaseFailureCount = _BCgnatAuthUdpPortReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 23),
    _BCgnatAuthUdpPortReleaseFailureCount_Type()
)
bCgnatAuthUdpPortReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUdpPortReleaseFailureCount.setStatus("current")
_BCgnatAuthMaxCgnatPortsExceeded_Type = Counter64
_BCgnatAuthMaxCgnatPortsExceeded_Object = MibTableColumn
bCgnatAuthMaxCgnatPortsExceeded = _BCgnatAuthMaxCgnatPortsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 24),
    _BCgnatAuthMaxCgnatPortsExceeded_Type()
)
bCgnatAuthMaxCgnatPortsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthMaxCgnatPortsExceeded.setStatus("current")
_BCgnatAuthMaxIcmpIdsExceeded_Type = Counter64
_BCgnatAuthMaxIcmpIdsExceeded_Object = MibTableColumn
bCgnatAuthMaxIcmpIdsExceeded = _BCgnatAuthMaxIcmpIdsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 25),
    _BCgnatAuthMaxIcmpIdsExceeded_Type()
)
bCgnatAuthMaxIcmpIdsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthMaxIcmpIdsExceeded.setStatus("current")
_BCgnatAuthFlowDeleteRcvd_Type = Counter64
_BCgnatAuthFlowDeleteRcvd_Object = MibTableColumn
bCgnatAuthFlowDeleteRcvd = _BCgnatAuthFlowDeleteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 26),
    _BCgnatAuthFlowDeleteRcvd_Type()
)
bCgnatAuthFlowDeleteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeleteRcvd.setStatus("current")
_BCgnatAuthFlowDeleteSent_Type = Counter64
_BCgnatAuthFlowDeleteSent_Object = MibTableColumn
bCgnatAuthFlowDeleteSent = _BCgnatAuthFlowDeleteSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 27),
    _BCgnatAuthFlowDeleteSent_Type()
)
bCgnatAuthFlowDeleteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeleteSent.setStatus("current")
_BCgnatAuthFlowDeleteFindFailure_Type = Counter64
_BCgnatAuthFlowDeleteFindFailure_Object = MibTableColumn
bCgnatAuthFlowDeleteFindFailure = _BCgnatAuthFlowDeleteFindFailure_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 28),
    _BCgnatAuthFlowDeleteFindFailure_Type()
)
bCgnatAuthFlowDeleteFindFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeleteFindFailure.setStatus("current")
_BCgnatAuthDnsFlowAlloc_Type = Counter64
_BCgnatAuthDnsFlowAlloc_Object = MibTableColumn
bCgnatAuthDnsFlowAlloc = _BCgnatAuthDnsFlowAlloc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 29),
    _BCgnatAuthDnsFlowAlloc_Type()
)
bCgnatAuthDnsFlowAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowAlloc.setStatus("current")
_BCgnatAuthDnsFlowRelease_Type = Counter64
_BCgnatAuthDnsFlowRelease_Object = MibTableColumn
bCgnatAuthDnsFlowRelease = _BCgnatAuthDnsFlowRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 30),
    _BCgnatAuthDnsFlowRelease_Type()
)
bCgnatAuthDnsFlowRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowRelease.setStatus("current")
_BCgnatAuthDnsFlowAllocSuccessCount_Type = Counter64
_BCgnatAuthDnsFlowAllocSuccessCount_Object = MibTableColumn
bCgnatAuthDnsFlowAllocSuccessCount = _BCgnatAuthDnsFlowAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 31),
    _BCgnatAuthDnsFlowAllocSuccessCount_Type()
)
bCgnatAuthDnsFlowAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowAllocSuccessCount.setStatus("current")
_BCgnatAuthDnsFlowReleaseSuccessCount_Type = Counter64
_BCgnatAuthDnsFlowReleaseSuccessCount_Object = MibTableColumn
bCgnatAuthDnsFlowReleaseSuccessCount = _BCgnatAuthDnsFlowReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 32),
    _BCgnatAuthDnsFlowReleaseSuccessCount_Type()
)
bCgnatAuthDnsFlowReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowReleaseSuccessCount.setStatus("current")
_BCgnatAuthDnsFlowAllocFailureCount_Type = Counter64
_BCgnatAuthDnsFlowAllocFailureCount_Object = MibTableColumn
bCgnatAuthDnsFlowAllocFailureCount = _BCgnatAuthDnsFlowAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 33),
    _BCgnatAuthDnsFlowAllocFailureCount_Type()
)
bCgnatAuthDnsFlowAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowAllocFailureCount.setStatus("current")
_BCgnatAuthDnsFlowReleaseFailureCount_Type = Counter64
_BCgnatAuthDnsFlowReleaseFailureCount_Object = MibTableColumn
bCgnatAuthDnsFlowReleaseFailureCount = _BCgnatAuthDnsFlowReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 34),
    _BCgnatAuthDnsFlowReleaseFailureCount_Type()
)
bCgnatAuthDnsFlowReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthDnsFlowReleaseFailureCount.setStatus("current")
_BCgnatAuthPortsThresholdExceededSent_Type = Counter64
_BCgnatAuthPortsThresholdExceededSent_Object = MibTableColumn
bCgnatAuthPortsThresholdExceededSent = _BCgnatAuthPortsThresholdExceededSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 35),
    _BCgnatAuthPortsThresholdExceededSent_Type()
)
bCgnatAuthPortsThresholdExceededSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortsThresholdExceededSent.setStatus("current")
_BCgnatAuthPortsThresholdExceededRcvd_Type = Counter64
_BCgnatAuthPortsThresholdExceededRcvd_Object = MibTableColumn
bCgnatAuthPortsThresholdExceededRcvd = _BCgnatAuthPortsThresholdExceededRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 36),
    _BCgnatAuthPortsThresholdExceededRcvd_Type()
)
bCgnatAuthPortsThresholdExceededRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortsThresholdExceededRcvd.setStatus("current")
_BCgnatAuthPortsThresholdExceededInt_Type = Counter64
_BCgnatAuthPortsThresholdExceededInt_Object = MibTableColumn
bCgnatAuthPortsThresholdExceededInt = _BCgnatAuthPortsThresholdExceededInt_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 37),
    _BCgnatAuthPortsThresholdExceededInt_Type()
)
bCgnatAuthPortsThresholdExceededInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortsThresholdExceededInt.setStatus("current")
_BCgnatAuthPortsThresholdExceededErr_Type = Counter64
_BCgnatAuthPortsThresholdExceededErr_Object = MibTableColumn
bCgnatAuthPortsThresholdExceededErr = _BCgnatAuthPortsThresholdExceededErr_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 38),
    _BCgnatAuthPortsThresholdExceededErr_Type()
)
bCgnatAuthPortsThresholdExceededErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortsThresholdExceededErr.setStatus("current")
_BCgnatAuthUnsupportedActionIdRcvd_Type = Counter64
_BCgnatAuthUnsupportedActionIdRcvd_Object = MibTableColumn
bCgnatAuthUnsupportedActionIdRcvd = _BCgnatAuthUnsupportedActionIdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 39),
    _BCgnatAuthUnsupportedActionIdRcvd_Type()
)
bCgnatAuthUnsupportedActionIdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUnsupportedActionIdRcvd.setStatus("current")
_BCgnatAuthNonTcpSynPortAllocDrop_Type = Counter64
_BCgnatAuthNonTcpSynPortAllocDrop_Object = MibTableColumn
bCgnatAuthNonTcpSynPortAllocDrop = _BCgnatAuthNonTcpSynPortAllocDrop_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 40),
    _BCgnatAuthNonTcpSynPortAllocDrop_Type()
)
bCgnatAuthNonTcpSynPortAllocDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthNonTcpSynPortAllocDrop.setStatus("current")
_BCgnatAuthFlowDeletedTimer_Type = Counter64
_BCgnatAuthFlowDeletedTimer_Object = MibTableColumn
bCgnatAuthFlowDeletedTimer = _BCgnatAuthFlowDeletedTimer_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 41),
    _BCgnatAuthFlowDeletedTimer_Type()
)
bCgnatAuthFlowDeletedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeletedTimer.setStatus("current")
_BCgnatAuthFlowDeletedSessionEnded_Type = Counter64
_BCgnatAuthFlowDeletedSessionEnded_Object = MibTableColumn
bCgnatAuthFlowDeletedSessionEnded = _BCgnatAuthFlowDeletedSessionEnded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 42),
    _BCgnatAuthFlowDeletedSessionEnded_Type()
)
bCgnatAuthFlowDeletedSessionEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeletedSessionEnded.setStatus("current")
_BCgnatAuthFlowDeletedSubClear_Type = Counter64
_BCgnatAuthFlowDeletedSubClear_Object = MibTableColumn
bCgnatAuthFlowDeletedSubClear = _BCgnatAuthFlowDeletedSubClear_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 43),
    _BCgnatAuthFlowDeletedSubClear_Type()
)
bCgnatAuthFlowDeletedSubClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthFlowDeletedSubClear.setStatus("current")
_BCgnatAuthNatFlowDelErrSubIdMismatch_Type = Counter64
_BCgnatAuthNatFlowDelErrSubIdMismatch_Object = MibTableColumn
bCgnatAuthNatFlowDelErrSubIdMismatch = _BCgnatAuthNatFlowDelErrSubIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 44),
    _BCgnatAuthNatFlowDelErrSubIdMismatch_Type()
)
bCgnatAuthNatFlowDelErrSubIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthNatFlowDelErrSubIdMismatch.setStatus("current")
_BCgnatAuthNatFlowDelErrValidFlagNotSet_Type = Counter64
_BCgnatAuthNatFlowDelErrValidFlagNotSet_Object = MibTableColumn
bCgnatAuthNatFlowDelErrValidFlagNotSet = _BCgnatAuthNatFlowDelErrValidFlagNotSet_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 45),
    _BCgnatAuthNatFlowDelErrValidFlagNotSet_Type()
)
bCgnatAuthNatFlowDelErrValidFlagNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthNatFlowDelErrValidFlagNotSet.setStatus("current")
_BCgnatAuthIcmpPortUnreachableSent_Type = Counter64
_BCgnatAuthIcmpPortUnreachableSent_Object = MibTableColumn
bCgnatAuthIcmpPortUnreachableSent = _BCgnatAuthIcmpPortUnreachableSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 46),
    _BCgnatAuthIcmpPortUnreachableSent_Type()
)
bCgnatAuthIcmpPortUnreachableSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthIcmpPortUnreachableSent.setStatus("current")
_BCgnatAuthPortsNotAvailableDrop_Type = Counter64
_BCgnatAuthPortsNotAvailableDrop_Object = MibTableColumn
bCgnatAuthPortsNotAvailableDrop = _BCgnatAuthPortsNotAvailableDrop_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 47),
    _BCgnatAuthPortsNotAvailableDrop_Type()
)
bCgnatAuthPortsNotAvailableDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortsNotAvailableDrop.setStatus("current")
_BCgnatAuthUnsupportedPrivatePortDropCount_Type = Counter64
_BCgnatAuthUnsupportedPrivatePortDropCount_Object = MibTableColumn
bCgnatAuthUnsupportedPrivatePortDropCount = _BCgnatAuthUnsupportedPrivatePortDropCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 48),
    _BCgnatAuthUnsupportedPrivatePortDropCount_Type()
)
bCgnatAuthUnsupportedPrivatePortDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthUnsupportedPrivatePortDropCount.setStatus("current")
_BCgnatUnauthStatsTable_Object = MibTable
bCgnatUnauthStatsTable = _BCgnatUnauthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    bCgnatUnauthStatsTable.setStatus("current")
_BCgnatUnauthStatsEntry_Object = MibTableRow
bCgnatUnauthStatsEntry = _BCgnatUnauthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1)
)
bCgnatUnauthStatsEntry.setIndexNames(
    (0, "BENU-CGNAT-STATS-MIB", "bCgnatUnauthStatsIndex"),
)
if mibBuilder.loadTexts:
    bCgnatUnauthStatsEntry.setStatus("current")
_BCgnatUnauthStatsIndex_Type = Integer32
_BCgnatUnauthStatsIndex_Object = MibTableColumn
bCgnatUnauthStatsIndex = _BCgnatUnauthStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 1),
    _BCgnatUnauthStatsIndex_Type()
)
bCgnatUnauthStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bCgnatUnauthStatsIndex.setStatus("current")
_BCgnatUnauthProfileName_Type = DisplayString
_BCgnatUnauthProfileName_Object = MibTableColumn
bCgnatUnauthProfileName = _BCgnatUnauthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 2),
    _BCgnatUnauthProfileName_Type()
)
bCgnatUnauthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthProfileName.setStatus("current")
_BCgnatUnauthDomainPublicIpZeroCount_Type = Counter64
_BCgnatUnauthDomainPublicIpZeroCount_Object = MibTableColumn
bCgnatUnauthDomainPublicIpZeroCount = _BCgnatUnauthDomainPublicIpZeroCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 3),
    _BCgnatUnauthDomainPublicIpZeroCount_Type()
)
bCgnatUnauthDomainPublicIpZeroCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDomainPublicIpZeroCount.setStatus("current")
_BCgnatUnauthDomainNoFreePortCount_Type = Counter64
_BCgnatUnauthDomainNoFreePortCount_Object = MibTableColumn
bCgnatUnauthDomainNoFreePortCount = _BCgnatUnauthDomainNoFreePortCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 4),
    _BCgnatUnauthDomainNoFreePortCount_Type()
)
bCgnatUnauthDomainNoFreePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDomainNoFreePortCount.setStatus("current")
_BCgnatUnauthFlowAddSuccessCount_Type = Counter64
_BCgnatUnauthFlowAddSuccessCount_Object = MibTableColumn
bCgnatUnauthFlowAddSuccessCount = _BCgnatUnauthFlowAddSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 5),
    _BCgnatUnauthFlowAddSuccessCount_Type()
)
bCgnatUnauthFlowAddSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowAddSuccessCount.setStatus("current")
_BCgnatUnauthFlowAddFailureCount_Type = Counter64
_BCgnatUnauthFlowAddFailureCount_Object = MibTableColumn
bCgnatUnauthFlowAddFailureCount = _BCgnatUnauthFlowAddFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 6),
    _BCgnatUnauthFlowAddFailureCount_Type()
)
bCgnatUnauthFlowAddFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowAddFailureCount.setStatus("current")
_BCgnatUnauthTimerAllocFailureCount_Type = Counter64
_BCgnatUnauthTimerAllocFailureCount_Object = MibTableColumn
bCgnatUnauthTimerAllocFailureCount = _BCgnatUnauthTimerAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 7),
    _BCgnatUnauthTimerAllocFailureCount_Type()
)
bCgnatUnauthTimerAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthTimerAllocFailureCount.setStatus("current")
_BCgnatUnauthFlowDeleteSuccessCount_Type = Counter64
_BCgnatUnauthFlowDeleteSuccessCount_Object = MibTableColumn
bCgnatUnauthFlowDeleteSuccessCount = _BCgnatUnauthFlowDeleteSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 8),
    _BCgnatUnauthFlowDeleteSuccessCount_Type()
)
bCgnatUnauthFlowDeleteSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeleteSuccessCount.setStatus("current")
_BCgnatUnauthFlowDeleteFailureCount_Type = Counter64
_BCgnatUnauthFlowDeleteFailureCount_Object = MibTableColumn
bCgnatUnauthFlowDeleteFailureCount = _BCgnatUnauthFlowDeleteFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 9),
    _BCgnatUnauthFlowDeleteFailureCount_Type()
)
bCgnatUnauthFlowDeleteFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeleteFailureCount.setStatus("current")
_BCgnatUnauthUnsupportedL4DropCount_Type = Counter64
_BCgnatUnauthUnsupportedL4DropCount_Object = MibTableColumn
bCgnatUnauthUnsupportedL4DropCount = _BCgnatUnauthUnsupportedL4DropCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 10),
    _BCgnatUnauthUnsupportedL4DropCount_Type()
)
bCgnatUnauthUnsupportedL4DropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUnsupportedL4DropCount.setStatus("current")
_BCgnatUnauthNatflowSyncFailureCount_Type = Counter64
_BCgnatUnauthNatflowSyncFailureCount_Object = MibTableColumn
bCgnatUnauthNatflowSyncFailureCount = _BCgnatUnauthNatflowSyncFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 11),
    _BCgnatUnauthNatflowSyncFailureCount_Type()
)
bCgnatUnauthNatflowSyncFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthNatflowSyncFailureCount.setStatus("current")
_BCgnatUnauthIcmpIdAllocSuccessCount_Type = Counter64
_BCgnatUnauthIcmpIdAllocSuccessCount_Object = MibTableColumn
bCgnatUnauthIcmpIdAllocSuccessCount = _BCgnatUnauthIcmpIdAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 12),
    _BCgnatUnauthIcmpIdAllocSuccessCount_Type()
)
bCgnatUnauthIcmpIdAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthIcmpIdAllocSuccessCount.setStatus("current")
_BCgnatUnauthTcpPortAllocSuccessCount_Type = Counter64
_BCgnatUnauthTcpPortAllocSuccessCount_Object = MibTableColumn
bCgnatUnauthTcpPortAllocSuccessCount = _BCgnatUnauthTcpPortAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 13),
    _BCgnatUnauthTcpPortAllocSuccessCount_Type()
)
bCgnatUnauthTcpPortAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthTcpPortAllocSuccessCount.setStatus("current")
_BCgnatUnauthUdpPortAllocSuccessCount_Type = Counter64
_BCgnatUnauthUdpPortAllocSuccessCount_Object = MibTableColumn
bCgnatUnauthUdpPortAllocSuccessCount = _BCgnatUnauthUdpPortAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 14),
    _BCgnatUnauthUdpPortAllocSuccessCount_Type()
)
bCgnatUnauthUdpPortAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUdpPortAllocSuccessCount.setStatus("current")
_BCgnatUnauthIcmpIdAllocFailureCount_Type = Counter64
_BCgnatUnauthIcmpIdAllocFailureCount_Object = MibTableColumn
bCgnatUnauthIcmpIdAllocFailureCount = _BCgnatUnauthIcmpIdAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 15),
    _BCgnatUnauthIcmpIdAllocFailureCount_Type()
)
bCgnatUnauthIcmpIdAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthIcmpIdAllocFailureCount.setStatus("current")
_BCgnatUnauthTcpPortAllocFailureCount_Type = Counter64
_BCgnatUnauthTcpPortAllocFailureCount_Object = MibTableColumn
bCgnatUnauthTcpPortAllocFailureCount = _BCgnatUnauthTcpPortAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 16),
    _BCgnatUnauthTcpPortAllocFailureCount_Type()
)
bCgnatUnauthTcpPortAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthTcpPortAllocFailureCount.setStatus("current")
_BCgnatUnauthUdpPortAllocFailureCount_Type = Counter64
_BCgnatUnauthUdpPortAllocFailureCount_Object = MibTableColumn
bCgnatUnauthUdpPortAllocFailureCount = _BCgnatUnauthUdpPortAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 17),
    _BCgnatUnauthUdpPortAllocFailureCount_Type()
)
bCgnatUnauthUdpPortAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUdpPortAllocFailureCount.setStatus("current")
_BCgnatUnauthIcmpIdReleaseSuccessCount_Type = Counter64
_BCgnatUnauthIcmpIdReleaseSuccessCount_Object = MibTableColumn
bCgnatUnauthIcmpIdReleaseSuccessCount = _BCgnatUnauthIcmpIdReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 18),
    _BCgnatUnauthIcmpIdReleaseSuccessCount_Type()
)
bCgnatUnauthIcmpIdReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthIcmpIdReleaseSuccessCount.setStatus("current")
_BCgnatUnauthTcpPortReleaseSuccessCount_Type = Counter64
_BCgnatUnauthTcpPortReleaseSuccessCount_Object = MibTableColumn
bCgnatUnauthTcpPortReleaseSuccessCount = _BCgnatUnauthTcpPortReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 19),
    _BCgnatUnauthTcpPortReleaseSuccessCount_Type()
)
bCgnatUnauthTcpPortReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthTcpPortReleaseSuccessCount.setStatus("current")
_BCgnatUnauthUdpPortReleaseSuccessCount_Type = Counter64
_BCgnatUnauthUdpPortReleaseSuccessCount_Object = MibTableColumn
bCgnatUnauthUdpPortReleaseSuccessCount = _BCgnatUnauthUdpPortReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 20),
    _BCgnatUnauthUdpPortReleaseSuccessCount_Type()
)
bCgnatUnauthUdpPortReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUdpPortReleaseSuccessCount.setStatus("current")
_BCgnatUnauthIcmpIdReleaseFailureCount_Type = Counter64
_BCgnatUnauthIcmpIdReleaseFailureCount_Object = MibTableColumn
bCgnatUnauthIcmpIdReleaseFailureCount = _BCgnatUnauthIcmpIdReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 21),
    _BCgnatUnauthIcmpIdReleaseFailureCount_Type()
)
bCgnatUnauthIcmpIdReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthIcmpIdReleaseFailureCount.setStatus("current")
_BCgnatUnauthTcpPortReleaseFailureCount_Type = Counter64
_BCgnatUnauthTcpPortReleaseFailureCount_Object = MibTableColumn
bCgnatUnauthTcpPortReleaseFailureCount = _BCgnatUnauthTcpPortReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 22),
    _BCgnatUnauthTcpPortReleaseFailureCount_Type()
)
bCgnatUnauthTcpPortReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthTcpPortReleaseFailureCount.setStatus("current")
_BCgnatUnauthUdpPortReleaseFailureCount_Type = Counter64
_BCgnatUnauthUdpPortReleaseFailureCount_Object = MibTableColumn
bCgnatUnauthUdpPortReleaseFailureCount = _BCgnatUnauthUdpPortReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 23),
    _BCgnatUnauthUdpPortReleaseFailureCount_Type()
)
bCgnatUnauthUdpPortReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUdpPortReleaseFailureCount.setStatus("current")
_BCgnatUnauthMaxCgnatPortsExceeded_Type = Counter64
_BCgnatUnauthMaxCgnatPortsExceeded_Object = MibTableColumn
bCgnatUnauthMaxCgnatPortsExceeded = _BCgnatUnauthMaxCgnatPortsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 24),
    _BCgnatUnauthMaxCgnatPortsExceeded_Type()
)
bCgnatUnauthMaxCgnatPortsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthMaxCgnatPortsExceeded.setStatus("current")
_BCgnatUnauthMaxIcmpIdsExceeded_Type = Counter64
_BCgnatUnauthMaxIcmpIdsExceeded_Object = MibTableColumn
bCgnatUnauthMaxIcmpIdsExceeded = _BCgnatUnauthMaxIcmpIdsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 25),
    _BCgnatUnauthMaxIcmpIdsExceeded_Type()
)
bCgnatUnauthMaxIcmpIdsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthMaxIcmpIdsExceeded.setStatus("current")
_BCgnatUnauthFlowDeleteRcvd_Type = Counter64
_BCgnatUnauthFlowDeleteRcvd_Object = MibTableColumn
bCgnatUnauthFlowDeleteRcvd = _BCgnatUnauthFlowDeleteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 26),
    _BCgnatUnauthFlowDeleteRcvd_Type()
)
bCgnatUnauthFlowDeleteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeleteRcvd.setStatus("current")
_BCgnatUnauthFlowDeleteSent_Type = Counter64
_BCgnatUnauthFlowDeleteSent_Object = MibTableColumn
bCgnatUnauthFlowDeleteSent = _BCgnatUnauthFlowDeleteSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 27),
    _BCgnatUnauthFlowDeleteSent_Type()
)
bCgnatUnauthFlowDeleteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeleteSent.setStatus("current")
_BCgnatUnauthFlowDeleteFindFailure_Type = Counter64
_BCgnatUnauthFlowDeleteFindFailure_Object = MibTableColumn
bCgnatUnauthFlowDeleteFindFailure = _BCgnatUnauthFlowDeleteFindFailure_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 28),
    _BCgnatUnauthFlowDeleteFindFailure_Type()
)
bCgnatUnauthFlowDeleteFindFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeleteFindFailure.setStatus("current")
_BCgnatUnauthDnsFlowAlloc_Type = Counter64
_BCgnatUnauthDnsFlowAlloc_Object = MibTableColumn
bCgnatUnauthDnsFlowAlloc = _BCgnatUnauthDnsFlowAlloc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 29),
    _BCgnatUnauthDnsFlowAlloc_Type()
)
bCgnatUnauthDnsFlowAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowAlloc.setStatus("current")
_BCgnatUnauthDnsFlowRelease_Type = Counter64
_BCgnatUnauthDnsFlowRelease_Object = MibTableColumn
bCgnatUnauthDnsFlowRelease = _BCgnatUnauthDnsFlowRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 30),
    _BCgnatUnauthDnsFlowRelease_Type()
)
bCgnatUnauthDnsFlowRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowRelease.setStatus("current")
_BCgnatUnauthDnsFlowAllocSuccessCount_Type = Counter64
_BCgnatUnauthDnsFlowAllocSuccessCount_Object = MibTableColumn
bCgnatUnauthDnsFlowAllocSuccessCount = _BCgnatUnauthDnsFlowAllocSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 31),
    _BCgnatUnauthDnsFlowAllocSuccessCount_Type()
)
bCgnatUnauthDnsFlowAllocSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowAllocSuccessCount.setStatus("current")
_BCgnatUnauthDnsFlowReleaseSuccessCount_Type = Counter64
_BCgnatUnauthDnsFlowReleaseSuccessCount_Object = MibTableColumn
bCgnatUnauthDnsFlowReleaseSuccessCount = _BCgnatUnauthDnsFlowReleaseSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 32),
    _BCgnatUnauthDnsFlowReleaseSuccessCount_Type()
)
bCgnatUnauthDnsFlowReleaseSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowReleaseSuccessCount.setStatus("current")
_BCgnatUnauthDnsFlowAllocFailureCount_Type = Counter64
_BCgnatUnauthDnsFlowAllocFailureCount_Object = MibTableColumn
bCgnatUnauthDnsFlowAllocFailureCount = _BCgnatUnauthDnsFlowAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 33),
    _BCgnatUnauthDnsFlowAllocFailureCount_Type()
)
bCgnatUnauthDnsFlowAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowAllocFailureCount.setStatus("current")
_BCgnatUnauthDnsFlowReleaseFailureCount_Type = Counter64
_BCgnatUnauthDnsFlowReleaseFailureCount_Object = MibTableColumn
bCgnatUnauthDnsFlowReleaseFailureCount = _BCgnatUnauthDnsFlowReleaseFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 34),
    _BCgnatUnauthDnsFlowReleaseFailureCount_Type()
)
bCgnatUnauthDnsFlowReleaseFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthDnsFlowReleaseFailureCount.setStatus("current")
_BCgnatUnauthPortsThresholdExceededSent_Type = Counter64
_BCgnatUnauthPortsThresholdExceededSent_Object = MibTableColumn
bCgnatUnauthPortsThresholdExceededSent = _BCgnatUnauthPortsThresholdExceededSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 35),
    _BCgnatUnauthPortsThresholdExceededSent_Type()
)
bCgnatUnauthPortsThresholdExceededSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthPortsThresholdExceededSent.setStatus("current")
_BCgnatUnauthPortsThresholdExceededRcvd_Type = Counter64
_BCgnatUnauthPortsThresholdExceededRcvd_Object = MibTableColumn
bCgnatUnauthPortsThresholdExceededRcvd = _BCgnatUnauthPortsThresholdExceededRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 36),
    _BCgnatUnauthPortsThresholdExceededRcvd_Type()
)
bCgnatUnauthPortsThresholdExceededRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthPortsThresholdExceededRcvd.setStatus("current")
_BCgnatUnauthPortsThresholdExceededInt_Type = Counter64
_BCgnatUnauthPortsThresholdExceededInt_Object = MibTableColumn
bCgnatUnauthPortsThresholdExceededInt = _BCgnatUnauthPortsThresholdExceededInt_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 37),
    _BCgnatUnauthPortsThresholdExceededInt_Type()
)
bCgnatUnauthPortsThresholdExceededInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthPortsThresholdExceededInt.setStatus("current")
_BCgnatUnauthPortsThresholdExceededErr_Type = Counter64
_BCgnatUnauthPortsThresholdExceededErr_Object = MibTableColumn
bCgnatUnauthPortsThresholdExceededErr = _BCgnatUnauthPortsThresholdExceededErr_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 38),
    _BCgnatUnauthPortsThresholdExceededErr_Type()
)
bCgnatUnauthPortsThresholdExceededErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthPortsThresholdExceededErr.setStatus("current")
_BCgnatUnauthUnsupportedActionIdRcvd_Type = Counter64
_BCgnatUnauthUnsupportedActionIdRcvd_Object = MibTableColumn
bCgnatUnauthUnsupportedActionIdRcvd = _BCgnatUnauthUnsupportedActionIdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 39),
    _BCgnatUnauthUnsupportedActionIdRcvd_Type()
)
bCgnatUnauthUnsupportedActionIdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUnsupportedActionIdRcvd.setStatus("current")
_BCgnatUnauthNonTcpSynPortAllocDrop_Type = Counter64
_BCgnatUnauthNonTcpSynPortAllocDrop_Object = MibTableColumn
bCgnatUnauthNonTcpSynPortAllocDrop = _BCgnatUnauthNonTcpSynPortAllocDrop_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 40),
    _BCgnatUnauthNonTcpSynPortAllocDrop_Type()
)
bCgnatUnauthNonTcpSynPortAllocDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthNonTcpSynPortAllocDrop.setStatus("current")
_BCgnatUnauthFlowDeletedTimer_Type = Counter64
_BCgnatUnauthFlowDeletedTimer_Object = MibTableColumn
bCgnatUnauthFlowDeletedTimer = _BCgnatUnauthFlowDeletedTimer_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 41),
    _BCgnatUnauthFlowDeletedTimer_Type()
)
bCgnatUnauthFlowDeletedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeletedTimer.setStatus("current")
_BCgnatUnauthFlowDeletedSessionEnded_Type = Counter64
_BCgnatUnauthFlowDeletedSessionEnded_Object = MibTableColumn
bCgnatUnauthFlowDeletedSessionEnded = _BCgnatUnauthFlowDeletedSessionEnded_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 42),
    _BCgnatUnauthFlowDeletedSessionEnded_Type()
)
bCgnatUnauthFlowDeletedSessionEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeletedSessionEnded.setStatus("current")
_BCgnatUnauthFlowDeletedSubClear_Type = Counter64
_BCgnatUnauthFlowDeletedSubClear_Object = MibTableColumn
bCgnatUnauthFlowDeletedSubClear = _BCgnatUnauthFlowDeletedSubClear_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 43),
    _BCgnatUnauthFlowDeletedSubClear_Type()
)
bCgnatUnauthFlowDeletedSubClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthFlowDeletedSubClear.setStatus("current")
_BCgnatUnauthNatFlowDelErrSubIdMismatch_Type = Counter64
_BCgnatUnauthNatFlowDelErrSubIdMismatch_Object = MibTableColumn
bCgnatUnauthNatFlowDelErrSubIdMismatch = _BCgnatUnauthNatFlowDelErrSubIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 44),
    _BCgnatUnauthNatFlowDelErrSubIdMismatch_Type()
)
bCgnatUnauthNatFlowDelErrSubIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthNatFlowDelErrSubIdMismatch.setStatus("current")
_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Type = Counter64
_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Object = MibTableColumn
bCgnatUnauthNatFlowDelErrValidFlagNotSet = _BCgnatUnauthNatFlowDelErrValidFlagNotSet_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 45),
    _BCgnatUnauthNatFlowDelErrValidFlagNotSet_Type()
)
bCgnatUnauthNatFlowDelErrValidFlagNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthNatFlowDelErrValidFlagNotSet.setStatus("current")
_BCgnatUnauthIcmpPortUnreachableSent_Type = Counter64
_BCgnatUnauthIcmpPortUnreachableSent_Object = MibTableColumn
bCgnatUnauthIcmpPortUnreachableSent = _BCgnatUnauthIcmpPortUnreachableSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 46),
    _BCgnatUnauthIcmpPortUnreachableSent_Type()
)
bCgnatUnauthIcmpPortUnreachableSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthIcmpPortUnreachableSent.setStatus("current")
_BCgnatUnauthPortsNotAvailableDrop_Type = Counter64
_BCgnatUnauthPortsNotAvailableDrop_Object = MibTableColumn
bCgnatUnauthPortsNotAvailableDrop = _BCgnatUnauthPortsNotAvailableDrop_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 47),
    _BCgnatUnauthPortsNotAvailableDrop_Type()
)
bCgnatUnauthPortsNotAvailableDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthPortsNotAvailableDrop.setStatus("current")
_BCgnatUnauthUnsupportedPrivatePortDropCount_Type = Counter64
_BCgnatUnauthUnsupportedPrivatePortDropCount_Object = MibTableColumn
bCgnatUnauthUnsupportedPrivatePortDropCount = _BCgnatUnauthUnsupportedPrivatePortDropCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 48),
    _BCgnatUnauthUnsupportedPrivatePortDropCount_Type()
)
bCgnatUnauthUnsupportedPrivatePortDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatUnauthUnsupportedPrivatePortDropCount.setStatus("current")
_BCgnatAuthPortUtilTable_Object = MibTable
bCgnatAuthPortUtilTable = _BCgnatAuthPortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    bCgnatAuthPortUtilTable.setStatus("current")
_BCgnatAuthPortUtilEntry_Object = MibTableRow
bCgnatAuthPortUtilEntry = _BCgnatAuthPortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1)
)
bCgnatAuthPortUtilEntry.setIndexNames(
    (0, "BENU-CGNAT-STATS-MIB", "bCgnatAuthPortUtilIndex"),
)
if mibBuilder.loadTexts:
    bCgnatAuthPortUtilEntry.setStatus("current")
_BCgnatAuthPortUtilIndex_Type = Unsigned32
_BCgnatAuthPortUtilIndex_Object = MibTableColumn
bCgnatAuthPortUtilIndex = _BCgnatAuthPortUtilIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 1),
    _BCgnatAuthPortUtilIndex_Type()
)
bCgnatAuthPortUtilIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bCgnatAuthPortUtilIndex.setStatus("current")
_BCgnatAuthSubscriberMac_Type = MacAddress
_BCgnatAuthSubscriberMac_Object = MibTableColumn
bCgnatAuthSubscriberMac = _BCgnatAuthSubscriberMac_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 2),
    _BCgnatAuthSubscriberMac_Type()
)
bCgnatAuthSubscriberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthSubscriberMac.setStatus("current")
_BCgnatAuthSubscriberPortsFree_Type = Unsigned32
_BCgnatAuthSubscriberPortsFree_Object = MibTableColumn
bCgnatAuthSubscriberPortsFree = _BCgnatAuthSubscriberPortsFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 3),
    _BCgnatAuthSubscriberPortsFree_Type()
)
bCgnatAuthSubscriberPortsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthSubscriberPortsFree.setStatus("current")
_BCgnatAuthPortRisingThresholdCrossedSubCount_Type = Unsigned32
_BCgnatAuthPortRisingThresholdCrossedSubCount_Object = MibScalar
bCgnatAuthPortRisingThresholdCrossedSubCount = _BCgnatAuthPortRisingThresholdCrossedSubCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 4),
    _BCgnatAuthPortRisingThresholdCrossedSubCount_Type()
)
bCgnatAuthPortRisingThresholdCrossedSubCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCgnatAuthPortRisingThresholdCrossedSubCount.setStatus("current")
_BDslitePortBlockRisingThresholdCrossedTunCount_Type = Unsigned32
_BDslitePortBlockRisingThresholdCrossedTunCount_Object = MibScalar
bDslitePortBlockRisingThresholdCrossedTunCount = _BDslitePortBlockRisingThresholdCrossedTunCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 5),
    _BDslitePortBlockRisingThresholdCrossedTunCount_Type()
)
bDslitePortBlockRisingThresholdCrossedTunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDslitePortBlockRisingThresholdCrossedTunCount.setStatus("current")
_BCgnatNotifObjects_ObjectIdentity = ObjectIdentity
bCgnatNotifObjects = _BCgnatNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    bCgnatNotifObjects.setStatus("current")
_BCgnatSubscriberMac_Type = MacAddress
_BCgnatSubscriberMac_Object = MibScalar
bCgnatSubscriberMac = _BCgnatSubscriberMac_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 1),
    _BCgnatSubscriberMac_Type()
)
bCgnatSubscriberMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatSubscriberMac.setStatus("current")
_BCgnatTotalPortBlocksPerSubscriber_Type = Unsigned32
_BCgnatTotalPortBlocksPerSubscriber_Object = MibScalar
bCgnatTotalPortBlocksPerSubscriber = _BCgnatTotalPortBlocksPerSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 2),
    _BCgnatTotalPortBlocksPerSubscriber_Type()
)
bCgnatTotalPortBlocksPerSubscriber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatTotalPortBlocksPerSubscriber.setStatus("current")
_BCgnatPortBlocksUsedHighThreshold_Type = Unsigned32
_BCgnatPortBlocksUsedHighThreshold_Object = MibScalar
bCgnatPortBlocksUsedHighThreshold = _BCgnatPortBlocksUsedHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 3),
    _BCgnatPortBlocksUsedHighThreshold_Type()
)
bCgnatPortBlocksUsedHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatPortBlocksUsedHighThreshold.setStatus("current")
_BCgnatPortBlocksUsedLowThreshold_Type = Unsigned32
_BCgnatPortBlocksUsedLowThreshold_Object = MibScalar
bCgnatPortBlocksUsedLowThreshold = _BCgnatPortBlocksUsedLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 4),
    _BCgnatPortBlocksUsedLowThreshold_Type()
)
bCgnatPortBlocksUsedLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatPortBlocksUsedLowThreshold.setStatus("current")
_BCgnatThresholdTunnelId_Type = Unsigned32
_BCgnatThresholdTunnelId_Object = MibScalar
bCgnatThresholdTunnelId = _BCgnatThresholdTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 5),
    _BCgnatThresholdTunnelId_Type()
)
bCgnatThresholdTunnelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatThresholdTunnelId.setStatus("current")
_BCgnatEvenPortsForTunnel_Type = Unsigned32
_BCgnatEvenPortsForTunnel_Object = MibScalar
bCgnatEvenPortsForTunnel = _BCgnatEvenPortsForTunnel_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 6),
    _BCgnatEvenPortsForTunnel_Type()
)
bCgnatEvenPortsForTunnel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatEvenPortsForTunnel.setStatus("current")
_BCgnatOddPortsForTunnel_Type = Unsigned32
_BCgnatOddPortsForTunnel_Object = MibScalar
bCgnatOddPortsForTunnel = _BCgnatOddPortsForTunnel_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 7),
    _BCgnatOddPortsForTunnel_Type()
)
bCgnatOddPortsForTunnel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatOddPortsForTunnel.setStatus("current")
_BCgnatPortParity_Type = Unsigned32
_BCgnatPortParity_Object = MibScalar
bCgnatPortParity = _BCgnatPortParity_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 8),
    _BCgnatPortParity_Type()
)
bCgnatPortParity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatPortParity.setStatus("current")
_BCgnatTunnelPortBlocksUsedHighThreshold_Type = Unsigned32
_BCgnatTunnelPortBlocksUsedHighThreshold_Object = MibScalar
bCgnatTunnelPortBlocksUsedHighThreshold = _BCgnatTunnelPortBlocksUsedHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 9),
    _BCgnatTunnelPortBlocksUsedHighThreshold_Type()
)
bCgnatTunnelPortBlocksUsedHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatTunnelPortBlocksUsedHighThreshold.setStatus("current")
_BCgnatTunnelPortBlocksUsedLowThreshold_Type = Unsigned32
_BCgnatTunnelPortBlocksUsedLowThreshold_Object = MibScalar
bCgnatTunnelPortBlocksUsedLowThreshold = _BCgnatTunnelPortBlocksUsedLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 10),
    _BCgnatTunnelPortBlocksUsedLowThreshold_Type()
)
bCgnatTunnelPortBlocksUsedLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bCgnatTunnelPortBlocksUsedLowThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

bCgnatPortBlocksUsedHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 1)
)
bCgnatPortBlocksUsedHighThresholdReached.setObjects(
      *(("BENU-CGNAT-STATS-MIB", "bCgnatSubscriberMac"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatTotalPortBlocksPerSubscriber"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatPortBlocksUsedHighThreshold"))
)
if mibBuilder.loadTexts:
    bCgnatPortBlocksUsedHighThresholdReached.setStatus(
        "current"
    )

bCgnatPortBlocksUsedLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 2)
)
bCgnatPortBlocksUsedLowThresholdReached.setObjects(
      *(("BENU-CGNAT-STATS-MIB", "bCgnatSubscriberMac"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatTotalPortBlocksPerSubscriber"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatPortBlocksUsedLowThreshold"))
)
if mibBuilder.loadTexts:
    bCgnatPortBlocksUsedLowThresholdReached.setStatus(
        "current"
    )

bCgnatTunnelPortBlocksUsedHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 3)
)
bCgnatTunnelPortBlocksUsedHighThresholdReached.setObjects(
      *(("BENU-CGNAT-STATS-MIB", "bCgnatThresholdTunnelId"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatEvenPortsForTunnel"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatOddPortsForTunnel"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatPortParity"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatTunnelPortBlocksUsedHighThreshold"))
)
if mibBuilder.loadTexts:
    bCgnatTunnelPortBlocksUsedHighThresholdReached.setStatus(
        "current"
    )

bCgnatTunnelPortBlocksUsedLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 4)
)
bCgnatTunnelPortBlocksUsedLowThresholdReached.setObjects(
      *(("BENU-CGNAT-STATS-MIB", "bCgnatThresholdTunnelId"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatEvenPortsForTunnel"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatOddPortsForTunnel"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatPortParity"),
        ("BENU-CGNAT-STATS-MIB", "bCgnatTunnelPortBlocksUsedLowThreshold"))
)
if mibBuilder.loadTexts:
    bCgnatTunnelPortBlocksUsedLowThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-CGNAT-STATS-MIB",
    **{"benuCgnatStatsMIB": benuCgnatStatsMIB,
       "bCgnatNotifications": bCgnatNotifications,
       "bCgnatPortBlocksUsedHighThresholdReached": bCgnatPortBlocksUsedHighThresholdReached,
       "bCgnatPortBlocksUsedLowThresholdReached": bCgnatPortBlocksUsedLowThresholdReached,
       "bCgnatTunnelPortBlocksUsedHighThresholdReached": bCgnatTunnelPortBlocksUsedHighThresholdReached,
       "bCgnatTunnelPortBlocksUsedLowThresholdReached": bCgnatTunnelPortBlocksUsedLowThresholdReached,
       "bCgnatMIBObjects": bCgnatMIBObjects,
       "bCgnatAuthStatsTable": bCgnatAuthStatsTable,
       "bCgnatAuthStatsEntry": bCgnatAuthStatsEntry,
       "bCgnatAuthStatsIndex": bCgnatAuthStatsIndex,
       "bCgnatAuthProfileName": bCgnatAuthProfileName,
       "bCgnatAuthDomainPublicIpZeroCount": bCgnatAuthDomainPublicIpZeroCount,
       "bCgnatAuthDomainNoFreePortCount": bCgnatAuthDomainNoFreePortCount,
       "bCgnatAuthFlowAddSuccessCount": bCgnatAuthFlowAddSuccessCount,
       "bCgnatAuthFlowAddFailureCount": bCgnatAuthFlowAddFailureCount,
       "bCgnatAuthTimerAllocFailureCount": bCgnatAuthTimerAllocFailureCount,
       "bCgnatAuthFlowDeleteSuccessCount": bCgnatAuthFlowDeleteSuccessCount,
       "bCgnatAuthFlowDeleteFailureCount": bCgnatAuthFlowDeleteFailureCount,
       "bCgnatAuthUnsupportedL4DropCount": bCgnatAuthUnsupportedL4DropCount,
       "bCgnatAuthNatflowSyncFailureCount": bCgnatAuthNatflowSyncFailureCount,
       "bCgnatAuthIcmpIdAllocSuccessCount": bCgnatAuthIcmpIdAllocSuccessCount,
       "bCgnatAuthTcpPortAllocSuccessCount": bCgnatAuthTcpPortAllocSuccessCount,
       "bCgnatAuthUdpPortAllocSuccessCount": bCgnatAuthUdpPortAllocSuccessCount,
       "bCgnatAuthIcmpIdAllocFailureCount": bCgnatAuthIcmpIdAllocFailureCount,
       "bCgnatAuthTcpPortAllocFailureCount": bCgnatAuthTcpPortAllocFailureCount,
       "bCgnatAuthUdpPortAllocFailureCount": bCgnatAuthUdpPortAllocFailureCount,
       "bCgnatAuthIcmpIdReleaseSuccessCount": bCgnatAuthIcmpIdReleaseSuccessCount,
       "bCgnatAuthTcpPortReleaseSuccessCount": bCgnatAuthTcpPortReleaseSuccessCount,
       "bCgnatAuthUdpPortReleaseSuccessCount": bCgnatAuthUdpPortReleaseSuccessCount,
       "bCgnatAuthIcmpIdReleaseFailureCount": bCgnatAuthIcmpIdReleaseFailureCount,
       "bCgnatAuthTcpPortReleaseFailureCount": bCgnatAuthTcpPortReleaseFailureCount,
       "bCgnatAuthUdpPortReleaseFailureCount": bCgnatAuthUdpPortReleaseFailureCount,
       "bCgnatAuthMaxCgnatPortsExceeded": bCgnatAuthMaxCgnatPortsExceeded,
       "bCgnatAuthMaxIcmpIdsExceeded": bCgnatAuthMaxIcmpIdsExceeded,
       "bCgnatAuthFlowDeleteRcvd": bCgnatAuthFlowDeleteRcvd,
       "bCgnatAuthFlowDeleteSent": bCgnatAuthFlowDeleteSent,
       "bCgnatAuthFlowDeleteFindFailure": bCgnatAuthFlowDeleteFindFailure,
       "bCgnatAuthDnsFlowAlloc": bCgnatAuthDnsFlowAlloc,
       "bCgnatAuthDnsFlowRelease": bCgnatAuthDnsFlowRelease,
       "bCgnatAuthDnsFlowAllocSuccessCount": bCgnatAuthDnsFlowAllocSuccessCount,
       "bCgnatAuthDnsFlowReleaseSuccessCount": bCgnatAuthDnsFlowReleaseSuccessCount,
       "bCgnatAuthDnsFlowAllocFailureCount": bCgnatAuthDnsFlowAllocFailureCount,
       "bCgnatAuthDnsFlowReleaseFailureCount": bCgnatAuthDnsFlowReleaseFailureCount,
       "bCgnatAuthPortsThresholdExceededSent": bCgnatAuthPortsThresholdExceededSent,
       "bCgnatAuthPortsThresholdExceededRcvd": bCgnatAuthPortsThresholdExceededRcvd,
       "bCgnatAuthPortsThresholdExceededInt": bCgnatAuthPortsThresholdExceededInt,
       "bCgnatAuthPortsThresholdExceededErr": bCgnatAuthPortsThresholdExceededErr,
       "bCgnatAuthUnsupportedActionIdRcvd": bCgnatAuthUnsupportedActionIdRcvd,
       "bCgnatAuthNonTcpSynPortAllocDrop": bCgnatAuthNonTcpSynPortAllocDrop,
       "bCgnatAuthFlowDeletedTimer": bCgnatAuthFlowDeletedTimer,
       "bCgnatAuthFlowDeletedSessionEnded": bCgnatAuthFlowDeletedSessionEnded,
       "bCgnatAuthFlowDeletedSubClear": bCgnatAuthFlowDeletedSubClear,
       "bCgnatAuthNatFlowDelErrSubIdMismatch": bCgnatAuthNatFlowDelErrSubIdMismatch,
       "bCgnatAuthNatFlowDelErrValidFlagNotSet": bCgnatAuthNatFlowDelErrValidFlagNotSet,
       "bCgnatAuthIcmpPortUnreachableSent": bCgnatAuthIcmpPortUnreachableSent,
       "bCgnatAuthPortsNotAvailableDrop": bCgnatAuthPortsNotAvailableDrop,
       "bCgnatAuthUnsupportedPrivatePortDropCount": bCgnatAuthUnsupportedPrivatePortDropCount,
       "bCgnatUnauthStatsTable": bCgnatUnauthStatsTable,
       "bCgnatUnauthStatsEntry": bCgnatUnauthStatsEntry,
       "bCgnatUnauthStatsIndex": bCgnatUnauthStatsIndex,
       "bCgnatUnauthProfileName": bCgnatUnauthProfileName,
       "bCgnatUnauthDomainPublicIpZeroCount": bCgnatUnauthDomainPublicIpZeroCount,
       "bCgnatUnauthDomainNoFreePortCount": bCgnatUnauthDomainNoFreePortCount,
       "bCgnatUnauthFlowAddSuccessCount": bCgnatUnauthFlowAddSuccessCount,
       "bCgnatUnauthFlowAddFailureCount": bCgnatUnauthFlowAddFailureCount,
       "bCgnatUnauthTimerAllocFailureCount": bCgnatUnauthTimerAllocFailureCount,
       "bCgnatUnauthFlowDeleteSuccessCount": bCgnatUnauthFlowDeleteSuccessCount,
       "bCgnatUnauthFlowDeleteFailureCount": bCgnatUnauthFlowDeleteFailureCount,
       "bCgnatUnauthUnsupportedL4DropCount": bCgnatUnauthUnsupportedL4DropCount,
       "bCgnatUnauthNatflowSyncFailureCount": bCgnatUnauthNatflowSyncFailureCount,
       "bCgnatUnauthIcmpIdAllocSuccessCount": bCgnatUnauthIcmpIdAllocSuccessCount,
       "bCgnatUnauthTcpPortAllocSuccessCount": bCgnatUnauthTcpPortAllocSuccessCount,
       "bCgnatUnauthUdpPortAllocSuccessCount": bCgnatUnauthUdpPortAllocSuccessCount,
       "bCgnatUnauthIcmpIdAllocFailureCount": bCgnatUnauthIcmpIdAllocFailureCount,
       "bCgnatUnauthTcpPortAllocFailureCount": bCgnatUnauthTcpPortAllocFailureCount,
       "bCgnatUnauthUdpPortAllocFailureCount": bCgnatUnauthUdpPortAllocFailureCount,
       "bCgnatUnauthIcmpIdReleaseSuccessCount": bCgnatUnauthIcmpIdReleaseSuccessCount,
       "bCgnatUnauthTcpPortReleaseSuccessCount": bCgnatUnauthTcpPortReleaseSuccessCount,
       "bCgnatUnauthUdpPortReleaseSuccessCount": bCgnatUnauthUdpPortReleaseSuccessCount,
       "bCgnatUnauthIcmpIdReleaseFailureCount": bCgnatUnauthIcmpIdReleaseFailureCount,
       "bCgnatUnauthTcpPortReleaseFailureCount": bCgnatUnauthTcpPortReleaseFailureCount,
       "bCgnatUnauthUdpPortReleaseFailureCount": bCgnatUnauthUdpPortReleaseFailureCount,
       "bCgnatUnauthMaxCgnatPortsExceeded": bCgnatUnauthMaxCgnatPortsExceeded,
       "bCgnatUnauthMaxIcmpIdsExceeded": bCgnatUnauthMaxIcmpIdsExceeded,
       "bCgnatUnauthFlowDeleteRcvd": bCgnatUnauthFlowDeleteRcvd,
       "bCgnatUnauthFlowDeleteSent": bCgnatUnauthFlowDeleteSent,
       "bCgnatUnauthFlowDeleteFindFailure": bCgnatUnauthFlowDeleteFindFailure,
       "bCgnatUnauthDnsFlowAlloc": bCgnatUnauthDnsFlowAlloc,
       "bCgnatUnauthDnsFlowRelease": bCgnatUnauthDnsFlowRelease,
       "bCgnatUnauthDnsFlowAllocSuccessCount": bCgnatUnauthDnsFlowAllocSuccessCount,
       "bCgnatUnauthDnsFlowReleaseSuccessCount": bCgnatUnauthDnsFlowReleaseSuccessCount,
       "bCgnatUnauthDnsFlowAllocFailureCount": bCgnatUnauthDnsFlowAllocFailureCount,
       "bCgnatUnauthDnsFlowReleaseFailureCount": bCgnatUnauthDnsFlowReleaseFailureCount,
       "bCgnatUnauthPortsThresholdExceededSent": bCgnatUnauthPortsThresholdExceededSent,
       "bCgnatUnauthPortsThresholdExceededRcvd": bCgnatUnauthPortsThresholdExceededRcvd,
       "bCgnatUnauthPortsThresholdExceededInt": bCgnatUnauthPortsThresholdExceededInt,
       "bCgnatUnauthPortsThresholdExceededErr": bCgnatUnauthPortsThresholdExceededErr,
       "bCgnatUnauthUnsupportedActionIdRcvd": bCgnatUnauthUnsupportedActionIdRcvd,
       "bCgnatUnauthNonTcpSynPortAllocDrop": bCgnatUnauthNonTcpSynPortAllocDrop,
       "bCgnatUnauthFlowDeletedTimer": bCgnatUnauthFlowDeletedTimer,
       "bCgnatUnauthFlowDeletedSessionEnded": bCgnatUnauthFlowDeletedSessionEnded,
       "bCgnatUnauthFlowDeletedSubClear": bCgnatUnauthFlowDeletedSubClear,
       "bCgnatUnauthNatFlowDelErrSubIdMismatch": bCgnatUnauthNatFlowDelErrSubIdMismatch,
       "bCgnatUnauthNatFlowDelErrValidFlagNotSet": bCgnatUnauthNatFlowDelErrValidFlagNotSet,
       "bCgnatUnauthIcmpPortUnreachableSent": bCgnatUnauthIcmpPortUnreachableSent,
       "bCgnatUnauthPortsNotAvailableDrop": bCgnatUnauthPortsNotAvailableDrop,
       "bCgnatUnauthUnsupportedPrivatePortDropCount": bCgnatUnauthUnsupportedPrivatePortDropCount,
       "bCgnatAuthPortUtilTable": bCgnatAuthPortUtilTable,
       "bCgnatAuthPortUtilEntry": bCgnatAuthPortUtilEntry,
       "bCgnatAuthPortUtilIndex": bCgnatAuthPortUtilIndex,
       "bCgnatAuthSubscriberMac": bCgnatAuthSubscriberMac,
       "bCgnatAuthSubscriberPortsFree": bCgnatAuthSubscriberPortsFree,
       "bCgnatAuthPortRisingThresholdCrossedSubCount": bCgnatAuthPortRisingThresholdCrossedSubCount,
       "bDslitePortBlockRisingThresholdCrossedTunCount": bDslitePortBlockRisingThresholdCrossedTunCount,
       "bCgnatNotifObjects": bCgnatNotifObjects,
       "bCgnatSubscriberMac": bCgnatSubscriberMac,
       "bCgnatTotalPortBlocksPerSubscriber": bCgnatTotalPortBlocksPerSubscriber,
       "bCgnatPortBlocksUsedHighThreshold": bCgnatPortBlocksUsedHighThreshold,
       "bCgnatPortBlocksUsedLowThreshold": bCgnatPortBlocksUsedLowThreshold,
       "bCgnatThresholdTunnelId": bCgnatThresholdTunnelId,
       "bCgnatEvenPortsForTunnel": bCgnatEvenPortsForTunnel,
       "bCgnatOddPortsForTunnel": bCgnatOddPortsForTunnel,
       "bCgnatPortParity": bCgnatPortParity,
       "bCgnatTunnelPortBlocksUsedHighThreshold": bCgnatTunnelPortBlocksUsedHighThreshold,
       "bCgnatTunnelPortBlocksUsedLowThreshold": bCgnatTunnelPortBlocksUsedLowThreshold}
)
