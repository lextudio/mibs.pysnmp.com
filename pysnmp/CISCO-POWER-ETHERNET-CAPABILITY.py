# SNMP MIB module (CISCO-POWER-ETHERNET-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-POWER-ETHERNET-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:00 2024
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

ciscoPowerEthernetCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 412)
)
ciscoPowerEthernetCapability.setRevisions(
        ("2012-09-04 00:00",
         "2012-04-06 00:00",
         "2009-02-14 00:00",
         "2007-07-09 00:00",
         "2007-02-08 00:00",
         "2006-05-31 00:00",
         "2004-06-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cPowerEthernetCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 1)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    cPowerEthernetCapCatOSV08R0401.setStatus(
        "current"
    )

cPowerEthernetCapC3kV122SR035 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 2)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapC3kV122SR035.setProductRelease("CISCO IOS 12.2S(0.35) for cat3k")
if mibBuilder.loadTexts:
    cPowerEthernetCapC3kV122SR035.setStatus(
        "current"
    )

cPowerEthernetCapV12RO233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 3)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO233SXHPCat6K.setStatus(
        "current"
    )

cPowerEthernetCapV12RO252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 4)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO252SGPCat4K.setProductRelease("""\
Cisco IOS 12.2(52)SG on CAT4K family
                    switches.""")
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO252SGPCat4K.setStatus(
        "current"
    )

cPowerEthernetCapV12RO233SXJ2PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 5)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO233SXJ2PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthernetCapV12RO233SXJ2PCat6K.setStatus(
        "current"
    )

cPowerEthernetCapV15RO101SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 412, 6)
)
if mibBuilder.loadTexts:
    cPowerEthernetCapV15RO101SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cPowerEthernetCapV15RO101SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POWER-ETHERNET-CAPABILITY",
    **{"ciscoPowerEthernetCapability": ciscoPowerEthernetCapability,
       "cPowerEthernetCapCatOSV08R0401": cPowerEthernetCapCatOSV08R0401,
       "cPowerEthernetCapC3kV122SR035": cPowerEthernetCapC3kV122SR035,
       "cPowerEthernetCapV12RO233SXHPCat6K": cPowerEthernetCapV12RO233SXHPCat6K,
       "cPowerEthernetCapV12RO252SGPCat4K": cPowerEthernetCapV12RO252SGPCat4K,
       "cPowerEthernetCapV12RO233SXJ2PCat6K": cPowerEthernetCapV12RO233SXJ2PCat6K,
       "cPowerEthernetCapV15RO101SYPCat6K": cPowerEthernetCapV15RO101SYPCat6K}
)
