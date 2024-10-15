# SNMP MIB module (CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:08 2024
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

cSwitchHwCapacityCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 572)
)
cSwitchHwCapacityCapability.setRevisions(
        ("2014-03-03 00:01",
         "2013-07-26 00:01",
         "2013-07-16 00:01",
         "2011-09-28 00:01",
         "2008-10-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cSwitchHwCapacityCapV12R0233SXIPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 572, 1)
)
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapV12R0233SXIPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapV12R0233SXIPCat6k.setStatus(
        "current"
    )

cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 572, 2)
)
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                         series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setStatus(
        "current"
    )

cSwitchHwCapacityCapNxOSV06R0104PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 572, 3)
)
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0104PN7k.setProductRelease("Cisco NX-OS 6.1(4) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0104PN7k.setStatus(
        "current"
    )

cSwitchHwCapacityCapNxOSV06R0202PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 572, 4)
)
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0202PN7k.setProductRelease("Cisco NX-OS 6.2(2) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0202PN7k.setStatus(
        "current"
    )

cSwitchHwCapacityCapNxOSV06R0208PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 572, 5)
)
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0208PN7k.setProductRelease("Cisco NX-OS 6.2(8) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    cSwitchHwCapacityCapNxOSV06R0208PN7k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY",
    **{"cSwitchHwCapacityCapability": cSwitchHwCapacityCapability,
       "cSwitchHwCapacityCapV12R0233SXIPCat6k": cSwitchHwCapacityCapV12R0233SXIPCat6k,
       "cSwitchHwCapacityCapV15R0001SYPCat6kSup2T": cSwitchHwCapacityCapV15R0001SYPCat6kSup2T,
       "cSwitchHwCapacityCapNxOSV06R0104PN7k": cSwitchHwCapacityCapNxOSV06R0104PN7k,
       "cSwitchHwCapacityCapNxOSV06R0202PN7k": cSwitchHwCapacityCapNxOSV06R0202PN7k,
       "cSwitchHwCapacityCapNxOSV06R0208PN7k": cSwitchHwCapacityCapNxOSV06R0208PN7k}
)
