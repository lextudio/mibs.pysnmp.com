# SNMP MIB module (CISCO-XGCP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-XGCP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:48 2024
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

(CCallControlProfileIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlProfileIndexOrZero")

(CMgcGroupIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-MGC-MIB",
    "CMgcGroupIndexOrZero")

(ciscoAgentCapability,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoAgentCapability")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(CXgcpRetryMethod,) = mibBuilder.importSymbols(
    "CISCO-XGCP-MIB",
    "CXgcpRetryMethod")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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

ciscoXgcpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 408)
)
ciscoXgcpCapability.setRevisions(
        ("2006-03-01 00:00",
         "2006-02-14 00:00",
         "2005-06-24 00:00",
         "2005-01-06 00:00",
         "2004-10-04 00:00",
         "2004-06-16 00:00",
         "2002-12-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoXgcpCapabilityV4R010 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 1)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV4R010.setProductRelease("MGX8850 Release 4.0")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV4R010.setStatus(
        "current"
    )

ciscoXgcpCapabilityV12R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 2)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R03.setProductRelease("Cisco IOS 12.3")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R03.setStatus(
        "deprecated"
    )

ciscoXgcpCapabilityV5R015 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 3)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R015.setProductRelease("MGX8850 release 5.0.15")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R015.setStatus(
        "current"
    )

ciscoXgcpCapabilityV5R100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 4)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R100.setProductRelease("MGX8880 release 5.1.00")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R100.setStatus(
        "current"
    )

ciscoXgcpCapabilityV5R300 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 5)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R300.setProductRelease("MGX8880 release 5.3.00")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV5R300.setStatus(
        "current"
    )

ciscoXgcpCapabilityV12R03AS5000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 6)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R03AS5000.setProductRelease("Cisco IOS 12.3")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R03AS5000.setStatus(
        "deprecated"
    )

ciscoXgcpCapabilityV12R04AS5000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 408, 7)
)
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R04AS5000.setProductRelease("Cisco IOS 12.4")
if mibBuilder.loadTexts:
    ciscoXgcpCapabilityV12R04AS5000.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-XGCP-CAPABILITY",
    **{"ciscoXgcpCapability": ciscoXgcpCapability,
       "ciscoXgcpCapabilityV4R010": ciscoXgcpCapabilityV4R010,
       "ciscoXgcpCapabilityV12R03": ciscoXgcpCapabilityV12R03,
       "ciscoXgcpCapabilityV5R015": ciscoXgcpCapabilityV5R015,
       "ciscoXgcpCapabilityV5R100": ciscoXgcpCapabilityV5R100,
       "ciscoXgcpCapabilityV5R300": ciscoXgcpCapabilityV5R300,
       "ciscoXgcpCapabilityV12R03AS5000": ciscoXgcpCapabilityV12R03AS5000,
       "ciscoXgcpCapabilityV12R04AS5000": ciscoXgcpCapabilityV12R04AS5000}
)
