# SNMP MIB module (CISCO-BULK-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BULK-FILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:26 2024
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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoBulkFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81)
)
ciscoBulkFileMIB.setRevisions(
        ("2002-06-10 00:00",
         "2002-05-15 00:00",
         "2001-08-22 00:00",
         "2001-08-01 00:00",
         "2001-06-26 17:00",
         "1998-10-29 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBulkFileMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBObjects = _CiscoBulkFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1)
)
_CbfDefine_ObjectIdentity = ObjectIdentity
cbfDefine = _CbfDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1)
)


class _CbfDefineMaxFiles_Type(Unsigned32):
    """Custom type cbfDefineMaxFiles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbfDefineMaxFiles_Type.__name__ = "Unsigned32"
_CbfDefineMaxFiles_Object = MibScalar
cbfDefineMaxFiles = _CbfDefineMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 1),
    _CbfDefineMaxFiles_Type()
)
cbfDefineMaxFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbfDefineMaxFiles.setStatus("current")
_CbfDefineFiles_Type = Gauge32
_CbfDefineFiles_Object = MibScalar
cbfDefineFiles = _CbfDefineFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 2),
    _CbfDefineFiles_Type()
)
cbfDefineFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineFiles.setStatus("current")
_CbfDefineHighFiles_Type = Gauge32
_CbfDefineHighFiles_Object = MibScalar
cbfDefineHighFiles = _CbfDefineHighFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 3),
    _CbfDefineHighFiles_Type()
)
cbfDefineHighFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineHighFiles.setStatus("current")
_CbfDefineFilesRefused_Type = Counter32
_CbfDefineFilesRefused_Object = MibScalar
cbfDefineFilesRefused = _CbfDefineFilesRefused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 4),
    _CbfDefineFilesRefused_Type()
)
cbfDefineFilesRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineFilesRefused.setStatus("current")


class _CbfDefineMaxObjects_Type(Unsigned32):
    """Custom type cbfDefineMaxObjects based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbfDefineMaxObjects_Type.__name__ = "Unsigned32"
_CbfDefineMaxObjects_Object = MibScalar
cbfDefineMaxObjects = _CbfDefineMaxObjects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 5),
    _CbfDefineMaxObjects_Type()
)
cbfDefineMaxObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbfDefineMaxObjects.setStatus("current")
_CbfDefineObjects_Type = Gauge32
_CbfDefineObjects_Object = MibScalar
cbfDefineObjects = _CbfDefineObjects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 6),
    _CbfDefineObjects_Type()
)
cbfDefineObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineObjects.setStatus("current")
_CbfDefineHighObjects_Type = Gauge32
_CbfDefineHighObjects_Object = MibScalar
cbfDefineHighObjects = _CbfDefineHighObjects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 7),
    _CbfDefineHighObjects_Type()
)
cbfDefineHighObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineHighObjects.setStatus("current")
_CbfDefineObjectsRefused_Type = Counter32
_CbfDefineObjectsRefused_Object = MibScalar
cbfDefineObjectsRefused = _CbfDefineObjectsRefused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 8),
    _CbfDefineObjectsRefused_Type()
)
cbfDefineObjectsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineObjectsRefused.setStatus("current")
_CbfDefineFileTable_Object = MibTable
cbfDefineFileTable = _CbfDefineFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cbfDefineFileTable.setStatus("current")
_CbfDefineFileEntry_Object = MibTableRow
cbfDefineFileEntry = _CbfDefineFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1)
)
cbfDefineFileEntry.setIndexNames(
    (0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"),
)
if mibBuilder.loadTexts:
    cbfDefineFileEntry.setStatus("current")


class _CbfDefineFileIndex_Type(Unsigned32):
    """Custom type cbfDefineFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbfDefineFileIndex_Type.__name__ = "Unsigned32"
_CbfDefineFileIndex_Object = MibTableColumn
cbfDefineFileIndex = _CbfDefineFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 1),
    _CbfDefineFileIndex_Type()
)
cbfDefineFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbfDefineFileIndex.setStatus("current")


class _CbfDefineFileName_Type(DisplayString):
    """Custom type cbfDefineFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbfDefineFileName_Type.__name__ = "DisplayString"
_CbfDefineFileName_Object = MibTableColumn
cbfDefineFileName = _CbfDefineFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 2),
    _CbfDefineFileName_Type()
)
cbfDefineFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileName.setStatus("current")


class _CbfDefineFileStorage_Type(Integer32):
    """Custom type cbfDefineFileStorage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ephemeral", 1),
          ("permanent", 3),
          ("volatile", 2))
    )


_CbfDefineFileStorage_Type.__name__ = "Integer32"
_CbfDefineFileStorage_Object = MibTableColumn
cbfDefineFileStorage = _CbfDefineFileStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 3),
    _CbfDefineFileStorage_Type()
)
cbfDefineFileStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileStorage.setStatus("current")


class _CbfDefineFileFormat_Type(Integer32):
    """Custom type cbfDefineFileFormat based on Integer32"""
    defaultValue = 2

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
        *(("bulkASCII", 3),
          ("bulkBinary", 2),
          ("standardBER", 1),
          ("variantBERWithCksum", 4),
          ("variantBinWithCksum", 5))
    )


_CbfDefineFileFormat_Type.__name__ = "Integer32"
_CbfDefineFileFormat_Object = MibTableColumn
cbfDefineFileFormat = _CbfDefineFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 4),
    _CbfDefineFileFormat_Type()
)
cbfDefineFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileFormat.setStatus("current")


class _CbfDefineFileNow_Type(Integer32):
    """Custom type cbfDefineFileNow based on Integer32"""
    defaultValue = 1

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
        *(("create", 3),
          ("forcedCreate", 5),
          ("notActive", 1),
          ("ready", 2),
          ("running", 4))
    )


_CbfDefineFileNow_Type.__name__ = "Integer32"
_CbfDefineFileNow_Object = MibTableColumn
cbfDefineFileNow = _CbfDefineFileNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 5),
    _CbfDefineFileNow_Type()
)
cbfDefineFileNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileNow.setStatus("current")
_CbfDefineFileEntryStatus_Type = RowStatus
_CbfDefineFileEntryStatus_Object = MibTableColumn
cbfDefineFileEntryStatus = _CbfDefineFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 6),
    _CbfDefineFileEntryStatus_Type()
)
cbfDefineFileEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileEntryStatus.setStatus("current")


class _CbfDefineFileNotifyOnCompletion_Type(TruthValue):
    """Custom type cbfDefineFileNotifyOnCompletion based on TruthValue"""


_CbfDefineFileNotifyOnCompletion_Object = MibTableColumn
cbfDefineFileNotifyOnCompletion = _CbfDefineFileNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 7),
    _CbfDefineFileNotifyOnCompletion_Type()
)
cbfDefineFileNotifyOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineFileNotifyOnCompletion.setStatus("current")
_CbfDefineObjectTable_Object = MibTable
cbfDefineObjectTable = _CbfDefineObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cbfDefineObjectTable.setStatus("current")
_CbfDefineObjectEntry_Object = MibTableRow
cbfDefineObjectEntry = _CbfDefineObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1)
)
cbfDefineObjectEntry.setIndexNames(
    (0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"),
    (0, "CISCO-BULK-FILE-MIB", "cbfDefineObjectIndex"),
)
if mibBuilder.loadTexts:
    cbfDefineObjectEntry.setStatus("current")


class _CbfDefineObjectIndex_Type(Unsigned32):
    """Custom type cbfDefineObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbfDefineObjectIndex_Type.__name__ = "Unsigned32"
_CbfDefineObjectIndex_Object = MibTableColumn
cbfDefineObjectIndex = _CbfDefineObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 1),
    _CbfDefineObjectIndex_Type()
)
cbfDefineObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbfDefineObjectIndex.setStatus("current")


class _CbfDefineObjectClass_Type(Integer32):
    """Custom type cbfDefineObjectClass based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leastCpuTable", 3),
          ("lexicalTable", 2),
          ("object", 1))
    )


_CbfDefineObjectClass_Type.__name__ = "Integer32"
_CbfDefineObjectClass_Object = MibTableColumn
cbfDefineObjectClass = _CbfDefineObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 2),
    _CbfDefineObjectClass_Type()
)
cbfDefineObjectClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineObjectClass.setStatus("current")


class _CbfDefineObjectID_Type(ObjectIdentifier):
    """Custom type cbfDefineObjectID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_CbfDefineObjectID_Object = MibTableColumn
cbfDefineObjectID = _CbfDefineObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 3),
    _CbfDefineObjectID_Type()
)
cbfDefineObjectID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineObjectID.setStatus("current")
_CbfDefineObjectEntryStatus_Type = RowStatus
_CbfDefineObjectEntryStatus_Object = MibTableColumn
cbfDefineObjectEntryStatus = _CbfDefineObjectEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 4),
    _CbfDefineObjectEntryStatus_Type()
)
cbfDefineObjectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineObjectEntryStatus.setStatus("current")


class _CbfDefineObjectTableInstance_Type(ObjectIdentifier):
    """Custom type cbfDefineObjectTableInstance based on ObjectIdentifier"""
    defaultValue = (0, 0)


_CbfDefineObjectTableInstance_Object = MibTableColumn
cbfDefineObjectTableInstance = _CbfDefineObjectTableInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 5),
    _CbfDefineObjectTableInstance_Type()
)
cbfDefineObjectTableInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineObjectTableInstance.setStatus("current")


class _CbfDefineObjectNumEntries_Type(Unsigned32):
    """Custom type cbfDefineObjectNumEntries based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbfDefineObjectNumEntries_Type.__name__ = "Unsigned32"
_CbfDefineObjectNumEntries_Object = MibTableColumn
cbfDefineObjectNumEntries = _CbfDefineObjectNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 6),
    _CbfDefineObjectNumEntries_Type()
)
cbfDefineObjectNumEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbfDefineObjectNumEntries.setStatus("current")
_CbfDefineObjectLastPolledInst_Type = ObjectIdentifier
_CbfDefineObjectLastPolledInst_Object = MibTableColumn
cbfDefineObjectLastPolledInst = _CbfDefineObjectLastPolledInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 7),
    _CbfDefineObjectLastPolledInst_Type()
)
cbfDefineObjectLastPolledInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfDefineObjectLastPolledInst.setStatus("current")
_CbfStatus_ObjectIdentity = ObjectIdentity
cbfStatus = _CbfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2)
)


class _CbfStatusMaxFiles_Type(Unsigned32):
    """Custom type cbfStatusMaxFiles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbfStatusMaxFiles_Type.__name__ = "Unsigned32"
_CbfStatusMaxFiles_Object = MibScalar
cbfStatusMaxFiles = _CbfStatusMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 1),
    _CbfStatusMaxFiles_Type()
)
cbfStatusMaxFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbfStatusMaxFiles.setStatus("current")
_CbfStatusFiles_Type = Gauge32
_CbfStatusFiles_Object = MibScalar
cbfStatusFiles = _CbfStatusFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 2),
    _CbfStatusFiles_Type()
)
cbfStatusFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfStatusFiles.setStatus("current")
_CbfStatusHighFiles_Type = Gauge32
_CbfStatusHighFiles_Object = MibScalar
cbfStatusHighFiles = _CbfStatusHighFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 3),
    _CbfStatusHighFiles_Type()
)
cbfStatusHighFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfStatusHighFiles.setStatus("current")
_CbfStatusFilesBumped_Type = Counter32
_CbfStatusFilesBumped_Object = MibScalar
cbfStatusFilesBumped = _CbfStatusFilesBumped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 4),
    _CbfStatusFilesBumped_Type()
)
cbfStatusFilesBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfStatusFilesBumped.setStatus("current")
_CbfStatusFileTable_Object = MibTable
cbfStatusFileTable = _CbfStatusFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cbfStatusFileTable.setStatus("current")
_CbfStatusFileEntry_Object = MibTableRow
cbfStatusFileEntry = _CbfStatusFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1)
)
cbfStatusFileEntry.setIndexNames(
    (0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"),
    (0, "CISCO-BULK-FILE-MIB", "cbfStatusFileIndex"),
)
if mibBuilder.loadTexts:
    cbfStatusFileEntry.setStatus("current")


class _CbfStatusFileIndex_Type(Unsigned32):
    """Custom type cbfStatusFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbfStatusFileIndex_Type.__name__ = "Unsigned32"
_CbfStatusFileIndex_Object = MibTableColumn
cbfStatusFileIndex = _CbfStatusFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 1),
    _CbfStatusFileIndex_Type()
)
cbfStatusFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbfStatusFileIndex.setStatus("current")


class _CbfStatusFileState_Type(Integer32):
    """Custom type cbfStatusFileState based on Integer32"""
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
        *(("aborted", 9),
          ("badName", 5),
          ("buffErr", 8),
          ("emptied", 3),
          ("noMem", 7),
          ("noSpace", 4),
          ("ready", 2),
          ("running", 1),
          ("writeErr", 6))
    )


_CbfStatusFileState_Type.__name__ = "Integer32"
_CbfStatusFileState_Object = MibTableColumn
cbfStatusFileState = _CbfStatusFileState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 2),
    _CbfStatusFileState_Type()
)
cbfStatusFileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfStatusFileState.setStatus("current")
_CbfStatusFileCompletionTime_Type = TimeStamp
_CbfStatusFileCompletionTime_Object = MibTableColumn
cbfStatusFileCompletionTime = _CbfStatusFileCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 3),
    _CbfStatusFileCompletionTime_Type()
)
cbfStatusFileCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbfStatusFileCompletionTime.setStatus("current")
_CbfStatusFileEntryStatus_Type = RowStatus
_CbfStatusFileEntryStatus_Object = MibTableColumn
cbfStatusFileEntryStatus = _CbfStatusFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 4),
    _CbfStatusFileEntryStatus_Type()
)
cbfStatusFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbfStatusFileEntryStatus.setStatus("current")
_CiscoBulkFileMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBNotificationPrefix = _CiscoBulkFileMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 2)
)
_CiscoBulkFileMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBNotifications = _CiscoBulkFileMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 2, 0)
)
_CiscoBulkFileMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBConformance = _CiscoBulkFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3)
)
_CiscoBulkFileMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBCompliances = _CiscoBulkFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1)
)
_CiscoBulkFileMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBulkFileMIBGroups = _CiscoBulkFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2)
)

# Managed Objects groups

ciscoBulkFileDefineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 1)
)
ciscoBulkFileDefineGroup.setObjects(
      *(("CISCO-BULK-FILE-MIB", "cbfDefineMaxFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineHighFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFilesRefused"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineMaxObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineHighObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectsRefused"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileName"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileStorage"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileFormat"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileNow"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileEntryStatus"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileNotifyOnCompletion"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectClass"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectID"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoBulkFileDefineGroup.setStatus("deprecated")

ciscoBulkFileStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 2)
)
ciscoBulkFileStatusGroup.setObjects(
      *(("CISCO-BULK-FILE-MIB", "cbfStatusMaxFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusHighFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFilesBumped"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFileState"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFileCompletionTime"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFileEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoBulkFileStatusGroup.setStatus("current")

ciscoBulkFileDefineGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 4)
)
ciscoBulkFileDefineGroupRev1.setObjects(
      *(("CISCO-BULK-FILE-MIB", "cbfDefineMaxFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineHighFiles"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFilesRefused"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineMaxObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineHighObjects"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectsRefused"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileName"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileStorage"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileFormat"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileNow"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileEntryStatus"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineFileNotifyOnCompletion"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectClass"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectID"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectEntryStatus"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectTableInstance"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectNumEntries"),
        ("CISCO-BULK-FILE-MIB", "cbfDefineObjectLastPolledInst"))
)
if mibBuilder.loadTexts:
    ciscoBulkFileDefineGroupRev1.setStatus("current")


# Notification objects

cbfDefineFileCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 2, 0, 1)
)
cbfDefineFileCompletion.setObjects(
      *(("CISCO-BULK-FILE-MIB", "cbfStatusFileState"),
        ("CISCO-BULK-FILE-MIB", "cbfStatusFileCompletionTime"))
)
if mibBuilder.loadTexts:
    cbfDefineFileCompletion.setStatus(
        "current"
    )


# Notifications groups

ciscoBulkFileNotiGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 3)
)
ciscoBulkFileNotiGroup.setObjects(
    ("CISCO-BULK-FILE-MIB", "cbfDefineFileCompletion")
)
if mibBuilder.loadTexts:
    ciscoBulkFileNotiGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBulkFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBulkFileMIBCompliance.setStatus(
        "deprecated"
    )

ciscoBulkFileMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoBulkFileMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BULK-FILE-MIB",
    **{"ciscoBulkFileMIB": ciscoBulkFileMIB,
       "ciscoBulkFileMIBObjects": ciscoBulkFileMIBObjects,
       "cbfDefine": cbfDefine,
       "cbfDefineMaxFiles": cbfDefineMaxFiles,
       "cbfDefineFiles": cbfDefineFiles,
       "cbfDefineHighFiles": cbfDefineHighFiles,
       "cbfDefineFilesRefused": cbfDefineFilesRefused,
       "cbfDefineMaxObjects": cbfDefineMaxObjects,
       "cbfDefineObjects": cbfDefineObjects,
       "cbfDefineHighObjects": cbfDefineHighObjects,
       "cbfDefineObjectsRefused": cbfDefineObjectsRefused,
       "cbfDefineFileTable": cbfDefineFileTable,
       "cbfDefineFileEntry": cbfDefineFileEntry,
       "cbfDefineFileIndex": cbfDefineFileIndex,
       "cbfDefineFileName": cbfDefineFileName,
       "cbfDefineFileStorage": cbfDefineFileStorage,
       "cbfDefineFileFormat": cbfDefineFileFormat,
       "cbfDefineFileNow": cbfDefineFileNow,
       "cbfDefineFileEntryStatus": cbfDefineFileEntryStatus,
       "cbfDefineFileNotifyOnCompletion": cbfDefineFileNotifyOnCompletion,
       "cbfDefineObjectTable": cbfDefineObjectTable,
       "cbfDefineObjectEntry": cbfDefineObjectEntry,
       "cbfDefineObjectIndex": cbfDefineObjectIndex,
       "cbfDefineObjectClass": cbfDefineObjectClass,
       "cbfDefineObjectID": cbfDefineObjectID,
       "cbfDefineObjectEntryStatus": cbfDefineObjectEntryStatus,
       "cbfDefineObjectTableInstance": cbfDefineObjectTableInstance,
       "cbfDefineObjectNumEntries": cbfDefineObjectNumEntries,
       "cbfDefineObjectLastPolledInst": cbfDefineObjectLastPolledInst,
       "cbfStatus": cbfStatus,
       "cbfStatusMaxFiles": cbfStatusMaxFiles,
       "cbfStatusFiles": cbfStatusFiles,
       "cbfStatusHighFiles": cbfStatusHighFiles,
       "cbfStatusFilesBumped": cbfStatusFilesBumped,
       "cbfStatusFileTable": cbfStatusFileTable,
       "cbfStatusFileEntry": cbfStatusFileEntry,
       "cbfStatusFileIndex": cbfStatusFileIndex,
       "cbfStatusFileState": cbfStatusFileState,
       "cbfStatusFileCompletionTime": cbfStatusFileCompletionTime,
       "cbfStatusFileEntryStatus": cbfStatusFileEntryStatus,
       "ciscoBulkFileMIBNotificationPrefix": ciscoBulkFileMIBNotificationPrefix,
       "ciscoBulkFileMIBNotifications": ciscoBulkFileMIBNotifications,
       "cbfDefineFileCompletion": cbfDefineFileCompletion,
       "ciscoBulkFileMIBConformance": ciscoBulkFileMIBConformance,
       "ciscoBulkFileMIBCompliances": ciscoBulkFileMIBCompliances,
       "ciscoBulkFileMIBCompliance": ciscoBulkFileMIBCompliance,
       "ciscoBulkFileMIBComplianceRev1": ciscoBulkFileMIBComplianceRev1,
       "ciscoBulkFileMIBGroups": ciscoBulkFileMIBGroups,
       "ciscoBulkFileDefineGroup": ciscoBulkFileDefineGroup,
       "ciscoBulkFileStatusGroup": ciscoBulkFileStatusGroup,
       "ciscoBulkFileNotiGroup": ciscoBulkFileNotiGroup,
       "ciscoBulkFileDefineGroupRev1": ciscoBulkFileDefineGroupRev1}
)
