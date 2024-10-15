# SNMP MIB module (WINDOWS-NT-PERFORMANCE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WINDOWS-NT-PERFORMANCE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:58 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microsoft_ObjectIdentity = ObjectIdentity
microsoft = _Microsoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1)
)
_Os_ObjectIdentity = ObjectIdentity
os = _Os_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3)
)
_Winnt_ObjectIdentity = ObjectIdentity
winnt = _Winnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1)
)
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1)
)
_MemoryAvailableBytes_Type = Integer32
_MemoryAvailableBytes_Object = MibScalar
memoryAvailableBytes = _MemoryAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 1),
    _MemoryAvailableBytes_Type()
)
memoryAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailableBytes.setStatus("mandatory")
_MemoryCommittedBytes_Type = Integer32
_MemoryCommittedBytes_Object = MibScalar
memoryCommittedBytes = _MemoryCommittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 2),
    _MemoryCommittedBytes_Type()
)
memoryCommittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCommittedBytes.setStatus("mandatory")
_MemoryCommitLimit_Type = Integer32
_MemoryCommitLimit_Object = MibScalar
memoryCommitLimit = _MemoryCommitLimit_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 3),
    _MemoryCommitLimit_Type()
)
memoryCommitLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCommitLimit.setStatus("mandatory")
_MemoryPageFaultsPerSec_Type = Counter32
_MemoryPageFaultsPerSec_Object = MibScalar
memoryPageFaultsPerSec = _MemoryPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 4),
    _MemoryPageFaultsPerSec_Type()
)
memoryPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPageFaultsPerSec.setStatus("mandatory")
_MemoryWriteCopiesPerSec_Type = Counter32
_MemoryWriteCopiesPerSec_Object = MibScalar
memoryWriteCopiesPerSec = _MemoryWriteCopiesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 5),
    _MemoryWriteCopiesPerSec_Type()
)
memoryWriteCopiesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryWriteCopiesPerSec.setStatus("mandatory")
_MemoryTransitionFaultsPerSec_Type = Counter32
_MemoryTransitionFaultsPerSec_Object = MibScalar
memoryTransitionFaultsPerSec = _MemoryTransitionFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 6),
    _MemoryTransitionFaultsPerSec_Type()
)
memoryTransitionFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTransitionFaultsPerSec.setStatus("mandatory")
_MemoryCacheFaultsPerSec_Type = Counter32
_MemoryCacheFaultsPerSec_Object = MibScalar
memoryCacheFaultsPerSec = _MemoryCacheFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 7),
    _MemoryCacheFaultsPerSec_Type()
)
memoryCacheFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheFaultsPerSec.setStatus("mandatory")
_MemoryDemandZeroFaultsPerSec_Type = Counter32
_MemoryDemandZeroFaultsPerSec_Object = MibScalar
memoryDemandZeroFaultsPerSec = _MemoryDemandZeroFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 8),
    _MemoryDemandZeroFaultsPerSec_Type()
)
memoryDemandZeroFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDemandZeroFaultsPerSec.setStatus("mandatory")
_MemoryPagesPerSec_Type = Counter32
_MemoryPagesPerSec_Object = MibScalar
memoryPagesPerSec = _MemoryPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 9),
    _MemoryPagesPerSec_Type()
)
memoryPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesPerSec.setStatus("mandatory")
_MemoryPagesInputPerSec_Type = Counter32
_MemoryPagesInputPerSec_Object = MibScalar
memoryPagesInputPerSec = _MemoryPagesInputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 10),
    _MemoryPagesInputPerSec_Type()
)
memoryPagesInputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesInputPerSec.setStatus("mandatory")
_MemoryPageReadsPerSec_Type = Counter32
_MemoryPageReadsPerSec_Object = MibScalar
memoryPageReadsPerSec = _MemoryPageReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 11),
    _MemoryPageReadsPerSec_Type()
)
memoryPageReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPageReadsPerSec.setStatus("mandatory")
_MemoryPagesOutputPerSec_Type = Counter32
_MemoryPagesOutputPerSec_Object = MibScalar
memoryPagesOutputPerSec = _MemoryPagesOutputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 12),
    _MemoryPagesOutputPerSec_Type()
)
memoryPagesOutputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesOutputPerSec.setStatus("mandatory")
_MemoryPageWritesPerSec_Type = Counter32
_MemoryPageWritesPerSec_Object = MibScalar
memoryPageWritesPerSec = _MemoryPageWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 13),
    _MemoryPageWritesPerSec_Type()
)
memoryPageWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPageWritesPerSec.setStatus("mandatory")
_MemoryPoolPagedBytes_Type = Integer32
_MemoryPoolPagedBytes_Object = MibScalar
memoryPoolPagedBytes = _MemoryPoolPagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 14),
    _MemoryPoolPagedBytes_Type()
)
memoryPoolPagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedBytes.setStatus("mandatory")
_MemoryPoolNonpagedBytes_Type = Integer32
_MemoryPoolNonpagedBytes_Object = MibScalar
memoryPoolNonpagedBytes = _MemoryPoolNonpagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 15),
    _MemoryPoolNonpagedBytes_Type()
)
memoryPoolNonpagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNonpagedBytes.setStatus("mandatory")
_MemoryPoolPagedAllocs_Type = Integer32
_MemoryPoolPagedAllocs_Object = MibScalar
memoryPoolPagedAllocs = _MemoryPoolPagedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 16),
    _MemoryPoolPagedAllocs_Type()
)
memoryPoolPagedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedAllocs.setStatus("mandatory")
_MemoryPoolNonpagedAllocs_Type = Integer32
_MemoryPoolNonpagedAllocs_Object = MibScalar
memoryPoolNonpagedAllocs = _MemoryPoolNonpagedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 17),
    _MemoryPoolNonpagedAllocs_Type()
)
memoryPoolNonpagedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNonpagedAllocs.setStatus("mandatory")
_MemoryFreeSystemPageTableEntries_Type = Integer32
_MemoryFreeSystemPageTableEntries_Object = MibScalar
memoryFreeSystemPageTableEntries = _MemoryFreeSystemPageTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 18),
    _MemoryFreeSystemPageTableEntries_Type()
)
memoryFreeSystemPageTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFreeSystemPageTableEntries.setStatus("mandatory")
_MemoryCacheBytes_Type = Integer32
_MemoryCacheBytes_Object = MibScalar
memoryCacheBytes = _MemoryCacheBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 19),
    _MemoryCacheBytes_Type()
)
memoryCacheBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheBytes.setStatus("mandatory")
_MemoryCacheBytesPeak_Type = Integer32
_MemoryCacheBytesPeak_Object = MibScalar
memoryCacheBytesPeak = _MemoryCacheBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 20),
    _MemoryCacheBytesPeak_Type()
)
memoryCacheBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheBytesPeak.setStatus("mandatory")
_MemoryPoolPagedResidentBytes_Type = Integer32
_MemoryPoolPagedResidentBytes_Object = MibScalar
memoryPoolPagedResidentBytes = _MemoryPoolPagedResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 21),
    _MemoryPoolPagedResidentBytes_Type()
)
memoryPoolPagedResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedResidentBytes.setStatus("mandatory")
_MemorySystemCodeTotalBytes_Type = Integer32
_MemorySystemCodeTotalBytes_Object = MibScalar
memorySystemCodeTotalBytes = _MemorySystemCodeTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 22),
    _MemorySystemCodeTotalBytes_Type()
)
memorySystemCodeTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeTotalBytes.setStatus("mandatory")
_MemorySystemCodeResidentBytes_Type = Integer32
_MemorySystemCodeResidentBytes_Object = MibScalar
memorySystemCodeResidentBytes = _MemorySystemCodeResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 23),
    _MemorySystemCodeResidentBytes_Type()
)
memorySystemCodeResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeResidentBytes.setStatus("mandatory")
_MemorySystemDriverTotalBytes_Type = Integer32
_MemorySystemDriverTotalBytes_Object = MibScalar
memorySystemDriverTotalBytes = _MemorySystemDriverTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 24),
    _MemorySystemDriverTotalBytes_Type()
)
memorySystemDriverTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverTotalBytes.setStatus("mandatory")
_MemorySystemDriverResidentBytes_Type = Integer32
_MemorySystemDriverResidentBytes_Object = MibScalar
memorySystemDriverResidentBytes = _MemorySystemDriverResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 25),
    _MemorySystemDriverResidentBytes_Type()
)
memorySystemDriverResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverResidentBytes.setStatus("mandatory")
_MemorySystemCacheResidentBytes_Type = Integer32
_MemorySystemCacheResidentBytes_Object = MibScalar
memorySystemCacheResidentBytes = _MemorySystemCacheResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 26),
    _MemorySystemCacheResidentBytes_Type()
)
memorySystemCacheResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCacheResidentBytes.setStatus("mandatory")
_MemoryPercentCommittedBytesInUse_Type = Integer32
_MemoryPercentCommittedBytesInUse_Object = MibScalar
memoryPercentCommittedBytesInUse = _MemoryPercentCommittedBytesInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 27),
    _MemoryPercentCommittedBytesInUse_Type()
)
memoryPercentCommittedBytesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPercentCommittedBytesInUse.setStatus("mandatory")
_CpuprocessorTable_Object = MibTable
cpuprocessorTable = _CpuprocessorTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpuprocessorTable.setStatus("mandatory")
_CpuprocessorEntry_Object = MibTableRow
cpuprocessorEntry = _CpuprocessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1)
)
cpuprocessorEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "cpuprocessorIndex"),
)
if mibBuilder.loadTexts:
    cpuprocessorEntry.setStatus("mandatory")
_CpuprocessorIndex_Type = Integer32
_CpuprocessorIndex_Object = MibTableColumn
cpuprocessorIndex = _CpuprocessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 1),
    _CpuprocessorIndex_Type()
)
cpuprocessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuprocessorIndex.setStatus("mandatory")
_CpuprocessorInstance_Type = DisplayString
_CpuprocessorInstance_Object = MibTableColumn
cpuprocessorInstance = _CpuprocessorInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 2),
    _CpuprocessorInstance_Type()
)
cpuprocessorInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuprocessorInstance.setStatus("mandatory")
_CpuPercentProcessorTime_Type = Integer32
_CpuPercentProcessorTime_Object = MibTableColumn
cpuPercentProcessorTime = _CpuPercentProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 3),
    _CpuPercentProcessorTime_Type()
)
cpuPercentProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentProcessorTime.setStatus("mandatory")
_CpuPercentUserTime_Type = Integer32
_CpuPercentUserTime_Object = MibTableColumn
cpuPercentUserTime = _CpuPercentUserTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 4),
    _CpuPercentUserTime_Type()
)
cpuPercentUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentUserTime.setStatus("mandatory")
_CpuPercentPrivilegedTime_Type = Integer32
_CpuPercentPrivilegedTime_Object = MibTableColumn
cpuPercentPrivilegedTime = _CpuPercentPrivilegedTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 5),
    _CpuPercentPrivilegedTime_Type()
)
cpuPercentPrivilegedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentPrivilegedTime.setStatus("mandatory")
_CpuInterruptsPerSec_Type = Counter32
_CpuInterruptsPerSec_Object = MibTableColumn
cpuInterruptsPerSec = _CpuInterruptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 6),
    _CpuInterruptsPerSec_Type()
)
cpuInterruptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInterruptsPerSec.setStatus("mandatory")
_CpuPercentDPCTime_Type = Integer32
_CpuPercentDPCTime_Object = MibTableColumn
cpuPercentDPCTime = _CpuPercentDPCTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 7),
    _CpuPercentDPCTime_Type()
)
cpuPercentDPCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentDPCTime.setStatus("mandatory")
_CpuPercentInterruptTime_Type = Integer32
_CpuPercentInterruptTime_Object = MibTableColumn
cpuPercentInterruptTime = _CpuPercentInterruptTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 8),
    _CpuPercentInterruptTime_Type()
)
cpuPercentInterruptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentInterruptTime.setStatus("mandatory")
_CpuDPCsQueuedPerSec_Type = Counter32
_CpuDPCsQueuedPerSec_Object = MibTableColumn
cpuDPCsQueuedPerSec = _CpuDPCsQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 9),
    _CpuDPCsQueuedPerSec_Type()
)
cpuDPCsQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCsQueuedPerSec.setStatus("mandatory")
_CpuDPCRate_Type = Integer32
_CpuDPCRate_Object = MibTableColumn
cpuDPCRate = _CpuDPCRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 10),
    _CpuDPCRate_Type()
)
cpuDPCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCRate.setStatus("mandatory")
_CpuDPCBypassesPerSec_Type = Counter32
_CpuDPCBypassesPerSec_Object = MibTableColumn
cpuDPCBypassesPerSec = _CpuDPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 11),
    _CpuDPCBypassesPerSec_Type()
)
cpuDPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCBypassesPerSec.setStatus("mandatory")
_CpuAPCBypassesPerSec_Type = Counter32
_CpuAPCBypassesPerSec_Object = MibTableColumn
cpuAPCBypassesPerSec = _CpuAPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 12),
    _CpuAPCBypassesPerSec_Type()
)
cpuAPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAPCBypassesPerSec.setStatus("mandatory")
_Netnetwork_InterfaceTable_Object = MibTable
netnetwork_InterfaceTable = _Netnetwork_InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    netnetwork_InterfaceTable.setStatus("mandatory")
_Netnetwork_InterfaceEntry_Object = MibTableRow
netnetwork_InterfaceEntry = _Netnetwork_InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1)
)
netnetwork_InterfaceEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "netnetwork-InterfaceIndex"),
)
if mibBuilder.loadTexts:
    netnetwork_InterfaceEntry.setStatus("mandatory")
_Netnetwork_InterfaceIndex_Type = Integer32
_Netnetwork_InterfaceIndex_Object = MibScalar
netnetwork_InterfaceIndex = _Netnetwork_InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 1),
    _Netnetwork_InterfaceIndex_Type()
)
netnetwork_InterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netnetwork_InterfaceIndex.setStatus("mandatory")
_Netnetwork_InterfaceInstance_Type = DisplayString
_Netnetwork_InterfaceInstance_Object = MibScalar
netnetwork_InterfaceInstance = _Netnetwork_InterfaceInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 2),
    _Netnetwork_InterfaceInstance_Type()
)
netnetwork_InterfaceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netnetwork_InterfaceInstance.setStatus("mandatory")
_NetBytesTotalPerSec_Type = Counter32
_NetBytesTotalPerSec_Object = MibTableColumn
netBytesTotalPerSec = _NetBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 3),
    _NetBytesTotalPerSec_Type()
)
netBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesTotalPerSec.setStatus("mandatory")
_NetPacketsPerSec_Type = Counter32
_NetPacketsPerSec_Object = MibTableColumn
netPacketsPerSec = _NetPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 4),
    _NetPacketsPerSec_Type()
)
netPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsPerSec.setStatus("mandatory")
_NetPacketsReceivedPerSec_Type = Counter32
_NetPacketsReceivedPerSec_Object = MibTableColumn
netPacketsReceivedPerSec = _NetPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 5),
    _NetPacketsReceivedPerSec_Type()
)
netPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedPerSec.setStatus("mandatory")
_NetPacketsSentPerSec_Type = Counter32
_NetPacketsSentPerSec_Object = MibTableColumn
netPacketsSentPerSec = _NetPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 6),
    _NetPacketsSentPerSec_Type()
)
netPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsSentPerSec.setStatus("mandatory")
_NetCurrentBandwidth_Type = Integer32
_NetCurrentBandwidth_Object = MibTableColumn
netCurrentBandwidth = _NetCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 7),
    _NetCurrentBandwidth_Type()
)
netCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCurrentBandwidth.setStatus("mandatory")
_NetBytesReceivedPerSec_Type = Counter32
_NetBytesReceivedPerSec_Object = MibTableColumn
netBytesReceivedPerSec = _NetBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 8),
    _NetBytesReceivedPerSec_Type()
)
netBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesReceivedPerSec.setStatus("mandatory")
_NetPacketsReceivedUnicastPerSec_Type = Counter32
_NetPacketsReceivedUnicastPerSec_Object = MibTableColumn
netPacketsReceivedUnicastPerSec = _NetPacketsReceivedUnicastPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 9),
    _NetPacketsReceivedUnicastPerSec_Type()
)
netPacketsReceivedUnicastPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedUnicastPerSec.setStatus("mandatory")
_NetPacketsReceivedNon_UnicastPerSec_Type = Counter32
_NetPacketsReceivedNon_UnicastPerSec_Object = MibScalar
netPacketsReceivedNon_UnicastPerSec = _NetPacketsReceivedNon_UnicastPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 10),
    _NetPacketsReceivedNon_UnicastPerSec_Type()
)
netPacketsReceivedNon_UnicastPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedNon_UnicastPerSec.setStatus("mandatory")
_NetPacketsReceivedDiscarded_Type = Integer32
_NetPacketsReceivedDiscarded_Object = MibTableColumn
netPacketsReceivedDiscarded = _NetPacketsReceivedDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 11),
    _NetPacketsReceivedDiscarded_Type()
)
netPacketsReceivedDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedDiscarded.setStatus("mandatory")
_NetPacketsReceivedErrors_Type = Integer32
_NetPacketsReceivedErrors_Object = MibTableColumn
netPacketsReceivedErrors = _NetPacketsReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 12),
    _NetPacketsReceivedErrors_Type()
)
netPacketsReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedErrors.setStatus("mandatory")
_NetPacketsReceivedUnknown_Type = Integer32
_NetPacketsReceivedUnknown_Object = MibTableColumn
netPacketsReceivedUnknown = _NetPacketsReceivedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 13),
    _NetPacketsReceivedUnknown_Type()
)
netPacketsReceivedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedUnknown.setStatus("mandatory")
_NetBytesSentPerSec_Type = Counter32
_NetBytesSentPerSec_Object = MibTableColumn
netBytesSentPerSec = _NetBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 14),
    _NetBytesSentPerSec_Type()
)
netBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesSentPerSec.setStatus("mandatory")
_NetPacketsSentUnicastPerSec_Type = Counter32
_NetPacketsSentUnicastPerSec_Object = MibTableColumn
netPacketsSentUnicastPerSec = _NetPacketsSentUnicastPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 15),
    _NetPacketsSentUnicastPerSec_Type()
)
netPacketsSentUnicastPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsSentUnicastPerSec.setStatus("mandatory")
_NetPacketsSentNon_UnicastPerSec_Type = Counter32
_NetPacketsSentNon_UnicastPerSec_Object = MibScalar
netPacketsSentNon_UnicastPerSec = _NetPacketsSentNon_UnicastPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 16),
    _NetPacketsSentNon_UnicastPerSec_Type()
)
netPacketsSentNon_UnicastPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsSentNon_UnicastPerSec.setStatus("mandatory")
_NetPacketsOutboundDiscarded_Type = Integer32
_NetPacketsOutboundDiscarded_Object = MibTableColumn
netPacketsOutboundDiscarded = _NetPacketsOutboundDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 17),
    _NetPacketsOutboundDiscarded_Type()
)
netPacketsOutboundDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsOutboundDiscarded.setStatus("mandatory")
_NetPacketsOutboundErrors_Type = Integer32
_NetPacketsOutboundErrors_Object = MibTableColumn
netPacketsOutboundErrors = _NetPacketsOutboundErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 18),
    _NetPacketsOutboundErrors_Type()
)
netPacketsOutboundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsOutboundErrors.setStatus("mandatory")
_NetOutputQueueLength_Type = Integer32
_NetOutputQueueLength_Object = MibTableColumn
netOutputQueueLength = _NetOutputQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1, 19),
    _NetOutputQueueLength_Type()
)
netOutputQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netOutputQueueLength.setStatus("mandatory")
_PdiskphysicalDiskTable_Object = MibTable
pdiskphysicalDiskTable = _PdiskphysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdiskphysicalDiskTable.setStatus("mandatory")
_PdiskphysicalDiskEntry_Object = MibTableRow
pdiskphysicalDiskEntry = _PdiskphysicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1)
)
pdiskphysicalDiskEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "pdiskphysicalDiskIndex"),
)
if mibBuilder.loadTexts:
    pdiskphysicalDiskEntry.setStatus("mandatory")
_PdiskphysicalDiskIndex_Type = Integer32
_PdiskphysicalDiskIndex_Object = MibTableColumn
pdiskphysicalDiskIndex = _PdiskphysicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 1),
    _PdiskphysicalDiskIndex_Type()
)
pdiskphysicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskphysicalDiskIndex.setStatus("mandatory")
_PdiskphysicalDiskInstance_Type = DisplayString
_PdiskphysicalDiskInstance_Object = MibTableColumn
pdiskphysicalDiskInstance = _PdiskphysicalDiskInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 2),
    _PdiskphysicalDiskInstance_Type()
)
pdiskphysicalDiskInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskphysicalDiskInstance.setStatus("mandatory")
_PdiskCurrentDiskQueueLength_Type = Integer32
_PdiskCurrentDiskQueueLength_Object = MibTableColumn
pdiskCurrentDiskQueueLength = _PdiskCurrentDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 3),
    _PdiskCurrentDiskQueueLength_Type()
)
pdiskCurrentDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskCurrentDiskQueueLength.setStatus("mandatory")
_PdiskPercentDiskTime_Type = TimeTicks
_PdiskPercentDiskTime_Object = MibTableColumn
pdiskPercentDiskTime = _PdiskPercentDiskTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 4),
    _PdiskPercentDiskTime_Type()
)
pdiskPercentDiskTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskPercentDiskTime.setStatus("mandatory")
_PdiskAvgDiskQueueLength_Type = Integer32
_PdiskAvgDiskQueueLength_Object = MibTableColumn
pdiskAvgDiskQueueLength = _PdiskAvgDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 5),
    _PdiskAvgDiskQueueLength_Type()
)
pdiskAvgDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskQueueLength.setStatus("mandatory")
_PdiskPercentDiskReadTime_Type = TimeTicks
_PdiskPercentDiskReadTime_Object = MibTableColumn
pdiskPercentDiskReadTime = _PdiskPercentDiskReadTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 6),
    _PdiskPercentDiskReadTime_Type()
)
pdiskPercentDiskReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskPercentDiskReadTime.setStatus("mandatory")
_PdiskAvgDiskReadQueueLength_Type = Integer32
_PdiskAvgDiskReadQueueLength_Object = MibTableColumn
pdiskAvgDiskReadQueueLength = _PdiskAvgDiskReadQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 7),
    _PdiskAvgDiskReadQueueLength_Type()
)
pdiskAvgDiskReadQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskReadQueueLength.setStatus("mandatory")
_PdiskPercentDiskWriteTime_Type = TimeTicks
_PdiskPercentDiskWriteTime_Object = MibTableColumn
pdiskPercentDiskWriteTime = _PdiskPercentDiskWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 8),
    _PdiskPercentDiskWriteTime_Type()
)
pdiskPercentDiskWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskPercentDiskWriteTime.setStatus("mandatory")
_PdiskAvgDiskWriteQueueLength_Type = Integer32
_PdiskAvgDiskWriteQueueLength_Object = MibTableColumn
pdiskAvgDiskWriteQueueLength = _PdiskAvgDiskWriteQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 9),
    _PdiskAvgDiskWriteQueueLength_Type()
)
pdiskAvgDiskWriteQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskWriteQueueLength.setStatus("mandatory")
_PdiskAvgDiskSecPerTransfer_Type = TimeTicks
_PdiskAvgDiskSecPerTransfer_Object = MibTableColumn
pdiskAvgDiskSecPerTransfer = _PdiskAvgDiskSecPerTransfer_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 10),
    _PdiskAvgDiskSecPerTransfer_Type()
)
pdiskAvgDiskSecPerTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskSecPerTransfer.setStatus("mandatory")
_PdiskAvgDiskSecPerRead_Type = TimeTicks
_PdiskAvgDiskSecPerRead_Object = MibTableColumn
pdiskAvgDiskSecPerRead = _PdiskAvgDiskSecPerRead_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 11),
    _PdiskAvgDiskSecPerRead_Type()
)
pdiskAvgDiskSecPerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskSecPerRead.setStatus("mandatory")
_PdiskAvgDiskSecPerWrite_Type = TimeTicks
_PdiskAvgDiskSecPerWrite_Object = MibTableColumn
pdiskAvgDiskSecPerWrite = _PdiskAvgDiskSecPerWrite_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 12),
    _PdiskAvgDiskSecPerWrite_Type()
)
pdiskAvgDiskSecPerWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskAvgDiskSecPerWrite.setStatus("mandatory")
_PdiskDiskTransfersPerSec_Type = Counter32
_PdiskDiskTransfersPerSec_Object = MibTableColumn
pdiskDiskTransfersPerSec = _PdiskDiskTransfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 13),
    _PdiskDiskTransfersPerSec_Type()
)
pdiskDiskTransfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskTransfersPerSec.setStatus("mandatory")
_PdiskDiskReadsPerSec_Type = Counter32
_PdiskDiskReadsPerSec_Object = MibTableColumn
pdiskDiskReadsPerSec = _PdiskDiskReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 14),
    _PdiskDiskReadsPerSec_Type()
)
pdiskDiskReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskReadsPerSec.setStatus("mandatory")
_PdiskDiskWritesPerSec_Type = Counter32
_PdiskDiskWritesPerSec_Object = MibTableColumn
pdiskDiskWritesPerSec = _PdiskDiskWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 15),
    _PdiskDiskWritesPerSec_Type()
)
pdiskDiskWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskWritesPerSec.setStatus("mandatory")
_PdiskDiskBytesPerSec_Type = Integer32
_PdiskDiskBytesPerSec_Object = MibTableColumn
pdiskDiskBytesPerSec = _PdiskDiskBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 16),
    _PdiskDiskBytesPerSec_Type()
)
pdiskDiskBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskBytesPerSec.setStatus("mandatory")
_PdiskDiskReadBytesPerSec_Type = Integer32
_PdiskDiskReadBytesPerSec_Object = MibTableColumn
pdiskDiskReadBytesPerSec = _PdiskDiskReadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 17),
    _PdiskDiskReadBytesPerSec_Type()
)
pdiskDiskReadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskReadBytesPerSec.setStatus("mandatory")
_PdiskDiskWriteBytesPerSec_Type = Integer32
_PdiskDiskWriteBytesPerSec_Object = MibTableColumn
pdiskDiskWriteBytesPerSec = _PdiskDiskWriteBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 4, 1, 18),
    _PdiskDiskWriteBytesPerSec_Type()
)
pdiskDiskWriteBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdiskDiskWriteBytesPerSec.setStatus("mandatory")
_LdisklogicalDiskTable_Object = MibTable
ldisklogicalDiskTable = _LdisklogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ldisklogicalDiskTable.setStatus("mandatory")
_LdisklogicalDiskEntry_Object = MibTableRow
ldisklogicalDiskEntry = _LdisklogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1)
)
ldisklogicalDiskEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "ldisklogicalDiskIndex"),
)
if mibBuilder.loadTexts:
    ldisklogicalDiskEntry.setStatus("mandatory")
_LdisklogicalDiskIndex_Type = Integer32
_LdisklogicalDiskIndex_Object = MibTableColumn
ldisklogicalDiskIndex = _LdisklogicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 1),
    _LdisklogicalDiskIndex_Type()
)
ldisklogicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldisklogicalDiskIndex.setStatus("mandatory")
_LdisklogicalDiskInstance_Type = DisplayString
_LdisklogicalDiskInstance_Object = MibTableColumn
ldisklogicalDiskInstance = _LdisklogicalDiskInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 2),
    _LdisklogicalDiskInstance_Type()
)
ldisklogicalDiskInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldisklogicalDiskInstance.setStatus("mandatory")
_LdiskPercentFreeSpace_Type = Integer32
_LdiskPercentFreeSpace_Object = MibTableColumn
ldiskPercentFreeSpace = _LdiskPercentFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 3),
    _LdiskPercentFreeSpace_Type()
)
ldiskPercentFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskPercentFreeSpace.setStatus("mandatory")
_LdiskFreeMegabytes_Type = Integer32
_LdiskFreeMegabytes_Object = MibTableColumn
ldiskFreeMegabytes = _LdiskFreeMegabytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 4),
    _LdiskFreeMegabytes_Type()
)
ldiskFreeMegabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskFreeMegabytes.setStatus("mandatory")
_LdiskCurrentDiskQueueLength_Type = Integer32
_LdiskCurrentDiskQueueLength_Object = MibTableColumn
ldiskCurrentDiskQueueLength = _LdiskCurrentDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 5),
    _LdiskCurrentDiskQueueLength_Type()
)
ldiskCurrentDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskCurrentDiskQueueLength.setStatus("mandatory")
_LdiskPercentDiskTime_Type = TimeTicks
_LdiskPercentDiskTime_Object = MibTableColumn
ldiskPercentDiskTime = _LdiskPercentDiskTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 6),
    _LdiskPercentDiskTime_Type()
)
ldiskPercentDiskTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskPercentDiskTime.setStatus("mandatory")
_LdiskAvgDiskQueueLength_Type = Integer32
_LdiskAvgDiskQueueLength_Object = MibTableColumn
ldiskAvgDiskQueueLength = _LdiskAvgDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 7),
    _LdiskAvgDiskQueueLength_Type()
)
ldiskAvgDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskQueueLength.setStatus("mandatory")
_LdiskPercentDiskReadTime_Type = TimeTicks
_LdiskPercentDiskReadTime_Object = MibTableColumn
ldiskPercentDiskReadTime = _LdiskPercentDiskReadTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 8),
    _LdiskPercentDiskReadTime_Type()
)
ldiskPercentDiskReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskPercentDiskReadTime.setStatus("mandatory")
_LdiskAvgDiskReadQueueLength_Type = Integer32
_LdiskAvgDiskReadQueueLength_Object = MibTableColumn
ldiskAvgDiskReadQueueLength = _LdiskAvgDiskReadQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 9),
    _LdiskAvgDiskReadQueueLength_Type()
)
ldiskAvgDiskReadQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskReadQueueLength.setStatus("mandatory")
_LdiskPercentDiskWriteTime_Type = TimeTicks
_LdiskPercentDiskWriteTime_Object = MibTableColumn
ldiskPercentDiskWriteTime = _LdiskPercentDiskWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 10),
    _LdiskPercentDiskWriteTime_Type()
)
ldiskPercentDiskWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskPercentDiskWriteTime.setStatus("mandatory")
_LdiskAvgDiskWriteQueueLength_Type = Integer32
_LdiskAvgDiskWriteQueueLength_Object = MibTableColumn
ldiskAvgDiskWriteQueueLength = _LdiskAvgDiskWriteQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 11),
    _LdiskAvgDiskWriteQueueLength_Type()
)
ldiskAvgDiskWriteQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskWriteQueueLength.setStatus("mandatory")
_LdiskAvgDiskSecPerTransfer_Type = TimeTicks
_LdiskAvgDiskSecPerTransfer_Object = MibTableColumn
ldiskAvgDiskSecPerTransfer = _LdiskAvgDiskSecPerTransfer_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 12),
    _LdiskAvgDiskSecPerTransfer_Type()
)
ldiskAvgDiskSecPerTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskSecPerTransfer.setStatus("mandatory")
_LdiskAvgDiskSecPerRead_Type = TimeTicks
_LdiskAvgDiskSecPerRead_Object = MibTableColumn
ldiskAvgDiskSecPerRead = _LdiskAvgDiskSecPerRead_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 13),
    _LdiskAvgDiskSecPerRead_Type()
)
ldiskAvgDiskSecPerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskSecPerRead.setStatus("mandatory")
_LdiskAvgDiskSecPerWrite_Type = TimeTicks
_LdiskAvgDiskSecPerWrite_Object = MibTableColumn
ldiskAvgDiskSecPerWrite = _LdiskAvgDiskSecPerWrite_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 14),
    _LdiskAvgDiskSecPerWrite_Type()
)
ldiskAvgDiskSecPerWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskAvgDiskSecPerWrite.setStatus("mandatory")
_LdiskDiskTransfersPerSec_Type = Counter32
_LdiskDiskTransfersPerSec_Object = MibTableColumn
ldiskDiskTransfersPerSec = _LdiskDiskTransfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 15),
    _LdiskDiskTransfersPerSec_Type()
)
ldiskDiskTransfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskTransfersPerSec.setStatus("mandatory")
_LdiskDiskReadsPerSec_Type = Counter32
_LdiskDiskReadsPerSec_Object = MibTableColumn
ldiskDiskReadsPerSec = _LdiskDiskReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 16),
    _LdiskDiskReadsPerSec_Type()
)
ldiskDiskReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskReadsPerSec.setStatus("mandatory")
_LdiskDiskWritesPerSec_Type = Counter32
_LdiskDiskWritesPerSec_Object = MibTableColumn
ldiskDiskWritesPerSec = _LdiskDiskWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 17),
    _LdiskDiskWritesPerSec_Type()
)
ldiskDiskWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskWritesPerSec.setStatus("mandatory")
_LdiskDiskBytesPerSec_Type = Integer32
_LdiskDiskBytesPerSec_Object = MibTableColumn
ldiskDiskBytesPerSec = _LdiskDiskBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 18),
    _LdiskDiskBytesPerSec_Type()
)
ldiskDiskBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskBytesPerSec.setStatus("mandatory")
_LdiskDiskReadBytesPerSec_Type = Integer32
_LdiskDiskReadBytesPerSec_Object = MibTableColumn
ldiskDiskReadBytesPerSec = _LdiskDiskReadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 19),
    _LdiskDiskReadBytesPerSec_Type()
)
ldiskDiskReadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskReadBytesPerSec.setStatus("mandatory")
_LdiskDiskWriteBytesPerSec_Type = Integer32
_LdiskDiskWriteBytesPerSec_Object = MibTableColumn
ldiskDiskWriteBytesPerSec = _LdiskDiskWriteBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 5, 1, 20),
    _LdiskDiskWriteBytesPerSec_Type()
)
ldiskDiskWriteBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldiskDiskWriteBytesPerSec.setStatus("mandatory")
_Pagefilepaging_FileTable_Object = MibTable
pagefilepaging_FileTable = _Pagefilepaging_FileTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pagefilepaging_FileTable.setStatus("mandatory")
_Pagefilepaging_FileEntry_Object = MibTableRow
pagefilepaging_FileEntry = _Pagefilepaging_FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6, 1)
)
pagefilepaging_FileEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "pagefilepaging-FileIndex"),
)
if mibBuilder.loadTexts:
    pagefilepaging_FileEntry.setStatus("mandatory")
_Pagefilepaging_FileIndex_Type = Integer32
_Pagefilepaging_FileIndex_Object = MibScalar
pagefilepaging_FileIndex = _Pagefilepaging_FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6, 1, 1),
    _Pagefilepaging_FileIndex_Type()
)
pagefilepaging_FileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagefilepaging_FileIndex.setStatus("mandatory")
_Pagefilepaging_FileInstance_Type = DisplayString
_Pagefilepaging_FileInstance_Object = MibScalar
pagefilepaging_FileInstance = _Pagefilepaging_FileInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6, 1, 2),
    _Pagefilepaging_FileInstance_Type()
)
pagefilepaging_FileInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagefilepaging_FileInstance.setStatus("mandatory")
_PagefilePercentUsage_Type = Integer32
_PagefilePercentUsage_Object = MibTableColumn
pagefilePercentUsage = _PagefilePercentUsage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6, 1, 3),
    _PagefilePercentUsage_Type()
)
pagefilePercentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagefilePercentUsage.setStatus("mandatory")
_PagefilePercentUsagePeak_Type = Integer32
_PagefilePercentUsagePeak_Object = MibTableColumn
pagefilePercentUsagePeak = _PagefilePercentUsagePeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 6, 1, 4),
    _PagefilePercentUsagePeak_Type()
)
pagefilePercentUsagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagefilePercentUsagePeak.setStatus("mandatory")
_ProcessprocessTable_Object = MibTable
processprocessTable = _ProcessprocessTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    processprocessTable.setStatus("mandatory")
_ProcessprocessEntry_Object = MibTableRow
processprocessEntry = _ProcessprocessEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1)
)
processprocessEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "processprocessIndex"),
)
if mibBuilder.loadTexts:
    processprocessEntry.setStatus("mandatory")
_ProcessprocessIndex_Type = Integer32
_ProcessprocessIndex_Object = MibTableColumn
processprocessIndex = _ProcessprocessIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 1),
    _ProcessprocessIndex_Type()
)
processprocessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processprocessIndex.setStatus("mandatory")
_ProcessprocessInstance_Type = DisplayString
_ProcessprocessInstance_Object = MibTableColumn
processprocessInstance = _ProcessprocessInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 2),
    _ProcessprocessInstance_Type()
)
processprocessInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processprocessInstance.setStatus("mandatory")
_ProcessPercentProcessorTime_Type = Integer32
_ProcessPercentProcessorTime_Object = MibTableColumn
processPercentProcessorTime = _ProcessPercentProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 3),
    _ProcessPercentProcessorTime_Type()
)
processPercentProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPercentProcessorTime.setStatus("mandatory")
_ProcessPercentUserTime_Type = Integer32
_ProcessPercentUserTime_Object = MibTableColumn
processPercentUserTime = _ProcessPercentUserTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 4),
    _ProcessPercentUserTime_Type()
)
processPercentUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPercentUserTime.setStatus("mandatory")
_ProcessPercentPrivilegedTime_Type = Integer32
_ProcessPercentPrivilegedTime_Object = MibTableColumn
processPercentPrivilegedTime = _ProcessPercentPrivilegedTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 5),
    _ProcessPercentPrivilegedTime_Type()
)
processPercentPrivilegedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPercentPrivilegedTime.setStatus("mandatory")
_ProcessVirtualBytesPeak_Type = Integer32
_ProcessVirtualBytesPeak_Object = MibTableColumn
processVirtualBytesPeak = _ProcessVirtualBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 6),
    _ProcessVirtualBytesPeak_Type()
)
processVirtualBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processVirtualBytesPeak.setStatus("mandatory")
_ProcessVirtualBytes_Type = Integer32
_ProcessVirtualBytes_Object = MibTableColumn
processVirtualBytes = _ProcessVirtualBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 7),
    _ProcessVirtualBytes_Type()
)
processVirtualBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processVirtualBytes.setStatus("mandatory")
_ProcessPageFaultsPerSec_Type = Counter32
_ProcessPageFaultsPerSec_Object = MibTableColumn
processPageFaultsPerSec = _ProcessPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 8),
    _ProcessPageFaultsPerSec_Type()
)
processPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPageFaultsPerSec.setStatus("mandatory")
_ProcessWorkingSetPeak_Type = Integer32
_ProcessWorkingSetPeak_Object = MibTableColumn
processWorkingSetPeak = _ProcessWorkingSetPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 9),
    _ProcessWorkingSetPeak_Type()
)
processWorkingSetPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processWorkingSetPeak.setStatus("mandatory")
_ProcessWorkingSet_Type = Integer32
_ProcessWorkingSet_Object = MibTableColumn
processWorkingSet = _ProcessWorkingSet_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 10),
    _ProcessWorkingSet_Type()
)
processWorkingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processWorkingSet.setStatus("mandatory")
_ProcessPageFileBytesPeak_Type = Integer32
_ProcessPageFileBytesPeak_Object = MibTableColumn
processPageFileBytesPeak = _ProcessPageFileBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 11),
    _ProcessPageFileBytesPeak_Type()
)
processPageFileBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPageFileBytesPeak.setStatus("mandatory")
_ProcessPageFileBytes_Type = Integer32
_ProcessPageFileBytes_Object = MibTableColumn
processPageFileBytes = _ProcessPageFileBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 12),
    _ProcessPageFileBytes_Type()
)
processPageFileBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPageFileBytes.setStatus("mandatory")
_ProcessPrivateBytes_Type = Integer32
_ProcessPrivateBytes_Object = MibTableColumn
processPrivateBytes = _ProcessPrivateBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 13),
    _ProcessPrivateBytes_Type()
)
processPrivateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPrivateBytes.setStatus("mandatory")
_ProcessThreadCount_Type = Integer32
_ProcessThreadCount_Object = MibTableColumn
processThreadCount = _ProcessThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 14),
    _ProcessThreadCount_Type()
)
processThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processThreadCount.setStatus("mandatory")
_ProcessPriorityBase_Type = Integer32
_ProcessPriorityBase_Object = MibTableColumn
processPriorityBase = _ProcessPriorityBase_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 15),
    _ProcessPriorityBase_Type()
)
processPriorityBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPriorityBase.setStatus("mandatory")
_ProcessElapsedTime_Type = TimeTicks
_ProcessElapsedTime_Object = MibTableColumn
processElapsedTime = _ProcessElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 16),
    _ProcessElapsedTime_Type()
)
processElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processElapsedTime.setStatus("mandatory")
_ProcessIDProcess_Type = Integer32
_ProcessIDProcess_Object = MibTableColumn
processIDProcess = _ProcessIDProcess_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 17),
    _ProcessIDProcess_Type()
)
processIDProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIDProcess.setStatus("mandatory")
_ProcessPoolPagedBytes_Type = Integer32
_ProcessPoolPagedBytes_Object = MibTableColumn
processPoolPagedBytes = _ProcessPoolPagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 18),
    _ProcessPoolPagedBytes_Type()
)
processPoolPagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPoolPagedBytes.setStatus("mandatory")
_ProcessPoolNonpagedBytes_Type = Integer32
_ProcessPoolNonpagedBytes_Object = MibTableColumn
processPoolNonpagedBytes = _ProcessPoolNonpagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 19),
    _ProcessPoolNonpagedBytes_Type()
)
processPoolNonpagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPoolNonpagedBytes.setStatus("mandatory")
_ProcessHandleCount_Type = Integer32
_ProcessHandleCount_Object = MibTableColumn
processHandleCount = _ProcessHandleCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 7, 1, 20),
    _ProcessHandleCount_Type()
)
processHandleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processHandleCount.setStatus("mandatory")
_Redirector_ObjectIdentity = ObjectIdentity
redirector = _Redirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8)
)
_RedirectorBytesTotalPerSec_Type = Integer32
_RedirectorBytesTotalPerSec_Object = MibScalar
redirectorBytesTotalPerSec = _RedirectorBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 1),
    _RedirectorBytesTotalPerSec_Type()
)
redirectorBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorBytesTotalPerSec.setStatus("mandatory")
_RedirectorFileDataOperationsPerSec_Type = Counter32
_RedirectorFileDataOperationsPerSec_Object = MibScalar
redirectorFileDataOperationsPerSec = _RedirectorFileDataOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 2),
    _RedirectorFileDataOperationsPerSec_Type()
)
redirectorFileDataOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorFileDataOperationsPerSec.setStatus("mandatory")
_RedirectorPacketsPerSec_Type = Integer32
_RedirectorPacketsPerSec_Object = MibScalar
redirectorPacketsPerSec = _RedirectorPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 3),
    _RedirectorPacketsPerSec_Type()
)
redirectorPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorPacketsPerSec.setStatus("mandatory")
_RedirectorBytesReceivedPerSec_Type = Integer32
_RedirectorBytesReceivedPerSec_Object = MibScalar
redirectorBytesReceivedPerSec = _RedirectorBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 4),
    _RedirectorBytesReceivedPerSec_Type()
)
redirectorBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorBytesReceivedPerSec.setStatus("mandatory")
_RedirectorPacketsReceivedPerSec_Type = Integer32
_RedirectorPacketsReceivedPerSec_Object = MibScalar
redirectorPacketsReceivedPerSec = _RedirectorPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 5),
    _RedirectorPacketsReceivedPerSec_Type()
)
redirectorPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorPacketsReceivedPerSec.setStatus("mandatory")
_RedirectorReadBytesPagingPerSec_Type = Integer32
_RedirectorReadBytesPagingPerSec_Object = MibScalar
redirectorReadBytesPagingPerSec = _RedirectorReadBytesPagingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 6),
    _RedirectorReadBytesPagingPerSec_Type()
)
redirectorReadBytesPagingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadBytesPagingPerSec.setStatus("mandatory")
_RedirectorReadBytesNon_PagingPerSec_Type = Integer32
_RedirectorReadBytesNon_PagingPerSec_Object = MibScalar
redirectorReadBytesNon_PagingPerSec = _RedirectorReadBytesNon_PagingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 7),
    _RedirectorReadBytesNon_PagingPerSec_Type()
)
redirectorReadBytesNon_PagingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadBytesNon_PagingPerSec.setStatus("mandatory")
_RedirectorReadBytesCachePerSec_Type = Integer32
_RedirectorReadBytesCachePerSec_Object = MibScalar
redirectorReadBytesCachePerSec = _RedirectorReadBytesCachePerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 8),
    _RedirectorReadBytesCachePerSec_Type()
)
redirectorReadBytesCachePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadBytesCachePerSec.setStatus("mandatory")
_RedirectorReadBytesNetworkPerSec_Type = Integer32
_RedirectorReadBytesNetworkPerSec_Object = MibScalar
redirectorReadBytesNetworkPerSec = _RedirectorReadBytesNetworkPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 9),
    _RedirectorReadBytesNetworkPerSec_Type()
)
redirectorReadBytesNetworkPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadBytesNetworkPerSec.setStatus("mandatory")
_RedirectorBytesTransmittedPerSec_Type = Integer32
_RedirectorBytesTransmittedPerSec_Object = MibScalar
redirectorBytesTransmittedPerSec = _RedirectorBytesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 10),
    _RedirectorBytesTransmittedPerSec_Type()
)
redirectorBytesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorBytesTransmittedPerSec.setStatus("mandatory")
_RedirectorPacketsTransmittedPerSec_Type = Integer32
_RedirectorPacketsTransmittedPerSec_Object = MibScalar
redirectorPacketsTransmittedPerSec = _RedirectorPacketsTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 11),
    _RedirectorPacketsTransmittedPerSec_Type()
)
redirectorPacketsTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorPacketsTransmittedPerSec.setStatus("mandatory")
_RedirectorWriteBytesPagingPerSec_Type = Integer32
_RedirectorWriteBytesPagingPerSec_Object = MibScalar
redirectorWriteBytesPagingPerSec = _RedirectorWriteBytesPagingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 12),
    _RedirectorWriteBytesPagingPerSec_Type()
)
redirectorWriteBytesPagingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWriteBytesPagingPerSec.setStatus("mandatory")
_RedirectorWriteBytesNon_PagingPerSec_Type = Integer32
_RedirectorWriteBytesNon_PagingPerSec_Object = MibScalar
redirectorWriteBytesNon_PagingPerSec = _RedirectorWriteBytesNon_PagingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 13),
    _RedirectorWriteBytesNon_PagingPerSec_Type()
)
redirectorWriteBytesNon_PagingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWriteBytesNon_PagingPerSec.setStatus("mandatory")
_RedirectorWriteBytesCachePerSec_Type = Integer32
_RedirectorWriteBytesCachePerSec_Object = MibScalar
redirectorWriteBytesCachePerSec = _RedirectorWriteBytesCachePerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 14),
    _RedirectorWriteBytesCachePerSec_Type()
)
redirectorWriteBytesCachePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWriteBytesCachePerSec.setStatus("mandatory")
_RedirectorWriteBytesNetworkPerSec_Type = Integer32
_RedirectorWriteBytesNetworkPerSec_Object = MibScalar
redirectorWriteBytesNetworkPerSec = _RedirectorWriteBytesNetworkPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 15),
    _RedirectorWriteBytesNetworkPerSec_Type()
)
redirectorWriteBytesNetworkPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWriteBytesNetworkPerSec.setStatus("mandatory")
_RedirectorFileReadOperationsPerSec_Type = Counter32
_RedirectorFileReadOperationsPerSec_Object = MibScalar
redirectorFileReadOperationsPerSec = _RedirectorFileReadOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 16),
    _RedirectorFileReadOperationsPerSec_Type()
)
redirectorFileReadOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorFileReadOperationsPerSec.setStatus("mandatory")
_RedirectorReadOperationsRandomPerSec_Type = Counter32
_RedirectorReadOperationsRandomPerSec_Object = MibScalar
redirectorReadOperationsRandomPerSec = _RedirectorReadOperationsRandomPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 17),
    _RedirectorReadOperationsRandomPerSec_Type()
)
redirectorReadOperationsRandomPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadOperationsRandomPerSec.setStatus("mandatory")
_RedirectorReadPacketsPerSec_Type = Counter32
_RedirectorReadPacketsPerSec_Object = MibScalar
redirectorReadPacketsPerSec = _RedirectorReadPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 18),
    _RedirectorReadPacketsPerSec_Type()
)
redirectorReadPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadPacketsPerSec.setStatus("mandatory")
_RedirectorReadsLargePerSec_Type = Counter32
_RedirectorReadsLargePerSec_Object = MibScalar
redirectorReadsLargePerSec = _RedirectorReadsLargePerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 19),
    _RedirectorReadsLargePerSec_Type()
)
redirectorReadsLargePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadsLargePerSec.setStatus("mandatory")
_RedirectorReadPacketsSmallPerSec_Type = Counter32
_RedirectorReadPacketsSmallPerSec_Object = MibScalar
redirectorReadPacketsSmallPerSec = _RedirectorReadPacketsSmallPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 20),
    _RedirectorReadPacketsSmallPerSec_Type()
)
redirectorReadPacketsSmallPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadPacketsSmallPerSec.setStatus("mandatory")
_RedirectorFileWriteOperationsPerSec_Type = Counter32
_RedirectorFileWriteOperationsPerSec_Object = MibScalar
redirectorFileWriteOperationsPerSec = _RedirectorFileWriteOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 21),
    _RedirectorFileWriteOperationsPerSec_Type()
)
redirectorFileWriteOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorFileWriteOperationsPerSec.setStatus("mandatory")
_RedirectorWriteOperationsRandomPerSec_Type = Counter32
_RedirectorWriteOperationsRandomPerSec_Object = MibScalar
redirectorWriteOperationsRandomPerSec = _RedirectorWriteOperationsRandomPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 22),
    _RedirectorWriteOperationsRandomPerSec_Type()
)
redirectorWriteOperationsRandomPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWriteOperationsRandomPerSec.setStatus("mandatory")
_RedirectorWritePacketsPerSec_Type = Counter32
_RedirectorWritePacketsPerSec_Object = MibScalar
redirectorWritePacketsPerSec = _RedirectorWritePacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 23),
    _RedirectorWritePacketsPerSec_Type()
)
redirectorWritePacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWritePacketsPerSec.setStatus("mandatory")
_RedirectorWritesLargePerSec_Type = Counter32
_RedirectorWritesLargePerSec_Object = MibScalar
redirectorWritesLargePerSec = _RedirectorWritesLargePerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 24),
    _RedirectorWritesLargePerSec_Type()
)
redirectorWritesLargePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWritesLargePerSec.setStatus("mandatory")
_RedirectorWritePacketsSmallPerSec_Type = Counter32
_RedirectorWritePacketsSmallPerSec_Object = MibScalar
redirectorWritePacketsSmallPerSec = _RedirectorWritePacketsSmallPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 25),
    _RedirectorWritePacketsSmallPerSec_Type()
)
redirectorWritePacketsSmallPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWritePacketsSmallPerSec.setStatus("mandatory")
_RedirectorReadsDeniedPerSec_Type = Counter32
_RedirectorReadsDeniedPerSec_Object = MibScalar
redirectorReadsDeniedPerSec = _RedirectorReadsDeniedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 26),
    _RedirectorReadsDeniedPerSec_Type()
)
redirectorReadsDeniedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorReadsDeniedPerSec.setStatus("mandatory")
_RedirectorWritesDeniedPerSec_Type = Counter32
_RedirectorWritesDeniedPerSec_Object = MibScalar
redirectorWritesDeniedPerSec = _RedirectorWritesDeniedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 27),
    _RedirectorWritesDeniedPerSec_Type()
)
redirectorWritesDeniedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorWritesDeniedPerSec.setStatus("mandatory")
_RedirectorNetworkErrorsPerSec_Type = Counter32
_RedirectorNetworkErrorsPerSec_Object = MibScalar
redirectorNetworkErrorsPerSec = _RedirectorNetworkErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 28),
    _RedirectorNetworkErrorsPerSec_Type()
)
redirectorNetworkErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorNetworkErrorsPerSec.setStatus("mandatory")
_RedirectorServerSessions_Type = Integer32
_RedirectorServerSessions_Object = MibScalar
redirectorServerSessions = _RedirectorServerSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 29),
    _RedirectorServerSessions_Type()
)
redirectorServerSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorServerSessions.setStatus("mandatory")
_RedirectorServerReconnects_Type = Integer32
_RedirectorServerReconnects_Object = MibScalar
redirectorServerReconnects = _RedirectorServerReconnects_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 30),
    _RedirectorServerReconnects_Type()
)
redirectorServerReconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorServerReconnects.setStatus("mandatory")
_RedirectorConnectsCore_Type = Integer32
_RedirectorConnectsCore_Object = MibScalar
redirectorConnectsCore = _RedirectorConnectsCore_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 31),
    _RedirectorConnectsCore_Type()
)
redirectorConnectsCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorConnectsCore.setStatus("mandatory")
_RedirectorConnectsLanManager20_Type = Integer32
_RedirectorConnectsLanManager20_Object = MibScalar
redirectorConnectsLanManager20 = _RedirectorConnectsLanManager20_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 32),
    _RedirectorConnectsLanManager20_Type()
)
redirectorConnectsLanManager20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorConnectsLanManager20.setStatus("mandatory")
_RedirectorConnectsLanManager21_Type = Integer32
_RedirectorConnectsLanManager21_Object = MibScalar
redirectorConnectsLanManager21 = _RedirectorConnectsLanManager21_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 33),
    _RedirectorConnectsLanManager21_Type()
)
redirectorConnectsLanManager21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorConnectsLanManager21.setStatus("mandatory")
_RedirectorConnectsWindowsNT_Type = Integer32
_RedirectorConnectsWindowsNT_Object = MibScalar
redirectorConnectsWindowsNT = _RedirectorConnectsWindowsNT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 34),
    _RedirectorConnectsWindowsNT_Type()
)
redirectorConnectsWindowsNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorConnectsWindowsNT.setStatus("mandatory")
_RedirectorServerDisconnects_Type = Integer32
_RedirectorServerDisconnects_Object = MibScalar
redirectorServerDisconnects = _RedirectorServerDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 35),
    _RedirectorServerDisconnects_Type()
)
redirectorServerDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorServerDisconnects.setStatus("mandatory")
_RedirectorServerSessionsHung_Type = Integer32
_RedirectorServerSessionsHung_Object = MibScalar
redirectorServerSessionsHung = _RedirectorServerSessionsHung_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 36),
    _RedirectorServerSessionsHung_Type()
)
redirectorServerSessionsHung.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorServerSessionsHung.setStatus("mandatory")
_RedirectorCurrentCommands_Type = Integer32
_RedirectorCurrentCommands_Object = MibScalar
redirectorCurrentCommands = _RedirectorCurrentCommands_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 8, 37),
    _RedirectorCurrentCommands_Type()
)
redirectorCurrentCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectorCurrentCommands.setStatus("mandatory")
_TCP_ObjectIdentity = ObjectIdentity
tCP = _TCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9)
)
_TcpSegmentsPerSec_Type = Counter32
_TcpSegmentsPerSec_Object = MibScalar
tcpSegmentsPerSec = _TcpSegmentsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 1),
    _TcpSegmentsPerSec_Type()
)
tcpSegmentsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSegmentsPerSec.setStatus("mandatory")
_TcpConnectionsEstablished_Type = Integer32
_TcpConnectionsEstablished_Object = MibScalar
tcpConnectionsEstablished = _TcpConnectionsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 2),
    _TcpConnectionsEstablished_Type()
)
tcpConnectionsEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionsEstablished.setStatus("mandatory")
_TcpConnectionsActive_Type = Integer32
_TcpConnectionsActive_Object = MibScalar
tcpConnectionsActive = _TcpConnectionsActive_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 3),
    _TcpConnectionsActive_Type()
)
tcpConnectionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionsActive.setStatus("mandatory")
_TcpConnectionsPassive_Type = Integer32
_TcpConnectionsPassive_Object = MibScalar
tcpConnectionsPassive = _TcpConnectionsPassive_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 4),
    _TcpConnectionsPassive_Type()
)
tcpConnectionsPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionsPassive.setStatus("mandatory")
_TcpConnectionFailures_Type = Integer32
_TcpConnectionFailures_Object = MibScalar
tcpConnectionFailures = _TcpConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 5),
    _TcpConnectionFailures_Type()
)
tcpConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionFailures.setStatus("mandatory")
_TcpConnectionsReset_Type = Integer32
_TcpConnectionsReset_Object = MibScalar
tcpConnectionsReset = _TcpConnectionsReset_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 6),
    _TcpConnectionsReset_Type()
)
tcpConnectionsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionsReset.setStatus("mandatory")
_TcpSegmentsReceivedPerSec_Type = Counter32
_TcpSegmentsReceivedPerSec_Object = MibScalar
tcpSegmentsReceivedPerSec = _TcpSegmentsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 7),
    _TcpSegmentsReceivedPerSec_Type()
)
tcpSegmentsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSegmentsReceivedPerSec.setStatus("mandatory")
_TcpSegmentsSentPerSec_Type = Counter32
_TcpSegmentsSentPerSec_Object = MibScalar
tcpSegmentsSentPerSec = _TcpSegmentsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 8),
    _TcpSegmentsSentPerSec_Type()
)
tcpSegmentsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSegmentsSentPerSec.setStatus("mandatory")
_TcpSegmentsRetransmittedPerSec_Type = Counter32
_TcpSegmentsRetransmittedPerSec_Object = MibScalar
tcpSegmentsRetransmittedPerSec = _TcpSegmentsRetransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 9, 9),
    _TcpSegmentsRetransmittedPerSec_Type()
)
tcpSegmentsRetransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSegmentsRetransmittedPerSec.setStatus("mandatory")
_IP_ObjectIdentity = ObjectIdentity
iP = _IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10)
)
_IpDatagramsPerSec_Type = Counter32
_IpDatagramsPerSec_Object = MibScalar
ipDatagramsPerSec = _IpDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 1),
    _IpDatagramsPerSec_Type()
)
ipDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsPerSec.setStatus("mandatory")
_IpDatagramsReceivedPerSec_Type = Counter32
_IpDatagramsReceivedPerSec_Object = MibScalar
ipDatagramsReceivedPerSec = _IpDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 2),
    _IpDatagramsReceivedPerSec_Type()
)
ipDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedPerSec.setStatus("mandatory")
_IpDatagramsReceivedHeaderErrors_Type = Integer32
_IpDatagramsReceivedHeaderErrors_Object = MibScalar
ipDatagramsReceivedHeaderErrors = _IpDatagramsReceivedHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 3),
    _IpDatagramsReceivedHeaderErrors_Type()
)
ipDatagramsReceivedHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedHeaderErrors.setStatus("mandatory")
_IpDatagramsReceivedAddressErrors_Type = Integer32
_IpDatagramsReceivedAddressErrors_Object = MibScalar
ipDatagramsReceivedAddressErrors = _IpDatagramsReceivedAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 4),
    _IpDatagramsReceivedAddressErrors_Type()
)
ipDatagramsReceivedAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedAddressErrors.setStatus("mandatory")
_IpDatagramsForwardedPerSec_Type = Counter32
_IpDatagramsForwardedPerSec_Object = MibScalar
ipDatagramsForwardedPerSec = _IpDatagramsForwardedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 5),
    _IpDatagramsForwardedPerSec_Type()
)
ipDatagramsForwardedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsForwardedPerSec.setStatus("mandatory")
_IpDatagramsReceivedUnknownProtocol_Type = Integer32
_IpDatagramsReceivedUnknownProtocol_Object = MibScalar
ipDatagramsReceivedUnknownProtocol = _IpDatagramsReceivedUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 6),
    _IpDatagramsReceivedUnknownProtocol_Type()
)
ipDatagramsReceivedUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedUnknownProtocol.setStatus("mandatory")
_IpDatagramsReceivedDiscarded_Type = Integer32
_IpDatagramsReceivedDiscarded_Object = MibScalar
ipDatagramsReceivedDiscarded = _IpDatagramsReceivedDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 7),
    _IpDatagramsReceivedDiscarded_Type()
)
ipDatagramsReceivedDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedDiscarded.setStatus("mandatory")
_IpDatagramsReceivedDeliveredPerSec_Type = Counter32
_IpDatagramsReceivedDeliveredPerSec_Object = MibScalar
ipDatagramsReceivedDeliveredPerSec = _IpDatagramsReceivedDeliveredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 8),
    _IpDatagramsReceivedDeliveredPerSec_Type()
)
ipDatagramsReceivedDeliveredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsReceivedDeliveredPerSec.setStatus("mandatory")
_IpDatagramsSentPerSec_Type = Counter32
_IpDatagramsSentPerSec_Object = MibScalar
ipDatagramsSentPerSec = _IpDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 9),
    _IpDatagramsSentPerSec_Type()
)
ipDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsSentPerSec.setStatus("mandatory")
_IpDatagramsOutboundDiscarded_Type = Integer32
_IpDatagramsOutboundDiscarded_Object = MibScalar
ipDatagramsOutboundDiscarded = _IpDatagramsOutboundDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 10),
    _IpDatagramsOutboundDiscarded_Type()
)
ipDatagramsOutboundDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsOutboundDiscarded.setStatus("mandatory")
_IpDatagramsOutboundNoRoute_Type = Integer32
_IpDatagramsOutboundNoRoute_Object = MibScalar
ipDatagramsOutboundNoRoute = _IpDatagramsOutboundNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 11),
    _IpDatagramsOutboundNoRoute_Type()
)
ipDatagramsOutboundNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDatagramsOutboundNoRoute.setStatus("mandatory")
_IpFragmentsReceivedPerSec_Type = Counter32
_IpFragmentsReceivedPerSec_Object = MibScalar
ipFragmentsReceivedPerSec = _IpFragmentsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 12),
    _IpFragmentsReceivedPerSec_Type()
)
ipFragmentsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentsReceivedPerSec.setStatus("mandatory")
_IpFragmentsRe_assembledPerSec_Type = Counter32
_IpFragmentsRe_assembledPerSec_Object = MibScalar
ipFragmentsRe_assembledPerSec = _IpFragmentsRe_assembledPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 13),
    _IpFragmentsRe_assembledPerSec_Type()
)
ipFragmentsRe_assembledPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentsRe_assembledPerSec.setStatus("mandatory")
_IpFragmentRe_assemblyFailures_Type = Integer32
_IpFragmentRe_assemblyFailures_Object = MibScalar
ipFragmentRe_assemblyFailures = _IpFragmentRe_assemblyFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 14),
    _IpFragmentRe_assemblyFailures_Type()
)
ipFragmentRe_assemblyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentRe_assemblyFailures.setStatus("mandatory")
_IpFragmentedDatagramsPerSec_Type = Counter32
_IpFragmentedDatagramsPerSec_Object = MibScalar
ipFragmentedDatagramsPerSec = _IpFragmentedDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 15),
    _IpFragmentedDatagramsPerSec_Type()
)
ipFragmentedDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentedDatagramsPerSec.setStatus("mandatory")
_IpFragmentationFailures_Type = Integer32
_IpFragmentationFailures_Object = MibScalar
ipFragmentationFailures = _IpFragmentationFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 16),
    _IpFragmentationFailures_Type()
)
ipFragmentationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentationFailures.setStatus("mandatory")
_IpFragmentsCreatedPerSec_Type = Counter32
_IpFragmentsCreatedPerSec_Object = MibScalar
ipFragmentsCreatedPerSec = _IpFragmentsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 10, 17),
    _IpFragmentsCreatedPerSec_Type()
)
ipFragmentsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentsCreatedPerSec.setStatus("mandatory")
_UDP_ObjectIdentity = ObjectIdentity
uDP = _UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11)
)
_UdpDatagramsPerSec_Type = Counter32
_UdpDatagramsPerSec_Object = MibScalar
udpDatagramsPerSec = _UdpDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11, 1),
    _UdpDatagramsPerSec_Type()
)
udpDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDatagramsPerSec.setStatus("mandatory")
_UdpDatagramsReceivedPerSec_Type = Counter32
_UdpDatagramsReceivedPerSec_Object = MibScalar
udpDatagramsReceivedPerSec = _UdpDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11, 2),
    _UdpDatagramsReceivedPerSec_Type()
)
udpDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDatagramsReceivedPerSec.setStatus("mandatory")
_UdpDatagramsNoPortPerSec_Type = Counter32
_UdpDatagramsNoPortPerSec_Object = MibScalar
udpDatagramsNoPortPerSec = _UdpDatagramsNoPortPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11, 3),
    _UdpDatagramsNoPortPerSec_Type()
)
udpDatagramsNoPortPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDatagramsNoPortPerSec.setStatus("mandatory")
_UdpDatagramsReceivedErrors_Type = Integer32
_UdpDatagramsReceivedErrors_Object = MibScalar
udpDatagramsReceivedErrors = _UdpDatagramsReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11, 4),
    _UdpDatagramsReceivedErrors_Type()
)
udpDatagramsReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDatagramsReceivedErrors.setStatus("mandatory")
_UdpDatagramsSentPerSec_Type = Counter32
_UdpDatagramsSentPerSec_Object = MibScalar
udpDatagramsSentPerSec = _UdpDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 11, 5),
    _UdpDatagramsSentPerSec_Type()
)
udpDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpDatagramsSentPerSec.setStatus("mandatory")
_NetbeuinetBEUITable_Object = MibTable
netbeuinetBEUITable = _NetbeuinetBEUITable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    netbeuinetBEUITable.setStatus("mandatory")
_NetbeuinetBEUIEntry_Object = MibTableRow
netbeuinetBEUIEntry = _NetbeuinetBEUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1)
)
netbeuinetBEUIEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "netbeuinetBEUIIndex"),
)
if mibBuilder.loadTexts:
    netbeuinetBEUIEntry.setStatus("mandatory")
_NetbeuinetBEUIIndex_Type = Integer32
_NetbeuinetBEUIIndex_Object = MibTableColumn
netbeuinetBEUIIndex = _NetbeuinetBEUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 1),
    _NetbeuinetBEUIIndex_Type()
)
netbeuinetBEUIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuinetBEUIIndex.setStatus("mandatory")
_NetbeuinetBEUIInstance_Type = DisplayString
_NetbeuinetBEUIInstance_Object = MibTableColumn
netbeuinetBEUIInstance = _NetbeuinetBEUIInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 2),
    _NetbeuinetBEUIInstance_Type()
)
netbeuinetBEUIInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuinetBEUIInstance.setStatus("mandatory")
_NetbeuiDatagramsPerSec_Type = Counter32
_NetbeuiDatagramsPerSec_Object = MibTableColumn
netbeuiDatagramsPerSec = _NetbeuiDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 3),
    _NetbeuiDatagramsPerSec_Type()
)
netbeuiDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramsPerSec.setStatus("mandatory")
_NetbeuiDatagramBytesPerSec_Type = Integer32
_NetbeuiDatagramBytesPerSec_Object = MibTableColumn
netbeuiDatagramBytesPerSec = _NetbeuiDatagramBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 4),
    _NetbeuiDatagramBytesPerSec_Type()
)
netbeuiDatagramBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramBytesPerSec.setStatus("mandatory")
_NetbeuiPacketsPerSec_Type = Counter32
_NetbeuiPacketsPerSec_Object = MibTableColumn
netbeuiPacketsPerSec = _NetbeuiPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 5),
    _NetbeuiPacketsPerSec_Type()
)
netbeuiPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiPacketsPerSec.setStatus("mandatory")
_NetbeuiFramesPerSec_Type = Counter32
_NetbeuiFramesPerSec_Object = MibTableColumn
netbeuiFramesPerSec = _NetbeuiFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 6),
    _NetbeuiFramesPerSec_Type()
)
netbeuiFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFramesPerSec.setStatus("mandatory")
_NetbeuiFrameBytesPerSec_Type = Integer32
_NetbeuiFrameBytesPerSec_Object = MibTableColumn
netbeuiFrameBytesPerSec = _NetbeuiFrameBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 7),
    _NetbeuiFrameBytesPerSec_Type()
)
netbeuiFrameBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFrameBytesPerSec.setStatus("mandatory")
_NetbeuiBytesTotalPerSec_Type = Integer32
_NetbeuiBytesTotalPerSec_Object = MibTableColumn
netbeuiBytesTotalPerSec = _NetbeuiBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 8),
    _NetbeuiBytesTotalPerSec_Type()
)
netbeuiBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiBytesTotalPerSec.setStatus("mandatory")
_NetbeuiConnectionsOpen_Type = Integer32
_NetbeuiConnectionsOpen_Object = MibTableColumn
netbeuiConnectionsOpen = _NetbeuiConnectionsOpen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 9),
    _NetbeuiConnectionsOpen_Type()
)
netbeuiConnectionsOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiConnectionsOpen.setStatus("mandatory")
_NetbeuiConnectionsNoRetries_Type = Integer32
_NetbeuiConnectionsNoRetries_Object = MibTableColumn
netbeuiConnectionsNoRetries = _NetbeuiConnectionsNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 10),
    _NetbeuiConnectionsNoRetries_Type()
)
netbeuiConnectionsNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiConnectionsNoRetries.setStatus("mandatory")
_NetbeuiConnectionsWithRetries_Type = Integer32
_NetbeuiConnectionsWithRetries_Object = MibTableColumn
netbeuiConnectionsWithRetries = _NetbeuiConnectionsWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 11),
    _NetbeuiConnectionsWithRetries_Type()
)
netbeuiConnectionsWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiConnectionsWithRetries.setStatus("mandatory")
_NetbeuiDisconnectsLocal_Type = Integer32
_NetbeuiDisconnectsLocal_Object = MibTableColumn
netbeuiDisconnectsLocal = _NetbeuiDisconnectsLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 12),
    _NetbeuiDisconnectsLocal_Type()
)
netbeuiDisconnectsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDisconnectsLocal.setStatus("mandatory")
_NetbeuiDisconnectsRemote_Type = Integer32
_NetbeuiDisconnectsRemote_Object = MibTableColumn
netbeuiDisconnectsRemote = _NetbeuiDisconnectsRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 13),
    _NetbeuiDisconnectsRemote_Type()
)
netbeuiDisconnectsRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDisconnectsRemote.setStatus("mandatory")
_NetbeuiFailuresLink_Type = Integer32
_NetbeuiFailuresLink_Object = MibTableColumn
netbeuiFailuresLink = _NetbeuiFailuresLink_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 14),
    _NetbeuiFailuresLink_Type()
)
netbeuiFailuresLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresLink.setStatus("mandatory")
_NetbeuiFailuresAdapter_Type = Integer32
_NetbeuiFailuresAdapter_Object = MibTableColumn
netbeuiFailuresAdapter = _NetbeuiFailuresAdapter_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 15),
    _NetbeuiFailuresAdapter_Type()
)
netbeuiFailuresAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresAdapter.setStatus("mandatory")
_NetbeuiConnectionSessionTimeouts_Type = Integer32
_NetbeuiConnectionSessionTimeouts_Object = MibTableColumn
netbeuiConnectionSessionTimeouts = _NetbeuiConnectionSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 16),
    _NetbeuiConnectionSessionTimeouts_Type()
)
netbeuiConnectionSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiConnectionSessionTimeouts.setStatus("mandatory")
_NetbeuiConnectionsCanceled_Type = Integer32
_NetbeuiConnectionsCanceled_Object = MibTableColumn
netbeuiConnectionsCanceled = _NetbeuiConnectionsCanceled_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 17),
    _NetbeuiConnectionsCanceled_Type()
)
netbeuiConnectionsCanceled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiConnectionsCanceled.setStatus("mandatory")
_NetbeuiFailuresResourceRemote_Type = Integer32
_NetbeuiFailuresResourceRemote_Object = MibTableColumn
netbeuiFailuresResourceRemote = _NetbeuiFailuresResourceRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 18),
    _NetbeuiFailuresResourceRemote_Type()
)
netbeuiFailuresResourceRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresResourceRemote.setStatus("mandatory")
_NetbeuiFailuresResourceLocal_Type = Integer32
_NetbeuiFailuresResourceLocal_Object = MibTableColumn
netbeuiFailuresResourceLocal = _NetbeuiFailuresResourceLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 19),
    _NetbeuiFailuresResourceLocal_Type()
)
netbeuiFailuresResourceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresResourceLocal.setStatus("mandatory")
_NetbeuiFailuresNotFound_Type = Integer32
_NetbeuiFailuresNotFound_Object = MibTableColumn
netbeuiFailuresNotFound = _NetbeuiFailuresNotFound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 20),
    _NetbeuiFailuresNotFound_Type()
)
netbeuiFailuresNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresNotFound.setStatus("mandatory")
_NetbeuiFailuresNoListen_Type = Integer32
_NetbeuiFailuresNoListen_Object = MibTableColumn
netbeuiFailuresNoListen = _NetbeuiFailuresNoListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 21),
    _NetbeuiFailuresNoListen_Type()
)
netbeuiFailuresNoListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFailuresNoListen.setStatus("mandatory")
_NetbeuiDatagramsSentPerSec_Type = Counter32
_NetbeuiDatagramsSentPerSec_Object = MibTableColumn
netbeuiDatagramsSentPerSec = _NetbeuiDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 22),
    _NetbeuiDatagramsSentPerSec_Type()
)
netbeuiDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramsSentPerSec.setStatus("mandatory")
_NetbeuiDatagramBytesSentPerSec_Type = Integer32
_NetbeuiDatagramBytesSentPerSec_Object = MibTableColumn
netbeuiDatagramBytesSentPerSec = _NetbeuiDatagramBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 23),
    _NetbeuiDatagramBytesSentPerSec_Type()
)
netbeuiDatagramBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramBytesSentPerSec.setStatus("mandatory")
_NetbeuiDatagramsReceivedPerSec_Type = Counter32
_NetbeuiDatagramsReceivedPerSec_Object = MibTableColumn
netbeuiDatagramsReceivedPerSec = _NetbeuiDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 24),
    _NetbeuiDatagramsReceivedPerSec_Type()
)
netbeuiDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramsReceivedPerSec.setStatus("mandatory")
_NetbeuiDatagramBytesReceivedPerSec_Type = Integer32
_NetbeuiDatagramBytesReceivedPerSec_Object = MibTableColumn
netbeuiDatagramBytesReceivedPerSec = _NetbeuiDatagramBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 25),
    _NetbeuiDatagramBytesReceivedPerSec_Type()
)
netbeuiDatagramBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiDatagramBytesReceivedPerSec.setStatus("mandatory")
_NetbeuiPacketsSentPerSec_Type = Counter32
_NetbeuiPacketsSentPerSec_Object = MibTableColumn
netbeuiPacketsSentPerSec = _NetbeuiPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 26),
    _NetbeuiPacketsSentPerSec_Type()
)
netbeuiPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiPacketsSentPerSec.setStatus("mandatory")
_NetbeuiPacketsReceivedPerSec_Type = Counter32
_NetbeuiPacketsReceivedPerSec_Object = MibTableColumn
netbeuiPacketsReceivedPerSec = _NetbeuiPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 27),
    _NetbeuiPacketsReceivedPerSec_Type()
)
netbeuiPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiPacketsReceivedPerSec.setStatus("mandatory")
_NetbeuiFramesSentPerSec_Type = Counter32
_NetbeuiFramesSentPerSec_Object = MibTableColumn
netbeuiFramesSentPerSec = _NetbeuiFramesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 28),
    _NetbeuiFramesSentPerSec_Type()
)
netbeuiFramesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFramesSentPerSec.setStatus("mandatory")
_NetbeuiFrameBytesSentPerSec_Type = Integer32
_NetbeuiFrameBytesSentPerSec_Object = MibTableColumn
netbeuiFrameBytesSentPerSec = _NetbeuiFrameBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 29),
    _NetbeuiFrameBytesSentPerSec_Type()
)
netbeuiFrameBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFrameBytesSentPerSec.setStatus("mandatory")
_NetbeuiFramesReceivedPerSec_Type = Counter32
_NetbeuiFramesReceivedPerSec_Object = MibTableColumn
netbeuiFramesReceivedPerSec = _NetbeuiFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 30),
    _NetbeuiFramesReceivedPerSec_Type()
)
netbeuiFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFramesReceivedPerSec.setStatus("mandatory")
_NetbeuiFrameBytesReceivedPerSec_Type = Integer32
_NetbeuiFrameBytesReceivedPerSec_Object = MibTableColumn
netbeuiFrameBytesReceivedPerSec = _NetbeuiFrameBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 31),
    _NetbeuiFrameBytesReceivedPerSec_Type()
)
netbeuiFrameBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFrameBytesReceivedPerSec.setStatus("mandatory")
_NetbeuiFramesRe_SentPerSec_Type = Counter32
_NetbeuiFramesRe_SentPerSec_Object = MibScalar
netbeuiFramesRe_SentPerSec = _NetbeuiFramesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 32),
    _NetbeuiFramesRe_SentPerSec_Type()
)
netbeuiFramesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFramesRe_SentPerSec.setStatus("mandatory")
_NetbeuiFrameBytesRe_SentPerSec_Type = Integer32
_NetbeuiFrameBytesRe_SentPerSec_Object = MibScalar
netbeuiFrameBytesRe_SentPerSec = _NetbeuiFrameBytesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 33),
    _NetbeuiFrameBytesRe_SentPerSec_Type()
)
netbeuiFrameBytesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFrameBytesRe_SentPerSec.setStatus("mandatory")
_NetbeuiFramesRejectedPerSec_Type = Counter32
_NetbeuiFramesRejectedPerSec_Object = MibTableColumn
netbeuiFramesRejectedPerSec = _NetbeuiFramesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 34),
    _NetbeuiFramesRejectedPerSec_Type()
)
netbeuiFramesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFramesRejectedPerSec.setStatus("mandatory")
_NetbeuiFrameBytesRejectedPerSec_Type = Integer32
_NetbeuiFrameBytesRejectedPerSec_Object = MibTableColumn
netbeuiFrameBytesRejectedPerSec = _NetbeuiFrameBytesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 35),
    _NetbeuiFrameBytesRejectedPerSec_Type()
)
netbeuiFrameBytesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiFrameBytesRejectedPerSec.setStatus("mandatory")
_NetbeuiExpirationsResponse_Type = Integer32
_NetbeuiExpirationsResponse_Object = MibTableColumn
netbeuiExpirationsResponse = _NetbeuiExpirationsResponse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 36),
    _NetbeuiExpirationsResponse_Type()
)
netbeuiExpirationsResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiExpirationsResponse.setStatus("mandatory")
_NetbeuiExpirationsAck_Type = Integer32
_NetbeuiExpirationsAck_Object = MibTableColumn
netbeuiExpirationsAck = _NetbeuiExpirationsAck_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 37),
    _NetbeuiExpirationsAck_Type()
)
netbeuiExpirationsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiExpirationsAck.setStatus("mandatory")
_NetbeuiWindowSendMaximum_Type = Integer32
_NetbeuiWindowSendMaximum_Object = MibTableColumn
netbeuiWindowSendMaximum = _NetbeuiWindowSendMaximum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 38),
    _NetbeuiWindowSendMaximum_Type()
)
netbeuiWindowSendMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiWindowSendMaximum.setStatus("mandatory")
_NetbeuiWindowSendAverage_Type = Integer32
_NetbeuiWindowSendAverage_Object = MibTableColumn
netbeuiWindowSendAverage = _NetbeuiWindowSendAverage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 39),
    _NetbeuiWindowSendAverage_Type()
)
netbeuiWindowSendAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiWindowSendAverage.setStatus("mandatory")
_NetbeuiPiggybackAckQueuedPerSec_Type = Counter32
_NetbeuiPiggybackAckQueuedPerSec_Object = MibTableColumn
netbeuiPiggybackAckQueuedPerSec = _NetbeuiPiggybackAckQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 40),
    _NetbeuiPiggybackAckQueuedPerSec_Type()
)
netbeuiPiggybackAckQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiPiggybackAckQueuedPerSec.setStatus("mandatory")
_NetbeuiPiggybackAckTimeouts_Type = Integer32
_NetbeuiPiggybackAckTimeouts_Object = MibTableColumn
netbeuiPiggybackAckTimeouts = _NetbeuiPiggybackAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 12, 1, 41),
    _NetbeuiPiggybackAckTimeouts_Type()
)
netbeuiPiggybackAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netbeuiPiggybackAckTimeouts.setStatus("mandatory")
_NbtconnnBT_ConnectionTable_Object = MibTable
nbtconnnBT_ConnectionTable = _NbtconnnBT_ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    nbtconnnBT_ConnectionTable.setStatus("mandatory")
_NbtconnnBT_ConnectionEntry_Object = MibTableRow
nbtconnnBT_ConnectionEntry = _NbtconnnBT_ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1)
)
nbtconnnBT_ConnectionEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "nbtconnnBT-ConnectionIndex"),
)
if mibBuilder.loadTexts:
    nbtconnnBT_ConnectionEntry.setStatus("mandatory")
_NbtconnnBT_ConnectionIndex_Type = Integer32
_NbtconnnBT_ConnectionIndex_Object = MibScalar
nbtconnnBT_ConnectionIndex = _NbtconnnBT_ConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1, 1),
    _NbtconnnBT_ConnectionIndex_Type()
)
nbtconnnBT_ConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbtconnnBT_ConnectionIndex.setStatus("mandatory")
_NbtconnnBT_ConnectionInstance_Type = DisplayString
_NbtconnnBT_ConnectionInstance_Object = MibScalar
nbtconnnBT_ConnectionInstance = _NbtconnnBT_ConnectionInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1, 2),
    _NbtconnnBT_ConnectionInstance_Type()
)
nbtconnnBT_ConnectionInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbtconnnBT_ConnectionInstance.setStatus("mandatory")
_NbtconnBytesReceivedPerSec_Type = Integer32
_NbtconnBytesReceivedPerSec_Object = MibTableColumn
nbtconnBytesReceivedPerSec = _NbtconnBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1, 3),
    _NbtconnBytesReceivedPerSec_Type()
)
nbtconnBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbtconnBytesReceivedPerSec.setStatus("mandatory")
_NbtconnBytesSentPerSec_Type = Integer32
_NbtconnBytesSentPerSec_Object = MibTableColumn
nbtconnBytesSentPerSec = _NbtconnBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1, 4),
    _NbtconnBytesSentPerSec_Type()
)
nbtconnBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbtconnBytesSentPerSec.setStatus("mandatory")
_NbtconnBytesTotalPerSec_Type = Integer32
_NbtconnBytesTotalPerSec_Object = MibTableColumn
nbtconnBytesTotalPerSec = _NbtconnBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 13, 1, 5),
    _NbtconnBytesTotalPerSec_Type()
)
nbtconnBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbtconnBytesTotalPerSec.setStatus("mandatory")
_NwlinkipxnWLink_IPXTable_Object = MibTable
nwlinkipxnWLink_IPXTable = _NwlinkipxnWLink_IPXTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    nwlinkipxnWLink_IPXTable.setStatus("mandatory")
_NwlinkipxnWLink_IPXEntry_Object = MibTableRow
nwlinkipxnWLink_IPXEntry = _NwlinkipxnWLink_IPXEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1)
)
nwlinkipxnWLink_IPXEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "nwlinkipxnWLink-IPXIndex"),
)
if mibBuilder.loadTexts:
    nwlinkipxnWLink_IPXEntry.setStatus("mandatory")
_NwlinkipxnWLink_IPXIndex_Type = Integer32
_NwlinkipxnWLink_IPXIndex_Object = MibScalar
nwlinkipxnWLink_IPXIndex = _NwlinkipxnWLink_IPXIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 1),
    _NwlinkipxnWLink_IPXIndex_Type()
)
nwlinkipxnWLink_IPXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxnWLink_IPXIndex.setStatus("mandatory")
_NwlinkipxnWLink_IPXInstance_Type = DisplayString
_NwlinkipxnWLink_IPXInstance_Object = MibScalar
nwlinkipxnWLink_IPXInstance = _NwlinkipxnWLink_IPXInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 2),
    _NwlinkipxnWLink_IPXInstance_Type()
)
nwlinkipxnWLink_IPXInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxnWLink_IPXInstance.setStatus("mandatory")
_NwlinkipxDatagramsPerSec_Type = Counter32
_NwlinkipxDatagramsPerSec_Object = MibTableColumn
nwlinkipxDatagramsPerSec = _NwlinkipxDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 3),
    _NwlinkipxDatagramsPerSec_Type()
)
nwlinkipxDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramsPerSec.setStatus("mandatory")
_NwlinkipxDatagramBytesPerSec_Type = Integer32
_NwlinkipxDatagramBytesPerSec_Object = MibTableColumn
nwlinkipxDatagramBytesPerSec = _NwlinkipxDatagramBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 4),
    _NwlinkipxDatagramBytesPerSec_Type()
)
nwlinkipxDatagramBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramBytesPerSec.setStatus("mandatory")
_NwlinkipxPacketsPerSec_Type = Counter32
_NwlinkipxPacketsPerSec_Object = MibTableColumn
nwlinkipxPacketsPerSec = _NwlinkipxPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 5),
    _NwlinkipxPacketsPerSec_Type()
)
nwlinkipxPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxPacketsPerSec.setStatus("mandatory")
_NwlinkipxFramesPerSec_Type = Counter32
_NwlinkipxFramesPerSec_Object = MibTableColumn
nwlinkipxFramesPerSec = _NwlinkipxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 6),
    _NwlinkipxFramesPerSec_Type()
)
nwlinkipxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFramesPerSec.setStatus("mandatory")
_NwlinkipxFrameBytesPerSec_Type = Integer32
_NwlinkipxFrameBytesPerSec_Object = MibTableColumn
nwlinkipxFrameBytesPerSec = _NwlinkipxFrameBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 7),
    _NwlinkipxFrameBytesPerSec_Type()
)
nwlinkipxFrameBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFrameBytesPerSec.setStatus("mandatory")
_NwlinkipxBytesTotalPerSec_Type = Integer32
_NwlinkipxBytesTotalPerSec_Object = MibTableColumn
nwlinkipxBytesTotalPerSec = _NwlinkipxBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 8),
    _NwlinkipxBytesTotalPerSec_Type()
)
nwlinkipxBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxBytesTotalPerSec.setStatus("mandatory")
_NwlinkipxConnectionsOpen_Type = Integer32
_NwlinkipxConnectionsOpen_Object = MibTableColumn
nwlinkipxConnectionsOpen = _NwlinkipxConnectionsOpen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 9),
    _NwlinkipxConnectionsOpen_Type()
)
nwlinkipxConnectionsOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxConnectionsOpen.setStatus("mandatory")
_NwlinkipxConnectionsNoRetries_Type = Integer32
_NwlinkipxConnectionsNoRetries_Object = MibTableColumn
nwlinkipxConnectionsNoRetries = _NwlinkipxConnectionsNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 10),
    _NwlinkipxConnectionsNoRetries_Type()
)
nwlinkipxConnectionsNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxConnectionsNoRetries.setStatus("mandatory")
_NwlinkipxConnectionsWithRetries_Type = Integer32
_NwlinkipxConnectionsWithRetries_Object = MibTableColumn
nwlinkipxConnectionsWithRetries = _NwlinkipxConnectionsWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 11),
    _NwlinkipxConnectionsWithRetries_Type()
)
nwlinkipxConnectionsWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxConnectionsWithRetries.setStatus("mandatory")
_NwlinkipxDisconnectsLocal_Type = Integer32
_NwlinkipxDisconnectsLocal_Object = MibTableColumn
nwlinkipxDisconnectsLocal = _NwlinkipxDisconnectsLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 12),
    _NwlinkipxDisconnectsLocal_Type()
)
nwlinkipxDisconnectsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDisconnectsLocal.setStatus("mandatory")
_NwlinkipxDisconnectsRemote_Type = Integer32
_NwlinkipxDisconnectsRemote_Object = MibTableColumn
nwlinkipxDisconnectsRemote = _NwlinkipxDisconnectsRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 13),
    _NwlinkipxDisconnectsRemote_Type()
)
nwlinkipxDisconnectsRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDisconnectsRemote.setStatus("mandatory")
_NwlinkipxFailuresLink_Type = Integer32
_NwlinkipxFailuresLink_Object = MibTableColumn
nwlinkipxFailuresLink = _NwlinkipxFailuresLink_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 14),
    _NwlinkipxFailuresLink_Type()
)
nwlinkipxFailuresLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresLink.setStatus("mandatory")
_NwlinkipxFailuresAdapter_Type = Integer32
_NwlinkipxFailuresAdapter_Object = MibTableColumn
nwlinkipxFailuresAdapter = _NwlinkipxFailuresAdapter_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 15),
    _NwlinkipxFailuresAdapter_Type()
)
nwlinkipxFailuresAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresAdapter.setStatus("mandatory")
_NwlinkipxConnectionSessionTimeouts_Type = Integer32
_NwlinkipxConnectionSessionTimeouts_Object = MibTableColumn
nwlinkipxConnectionSessionTimeouts = _NwlinkipxConnectionSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 16),
    _NwlinkipxConnectionSessionTimeouts_Type()
)
nwlinkipxConnectionSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxConnectionSessionTimeouts.setStatus("mandatory")
_NwlinkipxConnectionsCanceled_Type = Integer32
_NwlinkipxConnectionsCanceled_Object = MibTableColumn
nwlinkipxConnectionsCanceled = _NwlinkipxConnectionsCanceled_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 17),
    _NwlinkipxConnectionsCanceled_Type()
)
nwlinkipxConnectionsCanceled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxConnectionsCanceled.setStatus("mandatory")
_NwlinkipxFailuresResourceRemote_Type = Integer32
_NwlinkipxFailuresResourceRemote_Object = MibTableColumn
nwlinkipxFailuresResourceRemote = _NwlinkipxFailuresResourceRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 18),
    _NwlinkipxFailuresResourceRemote_Type()
)
nwlinkipxFailuresResourceRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresResourceRemote.setStatus("mandatory")
_NwlinkipxFailuresResourceLocal_Type = Integer32
_NwlinkipxFailuresResourceLocal_Object = MibTableColumn
nwlinkipxFailuresResourceLocal = _NwlinkipxFailuresResourceLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 19),
    _NwlinkipxFailuresResourceLocal_Type()
)
nwlinkipxFailuresResourceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresResourceLocal.setStatus("mandatory")
_NwlinkipxFailuresNotFound_Type = Integer32
_NwlinkipxFailuresNotFound_Object = MibTableColumn
nwlinkipxFailuresNotFound = _NwlinkipxFailuresNotFound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 20),
    _NwlinkipxFailuresNotFound_Type()
)
nwlinkipxFailuresNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresNotFound.setStatus("mandatory")
_NwlinkipxFailuresNoListen_Type = Integer32
_NwlinkipxFailuresNoListen_Object = MibTableColumn
nwlinkipxFailuresNoListen = _NwlinkipxFailuresNoListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 21),
    _NwlinkipxFailuresNoListen_Type()
)
nwlinkipxFailuresNoListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFailuresNoListen.setStatus("mandatory")
_NwlinkipxDatagramsSentPerSec_Type = Counter32
_NwlinkipxDatagramsSentPerSec_Object = MibTableColumn
nwlinkipxDatagramsSentPerSec = _NwlinkipxDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 22),
    _NwlinkipxDatagramsSentPerSec_Type()
)
nwlinkipxDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramsSentPerSec.setStatus("mandatory")
_NwlinkipxDatagramBytesSentPerSec_Type = Integer32
_NwlinkipxDatagramBytesSentPerSec_Object = MibTableColumn
nwlinkipxDatagramBytesSentPerSec = _NwlinkipxDatagramBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 23),
    _NwlinkipxDatagramBytesSentPerSec_Type()
)
nwlinkipxDatagramBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramBytesSentPerSec.setStatus("mandatory")
_NwlinkipxDatagramsReceivedPerSec_Type = Counter32
_NwlinkipxDatagramsReceivedPerSec_Object = MibTableColumn
nwlinkipxDatagramsReceivedPerSec = _NwlinkipxDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 24),
    _NwlinkipxDatagramsReceivedPerSec_Type()
)
nwlinkipxDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramsReceivedPerSec.setStatus("mandatory")
_NwlinkipxDatagramBytesReceivedPerSec_Type = Integer32
_NwlinkipxDatagramBytesReceivedPerSec_Object = MibTableColumn
nwlinkipxDatagramBytesReceivedPerSec = _NwlinkipxDatagramBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 25),
    _NwlinkipxDatagramBytesReceivedPerSec_Type()
)
nwlinkipxDatagramBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxDatagramBytesReceivedPerSec.setStatus("mandatory")
_NwlinkipxPacketsSentPerSec_Type = Counter32
_NwlinkipxPacketsSentPerSec_Object = MibTableColumn
nwlinkipxPacketsSentPerSec = _NwlinkipxPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 26),
    _NwlinkipxPacketsSentPerSec_Type()
)
nwlinkipxPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxPacketsSentPerSec.setStatus("mandatory")
_NwlinkipxPacketsReceivedPerSec_Type = Counter32
_NwlinkipxPacketsReceivedPerSec_Object = MibTableColumn
nwlinkipxPacketsReceivedPerSec = _NwlinkipxPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 27),
    _NwlinkipxPacketsReceivedPerSec_Type()
)
nwlinkipxPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxPacketsReceivedPerSec.setStatus("mandatory")
_NwlinkipxFramesSentPerSec_Type = Counter32
_NwlinkipxFramesSentPerSec_Object = MibTableColumn
nwlinkipxFramesSentPerSec = _NwlinkipxFramesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 28),
    _NwlinkipxFramesSentPerSec_Type()
)
nwlinkipxFramesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFramesSentPerSec.setStatus("mandatory")
_NwlinkipxFrameBytesSentPerSec_Type = Integer32
_NwlinkipxFrameBytesSentPerSec_Object = MibTableColumn
nwlinkipxFrameBytesSentPerSec = _NwlinkipxFrameBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 29),
    _NwlinkipxFrameBytesSentPerSec_Type()
)
nwlinkipxFrameBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFrameBytesSentPerSec.setStatus("mandatory")
_NwlinkipxFramesReceivedPerSec_Type = Counter32
_NwlinkipxFramesReceivedPerSec_Object = MibTableColumn
nwlinkipxFramesReceivedPerSec = _NwlinkipxFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 30),
    _NwlinkipxFramesReceivedPerSec_Type()
)
nwlinkipxFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFramesReceivedPerSec.setStatus("mandatory")
_NwlinkipxFrameBytesReceivedPerSec_Type = Integer32
_NwlinkipxFrameBytesReceivedPerSec_Object = MibTableColumn
nwlinkipxFrameBytesReceivedPerSec = _NwlinkipxFrameBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 31),
    _NwlinkipxFrameBytesReceivedPerSec_Type()
)
nwlinkipxFrameBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFrameBytesReceivedPerSec.setStatus("mandatory")
_NwlinkipxFramesRe_SentPerSec_Type = Counter32
_NwlinkipxFramesRe_SentPerSec_Object = MibScalar
nwlinkipxFramesRe_SentPerSec = _NwlinkipxFramesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 32),
    _NwlinkipxFramesRe_SentPerSec_Type()
)
nwlinkipxFramesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFramesRe_SentPerSec.setStatus("mandatory")
_NwlinkipxFrameBytesRe_SentPerSec_Type = Integer32
_NwlinkipxFrameBytesRe_SentPerSec_Object = MibScalar
nwlinkipxFrameBytesRe_SentPerSec = _NwlinkipxFrameBytesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 33),
    _NwlinkipxFrameBytesRe_SentPerSec_Type()
)
nwlinkipxFrameBytesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFrameBytesRe_SentPerSec.setStatus("mandatory")
_NwlinkipxFramesRejectedPerSec_Type = Counter32
_NwlinkipxFramesRejectedPerSec_Object = MibTableColumn
nwlinkipxFramesRejectedPerSec = _NwlinkipxFramesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 34),
    _NwlinkipxFramesRejectedPerSec_Type()
)
nwlinkipxFramesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFramesRejectedPerSec.setStatus("mandatory")
_NwlinkipxFrameBytesRejectedPerSec_Type = Integer32
_NwlinkipxFrameBytesRejectedPerSec_Object = MibTableColumn
nwlinkipxFrameBytesRejectedPerSec = _NwlinkipxFrameBytesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 35),
    _NwlinkipxFrameBytesRejectedPerSec_Type()
)
nwlinkipxFrameBytesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxFrameBytesRejectedPerSec.setStatus("mandatory")
_NwlinkipxExpirationsResponse_Type = Integer32
_NwlinkipxExpirationsResponse_Object = MibTableColumn
nwlinkipxExpirationsResponse = _NwlinkipxExpirationsResponse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 36),
    _NwlinkipxExpirationsResponse_Type()
)
nwlinkipxExpirationsResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxExpirationsResponse.setStatus("mandatory")
_NwlinkipxExpirationsAck_Type = Integer32
_NwlinkipxExpirationsAck_Object = MibTableColumn
nwlinkipxExpirationsAck = _NwlinkipxExpirationsAck_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 37),
    _NwlinkipxExpirationsAck_Type()
)
nwlinkipxExpirationsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxExpirationsAck.setStatus("mandatory")
_NwlinkipxWindowSendMaximum_Type = Integer32
_NwlinkipxWindowSendMaximum_Object = MibTableColumn
nwlinkipxWindowSendMaximum = _NwlinkipxWindowSendMaximum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 38),
    _NwlinkipxWindowSendMaximum_Type()
)
nwlinkipxWindowSendMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxWindowSendMaximum.setStatus("mandatory")
_NwlinkipxWindowSendAverage_Type = Integer32
_NwlinkipxWindowSendAverage_Object = MibTableColumn
nwlinkipxWindowSendAverage = _NwlinkipxWindowSendAverage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 39),
    _NwlinkipxWindowSendAverage_Type()
)
nwlinkipxWindowSendAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxWindowSendAverage.setStatus("mandatory")
_NwlinkipxPiggybackAckQueuedPerSec_Type = Counter32
_NwlinkipxPiggybackAckQueuedPerSec_Object = MibTableColumn
nwlinkipxPiggybackAckQueuedPerSec = _NwlinkipxPiggybackAckQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 40),
    _NwlinkipxPiggybackAckQueuedPerSec_Type()
)
nwlinkipxPiggybackAckQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxPiggybackAckQueuedPerSec.setStatus("mandatory")
_NwlinkipxPiggybackAckTimeouts_Type = Integer32
_NwlinkipxPiggybackAckTimeouts_Object = MibTableColumn
nwlinkipxPiggybackAckTimeouts = _NwlinkipxPiggybackAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 14, 1, 41),
    _NwlinkipxPiggybackAckTimeouts_Type()
)
nwlinkipxPiggybackAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkipxPiggybackAckTimeouts.setStatus("mandatory")
_NwlinkspxnWLink_SPXTable_Object = MibTable
nwlinkspxnWLink_SPXTable = _NwlinkspxnWLink_SPXTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    nwlinkspxnWLink_SPXTable.setStatus("mandatory")
_NwlinkspxnWLink_SPXEntry_Object = MibTableRow
nwlinkspxnWLink_SPXEntry = _NwlinkspxnWLink_SPXEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1)
)
nwlinkspxnWLink_SPXEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "nwlinkspxnWLink-SPXIndex"),
)
if mibBuilder.loadTexts:
    nwlinkspxnWLink_SPXEntry.setStatus("mandatory")
_NwlinkspxnWLink_SPXIndex_Type = Integer32
_NwlinkspxnWLink_SPXIndex_Object = MibScalar
nwlinkspxnWLink_SPXIndex = _NwlinkspxnWLink_SPXIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 1),
    _NwlinkspxnWLink_SPXIndex_Type()
)
nwlinkspxnWLink_SPXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxnWLink_SPXIndex.setStatus("mandatory")
_NwlinkspxnWLink_SPXInstance_Type = DisplayString
_NwlinkspxnWLink_SPXInstance_Object = MibScalar
nwlinkspxnWLink_SPXInstance = _NwlinkspxnWLink_SPXInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 2),
    _NwlinkspxnWLink_SPXInstance_Type()
)
nwlinkspxnWLink_SPXInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxnWLink_SPXInstance.setStatus("mandatory")
_NwlinkspxDatagramsPerSec_Type = Counter32
_NwlinkspxDatagramsPerSec_Object = MibTableColumn
nwlinkspxDatagramsPerSec = _NwlinkspxDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 3),
    _NwlinkspxDatagramsPerSec_Type()
)
nwlinkspxDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramsPerSec.setStatus("mandatory")
_NwlinkspxDatagramBytesPerSec_Type = Integer32
_NwlinkspxDatagramBytesPerSec_Object = MibTableColumn
nwlinkspxDatagramBytesPerSec = _NwlinkspxDatagramBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 4),
    _NwlinkspxDatagramBytesPerSec_Type()
)
nwlinkspxDatagramBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramBytesPerSec.setStatus("mandatory")
_NwlinkspxPacketsPerSec_Type = Counter32
_NwlinkspxPacketsPerSec_Object = MibTableColumn
nwlinkspxPacketsPerSec = _NwlinkspxPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 5),
    _NwlinkspxPacketsPerSec_Type()
)
nwlinkspxPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxPacketsPerSec.setStatus("mandatory")
_NwlinkspxFramesPerSec_Type = Counter32
_NwlinkspxFramesPerSec_Object = MibTableColumn
nwlinkspxFramesPerSec = _NwlinkspxFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 6),
    _NwlinkspxFramesPerSec_Type()
)
nwlinkspxFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFramesPerSec.setStatus("mandatory")
_NwlinkspxFrameBytesPerSec_Type = Integer32
_NwlinkspxFrameBytesPerSec_Object = MibTableColumn
nwlinkspxFrameBytesPerSec = _NwlinkspxFrameBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 7),
    _NwlinkspxFrameBytesPerSec_Type()
)
nwlinkspxFrameBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFrameBytesPerSec.setStatus("mandatory")
_NwlinkspxBytesTotalPerSec_Type = Integer32
_NwlinkspxBytesTotalPerSec_Object = MibTableColumn
nwlinkspxBytesTotalPerSec = _NwlinkspxBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 8),
    _NwlinkspxBytesTotalPerSec_Type()
)
nwlinkspxBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxBytesTotalPerSec.setStatus("mandatory")
_NwlinkspxConnectionsOpen_Type = Integer32
_NwlinkspxConnectionsOpen_Object = MibTableColumn
nwlinkspxConnectionsOpen = _NwlinkspxConnectionsOpen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 9),
    _NwlinkspxConnectionsOpen_Type()
)
nwlinkspxConnectionsOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxConnectionsOpen.setStatus("mandatory")
_NwlinkspxConnectionsNoRetries_Type = Integer32
_NwlinkspxConnectionsNoRetries_Object = MibTableColumn
nwlinkspxConnectionsNoRetries = _NwlinkspxConnectionsNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 10),
    _NwlinkspxConnectionsNoRetries_Type()
)
nwlinkspxConnectionsNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxConnectionsNoRetries.setStatus("mandatory")
_NwlinkspxConnectionsWithRetries_Type = Integer32
_NwlinkspxConnectionsWithRetries_Object = MibTableColumn
nwlinkspxConnectionsWithRetries = _NwlinkspxConnectionsWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 11),
    _NwlinkspxConnectionsWithRetries_Type()
)
nwlinkspxConnectionsWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxConnectionsWithRetries.setStatus("mandatory")
_NwlinkspxDisconnectsLocal_Type = Integer32
_NwlinkspxDisconnectsLocal_Object = MibTableColumn
nwlinkspxDisconnectsLocal = _NwlinkspxDisconnectsLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 12),
    _NwlinkspxDisconnectsLocal_Type()
)
nwlinkspxDisconnectsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDisconnectsLocal.setStatus("mandatory")
_NwlinkspxDisconnectsRemote_Type = Integer32
_NwlinkspxDisconnectsRemote_Object = MibTableColumn
nwlinkspxDisconnectsRemote = _NwlinkspxDisconnectsRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 13),
    _NwlinkspxDisconnectsRemote_Type()
)
nwlinkspxDisconnectsRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDisconnectsRemote.setStatus("mandatory")
_NwlinkspxFailuresLink_Type = Integer32
_NwlinkspxFailuresLink_Object = MibTableColumn
nwlinkspxFailuresLink = _NwlinkspxFailuresLink_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 14),
    _NwlinkspxFailuresLink_Type()
)
nwlinkspxFailuresLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresLink.setStatus("mandatory")
_NwlinkspxFailuresAdapter_Type = Integer32
_NwlinkspxFailuresAdapter_Object = MibTableColumn
nwlinkspxFailuresAdapter = _NwlinkspxFailuresAdapter_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 15),
    _NwlinkspxFailuresAdapter_Type()
)
nwlinkspxFailuresAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresAdapter.setStatus("mandatory")
_NwlinkspxConnectionSessionTimeouts_Type = Integer32
_NwlinkspxConnectionSessionTimeouts_Object = MibTableColumn
nwlinkspxConnectionSessionTimeouts = _NwlinkspxConnectionSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 16),
    _NwlinkspxConnectionSessionTimeouts_Type()
)
nwlinkspxConnectionSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxConnectionSessionTimeouts.setStatus("mandatory")
_NwlinkspxConnectionsCanceled_Type = Integer32
_NwlinkspxConnectionsCanceled_Object = MibTableColumn
nwlinkspxConnectionsCanceled = _NwlinkspxConnectionsCanceled_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 17),
    _NwlinkspxConnectionsCanceled_Type()
)
nwlinkspxConnectionsCanceled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxConnectionsCanceled.setStatus("mandatory")
_NwlinkspxFailuresResourceRemote_Type = Integer32
_NwlinkspxFailuresResourceRemote_Object = MibTableColumn
nwlinkspxFailuresResourceRemote = _NwlinkspxFailuresResourceRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 18),
    _NwlinkspxFailuresResourceRemote_Type()
)
nwlinkspxFailuresResourceRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresResourceRemote.setStatus("mandatory")
_NwlinkspxFailuresResourceLocal_Type = Integer32
_NwlinkspxFailuresResourceLocal_Object = MibTableColumn
nwlinkspxFailuresResourceLocal = _NwlinkspxFailuresResourceLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 19),
    _NwlinkspxFailuresResourceLocal_Type()
)
nwlinkspxFailuresResourceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresResourceLocal.setStatus("mandatory")
_NwlinkspxFailuresNotFound_Type = Integer32
_NwlinkspxFailuresNotFound_Object = MibTableColumn
nwlinkspxFailuresNotFound = _NwlinkspxFailuresNotFound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 20),
    _NwlinkspxFailuresNotFound_Type()
)
nwlinkspxFailuresNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresNotFound.setStatus("mandatory")
_NwlinkspxFailuresNoListen_Type = Integer32
_NwlinkspxFailuresNoListen_Object = MibTableColumn
nwlinkspxFailuresNoListen = _NwlinkspxFailuresNoListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 21),
    _NwlinkspxFailuresNoListen_Type()
)
nwlinkspxFailuresNoListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFailuresNoListen.setStatus("mandatory")
_NwlinkspxDatagramsSentPerSec_Type = Counter32
_NwlinkspxDatagramsSentPerSec_Object = MibTableColumn
nwlinkspxDatagramsSentPerSec = _NwlinkspxDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 22),
    _NwlinkspxDatagramsSentPerSec_Type()
)
nwlinkspxDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramsSentPerSec.setStatus("mandatory")
_NwlinkspxDatagramBytesSentPerSec_Type = Integer32
_NwlinkspxDatagramBytesSentPerSec_Object = MibTableColumn
nwlinkspxDatagramBytesSentPerSec = _NwlinkspxDatagramBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 23),
    _NwlinkspxDatagramBytesSentPerSec_Type()
)
nwlinkspxDatagramBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramBytesSentPerSec.setStatus("mandatory")
_NwlinkspxDatagramsReceivedPerSec_Type = Counter32
_NwlinkspxDatagramsReceivedPerSec_Object = MibTableColumn
nwlinkspxDatagramsReceivedPerSec = _NwlinkspxDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 24),
    _NwlinkspxDatagramsReceivedPerSec_Type()
)
nwlinkspxDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramsReceivedPerSec.setStatus("mandatory")
_NwlinkspxDatagramBytesReceivedPerSec_Type = Integer32
_NwlinkspxDatagramBytesReceivedPerSec_Object = MibTableColumn
nwlinkspxDatagramBytesReceivedPerSec = _NwlinkspxDatagramBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 25),
    _NwlinkspxDatagramBytesReceivedPerSec_Type()
)
nwlinkspxDatagramBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxDatagramBytesReceivedPerSec.setStatus("mandatory")
_NwlinkspxPacketsSentPerSec_Type = Counter32
_NwlinkspxPacketsSentPerSec_Object = MibTableColumn
nwlinkspxPacketsSentPerSec = _NwlinkspxPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 26),
    _NwlinkspxPacketsSentPerSec_Type()
)
nwlinkspxPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxPacketsSentPerSec.setStatus("mandatory")
_NwlinkspxPacketsReceivedPerSec_Type = Counter32
_NwlinkspxPacketsReceivedPerSec_Object = MibTableColumn
nwlinkspxPacketsReceivedPerSec = _NwlinkspxPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 27),
    _NwlinkspxPacketsReceivedPerSec_Type()
)
nwlinkspxPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxPacketsReceivedPerSec.setStatus("mandatory")
_NwlinkspxFramesSentPerSec_Type = Counter32
_NwlinkspxFramesSentPerSec_Object = MibTableColumn
nwlinkspxFramesSentPerSec = _NwlinkspxFramesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 28),
    _NwlinkspxFramesSentPerSec_Type()
)
nwlinkspxFramesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFramesSentPerSec.setStatus("mandatory")
_NwlinkspxFrameBytesSentPerSec_Type = Integer32
_NwlinkspxFrameBytesSentPerSec_Object = MibTableColumn
nwlinkspxFrameBytesSentPerSec = _NwlinkspxFrameBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 29),
    _NwlinkspxFrameBytesSentPerSec_Type()
)
nwlinkspxFrameBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFrameBytesSentPerSec.setStatus("mandatory")
_NwlinkspxFramesReceivedPerSec_Type = Counter32
_NwlinkspxFramesReceivedPerSec_Object = MibTableColumn
nwlinkspxFramesReceivedPerSec = _NwlinkspxFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 30),
    _NwlinkspxFramesReceivedPerSec_Type()
)
nwlinkspxFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFramesReceivedPerSec.setStatus("mandatory")
_NwlinkspxFrameBytesReceivedPerSec_Type = Integer32
_NwlinkspxFrameBytesReceivedPerSec_Object = MibTableColumn
nwlinkspxFrameBytesReceivedPerSec = _NwlinkspxFrameBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 31),
    _NwlinkspxFrameBytesReceivedPerSec_Type()
)
nwlinkspxFrameBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFrameBytesReceivedPerSec.setStatus("mandatory")
_NwlinkspxFramesRe_SentPerSec_Type = Counter32
_NwlinkspxFramesRe_SentPerSec_Object = MibScalar
nwlinkspxFramesRe_SentPerSec = _NwlinkspxFramesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 32),
    _NwlinkspxFramesRe_SentPerSec_Type()
)
nwlinkspxFramesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFramesRe_SentPerSec.setStatus("mandatory")
_NwlinkspxFrameBytesRe_SentPerSec_Type = Integer32
_NwlinkspxFrameBytesRe_SentPerSec_Object = MibScalar
nwlinkspxFrameBytesRe_SentPerSec = _NwlinkspxFrameBytesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 33),
    _NwlinkspxFrameBytesRe_SentPerSec_Type()
)
nwlinkspxFrameBytesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFrameBytesRe_SentPerSec.setStatus("mandatory")
_NwlinkspxFramesRejectedPerSec_Type = Counter32
_NwlinkspxFramesRejectedPerSec_Object = MibTableColumn
nwlinkspxFramesRejectedPerSec = _NwlinkspxFramesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 34),
    _NwlinkspxFramesRejectedPerSec_Type()
)
nwlinkspxFramesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFramesRejectedPerSec.setStatus("mandatory")
_NwlinkspxFrameBytesRejectedPerSec_Type = Integer32
_NwlinkspxFrameBytesRejectedPerSec_Object = MibTableColumn
nwlinkspxFrameBytesRejectedPerSec = _NwlinkspxFrameBytesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 35),
    _NwlinkspxFrameBytesRejectedPerSec_Type()
)
nwlinkspxFrameBytesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxFrameBytesRejectedPerSec.setStatus("mandatory")
_NwlinkspxExpirationsResponse_Type = Integer32
_NwlinkspxExpirationsResponse_Object = MibTableColumn
nwlinkspxExpirationsResponse = _NwlinkspxExpirationsResponse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 36),
    _NwlinkspxExpirationsResponse_Type()
)
nwlinkspxExpirationsResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxExpirationsResponse.setStatus("mandatory")
_NwlinkspxExpirationsAck_Type = Integer32
_NwlinkspxExpirationsAck_Object = MibTableColumn
nwlinkspxExpirationsAck = _NwlinkspxExpirationsAck_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 37),
    _NwlinkspxExpirationsAck_Type()
)
nwlinkspxExpirationsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxExpirationsAck.setStatus("mandatory")
_NwlinkspxWindowSendMaximum_Type = Integer32
_NwlinkspxWindowSendMaximum_Object = MibTableColumn
nwlinkspxWindowSendMaximum = _NwlinkspxWindowSendMaximum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 38),
    _NwlinkspxWindowSendMaximum_Type()
)
nwlinkspxWindowSendMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxWindowSendMaximum.setStatus("mandatory")
_NwlinkspxWindowSendAverage_Type = Integer32
_NwlinkspxWindowSendAverage_Object = MibTableColumn
nwlinkspxWindowSendAverage = _NwlinkspxWindowSendAverage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 39),
    _NwlinkspxWindowSendAverage_Type()
)
nwlinkspxWindowSendAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxWindowSendAverage.setStatus("mandatory")
_NwlinkspxPiggybackAckQueuedPerSec_Type = Counter32
_NwlinkspxPiggybackAckQueuedPerSec_Object = MibTableColumn
nwlinkspxPiggybackAckQueuedPerSec = _NwlinkspxPiggybackAckQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 40),
    _NwlinkspxPiggybackAckQueuedPerSec_Type()
)
nwlinkspxPiggybackAckQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxPiggybackAckQueuedPerSec.setStatus("mandatory")
_NwlinkspxPiggybackAckTimeouts_Type = Integer32
_NwlinkspxPiggybackAckTimeouts_Object = MibTableColumn
nwlinkspxPiggybackAckTimeouts = _NwlinkspxPiggybackAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 15, 1, 41),
    _NwlinkspxPiggybackAckTimeouts_Type()
)
nwlinkspxPiggybackAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwlinkspxPiggybackAckTimeouts.setStatus("mandatory")
_RAS_Total_ObjectIdentity = ObjectIdentity
rAS_Total = _RAS_Total_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16)
)
_RastotalBytesTransmitted_Type = Integer32
_RastotalBytesTransmitted_Object = MibScalar
rastotalBytesTransmitted = _RastotalBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 1),
    _RastotalBytesTransmitted_Type()
)
rastotalBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalBytesTransmitted.setStatus("mandatory")
_RastotalBytesReceived_Type = Integer32
_RastotalBytesReceived_Object = MibScalar
rastotalBytesReceived = _RastotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 2),
    _RastotalBytesReceived_Type()
)
rastotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalBytesReceived.setStatus("mandatory")
_RastotalFramesTransmitted_Type = Integer32
_RastotalFramesTransmitted_Object = MibScalar
rastotalFramesTransmitted = _RastotalFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 3),
    _RastotalFramesTransmitted_Type()
)
rastotalFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalFramesTransmitted.setStatus("mandatory")
_RastotalFramesReceived_Type = Integer32
_RastotalFramesReceived_Object = MibScalar
rastotalFramesReceived = _RastotalFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 4),
    _RastotalFramesReceived_Type()
)
rastotalFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalFramesReceived.setStatus("mandatory")
_RastotalPercentCompressionOut_Type = Integer32
_RastotalPercentCompressionOut_Object = MibScalar
rastotalPercentCompressionOut = _RastotalPercentCompressionOut_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 5),
    _RastotalPercentCompressionOut_Type()
)
rastotalPercentCompressionOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalPercentCompressionOut.setStatus("mandatory")
_RastotalPercentCompressionIn_Type = Integer32
_RastotalPercentCompressionIn_Object = MibScalar
rastotalPercentCompressionIn = _RastotalPercentCompressionIn_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 6),
    _RastotalPercentCompressionIn_Type()
)
rastotalPercentCompressionIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalPercentCompressionIn.setStatus("mandatory")
_RastotalCRCErrors_Type = Integer32
_RastotalCRCErrors_Object = MibScalar
rastotalCRCErrors = _RastotalCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 7),
    _RastotalCRCErrors_Type()
)
rastotalCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalCRCErrors.setStatus("mandatory")
_RastotalTimeoutErrors_Type = Integer32
_RastotalTimeoutErrors_Object = MibScalar
rastotalTimeoutErrors = _RastotalTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 8),
    _RastotalTimeoutErrors_Type()
)
rastotalTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalTimeoutErrors.setStatus("mandatory")
_RastotalSerialOverrunErrors_Type = Integer32
_RastotalSerialOverrunErrors_Object = MibScalar
rastotalSerialOverrunErrors = _RastotalSerialOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 9),
    _RastotalSerialOverrunErrors_Type()
)
rastotalSerialOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalSerialOverrunErrors.setStatus("mandatory")
_RastotalAlignmentErrors_Type = Integer32
_RastotalAlignmentErrors_Object = MibScalar
rastotalAlignmentErrors = _RastotalAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 10),
    _RastotalAlignmentErrors_Type()
)
rastotalAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalAlignmentErrors.setStatus("mandatory")
_RastotalBufferOverrunErrors_Type = Integer32
_RastotalBufferOverrunErrors_Object = MibScalar
rastotalBufferOverrunErrors = _RastotalBufferOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 11),
    _RastotalBufferOverrunErrors_Type()
)
rastotalBufferOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalBufferOverrunErrors.setStatus("mandatory")
_RastotalTotalErrors_Type = Integer32
_RastotalTotalErrors_Object = MibScalar
rastotalTotalErrors = _RastotalTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 12),
    _RastotalTotalErrors_Type()
)
rastotalTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalTotalErrors.setStatus("mandatory")
_RastotalBytesTransmittedPerSec_Type = Counter32
_RastotalBytesTransmittedPerSec_Object = MibScalar
rastotalBytesTransmittedPerSec = _RastotalBytesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 13),
    _RastotalBytesTransmittedPerSec_Type()
)
rastotalBytesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalBytesTransmittedPerSec.setStatus("mandatory")
_RastotalBytesReceivedPerSec_Type = Counter32
_RastotalBytesReceivedPerSec_Object = MibScalar
rastotalBytesReceivedPerSec = _RastotalBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 14),
    _RastotalBytesReceivedPerSec_Type()
)
rastotalBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalBytesReceivedPerSec.setStatus("mandatory")
_RastotalFramesTransmittedPerSec_Type = Counter32
_RastotalFramesTransmittedPerSec_Object = MibScalar
rastotalFramesTransmittedPerSec = _RastotalFramesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 15),
    _RastotalFramesTransmittedPerSec_Type()
)
rastotalFramesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalFramesTransmittedPerSec.setStatus("mandatory")
_RastotalFramesReceivedPerSec_Type = Counter32
_RastotalFramesReceivedPerSec_Object = MibScalar
rastotalFramesReceivedPerSec = _RastotalFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 16),
    _RastotalFramesReceivedPerSec_Type()
)
rastotalFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalFramesReceivedPerSec.setStatus("mandatory")
_RastotalTotalErrorsPerSec_Type = Counter32
_RastotalTotalErrorsPerSec_Object = MibScalar
rastotalTotalErrorsPerSec = _RastotalTotalErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 17),
    _RastotalTotalErrorsPerSec_Type()
)
rastotalTotalErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalTotalErrorsPerSec.setStatus("mandatory")
_RastotalTotalConnections_Type = Integer32
_RastotalTotalConnections_Object = MibScalar
rastotalTotalConnections = _RastotalTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 16, 18),
    _RastotalTotalConnections_Type()
)
rastotalTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rastotalTotalConnections.setStatus("mandatory")
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17)
)
_ServerBytesTotalPerSec_Type = Integer32
_ServerBytesTotalPerSec_Object = MibScalar
serverBytesTotalPerSec = _ServerBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 1),
    _ServerBytesTotalPerSec_Type()
)
serverBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBytesTotalPerSec.setStatus("mandatory")
_ServerBytesReceivedPerSec_Type = Integer32
_ServerBytesReceivedPerSec_Object = MibScalar
serverBytesReceivedPerSec = _ServerBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 2),
    _ServerBytesReceivedPerSec_Type()
)
serverBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBytesReceivedPerSec.setStatus("mandatory")
_ServerBytesTransmittedPerSec_Type = Integer32
_ServerBytesTransmittedPerSec_Object = MibScalar
serverBytesTransmittedPerSec = _ServerBytesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 3),
    _ServerBytesTransmittedPerSec_Type()
)
serverBytesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBytesTransmittedPerSec.setStatus("mandatory")
_ServerSessionsTimedOut_Type = Integer32
_ServerSessionsTimedOut_Object = MibScalar
serverSessionsTimedOut = _ServerSessionsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 4),
    _ServerSessionsTimedOut_Type()
)
serverSessionsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSessionsTimedOut.setStatus("mandatory")
_ServerSessionsErroredOut_Type = Integer32
_ServerSessionsErroredOut_Object = MibScalar
serverSessionsErroredOut = _ServerSessionsErroredOut_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 5),
    _ServerSessionsErroredOut_Type()
)
serverSessionsErroredOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSessionsErroredOut.setStatus("mandatory")
_ServerSessionsLoggedOff_Type = Integer32
_ServerSessionsLoggedOff_Object = MibScalar
serverSessionsLoggedOff = _ServerSessionsLoggedOff_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 6),
    _ServerSessionsLoggedOff_Type()
)
serverSessionsLoggedOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSessionsLoggedOff.setStatus("mandatory")
_ServerSessionsForcedOff_Type = Integer32
_ServerSessionsForcedOff_Object = MibScalar
serverSessionsForcedOff = _ServerSessionsForcedOff_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 7),
    _ServerSessionsForcedOff_Type()
)
serverSessionsForcedOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSessionsForcedOff.setStatus("mandatory")
_ServerErrorsLogon_Type = Integer32
_ServerErrorsLogon_Object = MibScalar
serverErrorsLogon = _ServerErrorsLogon_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 8),
    _ServerErrorsLogon_Type()
)
serverErrorsLogon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverErrorsLogon.setStatus("mandatory")
_ServerErrorsAccessPermissions_Type = Integer32
_ServerErrorsAccessPermissions_Object = MibScalar
serverErrorsAccessPermissions = _ServerErrorsAccessPermissions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 9),
    _ServerErrorsAccessPermissions_Type()
)
serverErrorsAccessPermissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverErrorsAccessPermissions.setStatus("mandatory")
_ServerErrorsGrantedAccess_Type = Integer32
_ServerErrorsGrantedAccess_Object = MibScalar
serverErrorsGrantedAccess = _ServerErrorsGrantedAccess_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 10),
    _ServerErrorsGrantedAccess_Type()
)
serverErrorsGrantedAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverErrorsGrantedAccess.setStatus("mandatory")
_ServerErrorsSystem_Type = Integer32
_ServerErrorsSystem_Object = MibScalar
serverErrorsSystem = _ServerErrorsSystem_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 11),
    _ServerErrorsSystem_Type()
)
serverErrorsSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverErrorsSystem.setStatus("mandatory")
_ServerBlockingRequestsRejected_Type = Counter32
_ServerBlockingRequestsRejected_Object = MibScalar
serverBlockingRequestsRejected = _ServerBlockingRequestsRejected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 12),
    _ServerBlockingRequestsRejected_Type()
)
serverBlockingRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBlockingRequestsRejected.setStatus("mandatory")
_ServerWorkItemShortages_Type = Counter32
_ServerWorkItemShortages_Object = MibScalar
serverWorkItemShortages = _ServerWorkItemShortages_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 13),
    _ServerWorkItemShortages_Type()
)
serverWorkItemShortages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverWorkItemShortages.setStatus("mandatory")
_ServerFilesOpenedTotal_Type = Integer32
_ServerFilesOpenedTotal_Object = MibScalar
serverFilesOpenedTotal = _ServerFilesOpenedTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 14),
    _ServerFilesOpenedTotal_Type()
)
serverFilesOpenedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverFilesOpenedTotal.setStatus("mandatory")
_ServerFilesOpen_Type = Integer32
_ServerFilesOpen_Object = MibScalar
serverFilesOpen = _ServerFilesOpen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 15),
    _ServerFilesOpen_Type()
)
serverFilesOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverFilesOpen.setStatus("mandatory")
_ServerServerSessions_Type = Integer32
_ServerServerSessions_Object = MibScalar
serverServerSessions = _ServerServerSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 16),
    _ServerServerSessions_Type()
)
serverServerSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverServerSessions.setStatus("mandatory")
_ServerFileDirectorySearches_Type = Integer32
_ServerFileDirectorySearches_Object = MibScalar
serverFileDirectorySearches = _ServerFileDirectorySearches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 17),
    _ServerFileDirectorySearches_Type()
)
serverFileDirectorySearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverFileDirectorySearches.setStatus("mandatory")
_ServerPoolNonpagedBytes_Type = Integer32
_ServerPoolNonpagedBytes_Object = MibScalar
serverPoolNonpagedBytes = _ServerPoolNonpagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 18),
    _ServerPoolNonpagedBytes_Type()
)
serverPoolNonpagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolNonpagedBytes.setStatus("mandatory")
_ServerPoolNonpagedFailures_Type = Counter32
_ServerPoolNonpagedFailures_Object = MibScalar
serverPoolNonpagedFailures = _ServerPoolNonpagedFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 19),
    _ServerPoolNonpagedFailures_Type()
)
serverPoolNonpagedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolNonpagedFailures.setStatus("mandatory")
_ServerPoolNonpagedPeak_Type = Integer32
_ServerPoolNonpagedPeak_Object = MibScalar
serverPoolNonpagedPeak = _ServerPoolNonpagedPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 20),
    _ServerPoolNonpagedPeak_Type()
)
serverPoolNonpagedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolNonpagedPeak.setStatus("mandatory")
_ServerPoolPagedBytes_Type = Integer32
_ServerPoolPagedBytes_Object = MibScalar
serverPoolPagedBytes = _ServerPoolPagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 21),
    _ServerPoolPagedBytes_Type()
)
serverPoolPagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolPagedBytes.setStatus("mandatory")
_ServerPoolPagedFailures_Type = Integer32
_ServerPoolPagedFailures_Object = MibScalar
serverPoolPagedFailures = _ServerPoolPagedFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 22),
    _ServerPoolPagedFailures_Type()
)
serverPoolPagedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolPagedFailures.setStatus("mandatory")
_ServerPoolPagedPeak_Type = Integer32
_ServerPoolPagedPeak_Object = MibScalar
serverPoolPagedPeak = _ServerPoolPagedPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 23),
    _ServerPoolPagedPeak_Type()
)
serverPoolPagedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPoolPagedPeak.setStatus("mandatory")
_ServerContextBlocksQueuedPerSec_Type = Counter32
_ServerContextBlocksQueuedPerSec_Object = MibScalar
serverContextBlocksQueuedPerSec = _ServerContextBlocksQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 24),
    _ServerContextBlocksQueuedPerSec_Type()
)
serverContextBlocksQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverContextBlocksQueuedPerSec.setStatus("mandatory")
_ServerLogonPerSec_Type = Counter32
_ServerLogonPerSec_Object = MibScalar
serverLogonPerSec = _ServerLogonPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 25),
    _ServerLogonPerSec_Type()
)
serverLogonPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLogonPerSec.setStatus("mandatory")
_ServerLogonTotal_Type = Integer32
_ServerLogonTotal_Object = MibScalar
serverLogonTotal = _ServerLogonTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 17, 26),
    _ServerLogonTotal_Type()
)
serverLogonTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLogonTotal.setStatus("mandatory")
_Srvrqueuesserver_Work_QueuesTable_Object = MibTable
srvrqueuesserver_Work_QueuesTable = _Srvrqueuesserver_Work_QueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18)
)
if mibBuilder.loadTexts:
    srvrqueuesserver_Work_QueuesTable.setStatus("mandatory")
_Srvrqueuesserver_Work_QueuesEntry_Object = MibTableRow
srvrqueuesserver_Work_QueuesEntry = _Srvrqueuesserver_Work_QueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1)
)
srvrqueuesserver_Work_QueuesEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "srvrqueuesserver-Work-QueuesIndex"),
)
if mibBuilder.loadTexts:
    srvrqueuesserver_Work_QueuesEntry.setStatus("mandatory")
_Srvrqueuesserver_Work_QueuesIndex_Type = Integer32
_Srvrqueuesserver_Work_QueuesIndex_Object = MibScalar
srvrqueuesserver_Work_QueuesIndex = _Srvrqueuesserver_Work_QueuesIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 1),
    _Srvrqueuesserver_Work_QueuesIndex_Type()
)
srvrqueuesserver_Work_QueuesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesserver_Work_QueuesIndex.setStatus("mandatory")
_Srvrqueuesserver_Work_QueuesInstance_Type = DisplayString
_Srvrqueuesserver_Work_QueuesInstance_Object = MibScalar
srvrqueuesserver_Work_QueuesInstance = _Srvrqueuesserver_Work_QueuesInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 2),
    _Srvrqueuesserver_Work_QueuesInstance_Type()
)
srvrqueuesserver_Work_QueuesInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesserver_Work_QueuesInstance.setStatus("mandatory")
_SrvrqueuesQueueLength_Type = Integer32
_SrvrqueuesQueueLength_Object = MibTableColumn
srvrqueuesQueueLength = _SrvrqueuesQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 3),
    _SrvrqueuesQueueLength_Type()
)
srvrqueuesQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesQueueLength.setStatus("mandatory")
_SrvrqueuesActiveThreads_Type = Integer32
_SrvrqueuesActiveThreads_Object = MibTableColumn
srvrqueuesActiveThreads = _SrvrqueuesActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 4),
    _SrvrqueuesActiveThreads_Type()
)
srvrqueuesActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesActiveThreads.setStatus("mandatory")
_SrvrqueuesAvailableThreads_Type = Integer32
_SrvrqueuesAvailableThreads_Object = MibTableColumn
srvrqueuesAvailableThreads = _SrvrqueuesAvailableThreads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 5),
    _SrvrqueuesAvailableThreads_Type()
)
srvrqueuesAvailableThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesAvailableThreads.setStatus("mandatory")
_SrvrqueuesAvailableWorkItems_Type = Integer32
_SrvrqueuesAvailableWorkItems_Object = MibTableColumn
srvrqueuesAvailableWorkItems = _SrvrqueuesAvailableWorkItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 6),
    _SrvrqueuesAvailableWorkItems_Type()
)
srvrqueuesAvailableWorkItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesAvailableWorkItems.setStatus("mandatory")
_SrvrqueuesBorrowedWorkItems_Type = Integer32
_SrvrqueuesBorrowedWorkItems_Object = MibTableColumn
srvrqueuesBorrowedWorkItems = _SrvrqueuesBorrowedWorkItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 7),
    _SrvrqueuesBorrowedWorkItems_Type()
)
srvrqueuesBorrowedWorkItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesBorrowedWorkItems.setStatus("mandatory")
_SrvrqueuesWorkItemShortages_Type = Integer32
_SrvrqueuesWorkItemShortages_Object = MibTableColumn
srvrqueuesWorkItemShortages = _SrvrqueuesWorkItemShortages_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 8),
    _SrvrqueuesWorkItemShortages_Type()
)
srvrqueuesWorkItemShortages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesWorkItemShortages.setStatus("mandatory")
_SrvrqueuesCurrentClients_Type = Integer32
_SrvrqueuesCurrentClients_Object = MibTableColumn
srvrqueuesCurrentClients = _SrvrqueuesCurrentClients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 9),
    _SrvrqueuesCurrentClients_Type()
)
srvrqueuesCurrentClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesCurrentClients.setStatus("mandatory")
_SrvrqueuesBytesReceivedPerSec_Type = Integer32
_SrvrqueuesBytesReceivedPerSec_Object = MibTableColumn
srvrqueuesBytesReceivedPerSec = _SrvrqueuesBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 10),
    _SrvrqueuesBytesReceivedPerSec_Type()
)
srvrqueuesBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesBytesReceivedPerSec.setStatus("mandatory")
_SrvrqueuesBytesSentPerSec_Type = Integer32
_SrvrqueuesBytesSentPerSec_Object = MibTableColumn
srvrqueuesBytesSentPerSec = _SrvrqueuesBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 11),
    _SrvrqueuesBytesSentPerSec_Type()
)
srvrqueuesBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesBytesSentPerSec.setStatus("mandatory")
_SrvrqueuesBytesTransferredPerSec_Type = Integer32
_SrvrqueuesBytesTransferredPerSec_Object = MibTableColumn
srvrqueuesBytesTransferredPerSec = _SrvrqueuesBytesTransferredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 12),
    _SrvrqueuesBytesTransferredPerSec_Type()
)
srvrqueuesBytesTransferredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesBytesTransferredPerSec.setStatus("mandatory")
_SrvrqueuesReadOperationsPerSec_Type = Integer32
_SrvrqueuesReadOperationsPerSec_Object = MibTableColumn
srvrqueuesReadOperationsPerSec = _SrvrqueuesReadOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 13),
    _SrvrqueuesReadOperationsPerSec_Type()
)
srvrqueuesReadOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesReadOperationsPerSec.setStatus("mandatory")
_SrvrqueuesReadBytesPerSec_Type = Integer32
_SrvrqueuesReadBytesPerSec_Object = MibTableColumn
srvrqueuesReadBytesPerSec = _SrvrqueuesReadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 14),
    _SrvrqueuesReadBytesPerSec_Type()
)
srvrqueuesReadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesReadBytesPerSec.setStatus("mandatory")
_SrvrqueuesWriteOperationsPerSec_Type = Integer32
_SrvrqueuesWriteOperationsPerSec_Object = MibTableColumn
srvrqueuesWriteOperationsPerSec = _SrvrqueuesWriteOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 15),
    _SrvrqueuesWriteOperationsPerSec_Type()
)
srvrqueuesWriteOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesWriteOperationsPerSec.setStatus("mandatory")
_SrvrqueuesWriteBytesPerSec_Type = Integer32
_SrvrqueuesWriteBytesPerSec_Object = MibTableColumn
srvrqueuesWriteBytesPerSec = _SrvrqueuesWriteBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 16),
    _SrvrqueuesWriteBytesPerSec_Type()
)
srvrqueuesWriteBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesWriteBytesPerSec.setStatus("mandatory")
_SrvrqueuesTotalBytesPerSec_Type = Integer32
_SrvrqueuesTotalBytesPerSec_Object = MibTableColumn
srvrqueuesTotalBytesPerSec = _SrvrqueuesTotalBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 17),
    _SrvrqueuesTotalBytesPerSec_Type()
)
srvrqueuesTotalBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesTotalBytesPerSec.setStatus("mandatory")
_SrvrqueuesTotalOperationsPerSec_Type = Integer32
_SrvrqueuesTotalOperationsPerSec_Object = MibTableColumn
srvrqueuesTotalOperationsPerSec = _SrvrqueuesTotalOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 18),
    _SrvrqueuesTotalOperationsPerSec_Type()
)
srvrqueuesTotalOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesTotalOperationsPerSec.setStatus("mandatory")
_SrvrqueuesContextBlocksQueuedPerSec_Type = Counter32
_SrvrqueuesContextBlocksQueuedPerSec_Object = MibTableColumn
srvrqueuesContextBlocksQueuedPerSec = _SrvrqueuesContextBlocksQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 18, 1, 19),
    _SrvrqueuesContextBlocksQueuedPerSec_Type()
)
srvrqueuesContextBlocksQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvrqueuesContextBlocksQueuedPerSec.setStatus("mandatory")
_Cache_ObjectIdentity = ObjectIdentity
cache = _Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19)
)
_CacheDataMapsPerSec_Type = Counter32
_CacheDataMapsPerSec_Object = MibScalar
cacheDataMapsPerSec = _CacheDataMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 1),
    _CacheDataMapsPerSec_Type()
)
cacheDataMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDataMapsPerSec.setStatus("mandatory")
_CacheSyncDataMapsPerSec_Type = Counter32
_CacheSyncDataMapsPerSec_Object = MibScalar
cacheSyncDataMapsPerSec = _CacheSyncDataMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 2),
    _CacheSyncDataMapsPerSec_Type()
)
cacheSyncDataMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSyncDataMapsPerSec.setStatus("mandatory")
_CacheAsyncDataMapsPerSec_Type = Counter32
_CacheAsyncDataMapsPerSec_Object = MibScalar
cacheAsyncDataMapsPerSec = _CacheAsyncDataMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 3),
    _CacheAsyncDataMapsPerSec_Type()
)
cacheAsyncDataMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAsyncDataMapsPerSec.setStatus("mandatory")
_CacheDataMapHitsPercent_Type = Integer32
_CacheDataMapHitsPercent_Object = MibScalar
cacheDataMapHitsPercent = _CacheDataMapHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 4),
    _CacheDataMapHitsPercent_Type()
)
cacheDataMapHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDataMapHitsPercent.setStatus("mandatory")
_CacheDataMapPinsPerSec_Type = Integer32
_CacheDataMapPinsPerSec_Object = MibScalar
cacheDataMapPinsPerSec = _CacheDataMapPinsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 6),
    _CacheDataMapPinsPerSec_Type()
)
cacheDataMapPinsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDataMapPinsPerSec.setStatus("mandatory")
_CachePinReadsPerSec_Type = Counter32
_CachePinReadsPerSec_Object = MibScalar
cachePinReadsPerSec = _CachePinReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 8),
    _CachePinReadsPerSec_Type()
)
cachePinReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePinReadsPerSec.setStatus("mandatory")
_CacheSyncPinReadsPerSec_Type = Counter32
_CacheSyncPinReadsPerSec_Object = MibScalar
cacheSyncPinReadsPerSec = _CacheSyncPinReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 9),
    _CacheSyncPinReadsPerSec_Type()
)
cacheSyncPinReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSyncPinReadsPerSec.setStatus("mandatory")
_CacheAsyncPinReadsPerSec_Type = Counter32
_CacheAsyncPinReadsPerSec_Object = MibScalar
cacheAsyncPinReadsPerSec = _CacheAsyncPinReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 10),
    _CacheAsyncPinReadsPerSec_Type()
)
cacheAsyncPinReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAsyncPinReadsPerSec.setStatus("mandatory")
_CachePinReadHitsPercent_Type = Integer32
_CachePinReadHitsPercent_Object = MibScalar
cachePinReadHitsPercent = _CachePinReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 11),
    _CachePinReadHitsPercent_Type()
)
cachePinReadHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePinReadHitsPercent.setStatus("mandatory")
_CacheCopyReadsPerSec_Type = Counter32
_CacheCopyReadsPerSec_Object = MibScalar
cacheCopyReadsPerSec = _CacheCopyReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 13),
    _CacheCopyReadsPerSec_Type()
)
cacheCopyReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCopyReadsPerSec.setStatus("mandatory")
_CacheSyncCopyReadsPerSec_Type = Counter32
_CacheSyncCopyReadsPerSec_Object = MibScalar
cacheSyncCopyReadsPerSec = _CacheSyncCopyReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 14),
    _CacheSyncCopyReadsPerSec_Type()
)
cacheSyncCopyReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSyncCopyReadsPerSec.setStatus("mandatory")
_CacheAsyncCopyReadsPerSec_Type = Counter32
_CacheAsyncCopyReadsPerSec_Object = MibScalar
cacheAsyncCopyReadsPerSec = _CacheAsyncCopyReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 15),
    _CacheAsyncCopyReadsPerSec_Type()
)
cacheAsyncCopyReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAsyncCopyReadsPerSec.setStatus("mandatory")
_CacheCopyReadHitsPercent_Type = Integer32
_CacheCopyReadHitsPercent_Object = MibScalar
cacheCopyReadHitsPercent = _CacheCopyReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 16),
    _CacheCopyReadHitsPercent_Type()
)
cacheCopyReadHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCopyReadHitsPercent.setStatus("mandatory")
_CacheMDLReadsPerSec_Type = Counter32
_CacheMDLReadsPerSec_Object = MibScalar
cacheMDLReadsPerSec = _CacheMDLReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 18),
    _CacheMDLReadsPerSec_Type()
)
cacheMDLReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMDLReadsPerSec.setStatus("mandatory")
_CacheSyncMDLReadsPerSec_Type = Counter32
_CacheSyncMDLReadsPerSec_Object = MibScalar
cacheSyncMDLReadsPerSec = _CacheSyncMDLReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 19),
    _CacheSyncMDLReadsPerSec_Type()
)
cacheSyncMDLReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSyncMDLReadsPerSec.setStatus("mandatory")
_CacheAsyncMDLReadsPerSec_Type = Counter32
_CacheAsyncMDLReadsPerSec_Object = MibScalar
cacheAsyncMDLReadsPerSec = _CacheAsyncMDLReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 20),
    _CacheAsyncMDLReadsPerSec_Type()
)
cacheAsyncMDLReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAsyncMDLReadsPerSec.setStatus("mandatory")
_CacheMDLReadHitsPercent_Type = Integer32
_CacheMDLReadHitsPercent_Object = MibScalar
cacheMDLReadHitsPercent = _CacheMDLReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 21),
    _CacheMDLReadHitsPercent_Type()
)
cacheMDLReadHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMDLReadHitsPercent.setStatus("mandatory")
_CacheReadAheadsPerSec_Type = Counter32
_CacheReadAheadsPerSec_Object = MibScalar
cacheReadAheadsPerSec = _CacheReadAheadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 23),
    _CacheReadAheadsPerSec_Type()
)
cacheReadAheadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheReadAheadsPerSec.setStatus("mandatory")
_CacheFastReadsPerSec_Type = Counter32
_CacheFastReadsPerSec_Object = MibScalar
cacheFastReadsPerSec = _CacheFastReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 24),
    _CacheFastReadsPerSec_Type()
)
cacheFastReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFastReadsPerSec.setStatus("mandatory")
_CacheSyncFastReadsPerSec_Type = Counter32
_CacheSyncFastReadsPerSec_Object = MibScalar
cacheSyncFastReadsPerSec = _CacheSyncFastReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 25),
    _CacheSyncFastReadsPerSec_Type()
)
cacheSyncFastReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSyncFastReadsPerSec.setStatus("mandatory")
_CacheAsyncFastReadsPerSec_Type = Counter32
_CacheAsyncFastReadsPerSec_Object = MibScalar
cacheAsyncFastReadsPerSec = _CacheAsyncFastReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 26),
    _CacheAsyncFastReadsPerSec_Type()
)
cacheAsyncFastReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAsyncFastReadsPerSec.setStatus("mandatory")
_CacheFastReadResourceMissesPerSec_Type = Counter32
_CacheFastReadResourceMissesPerSec_Object = MibScalar
cacheFastReadResourceMissesPerSec = _CacheFastReadResourceMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 27),
    _CacheFastReadResourceMissesPerSec_Type()
)
cacheFastReadResourceMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFastReadResourceMissesPerSec.setStatus("mandatory")
_CacheFastReadNotPossiblesPerSec_Type = Counter32
_CacheFastReadNotPossiblesPerSec_Object = MibScalar
cacheFastReadNotPossiblesPerSec = _CacheFastReadNotPossiblesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 28),
    _CacheFastReadNotPossiblesPerSec_Type()
)
cacheFastReadNotPossiblesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFastReadNotPossiblesPerSec.setStatus("mandatory")
_CacheLazyWriteFlushesPerSec_Type = Counter32
_CacheLazyWriteFlushesPerSec_Object = MibScalar
cacheLazyWriteFlushesPerSec = _CacheLazyWriteFlushesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 29),
    _CacheLazyWriteFlushesPerSec_Type()
)
cacheLazyWriteFlushesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheLazyWriteFlushesPerSec.setStatus("mandatory")
_CacheLazyWritePagesPerSec_Type = Counter32
_CacheLazyWritePagesPerSec_Object = MibScalar
cacheLazyWritePagesPerSec = _CacheLazyWritePagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 30),
    _CacheLazyWritePagesPerSec_Type()
)
cacheLazyWritePagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheLazyWritePagesPerSec.setStatus("mandatory")
_CacheDataFlushesPerSec_Type = Counter32
_CacheDataFlushesPerSec_Object = MibScalar
cacheDataFlushesPerSec = _CacheDataFlushesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 31),
    _CacheDataFlushesPerSec_Type()
)
cacheDataFlushesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDataFlushesPerSec.setStatus("mandatory")
_CacheDataFlushPagesPerSec_Type = Counter32
_CacheDataFlushPagesPerSec_Object = MibScalar
cacheDataFlushPagesPerSec = _CacheDataFlushPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 19, 32),
    _CacheDataFlushPagesPerSec_Type()
)
cacheDataFlushPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDataFlushPagesPerSec.setStatus("mandatory")
_MSExchangeMTA_ObjectIdentity = ObjectIdentity
mSExchangeMTA = _MSExchangeMTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20)
)
_ExchmtaAdjacentMTAAssociations_Type = Integer32
_ExchmtaAdjacentMTAAssociations_Object = MibScalar
exchmtaAdjacentMTAAssociations = _ExchmtaAdjacentMTAAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 1),
    _ExchmtaAdjacentMTAAssociations_Type()
)
exchmtaAdjacentMTAAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaAdjacentMTAAssociations.setStatus("mandatory")
_ExchmtaMessagesPerSec_Type = Counter32
_ExchmtaMessagesPerSec_Object = MibScalar
exchmtaMessagesPerSec = _ExchmtaMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 2),
    _ExchmtaMessagesPerSec_Type()
)
exchmtaMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaMessagesPerSec.setStatus("mandatory")
_ExchmtaMessageBytesPerSec_Type = Counter32
_ExchmtaMessageBytesPerSec_Object = MibScalar
exchmtaMessageBytesPerSec = _ExchmtaMessageBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 3),
    _ExchmtaMessageBytesPerSec_Type()
)
exchmtaMessageBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaMessageBytesPerSec.setStatus("mandatory")
_ExchmtaFreeElements_Type = Integer32
_ExchmtaFreeElements_Object = MibScalar
exchmtaFreeElements = _ExchmtaFreeElements_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 4),
    _ExchmtaFreeElements_Type()
)
exchmtaFreeElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaFreeElements.setStatus("mandatory")
_ExchmtaFreeHeaders_Type = Integer32
_ExchmtaFreeHeaders_Object = MibScalar
exchmtaFreeHeaders = _ExchmtaFreeHeaders_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 5),
    _ExchmtaFreeHeaders_Type()
)
exchmtaFreeHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaFreeHeaders.setStatus("mandatory")
_ExchmtaAdminConnections_Type = Integer32
_ExchmtaAdminConnections_Object = MibScalar
exchmtaAdminConnections = _ExchmtaAdminConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 6),
    _ExchmtaAdminConnections_Type()
)
exchmtaAdminConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaAdminConnections.setStatus("mandatory")
_ExchmtaThreadsInUse_Type = Integer32
_ExchmtaThreadsInUse_Object = MibScalar
exchmtaThreadsInUse = _ExchmtaThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 7),
    _ExchmtaThreadsInUse_Type()
)
exchmtaThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaThreadsInUse.setStatus("mandatory")
_ExchmtaWorkQueueLength_Type = Integer32
_ExchmtaWorkQueueLength_Object = MibScalar
exchmtaWorkQueueLength = _ExchmtaWorkQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 8),
    _ExchmtaWorkQueueLength_Type()
)
exchmtaWorkQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaWorkQueueLength.setStatus("mandatory")
_ExchmtaXAPIGateways_Type = Integer32
_ExchmtaXAPIGateways_Object = MibScalar
exchmtaXAPIGateways = _ExchmtaXAPIGateways_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 9),
    _ExchmtaXAPIGateways_Type()
)
exchmtaXAPIGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaXAPIGateways.setStatus("mandatory")
_ExchmtaXAPIClients_Type = Integer32
_ExchmtaXAPIClients_Object = MibScalar
exchmtaXAPIClients = _ExchmtaXAPIClients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 10),
    _ExchmtaXAPIClients_Type()
)
exchmtaXAPIClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaXAPIClients.setStatus("mandatory")
_ExchmtaDiskFileDeletesPerSec_Type = Counter32
_ExchmtaDiskFileDeletesPerSec_Object = MibScalar
exchmtaDiskFileDeletesPerSec = _ExchmtaDiskFileDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 11),
    _ExchmtaDiskFileDeletesPerSec_Type()
)
exchmtaDiskFileDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDiskFileDeletesPerSec.setStatus("mandatory")
_ExchmtaDiskFileSyncsPerSec_Type = Counter32
_ExchmtaDiskFileSyncsPerSec_Object = MibScalar
exchmtaDiskFileSyncsPerSec = _ExchmtaDiskFileSyncsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 12),
    _ExchmtaDiskFileSyncsPerSec_Type()
)
exchmtaDiskFileSyncsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDiskFileSyncsPerSec.setStatus("mandatory")
_ExchmtaDiskFileOpensPerSec_Type = Counter32
_ExchmtaDiskFileOpensPerSec_Object = MibScalar
exchmtaDiskFileOpensPerSec = _ExchmtaDiskFileOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 13),
    _ExchmtaDiskFileOpensPerSec_Type()
)
exchmtaDiskFileOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDiskFileOpensPerSec.setStatus("mandatory")
_ExchmtaDiskFileReadsPerSec_Type = Counter32
_ExchmtaDiskFileReadsPerSec_Object = MibScalar
exchmtaDiskFileReadsPerSec = _ExchmtaDiskFileReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 14),
    _ExchmtaDiskFileReadsPerSec_Type()
)
exchmtaDiskFileReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDiskFileReadsPerSec.setStatus("mandatory")
_ExchmtaDiskFileWritesPerSec_Type = Counter32
_ExchmtaDiskFileWritesPerSec_Object = MibScalar
exchmtaDiskFileWritesPerSec = _ExchmtaDiskFileWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 15),
    _ExchmtaDiskFileWritesPerSec_Type()
)
exchmtaDiskFileWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDiskFileWritesPerSec.setStatus("mandatory")
_ExchmtaExDSReadCallsPerSec_Type = Counter32
_ExchmtaExDSReadCallsPerSec_Object = MibScalar
exchmtaExDSReadCallsPerSec = _ExchmtaExDSReadCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 16),
    _ExchmtaExDSReadCallsPerSec_Type()
)
exchmtaExDSReadCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaExDSReadCallsPerSec.setStatus("mandatory")
_ExchmtaXAPIReceiveBytesPerSec_Type = Counter32
_ExchmtaXAPIReceiveBytesPerSec_Object = MibScalar
exchmtaXAPIReceiveBytesPerSec = _ExchmtaXAPIReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 17),
    _ExchmtaXAPIReceiveBytesPerSec_Type()
)
exchmtaXAPIReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaXAPIReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaXAPITransmitBytesPerSec_Type = Counter32
_ExchmtaXAPITransmitBytesPerSec_Object = MibScalar
exchmtaXAPITransmitBytesPerSec = _ExchmtaXAPITransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 18),
    _ExchmtaXAPITransmitBytesPerSec_Type()
)
exchmtaXAPITransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaXAPITransmitBytesPerSec.setStatus("mandatory")
_ExchmtaAdminInterfaceReceiveBytesPerSec_Type = Counter32
_ExchmtaAdminInterfaceReceiveBytesPerSec_Object = MibScalar
exchmtaAdminInterfaceReceiveBytesPerSec = _ExchmtaAdminInterfaceReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 19),
    _ExchmtaAdminInterfaceReceiveBytesPerSec_Type()
)
exchmtaAdminInterfaceReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaAdminInterfaceReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaAdminInterfaceTransmitBytesPerSec_Type = Counter32
_ExchmtaAdminInterfaceTransmitBytesPerSec_Object = MibScalar
exchmtaAdminInterfaceTransmitBytesPerSec = _ExchmtaAdminInterfaceTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 20),
    _ExchmtaAdminInterfaceTransmitBytesPerSec_Type()
)
exchmtaAdminInterfaceTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaAdminInterfaceTransmitBytesPerSec.setStatus("mandatory")
_ExchmtaLANReceiveBytesPerSec_Type = Counter32
_ExchmtaLANReceiveBytesPerSec_Object = MibScalar
exchmtaLANReceiveBytesPerSec = _ExchmtaLANReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 21),
    _ExchmtaLANReceiveBytesPerSec_Type()
)
exchmtaLANReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaLANReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaLANTransmitBytesPerSec_Type = Counter32
_ExchmtaLANTransmitBytesPerSec_Object = MibScalar
exchmtaLANTransmitBytesPerSec = _ExchmtaLANTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 22),
    _ExchmtaLANTransmitBytesPerSec_Type()
)
exchmtaLANTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaLANTransmitBytesPerSec.setStatus("mandatory")
_ExchmtaRASReceiveBytesPerSec_Type = Counter32
_ExchmtaRASReceiveBytesPerSec_Object = MibScalar
exchmtaRASReceiveBytesPerSec = _ExchmtaRASReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 23),
    _ExchmtaRASReceiveBytesPerSec_Type()
)
exchmtaRASReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaRASReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaRASTransmitBytesPerSec_Type = Counter32
_ExchmtaRASTransmitBytesPerSec_Object = MibScalar
exchmtaRASTransmitBytesPerSec = _ExchmtaRASTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 24),
    _ExchmtaRASTransmitBytesPerSec_Type()
)
exchmtaRASTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaRASTransmitBytesPerSec.setStatus("mandatory")
_ExchmtaTCPPerIPReceiveBytesPerSec_Type = Counter32
_ExchmtaTCPPerIPReceiveBytesPerSec_Object = MibScalar
exchmtaTCPPerIPReceiveBytesPerSec = _ExchmtaTCPPerIPReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 25),
    _ExchmtaTCPPerIPReceiveBytesPerSec_Type()
)
exchmtaTCPPerIPReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTCPPerIPReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaTCPPerIPTransmitBytesPerSec_Type = Counter32
_ExchmtaTCPPerIPTransmitBytesPerSec_Object = MibScalar
exchmtaTCPPerIPTransmitBytesPerSec = _ExchmtaTCPPerIPTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 26),
    _ExchmtaTCPPerIPTransmitBytesPerSec_Type()
)
exchmtaTCPPerIPTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTCPPerIPTransmitBytesPerSec.setStatus("mandatory")
_ExchmtaTP4ReceiveBytesPerSec_Type = Counter32
_ExchmtaTP4ReceiveBytesPerSec_Object = MibScalar
exchmtaTP4ReceiveBytesPerSec = _ExchmtaTP4ReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 27),
    _ExchmtaTP4ReceiveBytesPerSec_Type()
)
exchmtaTP4ReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTP4ReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaTP4TransmitBytesPerSec_Type = Counter32
_ExchmtaTP4TransmitBytesPerSec_Object = MibScalar
exchmtaTP4TransmitBytesPerSec = _ExchmtaTP4TransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 28),
    _ExchmtaTP4TransmitBytesPerSec_Type()
)
exchmtaTP4TransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTP4TransmitBytesPerSec.setStatus("mandatory")
_ExchmtaX25ReceiveBytesPerSec_Type = Counter32
_ExchmtaX25ReceiveBytesPerSec_Object = MibScalar
exchmtaX25ReceiveBytesPerSec = _ExchmtaX25ReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 29),
    _ExchmtaX25ReceiveBytesPerSec_Type()
)
exchmtaX25ReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaX25ReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaX25TransmitBytesPerSec_Type = Counter32
_ExchmtaX25TransmitBytesPerSec_Object = MibScalar
exchmtaX25TransmitBytesPerSec = _ExchmtaX25TransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 30),
    _ExchmtaX25TransmitBytesPerSec_Type()
)
exchmtaX25TransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaX25TransmitBytesPerSec.setStatus("mandatory")
_ExchmtaDeferredDeliveryMsgs_Type = Integer32
_ExchmtaDeferredDeliveryMsgs_Object = MibScalar
exchmtaDeferredDeliveryMsgs = _ExchmtaDeferredDeliveryMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 31),
    _ExchmtaDeferredDeliveryMsgs_Type()
)
exchmtaDeferredDeliveryMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaDeferredDeliveryMsgs.setStatus("mandatory")
_ExchmtaTotalRecipientsQueued_Type = Integer32
_ExchmtaTotalRecipientsQueued_Object = MibScalar
exchmtaTotalRecipientsQueued = _ExchmtaTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 32),
    _ExchmtaTotalRecipientsQueued_Type()
)
exchmtaTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalRecipientsQueued.setStatus("mandatory")
_ExchmtaTotalSuccessfulConversions_Type = Integer32
_ExchmtaTotalSuccessfulConversions_Object = MibScalar
exchmtaTotalSuccessfulConversions = _ExchmtaTotalSuccessfulConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 33),
    _ExchmtaTotalSuccessfulConversions_Type()
)
exchmtaTotalSuccessfulConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalSuccessfulConversions.setStatus("mandatory")
_ExchmtaTotalFailedConversions_Type = Integer32
_ExchmtaTotalFailedConversions_Object = MibScalar
exchmtaTotalFailedConversions = _ExchmtaTotalFailedConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 34),
    _ExchmtaTotalFailedConversions_Type()
)
exchmtaTotalFailedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalFailedConversions.setStatus("mandatory")
_ExchmtaTotalLoopsDetected_Type = Integer32
_ExchmtaTotalLoopsDetected_Object = MibScalar
exchmtaTotalLoopsDetected = _ExchmtaTotalLoopsDetected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 35),
    _ExchmtaTotalLoopsDetected_Type()
)
exchmtaTotalLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalLoopsDetected.setStatus("mandatory")
_ExchmtaInboundMessagesTotal_Type = Counter32
_ExchmtaInboundMessagesTotal_Object = MibScalar
exchmtaInboundMessagesTotal = _ExchmtaInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 36),
    _ExchmtaInboundMessagesTotal_Type()
)
exchmtaInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaInboundMessagesTotal.setStatus("mandatory")
_ExchmtaOutboundMessagesTotal_Type = Counter32
_ExchmtaOutboundMessagesTotal_Object = MibScalar
exchmtaOutboundMessagesTotal = _ExchmtaOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 37),
    _ExchmtaOutboundMessagesTotal_Type()
)
exchmtaOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaOutboundMessagesTotal.setStatus("mandatory")
_ExchmtaInboundBytesTotal_Type = Counter32
_ExchmtaInboundBytesTotal_Object = MibScalar
exchmtaInboundBytesTotal = _ExchmtaInboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 38),
    _ExchmtaInboundBytesTotal_Type()
)
exchmtaInboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaInboundBytesTotal.setStatus("mandatory")
_ExchmtaWorkQueueBytes_Type = Counter32
_ExchmtaWorkQueueBytes_Object = MibScalar
exchmtaWorkQueueBytes = _ExchmtaWorkQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 39),
    _ExchmtaWorkQueueBytes_Type()
)
exchmtaWorkQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaWorkQueueBytes.setStatus("mandatory")
_ExchmtaOutboundBytesTotal_Type = Counter32
_ExchmtaOutboundBytesTotal_Object = MibScalar
exchmtaOutboundBytesTotal = _ExchmtaOutboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 40),
    _ExchmtaOutboundBytesTotal_Type()
)
exchmtaOutboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaOutboundBytesTotal.setStatus("mandatory")
_ExchmtaTotalRecipientsInbound_Type = Counter32
_ExchmtaTotalRecipientsInbound_Object = MibScalar
exchmtaTotalRecipientsInbound = _ExchmtaTotalRecipientsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 41),
    _ExchmtaTotalRecipientsInbound_Type()
)
exchmtaTotalRecipientsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalRecipientsInbound.setStatus("mandatory")
_ExchmtaTotalRecipientsOutbound_Type = Counter32
_ExchmtaTotalRecipientsOutbound_Object = MibScalar
exchmtaTotalRecipientsOutbound = _ExchmtaTotalRecipientsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 20, 42),
    _ExchmtaTotalRecipientsOutbound_Type()
)
exchmtaTotalRecipientsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaTotalRecipientsOutbound.setStatus("mandatory")
_ExchmtaconnmSExchangeMTA_ConnectionsTable_Object = MibTable
exchmtaconnmSExchangeMTA_ConnectionsTable = _ExchmtaconnmSExchangeMTA_ConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21)
)
if mibBuilder.loadTexts:
    exchmtaconnmSExchangeMTA_ConnectionsTable.setStatus("mandatory")
_ExchmtaconnmSExchangeMTA_ConnectionsEntry_Object = MibTableRow
exchmtaconnmSExchangeMTA_ConnectionsEntry = _ExchmtaconnmSExchangeMTA_ConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1)
)
exchmtaconnmSExchangeMTA_ConnectionsEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "exchmtaconnmSExchangeMTA-ConnectionsIndex"),
)
if mibBuilder.loadTexts:
    exchmtaconnmSExchangeMTA_ConnectionsEntry.setStatus("mandatory")
_ExchmtaconnmSExchangeMTA_ConnectionsIndex_Type = Integer32
_ExchmtaconnmSExchangeMTA_ConnectionsIndex_Object = MibScalar
exchmtaconnmSExchangeMTA_ConnectionsIndex = _ExchmtaconnmSExchangeMTA_ConnectionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 1),
    _ExchmtaconnmSExchangeMTA_ConnectionsIndex_Type()
)
exchmtaconnmSExchangeMTA_ConnectionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnmSExchangeMTA_ConnectionsIndex.setStatus("mandatory")
_ExchmtaconnmSExchangeMTA_ConnectionsInstance_Type = DisplayString
_ExchmtaconnmSExchangeMTA_ConnectionsInstance_Object = MibScalar
exchmtaconnmSExchangeMTA_ConnectionsInstance = _ExchmtaconnmSExchangeMTA_ConnectionsInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 2),
    _ExchmtaconnmSExchangeMTA_ConnectionsInstance_Type()
)
exchmtaconnmSExchangeMTA_ConnectionsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnmSExchangeMTA_ConnectionsInstance.setStatus("mandatory")
_ExchmtaconnAssociations_Type = Integer32
_ExchmtaconnAssociations_Object = MibTableColumn
exchmtaconnAssociations = _ExchmtaconnAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 3),
    _ExchmtaconnAssociations_Type()
)
exchmtaconnAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnAssociations.setStatus("mandatory")
_ExchmtaconnReceiveBytesPerSec_Type = Counter32
_ExchmtaconnReceiveBytesPerSec_Object = MibTableColumn
exchmtaconnReceiveBytesPerSec = _ExchmtaconnReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 4),
    _ExchmtaconnReceiveBytesPerSec_Type()
)
exchmtaconnReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnReceiveBytesPerSec.setStatus("mandatory")
_ExchmtaconnSendBytesPerSec_Type = Counter32
_ExchmtaconnSendBytesPerSec_Object = MibTableColumn
exchmtaconnSendBytesPerSec = _ExchmtaconnSendBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 5),
    _ExchmtaconnSendBytesPerSec_Type()
)
exchmtaconnSendBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnSendBytesPerSec.setStatus("mandatory")
_ExchmtaconnReceiveMessagesPerSec_Type = Counter32
_ExchmtaconnReceiveMessagesPerSec_Object = MibTableColumn
exchmtaconnReceiveMessagesPerSec = _ExchmtaconnReceiveMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 6),
    _ExchmtaconnReceiveMessagesPerSec_Type()
)
exchmtaconnReceiveMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnReceiveMessagesPerSec.setStatus("mandatory")
_ExchmtaconnSendMessagesPerSec_Type = Counter32
_ExchmtaconnSendMessagesPerSec_Object = MibTableColumn
exchmtaconnSendMessagesPerSec = _ExchmtaconnSendMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 7),
    _ExchmtaconnSendMessagesPerSec_Type()
)
exchmtaconnSendMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnSendMessagesPerSec.setStatus("mandatory")
_ExchmtaconnQueueLength_Type = Integer32
_ExchmtaconnQueueLength_Object = MibTableColumn
exchmtaconnQueueLength = _ExchmtaconnQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 8),
    _ExchmtaconnQueueLength_Type()
)
exchmtaconnQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnQueueLength.setStatus("mandatory")
_ExchmtaconnConnectorIndex_Type = Integer32
_ExchmtaconnConnectorIndex_Object = MibTableColumn
exchmtaconnConnectorIndex = _ExchmtaconnConnectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 9),
    _ExchmtaconnConnectorIndex_Type()
)
exchmtaconnConnectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnConnectorIndex.setStatus("mandatory")
_ExchmtaconnInboundRejectedTotal_Type = Integer32
_ExchmtaconnInboundRejectedTotal_Object = MibTableColumn
exchmtaconnInboundRejectedTotal = _ExchmtaconnInboundRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 10),
    _ExchmtaconnInboundRejectedTotal_Type()
)
exchmtaconnInboundRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnInboundRejectedTotal.setStatus("mandatory")
_ExchmtaconnTotalRecipientsQueued_Type = Integer32
_ExchmtaconnTotalRecipientsQueued_Object = MibTableColumn
exchmtaconnTotalRecipientsQueued = _ExchmtaconnTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 11),
    _ExchmtaconnTotalRecipientsQueued_Type()
)
exchmtaconnTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnTotalRecipientsQueued.setStatus("mandatory")
_ExchmtaconnOldestMessageQueued_Type = TimeTicks
_ExchmtaconnOldestMessageQueued_Object = MibTableColumn
exchmtaconnOldestMessageQueued = _ExchmtaconnOldestMessageQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 12),
    _ExchmtaconnOldestMessageQueued_Type()
)
exchmtaconnOldestMessageQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnOldestMessageQueued.setStatus("mandatory")
_ExchmtaconnCurrentInboundAssociations_Type = Integer32
_ExchmtaconnCurrentInboundAssociations_Object = MibTableColumn
exchmtaconnCurrentInboundAssociations = _ExchmtaconnCurrentInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 13),
    _ExchmtaconnCurrentInboundAssociations_Type()
)
exchmtaconnCurrentInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnCurrentInboundAssociations.setStatus("mandatory")
_ExchmtaconnCurrentOutboundAssociations_Type = Integer32
_ExchmtaconnCurrentOutboundAssociations_Object = MibTableColumn
exchmtaconnCurrentOutboundAssociations = _ExchmtaconnCurrentOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 14),
    _ExchmtaconnCurrentOutboundAssociations_Type()
)
exchmtaconnCurrentOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnCurrentOutboundAssociations.setStatus("mandatory")
_ExchmtaconnCumulativeInboundAssociations_Type = Integer32
_ExchmtaconnCumulativeInboundAssociations_Object = MibTableColumn
exchmtaconnCumulativeInboundAssociations = _ExchmtaconnCumulativeInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 15),
    _ExchmtaconnCumulativeInboundAssociations_Type()
)
exchmtaconnCumulativeInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnCumulativeInboundAssociations.setStatus("mandatory")
_ExchmtaconnCumulativeOutboundAssociations_Type = Integer32
_ExchmtaconnCumulativeOutboundAssociations_Object = MibTableColumn
exchmtaconnCumulativeOutboundAssociations = _ExchmtaconnCumulativeOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 16),
    _ExchmtaconnCumulativeOutboundAssociations_Type()
)
exchmtaconnCumulativeOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnCumulativeOutboundAssociations.setStatus("mandatory")
_ExchmtaconnLastInboundAssociation_Type = TimeTicks
_ExchmtaconnLastInboundAssociation_Object = MibTableColumn
exchmtaconnLastInboundAssociation = _ExchmtaconnLastInboundAssociation_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 17),
    _ExchmtaconnLastInboundAssociation_Type()
)
exchmtaconnLastInboundAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnLastInboundAssociation.setStatus("mandatory")
_ExchmtaconnLastOutboundAssociation_Type = TimeTicks
_ExchmtaconnLastOutboundAssociation_Object = MibTableColumn
exchmtaconnLastOutboundAssociation = _ExchmtaconnLastOutboundAssociation_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 18),
    _ExchmtaconnLastOutboundAssociation_Type()
)
exchmtaconnLastOutboundAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnLastOutboundAssociation.setStatus("mandatory")
_ExchmtaconnRejectedInboundAssociations_Type = Integer32
_ExchmtaconnRejectedInboundAssociations_Object = MibTableColumn
exchmtaconnRejectedInboundAssociations = _ExchmtaconnRejectedInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 19),
    _ExchmtaconnRejectedInboundAssociations_Type()
)
exchmtaconnRejectedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnRejectedInboundAssociations.setStatus("mandatory")
_ExchmtaconnFailedOutboundAssociations_Type = Integer32
_ExchmtaconnFailedOutboundAssociations_Object = MibTableColumn
exchmtaconnFailedOutboundAssociations = _ExchmtaconnFailedOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 20),
    _ExchmtaconnFailedOutboundAssociations_Type()
)
exchmtaconnFailedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnFailedOutboundAssociations.setStatus("mandatory")
_ExchmtaconnNextAssociationRetry_Type = Integer32
_ExchmtaconnNextAssociationRetry_Object = MibTableColumn
exchmtaconnNextAssociationRetry = _ExchmtaconnNextAssociationRetry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 21),
    _ExchmtaconnNextAssociationRetry_Type()
)
exchmtaconnNextAssociationRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnNextAssociationRetry.setStatus("mandatory")
_ExchmtaconnInboundRejectReason_Type = Integer32
_ExchmtaconnInboundRejectReason_Object = MibTableColumn
exchmtaconnInboundRejectReason = _ExchmtaconnInboundRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 22),
    _ExchmtaconnInboundRejectReason_Type()
)
exchmtaconnInboundRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnInboundRejectReason.setStatus("mandatory")
_ExchmtaconnOutboundFailureReason_Type = Integer32
_ExchmtaconnOutboundFailureReason_Object = MibTableColumn
exchmtaconnOutboundFailureReason = _ExchmtaconnOutboundFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 23),
    _ExchmtaconnOutboundFailureReason_Type()
)
exchmtaconnOutboundFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnOutboundFailureReason.setStatus("mandatory")
_ExchmtaconnInboundMessagesTotal_Type = Counter32
_ExchmtaconnInboundMessagesTotal_Object = MibTableColumn
exchmtaconnInboundMessagesTotal = _ExchmtaconnInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 24),
    _ExchmtaconnInboundMessagesTotal_Type()
)
exchmtaconnInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnInboundMessagesTotal.setStatus("mandatory")
_ExchmtaconnOutboundMessagesTotal_Type = Counter32
_ExchmtaconnOutboundMessagesTotal_Object = MibTableColumn
exchmtaconnOutboundMessagesTotal = _ExchmtaconnOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 25),
    _ExchmtaconnOutboundMessagesTotal_Type()
)
exchmtaconnOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnOutboundMessagesTotal.setStatus("mandatory")
_ExchmtaconnInboundBytesTotal_Type = Counter32
_ExchmtaconnInboundBytesTotal_Object = MibTableColumn
exchmtaconnInboundBytesTotal = _ExchmtaconnInboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 26),
    _ExchmtaconnInboundBytesTotal_Type()
)
exchmtaconnInboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnInboundBytesTotal.setStatus("mandatory")
_ExchmtaconnQueuedBytes_Type = Counter32
_ExchmtaconnQueuedBytes_Object = MibTableColumn
exchmtaconnQueuedBytes = _ExchmtaconnQueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 27),
    _ExchmtaconnQueuedBytes_Type()
)
exchmtaconnQueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnQueuedBytes.setStatus("mandatory")
_ExchmtaconnOutboundBytesTotal_Type = Counter32
_ExchmtaconnOutboundBytesTotal_Object = MibTableColumn
exchmtaconnOutboundBytesTotal = _ExchmtaconnOutboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 28),
    _ExchmtaconnOutboundBytesTotal_Type()
)
exchmtaconnOutboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnOutboundBytesTotal.setStatus("mandatory")
_ExchmtaconnTotalRecipientsInbound_Type = Counter32
_ExchmtaconnTotalRecipientsInbound_Object = MibTableColumn
exchmtaconnTotalRecipientsInbound = _ExchmtaconnTotalRecipientsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 29),
    _ExchmtaconnTotalRecipientsInbound_Type()
)
exchmtaconnTotalRecipientsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnTotalRecipientsInbound.setStatus("mandatory")
_ExchmtaconnTotalRecipientsOutbound_Type = Counter32
_ExchmtaconnTotalRecipientsOutbound_Object = MibTableColumn
exchmtaconnTotalRecipientsOutbound = _ExchmtaconnTotalRecipientsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 21, 1, 30),
    _ExchmtaconnTotalRecipientsOutbound_Type()
)
exchmtaconnTotalRecipientsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchmtaconnTotalRecipientsOutbound.setStatus("mandatory")
_MSExchangeIMC_ObjectIdentity = ObjectIdentity
mSExchangeIMC = _MSExchangeIMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22)
)
_ExchimcQueuedMTS_IN_Type = Integer32
_ExchimcQueuedMTS_IN_Object = MibScalar
exchimcQueuedMTS_IN = _ExchimcQueuedMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 1),
    _ExchimcQueuedMTS_IN_Type()
)
exchimcQueuedMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcQueuedMTS_IN.setStatus("mandatory")
_ExchimcBytesQueuedMTS_IN_Type = Integer32
_ExchimcBytesQueuedMTS_IN_Object = MibScalar
exchimcBytesQueuedMTS_IN = _ExchimcBytesQueuedMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 2),
    _ExchimcBytesQueuedMTS_IN_Type()
)
exchimcBytesQueuedMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcBytesQueuedMTS_IN.setStatus("mandatory")
_ExchimcMessagesEnteringMTS_IN_Type = Integer32
_ExchimcMessagesEnteringMTS_IN_Object = MibScalar
exchimcMessagesEnteringMTS_IN = _ExchimcMessagesEnteringMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 3),
    _ExchimcMessagesEnteringMTS_IN_Type()
)
exchimcMessagesEnteringMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcMessagesEnteringMTS_IN.setStatus("mandatory")
_ExchimcQueuedMTS_OUT_Type = Integer32
_ExchimcQueuedMTS_OUT_Object = MibScalar
exchimcQueuedMTS_OUT = _ExchimcQueuedMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 4),
    _ExchimcQueuedMTS_OUT_Type()
)
exchimcQueuedMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcQueuedMTS_OUT.setStatus("mandatory")
_ExchimcBytesQueuedMTS_OUT_Type = Integer32
_ExchimcBytesQueuedMTS_OUT_Object = MibScalar
exchimcBytesQueuedMTS_OUT = _ExchimcBytesQueuedMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 5),
    _ExchimcBytesQueuedMTS_OUT_Type()
)
exchimcBytesQueuedMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcBytesQueuedMTS_OUT.setStatus("mandatory")
_ExchimcMessagesEnteringMTS_OUT_Type = Integer32
_ExchimcMessagesEnteringMTS_OUT_Object = MibScalar
exchimcMessagesEnteringMTS_OUT = _ExchimcMessagesEnteringMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 6),
    _ExchimcMessagesEnteringMTS_OUT_Type()
)
exchimcMessagesEnteringMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcMessagesEnteringMTS_OUT.setStatus("mandatory")
_ExchimcMessagesLeavingMTS_OUT_Type = Integer32
_ExchimcMessagesLeavingMTS_OUT_Object = MibScalar
exchimcMessagesLeavingMTS_OUT = _ExchimcMessagesLeavingMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 7),
    _ExchimcMessagesLeavingMTS_OUT_Type()
)
exchimcMessagesLeavingMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcMessagesLeavingMTS_OUT.setStatus("mandatory")
_ExchimcConnectionsInbound_Type = Integer32
_ExchimcConnectionsInbound_Object = MibScalar
exchimcConnectionsInbound = _ExchimcConnectionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 8),
    _ExchimcConnectionsInbound_Type()
)
exchimcConnectionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsInbound.setStatus("mandatory")
_ExchimcConnectionsOutbound_Type = Integer32
_ExchimcConnectionsOutbound_Object = MibScalar
exchimcConnectionsOutbound = _ExchimcConnectionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 9),
    _ExchimcConnectionsOutbound_Type()
)
exchimcConnectionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsOutbound.setStatus("mandatory")
_ExchimcConnectionsTotalOutbound_Type = Integer32
_ExchimcConnectionsTotalOutbound_Object = MibScalar
exchimcConnectionsTotalOutbound = _ExchimcConnectionsTotalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 10),
    _ExchimcConnectionsTotalOutbound_Type()
)
exchimcConnectionsTotalOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsTotalOutbound.setStatus("mandatory")
_ExchimcConnectionsTotalInbound_Type = Integer32
_ExchimcConnectionsTotalInbound_Object = MibScalar
exchimcConnectionsTotalInbound = _ExchimcConnectionsTotalInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 11),
    _ExchimcConnectionsTotalInbound_Type()
)
exchimcConnectionsTotalInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsTotalInbound.setStatus("mandatory")
_ExchimcConnectionsTotalRejected_Type = Integer32
_ExchimcConnectionsTotalRejected_Object = MibScalar
exchimcConnectionsTotalRejected = _ExchimcConnectionsTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 12),
    _ExchimcConnectionsTotalRejected_Type()
)
exchimcConnectionsTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsTotalRejected.setStatus("mandatory")
_ExchimcConnectionsTotalFailed_Type = Integer32
_ExchimcConnectionsTotalFailed_Object = MibScalar
exchimcConnectionsTotalFailed = _ExchimcConnectionsTotalFailed_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 13),
    _ExchimcConnectionsTotalFailed_Type()
)
exchimcConnectionsTotalFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcConnectionsTotalFailed.setStatus("mandatory")
_ExchimcQueuedOutbound_Type = Integer32
_ExchimcQueuedOutbound_Object = MibScalar
exchimcQueuedOutbound = _ExchimcQueuedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 14),
    _ExchimcQueuedOutbound_Type()
)
exchimcQueuedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcQueuedOutbound.setStatus("mandatory")
_ExchimcQueuedInbound_Type = Integer32
_ExchimcQueuedInbound_Object = MibScalar
exchimcQueuedInbound = _ExchimcQueuedInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 15),
    _ExchimcQueuedInbound_Type()
)
exchimcQueuedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcQueuedInbound.setStatus("mandatory")
_ExchimcNDRsTotalInbound_Type = Integer32
_ExchimcNDRsTotalInbound_Object = MibScalar
exchimcNDRsTotalInbound = _ExchimcNDRsTotalInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 16),
    _ExchimcNDRsTotalInbound_Type()
)
exchimcNDRsTotalInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcNDRsTotalInbound.setStatus("mandatory")
_ExchimcNDRsTotalOutbound_Type = Integer32
_ExchimcNDRsTotalOutbound_Object = MibScalar
exchimcNDRsTotalOutbound = _ExchimcNDRsTotalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 17),
    _ExchimcNDRsTotalOutbound_Type()
)
exchimcNDRsTotalOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcNDRsTotalOutbound.setStatus("mandatory")
_ExchimcTotalInboundKilobytes_Type = Integer32
_ExchimcTotalInboundKilobytes_Object = MibScalar
exchimcTotalInboundKilobytes = _ExchimcTotalInboundKilobytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 18),
    _ExchimcTotalInboundKilobytes_Type()
)
exchimcTotalInboundKilobytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalInboundKilobytes.setStatus("mandatory")
_ExchimcTotalOutboundKilobytes_Type = Integer32
_ExchimcTotalOutboundKilobytes_Object = MibScalar
exchimcTotalOutboundKilobytes = _ExchimcTotalOutboundKilobytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 19),
    _ExchimcTotalOutboundKilobytes_Type()
)
exchimcTotalOutboundKilobytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalOutboundKilobytes.setStatus("mandatory")
_ExchimcInboundMessagesTotal_Type = Integer32
_ExchimcInboundMessagesTotal_Object = MibScalar
exchimcInboundMessagesTotal = _ExchimcInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 20),
    _ExchimcInboundMessagesTotal_Type()
)
exchimcInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcInboundMessagesTotal.setStatus("mandatory")
_ExchimcOutboundMessagesTotal_Type = Integer32
_ExchimcOutboundMessagesTotal_Object = MibScalar
exchimcOutboundMessagesTotal = _ExchimcOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 21),
    _ExchimcOutboundMessagesTotal_Type()
)
exchimcOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcOutboundMessagesTotal.setStatus("mandatory")
_ExchimcInboundBytesPerHr_Type = Integer32
_ExchimcInboundBytesPerHr_Object = MibScalar
exchimcInboundBytesPerHr = _ExchimcInboundBytesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 22),
    _ExchimcInboundBytesPerHr_Type()
)
exchimcInboundBytesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcInboundBytesPerHr.setStatus("mandatory")
_ExchimcOutboundBytesPerHr_Type = Integer32
_ExchimcOutboundBytesPerHr_Object = MibScalar
exchimcOutboundBytesPerHr = _ExchimcOutboundBytesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 23),
    _ExchimcOutboundBytesPerHr_Type()
)
exchimcOutboundBytesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcOutboundBytesPerHr.setStatus("mandatory")
_ExchimcInboundMessagesPerHr_Type = Integer32
_ExchimcInboundMessagesPerHr_Object = MibScalar
exchimcInboundMessagesPerHr = _ExchimcInboundMessagesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 24),
    _ExchimcInboundMessagesPerHr_Type()
)
exchimcInboundMessagesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcInboundMessagesPerHr.setStatus("mandatory")
_ExchimcOutboundMessagesPerHr_Type = Integer32
_ExchimcOutboundMessagesPerHr_Object = MibScalar
exchimcOutboundMessagesPerHr = _ExchimcOutboundMessagesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 25),
    _ExchimcOutboundMessagesPerHr_Type()
)
exchimcOutboundMessagesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcOutboundMessagesPerHr.setStatus("mandatory")
_ExchimcOutboundConnectionsPerHr_Type = Integer32
_ExchimcOutboundConnectionsPerHr_Object = MibScalar
exchimcOutboundConnectionsPerHr = _ExchimcOutboundConnectionsPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 26),
    _ExchimcOutboundConnectionsPerHr_Type()
)
exchimcOutboundConnectionsPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcOutboundConnectionsPerHr.setStatus("mandatory")
_ExchimcInboundConnectionsPerHr_Type = Integer32
_ExchimcInboundConnectionsPerHr_Object = MibScalar
exchimcInboundConnectionsPerHr = _ExchimcInboundConnectionsPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 27),
    _ExchimcInboundConnectionsPerHr_Type()
)
exchimcInboundConnectionsPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcInboundConnectionsPerHr.setStatus("mandatory")
_ExchimcTotalMessagesQueued_Type = Integer32
_ExchimcTotalMessagesQueued_Object = MibScalar
exchimcTotalMessagesQueued = _ExchimcTotalMessagesQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 28),
    _ExchimcTotalMessagesQueued_Type()
)
exchimcTotalMessagesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalMessagesQueued.setStatus("mandatory")
_ExchimcTotalKilobytesQueued_Type = Integer32
_ExchimcTotalKilobytesQueued_Object = MibScalar
exchimcTotalKilobytesQueued = _ExchimcTotalKilobytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 29),
    _ExchimcTotalKilobytesQueued_Type()
)
exchimcTotalKilobytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalKilobytesQueued.setStatus("mandatory")
_ExchimcTotalInboundRecipients_Type = Integer32
_ExchimcTotalInboundRecipients_Object = MibScalar
exchimcTotalInboundRecipients = _ExchimcTotalInboundRecipients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 30),
    _ExchimcTotalInboundRecipients_Type()
)
exchimcTotalInboundRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalInboundRecipients.setStatus("mandatory")
_ExchimcTotalOutboundRecipients_Type = Integer32
_ExchimcTotalOutboundRecipients_Object = MibScalar
exchimcTotalOutboundRecipients = _ExchimcTotalOutboundRecipients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 31),
    _ExchimcTotalOutboundRecipients_Type()
)
exchimcTotalOutboundRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalOutboundRecipients.setStatus("mandatory")
_ExchimcTotalRecipientsQueued_Type = Integer32
_ExchimcTotalRecipientsQueued_Object = MibScalar
exchimcTotalRecipientsQueued = _ExchimcTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 32),
    _ExchimcTotalRecipientsQueued_Type()
)
exchimcTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalRecipientsQueued.setStatus("mandatory")
_ExchimcTotalSuccessfulConversions_Type = Integer32
_ExchimcTotalSuccessfulConversions_Object = MibScalar
exchimcTotalSuccessfulConversions = _ExchimcTotalSuccessfulConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 33),
    _ExchimcTotalSuccessfulConversions_Type()
)
exchimcTotalSuccessfulConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalSuccessfulConversions.setStatus("mandatory")
_ExchimcTotalFailedConversions_Type = Integer32
_ExchimcTotalFailedConversions_Object = MibScalar
exchimcTotalFailedConversions = _ExchimcTotalFailedConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 34),
    _ExchimcTotalFailedConversions_Type()
)
exchimcTotalFailedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalFailedConversions.setStatus("mandatory")
_ExchimcTotalLoopsDetected_Type = Integer32
_ExchimcTotalLoopsDetected_Object = MibScalar
exchimcTotalLoopsDetected = _ExchimcTotalLoopsDetected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 22, 35),
    _ExchimcTotalLoopsDetected_Type()
)
exchimcTotalLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchimcTotalLoopsDetected.setStatus("mandatory")
_MSExchangeIS_ObjectIdentity = ObjectIdentity
mSExchangeIS = _MSExchangeIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23)
)
_ExchisRPCPacketsPerSec_Type = Counter32
_ExchisRPCPacketsPerSec_Object = MibScalar
exchisRPCPacketsPerSec = _ExchisRPCPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 1),
    _ExchisRPCPacketsPerSec_Type()
)
exchisRPCPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisRPCPacketsPerSec.setStatus("mandatory")
_ExchisRPCOperationsPerSec_Type = Counter32
_ExchisRPCOperationsPerSec_Object = MibScalar
exchisRPCOperationsPerSec = _ExchisRPCOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 2),
    _ExchisRPCOperationsPerSec_Type()
)
exchisRPCOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisRPCOperationsPerSec.setStatus("mandatory")
_ExchisReadBytesRPCClientsPerSec_Type = Counter32
_ExchisReadBytesRPCClientsPerSec_Object = MibScalar
exchisReadBytesRPCClientsPerSec = _ExchisReadBytesRPCClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 3),
    _ExchisReadBytesRPCClientsPerSec_Type()
)
exchisReadBytesRPCClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisReadBytesRPCClientsPerSec.setStatus("mandatory")
_ExchisWriteBytesRPCClientsPerSec_Type = Counter32
_ExchisWriteBytesRPCClientsPerSec_Object = MibScalar
exchisWriteBytesRPCClientsPerSec = _ExchisWriteBytesRPCClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 4),
    _ExchisWriteBytesRPCClientsPerSec_Type()
)
exchisWriteBytesRPCClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisWriteBytesRPCClientsPerSec.setStatus("mandatory")
_ExchisPushNotificationsGeneratedPerSec_Type = Counter32
_ExchisPushNotificationsGeneratedPerSec_Object = MibScalar
exchisPushNotificationsGeneratedPerSec = _ExchisPushNotificationsGeneratedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 5),
    _ExchisPushNotificationsGeneratedPerSec_Type()
)
exchisPushNotificationsGeneratedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPushNotificationsGeneratedPerSec.setStatus("mandatory")
_ExchisPushNotificationsSkippedPerSec_Type = Counter32
_ExchisPushNotificationsSkippedPerSec_Object = MibScalar
exchisPushNotificationsSkippedPerSec = _ExchisPushNotificationsSkippedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 6),
    _ExchisPushNotificationsSkippedPerSec_Type()
)
exchisPushNotificationsSkippedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPushNotificationsSkippedPerSec.setStatus("mandatory")
_ExchisRPCRequests_Type = Integer32
_ExchisRPCRequests_Object = MibScalar
exchisRPCRequests = _ExchisRPCRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 7),
    _ExchisRPCRequests_Type()
)
exchisRPCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisRPCRequests.setStatus("mandatory")
_ExchisRPCRequestsPeak_Type = Integer32
_ExchisRPCRequestsPeak_Object = MibScalar
exchisRPCRequestsPeak = _ExchisRPCRequestsPeak_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 8),
    _ExchisRPCRequestsPeak_Type()
)
exchisRPCRequestsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisRPCRequestsPeak.setStatus("mandatory")
_ExchisUserCount_Type = Integer32
_ExchisUserCount_Object = MibScalar
exchisUserCount = _ExchisUserCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 9),
    _ExchisUserCount_Type()
)
exchisUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisUserCount.setStatus("mandatory")
_ExchisActiveUserCount_Type = Integer32
_ExchisActiveUserCount_Object = MibScalar
exchisActiveUserCount = _ExchisActiveUserCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 10),
    _ExchisActiveUserCount_Type()
)
exchisActiveUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisActiveUserCount.setStatus("mandatory")
_ExchisMaximumUsers_Type = Integer32
_ExchisMaximumUsers_Object = MibScalar
exchisMaximumUsers = _ExchisMaximumUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 11),
    _ExchisMaximumUsers_Type()
)
exchisMaximumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisMaximumUsers.setStatus("mandatory")
_ExchisAnonymousUserCount_Type = Integer32
_ExchisAnonymousUserCount_Object = MibScalar
exchisAnonymousUserCount = _ExchisAnonymousUserCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 12),
    _ExchisAnonymousUserCount_Type()
)
exchisAnonymousUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisAnonymousUserCount.setStatus("mandatory")
_ExchisActiveAnonymousUserCount_Type = Integer32
_ExchisActiveAnonymousUserCount_Object = MibScalar
exchisActiveAnonymousUserCount = _ExchisActiveAnonymousUserCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 13),
    _ExchisActiveAnonymousUserCount_Type()
)
exchisActiveAnonymousUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisActiveAnonymousUserCount.setStatus("mandatory")
_ExchisMaximumAnonymousUsers_Type = Integer32
_ExchisMaximumAnonymousUsers_Object = MibScalar
exchisMaximumAnonymousUsers = _ExchisMaximumAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 14),
    _ExchisMaximumAnonymousUsers_Type()
)
exchisMaximumAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisMaximumAnonymousUsers.setStatus("mandatory")
_ExchisConnectionCount_Type = Integer32
_ExchisConnectionCount_Object = MibScalar
exchisConnectionCount = _ExchisConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 15),
    _ExchisConnectionCount_Type()
)
exchisConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisConnectionCount.setStatus("mandatory")
_ExchisActiveConnectionCount_Type = Integer32
_ExchisActiveConnectionCount_Object = MibScalar
exchisActiveConnectionCount = _ExchisActiveConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 16),
    _ExchisActiveConnectionCount_Type()
)
exchisActiveConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisActiveConnectionCount.setStatus("mandatory")
_ExchisMaximumConnections_Type = Integer32
_ExchisMaximumConnections_Object = MibScalar
exchisMaximumConnections = _ExchisMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 17),
    _ExchisMaximumConnections_Type()
)
exchisMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisMaximumConnections.setStatus("mandatory")
_ExchisPushNotificationsCacheSize_Type = Integer32
_ExchisPushNotificationsCacheSize_Object = MibScalar
exchisPushNotificationsCacheSize = _ExchisPushNotificationsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 18),
    _ExchisPushNotificationsCacheSize_Type()
)
exchisPushNotificationsCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPushNotificationsCacheSize.setStatus("mandatory")
_ExchisPeakPushNotificationsCacheSize_Type = Integer32
_ExchisPeakPushNotificationsCacheSize_Object = MibScalar
exchisPeakPushNotificationsCacheSize = _ExchisPeakPushNotificationsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 19),
    _ExchisPeakPushNotificationsCacheSize_Type()
)
exchisPeakPushNotificationsCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPeakPushNotificationsCacheSize.setStatus("mandatory")
_ExchisDatabaseSessionHitRate_Type = Integer32
_ExchisDatabaseSessionHitRate_Object = MibScalar
exchisDatabaseSessionHitRate = _ExchisDatabaseSessionHitRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 20),
    _ExchisDatabaseSessionHitRate_Type()
)
exchisDatabaseSessionHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisDatabaseSessionHitRate.setStatus("mandatory")
_ExchisIMAPMessagesSent_Type = Integer32
_ExchisIMAPMessagesSent_Object = MibScalar
exchisIMAPMessagesSent = _ExchisIMAPMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 22),
    _ExchisIMAPMessagesSent_Type()
)
exchisIMAPMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisIMAPMessagesSent.setStatus("mandatory")
_ExchisIMAPCommandsIssued_Type = Integer32
_ExchisIMAPCommandsIssued_Object = MibScalar
exchisIMAPCommandsIssued = _ExchisIMAPCommandsIssued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 23),
    _ExchisIMAPCommandsIssued_Type()
)
exchisIMAPCommandsIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisIMAPCommandsIssued.setStatus("mandatory")
_ExchisIMAPMessageSendRate_Type = Counter32
_ExchisIMAPMessageSendRate_Object = MibScalar
exchisIMAPMessageSendRate = _ExchisIMAPMessageSendRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 24),
    _ExchisIMAPMessageSendRate_Type()
)
exchisIMAPMessageSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisIMAPMessageSendRate.setStatus("mandatory")
_ExchisIMAPCommandsIssuedRate_Type = Counter32
_ExchisIMAPCommandsIssuedRate_Object = MibScalar
exchisIMAPCommandsIssuedRate = _ExchisIMAPCommandsIssuedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 25),
    _ExchisIMAPCommandsIssuedRate_Type()
)
exchisIMAPCommandsIssuedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisIMAPCommandsIssuedRate.setStatus("mandatory")
_ExchisPOP3MessagesSent_Type = Integer32
_ExchisPOP3MessagesSent_Object = MibScalar
exchisPOP3MessagesSent = _ExchisPOP3MessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 26),
    _ExchisPOP3MessagesSent_Type()
)
exchisPOP3MessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPOP3MessagesSent.setStatus("mandatory")
_ExchisPOP3CommandsIssued_Type = Integer32
_ExchisPOP3CommandsIssued_Object = MibScalar
exchisPOP3CommandsIssued = _ExchisPOP3CommandsIssued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 27),
    _ExchisPOP3CommandsIssued_Type()
)
exchisPOP3CommandsIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPOP3CommandsIssued.setStatus("mandatory")
_ExchisPOP3MessagesSendRate_Type = Counter32
_ExchisPOP3MessagesSendRate_Object = MibScalar
exchisPOP3MessagesSendRate = _ExchisPOP3MessagesSendRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 28),
    _ExchisPOP3MessagesSendRate_Type()
)
exchisPOP3MessagesSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPOP3MessagesSendRate.setStatus("mandatory")
_ExchisPOP3CommandsIssuedRate_Type = Counter32
_ExchisPOP3CommandsIssuedRate_Object = MibScalar
exchisPOP3CommandsIssuedRate = _ExchisPOP3CommandsIssuedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 29),
    _ExchisPOP3CommandsIssuedRate_Type()
)
exchisPOP3CommandsIssuedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisPOP3CommandsIssuedRate.setStatus("mandatory")
_ExchisNNTPMessagesRead_Type = Integer32
_ExchisNNTPMessagesRead_Object = MibScalar
exchisNNTPMessagesRead = _ExchisNNTPMessagesRead_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 30),
    _ExchisNNTPMessagesRead_Type()
)
exchisNNTPMessagesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPMessagesRead.setStatus("mandatory")
_ExchisNNTPMessagesPosted_Type = Integer32
_ExchisNNTPMessagesPosted_Object = MibScalar
exchisNNTPMessagesPosted = _ExchisNNTPMessagesPosted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 31),
    _ExchisNNTPMessagesPosted_Type()
)
exchisNNTPMessagesPosted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPMessagesPosted.setStatus("mandatory")
_ExchisNNTPFailedPosts_Type = Integer32
_ExchisNNTPFailedPosts_Object = MibScalar
exchisNNTPFailedPosts = _ExchisNNTPFailedPosts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 32),
    _ExchisNNTPFailedPosts_Type()
)
exchisNNTPFailedPosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPFailedPosts.setStatus("mandatory")
_ExchisNewsfeedMessagesReceived_Type = Integer32
_ExchisNewsfeedMessagesReceived_Object = MibScalar
exchisNewsfeedMessagesReceived = _ExchisNewsfeedMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 33),
    _ExchisNewsfeedMessagesReceived_Type()
)
exchisNewsfeedMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedMessagesReceived.setStatus("mandatory")
_ExchisNewsfeedInboundRejectedMessages_Type = Integer32
_ExchisNewsfeedInboundRejectedMessages_Object = MibScalar
exchisNewsfeedInboundRejectedMessages = _ExchisNewsfeedInboundRejectedMessages_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 34),
    _ExchisNewsfeedInboundRejectedMessages_Type()
)
exchisNewsfeedInboundRejectedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedInboundRejectedMessages.setStatus("mandatory")
_ExchisNNTPCommandsIssued_Type = Integer32
_ExchisNNTPCommandsIssued_Object = MibScalar
exchisNNTPCommandsIssued = _ExchisNNTPCommandsIssued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 35),
    _ExchisNNTPCommandsIssued_Type()
)
exchisNNTPCommandsIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPCommandsIssued.setStatus("mandatory")
_ExchisNNTPMessagesReadRate_Type = Counter32
_ExchisNNTPMessagesReadRate_Object = MibScalar
exchisNNTPMessagesReadRate = _ExchisNNTPMessagesReadRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 36),
    _ExchisNNTPMessagesReadRate_Type()
)
exchisNNTPMessagesReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPMessagesReadRate.setStatus("mandatory")
_ExchisNNTPMessagesPostedRate_Type = Counter32
_ExchisNNTPMessagesPostedRate_Object = MibScalar
exchisNNTPMessagesPostedRate = _ExchisNNTPMessagesPostedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 37),
    _ExchisNNTPMessagesPostedRate_Type()
)
exchisNNTPMessagesPostedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPMessagesPostedRate.setStatus("mandatory")
_ExchisNNTPFailedPostsRate_Type = Counter32
_ExchisNNTPFailedPostsRate_Object = MibScalar
exchisNNTPFailedPostsRate = _ExchisNNTPFailedPostsRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 38),
    _ExchisNNTPFailedPostsRate_Type()
)
exchisNNTPFailedPostsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPFailedPostsRate.setStatus("mandatory")
_ExchisNewsfeedMessagesReceivedRate_Type = Counter32
_ExchisNewsfeedMessagesReceivedRate_Object = MibScalar
exchisNewsfeedMessagesReceivedRate = _ExchisNewsfeedMessagesReceivedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 39),
    _ExchisNewsfeedMessagesReceivedRate_Type()
)
exchisNewsfeedMessagesReceivedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedMessagesReceivedRate.setStatus("mandatory")
_ExchisNewsfeedInboundRejectedMessagesRate_Type = Counter32
_ExchisNewsfeedInboundRejectedMessagesRate_Object = MibScalar
exchisNewsfeedInboundRejectedMessagesRate = _ExchisNewsfeedInboundRejectedMessagesRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 40),
    _ExchisNewsfeedInboundRejectedMessagesRate_Type()
)
exchisNewsfeedInboundRejectedMessagesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedInboundRejectedMessagesRate.setStatus("mandatory")
_ExchisNNTPCommandsIssuedRate_Type = Counter32
_ExchisNNTPCommandsIssuedRate_Object = MibScalar
exchisNNTPCommandsIssuedRate = _ExchisNNTPCommandsIssuedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 41),
    _ExchisNNTPCommandsIssuedRate_Type()
)
exchisNNTPCommandsIssuedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPCommandsIssuedRate.setStatus("mandatory")
_ExchisNewsfeedMessagesSent_Type = Integer32
_ExchisNewsfeedMessagesSent_Object = MibScalar
exchisNewsfeedMessagesSent = _ExchisNewsfeedMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 42),
    _ExchisNewsfeedMessagesSent_Type()
)
exchisNewsfeedMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedMessagesSent.setStatus("mandatory")
_ExchisNewsfeedMessagesSentPerSec_Type = Counter32
_ExchisNewsfeedMessagesSentPerSec_Object = MibScalar
exchisNewsfeedMessagesSentPerSec = _ExchisNewsfeedMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 43),
    _ExchisNewsfeedMessagesSentPerSec_Type()
)
exchisNewsfeedMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedMessagesSentPerSec.setStatus("mandatory")
_ExchisNewsfeedBytesSent_Type = Integer32
_ExchisNewsfeedBytesSent_Object = MibScalar
exchisNewsfeedBytesSent = _ExchisNewsfeedBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 44),
    _ExchisNewsfeedBytesSent_Type()
)
exchisNewsfeedBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedBytesSent.setStatus("mandatory")
_ExchisNewsfeedBytesSentPerSec_Type = Counter32
_ExchisNewsfeedBytesSentPerSec_Object = MibScalar
exchisNewsfeedBytesSentPerSec = _ExchisNewsfeedBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 45),
    _ExchisNewsfeedBytesSentPerSec_Type()
)
exchisNewsfeedBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedBytesSentPerSec.setStatus("mandatory")
_ExchisNewsfeedOutboundRejectedMessages_Type = Integer32
_ExchisNewsfeedOutboundRejectedMessages_Object = MibScalar
exchisNewsfeedOutboundRejectedMessages = _ExchisNewsfeedOutboundRejectedMessages_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 46),
    _ExchisNewsfeedOutboundRejectedMessages_Type()
)
exchisNewsfeedOutboundRejectedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNewsfeedOutboundRejectedMessages.setStatus("mandatory")
_ExchisNNTPOutboundConnections_Type = Integer32
_ExchisNNTPOutboundConnections_Object = MibScalar
exchisNNTPOutboundConnections = _ExchisNNTPOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 47),
    _ExchisNNTPOutboundConnections_Type()
)
exchisNNTPOutboundConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPOutboundConnections.setStatus("mandatory")
_ExchisNNTPCurrentOutboundConnections_Type = Integer32
_ExchisNNTPCurrentOutboundConnections_Object = MibScalar
exchisNNTPCurrentOutboundConnections = _ExchisNNTPCurrentOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 48),
    _ExchisNNTPCurrentOutboundConnections_Type()
)
exchisNNTPCurrentOutboundConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNNTPCurrentOutboundConnections.setStatus("mandatory")
_ExchisNumberOfArticleIndexTableRowsExpired_Type = Integer32
_ExchisNumberOfArticleIndexTableRowsExpired_Object = MibScalar
exchisNumberOfArticleIndexTableRowsExpired = _ExchisNumberOfArticleIndexTableRowsExpired_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 23, 49),
    _ExchisNumberOfArticleIndexTableRowsExpired_Type()
)
exchisNumberOfArticleIndexTableRowsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisNumberOfArticleIndexTableRowsExpired.setStatus("mandatory")
_MSExchangeIS_Public_ObjectIdentity = ObjectIdentity
mSExchangeIS_Public = _MSExchangeIS_Public_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24)
)
_ExchispubSendQueueSize_Type = Integer32
_ExchispubSendQueueSize_Object = MibScalar
exchispubSendQueueSize = _ExchispubSendQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 1),
    _ExchispubSendQueueSize_Type()
)
exchispubSendQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubSendQueueSize.setStatus("mandatory")
_ExchispubReceiveQueueSize_Type = Integer32
_ExchispubReceiveQueueSize_Object = MibScalar
exchispubReceiveQueueSize = _ExchispubReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 2),
    _ExchispubReceiveQueueSize_Type()
)
exchispubReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReceiveQueueSize.setStatus("mandatory")
_ExchispubCategorizationCount_Type = Integer32
_ExchispubCategorizationCount_Object = MibScalar
exchispubCategorizationCount = _ExchispubCategorizationCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 3),
    _ExchispubCategorizationCount_Type()
)
exchispubCategorizationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubCategorizationCount.setStatus("mandatory")
_ExchispubMessagesDelivered_Type = Integer32
_ExchispubMessagesDelivered_Object = MibScalar
exchispubMessagesDelivered = _ExchispubMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 4),
    _ExchispubMessagesDelivered_Type()
)
exchispubMessagesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessagesDelivered.setStatus("mandatory")
_ExchispubMessageRecipientsDelivered_Type = Integer32
_ExchispubMessageRecipientsDelivered_Object = MibScalar
exchispubMessageRecipientsDelivered = _ExchispubMessageRecipientsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 5),
    _ExchispubMessageRecipientsDelivered_Type()
)
exchispubMessageRecipientsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessageRecipientsDelivered.setStatus("mandatory")
_ExchispubMessagesSent_Type = Integer32
_ExchispubMessagesSent_Object = MibScalar
exchispubMessagesSent = _ExchispubMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 6),
    _ExchispubMessagesSent_Type()
)
exchispubMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessagesSent.setStatus("mandatory")
_ExchispubMessagesSubmitted_Type = Integer32
_ExchispubMessagesSubmitted_Object = MibScalar
exchispubMessagesSubmitted = _ExchispubMessagesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 7),
    _ExchispubMessagesSubmitted_Type()
)
exchispubMessagesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessagesSubmitted.setStatus("mandatory")
_ExchispubSingleInstanceRatio_Type = Integer32
_ExchispubSingleInstanceRatio_Object = MibScalar
exchispubSingleInstanceRatio = _ExchispubSingleInstanceRatio_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 8),
    _ExchispubSingleInstanceRatio_Type()
)
exchispubSingleInstanceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubSingleInstanceRatio.setStatus("mandatory")
_ExchispubMessagesDeliveredPerMin_Type = Integer32
_ExchispubMessagesDeliveredPerMin_Object = MibScalar
exchispubMessagesDeliveredPerMin = _ExchispubMessagesDeliveredPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 10),
    _ExchispubMessagesDeliveredPerMin_Type()
)
exchispubMessagesDeliveredPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessagesDeliveredPerMin.setStatus("mandatory")
_ExchispubMessageRecipientsDeliveredPerMin_Type = Integer32
_ExchispubMessageRecipientsDeliveredPerMin_Object = MibScalar
exchispubMessageRecipientsDeliveredPerMin = _ExchispubMessageRecipientsDeliveredPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 11),
    _ExchispubMessageRecipientsDeliveredPerMin_Type()
)
exchispubMessageRecipientsDeliveredPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessageRecipientsDeliveredPerMin.setStatus("mandatory")
_ExchispubMessagesSentPerMin_Type = Integer32
_ExchispubMessagesSentPerMin_Object = MibScalar
exchispubMessagesSentPerMin = _ExchispubMessagesSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 12),
    _ExchispubMessagesSentPerMin_Type()
)
exchispubMessagesSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessagesSentPerMin.setStatus("mandatory")
_ExchispubMessageSubmittedPerMin_Type = Integer32
_ExchispubMessageSubmittedPerMin_Object = MibScalar
exchispubMessageSubmittedPerMin = _ExchispubMessageSubmittedPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 13),
    _ExchispubMessageSubmittedPerMin_Type()
)
exchispubMessageSubmittedPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessageSubmittedPerMin.setStatus("mandatory")
_ExchispubAverageTimeForDelivery_Type = Integer32
_ExchispubAverageTimeForDelivery_Object = MibScalar
exchispubAverageTimeForDelivery = _ExchispubAverageTimeForDelivery_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 14),
    _ExchispubAverageTimeForDelivery_Type()
)
exchispubAverageTimeForDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubAverageTimeForDelivery.setStatus("mandatory")
_ExchispubAverageTimeForLocalDelivery_Type = Integer32
_ExchispubAverageTimeForLocalDelivery_Object = MibScalar
exchispubAverageTimeForLocalDelivery = _ExchispubAverageTimeForLocalDelivery_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 15),
    _ExchispubAverageTimeForLocalDelivery_Type()
)
exchispubAverageTimeForLocalDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubAverageTimeForLocalDelivery.setStatus("mandatory")
_ExchispubTotalSizeOfRecoverableItems_Type = Integer32
_ExchispubTotalSizeOfRecoverableItems_Object = MibScalar
exchispubTotalSizeOfRecoverableItems = _ExchispubTotalSizeOfRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 16),
    _ExchispubTotalSizeOfRecoverableItems_Type()
)
exchispubTotalSizeOfRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubTotalSizeOfRecoverableItems.setStatus("mandatory")
_ExchispubTotalCountOfRecoverableItems_Type = Integer32
_ExchispubTotalCountOfRecoverableItems_Object = MibScalar
exchispubTotalCountOfRecoverableItems = _ExchispubTotalCountOfRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 17),
    _ExchispubTotalCountOfRecoverableItems_Type()
)
exchispubTotalCountOfRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubTotalCountOfRecoverableItems.setStatus("mandatory")
_ExchispubReplicationMessagesSent_Type = Integer32
_ExchispubReplicationMessagesSent_Object = MibScalar
exchispubReplicationMessagesSent = _ExchispubReplicationMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 18),
    _ExchispubReplicationMessagesSent_Type()
)
exchispubReplicationMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationMessagesSent.setStatus("mandatory")
_ExchispubReplicationFolderTreeMessagesSent_Type = Integer32
_ExchispubReplicationFolderTreeMessagesSent_Object = MibScalar
exchispubReplicationFolderTreeMessagesSent = _ExchispubReplicationFolderTreeMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 19),
    _ExchispubReplicationFolderTreeMessagesSent_Type()
)
exchispubReplicationFolderTreeMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderTreeMessagesSent.setStatus("mandatory")
_ExchispubReplicationFolderChangesSent_Type = Integer32
_ExchispubReplicationFolderChangesSent_Object = MibScalar
exchispubReplicationFolderChangesSent = _ExchispubReplicationFolderChangesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 20),
    _ExchispubReplicationFolderChangesSent_Type()
)
exchispubReplicationFolderChangesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderChangesSent.setStatus("mandatory")
_ExchispubReplicationFolderDataMessagesSent_Type = Integer32
_ExchispubReplicationFolderDataMessagesSent_Object = MibScalar
exchispubReplicationFolderDataMessagesSent = _ExchispubReplicationFolderDataMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 21),
    _ExchispubReplicationFolderDataMessagesSent_Type()
)
exchispubReplicationFolderDataMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderDataMessagesSent.setStatus("mandatory")
_ExchispubReplicationMessageChangesSent_Type = Integer32
_ExchispubReplicationMessageChangesSent_Object = MibScalar
exchispubReplicationMessageChangesSent = _ExchispubReplicationMessageChangesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 22),
    _ExchispubReplicationMessageChangesSent_Type()
)
exchispubReplicationMessageChangesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationMessageChangesSent.setStatus("mandatory")
_ExchispubReplicationStatusMessagesSent_Type = Integer32
_ExchispubReplicationStatusMessagesSent_Object = MibScalar
exchispubReplicationStatusMessagesSent = _ExchispubReplicationStatusMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 23),
    _ExchispubReplicationStatusMessagesSent_Type()
)
exchispubReplicationStatusMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationStatusMessagesSent.setStatus("mandatory")
_ExchispubReplicationBackfillRequestsSent_Type = Integer32
_ExchispubReplicationBackfillRequestsSent_Object = MibScalar
exchispubReplicationBackfillRequestsSent = _ExchispubReplicationBackfillRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 24),
    _ExchispubReplicationBackfillRequestsSent_Type()
)
exchispubReplicationBackfillRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationBackfillRequestsSent.setStatus("mandatory")
_ExchispubReplicationBackfillDataMessagesSent_Type = Integer32
_ExchispubReplicationBackfillDataMessagesSent_Object = MibScalar
exchispubReplicationBackfillDataMessagesSent = _ExchispubReplicationBackfillDataMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 25),
    _ExchispubReplicationBackfillDataMessagesSent_Type()
)
exchispubReplicationBackfillDataMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationBackfillDataMessagesSent.setStatus("mandatory")
_ExchispubReplicationMessagesReceived_Type = Integer32
_ExchispubReplicationMessagesReceived_Object = MibScalar
exchispubReplicationMessagesReceived = _ExchispubReplicationMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 26),
    _ExchispubReplicationMessagesReceived_Type()
)
exchispubReplicationMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationMessagesReceived.setStatus("mandatory")
_ExchispubReplicationFolderTreeMessagesReceived_Type = Integer32
_ExchispubReplicationFolderTreeMessagesReceived_Object = MibScalar
exchispubReplicationFolderTreeMessagesReceived = _ExchispubReplicationFolderTreeMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 27),
    _ExchispubReplicationFolderTreeMessagesReceived_Type()
)
exchispubReplicationFolderTreeMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderTreeMessagesReceived.setStatus("mandatory")
_ExchispubReplicationFolderChangesReceived_Type = Integer32
_ExchispubReplicationFolderChangesReceived_Object = MibScalar
exchispubReplicationFolderChangesReceived = _ExchispubReplicationFolderChangesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 28),
    _ExchispubReplicationFolderChangesReceived_Type()
)
exchispubReplicationFolderChangesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderChangesReceived.setStatus("mandatory")
_ExchispubReplicationFolderDataMessagesReceived_Type = Integer32
_ExchispubReplicationFolderDataMessagesReceived_Object = MibScalar
exchispubReplicationFolderDataMessagesReceived = _ExchispubReplicationFolderDataMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 29),
    _ExchispubReplicationFolderDataMessagesReceived_Type()
)
exchispubReplicationFolderDataMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationFolderDataMessagesReceived.setStatus("mandatory")
_ExchispubReplicationMessageChangesReceived_Type = Integer32
_ExchispubReplicationMessageChangesReceived_Object = MibScalar
exchispubReplicationMessageChangesReceived = _ExchispubReplicationMessageChangesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 30),
    _ExchispubReplicationMessageChangesReceived_Type()
)
exchispubReplicationMessageChangesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationMessageChangesReceived.setStatus("mandatory")
_ExchispubReplicationStatusMessagesReceived_Type = Integer32
_ExchispubReplicationStatusMessagesReceived_Object = MibScalar
exchispubReplicationStatusMessagesReceived = _ExchispubReplicationStatusMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 31),
    _ExchispubReplicationStatusMessagesReceived_Type()
)
exchispubReplicationStatusMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationStatusMessagesReceived.setStatus("mandatory")
_ExchispubReplicationBackfillRequestsReceived_Type = Integer32
_ExchispubReplicationBackfillRequestsReceived_Object = MibScalar
exchispubReplicationBackfillRequestsReceived = _ExchispubReplicationBackfillRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 32),
    _ExchispubReplicationBackfillRequestsReceived_Type()
)
exchispubReplicationBackfillRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationBackfillRequestsReceived.setStatus("mandatory")
_ExchispubReplicationBackfillDataMessagesReceived_Type = Integer32
_ExchispubReplicationBackfillDataMessagesReceived_Object = MibScalar
exchispubReplicationBackfillDataMessagesReceived = _ExchispubReplicationBackfillDataMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 33),
    _ExchispubReplicationBackfillDataMessagesReceived_Type()
)
exchispubReplicationBackfillDataMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationBackfillDataMessagesReceived.setStatus("mandatory")
_ExchispubReplicationReceiveQueueSize_Type = Integer32
_ExchispubReplicationReceiveQueueSize_Object = MibScalar
exchispubReplicationReceiveQueueSize = _ExchispubReplicationReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 34),
    _ExchispubReplicationReceiveQueueSize_Type()
)
exchispubReplicationReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubReplicationReceiveQueueSize.setStatus("mandatory")
_ExchispubNumberOfMessagesExpiredFromPublicFolders_Type = Integer32
_ExchispubNumberOfMessagesExpiredFromPublicFolders_Object = MibScalar
exchispubNumberOfMessagesExpiredFromPublicFolders = _ExchispubNumberOfMessagesExpiredFromPublicFolders_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 35),
    _ExchispubNumberOfMessagesExpiredFromPublicFolders_Type()
)
exchispubNumberOfMessagesExpiredFromPublicFolders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubNumberOfMessagesExpiredFromPublicFolders.setStatus("mandatory")
_ExchispubClientLogons_Type = Integer32
_ExchispubClientLogons_Object = MibScalar
exchispubClientLogons = _ExchispubClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 36),
    _ExchispubClientLogons_Type()
)
exchispubClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubClientLogons.setStatus("mandatory")
_ExchispubActiveClientLogons_Type = Integer32
_ExchispubActiveClientLogons_Object = MibScalar
exchispubActiveClientLogons = _ExchispubActiveClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 37),
    _ExchispubActiveClientLogons_Type()
)
exchispubActiveClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubActiveClientLogons.setStatus("mandatory")
_ExchispubPeakClientLogons_Type = Integer32
_ExchispubPeakClientLogons_Object = MibScalar
exchispubPeakClientLogons = _ExchispubPeakClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 38),
    _ExchispubPeakClientLogons_Type()
)
exchispubPeakClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubPeakClientLogons.setStatus("mandatory")
_ExchispubFolderOpensPerSec_Type = Counter32
_ExchispubFolderOpensPerSec_Object = MibScalar
exchispubFolderOpensPerSec = _ExchispubFolderOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 41),
    _ExchispubFolderOpensPerSec_Type()
)
exchispubFolderOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubFolderOpensPerSec.setStatus("mandatory")
_ExchispubMessageOpensPerSec_Type = Counter32
_ExchispubMessageOpensPerSec_Object = MibScalar
exchispubMessageOpensPerSec = _ExchispubMessageOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 24, 42),
    _ExchispubMessageOpensPerSec_Type()
)
exchispubMessageOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchispubMessageOpensPerSec.setStatus("mandatory")
_MSExchangeIS_Private_ObjectIdentity = ObjectIdentity
mSExchangeIS_Private = _MSExchangeIS_Private_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25)
)
_ExchisprivSendQueueSize_Type = Integer32
_ExchisprivSendQueueSize_Object = MibScalar
exchisprivSendQueueSize = _ExchisprivSendQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 1),
    _ExchisprivSendQueueSize_Type()
)
exchisprivSendQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivSendQueueSize.setStatus("mandatory")
_ExchisprivReceiveQueueSize_Type = Integer32
_ExchisprivReceiveQueueSize_Object = MibScalar
exchisprivReceiveQueueSize = _ExchisprivReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 2),
    _ExchisprivReceiveQueueSize_Type()
)
exchisprivReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivReceiveQueueSize.setStatus("mandatory")
_ExchisprivCategorizationCount_Type = Integer32
_ExchisprivCategorizationCount_Object = MibScalar
exchisprivCategorizationCount = _ExchisprivCategorizationCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 3),
    _ExchisprivCategorizationCount_Type()
)
exchisprivCategorizationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivCategorizationCount.setStatus("mandatory")
_ExchisprivMessagesDelivered_Type = Integer32
_ExchisprivMessagesDelivered_Object = MibScalar
exchisprivMessagesDelivered = _ExchisprivMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 4),
    _ExchisprivMessagesDelivered_Type()
)
exchisprivMessagesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesDelivered.setStatus("mandatory")
_ExchisprivMessageRecipientsDelivered_Type = Integer32
_ExchisprivMessageRecipientsDelivered_Object = MibScalar
exchisprivMessageRecipientsDelivered = _ExchisprivMessageRecipientsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 5),
    _ExchisprivMessageRecipientsDelivered_Type()
)
exchisprivMessageRecipientsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessageRecipientsDelivered.setStatus("mandatory")
_ExchisprivMessagesSent_Type = Integer32
_ExchisprivMessagesSent_Object = MibScalar
exchisprivMessagesSent = _ExchisprivMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 6),
    _ExchisprivMessagesSent_Type()
)
exchisprivMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesSent.setStatus("mandatory")
_ExchisprivMessagesSubmitted_Type = Integer32
_ExchisprivMessagesSubmitted_Object = MibScalar
exchisprivMessagesSubmitted = _ExchisprivMessagesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 7),
    _ExchisprivMessagesSubmitted_Type()
)
exchisprivMessagesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesSubmitted.setStatus("mandatory")
_ExchisprivSingleInstanceRatio_Type = Integer32
_ExchisprivSingleInstanceRatio_Object = MibScalar
exchisprivSingleInstanceRatio = _ExchisprivSingleInstanceRatio_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 8),
    _ExchisprivSingleInstanceRatio_Type()
)
exchisprivSingleInstanceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivSingleInstanceRatio.setStatus("mandatory")
_ExchisprivMessagesDeliveredPerMin_Type = Integer32
_ExchisprivMessagesDeliveredPerMin_Object = MibScalar
exchisprivMessagesDeliveredPerMin = _ExchisprivMessagesDeliveredPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 10),
    _ExchisprivMessagesDeliveredPerMin_Type()
)
exchisprivMessagesDeliveredPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesDeliveredPerMin.setStatus("mandatory")
_ExchisprivMessageRecipientsDeliveredPerMin_Type = Integer32
_ExchisprivMessageRecipientsDeliveredPerMin_Object = MibScalar
exchisprivMessageRecipientsDeliveredPerMin = _ExchisprivMessageRecipientsDeliveredPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 11),
    _ExchisprivMessageRecipientsDeliveredPerMin_Type()
)
exchisprivMessageRecipientsDeliveredPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessageRecipientsDeliveredPerMin.setStatus("mandatory")
_ExchisprivMessagesSentPerMin_Type = Integer32
_ExchisprivMessagesSentPerMin_Object = MibScalar
exchisprivMessagesSentPerMin = _ExchisprivMessagesSentPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 12),
    _ExchisprivMessagesSentPerMin_Type()
)
exchisprivMessagesSentPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesSentPerMin.setStatus("mandatory")
_ExchisprivMessagesSubmittedPerMin_Type = Integer32
_ExchisprivMessagesSubmittedPerMin_Object = MibScalar
exchisprivMessagesSubmittedPerMin = _ExchisprivMessagesSubmittedPerMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 13),
    _ExchisprivMessagesSubmittedPerMin_Type()
)
exchisprivMessagesSubmittedPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessagesSubmittedPerMin.setStatus("mandatory")
_ExchisprivAverageDeliveryTime_Type = Integer32
_ExchisprivAverageDeliveryTime_Object = MibScalar
exchisprivAverageDeliveryTime = _ExchisprivAverageDeliveryTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 14),
    _ExchisprivAverageDeliveryTime_Type()
)
exchisprivAverageDeliveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivAverageDeliveryTime.setStatus("mandatory")
_ExchisprivAverageLocalDeliveryTime_Type = Integer32
_ExchisprivAverageLocalDeliveryTime_Object = MibScalar
exchisprivAverageLocalDeliveryTime = _ExchisprivAverageLocalDeliveryTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 15),
    _ExchisprivAverageLocalDeliveryTime_Type()
)
exchisprivAverageLocalDeliveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivAverageLocalDeliveryTime.setStatus("mandatory")
_ExchisprivTotalSizeOfRecoverableItems_Type = Integer32
_ExchisprivTotalSizeOfRecoverableItems_Object = MibScalar
exchisprivTotalSizeOfRecoverableItems = _ExchisprivTotalSizeOfRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 16),
    _ExchisprivTotalSizeOfRecoverableItems_Type()
)
exchisprivTotalSizeOfRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivTotalSizeOfRecoverableItems.setStatus("mandatory")
_ExchisprivTotalCountOfRecoverableItems_Type = Integer32
_ExchisprivTotalCountOfRecoverableItems_Object = MibScalar
exchisprivTotalCountOfRecoverableItems = _ExchisprivTotalCountOfRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 17),
    _ExchisprivTotalCountOfRecoverableItems_Type()
)
exchisprivTotalCountOfRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivTotalCountOfRecoverableItems.setStatus("mandatory")
_ExchisprivClientLogons_Type = Integer32
_ExchisprivClientLogons_Object = MibScalar
exchisprivClientLogons = _ExchisprivClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 36),
    _ExchisprivClientLogons_Type()
)
exchisprivClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivClientLogons.setStatus("mandatory")
_ExchisprivActiveClientLogons_Type = Integer32
_ExchisprivActiveClientLogons_Object = MibScalar
exchisprivActiveClientLogons = _ExchisprivActiveClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 37),
    _ExchisprivActiveClientLogons_Type()
)
exchisprivActiveClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivActiveClientLogons.setStatus("mandatory")
_ExchisprivPeakClientLogons_Type = Integer32
_ExchisprivPeakClientLogons_Object = MibScalar
exchisprivPeakClientLogons = _ExchisprivPeakClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 38),
    _ExchisprivPeakClientLogons_Type()
)
exchisprivPeakClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivPeakClientLogons.setStatus("mandatory")
_ExchisprivLocalDeliveries_Type = Integer32
_ExchisprivLocalDeliveries_Object = MibScalar
exchisprivLocalDeliveries = _ExchisprivLocalDeliveries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 39),
    _ExchisprivLocalDeliveries_Type()
)
exchisprivLocalDeliveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivLocalDeliveries.setStatus("mandatory")
_ExchisprivLocalDeliveryRate_Type = Counter32
_ExchisprivLocalDeliveryRate_Object = MibScalar
exchisprivLocalDeliveryRate = _ExchisprivLocalDeliveryRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 40),
    _ExchisprivLocalDeliveryRate_Type()
)
exchisprivLocalDeliveryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivLocalDeliveryRate.setStatus("mandatory")
_ExchisprivFolderOpensPerSec_Type = Counter32
_ExchisprivFolderOpensPerSec_Object = MibScalar
exchisprivFolderOpensPerSec = _ExchisprivFolderOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 41),
    _ExchisprivFolderOpensPerSec_Type()
)
exchisprivFolderOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivFolderOpensPerSec.setStatus("mandatory")
_ExchisprivMessageOpensPerSec_Type = Counter32
_ExchisprivMessageOpensPerSec_Object = MibScalar
exchisprivMessageOpensPerSec = _ExchisprivMessageOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 25, 42),
    _ExchisprivMessageOpensPerSec_Type()
)
exchisprivMessageOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchisprivMessageOpensPerSec.setStatus("mandatory")
_MSExchangeDS_ObjectIdentity = ObjectIdentity
mSExchangeDS = _MSExchangeDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26)
)
_ExchdsAccessViolations_Type = Integer32
_ExchdsAccessViolations_Object = MibScalar
exchdsAccessViolations = _ExchdsAccessViolations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 1),
    _ExchdsAccessViolations_Type()
)
exchdsAccessViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsAccessViolations.setStatus("mandatory")
_ExchdsABBrowsesPerSec_Type = Counter32
_ExchdsABBrowsesPerSec_Object = MibScalar
exchdsABBrowsesPerSec = _ExchdsABBrowsesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 2),
    _ExchdsABBrowsesPerSec_Type()
)
exchdsABBrowsesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsABBrowsesPerSec.setStatus("mandatory")
_ExchdsABReadsPerSec_Type = Counter32
_ExchdsABReadsPerSec_Object = MibScalar
exchdsABReadsPerSec = _ExchdsABReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 3),
    _ExchdsABReadsPerSec_Type()
)
exchdsABReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsABReadsPerSec.setStatus("mandatory")
_ExchdsExDSReadsPerSec_Type = Counter32
_ExchdsExDSReadsPerSec_Object = MibScalar
exchdsExDSReadsPerSec = _ExchdsExDSReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 4),
    _ExchdsExDSReadsPerSec_Type()
)
exchdsExDSReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsExDSReadsPerSec.setStatus("mandatory")
_ExchdsReplicationUpdatesPerSec_Type = Counter32
_ExchdsReplicationUpdatesPerSec_Object = MibScalar
exchdsReplicationUpdatesPerSec = _ExchdsReplicationUpdatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 5),
    _ExchdsReplicationUpdatesPerSec_Type()
)
exchdsReplicationUpdatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsReplicationUpdatesPerSec.setStatus("mandatory")
_ExchdsThreadsInUse_Type = Integer32
_ExchdsThreadsInUse_Object = MibScalar
exchdsThreadsInUse = _ExchdsThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 6),
    _ExchdsThreadsInUse_Type()
)
exchdsThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsThreadsInUse.setStatus("mandatory")
_ExchdsABWritesPerSec_Type = Counter32
_ExchdsABWritesPerSec_Object = MibScalar
exchdsABWritesPerSec = _ExchdsABWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 7),
    _ExchdsABWritesPerSec_Type()
)
exchdsABWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsABWritesPerSec.setStatus("mandatory")
_ExchdsExDSWritesPerSec_Type = Counter32
_ExchdsExDSWritesPerSec_Object = MibScalar
exchdsExDSWritesPerSec = _ExchdsExDSWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 8),
    _ExchdsExDSWritesPerSec_Type()
)
exchdsExDSWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsExDSWritesPerSec.setStatus("mandatory")
_ExchdsExDSClientSessions_Type = Integer32
_ExchdsExDSClientSessions_Object = MibScalar
exchdsExDSClientSessions = _ExchdsExDSClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 9),
    _ExchdsExDSClientSessions_Type()
)
exchdsExDSClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsExDSClientSessions.setStatus("mandatory")
_ExchdsABClientSessions_Type = Integer32
_ExchdsABClientSessions_Object = MibScalar
exchdsABClientSessions = _ExchdsABClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 10),
    _ExchdsABClientSessions_Type()
)
exchdsABClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsABClientSessions.setStatus("mandatory")
_ExchdsPendingReplicationSynchronizations_Type = Integer32
_ExchdsPendingReplicationSynchronizations_Object = MibScalar
exchdsPendingReplicationSynchronizations = _ExchdsPendingReplicationSynchronizations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 11),
    _ExchdsPendingReplicationSynchronizations_Type()
)
exchdsPendingReplicationSynchronizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsPendingReplicationSynchronizations.setStatus("mandatory")
_ExchdsRemainingReplicationUpdates_Type = Integer32
_ExchdsRemainingReplicationUpdates_Object = MibScalar
exchdsRemainingReplicationUpdates = _ExchdsRemainingReplicationUpdates_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 12),
    _ExchdsRemainingReplicationUpdates_Type()
)
exchdsRemainingReplicationUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsRemainingReplicationUpdates.setStatus("mandatory")
_ExchdsObjectsReplicatedOutPerSec_Type = Counter32
_ExchdsObjectsReplicatedOutPerSec_Object = MibScalar
exchdsObjectsReplicatedOutPerSec = _ExchdsObjectsReplicatedOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 13),
    _ExchdsObjectsReplicatedOutPerSec_Type()
)
exchdsObjectsReplicatedOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsObjectsReplicatedOutPerSec.setStatus("mandatory")
_ExchdsAddressBookViewReadsPerSec_Type = Counter32
_ExchdsAddressBookViewReadsPerSec_Object = MibScalar
exchdsAddressBookViewReadsPerSec = _ExchdsAddressBookViewReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 14),
    _ExchdsAddressBookViewReadsPerSec_Type()
)
exchdsAddressBookViewReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsAddressBookViewReadsPerSec.setStatus("mandatory")
_ExchdsAddressBookViewWritesPerSec_Type = Counter32
_ExchdsAddressBookViewWritesPerSec_Object = MibScalar
exchdsAddressBookViewWritesPerSec = _ExchdsAddressBookViewWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 15),
    _ExchdsAddressBookViewWritesPerSec_Type()
)
exchdsAddressBookViewWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsAddressBookViewWritesPerSec.setStatus("mandatory")
_ExchdsAddressBookViewModifiesPerSec_Type = Counter32
_ExchdsAddressBookViewModifiesPerSec_Object = MibScalar
exchdsAddressBookViewModifiesPerSec = _ExchdsAddressBookViewModifiesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 16),
    _ExchdsAddressBookViewModifiesPerSec_Type()
)
exchdsAddressBookViewModifiesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsAddressBookViewModifiesPerSec.setStatus("mandatory")
_ExchdsLDAPSearches_Type = Integer32
_ExchdsLDAPSearches_Object = MibScalar
exchdsLDAPSearches = _ExchdsLDAPSearches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 17),
    _ExchdsLDAPSearches_Type()
)
exchdsLDAPSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsLDAPSearches.setStatus("mandatory")
_ExchdsLDAPSearchesPerSec_Type = Counter32
_ExchdsLDAPSearchesPerSec_Object = MibScalar
exchdsLDAPSearchesPerSec = _ExchdsLDAPSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 26, 18),
    _ExchdsLDAPSearchesPerSec_Type()
)
exchdsLDAPSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchdsLDAPSearchesPerSec.setStatus("mandatory")
_Web_Proxy_Server_Service_ObjectIdentity = ObjectIdentity
web_Proxy_Server_Service = _Web_Proxy_Server_Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27)
)
_WebproxysrvrUpstreamBytesSentPerSec_Type = Integer32
_WebproxysrvrUpstreamBytesSentPerSec_Object = MibScalar
webproxysrvrUpstreamBytesSentPerSec = _WebproxysrvrUpstreamBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 1),
    _WebproxysrvrUpstreamBytesSentPerSec_Type()
)
webproxysrvrUpstreamBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrUpstreamBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrUpstreamBytesReceivedPerSec_Type = Integer32
_WebproxysrvrUpstreamBytesReceivedPerSec_Object = MibScalar
webproxysrvrUpstreamBytesReceivedPerSec = _WebproxysrvrUpstreamBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 2),
    _WebproxysrvrUpstreamBytesReceivedPerSec_Type()
)
webproxysrvrUpstreamBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrUpstreamBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrUpstreamBytesTotalPerSec_Type = Integer32
_WebproxysrvrUpstreamBytesTotalPerSec_Object = MibScalar
webproxysrvrUpstreamBytesTotalPerSec = _WebproxysrvrUpstreamBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 3),
    _WebproxysrvrUpstreamBytesTotalPerSec_Type()
)
webproxysrvrUpstreamBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrUpstreamBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrClientBytesSentPerSec_Type = Integer32
_WebproxysrvrClientBytesSentPerSec_Object = MibScalar
webproxysrvrClientBytesSentPerSec = _WebproxysrvrClientBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 4),
    _WebproxysrvrClientBytesSentPerSec_Type()
)
webproxysrvrClientBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrClientBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrClientBytesReceivedPerSec_Type = Integer32
_WebproxysrvrClientBytesReceivedPerSec_Object = MibScalar
webproxysrvrClientBytesReceivedPerSec = _WebproxysrvrClientBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 5),
    _WebproxysrvrClientBytesReceivedPerSec_Type()
)
webproxysrvrClientBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrClientBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrClientBytesTotalPerSec_Type = Integer32
_WebproxysrvrClientBytesTotalPerSec_Object = MibScalar
webproxysrvrClientBytesTotalPerSec = _WebproxysrvrClientBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 6),
    _WebproxysrvrClientBytesTotalPerSec_Type()
)
webproxysrvrClientBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrClientBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrSSLClientBytesSentPerSec_Type = Integer32
_WebproxysrvrSSLClientBytesSentPerSec_Object = MibScalar
webproxysrvrSSLClientBytesSentPerSec = _WebproxysrvrSSLClientBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 7),
    _WebproxysrvrSSLClientBytesSentPerSec_Type()
)
webproxysrvrSSLClientBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSSLClientBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrSSLClientBytesReceivedPerSec_Type = Integer32
_WebproxysrvrSSLClientBytesReceivedPerSec_Object = MibScalar
webproxysrvrSSLClientBytesReceivedPerSec = _WebproxysrvrSSLClientBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 8),
    _WebproxysrvrSSLClientBytesReceivedPerSec_Type()
)
webproxysrvrSSLClientBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSSLClientBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrSSLClientBytesTotalPerSec_Type = Integer32
_WebproxysrvrSSLClientBytesTotalPerSec_Object = MibScalar
webproxysrvrSSLClientBytesTotalPerSec = _WebproxysrvrSSLClientBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 9),
    _WebproxysrvrSSLClientBytesTotalPerSec_Type()
)
webproxysrvrSSLClientBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSSLClientBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrSocksClientBytesSentPerSec_Type = Integer32
_WebproxysrvrSocksClientBytesSentPerSec_Object = MibScalar
webproxysrvrSocksClientBytesSentPerSec = _WebproxysrvrSocksClientBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 10),
    _WebproxysrvrSocksClientBytesSentPerSec_Type()
)
webproxysrvrSocksClientBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSocksClientBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrSocksClientBytesReceivedPerSec_Type = Integer32
_WebproxysrvrSocksClientBytesReceivedPerSec_Object = MibScalar
webproxysrvrSocksClientBytesReceivedPerSec = _WebproxysrvrSocksClientBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 11),
    _WebproxysrvrSocksClientBytesReceivedPerSec_Type()
)
webproxysrvrSocksClientBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSocksClientBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrSocksClientBytesTotalPerSec_Type = Integer32
_WebproxysrvrSocksClientBytesTotalPerSec_Object = MibScalar
webproxysrvrSocksClientBytesTotalPerSec = _WebproxysrvrSocksClientBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 12),
    _WebproxysrvrSocksClientBytesTotalPerSec_Type()
)
webproxysrvrSocksClientBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSocksClientBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrCurrentUsers_Type = Integer32
_WebproxysrvrCurrentUsers_Object = MibScalar
webproxysrvrCurrentUsers = _WebproxysrvrCurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 13),
    _WebproxysrvrCurrentUsers_Type()
)
webproxysrvrCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrCurrentUsers.setStatus("mandatory")
_WebproxysrvrTotalUsers_Type = Integer32
_WebproxysrvrTotalUsers_Object = MibScalar
webproxysrvrTotalUsers = _WebproxysrvrTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 14),
    _WebproxysrvrTotalUsers_Type()
)
webproxysrvrTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalUsers.setStatus("mandatory")
_WebproxysrvrMaximumUsers_Type = Integer32
_WebproxysrvrMaximumUsers_Object = MibScalar
webproxysrvrMaximumUsers = _WebproxysrvrMaximumUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 15),
    _WebproxysrvrMaximumUsers_Type()
)
webproxysrvrMaximumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrMaximumUsers.setStatus("mandatory")
_WebproxysrvrFtpRequests_Type = Integer32
_WebproxysrvrFtpRequests_Object = MibScalar
webproxysrvrFtpRequests = _WebproxysrvrFtpRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 16),
    _WebproxysrvrFtpRequests_Type()
)
webproxysrvrFtpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrFtpRequests.setStatus("mandatory")
_WebproxysrvrGopherRequests_Type = Integer32
_WebproxysrvrGopherRequests_Object = MibScalar
webproxysrvrGopherRequests = _WebproxysrvrGopherRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 17),
    _WebproxysrvrGopherRequests_Type()
)
webproxysrvrGopherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrGopherRequests.setStatus("mandatory")
_WebproxysrvrHttpRequests_Type = Integer32
_WebproxysrvrHttpRequests_Object = MibScalar
webproxysrvrHttpRequests = _WebproxysrvrHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 18),
    _WebproxysrvrHttpRequests_Type()
)
webproxysrvrHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrHttpRequests.setStatus("mandatory")
_WebproxysrvrTotalRequests_Type = Integer32
_WebproxysrvrTotalRequests_Object = MibScalar
webproxysrvrTotalRequests = _WebproxysrvrTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 19),
    _WebproxysrvrTotalRequests_Type()
)
webproxysrvrTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalRequests.setStatus("mandatory")
_WebproxysrvrTotalSuccessfulRequests_Type = Integer32
_WebproxysrvrTotalSuccessfulRequests_Object = MibScalar
webproxysrvrTotalSuccessfulRequests = _WebproxysrvrTotalSuccessfulRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 20),
    _WebproxysrvrTotalSuccessfulRequests_Type()
)
webproxysrvrTotalSuccessfulRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalSuccessfulRequests.setStatus("mandatory")
_WebproxysrvrTotalFailingRequests_Type = Integer32
_WebproxysrvrTotalFailingRequests_Object = MibScalar
webproxysrvrTotalFailingRequests = _WebproxysrvrTotalFailingRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 21),
    _WebproxysrvrTotalFailingRequests_Type()
)
webproxysrvrTotalFailingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalFailingRequests.setStatus("mandatory")
_WebproxysrvrTotalCacheFetches_Type = Integer32
_WebproxysrvrTotalCacheFetches_Object = MibScalar
webproxysrvrTotalCacheFetches = _WebproxysrvrTotalCacheFetches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 22),
    _WebproxysrvrTotalCacheFetches_Type()
)
webproxysrvrTotalCacheFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalCacheFetches.setStatus("mandatory")
_WebproxysrvrTotalUpstreamFetches_Type = Integer32
_WebproxysrvrTotalUpstreamFetches_Object = MibScalar
webproxysrvrTotalUpstreamFetches = _WebproxysrvrTotalUpstreamFetches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 23),
    _WebproxysrvrTotalUpstreamFetches_Type()
)
webproxysrvrTotalUpstreamFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalUpstreamFetches.setStatus("mandatory")
_WebproxysrvrCacheHitRatioPercent_Type = Integer32
_WebproxysrvrCacheHitRatioPercent_Object = MibScalar
webproxysrvrCacheHitRatioPercent = _WebproxysrvrCacheHitRatioPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 24),
    _WebproxysrvrCacheHitRatioPercent_Type()
)
webproxysrvrCacheHitRatioPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrCacheHitRatioPercent.setStatus("mandatory")
_WebproxysrvrSitesDenied_Type = Integer32
_WebproxysrvrSitesDenied_Object = MibScalar
webproxysrvrSitesDenied = _WebproxysrvrSitesDenied_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 25),
    _WebproxysrvrSitesDenied_Type()
)
webproxysrvrSitesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSitesDenied.setStatus("mandatory")
_WebproxysrvrSitesGranted_Type = Integer32
_WebproxysrvrSitesGranted_Object = MibScalar
webproxysrvrSitesGranted = _WebproxysrvrSitesGranted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 26),
    _WebproxysrvrSitesGranted_Type()
)
webproxysrvrSitesGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSitesGranted.setStatus("mandatory")
_WebproxysrvrDNSCacheEntries_Type = Integer32
_WebproxysrvrDNSCacheEntries_Object = MibScalar
webproxysrvrDNSCacheEntries = _WebproxysrvrDNSCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 27),
    _WebproxysrvrDNSCacheEntries_Type()
)
webproxysrvrDNSCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrDNSCacheEntries.setStatus("mandatory")
_WebproxysrvrDNSRetrievals_Type = Integer32
_WebproxysrvrDNSRetrievals_Object = MibScalar
webproxysrvrDNSRetrievals = _WebproxysrvrDNSRetrievals_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 28),
    _WebproxysrvrDNSRetrievals_Type()
)
webproxysrvrDNSRetrievals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrDNSRetrievals.setStatus("mandatory")
_WebproxysrvrDNSCacheFlushes_Type = Integer32
_WebproxysrvrDNSCacheFlushes_Object = MibScalar
webproxysrvrDNSCacheFlushes = _WebproxysrvrDNSCacheFlushes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 29),
    _WebproxysrvrDNSCacheFlushes_Type()
)
webproxysrvrDNSCacheFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrDNSCacheFlushes.setStatus("mandatory")
_WebproxysrvrDNSCacheHits_Type = Integer32
_WebproxysrvrDNSCacheHits_Object = MibScalar
webproxysrvrDNSCacheHits = _WebproxysrvrDNSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 30),
    _WebproxysrvrDNSCacheHits_Type()
)
webproxysrvrDNSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrDNSCacheHits.setStatus("mandatory")
_WebproxysrvrDNSCacheHitsPercent_Type = Integer32
_WebproxysrvrDNSCacheHitsPercent_Object = MibScalar
webproxysrvrDNSCacheHitsPercent = _WebproxysrvrDNSCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 31),
    _WebproxysrvrDNSCacheHitsPercent_Type()
)
webproxysrvrDNSCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrDNSCacheHitsPercent.setStatus("mandatory")
_WebproxysrvrHTTPSSessions_Type = Integer32
_WebproxysrvrHTTPSSessions_Object = MibScalar
webproxysrvrHTTPSSessions = _WebproxysrvrHTTPSSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 33),
    _WebproxysrvrHTTPSSessions_Type()
)
webproxysrvrHTTPSSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrHTTPSSessions.setStatus("mandatory")
_WebproxysrvrSNEWSSessions_Type = Integer32
_WebproxysrvrSNEWSSessions_Object = MibScalar
webproxysrvrSNEWSSessions = _WebproxysrvrSNEWSSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 34),
    _WebproxysrvrSNEWSSessions_Type()
)
webproxysrvrSNEWSSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSNEWSSessions.setStatus("mandatory")
_WebproxysrvrUnknownSSLSessions_Type = Integer32
_WebproxysrvrUnknownSSLSessions_Object = MibScalar
webproxysrvrUnknownSSLSessions = _WebproxysrvrUnknownSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 35),
    _WebproxysrvrUnknownSSLSessions_Type()
)
webproxysrvrUnknownSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrUnknownSSLSessions.setStatus("mandatory")
_WebproxysrvrTotalSSLSessions_Type = Integer32
_WebproxysrvrTotalSSLSessions_Object = MibScalar
webproxysrvrTotalSSLSessions = _WebproxysrvrTotalSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 36),
    _WebproxysrvrTotalSSLSessions_Type()
)
webproxysrvrTotalSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalSSLSessions.setStatus("mandatory")
_WebproxysrvrSocksSessions_Type = Integer32
_WebproxysrvrSocksSessions_Object = MibScalar
webproxysrvrSocksSessions = _WebproxysrvrSocksSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 37),
    _WebproxysrvrSocksSessions_Type()
)
webproxysrvrSocksSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSocksSessions.setStatus("mandatory")
_WebproxysrvrTotalSocksSessions_Type = Integer32
_WebproxysrvrTotalSocksSessions_Object = MibScalar
webproxysrvrTotalSocksSessions = _WebproxysrvrTotalSocksSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 38),
    _WebproxysrvrTotalSocksSessions_Type()
)
webproxysrvrTotalSocksSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalSocksSessions.setStatus("mandatory")
_WebproxysrvrTotalSuccessfulSocksSessions_Type = Integer32
_WebproxysrvrTotalSuccessfulSocksSessions_Object = MibScalar
webproxysrvrTotalSuccessfulSocksSessions = _WebproxysrvrTotalSuccessfulSocksSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 39),
    _WebproxysrvrTotalSuccessfulSocksSessions_Type()
)
webproxysrvrTotalSuccessfulSocksSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalSuccessfulSocksSessions.setStatus("mandatory")
_WebproxysrvrTotalFailedSocksSessions_Type = Integer32
_WebproxysrvrTotalFailedSocksSessions_Object = MibScalar
webproxysrvrTotalFailedSocksSessions = _WebproxysrvrTotalFailedSocksSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 40),
    _WebproxysrvrTotalFailedSocksSessions_Type()
)
webproxysrvrTotalFailedSocksSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalFailedSocksSessions.setStatus("mandatory")
_WebproxysrvrThreadPoolSize_Type = Integer32
_WebproxysrvrThreadPoolSize_Object = MibScalar
webproxysrvrThreadPoolSize = _WebproxysrvrThreadPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 41),
    _WebproxysrvrThreadPoolSize_Type()
)
webproxysrvrThreadPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrThreadPoolSize.setStatus("mandatory")
_WebproxysrvrThreadPoolFailures_Type = Integer32
_WebproxysrvrThreadPoolFailures_Object = MibScalar
webproxysrvrThreadPoolFailures = _WebproxysrvrThreadPoolFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 42),
    _WebproxysrvrThreadPoolFailures_Type()
)
webproxysrvrThreadPoolFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrThreadPoolFailures.setStatus("mandatory")
_WebproxysrvrSSLSessionsScavenged_Type = Integer32
_WebproxysrvrSSLSessionsScavenged_Object = MibScalar
webproxysrvrSSLSessionsScavenged = _WebproxysrvrSSLSessionsScavenged_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 43),
    _WebproxysrvrSSLSessionsScavenged_Type()
)
webproxysrvrSSLSessionsScavenged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrSSLSessionsScavenged.setStatus("mandatory")
_WebproxysrvrThreadPoolActiveSessions_Type = Integer32
_WebproxysrvrThreadPoolActiveSessions_Object = MibScalar
webproxysrvrThreadPoolActiveSessions = _WebproxysrvrThreadPoolActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 44),
    _WebproxysrvrThreadPoolActiveSessions_Type()
)
webproxysrvrThreadPoolActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrThreadPoolActiveSessions.setStatus("mandatory")
_WebproxysrvrArrayBytesSentPerSec_Type = Integer32
_WebproxysrvrArrayBytesSentPerSec_Object = MibScalar
webproxysrvrArrayBytesSentPerSec = _WebproxysrvrArrayBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 45),
    _WebproxysrvrArrayBytesSentPerSec_Type()
)
webproxysrvrArrayBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrArrayBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrArrayBytesReceivedPerSec_Type = Integer32
_WebproxysrvrArrayBytesReceivedPerSec_Object = MibScalar
webproxysrvrArrayBytesReceivedPerSec = _WebproxysrvrArrayBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 46),
    _WebproxysrvrArrayBytesReceivedPerSec_Type()
)
webproxysrvrArrayBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrArrayBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrArrayBytesTotalPerSec_Type = Integer32
_WebproxysrvrArrayBytesTotalPerSec_Object = MibScalar
webproxysrvrArrayBytesTotalPerSec = _WebproxysrvrArrayBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 47),
    _WebproxysrvrArrayBytesTotalPerSec_Type()
)
webproxysrvrArrayBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrArrayBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrTotalArrayFetches_Type = Integer32
_WebproxysrvrTotalArrayFetches_Object = MibScalar
webproxysrvrTotalArrayFetches = _WebproxysrvrTotalArrayFetches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 50),
    _WebproxysrvrTotalArrayFetches_Type()
)
webproxysrvrTotalArrayFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalArrayFetches.setStatus("mandatory")
_WebproxysrvrReverseBytesSentPerSec_Type = Integer32
_WebproxysrvrReverseBytesSentPerSec_Object = MibScalar
webproxysrvrReverseBytesSentPerSec = _WebproxysrvrReverseBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 51),
    _WebproxysrvrReverseBytesSentPerSec_Type()
)
webproxysrvrReverseBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrReverseBytesSentPerSec.setStatus("mandatory")
_WebproxysrvrReverseBytesReceivedPerSec_Type = Integer32
_WebproxysrvrReverseBytesReceivedPerSec_Object = MibScalar
webproxysrvrReverseBytesReceivedPerSec = _WebproxysrvrReverseBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 52),
    _WebproxysrvrReverseBytesReceivedPerSec_Type()
)
webproxysrvrReverseBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrReverseBytesReceivedPerSec.setStatus("mandatory")
_WebproxysrvrReverseBytesTotalPerSec_Type = Integer32
_WebproxysrvrReverseBytesTotalPerSec_Object = MibScalar
webproxysrvrReverseBytesTotalPerSec = _WebproxysrvrReverseBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 53),
    _WebproxysrvrReverseBytesTotalPerSec_Type()
)
webproxysrvrReverseBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrReverseBytesTotalPerSec.setStatus("mandatory")
_WebproxysrvrTotalReverseFetches_Type = Integer32
_WebproxysrvrTotalReverseFetches_Object = MibScalar
webproxysrvrTotalReverseFetches = _WebproxysrvrTotalReverseFetches_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 54),
    _WebproxysrvrTotalReverseFetches_Type()
)
webproxysrvrTotalReverseFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrTotalReverseFetches.setStatus("mandatory")
_WebproxysrvrRequestsPerSec_Type = Counter32
_WebproxysrvrRequestsPerSec_Object = MibScalar
webproxysrvrRequestsPerSec = _WebproxysrvrRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 55),
    _WebproxysrvrRequestsPerSec_Type()
)
webproxysrvrRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrRequestsPerSec.setStatus("mandatory")
_WebproxysrvrFailingRequestsPerSec_Type = Counter32
_WebproxysrvrFailingRequestsPerSec_Object = MibScalar
webproxysrvrFailingRequestsPerSec = _WebproxysrvrFailingRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 27, 56),
    _WebproxysrvrFailingRequestsPerSec_Type()
)
webproxysrvrFailingRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrFailingRequestsPerSec.setStatus("mandatory")
_WinSock_Proxy_Server_ObjectIdentity = ObjectIdentity
winSock_Proxy_Server = _WinSock_Proxy_Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28)
)
_WinsockproxysrvrSuccessfulDNSResolutions_Type = Integer32
_WinsockproxysrvrSuccessfulDNSResolutions_Object = MibScalar
winsockproxysrvrSuccessfulDNSResolutions = _WinsockproxysrvrSuccessfulDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 1),
    _WinsockproxysrvrSuccessfulDNSResolutions_Type()
)
winsockproxysrvrSuccessfulDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrSuccessfulDNSResolutions.setStatus("mandatory")
_WinsockproxysrvrFailedDNSResolutions_Type = Integer32
_WinsockproxysrvrFailedDNSResolutions_Object = MibScalar
winsockproxysrvrFailedDNSResolutions = _WinsockproxysrvrFailedDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 2),
    _WinsockproxysrvrFailedDNSResolutions_Type()
)
winsockproxysrvrFailedDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrFailedDNSResolutions.setStatus("mandatory")
_WinsockproxysrvrPendingDNSResolutions_Type = Integer32
_WinsockproxysrvrPendingDNSResolutions_Object = MibScalar
winsockproxysrvrPendingDNSResolutions = _WinsockproxysrvrPendingDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 3),
    _WinsockproxysrvrPendingDNSResolutions_Type()
)
winsockproxysrvrPendingDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrPendingDNSResolutions.setStatus("mandatory")
_WinsockproxysrvrActiveSessions_Type = Integer32
_WinsockproxysrvrActiveSessions_Object = MibScalar
winsockproxysrvrActiveSessions = _WinsockproxysrvrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 4),
    _WinsockproxysrvrActiveSessions_Type()
)
winsockproxysrvrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrActiveSessions.setStatus("mandatory")
_WinsockproxysrvrActiveTCPConnections_Type = Integer32
_WinsockproxysrvrActiveTCPConnections_Object = MibScalar
winsockproxysrvrActiveTCPConnections = _WinsockproxysrvrActiveTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 5),
    _WinsockproxysrvrActiveTCPConnections_Type()
)
winsockproxysrvrActiveTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrActiveTCPConnections.setStatus("mandatory")
_WinsockproxysrvrActiveUDPConnections_Type = Integer32
_WinsockproxysrvrActiveUDPConnections_Object = MibScalar
winsockproxysrvrActiveUDPConnections = _WinsockproxysrvrActiveUDPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 6),
    _WinsockproxysrvrActiveUDPConnections_Type()
)
winsockproxysrvrActiveUDPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrActiveUDPConnections.setStatus("mandatory")
_WinsockproxysrvrConnectingTCPConnections_Type = Integer32
_WinsockproxysrvrConnectingTCPConnections_Object = MibScalar
winsockproxysrvrConnectingTCPConnections = _WinsockproxysrvrConnectingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 7),
    _WinsockproxysrvrConnectingTCPConnections_Type()
)
winsockproxysrvrConnectingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrConnectingTCPConnections.setStatus("mandatory")
_WinsockproxysrvrBack_ConnectingTCPConnections_Type = Integer32
_WinsockproxysrvrBack_ConnectingTCPConnections_Object = MibScalar
winsockproxysrvrBack_ConnectingTCPConnections = _WinsockproxysrvrBack_ConnectingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 8),
    _WinsockproxysrvrBack_ConnectingTCPConnections_Type()
)
winsockproxysrvrBack_ConnectingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrBack_ConnectingTCPConnections.setStatus("mandatory")
_WinsockproxysrvrAcceptingTCPConnections_Type = Integer32
_WinsockproxysrvrAcceptingTCPConnections_Object = MibScalar
winsockproxysrvrAcceptingTCPConnections = _WinsockproxysrvrAcceptingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 9),
    _WinsockproxysrvrAcceptingTCPConnections_Type()
)
winsockproxysrvrAcceptingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrAcceptingTCPConnections.setStatus("mandatory")
_WinsockproxysrvrListeningTCPConnections_Type = Integer32
_WinsockproxysrvrListeningTCPConnections_Object = MibScalar
winsockproxysrvrListeningTCPConnections = _WinsockproxysrvrListeningTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 10),
    _WinsockproxysrvrListeningTCPConnections_Type()
)
winsockproxysrvrListeningTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrListeningTCPConnections.setStatus("mandatory")
_WinsockproxysrvrWorkerThreads_Type = Integer32
_WinsockproxysrvrWorkerThreads_Object = MibScalar
winsockproxysrvrWorkerThreads = _WinsockproxysrvrWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 11),
    _WinsockproxysrvrWorkerThreads_Type()
)
winsockproxysrvrWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrWorkerThreads.setStatus("mandatory")
_WinsockproxysrvrAvailableWorkerThreads_Type = Integer32
_WinsockproxysrvrAvailableWorkerThreads_Object = MibScalar
winsockproxysrvrAvailableWorkerThreads = _WinsockproxysrvrAvailableWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 12),
    _WinsockproxysrvrAvailableWorkerThreads_Type()
)
winsockproxysrvrAvailableWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrAvailableWorkerThreads.setStatus("mandatory")
_WinsockproxysrvrBytesReadPerSec_Type = Counter32
_WinsockproxysrvrBytesReadPerSec_Object = MibScalar
winsockproxysrvrBytesReadPerSec = _WinsockproxysrvrBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 13),
    _WinsockproxysrvrBytesReadPerSec_Type()
)
winsockproxysrvrBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrBytesReadPerSec.setStatus("mandatory")
_WinsockproxysrvrBytesWrittenPerSec_Type = Counter32
_WinsockproxysrvrBytesWrittenPerSec_Object = MibScalar
winsockproxysrvrBytesWrittenPerSec = _WinsockproxysrvrBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 14),
    _WinsockproxysrvrBytesWrittenPerSec_Type()
)
winsockproxysrvrBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrBytesWrittenPerSec.setStatus("mandatory")
_WinsockproxysrvrNon_connectedUDPMappings_Type = Integer32
_WinsockproxysrvrNon_connectedUDPMappings_Object = MibScalar
winsockproxysrvrNon_connectedUDPMappings = _WinsockproxysrvrNon_connectedUDPMappings_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 15),
    _WinsockproxysrvrNon_connectedUDPMappings_Type()
)
winsockproxysrvrNon_connectedUDPMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrNon_connectedUDPMappings.setStatus("mandatory")
_WinsockproxysrvrDNSCacheEntries_Type = Integer32
_WinsockproxysrvrDNSCacheEntries_Object = MibScalar
winsockproxysrvrDNSCacheEntries = _WinsockproxysrvrDNSCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 16),
    _WinsockproxysrvrDNSCacheEntries_Type()
)
winsockproxysrvrDNSCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrDNSCacheEntries.setStatus("mandatory")
_WinsockproxysrvrDNSCacheHits_Type = Integer32
_WinsockproxysrvrDNSCacheHits_Object = MibScalar
winsockproxysrvrDNSCacheHits = _WinsockproxysrvrDNSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 17),
    _WinsockproxysrvrDNSCacheHits_Type()
)
winsockproxysrvrDNSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrDNSCacheHits.setStatus("mandatory")
_WinsockproxysrvrDNSCacheFlushes_Type = Integer32
_WinsockproxysrvrDNSCacheFlushes_Object = MibScalar
winsockproxysrvrDNSCacheFlushes = _WinsockproxysrvrDNSCacheFlushes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 18),
    _WinsockproxysrvrDNSCacheFlushes_Type()
)
winsockproxysrvrDNSCacheFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrDNSCacheFlushes.setStatus("mandatory")
_WinsockproxysrvrDNSRetrievals_Type = Integer32
_WinsockproxysrvrDNSRetrievals_Object = MibScalar
winsockproxysrvrDNSRetrievals = _WinsockproxysrvrDNSRetrievals_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 19),
    _WinsockproxysrvrDNSRetrievals_Type()
)
winsockproxysrvrDNSRetrievals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrDNSRetrievals.setStatus("mandatory")
_WinsockproxysrvrDNSCacheHitsPercent_Type = Integer32
_WinsockproxysrvrDNSCacheHitsPercent_Object = MibScalar
winsockproxysrvrDNSCacheHitsPercent = _WinsockproxysrvrDNSCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 28, 20),
    _WinsockproxysrvrDNSCacheHitsPercent_Type()
)
winsockproxysrvrDNSCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winsockproxysrvrDNSCacheHitsPercent.setStatus("mandatory")
_Web_Proxy_Server_Cache_ObjectIdentity = ObjectIdentity
web_Proxy_Server_Cache = _Web_Proxy_Server_Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29)
)
_WebproxysrvrcacheURLsInCache_Type = Counter32
_WebproxysrvrcacheURLsInCache_Object = MibScalar
webproxysrvrcacheURLsInCache = _WebproxysrvrcacheURLsInCache_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 1),
    _WebproxysrvrcacheURLsInCache_Type()
)
webproxysrvrcacheURLsInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheURLsInCache.setStatus("mandatory")
_WebproxysrvrcacheBytesInCache_Type = Counter32
_WebproxysrvrcacheBytesInCache_Object = MibScalar
webproxysrvrcacheBytesInCache = _WebproxysrvrcacheBytesInCache_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 2),
    _WebproxysrvrcacheBytesInCache_Type()
)
webproxysrvrcacheBytesInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheBytesInCache.setStatus("mandatory")
_WebproxysrvrcacheTotalBytesCached_Type = Counter32
_WebproxysrvrcacheTotalBytesCached_Object = MibScalar
webproxysrvrcacheTotalBytesCached = _WebproxysrvrcacheTotalBytesCached_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 3),
    _WebproxysrvrcacheTotalBytesCached_Type()
)
webproxysrvrcacheTotalBytesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalBytesCached.setStatus("mandatory")
_WebproxysrvrcacheTotalBytesRetrieved_Type = Counter32
_WebproxysrvrcacheTotalBytesRetrieved_Object = MibScalar
webproxysrvrcacheTotalBytesRetrieved = _WebproxysrvrcacheTotalBytesRetrieved_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 4),
    _WebproxysrvrcacheTotalBytesRetrieved_Type()
)
webproxysrvrcacheTotalBytesRetrieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalBytesRetrieved.setStatus("mandatory")
_WebproxysrvrcacheTotalURLsCached_Type = Counter32
_WebproxysrvrcacheTotalURLsCached_Object = MibScalar
webproxysrvrcacheTotalURLsCached = _WebproxysrvrcacheTotalURLsCached_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 5),
    _WebproxysrvrcacheTotalURLsCached_Type()
)
webproxysrvrcacheTotalURLsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalURLsCached.setStatus("mandatory")
_WebproxysrvrcacheTotalURLsRetrieved_Type = Counter32
_WebproxysrvrcacheTotalURLsRetrieved_Object = MibScalar
webproxysrvrcacheTotalURLsRetrieved = _WebproxysrvrcacheTotalURLsRetrieved_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 6),
    _WebproxysrvrcacheTotalURLsRetrieved_Type()
)
webproxysrvrcacheTotalURLsRetrieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalURLsRetrieved.setStatus("mandatory")
_WebproxysrvrcacheMaxBytesCached_Type = Counter32
_WebproxysrvrcacheMaxBytesCached_Object = MibScalar
webproxysrvrcacheMaxBytesCached = _WebproxysrvrcacheMaxBytesCached_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 7),
    _WebproxysrvrcacheMaxBytesCached_Type()
)
webproxysrvrcacheMaxBytesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheMaxBytesCached.setStatus("mandatory")
_WebproxysrvrcacheMaxURLsCached_Type = Counter32
_WebproxysrvrcacheMaxURLsCached_Object = MibScalar
webproxysrvrcacheMaxURLsCached = _WebproxysrvrcacheMaxURLsCached_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 8),
    _WebproxysrvrcacheMaxURLsCached_Type()
)
webproxysrvrcacheMaxURLsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheMaxURLsCached.setStatus("mandatory")
_WebproxysrvrcacheTotalActivelyRefreshedURLs_Type = Counter32
_WebproxysrvrcacheTotalActivelyRefreshedURLs_Object = MibScalar
webproxysrvrcacheTotalActivelyRefreshedURLs = _WebproxysrvrcacheTotalActivelyRefreshedURLs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 9),
    _WebproxysrvrcacheTotalActivelyRefreshedURLs_Type()
)
webproxysrvrcacheTotalActivelyRefreshedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalActivelyRefreshedURLs.setStatus("mandatory")
_WebproxysrvrcacheTotalBytesActivelyRefreshed_Type = Counter32
_WebproxysrvrcacheTotalBytesActivelyRefreshed_Object = MibScalar
webproxysrvrcacheTotalBytesActivelyRefreshed = _WebproxysrvrcacheTotalBytesActivelyRefreshed_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 10),
    _WebproxysrvrcacheTotalBytesActivelyRefreshed_Type()
)
webproxysrvrcacheTotalBytesActivelyRefreshed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheTotalBytesActivelyRefreshed.setStatus("mandatory")
_WebproxysrvrcacheURLRetrieveRate_Type = Counter32
_WebproxysrvrcacheURLRetrieveRate_Object = MibScalar
webproxysrvrcacheURLRetrieveRate = _WebproxysrvrcacheURLRetrieveRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 11),
    _WebproxysrvrcacheURLRetrieveRate_Type()
)
webproxysrvrcacheURLRetrieveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheURLRetrieveRate.setStatus("mandatory")
_WebproxysrvrcacheBytesRetrievedRate_Type = Counter32
_WebproxysrvrcacheBytesRetrievedRate_Object = MibScalar
webproxysrvrcacheBytesRetrievedRate = _WebproxysrvrcacheBytesRetrievedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 12),
    _WebproxysrvrcacheBytesRetrievedRate_Type()
)
webproxysrvrcacheBytesRetrievedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheBytesRetrievedRate.setStatus("mandatory")
_WebproxysrvrcacheURLCommitRate_Type = Counter32
_WebproxysrvrcacheURLCommitRate_Object = MibScalar
webproxysrvrcacheURLCommitRate = _WebproxysrvrcacheURLCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 13),
    _WebproxysrvrcacheURLCommitRate_Type()
)
webproxysrvrcacheURLCommitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheURLCommitRate.setStatus("mandatory")
_WebproxysrvrcacheBytesCommitedRate_Type = Counter32
_WebproxysrvrcacheBytesCommitedRate_Object = MibScalar
webproxysrvrcacheBytesCommitedRate = _WebproxysrvrcacheBytesCommitedRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 14),
    _WebproxysrvrcacheBytesCommitedRate_Type()
)
webproxysrvrcacheBytesCommitedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheBytesCommitedRate.setStatus("mandatory")
_WebproxysrvrcacheActiveURLRefreshRate_Type = Counter32
_WebproxysrvrcacheActiveURLRefreshRate_Object = MibScalar
webproxysrvrcacheActiveURLRefreshRate = _WebproxysrvrcacheActiveURLRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 15),
    _WebproxysrvrcacheActiveURLRefreshRate_Type()
)
webproxysrvrcacheActiveURLRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheActiveURLRefreshRate.setStatus("mandatory")
_WebproxysrvrcacheActiveRefreshBytesRate_Type = Counter32
_WebproxysrvrcacheActiveRefreshBytesRate_Object = MibScalar
webproxysrvrcacheActiveRefreshBytesRate = _WebproxysrvrcacheActiveRefreshBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 29, 16),
    _WebproxysrvrcacheActiveRefreshBytesRate_Type()
)
webproxysrvrcacheActiveRefreshBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webproxysrvrcacheActiveRefreshBytesRate.setStatus("mandatory")
_Telephony_ObjectIdentity = ObjectIdentity
telephony = _Telephony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30)
)
_TelephonyLines_Type = Integer32
_TelephonyLines_Object = MibScalar
telephonyLines = _TelephonyLines_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 1),
    _TelephonyLines_Type()
)
telephonyLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyLines.setStatus("mandatory")
_TelephonyTelephoneDevices_Type = Integer32
_TelephonyTelephoneDevices_Object = MibScalar
telephonyTelephoneDevices = _TelephonyTelephoneDevices_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 2),
    _TelephonyTelephoneDevices_Type()
)
telephonyTelephoneDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyTelephoneDevices.setStatus("mandatory")
_TelephonyActiveLines_Type = Integer32
_TelephonyActiveLines_Object = MibScalar
telephonyActiveLines = _TelephonyActiveLines_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 3),
    _TelephonyActiveLines_Type()
)
telephonyActiveLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyActiveLines.setStatus("mandatory")
_TelephonyActiveTelephones_Type = Integer32
_TelephonyActiveTelephones_Object = MibScalar
telephonyActiveTelephones = _TelephonyActiveTelephones_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 4),
    _TelephonyActiveTelephones_Type()
)
telephonyActiveTelephones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyActiveTelephones.setStatus("mandatory")
_TelephonyOutgoingCallsPerSec_Type = Counter32
_TelephonyOutgoingCallsPerSec_Object = MibScalar
telephonyOutgoingCallsPerSec = _TelephonyOutgoingCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 5),
    _TelephonyOutgoingCallsPerSec_Type()
)
telephonyOutgoingCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyOutgoingCallsPerSec.setStatus("mandatory")
_TelephonyIncomingCallsPerSec_Type = Counter32
_TelephonyIncomingCallsPerSec_Object = MibScalar
telephonyIncomingCallsPerSec = _TelephonyIncomingCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 6),
    _TelephonyIncomingCallsPerSec_Type()
)
telephonyIncomingCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyIncomingCallsPerSec.setStatus("mandatory")
_TelephonyClientApps_Type = Integer32
_TelephonyClientApps_Object = MibScalar
telephonyClientApps = _TelephonyClientApps_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 7),
    _TelephonyClientApps_Type()
)
telephonyClientApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyClientApps.setStatus("mandatory")
_TelephonyCurrentOutgoingCalls_Type = Integer32
_TelephonyCurrentOutgoingCalls_Object = MibScalar
telephonyCurrentOutgoingCalls = _TelephonyCurrentOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 8),
    _TelephonyCurrentOutgoingCalls_Type()
)
telephonyCurrentOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyCurrentOutgoingCalls.setStatus("mandatory")
_TelephonyCurrentIncomingCalls_Type = Integer32
_TelephonyCurrentIncomingCalls_Object = MibScalar
telephonyCurrentIncomingCalls = _TelephonyCurrentIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 30, 9),
    _TelephonyCurrentIncomingCalls_Type()
)
telephonyCurrentIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyCurrentIncomingCalls.setStatus("mandatory")
_RasportrAS_PortTable_Object = MibTable
rasportrAS_PortTable = _RasportrAS_PortTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31)
)
if mibBuilder.loadTexts:
    rasportrAS_PortTable.setStatus("mandatory")
_RasportrAS_PortEntry_Object = MibTableRow
rasportrAS_PortEntry = _RasportrAS_PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1)
)
rasportrAS_PortEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "rasportrAS-PortIndex"),
)
if mibBuilder.loadTexts:
    rasportrAS_PortEntry.setStatus("mandatory")
_RasportrAS_PortIndex_Type = Integer32
_RasportrAS_PortIndex_Object = MibScalar
rasportrAS_PortIndex = _RasportrAS_PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 1),
    _RasportrAS_PortIndex_Type()
)
rasportrAS_PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportrAS_PortIndex.setStatus("mandatory")
_RasportrAS_PortInstance_Type = DisplayString
_RasportrAS_PortInstance_Object = MibScalar
rasportrAS_PortInstance = _RasportrAS_PortInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 2),
    _RasportrAS_PortInstance_Type()
)
rasportrAS_PortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportrAS_PortInstance.setStatus("mandatory")
_RasportBytesTransmitted_Type = Integer32
_RasportBytesTransmitted_Object = MibTableColumn
rasportBytesTransmitted = _RasportBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 3),
    _RasportBytesTransmitted_Type()
)
rasportBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportBytesTransmitted.setStatus("mandatory")
_RasportBytesReceived_Type = Integer32
_RasportBytesReceived_Object = MibTableColumn
rasportBytesReceived = _RasportBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 4),
    _RasportBytesReceived_Type()
)
rasportBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportBytesReceived.setStatus("mandatory")
_RasportFramesTransmitted_Type = Integer32
_RasportFramesTransmitted_Object = MibTableColumn
rasportFramesTransmitted = _RasportFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 5),
    _RasportFramesTransmitted_Type()
)
rasportFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportFramesTransmitted.setStatus("mandatory")
_RasportFramesReceived_Type = Integer32
_RasportFramesReceived_Object = MibTableColumn
rasportFramesReceived = _RasportFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 6),
    _RasportFramesReceived_Type()
)
rasportFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportFramesReceived.setStatus("mandatory")
_RasportPercentCompressionOut_Type = Integer32
_RasportPercentCompressionOut_Object = MibTableColumn
rasportPercentCompressionOut = _RasportPercentCompressionOut_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 7),
    _RasportPercentCompressionOut_Type()
)
rasportPercentCompressionOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportPercentCompressionOut.setStatus("mandatory")
_RasportPercentCompressionIn_Type = Integer32
_RasportPercentCompressionIn_Object = MibTableColumn
rasportPercentCompressionIn = _RasportPercentCompressionIn_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 8),
    _RasportPercentCompressionIn_Type()
)
rasportPercentCompressionIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportPercentCompressionIn.setStatus("mandatory")
_RasportCRCErrors_Type = Integer32
_RasportCRCErrors_Object = MibTableColumn
rasportCRCErrors = _RasportCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 9),
    _RasportCRCErrors_Type()
)
rasportCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportCRCErrors.setStatus("mandatory")
_RasportTimeoutErrors_Type = Integer32
_RasportTimeoutErrors_Object = MibTableColumn
rasportTimeoutErrors = _RasportTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 10),
    _RasportTimeoutErrors_Type()
)
rasportTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportTimeoutErrors.setStatus("mandatory")
_RasportSerialOverrunErrors_Type = Integer32
_RasportSerialOverrunErrors_Object = MibTableColumn
rasportSerialOverrunErrors = _RasportSerialOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 11),
    _RasportSerialOverrunErrors_Type()
)
rasportSerialOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportSerialOverrunErrors.setStatus("mandatory")
_RasportAlignmentErrors_Type = Integer32
_RasportAlignmentErrors_Object = MibTableColumn
rasportAlignmentErrors = _RasportAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 12),
    _RasportAlignmentErrors_Type()
)
rasportAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportAlignmentErrors.setStatus("mandatory")
_RasportBufferOverrunErrors_Type = Integer32
_RasportBufferOverrunErrors_Object = MibTableColumn
rasportBufferOverrunErrors = _RasportBufferOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 13),
    _RasportBufferOverrunErrors_Type()
)
rasportBufferOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportBufferOverrunErrors.setStatus("mandatory")
_RasportTotalErrors_Type = Integer32
_RasportTotalErrors_Object = MibTableColumn
rasportTotalErrors = _RasportTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 14),
    _RasportTotalErrors_Type()
)
rasportTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportTotalErrors.setStatus("mandatory")
_RasportBytesTransmittedPerSec_Type = Counter32
_RasportBytesTransmittedPerSec_Object = MibTableColumn
rasportBytesTransmittedPerSec = _RasportBytesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 15),
    _RasportBytesTransmittedPerSec_Type()
)
rasportBytesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportBytesTransmittedPerSec.setStatus("mandatory")
_RasportBytesReceivedPerSec_Type = Counter32
_RasportBytesReceivedPerSec_Object = MibTableColumn
rasportBytesReceivedPerSec = _RasportBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 16),
    _RasportBytesReceivedPerSec_Type()
)
rasportBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportBytesReceivedPerSec.setStatus("mandatory")
_RasportFramesTransmittedPerSec_Type = Counter32
_RasportFramesTransmittedPerSec_Object = MibTableColumn
rasportFramesTransmittedPerSec = _RasportFramesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 17),
    _RasportFramesTransmittedPerSec_Type()
)
rasportFramesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportFramesTransmittedPerSec.setStatus("mandatory")
_RasportFramesReceivedPerSec_Type = Counter32
_RasportFramesReceivedPerSec_Object = MibTableColumn
rasportFramesReceivedPerSec = _RasportFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 18),
    _RasportFramesReceivedPerSec_Type()
)
rasportFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportFramesReceivedPerSec.setStatus("mandatory")
_RasportTotalErrorsPerSec_Type = Counter32
_RasportTotalErrorsPerSec_Object = MibTableColumn
rasportTotalErrorsPerSec = _RasportTotalErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 31, 1, 19),
    _RasportTotalErrorsPerSec_Type()
)
rasportTotalErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasportTotalErrorsPerSec.setStatus("mandatory")
_NwnetbiosnWLink_NetBIOSTable_Object = MibTable
nwnetbiosnWLink_NetBIOSTable = _NwnetbiosnWLink_NetBIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32)
)
if mibBuilder.loadTexts:
    nwnetbiosnWLink_NetBIOSTable.setStatus("mandatory")
_NwnetbiosnWLink_NetBIOSEntry_Object = MibTableRow
nwnetbiosnWLink_NetBIOSEntry = _NwnetbiosnWLink_NetBIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1)
)
nwnetbiosnWLink_NetBIOSEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "nwnetbiosnWLink-NetBIOSIndex"),
)
if mibBuilder.loadTexts:
    nwnetbiosnWLink_NetBIOSEntry.setStatus("mandatory")
_NwnetbiosnWLink_NetBIOSIndex_Type = Integer32
_NwnetbiosnWLink_NetBIOSIndex_Object = MibScalar
nwnetbiosnWLink_NetBIOSIndex = _NwnetbiosnWLink_NetBIOSIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 1),
    _NwnetbiosnWLink_NetBIOSIndex_Type()
)
nwnetbiosnWLink_NetBIOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosnWLink_NetBIOSIndex.setStatus("mandatory")
_NwnetbiosnWLink_NetBIOSInstance_Type = DisplayString
_NwnetbiosnWLink_NetBIOSInstance_Object = MibScalar
nwnetbiosnWLink_NetBIOSInstance = _NwnetbiosnWLink_NetBIOSInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 2),
    _NwnetbiosnWLink_NetBIOSInstance_Type()
)
nwnetbiosnWLink_NetBIOSInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosnWLink_NetBIOSInstance.setStatus("mandatory")
_NwnetbiosDatagramsPerSec_Type = Counter32
_NwnetbiosDatagramsPerSec_Object = MibTableColumn
nwnetbiosDatagramsPerSec = _NwnetbiosDatagramsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 3),
    _NwnetbiosDatagramsPerSec_Type()
)
nwnetbiosDatagramsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramsPerSec.setStatus("mandatory")
_NwnetbiosDatagramBytesPerSec_Type = Integer32
_NwnetbiosDatagramBytesPerSec_Object = MibTableColumn
nwnetbiosDatagramBytesPerSec = _NwnetbiosDatagramBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 4),
    _NwnetbiosDatagramBytesPerSec_Type()
)
nwnetbiosDatagramBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramBytesPerSec.setStatus("mandatory")
_NwnetbiosPacketsPerSec_Type = Counter32
_NwnetbiosPacketsPerSec_Object = MibTableColumn
nwnetbiosPacketsPerSec = _NwnetbiosPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 5),
    _NwnetbiosPacketsPerSec_Type()
)
nwnetbiosPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosPacketsPerSec.setStatus("mandatory")
_NwnetbiosFramesPerSec_Type = Counter32
_NwnetbiosFramesPerSec_Object = MibTableColumn
nwnetbiosFramesPerSec = _NwnetbiosFramesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 6),
    _NwnetbiosFramesPerSec_Type()
)
nwnetbiosFramesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFramesPerSec.setStatus("mandatory")
_NwnetbiosFrameBytesPerSec_Type = Integer32
_NwnetbiosFrameBytesPerSec_Object = MibTableColumn
nwnetbiosFrameBytesPerSec = _NwnetbiosFrameBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 7),
    _NwnetbiosFrameBytesPerSec_Type()
)
nwnetbiosFrameBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFrameBytesPerSec.setStatus("mandatory")
_NwnetbiosBytesTotalPerSec_Type = Integer32
_NwnetbiosBytesTotalPerSec_Object = MibTableColumn
nwnetbiosBytesTotalPerSec = _NwnetbiosBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 8),
    _NwnetbiosBytesTotalPerSec_Type()
)
nwnetbiosBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosBytesTotalPerSec.setStatus("mandatory")
_NwnetbiosConnectionsOpen_Type = Integer32
_NwnetbiosConnectionsOpen_Object = MibTableColumn
nwnetbiosConnectionsOpen = _NwnetbiosConnectionsOpen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 9),
    _NwnetbiosConnectionsOpen_Type()
)
nwnetbiosConnectionsOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosConnectionsOpen.setStatus("mandatory")
_NwnetbiosConnectionsNoRetries_Type = Integer32
_NwnetbiosConnectionsNoRetries_Object = MibTableColumn
nwnetbiosConnectionsNoRetries = _NwnetbiosConnectionsNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 10),
    _NwnetbiosConnectionsNoRetries_Type()
)
nwnetbiosConnectionsNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosConnectionsNoRetries.setStatus("mandatory")
_NwnetbiosConnectionsWithRetries_Type = Integer32
_NwnetbiosConnectionsWithRetries_Object = MibTableColumn
nwnetbiosConnectionsWithRetries = _NwnetbiosConnectionsWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 11),
    _NwnetbiosConnectionsWithRetries_Type()
)
nwnetbiosConnectionsWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosConnectionsWithRetries.setStatus("mandatory")
_NwnetbiosDisconnectsLocal_Type = Integer32
_NwnetbiosDisconnectsLocal_Object = MibTableColumn
nwnetbiosDisconnectsLocal = _NwnetbiosDisconnectsLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 12),
    _NwnetbiosDisconnectsLocal_Type()
)
nwnetbiosDisconnectsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDisconnectsLocal.setStatus("mandatory")
_NwnetbiosDisconnectsRemote_Type = Integer32
_NwnetbiosDisconnectsRemote_Object = MibTableColumn
nwnetbiosDisconnectsRemote = _NwnetbiosDisconnectsRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 13),
    _NwnetbiosDisconnectsRemote_Type()
)
nwnetbiosDisconnectsRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDisconnectsRemote.setStatus("mandatory")
_NwnetbiosFailuresLink_Type = Integer32
_NwnetbiosFailuresLink_Object = MibTableColumn
nwnetbiosFailuresLink = _NwnetbiosFailuresLink_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 14),
    _NwnetbiosFailuresLink_Type()
)
nwnetbiosFailuresLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresLink.setStatus("mandatory")
_NwnetbiosFailuresAdapter_Type = Integer32
_NwnetbiosFailuresAdapter_Object = MibTableColumn
nwnetbiosFailuresAdapter = _NwnetbiosFailuresAdapter_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 15),
    _NwnetbiosFailuresAdapter_Type()
)
nwnetbiosFailuresAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresAdapter.setStatus("mandatory")
_NwnetbiosConnectionSessionTimeouts_Type = Integer32
_NwnetbiosConnectionSessionTimeouts_Object = MibTableColumn
nwnetbiosConnectionSessionTimeouts = _NwnetbiosConnectionSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 16),
    _NwnetbiosConnectionSessionTimeouts_Type()
)
nwnetbiosConnectionSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosConnectionSessionTimeouts.setStatus("mandatory")
_NwnetbiosConnectionsCanceled_Type = Integer32
_NwnetbiosConnectionsCanceled_Object = MibTableColumn
nwnetbiosConnectionsCanceled = _NwnetbiosConnectionsCanceled_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 17),
    _NwnetbiosConnectionsCanceled_Type()
)
nwnetbiosConnectionsCanceled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosConnectionsCanceled.setStatus("mandatory")
_NwnetbiosFailuresResourceRemote_Type = Integer32
_NwnetbiosFailuresResourceRemote_Object = MibTableColumn
nwnetbiosFailuresResourceRemote = _NwnetbiosFailuresResourceRemote_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 18),
    _NwnetbiosFailuresResourceRemote_Type()
)
nwnetbiosFailuresResourceRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresResourceRemote.setStatus("mandatory")
_NwnetbiosFailuresResourceLocal_Type = Integer32
_NwnetbiosFailuresResourceLocal_Object = MibTableColumn
nwnetbiosFailuresResourceLocal = _NwnetbiosFailuresResourceLocal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 19),
    _NwnetbiosFailuresResourceLocal_Type()
)
nwnetbiosFailuresResourceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresResourceLocal.setStatus("mandatory")
_NwnetbiosFailuresNotFound_Type = Integer32
_NwnetbiosFailuresNotFound_Object = MibTableColumn
nwnetbiosFailuresNotFound = _NwnetbiosFailuresNotFound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 20),
    _NwnetbiosFailuresNotFound_Type()
)
nwnetbiosFailuresNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresNotFound.setStatus("mandatory")
_NwnetbiosFailuresNoListen_Type = Integer32
_NwnetbiosFailuresNoListen_Object = MibTableColumn
nwnetbiosFailuresNoListen = _NwnetbiosFailuresNoListen_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 21),
    _NwnetbiosFailuresNoListen_Type()
)
nwnetbiosFailuresNoListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFailuresNoListen.setStatus("mandatory")
_NwnetbiosDatagramsSentPerSec_Type = Counter32
_NwnetbiosDatagramsSentPerSec_Object = MibTableColumn
nwnetbiosDatagramsSentPerSec = _NwnetbiosDatagramsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 22),
    _NwnetbiosDatagramsSentPerSec_Type()
)
nwnetbiosDatagramsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramsSentPerSec.setStatus("mandatory")
_NwnetbiosDatagramBytesSentPerSec_Type = Integer32
_NwnetbiosDatagramBytesSentPerSec_Object = MibTableColumn
nwnetbiosDatagramBytesSentPerSec = _NwnetbiosDatagramBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 23),
    _NwnetbiosDatagramBytesSentPerSec_Type()
)
nwnetbiosDatagramBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramBytesSentPerSec.setStatus("mandatory")
_NwnetbiosDatagramsReceivedPerSec_Type = Counter32
_NwnetbiosDatagramsReceivedPerSec_Object = MibTableColumn
nwnetbiosDatagramsReceivedPerSec = _NwnetbiosDatagramsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 24),
    _NwnetbiosDatagramsReceivedPerSec_Type()
)
nwnetbiosDatagramsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramsReceivedPerSec.setStatus("mandatory")
_NwnetbiosDatagramBytesReceivedPerSec_Type = Integer32
_NwnetbiosDatagramBytesReceivedPerSec_Object = MibTableColumn
nwnetbiosDatagramBytesReceivedPerSec = _NwnetbiosDatagramBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 25),
    _NwnetbiosDatagramBytesReceivedPerSec_Type()
)
nwnetbiosDatagramBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosDatagramBytesReceivedPerSec.setStatus("mandatory")
_NwnetbiosPacketsSentPerSec_Type = Counter32
_NwnetbiosPacketsSentPerSec_Object = MibTableColumn
nwnetbiosPacketsSentPerSec = _NwnetbiosPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 26),
    _NwnetbiosPacketsSentPerSec_Type()
)
nwnetbiosPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosPacketsSentPerSec.setStatus("mandatory")
_NwnetbiosPacketsReceivedPerSec_Type = Counter32
_NwnetbiosPacketsReceivedPerSec_Object = MibTableColumn
nwnetbiosPacketsReceivedPerSec = _NwnetbiosPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 27),
    _NwnetbiosPacketsReceivedPerSec_Type()
)
nwnetbiosPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosPacketsReceivedPerSec.setStatus("mandatory")
_NwnetbiosFramesSentPerSec_Type = Counter32
_NwnetbiosFramesSentPerSec_Object = MibTableColumn
nwnetbiosFramesSentPerSec = _NwnetbiosFramesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 28),
    _NwnetbiosFramesSentPerSec_Type()
)
nwnetbiosFramesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFramesSentPerSec.setStatus("mandatory")
_NwnetbiosFrameBytesSentPerSec_Type = Integer32
_NwnetbiosFrameBytesSentPerSec_Object = MibTableColumn
nwnetbiosFrameBytesSentPerSec = _NwnetbiosFrameBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 29),
    _NwnetbiosFrameBytesSentPerSec_Type()
)
nwnetbiosFrameBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFrameBytesSentPerSec.setStatus("mandatory")
_NwnetbiosFramesReceivedPerSec_Type = Counter32
_NwnetbiosFramesReceivedPerSec_Object = MibTableColumn
nwnetbiosFramesReceivedPerSec = _NwnetbiosFramesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 30),
    _NwnetbiosFramesReceivedPerSec_Type()
)
nwnetbiosFramesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFramesReceivedPerSec.setStatus("mandatory")
_NwnetbiosFrameBytesReceivedPerSec_Type = Integer32
_NwnetbiosFrameBytesReceivedPerSec_Object = MibTableColumn
nwnetbiosFrameBytesReceivedPerSec = _NwnetbiosFrameBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 31),
    _NwnetbiosFrameBytesReceivedPerSec_Type()
)
nwnetbiosFrameBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFrameBytesReceivedPerSec.setStatus("mandatory")
_NwnetbiosFramesRe_SentPerSec_Type = Counter32
_NwnetbiosFramesRe_SentPerSec_Object = MibScalar
nwnetbiosFramesRe_SentPerSec = _NwnetbiosFramesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 32),
    _NwnetbiosFramesRe_SentPerSec_Type()
)
nwnetbiosFramesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFramesRe_SentPerSec.setStatus("mandatory")
_NwnetbiosFrameBytesRe_SentPerSec_Type = Integer32
_NwnetbiosFrameBytesRe_SentPerSec_Object = MibScalar
nwnetbiosFrameBytesRe_SentPerSec = _NwnetbiosFrameBytesRe_SentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 33),
    _NwnetbiosFrameBytesRe_SentPerSec_Type()
)
nwnetbiosFrameBytesRe_SentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFrameBytesRe_SentPerSec.setStatus("mandatory")
_NwnetbiosFramesRejectedPerSec_Type = Counter32
_NwnetbiosFramesRejectedPerSec_Object = MibTableColumn
nwnetbiosFramesRejectedPerSec = _NwnetbiosFramesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 34),
    _NwnetbiosFramesRejectedPerSec_Type()
)
nwnetbiosFramesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFramesRejectedPerSec.setStatus("mandatory")
_NwnetbiosFrameBytesRejectedPerSec_Type = Integer32
_NwnetbiosFrameBytesRejectedPerSec_Object = MibTableColumn
nwnetbiosFrameBytesRejectedPerSec = _NwnetbiosFrameBytesRejectedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 35),
    _NwnetbiosFrameBytesRejectedPerSec_Type()
)
nwnetbiosFrameBytesRejectedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosFrameBytesRejectedPerSec.setStatus("mandatory")
_NwnetbiosExpirationsResponse_Type = Integer32
_NwnetbiosExpirationsResponse_Object = MibTableColumn
nwnetbiosExpirationsResponse = _NwnetbiosExpirationsResponse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 36),
    _NwnetbiosExpirationsResponse_Type()
)
nwnetbiosExpirationsResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosExpirationsResponse.setStatus("mandatory")
_NwnetbiosExpirationsAck_Type = Integer32
_NwnetbiosExpirationsAck_Object = MibTableColumn
nwnetbiosExpirationsAck = _NwnetbiosExpirationsAck_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 37),
    _NwnetbiosExpirationsAck_Type()
)
nwnetbiosExpirationsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosExpirationsAck.setStatus("mandatory")
_NwnetbiosWindowSendMaximum_Type = Integer32
_NwnetbiosWindowSendMaximum_Object = MibTableColumn
nwnetbiosWindowSendMaximum = _NwnetbiosWindowSendMaximum_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 38),
    _NwnetbiosWindowSendMaximum_Type()
)
nwnetbiosWindowSendMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosWindowSendMaximum.setStatus("mandatory")
_NwnetbiosWindowSendAverage_Type = Integer32
_NwnetbiosWindowSendAverage_Object = MibTableColumn
nwnetbiosWindowSendAverage = _NwnetbiosWindowSendAverage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 39),
    _NwnetbiosWindowSendAverage_Type()
)
nwnetbiosWindowSendAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosWindowSendAverage.setStatus("mandatory")
_NwnetbiosPiggybackAckQueuedPerSec_Type = Counter32
_NwnetbiosPiggybackAckQueuedPerSec_Object = MibTableColumn
nwnetbiosPiggybackAckQueuedPerSec = _NwnetbiosPiggybackAckQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 40),
    _NwnetbiosPiggybackAckQueuedPerSec_Type()
)
nwnetbiosPiggybackAckQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosPiggybackAckQueuedPerSec.setStatus("mandatory")
_NwnetbiosPiggybackAckTimeouts_Type = Integer32
_NwnetbiosPiggybackAckTimeouts_Object = MibTableColumn
nwnetbiosPiggybackAckTimeouts = _NwnetbiosPiggybackAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 32, 1, 41),
    _NwnetbiosPiggybackAckTimeouts_Type()
)
nwnetbiosPiggybackAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwnetbiosPiggybackAckTimeouts.setStatus("mandatory")
_Ntsystem_ObjectIdentity = ObjectIdentity
ntsystem = _Ntsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33)
)
_NtsystemFileReadOperationsPerSec_Type = Counter32
_NtsystemFileReadOperationsPerSec_Object = MibScalar
ntsystemFileReadOperationsPerSec = _NtsystemFileReadOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 1),
    _NtsystemFileReadOperationsPerSec_Type()
)
ntsystemFileReadOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileReadOperationsPerSec.setStatus("mandatory")
_NtsystemFileWriteOperationsPerSec_Type = Counter32
_NtsystemFileWriteOperationsPerSec_Object = MibScalar
ntsystemFileWriteOperationsPerSec = _NtsystemFileWriteOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 2),
    _NtsystemFileWriteOperationsPerSec_Type()
)
ntsystemFileWriteOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileWriteOperationsPerSec.setStatus("mandatory")
_NtsystemFileControlOperationsPerSec_Type = Counter32
_NtsystemFileControlOperationsPerSec_Object = MibScalar
ntsystemFileControlOperationsPerSec = _NtsystemFileControlOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 3),
    _NtsystemFileControlOperationsPerSec_Type()
)
ntsystemFileControlOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileControlOperationsPerSec.setStatus("mandatory")
_NtsystemFileReadBytesPerSec_Type = Integer32
_NtsystemFileReadBytesPerSec_Object = MibScalar
ntsystemFileReadBytesPerSec = _NtsystemFileReadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 4),
    _NtsystemFileReadBytesPerSec_Type()
)
ntsystemFileReadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileReadBytesPerSec.setStatus("mandatory")
_NtsystemFileWriteBytesPerSec_Type = Integer32
_NtsystemFileWriteBytesPerSec_Object = MibScalar
ntsystemFileWriteBytesPerSec = _NtsystemFileWriteBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 5),
    _NtsystemFileWriteBytesPerSec_Type()
)
ntsystemFileWriteBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileWriteBytesPerSec.setStatus("mandatory")
_NtsystemFileControlBytesPerSec_Type = Integer32
_NtsystemFileControlBytesPerSec_Object = MibScalar
ntsystemFileControlBytesPerSec = _NtsystemFileControlBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 6),
    _NtsystemFileControlBytesPerSec_Type()
)
ntsystemFileControlBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileControlBytesPerSec.setStatus("mandatory")
_NtsystemContextSwitchesPerSec_Type = Counter32
_NtsystemContextSwitchesPerSec_Object = MibScalar
ntsystemContextSwitchesPerSec = _NtsystemContextSwitchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 7),
    _NtsystemContextSwitchesPerSec_Type()
)
ntsystemContextSwitchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemContextSwitchesPerSec.setStatus("mandatory")
_NtsystemSystemCallsPerSec_Type = Counter32
_NtsystemSystemCallsPerSec_Object = MibScalar
ntsystemSystemCallsPerSec = _NtsystemSystemCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 8),
    _NtsystemSystemCallsPerSec_Type()
)
ntsystemSystemCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemSystemCallsPerSec.setStatus("mandatory")
_NtsystemPercentTotalProcessorTime_Type = Integer32
_NtsystemPercentTotalProcessorTime_Object = MibScalar
ntsystemPercentTotalProcessorTime = _NtsystemPercentTotalProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 9),
    _NtsystemPercentTotalProcessorTime_Type()
)
ntsystemPercentTotalProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentTotalProcessorTime.setStatus("mandatory")
_NtsystemPercentTotalUserTime_Type = Integer32
_NtsystemPercentTotalUserTime_Object = MibScalar
ntsystemPercentTotalUserTime = _NtsystemPercentTotalUserTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 10),
    _NtsystemPercentTotalUserTime_Type()
)
ntsystemPercentTotalUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentTotalUserTime.setStatus("mandatory")
_NtsystemPercentTotalPrivilegedTime_Type = Integer32
_NtsystemPercentTotalPrivilegedTime_Object = MibScalar
ntsystemPercentTotalPrivilegedTime = _NtsystemPercentTotalPrivilegedTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 11),
    _NtsystemPercentTotalPrivilegedTime_Type()
)
ntsystemPercentTotalPrivilegedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentTotalPrivilegedTime.setStatus("mandatory")
_NtsystemTotalInterruptsPerSec_Type = Counter32
_NtsystemTotalInterruptsPerSec_Object = MibScalar
ntsystemTotalInterruptsPerSec = _NtsystemTotalInterruptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 12),
    _NtsystemTotalInterruptsPerSec_Type()
)
ntsystemTotalInterruptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemTotalInterruptsPerSec.setStatus("mandatory")
_NtsystemFileDataOperationsPerSec_Type = Counter32
_NtsystemFileDataOperationsPerSec_Object = MibScalar
ntsystemFileDataOperationsPerSec = _NtsystemFileDataOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 13),
    _NtsystemFileDataOperationsPerSec_Type()
)
ntsystemFileDataOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFileDataOperationsPerSec.setStatus("mandatory")
_NtsystemSystemUpTime_Type = TimeTicks
_NtsystemSystemUpTime_Object = MibScalar
ntsystemSystemUpTime = _NtsystemSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 14),
    _NtsystemSystemUpTime_Type()
)
ntsystemSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemSystemUpTime.setStatus("mandatory")
_NtsystemProcessorQueueLength_Type = Integer32
_NtsystemProcessorQueueLength_Object = MibScalar
ntsystemProcessorQueueLength = _NtsystemProcessorQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 15),
    _NtsystemProcessorQueueLength_Type()
)
ntsystemProcessorQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemProcessorQueueLength.setStatus("mandatory")
_NtsystemAlignmentFixupsPerSec_Type = Counter32
_NtsystemAlignmentFixupsPerSec_Object = MibScalar
ntsystemAlignmentFixupsPerSec = _NtsystemAlignmentFixupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 16),
    _NtsystemAlignmentFixupsPerSec_Type()
)
ntsystemAlignmentFixupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemAlignmentFixupsPerSec.setStatus("mandatory")
_NtsystemExceptionDispatchesPerSec_Type = Counter32
_NtsystemExceptionDispatchesPerSec_Object = MibScalar
ntsystemExceptionDispatchesPerSec = _NtsystemExceptionDispatchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 17),
    _NtsystemExceptionDispatchesPerSec_Type()
)
ntsystemExceptionDispatchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemExceptionDispatchesPerSec.setStatus("mandatory")
_NtsystemFloatingEmulationsPerSec_Type = Counter32
_NtsystemFloatingEmulationsPerSec_Object = MibScalar
ntsystemFloatingEmulationsPerSec = _NtsystemFloatingEmulationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 18),
    _NtsystemFloatingEmulationsPerSec_Type()
)
ntsystemFloatingEmulationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemFloatingEmulationsPerSec.setStatus("mandatory")
_NtsystemPercentTotalDPCTime_Type = Integer32
_NtsystemPercentTotalDPCTime_Object = MibScalar
ntsystemPercentTotalDPCTime = _NtsystemPercentTotalDPCTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 19),
    _NtsystemPercentTotalDPCTime_Type()
)
ntsystemPercentTotalDPCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentTotalDPCTime.setStatus("mandatory")
_NtsystemPercentTotalInterruptTime_Type = Integer32
_NtsystemPercentTotalInterruptTime_Object = MibScalar
ntsystemPercentTotalInterruptTime = _NtsystemPercentTotalInterruptTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 20),
    _NtsystemPercentTotalInterruptTime_Type()
)
ntsystemPercentTotalInterruptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentTotalInterruptTime.setStatus("mandatory")
_NtsystemTotalDPCsQueuedPerSec_Type = Counter32
_NtsystemTotalDPCsQueuedPerSec_Object = MibScalar
ntsystemTotalDPCsQueuedPerSec = _NtsystemTotalDPCsQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 21),
    _NtsystemTotalDPCsQueuedPerSec_Type()
)
ntsystemTotalDPCsQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemTotalDPCsQueuedPerSec.setStatus("mandatory")
_NtsystemTotalDPCRate_Type = Integer32
_NtsystemTotalDPCRate_Object = MibScalar
ntsystemTotalDPCRate = _NtsystemTotalDPCRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 22),
    _NtsystemTotalDPCRate_Type()
)
ntsystemTotalDPCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemTotalDPCRate.setStatus("mandatory")
_NtsystemTotalDPCBypassesPerSec_Type = Counter32
_NtsystemTotalDPCBypassesPerSec_Object = MibScalar
ntsystemTotalDPCBypassesPerSec = _NtsystemTotalDPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 23),
    _NtsystemTotalDPCBypassesPerSec_Type()
)
ntsystemTotalDPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemTotalDPCBypassesPerSec.setStatus("mandatory")
_NtsystemTotalAPCBypassesPerSec_Type = Counter32
_NtsystemTotalAPCBypassesPerSec_Object = MibScalar
ntsystemTotalAPCBypassesPerSec = _NtsystemTotalAPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 24),
    _NtsystemTotalAPCBypassesPerSec_Type()
)
ntsystemTotalAPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemTotalAPCBypassesPerSec.setStatus("mandatory")
_NtsystemPercentRegistryQuotaInUse_Type = Integer32
_NtsystemPercentRegistryQuotaInUse_Object = MibScalar
ntsystemPercentRegistryQuotaInUse = _NtsystemPercentRegistryQuotaInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 33, 25),
    _NtsystemPercentRegistryQuotaInUse_Type()
)
ntsystemPercentRegistryQuotaInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntsystemPercentRegistryQuotaInUse.setStatus("mandatory")
_Packet_Filtering_ObjectIdentity = ObjectIdentity
packet_Filtering = _Packet_Filtering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34)
)
_PacketfilterTotalDroppedFrames_Type = Counter32
_PacketfilterTotalDroppedFrames_Object = MibScalar
packetfilterTotalDroppedFrames = _PacketfilterTotalDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34, 1),
    _PacketfilterTotalDroppedFrames_Type()
)
packetfilterTotalDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetfilterTotalDroppedFrames.setStatus("mandatory")
_PacketfilterFramesDroppedDueToFilterDenial_Type = Counter32
_PacketfilterFramesDroppedDueToFilterDenial_Object = MibScalar
packetfilterFramesDroppedDueToFilterDenial = _PacketfilterFramesDroppedDueToFilterDenial_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34, 2),
    _PacketfilterFramesDroppedDueToFilterDenial_Type()
)
packetfilterFramesDroppedDueToFilterDenial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetfilterFramesDroppedDueToFilterDenial.setStatus("mandatory")
_PacketfilterFramesDroppedDueToProtocolViolations_Type = Counter32
_PacketfilterFramesDroppedDueToProtocolViolations_Object = MibScalar
packetfilterFramesDroppedDueToProtocolViolations = _PacketfilterFramesDroppedDueToProtocolViolations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34, 3),
    _PacketfilterFramesDroppedDueToProtocolViolations_Type()
)
packetfilterFramesDroppedDueToProtocolViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetfilterFramesDroppedDueToProtocolViolations.setStatus("mandatory")
_PacketfilterTotalIncomingConnections_Type = Counter32
_PacketfilterTotalIncomingConnections_Object = MibScalar
packetfilterTotalIncomingConnections = _PacketfilterTotalIncomingConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34, 4),
    _PacketfilterTotalIncomingConnections_Type()
)
packetfilterTotalIncomingConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetfilterTotalIncomingConnections.setStatus("mandatory")
_PacketfilterTotalLostLoggingFrames_Type = Counter32
_PacketfilterTotalLostLoggingFrames_Object = MibScalar
packetfilterTotalLostLoggingFrames = _PacketfilterTotalLostLoggingFrames_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 34, 5),
    _PacketfilterTotalLostLoggingFrames_Type()
)
packetfilterTotalLostLoggingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetfilterTotalLostLoggingFrames.setStatus("mandatory")
_Webserviceweb_ServiceTable_Object = MibTable
webserviceweb_ServiceTable = _Webserviceweb_ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35)
)
if mibBuilder.loadTexts:
    webserviceweb_ServiceTable.setStatus("mandatory")
_Webserviceweb_ServiceEntry_Object = MibTableRow
webserviceweb_ServiceEntry = _Webserviceweb_ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1)
)
webserviceweb_ServiceEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE", "webserviceweb-ServiceIndex"),
)
if mibBuilder.loadTexts:
    webserviceweb_ServiceEntry.setStatus("mandatory")
_Webserviceweb_ServiceIndex_Type = Integer32
_Webserviceweb_ServiceIndex_Object = MibScalar
webserviceweb_ServiceIndex = _Webserviceweb_ServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 1),
    _Webserviceweb_ServiceIndex_Type()
)
webserviceweb_ServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceweb_ServiceIndex.setStatus("mandatory")
_Webserviceweb_ServiceInstance_Type = DisplayString
_Webserviceweb_ServiceInstance_Object = MibScalar
webserviceweb_ServiceInstance = _Webserviceweb_ServiceInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 2),
    _Webserviceweb_ServiceInstance_Type()
)
webserviceweb_ServiceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceweb_ServiceInstance.setStatus("mandatory")
_WebserviceBytesSentPerSec_Type = Integer32
_WebserviceBytesSentPerSec_Object = MibTableColumn
webserviceBytesSentPerSec = _WebserviceBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 3),
    _WebserviceBytesSentPerSec_Type()
)
webserviceBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceBytesSentPerSec.setStatus("mandatory")
_WebserviceBytesReceivedPerSec_Type = Integer32
_WebserviceBytesReceivedPerSec_Object = MibTableColumn
webserviceBytesReceivedPerSec = _WebserviceBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 4),
    _WebserviceBytesReceivedPerSec_Type()
)
webserviceBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceBytesReceivedPerSec.setStatus("mandatory")
_WebserviceBytesTotalPerSec_Type = Integer32
_WebserviceBytesTotalPerSec_Object = MibTableColumn
webserviceBytesTotalPerSec = _WebserviceBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 5),
    _WebserviceBytesTotalPerSec_Type()
)
webserviceBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceBytesTotalPerSec.setStatus("mandatory")
_WebserviceTotalFilesSent_Type = Integer32
_WebserviceTotalFilesSent_Object = MibTableColumn
webserviceTotalFilesSent = _WebserviceTotalFilesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 6),
    _WebserviceTotalFilesSent_Type()
)
webserviceTotalFilesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalFilesSent.setStatus("mandatory")
_WebserviceFilesSentPerSec_Type = Counter32
_WebserviceFilesSentPerSec_Object = MibTableColumn
webserviceFilesSentPerSec = _WebserviceFilesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 7),
    _WebserviceFilesSentPerSec_Type()
)
webserviceFilesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceFilesSentPerSec.setStatus("mandatory")
_WebserviceTotalFilesReceived_Type = Integer32
_WebserviceTotalFilesReceived_Object = MibTableColumn
webserviceTotalFilesReceived = _WebserviceTotalFilesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 8),
    _WebserviceTotalFilesReceived_Type()
)
webserviceTotalFilesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalFilesReceived.setStatus("mandatory")
_WebserviceFilesReceivedPerSec_Type = Counter32
_WebserviceFilesReceivedPerSec_Object = MibTableColumn
webserviceFilesReceivedPerSec = _WebserviceFilesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 9),
    _WebserviceFilesReceivedPerSec_Type()
)
webserviceFilesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceFilesReceivedPerSec.setStatus("mandatory")
_WebserviceTotalFilesTransferred_Type = Integer32
_WebserviceTotalFilesTransferred_Object = MibTableColumn
webserviceTotalFilesTransferred = _WebserviceTotalFilesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 10),
    _WebserviceTotalFilesTransferred_Type()
)
webserviceTotalFilesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalFilesTransferred.setStatus("mandatory")
_WebserviceFilesPerSec_Type = Counter32
_WebserviceFilesPerSec_Object = MibTableColumn
webserviceFilesPerSec = _WebserviceFilesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 11),
    _WebserviceFilesPerSec_Type()
)
webserviceFilesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceFilesPerSec.setStatus("mandatory")
_WebserviceCurrentAnonymousUsers_Type = Integer32
_WebserviceCurrentAnonymousUsers_Object = MibTableColumn
webserviceCurrentAnonymousUsers = _WebserviceCurrentAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 12),
    _WebserviceCurrentAnonymousUsers_Type()
)
webserviceCurrentAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentAnonymousUsers.setStatus("mandatory")
_WebserviceCurrentNonAnonymousUsers_Type = Integer32
_WebserviceCurrentNonAnonymousUsers_Object = MibTableColumn
webserviceCurrentNonAnonymousUsers = _WebserviceCurrentNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 13),
    _WebserviceCurrentNonAnonymousUsers_Type()
)
webserviceCurrentNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentNonAnonymousUsers.setStatus("mandatory")
_WebserviceTotalAnonymousUsers_Type = Integer32
_WebserviceTotalAnonymousUsers_Object = MibTableColumn
webserviceTotalAnonymousUsers = _WebserviceTotalAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 14),
    _WebserviceTotalAnonymousUsers_Type()
)
webserviceTotalAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalAnonymousUsers.setStatus("mandatory")
_WebserviceAnonymousUsersPerSec_Type = Counter32
_WebserviceAnonymousUsersPerSec_Object = MibTableColumn
webserviceAnonymousUsersPerSec = _WebserviceAnonymousUsersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 15),
    _WebserviceAnonymousUsersPerSec_Type()
)
webserviceAnonymousUsersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceAnonymousUsersPerSec.setStatus("mandatory")
_WebserviceTotalNonAnonymousUsers_Type = Integer32
_WebserviceTotalNonAnonymousUsers_Object = MibTableColumn
webserviceTotalNonAnonymousUsers = _WebserviceTotalNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 16),
    _WebserviceTotalNonAnonymousUsers_Type()
)
webserviceTotalNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalNonAnonymousUsers.setStatus("mandatory")
_WebserviceNonAnonymousUsersPerSec_Type = Counter32
_WebserviceNonAnonymousUsersPerSec_Object = MibTableColumn
webserviceNonAnonymousUsersPerSec = _WebserviceNonAnonymousUsersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 17),
    _WebserviceNonAnonymousUsersPerSec_Type()
)
webserviceNonAnonymousUsersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceNonAnonymousUsersPerSec.setStatus("mandatory")
_WebserviceMaximumAnonymousUsers_Type = Integer32
_WebserviceMaximumAnonymousUsers_Object = MibTableColumn
webserviceMaximumAnonymousUsers = _WebserviceMaximumAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 18),
    _WebserviceMaximumAnonymousUsers_Type()
)
webserviceMaximumAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMaximumAnonymousUsers.setStatus("mandatory")
_WebserviceMaximumNonAnonymousUsers_Type = Integer32
_WebserviceMaximumNonAnonymousUsers_Object = MibTableColumn
webserviceMaximumNonAnonymousUsers = _WebserviceMaximumNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 19),
    _WebserviceMaximumNonAnonymousUsers_Type()
)
webserviceMaximumNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMaximumNonAnonymousUsers.setStatus("mandatory")
_WebserviceCurrentConnections_Type = Integer32
_WebserviceCurrentConnections_Object = MibTableColumn
webserviceCurrentConnections = _WebserviceCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 20),
    _WebserviceCurrentConnections_Type()
)
webserviceCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentConnections.setStatus("mandatory")
_WebserviceMaximumConnections_Type = Integer32
_WebserviceMaximumConnections_Object = MibTableColumn
webserviceMaximumConnections = _WebserviceMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 21),
    _WebserviceMaximumConnections_Type()
)
webserviceMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMaximumConnections.setStatus("mandatory")
_WebserviceTotalConnectionAttempts_Type = Integer32
_WebserviceTotalConnectionAttempts_Object = MibTableColumn
webserviceTotalConnectionAttempts = _WebserviceTotalConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 22),
    _WebserviceTotalConnectionAttempts_Type()
)
webserviceTotalConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalConnectionAttempts.setStatus("mandatory")
_WebserviceConnectionAttemptsPerSec_Type = Counter32
_WebserviceConnectionAttemptsPerSec_Object = MibTableColumn
webserviceConnectionAttemptsPerSec = _WebserviceConnectionAttemptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 23),
    _WebserviceConnectionAttemptsPerSec_Type()
)
webserviceConnectionAttemptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceConnectionAttemptsPerSec.setStatus("mandatory")
_WebserviceTotalLogonAttempts_Type = Integer32
_WebserviceTotalLogonAttempts_Object = MibTableColumn
webserviceTotalLogonAttempts = _WebserviceTotalLogonAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 24),
    _WebserviceTotalLogonAttempts_Type()
)
webserviceTotalLogonAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalLogonAttempts.setStatus("mandatory")
_WebserviceLogonAttemptsPerSec_Type = Counter32
_WebserviceLogonAttemptsPerSec_Object = MibTableColumn
webserviceLogonAttemptsPerSec = _WebserviceLogonAttemptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 25),
    _WebserviceLogonAttemptsPerSec_Type()
)
webserviceLogonAttemptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceLogonAttemptsPerSec.setStatus("mandatory")
_WebserviceTotalGetRequests_Type = Integer32
_WebserviceTotalGetRequests_Object = MibTableColumn
webserviceTotalGetRequests = _WebserviceTotalGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 26),
    _WebserviceTotalGetRequests_Type()
)
webserviceTotalGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalGetRequests.setStatus("mandatory")
_WebserviceGetRequestsPerSec_Type = Counter32
_WebserviceGetRequestsPerSec_Object = MibTableColumn
webserviceGetRequestsPerSec = _WebserviceGetRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 27),
    _WebserviceGetRequestsPerSec_Type()
)
webserviceGetRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceGetRequestsPerSec.setStatus("mandatory")
_WebserviceTotalPostRequests_Type = Integer32
_WebserviceTotalPostRequests_Object = MibTableColumn
webserviceTotalPostRequests = _WebserviceTotalPostRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 28),
    _WebserviceTotalPostRequests_Type()
)
webserviceTotalPostRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalPostRequests.setStatus("mandatory")
_WebservicePostRequestsPerSec_Type = Counter32
_WebservicePostRequestsPerSec_Object = MibTableColumn
webservicePostRequestsPerSec = _WebservicePostRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 29),
    _WebservicePostRequestsPerSec_Type()
)
webservicePostRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webservicePostRequestsPerSec.setStatus("mandatory")
_WebserviceTotalHeadRequests_Type = Integer32
_WebserviceTotalHeadRequests_Object = MibTableColumn
webserviceTotalHeadRequests = _WebserviceTotalHeadRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 30),
    _WebserviceTotalHeadRequests_Type()
)
webserviceTotalHeadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalHeadRequests.setStatus("mandatory")
_WebserviceHeadRequestsPerSec_Type = Counter32
_WebserviceHeadRequestsPerSec_Object = MibTableColumn
webserviceHeadRequestsPerSec = _WebserviceHeadRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 31),
    _WebserviceHeadRequestsPerSec_Type()
)
webserviceHeadRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceHeadRequestsPerSec.setStatus("mandatory")
_WebserviceTotalPutRequests_Type = Integer32
_WebserviceTotalPutRequests_Object = MibTableColumn
webserviceTotalPutRequests = _WebserviceTotalPutRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 32),
    _WebserviceTotalPutRequests_Type()
)
webserviceTotalPutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalPutRequests.setStatus("mandatory")
_WebservicePutRequestsPerSec_Type = Counter32
_WebservicePutRequestsPerSec_Object = MibTableColumn
webservicePutRequestsPerSec = _WebservicePutRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 33),
    _WebservicePutRequestsPerSec_Type()
)
webservicePutRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webservicePutRequestsPerSec.setStatus("mandatory")
_WebserviceTotalDeleteRequests_Type = Integer32
_WebserviceTotalDeleteRequests_Object = MibTableColumn
webserviceTotalDeleteRequests = _WebserviceTotalDeleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 34),
    _WebserviceTotalDeleteRequests_Type()
)
webserviceTotalDeleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalDeleteRequests.setStatus("mandatory")
_WebserviceDeleteRequestsPerSec_Type = Counter32
_WebserviceDeleteRequestsPerSec_Object = MibTableColumn
webserviceDeleteRequestsPerSec = _WebserviceDeleteRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 35),
    _WebserviceDeleteRequestsPerSec_Type()
)
webserviceDeleteRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceDeleteRequestsPerSec.setStatus("mandatory")
_WebserviceTotalTraceRequests_Type = Integer32
_WebserviceTotalTraceRequests_Object = MibTableColumn
webserviceTotalTraceRequests = _WebserviceTotalTraceRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 36),
    _WebserviceTotalTraceRequests_Type()
)
webserviceTotalTraceRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalTraceRequests.setStatus("mandatory")
_WebserviceSystemCodeResidentBytes_Type = Counter32
_WebserviceSystemCodeResidentBytes_Object = MibTableColumn
webserviceSystemCodeResidentBytes = _WebserviceSystemCodeResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 37),
    _WebserviceSystemCodeResidentBytes_Type()
)
webserviceSystemCodeResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceSystemCodeResidentBytes.setStatus("mandatory")
_WebserviceTotalOtherRequestMethods_Type = Integer32
_WebserviceTotalOtherRequestMethods_Object = MibTableColumn
webserviceTotalOtherRequestMethods = _WebserviceTotalOtherRequestMethods_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 38),
    _WebserviceTotalOtherRequestMethods_Type()
)
webserviceTotalOtherRequestMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalOtherRequestMethods.setStatus("mandatory")
_WebserviceOtherRequestMethodsPerSec_Type = Counter32
_WebserviceOtherRequestMethodsPerSec_Object = MibTableColumn
webserviceOtherRequestMethodsPerSec = _WebserviceOtherRequestMethodsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 39),
    _WebserviceOtherRequestMethodsPerSec_Type()
)
webserviceOtherRequestMethodsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceOtherRequestMethodsPerSec.setStatus("mandatory")
_WebserviceTotalMethodRequests_Type = Integer32
_WebserviceTotalMethodRequests_Object = MibTableColumn
webserviceTotalMethodRequests = _WebserviceTotalMethodRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 40),
    _WebserviceTotalMethodRequests_Type()
)
webserviceTotalMethodRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalMethodRequests.setStatus("mandatory")
_WebserviceTotalMethodRequestsPerSec_Type = Counter32
_WebserviceTotalMethodRequestsPerSec_Object = MibTableColumn
webserviceTotalMethodRequestsPerSec = _WebserviceTotalMethodRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 41),
    _WebserviceTotalMethodRequestsPerSec_Type()
)
webserviceTotalMethodRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalMethodRequestsPerSec.setStatus("mandatory")
_WebserviceTotalCGIRequests_Type = Integer32
_WebserviceTotalCGIRequests_Object = MibTableColumn
webserviceTotalCGIRequests = _WebserviceTotalCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 42),
    _WebserviceTotalCGIRequests_Type()
)
webserviceTotalCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalCGIRequests.setStatus("mandatory")
_WebserviceCGIRequestsPerSec_Type = Counter32
_WebserviceCGIRequestsPerSec_Object = MibTableColumn
webserviceCGIRequestsPerSec = _WebserviceCGIRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 43),
    _WebserviceCGIRequestsPerSec_Type()
)
webserviceCGIRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCGIRequestsPerSec.setStatus("mandatory")
_WebserviceTotalISAPIExtensionRequests_Type = Integer32
_WebserviceTotalISAPIExtensionRequests_Object = MibTableColumn
webserviceTotalISAPIExtensionRequests = _WebserviceTotalISAPIExtensionRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 44),
    _WebserviceTotalISAPIExtensionRequests_Type()
)
webserviceTotalISAPIExtensionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalISAPIExtensionRequests.setStatus("mandatory")
_WebserviceISAPIExtensionRequestsPerSec_Type = Counter32
_WebserviceISAPIExtensionRequestsPerSec_Object = MibTableColumn
webserviceISAPIExtensionRequestsPerSec = _WebserviceISAPIExtensionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 45),
    _WebserviceISAPIExtensionRequestsPerSec_Type()
)
webserviceISAPIExtensionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceISAPIExtensionRequestsPerSec.setStatus("mandatory")
_WebserviceTotalNotFoundErrors_Type = Integer32
_WebserviceTotalNotFoundErrors_Object = MibTableColumn
webserviceTotalNotFoundErrors = _WebserviceTotalNotFoundErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 46),
    _WebserviceTotalNotFoundErrors_Type()
)
webserviceTotalNotFoundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalNotFoundErrors.setStatus("mandatory")
_WebserviceNotFoundErrorsPerSec_Type = Counter32
_WebserviceNotFoundErrorsPerSec_Object = MibTableColumn
webserviceNotFoundErrorsPerSec = _WebserviceNotFoundErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 47),
    _WebserviceNotFoundErrorsPerSec_Type()
)
webserviceNotFoundErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceNotFoundErrorsPerSec.setStatus("mandatory")
_WebserviceCurrentCGIRequests_Type = Integer32
_WebserviceCurrentCGIRequests_Object = MibTableColumn
webserviceCurrentCGIRequests = _WebserviceCurrentCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 48),
    _WebserviceCurrentCGIRequests_Type()
)
webserviceCurrentCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentCGIRequests.setStatus("mandatory")
_WebserviceCurrentISAPIExtensionRequests_Type = Integer32
_WebserviceCurrentISAPIExtensionRequests_Object = MibTableColumn
webserviceCurrentISAPIExtensionRequests = _WebserviceCurrentISAPIExtensionRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 49),
    _WebserviceCurrentISAPIExtensionRequests_Type()
)
webserviceCurrentISAPIExtensionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentISAPIExtensionRequests.setStatus("mandatory")
_WebserviceMaximumCGIRequests_Type = Integer32
_WebserviceMaximumCGIRequests_Object = MibTableColumn
webserviceMaximumCGIRequests = _WebserviceMaximumCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 50),
    _WebserviceMaximumCGIRequests_Type()
)
webserviceMaximumCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMaximumCGIRequests.setStatus("mandatory")
_WebserviceMaximumISAPIExtensionRequests_Type = Integer32
_WebserviceMaximumISAPIExtensionRequests_Object = MibTableColumn
webserviceMaximumISAPIExtensionRequests = _WebserviceMaximumISAPIExtensionRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 51),
    _WebserviceMaximumISAPIExtensionRequests_Type()
)
webserviceMaximumISAPIExtensionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMaximumISAPIExtensionRequests.setStatus("mandatory")
_WebserviceTotalBlockedAsyncIPerORequests_Type = Integer32
_WebserviceTotalBlockedAsyncIPerORequests_Object = MibTableColumn
webserviceTotalBlockedAsyncIPerORequests = _WebserviceTotalBlockedAsyncIPerORequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 52),
    _WebserviceTotalBlockedAsyncIPerORequests_Type()
)
webserviceTotalBlockedAsyncIPerORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalBlockedAsyncIPerORequests.setStatus("mandatory")
_WebserviceTotalAllowedAsyncIPerORequests_Type = Integer32
_WebserviceTotalAllowedAsyncIPerORequests_Object = MibTableColumn
webserviceTotalAllowedAsyncIPerORequests = _WebserviceTotalAllowedAsyncIPerORequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 53),
    _WebserviceTotalAllowedAsyncIPerORequests_Type()
)
webserviceTotalAllowedAsyncIPerORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalAllowedAsyncIPerORequests.setStatus("mandatory")
_WebserviceTotalRejectedAsyncIPerORequests_Type = Integer32
_WebserviceTotalRejectedAsyncIPerORequests_Object = MibTableColumn
webserviceTotalRejectedAsyncIPerORequests = _WebserviceTotalRejectedAsyncIPerORequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 54),
    _WebserviceTotalRejectedAsyncIPerORequests_Type()
)
webserviceTotalRejectedAsyncIPerORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceTotalRejectedAsyncIPerORequests.setStatus("mandatory")
_WebserviceCurrentBlockedAsyncIPerORequests_Type = Integer32
_WebserviceCurrentBlockedAsyncIPerORequests_Object = MibTableColumn
webserviceCurrentBlockedAsyncIPerORequests = _WebserviceCurrentBlockedAsyncIPerORequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 55),
    _WebserviceCurrentBlockedAsyncIPerORequests_Type()
)
webserviceCurrentBlockedAsyncIPerORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceCurrentBlockedAsyncIPerORequests.setStatus("mandatory")
_WebserviceMeasuredAsyncIPerOBandwidthUsage_Type = Integer32
_WebserviceMeasuredAsyncIPerOBandwidthUsage_Object = MibTableColumn
webserviceMeasuredAsyncIPerOBandwidthUsage = _WebserviceMeasuredAsyncIPerOBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 35, 1, 56),
    _WebserviceMeasuredAsyncIPerOBandwidthUsage_Type()
)
webserviceMeasuredAsyncIPerOBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webserviceMeasuredAsyncIPerOBandwidthUsage.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WINDOWS-NT-PERFORMANCE",
    **{"microsoft": microsoft,
       "software": software,
       "systems": systems,
       "os": os,
       "winnt": winnt,
       "performance": performance,
       "memory": memory,
       "memoryAvailableBytes": memoryAvailableBytes,
       "memoryCommittedBytes": memoryCommittedBytes,
       "memoryCommitLimit": memoryCommitLimit,
       "memoryPageFaultsPerSec": memoryPageFaultsPerSec,
       "memoryWriteCopiesPerSec": memoryWriteCopiesPerSec,
       "memoryTransitionFaultsPerSec": memoryTransitionFaultsPerSec,
       "memoryCacheFaultsPerSec": memoryCacheFaultsPerSec,
       "memoryDemandZeroFaultsPerSec": memoryDemandZeroFaultsPerSec,
       "memoryPagesPerSec": memoryPagesPerSec,
       "memoryPagesInputPerSec": memoryPagesInputPerSec,
       "memoryPageReadsPerSec": memoryPageReadsPerSec,
       "memoryPagesOutputPerSec": memoryPagesOutputPerSec,
       "memoryPageWritesPerSec": memoryPageWritesPerSec,
       "memoryPoolPagedBytes": memoryPoolPagedBytes,
       "memoryPoolNonpagedBytes": memoryPoolNonpagedBytes,
       "memoryPoolPagedAllocs": memoryPoolPagedAllocs,
       "memoryPoolNonpagedAllocs": memoryPoolNonpagedAllocs,
       "memoryFreeSystemPageTableEntries": memoryFreeSystemPageTableEntries,
       "memoryCacheBytes": memoryCacheBytes,
       "memoryCacheBytesPeak": memoryCacheBytesPeak,
       "memoryPoolPagedResidentBytes": memoryPoolPagedResidentBytes,
       "memorySystemCodeTotalBytes": memorySystemCodeTotalBytes,
       "memorySystemCodeResidentBytes": memorySystemCodeResidentBytes,
       "memorySystemDriverTotalBytes": memorySystemDriverTotalBytes,
       "memorySystemDriverResidentBytes": memorySystemDriverResidentBytes,
       "memorySystemCacheResidentBytes": memorySystemCacheResidentBytes,
       "memoryPercentCommittedBytesInUse": memoryPercentCommittedBytesInUse,
       "cpuprocessorTable": cpuprocessorTable,
       "cpuprocessorEntry": cpuprocessorEntry,
       "cpuprocessorIndex": cpuprocessorIndex,
       "cpuprocessorInstance": cpuprocessorInstance,
       "cpuPercentProcessorTime": cpuPercentProcessorTime,
       "cpuPercentUserTime": cpuPercentUserTime,
       "cpuPercentPrivilegedTime": cpuPercentPrivilegedTime,
       "cpuInterruptsPerSec": cpuInterruptsPerSec,
       "cpuPercentDPCTime": cpuPercentDPCTime,
       "cpuPercentInterruptTime": cpuPercentInterruptTime,
       "cpuDPCsQueuedPerSec": cpuDPCsQueuedPerSec,
       "cpuDPCRate": cpuDPCRate,
       "cpuDPCBypassesPerSec": cpuDPCBypassesPerSec,
       "cpuAPCBypassesPerSec": cpuAPCBypassesPerSec,
       "netnetwork-InterfaceTable": netnetwork_InterfaceTable,
       "netnetwork-InterfaceEntry": netnetwork_InterfaceEntry,
       "netnetwork-InterfaceIndex": netnetwork_InterfaceIndex,
       "netnetwork-InterfaceInstance": netnetwork_InterfaceInstance,
       "netBytesTotalPerSec": netBytesTotalPerSec,
       "netPacketsPerSec": netPacketsPerSec,
       "netPacketsReceivedPerSec": netPacketsReceivedPerSec,
       "netPacketsSentPerSec": netPacketsSentPerSec,
       "netCurrentBandwidth": netCurrentBandwidth,
       "netBytesReceivedPerSec": netBytesReceivedPerSec,
       "netPacketsReceivedUnicastPerSec": netPacketsReceivedUnicastPerSec,
       "netPacketsReceivedNon-UnicastPerSec": netPacketsReceivedNon_UnicastPerSec,
       "netPacketsReceivedDiscarded": netPacketsReceivedDiscarded,
       "netPacketsReceivedErrors": netPacketsReceivedErrors,
       "netPacketsReceivedUnknown": netPacketsReceivedUnknown,
       "netBytesSentPerSec": netBytesSentPerSec,
       "netPacketsSentUnicastPerSec": netPacketsSentUnicastPerSec,
       "netPacketsSentNon-UnicastPerSec": netPacketsSentNon_UnicastPerSec,
       "netPacketsOutboundDiscarded": netPacketsOutboundDiscarded,
       "netPacketsOutboundErrors": netPacketsOutboundErrors,
       "netOutputQueueLength": netOutputQueueLength,
       "pdiskphysicalDiskTable": pdiskphysicalDiskTable,
       "pdiskphysicalDiskEntry": pdiskphysicalDiskEntry,
       "pdiskphysicalDiskIndex": pdiskphysicalDiskIndex,
       "pdiskphysicalDiskInstance": pdiskphysicalDiskInstance,
       "pdiskCurrentDiskQueueLength": pdiskCurrentDiskQueueLength,
       "pdiskPercentDiskTime": pdiskPercentDiskTime,
       "pdiskAvgDiskQueueLength": pdiskAvgDiskQueueLength,
       "pdiskPercentDiskReadTime": pdiskPercentDiskReadTime,
       "pdiskAvgDiskReadQueueLength": pdiskAvgDiskReadQueueLength,
       "pdiskPercentDiskWriteTime": pdiskPercentDiskWriteTime,
       "pdiskAvgDiskWriteQueueLength": pdiskAvgDiskWriteQueueLength,
       "pdiskAvgDiskSecPerTransfer": pdiskAvgDiskSecPerTransfer,
       "pdiskAvgDiskSecPerRead": pdiskAvgDiskSecPerRead,
       "pdiskAvgDiskSecPerWrite": pdiskAvgDiskSecPerWrite,
       "pdiskDiskTransfersPerSec": pdiskDiskTransfersPerSec,
       "pdiskDiskReadsPerSec": pdiskDiskReadsPerSec,
       "pdiskDiskWritesPerSec": pdiskDiskWritesPerSec,
       "pdiskDiskBytesPerSec": pdiskDiskBytesPerSec,
       "pdiskDiskReadBytesPerSec": pdiskDiskReadBytesPerSec,
       "pdiskDiskWriteBytesPerSec": pdiskDiskWriteBytesPerSec,
       "ldisklogicalDiskTable": ldisklogicalDiskTable,
       "ldisklogicalDiskEntry": ldisklogicalDiskEntry,
       "ldisklogicalDiskIndex": ldisklogicalDiskIndex,
       "ldisklogicalDiskInstance": ldisklogicalDiskInstance,
       "ldiskPercentFreeSpace": ldiskPercentFreeSpace,
       "ldiskFreeMegabytes": ldiskFreeMegabytes,
       "ldiskCurrentDiskQueueLength": ldiskCurrentDiskQueueLength,
       "ldiskPercentDiskTime": ldiskPercentDiskTime,
       "ldiskAvgDiskQueueLength": ldiskAvgDiskQueueLength,
       "ldiskPercentDiskReadTime": ldiskPercentDiskReadTime,
       "ldiskAvgDiskReadQueueLength": ldiskAvgDiskReadQueueLength,
       "ldiskPercentDiskWriteTime": ldiskPercentDiskWriteTime,
       "ldiskAvgDiskWriteQueueLength": ldiskAvgDiskWriteQueueLength,
       "ldiskAvgDiskSecPerTransfer": ldiskAvgDiskSecPerTransfer,
       "ldiskAvgDiskSecPerRead": ldiskAvgDiskSecPerRead,
       "ldiskAvgDiskSecPerWrite": ldiskAvgDiskSecPerWrite,
       "ldiskDiskTransfersPerSec": ldiskDiskTransfersPerSec,
       "ldiskDiskReadsPerSec": ldiskDiskReadsPerSec,
       "ldiskDiskWritesPerSec": ldiskDiskWritesPerSec,
       "ldiskDiskBytesPerSec": ldiskDiskBytesPerSec,
       "ldiskDiskReadBytesPerSec": ldiskDiskReadBytesPerSec,
       "ldiskDiskWriteBytesPerSec": ldiskDiskWriteBytesPerSec,
       "pagefilepaging-FileTable": pagefilepaging_FileTable,
       "pagefilepaging-FileEntry": pagefilepaging_FileEntry,
       "pagefilepaging-FileIndex": pagefilepaging_FileIndex,
       "pagefilepaging-FileInstance": pagefilepaging_FileInstance,
       "pagefilePercentUsage": pagefilePercentUsage,
       "pagefilePercentUsagePeak": pagefilePercentUsagePeak,
       "processprocessTable": processprocessTable,
       "processprocessEntry": processprocessEntry,
       "processprocessIndex": processprocessIndex,
       "processprocessInstance": processprocessInstance,
       "processPercentProcessorTime": processPercentProcessorTime,
       "processPercentUserTime": processPercentUserTime,
       "processPercentPrivilegedTime": processPercentPrivilegedTime,
       "processVirtualBytesPeak": processVirtualBytesPeak,
       "processVirtualBytes": processVirtualBytes,
       "processPageFaultsPerSec": processPageFaultsPerSec,
       "processWorkingSetPeak": processWorkingSetPeak,
       "processWorkingSet": processWorkingSet,
       "processPageFileBytesPeak": processPageFileBytesPeak,
       "processPageFileBytes": processPageFileBytes,
       "processPrivateBytes": processPrivateBytes,
       "processThreadCount": processThreadCount,
       "processPriorityBase": processPriorityBase,
       "processElapsedTime": processElapsedTime,
       "processIDProcess": processIDProcess,
       "processPoolPagedBytes": processPoolPagedBytes,
       "processPoolNonpagedBytes": processPoolNonpagedBytes,
       "processHandleCount": processHandleCount,
       "redirector": redirector,
       "redirectorBytesTotalPerSec": redirectorBytesTotalPerSec,
       "redirectorFileDataOperationsPerSec": redirectorFileDataOperationsPerSec,
       "redirectorPacketsPerSec": redirectorPacketsPerSec,
       "redirectorBytesReceivedPerSec": redirectorBytesReceivedPerSec,
       "redirectorPacketsReceivedPerSec": redirectorPacketsReceivedPerSec,
       "redirectorReadBytesPagingPerSec": redirectorReadBytesPagingPerSec,
       "redirectorReadBytesNon-PagingPerSec": redirectorReadBytesNon_PagingPerSec,
       "redirectorReadBytesCachePerSec": redirectorReadBytesCachePerSec,
       "redirectorReadBytesNetworkPerSec": redirectorReadBytesNetworkPerSec,
       "redirectorBytesTransmittedPerSec": redirectorBytesTransmittedPerSec,
       "redirectorPacketsTransmittedPerSec": redirectorPacketsTransmittedPerSec,
       "redirectorWriteBytesPagingPerSec": redirectorWriteBytesPagingPerSec,
       "redirectorWriteBytesNon-PagingPerSec": redirectorWriteBytesNon_PagingPerSec,
       "redirectorWriteBytesCachePerSec": redirectorWriteBytesCachePerSec,
       "redirectorWriteBytesNetworkPerSec": redirectorWriteBytesNetworkPerSec,
       "redirectorFileReadOperationsPerSec": redirectorFileReadOperationsPerSec,
       "redirectorReadOperationsRandomPerSec": redirectorReadOperationsRandomPerSec,
       "redirectorReadPacketsPerSec": redirectorReadPacketsPerSec,
       "redirectorReadsLargePerSec": redirectorReadsLargePerSec,
       "redirectorReadPacketsSmallPerSec": redirectorReadPacketsSmallPerSec,
       "redirectorFileWriteOperationsPerSec": redirectorFileWriteOperationsPerSec,
       "redirectorWriteOperationsRandomPerSec": redirectorWriteOperationsRandomPerSec,
       "redirectorWritePacketsPerSec": redirectorWritePacketsPerSec,
       "redirectorWritesLargePerSec": redirectorWritesLargePerSec,
       "redirectorWritePacketsSmallPerSec": redirectorWritePacketsSmallPerSec,
       "redirectorReadsDeniedPerSec": redirectorReadsDeniedPerSec,
       "redirectorWritesDeniedPerSec": redirectorWritesDeniedPerSec,
       "redirectorNetworkErrorsPerSec": redirectorNetworkErrorsPerSec,
       "redirectorServerSessions": redirectorServerSessions,
       "redirectorServerReconnects": redirectorServerReconnects,
       "redirectorConnectsCore": redirectorConnectsCore,
       "redirectorConnectsLanManager20": redirectorConnectsLanManager20,
       "redirectorConnectsLanManager21": redirectorConnectsLanManager21,
       "redirectorConnectsWindowsNT": redirectorConnectsWindowsNT,
       "redirectorServerDisconnects": redirectorServerDisconnects,
       "redirectorServerSessionsHung": redirectorServerSessionsHung,
       "redirectorCurrentCommands": redirectorCurrentCommands,
       "tCP": tCP,
       "tcpSegmentsPerSec": tcpSegmentsPerSec,
       "tcpConnectionsEstablished": tcpConnectionsEstablished,
       "tcpConnectionsActive": tcpConnectionsActive,
       "tcpConnectionsPassive": tcpConnectionsPassive,
       "tcpConnectionFailures": tcpConnectionFailures,
       "tcpConnectionsReset": tcpConnectionsReset,
       "tcpSegmentsReceivedPerSec": tcpSegmentsReceivedPerSec,
       "tcpSegmentsSentPerSec": tcpSegmentsSentPerSec,
       "tcpSegmentsRetransmittedPerSec": tcpSegmentsRetransmittedPerSec,
       "iP": iP,
       "ipDatagramsPerSec": ipDatagramsPerSec,
       "ipDatagramsReceivedPerSec": ipDatagramsReceivedPerSec,
       "ipDatagramsReceivedHeaderErrors": ipDatagramsReceivedHeaderErrors,
       "ipDatagramsReceivedAddressErrors": ipDatagramsReceivedAddressErrors,
       "ipDatagramsForwardedPerSec": ipDatagramsForwardedPerSec,
       "ipDatagramsReceivedUnknownProtocol": ipDatagramsReceivedUnknownProtocol,
       "ipDatagramsReceivedDiscarded": ipDatagramsReceivedDiscarded,
       "ipDatagramsReceivedDeliveredPerSec": ipDatagramsReceivedDeliveredPerSec,
       "ipDatagramsSentPerSec": ipDatagramsSentPerSec,
       "ipDatagramsOutboundDiscarded": ipDatagramsOutboundDiscarded,
       "ipDatagramsOutboundNoRoute": ipDatagramsOutboundNoRoute,
       "ipFragmentsReceivedPerSec": ipFragmentsReceivedPerSec,
       "ipFragmentsRe-assembledPerSec": ipFragmentsRe_assembledPerSec,
       "ipFragmentRe-assemblyFailures": ipFragmentRe_assemblyFailures,
       "ipFragmentedDatagramsPerSec": ipFragmentedDatagramsPerSec,
       "ipFragmentationFailures": ipFragmentationFailures,
       "ipFragmentsCreatedPerSec": ipFragmentsCreatedPerSec,
       "uDP": uDP,
       "udpDatagramsPerSec": udpDatagramsPerSec,
       "udpDatagramsReceivedPerSec": udpDatagramsReceivedPerSec,
       "udpDatagramsNoPortPerSec": udpDatagramsNoPortPerSec,
       "udpDatagramsReceivedErrors": udpDatagramsReceivedErrors,
       "udpDatagramsSentPerSec": udpDatagramsSentPerSec,
       "netbeuinetBEUITable": netbeuinetBEUITable,
       "netbeuinetBEUIEntry": netbeuinetBEUIEntry,
       "netbeuinetBEUIIndex": netbeuinetBEUIIndex,
       "netbeuinetBEUIInstance": netbeuinetBEUIInstance,
       "netbeuiDatagramsPerSec": netbeuiDatagramsPerSec,
       "netbeuiDatagramBytesPerSec": netbeuiDatagramBytesPerSec,
       "netbeuiPacketsPerSec": netbeuiPacketsPerSec,
       "netbeuiFramesPerSec": netbeuiFramesPerSec,
       "netbeuiFrameBytesPerSec": netbeuiFrameBytesPerSec,
       "netbeuiBytesTotalPerSec": netbeuiBytesTotalPerSec,
       "netbeuiConnectionsOpen": netbeuiConnectionsOpen,
       "netbeuiConnectionsNoRetries": netbeuiConnectionsNoRetries,
       "netbeuiConnectionsWithRetries": netbeuiConnectionsWithRetries,
       "netbeuiDisconnectsLocal": netbeuiDisconnectsLocal,
       "netbeuiDisconnectsRemote": netbeuiDisconnectsRemote,
       "netbeuiFailuresLink": netbeuiFailuresLink,
       "netbeuiFailuresAdapter": netbeuiFailuresAdapter,
       "netbeuiConnectionSessionTimeouts": netbeuiConnectionSessionTimeouts,
       "netbeuiConnectionsCanceled": netbeuiConnectionsCanceled,
       "netbeuiFailuresResourceRemote": netbeuiFailuresResourceRemote,
       "netbeuiFailuresResourceLocal": netbeuiFailuresResourceLocal,
       "netbeuiFailuresNotFound": netbeuiFailuresNotFound,
       "netbeuiFailuresNoListen": netbeuiFailuresNoListen,
       "netbeuiDatagramsSentPerSec": netbeuiDatagramsSentPerSec,
       "netbeuiDatagramBytesSentPerSec": netbeuiDatagramBytesSentPerSec,
       "netbeuiDatagramsReceivedPerSec": netbeuiDatagramsReceivedPerSec,
       "netbeuiDatagramBytesReceivedPerSec": netbeuiDatagramBytesReceivedPerSec,
       "netbeuiPacketsSentPerSec": netbeuiPacketsSentPerSec,
       "netbeuiPacketsReceivedPerSec": netbeuiPacketsReceivedPerSec,
       "netbeuiFramesSentPerSec": netbeuiFramesSentPerSec,
       "netbeuiFrameBytesSentPerSec": netbeuiFrameBytesSentPerSec,
       "netbeuiFramesReceivedPerSec": netbeuiFramesReceivedPerSec,
       "netbeuiFrameBytesReceivedPerSec": netbeuiFrameBytesReceivedPerSec,
       "netbeuiFramesRe-SentPerSec": netbeuiFramesRe_SentPerSec,
       "netbeuiFrameBytesRe-SentPerSec": netbeuiFrameBytesRe_SentPerSec,
       "netbeuiFramesRejectedPerSec": netbeuiFramesRejectedPerSec,
       "netbeuiFrameBytesRejectedPerSec": netbeuiFrameBytesRejectedPerSec,
       "netbeuiExpirationsResponse": netbeuiExpirationsResponse,
       "netbeuiExpirationsAck": netbeuiExpirationsAck,
       "netbeuiWindowSendMaximum": netbeuiWindowSendMaximum,
       "netbeuiWindowSendAverage": netbeuiWindowSendAverage,
       "netbeuiPiggybackAckQueuedPerSec": netbeuiPiggybackAckQueuedPerSec,
       "netbeuiPiggybackAckTimeouts": netbeuiPiggybackAckTimeouts,
       "nbtconnnBT-ConnectionTable": nbtconnnBT_ConnectionTable,
       "nbtconnnBT-ConnectionEntry": nbtconnnBT_ConnectionEntry,
       "nbtconnnBT-ConnectionIndex": nbtconnnBT_ConnectionIndex,
       "nbtconnnBT-ConnectionInstance": nbtconnnBT_ConnectionInstance,
       "nbtconnBytesReceivedPerSec": nbtconnBytesReceivedPerSec,
       "nbtconnBytesSentPerSec": nbtconnBytesSentPerSec,
       "nbtconnBytesTotalPerSec": nbtconnBytesTotalPerSec,
       "nwlinkipxnWLink-IPXTable": nwlinkipxnWLink_IPXTable,
       "nwlinkipxnWLink-IPXEntry": nwlinkipxnWLink_IPXEntry,
       "nwlinkipxnWLink-IPXIndex": nwlinkipxnWLink_IPXIndex,
       "nwlinkipxnWLink-IPXInstance": nwlinkipxnWLink_IPXInstance,
       "nwlinkipxDatagramsPerSec": nwlinkipxDatagramsPerSec,
       "nwlinkipxDatagramBytesPerSec": nwlinkipxDatagramBytesPerSec,
       "nwlinkipxPacketsPerSec": nwlinkipxPacketsPerSec,
       "nwlinkipxFramesPerSec": nwlinkipxFramesPerSec,
       "nwlinkipxFrameBytesPerSec": nwlinkipxFrameBytesPerSec,
       "nwlinkipxBytesTotalPerSec": nwlinkipxBytesTotalPerSec,
       "nwlinkipxConnectionsOpen": nwlinkipxConnectionsOpen,
       "nwlinkipxConnectionsNoRetries": nwlinkipxConnectionsNoRetries,
       "nwlinkipxConnectionsWithRetries": nwlinkipxConnectionsWithRetries,
       "nwlinkipxDisconnectsLocal": nwlinkipxDisconnectsLocal,
       "nwlinkipxDisconnectsRemote": nwlinkipxDisconnectsRemote,
       "nwlinkipxFailuresLink": nwlinkipxFailuresLink,
       "nwlinkipxFailuresAdapter": nwlinkipxFailuresAdapter,
       "nwlinkipxConnectionSessionTimeouts": nwlinkipxConnectionSessionTimeouts,
       "nwlinkipxConnectionsCanceled": nwlinkipxConnectionsCanceled,
       "nwlinkipxFailuresResourceRemote": nwlinkipxFailuresResourceRemote,
       "nwlinkipxFailuresResourceLocal": nwlinkipxFailuresResourceLocal,
       "nwlinkipxFailuresNotFound": nwlinkipxFailuresNotFound,
       "nwlinkipxFailuresNoListen": nwlinkipxFailuresNoListen,
       "nwlinkipxDatagramsSentPerSec": nwlinkipxDatagramsSentPerSec,
       "nwlinkipxDatagramBytesSentPerSec": nwlinkipxDatagramBytesSentPerSec,
       "nwlinkipxDatagramsReceivedPerSec": nwlinkipxDatagramsReceivedPerSec,
       "nwlinkipxDatagramBytesReceivedPerSec": nwlinkipxDatagramBytesReceivedPerSec,
       "nwlinkipxPacketsSentPerSec": nwlinkipxPacketsSentPerSec,
       "nwlinkipxPacketsReceivedPerSec": nwlinkipxPacketsReceivedPerSec,
       "nwlinkipxFramesSentPerSec": nwlinkipxFramesSentPerSec,
       "nwlinkipxFrameBytesSentPerSec": nwlinkipxFrameBytesSentPerSec,
       "nwlinkipxFramesReceivedPerSec": nwlinkipxFramesReceivedPerSec,
       "nwlinkipxFrameBytesReceivedPerSec": nwlinkipxFrameBytesReceivedPerSec,
       "nwlinkipxFramesRe-SentPerSec": nwlinkipxFramesRe_SentPerSec,
       "nwlinkipxFrameBytesRe-SentPerSec": nwlinkipxFrameBytesRe_SentPerSec,
       "nwlinkipxFramesRejectedPerSec": nwlinkipxFramesRejectedPerSec,
       "nwlinkipxFrameBytesRejectedPerSec": nwlinkipxFrameBytesRejectedPerSec,
       "nwlinkipxExpirationsResponse": nwlinkipxExpirationsResponse,
       "nwlinkipxExpirationsAck": nwlinkipxExpirationsAck,
       "nwlinkipxWindowSendMaximum": nwlinkipxWindowSendMaximum,
       "nwlinkipxWindowSendAverage": nwlinkipxWindowSendAverage,
       "nwlinkipxPiggybackAckQueuedPerSec": nwlinkipxPiggybackAckQueuedPerSec,
       "nwlinkipxPiggybackAckTimeouts": nwlinkipxPiggybackAckTimeouts,
       "nwlinkspxnWLink-SPXTable": nwlinkspxnWLink_SPXTable,
       "nwlinkspxnWLink-SPXEntry": nwlinkspxnWLink_SPXEntry,
       "nwlinkspxnWLink-SPXIndex": nwlinkspxnWLink_SPXIndex,
       "nwlinkspxnWLink-SPXInstance": nwlinkspxnWLink_SPXInstance,
       "nwlinkspxDatagramsPerSec": nwlinkspxDatagramsPerSec,
       "nwlinkspxDatagramBytesPerSec": nwlinkspxDatagramBytesPerSec,
       "nwlinkspxPacketsPerSec": nwlinkspxPacketsPerSec,
       "nwlinkspxFramesPerSec": nwlinkspxFramesPerSec,
       "nwlinkspxFrameBytesPerSec": nwlinkspxFrameBytesPerSec,
       "nwlinkspxBytesTotalPerSec": nwlinkspxBytesTotalPerSec,
       "nwlinkspxConnectionsOpen": nwlinkspxConnectionsOpen,
       "nwlinkspxConnectionsNoRetries": nwlinkspxConnectionsNoRetries,
       "nwlinkspxConnectionsWithRetries": nwlinkspxConnectionsWithRetries,
       "nwlinkspxDisconnectsLocal": nwlinkspxDisconnectsLocal,
       "nwlinkspxDisconnectsRemote": nwlinkspxDisconnectsRemote,
       "nwlinkspxFailuresLink": nwlinkspxFailuresLink,
       "nwlinkspxFailuresAdapter": nwlinkspxFailuresAdapter,
       "nwlinkspxConnectionSessionTimeouts": nwlinkspxConnectionSessionTimeouts,
       "nwlinkspxConnectionsCanceled": nwlinkspxConnectionsCanceled,
       "nwlinkspxFailuresResourceRemote": nwlinkspxFailuresResourceRemote,
       "nwlinkspxFailuresResourceLocal": nwlinkspxFailuresResourceLocal,
       "nwlinkspxFailuresNotFound": nwlinkspxFailuresNotFound,
       "nwlinkspxFailuresNoListen": nwlinkspxFailuresNoListen,
       "nwlinkspxDatagramsSentPerSec": nwlinkspxDatagramsSentPerSec,
       "nwlinkspxDatagramBytesSentPerSec": nwlinkspxDatagramBytesSentPerSec,
       "nwlinkspxDatagramsReceivedPerSec": nwlinkspxDatagramsReceivedPerSec,
       "nwlinkspxDatagramBytesReceivedPerSec": nwlinkspxDatagramBytesReceivedPerSec,
       "nwlinkspxPacketsSentPerSec": nwlinkspxPacketsSentPerSec,
       "nwlinkspxPacketsReceivedPerSec": nwlinkspxPacketsReceivedPerSec,
       "nwlinkspxFramesSentPerSec": nwlinkspxFramesSentPerSec,
       "nwlinkspxFrameBytesSentPerSec": nwlinkspxFrameBytesSentPerSec,
       "nwlinkspxFramesReceivedPerSec": nwlinkspxFramesReceivedPerSec,
       "nwlinkspxFrameBytesReceivedPerSec": nwlinkspxFrameBytesReceivedPerSec,
       "nwlinkspxFramesRe-SentPerSec": nwlinkspxFramesRe_SentPerSec,
       "nwlinkspxFrameBytesRe-SentPerSec": nwlinkspxFrameBytesRe_SentPerSec,
       "nwlinkspxFramesRejectedPerSec": nwlinkspxFramesRejectedPerSec,
       "nwlinkspxFrameBytesRejectedPerSec": nwlinkspxFrameBytesRejectedPerSec,
       "nwlinkspxExpirationsResponse": nwlinkspxExpirationsResponse,
       "nwlinkspxExpirationsAck": nwlinkspxExpirationsAck,
       "nwlinkspxWindowSendMaximum": nwlinkspxWindowSendMaximum,
       "nwlinkspxWindowSendAverage": nwlinkspxWindowSendAverage,
       "nwlinkspxPiggybackAckQueuedPerSec": nwlinkspxPiggybackAckQueuedPerSec,
       "nwlinkspxPiggybackAckTimeouts": nwlinkspxPiggybackAckTimeouts,
       "rAS-Total": rAS_Total,
       "rastotalBytesTransmitted": rastotalBytesTransmitted,
       "rastotalBytesReceived": rastotalBytesReceived,
       "rastotalFramesTransmitted": rastotalFramesTransmitted,
       "rastotalFramesReceived": rastotalFramesReceived,
       "rastotalPercentCompressionOut": rastotalPercentCompressionOut,
       "rastotalPercentCompressionIn": rastotalPercentCompressionIn,
       "rastotalCRCErrors": rastotalCRCErrors,
       "rastotalTimeoutErrors": rastotalTimeoutErrors,
       "rastotalSerialOverrunErrors": rastotalSerialOverrunErrors,
       "rastotalAlignmentErrors": rastotalAlignmentErrors,
       "rastotalBufferOverrunErrors": rastotalBufferOverrunErrors,
       "rastotalTotalErrors": rastotalTotalErrors,
       "rastotalBytesTransmittedPerSec": rastotalBytesTransmittedPerSec,
       "rastotalBytesReceivedPerSec": rastotalBytesReceivedPerSec,
       "rastotalFramesTransmittedPerSec": rastotalFramesTransmittedPerSec,
       "rastotalFramesReceivedPerSec": rastotalFramesReceivedPerSec,
       "rastotalTotalErrorsPerSec": rastotalTotalErrorsPerSec,
       "rastotalTotalConnections": rastotalTotalConnections,
       "server": server,
       "serverBytesTotalPerSec": serverBytesTotalPerSec,
       "serverBytesReceivedPerSec": serverBytesReceivedPerSec,
       "serverBytesTransmittedPerSec": serverBytesTransmittedPerSec,
       "serverSessionsTimedOut": serverSessionsTimedOut,
       "serverSessionsErroredOut": serverSessionsErroredOut,
       "serverSessionsLoggedOff": serverSessionsLoggedOff,
       "serverSessionsForcedOff": serverSessionsForcedOff,
       "serverErrorsLogon": serverErrorsLogon,
       "serverErrorsAccessPermissions": serverErrorsAccessPermissions,
       "serverErrorsGrantedAccess": serverErrorsGrantedAccess,
       "serverErrorsSystem": serverErrorsSystem,
       "serverBlockingRequestsRejected": serverBlockingRequestsRejected,
       "serverWorkItemShortages": serverWorkItemShortages,
       "serverFilesOpenedTotal": serverFilesOpenedTotal,
       "serverFilesOpen": serverFilesOpen,
       "serverServerSessions": serverServerSessions,
       "serverFileDirectorySearches": serverFileDirectorySearches,
       "serverPoolNonpagedBytes": serverPoolNonpagedBytes,
       "serverPoolNonpagedFailures": serverPoolNonpagedFailures,
       "serverPoolNonpagedPeak": serverPoolNonpagedPeak,
       "serverPoolPagedBytes": serverPoolPagedBytes,
       "serverPoolPagedFailures": serverPoolPagedFailures,
       "serverPoolPagedPeak": serverPoolPagedPeak,
       "serverContextBlocksQueuedPerSec": serverContextBlocksQueuedPerSec,
       "serverLogonPerSec": serverLogonPerSec,
       "serverLogonTotal": serverLogonTotal,
       "srvrqueuesserver-Work-QueuesTable": srvrqueuesserver_Work_QueuesTable,
       "srvrqueuesserver-Work-QueuesEntry": srvrqueuesserver_Work_QueuesEntry,
       "srvrqueuesserver-Work-QueuesIndex": srvrqueuesserver_Work_QueuesIndex,
       "srvrqueuesserver-Work-QueuesInstance": srvrqueuesserver_Work_QueuesInstance,
       "srvrqueuesQueueLength": srvrqueuesQueueLength,
       "srvrqueuesActiveThreads": srvrqueuesActiveThreads,
       "srvrqueuesAvailableThreads": srvrqueuesAvailableThreads,
       "srvrqueuesAvailableWorkItems": srvrqueuesAvailableWorkItems,
       "srvrqueuesBorrowedWorkItems": srvrqueuesBorrowedWorkItems,
       "srvrqueuesWorkItemShortages": srvrqueuesWorkItemShortages,
       "srvrqueuesCurrentClients": srvrqueuesCurrentClients,
       "srvrqueuesBytesReceivedPerSec": srvrqueuesBytesReceivedPerSec,
       "srvrqueuesBytesSentPerSec": srvrqueuesBytesSentPerSec,
       "srvrqueuesBytesTransferredPerSec": srvrqueuesBytesTransferredPerSec,
       "srvrqueuesReadOperationsPerSec": srvrqueuesReadOperationsPerSec,
       "srvrqueuesReadBytesPerSec": srvrqueuesReadBytesPerSec,
       "srvrqueuesWriteOperationsPerSec": srvrqueuesWriteOperationsPerSec,
       "srvrqueuesWriteBytesPerSec": srvrqueuesWriteBytesPerSec,
       "srvrqueuesTotalBytesPerSec": srvrqueuesTotalBytesPerSec,
       "srvrqueuesTotalOperationsPerSec": srvrqueuesTotalOperationsPerSec,
       "srvrqueuesContextBlocksQueuedPerSec": srvrqueuesContextBlocksQueuedPerSec,
       "cache": cache,
       "cacheDataMapsPerSec": cacheDataMapsPerSec,
       "cacheSyncDataMapsPerSec": cacheSyncDataMapsPerSec,
       "cacheAsyncDataMapsPerSec": cacheAsyncDataMapsPerSec,
       "cacheDataMapHitsPercent": cacheDataMapHitsPercent,
       "cacheDataMapPinsPerSec": cacheDataMapPinsPerSec,
       "cachePinReadsPerSec": cachePinReadsPerSec,
       "cacheSyncPinReadsPerSec": cacheSyncPinReadsPerSec,
       "cacheAsyncPinReadsPerSec": cacheAsyncPinReadsPerSec,
       "cachePinReadHitsPercent": cachePinReadHitsPercent,
       "cacheCopyReadsPerSec": cacheCopyReadsPerSec,
       "cacheSyncCopyReadsPerSec": cacheSyncCopyReadsPerSec,
       "cacheAsyncCopyReadsPerSec": cacheAsyncCopyReadsPerSec,
       "cacheCopyReadHitsPercent": cacheCopyReadHitsPercent,
       "cacheMDLReadsPerSec": cacheMDLReadsPerSec,
       "cacheSyncMDLReadsPerSec": cacheSyncMDLReadsPerSec,
       "cacheAsyncMDLReadsPerSec": cacheAsyncMDLReadsPerSec,
       "cacheMDLReadHitsPercent": cacheMDLReadHitsPercent,
       "cacheReadAheadsPerSec": cacheReadAheadsPerSec,
       "cacheFastReadsPerSec": cacheFastReadsPerSec,
       "cacheSyncFastReadsPerSec": cacheSyncFastReadsPerSec,
       "cacheAsyncFastReadsPerSec": cacheAsyncFastReadsPerSec,
       "cacheFastReadResourceMissesPerSec": cacheFastReadResourceMissesPerSec,
       "cacheFastReadNotPossiblesPerSec": cacheFastReadNotPossiblesPerSec,
       "cacheLazyWriteFlushesPerSec": cacheLazyWriteFlushesPerSec,
       "cacheLazyWritePagesPerSec": cacheLazyWritePagesPerSec,
       "cacheDataFlushesPerSec": cacheDataFlushesPerSec,
       "cacheDataFlushPagesPerSec": cacheDataFlushPagesPerSec,
       "mSExchangeMTA": mSExchangeMTA,
       "exchmtaAdjacentMTAAssociations": exchmtaAdjacentMTAAssociations,
       "exchmtaMessagesPerSec": exchmtaMessagesPerSec,
       "exchmtaMessageBytesPerSec": exchmtaMessageBytesPerSec,
       "exchmtaFreeElements": exchmtaFreeElements,
       "exchmtaFreeHeaders": exchmtaFreeHeaders,
       "exchmtaAdminConnections": exchmtaAdminConnections,
       "exchmtaThreadsInUse": exchmtaThreadsInUse,
       "exchmtaWorkQueueLength": exchmtaWorkQueueLength,
       "exchmtaXAPIGateways": exchmtaXAPIGateways,
       "exchmtaXAPIClients": exchmtaXAPIClients,
       "exchmtaDiskFileDeletesPerSec": exchmtaDiskFileDeletesPerSec,
       "exchmtaDiskFileSyncsPerSec": exchmtaDiskFileSyncsPerSec,
       "exchmtaDiskFileOpensPerSec": exchmtaDiskFileOpensPerSec,
       "exchmtaDiskFileReadsPerSec": exchmtaDiskFileReadsPerSec,
       "exchmtaDiskFileWritesPerSec": exchmtaDiskFileWritesPerSec,
       "exchmtaExDSReadCallsPerSec": exchmtaExDSReadCallsPerSec,
       "exchmtaXAPIReceiveBytesPerSec": exchmtaXAPIReceiveBytesPerSec,
       "exchmtaXAPITransmitBytesPerSec": exchmtaXAPITransmitBytesPerSec,
       "exchmtaAdminInterfaceReceiveBytesPerSec": exchmtaAdminInterfaceReceiveBytesPerSec,
       "exchmtaAdminInterfaceTransmitBytesPerSec": exchmtaAdminInterfaceTransmitBytesPerSec,
       "exchmtaLANReceiveBytesPerSec": exchmtaLANReceiveBytesPerSec,
       "exchmtaLANTransmitBytesPerSec": exchmtaLANTransmitBytesPerSec,
       "exchmtaRASReceiveBytesPerSec": exchmtaRASReceiveBytesPerSec,
       "exchmtaRASTransmitBytesPerSec": exchmtaRASTransmitBytesPerSec,
       "exchmtaTCPPerIPReceiveBytesPerSec": exchmtaTCPPerIPReceiveBytesPerSec,
       "exchmtaTCPPerIPTransmitBytesPerSec": exchmtaTCPPerIPTransmitBytesPerSec,
       "exchmtaTP4ReceiveBytesPerSec": exchmtaTP4ReceiveBytesPerSec,
       "exchmtaTP4TransmitBytesPerSec": exchmtaTP4TransmitBytesPerSec,
       "exchmtaX25ReceiveBytesPerSec": exchmtaX25ReceiveBytesPerSec,
       "exchmtaX25TransmitBytesPerSec": exchmtaX25TransmitBytesPerSec,
       "exchmtaDeferredDeliveryMsgs": exchmtaDeferredDeliveryMsgs,
       "exchmtaTotalRecipientsQueued": exchmtaTotalRecipientsQueued,
       "exchmtaTotalSuccessfulConversions": exchmtaTotalSuccessfulConversions,
       "exchmtaTotalFailedConversions": exchmtaTotalFailedConversions,
       "exchmtaTotalLoopsDetected": exchmtaTotalLoopsDetected,
       "exchmtaInboundMessagesTotal": exchmtaInboundMessagesTotal,
       "exchmtaOutboundMessagesTotal": exchmtaOutboundMessagesTotal,
       "exchmtaInboundBytesTotal": exchmtaInboundBytesTotal,
       "exchmtaWorkQueueBytes": exchmtaWorkQueueBytes,
       "exchmtaOutboundBytesTotal": exchmtaOutboundBytesTotal,
       "exchmtaTotalRecipientsInbound": exchmtaTotalRecipientsInbound,
       "exchmtaTotalRecipientsOutbound": exchmtaTotalRecipientsOutbound,
       "exchmtaconnmSExchangeMTA-ConnectionsTable": exchmtaconnmSExchangeMTA_ConnectionsTable,
       "exchmtaconnmSExchangeMTA-ConnectionsEntry": exchmtaconnmSExchangeMTA_ConnectionsEntry,
       "exchmtaconnmSExchangeMTA-ConnectionsIndex": exchmtaconnmSExchangeMTA_ConnectionsIndex,
       "exchmtaconnmSExchangeMTA-ConnectionsInstance": exchmtaconnmSExchangeMTA_ConnectionsInstance,
       "exchmtaconnAssociations": exchmtaconnAssociations,
       "exchmtaconnReceiveBytesPerSec": exchmtaconnReceiveBytesPerSec,
       "exchmtaconnSendBytesPerSec": exchmtaconnSendBytesPerSec,
       "exchmtaconnReceiveMessagesPerSec": exchmtaconnReceiveMessagesPerSec,
       "exchmtaconnSendMessagesPerSec": exchmtaconnSendMessagesPerSec,
       "exchmtaconnQueueLength": exchmtaconnQueueLength,
       "exchmtaconnConnectorIndex": exchmtaconnConnectorIndex,
       "exchmtaconnInboundRejectedTotal": exchmtaconnInboundRejectedTotal,
       "exchmtaconnTotalRecipientsQueued": exchmtaconnTotalRecipientsQueued,
       "exchmtaconnOldestMessageQueued": exchmtaconnOldestMessageQueued,
       "exchmtaconnCurrentInboundAssociations": exchmtaconnCurrentInboundAssociations,
       "exchmtaconnCurrentOutboundAssociations": exchmtaconnCurrentOutboundAssociations,
       "exchmtaconnCumulativeInboundAssociations": exchmtaconnCumulativeInboundAssociations,
       "exchmtaconnCumulativeOutboundAssociations": exchmtaconnCumulativeOutboundAssociations,
       "exchmtaconnLastInboundAssociation": exchmtaconnLastInboundAssociation,
       "exchmtaconnLastOutboundAssociation": exchmtaconnLastOutboundAssociation,
       "exchmtaconnRejectedInboundAssociations": exchmtaconnRejectedInboundAssociations,
       "exchmtaconnFailedOutboundAssociations": exchmtaconnFailedOutboundAssociations,
       "exchmtaconnNextAssociationRetry": exchmtaconnNextAssociationRetry,
       "exchmtaconnInboundRejectReason": exchmtaconnInboundRejectReason,
       "exchmtaconnOutboundFailureReason": exchmtaconnOutboundFailureReason,
       "exchmtaconnInboundMessagesTotal": exchmtaconnInboundMessagesTotal,
       "exchmtaconnOutboundMessagesTotal": exchmtaconnOutboundMessagesTotal,
       "exchmtaconnInboundBytesTotal": exchmtaconnInboundBytesTotal,
       "exchmtaconnQueuedBytes": exchmtaconnQueuedBytes,
       "exchmtaconnOutboundBytesTotal": exchmtaconnOutboundBytesTotal,
       "exchmtaconnTotalRecipientsInbound": exchmtaconnTotalRecipientsInbound,
       "exchmtaconnTotalRecipientsOutbound": exchmtaconnTotalRecipientsOutbound,
       "mSExchangeIMC": mSExchangeIMC,
       "exchimcQueuedMTS-IN": exchimcQueuedMTS_IN,
       "exchimcBytesQueuedMTS-IN": exchimcBytesQueuedMTS_IN,
       "exchimcMessagesEnteringMTS-IN": exchimcMessagesEnteringMTS_IN,
       "exchimcQueuedMTS-OUT": exchimcQueuedMTS_OUT,
       "exchimcBytesQueuedMTS-OUT": exchimcBytesQueuedMTS_OUT,
       "exchimcMessagesEnteringMTS-OUT": exchimcMessagesEnteringMTS_OUT,
       "exchimcMessagesLeavingMTS-OUT": exchimcMessagesLeavingMTS_OUT,
       "exchimcConnectionsInbound": exchimcConnectionsInbound,
       "exchimcConnectionsOutbound": exchimcConnectionsOutbound,
       "exchimcConnectionsTotalOutbound": exchimcConnectionsTotalOutbound,
       "exchimcConnectionsTotalInbound": exchimcConnectionsTotalInbound,
       "exchimcConnectionsTotalRejected": exchimcConnectionsTotalRejected,
       "exchimcConnectionsTotalFailed": exchimcConnectionsTotalFailed,
       "exchimcQueuedOutbound": exchimcQueuedOutbound,
       "exchimcQueuedInbound": exchimcQueuedInbound,
       "exchimcNDRsTotalInbound": exchimcNDRsTotalInbound,
       "exchimcNDRsTotalOutbound": exchimcNDRsTotalOutbound,
       "exchimcTotalInboundKilobytes": exchimcTotalInboundKilobytes,
       "exchimcTotalOutboundKilobytes": exchimcTotalOutboundKilobytes,
       "exchimcInboundMessagesTotal": exchimcInboundMessagesTotal,
       "exchimcOutboundMessagesTotal": exchimcOutboundMessagesTotal,
       "exchimcInboundBytesPerHr": exchimcInboundBytesPerHr,
       "exchimcOutboundBytesPerHr": exchimcOutboundBytesPerHr,
       "exchimcInboundMessagesPerHr": exchimcInboundMessagesPerHr,
       "exchimcOutboundMessagesPerHr": exchimcOutboundMessagesPerHr,
       "exchimcOutboundConnectionsPerHr": exchimcOutboundConnectionsPerHr,
       "exchimcInboundConnectionsPerHr": exchimcInboundConnectionsPerHr,
       "exchimcTotalMessagesQueued": exchimcTotalMessagesQueued,
       "exchimcTotalKilobytesQueued": exchimcTotalKilobytesQueued,
       "exchimcTotalInboundRecipients": exchimcTotalInboundRecipients,
       "exchimcTotalOutboundRecipients": exchimcTotalOutboundRecipients,
       "exchimcTotalRecipientsQueued": exchimcTotalRecipientsQueued,
       "exchimcTotalSuccessfulConversions": exchimcTotalSuccessfulConversions,
       "exchimcTotalFailedConversions": exchimcTotalFailedConversions,
       "exchimcTotalLoopsDetected": exchimcTotalLoopsDetected,
       "mSExchangeIS": mSExchangeIS,
       "exchisRPCPacketsPerSec": exchisRPCPacketsPerSec,
       "exchisRPCOperationsPerSec": exchisRPCOperationsPerSec,
       "exchisReadBytesRPCClientsPerSec": exchisReadBytesRPCClientsPerSec,
       "exchisWriteBytesRPCClientsPerSec": exchisWriteBytesRPCClientsPerSec,
       "exchisPushNotificationsGeneratedPerSec": exchisPushNotificationsGeneratedPerSec,
       "exchisPushNotificationsSkippedPerSec": exchisPushNotificationsSkippedPerSec,
       "exchisRPCRequests": exchisRPCRequests,
       "exchisRPCRequestsPeak": exchisRPCRequestsPeak,
       "exchisUserCount": exchisUserCount,
       "exchisActiveUserCount": exchisActiveUserCount,
       "exchisMaximumUsers": exchisMaximumUsers,
       "exchisAnonymousUserCount": exchisAnonymousUserCount,
       "exchisActiveAnonymousUserCount": exchisActiveAnonymousUserCount,
       "exchisMaximumAnonymousUsers": exchisMaximumAnonymousUsers,
       "exchisConnectionCount": exchisConnectionCount,
       "exchisActiveConnectionCount": exchisActiveConnectionCount,
       "exchisMaximumConnections": exchisMaximumConnections,
       "exchisPushNotificationsCacheSize": exchisPushNotificationsCacheSize,
       "exchisPeakPushNotificationsCacheSize": exchisPeakPushNotificationsCacheSize,
       "exchisDatabaseSessionHitRate": exchisDatabaseSessionHitRate,
       "exchisIMAPMessagesSent": exchisIMAPMessagesSent,
       "exchisIMAPCommandsIssued": exchisIMAPCommandsIssued,
       "exchisIMAPMessageSendRate": exchisIMAPMessageSendRate,
       "exchisIMAPCommandsIssuedRate": exchisIMAPCommandsIssuedRate,
       "exchisPOP3MessagesSent": exchisPOP3MessagesSent,
       "exchisPOP3CommandsIssued": exchisPOP3CommandsIssued,
       "exchisPOP3MessagesSendRate": exchisPOP3MessagesSendRate,
       "exchisPOP3CommandsIssuedRate": exchisPOP3CommandsIssuedRate,
       "exchisNNTPMessagesRead": exchisNNTPMessagesRead,
       "exchisNNTPMessagesPosted": exchisNNTPMessagesPosted,
       "exchisNNTPFailedPosts": exchisNNTPFailedPosts,
       "exchisNewsfeedMessagesReceived": exchisNewsfeedMessagesReceived,
       "exchisNewsfeedInboundRejectedMessages": exchisNewsfeedInboundRejectedMessages,
       "exchisNNTPCommandsIssued": exchisNNTPCommandsIssued,
       "exchisNNTPMessagesReadRate": exchisNNTPMessagesReadRate,
       "exchisNNTPMessagesPostedRate": exchisNNTPMessagesPostedRate,
       "exchisNNTPFailedPostsRate": exchisNNTPFailedPostsRate,
       "exchisNewsfeedMessagesReceivedRate": exchisNewsfeedMessagesReceivedRate,
       "exchisNewsfeedInboundRejectedMessagesRate": exchisNewsfeedInboundRejectedMessagesRate,
       "exchisNNTPCommandsIssuedRate": exchisNNTPCommandsIssuedRate,
       "exchisNewsfeedMessagesSent": exchisNewsfeedMessagesSent,
       "exchisNewsfeedMessagesSentPerSec": exchisNewsfeedMessagesSentPerSec,
       "exchisNewsfeedBytesSent": exchisNewsfeedBytesSent,
       "exchisNewsfeedBytesSentPerSec": exchisNewsfeedBytesSentPerSec,
       "exchisNewsfeedOutboundRejectedMessages": exchisNewsfeedOutboundRejectedMessages,
       "exchisNNTPOutboundConnections": exchisNNTPOutboundConnections,
       "exchisNNTPCurrentOutboundConnections": exchisNNTPCurrentOutboundConnections,
       "exchisNumberOfArticleIndexTableRowsExpired": exchisNumberOfArticleIndexTableRowsExpired,
       "mSExchangeIS-Public": mSExchangeIS_Public,
       "exchispubSendQueueSize": exchispubSendQueueSize,
       "exchispubReceiveQueueSize": exchispubReceiveQueueSize,
       "exchispubCategorizationCount": exchispubCategorizationCount,
       "exchispubMessagesDelivered": exchispubMessagesDelivered,
       "exchispubMessageRecipientsDelivered": exchispubMessageRecipientsDelivered,
       "exchispubMessagesSent": exchispubMessagesSent,
       "exchispubMessagesSubmitted": exchispubMessagesSubmitted,
       "exchispubSingleInstanceRatio": exchispubSingleInstanceRatio,
       "exchispubMessagesDeliveredPerMin": exchispubMessagesDeliveredPerMin,
       "exchispubMessageRecipientsDeliveredPerMin": exchispubMessageRecipientsDeliveredPerMin,
       "exchispubMessagesSentPerMin": exchispubMessagesSentPerMin,
       "exchispubMessageSubmittedPerMin": exchispubMessageSubmittedPerMin,
       "exchispubAverageTimeForDelivery": exchispubAverageTimeForDelivery,
       "exchispubAverageTimeForLocalDelivery": exchispubAverageTimeForLocalDelivery,
       "exchispubTotalSizeOfRecoverableItems": exchispubTotalSizeOfRecoverableItems,
       "exchispubTotalCountOfRecoverableItems": exchispubTotalCountOfRecoverableItems,
       "exchispubReplicationMessagesSent": exchispubReplicationMessagesSent,
       "exchispubReplicationFolderTreeMessagesSent": exchispubReplicationFolderTreeMessagesSent,
       "exchispubReplicationFolderChangesSent": exchispubReplicationFolderChangesSent,
       "exchispubReplicationFolderDataMessagesSent": exchispubReplicationFolderDataMessagesSent,
       "exchispubReplicationMessageChangesSent": exchispubReplicationMessageChangesSent,
       "exchispubReplicationStatusMessagesSent": exchispubReplicationStatusMessagesSent,
       "exchispubReplicationBackfillRequestsSent": exchispubReplicationBackfillRequestsSent,
       "exchispubReplicationBackfillDataMessagesSent": exchispubReplicationBackfillDataMessagesSent,
       "exchispubReplicationMessagesReceived": exchispubReplicationMessagesReceived,
       "exchispubReplicationFolderTreeMessagesReceived": exchispubReplicationFolderTreeMessagesReceived,
       "exchispubReplicationFolderChangesReceived": exchispubReplicationFolderChangesReceived,
       "exchispubReplicationFolderDataMessagesReceived": exchispubReplicationFolderDataMessagesReceived,
       "exchispubReplicationMessageChangesReceived": exchispubReplicationMessageChangesReceived,
       "exchispubReplicationStatusMessagesReceived": exchispubReplicationStatusMessagesReceived,
       "exchispubReplicationBackfillRequestsReceived": exchispubReplicationBackfillRequestsReceived,
       "exchispubReplicationBackfillDataMessagesReceived": exchispubReplicationBackfillDataMessagesReceived,
       "exchispubReplicationReceiveQueueSize": exchispubReplicationReceiveQueueSize,
       "exchispubNumberOfMessagesExpiredFromPublicFolders": exchispubNumberOfMessagesExpiredFromPublicFolders,
       "exchispubClientLogons": exchispubClientLogons,
       "exchispubActiveClientLogons": exchispubActiveClientLogons,
       "exchispubPeakClientLogons": exchispubPeakClientLogons,
       "exchispubFolderOpensPerSec": exchispubFolderOpensPerSec,
       "exchispubMessageOpensPerSec": exchispubMessageOpensPerSec,
       "mSExchangeIS-Private": mSExchangeIS_Private,
       "exchisprivSendQueueSize": exchisprivSendQueueSize,
       "exchisprivReceiveQueueSize": exchisprivReceiveQueueSize,
       "exchisprivCategorizationCount": exchisprivCategorizationCount,
       "exchisprivMessagesDelivered": exchisprivMessagesDelivered,
       "exchisprivMessageRecipientsDelivered": exchisprivMessageRecipientsDelivered,
       "exchisprivMessagesSent": exchisprivMessagesSent,
       "exchisprivMessagesSubmitted": exchisprivMessagesSubmitted,
       "exchisprivSingleInstanceRatio": exchisprivSingleInstanceRatio,
       "exchisprivMessagesDeliveredPerMin": exchisprivMessagesDeliveredPerMin,
       "exchisprivMessageRecipientsDeliveredPerMin": exchisprivMessageRecipientsDeliveredPerMin,
       "exchisprivMessagesSentPerMin": exchisprivMessagesSentPerMin,
       "exchisprivMessagesSubmittedPerMin": exchisprivMessagesSubmittedPerMin,
       "exchisprivAverageDeliveryTime": exchisprivAverageDeliveryTime,
       "exchisprivAverageLocalDeliveryTime": exchisprivAverageLocalDeliveryTime,
       "exchisprivTotalSizeOfRecoverableItems": exchisprivTotalSizeOfRecoverableItems,
       "exchisprivTotalCountOfRecoverableItems": exchisprivTotalCountOfRecoverableItems,
       "exchisprivClientLogons": exchisprivClientLogons,
       "exchisprivActiveClientLogons": exchisprivActiveClientLogons,
       "exchisprivPeakClientLogons": exchisprivPeakClientLogons,
       "exchisprivLocalDeliveries": exchisprivLocalDeliveries,
       "exchisprivLocalDeliveryRate": exchisprivLocalDeliveryRate,
       "exchisprivFolderOpensPerSec": exchisprivFolderOpensPerSec,
       "exchisprivMessageOpensPerSec": exchisprivMessageOpensPerSec,
       "mSExchangeDS": mSExchangeDS,
       "exchdsAccessViolations": exchdsAccessViolations,
       "exchdsABBrowsesPerSec": exchdsABBrowsesPerSec,
       "exchdsABReadsPerSec": exchdsABReadsPerSec,
       "exchdsExDSReadsPerSec": exchdsExDSReadsPerSec,
       "exchdsReplicationUpdatesPerSec": exchdsReplicationUpdatesPerSec,
       "exchdsThreadsInUse": exchdsThreadsInUse,
       "exchdsABWritesPerSec": exchdsABWritesPerSec,
       "exchdsExDSWritesPerSec": exchdsExDSWritesPerSec,
       "exchdsExDSClientSessions": exchdsExDSClientSessions,
       "exchdsABClientSessions": exchdsABClientSessions,
       "exchdsPendingReplicationSynchronizations": exchdsPendingReplicationSynchronizations,
       "exchdsRemainingReplicationUpdates": exchdsRemainingReplicationUpdates,
       "exchdsObjectsReplicatedOutPerSec": exchdsObjectsReplicatedOutPerSec,
       "exchdsAddressBookViewReadsPerSec": exchdsAddressBookViewReadsPerSec,
       "exchdsAddressBookViewWritesPerSec": exchdsAddressBookViewWritesPerSec,
       "exchdsAddressBookViewModifiesPerSec": exchdsAddressBookViewModifiesPerSec,
       "exchdsLDAPSearches": exchdsLDAPSearches,
       "exchdsLDAPSearchesPerSec": exchdsLDAPSearchesPerSec,
       "web-Proxy-Server-Service": web_Proxy_Server_Service,
       "webproxysrvrUpstreamBytesSentPerSec": webproxysrvrUpstreamBytesSentPerSec,
       "webproxysrvrUpstreamBytesReceivedPerSec": webproxysrvrUpstreamBytesReceivedPerSec,
       "webproxysrvrUpstreamBytesTotalPerSec": webproxysrvrUpstreamBytesTotalPerSec,
       "webproxysrvrClientBytesSentPerSec": webproxysrvrClientBytesSentPerSec,
       "webproxysrvrClientBytesReceivedPerSec": webproxysrvrClientBytesReceivedPerSec,
       "webproxysrvrClientBytesTotalPerSec": webproxysrvrClientBytesTotalPerSec,
       "webproxysrvrSSLClientBytesSentPerSec": webproxysrvrSSLClientBytesSentPerSec,
       "webproxysrvrSSLClientBytesReceivedPerSec": webproxysrvrSSLClientBytesReceivedPerSec,
       "webproxysrvrSSLClientBytesTotalPerSec": webproxysrvrSSLClientBytesTotalPerSec,
       "webproxysrvrSocksClientBytesSentPerSec": webproxysrvrSocksClientBytesSentPerSec,
       "webproxysrvrSocksClientBytesReceivedPerSec": webproxysrvrSocksClientBytesReceivedPerSec,
       "webproxysrvrSocksClientBytesTotalPerSec": webproxysrvrSocksClientBytesTotalPerSec,
       "webproxysrvrCurrentUsers": webproxysrvrCurrentUsers,
       "webproxysrvrTotalUsers": webproxysrvrTotalUsers,
       "webproxysrvrMaximumUsers": webproxysrvrMaximumUsers,
       "webproxysrvrFtpRequests": webproxysrvrFtpRequests,
       "webproxysrvrGopherRequests": webproxysrvrGopherRequests,
       "webproxysrvrHttpRequests": webproxysrvrHttpRequests,
       "webproxysrvrTotalRequests": webproxysrvrTotalRequests,
       "webproxysrvrTotalSuccessfulRequests": webproxysrvrTotalSuccessfulRequests,
       "webproxysrvrTotalFailingRequests": webproxysrvrTotalFailingRequests,
       "webproxysrvrTotalCacheFetches": webproxysrvrTotalCacheFetches,
       "webproxysrvrTotalUpstreamFetches": webproxysrvrTotalUpstreamFetches,
       "webproxysrvrCacheHitRatioPercent": webproxysrvrCacheHitRatioPercent,
       "webproxysrvrSitesDenied": webproxysrvrSitesDenied,
       "webproxysrvrSitesGranted": webproxysrvrSitesGranted,
       "webproxysrvrDNSCacheEntries": webproxysrvrDNSCacheEntries,
       "webproxysrvrDNSRetrievals": webproxysrvrDNSRetrievals,
       "webproxysrvrDNSCacheFlushes": webproxysrvrDNSCacheFlushes,
       "webproxysrvrDNSCacheHits": webproxysrvrDNSCacheHits,
       "webproxysrvrDNSCacheHitsPercent": webproxysrvrDNSCacheHitsPercent,
       "webproxysrvrHTTPSSessions": webproxysrvrHTTPSSessions,
       "webproxysrvrSNEWSSessions": webproxysrvrSNEWSSessions,
       "webproxysrvrUnknownSSLSessions": webproxysrvrUnknownSSLSessions,
       "webproxysrvrTotalSSLSessions": webproxysrvrTotalSSLSessions,
       "webproxysrvrSocksSessions": webproxysrvrSocksSessions,
       "webproxysrvrTotalSocksSessions": webproxysrvrTotalSocksSessions,
       "webproxysrvrTotalSuccessfulSocksSessions": webproxysrvrTotalSuccessfulSocksSessions,
       "webproxysrvrTotalFailedSocksSessions": webproxysrvrTotalFailedSocksSessions,
       "webproxysrvrThreadPoolSize": webproxysrvrThreadPoolSize,
       "webproxysrvrThreadPoolFailures": webproxysrvrThreadPoolFailures,
       "webproxysrvrSSLSessionsScavenged": webproxysrvrSSLSessionsScavenged,
       "webproxysrvrThreadPoolActiveSessions": webproxysrvrThreadPoolActiveSessions,
       "webproxysrvrArrayBytesSentPerSec": webproxysrvrArrayBytesSentPerSec,
       "webproxysrvrArrayBytesReceivedPerSec": webproxysrvrArrayBytesReceivedPerSec,
       "webproxysrvrArrayBytesTotalPerSec": webproxysrvrArrayBytesTotalPerSec,
       "webproxysrvrTotalArrayFetches": webproxysrvrTotalArrayFetches,
       "webproxysrvrReverseBytesSentPerSec": webproxysrvrReverseBytesSentPerSec,
       "webproxysrvrReverseBytesReceivedPerSec": webproxysrvrReverseBytesReceivedPerSec,
       "webproxysrvrReverseBytesTotalPerSec": webproxysrvrReverseBytesTotalPerSec,
       "webproxysrvrTotalReverseFetches": webproxysrvrTotalReverseFetches,
       "webproxysrvrRequestsPerSec": webproxysrvrRequestsPerSec,
       "webproxysrvrFailingRequestsPerSec": webproxysrvrFailingRequestsPerSec,
       "winSock-Proxy-Server": winSock_Proxy_Server,
       "winsockproxysrvrSuccessfulDNSResolutions": winsockproxysrvrSuccessfulDNSResolutions,
       "winsockproxysrvrFailedDNSResolutions": winsockproxysrvrFailedDNSResolutions,
       "winsockproxysrvrPendingDNSResolutions": winsockproxysrvrPendingDNSResolutions,
       "winsockproxysrvrActiveSessions": winsockproxysrvrActiveSessions,
       "winsockproxysrvrActiveTCPConnections": winsockproxysrvrActiveTCPConnections,
       "winsockproxysrvrActiveUDPConnections": winsockproxysrvrActiveUDPConnections,
       "winsockproxysrvrConnectingTCPConnections": winsockproxysrvrConnectingTCPConnections,
       "winsockproxysrvrBack-ConnectingTCPConnections": winsockproxysrvrBack_ConnectingTCPConnections,
       "winsockproxysrvrAcceptingTCPConnections": winsockproxysrvrAcceptingTCPConnections,
       "winsockproxysrvrListeningTCPConnections": winsockproxysrvrListeningTCPConnections,
       "winsockproxysrvrWorkerThreads": winsockproxysrvrWorkerThreads,
       "winsockproxysrvrAvailableWorkerThreads": winsockproxysrvrAvailableWorkerThreads,
       "winsockproxysrvrBytesReadPerSec": winsockproxysrvrBytesReadPerSec,
       "winsockproxysrvrBytesWrittenPerSec": winsockproxysrvrBytesWrittenPerSec,
       "winsockproxysrvrNon-connectedUDPMappings": winsockproxysrvrNon_connectedUDPMappings,
       "winsockproxysrvrDNSCacheEntries": winsockproxysrvrDNSCacheEntries,
       "winsockproxysrvrDNSCacheHits": winsockproxysrvrDNSCacheHits,
       "winsockproxysrvrDNSCacheFlushes": winsockproxysrvrDNSCacheFlushes,
       "winsockproxysrvrDNSRetrievals": winsockproxysrvrDNSRetrievals,
       "winsockproxysrvrDNSCacheHitsPercent": winsockproxysrvrDNSCacheHitsPercent,
       "web-Proxy-Server-Cache": web_Proxy_Server_Cache,
       "webproxysrvrcacheURLsInCache": webproxysrvrcacheURLsInCache,
       "webproxysrvrcacheBytesInCache": webproxysrvrcacheBytesInCache,
       "webproxysrvrcacheTotalBytesCached": webproxysrvrcacheTotalBytesCached,
       "webproxysrvrcacheTotalBytesRetrieved": webproxysrvrcacheTotalBytesRetrieved,
       "webproxysrvrcacheTotalURLsCached": webproxysrvrcacheTotalURLsCached,
       "webproxysrvrcacheTotalURLsRetrieved": webproxysrvrcacheTotalURLsRetrieved,
       "webproxysrvrcacheMaxBytesCached": webproxysrvrcacheMaxBytesCached,
       "webproxysrvrcacheMaxURLsCached": webproxysrvrcacheMaxURLsCached,
       "webproxysrvrcacheTotalActivelyRefreshedURLs": webproxysrvrcacheTotalActivelyRefreshedURLs,
       "webproxysrvrcacheTotalBytesActivelyRefreshed": webproxysrvrcacheTotalBytesActivelyRefreshed,
       "webproxysrvrcacheURLRetrieveRate": webproxysrvrcacheURLRetrieveRate,
       "webproxysrvrcacheBytesRetrievedRate": webproxysrvrcacheBytesRetrievedRate,
       "webproxysrvrcacheURLCommitRate": webproxysrvrcacheURLCommitRate,
       "webproxysrvrcacheBytesCommitedRate": webproxysrvrcacheBytesCommitedRate,
       "webproxysrvrcacheActiveURLRefreshRate": webproxysrvrcacheActiveURLRefreshRate,
       "webproxysrvrcacheActiveRefreshBytesRate": webproxysrvrcacheActiveRefreshBytesRate,
       "telephony": telephony,
       "telephonyLines": telephonyLines,
       "telephonyTelephoneDevices": telephonyTelephoneDevices,
       "telephonyActiveLines": telephonyActiveLines,
       "telephonyActiveTelephones": telephonyActiveTelephones,
       "telephonyOutgoingCallsPerSec": telephonyOutgoingCallsPerSec,
       "telephonyIncomingCallsPerSec": telephonyIncomingCallsPerSec,
       "telephonyClientApps": telephonyClientApps,
       "telephonyCurrentOutgoingCalls": telephonyCurrentOutgoingCalls,
       "telephonyCurrentIncomingCalls": telephonyCurrentIncomingCalls,
       "rasportrAS-PortTable": rasportrAS_PortTable,
       "rasportrAS-PortEntry": rasportrAS_PortEntry,
       "rasportrAS-PortIndex": rasportrAS_PortIndex,
       "rasportrAS-PortInstance": rasportrAS_PortInstance,
       "rasportBytesTransmitted": rasportBytesTransmitted,
       "rasportBytesReceived": rasportBytesReceived,
       "rasportFramesTransmitted": rasportFramesTransmitted,
       "rasportFramesReceived": rasportFramesReceived,
       "rasportPercentCompressionOut": rasportPercentCompressionOut,
       "rasportPercentCompressionIn": rasportPercentCompressionIn,
       "rasportCRCErrors": rasportCRCErrors,
       "rasportTimeoutErrors": rasportTimeoutErrors,
       "rasportSerialOverrunErrors": rasportSerialOverrunErrors,
       "rasportAlignmentErrors": rasportAlignmentErrors,
       "rasportBufferOverrunErrors": rasportBufferOverrunErrors,
       "rasportTotalErrors": rasportTotalErrors,
       "rasportBytesTransmittedPerSec": rasportBytesTransmittedPerSec,
       "rasportBytesReceivedPerSec": rasportBytesReceivedPerSec,
       "rasportFramesTransmittedPerSec": rasportFramesTransmittedPerSec,
       "rasportFramesReceivedPerSec": rasportFramesReceivedPerSec,
       "rasportTotalErrorsPerSec": rasportTotalErrorsPerSec,
       "nwnetbiosnWLink-NetBIOSTable": nwnetbiosnWLink_NetBIOSTable,
       "nwnetbiosnWLink-NetBIOSEntry": nwnetbiosnWLink_NetBIOSEntry,
       "nwnetbiosnWLink-NetBIOSIndex": nwnetbiosnWLink_NetBIOSIndex,
       "nwnetbiosnWLink-NetBIOSInstance": nwnetbiosnWLink_NetBIOSInstance,
       "nwnetbiosDatagramsPerSec": nwnetbiosDatagramsPerSec,
       "nwnetbiosDatagramBytesPerSec": nwnetbiosDatagramBytesPerSec,
       "nwnetbiosPacketsPerSec": nwnetbiosPacketsPerSec,
       "nwnetbiosFramesPerSec": nwnetbiosFramesPerSec,
       "nwnetbiosFrameBytesPerSec": nwnetbiosFrameBytesPerSec,
       "nwnetbiosBytesTotalPerSec": nwnetbiosBytesTotalPerSec,
       "nwnetbiosConnectionsOpen": nwnetbiosConnectionsOpen,
       "nwnetbiosConnectionsNoRetries": nwnetbiosConnectionsNoRetries,
       "nwnetbiosConnectionsWithRetries": nwnetbiosConnectionsWithRetries,
       "nwnetbiosDisconnectsLocal": nwnetbiosDisconnectsLocal,
       "nwnetbiosDisconnectsRemote": nwnetbiosDisconnectsRemote,
       "nwnetbiosFailuresLink": nwnetbiosFailuresLink,
       "nwnetbiosFailuresAdapter": nwnetbiosFailuresAdapter,
       "nwnetbiosConnectionSessionTimeouts": nwnetbiosConnectionSessionTimeouts,
       "nwnetbiosConnectionsCanceled": nwnetbiosConnectionsCanceled,
       "nwnetbiosFailuresResourceRemote": nwnetbiosFailuresResourceRemote,
       "nwnetbiosFailuresResourceLocal": nwnetbiosFailuresResourceLocal,
       "nwnetbiosFailuresNotFound": nwnetbiosFailuresNotFound,
       "nwnetbiosFailuresNoListen": nwnetbiosFailuresNoListen,
       "nwnetbiosDatagramsSentPerSec": nwnetbiosDatagramsSentPerSec,
       "nwnetbiosDatagramBytesSentPerSec": nwnetbiosDatagramBytesSentPerSec,
       "nwnetbiosDatagramsReceivedPerSec": nwnetbiosDatagramsReceivedPerSec,
       "nwnetbiosDatagramBytesReceivedPerSec": nwnetbiosDatagramBytesReceivedPerSec,
       "nwnetbiosPacketsSentPerSec": nwnetbiosPacketsSentPerSec,
       "nwnetbiosPacketsReceivedPerSec": nwnetbiosPacketsReceivedPerSec,
       "nwnetbiosFramesSentPerSec": nwnetbiosFramesSentPerSec,
       "nwnetbiosFrameBytesSentPerSec": nwnetbiosFrameBytesSentPerSec,
       "nwnetbiosFramesReceivedPerSec": nwnetbiosFramesReceivedPerSec,
       "nwnetbiosFrameBytesReceivedPerSec": nwnetbiosFrameBytesReceivedPerSec,
       "nwnetbiosFramesRe-SentPerSec": nwnetbiosFramesRe_SentPerSec,
       "nwnetbiosFrameBytesRe-SentPerSec": nwnetbiosFrameBytesRe_SentPerSec,
       "nwnetbiosFramesRejectedPerSec": nwnetbiosFramesRejectedPerSec,
       "nwnetbiosFrameBytesRejectedPerSec": nwnetbiosFrameBytesRejectedPerSec,
       "nwnetbiosExpirationsResponse": nwnetbiosExpirationsResponse,
       "nwnetbiosExpirationsAck": nwnetbiosExpirationsAck,
       "nwnetbiosWindowSendMaximum": nwnetbiosWindowSendMaximum,
       "nwnetbiosWindowSendAverage": nwnetbiosWindowSendAverage,
       "nwnetbiosPiggybackAckQueuedPerSec": nwnetbiosPiggybackAckQueuedPerSec,
       "nwnetbiosPiggybackAckTimeouts": nwnetbiosPiggybackAckTimeouts,
       "ntsystem": ntsystem,
       "ntsystemFileReadOperationsPerSec": ntsystemFileReadOperationsPerSec,
       "ntsystemFileWriteOperationsPerSec": ntsystemFileWriteOperationsPerSec,
       "ntsystemFileControlOperationsPerSec": ntsystemFileControlOperationsPerSec,
       "ntsystemFileReadBytesPerSec": ntsystemFileReadBytesPerSec,
       "ntsystemFileWriteBytesPerSec": ntsystemFileWriteBytesPerSec,
       "ntsystemFileControlBytesPerSec": ntsystemFileControlBytesPerSec,
       "ntsystemContextSwitchesPerSec": ntsystemContextSwitchesPerSec,
       "ntsystemSystemCallsPerSec": ntsystemSystemCallsPerSec,
       "ntsystemPercentTotalProcessorTime": ntsystemPercentTotalProcessorTime,
       "ntsystemPercentTotalUserTime": ntsystemPercentTotalUserTime,
       "ntsystemPercentTotalPrivilegedTime": ntsystemPercentTotalPrivilegedTime,
       "ntsystemTotalInterruptsPerSec": ntsystemTotalInterruptsPerSec,
       "ntsystemFileDataOperationsPerSec": ntsystemFileDataOperationsPerSec,
       "ntsystemSystemUpTime": ntsystemSystemUpTime,
       "ntsystemProcessorQueueLength": ntsystemProcessorQueueLength,
       "ntsystemAlignmentFixupsPerSec": ntsystemAlignmentFixupsPerSec,
       "ntsystemExceptionDispatchesPerSec": ntsystemExceptionDispatchesPerSec,
       "ntsystemFloatingEmulationsPerSec": ntsystemFloatingEmulationsPerSec,
       "ntsystemPercentTotalDPCTime": ntsystemPercentTotalDPCTime,
       "ntsystemPercentTotalInterruptTime": ntsystemPercentTotalInterruptTime,
       "ntsystemTotalDPCsQueuedPerSec": ntsystemTotalDPCsQueuedPerSec,
       "ntsystemTotalDPCRate": ntsystemTotalDPCRate,
       "ntsystemTotalDPCBypassesPerSec": ntsystemTotalDPCBypassesPerSec,
       "ntsystemTotalAPCBypassesPerSec": ntsystemTotalAPCBypassesPerSec,
       "ntsystemPercentRegistryQuotaInUse": ntsystemPercentRegistryQuotaInUse,
       "packet-Filtering": packet_Filtering,
       "packetfilterTotalDroppedFrames": packetfilterTotalDroppedFrames,
       "packetfilterFramesDroppedDueToFilterDenial": packetfilterFramesDroppedDueToFilterDenial,
       "packetfilterFramesDroppedDueToProtocolViolations": packetfilterFramesDroppedDueToProtocolViolations,
       "packetfilterTotalIncomingConnections": packetfilterTotalIncomingConnections,
       "packetfilterTotalLostLoggingFrames": packetfilterTotalLostLoggingFrames,
       "webserviceweb-ServiceTable": webserviceweb_ServiceTable,
       "webserviceweb-ServiceEntry": webserviceweb_ServiceEntry,
       "webserviceweb-ServiceIndex": webserviceweb_ServiceIndex,
       "webserviceweb-ServiceInstance": webserviceweb_ServiceInstance,
       "webserviceBytesSentPerSec": webserviceBytesSentPerSec,
       "webserviceBytesReceivedPerSec": webserviceBytesReceivedPerSec,
       "webserviceBytesTotalPerSec": webserviceBytesTotalPerSec,
       "webserviceTotalFilesSent": webserviceTotalFilesSent,
       "webserviceFilesSentPerSec": webserviceFilesSentPerSec,
       "webserviceTotalFilesReceived": webserviceTotalFilesReceived,
       "webserviceFilesReceivedPerSec": webserviceFilesReceivedPerSec,
       "webserviceTotalFilesTransferred": webserviceTotalFilesTransferred,
       "webserviceFilesPerSec": webserviceFilesPerSec,
       "webserviceCurrentAnonymousUsers": webserviceCurrentAnonymousUsers,
       "webserviceCurrentNonAnonymousUsers": webserviceCurrentNonAnonymousUsers,
       "webserviceTotalAnonymousUsers": webserviceTotalAnonymousUsers,
       "webserviceAnonymousUsersPerSec": webserviceAnonymousUsersPerSec,
       "webserviceTotalNonAnonymousUsers": webserviceTotalNonAnonymousUsers,
       "webserviceNonAnonymousUsersPerSec": webserviceNonAnonymousUsersPerSec,
       "webserviceMaximumAnonymousUsers": webserviceMaximumAnonymousUsers,
       "webserviceMaximumNonAnonymousUsers": webserviceMaximumNonAnonymousUsers,
       "webserviceCurrentConnections": webserviceCurrentConnections,
       "webserviceMaximumConnections": webserviceMaximumConnections,
       "webserviceTotalConnectionAttempts": webserviceTotalConnectionAttempts,
       "webserviceConnectionAttemptsPerSec": webserviceConnectionAttemptsPerSec,
       "webserviceTotalLogonAttempts": webserviceTotalLogonAttempts,
       "webserviceLogonAttemptsPerSec": webserviceLogonAttemptsPerSec,
       "webserviceTotalGetRequests": webserviceTotalGetRequests,
       "webserviceGetRequestsPerSec": webserviceGetRequestsPerSec,
       "webserviceTotalPostRequests": webserviceTotalPostRequests,
       "webservicePostRequestsPerSec": webservicePostRequestsPerSec,
       "webserviceTotalHeadRequests": webserviceTotalHeadRequests,
       "webserviceHeadRequestsPerSec": webserviceHeadRequestsPerSec,
       "webserviceTotalPutRequests": webserviceTotalPutRequests,
       "webservicePutRequestsPerSec": webservicePutRequestsPerSec,
       "webserviceTotalDeleteRequests": webserviceTotalDeleteRequests,
       "webserviceDeleteRequestsPerSec": webserviceDeleteRequestsPerSec,
       "webserviceTotalTraceRequests": webserviceTotalTraceRequests,
       "webserviceSystemCodeResidentBytes": webserviceSystemCodeResidentBytes,
       "webserviceTotalOtherRequestMethods": webserviceTotalOtherRequestMethods,
       "webserviceOtherRequestMethodsPerSec": webserviceOtherRequestMethodsPerSec,
       "webserviceTotalMethodRequests": webserviceTotalMethodRequests,
       "webserviceTotalMethodRequestsPerSec": webserviceTotalMethodRequestsPerSec,
       "webserviceTotalCGIRequests": webserviceTotalCGIRequests,
       "webserviceCGIRequestsPerSec": webserviceCGIRequestsPerSec,
       "webserviceTotalISAPIExtensionRequests": webserviceTotalISAPIExtensionRequests,
       "webserviceISAPIExtensionRequestsPerSec": webserviceISAPIExtensionRequestsPerSec,
       "webserviceTotalNotFoundErrors": webserviceTotalNotFoundErrors,
       "webserviceNotFoundErrorsPerSec": webserviceNotFoundErrorsPerSec,
       "webserviceCurrentCGIRequests": webserviceCurrentCGIRequests,
       "webserviceCurrentISAPIExtensionRequests": webserviceCurrentISAPIExtensionRequests,
       "webserviceMaximumCGIRequests": webserviceMaximumCGIRequests,
       "webserviceMaximumISAPIExtensionRequests": webserviceMaximumISAPIExtensionRequests,
       "webserviceTotalBlockedAsyncIPerORequests": webserviceTotalBlockedAsyncIPerORequests,
       "webserviceTotalAllowedAsyncIPerORequests": webserviceTotalAllowedAsyncIPerORequests,
       "webserviceTotalRejectedAsyncIPerORequests": webserviceTotalRejectedAsyncIPerORequests,
       "webserviceCurrentBlockedAsyncIPerORequests": webserviceCurrentBlockedAsyncIPerORequests,
       "webserviceMeasuredAsyncIPerOBandwidthUsage": webserviceMeasuredAsyncIPerOBandwidthUsage}
)
