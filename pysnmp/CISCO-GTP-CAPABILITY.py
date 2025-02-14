# SNMP MIB module (CISCO-GTP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GTP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:04 2024
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

ciscoGtpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 263)
)
ciscoGtpCapability.setRevisions(
        ("2003-04-02 09:00",
         "2002-03-21 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cGtpCapabilityV12R02Rev08YD = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 263, 1)
)
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YD.setProductRelease("Cisco IOS 12.2(8)YD")
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YD.setStatus(
        "current"
    )

cGtpCapabilityV12R02Rev08YY = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 263, 2)
)
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YY.setProductRelease("Cisco IOS 12.2(8)YY")
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YY.setStatus(
        "current"
    )

cGtpCapabilityV12R02Rev08YW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 263, 3)
)
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YW.setProductRelease("Cisco IOS 12.2(8)YW")
if mibBuilder.loadTexts:
    cGtpCapabilityV12R02Rev08YW.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GTP-CAPABILITY",
    **{"ciscoGtpCapability": ciscoGtpCapability,
       "cGtpCapabilityV12R02Rev08YD": cGtpCapabilityV12R02Rev08YD,
       "cGtpCapabilityV12R02Rev08YY": cGtpCapabilityV12R02Rev08YY,
       "cGtpCapabilityV12R02Rev08YW": cGtpCapabilityV12R02Rev08YW}
)
