# SNMP MIB module (RUCKUS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:36 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ruckusRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusObjects_ObjectIdentity = ObjectIdentity
ruckusObjects = _RuckusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1)
)
_RuckusCommon_ObjectIdentity = ObjectIdentity
ruckusCommon = _RuckusCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1)
)
_RuckusCommonTCModule_ObjectIdentity = ObjectIdentity
ruckusCommonTCModule = _RuckusCommonTCModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1)
)
_RuckusCommonHwInfoModule_ObjectIdentity = ObjectIdentity
ruckusCommonHwInfoModule = _RuckusCommonHwInfoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 2)
)
_RuckusCommonSwInfoModule_ObjectIdentity = ObjectIdentity
ruckusCommonSwInfoModule = _RuckusCommonSwInfoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 3)
)
_RuckusCommonDeviceModule_ObjectIdentity = ObjectIdentity
ruckusCommonDeviceModule = _RuckusCommonDeviceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4)
)
_RuckusCommonUpgradeModule_ObjectIdentity = ObjectIdentity
ruckusCommonUpgradeModule = _RuckusCommonUpgradeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5)
)
_RuckusCommonWLANModule_ObjectIdentity = ObjectIdentity
ruckusCommonWLANModule = _RuckusCommonWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6)
)
_RuckusCommonPPPOEModule_ObjectIdentity = ObjectIdentity
ruckusCommonPPPOEModule = _RuckusCommonPPPOEModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8)
)
_RuckusCommonAdapterModule_ObjectIdentity = ObjectIdentity
ruckusCommonAdapterModule = _RuckusCommonAdapterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9)
)
_RuckusCommonSystemModule_ObjectIdentity = ObjectIdentity
ruckusCommonSystemModule = _RuckusCommonSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11)
)
_RuckusCommonRadioModule_ObjectIdentity = ObjectIdentity
ruckusCommonRadioModule = _RuckusCommonRadioModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12)
)
_RuckusCommonEthModule_ObjectIdentity = ObjectIdentity
ruckusCommonEthModule = _RuckusCommonEthModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 13)
)
_RuckusCommonL2TPModule_ObjectIdentity = ObjectIdentity
ruckusCommonL2TPModule = _RuckusCommonL2TPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 14)
)
_RuckusCommonWLINKModule_ObjectIdentity = ObjectIdentity
ruckusCommonWLINKModule = _RuckusCommonWLINKModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 15)
)
_RuckusZD_ObjectIdentity = ObjectIdentity
ruckusZD = _RuckusZD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2)
)
_RuckusZDSystemModule_ObjectIdentity = ObjectIdentity
ruckusZDSystemModule = _RuckusZDSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 1)
)
_RuckusZDWLANModule_ObjectIdentity = ObjectIdentity
ruckusZDWLANModule = _RuckusZDWLANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2)
)
_RuckusEvents_ObjectIdentity = ObjectIdentity
ruckusEvents = _RuckusEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2)
)
_RuckusProducts_ObjectIdentity = ObjectIdentity
ruckusProducts = _RuckusProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3)
)
_RuckusConformance_ObjectIdentity = ObjectIdentity
ruckusConformance = _RuckusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 4)
)
_RuckusConfGroups_ObjectIdentity = ObjectIdentity
ruckusConfGroups = _RuckusConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 4, 1)
)
_RuckusCompliances_ObjectIdentity = ObjectIdentity
ruckusCompliances = _RuckusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ROOT-MIB",
    **{"ruckusRootMIB": ruckusRootMIB,
       "ruckusObjects": ruckusObjects,
       "ruckusCommon": ruckusCommon,
       "ruckusCommonTCModule": ruckusCommonTCModule,
       "ruckusCommonHwInfoModule": ruckusCommonHwInfoModule,
       "ruckusCommonSwInfoModule": ruckusCommonSwInfoModule,
       "ruckusCommonDeviceModule": ruckusCommonDeviceModule,
       "ruckusCommonUpgradeModule": ruckusCommonUpgradeModule,
       "ruckusCommonWLANModule": ruckusCommonWLANModule,
       "ruckusCommonPPPOEModule": ruckusCommonPPPOEModule,
       "ruckusCommonAdapterModule": ruckusCommonAdapterModule,
       "ruckusCommonSystemModule": ruckusCommonSystemModule,
       "ruckusCommonRadioModule": ruckusCommonRadioModule,
       "ruckusCommonEthModule": ruckusCommonEthModule,
       "ruckusCommonL2TPModule": ruckusCommonL2TPModule,
       "ruckusCommonWLINKModule": ruckusCommonWLINKModule,
       "ruckusZD": ruckusZD,
       "ruckusZDSystemModule": ruckusZDSystemModule,
       "ruckusZDWLANModule": ruckusZDWLANModule,
       "ruckusEvents": ruckusEvents,
       "ruckusProducts": ruckusProducts,
       "ruckusConformance": ruckusConformance,
       "ruckusConfGroups": ruckusConfGroups,
       "ruckusCompliances": ruckusCompliances}
)
