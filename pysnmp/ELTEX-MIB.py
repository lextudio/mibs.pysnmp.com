# SNMP MIB module (ELTEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:08 2024
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

elt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265)
)
elt.setRevisions(
        ("2012-12-18 00:00",)
)


# Types definitions



class Percents(Integer32):
    """Custom type Percents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class VlanPriority(Integer32):
    """Custom type VlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltNotifications_ObjectIdentity = ObjectIdentity
eltNotifications = _EltNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 0)
)
if mibBuilder.loadTexts:
    eltNotifications.setStatus("current")
_EltMng_ObjectIdentity = ObjectIdentity
eltMng = _EltMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1)
)
_EltDevParams_ObjectIdentity = ObjectIdentity
eltDevParams = _EltDevParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 2)
)
_EltCopy_ObjectIdentity = ObjectIdentity
eltCopy = _EltCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3)
)
_EltIpOspfMtu_ObjectIdentity = ObjectIdentity
eltIpOspfMtu = _EltIpOspfMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 4)
)
_EltIpBfd_ObjectIdentity = ObjectIdentity
eltIpBfd = _EltIpBfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 6)
)
_EltIpUnnumbered_ObjectIdentity = ObjectIdentity
eltIpUnnumbered = _EltIpUnnumbered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 7)
)
_EltDhcp_ObjectIdentity = ObjectIdentity
eltDhcp = _EltDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 8)
)
_EltLinkAgg_ObjectIdentity = ObjectIdentity
eltLinkAgg = _EltLinkAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 9)
)
_EltQosTailDropMib_ObjectIdentity = ObjectIdentity
eltQosTailDropMib = _EltQosTailDropMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 12)
)
_EltTuning_ObjectIdentity = ObjectIdentity
eltTuning = _EltTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 29)
)
_EltSwInterfaces_ObjectIdentity = ObjectIdentity
eltSwInterfaces = _EltSwInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 43)
)
_EltIpMulticast_ObjectIdentity = ObjectIdentity
eltIpMulticast = _EltIpMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46)
)
_EltPhdTransceiver_ObjectIdentity = ObjectIdentity
eltPhdTransceiver = _EltPhdTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 53)
)
_EltMacMulticast_ObjectIdentity = ObjectIdentity
eltMacMulticast = _EltMacMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 55)
)
_EltStormCtrl_ObjectIdentity = ObjectIdentity
eltStormCtrl = _EltStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 77)
)
_EltRadius_ObjectIdentity = ObjectIdentity
eltRadius = _EltRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 80)
)
_EltQosCliMib_ObjectIdentity = ObjectIdentity
eltQosCliMib = _EltQosCliMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 88)
)
_EltPhy_ObjectIdentity = ObjectIdentity
eltPhy = _EltPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 90)
)
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 91)
)
_Eltdot1x_ObjectIdentity = ObjectIdentity
eltdot1x = _Eltdot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 95)
)
_EltBridgeSecurity_ObjectIdentity = ObjectIdentity
eltBridgeSecurity = _EltBridgeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 112)
)
_EltEndOfMibGroup_ObjectIdentity = ObjectIdentity
eltEndOfMibGroup = _EltEndOfMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MIB",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "VlanPriority": VlanPriority,
       "elt": elt,
       "eltNotifications": eltNotifications,
       "eltMng": eltMng,
       "eltDevParams": eltDevParams,
       "eltCopy": eltCopy,
       "eltIpOspfMtu": eltIpOspfMtu,
       "eltIpBfd": eltIpBfd,
       "eltIpUnnumbered": eltIpUnnumbered,
       "eltDhcp": eltDhcp,
       "eltLinkAgg": eltLinkAgg,
       "eltQosTailDropMib": eltQosTailDropMib,
       "eltTuning": eltTuning,
       "eltSwInterfaces": eltSwInterfaces,
       "eltIpMulticast": eltIpMulticast,
       "eltPhdTransceiver": eltPhdTransceiver,
       "eltMacMulticast": eltMacMulticast,
       "eltStormCtrl": eltStormCtrl,
       "eltRadius": eltRadius,
       "eltQosCliMib": eltQosCliMib,
       "eltPhy": eltPhy,
       "ipSpec": ipSpec,
       "eltdot1x": eltdot1x,
       "eltBridgeSecurity": eltBridgeSecurity,
       "eltEndOfMibGroup": eltEndOfMibGroup}
)
