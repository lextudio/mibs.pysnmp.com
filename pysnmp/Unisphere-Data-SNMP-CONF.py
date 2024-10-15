# SNMP MIB module (Unisphere-Data-SNMP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SNMP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:37 2024
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

(snmpEngineGroup,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "snmpEngineGroup")

(snmpMPDGroup,) = mibBuilder.importSymbols(
    "SNMP-MPD-MIB",
    "snmpMPDGroup")

(snmpNotifyFilterGroup,
 snmpNotifyFilterMask,
 snmpNotifyFilterProfileName,
 snmpNotifyFilterProfileRowStatus,
 snmpNotifyFilterProfileStorType,
 snmpNotifyFilterRowStatus,
 snmpNotifyFilterStorageType,
 snmpNotifyFilterType,
 snmpNotifyGroup,
 snmpNotifyRowStatus,
 snmpNotifyStorageType,
 snmpNotifyTag,
 snmpNotifyType) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyFilterGroup",
    "snmpNotifyFilterMask",
    "snmpNotifyFilterProfileName",
    "snmpNotifyFilterProfileRowStatus",
    "snmpNotifyFilterProfileStorType",
    "snmpNotifyFilterRowStatus",
    "snmpNotifyFilterStorageType",
    "snmpNotifyFilterType",
    "snmpNotifyGroup",
    "snmpNotifyRowStatus",
    "snmpNotifyStorageType",
    "snmpNotifyTag",
    "snmpNotifyType")

(snmpTargetAddrParams,
 snmpTargetAddrRetryCount,
 snmpTargetAddrRowStatus,
 snmpTargetAddrStorageType,
 snmpTargetAddrTAddress,
 snmpTargetAddrTDomain,
 snmpTargetAddrTagList,
 snmpTargetAddrTimeout,
 snmpTargetBasicGroup,
 snmpTargetCommandResponderGroup,
 snmpTargetParamsMPModel,
 snmpTargetParamsRowStatus,
 snmpTargetParamsSecurityLevel,
 snmpTargetParamsSecurityModel,
 snmpTargetParamsSecurityName,
 snmpTargetParamsStorageType,
 snmpTargetResponseGroup) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrParams",
    "snmpTargetAddrRetryCount",
    "snmpTargetAddrRowStatus",
    "snmpTargetAddrStorageType",
    "snmpTargetAddrTAddress",
    "snmpTargetAddrTDomain",
    "snmpTargetAddrTagList",
    "snmpTargetAddrTimeout",
    "snmpTargetBasicGroup",
    "snmpTargetCommandResponderGroup",
    "snmpTargetParamsMPModel",
    "snmpTargetParamsRowStatus",
    "snmpTargetParamsSecurityLevel",
    "snmpTargetParamsSecurityModel",
    "snmpTargetParamsSecurityName",
    "snmpTargetParamsStorageType",
    "snmpTargetResponseGroup")

(usmMIBBasicGroup,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmMIBBasicGroup")

(vacmBasicGroup,) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmBasicGroup")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
    "ModuleCompliance",
    "NotificationGroup")

(snmpBasicNotificationsGroup,
 snmpCommunityGroup,
 snmpGroup,
 snmpObsoleteGroup,
 snmpSetGroup,
 sysORDescr,
 sysORID,
 sysORLastChange,
 sysORUpTime,
 systemGroup) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpBasicNotificationsGroup",
    "snmpCommunityGroup",
    "snmpGroup",
    "snmpObsoleteGroup",
    "snmpSetGroup",
    "sysORDescr",
    "sysORID",
    "sysORLastChange",
    "sysORUpTime",
    "systemGroup")

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

(usdSnmpAccessGroup,
 usdSnmpAuthFailGroup,
 usdSnmpGeneralGroup,
 usdSnmpGeneralGroup2,
 usdSnmpGroup,
 usdSnmpGroup2,
 usdSnmpGroup3,
 usdSnmpTrapGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-SNMP-MIB",
    "usdSnmpAccessGroup",
    "usdSnmpAuthFailGroup",
    "usdSnmpGeneralGroup",
    "usdSnmpGeneralGroup2",
    "usdSnmpGroup",
    "usdSnmpGroup2",
    "usdSnmpGroup3",
    "usdSnmpTrapGroup")


# MODULE-IDENTITY

usdSnmpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39)
)
usdSnmpAgent.setRevisions(
        ("2002-08-14 19:23",
         "2001-10-16 13:44",
         "2001-04-13 15:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdSnmpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV1.setProductRelease("""\
Version 1 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component was supported in
        the Unisphere RX 1.x system releases.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV1.setStatus(
        "obsolete"
    )

usdSnmpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV2.setProductRelease("""\
Version 2 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component was supported in
        the Unisphere RX 2.0 thru 2.2 system releases.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV2.setStatus(
        "obsolete"
    )

usdSnmpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV3.setProductRelease("""\
Version 3 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component was supported in
        the Unisphere RX 2.3 thru 3.1 system releases.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV3.setStatus(
        "obsolete"
    )

usdSnmpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV4.setProductRelease("""\
Version 4 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component was supported in
        the Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV4.setStatus(
        "obsolete"
    )

usdSnmpAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV5.setProductRelease("""\
Version 5 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component was supported in
        the Unisphere RX 3.3 system releases.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV5.setStatus(
        "obsolete"
    )

usdSnmpAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6)
)
if mibBuilder.loadTexts:
    usdSnmpAgentV6.setProductRelease("""\
Version 6 of the SNMP entity component of the Unisphere Routing Switch
        SNMP agent.  This version of the SNMP entity component is supported in
        the Unisphere RX 3.4 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdSnmpAgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SNMP-CONF",
    **{"usdSnmpAgent": usdSnmpAgent,
       "usdSnmpAgentV1": usdSnmpAgentV1,
       "usdSnmpAgentV2": usdSnmpAgentV2,
       "usdSnmpAgentV3": usdSnmpAgentV3,
       "usdSnmpAgentV4": usdSnmpAgentV4,
       "usdSnmpAgentV5": usdSnmpAgentV5,
       "usdSnmpAgentV6": usdSnmpAgentV6}
)
