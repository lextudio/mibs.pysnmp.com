# SNMP MIB module (CISCO-HC-ALARM-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HC-ALARM-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:11 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoHcAlarmCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 398)
)
ciscoHcAlarmCapability.setRevisions(
        ("2008-08-05 00:00",
         "2004-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoHcAlarmCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 398, 1)
)
if mibBuilder.loadTexts:
    ciscoHcAlarmCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    ciscoHcAlarmCapCatOSV08R0401.setStatus(
        "current"
    )

ciscoHcAlarmCapNXOSV04R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 398, 2)
)
if mibBuilder.loadTexts:
    ciscoHcAlarmCapNXOSV04R0101.setProductRelease("Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.")
if mibBuilder.loadTexts:
    ciscoHcAlarmCapNXOSV04R0101.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HC-ALARM-CAPABILITY",
    **{"ciscoHcAlarmCapability": ciscoHcAlarmCapability,
       "ciscoHcAlarmCapCatOSV08R0401": ciscoHcAlarmCapCatOSV08R0401,
       "ciscoHcAlarmCapNXOSV04R0101": ciscoHcAlarmCapNXOSV04R0101}
)
