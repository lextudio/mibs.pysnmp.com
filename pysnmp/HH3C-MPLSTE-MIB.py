# SNMP MIB module (HH3C-MPLSTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLSTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:14 2024
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

hh3cMplsTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143)
)
hh3cMplsTe.setRevisions(
        ("2013-06-13 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMplsTeObjects_ObjectIdentity = ObjectIdentity
hh3cMplsTeObjects = _Hh3cMplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1)
)
_Hh3cMplsTeScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMplsTeScalarGroup = _Hh3cMplsTeScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1)
)
_Hh3cMplsTeStatus_Type = TruthValue
_Hh3cMplsTeStatus_Object = MibScalar
hh3cMplsTeStatus = _Hh3cMplsTeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1, 1),
    _Hh3cMplsTeStatus_Type()
)
hh3cMplsTeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsTeStatus.setStatus("current")
_Hh3cMplsTeRsvpStatus_Type = TruthValue
_Hh3cMplsTeRsvpStatus_Object = MibScalar
hh3cMplsTeRsvpStatus = _Hh3cMplsTeRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1, 2),
    _Hh3cMplsTeRsvpStatus_Type()
)
hh3cMplsTeRsvpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpStatus.setStatus("current")
_Hh3cMplsTeTable_Object = MibTable
hh3cMplsTeTable = _Hh3cMplsTeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsTeTable.setStatus("current")
_Hh3cMplsTeEntry_Object = MibTableRow
hh3cMplsTeEntry = _Hh3cMplsTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1)
)
hh3cMplsTeEntry.setIndexNames(
    (0, "HH3C-MPLSTE-MIB", "hh3cMplsTeIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsTeEntry.setStatus("current")


class _Hh3cMplsTeIndex_Type(Unsigned32):
    """Custom type hh3cMplsTeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsTeIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsTeIndex_Object = MibTableColumn
hh3cMplsTeIndex = _Hh3cMplsTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 1),
    _Hh3cMplsTeIndex_Type()
)
hh3cMplsTeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsTeIndex.setStatus("current")


class _Hh3cMplsTeCapability_Type(TruthValue):
    """Custom type hh3cMplsTeCapability based on TruthValue"""


_Hh3cMplsTeCapability_Object = MibTableColumn
hh3cMplsTeCapability = _Hh3cMplsTeCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 2),
    _Hh3cMplsTeCapability_Type()
)
hh3cMplsTeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsTeCapability.setStatus("current")
_Hh3cMplsTeRowStatus_Type = RowStatus
_Hh3cMplsTeRowStatus_Object = MibTableColumn
hh3cMplsTeRowStatus = _Hh3cMplsTeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 3),
    _Hh3cMplsTeRowStatus_Type()
)
hh3cMplsTeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsTeRowStatus.setStatus("current")
_Hh3cMplsTeRsvpTable_Object = MibTable
hh3cMplsTeRsvpTable = _Hh3cMplsTeRsvpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpTable.setStatus("current")
_Hh3cMplsTeRsvpEntry_Object = MibTableRow
hh3cMplsTeRsvpEntry = _Hh3cMplsTeRsvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1)
)
hh3cMplsTeRsvpEntry.setIndexNames(
    (0, "HH3C-MPLSTE-MIB", "hh3cMplsTeRsvpIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpEntry.setStatus("current")


class _Hh3cMplsTeRsvpIndex_Type(Unsigned32):
    """Custom type hh3cMplsTeRsvpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsTeRsvpIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsTeRsvpIndex_Object = MibTableColumn
hh3cMplsTeRsvpIndex = _Hh3cMplsTeRsvpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 1),
    _Hh3cMplsTeRsvpIndex_Type()
)
hh3cMplsTeRsvpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpIndex.setStatus("current")


class _Hh3cMplsTeRsvpCapability_Type(TruthValue):
    """Custom type hh3cMplsTeRsvpCapability based on TruthValue"""


_Hh3cMplsTeRsvpCapability_Object = MibTableColumn
hh3cMplsTeRsvpCapability = _Hh3cMplsTeRsvpCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 2),
    _Hh3cMplsTeRsvpCapability_Type()
)
hh3cMplsTeRsvpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpCapability.setStatus("current")
_Hh3cMplsTeRsvpRowStatus_Type = RowStatus
_Hh3cMplsTeRsvpRowStatus_Object = MibTableColumn
hh3cMplsTeRsvpRowStatus = _Hh3cMplsTeRsvpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 3),
    _Hh3cMplsTeRsvpRowStatus_Type()
)
hh3cMplsTeRsvpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsTeRsvpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLSTE-MIB",
    **{"hh3cMplsTe": hh3cMplsTe,
       "hh3cMplsTeObjects": hh3cMplsTeObjects,
       "hh3cMplsTeScalarGroup": hh3cMplsTeScalarGroup,
       "hh3cMplsTeStatus": hh3cMplsTeStatus,
       "hh3cMplsTeRsvpStatus": hh3cMplsTeRsvpStatus,
       "hh3cMplsTeTable": hh3cMplsTeTable,
       "hh3cMplsTeEntry": hh3cMplsTeEntry,
       "hh3cMplsTeIndex": hh3cMplsTeIndex,
       "hh3cMplsTeCapability": hh3cMplsTeCapability,
       "hh3cMplsTeRowStatus": hh3cMplsTeRowStatus,
       "hh3cMplsTeRsvpTable": hh3cMplsTeRsvpTable,
       "hh3cMplsTeRsvpEntry": hh3cMplsTeRsvpEntry,
       "hh3cMplsTeRsvpIndex": hh3cMplsTeRsvpIndex,
       "hh3cMplsTeRsvpCapability": hh3cMplsTeRsvpCapability,
       "hh3cMplsTeRsvpRowStatus": hh3cMplsTeRsvpRowStatus}
)
