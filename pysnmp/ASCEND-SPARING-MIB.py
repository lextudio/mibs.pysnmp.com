# SNMP MIB module (ASCEND-SPARING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-SPARING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:42 2024
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

(sparingGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "sparingGroup")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SparingGlobalGroup_ObjectIdentity = ObjectIdentity
sparingGlobalGroup = _SparingGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 30, 1)
)
_SparingSlotGroup_ObjectIdentity = ObjectIdentity
sparingSlotGroup = _SparingSlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 30, 2)
)


class _SparingSlotMode_Type(Integer32):
    """Custom type sparingSlotMode based on Integer32"""
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
        *(("automatic", 4),
          ("disable", 2),
          ("manual", 3),
          ("unknown", 1))
    )


_SparingSlotMode_Type.__name__ = "Integer32"
_SparingSlotMode_Object = MibScalar
sparingSlotMode = _SparingSlotMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 1),
    _SparingSlotMode_Type()
)
sparingSlotMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotMode.setStatus("mandatory")
_SparingSlotTable_Object = MibTable
sparingSlotTable = _SparingSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2)
)
if mibBuilder.loadTexts:
    sparingSlotTable.setStatus("mandatory")
_SparingSlotEntry_Object = MibTableRow
sparingSlotEntry = _SparingSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1)
)
sparingSlotEntry.setIndexNames(
    (0, "ASCEND-SPARING-MIB", "sparingSlotPrimaryIndex"),
    (0, "ASCEND-SPARING-MIB", "sparingSlotSparingIndex"),
)
if mibBuilder.loadTexts:
    sparingSlotEntry.setStatus("mandatory")
_SparingSlotPrimaryIndex_Type = Integer32
_SparingSlotPrimaryIndex_Object = MibTableColumn
sparingSlotPrimaryIndex = _SparingSlotPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 1),
    _SparingSlotPrimaryIndex_Type()
)
sparingSlotPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotPrimaryIndex.setStatus("mandatory")
_SparingSlotSparingIndex_Type = Integer32
_SparingSlotSparingIndex_Object = MibTableColumn
sparingSlotSparingIndex = _SparingSlotSparingIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 2),
    _SparingSlotSparingIndex_Type()
)
sparingSlotSparingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotSparingIndex.setStatus("mandatory")


class _SparingSlotStatus_Type(Integer32):
    """Custom type sparingSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("fault", 2),
          ("standby", 1))
    )


_SparingSlotStatus_Type.__name__ = "Integer32"
_SparingSlotStatus_Object = MibTableColumn
sparingSlotStatus = _SparingSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 3),
    _SparingSlotStatus_Type()
)
sparingSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotStatus.setStatus("mandatory")
_SparingSlotLastStatusChange_Type = TimeTicks
_SparingSlotLastStatusChange_Object = MibTableColumn
sparingSlotLastStatusChange = _SparingSlotLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 4),
    _SparingSlotLastStatusChange_Type()
)
sparingSlotLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotLastStatusChange.setStatus("mandatory")


class _SparingSlotLastChangeReason_Type(Integer32):
    """Custom type sparingSlotLastChangeReason based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 2),
          ("test", 4),
          ("unknown", 1))
    )


_SparingSlotLastChangeReason_Type.__name__ = "Integer32"
_SparingSlotLastChangeReason_Object = MibTableColumn
sparingSlotLastChangeReason = _SparingSlotLastChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 5),
    _SparingSlotLastChangeReason_Type()
)
sparingSlotLastChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotLastChangeReason.setStatus("mandatory")
_SparingSlotStatusChangeCount_Type = Counter32
_SparingSlotStatusChangeCount_Object = MibTableColumn
sparingSlotStatusChangeCount = _SparingSlotStatusChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 6),
    _SparingSlotStatusChangeCount_Type()
)
sparingSlotStatusChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingSlotStatusChangeCount.setStatus("mandatory")
_SparingIfGroup_ObjectIdentity = ObjectIdentity
sparingIfGroup = _SparingIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 30, 3)
)
_SparingIfTable_Object = MibTable
sparingIfTable = _SparingIfTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2)
)
if mibBuilder.loadTexts:
    sparingIfTable.setStatus("mandatory")
_SparingIfEntry_Object = MibTableRow
sparingIfEntry = _SparingIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1)
)
sparingIfEntry.setIndexNames(
    (0, "ASCEND-SPARING-MIB", "sparingIfPrimaryIndex"),
    (0, "ASCEND-SPARING-MIB", "sparingIfSparingIndex"),
)
if mibBuilder.loadTexts:
    sparingIfEntry.setStatus("mandatory")
_SparingIfPrimaryIndex_Type = Integer32
_SparingIfPrimaryIndex_Object = MibTableColumn
sparingIfPrimaryIndex = _SparingIfPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 1),
    _SparingIfPrimaryIndex_Type()
)
sparingIfPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfPrimaryIndex.setStatus("mandatory")
_SparingIfSparingIndex_Type = Integer32
_SparingIfSparingIndex_Object = MibTableColumn
sparingIfSparingIndex = _SparingIfSparingIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 2),
    _SparingIfSparingIndex_Type()
)
sparingIfSparingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfSparingIndex.setStatus("mandatory")


class _SparingIfStatus_Type(Integer32):
    """Custom type sparingIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("fault", 2),
          ("standby", 1))
    )


_SparingIfStatus_Type.__name__ = "Integer32"
_SparingIfStatus_Object = MibTableColumn
sparingIfStatus = _SparingIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 3),
    _SparingIfStatus_Type()
)
sparingIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfStatus.setStatus("mandatory")
_SparingIfLastStatusChange_Type = TimeTicks
_SparingIfLastStatusChange_Object = MibTableColumn
sparingIfLastStatusChange = _SparingIfLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 4),
    _SparingIfLastStatusChange_Type()
)
sparingIfLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfLastStatusChange.setStatus("mandatory")


class _SparingIfLastChangeReason_Type(Integer32):
    """Custom type sparingIfLastChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("manual", 2),
          ("unknown", 1))
    )


_SparingIfLastChangeReason_Type.__name__ = "Integer32"
_SparingIfLastChangeReason_Object = MibTableColumn
sparingIfLastChangeReason = _SparingIfLastChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 5),
    _SparingIfLastChangeReason_Type()
)
sparingIfLastChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfLastChangeReason.setStatus("mandatory")
_SparingIfStatusChangeCount_Type = Counter32
_SparingIfStatusChangeCount_Object = MibTableColumn
sparingIfStatusChangeCount = _SparingIfStatusChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 6),
    _SparingIfStatusChangeCount_Type()
)
sparingIfStatusChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparingIfStatusChangeCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-SPARING-MIB",
    **{"sparingGlobalGroup": sparingGlobalGroup,
       "sparingSlotGroup": sparingSlotGroup,
       "sparingSlotMode": sparingSlotMode,
       "sparingSlotTable": sparingSlotTable,
       "sparingSlotEntry": sparingSlotEntry,
       "sparingSlotPrimaryIndex": sparingSlotPrimaryIndex,
       "sparingSlotSparingIndex": sparingSlotSparingIndex,
       "sparingSlotStatus": sparingSlotStatus,
       "sparingSlotLastStatusChange": sparingSlotLastStatusChange,
       "sparingSlotLastChangeReason": sparingSlotLastChangeReason,
       "sparingSlotStatusChangeCount": sparingSlotStatusChangeCount,
       "sparingIfGroup": sparingIfGroup,
       "sparingIfTable": sparingIfTable,
       "sparingIfEntry": sparingIfEntry,
       "sparingIfPrimaryIndex": sparingIfPrimaryIndex,
       "sparingIfSparingIndex": sparingIfSparingIndex,
       "sparingIfStatus": sparingIfStatus,
       "sparingIfLastStatusChange": sparingIfLastStatusChange,
       "sparingIfLastChangeReason": sparingIfLastChangeReason,
       "sparingIfStatusChangeCount": sparingIfStatusChangeCount}
)
