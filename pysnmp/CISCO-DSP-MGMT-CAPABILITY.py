# SNMP MIB module (CISCO-DSP-MGMT-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DSP-MGMT-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:09 2024
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

ciscoDspMgmtCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 121)
)
ciscoDspMgmtCapability.setRevisions(
        ("2011-04-18 00:00",
         "2006-08-09 00:00",
         "2005-10-16 00:00",
         "2005-06-29 00:00",
         "2005-04-21 00:00",
         "2004-08-07 00:00",
         "2003-09-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoDspMgmtCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 1)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R00.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV5R015 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 2)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R015.setProductRelease("MGX8850 Release 5.0.15")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R015.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV5R100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 3)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R100.setProductRelease("MGX8880 Release 5.1.00")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R100.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV12R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 4)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV12R03.setProductRelease("Cisco IOS 12.3")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV12R03.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV5R300 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 5)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R300.setProductRelease("MGX8880 Release 5.3.00")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R300.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV5R400 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 6)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R400.setProductRelease("MGX8880 Release 5.4.00")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV5R400.setStatus(
        "current"
    )

ciscoDspMgmtCapabilityV15R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 121, 7)
)
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV15R02.setProductRelease("""\
OS=IOS
                     OSVERSION=15.2(1)T
                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E
                     INTERFACE=None""")
if mibBuilder.loadTexts:
    ciscoDspMgmtCapabilityV15R02.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DSP-MGMT-CAPABILITY",
    **{"ciscoDspMgmtCapability": ciscoDspMgmtCapability,
       "ciscoDspMgmtCapabilityV5R00": ciscoDspMgmtCapabilityV5R00,
       "ciscoDspMgmtCapabilityV5R015": ciscoDspMgmtCapabilityV5R015,
       "ciscoDspMgmtCapabilityV5R100": ciscoDspMgmtCapabilityV5R100,
       "ciscoDspMgmtCapabilityV12R03": ciscoDspMgmtCapabilityV12R03,
       "ciscoDspMgmtCapabilityV5R300": ciscoDspMgmtCapabilityV5R300,
       "ciscoDspMgmtCapabilityV5R400": ciscoDspMgmtCapabilityV5R400,
       "ciscoDspMgmtCapabilityV15R02": ciscoDspMgmtCapabilityV15R02}
)
