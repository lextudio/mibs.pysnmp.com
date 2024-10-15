# SNMP MIB module (CISCO-POWER-ETHERNET-EXT-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-POWER-ETHERNET-EXT-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:01 2024
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

ciscoPowerEthernetExtCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 406)
)
ciscoPowerEthernetExtCapability.setRevisions(
        ("2013-07-16 00:00",
         "2012-12-12 00:00",
         "2012-04-04 00:00",
         "2009-05-29 00:00",
         "2008-10-28 00:00",
         "2007-06-29 00:00",
         "2007-06-27 00:00",
         "2007-02-08 00:00",
         "2006-12-20 00:00",
         "2006-10-19 00:00",
         "2004-06-15 00:00",
         "2004-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cPowerEthExtCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 1)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0401.setStatus(
        "current"
    )

cPowerEthExtCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 2)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0501.setStatus(
        "current"
    )

cPowerEthExtCapC3kV122SR035 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 3)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapC3kV122SR035.setProductRelease("CISCO IOS 12.2S(0.35) for Cat3k")
if mibBuilder.loadTexts:
    cPowerEthExtCapC3kV122SR035.setStatus(
        "current"
    )

cPowerEthExtCapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 4)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0601.setProductRelease("Cisco CatOS 8.6(1)")
if mibBuilder.loadTexts:
    cPowerEthExtCapCatOSV08R0601.setStatus(
        "current"
    )

cPowerEthExtCapC3kV122SU040 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 5)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapC3kV122SU040.setProductRelease("CISCO IOS 12.2S(0.40) for Cat3k")
if mibBuilder.loadTexts:
    cPowerEthExtCapC3kV122SU040.setStatus(
        "current"
    )

cPowerEthExtCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 6)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

cPowerEthExtCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 7)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500 
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cPowerEthExtCapV12R0252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 8)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0252SGPCat4K.setProductRelease("""\
Cisco IOS 12.2(52)SG on CAT4K family
                    switches.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0252SGPCat4K.setStatus(
        "current"
    )

cPowerEthExtCapV12R0233SXJ2PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 9)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXJ2PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV12R0233SXJ2PCat6K.setStatus(
        "current"
    )

cPowerEthExtCapV15R0101SGCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 10)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0101SGCat4K.setProductRelease("Cisco IOS 15.1(1)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0101SGCat4K.setStatus(
        "current"
    )

cPowerEthExtCapV15R0101SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 11)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0101SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0101SYPCat6K.setStatus(
        "current"
    )

cPowerEthExtCapV15R0102SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 406, 12)
)
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0102SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthExtCapV15R0102SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POWER-ETHERNET-EXT-CAPABILITY",
    **{"ciscoPowerEthernetExtCapability": ciscoPowerEthernetExtCapability,
       "cPowerEthExtCapCatOSV08R0401": cPowerEthExtCapCatOSV08R0401,
       "cPowerEthExtCapCatOSV08R0501": cPowerEthExtCapCatOSV08R0501,
       "cPowerEthExtCapC3kV122SR035": cPowerEthExtCapC3kV122SR035,
       "cPowerEthExtCapCatOSV08R0601": cPowerEthExtCapCatOSV08R0601,
       "cPowerEthExtCapC3kV122SU040": cPowerEthExtCapC3kV122SU040,
       "cPowerEthExtCapV12R0233SXHPCat6K": cPowerEthExtCapV12R0233SXHPCat6K,
       "cPowerEthExtCapV12R0233SXIPCat6K": cPowerEthExtCapV12R0233SXIPCat6K,
       "cPowerEthExtCapV12R0252SGPCat4K": cPowerEthExtCapV12R0252SGPCat4K,
       "cPowerEthExtCapV12R0233SXJ2PCat6K": cPowerEthExtCapV12R0233SXJ2PCat6K,
       "cPowerEthExtCapV15R0101SGCat4K": cPowerEthExtCapV15R0101SGCat4K,
       "cPowerEthExtCapV15R0101SYPCat6K": cPowerEthExtCapV15R0101SYPCat6K,
       "cPowerEthExtCapV15R0102SYPCat6K": cPowerEthExtCapV15R0102SYPCat6K}
)
