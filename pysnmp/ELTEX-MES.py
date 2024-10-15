# SNMP MIB module (ELTEX-MES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:57 2024
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

(elHardware,
 eltexLtd) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware",
    "eltexLtd")

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

eltMes = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23)
)
eltMes.setRevisions(
        ("2015-11-17 00:00",)
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

_EltMesNotifications_ObjectIdentity = ObjectIdentity
eltMesNotifications = _EltMesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0)
)
if mibBuilder.loadTexts:
    eltMesNotifications.setStatus("current")
_EltMesMng_ObjectIdentity = ObjectIdentity
eltMesMng = _EltMesMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1)
)
_EltMesDevParams_ObjectIdentity = ObjectIdentity
eltMesDevParams = _EltMesDevParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 2)
)
_EltMesCopy_ObjectIdentity = ObjectIdentity
eltMesCopy = _EltMesCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3)
)
_EltMesIpOspfMtu_ObjectIdentity = ObjectIdentity
eltMesIpOspfMtu = _EltMesIpOspfMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4)
)
_EltMesIpBfd_ObjectIdentity = ObjectIdentity
eltMesIpBfd = _EltMesIpBfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 6)
)
_EltMesIpUnnumbered_ObjectIdentity = ObjectIdentity
eltMesIpUnnumbered = _EltMesIpUnnumbered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7)
)
_EltMesDhcp_ObjectIdentity = ObjectIdentity
eltMesDhcp = _EltMesDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8)
)
_EltMesLinkAgg_ObjectIdentity = ObjectIdentity
eltMesLinkAgg = _EltMesLinkAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9)
)
_EltMesQosTailDropMib_ObjectIdentity = ObjectIdentity
eltMesQosTailDropMib = _EltMesQosTailDropMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 12)
)
_EltMesTuning_ObjectIdentity = ObjectIdentity
eltMesTuning = _EltMesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 29)
)
_EltMesSwInterfaces_ObjectIdentity = ObjectIdentity
eltMesSwInterfaces = _EltMesSwInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 43)
)
_EltMesIpMulticast_ObjectIdentity = ObjectIdentity
eltMesIpMulticast = _EltMesIpMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 46)
)
_EltMesPhdTransceiver_ObjectIdentity = ObjectIdentity
eltMesPhdTransceiver = _EltMesPhdTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53)
)
_EltMesMacMulticast_ObjectIdentity = ObjectIdentity
eltMesMacMulticast = _EltMesMacMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55)
)
_EltMesStormCtrl_ObjectIdentity = ObjectIdentity
eltMesStormCtrl = _EltMesStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 77)
)
_EltMesAAA_ObjectIdentity = ObjectIdentity
eltMesAAA = _EltMesAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 79)
)
_EltMesRadius_ObjectIdentity = ObjectIdentity
eltMesRadius = _EltMesRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 80)
)
_EltMesSmon_ObjectIdentity = ObjectIdentity
eltMesSmon = _EltMesSmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84)
)
_EltMesQosCliMib_ObjectIdentity = ObjectIdentity
eltMesQosCliMib = _EltMesQosCliMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88)
)
_EltMesPhy_ObjectIdentity = ObjectIdentity
eltMesPhy = _EltMesPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90)
)
_EltMesIpSpec_ObjectIdentity = ObjectIdentity
eltMesIpSpec = _EltMesIpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91)
)
_EltMesDot1x_ObjectIdentity = ObjectIdentity
eltMesDot1x = _EltMesDot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95)
)
_EltMesBridgeSecurity_ObjectIdentity = ObjectIdentity
eltMesBridgeSecurity = _EltMesBridgeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 112)
)
_EltMesEndOfMibGroup_ObjectIdentity = ObjectIdentity
eltMesEndOfMibGroup = _EltMesEndOfMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "VlanPriority": VlanPriority,
       "eltMes": eltMes,
       "eltMesNotifications": eltMesNotifications,
       "eltMesMng": eltMesMng,
       "eltMesDevParams": eltMesDevParams,
       "eltMesCopy": eltMesCopy,
       "eltMesIpOspfMtu": eltMesIpOspfMtu,
       "eltMesIpBfd": eltMesIpBfd,
       "eltMesIpUnnumbered": eltMesIpUnnumbered,
       "eltMesDhcp": eltMesDhcp,
       "eltMesLinkAgg": eltMesLinkAgg,
       "eltMesQosTailDropMib": eltMesQosTailDropMib,
       "eltMesTuning": eltMesTuning,
       "eltMesSwInterfaces": eltMesSwInterfaces,
       "eltMesIpMulticast": eltMesIpMulticast,
       "eltMesPhdTransceiver": eltMesPhdTransceiver,
       "eltMesMacMulticast": eltMesMacMulticast,
       "eltMesStormCtrl": eltMesStormCtrl,
       "eltMesAAA": eltMesAAA,
       "eltMesRadius": eltMesRadius,
       "eltMesSmon": eltMesSmon,
       "eltMesQosCliMib": eltMesQosCliMib,
       "eltMesPhy": eltMesPhy,
       "eltMesIpSpec": eltMesIpSpec,
       "eltMesDot1x": eltMesDot1x,
       "eltMesBridgeSecurity": eltMesBridgeSecurity,
       "eltMesEndOfMibGroup": eltMesEndOfMibGroup}
)
