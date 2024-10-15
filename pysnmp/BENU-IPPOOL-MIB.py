# SNMP MIB module (BENU-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-IPPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:56 2024
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
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

benuIPPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5)
)
benuIPPoolMIB.setRevisions(
        ("2015-08-11 00:00",
         "2015-01-05 00:00",
         "2013-10-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BIPPoolNotifications_ObjectIdentity = ObjectIdentity
bIPPoolNotifications = _BIPPoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0)
)
if mibBuilder.loadTexts:
    bIPPoolNotifications.setStatus("current")
_BIPv4PoolMIBObjects_ObjectIdentity = ObjectIdentity
bIPv4PoolMIBObjects = _BIPv4PoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bIPv4PoolMIBObjects.setStatus("current")
_BIPPoolTable_Object = MibTable
bIPPoolTable = _BIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    bIPPoolTable.setStatus("current")
_BIPPoolEntry_Object = MibTableRow
bIPPoolEntry = _BIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1)
)
bIPPoolEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPPoolStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPPoolIndex"),
)
if mibBuilder.loadTexts:
    bIPPoolEntry.setStatus("current")
_BIPPoolStatsInterval_Type = Integer32
_BIPPoolStatsInterval_Object = MibTableColumn
bIPPoolStatsInterval = _BIPPoolStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 1),
    _BIPPoolStatsInterval_Type()
)
bIPPoolStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolStatsInterval.setStatus("current")
_BIPPoolIndex_Type = Integer32
_BIPPoolIndex_Object = MibTableColumn
bIPPoolIndex = _BIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 2),
    _BIPPoolIndex_Type()
)
bIPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolIndex.setStatus("current")
_BIPPoolIntervalDuration_Type = Integer32
_BIPPoolIntervalDuration_Object = MibTableColumn
bIPPoolIntervalDuration = _BIPPoolIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 3),
    _BIPPoolIntervalDuration_Type()
)
bIPPoolIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolIntervalDuration.setStatus("current")
_BIPPoolName_Type = DisplayString
_BIPPoolName_Object = MibTableColumn
bIPPoolName = _BIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 4),
    _BIPPoolName_Type()
)
bIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolName.setStatus("current")
_BIPPoolStartAddress_Type = InetAddressIPv4
_BIPPoolStartAddress_Object = MibTableColumn
bIPPoolStartAddress = _BIPPoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 5),
    _BIPPoolStartAddress_Type()
)
bIPPoolStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolStartAddress.setStatus("current")
_BIPPoolEndAddress_Type = InetAddressIPv4
_BIPPoolEndAddress_Object = MibTableColumn
bIPPoolEndAddress = _BIPPoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 6),
    _BIPPoolEndAddress_Type()
)
bIPPoolEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolEndAddress.setStatus("current")
_BIPPoolTotalAddresses_Type = Unsigned32
_BIPPoolTotalAddresses_Object = MibTableColumn
bIPPoolTotalAddresses = _BIPPoolTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 7),
    _BIPPoolTotalAddresses_Type()
)
bIPPoolTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolTotalAddresses.setStatus("current")
_BIPPoolReservedAddresses_Type = Unsigned32
_BIPPoolReservedAddresses_Object = MibTableColumn
bIPPoolReservedAddresses = _BIPPoolReservedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 8),
    _BIPPoolReservedAddresses_Type()
)
bIPPoolReservedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolReservedAddresses.setStatus("current")
_BIPPoolPeakFreeAddresses_Type = Unsigned32
_BIPPoolPeakFreeAddresses_Object = MibTableColumn
bIPPoolPeakFreeAddresses = _BIPPoolPeakFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 9),
    _BIPPoolPeakFreeAddresses_Type()
)
bIPPoolPeakFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolPeakFreeAddresses.setStatus("current")
_BIPPoolPeakUsedAddresses_Type = Unsigned32
_BIPPoolPeakUsedAddresses_Object = MibTableColumn
bIPPoolPeakUsedAddresses = _BIPPoolPeakUsedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 10),
    _BIPPoolPeakUsedAddresses_Type()
)
bIPPoolPeakUsedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolPeakUsedAddresses.setStatus("current")
_BIPPoolUsedAddrLowThreshold_Type = Unsigned32
_BIPPoolUsedAddrLowThreshold_Object = MibTableColumn
bIPPoolUsedAddrLowThreshold = _BIPPoolUsedAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 11),
    _BIPPoolUsedAddrLowThreshold_Type()
)
bIPPoolUsedAddrLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolUsedAddrLowThreshold.setStatus("current")
_BIPPoolUsedAddrHighThreshold_Type = Unsigned32
_BIPPoolUsedAddrHighThreshold_Object = MibTableColumn
bIPPoolUsedAddrHighThreshold = _BIPPoolUsedAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 12),
    _BIPPoolUsedAddrHighThreshold_Type()
)
bIPPoolUsedAddrHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolUsedAddrHighThreshold.setStatus("current")
_BIPPoolGrpName_Type = DisplayString
_BIPPoolGrpName_Object = MibTableColumn
bIPPoolGrpName = _BIPPoolGrpName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 13),
    _BIPPoolGrpName_Type()
)
bIPPoolGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGrpName.setStatus("current")
_BIPPoolGroupTable_Object = MibTable
bIPPoolGroupTable = _BIPPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    bIPPoolGroupTable.setStatus("current")
_BIPPoolGroupEntry_Object = MibTableRow
bIPPoolGroupEntry = _BIPPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1)
)
bIPPoolGroupEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPPoolGroupStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPPoolGroupIndex"),
)
if mibBuilder.loadTexts:
    bIPPoolGroupEntry.setStatus("current")
_BIPPoolGroupStatsInterval_Type = Integer32
_BIPPoolGroupStatsInterval_Object = MibTableColumn
bIPPoolGroupStatsInterval = _BIPPoolGroupStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 1),
    _BIPPoolGroupStatsInterval_Type()
)
bIPPoolGroupStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolGroupStatsInterval.setStatus("current")
_BIPPoolGroupIndex_Type = Integer32
_BIPPoolGroupIndex_Object = MibTableColumn
bIPPoolGroupIndex = _BIPPoolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 2),
    _BIPPoolGroupIndex_Type()
)
bIPPoolGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolGroupIndex.setStatus("current")
_BIPPoolGroupIntervalDuration_Type = Integer32
_BIPPoolGroupIntervalDuration_Object = MibTableColumn
bIPPoolGroupIntervalDuration = _BIPPoolGroupIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 3),
    _BIPPoolGroupIntervalDuration_Type()
)
bIPPoolGroupIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupIntervalDuration.setStatus("current")
_BIPPoolGroupName_Type = DisplayString
_BIPPoolGroupName_Object = MibTableColumn
bIPPoolGroupName = _BIPPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 4),
    _BIPPoolGroupName_Type()
)
bIPPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupName.setStatus("current")
_BIPPoolGroupTotalAddresses_Type = Unsigned32
_BIPPoolGroupTotalAddresses_Object = MibTableColumn
bIPPoolGroupTotalAddresses = _BIPPoolGroupTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 5),
    _BIPPoolGroupTotalAddresses_Type()
)
bIPPoolGroupTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupTotalAddresses.setStatus("current")
_BIPPoolGroupReservedAddresses_Type = Unsigned32
_BIPPoolGroupReservedAddresses_Object = MibTableColumn
bIPPoolGroupReservedAddresses = _BIPPoolGroupReservedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 6),
    _BIPPoolGroupReservedAddresses_Type()
)
bIPPoolGroupReservedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupReservedAddresses.setStatus("current")
_BIPPoolGroupPeakFreeAddresses_Type = Unsigned32
_BIPPoolGroupPeakFreeAddresses_Object = MibTableColumn
bIPPoolGroupPeakFreeAddresses = _BIPPoolGroupPeakFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 7),
    _BIPPoolGroupPeakFreeAddresses_Type()
)
bIPPoolGroupPeakFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupPeakFreeAddresses.setStatus("current")
_BIPPoolGroupPeakUsedAddresses_Type = Unsigned32
_BIPPoolGroupPeakUsedAddresses_Object = MibTableColumn
bIPPoolGroupPeakUsedAddresses = _BIPPoolGroupPeakUsedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 8),
    _BIPPoolGroupPeakUsedAddresses_Type()
)
bIPPoolGroupPeakUsedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGroupPeakUsedAddresses.setStatus("current")
_BIPPoolGlobalTable_Object = MibTable
bIPPoolGlobalTable = _BIPPoolGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    bIPPoolGlobalTable.setStatus("current")
_BIPPoolGlobalEntry_Object = MibTableRow
bIPPoolGlobalEntry = _BIPPoolGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1)
)
bIPPoolGlobalEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPPoolGlobalStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPPoolClientIndex"),
)
if mibBuilder.loadTexts:
    bIPPoolGlobalEntry.setStatus("current")
_BIPPoolGlobalStatsInterval_Type = Integer32
_BIPPoolGlobalStatsInterval_Object = MibTableColumn
bIPPoolGlobalStatsInterval = _BIPPoolGlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 1),
    _BIPPoolGlobalStatsInterval_Type()
)
bIPPoolGlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolGlobalStatsInterval.setStatus("current")
_BIPPoolClientIndex_Type = Integer32
_BIPPoolClientIndex_Object = MibTableColumn
bIPPoolClientIndex = _BIPPoolClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 2),
    _BIPPoolClientIndex_Type()
)
bIPPoolClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPoolClientIndex.setStatus("current")
_BIPPoolClientName_Type = DisplayString
_BIPPoolClientName_Object = MibTableColumn
bIPPoolClientName = _BIPPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 3),
    _BIPPoolClientName_Type()
)
bIPPoolClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolClientName.setStatus("current")
_BIPPoolGlobalAllocReq_Type = Unsigned32
_BIPPoolGlobalAllocReq_Object = MibTableColumn
bIPPoolGlobalAllocReq = _BIPPoolGlobalAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 4),
    _BIPPoolGlobalAllocReq_Type()
)
bIPPoolGlobalAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalAllocReq.setStatus("current")
_BIPPoolGlobalAllocReqSucc_Type = Unsigned32
_BIPPoolGlobalAllocReqSucc_Object = MibTableColumn
bIPPoolGlobalAllocReqSucc = _BIPPoolGlobalAllocReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 5),
    _BIPPoolGlobalAllocReqSucc_Type()
)
bIPPoolGlobalAllocReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalAllocReqSucc.setStatus("current")
_BIPPoolGlobalAllocReqUnSucc_Type = Unsigned32
_BIPPoolGlobalAllocReqUnSucc_Object = MibTableColumn
bIPPoolGlobalAllocReqUnSucc = _BIPPoolGlobalAllocReqUnSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 6),
    _BIPPoolGlobalAllocReqUnSucc_Type()
)
bIPPoolGlobalAllocReqUnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalAllocReqUnSucc.setStatus("current")
_BIPPoolGlobalDupAllocReq_Type = Unsigned32
_BIPPoolGlobalDupAllocReq_Object = MibTableColumn
bIPPoolGlobalDupAllocReq = _BIPPoolGlobalDupAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 7),
    _BIPPoolGlobalDupAllocReq_Type()
)
bIPPoolGlobalDupAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalDupAllocReq.setStatus("current")
_BIPPoolGlobalStaticAllocReq_Type = Unsigned32
_BIPPoolGlobalStaticAllocReq_Object = MibTableColumn
bIPPoolGlobalStaticAllocReq = _BIPPoolGlobalStaticAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 8),
    _BIPPoolGlobalStaticAllocReq_Type()
)
bIPPoolGlobalStaticAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalStaticAllocReq.setStatus("current")
_BIPPoolGlobalAllocResponses_Type = Unsigned32
_BIPPoolGlobalAllocResponses_Object = MibTableColumn
bIPPoolGlobalAllocResponses = _BIPPoolGlobalAllocResponses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 9),
    _BIPPoolGlobalAllocResponses_Type()
)
bIPPoolGlobalAllocResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalAllocResponses.setStatus("current")
_BIPPoolGlobalDeAllocReq_Type = Unsigned32
_BIPPoolGlobalDeAllocReq_Object = MibTableColumn
bIPPoolGlobalDeAllocReq = _BIPPoolGlobalDeAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 10),
    _BIPPoolGlobalDeAllocReq_Type()
)
bIPPoolGlobalDeAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalDeAllocReq.setStatus("current")
_BIPPoolGlobalDeAllocReqSucc_Type = Unsigned32
_BIPPoolGlobalDeAllocReqSucc_Object = MibTableColumn
bIPPoolGlobalDeAllocReqSucc = _BIPPoolGlobalDeAllocReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 11),
    _BIPPoolGlobalDeAllocReqSucc_Type()
)
bIPPoolGlobalDeAllocReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalDeAllocReqSucc.setStatus("current")
_BIPPoolGlobalDeAllocReqUnSucc_Type = Unsigned32
_BIPPoolGlobalDeAllocReqUnSucc_Object = MibTableColumn
bIPPoolGlobalDeAllocReqUnSucc = _BIPPoolGlobalDeAllocReqUnSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 12),
    _BIPPoolGlobalDeAllocReqUnSucc_Type()
)
bIPPoolGlobalDeAllocReqUnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalDeAllocReqUnSucc.setStatus("current")
_BIPPoolGlobalInvalidReq_Type = Unsigned32
_BIPPoolGlobalInvalidReq_Object = MibTableColumn
bIPPoolGlobalInvalidReq = _BIPPoolGlobalInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 13),
    _BIPPoolGlobalInvalidReq_Type()
)
bIPPoolGlobalInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalInvalidReq.setStatus("current")
_BIPPoolGlobalNotAvailCount_Type = Unsigned32
_BIPPoolGlobalNotAvailCount_Object = MibTableColumn
bIPPoolGlobalNotAvailCount = _BIPPoolGlobalNotAvailCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 14),
    _BIPPoolGlobalNotAvailCount_Type()
)
bIPPoolGlobalNotAvailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalNotAvailCount.setStatus("current")
_BIPPoolGlobalPoolExhaustedCount_Type = Unsigned32
_BIPPoolGlobalPoolExhaustedCount_Object = MibTableColumn
bIPPoolGlobalPoolExhaustedCount = _BIPPoolGlobalPoolExhaustedCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 15),
    _BIPPoolGlobalPoolExhaustedCount_Type()
)
bIPPoolGlobalPoolExhaustedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalPoolExhaustedCount.setStatus("current")
_BIPPoolGlobalGroupExhaustedCount_Type = Unsigned32
_BIPPoolGlobalGroupExhaustedCount_Object = MibTableColumn
bIPPoolGlobalGroupExhaustedCount = _BIPPoolGlobalGroupExhaustedCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 16),
    _BIPPoolGlobalGroupExhaustedCount_Type()
)
bIPPoolGlobalGroupExhaustedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalGroupExhaustedCount.setStatus("current")
_BIPPoolGlobalInvalidPoolNameCount_Type = Unsigned32
_BIPPoolGlobalInvalidPoolNameCount_Object = MibTableColumn
bIPPoolGlobalInvalidPoolNameCount = _BIPPoolGlobalInvalidPoolNameCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 17),
    _BIPPoolGlobalInvalidPoolNameCount_Type()
)
bIPPoolGlobalInvalidPoolNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalInvalidPoolNameCount.setStatus("current")
_BIPPoolGlobalInvalidGroupNameCount_Type = Unsigned32
_BIPPoolGlobalInvalidGroupNameCount_Object = MibTableColumn
bIPPoolGlobalInvalidGroupNameCount = _BIPPoolGlobalInvalidGroupNameCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 18),
    _BIPPoolGlobalInvalidGroupNameCount_Type()
)
bIPPoolGlobalInvalidGroupNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalInvalidGroupNameCount.setStatus("current")
_BIPPoolGlobalInvalidIPAddrCount_Type = Unsigned32
_BIPPoolGlobalInvalidIPAddrCount_Object = MibTableColumn
bIPPoolGlobalInvalidIPAddrCount = _BIPPoolGlobalInvalidIPAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 19),
    _BIPPoolGlobalInvalidIPAddrCount_Type()
)
bIPPoolGlobalInvalidIPAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalInvalidIPAddrCount.setStatus("current")
_BIPPoolGlobalHashInsertFail_Type = Unsigned32
_BIPPoolGlobalHashInsertFail_Object = MibTableColumn
bIPPoolGlobalHashInsertFail = _BIPPoolGlobalHashInsertFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 20),
    _BIPPoolGlobalHashInsertFail_Type()
)
bIPPoolGlobalHashInsertFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalHashInsertFail.setStatus("current")
_BIPPoolGlobalHashDeleteFail_Type = Unsigned32
_BIPPoolGlobalHashDeleteFail_Object = MibTableColumn
bIPPoolGlobalHashDeleteFail = _BIPPoolGlobalHashDeleteFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 21),
    _BIPPoolGlobalHashDeleteFail_Type()
)
bIPPoolGlobalHashDeleteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalHashDeleteFail.setStatus("current")
_BIPPoolGlobalRequestedAllocatedMismacth_Type = Unsigned32
_BIPPoolGlobalRequestedAllocatedMismacth_Object = MibTableColumn
bIPPoolGlobalRequestedAllocatedMismacth = _BIPPoolGlobalRequestedAllocatedMismacth_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 22),
    _BIPPoolGlobalRequestedAllocatedMismacth_Type()
)
bIPPoolGlobalRequestedAllocatedMismacth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalRequestedAllocatedMismacth.setStatus("current")
_BIPPoolGlobalRequestedIPNotFree_Type = Unsigned32
_BIPPoolGlobalRequestedIPNotFree_Object = MibTableColumn
bIPPoolGlobalRequestedIPNotFree = _BIPPoolGlobalRequestedIPNotFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 23),
    _BIPPoolGlobalRequestedIPNotFree_Type()
)
bIPPoolGlobalRequestedIPNotFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalRequestedIPNotFree.setStatus("current")
_BIPPoolGlobalGenErrCount_Type = Unsigned32
_BIPPoolGlobalGenErrCount_Object = MibTableColumn
bIPPoolGlobalGenErrCount = _BIPPoolGlobalGenErrCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 24),
    _BIPPoolGlobalGenErrCount_Type()
)
bIPPoolGlobalGenErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalGenErrCount.setStatus("current")
_BIPPoolGlobalAddrRelDueToIntAdd_Type = Unsigned32
_BIPPoolGlobalAddrRelDueToIntAdd_Object = MibTableColumn
bIPPoolGlobalAddrRelDueToIntAdd = _BIPPoolGlobalAddrRelDueToIntAdd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 25),
    _BIPPoolGlobalAddrRelDueToIntAdd_Type()
)
bIPPoolGlobalAddrRelDueToIntAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalAddrRelDueToIntAdd.setStatus("current")
_BIPPoolGlobalGroupDeAllocReq_Type = Unsigned32
_BIPPoolGlobalGroupDeAllocReq_Object = MibTableColumn
bIPPoolGlobalGroupDeAllocReq = _BIPPoolGlobalGroupDeAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 26),
    _BIPPoolGlobalGroupDeAllocReq_Type()
)
bIPPoolGlobalGroupDeAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalGroupDeAllocReq.setStatus("current")
_BIPPoolGlobalGroupDeAllocReqSucc_Type = Unsigned32
_BIPPoolGlobalGroupDeAllocReqSucc_Object = MibTableColumn
bIPPoolGlobalGroupDeAllocReqSucc = _BIPPoolGlobalGroupDeAllocReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 27),
    _BIPPoolGlobalGroupDeAllocReqSucc_Type()
)
bIPPoolGlobalGroupDeAllocReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalGroupDeAllocReqSucc.setStatus("current")
_BIPPoolGlobalGroupDeAllocReqUnSucc_Type = Unsigned32
_BIPPoolGlobalGroupDeAllocReqUnSucc_Object = MibTableColumn
bIPPoolGlobalGroupDeAllocReqUnSucc = _BIPPoolGlobalGroupDeAllocReqUnSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 28),
    _BIPPoolGlobalGroupDeAllocReqUnSucc_Type()
)
bIPPoolGlobalGroupDeAllocReqUnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalGroupDeAllocReqUnSucc.setStatus("current")
_BIPPoolTotalPoolCreatedEvents_Type = Unsigned32
_BIPPoolTotalPoolCreatedEvents_Object = MibTableColumn
bIPPoolTotalPoolCreatedEvents = _BIPPoolTotalPoolCreatedEvents_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 29),
    _BIPPoolTotalPoolCreatedEvents_Type()
)
bIPPoolTotalPoolCreatedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolTotalPoolCreatedEvents.setStatus("current")
_BIPPoolTotalPoolDeletedEvents_Type = Unsigned32
_BIPPoolTotalPoolDeletedEvents_Object = MibTableColumn
bIPPoolTotalPoolDeletedEvents = _BIPPoolTotalPoolDeletedEvents_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 30),
    _BIPPoolTotalPoolDeletedEvents_Type()
)
bIPPoolTotalPoolDeletedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolTotalPoolDeletedEvents.setStatus("current")
_BIPPoolGlobalIntervalDuration_Type = Integer32
_BIPPoolGlobalIntervalDuration_Object = MibTableColumn
bIPPoolGlobalIntervalDuration = _BIPPoolGlobalIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 31),
    _BIPPoolGlobalIntervalDuration_Type()
)
bIPPoolGlobalIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPoolGlobalIntervalDuration.setStatus("current")
_BIPv4PoolNotifObjects_ObjectIdentity = ObjectIdentity
bIPv4PoolNotifObjects = _BIPv4PoolNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bIPv4PoolNotifObjects.setStatus("current")
_BIPv6PoolMIBObjects_ObjectIdentity = ObjectIdentity
bIPv6PoolMIBObjects = _BIPv6PoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    bIPv6PoolMIBObjects.setStatus("current")
_BIPv6PoolTable_Object = MibTable
bIPv6PoolTable = _BIPv6PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    bIPv6PoolTable.setStatus("current")
_BIPv6PoolEntry_Object = MibTableRow
bIPv6PoolEntry = _BIPv6PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1)
)
bIPv6PoolEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolIndex"),
)
if mibBuilder.loadTexts:
    bIPv6PoolEntry.setStatus("current")
_BIPv6PoolStatsInterval_Type = Integer32
_BIPv6PoolStatsInterval_Object = MibTableColumn
bIPv6PoolStatsInterval = _BIPv6PoolStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 1),
    _BIPv6PoolStatsInterval_Type()
)
bIPv6PoolStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolStatsInterval.setStatus("current")
_BIPv6PoolIndex_Type = Integer32
_BIPv6PoolIndex_Object = MibTableColumn
bIPv6PoolIndex = _BIPv6PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 2),
    _BIPv6PoolIndex_Type()
)
bIPv6PoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolIndex.setStatus("current")
_BIPv6PoolIntervalDuration_Type = Integer32
_BIPv6PoolIntervalDuration_Object = MibTableColumn
bIPv6PoolIntervalDuration = _BIPv6PoolIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 3),
    _BIPv6PoolIntervalDuration_Type()
)
bIPv6PoolIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolIntervalDuration.setStatus("current")
_BIPv6PoolName_Type = DisplayString
_BIPv6PoolName_Object = MibTableColumn
bIPv6PoolName = _BIPv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 4),
    _BIPv6PoolName_Type()
)
bIPv6PoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolName.setStatus("current")
_BIPv6PoolStartPrefix_Type = InetAddressIPv6
_BIPv6PoolStartPrefix_Object = MibTableColumn
bIPv6PoolStartPrefix = _BIPv6PoolStartPrefix_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 5),
    _BIPv6PoolStartPrefix_Type()
)
bIPv6PoolStartPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolStartPrefix.setStatus("current")
_BIPv6PoolEndPrefix_Type = InetAddressIPv6
_BIPv6PoolEndPrefix_Object = MibTableColumn
bIPv6PoolEndPrefix = _BIPv6PoolEndPrefix_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 6),
    _BIPv6PoolEndPrefix_Type()
)
bIPv6PoolEndPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolEndPrefix.setStatus("current")
_BIPv6PoolTotalPrefixes_Type = Unsigned32
_BIPv6PoolTotalPrefixes_Object = MibTableColumn
bIPv6PoolTotalPrefixes = _BIPv6PoolTotalPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 7),
    _BIPv6PoolTotalPrefixes_Type()
)
bIPv6PoolTotalPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolTotalPrefixes.setStatus("current")
_BIPv6PoolReservedPrefixes_Type = Unsigned32
_BIPv6PoolReservedPrefixes_Object = MibTableColumn
bIPv6PoolReservedPrefixes = _BIPv6PoolReservedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 8),
    _BIPv6PoolReservedPrefixes_Type()
)
bIPv6PoolReservedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolReservedPrefixes.setStatus("current")
_BIPv6PoolPeakFreePrefixes_Type = Unsigned32
_BIPv6PoolPeakFreePrefixes_Object = MibTableColumn
bIPv6PoolPeakFreePrefixes = _BIPv6PoolPeakFreePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 9),
    _BIPv6PoolPeakFreePrefixes_Type()
)
bIPv6PoolPeakFreePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolPeakFreePrefixes.setStatus("current")
_BIPv6PoolPeakUsedPrefixes_Type = Unsigned32
_BIPv6PoolPeakUsedPrefixes_Object = MibTableColumn
bIPv6PoolPeakUsedPrefixes = _BIPv6PoolPeakUsedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 10),
    _BIPv6PoolPeakUsedPrefixes_Type()
)
bIPv6PoolPeakUsedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolPeakUsedPrefixes.setStatus("current")
_BIPv6PoolUsedPrefixLowThreshold_Type = Unsigned32
_BIPv6PoolUsedPrefixLowThreshold_Object = MibTableColumn
bIPv6PoolUsedPrefixLowThreshold = _BIPv6PoolUsedPrefixLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 11),
    _BIPv6PoolUsedPrefixLowThreshold_Type()
)
bIPv6PoolUsedPrefixLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolUsedPrefixLowThreshold.setStatus("current")
_BIPv6PoolUsedPrefixHighThreshold_Type = Unsigned32
_BIPv6PoolUsedPrefixHighThreshold_Object = MibTableColumn
bIPv6PoolUsedPrefixHighThreshold = _BIPv6PoolUsedPrefixHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 12),
    _BIPv6PoolUsedPrefixHighThreshold_Type()
)
bIPv6PoolUsedPrefixHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolUsedPrefixHighThreshold.setStatus("current")
_BIPv6PoolGrpName_Type = DisplayString
_BIPv6PoolGrpName_Object = MibTableColumn
bIPv6PoolGrpName = _BIPv6PoolGrpName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 13),
    _BIPv6PoolGrpName_Type()
)
bIPv6PoolGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGrpName.setStatus("current")
_BIPv6PoolGroupTable_Object = MibTable
bIPv6PoolGroupTable = _BIPv6PoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    bIPv6PoolGroupTable.setStatus("current")
_BIPv6PoolGroupEntry_Object = MibTableRow
bIPv6PoolGroupEntry = _BIPv6PoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1)
)
bIPv6PoolGroupEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolGroupStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolGroupIndex"),
)
if mibBuilder.loadTexts:
    bIPv6PoolGroupEntry.setStatus("current")
_BIPv6PoolGroupStatsInterval_Type = Integer32
_BIPv6PoolGroupStatsInterval_Object = MibTableColumn
bIPv6PoolGroupStatsInterval = _BIPv6PoolGroupStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 1),
    _BIPv6PoolGroupStatsInterval_Type()
)
bIPv6PoolGroupStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolGroupStatsInterval.setStatus("current")
_BIPv6PoolGroupIndex_Type = Integer32
_BIPv6PoolGroupIndex_Object = MibTableColumn
bIPv6PoolGroupIndex = _BIPv6PoolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 2),
    _BIPv6PoolGroupIndex_Type()
)
bIPv6PoolGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolGroupIndex.setStatus("current")
_BIPv6PoolGroupIntervalDuration_Type = Integer32
_BIPv6PoolGroupIntervalDuration_Object = MibTableColumn
bIPv6PoolGroupIntervalDuration = _BIPv6PoolGroupIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 3),
    _BIPv6PoolGroupIntervalDuration_Type()
)
bIPv6PoolGroupIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupIntervalDuration.setStatus("current")
_BIPv6PoolGroupName_Type = DisplayString
_BIPv6PoolGroupName_Object = MibTableColumn
bIPv6PoolGroupName = _BIPv6PoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 4),
    _BIPv6PoolGroupName_Type()
)
bIPv6PoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupName.setStatus("current")
_BIPv6PoolGroupTotalPrefixes_Type = Unsigned32
_BIPv6PoolGroupTotalPrefixes_Object = MibTableColumn
bIPv6PoolGroupTotalPrefixes = _BIPv6PoolGroupTotalPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 5),
    _BIPv6PoolGroupTotalPrefixes_Type()
)
bIPv6PoolGroupTotalPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupTotalPrefixes.setStatus("current")
_BIPv6PoolGroupReservedPrefixes_Type = Unsigned32
_BIPv6PoolGroupReservedPrefixes_Object = MibTableColumn
bIPv6PoolGroupReservedPrefixes = _BIPv6PoolGroupReservedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 6),
    _BIPv6PoolGroupReservedPrefixes_Type()
)
bIPv6PoolGroupReservedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupReservedPrefixes.setStatus("current")
_BIPv6PoolGroupPeakFreePrefixes_Type = Unsigned32
_BIPv6PoolGroupPeakFreePrefixes_Object = MibTableColumn
bIPv6PoolGroupPeakFreePrefixes = _BIPv6PoolGroupPeakFreePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 7),
    _BIPv6PoolGroupPeakFreePrefixes_Type()
)
bIPv6PoolGroupPeakFreePrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupPeakFreePrefixes.setStatus("current")
_BIPv6PoolGroupPeakUsedPrefixes_Type = Unsigned32
_BIPv6PoolGroupPeakUsedPrefixes_Object = MibTableColumn
bIPv6PoolGroupPeakUsedPrefixes = _BIPv6PoolGroupPeakUsedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 8),
    _BIPv6PoolGroupPeakUsedPrefixes_Type()
)
bIPv6PoolGroupPeakUsedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGroupPeakUsedPrefixes.setStatus("current")
_BIPv6PoolGlobalTable_Object = MibTable
bIPv6PoolGlobalTable = _BIPv6PoolGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    bIPv6PoolGlobalTable.setStatus("current")
_BIPv6PoolGlobalEntry_Object = MibTableRow
bIPv6PoolGlobalEntry = _BIPv6PoolGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1)
)
bIPv6PoolGlobalEntry.setIndexNames(
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolGlobalStatsInterval"),
    (0, "BENU-IPPOOL-MIB", "bIPv6PoolClientIndex"),
)
if mibBuilder.loadTexts:
    bIPv6PoolGlobalEntry.setStatus("current")
_BIPv6PoolGlobalStatsInterval_Type = Integer32
_BIPv6PoolGlobalStatsInterval_Object = MibTableColumn
bIPv6PoolGlobalStatsInterval = _BIPv6PoolGlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 1),
    _BIPv6PoolGlobalStatsInterval_Type()
)
bIPv6PoolGlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalStatsInterval.setStatus("current")
_BIPv6PoolClientIndex_Type = Integer32
_BIPv6PoolClientIndex_Object = MibTableColumn
bIPv6PoolClientIndex = _BIPv6PoolClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 2),
    _BIPv6PoolClientIndex_Type()
)
bIPv6PoolClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPv6PoolClientIndex.setStatus("current")
_BIPv6PoolClientName_Type = DisplayString
_BIPv6PoolClientName_Object = MibTableColumn
bIPv6PoolClientName = _BIPv6PoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 3),
    _BIPv6PoolClientName_Type()
)
bIPv6PoolClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolClientName.setStatus("current")
_BIPv6PoolGlobalAllocReq_Type = Unsigned32
_BIPv6PoolGlobalAllocReq_Object = MibTableColumn
bIPv6PoolGlobalAllocReq = _BIPv6PoolGlobalAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 4),
    _BIPv6PoolGlobalAllocReq_Type()
)
bIPv6PoolGlobalAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalAllocReq.setStatus("current")
_BIPv6PoolGlobalAllocReqSucc_Type = Unsigned32
_BIPv6PoolGlobalAllocReqSucc_Object = MibTableColumn
bIPv6PoolGlobalAllocReqSucc = _BIPv6PoolGlobalAllocReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 5),
    _BIPv6PoolGlobalAllocReqSucc_Type()
)
bIPv6PoolGlobalAllocReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalAllocReqSucc.setStatus("current")
_BIPv6PoolGlobalAllocReqUnSucc_Type = Unsigned32
_BIPv6PoolGlobalAllocReqUnSucc_Object = MibTableColumn
bIPv6PoolGlobalAllocReqUnSucc = _BIPv6PoolGlobalAllocReqUnSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 6),
    _BIPv6PoolGlobalAllocReqUnSucc_Type()
)
bIPv6PoolGlobalAllocReqUnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalAllocReqUnSucc.setStatus("current")
_BIPv6PoolGlobalDupAllocReq_Type = Unsigned32
_BIPv6PoolGlobalDupAllocReq_Object = MibTableColumn
bIPv6PoolGlobalDupAllocReq = _BIPv6PoolGlobalDupAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 7),
    _BIPv6PoolGlobalDupAllocReq_Type()
)
bIPv6PoolGlobalDupAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalDupAllocReq.setStatus("current")
_BIPv6PoolGlobalStaticAllocReq_Type = Unsigned32
_BIPv6PoolGlobalStaticAllocReq_Object = MibTableColumn
bIPv6PoolGlobalStaticAllocReq = _BIPv6PoolGlobalStaticAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 8),
    _BIPv6PoolGlobalStaticAllocReq_Type()
)
bIPv6PoolGlobalStaticAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalStaticAllocReq.setStatus("current")
_BIPv6PoolGlobalAllocResponses_Type = Unsigned32
_BIPv6PoolGlobalAllocResponses_Object = MibTableColumn
bIPv6PoolGlobalAllocResponses = _BIPv6PoolGlobalAllocResponses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 9),
    _BIPv6PoolGlobalAllocResponses_Type()
)
bIPv6PoolGlobalAllocResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalAllocResponses.setStatus("current")
_BIPv6PoolGlobalDeAllocReq_Type = Unsigned32
_BIPv6PoolGlobalDeAllocReq_Object = MibTableColumn
bIPv6PoolGlobalDeAllocReq = _BIPv6PoolGlobalDeAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 10),
    _BIPv6PoolGlobalDeAllocReq_Type()
)
bIPv6PoolGlobalDeAllocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalDeAllocReq.setStatus("current")
_BIPv6PoolGlobalDeAllocReqSucc_Type = Unsigned32
_BIPv6PoolGlobalDeAllocReqSucc_Object = MibTableColumn
bIPv6PoolGlobalDeAllocReqSucc = _BIPv6PoolGlobalDeAllocReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 11),
    _BIPv6PoolGlobalDeAllocReqSucc_Type()
)
bIPv6PoolGlobalDeAllocReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalDeAllocReqSucc.setStatus("current")
_BIPv6PoolGlobalDeAllocReqUnSucc_Type = Unsigned32
_BIPv6PoolGlobalDeAllocReqUnSucc_Object = MibTableColumn
bIPv6PoolGlobalDeAllocReqUnSucc = _BIPv6PoolGlobalDeAllocReqUnSucc_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 12),
    _BIPv6PoolGlobalDeAllocReqUnSucc_Type()
)
bIPv6PoolGlobalDeAllocReqUnSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalDeAllocReqUnSucc.setStatus("current")
_BIPv6PoolGlobalInvalidReq_Type = Unsigned32
_BIPv6PoolGlobalInvalidReq_Object = MibTableColumn
bIPv6PoolGlobalInvalidReq = _BIPv6PoolGlobalInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 13),
    _BIPv6PoolGlobalInvalidReq_Type()
)
bIPv6PoolGlobalInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalInvalidReq.setStatus("current")
_BIPv6PoolGlobalNotAvailCount_Type = Unsigned32
_BIPv6PoolGlobalNotAvailCount_Object = MibTableColumn
bIPv6PoolGlobalNotAvailCount = _BIPv6PoolGlobalNotAvailCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 14),
    _BIPv6PoolGlobalNotAvailCount_Type()
)
bIPv6PoolGlobalNotAvailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalNotAvailCount.setStatus("current")
_BIPv6PoolGlobalPoolExhaustedCount_Type = Unsigned32
_BIPv6PoolGlobalPoolExhaustedCount_Object = MibTableColumn
bIPv6PoolGlobalPoolExhaustedCount = _BIPv6PoolGlobalPoolExhaustedCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 15),
    _BIPv6PoolGlobalPoolExhaustedCount_Type()
)
bIPv6PoolGlobalPoolExhaustedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalPoolExhaustedCount.setStatus("current")
_BIPv6PoolGlobalGroupExhaustedCount_Type = Unsigned32
_BIPv6PoolGlobalGroupExhaustedCount_Object = MibTableColumn
bIPv6PoolGlobalGroupExhaustedCount = _BIPv6PoolGlobalGroupExhaustedCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 16),
    _BIPv6PoolGlobalGroupExhaustedCount_Type()
)
bIPv6PoolGlobalGroupExhaustedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalGroupExhaustedCount.setStatus("current")
_BIPv6PoolGlobalInvalidPoolNameCount_Type = Unsigned32
_BIPv6PoolGlobalInvalidPoolNameCount_Object = MibTableColumn
bIPv6PoolGlobalInvalidPoolNameCount = _BIPv6PoolGlobalInvalidPoolNameCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 17),
    _BIPv6PoolGlobalInvalidPoolNameCount_Type()
)
bIPv6PoolGlobalInvalidPoolNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalInvalidPoolNameCount.setStatus("current")
_BIPv6PoolGlobalInvalidGroupNameCount_Type = Unsigned32
_BIPv6PoolGlobalInvalidGroupNameCount_Object = MibTableColumn
bIPv6PoolGlobalInvalidGroupNameCount = _BIPv6PoolGlobalInvalidGroupNameCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 18),
    _BIPv6PoolGlobalInvalidGroupNameCount_Type()
)
bIPv6PoolGlobalInvalidGroupNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalInvalidGroupNameCount.setStatus("current")
_BIPv6PoolGlobalInvalidIPAddrCount_Type = Unsigned32
_BIPv6PoolGlobalInvalidIPAddrCount_Object = MibTableColumn
bIPv6PoolGlobalInvalidIPAddrCount = _BIPv6PoolGlobalInvalidIPAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 19),
    _BIPv6PoolGlobalInvalidIPAddrCount_Type()
)
bIPv6PoolGlobalInvalidIPAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalInvalidIPAddrCount.setStatus("current")
_BIPv6PoolGlobalHashInsertFail_Type = Unsigned32
_BIPv6PoolGlobalHashInsertFail_Object = MibTableColumn
bIPv6PoolGlobalHashInsertFail = _BIPv6PoolGlobalHashInsertFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 20),
    _BIPv6PoolGlobalHashInsertFail_Type()
)
bIPv6PoolGlobalHashInsertFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalHashInsertFail.setStatus("current")
_BIPv6PoolGlobalHashDeleteFail_Type = Unsigned32
_BIPv6PoolGlobalHashDeleteFail_Object = MibTableColumn
bIPv6PoolGlobalHashDeleteFail = _BIPv6PoolGlobalHashDeleteFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 21),
    _BIPv6PoolGlobalHashDeleteFail_Type()
)
bIPv6PoolGlobalHashDeleteFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalHashDeleteFail.setStatus("current")
_BIPv6PoolGlobalRequestedAllocatedMismacth_Type = Unsigned32
_BIPv6PoolGlobalRequestedAllocatedMismacth_Object = MibTableColumn
bIPv6PoolGlobalRequestedAllocatedMismacth = _BIPv6PoolGlobalRequestedAllocatedMismacth_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 22),
    _BIPv6PoolGlobalRequestedAllocatedMismacth_Type()
)
bIPv6PoolGlobalRequestedAllocatedMismacth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalRequestedAllocatedMismacth.setStatus("current")
_BIPv6PoolGlobalRequestedIPNotFree_Type = Unsigned32
_BIPv6PoolGlobalRequestedIPNotFree_Object = MibTableColumn
bIPv6PoolGlobalRequestedIPNotFree = _BIPv6PoolGlobalRequestedIPNotFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 23),
    _BIPv6PoolGlobalRequestedIPNotFree_Type()
)
bIPv6PoolGlobalRequestedIPNotFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalRequestedIPNotFree.setStatus("current")
_BIPv6PoolGlobalGenErrCount_Type = Unsigned32
_BIPv6PoolGlobalGenErrCount_Object = MibTableColumn
bIPv6PoolGlobalGenErrCount = _BIPv6PoolGlobalGenErrCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 24),
    _BIPv6PoolGlobalGenErrCount_Type()
)
bIPv6PoolGlobalGenErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalGenErrCount.setStatus("current")
_BIPv6PoolGlobalPrefixRelDueToIntAdd_Type = Unsigned32
_BIPv6PoolGlobalPrefixRelDueToIntAdd_Object = MibTableColumn
bIPv6PoolGlobalPrefixRelDueToIntAdd = _BIPv6PoolGlobalPrefixRelDueToIntAdd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 25),
    _BIPv6PoolGlobalPrefixRelDueToIntAdd_Type()
)
bIPv6PoolGlobalPrefixRelDueToIntAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalPrefixRelDueToIntAdd.setStatus("current")
_BIPv6PoolTotalPoolCreatedEvents_Type = Unsigned32
_BIPv6PoolTotalPoolCreatedEvents_Object = MibTableColumn
bIPv6PoolTotalPoolCreatedEvents = _BIPv6PoolTotalPoolCreatedEvents_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 26),
    _BIPv6PoolTotalPoolCreatedEvents_Type()
)
bIPv6PoolTotalPoolCreatedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolTotalPoolCreatedEvents.setStatus("current")
_BIPv6PoolTotalPoolDeletedEvents_Type = Unsigned32
_BIPv6PoolTotalPoolDeletedEvents_Object = MibTableColumn
bIPv6PoolTotalPoolDeletedEvents = _BIPv6PoolTotalPoolDeletedEvents_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 27),
    _BIPv6PoolTotalPoolDeletedEvents_Type()
)
bIPv6PoolTotalPoolDeletedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolTotalPoolDeletedEvents.setStatus("current")
_BIPv6PoolGlobalIntervalDuration_Type = Integer32
_BIPv6PoolGlobalIntervalDuration_Object = MibTableColumn
bIPv6PoolGlobalIntervalDuration = _BIPv6PoolGlobalIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 28),
    _BIPv6PoolGlobalIntervalDuration_Type()
)
bIPv6PoolGlobalIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPv6PoolGlobalIntervalDuration.setStatus("current")
_BIPv6PoolNotifObjects_ObjectIdentity = ObjectIdentity
bIPv6PoolNotifObjects = _BIPv6PoolNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    bIPv6PoolNotifObjects.setStatus("current")

# Managed Objects groups


# Notification objects

bIPPoolUsedAddrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 1)
)
bIPPoolUsedAddrLow.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPPoolName"),
        ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"),
        ("BENU-IPPOOL-MIB", "bIPPoolUsedAddrLowThreshold"))
)
if mibBuilder.loadTexts:
    bIPPoolUsedAddrLow.setStatus(
        "current"
    )

bIPPoolUsedAddrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 2)
)
bIPPoolUsedAddrHigh.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPPoolName"),
        ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"),
        ("BENU-IPPOOL-MIB", "bIPPoolUsedAddrHighThreshold"))
)
if mibBuilder.loadTexts:
    bIPPoolUsedAddrHigh.setStatus(
        "current"
    )

bIPv6PoolUsedPrefixLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 3)
)
bIPv6PoolUsedPrefixLow.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPv6PoolName"),
        ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"),
        ("BENU-IPPOOL-MIB", "bIPv6PoolUsedPrefixLowThreshold"))
)
if mibBuilder.loadTexts:
    bIPv6PoolUsedPrefixLow.setStatus(
        "current"
    )

bIPv6PoolUsedPrefixHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 4)
)
bIPv6PoolUsedPrefixHigh.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPv6PoolName"),
        ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"),
        ("BENU-IPPOOL-MIB", "bIPv6PoolUsedPrefixHighThreshold"))
)
if mibBuilder.loadTexts:
    bIPv6PoolUsedPrefixHigh.setStatus(
        "current"
    )

bIPPoolAddrExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 5)
)
bIPPoolAddrExhausted.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPPoolName"),
        ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"))
)
if mibBuilder.loadTexts:
    bIPPoolAddrExhausted.setStatus(
        "current"
    )

bIPv6PoolPrefixExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 6)
)
bIPv6PoolPrefixExhausted.setObjects(
      *(("BENU-IPPOOL-MIB", "bIPv6PoolName"),
        ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"))
)
if mibBuilder.loadTexts:
    bIPv6PoolPrefixExhausted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-IPPOOL-MIB",
    **{"benuIPPoolMIB": benuIPPoolMIB,
       "bIPPoolNotifications": bIPPoolNotifications,
       "bIPPoolUsedAddrLow": bIPPoolUsedAddrLow,
       "bIPPoolUsedAddrHigh": bIPPoolUsedAddrHigh,
       "bIPv6PoolUsedPrefixLow": bIPv6PoolUsedPrefixLow,
       "bIPv6PoolUsedPrefixHigh": bIPv6PoolUsedPrefixHigh,
       "bIPPoolAddrExhausted": bIPPoolAddrExhausted,
       "bIPv6PoolPrefixExhausted": bIPv6PoolPrefixExhausted,
       "bIPv4PoolMIBObjects": bIPv4PoolMIBObjects,
       "bIPPoolTable": bIPPoolTable,
       "bIPPoolEntry": bIPPoolEntry,
       "bIPPoolStatsInterval": bIPPoolStatsInterval,
       "bIPPoolIndex": bIPPoolIndex,
       "bIPPoolIntervalDuration": bIPPoolIntervalDuration,
       "bIPPoolName": bIPPoolName,
       "bIPPoolStartAddress": bIPPoolStartAddress,
       "bIPPoolEndAddress": bIPPoolEndAddress,
       "bIPPoolTotalAddresses": bIPPoolTotalAddresses,
       "bIPPoolReservedAddresses": bIPPoolReservedAddresses,
       "bIPPoolPeakFreeAddresses": bIPPoolPeakFreeAddresses,
       "bIPPoolPeakUsedAddresses": bIPPoolPeakUsedAddresses,
       "bIPPoolUsedAddrLowThreshold": bIPPoolUsedAddrLowThreshold,
       "bIPPoolUsedAddrHighThreshold": bIPPoolUsedAddrHighThreshold,
       "bIPPoolGrpName": bIPPoolGrpName,
       "bIPPoolGroupTable": bIPPoolGroupTable,
       "bIPPoolGroupEntry": bIPPoolGroupEntry,
       "bIPPoolGroupStatsInterval": bIPPoolGroupStatsInterval,
       "bIPPoolGroupIndex": bIPPoolGroupIndex,
       "bIPPoolGroupIntervalDuration": bIPPoolGroupIntervalDuration,
       "bIPPoolGroupName": bIPPoolGroupName,
       "bIPPoolGroupTotalAddresses": bIPPoolGroupTotalAddresses,
       "bIPPoolGroupReservedAddresses": bIPPoolGroupReservedAddresses,
       "bIPPoolGroupPeakFreeAddresses": bIPPoolGroupPeakFreeAddresses,
       "bIPPoolGroupPeakUsedAddresses": bIPPoolGroupPeakUsedAddresses,
       "bIPPoolGlobalTable": bIPPoolGlobalTable,
       "bIPPoolGlobalEntry": bIPPoolGlobalEntry,
       "bIPPoolGlobalStatsInterval": bIPPoolGlobalStatsInterval,
       "bIPPoolClientIndex": bIPPoolClientIndex,
       "bIPPoolClientName": bIPPoolClientName,
       "bIPPoolGlobalAllocReq": bIPPoolGlobalAllocReq,
       "bIPPoolGlobalAllocReqSucc": bIPPoolGlobalAllocReqSucc,
       "bIPPoolGlobalAllocReqUnSucc": bIPPoolGlobalAllocReqUnSucc,
       "bIPPoolGlobalDupAllocReq": bIPPoolGlobalDupAllocReq,
       "bIPPoolGlobalStaticAllocReq": bIPPoolGlobalStaticAllocReq,
       "bIPPoolGlobalAllocResponses": bIPPoolGlobalAllocResponses,
       "bIPPoolGlobalDeAllocReq": bIPPoolGlobalDeAllocReq,
       "bIPPoolGlobalDeAllocReqSucc": bIPPoolGlobalDeAllocReqSucc,
       "bIPPoolGlobalDeAllocReqUnSucc": bIPPoolGlobalDeAllocReqUnSucc,
       "bIPPoolGlobalInvalidReq": bIPPoolGlobalInvalidReq,
       "bIPPoolGlobalNotAvailCount": bIPPoolGlobalNotAvailCount,
       "bIPPoolGlobalPoolExhaustedCount": bIPPoolGlobalPoolExhaustedCount,
       "bIPPoolGlobalGroupExhaustedCount": bIPPoolGlobalGroupExhaustedCount,
       "bIPPoolGlobalInvalidPoolNameCount": bIPPoolGlobalInvalidPoolNameCount,
       "bIPPoolGlobalInvalidGroupNameCount": bIPPoolGlobalInvalidGroupNameCount,
       "bIPPoolGlobalInvalidIPAddrCount": bIPPoolGlobalInvalidIPAddrCount,
       "bIPPoolGlobalHashInsertFail": bIPPoolGlobalHashInsertFail,
       "bIPPoolGlobalHashDeleteFail": bIPPoolGlobalHashDeleteFail,
       "bIPPoolGlobalRequestedAllocatedMismacth": bIPPoolGlobalRequestedAllocatedMismacth,
       "bIPPoolGlobalRequestedIPNotFree": bIPPoolGlobalRequestedIPNotFree,
       "bIPPoolGlobalGenErrCount": bIPPoolGlobalGenErrCount,
       "bIPPoolGlobalAddrRelDueToIntAdd": bIPPoolGlobalAddrRelDueToIntAdd,
       "bIPPoolGlobalGroupDeAllocReq": bIPPoolGlobalGroupDeAllocReq,
       "bIPPoolGlobalGroupDeAllocReqSucc": bIPPoolGlobalGroupDeAllocReqSucc,
       "bIPPoolGlobalGroupDeAllocReqUnSucc": bIPPoolGlobalGroupDeAllocReqUnSucc,
       "bIPPoolTotalPoolCreatedEvents": bIPPoolTotalPoolCreatedEvents,
       "bIPPoolTotalPoolDeletedEvents": bIPPoolTotalPoolDeletedEvents,
       "bIPPoolGlobalIntervalDuration": bIPPoolGlobalIntervalDuration,
       "bIPv4PoolNotifObjects": bIPv4PoolNotifObjects,
       "bIPv6PoolMIBObjects": bIPv6PoolMIBObjects,
       "bIPv6PoolTable": bIPv6PoolTable,
       "bIPv6PoolEntry": bIPv6PoolEntry,
       "bIPv6PoolStatsInterval": bIPv6PoolStatsInterval,
       "bIPv6PoolIndex": bIPv6PoolIndex,
       "bIPv6PoolIntervalDuration": bIPv6PoolIntervalDuration,
       "bIPv6PoolName": bIPv6PoolName,
       "bIPv6PoolStartPrefix": bIPv6PoolStartPrefix,
       "bIPv6PoolEndPrefix": bIPv6PoolEndPrefix,
       "bIPv6PoolTotalPrefixes": bIPv6PoolTotalPrefixes,
       "bIPv6PoolReservedPrefixes": bIPv6PoolReservedPrefixes,
       "bIPv6PoolPeakFreePrefixes": bIPv6PoolPeakFreePrefixes,
       "bIPv6PoolPeakUsedPrefixes": bIPv6PoolPeakUsedPrefixes,
       "bIPv6PoolUsedPrefixLowThreshold": bIPv6PoolUsedPrefixLowThreshold,
       "bIPv6PoolUsedPrefixHighThreshold": bIPv6PoolUsedPrefixHighThreshold,
       "bIPv6PoolGrpName": bIPv6PoolGrpName,
       "bIPv6PoolGroupTable": bIPv6PoolGroupTable,
       "bIPv6PoolGroupEntry": bIPv6PoolGroupEntry,
       "bIPv6PoolGroupStatsInterval": bIPv6PoolGroupStatsInterval,
       "bIPv6PoolGroupIndex": bIPv6PoolGroupIndex,
       "bIPv6PoolGroupIntervalDuration": bIPv6PoolGroupIntervalDuration,
       "bIPv6PoolGroupName": bIPv6PoolGroupName,
       "bIPv6PoolGroupTotalPrefixes": bIPv6PoolGroupTotalPrefixes,
       "bIPv6PoolGroupReservedPrefixes": bIPv6PoolGroupReservedPrefixes,
       "bIPv6PoolGroupPeakFreePrefixes": bIPv6PoolGroupPeakFreePrefixes,
       "bIPv6PoolGroupPeakUsedPrefixes": bIPv6PoolGroupPeakUsedPrefixes,
       "bIPv6PoolGlobalTable": bIPv6PoolGlobalTable,
       "bIPv6PoolGlobalEntry": bIPv6PoolGlobalEntry,
       "bIPv6PoolGlobalStatsInterval": bIPv6PoolGlobalStatsInterval,
       "bIPv6PoolClientIndex": bIPv6PoolClientIndex,
       "bIPv6PoolClientName": bIPv6PoolClientName,
       "bIPv6PoolGlobalAllocReq": bIPv6PoolGlobalAllocReq,
       "bIPv6PoolGlobalAllocReqSucc": bIPv6PoolGlobalAllocReqSucc,
       "bIPv6PoolGlobalAllocReqUnSucc": bIPv6PoolGlobalAllocReqUnSucc,
       "bIPv6PoolGlobalDupAllocReq": bIPv6PoolGlobalDupAllocReq,
       "bIPv6PoolGlobalStaticAllocReq": bIPv6PoolGlobalStaticAllocReq,
       "bIPv6PoolGlobalAllocResponses": bIPv6PoolGlobalAllocResponses,
       "bIPv6PoolGlobalDeAllocReq": bIPv6PoolGlobalDeAllocReq,
       "bIPv6PoolGlobalDeAllocReqSucc": bIPv6PoolGlobalDeAllocReqSucc,
       "bIPv6PoolGlobalDeAllocReqUnSucc": bIPv6PoolGlobalDeAllocReqUnSucc,
       "bIPv6PoolGlobalInvalidReq": bIPv6PoolGlobalInvalidReq,
       "bIPv6PoolGlobalNotAvailCount": bIPv6PoolGlobalNotAvailCount,
       "bIPv6PoolGlobalPoolExhaustedCount": bIPv6PoolGlobalPoolExhaustedCount,
       "bIPv6PoolGlobalGroupExhaustedCount": bIPv6PoolGlobalGroupExhaustedCount,
       "bIPv6PoolGlobalInvalidPoolNameCount": bIPv6PoolGlobalInvalidPoolNameCount,
       "bIPv6PoolGlobalInvalidGroupNameCount": bIPv6PoolGlobalInvalidGroupNameCount,
       "bIPv6PoolGlobalInvalidIPAddrCount": bIPv6PoolGlobalInvalidIPAddrCount,
       "bIPv6PoolGlobalHashInsertFail": bIPv6PoolGlobalHashInsertFail,
       "bIPv6PoolGlobalHashDeleteFail": bIPv6PoolGlobalHashDeleteFail,
       "bIPv6PoolGlobalRequestedAllocatedMismacth": bIPv6PoolGlobalRequestedAllocatedMismacth,
       "bIPv6PoolGlobalRequestedIPNotFree": bIPv6PoolGlobalRequestedIPNotFree,
       "bIPv6PoolGlobalGenErrCount": bIPv6PoolGlobalGenErrCount,
       "bIPv6PoolGlobalPrefixRelDueToIntAdd": bIPv6PoolGlobalPrefixRelDueToIntAdd,
       "bIPv6PoolTotalPoolCreatedEvents": bIPv6PoolTotalPoolCreatedEvents,
       "bIPv6PoolTotalPoolDeletedEvents": bIPv6PoolTotalPoolDeletedEvents,
       "bIPv6PoolGlobalIntervalDuration": bIPv6PoolGlobalIntervalDuration,
       "bIPv6PoolNotifObjects": bIPv6PoolNotifObjects}
)
