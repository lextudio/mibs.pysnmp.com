# SNMP MIB module (ASCEND-ADSL-DMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-ADSL-DMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:51 2024
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

(wanTypeAdslDmt,) = mibBuilder.importSymbols(
    "ASCEND-WAN-MIB",
    "wanTypeAdslDmt")

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

_AdslDmtLineStatusTable_Object = MibTable
adslDmtLineStatusTable = _AdslDmtLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1)
)
if mibBuilder.loadTexts:
    adslDmtLineStatusTable.setStatus("mandatory")
_AdslDmtLineStatusEntry_Object = MibTableRow
adslDmtLineStatusEntry = _AdslDmtLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1)
)
adslDmtLineStatusEntry.setIndexNames(
    (0, "ASCEND-ADSL-DMT-MIB", "adslDmtStatusIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslDmtLineStatusEntry.setStatus("mandatory")


class _AdslDmtStatusIfEntryIndex_Type(Integer32):
    """Custom type adslDmtStatusIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslDmtStatusIfEntryIndex_Type.__name__ = "Integer32"
_AdslDmtStatusIfEntryIndex_Object = MibTableColumn
adslDmtStatusIfEntryIndex = _AdslDmtStatusIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 1),
    _AdslDmtStatusIfEntryIndex_Type()
)
adslDmtStatusIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusIfEntryIndex.setStatus("mandatory")
_AdslDmtStatusShelfIndex_Type = Integer32
_AdslDmtStatusShelfIndex_Object = MibTableColumn
adslDmtStatusShelfIndex = _AdslDmtStatusShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 2),
    _AdslDmtStatusShelfIndex_Type()
)
adslDmtStatusShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusShelfIndex.setStatus("mandatory")
_AdslDmtStatusSlotIndex_Type = Integer32
_AdslDmtStatusSlotIndex_Object = MibTableColumn
adslDmtStatusSlotIndex = _AdslDmtStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 3),
    _AdslDmtStatusSlotIndex_Type()
)
adslDmtStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusSlotIndex.setStatus("mandatory")
_AdslDmtStatusLineIndex_Type = Integer32
_AdslDmtStatusLineIndex_Object = MibTableColumn
adslDmtStatusLineIndex = _AdslDmtStatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 4),
    _AdslDmtStatusLineIndex_Type()
)
adslDmtStatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusLineIndex.setStatus("mandatory")


class _AdslDmtStatusUnitType_Type(Integer32):
    """Custom type adslDmtStatusUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coe", 1),
          ("cpe", 2),
          ("other", 3))
    )


_AdslDmtStatusUnitType_Type.__name__ = "Integer32"
_AdslDmtStatusUnitType_Object = MibTableColumn
adslDmtStatusUnitType = _AdslDmtStatusUnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 5),
    _AdslDmtStatusUnitType_Type()
)
adslDmtStatusUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusUnitType.setStatus("mandatory")
_AdslDmtStatusUpRate_Type = Integer32
_AdslDmtStatusUpRate_Object = MibTableColumn
adslDmtStatusUpRate = _AdslDmtStatusUpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 6),
    _AdslDmtStatusUpRate_Type()
)
adslDmtStatusUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusUpRate.setStatus("mandatory")
_AdslDmtStatusDownRate_Type = Integer32
_AdslDmtStatusDownRate_Object = MibTableColumn
adslDmtStatusDownRate = _AdslDmtStatusDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 7),
    _AdslDmtStatusDownRate_Type()
)
adslDmtStatusDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusDownRate.setStatus("mandatory")
_AdslDmtStatusVendorId_Type = Integer32
_AdslDmtStatusVendorId_Object = MibTableColumn
adslDmtStatusVendorId = _AdslDmtStatusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 8),
    _AdslDmtStatusVendorId_Type()
)
adslDmtStatusVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusVendorId.setStatus("mandatory")
_AdslDmtStatusFirmWareVer_Type = Integer32
_AdslDmtStatusFirmWareVer_Object = MibTableColumn
adslDmtStatusFirmWareVer = _AdslDmtStatusFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 9),
    _AdslDmtStatusFirmWareVer_Type()
)
adslDmtStatusFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusFirmWareVer.setStatus("mandatory")
_AdslDmtStatusHardWareVer_Type = Integer32
_AdslDmtStatusHardWareVer_Object = MibTableColumn
adslDmtStatusHardWareVer = _AdslDmtStatusHardWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 10),
    _AdslDmtStatusHardWareVer_Type()
)
adslDmtStatusHardWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusHardWareVer.setStatus("mandatory")


class _AdslDmtStatusTrellis_Type(Integer32):
    """Custom type adslDmtStatusTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 3),
          ("yes", 2))
    )


_AdslDmtStatusTrellis_Type.__name__ = "Integer32"
_AdslDmtStatusTrellis_Object = MibTableColumn
adslDmtStatusTrellis = _AdslDmtStatusTrellis_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 11),
    _AdslDmtStatusTrellis_Type()
)
adslDmtStatusTrellis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusTrellis.setStatus("mandatory")


class _AdslDmtStatusEoc_Type(Integer32):
    """Custom type adslDmtStatusEoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("streaming", 3),
          ("transaction", 2),
          ("unknown", 1))
    )


_AdslDmtStatusEoc_Type.__name__ = "Integer32"
_AdslDmtStatusEoc_Object = MibTableColumn
adslDmtStatusEoc = _AdslDmtStatusEoc_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 12),
    _AdslDmtStatusEoc_Type()
)
adslDmtStatusEoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatusEoc.setStatus("mandatory")
_AdslAtucDMTPhysTable_Object = MibTable
adslAtucDMTPhysTable = _AdslAtucDMTPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2)
)
if mibBuilder.loadTexts:
    adslAtucDMTPhysTable.setStatus("mandatory")
_AdslAtucDMTPhysEntry_Object = MibTableRow
adslAtucDMTPhysEntry = _AdslAtucDMTPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1)
)
adslAtucDMTPhysEntry.setIndexNames(
    (0, "ASCEND-ADSL-DMT-MIB", "adslAtucDMTIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslAtucDMTPhysEntry.setStatus("mandatory")


class _AdslAtucDMTIfEntryIndex_Type(Integer32):
    """Custom type adslAtucDMTIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslAtucDMTIfEntryIndex_Type.__name__ = "Integer32"
_AdslAtucDMTIfEntryIndex_Object = MibTableColumn
adslAtucDMTIfEntryIndex = _AdslAtucDMTIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 1),
    _AdslAtucDMTIfEntryIndex_Type()
)
adslAtucDMTIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTIfEntryIndex.setStatus("mandatory")
_AdslAtucDMTShelfIndex_Type = Integer32
_AdslAtucDMTShelfIndex_Object = MibTableColumn
adslAtucDMTShelfIndex = _AdslAtucDMTShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 2),
    _AdslAtucDMTShelfIndex_Type()
)
adslAtucDMTShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTShelfIndex.setStatus("mandatory")
_AdslAtucDMTSlotIndex_Type = Integer32
_AdslAtucDMTSlotIndex_Object = MibTableColumn
adslAtucDMTSlotIndex = _AdslAtucDMTSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 3),
    _AdslAtucDMTSlotIndex_Type()
)
adslAtucDMTSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTSlotIndex.setStatus("mandatory")
_AdslAtucDMTLineIndex_Type = Integer32
_AdslAtucDMTLineIndex_Object = MibTableColumn
adslAtucDMTLineIndex = _AdslAtucDMTLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 4),
    _AdslAtucDMTLineIndex_Type()
)
adslAtucDMTLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTLineIndex.setStatus("mandatory")


class _AdslAtucDMTIssue_Type(Integer32):
    """Custom type adslAtucDMTIssue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("etsi-iss1", 5),
          ("gdmt-iss1", 4),
          ("other", 6),
          ("t1-413-iss1", 1),
          ("t1-413-iss2", 2),
          ("t1-413-iss3", 3))
    )


_AdslAtucDMTIssue_Type.__name__ = "Integer32"
_AdslAtucDMTIssue_Object = MibTableColumn
adslAtucDMTIssue = _AdslAtucDMTIssue_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 5),
    _AdslAtucDMTIssue_Type()
)
adslAtucDMTIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTIssue.setStatus("mandatory")


class _AdslAtucDMTState_Type(Integer32):
    """Custom type adslAtucDMTState based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("activating", 7),
          ("analyzing", 9),
          ("configure", 3),
          ("exchange", 10),
          ("idle", 4),
          ("not-responding", 12),
          ("other", 1),
          ("power-up", 2),
          ("quiet", 5),
          ("steady-state", 11),
          ("tone", 6),
          ("training", 8))
    )


_AdslAtucDMTState_Type.__name__ = "Integer32"
_AdslAtucDMTState_Object = MibTableColumn
adslAtucDMTState = _AdslAtucDMTState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 6),
    _AdslAtucDMTState_Type()
)
adslAtucDMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTState.setStatus("mandatory")


class _AdslAtucDMTInterleavePath_Type(Integer32):
    """Custom type adslAtucDMTInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDMTInterleavePath_Type.__name__ = "Integer32"
_AdslAtucDMTInterleavePath_Object = MibTableColumn
adslAtucDMTInterleavePath = _AdslAtucDMTInterleavePath_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 7),
    _AdslAtucDMTInterleavePath_Type()
)
adslAtucDMTInterleavePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTInterleavePath.setStatus("mandatory")


class _AdslAtucDMTFastPath_Type(Integer32):
    """Custom type adslAtucDMTFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as0", 2),
          ("as1", 3),
          ("none", 1))
    )


_AdslAtucDMTFastPath_Type.__name__ = "Integer32"
_AdslAtucDMTFastPath_Object = MibTableColumn
adslAtucDMTFastPath = _AdslAtucDMTFastPath_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 8),
    _AdslAtucDMTFastPath_Type()
)
adslAtucDMTFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucDMTFastPath.setStatus("mandatory")
_AdslAturDMTPhysTable_Object = MibTable
adslAturDMTPhysTable = _AdslAturDMTPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3)
)
if mibBuilder.loadTexts:
    adslAturDMTPhysTable.setStatus("mandatory")
_AdslAturDMTPhysEntry_Object = MibTableRow
adslAturDMTPhysEntry = _AdslAturDMTPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1)
)
adslAturDMTPhysEntry.setIndexNames(
    (0, "ASCEND-ADSL-DMT-MIB", "adslAturDMTIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslAturDMTPhysEntry.setStatus("mandatory")


class _AdslAturDMTIfEntryIndex_Type(Integer32):
    """Custom type adslAturDMTIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslAturDMTIfEntryIndex_Type.__name__ = "Integer32"
_AdslAturDMTIfEntryIndex_Object = MibTableColumn
adslAturDMTIfEntryIndex = _AdslAturDMTIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 1),
    _AdslAturDMTIfEntryIndex_Type()
)
adslAturDMTIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTIfEntryIndex.setStatus("mandatory")
_AdslAturDMTShelfIndex_Type = Integer32
_AdslAturDMTShelfIndex_Object = MibTableColumn
adslAturDMTShelfIndex = _AdslAturDMTShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 2),
    _AdslAturDMTShelfIndex_Type()
)
adslAturDMTShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTShelfIndex.setStatus("mandatory")
_AdslAturDMTSlotIndex_Type = Integer32
_AdslAturDMTSlotIndex_Object = MibTableColumn
adslAturDMTSlotIndex = _AdslAturDMTSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 3),
    _AdslAturDMTSlotIndex_Type()
)
adslAturDMTSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTSlotIndex.setStatus("mandatory")
_AdslAturDMTLineIndex_Type = Integer32
_AdslAturDMTLineIndex_Object = MibTableColumn
adslAturDMTLineIndex = _AdslAturDMTLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 4),
    _AdslAturDMTLineIndex_Type()
)
adslAturDMTLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTLineIndex.setStatus("mandatory")


class _AdslAturDMTIssue_Type(Integer32):
    """Custom type adslAturDMTIssue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("etsi-iss1", 5),
          ("gdmt-iss1", 4),
          ("other", 6),
          ("t1-413-iss1", 1),
          ("t1-413-iss2", 2),
          ("t1-413-iss3", 3))
    )


_AdslAturDMTIssue_Type.__name__ = "Integer32"
_AdslAturDMTIssue_Object = MibTableColumn
adslAturDMTIssue = _AdslAturDMTIssue_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 5),
    _AdslAturDMTIssue_Type()
)
adslAturDMTIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTIssue.setStatus("mandatory")


class _AdslAturDMTState_Type(Integer32):
    """Custom type adslAturDMTState based on Integer32"""
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
        *(("activating", 2),
          ("analyzing", 4),
          ("exchange", 5),
          ("not-responding", 7),
          ("other", 1),
          ("steady-state", 6),
          ("training", 3))
    )


_AdslAturDMTState_Type.__name__ = "Integer32"
_AdslAturDMTState_Object = MibTableColumn
adslAturDMTState = _AdslAturDMTState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 6),
    _AdslAturDMTState_Type()
)
adslAturDMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTState.setStatus("mandatory")


class _AdslAturDMTInterleavePath_Type(Integer32):
    """Custom type adslAturDMTInterleavePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDMTInterleavePath_Type.__name__ = "Integer32"
_AdslAturDMTInterleavePath_Object = MibTableColumn
adslAturDMTInterleavePath = _AdslAturDMTInterleavePath_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 7),
    _AdslAturDMTInterleavePath_Type()
)
adslAturDMTInterleavePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTInterleavePath.setStatus("mandatory")


class _AdslAturDMTFastPath_Type(Integer32):
    """Custom type adslAturDMTFastPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ls0", 2),
          ("ls1", 3),
          ("none", 1))
    )


_AdslAturDMTFastPath_Type.__name__ = "Integer32"
_AdslAturDMTFastPath_Object = MibTableColumn
adslAturDMTFastPath = _AdslAturDMTFastPath_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 8),
    _AdslAturDMTFastPath_Type()
)
adslAturDMTFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturDMTFastPath.setStatus("mandatory")
_AdslDmtLineStatisticTable_Object = MibTable
adslDmtLineStatisticTable = _AdslDmtLineStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4)
)
if mibBuilder.loadTexts:
    adslDmtLineStatisticTable.setStatus("mandatory")
_AdslDmtLineStatisticEntry_Object = MibTableRow
adslDmtLineStatisticEntry = _AdslDmtLineStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1)
)
adslDmtLineStatisticEntry.setIndexNames(
    (0, "ASCEND-ADSL-DMT-MIB", "adslDmtStatIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslDmtLineStatisticEntry.setStatus("mandatory")


class _AdslDmtStatIfEntryIndex_Type(Integer32):
    """Custom type adslDmtStatIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslDmtStatIfEntryIndex_Type.__name__ = "Integer32"
_AdslDmtStatIfEntryIndex_Object = MibTableColumn
adslDmtStatIfEntryIndex = _AdslDmtStatIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 1),
    _AdslDmtStatIfEntryIndex_Type()
)
adslDmtStatIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatIfEntryIndex.setStatus("mandatory")
_AdslDmtStatShelfIndex_Type = Integer32
_AdslDmtStatShelfIndex_Object = MibTableColumn
adslDmtStatShelfIndex = _AdslDmtStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 2),
    _AdslDmtStatShelfIndex_Type()
)
adslDmtStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatShelfIndex.setStatus("mandatory")
_AdslDmtStatSlotIndex_Type = Integer32
_AdslDmtStatSlotIndex_Object = MibTableColumn
adslDmtStatSlotIndex = _AdslDmtStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 3),
    _AdslDmtStatSlotIndex_Type()
)
adslDmtStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatSlotIndex.setStatus("mandatory")
_AdslDmtStatLineIndex_Type = Integer32
_AdslDmtStatLineIndex_Object = MibTableColumn
adslDmtStatLineIndex = _AdslDmtStatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 4),
    _AdslDmtStatLineIndex_Type()
)
adslDmtStatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatLineIndex.setStatus("mandatory")
_AdslDmtStatConnUpDays_Type = Integer32
_AdslDmtStatConnUpDays_Object = MibTableColumn
adslDmtStatConnUpDays = _AdslDmtStatConnUpDays_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 5),
    _AdslDmtStatConnUpDays_Type()
)
adslDmtStatConnUpDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatConnUpDays.setStatus("mandatory")
_AdslDmtStatConnUpHours_Type = Integer32
_AdslDmtStatConnUpHours_Object = MibTableColumn
adslDmtStatConnUpHours = _AdslDmtStatConnUpHours_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 6),
    _AdslDmtStatConnUpHours_Type()
)
adslDmtStatConnUpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatConnUpHours.setStatus("mandatory")
_AdslDmtStatConnUpMinutes_Type = Integer32
_AdslDmtStatConnUpMinutes_Object = MibTableColumn
adslDmtStatConnUpMinutes = _AdslDmtStatConnUpMinutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 7),
    _AdslDmtStatConnUpMinutes_Type()
)
adslDmtStatConnUpMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatConnUpMinutes.setStatus("mandatory")


class _AdslDmtStatRxSignalPresent_Type(Integer32):
    """Custom type adslDmtStatRxSignalPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdslDmtStatRxSignalPresent_Type.__name__ = "Integer32"
_AdslDmtStatRxSignalPresent_Object = MibTableColumn
adslDmtStatRxSignalPresent = _AdslDmtStatRxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 8),
    _AdslDmtStatRxSignalPresent_Type()
)
adslDmtStatRxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatRxSignalPresent.setStatus("mandatory")
_AdslDmtStatUpDwnCntr_Type = Integer32
_AdslDmtStatUpDwnCntr_Object = MibTableColumn
adslDmtStatUpDwnCntr = _AdslDmtStatUpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 9),
    _AdslDmtStatUpDwnCntr_Type()
)
adslDmtStatUpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatUpDwnCntr.setStatus("mandatory")


class _AdslDmtStatLineSelfTest_Type(Integer32):
    """Custom type adslDmtStatLineSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("passed", 3),
          ("unknown", 1))
    )


_AdslDmtStatLineSelfTest_Type.__name__ = "Integer32"
_AdslDmtStatLineSelfTest_Object = MibTableColumn
adslDmtStatLineSelfTest = _AdslDmtStatLineSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 10),
    _AdslDmtStatLineSelfTest_Type()
)
adslDmtStatLineSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslDmtStatLineSelfTest.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-ADSL-DMT-MIB",
    **{"adslDmtLineStatusTable": adslDmtLineStatusTable,
       "adslDmtLineStatusEntry": adslDmtLineStatusEntry,
       "adslDmtStatusIfEntryIndex": adslDmtStatusIfEntryIndex,
       "adslDmtStatusShelfIndex": adslDmtStatusShelfIndex,
       "adslDmtStatusSlotIndex": adslDmtStatusSlotIndex,
       "adslDmtStatusLineIndex": adslDmtStatusLineIndex,
       "adslDmtStatusUnitType": adslDmtStatusUnitType,
       "adslDmtStatusUpRate": adslDmtStatusUpRate,
       "adslDmtStatusDownRate": adslDmtStatusDownRate,
       "adslDmtStatusVendorId": adslDmtStatusVendorId,
       "adslDmtStatusFirmWareVer": adslDmtStatusFirmWareVer,
       "adslDmtStatusHardWareVer": adslDmtStatusHardWareVer,
       "adslDmtStatusTrellis": adslDmtStatusTrellis,
       "adslDmtStatusEoc": adslDmtStatusEoc,
       "adslAtucDMTPhysTable": adslAtucDMTPhysTable,
       "adslAtucDMTPhysEntry": adslAtucDMTPhysEntry,
       "adslAtucDMTIfEntryIndex": adslAtucDMTIfEntryIndex,
       "adslAtucDMTShelfIndex": adslAtucDMTShelfIndex,
       "adslAtucDMTSlotIndex": adslAtucDMTSlotIndex,
       "adslAtucDMTLineIndex": adslAtucDMTLineIndex,
       "adslAtucDMTIssue": adslAtucDMTIssue,
       "adslAtucDMTState": adslAtucDMTState,
       "adslAtucDMTInterleavePath": adslAtucDMTInterleavePath,
       "adslAtucDMTFastPath": adslAtucDMTFastPath,
       "adslAturDMTPhysTable": adslAturDMTPhysTable,
       "adslAturDMTPhysEntry": adslAturDMTPhysEntry,
       "adslAturDMTIfEntryIndex": adslAturDMTIfEntryIndex,
       "adslAturDMTShelfIndex": adslAturDMTShelfIndex,
       "adslAturDMTSlotIndex": adslAturDMTSlotIndex,
       "adslAturDMTLineIndex": adslAturDMTLineIndex,
       "adslAturDMTIssue": adslAturDMTIssue,
       "adslAturDMTState": adslAturDMTState,
       "adslAturDMTInterleavePath": adslAturDMTInterleavePath,
       "adslAturDMTFastPath": adslAturDMTFastPath,
       "adslDmtLineStatisticTable": adslDmtLineStatisticTable,
       "adslDmtLineStatisticEntry": adslDmtLineStatisticEntry,
       "adslDmtStatIfEntryIndex": adslDmtStatIfEntryIndex,
       "adslDmtStatShelfIndex": adslDmtStatShelfIndex,
       "adslDmtStatSlotIndex": adslDmtStatSlotIndex,
       "adslDmtStatLineIndex": adslDmtStatLineIndex,
       "adslDmtStatConnUpDays": adslDmtStatConnUpDays,
       "adslDmtStatConnUpHours": adslDmtStatConnUpHours,
       "adslDmtStatConnUpMinutes": adslDmtStatConnUpMinutes,
       "adslDmtStatRxSignalPresent": adslDmtStatRxSignalPresent,
       "adslDmtStatUpDwnCntr": adslDmtStatUpDwnCntr,
       "adslDmtStatLineSelfTest": adslDmtStatLineSelfTest}
)
