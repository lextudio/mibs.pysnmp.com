# SNMP MIB module (CISCO-PORT-STORM-CONTROL-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PORT-STORM-CONTROL-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:58 2024
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

ciscoPortStormControlCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 542)
)
ciscoPortStormControlCapability.setRevisions(
        ("2014-04-04 00:00",
         "2012-09-07 00:00",
         "2011-03-24 00:00",
         "2007-07-03 00:00",
         "2007-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cpscCapabilityV12R0240SGCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 542, 1)
)
if mibBuilder.loadTexts:
    cpscCapabilityV12R0240SGCat4K.setProductRelease("Cisco IOS 12.2(40)SG on Cat4K platform")
if mibBuilder.loadTexts:
    cpscCapabilityV12R0240SGCat4K.setStatus(
        "current"
    )

cpscCapabilityV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 542, 2)
)
if mibBuilder.loadTexts:
    cpscCapabilityV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cpscCapabilityV12R0233SXHPCat6K.setStatus(
        "current"
    )

cpscCapabilityV12R0233SXJPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 542, 3)
)
if mibBuilder.loadTexts:
    cpscCapabilityV12R0233SXJPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cpscCapabilityV12R0233SXJPCat6k.setStatus(
        "current"
    )

cpscCapabilityV15R0101SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 542, 4)
)
if mibBuilder.loadTexts:
    cpscCapabilityV15R0101SYPCat6k.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cpscCapabilityV15R0101SYPCat6k.setStatus(
        "current"
    )

cpscCapabilityV06R0002U0301PN3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 542, 5)
)
if mibBuilder.loadTexts:
    cpscCapabilityV06R0002U0301PN3K.setProductRelease("Cisco NX-OS 6.0(2)U3(1) on Nexus 3000.")
if mibBuilder.loadTexts:
    cpscCapabilityV06R0002U0301PN3K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-STORM-CONTROL-CAPABILITY",
    **{"ciscoPortStormControlCapability": ciscoPortStormControlCapability,
       "cpscCapabilityV12R0240SGCat4K": cpscCapabilityV12R0240SGCat4K,
       "cpscCapabilityV12R0233SXHPCat6K": cpscCapabilityV12R0233SXHPCat6K,
       "cpscCapabilityV12R0233SXJPCat6k": cpscCapabilityV12R0233SXJPCat6k,
       "cpscCapabilityV15R0101SYPCat6k": cpscCapabilityV15R0101SYPCat6k,
       "cpscCapabilityV06R0002U0301PN3K": cpscCapabilityV06R0002U0301PN3K}
)
