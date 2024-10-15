# SNMP MIB module (CISCO-UNIFIED-COMPUTING-BIOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-BIOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:02 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsBiosBootDevErrorCode,
 CucsBiosBootDevGrpType,
 CucsBiosBootDevOrder,
 CucsBiosDefaultAction,
 CucsBiosSupportedAction,
 CucsBiosVfACPI10SupportVpACPI10Support,
 CucsBiosVfASPMSupportVpASPMSupport,
 CucsBiosVfAllUSBDevicesVpAllUSBDevices,
 CucsBiosVfAltitudeVpAltitude,
 CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
 CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
 CucsBiosVfBootOptionRetryVpBootOptionRetry,
 CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement,
 CucsBiosVfCPUPerformanceVpCPUPerformance,
 CucsBiosVfCPUPowerManagementVpCPUPowerManagement,
 CucsBiosVfConsistentDeviceNameControlVpCDNControl,
 CucsBiosVfConsoleRedirectionVpBaudRate,
 CucsBiosVfConsoleRedirectionVpConsoleRedirection,
 CucsBiosVfConsoleRedirectionVpFlowControl,
 CucsBiosVfConsoleRedirectionVpLegacyOSRedirection,
 CucsBiosVfConsoleRedirectionVpPuttyKeyPad,
 CucsBiosVfConsoleRedirectionVpTerminalType,
 CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing,
 CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection,
 CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
 CucsBiosVfDirectCacheAccessVpDirectCacheAccess,
 CucsBiosVfDramRefreshRateVpDramRefreshRate,
 CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
 CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping,
 CucsBiosVfExecuteDisableBitVpExecuteDisableBit,
 CucsBiosVfFRB2TimerVpFRB2Timer,
 CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
 CucsBiosVfFrontPanelLockoutVpFrontPanelLockout,
 CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize,
 CucsBiosVfIntegratedGraphicsVpIntegratedGraphics,
 CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID,
 CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
 CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
 CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup,
 CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
 CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
 CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
 CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
 CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
 CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
 CucsBiosVfInterleaveConfigurationVpChannelInterleaving,
 CucsBiosVfInterleaveConfigurationVpMemoryInterleaving,
 CucsBiosVfInterleaveConfigurationVpRankInterleaving,
 CucsBiosVfLocalX2ApicVpLocalX2Apic,
 CucsBiosVfLvDIMMSupportVpLvDDRMode,
 CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
 CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
 CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
 CucsBiosVfMirroringModeVpMirroringMode,
 CucsBiosVfNUMAOptimizedVpNUMAOptimized,
 CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
 CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
 CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
 CucsBiosVfOnboardGraphicsVpOnboardGraphics,
 CucsBiosVfOnboardSATAControllerVpOnboardSATAController,
 CucsBiosVfOnboardSATAControllerVpSATAMode,
 CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport,
 CucsBiosVfOptionROMEnableVpState,
 CucsBiosVfOptionROMLoadVpLoad,
 CucsBiosVfPCHSATAModeVpSATAMode,
 CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
 CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
 CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
 CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
 CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
 CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
 CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
 CucsBiosVfPCISlotOptionROMEnableVpSlot10State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot1State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot2State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot3State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot4State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot5State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot6State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot7State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot8State,
 CucsBiosVfPCISlotOptionROMEnableVpSlot9State,
 CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState,
 CucsBiosVfPOSTErrorPauseVpPOSTErrorPause,
 CucsBiosVfPSTATECoordinationVpPSTATECoordination,
 CucsBiosVfPackageCStateLimitVpPackageCStateLimit,
 CucsBiosVfProcessorC1EVpProcessorC1E,
 CucsBiosVfProcessorC3ReportVpProcessorC3Report,
 CucsBiosVfProcessorC6ReportVpProcessorC6Report,
 CucsBiosVfProcessorC7ReportVpProcessorC7Report,
 CucsBiosVfProcessorCStateVpProcessorCState,
 CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
 CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology,
 CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
 CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
 CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
 CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
 CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
 CucsBiosVfQPISnoopModeVpQPISnoopMode,
 CucsBiosVfQuietBootVpQuietBoot,
 CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
 CucsBiosVfScrubPoliciesVpDemandScrub,
 CucsBiosVfScrubPoliciesVpPatrolScrub,
 CucsBiosVfSerialPortAEnableVpSerialPortAEnable,
 CucsBiosVfSparingModeVpSparingMode,
 CucsBiosVfSriovConfigVpSriov,
 CucsBiosVfTPMPendingOperationVpTPMPendingOperation,
 CucsBiosVfTPMSupportVpTPMSupport,
 CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport,
 CucsBiosVfUCSMBootModeControlVpUEFIBootMode,
 CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule,
 CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
 CucsBiosVfUSBBootConfigVpLegacyUSBSupport,
 CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable,
 CucsBiosVfUSBConfigurationVpLegacyUSBSupport,
 CucsBiosVfUSBConfigurationVpXHCIMode,
 CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
 CucsBiosVfUSBPortConfigurationVpPort6064Emulation,
 CucsBiosVfUSBPortConfigurationVpUSBPortFront,
 CucsBiosVfUSBPortConfigurationVpUSBPortInternal,
 CucsBiosVfUSBPortConfigurationVpUSBPortKVM,
 CucsBiosVfUSBPortConfigurationVpUSBPortRear,
 CucsBiosVfUSBPortConfigurationVpUSBPortSDCard,
 CucsBiosVfUSBPortConfigurationVpUSBPortVMedia,
 CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize,
 CucsBiosVfVGAPriorityVpVGAPriority,
 CucsBiosVpIntelVirtualizationTechnology,
 CucsBiosVpSelectMemoryRASConfiguration,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsBiosBootDevErrorCode",
    "CucsBiosBootDevGrpType",
    "CucsBiosBootDevOrder",
    "CucsBiosDefaultAction",
    "CucsBiosSupportedAction",
    "CucsBiosVfACPI10SupportVpACPI10Support",
    "CucsBiosVfASPMSupportVpASPMSupport",
    "CucsBiosVfAllUSBDevicesVpAllUSBDevices",
    "CucsBiosVfAltitudeVpAltitude",
    "CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR",
    "CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR",
    "CucsBiosVfBootOptionRetryVpBootOptionRetry",
    "CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement",
    "CucsBiosVfCPUPerformanceVpCPUPerformance",
    "CucsBiosVfCPUPowerManagementVpCPUPowerManagement",
    "CucsBiosVfConsistentDeviceNameControlVpCDNControl",
    "CucsBiosVfConsoleRedirectionVpBaudRate",
    "CucsBiosVfConsoleRedirectionVpConsoleRedirection",
    "CucsBiosVfConsoleRedirectionVpFlowControl",
    "CucsBiosVfConsoleRedirectionVpLegacyOSRedirection",
    "CucsBiosVfConsoleRedirectionVpPuttyKeyPad",
    "CucsBiosVfConsoleRedirectionVpTerminalType",
    "CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing",
    "CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection",
    "CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling",
    "CucsBiosVfDirectCacheAccessVpDirectCacheAccess",
    "CucsBiosVfDramRefreshRateVpDramRefreshRate",
    "CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech",
    "CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping",
    "CucsBiosVfExecuteDisableBitVpExecuteDisableBit",
    "CucsBiosVfFRB2TimerVpFRB2Timer",
    "CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride",
    "CucsBiosVfFrontPanelLockoutVpFrontPanelLockout",
    "CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize",
    "CucsBiosVfIntegratedGraphicsVpIntegratedGraphics",
    "CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID",
    "CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule",
    "CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech",
    "CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup",
    "CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech",
    "CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport",
    "CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport",
    "CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping",
    "CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport",
    "CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO",
    "CucsBiosVfInterleaveConfigurationVpChannelInterleaving",
    "CucsBiosVfInterleaveConfigurationVpMemoryInterleaving",
    "CucsBiosVfInterleaveConfigurationVpRankInterleaving",
    "CucsBiosVfLocalX2ApicVpLocalX2Apic",
    "CucsBiosVfLvDIMMSupportVpLvDDRMode",
    "CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr",
    "CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB",
    "CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB",
    "CucsBiosVfMirroringModeVpMirroringMode",
    "CucsBiosVfNUMAOptimizedVpNUMAOptimized",
    "CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy",
    "CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout",
    "CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer",
    "CucsBiosVfOnboardGraphicsVpOnboardGraphics",
    "CucsBiosVfOnboardSATAControllerVpOnboardSATAController",
    "CucsBiosVfOnboardSATAControllerVpSATAMode",
    "CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport",
    "CucsBiosVfOptionROMEnableVpState",
    "CucsBiosVfOptionROMLoadVpLoad",
    "CucsBiosVfPCHSATAModeVpSATAMode",
    "CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed",
    "CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed",
    "CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM",
    "CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM",
    "CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM",
    "CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM",
    "CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot10State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot1State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot2State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot3State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot4State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot5State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot6State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot7State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot8State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlot9State",
    "CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState",
    "CucsBiosVfPOSTErrorPauseVpPOSTErrorPause",
    "CucsBiosVfPSTATECoordinationVpPSTATECoordination",
    "CucsBiosVfPackageCStateLimitVpPackageCStateLimit",
    "CucsBiosVfProcessorC1EVpProcessorC1E",
    "CucsBiosVfProcessorC3ReportVpProcessorC3Report",
    "CucsBiosVfProcessorC6ReportVpProcessorC6Report",
    "CucsBiosVfProcessorC7ReportVpProcessorC7Report",
    "CucsBiosVfProcessorCStateVpProcessorCState",
    "CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance",
    "CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology",
    "CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher",
    "CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher",
    "CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch",
    "CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher",
    "CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect",
    "CucsBiosVfQPISnoopModeVpQPISnoopMode",
    "CucsBiosVfQuietBootVpQuietBoot",
    "CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss",
    "CucsBiosVfScrubPoliciesVpDemandScrub",
    "CucsBiosVfScrubPoliciesVpPatrolScrub",
    "CucsBiosVfSerialPortAEnableVpSerialPortAEnable",
    "CucsBiosVfSparingModeVpSparingMode",
    "CucsBiosVfSriovConfigVpSriov",
    "CucsBiosVfTPMPendingOperationVpTPMPendingOperation",
    "CucsBiosVfTPMSupportVpTPMSupport",
    "CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport",
    "CucsBiosVfUCSMBootModeControlVpUEFIBootMode",
    "CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule",
    "CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo",
    "CucsBiosVfUSBBootConfigVpLegacyUSBSupport",
    "CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable",
    "CucsBiosVfUSBConfigurationVpLegacyUSBSupport",
    "CucsBiosVfUSBConfigurationVpXHCIMode",
    "CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock",
    "CucsBiosVfUSBPortConfigurationVpPort6064Emulation",
    "CucsBiosVfUSBPortConfigurationVpUSBPortFront",
    "CucsBiosVfUSBPortConfigurationVpUSBPortInternal",
    "CucsBiosVfUSBPortConfigurationVpUSBPortKVM",
    "CucsBiosVfUSBPortConfigurationVpUSBPortRear",
    "CucsBiosVfUSBPortConfigurationVpUSBPortSDCard",
    "CucsBiosVfUSBPortConfigurationVpUSBPortVMedia",
    "CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize",
    "CucsBiosVfVGAPriorityVpVGAPriority",
    "CucsBiosVpIntelVirtualizationTechnology",
    "CucsBiosVpSelectMemoryRASConfiguration",
    "CucsPolicyPolicyOwner")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsBiosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsBiosBOTTable_Object = MibTable
cucsBiosBOTTable = _CucsBiosBOTTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cucsBiosBOTTable.setStatus("current")
_CucsBiosBOTEntry_Object = MibTableRow
cucsBiosBOTEntry = _CucsBiosBOTEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1, 1)
)
cucsBiosBOTEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosBOTInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosBOTEntry.setStatus("current")
_CucsBiosBOTInstanceId_Type = CucsManagedObjectId
_CucsBiosBOTInstanceId_Object = MibTableColumn
cucsBiosBOTInstanceId = _CucsBiosBOTInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1, 1, 1),
    _CucsBiosBOTInstanceId_Type()
)
cucsBiosBOTInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosBOTInstanceId.setStatus("current")
_CucsBiosBOTDn_Type = CucsManagedObjectDn
_CucsBiosBOTDn_Object = MibTableColumn
cucsBiosBOTDn = _CucsBiosBOTDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1, 1, 2),
    _CucsBiosBOTDn_Type()
)
cucsBiosBOTDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBOTDn.setStatus("current")
_CucsBiosBOTRn_Type = SnmpAdminString
_CucsBiosBOTRn_Object = MibTableColumn
cucsBiosBOTRn = _CucsBiosBOTRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1, 1, 3),
    _CucsBiosBOTRn_Type()
)
cucsBiosBOTRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBOTRn.setStatus("current")
_CucsBiosBOTLastUpdate_Type = DateAndTime
_CucsBiosBOTLastUpdate_Object = MibTableColumn
cucsBiosBOTLastUpdate = _CucsBiosBOTLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 1, 1, 4),
    _CucsBiosBOTLastUpdate_Type()
)
cucsBiosBOTLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBOTLastUpdate.setStatus("current")
_CucsBiosBootDevTable_Object = MibTable
cucsBiosBootDevTable = _CucsBiosBootDevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cucsBiosBootDevTable.setStatus("current")
_CucsBiosBootDevEntry_Object = MibTableRow
cucsBiosBootDevEntry = _CucsBiosBootDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1)
)
cucsBiosBootDevEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosBootDevInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosBootDevEntry.setStatus("current")
_CucsBiosBootDevInstanceId_Type = CucsManagedObjectId
_CucsBiosBootDevInstanceId_Object = MibTableColumn
cucsBiosBootDevInstanceId = _CucsBiosBootDevInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 1),
    _CucsBiosBootDevInstanceId_Type()
)
cucsBiosBootDevInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosBootDevInstanceId.setStatus("current")
_CucsBiosBootDevDn_Type = CucsManagedObjectDn
_CucsBiosBootDevDn_Object = MibTableColumn
cucsBiosBootDevDn = _CucsBiosBootDevDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 2),
    _CucsBiosBootDevDn_Type()
)
cucsBiosBootDevDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevDn.setStatus("current")
_CucsBiosBootDevRn_Type = SnmpAdminString
_CucsBiosBootDevRn_Object = MibTableColumn
cucsBiosBootDevRn = _CucsBiosBootDevRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 3),
    _CucsBiosBootDevRn_Type()
)
cucsBiosBootDevRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevRn.setStatus("current")
_CucsBiosBootDevDescr_Type = SnmpAdminString
_CucsBiosBootDevDescr_Object = MibTableColumn
cucsBiosBootDevDescr = _CucsBiosBootDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 4),
    _CucsBiosBootDevDescr_Type()
)
cucsBiosBootDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevDescr.setStatus("current")
_CucsBiosBootDevOrder_Type = CucsBiosBootDevOrder
_CucsBiosBootDevOrder_Object = MibTableColumn
cucsBiosBootDevOrder = _CucsBiosBootDevOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 5),
    _CucsBiosBootDevOrder_Type()
)
cucsBiosBootDevOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevOrder.setStatus("current")
_CucsBiosBootDevDeviceName_Type = SnmpAdminString
_CucsBiosBootDevDeviceName_Object = MibTableColumn
cucsBiosBootDevDeviceName = _CucsBiosBootDevDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 6),
    _CucsBiosBootDevDeviceName_Type()
)
cucsBiosBootDevDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevDeviceName.setStatus("current")
_CucsBiosBootDevErrValue_Type = CucsBiosBootDevErrorCode
_CucsBiosBootDevErrValue_Object = MibTableColumn
cucsBiosBootDevErrValue = _CucsBiosBootDevErrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 2, 1, 7),
    _CucsBiosBootDevErrValue_Type()
)
cucsBiosBootDevErrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevErrValue.setStatus("current")
_CucsBiosBootDevGrpTable_Object = MibTable
cucsBiosBootDevGrpTable = _CucsBiosBootDevGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpTable.setStatus("current")
_CucsBiosBootDevGrpEntry_Object = MibTableRow
cucsBiosBootDevGrpEntry = _CucsBiosBootDevGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1)
)
cucsBiosBootDevGrpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosBootDevGrpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpEntry.setStatus("current")
_CucsBiosBootDevGrpInstanceId_Type = CucsManagedObjectId
_CucsBiosBootDevGrpInstanceId_Object = MibTableColumn
cucsBiosBootDevGrpInstanceId = _CucsBiosBootDevGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 1),
    _CucsBiosBootDevGrpInstanceId_Type()
)
cucsBiosBootDevGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpInstanceId.setStatus("current")
_CucsBiosBootDevGrpDn_Type = CucsManagedObjectDn
_CucsBiosBootDevGrpDn_Object = MibTableColumn
cucsBiosBootDevGrpDn = _CucsBiosBootDevGrpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 2),
    _CucsBiosBootDevGrpDn_Type()
)
cucsBiosBootDevGrpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpDn.setStatus("current")
_CucsBiosBootDevGrpRn_Type = SnmpAdminString
_CucsBiosBootDevGrpRn_Object = MibTableColumn
cucsBiosBootDevGrpRn = _CucsBiosBootDevGrpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 3),
    _CucsBiosBootDevGrpRn_Type()
)
cucsBiosBootDevGrpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpRn.setStatus("current")
_CucsBiosBootDevGrpDescr_Type = SnmpAdminString
_CucsBiosBootDevGrpDescr_Object = MibTableColumn
cucsBiosBootDevGrpDescr = _CucsBiosBootDevGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 4),
    _CucsBiosBootDevGrpDescr_Type()
)
cucsBiosBootDevGrpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpDescr.setStatus("current")
_CucsBiosBootDevGrpOrder_Type = CucsBiosBootDevOrder
_CucsBiosBootDevGrpOrder_Object = MibTableColumn
cucsBiosBootDevGrpOrder = _CucsBiosBootDevGrpOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 5),
    _CucsBiosBootDevGrpOrder_Type()
)
cucsBiosBootDevGrpOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpOrder.setStatus("current")
_CucsBiosBootDevGrpType_Type = CucsBiosBootDevGrpType
_CucsBiosBootDevGrpType_Object = MibTableColumn
cucsBiosBootDevGrpType = _CucsBiosBootDevGrpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 6),
    _CucsBiosBootDevGrpType_Type()
)
cucsBiosBootDevGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpType.setStatus("current")
_CucsBiosBootDevGrpDeviceName_Type = SnmpAdminString
_CucsBiosBootDevGrpDeviceName_Object = MibTableColumn
cucsBiosBootDevGrpDeviceName = _CucsBiosBootDevGrpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 7),
    _CucsBiosBootDevGrpDeviceName_Type()
)
cucsBiosBootDevGrpDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpDeviceName.setStatus("current")
_CucsBiosBootDevGrpErrVal_Type = CucsBiosBootDevErrorCode
_CucsBiosBootDevGrpErrVal_Object = MibTableColumn
cucsBiosBootDevGrpErrVal = _CucsBiosBootDevGrpErrVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 3, 1, 8),
    _CucsBiosBootDevGrpErrVal_Type()
)
cucsBiosBootDevGrpErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosBootDevGrpErrVal.setStatus("current")
_CucsBiosFeatureRefTable_Object = MibTable
cucsBiosFeatureRefTable = _CucsBiosFeatureRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cucsBiosFeatureRefTable.setStatus("current")
_CucsBiosFeatureRefEntry_Object = MibTableRow
cucsBiosFeatureRefEntry = _CucsBiosFeatureRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1)
)
cucsBiosFeatureRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosFeatureRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosFeatureRefEntry.setStatus("current")
_CucsBiosFeatureRefInstanceId_Type = CucsManagedObjectId
_CucsBiosFeatureRefInstanceId_Object = MibTableColumn
cucsBiosFeatureRefInstanceId = _CucsBiosFeatureRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 1),
    _CucsBiosFeatureRefInstanceId_Type()
)
cucsBiosFeatureRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefInstanceId.setStatus("current")
_CucsBiosFeatureRefDn_Type = CucsManagedObjectDn
_CucsBiosFeatureRefDn_Object = MibTableColumn
cucsBiosFeatureRefDn = _CucsBiosFeatureRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 2),
    _CucsBiosFeatureRefDn_Type()
)
cucsBiosFeatureRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefDn.setStatus("current")
_CucsBiosFeatureRefRn_Type = SnmpAdminString
_CucsBiosFeatureRefRn_Object = MibTableColumn
cucsBiosFeatureRefRn = _CucsBiosFeatureRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 3),
    _CucsBiosFeatureRefRn_Type()
)
cucsBiosFeatureRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefRn.setStatus("current")
_CucsBiosFeatureRefIsSupported_Type = CucsBiosSupportedAction
_CucsBiosFeatureRefIsSupported_Object = MibTableColumn
cucsBiosFeatureRefIsSupported = _CucsBiosFeatureRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 4),
    _CucsBiosFeatureRefIsSupported_Type()
)
cucsBiosFeatureRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefIsSupported.setStatus("current")
_CucsBiosFeatureRefName_Type = SnmpAdminString
_CucsBiosFeatureRefName_Object = MibTableColumn
cucsBiosFeatureRefName = _CucsBiosFeatureRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 5),
    _CucsBiosFeatureRefName_Type()
)
cucsBiosFeatureRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefName.setStatus("current")
_CucsBiosFeatureRefFtrMoClassName_Type = SnmpAdminString
_CucsBiosFeatureRefFtrMoClassName_Object = MibTableColumn
cucsBiosFeatureRefFtrMoClassName = _CucsBiosFeatureRefFtrMoClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 4, 1, 6),
    _CucsBiosFeatureRefFtrMoClassName_Type()
)
cucsBiosFeatureRefFtrMoClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosFeatureRefFtrMoClassName.setStatus("current")
_CucsBiosParameterRefTable_Object = MibTable
cucsBiosParameterRefTable = _CucsBiosParameterRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cucsBiosParameterRefTable.setStatus("current")
_CucsBiosParameterRefEntry_Object = MibTableRow
cucsBiosParameterRefEntry = _CucsBiosParameterRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1)
)
cucsBiosParameterRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosParameterRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosParameterRefEntry.setStatus("current")
_CucsBiosParameterRefInstanceId_Type = CucsManagedObjectId
_CucsBiosParameterRefInstanceId_Object = MibTableColumn
cucsBiosParameterRefInstanceId = _CucsBiosParameterRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 1),
    _CucsBiosParameterRefInstanceId_Type()
)
cucsBiosParameterRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosParameterRefInstanceId.setStatus("current")
_CucsBiosParameterRefDn_Type = CucsManagedObjectDn
_CucsBiosParameterRefDn_Object = MibTableColumn
cucsBiosParameterRefDn = _CucsBiosParameterRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 2),
    _CucsBiosParameterRefDn_Type()
)
cucsBiosParameterRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosParameterRefDn.setStatus("current")
_CucsBiosParameterRefRn_Type = SnmpAdminString
_CucsBiosParameterRefRn_Object = MibTableColumn
cucsBiosParameterRefRn = _CucsBiosParameterRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 3),
    _CucsBiosParameterRefRn_Type()
)
cucsBiosParameterRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosParameterRefRn.setStatus("current")
_CucsBiosParameterRefIsSupported_Type = CucsBiosSupportedAction
_CucsBiosParameterRefIsSupported_Object = MibTableColumn
cucsBiosParameterRefIsSupported = _CucsBiosParameterRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 4),
    _CucsBiosParameterRefIsSupported_Type()
)
cucsBiosParameterRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosParameterRefIsSupported.setStatus("current")
_CucsBiosParameterRefName_Type = SnmpAdminString
_CucsBiosParameterRefName_Object = MibTableColumn
cucsBiosParameterRefName = _CucsBiosParameterRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 5),
    _CucsBiosParameterRefName_Type()
)
cucsBiosParameterRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosParameterRefName.setStatus("current")
_CucsBiosParameterRefPropertyName_Type = SnmpAdminString
_CucsBiosParameterRefPropertyName_Object = MibTableColumn
cucsBiosParameterRefPropertyName = _CucsBiosParameterRefPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 5, 1, 6),
    _CucsBiosParameterRefPropertyName_Type()
)
cucsBiosParameterRefPropertyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosParameterRefPropertyName.setStatus("current")
_CucsBiosRefTable_Object = MibTable
cucsBiosRefTable = _CucsBiosRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cucsBiosRefTable.setStatus("current")
_CucsBiosRefEntry_Object = MibTableRow
cucsBiosRefEntry = _CucsBiosRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6, 1)
)
cucsBiosRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosRefEntry.setStatus("current")
_CucsBiosRefInstanceId_Type = CucsManagedObjectId
_CucsBiosRefInstanceId_Object = MibTableColumn
cucsBiosRefInstanceId = _CucsBiosRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6, 1, 1),
    _CucsBiosRefInstanceId_Type()
)
cucsBiosRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosRefInstanceId.setStatus("current")
_CucsBiosRefDn_Type = CucsManagedObjectDn
_CucsBiosRefDn_Object = MibTableColumn
cucsBiosRefDn = _CucsBiosRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6, 1, 2),
    _CucsBiosRefDn_Type()
)
cucsBiosRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosRefDn.setStatus("current")
_CucsBiosRefRn_Type = SnmpAdminString
_CucsBiosRefRn_Object = MibTableColumn
cucsBiosRefRn = _CucsBiosRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6, 1, 3),
    _CucsBiosRefRn_Type()
)
cucsBiosRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosRefRn.setStatus("current")
_CucsBiosRefIsSupported_Type = CucsBiosSupportedAction
_CucsBiosRefIsSupported_Object = MibTableColumn
cucsBiosRefIsSupported = _CucsBiosRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 6, 1, 4),
    _CucsBiosRefIsSupported_Type()
)
cucsBiosRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosRefIsSupported.setStatus("current")
_CucsBiosSettingRefTable_Object = MibTable
cucsBiosSettingRefTable = _CucsBiosSettingRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7)
)
if mibBuilder.loadTexts:
    cucsBiosSettingRefTable.setStatus("current")
_CucsBiosSettingRefEntry_Object = MibTableRow
cucsBiosSettingRefEntry = _CucsBiosSettingRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1)
)
cucsBiosSettingRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosSettingRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosSettingRefEntry.setStatus("current")
_CucsBiosSettingRefInstanceId_Type = CucsManagedObjectId
_CucsBiosSettingRefInstanceId_Object = MibTableColumn
cucsBiosSettingRefInstanceId = _CucsBiosSettingRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 1),
    _CucsBiosSettingRefInstanceId_Type()
)
cucsBiosSettingRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosSettingRefInstanceId.setStatus("current")
_CucsBiosSettingRefDn_Type = CucsManagedObjectDn
_CucsBiosSettingRefDn_Object = MibTableColumn
cucsBiosSettingRefDn = _CucsBiosSettingRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 2),
    _CucsBiosSettingRefDn_Type()
)
cucsBiosSettingRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefDn.setStatus("current")
_CucsBiosSettingRefRn_Type = SnmpAdminString
_CucsBiosSettingRefRn_Object = MibTableColumn
cucsBiosSettingRefRn = _CucsBiosSettingRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 3),
    _CucsBiosSettingRefRn_Type()
)
cucsBiosSettingRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefRn.setStatus("current")
_CucsBiosSettingRefIsDefault_Type = CucsBiosDefaultAction
_CucsBiosSettingRefIsDefault_Object = MibTableColumn
cucsBiosSettingRefIsDefault = _CucsBiosSettingRefIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 4),
    _CucsBiosSettingRefIsDefault_Type()
)
cucsBiosSettingRefIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefIsDefault.setStatus("current")
_CucsBiosSettingRefIsSupported_Type = CucsBiosSupportedAction
_CucsBiosSettingRefIsSupported_Object = MibTableColumn
cucsBiosSettingRefIsSupported = _CucsBiosSettingRefIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 5),
    _CucsBiosSettingRefIsSupported_Type()
)
cucsBiosSettingRefIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefIsSupported.setStatus("current")
_CucsBiosSettingRefName_Type = SnmpAdminString
_CucsBiosSettingRefName_Object = MibTableColumn
cucsBiosSettingRefName = _CucsBiosSettingRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 6),
    _CucsBiosSettingRefName_Type()
)
cucsBiosSettingRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefName.setStatus("current")
_CucsBiosSettingRefConstantName_Type = SnmpAdminString
_CucsBiosSettingRefConstantName_Object = MibTableColumn
cucsBiosSettingRefConstantName = _CucsBiosSettingRefConstantName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 7, 1, 7),
    _CucsBiosSettingRefConstantName_Type()
)
cucsBiosSettingRefConstantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingRefConstantName.setStatus("current")
_CucsBiosSettingsTable_Object = MibTable
cucsBiosSettingsTable = _CucsBiosSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8)
)
if mibBuilder.loadTexts:
    cucsBiosSettingsTable.setStatus("current")
_CucsBiosSettingsEntry_Object = MibTableRow
cucsBiosSettingsEntry = _CucsBiosSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8, 1)
)
cucsBiosSettingsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosSettingsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosSettingsEntry.setStatus("current")
_CucsBiosSettingsInstanceId_Type = CucsManagedObjectId
_CucsBiosSettingsInstanceId_Object = MibTableColumn
cucsBiosSettingsInstanceId = _CucsBiosSettingsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8, 1, 1),
    _CucsBiosSettingsInstanceId_Type()
)
cucsBiosSettingsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosSettingsInstanceId.setStatus("current")
_CucsBiosSettingsDn_Type = CucsManagedObjectDn
_CucsBiosSettingsDn_Object = MibTableColumn
cucsBiosSettingsDn = _CucsBiosSettingsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8, 1, 2),
    _CucsBiosSettingsDn_Type()
)
cucsBiosSettingsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingsDn.setStatus("current")
_CucsBiosSettingsRn_Type = SnmpAdminString
_CucsBiosSettingsRn_Object = MibTableColumn
cucsBiosSettingsRn = _CucsBiosSettingsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8, 1, 3),
    _CucsBiosSettingsRn_Type()
)
cucsBiosSettingsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingsRn.setStatus("current")
_CucsBiosSettingsPropAcl_Type = Unsigned64
_CucsBiosSettingsPropAcl_Object = MibTableColumn
cucsBiosSettingsPropAcl = _CucsBiosSettingsPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 8, 1, 4),
    _CucsBiosSettingsPropAcl_Type()
)
cucsBiosSettingsPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosSettingsPropAcl.setStatus("current")
_CucsBiosUnitTable_Object = MibTable
cucsBiosUnitTable = _CucsBiosUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9)
)
if mibBuilder.loadTexts:
    cucsBiosUnitTable.setStatus("current")
_CucsBiosUnitEntry_Object = MibTableRow
cucsBiosUnitEntry = _CucsBiosUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1)
)
cucsBiosUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosUnitEntry.setStatus("current")
_CucsBiosUnitInstanceId_Type = CucsManagedObjectId
_CucsBiosUnitInstanceId_Object = MibTableColumn
cucsBiosUnitInstanceId = _CucsBiosUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 1),
    _CucsBiosUnitInstanceId_Type()
)
cucsBiosUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosUnitInstanceId.setStatus("current")
_CucsBiosUnitDn_Type = CucsManagedObjectDn
_CucsBiosUnitDn_Object = MibTableColumn
cucsBiosUnitDn = _CucsBiosUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 2),
    _CucsBiosUnitDn_Type()
)
cucsBiosUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitDn.setStatus("current")
_CucsBiosUnitRn_Type = SnmpAdminString
_CucsBiosUnitRn_Object = MibTableColumn
cucsBiosUnitRn = _CucsBiosUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 3),
    _CucsBiosUnitRn_Type()
)
cucsBiosUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitRn.setStatus("current")
_CucsBiosUnitInitSeq_Type = SnmpAdminString
_CucsBiosUnitInitSeq_Object = MibTableColumn
cucsBiosUnitInitSeq = _CucsBiosUnitInitSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 4),
    _CucsBiosUnitInitSeq_Type()
)
cucsBiosUnitInitSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitInitSeq.setStatus("current")
_CucsBiosUnitInitTs_Type = DateAndTime
_CucsBiosUnitInitTs_Object = MibTableColumn
cucsBiosUnitInitTs = _CucsBiosUnitInitTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 5),
    _CucsBiosUnitInitTs_Type()
)
cucsBiosUnitInitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitInitTs.setStatus("current")
_CucsBiosUnitModel_Type = SnmpAdminString
_CucsBiosUnitModel_Object = MibTableColumn
cucsBiosUnitModel = _CucsBiosUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 6),
    _CucsBiosUnitModel_Type()
)
cucsBiosUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitModel.setStatus("current")
_CucsBiosUnitRevision_Type = SnmpAdminString
_CucsBiosUnitRevision_Object = MibTableColumn
cucsBiosUnitRevision = _CucsBiosUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 7),
    _CucsBiosUnitRevision_Type()
)
cucsBiosUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitRevision.setStatus("current")
_CucsBiosUnitSerial_Type = SnmpAdminString
_CucsBiosUnitSerial_Object = MibTableColumn
cucsBiosUnitSerial = _CucsBiosUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 8),
    _CucsBiosUnitSerial_Type()
)
cucsBiosUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitSerial.setStatus("current")
_CucsBiosUnitVendor_Type = SnmpAdminString
_CucsBiosUnitVendor_Object = MibTableColumn
cucsBiosUnitVendor = _CucsBiosUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 9, 1, 9),
    _CucsBiosUnitVendor_Type()
)
cucsBiosUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosUnitVendor.setStatus("current")
_CucsBiosVProfileTable_Object = MibTable
cucsBiosVProfileTable = _CucsBiosVProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10)
)
if mibBuilder.loadTexts:
    cucsBiosVProfileTable.setStatus("current")
_CucsBiosVProfileEntry_Object = MibTableRow
cucsBiosVProfileEntry = _CucsBiosVProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1)
)
cucsBiosVProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVProfileEntry.setStatus("current")
_CucsBiosVProfileInstanceId_Type = CucsManagedObjectId
_CucsBiosVProfileInstanceId_Object = MibTableColumn
cucsBiosVProfileInstanceId = _CucsBiosVProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 1),
    _CucsBiosVProfileInstanceId_Type()
)
cucsBiosVProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVProfileInstanceId.setStatus("current")
_CucsBiosVProfileDn_Type = CucsManagedObjectDn
_CucsBiosVProfileDn_Object = MibTableColumn
cucsBiosVProfileDn = _CucsBiosVProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 2),
    _CucsBiosVProfileDn_Type()
)
cucsBiosVProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileDn.setStatus("current")
_CucsBiosVProfileRn_Type = SnmpAdminString
_CucsBiosVProfileRn_Object = MibTableColumn
cucsBiosVProfileRn = _CucsBiosVProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 3),
    _CucsBiosVProfileRn_Type()
)
cucsBiosVProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileRn.setStatus("current")
_CucsBiosVProfileDescr_Type = SnmpAdminString
_CucsBiosVProfileDescr_Object = MibTableColumn
cucsBiosVProfileDescr = _CucsBiosVProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 4),
    _CucsBiosVProfileDescr_Type()
)
cucsBiosVProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileDescr.setStatus("current")
_CucsBiosVProfileIntId_Type = SnmpAdminString
_CucsBiosVProfileIntId_Object = MibTableColumn
cucsBiosVProfileIntId = _CucsBiosVProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 5),
    _CucsBiosVProfileIntId_Type()
)
cucsBiosVProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileIntId.setStatus("current")
_CucsBiosVProfileName_Type = SnmpAdminString
_CucsBiosVProfileName_Object = MibTableColumn
cucsBiosVProfileName = _CucsBiosVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 6),
    _CucsBiosVProfileName_Type()
)
cucsBiosVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileName.setStatus("current")
_CucsBiosVProfileRebootOnUpdate_Type = TruthValue
_CucsBiosVProfileRebootOnUpdate_Object = MibTableColumn
cucsBiosVProfileRebootOnUpdate = _CucsBiosVProfileRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 7),
    _CucsBiosVProfileRebootOnUpdate_Type()
)
cucsBiosVProfileRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfileRebootOnUpdate.setStatus("current")
_CucsBiosVProfilePolicyLevel_Type = Gauge32
_CucsBiosVProfilePolicyLevel_Object = MibTableColumn
cucsBiosVProfilePolicyLevel = _CucsBiosVProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 8),
    _CucsBiosVProfilePolicyLevel_Type()
)
cucsBiosVProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfilePolicyLevel.setStatus("current")
_CucsBiosVProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsBiosVProfilePolicyOwner_Object = MibTableColumn
cucsBiosVProfilePolicyOwner = _CucsBiosVProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 10, 1, 9),
    _CucsBiosVProfilePolicyOwner_Type()
)
cucsBiosVProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVProfilePolicyOwner.setStatus("current")
_CucsBiosVfConsoleRedirectionTable_Object = MibTable
cucsBiosVfConsoleRedirectionTable = _CucsBiosVfConsoleRedirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11)
)
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionTable.setStatus("current")
_CucsBiosVfConsoleRedirectionEntry_Object = MibTableRow
cucsBiosVfConsoleRedirectionEntry = _CucsBiosVfConsoleRedirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1)
)
cucsBiosVfConsoleRedirectionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfConsoleRedirectionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionEntry.setStatus("current")
_CucsBiosVfConsoleRedirectionInstanceId_Type = CucsManagedObjectId
_CucsBiosVfConsoleRedirectionInstanceId_Object = MibTableColumn
cucsBiosVfConsoleRedirectionInstanceId = _CucsBiosVfConsoleRedirectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 1),
    _CucsBiosVfConsoleRedirectionInstanceId_Type()
)
cucsBiosVfConsoleRedirectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionInstanceId.setStatus("current")
_CucsBiosVfConsoleRedirectionDn_Type = CucsManagedObjectDn
_CucsBiosVfConsoleRedirectionDn_Object = MibTableColumn
cucsBiosVfConsoleRedirectionDn = _CucsBiosVfConsoleRedirectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 2),
    _CucsBiosVfConsoleRedirectionDn_Type()
)
cucsBiosVfConsoleRedirectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionDn.setStatus("current")
_CucsBiosVfConsoleRedirectionRn_Type = SnmpAdminString
_CucsBiosVfConsoleRedirectionRn_Object = MibTableColumn
cucsBiosVfConsoleRedirectionRn = _CucsBiosVfConsoleRedirectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 3),
    _CucsBiosVfConsoleRedirectionRn_Type()
)
cucsBiosVfConsoleRedirectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionRn.setStatus("current")
_CucsBiosVfConsoleRedirectionVpBaudRate_Type = CucsBiosVfConsoleRedirectionVpBaudRate
_CucsBiosVfConsoleRedirectionVpBaudRate_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpBaudRate = _CucsBiosVfConsoleRedirectionVpBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 4),
    _CucsBiosVfConsoleRedirectionVpBaudRate_Type()
)
cucsBiosVfConsoleRedirectionVpBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpBaudRate.setStatus("current")
_CucsBiosVfConsoleRedirectionVpConsoleRedirection_Type = CucsBiosVfConsoleRedirectionVpConsoleRedirection
_CucsBiosVfConsoleRedirectionVpConsoleRedirection_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpConsoleRedirection = _CucsBiosVfConsoleRedirectionVpConsoleRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 5),
    _CucsBiosVfConsoleRedirectionVpConsoleRedirection_Type()
)
cucsBiosVfConsoleRedirectionVpConsoleRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpConsoleRedirection.setStatus("current")
_CucsBiosVfConsoleRedirectionVpFlowControl_Type = CucsBiosVfConsoleRedirectionVpFlowControl
_CucsBiosVfConsoleRedirectionVpFlowControl_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpFlowControl = _CucsBiosVfConsoleRedirectionVpFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 6),
    _CucsBiosVfConsoleRedirectionVpFlowControl_Type()
)
cucsBiosVfConsoleRedirectionVpFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpFlowControl.setStatus("current")
_CucsBiosVfConsoleRedirectionVpLegacyOSRedirection_Type = CucsBiosVfConsoleRedirectionVpLegacyOSRedirection
_CucsBiosVfConsoleRedirectionVpLegacyOSRedirection_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpLegacyOSRedirection = _CucsBiosVfConsoleRedirectionVpLegacyOSRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 7),
    _CucsBiosVfConsoleRedirectionVpLegacyOSRedirection_Type()
)
cucsBiosVfConsoleRedirectionVpLegacyOSRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpLegacyOSRedirection.setStatus("current")
_CucsBiosVfConsoleRedirectionVpTerminalType_Type = CucsBiosVfConsoleRedirectionVpTerminalType
_CucsBiosVfConsoleRedirectionVpTerminalType_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpTerminalType = _CucsBiosVfConsoleRedirectionVpTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 8),
    _CucsBiosVfConsoleRedirectionVpTerminalType_Type()
)
cucsBiosVfConsoleRedirectionVpTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpTerminalType.setStatus("current")
_CucsBiosVfConsoleRedirectionVpPuttyKeyPad_Type = CucsBiosVfConsoleRedirectionVpPuttyKeyPad
_CucsBiosVfConsoleRedirectionVpPuttyKeyPad_Object = MibTableColumn
cucsBiosVfConsoleRedirectionVpPuttyKeyPad = _CucsBiosVfConsoleRedirectionVpPuttyKeyPad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 9),
    _CucsBiosVfConsoleRedirectionVpPuttyKeyPad_Type()
)
cucsBiosVfConsoleRedirectionVpPuttyKeyPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionVpPuttyKeyPad.setStatus("current")
_CucsBiosVfConsoleRedirectionPropAcl_Type = Unsigned64
_CucsBiosVfConsoleRedirectionPropAcl_Object = MibTableColumn
cucsBiosVfConsoleRedirectionPropAcl = _CucsBiosVfConsoleRedirectionPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 10),
    _CucsBiosVfConsoleRedirectionPropAcl_Type()
)
cucsBiosVfConsoleRedirectionPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionPropAcl.setStatus("current")
_CucsBiosVfConsoleRedirectionSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfConsoleRedirectionSupportedByDefault_Object = MibTableColumn
cucsBiosVfConsoleRedirectionSupportedByDefault = _CucsBiosVfConsoleRedirectionSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 11, 1, 11),
    _CucsBiosVfConsoleRedirectionSupportedByDefault_Type()
)
cucsBiosVfConsoleRedirectionSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsoleRedirectionSupportedByDefault.setStatus("current")
_CucsBiosVfOptionROMLoadTable_Object = MibTable
cucsBiosVfOptionROMLoadTable = _CucsBiosVfOptionROMLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12)
)
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadTable.setStatus("current")
_CucsBiosVfOptionROMLoadEntry_Object = MibTableRow
cucsBiosVfOptionROMLoadEntry = _CucsBiosVfOptionROMLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1)
)
cucsBiosVfOptionROMLoadEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOptionROMLoadInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadEntry.setStatus("current")
_CucsBiosVfOptionROMLoadInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOptionROMLoadInstanceId_Object = MibTableColumn
cucsBiosVfOptionROMLoadInstanceId = _CucsBiosVfOptionROMLoadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 1),
    _CucsBiosVfOptionROMLoadInstanceId_Type()
)
cucsBiosVfOptionROMLoadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadInstanceId.setStatus("current")
_CucsBiosVfOptionROMLoadDn_Type = CucsManagedObjectDn
_CucsBiosVfOptionROMLoadDn_Object = MibTableColumn
cucsBiosVfOptionROMLoadDn = _CucsBiosVfOptionROMLoadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 2),
    _CucsBiosVfOptionROMLoadDn_Type()
)
cucsBiosVfOptionROMLoadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadDn.setStatus("current")
_CucsBiosVfOptionROMLoadRn_Type = SnmpAdminString
_CucsBiosVfOptionROMLoadRn_Object = MibTableColumn
cucsBiosVfOptionROMLoadRn = _CucsBiosVfOptionROMLoadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 3),
    _CucsBiosVfOptionROMLoadRn_Type()
)
cucsBiosVfOptionROMLoadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadRn.setStatus("current")
_CucsBiosVfOptionROMLoadVpLoad_Type = CucsBiosVfOptionROMLoadVpLoad
_CucsBiosVfOptionROMLoadVpLoad_Object = MibTableColumn
cucsBiosVfOptionROMLoadVpLoad = _CucsBiosVfOptionROMLoadVpLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 4),
    _CucsBiosVfOptionROMLoadVpLoad_Type()
)
cucsBiosVfOptionROMLoadVpLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadVpLoad.setStatus("current")
_CucsBiosVfOptionROMLoadPropAcl_Type = Unsigned64
_CucsBiosVfOptionROMLoadPropAcl_Object = MibTableColumn
cucsBiosVfOptionROMLoadPropAcl = _CucsBiosVfOptionROMLoadPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 5),
    _CucsBiosVfOptionROMLoadPropAcl_Type()
)
cucsBiosVfOptionROMLoadPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadPropAcl.setStatus("current")
_CucsBiosVfOptionROMLoadSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOptionROMLoadSupportedByDefault_Object = MibTableColumn
cucsBiosVfOptionROMLoadSupportedByDefault = _CucsBiosVfOptionROMLoadSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 12, 1, 6),
    _CucsBiosVfOptionROMLoadSupportedByDefault_Type()
)
cucsBiosVfOptionROMLoadSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMLoadSupportedByDefault.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechTable_Object = MibTable
cucsBiosVfEnhancedIntelSpeedStepTechTable = _CucsBiosVfEnhancedIntelSpeedStepTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13)
)
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechTable.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechEntry_Object = MibTableRow
cucsBiosVfEnhancedIntelSpeedStepTechEntry = _CucsBiosVfEnhancedIntelSpeedStepTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1)
)
cucsBiosVfEnhancedIntelSpeedStepTechEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfEnhancedIntelSpeedStepTechInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechEntry.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechInstanceId_Type = CucsManagedObjectId
_CucsBiosVfEnhancedIntelSpeedStepTechInstanceId_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechInstanceId = _CucsBiosVfEnhancedIntelSpeedStepTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 1),
    _CucsBiosVfEnhancedIntelSpeedStepTechInstanceId_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechInstanceId.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechDn_Type = CucsManagedObjectDn
_CucsBiosVfEnhancedIntelSpeedStepTechDn_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechDn = _CucsBiosVfEnhancedIntelSpeedStepTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 2),
    _CucsBiosVfEnhancedIntelSpeedStepTechDn_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechDn.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechRn_Type = SnmpAdminString
_CucsBiosVfEnhancedIntelSpeedStepTechRn_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechRn = _CucsBiosVfEnhancedIntelSpeedStepTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 3),
    _CucsBiosVfEnhancedIntelSpeedStepTechRn_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechRn.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type = CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech
_CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech = _CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 4),
    _CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechPropAcl_Type = Unsigned64
_CucsBiosVfEnhancedIntelSpeedStepTechPropAcl_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechPropAcl = _CucsBiosVfEnhancedIntelSpeedStepTechPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 5),
    _CucsBiosVfEnhancedIntelSpeedStepTechPropAcl_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechPropAcl.setStatus("current")
_CucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Object = MibTableColumn
cucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault = _CucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 13, 1, 6),
    _CucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault_Type()
)
cucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault.setStatus("current")
_CucsBiosVfFrontPanelLockoutTable_Object = MibTable
cucsBiosVfFrontPanelLockoutTable = _CucsBiosVfFrontPanelLockoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14)
)
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutTable.setStatus("current")
_CucsBiosVfFrontPanelLockoutEntry_Object = MibTableRow
cucsBiosVfFrontPanelLockoutEntry = _CucsBiosVfFrontPanelLockoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1)
)
cucsBiosVfFrontPanelLockoutEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfFrontPanelLockoutInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutEntry.setStatus("current")
_CucsBiosVfFrontPanelLockoutInstanceId_Type = CucsManagedObjectId
_CucsBiosVfFrontPanelLockoutInstanceId_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutInstanceId = _CucsBiosVfFrontPanelLockoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 1),
    _CucsBiosVfFrontPanelLockoutInstanceId_Type()
)
cucsBiosVfFrontPanelLockoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutInstanceId.setStatus("current")
_CucsBiosVfFrontPanelLockoutDn_Type = CucsManagedObjectDn
_CucsBiosVfFrontPanelLockoutDn_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutDn = _CucsBiosVfFrontPanelLockoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 2),
    _CucsBiosVfFrontPanelLockoutDn_Type()
)
cucsBiosVfFrontPanelLockoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutDn.setStatus("current")
_CucsBiosVfFrontPanelLockoutRn_Type = SnmpAdminString
_CucsBiosVfFrontPanelLockoutRn_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutRn = _CucsBiosVfFrontPanelLockoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 3),
    _CucsBiosVfFrontPanelLockoutRn_Type()
)
cucsBiosVfFrontPanelLockoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutRn.setStatus("current")
_CucsBiosVfFrontPanelLockoutVpFrontPanelLockout_Type = CucsBiosVfFrontPanelLockoutVpFrontPanelLockout
_CucsBiosVfFrontPanelLockoutVpFrontPanelLockout_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutVpFrontPanelLockout = _CucsBiosVfFrontPanelLockoutVpFrontPanelLockout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 4),
    _CucsBiosVfFrontPanelLockoutVpFrontPanelLockout_Type()
)
cucsBiosVfFrontPanelLockoutVpFrontPanelLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutVpFrontPanelLockout.setStatus("current")
_CucsBiosVfFrontPanelLockoutPropAcl_Type = Unsigned64
_CucsBiosVfFrontPanelLockoutPropAcl_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutPropAcl = _CucsBiosVfFrontPanelLockoutPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 5),
    _CucsBiosVfFrontPanelLockoutPropAcl_Type()
)
cucsBiosVfFrontPanelLockoutPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutPropAcl.setStatus("current")
_CucsBiosVfFrontPanelLockoutSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfFrontPanelLockoutSupportedByDefault_Object = MibTableColumn
cucsBiosVfFrontPanelLockoutSupportedByDefault = _CucsBiosVfFrontPanelLockoutSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 14, 1, 6),
    _CucsBiosVfFrontPanelLockoutSupportedByDefault_Type()
)
cucsBiosVfFrontPanelLockoutSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrontPanelLockoutSupportedByDefault.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechTable_Object = MibTable
cucsBiosVfIntelHyperThreadingTechTable = _CucsBiosVfIntelHyperThreadingTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechTable.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechEntry_Object = MibTableRow
cucsBiosVfIntelHyperThreadingTechEntry = _CucsBiosVfIntelHyperThreadingTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1)
)
cucsBiosVfIntelHyperThreadingTechEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelHyperThreadingTechInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechEntry.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelHyperThreadingTechInstanceId_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechInstanceId = _CucsBiosVfIntelHyperThreadingTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 1),
    _CucsBiosVfIntelHyperThreadingTechInstanceId_Type()
)
cucsBiosVfIntelHyperThreadingTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechInstanceId.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechDn_Type = CucsManagedObjectDn
_CucsBiosVfIntelHyperThreadingTechDn_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechDn = _CucsBiosVfIntelHyperThreadingTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 2),
    _CucsBiosVfIntelHyperThreadingTechDn_Type()
)
cucsBiosVfIntelHyperThreadingTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechDn.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechRn_Type = SnmpAdminString
_CucsBiosVfIntelHyperThreadingTechRn_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechRn = _CucsBiosVfIntelHyperThreadingTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 3),
    _CucsBiosVfIntelHyperThreadingTechRn_Type()
)
cucsBiosVfIntelHyperThreadingTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechRn.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type = CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech
_CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech = _CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 4),
    _CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech_Type()
)
cucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechPropAcl_Type = Unsigned64
_CucsBiosVfIntelHyperThreadingTechPropAcl_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechPropAcl = _CucsBiosVfIntelHyperThreadingTechPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 5),
    _CucsBiosVfIntelHyperThreadingTechPropAcl_Type()
)
cucsBiosVfIntelHyperThreadingTechPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechPropAcl.setStatus("current")
_CucsBiosVfIntelHyperThreadingTechSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelHyperThreadingTechSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelHyperThreadingTechSupportedByDefault = _CucsBiosVfIntelHyperThreadingTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 15, 1, 6),
    _CucsBiosVfIntelHyperThreadingTechSupportedByDefault_Type()
)
cucsBiosVfIntelHyperThreadingTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelHyperThreadingTechSupportedByDefault.setStatus("current")
_CucsBiosVfIntelTurboBoostTechTable_Object = MibTable
cucsBiosVfIntelTurboBoostTechTable = _CucsBiosVfIntelTurboBoostTechTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechTable.setStatus("current")
_CucsBiosVfIntelTurboBoostTechEntry_Object = MibTableRow
cucsBiosVfIntelTurboBoostTechEntry = _CucsBiosVfIntelTurboBoostTechEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1)
)
cucsBiosVfIntelTurboBoostTechEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelTurboBoostTechInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechEntry.setStatus("current")
_CucsBiosVfIntelTurboBoostTechInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelTurboBoostTechInstanceId_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechInstanceId = _CucsBiosVfIntelTurboBoostTechInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 1),
    _CucsBiosVfIntelTurboBoostTechInstanceId_Type()
)
cucsBiosVfIntelTurboBoostTechInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechInstanceId.setStatus("current")
_CucsBiosVfIntelTurboBoostTechDn_Type = CucsManagedObjectDn
_CucsBiosVfIntelTurboBoostTechDn_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechDn = _CucsBiosVfIntelTurboBoostTechDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 2),
    _CucsBiosVfIntelTurboBoostTechDn_Type()
)
cucsBiosVfIntelTurboBoostTechDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechDn.setStatus("current")
_CucsBiosVfIntelTurboBoostTechRn_Type = SnmpAdminString
_CucsBiosVfIntelTurboBoostTechRn_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechRn = _CucsBiosVfIntelTurboBoostTechRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 3),
    _CucsBiosVfIntelTurboBoostTechRn_Type()
)
cucsBiosVfIntelTurboBoostTechRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechRn.setStatus("current")
_CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type = CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech
_CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech = _CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 4),
    _CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech_Type()
)
cucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech.setStatus("current")
_CucsBiosVfIntelTurboBoostTechPropAcl_Type = Unsigned64
_CucsBiosVfIntelTurboBoostTechPropAcl_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechPropAcl = _CucsBiosVfIntelTurboBoostTechPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 5),
    _CucsBiosVfIntelTurboBoostTechPropAcl_Type()
)
cucsBiosVfIntelTurboBoostTechPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechPropAcl.setStatus("current")
_CucsBiosVfIntelTurboBoostTechSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelTurboBoostTechSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelTurboBoostTechSupportedByDefault = _CucsBiosVfIntelTurboBoostTechSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 16, 1, 6),
    _CucsBiosVfIntelTurboBoostTechSupportedByDefault_Type()
)
cucsBiosVfIntelTurboBoostTechSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTurboBoostTechSupportedByDefault.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOTable_Object = MibTable
cucsBiosVfIntelVTForDirectedIOTable = _CucsBiosVfIntelVTForDirectedIOTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOTable.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOEntry_Object = MibTableRow
cucsBiosVfIntelVTForDirectedIOEntry = _CucsBiosVfIntelVTForDirectedIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1)
)
cucsBiosVfIntelVTForDirectedIOEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelVTForDirectedIOInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOEntry.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelVTForDirectedIOInstanceId_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOInstanceId = _CucsBiosVfIntelVTForDirectedIOInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 1),
    _CucsBiosVfIntelVTForDirectedIOInstanceId_Type()
)
cucsBiosVfIntelVTForDirectedIOInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOInstanceId.setStatus("current")
_CucsBiosVfIntelVTForDirectedIODn_Type = CucsManagedObjectDn
_CucsBiosVfIntelVTForDirectedIODn_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIODn = _CucsBiosVfIntelVTForDirectedIODn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 2),
    _CucsBiosVfIntelVTForDirectedIODn_Type()
)
cucsBiosVfIntelVTForDirectedIODn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIODn.setStatus("current")
_CucsBiosVfIntelVTForDirectedIORn_Type = SnmpAdminString
_CucsBiosVfIntelVTForDirectedIORn_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIORn = _CucsBiosVfIntelVTForDirectedIORn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 3),
    _CucsBiosVfIntelVTForDirectedIORn_Type()
)
cucsBiosVfIntelVTForDirectedIORn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIORn.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type = CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport = _CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 4),
    _CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport_Type()
)
cucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type = CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport = _CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 5),
    _CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport_Type()
)
cucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type = CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping = _CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 6),
    _CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping_Type()
)
cucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type = CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport
_CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport = _CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 7),
    _CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport_Type()
)
cucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type = CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO
_CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO = _CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 8),
    _CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO_Type()
)
cucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOPropAcl_Type = Unsigned64
_CucsBiosVfIntelVTForDirectedIOPropAcl_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOPropAcl = _CucsBiosVfIntelVTForDirectedIOPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 9),
    _CucsBiosVfIntelVTForDirectedIOPropAcl_Type()
)
cucsBiosVfIntelVTForDirectedIOPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOPropAcl.setStatus("current")
_CucsBiosVfIntelVTForDirectedIOSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelVTForDirectedIOSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelVTForDirectedIOSupportedByDefault = _CucsBiosVfIntelVTForDirectedIOSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 17, 1, 10),
    _CucsBiosVfIntelVTForDirectedIOSupportedByDefault_Type()
)
cucsBiosVfIntelVTForDirectedIOSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVTForDirectedIOSupportedByDefault.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyTable_Object = MibTable
cucsBiosVfIntelVirtualizationTechnologyTable = _CucsBiosVfIntelVirtualizationTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyTable.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyEntry_Object = MibTableRow
cucsBiosVfIntelVirtualizationTechnologyEntry = _CucsBiosVfIntelVirtualizationTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1)
)
cucsBiosVfIntelVirtualizationTechnologyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelVirtualizationTechnologyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyEntry.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelVirtualizationTechnologyInstanceId_Object = MibTableColumn
cucsBiosVfIntelVirtualizationTechnologyInstanceId = _CucsBiosVfIntelVirtualizationTechnologyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 1),
    _CucsBiosVfIntelVirtualizationTechnologyInstanceId_Type()
)
cucsBiosVfIntelVirtualizationTechnologyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyInstanceId.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyDn_Type = CucsManagedObjectDn
_CucsBiosVfIntelVirtualizationTechnologyDn_Object = MibTableColumn
cucsBiosVfIntelVirtualizationTechnologyDn = _CucsBiosVfIntelVirtualizationTechnologyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 2),
    _CucsBiosVfIntelVirtualizationTechnologyDn_Type()
)
cucsBiosVfIntelVirtualizationTechnologyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyDn.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyRn_Type = SnmpAdminString
_CucsBiosVfIntelVirtualizationTechnologyRn_Object = MibTableColumn
cucsBiosVfIntelVirtualizationTechnologyRn = _CucsBiosVfIntelVirtualizationTechnologyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 3),
    _CucsBiosVfIntelVirtualizationTechnologyRn_Type()
)
cucsBiosVfIntelVirtualizationTechnologyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyRn.setStatus("current")
_CucsBiosVpIntelVirtualizationTechnology_Type = CucsBiosVpIntelVirtualizationTechnology
_CucsBiosVpIntelVirtualizationTechnology_Object = MibTableColumn
cucsBiosVpIntelVirtualizationTechnology = _CucsBiosVpIntelVirtualizationTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 4),
    _CucsBiosVpIntelVirtualizationTechnology_Type()
)
cucsBiosVpIntelVirtualizationTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVpIntelVirtualizationTechnology.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologyPropAcl_Type = Unsigned64
_CucsBiosVfIntelVirtualizationTechnologyPropAcl_Object = MibTableColumn
cucsBiosVfIntelVirtualizationTechnologyPropAcl = _CucsBiosVfIntelVirtualizationTechnologyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 5),
    _CucsBiosVfIntelVirtualizationTechnologyPropAcl_Type()
)
cucsBiosVfIntelVirtualizationTechnologyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologyPropAcl.setStatus("current")
_CucsBiosVfIntelVirtualizationTechnologySupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelVirtualizationTechnologySupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelVirtualizationTechnologySupportedByDefault = _CucsBiosVfIntelVirtualizationTechnologySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 18, 1, 6),
    _CucsBiosVfIntelVirtualizationTechnologySupportedByDefault_Type()
)
cucsBiosVfIntelVirtualizationTechnologySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelVirtualizationTechnologySupportedByDefault.setStatus("current")
_CucsBiosVfLvDIMMSupportTable_Object = MibTable
cucsBiosVfLvDIMMSupportTable = _CucsBiosVfLvDIMMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19)
)
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportTable.setStatus("current")
_CucsBiosVfLvDIMMSupportEntry_Object = MibTableRow
cucsBiosVfLvDIMMSupportEntry = _CucsBiosVfLvDIMMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1)
)
cucsBiosVfLvDIMMSupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfLvDIMMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportEntry.setStatus("current")
_CucsBiosVfLvDIMMSupportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfLvDIMMSupportInstanceId_Object = MibTableColumn
cucsBiosVfLvDIMMSupportInstanceId = _CucsBiosVfLvDIMMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 1),
    _CucsBiosVfLvDIMMSupportInstanceId_Type()
)
cucsBiosVfLvDIMMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportInstanceId.setStatus("current")
_CucsBiosVfLvDIMMSupportDn_Type = CucsManagedObjectDn
_CucsBiosVfLvDIMMSupportDn_Object = MibTableColumn
cucsBiosVfLvDIMMSupportDn = _CucsBiosVfLvDIMMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 2),
    _CucsBiosVfLvDIMMSupportDn_Type()
)
cucsBiosVfLvDIMMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportDn.setStatus("current")
_CucsBiosVfLvDIMMSupportRn_Type = SnmpAdminString
_CucsBiosVfLvDIMMSupportRn_Object = MibTableColumn
cucsBiosVfLvDIMMSupportRn = _CucsBiosVfLvDIMMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 3),
    _CucsBiosVfLvDIMMSupportRn_Type()
)
cucsBiosVfLvDIMMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportRn.setStatus("current")
_CucsBiosVfLvDIMMSupportVpLvDDRMode_Type = CucsBiosVfLvDIMMSupportVpLvDDRMode
_CucsBiosVfLvDIMMSupportVpLvDDRMode_Object = MibTableColumn
cucsBiosVfLvDIMMSupportVpLvDDRMode = _CucsBiosVfLvDIMMSupportVpLvDDRMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 4),
    _CucsBiosVfLvDIMMSupportVpLvDDRMode_Type()
)
cucsBiosVfLvDIMMSupportVpLvDDRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportVpLvDDRMode.setStatus("current")
_CucsBiosVfLvDIMMSupportPropAcl_Type = Unsigned64
_CucsBiosVfLvDIMMSupportPropAcl_Object = MibTableColumn
cucsBiosVfLvDIMMSupportPropAcl = _CucsBiosVfLvDIMMSupportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 5),
    _CucsBiosVfLvDIMMSupportPropAcl_Type()
)
cucsBiosVfLvDIMMSupportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportPropAcl.setStatus("current")
_CucsBiosVfLvDIMMSupportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfLvDIMMSupportSupportedByDefault_Object = MibTableColumn
cucsBiosVfLvDIMMSupportSupportedByDefault = _CucsBiosVfLvDIMMSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 19, 1, 6),
    _CucsBiosVfLvDIMMSupportSupportedByDefault_Type()
)
cucsBiosVfLvDIMMSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLvDIMMSupportSupportedByDefault.setStatus("current")
_CucsBiosVfMirroringModeTable_Object = MibTable
cucsBiosVfMirroringModeTable = _CucsBiosVfMirroringModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20)
)
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeTable.setStatus("current")
_CucsBiosVfMirroringModeEntry_Object = MibTableRow
cucsBiosVfMirroringModeEntry = _CucsBiosVfMirroringModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1)
)
cucsBiosVfMirroringModeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfMirroringModeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeEntry.setStatus("current")
_CucsBiosVfMirroringModeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfMirroringModeInstanceId_Object = MibTableColumn
cucsBiosVfMirroringModeInstanceId = _CucsBiosVfMirroringModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 1),
    _CucsBiosVfMirroringModeInstanceId_Type()
)
cucsBiosVfMirroringModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeInstanceId.setStatus("current")
_CucsBiosVfMirroringModeDn_Type = CucsManagedObjectDn
_CucsBiosVfMirroringModeDn_Object = MibTableColumn
cucsBiosVfMirroringModeDn = _CucsBiosVfMirroringModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 2),
    _CucsBiosVfMirroringModeDn_Type()
)
cucsBiosVfMirroringModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeDn.setStatus("current")
_CucsBiosVfMirroringModeRn_Type = SnmpAdminString
_CucsBiosVfMirroringModeRn_Object = MibTableColumn
cucsBiosVfMirroringModeRn = _CucsBiosVfMirroringModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 3),
    _CucsBiosVfMirroringModeRn_Type()
)
cucsBiosVfMirroringModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeRn.setStatus("current")
_CucsBiosVfMirroringModeVpMirroringMode_Type = CucsBiosVfMirroringModeVpMirroringMode
_CucsBiosVfMirroringModeVpMirroringMode_Object = MibTableColumn
cucsBiosVfMirroringModeVpMirroringMode = _CucsBiosVfMirroringModeVpMirroringMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 4),
    _CucsBiosVfMirroringModeVpMirroringMode_Type()
)
cucsBiosVfMirroringModeVpMirroringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeVpMirroringMode.setStatus("current")
_CucsBiosVfMirroringModePropAcl_Type = Unsigned64
_CucsBiosVfMirroringModePropAcl_Object = MibTableColumn
cucsBiosVfMirroringModePropAcl = _CucsBiosVfMirroringModePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 5),
    _CucsBiosVfMirroringModePropAcl_Type()
)
cucsBiosVfMirroringModePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModePropAcl.setStatus("current")
_CucsBiosVfMirroringModeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfMirroringModeSupportedByDefault_Object = MibTableColumn
cucsBiosVfMirroringModeSupportedByDefault = _CucsBiosVfMirroringModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 20, 1, 6),
    _CucsBiosVfMirroringModeSupportedByDefault_Type()
)
cucsBiosVfMirroringModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMirroringModeSupportedByDefault.setStatus("current")
_CucsBiosVfNUMAOptimizedTable_Object = MibTable
cucsBiosVfNUMAOptimizedTable = _CucsBiosVfNUMAOptimizedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21)
)
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedTable.setStatus("current")
_CucsBiosVfNUMAOptimizedEntry_Object = MibTableRow
cucsBiosVfNUMAOptimizedEntry = _CucsBiosVfNUMAOptimizedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1)
)
cucsBiosVfNUMAOptimizedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfNUMAOptimizedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedEntry.setStatus("current")
_CucsBiosVfNUMAOptimizedInstanceId_Type = CucsManagedObjectId
_CucsBiosVfNUMAOptimizedInstanceId_Object = MibTableColumn
cucsBiosVfNUMAOptimizedInstanceId = _CucsBiosVfNUMAOptimizedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 1),
    _CucsBiosVfNUMAOptimizedInstanceId_Type()
)
cucsBiosVfNUMAOptimizedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedInstanceId.setStatus("current")
_CucsBiosVfNUMAOptimizedDn_Type = CucsManagedObjectDn
_CucsBiosVfNUMAOptimizedDn_Object = MibTableColumn
cucsBiosVfNUMAOptimizedDn = _CucsBiosVfNUMAOptimizedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 2),
    _CucsBiosVfNUMAOptimizedDn_Type()
)
cucsBiosVfNUMAOptimizedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedDn.setStatus("current")
_CucsBiosVfNUMAOptimizedRn_Type = SnmpAdminString
_CucsBiosVfNUMAOptimizedRn_Object = MibTableColumn
cucsBiosVfNUMAOptimizedRn = _CucsBiosVfNUMAOptimizedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 3),
    _CucsBiosVfNUMAOptimizedRn_Type()
)
cucsBiosVfNUMAOptimizedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedRn.setStatus("current")
_CucsBiosVfNUMAOptimizedVpNUMAOptimized_Type = CucsBiosVfNUMAOptimizedVpNUMAOptimized
_CucsBiosVfNUMAOptimizedVpNUMAOptimized_Object = MibTableColumn
cucsBiosVfNUMAOptimizedVpNUMAOptimized = _CucsBiosVfNUMAOptimizedVpNUMAOptimized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 4),
    _CucsBiosVfNUMAOptimizedVpNUMAOptimized_Type()
)
cucsBiosVfNUMAOptimizedVpNUMAOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedVpNUMAOptimized.setStatus("current")
_CucsBiosVfNUMAOptimizedPropAcl_Type = Unsigned64
_CucsBiosVfNUMAOptimizedPropAcl_Object = MibTableColumn
cucsBiosVfNUMAOptimizedPropAcl = _CucsBiosVfNUMAOptimizedPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 5),
    _CucsBiosVfNUMAOptimizedPropAcl_Type()
)
cucsBiosVfNUMAOptimizedPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedPropAcl.setStatus("current")
_CucsBiosVfNUMAOptimizedSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfNUMAOptimizedSupportedByDefault_Object = MibTableColumn
cucsBiosVfNUMAOptimizedSupportedByDefault = _CucsBiosVfNUMAOptimizedSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 21, 1, 6),
    _CucsBiosVfNUMAOptimizedSupportedByDefault_Type()
)
cucsBiosVfNUMAOptimizedSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfNUMAOptimizedSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorC3ReportTable_Object = MibTable
cucsBiosVfProcessorC3ReportTable = _CucsBiosVfProcessorC3ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportTable.setStatus("current")
_CucsBiosVfProcessorC3ReportEntry_Object = MibTableRow
cucsBiosVfProcessorC3ReportEntry = _CucsBiosVfProcessorC3ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1)
)
cucsBiosVfProcessorC3ReportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorC3ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportEntry.setStatus("current")
_CucsBiosVfProcessorC3ReportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorC3ReportInstanceId_Object = MibTableColumn
cucsBiosVfProcessorC3ReportInstanceId = _CucsBiosVfProcessorC3ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 1),
    _CucsBiosVfProcessorC3ReportInstanceId_Type()
)
cucsBiosVfProcessorC3ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportInstanceId.setStatus("current")
_CucsBiosVfProcessorC3ReportDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorC3ReportDn_Object = MibTableColumn
cucsBiosVfProcessorC3ReportDn = _CucsBiosVfProcessorC3ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 2),
    _CucsBiosVfProcessorC3ReportDn_Type()
)
cucsBiosVfProcessorC3ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportDn.setStatus("current")
_CucsBiosVfProcessorC3ReportRn_Type = SnmpAdminString
_CucsBiosVfProcessorC3ReportRn_Object = MibTableColumn
cucsBiosVfProcessorC3ReportRn = _CucsBiosVfProcessorC3ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 3),
    _CucsBiosVfProcessorC3ReportRn_Type()
)
cucsBiosVfProcessorC3ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportRn.setStatus("current")
_CucsBiosVfProcessorC3ReportVpProcessorC3Report_Type = CucsBiosVfProcessorC3ReportVpProcessorC3Report
_CucsBiosVfProcessorC3ReportVpProcessorC3Report_Object = MibTableColumn
cucsBiosVfProcessorC3ReportVpProcessorC3Report = _CucsBiosVfProcessorC3ReportVpProcessorC3Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 4),
    _CucsBiosVfProcessorC3ReportVpProcessorC3Report_Type()
)
cucsBiosVfProcessorC3ReportVpProcessorC3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportVpProcessorC3Report.setStatus("current")
_CucsBiosVfProcessorC3ReportPropAcl_Type = Unsigned64
_CucsBiosVfProcessorC3ReportPropAcl_Object = MibTableColumn
cucsBiosVfProcessorC3ReportPropAcl = _CucsBiosVfProcessorC3ReportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 5),
    _CucsBiosVfProcessorC3ReportPropAcl_Type()
)
cucsBiosVfProcessorC3ReportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportPropAcl.setStatus("current")
_CucsBiosVfProcessorC3ReportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorC3ReportSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorC3ReportSupportedByDefault = _CucsBiosVfProcessorC3ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 22, 1, 6),
    _CucsBiosVfProcessorC3ReportSupportedByDefault_Type()
)
cucsBiosVfProcessorC3ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC3ReportSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorC6ReportTable_Object = MibTable
cucsBiosVfProcessorC6ReportTable = _CucsBiosVfProcessorC6ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportTable.setStatus("current")
_CucsBiosVfProcessorC6ReportEntry_Object = MibTableRow
cucsBiosVfProcessorC6ReportEntry = _CucsBiosVfProcessorC6ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1)
)
cucsBiosVfProcessorC6ReportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorC6ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportEntry.setStatus("current")
_CucsBiosVfProcessorC6ReportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorC6ReportInstanceId_Object = MibTableColumn
cucsBiosVfProcessorC6ReportInstanceId = _CucsBiosVfProcessorC6ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 1),
    _CucsBiosVfProcessorC6ReportInstanceId_Type()
)
cucsBiosVfProcessorC6ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportInstanceId.setStatus("current")
_CucsBiosVfProcessorC6ReportDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorC6ReportDn_Object = MibTableColumn
cucsBiosVfProcessorC6ReportDn = _CucsBiosVfProcessorC6ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 2),
    _CucsBiosVfProcessorC6ReportDn_Type()
)
cucsBiosVfProcessorC6ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportDn.setStatus("current")
_CucsBiosVfProcessorC6ReportRn_Type = SnmpAdminString
_CucsBiosVfProcessorC6ReportRn_Object = MibTableColumn
cucsBiosVfProcessorC6ReportRn = _CucsBiosVfProcessorC6ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 3),
    _CucsBiosVfProcessorC6ReportRn_Type()
)
cucsBiosVfProcessorC6ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportRn.setStatus("current")
_CucsBiosVfProcessorC6ReportVpProcessorC6Report_Type = CucsBiosVfProcessorC6ReportVpProcessorC6Report
_CucsBiosVfProcessorC6ReportVpProcessorC6Report_Object = MibTableColumn
cucsBiosVfProcessorC6ReportVpProcessorC6Report = _CucsBiosVfProcessorC6ReportVpProcessorC6Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 4),
    _CucsBiosVfProcessorC6ReportVpProcessorC6Report_Type()
)
cucsBiosVfProcessorC6ReportVpProcessorC6Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportVpProcessorC6Report.setStatus("current")
_CucsBiosVfProcessorC6ReportPropAcl_Type = Unsigned64
_CucsBiosVfProcessorC6ReportPropAcl_Object = MibTableColumn
cucsBiosVfProcessorC6ReportPropAcl = _CucsBiosVfProcessorC6ReportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 5),
    _CucsBiosVfProcessorC6ReportPropAcl_Type()
)
cucsBiosVfProcessorC6ReportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportPropAcl.setStatus("current")
_CucsBiosVfProcessorC6ReportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorC6ReportSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorC6ReportSupportedByDefault = _CucsBiosVfProcessorC6ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 23, 1, 6),
    _CucsBiosVfProcessorC6ReportSupportedByDefault_Type()
)
cucsBiosVfProcessorC6ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC6ReportSupportedByDefault.setStatus("current")
_CucsBiosVfQuietBootTable_Object = MibTable
cucsBiosVfQuietBootTable = _CucsBiosVfQuietBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24)
)
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootTable.setStatus("current")
_CucsBiosVfQuietBootEntry_Object = MibTableRow
cucsBiosVfQuietBootEntry = _CucsBiosVfQuietBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1)
)
cucsBiosVfQuietBootEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfQuietBootInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootEntry.setStatus("current")
_CucsBiosVfQuietBootInstanceId_Type = CucsManagedObjectId
_CucsBiosVfQuietBootInstanceId_Object = MibTableColumn
cucsBiosVfQuietBootInstanceId = _CucsBiosVfQuietBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 1),
    _CucsBiosVfQuietBootInstanceId_Type()
)
cucsBiosVfQuietBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootInstanceId.setStatus("current")
_CucsBiosVfQuietBootDn_Type = CucsManagedObjectDn
_CucsBiosVfQuietBootDn_Object = MibTableColumn
cucsBiosVfQuietBootDn = _CucsBiosVfQuietBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 2),
    _CucsBiosVfQuietBootDn_Type()
)
cucsBiosVfQuietBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootDn.setStatus("current")
_CucsBiosVfQuietBootRn_Type = SnmpAdminString
_CucsBiosVfQuietBootRn_Object = MibTableColumn
cucsBiosVfQuietBootRn = _CucsBiosVfQuietBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 3),
    _CucsBiosVfQuietBootRn_Type()
)
cucsBiosVfQuietBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootRn.setStatus("current")
_CucsBiosVfQuietBootVpQuietBoot_Type = CucsBiosVfQuietBootVpQuietBoot
_CucsBiosVfQuietBootVpQuietBoot_Object = MibTableColumn
cucsBiosVfQuietBootVpQuietBoot = _CucsBiosVfQuietBootVpQuietBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 4),
    _CucsBiosVfQuietBootVpQuietBoot_Type()
)
cucsBiosVfQuietBootVpQuietBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootVpQuietBoot.setStatus("current")
_CucsBiosVfQuietBootPropAcl_Type = Unsigned64
_CucsBiosVfQuietBootPropAcl_Object = MibTableColumn
cucsBiosVfQuietBootPropAcl = _CucsBiosVfQuietBootPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 5),
    _CucsBiosVfQuietBootPropAcl_Type()
)
cucsBiosVfQuietBootPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootPropAcl.setStatus("current")
_CucsBiosVfQuietBootSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfQuietBootSupportedByDefault_Object = MibTableColumn
cucsBiosVfQuietBootSupportedByDefault = _CucsBiosVfQuietBootSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 24, 1, 6),
    _CucsBiosVfQuietBootSupportedByDefault_Type()
)
cucsBiosVfQuietBootSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQuietBootSupportedByDefault.setStatus("current")
_CucsBiosVfResumeOnACPowerLossTable_Object = MibTable
cucsBiosVfResumeOnACPowerLossTable = _CucsBiosVfResumeOnACPowerLossTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25)
)
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossTable.setStatus("current")
_CucsBiosVfResumeOnACPowerLossEntry_Object = MibTableRow
cucsBiosVfResumeOnACPowerLossEntry = _CucsBiosVfResumeOnACPowerLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1)
)
cucsBiosVfResumeOnACPowerLossEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfResumeOnACPowerLossInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossEntry.setStatus("current")
_CucsBiosVfResumeOnACPowerLossInstanceId_Type = CucsManagedObjectId
_CucsBiosVfResumeOnACPowerLossInstanceId_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossInstanceId = _CucsBiosVfResumeOnACPowerLossInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 1),
    _CucsBiosVfResumeOnACPowerLossInstanceId_Type()
)
cucsBiosVfResumeOnACPowerLossInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossInstanceId.setStatus("current")
_CucsBiosVfResumeOnACPowerLossDn_Type = CucsManagedObjectDn
_CucsBiosVfResumeOnACPowerLossDn_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossDn = _CucsBiosVfResumeOnACPowerLossDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 2),
    _CucsBiosVfResumeOnACPowerLossDn_Type()
)
cucsBiosVfResumeOnACPowerLossDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossDn.setStatus("current")
_CucsBiosVfResumeOnACPowerLossRn_Type = SnmpAdminString
_CucsBiosVfResumeOnACPowerLossRn_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossRn = _CucsBiosVfResumeOnACPowerLossRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 3),
    _CucsBiosVfResumeOnACPowerLossRn_Type()
)
cucsBiosVfResumeOnACPowerLossRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossRn.setStatus("current")
_CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type = CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss
_CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss = _CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 4),
    _CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss_Type()
)
cucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss.setStatus("current")
_CucsBiosVfResumeOnACPowerLossPropAcl_Type = Unsigned64
_CucsBiosVfResumeOnACPowerLossPropAcl_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossPropAcl = _CucsBiosVfResumeOnACPowerLossPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 5),
    _CucsBiosVfResumeOnACPowerLossPropAcl_Type()
)
cucsBiosVfResumeOnACPowerLossPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossPropAcl.setStatus("current")
_CucsBiosVfResumeOnACPowerLossSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfResumeOnACPowerLossSupportedByDefault_Object = MibTableColumn
cucsBiosVfResumeOnACPowerLossSupportedByDefault = _CucsBiosVfResumeOnACPowerLossSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 25, 1, 6),
    _CucsBiosVfResumeOnACPowerLossSupportedByDefault_Type()
)
cucsBiosVfResumeOnACPowerLossSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfResumeOnACPowerLossSupportedByDefault.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationTable_Object = MibTable
cucsBiosVfSelectMemoryRASConfigurationTable = _CucsBiosVfSelectMemoryRASConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26)
)
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationTable.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationEntry_Object = MibTableRow
cucsBiosVfSelectMemoryRASConfigurationEntry = _CucsBiosVfSelectMemoryRASConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1)
)
cucsBiosVfSelectMemoryRASConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfSelectMemoryRASConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationEntry.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfSelectMemoryRASConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfSelectMemoryRASConfigurationInstanceId = _CucsBiosVfSelectMemoryRASConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 1),
    _CucsBiosVfSelectMemoryRASConfigurationInstanceId_Type()
)
cucsBiosVfSelectMemoryRASConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationInstanceId.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfSelectMemoryRASConfigurationDn_Object = MibTableColumn
cucsBiosVfSelectMemoryRASConfigurationDn = _CucsBiosVfSelectMemoryRASConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 2),
    _CucsBiosVfSelectMemoryRASConfigurationDn_Type()
)
cucsBiosVfSelectMemoryRASConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationDn.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationRn_Type = SnmpAdminString
_CucsBiosVfSelectMemoryRASConfigurationRn_Object = MibTableColumn
cucsBiosVfSelectMemoryRASConfigurationRn = _CucsBiosVfSelectMemoryRASConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 3),
    _CucsBiosVfSelectMemoryRASConfigurationRn_Type()
)
cucsBiosVfSelectMemoryRASConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationRn.setStatus("current")
_CucsBiosVpSelectMemoryRASConfiguration_Type = CucsBiosVpSelectMemoryRASConfiguration
_CucsBiosVpSelectMemoryRASConfiguration_Object = MibTableColumn
cucsBiosVpSelectMemoryRASConfiguration = _CucsBiosVpSelectMemoryRASConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 4),
    _CucsBiosVpSelectMemoryRASConfiguration_Type()
)
cucsBiosVpSelectMemoryRASConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVpSelectMemoryRASConfiguration.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfSelectMemoryRASConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfSelectMemoryRASConfigurationPropAcl = _CucsBiosVfSelectMemoryRASConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 5),
    _CucsBiosVfSelectMemoryRASConfigurationPropAcl_Type()
)
cucsBiosVfSelectMemoryRASConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationPropAcl.setStatus("current")
_CucsBiosVfSelectMemoryRASConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfSelectMemoryRASConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfSelectMemoryRASConfigurationSupportedByDefault = _CucsBiosVfSelectMemoryRASConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 26, 1, 6),
    _CucsBiosVfSelectMemoryRASConfigurationSupportedByDefault_Type()
)
cucsBiosVfSelectMemoryRASConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSelectMemoryRASConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfACPI10SupportTable_Object = MibTable
cucsBiosVfACPI10SupportTable = _CucsBiosVfACPI10SupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27)
)
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportTable.setStatus("current")
_CucsBiosVfACPI10SupportEntry_Object = MibTableRow
cucsBiosVfACPI10SupportEntry = _CucsBiosVfACPI10SupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1)
)
cucsBiosVfACPI10SupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfACPI10SupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportEntry.setStatus("current")
_CucsBiosVfACPI10SupportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfACPI10SupportInstanceId_Object = MibTableColumn
cucsBiosVfACPI10SupportInstanceId = _CucsBiosVfACPI10SupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 1),
    _CucsBiosVfACPI10SupportInstanceId_Type()
)
cucsBiosVfACPI10SupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportInstanceId.setStatus("current")
_CucsBiosVfACPI10SupportDn_Type = CucsManagedObjectDn
_CucsBiosVfACPI10SupportDn_Object = MibTableColumn
cucsBiosVfACPI10SupportDn = _CucsBiosVfACPI10SupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 2),
    _CucsBiosVfACPI10SupportDn_Type()
)
cucsBiosVfACPI10SupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportDn.setStatus("current")
_CucsBiosVfACPI10SupportRn_Type = SnmpAdminString
_CucsBiosVfACPI10SupportRn_Object = MibTableColumn
cucsBiosVfACPI10SupportRn = _CucsBiosVfACPI10SupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 3),
    _CucsBiosVfACPI10SupportRn_Type()
)
cucsBiosVfACPI10SupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportRn.setStatus("current")
_CucsBiosVfACPI10SupportVpACPI10Support_Type = CucsBiosVfACPI10SupportVpACPI10Support
_CucsBiosVfACPI10SupportVpACPI10Support_Object = MibTableColumn
cucsBiosVfACPI10SupportVpACPI10Support = _CucsBiosVfACPI10SupportVpACPI10Support_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 4),
    _CucsBiosVfACPI10SupportVpACPI10Support_Type()
)
cucsBiosVfACPI10SupportVpACPI10Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportVpACPI10Support.setStatus("current")
_CucsBiosVfACPI10SupportPropAcl_Type = Unsigned64
_CucsBiosVfACPI10SupportPropAcl_Object = MibTableColumn
cucsBiosVfACPI10SupportPropAcl = _CucsBiosVfACPI10SupportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 5),
    _CucsBiosVfACPI10SupportPropAcl_Type()
)
cucsBiosVfACPI10SupportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportPropAcl.setStatus("current")
_CucsBiosVfACPI10SupportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfACPI10SupportSupportedByDefault_Object = MibTableColumn
cucsBiosVfACPI10SupportSupportedByDefault = _CucsBiosVfACPI10SupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 27, 1, 6),
    _CucsBiosVfACPI10SupportSupportedByDefault_Type()
)
cucsBiosVfACPI10SupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfACPI10SupportSupportedByDefault.setStatus("current")
_CucsBiosVfAssertNMIOnPERRTable_Object = MibTable
cucsBiosVfAssertNMIOnPERRTable = _CucsBiosVfAssertNMIOnPERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28)
)
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRTable.setStatus("current")
_CucsBiosVfAssertNMIOnPERREntry_Object = MibTableRow
cucsBiosVfAssertNMIOnPERREntry = _CucsBiosVfAssertNMIOnPERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1)
)
cucsBiosVfAssertNMIOnPERREntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfAssertNMIOnPERRInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERREntry.setStatus("current")
_CucsBiosVfAssertNMIOnPERRInstanceId_Type = CucsManagedObjectId
_CucsBiosVfAssertNMIOnPERRInstanceId_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRInstanceId = _CucsBiosVfAssertNMIOnPERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 1),
    _CucsBiosVfAssertNMIOnPERRInstanceId_Type()
)
cucsBiosVfAssertNMIOnPERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRInstanceId.setStatus("current")
_CucsBiosVfAssertNMIOnPERRDn_Type = CucsManagedObjectDn
_CucsBiosVfAssertNMIOnPERRDn_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRDn = _CucsBiosVfAssertNMIOnPERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 2),
    _CucsBiosVfAssertNMIOnPERRDn_Type()
)
cucsBiosVfAssertNMIOnPERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRDn.setStatus("current")
_CucsBiosVfAssertNMIOnPERRRn_Type = SnmpAdminString
_CucsBiosVfAssertNMIOnPERRRn_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRRn = _CucsBiosVfAssertNMIOnPERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 3),
    _CucsBiosVfAssertNMIOnPERRRn_Type()
)
cucsBiosVfAssertNMIOnPERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRRn.setStatus("current")
_CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type = CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR
_CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR = _CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 4),
    _CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR_Type()
)
cucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR.setStatus("current")
_CucsBiosVfAssertNMIOnPERRPropAcl_Type = Unsigned64
_CucsBiosVfAssertNMIOnPERRPropAcl_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRPropAcl = _CucsBiosVfAssertNMIOnPERRPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 5),
    _CucsBiosVfAssertNMIOnPERRPropAcl_Type()
)
cucsBiosVfAssertNMIOnPERRPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRPropAcl.setStatus("current")
_CucsBiosVfAssertNMIOnPERRSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfAssertNMIOnPERRSupportedByDefault_Object = MibTableColumn
cucsBiosVfAssertNMIOnPERRSupportedByDefault = _CucsBiosVfAssertNMIOnPERRSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 28, 1, 6),
    _CucsBiosVfAssertNMIOnPERRSupportedByDefault_Type()
)
cucsBiosVfAssertNMIOnPERRSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnPERRSupportedByDefault.setStatus("current")
_CucsBiosVfAssertNMIOnSERRTable_Object = MibTable
cucsBiosVfAssertNMIOnSERRTable = _CucsBiosVfAssertNMIOnSERRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29)
)
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRTable.setStatus("current")
_CucsBiosVfAssertNMIOnSERREntry_Object = MibTableRow
cucsBiosVfAssertNMIOnSERREntry = _CucsBiosVfAssertNMIOnSERREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1)
)
cucsBiosVfAssertNMIOnSERREntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfAssertNMIOnSERRInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERREntry.setStatus("current")
_CucsBiosVfAssertNMIOnSERRInstanceId_Type = CucsManagedObjectId
_CucsBiosVfAssertNMIOnSERRInstanceId_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRInstanceId = _CucsBiosVfAssertNMIOnSERRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 1),
    _CucsBiosVfAssertNMIOnSERRInstanceId_Type()
)
cucsBiosVfAssertNMIOnSERRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRInstanceId.setStatus("current")
_CucsBiosVfAssertNMIOnSERRDn_Type = CucsManagedObjectDn
_CucsBiosVfAssertNMIOnSERRDn_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRDn = _CucsBiosVfAssertNMIOnSERRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 2),
    _CucsBiosVfAssertNMIOnSERRDn_Type()
)
cucsBiosVfAssertNMIOnSERRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRDn.setStatus("current")
_CucsBiosVfAssertNMIOnSERRRn_Type = SnmpAdminString
_CucsBiosVfAssertNMIOnSERRRn_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRRn = _CucsBiosVfAssertNMIOnSERRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 3),
    _CucsBiosVfAssertNMIOnSERRRn_Type()
)
cucsBiosVfAssertNMIOnSERRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRRn.setStatus("current")
_CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type = CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR
_CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR = _CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 4),
    _CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR_Type()
)
cucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR.setStatus("current")
_CucsBiosVfAssertNMIOnSERRPropAcl_Type = Unsigned64
_CucsBiosVfAssertNMIOnSERRPropAcl_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRPropAcl = _CucsBiosVfAssertNMIOnSERRPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 5),
    _CucsBiosVfAssertNMIOnSERRPropAcl_Type()
)
cucsBiosVfAssertNMIOnSERRPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRPropAcl.setStatus("current")
_CucsBiosVfAssertNMIOnSERRSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfAssertNMIOnSERRSupportedByDefault_Object = MibTableColumn
cucsBiosVfAssertNMIOnSERRSupportedByDefault = _CucsBiosVfAssertNMIOnSERRSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 29, 1, 6),
    _CucsBiosVfAssertNMIOnSERRSupportedByDefault_Type()
)
cucsBiosVfAssertNMIOnSERRSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAssertNMIOnSERRSupportedByDefault.setStatus("current")
_CucsBiosVfCPUPerformanceTable_Object = MibTable
cucsBiosVfCPUPerformanceTable = _CucsBiosVfCPUPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30)
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceTable.setStatus("current")
_CucsBiosVfCPUPerformanceEntry_Object = MibTableRow
cucsBiosVfCPUPerformanceEntry = _CucsBiosVfCPUPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1)
)
cucsBiosVfCPUPerformanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfCPUPerformanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceEntry.setStatus("current")
_CucsBiosVfCPUPerformanceInstanceId_Type = CucsManagedObjectId
_CucsBiosVfCPUPerformanceInstanceId_Object = MibTableColumn
cucsBiosVfCPUPerformanceInstanceId = _CucsBiosVfCPUPerformanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 1),
    _CucsBiosVfCPUPerformanceInstanceId_Type()
)
cucsBiosVfCPUPerformanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceInstanceId.setStatus("current")
_CucsBiosVfCPUPerformanceDn_Type = CucsManagedObjectDn
_CucsBiosVfCPUPerformanceDn_Object = MibTableColumn
cucsBiosVfCPUPerformanceDn = _CucsBiosVfCPUPerformanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 2),
    _CucsBiosVfCPUPerformanceDn_Type()
)
cucsBiosVfCPUPerformanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceDn.setStatus("current")
_CucsBiosVfCPUPerformanceRn_Type = SnmpAdminString
_CucsBiosVfCPUPerformanceRn_Object = MibTableColumn
cucsBiosVfCPUPerformanceRn = _CucsBiosVfCPUPerformanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 3),
    _CucsBiosVfCPUPerformanceRn_Type()
)
cucsBiosVfCPUPerformanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceRn.setStatus("current")
_CucsBiosVfCPUPerformanceVpCPUPerformance_Type = CucsBiosVfCPUPerformanceVpCPUPerformance
_CucsBiosVfCPUPerformanceVpCPUPerformance_Object = MibTableColumn
cucsBiosVfCPUPerformanceVpCPUPerformance = _CucsBiosVfCPUPerformanceVpCPUPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 4),
    _CucsBiosVfCPUPerformanceVpCPUPerformance_Type()
)
cucsBiosVfCPUPerformanceVpCPUPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceVpCPUPerformance.setStatus("current")
_CucsBiosVfCPUPerformancePropAcl_Type = Unsigned64
_CucsBiosVfCPUPerformancePropAcl_Object = MibTableColumn
cucsBiosVfCPUPerformancePropAcl = _CucsBiosVfCPUPerformancePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 5),
    _CucsBiosVfCPUPerformancePropAcl_Type()
)
cucsBiosVfCPUPerformancePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformancePropAcl.setStatus("current")
_CucsBiosVfCPUPerformanceSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfCPUPerformanceSupportedByDefault_Object = MibTableColumn
cucsBiosVfCPUPerformanceSupportedByDefault = _CucsBiosVfCPUPerformanceSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 30, 1, 6),
    _CucsBiosVfCPUPerformanceSupportedByDefault_Type()
)
cucsBiosVfCPUPerformanceSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPerformanceSupportedByDefault.setStatus("current")
_CucsBiosVfBootOptionRetryTable_Object = MibTable
cucsBiosVfBootOptionRetryTable = _CucsBiosVfBootOptionRetryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31)
)
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryTable.setStatus("current")
_CucsBiosVfBootOptionRetryEntry_Object = MibTableRow
cucsBiosVfBootOptionRetryEntry = _CucsBiosVfBootOptionRetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1)
)
cucsBiosVfBootOptionRetryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfBootOptionRetryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryEntry.setStatus("current")
_CucsBiosVfBootOptionRetryInstanceId_Type = CucsManagedObjectId
_CucsBiosVfBootOptionRetryInstanceId_Object = MibTableColumn
cucsBiosVfBootOptionRetryInstanceId = _CucsBiosVfBootOptionRetryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 1),
    _CucsBiosVfBootOptionRetryInstanceId_Type()
)
cucsBiosVfBootOptionRetryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryInstanceId.setStatus("current")
_CucsBiosVfBootOptionRetryDn_Type = CucsManagedObjectDn
_CucsBiosVfBootOptionRetryDn_Object = MibTableColumn
cucsBiosVfBootOptionRetryDn = _CucsBiosVfBootOptionRetryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 2),
    _CucsBiosVfBootOptionRetryDn_Type()
)
cucsBiosVfBootOptionRetryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryDn.setStatus("current")
_CucsBiosVfBootOptionRetryRn_Type = SnmpAdminString
_CucsBiosVfBootOptionRetryRn_Object = MibTableColumn
cucsBiosVfBootOptionRetryRn = _CucsBiosVfBootOptionRetryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 3),
    _CucsBiosVfBootOptionRetryRn_Type()
)
cucsBiosVfBootOptionRetryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryRn.setStatus("current")
_CucsBiosVfBootOptionRetryVpBootOptionRetry_Type = CucsBiosVfBootOptionRetryVpBootOptionRetry
_CucsBiosVfBootOptionRetryVpBootOptionRetry_Object = MibTableColumn
cucsBiosVfBootOptionRetryVpBootOptionRetry = _CucsBiosVfBootOptionRetryVpBootOptionRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 4),
    _CucsBiosVfBootOptionRetryVpBootOptionRetry_Type()
)
cucsBiosVfBootOptionRetryVpBootOptionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryVpBootOptionRetry.setStatus("current")
_CucsBiosVfBootOptionRetryPropAcl_Type = Unsigned64
_CucsBiosVfBootOptionRetryPropAcl_Object = MibTableColumn
cucsBiosVfBootOptionRetryPropAcl = _CucsBiosVfBootOptionRetryPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 5),
    _CucsBiosVfBootOptionRetryPropAcl_Type()
)
cucsBiosVfBootOptionRetryPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetryPropAcl.setStatus("current")
_CucsBiosVfBootOptionRetrySupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfBootOptionRetrySupportedByDefault_Object = MibTableColumn
cucsBiosVfBootOptionRetrySupportedByDefault = _CucsBiosVfBootOptionRetrySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 31, 1, 6),
    _CucsBiosVfBootOptionRetrySupportedByDefault_Type()
)
cucsBiosVfBootOptionRetrySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfBootOptionRetrySupportedByDefault.setStatus("current")
_CucsBiosVfUSBBootConfigTable_Object = MibTable
cucsBiosVfUSBBootConfigTable = _CucsBiosVfUSBBootConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32)
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigTable.setStatus("current")
_CucsBiosVfUSBBootConfigEntry_Object = MibTableRow
cucsBiosVfUSBBootConfigEntry = _CucsBiosVfUSBBootConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1)
)
cucsBiosVfUSBBootConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUSBBootConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigEntry.setStatus("current")
_CucsBiosVfUSBBootConfigInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUSBBootConfigInstanceId_Object = MibTableColumn
cucsBiosVfUSBBootConfigInstanceId = _CucsBiosVfUSBBootConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 1),
    _CucsBiosVfUSBBootConfigInstanceId_Type()
)
cucsBiosVfUSBBootConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigInstanceId.setStatus("current")
_CucsBiosVfUSBBootConfigDn_Type = CucsManagedObjectDn
_CucsBiosVfUSBBootConfigDn_Object = MibTableColumn
cucsBiosVfUSBBootConfigDn = _CucsBiosVfUSBBootConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 2),
    _CucsBiosVfUSBBootConfigDn_Type()
)
cucsBiosVfUSBBootConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigDn.setStatus("current")
_CucsBiosVfUSBBootConfigRn_Type = SnmpAdminString
_CucsBiosVfUSBBootConfigRn_Object = MibTableColumn
cucsBiosVfUSBBootConfigRn = _CucsBiosVfUSBBootConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 3),
    _CucsBiosVfUSBBootConfigRn_Type()
)
cucsBiosVfUSBBootConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigRn.setStatus("current")
_CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type = CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable
_CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object = MibTableColumn
cucsBiosVfUSBBootConfigVpMakeDeviceNonBootable = _CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 4),
    _CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable_Type()
)
cucsBiosVfUSBBootConfigVpMakeDeviceNonBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigVpMakeDeviceNonBootable.setStatus("current")
_CucsBiosVfUSBBootConfigVpLegacyUSBSupport_Type = CucsBiosVfUSBBootConfigVpLegacyUSBSupport
_CucsBiosVfUSBBootConfigVpLegacyUSBSupport_Object = MibTableColumn
cucsBiosVfUSBBootConfigVpLegacyUSBSupport = _CucsBiosVfUSBBootConfigVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 5),
    _CucsBiosVfUSBBootConfigVpLegacyUSBSupport_Type()
)
cucsBiosVfUSBBootConfigVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigVpLegacyUSBSupport.setStatus("current")
_CucsBiosVfUSBBootConfigPropAcl_Type = Unsigned64
_CucsBiosVfUSBBootConfigPropAcl_Object = MibTableColumn
cucsBiosVfUSBBootConfigPropAcl = _CucsBiosVfUSBBootConfigPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 6),
    _CucsBiosVfUSBBootConfigPropAcl_Type()
)
cucsBiosVfUSBBootConfigPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigPropAcl.setStatus("current")
_CucsBiosVfUSBBootConfigSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUSBBootConfigSupportedByDefault_Object = MibTableColumn
cucsBiosVfUSBBootConfigSupportedByDefault = _CucsBiosVfUSBBootConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 32, 1, 7),
    _CucsBiosVfUSBBootConfigSupportedByDefault_Type()
)
cucsBiosVfUSBBootConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBBootConfigSupportedByDefault.setStatus("current")
_CucsBiosVfCoreMultiProcessingTable_Object = MibTable
cucsBiosVfCoreMultiProcessingTable = _CucsBiosVfCoreMultiProcessingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33)
)
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingTable.setStatus("current")
_CucsBiosVfCoreMultiProcessingEntry_Object = MibTableRow
cucsBiosVfCoreMultiProcessingEntry = _CucsBiosVfCoreMultiProcessingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1)
)
cucsBiosVfCoreMultiProcessingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfCoreMultiProcessingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingEntry.setStatus("current")
_CucsBiosVfCoreMultiProcessingInstanceId_Type = CucsManagedObjectId
_CucsBiosVfCoreMultiProcessingInstanceId_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingInstanceId = _CucsBiosVfCoreMultiProcessingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 1),
    _CucsBiosVfCoreMultiProcessingInstanceId_Type()
)
cucsBiosVfCoreMultiProcessingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingInstanceId.setStatus("current")
_CucsBiosVfCoreMultiProcessingDn_Type = CucsManagedObjectDn
_CucsBiosVfCoreMultiProcessingDn_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingDn = _CucsBiosVfCoreMultiProcessingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 2),
    _CucsBiosVfCoreMultiProcessingDn_Type()
)
cucsBiosVfCoreMultiProcessingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingDn.setStatus("current")
_CucsBiosVfCoreMultiProcessingRn_Type = SnmpAdminString
_CucsBiosVfCoreMultiProcessingRn_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingRn = _CucsBiosVfCoreMultiProcessingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 3),
    _CucsBiosVfCoreMultiProcessingRn_Type()
)
cucsBiosVfCoreMultiProcessingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingRn.setStatus("current")
_CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type = CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing
_CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingVpCoreMultiProcessing = _CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 4),
    _CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing_Type()
)
cucsBiosVfCoreMultiProcessingVpCoreMultiProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingVpCoreMultiProcessing.setStatus("current")
_CucsBiosVfCoreMultiProcessingPropAcl_Type = Unsigned64
_CucsBiosVfCoreMultiProcessingPropAcl_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingPropAcl = _CucsBiosVfCoreMultiProcessingPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 5),
    _CucsBiosVfCoreMultiProcessingPropAcl_Type()
)
cucsBiosVfCoreMultiProcessingPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingPropAcl.setStatus("current")
_CucsBiosVfCoreMultiProcessingSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfCoreMultiProcessingSupportedByDefault_Object = MibTableColumn
cucsBiosVfCoreMultiProcessingSupportedByDefault = _CucsBiosVfCoreMultiProcessingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 33, 1, 6),
    _CucsBiosVfCoreMultiProcessingSupportedByDefault_Type()
)
cucsBiosVfCoreMultiProcessingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCoreMultiProcessingSupportedByDefault.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoTable_Object = MibTable
cucsBiosVfUEFIOSUseLegacyVideoTable = _CucsBiosVfUEFIOSUseLegacyVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34)
)
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoTable.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoEntry_Object = MibTableRow
cucsBiosVfUEFIOSUseLegacyVideoEntry = _CucsBiosVfUEFIOSUseLegacyVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1)
)
cucsBiosVfUEFIOSUseLegacyVideoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUEFIOSUseLegacyVideoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoEntry.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUEFIOSUseLegacyVideoInstanceId_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoInstanceId = _CucsBiosVfUEFIOSUseLegacyVideoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 1),
    _CucsBiosVfUEFIOSUseLegacyVideoInstanceId_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoInstanceId.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoDn_Type = CucsManagedObjectDn
_CucsBiosVfUEFIOSUseLegacyVideoDn_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoDn = _CucsBiosVfUEFIOSUseLegacyVideoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 2),
    _CucsBiosVfUEFIOSUseLegacyVideoDn_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoDn.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoRn_Type = SnmpAdminString
_CucsBiosVfUEFIOSUseLegacyVideoRn_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoRn = _CucsBiosVfUEFIOSUseLegacyVideoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 3),
    _CucsBiosVfUEFIOSUseLegacyVideoRn_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoRn.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type = CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo
_CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo = _CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 4),
    _CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoPropAcl_Type = Unsigned64
_CucsBiosVfUEFIOSUseLegacyVideoPropAcl_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoPropAcl = _CucsBiosVfUEFIOSUseLegacyVideoPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 5),
    _CucsBiosVfUEFIOSUseLegacyVideoPropAcl_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoPropAcl.setStatus("current")
_CucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Object = MibTableColumn
cucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault = _CucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 34, 1, 6),
    _CucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault_Type()
)
cucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault.setStatus("current")
_CucsBiosVfDirectCacheAccessTable_Object = MibTable
cucsBiosVfDirectCacheAccessTable = _CucsBiosVfDirectCacheAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35)
)
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessTable.setStatus("current")
_CucsBiosVfDirectCacheAccessEntry_Object = MibTableRow
cucsBiosVfDirectCacheAccessEntry = _CucsBiosVfDirectCacheAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1)
)
cucsBiosVfDirectCacheAccessEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfDirectCacheAccessInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessEntry.setStatus("current")
_CucsBiosVfDirectCacheAccessInstanceId_Type = CucsManagedObjectId
_CucsBiosVfDirectCacheAccessInstanceId_Object = MibTableColumn
cucsBiosVfDirectCacheAccessInstanceId = _CucsBiosVfDirectCacheAccessInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 1),
    _CucsBiosVfDirectCacheAccessInstanceId_Type()
)
cucsBiosVfDirectCacheAccessInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessInstanceId.setStatus("current")
_CucsBiosVfDirectCacheAccessDn_Type = CucsManagedObjectDn
_CucsBiosVfDirectCacheAccessDn_Object = MibTableColumn
cucsBiosVfDirectCacheAccessDn = _CucsBiosVfDirectCacheAccessDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 2),
    _CucsBiosVfDirectCacheAccessDn_Type()
)
cucsBiosVfDirectCacheAccessDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessDn.setStatus("current")
_CucsBiosVfDirectCacheAccessRn_Type = SnmpAdminString
_CucsBiosVfDirectCacheAccessRn_Object = MibTableColumn
cucsBiosVfDirectCacheAccessRn = _CucsBiosVfDirectCacheAccessRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 3),
    _CucsBiosVfDirectCacheAccessRn_Type()
)
cucsBiosVfDirectCacheAccessRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessRn.setStatus("current")
_CucsBiosVfDirectCacheAccessVpDirectCacheAccess_Type = CucsBiosVfDirectCacheAccessVpDirectCacheAccess
_CucsBiosVfDirectCacheAccessVpDirectCacheAccess_Object = MibTableColumn
cucsBiosVfDirectCacheAccessVpDirectCacheAccess = _CucsBiosVfDirectCacheAccessVpDirectCacheAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 4),
    _CucsBiosVfDirectCacheAccessVpDirectCacheAccess_Type()
)
cucsBiosVfDirectCacheAccessVpDirectCacheAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessVpDirectCacheAccess.setStatus("current")
_CucsBiosVfDirectCacheAccessPropAcl_Type = Unsigned64
_CucsBiosVfDirectCacheAccessPropAcl_Object = MibTableColumn
cucsBiosVfDirectCacheAccessPropAcl = _CucsBiosVfDirectCacheAccessPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 5),
    _CucsBiosVfDirectCacheAccessPropAcl_Type()
)
cucsBiosVfDirectCacheAccessPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessPropAcl.setStatus("current")
_CucsBiosVfDirectCacheAccessSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfDirectCacheAccessSupportedByDefault_Object = MibTableColumn
cucsBiosVfDirectCacheAccessSupportedByDefault = _CucsBiosVfDirectCacheAccessSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 35, 1, 6),
    _CucsBiosVfDirectCacheAccessSupportedByDefault_Type()
)
cucsBiosVfDirectCacheAccessSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDirectCacheAccessSupportedByDefault.setStatus("current")
_CucsBiosVfExecuteDisableBitTable_Object = MibTable
cucsBiosVfExecuteDisableBitTable = _CucsBiosVfExecuteDisableBitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36)
)
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitTable.setStatus("current")
_CucsBiosVfExecuteDisableBitEntry_Object = MibTableRow
cucsBiosVfExecuteDisableBitEntry = _CucsBiosVfExecuteDisableBitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1)
)
cucsBiosVfExecuteDisableBitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfExecuteDisableBitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitEntry.setStatus("current")
_CucsBiosVfExecuteDisableBitInstanceId_Type = CucsManagedObjectId
_CucsBiosVfExecuteDisableBitInstanceId_Object = MibTableColumn
cucsBiosVfExecuteDisableBitInstanceId = _CucsBiosVfExecuteDisableBitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 1),
    _CucsBiosVfExecuteDisableBitInstanceId_Type()
)
cucsBiosVfExecuteDisableBitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitInstanceId.setStatus("current")
_CucsBiosVfExecuteDisableBitDn_Type = CucsManagedObjectDn
_CucsBiosVfExecuteDisableBitDn_Object = MibTableColumn
cucsBiosVfExecuteDisableBitDn = _CucsBiosVfExecuteDisableBitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 2),
    _CucsBiosVfExecuteDisableBitDn_Type()
)
cucsBiosVfExecuteDisableBitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitDn.setStatus("current")
_CucsBiosVfExecuteDisableBitRn_Type = SnmpAdminString
_CucsBiosVfExecuteDisableBitRn_Object = MibTableColumn
cucsBiosVfExecuteDisableBitRn = _CucsBiosVfExecuteDisableBitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 3),
    _CucsBiosVfExecuteDisableBitRn_Type()
)
cucsBiosVfExecuteDisableBitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitRn.setStatus("current")
_CucsBiosVfExecuteDisableBitVpExecuteDisableBit_Type = CucsBiosVfExecuteDisableBitVpExecuteDisableBit
_CucsBiosVfExecuteDisableBitVpExecuteDisableBit_Object = MibTableColumn
cucsBiosVfExecuteDisableBitVpExecuteDisableBit = _CucsBiosVfExecuteDisableBitVpExecuteDisableBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 4),
    _CucsBiosVfExecuteDisableBitVpExecuteDisableBit_Type()
)
cucsBiosVfExecuteDisableBitVpExecuteDisableBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitVpExecuteDisableBit.setStatus("current")
_CucsBiosVfExecuteDisableBitPropAcl_Type = Unsigned64
_CucsBiosVfExecuteDisableBitPropAcl_Object = MibTableColumn
cucsBiosVfExecuteDisableBitPropAcl = _CucsBiosVfExecuteDisableBitPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 5),
    _CucsBiosVfExecuteDisableBitPropAcl_Type()
)
cucsBiosVfExecuteDisableBitPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitPropAcl.setStatus("current")
_CucsBiosVfExecuteDisableBitSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfExecuteDisableBitSupportedByDefault_Object = MibTableColumn
cucsBiosVfExecuteDisableBitSupportedByDefault = _CucsBiosVfExecuteDisableBitSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 36, 1, 6),
    _CucsBiosVfExecuteDisableBitSupportedByDefault_Type()
)
cucsBiosVfExecuteDisableBitSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfExecuteDisableBitSupportedByDefault.setStatus("current")
_CucsBiosVfSparingModeTable_Object = MibTable
cucsBiosVfSparingModeTable = _CucsBiosVfSparingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37)
)
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeTable.setStatus("current")
_CucsBiosVfSparingModeEntry_Object = MibTableRow
cucsBiosVfSparingModeEntry = _CucsBiosVfSparingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1)
)
cucsBiosVfSparingModeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfSparingModeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeEntry.setStatus("current")
_CucsBiosVfSparingModeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfSparingModeInstanceId_Object = MibTableColumn
cucsBiosVfSparingModeInstanceId = _CucsBiosVfSparingModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 1),
    _CucsBiosVfSparingModeInstanceId_Type()
)
cucsBiosVfSparingModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeInstanceId.setStatus("current")
_CucsBiosVfSparingModeDn_Type = CucsManagedObjectDn
_CucsBiosVfSparingModeDn_Object = MibTableColumn
cucsBiosVfSparingModeDn = _CucsBiosVfSparingModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 2),
    _CucsBiosVfSparingModeDn_Type()
)
cucsBiosVfSparingModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeDn.setStatus("current")
_CucsBiosVfSparingModeRn_Type = SnmpAdminString
_CucsBiosVfSparingModeRn_Object = MibTableColumn
cucsBiosVfSparingModeRn = _CucsBiosVfSparingModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 3),
    _CucsBiosVfSparingModeRn_Type()
)
cucsBiosVfSparingModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeRn.setStatus("current")
_CucsBiosVfSparingModeVpSparingMode_Type = CucsBiosVfSparingModeVpSparingMode
_CucsBiosVfSparingModeVpSparingMode_Object = MibTableColumn
cucsBiosVfSparingModeVpSparingMode = _CucsBiosVfSparingModeVpSparingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 4),
    _CucsBiosVfSparingModeVpSparingMode_Type()
)
cucsBiosVfSparingModeVpSparingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeVpSparingMode.setStatus("current")
_CucsBiosVfSparingModePropAcl_Type = Unsigned64
_CucsBiosVfSparingModePropAcl_Object = MibTableColumn
cucsBiosVfSparingModePropAcl = _CucsBiosVfSparingModePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 5),
    _CucsBiosVfSparingModePropAcl_Type()
)
cucsBiosVfSparingModePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModePropAcl.setStatus("current")
_CucsBiosVfSparingModeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfSparingModeSupportedByDefault_Object = MibTableColumn
cucsBiosVfSparingModeSupportedByDefault = _CucsBiosVfSparingModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 37, 1, 6),
    _CucsBiosVfSparingModeSupportedByDefault_Type()
)
cucsBiosVfSparingModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSparingModeSupportedByDefault.setStatus("current")
_CucsBiosVfSerialPortAEnableTable_Object = MibTable
cucsBiosVfSerialPortAEnableTable = _CucsBiosVfSerialPortAEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38)
)
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableTable.setStatus("current")
_CucsBiosVfSerialPortAEnableEntry_Object = MibTableRow
cucsBiosVfSerialPortAEnableEntry = _CucsBiosVfSerialPortAEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1)
)
cucsBiosVfSerialPortAEnableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfSerialPortAEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableEntry.setStatus("current")
_CucsBiosVfSerialPortAEnableInstanceId_Type = CucsManagedObjectId
_CucsBiosVfSerialPortAEnableInstanceId_Object = MibTableColumn
cucsBiosVfSerialPortAEnableInstanceId = _CucsBiosVfSerialPortAEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 1),
    _CucsBiosVfSerialPortAEnableInstanceId_Type()
)
cucsBiosVfSerialPortAEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableInstanceId.setStatus("current")
_CucsBiosVfSerialPortAEnableDn_Type = CucsManagedObjectDn
_CucsBiosVfSerialPortAEnableDn_Object = MibTableColumn
cucsBiosVfSerialPortAEnableDn = _CucsBiosVfSerialPortAEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 2),
    _CucsBiosVfSerialPortAEnableDn_Type()
)
cucsBiosVfSerialPortAEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableDn.setStatus("current")
_CucsBiosVfSerialPortAEnableRn_Type = SnmpAdminString
_CucsBiosVfSerialPortAEnableRn_Object = MibTableColumn
cucsBiosVfSerialPortAEnableRn = _CucsBiosVfSerialPortAEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 3),
    _CucsBiosVfSerialPortAEnableRn_Type()
)
cucsBiosVfSerialPortAEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableRn.setStatus("current")
_CucsBiosVfSerialPortAEnableVpSerialPortAEnable_Type = CucsBiosVfSerialPortAEnableVpSerialPortAEnable
_CucsBiosVfSerialPortAEnableVpSerialPortAEnable_Object = MibTableColumn
cucsBiosVfSerialPortAEnableVpSerialPortAEnable = _CucsBiosVfSerialPortAEnableVpSerialPortAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 4),
    _CucsBiosVfSerialPortAEnableVpSerialPortAEnable_Type()
)
cucsBiosVfSerialPortAEnableVpSerialPortAEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableVpSerialPortAEnable.setStatus("current")
_CucsBiosVfSerialPortAEnablePropAcl_Type = Unsigned64
_CucsBiosVfSerialPortAEnablePropAcl_Object = MibTableColumn
cucsBiosVfSerialPortAEnablePropAcl = _CucsBiosVfSerialPortAEnablePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 5),
    _CucsBiosVfSerialPortAEnablePropAcl_Type()
)
cucsBiosVfSerialPortAEnablePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnablePropAcl.setStatus("current")
_CucsBiosVfSerialPortAEnableSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfSerialPortAEnableSupportedByDefault_Object = MibTableColumn
cucsBiosVfSerialPortAEnableSupportedByDefault = _CucsBiosVfSerialPortAEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 38, 1, 6),
    _CucsBiosVfSerialPortAEnableSupportedByDefault_Type()
)
cucsBiosVfSerialPortAEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSerialPortAEnableSupportedByDefault.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleTable_Object = MibTable
cucsBiosVfIntelEntrySASRAIDModuleTable = _CucsBiosVfIntelEntrySASRAIDModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleTable.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleEntry_Object = MibTableRow
cucsBiosVfIntelEntrySASRAIDModuleEntry = _CucsBiosVfIntelEntrySASRAIDModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1)
)
cucsBiosVfIntelEntrySASRAIDModuleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelEntrySASRAIDModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleEntry.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelEntrySASRAIDModuleInstanceId_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleInstanceId = _CucsBiosVfIntelEntrySASRAIDModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 1),
    _CucsBiosVfIntelEntrySASRAIDModuleInstanceId_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleInstanceId.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleDn_Type = CucsManagedObjectDn
_CucsBiosVfIntelEntrySASRAIDModuleDn_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleDn = _CucsBiosVfIntelEntrySASRAIDModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 2),
    _CucsBiosVfIntelEntrySASRAIDModuleDn_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleDn.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleRn_Type = SnmpAdminString
_CucsBiosVfIntelEntrySASRAIDModuleRn_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleRn = _CucsBiosVfIntelEntrySASRAIDModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 3),
    _CucsBiosVfIntelEntrySASRAIDModuleRn_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleRn.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type = CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID
_CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleVpSASRAID = _CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 4),
    _CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleVpSASRAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleVpSASRAID.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type = CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule
_CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule = _CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 5),
    _CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModulePropAcl_Type = Unsigned64
_CucsBiosVfIntelEntrySASRAIDModulePropAcl_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModulePropAcl = _CucsBiosVfIntelEntrySASRAIDModulePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 6),
    _CucsBiosVfIntelEntrySASRAIDModulePropAcl_Type()
)
cucsBiosVfIntelEntrySASRAIDModulePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModulePropAcl.setStatus("current")
_CucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault = _CucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 39, 1, 7),
    _CucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault_Type()
)
cucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault.setStatus("current")
_CucsBiosVfPOSTErrorPauseTable_Object = MibTable
cucsBiosVfPOSTErrorPauseTable = _CucsBiosVfPOSTErrorPauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40)
)
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseTable.setStatus("current")
_CucsBiosVfPOSTErrorPauseEntry_Object = MibTableRow
cucsBiosVfPOSTErrorPauseEntry = _CucsBiosVfPOSTErrorPauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1)
)
cucsBiosVfPOSTErrorPauseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPOSTErrorPauseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseEntry.setStatus("current")
_CucsBiosVfPOSTErrorPauseInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPOSTErrorPauseInstanceId_Object = MibTableColumn
cucsBiosVfPOSTErrorPauseInstanceId = _CucsBiosVfPOSTErrorPauseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 1),
    _CucsBiosVfPOSTErrorPauseInstanceId_Type()
)
cucsBiosVfPOSTErrorPauseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseInstanceId.setStatus("current")
_CucsBiosVfPOSTErrorPauseDn_Type = CucsManagedObjectDn
_CucsBiosVfPOSTErrorPauseDn_Object = MibTableColumn
cucsBiosVfPOSTErrorPauseDn = _CucsBiosVfPOSTErrorPauseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 2),
    _CucsBiosVfPOSTErrorPauseDn_Type()
)
cucsBiosVfPOSTErrorPauseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseDn.setStatus("current")
_CucsBiosVfPOSTErrorPauseRn_Type = SnmpAdminString
_CucsBiosVfPOSTErrorPauseRn_Object = MibTableColumn
cucsBiosVfPOSTErrorPauseRn = _CucsBiosVfPOSTErrorPauseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 3),
    _CucsBiosVfPOSTErrorPauseRn_Type()
)
cucsBiosVfPOSTErrorPauseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseRn.setStatus("current")
_CucsBiosVfPOSTErrorPauseVpPOSTErrorPause_Type = CucsBiosVfPOSTErrorPauseVpPOSTErrorPause
_CucsBiosVfPOSTErrorPauseVpPOSTErrorPause_Object = MibTableColumn
cucsBiosVfPOSTErrorPauseVpPOSTErrorPause = _CucsBiosVfPOSTErrorPauseVpPOSTErrorPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 4),
    _CucsBiosVfPOSTErrorPauseVpPOSTErrorPause_Type()
)
cucsBiosVfPOSTErrorPauseVpPOSTErrorPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseVpPOSTErrorPause.setStatus("current")
_CucsBiosVfPOSTErrorPausePropAcl_Type = Unsigned64
_CucsBiosVfPOSTErrorPausePropAcl_Object = MibTableColumn
cucsBiosVfPOSTErrorPausePropAcl = _CucsBiosVfPOSTErrorPausePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 5),
    _CucsBiosVfPOSTErrorPausePropAcl_Type()
)
cucsBiosVfPOSTErrorPausePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPausePropAcl.setStatus("current")
_CucsBiosVfPOSTErrorPauseSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPOSTErrorPauseSupportedByDefault_Object = MibTableColumn
cucsBiosVfPOSTErrorPauseSupportedByDefault = _CucsBiosVfPOSTErrorPauseSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 40, 1, 6),
    _CucsBiosVfPOSTErrorPauseSupportedByDefault_Type()
)
cucsBiosVfPOSTErrorPauseSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPOSTErrorPauseSupportedByDefault.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBTable_Object = MibTable
cucsBiosVfMaximumMemoryBelow4GBTable = _CucsBiosVfMaximumMemoryBelow4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41)
)
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBTable.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBEntry_Object = MibTableRow
cucsBiosVfMaximumMemoryBelow4GBEntry = _CucsBiosVfMaximumMemoryBelow4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1)
)
cucsBiosVfMaximumMemoryBelow4GBEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfMaximumMemoryBelow4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBEntry.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBInstanceId_Type = CucsManagedObjectId
_CucsBiosVfMaximumMemoryBelow4GBInstanceId_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBInstanceId = _CucsBiosVfMaximumMemoryBelow4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 1),
    _CucsBiosVfMaximumMemoryBelow4GBInstanceId_Type()
)
cucsBiosVfMaximumMemoryBelow4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBInstanceId.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBDn_Type = CucsManagedObjectDn
_CucsBiosVfMaximumMemoryBelow4GBDn_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBDn = _CucsBiosVfMaximumMemoryBelow4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 2),
    _CucsBiosVfMaximumMemoryBelow4GBDn_Type()
)
cucsBiosVfMaximumMemoryBelow4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBDn.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBRn_Type = SnmpAdminString
_CucsBiosVfMaximumMemoryBelow4GBRn_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBRn = _CucsBiosVfMaximumMemoryBelow4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 3),
    _CucsBiosVfMaximumMemoryBelow4GBRn_Type()
)
cucsBiosVfMaximumMemoryBelow4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBRn.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type = CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB
_CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB = _CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 4),
    _CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB_Type()
)
cucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBPropAcl_Type = Unsigned64
_CucsBiosVfMaximumMemoryBelow4GBPropAcl_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBPropAcl = _CucsBiosVfMaximumMemoryBelow4GBPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 5),
    _CucsBiosVfMaximumMemoryBelow4GBPropAcl_Type()
)
cucsBiosVfMaximumMemoryBelow4GBPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBPropAcl.setStatus("current")
_CucsBiosVfMaximumMemoryBelow4GBSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfMaximumMemoryBelow4GBSupportedByDefault_Object = MibTableColumn
cucsBiosVfMaximumMemoryBelow4GBSupportedByDefault = _CucsBiosVfMaximumMemoryBelow4GBSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 41, 1, 6),
    _CucsBiosVfMaximumMemoryBelow4GBSupportedByDefault_Type()
)
cucsBiosVfMaximumMemoryBelow4GBSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaximumMemoryBelow4GBSupportedByDefault.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBTable_Object = MibTable
cucsBiosVfMemoryMappedIOAbove4GBTable = _CucsBiosVfMemoryMappedIOAbove4GBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42)
)
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBTable.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBEntry_Object = MibTableRow
cucsBiosVfMemoryMappedIOAbove4GBEntry = _CucsBiosVfMemoryMappedIOAbove4GBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1)
)
cucsBiosVfMemoryMappedIOAbove4GBEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfMemoryMappedIOAbove4GBInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBEntry.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBInstanceId_Type = CucsManagedObjectId
_CucsBiosVfMemoryMappedIOAbove4GBInstanceId_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBInstanceId = _CucsBiosVfMemoryMappedIOAbove4GBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 1),
    _CucsBiosVfMemoryMappedIOAbove4GBInstanceId_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBInstanceId.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBDn_Type = CucsManagedObjectDn
_CucsBiosVfMemoryMappedIOAbove4GBDn_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBDn = _CucsBiosVfMemoryMappedIOAbove4GBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 2),
    _CucsBiosVfMemoryMappedIOAbove4GBDn_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBDn.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBRn_Type = SnmpAdminString
_CucsBiosVfMemoryMappedIOAbove4GBRn_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBRn = _CucsBiosVfMemoryMappedIOAbove4GBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 3),
    _CucsBiosVfMemoryMappedIOAbove4GBRn_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBRn.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type = CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB
_CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB = _CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 4),
    _CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBPropAcl_Type = Unsigned64
_CucsBiosVfMemoryMappedIOAbove4GBPropAcl_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBPropAcl = _CucsBiosVfMemoryMappedIOAbove4GBPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 5),
    _CucsBiosVfMemoryMappedIOAbove4GBPropAcl_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBPropAcl.setStatus("current")
_CucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Object = MibTableColumn
cucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault = _CucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 42, 1, 6),
    _CucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault_Type()
)
cucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTable_Object = MibTable
cucsBiosVfOSBootWatchdogTimerTable = _CucsBiosVfOSBootWatchdogTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43)
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTable.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerEntry_Object = MibTableRow
cucsBiosVfOSBootWatchdogTimerEntry = _CucsBiosVfOSBootWatchdogTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1)
)
cucsBiosVfOSBootWatchdogTimerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOSBootWatchdogTimerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerEntry.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOSBootWatchdogTimerInstanceId_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerInstanceId = _CucsBiosVfOSBootWatchdogTimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 1),
    _CucsBiosVfOSBootWatchdogTimerInstanceId_Type()
)
cucsBiosVfOSBootWatchdogTimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerInstanceId.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerDn_Type = CucsManagedObjectDn
_CucsBiosVfOSBootWatchdogTimerDn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerDn = _CucsBiosVfOSBootWatchdogTimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 2),
    _CucsBiosVfOSBootWatchdogTimerDn_Type()
)
cucsBiosVfOSBootWatchdogTimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerDn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerRn_Type = SnmpAdminString
_CucsBiosVfOSBootWatchdogTimerRn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerRn = _CucsBiosVfOSBootWatchdogTimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 3),
    _CucsBiosVfOSBootWatchdogTimerRn_Type()
)
cucsBiosVfOSBootWatchdogTimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerRn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type = CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer
_CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer = _CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 4),
    _CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer_Type()
)
cucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPropAcl_Type = Unsigned64
_CucsBiosVfOSBootWatchdogTimerPropAcl_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPropAcl = _CucsBiosVfOSBootWatchdogTimerPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 5),
    _CucsBiosVfOSBootWatchdogTimerPropAcl_Type()
)
cucsBiosVfOSBootWatchdogTimerPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPropAcl.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOSBootWatchdogTimerSupportedByDefault_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerSupportedByDefault = _CucsBiosVfOSBootWatchdogTimerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 43, 1, 6),
    _CucsBiosVfOSBootWatchdogTimerSupportedByDefault_Type()
)
cucsBiosVfOSBootWatchdogTimerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerSupportedByDefault.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyTable_Object = MibTable
cucsBiosVfOSBootWatchdogTimerPolicyTable = _CucsBiosVfOSBootWatchdogTimerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44)
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyTable.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyEntry_Object = MibTableRow
cucsBiosVfOSBootWatchdogTimerPolicyEntry = _CucsBiosVfOSBootWatchdogTimerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1)
)
cucsBiosVfOSBootWatchdogTimerPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOSBootWatchdogTimerPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyEntry.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOSBootWatchdogTimerPolicyInstanceId_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicyInstanceId = _CucsBiosVfOSBootWatchdogTimerPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 1),
    _CucsBiosVfOSBootWatchdogTimerPolicyInstanceId_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyInstanceId.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyDn_Type = CucsManagedObjectDn
_CucsBiosVfOSBootWatchdogTimerPolicyDn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicyDn = _CucsBiosVfOSBootWatchdogTimerPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 2),
    _CucsBiosVfOSBootWatchdogTimerPolicyDn_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyDn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyRn_Type = SnmpAdminString
_CucsBiosVfOSBootWatchdogTimerPolicyRn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicyRn = _CucsBiosVfOSBootWatchdogTimerPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 3),
    _CucsBiosVfOSBootWatchdogTimerPolicyRn_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyRn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type = CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy
_CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy = _CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 4),
    _CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicyPropAcl_Type = Unsigned64
_CucsBiosVfOSBootWatchdogTimerPolicyPropAcl_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicyPropAcl = _CucsBiosVfOSBootWatchdogTimerPolicyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 5),
    _CucsBiosVfOSBootWatchdogTimerPolicyPropAcl_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicyPropAcl.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault = _CucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 44, 1, 6),
    _CucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault_Type()
)
cucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault.setStatus("current")
_CucsBiosVfOnboardSATAControllerTable_Object = MibTable
cucsBiosVfOnboardSATAControllerTable = _CucsBiosVfOnboardSATAControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46)
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerTable.setStatus("current")
_CucsBiosVfOnboardSATAControllerEntry_Object = MibTableRow
cucsBiosVfOnboardSATAControllerEntry = _CucsBiosVfOnboardSATAControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1)
)
cucsBiosVfOnboardSATAControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOnboardSATAControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerEntry.setStatus("current")
_CucsBiosVfOnboardSATAControllerInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOnboardSATAControllerInstanceId_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerInstanceId = _CucsBiosVfOnboardSATAControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 1),
    _CucsBiosVfOnboardSATAControllerInstanceId_Type()
)
cucsBiosVfOnboardSATAControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerInstanceId.setStatus("current")
_CucsBiosVfOnboardSATAControllerDn_Type = CucsManagedObjectDn
_CucsBiosVfOnboardSATAControllerDn_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerDn = _CucsBiosVfOnboardSATAControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 2),
    _CucsBiosVfOnboardSATAControllerDn_Type()
)
cucsBiosVfOnboardSATAControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerDn.setStatus("current")
_CucsBiosVfOnboardSATAControllerRn_Type = SnmpAdminString
_CucsBiosVfOnboardSATAControllerRn_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerRn = _CucsBiosVfOnboardSATAControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 3),
    _CucsBiosVfOnboardSATAControllerRn_Type()
)
cucsBiosVfOnboardSATAControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerRn.setStatus("current")
_CucsBiosVfOnboardSATAControllerVpOnboardSATAController_Type = CucsBiosVfOnboardSATAControllerVpOnboardSATAController
_CucsBiosVfOnboardSATAControllerVpOnboardSATAController_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerVpOnboardSATAController = _CucsBiosVfOnboardSATAControllerVpOnboardSATAController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 4),
    _CucsBiosVfOnboardSATAControllerVpOnboardSATAController_Type()
)
cucsBiosVfOnboardSATAControllerVpOnboardSATAController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerVpOnboardSATAController.setStatus("current")
_CucsBiosVfOnboardSATAControllerVpSATAMode_Type = CucsBiosVfOnboardSATAControllerVpSATAMode
_CucsBiosVfOnboardSATAControllerVpSATAMode_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerVpSATAMode = _CucsBiosVfOnboardSATAControllerVpSATAMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 5),
    _CucsBiosVfOnboardSATAControllerVpSATAMode_Type()
)
cucsBiosVfOnboardSATAControllerVpSATAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerVpSATAMode.setStatus("current")
_CucsBiosVfOnboardSATAControllerPropAcl_Type = Unsigned64
_CucsBiosVfOnboardSATAControllerPropAcl_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerPropAcl = _CucsBiosVfOnboardSATAControllerPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 6),
    _CucsBiosVfOnboardSATAControllerPropAcl_Type()
)
cucsBiosVfOnboardSATAControllerPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerPropAcl.setStatus("current")
_CucsBiosVfOnboardSATAControllerSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOnboardSATAControllerSupportedByDefault_Object = MibTableColumn
cucsBiosVfOnboardSATAControllerSupportedByDefault = _CucsBiosVfOnboardSATAControllerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 46, 1, 7),
    _CucsBiosVfOnboardSATAControllerSupportedByDefault_Type()
)
cucsBiosVfOnboardSATAControllerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardSATAControllerSupportedByDefault.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingTable_Object = MibTable
cucsBiosVfMaxVariableMTRRSettingTable = _CucsBiosVfMaxVariableMTRRSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47)
)
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingTable.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingEntry_Object = MibTableRow
cucsBiosVfMaxVariableMTRRSettingEntry = _CucsBiosVfMaxVariableMTRRSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1)
)
cucsBiosVfMaxVariableMTRRSettingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfMaxVariableMTRRSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingEntry.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingInstanceId_Type = CucsManagedObjectId
_CucsBiosVfMaxVariableMTRRSettingInstanceId_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingInstanceId = _CucsBiosVfMaxVariableMTRRSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 1),
    _CucsBiosVfMaxVariableMTRRSettingInstanceId_Type()
)
cucsBiosVfMaxVariableMTRRSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingInstanceId.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingDn_Type = CucsManagedObjectDn
_CucsBiosVfMaxVariableMTRRSettingDn_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingDn = _CucsBiosVfMaxVariableMTRRSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 2),
    _CucsBiosVfMaxVariableMTRRSettingDn_Type()
)
cucsBiosVfMaxVariableMTRRSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingDn.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingRn_Type = SnmpAdminString
_CucsBiosVfMaxVariableMTRRSettingRn_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingRn = _CucsBiosVfMaxVariableMTRRSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 3),
    _CucsBiosVfMaxVariableMTRRSettingRn_Type()
)
cucsBiosVfMaxVariableMTRRSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingRn.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type = CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr
_CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr = _CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 4),
    _CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr_Type()
)
cucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingPropAcl_Type = Unsigned64
_CucsBiosVfMaxVariableMTRRSettingPropAcl_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingPropAcl = _CucsBiosVfMaxVariableMTRRSettingPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 5),
    _CucsBiosVfMaxVariableMTRRSettingPropAcl_Type()
)
cucsBiosVfMaxVariableMTRRSettingPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingPropAcl.setStatus("current")
_CucsBiosVfMaxVariableMTRRSettingSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfMaxVariableMTRRSettingSupportedByDefault_Object = MibTableColumn
cucsBiosVfMaxVariableMTRRSettingSupportedByDefault = _CucsBiosVfMaxVariableMTRRSettingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 47, 1, 6),
    _CucsBiosVfMaxVariableMTRRSettingSupportedByDefault_Type()
)
cucsBiosVfMaxVariableMTRRSettingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfMaxVariableMTRRSettingSupportedByDefault.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlTable_Object = MibTable
cucsBiosVfUCSMBootOrderRuleControlTable = _CucsBiosVfUCSMBootOrderRuleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48)
)
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlTable.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlEntry_Object = MibTableRow
cucsBiosVfUCSMBootOrderRuleControlEntry = _CucsBiosVfUCSMBootOrderRuleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1)
)
cucsBiosVfUCSMBootOrderRuleControlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUCSMBootOrderRuleControlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlEntry.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUCSMBootOrderRuleControlInstanceId_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlInstanceId = _CucsBiosVfUCSMBootOrderRuleControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 1),
    _CucsBiosVfUCSMBootOrderRuleControlInstanceId_Type()
)
cucsBiosVfUCSMBootOrderRuleControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlInstanceId.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlDn_Type = CucsManagedObjectDn
_CucsBiosVfUCSMBootOrderRuleControlDn_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlDn = _CucsBiosVfUCSMBootOrderRuleControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 2),
    _CucsBiosVfUCSMBootOrderRuleControlDn_Type()
)
cucsBiosVfUCSMBootOrderRuleControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlDn.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlRn_Type = SnmpAdminString
_CucsBiosVfUCSMBootOrderRuleControlRn_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlRn = _CucsBiosVfUCSMBootOrderRuleControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 3),
    _CucsBiosVfUCSMBootOrderRuleControlRn_Type()
)
cucsBiosVfUCSMBootOrderRuleControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlRn.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Type = CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule
_CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule = _CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 4),
    _CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule_Type()
)
cucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlPropAcl_Type = Unsigned64
_CucsBiosVfUCSMBootOrderRuleControlPropAcl_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlPropAcl = _CucsBiosVfUCSMBootOrderRuleControlPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 5),
    _CucsBiosVfUCSMBootOrderRuleControlPropAcl_Type()
)
cucsBiosVfUCSMBootOrderRuleControlPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlPropAcl.setStatus("current")
_CucsBiosVfUCSMBootOrderRuleControlSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUCSMBootOrderRuleControlSupportedByDefault_Object = MibTableColumn
cucsBiosVfUCSMBootOrderRuleControlSupportedByDefault = _CucsBiosVfUCSMBootOrderRuleControlSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 48, 1, 6),
    _CucsBiosVfUCSMBootOrderRuleControlSupportedByDefault_Type()
)
cucsBiosVfUCSMBootOrderRuleControlSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootOrderRuleControlSupportedByDefault.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockTable_Object = MibTable
cucsBiosVfUSBFrontPanelAccessLockTable = _CucsBiosVfUSBFrontPanelAccessLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49)
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockTable.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockEntry_Object = MibTableRow
cucsBiosVfUSBFrontPanelAccessLockEntry = _CucsBiosVfUSBFrontPanelAccessLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1)
)
cucsBiosVfUSBFrontPanelAccessLockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUSBFrontPanelAccessLockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockEntry.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUSBFrontPanelAccessLockInstanceId_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockInstanceId = _CucsBiosVfUSBFrontPanelAccessLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 1),
    _CucsBiosVfUSBFrontPanelAccessLockInstanceId_Type()
)
cucsBiosVfUSBFrontPanelAccessLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockInstanceId.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockDn_Type = CucsManagedObjectDn
_CucsBiosVfUSBFrontPanelAccessLockDn_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockDn = _CucsBiosVfUSBFrontPanelAccessLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 2),
    _CucsBiosVfUSBFrontPanelAccessLockDn_Type()
)
cucsBiosVfUSBFrontPanelAccessLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockDn.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockRn_Type = SnmpAdminString
_CucsBiosVfUSBFrontPanelAccessLockRn_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockRn = _CucsBiosVfUSBFrontPanelAccessLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 3),
    _CucsBiosVfUSBFrontPanelAccessLockRn_Type()
)
cucsBiosVfUSBFrontPanelAccessLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockRn.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type = CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock
_CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock = _CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 4),
    _CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock_Type()
)
cucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockPropAcl_Type = Unsigned64
_CucsBiosVfUSBFrontPanelAccessLockPropAcl_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockPropAcl = _CucsBiosVfUSBFrontPanelAccessLockPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 5),
    _CucsBiosVfUSBFrontPanelAccessLockPropAcl_Type()
)
cucsBiosVfUSBFrontPanelAccessLockPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockPropAcl.setStatus("current")
_CucsBiosVfUSBFrontPanelAccessLockSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUSBFrontPanelAccessLockSupportedByDefault_Object = MibTableColumn
cucsBiosVfUSBFrontPanelAccessLockSupportedByDefault = _CucsBiosVfUSBFrontPanelAccessLockSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 49, 1, 6),
    _CucsBiosVfUSBFrontPanelAccessLockSupportedByDefault_Type()
)
cucsBiosVfUSBFrontPanelAccessLockSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBFrontPanelAccessLockSupportedByDefault.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object = MibTable
cucsBiosVfUSBSystemIdlePowerOptimizingSettingTable = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50)
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingTable.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object = MibTableRow
cucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1)
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object = MibTableColumn
cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 1),
    _CucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId_Type()
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type = CucsManagedObjectDn
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object = MibTableColumn
cucsBiosVfUSBSystemIdlePowerOptimizingSettingDn = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 2),
    _CucsBiosVfUSBSystemIdlePowerOptimizingSettingDn_Type()
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingDn.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type = SnmpAdminString
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object = MibTableColumn
cucsBiosVfUSBSystemIdlePowerOptimizingSettingRn = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 3),
    _CucsBiosVfUSBSystemIdlePowerOptimizingSettingRn_Type()
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingRn.setStatus("current")
_CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize_Type = CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize
_CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize_Object = MibTableColumn
cucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize = _CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 4),
    _CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize_Type()
)
cucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl_Type = Unsigned64
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl_Object = MibTableColumn
cucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 5),
    _CucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl_Type()
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl.setStatus("current")
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Object = MibTableColumn
cucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault = _CucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 50, 1, 6),
    _CucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault_Type()
)
cucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault.setStatus("current")
_CucsBiosVIdentityParamsTable_Object = MibTable
cucsBiosVIdentityParamsTable = _CucsBiosVIdentityParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51)
)
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsTable.setStatus("current")
_CucsBiosVIdentityParamsEntry_Object = MibTableRow
cucsBiosVIdentityParamsEntry = _CucsBiosVIdentityParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1)
)
cucsBiosVIdentityParamsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVIdentityParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsEntry.setStatus("current")
_CucsBiosVIdentityParamsInstanceId_Type = CucsManagedObjectId
_CucsBiosVIdentityParamsInstanceId_Object = MibTableColumn
cucsBiosVIdentityParamsInstanceId = _CucsBiosVIdentityParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 1),
    _CucsBiosVIdentityParamsInstanceId_Type()
)
cucsBiosVIdentityParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsInstanceId.setStatus("current")
_CucsBiosVIdentityParamsDn_Type = CucsManagedObjectDn
_CucsBiosVIdentityParamsDn_Object = MibTableColumn
cucsBiosVIdentityParamsDn = _CucsBiosVIdentityParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 2),
    _CucsBiosVIdentityParamsDn_Type()
)
cucsBiosVIdentityParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsDn.setStatus("current")
_CucsBiosVIdentityParamsRn_Type = SnmpAdminString
_CucsBiosVIdentityParamsRn_Object = MibTableColumn
cucsBiosVIdentityParamsRn = _CucsBiosVIdentityParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 3),
    _CucsBiosVIdentityParamsRn_Type()
)
cucsBiosVIdentityParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsRn.setStatus("current")
_CucsBiosVIdentityParamsLsServerName_Type = SnmpAdminString
_CucsBiosVIdentityParamsLsServerName_Object = MibTableColumn
cucsBiosVIdentityParamsLsServerName = _CucsBiosVIdentityParamsLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 4),
    _CucsBiosVIdentityParamsLsServerName_Type()
)
cucsBiosVIdentityParamsLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsLsServerName.setStatus("current")
_CucsBiosVIdentityParamsLsServerTmplName_Type = SnmpAdminString
_CucsBiosVIdentityParamsLsServerTmplName_Object = MibTableColumn
cucsBiosVIdentityParamsLsServerTmplName = _CucsBiosVIdentityParamsLsServerTmplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 5),
    _CucsBiosVIdentityParamsLsServerTmplName_Type()
)
cucsBiosVIdentityParamsLsServerTmplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsLsServerTmplName.setStatus("current")
_CucsBiosVIdentityParamsSysName_Type = SnmpAdminString
_CucsBiosVIdentityParamsSysName_Object = MibTableColumn
cucsBiosVIdentityParamsSysName = _CucsBiosVIdentityParamsSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 51, 1, 6),
    _CucsBiosVIdentityParamsSysName_Type()
)
cucsBiosVIdentityParamsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVIdentityParamsSysName.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutTable_Object = MibTable
cucsBiosVfOSBootWatchdogTimerTimeoutTable = _CucsBiosVfOSBootWatchdogTimerTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52)
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutTable.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutEntry_Object = MibTableRow
cucsBiosVfOSBootWatchdogTimerTimeoutEntry = _CucsBiosVfOSBootWatchdogTimerTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1)
)
cucsBiosVfOSBootWatchdogTimerTimeoutEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutEntry.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId = _CucsBiosVfOSBootWatchdogTimerTimeoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 1),
    _CucsBiosVfOSBootWatchdogTimerTimeoutInstanceId_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutDn_Type = CucsManagedObjectDn
_CucsBiosVfOSBootWatchdogTimerTimeoutDn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutDn = _CucsBiosVfOSBootWatchdogTimerTimeoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 2),
    _CucsBiosVfOSBootWatchdogTimerTimeoutDn_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutDn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutRn_Type = SnmpAdminString
_CucsBiosVfOSBootWatchdogTimerTimeoutRn_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutRn = _CucsBiosVfOSBootWatchdogTimerTimeoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 3),
    _CucsBiosVfOSBootWatchdogTimerTimeoutRn_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutRn.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type = CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout
_CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout = _CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 4),
    _CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutPropAcl_Type = Unsigned64
_CucsBiosVfOSBootWatchdogTimerTimeoutPropAcl_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutPropAcl = _CucsBiosVfOSBootWatchdogTimerTimeoutPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 5),
    _CucsBiosVfOSBootWatchdogTimerTimeoutPropAcl_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutPropAcl.setStatus("current")
_CucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Object = MibTableColumn
cucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault = _CucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 52, 1, 6),
    _CucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault_Type()
)
cucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault.setStatus("current")
_CucsBiosVfOnboardStorageTable_Object = MibTable
cucsBiosVfOnboardStorageTable = _CucsBiosVfOnboardStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53)
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageTable.setStatus("current")
_CucsBiosVfOnboardStorageEntry_Object = MibTableRow
cucsBiosVfOnboardStorageEntry = _CucsBiosVfOnboardStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1)
)
cucsBiosVfOnboardStorageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOnboardStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageEntry.setStatus("current")
_CucsBiosVfOnboardStorageInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOnboardStorageInstanceId_Object = MibTableColumn
cucsBiosVfOnboardStorageInstanceId = _CucsBiosVfOnboardStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 1),
    _CucsBiosVfOnboardStorageInstanceId_Type()
)
cucsBiosVfOnboardStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageInstanceId.setStatus("current")
_CucsBiosVfOnboardStorageDn_Type = CucsManagedObjectDn
_CucsBiosVfOnboardStorageDn_Object = MibTableColumn
cucsBiosVfOnboardStorageDn = _CucsBiosVfOnboardStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 2),
    _CucsBiosVfOnboardStorageDn_Type()
)
cucsBiosVfOnboardStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageDn.setStatus("current")
_CucsBiosVfOnboardStorageRn_Type = SnmpAdminString
_CucsBiosVfOnboardStorageRn_Object = MibTableColumn
cucsBiosVfOnboardStorageRn = _CucsBiosVfOnboardStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 3),
    _CucsBiosVfOnboardStorageRn_Type()
)
cucsBiosVfOnboardStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageRn.setStatus("current")
_CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type = CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport
_CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object = MibTableColumn
cucsBiosVfOnboardStorageVpOnboardSCUStorageSupport = _CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 4),
    _CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport_Type()
)
cucsBiosVfOnboardStorageVpOnboardSCUStorageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageVpOnboardSCUStorageSupport.setStatus("current")
_CucsBiosVfOnboardStoragePropAcl_Type = Unsigned64
_CucsBiosVfOnboardStoragePropAcl_Object = MibTableColumn
cucsBiosVfOnboardStoragePropAcl = _CucsBiosVfOnboardStoragePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 5),
    _CucsBiosVfOnboardStoragePropAcl_Type()
)
cucsBiosVfOnboardStoragePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStoragePropAcl.setStatus("current")
_CucsBiosVfOnboardStorageSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOnboardStorageSupportedByDefault_Object = MibTableColumn
cucsBiosVfOnboardStorageSupportedByDefault = _CucsBiosVfOnboardStorageSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 53, 1, 6),
    _CucsBiosVfOnboardStorageSupportedByDefault_Type()
)
cucsBiosVfOnboardStorageSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardStorageSupportedByDefault.setStatus("current")
_CucsBiosVfOptionROMEnableTable_Object = MibTable
cucsBiosVfOptionROMEnableTable = _CucsBiosVfOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54)
)
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableTable.setStatus("current")
_CucsBiosVfOptionROMEnableEntry_Object = MibTableRow
cucsBiosVfOptionROMEnableEntry = _CucsBiosVfOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1)
)
cucsBiosVfOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableEntry.setStatus("current")
_CucsBiosVfOptionROMEnableInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOptionROMEnableInstanceId_Object = MibTableColumn
cucsBiosVfOptionROMEnableInstanceId = _CucsBiosVfOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 1),
    _CucsBiosVfOptionROMEnableInstanceId_Type()
)
cucsBiosVfOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableInstanceId.setStatus("current")
_CucsBiosVfOptionROMEnableDn_Type = CucsManagedObjectDn
_CucsBiosVfOptionROMEnableDn_Object = MibTableColumn
cucsBiosVfOptionROMEnableDn = _CucsBiosVfOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 2),
    _CucsBiosVfOptionROMEnableDn_Type()
)
cucsBiosVfOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableDn.setStatus("current")
_CucsBiosVfOptionROMEnableRn_Type = SnmpAdminString
_CucsBiosVfOptionROMEnableRn_Object = MibTableColumn
cucsBiosVfOptionROMEnableRn = _CucsBiosVfOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 3),
    _CucsBiosVfOptionROMEnableRn_Type()
)
cucsBiosVfOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableRn.setStatus("current")
_CucsBiosVfOptionROMEnableVpState_Type = CucsBiosVfOptionROMEnableVpState
_CucsBiosVfOptionROMEnableVpState_Object = MibTableColumn
cucsBiosVfOptionROMEnableVpState = _CucsBiosVfOptionROMEnableVpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 4),
    _CucsBiosVfOptionROMEnableVpState_Type()
)
cucsBiosVfOptionROMEnableVpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableVpState.setStatus("current")
_CucsBiosVfOptionROMEnablePropAcl_Type = Unsigned64
_CucsBiosVfOptionROMEnablePropAcl_Object = MibTableColumn
cucsBiosVfOptionROMEnablePropAcl = _CucsBiosVfOptionROMEnablePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 5),
    _CucsBiosVfOptionROMEnablePropAcl_Type()
)
cucsBiosVfOptionROMEnablePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnablePropAcl.setStatus("current")
_CucsBiosVfOptionROMEnableSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOptionROMEnableSupportedByDefault_Object = MibTableColumn
cucsBiosVfOptionROMEnableSupportedByDefault = _CucsBiosVfOptionROMEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 54, 1, 6),
    _CucsBiosVfOptionROMEnableSupportedByDefault_Type()
)
cucsBiosVfOptionROMEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOptionROMEnableSupportedByDefault.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableTable_Object = MibTable
cucsBiosVfPCISlotOptionROMEnableTable = _CucsBiosVfPCISlotOptionROMEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55)
)
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableTable.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableEntry_Object = MibTableRow
cucsBiosVfPCISlotOptionROMEnableEntry = _CucsBiosVfPCISlotOptionROMEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1)
)
cucsBiosVfPCISlotOptionROMEnableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPCISlotOptionROMEnableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableEntry.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPCISlotOptionROMEnableInstanceId_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableInstanceId = _CucsBiosVfPCISlotOptionROMEnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 1),
    _CucsBiosVfPCISlotOptionROMEnableInstanceId_Type()
)
cucsBiosVfPCISlotOptionROMEnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableInstanceId.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableDn_Type = CucsManagedObjectDn
_CucsBiosVfPCISlotOptionROMEnableDn_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableDn = _CucsBiosVfPCISlotOptionROMEnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 2),
    _CucsBiosVfPCISlotOptionROMEnableDn_Type()
)
cucsBiosVfPCISlotOptionROMEnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableDn.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableRn_Type = SnmpAdminString
_CucsBiosVfPCISlotOptionROMEnableRn_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableRn = _CucsBiosVfPCISlotOptionROMEnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 3),
    _CucsBiosVfPCISlotOptionROMEnableRn_Type()
)
cucsBiosVfPCISlotOptionROMEnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableRn.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot1State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot1State
_CucsBiosVfPCISlotOptionROMEnableVpSlot1State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot1State = _CucsBiosVfPCISlotOptionROMEnableVpSlot1State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 4),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot1State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot1State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot2State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot2State
_CucsBiosVfPCISlotOptionROMEnableVpSlot2State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot2State = _CucsBiosVfPCISlotOptionROMEnableVpSlot2State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 5),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot2State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot2State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot3State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot3State
_CucsBiosVfPCISlotOptionROMEnableVpSlot3State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot3State = _CucsBiosVfPCISlotOptionROMEnableVpSlot3State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 6),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot3State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot3State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot4State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot4State
_CucsBiosVfPCISlotOptionROMEnableVpSlot4State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot4State = _CucsBiosVfPCISlotOptionROMEnableVpSlot4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 7),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot4State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot4State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot5State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot5State
_CucsBiosVfPCISlotOptionROMEnableVpSlot5State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot5State = _CucsBiosVfPCISlotOptionROMEnableVpSlot5State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 8),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot5State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot5State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type = CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState
_CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlotMezzState = _CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 9),
    _CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlotMezzState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlotMezzState.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot6State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot6State
_CucsBiosVfPCISlotOptionROMEnableVpSlot6State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot6State = _CucsBiosVfPCISlotOptionROMEnableVpSlot6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 10),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot6State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot6State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot7State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot7State
_CucsBiosVfPCISlotOptionROMEnableVpSlot7State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot7State = _CucsBiosVfPCISlotOptionROMEnableVpSlot7State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 11),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot7State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot7State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type = CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM = _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 12),
    _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot10State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot10State
_CucsBiosVfPCISlotOptionROMEnableVpSlot10State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot10State = _CucsBiosVfPCISlotOptionROMEnableVpSlot10State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 13),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot10State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot10State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot8State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot8State
_CucsBiosVfPCISlotOptionROMEnableVpSlot8State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot8State = _CucsBiosVfPCISlotOptionROMEnableVpSlot8State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 14),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot8State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot8State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpSlot9State_Type = CucsBiosVfPCISlotOptionROMEnableVpSlot9State
_CucsBiosVfPCISlotOptionROMEnableVpSlot9State_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpSlot9State = _CucsBiosVfPCISlotOptionROMEnableVpSlot9State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 15),
    _CucsBiosVfPCISlotOptionROMEnableVpSlot9State_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpSlot9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpSlot9State.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type = CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM = _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 16),
    _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type = CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM = _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 17),
    _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type = CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM = _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 18),
    _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type = CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM
_CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM = _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 19),
    _CucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM_Type()
)
cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnablePropAcl_Type = Unsigned64
_CucsBiosVfPCISlotOptionROMEnablePropAcl_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnablePropAcl = _CucsBiosVfPCISlotOptionROMEnablePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 20),
    _CucsBiosVfPCISlotOptionROMEnablePropAcl_Type()
)
cucsBiosVfPCISlotOptionROMEnablePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnablePropAcl.setStatus("current")
_CucsBiosVfPCISlotOptionROMEnableSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPCISlotOptionROMEnableSupportedByDefault_Object = MibTableColumn
cucsBiosVfPCISlotOptionROMEnableSupportedByDefault = _CucsBiosVfPCISlotOptionROMEnableSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 55, 1, 21),
    _CucsBiosVfPCISlotOptionROMEnableSupportedByDefault_Type()
)
cucsBiosVfPCISlotOptionROMEnableSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotOptionROMEnableSupportedByDefault.setStatus("current")
_CucsBiosVfPackageCStateLimitTable_Object = MibTable
cucsBiosVfPackageCStateLimitTable = _CucsBiosVfPackageCStateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56)
)
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitTable.setStatus("current")
_CucsBiosVfPackageCStateLimitEntry_Object = MibTableRow
cucsBiosVfPackageCStateLimitEntry = _CucsBiosVfPackageCStateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1)
)
cucsBiosVfPackageCStateLimitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPackageCStateLimitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitEntry.setStatus("current")
_CucsBiosVfPackageCStateLimitInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPackageCStateLimitInstanceId_Object = MibTableColumn
cucsBiosVfPackageCStateLimitInstanceId = _CucsBiosVfPackageCStateLimitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 1),
    _CucsBiosVfPackageCStateLimitInstanceId_Type()
)
cucsBiosVfPackageCStateLimitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitInstanceId.setStatus("current")
_CucsBiosVfPackageCStateLimitDn_Type = CucsManagedObjectDn
_CucsBiosVfPackageCStateLimitDn_Object = MibTableColumn
cucsBiosVfPackageCStateLimitDn = _CucsBiosVfPackageCStateLimitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 2),
    _CucsBiosVfPackageCStateLimitDn_Type()
)
cucsBiosVfPackageCStateLimitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitDn.setStatus("current")
_CucsBiosVfPackageCStateLimitRn_Type = SnmpAdminString
_CucsBiosVfPackageCStateLimitRn_Object = MibTableColumn
cucsBiosVfPackageCStateLimitRn = _CucsBiosVfPackageCStateLimitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 3),
    _CucsBiosVfPackageCStateLimitRn_Type()
)
cucsBiosVfPackageCStateLimitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitRn.setStatus("current")
_CucsBiosVfPackageCStateLimitVpPackageCStateLimit_Type = CucsBiosVfPackageCStateLimitVpPackageCStateLimit
_CucsBiosVfPackageCStateLimitVpPackageCStateLimit_Object = MibTableColumn
cucsBiosVfPackageCStateLimitVpPackageCStateLimit = _CucsBiosVfPackageCStateLimitVpPackageCStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 4),
    _CucsBiosVfPackageCStateLimitVpPackageCStateLimit_Type()
)
cucsBiosVfPackageCStateLimitVpPackageCStateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitVpPackageCStateLimit.setStatus("current")
_CucsBiosVfPackageCStateLimitPropAcl_Type = Unsigned64
_CucsBiosVfPackageCStateLimitPropAcl_Object = MibTableColumn
cucsBiosVfPackageCStateLimitPropAcl = _CucsBiosVfPackageCStateLimitPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 5),
    _CucsBiosVfPackageCStateLimitPropAcl_Type()
)
cucsBiosVfPackageCStateLimitPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitPropAcl.setStatus("current")
_CucsBiosVfPackageCStateLimitSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPackageCStateLimitSupportedByDefault_Object = MibTableColumn
cucsBiosVfPackageCStateLimitSupportedByDefault = _CucsBiosVfPackageCStateLimitSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 56, 1, 6),
    _CucsBiosVfPackageCStateLimitSupportedByDefault_Type()
)
cucsBiosVfPackageCStateLimitSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPackageCStateLimitSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorC1ETable_Object = MibTable
cucsBiosVfProcessorC1ETable = _CucsBiosVfProcessorC1ETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1ETable.setStatus("current")
_CucsBiosVfProcessorC1EEntry_Object = MibTableRow
cucsBiosVfProcessorC1EEntry = _CucsBiosVfProcessorC1EEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1)
)
cucsBiosVfProcessorC1EEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorC1EInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1EEntry.setStatus("current")
_CucsBiosVfProcessorC1EInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorC1EInstanceId_Object = MibTableColumn
cucsBiosVfProcessorC1EInstanceId = _CucsBiosVfProcessorC1EInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 1),
    _CucsBiosVfProcessorC1EInstanceId_Type()
)
cucsBiosVfProcessorC1EInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1EInstanceId.setStatus("current")
_CucsBiosVfProcessorC1EDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorC1EDn_Object = MibTableColumn
cucsBiosVfProcessorC1EDn = _CucsBiosVfProcessorC1EDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 2),
    _CucsBiosVfProcessorC1EDn_Type()
)
cucsBiosVfProcessorC1EDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1EDn.setStatus("current")
_CucsBiosVfProcessorC1ERn_Type = SnmpAdminString
_CucsBiosVfProcessorC1ERn_Object = MibTableColumn
cucsBiosVfProcessorC1ERn = _CucsBiosVfProcessorC1ERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 3),
    _CucsBiosVfProcessorC1ERn_Type()
)
cucsBiosVfProcessorC1ERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1ERn.setStatus("current")
_CucsBiosVfProcessorC1EVpProcessorC1E_Type = CucsBiosVfProcessorC1EVpProcessorC1E
_CucsBiosVfProcessorC1EVpProcessorC1E_Object = MibTableColumn
cucsBiosVfProcessorC1EVpProcessorC1E = _CucsBiosVfProcessorC1EVpProcessorC1E_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 4),
    _CucsBiosVfProcessorC1EVpProcessorC1E_Type()
)
cucsBiosVfProcessorC1EVpProcessorC1E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1EVpProcessorC1E.setStatus("current")
_CucsBiosVfProcessorC1EPropAcl_Type = Unsigned64
_CucsBiosVfProcessorC1EPropAcl_Object = MibTableColumn
cucsBiosVfProcessorC1EPropAcl = _CucsBiosVfProcessorC1EPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 5),
    _CucsBiosVfProcessorC1EPropAcl_Type()
)
cucsBiosVfProcessorC1EPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1EPropAcl.setStatus("current")
_CucsBiosVfProcessorC1ESupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorC1ESupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorC1ESupportedByDefault = _CucsBiosVfProcessorC1ESupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 57, 1, 6),
    _CucsBiosVfProcessorC1ESupportedByDefault_Type()
)
cucsBiosVfProcessorC1ESupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC1ESupportedByDefault.setStatus("current")
_CucsBiosVfProcessorC7ReportTable_Object = MibTable
cucsBiosVfProcessorC7ReportTable = _CucsBiosVfProcessorC7ReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportTable.setStatus("current")
_CucsBiosVfProcessorC7ReportEntry_Object = MibTableRow
cucsBiosVfProcessorC7ReportEntry = _CucsBiosVfProcessorC7ReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1)
)
cucsBiosVfProcessorC7ReportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorC7ReportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportEntry.setStatus("current")
_CucsBiosVfProcessorC7ReportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorC7ReportInstanceId_Object = MibTableColumn
cucsBiosVfProcessorC7ReportInstanceId = _CucsBiosVfProcessorC7ReportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 1),
    _CucsBiosVfProcessorC7ReportInstanceId_Type()
)
cucsBiosVfProcessorC7ReportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportInstanceId.setStatus("current")
_CucsBiosVfProcessorC7ReportDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorC7ReportDn_Object = MibTableColumn
cucsBiosVfProcessorC7ReportDn = _CucsBiosVfProcessorC7ReportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 2),
    _CucsBiosVfProcessorC7ReportDn_Type()
)
cucsBiosVfProcessorC7ReportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportDn.setStatus("current")
_CucsBiosVfProcessorC7ReportRn_Type = SnmpAdminString
_CucsBiosVfProcessorC7ReportRn_Object = MibTableColumn
cucsBiosVfProcessorC7ReportRn = _CucsBiosVfProcessorC7ReportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 3),
    _CucsBiosVfProcessorC7ReportRn_Type()
)
cucsBiosVfProcessorC7ReportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportRn.setStatus("current")
_CucsBiosVfProcessorC7ReportVpProcessorC7Report_Type = CucsBiosVfProcessorC7ReportVpProcessorC7Report
_CucsBiosVfProcessorC7ReportVpProcessorC7Report_Object = MibTableColumn
cucsBiosVfProcessorC7ReportVpProcessorC7Report = _CucsBiosVfProcessorC7ReportVpProcessorC7Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 4),
    _CucsBiosVfProcessorC7ReportVpProcessorC7Report_Type()
)
cucsBiosVfProcessorC7ReportVpProcessorC7Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportVpProcessorC7Report.setStatus("current")
_CucsBiosVfProcessorC7ReportPropAcl_Type = Unsigned64
_CucsBiosVfProcessorC7ReportPropAcl_Object = MibTableColumn
cucsBiosVfProcessorC7ReportPropAcl = _CucsBiosVfProcessorC7ReportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 5),
    _CucsBiosVfProcessorC7ReportPropAcl_Type()
)
cucsBiosVfProcessorC7ReportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportPropAcl.setStatus("current")
_CucsBiosVfProcessorC7ReportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorC7ReportSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorC7ReportSupportedByDefault = _CucsBiosVfProcessorC7ReportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 58, 1, 6),
    _CucsBiosVfProcessorC7ReportSupportedByDefault_Type()
)
cucsBiosVfProcessorC7ReportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorC7ReportSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorCStateTable_Object = MibTable
cucsBiosVfProcessorCStateTable = _CucsBiosVfProcessorCStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateTable.setStatus("current")
_CucsBiosVfProcessorCStateEntry_Object = MibTableRow
cucsBiosVfProcessorCStateEntry = _CucsBiosVfProcessorCStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1)
)
cucsBiosVfProcessorCStateEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorCStateInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateEntry.setStatus("current")
_CucsBiosVfProcessorCStateInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorCStateInstanceId_Object = MibTableColumn
cucsBiosVfProcessorCStateInstanceId = _CucsBiosVfProcessorCStateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 1),
    _CucsBiosVfProcessorCStateInstanceId_Type()
)
cucsBiosVfProcessorCStateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateInstanceId.setStatus("current")
_CucsBiosVfProcessorCStateDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorCStateDn_Object = MibTableColumn
cucsBiosVfProcessorCStateDn = _CucsBiosVfProcessorCStateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 2),
    _CucsBiosVfProcessorCStateDn_Type()
)
cucsBiosVfProcessorCStateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateDn.setStatus("current")
_CucsBiosVfProcessorCStateRn_Type = SnmpAdminString
_CucsBiosVfProcessorCStateRn_Object = MibTableColumn
cucsBiosVfProcessorCStateRn = _CucsBiosVfProcessorCStateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 3),
    _CucsBiosVfProcessorCStateRn_Type()
)
cucsBiosVfProcessorCStateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateRn.setStatus("current")
_CucsBiosVfProcessorCStateVpProcessorCState_Type = CucsBiosVfProcessorCStateVpProcessorCState
_CucsBiosVfProcessorCStateVpProcessorCState_Object = MibTableColumn
cucsBiosVfProcessorCStateVpProcessorCState = _CucsBiosVfProcessorCStateVpProcessorCState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 4),
    _CucsBiosVfProcessorCStateVpProcessorCState_Type()
)
cucsBiosVfProcessorCStateVpProcessorCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateVpProcessorCState.setStatus("current")
_CucsBiosVfProcessorCStatePropAcl_Type = Unsigned64
_CucsBiosVfProcessorCStatePropAcl_Object = MibTableColumn
cucsBiosVfProcessorCStatePropAcl = _CucsBiosVfProcessorCStatePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 5),
    _CucsBiosVfProcessorCStatePropAcl_Type()
)
cucsBiosVfProcessorCStatePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStatePropAcl.setStatus("current")
_CucsBiosVfProcessorCStateSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorCStateSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorCStateSupportedByDefault = _CucsBiosVfProcessorCStateSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 59, 1, 6),
    _CucsBiosVfProcessorCStateSupportedByDefault_Type()
)
cucsBiosVfProcessorCStateSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorCStateSupportedByDefault.setStatus("current")
_CucsBiosVfSriovConfigTable_Object = MibTable
cucsBiosVfSriovConfigTable = _CucsBiosVfSriovConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60)
)
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigTable.setStatus("current")
_CucsBiosVfSriovConfigEntry_Object = MibTableRow
cucsBiosVfSriovConfigEntry = _CucsBiosVfSriovConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1)
)
cucsBiosVfSriovConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfSriovConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigEntry.setStatus("current")
_CucsBiosVfSriovConfigInstanceId_Type = CucsManagedObjectId
_CucsBiosVfSriovConfigInstanceId_Object = MibTableColumn
cucsBiosVfSriovConfigInstanceId = _CucsBiosVfSriovConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 1),
    _CucsBiosVfSriovConfigInstanceId_Type()
)
cucsBiosVfSriovConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigInstanceId.setStatus("current")
_CucsBiosVfSriovConfigDn_Type = CucsManagedObjectDn
_CucsBiosVfSriovConfigDn_Object = MibTableColumn
cucsBiosVfSriovConfigDn = _CucsBiosVfSriovConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 2),
    _CucsBiosVfSriovConfigDn_Type()
)
cucsBiosVfSriovConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigDn.setStatus("current")
_CucsBiosVfSriovConfigRn_Type = SnmpAdminString
_CucsBiosVfSriovConfigRn_Object = MibTableColumn
cucsBiosVfSriovConfigRn = _CucsBiosVfSriovConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 3),
    _CucsBiosVfSriovConfigRn_Type()
)
cucsBiosVfSriovConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigRn.setStatus("current")
_CucsBiosVfSriovConfigVpSriov_Type = CucsBiosVfSriovConfigVpSriov
_CucsBiosVfSriovConfigVpSriov_Object = MibTableColumn
cucsBiosVfSriovConfigVpSriov = _CucsBiosVfSriovConfigVpSriov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 4),
    _CucsBiosVfSriovConfigVpSriov_Type()
)
cucsBiosVfSriovConfigVpSriov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigVpSriov.setStatus("current")
_CucsBiosVfSriovConfigPropAcl_Type = Unsigned64
_CucsBiosVfSriovConfigPropAcl_Object = MibTableColumn
cucsBiosVfSriovConfigPropAcl = _CucsBiosVfSriovConfigPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 5),
    _CucsBiosVfSriovConfigPropAcl_Type()
)
cucsBiosVfSriovConfigPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigPropAcl.setStatus("current")
_CucsBiosVfSriovConfigSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfSriovConfigSupportedByDefault_Object = MibTableColumn
cucsBiosVfSriovConfigSupportedByDefault = _CucsBiosVfSriovConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 60, 1, 6),
    _CucsBiosVfSriovConfigSupportedByDefault_Type()
)
cucsBiosVfSriovConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfSriovConfigSupportedByDefault.setStatus("current")
_CucsBiosVfDramRefreshRateTable_Object = MibTable
cucsBiosVfDramRefreshRateTable = _CucsBiosVfDramRefreshRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61)
)
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateTable.setStatus("current")
_CucsBiosVfDramRefreshRateEntry_Object = MibTableRow
cucsBiosVfDramRefreshRateEntry = _CucsBiosVfDramRefreshRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1)
)
cucsBiosVfDramRefreshRateEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfDramRefreshRateInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateEntry.setStatus("current")
_CucsBiosVfDramRefreshRateInstanceId_Type = CucsManagedObjectId
_CucsBiosVfDramRefreshRateInstanceId_Object = MibTableColumn
cucsBiosVfDramRefreshRateInstanceId = _CucsBiosVfDramRefreshRateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 1),
    _CucsBiosVfDramRefreshRateInstanceId_Type()
)
cucsBiosVfDramRefreshRateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateInstanceId.setStatus("current")
_CucsBiosVfDramRefreshRateDn_Type = CucsManagedObjectDn
_CucsBiosVfDramRefreshRateDn_Object = MibTableColumn
cucsBiosVfDramRefreshRateDn = _CucsBiosVfDramRefreshRateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 2),
    _CucsBiosVfDramRefreshRateDn_Type()
)
cucsBiosVfDramRefreshRateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateDn.setStatus("current")
_CucsBiosVfDramRefreshRateRn_Type = SnmpAdminString
_CucsBiosVfDramRefreshRateRn_Object = MibTableColumn
cucsBiosVfDramRefreshRateRn = _CucsBiosVfDramRefreshRateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 3),
    _CucsBiosVfDramRefreshRateRn_Type()
)
cucsBiosVfDramRefreshRateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateRn.setStatus("current")
_CucsBiosVfDramRefreshRateVpDramRefreshRate_Type = CucsBiosVfDramRefreshRateVpDramRefreshRate
_CucsBiosVfDramRefreshRateVpDramRefreshRate_Object = MibTableColumn
cucsBiosVfDramRefreshRateVpDramRefreshRate = _CucsBiosVfDramRefreshRateVpDramRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 4),
    _CucsBiosVfDramRefreshRateVpDramRefreshRate_Type()
)
cucsBiosVfDramRefreshRateVpDramRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateVpDramRefreshRate.setStatus("current")
_CucsBiosVfDramRefreshRatePropAcl_Type = Unsigned64
_CucsBiosVfDramRefreshRatePropAcl_Object = MibTableColumn
cucsBiosVfDramRefreshRatePropAcl = _CucsBiosVfDramRefreshRatePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 5),
    _CucsBiosVfDramRefreshRatePropAcl_Type()
)
cucsBiosVfDramRefreshRatePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRatePropAcl.setStatus("current")
_CucsBiosVfDramRefreshRateSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfDramRefreshRateSupportedByDefault_Object = MibTableColumn
cucsBiosVfDramRefreshRateSupportedByDefault = _CucsBiosVfDramRefreshRateSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 61, 1, 6),
    _CucsBiosVfDramRefreshRateSupportedByDefault_Type()
)
cucsBiosVfDramRefreshRateSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDramRefreshRateSupportedByDefault.setStatus("current")
_CucsBiosVfLocalX2ApicTable_Object = MibTable
cucsBiosVfLocalX2ApicTable = _CucsBiosVfLocalX2ApicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62)
)
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicTable.setStatus("current")
_CucsBiosVfLocalX2ApicEntry_Object = MibTableRow
cucsBiosVfLocalX2ApicEntry = _CucsBiosVfLocalX2ApicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1)
)
cucsBiosVfLocalX2ApicEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfLocalX2ApicInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicEntry.setStatus("current")
_CucsBiosVfLocalX2ApicInstanceId_Type = CucsManagedObjectId
_CucsBiosVfLocalX2ApicInstanceId_Object = MibTableColumn
cucsBiosVfLocalX2ApicInstanceId = _CucsBiosVfLocalX2ApicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 1),
    _CucsBiosVfLocalX2ApicInstanceId_Type()
)
cucsBiosVfLocalX2ApicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicInstanceId.setStatus("current")
_CucsBiosVfLocalX2ApicDn_Type = CucsManagedObjectDn
_CucsBiosVfLocalX2ApicDn_Object = MibTableColumn
cucsBiosVfLocalX2ApicDn = _CucsBiosVfLocalX2ApicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 2),
    _CucsBiosVfLocalX2ApicDn_Type()
)
cucsBiosVfLocalX2ApicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicDn.setStatus("current")
_CucsBiosVfLocalX2ApicRn_Type = SnmpAdminString
_CucsBiosVfLocalX2ApicRn_Object = MibTableColumn
cucsBiosVfLocalX2ApicRn = _CucsBiosVfLocalX2ApicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 3),
    _CucsBiosVfLocalX2ApicRn_Type()
)
cucsBiosVfLocalX2ApicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicRn.setStatus("current")
_CucsBiosVfLocalX2ApicVpLocalX2Apic_Type = CucsBiosVfLocalX2ApicVpLocalX2Apic
_CucsBiosVfLocalX2ApicVpLocalX2Apic_Object = MibTableColumn
cucsBiosVfLocalX2ApicVpLocalX2Apic = _CucsBiosVfLocalX2ApicVpLocalX2Apic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 4),
    _CucsBiosVfLocalX2ApicVpLocalX2Apic_Type()
)
cucsBiosVfLocalX2ApicVpLocalX2Apic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicVpLocalX2Apic.setStatus("current")
_CucsBiosVfLocalX2ApicPropAcl_Type = Unsigned64
_CucsBiosVfLocalX2ApicPropAcl_Object = MibTableColumn
cucsBiosVfLocalX2ApicPropAcl = _CucsBiosVfLocalX2ApicPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 5),
    _CucsBiosVfLocalX2ApicPropAcl_Type()
)
cucsBiosVfLocalX2ApicPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicPropAcl.setStatus("current")
_CucsBiosVfLocalX2ApicSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfLocalX2ApicSupportedByDefault_Object = MibTableColumn
cucsBiosVfLocalX2ApicSupportedByDefault = _CucsBiosVfLocalX2ApicSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 62, 1, 6),
    _CucsBiosVfLocalX2ApicSupportedByDefault_Type()
)
cucsBiosVfLocalX2ApicSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfLocalX2ApicSupportedByDefault.setStatus("current")
_CucsBiosVfUCSMBootModeControlTable_Object = MibTable
cucsBiosVfUCSMBootModeControlTable = _CucsBiosVfUCSMBootModeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63)
)
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlTable.setStatus("current")
_CucsBiosVfUCSMBootModeControlEntry_Object = MibTableRow
cucsBiosVfUCSMBootModeControlEntry = _CucsBiosVfUCSMBootModeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1)
)
cucsBiosVfUCSMBootModeControlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUCSMBootModeControlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlEntry.setStatus("current")
_CucsBiosVfUCSMBootModeControlInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUCSMBootModeControlInstanceId_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlInstanceId = _CucsBiosVfUCSMBootModeControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 1),
    _CucsBiosVfUCSMBootModeControlInstanceId_Type()
)
cucsBiosVfUCSMBootModeControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlInstanceId.setStatus("current")
_CucsBiosVfUCSMBootModeControlDn_Type = CucsManagedObjectDn
_CucsBiosVfUCSMBootModeControlDn_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlDn = _CucsBiosVfUCSMBootModeControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 2),
    _CucsBiosVfUCSMBootModeControlDn_Type()
)
cucsBiosVfUCSMBootModeControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlDn.setStatus("current")
_CucsBiosVfUCSMBootModeControlRn_Type = SnmpAdminString
_CucsBiosVfUCSMBootModeControlRn_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlRn = _CucsBiosVfUCSMBootModeControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 3),
    _CucsBiosVfUCSMBootModeControlRn_Type()
)
cucsBiosVfUCSMBootModeControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlRn.setStatus("current")
_CucsBiosVfUCSMBootModeControlVpUEFIBootMode_Type = CucsBiosVfUCSMBootModeControlVpUEFIBootMode
_CucsBiosVfUCSMBootModeControlVpUEFIBootMode_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlVpUEFIBootMode = _CucsBiosVfUCSMBootModeControlVpUEFIBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 4),
    _CucsBiosVfUCSMBootModeControlVpUEFIBootMode_Type()
)
cucsBiosVfUCSMBootModeControlVpUEFIBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlVpUEFIBootMode.setStatus("current")
_CucsBiosVfUCSMBootModeControlPropAcl_Type = Unsigned64
_CucsBiosVfUCSMBootModeControlPropAcl_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlPropAcl = _CucsBiosVfUCSMBootModeControlPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 5),
    _CucsBiosVfUCSMBootModeControlPropAcl_Type()
)
cucsBiosVfUCSMBootModeControlPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlPropAcl.setStatus("current")
_CucsBiosVfUCSMBootModeControlSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUCSMBootModeControlSupportedByDefault_Object = MibTableColumn
cucsBiosVfUCSMBootModeControlSupportedByDefault = _CucsBiosVfUCSMBootModeControlSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 63, 1, 6),
    _CucsBiosVfUCSMBootModeControlSupportedByDefault_Type()
)
cucsBiosVfUCSMBootModeControlSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUCSMBootModeControlSupportedByDefault.setStatus("current")
_CucsBiosVfAllUSBDevicesTable_Object = MibTable
cucsBiosVfAllUSBDevicesTable = _CucsBiosVfAllUSBDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64)
)
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesTable.setStatus("current")
_CucsBiosVfAllUSBDevicesEntry_Object = MibTableRow
cucsBiosVfAllUSBDevicesEntry = _CucsBiosVfAllUSBDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1)
)
cucsBiosVfAllUSBDevicesEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfAllUSBDevicesInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesEntry.setStatus("current")
_CucsBiosVfAllUSBDevicesInstanceId_Type = CucsManagedObjectId
_CucsBiosVfAllUSBDevicesInstanceId_Object = MibTableColumn
cucsBiosVfAllUSBDevicesInstanceId = _CucsBiosVfAllUSBDevicesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 1),
    _CucsBiosVfAllUSBDevicesInstanceId_Type()
)
cucsBiosVfAllUSBDevicesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesInstanceId.setStatus("current")
_CucsBiosVfAllUSBDevicesDn_Type = CucsManagedObjectDn
_CucsBiosVfAllUSBDevicesDn_Object = MibTableColumn
cucsBiosVfAllUSBDevicesDn = _CucsBiosVfAllUSBDevicesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 2),
    _CucsBiosVfAllUSBDevicesDn_Type()
)
cucsBiosVfAllUSBDevicesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesDn.setStatus("current")
_CucsBiosVfAllUSBDevicesRn_Type = SnmpAdminString
_CucsBiosVfAllUSBDevicesRn_Object = MibTableColumn
cucsBiosVfAllUSBDevicesRn = _CucsBiosVfAllUSBDevicesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 3),
    _CucsBiosVfAllUSBDevicesRn_Type()
)
cucsBiosVfAllUSBDevicesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesRn.setStatus("current")
_CucsBiosVfAllUSBDevicesVpAllUSBDevices_Type = CucsBiosVfAllUSBDevicesVpAllUSBDevices
_CucsBiosVfAllUSBDevicesVpAllUSBDevices_Object = MibTableColumn
cucsBiosVfAllUSBDevicesVpAllUSBDevices = _CucsBiosVfAllUSBDevicesVpAllUSBDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 4),
    _CucsBiosVfAllUSBDevicesVpAllUSBDevices_Type()
)
cucsBiosVfAllUSBDevicesVpAllUSBDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesVpAllUSBDevices.setStatus("current")
_CucsBiosVfAllUSBDevicesPropAcl_Type = Unsigned64
_CucsBiosVfAllUSBDevicesPropAcl_Object = MibTableColumn
cucsBiosVfAllUSBDevicesPropAcl = _CucsBiosVfAllUSBDevicesPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 5),
    _CucsBiosVfAllUSBDevicesPropAcl_Type()
)
cucsBiosVfAllUSBDevicesPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesPropAcl.setStatus("current")
_CucsBiosVfAllUSBDevicesSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfAllUSBDevicesSupportedByDefault_Object = MibTableColumn
cucsBiosVfAllUSBDevicesSupportedByDefault = _CucsBiosVfAllUSBDevicesSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 64, 1, 6),
    _CucsBiosVfAllUSBDevicesSupportedByDefault_Type()
)
cucsBiosVfAllUSBDevicesSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAllUSBDevicesSupportedByDefault.setStatus("current")
_CucsBiosVfDRAMClockThrottlingTable_Object = MibTable
cucsBiosVfDRAMClockThrottlingTable = _CucsBiosVfDRAMClockThrottlingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65)
)
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingTable.setStatus("current")
_CucsBiosVfDRAMClockThrottlingEntry_Object = MibTableRow
cucsBiosVfDRAMClockThrottlingEntry = _CucsBiosVfDRAMClockThrottlingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1)
)
cucsBiosVfDRAMClockThrottlingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfDRAMClockThrottlingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingEntry.setStatus("current")
_CucsBiosVfDRAMClockThrottlingInstanceId_Type = CucsManagedObjectId
_CucsBiosVfDRAMClockThrottlingInstanceId_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingInstanceId = _CucsBiosVfDRAMClockThrottlingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 1),
    _CucsBiosVfDRAMClockThrottlingInstanceId_Type()
)
cucsBiosVfDRAMClockThrottlingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingInstanceId.setStatus("current")
_CucsBiosVfDRAMClockThrottlingDn_Type = CucsManagedObjectDn
_CucsBiosVfDRAMClockThrottlingDn_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingDn = _CucsBiosVfDRAMClockThrottlingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 2),
    _CucsBiosVfDRAMClockThrottlingDn_Type()
)
cucsBiosVfDRAMClockThrottlingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingDn.setStatus("current")
_CucsBiosVfDRAMClockThrottlingRn_Type = SnmpAdminString
_CucsBiosVfDRAMClockThrottlingRn_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingRn = _CucsBiosVfDRAMClockThrottlingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 3),
    _CucsBiosVfDRAMClockThrottlingRn_Type()
)
cucsBiosVfDRAMClockThrottlingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingRn.setStatus("current")
_CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type = CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling
_CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling = _CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 4),
    _CucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling_Type()
)
cucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling.setStatus("current")
_CucsBiosVfDRAMClockThrottlingPropAcl_Type = Unsigned64
_CucsBiosVfDRAMClockThrottlingPropAcl_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingPropAcl = _CucsBiosVfDRAMClockThrottlingPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 5),
    _CucsBiosVfDRAMClockThrottlingPropAcl_Type()
)
cucsBiosVfDRAMClockThrottlingPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingPropAcl.setStatus("current")
_CucsBiosVfDRAMClockThrottlingSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfDRAMClockThrottlingSupportedByDefault_Object = MibTableColumn
cucsBiosVfDRAMClockThrottlingSupportedByDefault = _CucsBiosVfDRAMClockThrottlingSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 65, 1, 6),
    _CucsBiosVfDRAMClockThrottlingSupportedByDefault_Type()
)
cucsBiosVfDRAMClockThrottlingSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDRAMClockThrottlingSupportedByDefault.setStatus("current")
_CucsBiosVfFRB2TimerTable_Object = MibTable
cucsBiosVfFRB2TimerTable = _CucsBiosVfFRB2TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66)
)
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerTable.setStatus("current")
_CucsBiosVfFRB2TimerEntry_Object = MibTableRow
cucsBiosVfFRB2TimerEntry = _CucsBiosVfFRB2TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1)
)
cucsBiosVfFRB2TimerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfFRB2TimerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerEntry.setStatus("current")
_CucsBiosVfFRB2TimerInstanceId_Type = CucsManagedObjectId
_CucsBiosVfFRB2TimerInstanceId_Object = MibTableColumn
cucsBiosVfFRB2TimerInstanceId = _CucsBiosVfFRB2TimerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 1),
    _CucsBiosVfFRB2TimerInstanceId_Type()
)
cucsBiosVfFRB2TimerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerInstanceId.setStatus("current")
_CucsBiosVfFRB2TimerDn_Type = CucsManagedObjectDn
_CucsBiosVfFRB2TimerDn_Object = MibTableColumn
cucsBiosVfFRB2TimerDn = _CucsBiosVfFRB2TimerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 2),
    _CucsBiosVfFRB2TimerDn_Type()
)
cucsBiosVfFRB2TimerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerDn.setStatus("current")
_CucsBiosVfFRB2TimerRn_Type = SnmpAdminString
_CucsBiosVfFRB2TimerRn_Object = MibTableColumn
cucsBiosVfFRB2TimerRn = _CucsBiosVfFRB2TimerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 3),
    _CucsBiosVfFRB2TimerRn_Type()
)
cucsBiosVfFRB2TimerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerRn.setStatus("current")
_CucsBiosVfFRB2TimerVpFRB2Timer_Type = CucsBiosVfFRB2TimerVpFRB2Timer
_CucsBiosVfFRB2TimerVpFRB2Timer_Object = MibTableColumn
cucsBiosVfFRB2TimerVpFRB2Timer = _CucsBiosVfFRB2TimerVpFRB2Timer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 4),
    _CucsBiosVfFRB2TimerVpFRB2Timer_Type()
)
cucsBiosVfFRB2TimerVpFRB2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerVpFRB2Timer.setStatus("current")
_CucsBiosVfFRB2TimerPropAcl_Type = Unsigned64
_CucsBiosVfFRB2TimerPropAcl_Object = MibTableColumn
cucsBiosVfFRB2TimerPropAcl = _CucsBiosVfFRB2TimerPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 5),
    _CucsBiosVfFRB2TimerPropAcl_Type()
)
cucsBiosVfFRB2TimerPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerPropAcl.setStatus("current")
_CucsBiosVfFRB2TimerSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfFRB2TimerSupportedByDefault_Object = MibTableColumn
cucsBiosVfFRB2TimerSupportedByDefault = _CucsBiosVfFRB2TimerSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 66, 1, 6),
    _CucsBiosVfFRB2TimerSupportedByDefault_Type()
)
cucsBiosVfFRB2TimerSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFRB2TimerSupportedByDefault.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideTable_Object = MibTable
cucsBiosVfFrequencyFloorOverrideTable = _CucsBiosVfFrequencyFloorOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67)
)
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideTable.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideEntry_Object = MibTableRow
cucsBiosVfFrequencyFloorOverrideEntry = _CucsBiosVfFrequencyFloorOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1)
)
cucsBiosVfFrequencyFloorOverrideEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfFrequencyFloorOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideEntry.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideInstanceId_Type = CucsManagedObjectId
_CucsBiosVfFrequencyFloorOverrideInstanceId_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverrideInstanceId = _CucsBiosVfFrequencyFloorOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 1),
    _CucsBiosVfFrequencyFloorOverrideInstanceId_Type()
)
cucsBiosVfFrequencyFloorOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideInstanceId.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideDn_Type = CucsManagedObjectDn
_CucsBiosVfFrequencyFloorOverrideDn_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverrideDn = _CucsBiosVfFrequencyFloorOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 2),
    _CucsBiosVfFrequencyFloorOverrideDn_Type()
)
cucsBiosVfFrequencyFloorOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideDn.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideRn_Type = SnmpAdminString
_CucsBiosVfFrequencyFloorOverrideRn_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverrideRn = _CucsBiosVfFrequencyFloorOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 3),
    _CucsBiosVfFrequencyFloorOverrideRn_Type()
)
cucsBiosVfFrequencyFloorOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideRn.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type = CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride
_CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride = _CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 4),
    _CucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride_Type()
)
cucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride.setStatus("current")
_CucsBiosVfFrequencyFloorOverridePropAcl_Type = Unsigned64
_CucsBiosVfFrequencyFloorOverridePropAcl_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverridePropAcl = _CucsBiosVfFrequencyFloorOverridePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 5),
    _CucsBiosVfFrequencyFloorOverridePropAcl_Type()
)
cucsBiosVfFrequencyFloorOverridePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverridePropAcl.setStatus("current")
_CucsBiosVfFrequencyFloorOverrideSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfFrequencyFloorOverrideSupportedByDefault_Object = MibTableColumn
cucsBiosVfFrequencyFloorOverrideSupportedByDefault = _CucsBiosVfFrequencyFloorOverrideSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 67, 1, 6),
    _CucsBiosVfFrequencyFloorOverrideSupportedByDefault_Type()
)
cucsBiosVfFrequencyFloorOverrideSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfFrequencyFloorOverrideSupportedByDefault.setStatus("current")
_CucsBiosVfInterleaveConfigurationTable_Object = MibTable
cucsBiosVfInterleaveConfigurationTable = _CucsBiosVfInterleaveConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68)
)
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationTable.setStatus("current")
_CucsBiosVfInterleaveConfigurationEntry_Object = MibTableRow
cucsBiosVfInterleaveConfigurationEntry = _CucsBiosVfInterleaveConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1)
)
cucsBiosVfInterleaveConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfInterleaveConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationEntry.setStatus("current")
_CucsBiosVfInterleaveConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfInterleaveConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationInstanceId = _CucsBiosVfInterleaveConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 1),
    _CucsBiosVfInterleaveConfigurationInstanceId_Type()
)
cucsBiosVfInterleaveConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationInstanceId.setStatus("current")
_CucsBiosVfInterleaveConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfInterleaveConfigurationDn_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationDn = _CucsBiosVfInterleaveConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 2),
    _CucsBiosVfInterleaveConfigurationDn_Type()
)
cucsBiosVfInterleaveConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationDn.setStatus("current")
_CucsBiosVfInterleaveConfigurationRn_Type = SnmpAdminString
_CucsBiosVfInterleaveConfigurationRn_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationRn = _CucsBiosVfInterleaveConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 3),
    _CucsBiosVfInterleaveConfigurationRn_Type()
)
cucsBiosVfInterleaveConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationRn.setStatus("current")
_CucsBiosVfInterleaveConfigurationVpChannelInterleaving_Type = CucsBiosVfInterleaveConfigurationVpChannelInterleaving
_CucsBiosVfInterleaveConfigurationVpChannelInterleaving_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationVpChannelInterleaving = _CucsBiosVfInterleaveConfigurationVpChannelInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 4),
    _CucsBiosVfInterleaveConfigurationVpChannelInterleaving_Type()
)
cucsBiosVfInterleaveConfigurationVpChannelInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationVpChannelInterleaving.setStatus("current")
_CucsBiosVfInterleaveConfigurationVpMemoryInterleaving_Type = CucsBiosVfInterleaveConfigurationVpMemoryInterleaving
_CucsBiosVfInterleaveConfigurationVpMemoryInterleaving_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationVpMemoryInterleaving = _CucsBiosVfInterleaveConfigurationVpMemoryInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 5),
    _CucsBiosVfInterleaveConfigurationVpMemoryInterleaving_Type()
)
cucsBiosVfInterleaveConfigurationVpMemoryInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationVpMemoryInterleaving.setStatus("current")
_CucsBiosVfInterleaveConfigurationVpRankInterleaving_Type = CucsBiosVfInterleaveConfigurationVpRankInterleaving
_CucsBiosVfInterleaveConfigurationVpRankInterleaving_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationVpRankInterleaving = _CucsBiosVfInterleaveConfigurationVpRankInterleaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 6),
    _CucsBiosVfInterleaveConfigurationVpRankInterleaving_Type()
)
cucsBiosVfInterleaveConfigurationVpRankInterleaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationVpRankInterleaving.setStatus("current")
_CucsBiosVfInterleaveConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfInterleaveConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationPropAcl = _CucsBiosVfInterleaveConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 7),
    _CucsBiosVfInterleaveConfigurationPropAcl_Type()
)
cucsBiosVfInterleaveConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationPropAcl.setStatus("current")
_CucsBiosVfInterleaveConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfInterleaveConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfInterleaveConfigurationSupportedByDefault = _CucsBiosVfInterleaveConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 68, 1, 8),
    _CucsBiosVfInterleaveConfigurationSupportedByDefault_Type()
)
cucsBiosVfInterleaveConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfInterleaveConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedTable_Object = MibTable
cucsBiosVfPCISlotLinkSpeedTable = _CucsBiosVfPCISlotLinkSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70)
)
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedTable.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedEntry_Object = MibTableRow
cucsBiosVfPCISlotLinkSpeedEntry = _CucsBiosVfPCISlotLinkSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1)
)
cucsBiosVfPCISlotLinkSpeedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPCISlotLinkSpeedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedEntry.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPCISlotLinkSpeedInstanceId_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedInstanceId = _CucsBiosVfPCISlotLinkSpeedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 1),
    _CucsBiosVfPCISlotLinkSpeedInstanceId_Type()
)
cucsBiosVfPCISlotLinkSpeedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedInstanceId.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedDn_Type = CucsManagedObjectDn
_CucsBiosVfPCISlotLinkSpeedDn_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedDn = _CucsBiosVfPCISlotLinkSpeedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 2),
    _CucsBiosVfPCISlotLinkSpeedDn_Type()
)
cucsBiosVfPCISlotLinkSpeedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedDn.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedRn_Type = SnmpAdminString
_CucsBiosVfPCISlotLinkSpeedRn_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedRn = _CucsBiosVfPCISlotLinkSpeedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 3),
    _CucsBiosVfPCISlotLinkSpeedRn_Type()
)
cucsBiosVfPCISlotLinkSpeedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedRn.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 4),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 5),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 6),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 7),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 8),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 9),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 10),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 11),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 12),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type = CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed
_CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed = _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 13),
    _CucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed_Type()
)
cucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedPropAcl_Type = Unsigned64
_CucsBiosVfPCISlotLinkSpeedPropAcl_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedPropAcl = _CucsBiosVfPCISlotLinkSpeedPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 14),
    _CucsBiosVfPCISlotLinkSpeedPropAcl_Type()
)
cucsBiosVfPCISlotLinkSpeedPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedPropAcl.setStatus("current")
_CucsBiosVfPCISlotLinkSpeedSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPCISlotLinkSpeedSupportedByDefault_Object = MibTableColumn
cucsBiosVfPCISlotLinkSpeedSupportedByDefault = _CucsBiosVfPCISlotLinkSpeedSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 70, 1, 15),
    _CucsBiosVfPCISlotLinkSpeedSupportedByDefault_Type()
)
cucsBiosVfPCISlotLinkSpeedSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCISlotLinkSpeedSupportedByDefault.setStatus("current")
_CucsBiosVfPSTATECoordinationTable_Object = MibTable
cucsBiosVfPSTATECoordinationTable = _CucsBiosVfPSTATECoordinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71)
)
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationTable.setStatus("current")
_CucsBiosVfPSTATECoordinationEntry_Object = MibTableRow
cucsBiosVfPSTATECoordinationEntry = _CucsBiosVfPSTATECoordinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1)
)
cucsBiosVfPSTATECoordinationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPSTATECoordinationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationEntry.setStatus("current")
_CucsBiosVfPSTATECoordinationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPSTATECoordinationInstanceId_Object = MibTableColumn
cucsBiosVfPSTATECoordinationInstanceId = _CucsBiosVfPSTATECoordinationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 1),
    _CucsBiosVfPSTATECoordinationInstanceId_Type()
)
cucsBiosVfPSTATECoordinationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationInstanceId.setStatus("current")
_CucsBiosVfPSTATECoordinationDn_Type = CucsManagedObjectDn
_CucsBiosVfPSTATECoordinationDn_Object = MibTableColumn
cucsBiosVfPSTATECoordinationDn = _CucsBiosVfPSTATECoordinationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 2),
    _CucsBiosVfPSTATECoordinationDn_Type()
)
cucsBiosVfPSTATECoordinationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationDn.setStatus("current")
_CucsBiosVfPSTATECoordinationRn_Type = SnmpAdminString
_CucsBiosVfPSTATECoordinationRn_Object = MibTableColumn
cucsBiosVfPSTATECoordinationRn = _CucsBiosVfPSTATECoordinationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 3),
    _CucsBiosVfPSTATECoordinationRn_Type()
)
cucsBiosVfPSTATECoordinationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationRn.setStatus("current")
_CucsBiosVfPSTATECoordinationVpPSTATECoordination_Type = CucsBiosVfPSTATECoordinationVpPSTATECoordination
_CucsBiosVfPSTATECoordinationVpPSTATECoordination_Object = MibTableColumn
cucsBiosVfPSTATECoordinationVpPSTATECoordination = _CucsBiosVfPSTATECoordinationVpPSTATECoordination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 4),
    _CucsBiosVfPSTATECoordinationVpPSTATECoordination_Type()
)
cucsBiosVfPSTATECoordinationVpPSTATECoordination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationVpPSTATECoordination.setStatus("current")
_CucsBiosVfPSTATECoordinationPropAcl_Type = Unsigned64
_CucsBiosVfPSTATECoordinationPropAcl_Object = MibTableColumn
cucsBiosVfPSTATECoordinationPropAcl = _CucsBiosVfPSTATECoordinationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 5),
    _CucsBiosVfPSTATECoordinationPropAcl_Type()
)
cucsBiosVfPSTATECoordinationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationPropAcl.setStatus("current")
_CucsBiosVfPSTATECoordinationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPSTATECoordinationSupportedByDefault_Object = MibTableColumn
cucsBiosVfPSTATECoordinationSupportedByDefault = _CucsBiosVfPSTATECoordinationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 71, 1, 6),
    _CucsBiosVfPSTATECoordinationSupportedByDefault_Type()
)
cucsBiosVfPSTATECoordinationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPSTATECoordinationSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationTable_Object = MibTable
cucsBiosVfProcessorEnergyConfigurationTable = _CucsBiosVfProcessorEnergyConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationTable.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationEntry_Object = MibTableRow
cucsBiosVfProcessorEnergyConfigurationEntry = _CucsBiosVfProcessorEnergyConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1)
)
cucsBiosVfProcessorEnergyConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorEnergyConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationEntry.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorEnergyConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationInstanceId = _CucsBiosVfProcessorEnergyConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 1),
    _CucsBiosVfProcessorEnergyConfigurationInstanceId_Type()
)
cucsBiosVfProcessorEnergyConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationInstanceId.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorEnergyConfigurationDn_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationDn = _CucsBiosVfProcessorEnergyConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 2),
    _CucsBiosVfProcessorEnergyConfigurationDn_Type()
)
cucsBiosVfProcessorEnergyConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationDn.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationRn_Type = SnmpAdminString
_CucsBiosVfProcessorEnergyConfigurationRn_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationRn = _CucsBiosVfProcessorEnergyConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 3),
    _CucsBiosVfProcessorEnergyConfigurationRn_Type()
)
cucsBiosVfProcessorEnergyConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationRn.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type = CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance
_CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance = _CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 4),
    _CucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance_Type()
)
cucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type = CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology
_CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationVpPowerTechnology = _CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 5),
    _CucsBiosVfProcessorEnergyConfigurationVpPowerTechnology_Type()
)
cucsBiosVfProcessorEnergyConfigurationVpPowerTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationVpPowerTechnology.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfProcessorEnergyConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationPropAcl = _CucsBiosVfProcessorEnergyConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 6),
    _CucsBiosVfProcessorEnergyConfigurationPropAcl_Type()
)
cucsBiosVfProcessorEnergyConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationPropAcl.setStatus("current")
_CucsBiosVfProcessorEnergyConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorEnergyConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorEnergyConfigurationSupportedByDefault = _CucsBiosVfProcessorEnergyConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 72, 1, 7),
    _CucsBiosVfProcessorEnergyConfigurationSupportedByDefault_Type()
)
cucsBiosVfProcessorEnergyConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorEnergyConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigTable_Object = MibTable
cucsBiosVfProcessorPrefetchConfigTable = _CucsBiosVfProcessorPrefetchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73)
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigTable.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigEntry_Object = MibTableRow
cucsBiosVfProcessorPrefetchConfigEntry = _CucsBiosVfProcessorPrefetchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1)
)
cucsBiosVfProcessorPrefetchConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfProcessorPrefetchConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigEntry.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigInstanceId_Type = CucsManagedObjectId
_CucsBiosVfProcessorPrefetchConfigInstanceId_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigInstanceId = _CucsBiosVfProcessorPrefetchConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 1),
    _CucsBiosVfProcessorPrefetchConfigInstanceId_Type()
)
cucsBiosVfProcessorPrefetchConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigInstanceId.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigDn_Type = CucsManagedObjectDn
_CucsBiosVfProcessorPrefetchConfigDn_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigDn = _CucsBiosVfProcessorPrefetchConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 2),
    _CucsBiosVfProcessorPrefetchConfigDn_Type()
)
cucsBiosVfProcessorPrefetchConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigDn.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigRn_Type = SnmpAdminString
_CucsBiosVfProcessorPrefetchConfigRn_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigRn = _CucsBiosVfProcessorPrefetchConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 3),
    _CucsBiosVfProcessorPrefetchConfigRn_Type()
)
cucsBiosVfProcessorPrefetchConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigRn.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type = CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher
_CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher = _CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 4),
    _CucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher_Type()
)
cucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type = CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher
_CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher = _CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 5),
    _CucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher_Type()
)
cucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type = CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch
_CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch = _CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 6),
    _CucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch_Type()
)
cucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type = CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher
_CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher = _CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 7),
    _CucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher_Type()
)
cucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigPropAcl_Type = Unsigned64
_CucsBiosVfProcessorPrefetchConfigPropAcl_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigPropAcl = _CucsBiosVfProcessorPrefetchConfigPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 8),
    _CucsBiosVfProcessorPrefetchConfigPropAcl_Type()
)
cucsBiosVfProcessorPrefetchConfigPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigPropAcl.setStatus("current")
_CucsBiosVfProcessorPrefetchConfigSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfProcessorPrefetchConfigSupportedByDefault_Object = MibTableColumn
cucsBiosVfProcessorPrefetchConfigSupportedByDefault = _CucsBiosVfProcessorPrefetchConfigSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 73, 1, 9),
    _CucsBiosVfProcessorPrefetchConfigSupportedByDefault_Type()
)
cucsBiosVfProcessorPrefetchConfigSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfProcessorPrefetchConfigSupportedByDefault.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectTable_Object = MibTable
cucsBiosVfQPILinkFrequencySelectTable = _CucsBiosVfQPILinkFrequencySelectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74)
)
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectTable.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectEntry_Object = MibTableRow
cucsBiosVfQPILinkFrequencySelectEntry = _CucsBiosVfQPILinkFrequencySelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1)
)
cucsBiosVfQPILinkFrequencySelectEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfQPILinkFrequencySelectInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectEntry.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectInstanceId_Type = CucsManagedObjectId
_CucsBiosVfQPILinkFrequencySelectInstanceId_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectInstanceId = _CucsBiosVfQPILinkFrequencySelectInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 1),
    _CucsBiosVfQPILinkFrequencySelectInstanceId_Type()
)
cucsBiosVfQPILinkFrequencySelectInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectInstanceId.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectDn_Type = CucsManagedObjectDn
_CucsBiosVfQPILinkFrequencySelectDn_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectDn = _CucsBiosVfQPILinkFrequencySelectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 2),
    _CucsBiosVfQPILinkFrequencySelectDn_Type()
)
cucsBiosVfQPILinkFrequencySelectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectDn.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectRn_Type = SnmpAdminString
_CucsBiosVfQPILinkFrequencySelectRn_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectRn = _CucsBiosVfQPILinkFrequencySelectRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 3),
    _CucsBiosVfQPILinkFrequencySelectRn_Type()
)
cucsBiosVfQPILinkFrequencySelectRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectRn.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type = CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect
_CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect = _CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 4),
    _CucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect_Type()
)
cucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectPropAcl_Type = Unsigned64
_CucsBiosVfQPILinkFrequencySelectPropAcl_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectPropAcl = _CucsBiosVfQPILinkFrequencySelectPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 5),
    _CucsBiosVfQPILinkFrequencySelectPropAcl_Type()
)
cucsBiosVfQPILinkFrequencySelectPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectPropAcl.setStatus("current")
_CucsBiosVfQPILinkFrequencySelectSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfQPILinkFrequencySelectSupportedByDefault_Object = MibTableColumn
cucsBiosVfQPILinkFrequencySelectSupportedByDefault = _CucsBiosVfQPILinkFrequencySelectSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 74, 1, 6),
    _CucsBiosVfQPILinkFrequencySelectSupportedByDefault_Type()
)
cucsBiosVfQPILinkFrequencySelectSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPILinkFrequencySelectSupportedByDefault.setStatus("current")
_CucsBiosVfScrubPoliciesTable_Object = MibTable
cucsBiosVfScrubPoliciesTable = _CucsBiosVfScrubPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75)
)
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesTable.setStatus("current")
_CucsBiosVfScrubPoliciesEntry_Object = MibTableRow
cucsBiosVfScrubPoliciesEntry = _CucsBiosVfScrubPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1)
)
cucsBiosVfScrubPoliciesEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfScrubPoliciesInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesEntry.setStatus("current")
_CucsBiosVfScrubPoliciesInstanceId_Type = CucsManagedObjectId
_CucsBiosVfScrubPoliciesInstanceId_Object = MibTableColumn
cucsBiosVfScrubPoliciesInstanceId = _CucsBiosVfScrubPoliciesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 1),
    _CucsBiosVfScrubPoliciesInstanceId_Type()
)
cucsBiosVfScrubPoliciesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesInstanceId.setStatus("current")
_CucsBiosVfScrubPoliciesDn_Type = CucsManagedObjectDn
_CucsBiosVfScrubPoliciesDn_Object = MibTableColumn
cucsBiosVfScrubPoliciesDn = _CucsBiosVfScrubPoliciesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 2),
    _CucsBiosVfScrubPoliciesDn_Type()
)
cucsBiosVfScrubPoliciesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesDn.setStatus("current")
_CucsBiosVfScrubPoliciesRn_Type = SnmpAdminString
_CucsBiosVfScrubPoliciesRn_Object = MibTableColumn
cucsBiosVfScrubPoliciesRn = _CucsBiosVfScrubPoliciesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 3),
    _CucsBiosVfScrubPoliciesRn_Type()
)
cucsBiosVfScrubPoliciesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesRn.setStatus("current")
_CucsBiosVfScrubPoliciesVpDemandScrub_Type = CucsBiosVfScrubPoliciesVpDemandScrub
_CucsBiosVfScrubPoliciesVpDemandScrub_Object = MibTableColumn
cucsBiosVfScrubPoliciesVpDemandScrub = _CucsBiosVfScrubPoliciesVpDemandScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 4),
    _CucsBiosVfScrubPoliciesVpDemandScrub_Type()
)
cucsBiosVfScrubPoliciesVpDemandScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesVpDemandScrub.setStatus("current")
_CucsBiosVfScrubPoliciesVpPatrolScrub_Type = CucsBiosVfScrubPoliciesVpPatrolScrub
_CucsBiosVfScrubPoliciesVpPatrolScrub_Object = MibTableColumn
cucsBiosVfScrubPoliciesVpPatrolScrub = _CucsBiosVfScrubPoliciesVpPatrolScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 5),
    _CucsBiosVfScrubPoliciesVpPatrolScrub_Type()
)
cucsBiosVfScrubPoliciesVpPatrolScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesVpPatrolScrub.setStatus("current")
_CucsBiosVfScrubPoliciesPropAcl_Type = Unsigned64
_CucsBiosVfScrubPoliciesPropAcl_Object = MibTableColumn
cucsBiosVfScrubPoliciesPropAcl = _CucsBiosVfScrubPoliciesPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 6),
    _CucsBiosVfScrubPoliciesPropAcl_Type()
)
cucsBiosVfScrubPoliciesPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesPropAcl.setStatus("current")
_CucsBiosVfScrubPoliciesSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfScrubPoliciesSupportedByDefault_Object = MibTableColumn
cucsBiosVfScrubPoliciesSupportedByDefault = _CucsBiosVfScrubPoliciesSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 75, 1, 7),
    _CucsBiosVfScrubPoliciesSupportedByDefault_Type()
)
cucsBiosVfScrubPoliciesSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfScrubPoliciesSupportedByDefault.setStatus("current")
_CucsBiosVfUSBPortConfigurationTable_Object = MibTable
cucsBiosVfUSBPortConfigurationTable = _CucsBiosVfUSBPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76)
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationTable.setStatus("current")
_CucsBiosVfUSBPortConfigurationEntry_Object = MibTableRow
cucsBiosVfUSBPortConfigurationEntry = _CucsBiosVfUSBPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1)
)
cucsBiosVfUSBPortConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUSBPortConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationEntry.setStatus("current")
_CucsBiosVfUSBPortConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUSBPortConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationInstanceId = _CucsBiosVfUSBPortConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 1),
    _CucsBiosVfUSBPortConfigurationInstanceId_Type()
)
cucsBiosVfUSBPortConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationInstanceId.setStatus("current")
_CucsBiosVfUSBPortConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfUSBPortConfigurationDn_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationDn = _CucsBiosVfUSBPortConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 2),
    _CucsBiosVfUSBPortConfigurationDn_Type()
)
cucsBiosVfUSBPortConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationDn.setStatus("current")
_CucsBiosVfUSBPortConfigurationRn_Type = SnmpAdminString
_CucsBiosVfUSBPortConfigurationRn_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationRn = _CucsBiosVfUSBPortConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 3),
    _CucsBiosVfUSBPortConfigurationRn_Type()
)
cucsBiosVfUSBPortConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationRn.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpPort6064Emulation_Type = CucsBiosVfUSBPortConfigurationVpPort6064Emulation
_CucsBiosVfUSBPortConfigurationVpPort6064Emulation_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpPort6064Emulation = _CucsBiosVfUSBPortConfigurationVpPort6064Emulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 4),
    _CucsBiosVfUSBPortConfigurationVpPort6064Emulation_Type()
)
cucsBiosVfUSBPortConfigurationVpPort6064Emulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpPort6064Emulation.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortFront_Type = CucsBiosVfUSBPortConfigurationVpUSBPortFront
_CucsBiosVfUSBPortConfigurationVpUSBPortFront_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortFront = _CucsBiosVfUSBPortConfigurationVpUSBPortFront_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 5),
    _CucsBiosVfUSBPortConfigurationVpUSBPortFront_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortFront.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortFront.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortInternal_Type = CucsBiosVfUSBPortConfigurationVpUSBPortInternal
_CucsBiosVfUSBPortConfigurationVpUSBPortInternal_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortInternal = _CucsBiosVfUSBPortConfigurationVpUSBPortInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 6),
    _CucsBiosVfUSBPortConfigurationVpUSBPortInternal_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortInternal.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortKVM_Type = CucsBiosVfUSBPortConfigurationVpUSBPortKVM
_CucsBiosVfUSBPortConfigurationVpUSBPortKVM_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortKVM = _CucsBiosVfUSBPortConfigurationVpUSBPortKVM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 7),
    _CucsBiosVfUSBPortConfigurationVpUSBPortKVM_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortKVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortKVM.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortRear_Type = CucsBiosVfUSBPortConfigurationVpUSBPortRear
_CucsBiosVfUSBPortConfigurationVpUSBPortRear_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortRear = _CucsBiosVfUSBPortConfigurationVpUSBPortRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 8),
    _CucsBiosVfUSBPortConfigurationVpUSBPortRear_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortRear.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortSDCard_Type = CucsBiosVfUSBPortConfigurationVpUSBPortSDCard
_CucsBiosVfUSBPortConfigurationVpUSBPortSDCard_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortSDCard = _CucsBiosVfUSBPortConfigurationVpUSBPortSDCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 9),
    _CucsBiosVfUSBPortConfigurationVpUSBPortSDCard_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortSDCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortSDCard.setStatus("current")
_CucsBiosVfUSBPortConfigurationVpUSBPortVMedia_Type = CucsBiosVfUSBPortConfigurationVpUSBPortVMedia
_CucsBiosVfUSBPortConfigurationVpUSBPortVMedia_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationVpUSBPortVMedia = _CucsBiosVfUSBPortConfigurationVpUSBPortVMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 10),
    _CucsBiosVfUSBPortConfigurationVpUSBPortVMedia_Type()
)
cucsBiosVfUSBPortConfigurationVpUSBPortVMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationVpUSBPortVMedia.setStatus("current")
_CucsBiosVfUSBPortConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfUSBPortConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationPropAcl = _CucsBiosVfUSBPortConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 11),
    _CucsBiosVfUSBPortConfigurationPropAcl_Type()
)
cucsBiosVfUSBPortConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationPropAcl.setStatus("current")
_CucsBiosVfUSBPortConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUSBPortConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfUSBPortConfigurationSupportedByDefault = _CucsBiosVfUSBPortConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 76, 1, 12),
    _CucsBiosVfUSBPortConfigurationSupportedByDefault_Type()
)
cucsBiosVfUSBPortConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBPortConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfVGAPriorityTable_Object = MibTable
cucsBiosVfVGAPriorityTable = _CucsBiosVfVGAPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77)
)
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityTable.setStatus("current")
_CucsBiosVfVGAPriorityEntry_Object = MibTableRow
cucsBiosVfVGAPriorityEntry = _CucsBiosVfVGAPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1)
)
cucsBiosVfVGAPriorityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfVGAPriorityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityEntry.setStatus("current")
_CucsBiosVfVGAPriorityInstanceId_Type = CucsManagedObjectId
_CucsBiosVfVGAPriorityInstanceId_Object = MibTableColumn
cucsBiosVfVGAPriorityInstanceId = _CucsBiosVfVGAPriorityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 1),
    _CucsBiosVfVGAPriorityInstanceId_Type()
)
cucsBiosVfVGAPriorityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityInstanceId.setStatus("current")
_CucsBiosVfVGAPriorityDn_Type = CucsManagedObjectDn
_CucsBiosVfVGAPriorityDn_Object = MibTableColumn
cucsBiosVfVGAPriorityDn = _CucsBiosVfVGAPriorityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 2),
    _CucsBiosVfVGAPriorityDn_Type()
)
cucsBiosVfVGAPriorityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityDn.setStatus("current")
_CucsBiosVfVGAPriorityRn_Type = SnmpAdminString
_CucsBiosVfVGAPriorityRn_Object = MibTableColumn
cucsBiosVfVGAPriorityRn = _CucsBiosVfVGAPriorityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 3),
    _CucsBiosVfVGAPriorityRn_Type()
)
cucsBiosVfVGAPriorityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityRn.setStatus("current")
_CucsBiosVfVGAPriorityVpVGAPriority_Type = CucsBiosVfVGAPriorityVpVGAPriority
_CucsBiosVfVGAPriorityVpVGAPriority_Object = MibTableColumn
cucsBiosVfVGAPriorityVpVGAPriority = _CucsBiosVfVGAPriorityVpVGAPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 4),
    _CucsBiosVfVGAPriorityVpVGAPriority_Type()
)
cucsBiosVfVGAPriorityVpVGAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityVpVGAPriority.setStatus("current")
_CucsBiosVfVGAPriorityPropAcl_Type = Unsigned64
_CucsBiosVfVGAPriorityPropAcl_Object = MibTableColumn
cucsBiosVfVGAPriorityPropAcl = _CucsBiosVfVGAPriorityPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 5),
    _CucsBiosVfVGAPriorityPropAcl_Type()
)
cucsBiosVfVGAPriorityPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPriorityPropAcl.setStatus("current")
_CucsBiosVfVGAPrioritySupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfVGAPrioritySupportedByDefault_Object = MibTableColumn
cucsBiosVfVGAPrioritySupportedByDefault = _CucsBiosVfVGAPrioritySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 77, 1, 6),
    _CucsBiosVfVGAPrioritySupportedByDefault_Type()
)
cucsBiosVfVGAPrioritySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfVGAPrioritySupportedByDefault.setStatus("current")
_CucsBiosVfAltitudeTable_Object = MibTable
cucsBiosVfAltitudeTable = _CucsBiosVfAltitudeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78)
)
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeTable.setStatus("current")
_CucsBiosVfAltitudeEntry_Object = MibTableRow
cucsBiosVfAltitudeEntry = _CucsBiosVfAltitudeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1)
)
cucsBiosVfAltitudeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfAltitudeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeEntry.setStatus("current")
_CucsBiosVfAltitudeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfAltitudeInstanceId_Object = MibTableColumn
cucsBiosVfAltitudeInstanceId = _CucsBiosVfAltitudeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 1),
    _CucsBiosVfAltitudeInstanceId_Type()
)
cucsBiosVfAltitudeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeInstanceId.setStatus("current")
_CucsBiosVfAltitudeDn_Type = CucsManagedObjectDn
_CucsBiosVfAltitudeDn_Object = MibTableColumn
cucsBiosVfAltitudeDn = _CucsBiosVfAltitudeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 2),
    _CucsBiosVfAltitudeDn_Type()
)
cucsBiosVfAltitudeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeDn.setStatus("current")
_CucsBiosVfAltitudeRn_Type = SnmpAdminString
_CucsBiosVfAltitudeRn_Object = MibTableColumn
cucsBiosVfAltitudeRn = _CucsBiosVfAltitudeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 3),
    _CucsBiosVfAltitudeRn_Type()
)
cucsBiosVfAltitudeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeRn.setStatus("current")
_CucsBiosVfAltitudeVpAltitude_Type = CucsBiosVfAltitudeVpAltitude
_CucsBiosVfAltitudeVpAltitude_Object = MibTableColumn
cucsBiosVfAltitudeVpAltitude = _CucsBiosVfAltitudeVpAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 4),
    _CucsBiosVfAltitudeVpAltitude_Type()
)
cucsBiosVfAltitudeVpAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeVpAltitude.setStatus("current")
_CucsBiosVfAltitudePropAcl_Type = Unsigned64
_CucsBiosVfAltitudePropAcl_Object = MibTableColumn
cucsBiosVfAltitudePropAcl = _CucsBiosVfAltitudePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 5),
    _CucsBiosVfAltitudePropAcl_Type()
)
cucsBiosVfAltitudePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudePropAcl.setStatus("current")
_CucsBiosVfAltitudeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfAltitudeSupportedByDefault_Object = MibTableColumn
cucsBiosVfAltitudeSupportedByDefault = _CucsBiosVfAltitudeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 78, 1, 6),
    _CucsBiosVfAltitudeSupportedByDefault_Type()
)
cucsBiosVfAltitudeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfAltitudeSupportedByDefault.setStatus("current")
_CucsBiosVfTPMSupportTable_Object = MibTable
cucsBiosVfTPMSupportTable = _CucsBiosVfTPMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79)
)
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportTable.setStatus("current")
_CucsBiosVfTPMSupportEntry_Object = MibTableRow
cucsBiosVfTPMSupportEntry = _CucsBiosVfTPMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1)
)
cucsBiosVfTPMSupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfTPMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportEntry.setStatus("current")
_CucsBiosVfTPMSupportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfTPMSupportInstanceId_Object = MibTableColumn
cucsBiosVfTPMSupportInstanceId = _CucsBiosVfTPMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 1),
    _CucsBiosVfTPMSupportInstanceId_Type()
)
cucsBiosVfTPMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportInstanceId.setStatus("current")
_CucsBiosVfTPMSupportDn_Type = CucsManagedObjectDn
_CucsBiosVfTPMSupportDn_Object = MibTableColumn
cucsBiosVfTPMSupportDn = _CucsBiosVfTPMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 2),
    _CucsBiosVfTPMSupportDn_Type()
)
cucsBiosVfTPMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportDn.setStatus("current")
_CucsBiosVfTPMSupportRn_Type = SnmpAdminString
_CucsBiosVfTPMSupportRn_Object = MibTableColumn
cucsBiosVfTPMSupportRn = _CucsBiosVfTPMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 3),
    _CucsBiosVfTPMSupportRn_Type()
)
cucsBiosVfTPMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportRn.setStatus("current")
_CucsBiosVfTPMSupportVpTPMSupport_Type = CucsBiosVfTPMSupportVpTPMSupport
_CucsBiosVfTPMSupportVpTPMSupport_Object = MibTableColumn
cucsBiosVfTPMSupportVpTPMSupport = _CucsBiosVfTPMSupportVpTPMSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 4),
    _CucsBiosVfTPMSupportVpTPMSupport_Type()
)
cucsBiosVfTPMSupportVpTPMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportVpTPMSupport.setStatus("current")
_CucsBiosVfTPMSupportPropAcl_Type = Unsigned64
_CucsBiosVfTPMSupportPropAcl_Object = MibTableColumn
cucsBiosVfTPMSupportPropAcl = _CucsBiosVfTPMSupportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 5),
    _CucsBiosVfTPMSupportPropAcl_Type()
)
cucsBiosVfTPMSupportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportPropAcl.setStatus("current")
_CucsBiosVfTPMSupportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfTPMSupportSupportedByDefault_Object = MibTableColumn
cucsBiosVfTPMSupportSupportedByDefault = _CucsBiosVfTPMSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 79, 1, 6),
    _CucsBiosVfTPMSupportSupportedByDefault_Type()
)
cucsBiosVfTPMSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMSupportSupportedByDefault.setStatus("current")
_CucsBiosVfUSBConfigurationTable_Object = MibTable
cucsBiosVfUSBConfigurationTable = _CucsBiosVfUSBConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80)
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationTable.setStatus("current")
_CucsBiosVfUSBConfigurationEntry_Object = MibTableRow
cucsBiosVfUSBConfigurationEntry = _CucsBiosVfUSBConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1)
)
cucsBiosVfUSBConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfUSBConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationEntry.setStatus("current")
_CucsBiosVfUSBConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfUSBConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfUSBConfigurationInstanceId = _CucsBiosVfUSBConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 1),
    _CucsBiosVfUSBConfigurationInstanceId_Type()
)
cucsBiosVfUSBConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationInstanceId.setStatus("current")
_CucsBiosVfUSBConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfUSBConfigurationDn_Object = MibTableColumn
cucsBiosVfUSBConfigurationDn = _CucsBiosVfUSBConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 2),
    _CucsBiosVfUSBConfigurationDn_Type()
)
cucsBiosVfUSBConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationDn.setStatus("current")
_CucsBiosVfUSBConfigurationRn_Type = SnmpAdminString
_CucsBiosVfUSBConfigurationRn_Object = MibTableColumn
cucsBiosVfUSBConfigurationRn = _CucsBiosVfUSBConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 3),
    _CucsBiosVfUSBConfigurationRn_Type()
)
cucsBiosVfUSBConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationRn.setStatus("current")
_CucsBiosVfUSBConfigurationVpLegacyUSBSupport_Type = CucsBiosVfUSBConfigurationVpLegacyUSBSupport
_CucsBiosVfUSBConfigurationVpLegacyUSBSupport_Object = MibTableColumn
cucsBiosVfUSBConfigurationVpLegacyUSBSupport = _CucsBiosVfUSBConfigurationVpLegacyUSBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 4),
    _CucsBiosVfUSBConfigurationVpLegacyUSBSupport_Type()
)
cucsBiosVfUSBConfigurationVpLegacyUSBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationVpLegacyUSBSupport.setStatus("current")
_CucsBiosVfUSBConfigurationVpXHCIMode_Type = CucsBiosVfUSBConfigurationVpXHCIMode
_CucsBiosVfUSBConfigurationVpXHCIMode_Object = MibTableColumn
cucsBiosVfUSBConfigurationVpXHCIMode = _CucsBiosVfUSBConfigurationVpXHCIMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 5),
    _CucsBiosVfUSBConfigurationVpXHCIMode_Type()
)
cucsBiosVfUSBConfigurationVpXHCIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationVpXHCIMode.setStatus("current")
_CucsBiosVfUSBConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfUSBConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfUSBConfigurationPropAcl = _CucsBiosVfUSBConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 6),
    _CucsBiosVfUSBConfigurationPropAcl_Type()
)
cucsBiosVfUSBConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationPropAcl.setStatus("current")
_CucsBiosVfUSBConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfUSBConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfUSBConfigurationSupportedByDefault = _CucsBiosVfUSBConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 80, 1, 7),
    _CucsBiosVfUSBConfigurationSupportedByDefault_Type()
)
cucsBiosVfUSBConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfUSBConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfQPISnoopModeTable_Object = MibTable
cucsBiosVfQPISnoopModeTable = _CucsBiosVfQPISnoopModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81)
)
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeTable.setStatus("current")
_CucsBiosVfQPISnoopModeEntry_Object = MibTableRow
cucsBiosVfQPISnoopModeEntry = _CucsBiosVfQPISnoopModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1)
)
cucsBiosVfQPISnoopModeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfQPISnoopModeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeEntry.setStatus("current")
_CucsBiosVfQPISnoopModeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfQPISnoopModeInstanceId_Object = MibTableColumn
cucsBiosVfQPISnoopModeInstanceId = _CucsBiosVfQPISnoopModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 1),
    _CucsBiosVfQPISnoopModeInstanceId_Type()
)
cucsBiosVfQPISnoopModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeInstanceId.setStatus("current")
_CucsBiosVfQPISnoopModeDn_Type = CucsManagedObjectDn
_CucsBiosVfQPISnoopModeDn_Object = MibTableColumn
cucsBiosVfQPISnoopModeDn = _CucsBiosVfQPISnoopModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 2),
    _CucsBiosVfQPISnoopModeDn_Type()
)
cucsBiosVfQPISnoopModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeDn.setStatus("current")
_CucsBiosVfQPISnoopModeRn_Type = SnmpAdminString
_CucsBiosVfQPISnoopModeRn_Object = MibTableColumn
cucsBiosVfQPISnoopModeRn = _CucsBiosVfQPISnoopModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 3),
    _CucsBiosVfQPISnoopModeRn_Type()
)
cucsBiosVfQPISnoopModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeRn.setStatus("current")
_CucsBiosVfQPISnoopModeVpQPISnoopMode_Type = CucsBiosVfQPISnoopModeVpQPISnoopMode
_CucsBiosVfQPISnoopModeVpQPISnoopMode_Object = MibTableColumn
cucsBiosVfQPISnoopModeVpQPISnoopMode = _CucsBiosVfQPISnoopModeVpQPISnoopMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 4),
    _CucsBiosVfQPISnoopModeVpQPISnoopMode_Type()
)
cucsBiosVfQPISnoopModeVpQPISnoopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeVpQPISnoopMode.setStatus("current")
_CucsBiosVfQPISnoopModePropAcl_Type = Unsigned64
_CucsBiosVfQPISnoopModePropAcl_Object = MibTableColumn
cucsBiosVfQPISnoopModePropAcl = _CucsBiosVfQPISnoopModePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 5),
    _CucsBiosVfQPISnoopModePropAcl_Type()
)
cucsBiosVfQPISnoopModePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModePropAcl.setStatus("current")
_CucsBiosVfQPISnoopModeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfQPISnoopModeSupportedByDefault_Object = MibTableColumn
cucsBiosVfQPISnoopModeSupportedByDefault = _CucsBiosVfQPISnoopModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 81, 1, 6),
    _CucsBiosVfQPISnoopModeSupportedByDefault_Type()
)
cucsBiosVfQPISnoopModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfQPISnoopModeSupportedByDefault.setStatus("current")
_CucsBiosVfCPUPowerManagementTable_Object = MibTable
cucsBiosVfCPUPowerManagementTable = _CucsBiosVfCPUPowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82)
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementTable.setStatus("current")
_CucsBiosVfCPUPowerManagementEntry_Object = MibTableRow
cucsBiosVfCPUPowerManagementEntry = _CucsBiosVfCPUPowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1)
)
cucsBiosVfCPUPowerManagementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfCPUPowerManagementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementEntry.setStatus("current")
_CucsBiosVfCPUPowerManagementInstanceId_Type = CucsManagedObjectId
_CucsBiosVfCPUPowerManagementInstanceId_Object = MibTableColumn
cucsBiosVfCPUPowerManagementInstanceId = _CucsBiosVfCPUPowerManagementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 1),
    _CucsBiosVfCPUPowerManagementInstanceId_Type()
)
cucsBiosVfCPUPowerManagementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementInstanceId.setStatus("current")
_CucsBiosVfCPUPowerManagementDn_Type = CucsManagedObjectDn
_CucsBiosVfCPUPowerManagementDn_Object = MibTableColumn
cucsBiosVfCPUPowerManagementDn = _CucsBiosVfCPUPowerManagementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 2),
    _CucsBiosVfCPUPowerManagementDn_Type()
)
cucsBiosVfCPUPowerManagementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementDn.setStatus("current")
_CucsBiosVfCPUPowerManagementRn_Type = SnmpAdminString
_CucsBiosVfCPUPowerManagementRn_Object = MibTableColumn
cucsBiosVfCPUPowerManagementRn = _CucsBiosVfCPUPowerManagementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 3),
    _CucsBiosVfCPUPowerManagementRn_Type()
)
cucsBiosVfCPUPowerManagementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementRn.setStatus("current")
_CucsBiosVfCPUPowerManagementPropAcl_Type = Unsigned64
_CucsBiosVfCPUPowerManagementPropAcl_Object = MibTableColumn
cucsBiosVfCPUPowerManagementPropAcl = _CucsBiosVfCPUPowerManagementPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 4),
    _CucsBiosVfCPUPowerManagementPropAcl_Type()
)
cucsBiosVfCPUPowerManagementPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementPropAcl.setStatus("current")
_CucsBiosVfCPUPowerManagementSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfCPUPowerManagementSupportedByDefault_Object = MibTableColumn
cucsBiosVfCPUPowerManagementSupportedByDefault = _CucsBiosVfCPUPowerManagementSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 5),
    _CucsBiosVfCPUPowerManagementSupportedByDefault_Type()
)
cucsBiosVfCPUPowerManagementSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementSupportedByDefault.setStatus("current")
_CucsBiosVfCPUPowerManagementVpCPUPowerManagement_Type = CucsBiosVfCPUPowerManagementVpCPUPowerManagement
_CucsBiosVfCPUPowerManagementVpCPUPowerManagement_Object = MibTableColumn
cucsBiosVfCPUPowerManagementVpCPUPowerManagement = _CucsBiosVfCPUPowerManagementVpCPUPowerManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 82, 1, 6),
    _CucsBiosVfCPUPowerManagementVpCPUPowerManagement_Type()
)
cucsBiosVfCPUPowerManagementVpCPUPowerManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUPowerManagementVpCPUPowerManagement.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportTable_Object = MibTable
cucsBiosVfEnhancedPowerCappingSupportTable = _CucsBiosVfEnhancedPowerCappingSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83)
)
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportTable.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportEntry_Object = MibTableRow
cucsBiosVfEnhancedPowerCappingSupportEntry = _CucsBiosVfEnhancedPowerCappingSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1)
)
cucsBiosVfEnhancedPowerCappingSupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfEnhancedPowerCappingSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportEntry.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfEnhancedPowerCappingSupportInstanceId_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportInstanceId = _CucsBiosVfEnhancedPowerCappingSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 1),
    _CucsBiosVfEnhancedPowerCappingSupportInstanceId_Type()
)
cucsBiosVfEnhancedPowerCappingSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportInstanceId.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportDn_Type = CucsManagedObjectDn
_CucsBiosVfEnhancedPowerCappingSupportDn_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportDn = _CucsBiosVfEnhancedPowerCappingSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 2),
    _CucsBiosVfEnhancedPowerCappingSupportDn_Type()
)
cucsBiosVfEnhancedPowerCappingSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportDn.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportRn_Type = SnmpAdminString
_CucsBiosVfEnhancedPowerCappingSupportRn_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportRn = _CucsBiosVfEnhancedPowerCappingSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 3),
    _CucsBiosVfEnhancedPowerCappingSupportRn_Type()
)
cucsBiosVfEnhancedPowerCappingSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportRn.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportPropAcl_Type = Unsigned64
_CucsBiosVfEnhancedPowerCappingSupportPropAcl_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportPropAcl = _CucsBiosVfEnhancedPowerCappingSupportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 4),
    _CucsBiosVfEnhancedPowerCappingSupportPropAcl_Type()
)
cucsBiosVfEnhancedPowerCappingSupportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportPropAcl.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfEnhancedPowerCappingSupportSupportedByDefault_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportSupportedByDefault = _CucsBiosVfEnhancedPowerCappingSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 5),
    _CucsBiosVfEnhancedPowerCappingSupportSupportedByDefault_Type()
)
cucsBiosVfEnhancedPowerCappingSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportSupportedByDefault.setStatus("current")
_CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping_Type = CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping
_CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping_Object = MibTableColumn
cucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping = _CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 83, 1, 6),
    _CucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping_Type()
)
cucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping.setStatus("current")
_CucsBiosVfPCHSATAModeTable_Object = MibTable
cucsBiosVfPCHSATAModeTable = _CucsBiosVfPCHSATAModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84)
)
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeTable.setStatus("current")
_CucsBiosVfPCHSATAModeEntry_Object = MibTableRow
cucsBiosVfPCHSATAModeEntry = _CucsBiosVfPCHSATAModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1)
)
cucsBiosVfPCHSATAModeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPCHSATAModeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeEntry.setStatus("current")
_CucsBiosVfPCHSATAModeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPCHSATAModeInstanceId_Object = MibTableColumn
cucsBiosVfPCHSATAModeInstanceId = _CucsBiosVfPCHSATAModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 1),
    _CucsBiosVfPCHSATAModeInstanceId_Type()
)
cucsBiosVfPCHSATAModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeInstanceId.setStatus("current")
_CucsBiosVfPCHSATAModeDn_Type = CucsManagedObjectDn
_CucsBiosVfPCHSATAModeDn_Object = MibTableColumn
cucsBiosVfPCHSATAModeDn = _CucsBiosVfPCHSATAModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 2),
    _CucsBiosVfPCHSATAModeDn_Type()
)
cucsBiosVfPCHSATAModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeDn.setStatus("current")
_CucsBiosVfPCHSATAModeRn_Type = SnmpAdminString
_CucsBiosVfPCHSATAModeRn_Object = MibTableColumn
cucsBiosVfPCHSATAModeRn = _CucsBiosVfPCHSATAModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 3),
    _CucsBiosVfPCHSATAModeRn_Type()
)
cucsBiosVfPCHSATAModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeRn.setStatus("current")
_CucsBiosVfPCHSATAModePropAcl_Type = Unsigned64
_CucsBiosVfPCHSATAModePropAcl_Object = MibTableColumn
cucsBiosVfPCHSATAModePropAcl = _CucsBiosVfPCHSATAModePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 4),
    _CucsBiosVfPCHSATAModePropAcl_Type()
)
cucsBiosVfPCHSATAModePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModePropAcl.setStatus("current")
_CucsBiosVfPCHSATAModeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPCHSATAModeSupportedByDefault_Object = MibTableColumn
cucsBiosVfPCHSATAModeSupportedByDefault = _CucsBiosVfPCHSATAModeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 5),
    _CucsBiosVfPCHSATAModeSupportedByDefault_Type()
)
cucsBiosVfPCHSATAModeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeSupportedByDefault.setStatus("current")
_CucsBiosVfPCHSATAModeVpSATAMode_Type = CucsBiosVfPCHSATAModeVpSATAMode
_CucsBiosVfPCHSATAModeVpSATAMode_Object = MibTableColumn
cucsBiosVfPCHSATAModeVpSATAMode = _CucsBiosVfPCHSATAModeVpSATAMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 84, 1, 7),
    _CucsBiosVfPCHSATAModeVpSATAMode_Type()
)
cucsBiosVfPCHSATAModeVpSATAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCHSATAModeVpSATAMode.setStatus("current")
_CucsBiosVfASPMSupportTable_Object = MibTable
cucsBiosVfASPMSupportTable = _CucsBiosVfASPMSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85)
)
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportTable.setStatus("current")
_CucsBiosVfASPMSupportEntry_Object = MibTableRow
cucsBiosVfASPMSupportEntry = _CucsBiosVfASPMSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1)
)
cucsBiosVfASPMSupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfASPMSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportEntry.setStatus("current")
_CucsBiosVfASPMSupportInstanceId_Type = CucsManagedObjectId
_CucsBiosVfASPMSupportInstanceId_Object = MibTableColumn
cucsBiosVfASPMSupportInstanceId = _CucsBiosVfASPMSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 1),
    _CucsBiosVfASPMSupportInstanceId_Type()
)
cucsBiosVfASPMSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportInstanceId.setStatus("current")
_CucsBiosVfASPMSupportDn_Type = CucsManagedObjectDn
_CucsBiosVfASPMSupportDn_Object = MibTableColumn
cucsBiosVfASPMSupportDn = _CucsBiosVfASPMSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 2),
    _CucsBiosVfASPMSupportDn_Type()
)
cucsBiosVfASPMSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportDn.setStatus("current")
_CucsBiosVfASPMSupportRn_Type = SnmpAdminString
_CucsBiosVfASPMSupportRn_Object = MibTableColumn
cucsBiosVfASPMSupportRn = _CucsBiosVfASPMSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 3),
    _CucsBiosVfASPMSupportRn_Type()
)
cucsBiosVfASPMSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportRn.setStatus("current")
_CucsBiosVfASPMSupportVpASPMSupport_Type = CucsBiosVfASPMSupportVpASPMSupport
_CucsBiosVfASPMSupportVpASPMSupport_Object = MibTableColumn
cucsBiosVfASPMSupportVpASPMSupport = _CucsBiosVfASPMSupportVpASPMSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 4),
    _CucsBiosVfASPMSupportVpASPMSupport_Type()
)
cucsBiosVfASPMSupportVpASPMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportVpASPMSupport.setStatus("current")
_CucsBiosVfASPMSupportSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfASPMSupportSupportedByDefault_Object = MibTableColumn
cucsBiosVfASPMSupportSupportedByDefault = _CucsBiosVfASPMSupportSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 5),
    _CucsBiosVfASPMSupportSupportedByDefault_Type()
)
cucsBiosVfASPMSupportSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportSupportedByDefault.setStatus("current")
_CucsBiosVfASPMSupportPropAcl_Type = Unsigned64
_CucsBiosVfASPMSupportPropAcl_Object = MibTableColumn
cucsBiosVfASPMSupportPropAcl = _CucsBiosVfASPMSupportPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 85, 1, 6),
    _CucsBiosVfASPMSupportPropAcl_Type()
)
cucsBiosVfASPMSupportPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfASPMSupportPropAcl.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionTable_Object = MibTable
cucsBiosVfDDR3VoltageSelectionTable = _CucsBiosVfDDR3VoltageSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86)
)
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionTable.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionEntry_Object = MibTableRow
cucsBiosVfDDR3VoltageSelectionEntry = _CucsBiosVfDDR3VoltageSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1)
)
cucsBiosVfDDR3VoltageSelectionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfDDR3VoltageSelectionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionEntry.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionInstanceId_Type = CucsManagedObjectId
_CucsBiosVfDDR3VoltageSelectionInstanceId_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionInstanceId = _CucsBiosVfDDR3VoltageSelectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 1),
    _CucsBiosVfDDR3VoltageSelectionInstanceId_Type()
)
cucsBiosVfDDR3VoltageSelectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionInstanceId.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionDn_Type = CucsManagedObjectDn
_CucsBiosVfDDR3VoltageSelectionDn_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionDn = _CucsBiosVfDDR3VoltageSelectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 2),
    _CucsBiosVfDDR3VoltageSelectionDn_Type()
)
cucsBiosVfDDR3VoltageSelectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionDn.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionRn_Type = SnmpAdminString
_CucsBiosVfDDR3VoltageSelectionRn_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionRn = _CucsBiosVfDDR3VoltageSelectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 3),
    _CucsBiosVfDDR3VoltageSelectionRn_Type()
)
cucsBiosVfDDR3VoltageSelectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionRn.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection_Type = CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection
_CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection = _CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 4),
    _CucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection_Type()
)
cucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfDDR3VoltageSelectionSupportedByDefault_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionSupportedByDefault = _CucsBiosVfDDR3VoltageSelectionSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 5),
    _CucsBiosVfDDR3VoltageSelectionSupportedByDefault_Type()
)
cucsBiosVfDDR3VoltageSelectionSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionSupportedByDefault.setStatus("current")
_CucsBiosVfDDR3VoltageSelectionPropAcl_Type = Unsigned64
_CucsBiosVfDDR3VoltageSelectionPropAcl_Object = MibTableColumn
cucsBiosVfDDR3VoltageSelectionPropAcl = _CucsBiosVfDDR3VoltageSelectionPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 86, 1, 6),
    _CucsBiosVfDDR3VoltageSelectionPropAcl_Type()
)
cucsBiosVfDDR3VoltageSelectionPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfDDR3VoltageSelectionPropAcl.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlTable_Object = MibTable
cucsBiosVfConsistentDeviceNameControlTable = _CucsBiosVfConsistentDeviceNameControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87)
)
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlTable.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlEntry_Object = MibTableRow
cucsBiosVfConsistentDeviceNameControlEntry = _CucsBiosVfConsistentDeviceNameControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1)
)
cucsBiosVfConsistentDeviceNameControlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfConsistentDeviceNameControlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlEntry.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlInstanceId_Type = CucsManagedObjectId
_CucsBiosVfConsistentDeviceNameControlInstanceId_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlInstanceId = _CucsBiosVfConsistentDeviceNameControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 1),
    _CucsBiosVfConsistentDeviceNameControlInstanceId_Type()
)
cucsBiosVfConsistentDeviceNameControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlInstanceId.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlDn_Type = CucsManagedObjectDn
_CucsBiosVfConsistentDeviceNameControlDn_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlDn = _CucsBiosVfConsistentDeviceNameControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 2),
    _CucsBiosVfConsistentDeviceNameControlDn_Type()
)
cucsBiosVfConsistentDeviceNameControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlDn.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlRn_Type = SnmpAdminString
_CucsBiosVfConsistentDeviceNameControlRn_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlRn = _CucsBiosVfConsistentDeviceNameControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 3),
    _CucsBiosVfConsistentDeviceNameControlRn_Type()
)
cucsBiosVfConsistentDeviceNameControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlRn.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlVpCDNControl_Type = CucsBiosVfConsistentDeviceNameControlVpCDNControl
_CucsBiosVfConsistentDeviceNameControlVpCDNControl_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlVpCDNControl = _CucsBiosVfConsistentDeviceNameControlVpCDNControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 4),
    _CucsBiosVfConsistentDeviceNameControlVpCDNControl_Type()
)
cucsBiosVfConsistentDeviceNameControlVpCDNControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlVpCDNControl.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfConsistentDeviceNameControlSupportedByDefault_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlSupportedByDefault = _CucsBiosVfConsistentDeviceNameControlSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 5),
    _CucsBiosVfConsistentDeviceNameControlSupportedByDefault_Type()
)
cucsBiosVfConsistentDeviceNameControlSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlSupportedByDefault.setStatus("current")
_CucsBiosVfConsistentDeviceNameControlPropAcl_Type = Unsigned64
_CucsBiosVfConsistentDeviceNameControlPropAcl_Object = MibTableColumn
cucsBiosVfConsistentDeviceNameControlPropAcl = _CucsBiosVfConsistentDeviceNameControlPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 87, 1, 6),
    _CucsBiosVfConsistentDeviceNameControlPropAcl_Type()
)
cucsBiosVfConsistentDeviceNameControlPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfConsistentDeviceNameControlPropAcl.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyTable_Object = MibTable
cucsBiosVfIntelTrustedExecutionTechnologyTable = _CucsBiosVfIntelTrustedExecutionTechnologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyTable.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyEntry_Object = MibTableRow
cucsBiosVfIntelTrustedExecutionTechnologyEntry = _CucsBiosVfIntelTrustedExecutionTechnologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1)
)
cucsBiosVfIntelTrustedExecutionTechnologyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntelTrustedExecutionTechnologyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyEntry.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntelTrustedExecutionTechnologyInstanceId_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologyInstanceId = _CucsBiosVfIntelTrustedExecutionTechnologyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 1),
    _CucsBiosVfIntelTrustedExecutionTechnologyInstanceId_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyInstanceId.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyDn_Type = CucsManagedObjectDn
_CucsBiosVfIntelTrustedExecutionTechnologyDn_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologyDn = _CucsBiosVfIntelTrustedExecutionTechnologyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 2),
    _CucsBiosVfIntelTrustedExecutionTechnologyDn_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyDn.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyRn_Type = SnmpAdminString
_CucsBiosVfIntelTrustedExecutionTechnologyRn_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologyRn = _CucsBiosVfIntelTrustedExecutionTechnologyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 3),
    _CucsBiosVfIntelTrustedExecutionTechnologyRn_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyRn.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup_Type = CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup
_CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup = _CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 4),
    _CucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault = _CucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 5),
    _CucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault.setStatus("current")
_CucsBiosVfIntelTrustedExecutionTechnologyPropAcl_Type = Unsigned64
_CucsBiosVfIntelTrustedExecutionTechnologyPropAcl_Object = MibTableColumn
cucsBiosVfIntelTrustedExecutionTechnologyPropAcl = _CucsBiosVfIntelTrustedExecutionTechnologyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 88, 1, 6),
    _CucsBiosVfIntelTrustedExecutionTechnologyPropAcl_Type()
)
cucsBiosVfIntelTrustedExecutionTechnologyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntelTrustedExecutionTechnologyPropAcl.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationTable_Object = MibTable
cucsBiosVfPCILOMPortsConfigurationTable = _CucsBiosVfPCILOMPortsConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89)
)
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationTable.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationEntry_Object = MibTableRow
cucsBiosVfPCILOMPortsConfigurationEntry = _CucsBiosVfPCILOMPortsConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1)
)
cucsBiosVfPCILOMPortsConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfPCILOMPortsConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationEntry.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfPCILOMPortsConfigurationInstanceId_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationInstanceId = _CucsBiosVfPCILOMPortsConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 1),
    _CucsBiosVfPCILOMPortsConfigurationInstanceId_Type()
)
cucsBiosVfPCILOMPortsConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationInstanceId.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationDn_Type = CucsManagedObjectDn
_CucsBiosVfPCILOMPortsConfigurationDn_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationDn = _CucsBiosVfPCILOMPortsConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 2),
    _CucsBiosVfPCILOMPortsConfigurationDn_Type()
)
cucsBiosVfPCILOMPortsConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationDn.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationRn_Type = SnmpAdminString
_CucsBiosVfPCILOMPortsConfigurationRn_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationRn = _CucsBiosVfPCILOMPortsConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 3),
    _CucsBiosVfPCILOMPortsConfigurationRn_Type()
)
cucsBiosVfPCILOMPortsConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationRn.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link_Type = CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link
_CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link = _CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 4),
    _CucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link_Type()
)
cucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfPCILOMPortsConfigurationSupportedByDefault_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationSupportedByDefault = _CucsBiosVfPCILOMPortsConfigurationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 5),
    _CucsBiosVfPCILOMPortsConfigurationSupportedByDefault_Type()
)
cucsBiosVfPCILOMPortsConfigurationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationSupportedByDefault.setStatus("current")
_CucsBiosVfPCILOMPortsConfigurationPropAcl_Type = Unsigned64
_CucsBiosVfPCILOMPortsConfigurationPropAcl_Object = MibTableColumn
cucsBiosVfPCILOMPortsConfigurationPropAcl = _CucsBiosVfPCILOMPortsConfigurationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 89, 1, 6),
    _CucsBiosVfPCILOMPortsConfigurationPropAcl_Type()
)
cucsBiosVfPCILOMPortsConfigurationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfPCILOMPortsConfigurationPropAcl.setStatus("current")
_CucsBiosVfTPMPendingOperationTable_Object = MibTable
cucsBiosVfTPMPendingOperationTable = _CucsBiosVfTPMPendingOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90)
)
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationTable.setStatus("current")
_CucsBiosVfTPMPendingOperationEntry_Object = MibTableRow
cucsBiosVfTPMPendingOperationEntry = _CucsBiosVfTPMPendingOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1)
)
cucsBiosVfTPMPendingOperationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfTPMPendingOperationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationEntry.setStatus("current")
_CucsBiosVfTPMPendingOperationInstanceId_Type = CucsManagedObjectId
_CucsBiosVfTPMPendingOperationInstanceId_Object = MibTableColumn
cucsBiosVfTPMPendingOperationInstanceId = _CucsBiosVfTPMPendingOperationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 1),
    _CucsBiosVfTPMPendingOperationInstanceId_Type()
)
cucsBiosVfTPMPendingOperationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationInstanceId.setStatus("current")
_CucsBiosVfTPMPendingOperationDn_Type = CucsManagedObjectDn
_CucsBiosVfTPMPendingOperationDn_Object = MibTableColumn
cucsBiosVfTPMPendingOperationDn = _CucsBiosVfTPMPendingOperationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 2),
    _CucsBiosVfTPMPendingOperationDn_Type()
)
cucsBiosVfTPMPendingOperationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationDn.setStatus("current")
_CucsBiosVfTPMPendingOperationRn_Type = SnmpAdminString
_CucsBiosVfTPMPendingOperationRn_Object = MibTableColumn
cucsBiosVfTPMPendingOperationRn = _CucsBiosVfTPMPendingOperationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 3),
    _CucsBiosVfTPMPendingOperationRn_Type()
)
cucsBiosVfTPMPendingOperationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationRn.setStatus("current")
_CucsBiosVfTPMPendingOperationVpTPMPendingOperation_Type = CucsBiosVfTPMPendingOperationVpTPMPendingOperation
_CucsBiosVfTPMPendingOperationVpTPMPendingOperation_Object = MibTableColumn
cucsBiosVfTPMPendingOperationVpTPMPendingOperation = _CucsBiosVfTPMPendingOperationVpTPMPendingOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 4),
    _CucsBiosVfTPMPendingOperationVpTPMPendingOperation_Type()
)
cucsBiosVfTPMPendingOperationVpTPMPendingOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationVpTPMPendingOperation.setStatus("current")
_CucsBiosVfTPMPendingOperationSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfTPMPendingOperationSupportedByDefault_Object = MibTableColumn
cucsBiosVfTPMPendingOperationSupportedByDefault = _CucsBiosVfTPMPendingOperationSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 5),
    _CucsBiosVfTPMPendingOperationSupportedByDefault_Type()
)
cucsBiosVfTPMPendingOperationSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationSupportedByDefault.setStatus("current")
_CucsBiosVfTPMPendingOperationPropAcl_Type = Unsigned64
_CucsBiosVfTPMPendingOperationPropAcl_Object = MibTableColumn
cucsBiosVfTPMPendingOperationPropAcl = _CucsBiosVfTPMPendingOperationPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 90, 1, 6),
    _CucsBiosVfTPMPendingOperationPropAcl_Type()
)
cucsBiosVfTPMPendingOperationPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTPMPendingOperationPropAcl.setStatus("current")
_CucsBiosVfTrustedPlatformModuleTable_Object = MibTable
cucsBiosVfTrustedPlatformModuleTable = _CucsBiosVfTrustedPlatformModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91)
)
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleTable.setStatus("current")
_CucsBiosVfTrustedPlatformModuleEntry_Object = MibTableRow
cucsBiosVfTrustedPlatformModuleEntry = _CucsBiosVfTrustedPlatformModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1)
)
cucsBiosVfTrustedPlatformModuleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfTrustedPlatformModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleEntry.setStatus("current")
_CucsBiosVfTrustedPlatformModuleInstanceId_Type = CucsManagedObjectId
_CucsBiosVfTrustedPlatformModuleInstanceId_Object = MibTableColumn
cucsBiosVfTrustedPlatformModuleInstanceId = _CucsBiosVfTrustedPlatformModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 1),
    _CucsBiosVfTrustedPlatformModuleInstanceId_Type()
)
cucsBiosVfTrustedPlatformModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleInstanceId.setStatus("current")
_CucsBiosVfTrustedPlatformModuleDn_Type = CucsManagedObjectDn
_CucsBiosVfTrustedPlatformModuleDn_Object = MibTableColumn
cucsBiosVfTrustedPlatformModuleDn = _CucsBiosVfTrustedPlatformModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 2),
    _CucsBiosVfTrustedPlatformModuleDn_Type()
)
cucsBiosVfTrustedPlatformModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleDn.setStatus("current")
_CucsBiosVfTrustedPlatformModuleRn_Type = SnmpAdminString
_CucsBiosVfTrustedPlatformModuleRn_Object = MibTableColumn
cucsBiosVfTrustedPlatformModuleRn = _CucsBiosVfTrustedPlatformModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 3),
    _CucsBiosVfTrustedPlatformModuleRn_Type()
)
cucsBiosVfTrustedPlatformModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleRn.setStatus("current")
_CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport_Type = CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport
_CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport_Object = MibTableColumn
cucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport = _CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 4),
    _CucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport_Type()
)
cucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport.setStatus("current")
_CucsBiosVfTrustedPlatformModuleSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfTrustedPlatformModuleSupportedByDefault_Object = MibTableColumn
cucsBiosVfTrustedPlatformModuleSupportedByDefault = _CucsBiosVfTrustedPlatformModuleSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 5),
    _CucsBiosVfTrustedPlatformModuleSupportedByDefault_Type()
)
cucsBiosVfTrustedPlatformModuleSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModuleSupportedByDefault.setStatus("current")
_CucsBiosVfTrustedPlatformModulePropAcl_Type = Unsigned64
_CucsBiosVfTrustedPlatformModulePropAcl_Object = MibTableColumn
cucsBiosVfTrustedPlatformModulePropAcl = _CucsBiosVfTrustedPlatformModulePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 91, 1, 6),
    _CucsBiosVfTrustedPlatformModulePropAcl_Type()
)
cucsBiosVfTrustedPlatformModulePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfTrustedPlatformModulePropAcl.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementTable_Object = MibTable
cucsBiosVfCPUHardwarePowerManagementTable = _CucsBiosVfCPUHardwarePowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92)
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementTable.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementEntry_Object = MibTableRow
cucsBiosVfCPUHardwarePowerManagementEntry = _CucsBiosVfCPUHardwarePowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1)
)
cucsBiosVfCPUHardwarePowerManagementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfCPUHardwarePowerManagementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementEntry.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementInstanceId_Type = CucsManagedObjectId
_CucsBiosVfCPUHardwarePowerManagementInstanceId_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementInstanceId = _CucsBiosVfCPUHardwarePowerManagementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 1),
    _CucsBiosVfCPUHardwarePowerManagementInstanceId_Type()
)
cucsBiosVfCPUHardwarePowerManagementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementInstanceId.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementDn_Type = CucsManagedObjectDn
_CucsBiosVfCPUHardwarePowerManagementDn_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementDn = _CucsBiosVfCPUHardwarePowerManagementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 2),
    _CucsBiosVfCPUHardwarePowerManagementDn_Type()
)
cucsBiosVfCPUHardwarePowerManagementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementDn.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementRn_Type = SnmpAdminString
_CucsBiosVfCPUHardwarePowerManagementRn_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementRn = _CucsBiosVfCPUHardwarePowerManagementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 3),
    _CucsBiosVfCPUHardwarePowerManagementRn_Type()
)
cucsBiosVfCPUHardwarePowerManagementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementRn.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfCPUHardwarePowerManagementSupportedByDefault_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementSupportedByDefault = _CucsBiosVfCPUHardwarePowerManagementSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 4),
    _CucsBiosVfCPUHardwarePowerManagementSupportedByDefault_Type()
)
cucsBiosVfCPUHardwarePowerManagementSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementSupportedByDefault.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement_Type = CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement
_CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement = _CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 5),
    _CucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement_Type()
)
cucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement.setStatus("current")
_CucsBiosVfCPUHardwarePowerManagementPropAcl_Type = Unsigned64
_CucsBiosVfCPUHardwarePowerManagementPropAcl_Object = MibTableColumn
cucsBiosVfCPUHardwarePowerManagementPropAcl = _CucsBiosVfCPUHardwarePowerManagementPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 92, 1, 6),
    _CucsBiosVfCPUHardwarePowerManagementPropAcl_Type()
)
cucsBiosVfCPUHardwarePowerManagementPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfCPUHardwarePowerManagementPropAcl.setStatus("current")
_CucsBiosVfIntegratedGraphicsTable_Object = MibTable
cucsBiosVfIntegratedGraphicsTable = _CucsBiosVfIntegratedGraphicsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsTable.setStatus("current")
_CucsBiosVfIntegratedGraphicsEntry_Object = MibTableRow
cucsBiosVfIntegratedGraphicsEntry = _CucsBiosVfIntegratedGraphicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1)
)
cucsBiosVfIntegratedGraphicsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntegratedGraphicsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsEntry.setStatus("current")
_CucsBiosVfIntegratedGraphicsInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntegratedGraphicsInstanceId_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsInstanceId = _CucsBiosVfIntegratedGraphicsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 1),
    _CucsBiosVfIntegratedGraphicsInstanceId_Type()
)
cucsBiosVfIntegratedGraphicsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsInstanceId.setStatus("current")
_CucsBiosVfIntegratedGraphicsDn_Type = CucsManagedObjectDn
_CucsBiosVfIntegratedGraphicsDn_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsDn = _CucsBiosVfIntegratedGraphicsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 2),
    _CucsBiosVfIntegratedGraphicsDn_Type()
)
cucsBiosVfIntegratedGraphicsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsDn.setStatus("current")
_CucsBiosVfIntegratedGraphicsRn_Type = SnmpAdminString
_CucsBiosVfIntegratedGraphicsRn_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsRn = _CucsBiosVfIntegratedGraphicsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 3),
    _CucsBiosVfIntegratedGraphicsRn_Type()
)
cucsBiosVfIntegratedGraphicsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsRn.setStatus("current")
_CucsBiosVfIntegratedGraphicsSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntegratedGraphicsSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsSupportedByDefault = _CucsBiosVfIntegratedGraphicsSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 4),
    _CucsBiosVfIntegratedGraphicsSupportedByDefault_Type()
)
cucsBiosVfIntegratedGraphicsSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsSupportedByDefault.setStatus("current")
_CucsBiosVfIntegratedGraphicsVpIntegratedGraphics_Type = CucsBiosVfIntegratedGraphicsVpIntegratedGraphics
_CucsBiosVfIntegratedGraphicsVpIntegratedGraphics_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsVpIntegratedGraphics = _CucsBiosVfIntegratedGraphicsVpIntegratedGraphics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 5),
    _CucsBiosVfIntegratedGraphicsVpIntegratedGraphics_Type()
)
cucsBiosVfIntegratedGraphicsVpIntegratedGraphics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsVpIntegratedGraphics.setStatus("current")
_CucsBiosVfIntegratedGraphicsPropAcl_Type = Unsigned64
_CucsBiosVfIntegratedGraphicsPropAcl_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsPropAcl = _CucsBiosVfIntegratedGraphicsPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 93, 1, 6),
    _CucsBiosVfIntegratedGraphicsPropAcl_Type()
)
cucsBiosVfIntegratedGraphicsPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsPropAcl.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeTable_Object = MibTable
cucsBiosVfIntegratedGraphicsApertureSizeTable = _CucsBiosVfIntegratedGraphicsApertureSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94)
)
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeTable.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeEntry_Object = MibTableRow
cucsBiosVfIntegratedGraphicsApertureSizeEntry = _CucsBiosVfIntegratedGraphicsApertureSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1)
)
cucsBiosVfIntegratedGraphicsApertureSizeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfIntegratedGraphicsApertureSizeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeEntry.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeInstanceId_Type = CucsManagedObjectId
_CucsBiosVfIntegratedGraphicsApertureSizeInstanceId_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizeInstanceId = _CucsBiosVfIntegratedGraphicsApertureSizeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 1),
    _CucsBiosVfIntegratedGraphicsApertureSizeInstanceId_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeInstanceId.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeDn_Type = CucsManagedObjectDn
_CucsBiosVfIntegratedGraphicsApertureSizeDn_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizeDn = _CucsBiosVfIntegratedGraphicsApertureSizeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 2),
    _CucsBiosVfIntegratedGraphicsApertureSizeDn_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeDn.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeRn_Type = SnmpAdminString
_CucsBiosVfIntegratedGraphicsApertureSizeRn_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizeRn = _CucsBiosVfIntegratedGraphicsApertureSizeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 3),
    _CucsBiosVfIntegratedGraphicsApertureSizeRn_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeRn.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault = _CucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 4),
    _CucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize_Type = CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize
_CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize = _CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 5),
    _CucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize.setStatus("current")
_CucsBiosVfIntegratedGraphicsApertureSizePropAcl_Type = Unsigned64
_CucsBiosVfIntegratedGraphicsApertureSizePropAcl_Object = MibTableColumn
cucsBiosVfIntegratedGraphicsApertureSizePropAcl = _CucsBiosVfIntegratedGraphicsApertureSizePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 94, 1, 6),
    _CucsBiosVfIntegratedGraphicsApertureSizePropAcl_Type()
)
cucsBiosVfIntegratedGraphicsApertureSizePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfIntegratedGraphicsApertureSizePropAcl.setStatus("current")
_CucsBiosVfOnboardGraphicsTable_Object = MibTable
cucsBiosVfOnboardGraphicsTable = _CucsBiosVfOnboardGraphicsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95)
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsTable.setStatus("current")
_CucsBiosVfOnboardGraphicsEntry_Object = MibTableRow
cucsBiosVfOnboardGraphicsEntry = _CucsBiosVfOnboardGraphicsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1)
)
cucsBiosVfOnboardGraphicsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BIOS-MIB", "cucsBiosVfOnboardGraphicsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsEntry.setStatus("current")
_CucsBiosVfOnboardGraphicsInstanceId_Type = CucsManagedObjectId
_CucsBiosVfOnboardGraphicsInstanceId_Object = MibTableColumn
cucsBiosVfOnboardGraphicsInstanceId = _CucsBiosVfOnboardGraphicsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 1),
    _CucsBiosVfOnboardGraphicsInstanceId_Type()
)
cucsBiosVfOnboardGraphicsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsInstanceId.setStatus("current")
_CucsBiosVfOnboardGraphicsDn_Type = CucsManagedObjectDn
_CucsBiosVfOnboardGraphicsDn_Object = MibTableColumn
cucsBiosVfOnboardGraphicsDn = _CucsBiosVfOnboardGraphicsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 2),
    _CucsBiosVfOnboardGraphicsDn_Type()
)
cucsBiosVfOnboardGraphicsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsDn.setStatus("current")
_CucsBiosVfOnboardGraphicsRn_Type = SnmpAdminString
_CucsBiosVfOnboardGraphicsRn_Object = MibTableColumn
cucsBiosVfOnboardGraphicsRn = _CucsBiosVfOnboardGraphicsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 3),
    _CucsBiosVfOnboardGraphicsRn_Type()
)
cucsBiosVfOnboardGraphicsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsRn.setStatus("current")
_CucsBiosVfOnboardGraphicsSupportedByDefault_Type = CucsBiosSupportedAction
_CucsBiosVfOnboardGraphicsSupportedByDefault_Object = MibTableColumn
cucsBiosVfOnboardGraphicsSupportedByDefault = _CucsBiosVfOnboardGraphicsSupportedByDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 4),
    _CucsBiosVfOnboardGraphicsSupportedByDefault_Type()
)
cucsBiosVfOnboardGraphicsSupportedByDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsSupportedByDefault.setStatus("current")
_CucsBiosVfOnboardGraphicsVpOnboardGraphics_Type = CucsBiosVfOnboardGraphicsVpOnboardGraphics
_CucsBiosVfOnboardGraphicsVpOnboardGraphics_Object = MibTableColumn
cucsBiosVfOnboardGraphicsVpOnboardGraphics = _CucsBiosVfOnboardGraphicsVpOnboardGraphics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 5),
    _CucsBiosVfOnboardGraphicsVpOnboardGraphics_Type()
)
cucsBiosVfOnboardGraphicsVpOnboardGraphics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsVpOnboardGraphics.setStatus("current")
_CucsBiosVfOnboardGraphicsPropAcl_Type = Unsigned64
_CucsBiosVfOnboardGraphicsPropAcl_Object = MibTableColumn
cucsBiosVfOnboardGraphicsPropAcl = _CucsBiosVfOnboardGraphicsPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 4, 95, 1, 6),
    _CucsBiosVfOnboardGraphicsPropAcl_Type()
)
cucsBiosVfOnboardGraphicsPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBiosVfOnboardGraphicsPropAcl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-BIOS-MIB",
    **{"cucsBiosObjects": cucsBiosObjects,
       "cucsBiosBOTTable": cucsBiosBOTTable,
       "cucsBiosBOTEntry": cucsBiosBOTEntry,
       "cucsBiosBOTInstanceId": cucsBiosBOTInstanceId,
       "cucsBiosBOTDn": cucsBiosBOTDn,
       "cucsBiosBOTRn": cucsBiosBOTRn,
       "cucsBiosBOTLastUpdate": cucsBiosBOTLastUpdate,
       "cucsBiosBootDevTable": cucsBiosBootDevTable,
       "cucsBiosBootDevEntry": cucsBiosBootDevEntry,
       "cucsBiosBootDevInstanceId": cucsBiosBootDevInstanceId,
       "cucsBiosBootDevDn": cucsBiosBootDevDn,
       "cucsBiosBootDevRn": cucsBiosBootDevRn,
       "cucsBiosBootDevDescr": cucsBiosBootDevDescr,
       "cucsBiosBootDevOrder": cucsBiosBootDevOrder,
       "cucsBiosBootDevDeviceName": cucsBiosBootDevDeviceName,
       "cucsBiosBootDevErrValue": cucsBiosBootDevErrValue,
       "cucsBiosBootDevGrpTable": cucsBiosBootDevGrpTable,
       "cucsBiosBootDevGrpEntry": cucsBiosBootDevGrpEntry,
       "cucsBiosBootDevGrpInstanceId": cucsBiosBootDevGrpInstanceId,
       "cucsBiosBootDevGrpDn": cucsBiosBootDevGrpDn,
       "cucsBiosBootDevGrpRn": cucsBiosBootDevGrpRn,
       "cucsBiosBootDevGrpDescr": cucsBiosBootDevGrpDescr,
       "cucsBiosBootDevGrpOrder": cucsBiosBootDevGrpOrder,
       "cucsBiosBootDevGrpType": cucsBiosBootDevGrpType,
       "cucsBiosBootDevGrpDeviceName": cucsBiosBootDevGrpDeviceName,
       "cucsBiosBootDevGrpErrVal": cucsBiosBootDevGrpErrVal,
       "cucsBiosFeatureRefTable": cucsBiosFeatureRefTable,
       "cucsBiosFeatureRefEntry": cucsBiosFeatureRefEntry,
       "cucsBiosFeatureRefInstanceId": cucsBiosFeatureRefInstanceId,
       "cucsBiosFeatureRefDn": cucsBiosFeatureRefDn,
       "cucsBiosFeatureRefRn": cucsBiosFeatureRefRn,
       "cucsBiosFeatureRefIsSupported": cucsBiosFeatureRefIsSupported,
       "cucsBiosFeatureRefName": cucsBiosFeatureRefName,
       "cucsBiosFeatureRefFtrMoClassName": cucsBiosFeatureRefFtrMoClassName,
       "cucsBiosParameterRefTable": cucsBiosParameterRefTable,
       "cucsBiosParameterRefEntry": cucsBiosParameterRefEntry,
       "cucsBiosParameterRefInstanceId": cucsBiosParameterRefInstanceId,
       "cucsBiosParameterRefDn": cucsBiosParameterRefDn,
       "cucsBiosParameterRefRn": cucsBiosParameterRefRn,
       "cucsBiosParameterRefIsSupported": cucsBiosParameterRefIsSupported,
       "cucsBiosParameterRefName": cucsBiosParameterRefName,
       "cucsBiosParameterRefPropertyName": cucsBiosParameterRefPropertyName,
       "cucsBiosRefTable": cucsBiosRefTable,
       "cucsBiosRefEntry": cucsBiosRefEntry,
       "cucsBiosRefInstanceId": cucsBiosRefInstanceId,
       "cucsBiosRefDn": cucsBiosRefDn,
       "cucsBiosRefRn": cucsBiosRefRn,
       "cucsBiosRefIsSupported": cucsBiosRefIsSupported,
       "cucsBiosSettingRefTable": cucsBiosSettingRefTable,
       "cucsBiosSettingRefEntry": cucsBiosSettingRefEntry,
       "cucsBiosSettingRefInstanceId": cucsBiosSettingRefInstanceId,
       "cucsBiosSettingRefDn": cucsBiosSettingRefDn,
       "cucsBiosSettingRefRn": cucsBiosSettingRefRn,
       "cucsBiosSettingRefIsDefault": cucsBiosSettingRefIsDefault,
       "cucsBiosSettingRefIsSupported": cucsBiosSettingRefIsSupported,
       "cucsBiosSettingRefName": cucsBiosSettingRefName,
       "cucsBiosSettingRefConstantName": cucsBiosSettingRefConstantName,
       "cucsBiosSettingsTable": cucsBiosSettingsTable,
       "cucsBiosSettingsEntry": cucsBiosSettingsEntry,
       "cucsBiosSettingsInstanceId": cucsBiosSettingsInstanceId,
       "cucsBiosSettingsDn": cucsBiosSettingsDn,
       "cucsBiosSettingsRn": cucsBiosSettingsRn,
       "cucsBiosSettingsPropAcl": cucsBiosSettingsPropAcl,
       "cucsBiosUnitTable": cucsBiosUnitTable,
       "cucsBiosUnitEntry": cucsBiosUnitEntry,
       "cucsBiosUnitInstanceId": cucsBiosUnitInstanceId,
       "cucsBiosUnitDn": cucsBiosUnitDn,
       "cucsBiosUnitRn": cucsBiosUnitRn,
       "cucsBiosUnitInitSeq": cucsBiosUnitInitSeq,
       "cucsBiosUnitInitTs": cucsBiosUnitInitTs,
       "cucsBiosUnitModel": cucsBiosUnitModel,
       "cucsBiosUnitRevision": cucsBiosUnitRevision,
       "cucsBiosUnitSerial": cucsBiosUnitSerial,
       "cucsBiosUnitVendor": cucsBiosUnitVendor,
       "cucsBiosVProfileTable": cucsBiosVProfileTable,
       "cucsBiosVProfileEntry": cucsBiosVProfileEntry,
       "cucsBiosVProfileInstanceId": cucsBiosVProfileInstanceId,
       "cucsBiosVProfileDn": cucsBiosVProfileDn,
       "cucsBiosVProfileRn": cucsBiosVProfileRn,
       "cucsBiosVProfileDescr": cucsBiosVProfileDescr,
       "cucsBiosVProfileIntId": cucsBiosVProfileIntId,
       "cucsBiosVProfileName": cucsBiosVProfileName,
       "cucsBiosVProfileRebootOnUpdate": cucsBiosVProfileRebootOnUpdate,
       "cucsBiosVProfilePolicyLevel": cucsBiosVProfilePolicyLevel,
       "cucsBiosVProfilePolicyOwner": cucsBiosVProfilePolicyOwner,
       "cucsBiosVfConsoleRedirectionTable": cucsBiosVfConsoleRedirectionTable,
       "cucsBiosVfConsoleRedirectionEntry": cucsBiosVfConsoleRedirectionEntry,
       "cucsBiosVfConsoleRedirectionInstanceId": cucsBiosVfConsoleRedirectionInstanceId,
       "cucsBiosVfConsoleRedirectionDn": cucsBiosVfConsoleRedirectionDn,
       "cucsBiosVfConsoleRedirectionRn": cucsBiosVfConsoleRedirectionRn,
       "cucsBiosVfConsoleRedirectionVpBaudRate": cucsBiosVfConsoleRedirectionVpBaudRate,
       "cucsBiosVfConsoleRedirectionVpConsoleRedirection": cucsBiosVfConsoleRedirectionVpConsoleRedirection,
       "cucsBiosVfConsoleRedirectionVpFlowControl": cucsBiosVfConsoleRedirectionVpFlowControl,
       "cucsBiosVfConsoleRedirectionVpLegacyOSRedirection": cucsBiosVfConsoleRedirectionVpLegacyOSRedirection,
       "cucsBiosVfConsoleRedirectionVpTerminalType": cucsBiosVfConsoleRedirectionVpTerminalType,
       "cucsBiosVfConsoleRedirectionVpPuttyKeyPad": cucsBiosVfConsoleRedirectionVpPuttyKeyPad,
       "cucsBiosVfConsoleRedirectionPropAcl": cucsBiosVfConsoleRedirectionPropAcl,
       "cucsBiosVfConsoleRedirectionSupportedByDefault": cucsBiosVfConsoleRedirectionSupportedByDefault,
       "cucsBiosVfOptionROMLoadTable": cucsBiosVfOptionROMLoadTable,
       "cucsBiosVfOptionROMLoadEntry": cucsBiosVfOptionROMLoadEntry,
       "cucsBiosVfOptionROMLoadInstanceId": cucsBiosVfOptionROMLoadInstanceId,
       "cucsBiosVfOptionROMLoadDn": cucsBiosVfOptionROMLoadDn,
       "cucsBiosVfOptionROMLoadRn": cucsBiosVfOptionROMLoadRn,
       "cucsBiosVfOptionROMLoadVpLoad": cucsBiosVfOptionROMLoadVpLoad,
       "cucsBiosVfOptionROMLoadPropAcl": cucsBiosVfOptionROMLoadPropAcl,
       "cucsBiosVfOptionROMLoadSupportedByDefault": cucsBiosVfOptionROMLoadSupportedByDefault,
       "cucsBiosVfEnhancedIntelSpeedStepTechTable": cucsBiosVfEnhancedIntelSpeedStepTechTable,
       "cucsBiosVfEnhancedIntelSpeedStepTechEntry": cucsBiosVfEnhancedIntelSpeedStepTechEntry,
       "cucsBiosVfEnhancedIntelSpeedStepTechInstanceId": cucsBiosVfEnhancedIntelSpeedStepTechInstanceId,
       "cucsBiosVfEnhancedIntelSpeedStepTechDn": cucsBiosVfEnhancedIntelSpeedStepTechDn,
       "cucsBiosVfEnhancedIntelSpeedStepTechRn": cucsBiosVfEnhancedIntelSpeedStepTechRn,
       "cucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech": cucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech,
       "cucsBiosVfEnhancedIntelSpeedStepTechPropAcl": cucsBiosVfEnhancedIntelSpeedStepTechPropAcl,
       "cucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault": cucsBiosVfEnhancedIntelSpeedStepTechSupportedByDefault,
       "cucsBiosVfFrontPanelLockoutTable": cucsBiosVfFrontPanelLockoutTable,
       "cucsBiosVfFrontPanelLockoutEntry": cucsBiosVfFrontPanelLockoutEntry,
       "cucsBiosVfFrontPanelLockoutInstanceId": cucsBiosVfFrontPanelLockoutInstanceId,
       "cucsBiosVfFrontPanelLockoutDn": cucsBiosVfFrontPanelLockoutDn,
       "cucsBiosVfFrontPanelLockoutRn": cucsBiosVfFrontPanelLockoutRn,
       "cucsBiosVfFrontPanelLockoutVpFrontPanelLockout": cucsBiosVfFrontPanelLockoutVpFrontPanelLockout,
       "cucsBiosVfFrontPanelLockoutPropAcl": cucsBiosVfFrontPanelLockoutPropAcl,
       "cucsBiosVfFrontPanelLockoutSupportedByDefault": cucsBiosVfFrontPanelLockoutSupportedByDefault,
       "cucsBiosVfIntelHyperThreadingTechTable": cucsBiosVfIntelHyperThreadingTechTable,
       "cucsBiosVfIntelHyperThreadingTechEntry": cucsBiosVfIntelHyperThreadingTechEntry,
       "cucsBiosVfIntelHyperThreadingTechInstanceId": cucsBiosVfIntelHyperThreadingTechInstanceId,
       "cucsBiosVfIntelHyperThreadingTechDn": cucsBiosVfIntelHyperThreadingTechDn,
       "cucsBiosVfIntelHyperThreadingTechRn": cucsBiosVfIntelHyperThreadingTechRn,
       "cucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech": cucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech,
       "cucsBiosVfIntelHyperThreadingTechPropAcl": cucsBiosVfIntelHyperThreadingTechPropAcl,
       "cucsBiosVfIntelHyperThreadingTechSupportedByDefault": cucsBiosVfIntelHyperThreadingTechSupportedByDefault,
       "cucsBiosVfIntelTurboBoostTechTable": cucsBiosVfIntelTurboBoostTechTable,
       "cucsBiosVfIntelTurboBoostTechEntry": cucsBiosVfIntelTurboBoostTechEntry,
       "cucsBiosVfIntelTurboBoostTechInstanceId": cucsBiosVfIntelTurboBoostTechInstanceId,
       "cucsBiosVfIntelTurboBoostTechDn": cucsBiosVfIntelTurboBoostTechDn,
       "cucsBiosVfIntelTurboBoostTechRn": cucsBiosVfIntelTurboBoostTechRn,
       "cucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech": cucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech,
       "cucsBiosVfIntelTurboBoostTechPropAcl": cucsBiosVfIntelTurboBoostTechPropAcl,
       "cucsBiosVfIntelTurboBoostTechSupportedByDefault": cucsBiosVfIntelTurboBoostTechSupportedByDefault,
       "cucsBiosVfIntelVTForDirectedIOTable": cucsBiosVfIntelVTForDirectedIOTable,
       "cucsBiosVfIntelVTForDirectedIOEntry": cucsBiosVfIntelVTForDirectedIOEntry,
       "cucsBiosVfIntelVTForDirectedIOInstanceId": cucsBiosVfIntelVTForDirectedIOInstanceId,
       "cucsBiosVfIntelVTForDirectedIODn": cucsBiosVfIntelVTForDirectedIODn,
       "cucsBiosVfIntelVTForDirectedIORn": cucsBiosVfIntelVTForDirectedIORn,
       "cucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport": cucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport,
       "cucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport": cucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport,
       "cucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping": cucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping,
       "cucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport": cucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport,
       "cucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO": cucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO,
       "cucsBiosVfIntelVTForDirectedIOPropAcl": cucsBiosVfIntelVTForDirectedIOPropAcl,
       "cucsBiosVfIntelVTForDirectedIOSupportedByDefault": cucsBiosVfIntelVTForDirectedIOSupportedByDefault,
       "cucsBiosVfIntelVirtualizationTechnologyTable": cucsBiosVfIntelVirtualizationTechnologyTable,
       "cucsBiosVfIntelVirtualizationTechnologyEntry": cucsBiosVfIntelVirtualizationTechnologyEntry,
       "cucsBiosVfIntelVirtualizationTechnologyInstanceId": cucsBiosVfIntelVirtualizationTechnologyInstanceId,
       "cucsBiosVfIntelVirtualizationTechnologyDn": cucsBiosVfIntelVirtualizationTechnologyDn,
       "cucsBiosVfIntelVirtualizationTechnologyRn": cucsBiosVfIntelVirtualizationTechnologyRn,
       "cucsBiosVpIntelVirtualizationTechnology": cucsBiosVpIntelVirtualizationTechnology,
       "cucsBiosVfIntelVirtualizationTechnologyPropAcl": cucsBiosVfIntelVirtualizationTechnologyPropAcl,
       "cucsBiosVfIntelVirtualizationTechnologySupportedByDefault": cucsBiosVfIntelVirtualizationTechnologySupportedByDefault,
       "cucsBiosVfLvDIMMSupportTable": cucsBiosVfLvDIMMSupportTable,
       "cucsBiosVfLvDIMMSupportEntry": cucsBiosVfLvDIMMSupportEntry,
       "cucsBiosVfLvDIMMSupportInstanceId": cucsBiosVfLvDIMMSupportInstanceId,
       "cucsBiosVfLvDIMMSupportDn": cucsBiosVfLvDIMMSupportDn,
       "cucsBiosVfLvDIMMSupportRn": cucsBiosVfLvDIMMSupportRn,
       "cucsBiosVfLvDIMMSupportVpLvDDRMode": cucsBiosVfLvDIMMSupportVpLvDDRMode,
       "cucsBiosVfLvDIMMSupportPropAcl": cucsBiosVfLvDIMMSupportPropAcl,
       "cucsBiosVfLvDIMMSupportSupportedByDefault": cucsBiosVfLvDIMMSupportSupportedByDefault,
       "cucsBiosVfMirroringModeTable": cucsBiosVfMirroringModeTable,
       "cucsBiosVfMirroringModeEntry": cucsBiosVfMirroringModeEntry,
       "cucsBiosVfMirroringModeInstanceId": cucsBiosVfMirroringModeInstanceId,
       "cucsBiosVfMirroringModeDn": cucsBiosVfMirroringModeDn,
       "cucsBiosVfMirroringModeRn": cucsBiosVfMirroringModeRn,
       "cucsBiosVfMirroringModeVpMirroringMode": cucsBiosVfMirroringModeVpMirroringMode,
       "cucsBiosVfMirroringModePropAcl": cucsBiosVfMirroringModePropAcl,
       "cucsBiosVfMirroringModeSupportedByDefault": cucsBiosVfMirroringModeSupportedByDefault,
       "cucsBiosVfNUMAOptimizedTable": cucsBiosVfNUMAOptimizedTable,
       "cucsBiosVfNUMAOptimizedEntry": cucsBiosVfNUMAOptimizedEntry,
       "cucsBiosVfNUMAOptimizedInstanceId": cucsBiosVfNUMAOptimizedInstanceId,
       "cucsBiosVfNUMAOptimizedDn": cucsBiosVfNUMAOptimizedDn,
       "cucsBiosVfNUMAOptimizedRn": cucsBiosVfNUMAOptimizedRn,
       "cucsBiosVfNUMAOptimizedVpNUMAOptimized": cucsBiosVfNUMAOptimizedVpNUMAOptimized,
       "cucsBiosVfNUMAOptimizedPropAcl": cucsBiosVfNUMAOptimizedPropAcl,
       "cucsBiosVfNUMAOptimizedSupportedByDefault": cucsBiosVfNUMAOptimizedSupportedByDefault,
       "cucsBiosVfProcessorC3ReportTable": cucsBiosVfProcessorC3ReportTable,
       "cucsBiosVfProcessorC3ReportEntry": cucsBiosVfProcessorC3ReportEntry,
       "cucsBiosVfProcessorC3ReportInstanceId": cucsBiosVfProcessorC3ReportInstanceId,
       "cucsBiosVfProcessorC3ReportDn": cucsBiosVfProcessorC3ReportDn,
       "cucsBiosVfProcessorC3ReportRn": cucsBiosVfProcessorC3ReportRn,
       "cucsBiosVfProcessorC3ReportVpProcessorC3Report": cucsBiosVfProcessorC3ReportVpProcessorC3Report,
       "cucsBiosVfProcessorC3ReportPropAcl": cucsBiosVfProcessorC3ReportPropAcl,
       "cucsBiosVfProcessorC3ReportSupportedByDefault": cucsBiosVfProcessorC3ReportSupportedByDefault,
       "cucsBiosVfProcessorC6ReportTable": cucsBiosVfProcessorC6ReportTable,
       "cucsBiosVfProcessorC6ReportEntry": cucsBiosVfProcessorC6ReportEntry,
       "cucsBiosVfProcessorC6ReportInstanceId": cucsBiosVfProcessorC6ReportInstanceId,
       "cucsBiosVfProcessorC6ReportDn": cucsBiosVfProcessorC6ReportDn,
       "cucsBiosVfProcessorC6ReportRn": cucsBiosVfProcessorC6ReportRn,
       "cucsBiosVfProcessorC6ReportVpProcessorC6Report": cucsBiosVfProcessorC6ReportVpProcessorC6Report,
       "cucsBiosVfProcessorC6ReportPropAcl": cucsBiosVfProcessorC6ReportPropAcl,
       "cucsBiosVfProcessorC6ReportSupportedByDefault": cucsBiosVfProcessorC6ReportSupportedByDefault,
       "cucsBiosVfQuietBootTable": cucsBiosVfQuietBootTable,
       "cucsBiosVfQuietBootEntry": cucsBiosVfQuietBootEntry,
       "cucsBiosVfQuietBootInstanceId": cucsBiosVfQuietBootInstanceId,
       "cucsBiosVfQuietBootDn": cucsBiosVfQuietBootDn,
       "cucsBiosVfQuietBootRn": cucsBiosVfQuietBootRn,
       "cucsBiosVfQuietBootVpQuietBoot": cucsBiosVfQuietBootVpQuietBoot,
       "cucsBiosVfQuietBootPropAcl": cucsBiosVfQuietBootPropAcl,
       "cucsBiosVfQuietBootSupportedByDefault": cucsBiosVfQuietBootSupportedByDefault,
       "cucsBiosVfResumeOnACPowerLossTable": cucsBiosVfResumeOnACPowerLossTable,
       "cucsBiosVfResumeOnACPowerLossEntry": cucsBiosVfResumeOnACPowerLossEntry,
       "cucsBiosVfResumeOnACPowerLossInstanceId": cucsBiosVfResumeOnACPowerLossInstanceId,
       "cucsBiosVfResumeOnACPowerLossDn": cucsBiosVfResumeOnACPowerLossDn,
       "cucsBiosVfResumeOnACPowerLossRn": cucsBiosVfResumeOnACPowerLossRn,
       "cucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss": cucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss,
       "cucsBiosVfResumeOnACPowerLossPropAcl": cucsBiosVfResumeOnACPowerLossPropAcl,
       "cucsBiosVfResumeOnACPowerLossSupportedByDefault": cucsBiosVfResumeOnACPowerLossSupportedByDefault,
       "cucsBiosVfSelectMemoryRASConfigurationTable": cucsBiosVfSelectMemoryRASConfigurationTable,
       "cucsBiosVfSelectMemoryRASConfigurationEntry": cucsBiosVfSelectMemoryRASConfigurationEntry,
       "cucsBiosVfSelectMemoryRASConfigurationInstanceId": cucsBiosVfSelectMemoryRASConfigurationInstanceId,
       "cucsBiosVfSelectMemoryRASConfigurationDn": cucsBiosVfSelectMemoryRASConfigurationDn,
       "cucsBiosVfSelectMemoryRASConfigurationRn": cucsBiosVfSelectMemoryRASConfigurationRn,
       "cucsBiosVpSelectMemoryRASConfiguration": cucsBiosVpSelectMemoryRASConfiguration,
       "cucsBiosVfSelectMemoryRASConfigurationPropAcl": cucsBiosVfSelectMemoryRASConfigurationPropAcl,
       "cucsBiosVfSelectMemoryRASConfigurationSupportedByDefault": cucsBiosVfSelectMemoryRASConfigurationSupportedByDefault,
       "cucsBiosVfACPI10SupportTable": cucsBiosVfACPI10SupportTable,
       "cucsBiosVfACPI10SupportEntry": cucsBiosVfACPI10SupportEntry,
       "cucsBiosVfACPI10SupportInstanceId": cucsBiosVfACPI10SupportInstanceId,
       "cucsBiosVfACPI10SupportDn": cucsBiosVfACPI10SupportDn,
       "cucsBiosVfACPI10SupportRn": cucsBiosVfACPI10SupportRn,
       "cucsBiosVfACPI10SupportVpACPI10Support": cucsBiosVfACPI10SupportVpACPI10Support,
       "cucsBiosVfACPI10SupportPropAcl": cucsBiosVfACPI10SupportPropAcl,
       "cucsBiosVfACPI10SupportSupportedByDefault": cucsBiosVfACPI10SupportSupportedByDefault,
       "cucsBiosVfAssertNMIOnPERRTable": cucsBiosVfAssertNMIOnPERRTable,
       "cucsBiosVfAssertNMIOnPERREntry": cucsBiosVfAssertNMIOnPERREntry,
       "cucsBiosVfAssertNMIOnPERRInstanceId": cucsBiosVfAssertNMIOnPERRInstanceId,
       "cucsBiosVfAssertNMIOnPERRDn": cucsBiosVfAssertNMIOnPERRDn,
       "cucsBiosVfAssertNMIOnPERRRn": cucsBiosVfAssertNMIOnPERRRn,
       "cucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR": cucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR,
       "cucsBiosVfAssertNMIOnPERRPropAcl": cucsBiosVfAssertNMIOnPERRPropAcl,
       "cucsBiosVfAssertNMIOnPERRSupportedByDefault": cucsBiosVfAssertNMIOnPERRSupportedByDefault,
       "cucsBiosVfAssertNMIOnSERRTable": cucsBiosVfAssertNMIOnSERRTable,
       "cucsBiosVfAssertNMIOnSERREntry": cucsBiosVfAssertNMIOnSERREntry,
       "cucsBiosVfAssertNMIOnSERRInstanceId": cucsBiosVfAssertNMIOnSERRInstanceId,
       "cucsBiosVfAssertNMIOnSERRDn": cucsBiosVfAssertNMIOnSERRDn,
       "cucsBiosVfAssertNMIOnSERRRn": cucsBiosVfAssertNMIOnSERRRn,
       "cucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR": cucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR,
       "cucsBiosVfAssertNMIOnSERRPropAcl": cucsBiosVfAssertNMIOnSERRPropAcl,
       "cucsBiosVfAssertNMIOnSERRSupportedByDefault": cucsBiosVfAssertNMIOnSERRSupportedByDefault,
       "cucsBiosVfCPUPerformanceTable": cucsBiosVfCPUPerformanceTable,
       "cucsBiosVfCPUPerformanceEntry": cucsBiosVfCPUPerformanceEntry,
       "cucsBiosVfCPUPerformanceInstanceId": cucsBiosVfCPUPerformanceInstanceId,
       "cucsBiosVfCPUPerformanceDn": cucsBiosVfCPUPerformanceDn,
       "cucsBiosVfCPUPerformanceRn": cucsBiosVfCPUPerformanceRn,
       "cucsBiosVfCPUPerformanceVpCPUPerformance": cucsBiosVfCPUPerformanceVpCPUPerformance,
       "cucsBiosVfCPUPerformancePropAcl": cucsBiosVfCPUPerformancePropAcl,
       "cucsBiosVfCPUPerformanceSupportedByDefault": cucsBiosVfCPUPerformanceSupportedByDefault,
       "cucsBiosVfBootOptionRetryTable": cucsBiosVfBootOptionRetryTable,
       "cucsBiosVfBootOptionRetryEntry": cucsBiosVfBootOptionRetryEntry,
       "cucsBiosVfBootOptionRetryInstanceId": cucsBiosVfBootOptionRetryInstanceId,
       "cucsBiosVfBootOptionRetryDn": cucsBiosVfBootOptionRetryDn,
       "cucsBiosVfBootOptionRetryRn": cucsBiosVfBootOptionRetryRn,
       "cucsBiosVfBootOptionRetryVpBootOptionRetry": cucsBiosVfBootOptionRetryVpBootOptionRetry,
       "cucsBiosVfBootOptionRetryPropAcl": cucsBiosVfBootOptionRetryPropAcl,
       "cucsBiosVfBootOptionRetrySupportedByDefault": cucsBiosVfBootOptionRetrySupportedByDefault,
       "cucsBiosVfUSBBootConfigTable": cucsBiosVfUSBBootConfigTable,
       "cucsBiosVfUSBBootConfigEntry": cucsBiosVfUSBBootConfigEntry,
       "cucsBiosVfUSBBootConfigInstanceId": cucsBiosVfUSBBootConfigInstanceId,
       "cucsBiosVfUSBBootConfigDn": cucsBiosVfUSBBootConfigDn,
       "cucsBiosVfUSBBootConfigRn": cucsBiosVfUSBBootConfigRn,
       "cucsBiosVfUSBBootConfigVpMakeDeviceNonBootable": cucsBiosVfUSBBootConfigVpMakeDeviceNonBootable,
       "cucsBiosVfUSBBootConfigVpLegacyUSBSupport": cucsBiosVfUSBBootConfigVpLegacyUSBSupport,
       "cucsBiosVfUSBBootConfigPropAcl": cucsBiosVfUSBBootConfigPropAcl,
       "cucsBiosVfUSBBootConfigSupportedByDefault": cucsBiosVfUSBBootConfigSupportedByDefault,
       "cucsBiosVfCoreMultiProcessingTable": cucsBiosVfCoreMultiProcessingTable,
       "cucsBiosVfCoreMultiProcessingEntry": cucsBiosVfCoreMultiProcessingEntry,
       "cucsBiosVfCoreMultiProcessingInstanceId": cucsBiosVfCoreMultiProcessingInstanceId,
       "cucsBiosVfCoreMultiProcessingDn": cucsBiosVfCoreMultiProcessingDn,
       "cucsBiosVfCoreMultiProcessingRn": cucsBiosVfCoreMultiProcessingRn,
       "cucsBiosVfCoreMultiProcessingVpCoreMultiProcessing": cucsBiosVfCoreMultiProcessingVpCoreMultiProcessing,
       "cucsBiosVfCoreMultiProcessingPropAcl": cucsBiosVfCoreMultiProcessingPropAcl,
       "cucsBiosVfCoreMultiProcessingSupportedByDefault": cucsBiosVfCoreMultiProcessingSupportedByDefault,
       "cucsBiosVfUEFIOSUseLegacyVideoTable": cucsBiosVfUEFIOSUseLegacyVideoTable,
       "cucsBiosVfUEFIOSUseLegacyVideoEntry": cucsBiosVfUEFIOSUseLegacyVideoEntry,
       "cucsBiosVfUEFIOSUseLegacyVideoInstanceId": cucsBiosVfUEFIOSUseLegacyVideoInstanceId,
       "cucsBiosVfUEFIOSUseLegacyVideoDn": cucsBiosVfUEFIOSUseLegacyVideoDn,
       "cucsBiosVfUEFIOSUseLegacyVideoRn": cucsBiosVfUEFIOSUseLegacyVideoRn,
       "cucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo": cucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo,
       "cucsBiosVfUEFIOSUseLegacyVideoPropAcl": cucsBiosVfUEFIOSUseLegacyVideoPropAcl,
       "cucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault": cucsBiosVfUEFIOSUseLegacyVideoSupportedByDefault,
       "cucsBiosVfDirectCacheAccessTable": cucsBiosVfDirectCacheAccessTable,
       "cucsBiosVfDirectCacheAccessEntry": cucsBiosVfDirectCacheAccessEntry,
       "cucsBiosVfDirectCacheAccessInstanceId": cucsBiosVfDirectCacheAccessInstanceId,
       "cucsBiosVfDirectCacheAccessDn": cucsBiosVfDirectCacheAccessDn,
       "cucsBiosVfDirectCacheAccessRn": cucsBiosVfDirectCacheAccessRn,
       "cucsBiosVfDirectCacheAccessVpDirectCacheAccess": cucsBiosVfDirectCacheAccessVpDirectCacheAccess,
       "cucsBiosVfDirectCacheAccessPropAcl": cucsBiosVfDirectCacheAccessPropAcl,
       "cucsBiosVfDirectCacheAccessSupportedByDefault": cucsBiosVfDirectCacheAccessSupportedByDefault,
       "cucsBiosVfExecuteDisableBitTable": cucsBiosVfExecuteDisableBitTable,
       "cucsBiosVfExecuteDisableBitEntry": cucsBiosVfExecuteDisableBitEntry,
       "cucsBiosVfExecuteDisableBitInstanceId": cucsBiosVfExecuteDisableBitInstanceId,
       "cucsBiosVfExecuteDisableBitDn": cucsBiosVfExecuteDisableBitDn,
       "cucsBiosVfExecuteDisableBitRn": cucsBiosVfExecuteDisableBitRn,
       "cucsBiosVfExecuteDisableBitVpExecuteDisableBit": cucsBiosVfExecuteDisableBitVpExecuteDisableBit,
       "cucsBiosVfExecuteDisableBitPropAcl": cucsBiosVfExecuteDisableBitPropAcl,
       "cucsBiosVfExecuteDisableBitSupportedByDefault": cucsBiosVfExecuteDisableBitSupportedByDefault,
       "cucsBiosVfSparingModeTable": cucsBiosVfSparingModeTable,
       "cucsBiosVfSparingModeEntry": cucsBiosVfSparingModeEntry,
       "cucsBiosVfSparingModeInstanceId": cucsBiosVfSparingModeInstanceId,
       "cucsBiosVfSparingModeDn": cucsBiosVfSparingModeDn,
       "cucsBiosVfSparingModeRn": cucsBiosVfSparingModeRn,
       "cucsBiosVfSparingModeVpSparingMode": cucsBiosVfSparingModeVpSparingMode,
       "cucsBiosVfSparingModePropAcl": cucsBiosVfSparingModePropAcl,
       "cucsBiosVfSparingModeSupportedByDefault": cucsBiosVfSparingModeSupportedByDefault,
       "cucsBiosVfSerialPortAEnableTable": cucsBiosVfSerialPortAEnableTable,
       "cucsBiosVfSerialPortAEnableEntry": cucsBiosVfSerialPortAEnableEntry,
       "cucsBiosVfSerialPortAEnableInstanceId": cucsBiosVfSerialPortAEnableInstanceId,
       "cucsBiosVfSerialPortAEnableDn": cucsBiosVfSerialPortAEnableDn,
       "cucsBiosVfSerialPortAEnableRn": cucsBiosVfSerialPortAEnableRn,
       "cucsBiosVfSerialPortAEnableVpSerialPortAEnable": cucsBiosVfSerialPortAEnableVpSerialPortAEnable,
       "cucsBiosVfSerialPortAEnablePropAcl": cucsBiosVfSerialPortAEnablePropAcl,
       "cucsBiosVfSerialPortAEnableSupportedByDefault": cucsBiosVfSerialPortAEnableSupportedByDefault,
       "cucsBiosVfIntelEntrySASRAIDModuleTable": cucsBiosVfIntelEntrySASRAIDModuleTable,
       "cucsBiosVfIntelEntrySASRAIDModuleEntry": cucsBiosVfIntelEntrySASRAIDModuleEntry,
       "cucsBiosVfIntelEntrySASRAIDModuleInstanceId": cucsBiosVfIntelEntrySASRAIDModuleInstanceId,
       "cucsBiosVfIntelEntrySASRAIDModuleDn": cucsBiosVfIntelEntrySASRAIDModuleDn,
       "cucsBiosVfIntelEntrySASRAIDModuleRn": cucsBiosVfIntelEntrySASRAIDModuleRn,
       "cucsBiosVfIntelEntrySASRAIDModuleVpSASRAID": cucsBiosVfIntelEntrySASRAIDModuleVpSASRAID,
       "cucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule": cucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule,
       "cucsBiosVfIntelEntrySASRAIDModulePropAcl": cucsBiosVfIntelEntrySASRAIDModulePropAcl,
       "cucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault": cucsBiosVfIntelEntrySASRAIDModuleSupportedByDefault,
       "cucsBiosVfPOSTErrorPauseTable": cucsBiosVfPOSTErrorPauseTable,
       "cucsBiosVfPOSTErrorPauseEntry": cucsBiosVfPOSTErrorPauseEntry,
       "cucsBiosVfPOSTErrorPauseInstanceId": cucsBiosVfPOSTErrorPauseInstanceId,
       "cucsBiosVfPOSTErrorPauseDn": cucsBiosVfPOSTErrorPauseDn,
       "cucsBiosVfPOSTErrorPauseRn": cucsBiosVfPOSTErrorPauseRn,
       "cucsBiosVfPOSTErrorPauseVpPOSTErrorPause": cucsBiosVfPOSTErrorPauseVpPOSTErrorPause,
       "cucsBiosVfPOSTErrorPausePropAcl": cucsBiosVfPOSTErrorPausePropAcl,
       "cucsBiosVfPOSTErrorPauseSupportedByDefault": cucsBiosVfPOSTErrorPauseSupportedByDefault,
       "cucsBiosVfMaximumMemoryBelow4GBTable": cucsBiosVfMaximumMemoryBelow4GBTable,
       "cucsBiosVfMaximumMemoryBelow4GBEntry": cucsBiosVfMaximumMemoryBelow4GBEntry,
       "cucsBiosVfMaximumMemoryBelow4GBInstanceId": cucsBiosVfMaximumMemoryBelow4GBInstanceId,
       "cucsBiosVfMaximumMemoryBelow4GBDn": cucsBiosVfMaximumMemoryBelow4GBDn,
       "cucsBiosVfMaximumMemoryBelow4GBRn": cucsBiosVfMaximumMemoryBelow4GBRn,
       "cucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB": cucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB,
       "cucsBiosVfMaximumMemoryBelow4GBPropAcl": cucsBiosVfMaximumMemoryBelow4GBPropAcl,
       "cucsBiosVfMaximumMemoryBelow4GBSupportedByDefault": cucsBiosVfMaximumMemoryBelow4GBSupportedByDefault,
       "cucsBiosVfMemoryMappedIOAbove4GBTable": cucsBiosVfMemoryMappedIOAbove4GBTable,
       "cucsBiosVfMemoryMappedIOAbove4GBEntry": cucsBiosVfMemoryMappedIOAbove4GBEntry,
       "cucsBiosVfMemoryMappedIOAbove4GBInstanceId": cucsBiosVfMemoryMappedIOAbove4GBInstanceId,
       "cucsBiosVfMemoryMappedIOAbove4GBDn": cucsBiosVfMemoryMappedIOAbove4GBDn,
       "cucsBiosVfMemoryMappedIOAbove4GBRn": cucsBiosVfMemoryMappedIOAbove4GBRn,
       "cucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB": cucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB,
       "cucsBiosVfMemoryMappedIOAbove4GBPropAcl": cucsBiosVfMemoryMappedIOAbove4GBPropAcl,
       "cucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault": cucsBiosVfMemoryMappedIOAbove4GBSupportedByDefault,
       "cucsBiosVfOSBootWatchdogTimerTable": cucsBiosVfOSBootWatchdogTimerTable,
       "cucsBiosVfOSBootWatchdogTimerEntry": cucsBiosVfOSBootWatchdogTimerEntry,
       "cucsBiosVfOSBootWatchdogTimerInstanceId": cucsBiosVfOSBootWatchdogTimerInstanceId,
       "cucsBiosVfOSBootWatchdogTimerDn": cucsBiosVfOSBootWatchdogTimerDn,
       "cucsBiosVfOSBootWatchdogTimerRn": cucsBiosVfOSBootWatchdogTimerRn,
       "cucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer": cucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer,
       "cucsBiosVfOSBootWatchdogTimerPropAcl": cucsBiosVfOSBootWatchdogTimerPropAcl,
       "cucsBiosVfOSBootWatchdogTimerSupportedByDefault": cucsBiosVfOSBootWatchdogTimerSupportedByDefault,
       "cucsBiosVfOSBootWatchdogTimerPolicyTable": cucsBiosVfOSBootWatchdogTimerPolicyTable,
       "cucsBiosVfOSBootWatchdogTimerPolicyEntry": cucsBiosVfOSBootWatchdogTimerPolicyEntry,
       "cucsBiosVfOSBootWatchdogTimerPolicyInstanceId": cucsBiosVfOSBootWatchdogTimerPolicyInstanceId,
       "cucsBiosVfOSBootWatchdogTimerPolicyDn": cucsBiosVfOSBootWatchdogTimerPolicyDn,
       "cucsBiosVfOSBootWatchdogTimerPolicyRn": cucsBiosVfOSBootWatchdogTimerPolicyRn,
       "cucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy": cucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy,
       "cucsBiosVfOSBootWatchdogTimerPolicyPropAcl": cucsBiosVfOSBootWatchdogTimerPolicyPropAcl,
       "cucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault": cucsBiosVfOSBootWatchdogTimerPolicySupportedByDefault,
       "cucsBiosVfOnboardSATAControllerTable": cucsBiosVfOnboardSATAControllerTable,
       "cucsBiosVfOnboardSATAControllerEntry": cucsBiosVfOnboardSATAControllerEntry,
       "cucsBiosVfOnboardSATAControllerInstanceId": cucsBiosVfOnboardSATAControllerInstanceId,
       "cucsBiosVfOnboardSATAControllerDn": cucsBiosVfOnboardSATAControllerDn,
       "cucsBiosVfOnboardSATAControllerRn": cucsBiosVfOnboardSATAControllerRn,
       "cucsBiosVfOnboardSATAControllerVpOnboardSATAController": cucsBiosVfOnboardSATAControllerVpOnboardSATAController,
       "cucsBiosVfOnboardSATAControllerVpSATAMode": cucsBiosVfOnboardSATAControllerVpSATAMode,
       "cucsBiosVfOnboardSATAControllerPropAcl": cucsBiosVfOnboardSATAControllerPropAcl,
       "cucsBiosVfOnboardSATAControllerSupportedByDefault": cucsBiosVfOnboardSATAControllerSupportedByDefault,
       "cucsBiosVfMaxVariableMTRRSettingTable": cucsBiosVfMaxVariableMTRRSettingTable,
       "cucsBiosVfMaxVariableMTRRSettingEntry": cucsBiosVfMaxVariableMTRRSettingEntry,
       "cucsBiosVfMaxVariableMTRRSettingInstanceId": cucsBiosVfMaxVariableMTRRSettingInstanceId,
       "cucsBiosVfMaxVariableMTRRSettingDn": cucsBiosVfMaxVariableMTRRSettingDn,
       "cucsBiosVfMaxVariableMTRRSettingRn": cucsBiosVfMaxVariableMTRRSettingRn,
       "cucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr": cucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr,
       "cucsBiosVfMaxVariableMTRRSettingPropAcl": cucsBiosVfMaxVariableMTRRSettingPropAcl,
       "cucsBiosVfMaxVariableMTRRSettingSupportedByDefault": cucsBiosVfMaxVariableMTRRSettingSupportedByDefault,
       "cucsBiosVfUCSMBootOrderRuleControlTable": cucsBiosVfUCSMBootOrderRuleControlTable,
       "cucsBiosVfUCSMBootOrderRuleControlEntry": cucsBiosVfUCSMBootOrderRuleControlEntry,
       "cucsBiosVfUCSMBootOrderRuleControlInstanceId": cucsBiosVfUCSMBootOrderRuleControlInstanceId,
       "cucsBiosVfUCSMBootOrderRuleControlDn": cucsBiosVfUCSMBootOrderRuleControlDn,
       "cucsBiosVfUCSMBootOrderRuleControlRn": cucsBiosVfUCSMBootOrderRuleControlRn,
       "cucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule": cucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule,
       "cucsBiosVfUCSMBootOrderRuleControlPropAcl": cucsBiosVfUCSMBootOrderRuleControlPropAcl,
       "cucsBiosVfUCSMBootOrderRuleControlSupportedByDefault": cucsBiosVfUCSMBootOrderRuleControlSupportedByDefault,
       "cucsBiosVfUSBFrontPanelAccessLockTable": cucsBiosVfUSBFrontPanelAccessLockTable,
       "cucsBiosVfUSBFrontPanelAccessLockEntry": cucsBiosVfUSBFrontPanelAccessLockEntry,
       "cucsBiosVfUSBFrontPanelAccessLockInstanceId": cucsBiosVfUSBFrontPanelAccessLockInstanceId,
       "cucsBiosVfUSBFrontPanelAccessLockDn": cucsBiosVfUSBFrontPanelAccessLockDn,
       "cucsBiosVfUSBFrontPanelAccessLockRn": cucsBiosVfUSBFrontPanelAccessLockRn,
       "cucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock": cucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock,
       "cucsBiosVfUSBFrontPanelAccessLockPropAcl": cucsBiosVfUSBFrontPanelAccessLockPropAcl,
       "cucsBiosVfUSBFrontPanelAccessLockSupportedByDefault": cucsBiosVfUSBFrontPanelAccessLockSupportedByDefault,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingTable": cucsBiosVfUSBSystemIdlePowerOptimizingSettingTable,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry": cucsBiosVfUSBSystemIdlePowerOptimizingSettingEntry,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId": cucsBiosVfUSBSystemIdlePowerOptimizingSettingInstanceId,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingDn": cucsBiosVfUSBSystemIdlePowerOptimizingSettingDn,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingRn": cucsBiosVfUSBSystemIdlePowerOptimizingSettingRn,
       "cucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize": cucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl": cucsBiosVfUSBSystemIdlePowerOptimizingSettingPropAcl,
       "cucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault": cucsBiosVfUSBSystemIdlePowerOptimizingSettingSupportedByDefault,
       "cucsBiosVIdentityParamsTable": cucsBiosVIdentityParamsTable,
       "cucsBiosVIdentityParamsEntry": cucsBiosVIdentityParamsEntry,
       "cucsBiosVIdentityParamsInstanceId": cucsBiosVIdentityParamsInstanceId,
       "cucsBiosVIdentityParamsDn": cucsBiosVIdentityParamsDn,
       "cucsBiosVIdentityParamsRn": cucsBiosVIdentityParamsRn,
       "cucsBiosVIdentityParamsLsServerName": cucsBiosVIdentityParamsLsServerName,
       "cucsBiosVIdentityParamsLsServerTmplName": cucsBiosVIdentityParamsLsServerTmplName,
       "cucsBiosVIdentityParamsSysName": cucsBiosVIdentityParamsSysName,
       "cucsBiosVfOSBootWatchdogTimerTimeoutTable": cucsBiosVfOSBootWatchdogTimerTimeoutTable,
       "cucsBiosVfOSBootWatchdogTimerTimeoutEntry": cucsBiosVfOSBootWatchdogTimerTimeoutEntry,
       "cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId": cucsBiosVfOSBootWatchdogTimerTimeoutInstanceId,
       "cucsBiosVfOSBootWatchdogTimerTimeoutDn": cucsBiosVfOSBootWatchdogTimerTimeoutDn,
       "cucsBiosVfOSBootWatchdogTimerTimeoutRn": cucsBiosVfOSBootWatchdogTimerTimeoutRn,
       "cucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout": cucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout,
       "cucsBiosVfOSBootWatchdogTimerTimeoutPropAcl": cucsBiosVfOSBootWatchdogTimerTimeoutPropAcl,
       "cucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault": cucsBiosVfOSBootWatchdogTimerTimeoutSupportedByDefault,
       "cucsBiosVfOnboardStorageTable": cucsBiosVfOnboardStorageTable,
       "cucsBiosVfOnboardStorageEntry": cucsBiosVfOnboardStorageEntry,
       "cucsBiosVfOnboardStorageInstanceId": cucsBiosVfOnboardStorageInstanceId,
       "cucsBiosVfOnboardStorageDn": cucsBiosVfOnboardStorageDn,
       "cucsBiosVfOnboardStorageRn": cucsBiosVfOnboardStorageRn,
       "cucsBiosVfOnboardStorageVpOnboardSCUStorageSupport": cucsBiosVfOnboardStorageVpOnboardSCUStorageSupport,
       "cucsBiosVfOnboardStoragePropAcl": cucsBiosVfOnboardStoragePropAcl,
       "cucsBiosVfOnboardStorageSupportedByDefault": cucsBiosVfOnboardStorageSupportedByDefault,
       "cucsBiosVfOptionROMEnableTable": cucsBiosVfOptionROMEnableTable,
       "cucsBiosVfOptionROMEnableEntry": cucsBiosVfOptionROMEnableEntry,
       "cucsBiosVfOptionROMEnableInstanceId": cucsBiosVfOptionROMEnableInstanceId,
       "cucsBiosVfOptionROMEnableDn": cucsBiosVfOptionROMEnableDn,
       "cucsBiosVfOptionROMEnableRn": cucsBiosVfOptionROMEnableRn,
       "cucsBiosVfOptionROMEnableVpState": cucsBiosVfOptionROMEnableVpState,
       "cucsBiosVfOptionROMEnablePropAcl": cucsBiosVfOptionROMEnablePropAcl,
       "cucsBiosVfOptionROMEnableSupportedByDefault": cucsBiosVfOptionROMEnableSupportedByDefault,
       "cucsBiosVfPCISlotOptionROMEnableTable": cucsBiosVfPCISlotOptionROMEnableTable,
       "cucsBiosVfPCISlotOptionROMEnableEntry": cucsBiosVfPCISlotOptionROMEnableEntry,
       "cucsBiosVfPCISlotOptionROMEnableInstanceId": cucsBiosVfPCISlotOptionROMEnableInstanceId,
       "cucsBiosVfPCISlotOptionROMEnableDn": cucsBiosVfPCISlotOptionROMEnableDn,
       "cucsBiosVfPCISlotOptionROMEnableRn": cucsBiosVfPCISlotOptionROMEnableRn,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot1State": cucsBiosVfPCISlotOptionROMEnableVpSlot1State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot2State": cucsBiosVfPCISlotOptionROMEnableVpSlot2State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot3State": cucsBiosVfPCISlotOptionROMEnableVpSlot3State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot4State": cucsBiosVfPCISlotOptionROMEnableVpSlot4State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot5State": cucsBiosVfPCISlotOptionROMEnableVpSlot5State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlotMezzState": cucsBiosVfPCISlotOptionROMEnableVpSlotMezzState,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot6State": cucsBiosVfPCISlotOptionROMEnableVpSlot6State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot7State": cucsBiosVfPCISlotOptionROMEnableVpSlot7State,
       "cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM": cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotSASOptionROM,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot10State": cucsBiosVfPCISlotOptionROMEnableVpSlot10State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot8State": cucsBiosVfPCISlotOptionROMEnableVpSlot8State,
       "cucsBiosVfPCISlotOptionROMEnableVpSlot9State": cucsBiosVfPCISlotOptionROMEnableVpSlot9State,
       "cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM": cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotHBAOptionROM,
       "cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM": cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotMLOMOptionROM,
       "cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM": cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN1OptionROM,
       "cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM": cucsBiosVfPCISlotOptionROMEnableVpPCIeSlotN2OptionROM,
       "cucsBiosVfPCISlotOptionROMEnablePropAcl": cucsBiosVfPCISlotOptionROMEnablePropAcl,
       "cucsBiosVfPCISlotOptionROMEnableSupportedByDefault": cucsBiosVfPCISlotOptionROMEnableSupportedByDefault,
       "cucsBiosVfPackageCStateLimitTable": cucsBiosVfPackageCStateLimitTable,
       "cucsBiosVfPackageCStateLimitEntry": cucsBiosVfPackageCStateLimitEntry,
       "cucsBiosVfPackageCStateLimitInstanceId": cucsBiosVfPackageCStateLimitInstanceId,
       "cucsBiosVfPackageCStateLimitDn": cucsBiosVfPackageCStateLimitDn,
       "cucsBiosVfPackageCStateLimitRn": cucsBiosVfPackageCStateLimitRn,
       "cucsBiosVfPackageCStateLimitVpPackageCStateLimit": cucsBiosVfPackageCStateLimitVpPackageCStateLimit,
       "cucsBiosVfPackageCStateLimitPropAcl": cucsBiosVfPackageCStateLimitPropAcl,
       "cucsBiosVfPackageCStateLimitSupportedByDefault": cucsBiosVfPackageCStateLimitSupportedByDefault,
       "cucsBiosVfProcessorC1ETable": cucsBiosVfProcessorC1ETable,
       "cucsBiosVfProcessorC1EEntry": cucsBiosVfProcessorC1EEntry,
       "cucsBiosVfProcessorC1EInstanceId": cucsBiosVfProcessorC1EInstanceId,
       "cucsBiosVfProcessorC1EDn": cucsBiosVfProcessorC1EDn,
       "cucsBiosVfProcessorC1ERn": cucsBiosVfProcessorC1ERn,
       "cucsBiosVfProcessorC1EVpProcessorC1E": cucsBiosVfProcessorC1EVpProcessorC1E,
       "cucsBiosVfProcessorC1EPropAcl": cucsBiosVfProcessorC1EPropAcl,
       "cucsBiosVfProcessorC1ESupportedByDefault": cucsBiosVfProcessorC1ESupportedByDefault,
       "cucsBiosVfProcessorC7ReportTable": cucsBiosVfProcessorC7ReportTable,
       "cucsBiosVfProcessorC7ReportEntry": cucsBiosVfProcessorC7ReportEntry,
       "cucsBiosVfProcessorC7ReportInstanceId": cucsBiosVfProcessorC7ReportInstanceId,
       "cucsBiosVfProcessorC7ReportDn": cucsBiosVfProcessorC7ReportDn,
       "cucsBiosVfProcessorC7ReportRn": cucsBiosVfProcessorC7ReportRn,
       "cucsBiosVfProcessorC7ReportVpProcessorC7Report": cucsBiosVfProcessorC7ReportVpProcessorC7Report,
       "cucsBiosVfProcessorC7ReportPropAcl": cucsBiosVfProcessorC7ReportPropAcl,
       "cucsBiosVfProcessorC7ReportSupportedByDefault": cucsBiosVfProcessorC7ReportSupportedByDefault,
       "cucsBiosVfProcessorCStateTable": cucsBiosVfProcessorCStateTable,
       "cucsBiosVfProcessorCStateEntry": cucsBiosVfProcessorCStateEntry,
       "cucsBiosVfProcessorCStateInstanceId": cucsBiosVfProcessorCStateInstanceId,
       "cucsBiosVfProcessorCStateDn": cucsBiosVfProcessorCStateDn,
       "cucsBiosVfProcessorCStateRn": cucsBiosVfProcessorCStateRn,
       "cucsBiosVfProcessorCStateVpProcessorCState": cucsBiosVfProcessorCStateVpProcessorCState,
       "cucsBiosVfProcessorCStatePropAcl": cucsBiosVfProcessorCStatePropAcl,
       "cucsBiosVfProcessorCStateSupportedByDefault": cucsBiosVfProcessorCStateSupportedByDefault,
       "cucsBiosVfSriovConfigTable": cucsBiosVfSriovConfigTable,
       "cucsBiosVfSriovConfigEntry": cucsBiosVfSriovConfigEntry,
       "cucsBiosVfSriovConfigInstanceId": cucsBiosVfSriovConfigInstanceId,
       "cucsBiosVfSriovConfigDn": cucsBiosVfSriovConfigDn,
       "cucsBiosVfSriovConfigRn": cucsBiosVfSriovConfigRn,
       "cucsBiosVfSriovConfigVpSriov": cucsBiosVfSriovConfigVpSriov,
       "cucsBiosVfSriovConfigPropAcl": cucsBiosVfSriovConfigPropAcl,
       "cucsBiosVfSriovConfigSupportedByDefault": cucsBiosVfSriovConfigSupportedByDefault,
       "cucsBiosVfDramRefreshRateTable": cucsBiosVfDramRefreshRateTable,
       "cucsBiosVfDramRefreshRateEntry": cucsBiosVfDramRefreshRateEntry,
       "cucsBiosVfDramRefreshRateInstanceId": cucsBiosVfDramRefreshRateInstanceId,
       "cucsBiosVfDramRefreshRateDn": cucsBiosVfDramRefreshRateDn,
       "cucsBiosVfDramRefreshRateRn": cucsBiosVfDramRefreshRateRn,
       "cucsBiosVfDramRefreshRateVpDramRefreshRate": cucsBiosVfDramRefreshRateVpDramRefreshRate,
       "cucsBiosVfDramRefreshRatePropAcl": cucsBiosVfDramRefreshRatePropAcl,
       "cucsBiosVfDramRefreshRateSupportedByDefault": cucsBiosVfDramRefreshRateSupportedByDefault,
       "cucsBiosVfLocalX2ApicTable": cucsBiosVfLocalX2ApicTable,
       "cucsBiosVfLocalX2ApicEntry": cucsBiosVfLocalX2ApicEntry,
       "cucsBiosVfLocalX2ApicInstanceId": cucsBiosVfLocalX2ApicInstanceId,
       "cucsBiosVfLocalX2ApicDn": cucsBiosVfLocalX2ApicDn,
       "cucsBiosVfLocalX2ApicRn": cucsBiosVfLocalX2ApicRn,
       "cucsBiosVfLocalX2ApicVpLocalX2Apic": cucsBiosVfLocalX2ApicVpLocalX2Apic,
       "cucsBiosVfLocalX2ApicPropAcl": cucsBiosVfLocalX2ApicPropAcl,
       "cucsBiosVfLocalX2ApicSupportedByDefault": cucsBiosVfLocalX2ApicSupportedByDefault,
       "cucsBiosVfUCSMBootModeControlTable": cucsBiosVfUCSMBootModeControlTable,
       "cucsBiosVfUCSMBootModeControlEntry": cucsBiosVfUCSMBootModeControlEntry,
       "cucsBiosVfUCSMBootModeControlInstanceId": cucsBiosVfUCSMBootModeControlInstanceId,
       "cucsBiosVfUCSMBootModeControlDn": cucsBiosVfUCSMBootModeControlDn,
       "cucsBiosVfUCSMBootModeControlRn": cucsBiosVfUCSMBootModeControlRn,
       "cucsBiosVfUCSMBootModeControlVpUEFIBootMode": cucsBiosVfUCSMBootModeControlVpUEFIBootMode,
       "cucsBiosVfUCSMBootModeControlPropAcl": cucsBiosVfUCSMBootModeControlPropAcl,
       "cucsBiosVfUCSMBootModeControlSupportedByDefault": cucsBiosVfUCSMBootModeControlSupportedByDefault,
       "cucsBiosVfAllUSBDevicesTable": cucsBiosVfAllUSBDevicesTable,
       "cucsBiosVfAllUSBDevicesEntry": cucsBiosVfAllUSBDevicesEntry,
       "cucsBiosVfAllUSBDevicesInstanceId": cucsBiosVfAllUSBDevicesInstanceId,
       "cucsBiosVfAllUSBDevicesDn": cucsBiosVfAllUSBDevicesDn,
       "cucsBiosVfAllUSBDevicesRn": cucsBiosVfAllUSBDevicesRn,
       "cucsBiosVfAllUSBDevicesVpAllUSBDevices": cucsBiosVfAllUSBDevicesVpAllUSBDevices,
       "cucsBiosVfAllUSBDevicesPropAcl": cucsBiosVfAllUSBDevicesPropAcl,
       "cucsBiosVfAllUSBDevicesSupportedByDefault": cucsBiosVfAllUSBDevicesSupportedByDefault,
       "cucsBiosVfDRAMClockThrottlingTable": cucsBiosVfDRAMClockThrottlingTable,
       "cucsBiosVfDRAMClockThrottlingEntry": cucsBiosVfDRAMClockThrottlingEntry,
       "cucsBiosVfDRAMClockThrottlingInstanceId": cucsBiosVfDRAMClockThrottlingInstanceId,
       "cucsBiosVfDRAMClockThrottlingDn": cucsBiosVfDRAMClockThrottlingDn,
       "cucsBiosVfDRAMClockThrottlingRn": cucsBiosVfDRAMClockThrottlingRn,
       "cucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling": cucsBiosVfDRAMClockThrottlingVpDRAMClockThrottling,
       "cucsBiosVfDRAMClockThrottlingPropAcl": cucsBiosVfDRAMClockThrottlingPropAcl,
       "cucsBiosVfDRAMClockThrottlingSupportedByDefault": cucsBiosVfDRAMClockThrottlingSupportedByDefault,
       "cucsBiosVfFRB2TimerTable": cucsBiosVfFRB2TimerTable,
       "cucsBiosVfFRB2TimerEntry": cucsBiosVfFRB2TimerEntry,
       "cucsBiosVfFRB2TimerInstanceId": cucsBiosVfFRB2TimerInstanceId,
       "cucsBiosVfFRB2TimerDn": cucsBiosVfFRB2TimerDn,
       "cucsBiosVfFRB2TimerRn": cucsBiosVfFRB2TimerRn,
       "cucsBiosVfFRB2TimerVpFRB2Timer": cucsBiosVfFRB2TimerVpFRB2Timer,
       "cucsBiosVfFRB2TimerPropAcl": cucsBiosVfFRB2TimerPropAcl,
       "cucsBiosVfFRB2TimerSupportedByDefault": cucsBiosVfFRB2TimerSupportedByDefault,
       "cucsBiosVfFrequencyFloorOverrideTable": cucsBiosVfFrequencyFloorOverrideTable,
       "cucsBiosVfFrequencyFloorOverrideEntry": cucsBiosVfFrequencyFloorOverrideEntry,
       "cucsBiosVfFrequencyFloorOverrideInstanceId": cucsBiosVfFrequencyFloorOverrideInstanceId,
       "cucsBiosVfFrequencyFloorOverrideDn": cucsBiosVfFrequencyFloorOverrideDn,
       "cucsBiosVfFrequencyFloorOverrideRn": cucsBiosVfFrequencyFloorOverrideRn,
       "cucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride": cucsBiosVfFrequencyFloorOverrideVpFrequencyFloorOverride,
       "cucsBiosVfFrequencyFloorOverridePropAcl": cucsBiosVfFrequencyFloorOverridePropAcl,
       "cucsBiosVfFrequencyFloorOverrideSupportedByDefault": cucsBiosVfFrequencyFloorOverrideSupportedByDefault,
       "cucsBiosVfInterleaveConfigurationTable": cucsBiosVfInterleaveConfigurationTable,
       "cucsBiosVfInterleaveConfigurationEntry": cucsBiosVfInterleaveConfigurationEntry,
       "cucsBiosVfInterleaveConfigurationInstanceId": cucsBiosVfInterleaveConfigurationInstanceId,
       "cucsBiosVfInterleaveConfigurationDn": cucsBiosVfInterleaveConfigurationDn,
       "cucsBiosVfInterleaveConfigurationRn": cucsBiosVfInterleaveConfigurationRn,
       "cucsBiosVfInterleaveConfigurationVpChannelInterleaving": cucsBiosVfInterleaveConfigurationVpChannelInterleaving,
       "cucsBiosVfInterleaveConfigurationVpMemoryInterleaving": cucsBiosVfInterleaveConfigurationVpMemoryInterleaving,
       "cucsBiosVfInterleaveConfigurationVpRankInterleaving": cucsBiosVfInterleaveConfigurationVpRankInterleaving,
       "cucsBiosVfInterleaveConfigurationPropAcl": cucsBiosVfInterleaveConfigurationPropAcl,
       "cucsBiosVfInterleaveConfigurationSupportedByDefault": cucsBiosVfInterleaveConfigurationSupportedByDefault,
       "cucsBiosVfPCISlotLinkSpeedTable": cucsBiosVfPCISlotLinkSpeedTable,
       "cucsBiosVfPCISlotLinkSpeedEntry": cucsBiosVfPCISlotLinkSpeedEntry,
       "cucsBiosVfPCISlotLinkSpeedInstanceId": cucsBiosVfPCISlotLinkSpeedInstanceId,
       "cucsBiosVfPCISlotLinkSpeedDn": cucsBiosVfPCISlotLinkSpeedDn,
       "cucsBiosVfPCISlotLinkSpeedRn": cucsBiosVfPCISlotLinkSpeedRn,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot10LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot1LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot2LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot3LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot4LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot5LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot6LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot7LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot8LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed": cucsBiosVfPCISlotLinkSpeedVpPCIeSlot9LinkSpeed,
       "cucsBiosVfPCISlotLinkSpeedPropAcl": cucsBiosVfPCISlotLinkSpeedPropAcl,
       "cucsBiosVfPCISlotLinkSpeedSupportedByDefault": cucsBiosVfPCISlotLinkSpeedSupportedByDefault,
       "cucsBiosVfPSTATECoordinationTable": cucsBiosVfPSTATECoordinationTable,
       "cucsBiosVfPSTATECoordinationEntry": cucsBiosVfPSTATECoordinationEntry,
       "cucsBiosVfPSTATECoordinationInstanceId": cucsBiosVfPSTATECoordinationInstanceId,
       "cucsBiosVfPSTATECoordinationDn": cucsBiosVfPSTATECoordinationDn,
       "cucsBiosVfPSTATECoordinationRn": cucsBiosVfPSTATECoordinationRn,
       "cucsBiosVfPSTATECoordinationVpPSTATECoordination": cucsBiosVfPSTATECoordinationVpPSTATECoordination,
       "cucsBiosVfPSTATECoordinationPropAcl": cucsBiosVfPSTATECoordinationPropAcl,
       "cucsBiosVfPSTATECoordinationSupportedByDefault": cucsBiosVfPSTATECoordinationSupportedByDefault,
       "cucsBiosVfProcessorEnergyConfigurationTable": cucsBiosVfProcessorEnergyConfigurationTable,
       "cucsBiosVfProcessorEnergyConfigurationEntry": cucsBiosVfProcessorEnergyConfigurationEntry,
       "cucsBiosVfProcessorEnergyConfigurationInstanceId": cucsBiosVfProcessorEnergyConfigurationInstanceId,
       "cucsBiosVfProcessorEnergyConfigurationDn": cucsBiosVfProcessorEnergyConfigurationDn,
       "cucsBiosVfProcessorEnergyConfigurationRn": cucsBiosVfProcessorEnergyConfigurationRn,
       "cucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance": cucsBiosVfProcessorEnergyConfigurationVpEnergyPerformance,
       "cucsBiosVfProcessorEnergyConfigurationVpPowerTechnology": cucsBiosVfProcessorEnergyConfigurationVpPowerTechnology,
       "cucsBiosVfProcessorEnergyConfigurationPropAcl": cucsBiosVfProcessorEnergyConfigurationPropAcl,
       "cucsBiosVfProcessorEnergyConfigurationSupportedByDefault": cucsBiosVfProcessorEnergyConfigurationSupportedByDefault,
       "cucsBiosVfProcessorPrefetchConfigTable": cucsBiosVfProcessorPrefetchConfigTable,
       "cucsBiosVfProcessorPrefetchConfigEntry": cucsBiosVfProcessorPrefetchConfigEntry,
       "cucsBiosVfProcessorPrefetchConfigInstanceId": cucsBiosVfProcessorPrefetchConfigInstanceId,
       "cucsBiosVfProcessorPrefetchConfigDn": cucsBiosVfProcessorPrefetchConfigDn,
       "cucsBiosVfProcessorPrefetchConfigRn": cucsBiosVfProcessorPrefetchConfigRn,
       "cucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher": cucsBiosVfProcessorPrefetchConfigVpAdjacentCacheLinePrefetcher,
       "cucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher": cucsBiosVfProcessorPrefetchConfigVpDCUIPPrefetcher,
       "cucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch": cucsBiosVfProcessorPrefetchConfigVpDCUStreamerPrefetch,
       "cucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher": cucsBiosVfProcessorPrefetchConfigVpHardwarePrefetcher,
       "cucsBiosVfProcessorPrefetchConfigPropAcl": cucsBiosVfProcessorPrefetchConfigPropAcl,
       "cucsBiosVfProcessorPrefetchConfigSupportedByDefault": cucsBiosVfProcessorPrefetchConfigSupportedByDefault,
       "cucsBiosVfQPILinkFrequencySelectTable": cucsBiosVfQPILinkFrequencySelectTable,
       "cucsBiosVfQPILinkFrequencySelectEntry": cucsBiosVfQPILinkFrequencySelectEntry,
       "cucsBiosVfQPILinkFrequencySelectInstanceId": cucsBiosVfQPILinkFrequencySelectInstanceId,
       "cucsBiosVfQPILinkFrequencySelectDn": cucsBiosVfQPILinkFrequencySelectDn,
       "cucsBiosVfQPILinkFrequencySelectRn": cucsBiosVfQPILinkFrequencySelectRn,
       "cucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect": cucsBiosVfQPILinkFrequencySelectVpQPILinkFrequencySelect,
       "cucsBiosVfQPILinkFrequencySelectPropAcl": cucsBiosVfQPILinkFrequencySelectPropAcl,
       "cucsBiosVfQPILinkFrequencySelectSupportedByDefault": cucsBiosVfQPILinkFrequencySelectSupportedByDefault,
       "cucsBiosVfScrubPoliciesTable": cucsBiosVfScrubPoliciesTable,
       "cucsBiosVfScrubPoliciesEntry": cucsBiosVfScrubPoliciesEntry,
       "cucsBiosVfScrubPoliciesInstanceId": cucsBiosVfScrubPoliciesInstanceId,
       "cucsBiosVfScrubPoliciesDn": cucsBiosVfScrubPoliciesDn,
       "cucsBiosVfScrubPoliciesRn": cucsBiosVfScrubPoliciesRn,
       "cucsBiosVfScrubPoliciesVpDemandScrub": cucsBiosVfScrubPoliciesVpDemandScrub,
       "cucsBiosVfScrubPoliciesVpPatrolScrub": cucsBiosVfScrubPoliciesVpPatrolScrub,
       "cucsBiosVfScrubPoliciesPropAcl": cucsBiosVfScrubPoliciesPropAcl,
       "cucsBiosVfScrubPoliciesSupportedByDefault": cucsBiosVfScrubPoliciesSupportedByDefault,
       "cucsBiosVfUSBPortConfigurationTable": cucsBiosVfUSBPortConfigurationTable,
       "cucsBiosVfUSBPortConfigurationEntry": cucsBiosVfUSBPortConfigurationEntry,
       "cucsBiosVfUSBPortConfigurationInstanceId": cucsBiosVfUSBPortConfigurationInstanceId,
       "cucsBiosVfUSBPortConfigurationDn": cucsBiosVfUSBPortConfigurationDn,
       "cucsBiosVfUSBPortConfigurationRn": cucsBiosVfUSBPortConfigurationRn,
       "cucsBiosVfUSBPortConfigurationVpPort6064Emulation": cucsBiosVfUSBPortConfigurationVpPort6064Emulation,
       "cucsBiosVfUSBPortConfigurationVpUSBPortFront": cucsBiosVfUSBPortConfigurationVpUSBPortFront,
       "cucsBiosVfUSBPortConfigurationVpUSBPortInternal": cucsBiosVfUSBPortConfigurationVpUSBPortInternal,
       "cucsBiosVfUSBPortConfigurationVpUSBPortKVM": cucsBiosVfUSBPortConfigurationVpUSBPortKVM,
       "cucsBiosVfUSBPortConfigurationVpUSBPortRear": cucsBiosVfUSBPortConfigurationVpUSBPortRear,
       "cucsBiosVfUSBPortConfigurationVpUSBPortSDCard": cucsBiosVfUSBPortConfigurationVpUSBPortSDCard,
       "cucsBiosVfUSBPortConfigurationVpUSBPortVMedia": cucsBiosVfUSBPortConfigurationVpUSBPortVMedia,
       "cucsBiosVfUSBPortConfigurationPropAcl": cucsBiosVfUSBPortConfigurationPropAcl,
       "cucsBiosVfUSBPortConfigurationSupportedByDefault": cucsBiosVfUSBPortConfigurationSupportedByDefault,
       "cucsBiosVfVGAPriorityTable": cucsBiosVfVGAPriorityTable,
       "cucsBiosVfVGAPriorityEntry": cucsBiosVfVGAPriorityEntry,
       "cucsBiosVfVGAPriorityInstanceId": cucsBiosVfVGAPriorityInstanceId,
       "cucsBiosVfVGAPriorityDn": cucsBiosVfVGAPriorityDn,
       "cucsBiosVfVGAPriorityRn": cucsBiosVfVGAPriorityRn,
       "cucsBiosVfVGAPriorityVpVGAPriority": cucsBiosVfVGAPriorityVpVGAPriority,
       "cucsBiosVfVGAPriorityPropAcl": cucsBiosVfVGAPriorityPropAcl,
       "cucsBiosVfVGAPrioritySupportedByDefault": cucsBiosVfVGAPrioritySupportedByDefault,
       "cucsBiosVfAltitudeTable": cucsBiosVfAltitudeTable,
       "cucsBiosVfAltitudeEntry": cucsBiosVfAltitudeEntry,
       "cucsBiosVfAltitudeInstanceId": cucsBiosVfAltitudeInstanceId,
       "cucsBiosVfAltitudeDn": cucsBiosVfAltitudeDn,
       "cucsBiosVfAltitudeRn": cucsBiosVfAltitudeRn,
       "cucsBiosVfAltitudeVpAltitude": cucsBiosVfAltitudeVpAltitude,
       "cucsBiosVfAltitudePropAcl": cucsBiosVfAltitudePropAcl,
       "cucsBiosVfAltitudeSupportedByDefault": cucsBiosVfAltitudeSupportedByDefault,
       "cucsBiosVfTPMSupportTable": cucsBiosVfTPMSupportTable,
       "cucsBiosVfTPMSupportEntry": cucsBiosVfTPMSupportEntry,
       "cucsBiosVfTPMSupportInstanceId": cucsBiosVfTPMSupportInstanceId,
       "cucsBiosVfTPMSupportDn": cucsBiosVfTPMSupportDn,
       "cucsBiosVfTPMSupportRn": cucsBiosVfTPMSupportRn,
       "cucsBiosVfTPMSupportVpTPMSupport": cucsBiosVfTPMSupportVpTPMSupport,
       "cucsBiosVfTPMSupportPropAcl": cucsBiosVfTPMSupportPropAcl,
       "cucsBiosVfTPMSupportSupportedByDefault": cucsBiosVfTPMSupportSupportedByDefault,
       "cucsBiosVfUSBConfigurationTable": cucsBiosVfUSBConfigurationTable,
       "cucsBiosVfUSBConfigurationEntry": cucsBiosVfUSBConfigurationEntry,
       "cucsBiosVfUSBConfigurationInstanceId": cucsBiosVfUSBConfigurationInstanceId,
       "cucsBiosVfUSBConfigurationDn": cucsBiosVfUSBConfigurationDn,
       "cucsBiosVfUSBConfigurationRn": cucsBiosVfUSBConfigurationRn,
       "cucsBiosVfUSBConfigurationVpLegacyUSBSupport": cucsBiosVfUSBConfigurationVpLegacyUSBSupport,
       "cucsBiosVfUSBConfigurationVpXHCIMode": cucsBiosVfUSBConfigurationVpXHCIMode,
       "cucsBiosVfUSBConfigurationPropAcl": cucsBiosVfUSBConfigurationPropAcl,
       "cucsBiosVfUSBConfigurationSupportedByDefault": cucsBiosVfUSBConfigurationSupportedByDefault,
       "cucsBiosVfQPISnoopModeTable": cucsBiosVfQPISnoopModeTable,
       "cucsBiosVfQPISnoopModeEntry": cucsBiosVfQPISnoopModeEntry,
       "cucsBiosVfQPISnoopModeInstanceId": cucsBiosVfQPISnoopModeInstanceId,
       "cucsBiosVfQPISnoopModeDn": cucsBiosVfQPISnoopModeDn,
       "cucsBiosVfQPISnoopModeRn": cucsBiosVfQPISnoopModeRn,
       "cucsBiosVfQPISnoopModeVpQPISnoopMode": cucsBiosVfQPISnoopModeVpQPISnoopMode,
       "cucsBiosVfQPISnoopModePropAcl": cucsBiosVfQPISnoopModePropAcl,
       "cucsBiosVfQPISnoopModeSupportedByDefault": cucsBiosVfQPISnoopModeSupportedByDefault,
       "cucsBiosVfCPUPowerManagementTable": cucsBiosVfCPUPowerManagementTable,
       "cucsBiosVfCPUPowerManagementEntry": cucsBiosVfCPUPowerManagementEntry,
       "cucsBiosVfCPUPowerManagementInstanceId": cucsBiosVfCPUPowerManagementInstanceId,
       "cucsBiosVfCPUPowerManagementDn": cucsBiosVfCPUPowerManagementDn,
       "cucsBiosVfCPUPowerManagementRn": cucsBiosVfCPUPowerManagementRn,
       "cucsBiosVfCPUPowerManagementPropAcl": cucsBiosVfCPUPowerManagementPropAcl,
       "cucsBiosVfCPUPowerManagementSupportedByDefault": cucsBiosVfCPUPowerManagementSupportedByDefault,
       "cucsBiosVfCPUPowerManagementVpCPUPowerManagement": cucsBiosVfCPUPowerManagementVpCPUPowerManagement,
       "cucsBiosVfEnhancedPowerCappingSupportTable": cucsBiosVfEnhancedPowerCappingSupportTable,
       "cucsBiosVfEnhancedPowerCappingSupportEntry": cucsBiosVfEnhancedPowerCappingSupportEntry,
       "cucsBiosVfEnhancedPowerCappingSupportInstanceId": cucsBiosVfEnhancedPowerCappingSupportInstanceId,
       "cucsBiosVfEnhancedPowerCappingSupportDn": cucsBiosVfEnhancedPowerCappingSupportDn,
       "cucsBiosVfEnhancedPowerCappingSupportRn": cucsBiosVfEnhancedPowerCappingSupportRn,
       "cucsBiosVfEnhancedPowerCappingSupportPropAcl": cucsBiosVfEnhancedPowerCappingSupportPropAcl,
       "cucsBiosVfEnhancedPowerCappingSupportSupportedByDefault": cucsBiosVfEnhancedPowerCappingSupportSupportedByDefault,
       "cucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping": cucsBiosVfEnhancedPowerCappingSupportVpEnhancedPowerCapping,
       "cucsBiosVfPCHSATAModeTable": cucsBiosVfPCHSATAModeTable,
       "cucsBiosVfPCHSATAModeEntry": cucsBiosVfPCHSATAModeEntry,
       "cucsBiosVfPCHSATAModeInstanceId": cucsBiosVfPCHSATAModeInstanceId,
       "cucsBiosVfPCHSATAModeDn": cucsBiosVfPCHSATAModeDn,
       "cucsBiosVfPCHSATAModeRn": cucsBiosVfPCHSATAModeRn,
       "cucsBiosVfPCHSATAModePropAcl": cucsBiosVfPCHSATAModePropAcl,
       "cucsBiosVfPCHSATAModeSupportedByDefault": cucsBiosVfPCHSATAModeSupportedByDefault,
       "cucsBiosVfPCHSATAModeVpSATAMode": cucsBiosVfPCHSATAModeVpSATAMode,
       "cucsBiosVfASPMSupportTable": cucsBiosVfASPMSupportTable,
       "cucsBiosVfASPMSupportEntry": cucsBiosVfASPMSupportEntry,
       "cucsBiosVfASPMSupportInstanceId": cucsBiosVfASPMSupportInstanceId,
       "cucsBiosVfASPMSupportDn": cucsBiosVfASPMSupportDn,
       "cucsBiosVfASPMSupportRn": cucsBiosVfASPMSupportRn,
       "cucsBiosVfASPMSupportVpASPMSupport": cucsBiosVfASPMSupportVpASPMSupport,
       "cucsBiosVfASPMSupportSupportedByDefault": cucsBiosVfASPMSupportSupportedByDefault,
       "cucsBiosVfASPMSupportPropAcl": cucsBiosVfASPMSupportPropAcl,
       "cucsBiosVfDDR3VoltageSelectionTable": cucsBiosVfDDR3VoltageSelectionTable,
       "cucsBiosVfDDR3VoltageSelectionEntry": cucsBiosVfDDR3VoltageSelectionEntry,
       "cucsBiosVfDDR3VoltageSelectionInstanceId": cucsBiosVfDDR3VoltageSelectionInstanceId,
       "cucsBiosVfDDR3VoltageSelectionDn": cucsBiosVfDDR3VoltageSelectionDn,
       "cucsBiosVfDDR3VoltageSelectionRn": cucsBiosVfDDR3VoltageSelectionRn,
       "cucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection": cucsBiosVfDDR3VoltageSelectionVpDDR3VoltageSelection,
       "cucsBiosVfDDR3VoltageSelectionSupportedByDefault": cucsBiosVfDDR3VoltageSelectionSupportedByDefault,
       "cucsBiosVfDDR3VoltageSelectionPropAcl": cucsBiosVfDDR3VoltageSelectionPropAcl,
       "cucsBiosVfConsistentDeviceNameControlTable": cucsBiosVfConsistentDeviceNameControlTable,
       "cucsBiosVfConsistentDeviceNameControlEntry": cucsBiosVfConsistentDeviceNameControlEntry,
       "cucsBiosVfConsistentDeviceNameControlInstanceId": cucsBiosVfConsistentDeviceNameControlInstanceId,
       "cucsBiosVfConsistentDeviceNameControlDn": cucsBiosVfConsistentDeviceNameControlDn,
       "cucsBiosVfConsistentDeviceNameControlRn": cucsBiosVfConsistentDeviceNameControlRn,
       "cucsBiosVfConsistentDeviceNameControlVpCDNControl": cucsBiosVfConsistentDeviceNameControlVpCDNControl,
       "cucsBiosVfConsistentDeviceNameControlSupportedByDefault": cucsBiosVfConsistentDeviceNameControlSupportedByDefault,
       "cucsBiosVfConsistentDeviceNameControlPropAcl": cucsBiosVfConsistentDeviceNameControlPropAcl,
       "cucsBiosVfIntelTrustedExecutionTechnologyTable": cucsBiosVfIntelTrustedExecutionTechnologyTable,
       "cucsBiosVfIntelTrustedExecutionTechnologyEntry": cucsBiosVfIntelTrustedExecutionTechnologyEntry,
       "cucsBiosVfIntelTrustedExecutionTechnologyInstanceId": cucsBiosVfIntelTrustedExecutionTechnologyInstanceId,
       "cucsBiosVfIntelTrustedExecutionTechnologyDn": cucsBiosVfIntelTrustedExecutionTechnologyDn,
       "cucsBiosVfIntelTrustedExecutionTechnologyRn": cucsBiosVfIntelTrustedExecutionTechnologyRn,
       "cucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup": cucsBiosVfIntelTrustedExecutionTechnologyVpIntelTstdExecTechSup,
       "cucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault": cucsBiosVfIntelTrustedExecutionTechnologySupportedByDefault,
       "cucsBiosVfIntelTrustedExecutionTechnologyPropAcl": cucsBiosVfIntelTrustedExecutionTechnologyPropAcl,
       "cucsBiosVfPCILOMPortsConfigurationTable": cucsBiosVfPCILOMPortsConfigurationTable,
       "cucsBiosVfPCILOMPortsConfigurationEntry": cucsBiosVfPCILOMPortsConfigurationEntry,
       "cucsBiosVfPCILOMPortsConfigurationInstanceId": cucsBiosVfPCILOMPortsConfigurationInstanceId,
       "cucsBiosVfPCILOMPortsConfigurationDn": cucsBiosVfPCILOMPortsConfigurationDn,
       "cucsBiosVfPCILOMPortsConfigurationRn": cucsBiosVfPCILOMPortsConfigurationRn,
       "cucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link": cucsBiosVfPCILOMPortsConfigurationVpPCIe10GLOM2Link,
       "cucsBiosVfPCILOMPortsConfigurationSupportedByDefault": cucsBiosVfPCILOMPortsConfigurationSupportedByDefault,
       "cucsBiosVfPCILOMPortsConfigurationPropAcl": cucsBiosVfPCILOMPortsConfigurationPropAcl,
       "cucsBiosVfTPMPendingOperationTable": cucsBiosVfTPMPendingOperationTable,
       "cucsBiosVfTPMPendingOperationEntry": cucsBiosVfTPMPendingOperationEntry,
       "cucsBiosVfTPMPendingOperationInstanceId": cucsBiosVfTPMPendingOperationInstanceId,
       "cucsBiosVfTPMPendingOperationDn": cucsBiosVfTPMPendingOperationDn,
       "cucsBiosVfTPMPendingOperationRn": cucsBiosVfTPMPendingOperationRn,
       "cucsBiosVfTPMPendingOperationVpTPMPendingOperation": cucsBiosVfTPMPendingOperationVpTPMPendingOperation,
       "cucsBiosVfTPMPendingOperationSupportedByDefault": cucsBiosVfTPMPendingOperationSupportedByDefault,
       "cucsBiosVfTPMPendingOperationPropAcl": cucsBiosVfTPMPendingOperationPropAcl,
       "cucsBiosVfTrustedPlatformModuleTable": cucsBiosVfTrustedPlatformModuleTable,
       "cucsBiosVfTrustedPlatformModuleEntry": cucsBiosVfTrustedPlatformModuleEntry,
       "cucsBiosVfTrustedPlatformModuleInstanceId": cucsBiosVfTrustedPlatformModuleInstanceId,
       "cucsBiosVfTrustedPlatformModuleDn": cucsBiosVfTrustedPlatformModuleDn,
       "cucsBiosVfTrustedPlatformModuleRn": cucsBiosVfTrustedPlatformModuleRn,
       "cucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport": cucsBiosVfTrustedPlatformModuleVpTrustedPlatformModuleSupport,
       "cucsBiosVfTrustedPlatformModuleSupportedByDefault": cucsBiosVfTrustedPlatformModuleSupportedByDefault,
       "cucsBiosVfTrustedPlatformModulePropAcl": cucsBiosVfTrustedPlatformModulePropAcl,
       "cucsBiosVfCPUHardwarePowerManagementTable": cucsBiosVfCPUHardwarePowerManagementTable,
       "cucsBiosVfCPUHardwarePowerManagementEntry": cucsBiosVfCPUHardwarePowerManagementEntry,
       "cucsBiosVfCPUHardwarePowerManagementInstanceId": cucsBiosVfCPUHardwarePowerManagementInstanceId,
       "cucsBiosVfCPUHardwarePowerManagementDn": cucsBiosVfCPUHardwarePowerManagementDn,
       "cucsBiosVfCPUHardwarePowerManagementRn": cucsBiosVfCPUHardwarePowerManagementRn,
       "cucsBiosVfCPUHardwarePowerManagementSupportedByDefault": cucsBiosVfCPUHardwarePowerManagementSupportedByDefault,
       "cucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement": cucsBiosVfCPUHardwarePowerManagementVpCPUHardwarePowerManagement,
       "cucsBiosVfCPUHardwarePowerManagementPropAcl": cucsBiosVfCPUHardwarePowerManagementPropAcl,
       "cucsBiosVfIntegratedGraphicsTable": cucsBiosVfIntegratedGraphicsTable,
       "cucsBiosVfIntegratedGraphicsEntry": cucsBiosVfIntegratedGraphicsEntry,
       "cucsBiosVfIntegratedGraphicsInstanceId": cucsBiosVfIntegratedGraphicsInstanceId,
       "cucsBiosVfIntegratedGraphicsDn": cucsBiosVfIntegratedGraphicsDn,
       "cucsBiosVfIntegratedGraphicsRn": cucsBiosVfIntegratedGraphicsRn,
       "cucsBiosVfIntegratedGraphicsSupportedByDefault": cucsBiosVfIntegratedGraphicsSupportedByDefault,
       "cucsBiosVfIntegratedGraphicsVpIntegratedGraphics": cucsBiosVfIntegratedGraphicsVpIntegratedGraphics,
       "cucsBiosVfIntegratedGraphicsPropAcl": cucsBiosVfIntegratedGraphicsPropAcl,
       "cucsBiosVfIntegratedGraphicsApertureSizeTable": cucsBiosVfIntegratedGraphicsApertureSizeTable,
       "cucsBiosVfIntegratedGraphicsApertureSizeEntry": cucsBiosVfIntegratedGraphicsApertureSizeEntry,
       "cucsBiosVfIntegratedGraphicsApertureSizeInstanceId": cucsBiosVfIntegratedGraphicsApertureSizeInstanceId,
       "cucsBiosVfIntegratedGraphicsApertureSizeDn": cucsBiosVfIntegratedGraphicsApertureSizeDn,
       "cucsBiosVfIntegratedGraphicsApertureSizeRn": cucsBiosVfIntegratedGraphicsApertureSizeRn,
       "cucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault": cucsBiosVfIntegratedGraphicsApertureSizeSupportedByDefault,
       "cucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize": cucsBiosVfIntegratedGraphicsApertureSizeVpIntegratedGraphicsApertureSize,
       "cucsBiosVfIntegratedGraphicsApertureSizePropAcl": cucsBiosVfIntegratedGraphicsApertureSizePropAcl,
       "cucsBiosVfOnboardGraphicsTable": cucsBiosVfOnboardGraphicsTable,
       "cucsBiosVfOnboardGraphicsEntry": cucsBiosVfOnboardGraphicsEntry,
       "cucsBiosVfOnboardGraphicsInstanceId": cucsBiosVfOnboardGraphicsInstanceId,
       "cucsBiosVfOnboardGraphicsDn": cucsBiosVfOnboardGraphicsDn,
       "cucsBiosVfOnboardGraphicsRn": cucsBiosVfOnboardGraphicsRn,
       "cucsBiosVfOnboardGraphicsSupportedByDefault": cucsBiosVfOnboardGraphicsSupportedByDefault,
       "cucsBiosVfOnboardGraphicsVpOnboardGraphics": cucsBiosVfOnboardGraphicsVpOnboardGraphics,
       "cucsBiosVfOnboardGraphicsPropAcl": cucsBiosVfOnboardGraphicsPropAcl}
)
