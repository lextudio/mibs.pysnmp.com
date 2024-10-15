# SNMP MIB module (CISCO-CAT6K-CROSSBAR-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAT6K-CROSSBAR-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:00 2024
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

ciscoCat6kCrossbarCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 356)
)
ciscoCat6kCrossbarCapability.setRevisions(
        ("2013-07-25 00:00",
         "2010-11-24 00:00",
         "2010-03-11 00:00",
         "2008-10-22 00:00",
         "2008-03-24 00:00",
         "2008-03-14 00:00",
         "2007-11-19 00:00",
         "2007-06-28 00:00",
         "2007-01-03 00:00",
         "2005-06-22 00:00",
         "2005-05-03 00:00",
         "2004-10-19 00:00",
         "2004-04-19 00:00",
         "2004-04-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ccXbarCapV12R0108aEXCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 1)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0108aEXCat6KSup2.setProductRelease("""\
Cisco IOS 12.1(8a)EX on Catalyst 6000/6500
                         and Cisco 7600 series devices with 
                         Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0108aEXCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0214SXCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 2)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0214SXCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6500 
                        and Cisco 7600 series devices with 
                        Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0214SXCat6KSup720.setStatus(
        "current"
    )

ccXbarCapCatOSV06R0301Cat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 3)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV06R0301Cat6KSup2.setProductRelease("""\
Cisco CatOS 6.3(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices
                         with Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV06R0301Cat6KSup2.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0101Cat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 4)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0101Cat6KSup2.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices
                         with Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0101Cat6KSup2.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0101Cat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 5)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0101Cat6KSup720.setProductRelease("""\
Cisco CatOS 8.1(1) on  Catalyst 6500
                        and Cisco 7600 series devices with 
                        Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0101Cat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0218SXDCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 6)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXDCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 
                        and Cisco 7600 series devices with 
                        Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXDCat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0218SXDCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 7)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXDCat6KSup2.setProductRelease("""\
Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 
                        and Cisco 7600 series devices with 
                        Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXDCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0119EPCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 8)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0119EPCat6KSup2.setProductRelease("""\
Cisco IOS 12.1(19)E on Catalyst 6000/6500
                         and Cisco 7600 series devices with 
                         Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0119EPCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0123E01PCat6KSup1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 9)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0123E01PCat6KSup1.setProductRelease("""\
Cisco IOS 12.1(23)E1 on Catalyst 6000/6500 
                        series devices with Supervisor 1 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0123E01PCat6KSup1.setStatus(
        "current"
    )

ccXbarCapV12R0123E01PCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 10)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0123E01PCat6KSup2.setProductRelease("""\
Cisco IOS 12.1(23)E1 on Catalyst 6000/6500
                         and Cisco 7600 series devices with 
                         Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0123E01PCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R012504EPCat6KSup1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 11)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R012504EPCat6KSup1.setProductRelease("""\
Cisco IOS 12.1(25.04)E on Catalyst 6000/6500 
                        series devices with Supervisor 1 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R012504EPCat6KSup1.setStatus(
        "current"
    )

ccXbarCapV12R012504EPCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 12)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R012504EPCat6KSup2.setProductRelease("""\
Cisco IOS 12.1(25.04)E on Catalyst 6000/6500
                         and Cisco 7600 series devices with 
                         Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R012504EPCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0218SXFPCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 13)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup2.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 
                        and Cisco 7600 series devices with 
                        Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0218SXFPCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 14)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 
                        and Cisco 7600 series devices with 
                        Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0218SXFPCat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 15)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup32.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 
                        and Cisco 7600 series devices with 
                        Supervisor 32 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0218SXFPCat6KSup32.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0601Cat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 16)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0601Cat6KSup32.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6500
                        series devices with Supervisor 32 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0601Cat6KSup32.setStatus(
        "current"
    )

ccXbarCapV12R0233SXHPCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 17)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXHPCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                        series devices with Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXHPCat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0233SXHPCat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 18)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXHPCat6KSup32.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                     series devices with Supervisor 32 present
                     and ME-C65xx series devices.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXHPCat6KSup32.setStatus(
        "current"
    )

ccXbarCapV12R0233SXH01PCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 19)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXH01PCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500
                        series devices with Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXH01PCat6KSup720.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0701PCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 20)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup720.setProductRelease("""\
Cisco CatOS 8.7(1) on  Catalyst 6000/6500
                        and Cisco 7600 series devices with 
                        Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup720.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0701PCat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 21)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup32.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6500
                     series devices with Supervisor 32 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup32.setStatus(
        "current"
    )

ccXbarCapCatOSV08R0701PCat6KSup2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 22)
)
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup2.setProductRelease("""\
Cisco CatOS 8.7(1) on  Catalyst 6000/6500
                     and Cisco 7600 series devices with 
                     Supervisor 2 present.""")
if mibBuilder.loadTexts:
    ccXbarCapCatOSV08R0701PCat6KSup2.setStatus(
        "current"
    )

ccXbarCapV12R0233SXIPCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 23)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXIPCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                     series devices with Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXIPCat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0233SXIPCat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 24)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXIPCat6KSup32.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                     series devices with Supervisor 32 present
                     and ME-C65xx series devices.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXIPCat6KSup32.setStatus(
        "current"
    )

ccXbarCapV12R0233SXI4PCat6KSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 25)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXI4PCat6KSup720.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                     series devices with Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXI4PCat6KSup720.setStatus(
        "current"
    )

ccXbarCapV12R0233SXI4PCat6KSup32 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 26)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXI4PCat6KSup32.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                     series devices with Supervisor 32 present
                     and ME-C65xx series devices.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0233SXI4PCat6KSup32.setStatus(
        "current"
    )

ccXbarCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 27)
)
if mibBuilder.loadTexts:
    ccXbarCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    ccXbarCapV12R0250SYPCat6K.setStatus(
        "current"
    )

ccXbarCapV15R0102SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 28)
)
if mibBuilder.loadTexts:
    ccXbarCapV15R0102SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                     series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    ccXbarCapV15R0102SYPCat6kSup2T.setStatus(
        "current"
    )

ccXbarCapV15R0102SYPCat6kSup720 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 356, 29)
)
if mibBuilder.loadTexts:
    ccXbarCapV15R0102SYPCat6kSup720.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                     series devices with Supervisor 720 present.""")
if mibBuilder.loadTexts:
    ccXbarCapV15R0102SYPCat6kSup720.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAT6K-CROSSBAR-CAPABILITY",
    **{"ciscoCat6kCrossbarCapability": ciscoCat6kCrossbarCapability,
       "ccXbarCapV12R0108aEXCat6KSup2": ccXbarCapV12R0108aEXCat6KSup2,
       "ccXbarCapV12R0214SXCat6KSup720": ccXbarCapV12R0214SXCat6KSup720,
       "ccXbarCapCatOSV06R0301Cat6KSup2": ccXbarCapCatOSV06R0301Cat6KSup2,
       "ccXbarCapCatOSV08R0101Cat6KSup2": ccXbarCapCatOSV08R0101Cat6KSup2,
       "ccXbarCapCatOSV08R0101Cat6KSup720": ccXbarCapCatOSV08R0101Cat6KSup720,
       "ccXbarCapV12R0218SXDCat6KSup720": ccXbarCapV12R0218SXDCat6KSup720,
       "ccXbarCapV12R0218SXDCat6KSup2": ccXbarCapV12R0218SXDCat6KSup2,
       "ccXbarCapV12R0119EPCat6KSup2": ccXbarCapV12R0119EPCat6KSup2,
       "ccXbarCapV12R0123E01PCat6KSup1": ccXbarCapV12R0123E01PCat6KSup1,
       "ccXbarCapV12R0123E01PCat6KSup2": ccXbarCapV12R0123E01PCat6KSup2,
       "ccXbarCapV12R012504EPCat6KSup1": ccXbarCapV12R012504EPCat6KSup1,
       "ccXbarCapV12R012504EPCat6KSup2": ccXbarCapV12R012504EPCat6KSup2,
       "ccXbarCapV12R0218SXFPCat6KSup2": ccXbarCapV12R0218SXFPCat6KSup2,
       "ccXbarCapV12R0218SXFPCat6KSup720": ccXbarCapV12R0218SXFPCat6KSup720,
       "ccXbarCapV12R0218SXFPCat6KSup32": ccXbarCapV12R0218SXFPCat6KSup32,
       "ccXbarCapCatOSV08R0601Cat6KSup32": ccXbarCapCatOSV08R0601Cat6KSup32,
       "ccXbarCapV12R0233SXHPCat6KSup720": ccXbarCapV12R0233SXHPCat6KSup720,
       "ccXbarCapV12R0233SXHPCat6KSup32": ccXbarCapV12R0233SXHPCat6KSup32,
       "ccXbarCapV12R0233SXH01PCat6KSup720": ccXbarCapV12R0233SXH01PCat6KSup720,
       "ccXbarCapCatOSV08R0701PCat6KSup720": ccXbarCapCatOSV08R0701PCat6KSup720,
       "ccXbarCapCatOSV08R0701PCat6KSup32": ccXbarCapCatOSV08R0701PCat6KSup32,
       "ccXbarCapCatOSV08R0701PCat6KSup2": ccXbarCapCatOSV08R0701PCat6KSup2,
       "ccXbarCapV12R0233SXIPCat6KSup720": ccXbarCapV12R0233SXIPCat6KSup720,
       "ccXbarCapV12R0233SXIPCat6KSup32": ccXbarCapV12R0233SXIPCat6KSup32,
       "ccXbarCapV12R0233SXI4PCat6KSup720": ccXbarCapV12R0233SXI4PCat6KSup720,
       "ccXbarCapV12R0233SXI4PCat6KSup32": ccXbarCapV12R0233SXI4PCat6KSup32,
       "ccXbarCapV12R0250SYPCat6K": ccXbarCapV12R0250SYPCat6K,
       "ccXbarCapV15R0102SYPCat6kSup2T": ccXbarCapV15R0102SYPCat6kSup2T,
       "ccXbarCapV15R0102SYPCat6kSup720": ccXbarCapV15R0102SYPCat6kSup720}
)
