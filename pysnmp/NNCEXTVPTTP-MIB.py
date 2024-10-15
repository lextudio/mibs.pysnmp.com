# SNMP MIB module (NNCEXTVPTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTVPTTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:23 2024
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

(atmVclVpi,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

nncExtVpttp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtVpttpObjects_ObjectIdentity = ObjectIdentity
nncExtVpttpObjects = _NncExtVpttpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 1)
)
_NncCrVpTrailTerminationPointTable_Object = MibTable
nncCrVpTrailTerminationPointTable = _NncCrVpTrailTerminationPointTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1)
)
if mibBuilder.loadTexts:
    nncCrVpTrailTerminationPointTable.setStatus("current")
_NncCrVpTrailTerminationPointEntry_Object = MibTableRow
nncCrVpTrailTerminationPointEntry = _NncCrVpTrailTerminationPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1)
)
nncCrVpTrailTerminationPointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
)
if mibBuilder.loadTexts:
    nncCrVpTrailTerminationPointEntry.setStatus("current")


class _NncCrVpTrailTerminationPoint_Type(Integer32):
    """Custom type nncCrVpTrailTerminationPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabledWithAlarms", 2),
          ("enabledWithNoAlarms", 1))
    )


_NncCrVpTrailTerminationPoint_Type.__name__ = "Integer32"
_NncCrVpTrailTerminationPoint_Object = MibTableColumn
nncCrVpTrailTerminationPoint = _NncCrVpTrailTerminationPoint_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 1, 1, 1, 1),
    _NncCrVpTrailTerminationPoint_Type()
)
nncCrVpTrailTerminationPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncCrVpTrailTerminationPoint.setStatus("current")
_NncExtVpttpGroups_ObjectIdentity = ObjectIdentity
nncExtVpttpGroups = _NncExtVpttpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 3)
)
_NncExtVpttpCompliances_ObjectIdentity = ObjectIdentity
nncExtVpttpCompliances = _NncExtVpttpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 4)
)

# Managed Objects groups

nncCrVpTrailTerminationPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 3, 1)
)
nncCrVpTrailTerminationPointGroup.setObjects(
    ("NNCEXTVPTTP-MIB", "nncCrVpTrailTerminationPoint")
)
if mibBuilder.loadTexts:
    nncCrVpTrailTerminationPointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncVpttpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 80, 4, 1)
)
if mibBuilder.loadTexts:
    nncVpttpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTVPTTP-MIB",
    **{"nncExtVpttp": nncExtVpttp,
       "nncExtVpttpObjects": nncExtVpttpObjects,
       "nncCrVpTrailTerminationPointTable": nncCrVpTrailTerminationPointTable,
       "nncCrVpTrailTerminationPointEntry": nncCrVpTrailTerminationPointEntry,
       "nncCrVpTrailTerminationPoint": nncCrVpTrailTerminationPoint,
       "nncExtVpttpGroups": nncExtVpttpGroups,
       "nncCrVpTrailTerminationPointGroup": nncCrVpTrailTerminationPointGroup,
       "nncExtVpttpCompliances": nncExtVpttpCompliances,
       "nncVpttpCompliance": nncVpttpCompliance}
)
