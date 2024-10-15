# SNMP MIB module (CISCO-CATOS-ACL-QOS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CATOS-ACL-QOS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:02 2024
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

ciscoCatOSAclQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 325)
)
ciscoCatOSAclQosCapability.setRevisions(
        ("2008-03-17 00:00",
         "2006-06-29 00:00",
         "2005-09-06 00:00",
         "2004-06-24 00:00",
         "2004-01-27 00:00",
         "2003-12-19 00:00",
         "2003-08-25 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

caqCapabilityV08R0101Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 1)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0101Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 2)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0101Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 3)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0101Cat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 4)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat4K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 4000 series
                         devices.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0101Cat4K.setStatus(
        "current"
    )

caqCapabilityV08R0301Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 5)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0301Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 6)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0301Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 7)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0301Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0401Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 8)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0401Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 9)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0401Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 10)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0401Cat6KPfc3b = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 11)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc3b.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3B
                         or PFC3BXL card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0401Cat6KPfc3b.setStatus(
        "current"
    )

caqCapabilityV08R0501Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 12)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.5(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0501Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 13)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.5(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0501Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 14)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.5(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0501Cat6KPfc3b = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 15)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc3b.setProductRelease("""\
Cisco CatOS 8.5(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3B
                         or PFC3BXL card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0501Cat6KPfc3b.setStatus(
        "current"
    )

caqCapabilityV08R0601Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 16)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0601Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 17)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0601Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 18)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0601Cat6KPfc3b = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 19)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc3b.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3B
                         or PFC3BXL card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0601Cat6KPfc3b.setStatus(
        "current"
    )

caqCapabilityV08R0701Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 20)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc.setStatus(
        "current"
    )

caqCapabilityV08R0701Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 21)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC2
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc2.setStatus(
        "current"
    )

caqCapabilityV08R0701Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 22)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3
                         card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc3.setStatus(
        "current"
    )

caqCapabilityV08R0701Cat6KPfc3b = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 325, 23)
)
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc3b.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC3B
                         or PFC3BXL card.""")
if mibBuilder.loadTexts:
    caqCapabilityV08R0701Cat6KPfc3b.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CATOS-ACL-QOS-CAPABILITY",
    **{"ciscoCatOSAclQosCapability": ciscoCatOSAclQosCapability,
       "caqCapabilityV08R0101Cat6KPfc": caqCapabilityV08R0101Cat6KPfc,
       "caqCapabilityV08R0101Cat6KPfc2": caqCapabilityV08R0101Cat6KPfc2,
       "caqCapabilityV08R0101Cat6KPfc3": caqCapabilityV08R0101Cat6KPfc3,
       "caqCapabilityV08R0101Cat4K": caqCapabilityV08R0101Cat4K,
       "caqCapabilityV08R0301Cat6KPfc": caqCapabilityV08R0301Cat6KPfc,
       "caqCapabilityV08R0301Cat6KPfc2": caqCapabilityV08R0301Cat6KPfc2,
       "caqCapabilityV08R0301Cat6KPfc3": caqCapabilityV08R0301Cat6KPfc3,
       "caqCapabilityV08R0401Cat6KPfc": caqCapabilityV08R0401Cat6KPfc,
       "caqCapabilityV08R0401Cat6KPfc2": caqCapabilityV08R0401Cat6KPfc2,
       "caqCapabilityV08R0401Cat6KPfc3": caqCapabilityV08R0401Cat6KPfc3,
       "caqCapabilityV08R0401Cat6KPfc3b": caqCapabilityV08R0401Cat6KPfc3b,
       "caqCapabilityV08R0501Cat6KPfc": caqCapabilityV08R0501Cat6KPfc,
       "caqCapabilityV08R0501Cat6KPfc2": caqCapabilityV08R0501Cat6KPfc2,
       "caqCapabilityV08R0501Cat6KPfc3": caqCapabilityV08R0501Cat6KPfc3,
       "caqCapabilityV08R0501Cat6KPfc3b": caqCapabilityV08R0501Cat6KPfc3b,
       "caqCapabilityV08R0601Cat6KPfc": caqCapabilityV08R0601Cat6KPfc,
       "caqCapabilityV08R0601Cat6KPfc2": caqCapabilityV08R0601Cat6KPfc2,
       "caqCapabilityV08R0601Cat6KPfc3": caqCapabilityV08R0601Cat6KPfc3,
       "caqCapabilityV08R0601Cat6KPfc3b": caqCapabilityV08R0601Cat6KPfc3b,
       "caqCapabilityV08R0701Cat6KPfc": caqCapabilityV08R0701Cat6KPfc,
       "caqCapabilityV08R0701Cat6KPfc2": caqCapabilityV08R0701Cat6KPfc2,
       "caqCapabilityV08R0701Cat6KPfc3": caqCapabilityV08R0701Cat6KPfc3,
       "caqCapabilityV08R0701Cat6KPfc3b": caqCapabilityV08R0701Cat6KPfc3b}
)
