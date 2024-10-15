# SNMP MIB module (Unisphere-Data-PPP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:17 2024
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

(pppIpConfigEntry,
 pppIpEntry) = mibBuilder.importSymbols(
    "PPP-IP-NCP-MIB",
    "pppIpConfigEntry",
    "pppIpEntry")

(pppLinkConfigEntry,
 pppLinkStatusEntry,
 pppLqrConfigEntry,
 pppLqrEntry,
 pppLqrExtnsEntry) = mibBuilder.importSymbols(
    "PPP-LCP-MIB",
    "pppLinkConfigEntry",
    "pppLinkStatusEntry",
    "pppLqrConfigEntry",
    "pppLqrEntry",
    "pppLqrExtnsEntry")

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

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdPppIpGroup2,
 usdPppIpGroup3,
 usdPppLcpGroup3,
 usdPppLcpGroup4,
 usdPppMlPppGroup,
 usdPppMlPppGroup2,
 usdPppOsiGroup2,
 usdPppSessionGroup,
 usdPppSummaryBasicGroup,
 usdPppSummaryGroup,
 usdPppSummaryLinkGroup,
 usdPppSummaryNetworkGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-PPP-MIB",
    "usdPppIpGroup2",
    "usdPppIpGroup3",
    "usdPppLcpGroup3",
    "usdPppLcpGroup4",
    "usdPppMlPppGroup",
    "usdPppMlPppGroup2",
    "usdPppOsiGroup2",
    "usdPppSessionGroup",
    "usdPppSummaryBasicGroup",
    "usdPppSummaryGroup",
    "usdPppSummaryLinkGroup",
    "usdPppSummaryNetworkGroup")


# MODULE-IDENTITY

usdPppAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32)
)
usdPppAgent.setRevisions(
        ("2002-05-09 21:03",
         "2002-05-08 20:25",
         "2001-04-10 18:23")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdPppGeneralAgent_ObjectIdentity = ObjectIdentity
usdPppGeneralAgent = _UsdPppGeneralAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2)
)
if mibBuilder.loadTexts:
    usdPppGeneralAgent.setStatus("current")
_UsdPppMultiLinkAgent_ObjectIdentity = ObjectIdentity
usdPppMultiLinkAgent = _UsdPppMultiLinkAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3)
)
if mibBuilder.loadTexts:
    usdPppMultiLinkAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdPppAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1)
)
if mibBuilder.loadTexts:
    usdPppAgentV1.setProductRelease("""\
Version 1 of the PPP component of the Unisphere Routing Switch SNMP
        agent.  This version of the PPP component was supported in the Unisphere
        RX 2.4 thru 3.2 system releases.""")
if mibBuilder.loadTexts:
    usdPppAgentV1.setStatus(
        "obsolete"
    )

usdPppGeneralAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1)
)
if mibBuilder.loadTexts:
    usdPppGeneralAgentV1.setProductRelease("""\
Version 1 of the general PPP component of the Unisphere Routing Switch
        SNMP agent.  This version of the PPP component was supported in the
        Unisphere RX 3.3 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdPppGeneralAgentV1.setStatus(
        "obsolete"
    )

usdPppGeneralAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2)
)
if mibBuilder.loadTexts:
    usdPppGeneralAgentV2.setProductRelease("""\
Version 2 of the general PPP component of the Unisphere Routing Switch
        SNMP agent.  This version of the PPP component is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPppGeneralAgentV2.setStatus(
        "current"
    )

usdPppMultiLinkAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1)
)
if mibBuilder.loadTexts:
    usdPppMultiLinkAgentV1.setProductRelease("""\
Version 1 of the multi-link PPP component of the Unisphere Routing
        Switch SNMP agent.  This version of the PPP component was supported in
        the Unisphere RX 3.3 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdPppMultiLinkAgentV1.setStatus(
        "obsolete"
    )

usdPppMultiLinkAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2)
)
if mibBuilder.loadTexts:
    usdPppMultiLinkAgentV2.setProductRelease("""\
Version 2 of the multi-link PPP component of the Unisphere Routing
        Switch SNMP agent.  This version of the PPP component is supported in
        the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPppMultiLinkAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPP-CONF",
    **{"usdPppAgent": usdPppAgent,
       "usdPppAgentV1": usdPppAgentV1,
       "usdPppGeneralAgent": usdPppGeneralAgent,
       "usdPppGeneralAgentV1": usdPppGeneralAgentV1,
       "usdPppGeneralAgentV2": usdPppGeneralAgentV2,
       "usdPppMultiLinkAgent": usdPppMultiLinkAgent,
       "usdPppMultiLinkAgentV1": usdPppMultiLinkAgentV1,
       "usdPppMultiLinkAgentV2": usdPppMultiLinkAgentV2}
)
