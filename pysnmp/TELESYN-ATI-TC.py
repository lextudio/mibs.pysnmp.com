# SNMP MIB module (TELESYN-ATI-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TELESYN-ATI-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:45 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alliedtelesyn_ObjectIdentity = ObjectIdentity
alliedtelesyn = _Alliedtelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_SwitchingHubs_ObjectIdentity = ObjectIdentity
switchingHubs = _SwitchingHubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
_At_8200Switch_ObjectIdentity = ObjectIdentity
at_8200Switch = _At_8200Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 9)
)
_MibObjects_ObjectIdentity = ObjectIdentity
mibObjects = _MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_At8200SwitchMib_ObjectIdentity = ObjectIdentity
at8200SwitchMib = _At8200SwitchMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9)
)
_SwitchChassis_ObjectIdentity = ObjectIdentity
switchChassis = _SwitchChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1)
)
_SwitchMibModules_ObjectIdentity = ObjectIdentity
switchMibModules = _SwitchMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2)
)
_AtmModule_ObjectIdentity = ObjectIdentity
atmModule = _AtmModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1)
)
_BridgeModule_ObjectIdentity = ObjectIdentity
bridgeModule = _BridgeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2)
)
_FddiModule_ObjectIdentity = ObjectIdentity
fddiModule = _FddiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 3)
)
_IsdnModule_ObjectIdentity = ObjectIdentity
isdnModule = _IsdnModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 4)
)
_VLanModule_ObjectIdentity = ObjectIdentity
vLanModule = _VLanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5)
)
_AtiProducts_ObjectIdentity = ObjectIdentity
atiProducts = _AtiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 3)
)
_SwitchProduct_ObjectIdentity = ObjectIdentity
switchProduct = _SwitchProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 3, 1)
)
_AtiAgents_ObjectIdentity = ObjectIdentity
atiAgents = _AtiAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 100)
)
_UplinkSwitchAgent_ObjectIdentity = ObjectIdentity
uplinkSwitchAgent = _UplinkSwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 100, 1)
)
_SwitchAgent_ObjectIdentity = ObjectIdentity
switchAgent = _SwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 100, 2)
)
_AtiConventions_ObjectIdentity = ObjectIdentity
atiConventions = _AtiConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 200)
)
_SwitchVendor_ObjectIdentity = ObjectIdentity
switchVendor = _SwitchVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300)
)
_AtiAgentCapabilities_ObjectIdentity = ObjectIdentity
atiAgentCapabilities = _AtiAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELESYN-ATI-TC",
    **{"alliedtelesyn": alliedtelesyn,
       "products": products,
       "switchingHubs": switchingHubs,
       "at-8200Switch": at_8200Switch,
       "mibObjects": mibObjects,
       "at8200SwitchMib": at8200SwitchMib,
       "switchChassis": switchChassis,
       "switchMibModules": switchMibModules,
       "atmModule": atmModule,
       "bridgeModule": bridgeModule,
       "fddiModule": fddiModule,
       "isdnModule": isdnModule,
       "vLanModule": vLanModule,
       "atiProducts": atiProducts,
       "switchProduct": switchProduct,
       "atiAgents": atiAgents,
       "uplinkSwitchAgent": uplinkSwitchAgent,
       "switchAgent": switchAgent,
       "atiConventions": atiConventions,
       "switchVendor": switchVendor,
       "atiAgentCapabilities": atiAgentCapabilities}
)
