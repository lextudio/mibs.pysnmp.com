# SNMP MIB module (CISCO-WAN-TOPOLOGY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-TOPOLOGY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:22 2024
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

ciscoWanTopologyCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 254)
)
ciscoWanTopologyCapability.setRevisions(
        ("2003-01-15 00:00",
         "2002-10-31 00:00",
         "2001-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoWanTopologyCapabilityV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 254, 1)
)
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV3R00.setProductRelease("MGX8850 and BPX-SES Release 3.00")
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV3R00.setStatus(
        "current"
    )

ciscoWanTopologyCapabilityV3R0020 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 254, 2)
)
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV3R0020.setProductRelease("MGX8850 and BPX-SES Release 3.0.20")
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV3R0020.setStatus(
        "current"
    )

ciscoWanTopologyCapabilityV4R0000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 254, 3)
)
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV4R0000.setProductRelease("MGX8850 and BPX-SES Release 4.0.00")
if mibBuilder.loadTexts:
    ciscoWanTopologyCapabilityV4R0000.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-TOPOLOGY-CAPABILITY",
    **{"ciscoWanTopologyCapability": ciscoWanTopologyCapability,
       "ciscoWanTopologyCapabilityV3R00": ciscoWanTopologyCapabilityV3R00,
       "ciscoWanTopologyCapabilityV3R0020": ciscoWanTopologyCapabilityV3R0020,
       "ciscoWanTopologyCapabilityV4R0000": ciscoWanTopologyCapabilityV4R0000}
)
