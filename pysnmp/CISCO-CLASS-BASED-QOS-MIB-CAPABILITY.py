# SNMP MIB module (CISCO-CLASS-BASED-QOS-MIB-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CLASS-BASED-QOS-MIB-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:32 2024
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

ciscoCBQosMibCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 525)
)
ciscoCBQosMibCapability.setRevisions(
        ("2007-07-17 00:00",
         "2006-11-08 00:00",
         "2005-06-22 00:00",
         "2004-09-01 00:00",
         "2003-01-24 00:00",
         "2001-06-13 00:00",
         "2000-12-01 00:00",
         "2000-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoCBQosMibCapabilityV121R02E7500 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 1)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R02E7500.setProductRelease("Cisco IOS 12.1(2)E on 7500.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R02E7500.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV120R12S7500 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 2)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV120R12S7500.setProductRelease("Cisco IOS 12.0(12)S on 7500.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV120R12S7500.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV121R05T7200 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 3)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R05T7200.setProductRelease("Cisco IOS 12.1(5)T for 7200/lower-end platforms.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R05T7200.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV122R01T7200 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 4)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV122R01T7200.setProductRelease("Cisco IOS 12.2(2)T on 7200 and lower-end platforms.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV122R01T7200.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV123R01T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 5)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV123R01T.setProductRelease("""\
Cisco IOS 12.3(1)T on 7500, 7200 and 
                 lower-end platforms.""")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV123R01T.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV121R14EB = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 6)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R14EB.setProductRelease("Cisco IOS 12.1(14)EB on Catalyst 8540MSR platform.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV121R14EB.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV12R0306T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 7)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R0306T.setProductRelease("""\
Cisco IOS 12.3(6)T on 7200 and 
                 lower-end platforms.""")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R0306T.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV12R02S = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 8)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R02S.setProductRelease("Cisco IOS 12.2S for 7500/7200/lower-end platforms.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R02S.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV12R00S = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 9)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R00S.setProductRelease("Cisco IOS 12.0S for 7500/7200/lower-end platforms.")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV12R00S.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV320CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 10)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV320CRS1.setProductRelease("Cisco IOS XR 3.2.0 on CRS-1")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV320CRS1.setStatus(
        "current"
    )

ciscoCBQosMibCapabilityV3R4CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 11)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV3R4CRS1.setProductRelease("Cisco IOS XR 3.4 on CRS-1")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapabilityV3R4CRS1.setStatus(
        "current"
    )

ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 12)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500
                     and Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setStatus(
        "current"
    )

ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 13)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500
                     and Cisco 7600 series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setStatus(
        "current"
    )

ciscoCBQosMibCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 525, 14)
)
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                     devices.""")
if mibBuilder.loadTexts:
    ciscoCBQosMibCapV12R0233SXHPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CLASS-BASED-QOS-MIB-CAPABILITY",
    **{"ciscoCBQosMibCapability": ciscoCBQosMibCapability,
       "ciscoCBQosMibCapabilityV121R02E7500": ciscoCBQosMibCapabilityV121R02E7500,
       "ciscoCBQosMibCapabilityV120R12S7500": ciscoCBQosMibCapabilityV120R12S7500,
       "ciscoCBQosMibCapabilityV121R05T7200": ciscoCBQosMibCapabilityV121R05T7200,
       "ciscoCBQosMibCapabilityV122R01T7200": ciscoCBQosMibCapabilityV122R01T7200,
       "ciscoCBQosMibCapabilityV123R01T": ciscoCBQosMibCapabilityV123R01T,
       "ciscoCBQosMibCapabilityV121R14EB": ciscoCBQosMibCapabilityV121R14EB,
       "ciscoCBQosMibCapabilityV12R0306T": ciscoCBQosMibCapabilityV12R0306T,
       "ciscoCBQosMibCapabilityV12R02S": ciscoCBQosMibCapabilityV12R02S,
       "ciscoCBQosMibCapabilityV12R00S": ciscoCBQosMibCapabilityV12R00S,
       "ciscoCBQosMibCapabilityV320CRS1": ciscoCBQosMibCapabilityV320CRS1,
       "ciscoCBQosMibCapabilityV3R4CRS1": ciscoCBQosMibCapabilityV3R4CRS1,
       "ciscoCBQosMibCapV12R0218SXFPCat6KPfc2": ciscoCBQosMibCapV12R0218SXFPCat6KPfc2,
       "ciscoCBQosMibCapV12R0218SXFPCat6KPfc3": ciscoCBQosMibCapV12R0218SXFPCat6KPfc3,
       "ciscoCBQosMibCapV12R0233SXHPCat6K": ciscoCBQosMibCapV12R0233SXHPCat6K}
)
