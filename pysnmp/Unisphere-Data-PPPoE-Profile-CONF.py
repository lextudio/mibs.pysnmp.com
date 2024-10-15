# SNMP MIB module (Unisphere-Data-PPPoE-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPPoE-Profile-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:23 2024
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

(usdProfileAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usdProfileAgents")

(usdPppoeProfileGroup,
 usdPppoeProfileGroup2,
 usdPppoeProfileGroup3) = mibBuilder.importSymbols(
    "Unisphere-Data-PPPOE-PROFILE-MIB",
    "usdPppoeProfileGroup",
    "usdPppoeProfileGroup2",
    "usdPppoeProfileGroup3")


# MODULE-IDENTITY

usdPppoeProfileAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4)
)
usdPppoeProfileAgent.setRevisions(
        ("2002-08-15 20:38",
         "2002-05-31 18:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdPppoeProfileAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1)
)
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV1.setProductRelease("""\
Version 1 of the PPPoE Profile component of the Unisphere Routing
        Switch SNMP agent.  This version of the PPPoE Profile component was
        supported in the Unisphere RX 3.0 and 3.1 system releases.""")
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV1.setStatus(
        "obsolete"
    )

usdPppoeProfileAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2)
)
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV2.setProductRelease("""\
Version 2 of the PPPoE Profile component of the Unisphere Routing
        Switch SNMP agent.  This version of the PPPoE Profile component was
        supported in the Unisphere RX 3.2 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV2.setStatus(
        "obsolete"
    )

usdPppoeProfileAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3)
)
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV3.setProductRelease("""\
Version 3 of the PPPoE Profile component of the Unisphere Routing
        Switch SNMP agent.  This version of the PPPoE Profile component is
        supported in the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPppoeProfileAgentV3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPPoE-Profile-CONF",
    **{"usdPppoeProfileAgent": usdPppoeProfileAgent,
       "usdPppoeProfileAgentV1": usdPppoeProfileAgentV1,
       "usdPppoeProfileAgentV2": usdPppoeProfileAgentV2,
       "usdPppoeProfileAgentV3": usdPppoeProfileAgentV3}
)
