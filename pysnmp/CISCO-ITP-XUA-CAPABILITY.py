# SNMP MIB module (CISCO-ITP-XUA-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-XUA-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:38 2024
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

ciscoItpXuaCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 268)
)
ciscoItpXuaCapability.setRevisions(
        ("2008-06-25 00:00",
         "2007-09-26 00:00",
         "2006-10-05 00:00",
         "2004-11-03 00:00",
         "2003-10-15 00:00",
         "2003-08-15 00:00",
         "2002-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoItpXuaCapabilityV12R0204MB5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 1)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0204MB5.setProductRelease("Cisco IOS 12.2(4)MB5")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0204MB5.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0219SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 2)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0219SW.setProductRelease("Cisco IOS 12.2(19)SW")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0219SW.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0223SW01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 3)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0223SW01.setProductRelease("Cisco IOS 12.2(23)SW01")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0223SW01.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0225SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 4)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0225SW.setProductRelease("Cisco IOS 12.2(25)SW")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0225SW.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0218IXA = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 5)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0218IXA.setProductRelease("Cisco IOS 12.2(18)IXA")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0218IXA.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0411SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 6)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0411SW.setProductRelease("Cisco IOS 12.4(11)SW")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0411SW.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0415SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 7)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0415SW.setProductRelease("Cisco IOS 12.4(15)SW")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0415SW.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0218IXE = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 8)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0218IXE.setProductRelease("Cisco IOS 12.2(18)IXE")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0218IXE.setStatus(
        "current"
    )

ciscoItpXuaCapabilityV12R0233IRA = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 268, 9)
)
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0233IRA.setProductRelease("Cisco IOS 12.2(33)IRA")
if mibBuilder.loadTexts:
    ciscoItpXuaCapabilityV12R0233IRA.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-XUA-CAPABILITY",
    **{"ciscoItpXuaCapability": ciscoItpXuaCapability,
       "ciscoItpXuaCapabilityV12R0204MB5": ciscoItpXuaCapabilityV12R0204MB5,
       "ciscoItpXuaCapabilityV12R0219SW": ciscoItpXuaCapabilityV12R0219SW,
       "ciscoItpXuaCapabilityV12R0223SW01": ciscoItpXuaCapabilityV12R0223SW01,
       "ciscoItpXuaCapabilityV12R0225SW": ciscoItpXuaCapabilityV12R0225SW,
       "ciscoItpXuaCapabilityV12R0218IXA": ciscoItpXuaCapabilityV12R0218IXA,
       "ciscoItpXuaCapabilityV12R0411SW": ciscoItpXuaCapabilityV12R0411SW,
       "ciscoItpXuaCapabilityV12R0415SW": ciscoItpXuaCapabilityV12R0415SW,
       "ciscoItpXuaCapabilityV12R0218IXE": ciscoItpXuaCapabilityV12R0218IXE,
       "ciscoItpXuaCapabilityV12R0233IRA": ciscoItpXuaCapabilityV12R0233IRA}
)
