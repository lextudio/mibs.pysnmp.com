# SNMP MIB module (CISCO-NAT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NAT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:03 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

ciscoNATExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532)
)
ciscoNATExtMIB.setRevisions(
        ("2006-06-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNatExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNatExtMIBNotifs = _CiscoNatExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 0)
)
_CiscoNatExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNatExtMIBObjects = _CiscoNatExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1)
)
_CneAddrTranslationStatsTable_Object = MibTable
cneAddrTranslationStatsTable = _CneAddrTranslationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1)
)
if mibBuilder.loadTexts:
    cneAddrTranslationStatsTable.setStatus("current")
_CneAddrTranslationStatsEntry_Object = MibTableRow
cneAddrTranslationStatsEntry = _CneAddrTranslationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1)
)
cneAddrTranslationStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cneAddrTranslationStatsEntry.setStatus("current")
_CneAddrTranslationNumActive_Type = Gauge32
_CneAddrTranslationNumActive_Object = MibTableColumn
cneAddrTranslationNumActive = _CneAddrTranslationNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1),
    _CneAddrTranslationNumActive_Type()
)
cneAddrTranslationNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneAddrTranslationNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cneAddrTranslationNumActive.setUnits("Number of address translation entries")
_CneAddrTranslationNumPeak_Type = Unsigned32
_CneAddrTranslationNumPeak_Object = MibTableColumn
cneAddrTranslationNumPeak = _CneAddrTranslationNumPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2),
    _CneAddrTranslationNumPeak_Type()
)
cneAddrTranslationNumPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneAddrTranslationNumPeak.setStatus("current")
if mibBuilder.loadTexts:
    cneAddrTranslationNumPeak.setUnits("Number of address translation entries")
_CneAddrTranslation1min_Type = Gauge32
_CneAddrTranslation1min_Object = MibTableColumn
cneAddrTranslation1min = _CneAddrTranslation1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3),
    _CneAddrTranslation1min_Type()
)
cneAddrTranslation1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneAddrTranslation1min.setStatus("current")
if mibBuilder.loadTexts:
    cneAddrTranslation1min.setUnits("Address translation entries per second")
_CneAddrTranslation5min_Type = Gauge32
_CneAddrTranslation5min_Object = MibTableColumn
cneAddrTranslation5min = _CneAddrTranslation5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4),
    _CneAddrTranslation5min_Type()
)
cneAddrTranslation5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cneAddrTranslation5min.setStatus("current")
if mibBuilder.loadTexts:
    cneAddrTranslation5min.setUnits("Address translation entries per second")
_CiscoNatExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNatExtMIBConformance = _CiscoNatExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 2)
)
_CiscoNatExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNatExtMIBCompliances = _CiscoNatExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1)
)
_CiscoNatExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNatExtMIBGroups = _CiscoNatExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2)
)

# Managed Objects groups

ciscoNatExtAddrTransStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)
)
ciscoNatExtAddrTransStatsGroup.setObjects(
      *(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"),
        ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"),
        ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"),
        ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
)
if mibBuilder.loadTexts:
    ciscoNatExtAddrTransStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNatExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNatExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NAT-EXT-MIB",
    **{"ciscoNATExtMIB": ciscoNATExtMIB,
       "ciscoNatExtMIBNotifs": ciscoNatExtMIBNotifs,
       "ciscoNatExtMIBObjects": ciscoNatExtMIBObjects,
       "cneAddrTranslationStatsTable": cneAddrTranslationStatsTable,
       "cneAddrTranslationStatsEntry": cneAddrTranslationStatsEntry,
       "cneAddrTranslationNumActive": cneAddrTranslationNumActive,
       "cneAddrTranslationNumPeak": cneAddrTranslationNumPeak,
       "cneAddrTranslation1min": cneAddrTranslation1min,
       "cneAddrTranslation5min": cneAddrTranslation5min,
       "ciscoNatExtMIBConformance": ciscoNatExtMIBConformance,
       "ciscoNatExtMIBCompliances": ciscoNatExtMIBCompliances,
       "ciscoNatExtMIBCompliance": ciscoNatExtMIBCompliance,
       "ciscoNatExtMIBGroups": ciscoNatExtMIBGroups,
       "ciscoNatExtAddrTransStatsGroup": ciscoNatExtAddrTransStatsGroup}
)
