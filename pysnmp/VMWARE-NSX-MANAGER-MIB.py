# SNMP MIB module (VMWARE-NSX-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-NSX-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:52 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(UUID,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUID")

(vmwNsxManager,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNsxManager")


# MODULE-IDENTITY

vmwNsxManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1)
)
vmwNsxManagerMIB.setRevisions(
        ("2016-06-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VmwNsxManagerTypeSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("high", 6),
          ("informational", 1),
          ("low", 2),
          ("major", 4),
          ("medium", 3))
    )



# MIB Managed Objects in the order of their OIDs

_VmwNsxMAlertData_ObjectIdentity = ObjectIdentity
vmwNsxMAlertData = _VmwNsxMAlertData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMAlertData.setStatus("current")


class _VmwNsxMEventCode_Type(Integer32):
    """Custom type vmwNsxMEventCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmwNsxMEventCode_Type.__name__ = "Integer32"
_VmwNsxMEventCode_Object = MibScalar
vmwNsxMEventCode = _VmwNsxMEventCode_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 1),
    _VmwNsxMEventCode_Type()
)
vmwNsxMEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventCode.setStatus("current")
_VmwNsxMEventTimestamp_Type = DateAndTime
_VmwNsxMEventTimestamp_Object = MibScalar
vmwNsxMEventTimestamp = _VmwNsxMEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 2),
    _VmwNsxMEventTimestamp_Type()
)
vmwNsxMEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventTimestamp.setStatus("current")
_VmwNsxMEventMessage_Type = OctetString
_VmwNsxMEventMessage_Object = MibScalar
vmwNsxMEventMessage = _VmwNsxMEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 3),
    _VmwNsxMEventMessage_Type()
)
vmwNsxMEventMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventMessage.setStatus("current")
_VmwNsxMEventSeverity_Type = VmwNsxManagerTypeSeverity
_VmwNsxMEventSeverity_Object = MibScalar
vmwNsxMEventSeverity = _VmwNsxMEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 4),
    _VmwNsxMEventSeverity_Type()
)
vmwNsxMEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventSeverity.setStatus("current")
_VmwNsxMEventComponent_Type = OctetString
_VmwNsxMEventComponent_Object = MibScalar
vmwNsxMEventComponent = _VmwNsxMEventComponent_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 5),
    _VmwNsxMEventComponent_Type()
)
vmwNsxMEventComponent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMEventComponent.setStatus("current")
_VmwNsxMUuid_Type = UUID
_VmwNsxMUuid_Object = MibScalar
vmwNsxMUuid = _VmwNsxMUuid_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 6),
    _VmwNsxMUuid_Type()
)
vmwNsxMUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMUuid.setStatus("current")


class _VmwNsxMCount_Type(Integer32):
    """Custom type vmwNsxMCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmwNsxMCount_Type.__name__ = "Integer32"
_VmwNsxMCount_Object = MibScalar
vmwNsxMCount = _VmwNsxMCount_Object(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 1, 7),
    _VmwNsxMCount_Type()
)
vmwNsxMCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwNsxMCount.setStatus("current")
_VmwNsxMNotification_ObjectIdentity = ObjectIdentity
vmwNsxMNotification = _VmwNsxMNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2)
)
if mibBuilder.loadTexts:
    vmwNsxMNotification.setStatus("current")
_VmwNsxMBranch_ObjectIdentity = ObjectIdentity
vmwNsxMBranch = _VmwNsxMBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMBranch.setStatus("current")
_VmwNsxMGroupsBranch_ObjectIdentity = ObjectIdentity
vmwNsxMGroupsBranch = _VmwNsxMGroupsBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMGroupsBranch.setStatus("current")
_VmwNsxMGroupsPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMGroupsPrefix = _VmwNsxMGroupsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMGroupsPrefix.setStatus("current")
_VmwNsxMSnmp_ObjectIdentity = ObjectIdentity
vmwNsxMSnmp = _VmwNsxMSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vmwNsxMSnmp.setStatus("current")
_VmwNsxMSnmpPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSnmpPrefix = _VmwNsxMSnmpPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpPrefix.setStatus("current")
_VmwNsxMSecurity_ObjectIdentity = ObjectIdentity
vmwNsxMSecurity = _VmwNsxMSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vmwNsxMSecurity.setStatus("current")
_VmwNsxMSecurityPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSecurityPrefix = _VmwNsxMSecurityPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSecurityPrefix.setStatus("current")
_VmwNsxMFirewall_ObjectIdentity = ObjectIdentity
vmwNsxMFirewall = _VmwNsxMFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vmwNsxMFirewall.setStatus("current")
_VmwNsxMFirewallPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMFirewallPrefix = _VmwNsxMFirewallPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallPrefix.setStatus("current")
_VmwNsxMEdge_ObjectIdentity = ObjectIdentity
vmwNsxMEdge = _VmwNsxMEdge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4)
)
if mibBuilder.loadTexts:
    vmwNsxMEdge.setStatus("current")
_VmwNsxMEdgePrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEdgePrefix = _VmwNsxMEdgePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEdgePrefix.setStatus("current")
_VmwNsxMEndpoint_ObjectIdentity = ObjectIdentity
vmwNsxMEndpoint = _VmwNsxMEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5)
)
if mibBuilder.loadTexts:
    vmwNsxMEndpoint.setStatus("current")
_VmwNsxMEndpointPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEndpointPrefix = _VmwNsxMEndpointPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointPrefix.setStatus("current")
_VmwNsxMEam_ObjectIdentity = ObjectIdentity
vmwNsxMEam = _VmwNsxMEam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6)
)
if mibBuilder.loadTexts:
    vmwNsxMEam.setStatus("current")
_VmwNsxMEamPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMEamPrefix = _VmwNsxMEamPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMEamPrefix.setStatus("current")
_VmwNsxMFabric_ObjectIdentity = ObjectIdentity
vmwNsxMFabric = _VmwNsxMFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7)
)
if mibBuilder.loadTexts:
    vmwNsxMFabric.setStatus("current")
_VmwNsxMFabricPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMFabricPrefix = _VmwNsxMFabricPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMFabricPrefix.setStatus("current")
_VmwNsxMDepPlugin_ObjectIdentity = ObjectIdentity
vmwNsxMDepPlugin = _VmwNsxMDepPlugin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8)
)
if mibBuilder.loadTexts:
    vmwNsxMDepPlugin.setStatus("current")
_VmwNsxMDepPluginPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMDepPluginPrefix = _VmwNsxMDepPluginPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginPrefix.setStatus("current")
_VmwNsxMMessaging_ObjectIdentity = ObjectIdentity
vmwNsxMMessaging = _VmwNsxMMessaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9)
)
if mibBuilder.loadTexts:
    vmwNsxMMessaging.setStatus("current")
_VmwNsxMMessagingPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMMessagingPrefix = _VmwNsxMMessagingPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingPrefix.setStatus("current")
_VmwNsxMServiceComposer_ObjectIdentity = ObjectIdentity
vmwNsxMServiceComposer = _VmwNsxMServiceComposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10)
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposer.setStatus("current")
_VmwNsxMServiceComposerPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMServiceComposerPrefix = _VmwNsxMServiceComposerPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPrefix.setStatus("current")
_VmwNsxMSvmOperations_ObjectIdentity = ObjectIdentity
vmwNsxMSvmOperations = _VmwNsxMSvmOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11)
)
if mibBuilder.loadTexts:
    vmwNsxMSvmOperations.setStatus("current")
_VmwNsxMSvmOperationsPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSvmOperationsPrefix = _VmwNsxMSvmOperationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSvmOperationsPrefix.setStatus("current")
_VmwNsxMTranslation_ObjectIdentity = ObjectIdentity
vmwNsxMTranslation = _VmwNsxMTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12)
)
if mibBuilder.loadTexts:
    vmwNsxMTranslation.setStatus("current")
_VmwNsxMTranslationPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMTranslationPrefix = _VmwNsxMTranslationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMTranslationPrefix.setStatus("current")
_VmwNsxMUniversalSync_ObjectIdentity = ObjectIdentity
vmwNsxMUniversalSync = _VmwNsxMUniversalSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13)
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSync.setStatus("current")
_VmwNsxMUniversalSyncPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMUniversalSyncPrefix = _VmwNsxMUniversalSyncPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncPrefix.setStatus("current")
_VmwNsxMAsyncRest_ObjectIdentity = ObjectIdentity
vmwNsxMAsyncRest = _VmwNsxMAsyncRest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14)
)
if mibBuilder.loadTexts:
    vmwNsxMAsyncRest.setStatus("current")
_VmwNsxMAsyncRestPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMAsyncRestPrefix = _VmwNsxMAsyncRestPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMAsyncRestPrefix.setStatus("current")
_VmwNsxMExtensionRegistration_ObjectIdentity = ObjectIdentity
vmwNsxMExtensionRegistration = _VmwNsxMExtensionRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15)
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistration.setStatus("current")
_VmwNsxMExtensionRegistrationPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMExtensionRegistrationPrefix = _VmwNsxMExtensionRegistrationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistrationPrefix.setStatus("current")
_VmwNsxMDlp_ObjectIdentity = ObjectIdentity
vmwNsxMDlp = _VmwNsxMDlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16)
)
if mibBuilder.loadTexts:
    vmwNsxMDlp.setStatus("current")
_VmwNsxMDlpPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMDlpPrefix = _VmwNsxMDlpPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMDlpPrefix.setStatus("current")
_VmwNsxMSamSystem_ObjectIdentity = ObjectIdentity
vmwNsxMSamSystem = _VmwNsxMSamSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17)
)
if mibBuilder.loadTexts:
    vmwNsxMSamSystem.setStatus("current")
_VmwNsxMSamSystemPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMSamSystemPrefix = _VmwNsxMSamSystemPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMSamSystemPrefix.setStatus("current")
_VmwNsxMUsvm_ObjectIdentity = ObjectIdentity
vmwNsxMUsvm = _VmwNsxMUsvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18)
)
if mibBuilder.loadTexts:
    vmwNsxMUsvm.setStatus("current")
_VmwNsxMUsvmPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMUsvmPrefix = _VmwNsxMUsvmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmPrefix.setStatus("current")
_VmwNsxMVsmCore_ObjectIdentity = ObjectIdentity
vmwNsxMVsmCore = _VmwNsxMVsmCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19)
)
if mibBuilder.loadTexts:
    vmwNsxMVsmCore.setStatus("current")
_VmwNsxMVsmCorePrefix_ObjectIdentity = ObjectIdentity
vmwNsxMVsmCorePrefix = _VmwNsxMVsmCorePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMVsmCorePrefix.setStatus("current")
_VmwNsxMVxlan_ObjectIdentity = ObjectIdentity
vmwNsxMVxlan = _VmwNsxMVxlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20)
)
if mibBuilder.loadTexts:
    vmwNsxMVxlan.setStatus("current")
_VmwNsxMVxlanPrefix_ObjectIdentity = ObjectIdentity
vmwNsxMVxlanPrefix = _VmwNsxMVxlanPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0)
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanPrefix.setStatus("current")
_VmwNsxManagerMIBConformance_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBConformance = _VmwNsxManagerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99)
)
_VmwNsxManagerMIBCompliances_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBCompliances = _VmwNsxManagerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1)
)
_VmwNsxManagerMIBGroups_ObjectIdentity = ObjectIdentity
vmwNsxManagerMIBGroups = _VmwNsxManagerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2)
)

# Managed Objects groups

vmwNsxManagerNotificationInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 2)
)
vmwNsxManagerNotificationInfoGroup1.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCount"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationInfoGroup1.setStatus("current")


# Notification objects

vmwNsxMConfigGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 0, 1, 0, 1)
)
vmwNsxMConfigGroup.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCount"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMConfigGroup.setStatus(
        "current"
    )

vmwNsxMSnmpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0, 1)
)
vmwNsxMSnmpDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpDisabled.setStatus(
        "current"
    )

vmwNsxMSnmpManagerConfigUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 1, 0, 2)
)
vmwNsxMSnmpManagerConfigUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSnmpManagerConfigUpdated.setStatus(
        "current"
    )

vmwNsxMIpAddedBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 1)
)
vmwNsxMIpAddedBlackList.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpAddedBlackList.setStatus(
        "current"
    )

vmwNsxMIpRemovedBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 2)
)
vmwNsxMIpRemovedBlackList.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpRemovedBlackList.setStatus(
        "current"
    )

vmwNsxMSsoConfigFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 3)
)
vmwNsxMSsoConfigFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoConfigFailure.setStatus(
        "current"
    )

vmwNsxMSsoUnconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 4)
)
vmwNsxMSsoUnconfigured.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoUnconfigured.setStatus(
        "current"
    )

vmwNsxMUserRoleAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 5)
)
vmwNsxMUserRoleAssigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUserRoleAssigned.setStatus(
        "current"
    )

vmwNsxMUserRoleUnassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 6)
)
vmwNsxMUserRoleUnassigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUserRoleUnassigned.setStatus(
        "current"
    )

vmwNsxMGroupRoleAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 7)
)
vmwNsxMGroupRoleAssigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGroupRoleAssigned.setStatus(
        "current"
    )

vmwNsxMGroupRoleUnassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 8)
)
vmwNsxMGroupRoleUnassigned.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGroupRoleUnassigned.setStatus(
        "current"
    )

vmwNsxMVcLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 9)
)
vmwNsxMVcLoginFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVcLoginFailed.setStatus(
        "current"
    )

vmwNsxMVcDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 10)
)
vmwNsxMVcDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVcDisconnected.setStatus(
        "current"
    )

vmwNsxMLostVcConnectivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 11)
)
vmwNsxMLostVcConnectivity.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLostVcConnectivity.setStatus(
        "current"
    )

vmwNsxMSsoDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 2, 0, 12)
)
vmwNsxMSsoDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSsoDisconnected.setStatus(
        "current"
    )

vmwNsxMFltrCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 1)
)
vmwNsxMFltrCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFltrCnfgNotAppliedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 2)
)
vmwNsxMFltrCnfgNotAppliedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgNotAppliedToVnic.setStatus(
        "current"
    )

vmwNsxMFltrCnfgAppliedToVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 3)
)
vmwNsxMFltrCnfgAppliedToVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCnfgAppliedToVnic.setStatus(
        "current"
    )

vmwNsxMFltrCreatedForVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 4)
)
vmwNsxMFltrCreatedForVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrCreatedForVnic.setStatus(
        "current"
    )

vmwNsxMFltrDeletedForVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 5)
)
vmwNsxMFltrDeletedForVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFltrDeletedForVnic.setStatus(
        "current"
    )

vmwNsxMFirewallConfigUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 6)
)
vmwNsxMFirewallConfigUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallConfigUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFirewallRuleFailedVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 7)
)
vmwNsxMFirewallRuleFailedVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleFailedVnic.setStatus(
        "current"
    )

vmwNsxMFirewallRuleAppliedVnic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 8)
)
vmwNsxMFirewallRuleAppliedVnic.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleAppliedVnic.setStatus(
        "current"
    )

vmwNsxMCntnrCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 9)
)
vmwNsxMCntnrCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMFlowMissed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 10)
)
vmwNsxMFlowMissed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFlowMissed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardCnfgUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 11)
)
vmwNsxMSpoofGuardCnfgUpdateFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardCnfgUpdateFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 12)
)
vmwNsxMSpoofGuardFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 13)
)
vmwNsxMSpoofGuardApplied.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardApplied.setStatus(
        "current"
    )

vmwNsxMSpoofGuardDisableFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 14)
)
vmwNsxMSpoofGuardDisableFail.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardDisableFail.setStatus(
        "current"
    )

vmwNsxMSpoofGuardDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 15)
)
vmwNsxMSpoofGuardDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardDisabled.setStatus(
        "current"
    )

vmwNsxMLegacyAppServiceDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 16)
)
vmwNsxMLegacyAppServiceDeletionFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLegacyAppServiceDeletionFailed.setStatus(
        "current"
    )

vmwNsxMFirewallCpuThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 17)
)
vmwNsxMFirewallCpuThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCpuThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallMemThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 18)
)
vmwNsxMFirewallMemThresholdCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallMemThresholdCrossed.setStatus(
        "current"
    )

vmwNsxMConnPerSecThrshldCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 19)
)
vmwNsxMConnPerSecThrshldCrossed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMConnPerSecThrshldCrossed.setStatus(
        "current"
    )

vmwNsxMFirewallCnfgUpdateTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 20)
)
vmwNsxMFirewallCnfgUpdateTimedOut.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCnfgUpdateTimedOut.setStatus(
        "current"
    )

vmwNsxMSpoofGuardCnfgUpdateTmOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 21)
)
vmwNsxMSpoofGuardCnfgUpdateTmOut.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardCnfgUpdateTmOut.setStatus(
        "current"
    )

vmwNsxMFirewallPublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 22)
)
vmwNsxMFirewallPublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallPublishFailed.setStatus(
        "current"
    )

vmwNsxMCntnrUpdatePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 23)
)
vmwNsxMCntnrUpdatePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMCntnrUpdatePublishFailed.setStatus(
        "current"
    )

vmwNsxMSpoofGuardUpdatePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 24)
)
vmwNsxMSpoofGuardUpdatePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSpoofGuardUpdatePublishFailed.setStatus(
        "current"
    )

vmwNsxMExcludeListPublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 25)
)
vmwNsxMExcludeListPublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMExcludeListPublishFailed.setStatus(
        "current"
    )

vmwNsxMFirewallCnfgUpdateOnDltCntnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 26)
)
vmwNsxMFirewallCnfgUpdateOnDltCntnr.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallCnfgUpdateOnDltCntnr.setStatus(
        "current"
    )

vmwNsxMHostSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 27)
)
vmwNsxMHostSyncFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMHostSyncFailed.setStatus(
        "current"
    )

vmwNsxMHostSynced = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 28)
)
vmwNsxMHostSynced.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMHostSynced.setStatus(
        "current"
    )

vmwNsxMFirewallInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 29)
)
vmwNsxMFirewallInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallInstalled.setStatus(
        "current"
    )

vmwNsxMFirewallInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 30)
)
vmwNsxMFirewallInstallFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallInstallFailed.setStatus(
        "current"
    )

vmwNsxMFirewallClusterInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 31)
)
vmwNsxMFirewallClusterInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterInstalled.setStatus(
        "current"
    )

vmwNsxMFirewallClusterUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 32)
)
vmwNsxMFirewallClusterUninstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterUninstalled.setStatus(
        "current"
    )

vmwNsxMFirewallClusterDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 33)
)
vmwNsxMFirewallClusterDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallClusterDisabled.setStatus(
        "current"
    )

vmwNsxMFirewallForceSyncClusterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 34)
)
vmwNsxMFirewallForceSyncClusterFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallForceSyncClusterFailed.setStatus(
        "current"
    )

vmwNsxMFirewallForceSyncClusterSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 35)
)
vmwNsxMFirewallForceSyncClusterSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallForceSyncClusterSuccess.setStatus(
        "current"
    )

vmwNsxMFirewallVsfwdProcessStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 3, 0, 36)
)
vmwNsxMFirewallVsfwdProcessStarted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallVsfwdProcessStarted.setStatus(
        "current"
    )

vmwNsxMEdgeNoVmServing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 1)
)
vmwNsxMEdgeNoVmServing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeNoVmServing.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 2)
)
vmwNsxMEdgeGatewayCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayCreated.setStatus(
        "current"
    )

vmwNsxMEdgeVmBadState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 3)
)
vmwNsxMEdgeVmBadState.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBadState.setStatus(
        "current"
    )

vmwNsxMEdgeVmCommFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 4)
)
vmwNsxMEdgeVmCommFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCommFailed.setStatus(
        "current"
    )

vmwNsxMEdgeVmCnfgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 5)
)
vmwNsxMEdgeVmCnfgChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCnfgChanged.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 6)
)
vmwNsxMEdgeGatewayDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayDeleted.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayReDeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 7)
)
vmwNsxMEdgeGatewayReDeployed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayReDeployed.setStatus(
        "current"
    )

vmwNsxMEdgeVmPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 8)
)
vmwNsxMEdgeVmPowerOff.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmPowerOff.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 9)
)
vmwNsxMEdgeApplianceSizeChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceSizeChanged.setStatus(
        "current"
    )

vmwNsxMEdgeUpgrade51x = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 10)
)
vmwNsxMEdgeUpgrade51x.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeUpgrade51x.setStatus(
        "current"
    )

vmwNsxMEdgeLicenseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 11)
)
vmwNsxMEdgeLicenseChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeLicenseChanged.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 12)
)
vmwNsxMEdgeApplianceMoved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceMoved.setStatus(
        "current"
    )

vmwNsxMEdgeApplianceNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 13)
)
vmwNsxMEdgeApplianceNotFound.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeApplianceNotFound.setStatus(
        "current"
    )

vmwNsxMEdgeVMHealthCheckMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 14)
)
vmwNsxMEdgeVMHealthCheckMiss.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVMHealthCheckMiss.setStatus(
        "current"
    )

vmwNsxMEdgeHealthCheckMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 15)
)
vmwNsxMEdgeHealthCheckMiss.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHealthCheckMiss.setStatus(
        "current"
    )

vmwNsxMEdgeCommAgentNotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 16)
)
vmwNsxMEdgeCommAgentNotConnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeCommAgentNotConnected.setStatus(
        "current"
    )

vmwNsxMApplianceWithDifferentId = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 17)
)
vmwNsxMApplianceWithDifferentId.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMApplianceWithDifferentId.setStatus(
        "current"
    )

vmwNsxMFirewallRuleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 18)
)
vmwNsxMFirewallRuleModified.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFirewallRuleModified.setStatus(
        "current"
    )

vmwNsxMEdgeAntiAffinityRuleViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 19)
)
vmwNsxMEdgeAntiAffinityRuleViolated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAntiAffinityRuleViolated.setStatus(
        "current"
    )

vmwNsxMEdgeHaEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 20)
)
vmwNsxMEdgeHaEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaEnabled.setStatus(
        "current"
    )

vmwNsxMEdgeHaDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 21)
)
vmwNsxMEdgeHaDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaDisabled.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 22)
)
vmwNsxMEdgeGatewayRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeVmRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 23)
)
vmwNsxMEdgeVmRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeGatewayUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 24)
)
vmwNsxMEdgeGatewayUpgraded.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeGatewayUpgraded.setStatus(
        "current"
    )

vmwNsxMEdgeVmHlthChkDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 25)
)
vmwNsxMEdgeVmHlthChkDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmHlthChkDisabled.setStatus(
        "current"
    )

vmwNsxMEdgePrePublishFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 26)
)
vmwNsxMEdgePrePublishFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgePrePublishFailed.setStatus(
        "current"
    )

vmwNsxMEdgeForcedSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 27)
)
vmwNsxMEdgeForcedSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeForcedSync.setStatus(
        "current"
    )

vmwNsxMEdgeVmBooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 28)
)
vmwNsxMEdgeVmBooted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmBooted.setStatus(
        "current"
    )

vmwNsxMEdgeVmInBadState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 29)
)
vmwNsxMEdgeVmInBadState.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmInBadState.setStatus(
        "current"
    )

vmwNsxMEdgeVmCpuUsageIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 30)
)
vmwNsxMEdgeVmCpuUsageIncreased.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmCpuUsageIncreased.setStatus(
        "current"
    )

vmwNsxMEdgeVmMemUsageIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 31)
)
vmwNsxMEdgeVmMemUsageIncreased.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmMemUsageIncreased.setStatus(
        "current"
    )

vmwNsxMEdgeVmProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 32)
)
vmwNsxMEdgeVmProcessFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmProcessFailure.setStatus(
        "current"
    )

vmwNsxMEdgeVmSysTimeBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 33)
)
vmwNsxMEdgeVmSysTimeBad.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmSysTimeBad.setStatus(
        "current"
    )

vmwNsxMEdgeVmSysTimeSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 34)
)
vmwNsxMEdgeVmSysTimeSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmSysTimeSync.setStatus(
        "current"
    )

vmwNsxMEdgeAesniCryptoEngineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 35)
)
vmwNsxMEdgeAesniCryptoEngineUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAesniCryptoEngineUp.setStatus(
        "current"
    )

vmwNsxMEdgeAesniCryptoEngineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 36)
)
vmwNsxMEdgeAesniCryptoEngineDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeAesniCryptoEngineDown.setStatus(
        "current"
    )

vmwNsxMEdgeVmOom = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 37)
)
vmwNsxMEdgeVmOom.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeVmOom.setStatus(
        "current"
    )

vmwNsxMEdgeFileSysRo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 38)
)
vmwNsxMEdgeFileSysRo.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeFileSysRo.setStatus(
        "current"
    )

vmwNsxMEdgeHaCommDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 39)
)
vmwNsxMEdgeHaCommDisconnected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaCommDisconnected.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverSelf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 40)
)
vmwNsxMEdgeHaSwitchOverSelf.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverSelf.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 41)
)
vmwNsxMEdgeHaSwitchOverActive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverActive.setStatus(
        "current"
    )

vmwNsxMEdgeHaSwitchOverStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 42)
)
vmwNsxMEdgeHaSwitchOverStandby.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeHaSwitchOverStandby.setStatus(
        "current"
    )

vmwNsxMEdgeMonitorProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 43)
)
vmwNsxMEdgeMonitorProcessFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeMonitorProcessFailure.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 44)
)
vmwNsxMLbVirtualServerPoolUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolUp.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 45)
)
vmwNsxMLbVirtualServerPoolDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolDown.setStatus(
        "current"
    )

vmwNsxMLbVirtualServerPoolWrong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 46)
)
vmwNsxMLbVirtualServerPoolWrong.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbVirtualServerPoolWrong.setStatus(
        "current"
    )

vmwNsxMLbPoolWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 47)
)
vmwNsxMLbPoolWarning.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMLbPoolWarning.setStatus(
        "current"
    )

vmwNsxMIpsecChannelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 48)
)
vmwNsxMIpsecChannelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelUp.setStatus(
        "current"
    )

vmwNsxMIpsecChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 49)
)
vmwNsxMIpsecChannelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelDown.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 50)
)
vmwNsxMIpsecTunnelUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelUp.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 51)
)
vmwNsxMIpsecTunnelDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelDown.setStatus(
        "current"
    )

vmwNsxMIpsecChannelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 52)
)
vmwNsxMIpsecChannelUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecChannelUnknown.setStatus(
        "current"
    )

vmwNsxMIpsecTunnelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 53)
)
vmwNsxMIpsecTunnelUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMIpsecTunnelUnknown.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 54)
)
vmwNsxMGlobalLbMemberUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberUp.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 55)
)
vmwNsxMGlobalLbMemberWarning.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberWarning.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 56)
)
vmwNsxMGlobalLbMemberDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberDown.setStatus(
        "current"
    )

vmwNsxMGlobalLbMemberUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 57)
)
vmwNsxMGlobalLbMemberUnknown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbMemberUnknown.setStatus(
        "current"
    )

vmwNsxMGlobalLbPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 58)
)
vmwNsxMGlobalLbPeerUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbPeerUp.setStatus(
        "current"
    )

vmwNsxMGlobalLbPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 59)
)
vmwNsxMGlobalLbPeerDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGlobalLbPeerDown.setStatus(
        "current"
    )

vmwNsxMDhcpServiceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 60)
)
vmwNsxMDhcpServiceDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDhcpServiceDisabled.setStatus(
        "current"
    )

vmwNsxMEdgeResourceReservationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 61)
)
vmwNsxMEdgeResourceReservationFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeResourceReservationFailure.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 62)
)
vmwNsxMEdgeSplitBrainDetected.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainDetected.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 63)
)
vmwNsxMEdgeSplitBrainRecovered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainRecovered.setStatus(
        "current"
    )

vmwNsxMEdgeSplitBrainRecoveryAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 4, 0, 64)
)
vmwNsxMEdgeSplitBrainRecoveryAttempt.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEdgeSplitBrainRecoveryAttempt.setStatus(
        "current"
    )

vmwNsxMEndpointThinAgentEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 1)
)
vmwNsxMEndpointThinAgentEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointThinAgentEnabled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 2)
)
vmwNsxMGuestIntrspctnEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnEnabled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnIncompatibleEsx = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 3)
)
vmwNsxMGuestIntrspctnIncompatibleEsx.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnIncompatibleEsx.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnEsxConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 4)
)
vmwNsxMGuestIntrspctnEsxConnFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnEsxConnFailed.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnStatusRcvFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 5)
)
vmwNsxMGuestIntrspctnStatusRcvFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnStatusRcvFailed.setStatus(
        "current"
    )

vmwNsxMEsxModuleEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 6)
)
vmwNsxMEsxModuleEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEsxModuleEnabled.setStatus(
        "current"
    )

vmwNsxMEsxModuleUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 7)
)
vmwNsxMEsxModuleUninstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEsxModuleUninstalled.setStatus(
        "current"
    )

vmwNsxMGuestIntrspctnHstMxMssngRep = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 8)
)
vmwNsxMGuestIntrspctnHstMxMssngRep.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMGuestIntrspctnHstMxMssngRep.setStatus(
        "current"
    )

vmwNsxMEndpointUndefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 5, 0, 9)
)
vmwNsxMEndpointUndefined.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEndpointUndefined.setStatus(
        "current"
    )

vmwNsxMEamGenericAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 6, 0, 1)
)
vmwNsxMEamGenericAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMEamGenericAlarm.setStatus(
        "current"
    )

vmwNsxMFabricDplymntStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 1)
)
vmwNsxMFabricDplymntStatusChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntStatusChanged.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 2)
)
vmwNsxMFabricDplymntUnitCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitCreated.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 3)
)
vmwNsxMFabricDplymntUnitUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitUpdated.setStatus(
        "current"
    )

vmwNsxMFabricDplymntUnitDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 4)
)
vmwNsxMFabricDplymntUnitDestroyed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntUnitDestroyed.setStatus(
        "current"
    )

vmwNsxMDataStoreNotCnfgrdOnHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 5)
)
vmwNsxMDataStoreNotCnfgrdOnHost.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataStoreNotCnfgrdOnHost.setStatus(
        "current"
    )

vmwNsxMFabricDplymntInstallationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 6)
)
vmwNsxMFabricDplymntInstallationFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDplymntInstallationFailed.setStatus(
        "current"
    )

vmwNsxMFabricAgentCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 7)
)
vmwNsxMFabricAgentCreated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricAgentCreated.setStatus(
        "current"
    )

vmwNsxMFabricAgentDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 8)
)
vmwNsxMFabricAgentDestroyed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricAgentDestroyed.setStatus(
        "current"
    )

vmwNsxMFabricSrvceNeedsRedplymnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 9)
)
vmwNsxMFabricSrvceNeedsRedplymnt.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricSrvceNeedsRedplymnt.setStatus(
        "current"
    )

vmwNsxMUpgradeOfDplymntFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 10)
)
vmwNsxMUpgradeOfDplymntFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUpgradeOfDplymntFailed.setStatus(
        "current"
    )

vmwNsxMFabricDependenciesNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 11)
)
vmwNsxMFabricDependenciesNotInstalled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricDependenciesNotInstalled.setStatus(
        "current"
    )

vmwNsxMFabricErrorNotifSecBfrUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 12)
)
vmwNsxMFabricErrorNotifSecBfrUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrorNotifSecBfrUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricErrCallbackNtRcvdUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 13)
)
vmwNsxMFabricErrCallbackNtRcvdUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrCallbackNtRcvdUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricErrCallbackNtRcvdUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 14)
)
vmwNsxMFabricErrCallbackNtRcvdUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrCallbackNtRcvdUninstall.setStatus(
        "current"
    )

vmwNsxMFabricUninstallServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 15)
)
vmwNsxMFabricUninstallServiceFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricUninstallServiceFailed.setStatus(
        "current"
    )

vmwNsxMFabricErrorNotifSecBfrUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 16)
)
vmwNsxMFabricErrorNotifSecBfrUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricErrorNotifSecBfrUninstall.setStatus(
        "current"
    )

vmwNsxMFabricServerRebootUninstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 17)
)
vmwNsxMFabricServerRebootUninstall.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricServerRebootUninstall.setStatus(
        "current"
    )

vmwNsxMFabricServerRebootUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 18)
)
vmwNsxMFabricServerRebootUpgrade.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricServerRebootUpgrade.setStatus(
        "current"
    )

vmwNsxMFabricConnEamFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 19)
)
vmwNsxMFabricConnEamFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricConnEamFailed.setStatus(
        "current"
    )

vmwNsxMFabricConnEamRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 20)
)
vmwNsxMFabricConnEamRestored.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricConnEamRestored.setStatus(
        "current"
    )

vmwNsxMFabricPreUninstallCleanUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 21)
)
vmwNsxMFabricPreUninstallCleanUpFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricPreUninstallCleanUpFailed.setStatus(
        "current"
    )

vmwNsxMFabricBackingEamNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 7, 0, 22)
)
vmwNsxMFabricBackingEamNotFound.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFabricBackingEamNotFound.setStatus(
        "current"
    )

vmwNsxMDepPluginIpPoolExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 1)
)
vmwNsxMDepPluginIpPoolExhausted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginIpPoolExhausted.setStatus(
        "current"
    )

vmwNsxMDepPluginGenericAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 2)
)
vmwNsxMDepPluginGenericAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginGenericAlarm.setStatus(
        "current"
    )

vmwNsxMDepPluginGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 3)
)
vmwNsxMDepPluginGenericException.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginGenericException.setStatus(
        "current"
    )

vmwNsxMDepPluginVmReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 8, 0, 4)
)
vmwNsxMDepPluginVmReboot.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDepPluginVmReboot.setStatus(
        "current"
    )

vmwNsxMMessagingConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 1)
)
vmwNsxMMessagingConfigFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingConfigFailed.setStatus(
        "current"
    )

vmwNsxMMessagingReconfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 2)
)
vmwNsxMMessagingReconfigFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingReconfigFailed.setStatus(
        "current"
    )

vmwNsxMMessagingConfigFailedNotifSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 3)
)
vmwNsxMMessagingConfigFailedNotifSkip.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingConfigFailedNotifSkip.setStatus(
        "current"
    )

vmwNsxMMessagingInfraUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 4)
)
vmwNsxMMessagingInfraUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingInfraUp.setStatus(
        "current"
    )

vmwNsxMMessagingInfraDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 5)
)
vmwNsxMMessagingInfraDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingInfraDown.setStatus(
        "current"
    )

vmwNsxMMessagingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 9, 0, 6)
)
vmwNsxMMessagingDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMMessagingDisabled.setStatus(
        "current"
    )

vmwNsxMServiceComposerPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 1)
)
vmwNsxMServiceComposerPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 2)
)
vmwNsxMServiceComposerPolicyDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerPolicyDeleted.setStatus(
        "current"
    )

vmwNsxMServiceComposerFirewallPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 3)
)
vmwNsxMServiceComposerFirewallPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerFirewallPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerNetworkPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 4)
)
vmwNsxMServiceComposerNetworkPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerNetworkPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerGuestPolicyOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 5)
)
vmwNsxMServiceComposerGuestPolicyOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerGuestPolicyOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 6)
)
vmwNsxMServiceComposerOutOfSync.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSync.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncRebootFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 7)
)
vmwNsxMServiceComposerOutOfSyncRebootFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncRebootFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncDraftRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 8)
)
vmwNsxMServiceComposerOutOfSyncDraftRollback.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncDraftRollback.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 9)
)
vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 10)
)
vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure.setStatus(
        "current"
    )

vmwNsxMServiceComposerOutOfSyncDraftSettingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 10, 0, 11)
)
vmwNsxMServiceComposerOutOfSyncDraftSettingFailure.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServiceComposerOutOfSyncDraftSettingFailure.setStatus(
        "current"
    )

vmwNsxMInconsistentSvmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 1)
)
vmwNsxMInconsistentSvmAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMInconsistentSvmAlarm.setStatus(
        "current"
    )

vmwNsxMSvmRestartAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 2)
)
vmwNsxMSvmRestartAlarm.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSvmRestartAlarm.setStatus(
        "current"
    )

vmwNsxMSvmAgentUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 11, 0, 3)
)
vmwNsxMSvmAgentUnavailable.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSvmAgentUnavailable.setStatus(
        "current"
    )

vmwNsxMVmAddedToSg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0, 1)
)
vmwNsxMVmAddedToSg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVmAddedToSg.setStatus(
        "current"
    )

vmwNsxMVmRemovedFromSg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 12, 0, 2)
)
vmwNsxMVmRemovedFromSg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVmRemovedFromSg.setStatus(
        "current"
    )

vmwNsxMFullUniversalSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 1)
)
vmwNsxMFullUniversalSyncFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMFullUniversalSyncFailed.setStatus(
        "current"
    )

vmwNsxMSecondaryDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 2)
)
vmwNsxMSecondaryDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSecondaryDown.setStatus(
        "current"
    )

vmwNsxMUniversalSyncFailedForEntity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 13, 0, 3)
)
vmwNsxMUniversalSyncFailedForEntity.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUniversalSyncFailedForEntity.setStatus(
        "current"
    )

vmwNsxMServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 14, 0, 1)
)
vmwNsxMServerUp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMServerUp.setStatus(
        "current"
    )

vmwNsxMExtensionRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0, 1)
)
vmwNsxMExtensionRegistered.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionRegistered.setStatus(
        "current"
    )

vmwNsxMExtensionUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 15, 0, 2)
)
vmwNsxMExtensionUpdated.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMExtensionUpdated.setStatus(
        "current"
    )

vmwNsxMDataSecScanStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0, 1)
)
vmwNsxMDataSecScanStarted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataSecScanStarted.setStatus(
        "current"
    )

vmwNsxMDataSecScanEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 16, 0, 2)
)
vmwNsxMDataSecScanEnded.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDataSecScanEnded.setStatus(
        "current"
    )

vmwNsxMSamDataCollectionEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 1)
)
vmwNsxMSamDataCollectionEnabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataCollectionEnabled.setStatus(
        "current"
    )

vmwNsxMSamDataCollectionDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 2)
)
vmwNsxMSamDataCollectionDisabled.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataCollectionDisabled.setStatus(
        "current"
    )

vmwNsxMSamDataStoppedFlowing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 3)
)
vmwNsxMSamDataStoppedFlowing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataStoppedFlowing.setStatus(
        "current"
    )

vmwNsxMSamDataResumedFlowing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 17, 0, 4)
)
vmwNsxMSamDataResumedFlowing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMSamDataResumedFlowing.setStatus(
        "current"
    )

vmwNsxMUsvmHeartbeatStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 1)
)
vmwNsxMUsvmHeartbeatStopped.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmHeartbeatStopped.setStatus(
        "current"
    )

vmwNsxMUsvmHeartbeatResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 2)
)
vmwNsxMUsvmHeartbeatResumed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmHeartbeatResumed.setStatus(
        "current"
    )

vmwNsxMUsvmReceivedHello = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 18, 0, 3)
)
vmwNsxMUsvmReceivedHello.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUsvmReceivedHello.setStatus(
        "current"
    )

vmwNsxMUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 1)
)
vmwNsxMUpgradeSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMUpgradeSuccess.setStatus(
        "current"
    )

vmwNsxMRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 2)
)
vmwNsxMRestoreSuccess.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMRestoreSuccess.setStatus(
        "current"
    )

vmwNsxMDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 19, 0, 3)
)
vmwNsxMDuplicateIp.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMDuplicateIp.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchImproperlyCnfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 1)
)
vmwNsxMVxlanLogicalSwitchImproperlyCnfg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchImproperlyCnfg.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchProperlyCnfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 2)
)
vmwNsxMVxlanLogicalSwitchProperlyCnfg.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchProperlyCnfg.setStatus(
        "current"
    )

vmwNsxMVxlanInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 3)
)
vmwNsxMVxlanInitFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInitFailed.setStatus(
        "current"
    )

vmwNsxMVxlanPortInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 4)
)
vmwNsxMVxlanPortInitFailed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanPortInitFailed.setStatus(
        "current"
    )

vmwNsxMVxlanInstanceDoesNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 5)
)
vmwNsxMVxlanInstanceDoesNotExist.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInstanceDoesNotExist.setStatus(
        "current"
    )

vmwNsxMVxlanLogicalSwitchWrkngImproperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 6)
)
vmwNsxMVxlanLogicalSwitchWrkngImproperly.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanLogicalSwitchWrkngImproperly.setStatus(
        "current"
    )

vmwNsxMVxlanTransportZoneIncorrectlyWrkng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 7)
)
vmwNsxMVxlanTransportZoneIncorrectlyWrkng.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanTransportZoneIncorrectlyWrkng.setStatus(
        "current"
    )

vmwNsxMVxlanTransportZoneNotUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 8)
)
vmwNsxMVxlanTransportZoneNotUsed.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanTransportZoneNotUsed.setStatus(
        "current"
    )

vmwNsxMVxlanOverlayClassMissingOnDvs = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 9)
)
vmwNsxMVxlanOverlayClassMissingOnDvs.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanOverlayClassMissingOnDvs.setStatus(
        "current"
    )

vmwNsxMVxlanControllerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 10)
)
vmwNsxMVxlanControllerRemoved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerRemoved.setStatus(
        "current"
    )

vmwNsxMVxlanControllerConnProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 11)
)
vmwNsxMVxlanControllerConnProblem.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerConnProblem.setStatus(
        "current"
    )

vmwNsxMVxlanControllerInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 12)
)
vmwNsxMVxlanControllerInactive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerInactive.setStatus(
        "current"
    )

vmwNsxMVxlanControllerActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 13)
)
vmwNsxMVxlanControllerActive.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanControllerActive.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicMissingOrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 14)
)
vmwNsxMVxlanVmknicMissingOrDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicMissingOrDeleted.setStatus(
        "current"
    )

vmwNsxMVxlanInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 15)
)
vmwNsxMVxlanInfo.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanInfo.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicPortGrpMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 16)
)
vmwNsxMVxlanVmknicPortGrpMissing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicPortGrpMissing.setStatus(
        "current"
    )

vmwNsxMVxlanVmknicPortGrpAppears = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 17)
)
vmwNsxMVxlanVmknicPortGrpAppears.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanVmknicPortGrpAppears.setStatus(
        "current"
    )

vmwNsxMVxlanConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 18)
)
vmwNsxMVxlanConnDown.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanConnDown.setStatus(
        "current"
    )

vmwNsxMBackingPortgroupMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 19)
)
vmwNsxMBackingPortgroupMissing.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMBackingPortgroupMissing.setStatus(
        "current"
    )

vmwNsxMBackingPortgroupReappears = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 20)
)
vmwNsxMBackingPortgroupReappears.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMBackingPortgroupReappears.setStatus(
        "current"
    )

vmwNsxMManagedObjectIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 21)
)
vmwNsxMManagedObjectIdChanged.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMManagedObjectIdChanged.setStatus(
        "current"
    )

vmwNsxMHighLatencyOnDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 22)
)
vmwNsxMHighLatencyOnDisk.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMHighLatencyOnDisk.setStatus(
        "current"
    )

vmwNsxMHighLatencyOnDiskResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 23)
)
vmwNsxMHighLatencyOnDiskResolved.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMHighLatencyOnDiskResolved.setStatus(
        "current"
    )

vmwNsxMControllerVmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 24)
)
vmwNsxMControllerVmPoweredOff.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMControllerVmPoweredOff.setStatus(
        "current"
    )

vmwNsxMControllerVmDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 25)
)
vmwNsxMControllerVmDeleted.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMControllerVmDeleted.setStatus(
        "current"
    )

vmwNsxMVxlanConfigNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 2, 20, 0, 26)
)
vmwNsxMVxlanConfigNotSet.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventCode"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventTimestamp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventMessage"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventSeverity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEventComponent"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUuid"))
)
if mibBuilder.loadTexts:
    vmwNsxMVxlanConfigNotSet.setStatus(
        "current"
    )


# Notifications groups

vmwNsxManagerNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 2, 3)
)
vmwNsxManagerNotificationGroup1.setObjects(
      *(("VMWARE-NSX-MANAGER-MIB", "vmwNsxMConfigGroup"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpAddedBlackList"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpRemovedBlackList"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoConfigFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoUnconfigured"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUserRoleAssigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUserRoleUnassigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGroupRoleAssigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGroupRoleUnassigned"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVcLoginFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVcDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLostVcConnectivity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgNotAppliedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCnfgAppliedToVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrCreatedForVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFltrDeletedForVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallConfigUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleFailedVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleAppliedVnic"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFlowMissed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardCnfgUpdateFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardApplied"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardDisableFail"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLegacyAppServiceDeletionFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCpuThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallMemThresholdCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMConnPerSecThrshldCrossed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCnfgUpdateTimedOut"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardCnfgUpdateTmOut"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallPublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMCntnrUpdatePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSpoofGuardUpdatePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExcludeListPublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallCnfgUpdateOnDltCntnr"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHostSyncFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHostSynced"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterUninstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallClusterDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeNoVmServing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBadState"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCommFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCnfgChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayReDeployed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmPowerOff"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceSizeChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeUpgrade51x"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeLicenseChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceMoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeApplianceNotFound"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVMHealthCheckMiss"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHealthCheckMiss"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeCommAgentNotConnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMApplianceWithDifferentId"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallRuleModified"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAntiAffinityRuleViolated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeGatewayUpgraded"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmHlthChkDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgePrePublishFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeForcedSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmBooted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmInBadState"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmCpuUsageIncreased"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmMemUsageIncreased"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmProcessFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmSysTimeBad"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmSysTimeSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAesniCryptoEngineUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeAesniCryptoEngineDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeVmOom"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeFileSysRo"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaCommDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverSelf"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverActive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeHaSwitchOverStandby"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeMonitorProcessFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbVirtualServerPoolWrong"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMLbPoolWarning"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecChannelUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMIpsecTunnelUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberWarning"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbMemberUnknown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbPeerUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGlobalLbPeerDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDhcpServiceDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEndpointThinAgentEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnIncompatibleEsx"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnEsxConnFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnStatusRcvFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEsxModuleEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEsxModuleUninstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMGuestIntrspctnHstMxMssngRep"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEndpointUndefined"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEamGenericAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntStatusChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntUnitDestroyed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataStoreNotCnfgrdOnHost"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDplymntInstallationFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricAgentCreated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricAgentDestroyed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricSrvceNeedsRedplymnt"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUpgradeOfDplymntFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricDependenciesNotInstalled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrorNotifSecBfrUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrCallbackNtRcvdUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrCallbackNtRcvdUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricUninstallServiceFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricErrorNotifSecBfrUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricServerRebootUninstall"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricServerRebootUpgrade"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricConnEamFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricConnEamRestored"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricPreUninstallCleanUpFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFabricBackingEamNotFound"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginIpPoolExhausted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginGenericAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginGenericException"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDepPluginVmReboot"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingConfigFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingReconfigFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingConfigFailedNotifSkip"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingInfraUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingInfraDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMMessagingDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerPolicyDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMInconsistentSvmAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSvmRestartAlarm"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSvmAgentUnavailable"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVmAddedToSg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVmRemovedFromSg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFullUniversalSyncFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSecondaryDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUniversalSyncFailedForEntity"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServerUp"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExtensionRegistered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMExtensionUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataSecScanStarted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDataSecScanEnded"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionEnabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataStoppedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataResumedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmHeartbeatStopped"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmHeartbeatResumed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUsvmReceivedHello"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMUpgradeSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMRestoreSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchImproperlyCnfg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchProperlyCnfg"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInitFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanPortInitFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInstanceDoesNotExist"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanLogicalSwitchWrkngImproperly"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanTransportZoneIncorrectlyWrkng"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanTransportZoneNotUsed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanOverlayClassMissingOnDvs"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerRemoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerConnProblem"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerInactive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerActive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicMissingOrDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanInfo"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicPortGrpMissing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanVmknicPortGrpAppears"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanConnDown"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataCollectionDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataStoppedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSamDataResumedFlowing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanOverlayClassMissingOnDvs"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerRemoved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerConnProblem"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanControllerInactive"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSsoDisconnected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallInstallFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallForceSyncClusterFailed"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallForceSyncClusterSuccess"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMFirewallVsfwdProcessStarted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeResourceReservationFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainDetected"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainRecovered"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMEdgeSplitBrainRecoveryAttempt"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerFirewallPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerNetworkPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerGuestPolicyOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSync"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncRebootFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncDraftRollback"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMServiceComposerOutOfSyncDraftSettingFailure"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMBackingPortgroupMissing"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMBackingPortgroupReappears"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMManagedObjectIdChanged"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHighLatencyOnDisk"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMHighLatencyOnDiskResolved"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMControllerVmPoweredOff"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMControllerVmDeleted"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMVxlanConfigNotSet"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSnmpDisabled"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMSnmpManagerConfigUpdated"),
        ("VMWARE-NSX-MANAGER-MIB", "vmwNsxMDuplicateIp"))
)
if mibBuilder.loadTexts:
    vmwNsxManagerNotificationGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwNsxManagerMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 90, 1, 99, 1, 3)
)
if mibBuilder.loadTexts:
    vmwNsxManagerMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-NSX-MANAGER-MIB",
    **{"VmwNsxManagerTypeSeverity": VmwNsxManagerTypeSeverity,
       "vmwNsxManagerMIB": vmwNsxManagerMIB,
       "vmwNsxMAlertData": vmwNsxMAlertData,
       "vmwNsxMEventCode": vmwNsxMEventCode,
       "vmwNsxMEventTimestamp": vmwNsxMEventTimestamp,
       "vmwNsxMEventMessage": vmwNsxMEventMessage,
       "vmwNsxMEventSeverity": vmwNsxMEventSeverity,
       "vmwNsxMEventComponent": vmwNsxMEventComponent,
       "vmwNsxMUuid": vmwNsxMUuid,
       "vmwNsxMCount": vmwNsxMCount,
       "vmwNsxMNotification": vmwNsxMNotification,
       "vmwNsxMBranch": vmwNsxMBranch,
       "vmwNsxMGroupsBranch": vmwNsxMGroupsBranch,
       "vmwNsxMGroupsPrefix": vmwNsxMGroupsPrefix,
       "vmwNsxMConfigGroup": vmwNsxMConfigGroup,
       "vmwNsxMSnmp": vmwNsxMSnmp,
       "vmwNsxMSnmpPrefix": vmwNsxMSnmpPrefix,
       "vmwNsxMSnmpDisabled": vmwNsxMSnmpDisabled,
       "vmwNsxMSnmpManagerConfigUpdated": vmwNsxMSnmpManagerConfigUpdated,
       "vmwNsxMSecurity": vmwNsxMSecurity,
       "vmwNsxMSecurityPrefix": vmwNsxMSecurityPrefix,
       "vmwNsxMIpAddedBlackList": vmwNsxMIpAddedBlackList,
       "vmwNsxMIpRemovedBlackList": vmwNsxMIpRemovedBlackList,
       "vmwNsxMSsoConfigFailure": vmwNsxMSsoConfigFailure,
       "vmwNsxMSsoUnconfigured": vmwNsxMSsoUnconfigured,
       "vmwNsxMUserRoleAssigned": vmwNsxMUserRoleAssigned,
       "vmwNsxMUserRoleUnassigned": vmwNsxMUserRoleUnassigned,
       "vmwNsxMGroupRoleAssigned": vmwNsxMGroupRoleAssigned,
       "vmwNsxMGroupRoleUnassigned": vmwNsxMGroupRoleUnassigned,
       "vmwNsxMVcLoginFailed": vmwNsxMVcLoginFailed,
       "vmwNsxMVcDisconnected": vmwNsxMVcDisconnected,
       "vmwNsxMLostVcConnectivity": vmwNsxMLostVcConnectivity,
       "vmwNsxMSsoDisconnected": vmwNsxMSsoDisconnected,
       "vmwNsxMFirewall": vmwNsxMFirewall,
       "vmwNsxMFirewallPrefix": vmwNsxMFirewallPrefix,
       "vmwNsxMFltrCnfgUpdateFailed": vmwNsxMFltrCnfgUpdateFailed,
       "vmwNsxMFltrCnfgNotAppliedToVnic": vmwNsxMFltrCnfgNotAppliedToVnic,
       "vmwNsxMFltrCnfgAppliedToVnic": vmwNsxMFltrCnfgAppliedToVnic,
       "vmwNsxMFltrCreatedForVnic": vmwNsxMFltrCreatedForVnic,
       "vmwNsxMFltrDeletedForVnic": vmwNsxMFltrDeletedForVnic,
       "vmwNsxMFirewallConfigUpdateFailed": vmwNsxMFirewallConfigUpdateFailed,
       "vmwNsxMFirewallRuleFailedVnic": vmwNsxMFirewallRuleFailedVnic,
       "vmwNsxMFirewallRuleAppliedVnic": vmwNsxMFirewallRuleAppliedVnic,
       "vmwNsxMCntnrCnfgUpdateFailed": vmwNsxMCntnrCnfgUpdateFailed,
       "vmwNsxMFlowMissed": vmwNsxMFlowMissed,
       "vmwNsxMSpoofGuardCnfgUpdateFailed": vmwNsxMSpoofGuardCnfgUpdateFailed,
       "vmwNsxMSpoofGuardFailed": vmwNsxMSpoofGuardFailed,
       "vmwNsxMSpoofGuardApplied": vmwNsxMSpoofGuardApplied,
       "vmwNsxMSpoofGuardDisableFail": vmwNsxMSpoofGuardDisableFail,
       "vmwNsxMSpoofGuardDisabled": vmwNsxMSpoofGuardDisabled,
       "vmwNsxMLegacyAppServiceDeletionFailed": vmwNsxMLegacyAppServiceDeletionFailed,
       "vmwNsxMFirewallCpuThresholdCrossed": vmwNsxMFirewallCpuThresholdCrossed,
       "vmwNsxMFirewallMemThresholdCrossed": vmwNsxMFirewallMemThresholdCrossed,
       "vmwNsxMConnPerSecThrshldCrossed": vmwNsxMConnPerSecThrshldCrossed,
       "vmwNsxMFirewallCnfgUpdateTimedOut": vmwNsxMFirewallCnfgUpdateTimedOut,
       "vmwNsxMSpoofGuardCnfgUpdateTmOut": vmwNsxMSpoofGuardCnfgUpdateTmOut,
       "vmwNsxMFirewallPublishFailed": vmwNsxMFirewallPublishFailed,
       "vmwNsxMCntnrUpdatePublishFailed": vmwNsxMCntnrUpdatePublishFailed,
       "vmwNsxMSpoofGuardUpdatePublishFailed": vmwNsxMSpoofGuardUpdatePublishFailed,
       "vmwNsxMExcludeListPublishFailed": vmwNsxMExcludeListPublishFailed,
       "vmwNsxMFirewallCnfgUpdateOnDltCntnr": vmwNsxMFirewallCnfgUpdateOnDltCntnr,
       "vmwNsxMHostSyncFailed": vmwNsxMHostSyncFailed,
       "vmwNsxMHostSynced": vmwNsxMHostSynced,
       "vmwNsxMFirewallInstalled": vmwNsxMFirewallInstalled,
       "vmwNsxMFirewallInstallFailed": vmwNsxMFirewallInstallFailed,
       "vmwNsxMFirewallClusterInstalled": vmwNsxMFirewallClusterInstalled,
       "vmwNsxMFirewallClusterUninstalled": vmwNsxMFirewallClusterUninstalled,
       "vmwNsxMFirewallClusterDisabled": vmwNsxMFirewallClusterDisabled,
       "vmwNsxMFirewallForceSyncClusterFailed": vmwNsxMFirewallForceSyncClusterFailed,
       "vmwNsxMFirewallForceSyncClusterSuccess": vmwNsxMFirewallForceSyncClusterSuccess,
       "vmwNsxMFirewallVsfwdProcessStarted": vmwNsxMFirewallVsfwdProcessStarted,
       "vmwNsxMEdge": vmwNsxMEdge,
       "vmwNsxMEdgePrefix": vmwNsxMEdgePrefix,
       "vmwNsxMEdgeNoVmServing": vmwNsxMEdgeNoVmServing,
       "vmwNsxMEdgeGatewayCreated": vmwNsxMEdgeGatewayCreated,
       "vmwNsxMEdgeVmBadState": vmwNsxMEdgeVmBadState,
       "vmwNsxMEdgeVmCommFailed": vmwNsxMEdgeVmCommFailed,
       "vmwNsxMEdgeVmCnfgChanged": vmwNsxMEdgeVmCnfgChanged,
       "vmwNsxMEdgeGatewayDeleted": vmwNsxMEdgeGatewayDeleted,
       "vmwNsxMEdgeGatewayReDeployed": vmwNsxMEdgeGatewayReDeployed,
       "vmwNsxMEdgeVmPowerOff": vmwNsxMEdgeVmPowerOff,
       "vmwNsxMEdgeApplianceSizeChanged": vmwNsxMEdgeApplianceSizeChanged,
       "vmwNsxMEdgeUpgrade51x": vmwNsxMEdgeUpgrade51x,
       "vmwNsxMEdgeLicenseChanged": vmwNsxMEdgeLicenseChanged,
       "vmwNsxMEdgeApplianceMoved": vmwNsxMEdgeApplianceMoved,
       "vmwNsxMEdgeApplianceNotFound": vmwNsxMEdgeApplianceNotFound,
       "vmwNsxMEdgeVMHealthCheckMiss": vmwNsxMEdgeVMHealthCheckMiss,
       "vmwNsxMEdgeHealthCheckMiss": vmwNsxMEdgeHealthCheckMiss,
       "vmwNsxMEdgeCommAgentNotConnected": vmwNsxMEdgeCommAgentNotConnected,
       "vmwNsxMApplianceWithDifferentId": vmwNsxMApplianceWithDifferentId,
       "vmwNsxMFirewallRuleModified": vmwNsxMFirewallRuleModified,
       "vmwNsxMEdgeAntiAffinityRuleViolated": vmwNsxMEdgeAntiAffinityRuleViolated,
       "vmwNsxMEdgeHaEnabled": vmwNsxMEdgeHaEnabled,
       "vmwNsxMEdgeHaDisabled": vmwNsxMEdgeHaDisabled,
       "vmwNsxMEdgeGatewayRecovered": vmwNsxMEdgeGatewayRecovered,
       "vmwNsxMEdgeVmRecovered": vmwNsxMEdgeVmRecovered,
       "vmwNsxMEdgeGatewayUpgraded": vmwNsxMEdgeGatewayUpgraded,
       "vmwNsxMEdgeVmHlthChkDisabled": vmwNsxMEdgeVmHlthChkDisabled,
       "vmwNsxMEdgePrePublishFailed": vmwNsxMEdgePrePublishFailed,
       "vmwNsxMEdgeForcedSync": vmwNsxMEdgeForcedSync,
       "vmwNsxMEdgeVmBooted": vmwNsxMEdgeVmBooted,
       "vmwNsxMEdgeVmInBadState": vmwNsxMEdgeVmInBadState,
       "vmwNsxMEdgeVmCpuUsageIncreased": vmwNsxMEdgeVmCpuUsageIncreased,
       "vmwNsxMEdgeVmMemUsageIncreased": vmwNsxMEdgeVmMemUsageIncreased,
       "vmwNsxMEdgeVmProcessFailure": vmwNsxMEdgeVmProcessFailure,
       "vmwNsxMEdgeVmSysTimeBad": vmwNsxMEdgeVmSysTimeBad,
       "vmwNsxMEdgeVmSysTimeSync": vmwNsxMEdgeVmSysTimeSync,
       "vmwNsxMEdgeAesniCryptoEngineUp": vmwNsxMEdgeAesniCryptoEngineUp,
       "vmwNsxMEdgeAesniCryptoEngineDown": vmwNsxMEdgeAesniCryptoEngineDown,
       "vmwNsxMEdgeVmOom": vmwNsxMEdgeVmOom,
       "vmwNsxMEdgeFileSysRo": vmwNsxMEdgeFileSysRo,
       "vmwNsxMEdgeHaCommDisconnected": vmwNsxMEdgeHaCommDisconnected,
       "vmwNsxMEdgeHaSwitchOverSelf": vmwNsxMEdgeHaSwitchOverSelf,
       "vmwNsxMEdgeHaSwitchOverActive": vmwNsxMEdgeHaSwitchOverActive,
       "vmwNsxMEdgeHaSwitchOverStandby": vmwNsxMEdgeHaSwitchOverStandby,
       "vmwNsxMEdgeMonitorProcessFailure": vmwNsxMEdgeMonitorProcessFailure,
       "vmwNsxMLbVirtualServerPoolUp": vmwNsxMLbVirtualServerPoolUp,
       "vmwNsxMLbVirtualServerPoolDown": vmwNsxMLbVirtualServerPoolDown,
       "vmwNsxMLbVirtualServerPoolWrong": vmwNsxMLbVirtualServerPoolWrong,
       "vmwNsxMLbPoolWarning": vmwNsxMLbPoolWarning,
       "vmwNsxMIpsecChannelUp": vmwNsxMIpsecChannelUp,
       "vmwNsxMIpsecChannelDown": vmwNsxMIpsecChannelDown,
       "vmwNsxMIpsecTunnelUp": vmwNsxMIpsecTunnelUp,
       "vmwNsxMIpsecTunnelDown": vmwNsxMIpsecTunnelDown,
       "vmwNsxMIpsecChannelUnknown": vmwNsxMIpsecChannelUnknown,
       "vmwNsxMIpsecTunnelUnknown": vmwNsxMIpsecTunnelUnknown,
       "vmwNsxMGlobalLbMemberUp": vmwNsxMGlobalLbMemberUp,
       "vmwNsxMGlobalLbMemberWarning": vmwNsxMGlobalLbMemberWarning,
       "vmwNsxMGlobalLbMemberDown": vmwNsxMGlobalLbMemberDown,
       "vmwNsxMGlobalLbMemberUnknown": vmwNsxMGlobalLbMemberUnknown,
       "vmwNsxMGlobalLbPeerUp": vmwNsxMGlobalLbPeerUp,
       "vmwNsxMGlobalLbPeerDown": vmwNsxMGlobalLbPeerDown,
       "vmwNsxMDhcpServiceDisabled": vmwNsxMDhcpServiceDisabled,
       "vmwNsxMEdgeResourceReservationFailure": vmwNsxMEdgeResourceReservationFailure,
       "vmwNsxMEdgeSplitBrainDetected": vmwNsxMEdgeSplitBrainDetected,
       "vmwNsxMEdgeSplitBrainRecovered": vmwNsxMEdgeSplitBrainRecovered,
       "vmwNsxMEdgeSplitBrainRecoveryAttempt": vmwNsxMEdgeSplitBrainRecoveryAttempt,
       "vmwNsxMEndpoint": vmwNsxMEndpoint,
       "vmwNsxMEndpointPrefix": vmwNsxMEndpointPrefix,
       "vmwNsxMEndpointThinAgentEnabled": vmwNsxMEndpointThinAgentEnabled,
       "vmwNsxMGuestIntrspctnEnabled": vmwNsxMGuestIntrspctnEnabled,
       "vmwNsxMGuestIntrspctnIncompatibleEsx": vmwNsxMGuestIntrspctnIncompatibleEsx,
       "vmwNsxMGuestIntrspctnEsxConnFailed": vmwNsxMGuestIntrspctnEsxConnFailed,
       "vmwNsxMGuestIntrspctnStatusRcvFailed": vmwNsxMGuestIntrspctnStatusRcvFailed,
       "vmwNsxMEsxModuleEnabled": vmwNsxMEsxModuleEnabled,
       "vmwNsxMEsxModuleUninstalled": vmwNsxMEsxModuleUninstalled,
       "vmwNsxMGuestIntrspctnHstMxMssngRep": vmwNsxMGuestIntrspctnHstMxMssngRep,
       "vmwNsxMEndpointUndefined": vmwNsxMEndpointUndefined,
       "vmwNsxMEam": vmwNsxMEam,
       "vmwNsxMEamPrefix": vmwNsxMEamPrefix,
       "vmwNsxMEamGenericAlarm": vmwNsxMEamGenericAlarm,
       "vmwNsxMFabric": vmwNsxMFabric,
       "vmwNsxMFabricPrefix": vmwNsxMFabricPrefix,
       "vmwNsxMFabricDplymntStatusChanged": vmwNsxMFabricDplymntStatusChanged,
       "vmwNsxMFabricDplymntUnitCreated": vmwNsxMFabricDplymntUnitCreated,
       "vmwNsxMFabricDplymntUnitUpdated": vmwNsxMFabricDplymntUnitUpdated,
       "vmwNsxMFabricDplymntUnitDestroyed": vmwNsxMFabricDplymntUnitDestroyed,
       "vmwNsxMDataStoreNotCnfgrdOnHost": vmwNsxMDataStoreNotCnfgrdOnHost,
       "vmwNsxMFabricDplymntInstallationFailed": vmwNsxMFabricDplymntInstallationFailed,
       "vmwNsxMFabricAgentCreated": vmwNsxMFabricAgentCreated,
       "vmwNsxMFabricAgentDestroyed": vmwNsxMFabricAgentDestroyed,
       "vmwNsxMFabricSrvceNeedsRedplymnt": vmwNsxMFabricSrvceNeedsRedplymnt,
       "vmwNsxMUpgradeOfDplymntFailed": vmwNsxMUpgradeOfDplymntFailed,
       "vmwNsxMFabricDependenciesNotInstalled": vmwNsxMFabricDependenciesNotInstalled,
       "vmwNsxMFabricErrorNotifSecBfrUpgrade": vmwNsxMFabricErrorNotifSecBfrUpgrade,
       "vmwNsxMFabricErrCallbackNtRcvdUpgrade": vmwNsxMFabricErrCallbackNtRcvdUpgrade,
       "vmwNsxMFabricErrCallbackNtRcvdUninstall": vmwNsxMFabricErrCallbackNtRcvdUninstall,
       "vmwNsxMFabricUninstallServiceFailed": vmwNsxMFabricUninstallServiceFailed,
       "vmwNsxMFabricErrorNotifSecBfrUninstall": vmwNsxMFabricErrorNotifSecBfrUninstall,
       "vmwNsxMFabricServerRebootUninstall": vmwNsxMFabricServerRebootUninstall,
       "vmwNsxMFabricServerRebootUpgrade": vmwNsxMFabricServerRebootUpgrade,
       "vmwNsxMFabricConnEamFailed": vmwNsxMFabricConnEamFailed,
       "vmwNsxMFabricConnEamRestored": vmwNsxMFabricConnEamRestored,
       "vmwNsxMFabricPreUninstallCleanUpFailed": vmwNsxMFabricPreUninstallCleanUpFailed,
       "vmwNsxMFabricBackingEamNotFound": vmwNsxMFabricBackingEamNotFound,
       "vmwNsxMDepPlugin": vmwNsxMDepPlugin,
       "vmwNsxMDepPluginPrefix": vmwNsxMDepPluginPrefix,
       "vmwNsxMDepPluginIpPoolExhausted": vmwNsxMDepPluginIpPoolExhausted,
       "vmwNsxMDepPluginGenericAlarm": vmwNsxMDepPluginGenericAlarm,
       "vmwNsxMDepPluginGenericException": vmwNsxMDepPluginGenericException,
       "vmwNsxMDepPluginVmReboot": vmwNsxMDepPluginVmReboot,
       "vmwNsxMMessaging": vmwNsxMMessaging,
       "vmwNsxMMessagingPrefix": vmwNsxMMessagingPrefix,
       "vmwNsxMMessagingConfigFailed": vmwNsxMMessagingConfigFailed,
       "vmwNsxMMessagingReconfigFailed": vmwNsxMMessagingReconfigFailed,
       "vmwNsxMMessagingConfigFailedNotifSkip": vmwNsxMMessagingConfigFailedNotifSkip,
       "vmwNsxMMessagingInfraUp": vmwNsxMMessagingInfraUp,
       "vmwNsxMMessagingInfraDown": vmwNsxMMessagingInfraDown,
       "vmwNsxMMessagingDisabled": vmwNsxMMessagingDisabled,
       "vmwNsxMServiceComposer": vmwNsxMServiceComposer,
       "vmwNsxMServiceComposerPrefix": vmwNsxMServiceComposerPrefix,
       "vmwNsxMServiceComposerPolicyOutOfSync": vmwNsxMServiceComposerPolicyOutOfSync,
       "vmwNsxMServiceComposerPolicyDeleted": vmwNsxMServiceComposerPolicyDeleted,
       "vmwNsxMServiceComposerFirewallPolicyOutOfSync": vmwNsxMServiceComposerFirewallPolicyOutOfSync,
       "vmwNsxMServiceComposerNetworkPolicyOutOfSync": vmwNsxMServiceComposerNetworkPolicyOutOfSync,
       "vmwNsxMServiceComposerGuestPolicyOutOfSync": vmwNsxMServiceComposerGuestPolicyOutOfSync,
       "vmwNsxMServiceComposerOutOfSync": vmwNsxMServiceComposerOutOfSync,
       "vmwNsxMServiceComposerOutOfSyncRebootFailure": vmwNsxMServiceComposerOutOfSyncRebootFailure,
       "vmwNsxMServiceComposerOutOfSyncDraftRollback": vmwNsxMServiceComposerOutOfSyncDraftRollback,
       "vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure": vmwNsxMServiceComposerOutOfSyncSectionDeletionFailure,
       "vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure": vmwNsxMServiceComposerOutOfSyncPrecedenceChangeFailure,
       "vmwNsxMServiceComposerOutOfSyncDraftSettingFailure": vmwNsxMServiceComposerOutOfSyncDraftSettingFailure,
       "vmwNsxMSvmOperations": vmwNsxMSvmOperations,
       "vmwNsxMSvmOperationsPrefix": vmwNsxMSvmOperationsPrefix,
       "vmwNsxMInconsistentSvmAlarm": vmwNsxMInconsistentSvmAlarm,
       "vmwNsxMSvmRestartAlarm": vmwNsxMSvmRestartAlarm,
       "vmwNsxMSvmAgentUnavailable": vmwNsxMSvmAgentUnavailable,
       "vmwNsxMTranslation": vmwNsxMTranslation,
       "vmwNsxMTranslationPrefix": vmwNsxMTranslationPrefix,
       "vmwNsxMVmAddedToSg": vmwNsxMVmAddedToSg,
       "vmwNsxMVmRemovedFromSg": vmwNsxMVmRemovedFromSg,
       "vmwNsxMUniversalSync": vmwNsxMUniversalSync,
       "vmwNsxMUniversalSyncPrefix": vmwNsxMUniversalSyncPrefix,
       "vmwNsxMFullUniversalSyncFailed": vmwNsxMFullUniversalSyncFailed,
       "vmwNsxMSecondaryDown": vmwNsxMSecondaryDown,
       "vmwNsxMUniversalSyncFailedForEntity": vmwNsxMUniversalSyncFailedForEntity,
       "vmwNsxMAsyncRest": vmwNsxMAsyncRest,
       "vmwNsxMAsyncRestPrefix": vmwNsxMAsyncRestPrefix,
       "vmwNsxMServerUp": vmwNsxMServerUp,
       "vmwNsxMExtensionRegistration": vmwNsxMExtensionRegistration,
       "vmwNsxMExtensionRegistrationPrefix": vmwNsxMExtensionRegistrationPrefix,
       "vmwNsxMExtensionRegistered": vmwNsxMExtensionRegistered,
       "vmwNsxMExtensionUpdated": vmwNsxMExtensionUpdated,
       "vmwNsxMDlp": vmwNsxMDlp,
       "vmwNsxMDlpPrefix": vmwNsxMDlpPrefix,
       "vmwNsxMDataSecScanStarted": vmwNsxMDataSecScanStarted,
       "vmwNsxMDataSecScanEnded": vmwNsxMDataSecScanEnded,
       "vmwNsxMSamSystem": vmwNsxMSamSystem,
       "vmwNsxMSamSystemPrefix": vmwNsxMSamSystemPrefix,
       "vmwNsxMSamDataCollectionEnabled": vmwNsxMSamDataCollectionEnabled,
       "vmwNsxMSamDataCollectionDisabled": vmwNsxMSamDataCollectionDisabled,
       "vmwNsxMSamDataStoppedFlowing": vmwNsxMSamDataStoppedFlowing,
       "vmwNsxMSamDataResumedFlowing": vmwNsxMSamDataResumedFlowing,
       "vmwNsxMUsvm": vmwNsxMUsvm,
       "vmwNsxMUsvmPrefix": vmwNsxMUsvmPrefix,
       "vmwNsxMUsvmHeartbeatStopped": vmwNsxMUsvmHeartbeatStopped,
       "vmwNsxMUsvmHeartbeatResumed": vmwNsxMUsvmHeartbeatResumed,
       "vmwNsxMUsvmReceivedHello": vmwNsxMUsvmReceivedHello,
       "vmwNsxMVsmCore": vmwNsxMVsmCore,
       "vmwNsxMVsmCorePrefix": vmwNsxMVsmCorePrefix,
       "vmwNsxMUpgradeSuccess": vmwNsxMUpgradeSuccess,
       "vmwNsxMRestoreSuccess": vmwNsxMRestoreSuccess,
       "vmwNsxMDuplicateIp": vmwNsxMDuplicateIp,
       "vmwNsxMVxlan": vmwNsxMVxlan,
       "vmwNsxMVxlanPrefix": vmwNsxMVxlanPrefix,
       "vmwNsxMVxlanLogicalSwitchImproperlyCnfg": vmwNsxMVxlanLogicalSwitchImproperlyCnfg,
       "vmwNsxMVxlanLogicalSwitchProperlyCnfg": vmwNsxMVxlanLogicalSwitchProperlyCnfg,
       "vmwNsxMVxlanInitFailed": vmwNsxMVxlanInitFailed,
       "vmwNsxMVxlanPortInitFailed": vmwNsxMVxlanPortInitFailed,
       "vmwNsxMVxlanInstanceDoesNotExist": vmwNsxMVxlanInstanceDoesNotExist,
       "vmwNsxMVxlanLogicalSwitchWrkngImproperly": vmwNsxMVxlanLogicalSwitchWrkngImproperly,
       "vmwNsxMVxlanTransportZoneIncorrectlyWrkng": vmwNsxMVxlanTransportZoneIncorrectlyWrkng,
       "vmwNsxMVxlanTransportZoneNotUsed": vmwNsxMVxlanTransportZoneNotUsed,
       "vmwNsxMVxlanOverlayClassMissingOnDvs": vmwNsxMVxlanOverlayClassMissingOnDvs,
       "vmwNsxMVxlanControllerRemoved": vmwNsxMVxlanControllerRemoved,
       "vmwNsxMVxlanControllerConnProblem": vmwNsxMVxlanControllerConnProblem,
       "vmwNsxMVxlanControllerInactive": vmwNsxMVxlanControllerInactive,
       "vmwNsxMVxlanControllerActive": vmwNsxMVxlanControllerActive,
       "vmwNsxMVxlanVmknicMissingOrDeleted": vmwNsxMVxlanVmknicMissingOrDeleted,
       "vmwNsxMVxlanInfo": vmwNsxMVxlanInfo,
       "vmwNsxMVxlanVmknicPortGrpMissing": vmwNsxMVxlanVmknicPortGrpMissing,
       "vmwNsxMVxlanVmknicPortGrpAppears": vmwNsxMVxlanVmknicPortGrpAppears,
       "vmwNsxMVxlanConnDown": vmwNsxMVxlanConnDown,
       "vmwNsxMBackingPortgroupMissing": vmwNsxMBackingPortgroupMissing,
       "vmwNsxMBackingPortgroupReappears": vmwNsxMBackingPortgroupReappears,
       "vmwNsxMManagedObjectIdChanged": vmwNsxMManagedObjectIdChanged,
       "vmwNsxMHighLatencyOnDisk": vmwNsxMHighLatencyOnDisk,
       "vmwNsxMHighLatencyOnDiskResolved": vmwNsxMHighLatencyOnDiskResolved,
       "vmwNsxMControllerVmPoweredOff": vmwNsxMControllerVmPoweredOff,
       "vmwNsxMControllerVmDeleted": vmwNsxMControllerVmDeleted,
       "vmwNsxMVxlanConfigNotSet": vmwNsxMVxlanConfigNotSet,
       "vmwNsxManagerMIBConformance": vmwNsxManagerMIBConformance,
       "vmwNsxManagerMIBCompliances": vmwNsxManagerMIBCompliances,
       "vmwNsxManagerMIBBasicCompliance": vmwNsxManagerMIBBasicCompliance,
       "vmwNsxManagerMIBGroups": vmwNsxManagerMIBGroups,
       "vmwNsxManagerNotificationInfoGroup1": vmwNsxManagerNotificationInfoGroup1,
       "vmwNsxManagerNotificationGroup1": vmwNsxManagerNotificationGroup1}
)
