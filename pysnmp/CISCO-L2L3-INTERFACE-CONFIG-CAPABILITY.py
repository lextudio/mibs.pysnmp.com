# SNMP MIB module (CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:47 2024
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

ciscoL2L3IfConfigCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 326)
)
ciscoL2L3IfConfigCapability.setRevisions(
        ("2014-04-04 00:00",
         "2013-08-28 00:00",
         "2004-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoL2L3IfConfigCapV12R0119E = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 326, 1)
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapV12R0119E.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapV12R0119E.setStatus(
        "current"
    )

ciscoL2L3IfConfigCapNxOSV06R0202PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 326, 2)
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setProductRelease("""\
Cisco NX-OS 6.2(2) on 
                    Nexus 7000 series devices.""")
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setStatus(
        "current"
    )

ciscoL2L3IfConfigCapNxOSV06R0201PMds = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 326, 3)
)
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapNxOSV06R0201PMds.setProductRelease("Cisco NX-OS 6.2(1) on MDS series devices.")
if mibBuilder.loadTexts:
    ciscoL2L3IfConfigCapNxOSV06R0201PMds.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY",
    **{"ciscoL2L3IfConfigCapability": ciscoL2L3IfConfigCapability,
       "ciscoL2L3IfConfigCapV12R0119E": ciscoL2L3IfConfigCapV12R0119E,
       "ciscoL2L3IfConfigCapNxOSV06R0202PN7K": ciscoL2L3IfConfigCapNxOSV06R0202PN7K,
       "ciscoL2L3IfConfigCapNxOSV06R0201PMds": ciscoL2L3IfConfigCapNxOSV06R0201PMds}
)
