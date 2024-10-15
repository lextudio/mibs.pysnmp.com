# SNMP MIB module (CISCO-L2-TUNNEL-CONFIG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2-TUNNEL-CONFIG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:45 2024
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

ciscoL2TunnelConfigCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 334)
)
ciscoL2TunnelConfigCapability.setRevisions(
        ("2010-05-14 00:00",
         "2008-10-27 00:00",
         "2007-07-09 00:00",
         "2005-07-05 00:00",
         "2004-06-21 00:00",
         "2003-08-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cL2TunConfCapCatOSV07R0501Cat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 1)
)
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV07R0501Cat6k.setProductRelease("""\
Cisco CatOS 7.5(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV07R0501Cat6k.setStatus(
        "current"
    )

cL2TunnelConfigCapV12R0214SX = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 2)
)
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0214SX.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0214SX.setStatus(
        "current"
    )

cL2TunConfCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 3)
)
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV08R0401.setStatus(
        "current"
    )

cL2TunConfCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 4)
)
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    cL2TunConfCapCatOSV08R0501.setStatus(
        "current"
    )

cL2TunnelConfigCapV12R0233SXHPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 5)
)
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0233SXHPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0233SXHPCat6k.setStatus(
        "current"
    )

cL2TunnelConfigCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 6)
)
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cL2TunnelConfigCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 334, 7)
)
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0254SGPCat4K.setProductRelease("""\
Cisco IOS 12.2(54)SG on CAT4K family switches,
                    except LAN Base images.""")
if mibBuilder.loadTexts:
    cL2TunnelConfigCapV12R0254SGPCat4K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2-TUNNEL-CONFIG-CAPABILITY",
    **{"ciscoL2TunnelConfigCapability": ciscoL2TunnelConfigCapability,
       "cL2TunConfCapCatOSV07R0501Cat6k": cL2TunConfCapCatOSV07R0501Cat6k,
       "cL2TunnelConfigCapV12R0214SX": cL2TunnelConfigCapV12R0214SX,
       "cL2TunConfCapCatOSV08R0401": cL2TunConfCapCatOSV08R0401,
       "cL2TunConfCapCatOSV08R0501": cL2TunConfCapCatOSV08R0501,
       "cL2TunnelConfigCapV12R0233SXHPCat6k": cL2TunnelConfigCapV12R0233SXHPCat6k,
       "cL2TunnelConfigCapV12R0233SXIPCat6K": cL2TunnelConfigCapV12R0233SXIPCat6K,
       "cL2TunnelConfigCapV12R0254SGPCat4K": cL2TunnelConfigCapV12R0254SGPCat4K}
)
