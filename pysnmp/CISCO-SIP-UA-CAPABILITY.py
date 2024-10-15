# SNMP MIB module (CISCO-SIP-UA-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIP-UA-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:17 2024
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

(ciscoAgentCapability,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoAgentCapability")

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

ciscoSipUaCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 172)
)
ciscoSipUaCapability.setRevisions(
        ("2005-06-22 00:00",
         "2003-07-30 00:00",
         "2003-03-21 00:00",
         "2001-09-26 00:00",
         "2001-06-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSipUaCapabilityV12R0202 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 1)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0202.setProductRelease("Cisco IOS 12.2(2).")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0202.setStatus(
        "current"
    )

ciscoSipUaCapabilityV12R0208 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 2)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0208.setProductRelease("Cisco IOS 12.2(8).")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0208.setStatus(
        "current"
    )

ciscoSipUaCapabilityV12R0211 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 3)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0211.setProductRelease("Cisco IOS 12.2(11).")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0211.setStatus(
        "current"
    )

ciscoSipUaCapabilityV12R0215 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 4)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0215.setProductRelease("Cisco IOS 12.2(15).")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0215.setStatus(
        "current"
    )

ciscoSipUaCapabilityV12R0302 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 5)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0302.setProductRelease("Cisco IOS 12.3(2).")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0302.setStatus(
        "current"
    )

ciscoSipUaCapabilityV12R0402T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 172, 6)
)
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0402T.setProductRelease("Cisco IOS 12.4(2)T.")
if mibBuilder.loadTexts:
    ciscoSipUaCapabilityV12R0402T.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIP-UA-CAPABILITY",
    **{"ciscoSipUaCapability": ciscoSipUaCapability,
       "ciscoSipUaCapabilityV12R0202": ciscoSipUaCapabilityV12R0202,
       "ciscoSipUaCapabilityV12R0208": ciscoSipUaCapabilityV12R0208,
       "ciscoSipUaCapabilityV12R0211": ciscoSipUaCapabilityV12R0211,
       "ciscoSipUaCapabilityV12R0215": ciscoSipUaCapabilityV12R0215,
       "ciscoSipUaCapabilityV12R0302": ciscoSipUaCapabilityV12R0302,
       "ciscoSipUaCapabilityV12R0402T": ciscoSipUaCapabilityV12R0402T}
)
