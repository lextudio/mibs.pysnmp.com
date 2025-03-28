# SNMP MIB module (CISCO-NOTIFICATION-LOG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NOTIFICATION-LOG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:15 2024
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

ciscoNotificationLogCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 463)
)
ciscoNotificationLogCapability.setRevisions(
        ("2008-12-18 00:00",
         "2007-01-22 00:00",
         "2005-11-29 00:00",
         "2005-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cNotificationLogCapabilityV12R04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 463, 1)
)
if mibBuilder.loadTexts:
    cNotificationLogCapabilityV12R04.setProductRelease("Cisco IOS 12.4")
if mibBuilder.loadTexts:
    cNotificationLogCapabilityV12R04.setStatus(
        "current"
    )

cNotificationLogCapabilityV12R2S = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 463, 2)
)
if mibBuilder.loadTexts:
    cNotificationLogCapabilityV12R2S.setProductRelease("Cisco IOS 12.2S and 12.2S based releases")
if mibBuilder.loadTexts:
    cNotificationLogCapabilityV12R2S.setStatus(
        "current"
    )

cNotificationLogCapIOSXRV3R4CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 463, 3)
)
if mibBuilder.loadTexts:
    cNotificationLogCapIOSXRV3R4CRS1.setProductRelease("Cisco IOS XR 3.4 for CRS-1")
if mibBuilder.loadTexts:
    cNotificationLogCapIOSXRV3R4CRS1.setStatus(
        "current"
    )

cNotificationLogCapNXOSV04R0103 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 463, 4)
)
if mibBuilder.loadTexts:
    cNotificationLogCapNXOSV04R0103.setProductRelease("Cisco NX-OS 4.1(3) on MDS9000 and Nexus7000 Storage Switches")
if mibBuilder.loadTexts:
    cNotificationLogCapNXOSV04R0103.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NOTIFICATION-LOG-CAPABILITY",
    **{"ciscoNotificationLogCapability": ciscoNotificationLogCapability,
       "cNotificationLogCapabilityV12R04": cNotificationLogCapabilityV12R04,
       "cNotificationLogCapabilityV12R2S": cNotificationLogCapabilityV12R2S,
       "cNotificationLogCapIOSXRV3R4CRS1": cNotificationLogCapIOSXRV3R4CRS1,
       "cNotificationLogCapNXOSV04R0103": cNotificationLogCapNXOSV04R0103}
)
