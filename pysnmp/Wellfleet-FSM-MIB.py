# SNMP MIB module (Wellfleet-FSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:16 2024
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

(wfFileSystemGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFileSystemGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFsBase_ObjectIdentity = ObjectIdentity
wfFsBase = _WfFsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1)
)
_WfFsVolLastUpdated_Type = OctetString
_WfFsVolLastUpdated_Object = MibScalar
wfFsVolLastUpdated = _WfFsVolLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1, 1),
    _WfFsVolLastUpdated_Type()
)
wfFsVolLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsVolLastUpdated.setStatus("mandatory")
_WfFsVols_Type = Gauge32
_WfFsVols_Object = MibScalar
wfFsVols = _WfFsVols_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 1, 2),
    _WfFsVols_Type()
)
wfFsVols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsVols.setStatus("mandatory")
_WfFsVolTable_Object = MibTable
wfFsVolTable = _WfFsVolTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2)
)
if mibBuilder.loadTexts:
    wfFsVolTable.setStatus("mandatory")
_WfFsVolEntry_Object = MibTableRow
wfFsVolEntry = _WfFsVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1)
)
wfFsVolEntry.setIndexNames(
    (0, "Wellfleet-FSM-MIB", "wfFsVolID"),
)
if mibBuilder.loadTexts:
    wfFsVolEntry.setStatus("mandatory")
_WfFsVolID_Type = Integer32
_WfFsVolID_Object = MibTableColumn
wfFsVolID = _WfFsVolID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 1),
    _WfFsVolID_Type()
)
wfFsVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsVolID.setStatus("mandatory")
_WfFsSlot_Type = Integer32
_WfFsSlot_Object = MibTableColumn
wfFsSlot = _WfFsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 2),
    _WfFsSlot_Type()
)
wfFsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsSlot.setStatus("mandatory")


class _WfFsType_Type(Integer32):
    """Custom type wfFsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dos", 1),
          ("nvfs", 2),
          ("unix", 3))
    )


_WfFsType_Type.__name__ = "Integer32"
_WfFsType_Object = MibTableColumn
wfFsType = _WfFsType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 3),
    _WfFsType_Type()
)
wfFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsType.setStatus("mandatory")


class _WfFsRemoveable_Type(Integer32):
    """Custom type wfFsRemoveable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("remove", 1))
    )


_WfFsRemoveable_Type.__name__ = "Integer32"
_WfFsRemoveable_Object = MibTableColumn
wfFsRemoveable = _WfFsRemoveable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 4),
    _WfFsRemoveable_Type()
)
wfFsRemoveable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsRemoveable.setStatus("mandatory")


class _WfFsAccess_Type(Integer32):
    """Custom type wfFsAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 2),
          ("readwrite", 3),
          ("unknown", 1))
    )


_WfFsAccess_Type.__name__ = "Integer32"
_WfFsAccess_Object = MibTableColumn
wfFsAccess = _WfFsAccess_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 5),
    _WfFsAccess_Type()
)
wfFsAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsAccess.setStatus("mandatory")


class _WfFsState_Type(Integer32):
    """Custom type wfFsState based on Integer32"""
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
        *(("busy", 3),
          ("corrupt", 2),
          ("incomplete", 5),
          ("ok", 1),
          ("present", 4))
    )


_WfFsState_Type.__name__ = "Integer32"
_WfFsState_Object = MibTableColumn
wfFsState = _WfFsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 6),
    _WfFsState_Type()
)
wfFsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsState.setStatus("mandatory")
_WfFsSize_Type = Gauge32
_WfFsSize_Object = MibTableColumn
wfFsSize = _WfFsSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 7),
    _WfFsSize_Type()
)
wfFsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsSize.setStatus("mandatory")
_WfFsFreeSize_Type = Gauge32
_WfFsFreeSize_Object = MibTableColumn
wfFsFreeSize = _WfFsFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 8),
    _WfFsFreeSize_Type()
)
wfFsFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsFreeSize.setStatus("mandatory")
_WfFsContigFree_Type = Gauge32
_WfFsContigFree_Object = MibTableColumn
wfFsContigFree = _WfFsContigFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 9),
    _WfFsContigFree_Type()
)
wfFsContigFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsContigFree.setStatus("mandatory")
_WfFsNumFiles_Type = Gauge32
_WfFsNumFiles_Object = MibTableColumn
wfFsNumFiles = _WfFsNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 10),
    _WfFsNumFiles_Type()
)
wfFsNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsNumFiles.setStatus("mandatory")
_WfFsLastWritten_Type = OctetString
_WfFsLastWritten_Object = MibTableColumn
wfFsLastWritten = _WfFsLastWritten_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 11),
    _WfFsLastWritten_Type()
)
wfFsLastWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsLastWritten.setStatus("mandatory")
_WfFsBecameActive_Type = OctetString
_WfFsBecameActive_Object = MibTableColumn
wfFsBecameActive = _WfFsBecameActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 12),
    _WfFsBecameActive_Type()
)
wfFsBecameActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsBecameActive.setStatus("mandatory")


class _WfFsAction_Type(Integer32):
    """Custom type wfFsAction based on Integer32"""
    defaultValue = 7

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
        *(("compact", 3),
          ("dir", 1),
          ("format", 2),
          ("noaction", 7),
          ("partcre", 5),
          ("partdel", 6),
          ("purge", 4))
    )


_WfFsAction_Type.__name__ = "Integer32"
_WfFsAction_Object = MibTableColumn
wfFsAction = _WfFsAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 13),
    _WfFsAction_Type()
)
wfFsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFsAction.setStatus("mandatory")
_WfFsActionArg_Type = ObjectIdentifier
_WfFsActionArg_Object = MibTableColumn
wfFsActionArg = _WfFsActionArg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 14),
    _WfFsActionArg_Type()
)
wfFsActionArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFsActionArg.setStatus("mandatory")
_WfFsPercentDone_Type = Integer32
_WfFsPercentDone_Object = MibTableColumn
wfFsPercentDone = _WfFsPercentDone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 2, 1, 15),
    _WfFsPercentDone_Type()
)
wfFsPercentDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsPercentDone.setStatus("mandatory")
_WfFsDirBase_ObjectIdentity = ObjectIdentity
wfFsDirBase = _WfFsDirBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3)
)
_WfFsDirEntries_Type = Gauge32
_WfFsDirEntries_Object = MibScalar
wfFsDirEntries = _WfFsDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3, 1),
    _WfFsDirEntries_Type()
)
wfFsDirEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirEntries.setStatus("mandatory")
_WfFsDirLastUpdated_Type = OctetString
_WfFsDirLastUpdated_Object = MibScalar
wfFsDirLastUpdated = _WfFsDirLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 3, 2),
    _WfFsDirLastUpdated_Type()
)
wfFsDirLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirLastUpdated.setStatus("mandatory")
_WfFsDirTable_Object = MibTable
wfFsDirTable = _WfFsDirTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5)
)
if mibBuilder.loadTexts:
    wfFsDirTable.setStatus("mandatory")
_WfFsDirEntry_Object = MibTableRow
wfFsDirEntry = _WfFsDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1)
)
wfFsDirEntry.setIndexNames(
    (0, "Wellfleet-FSM-MIB", "wfFsDirVolID"),
    (0, "Wellfleet-FSM-MIB", "wfFsDirFileIndex"),
)
if mibBuilder.loadTexts:
    wfFsDirEntry.setStatus("mandatory")
_WfFsDirVolID_Type = Integer32
_WfFsDirVolID_Object = MibTableColumn
wfFsDirVolID = _WfFsDirVolID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 1),
    _WfFsDirVolID_Type()
)
wfFsDirVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirVolID.setStatus("mandatory")
_WfFsDirFileIndex_Type = ObjectIdentifier
_WfFsDirFileIndex_Object = MibTableColumn
wfFsDirFileIndex = _WfFsDirFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 2),
    _WfFsDirFileIndex_Type()
)
wfFsDirFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirFileIndex.setStatus("mandatory")
_WfFsDirFileName_Type = DisplayString
_WfFsDirFileName_Object = MibTableColumn
wfFsDirFileName = _WfFsDirFileName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 3),
    _WfFsDirFileName_Type()
)
wfFsDirFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirFileName.setStatus("mandatory")
_WfFsDirCreated_Type = OctetString
_WfFsDirCreated_Object = MibTableColumn
wfFsDirCreated = _WfFsDirCreated_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 4),
    _WfFsDirCreated_Type()
)
wfFsDirCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirCreated.setStatus("mandatory")
_WfFsDirFileSize_Type = Gauge32
_WfFsDirFileSize_Object = MibTableColumn
wfFsDirFileSize = _WfFsDirFileSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 5),
    _WfFsDirFileSize_Type()
)
wfFsDirFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirFileSize.setStatus("mandatory")
_WfFsDirFileMask_Type = Gauge32
_WfFsDirFileMask_Object = MibTableColumn
wfFsDirFileMask = _WfFsDirFileMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12, 5, 1, 6),
    _WfFsDirFileMask_Type()
)
wfFsDirFileMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFsDirFileMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FSM-MIB",
    **{"wfFsBase": wfFsBase,
       "wfFsVolLastUpdated": wfFsVolLastUpdated,
       "wfFsVols": wfFsVols,
       "wfFsVolTable": wfFsVolTable,
       "wfFsVolEntry": wfFsVolEntry,
       "wfFsVolID": wfFsVolID,
       "wfFsSlot": wfFsSlot,
       "wfFsType": wfFsType,
       "wfFsRemoveable": wfFsRemoveable,
       "wfFsAccess": wfFsAccess,
       "wfFsState": wfFsState,
       "wfFsSize": wfFsSize,
       "wfFsFreeSize": wfFsFreeSize,
       "wfFsContigFree": wfFsContigFree,
       "wfFsNumFiles": wfFsNumFiles,
       "wfFsLastWritten": wfFsLastWritten,
       "wfFsBecameActive": wfFsBecameActive,
       "wfFsAction": wfFsAction,
       "wfFsActionArg": wfFsActionArg,
       "wfFsPercentDone": wfFsPercentDone,
       "wfFsDirBase": wfFsDirBase,
       "wfFsDirEntries": wfFsDirEntries,
       "wfFsDirLastUpdated": wfFsDirLastUpdated,
       "wfFsDirTable": wfFsDirTable,
       "wfFsDirEntry": wfFsDirEntry,
       "wfFsDirVolID": wfFsDirVolID,
       "wfFsDirFileIndex": wfFsDirFileIndex,
       "wfFsDirFileName": wfFsDirFileName,
       "wfFsDirCreated": wfFsDirCreated,
       "wfFsDirFileSize": wfFsDirFileSize,
       "wfFsDirFileMask": wfFsDirFileMask}
)
