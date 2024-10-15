# SNMP MIB module (CISCO-VLAN-GROUP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-GROUP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:03 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVlanGroupCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 590)
)
ciscoVlanGroupCapability.setRevisions(
        ("2012-04-10 00:00",
         "2011-09-22 00:00",
         "2011-03-31 00:00",
         "2011-03-23 00:00",
         "2010-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoVlanGroupCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 590, 1)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                        series devices.""")
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

ciscoVlanGroupCapV12R0233SXJPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 590, 2)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV12R0233SXJPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500
                        series devices.""")
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV12R0233SXJPCat6k.setStatus(
        "current"
    )

ciscoVlanGroupCapV15R0002SGPCat4k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 590, 3)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0002SGPCat4k.setProductRelease("""\
Cisco IOS 15.0(2)SG on Cat4k family switches
                    (excluding switches with SUP7).""")
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0002SGPCat4k.setStatus(
        "current"
    )

ciscoVlanGroupCapV15R0001SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 590, 4)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0001SYPCat6k.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                        series devices.""")
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0001SYPCat6k.setStatus(
        "current"
    )

ciscoVlanGroupCapV15R0101SGPCat4k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 590, 5)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0101SGPCat4k.setProductRelease("Cisco IOS 15.1(1)SG on Cat4k family switches.")
if mibBuilder.loadTexts:
    ciscoVlanGroupCapV15R0101SGPCat4k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-GROUP-CAPABILITY",
    **{"ciscoVlanGroupCapability": ciscoVlanGroupCapability,
       "ciscoVlanGroupCapV12R0233SXI4PCat6K": ciscoVlanGroupCapV12R0233SXI4PCat6K,
       "ciscoVlanGroupCapV12R0233SXJPCat6k": ciscoVlanGroupCapV12R0233SXJPCat6k,
       "ciscoVlanGroupCapV15R0002SGPCat4k": ciscoVlanGroupCapV15R0002SGPCat4k,
       "ciscoVlanGroupCapV15R0001SYPCat6k": ciscoVlanGroupCapV15R0001SYPCat6k,
       "ciscoVlanGroupCapV15R0101SGPCat4k": ciscoVlanGroupCapV15R0101SGPCat4k}
)
