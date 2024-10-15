# SNMP MIB module (CISCO-PAGP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PAGP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:40 2024
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

ciscoPagpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 391)
)
ciscoPagpCapability.setRevisions(
        ("2011-09-27 00:00",
         "2010-11-17 00:00",
         "2010-05-06 00:00",
         "2004-03-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoPagpCapV12R0111bEXCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 1)
)
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0111bEXCat6k.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0111bEXCat6k.setStatus(
        "current"
    )

ciscoPagpCapV12R0217aSXCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 2)
)
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0217aSXCat6k.setProductRelease("""\
Cisco IOS 12.2(17a)SX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0217aSXCat6k.setStatus(
        "current"
    )

ciscoPagpCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 3)
)
if mibBuilder.loadTexts:
    ciscoPagpCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoPagpCapCatOSV08R0101.setStatus(
        "current"
    )

ciscoPagpCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 4)
)
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0254SGPCat4K.setProductRelease("Cisco IOS 12.2(54)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0254SGPCat4K.setStatus(
        "current"
    )

ciscoPagpCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 5)
)
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPagpCapV12R0250SYPCat6K.setStatus(
        "current"
    )

ciscoPagpCapV15R0001SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 391, 6)
)
if mibBuilder.loadTexts:
    ciscoPagpCapV15R0001SYPCat6k.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoPagpCapV15R0001SYPCat6k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PAGP-CAPABILITY",
    **{"ciscoPagpCapability": ciscoPagpCapability,
       "ciscoPagpCapV12R0111bEXCat6k": ciscoPagpCapV12R0111bEXCat6k,
       "ciscoPagpCapV12R0217aSXCat6k": ciscoPagpCapV12R0217aSXCat6k,
       "ciscoPagpCapCatOSV08R0101": ciscoPagpCapCatOSV08R0101,
       "ciscoPagpCapV12R0254SGPCat4K": ciscoPagpCapV12R0254SGPCat4K,
       "ciscoPagpCapV12R0250SYPCat6K": ciscoPagpCapV12R0250SYPCat6K,
       "ciscoPagpCapV15R0001SYPCat6k": ciscoPagpCapV15R0001SYPCat6k}
)
