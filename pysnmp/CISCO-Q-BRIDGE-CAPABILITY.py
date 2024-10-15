# SNMP MIB module (CISCO-Q-BRIDGE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-Q-BRIDGE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:17 2024
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

ciscoQBridgeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 389)
)
ciscoQBridgeCapability.setRevisions(
        ("2011-09-27 00:00",
         "2011-07-27 00:00",
         "2008-10-28 00:00",
         "2004-01-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoQBridgeCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 389, 1)
)
if mibBuilder.loadTexts:
    ciscoQBridgeCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoQBridgeCapCatOSV08R0301.setStatus(
        "current"
    )

ciscoQBridgeCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 389, 2)
)
if mibBuilder.loadTexts:
    ciscoQBridgeCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoQBridgeCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

ciscoQBridgeCapNxOSV05R0201PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 389, 3)
)
if mibBuilder.loadTexts:
    ciscoQBridgeCapNxOSV05R0201PN7K.setProductRelease("""\
Cisco NX-OS 5.2(1) on Nexus 7000
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoQBridgeCapNxOSV05R0201PN7K.setStatus(
        "current"
    )

ciscoQBridgeCapV15R0001SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 389, 4)
)
if mibBuilder.loadTexts:
    ciscoQBridgeCapV15R0001SYPCat6K.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoQBridgeCapV15R0001SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-Q-BRIDGE-CAPABILITY",
    **{"ciscoQBridgeCapability": ciscoQBridgeCapability,
       "ciscoQBridgeCapCatOSV08R0301": ciscoQBridgeCapCatOSV08R0301,
       "ciscoQBridgeCapV12R0233SXIPCat6K": ciscoQBridgeCapV12R0233SXIPCat6K,
       "ciscoQBridgeCapNxOSV05R0201PN7K": ciscoQBridgeCapNxOSV05R0201PN7K,
       "ciscoQBridgeCapV15R0001SYPCat6K": ciscoQBridgeCapV15R0001SYPCat6K}
)
