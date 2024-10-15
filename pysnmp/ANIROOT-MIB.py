# SNMP MIB module (ANIROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANIROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:53 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 private) = mibBuilder.importSymbols(
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
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Ani_ObjectIdentity = ObjectIdentity
ani = _Ani_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325)
)
_Topology_ObjectIdentity = ObjectIdentity
topology = _Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 1)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2)
)
_AniDevBase_ObjectIdentity = ObjectIdentity
aniDevBase = _AniDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1)
)
_AniDevSoftware_ObjectIdentity = ObjectIdentity
aniDevSoftware = _AniDevSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2)
)
_AniDevHardware_ObjectIdentity = ObjectIdentity
aniDevHardware = _AniDevHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3)
)
_AniDevControl_ObjectIdentity = ObjectIdentity
aniDevControl = _AniDevControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4)
)
_AniDevServer_ObjectIdentity = ObjectIdentity
aniDevServer = _AniDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5)
)
_AniDevEvent_ObjectIdentity = ObjectIdentity
aniDevEvent = _AniDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6)
)
_AniDevNetworkManager_ObjectIdentity = ObjectIdentity
aniDevNetworkManager = _AniDevNetworkManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7)
)
_AniDevFilter_ObjectIdentity = ObjectIdentity
aniDevFilter = _AniDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 8)
)
_AniDevRoute_ObjectIdentity = ObjectIdentity
aniDevRoute = _AniDevRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9)
)
_AniDevTrap_ObjectIdentity = ObjectIdentity
aniDevTrap = _AniDevTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10)
)
_AniDevEthernet_ObjectIdentity = ObjectIdentity
aniDevEthernet = _AniDevEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11)
)
_Bsu_ObjectIdentity = ObjectIdentity
bsu = _Bsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3)
)
_AniBsuStatus_ObjectIdentity = ObjectIdentity
aniBsuStatus = _AniBsuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1)
)
_AniBsuWirelessIf_ObjectIdentity = ObjectIdentity
aniBsuWirelessIf = _AniBsuWirelessIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 2)
)
_AniBsuStatistics_ObjectIdentity = ObjectIdentity
aniBsuStatistics = _AniBsuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3)
)
_AniBsuClock_ObjectIdentity = ObjectIdentity
aniBsuClock = _AniBsuClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4)
)
_AniBsuBridge_ObjectIdentity = ObjectIdentity
aniBsuBridge = _AniBsuBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 5)
)
_AniBsuMultSubnets_ObjectIdentity = ObjectIdentity
aniBsuMultSubnets = _AniBsuMultSubnets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 6)
)
_AniBsuSuGroup_ObjectIdentity = ObjectIdentity
aniBsuSuGroup = _AniBsuSuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7)
)
_AniBsuSuInventory_ObjectIdentity = ObjectIdentity
aniBsuSuInventory = _AniBsuSuInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1)
)
_AniBsuSuBase_ObjectIdentity = ObjectIdentity
aniBsuSuBase = _AniBsuSuBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 2)
)
_AniBsuSuStatus_ObjectIdentity = ObjectIdentity
aniBsuSuStatus = _AniBsuSuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3)
)
_AniBsuSuStatistics_ObjectIdentity = ObjectIdentity
aniBsuSuStatistics = _AniBsuSuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4)
)
_AniBsuParam_ObjectIdentity = ObjectIdentity
aniBsuParam = _AniBsuParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 8)
)
_AniBsuVlan_ObjectIdentity = ObjectIdentity
aniBsuVlan = _AniBsuVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11)
)
_Su_ObjectIdentity = ObjectIdentity
su = _Su_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4)
)
_AniSuBase_ObjectIdentity = ObjectIdentity
aniSuBase = _AniSuBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 1)
)
_AniSuStatus_ObjectIdentity = ObjectIdentity
aniSuStatus = _AniSuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 2)
)
_AniSuStatistics_ObjectIdentity = ObjectIdentity
aniSuStatistics = _AniSuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 3)
)
_AniSuClassifier_ObjectIdentity = ObjectIdentity
aniSuClassifier = _AniSuClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 4)
)
_AniSuServiceFlow_ObjectIdentity = ObjectIdentity
aniSuServiceFlow = _AniSuServiceFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 5)
)
_AniSuNat_ObjectIdentity = ObjectIdentity
aniSuNat = _AniSuNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 6)
)
_AniSuDhcp_ObjectIdentity = ObjectIdentity
aniSuDhcp = _AniSuDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 7)
)
_AniSuPppoe_ObjectIdentity = ObjectIdentity
aniSuPppoe = _AniSuPppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 10)
)
_AniSuPpp_ObjectIdentity = ObjectIdentity
aniSuPpp = _AniSuPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 11)
)
_AniSuVlan_ObjectIdentity = ObjectIdentity
aniSuVlan = _AniSuVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 12)
)
_AniSuWireless_ObjectIdentity = ObjectIdentity
aniSuWireless = _AniSuWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 4, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANIROOT-MIB",
    **{"enterprises": enterprises,
       "ani": ani,
       "topology": topology,
       "device": device,
       "aniDevBase": aniDevBase,
       "aniDevSoftware": aniDevSoftware,
       "aniDevHardware": aniDevHardware,
       "aniDevControl": aniDevControl,
       "aniDevServer": aniDevServer,
       "aniDevEvent": aniDevEvent,
       "aniDevNetworkManager": aniDevNetworkManager,
       "aniDevFilter": aniDevFilter,
       "aniDevRoute": aniDevRoute,
       "aniDevTrap": aniDevTrap,
       "aniDevEthernet": aniDevEthernet,
       "bsu": bsu,
       "aniBsuStatus": aniBsuStatus,
       "aniBsuWirelessIf": aniBsuWirelessIf,
       "aniBsuStatistics": aniBsuStatistics,
       "aniBsuClock": aniBsuClock,
       "aniBsuBridge": aniBsuBridge,
       "aniBsuMultSubnets": aniBsuMultSubnets,
       "aniBsuSuGroup": aniBsuSuGroup,
       "aniBsuSuInventory": aniBsuSuInventory,
       "aniBsuSuBase": aniBsuSuBase,
       "aniBsuSuStatus": aniBsuSuStatus,
       "aniBsuSuStatistics": aniBsuSuStatistics,
       "aniBsuParam": aniBsuParam,
       "aniBsuVlan": aniBsuVlan,
       "su": su,
       "aniSuBase": aniSuBase,
       "aniSuStatus": aniSuStatus,
       "aniSuStatistics": aniSuStatistics,
       "aniSuClassifier": aniSuClassifier,
       "aniSuServiceFlow": aniSuServiceFlow,
       "aniSuNat": aniSuNat,
       "aniSuDhcp": aniSuDhcp,
       "aniSuPppoe": aniSuPppoe,
       "aniSuPpp": aniSuPpp,
       "aniSuVlan": aniSuVlan,
       "aniSuWireless": aniSuWireless}
)
