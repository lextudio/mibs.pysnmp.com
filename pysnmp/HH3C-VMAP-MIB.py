# SNMP MIB module (HH3C-VMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:15 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cVmap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138)
)
hh3cVmap.setRevisions(
        ("2013-03-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVMAPNNITable_Object = MibTable
hh3cVMAPNNITable = _Hh3cVMAPNNITable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 1)
)
if mibBuilder.loadTexts:
    hh3cVMAPNNITable.setStatus("current")
_Hh3cVMAPNNIEntry_Object = MibTableRow
hh3cVMAPNNIEntry = _Hh3cVMAPNNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 1, 1)
)
hh3cVMAPNNIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cVMAPNNIEntry.setStatus("current")
_Hh3cVMAPNNIState_Type = TruthValue
_Hh3cVMAPNNIState_Object = MibTableColumn
hh3cVMAPNNIState = _Hh3cVMAPNNIState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 1, 1, 1),
    _Hh3cVMAPNNIState_Type()
)
hh3cVMAPNNIState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVMAPNNIState.setStatus("current")
_Hh3cVMAP1to1Table_Object = MibTable
hh3cVMAP1to1Table = _Hh3cVMAP1to1Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 2)
)
if mibBuilder.loadTexts:
    hh3cVMAP1to1Table.setStatus("current")
_Hh3cVMAP1to1Entry_Object = MibTableRow
hh3cVMAP1to1Entry = _Hh3cVMAP1to1Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1)
)
hh3cVMAP1to1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAP1to1Vlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAP1to1Entry.setStatus("current")


class _Hh3cVMAP1to1Vlan_Type(Integer32):
    """Custom type hh3cVMAP1to1Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to1Vlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to1Vlan_Object = MibTableColumn
hh3cVMAP1to1Vlan = _Hh3cVMAP1to1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 1),
    _Hh3cVMAP1to1Vlan_Type()
)
hh3cVMAP1to1Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAP1to1Vlan.setStatus("current")


class _Hh3cVMAP1to1TranslatedVlan_Type(Integer32):
    """Custom type hh3cVMAP1to1TranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to1TranslatedVlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to1TranslatedVlan_Object = MibTableColumn
hh3cVMAP1to1TranslatedVlan = _Hh3cVMAP1to1TranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 2),
    _Hh3cVMAP1to1TranslatedVlan_Type()
)
hh3cVMAP1to1TranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to1TranslatedVlan.setStatus("current")
_Hh3cVMAP1to1RowStatus_Type = RowStatus
_Hh3cVMAP1to1RowStatus_Object = MibTableColumn
hh3cVMAP1to1RowStatus = _Hh3cVMAP1to1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 3),
    _Hh3cVMAP1to1RowStatus_Type()
)
hh3cVMAP1to1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to1RowStatus.setStatus("current")
_Hh3cVMAPNto1RangeTable_Object = MibTable
hh3cVMAPNto1RangeTable = _Hh3cVMAPNto1RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3)
)
if mibBuilder.loadTexts:
    hh3cVMAPNto1RangeTable.setStatus("current")
_Hh3cVMAPNto1RangeEntry_Object = MibTableRow
hh3cVMAPNto1RangeEntry = _Hh3cVMAPNto1RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1)
)
hh3cVMAPNto1RangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAPNto1StartVlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAPNto1RangeEntry.setStatus("current")


class _Hh3cVMAPNto1StartVlan_Type(Integer32):
    """Custom type hh3cVMAPNto1StartVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAPNto1StartVlan_Type.__name__ = "Integer32"
_Hh3cVMAPNto1StartVlan_Object = MibTableColumn
hh3cVMAPNto1StartVlan = _Hh3cVMAPNto1StartVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 1),
    _Hh3cVMAPNto1StartVlan_Type()
)
hh3cVMAPNto1StartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAPNto1StartVlan.setStatus("current")


class _Hh3cVMAPNto1EndVlan_Type(Integer32):
    """Custom type hh3cVMAPNto1EndVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAPNto1EndVlan_Type.__name__ = "Integer32"
_Hh3cVMAPNto1EndVlan_Object = MibTableColumn
hh3cVMAPNto1EndVlan = _Hh3cVMAPNto1EndVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 2),
    _Hh3cVMAPNto1EndVlan_Type()
)
hh3cVMAPNto1EndVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAPNto1EndVlan.setStatus("current")


class _Hh3cVMAPNto1RangeTranslatedVlan_Type(Integer32):
    """Custom type hh3cVMAPNto1RangeTranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAPNto1RangeTranslatedVlan_Type.__name__ = "Integer32"
_Hh3cVMAPNto1RangeTranslatedVlan_Object = MibTableColumn
hh3cVMAPNto1RangeTranslatedVlan = _Hh3cVMAPNto1RangeTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 3),
    _Hh3cVMAPNto1RangeTranslatedVlan_Type()
)
hh3cVMAPNto1RangeTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAPNto1RangeTranslatedVlan.setStatus("current")
_Hh3cVMAPNto1RangeRowStatus_Type = RowStatus
_Hh3cVMAPNto1RangeRowStatus_Object = MibTableColumn
hh3cVMAPNto1RangeRowStatus = _Hh3cVMAPNto1RangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 4),
    _Hh3cVMAPNto1RangeRowStatus_Type()
)
hh3cVMAPNto1RangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAPNto1RangeRowStatus.setStatus("current")
_Hh3cVMAPNto1SingleTable_Object = MibTable
hh3cVMAPNto1SingleTable = _Hh3cVMAPNto1SingleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 4)
)
if mibBuilder.loadTexts:
    hh3cVMAPNto1SingleTable.setStatus("current")
_Hh3cVMAPNto1SingleEntry_Object = MibTableRow
hh3cVMAPNto1SingleEntry = _Hh3cVMAPNto1SingleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1)
)
hh3cVMAPNto1SingleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAPNto1Vlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAPNto1SingleEntry.setStatus("current")


class _Hh3cVMAPNto1Vlan_Type(Integer32):
    """Custom type hh3cVMAPNto1Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAPNto1Vlan_Type.__name__ = "Integer32"
_Hh3cVMAPNto1Vlan_Object = MibTableColumn
hh3cVMAPNto1Vlan = _Hh3cVMAPNto1Vlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 1),
    _Hh3cVMAPNto1Vlan_Type()
)
hh3cVMAPNto1Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAPNto1Vlan.setStatus("current")


class _Hh3cVMAPNto1SingleTranslatedVlan_Type(Integer32):
    """Custom type hh3cVMAPNto1SingleTranslatedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAPNto1SingleTranslatedVlan_Type.__name__ = "Integer32"
_Hh3cVMAPNto1SingleTranslatedVlan_Object = MibTableColumn
hh3cVMAPNto1SingleTranslatedVlan = _Hh3cVMAPNto1SingleTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 2),
    _Hh3cVMAPNto1SingleTranslatedVlan_Type()
)
hh3cVMAPNto1SingleTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAPNto1SingleTranslatedVlan.setStatus("current")
_Hh3cVMAPNto1SingleRowStatus_Type = RowStatus
_Hh3cVMAPNto1SingleRowStatus_Object = MibTableColumn
hh3cVMAPNto1SingleRowStatus = _Hh3cVMAPNto1SingleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 3),
    _Hh3cVMAPNto1SingleRowStatus_Type()
)
hh3cVMAPNto1SingleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAPNto1SingleRowStatus.setStatus("current")
_Hh3cVMAP1to2RangeTable_Object = MibTable
hh3cVMAP1to2RangeTable = _Hh3cVMAP1to2RangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5)
)
if mibBuilder.loadTexts:
    hh3cVMAP1to2RangeTable.setStatus("current")
_Hh3cVMAP1to2RangeEntry_Object = MibTableRow
hh3cVMAP1to2RangeEntry = _Hh3cVMAP1to2RangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1)
)
hh3cVMAP1to2RangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAP1to2StartVlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAP1to2RangeEntry.setStatus("current")


class _Hh3cVMAP1to2StartVlan_Type(Integer32):
    """Custom type hh3cVMAP1to2StartVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to2StartVlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to2StartVlan_Object = MibTableColumn
hh3cVMAP1to2StartVlan = _Hh3cVMAP1to2StartVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 1),
    _Hh3cVMAP1to2StartVlan_Type()
)
hh3cVMAP1to2StartVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAP1to2StartVlan.setStatus("current")


class _Hh3cVMAP1to2EndVlan_Type(Integer32):
    """Custom type hh3cVMAP1to2EndVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to2EndVlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to2EndVlan_Object = MibTableColumn
hh3cVMAP1to2EndVlan = _Hh3cVMAP1to2EndVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 2),
    _Hh3cVMAP1to2EndVlan_Type()
)
hh3cVMAP1to2EndVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to2EndVlan.setStatus("current")


class _Hh3cVMAP1to2RangeNestedVlan_Type(Integer32):
    """Custom type hh3cVMAP1to2RangeNestedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to2RangeNestedVlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to2RangeNestedVlan_Object = MibTableColumn
hh3cVMAP1to2RangeNestedVlan = _Hh3cVMAP1to2RangeNestedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 3),
    _Hh3cVMAP1to2RangeNestedVlan_Type()
)
hh3cVMAP1to2RangeNestedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to2RangeNestedVlan.setStatus("current")
_Hh3cVMAP1to2RangeRowStatus_Type = RowStatus
_Hh3cVMAP1to2RangeRowStatus_Object = MibTableColumn
hh3cVMAP1to2RangeRowStatus = _Hh3cVMAP1to2RangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 4),
    _Hh3cVMAP1to2RangeRowStatus_Type()
)
hh3cVMAP1to2RangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to2RangeRowStatus.setStatus("current")
_Hh3cVMAP1to2SingleTable_Object = MibTable
hh3cVMAP1to2SingleTable = _Hh3cVMAP1to2SingleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 6)
)
if mibBuilder.loadTexts:
    hh3cVMAP1to2SingleTable.setStatus("current")
_Hh3cVMAP1to2SingleEntry_Object = MibTableRow
hh3cVMAP1to2SingleEntry = _Hh3cVMAP1to2SingleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1)
)
hh3cVMAP1to2SingleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAP1to2Vlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAP1to2SingleEntry.setStatus("current")


class _Hh3cVMAP1to2Vlan_Type(Integer32):
    """Custom type hh3cVMAP1to2Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to2Vlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to2Vlan_Object = MibTableColumn
hh3cVMAP1to2Vlan = _Hh3cVMAP1to2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 1),
    _Hh3cVMAP1to2Vlan_Type()
)
hh3cVMAP1to2Vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAP1to2Vlan.setStatus("current")


class _Hh3cVMAP1to2SingleNestedVlan_Type(Integer32):
    """Custom type hh3cVMAP1to2SingleNestedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP1to2SingleNestedVlan_Type.__name__ = "Integer32"
_Hh3cVMAP1to2SingleNestedVlan_Object = MibTableColumn
hh3cVMAP1to2SingleNestedVlan = _Hh3cVMAP1to2SingleNestedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 2),
    _Hh3cVMAP1to2SingleNestedVlan_Type()
)
hh3cVMAP1to2SingleNestedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to2SingleNestedVlan.setStatus("current")
_Hh3cVMAP1to2SingleRowStatus_Type = RowStatus
_Hh3cVMAP1to2SingleRowStatus_Object = MibTableColumn
hh3cVMAP1to2SingleRowStatus = _Hh3cVMAP1to2SingleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 3),
    _Hh3cVMAP1to2SingleRowStatus_Type()
)
hh3cVMAP1to2SingleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP1to2SingleRowStatus.setStatus("current")
_Hh3cVMAP2to2Table_Object = MibTable
hh3cVMAP2to2Table = _Hh3cVMAP2to2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7)
)
if mibBuilder.loadTexts:
    hh3cVMAP2to2Table.setStatus("current")
_Hh3cVMAP2to2Entry_Object = MibTableRow
hh3cVMAP2to2Entry = _Hh3cVMAP2to2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1)
)
hh3cVMAP2to2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAP2to2OuterVlan"),
    (0, "HH3C-VMAP-MIB", "hh3cVMAP2to2InnerVlan"),
)
if mibBuilder.loadTexts:
    hh3cVMAP2to2Entry.setStatus("current")


class _Hh3cVMAP2to2OuterVlan_Type(Integer32):
    """Custom type hh3cVMAP2to2OuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP2to2OuterVlan_Type.__name__ = "Integer32"
_Hh3cVMAP2to2OuterVlan_Object = MibTableColumn
hh3cVMAP2to2OuterVlan = _Hh3cVMAP2to2OuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 1),
    _Hh3cVMAP2to2OuterVlan_Type()
)
hh3cVMAP2to2OuterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAP2to2OuterVlan.setStatus("current")


class _Hh3cVMAP2to2InnerVlan_Type(Integer32):
    """Custom type hh3cVMAP2to2InnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP2to2InnerVlan_Type.__name__ = "Integer32"
_Hh3cVMAP2to2InnerVlan_Object = MibTableColumn
hh3cVMAP2to2InnerVlan = _Hh3cVMAP2to2InnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 2),
    _Hh3cVMAP2to2InnerVlan_Type()
)
hh3cVMAP2to2InnerVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVMAP2to2InnerVlan.setStatus("current")


class _Hh3cVMAP2to2TranslatedOuterVlan_Type(Integer32):
    """Custom type hh3cVMAP2to2TranslatedOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP2to2TranslatedOuterVlan_Type.__name__ = "Integer32"
_Hh3cVMAP2to2TranslatedOuterVlan_Object = MibTableColumn
hh3cVMAP2to2TranslatedOuterVlan = _Hh3cVMAP2to2TranslatedOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 3),
    _Hh3cVMAP2to2TranslatedOuterVlan_Type()
)
hh3cVMAP2to2TranslatedOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP2to2TranslatedOuterVlan.setStatus("current")


class _Hh3cVMAP2to2TranslatedInnerVlan_Type(Integer32):
    """Custom type hh3cVMAP2to2TranslatedInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVMAP2to2TranslatedInnerVlan_Type.__name__ = "Integer32"
_Hh3cVMAP2to2TranslatedInnerVlan_Object = MibTableColumn
hh3cVMAP2to2TranslatedInnerVlan = _Hh3cVMAP2to2TranslatedInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 4),
    _Hh3cVMAP2to2TranslatedInnerVlan_Type()
)
hh3cVMAP2to2TranslatedInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP2to2TranslatedInnerVlan.setStatus("current")
_Hh3cVMAP2to2RowStatus_Type = RowStatus
_Hh3cVMAP2to2RowStatus_Object = MibTableColumn
hh3cVMAP2to2RowStatus = _Hh3cVMAP2to2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 5),
    _Hh3cVMAP2to2RowStatus_Type()
)
hh3cVMAP2to2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVMAP2to2RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VMAP-MIB",
    **{"hh3cVmap": hh3cVmap,
       "hh3cVMAPNNITable": hh3cVMAPNNITable,
       "hh3cVMAPNNIEntry": hh3cVMAPNNIEntry,
       "hh3cVMAPNNIState": hh3cVMAPNNIState,
       "hh3cVMAP1to1Table": hh3cVMAP1to1Table,
       "hh3cVMAP1to1Entry": hh3cVMAP1to1Entry,
       "hh3cVMAP1to1Vlan": hh3cVMAP1to1Vlan,
       "hh3cVMAP1to1TranslatedVlan": hh3cVMAP1to1TranslatedVlan,
       "hh3cVMAP1to1RowStatus": hh3cVMAP1to1RowStatus,
       "hh3cVMAPNto1RangeTable": hh3cVMAPNto1RangeTable,
       "hh3cVMAPNto1RangeEntry": hh3cVMAPNto1RangeEntry,
       "hh3cVMAPNto1StartVlan": hh3cVMAPNto1StartVlan,
       "hh3cVMAPNto1EndVlan": hh3cVMAPNto1EndVlan,
       "hh3cVMAPNto1RangeTranslatedVlan": hh3cVMAPNto1RangeTranslatedVlan,
       "hh3cVMAPNto1RangeRowStatus": hh3cVMAPNto1RangeRowStatus,
       "hh3cVMAPNto1SingleTable": hh3cVMAPNto1SingleTable,
       "hh3cVMAPNto1SingleEntry": hh3cVMAPNto1SingleEntry,
       "hh3cVMAPNto1Vlan": hh3cVMAPNto1Vlan,
       "hh3cVMAPNto1SingleTranslatedVlan": hh3cVMAPNto1SingleTranslatedVlan,
       "hh3cVMAPNto1SingleRowStatus": hh3cVMAPNto1SingleRowStatus,
       "hh3cVMAP1to2RangeTable": hh3cVMAP1to2RangeTable,
       "hh3cVMAP1to2RangeEntry": hh3cVMAP1to2RangeEntry,
       "hh3cVMAP1to2StartVlan": hh3cVMAP1to2StartVlan,
       "hh3cVMAP1to2EndVlan": hh3cVMAP1to2EndVlan,
       "hh3cVMAP1to2RangeNestedVlan": hh3cVMAP1to2RangeNestedVlan,
       "hh3cVMAP1to2RangeRowStatus": hh3cVMAP1to2RangeRowStatus,
       "hh3cVMAP1to2SingleTable": hh3cVMAP1to2SingleTable,
       "hh3cVMAP1to2SingleEntry": hh3cVMAP1to2SingleEntry,
       "hh3cVMAP1to2Vlan": hh3cVMAP1to2Vlan,
       "hh3cVMAP1to2SingleNestedVlan": hh3cVMAP1to2SingleNestedVlan,
       "hh3cVMAP1to2SingleRowStatus": hh3cVMAP1to2SingleRowStatus,
       "hh3cVMAP2to2Table": hh3cVMAP2to2Table,
       "hh3cVMAP2to2Entry": hh3cVMAP2to2Entry,
       "hh3cVMAP2to2OuterVlan": hh3cVMAP2to2OuterVlan,
       "hh3cVMAP2to2InnerVlan": hh3cVMAP2to2InnerVlan,
       "hh3cVMAP2to2TranslatedOuterVlan": hh3cVMAP2to2TranslatedOuterVlan,
       "hh3cVMAP2to2TranslatedInnerVlan": hh3cVMAP2to2TranslatedInnerVlan,
       "hh3cVMAP2to2RowStatus": hh3cVMAP2to2RowStatus}
)
