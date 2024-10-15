# SNMP MIB module (HPN-ICF-VMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:07 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfVmap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138)
)
hpnicfVmap.setRevisions(
        ("2013-03-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVMAPNNITable_Object = MibTable
hpnicfVMAPNNITable = _HpnicfVMAPNNITable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1)
)
if mibBuilder.loadTexts:
    hpnicfVMAPNNITable.setStatus("current")
_HpnicfVMAPNNIEntry_Object = MibTableRow
hpnicfVMAPNNIEntry = _HpnicfVMAPNNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1, 1)
)
hpnicfVMAPNNIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVMAPNNIEntry.setStatus("current")
_HpnicfVMAPNNIState_Type = TruthValue
_HpnicfVMAPNNIState_Object = MibTableColumn
hpnicfVMAPNNIState = _HpnicfVMAPNNIState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1, 1, 1),
    _HpnicfVMAPNNIState_Type()
)
hpnicfVMAPNNIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVMAPNNIState.setStatus("current")
_HpnicfVMAP1to1Table_Object = MibTable
hpnicfVMAP1to1Table = _HpnicfVMAP1to1Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2)
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to1Table.setStatus("current")
_HpnicfVMAP1to1Entry_Object = MibTableRow
hpnicfVMAP1to1Entry = _HpnicfVMAP1to1Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1)
)
hpnicfVMAP1to1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to1Vlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to1Entry.setStatus("current")


class _HpnicfVMAP1to1Vlan_Type(Integer32):
    """Custom type hpnicfVMAP1to1Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to1Vlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to1Vlan_Object = MibTableColumn
hpnicfVMAP1to1Vlan = _HpnicfVMAP1to1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 1),
    _HpnicfVMAP1to1Vlan_Type()
)
hpnicfVMAP1to1Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAP1to1Vlan.setStatus("current")


class _HpnicfVMAP1to1TranslatedVlan_Type(Integer32):
    """Custom type hpnicfVMAP1to1TranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to1TranslatedVlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to1TranslatedVlan_Object = MibTableColumn
hpnicfVMAP1to1TranslatedVlan = _HpnicfVMAP1to1TranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 2),
    _HpnicfVMAP1to1TranslatedVlan_Type()
)
hpnicfVMAP1to1TranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to1TranslatedVlan.setStatus("current")
_HpnicfVMAP1to1RowStatus_Type = RowStatus
_HpnicfVMAP1to1RowStatus_Object = MibTableColumn
hpnicfVMAP1to1RowStatus = _HpnicfVMAP1to1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 3),
    _HpnicfVMAP1to1RowStatus_Type()
)
hpnicfVMAP1to1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to1RowStatus.setStatus("current")
_HpnicfVMAPNto1RangeTable_Object = MibTable
hpnicfVMAPNto1RangeTable = _HpnicfVMAPNto1RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3)
)
if mibBuilder.loadTexts:
    hpnicfVMAPNto1RangeTable.setStatus("current")
_HpnicfVMAPNto1RangeEntry_Object = MibTableRow
hpnicfVMAPNto1RangeEntry = _HpnicfVMAPNto1RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1)
)
hpnicfVMAPNto1RangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAPNto1StartVlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAPNto1RangeEntry.setStatus("current")


class _HpnicfVMAPNto1StartVlan_Type(Integer32):
    """Custom type hpnicfVMAPNto1StartVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAPNto1StartVlan_Type.__name__ = "Integer32"
_HpnicfVMAPNto1StartVlan_Object = MibTableColumn
hpnicfVMAPNto1StartVlan = _HpnicfVMAPNto1StartVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 1),
    _HpnicfVMAPNto1StartVlan_Type()
)
hpnicfVMAPNto1StartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1StartVlan.setStatus("current")


class _HpnicfVMAPNto1EndVlan_Type(Integer32):
    """Custom type hpnicfVMAPNto1EndVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAPNto1EndVlan_Type.__name__ = "Integer32"
_HpnicfVMAPNto1EndVlan_Object = MibTableColumn
hpnicfVMAPNto1EndVlan = _HpnicfVMAPNto1EndVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 2),
    _HpnicfVMAPNto1EndVlan_Type()
)
hpnicfVMAPNto1EndVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1EndVlan.setStatus("current")


class _HpnicfVMAPNto1RangeTranslatedVlan_Type(Integer32):
    """Custom type hpnicfVMAPNto1RangeTranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAPNto1RangeTranslatedVlan_Type.__name__ = "Integer32"
_HpnicfVMAPNto1RangeTranslatedVlan_Object = MibTableColumn
hpnicfVMAPNto1RangeTranslatedVlan = _HpnicfVMAPNto1RangeTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 3),
    _HpnicfVMAPNto1RangeTranslatedVlan_Type()
)
hpnicfVMAPNto1RangeTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1RangeTranslatedVlan.setStatus("current")
_HpnicfVMAPNto1RangeRowStatus_Type = RowStatus
_HpnicfVMAPNto1RangeRowStatus_Object = MibTableColumn
hpnicfVMAPNto1RangeRowStatus = _HpnicfVMAPNto1RangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 4),
    _HpnicfVMAPNto1RangeRowStatus_Type()
)
hpnicfVMAPNto1RangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1RangeRowStatus.setStatus("current")
_HpnicfVMAPNto1SingleTable_Object = MibTable
hpnicfVMAPNto1SingleTable = _HpnicfVMAPNto1SingleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4)
)
if mibBuilder.loadTexts:
    hpnicfVMAPNto1SingleTable.setStatus("current")
_HpnicfVMAPNto1SingleEntry_Object = MibTableRow
hpnicfVMAPNto1SingleEntry = _HpnicfVMAPNto1SingleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1)
)
hpnicfVMAPNto1SingleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAPNto1Vlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAPNto1SingleEntry.setStatus("current")


class _HpnicfVMAPNto1Vlan_Type(Integer32):
    """Custom type hpnicfVMAPNto1Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAPNto1Vlan_Type.__name__ = "Integer32"
_HpnicfVMAPNto1Vlan_Object = MibTableColumn
hpnicfVMAPNto1Vlan = _HpnicfVMAPNto1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 1),
    _HpnicfVMAPNto1Vlan_Type()
)
hpnicfVMAPNto1Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1Vlan.setStatus("current")


class _HpnicfVMAPNto1SingleTranslatedVlan_Type(Integer32):
    """Custom type hpnicfVMAPNto1SingleTranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAPNto1SingleTranslatedVlan_Type.__name__ = "Integer32"
_HpnicfVMAPNto1SingleTranslatedVlan_Object = MibTableColumn
hpnicfVMAPNto1SingleTranslatedVlan = _HpnicfVMAPNto1SingleTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 2),
    _HpnicfVMAPNto1SingleTranslatedVlan_Type()
)
hpnicfVMAPNto1SingleTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1SingleTranslatedVlan.setStatus("current")
_HpnicfVMAPNto1SingleRowStatus_Type = RowStatus
_HpnicfVMAPNto1SingleRowStatus_Object = MibTableColumn
hpnicfVMAPNto1SingleRowStatus = _HpnicfVMAPNto1SingleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 3),
    _HpnicfVMAPNto1SingleRowStatus_Type()
)
hpnicfVMAPNto1SingleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAPNto1SingleRowStatus.setStatus("current")
_HpnicfVMAP1to2RangeTable_Object = MibTable
hpnicfVMAP1to2RangeTable = _HpnicfVMAP1to2RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5)
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to2RangeTable.setStatus("current")
_HpnicfVMAP1to2RangeEntry_Object = MibTableRow
hpnicfVMAP1to2RangeEntry = _HpnicfVMAP1to2RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1)
)
hpnicfVMAP1to2RangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to2StartVlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to2RangeEntry.setStatus("current")


class _HpnicfVMAP1to2StartVlan_Type(Integer32):
    """Custom type hpnicfVMAP1to2StartVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to2StartVlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to2StartVlan_Object = MibTableColumn
hpnicfVMAP1to2StartVlan = _HpnicfVMAP1to2StartVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 1),
    _HpnicfVMAP1to2StartVlan_Type()
)
hpnicfVMAP1to2StartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2StartVlan.setStatus("current")


class _HpnicfVMAP1to2EndVlan_Type(Integer32):
    """Custom type hpnicfVMAP1to2EndVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to2EndVlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to2EndVlan_Object = MibTableColumn
hpnicfVMAP1to2EndVlan = _HpnicfVMAP1to2EndVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 2),
    _HpnicfVMAP1to2EndVlan_Type()
)
hpnicfVMAP1to2EndVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2EndVlan.setStatus("current")


class _HpnicfVMAP1to2RangeNestedVlan_Type(Integer32):
    """Custom type hpnicfVMAP1to2RangeNestedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to2RangeNestedVlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to2RangeNestedVlan_Object = MibTableColumn
hpnicfVMAP1to2RangeNestedVlan = _HpnicfVMAP1to2RangeNestedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 3),
    _HpnicfVMAP1to2RangeNestedVlan_Type()
)
hpnicfVMAP1to2RangeNestedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2RangeNestedVlan.setStatus("current")
_HpnicfVMAP1to2RangeRowStatus_Type = RowStatus
_HpnicfVMAP1to2RangeRowStatus_Object = MibTableColumn
hpnicfVMAP1to2RangeRowStatus = _HpnicfVMAP1to2RangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 4),
    _HpnicfVMAP1to2RangeRowStatus_Type()
)
hpnicfVMAP1to2RangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2RangeRowStatus.setStatus("current")
_HpnicfVMAP1to2SingleTable_Object = MibTable
hpnicfVMAP1to2SingleTable = _HpnicfVMAP1to2SingleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6)
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to2SingleTable.setStatus("current")
_HpnicfVMAP1to2SingleEntry_Object = MibTableRow
hpnicfVMAP1to2SingleEntry = _HpnicfVMAP1to2SingleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1)
)
hpnicfVMAP1to2SingleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to2Vlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAP1to2SingleEntry.setStatus("current")


class _HpnicfVMAP1to2Vlan_Type(Integer32):
    """Custom type hpnicfVMAP1to2Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to2Vlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to2Vlan_Object = MibTableColumn
hpnicfVMAP1to2Vlan = _HpnicfVMAP1to2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 1),
    _HpnicfVMAP1to2Vlan_Type()
)
hpnicfVMAP1to2Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2Vlan.setStatus("current")


class _HpnicfVMAP1to2SingleNestedVlan_Type(Integer32):
    """Custom type hpnicfVMAP1to2SingleNestedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP1to2SingleNestedVlan_Type.__name__ = "Integer32"
_HpnicfVMAP1to2SingleNestedVlan_Object = MibTableColumn
hpnicfVMAP1to2SingleNestedVlan = _HpnicfVMAP1to2SingleNestedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 2),
    _HpnicfVMAP1to2SingleNestedVlan_Type()
)
hpnicfVMAP1to2SingleNestedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2SingleNestedVlan.setStatus("current")
_HpnicfVMAP1to2SingleRowStatus_Type = RowStatus
_HpnicfVMAP1to2SingleRowStatus_Object = MibTableColumn
hpnicfVMAP1to2SingleRowStatus = _HpnicfVMAP1to2SingleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 3),
    _HpnicfVMAP1to2SingleRowStatus_Type()
)
hpnicfVMAP1to2SingleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP1to2SingleRowStatus.setStatus("current")
_HpnicfVMAP2to2Table_Object = MibTable
hpnicfVMAP2to2Table = _HpnicfVMAP2to2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7)
)
if mibBuilder.loadTexts:
    hpnicfVMAP2to2Table.setStatus("current")
_HpnicfVMAP2to2Entry_Object = MibTableRow
hpnicfVMAP2to2Entry = _HpnicfVMAP2to2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1)
)
hpnicfVMAP2to2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP2to2OuterVlan"),
    (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP2to2InnerVlan"),
)
if mibBuilder.loadTexts:
    hpnicfVMAP2to2Entry.setStatus("current")


class _HpnicfVMAP2to2OuterVlan_Type(Integer32):
    """Custom type hpnicfVMAP2to2OuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP2to2OuterVlan_Type.__name__ = "Integer32"
_HpnicfVMAP2to2OuterVlan_Object = MibTableColumn
hpnicfVMAP2to2OuterVlan = _HpnicfVMAP2to2OuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 1),
    _HpnicfVMAP2to2OuterVlan_Type()
)
hpnicfVMAP2to2OuterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAP2to2OuterVlan.setStatus("current")


class _HpnicfVMAP2to2InnerVlan_Type(Integer32):
    """Custom type hpnicfVMAP2to2InnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP2to2InnerVlan_Type.__name__ = "Integer32"
_HpnicfVMAP2to2InnerVlan_Object = MibTableColumn
hpnicfVMAP2to2InnerVlan = _HpnicfVMAP2to2InnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 2),
    _HpnicfVMAP2to2InnerVlan_Type()
)
hpnicfVMAP2to2InnerVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVMAP2to2InnerVlan.setStatus("current")


class _HpnicfVMAP2to2TranslatedOuterVlan_Type(Integer32):
    """Custom type hpnicfVMAP2to2TranslatedOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP2to2TranslatedOuterVlan_Type.__name__ = "Integer32"
_HpnicfVMAP2to2TranslatedOuterVlan_Object = MibTableColumn
hpnicfVMAP2to2TranslatedOuterVlan = _HpnicfVMAP2to2TranslatedOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 3),
    _HpnicfVMAP2to2TranslatedOuterVlan_Type()
)
hpnicfVMAP2to2TranslatedOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP2to2TranslatedOuterVlan.setStatus("current")


class _HpnicfVMAP2to2TranslatedInnerVlan_Type(Integer32):
    """Custom type hpnicfVMAP2to2TranslatedInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVMAP2to2TranslatedInnerVlan_Type.__name__ = "Integer32"
_HpnicfVMAP2to2TranslatedInnerVlan_Object = MibTableColumn
hpnicfVMAP2to2TranslatedInnerVlan = _HpnicfVMAP2to2TranslatedInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 4),
    _HpnicfVMAP2to2TranslatedInnerVlan_Type()
)
hpnicfVMAP2to2TranslatedInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP2to2TranslatedInnerVlan.setStatus("current")
_HpnicfVMAP2to2RowStatus_Type = RowStatus
_HpnicfVMAP2to2RowStatus_Object = MibTableColumn
hpnicfVMAP2to2RowStatus = _HpnicfVMAP2to2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 5),
    _HpnicfVMAP2to2RowStatus_Type()
)
hpnicfVMAP2to2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVMAP2to2RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VMAP-MIB",
    **{"hpnicfVmap": hpnicfVmap,
       "hpnicfVMAPNNITable": hpnicfVMAPNNITable,
       "hpnicfVMAPNNIEntry": hpnicfVMAPNNIEntry,
       "hpnicfVMAPNNIState": hpnicfVMAPNNIState,
       "hpnicfVMAP1to1Table": hpnicfVMAP1to1Table,
       "hpnicfVMAP1to1Entry": hpnicfVMAP1to1Entry,
       "hpnicfVMAP1to1Vlan": hpnicfVMAP1to1Vlan,
       "hpnicfVMAP1to1TranslatedVlan": hpnicfVMAP1to1TranslatedVlan,
       "hpnicfVMAP1to1RowStatus": hpnicfVMAP1to1RowStatus,
       "hpnicfVMAPNto1RangeTable": hpnicfVMAPNto1RangeTable,
       "hpnicfVMAPNto1RangeEntry": hpnicfVMAPNto1RangeEntry,
       "hpnicfVMAPNto1StartVlan": hpnicfVMAPNto1StartVlan,
       "hpnicfVMAPNto1EndVlan": hpnicfVMAPNto1EndVlan,
       "hpnicfVMAPNto1RangeTranslatedVlan": hpnicfVMAPNto1RangeTranslatedVlan,
       "hpnicfVMAPNto1RangeRowStatus": hpnicfVMAPNto1RangeRowStatus,
       "hpnicfVMAPNto1SingleTable": hpnicfVMAPNto1SingleTable,
       "hpnicfVMAPNto1SingleEntry": hpnicfVMAPNto1SingleEntry,
       "hpnicfVMAPNto1Vlan": hpnicfVMAPNto1Vlan,
       "hpnicfVMAPNto1SingleTranslatedVlan": hpnicfVMAPNto1SingleTranslatedVlan,
       "hpnicfVMAPNto1SingleRowStatus": hpnicfVMAPNto1SingleRowStatus,
       "hpnicfVMAP1to2RangeTable": hpnicfVMAP1to2RangeTable,
       "hpnicfVMAP1to2RangeEntry": hpnicfVMAP1to2RangeEntry,
       "hpnicfVMAP1to2StartVlan": hpnicfVMAP1to2StartVlan,
       "hpnicfVMAP1to2EndVlan": hpnicfVMAP1to2EndVlan,
       "hpnicfVMAP1to2RangeNestedVlan": hpnicfVMAP1to2RangeNestedVlan,
       "hpnicfVMAP1to2RangeRowStatus": hpnicfVMAP1to2RangeRowStatus,
       "hpnicfVMAP1to2SingleTable": hpnicfVMAP1to2SingleTable,
       "hpnicfVMAP1to2SingleEntry": hpnicfVMAP1to2SingleEntry,
       "hpnicfVMAP1to2Vlan": hpnicfVMAP1to2Vlan,
       "hpnicfVMAP1to2SingleNestedVlan": hpnicfVMAP1to2SingleNestedVlan,
       "hpnicfVMAP1to2SingleRowStatus": hpnicfVMAP1to2SingleRowStatus,
       "hpnicfVMAP2to2Table": hpnicfVMAP2to2Table,
       "hpnicfVMAP2to2Entry": hpnicfVMAP2to2Entry,
       "hpnicfVMAP2to2OuterVlan": hpnicfVMAP2to2OuterVlan,
       "hpnicfVMAP2to2InnerVlan": hpnicfVMAP2to2InnerVlan,
       "hpnicfVMAP2to2TranslatedOuterVlan": hpnicfVMAP2to2TranslatedOuterVlan,
       "hpnicfVMAP2to2TranslatedInnerVlan": hpnicfVMAP2to2TranslatedInnerVlan,
       "hpnicfVMAP2to2RowStatus": hpnicfVMAP2to2RowStatus}
)
