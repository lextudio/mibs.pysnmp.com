# SNMP MIB module (Unisphere-Data-Internet-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-Internet-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:02 2024
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

(ipCidrRouteIfIndex,
 ipCidrRouteInfo,
 ipCidrRouteMetric1,
 ipCidrRouteMetric2,
 ipCidrRouteMetric3,
 ipCidrRouteMetric4,
 ipCidrRouteMetric5,
 ipCidrRouteNextHopAS,
 ipCidrRouteStatus,
 ipCidrRouteType,
 ipForwardCidrRouteGroup) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteIfIndex",
    "ipCidrRouteInfo",
    "ipCidrRouteMetric1",
    "ipCidrRouteMetric2",
    "ipCidrRouteMetric3",
    "ipCidrRouteMetric4",
    "ipCidrRouteMetric5",
    "ipCidrRouteNextHopAS",
    "ipCidrRouteStatus",
    "ipCidrRouteType",
    "ipForwardCidrRouteGroup")

(icmpGroup,
 ipGroup,
 ipNetToMediaIfIndex,
 ipNetToMediaNetAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "icmpGroup",
    "ipGroup",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress")

(ipRouteAge,
 ipRouteDest,
 ipRouteEntry,
 ipRouteIfIndex,
 ipRouteMask,
 ipRouteMetric1,
 ipRouteMetric2,
 ipRouteMetric3,
 ipRouteMetric4,
 ipRouteMetric5,
 ipRouteNextHop,
 ipRouteType) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "ipRouteAge",
    "ipRouteDest",
    "ipRouteEntry",
    "ipRouteIfIndex",
    "ipRouteMask",
    "ipRouteMetric1",
    "ipRouteMetric2",
    "ipRouteMetric3",
    "ipRouteMetric4",
    "ipRouteMetric5",
    "ipRouteNextHop",
    "ipRouteType")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(tcpGroup,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpGroup")

(udpGroup,) = mibBuilder.importSymbols(
    "UDP-MIB",
    "udpGroup")

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdHostGroup,) = mibBuilder.importSymbols(
    "Unisphere-Data-HOST-MIB",
    "usdHostGroup")

(usdIpAddressGroup,
 usdIpAddressGroup2,
 usdIpGlobalGroup,
 usdIpInterfaceGroup,
 usdIpInterfaceGroup2,
 usdIpInterfaceGroup3,
 usdIpInterfaceGroup4,
 usdIpRouteGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-IP-MIB",
    "usdIpAddressGroup",
    "usdIpAddressGroup2",
    "usdIpGlobalGroup",
    "usdIpInterfaceGroup",
    "usdIpInterfaceGroup2",
    "usdIpInterfaceGroup3",
    "usdIpInterfaceGroup4",
    "usdIpRouteGroup")


# MODULE-IDENTITY

usdInternetAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21)
)
usdInternetAgent.setRevisions(
        ("2002-04-03 14:04",
         "2002-03-26 21:46")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdInternetAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 1)
)
if mibBuilder.loadTexts:
    usdInternetAgentV1.setProductRelease("""\
Version 1 of the Internet component of the Unisphere Routing Switch
        SNMP agent.  This version of the Internet component was supported in the
        Unisphere 2.x system releases.""")
if mibBuilder.loadTexts:
    usdInternetAgentV1.setStatus(
        "obsolete"
    )

usdInternetAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 2)
)
if mibBuilder.loadTexts:
    usdInternetAgentV2.setProductRelease("""\
Version 2 of the Internet component of the Unisphere Routing Switch
        SNMP agent.  This version of the Internet component was supported in the
        Unisphere RX 3.0 and RX 3.1 system releases.""")
if mibBuilder.loadTexts:
    usdInternetAgentV2.setStatus(
        "obsolete"
    )

usdInternetAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 3)
)
if mibBuilder.loadTexts:
    usdInternetAgentV3.setProductRelease("""\
Version 3 of the Internet component of the Unisphere Routing Switch
        SNMP agent.  This version of the Internet component was supported in the
        Unisphere RX 3.2 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdInternetAgentV3.setStatus(
        "obsolete"
    )

usdInternetAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21, 4)
)
if mibBuilder.loadTexts:
    usdInternetAgentV4.setProductRelease("""\
Version 4 of the Internet component of the Unisphere Routing Switch
        SNMP agent.  This version of the Internet component is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdInternetAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-Internet-CONF",
    **{"usdInternetAgent": usdInternetAgent,
       "usdInternetAgentV1": usdInternetAgentV1,
       "usdInternetAgentV2": usdInternetAgentV2,
       "usdInternetAgentV3": usdInternetAgentV3,
       "usdInternetAgentV4": usdInternetAgentV4}
)
