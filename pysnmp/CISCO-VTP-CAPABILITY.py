# SNMP MIB module (CISCO-VTP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VTP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:42 2024
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

ciscoVtpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 329)
)
ciscoVtpCapability.setRevisions(
        ("2013-09-27 00:00",
         "2013-08-27 00:00",
         "2011-09-30 00:00",
         "2011-07-31 00:00",
         "2011-04-06 00:00",
         "2011-03-30 00:00",
         "2010-11-10 00:00",
         "2010-03-22 00:00",
         "2010-03-10 00:00",
         "2008-10-28 00:00",
         "2008-05-28 00:00",
         "2007-07-18 00:00",
         "2006-03-15 00:00",
         "2005-03-09 00:00",
         "2004-04-15 00:00",
         "2003-12-01 00:00",
         "2003-09-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoVtpCapV12R0119ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 1)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0119ECat6K.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0119ECat6K.setStatus(
        "current"
    )

ciscoVtpCapV12R0217SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 2)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0217SXCat6K.setProductRelease("""\
Cisco IOS 12.2(17)SX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0217SXCat6K.setStatus(
        "current"
    )

ciscoVtpCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 3)
)
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0101.setStatus(
        "current"
    )

ciscoVtpCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 4)
)
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0301.setProductRelease("Cisco CatOS 8.3(1).")
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0301.setStatus(
        "current"
    )

ciscoVtpCapV12R0217SXACat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 5)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0217SXACat6K.setProductRelease("""\
Cisco IOS 12.2(17)SXA on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0217SXACat6K.setStatus(
        "current"
    )

ciscoVtpCapV12R0218SXECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 6)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0218SXECat6K.setProductRelease("""\
Cisco IOS 12.2(18)SXE on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0218SXECat6K.setStatus(
        "current"
    )

ciscoVtpCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 7)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

ciscoVtpCapCatOSV08R0701 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 8)
)
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0701.setProductRelease("Cisco CatOS 8.7(1).")
if mibBuilder.loadTexts:
    ciscoVtpCapCatOSV08R0701.setStatus(
        "current"
    )

ciscoVtpCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 9)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

ciscoVtpCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 10)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

ciscoVtpCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 11)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0254SGPCat4K.setProductRelease("Cisco IOS 12.2(54)SG on CAT4K family switches.")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0254SGPCat4K.setStatus(
        "current"
    )

ciscoVtpCapNxOSV05R0101PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 12)
)
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0101PN7K.setProductRelease("Cisco NX-OS 5.1(1) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0101PN7K.setStatus(
        "current"
    )

ciscoVtpCapV12R0233SXJPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 13)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXJPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV12R0233SXJPCat6k.setStatus(
        "current"
    )

ciscoVtpCapNxOSV05R0002PN5k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 14)
)
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0002PN5k.setProductRelease("Cisco NX-OS 5.0(2) on Nexus 5000 series devices.")
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0002PN5k.setStatus(
        "current"
    )

ciscoVtpCapNxOSV05R0201PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 15)
)
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0201PN7K.setProductRelease("Cisco NX-OS 5.2(1) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV05R0201PN7K.setStatus(
        "current"
    )

ciscoVtpCapV15R0001SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 16)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV15R0001SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV15R0001SYPCat6kSup2T.setStatus(
        "current"
    )

ciscoVtpCapNxOSV06R0101PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 17)
)
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV06R0101PN7K.setProductRelease("Cisco NX-OS 6.1(1) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoVtpCapNxOSV06R0101PN7K.setStatus(
        "current"
    )

ciscoVtpCapV15R0102SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 329, 18)
)
if mibBuilder.loadTexts:
    ciscoVtpCapV15R0102SYPCat6k.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoVtpCapV15R0102SYPCat6k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VTP-CAPABILITY",
    **{"ciscoVtpCapability": ciscoVtpCapability,
       "ciscoVtpCapV12R0119ECat6K": ciscoVtpCapV12R0119ECat6K,
       "ciscoVtpCapV12R0217SXCat6K": ciscoVtpCapV12R0217SXCat6K,
       "ciscoVtpCapCatOSV08R0101": ciscoVtpCapCatOSV08R0101,
       "ciscoVtpCapCatOSV08R0301": ciscoVtpCapCatOSV08R0301,
       "ciscoVtpCapV12R0217SXACat6K": ciscoVtpCapV12R0217SXACat6K,
       "ciscoVtpCapV12R0218SXECat6K": ciscoVtpCapV12R0218SXECat6K,
       "ciscoVtpCapV12R0233SXHPCat6K": ciscoVtpCapV12R0233SXHPCat6K,
       "ciscoVtpCapCatOSV08R0701": ciscoVtpCapCatOSV08R0701,
       "ciscoVtpCapV12R0233SXIPCat6K": ciscoVtpCapV12R0233SXIPCat6K,
       "ciscoVtpCapV12R0233SXI4PCat6K": ciscoVtpCapV12R0233SXI4PCat6K,
       "ciscoVtpCapV12R0254SGPCat4K": ciscoVtpCapV12R0254SGPCat4K,
       "ciscoVtpCapNxOSV05R0101PN7K": ciscoVtpCapNxOSV05R0101PN7K,
       "ciscoVtpCapV12R0233SXJPCat6k": ciscoVtpCapV12R0233SXJPCat6k,
       "ciscoVtpCapNxOSV05R0002PN5k": ciscoVtpCapNxOSV05R0002PN5k,
       "ciscoVtpCapNxOSV05R0201PN7K": ciscoVtpCapNxOSV05R0201PN7K,
       "ciscoVtpCapV15R0001SYPCat6kSup2T": ciscoVtpCapV15R0001SYPCat6kSup2T,
       "ciscoVtpCapNxOSV06R0101PN7K": ciscoVtpCapNxOSV06R0101PN7K,
       "ciscoVtpCapV15R0102SYPCat6k": ciscoVtpCapV15R0102SYPCat6k}
)
