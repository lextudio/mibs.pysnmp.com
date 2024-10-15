# SNMP MIB module (CISCO-PAE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PAE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:39 2024
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

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

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

ciscoPaeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 319)
)
ciscoPaeCapability.setRevisions(
        ("2010-11-01 00:00",
         "2010-03-22 00:00",
         "2010-03-15 00:00",
         "2009-12-31 00:00",
         "2008-11-06 00:00",
         "2008-11-04 00:00",
         "2008-10-20 00:00",
         "2008-04-24 00:00",
         "2007-07-09 00:00",
         "2007-04-26 00:00",
         "2007-02-27 00:00",
         "2005-09-05 00:00",
         "2004-01-16 00:00",
         "2003-08-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoPaeCapV12R0111bEXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 1)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0111bEXCat6K.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0111bEXCat6K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV07R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 2)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0101.setProductRelease("Cisco CatOS 7.1(1).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0101.setStatus(
        "current"
    )

ciscoPaeCapCatOSV07R0501Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 3)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0501Cat6K.setProductRelease("""\
Cisco CatOS 7.5(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0501Cat6K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV07R0601Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 4)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0601Cat6K.setProductRelease("""\
Cisco CatOS 7.6(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV07R0601Cat6K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0101Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 5)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0101Cat6K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0101Cat6K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0101Cat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 6)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0101Cat4K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 4000 series
                    devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0101Cat4K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 7)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0301.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 8)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0501.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 9)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0601.setProductRelease("Cisco CatOS 8.6(1).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0601.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0602 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 10)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0602.setProductRelease("Cisco CatOS 8.6(2).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0602.setStatus(
        "current"
    )

ciscoPaeCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 11)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0701 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 12)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0701.setProductRelease("Cisco CatOS 8.7(1).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0701.setStatus(
        "current"
    )

ciscoPaeCapV12R0246SECat3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 13)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0246SECat3K.setProductRelease("Cisco IOS 12.2(46)SE.")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0246SECat3K.setStatus(
        "current"
    )

ciscoPaeCapCatOSV08R0702 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 14)
)
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0702.setProductRelease("Cisco CatOS 8.7(2).")
if mibBuilder.loadTexts:
    ciscoPaeCapCatOSV08R0702.setStatus(
        "current"
    )

ciscoPaeCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 15)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

ciscoPaeCapV120252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 16)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV120252SGPCat4K.setProductRelease("Cisco IOS 12.2(52)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    ciscoPaeCapV120252SGPCat4K.setStatus(
        "current"
    )

ciscoPaeCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 17)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

ciscoPaeCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 319, 18)
)
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPaeCapV12R0250SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PAE-CAPABILITY",
    **{"ciscoPaeCapability": ciscoPaeCapability,
       "ciscoPaeCapV12R0111bEXCat6K": ciscoPaeCapV12R0111bEXCat6K,
       "ciscoPaeCapCatOSV07R0101": ciscoPaeCapCatOSV07R0101,
       "ciscoPaeCapCatOSV07R0501Cat6K": ciscoPaeCapCatOSV07R0501Cat6K,
       "ciscoPaeCapCatOSV07R0601Cat6K": ciscoPaeCapCatOSV07R0601Cat6K,
       "ciscoPaeCapCatOSV08R0101Cat6K": ciscoPaeCapCatOSV08R0101Cat6K,
       "ciscoPaeCapCatOSV08R0101Cat4K": ciscoPaeCapCatOSV08R0101Cat4K,
       "ciscoPaeCapCatOSV08R0301": ciscoPaeCapCatOSV08R0301,
       "ciscoPaeCapCatOSV08R0501": ciscoPaeCapCatOSV08R0501,
       "ciscoPaeCapCatOSV08R0601": ciscoPaeCapCatOSV08R0601,
       "ciscoPaeCapCatOSV08R0602": ciscoPaeCapCatOSV08R0602,
       "ciscoPaeCapV12R0233SXHPCat6K": ciscoPaeCapV12R0233SXHPCat6K,
       "ciscoPaeCapCatOSV08R0701": ciscoPaeCapCatOSV08R0701,
       "ciscoPaeCapV12R0246SECat3K": ciscoPaeCapV12R0246SECat3K,
       "ciscoPaeCapCatOSV08R0702": ciscoPaeCapCatOSV08R0702,
       "ciscoPaeCapV12R0233SXIPCat6K": ciscoPaeCapV12R0233SXIPCat6K,
       "ciscoPaeCapV120252SGPCat4K": ciscoPaeCapV120252SGPCat4K,
       "ciscoPaeCapV12R0233SXI4PCat6K": ciscoPaeCapV12R0233SXI4PCat6K,
       "ciscoPaeCapV12R0250SYPCat6K": ciscoPaeCapV12R0250SYPCat6K}
)
