# SNMP MIB module (CISCO-SWITCH-FABRIC-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-FABRIC-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:07 2024
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

ciscoSwitchFabricCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 618)
)
ciscoSwitchFabricCapability.setRevisions(
        ("2014-09-16 00:00",
         "2013-07-17 00:00",
         "2013-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSwitchFabricCapNxOSV06R0104PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 618, 1)
)
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0104PN7k.setProductRelease("Cisco NX-OS 6.1(4) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0104PN7k.setStatus(
        "current"
    )

ciscoSwitchFabricCapNxOSV06R0201PMds = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 618, 2)
)
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0201PMds.setProductRelease("Cisco NX-OS 6.2(1) on MDS series devices.")
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0201PMds.setStatus(
        "current"
    )

ciscoSwitchFabricCapV15R0102SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 618, 3)
)
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapV15R0102SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapV15R0102SYPCat6K.setStatus(
        "current"
    )

ciscoSwitchFabricCapNxOSV06R0210PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 618, 4)
)
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0210PN7k.setProductRelease("Cisco NX-OS 6.2(10) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoSwitchFabricCapNxOSV06R0210PN7k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-FABRIC-CAPABILITY",
    **{"ciscoSwitchFabricCapability": ciscoSwitchFabricCapability,
       "ciscoSwitchFabricCapNxOSV06R0104PN7k": ciscoSwitchFabricCapNxOSV06R0104PN7k,
       "ciscoSwitchFabricCapNxOSV06R0201PMds": ciscoSwitchFabricCapNxOSV06R0201PMds,
       "ciscoSwitchFabricCapV15R0102SYPCat6K": ciscoSwitchFabricCapV15R0102SYPCat6K,
       "ciscoSwitchFabricCapNxOSV06R0210PN7k": ciscoSwitchFabricCapNxOSV06R0210PN7k}
)
