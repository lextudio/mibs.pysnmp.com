# SNMP MIB module (ORADB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORADB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:37 2024
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

(rdbmsDbIndex,) = mibBuilder.importSymbols(
    "RDBMS-MIB",
    "rdbmsDbIndex")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraDbMIB_ObjectIdentity = ObjectIdentity
oraDbMIB = _OraDbMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 4)
)
_OraDbObjects_ObjectIdentity = ObjectIdentity
oraDbObjects = _OraDbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 4, 1)
)
_OraDbSysTable_Object = MibTable
oraDbSysTable = _OraDbSysTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1)
)
if mibBuilder.loadTexts:
    oraDbSysTable.setStatus("mandatory")
_OraDbSysEntry_Object = MibTableRow
oraDbSysEntry = _OraDbSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1)
)
oraDbSysEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    oraDbSysEntry.setStatus("mandatory")
_OraDbSysConsistentChanges_Type = Counter32
_OraDbSysConsistentChanges_Object = MibTableColumn
oraDbSysConsistentChanges = _OraDbSysConsistentChanges_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 1),
    _OraDbSysConsistentChanges_Type()
)
oraDbSysConsistentChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysConsistentChanges.setStatus("mandatory")
_OraDbSysConsistentGets_Type = Counter32
_OraDbSysConsistentGets_Object = MibTableColumn
oraDbSysConsistentGets = _OraDbSysConsistentGets_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 2),
    _OraDbSysConsistentGets_Type()
)
oraDbSysConsistentGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysConsistentGets.setStatus("mandatory")
_OraDbSysDbBlockChanges_Type = Counter32
_OraDbSysDbBlockChanges_Object = MibTableColumn
oraDbSysDbBlockChanges = _OraDbSysDbBlockChanges_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 3),
    _OraDbSysDbBlockChanges_Type()
)
oraDbSysDbBlockChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysDbBlockChanges.setStatus("mandatory")
_OraDbSysDbBlockGets_Type = Counter32
_OraDbSysDbBlockGets_Object = MibTableColumn
oraDbSysDbBlockGets = _OraDbSysDbBlockGets_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 4),
    _OraDbSysDbBlockGets_Type()
)
oraDbSysDbBlockGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysDbBlockGets.setStatus("mandatory")
_OraDbSysFreeBufferInspected_Type = Counter32
_OraDbSysFreeBufferInspected_Object = MibTableColumn
oraDbSysFreeBufferInspected = _OraDbSysFreeBufferInspected_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 5),
    _OraDbSysFreeBufferInspected_Type()
)
oraDbSysFreeBufferInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysFreeBufferInspected.setStatus("mandatory")
_OraDbSysFreeBufferRequested_Type = Counter32
_OraDbSysFreeBufferRequested_Object = MibTableColumn
oraDbSysFreeBufferRequested = _OraDbSysFreeBufferRequested_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 6),
    _OraDbSysFreeBufferRequested_Type()
)
oraDbSysFreeBufferRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysFreeBufferRequested.setStatus("mandatory")
_OraDbSysParseCount_Type = Counter32
_OraDbSysParseCount_Object = MibTableColumn
oraDbSysParseCount = _OraDbSysParseCount_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 7),
    _OraDbSysParseCount_Type()
)
oraDbSysParseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysParseCount.setStatus("mandatory")
_OraDbSysPhysReads_Type = Counter32
_OraDbSysPhysReads_Object = MibTableColumn
oraDbSysPhysReads = _OraDbSysPhysReads_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 8),
    _OraDbSysPhysReads_Type()
)
oraDbSysPhysReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysPhysReads.setStatus("mandatory")
_OraDbSysPhysWrites_Type = Counter32
_OraDbSysPhysWrites_Object = MibTableColumn
oraDbSysPhysWrites = _OraDbSysPhysWrites_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 9),
    _OraDbSysPhysWrites_Type()
)
oraDbSysPhysWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysPhysWrites.setStatus("mandatory")
_OraDbSysRedoEntries_Type = Counter32
_OraDbSysRedoEntries_Object = MibTableColumn
oraDbSysRedoEntries = _OraDbSysRedoEntries_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 10),
    _OraDbSysRedoEntries_Type()
)
oraDbSysRedoEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysRedoEntries.setStatus("mandatory")
_OraDbSysRedoLogSpaceRequests_Type = Counter32
_OraDbSysRedoLogSpaceRequests_Object = MibTableColumn
oraDbSysRedoLogSpaceRequests = _OraDbSysRedoLogSpaceRequests_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 11),
    _OraDbSysRedoLogSpaceRequests_Type()
)
oraDbSysRedoLogSpaceRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysRedoLogSpaceRequests.setStatus("mandatory")
_OraDbSysRedoSyncWrites_Type = Counter32
_OraDbSysRedoSyncWrites_Object = MibTableColumn
oraDbSysRedoSyncWrites = _OraDbSysRedoSyncWrites_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 12),
    _OraDbSysRedoSyncWrites_Type()
)
oraDbSysRedoSyncWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysRedoSyncWrites.setStatus("mandatory")
_OraDbSysSortsDisk_Type = Counter32
_OraDbSysSortsDisk_Object = MibTableColumn
oraDbSysSortsDisk = _OraDbSysSortsDisk_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 13),
    _OraDbSysSortsDisk_Type()
)
oraDbSysSortsDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysSortsDisk.setStatus("mandatory")
_OraDbSysSortsMemory_Type = Counter32
_OraDbSysSortsMemory_Object = MibTableColumn
oraDbSysSortsMemory = _OraDbSysSortsMemory_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 14),
    _OraDbSysSortsMemory_Type()
)
oraDbSysSortsMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysSortsMemory.setStatus("mandatory")
_OraDbSysSortsRows_Type = Counter32
_OraDbSysSortsRows_Object = MibTableColumn
oraDbSysSortsRows = _OraDbSysSortsRows_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 15),
    _OraDbSysSortsRows_Type()
)
oraDbSysSortsRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysSortsRows.setStatus("mandatory")
_OraDbSysTableFetchRowid_Type = Counter32
_OraDbSysTableFetchRowid_Object = MibTableColumn
oraDbSysTableFetchRowid = _OraDbSysTableFetchRowid_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 16),
    _OraDbSysTableFetchRowid_Type()
)
oraDbSysTableFetchRowid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableFetchRowid.setStatus("mandatory")
_OraDbSysTableFetchContinuedRow_Type = Counter32
_OraDbSysTableFetchContinuedRow_Object = MibTableColumn
oraDbSysTableFetchContinuedRow = _OraDbSysTableFetchContinuedRow_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 17),
    _OraDbSysTableFetchContinuedRow_Type()
)
oraDbSysTableFetchContinuedRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableFetchContinuedRow.setStatus("mandatory")
_OraDbSysTableScanBlocks_Type = Counter32
_OraDbSysTableScanBlocks_Object = MibTableColumn
oraDbSysTableScanBlocks = _OraDbSysTableScanBlocks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 18),
    _OraDbSysTableScanBlocks_Type()
)
oraDbSysTableScanBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableScanBlocks.setStatus("mandatory")
_OraDbSysTableScanRows_Type = Counter32
_OraDbSysTableScanRows_Object = MibTableColumn
oraDbSysTableScanRows = _OraDbSysTableScanRows_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 19),
    _OraDbSysTableScanRows_Type()
)
oraDbSysTableScanRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableScanRows.setStatus("mandatory")
_OraDbSysTableScansLong_Type = Counter32
_OraDbSysTableScansLong_Object = MibTableColumn
oraDbSysTableScansLong = _OraDbSysTableScansLong_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 20),
    _OraDbSysTableScansLong_Type()
)
oraDbSysTableScansLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableScansLong.setStatus("mandatory")
_OraDbSysTableScansShort_Type = Counter32
_OraDbSysTableScansShort_Object = MibTableColumn
oraDbSysTableScansShort = _OraDbSysTableScansShort_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 21),
    _OraDbSysTableScansShort_Type()
)
oraDbSysTableScansShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysTableScansShort.setStatus("mandatory")
_OraDbSysUserCalls_Type = Counter32
_OraDbSysUserCalls_Object = MibTableColumn
oraDbSysUserCalls = _OraDbSysUserCalls_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 22),
    _OraDbSysUserCalls_Type()
)
oraDbSysUserCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysUserCalls.setStatus("mandatory")
_OraDbSysUserCommits_Type = Counter32
_OraDbSysUserCommits_Object = MibTableColumn
oraDbSysUserCommits = _OraDbSysUserCommits_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 23),
    _OraDbSysUserCommits_Type()
)
oraDbSysUserCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysUserCommits.setStatus("mandatory")
_OraDbSysUserRollbacks_Type = Counter32
_OraDbSysUserRollbacks_Object = MibTableColumn
oraDbSysUserRollbacks = _OraDbSysUserRollbacks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 24),
    _OraDbSysUserRollbacks_Type()
)
oraDbSysUserRollbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysUserRollbacks.setStatus("mandatory")
_OraDbSysWriteRequests_Type = Counter32
_OraDbSysWriteRequests_Object = MibTableColumn
oraDbSysWriteRequests = _OraDbSysWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 1, 1, 25),
    _OraDbSysWriteRequests_Type()
)
oraDbSysWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSysWriteRequests.setStatus("mandatory")
_OraDbTablespaceTable_Object = MibTable
oraDbTablespaceTable = _OraDbTablespaceTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2)
)
if mibBuilder.loadTexts:
    oraDbTablespaceTable.setStatus("mandatory")
_OraDbTablespaceEntry_Object = MibTableRow
oraDbTablespaceEntry = _OraDbTablespaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1)
)
oraDbTablespaceEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "ORADB-MIB", "oraDbTablespaceIndex"),
)
if mibBuilder.loadTexts:
    oraDbTablespaceEntry.setStatus("mandatory")
_OraDbTablespaceIndex_Type = Integer32
_OraDbTablespaceIndex_Object = MibTableColumn
oraDbTablespaceIndex = _OraDbTablespaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 1),
    _OraDbTablespaceIndex_Type()
)
oraDbTablespaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceIndex.setStatus("mandatory")
_OraDbTablespaceName_Type = DisplayString
_OraDbTablespaceName_Object = MibTableColumn
oraDbTablespaceName = _OraDbTablespaceName_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 2),
    _OraDbTablespaceName_Type()
)
oraDbTablespaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceName.setStatus("mandatory")


class _OraDbTablespaceSizeAllocated_Type(Integer32):
    """Custom type oraDbTablespaceSizeAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraDbTablespaceSizeAllocated_Type.__name__ = "Integer32"
_OraDbTablespaceSizeAllocated_Object = MibTableColumn
oraDbTablespaceSizeAllocated = _OraDbTablespaceSizeAllocated_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 3),
    _OraDbTablespaceSizeAllocated_Type()
)
oraDbTablespaceSizeAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceSizeAllocated.setStatus("mandatory")


class _OraDbTablespaceSizeUsed_Type(Integer32):
    """Custom type oraDbTablespaceSizeUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraDbTablespaceSizeUsed_Type.__name__ = "Integer32"
_OraDbTablespaceSizeUsed_Object = MibTableColumn
oraDbTablespaceSizeUsed = _OraDbTablespaceSizeUsed_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 4),
    _OraDbTablespaceSizeUsed_Type()
)
oraDbTablespaceSizeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceSizeUsed.setStatus("mandatory")


class _OraDbTablespaceState_Type(Integer32):
    """Custom type oraDbTablespaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("offline", 2),
          ("online", 1))
    )


_OraDbTablespaceState_Type.__name__ = "Integer32"
_OraDbTablespaceState_Object = MibTableColumn
oraDbTablespaceState = _OraDbTablespaceState_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 5),
    _OraDbTablespaceState_Type()
)
oraDbTablespaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceState.setStatus("mandatory")


class _OraDbTablespaceLargestAvailableChunk_Type(Integer32):
    """Custom type oraDbTablespaceLargestAvailableChunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraDbTablespaceLargestAvailableChunk_Type.__name__ = "Integer32"
_OraDbTablespaceLargestAvailableChunk_Object = MibTableColumn
oraDbTablespaceLargestAvailableChunk = _OraDbTablespaceLargestAvailableChunk_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 2, 1, 6),
    _OraDbTablespaceLargestAvailableChunk_Type()
)
oraDbTablespaceLargestAvailableChunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbTablespaceLargestAvailableChunk.setStatus("mandatory")
_OraDbDataFileTable_Object = MibTable
oraDbDataFileTable = _OraDbDataFileTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3)
)
if mibBuilder.loadTexts:
    oraDbDataFileTable.setStatus("mandatory")
_OraDbDataFileEntry_Object = MibTableRow
oraDbDataFileEntry = _OraDbDataFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1)
)
oraDbDataFileEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "ORADB-MIB", "oraDbDataFileIndex"),
)
if mibBuilder.loadTexts:
    oraDbDataFileEntry.setStatus("mandatory")
_OraDbDataFileIndex_Type = Integer32
_OraDbDataFileIndex_Object = MibTableColumn
oraDbDataFileIndex = _OraDbDataFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 1),
    _OraDbDataFileIndex_Type()
)
oraDbDataFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileIndex.setStatus("mandatory")
_OraDbDataFileName_Type = DisplayString
_OraDbDataFileName_Object = MibTableColumn
oraDbDataFileName = _OraDbDataFileName_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 2),
    _OraDbDataFileName_Type()
)
oraDbDataFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileName.setStatus("mandatory")


class _OraDbDataFileSizeAllocated_Type(Integer32):
    """Custom type oraDbDataFileSizeAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OraDbDataFileSizeAllocated_Type.__name__ = "Integer32"
_OraDbDataFileSizeAllocated_Object = MibTableColumn
oraDbDataFileSizeAllocated = _OraDbDataFileSizeAllocated_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 3),
    _OraDbDataFileSizeAllocated_Type()
)
oraDbDataFileSizeAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileSizeAllocated.setStatus("mandatory")
_OraDbDataFileDiskReads_Type = Counter32
_OraDbDataFileDiskReads_Object = MibTableColumn
oraDbDataFileDiskReads = _OraDbDataFileDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 4),
    _OraDbDataFileDiskReads_Type()
)
oraDbDataFileDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskReads.setStatus("mandatory")
_OraDbDataFileDiskWrites_Type = Counter32
_OraDbDataFileDiskWrites_Object = MibTableColumn
oraDbDataFileDiskWrites = _OraDbDataFileDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 5),
    _OraDbDataFileDiskWrites_Type()
)
oraDbDataFileDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskWrites.setStatus("mandatory")
_OraDbDataFileDiskReadBlocks_Type = Counter32
_OraDbDataFileDiskReadBlocks_Object = MibTableColumn
oraDbDataFileDiskReadBlocks = _OraDbDataFileDiskReadBlocks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 6),
    _OraDbDataFileDiskReadBlocks_Type()
)
oraDbDataFileDiskReadBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskReadBlocks.setStatus("mandatory")
_OraDbDataFileDiskWrittenBlocks_Type = Counter32
_OraDbDataFileDiskWrittenBlocks_Object = MibTableColumn
oraDbDataFileDiskWrittenBlocks = _OraDbDataFileDiskWrittenBlocks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 7),
    _OraDbDataFileDiskWrittenBlocks_Type()
)
oraDbDataFileDiskWrittenBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskWrittenBlocks.setStatus("mandatory")
_OraDbDataFileDiskReadTimeTicks_Type = Counter32
_OraDbDataFileDiskReadTimeTicks_Object = MibTableColumn
oraDbDataFileDiskReadTimeTicks = _OraDbDataFileDiskReadTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 8),
    _OraDbDataFileDiskReadTimeTicks_Type()
)
oraDbDataFileDiskReadTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskReadTimeTicks.setStatus("mandatory")
_OraDbDataFileDiskWriteTimeTicks_Type = Counter32
_OraDbDataFileDiskWriteTimeTicks_Object = MibTableColumn
oraDbDataFileDiskWriteTimeTicks = _OraDbDataFileDiskWriteTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 3, 1, 9),
    _OraDbDataFileDiskWriteTimeTicks_Type()
)
oraDbDataFileDiskWriteTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbDataFileDiskWriteTimeTicks.setStatus("mandatory")
_OraDbLibraryCacheTable_Object = MibTable
oraDbLibraryCacheTable = _OraDbLibraryCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4)
)
if mibBuilder.loadTexts:
    oraDbLibraryCacheTable.setStatus("mandatory")
_OraDbLibraryCacheEntry_Object = MibTableRow
oraDbLibraryCacheEntry = _OraDbLibraryCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1)
)
oraDbLibraryCacheEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "ORADB-MIB", "oraDbLibraryCacheIndex"),
)
if mibBuilder.loadTexts:
    oraDbLibraryCacheEntry.setStatus("mandatory")
_OraDbLibraryCacheIndex_Type = Integer32
_OraDbLibraryCacheIndex_Object = MibTableColumn
oraDbLibraryCacheIndex = _OraDbLibraryCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 1),
    _OraDbLibraryCacheIndex_Type()
)
oraDbLibraryCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheIndex.setStatus("mandatory")
_OraDbLibraryCacheNameSpace_Type = DisplayString
_OraDbLibraryCacheNameSpace_Object = MibTableColumn
oraDbLibraryCacheNameSpace = _OraDbLibraryCacheNameSpace_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 2),
    _OraDbLibraryCacheNameSpace_Type()
)
oraDbLibraryCacheNameSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheNameSpace.setStatus("mandatory")
_OraDbLibraryCacheGets_Type = Counter32
_OraDbLibraryCacheGets_Object = MibTableColumn
oraDbLibraryCacheGets = _OraDbLibraryCacheGets_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 3),
    _OraDbLibraryCacheGets_Type()
)
oraDbLibraryCacheGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheGets.setStatus("mandatory")
_OraDbLibraryCacheGetHits_Type = Counter32
_OraDbLibraryCacheGetHits_Object = MibTableColumn
oraDbLibraryCacheGetHits = _OraDbLibraryCacheGetHits_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 4),
    _OraDbLibraryCacheGetHits_Type()
)
oraDbLibraryCacheGetHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheGetHits.setStatus("mandatory")
_OraDbLibraryCachePins_Type = Counter32
_OraDbLibraryCachePins_Object = MibTableColumn
oraDbLibraryCachePins = _OraDbLibraryCachePins_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 5),
    _OraDbLibraryCachePins_Type()
)
oraDbLibraryCachePins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCachePins.setStatus("mandatory")
_OraDbLibraryCachePinHits_Type = Counter32
_OraDbLibraryCachePinHits_Object = MibTableColumn
oraDbLibraryCachePinHits = _OraDbLibraryCachePinHits_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 6),
    _OraDbLibraryCachePinHits_Type()
)
oraDbLibraryCachePinHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCachePinHits.setStatus("mandatory")
_OraDbLibraryCacheReloads_Type = Counter32
_OraDbLibraryCacheReloads_Object = MibTableColumn
oraDbLibraryCacheReloads = _OraDbLibraryCacheReloads_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 7),
    _OraDbLibraryCacheReloads_Type()
)
oraDbLibraryCacheReloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheReloads.setStatus("mandatory")
_OraDbLibraryCacheInvalidations_Type = Counter32
_OraDbLibraryCacheInvalidations_Object = MibTableColumn
oraDbLibraryCacheInvalidations = _OraDbLibraryCacheInvalidations_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 4, 1, 8),
    _OraDbLibraryCacheInvalidations_Type()
)
oraDbLibraryCacheInvalidations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheInvalidations.setStatus("mandatory")
_OraDbLibraryCacheSumTable_Object = MibTable
oraDbLibraryCacheSumTable = _OraDbLibraryCacheSumTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5)
)
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumTable.setStatus("mandatory")
_OraDbLibraryCacheSumEntry_Object = MibTableRow
oraDbLibraryCacheSumEntry = _OraDbLibraryCacheSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1)
)
oraDbLibraryCacheSumEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumEntry.setStatus("mandatory")
_OraDbLibraryCacheSumGets_Type = Counter32
_OraDbLibraryCacheSumGets_Object = MibTableColumn
oraDbLibraryCacheSumGets = _OraDbLibraryCacheSumGets_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 1),
    _OraDbLibraryCacheSumGets_Type()
)
oraDbLibraryCacheSumGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumGets.setStatus("mandatory")
_OraDbLibraryCacheSumGetHits_Type = Counter32
_OraDbLibraryCacheSumGetHits_Object = MibTableColumn
oraDbLibraryCacheSumGetHits = _OraDbLibraryCacheSumGetHits_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 2),
    _OraDbLibraryCacheSumGetHits_Type()
)
oraDbLibraryCacheSumGetHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumGetHits.setStatus("mandatory")
_OraDbLibraryCacheSumPins_Type = Counter32
_OraDbLibraryCacheSumPins_Object = MibTableColumn
oraDbLibraryCacheSumPins = _OraDbLibraryCacheSumPins_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 3),
    _OraDbLibraryCacheSumPins_Type()
)
oraDbLibraryCacheSumPins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumPins.setStatus("mandatory")
_OraDbLibraryCacheSumPinHits_Type = Counter32
_OraDbLibraryCacheSumPinHits_Object = MibTableColumn
oraDbLibraryCacheSumPinHits = _OraDbLibraryCacheSumPinHits_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 4),
    _OraDbLibraryCacheSumPinHits_Type()
)
oraDbLibraryCacheSumPinHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumPinHits.setStatus("mandatory")
_OraDbLibraryCacheSumReloads_Type = Counter32
_OraDbLibraryCacheSumReloads_Object = MibTableColumn
oraDbLibraryCacheSumReloads = _OraDbLibraryCacheSumReloads_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 5),
    _OraDbLibraryCacheSumReloads_Type()
)
oraDbLibraryCacheSumReloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumReloads.setStatus("mandatory")
_OraDbLibraryCacheSumInvalidations_Type = Counter32
_OraDbLibraryCacheSumInvalidations_Object = MibTableColumn
oraDbLibraryCacheSumInvalidations = _OraDbLibraryCacheSumInvalidations_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 5, 1, 6),
    _OraDbLibraryCacheSumInvalidations_Type()
)
oraDbLibraryCacheSumInvalidations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbLibraryCacheSumInvalidations.setStatus("mandatory")
_OraDbSGATable_Object = MibTable
oraDbSGATable = _OraDbSGATable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6)
)
if mibBuilder.loadTexts:
    oraDbSGATable.setStatus("mandatory")
_OraDbSGAEntry_Object = MibTableRow
oraDbSGAEntry = _OraDbSGAEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6, 1)
)
oraDbSGAEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    oraDbSGAEntry.setStatus("mandatory")
_OraDbSGAFixedSize_Type = Integer32
_OraDbSGAFixedSize_Object = MibTableColumn
oraDbSGAFixedSize = _OraDbSGAFixedSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6, 1, 1),
    _OraDbSGAFixedSize_Type()
)
oraDbSGAFixedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSGAFixedSize.setStatus("mandatory")
_OraDbSGAVariableSize_Type = Integer32
_OraDbSGAVariableSize_Object = MibTableColumn
oraDbSGAVariableSize = _OraDbSGAVariableSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6, 1, 2),
    _OraDbSGAVariableSize_Type()
)
oraDbSGAVariableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSGAVariableSize.setStatus("mandatory")
_OraDbSGADatabaseBuffers_Type = Integer32
_OraDbSGADatabaseBuffers_Object = MibTableColumn
oraDbSGADatabaseBuffers = _OraDbSGADatabaseBuffers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6, 1, 3),
    _OraDbSGADatabaseBuffers_Type()
)
oraDbSGADatabaseBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSGADatabaseBuffers.setStatus("mandatory")
_OraDbSGARedoBuffers_Type = Integer32
_OraDbSGARedoBuffers_Object = MibTableColumn
oraDbSGARedoBuffers = _OraDbSGARedoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 6, 1, 4),
    _OraDbSGARedoBuffers_Type()
)
oraDbSGARedoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbSGARedoBuffers.setStatus("mandatory")
_OraDbConfigTable_Object = MibTable
oraDbConfigTable = _OraDbConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7)
)
if mibBuilder.loadTexts:
    oraDbConfigTable.setStatus("mandatory")
_OraDbConfigEntry_Object = MibTableRow
oraDbConfigEntry = _OraDbConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1)
)
oraDbConfigEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    oraDbConfigEntry.setStatus("mandatory")
_OraDbConfigDbBlockBuffers_Type = Integer32
_OraDbConfigDbBlockBuffers_Object = MibTableColumn
oraDbConfigDbBlockBuffers = _OraDbConfigDbBlockBuffers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 1),
    _OraDbConfigDbBlockBuffers_Type()
)
oraDbConfigDbBlockBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDbBlockBuffers.setStatus("mandatory")
_OraDbConfigDbBlockCkptBatch_Type = Integer32
_OraDbConfigDbBlockCkptBatch_Object = MibTableColumn
oraDbConfigDbBlockCkptBatch = _OraDbConfigDbBlockCkptBatch_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 2),
    _OraDbConfigDbBlockCkptBatch_Type()
)
oraDbConfigDbBlockCkptBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDbBlockCkptBatch.setStatus("mandatory")
_OraDbConfigDbBlockSize_Type = Integer32
_OraDbConfigDbBlockSize_Object = MibTableColumn
oraDbConfigDbBlockSize = _OraDbConfigDbBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 3),
    _OraDbConfigDbBlockSize_Type()
)
oraDbConfigDbBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDbBlockSize.setStatus("mandatory")
_OraDbConfigDbFileSimWrites_Type = Integer32
_OraDbConfigDbFileSimWrites_Object = MibTableColumn
oraDbConfigDbFileSimWrites = _OraDbConfigDbFileSimWrites_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 4),
    _OraDbConfigDbFileSimWrites_Type()
)
oraDbConfigDbFileSimWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDbFileSimWrites.setStatus("mandatory")
_OraDbConfigDbMultiBlockReadCount_Type = Integer32
_OraDbConfigDbMultiBlockReadCount_Object = MibTableColumn
oraDbConfigDbMultiBlockReadCount = _OraDbConfigDbMultiBlockReadCount_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 5),
    _OraDbConfigDbMultiBlockReadCount_Type()
)
oraDbConfigDbMultiBlockReadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDbMultiBlockReadCount.setStatus("mandatory")
_OraDbConfigDistLockTimeout_Type = Integer32
_OraDbConfigDistLockTimeout_Object = MibTableColumn
oraDbConfigDistLockTimeout = _OraDbConfigDistLockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 6),
    _OraDbConfigDistLockTimeout_Type()
)
oraDbConfigDistLockTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDistLockTimeout.setStatus("mandatory")
_OraDbConfigDistRecoveryConnectHold_Type = Integer32
_OraDbConfigDistRecoveryConnectHold_Object = MibTableColumn
oraDbConfigDistRecoveryConnectHold = _OraDbConfigDistRecoveryConnectHold_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 7),
    _OraDbConfigDistRecoveryConnectHold_Type()
)
oraDbConfigDistRecoveryConnectHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDistRecoveryConnectHold.setStatus("mandatory")
_OraDbConfigDistTransactions_Type = Integer32
_OraDbConfigDistTransactions_Object = MibTableColumn
oraDbConfigDistTransactions = _OraDbConfigDistTransactions_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 8),
    _OraDbConfigDistTransactions_Type()
)
oraDbConfigDistTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigDistTransactions.setStatus("mandatory")
_OraDbConfigLogArchiveBufferSize_Type = Integer32
_OraDbConfigLogArchiveBufferSize_Object = MibTableColumn
oraDbConfigLogArchiveBufferSize = _OraDbConfigLogArchiveBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 9),
    _OraDbConfigLogArchiveBufferSize_Type()
)
oraDbConfigLogArchiveBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogArchiveBufferSize.setStatus("mandatory")
_OraDbConfigLogArchiveBuffers_Type = Integer32
_OraDbConfigLogArchiveBuffers_Object = MibTableColumn
oraDbConfigLogArchiveBuffers = _OraDbConfigLogArchiveBuffers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 10),
    _OraDbConfigLogArchiveBuffers_Type()
)
oraDbConfigLogArchiveBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogArchiveBuffers.setStatus("mandatory")
_OraDbConfigLogBuffer_Type = Integer32
_OraDbConfigLogBuffer_Object = MibTableColumn
oraDbConfigLogBuffer = _OraDbConfigLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 11),
    _OraDbConfigLogBuffer_Type()
)
oraDbConfigLogBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogBuffer.setStatus("mandatory")
_OraDbConfigLogCheckpointInterval_Type = Integer32
_OraDbConfigLogCheckpointInterval_Object = MibTableColumn
oraDbConfigLogCheckpointInterval = _OraDbConfigLogCheckpointInterval_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 12),
    _OraDbConfigLogCheckpointInterval_Type()
)
oraDbConfigLogCheckpointInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogCheckpointInterval.setStatus("mandatory")
_OraDbConfigLogCheckpointTimeout_Type = Integer32
_OraDbConfigLogCheckpointTimeout_Object = MibTableColumn
oraDbConfigLogCheckpointTimeout = _OraDbConfigLogCheckpointTimeout_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 13),
    _OraDbConfigLogCheckpointTimeout_Type()
)
oraDbConfigLogCheckpointTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogCheckpointTimeout.setStatus("mandatory")
_OraDbConfigLogFiles_Type = Integer32
_OraDbConfigLogFiles_Object = MibTableColumn
oraDbConfigLogFiles = _OraDbConfigLogFiles_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 14),
    _OraDbConfigLogFiles_Type()
)
oraDbConfigLogFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigLogFiles.setStatus("mandatory")
_OraDbConfigMaxRollbackSegments_Type = Integer32
_OraDbConfigMaxRollbackSegments_Object = MibTableColumn
oraDbConfigMaxRollbackSegments = _OraDbConfigMaxRollbackSegments_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 15),
    _OraDbConfigMaxRollbackSegments_Type()
)
oraDbConfigMaxRollbackSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigMaxRollbackSegments.setStatus("mandatory")
_OraDbConfigMTSMaxDispatchers_Type = Integer32
_OraDbConfigMTSMaxDispatchers_Object = MibTableColumn
oraDbConfigMTSMaxDispatchers = _OraDbConfigMTSMaxDispatchers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 16),
    _OraDbConfigMTSMaxDispatchers_Type()
)
oraDbConfigMTSMaxDispatchers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigMTSMaxDispatchers.setStatus("mandatory")
_OraDbConfigMTSMaxServers_Type = Integer32
_OraDbConfigMTSMaxServers_Object = MibTableColumn
oraDbConfigMTSMaxServers = _OraDbConfigMTSMaxServers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 17),
    _OraDbConfigMTSMaxServers_Type()
)
oraDbConfigMTSMaxServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigMTSMaxServers.setStatus("mandatory")
_OraDbConfigMTSServers_Type = Integer32
_OraDbConfigMTSServers_Object = MibTableColumn
oraDbConfigMTSServers = _OraDbConfigMTSServers_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 18),
    _OraDbConfigMTSServers_Type()
)
oraDbConfigMTSServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigMTSServers.setStatus("mandatory")
_OraDbConfigOpenCursors_Type = Integer32
_OraDbConfigOpenCursors_Object = MibTableColumn
oraDbConfigOpenCursors = _OraDbConfigOpenCursors_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 19),
    _OraDbConfigOpenCursors_Type()
)
oraDbConfigOpenCursors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigOpenCursors.setStatus("mandatory")
_OraDbConfigOpenLinks_Type = Integer32
_OraDbConfigOpenLinks_Object = MibTableColumn
oraDbConfigOpenLinks = _OraDbConfigOpenLinks_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 20),
    _OraDbConfigOpenLinks_Type()
)
oraDbConfigOpenLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigOpenLinks.setStatus("mandatory")
_OraDbConfigOptimizerMode_Type = DisplayString
_OraDbConfigOptimizerMode_Object = MibTableColumn
oraDbConfigOptimizerMode = _OraDbConfigOptimizerMode_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 21),
    _OraDbConfigOptimizerMode_Type()
)
oraDbConfigOptimizerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigOptimizerMode.setStatus("mandatory")
_OraDbConfigProcesses_Type = Integer32
_OraDbConfigProcesses_Object = MibTableColumn
oraDbConfigProcesses = _OraDbConfigProcesses_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 22),
    _OraDbConfigProcesses_Type()
)
oraDbConfigProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigProcesses.setStatus("mandatory")
_OraDbConfigSerializable_Type = TruthValue
_OraDbConfigSerializable_Object = MibTableColumn
oraDbConfigSerializable = _OraDbConfigSerializable_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 23),
    _OraDbConfigSerializable_Type()
)
oraDbConfigSerializable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigSerializable.setStatus("mandatory")
_OraDbConfigSessions_Type = Integer32
_OraDbConfigSessions_Object = MibTableColumn
oraDbConfigSessions = _OraDbConfigSessions_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 24),
    _OraDbConfigSessions_Type()
)
oraDbConfigSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigSessions.setStatus("mandatory")
_OraDbConfigSharedPool_Type = Integer32
_OraDbConfigSharedPool_Object = MibTableColumn
oraDbConfigSharedPool = _OraDbConfigSharedPool_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 25),
    _OraDbConfigSharedPool_Type()
)
oraDbConfigSharedPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigSharedPool.setStatus("mandatory")
_OraDbConfigSortAreaSize_Type = Integer32
_OraDbConfigSortAreaSize_Object = MibTableColumn
oraDbConfigSortAreaSize = _OraDbConfigSortAreaSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 26),
    _OraDbConfigSortAreaSize_Type()
)
oraDbConfigSortAreaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigSortAreaSize.setStatus("mandatory")
_OraDbConfigSortAreaRetainedSize_Type = Integer32
_OraDbConfigSortAreaRetainedSize_Object = MibTableColumn
oraDbConfigSortAreaRetainedSize = _OraDbConfigSortAreaRetainedSize_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 27),
    _OraDbConfigSortAreaRetainedSize_Type()
)
oraDbConfigSortAreaRetainedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigSortAreaRetainedSize.setStatus("mandatory")
_OraDbConfigTransactions_Type = Integer32
_OraDbConfigTransactions_Object = MibTableColumn
oraDbConfigTransactions = _OraDbConfigTransactions_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 28),
    _OraDbConfigTransactions_Type()
)
oraDbConfigTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigTransactions.setStatus("mandatory")
_OraDbConfigTransactionsPerRollback_Type = Integer32
_OraDbConfigTransactionsPerRollback_Object = MibTableColumn
oraDbConfigTransactionsPerRollback = _OraDbConfigTransactionsPerRollback_Object(
    (1, 3, 6, 1, 4, 1, 111, 4, 1, 7, 1, 29),
    _OraDbConfigTransactionsPerRollback_Type()
)
oraDbConfigTransactionsPerRollback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDbConfigTransactionsPerRollback.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORADB-MIB",
    **{"DateAndTime": DateAndTime,
       "TruthValue": TruthValue,
       "oracle": oracle,
       "oraDbMIB": oraDbMIB,
       "oraDbObjects": oraDbObjects,
       "oraDbSysTable": oraDbSysTable,
       "oraDbSysEntry": oraDbSysEntry,
       "oraDbSysConsistentChanges": oraDbSysConsistentChanges,
       "oraDbSysConsistentGets": oraDbSysConsistentGets,
       "oraDbSysDbBlockChanges": oraDbSysDbBlockChanges,
       "oraDbSysDbBlockGets": oraDbSysDbBlockGets,
       "oraDbSysFreeBufferInspected": oraDbSysFreeBufferInspected,
       "oraDbSysFreeBufferRequested": oraDbSysFreeBufferRequested,
       "oraDbSysParseCount": oraDbSysParseCount,
       "oraDbSysPhysReads": oraDbSysPhysReads,
       "oraDbSysPhysWrites": oraDbSysPhysWrites,
       "oraDbSysRedoEntries": oraDbSysRedoEntries,
       "oraDbSysRedoLogSpaceRequests": oraDbSysRedoLogSpaceRequests,
       "oraDbSysRedoSyncWrites": oraDbSysRedoSyncWrites,
       "oraDbSysSortsDisk": oraDbSysSortsDisk,
       "oraDbSysSortsMemory": oraDbSysSortsMemory,
       "oraDbSysSortsRows": oraDbSysSortsRows,
       "oraDbSysTableFetchRowid": oraDbSysTableFetchRowid,
       "oraDbSysTableFetchContinuedRow": oraDbSysTableFetchContinuedRow,
       "oraDbSysTableScanBlocks": oraDbSysTableScanBlocks,
       "oraDbSysTableScanRows": oraDbSysTableScanRows,
       "oraDbSysTableScansLong": oraDbSysTableScansLong,
       "oraDbSysTableScansShort": oraDbSysTableScansShort,
       "oraDbSysUserCalls": oraDbSysUserCalls,
       "oraDbSysUserCommits": oraDbSysUserCommits,
       "oraDbSysUserRollbacks": oraDbSysUserRollbacks,
       "oraDbSysWriteRequests": oraDbSysWriteRequests,
       "oraDbTablespaceTable": oraDbTablespaceTable,
       "oraDbTablespaceEntry": oraDbTablespaceEntry,
       "oraDbTablespaceIndex": oraDbTablespaceIndex,
       "oraDbTablespaceName": oraDbTablespaceName,
       "oraDbTablespaceSizeAllocated": oraDbTablespaceSizeAllocated,
       "oraDbTablespaceSizeUsed": oraDbTablespaceSizeUsed,
       "oraDbTablespaceState": oraDbTablespaceState,
       "oraDbTablespaceLargestAvailableChunk": oraDbTablespaceLargestAvailableChunk,
       "oraDbDataFileTable": oraDbDataFileTable,
       "oraDbDataFileEntry": oraDbDataFileEntry,
       "oraDbDataFileIndex": oraDbDataFileIndex,
       "oraDbDataFileName": oraDbDataFileName,
       "oraDbDataFileSizeAllocated": oraDbDataFileSizeAllocated,
       "oraDbDataFileDiskReads": oraDbDataFileDiskReads,
       "oraDbDataFileDiskWrites": oraDbDataFileDiskWrites,
       "oraDbDataFileDiskReadBlocks": oraDbDataFileDiskReadBlocks,
       "oraDbDataFileDiskWrittenBlocks": oraDbDataFileDiskWrittenBlocks,
       "oraDbDataFileDiskReadTimeTicks": oraDbDataFileDiskReadTimeTicks,
       "oraDbDataFileDiskWriteTimeTicks": oraDbDataFileDiskWriteTimeTicks,
       "oraDbLibraryCacheTable": oraDbLibraryCacheTable,
       "oraDbLibraryCacheEntry": oraDbLibraryCacheEntry,
       "oraDbLibraryCacheIndex": oraDbLibraryCacheIndex,
       "oraDbLibraryCacheNameSpace": oraDbLibraryCacheNameSpace,
       "oraDbLibraryCacheGets": oraDbLibraryCacheGets,
       "oraDbLibraryCacheGetHits": oraDbLibraryCacheGetHits,
       "oraDbLibraryCachePins": oraDbLibraryCachePins,
       "oraDbLibraryCachePinHits": oraDbLibraryCachePinHits,
       "oraDbLibraryCacheReloads": oraDbLibraryCacheReloads,
       "oraDbLibraryCacheInvalidations": oraDbLibraryCacheInvalidations,
       "oraDbLibraryCacheSumTable": oraDbLibraryCacheSumTable,
       "oraDbLibraryCacheSumEntry": oraDbLibraryCacheSumEntry,
       "oraDbLibraryCacheSumGets": oraDbLibraryCacheSumGets,
       "oraDbLibraryCacheSumGetHits": oraDbLibraryCacheSumGetHits,
       "oraDbLibraryCacheSumPins": oraDbLibraryCacheSumPins,
       "oraDbLibraryCacheSumPinHits": oraDbLibraryCacheSumPinHits,
       "oraDbLibraryCacheSumReloads": oraDbLibraryCacheSumReloads,
       "oraDbLibraryCacheSumInvalidations": oraDbLibraryCacheSumInvalidations,
       "oraDbSGATable": oraDbSGATable,
       "oraDbSGAEntry": oraDbSGAEntry,
       "oraDbSGAFixedSize": oraDbSGAFixedSize,
       "oraDbSGAVariableSize": oraDbSGAVariableSize,
       "oraDbSGADatabaseBuffers": oraDbSGADatabaseBuffers,
       "oraDbSGARedoBuffers": oraDbSGARedoBuffers,
       "oraDbConfigTable": oraDbConfigTable,
       "oraDbConfigEntry": oraDbConfigEntry,
       "oraDbConfigDbBlockBuffers": oraDbConfigDbBlockBuffers,
       "oraDbConfigDbBlockCkptBatch": oraDbConfigDbBlockCkptBatch,
       "oraDbConfigDbBlockSize": oraDbConfigDbBlockSize,
       "oraDbConfigDbFileSimWrites": oraDbConfigDbFileSimWrites,
       "oraDbConfigDbMultiBlockReadCount": oraDbConfigDbMultiBlockReadCount,
       "oraDbConfigDistLockTimeout": oraDbConfigDistLockTimeout,
       "oraDbConfigDistRecoveryConnectHold": oraDbConfigDistRecoveryConnectHold,
       "oraDbConfigDistTransactions": oraDbConfigDistTransactions,
       "oraDbConfigLogArchiveBufferSize": oraDbConfigLogArchiveBufferSize,
       "oraDbConfigLogArchiveBuffers": oraDbConfigLogArchiveBuffers,
       "oraDbConfigLogBuffer": oraDbConfigLogBuffer,
       "oraDbConfigLogCheckpointInterval": oraDbConfigLogCheckpointInterval,
       "oraDbConfigLogCheckpointTimeout": oraDbConfigLogCheckpointTimeout,
       "oraDbConfigLogFiles": oraDbConfigLogFiles,
       "oraDbConfigMaxRollbackSegments": oraDbConfigMaxRollbackSegments,
       "oraDbConfigMTSMaxDispatchers": oraDbConfigMTSMaxDispatchers,
       "oraDbConfigMTSMaxServers": oraDbConfigMTSMaxServers,
       "oraDbConfigMTSServers": oraDbConfigMTSServers,
       "oraDbConfigOpenCursors": oraDbConfigOpenCursors,
       "oraDbConfigOpenLinks": oraDbConfigOpenLinks,
       "oraDbConfigOptimizerMode": oraDbConfigOptimizerMode,
       "oraDbConfigProcesses": oraDbConfigProcesses,
       "oraDbConfigSerializable": oraDbConfigSerializable,
       "oraDbConfigSessions": oraDbConfigSessions,
       "oraDbConfigSharedPool": oraDbConfigSharedPool,
       "oraDbConfigSortAreaSize": oraDbConfigSortAreaSize,
       "oraDbConfigSortAreaRetainedSize": oraDbConfigSortAreaRetainedSize,
       "oraDbConfigTransactions": oraDbConfigTransactions,
       "oraDbConfigTransactionsPerRollback": oraDbConfigTransactionsPerRollback}
)
