# SNMP MIB module (Unisphere-Data-DS3-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DS3-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:34 2024
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

(dsx3ConfigEntry,
 dsx3CurrentEntry,
 dsx3FarEndConfigEntry,
 dsx3FarEndCurrentEntry,
 dsx3FarEndIntervalEntry,
 dsx3FarEndTotalEntry,
 dsx3FracEntry,
 dsx3IntervalEntry,
 dsx3SendCode,
 dsx3TotalEntry) = mibBuilder.importSymbols(
    "RFC1407-MIB",
    "dsx3ConfigEntry",
    "dsx3CurrentEntry",
    "dsx3FarEndConfigEntry",
    "dsx3FarEndCurrentEntry",
    "dsx3FarEndIntervalEntry",
    "dsx3FarEndTotalEntry",
    "dsx3FracEntry",
    "dsx3IntervalEntry",
    "dsx3SendCode",
    "dsx3TotalEntry")

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

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdDs3FarEndGroup,
 usdDs3Group,
 usdDs3Group2,
 usdDs3Group3,
 usdDs3Group4,
 usdDs3Group5) = mibBuilder.importSymbols(
    "Unisphere-Data-DS3-MIB",
    "usdDs3FarEndGroup",
    "usdDs3Group",
    "usdDs3Group2",
    "usdDs3Group3",
    "usdDs3Group4",
    "usdDs3Group5")


# MODULE-IDENTITY

usdDs3Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11)
)
usdDs3Agent.setRevisions(
        ("2002-08-27 18:48",
         "2001-04-18 19:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdDs3AgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1)
)
if mibBuilder.loadTexts:
    usdDs3AgentV1.setProductRelease("""\
Version 1 of the DS3 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS3 component was supported in the Unisphere
        RX 1.0 system release.""")
if mibBuilder.loadTexts:
    usdDs3AgentV1.setStatus(
        "obsolete"
    )

usdDs3AgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2)
)
if mibBuilder.loadTexts:
    usdDs3AgentV2.setProductRelease("""\
Version 2 of the DS3 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS3 component was supported in the Unisphere
        RX 1.1 thru RX 2.5 system releases.""")
if mibBuilder.loadTexts:
    usdDs3AgentV2.setStatus(
        "obsolete"
    )

usdDs3AgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3)
)
if mibBuilder.loadTexts:
    usdDs3AgentV3.setProductRelease("""\
Version 3 of the DS3 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS3 component was supported in the Unisphere
        RX 2.6 thru RX 2.9 system releases.""")
if mibBuilder.loadTexts:
    usdDs3AgentV3.setStatus(
        "obsolete"
    )

usdDs3AgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4)
)
if mibBuilder.loadTexts:
    usdDs3AgentV4.setProductRelease("""\
Version 4 of the DS3 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS3 component was supported in the Unisphere
        RX 3.x system releases.""")
if mibBuilder.loadTexts:
    usdDs3AgentV4.setStatus(
        "obsolete"
    )

usdDs3AgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5)
)
if mibBuilder.loadTexts:
    usdDs3AgentV5.setProductRelease("""\
Version 5 of the DS3 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS3 component is supported in the Unisphere
        RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdDs3AgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DS3-CONF",
    **{"usdDs3Agent": usdDs3Agent,
       "usdDs3AgentV1": usdDs3AgentV1,
       "usdDs3AgentV2": usdDs3AgentV2,
       "usdDs3AgentV3": usdDs3AgentV3,
       "usdDs3AgentV4": usdDs3AgentV4,
       "usdDs3AgentV5": usdDs3AgentV5}
)
