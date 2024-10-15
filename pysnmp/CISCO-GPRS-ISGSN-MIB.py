# SNMP MIB module (CISCO-GPRS-ISGSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GPRS-ISGSN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:57 2024
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

ciscoGprsIsgsnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGprsIsgsnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGprsIsgsnMIBObjects = _CiscoGprsIsgsnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1)
)
_CiscoGprsIsgsnStats_ObjectIdentity = ObjectIdentity
ciscoGprsIsgsnStats = _CiscoGprsIsgsnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1)
)
_CgprsIsgsnRxPacketCountFromTnode_Type = Counter32
_CgprsIsgsnRxPacketCountFromTnode_Object = MibScalar
cgprsIsgsnRxPacketCountFromTnode = _CgprsIsgsnRxPacketCountFromTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 1),
    _CgprsIsgsnRxPacketCountFromTnode_Type()
)
cgprsIsgsnRxPacketCountFromTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnRxPacketCountFromTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnRxPacketCountFromTnode.setUnits("packets")
_CgprsIsgsnTxPacketCountToTnode_Type = Counter32
_CgprsIsgsnTxPacketCountToTnode_Object = MibScalar
cgprsIsgsnTxPacketCountToTnode = _CgprsIsgsnTxPacketCountToTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 2),
    _CgprsIsgsnTxPacketCountToTnode_Type()
)
cgprsIsgsnTxPacketCountToTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnTxPacketCountToTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnTxPacketCountToTnode.setUnits("packets")
_CgprsIsgsnRxOctetCountFromTnode_Type = Counter32
_CgprsIsgsnRxOctetCountFromTnode_Object = MibScalar
cgprsIsgsnRxOctetCountFromTnode = _CgprsIsgsnRxOctetCountFromTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 3),
    _CgprsIsgsnRxOctetCountFromTnode_Type()
)
cgprsIsgsnRxOctetCountFromTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnRxOctetCountFromTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnRxOctetCountFromTnode.setUnits("bytes")
_CgprsIsgsnTxOctetCountToTnode_Type = Counter32
_CgprsIsgsnTxOctetCountToTnode_Object = MibScalar
cgprsIsgsnTxOctetCountToTnode = _CgprsIsgsnTxOctetCountToTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 4),
    _CgprsIsgsnTxOctetCountToTnode_Type()
)
cgprsIsgsnTxOctetCountToTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnTxOctetCountToTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnTxOctetCountToTnode.setUnits("bytes")
_CgprsIsgsnErrorCountRxFromTnode_Type = Counter32
_CgprsIsgsnErrorCountRxFromTnode_Object = MibScalar
cgprsIsgsnErrorCountRxFromTnode = _CgprsIsgsnErrorCountRxFromTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 5),
    _CgprsIsgsnErrorCountRxFromTnode_Type()
)
cgprsIsgsnErrorCountRxFromTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnErrorCountRxFromTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnErrorCountRxFromTnode.setUnits("packets")
_CgprsIsgsnErrorCountRxToTnode_Type = Counter32
_CgprsIsgsnErrorCountRxToTnode_Object = MibScalar
cgprsIsgsnErrorCountRxToTnode = _CgprsIsgsnErrorCountRxToTnode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 6),
    _CgprsIsgsnErrorCountRxToTnode_Type()
)
cgprsIsgsnErrorCountRxToTnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsIsgsnErrorCountRxToTnode.setStatus("current")
if mibBuilder.loadTexts:
    cgprsIsgsnErrorCountRxToTnode.setUnits("packets")
_CiscoGprsIsgsnConformances_ObjectIdentity = ObjectIdentity
ciscoGprsIsgsnConformances = _CiscoGprsIsgsnConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 3)
)
_CgprsIsgsnGroups_ObjectIdentity = ObjectIdentity
cgprsIsgsnGroups = _CgprsIsgsnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1)
)
_CgprsIsgsnCompliances_ObjectIdentity = ObjectIdentity
cgprsIsgsnCompliances = _CgprsIsgsnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2)
)

# Managed Objects groups

cgprsIsgsnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1, 1)
)
cgprsIsgsnStatsGroup.setObjects(
      *(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxPacketCountFromTnode"),
        ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxPacketCountToTnode"),
        ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxOctetCountFromTnode"),
        ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxOctetCountToTnode"),
        ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxFromTnode"),
        ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxToTnode"))
)
if mibBuilder.loadTexts:
    cgprsIsgsnStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cgprsIsgsnCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cgprsIsgsnCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GPRS-ISGSN-MIB",
    **{"ciscoGprsIsgsnMIB": ciscoGprsIsgsnMIB,
       "ciscoGprsIsgsnMIBObjects": ciscoGprsIsgsnMIBObjects,
       "ciscoGprsIsgsnStats": ciscoGprsIsgsnStats,
       "cgprsIsgsnRxPacketCountFromTnode": cgprsIsgsnRxPacketCountFromTnode,
       "cgprsIsgsnTxPacketCountToTnode": cgprsIsgsnTxPacketCountToTnode,
       "cgprsIsgsnRxOctetCountFromTnode": cgprsIsgsnRxOctetCountFromTnode,
       "cgprsIsgsnTxOctetCountToTnode": cgprsIsgsnTxOctetCountToTnode,
       "cgprsIsgsnErrorCountRxFromTnode": cgprsIsgsnErrorCountRxFromTnode,
       "cgprsIsgsnErrorCountRxToTnode": cgprsIsgsnErrorCountRxToTnode,
       "ciscoGprsIsgsnConformances": ciscoGprsIsgsnConformances,
       "cgprsIsgsnGroups": cgprsIsgsnGroups,
       "cgprsIsgsnStatsGroup": cgprsIsgsnStatsGroup,
       "cgprsIsgsnCompliances": cgprsIsgsnCompliances,
       "cgprsIsgsnCompliance1": cgprsIsgsnCompliance1}
)
