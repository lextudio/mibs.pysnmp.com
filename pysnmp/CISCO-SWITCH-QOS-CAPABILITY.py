# SNMP MIB module (CISCO-SWITCH-QOS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-QOS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:14 2024
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

ciscoSwitchQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 541)
)
ciscoSwitchQosCapability.setRevisions(
        ("2014-10-03 00:00",
         "2014-04-03 00:00",
         "2013-10-16 00:00",
         "2011-09-26 00:00",
         "2010-11-17 00:00",
         "2010-03-19 00:00",
         "2008-06-04 00:00",
         "2007-06-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSwitchQosCapV12R0233SXHPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 1)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXHPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXHPCat6k.setStatus(
        "current"
    )

ciscoSwitchQosCapV12R0233SXIPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 2)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXIPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXIPCat6k.setStatus(
        "current"
    )

ciscoSwitchQosCapV12R0233SXI4PCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 3)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXI4PCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0233SXI4PCat6k.setStatus(
        "current"
    )

ciscoSwitchQosCapV12R0250SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 4)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0250SYPCat6k.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV12R0250SYPCat6k.setStatus(
        "current"
    )

ciscoSwitchQosCapV15R0001SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 5)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV15R0001SYPCat6k.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV15R0001SYPCat6k.setStatus(
        "current"
    )

ciscoSwitchQosCapV5R0003U0501gPN3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 6)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV5R0003U0501gPN3K.setProductRelease("""\
Cisco NX-OS 5.0(3)U5(1g) on Nexus 3000
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV5R0003U0501gPN3K.setStatus(
        "current"
    )

ciscoSwitchQosCapV6R0002U0101PN3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 7)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV6R0002U0101PN3K.setProductRelease("""\
Cisco NX-OS 6.0(2)U1(1) on Nexus 3000
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV6R0002U0101PN3K.setStatus(
        "current"
    )

ciscoSwitchQosCapV06R0002U0201PN3K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 8)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV06R0002U0201PN3K.setProductRelease("""\
Cisco NX-OS 6.0(2)U2(1) on Nexus 3000
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapV06R0002U0201PN3K.setStatus(
        "current"
    )

ciscoSwitchQosCapNxOSV06R0210PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 541, 9)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosCapNxOSV06R0210PN7K.setProductRelease("""\
Cisco NX-OS 6.2(10) on Nexus 7000
                     series devices.""")
if mibBuilder.loadTexts:
    ciscoSwitchQosCapNxOSV06R0210PN7K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-QOS-CAPABILITY",
    **{"ciscoSwitchQosCapability": ciscoSwitchQosCapability,
       "ciscoSwitchQosCapV12R0233SXHPCat6k": ciscoSwitchQosCapV12R0233SXHPCat6k,
       "ciscoSwitchQosCapV12R0233SXIPCat6k": ciscoSwitchQosCapV12R0233SXIPCat6k,
       "ciscoSwitchQosCapV12R0233SXI4PCat6k": ciscoSwitchQosCapV12R0233SXI4PCat6k,
       "ciscoSwitchQosCapV12R0250SYPCat6k": ciscoSwitchQosCapV12R0250SYPCat6k,
       "ciscoSwitchQosCapV15R0001SYPCat6k": ciscoSwitchQosCapV15R0001SYPCat6k,
       "ciscoSwitchQosCapV5R0003U0501gPN3K": ciscoSwitchQosCapV5R0003U0501gPN3K,
       "ciscoSwitchQosCapV6R0002U0101PN3K": ciscoSwitchQosCapV6R0002U0101PN3K,
       "ciscoSwitchQosCapV06R0002U0201PN3K": ciscoSwitchQosCapV06R0002U0201PN3K,
       "ciscoSwitchQosCapNxOSV06R0210PN7K": ciscoSwitchQosCapNxOSV06R0210PN7K}
)
