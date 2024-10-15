# SNMP MIB module (CISCO-SWITCH-STATS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-STATS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:17 2024
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

ciscoSwitchStatsCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 600)
)
ciscoSwitchStatsCapability.setRevisions(
        ("2013-09-25 00:00",
         "2013-07-26 00:00",
         "2010-11-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

csstCapV12R0250SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 600, 1)
)
if mibBuilder.loadTexts:
    csstCapV12R0250SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices with PFC4 card.""")
if mibBuilder.loadTexts:
    csstCapV12R0250SYPCat6kPfc4.setStatus(
        "current"
    )

csstCapNxOSV06R0104PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 600, 2)
)
if mibBuilder.loadTexts:
    csstCapNxOSV06R0104PN7k.setProductRelease("Cisco NX-OS 6.1(4) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    csstCapNxOSV06R0104PN7k.setStatus(
        "current"
    )

csstCapNxOSV06R0201PMds = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 600, 3)
)
if mibBuilder.loadTexts:
    csstCapNxOSV06R0201PMds.setProductRelease("Cisco NX-OS 6.2(1) on MDS series devices.")
if mibBuilder.loadTexts:
    csstCapNxOSV06R0201PMds.setStatus(
        "current"
    )

csstCapV15R0102SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 600, 4)
)
if mibBuilder.loadTexts:
    csstCapV15R0102SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                    series devices with PFC4 card.""")
if mibBuilder.loadTexts:
    csstCapV15R0102SYPCat6kPfc4.setStatus(
        "current"
    )

csstCapV15R0102SYPCat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 600, 5)
)
if mibBuilder.loadTexts:
    csstCapV15R0102SYPCat6kPfc3.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                    series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    csstCapV15R0102SYPCat6kPfc3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-STATS-CAPABILITY",
    **{"ciscoSwitchStatsCapability": ciscoSwitchStatsCapability,
       "csstCapV12R0250SYPCat6kPfc4": csstCapV12R0250SYPCat6kPfc4,
       "csstCapNxOSV06R0104PN7k": csstCapNxOSV06R0104PN7k,
       "csstCapNxOSV06R0201PMds": csstCapNxOSV06R0201PMds,
       "csstCapV15R0102SYPCat6kPfc4": csstCapV15R0102SYPCat6kPfc4,
       "csstCapV15R0102SYPCat6kPfc3": csstCapV15R0102SYPCat6kPfc3}
)
