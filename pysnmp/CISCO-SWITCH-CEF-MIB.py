# SNMP MIB module (CISCO-SWITCH-CEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-CEF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:03 2024
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

ciscoSwitchCefMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790)
)
ciscoSwitchCefMIB.setRevisions(
        ("2011-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchCefMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchCefMIBNotifs = _CiscoSwitchCefMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 0)
)
_CiscoSwitchCefMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchCefMIBObjects = _CiscoSwitchCefMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1)
)
_CscStats_ObjectIdentity = ObjectIdentity
cscStats = _CscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1)
)
_CscSwitchCefStatsTable_Object = MibTable
cscSwitchCefStatsTable = _CscSwitchCefStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cscSwitchCefStatsTable.setStatus("current")
_CscSwitchCefStatsEntry_Object = MibTableRow
cscSwitchCefStatsEntry = _CscSwitchCefStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1)
)
cscSwitchCefStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cscSwitchCefStatsEntry.setStatus("current")
_CscIpv4NonVrfRoutes_Type = Gauge32
_CscIpv4NonVrfRoutes_Object = MibTableColumn
cscIpv4NonVrfRoutes = _CscIpv4NonVrfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 1),
    _CscIpv4NonVrfRoutes_Type()
)
cscIpv4NonVrfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv4NonVrfRoutes.setStatus("current")
_CscIpv4VrfRoutes_Type = Gauge32
_CscIpv4VrfRoutes_Object = MibTableColumn
cscIpv4VrfRoutes = _CscIpv4VrfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 2),
    _CscIpv4VrfRoutes_Type()
)
cscIpv4VrfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv4VrfRoutes.setStatus("current")
_CscIpv4MulticastRoutes_Type = Gauge32
_CscIpv4MulticastRoutes_Object = MibTableColumn
cscIpv4MulticastRoutes = _CscIpv4MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 3),
    _CscIpv4MulticastRoutes_Type()
)
cscIpv4MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv4MulticastRoutes.setStatus("current")
_CscIpv4UnicastRoutes_Type = Gauge32
_CscIpv4UnicastRoutes_Object = MibTableColumn
cscIpv4UnicastRoutes = _CscIpv4UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 4),
    _CscIpv4UnicastRoutes_Type()
)
cscIpv4UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv4UnicastRoutes.setStatus("current")
_CscIpv6GlobalRoutes_Type = Gauge32
_CscIpv6GlobalRoutes_Object = MibTableColumn
cscIpv6GlobalRoutes = _CscIpv6GlobalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 5),
    _CscIpv6GlobalRoutes_Type()
)
cscIpv6GlobalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6GlobalRoutes.setStatus("current")
_CscIpv6NonVrfRoutes_Type = Gauge32
_CscIpv6NonVrfRoutes_Object = MibTableColumn
cscIpv6NonVrfRoutes = _CscIpv6NonVrfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 6),
    _CscIpv6NonVrfRoutes_Type()
)
cscIpv6NonVrfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6NonVrfRoutes.setStatus("current")
_CscIpv6VrfRoutes_Type = Gauge32
_CscIpv6VrfRoutes_Object = MibTableColumn
cscIpv6VrfRoutes = _CscIpv6VrfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 7),
    _CscIpv6VrfRoutes_Type()
)
cscIpv6VrfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6VrfRoutes.setStatus("current")
_CscIpv6LinkLocalRoutes_Type = Gauge32
_CscIpv6LinkLocalRoutes_Object = MibTableColumn
cscIpv6LinkLocalRoutes = _CscIpv6LinkLocalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 8),
    _CscIpv6LinkLocalRoutes_Type()
)
cscIpv6LinkLocalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6LinkLocalRoutes.setStatus("current")
_CscIpv6MulticastRoutes_Type = Gauge32
_CscIpv6MulticastRoutes_Object = MibTableColumn
cscIpv6MulticastRoutes = _CscIpv6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 9),
    _CscIpv6MulticastRoutes_Type()
)
cscIpv6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6MulticastRoutes.setStatus("current")
_CscIpv6UnicastRoutes_Type = Gauge32
_CscIpv6UnicastRoutes_Object = MibTableColumn
cscIpv6UnicastRoutes = _CscIpv6UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 10),
    _CscIpv6UnicastRoutes_Type()
)
cscIpv6UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscIpv6UnicastRoutes.setStatus("current")
_CscMplsRoutes_Type = Gauge32
_CscMplsRoutes_Object = MibTableColumn
cscMplsRoutes = _CscMplsRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 11),
    _CscMplsRoutes_Type()
)
cscMplsRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscMplsRoutes.setStatus("current")
_CscMplsVpnRoutes_Type = Gauge32
_CscMplsVpnRoutes_Object = MibTableColumn
cscMplsVpnRoutes = _CscMplsVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 12),
    _CscMplsVpnRoutes_Type()
)
cscMplsVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscMplsVpnRoutes.setStatus("current")
_CscEomL2Routes_Type = Gauge32
_CscEomL2Routes_Object = MibTableColumn
cscEomL2Routes = _CscEomL2Routes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 13),
    _CscEomL2Routes_Type()
)
cscEomL2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscEomL2Routes.setStatus("current")
_CscEomIpv4MulticastRoutes_Type = Gauge32
_CscEomIpv4MulticastRoutes_Object = MibTableColumn
cscEomIpv4MulticastRoutes = _CscEomIpv4MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 14),
    _CscEomIpv4MulticastRoutes_Type()
)
cscEomIpv4MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscEomIpv4MulticastRoutes.setStatus("current")
_CscEomIpv6MulticastRoutes_Type = Gauge32
_CscEomIpv6MulticastRoutes_Object = MibTableColumn
cscEomIpv6MulticastRoutes = _CscEomIpv6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 15),
    _CscEomIpv6MulticastRoutes_Type()
)
cscEomIpv6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscEomIpv6MulticastRoutes.setStatus("current")
_CscTotalRoutes_Type = Gauge32
_CscTotalRoutes_Object = MibTableColumn
cscTotalRoutes = _CscTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 1, 1, 1, 1, 16),
    _CscTotalRoutes_Type()
)
cscTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTotalRoutes.setStatus("current")
_CiscoSwitchCefMIBConform_ObjectIdentity = ObjectIdentity
ciscoSwitchCefMIBConform = _CiscoSwitchCefMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2)
)
_CscSwitchCefMIBCompliances_ObjectIdentity = ObjectIdentity
cscSwitchCefMIBCompliances = _CscSwitchCefMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 1)
)
_CscSwitchCefMIBGroups_ObjectIdentity = ObjectIdentity
cscSwitchCefMIBGroups = _CscSwitchCefMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2)
)

# Managed Objects groups

cscSwitchCefIpv4StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 1)
)
cscSwitchCefIpv4StatsGroup.setObjects(
      *(("CISCO-SWITCH-CEF-MIB", "cscIpv4NonVrfRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv4VrfRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv4MulticastRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv4UnicastRoutes"))
)
if mibBuilder.loadTexts:
    cscSwitchCefIpv4StatsGroup.setStatus("current")

cscSwitchCefIpv6StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 2)
)
cscSwitchCefIpv6StatsGroup.setObjects(
      *(("CISCO-SWITCH-CEF-MIB", "cscIpv6NonVrfRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv6VrfRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv6MulticastRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscIpv6UnicastRoutes"))
)
if mibBuilder.loadTexts:
    cscSwitchCefIpv6StatsGroup.setStatus("current")

cscSwitchCefIpv6GlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 3)
)
cscSwitchCefIpv6GlobalStatsGroup.setObjects(
    ("CISCO-SWITCH-CEF-MIB", "cscIpv6GlobalRoutes")
)
if mibBuilder.loadTexts:
    cscSwitchCefIpv6GlobalStatsGroup.setStatus("current")

cscSwitchCefIpv6LinkLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 4)
)
cscSwitchCefIpv6LinkLocalGroup.setObjects(
    ("CISCO-SWITCH-CEF-MIB", "cscIpv6LinkLocalRoutes")
)
if mibBuilder.loadTexts:
    cscSwitchCefIpv6LinkLocalGroup.setStatus("current")

cscSwitchCefEomL2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 5)
)
cscSwitchCefEomL2Group.setObjects(
    ("CISCO-SWITCH-CEF-MIB", "cscEomL2Routes")
)
if mibBuilder.loadTexts:
    cscSwitchCefEomL2Group.setStatus("current")

cscMplsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 6)
)
cscMplsStatsGroup.setObjects(
    ("CISCO-SWITCH-CEF-MIB", "cscMplsRoutes")
)
if mibBuilder.loadTexts:
    cscMplsStatsGroup.setStatus("current")

cscMplsStatsGroupExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 7)
)
cscMplsStatsGroupExt.setObjects(
      *(("CISCO-SWITCH-CEF-MIB", "cscMplsVpnRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscEomIpv4MulticastRoutes"),
        ("CISCO-SWITCH-CEF-MIB", "cscEomIpv6MulticastRoutes"))
)
if mibBuilder.loadTexts:
    cscMplsStatsGroupExt.setStatus("current")

cscTotalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 2, 8)
)
cscTotalStatsGroup.setObjects(
    ("CISCO-SWITCH-CEF-MIB", "cscTotalRoutes")
)
if mibBuilder.loadTexts:
    cscTotalStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cscSwitchCefMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 790, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cscSwitchCefMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-CEF-MIB",
    **{"ciscoSwitchCefMIB": ciscoSwitchCefMIB,
       "ciscoSwitchCefMIBNotifs": ciscoSwitchCefMIBNotifs,
       "ciscoSwitchCefMIBObjects": ciscoSwitchCefMIBObjects,
       "cscStats": cscStats,
       "cscSwitchCefStatsTable": cscSwitchCefStatsTable,
       "cscSwitchCefStatsEntry": cscSwitchCefStatsEntry,
       "cscIpv4NonVrfRoutes": cscIpv4NonVrfRoutes,
       "cscIpv4VrfRoutes": cscIpv4VrfRoutes,
       "cscIpv4MulticastRoutes": cscIpv4MulticastRoutes,
       "cscIpv4UnicastRoutes": cscIpv4UnicastRoutes,
       "cscIpv6GlobalRoutes": cscIpv6GlobalRoutes,
       "cscIpv6NonVrfRoutes": cscIpv6NonVrfRoutes,
       "cscIpv6VrfRoutes": cscIpv6VrfRoutes,
       "cscIpv6LinkLocalRoutes": cscIpv6LinkLocalRoutes,
       "cscIpv6MulticastRoutes": cscIpv6MulticastRoutes,
       "cscIpv6UnicastRoutes": cscIpv6UnicastRoutes,
       "cscMplsRoutes": cscMplsRoutes,
       "cscMplsVpnRoutes": cscMplsVpnRoutes,
       "cscEomL2Routes": cscEomL2Routes,
       "cscEomIpv4MulticastRoutes": cscEomIpv4MulticastRoutes,
       "cscEomIpv6MulticastRoutes": cscEomIpv6MulticastRoutes,
       "cscTotalRoutes": cscTotalRoutes,
       "ciscoSwitchCefMIBConform": ciscoSwitchCefMIBConform,
       "cscSwitchCefMIBCompliances": cscSwitchCefMIBCompliances,
       "cscSwitchCefMIBCompliance": cscSwitchCefMIBCompliance,
       "cscSwitchCefMIBGroups": cscSwitchCefMIBGroups,
       "cscSwitchCefIpv4StatsGroup": cscSwitchCefIpv4StatsGroup,
       "cscSwitchCefIpv6StatsGroup": cscSwitchCefIpv6StatsGroup,
       "cscSwitchCefIpv6GlobalStatsGroup": cscSwitchCefIpv6GlobalStatsGroup,
       "cscSwitchCefIpv6LinkLocalGroup": cscSwitchCefIpv6LinkLocalGroup,
       "cscSwitchCefEomL2Group": cscSwitchCefEomL2Group,
       "cscMplsStatsGroup": cscMplsStatsGroup,
       "cscMplsStatsGroupExt": cscMplsStatsGroupExt,
       "cscTotalStatsGroup": cscTotalStatsGroup}
)
