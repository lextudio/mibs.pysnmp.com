# SNMP MIB module (CISCO-IEEE8021-PAE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IEEE8021-PAE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:24 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIeee8021PaeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 314)
)
ciscoIeee8021PaeCapability.setRevisions(
        ("2012-09-05 00:00",
         "2011-03-25 16:00",
         "2010-11-01 00:00",
         "2010-03-22 00:00",
         "2009-08-26 00:00",
         "2008-06-02 00:00",
         "2007-07-09 00:00",
         "2004-01-13 00:00",
         "2003-09-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cIeee8021PaeCapV12R0111bEXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 1)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0111bEXCat6K.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0111bEXCat6K.setStatus(
        "current"
    )

ciscoIeee8021PaeCapCatOSV07R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 2)
)
if mibBuilder.loadTexts:
    ciscoIeee8021PaeCapCatOSV07R0101.setProductRelease("Cisco CatOS 7.1(1).")
if mibBuilder.loadTexts:
    ciscoIeee8021PaeCapCatOSV07R0101.setStatus(
        "current"
    )

ciscoIeee8021PaeCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 3)
)
if mibBuilder.loadTexts:
    ciscoIeee8021PaeCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIeee8021PaeCapCatOSV08R0301.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 4)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                          series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 5)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 6)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0252SGPCat4K.setProductRelease("Cisco IOS 12.2(52)SG on CAT4K family switches.")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0252SGPCat4K.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 7)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 8)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0250SYPCat6K.setStatus(
        "current"
    )

cIeee8021PaeCapV12R0233SXJPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 9)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXJPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV12R0233SXJPCat6K.setStatus(
        "current"
    )

cIeee8021PaeCapV15R0101SYCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 314, 10)
)
if mibBuilder.loadTexts:
    cIeee8021PaeCapV15R0101SYCat6K.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cIeee8021PaeCapV15R0101SYCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IEEE8021-PAE-CAPABILITY",
    **{"ciscoIeee8021PaeCapability": ciscoIeee8021PaeCapability,
       "cIeee8021PaeCapV12R0111bEXCat6K": cIeee8021PaeCapV12R0111bEXCat6K,
       "ciscoIeee8021PaeCapCatOSV07R0101": ciscoIeee8021PaeCapCatOSV07R0101,
       "ciscoIeee8021PaeCapCatOSV08R0301": ciscoIeee8021PaeCapCatOSV08R0301,
       "cIeee8021PaeCapV12R0233SXHPCat6K": cIeee8021PaeCapV12R0233SXHPCat6K,
       "cIeee8021PaeCapV12R0233SXIPCat6K": cIeee8021PaeCapV12R0233SXIPCat6K,
       "cIeee8021PaeCapV12R0252SGPCat4K": cIeee8021PaeCapV12R0252SGPCat4K,
       "cIeee8021PaeCapV12R0233SXI4PCat6K": cIeee8021PaeCapV12R0233SXI4PCat6K,
       "cIeee8021PaeCapV12R0250SYPCat6K": cIeee8021PaeCapV12R0250SYPCat6K,
       "cIeee8021PaeCapV12R0233SXJPCat6K": cIeee8021PaeCapV12R0233SXJPCat6K,
       "cIeee8021PaeCapV15R0101SYCat6K": cIeee8021PaeCapV15R0101SYCat6K}
)
