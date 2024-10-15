# SNMP MIB module (SONUS-EVENT-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-EVENT-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:56 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex")

(sonusSystemMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSystemMIBs")

(SonusEventClass,
 SonusEventFilterLevel,
 SonusEventString,
 SonusShelfIndex,
 SonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusEventClass",
    "SonusEventFilterLevel",
    "SonusEventString",
    "SonusShelfIndex",
    "SonusSlotIndex")


# MODULE-IDENTITY

sonusEventLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusEventLogMIBObjects_ObjectIdentity = ObjectIdentity
sonusEventLogMIBObjects = _SonusEventLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1)
)
_SonusEvLogTypeTable_Object = MibTable
sonusEvLogTypeTable = _SonusEvLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonusEvLogTypeTable.setStatus("current")
_SonusEvLogTypeEntry_Object = MibTableRow
sonusEvLogTypeEntry = _SonusEvLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1)
)
sonusEvLogTypeEntry.setIndexNames(
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
)
if mibBuilder.loadTexts:
    sonusEvLogTypeEntry.setStatus("current")


class _SonusEvLogType_Type(Integer32):
    """Custom type sonusEvLogType based on Integer32"""
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
        *(("acct", 4),
          ("debug", 2),
          ("system", 1),
          ("trace", 3))
    )


_SonusEvLogType_Type.__name__ = "Integer32"
_SonusEvLogType_Object = MibTableColumn
sonusEvLogType = _SonusEvLogType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 1),
    _SonusEvLogType_Type()
)
sonusEvLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogType.setStatus("current")


class _SonusEvLogTypeAdminState_Type(Integer32):
    """Custom type sonusEvLogTypeAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("rollfile", 3))
    )


_SonusEvLogTypeAdminState_Type.__name__ = "Integer32"
_SonusEvLogTypeAdminState_Object = MibTableColumn
sonusEvLogTypeAdminState = _SonusEvLogTypeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 2),
    _SonusEvLogTypeAdminState_Type()
)
sonusEvLogTypeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeAdminState.setStatus("current")


class _SonusEvLogTypeFileCount_Type(Integer32):
    """Custom type sonusEvLogTypeFileCount based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SonusEvLogTypeFileCount_Type.__name__ = "Integer32"
_SonusEvLogTypeFileCount_Object = MibTableColumn
sonusEvLogTypeFileCount = _SonusEvLogTypeFileCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 3),
    _SonusEvLogTypeFileCount_Type()
)
sonusEvLogTypeFileCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeFileCount.setStatus("current")


class _SonusEvLogTypeFileSize_Type(Integer32):
    """Custom type sonusEvLogTypeFileSize based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_SonusEvLogTypeFileSize_Type.__name__ = "Integer32"
_SonusEvLogTypeFileSize_Object = MibTableColumn
sonusEvLogTypeFileSize = _SonusEvLogTypeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 4),
    _SonusEvLogTypeFileSize_Type()
)
sonusEvLogTypeFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeFileSize.setStatus("current")


class _SonusEvLogTypeFileMsgQueue_Type(Integer32):
    """Custom type sonusEvLogTypeFileMsgQueue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_SonusEvLogTypeFileMsgQueue_Type.__name__ = "Integer32"
_SonusEvLogTypeFileMsgQueue_Object = MibTableColumn
sonusEvLogTypeFileMsgQueue = _SonusEvLogTypeFileMsgQueue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 5),
    _SonusEvLogTypeFileMsgQueue_Type()
)
sonusEvLogTypeFileMsgQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeFileMsgQueue.setStatus("current")
_SonusEvLogTypeBaseDirectory_Type = DisplayString
_SonusEvLogTypeBaseDirectory_Object = MibTableColumn
sonusEvLogTypeBaseDirectory = _SonusEvLogTypeBaseDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 6),
    _SonusEvLogTypeBaseDirectory_Type()
)
sonusEvLogTypeBaseDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeBaseDirectory.setStatus("current")


class _SonusEvLogTypeSaveTo_Type(Integer32):
    """Custom type sonusEvLogTypeSaveTo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("disk", 1),
          ("memory", 2),
          ("none", 0))
    )


_SonusEvLogTypeSaveTo_Type.__name__ = "Integer32"
_SonusEvLogTypeSaveTo_Object = MibTableColumn
sonusEvLogTypeSaveTo = _SonusEvLogTypeSaveTo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 7),
    _SonusEvLogTypeSaveTo_Type()
)
sonusEvLogTypeSaveTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeSaveTo.setStatus("current")


class _SonusEvLogTypeMaxEventMemSize_Type(Integer32):
    """Custom type sonusEvLogTypeMaxEventMemSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SonusEvLogTypeMaxEventMemSize_Type.__name__ = "Integer32"
_SonusEvLogTypeMaxEventMemSize_Object = MibTableColumn
sonusEvLogTypeMaxEventMemSize = _SonusEvLogTypeMaxEventMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 8),
    _SonusEvLogTypeMaxEventMemSize_Type()
)
sonusEvLogTypeMaxEventMemSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeMaxEventMemSize.setStatus("current")


class _SonusEvLogTypeFilterLevel_Type(SonusEventFilterLevel):
    """Custom type sonusEvLogTypeFilterLevel based on SonusEventFilterLevel"""


_SonusEvLogTypeFilterLevel_Object = MibTableColumn
sonusEvLogTypeFilterLevel = _SonusEvLogTypeFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 1, 1, 9),
    _SonusEvLogTypeFilterLevel_Type()
)
sonusEvLogTypeFilterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogTypeFilterLevel.setStatus("current")
_SonusEvLogTypeStatusTable_Object = MibTable
sonusEvLogTypeStatusTable = _SonusEvLogTypeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusTable.setStatus("current")
_SonusEvLogTypeStatusEntry_Object = MibTableRow
sonusEvLogTypeStatusEntry = _SonusEvLogTypeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1)
)
sonusEvLogTypeStatusEntry.setIndexNames(
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusShelf"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusType"),
)
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusEntry.setStatus("current")
_SonusEvLogTypeStatusShelf_Type = Integer32
_SonusEvLogTypeStatusShelf_Object = MibTableColumn
sonusEvLogTypeStatusShelf = _SonusEvLogTypeStatusShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 1),
    _SonusEvLogTypeStatusShelf_Type()
)
sonusEvLogTypeStatusShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusShelf.setStatus("current")


class _SonusEvLogTypeStatusType_Type(Integer32):
    """Custom type sonusEvLogTypeStatusType based on Integer32"""
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
        *(("acct", 4),
          ("debug", 2),
          ("system", 1),
          ("trace", 3))
    )


_SonusEvLogTypeStatusType_Type.__name__ = "Integer32"
_SonusEvLogTypeStatusType_Object = MibTableColumn
sonusEvLogTypeStatusType = _SonusEvLogTypeStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 2),
    _SonusEvLogTypeStatusType_Type()
)
sonusEvLogTypeStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusType.setStatus("current")
_SonusEvLogTypeStatusCurrentFile_Type = DisplayString
_SonusEvLogTypeStatusCurrentFile_Object = MibTableColumn
sonusEvLogTypeStatusCurrentFile = _SonusEvLogTypeStatusCurrentFile_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 3),
    _SonusEvLogTypeStatusCurrentFile_Type()
)
sonusEvLogTypeStatusCurrentFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusCurrentFile.setStatus("current")
_SonusEvLogTypeStatusFileRecs_Type = Integer32
_SonusEvLogTypeStatusFileRecs_Object = MibTableColumn
sonusEvLogTypeStatusFileRecs = _SonusEvLogTypeStatusFileRecs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 4),
    _SonusEvLogTypeStatusFileRecs_Type()
)
sonusEvLogTypeStatusFileRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusFileRecs.setStatus("current")
_SonusEvLogTypeStatusFileBytes_Type = Integer32
_SonusEvLogTypeStatusFileBytes_Object = MibTableColumn
sonusEvLogTypeStatusFileBytes = _SonusEvLogTypeStatusFileBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 5),
    _SonusEvLogTypeStatusFileBytes_Type()
)
sonusEvLogTypeStatusFileBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusFileBytes.setStatus("current")
_SonusEvLogTypeStatusMemRecs_Type = Integer32
_SonusEvLogTypeStatusMemRecs_Object = MibTableColumn
sonusEvLogTypeStatusMemRecs = _SonusEvLogTypeStatusMemRecs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 6),
    _SonusEvLogTypeStatusMemRecs_Type()
)
sonusEvLogTypeStatusMemRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusMemRecs.setStatus("current")
_SonusEvLogTypeStatusMemBytes_Type = Integer32
_SonusEvLogTypeStatusMemBytes_Object = MibTableColumn
sonusEvLogTypeStatusMemBytes = _SonusEvLogTypeStatusMemBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 7),
    _SonusEvLogTypeStatusMemBytes_Type()
)
sonusEvLogTypeStatusMemBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusMemBytes.setStatus("current")
_SonusEvLogTypeStatusFileDropped_Type = Integer32
_SonusEvLogTypeStatusFileDropped_Object = MibTableColumn
sonusEvLogTypeStatusFileDropped = _SonusEvLogTypeStatusFileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 8),
    _SonusEvLogTypeStatusFileDropped_Type()
)
sonusEvLogTypeStatusFileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusFileDropped.setStatus("current")
_SonusEvLogTypeStatusMemDropped_Type = Integer32
_SonusEvLogTypeStatusMemDropped_Object = MibTableColumn
sonusEvLogTypeStatusMemDropped = _SonusEvLogTypeStatusMemDropped_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 2, 1, 9),
    _SonusEvLogTypeStatusMemDropped_Type()
)
sonusEvLogTypeStatusMemDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogTypeStatusMemDropped.setStatus("current")
_SonusEvLogMemTable_Object = MibTable
sonusEvLogMemTable = _SonusEvLogMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sonusEvLogMemTable.setStatus("current")
_SonusEvLogMemEntry_Object = MibTableRow
sonusEvLogMemEntry = _SonusEvLogMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3, 1)
)
sonusEvLogMemEntry.setIndexNames(
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogMemShelf"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogMemType"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogMemIndex"),
)
if mibBuilder.loadTexts:
    sonusEvLogMemEntry.setStatus("current")
_SonusEvLogMemShelf_Type = Integer32
_SonusEvLogMemShelf_Object = MibTableColumn
sonusEvLogMemShelf = _SonusEvLogMemShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3, 1, 1),
    _SonusEvLogMemShelf_Type()
)
sonusEvLogMemShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogMemShelf.setStatus("current")


class _SonusEvLogMemType_Type(Integer32):
    """Custom type sonusEvLogMemType based on Integer32"""
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
        *(("acct", 4),
          ("debug", 2),
          ("system", 1),
          ("trace", 3))
    )


_SonusEvLogMemType_Type.__name__ = "Integer32"
_SonusEvLogMemType_Object = MibTableColumn
sonusEvLogMemType = _SonusEvLogMemType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3, 1, 2),
    _SonusEvLogMemType_Type()
)
sonusEvLogMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogMemType.setStatus("current")
_SonusEvLogMemIndex_Type = Integer32
_SonusEvLogMemIndex_Object = MibTableColumn
sonusEvLogMemIndex = _SonusEvLogMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3, 1, 3),
    _SonusEvLogMemIndex_Type()
)
sonusEvLogMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogMemIndex.setStatus("current")
_SonusEvLogMemText_Type = SonusEventString
_SonusEvLogMemText_Object = MibTableColumn
sonusEvLogMemText = _SonusEvLogMemText_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 3, 1, 4),
    _SonusEvLogMemText_Type()
)
sonusEvLogMemText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogMemText.setStatus("current")
_SonusEvLogFilterTable_Object = MibTable
sonusEvLogFilterTable = _SonusEvLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    sonusEvLogFilterTable.setStatus("current")
_SonusEvLogFilterEntry_Object = MibTableRow
sonusEvLogFilterEntry = _SonusEvLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1)
)
sonusEvLogFilterEntry.setIndexNames(
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterShelf"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterSlot"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterType"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterEventClass"),
)
if mibBuilder.loadTexts:
    sonusEvLogFilterEntry.setStatus("current")
_SonusEvLogFilterShelf_Type = SonusShelfIndex
_SonusEvLogFilterShelf_Object = MibTableColumn
sonusEvLogFilterShelf = _SonusEvLogFilterShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 1),
    _SonusEvLogFilterShelf_Type()
)
sonusEvLogFilterShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterShelf.setStatus("current")
_SonusEvLogFilterSlot_Type = SonusSlotIndex
_SonusEvLogFilterSlot_Object = MibTableColumn
sonusEvLogFilterSlot = _SonusEvLogFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 2),
    _SonusEvLogFilterSlot_Type()
)
sonusEvLogFilterSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterSlot.setStatus("current")


class _SonusEvLogFilterType_Type(Integer32):
    """Custom type sonusEvLogFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("debug", 2),
          ("system", 1),
          ("trace", 3))
    )


_SonusEvLogFilterType_Type.__name__ = "Integer32"
_SonusEvLogFilterType_Object = MibTableColumn
sonusEvLogFilterType = _SonusEvLogFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 3),
    _SonusEvLogFilterType_Type()
)
sonusEvLogFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterType.setStatus("current")
_SonusEvLogFilterEventClass_Type = SonusEventClass
_SonusEvLogFilterEventClass_Object = MibTableColumn
sonusEvLogFilterEventClass = _SonusEvLogFilterEventClass_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 4),
    _SonusEvLogFilterEventClass_Type()
)
sonusEvLogFilterEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterEventClass.setStatus("current")


class _SonusEvLogFilterLevel_Type(SonusEventFilterLevel):
    """Custom type sonusEvLogFilterLevel based on SonusEventFilterLevel"""


_SonusEvLogFilterLevel_Object = MibTableColumn
sonusEvLogFilterLevel = _SonusEvLogFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 5),
    _SonusEvLogFilterLevel_Type()
)
sonusEvLogFilterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterLevel.setStatus("current")


class _SonusEvLogFilterState_Type(Integer32):
    """Custom type sonusEvLogFilterState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SonusEvLogFilterState_Type.__name__ = "Integer32"
_SonusEvLogFilterState_Object = MibTableColumn
sonusEvLogFilterState = _SonusEvLogFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 6, 1, 6),
    _SonusEvLogFilterState_Type()
)
sonusEvLogFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusEvLogFilterState.setStatus("current")
_SonusEvLogFilterStatusTable_Object = MibTable
sonusEvLogFilterStatusTable = _SonusEvLogFilterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusTable.setStatus("current")
_SonusEvLogFilterStatusEntry_Object = MibTableRow
sonusEvLogFilterStatusEntry = _SonusEvLogFilterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1)
)
sonusEvLogFilterStatusEntry.setIndexNames(
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterStatusShelf"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterStatusSlot"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterStatusType"),
    (0, "SONUS-EVENT-LOG-MIB", "sonusEvLogFilterStatusEventClass"),
)
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusEntry.setStatus("current")
_SonusEvLogFilterStatusShelf_Type = Integer32
_SonusEvLogFilterStatusShelf_Object = MibTableColumn
sonusEvLogFilterStatusShelf = _SonusEvLogFilterStatusShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1, 1),
    _SonusEvLogFilterStatusShelf_Type()
)
sonusEvLogFilterStatusShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusShelf.setStatus("current")
_SonusEvLogFilterStatusSlot_Type = Integer32
_SonusEvLogFilterStatusSlot_Object = MibTableColumn
sonusEvLogFilterStatusSlot = _SonusEvLogFilterStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1, 2),
    _SonusEvLogFilterStatusSlot_Type()
)
sonusEvLogFilterStatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusSlot.setStatus("current")


class _SonusEvLogFilterStatusType_Type(Integer32):
    """Custom type sonusEvLogFilterStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("debug", 2),
          ("system", 1),
          ("trace", 3))
    )


_SonusEvLogFilterStatusType_Type.__name__ = "Integer32"
_SonusEvLogFilterStatusType_Object = MibTableColumn
sonusEvLogFilterStatusType = _SonusEvLogFilterStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1, 3),
    _SonusEvLogFilterStatusType_Type()
)
sonusEvLogFilterStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusType.setStatus("current")
_SonusEvLogFilterStatusEventClass_Type = SonusEventClass
_SonusEvLogFilterStatusEventClass_Object = MibTableColumn
sonusEvLogFilterStatusEventClass = _SonusEvLogFilterStatusEventClass_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1, 4),
    _SonusEvLogFilterStatusEventClass_Type()
)
sonusEvLogFilterStatusEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusEventClass.setStatus("current")
_SonusEvLogFilterStatusFiltered_Type = Integer32
_SonusEvLogFilterStatusFiltered_Object = MibTableColumn
sonusEvLogFilterStatusFiltered = _SonusEvLogFilterStatusFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 1, 7, 1, 5),
    _SonusEvLogFilterStatusFiltered_Type()
)
sonusEvLogFilterStatusFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilterStatusFiltered.setStatus("current")
_SonusEventLogMIBNotifications_ObjectIdentity = ObjectIdentity
sonusEventLogMIBNotifications = _SonusEventLogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2)
)
_SonusEventLogMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusEventLogMIBNotificationsPrefix = _SonusEventLogMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0)
)
_SonusEventLogMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusEventLogMIBNotificationsObjects = _SonusEventLogMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1)
)


class _SonusEvLogAdminState_Type(Integer32):
    """Custom type sonusEvLogAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("rollfile", 3))
    )


_SonusEvLogAdminState_Type.__name__ = "Integer32"
_SonusEvLogAdminState_Object = MibScalar
sonusEvLogAdminState = _SonusEvLogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1, 1),
    _SonusEvLogAdminState_Type()
)
sonusEvLogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogAdminState.setStatus("current")


class _SonusEvLogShutdownReason_Type(Integer32):
    """Custom type sonusEvLogShutdownReason based on Integer32"""
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
        *(("administrativeShutdown", 9),
          ("createDirectoryFailed", 3),
          ("fileHeaderWriteFailed", 7),
          ("fileOpenFailed", 6),
          ("fileRemoveFailed", 5),
          ("fileWriteFailed", 1),
          ("maximumFileCountReached", 4),
          ("memoryAllocationFailed", 8),
          ("nfsError", 2))
    )


_SonusEvLogShutdownReason_Type.__name__ = "Integer32"
_SonusEvLogShutdownReason_Object = MibScalar
sonusEvLogShutdownReason = _SonusEvLogShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1, 2),
    _SonusEvLogShutdownReason_Type()
)
sonusEvLogShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogShutdownReason.setStatus("current")
_SonusEvLogDirName_Type = DisplayString
_SonusEvLogDirName_Object = MibScalar
sonusEvLogDirName = _SonusEvLogDirName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1, 3),
    _SonusEvLogDirName_Type()
)
sonusEvLogDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogDirName.setStatus("current")
_SonusEvLogFilePercentage_Type = Integer32
_SonusEvLogFilePercentage_Object = MibScalar
sonusEvLogFilePercentage = _SonusEvLogFilePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1, 4),
    _SonusEvLogFilePercentage_Type()
)
sonusEvLogFilePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogFilePercentage.setStatus("current")
_SonusEvLogCurFileCount_Type = Integer32
_SonusEvLogCurFileCount_Object = MibScalar
sonusEvLogCurFileCount = _SonusEvLogCurFileCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 1, 5),
    _SonusEvLogCurFileCount_Type()
)
sonusEvLogCurFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEvLogCurFileCount.setStatus("current")

# Managed Objects groups


# Notification objects

sonusEventLogFileStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 1)
)
sonusEventLogFileStateNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogAdminState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileStateNotification.setStatus(
        "current"
    )

sonusEventLogFileCreatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 2)
)
sonusEventLogFileCreatedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusCurrentFile"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileCreatedNotification.setStatus(
        "current"
    )

sonusEventLogAcctFileCreatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 3)
)
sonusEventLogAcctFileCreatedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusCurrentFile"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogAcctFileCreatedNotification.setStatus(
        "current"
    )

sonusEventLogFileRestartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 4)
)
sonusEventLogFileRestartNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileRestartNotification.setStatus(
        "current"
    )

sonusEventLogAcctFileRestartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 5)
)
sonusEventLogAcctFileRestartNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogAcctFileRestartNotification.setStatus(
        "current"
    )

sonusEventLogFileClosedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 6)
)
sonusEventLogFileClosedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusCurrentFile"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileClosedNotification.setStatus(
        "current"
    )

sonusEventLogAcctFileClosedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 7)
)
sonusEventLogAcctFileClosedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeStatusCurrentFile"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogAcctFileClosedNotification.setStatus(
        "current"
    )

sonusEventLogFileShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 8)
)
sonusEventLogFileShutdownNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogShutdownReason"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogAdminState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileShutdownNotification.setStatus(
        "current"
    )

sonusEventLogFileCountNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 9)
)
sonusEventLogFileCountNotification.setObjects(
      *(("SONUS-EVENT-LOG-MIB", "sonusEvLogDirName"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogFilePercentage"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogCurFileCount"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeFileCount"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileCountNotification.setStatus(
        "current"
    )

sonusEventLogFileCountChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 10)
)
sonusEventLogFileCountChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeFileCount"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileCountChngNotification.setStatus(
        "current"
    )

sonusEventLogFileSizeChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 11)
)
sonusEventLogFileSizeChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeFileSize"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileSizeChngNotification.setStatus(
        "current"
    )

sonusEventLogFileMsgQueueChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 12)
)
sonusEventLogFileMsgQueueChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeFileMsgQueue"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileMsgQueueChngNotification.setStatus(
        "current"
    )

sonusEventLogSaveToChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 13)
)
sonusEventLogSaveToChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeSaveTo"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogSaveToChngNotification.setStatus(
        "current"
    )

sonusEventLogFileMaxEventMemSizeChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 14)
)
sonusEventLogFileMaxEventMemSizeChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeMaxEventMemSize"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileMaxEventMemSizeChngNotification.setStatus(
        "current"
    )

sonusEventLogFileFilterLevelChngNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 2, 2, 0, 15)
)
sonusEventLogFileFilterLevelChngNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogType"),
        ("SONUS-EVENT-LOG-MIB", "sonusEvLogTypeFilterLevel"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusEventLogFileFilterLevelChngNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-EVENT-LOG-MIB",
    **{"sonusEventLogMIB": sonusEventLogMIB,
       "sonusEventLogMIBObjects": sonusEventLogMIBObjects,
       "sonusEvLogTypeTable": sonusEvLogTypeTable,
       "sonusEvLogTypeEntry": sonusEvLogTypeEntry,
       "sonusEvLogType": sonusEvLogType,
       "sonusEvLogTypeAdminState": sonusEvLogTypeAdminState,
       "sonusEvLogTypeFileCount": sonusEvLogTypeFileCount,
       "sonusEvLogTypeFileSize": sonusEvLogTypeFileSize,
       "sonusEvLogTypeFileMsgQueue": sonusEvLogTypeFileMsgQueue,
       "sonusEvLogTypeBaseDirectory": sonusEvLogTypeBaseDirectory,
       "sonusEvLogTypeSaveTo": sonusEvLogTypeSaveTo,
       "sonusEvLogTypeMaxEventMemSize": sonusEvLogTypeMaxEventMemSize,
       "sonusEvLogTypeFilterLevel": sonusEvLogTypeFilterLevel,
       "sonusEvLogTypeStatusTable": sonusEvLogTypeStatusTable,
       "sonusEvLogTypeStatusEntry": sonusEvLogTypeStatusEntry,
       "sonusEvLogTypeStatusShelf": sonusEvLogTypeStatusShelf,
       "sonusEvLogTypeStatusType": sonusEvLogTypeStatusType,
       "sonusEvLogTypeStatusCurrentFile": sonusEvLogTypeStatusCurrentFile,
       "sonusEvLogTypeStatusFileRecs": sonusEvLogTypeStatusFileRecs,
       "sonusEvLogTypeStatusFileBytes": sonusEvLogTypeStatusFileBytes,
       "sonusEvLogTypeStatusMemRecs": sonusEvLogTypeStatusMemRecs,
       "sonusEvLogTypeStatusMemBytes": sonusEvLogTypeStatusMemBytes,
       "sonusEvLogTypeStatusFileDropped": sonusEvLogTypeStatusFileDropped,
       "sonusEvLogTypeStatusMemDropped": sonusEvLogTypeStatusMemDropped,
       "sonusEvLogMemTable": sonusEvLogMemTable,
       "sonusEvLogMemEntry": sonusEvLogMemEntry,
       "sonusEvLogMemShelf": sonusEvLogMemShelf,
       "sonusEvLogMemType": sonusEvLogMemType,
       "sonusEvLogMemIndex": sonusEvLogMemIndex,
       "sonusEvLogMemText": sonusEvLogMemText,
       "sonusEvLogFilterTable": sonusEvLogFilterTable,
       "sonusEvLogFilterEntry": sonusEvLogFilterEntry,
       "sonusEvLogFilterShelf": sonusEvLogFilterShelf,
       "sonusEvLogFilterSlot": sonusEvLogFilterSlot,
       "sonusEvLogFilterType": sonusEvLogFilterType,
       "sonusEvLogFilterEventClass": sonusEvLogFilterEventClass,
       "sonusEvLogFilterLevel": sonusEvLogFilterLevel,
       "sonusEvLogFilterState": sonusEvLogFilterState,
       "sonusEvLogFilterStatusTable": sonusEvLogFilterStatusTable,
       "sonusEvLogFilterStatusEntry": sonusEvLogFilterStatusEntry,
       "sonusEvLogFilterStatusShelf": sonusEvLogFilterStatusShelf,
       "sonusEvLogFilterStatusSlot": sonusEvLogFilterStatusSlot,
       "sonusEvLogFilterStatusType": sonusEvLogFilterStatusType,
       "sonusEvLogFilterStatusEventClass": sonusEvLogFilterStatusEventClass,
       "sonusEvLogFilterStatusFiltered": sonusEvLogFilterStatusFiltered,
       "sonusEventLogMIBNotifications": sonusEventLogMIBNotifications,
       "sonusEventLogMIBNotificationsPrefix": sonusEventLogMIBNotificationsPrefix,
       "sonusEventLogFileStateNotification": sonusEventLogFileStateNotification,
       "sonusEventLogFileCreatedNotification": sonusEventLogFileCreatedNotification,
       "sonusEventLogAcctFileCreatedNotification": sonusEventLogAcctFileCreatedNotification,
       "sonusEventLogFileRestartNotification": sonusEventLogFileRestartNotification,
       "sonusEventLogAcctFileRestartNotification": sonusEventLogAcctFileRestartNotification,
       "sonusEventLogFileClosedNotification": sonusEventLogFileClosedNotification,
       "sonusEventLogAcctFileClosedNotification": sonusEventLogAcctFileClosedNotification,
       "sonusEventLogFileShutdownNotification": sonusEventLogFileShutdownNotification,
       "sonusEventLogFileCountNotification": sonusEventLogFileCountNotification,
       "sonusEventLogFileCountChngNotification": sonusEventLogFileCountChngNotification,
       "sonusEventLogFileSizeChngNotification": sonusEventLogFileSizeChngNotification,
       "sonusEventLogFileMsgQueueChngNotification": sonusEventLogFileMsgQueueChngNotification,
       "sonusEventLogSaveToChngNotification": sonusEventLogSaveToChngNotification,
       "sonusEventLogFileMaxEventMemSizeChngNotification": sonusEventLogFileMaxEventMemSizeChngNotification,
       "sonusEventLogFileFilterLevelChngNotification": sonusEventLogFileFilterLevelChngNotification,
       "sonusEventLogMIBNotificationsObjects": sonusEventLogMIBNotificationsObjects,
       "sonusEvLogAdminState": sonusEvLogAdminState,
       "sonusEvLogShutdownReason": sonusEvLogShutdownReason,
       "sonusEvLogDirName": sonusEvLogDirName,
       "sonusEvLogFilePercentage": sonusEvLogFilePercentage,
       "sonusEvLogCurFileCount": sonusEvLogCurFileCount}
)
