# SNMP MIB module (ROHC-UNCOMPRESSED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROHC-UNCOMPRESSED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:11 2024
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

(rohcChannelID,
 rohcContextCID) = mibBuilder.importSymbols(
    "ROHC-MIB",
    "rohcChannelID",
    "rohcContextCID")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rohcUncmprMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 113)
)
rohcUncmprMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RohcUncmprObjects_ObjectIdentity = ObjectIdentity
rohcUncmprObjects = _RohcUncmprObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 113, 1)
)
_RohcUncmprContextTable_Object = MibTable
rohcUncmprContextTable = _RohcUncmprContextTable_Object(
    (1, 3, 6, 1, 2, 1, 113, 1, 1)
)
if mibBuilder.loadTexts:
    rohcUncmprContextTable.setStatus("current")
_RohcUncmprContextEntry_Object = MibTableRow
rohcUncmprContextEntry = _RohcUncmprContextEntry_Object(
    (1, 3, 6, 1, 2, 1, 113, 1, 1, 1)
)
rohcUncmprContextEntry.setIndexNames(
    (0, "ROHC-MIB", "rohcChannelID"),
    (0, "ROHC-MIB", "rohcContextCID"),
)
if mibBuilder.loadTexts:
    rohcUncmprContextEntry.setStatus("current")


class _RohcUncmprContextState_Type(Integer32):
    """Custom type rohcUncmprContextState based on Integer32"""
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
        *(("fullContext", 4),
          ("initAndRefresh", 1),
          ("noContext", 3),
          ("normal", 2))
    )


_RohcUncmprContextState_Type.__name__ = "Integer32"
_RohcUncmprContextState_Object = MibTableColumn
rohcUncmprContextState = _RohcUncmprContextState_Object(
    (1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 3),
    _RohcUncmprContextState_Type()
)
rohcUncmprContextState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcUncmprContextState.setStatus("current")


class _RohcUncmprContextMode_Type(Integer32):
    """Custom type rohcUncmprContextMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_RohcUncmprContextMode_Type.__name__ = "Integer32"
_RohcUncmprContextMode_Object = MibTableColumn
rohcUncmprContextMode = _RohcUncmprContextMode_Object(
    (1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 4),
    _RohcUncmprContextMode_Type()
)
rohcUncmprContextMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcUncmprContextMode.setStatus("current")
_RohcUncmprContextACKs_Type = Counter32
_RohcUncmprContextACKs_Object = MibTableColumn
rohcUncmprContextACKs = _RohcUncmprContextACKs_Object(
    (1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 5),
    _RohcUncmprContextACKs_Type()
)
rohcUncmprContextACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcUncmprContextACKs.setStatus("current")
_RohcUncmprConformance_ObjectIdentity = ObjectIdentity
rohcUncmprConformance = _RohcUncmprConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 113, 2)
)
_RohcUncmprCompliances_ObjectIdentity = ObjectIdentity
rohcUncmprCompliances = _RohcUncmprCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 113, 2, 1)
)
_RohcUncmprGroups_ObjectIdentity = ObjectIdentity
rohcUncmprGroups = _RohcUncmprGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 113, 2, 2)
)

# Managed Objects groups

rohcUncmprContextGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 113, 2, 2, 1)
)
rohcUncmprContextGroup.setObjects(
      *(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextState"),
        ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextMode"))
)
if mibBuilder.loadTexts:
    rohcUncmprContextGroup.setStatus("current")

rohcUncmprStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 113, 2, 2, 2)
)
rohcUncmprStatisticsGroup.setObjects(
    ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextACKs")
)
if mibBuilder.loadTexts:
    rohcUncmprStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rohcUncmprCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 113, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rohcUncmprCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROHC-UNCOMPRESSED-MIB",
    **{"rohcUncmprMIB": rohcUncmprMIB,
       "rohcUncmprObjects": rohcUncmprObjects,
       "rohcUncmprContextTable": rohcUncmprContextTable,
       "rohcUncmprContextEntry": rohcUncmprContextEntry,
       "rohcUncmprContextState": rohcUncmprContextState,
       "rohcUncmprContextMode": rohcUncmprContextMode,
       "rohcUncmprContextACKs": rohcUncmprContextACKs,
       "rohcUncmprConformance": rohcUncmprConformance,
       "rohcUncmprCompliances": rohcUncmprCompliances,
       "rohcUncmprCompliance": rohcUncmprCompliance,
       "rohcUncmprGroups": rohcUncmprGroups,
       "rohcUncmprContextGroup": rohcUncmprContextGroup,
       "rohcUncmprStatisticsGroup": rohcUncmprStatisticsGroup}
)
