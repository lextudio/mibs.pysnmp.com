# SNMP MIB module (HPN-ICF-MPLSTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLSTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:14 2024
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

hpnicfMplsTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143)
)
hpnicfMplsTe.setRevisions(
        ("2013-06-13 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMplsTeObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsTeObjects = _HpnicfMplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1)
)
_HpnicfMplsTeScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfMplsTeScalarGroup = _HpnicfMplsTeScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1)
)
_HpnicfMplsTeStatus_Type = TruthValue
_HpnicfMplsTeStatus_Object = MibScalar
hpnicfMplsTeStatus = _HpnicfMplsTeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1, 1),
    _HpnicfMplsTeStatus_Type()
)
hpnicfMplsTeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsTeStatus.setStatus("current")
_HpnicfMplsTeRsvpStatus_Type = TruthValue
_HpnicfMplsTeRsvpStatus_Object = MibScalar
hpnicfMplsTeRsvpStatus = _HpnicfMplsTeRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1, 2),
    _HpnicfMplsTeRsvpStatus_Type()
)
hpnicfMplsTeRsvpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpStatus.setStatus("current")
_HpnicfMplsTeTable_Object = MibTable
hpnicfMplsTeTable = _HpnicfMplsTeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsTeTable.setStatus("current")
_HpnicfMplsTeEntry_Object = MibTableRow
hpnicfMplsTeEntry = _HpnicfMplsTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1)
)
hpnicfMplsTeEntry.setIndexNames(
    (0, "HPN-ICF-MPLSTE-MIB", "hpnicfMplsTeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsTeEntry.setStatus("current")


class _HpnicfMplsTeIndex_Type(Unsigned32):
    """Custom type hpnicfMplsTeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsTeIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsTeIndex_Object = MibTableColumn
hpnicfMplsTeIndex = _HpnicfMplsTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 1),
    _HpnicfMplsTeIndex_Type()
)
hpnicfMplsTeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsTeIndex.setStatus("current")


class _HpnicfMplsTeCapability_Type(TruthValue):
    """Custom type hpnicfMplsTeCapability based on TruthValue"""


_HpnicfMplsTeCapability_Object = MibTableColumn
hpnicfMplsTeCapability = _HpnicfMplsTeCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 2),
    _HpnicfMplsTeCapability_Type()
)
hpnicfMplsTeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsTeCapability.setStatus("current")
_HpnicfMplsTeRowStatus_Type = RowStatus
_HpnicfMplsTeRowStatus_Object = MibTableColumn
hpnicfMplsTeRowStatus = _HpnicfMplsTeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 3),
    _HpnicfMplsTeRowStatus_Type()
)
hpnicfMplsTeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsTeRowStatus.setStatus("current")
_HpnicfMplsTeRsvpTable_Object = MibTable
hpnicfMplsTeRsvpTable = _HpnicfMplsTeRsvpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpTable.setStatus("current")
_HpnicfMplsTeRsvpEntry_Object = MibTableRow
hpnicfMplsTeRsvpEntry = _HpnicfMplsTeRsvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1)
)
hpnicfMplsTeRsvpEntry.setIndexNames(
    (0, "HPN-ICF-MPLSTE-MIB", "hpnicfMplsTeRsvpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpEntry.setStatus("current")


class _HpnicfMplsTeRsvpIndex_Type(Unsigned32):
    """Custom type hpnicfMplsTeRsvpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsTeRsvpIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsTeRsvpIndex_Object = MibTableColumn
hpnicfMplsTeRsvpIndex = _HpnicfMplsTeRsvpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 1),
    _HpnicfMplsTeRsvpIndex_Type()
)
hpnicfMplsTeRsvpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpIndex.setStatus("current")


class _HpnicfMplsTeRsvpCapability_Type(TruthValue):
    """Custom type hpnicfMplsTeRsvpCapability based on TruthValue"""


_HpnicfMplsTeRsvpCapability_Object = MibTableColumn
hpnicfMplsTeRsvpCapability = _HpnicfMplsTeRsvpCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 2),
    _HpnicfMplsTeRsvpCapability_Type()
)
hpnicfMplsTeRsvpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpCapability.setStatus("current")
_HpnicfMplsTeRsvpRowStatus_Type = RowStatus
_HpnicfMplsTeRsvpRowStatus_Object = MibTableColumn
hpnicfMplsTeRsvpRowStatus = _HpnicfMplsTeRsvpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 3),
    _HpnicfMplsTeRsvpRowStatus_Type()
)
hpnicfMplsTeRsvpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsTeRsvpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLSTE-MIB",
    **{"hpnicfMplsTe": hpnicfMplsTe,
       "hpnicfMplsTeObjects": hpnicfMplsTeObjects,
       "hpnicfMplsTeScalarGroup": hpnicfMplsTeScalarGroup,
       "hpnicfMplsTeStatus": hpnicfMplsTeStatus,
       "hpnicfMplsTeRsvpStatus": hpnicfMplsTeRsvpStatus,
       "hpnicfMplsTeTable": hpnicfMplsTeTable,
       "hpnicfMplsTeEntry": hpnicfMplsTeEntry,
       "hpnicfMplsTeIndex": hpnicfMplsTeIndex,
       "hpnicfMplsTeCapability": hpnicfMplsTeCapability,
       "hpnicfMplsTeRowStatus": hpnicfMplsTeRowStatus,
       "hpnicfMplsTeRsvpTable": hpnicfMplsTeRsvpTable,
       "hpnicfMplsTeRsvpEntry": hpnicfMplsTeRsvpEntry,
       "hpnicfMplsTeRsvpIndex": hpnicfMplsTeRsvpIndex,
       "hpnicfMplsTeRsvpCapability": hpnicfMplsTeRsvpCapability,
       "hpnicfMplsTeRsvpRowStatus": hpnicfMplsTeRsvpRowStatus}
)
