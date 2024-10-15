# SNMP MIB module (CISCO-BRIDGE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BRIDGE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:20 2024
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

ciscoBridgeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 106)
)
ciscoBridgeCapability.setRevisions(
        ("2014-09-18 00:00",
         "2013-07-16 00:00",
         "2011-07-26 00:00",
         "2010-12-01 00:00",
         "2010-11-18 00:00",
         "2010-09-09 00:00",
         "2010-06-10 00:00",
         "2010-03-02 00:00",
         "2007-03-28 00:00",
         "2006-06-12 00:00",
         "1994-08-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoBridgeCapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 2)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapCatOSV08R0601.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapCatOSV08R0601.setStatus(
        "current"
    )

ciscoBridgeCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 3)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

ciscoBridgeCapNxOSV04R0201N0101PN5k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 4)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV04R0201N0101PN5k.setProductRelease("""\
Cisco NX-OS 4.2(1)N1(1) on Nexus 5000
                         series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV04R0201N0101PN5k.setStatus(
        "current"
    )

ciscoBridgeCapNxOSV05R0002PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 5)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0002PN7k.setProductRelease("""\
Cisco NX-OS 5.0(2) on Nexus 7000
                         series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0002PN7k.setStatus(
        "current"
    )

ciscoBridgeCapV12R2SEPCat3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 6)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R2SEPCat3K.setProductRelease("""\
Cisco IOS 12.2SE on Catalyst 3K
                        series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R2SEPCat3K.setStatus(
        "current"
    )

ciscoBridgeCapNxOSV05R0101PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 7)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0101PN7k.setProductRelease("""\
Cisco NX-OS 5.1(1) on Nexus 7000
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0101PN7k.setStatus(
        "current"
    )

ciscoBridgeCapV12R4SEPC1861 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 8)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R4SEPC1861.setProductRelease("""\
OS=IOS
                     OSVERSION=Cisco IOS 12.4,15.1T
                     PLATFORM=c1861""")
if mibBuilder.loadTexts:
    ciscoBridgeCapV12R4SEPC1861.setStatus(
        "current"
    )

ciscoBridgeCapNxOSV05R0201PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 9)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0201PN7k.setProductRelease("""\
Cisco NX-OS 5.2(1) on Nexus 7000
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV05R0201PN7k.setStatus(
        "current"
    )

ciscoBridgeCapNxOSV06R0201PMds = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 106, 10)
)
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV06R0201PMds.setProductRelease("""\
Cisco NX-OS 6.2(1) on MDS 9700
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoBridgeCapNxOSV06R0201PMds.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BRIDGE-CAPABILITY",
    **{"ciscoBridgeCapability": ciscoBridgeCapability,
       "ciscoBridgeCapCatOSV08R0601": ciscoBridgeCapCatOSV08R0601,
       "ciscoBridgeCapV12R0233SXHPCat6K": ciscoBridgeCapV12R0233SXHPCat6K,
       "ciscoBridgeCapNxOSV04R0201N0101PN5k": ciscoBridgeCapNxOSV04R0201N0101PN5k,
       "ciscoBridgeCapNxOSV05R0002PN7k": ciscoBridgeCapNxOSV05R0002PN7k,
       "ciscoBridgeCapV12R2SEPCat3K": ciscoBridgeCapV12R2SEPCat3K,
       "ciscoBridgeCapNxOSV05R0101PN7k": ciscoBridgeCapNxOSV05R0101PN7k,
       "ciscoBridgeCapV12R4SEPC1861": ciscoBridgeCapV12R4SEPC1861,
       "ciscoBridgeCapNxOSV05R0201PN7k": ciscoBridgeCapNxOSV05R0201PN7k,
       "ciscoBridgeCapNxOSV06R0201PMds": ciscoBridgeCapNxOSV06R0201PMds}
)
