# SNMP MIB module (CISCO-AUTH-FRAMEWORK-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AUTH-FRAMEWORK-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:10 2024
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

ciscoAuthFrameworkCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 573)
)
ciscoAuthFrameworkCapability.setRevisions(
        ("2012-09-04 00:00",
         "2012-04-02 00:00",
         "2011-03-29 00:00",
         "2011-03-24 00:00",
         "2010-05-06 00:00",
         "2010-04-05 00:00",
         "2010-03-09 00:00",
         "2009-05-18 00:00",
         "2008-10-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cafCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 1)
)
if mibBuilder.loadTexts:
    cafCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cafCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cafCapV12R0233SXI2PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 2)
)
if mibBuilder.loadTexts:
    cafCapV12R0233SXI2PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cafCapV12R0233SXI2PCat6K.setStatus(
        "current"
    )

cafCapV12R0252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 3)
)
if mibBuilder.loadTexts:
    cafCapV12R0252SGPCat4K.setProductRelease("Cisco IOS 12.2(52)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cafCapV12R0252SGPCat4K.setStatus(
        "current"
    )

cafCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 4)
)
if mibBuilder.loadTexts:
    cafCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cafCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cafCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 5)
)
if mibBuilder.loadTexts:
    cafCapV12R0254SGPCat4K.setProductRelease("Cisco IOS 12.2(54)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cafCapV12R0254SGPCat4K.setStatus(
        "current"
    )

cafCapV12R0233SXJPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 6)
)
if mibBuilder.loadTexts:
    cafCapV12R0233SXJPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cafCapV12R0233SXJPCat6K.setStatus(
        "current"
    )

cafCapV15R0002SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 7)
)
if mibBuilder.loadTexts:
    cafCapV15R0002SGPCat4K.setProductRelease("Cisco IOS 15.0(2)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cafCapV15R0002SGPCat4K.setStatus(
        "current"
    )

cafCapV15R0101SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 8)
)
if mibBuilder.loadTexts:
    cafCapV15R0101SGPCat4K.setProductRelease("Cisco IOS 15.1(1)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cafCapV15R0101SGPCat4K.setStatus(
        "current"
    )

cafCapV15R0101SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 573, 9)
)
if mibBuilder.loadTexts:
    cafCapV15R0101SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cafCapV15R0101SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AUTH-FRAMEWORK-CAPABILITY",
    **{"ciscoAuthFrameworkCapability": ciscoAuthFrameworkCapability,
       "cafCapV12R0233SXIPCat6K": cafCapV12R0233SXIPCat6K,
       "cafCapV12R0233SXI2PCat6K": cafCapV12R0233SXI2PCat6K,
       "cafCapV12R0252SGPCat4K": cafCapV12R0252SGPCat4K,
       "cafCapV12R0233SXI4PCat6K": cafCapV12R0233SXI4PCat6K,
       "cafCapV12R0254SGPCat4K": cafCapV12R0254SGPCat4K,
       "cafCapV12R0233SXJPCat6K": cafCapV12R0233SXJPCat6K,
       "cafCapV15R0002SGPCat4K": cafCapV15R0002SGPCat4K,
       "cafCapV15R0101SGPCat4K": cafCapV15R0101SGPCat4K,
       "cafCapV15R0101SYPCat6K": cafCapV15R0101SYPCat6K}
)
