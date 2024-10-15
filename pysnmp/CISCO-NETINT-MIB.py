# SNMP MIB module (CISCO-NETINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NETINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:10 2024
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

ciscoNetintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490)
)
ciscoNetintMIB.setRevisions(
        ("2005-09-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNetintMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetintMIBNotifs = _CiscoNetintMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 0)
)
_CiscoNetintMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetintMIBObjects = _CiscoNetintMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1)
)
_CniThrottle_ObjectIdentity = ObjectIdentity
cniThrottle = _CniThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1)
)
_CniThrottleTable_Object = MibTable
cniThrottleTable = _CniThrottleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cniThrottleTable.setStatus("current")
_CniThrottleEntry_Object = MibTableRow
cniThrottleEntry = _CniThrottleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1)
)
cniThrottleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cniThrottleEntry.setStatus("current")
_CniThrottleCount_Type = Counter32
_CniThrottleCount_Object = MibTableColumn
cniThrottleCount = _CniThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1),
    _CniThrottleCount_Type()
)
cniThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cniThrottleCount.setStatus("current")
_CiscoNetintMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNetintMIBConformance = _CiscoNetintMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2)
)
_CiscoNetintMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetintMIBCompliances = _CiscoNetintMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1)
)
_CiscoNetintMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetintMIBGroups = _CiscoNetintMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2)
)

# Managed Objects groups

ciscoThrottleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)
)
ciscoThrottleGroup.setObjects(
    ("CISCO-NETINT-MIB", "cniThrottleCount")
)
if mibBuilder.loadTexts:
    ciscoThrottleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNetintMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNetintMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETINT-MIB",
    **{"ciscoNetintMIB": ciscoNetintMIB,
       "ciscoNetintMIBNotifs": ciscoNetintMIBNotifs,
       "ciscoNetintMIBObjects": ciscoNetintMIBObjects,
       "cniThrottle": cniThrottle,
       "cniThrottleTable": cniThrottleTable,
       "cniThrottleEntry": cniThrottleEntry,
       "cniThrottleCount": cniThrottleCount,
       "ciscoNetintMIBConformance": ciscoNetintMIBConformance,
       "ciscoNetintMIBCompliances": ciscoNetintMIBCompliances,
       "ciscoNetintMIBCompliance": ciscoNetintMIBCompliance,
       "ciscoNetintMIBGroups": ciscoNetintMIBGroups,
       "ciscoThrottleGroup": ciscoThrottleGroup}
)
