# SNMP MIB module (EQUIPE-ACAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPE-ACAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:16 2024
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

(AtmServiceCategory,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eqAcacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Equipe_ObjectIdentity = ObjectIdentity
equipe = _Equipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022)
)
_EqAcacViTable_Object = MibTable
eqAcacViTable = _EqAcacViTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1)
)
if mibBuilder.loadTexts:
    eqAcacViTable.setStatus("current")
_EqAcacViEntry_Object = MibTableRow
eqAcacViEntry = _EqAcacViEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1)
)
eqAcacViEntry.setIndexNames(
    (0, "EQUIPE-ACAC-MIB", "eqAcacViIfIndex"),
)
if mibBuilder.loadTexts:
    eqAcacViEntry.setStatus("current")


class _EqAcacViIfIndex_Type(Integer32):
    """Custom type eqAcacViIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAcacViIfIndex_Type.__name__ = "Integer32"
_EqAcacViIfIndex_Object = MibTableColumn
eqAcacViIfIndex = _EqAcacViIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 1),
    _EqAcacViIfIndex_Type()
)
eqAcacViIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViIfIndex.setStatus("current")


class _EqAcacViStartingBw_Type(Integer32):
    """Custom type eqAcacViStartingBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAcacViStartingBw_Type.__name__ = "Integer32"
_EqAcacViStartingBw_Object = MibTableColumn
eqAcacViStartingBw = _EqAcacViStartingBw_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 2),
    _EqAcacViStartingBw_Type()
)
eqAcacViStartingBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViStartingBw.setStatus("current")
_EqAcacViConsumedBw_Type = Gauge32
_EqAcacViConsumedBw_Object = MibTableColumn
eqAcacViConsumedBw = _EqAcacViConsumedBw_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 3),
    _EqAcacViConsumedBw_Type()
)
eqAcacViConsumedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViConsumedBw.setStatus("current")
_EqAcacViInConsideredCcts_Type = Counter32
_EqAcacViInConsideredCcts_Object = MibTableColumn
eqAcacViInConsideredCcts = _EqAcacViInConsideredCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 4),
    _EqAcacViInConsideredCcts_Type()
)
eqAcacViInConsideredCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViInConsideredCcts.setStatus("current")
_EqAcacViInRejectedCcts_Type = Counter32
_EqAcacViInRejectedCcts_Object = MibTableColumn
eqAcacViInRejectedCcts = _EqAcacViInRejectedCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 5),
    _EqAcacViInRejectedCcts_Type()
)
eqAcacViInRejectedCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViInRejectedCcts.setStatus("current")
_EqAcacViInActiveCcts_Type = Gauge32
_EqAcacViInActiveCcts_Object = MibTableColumn
eqAcacViInActiveCcts = _EqAcacViInActiveCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 6),
    _EqAcacViInActiveCcts_Type()
)
eqAcacViInActiveCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViInActiveCcts.setStatus("current")
_EqAcacViInReservedCcts_Type = Gauge32
_EqAcacViInReservedCcts_Object = MibTableColumn
eqAcacViInReservedCcts = _EqAcacViInReservedCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 7),
    _EqAcacViInReservedCcts_Type()
)
eqAcacViInReservedCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViInReservedCcts.setStatus("current")
_EqAcacViOutConsideredCcts_Type = Counter32
_EqAcacViOutConsideredCcts_Object = MibTableColumn
eqAcacViOutConsideredCcts = _EqAcacViOutConsideredCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 8),
    _EqAcacViOutConsideredCcts_Type()
)
eqAcacViOutConsideredCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViOutConsideredCcts.setStatus("current")
_EqAcacViOutRejectedCcts_Type = Counter32
_EqAcacViOutRejectedCcts_Object = MibTableColumn
eqAcacViOutRejectedCcts = _EqAcacViOutRejectedCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 9),
    _EqAcacViOutRejectedCcts_Type()
)
eqAcacViOutRejectedCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViOutRejectedCcts.setStatus("current")
_EqAcacViOutActiveCcts_Type = Gauge32
_EqAcacViOutActiveCcts_Object = MibTableColumn
eqAcacViOutActiveCcts = _EqAcacViOutActiveCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 10),
    _EqAcacViOutActiveCcts_Type()
)
eqAcacViOutActiveCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViOutActiveCcts.setStatus("current")
_EqAcacViOutReservedCcts_Type = Gauge32
_EqAcacViOutReservedCcts_Object = MibTableColumn
eqAcacViOutReservedCcts = _EqAcacViOutReservedCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 11),
    _EqAcacViOutReservedCcts_Type()
)
eqAcacViOutReservedCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViOutReservedCcts.setStatus("current")
_EqAcacViServCatTable_Object = MibTable
eqAcacViServCatTable = _EqAcacViServCatTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2)
)
if mibBuilder.loadTexts:
    eqAcacViServCatTable.setStatus("current")
_EqAcacViServCatEntry_Object = MibTableRow
eqAcacViServCatEntry = _EqAcacViServCatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2, 1)
)
eqAcacViServCatEntry.setIndexNames(
    (0, "EQUIPE-ACAC-MIB", "eqAcacViServCatIfIndex"),
    (0, "EQUIPE-ACAC-MIB", "eqAcacViServCatServiceCategory"),
)
if mibBuilder.loadTexts:
    eqAcacViServCatEntry.setStatus("current")


class _EqAcacViServCatIfIndex_Type(Integer32):
    """Custom type eqAcacViServCatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAcacViServCatIfIndex_Type.__name__ = "Integer32"
_EqAcacViServCatIfIndex_Object = MibTableColumn
eqAcacViServCatIfIndex = _EqAcacViServCatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 1),
    _EqAcacViServCatIfIndex_Type()
)
eqAcacViServCatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViServCatIfIndex.setStatus("current")
_EqAcacViServCatServiceCategory_Type = AtmServiceCategory
_EqAcacViServCatServiceCategory_Object = MibTableColumn
eqAcacViServCatServiceCategory = _EqAcacViServCatServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 2),
    _EqAcacViServCatServiceCategory_Type()
)
eqAcacViServCatServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViServCatServiceCategory.setStatus("current")
_EqAcacViServCatConsumedBw_Type = Gauge32
_EqAcacViServCatConsumedBw_Object = MibTableColumn
eqAcacViServCatConsumedBw = _EqAcacViServCatConsumedBw_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 3),
    _EqAcacViServCatConsumedBw_Type()
)
eqAcacViServCatConsumedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViServCatConsumedBw.setStatus("current")
_EqAcacViServCatActiveCcts_Type = Gauge32
_EqAcacViServCatActiveCcts_Object = MibTableColumn
eqAcacViServCatActiveCcts = _EqAcacViServCatActiveCcts_Object(
    (1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 4),
    _EqAcacViServCatActiveCcts_Type()
)
eqAcacViServCatActiveCcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAcacViServCatActiveCcts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPE-ACAC-MIB",
    **{"equipe": equipe,
       "eqAcacMib": eqAcacMib,
       "eqAcacViTable": eqAcacViTable,
       "eqAcacViEntry": eqAcacViEntry,
       "eqAcacViIfIndex": eqAcacViIfIndex,
       "eqAcacViStartingBw": eqAcacViStartingBw,
       "eqAcacViConsumedBw": eqAcacViConsumedBw,
       "eqAcacViInConsideredCcts": eqAcacViInConsideredCcts,
       "eqAcacViInRejectedCcts": eqAcacViInRejectedCcts,
       "eqAcacViInActiveCcts": eqAcacViInActiveCcts,
       "eqAcacViInReservedCcts": eqAcacViInReservedCcts,
       "eqAcacViOutConsideredCcts": eqAcacViOutConsideredCcts,
       "eqAcacViOutRejectedCcts": eqAcacViOutRejectedCcts,
       "eqAcacViOutActiveCcts": eqAcacViOutActiveCcts,
       "eqAcacViOutReservedCcts": eqAcacViOutReservedCcts,
       "eqAcacViServCatTable": eqAcacViServCatTable,
       "eqAcacViServCatEntry": eqAcacViServCatEntry,
       "eqAcacViServCatIfIndex": eqAcacViServCatIfIndex,
       "eqAcacViServCatServiceCategory": eqAcacViServCatServiceCategory,
       "eqAcacViServCatConsumedBw": eqAcacViServCatConsumedBw,
       "eqAcacViServCatActiveCcts": eqAcacViServCatActiveCcts}
)
