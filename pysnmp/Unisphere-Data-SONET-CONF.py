# SNMP MIB module (Unisphere-Data-SONET-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SONET-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:39 2024
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

(sonetFarEndLineStuff2,
 sonetFarEndPathStuff2,
 sonetFarEndVTStuff2,
 sonetLineStuff,
 sonetLineStuff2,
 sonetMediumLineCoding,
 sonetMediumLineType,
 sonetMediumLoopbackConfig,
 sonetMediumStuff,
 sonetMediumStuff2,
 sonetMediumTimeElapsed,
 sonetMediumValidIntervals,
 sonetPathStuff,
 sonetPathStuff2,
 sonetSectionStuff,
 sonetSectionStuff2,
 sonetVTStuff,
 sonetVTStuff2) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetFarEndLineStuff2",
    "sonetFarEndPathStuff2",
    "sonetFarEndVTStuff2",
    "sonetLineStuff",
    "sonetLineStuff2",
    "sonetMediumLineCoding",
    "sonetMediumLineType",
    "sonetMediumLoopbackConfig",
    "sonetMediumStuff",
    "sonetMediumStuff2",
    "sonetMediumTimeElapsed",
    "sonetMediumValidIntervals",
    "sonetPathStuff",
    "sonetPathStuff2",
    "sonetSectionStuff",
    "sonetSectionStuff2",
    "sonetVTStuff",
    "sonetVTStuff2")

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdSonetGroup,
 usdSonetPathGroup,
 usdSonetVirtualTributaryGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-SONET-MIB",
    "usdSonetGroup",
    "usdSonetPathGroup",
    "usdSonetVirtualTributaryGroup")


# MODULE-IDENTITY

usdSonetAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40)
)
usdSonetAgent.setRevisions(
        ("2002-02-04 21:35",
         "2001-04-03 22:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdSonetBasicAgent_ObjectIdentity = ObjectIdentity
usdSonetBasicAgent = _UsdSonetBasicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5)
)
_UsdSonetVTAgent_ObjectIdentity = ObjectIdentity
usdSonetVTAgent = _UsdSonetVTAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdSonetAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1)
)
if mibBuilder.loadTexts:
    usdSonetAgentV1.setProductRelease("""\
Version 1 of the SONET component of the Unisphere Routing Switch SNMP
        agent.  This version of the SONET component was supported in the
        Unisphere RX 1.x system releases.""")
if mibBuilder.loadTexts:
    usdSonetAgentV1.setStatus(
        "obsolete"
    )

usdSonetAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2)
)
if mibBuilder.loadTexts:
    usdSonetAgentV2.setProductRelease("""\
Version 2 of the SONET component of the Unisphere Routing Switch SNMP
        agent.  This version of the SONET component was supported in the
        Unisphere RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdSonetAgentV2.setStatus(
        "obsolete"
    )

usdSonetAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3)
)
if mibBuilder.loadTexts:
    usdSonetAgentV3.setProductRelease("""\
Version 3 of the SONET component of the Unisphere Routing Switch SNMP
        agent.  This version of the SONET component was supported in the
        Unisphere RX 3.0 and 3.1 system releases.""")
if mibBuilder.loadTexts:
    usdSonetAgentV3.setStatus(
        "obsolete"
    )

usdSonetAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4)
)
if mibBuilder.loadTexts:
    usdSonetAgentV4.setProductRelease("""\
Version 4 of the SONET component of the Unisphere Routing Switch SNMP
        agent.  This version of the SONET component was supported in the
        Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdSonetAgentV4.setStatus(
        "obsolete"
    )

usdSonetBasicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1)
)
if mibBuilder.loadTexts:
    usdSonetBasicAgentV1.setProductRelease("""\
Version 1 of the basic SONET component of the Unisphere Routing Switch
        SNMP agent.  It does not include Virtual Tributary (VT) support.  This
        version of the basic SONET component is supported in the Unisphere RX
        3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdSonetBasicAgentV1.setStatus(
        "current"
    )

usdSonetVTAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1)
)
if mibBuilder.loadTexts:
    usdSonetVTAgentV1.setProductRelease("""\
Version 1 of the SONET VT component of the Unisphere Routing Switch
        SNMP agent.  This version of the SONET component is supported in the
        Unisphere RX 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdSonetVTAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SONET-CONF",
    **{"usdSonetAgent": usdSonetAgent,
       "usdSonetAgentV1": usdSonetAgentV1,
       "usdSonetAgentV2": usdSonetAgentV2,
       "usdSonetAgentV3": usdSonetAgentV3,
       "usdSonetAgentV4": usdSonetAgentV4,
       "usdSonetBasicAgent": usdSonetBasicAgent,
       "usdSonetBasicAgentV1": usdSonetBasicAgentV1,
       "usdSonetVTAgent": usdSonetVTAgent,
       "usdSonetVTAgentV1": usdSonetVTAgentV1}
)
