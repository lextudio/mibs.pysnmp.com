# SNMP MIB module (RSTONE-RS-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RSTONE-RS-AGENTCAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:29 2024
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

(riverstoneAgentCapabilities,) = mibBuilder.importSymbols(
    "RSTONE-SMI-MIB",
    "riverstoneAgentCapabilities")

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


# MODULE-IDENTITY

rstoneRsAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1)
)
rstoneRsAgentCapabilityMIB.setRevisions(
        ("2001-06-21 00:00",
         "2001-03-11 00:00",
         "2001-03-07 00:00",
         "2000-12-13 00:00",
         "2000-09-18 00:00",
         "2000-09-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCapability_ObjectIdentity = ObjectIdentity
rsCapability = _RsCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

rs61x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rs61x.setProductRelease("6.1.x")
if mibBuilder.loadTexts:
    rs61x.setStatus(
        "current"
    )

rs62x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rs62x.setProductRelease("6.2.x")
if mibBuilder.loadTexts:
    rs62x.setStatus(
        "current"
    )

rs63x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rs63x.setProductRelease("6.3.x")
if mibBuilder.loadTexts:
    rs63x.setStatus(
        "current"
    )

rs70x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rs70x.setProductRelease("7.0.x")
if mibBuilder.loadTexts:
    rs70x.setStatus(
        "current"
    )

rs80x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rs80x.setProductRelease("8.0.x")
if mibBuilder.loadTexts:
    rs80x.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RSTONE-RS-AGENTCAP-MIB",
    **{"rstoneRsAgentCapabilityMIB": rstoneRsAgentCapabilityMIB,
       "rsCapability": rsCapability,
       "rs61x": rs61x,
       "rs62x": rs62x,
       "rs63x": rs63x,
       "rs70x": rs70x,
       "rs80x": rs80x}
)
