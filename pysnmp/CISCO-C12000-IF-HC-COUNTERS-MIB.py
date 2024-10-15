# SNMP MIB module (CISCO-C12000-IF-HC-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-C12000-IF-HC-COUNTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:28 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoC12000IfHcCountersMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CHCCounterMIBObjects_ObjectIdentity = ObjectIdentity
cHCCounterMIBObjects = _CHCCounterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1)
)
_CHCCounterTable_Object = MibTable
cHCCounterTable = _CHCCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1)
)
if mibBuilder.loadTexts:
    cHCCounterTable.setStatus("current")
_CHCCounterEntry_Object = MibTableRow
cHCCounterEntry = _CHCCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1)
)
cHCCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cHCCounterEntry.setStatus("current")
_CHCCounterIfInOctetsUpper_Type = Counter32
_CHCCounterIfInOctetsUpper_Object = MibTableColumn
cHCCounterIfInOctetsUpper = _CHCCounterIfInOctetsUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 1),
    _CHCCounterIfInOctetsUpper_Type()
)
cHCCounterIfInOctetsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfInOctetsUpper.setStatus("current")
_CHCCounterIfInOctetsLower_Type = Counter32
_CHCCounterIfInOctetsLower_Object = MibTableColumn
cHCCounterIfInOctetsLower = _CHCCounterIfInOctetsLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 2),
    _CHCCounterIfInOctetsLower_Type()
)
cHCCounterIfInOctetsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfInOctetsLower.setStatus("current")
_CHCCounterIfInUcastPktsUpper_Type = Counter32
_CHCCounterIfInUcastPktsUpper_Object = MibTableColumn
cHCCounterIfInUcastPktsUpper = _CHCCounterIfInUcastPktsUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 3),
    _CHCCounterIfInUcastPktsUpper_Type()
)
cHCCounterIfInUcastPktsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfInUcastPktsUpper.setStatus("current")
_CHCCounterIfInUcastPktsLower_Type = Counter32
_CHCCounterIfInUcastPktsLower_Object = MibTableColumn
cHCCounterIfInUcastPktsLower = _CHCCounterIfInUcastPktsLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 4),
    _CHCCounterIfInUcastPktsLower_Type()
)
cHCCounterIfInUcastPktsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfInUcastPktsLower.setStatus("current")
_CHCCounterIfOutOctetsUpper_Type = Counter32
_CHCCounterIfOutOctetsUpper_Object = MibTableColumn
cHCCounterIfOutOctetsUpper = _CHCCounterIfOutOctetsUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 5),
    _CHCCounterIfOutOctetsUpper_Type()
)
cHCCounterIfOutOctetsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfOutOctetsUpper.setStatus("current")
_CHCCounterIfOutOctetsLower_Type = Counter32
_CHCCounterIfOutOctetsLower_Object = MibTableColumn
cHCCounterIfOutOctetsLower = _CHCCounterIfOutOctetsLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 6),
    _CHCCounterIfOutOctetsLower_Type()
)
cHCCounterIfOutOctetsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfOutOctetsLower.setStatus("current")
_CHCCounterIfOutUcastPktsUpper_Type = Counter32
_CHCCounterIfOutUcastPktsUpper_Object = MibTableColumn
cHCCounterIfOutUcastPktsUpper = _CHCCounterIfOutUcastPktsUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 7),
    _CHCCounterIfOutUcastPktsUpper_Type()
)
cHCCounterIfOutUcastPktsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfOutUcastPktsUpper.setStatus("current")
_CHCCounterIfOutUcastPktsLower_Type = Counter32
_CHCCounterIfOutUcastPktsLower_Object = MibTableColumn
cHCCounterIfOutUcastPktsLower = _CHCCounterIfOutUcastPktsLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 1, 1, 1, 8),
    _CHCCounterIfOutUcastPktsLower_Type()
)
cHCCounterIfOutUcastPktsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHCCounterIfOutUcastPktsLower.setStatus("current")
_CiscoHCCountersMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoHCCountersMIBNotifications = _CiscoHCCountersMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 2)
)
_CiscoHCCountersMIBConformance_ObjectIdentity = ObjectIdentity
ciscoHCCountersMIBConformance = _CiscoHCCountersMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 3)
)
_CiscoHCCountersMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoHCCountersMIBCompliances = _CiscoHCCountersMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 1)
)
_CiscoHCCountersMIBGroups_ObjectIdentity = ObjectIdentity
ciscoHCCountersMIBGroups = _CiscoHCCountersMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 2)
)

# Managed Objects groups

ciscoHCCountersMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 2, 1)
)
ciscoHCCountersMIBGroup.setObjects(
      *(("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfInOctetsUpper"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfInOctetsLower"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfInUcastPktsUpper"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfInUcastPktsLower"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfOutOctetsUpper"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfOutOctetsLower"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfOutUcastPktsUpper"),
        ("CISCO-C12000-IF-HC-COUNTERS-MIB", "cHCCounterIfOutUcastPktsLower"))
)
if mibBuilder.loadTexts:
    ciscoHCCountersMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoHCCountersMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 31, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHCCountersMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-C12000-IF-HC-COUNTERS-MIB",
    **{"ciscoC12000IfHcCountersMIB": ciscoC12000IfHcCountersMIB,
       "cHCCounterMIBObjects": cHCCounterMIBObjects,
       "cHCCounterTable": cHCCounterTable,
       "cHCCounterEntry": cHCCounterEntry,
       "cHCCounterIfInOctetsUpper": cHCCounterIfInOctetsUpper,
       "cHCCounterIfInOctetsLower": cHCCounterIfInOctetsLower,
       "cHCCounterIfInUcastPktsUpper": cHCCounterIfInUcastPktsUpper,
       "cHCCounterIfInUcastPktsLower": cHCCounterIfInUcastPktsLower,
       "cHCCounterIfOutOctetsUpper": cHCCounterIfOutOctetsUpper,
       "cHCCounterIfOutOctetsLower": cHCCounterIfOutOctetsLower,
       "cHCCounterIfOutUcastPktsUpper": cHCCounterIfOutUcastPktsUpper,
       "cHCCounterIfOutUcastPktsLower": cHCCounterIfOutUcastPktsLower,
       "ciscoHCCountersMIBNotifications": ciscoHCCountersMIBNotifications,
       "ciscoHCCountersMIBConformance": ciscoHCCountersMIBConformance,
       "ciscoHCCountersMIBCompliances": ciscoHCCountersMIBCompliances,
       "ciscoHCCountersMIBCompliance": ciscoHCCountersMIBCompliance,
       "ciscoHCCountersMIBGroups": ciscoHCCountersMIBGroups,
       "ciscoHCCountersMIBGroup": ciscoHCCountersMIBGroup}
)
