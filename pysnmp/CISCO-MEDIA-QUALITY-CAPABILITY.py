# SNMP MIB module (CISCO-MEDIA-QUALITY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEDIA-QUALITY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:20 2024
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

ciscoMediaQualityCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 604)
)
ciscoMediaQualityCapability.setRevisions(
        ("2011-09-23 00:00",
         "2011-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoMediaQualityCapabilityV152R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 604, 1)
)
if mibBuilder.loadTexts:
    ciscoMediaQualityCapabilityV152R01.setProductRelease("""\
OS=IOS
                     OSVERSION=15.2(1)T
                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E
                     INTERFACE=None""")
if mibBuilder.loadTexts:
    ciscoMediaQualityCapabilityV152R01.setStatus(
        "current"
    )

ciscoMediaQualityCapabilityV152R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 604, 2)
)
if mibBuilder.loadTexts:
    ciscoMediaQualityCapabilityV152R02.setProductRelease("""\
OS=IOS
                     OSVERSION=15.2(2)T
                     PLATFORM=c28xx,c3825,c3845,c29xx,c3925,c3945,c3925E,c3945E
                     INTERFACE=None""")
if mibBuilder.loadTexts:
    ciscoMediaQualityCapabilityV152R02.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEDIA-QUALITY-CAPABILITY",
    **{"ciscoMediaQualityCapability": ciscoMediaQualityCapability,
       "ciscoMediaQualityCapabilityV152R01": ciscoMediaQualityCapabilityV152R01,
       "ciscoMediaQualityCapabilityV152R02": ciscoMediaQualityCapabilityV152R02}
)
