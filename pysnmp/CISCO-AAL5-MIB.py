# SNMP MIB module (CISCO-AAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAL5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:28 2024
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

ciscoAal5MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66)
)
ciscoAal5MIB.setRevisions(
        ("2003-09-22 00:00",
         "2002-10-17 00:00",
         "1996-11-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAal5MIBObjects_ObjectIdentity = ObjectIdentity
ciscoAal5MIBObjects = _CiscoAal5MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1)
)
_CAal5Connections_ObjectIdentity = ObjectIdentity
cAal5Connections = _CAal5Connections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1)
)
_CAal5VccTable_Object = MibTable
cAal5VccTable = _CAal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5VccTable.setStatus("current")
_CAal5VccEntry_Object = MibTableRow
cAal5VccEntry = _CAal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5VccEntry.setStatus("current")
_CAal5VccInPkts_Type = Counter32
_CAal5VccInPkts_Object = MibTableColumn
cAal5VccInPkts = _CAal5VccInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 1),
    _CAal5VccInPkts_Type()
)
cAal5VccInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInPkts.setUnits("packets")
_CAal5VccOutPkts_Type = Counter32
_CAal5VccOutPkts_Object = MibTableColumn
cAal5VccOutPkts = _CAal5VccOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 2),
    _CAal5VccOutPkts_Type()
)
cAal5VccOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutPkts.setUnits("packets")
_CAal5VccInOctets_Type = Counter32
_CAal5VccInOctets_Object = MibTableColumn
cAal5VccInOctets = _CAal5VccInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 3),
    _CAal5VccInOctets_Type()
)
cAal5VccInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccInOctets.setUnits("octets")
_CAal5VccOutOctets_Type = Counter32
_CAal5VccOutOctets_Object = MibTableColumn
cAal5VccOutOctets = _CAal5VccOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 4),
    _CAal5VccOutOctets_Type()
)
cAal5VccOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutOctets.setUnits("octets")
_CAal5VccInDroppedPkts_Type = Counter32
_CAal5VccInDroppedPkts_Object = MibTableColumn
cAal5VccInDroppedPkts = _CAal5VccInDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 8),
    _CAal5VccOutDroppedOctets_Type()
)
cAal5VccOutDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedOctets.setStatus("current")
if mibBuilder.loadTexts:
    cAal5VccOutDroppedOctets.setUnits("octets")
_CAal5VccHCInPkts_Type = Counter64
_CAal5VccHCInPkts_Object = MibTableColumn
cAal5VccHCInPkts = _CAal5VccHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 9),
    _CAal5VccHCInPkts_Type()
)
cAal5VccHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccHCInPkts.setStatus("current")
_CAal5VccHCOutPkts_Type = Counter64
_CAal5VccHCOutPkts_Object = MibTableColumn
cAal5VccHCOutPkts = _CAal5VccHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 10),
    _CAal5VccHCOutPkts_Type()
)
cAal5VccHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccHCOutPkts.setStatus("current")
_CAal5VccHCInOctets_Type = Counter64
_CAal5VccHCInOctets_Object = MibTableColumn
cAal5VccHCInOctets = _CAal5VccHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 11),
    _CAal5VccHCInOctets_Type()
)
cAal5VccHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccHCInOctets.setStatus("current")
_CAal5VccHCOutOctets_Type = Counter64
_CAal5VccHCOutOctets_Object = MibTableColumn
cAal5VccHCOutOctets = _CAal5VccHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 12),
    _CAal5VccHCOutOctets_Type()
)
cAal5VccHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccHCOutOctets.setStatus("current")
_CiscoAal5MIBConformance_ObjectIdentity = ObjectIdentity
ciscoAal5MIBConformance = _CiscoAal5MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3)
)
_CiscoAal5MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAal5MIBCompliances = _CiscoAal5MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1)
)
_CiscoAal5MIBGroups_ObjectIdentity = ObjectIdentity
ciscoAal5MIBGroups = _CiscoAal5MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2)
)
aal5VccEntry.registerAugmentions(
    ("CISCO-AAL5-MIB",
     "cAal5VccEntry")
)
cAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())

# Managed Objects groups

ciscoAal5MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 1)
)
ciscoAal5MIBGroup.setObjects(
      *(("CISCO-AAL5-MIB", "cAal5VccInPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccOutPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccInOctets"),
        ("CISCO-AAL5-MIB", "cAal5VccOutOctets"))
)
if mibBuilder.loadTexts:
    ciscoAal5MIBGroup.setStatus("current")

ciscoAal5VcStatsExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 2)
)
ciscoAal5VcStatsExtMIBGroup.setObjects(
      *(("CISCO-AAL5-MIB", "cAal5VccInDroppedPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccOutDroppedPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccInDroppedOctets"),
        ("CISCO-AAL5-MIB", "cAal5VccOutDroppedOctets"))
)
if mibBuilder.loadTexts:
    ciscoAal5VcStatsExtMIBGroup.setStatus("current")

ciscoAal5MIBHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 3)
)
ciscoAal5MIBHCGroup.setObjects(
      *(("CISCO-AAL5-MIB", "cAal5VccHCInPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccHCOutPkts"),
        ("CISCO-AAL5-MIB", "cAal5VccHCInOctets"),
        ("CISCO-AAL5-MIB", "cAal5VccHCOutOctets"))
)
if mibBuilder.loadTexts:
    ciscoAal5MIBHCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAal5MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAal5MIBCompliance.setStatus(
        "deprecated"
    )

ciscoAal5MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAal5MIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoAal5MIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAal5MIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAL5-MIB",
    **{"ciscoAal5MIB": ciscoAal5MIB,
       "ciscoAal5MIBObjects": ciscoAal5MIBObjects,
       "cAal5Connections": cAal5Connections,
       "cAal5VccTable": cAal5VccTable,
       "cAal5VccEntry": cAal5VccEntry,
       "cAal5VccInPkts": cAal5VccInPkts,
       "cAal5VccOutPkts": cAal5VccOutPkts,
       "cAal5VccInOctets": cAal5VccInOctets,
       "cAal5VccOutOctets": cAal5VccOutOctets,
       "cAal5VccInDroppedPkts": cAal5VccInDroppedPkts,
       "cAal5VccOutDroppedPkts": cAal5VccOutDroppedPkts,
       "cAal5VccInDroppedOctets": cAal5VccInDroppedOctets,
       "cAal5VccOutDroppedOctets": cAal5VccOutDroppedOctets,
       "cAal5VccHCInPkts": cAal5VccHCInPkts,
       "cAal5VccHCOutPkts": cAal5VccHCOutPkts,
       "cAal5VccHCInOctets": cAal5VccHCInOctets,
       "cAal5VccHCOutOctets": cAal5VccHCOutOctets,
       "ciscoAal5MIBConformance": ciscoAal5MIBConformance,
       "ciscoAal5MIBCompliances": ciscoAal5MIBCompliances,
       "ciscoAal5MIBCompliance": ciscoAal5MIBCompliance,
       "ciscoAal5MIBComplianceRev1": ciscoAal5MIBComplianceRev1,
       "ciscoAal5MIBComplianceRev2": ciscoAal5MIBComplianceRev2,
       "ciscoAal5MIBGroups": ciscoAal5MIBGroups,
       "ciscoAal5MIBGroup": ciscoAal5MIBGroup,
       "ciscoAal5VcStatsExtMIBGroup": ciscoAal5VcStatsExtMIBGroup,
       "ciscoAal5MIBHCGroup": ciscoAal5MIBHCGroup}
)
