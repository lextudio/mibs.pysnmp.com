# SNMP MIB module (Unisphere-Data-ERX-System-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ERX-System-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:38 2024
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

(usdSystemAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usdSystemAgents")

(usdERXSysFabricGroup,
 usdERXSysGeneralGroup,
 usdERXSysGeneralGroup2,
 usdERXSysGroup,
 usdERXSysNotifyGroup,
 usdERXSysNotifyGroup2,
 usdERXSysNotifyGroup3,
 usdERXSysNvsGroup,
 usdERXSysPortGroup,
 usdERXSysPowerGroup,
 usdERXSysSlotGroup,
 usdERXSysSubsystemGroup,
 usdERXSysTemperatureGroup,
 usdERXSysTemperatureGroup2,
 usdERXSysTimingGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-ERX-System-MIB",
    "usdERXSysFabricGroup",
    "usdERXSysGeneralGroup",
    "usdERXSysGeneralGroup2",
    "usdERXSysGroup",
    "usdERXSysNotifyGroup",
    "usdERXSysNotifyGroup2",
    "usdERXSysNotifyGroup3",
    "usdERXSysNvsGroup",
    "usdERXSysPortGroup",
    "usdERXSysPowerGroup",
    "usdERXSysSlotGroup",
    "usdERXSysSubsystemGroup",
    "usdERXSysTemperatureGroup",
    "usdERXSysTemperatureGroup2",
    "usdERXSysTimingGroup")


# MODULE-IDENTITY

usdErxSystemAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1)
)
usdErxSystemAgent.setRevisions(
        ("2002-04-01 22:32",
         "2001-04-13 13:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdErxSystemAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1)
)
if mibBuilder.loadTexts:
    usdErxSystemAgentV1.setProductRelease("""\
Version 1 of the ERX System component of the Unisphere Edge Routing
        Switch SNMP agent.  This version of the ERX System component was
        supported in the Unisphere RX 1.3 system release.""")
if mibBuilder.loadTexts:
    usdErxSystemAgentV1.setStatus(
        "obsolete"
    )

usdErxSystemAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2)
)
if mibBuilder.loadTexts:
    usdErxSystemAgentV2.setProductRelease("""\
Version 2 of the ERX System component of the Unisphere Edge Routing
        Switch SNMP agent.  This version of the ERX System component was
        supported in the Unisphere RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdErxSystemAgentV2.setStatus(
        "obsolete"
    )

usdErxSystemAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3)
)
if mibBuilder.loadTexts:
    usdErxSystemAgentV3.setProductRelease("""\
Version 3 of the ERX System component of the Unisphere Edge Routing
        Switch SNMP agent.  This version of the ERX System component was
        supported in the Unisphere RX 3.0 system release.""")
if mibBuilder.loadTexts:
    usdErxSystemAgentV3.setStatus(
        "obsolete"
    )

usdErxSystemAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4)
)
if mibBuilder.loadTexts:
    usdErxSystemAgentV4.setProductRelease("""\
Version 4 of the ERX System component of the Unisphere Edge Routing
        Switch SNMP agent.  This version of the ERX System component was
        supported in the Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdErxSystemAgentV4.setStatus(
        "obsolete"
    )

usdErxSystemAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5)
)
if mibBuilder.loadTexts:
    usdErxSystemAgentV5.setProductRelease("""\
Version 5 of the ERX System component of the Unisphere Edge Routing
        Switch SNMP agent.  This version of the ERX System component is
        supported in the Unisphere RX 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdErxSystemAgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ERX-System-CONF",
    **{"usdErxSystemAgent": usdErxSystemAgent,
       "usdErxSystemAgentV1": usdErxSystemAgentV1,
       "usdErxSystemAgentV2": usdErxSystemAgentV2,
       "usdErxSystemAgentV3": usdErxSystemAgentV3,
       "usdErxSystemAgentV4": usdErxSystemAgentV4,
       "usdErxSystemAgentV5": usdErxSystemAgentV5}
)
