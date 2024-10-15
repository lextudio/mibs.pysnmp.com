# SNMP MIB module (CISCO-AAL5-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAL5-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:27 2024
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

(aal5VccEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoAal5ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)
ciscoAal5ExtMIB.setRevisions(
        ("2001-11-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAal5ExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAal5ExtMIBObjects = _CiscoAal5ExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CAal5ExtConnections_ObjectIdentity = ObjectIdentity
cAal5ExtConnections = _CAal5ExtConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1)
)
_CAal5ExtVccTable_Object = MibTable
cAal5ExtVccTable = _CAal5ExtVccTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5ExtVccTable.setStatus("current")
_CAal5ExtVccEntry_Object = MibTableRow
cAal5ExtVccEntry = _CAal5ExtVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5ExtVccEntry.setStatus("current")
_CAal5VccInDroppedPkts_Type = Counter32
_CAal5VccInDroppedPkts_Object = MibTableColumn
cAal5VccInDroppedPkts = _CAal5VccInDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1),
    _CAal5VccInDroppedPkts_Type()
)
cAal5VccInDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInDroppedPkts.setUnits("packets")
_CAal5VccOutDroppedPkts_Type = Counter32
_CAal5VccOutDroppedPkts_Object = MibTableColumn
cAal5VccOutDroppedPkts = _CAal5VccOutDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2),
    _CAal5VccOutDroppedPkts_Type()
)
cAal5VccOutDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedPkts.setUnits("packets")
_CAal5VccInDroppedOctets_Type = Counter32
_CAal5VccInDroppedOctets_Object = MibTableColumn
cAal5VccInDroppedOctets = _CAal5VccInDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3),
    _CAal5VccInDroppedOctets_Type()
)
cAal5VccInDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInDroppedOctets.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInDroppedOctets.setUnits("octets")
_CAal5VccOutDroppedOctets_Type = Counter32
_CAal5VccOutDroppedOctets_Object = MibTableColumn
cAal5VccOutDroppedOctets = _CAal5VccOutDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4),
    _CAal5VccOutDroppedOctets_Type()
)
cAal5VccOutDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedOctets.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedOctets.setUnits("octets")
_CAal5VccInCells_Type = Counter32
_CAal5VccInCells_Object = MibTableColumn
cAal5VccInCells = _CAal5VccInCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5),
    _CAal5VccInCells_Type()
)
cAal5VccInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInCells.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInCells.setUnits("cells")
_CAal5VccOutCells_Type = Counter32
_CAal5VccOutCells_Object = MibTableColumn
cAal5VccOutCells = _CAal5VccOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 6),
    _CAal5VccOutCells_Type()
)
cAal5VccOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutCells.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutCells.setUnits("cells")
_CAal5VccInDroppedCells_Type = Counter32
_CAal5VccInDroppedCells_Object = MibTableColumn
cAal5VccInDroppedCells = _CAal5VccInDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 7),
    _CAal5VccInDroppedCells_Type()
)
cAal5VccInDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInDroppedCells.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInDroppedCells.setUnits("cells")
_CAal5VccOutDroppedCells_Type = Counter32
_CAal5VccOutDroppedCells_Object = MibTableColumn
cAal5VccOutDroppedCells = _CAal5VccOutDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 8),
    _CAal5VccOutDroppedCells_Type()
)
cAal5VccOutDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedCells.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedCells.setUnits("cells")
_CiscoAAL5ExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAAL5ExtMIBConformance = _CiscoAAL5ExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CiscoAAL5ExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAAL5ExtMIBCompliances = _CiscoAAL5ExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CiscoAAL5ExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAAL5ExtMIBGroups = _CiscoAAL5ExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)
aal5VccEntry.registerAugmentions(
    ("CISCO-AAL5-EXT-MIB",
     "cAal5ExtVccEntry")
)
cAal5ExtVccEntry.setIndexNames(*aal5VccEntry.getIndexNames())

# Managed Objects groups

ciscoAal5ExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)
)
ciscoAal5ExtMIBGroup.setObjects(
      *(("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedPkts"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedPkts"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedOctets"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedOctets"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccInCells"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccOutCells"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedCells"),
        ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedCells"))
)
if mibBuilder.loadTexts:
    ciscoAal5ExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAAL5ExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAAL5ExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAL5-EXT-MIB",
    **{"ciscoAal5ExtMIB": ciscoAal5ExtMIB,
       "ciscoAal5ExtMIBObjects": ciscoAal5ExtMIBObjects,
       "cAal5ExtConnections": cAal5ExtConnections,
       "cAal5ExtVccTable": cAal5ExtVccTable,
       "cAal5ExtVccEntry": cAal5ExtVccEntry,
       "cAal5VccInDroppedPkts": cAal5VccInDroppedPkts,
       "cAal5VccOutDroppedPkts": cAal5VccOutDroppedPkts,
       "cAal5VccInDroppedOctets": cAal5VccInDroppedOctets,
       "cAal5VccOutDroppedOctets": cAal5VccOutDroppedOctets,
       "cAal5VccInCells": cAal5VccInCells,
       "cAal5VccOutCells": cAal5VccOutCells,
       "cAal5VccInDroppedCells": cAal5VccInDroppedCells,
       "cAal5VccOutDroppedCells": cAal5VccOutDroppedCells,
       "ciscoAAL5ExtMIBConformance": ciscoAAL5ExtMIBConformance,
       "ciscoAAL5ExtMIBCompliances": ciscoAAL5ExtMIBCompliances,
       "ciscoAAL5ExtMIBCompliance": ciscoAAL5ExtMIBCompliance,
       "ciscoAAL5ExtMIBGroups": ciscoAAL5ExtMIBGroups,
       "ciscoAal5ExtMIBGroup": ciscoAal5ExtMIBGroup}
)
