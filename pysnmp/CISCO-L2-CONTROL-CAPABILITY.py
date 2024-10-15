# SNMP MIB module (CISCO-L2-CONTROL-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2-CONTROL-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:42 2024
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

ciscoL2ControlCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 397)
)
ciscoL2ControlCapability.setRevisions(
        ("2013-10-16 00:00",
         "2007-06-30 00:00",
         "2007-02-28 00:00",
         "2004-11-01 00:00",
         "2004-03-29 00:00",
         "2003-10-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

clcCapabilityV12R0217aSXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 397, 1)
)
if mibBuilder.loadTexts:
    clcCapabilityV12R0217aSXCat6K.setProductRelease("""\
Cisco IOS 12.2(17a)SX on Catalyst 6000/6500
                      and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    clcCapabilityV12R0217aSXCat6K.setStatus(
        "current"
    )

clcCapabilityCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 397, 2)
)
if mibBuilder.loadTexts:
    clcCapabilityCatOSV08R0301.setProductRelease("Cisco CatOS 8.3(1).")
if mibBuilder.loadTexts:
    clcCapabilityCatOSV08R0301.setStatus(
        "current"
    )

clcCapabilityCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 397, 3)
)
if mibBuilder.loadTexts:
    clcCapabilityCatOSV08R0601.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                      and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    clcCapabilityCatOSV08R0601.setStatus(
        "current"
    )

clcCapabilityV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 397, 4)
)
if mibBuilder.loadTexts:
    clcCapabilityV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                       series devices.""")
if mibBuilder.loadTexts:
    clcCapabilityV12R0233SXHPCat6K.setStatus(
        "current"
    )

clcCapabilityV6R0002U0102PN3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 397, 5)
)
if mibBuilder.loadTexts:
    clcCapabilityV6R0002U0102PN3K.setProductRelease("""\
Cisco NX-OS 6.0(2)U1(2) on Nexus 3000
                       series devices.""")
if mibBuilder.loadTexts:
    clcCapabilityV6R0002U0102PN3K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2-CONTROL-CAPABILITY",
    **{"ciscoL2ControlCapability": ciscoL2ControlCapability,
       "clcCapabilityV12R0217aSXCat6K": clcCapabilityV12R0217aSXCat6K,
       "clcCapabilityCatOSV08R0301": clcCapabilityCatOSV08R0301,
       "clcCapabilityCatOSV08R0601": clcCapabilityCatOSV08R0601,
       "clcCapabilityV12R0233SXHPCat6K": clcCapabilityV12R0233SXHPCat6K,
       "clcCapabilityV6R0002U0102PN3K": clcCapabilityV6R0002U0102PN3K}
)
