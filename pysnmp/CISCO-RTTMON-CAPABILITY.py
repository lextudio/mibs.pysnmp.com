# SNMP MIB module (CISCO-RTTMON-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:46 2024
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

ciscoRttMonCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 62)
)
ciscoRttMonCapability.setRevisions(
        ("2006-03-02 00:00",
         "2005-12-14 00:00",
         "2005-06-09 00:00",
         "2005-05-01 00:00",
         "2004-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoRttMonCapabilityRev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 1)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapabilityRev1.setProductRelease("Cisco IOS 12.3(6th)T")
if mibBuilder.loadTexts:
    ciscoRttMonCapabilityRev1.setStatus(
        "current"
    )

ciscoRttMonCapV12R0402ndT = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 2)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0402ndT.setProductRelease("Cisco IOS 12.4(2nd)T")
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0402ndT.setStatus(
        "current"
    )

ciscoRttMonCapV12R0206thSX = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 3)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0206thSX.setProductRelease("Cisco IOS 12.2(6th)SX")
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0206thSX.setStatus(
        "current"
    )

ciscoRttMonCapV12R0403rdT = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 4)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0403rdT.setProductRelease("Cisco IOS 12.4(3rd)T")
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0403rdT.setStatus(
        "current"
    )

ciscoRttMonCapCRS1V3R3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 5)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapCRS1V3R3.setProductRelease("Cisco IOS XR release 3.3 for CRS-1")
if mibBuilder.loadTexts:
    ciscoRttMonCapCRS1V3R3.setStatus(
        "current"
    )

ciscoRttMonCapV12R0201SRB = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 62, 6)
)
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0201SRB.setProductRelease("Cisco IOS 12.2(01)SRB")
if mibBuilder.loadTexts:
    ciscoRttMonCapV12R0201SRB.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-CAPABILITY",
    **{"ciscoRttMonCapability": ciscoRttMonCapability,
       "ciscoRttMonCapabilityRev1": ciscoRttMonCapabilityRev1,
       "ciscoRttMonCapV12R0402ndT": ciscoRttMonCapV12R0402ndT,
       "ciscoRttMonCapV12R0206thSX": ciscoRttMonCapV12R0206thSX,
       "ciscoRttMonCapV12R0403rdT": ciscoRttMonCapV12R0403rdT,
       "ciscoRttMonCapCRS1V3R3": ciscoRttMonCapCRS1V3R3,
       "ciscoRttMonCapV12R0201SRB": ciscoRttMonCapV12R0201SRB}
)
