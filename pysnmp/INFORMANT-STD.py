# SNMP MIB module (INFORMANT-STD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-STD
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(InstanceName,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "InstanceName",
    "informant")


# MODULE-IDENTITY

standard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1)
)
standard.setRevisions(
        ("2008-07-11 23:59",
         "2008-03-21 23:08",
         "2005-07-19 18:26",
         "2004-02-29 06:27",
         "2004-01-17 16:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogicalDiskTable_Object = MibTable
logicalDiskTable = _LogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1)
)
if mibBuilder.loadTexts:
    logicalDiskTable.setStatus("current")
_LogicalDiskEntry_Object = MibTableRow
logicalDiskEntry = _LogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1)
)
logicalDiskEntry.setIndexNames(
    (0, "INFORMANT-STD", "lDiskInstance"),
)
if mibBuilder.loadTexts:
    logicalDiskEntry.setStatus("current")
_LDiskInstance_Type = InstanceName
_LDiskInstance_Object = MibTableColumn
lDiskInstance = _LDiskInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 1),
    _LDiskInstance_Type()
)
lDiskInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskInstance.setStatus("current")
_LDiskPercentDiskReadTime_Type = Gauge32
_LDiskPercentDiskReadTime_Object = MibTableColumn
lDiskPercentDiskReadTime = _LDiskPercentDiskReadTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 2),
    _LDiskPercentDiskReadTime_Type()
)
lDiskPercentDiskReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskPercentDiskReadTime.setStatus("current")
_LDiskPercentDiskTime_Type = Gauge32
_LDiskPercentDiskTime_Object = MibTableColumn
lDiskPercentDiskTime = _LDiskPercentDiskTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 3),
    _LDiskPercentDiskTime_Type()
)
lDiskPercentDiskTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskPercentDiskTime.setStatus("current")
_LDiskPercentDiskWriteTime_Type = Gauge32
_LDiskPercentDiskWriteTime_Object = MibTableColumn
lDiskPercentDiskWriteTime = _LDiskPercentDiskWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 4),
    _LDiskPercentDiskWriteTime_Type()
)
lDiskPercentDiskWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskPercentDiskWriteTime.setStatus("current")
_LDiskPercentFreeSpace_Type = Gauge32
_LDiskPercentFreeSpace_Object = MibTableColumn
lDiskPercentFreeSpace = _LDiskPercentFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 5),
    _LDiskPercentFreeSpace_Type()
)
lDiskPercentFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskPercentFreeSpace.setStatus("current")
_LDiskPercentIdleTime_Type = Gauge32
_LDiskPercentIdleTime_Object = MibTableColumn
lDiskPercentIdleTime = _LDiskPercentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 6),
    _LDiskPercentIdleTime_Type()
)
lDiskPercentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskPercentIdleTime.setStatus("current")
_LDiskAvgDiskQueueLength_Type = Gauge32
_LDiskAvgDiskQueueLength_Object = MibTableColumn
lDiskAvgDiskQueueLength = _LDiskAvgDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 7),
    _LDiskAvgDiskQueueLength_Type()
)
lDiskAvgDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskQueueLength.setStatus("current")
_LDiskAvgDiskReadQueueLength_Type = Gauge32
_LDiskAvgDiskReadQueueLength_Object = MibTableColumn
lDiskAvgDiskReadQueueLength = _LDiskAvgDiskReadQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 8),
    _LDiskAvgDiskReadQueueLength_Type()
)
lDiskAvgDiskReadQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskReadQueueLength.setStatus("current")
_LDiskAvgDiskWriteQueueLength_Type = Gauge32
_LDiskAvgDiskWriteQueueLength_Object = MibTableColumn
lDiskAvgDiskWriteQueueLength = _LDiskAvgDiskWriteQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 9),
    _LDiskAvgDiskWriteQueueLength_Type()
)
lDiskAvgDiskWriteQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskWriteQueueLength.setStatus("current")
_LDiskAvgDiskSecPerRead_Type = Gauge32
_LDiskAvgDiskSecPerRead_Object = MibTableColumn
lDiskAvgDiskSecPerRead = _LDiskAvgDiskSecPerRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 10),
    _LDiskAvgDiskSecPerRead_Type()
)
lDiskAvgDiskSecPerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskSecPerRead.setStatus("current")
_LDiskAvgDiskSecPerTransfer_Type = Gauge32
_LDiskAvgDiskSecPerTransfer_Object = MibTableColumn
lDiskAvgDiskSecPerTransfer = _LDiskAvgDiskSecPerTransfer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 11),
    _LDiskAvgDiskSecPerTransfer_Type()
)
lDiskAvgDiskSecPerTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskSecPerTransfer.setStatus("current")
_LDiskAvgDiskSecPerWrite_Type = Gauge32
_LDiskAvgDiskSecPerWrite_Object = MibTableColumn
lDiskAvgDiskSecPerWrite = _LDiskAvgDiskSecPerWrite_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 12),
    _LDiskAvgDiskSecPerWrite_Type()
)
lDiskAvgDiskSecPerWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskAvgDiskSecPerWrite.setStatus("current")
_LDiskCurrentDiskQueueLength_Type = Gauge32
_LDiskCurrentDiskQueueLength_Object = MibTableColumn
lDiskCurrentDiskQueueLength = _LDiskCurrentDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 13),
    _LDiskCurrentDiskQueueLength_Type()
)
lDiskCurrentDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskCurrentDiskQueueLength.setStatus("current")
_LDiskDiskBytesPerSec_Type = Gauge32
_LDiskDiskBytesPerSec_Object = MibTableColumn
lDiskDiskBytesPerSec = _LDiskDiskBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 14),
    _LDiskDiskBytesPerSec_Type()
)
lDiskDiskBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskBytesPerSec.setStatus("current")
_LDiskDiskReadBytesPerSec_Type = Gauge32
_LDiskDiskReadBytesPerSec_Object = MibTableColumn
lDiskDiskReadBytesPerSec = _LDiskDiskReadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 15),
    _LDiskDiskReadBytesPerSec_Type()
)
lDiskDiskReadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskReadBytesPerSec.setStatus("current")
_LDiskDiskReadsPerSec_Type = Gauge32
_LDiskDiskReadsPerSec_Object = MibTableColumn
lDiskDiskReadsPerSec = _LDiskDiskReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 16),
    _LDiskDiskReadsPerSec_Type()
)
lDiskDiskReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskReadsPerSec.setStatus("current")
_LDiskDiskTransfersPerSec_Type = Gauge32
_LDiskDiskTransfersPerSec_Object = MibTableColumn
lDiskDiskTransfersPerSec = _LDiskDiskTransfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 17),
    _LDiskDiskTransfersPerSec_Type()
)
lDiskDiskTransfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskTransfersPerSec.setStatus("current")
_LDiskDiskWriteBytesPerSec_Type = Gauge32
_LDiskDiskWriteBytesPerSec_Object = MibTableColumn
lDiskDiskWriteBytesPerSec = _LDiskDiskWriteBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 18),
    _LDiskDiskWriteBytesPerSec_Type()
)
lDiskDiskWriteBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskWriteBytesPerSec.setStatus("current")
_LDiskDiskWritesPerSec_Type = Gauge32
_LDiskDiskWritesPerSec_Object = MibTableColumn
lDiskDiskWritesPerSec = _LDiskDiskWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 19),
    _LDiskDiskWritesPerSec_Type()
)
lDiskDiskWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskDiskWritesPerSec.setStatus("current")
_LDiskFreeMegabytes_Type = Gauge32
_LDiskFreeMegabytes_Object = MibTableColumn
lDiskFreeMegabytes = _LDiskFreeMegabytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 20),
    _LDiskFreeMegabytes_Type()
)
lDiskFreeMegabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskFreeMegabytes.setStatus("current")
_LDiskSplitIOPerSec_Type = Gauge32
_LDiskSplitIOPerSec_Object = MibTableColumn
lDiskSplitIOPerSec = _LDiskSplitIOPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 1, 1, 21),
    _LDiskSplitIOPerSec_Type()
)
lDiskSplitIOPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lDiskSplitIOPerSec.setStatus("current")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2)
)
if mibBuilder.loadTexts:
    memory.setStatus("current")
_MemoryAvailableBytes_Type = Gauge32
_MemoryAvailableBytes_Object = MibScalar
memoryAvailableBytes = _MemoryAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 1),
    _MemoryAvailableBytes_Type()
)
memoryAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailableBytes.setStatus("current")
_MemoryAvailableKBytes_Type = Gauge32
_MemoryAvailableKBytes_Object = MibScalar
memoryAvailableKBytes = _MemoryAvailableKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 2),
    _MemoryAvailableKBytes_Type()
)
memoryAvailableKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailableKBytes.setStatus("current")
_MemoryAvailableMBytes_Type = Gauge32
_MemoryAvailableMBytes_Object = MibScalar
memoryAvailableMBytes = _MemoryAvailableMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 3),
    _MemoryAvailableMBytes_Type()
)
memoryAvailableMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailableMBytes.setStatus("current")
_MemoryCommittedBytes_Type = Gauge32
_MemoryCommittedBytes_Object = MibScalar
memoryCommittedBytes = _MemoryCommittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 4),
    _MemoryCommittedBytes_Type()
)
memoryCommittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCommittedBytes.setStatus("current")
_MemoryCacheBytes_Type = Gauge32
_MemoryCacheBytes_Object = MibScalar
memoryCacheBytes = _MemoryCacheBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 5),
    _MemoryCacheBytes_Type()
)
memoryCacheBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheBytes.setStatus("current")
_MemoryCacheBytesPeak_Type = Gauge32
_MemoryCacheBytesPeak_Object = MibScalar
memoryCacheBytesPeak = _MemoryCacheBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 6),
    _MemoryCacheBytesPeak_Type()
)
memoryCacheBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheBytesPeak.setStatus("current")
_MemoryPageFaultsPerSec_Type = Gauge32
_MemoryPageFaultsPerSec_Object = MibScalar
memoryPageFaultsPerSec = _MemoryPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 7),
    _MemoryPageFaultsPerSec_Type()
)
memoryPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPageFaultsPerSec.setStatus("current")
_MemoryPagesInputPerSec_Type = Gauge32
_MemoryPagesInputPerSec_Object = MibScalar
memoryPagesInputPerSec = _MemoryPagesInputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 8),
    _MemoryPagesInputPerSec_Type()
)
memoryPagesInputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesInputPerSec.setStatus("current")
_MemoryPagesOutputPerSec_Type = Gauge32
_MemoryPagesOutputPerSec_Object = MibScalar
memoryPagesOutputPerSec = _MemoryPagesOutputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 9),
    _MemoryPagesOutputPerSec_Type()
)
memoryPagesOutputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesOutputPerSec.setStatus("current")
_MemoryPagesPerSec_Type = Gauge32
_MemoryPagesPerSec_Object = MibScalar
memoryPagesPerSec = _MemoryPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 10),
    _MemoryPagesPerSec_Type()
)
memoryPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPagesPerSec.setStatus("current")
_MemoryPoolNonpagedBytes_Type = Gauge32
_MemoryPoolNonpagedBytes_Object = MibScalar
memoryPoolNonpagedBytes = _MemoryPoolNonpagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 11),
    _MemoryPoolNonpagedBytes_Type()
)
memoryPoolNonpagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNonpagedBytes.setStatus("current")
_MemoryPoolPagedBytes_Type = Gauge32
_MemoryPoolPagedBytes_Object = MibScalar
memoryPoolPagedBytes = _MemoryPoolPagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 12),
    _MemoryPoolPagedBytes_Type()
)
memoryPoolPagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedBytes.setStatus("current")
_MemoryPoolPagedResidentBytes_Type = Gauge32
_MemoryPoolPagedResidentBytes_Object = MibScalar
memoryPoolPagedResidentBytes = _MemoryPoolPagedResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 13),
    _MemoryPoolPagedResidentBytes_Type()
)
memoryPoolPagedResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedResidentBytes.setStatus("current")
_MemorySystemCacheResidentBytes_Type = Gauge32
_MemorySystemCacheResidentBytes_Object = MibScalar
memorySystemCacheResidentBytes = _MemorySystemCacheResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 14),
    _MemorySystemCacheResidentBytes_Type()
)
memorySystemCacheResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCacheResidentBytes.setStatus("current")
_MemorySystemCodeResidentBytes_Type = Gauge32
_MemorySystemCodeResidentBytes_Object = MibScalar
memorySystemCodeResidentBytes = _MemorySystemCodeResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 15),
    _MemorySystemCodeResidentBytes_Type()
)
memorySystemCodeResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeResidentBytes.setStatus("current")
_MemorySystemCodeTotalBytes_Type = Gauge32
_MemorySystemCodeTotalBytes_Object = MibScalar
memorySystemCodeTotalBytes = _MemorySystemCodeTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 16),
    _MemorySystemCodeTotalBytes_Type()
)
memorySystemCodeTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeTotalBytes.setStatus("current")
_MemorySystemDriverResidentBytes_Type = Gauge32
_MemorySystemDriverResidentBytes_Object = MibScalar
memorySystemDriverResidentBytes = _MemorySystemDriverResidentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 17),
    _MemorySystemDriverResidentBytes_Type()
)
memorySystemDriverResidentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverResidentBytes.setStatus("current")
_MemorySystemDriverTotalBytes_Type = Gauge32
_MemorySystemDriverTotalBytes_Object = MibScalar
memorySystemDriverTotalBytes = _MemorySystemDriverTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 18),
    _MemorySystemDriverTotalBytes_Type()
)
memorySystemDriverTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverTotalBytes.setStatus("current")
_MemoryCommittedKBytes_Type = Gauge32
_MemoryCommittedKBytes_Object = MibScalar
memoryCommittedKBytes = _MemoryCommittedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 19),
    _MemoryCommittedKBytes_Type()
)
memoryCommittedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCommittedKBytes.setStatus("current")
_MemoryCacheKBytes_Type = Gauge32
_MemoryCacheKBytes_Object = MibScalar
memoryCacheKBytes = _MemoryCacheKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 20),
    _MemoryCacheKBytes_Type()
)
memoryCacheKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheKBytes.setStatus("current")
_MemoryCacheKBytesPeak_Type = Gauge32
_MemoryCacheKBytesPeak_Object = MibScalar
memoryCacheKBytesPeak = _MemoryCacheKBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 21),
    _MemoryCacheKBytesPeak_Type()
)
memoryCacheKBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheKBytesPeak.setStatus("current")
_MemoryPoolNonpagedKBytes_Type = Gauge32
_MemoryPoolNonpagedKBytes_Object = MibScalar
memoryPoolNonpagedKBytes = _MemoryPoolNonpagedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 22),
    _MemoryPoolNonpagedKBytes_Type()
)
memoryPoolNonpagedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNonpagedKBytes.setStatus("current")
_MemoryPoolPagedKBytes_Type = Gauge32
_MemoryPoolPagedKBytes_Object = MibScalar
memoryPoolPagedKBytes = _MemoryPoolPagedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 23),
    _MemoryPoolPagedKBytes_Type()
)
memoryPoolPagedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedKBytes.setStatus("current")
_MemoryPoolPagedResidentKBytes_Type = Gauge32
_MemoryPoolPagedResidentKBytes_Object = MibScalar
memoryPoolPagedResidentKBytes = _MemoryPoolPagedResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 24),
    _MemoryPoolPagedResidentKBytes_Type()
)
memoryPoolPagedResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedResidentKBytes.setStatus("current")
_MemorySystemCacheResidentKBytes_Type = Gauge32
_MemorySystemCacheResidentKBytes_Object = MibScalar
memorySystemCacheResidentKBytes = _MemorySystemCacheResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 25),
    _MemorySystemCacheResidentKBytes_Type()
)
memorySystemCacheResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCacheResidentKBytes.setStatus("current")
_MemorySystemCodeResidentKBytes_Type = Gauge32
_MemorySystemCodeResidentKBytes_Object = MibScalar
memorySystemCodeResidentKBytes = _MemorySystemCodeResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 26),
    _MemorySystemCodeResidentKBytes_Type()
)
memorySystemCodeResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeResidentKBytes.setStatus("current")
_MemorySystemCodeTotalKBytes_Type = Gauge32
_MemorySystemCodeTotalKBytes_Object = MibScalar
memorySystemCodeTotalKBytes = _MemorySystemCodeTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 27),
    _MemorySystemCodeTotalKBytes_Type()
)
memorySystemCodeTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeTotalKBytes.setStatus("current")
_MemorySystemDriverResidentKBytes_Type = Gauge32
_MemorySystemDriverResidentKBytes_Object = MibScalar
memorySystemDriverResidentKBytes = _MemorySystemDriverResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 28),
    _MemorySystemDriverResidentKBytes_Type()
)
memorySystemDriverResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverResidentKBytes.setStatus("current")
_MemorySystemDriverTotalKBytes_Type = Gauge32
_MemorySystemDriverTotalKBytes_Object = MibScalar
memorySystemDriverTotalKBytes = _MemorySystemDriverTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 29),
    _MemorySystemDriverTotalKBytes_Type()
)
memorySystemDriverTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverTotalKBytes.setStatus("current")
_MemoryCommittedMBytes_Type = Gauge32
_MemoryCommittedMBytes_Object = MibScalar
memoryCommittedMBytes = _MemoryCommittedMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 30),
    _MemoryCommittedMBytes_Type()
)
memoryCommittedMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCommittedMBytes.setStatus("current")
_MemoryCacheMBytes_Type = Gauge32
_MemoryCacheMBytes_Object = MibScalar
memoryCacheMBytes = _MemoryCacheMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 31),
    _MemoryCacheMBytes_Type()
)
memoryCacheMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheMBytes.setStatus("current")
_MemoryCacheMBytesPeak_Type = Gauge32
_MemoryCacheMBytesPeak_Object = MibScalar
memoryCacheMBytesPeak = _MemoryCacheMBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 32),
    _MemoryCacheMBytesPeak_Type()
)
memoryCacheMBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheMBytesPeak.setStatus("current")
_MemoryPoolNonpagedMBytes_Type = Gauge32
_MemoryPoolNonpagedMBytes_Object = MibScalar
memoryPoolNonpagedMBytes = _MemoryPoolNonpagedMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 33),
    _MemoryPoolNonpagedMBytes_Type()
)
memoryPoolNonpagedMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNonpagedMBytes.setStatus("current")
_MemoryPoolPagedMBytes_Type = Gauge32
_MemoryPoolPagedMBytes_Object = MibScalar
memoryPoolPagedMBytes = _MemoryPoolPagedMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 34),
    _MemoryPoolPagedMBytes_Type()
)
memoryPoolPagedMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedMBytes.setStatus("current")
_MemoryPoolPagedResidentMBytes_Type = Gauge32
_MemoryPoolPagedResidentMBytes_Object = MibScalar
memoryPoolPagedResidentMBytes = _MemoryPoolPagedResidentMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 35),
    _MemoryPoolPagedResidentMBytes_Type()
)
memoryPoolPagedResidentMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolPagedResidentMBytes.setStatus("current")
_MemorySystemCacheResidentMBytes_Type = Gauge32
_MemorySystemCacheResidentMBytes_Object = MibScalar
memorySystemCacheResidentMBytes = _MemorySystemCacheResidentMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 36),
    _MemorySystemCacheResidentMBytes_Type()
)
memorySystemCacheResidentMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCacheResidentMBytes.setStatus("current")
_MemorySystemCodeResidentMBytes_Type = Gauge32
_MemorySystemCodeResidentMBytes_Object = MibScalar
memorySystemCodeResidentMBytes = _MemorySystemCodeResidentMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 37),
    _MemorySystemCodeResidentMBytes_Type()
)
memorySystemCodeResidentMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeResidentMBytes.setStatus("current")
_MemorySystemCodeTotalMBytes_Type = Gauge32
_MemorySystemCodeTotalMBytes_Object = MibScalar
memorySystemCodeTotalMBytes = _MemorySystemCodeTotalMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 38),
    _MemorySystemCodeTotalMBytes_Type()
)
memorySystemCodeTotalMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemCodeTotalMBytes.setStatus("current")
_MemorySystemDriverResidentMBytes_Type = Gauge32
_MemorySystemDriverResidentMBytes_Object = MibScalar
memorySystemDriverResidentMBytes = _MemorySystemDriverResidentMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 39),
    _MemorySystemDriverResidentMBytes_Type()
)
memorySystemDriverResidentMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverResidentMBytes.setStatus("current")
_MemorySystemDriverTotalMBytes_Type = Gauge32
_MemorySystemDriverTotalMBytes_Object = MibScalar
memorySystemDriverTotalMBytes = _MemorySystemDriverTotalMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 2, 40),
    _MemorySystemDriverTotalMBytes_Type()
)
memorySystemDriverTotalMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySystemDriverTotalMBytes.setStatus("current")
_NetworkInterfaceTable_Object = MibTable
networkInterfaceTable = _NetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3)
)
if mibBuilder.loadTexts:
    networkInterfaceTable.setStatus("current")
_NetworkInterfaceEntry_Object = MibTableRow
networkInterfaceEntry = _NetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1)
)
networkInterfaceEntry.setIndexNames(
    (0, "INFORMANT-STD", "netInstance"),
)
if mibBuilder.loadTexts:
    networkInterfaceEntry.setStatus("current")
_NetInstance_Type = InstanceName
_NetInstance_Object = MibTableColumn
netInstance = _NetInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 1),
    _NetInstance_Type()
)
netInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netInstance.setStatus("current")
_NetBytesReceivedPerSec_Type = Gauge32
_NetBytesReceivedPerSec_Object = MibTableColumn
netBytesReceivedPerSec = _NetBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 2),
    _NetBytesReceivedPerSec_Type()
)
netBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesReceivedPerSec.setStatus("current")
_NetBytesSentPerSec_Type = Gauge32
_NetBytesSentPerSec_Object = MibTableColumn
netBytesSentPerSec = _NetBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 3),
    _NetBytesSentPerSec_Type()
)
netBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesSentPerSec.setStatus("current")
_NetBytesTotalPerSec_Type = Gauge32
_NetBytesTotalPerSec_Object = MibTableColumn
netBytesTotalPerSec = _NetBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 4),
    _NetBytesTotalPerSec_Type()
)
netBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBytesTotalPerSec.setStatus("current")
_NetCurrentBandwidth_Type = Gauge32
_NetCurrentBandwidth_Object = MibTableColumn
netCurrentBandwidth = _NetCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 5),
    _NetCurrentBandwidth_Type()
)
netCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCurrentBandwidth.setStatus("current")
_NetOutputQueueLength_Type = Gauge32
_NetOutputQueueLength_Object = MibTableColumn
netOutputQueueLength = _NetOutputQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 6),
    _NetOutputQueueLength_Type()
)
netOutputQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netOutputQueueLength.setStatus("current")
_NetPacketsOutboundDiscarded_Type = Gauge32
_NetPacketsOutboundDiscarded_Object = MibTableColumn
netPacketsOutboundDiscarded = _NetPacketsOutboundDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 7),
    _NetPacketsOutboundDiscarded_Type()
)
netPacketsOutboundDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsOutboundDiscarded.setStatus("current")
_NetPacketsOutboundErrors_Type = Gauge32
_NetPacketsOutboundErrors_Object = MibTableColumn
netPacketsOutboundErrors = _NetPacketsOutboundErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 8),
    _NetPacketsOutboundErrors_Type()
)
netPacketsOutboundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsOutboundErrors.setStatus("current")
_NetPacketsReceivedDiscarded_Type = Gauge32
_NetPacketsReceivedDiscarded_Object = MibTableColumn
netPacketsReceivedDiscarded = _NetPacketsReceivedDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 9),
    _NetPacketsReceivedDiscarded_Type()
)
netPacketsReceivedDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedDiscarded.setStatus("current")
_NetPacketsReceivedErrors_Type = Gauge32
_NetPacketsReceivedErrors_Object = MibTableColumn
netPacketsReceivedErrors = _NetPacketsReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 10),
    _NetPacketsReceivedErrors_Type()
)
netPacketsReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedErrors.setStatus("current")
_NetPacketsReceivedUnknown_Type = Gauge32
_NetPacketsReceivedUnknown_Object = MibTableColumn
netPacketsReceivedUnknown = _NetPacketsReceivedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 11),
    _NetPacketsReceivedUnknown_Type()
)
netPacketsReceivedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedUnknown.setStatus("current")
_NetPacketsReceivedPerSec_Type = Gauge32
_NetPacketsReceivedPerSec_Object = MibTableColumn
netPacketsReceivedPerSec = _NetPacketsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 12),
    _NetPacketsReceivedPerSec_Type()
)
netPacketsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsReceivedPerSec.setStatus("current")
_NetPacketsSentPerSec_Type = Gauge32
_NetPacketsSentPerSec_Object = MibTableColumn
netPacketsSentPerSec = _NetPacketsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 13),
    _NetPacketsSentPerSec_Type()
)
netPacketsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsSentPerSec.setStatus("current")
_NetPacketsPerSec_Type = Gauge32
_NetPacketsPerSec_Object = MibTableColumn
netPacketsPerSec = _NetPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 3, 1, 14),
    _NetPacketsPerSec_Type()
)
netPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketsPerSec.setStatus("current")
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 4)
)
if mibBuilder.loadTexts:
    objects.setStatus("current")
_ObjectsProcesses_Type = Gauge32
_ObjectsProcesses_Object = MibScalar
objectsProcesses = _ObjectsProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 4, 1),
    _ObjectsProcesses_Type()
)
objectsProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectsProcesses.setStatus("current")
_ObjectsThreads_Type = Gauge32
_ObjectsThreads_Object = MibScalar
objectsThreads = _ObjectsThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 4, 2),
    _ObjectsThreads_Type()
)
objectsThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectsThreads.setStatus("current")
_ProcessorTable_Object = MibTable
processorTable = _ProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5)
)
if mibBuilder.loadTexts:
    processorTable.setStatus("current")
_ProcessorEntry_Object = MibTableRow
processorEntry = _ProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1)
)
processorEntry.setIndexNames(
    (0, "INFORMANT-STD", "cpuInstance"),
)
if mibBuilder.loadTexts:
    processorEntry.setStatus("current")
_CpuInstance_Type = InstanceName
_CpuInstance_Object = MibTableColumn
cpuInstance = _CpuInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 1),
    _CpuInstance_Type()
)
cpuInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInstance.setStatus("current")
_CpuPercentDPCTime_Type = Gauge32
_CpuPercentDPCTime_Object = MibTableColumn
cpuPercentDPCTime = _CpuPercentDPCTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 2),
    _CpuPercentDPCTime_Type()
)
cpuPercentDPCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentDPCTime.setStatus("current")
_CpuPercentInterruptTime_Type = Gauge32
_CpuPercentInterruptTime_Object = MibTableColumn
cpuPercentInterruptTime = _CpuPercentInterruptTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 3),
    _CpuPercentInterruptTime_Type()
)
cpuPercentInterruptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentInterruptTime.setStatus("current")
_CpuPercentPrivilegedTime_Type = Gauge32
_CpuPercentPrivilegedTime_Object = MibTableColumn
cpuPercentPrivilegedTime = _CpuPercentPrivilegedTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 4),
    _CpuPercentPrivilegedTime_Type()
)
cpuPercentPrivilegedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentPrivilegedTime.setStatus("current")
_CpuPercentProcessorTime_Type = Gauge32
_CpuPercentProcessorTime_Object = MibTableColumn
cpuPercentProcessorTime = _CpuPercentProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 5),
    _CpuPercentProcessorTime_Type()
)
cpuPercentProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentProcessorTime.setStatus("current")
_CpuPercentUserTime_Type = Gauge32
_CpuPercentUserTime_Object = MibTableColumn
cpuPercentUserTime = _CpuPercentUserTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 6),
    _CpuPercentUserTime_Type()
)
cpuPercentUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercentUserTime.setStatus("current")
_CpuAPCBypassesPerSec_Type = Gauge32
_CpuAPCBypassesPerSec_Object = MibTableColumn
cpuAPCBypassesPerSec = _CpuAPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 7),
    _CpuAPCBypassesPerSec_Type()
)
cpuAPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAPCBypassesPerSec.setStatus("current")
_CpuDPCBypassesPerSec_Type = Gauge32
_CpuDPCBypassesPerSec_Object = MibTableColumn
cpuDPCBypassesPerSec = _CpuDPCBypassesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 8),
    _CpuDPCBypassesPerSec_Type()
)
cpuDPCBypassesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCBypassesPerSec.setStatus("current")
_CpuDPCRate_Type = Gauge32
_CpuDPCRate_Object = MibTableColumn
cpuDPCRate = _CpuDPCRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 9),
    _CpuDPCRate_Type()
)
cpuDPCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCRate.setStatus("current")
_CpuDPCsQueuedPerSec_Type = Gauge32
_CpuDPCsQueuedPerSec_Object = MibTableColumn
cpuDPCsQueuedPerSec = _CpuDPCsQueuedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 10),
    _CpuDPCsQueuedPerSec_Type()
)
cpuDPCsQueuedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDPCsQueuedPerSec.setStatus("current")
_CpuInterruptsPerSec_Type = Gauge32
_CpuInterruptsPerSec_Object = MibTableColumn
cpuInterruptsPerSec = _CpuInterruptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 5, 1, 11),
    _CpuInterruptsPerSec_Type()
)
cpuInterruptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInterruptsPerSec.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 6)
)
if mibBuilder.loadTexts:
    system.setStatus("current")
_SystemSystemUpTime_Type = Gauge32
_SystemSystemUpTime_Object = MibScalar
systemSystemUpTime = _SystemSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 1, 6, 1),
    _SystemSystemUpTime_Type()
)
systemSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSystemUpTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-STD",
    **{"standard": standard,
       "logicalDiskTable": logicalDiskTable,
       "logicalDiskEntry": logicalDiskEntry,
       "lDiskInstance": lDiskInstance,
       "lDiskPercentDiskReadTime": lDiskPercentDiskReadTime,
       "lDiskPercentDiskTime": lDiskPercentDiskTime,
       "lDiskPercentDiskWriteTime": lDiskPercentDiskWriteTime,
       "lDiskPercentFreeSpace": lDiskPercentFreeSpace,
       "lDiskPercentIdleTime": lDiskPercentIdleTime,
       "lDiskAvgDiskQueueLength": lDiskAvgDiskQueueLength,
       "lDiskAvgDiskReadQueueLength": lDiskAvgDiskReadQueueLength,
       "lDiskAvgDiskWriteQueueLength": lDiskAvgDiskWriteQueueLength,
       "lDiskAvgDiskSecPerRead": lDiskAvgDiskSecPerRead,
       "lDiskAvgDiskSecPerTransfer": lDiskAvgDiskSecPerTransfer,
       "lDiskAvgDiskSecPerWrite": lDiskAvgDiskSecPerWrite,
       "lDiskCurrentDiskQueueLength": lDiskCurrentDiskQueueLength,
       "lDiskDiskBytesPerSec": lDiskDiskBytesPerSec,
       "lDiskDiskReadBytesPerSec": lDiskDiskReadBytesPerSec,
       "lDiskDiskReadsPerSec": lDiskDiskReadsPerSec,
       "lDiskDiskTransfersPerSec": lDiskDiskTransfersPerSec,
       "lDiskDiskWriteBytesPerSec": lDiskDiskWriteBytesPerSec,
       "lDiskDiskWritesPerSec": lDiskDiskWritesPerSec,
       "lDiskFreeMegabytes": lDiskFreeMegabytes,
       "lDiskSplitIOPerSec": lDiskSplitIOPerSec,
       "memory": memory,
       "memoryAvailableBytes": memoryAvailableBytes,
       "memoryAvailableKBytes": memoryAvailableKBytes,
       "memoryAvailableMBytes": memoryAvailableMBytes,
       "memoryCommittedBytes": memoryCommittedBytes,
       "memoryCacheBytes": memoryCacheBytes,
       "memoryCacheBytesPeak": memoryCacheBytesPeak,
       "memoryPageFaultsPerSec": memoryPageFaultsPerSec,
       "memoryPagesInputPerSec": memoryPagesInputPerSec,
       "memoryPagesOutputPerSec": memoryPagesOutputPerSec,
       "memoryPagesPerSec": memoryPagesPerSec,
       "memoryPoolNonpagedBytes": memoryPoolNonpagedBytes,
       "memoryPoolPagedBytes": memoryPoolPagedBytes,
       "memoryPoolPagedResidentBytes": memoryPoolPagedResidentBytes,
       "memorySystemCacheResidentBytes": memorySystemCacheResidentBytes,
       "memorySystemCodeResidentBytes": memorySystemCodeResidentBytes,
       "memorySystemCodeTotalBytes": memorySystemCodeTotalBytes,
       "memorySystemDriverResidentBytes": memorySystemDriverResidentBytes,
       "memorySystemDriverTotalBytes": memorySystemDriverTotalBytes,
       "memoryCommittedKBytes": memoryCommittedKBytes,
       "memoryCacheKBytes": memoryCacheKBytes,
       "memoryCacheKBytesPeak": memoryCacheKBytesPeak,
       "memoryPoolNonpagedKBytes": memoryPoolNonpagedKBytes,
       "memoryPoolPagedKBytes": memoryPoolPagedKBytes,
       "memoryPoolPagedResidentKBytes": memoryPoolPagedResidentKBytes,
       "memorySystemCacheResidentKBytes": memorySystemCacheResidentKBytes,
       "memorySystemCodeResidentKBytes": memorySystemCodeResidentKBytes,
       "memorySystemCodeTotalKBytes": memorySystemCodeTotalKBytes,
       "memorySystemDriverResidentKBytes": memorySystemDriverResidentKBytes,
       "memorySystemDriverTotalKBytes": memorySystemDriverTotalKBytes,
       "memoryCommittedMBytes": memoryCommittedMBytes,
       "memoryCacheMBytes": memoryCacheMBytes,
       "memoryCacheMBytesPeak": memoryCacheMBytesPeak,
       "memoryPoolNonpagedMBytes": memoryPoolNonpagedMBytes,
       "memoryPoolPagedMBytes": memoryPoolPagedMBytes,
       "memoryPoolPagedResidentMBytes": memoryPoolPagedResidentMBytes,
       "memorySystemCacheResidentMBytes": memorySystemCacheResidentMBytes,
       "memorySystemCodeResidentMBytes": memorySystemCodeResidentMBytes,
       "memorySystemCodeTotalMBytes": memorySystemCodeTotalMBytes,
       "memorySystemDriverResidentMBytes": memorySystemDriverResidentMBytes,
       "memorySystemDriverTotalMBytes": memorySystemDriverTotalMBytes,
       "networkInterfaceTable": networkInterfaceTable,
       "networkInterfaceEntry": networkInterfaceEntry,
       "netInstance": netInstance,
       "netBytesReceivedPerSec": netBytesReceivedPerSec,
       "netBytesSentPerSec": netBytesSentPerSec,
       "netBytesTotalPerSec": netBytesTotalPerSec,
       "netCurrentBandwidth": netCurrentBandwidth,
       "netOutputQueueLength": netOutputQueueLength,
       "netPacketsOutboundDiscarded": netPacketsOutboundDiscarded,
       "netPacketsOutboundErrors": netPacketsOutboundErrors,
       "netPacketsReceivedDiscarded": netPacketsReceivedDiscarded,
       "netPacketsReceivedErrors": netPacketsReceivedErrors,
       "netPacketsReceivedUnknown": netPacketsReceivedUnknown,
       "netPacketsReceivedPerSec": netPacketsReceivedPerSec,
       "netPacketsSentPerSec": netPacketsSentPerSec,
       "netPacketsPerSec": netPacketsPerSec,
       "objects": objects,
       "objectsProcesses": objectsProcesses,
       "objectsThreads": objectsThreads,
       "processorTable": processorTable,
       "processorEntry": processorEntry,
       "cpuInstance": cpuInstance,
       "cpuPercentDPCTime": cpuPercentDPCTime,
       "cpuPercentInterruptTime": cpuPercentInterruptTime,
       "cpuPercentPrivilegedTime": cpuPercentPrivilegedTime,
       "cpuPercentProcessorTime": cpuPercentProcessorTime,
       "cpuPercentUserTime": cpuPercentUserTime,
       "cpuAPCBypassesPerSec": cpuAPCBypassesPerSec,
       "cpuDPCBypassesPerSec": cpuDPCBypassesPerSec,
       "cpuDPCRate": cpuDPCRate,
       "cpuDPCsQueuedPerSec": cpuDPCsQueuedPerSec,
       "cpuInterruptsPerSec": cpuInterruptsPerSec,
       "system": system,
       "systemSystemUpTime": systemSystemUpTime}
)
