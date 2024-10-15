# SNMP MIB module (NNCCEFILLLEVELSTATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCCEFILLLEVELSTATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:17 2024
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

nncCEFillLevelStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncCEFillLevelStatisticsObjects_ObjectIdentity = ObjectIdentity
nncCEFillLevelStatisticsObjects = _NncCEFillLevelStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 1)
)
_NncCEFillLevelStatisticsTable_Object = MibTable
nncCEFillLevelStatisticsTable = _NncCEFillLevelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1)
)
if mibBuilder.loadTexts:
    nncCEFillLevelStatisticsTable.setStatus("current")
_NncCEFillLevelStatisticsEntry_Object = MibTableRow
nncCEFillLevelStatisticsEntry = _NncCEFillLevelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1)
)
nncCEFillLevelStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncCEFillLevelStatisticsEntry.setStatus("current")


class _NncCEMinFillLevel_Type(Integer32):
    """Custom type nncCEMinFillLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_NncCEMinFillLevel_Type.__name__ = "Integer32"
_NncCEMinFillLevel_Object = MibTableColumn
nncCEMinFillLevel = _NncCEMinFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 1),
    _NncCEMinFillLevel_Type()
)
nncCEMinFillLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCEMinFillLevel.setStatus("current")


class _NncCEMaxFillLevel_Type(Integer32):
    """Custom type nncCEMaxFillLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_NncCEMaxFillLevel_Type.__name__ = "Integer32"
_NncCEMaxFillLevel_Object = MibTableColumn
nncCEMaxFillLevel = _NncCEMaxFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 2),
    _NncCEMaxFillLevel_Type()
)
nncCEMaxFillLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncCEMaxFillLevel.setStatus("current")
_NncCEFillLevelStatisticsGroups_ObjectIdentity = ObjectIdentity
nncCEFillLevelStatisticsGroups = _NncCEFillLevelStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 2)
)
_NncCEFillLevelStatisticsCompliances_ObjectIdentity = ObjectIdentity
nncCEFillLevelStatisticsCompliances = _NncCEFillLevelStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 3)
)

# Managed Objects groups

nncCERawFillLevelStatisticsGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 2, 1)
)
nncCERawFillLevelStatisticsGroups.setObjects(
      *(("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMinFillLevel"),
        ("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMaxFillLevel"))
)
if mibBuilder.loadTexts:
    nncCERawFillLevelStatisticsGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncCEFillLevelStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 47, 3, 1)
)
if mibBuilder.loadTexts:
    nncCEFillLevelStatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCCEFILLLEVELSTATISTICS-MIB",
    **{"nncCEFillLevelStatistics": nncCEFillLevelStatistics,
       "nncCEFillLevelStatisticsObjects": nncCEFillLevelStatisticsObjects,
       "nncCEFillLevelStatisticsTable": nncCEFillLevelStatisticsTable,
       "nncCEFillLevelStatisticsEntry": nncCEFillLevelStatisticsEntry,
       "nncCEMinFillLevel": nncCEMinFillLevel,
       "nncCEMaxFillLevel": nncCEMaxFillLevel,
       "nncCEFillLevelStatisticsGroups": nncCEFillLevelStatisticsGroups,
       "nncCERawFillLevelStatisticsGroups": nncCERawFillLevelStatisticsGroups,
       "nncCEFillLevelStatisticsCompliances": nncCEFillLevelStatisticsCompliances,
       "nncCEFillLevelStatisticsCompliance": nncCEFillLevelStatisticsCompliance}
)
