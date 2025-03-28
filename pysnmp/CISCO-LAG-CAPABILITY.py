# SNMP MIB module (CISCO-LAG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LAG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:52 2024
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

ciscoLagCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 332)
)
ciscoLagCapability.setRevisions(
        ("2012-04-02 00:00",
         "2011-09-27 00:00",
         "2010-11-01 00:00",
         "2009-11-19 00:00",
         "2007-07-10 10:00",
         "2006-06-15 12:00",
         "2004-02-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

clagCapV12R0111bEXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 1)
)
if mibBuilder.loadTexts:
    clagCapV12R0111bEXCat6K.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    clagCapV12R0111bEXCat6K.setStatus(
        "current"
    )

clagCapV12R0217SXCat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 2)
)
if mibBuilder.loadTexts:
    clagCapV12R0217SXCat6KPfc2.setProductRelease("""\
Cisco IOS 12.2(17)SX on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    clagCapV12R0217SXCat6KPfc2.setStatus(
        "current"
    )

clagCapV12R0217SXCat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 3)
)
if mibBuilder.loadTexts:
    clagCapV12R0217SXCat6KPfc3.setProductRelease("""\
Cisco IOS 12.2(17)SX on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    clagCapV12R0217SXCat6KPfc3.setStatus(
        "current"
    )

clagCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 4)
)
if mibBuilder.loadTexts:
    clagCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    clagCapCatOSV08R0101.setStatus(
        "current"
    )

clagCapV12R0218SXF5PCat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 5)
)
if mibBuilder.loadTexts:
    clagCapV12R0218SXF5PCat6KPfc2.setProductRelease("""\
Cisco IOS 12.2(18)SXF5 on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    clagCapV12R0218SXF5PCat6KPfc2.setStatus(
        "current"
    )

clagCapV12R0218SXF5PCat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 6)
)
if mibBuilder.loadTexts:
    clagCapV12R0218SXF5PCat6KPfc3.setProductRelease("""\
Cisco IOS 12.2(18)SXF5 on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    clagCapV12R0218SXF5PCat6KPfc3.setStatus(
        "current"
    )

clagCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 7)
)
if mibBuilder.loadTexts:
    clagCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    devices.""")
if mibBuilder.loadTexts:
    clagCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

clagCapV12R0252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 8)
)
if mibBuilder.loadTexts:
    clagCapV12R0252SGPCat4K.setProductRelease("Cisco IOS 12.2(52)SG on Cat4K family devices.")
if mibBuilder.loadTexts:
    clagCapV12R0252SGPCat4K.setStatus(
        "current"
    )

clagCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 9)
)
if mibBuilder.loadTexts:
    clagCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    clagCapV12R0250SYPCat6K.setStatus(
        "current"
    )

clagCapV15R0001SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 10)
)
if mibBuilder.loadTexts:
    clagCapV15R0001SYPCat6k.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    clagCapV15R0001SYPCat6k.setStatus(
        "current"
    )

clagCapV15R0101SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 332, 11)
)
if mibBuilder.loadTexts:
    clagCapV15R0101SGPCat4K.setProductRelease("Cisco IOS 15.1(1)SG on Cat4K family devices.")
if mibBuilder.loadTexts:
    clagCapV15R0101SGPCat4K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LAG-CAPABILITY",
    **{"ciscoLagCapability": ciscoLagCapability,
       "clagCapV12R0111bEXCat6K": clagCapV12R0111bEXCat6K,
       "clagCapV12R0217SXCat6KPfc2": clagCapV12R0217SXCat6KPfc2,
       "clagCapV12R0217SXCat6KPfc3": clagCapV12R0217SXCat6KPfc3,
       "clagCapCatOSV08R0101": clagCapCatOSV08R0101,
       "clagCapV12R0218SXF5PCat6KPfc2": clagCapV12R0218SXF5PCat6KPfc2,
       "clagCapV12R0218SXF5PCat6KPfc3": clagCapV12R0218SXF5PCat6KPfc3,
       "clagCapV12R0233SXHPCat6K": clagCapV12R0233SXHPCat6K,
       "clagCapV12R0252SGPCat4K": clagCapV12R0252SGPCat4K,
       "clagCapV12R0250SYPCat6K": clagCapV12R0250SYPCat6K,
       "clagCapV15R0001SYPCat6k": clagCapV15R0001SYPCat6k,
       "clagCapV15R0101SGPCat4K": clagCapV15R0101SGPCat4K}
)
