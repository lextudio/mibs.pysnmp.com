# SNMP MIB module (CISCO-SWITCH-ENGINE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-ENGINE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:05 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchEngineCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 343)
)
ciscoSwitchEngineCapability.setRevisions(
        ("2013-07-25 00:00",
         "2012-09-10 00:00",
         "2011-09-28 00:00",
         "2010-11-11 00:00",
         "2010-03-22 00:00",
         "2008-10-30 00:00",
         "2007-07-16 00:00",
         "2005-09-16 00:00",
         "2005-08-24 00:00",
         "2004-12-22 00:00",
         "2004-06-14 00:00",
         "2004-01-15 00:00",
         "2003-12-04 00:00",
         "2003-08-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cseCapCatOSV08R0101Cat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 1)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                    series devices with PFC card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc.setStatus(
        "current"
    )

cseCapCatOSV08R0101Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 2)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc2.setStatus(
        "current"
    )

cseCapCatOSV08R0101Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 3)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0101Cat6KPfc3.setStatus(
        "current"
    )

cseCapV12R0119ECat6KPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 4)
)
if mibBuilder.loadTexts:
    cseCapV12R0119ECat6KPfc.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                    series devices with PFC card.""")
if mibBuilder.loadTexts:
    cseCapV12R0119ECat6KPfc.setStatus(
        "current"
    )

cseCapV12R0119ECat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 5)
)
if mibBuilder.loadTexts:
    cseCapV12R0119ECat6KPfc2.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC2 card.""")
if mibBuilder.loadTexts:
    cseCapV12R0119ECat6KPfc2.setStatus(
        "current"
    )

cseCapV12R0217SXCat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 6)
)
if mibBuilder.loadTexts:
    cseCapV12R0217SXCat6KPfc3.setProductRelease("""\
Cisco IOS 12.2(17SX) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapV12R0217SXCat6KPfc3.setStatus(
        "current"
    )

cseCapCatOSV08R0301Cat6KPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 7)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0301Cat6KPfc2.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0301Cat6KPfc2.setStatus(
        "current"
    )

cseCapCatOSV08R0301Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 8)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0301Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0301Cat6KPfc3.setStatus(
        "current"
    )

cseCapCatOSV08R0401Cat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 9)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0401Cat6KPfc3.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0401Cat6KPfc3.setStatus(
        "current"
    )

cseCapV12R0218SXEPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 10)
)
if mibBuilder.loadTexts:
    cseCapV12R0218SXEPCat6K.setProductRelease("""\
Cisco IOS 12.2(18)SXE on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cseCapV12R0218SXEPCat6K.setStatus(
        "current"
    )

cseCapCatOSV08R0501PCat6KPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 11)
)
if mibBuilder.loadTexts:
    cseCapCatOSV08R0501PCat6KPfc3.setProductRelease("""\
Cisco CatOS 8.5(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices with 
                    PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapCatOSV08R0501PCat6KPfc3.setStatus(
        "current"
    )

cseCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 12)
)
if mibBuilder.loadTexts:
    cseCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cseCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

cseCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 13)
)
if mibBuilder.loadTexts:
    cseCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cseCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cseCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 14)
)
if mibBuilder.loadTexts:
    cseCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cseCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cseCapV12R0250SYPCat6KPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 15)
)
if mibBuilder.loadTexts:
    cseCapV12R0250SYPCat6KPfc4.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices for PFC4 card.""")
if mibBuilder.loadTexts:
    cseCapV12R0250SYPCat6KPfc4.setStatus(
        "current"
    )

cseCapV15R0001SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 16)
)
if mibBuilder.loadTexts:
    cseCapV15R0001SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices for PFC4 card.""")
if mibBuilder.loadTexts:
    cseCapV15R0001SYPCat6kPfc4.setStatus(
        "current"
    )

cseCapV15R0101SYPCat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 17)
)
if mibBuilder.loadTexts:
    cseCapV15R0101SYPCat6kPfc3.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    cseCapV15R0101SYPCat6kPfc3.setStatus(
        "current"
    )

cseCapV15R0101SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 18)
)
if mibBuilder.loadTexts:
    cseCapV15R0101SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices for PFC4 card.""")
if mibBuilder.loadTexts:
    cseCapV15R0101SYPCat6kPfc4.setStatus(
        "current"
    )

cseCapNxOSV06R0104PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 343, 19)
)
if mibBuilder.loadTexts:
    cseCapNxOSV06R0104PN7k.setProductRelease("Cisco NX-OS 6.1(4) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    cseCapNxOSV06R0104PN7k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-ENGINE-CAPABILITY",
    **{"ciscoSwitchEngineCapability": ciscoSwitchEngineCapability,
       "cseCapCatOSV08R0101Cat6KPfc": cseCapCatOSV08R0101Cat6KPfc,
       "cseCapCatOSV08R0101Cat6KPfc2": cseCapCatOSV08R0101Cat6KPfc2,
       "cseCapCatOSV08R0101Cat6KPfc3": cseCapCatOSV08R0101Cat6KPfc3,
       "cseCapV12R0119ECat6KPfc": cseCapV12R0119ECat6KPfc,
       "cseCapV12R0119ECat6KPfc2": cseCapV12R0119ECat6KPfc2,
       "cseCapV12R0217SXCat6KPfc3": cseCapV12R0217SXCat6KPfc3,
       "cseCapCatOSV08R0301Cat6KPfc2": cseCapCatOSV08R0301Cat6KPfc2,
       "cseCapCatOSV08R0301Cat6KPfc3": cseCapCatOSV08R0301Cat6KPfc3,
       "cseCapCatOSV08R0401Cat6KPfc3": cseCapCatOSV08R0401Cat6KPfc3,
       "cseCapV12R0218SXEPCat6K": cseCapV12R0218SXEPCat6K,
       "cseCapCatOSV08R0501PCat6KPfc3": cseCapCatOSV08R0501PCat6KPfc3,
       "cseCapV12R0233SXHPCat6K": cseCapV12R0233SXHPCat6K,
       "cseCapV12R0233SXIPCat6K": cseCapV12R0233SXIPCat6K,
       "cseCapV12R0233SXI4PCat6K": cseCapV12R0233SXI4PCat6K,
       "cseCapV12R0250SYPCat6KPfc4": cseCapV12R0250SYPCat6KPfc4,
       "cseCapV15R0001SYPCat6kPfc4": cseCapV15R0001SYPCat6kPfc4,
       "cseCapV15R0101SYPCat6kPfc3": cseCapV15R0101SYPCat6kPfc3,
       "cseCapV15R0101SYPCat6kPfc4": cseCapV15R0101SYPCat6kPfc4,
       "cseCapNxOSV06R0104PN7k": cseCapNxOSV06R0104PN7k}
)
