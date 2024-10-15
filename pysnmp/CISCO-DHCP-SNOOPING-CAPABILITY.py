# SNMP MIB module (CISCO-DHCP-SNOOPING-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DHCP-SNOOPING-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:56 2024
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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

ciscoDhcpSnoopingCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 383)
)
ciscoDhcpSnoopingCapability.setRevisions(
        ("2011-09-28 00:00",
         "2010-10-27 00:00",
         "2010-03-18 00:00",
         "2008-03-20 00:00",
         "2007-07-02 09:00",
         "2006-06-28 00:00",
         "2004-03-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cdsCapabilityV08R0301Cat6kPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 1)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0301Cat6kPfc.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC
                          of PFC2 card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0301Cat6kPfc.setStatus(
        "current"
    )

cdsCapabilityV08R0301Cat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 2)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0301Cat6kPfc3.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC3
                          card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0301Cat6kPfc3.setStatus(
        "current"
    )

cdsCapabilityV08R0601Cat6kPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 3)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0601Cat6kPfc.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC
                          or PFC2 card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0601Cat6kPfc.setStatus(
        "current"
    )

cdsCapabilityV08R0601Cat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 4)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0601Cat6kPfc3.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC3
                          card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0601Cat6kPfc3.setStatus(
        "current"
    )

cdsCapV12R0233SXHPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 5)
)
if mibBuilder.loadTexts:
    cdsCapV12R0233SXHPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cdsCapV12R0233SXHPCat6k.setStatus(
        "current"
    )

cdsCapabilityV08R0701Cat6kPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 6)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0701Cat6kPfc.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC
                          or PFC2 card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0701Cat6kPfc.setStatus(
        "current"
    )

cdsCapabilityV08R0701Cat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 7)
)
if mibBuilder.loadTexts:
    cdsCapabilityV08R0701Cat6kPfc3.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices with PFC3
                          card.""")
if mibBuilder.loadTexts:
    cdsCapabilityV08R0701Cat6kPfc3.setStatus(
        "current"
    )

cdsCapV12R0233SXI4PCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 8)
)
if mibBuilder.loadTexts:
    cdsCapV12R0233SXI4PCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cdsCapV12R0233SXI4PCat6k.setStatus(
        "current"
    )

cdsCapV12R0250SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 9)
)
if mibBuilder.loadTexts:
    cdsCapV12R0250SYPCat6k.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cdsCapV12R0250SYPCat6k.setStatus(
        "current"
    )

cdsCapV15R0001SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 383, 10)
)
if mibBuilder.loadTexts:
    cdsCapV15R0001SYPCat6k.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cdsCapV15R0001SYPCat6k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DHCP-SNOOPING-CAPABILITY",
    **{"ciscoDhcpSnoopingCapability": ciscoDhcpSnoopingCapability,
       "cdsCapabilityV08R0301Cat6kPfc": cdsCapabilityV08R0301Cat6kPfc,
       "cdsCapabilityV08R0301Cat6kPfc3": cdsCapabilityV08R0301Cat6kPfc3,
       "cdsCapabilityV08R0601Cat6kPfc": cdsCapabilityV08R0601Cat6kPfc,
       "cdsCapabilityV08R0601Cat6kPfc3": cdsCapabilityV08R0601Cat6kPfc3,
       "cdsCapV12R0233SXHPCat6k": cdsCapV12R0233SXHPCat6k,
       "cdsCapabilityV08R0701Cat6kPfc": cdsCapabilityV08R0701Cat6kPfc,
       "cdsCapabilityV08R0701Cat6kPfc3": cdsCapabilityV08R0701Cat6kPfc3,
       "cdsCapV12R0233SXI4PCat6k": cdsCapV12R0233SXI4PCat6k,
       "cdsCapV12R0250SYPCat6k": cdsCapV12R0250SYPCat6k,
       "cdsCapV15R0001SYPCat6k": cdsCapV15R0001SYPCat6k}
)
