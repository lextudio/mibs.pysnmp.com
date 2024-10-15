# SNMP MIB module (Wellfleet-HWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-HWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:20 2024
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

(wfHwFGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHwFGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfHwfTable_Object = MibTable
wfHwfTable = _WfHwfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    wfHwfTable.setStatus("mandatory")
_WfHwfEntry_Object = MibTableRow
wfHwfEntry = _WfHwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1)
)
wfHwfEntry.setIndexNames(
    (0, "Wellfleet-HWF-MIB", "wfHwfSlot"),
)
if mibBuilder.loadTexts:
    wfHwfEntry.setStatus("mandatory")


class _WfHwfDelete_Type(Integer32):
    """Custom type wfHwfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfHwfDelete_Type.__name__ = "Integer32"
_WfHwfDelete_Object = MibTableColumn
wfHwfDelete = _WfHwfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 1),
    _WfHwfDelete_Type()
)
wfHwfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHwfDelete.setStatus("mandatory")


class _WfHwfEnable_Type(Integer32):
    """Custom type wfHwfEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfHwfEnable_Type.__name__ = "Integer32"
_WfHwfEnable_Object = MibTableColumn
wfHwfEnable = _WfHwfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 2),
    _WfHwfEnable_Type()
)
wfHwfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHwfEnable.setStatus("mandatory")


class _WfHwfState_Type(Integer32):
    """Custom type wfHwfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfHwfState_Type.__name__ = "Integer32"
_WfHwfState_Object = MibTableColumn
wfHwfState = _WfHwfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 3),
    _WfHwfState_Type()
)
wfHwfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfState.setStatus("mandatory")


class _WfHwfSlot_Type(Integer32):
    """Custom type wfHwfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfHwfSlot_Type.__name__ = "Integer32"
_WfHwfSlot_Object = MibTableColumn
wfHwfSlot = _WfHwfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 4),
    _WfHwfSlot_Type()
)
wfHwfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfSlot.setStatus("mandatory")
_WfHwfAvailableLines_Type = Integer32
_WfHwfAvailableLines_Object = MibTableColumn
wfHwfAvailableLines = _WfHwfAvailableLines_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 5),
    _WfHwfAvailableLines_Type()
)
wfHwfAvailableLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfAvailableLines.setStatus("mandatory")
_WfHwfLineTable_Object = MibTable
wfHwfLineTable = _WfHwfLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    wfHwfLineTable.setStatus("mandatory")
_WfHwfLineEntry_Object = MibTableRow
wfHwfLineEntry = _WfHwfLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1)
)
wfHwfLineEntry.setIndexNames(
    (0, "Wellfleet-HWF-MIB", "wfHwfLineSlot"),
    (0, "Wellfleet-HWF-MIB", "wfHwfLineNumber"),
)
if mibBuilder.loadTexts:
    wfHwfLineEntry.setStatus("mandatory")


class _WfHwfLineState_Type(Integer32):
    """Custom type wfHwfLineState based on Integer32"""
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
        *(("disabled", 2),
          ("full", 3),
          ("operational", 1))
    )


_WfHwfLineState_Type.__name__ = "Integer32"
_WfHwfLineState_Object = MibTableColumn
wfHwfLineState = _WfHwfLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 1),
    _WfHwfLineState_Type()
)
wfHwfLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineState.setStatus("mandatory")
_WfHwfLineSlot_Type = Integer32
_WfHwfLineSlot_Object = MibTableColumn
wfHwfLineSlot = _WfHwfLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 2),
    _WfHwfLineSlot_Type()
)
wfHwfLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineSlot.setStatus("mandatory")


class _WfHwfLineNumber_Type(Integer32):
    """Custom type wfHwfLineNumber based on Integer32"""
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
        *(("five", 5),
          ("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfHwfLineNumber_Type.__name__ = "Integer32"
_WfHwfLineNumber_Object = MibTableColumn
wfHwfLineNumber = _WfHwfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 3),
    _WfHwfLineNumber_Type()
)
wfHwfLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineNumber.setStatus("mandatory")
_WfHwfLineCct_Type = Integer32
_WfHwfLineCct_Object = MibTableColumn
wfHwfLineCct = _WfHwfLineCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 4),
    _WfHwfLineCct_Type()
)
wfHwfLineCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCct.setStatus("mandatory")
_WfHwfLineCapableMaxTblSize_Type = Integer32
_WfHwfLineCapableMaxTblSize_Object = MibTableColumn
wfHwfLineCapableMaxTblSize = _WfHwfLineCapableMaxTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 5),
    _WfHwfLineCapableMaxTblSize_Type()
)
wfHwfLineCapableMaxTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCapableMaxTblSize.setStatus("mandatory")
_WfHwfLineCurrentTblSize_Type = Integer32
_WfHwfLineCurrentTblSize_Object = MibTableColumn
wfHwfLineCurrentTblSize = _WfHwfLineCurrentTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 6),
    _WfHwfLineCurrentTblSize_Type()
)
wfHwfLineCurrentTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCurrentTblSize.setStatus("mandatory")
_WfHwfLineCurrentUsedEntries_Type = Integer32
_WfHwfLineCurrentUsedEntries_Object = MibTableColumn
wfHwfLineCurrentUsedEntries = _WfHwfLineCurrentUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 7),
    _WfHwfLineCurrentUsedEntries_Type()
)
wfHwfLineCurrentUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineCurrentUsedEntries.setStatus("mandatory")
_WfHwfLineDroppedFrames_Type = Integer32
_WfHwfLineDroppedFrames_Object = MibTableColumn
wfHwfLineDroppedFrames = _WfHwfLineDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 8),
    _WfHwfLineDroppedFrames_Type()
)
wfHwfLineDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwfLineDroppedFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-HWF-MIB",
    **{"wfHwfTable": wfHwfTable,
       "wfHwfEntry": wfHwfEntry,
       "wfHwfDelete": wfHwfDelete,
       "wfHwfEnable": wfHwfEnable,
       "wfHwfState": wfHwfState,
       "wfHwfSlot": wfHwfSlot,
       "wfHwfAvailableLines": wfHwfAvailableLines,
       "wfHwfLineTable": wfHwfLineTable,
       "wfHwfLineEntry": wfHwfLineEntry,
       "wfHwfLineState": wfHwfLineState,
       "wfHwfLineSlot": wfHwfLineSlot,
       "wfHwfLineNumber": wfHwfLineNumber,
       "wfHwfLineCct": wfHwfLineCct,
       "wfHwfLineCapableMaxTblSize": wfHwfLineCapableMaxTblSize,
       "wfHwfLineCurrentTblSize": wfHwfLineCurrentTblSize,
       "wfHwfLineCurrentUsedEntries": wfHwfLineCurrentUsedEntries,
       "wfHwfLineDroppedFrames": wfHwfLineDroppedFrames}
)
