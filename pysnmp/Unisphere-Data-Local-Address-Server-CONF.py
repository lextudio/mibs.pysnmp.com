# SNMP MIB module (Unisphere-Data-Local-Address-Server-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-Local-Address-Server-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:07 2024
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

(usdAddressPoolGroup,
 usdAddressPoolGroup2,
 usdAddressPoolGroup3,
 usdAddressPoolTrapGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-ADDRESS-POOL-MIB",
    "usdAddressPoolGroup",
    "usdAddressPoolGroup2",
    "usdAddressPoolGroup3",
    "usdAddressPoolTrapGroup")

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")


# MODULE-IDENTITY

usdLocalAddressServerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25)
)
usdLocalAddressServerAgent.setRevisions(
        ("2002-05-06 19:20",
         "2001-05-02 13:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdLocalAddressServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1)
)
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV1.setProductRelease("""\
Version 1 of the Local Address Server component of the Unisphere
        Routing Switch SNMP agent.  This version of the Local Address Server
        component was supported in the Unisphere RX 1.3 thru RX 3.1 system
        releases.""")
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV1.setStatus(
        "obsolete"
    )

usdLocalAddressServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2)
)
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV2.setProductRelease("""\
Version 2 of the Local Address Server component of the Unisphere
        Routing Switch SNMP agent.  This version of the Local Address Server
        component was supported in the Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV2.setStatus(
        "obsolete"
    )

usdLocalAddressServerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3)
)
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV3.setProductRelease("""\
Version 3 of the Local Address Server component of the Unisphere
        Routing Switch SNMP agent.  This version of the Local Address Server
        component is supported in the Unisphere RX 3.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    usdLocalAddressServerAgentV3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-Local-Address-Server-CONF",
    **{"usdLocalAddressServerAgent": usdLocalAddressServerAgent,
       "usdLocalAddressServerAgentV1": usdLocalAddressServerAgentV1,
       "usdLocalAddressServerAgentV2": usdLocalAddressServerAgentV2,
       "usdLocalAddressServerAgentV3": usdLocalAddressServerAgentV3}
)
