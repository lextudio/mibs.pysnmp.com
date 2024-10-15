# SNMP MIB module (ADVA-FSPR7-CAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADVA-FSPR7-CAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:41 2024
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

(entityConnectionClassName,
 entityContainerClassName,
 entityContainerExtNo,
 entityContainerPortNo,
 entityContainerShelfNo,
 entityContainerSlotNo,
 entityCrossConnClassName,
 entityCrossConnFromClassName,
 entityCrossConnFromExtNo,
 entityCrossConnFromPortNo,
 entityCrossConnFromShelfNo,
 entityCrossConnFromSlotNo,
 entityCrossConnToClassName,
 entityCrossConnToExtNo,
 entityCrossConnToPortNo,
 entityCrossConnToShelfNo,
 entityCrossConnToSlotNo,
 entityCrossDcnClassName,
 entityCrossDcnExtNo,
 entityCrossDcnPortNo,
 entityCrossDcnShelfNo,
 entityCrossDcnSlotNo,
 entityCrsOptLineClassName,
 entityCrsOptLineFromClassName,
 entityCrsOptLineFromIndexNo1,
 entityCrsOptLineFromIndexNo2,
 entityCrsOptLineFromIndexNo3,
 entityCrsOptLineFromIndexNo4,
 entityCrsOptLineToClassName,
 entityCrsOptLineToIndexNo1,
 entityCrsOptLineToIndexNo2,
 entityCrsOptLineToIndexNo3,
 entityCrsOptLineToIndexNo4,
 entityDcnClassName,
 entityDcnExtNo,
 entityDcnPortNo,
 entityDcnShelfNo,
 entityDcnSlotNo,
 entityEqptClassName,
 entityEqptExtNo,
 entityEqptPortNo,
 entityEqptShelfNo,
 entityEqptSlotNo,
 entityExternalPortClassName,
 entityExternalPortExtNo,
 entityExternalPortPortNo,
 entityExternalPortShelfNo,
 entityExternalPortSlotNo,
 entityFacilityClassName,
 entityFacilityExtNo,
 entityFacilityPortNo,
 entityFacilityShelfNo,
 entityFacilitySlotNo,
 entityFfpClassName,
 entityFfpExtNo,
 entityFfpPortNo,
 entityFfpShelfNo,
 entityFfpSlotNo,
 entityFilterCableClassName,
 entityFilterCableIndex1,
 entityFilterCableIndex2,
 entityFilterCableIndex3,
 entityFilterCableIndex4,
 entityOptLineClassName,
 entityOptLineIndexNo1,
 entityOpticalMuxClassName,
 entityOpticalMuxExtNo,
 entityOpticalMuxPortNo,
 entityOpticalMuxShelfNo,
 entityOpticalMuxSlotNo,
 entityProtectionCableClassName,
 entityProtectionCableIndex1,
 entityProtectionCableIndex2,
 entityProtectionCableIndex3,
 entityProtectionCableIndex4,
 entityShelfConnClassName,
 entityShelfConnExtNo,
 entityShelfConnPortNo,
 entityShelfConnShelfNo,
 entityShelfConnSlotNo,
 entityTerminPointClassName,
 entityTerminPointIndexNo1,
 entityTerminPointIndexNo2,
 entityTerminPointIndexNo3,
 entityTerminPointIndexNo4) = mibBuilder.importSymbols(
    "ADVA-FSPR7-MIB",
    "entityConnectionClassName",
    "entityContainerClassName",
    "entityContainerExtNo",
    "entityContainerPortNo",
    "entityContainerShelfNo",
    "entityContainerSlotNo",
    "entityCrossConnClassName",
    "entityCrossConnFromClassName",
    "entityCrossConnFromExtNo",
    "entityCrossConnFromPortNo",
    "entityCrossConnFromShelfNo",
    "entityCrossConnFromSlotNo",
    "entityCrossConnToClassName",
    "entityCrossConnToExtNo",
    "entityCrossConnToPortNo",
    "entityCrossConnToShelfNo",
    "entityCrossConnToSlotNo",
    "entityCrossDcnClassName",
    "entityCrossDcnExtNo",
    "entityCrossDcnPortNo",
    "entityCrossDcnShelfNo",
    "entityCrossDcnSlotNo",
    "entityCrsOptLineClassName",
    "entityCrsOptLineFromClassName",
    "entityCrsOptLineFromIndexNo1",
    "entityCrsOptLineFromIndexNo2",
    "entityCrsOptLineFromIndexNo3",
    "entityCrsOptLineFromIndexNo4",
    "entityCrsOptLineToClassName",
    "entityCrsOptLineToIndexNo1",
    "entityCrsOptLineToIndexNo2",
    "entityCrsOptLineToIndexNo3",
    "entityCrsOptLineToIndexNo4",
    "entityDcnClassName",
    "entityDcnExtNo",
    "entityDcnPortNo",
    "entityDcnShelfNo",
    "entityDcnSlotNo",
    "entityEqptClassName",
    "entityEqptExtNo",
    "entityEqptPortNo",
    "entityEqptShelfNo",
    "entityEqptSlotNo",
    "entityExternalPortClassName",
    "entityExternalPortExtNo",
    "entityExternalPortPortNo",
    "entityExternalPortShelfNo",
    "entityExternalPortSlotNo",
    "entityFacilityClassName",
    "entityFacilityExtNo",
    "entityFacilityPortNo",
    "entityFacilityShelfNo",
    "entityFacilitySlotNo",
    "entityFfpClassName",
    "entityFfpExtNo",
    "entityFfpPortNo",
    "entityFfpShelfNo",
    "entityFfpSlotNo",
    "entityFilterCableClassName",
    "entityFilterCableIndex1",
    "entityFilterCableIndex2",
    "entityFilterCableIndex3",
    "entityFilterCableIndex4",
    "entityOptLineClassName",
    "entityOptLineIndexNo1",
    "entityOpticalMuxClassName",
    "entityOpticalMuxExtNo",
    "entityOpticalMuxPortNo",
    "entityOpticalMuxShelfNo",
    "entityOpticalMuxSlotNo",
    "entityProtectionCableClassName",
    "entityProtectionCableIndex1",
    "entityProtectionCableIndex2",
    "entityProtectionCableIndex3",
    "entityProtectionCableIndex4",
    "entityShelfConnClassName",
    "entityShelfConnExtNo",
    "entityShelfConnPortNo",
    "entityShelfConnShelfNo",
    "entityShelfConnSlotNo",
    "entityTerminPointClassName",
    "entityTerminPointIndexNo1",
    "entityTerminPointIndexNo2",
    "entityTerminPointIndexNo3",
    "entityTerminPointIndexNo4")

(ApsRevertModeCaps,
 ApsTypeCaps,
 Counter64StringCaps,
 FfpTypeCaps,
 FspR7APSCommandCaps,
 FspR7AdminStateCaps,
 FspR7AlsModeCaps,
 FspR7AseTabOprCaps,
 FspR7AutoThresResetCaps,
 FspR7BERThresholdCaps,
 FspR7BERThresholdSectionCaps,
 FspR7BaundCaps,
 FspR7BidirectionalChannelCaps,
 FspR7BitrateCaps,
 FspR7CapInventoryCaps,
 FspR7ChannelBandwidthCaps,
 FspR7ChannelIdentifierCaps,
 FspR7ChannelSpacingCaps,
 FspR7CodeGainCaps,
 FspR7ConnCaps,
 FspR7ConnectorTypeCaps,
 FspR7CpAuthTypeCaps,
 FspR7DCFiberTypeCaps,
 FspR7DeploymentScenarioCaps,
 FspR7DisableEnableCaps,
 FspR7DispersionCompensationCaps,
 FspR7DispersionConfigCaps,
 FspR7DispersionModesCaps,
 FspR7EdfaOutputPowerRatingCaps,
 FspR7EnableDisableCaps,
 FspR7EqlzAdminStateCaps,
 FspR7ErrorFwdModeCaps,
 FspR7FecTypeCaps,
 FspR7FiberBrandCaps,
 FspR7FiberDetectCaps,
 FspR7FlowControlModeCaps,
 FspR7FltrCableTypeCaps,
 FspR7ForceConfigCaps,
 FspR7ForcedStatusCaps,
 FspR7FrameFormatCaps,
 FspR7FunctionCrsCaps,
 FspR7GainCaps,
 FspR7GainRangeCaps,
 FspR7IPv6TypeCaps,
 FspR7InitEqualizationCaps,
 FspR7Integer32Caps,
 FspR7InterfaceTypeCaps,
 FspR7InvertTelemetryInputLogicCaps,
 FspR7IpModeCaps,
 FspR7IpTypeCaps,
 FspR7LacpModeCaps,
 FspR7LacpTimeoutCaps,
 FspR7LagPortTypeCaps,
 FspR7LaneGroupInventoryCaps,
 FspR7LaserDelayTimerCaps,
 FspR7LaserForcedOperationCaps,
 FspR7LineCodingCaps,
 FspR7LossAttenuationCaps,
 FspR7ManualAutoCaps,
 FspR7MappingCaps,
 FspR7MaxBitErrorRateCaps,
 FspR7MuxMethodCaps,
 FspR7NdpCleanupCaps,
 FspR7NoYesCaps,
 FspR7NumberOfChannelsCaps,
 FspR7NumberOfChannelsProvCaps,
 FspR7OptUpdateCaps,
 FspR7OpticalBandCaps,
 FspR7OpticalFiberTypeCaps,
 FspR7OpticalGroupCaps,
 FspR7OpticalInterfaceReachCaps,
 FspR7OpticalSubBandCaps,
 FspR7OpuPayloadTypeCaps,
 FspR7OscUsageCaps,
 FspR7OspfModeCaps,
 FspR7OtdrPeriodCaps,
 FspR7PRBSTestCaps,
 FspR7PathNodeCaps,
 FspR7PlugDataRateCaps,
 FspR7PmResetCaps,
 FspR7PortBehaviourCaps,
 FspR7PortModeCaps,
 FspR7PortRoleCaps,
 FspR7PrbsPmResetCaps,
 FspR7PsuOutputPowerCaps,
 FspR7RedLinedStateCaps,
 FspR7RlsManCaps,
 FspR7RoadmNumberCaps,
 FspR7RowStatusCaps,
 FspR7ScramblingCaps,
 FspR7SingleFiberLocationCaps,
 FspR7SnmpLongString,
 FspR7StuffCaps,
 FspR7SupplyTypeCaps,
 FspR7TelemetryOutputCaps,
 FspR7TifOutputResetCaps,
 FspR7TiltSetCaps,
 FspR7TopologyCaps,
 FspR7TrafficDirectionCaps,
 FspR7TransmissionModeCaps,
 FspR7TurnupConfigCaps,
 FspR7TxOffOnTmCaps,
 FspR7TypeConnectionCaps,
 FspR7TypeCrsCaps,
 FspR7Unsigned32Caps,
 FspR7UntaggedFramesCaps,
 FspR7VoaModeCaps,
 FspR7XfpDecisionThresCaps,
 FspR7YcableTypeCaps,
 FspR7YesNo,
 FspR7YesNoCaps) = mibBuilder.importSymbols(
    "ADVA-FSPR7-TC-MIB",
    "ApsRevertModeCaps",
    "ApsTypeCaps",
    "Counter64StringCaps",
    "FfpTypeCaps",
    "FspR7APSCommandCaps",
    "FspR7AdminStateCaps",
    "FspR7AlsModeCaps",
    "FspR7AseTabOprCaps",
    "FspR7AutoThresResetCaps",
    "FspR7BERThresholdCaps",
    "FspR7BERThresholdSectionCaps",
    "FspR7BaundCaps",
    "FspR7BidirectionalChannelCaps",
    "FspR7BitrateCaps",
    "FspR7CapInventoryCaps",
    "FspR7ChannelBandwidthCaps",
    "FspR7ChannelIdentifierCaps",
    "FspR7ChannelSpacingCaps",
    "FspR7CodeGainCaps",
    "FspR7ConnCaps",
    "FspR7ConnectorTypeCaps",
    "FspR7CpAuthTypeCaps",
    "FspR7DCFiberTypeCaps",
    "FspR7DeploymentScenarioCaps",
    "FspR7DisableEnableCaps",
    "FspR7DispersionCompensationCaps",
    "FspR7DispersionConfigCaps",
    "FspR7DispersionModesCaps",
    "FspR7EdfaOutputPowerRatingCaps",
    "FspR7EnableDisableCaps",
    "FspR7EqlzAdminStateCaps",
    "FspR7ErrorFwdModeCaps",
    "FspR7FecTypeCaps",
    "FspR7FiberBrandCaps",
    "FspR7FiberDetectCaps",
    "FspR7FlowControlModeCaps",
    "FspR7FltrCableTypeCaps",
    "FspR7ForceConfigCaps",
    "FspR7ForcedStatusCaps",
    "FspR7FrameFormatCaps",
    "FspR7FunctionCrsCaps",
    "FspR7GainCaps",
    "FspR7GainRangeCaps",
    "FspR7IPv6TypeCaps",
    "FspR7InitEqualizationCaps",
    "FspR7Integer32Caps",
    "FspR7InterfaceTypeCaps",
    "FspR7InvertTelemetryInputLogicCaps",
    "FspR7IpModeCaps",
    "FspR7IpTypeCaps",
    "FspR7LacpModeCaps",
    "FspR7LacpTimeoutCaps",
    "FspR7LagPortTypeCaps",
    "FspR7LaneGroupInventoryCaps",
    "FspR7LaserDelayTimerCaps",
    "FspR7LaserForcedOperationCaps",
    "FspR7LineCodingCaps",
    "FspR7LossAttenuationCaps",
    "FspR7ManualAutoCaps",
    "FspR7MappingCaps",
    "FspR7MaxBitErrorRateCaps",
    "FspR7MuxMethodCaps",
    "FspR7NdpCleanupCaps",
    "FspR7NoYesCaps",
    "FspR7NumberOfChannelsCaps",
    "FspR7NumberOfChannelsProvCaps",
    "FspR7OptUpdateCaps",
    "FspR7OpticalBandCaps",
    "FspR7OpticalFiberTypeCaps",
    "FspR7OpticalGroupCaps",
    "FspR7OpticalInterfaceReachCaps",
    "FspR7OpticalSubBandCaps",
    "FspR7OpuPayloadTypeCaps",
    "FspR7OscUsageCaps",
    "FspR7OspfModeCaps",
    "FspR7OtdrPeriodCaps",
    "FspR7PRBSTestCaps",
    "FspR7PathNodeCaps",
    "FspR7PlugDataRateCaps",
    "FspR7PmResetCaps",
    "FspR7PortBehaviourCaps",
    "FspR7PortModeCaps",
    "FspR7PortRoleCaps",
    "FspR7PrbsPmResetCaps",
    "FspR7PsuOutputPowerCaps",
    "FspR7RedLinedStateCaps",
    "FspR7RlsManCaps",
    "FspR7RoadmNumberCaps",
    "FspR7RowStatusCaps",
    "FspR7ScramblingCaps",
    "FspR7SingleFiberLocationCaps",
    "FspR7SnmpLongString",
    "FspR7StuffCaps",
    "FspR7SupplyTypeCaps",
    "FspR7TelemetryOutputCaps",
    "FspR7TifOutputResetCaps",
    "FspR7TiltSetCaps",
    "FspR7TopologyCaps",
    "FspR7TrafficDirectionCaps",
    "FspR7TransmissionModeCaps",
    "FspR7TurnupConfigCaps",
    "FspR7TxOffOnTmCaps",
    "FspR7TypeConnectionCaps",
    "FspR7TypeCrsCaps",
    "FspR7Unsigned32Caps",
    "FspR7UntaggedFramesCaps",
    "FspR7VoaModeCaps",
    "FspR7XfpDecisionThresCaps",
    "FspR7YcableTypeCaps",
    "FspR7YesNo",
    "FspR7YesNoCaps")

(ApsDirectionCaps,
 ApsHoldoffTimeCaps,
 EnableStateCaps,
 EthDuplexModeCaps,
 FspR7EquipmentTypeCaps,
 LoopConfigCaps,
 OhTerminationLevelCaps,
 OtnPayloadTypeCaps,
 OtnTcmLevelCaps,
 ProtectionMechCaps,
 SonetTimingSourceCaps,
 SonetTraceFormCaps,
 TimModeCaps,
 VirtualContainerTypeCaps,
 fspR7) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "ApsDirectionCaps",
    "ApsHoldoffTimeCaps",
    "EnableStateCaps",
    "EthDuplexModeCaps",
    "FspR7EquipmentTypeCaps",
    "LoopConfigCaps",
    "OhTerminationLevelCaps",
    "OtnPayloadTypeCaps",
    "OtnTcmLevelCaps",
    "ProtectionMechCaps",
    "SonetTimingSourceCaps",
    "SonetTraceFormCaps",
    "TimModeCaps",
    "VirtualContainerTypeCaps",
    "fspR7")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

advaFspR7Cap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9)
)
advaFspR7Cap.setRevisions(
        ("2014-10-15 00:00",
         "2014-09-29 00:00",
         "2013-12-04 00:00",
         "2013-08-20 00:00",
         "2011-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ManagementCap_ObjectIdentity = ObjectIdentity
managementCap = _ManagementCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3)
)
_SpecificMgmtCap_ObjectIdentity = ObjectIdentity
specificMgmtCap = _SpecificMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2)
)
_CrossConnectionCapTable_Object = MibTable
crossConnectionCapTable = _CrossConnectionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6)
)
if mibBuilder.loadTexts:
    crossConnectionCapTable.setStatus("current")
_CrossConnectionCapEntry_Object = MibTableRow
crossConnectionCapEntry = _CrossConnectionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1)
)
crossConnectionCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityCrossConnFromShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnFromSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnFromPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnFromExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnFromClassName"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnToShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnToSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnToPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnToExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnToClassName"),
    (0, "ADVA-FSPR7-MIB", "entityCrossConnClassName"),
)
if mibBuilder.loadTexts:
    crossConnectionCapEntry.setStatus("current")
_CrossConnectionCapRowStatus_Type = FspR7RowStatusCaps
_CrossConnectionCapRowStatus_Object = MibTableColumn
crossConnectionCapRowStatus = _CrossConnectionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 1),
    _CrossConnectionCapRowStatus_Type()
)
crossConnectionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapRowStatus.setStatus("current")
_CrossConnectionCapAdmin_Type = FspR7AdminStateCaps
_CrossConnectionCapAdmin_Object = MibTableColumn
crossConnectionCapAdmin = _CrossConnectionCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 2),
    _CrossConnectionCapAdmin_Type()
)
crossConnectionCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapAdmin.setStatus("current")
_CrossConnectionCapRedLineState_Type = FspR7RedLinedStateCaps
_CrossConnectionCapRedLineState_Object = MibTableColumn
crossConnectionCapRedLineState = _CrossConnectionCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 3),
    _CrossConnectionCapRedLineState_Type()
)
crossConnectionCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapRedLineState.setStatus("current")
_CrossConnectionCapConn_Type = FspR7ConnCaps
_CrossConnectionCapConn_Object = MibTableColumn
crossConnectionCapConn = _CrossConnectionCapConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 4),
    _CrossConnectionCapConn_Type()
)
crossConnectionCapConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapConn.setStatus("current")
_CrossConnectionCapAlias_Type = Integer32
_CrossConnectionCapAlias_Object = MibTableColumn
crossConnectionCapAlias = _CrossConnectionCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 5),
    _CrossConnectionCapAlias_Type()
)
crossConnectionCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapAlias.setStatus("current")
_CrossConnectionCapPathNode_Type = FspR7PathNodeCaps
_CrossConnectionCapPathNode_Object = MibTableColumn
crossConnectionCapPathNode = _CrossConnectionCapPathNode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 6),
    _CrossConnectionCapPathNode_Type()
)
crossConnectionCapPathNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapPathNode.setStatus("current")
_CrossConnectionCapTunnelAid_Type = Integer32
_CrossConnectionCapTunnelAid_Object = MibTableColumn
crossConnectionCapTunnelAid = _CrossConnectionCapTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 7),
    _CrossConnectionCapTunnelAid_Type()
)
crossConnectionCapTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapTunnelAid.setStatus("current")
_CrossConnectionCapType_Type = FspR7InterfaceTypeCaps
_CrossConnectionCapType_Object = MibTableColumn
crossConnectionCapType = _CrossConnectionCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 8),
    _CrossConnectionCapType_Type()
)
crossConnectionCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapType.setStatus("current")
_CrossConnectionCapCrsFunction_Type = FspR7FunctionCrsCaps
_CrossConnectionCapCrsFunction_Object = MibTableColumn
crossConnectionCapCrsFunction = _CrossConnectionCapCrsFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 9),
    _CrossConnectionCapCrsFunction_Type()
)
crossConnectionCapCrsFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsFunction.setStatus("current")
_CrossConnectionCapCrsFromAidTwo_Type = FspR7SnmpLongString
_CrossConnectionCapCrsFromAidTwo_Object = MibTableColumn
crossConnectionCapCrsFromAidTwo = _CrossConnectionCapCrsFromAidTwo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 10),
    _CrossConnectionCapCrsFromAidTwo_Type()
)
crossConnectionCapCrsFromAidTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsFromAidTwo.setStatus("current")
_CrossConnectionCapCrsToAidTwo_Type = FspR7SnmpLongString
_CrossConnectionCapCrsToAidTwo_Object = MibTableColumn
crossConnectionCapCrsToAidTwo = _CrossConnectionCapCrsToAidTwo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 11),
    _CrossConnectionCapCrsToAidTwo_Type()
)
crossConnectionCapCrsToAidTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsToAidTwo.setStatus("current")
_CrossConnectionCapCrsMcAidList_Type = FspR7SnmpLongString
_CrossConnectionCapCrsMcAidList_Object = MibTableColumn
crossConnectionCapCrsMcAidList = _CrossConnectionCapCrsMcAidList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 12),
    _CrossConnectionCapCrsMcAidList_Type()
)
crossConnectionCapCrsMcAidList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsMcAidList.setStatus("current")
_CrossConnectionCapCrsContAidList_Type = FspR7SnmpLongString
_CrossConnectionCapCrsContAidList_Object = MibTableColumn
crossConnectionCapCrsContAidList = _CrossConnectionCapCrsContAidList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 13),
    _CrossConnectionCapCrsContAidList_Type()
)
crossConnectionCapCrsContAidList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsContAidList.setStatus("current")
_CrossConnectionCapCrsContAidListTwo_Type = FspR7SnmpLongString
_CrossConnectionCapCrsContAidListTwo_Object = MibTableColumn
crossConnectionCapCrsContAidListTwo = _CrossConnectionCapCrsContAidListTwo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 6, 1, 14),
    _CrossConnectionCapCrsContAidListTwo_Type()
)
crossConnectionCapCrsContAidListTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionCapCrsContAidListTwo.setStatus("current")
_CrossOpticalLineCapTable_Object = MibTable
crossOpticalLineCapTable = _CrossOpticalLineCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7)
)
if mibBuilder.loadTexts:
    crossOpticalLineCapTable.setStatus("current")
_CrossOpticalLineCapEntry_Object = MibTableRow
crossOpticalLineCapEntry = _CrossOpticalLineCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1)
)
crossOpticalLineCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineFromIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineFromIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineFromIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineFromIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineFromClassName"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineToIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineToIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineToIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineToIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineToClassName"),
    (0, "ADVA-FSPR7-MIB", "entityCrsOptLineClassName"),
)
if mibBuilder.loadTexts:
    crossOpticalLineCapEntry.setStatus("current")
_CrossOpticalLineCapRowStatus_Type = FspR7RowStatusCaps
_CrossOpticalLineCapRowStatus_Object = MibTableColumn
crossOpticalLineCapRowStatus = _CrossOpticalLineCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 1),
    _CrossOpticalLineCapRowStatus_Type()
)
crossOpticalLineCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapRowStatus.setStatus("current")
_CrossOpticalLineCapRedLineState_Type = FspR7RedLinedStateCaps
_CrossOpticalLineCapRedLineState_Object = MibTableColumn
crossOpticalLineCapRedLineState = _CrossOpticalLineCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 2),
    _CrossOpticalLineCapRedLineState_Type()
)
crossOpticalLineCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapRedLineState.setStatus("current")
_CrossOpticalLineCapConn_Type = FspR7ConnCaps
_CrossOpticalLineCapConn_Object = MibTableColumn
crossOpticalLineCapConn = _CrossOpticalLineCapConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 3),
    _CrossOpticalLineCapConn_Type()
)
crossOpticalLineCapConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapConn.setStatus("current")
_CrossOpticalLineCapCrsType_Type = FspR7TypeCrsCaps
_CrossOpticalLineCapCrsType_Object = MibTableColumn
crossOpticalLineCapCrsType = _CrossOpticalLineCapCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 4),
    _CrossOpticalLineCapCrsType_Type()
)
crossOpticalLineCapCrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapCrsType.setStatus("current")
_CrossOpticalLineCapAlias_Type = Integer32
_CrossOpticalLineCapAlias_Object = MibTableColumn
crossOpticalLineCapAlias = _CrossOpticalLineCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 5),
    _CrossOpticalLineCapAlias_Type()
)
crossOpticalLineCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapAlias.setStatus("current")
_CrossOpticalLineCapTunnelAid_Type = Integer32
_CrossOpticalLineCapTunnelAid_Object = MibTableColumn
crossOpticalLineCapTunnelAid = _CrossOpticalLineCapTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 7, 1, 6),
    _CrossOpticalLineCapTunnelAid_Type()
)
crossOpticalLineCapTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineCapTunnelAid.setStatus("current")
_EndOfCrossOpticalLineCapTable_Type = Integer32
_EndOfCrossOpticalLineCapTable_Object = MibScalar
endOfCrossOpticalLineCapTable = _EndOfCrossOpticalLineCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 8),
    _EndOfCrossOpticalLineCapTable_Type()
)
endOfCrossOpticalLineCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfCrossOpticalLineCapTable.setStatus("current")
_CrossDcnCapTable_Object = MibTable
crossDcnCapTable = _CrossDcnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9)
)
if mibBuilder.loadTexts:
    crossDcnCapTable.setStatus("current")
_CrossDcnCapEntry_Object = MibTableRow
crossDcnCapEntry = _CrossDcnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9, 1)
)
crossDcnCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnClassName"),
)
if mibBuilder.loadTexts:
    crossDcnCapEntry.setStatus("current")
_CrossDcnCapRowStatus_Type = FspR7RowStatusCaps
_CrossDcnCapRowStatus_Object = MibTableColumn
crossDcnCapRowStatus = _CrossDcnCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9, 1, 1),
    _CrossDcnCapRowStatus_Type()
)
crossDcnCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnCapRowStatus.setStatus("current")
_CrossDcnCapType_Type = FspR7TypeConnectionCaps
_CrossDcnCapType_Object = MibTableColumn
crossDcnCapType = _CrossDcnCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9, 1, 2),
    _CrossDcnCapType_Type()
)
crossDcnCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnCapType.setStatus("current")
_CrossDcnCapLink_Type = SnmpAdminString
_CrossDcnCapLink_Object = MibTableColumn
crossDcnCapLink = _CrossDcnCapLink_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9, 1, 3),
    _CrossDcnCapLink_Type()
)
crossDcnCapLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnCapLink.setStatus("current")
_CrossDcnCapEcc_Type = SnmpAdminString
_CrossDcnCapEcc_Object = MibTableColumn
crossDcnCapEcc = _CrossDcnCapEcc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 9, 1, 4),
    _CrossDcnCapEcc_Type()
)
crossDcnCapEcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnCapEcc.setStatus("current")
_EndOfCrossDcnCapTable_Type = Integer32
_EndOfCrossDcnCapTable_Object = MibScalar
endOfCrossDcnCapTable = _EndOfCrossDcnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 10),
    _EndOfCrossDcnCapTable_Type()
)
endOfCrossDcnCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfCrossDcnCapTable.setStatus("current")
_EndOfSpecificMgmtCap_Type = Integer32
_EndOfSpecificMgmtCap_Object = MibScalar
endOfSpecificMgmtCap = _EndOfSpecificMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 2, 10000),
    _EndOfSpecificMgmtCap_Type()
)
endOfSpecificMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfSpecificMgmtCap.setStatus("current")
_EqptMgmtCap_ObjectIdentity = ObjectIdentity
eqptMgmtCap = _EqptMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3)
)
_ShelfCapTable_Object = MibTable
shelfCapTable = _ShelfCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1)
)
if mibBuilder.loadTexts:
    shelfCapTable.setStatus("current")
_ShelfCapEntry_Object = MibTableRow
shelfCapEntry = _ShelfCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1)
)
shelfCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    shelfCapEntry.setStatus("current")
_ShelfCapRowStatus_Type = FspR7RowStatusCaps
_ShelfCapRowStatus_Object = MibTableColumn
shelfCapRowStatus = _ShelfCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 1),
    _ShelfCapRowStatus_Type()
)
shelfCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapRowStatus.setStatus("current")
_ShelfCapPsuOutputPower_Type = FspR7PsuOutputPowerCaps
_ShelfCapPsuOutputPower_Object = MibTableColumn
shelfCapPsuOutputPower = _ShelfCapPsuOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 2),
    _ShelfCapPsuOutputPower_Type()
)
shelfCapPsuOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapPsuOutputPower.setStatus("current")
_ShelfCapType_Type = FspR7EquipmentTypeCaps
_ShelfCapType_Object = MibTableColumn
shelfCapType = _ShelfCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 3),
    _ShelfCapType_Type()
)
shelfCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapType.setStatus("current")
_ShelfCapRack_Type = Integer32
_ShelfCapRack_Object = MibTableColumn
shelfCapRack = _ShelfCapRack_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 4),
    _ShelfCapRack_Type()
)
shelfCapRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapRack.setStatus("current")
_ShelfCapSupply_Type = FspR7SupplyTypeCaps
_ShelfCapSupply_Object = MibTableColumn
shelfCapSupply = _ShelfCapSupply_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 5),
    _ShelfCapSupply_Type()
)
shelfCapSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapSupply.setStatus("current")
_ShelfCapBandProvision_Type = FspR7OpticalBandCaps
_ShelfCapBandProvision_Object = MibTableColumn
shelfCapBandProvision = _ShelfCapBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 6),
    _ShelfCapBandProvision_Type()
)
shelfCapBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapBandProvision.setStatus("current")
_ShelfCapAdmin_Type = FspR7AdminStateCaps
_ShelfCapAdmin_Object = MibTableColumn
shelfCapAdmin = _ShelfCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 7),
    _ShelfCapAdmin_Type()
)
shelfCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapAdmin.setStatus("current")
_ShelfCapRackNumber_Type = FspR7Unsigned32Caps
_ShelfCapRackNumber_Object = MibTableColumn
shelfCapRackNumber = _ShelfCapRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 8),
    _ShelfCapRackNumber_Type()
)
shelfCapRackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapRackNumber.setStatus("current")
_ShelfCapRackOrder_Type = FspR7Unsigned32Caps
_ShelfCapRackOrder_Object = MibTableColumn
shelfCapRackOrder = _ShelfCapRackOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 9),
    _ShelfCapRackOrder_Type()
)
shelfCapRackOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapRackOrder.setStatus("current")
_ShelfCapAlias_Type = Integer32
_ShelfCapAlias_Object = MibTableColumn
shelfCapAlias = _ShelfCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 10),
    _ShelfCapAlias_Type()
)
shelfCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapAlias.setStatus("current")
_ShelfCapSlot_Type = FspR7Unsigned32Caps
_ShelfCapSlot_Object = MibTableColumn
shelfCapSlot = _ShelfCapSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 1, 1, 11),
    _ShelfCapSlot_Type()
)
shelfCapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCapSlot.setStatus("current")
_EndOfShelfCapTable_Type = Integer32
_EndOfShelfCapTable_Object = MibScalar
endOfShelfCapTable = _EndOfShelfCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 2),
    _EndOfShelfCapTable_Type()
)
endOfShelfCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfCapTable.setStatus("current")
_FanCapTable_Object = MibTable
fanCapTable = _FanCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3)
)
if mibBuilder.loadTexts:
    fanCapTable.setStatus("current")
_FanCapEntry_Object = MibTableRow
fanCapEntry = _FanCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1)
)
fanCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    fanCapEntry.setStatus("current")
_FanCapRowStatus_Type = FspR7RowStatusCaps
_FanCapRowStatus_Object = MibTableColumn
fanCapRowStatus = _FanCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 1),
    _FanCapRowStatus_Type()
)
fanCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapRowStatus.setStatus("current")
_FanCapForceDestroy_Type = FspR7ForcedStatusCaps
_FanCapForceDestroy_Object = MibTableColumn
fanCapForceDestroy = _FanCapForceDestroy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 2),
    _FanCapForceDestroy_Type()
)
fanCapForceDestroy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapForceDestroy.setStatus("current")
_FanCapAdmin_Type = FspR7AdminStateCaps
_FanCapAdmin_Object = MibTableColumn
fanCapAdmin = _FanCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 3),
    _FanCapAdmin_Type()
)
fanCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapAdmin.setStatus("current")
_FanCapType_Type = FspR7EquipmentTypeCaps
_FanCapType_Object = MibTableColumn
fanCapType = _FanCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 4),
    _FanCapType_Type()
)
fanCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapType.setStatus("current")
_FanCapAlias_Type = Integer32
_FanCapAlias_Object = MibTableColumn
fanCapAlias = _FanCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 5),
    _FanCapAlias_Type()
)
fanCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapAlias.setStatus("current")
_FanCapOutputReset_Type = FspR7TifOutputResetCaps
_FanCapOutputReset_Object = MibTableColumn
fanCapOutputReset = _FanCapOutputReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 3, 1, 6),
    _FanCapOutputReset_Type()
)
fanCapOutputReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCapOutputReset.setStatus("current")
_EndOfFanCapTable_Type = Integer32
_EndOfFanCapTable_Object = MibScalar
endOfFanCapTable = _EndOfFanCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 4),
    _EndOfFanCapTable_Type()
)
endOfFanCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFanCapTable.setStatus("current")
_PlugCapTable_Object = MibTable
plugCapTable = _PlugCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5)
)
if mibBuilder.loadTexts:
    plugCapTable.setStatus("current")
_PlugCapEntry_Object = MibTableRow
plugCapEntry = _PlugCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1)
)
plugCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    plugCapEntry.setStatus("current")
_PlugCapRowStatus_Type = FspR7RowStatusCaps
_PlugCapRowStatus_Object = MibTableColumn
plugCapRowStatus = _PlugCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 1),
    _PlugCapRowStatus_Type()
)
plugCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapRowStatus.setStatus("current")
_PlugCapConnector_Type = FspR7ConnectorTypeCaps
_PlugCapConnector_Object = MibTableColumn
plugCapConnector = _PlugCapConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 2),
    _PlugCapConnector_Type()
)
plugCapConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapConnector.setStatus("current")
_PlugCapType_Type = FspR7EquipmentTypeCaps
_PlugCapType_Object = MibTableColumn
plugCapType = _PlugCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 3),
    _PlugCapType_Type()
)
plugCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapType.setStatus("current")
_PlugCapReach_Type = FspR7OpticalInterfaceReachCaps
_PlugCapReach_Object = MibTableColumn
plugCapReach = _PlugCapReach_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 4),
    _PlugCapReach_Type()
)
plugCapReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapReach.setStatus("current")
_PlugCapLoopbackAttenuation_Type = FspR7Unsigned32Caps
_PlugCapLoopbackAttenuation_Object = MibTableColumn
plugCapLoopbackAttenuation = _PlugCapLoopbackAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 5),
    _PlugCapLoopbackAttenuation_Type()
)
plugCapLoopbackAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapLoopbackAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    plugCapLoopbackAttenuation.setUnits("0.1 dB")
_PlugCapTransmitChannel_Type = FspR7ChannelIdentifierCaps
_PlugCapTransmitChannel_Object = MibTableColumn
plugCapTransmitChannel = _PlugCapTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 6),
    _PlugCapTransmitChannel_Type()
)
plugCapTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapTransmitChannel.setStatus("current")
_PlugCapAlias_Type = Integer32
_PlugCapAlias_Object = MibTableColumn
plugCapAlias = _PlugCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 7),
    _PlugCapAlias_Type()
)
plugCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapAlias.setStatus("current")
_PlugCapLaneGroup_Type = FspR7LaneGroupInventoryCaps
_PlugCapLaneGroup_Object = MibTableColumn
plugCapLaneGroup = _PlugCapLaneGroup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 8),
    _PlugCapLaneGroup_Type()
)
plugCapLaneGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapLaneGroup.setStatus("current")
_PlugCapMaxDataRate_Type = FspR7PlugDataRateCaps
_PlugCapMaxDataRate_Object = MibTableColumn
plugCapMaxDataRate = _PlugCapMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 9),
    _PlugCapMaxDataRate_Type()
)
plugCapMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapMaxDataRate.setStatus("current")
_PlugCapThirdPartyUsage_Type = EnableStateCaps
_PlugCapThirdPartyUsage_Object = MibTableColumn
plugCapThirdPartyUsage = _PlugCapThirdPartyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 10),
    _PlugCapThirdPartyUsage_Type()
)
plugCapThirdPartyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapThirdPartyUsage.setStatus("current")
_PlugCapAdmin_Type = FspR7AdminStateCaps
_PlugCapAdmin_Object = MibTableColumn
plugCapAdmin = _PlugCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 11),
    _PlugCapAdmin_Type()
)
plugCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapAdmin.setStatus("current")
_PlugCapBidirectionalChannel_Type = FspR7BidirectionalChannelCaps
_PlugCapBidirectionalChannel_Object = MibTableColumn
plugCapBidirectionalChannel = _PlugCapBidirectionalChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 12),
    _PlugCapBidirectionalChannel_Type()
)
plugCapBidirectionalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapBidirectionalChannel.setStatus("current")
_PlugCapChannelSpacingProvision_Type = FspR7ChannelSpacingCaps
_PlugCapChannelSpacingProvision_Object = MibTableColumn
plugCapChannelSpacingProvision = _PlugCapChannelSpacingProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 5, 1, 13),
    _PlugCapChannelSpacingProvision_Type()
)
plugCapChannelSpacingProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugCapChannelSpacingProvision.setStatus("current")
_EndOfPlugCapTable_Type = Integer32
_EndOfPlugCapTable_Object = MibScalar
endOfPlugCapTable = _EndOfPlugCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 6),
    _EndOfPlugCapTable_Type()
)
endOfPlugCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPlugCapTable.setStatus("current")
_ModuleCapTable_Object = MibTable
moduleCapTable = _ModuleCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7)
)
if mibBuilder.loadTexts:
    moduleCapTable.setStatus("current")
_ModuleCapEntry_Object = MibTableRow
moduleCapEntry = _ModuleCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1)
)
moduleCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    moduleCapEntry.setStatus("current")
_ModuleCapRowStatus_Type = FspR7RowStatusCaps
_ModuleCapRowStatus_Object = MibTableColumn
moduleCapRowStatus = _ModuleCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 1),
    _ModuleCapRowStatus_Type()
)
moduleCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapRowStatus.setStatus("current")
_ModuleCapForceDestroy_Type = FspR7ForcedStatusCaps
_ModuleCapForceDestroy_Object = MibTableColumn
moduleCapForceDestroy = _ModuleCapForceDestroy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 2),
    _ModuleCapForceDestroy_Type()
)
moduleCapForceDestroy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapForceDestroy.setStatus("current")
_ModuleCapPsuOutputPower_Type = FspR7PsuOutputPowerCaps
_ModuleCapPsuOutputPower_Object = MibTableColumn
moduleCapPsuOutputPower = _ModuleCapPsuOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 3),
    _ModuleCapPsuOutputPower_Type()
)
moduleCapPsuOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapPsuOutputPower.setStatus("current")
_ModuleCapPower_Type = FspR7EdfaOutputPowerRatingCaps
_ModuleCapPower_Object = MibTableColumn
moduleCapPower = _ModuleCapPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 4),
    _ModuleCapPower_Type()
)
moduleCapPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapPower.setStatus("current")
_ModuleCapReach_Type = FspR7OpticalInterfaceReachCaps
_ModuleCapReach_Object = MibTableColumn
moduleCapReach = _ModuleCapReach_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 5),
    _ModuleCapReach_Type()
)
moduleCapReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapReach.setStatus("current")
_ModuleCapInitEqlz_Type = FspR7InitEqualizationCaps
_ModuleCapInitEqlz_Object = MibTableColumn
moduleCapInitEqlz = _ModuleCapInitEqlz_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 6),
    _ModuleCapInitEqlz_Type()
)
moduleCapInitEqlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapInitEqlz.setStatus("current")
_ModuleCapLanAid_Type = SnmpAdminString
_ModuleCapLanAid_Object = MibTableColumn
moduleCapLanAid = _ModuleCapLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 7),
    _ModuleCapLanAid_Type()
)
moduleCapLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapLanAid.setStatus("current")
_ModuleCapType_Type = FspR7EquipmentTypeCaps
_ModuleCapType_Object = MibTableColumn
moduleCapType = _ModuleCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 8),
    _ModuleCapType_Type()
)
moduleCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapType.setStatus("current")
_ModuleCapMapping_Type = FspR7MappingCaps
_ModuleCapMapping_Object = MibTableColumn
moduleCapMapping = _ModuleCapMapping_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 9),
    _ModuleCapMapping_Type()
)
moduleCapMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapMapping.setStatus("current")
_ModuleCapGainRange_Type = FspR7GainRangeCaps
_ModuleCapGainRange_Object = MibTableColumn
moduleCapGainRange = _ModuleCapGainRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 10),
    _ModuleCapGainRange_Type()
)
moduleCapGainRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapGainRange.setStatus("current")
_ModuleCapSfProvision_Type = FspR7SingleFiberLocationCaps
_ModuleCapSfProvision_Object = MibTableColumn
moduleCapSfProvision = _ModuleCapSfProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 11),
    _ModuleCapSfProvision_Type()
)
moduleCapSfProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapSfProvision.setStatus("current")
_ModuleCapCapabilityLevelProvision_Type = FspR7CapInventoryCaps
_ModuleCapCapabilityLevelProvision_Object = MibTableColumn
moduleCapCapabilityLevelProvision = _ModuleCapCapabilityLevelProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 12),
    _ModuleCapCapabilityLevelProvision_Type()
)
moduleCapCapabilityLevelProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapCapabilityLevelProvision.setStatus("current")
_ModuleCapDCFiberType_Type = FspR7DCFiberTypeCaps
_ModuleCapDCFiberType_Object = MibTableColumn
moduleCapDCFiberType = _ModuleCapDCFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 13),
    _ModuleCapDCFiberType_Type()
)
moduleCapDCFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapDCFiberType.setStatus("current")
_ModuleCapChannelsProvision_Type = FspR7NumberOfChannelsProvCaps
_ModuleCapChannelsProvision_Object = MibTableColumn
moduleCapChannelsProvision = _ModuleCapChannelsProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 14),
    _ModuleCapChannelsProvision_Type()
)
moduleCapChannelsProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapChannelsProvision.setStatus("current")
_ModuleCapFiberDetect_Type = FspR7FiberDetectCaps
_ModuleCapFiberDetect_Object = MibTableColumn
moduleCapFiberDetect = _ModuleCapFiberDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 15),
    _ModuleCapFiberDetect_Type()
)
moduleCapFiberDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapFiberDetect.setStatus("current")
_ModuleCapSupply_Type = FspR7SupplyTypeCaps
_ModuleCapSupply_Object = MibTableColumn
moduleCapSupply = _ModuleCapSupply_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 16),
    _ModuleCapSupply_Type()
)
moduleCapSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapSupply.setStatus("current")
_ModuleCapGroup_Type = FspR7OpticalGroupCaps
_ModuleCapGroup_Object = MibTableColumn
moduleCapGroup = _ModuleCapGroup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 17),
    _ModuleCapGroup_Type()
)
moduleCapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapGroup.setStatus("current")
_ModuleCapDeploy_Type = FspR7DeploymentScenarioCaps
_ModuleCapDeploy_Object = MibTableColumn
moduleCapDeploy = _ModuleCapDeploy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 18),
    _ModuleCapDeploy_Type()
)
moduleCapDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapDeploy.setStatus("current")
_ModuleCapLagSysPrio_Type = FspR7Unsigned32Caps
_ModuleCapLagSysPrio_Object = MibTableColumn
moduleCapLagSysPrio = _ModuleCapLagSysPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 19),
    _ModuleCapLagSysPrio_Type()
)
moduleCapLagSysPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapLagSysPrio.setStatus("current")
_ModuleCapTransmitChannel_Type = FspR7ChannelIdentifierCaps
_ModuleCapTransmitChannel_Object = MibTableColumn
moduleCapTransmitChannel = _ModuleCapTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 20),
    _ModuleCapTransmitChannel_Type()
)
moduleCapTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapTransmitChannel.setStatus("current")
_ModuleCapBand_Type = FspR7OpticalBandCaps
_ModuleCapBand_Object = MibTableColumn
moduleCapBand = _ModuleCapBand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 21),
    _ModuleCapBand_Type()
)
moduleCapBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapBand.setStatus("current")
_ModuleCapTrafficDirection_Type = FspR7TrafficDirectionCaps
_ModuleCapTrafficDirection_Object = MibTableColumn
moduleCapTrafficDirection = _ModuleCapTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 22),
    _ModuleCapTrafficDirection_Type()
)
moduleCapTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapTrafficDirection.setStatus("current")
_ModuleCapIpAddr_Type = FspR7YesNo
_ModuleCapIpAddr_Object = MibTableColumn
moduleCapIpAddr = _ModuleCapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 23),
    _ModuleCapIpAddr_Type()
)
moduleCapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapIpAddr.setStatus("current")
_ModuleCapDispersionCompensation_Type = FspR7DispersionCompensationCaps
_ModuleCapDispersionCompensation_Object = MibTableColumn
moduleCapDispersionCompensation = _ModuleCapDispersionCompensation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 24),
    _ModuleCapDispersionCompensation_Type()
)
moduleCapDispersionCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapDispersionCompensation.setStatus("current")
_ModuleCapActivateDetect_Type = FspR7YesNoCaps
_ModuleCapActivateDetect_Object = MibTableColumn
moduleCapActivateDetect = _ModuleCapActivateDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 25),
    _ModuleCapActivateDetect_Type()
)
moduleCapActivateDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapActivateDetect.setStatus("current")
_ModuleCapOscUsage_Type = FspR7OscUsageCaps
_ModuleCapOscUsage_Object = MibTableColumn
moduleCapOscUsage = _ModuleCapOscUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 26),
    _ModuleCapOscUsage_Type()
)
moduleCapOscUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapOscUsage.setStatus("current")
_ModuleCapAdmin_Type = FspR7AdminStateCaps
_ModuleCapAdmin_Object = MibTableColumn
moduleCapAdmin = _ModuleCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 27),
    _ModuleCapAdmin_Type()
)
moduleCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapAdmin.setStatus("current")
_ModuleCapScrambling_Type = FspR7ScramblingCaps
_ModuleCapScrambling_Object = MibTableColumn
moduleCapScrambling = _ModuleCapScrambling_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 28),
    _ModuleCapScrambling_Type()
)
moduleCapScrambling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapScrambling.setStatus("current")
_ModuleCapChannelsNumber_Type = FspR7NumberOfChannelsCaps
_ModuleCapChannelsNumber_Object = MibTableColumn
moduleCapChannelsNumber = _ModuleCapChannelsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 29),
    _ModuleCapChannelsNumber_Type()
)
moduleCapChannelsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapChannelsNumber.setStatus("current")
_ModuleCapChannelSpacingProvision_Type = FspR7ChannelSpacingCaps
_ModuleCapChannelSpacingProvision_Object = MibTableColumn
moduleCapChannelSpacingProvision = _ModuleCapChannelSpacingProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 30),
    _ModuleCapChannelSpacingProvision_Type()
)
moduleCapChannelSpacingProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapChannelSpacingProvision.setStatus("current")
_ModuleCapMode_Type = FspR7TransmissionModeCaps
_ModuleCapMode_Object = MibTableColumn
moduleCapMode = _ModuleCapMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 31),
    _ModuleCapMode_Type()
)
moduleCapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapMode.setStatus("current")
_ModuleCapSubBandProvision_Type = FspR7OpticalSubBandCaps
_ModuleCapSubBandProvision_Object = MibTableColumn
moduleCapSubBandProvision = _ModuleCapSubBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 32),
    _ModuleCapSubBandProvision_Type()
)
moduleCapSubBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapSubBandProvision.setStatus("current")
_ModuleCapAlias_Type = Integer32
_ModuleCapAlias_Object = MibTableColumn
moduleCapAlias = _ModuleCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 33),
    _ModuleCapAlias_Type()
)
moduleCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapAlias.setStatus("current")
_ModuleCapFiberType_Type = FspR7OpticalFiberTypeCaps
_ModuleCapFiberType_Object = MibTableColumn
moduleCapFiberType = _ModuleCapFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 34),
    _ModuleCapFiberType_Type()
)
moduleCapFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapFiberType.setStatus("current")
_ModuleCapChannelSpacing_Type = FspR7ChannelSpacingCaps
_ModuleCapChannelSpacing_Object = MibTableColumn
moduleCapChannelSpacing = _ModuleCapChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 35),
    _ModuleCapChannelSpacing_Type()
)
moduleCapChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapChannelSpacing.setStatus("current")
_ModuleCapOutputReset_Type = FspR7TifOutputResetCaps
_ModuleCapOutputReset_Object = MibTableColumn
moduleCapOutputReset = _ModuleCapOutputReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 36),
    _ModuleCapOutputReset_Type()
)
moduleCapOutputReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapOutputReset.setStatus("current")
_ModuleCapRoadmNumber_Type = FspR7RoadmNumberCaps
_ModuleCapRoadmNumber_Object = MibTableColumn
moduleCapRoadmNumber = _ModuleCapRoadmNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 37),
    _ModuleCapRoadmNumber_Type()
)
moduleCapRoadmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapRoadmNumber.setStatus("current")
_ModuleCapTopology_Type = FspR7TopologyCaps
_ModuleCapTopology_Object = MibTableColumn
moduleCapTopology = _ModuleCapTopology_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 38),
    _ModuleCapTopology_Type()
)
moduleCapTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapTopology.setStatus("current")
_ModuleCapForceConfig_Type = FspR7ForceConfigCaps
_ModuleCapForceConfig_Object = MibTableColumn
moduleCapForceConfig = _ModuleCapForceConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 39),
    _ModuleCapForceConfig_Type()
)
moduleCapForceConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapForceConfig.setStatus("current")
_ModuleCapMuxMethod_Type = FspR7MuxMethodCaps
_ModuleCapMuxMethod_Object = MibTableColumn
moduleCapMuxMethod = _ModuleCapMuxMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 40),
    _ModuleCapMuxMethod_Type()
)
moduleCapMuxMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapMuxMethod.setStatus("current")
_ModuleCapNdpCleanup_Type = FspR7NdpCleanupCaps
_ModuleCapNdpCleanup_Object = MibTableColumn
moduleCapNdpCleanup = _ModuleCapNdpCleanup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 41),
    _ModuleCapNdpCleanup_Type()
)
moduleCapNdpCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapNdpCleanup.setStatus("current")
_ModuleCapRstp_Type = FspR7EnableDisableCaps
_ModuleCapRstp_Object = MibTableColumn
moduleCapRstp = _ModuleCapRstp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 42),
    _ModuleCapRstp_Type()
)
moduleCapRstp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapRstp.setStatus("current")
_ModuleCapRemoteReset_Type = FspR7RlsManCaps
_ModuleCapRemoteReset_Object = MibTableColumn
moduleCapRemoteReset = _ModuleCapRemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 7, 1, 43),
    _ModuleCapRemoteReset_Type()
)
moduleCapRemoteReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCapRemoteReset.setStatus("current")
_EndOfModuleCap_Type = Integer32
_EndOfModuleCap_Object = MibScalar
endOfModuleCap = _EndOfModuleCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 8),
    _EndOfModuleCap_Type()
)
endOfModuleCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfModuleCap.setStatus("current")
_ProtectionCableCapTable_Object = MibTable
protectionCableCapTable = _ProtectionCableCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 9)
)
if mibBuilder.loadTexts:
    protectionCableCapTable.setStatus("current")
_ProtectionCableCapEntry_Object = MibTableRow
protectionCableCapEntry = _ProtectionCableCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 9, 1)
)
protectionCableCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityProtectionCableIndex1"),
    (0, "ADVA-FSPR7-MIB", "entityProtectionCableIndex2"),
    (0, "ADVA-FSPR7-MIB", "entityProtectionCableIndex3"),
    (0, "ADVA-FSPR7-MIB", "entityProtectionCableIndex4"),
    (0, "ADVA-FSPR7-MIB", "entityProtectionCableClassName"),
)
if mibBuilder.loadTexts:
    protectionCableCapEntry.setStatus("current")
_ProtectionCableCapRowStatus_Type = FspR7RowStatusCaps
_ProtectionCableCapRowStatus_Object = MibTableColumn
protectionCableCapRowStatus = _ProtectionCableCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 9, 1, 1),
    _ProtectionCableCapRowStatus_Type()
)
protectionCableCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionCableCapRowStatus.setStatus("current")
_ProtectionCableCapType_Type = FspR7YcableTypeCaps
_ProtectionCableCapType_Object = MibTableColumn
protectionCableCapType = _ProtectionCableCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 9, 1, 2),
    _ProtectionCableCapType_Type()
)
protectionCableCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionCableCapType.setStatus("current")
_EndOfProtectionCableCap_Type = Integer32
_EndOfProtectionCableCap_Object = MibScalar
endOfProtectionCableCap = _EndOfProtectionCableCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 10),
    _EndOfProtectionCableCap_Type()
)
endOfProtectionCableCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfProtectionCableCap.setStatus("current")
_FilterCableCapTable_Object = MibTable
filterCableCapTable = _FilterCableCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 11)
)
if mibBuilder.loadTexts:
    filterCableCapTable.setStatus("current")
_FilterCableCapEntry_Object = MibTableRow
filterCableCapEntry = _FilterCableCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 11, 1)
)
filterCableCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFilterCableIndex1"),
    (0, "ADVA-FSPR7-MIB", "entityFilterCableIndex2"),
    (0, "ADVA-FSPR7-MIB", "entityFilterCableIndex3"),
    (0, "ADVA-FSPR7-MIB", "entityFilterCableIndex4"),
    (0, "ADVA-FSPR7-MIB", "entityFilterCableClassName"),
)
if mibBuilder.loadTexts:
    filterCableCapEntry.setStatus("current")
_FilterCableCapRowStatus_Type = FspR7RowStatusCaps
_FilterCableCapRowStatus_Object = MibTableColumn
filterCableCapRowStatus = _FilterCableCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 11, 1, 1),
    _FilterCableCapRowStatus_Type()
)
filterCableCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCableCapRowStatus.setStatus("current")
_FilterCableCapType_Type = FspR7FltrCableTypeCaps
_FilterCableCapType_Object = MibTableColumn
filterCableCapType = _FilterCableCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 11, 1, 2),
    _FilterCableCapType_Type()
)
filterCableCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCableCapType.setStatus("current")
_EndOfFilterCableCap_Type = Integer32
_EndOfFilterCableCap_Object = MibScalar
endOfFilterCableCap = _EndOfFilterCableCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 12),
    _EndOfFilterCableCap_Type()
)
endOfFilterCableCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFilterCableCap.setStatus("current")
_EndOfEqptMgmCap_Type = Integer32
_EndOfEqptMgmCap_Object = MibScalar
endOfEqptMgmCap = _EndOfEqptMgmCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 3, 10000),
    _EndOfEqptMgmCap_Type()
)
endOfEqptMgmCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEqptMgmCap.setStatus("current")
_FacilityMgmtCap_ObjectIdentity = ObjectIdentity
facilityMgmtCap = _FacilityMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4)
)
_PhysicalPortCapTable_Object = MibTable
physicalPortCapTable = _PhysicalPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1)
)
if mibBuilder.loadTexts:
    physicalPortCapTable.setStatus("current")
_PhysicalPortCapEntry_Object = MibTableRow
physicalPortCapEntry = _PhysicalPortCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1)
)
physicalPortCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    physicalPortCapEntry.setStatus("current")
_PhysicalPortCapRowStatus_Type = FspR7RowStatusCaps
_PhysicalPortCapRowStatus_Object = MibTableColumn
physicalPortCapRowStatus = _PhysicalPortCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 1),
    _PhysicalPortCapRowStatus_Type()
)
physicalPortCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapRowStatus.setStatus("current")
_PhysicalPortCapType_Type = FspR7InterfaceTypeCaps
_PhysicalPortCapType_Object = MibTableColumn
physicalPortCapType = _PhysicalPortCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 2),
    _PhysicalPortCapType_Type()
)
physicalPortCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapType.setStatus("current")
_PhysicalPortCapAdmin_Type = FspR7AdminStateCaps
_PhysicalPortCapAdmin_Object = MibTableColumn
physicalPortCapAdmin = _PhysicalPortCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 3),
    _PhysicalPortCapAdmin_Type()
)
physicalPortCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAdmin.setStatus("current")
_PhysicalPortCapAlias_Type = Integer32
_PhysicalPortCapAlias_Object = MibTableColumn
physicalPortCapAlias = _PhysicalPortCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 4),
    _PhysicalPortCapAlias_Type()
)
physicalPortCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAlias.setStatus("current")
_PhysicalPortCapAlsMode_Type = FspR7AlsModeCaps
_PhysicalPortCapAlsMode_Object = MibTableColumn
physicalPortCapAlsMode = _PhysicalPortCapAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 5),
    _PhysicalPortCapAlsMode_Type()
)
physicalPortCapAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAlsMode.setStatus("current")
_PhysicalPortCapAutoThresReset_Type = FspR7AutoThresResetCaps
_PhysicalPortCapAutoThresReset_Object = MibTableColumn
physicalPortCapAutoThresReset = _PhysicalPortCapAutoThresReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 6),
    _PhysicalPortCapAutoThresReset_Type()
)
physicalPortCapAutoThresReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAutoThresReset.setStatus("current")
_PhysicalPortCapAutonegotiation_Type = EnableStateCaps
_PhysicalPortCapAutonegotiation_Object = MibTableColumn
physicalPortCapAutonegotiation = _PhysicalPortCapAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 7),
    _PhysicalPortCapAutonegotiation_Type()
)
physicalPortCapAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAutonegotiation.setStatus("current")
_PhysicalPortCapBehaviour_Type = FspR7PortBehaviourCaps
_PhysicalPortCapBehaviour_Object = MibTableColumn
physicalPortCapBehaviour = _PhysicalPortCapBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 8),
    _PhysicalPortCapBehaviour_Type()
)
physicalPortCapBehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapBehaviour.setStatus("current")
_PhysicalPortCapDispertionConfig_Type = FspR7DispersionConfigCaps
_PhysicalPortCapDispertionConfig_Object = MibTableColumn
physicalPortCapDispertionConfig = _PhysicalPortCapDispertionConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 9),
    _PhysicalPortCapDispertionConfig_Type()
)
physicalPortCapDispertionConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapDispertionConfig.setStatus("current")
_PhysicalPortCapDispersionSetting_Type = FspR7Integer32Caps
_PhysicalPortCapDispersionSetting_Object = MibTableColumn
physicalPortCapDispersionSetting = _PhysicalPortCapDispersionSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 10),
    _PhysicalPortCapDispersionSetting_Type()
)
physicalPortCapDispersionSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapDispersionSetting.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapDispersionSetting.setUnits("ps/nm")
_PhysicalPortCapDispersionMode_Type = FspR7DispersionModesCaps
_PhysicalPortCapDispersionMode_Object = MibTableColumn
physicalPortCapDispersionMode = _PhysicalPortCapDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 11),
    _PhysicalPortCapDispersionMode_Type()
)
physicalPortCapDispersionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapDispersionMode.setStatus("current")
_PhysicalPortCapChannelProv_Type = FspR7ChannelIdentifierCaps
_PhysicalPortCapChannelProv_Object = MibTableColumn
physicalPortCapChannelProv = _PhysicalPortCapChannelProv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 12),
    _PhysicalPortCapChannelProv_Type()
)
physicalPortCapChannelProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapChannelProv.setStatus("current")
_PhysicalPortCapWdmRxChannel_Type = FspR7ChannelIdentifierCaps
_PhysicalPortCapWdmRxChannel_Object = MibTableColumn
physicalPortCapWdmRxChannel = _PhysicalPortCapWdmRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 13),
    _PhysicalPortCapWdmRxChannel_Type()
)
physicalPortCapWdmRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapWdmRxChannel.setStatus("current")
_PhysicalPortCapCodeGain_Type = FspR7CodeGainCaps
_PhysicalPortCapCodeGain_Object = MibTableColumn
physicalPortCapCodeGain = _PhysicalPortCapCodeGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 14),
    _PhysicalPortCapCodeGain_Type()
)
physicalPortCapCodeGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapCodeGain.setStatus("current")
_PhysicalPortCapXfpDecisionThres_Type = FspR7XfpDecisionThresCaps
_PhysicalPortCapXfpDecisionThres_Object = MibTableColumn
physicalPortCapXfpDecisionThres = _PhysicalPortCapXfpDecisionThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 15),
    _PhysicalPortCapXfpDecisionThres_Type()
)
physicalPortCapXfpDecisionThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapXfpDecisionThres.setStatus("current")
_PhysicalPortCapDisparityCorrection_Type = EnableStateCaps
_PhysicalPortCapDisparityCorrection_Object = MibTableColumn
physicalPortCapDisparityCorrection = _PhysicalPortCapDisparityCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 16),
    _PhysicalPortCapDisparityCorrection_Type()
)
physicalPortCapDisparityCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapDisparityCorrection.setStatus("current")
_PhysicalPortCapEqlzAdmin_Type = FspR7EqlzAdminStateCaps
_PhysicalPortCapEqlzAdmin_Object = MibTableColumn
physicalPortCapEqlzAdmin = _PhysicalPortCapEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 17),
    _PhysicalPortCapEqlzAdmin_Type()
)
physicalPortCapEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapEqlzAdmin.setStatus("current")
_PhysicalPortCapErrorForwarding_Type = FspR7ErrorFwdModeCaps
_PhysicalPortCapErrorForwarding_Object = MibTableColumn
physicalPortCapErrorForwarding = _PhysicalPortCapErrorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 18),
    _PhysicalPortCapErrorForwarding_Type()
)
physicalPortCapErrorForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapErrorForwarding.setStatus("current")
_PhysicalPortCapFecType_Type = FspR7FecTypeCaps
_PhysicalPortCapFecType_Object = MibTableColumn
physicalPortCapFecType = _PhysicalPortCapFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 19),
    _PhysicalPortCapFecType_Type()
)
physicalPortCapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapFecType.setStatus("current")
_PhysicalPortCapFarEndCommunication_Type = FspR7YesNoCaps
_PhysicalPortCapFarEndCommunication_Object = MibTableColumn
physicalPortCapFarEndCommunication = _PhysicalPortCapFarEndCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 20),
    _PhysicalPortCapFarEndCommunication_Type()
)
physicalPortCapFarEndCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapFarEndCommunication.setStatus("current")
_PhysicalPortCapFlowControl_Type = FspR7FlowControlModeCaps
_PhysicalPortCapFlowControl_Object = MibTableColumn
physicalPortCapFlowControl = _PhysicalPortCapFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 21),
    _PhysicalPortCapFlowControl_Type()
)
physicalPortCapFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapFlowControl.setStatus("current")
_PhysicalPortCapForceLaserOn_Type = FspR7LaserForcedOperationCaps
_PhysicalPortCapForceLaserOn_Object = MibTableColumn
physicalPortCapForceLaserOn = _PhysicalPortCapForceLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 22),
    _PhysicalPortCapForceLaserOn_Type()
)
physicalPortCapForceLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapForceLaserOn.setStatus("current")
_PhysicalPortCapInhibitSwitchToProt_Type = FspR7YesNoCaps
_PhysicalPortCapInhibitSwitchToProt_Object = MibTableColumn
physicalPortCapInhibitSwitchToProt = _PhysicalPortCapInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 23),
    _PhysicalPortCapInhibitSwitchToProt_Type()
)
physicalPortCapInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapInhibitSwitchToProt.setStatus("current")
_PhysicalPortCapInhibitSwitchToWork_Type = FspR7YesNoCaps
_PhysicalPortCapInhibitSwitchToWork_Object = MibTableColumn
physicalPortCapInhibitSwitchToWork = _PhysicalPortCapInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 24),
    _PhysicalPortCapInhibitSwitchToWork_Type()
)
physicalPortCapInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapInhibitSwitchToWork.setStatus("current")
_PhysicalPortCapLaneChannelSetting_Type = FspR7ChannelIdentifierCaps
_PhysicalPortCapLaneChannelSetting_Object = MibTableColumn
physicalPortCapLaneChannelSetting = _PhysicalPortCapLaneChannelSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 25),
    _PhysicalPortCapLaneChannelSetting_Type()
)
physicalPortCapLaneChannelSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLaneChannelSetting.setStatus("current")
_PhysicalPortCapLoopConfig_Type = LoopConfigCaps
_PhysicalPortCapLoopConfig_Object = MibTableColumn
physicalPortCapLoopConfig = _PhysicalPortCapLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 26),
    _PhysicalPortCapLoopConfig_Type()
)
physicalPortCapLoopConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLoopConfig.setStatus("current")
_PhysicalPortCapLaserDelayTimer_Type = FspR7LaserDelayTimerCaps
_PhysicalPortCapLaserDelayTimer_Object = MibTableColumn
physicalPortCapLaserDelayTimer = _PhysicalPortCapLaserDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 27),
    _PhysicalPortCapLaserDelayTimer_Type()
)
physicalPortCapLaserDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLaserDelayTimer.setStatus("current")
_PhysicalPortCapLaserOffTimer_Type = FspR7Unsigned32Caps
_PhysicalPortCapLaserOffTimer_Object = MibTableColumn
physicalPortCapLaserOffTimer = _PhysicalPortCapLaserOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 28),
    _PhysicalPortCapLaserOffTimer_Type()
)
physicalPortCapLaserOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLaserOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapLaserOffTimer.setUnits("ms")
_PhysicalPortCapLaserOnTimer_Type = FspR7Unsigned32Caps
_PhysicalPortCapLaserOnTimer_Object = MibTableColumn
physicalPortCapLaserOnTimer = _PhysicalPortCapLaserOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 29),
    _PhysicalPortCapLaserOnTimer_Type()
)
physicalPortCapLaserOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLaserOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapLaserOnTimer.setUnits("ms")
_PhysicalPortCapLaserOffDelayFunction_Type = EnableStateCaps
_PhysicalPortCapLaserOffDelayFunction_Object = MibTableColumn
physicalPortCapLaserOffDelayFunction = _PhysicalPortCapLaserOffDelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 30),
    _PhysicalPortCapLaserOffDelayFunction_Type()
)
physicalPortCapLaserOffDelayFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLaserOffDelayFunction.setStatus("current")
_PhysicalPortCapAutoPTassignment_Type = FspR7ManualAutoCaps
_PhysicalPortCapAutoPTassignment_Object = MibTableColumn
physicalPortCapAutoPTassignment = _PhysicalPortCapAutoPTassignment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 31),
    _PhysicalPortCapAutoPTassignment_Type()
)
physicalPortCapAutoPTassignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapAutoPTassignment.setStatus("current")
_PhysicalPortCapTributarySlotMethod_Type = FspR7ManualAutoCaps
_PhysicalPortCapTributarySlotMethod_Object = MibTableColumn
physicalPortCapTributarySlotMethod = _PhysicalPortCapTributarySlotMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 32),
    _PhysicalPortCapTributarySlotMethod_Type()
)
physicalPortCapTributarySlotMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTributarySlotMethod.setStatus("current")
_PhysicalPortCapInitiateEqualization_Type = FspR7InitEqualizationCaps
_PhysicalPortCapInitiateEqualization_Object = MibTableColumn
physicalPortCapInitiateEqualization = _PhysicalPortCapInitiateEqualization_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 33),
    _PhysicalPortCapInitiateEqualization_Type()
)
physicalPortCapInitiateEqualization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapInitiateEqualization.setStatus("current")
_PhysicalPortCapLossAttenuation_Type = FspR7LossAttenuationCaps
_PhysicalPortCapLossAttenuation_Object = MibTableColumn
physicalPortCapLossAttenuation = _PhysicalPortCapLossAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 34),
    _PhysicalPortCapLossAttenuation_Type()
)
physicalPortCapLossAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLossAttenuation.setStatus("current")
_PhysicalPortCapOpticalSetPoint_Type = FspR7Integer32Caps
_PhysicalPortCapOpticalSetPoint_Object = MibTableColumn
physicalPortCapOpticalSetPoint = _PhysicalPortCapOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 35),
    _PhysicalPortCapOpticalSetPoint_Type()
)
physicalPortCapOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapOpticalSetPoint.setUnits("0.1 dBm")
_PhysicalPortCapDataLayerPmReset_Type = FspR7PmResetCaps
_PhysicalPortCapDataLayerPmReset_Object = MibTableColumn
physicalPortCapDataLayerPmReset = _PhysicalPortCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 36),
    _PhysicalPortCapDataLayerPmReset_Type()
)
physicalPortCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapDataLayerPmReset.setStatus("current")
_PhysicalPortCapPrbsPmReset_Type = FspR7PrbsPmResetCaps
_PhysicalPortCapPrbsPmReset_Object = MibTableColumn
physicalPortCapPrbsPmReset = _PhysicalPortCapPrbsPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 37),
    _PhysicalPortCapPrbsPmReset_Type()
)
physicalPortCapPrbsPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPrbsPmReset.setStatus("current")
_PhysicalPortCapTestPrbsRcvMode_Type = FspR7PRBSTestCaps
_PhysicalPortCapTestPrbsRcvMode_Object = MibTableColumn
physicalPortCapTestPrbsRcvMode = _PhysicalPortCapTestPrbsRcvMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 38),
    _PhysicalPortCapTestPrbsRcvMode_Type()
)
physicalPortCapTestPrbsRcvMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTestPrbsRcvMode.setStatus("current")
_PhysicalPortCapTestPrbsTrmtMode_Type = FspR7PRBSTestCaps
_PhysicalPortCapTestPrbsTrmtMode_Object = MibTableColumn
physicalPortCapTestPrbsTrmtMode = _PhysicalPortCapTestPrbsTrmtMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 39),
    _PhysicalPortCapTestPrbsTrmtMode_Type()
)
physicalPortCapTestPrbsTrmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTestPrbsTrmtMode.setStatus("current")
_PhysicalPortCapSwitchCommand_Type = FspR7APSCommandCaps
_PhysicalPortCapSwitchCommand_Object = MibTableColumn
physicalPortCapSwitchCommand = _PhysicalPortCapSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 40),
    _PhysicalPortCapSwitchCommand_Type()
)
physicalPortCapSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSwitchCommand.setStatus("current")
_PhysicalPortCapOpuPayloadType_Type = FspR7OpuPayloadTypeCaps
_PhysicalPortCapOpuPayloadType_Object = MibTableColumn
physicalPortCapOpuPayloadType = _PhysicalPortCapOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 41),
    _PhysicalPortCapOpuPayloadType_Type()
)
physicalPortCapOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapOpuPayloadType.setStatus("current")
_PhysicalPortCapSigDegThresSonetLine_Type = FspR7BERThresholdCaps
_PhysicalPortCapSigDegThresSonetLine_Object = MibTableColumn
physicalPortCapSigDegThresSonetLine = _PhysicalPortCapSigDegThresSonetLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 42),
    _PhysicalPortCapSigDegThresSonetLine_Type()
)
physicalPortCapSigDegThresSonetLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSonetLine.setStatus("current")
_PhysicalPortCapSigDegThresSdhMs_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegThresSdhMs_Object = MibTableColumn
physicalPortCapSigDegThresSdhMs = _PhysicalPortCapSigDegThresSdhMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 43),
    _PhysicalPortCapSigDegThresSdhMs_Type()
)
physicalPortCapSigDegThresSdhMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSdhMs.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSdhMs.setUnits("%")
_PhysicalPortCapSigDegThresOtu_Type = FspR7Integer32Caps
_PhysicalPortCapSigDegThresOtu_Object = MibTableColumn
physicalPortCapSigDegThresOtu = _PhysicalPortCapSigDegThresOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 44),
    _PhysicalPortCapSigDegThresOtu_Type()
)
physicalPortCapSigDegThresOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOtu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOtu.setUnits("%")
_PhysicalPortCapSigDegThresOdu_Type = FspR7Integer32Caps
_PhysicalPortCapSigDegThresOdu_Object = MibTableColumn
physicalPortCapSigDegThresOdu = _PhysicalPortCapSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 45),
    _PhysicalPortCapSigDegThresOdu_Type()
)
physicalPortCapSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOdu.setUnits("%")
_PhysicalPortCapSigDegThreshold_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegThreshold_Object = MibTableColumn
physicalPortCapSigDegThreshold = _PhysicalPortCapSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 46),
    _PhysicalPortCapSigDegThreshold_Type()
)
physicalPortCapSigDegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThreshold.setStatus("current")
_PhysicalPortCapSigDegPcslThreshold_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPcslThreshold_Object = MibTableColumn
physicalPortCapSigDegPcslThreshold = _PhysicalPortCapSigDegPcslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 47),
    _PhysicalPortCapSigDegPcslThreshold_Type()
)
physicalPortCapSigDegPcslThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPcslThreshold.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPcslThreshold.setUnits("%")
_PhysicalPortCapSigDegThresSonetSection_Type = FspR7BERThresholdSectionCaps
_PhysicalPortCapSigDegThresSonetSection_Object = MibTableColumn
physicalPortCapSigDegThresSonetSection = _PhysicalPortCapSigDegThresSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 48),
    _PhysicalPortCapSigDegThresSonetSection_Type()
)
physicalPortCapSigDegThresSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSonetSection.setStatus("current")
_PhysicalPortCapSigDegThresSdhSection_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegThresSdhSection_Object = MibTableColumn
physicalPortCapSigDegThresSdhSection = _PhysicalPortCapSigDegThresSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 49),
    _PhysicalPortCapSigDegThresSdhSection_Type()
)
physicalPortCapSigDegThresSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresSdhSection.setUnits("%")
_PhysicalPortCapSigDegThresOduTcmA_Type = FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmA_Object = MibTableColumn
physicalPortCapSigDegThresOduTcmA = _PhysicalPortCapSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 50),
    _PhysicalPortCapSigDegThresOduTcmA_Type()
)
physicalPortCapSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmA.setUnits("%")
_PhysicalPortCapSigDegThresOduTcmB_Type = FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmB_Object = MibTableColumn
physicalPortCapSigDegThresOduTcmB = _PhysicalPortCapSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 51),
    _PhysicalPortCapSigDegThresOduTcmB_Type()
)
physicalPortCapSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmB.setUnits("%")
_PhysicalPortCapSigDegThresOduTcmC_Type = FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmC_Object = MibTableColumn
physicalPortCapSigDegThresOduTcmC = _PhysicalPortCapSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 52),
    _PhysicalPortCapSigDegThresOduTcmC_Type()
)
physicalPortCapSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegThresOduTcmC.setUnits("%")
_PhysicalPortCapSignalDegradePeriod_Type = FspR7Unsigned32Caps
_PhysicalPortCapSignalDegradePeriod_Object = MibTableColumn
physicalPortCapSignalDegradePeriod = _PhysicalPortCapSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 53),
    _PhysicalPortCapSignalDegradePeriod_Type()
)
physicalPortCapSignalDegradePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSignalDegradePeriod.setUnits("s")
_PhysicalPortCapSigDegPeriodOdu_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOdu_Object = MibTableColumn
physicalPortCapSigDegPeriodOdu = _PhysicalPortCapSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 54),
    _PhysicalPortCapSigDegPeriodOdu_Type()
)
physicalPortCapSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOdu.setUnits("s")
_PhysicalPortCapSigDegPeriodOtu_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOtu_Object = MibTableColumn
physicalPortCapSigDegPeriodOtu = _PhysicalPortCapSigDegPeriodOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 55),
    _PhysicalPortCapSigDegPeriodOtu_Type()
)
physicalPortCapSigDegPeriodOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOtu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOtu.setUnits("s")
_PhysicalPortCapSigDegPeriodIntegration_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodIntegration_Object = MibTableColumn
physicalPortCapSigDegPeriodIntegration = _PhysicalPortCapSigDegPeriodIntegration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 56),
    _PhysicalPortCapSigDegPeriodIntegration_Type()
)
physicalPortCapSigDegPeriodIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodIntegration.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodIntegration.setUnits("s")
_PhysicalPortCapSigDegPeriodSdhSection_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodSdhSection_Object = MibTableColumn
physicalPortCapSigDegPeriodSdhSection = _PhysicalPortCapSigDegPeriodSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 57),
    _PhysicalPortCapSigDegPeriodSdhSection_Type()
)
physicalPortCapSigDegPeriodSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodSdhSection.setUnits("s")
_PhysicalPortCapSigDegPeriodOduTcmA_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmA_Object = MibTableColumn
physicalPortCapSigDegPeriodOduTcmA = _PhysicalPortCapSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 58),
    _PhysicalPortCapSigDegPeriodOduTcmA_Type()
)
physicalPortCapSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmA.setUnits("s")
_PhysicalPortCapSigDegPeriodOduTcmB_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmB_Object = MibTableColumn
physicalPortCapSigDegPeriodOduTcmB = _PhysicalPortCapSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 59),
    _PhysicalPortCapSigDegPeriodOduTcmB_Type()
)
physicalPortCapSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmB.setUnits("s")
_PhysicalPortCapSigDegPeriodOduTcmC_Type = FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmC_Object = MibTableColumn
physicalPortCapSigDegPeriodOduTcmC = _PhysicalPortCapSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 60),
    _PhysicalPortCapSigDegPeriodOduTcmC_Type()
)
physicalPortCapSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapSigDegPeriodOduTcmC.setUnits("s")
_PhysicalPortCapOtnStuffing_Type = FspR7StuffCaps
_PhysicalPortCapOtnStuffing_Object = MibTableColumn
physicalPortCapOtnStuffing = _PhysicalPortCapOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 61),
    _PhysicalPortCapOtnStuffing_Type()
)
physicalPortCapOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapOtnStuffing.setStatus("current")
_PhysicalPortCapTcmALevel_Type = OtnTcmLevelCaps
_PhysicalPortCapTcmALevel_Object = MibTableColumn
physicalPortCapTcmALevel = _PhysicalPortCapTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 62),
    _PhysicalPortCapTcmALevel_Type()
)
physicalPortCapTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTcmALevel.setStatus("current")
_PhysicalPortCapTcmBLevel_Type = OtnTcmLevelCaps
_PhysicalPortCapTcmBLevel_Object = MibTableColumn
physicalPortCapTcmBLevel = _PhysicalPortCapTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 63),
    _PhysicalPortCapTcmBLevel_Type()
)
physicalPortCapTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTcmBLevel.setStatus("current")
_PhysicalPortCapTcmCLevel_Type = OtnTcmLevelCaps
_PhysicalPortCapTcmCLevel_Object = MibTableColumn
physicalPortCapTcmCLevel = _PhysicalPortCapTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 64),
    _PhysicalPortCapTcmCLevel_Type()
)
physicalPortCapTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTcmCLevel.setStatus("current")
_PhysicalPortCapTerminationLevel_Type = OhTerminationLevelCaps
_PhysicalPortCapTerminationLevel_Object = MibTableColumn
physicalPortCapTerminationLevel = _PhysicalPortCapTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 65),
    _PhysicalPortCapTerminationLevel_Type()
)
physicalPortCapTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTerminationLevel.setStatus("current")
_PhysicalPortCapTimingSource_Type = SonetTimingSourceCaps
_PhysicalPortCapTimingSource_Object = MibTableColumn
physicalPortCapTimingSource = _PhysicalPortCapTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 66),
    _PhysicalPortCapTimingSource_Type()
)
physicalPortCapTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimingSource.setStatus("current")
_PhysicalPortCapTimModeOdu_Type = TimModeCaps
_PhysicalPortCapTimModeOdu_Object = MibTableColumn
physicalPortCapTimModeOdu = _PhysicalPortCapTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 67),
    _PhysicalPortCapTimModeOdu_Type()
)
physicalPortCapTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeOdu.setStatus("current")
_PhysicalPortCapTimModeOtu_Type = TimModeCaps
_PhysicalPortCapTimModeOtu_Object = MibTableColumn
physicalPortCapTimModeOtu = _PhysicalPortCapTimModeOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 68),
    _PhysicalPortCapTimModeOtu_Type()
)
physicalPortCapTimModeOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeOtu.setStatus("current")
_PhysicalPortCapTimModeSonetSection_Type = TimModeCaps
_PhysicalPortCapTimModeSonetSection_Object = MibTableColumn
physicalPortCapTimModeSonetSection = _PhysicalPortCapTimModeSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 69),
    _PhysicalPortCapTimModeSonetSection_Type()
)
physicalPortCapTimModeSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeSonetSection.setStatus("current")
_PhysicalPortCapTimModeOduTcmA_Type = TimModeCaps
_PhysicalPortCapTimModeOduTcmA_Object = MibTableColumn
physicalPortCapTimModeOduTcmA = _PhysicalPortCapTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 70),
    _PhysicalPortCapTimModeOduTcmA_Type()
)
physicalPortCapTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeOduTcmA.setStatus("current")
_PhysicalPortCapTimModeOduTcmB_Type = TimModeCaps
_PhysicalPortCapTimModeOduTcmB_Object = MibTableColumn
physicalPortCapTimModeOduTcmB = _PhysicalPortCapTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 71),
    _PhysicalPortCapTimModeOduTcmB_Type()
)
physicalPortCapTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeOduTcmB.setStatus("current")
_PhysicalPortCapTimModeOduTcmC_Type = TimModeCaps
_PhysicalPortCapTimModeOduTcmC_Object = MibTableColumn
physicalPortCapTimModeOduTcmC = _PhysicalPortCapTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 72),
    _PhysicalPortCapTimModeOduTcmC_Type()
)
physicalPortCapTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTimModeOduTcmC.setStatus("current")
_PhysicalPortCapTraceFormSonetSection_Type = SonetTraceFormCaps
_PhysicalPortCapTraceFormSonetSection_Object = MibTableColumn
physicalPortCapTraceFormSonetSection = _PhysicalPortCapTraceFormSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 73),
    _PhysicalPortCapTraceFormSonetSection_Type()
)
physicalPortCapTraceFormSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceFormSonetSection.setStatus("current")
_PhysicalPortCapTraceExpectedSonetSection_Type = Integer32
_PhysicalPortCapTraceExpectedSonetSection_Object = MibTableColumn
physicalPortCapTraceExpectedSonetSection = _PhysicalPortCapTraceExpectedSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 74),
    _PhysicalPortCapTraceExpectedSonetSection_Type()
)
physicalPortCapTraceExpectedSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedSonetSection.setStatus("current")
_PhysicalPortCapTraceTransmitSonetSection_Type = Integer32
_PhysicalPortCapTraceTransmitSonetSection_Object = MibTableColumn
physicalPortCapTraceTransmitSonetSection = _PhysicalPortCapTraceTransmitSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 75),
    _PhysicalPortCapTraceTransmitSonetSection_Type()
)
physicalPortCapTraceTransmitSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSonetSection.setStatus("current")
_PhysicalPortCapTraceExpectedOtu_Type = Integer32
_PhysicalPortCapTraceExpectedOtu_Object = MibTableColumn
physicalPortCapTraceExpectedOtu = _PhysicalPortCapTraceExpectedOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 76),
    _PhysicalPortCapTraceExpectedOtu_Type()
)
physicalPortCapTraceExpectedOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedOtu.setStatus("current")
_PhysicalPortCapTraceTransmitSapiOtu_Type = Integer32
_PhysicalPortCapTraceTransmitSapiOtu_Object = MibTableColumn
physicalPortCapTraceTransmitSapiOtu = _PhysicalPortCapTraceTransmitSapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 77),
    _PhysicalPortCapTraceTransmitSapiOtu_Type()
)
physicalPortCapTraceTransmitSapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSapiOtu.setStatus("current")
_PhysicalPortCapTraceTransmitDapiOtu_Type = Integer32
_PhysicalPortCapTraceTransmitDapiOtu_Object = MibTableColumn
physicalPortCapTraceTransmitDapiOtu = _PhysicalPortCapTraceTransmitDapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 78),
    _PhysicalPortCapTraceTransmitDapiOtu_Type()
)
physicalPortCapTraceTransmitDapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitDapiOtu.setStatus("current")
_PhysicalPortCapTraceTransmitOpspOtu_Type = Integer32
_PhysicalPortCapTraceTransmitOpspOtu_Object = MibTableColumn
physicalPortCapTraceTransmitOpspOtu = _PhysicalPortCapTraceTransmitOpspOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 79),
    _PhysicalPortCapTraceTransmitOpspOtu_Type()
)
physicalPortCapTraceTransmitOpspOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitOpspOtu.setStatus("current")
_PhysicalPortCapTraceExpectedOdu_Type = Integer32
_PhysicalPortCapTraceExpectedOdu_Object = MibTableColumn
physicalPortCapTraceExpectedOdu = _PhysicalPortCapTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 80),
    _PhysicalPortCapTraceExpectedOdu_Type()
)
physicalPortCapTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedOdu.setStatus("current")
_PhysicalPortCapTraceTransmitSapiOdu_Type = Integer32
_PhysicalPortCapTraceTransmitSapiOdu_Object = MibTableColumn
physicalPortCapTraceTransmitSapiOdu = _PhysicalPortCapTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 81),
    _PhysicalPortCapTraceTransmitSapiOdu_Type()
)
physicalPortCapTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSapiOdu.setStatus("current")
_PhysicalPortCapTraceTransmitDapiOdu_Type = Integer32
_PhysicalPortCapTraceTransmitDapiOdu_Object = MibTableColumn
physicalPortCapTraceTransmitDapiOdu = _PhysicalPortCapTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 82),
    _PhysicalPortCapTraceTransmitDapiOdu_Type()
)
physicalPortCapTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitDapiOdu.setStatus("current")
_PhysicalPortCapTraceTransmitOpspOdu_Type = Integer32
_PhysicalPortCapTraceTransmitOpspOdu_Object = MibTableColumn
physicalPortCapTraceTransmitOpspOdu = _PhysicalPortCapTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 83),
    _PhysicalPortCapTraceTransmitOpspOdu_Type()
)
physicalPortCapTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitOpspOdu.setStatus("current")
_PhysicalPortCapTraceExpectedOduTcmA_Type = Integer32
_PhysicalPortCapTraceExpectedOduTcmA_Object = MibTableColumn
physicalPortCapTraceExpectedOduTcmA = _PhysicalPortCapTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 84),
    _PhysicalPortCapTraceExpectedOduTcmA_Type()
)
physicalPortCapTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedOduTcmA.setStatus("current")
_PhysicalPortCapTraceTransmitSapiOduTcmA_Type = Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmA_Object = MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmA = _PhysicalPortCapTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 85),
    _PhysicalPortCapTraceTransmitSapiOduTcmA_Type()
)
physicalPortCapTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSapiOduTcmA.setStatus("current")
_PhysicalPortCapTraceTransmitDapiOduTcmA_Type = Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmA_Object = MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmA = _PhysicalPortCapTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 86),
    _PhysicalPortCapTraceTransmitDapiOduTcmA_Type()
)
physicalPortCapTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitDapiOduTcmA.setStatus("current")
_PhysicalPortCapTraceTransmitOpspOduTcmA_Type = Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmA_Object = MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmA = _PhysicalPortCapTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 87),
    _PhysicalPortCapTraceTransmitOpspOduTcmA_Type()
)
physicalPortCapTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitOpspOduTcmA.setStatus("current")
_PhysicalPortCapTraceExpectedOduTcmB_Type = Integer32
_PhysicalPortCapTraceExpectedOduTcmB_Object = MibTableColumn
physicalPortCapTraceExpectedOduTcmB = _PhysicalPortCapTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 88),
    _PhysicalPortCapTraceExpectedOduTcmB_Type()
)
physicalPortCapTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedOduTcmB.setStatus("current")
_PhysicalPortCapTraceTransmitSapiOduTcmB_Type = Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmB_Object = MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmB = _PhysicalPortCapTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 89),
    _PhysicalPortCapTraceTransmitSapiOduTcmB_Type()
)
physicalPortCapTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSapiOduTcmB.setStatus("current")
_PhysicalPortCapTraceTransmitDapiOduTcmB_Type = Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmB_Object = MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmB = _PhysicalPortCapTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 90),
    _PhysicalPortCapTraceTransmitDapiOduTcmB_Type()
)
physicalPortCapTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitDapiOduTcmB.setStatus("current")
_PhysicalPortCapTraceTransmitOpspOduTcmB_Type = Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmB_Object = MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmB = _PhysicalPortCapTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 91),
    _PhysicalPortCapTraceTransmitOpspOduTcmB_Type()
)
physicalPortCapTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitOpspOduTcmB.setStatus("current")
_PhysicalPortCapTraceExpectedOduTcmC_Type = Integer32
_PhysicalPortCapTraceExpectedOduTcmC_Object = MibTableColumn
physicalPortCapTraceExpectedOduTcmC = _PhysicalPortCapTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 92),
    _PhysicalPortCapTraceExpectedOduTcmC_Type()
)
physicalPortCapTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceExpectedOduTcmC.setStatus("current")
_PhysicalPortCapTraceTransmitSapiOduTcmC_Type = Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmC_Object = MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmC = _PhysicalPortCapTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 93),
    _PhysicalPortCapTraceTransmitSapiOduTcmC_Type()
)
physicalPortCapTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitSapiOduTcmC.setStatus("current")
_PhysicalPortCapTraceTransmitDapiOduTcmC_Type = Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmC_Object = MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmC = _PhysicalPortCapTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 94),
    _PhysicalPortCapTraceTransmitDapiOduTcmC_Type()
)
physicalPortCapTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitDapiOduTcmC.setStatus("current")
_PhysicalPortCapTraceTransmitOpspOduTcmC_Type = Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmC_Object = MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmC = _PhysicalPortCapTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 95),
    _PhysicalPortCapTraceTransmitOpspOduTcmC_Type()
)
physicalPortCapTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTraceTransmitOpspOduTcmC.setStatus("current")
_PhysicalPortCapTurnupConfig_Type = FspR7TurnupConfigCaps
_PhysicalPortCapTurnupConfig_Object = MibTableColumn
physicalPortCapTurnupConfig = _PhysicalPortCapTurnupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 96),
    _PhysicalPortCapTurnupConfig_Type()
)
physicalPortCapTurnupConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTurnupConfig.setStatus("current")
_PhysicalPortCapTxOffDelay_Type = FspR7EnableDisableCaps
_PhysicalPortCapTxOffDelay_Object = MibTableColumn
physicalPortCapTxOffDelay = _PhysicalPortCapTxOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 97),
    _PhysicalPortCapTxOffDelay_Type()
)
physicalPortCapTxOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTxOffDelay.setStatus("current")
_PhysicalPortCapVoaMode_Type = FspR7VoaModeCaps
_PhysicalPortCapVoaMode_Object = MibTableColumn
physicalPortCapVoaMode = _PhysicalPortCapVoaMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 98),
    _PhysicalPortCapVoaMode_Type()
)
physicalPortCapVoaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapVoaMode.setStatus("current")
_PhysicalPortCapVoaSetpoint_Type = FspR7Unsigned32Caps
_PhysicalPortCapVoaSetpoint_Object = MibTableColumn
physicalPortCapVoaSetpoint = _PhysicalPortCapVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 99),
    _PhysicalPortCapVoaSetpoint_Type()
)
physicalPortCapVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapVoaSetpoint.setUnits("0.1 dB")
_PhysicalPortCapLagPrio_Type = FspR7Unsigned32Caps
_PhysicalPortCapLagPrio_Object = MibTableColumn
physicalPortCapLagPrio = _PhysicalPortCapLagPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 100),
    _PhysicalPortCapLagPrio_Type()
)
physicalPortCapLagPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapLagPrio.setStatus("current")
_PhysicalPortCapMaxFrameSize_Type = FspR7Unsigned32Caps
_PhysicalPortCapMaxFrameSize_Object = MibTableColumn
physicalPortCapMaxFrameSize = _PhysicalPortCapMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 101),
    _PhysicalPortCapMaxFrameSize_Type()
)
physicalPortCapMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapMaxFrameSize.setStatus("current")
_PhysicalPortCapPayload_Type = OtnPayloadTypeCaps
_PhysicalPortCapPayload_Object = MibTableColumn
physicalPortCapPayload = _PhysicalPortCapPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 102),
    _PhysicalPortCapPayload_Type()
)
physicalPortCapPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPayload.setStatus("current")
_PhysicalPortCapPortMode_Type = FspR7PortModeCaps
_PhysicalPortCapPortMode_Object = MibTableColumn
physicalPortCapPortMode = _PhysicalPortCapPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 103),
    _PhysicalPortCapPortMode_Type()
)
physicalPortCapPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPortMode.setStatus("current")
_PhysicalPortCapPortRole_Type = FspR7PortRoleCaps
_PhysicalPortCapPortRole_Object = MibTableColumn
physicalPortCapPortRole = _PhysicalPortCapPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 104),
    _PhysicalPortCapPortRole_Type()
)
physicalPortCapPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPortRole.setStatus("current")
_PhysicalPortCapPriority_Type = FspR7Unsigned32Caps
_PhysicalPortCapPriority_Object = MibTableColumn
physicalPortCapPriority = _PhysicalPortCapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 105),
    _PhysicalPortCapPriority_Type()
)
physicalPortCapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPriority.setStatus("current")
_PhysicalPortCapPvid_Type = FspR7Unsigned32Caps
_PhysicalPortCapPvid_Object = MibTableColumn
physicalPortCapPvid = _PhysicalPortCapPvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 106),
    _PhysicalPortCapPvid_Type()
)
physicalPortCapPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapPvid.setStatus("current")
_PhysicalPortCapStagType_Type = Integer32
_PhysicalPortCapStagType_Object = MibTableColumn
physicalPortCapStagType = _PhysicalPortCapStagType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 107),
    _PhysicalPortCapStagType_Type()
)
physicalPortCapStagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapStagType.setStatus("current")
_PhysicalPortCapUtag_Type = FspR7UntaggedFramesCaps
_PhysicalPortCapUtag_Object = MibTableColumn
physicalPortCapUtag = _PhysicalPortCapUtag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 108),
    _PhysicalPortCapUtag_Type()
)
physicalPortCapUtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapUtag.setStatus("current")
_PhysicalPortCapVethAid_Type = SnmpAdminString
_PhysicalPortCapVethAid_Object = MibTableColumn
physicalPortCapVethAid = _PhysicalPortCapVethAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 109),
    _PhysicalPortCapVethAid_Type()
)
physicalPortCapVethAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapVethAid.setStatus("current")
_PhysicalPortCapRedLineState_Type = FspR7RedLinedStateCaps
_PhysicalPortCapRedLineState_Object = MibTableColumn
physicalPortCapRedLineState = _PhysicalPortCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 110),
    _PhysicalPortCapRedLineState_Type()
)
physicalPortCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapRedLineState.setStatus("current")
_PhysicalPortCapTunnelAid_Type = Integer32
_PhysicalPortCapTunnelAid_Object = MibTableColumn
physicalPortCapTunnelAid = _PhysicalPortCapTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 111),
    _PhysicalPortCapTunnelAid_Type()
)
physicalPortCapTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTunnelAid.setStatus("current")
_PhysicalPortCapRateLimit_Type = FspR7DisableEnableCaps
_PhysicalPortCapRateLimit_Object = MibTableColumn
physicalPortCapRateLimit = _PhysicalPortCapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 112),
    _PhysicalPortCapRateLimit_Type()
)
physicalPortCapRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapRateLimit.setStatus("current")
_PhysicalPortCapTxOffOnTm_Type = FspR7TxOffOnTmCaps
_PhysicalPortCapTxOffOnTm_Object = MibTableColumn
physicalPortCapTxOffOnTm = _PhysicalPortCapTxOffOnTm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 113),
    _PhysicalPortCapTxOffOnTm_Type()
)
physicalPortCapTxOffOnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTxOffOnTm.setStatus("current")
_PhysicalPortCapTxOffTimer_Type = FspR7Unsigned32Caps
_PhysicalPortCapTxOffTimer_Object = MibTableColumn
physicalPortCapTxOffTimer = _PhysicalPortCapTxOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 114),
    _PhysicalPortCapTxOffTimer_Type()
)
physicalPortCapTxOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTxOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapTxOffTimer.setUnits("ms")
_PhysicalPortCapTxOnTimer_Type = FspR7Unsigned32Caps
_PhysicalPortCapTxOnTimer_Object = MibTableColumn
physicalPortCapTxOnTimer = _PhysicalPortCapTxOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 1, 1, 115),
    _PhysicalPortCapTxOnTimer_Type()
)
physicalPortCapTxOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCapTxOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortCapTxOnTimer.setUnits("ms")
_VirtualPortCapTable_Object = MibTable
virtualPortCapTable = _VirtualPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2)
)
if mibBuilder.loadTexts:
    virtualPortCapTable.setStatus("current")
_VirtualPortCapEntry_Object = MibTableRow
virtualPortCapEntry = _VirtualPortCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1)
)
virtualPortCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    virtualPortCapEntry.setStatus("current")
_VirtualPortCapRowStatus_Type = FspR7RowStatusCaps
_VirtualPortCapRowStatus_Object = MibTableColumn
virtualPortCapRowStatus = _VirtualPortCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 1),
    _VirtualPortCapRowStatus_Type()
)
virtualPortCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapRowStatus.setStatus("current")
_VirtualPortCapChannelBand_Type = FspR7ChannelBandwidthCaps
_VirtualPortCapChannelBand_Object = MibTableColumn
virtualPortCapChannelBand = _VirtualPortCapChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 2),
    _VirtualPortCapChannelBand_Type()
)
virtualPortCapChannelBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapChannelBand.setStatus("current")
_VirtualPortCapType_Type = FspR7InterfaceTypeCaps
_VirtualPortCapType_Object = MibTableColumn
virtualPortCapType = _VirtualPortCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 3),
    _VirtualPortCapType_Type()
)
virtualPortCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapType.setStatus("current")
_VirtualPortCapAlias_Type = Integer32
_VirtualPortCapAlias_Object = MibTableColumn
virtualPortCapAlias = _VirtualPortCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 4),
    _VirtualPortCapAlias_Type()
)
virtualPortCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapAlias.setStatus("current")
_VirtualPortCapAdmin_Type = FspR7AdminStateCaps
_VirtualPortCapAdmin_Object = MibTableColumn
virtualPortCapAdmin = _VirtualPortCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 5),
    _VirtualPortCapAdmin_Type()
)
virtualPortCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapAdmin.setStatus("current")
_VirtualPortCapEqlzAdmin_Type = FspR7EqlzAdminStateCaps
_VirtualPortCapEqlzAdmin_Object = MibTableColumn
virtualPortCapEqlzAdmin = _VirtualPortCapEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 6),
    _VirtualPortCapEqlzAdmin_Type()
)
virtualPortCapEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapEqlzAdmin.setStatus("current")
_VirtualPortCapInitEqlz_Type = FspR7InitEqualizationCaps
_VirtualPortCapInitEqlz_Object = MibTableColumn
virtualPortCapInitEqlz = _VirtualPortCapInitEqlz_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 7),
    _VirtualPortCapInitEqlz_Type()
)
virtualPortCapInitEqlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapInitEqlz.setStatus("current")
_VirtualPortCapLacpMode_Type = FspR7LacpModeCaps
_VirtualPortCapLacpMode_Object = MibTableColumn
virtualPortCapLacpMode = _VirtualPortCapLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 8),
    _VirtualPortCapLacpMode_Type()
)
virtualPortCapLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapLacpMode.setStatus("current")
_VirtualPortCapLacpTimeout_Type = FspR7LacpTimeoutCaps
_VirtualPortCapLacpTimeout_Object = MibTableColumn
virtualPortCapLacpTimeout = _VirtualPortCapLacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 9),
    _VirtualPortCapLacpTimeout_Type()
)
virtualPortCapLacpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapLacpTimeout.setStatus("current")
_VirtualPortCapLagActivePorts_Type = FspR7Unsigned32Caps
_VirtualPortCapLagActivePorts_Object = MibTableColumn
virtualPortCapLagActivePorts = _VirtualPortCapLagActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 10),
    _VirtualPortCapLagActivePorts_Type()
)
virtualPortCapLagActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapLagActivePorts.setStatus("current")
_VirtualPortCapMaxFrameSize_Type = FspR7Unsigned32Caps
_VirtualPortCapMaxFrameSize_Object = MibTableColumn
virtualPortCapMaxFrameSize = _VirtualPortCapMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 11),
    _VirtualPortCapMaxFrameSize_Type()
)
virtualPortCapMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapMaxFrameSize.setStatus("current")
_VirtualPortCapPortMode_Type = FspR7PortModeCaps
_VirtualPortCapPortMode_Object = MibTableColumn
virtualPortCapPortMode = _VirtualPortCapPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 12),
    _VirtualPortCapPortMode_Type()
)
virtualPortCapPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapPortMode.setStatus("current")
_VirtualPortCapDataLayerPmReset_Type = FspR7PmResetCaps
_VirtualPortCapDataLayerPmReset_Object = MibTableColumn
virtualPortCapDataLayerPmReset = _VirtualPortCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 13),
    _VirtualPortCapDataLayerPmReset_Type()
)
virtualPortCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapDataLayerPmReset.setStatus("current")
_VirtualPortCapPortRole_Type = FspR7PortRoleCaps
_VirtualPortCapPortRole_Object = MibTableColumn
virtualPortCapPortRole = _VirtualPortCapPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 14),
    _VirtualPortCapPortRole_Type()
)
virtualPortCapPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapPortRole.setStatus("current")
_VirtualPortCapLagPortType_Type = FspR7LagPortTypeCaps
_VirtualPortCapLagPortType_Object = MibTableColumn
virtualPortCapLagPortType = _VirtualPortCapLagPortType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 15),
    _VirtualPortCapLagPortType_Type()
)
virtualPortCapLagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapLagPortType.setStatus("current")
_VirtualPortCapPriority_Type = FspR7Unsigned32Caps
_VirtualPortCapPriority_Object = MibTableColumn
virtualPortCapPriority = _VirtualPortCapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 16),
    _VirtualPortCapPriority_Type()
)
virtualPortCapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapPriority.setStatus("current")
_VirtualPortCapPvid_Type = FspR7Unsigned32Caps
_VirtualPortCapPvid_Object = MibTableColumn
virtualPortCapPvid = _VirtualPortCapPvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 17),
    _VirtualPortCapPvid_Type()
)
virtualPortCapPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapPvid.setStatus("current")
_VirtualPortCapRevertiveMode_Type = ApsRevertModeCaps
_VirtualPortCapRevertiveMode_Object = MibTableColumn
virtualPortCapRevertiveMode = _VirtualPortCapRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 18),
    _VirtualPortCapRevertiveMode_Type()
)
virtualPortCapRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapRevertiveMode.setStatus("current")
_VirtualPortCapStagType_Type = Integer32
_VirtualPortCapStagType_Object = MibTableColumn
virtualPortCapStagType = _VirtualPortCapStagType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 19),
    _VirtualPortCapStagType_Type()
)
virtualPortCapStagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapStagType.setStatus("current")
_VirtualPortCapUtag_Type = FspR7UntaggedFramesCaps
_VirtualPortCapUtag_Object = MibTableColumn
virtualPortCapUtag = _VirtualPortCapUtag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 20),
    _VirtualPortCapUtag_Type()
)
virtualPortCapUtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapUtag.setStatus("current")
_VirtualPortCapBundle_Type = FspR7SnmpLongString
_VirtualPortCapBundle_Object = MibTableColumn
virtualPortCapBundle = _VirtualPortCapBundle_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 21),
    _VirtualPortCapBundle_Type()
)
virtualPortCapBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapBundle.setStatus("current")
_VirtualPortCapSwitchCommand_Type = FspR7APSCommandCaps
_VirtualPortCapSwitchCommand_Object = MibTableColumn
virtualPortCapSwitchCommand = _VirtualPortCapSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 22),
    _VirtualPortCapSwitchCommand_Type()
)
virtualPortCapSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSwitchCommand.setStatus("current")
_VirtualPortCapInhibitSwitchToWork_Type = FspR7YesNoCaps
_VirtualPortCapInhibitSwitchToWork_Object = MibTableColumn
virtualPortCapInhibitSwitchToWork = _VirtualPortCapInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 23),
    _VirtualPortCapInhibitSwitchToWork_Type()
)
virtualPortCapInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapInhibitSwitchToWork.setStatus("current")
_VirtualPortCapInhibitSwitchToProt_Type = FspR7YesNoCaps
_VirtualPortCapInhibitSwitchToProt_Object = MibTableColumn
virtualPortCapInhibitSwitchToProt = _VirtualPortCapInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 24),
    _VirtualPortCapInhibitSwitchToProt_Type()
)
virtualPortCapInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapInhibitSwitchToProt.setStatus("current")
_VirtualPortCapOduTribPortNo_Type = SnmpAdminString
_VirtualPortCapOduTribPortNo_Object = MibTableColumn
virtualPortCapOduTribPortNo = _VirtualPortCapOduTribPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 25),
    _VirtualPortCapOduTribPortNo_Type()
)
virtualPortCapOduTribPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapOduTribPortNo.setStatus("current")
_VirtualPortCapOduTribTimeSlottNo_Type = SnmpAdminString
_VirtualPortCapOduTribTimeSlottNo_Object = MibTableColumn
virtualPortCapOduTribTimeSlottNo = _VirtualPortCapOduTribTimeSlottNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 26),
    _VirtualPortCapOduTribTimeSlottNo_Type()
)
virtualPortCapOduTribTimeSlottNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapOduTribTimeSlottNo.setStatus("current")
_VirtualPortCapSigDegThresOdu_Type = FspR7Integer32Caps
_VirtualPortCapSigDegThresOdu_Object = MibTableColumn
virtualPortCapSigDegThresOdu = _VirtualPortCapSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 27),
    _VirtualPortCapSigDegThresOdu_Type()
)
virtualPortCapSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOdu.setUnits("%")
_VirtualPortCapSigDegPeriodOdu_Type = FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOdu_Object = MibTableColumn
virtualPortCapSigDegPeriodOdu = _VirtualPortCapSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 28),
    _VirtualPortCapSigDegPeriodOdu_Type()
)
virtualPortCapSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOdu.setUnits("s")
_VirtualPortCapTraceExpectedOdu_Type = Integer32
_VirtualPortCapTraceExpectedOdu_Object = MibTableColumn
virtualPortCapTraceExpectedOdu = _VirtualPortCapTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 29),
    _VirtualPortCapTraceExpectedOdu_Type()
)
virtualPortCapTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceExpectedOdu.setStatus("current")
_VirtualPortCapTraceTransmitSapiOdu_Type = Integer32
_VirtualPortCapTraceTransmitSapiOdu_Object = MibTableColumn
virtualPortCapTraceTransmitSapiOdu = _VirtualPortCapTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 30),
    _VirtualPortCapTraceTransmitSapiOdu_Type()
)
virtualPortCapTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitSapiOdu.setStatus("current")
_VirtualPortCapTraceTransmitDapiOdu_Type = Integer32
_VirtualPortCapTraceTransmitDapiOdu_Object = MibTableColumn
virtualPortCapTraceTransmitDapiOdu = _VirtualPortCapTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 31),
    _VirtualPortCapTraceTransmitDapiOdu_Type()
)
virtualPortCapTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitDapiOdu.setStatus("current")
_VirtualPortCapTraceTransmitOpspOdu_Type = Integer32
_VirtualPortCapTraceTransmitOpspOdu_Object = MibTableColumn
virtualPortCapTraceTransmitOpspOdu = _VirtualPortCapTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 32),
    _VirtualPortCapTraceTransmitOpspOdu_Type()
)
virtualPortCapTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitOpspOdu.setStatus("current")
_VirtualPortCapTimModeOdu_Type = TimModeCaps
_VirtualPortCapTimModeOdu_Object = MibTableColumn
virtualPortCapTimModeOdu = _VirtualPortCapTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 33),
    _VirtualPortCapTimModeOdu_Type()
)
virtualPortCapTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTimModeOdu.setStatus("current")
_VirtualPortCapSigDegThresOduTcmA_Type = FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmA_Object = MibTableColumn
virtualPortCapSigDegThresOduTcmA = _VirtualPortCapSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 34),
    _VirtualPortCapSigDegThresOduTcmA_Type()
)
virtualPortCapSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmA.setUnits("%")
_VirtualPortCapSigDegPeriodOduTcmA_Type = FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmA_Object = MibTableColumn
virtualPortCapSigDegPeriodOduTcmA = _VirtualPortCapSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 35),
    _VirtualPortCapSigDegPeriodOduTcmA_Type()
)
virtualPortCapSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmA.setUnits("s")
_VirtualPortCapSigDegThresOduTcmB_Type = FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmB_Object = MibTableColumn
virtualPortCapSigDegThresOduTcmB = _VirtualPortCapSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 36),
    _VirtualPortCapSigDegThresOduTcmB_Type()
)
virtualPortCapSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmB.setUnits("%")
_VirtualPortCapSigDegPeriodOduTcmB_Type = FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmB_Object = MibTableColumn
virtualPortCapSigDegPeriodOduTcmB = _VirtualPortCapSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 37),
    _VirtualPortCapSigDegPeriodOduTcmB_Type()
)
virtualPortCapSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmB.setUnits("s")
_VirtualPortCapSigDegThresOduTcmC_Type = FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmC_Object = MibTableColumn
virtualPortCapSigDegThresOduTcmC = _VirtualPortCapSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 38),
    _VirtualPortCapSigDegThresOduTcmC_Type()
)
virtualPortCapSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegThresOduTcmC.setUnits("%")
_VirtualPortCapSigDegPeriodOduTcmC_Type = FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmC_Object = MibTableColumn
virtualPortCapSigDegPeriodOduTcmC = _VirtualPortCapSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 39),
    _VirtualPortCapSigDegPeriodOduTcmC_Type()
)
virtualPortCapSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapSigDegPeriodOduTcmC.setUnits("s")
_VirtualPortCapTcmALevel_Type = OtnTcmLevelCaps
_VirtualPortCapTcmALevel_Object = MibTableColumn
virtualPortCapTcmALevel = _VirtualPortCapTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 40),
    _VirtualPortCapTcmALevel_Type()
)
virtualPortCapTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTcmALevel.setStatus("current")
_VirtualPortCapTcmBLevel_Type = OtnTcmLevelCaps
_VirtualPortCapTcmBLevel_Object = MibTableColumn
virtualPortCapTcmBLevel = _VirtualPortCapTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 41),
    _VirtualPortCapTcmBLevel_Type()
)
virtualPortCapTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTcmBLevel.setStatus("current")
_VirtualPortCapTcmCLevel_Type = OtnTcmLevelCaps
_VirtualPortCapTcmCLevel_Object = MibTableColumn
virtualPortCapTcmCLevel = _VirtualPortCapTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 42),
    _VirtualPortCapTcmCLevel_Type()
)
virtualPortCapTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTcmCLevel.setStatus("current")
_VirtualPortCapTraceTransmitSapiOduTcmA_Type = Integer32
_VirtualPortCapTraceTransmitSapiOduTcmA_Object = MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmA = _VirtualPortCapTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 43),
    _VirtualPortCapTraceTransmitSapiOduTcmA_Type()
)
virtualPortCapTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitSapiOduTcmA.setStatus("current")
_VirtualPortCapTraceTransmitDapiOduTcmA_Type = Integer32
_VirtualPortCapTraceTransmitDapiOduTcmA_Object = MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmA = _VirtualPortCapTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 44),
    _VirtualPortCapTraceTransmitDapiOduTcmA_Type()
)
virtualPortCapTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitDapiOduTcmA.setStatus("current")
_VirtualPortCapTraceTransmitOpspOduTcmA_Type = Integer32
_VirtualPortCapTraceTransmitOpspOduTcmA_Object = MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmA = _VirtualPortCapTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 45),
    _VirtualPortCapTraceTransmitOpspOduTcmA_Type()
)
virtualPortCapTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitOpspOduTcmA.setStatus("current")
_VirtualPortCapTraceExpectedOduTcmA_Type = Integer32
_VirtualPortCapTraceExpectedOduTcmA_Object = MibTableColumn
virtualPortCapTraceExpectedOduTcmA = _VirtualPortCapTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 46),
    _VirtualPortCapTraceExpectedOduTcmA_Type()
)
virtualPortCapTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceExpectedOduTcmA.setStatus("current")
_VirtualPortCapTimModeOduTcmA_Type = TimModeCaps
_VirtualPortCapTimModeOduTcmA_Object = MibTableColumn
virtualPortCapTimModeOduTcmA = _VirtualPortCapTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 47),
    _VirtualPortCapTimModeOduTcmA_Type()
)
virtualPortCapTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTimModeOduTcmA.setStatus("current")
_VirtualPortCapTraceExpectedOduTcmB_Type = Integer32
_VirtualPortCapTraceExpectedOduTcmB_Object = MibTableColumn
virtualPortCapTraceExpectedOduTcmB = _VirtualPortCapTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 48),
    _VirtualPortCapTraceExpectedOduTcmB_Type()
)
virtualPortCapTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceExpectedOduTcmB.setStatus("current")
_VirtualPortCapTraceTransmitSapiOduTcmB_Type = Integer32
_VirtualPortCapTraceTransmitSapiOduTcmB_Object = MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmB = _VirtualPortCapTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 49),
    _VirtualPortCapTraceTransmitSapiOduTcmB_Type()
)
virtualPortCapTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitSapiOduTcmB.setStatus("current")
_VirtualPortCapTraceTransmitDapiOduTcmB_Type = Integer32
_VirtualPortCapTraceTransmitDapiOduTcmB_Object = MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmB = _VirtualPortCapTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 50),
    _VirtualPortCapTraceTransmitDapiOduTcmB_Type()
)
virtualPortCapTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitDapiOduTcmB.setStatus("current")
_VirtualPortCapTraceTransmitOpspOduTcmB_Type = Integer32
_VirtualPortCapTraceTransmitOpspOduTcmB_Object = MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmB = _VirtualPortCapTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 51),
    _VirtualPortCapTraceTransmitOpspOduTcmB_Type()
)
virtualPortCapTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitOpspOduTcmB.setStatus("current")
_VirtualPortCapTimModeOduTcmB_Type = TimModeCaps
_VirtualPortCapTimModeOduTcmB_Object = MibTableColumn
virtualPortCapTimModeOduTcmB = _VirtualPortCapTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 52),
    _VirtualPortCapTimModeOduTcmB_Type()
)
virtualPortCapTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTimModeOduTcmB.setStatus("current")
_VirtualPortCapTraceExpectedOduTcmC_Type = Integer32
_VirtualPortCapTraceExpectedOduTcmC_Object = MibTableColumn
virtualPortCapTraceExpectedOduTcmC = _VirtualPortCapTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 53),
    _VirtualPortCapTraceExpectedOduTcmC_Type()
)
virtualPortCapTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceExpectedOduTcmC.setStatus("current")
_VirtualPortCapTraceTransmitSapiOduTcmC_Type = Integer32
_VirtualPortCapTraceTransmitSapiOduTcmC_Object = MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmC = _VirtualPortCapTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 54),
    _VirtualPortCapTraceTransmitSapiOduTcmC_Type()
)
virtualPortCapTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitSapiOduTcmC.setStatus("current")
_VirtualPortCapTraceTransmitDapiOduTcmC_Type = Integer32
_VirtualPortCapTraceTransmitDapiOduTcmC_Object = MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmC = _VirtualPortCapTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 55),
    _VirtualPortCapTraceTransmitDapiOduTcmC_Type()
)
virtualPortCapTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitDapiOduTcmC.setStatus("current")
_VirtualPortCapTraceTransmitOpspOduTcmC_Type = Integer32
_VirtualPortCapTraceTransmitOpspOduTcmC_Object = MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmC = _VirtualPortCapTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 56),
    _VirtualPortCapTraceTransmitOpspOduTcmC_Type()
)
virtualPortCapTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTraceTransmitOpspOduTcmC.setStatus("current")
_VirtualPortCapTimModeOduTcmC_Type = TimModeCaps
_VirtualPortCapTimModeOduTcmC_Object = MibTableColumn
virtualPortCapTimModeOduTcmC = _VirtualPortCapTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 57),
    _VirtualPortCapTimModeOduTcmC_Type()
)
virtualPortCapTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTimModeOduTcmC.setStatus("current")
_VirtualPortCapTerminationLevel_Type = OhTerminationLevelCaps
_VirtualPortCapTerminationLevel_Object = MibTableColumn
virtualPortCapTerminationLevel = _VirtualPortCapTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 58),
    _VirtualPortCapTerminationLevel_Type()
)
virtualPortCapTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTerminationLevel.setStatus("current")
_VirtualPortCapLoopConfig_Type = LoopConfigCaps
_VirtualPortCapLoopConfig_Object = MibTableColumn
virtualPortCapLoopConfig = _VirtualPortCapLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 59),
    _VirtualPortCapLoopConfig_Type()
)
virtualPortCapLoopConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapLoopConfig.setStatus("current")
_VirtualPortCapVcType_Type = VirtualContainerTypeCaps
_VirtualPortCapVcType_Object = MibTableColumn
virtualPortCapVcType = _VirtualPortCapVcType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 60),
    _VirtualPortCapVcType_Type()
)
virtualPortCapVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapVcType.setStatus("current")
_VirtualPortCapCir_Type = FspR7Unsigned32Caps
_VirtualPortCapCir_Object = MibTableColumn
virtualPortCapCir = _VirtualPortCapCir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 61),
    _VirtualPortCapCir_Type()
)
virtualPortCapCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapCir.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortCapCir.setUnits("Mbps")
_VirtualPortCapOpuPayloadType_Type = FspR7OpuPayloadTypeCaps
_VirtualPortCapOpuPayloadType_Object = MibTableColumn
virtualPortCapOpuPayloadType = _VirtualPortCapOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 62),
    _VirtualPortCapOpuPayloadType_Type()
)
virtualPortCapOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapOpuPayloadType.setStatus("current")
_VirtualPortCapOtnStuffing_Type = FspR7StuffCaps
_VirtualPortCapOtnStuffing_Object = MibTableColumn
virtualPortCapOtnStuffing = _VirtualPortCapOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 63),
    _VirtualPortCapOtnStuffing_Type()
)
virtualPortCapOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapOtnStuffing.setStatus("current")
_VirtualPortCapRedLineState_Type = FspR7RedLinedStateCaps
_VirtualPortCapRedLineState_Object = MibTableColumn
virtualPortCapRedLineState = _VirtualPortCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 64),
    _VirtualPortCapRedLineState_Type()
)
virtualPortCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapRedLineState.setStatus("current")
_VirtualPortCapTunnelAid_Type = Integer32
_VirtualPortCapTunnelAid_Object = MibTableColumn
virtualPortCapTunnelAid = _VirtualPortCapTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 65),
    _VirtualPortCapTunnelAid_Type()
)
virtualPortCapTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTunnelAid.setStatus("current")
_VirtualPortCapTrafficDirection_Type = FspR7TrafficDirectionCaps
_VirtualPortCapTrafficDirection_Object = MibTableColumn
virtualPortCapTrafficDirection = _VirtualPortCapTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 66),
    _VirtualPortCapTrafficDirection_Type()
)
virtualPortCapTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapTrafficDirection.setStatus("current")
_VirtualPortCapChannelId_Type = FspR7SnmpLongString
_VirtualPortCapChannelId_Object = MibTableColumn
virtualPortCapChannelId = _VirtualPortCapChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 2, 1, 67),
    _VirtualPortCapChannelId_Type()
)
virtualPortCapChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortCapChannelId.setStatus("current")
_EndOfVirtualPortCapTable_Type = Integer32
_EndOfVirtualPortCapTable_Object = MibScalar
endOfVirtualPortCapTable = _EndOfVirtualPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 3),
    _EndOfVirtualPortCapTable_Type()
)
endOfVirtualPortCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfVirtualPortCapTable.setStatus("current")
_EndOfFacilityMgmtCap_Type = Integer32
_EndOfFacilityMgmtCap_Object = MibScalar
endOfFacilityMgmtCap = _EndOfFacilityMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 4, 10000),
    _EndOfFacilityMgmtCap_Type()
)
endOfFacilityMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFacilityMgmtCap.setStatus("current")
_DcnMgmtCap_ObjectIdentity = ObjectIdentity
dcnMgmtCap = _DcnMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5)
)
_LinkCapTable_Object = MibTable
linkCapTable = _LinkCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1)
)
if mibBuilder.loadTexts:
    linkCapTable.setStatus("current")
_LinkCapEntry_Object = MibTableRow
linkCapEntry = _LinkCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1)
)
linkCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    linkCapEntry.setStatus("current")
_LinkCapRowStatus_Type = FspR7RowStatusCaps
_LinkCapRowStatus_Object = MibTableColumn
linkCapRowStatus = _LinkCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 1),
    _LinkCapRowStatus_Type()
)
linkCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapRowStatus.setStatus("current")
_LinkCapType_Type = FspR7InterfaceTypeCaps
_LinkCapType_Object = MibTableColumn
linkCapType = _LinkCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 2),
    _LinkCapType_Type()
)
linkCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapType.setStatus("current")
_LinkCapAdmin_Type = FspR7AdminStateCaps
_LinkCapAdmin_Object = MibTableColumn
linkCapAdmin = _LinkCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 3),
    _LinkCapAdmin_Type()
)
linkCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapAdmin.setStatus("current")
_LinkCapAlias_Type = Integer32
_LinkCapAlias_Object = MibTableColumn
linkCapAlias = _LinkCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 4),
    _LinkCapAlias_Type()
)
linkCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapAlias.setStatus("current")
_LinkCapAuthString_Type = Integer32
_LinkCapAuthString_Object = MibTableColumn
linkCapAuthString = _LinkCapAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 5),
    _LinkCapAuthString_Type()
)
linkCapAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapAuthString.setStatus("current")
_LinkCapProxyArp_Type = FspR7NoYesCaps
_LinkCapProxyArp_Object = MibTableColumn
linkCapProxyArp = _LinkCapProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 6),
    _LinkCapProxyArp_Type()
)
linkCapProxyArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapProxyArp.setStatus("current")
_LinkCapOspf_Type = FspR7OspfModeCaps
_LinkCapOspf_Object = MibTableColumn
linkCapOspf = _LinkCapOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 7),
    _LinkCapOspf_Type()
)
linkCapOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapOspf.setStatus("current")
_LinkCapBaud_Type = FspR7BaundCaps
_LinkCapBaud_Object = MibTableColumn
linkCapBaud = _LinkCapBaud_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 8),
    _LinkCapBaud_Type()
)
linkCapBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapBaud.setStatus("current")
_LinkCapAuthType_Type = FspR7CpAuthTypeCaps
_LinkCapAuthType_Object = MibTableColumn
linkCapAuthType = _LinkCapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 9),
    _LinkCapAuthType_Type()
)
linkCapAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapAuthType.setStatus("current")
_LinkCapIpType_Type = FspR7IpTypeCaps
_LinkCapIpType_Object = MibTableColumn
linkCapIpType = _LinkCapIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 10),
    _LinkCapIpType_Type()
)
linkCapIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapIpType.setStatus("current")
_LinkCapMetric_Type = FspR7Unsigned32Caps
_LinkCapMetric_Object = MibTableColumn
linkCapMetric = _LinkCapMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 11),
    _LinkCapMetric_Type()
)
linkCapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapMetric.setStatus("current")
_LinkCapAreaAid_Type = SnmpAdminString
_LinkCapAreaAid_Object = MibTableColumn
linkCapAreaAid = _LinkCapAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 12),
    _LinkCapAreaAid_Type()
)
linkCapAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapAreaAid.setStatus("current")
_LinkCapNearEndIp_Type = FspR7YesNo
_LinkCapNearEndIp_Object = MibTableColumn
linkCapNearEndIp = _LinkCapNearEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 13),
    _LinkCapNearEndIp_Type()
)
linkCapNearEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapNearEndIp.setStatus("current")
_LinkCapBitrate_Type = FspR7Unsigned32Caps
_LinkCapBitrate_Object = MibTableColumn
linkCapBitrate = _LinkCapBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 14),
    _LinkCapBitrate_Type()
)
linkCapBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapBitrate.setStatus("current")
if mibBuilder.loadTexts:
    linkCapBitrate.setUnits("kbps")
_LinkCapIPv6Type_Type = FspR7IPv6TypeCaps
_LinkCapIPv6Type_Object = MibTableColumn
linkCapIPv6Type = _LinkCapIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 15),
    _LinkCapIPv6Type_Type()
)
linkCapIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapIPv6Type.setStatus("current")
_LinkCapNendIPv6_Type = FspR7YesNo
_LinkCapNendIPv6_Object = MibTableColumn
linkCapNendIPv6 = _LinkCapNendIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 1, 1, 16),
    _LinkCapNendIPv6_Type()
)
linkCapNendIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapNendIPv6.setStatus("current")
_EndOfLinkCapTable_Type = Integer32
_EndOfLinkCapTable_Object = MibScalar
endOfLinkCapTable = _EndOfLinkCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 2),
    _EndOfLinkCapTable_Type()
)
endOfLinkCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfLinkCapTable.setStatus("current")
_ScCapTable_Object = MibTable
scCapTable = _ScCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3)
)
if mibBuilder.loadTexts:
    scCapTable.setStatus("current")
_ScCapEntry_Object = MibTableRow
scCapEntry = _ScCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1)
)
scCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    scCapEntry.setStatus("current")
_ScCapRowStatus_Type = FspR7RowStatusCaps
_ScCapRowStatus_Object = MibTableColumn
scCapRowStatus = _ScCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 1),
    _ScCapRowStatus_Type()
)
scCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapRowStatus.setStatus("current")
_ScCapType_Type = FspR7InterfaceTypeCaps
_ScCapType_Object = MibTableColumn
scCapType = _ScCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 2),
    _ScCapType_Type()
)
scCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapType.setStatus("current")
_ScCapAdmin_Type = FspR7AdminStateCaps
_ScCapAdmin_Object = MibTableColumn
scCapAdmin = _ScCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 3),
    _ScCapAdmin_Type()
)
scCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAdmin.setStatus("current")
_ScCapAlias_Type = Integer32
_ScCapAlias_Object = MibTableColumn
scCapAlias = _ScCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 4),
    _ScCapAlias_Type()
)
scCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAlias.setStatus("current")
_ScCapAuthString_Type = Integer32
_ScCapAuthString_Object = MibTableColumn
scCapAuthString = _ScCapAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 5),
    _ScCapAuthString_Type()
)
scCapAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAuthString.setStatus("current")
_ScCapOspf_Type = FspR7OspfModeCaps
_ScCapOspf_Object = MibTableColumn
scCapOspf = _ScCapOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 6),
    _ScCapOspf_Type()
)
scCapOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapOspf.setStatus("current")
_ScCapAuthType_Type = FspR7CpAuthTypeCaps
_ScCapAuthType_Object = MibTableColumn
scCapAuthType = _ScCapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 7),
    _ScCapAuthType_Type()
)
scCapAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAuthType.setStatus("current")
_ScCapIpType_Type = FspR7IpTypeCaps
_ScCapIpType_Object = MibTableColumn
scCapIpType = _ScCapIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 8),
    _ScCapIpType_Type()
)
scCapIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIpType.setStatus("current")
_ScCapMetric_Type = FspR7Unsigned32Caps
_ScCapMetric_Object = MibTableColumn
scCapMetric = _ScCapMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 9),
    _ScCapMetric_Type()
)
scCapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapMetric.setStatus("current")
_ScCapAreaAid_Type = SnmpAdminString
_ScCapAreaAid_Object = MibTableColumn
scCapAreaAid = _ScCapAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 10),
    _ScCapAreaAid_Type()
)
scCapAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAreaAid.setStatus("current")
_ScCapAlsMode_Type = FspR7AlsModeCaps
_ScCapAlsMode_Object = MibTableColumn
scCapAlsMode = _ScCapAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 11),
    _ScCapAlsMode_Type()
)
scCapAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAlsMode.setStatus("current")
_ScCapSigDegThresReceiver_Type = FspR7Unsigned32Caps
_ScCapSigDegThresReceiver_Object = MibTableColumn
scCapSigDegThresReceiver = _ScCapSigDegThresReceiver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 12),
    _ScCapSigDegThresReceiver_Type()
)
scCapSigDegThresReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapSigDegThresReceiver.setStatus("current")
if mibBuilder.loadTexts:
    scCapSigDegThresReceiver.setUnits("0.1 dB")
_ScCapAutonegotiation_Type = EnableStateCaps
_ScCapAutonegotiation_Object = MibTableColumn
scCapAutonegotiation = _ScCapAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 13),
    _ScCapAutonegotiation_Type()
)
scCapAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAutonegotiation.setStatus("current")
_ScCapBitrate_Type = FspR7BitrateCaps
_ScCapBitrate_Object = MibTableColumn
scCapBitrate = _ScCapBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 14),
    _ScCapBitrate_Type()
)
scCapBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapBitrate.setStatus("current")
_ScCapDuplex_Type = EthDuplexModeCaps
_ScCapDuplex_Object = MibTableColumn
scCapDuplex = _ScCapDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 15),
    _ScCapDuplex_Type()
)
scCapDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapDuplex.setStatus("current")
_ScCapAttGradientTh_Type = FspR7Unsigned32Caps
_ScCapAttGradientTh_Object = MibTableColumn
scCapAttGradientTh = _ScCapAttGradientTh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 16),
    _ScCapAttGradientTh_Type()
)
scCapAttGradientTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapAttGradientTh.setStatus("current")
if mibBuilder.loadTexts:
    scCapAttGradientTh.setUnits("0.1 dB/min")
_ScCapIpAddr_Type = FspR7YesNo
_ScCapIpAddr_Object = MibTableColumn
scCapIpAddr = _ScCapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 17),
    _ScCapIpAddr_Type()
)
scCapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIpAddr.setStatus("current")
_ScCapLanAid_Type = SnmpAdminString
_ScCapLanAid_Object = MibTableColumn
scCapLanAid = _ScCapLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 18),
    _ScCapLanAid_Type()
)
scCapLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapLanAid.setStatus("current")
_ScCapIpMask_Type = FspR7YesNo
_ScCapIpMask_Object = MibTableColumn
scCapIpMask = _ScCapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 19),
    _ScCapIpMask_Type()
)
scCapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIpMask.setStatus("current")
_ScCapDataLayerPmReset_Type = FspR7PmResetCaps
_ScCapDataLayerPmReset_Object = MibTableColumn
scCapDataLayerPmReset = _ScCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 20),
    _ScCapDataLayerPmReset_Type()
)
scCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapDataLayerPmReset.setStatus("current")
_ScCapPriority_Type = FspR7Unsigned32Caps
_ScCapPriority_Object = MibTableColumn
scCapPriority = _ScCapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 21),
    _ScCapPriority_Type()
)
scCapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapPriority.setStatus("current")
_ScCapIPv6_Type = FspR7YesNo
_ScCapIPv6_Object = MibTableColumn
scCapIPv6 = _ScCapIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 22),
    _ScCapIPv6_Type()
)
scCapIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIPv6.setStatus("current")
_ScCapIPv6PrefixLen_Type = FspR7Unsigned32Caps
_ScCapIPv6PrefixLen_Object = MibTableColumn
scCapIPv6PrefixLen = _ScCapIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 23),
    _ScCapIPv6PrefixLen_Type()
)
scCapIPv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIPv6PrefixLen.setStatus("current")
_ScCapIpMode_Type = FspR7IpModeCaps
_ScCapIpMode_Object = MibTableColumn
scCapIpMode = _ScCapIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 24),
    _ScCapIpMode_Type()
)
scCapIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapIpMode.setStatus("current")
_ScCapGatewayProxyArp_Type = FspR7EnableDisableCaps
_ScCapGatewayProxyArp_Object = MibTableColumn
scCapGatewayProxyArp = _ScCapGatewayProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 3, 1, 25),
    _ScCapGatewayProxyArp_Type()
)
scCapGatewayProxyArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCapGatewayProxyArp.setStatus("current")
_EndOfScCapTable_Type = Integer32
_EndOfScCapTable_Object = MibScalar
endOfScCapTable = _EndOfScCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 4),
    _EndOfScCapTable_Type()
)
endOfScCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfScCapTable.setStatus("current")
_LanCapTable_Object = MibTable
lanCapTable = _LanCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5)
)
if mibBuilder.loadTexts:
    lanCapTable.setStatus("current")
_LanCapEntry_Object = MibTableRow
lanCapEntry = _LanCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1)
)
lanCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    lanCapEntry.setStatus("current")
_LanCapRowStatus_Type = FspR7RowStatusCaps
_LanCapRowStatus_Object = MibTableColumn
lanCapRowStatus = _LanCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 1),
    _LanCapRowStatus_Type()
)
lanCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapRowStatus.setStatus("current")
_LanCapType_Type = FspR7InterfaceTypeCaps
_LanCapType_Object = MibTableColumn
lanCapType = _LanCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 2),
    _LanCapType_Type()
)
lanCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapType.setStatus("current")
_LanCapAdmin_Type = FspR7AdminStateCaps
_LanCapAdmin_Object = MibTableColumn
lanCapAdmin = _LanCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 3),
    _LanCapAdmin_Type()
)
lanCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapAdmin.setStatus("current")
_LanCapAlias_Type = Integer32
_LanCapAlias_Object = MibTableColumn
lanCapAlias = _LanCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 4),
    _LanCapAlias_Type()
)
lanCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapAlias.setStatus("current")
_LanCapAuthString_Type = Integer32
_LanCapAuthString_Object = MibTableColumn
lanCapAuthString = _LanCapAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 5),
    _LanCapAuthString_Type()
)
lanCapAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapAuthString.setStatus("current")
_LanCapOspf_Type = FspR7OspfModeCaps
_LanCapOspf_Object = MibTableColumn
lanCapOspf = _LanCapOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 6),
    _LanCapOspf_Type()
)
lanCapOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapOspf.setStatus("current")
_LanCapAuthType_Type = FspR7CpAuthTypeCaps
_LanCapAuthType_Object = MibTableColumn
lanCapAuthType = _LanCapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 7),
    _LanCapAuthType_Type()
)
lanCapAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapAuthType.setStatus("current")
_LanCapIpType_Type = FspR7IpTypeCaps
_LanCapIpType_Object = MibTableColumn
lanCapIpType = _LanCapIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 8),
    _LanCapIpType_Type()
)
lanCapIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIpType.setStatus("current")
_LanCapMetric_Type = FspR7Unsigned32Caps
_LanCapMetric_Object = MibTableColumn
lanCapMetric = _LanCapMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 9),
    _LanCapMetric_Type()
)
lanCapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapMetric.setStatus("current")
_LanCapAreaAid_Type = SnmpAdminString
_LanCapAreaAid_Object = MibTableColumn
lanCapAreaAid = _LanCapAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 10),
    _LanCapAreaAid_Type()
)
lanCapAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapAreaAid.setStatus("current")
_LanCapIpAddr_Type = FspR7YesNo
_LanCapIpAddr_Object = MibTableColumn
lanCapIpAddr = _LanCapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 11),
    _LanCapIpAddr_Type()
)
lanCapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIpAddr.setStatus("current")
_LanCapIpMask_Type = FspR7YesNo
_LanCapIpMask_Object = MibTableColumn
lanCapIpMask = _LanCapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 12),
    _LanCapIpMask_Type()
)
lanCapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIpMask.setStatus("current")
_LanCapPriority_Type = FspR7Unsigned32Caps
_LanCapPriority_Object = MibTableColumn
lanCapPriority = _LanCapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 13),
    _LanCapPriority_Type()
)
lanCapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapPriority.setStatus("current")
_LanCapIPv6_Type = FspR7YesNo
_LanCapIPv6_Object = MibTableColumn
lanCapIPv6 = _LanCapIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 14),
    _LanCapIPv6_Type()
)
lanCapIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIPv6.setStatus("current")
_LanCapIPv6PrefixLen_Type = FspR7Unsigned32Caps
_LanCapIPv6PrefixLen_Object = MibTableColumn
lanCapIPv6PrefixLen = _LanCapIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 15),
    _LanCapIPv6PrefixLen_Type()
)
lanCapIPv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIPv6PrefixLen.setStatus("current")
_LanCapIpMode_Type = FspR7IpModeCaps
_LanCapIpMode_Object = MibTableColumn
lanCapIpMode = _LanCapIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 5, 1, 16),
    _LanCapIpMode_Type()
)
lanCapIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCapIpMode.setStatus("current")
_EndOfLanCapTable_Type = Integer32
_EndOfLanCapTable_Object = MibScalar
endOfLanCapTable = _EndOfLanCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 6),
    _EndOfLanCapTable_Type()
)
endOfLanCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfLanCapTable.setStatus("current")
_EccCapTable_Object = MibTable
eccCapTable = _EccCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7)
)
if mibBuilder.loadTexts:
    eccCapTable.setStatus("current")
_EccCapEntry_Object = MibTableRow
eccCapEntry = _EccCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1)
)
eccCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    eccCapEntry.setStatus("current")
_EccCapRowStatus_Type = FspR7RowStatusCaps
_EccCapRowStatus_Object = MibTableColumn
eccCapRowStatus = _EccCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 1),
    _EccCapRowStatus_Type()
)
eccCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapRowStatus.setStatus("current")
_EccCapType_Type = FspR7InterfaceTypeCaps
_EccCapType_Object = MibTableColumn
eccCapType = _EccCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 2),
    _EccCapType_Type()
)
eccCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapType.setStatus("current")
_EccCapAdmin_Type = FspR7AdminStateCaps
_EccCapAdmin_Object = MibTableColumn
eccCapAdmin = _EccCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 3),
    _EccCapAdmin_Type()
)
eccCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapAdmin.setStatus("current")
_EccCapAlias_Type = Integer32
_EccCapAlias_Object = MibTableColumn
eccCapAlias = _EccCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 4),
    _EccCapAlias_Type()
)
eccCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapAlias.setStatus("current")
_EccCapLanAid_Type = SnmpAdminString
_EccCapLanAid_Object = MibTableColumn
eccCapLanAid = _EccCapLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 5),
    _EccCapLanAid_Type()
)
eccCapLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapLanAid.setStatus("current")
_EccCapExternalVid_Type = Unsigned32
_EccCapExternalVid_Object = MibTableColumn
eccCapExternalVid = _EccCapExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 7, 1, 6),
    _EccCapExternalVid_Type()
)
eccCapExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccCapExternalVid.setStatus("current")
_EndOfEccCapTable_Type = Integer32
_EndOfEccCapTable_Object = MibScalar
endOfEccCapTable = _EndOfEccCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 8),
    _EndOfEccCapTable_Type()
)
endOfEccCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEccCapTable.setStatus("current")
_EndOfDcnMgmtCap_Type = Integer32
_EndOfDcnMgmtCap_Object = MibScalar
endOfDcnMgmtCap = _EndOfDcnMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 5, 10000),
    _EndOfDcnMgmtCap_Type()
)
endOfDcnMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfDcnMgmtCap.setStatus("current")
_OpticalMuxMgmtCap_ObjectIdentity = ObjectIdentity
opticalMuxMgmtCap = _OpticalMuxMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6)
)
_OpticalMuxCapTable_Object = MibTable
opticalMuxCapTable = _OpticalMuxCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1)
)
if mibBuilder.loadTexts:
    opticalMuxCapTable.setStatus("current")
_OpticalMuxCapEntry_Object = MibTableRow
opticalMuxCapEntry = _OpticalMuxCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1)
)
opticalMuxCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxClassName"),
)
if mibBuilder.loadTexts:
    opticalMuxCapEntry.setStatus("current")
_OpticalMuxCapRowStatus_Type = FspR7RowStatusCaps
_OpticalMuxCapRowStatus_Object = MibTableColumn
opticalMuxCapRowStatus = _OpticalMuxCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 1),
    _OpticalMuxCapRowStatus_Type()
)
opticalMuxCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapRowStatus.setStatus("current")
_OpticalMuxCapPumpPower_Type = FspR7Integer32Caps
_OpticalMuxCapPumpPower_Object = MibTableColumn
opticalMuxCapPumpPower = _OpticalMuxCapPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 2),
    _OpticalMuxCapPumpPower_Type()
)
opticalMuxCapPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapPumpPower.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapPumpPower.setUnits("0.2 dBm")
_OpticalMuxCapInhibitSwitchToWork_Type = FspR7YesNoCaps
_OpticalMuxCapInhibitSwitchToWork_Object = MibTableColumn
opticalMuxCapInhibitSwitchToWork = _OpticalMuxCapInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 3),
    _OpticalMuxCapInhibitSwitchToWork_Type()
)
opticalMuxCapInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapInhibitSwitchToWork.setStatus("current")
_OpticalMuxCapForceLaserOn_Type = FspR7LaserForcedOperationCaps
_OpticalMuxCapForceLaserOn_Object = MibTableColumn
opticalMuxCapForceLaserOn = _OpticalMuxCapForceLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 4),
    _OpticalMuxCapForceLaserOn_Type()
)
opticalMuxCapForceLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapForceLaserOn.setStatus("current")
_OpticalMuxCapAseTabCreation_Type = FspR7AseTabOprCaps
_OpticalMuxCapAseTabCreation_Object = MibTableColumn
opticalMuxCapAseTabCreation = _OpticalMuxCapAseTabCreation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 5),
    _OpticalMuxCapAseTabCreation_Type()
)
opticalMuxCapAseTabCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapAseTabCreation.setStatus("current")
_OpticalMuxCapOpticalSetPoint_Type = FspR7Integer32Caps
_OpticalMuxCapOpticalSetPoint_Object = MibTableColumn
opticalMuxCapOpticalSetPoint = _OpticalMuxCapOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 6),
    _OpticalMuxCapOpticalSetPoint_Type()
)
opticalMuxCapOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapOpticalSetPoint.setUnits("0.1 dBm")
_OpticalMuxCapInitiateEqualization_Type = FspR7InitEqualizationCaps
_OpticalMuxCapInitiateEqualization_Object = MibTableColumn
opticalMuxCapInitiateEqualization = _OpticalMuxCapInitiateEqualization_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 7),
    _OpticalMuxCapInitiateEqualization_Type()
)
opticalMuxCapInitiateEqualization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapInitiateEqualization.setStatus("current")
_OpticalMuxCapTilt_Type = FspR7Integer32Caps
_OpticalMuxCapTilt_Object = MibTableColumn
opticalMuxCapTilt = _OpticalMuxCapTilt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 8),
    _OpticalMuxCapTilt_Type()
)
opticalMuxCapTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapTilt.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapTilt.setUnits("0.1 dB")
_OpticalMuxCapOscOpticalSetpoint_Type = FspR7Integer32Caps
_OpticalMuxCapOscOpticalSetpoint_Object = MibTableColumn
opticalMuxCapOscOpticalSetpoint = _OpticalMuxCapOscOpticalSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 9),
    _OpticalMuxCapOscOpticalSetpoint_Type()
)
opticalMuxCapOscOpticalSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOscOpticalSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapOscOpticalSetpoint.setUnits("0.1 dBm")
_OpticalMuxCapOffset_Type = FspR7Integer32Caps
_OpticalMuxCapOffset_Object = MibTableColumn
opticalMuxCapOffset = _OpticalMuxCapOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 10),
    _OpticalMuxCapOffset_Type()
)
opticalMuxCapOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOffset.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapOffset.setUnits("0.1 dB")
_OpticalMuxCapSwitchCommand_Type = FspR7APSCommandCaps
_OpticalMuxCapSwitchCommand_Object = MibTableColumn
opticalMuxCapSwitchCommand = _OpticalMuxCapSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 11),
    _OpticalMuxCapSwitchCommand_Type()
)
opticalMuxCapSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapSwitchCommand.setStatus("current")
_OpticalMuxCapAlsMode_Type = FspR7AlsModeCaps
_OpticalMuxCapAlsMode_Object = MibTableColumn
opticalMuxCapAlsMode = _OpticalMuxCapAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 12),
    _OpticalMuxCapAlsMode_Type()
)
opticalMuxCapAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapAlsMode.setStatus("current")
_OpticalMuxCapType_Type = FspR7InterfaceTypeCaps
_OpticalMuxCapType_Object = MibTableColumn
opticalMuxCapType = _OpticalMuxCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 13),
    _OpticalMuxCapType_Type()
)
opticalMuxCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapType.setStatus("current")
_OpticalMuxCapAttenuationGradient_Type = FspR7Unsigned32Caps
_OpticalMuxCapAttenuationGradient_Object = MibTableColumn
opticalMuxCapAttenuationGradient = _OpticalMuxCapAttenuationGradient_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 14),
    _OpticalMuxCapAttenuationGradient_Type()
)
opticalMuxCapAttenuationGradient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapAttenuationGradient.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapAttenuationGradient.setUnits("0.1 dB/min")
_OpticalMuxCapInhibitSwitchToProt_Type = FspR7YesNoCaps
_OpticalMuxCapInhibitSwitchToProt_Object = MibTableColumn
opticalMuxCapInhibitSwitchToProt = _OpticalMuxCapInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 15),
    _OpticalMuxCapInhibitSwitchToProt_Type()
)
opticalMuxCapInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapInhibitSwitchToProt.setStatus("current")
_OpticalMuxCapVariableGain_Type = FspR7Unsigned32Caps
_OpticalMuxCapVariableGain_Object = MibTableColumn
opticalMuxCapVariableGain = _OpticalMuxCapVariableGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 16),
    _OpticalMuxCapVariableGain_Type()
)
opticalMuxCapVariableGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapVariableGain.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapVariableGain.setUnits("0.1 dB")
_OpticalMuxCapAdmin_Type = FspR7AdminStateCaps
_OpticalMuxCapAdmin_Object = MibTableColumn
opticalMuxCapAdmin = _OpticalMuxCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 17),
    _OpticalMuxCapAdmin_Type()
)
opticalMuxCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapAdmin.setStatus("current")
_OpticalMuxCapTimePeriod_Type = FspR7OtdrPeriodCaps
_OpticalMuxCapTimePeriod_Object = MibTableColumn
opticalMuxCapTimePeriod = _OpticalMuxCapTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 18),
    _OpticalMuxCapTimePeriod_Type()
)
opticalMuxCapTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapTimePeriod.setStatus("current")
_OpticalMuxCapSigDegThresReceiver_Type = FspR7Unsigned32Caps
_OpticalMuxCapSigDegThresReceiver_Object = MibTableColumn
opticalMuxCapSigDegThresReceiver = _OpticalMuxCapSigDegThresReceiver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 19),
    _OpticalMuxCapSigDegThresReceiver_Type()
)
opticalMuxCapSigDegThresReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapSigDegThresReceiver.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapSigDegThresReceiver.setUnits("0.1 dB")
_OpticalMuxCapAlias_Type = Integer32
_OpticalMuxCapAlias_Object = MibTableColumn
opticalMuxCapAlias = _OpticalMuxCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 20),
    _OpticalMuxCapAlias_Type()
)
opticalMuxCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapAlias.setStatus("current")
_OpticalMuxCapDataLayerPmReset_Type = FspR7PmResetCaps
_OpticalMuxCapDataLayerPmReset_Object = MibTableColumn
opticalMuxCapDataLayerPmReset = _OpticalMuxCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 21),
    _OpticalMuxCapDataLayerPmReset_Type()
)
opticalMuxCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapDataLayerPmReset.setStatus("current")
_OpticalMuxCapGain_Type = FspR7GainCaps
_OpticalMuxCapGain_Object = MibTableColumn
opticalMuxCapGain = _OpticalMuxCapGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 22),
    _OpticalMuxCapGain_Type()
)
opticalMuxCapGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapGain.setStatus("current")
_OpticalMuxCapEdfaPwrOut_Type = FspR7EdfaOutputPowerRatingCaps
_OpticalMuxCapEdfaPwrOut_Object = MibTableColumn
opticalMuxCapEdfaPwrOut = _OpticalMuxCapEdfaPwrOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 23),
    _OpticalMuxCapEdfaPwrOut_Type()
)
opticalMuxCapEdfaPwrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapEdfaPwrOut.setStatus("current")
_OpticalMuxCapVoaSetpoint_Type = FspR7Unsigned32Caps
_OpticalMuxCapVoaSetpoint_Object = MibTableColumn
opticalMuxCapVoaSetpoint = _OpticalMuxCapVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 24),
    _OpticalMuxCapVoaSetpoint_Type()
)
opticalMuxCapVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapVoaSetpoint.setUnits("0.1 dB")
_OpticalMuxCapFiberBrand_Type = FspR7FiberBrandCaps
_OpticalMuxCapFiberBrand_Object = MibTableColumn
opticalMuxCapFiberBrand = _OpticalMuxCapFiberBrand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 25),
    _OpticalMuxCapFiberBrand_Type()
)
opticalMuxCapFiberBrand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapFiberBrand.setStatus("current")
_OpticalMuxCapTiltSet_Type = FspR7TiltSetCaps
_OpticalMuxCapTiltSet_Object = MibTableColumn
opticalMuxCapTiltSet = _OpticalMuxCapTiltSet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 26),
    _OpticalMuxCapTiltSet_Type()
)
opticalMuxCapTiltSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapTiltSet.setStatus("current")
_OpticalMuxCapForceFwdAsePilotOn_Type = FspR7LaserForcedOperationCaps
_OpticalMuxCapForceFwdAsePilotOn_Object = MibTableColumn
opticalMuxCapForceFwdAsePilotOn = _OpticalMuxCapForceFwdAsePilotOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 27),
    _OpticalMuxCapForceFwdAsePilotOn_Type()
)
opticalMuxCapForceFwdAsePilotOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapForceFwdAsePilotOn.setStatus("current")
_OpticalMuxCapBandProvision_Type = FspR7OpticalBandCaps
_OpticalMuxCapBandProvision_Object = MibTableColumn
opticalMuxCapBandProvision = _OpticalMuxCapBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 28),
    _OpticalMuxCapBandProvision_Type()
)
opticalMuxCapBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapBandProvision.setStatus("current")
_OpticalMuxCapOffsetHigh_Type = FspR7Integer32Caps
_OpticalMuxCapOffsetHigh_Object = MibTableColumn
opticalMuxCapOffsetHigh = _OpticalMuxCapOffsetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 29),
    _OpticalMuxCapOffsetHigh_Type()
)
opticalMuxCapOffsetHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOffsetHigh.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapOffsetHigh.setUnits("0.1 dBm")
_OpticalMuxCapOffsetLow_Type = FspR7Integer32Caps
_OpticalMuxCapOffsetLow_Object = MibTableColumn
opticalMuxCapOffsetLow = _OpticalMuxCapOffsetLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 30),
    _OpticalMuxCapOffsetLow_Type()
)
opticalMuxCapOffsetLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOffsetLow.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxCapOffsetLow.setUnits("0.1 dBm")
_OpticalMuxCapOptUpdate_Type = FspR7OptUpdateCaps
_OpticalMuxCapOptUpdate_Object = MibTableColumn
opticalMuxCapOptUpdate = _OpticalMuxCapOptUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 1, 1, 31),
    _OpticalMuxCapOptUpdate_Type()
)
opticalMuxCapOptUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxCapOptUpdate.setStatus("current")
_EndOfOpticalMuxCapTable_Type = Integer32
_EndOfOpticalMuxCapTable_Object = MibScalar
endOfOpticalMuxCapTable = _EndOfOpticalMuxCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 2),
    _EndOfOpticalMuxCapTable_Type()
)
endOfOpticalMuxCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalMuxCapTable.setStatus("current")
_EndOfOpticalMuxMgmtCap_Type = Integer32
_EndOfOpticalMuxMgmtCap_Object = MibScalar
endOfOpticalMuxMgmtCap = _EndOfOpticalMuxMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 6, 10000),
    _EndOfOpticalMuxMgmtCap_Type()
)
endOfOpticalMuxMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalMuxMgmtCap.setStatus("current")
_ShelfConnMgmtCap_ObjectIdentity = ObjectIdentity
shelfConnMgmtCap = _ShelfConnMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7)
)
_ShelfConnCapTable_Object = MibTable
shelfConnCapTable = _ShelfConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1)
)
if mibBuilder.loadTexts:
    shelfConnCapTable.setStatus("current")
_ShelfConnCapEntry_Object = MibTableRow
shelfConnCapEntry = _ShelfConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1, 1)
)
shelfConnCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityShelfConnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnClassName"),
)
if mibBuilder.loadTexts:
    shelfConnCapEntry.setStatus("current")
_ShelfConnCapRowStatus_Type = FspR7RowStatusCaps
_ShelfConnCapRowStatus_Object = MibTableColumn
shelfConnCapRowStatus = _ShelfConnCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1, 1, 1),
    _ShelfConnCapRowStatus_Type()
)
shelfConnCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnCapRowStatus.setStatus("current")
_ShelfConnCapAdmin_Type = FspR7AdminStateCaps
_ShelfConnCapAdmin_Object = MibTableColumn
shelfConnCapAdmin = _ShelfConnCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1, 1, 2),
    _ShelfConnCapAdmin_Type()
)
shelfConnCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnCapAdmin.setStatus("current")
_ShelfConnCapAlias_Type = Integer32
_ShelfConnCapAlias_Object = MibTableColumn
shelfConnCapAlias = _ShelfConnCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1, 1, 3),
    _ShelfConnCapAlias_Type()
)
shelfConnCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnCapAlias.setStatus("current")
_ShelfConnCapFacilityType_Type = FspR7InterfaceTypeCaps
_ShelfConnCapFacilityType_Object = MibTableColumn
shelfConnCapFacilityType = _ShelfConnCapFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 1, 1, 4),
    _ShelfConnCapFacilityType_Type()
)
shelfConnCapFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnCapFacilityType.setStatus("current")
_EndOfShelfConnCapTable_Type = Integer32
_EndOfShelfConnCapTable_Object = MibScalar
endOfShelfConnCapTable = _EndOfShelfConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 2),
    _EndOfShelfConnCapTable_Type()
)
endOfShelfConnCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfConnCapTable.setStatus("current")
_EndOfShelfConnMgmtCap_Type = Integer32
_EndOfShelfConnMgmtCap_Object = MibScalar
endOfShelfConnMgmtCap = _EndOfShelfConnMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 7, 10000),
    _EndOfShelfConnMgmtCap_Type()
)
endOfShelfConnMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfConnMgmtCap.setStatus("current")
_EnvMgmtCap_ObjectIdentity = ObjectIdentity
envMgmtCap = _EnvMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8)
)
_EnvPortCapTable_Object = MibTable
envPortCapTable = _EnvPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1)
)
if mibBuilder.loadTexts:
    envPortCapTable.setStatus("current")
_EnvPortCapEntry_Object = MibTableRow
envPortCapEntry = _EnvPortCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1)
)
envPortCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    envPortCapEntry.setStatus("current")
_EnvPortCapRowStatus_Type = FspR7RowStatusCaps
_EnvPortCapRowStatus_Object = MibTableColumn
envPortCapRowStatus = _EnvPortCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 1),
    _EnvPortCapRowStatus_Type()
)
envPortCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapRowStatus.setStatus("current")
_EnvPortCapTelemetry_Type = FspR7TelemetryOutputCaps
_EnvPortCapTelemetry_Object = MibTableColumn
envPortCapTelemetry = _EnvPortCapTelemetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 2),
    _EnvPortCapTelemetry_Type()
)
envPortCapTelemetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapTelemetry.setStatus("current")
_EnvPortCapFacilityType_Type = FspR7InterfaceTypeCaps
_EnvPortCapFacilityType_Object = MibTableColumn
envPortCapFacilityType = _EnvPortCapFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 3),
    _EnvPortCapFacilityType_Type()
)
envPortCapFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapFacilityType.setStatus("current")
_EnvPortCapTifAlarmType_Type = Integer32
_EnvPortCapTifAlarmType_Object = MibTableColumn
envPortCapTifAlarmType = _EnvPortCapTifAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 4),
    _EnvPortCapTifAlarmType_Type()
)
envPortCapTifAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapTifAlarmType.setStatus("current")
_EnvPortCapTifAlarmMessage_Type = Integer32
_EnvPortCapTifAlarmMessage_Object = MibTableColumn
envPortCapTifAlarmMessage = _EnvPortCapTifAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 5),
    _EnvPortCapTifAlarmMessage_Type()
)
envPortCapTifAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapTifAlarmMessage.setStatus("current")
_EnvPortCapInvertTifInputLogic_Type = FspR7InvertTelemetryInputLogicCaps
_EnvPortCapInvertTifInputLogic_Object = MibTableColumn
envPortCapInvertTifInputLogic = _EnvPortCapInvertTifInputLogic_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 1, 1, 6),
    _EnvPortCapInvertTifInputLogic_Type()
)
envPortCapInvertTifInputLogic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortCapInvertTifInputLogic.setStatus("current")
_EndOfEnvPortCapTable_Type = Integer32
_EndOfEnvPortCapTable_Object = MibScalar
endOfEnvPortCapTable = _EndOfEnvPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 2),
    _EndOfEnvPortCapTable_Type()
)
endOfEnvPortCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEnvPortCapTable.setStatus("current")
_EndOfEnvMgmtCap_Type = Integer32
_EndOfEnvMgmtCap_Object = MibScalar
endOfEnvMgmtCap = _EndOfEnvMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 8, 10000),
    _EndOfEnvMgmtCap_Type()
)
endOfEnvMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEnvMgmtCap.setStatus("current")
_ContainerMgmtCap_ObjectIdentity = ObjectIdentity
containerMgmtCap = _ContainerMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9)
)
_ContainerCapTable_Object = MibTable
containerCapTable = _ContainerCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 1)
)
if mibBuilder.loadTexts:
    containerCapTable.setStatus("current")
_ContainerCapEntry_Object = MibTableRow
containerCapEntry = _ContainerCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 1, 1)
)
containerCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityContainerShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerClassName"),
)
if mibBuilder.loadTexts:
    containerCapEntry.setStatus("current")
_ContainerCapRowStatus_Type = FspR7RowStatusCaps
_ContainerCapRowStatus_Object = MibTableColumn
containerCapRowStatus = _ContainerCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 1, 1, 1),
    _ContainerCapRowStatus_Type()
)
containerCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerCapRowStatus.setStatus("current")
_ContainerCapFacilityType_Type = FspR7InterfaceTypeCaps
_ContainerCapFacilityType_Object = MibTableColumn
containerCapFacilityType = _ContainerCapFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 1, 1, 2),
    _ContainerCapFacilityType_Type()
)
containerCapFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerCapFacilityType.setStatus("current")
_EndOfContainerCapTable_Type = Integer32
_EndOfContainerCapTable_Object = MibScalar
endOfContainerCapTable = _EndOfContainerCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 2),
    _EndOfContainerCapTable_Type()
)
endOfContainerCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfContainerCapTable.setStatus("current")
_EndOfContainerMgmtCap_Type = Integer32
_EndOfContainerMgmtCap_Object = MibScalar
endOfContainerMgmtCap = _EndOfContainerMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 9, 10000),
    _EndOfContainerMgmtCap_Type()
)
endOfContainerMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfContainerMgmtCap.setStatus("current")
_OpticalLineMgmtCap_ObjectIdentity = ObjectIdentity
opticalLineMgmtCap = _OpticalLineMgmtCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10)
)
_OpticalLineCapTable_Object = MibTable
opticalLineCapTable = _OpticalLineCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1)
)
if mibBuilder.loadTexts:
    opticalLineCapTable.setStatus("current")
_OpticalLineCapEntry_Object = MibTableRow
opticalLineCapEntry = _OpticalLineCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1)
)
opticalLineCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineClassName"),
)
if mibBuilder.loadTexts:
    opticalLineCapEntry.setStatus("current")
_OpticalLineCapRowStatus_Type = FspR7RowStatusCaps
_OpticalLineCapRowStatus_Object = MibTableColumn
opticalLineCapRowStatus = _OpticalLineCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1, 1),
    _OpticalLineCapRowStatus_Type()
)
opticalLineCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineCapRowStatus.setStatus("current")
_OpticalLineCapTxLineAttenuation_Type = FspR7Integer32Caps
_OpticalLineCapTxLineAttenuation_Object = MibTableColumn
opticalLineCapTxLineAttenuation = _OpticalLineCapTxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1, 2),
    _OpticalLineCapTxLineAttenuation_Type()
)
opticalLineCapTxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineCapTxLineAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    opticalLineCapTxLineAttenuation.setUnits("0.1 dB")
_OpticalLineCapRxLineAttenuation_Type = FspR7Integer32Caps
_OpticalLineCapRxLineAttenuation_Object = MibTableColumn
opticalLineCapRxLineAttenuation = _OpticalLineCapRxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1, 3),
    _OpticalLineCapRxLineAttenuation_Type()
)
opticalLineCapRxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineCapRxLineAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    opticalLineCapRxLineAttenuation.setUnits("0.1 dB")
_OpticalLineCapAlias_Type = Integer32
_OpticalLineCapAlias_Object = MibTableColumn
opticalLineCapAlias = _OpticalLineCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1, 4),
    _OpticalLineCapAlias_Type()
)
opticalLineCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineCapAlias.setStatus("current")
_OpticalLineCapFarEndLocation_Type = Integer32
_OpticalLineCapFarEndLocation_Object = MibTableColumn
opticalLineCapFarEndLocation = _OpticalLineCapFarEndLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 1, 1, 5),
    _OpticalLineCapFarEndLocation_Type()
)
opticalLineCapFarEndLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineCapFarEndLocation.setStatus("current")
_EndOfOpticalLineCapTable_Type = Integer32
_EndOfOpticalLineCapTable_Object = MibScalar
endOfOpticalLineCapTable = _EndOfOpticalLineCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 2),
    _EndOfOpticalLineCapTable_Type()
)
endOfOpticalLineCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalLineCapTable.setStatus("current")
_EndOfOpticalLineMgmtCap_Type = Integer32
_EndOfOpticalLineMgmtCap_Object = MibScalar
endOfOpticalLineMgmtCap = _EndOfOpticalLineMgmtCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10, 10000),
    _EndOfOpticalLineMgmtCap_Type()
)
endOfOpticalLineMgmtCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalLineMgmtCap.setStatus("current")
_EndOfManagementCap_Type = Integer32
_EndOfManagementCap_Object = MibScalar
endOfManagementCap = _EndOfManagementCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 3, 10000),
    _EndOfManagementCap_Type()
)
endOfManagementCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfManagementCap.setStatus("current")
_PerformanceCap_ObjectIdentity = ObjectIdentity
performanceCap = _PerformanceCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6)
)
_PerformanceFacilityCap_ObjectIdentity = ObjectIdentity
performanceFacilityCap = _PerformanceFacilityCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4)
)
_PerformanceFacilityThresholdCap_ObjectIdentity = ObjectIdentity
performanceFacilityThresholdCap = _PerformanceFacilityThresholdCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1)
)
_OptThresholdConfigCapTable_Object = MibTable
optThresholdConfigCapTable = _OptThresholdConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    optThresholdConfigCapTable.setStatus("current")
_OptThresholdConfigCapEntry_Object = MibTableRow
optThresholdConfigCapEntry = _OptThresholdConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 1, 1)
)
optThresholdConfigCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    optThresholdConfigCapEntry.setStatus("current")
_OptThresholdConfigCapLowConfig_Type = FspR7Integer32Caps
_OptThresholdConfigCapLowConfig_Object = MibTableColumn
optThresholdConfigCapLowConfig = _OptThresholdConfigCapLowConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 1, 1, 1),
    _OptThresholdConfigCapLowConfig_Type()
)
optThresholdConfigCapLowConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optThresholdConfigCapLowConfig.setStatus("current")
if mibBuilder.loadTexts:
    optThresholdConfigCapLowConfig.setUnits("0.1 dBm")
_OptThresholdConfigCapHighConfig_Type = FspR7Integer32Caps
_OptThresholdConfigCapHighConfig_Object = MibTableColumn
optThresholdConfigCapHighConfig = _OptThresholdConfigCapHighConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 1, 1, 2),
    _OptThresholdConfigCapHighConfig_Type()
)
optThresholdConfigCapHighConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optThresholdConfigCapHighConfig.setStatus("current")
if mibBuilder.loadTexts:
    optThresholdConfigCapHighConfig.setUnits("0.1 dBm")
_OprThresholdConfigCapTable_Object = MibTable
oprThresholdConfigCapTable = _OprThresholdConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    oprThresholdConfigCapTable.setStatus("current")
_OprThresholdConfigCapEntry_Object = MibTableRow
oprThresholdConfigCapEntry = _OprThresholdConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 2, 1)
)
oprThresholdConfigCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    oprThresholdConfigCapEntry.setStatus("current")
_OprThresholdConfigCapLowConfig_Type = FspR7Integer32Caps
_OprThresholdConfigCapLowConfig_Object = MibTableColumn
oprThresholdConfigCapLowConfig = _OprThresholdConfigCapLowConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 2, 1, 1),
    _OprThresholdConfigCapLowConfig_Type()
)
oprThresholdConfigCapLowConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oprThresholdConfigCapLowConfig.setStatus("current")
if mibBuilder.loadTexts:
    oprThresholdConfigCapLowConfig.setUnits("0.1 dBm")
_OprThresholdConfigCapHighConfig_Type = FspR7Integer32Caps
_OprThresholdConfigCapHighConfig_Object = MibTableColumn
oprThresholdConfigCapHighConfig = _OprThresholdConfigCapHighConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 2, 1, 2),
    _OprThresholdConfigCapHighConfig_Type()
)
oprThresholdConfigCapHighConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oprThresholdConfigCapHighConfig.setStatus("current")
if mibBuilder.loadTexts:
    oprThresholdConfigCapHighConfig.setUnits("0.1 dBm")
_EndOfOprThresholdConfigCapTable_Type = Integer32
_EndOfOprThresholdConfigCapTable_Object = MibScalar
endOfOprThresholdConfigCapTable = _EndOfOprThresholdConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 3),
    _EndOfOprThresholdConfigCapTable_Type()
)
endOfOprThresholdConfigCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOprThresholdConfigCapTable.setStatus("current")
_EndOfPerformanceFacilityThresholdCap_Type = Integer32
_EndOfPerformanceFacilityThresholdCap_Object = MibScalar
endOfPerformanceFacilityThresholdCap = _EndOfPerformanceFacilityThresholdCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 1, 10000),
    _EndOfPerformanceFacilityThresholdCap_Type()
)
endOfPerformanceFacilityThresholdCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPerformanceFacilityThresholdCap.setStatus("current")
_EndOfPerformanceFacilityCap_Type = Integer32
_EndOfPerformanceFacilityCap_Object = MibScalar
endOfPerformanceFacilityCap = _EndOfPerformanceFacilityCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 4, 10000),
    _EndOfPerformanceFacilityCap_Type()
)
endOfPerformanceFacilityCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPerformanceFacilityCap.setStatus("current")
_PmEqptCap_ObjectIdentity = ObjectIdentity
pmEqptCap = _PmEqptCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 10)
)
_PmDcnCap_ObjectIdentity = ObjectIdentity
pmDcnCap = _PmDcnCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11)
)
_PmDcnDataCap_ObjectIdentity = ObjectIdentity
pmDcnDataCap = _PmDcnDataCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 1)
)
_PmDcnPhysicalCap_ObjectIdentity = ObjectIdentity
pmDcnPhysicalCap = _PmDcnPhysicalCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2)
)
_PmDcnPhysThresholdCap_ObjectIdentity = ObjectIdentity
pmDcnPhysThresholdCap = _PmDcnPhysThresholdCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2)
)
_DcnPhysThresholdCapTable_Object = MibTable
dcnPhysThresholdCapTable = _DcnPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcnPhysThresholdCapTable.setStatus("current")
_DcnPhysThresholdCapEntry_Object = MibTableRow
dcnPhysThresholdCapEntry = _DcnPhysThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1, 1)
)
dcnPhysThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    dcnPhysThresholdCapEntry.setStatus("current")
_DcnPhysThresholdCapOprLow_Type = FspR7Integer32Caps
_DcnPhysThresholdCapOprLow_Object = MibTableColumn
dcnPhysThresholdCapOprLow = _DcnPhysThresholdCapOprLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1, 1, 1),
    _DcnPhysThresholdCapOprLow_Type()
)
dcnPhysThresholdCapOprLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapOprLow.setStatus("current")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapOprLow.setUnits("0.1 dBm")
_DcnPhysThresholdCapOprHigh_Type = FspR7Integer32Caps
_DcnPhysThresholdCapOprHigh_Object = MibTableColumn
dcnPhysThresholdCapOprHigh = _DcnPhysThresholdCapOprHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1, 1, 2),
    _DcnPhysThresholdCapOprHigh_Type()
)
dcnPhysThresholdCapOprHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapOprHigh.setStatus("current")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapOprHigh.setUnits("0.1 dBm")
_DcnPhysThresholdCapAttRcvLow_Type = FspR7Integer32Caps
_DcnPhysThresholdCapAttRcvLow_Object = MibTableColumn
dcnPhysThresholdCapAttRcvLow = _DcnPhysThresholdCapAttRcvLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1, 1, 3),
    _DcnPhysThresholdCapAttRcvLow_Type()
)
dcnPhysThresholdCapAttRcvLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapAttRcvLow.setStatus("current")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapAttRcvLow.setUnits("0.1 dB")
_DcnPhysThresholdCapAttRcvHigh_Type = FspR7Integer32Caps
_DcnPhysThresholdCapAttRcvHigh_Object = MibTableColumn
dcnPhysThresholdCapAttRcvHigh = _DcnPhysThresholdCapAttRcvHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 1, 1, 4),
    _DcnPhysThresholdCapAttRcvHigh_Type()
)
dcnPhysThresholdCapAttRcvHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapAttRcvHigh.setStatus("current")
if mibBuilder.loadTexts:
    dcnPhysThresholdCapAttRcvHigh.setUnits("0.1 dB")
_EndOfDcnPhysThresholdCapTable_Type = Integer32
_EndOfDcnPhysThresholdCapTable_Object = MibScalar
endOfDcnPhysThresholdCapTable = _EndOfDcnPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 2),
    _EndOfDcnPhysThresholdCapTable_Type()
)
endOfDcnPhysThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfDcnPhysThresholdCapTable.setStatus("current")
_EndOfPmDcnPhysThresholdCap_Type = Integer32
_EndOfPmDcnPhysThresholdCap_Object = MibScalar
endOfPmDcnPhysThresholdCap = _EndOfPmDcnPhysThresholdCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 2, 10000),
    _EndOfPmDcnPhysThresholdCap_Type()
)
endOfPmDcnPhysThresholdCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmDcnPhysThresholdCap.setStatus("current")
_EndOfPmDcnPhysicalCap_Type = Integer32
_EndOfPmDcnPhysicalCap_Object = MibScalar
endOfPmDcnPhysicalCap = _EndOfPmDcnPhysicalCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 2, 10000),
    _EndOfPmDcnPhysicalCap_Type()
)
endOfPmDcnPhysicalCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmDcnPhysicalCap.setStatus("current")
_EndOfPmDcnCap_Type = Integer32
_EndOfPmDcnCap_Object = MibScalar
endOfPmDcnCap = _EndOfPmDcnCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 11, 10000),
    _EndOfPmDcnCap_Type()
)
endOfPmDcnCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmDcnCap.setStatus("current")
_PmFacilityCap_ObjectIdentity = ObjectIdentity
pmFacilityCap = _PmFacilityCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12)
)
_PmFacilityDataCap_ObjectIdentity = ObjectIdentity
pmFacilityDataCap = _PmFacilityDataCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1)
)
_PmFacilityDataThresholdCap_ObjectIdentity = ObjectIdentity
pmFacilityDataThresholdCap = _PmFacilityDataThresholdCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1)
)
_OduFacilityDataThresholdCapTable_Object = MibTable
oduFacilityDataThresholdCapTable = _OduFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapTable.setStatus("current")
_OduFacilityDataThresholdCapEntry_Object = MibTableRow
oduFacilityDataThresholdCapEntry = _OduFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1)
)
oduFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapEntry.setStatus("current")
_OduFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
oduFacilityDataThresholdCapESHighThres15min = _OduFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 1),
    _OduFacilityDataThresholdCapESHighThres15min_Type()
)
oduFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapESHighThres15min.setStatus("current")
_OduFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
oduFacilityDataThresholdCapESHighThres1day = _OduFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 2),
    _OduFacilityDataThresholdCapESHighThres1day_Type()
)
oduFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapESHighThres1day.setStatus("current")
_OduFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
oduFacilityDataThresholdCapSESHighThres15min = _OduFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 3),
    _OduFacilityDataThresholdCapSESHighThres15min_Type()
)
oduFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_OduFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
oduFacilityDataThresholdCapSESHighThres1day = _OduFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 4),
    _OduFacilityDataThresholdCapSESHighThres1day_Type()
)
oduFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_OduFacilityDataThresholdCapBbeHighThres15min_Type = Counter64StringCaps
_OduFacilityDataThresholdCapBbeHighThres15min_Object = MibTableColumn
oduFacilityDataThresholdCapBbeHighThres15min = _OduFacilityDataThresholdCapBbeHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 5),
    _OduFacilityDataThresholdCapBbeHighThres15min_Type()
)
oduFacilityDataThresholdCapBbeHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapBbeHighThres15min.setStatus("current")
_OduFacilityDataThresholdCapBbeHighThres1day_Type = Counter64StringCaps
_OduFacilityDataThresholdCapBbeHighThres1day_Object = MibTableColumn
oduFacilityDataThresholdCapBbeHighThres1day = _OduFacilityDataThresholdCapBbeHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 6),
    _OduFacilityDataThresholdCapBbeHighThres1day_Type()
)
oduFacilityDataThresholdCapBbeHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapBbeHighThres1day.setStatus("current")
_OduFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
oduFacilityDataThresholdCapUASHighThres15min = _OduFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 7),
    _OduFacilityDataThresholdCapUASHighThres15min_Type()
)
oduFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_OduFacilityDataThresholdCapUASHighThres1day_Type = FspR7Unsigned32Caps
_OduFacilityDataThresholdCapUASHighThres1day_Object = MibTableColumn
oduFacilityDataThresholdCapUASHighThres1day = _OduFacilityDataThresholdCapUASHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 1, 1, 8),
    _OduFacilityDataThresholdCapUASHighThres1day_Type()
)
oduFacilityDataThresholdCapUASHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduFacilityDataThresholdCapUASHighThres1day.setStatus("current")
_EndOfOduFacilityDataThresholdCapTable_Type = Integer32
_EndOfOduFacilityDataThresholdCapTable_Object = MibScalar
endOfOduFacilityDataThresholdCapTable = _EndOfOduFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 2),
    _EndOfOduFacilityDataThresholdCapTable_Type()
)
endOfOduFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOduFacilityDataThresholdCapTable.setStatus("current")
_TcmAFacilityDataThresholdCapTable_Object = MibTable
tcmAFacilityDataThresholdCapTable = _TcmAFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapTable.setStatus("current")
_TcmAFacilityDataThresholdCapEntry_Object = MibTableRow
tcmAFacilityDataThresholdCapEntry = _TcmAFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1)
)
tcmAFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapEntry.setStatus("current")
_TcmAFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
tcmAFacilityDataThresholdCapESHighThres15min = _TcmAFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 1),
    _TcmAFacilityDataThresholdCapESHighThres15min_Type()
)
tcmAFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapESHighThres15min.setStatus("current")
_TcmAFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
tcmAFacilityDataThresholdCapESHighThres1day = _TcmAFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 2),
    _TcmAFacilityDataThresholdCapESHighThres1day_Type()
)
tcmAFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapESHighThres1day.setStatus("current")
_TcmAFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
tcmAFacilityDataThresholdCapSESHighThres15min = _TcmAFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 3),
    _TcmAFacilityDataThresholdCapSESHighThres15min_Type()
)
tcmAFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_TcmAFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
tcmAFacilityDataThresholdCapSESHighThres1day = _TcmAFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 4),
    _TcmAFacilityDataThresholdCapSESHighThres1day_Type()
)
tcmAFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_TcmAFacilityDataThresholdCapBbeHighThres15min_Type = Counter64StringCaps
_TcmAFacilityDataThresholdCapBbeHighThres15min_Object = MibTableColumn
tcmAFacilityDataThresholdCapBbeHighThres15min = _TcmAFacilityDataThresholdCapBbeHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 5),
    _TcmAFacilityDataThresholdCapBbeHighThres15min_Type()
)
tcmAFacilityDataThresholdCapBbeHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapBbeHighThres15min.setStatus("current")
_TcmAFacilityDataThresholdCapBbeHighThres1day_Type = Counter64StringCaps
_TcmAFacilityDataThresholdCapBbeHighThres1day_Object = MibTableColumn
tcmAFacilityDataThresholdCapBbeHighThres1day = _TcmAFacilityDataThresholdCapBbeHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 6),
    _TcmAFacilityDataThresholdCapBbeHighThres1day_Type()
)
tcmAFacilityDataThresholdCapBbeHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapBbeHighThres1day.setStatus("current")
_TcmAFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
tcmAFacilityDataThresholdCapUASHighThres15min = _TcmAFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 7),
    _TcmAFacilityDataThresholdCapUASHighThres15min_Type()
)
tcmAFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_TcmAFacilityDataThresholdCapUASHighThres1day_Type = FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapUASHighThres1day_Object = MibTableColumn
tcmAFacilityDataThresholdCapUASHighThres1day = _TcmAFacilityDataThresholdCapUASHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 3, 1, 8),
    _TcmAFacilityDataThresholdCapUASHighThres1day_Type()
)
tcmAFacilityDataThresholdCapUASHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmAFacilityDataThresholdCapUASHighThres1day.setStatus("current")
_EndOfTcmAFacilityDataThresholdCapTable_Type = Integer32
_EndOfTcmAFacilityDataThresholdCapTable_Object = MibScalar
endOfTcmAFacilityDataThresholdCapTable = _EndOfTcmAFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 4),
    _EndOfTcmAFacilityDataThresholdCapTable_Type()
)
endOfTcmAFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfTcmAFacilityDataThresholdCapTable.setStatus("current")
_TcmBFacilityDataThresholdCapTable_Object = MibTable
tcmBFacilityDataThresholdCapTable = _TcmBFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapTable.setStatus("current")
_TcmBFacilityDataThresholdCapEntry_Object = MibTableRow
tcmBFacilityDataThresholdCapEntry = _TcmBFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1)
)
tcmBFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapEntry.setStatus("current")
_TcmBFacilityDataThresholdCapBESHighThres15min_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapBESHighThres15min_Object = MibTableColumn
tcmBFacilityDataThresholdCapBESHighThres15min = _TcmBFacilityDataThresholdCapBESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 1),
    _TcmBFacilityDataThresholdCapBESHighThres15min_Type()
)
tcmBFacilityDataThresholdCapBESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapBESHighThres15min.setStatus("current")
_TcmBFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
tcmBFacilityDataThresholdCapESHighThres1day = _TcmBFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 2),
    _TcmBFacilityDataThresholdCapESHighThres1day_Type()
)
tcmBFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapESHighThres1day.setStatus("current")
_TcmBFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
tcmBFacilityDataThresholdCapSESHighThres15min = _TcmBFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 3),
    _TcmBFacilityDataThresholdCapSESHighThres15min_Type()
)
tcmBFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_TcmBFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
tcmBFacilityDataThresholdCapSESHighThres1day = _TcmBFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 4),
    _TcmBFacilityDataThresholdCapSESHighThres1day_Type()
)
tcmBFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Type = Counter64StringCaps
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Object = MibTableColumn
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min = _TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 5),
    _TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Type()
)
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min.setStatus("current")
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Type = Counter64StringCaps
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Object = MibTableColumn
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day = _TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 6),
    _TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Type()
)
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day.setStatus("current")
_TcmBFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
tcmBFacilityDataThresholdCapUASHighThres15min = _TcmBFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 7),
    _TcmBFacilityDataThresholdCapUASHighThres15min_Type()
)
tcmBFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_TcmBFacilityDataThresholdCapUASHighThres1day_Type = FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapUASHighThres1day_Object = MibTableColumn
tcmBFacilityDataThresholdCapUASHighThres1day = _TcmBFacilityDataThresholdCapUASHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 5, 1, 8),
    _TcmBFacilityDataThresholdCapUASHighThres1day_Type()
)
tcmBFacilityDataThresholdCapUASHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmBFacilityDataThresholdCapUASHighThres1day.setStatus("current")
_EndOfTcmBFacilityDataThresholdCapTable_Type = Integer32
_EndOfTcmBFacilityDataThresholdCapTable_Object = MibScalar
endOfTcmBFacilityDataThresholdCapTable = _EndOfTcmBFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 6),
    _EndOfTcmBFacilityDataThresholdCapTable_Type()
)
endOfTcmBFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfTcmBFacilityDataThresholdCapTable.setStatus("current")
_TcmCFacilityDataThresholdCapTable_Object = MibTable
tcmCFacilityDataThresholdCapTable = _TcmCFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapTable.setStatus("current")
_TcmCFacilityDataThresholdCapEntry_Object = MibTableRow
tcmCFacilityDataThresholdCapEntry = _TcmCFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1)
)
tcmCFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapEntry.setStatus("current")
_TcmCFacilityDataThresholdCapBESHighThres15min_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapBESHighThres15min_Object = MibTableColumn
tcmCFacilityDataThresholdCapBESHighThres15min = _TcmCFacilityDataThresholdCapBESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 1),
    _TcmCFacilityDataThresholdCapBESHighThres15min_Type()
)
tcmCFacilityDataThresholdCapBESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapBESHighThres15min.setStatus("current")
_TcmCFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
tcmCFacilityDataThresholdCapESHighThres1day = _TcmCFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 2),
    _TcmCFacilityDataThresholdCapESHighThres1day_Type()
)
tcmCFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapESHighThres1day.setStatus("current")
_TcmCFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
tcmCFacilityDataThresholdCapSESHighThres15min = _TcmCFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 3),
    _TcmCFacilityDataThresholdCapSESHighThres15min_Type()
)
tcmCFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_TcmCFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
tcmCFacilityDataThresholdCapSESHighThres1day = _TcmCFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 4),
    _TcmCFacilityDataThresholdCapSESHighThres1day_Type()
)
tcmCFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Type = Counter64StringCaps
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Object = MibTableColumn
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min = _TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 5),
    _TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Type()
)
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min.setStatus("current")
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Type = Counter64StringCaps
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Object = MibTableColumn
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day = _TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 6),
    _TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Type()
)
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day.setStatus("current")
_TcmCFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
tcmCFacilityDataThresholdCapUASHighThres15min = _TcmCFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 7),
    _TcmCFacilityDataThresholdCapUASHighThres15min_Type()
)
tcmCFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_TcmCFacilityDataThresholdCapUASHighThres1day_Type = FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapUASHighThres1day_Object = MibTableColumn
tcmCFacilityDataThresholdCapUASHighThres1day = _TcmCFacilityDataThresholdCapUASHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 7, 1, 8),
    _TcmCFacilityDataThresholdCapUASHighThres1day_Type()
)
tcmCFacilityDataThresholdCapUASHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCFacilityDataThresholdCapUASHighThres1day.setStatus("current")
_EndOfTcmCFacilityDataThresholdCapTable_Type = Integer32
_EndOfTcmCFacilityDataThresholdCapTable_Object = MibScalar
endOfTcmCFacilityDataThresholdCapTable = _EndOfTcmCFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 8),
    _EndOfTcmCFacilityDataThresholdCapTable_Type()
)
endOfTcmCFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfTcmCFacilityDataThresholdCapTable.setStatus("current")
_OtuFacilityDataThresholdCapTable_Object = MibTable
otuFacilityDataThresholdCapTable = _OtuFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9)
)
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapTable.setStatus("current")
_OtuFacilityDataThresholdCapEntry_Object = MibTableRow
otuFacilityDataThresholdCapEntry = _OtuFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1)
)
otuFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapEntry.setStatus("current")
_OtuFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
otuFacilityDataThresholdCapESHighThres15min = _OtuFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 1),
    _OtuFacilityDataThresholdCapESHighThres15min_Type()
)
otuFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapESHighThres15min.setStatus("current")
_OtuFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
otuFacilityDataThresholdCapESHighThres1day = _OtuFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 2),
    _OtuFacilityDataThresholdCapESHighThres1day_Type()
)
otuFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapESHighThres1day.setStatus("current")
_OtuFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
otuFacilityDataThresholdCapSESHighThres15min = _OtuFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 3),
    _OtuFacilityDataThresholdCapSESHighThres15min_Type()
)
otuFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_OtuFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
otuFacilityDataThresholdCapSESHighThres1day = _OtuFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 4),
    _OtuFacilityDataThresholdCapSESHighThres1day_Type()
)
otuFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_OtuFacilityDataThresholdCapBbeHighThres15min_Type = Counter64StringCaps
_OtuFacilityDataThresholdCapBbeHighThres15min_Object = MibTableColumn
otuFacilityDataThresholdCapBbeHighThres15min = _OtuFacilityDataThresholdCapBbeHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 5),
    _OtuFacilityDataThresholdCapBbeHighThres15min_Type()
)
otuFacilityDataThresholdCapBbeHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapBbeHighThres15min.setStatus("current")
_OtuFacilityDataThresholdCapBbeHighThres1day_Type = Counter64StringCaps
_OtuFacilityDataThresholdCapBbeHighThres1day_Object = MibTableColumn
otuFacilityDataThresholdCapBbeHighThres1day = _OtuFacilityDataThresholdCapBbeHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 6),
    _OtuFacilityDataThresholdCapBbeHighThres1day_Type()
)
otuFacilityDataThresholdCapBbeHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapBbeHighThres1day.setStatus("current")
_OtuFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
otuFacilityDataThresholdCapUASHighThres15min = _OtuFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 7),
    _OtuFacilityDataThresholdCapUASHighThres15min_Type()
)
otuFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_OtuFacilityDataThresholdCapUASHighThres1day_Type = FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapUASHighThres1day_Object = MibTableColumn
otuFacilityDataThresholdCapUASHighThres1day = _OtuFacilityDataThresholdCapUASHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 9, 1, 8),
    _OtuFacilityDataThresholdCapUASHighThres1day_Type()
)
otuFacilityDataThresholdCapUASHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFacilityDataThresholdCapUASHighThres1day.setStatus("current")
_EndOfOtuFacilityDataThresholdCapTable_Type = Integer32
_EndOfOtuFacilityDataThresholdCapTable_Object = MibScalar
endOfOtuFacilityDataThresholdCapTable = _EndOfOtuFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 10),
    _EndOfOtuFacilityDataThresholdCapTable_Type()
)
endOfOtuFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOtuFacilityDataThresholdCapTable.setStatus("current")
_OtuFecFacilityDataThresholdCapTable_Object = MibTable
otuFecFacilityDataThresholdCapTable = _OtuFecFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11)
)
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapTable.setStatus("current")
_OtuFecFacilityDataThresholdCapEntry_Object = MibTableRow
otuFecFacilityDataThresholdCapEntry = _OtuFecFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1)
)
otuFecFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapEntry.setStatus("current")
_OtuFecFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
otuFecFacilityDataThresholdCapESHighThres15min = _OtuFecFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 1),
    _OtuFecFacilityDataThresholdCapESHighThres15min_Type()
)
otuFecFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapESHighThres15min.setStatus("current")
_OtuFecFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
otuFecFacilityDataThresholdCapESHighThres1day = _OtuFecFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 2),
    _OtuFecFacilityDataThresholdCapESHighThres1day_Type()
)
otuFecFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapESHighThres1day.setStatus("current")
_OtuFecFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
otuFecFacilityDataThresholdCapSESHighThres15min = _OtuFecFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 3),
    _OtuFecFacilityDataThresholdCapSESHighThres15min_Type()
)
otuFecFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_OtuFecFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
otuFecFacilityDataThresholdCapSESHighThres1day = _OtuFecFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 4),
    _OtuFecFacilityDataThresholdCapSESHighThres1day_Type()
)
otuFecFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_OtuFecFacilityDataThresholdCapUBEHighThres15min_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapUBEHighThres15min_Object = MibTableColumn
otuFecFacilityDataThresholdCapUBEHighThres15min = _OtuFecFacilityDataThresholdCapUBEHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 5),
    _OtuFecFacilityDataThresholdCapUBEHighThres15min_Type()
)
otuFecFacilityDataThresholdCapUBEHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapUBEHighThres15min.setStatus("current")
_OtuFecFacilityDataThresholdCapUBEHighThres1day_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapUBEHighThres1day_Object = MibTableColumn
otuFecFacilityDataThresholdCapUBEHighThres1day = _OtuFecFacilityDataThresholdCapUBEHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 6),
    _OtuFecFacilityDataThresholdCapUBEHighThres1day_Type()
)
otuFecFacilityDataThresholdCapUBEHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapUBEHighThres1day.setStatus("current")
_OtuFecFacilityDataThresholdCapCErrHighThres15min_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapCErrHighThres15min_Object = MibTableColumn
otuFecFacilityDataThresholdCapCErrHighThres15min = _OtuFecFacilityDataThresholdCapCErrHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 7),
    _OtuFecFacilityDataThresholdCapCErrHighThres15min_Type()
)
otuFecFacilityDataThresholdCapCErrHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapCErrHighThres15min.setStatus("current")
_OtuFecFacilityDataThresholdCapCErrHighThres1day_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapCErrHighThres1day_Object = MibTableColumn
otuFecFacilityDataThresholdCapCErrHighThres1day = _OtuFecFacilityDataThresholdCapCErrHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 8),
    _OtuFecFacilityDataThresholdCapCErrHighThres1day_Type()
)
otuFecFacilityDataThresholdCapCErrHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapCErrHighThres1day.setStatus("current")
_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Object = MibTableColumn
otuFecFacilityDataThresholdCapBERCErrHighThres15min = _OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 9),
    _OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Type()
)
otuFecFacilityDataThresholdCapBERCErrHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapBERCErrHighThres15min.setStatus("current")
_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Type = Counter64StringCaps
_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Object = MibTableColumn
otuFecFacilityDataThresholdCapBERCErrHighThres1day = _OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 11, 1, 10),
    _OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Type()
)
otuFecFacilityDataThresholdCapBERCErrHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuFecFacilityDataThresholdCapBERCErrHighThres1day.setStatus("current")
_EndOfOtuFecFacilityDataThresholdCapTable_Type = Integer32
_EndOfOtuFecFacilityDataThresholdCapTable_Object = MibScalar
endOfOtuFecFacilityDataThresholdCapTable = _EndOfOtuFecFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 12),
    _EndOfOtuFecFacilityDataThresholdCapTable_Type()
)
endOfOtuFecFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOtuFecFacilityDataThresholdCapTable.setStatus("current")
_FecFacilityDataThresholdCapTable_Object = MibTable
fecFacilityDataThresholdCapTable = _FecFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapTable.setStatus("current")
_FecFacilityDataThresholdCapEntry_Object = MibTableRow
fecFacilityDataThresholdCapEntry = _FecFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13, 1)
)
fecFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapEntry.setStatus("current")
_FecFacilityDataThresholdCapCEHighThres15min_Type = Counter64StringCaps
_FecFacilityDataThresholdCapCEHighThres15min_Object = MibTableColumn
fecFacilityDataThresholdCapCEHighThres15min = _FecFacilityDataThresholdCapCEHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13, 1, 1),
    _FecFacilityDataThresholdCapCEHighThres15min_Type()
)
fecFacilityDataThresholdCapCEHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapCEHighThres15min.setStatus("current")
_FecFacilityDataThresholdCapCEHighThres1day_Type = Counter64StringCaps
_FecFacilityDataThresholdCapCEHighThres1day_Object = MibTableColumn
fecFacilityDataThresholdCapCEHighThres1day = _FecFacilityDataThresholdCapCEHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13, 1, 2),
    _FecFacilityDataThresholdCapCEHighThres1day_Type()
)
fecFacilityDataThresholdCapCEHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapCEHighThres1day.setStatus("current")
_FecFacilityDataThresholdCapUBEHighThres15min_Type = Counter64StringCaps
_FecFacilityDataThresholdCapUBEHighThres15min_Object = MibTableColumn
fecFacilityDataThresholdCapUBEHighThres15min = _FecFacilityDataThresholdCapUBEHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13, 1, 3),
    _FecFacilityDataThresholdCapUBEHighThres15min_Type()
)
fecFacilityDataThresholdCapUBEHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapUBEHighThres15min.setStatus("current")
_FecFacilityDataThresholdCapUBEHighThres1day_Type = Counter64StringCaps
_FecFacilityDataThresholdCapUBEHighThres1day_Object = MibTableColumn
fecFacilityDataThresholdCapUBEHighThres1day = _FecFacilityDataThresholdCapUBEHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 13, 1, 4),
    _FecFacilityDataThresholdCapUBEHighThres1day_Type()
)
fecFacilityDataThresholdCapUBEHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecFacilityDataThresholdCapUBEHighThres1day.setStatus("current")
_EndOfFecFacilityDataThresholdCapTable_Type = Integer32
_EndOfFecFacilityDataThresholdCapTable_Object = MibScalar
endOfFecFacilityDataThresholdCapTable = _EndOfFecFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 14),
    _EndOfFecFacilityDataThresholdCapTable_Type()
)
endOfFecFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFecFacilityDataThresholdCapTable.setStatus("current")
_Pcs2FacilityDataThresholdCapTable_Object = MibTable
pcs2FacilityDataThresholdCapTable = _Pcs2FacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15)
)
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapTable.setStatus("current")
_Pcs2FacilityDataThresholdCapEntry_Object = MibTableRow
pcs2FacilityDataThresholdCapEntry = _Pcs2FacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1)
)
pcs2FacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapEntry.setStatus("current")
_Pcs2FacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
pcs2FacilityDataThresholdCapESHighThres15min = _Pcs2FacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 1),
    _Pcs2FacilityDataThresholdCapESHighThres15min_Type()
)
pcs2FacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapESHighThres15min.setStatus("current")
_Pcs2FacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
pcs2FacilityDataThresholdCapESHighThres1day = _Pcs2FacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 2),
    _Pcs2FacilityDataThresholdCapESHighThres1day_Type()
)
pcs2FacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapESHighThres1day.setStatus("current")
_Pcs2FacilityDataThresholdCapDEHighThres15min_Type = FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapDEHighThres15min_Object = MibTableColumn
pcs2FacilityDataThresholdCapDEHighThres15min = _Pcs2FacilityDataThresholdCapDEHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 3),
    _Pcs2FacilityDataThresholdCapDEHighThres15min_Type()
)
pcs2FacilityDataThresholdCapDEHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapDEHighThres15min.setStatus("current")
_Pcs2FacilityDataThresholdCapDEHighThres1day_Type = FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapDEHighThres1day_Object = MibTableColumn
pcs2FacilityDataThresholdCapDEHighThres1day = _Pcs2FacilityDataThresholdCapDEHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 4),
    _Pcs2FacilityDataThresholdCapDEHighThres1day_Type()
)
pcs2FacilityDataThresholdCapDEHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapDEHighThres1day.setStatus("current")
_Pcs2FacilityDataThresholdCapCVHighThres15min_Type = Counter64StringCaps
_Pcs2FacilityDataThresholdCapCVHighThres15min_Object = MibTableColumn
pcs2FacilityDataThresholdCapCVHighThres15min = _Pcs2FacilityDataThresholdCapCVHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 5),
    _Pcs2FacilityDataThresholdCapCVHighThres15min_Type()
)
pcs2FacilityDataThresholdCapCVHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapCVHighThres15min.setStatus("current")
_Pcs2FacilityDataThresholdCapCVHighThres1day_Type = Counter64StringCaps
_Pcs2FacilityDataThresholdCapCVHighThres1day_Object = MibTableColumn
pcs2FacilityDataThresholdCapCVHighThres1day = _Pcs2FacilityDataThresholdCapCVHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 15, 1, 6),
    _Pcs2FacilityDataThresholdCapCVHighThres1day_Type()
)
pcs2FacilityDataThresholdCapCVHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcs2FacilityDataThresholdCapCVHighThres1day.setStatus("current")
_EndOfPcs2FacilityDataThresholdCapTable_Type = Integer32
_EndOfPcs2FacilityDataThresholdCapTable_Object = MibScalar
endOfPcs2FacilityDataThresholdCapTable = _EndOfPcs2FacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 16),
    _EndOfPcs2FacilityDataThresholdCapTable_Type()
)
endOfPcs2FacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPcs2FacilityDataThresholdCapTable.setStatus("current")
_LFacilityDataThresholdCapTable_Object = MibTable
lFacilityDataThresholdCapTable = _LFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17)
)
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapTable.setStatus("current")
_LFacilityDataThresholdCapEntry_Object = MibTableRow
lFacilityDataThresholdCapEntry = _LFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1)
)
lFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapEntry.setStatus("current")
_LFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
lFacilityDataThresholdCapESHighThres15min = _LFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 1),
    _LFacilityDataThresholdCapESHighThres15min_Type()
)
lFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapESHighThres15min.setStatus("current")
_LFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
lFacilityDataThresholdCapESHighThres1day = _LFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 2),
    _LFacilityDataThresholdCapESHighThres1day_Type()
)
lFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapESHighThres1day.setStatus("current")
_LFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
lFacilityDataThresholdCapSESHighThres15min = _LFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 3),
    _LFacilityDataThresholdCapSESHighThres15min_Type()
)
lFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_LFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
lFacilityDataThresholdCapSESHighThres1day = _LFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 4),
    _LFacilityDataThresholdCapSESHighThres1day_Type()
)
lFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_LFacilityDataThresholdCapUASHighThres15min_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapUASHighThres15min_Object = MibTableColumn
lFacilityDataThresholdCapUASHighThres15min = _LFacilityDataThresholdCapUASHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 5),
    _LFacilityDataThresholdCapUASHighThres15min_Type()
)
lFacilityDataThresholdCapUASHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapUASHighThres15min.setStatus("current")
_LFacilityDataThresholdCapUASSHighThres1day_Type = FspR7Unsigned32Caps
_LFacilityDataThresholdCapUASSHighThres1day_Object = MibTableColumn
lFacilityDataThresholdCapUASSHighThres1day = _LFacilityDataThresholdCapUASSHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 6),
    _LFacilityDataThresholdCapUASSHighThres1day_Type()
)
lFacilityDataThresholdCapUASSHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapUASSHighThres1day.setStatus("current")
_LFacilityDataThresholdCapCVHighThres15min_Type = Counter64StringCaps
_LFacilityDataThresholdCapCVHighThres15min_Object = MibTableColumn
lFacilityDataThresholdCapCVHighThres15min = _LFacilityDataThresholdCapCVHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 7),
    _LFacilityDataThresholdCapCVHighThres15min_Type()
)
lFacilityDataThresholdCapCVHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapCVHighThres15min.setStatus("current")
_LFacilityDataThresholdCapCVSHighThres1day_Type = Counter64StringCaps
_LFacilityDataThresholdCapCVSHighThres1day_Object = MibTableColumn
lFacilityDataThresholdCapCVSHighThres1day = _LFacilityDataThresholdCapCVSHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 17, 1, 8),
    _LFacilityDataThresholdCapCVSHighThres1day_Type()
)
lFacilityDataThresholdCapCVSHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lFacilityDataThresholdCapCVSHighThres1day.setStatus("current")
_EndOfLFacilityDataThresholdCapTable_Type = Integer32
_EndOfLFacilityDataThresholdCapTable_Object = MibScalar
endOfLFacilityDataThresholdCapTable = _EndOfLFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 18),
    _EndOfLFacilityDataThresholdCapTable_Type()
)
endOfLFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfLFacilityDataThresholdCapTable.setStatus("current")
_SFacilityDataThresholdCapTable_Object = MibTable
sFacilityDataThresholdCapTable = _SFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19)
)
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapTable.setStatus("current")
_SFacilityDataThresholdCapEntry_Object = MibTableRow
sFacilityDataThresholdCapEntry = _SFacilityDataThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1)
)
sFacilityDataThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapEntry.setStatus("current")
_SFacilityDataThresholdCapESHighThres15min_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapESHighThres15min_Object = MibTableColumn
sFacilityDataThresholdCapESHighThres15min = _SFacilityDataThresholdCapESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 1),
    _SFacilityDataThresholdCapESHighThres15min_Type()
)
sFacilityDataThresholdCapESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapESHighThres15min.setStatus("current")
_SFacilityDataThresholdCapESHighThres1day_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapESHighThres1day_Object = MibTableColumn
sFacilityDataThresholdCapESHighThres1day = _SFacilityDataThresholdCapESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 2),
    _SFacilityDataThresholdCapESHighThres1day_Type()
)
sFacilityDataThresholdCapESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapESHighThres1day.setStatus("current")
_SFacilityDataThresholdCapSESHighThres15min_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapSESHighThres15min_Object = MibTableColumn
sFacilityDataThresholdCapSESHighThres15min = _SFacilityDataThresholdCapSESHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 3),
    _SFacilityDataThresholdCapSESHighThres15min_Type()
)
sFacilityDataThresholdCapSESHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapSESHighThres15min.setStatus("current")
_SFacilityDataThresholdCapSESHighThres1day_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapSESHighThres1day_Object = MibTableColumn
sFacilityDataThresholdCapSESHighThres1day = _SFacilityDataThresholdCapSESHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 4),
    _SFacilityDataThresholdCapSESHighThres1day_Type()
)
sFacilityDataThresholdCapSESHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapSESHighThres1day.setStatus("current")
_SFacilityDataThresholdCapSEFSHighThres15min_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapSEFSHighThres15min_Object = MibTableColumn
sFacilityDataThresholdCapSEFSHighThres15min = _SFacilityDataThresholdCapSEFSHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 5),
    _SFacilityDataThresholdCapSEFSHighThres15min_Type()
)
sFacilityDataThresholdCapSEFSHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapSEFSHighThres15min.setStatus("current")
_SFacilityDataThresholdCapSEFSHighThres1day_Type = FspR7Unsigned32Caps
_SFacilityDataThresholdCapSEFSHighThres1day_Object = MibTableColumn
sFacilityDataThresholdCapSEFSHighThres1day = _SFacilityDataThresholdCapSEFSHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 6),
    _SFacilityDataThresholdCapSEFSHighThres1day_Type()
)
sFacilityDataThresholdCapSEFSHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapSEFSHighThres1day.setStatus("current")
_SFacilityDataThresholdCapCVHighThres15min_Type = Counter64StringCaps
_SFacilityDataThresholdCapCVHighThres15min_Object = MibTableColumn
sFacilityDataThresholdCapCVHighThres15min = _SFacilityDataThresholdCapCVHighThres15min_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 7),
    _SFacilityDataThresholdCapCVHighThres15min_Type()
)
sFacilityDataThresholdCapCVHighThres15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapCVHighThres15min.setStatus("current")
_SFacilityDataThresholdCapCVHighThres1day_Type = Counter64StringCaps
_SFacilityDataThresholdCapCVHighThres1day_Object = MibTableColumn
sFacilityDataThresholdCapCVHighThres1day = _SFacilityDataThresholdCapCVHighThres1day_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 19, 1, 8),
    _SFacilityDataThresholdCapCVHighThres1day_Type()
)
sFacilityDataThresholdCapCVHighThres1day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFacilityDataThresholdCapCVHighThres1day.setStatus("current")
_EndOfSFacilityDataThresholdCapTable_Type = Integer32
_EndOfSFacilityDataThresholdCapTable_Object = MibScalar
endOfSFacilityDataThresholdCapTable = _EndOfSFacilityDataThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 20),
    _EndOfSFacilityDataThresholdCapTable_Type()
)
endOfSFacilityDataThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfSFacilityDataThresholdCapTable.setStatus("current")
_EndOfPmFacilityDataThresholdCap_Type = Integer32
_EndOfPmFacilityDataThresholdCap_Object = MibScalar
endOfPmFacilityDataThresholdCap = _EndOfPmFacilityDataThresholdCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 1, 10000),
    _EndOfPmFacilityDataThresholdCap_Type()
)
endOfPmFacilityDataThresholdCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmFacilityDataThresholdCap.setStatus("current")
_EndOfPmFacilityDataCap_Type = Integer32
_EndOfPmFacilityDataCap_Object = MibScalar
endOfPmFacilityDataCap = _EndOfPmFacilityDataCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 1, 10000),
    _EndOfPmFacilityDataCap_Type()
)
endOfPmFacilityDataCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmFacilityDataCap.setStatus("current")
_PmFacilityPhysicalCap_ObjectIdentity = ObjectIdentity
pmFacilityPhysicalCap = _PmFacilityPhysicalCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2)
)
_PmFacilityPhysValueCap_ObjectIdentity = ObjectIdentity
pmFacilityPhysValueCap = _PmFacilityPhysValueCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 1)
)
_PmFacilityPhysThresholdCap_ObjectIdentity = ObjectIdentity
pmFacilityPhysThresholdCap = _PmFacilityPhysThresholdCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2)
)
_FacilityPhysThresholdCapTable_Object = MibTable
facilityPhysThresholdCapTable = _FacilityPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    facilityPhysThresholdCapTable.setStatus("current")
_FacilityPhysThresholdCapEntry_Object = MibTableRow
facilityPhysThresholdCapEntry = _FacilityPhysThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1)
)
facilityPhysThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    facilityPhysThresholdCapEntry.setStatus("current")
_FacilityPhysThresholdCapOpticalInputPwrLow_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapOpticalInputPwrLow_Object = MibTableColumn
facilityPhysThresholdCapOpticalInputPwrLow = _FacilityPhysThresholdCapOpticalInputPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 1),
    _FacilityPhysThresholdCapOpticalInputPwrLow_Type()
)
facilityPhysThresholdCapOpticalInputPwrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapOpticalInputPwrLow.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapOpticalInputPwrLow.setUnits("0.1 dBm")
_FacilityPhysThresholdCapOpticalInputPwrHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapOpticalInputPwrHigh_Object = MibTableColumn
facilityPhysThresholdCapOpticalInputPwrHigh = _FacilityPhysThresholdCapOpticalInputPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 2),
    _FacilityPhysThresholdCapOpticalInputPwrHigh_Type()
)
facilityPhysThresholdCapOpticalInputPwrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapOpticalInputPwrHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapOpticalInputPwrHigh.setUnits("0.1 dBm")
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Object = MibTableColumn
facilityPhysThresholdCapConfigurableOpticalOutputPwrLow = _FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 3),
    _FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Type()
)
facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setUnits("0.1 dBm")
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object = MibTableColumn
facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh = _FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 4),
    _FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type()
)
facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setUnits("0.1 dBm")
_FacilityPhysThresholdCapRoundTripDelayLowThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapRoundTripDelayLowThres_Object = MibTableColumn
facilityPhysThresholdCapRoundTripDelayLowThres = _FacilityPhysThresholdCapRoundTripDelayLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 5),
    _FacilityPhysThresholdCapRoundTripDelayLowThres_Type()
)
facilityPhysThresholdCapRoundTripDelayLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapRoundTripDelayLowThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapRoundTripDelayLowThres.setUnits("ns")
_FacilityPhysThresholdCapRoundTripDelayHighThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapRoundTripDelayHighThres_Object = MibTableColumn
facilityPhysThresholdCapRoundTripDelayHighThres = _FacilityPhysThresholdCapRoundTripDelayHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 6),
    _FacilityPhysThresholdCapRoundTripDelayHighThres_Type()
)
facilityPhysThresholdCapRoundTripDelayHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapRoundTripDelayHighThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapRoundTripDelayHighThres.setUnits("ns")
_FacilityPhysThresholdCapLatencyLowThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapLatencyLowThres_Object = MibTableColumn
facilityPhysThresholdCapLatencyLowThres = _FacilityPhysThresholdCapLatencyLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 7),
    _FacilityPhysThresholdCapLatencyLowThres_Type()
)
facilityPhysThresholdCapLatencyLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLatencyLowThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLatencyLowThres.setUnits("0.1 us")
_FacilityPhysThresholdCapLatencyHighThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapLatencyHighThres_Object = MibTableColumn
facilityPhysThresholdCapLatencyHighThres = _FacilityPhysThresholdCapLatencyHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 8),
    _FacilityPhysThresholdCapLatencyHighThres_Type()
)
facilityPhysThresholdCapLatencyHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLatencyHighThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLatencyHighThres.setUnits("0.1 us")
_FacilityPhysThresholdCapChromaticDispersionHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapChromaticDispersionHigh_Object = MibTableColumn
facilityPhysThresholdCapChromaticDispersionHigh = _FacilityPhysThresholdCapChromaticDispersionHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 9),
    _FacilityPhysThresholdCapChromaticDispersionHigh_Type()
)
facilityPhysThresholdCapChromaticDispersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapChromaticDispersionHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapChromaticDispersionHigh.setUnits("ps/nm")
_FacilityPhysThresholdCapChromaticDispersionLow_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapChromaticDispersionLow_Object = MibTableColumn
facilityPhysThresholdCapChromaticDispersionLow = _FacilityPhysThresholdCapChromaticDispersionLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 10),
    _FacilityPhysThresholdCapChromaticDispersionLow_Type()
)
facilityPhysThresholdCapChromaticDispersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapChromaticDispersionLow.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapChromaticDispersionLow.setUnits("ps/nm")
_FacilityPhysThresholdCapCarrierFreqOffsetLow_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapCarrierFreqOffsetLow_Object = MibTableColumn
facilityPhysThresholdCapCarrierFreqOffsetLow = _FacilityPhysThresholdCapCarrierFreqOffsetLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 11),
    _FacilityPhysThresholdCapCarrierFreqOffsetLow_Type()
)
facilityPhysThresholdCapCarrierFreqOffsetLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapCarrierFreqOffsetLow.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapCarrierFreqOffsetLow.setUnits("0.001 GHz")
_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Object = MibTableColumn
facilityPhysThresholdCapCarrierFreqOffsetHigh = _FacilityPhysThresholdCapCarrierFreqOffsetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 12),
    _FacilityPhysThresholdCapCarrierFreqOffsetHigh_Type()
)
facilityPhysThresholdCapCarrierFreqOffsetHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapCarrierFreqOffsetHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapCarrierFreqOffsetHigh.setUnits("0.001 GHz")
_FacilityPhysThresholdCapLogicalLanesSkewHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapLogicalLanesSkewHigh_Object = MibTableColumn
facilityPhysThresholdCapLogicalLanesSkewHigh = _FacilityPhysThresholdCapLogicalLanesSkewHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 13),
    _FacilityPhysThresholdCapLogicalLanesSkewHigh_Type()
)
facilityPhysThresholdCapLogicalLanesSkewHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLogicalLanesSkewHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapLogicalLanesSkewHigh.setUnits("ns")
_FacilityPhysThresholdCapDispersionCompensationLowThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapDispersionCompensationLowThres_Object = MibTableColumn
facilityPhysThresholdCapDispersionCompensationLowThres = _FacilityPhysThresholdCapDispersionCompensationLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 14),
    _FacilityPhysThresholdCapDispersionCompensationLowThres_Type()
)
facilityPhysThresholdCapDispersionCompensationLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDispersionCompensationLowThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDispersionCompensationLowThres.setUnits("ps/nm")
_FacilityPhysThresholdCapDispersionCompensationHighThres_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapDispersionCompensationHighThres_Object = MibTableColumn
facilityPhysThresholdCapDispersionCompensationHighThres = _FacilityPhysThresholdCapDispersionCompensationHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 15),
    _FacilityPhysThresholdCapDispersionCompensationHighThres_Type()
)
facilityPhysThresholdCapDispersionCompensationHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDispersionCompensationHighThres.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDispersionCompensationHighThres.setUnits("ps/nm")
_FacilityPhysThresholdCapSignalToNoiseRatioLow_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapSignalToNoiseRatioLow_Object = MibTableColumn
facilityPhysThresholdCapSignalToNoiseRatioLow = _FacilityPhysThresholdCapSignalToNoiseRatioLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 16),
    _FacilityPhysThresholdCapSignalToNoiseRatioLow_Type()
)
facilityPhysThresholdCapSignalToNoiseRatioLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapSignalToNoiseRatioLow.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapSignalToNoiseRatioLow.setUnits("0.1 dB")
_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Type = FspR7Integer32Caps
_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Object = MibTableColumn
facilityPhysThresholdCapDifferentialGroupDelayHigh = _FacilityPhysThresholdCapDifferentialGroupDelayHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 1, 1, 17),
    _FacilityPhysThresholdCapDifferentialGroupDelayHigh_Type()
)
facilityPhysThresholdCapDifferentialGroupDelayHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDifferentialGroupDelayHigh.setStatus("current")
if mibBuilder.loadTexts:
    facilityPhysThresholdCapDifferentialGroupDelayHigh.setUnits("ps")
_EndOfFacilityPhysThresholdCapTable_Type = Integer32
_EndOfFacilityPhysThresholdCapTable_Object = MibScalar
endOfFacilityPhysThresholdCapTable = _EndOfFacilityPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 2),
    _EndOfFacilityPhysThresholdCapTable_Type()
)
endOfFacilityPhysThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFacilityPhysThresholdCapTable.setStatus("current")
_EndOfPmFacilityPhysThresholdCap_Type = Integer32
_EndOfPmFacilityPhysThresholdCap_Object = MibScalar
endOfPmFacilityPhysThresholdCap = _EndOfPmFacilityPhysThresholdCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 2, 10000),
    _EndOfPmFacilityPhysThresholdCap_Type()
)
endOfPmFacilityPhysThresholdCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmFacilityPhysThresholdCap.setStatus("current")
_EndOfPmFacilityPhysicalCap_Type = Integer32
_EndOfPmFacilityPhysicalCap_Object = MibScalar
endOfPmFacilityPhysicalCap = _EndOfPmFacilityPhysicalCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 2, 10000),
    _EndOfPmFacilityPhysicalCap_Type()
)
endOfPmFacilityPhysicalCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmFacilityPhysicalCap.setStatus("current")
_EndOfPmFacilityCap_Type = Integer32
_EndOfPmFacilityCap_Object = MibScalar
endOfPmFacilityCap = _EndOfPmFacilityCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 12, 10000),
    _EndOfPmFacilityCap_Type()
)
endOfPmFacilityCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmFacilityCap.setStatus("current")
_PmTerminPointCap_ObjectIdentity = ObjectIdentity
pmTerminPointCap = _PmTerminPointCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 13)
)
_PmOptMuxCap_ObjectIdentity = ObjectIdentity
pmOptMuxCap = _PmOptMuxCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14)
)
_PmOptMuxDataCap_ObjectIdentity = ObjectIdentity
pmOptMuxDataCap = _PmOptMuxDataCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 1)
)
_PmOptMuxPhysicalCap_ObjectIdentity = ObjectIdentity
pmOptMuxPhysicalCap = _PmOptMuxPhysicalCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2)
)
_PmOptMuxPhysValueCap_ObjectIdentity = ObjectIdentity
pmOptMuxPhysValueCap = _PmOptMuxPhysValueCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 1)
)
_PmOptMuxPhysThresholdCap_ObjectIdentity = ObjectIdentity
pmOptMuxPhysThresholdCap = _PmOptMuxPhysThresholdCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2)
)
_OptMuxPhysThresholdCapTable_Object = MibTable
optMuxPhysThresholdCapTable = _OptMuxPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2)
)
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapTable.setStatus("current")
_OptMuxPhysThresholdCapEntry_Object = MibTableRow
optMuxPhysThresholdCapEntry = _OptMuxPhysThresholdCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1)
)
optMuxPhysThresholdCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxClassName"),
)
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapEntry.setStatus("current")
_OptMuxPhysThresholdCapBrtxHighConfig_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapBrtxHighConfig_Object = MibTableColumn
optMuxPhysThresholdCapBrtxHighConfig = _OptMuxPhysThresholdCapBrtxHighConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 1),
    _OptMuxPhysThresholdCapBrtxHighConfig_Type()
)
optMuxPhysThresholdCapBrtxHighConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapBrtxHighConfig.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapBrtxHighConfig.setUnits("0.1 dB")
_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Object = MibTableColumn
optMuxPhysThresholdCapBrPwrReceivedHighThres = _OptMuxPhysThresholdCapBrPwrReceivedHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 2),
    _OptMuxPhysThresholdCapBrPwrReceivedHighThres_Type()
)
optMuxPhysThresholdCapBrPwrReceivedHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapBrPwrReceivedHighThres.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapBrPwrReceivedHighThres.setUnits("0.1 dB")
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object = MibTableColumn
optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh = _OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 3),
    _OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type()
)
optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Object = MibTableColumn
optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow = _OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 4),
    _OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Type()
)
optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapOscPwrRcvHighThres_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapOscPwrRcvHighThres_Object = MibTableColumn
optMuxPhysThresholdCapOscPwrRcvHighThres = _OptMuxPhysThresholdCapOscPwrRcvHighThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 5),
    _OptMuxPhysThresholdCapOscPwrRcvHighThres_Type()
)
optMuxPhysThresholdCapOscPwrRcvHighThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOscPwrRcvHighThres.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOscPwrRcvHighThres.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapOscPwrRcvLowThres_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapOscPwrRcvLowThres_Object = MibTableColumn
optMuxPhysThresholdCapOscPwrRcvLowThres = _OptMuxPhysThresholdCapOscPwrRcvLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 6),
    _OptMuxPhysThresholdCapOscPwrRcvLowThres_Type()
)
optMuxPhysThresholdCapOscPwrRcvLowThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOscPwrRcvLowThres.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOscPwrRcvLowThres.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapOpticalInputPwrHigh_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapOpticalInputPwrHigh_Object = MibTableColumn
optMuxPhysThresholdCapOpticalInputPwrHigh = _OptMuxPhysThresholdCapOpticalInputPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 7),
    _OptMuxPhysThresholdCapOpticalInputPwrHigh_Type()
)
optMuxPhysThresholdCapOpticalInputPwrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOpticalInputPwrHigh.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOpticalInputPwrHigh.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapOpticalInputPwrLow_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapOpticalInputPwrLow_Object = MibTableColumn
optMuxPhysThresholdCapOpticalInputPwrLow = _OptMuxPhysThresholdCapOpticalInputPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 8),
    _OptMuxPhysThresholdCapOpticalInputPwrLow_Type()
)
optMuxPhysThresholdCapOpticalInputPwrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOpticalInputPwrLow.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapOpticalInputPwrLow.setUnits("0.1 dBm")
_OptMuxPhysThresholdCapAttRxHigh_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapAttRxHigh_Object = MibTableColumn
optMuxPhysThresholdCapAttRxHigh = _OptMuxPhysThresholdCapAttRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 9),
    _OptMuxPhysThresholdCapAttRxHigh_Type()
)
optMuxPhysThresholdCapAttRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttRxHigh.setUnits("0.1 dB")
_OptMuxPhysThresholdCapAttRxLow_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapAttRxLow_Object = MibTableColumn
optMuxPhysThresholdCapAttRxLow = _OptMuxPhysThresholdCapAttRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 10),
    _OptMuxPhysThresholdCapAttRxLow_Type()
)
optMuxPhysThresholdCapAttRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttRxLow.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttRxLow.setUnits("0.1 dB")
_OptMuxPhysThresholdCapAttTxHigh_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapAttTxHigh_Object = MibTableColumn
optMuxPhysThresholdCapAttTxHigh = _OptMuxPhysThresholdCapAttTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 11),
    _OptMuxPhysThresholdCapAttTxHigh_Type()
)
optMuxPhysThresholdCapAttTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttTxHigh.setUnits("0.1 dB")
_OptMuxPhysThresholdCapAttTxLow_Type = FspR7Integer32Caps
_OptMuxPhysThresholdCapAttTxLow_Object = MibTableColumn
optMuxPhysThresholdCapAttTxLow = _OptMuxPhysThresholdCapAttTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 2, 1, 12),
    _OptMuxPhysThresholdCapAttTxLow_Type()
)
optMuxPhysThresholdCapAttTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttTxLow.setStatus("current")
if mibBuilder.loadTexts:
    optMuxPhysThresholdCapAttTxLow.setUnits("0.1 dB")
_EndOfOptMuxPhysThresholdCapTable_Type = Integer32
_EndOfOptMuxPhysThresholdCapTable_Object = MibScalar
endOfOptMuxPhysThresholdCapTable = _EndOfOptMuxPhysThresholdCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 3),
    _EndOfOptMuxPhysThresholdCapTable_Type()
)
endOfOptMuxPhysThresholdCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOptMuxPhysThresholdCapTable.setStatus("current")
_EndOfPmOptMuxPhysThresholdCap_Type = Integer32
_EndOfPmOptMuxPhysThresholdCap_Object = MibScalar
endOfPmOptMuxPhysThresholdCap = _EndOfPmOptMuxPhysThresholdCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 6, 14, 2, 2, 10000),
    _EndOfPmOptMuxPhysThresholdCap_Type()
)
endOfPmOptMuxPhysThresholdCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPmOptMuxPhysThresholdCap.setStatus("current")
_FeatureSpecificCap_ObjectIdentity = ObjectIdentity
featureSpecificCap = _FeatureSpecificCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7)
)
_FiberMapCap_ObjectIdentity = ObjectIdentity
fiberMapCap = _FiberMapCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1)
)
_TerminationPointCapTable_Object = MibTable
terminationPointCapTable = _TerminationPointCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1)
)
if mibBuilder.loadTexts:
    terminationPointCapTable.setStatus("current")
_TerminationPointCapEntry_Object = MibTableRow
terminationPointCapEntry = _TerminationPointCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1, 1)
)
terminationPointCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointClassName"),
)
if mibBuilder.loadTexts:
    terminationPointCapEntry.setStatus("current")
_TerminationPointCapRowStatus_Type = FspR7RowStatusCaps
_TerminationPointCapRowStatus_Object = MibTableColumn
terminationPointCapRowStatus = _TerminationPointCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1, 1, 1),
    _TerminationPointCapRowStatus_Type()
)
terminationPointCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointCapRowStatus.setStatus("current")
_TerminationPointCapAdmin_Type = FspR7AdminStateCaps
_TerminationPointCapAdmin_Object = MibTableColumn
terminationPointCapAdmin = _TerminationPointCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1, 1, 2),
    _TerminationPointCapAdmin_Type()
)
terminationPointCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointCapAdmin.setStatus("current")
_TerminationPointCapFiberDetect_Type = FspR7FiberDetectCaps
_TerminationPointCapFiberDetect_Object = MibTableColumn
terminationPointCapFiberDetect = _TerminationPointCapFiberDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1, 1, 3),
    _TerminationPointCapFiberDetect_Type()
)
terminationPointCapFiberDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointCapFiberDetect.setStatus("current")
_TerminationPointCapAlias_Type = Integer32
_TerminationPointCapAlias_Object = MibTableColumn
terminationPointCapAlias = _TerminationPointCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 1, 1, 4),
    _TerminationPointCapAlias_Type()
)
terminationPointCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointCapAlias.setStatus("current")
_ConnectionCapTable_Object = MibTable
connectionCapTable = _ConnectionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 2)
)
if mibBuilder.loadTexts:
    connectionCapTable.setStatus("current")
_ConnectionCapEntry_Object = MibTableRow
connectionCapEntry = _ConnectionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 2, 1)
)
connectionCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointClassName"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointClassName"),
    (0, "ADVA-FSPR7-MIB", "entityConnectionClassName"),
)
if mibBuilder.loadTexts:
    connectionCapEntry.setStatus("current")
_ConnectionCapRowStatus_Type = FspR7RowStatusCaps
_ConnectionCapRowStatus_Object = MibTableColumn
connectionCapRowStatus = _ConnectionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 2, 1, 1),
    _ConnectionCapRowStatus_Type()
)
connectionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCapRowStatus.setStatus("current")
_ConnectionCapType_Type = FspR7TypeConnectionCaps
_ConnectionCapType_Object = MibTableColumn
connectionCapType = _ConnectionCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 2, 1, 2),
    _ConnectionCapType_Type()
)
connectionCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCapType.setStatus("current")
_EndOfConnectionCapTable_Type = Integer32
_EndOfConnectionCapTable_Object = MibScalar
endOfConnectionCapTable = _EndOfConnectionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 3),
    _EndOfConnectionCapTable_Type()
)
endOfConnectionCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfConnectionCapTable.setStatus("current")
_EndOfFiberMapCap_Type = Integer32
_EndOfFiberMapCap_Object = MibScalar
endOfFiberMapCap = _EndOfFiberMapCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 1, 10000),
    _EndOfFiberMapCap_Type()
)
endOfFiberMapCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFiberMapCap.setStatus("current")
_EciCap_ObjectIdentity = ObjectIdentity
eciCap = _EciCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3)
)
_ExternalPortCapTable_Object = MibTable
externalPortCapTable = _ExternalPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1)
)
if mibBuilder.loadTexts:
    externalPortCapTable.setStatus("current")
_ExternalPortCapEntry_Object = MibTableRow
externalPortCapEntry = _ExternalPortCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1)
)
externalPortCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityExternalPortShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortClassName"),
)
if mibBuilder.loadTexts:
    externalPortCapEntry.setStatus("current")
_ExternalPortCapRowStatus_Type = FspR7RowStatusCaps
_ExternalPortCapRowStatus_Object = MibTableColumn
externalPortCapRowStatus = _ExternalPortCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 1),
    _ExternalPortCapRowStatus_Type()
)
externalPortCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapRowStatus.setStatus("current")
_ExternalPortCapType_Type = FspR7InterfaceTypeCaps
_ExternalPortCapType_Object = MibTableColumn
externalPortCapType = _ExternalPortCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 2),
    _ExternalPortCapType_Type()
)
externalPortCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapType.setStatus("current")
_ExternalPortCapTransmitChannel_Type = FspR7ChannelIdentifierCaps
_ExternalPortCapTransmitChannel_Object = MibTableColumn
externalPortCapTransmitChannel = _ExternalPortCapTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 3),
    _ExternalPortCapTransmitChannel_Type()
)
externalPortCapTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapTransmitChannel.setStatus("current")
_ExternalPortCapChannelBandwith_Type = FspR7ChannelBandwidthCaps
_ExternalPortCapChannelBandwith_Object = MibTableColumn
externalPortCapChannelBandwith = _ExternalPortCapChannelBandwith_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 4),
    _ExternalPortCapChannelBandwith_Type()
)
externalPortCapChannelBandwith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapChannelBandwith.setStatus("current")
_ExternalPortCapAlias_Type = Integer32
_ExternalPortCapAlias_Object = MibTableColumn
externalPortCapAlias = _ExternalPortCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 5),
    _ExternalPortCapAlias_Type()
)
externalPortCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapAlias.setStatus("current")
_ExternalPortCapFarEndLocation_Type = Integer32
_ExternalPortCapFarEndLocation_Object = MibTableColumn
externalPortCapFarEndLocation = _ExternalPortCapFarEndLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 6),
    _ExternalPortCapFarEndLocation_Type()
)
externalPortCapFarEndLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapFarEndLocation.setStatus("current")
_ExternalPortCapBitrate_Type = FspR7Unsigned32Caps
_ExternalPortCapBitrate_Object = MibTableColumn
externalPortCapBitrate = _ExternalPortCapBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 7),
    _ExternalPortCapBitrate_Type()
)
externalPortCapBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapBitrate.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapBitrate.setUnits("Mbps")
_ExternalPortCapFecType_Type = FspR7FecTypeCaps
_ExternalPortCapFecType_Object = MibTableColumn
externalPortCapFecType = _ExternalPortCapFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 8),
    _ExternalPortCapFecType_Type()
)
externalPortCapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapFecType.setStatus("current")
_ExternalPortCapLineCoding_Type = FspR7LineCodingCaps
_ExternalPortCapLineCoding_Object = MibTableColumn
externalPortCapLineCoding = _ExternalPortCapLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 9),
    _ExternalPortCapLineCoding_Type()
)
externalPortCapLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapLineCoding.setStatus("current")
_ExternalPortCapFrameFormat_Type = FspR7FrameFormatCaps
_ExternalPortCapFrameFormat_Object = MibTableColumn
externalPortCapFrameFormat = _ExternalPortCapFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 10),
    _ExternalPortCapFrameFormat_Type()
)
externalPortCapFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapFrameFormat.setStatus("current")
_ExternalPortCapOpticalPowerTx_Type = FspR7Integer32Caps
_ExternalPortCapOpticalPowerTx_Object = MibTableColumn
externalPortCapOpticalPowerTx = _ExternalPortCapOpticalPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 11),
    _ExternalPortCapOpticalPowerTx_Type()
)
externalPortCapOpticalPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapOpticalPowerTx.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapOpticalPowerTx.setUnits("0.1 dBm")
_ExternalPortCapOsnrTransmit_Type = FspR7Unsigned32Caps
_ExternalPortCapOsnrTransmit_Object = MibTableColumn
externalPortCapOsnrTransmit = _ExternalPortCapOsnrTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 12),
    _ExternalPortCapOsnrTransmit_Type()
)
externalPortCapOsnrTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapOsnrTransmit.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapOsnrTransmit.setUnits("dB")
_ExternalPortCapPmdTransmit_Type = FspR7Unsigned32Caps
_ExternalPortCapPmdTransmit_Object = MibTableColumn
externalPortCapPmdTransmit = _ExternalPortCapPmdTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 13),
    _ExternalPortCapPmdTransmit_Type()
)
externalPortCapPmdTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapPmdTransmit.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapPmdTransmit.setUnits("ps")
_ExternalPortCapChromDisperTx_Type = FspR7Integer32Caps
_ExternalPortCapChromDisperTx_Object = MibTableColumn
externalPortCapChromDisperTx = _ExternalPortCapChromDisperTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 14),
    _ExternalPortCapChromDisperTx_Type()
)
externalPortCapChromDisperTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapChromDisperTx.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapChromDisperTx.setUnits("ps/nm")
_ExternalPortCapMinOsnrRcv_Type = FspR7Unsigned32Caps
_ExternalPortCapMinOsnrRcv_Object = MibTableColumn
externalPortCapMinOsnrRcv = _ExternalPortCapMinOsnrRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 15),
    _ExternalPortCapMinOsnrRcv_Type()
)
externalPortCapMinOsnrRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMinOsnrRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMinOsnrRcv.setUnits("dB")
_ExternalPortCapMinOptPowerRcv_Type = FspR7Integer32Caps
_ExternalPortCapMinOptPowerRcv_Object = MibTableColumn
externalPortCapMinOptPowerRcv = _ExternalPortCapMinOptPowerRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 16),
    _ExternalPortCapMinOptPowerRcv_Type()
)
externalPortCapMinOptPowerRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMinOptPowerRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMinOptPowerRcv.setUnits("0.1 dBm")
_ExternalPortCapMaxOptPowerRcv_Type = FspR7Integer32Caps
_ExternalPortCapMaxOptPowerRcv_Object = MibTableColumn
externalPortCapMaxOptPowerRcv = _ExternalPortCapMaxOptPowerRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 17),
    _ExternalPortCapMaxOptPowerRcv_Type()
)
externalPortCapMaxOptPowerRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMaxOptPowerRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMaxOptPowerRcv.setUnits("0.1 dBm")
_ExternalPortCapMaxPmdRcv_Type = FspR7Unsigned32Caps
_ExternalPortCapMaxPmdRcv_Object = MibTableColumn
externalPortCapMaxPmdRcv = _ExternalPortCapMaxPmdRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 18),
    _ExternalPortCapMaxPmdRcv_Type()
)
externalPortCapMaxPmdRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMaxPmdRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMaxPmdRcv.setUnits("ps")
_ExternalPortCapMinChromDisperRcv_Type = FspR7Integer32Caps
_ExternalPortCapMinChromDisperRcv_Object = MibTableColumn
externalPortCapMinChromDisperRcv = _ExternalPortCapMinChromDisperRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 19),
    _ExternalPortCapMinChromDisperRcv_Type()
)
externalPortCapMinChromDisperRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMinChromDisperRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMinChromDisperRcv.setUnits("ps/nm")
_ExternalPortCapMaxChromDisperRcv_Type = FspR7Integer32Caps
_ExternalPortCapMaxChromDisperRcv_Object = MibTableColumn
externalPortCapMaxChromDisperRcv = _ExternalPortCapMaxChromDisperRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 20),
    _ExternalPortCapMaxChromDisperRcv_Type()
)
externalPortCapMaxChromDisperRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMaxChromDisperRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortCapMaxChromDisperRcv.setUnits("ps/nm")
_ExternalPortCapMaxBitErrorRate_Type = FspR7MaxBitErrorRateCaps
_ExternalPortCapMaxBitErrorRate_Object = MibTableColumn
externalPortCapMaxBitErrorRate = _ExternalPortCapMaxBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 21),
    _ExternalPortCapMaxBitErrorRate_Type()
)
externalPortCapMaxBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapMaxBitErrorRate.setStatus("current")
_ExternalPortCapSourceProfile_Type = Integer32
_ExternalPortCapSourceProfile_Object = MibTableColumn
externalPortCapSourceProfile = _ExternalPortCapSourceProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 1, 1, 22),
    _ExternalPortCapSourceProfile_Type()
)
externalPortCapSourceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortCapSourceProfile.setStatus("current")
_EndOfExternalPortCapTable_Type = Integer32
_EndOfExternalPortCapTable_Object = MibScalar
endOfExternalPortCapTable = _EndOfExternalPortCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 2),
    _EndOfExternalPortCapTable_Type()
)
endOfExternalPortCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfExternalPortCapTable.setStatus("current")
_EndOfEciCap_Type = Integer32
_EndOfEciCap_Object = MibScalar
endOfEciCap = _EndOfEciCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 3, 10000),
    _EndOfEciCap_Type()
)
endOfEciCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEciCap.setStatus("current")
_ChangeServiceCap_ObjectIdentity = ObjectIdentity
changeServiceCap = _ChangeServiceCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5)
)
_ChangePhysicalPortServiceCapTable_Object = MibTable
changePhysicalPortServiceCapTable = _ChangePhysicalPortServiceCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1)
)
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTable.setStatus("current")
_ChangePhysicalPortServiceCapEntry_Object = MibTableRow
changePhysicalPortServiceCapEntry = _ChangePhysicalPortServiceCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1)
)
changePhysicalPortServiceCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapEntry.setStatus("current")
_ChangePhysicalPortServiceCapRowStatus_Type = FspR7RowStatusCaps
_ChangePhysicalPortServiceCapRowStatus_Object = MibTableColumn
changePhysicalPortServiceCapRowStatus = _ChangePhysicalPortServiceCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 1),
    _ChangePhysicalPortServiceCapRowStatus_Type()
)
changePhysicalPortServiceCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapRowStatus.setStatus("current")
_ChangePhysicalPortServiceCapType_Type = FspR7InterfaceTypeCaps
_ChangePhysicalPortServiceCapType_Object = MibTableColumn
changePhysicalPortServiceCapType = _ChangePhysicalPortServiceCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 2),
    _ChangePhysicalPortServiceCapType_Type()
)
changePhysicalPortServiceCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapType.setStatus("current")
_ChangePhysicalPortServiceCapAdmin_Type = FspR7AdminStateCaps
_ChangePhysicalPortServiceCapAdmin_Object = MibTableColumn
changePhysicalPortServiceCapAdmin = _ChangePhysicalPortServiceCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 3),
    _ChangePhysicalPortServiceCapAdmin_Type()
)
changePhysicalPortServiceCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapAdmin.setStatus("current")
_ChangePhysicalPortServiceCapAlias_Type = Integer32
_ChangePhysicalPortServiceCapAlias_Object = MibTableColumn
changePhysicalPortServiceCapAlias = _ChangePhysicalPortServiceCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 4),
    _ChangePhysicalPortServiceCapAlias_Type()
)
changePhysicalPortServiceCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapAlias.setStatus("current")
_ChangePhysicalPortServiceCapAlsMode_Type = FspR7AlsModeCaps
_ChangePhysicalPortServiceCapAlsMode_Object = MibTableColumn
changePhysicalPortServiceCapAlsMode = _ChangePhysicalPortServiceCapAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 5),
    _ChangePhysicalPortServiceCapAlsMode_Type()
)
changePhysicalPortServiceCapAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapAlsMode.setStatus("current")
_ChangePhysicalPortServiceCapBehaviour_Type = FspR7PortBehaviourCaps
_ChangePhysicalPortServiceCapBehaviour_Object = MibTableColumn
changePhysicalPortServiceCapBehaviour = _ChangePhysicalPortServiceCapBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 6),
    _ChangePhysicalPortServiceCapBehaviour_Type()
)
changePhysicalPortServiceCapBehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapBehaviour.setStatus("current")
_ChangePhysicalPortServiceCapDispersionSetting_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapDispersionSetting_Object = MibTableColumn
changePhysicalPortServiceCapDispersionSetting = _ChangePhysicalPortServiceCapDispersionSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 7),
    _ChangePhysicalPortServiceCapDispersionSetting_Type()
)
changePhysicalPortServiceCapDispersionSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapDispersionSetting.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapDispersionSetting.setUnits("ps/nm")
_ChangePhysicalPortServiceCapDispersionMode_Type = FspR7DispersionModesCaps
_ChangePhysicalPortServiceCapDispersionMode_Object = MibTableColumn
changePhysicalPortServiceCapDispersionMode = _ChangePhysicalPortServiceCapDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 8),
    _ChangePhysicalPortServiceCapDispersionMode_Type()
)
changePhysicalPortServiceCapDispersionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapDispersionMode.setStatus("current")
_ChangePhysicalPortServiceCapChannelProv_Type = FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapChannelProv_Object = MibTableColumn
changePhysicalPortServiceCapChannelProv = _ChangePhysicalPortServiceCapChannelProv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 9),
    _ChangePhysicalPortServiceCapChannelProv_Type()
)
changePhysicalPortServiceCapChannelProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapChannelProv.setStatus("current")
_ChangePhysicalPortServiceCapWdmRxChannel_Type = FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapWdmRxChannel_Object = MibTableColumn
changePhysicalPortServiceCapWdmRxChannel = _ChangePhysicalPortServiceCapWdmRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 10),
    _ChangePhysicalPortServiceCapWdmRxChannel_Type()
)
changePhysicalPortServiceCapWdmRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapWdmRxChannel.setStatus("current")
_ChangePhysicalPortServiceCapCodeGain_Type = FspR7CodeGainCaps
_ChangePhysicalPortServiceCapCodeGain_Object = MibTableColumn
changePhysicalPortServiceCapCodeGain = _ChangePhysicalPortServiceCapCodeGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 11),
    _ChangePhysicalPortServiceCapCodeGain_Type()
)
changePhysicalPortServiceCapCodeGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapCodeGain.setStatus("current")
_ChangePhysicalPortServiceCapXfpDecisionThres_Type = FspR7XfpDecisionThresCaps
_ChangePhysicalPortServiceCapXfpDecisionThres_Object = MibTableColumn
changePhysicalPortServiceCapXfpDecisionThres = _ChangePhysicalPortServiceCapXfpDecisionThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 12),
    _ChangePhysicalPortServiceCapXfpDecisionThres_Type()
)
changePhysicalPortServiceCapXfpDecisionThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapXfpDecisionThres.setStatus("current")
_ChangePhysicalPortServiceCapDisparityCorrection_Type = EnableStateCaps
_ChangePhysicalPortServiceCapDisparityCorrection_Object = MibTableColumn
changePhysicalPortServiceCapDisparityCorrection = _ChangePhysicalPortServiceCapDisparityCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 13),
    _ChangePhysicalPortServiceCapDisparityCorrection_Type()
)
changePhysicalPortServiceCapDisparityCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapDisparityCorrection.setStatus("current")
_ChangePhysicalPortServiceCapEqlzAdmin_Type = FspR7EqlzAdminStateCaps
_ChangePhysicalPortServiceCapEqlzAdmin_Object = MibTableColumn
changePhysicalPortServiceCapEqlzAdmin = _ChangePhysicalPortServiceCapEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 14),
    _ChangePhysicalPortServiceCapEqlzAdmin_Type()
)
changePhysicalPortServiceCapEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapEqlzAdmin.setStatus("current")
_ChangePhysicalPortServiceCapErrorForwarding_Type = FspR7ErrorFwdModeCaps
_ChangePhysicalPortServiceCapErrorForwarding_Object = MibTableColumn
changePhysicalPortServiceCapErrorForwarding = _ChangePhysicalPortServiceCapErrorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 15),
    _ChangePhysicalPortServiceCapErrorForwarding_Type()
)
changePhysicalPortServiceCapErrorForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapErrorForwarding.setStatus("current")
_ChangePhysicalPortServiceCapFecType_Type = FspR7FecTypeCaps
_ChangePhysicalPortServiceCapFecType_Object = MibTableColumn
changePhysicalPortServiceCapFecType = _ChangePhysicalPortServiceCapFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 16),
    _ChangePhysicalPortServiceCapFecType_Type()
)
changePhysicalPortServiceCapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapFecType.setStatus("current")
_ChangePhysicalPortServiceCapFarEndCommunication_Type = FspR7YesNoCaps
_ChangePhysicalPortServiceCapFarEndCommunication_Object = MibTableColumn
changePhysicalPortServiceCapFarEndCommunication = _ChangePhysicalPortServiceCapFarEndCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 17),
    _ChangePhysicalPortServiceCapFarEndCommunication_Type()
)
changePhysicalPortServiceCapFarEndCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapFarEndCommunication.setStatus("current")
_ChangePhysicalPortServiceCapFlowControl_Type = FspR7FlowControlModeCaps
_ChangePhysicalPortServiceCapFlowControl_Object = MibTableColumn
changePhysicalPortServiceCapFlowControl = _ChangePhysicalPortServiceCapFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 18),
    _ChangePhysicalPortServiceCapFlowControl_Type()
)
changePhysicalPortServiceCapFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapFlowControl.setStatus("current")
_ChangePhysicalPortServiceCapLaneChannelSetting_Type = FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapLaneChannelSetting_Object = MibTableColumn
changePhysicalPortServiceCapLaneChannelSetting = _ChangePhysicalPortServiceCapLaneChannelSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 19),
    _ChangePhysicalPortServiceCapLaneChannelSetting_Type()
)
changePhysicalPortServiceCapLaneChannelSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaneChannelSetting.setStatus("current")
_ChangePhysicalPortServiceCapLaserDelayTimer_Type = FspR7LaserDelayTimerCaps
_ChangePhysicalPortServiceCapLaserDelayTimer_Object = MibTableColumn
changePhysicalPortServiceCapLaserDelayTimer = _ChangePhysicalPortServiceCapLaserDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 20),
    _ChangePhysicalPortServiceCapLaserDelayTimer_Type()
)
changePhysicalPortServiceCapLaserDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserDelayTimer.setStatus("current")
_ChangePhysicalPortServiceCapLaserOffTimer_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapLaserOffTimer_Object = MibTableColumn
changePhysicalPortServiceCapLaserOffTimer = _ChangePhysicalPortServiceCapLaserOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 21),
    _ChangePhysicalPortServiceCapLaserOffTimer_Type()
)
changePhysicalPortServiceCapLaserOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserOffTimer.setUnits("ms")
_ChangePhysicalPortServiceCapLaserOnTimer_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapLaserOnTimer_Object = MibTableColumn
changePhysicalPortServiceCapLaserOnTimer = _ChangePhysicalPortServiceCapLaserOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 22),
    _ChangePhysicalPortServiceCapLaserOnTimer_Type()
)
changePhysicalPortServiceCapLaserOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserOnTimer.setUnits("ms")
_ChangePhysicalPortServiceCapLaserOffDelayFunction_Type = EnableStateCaps
_ChangePhysicalPortServiceCapLaserOffDelayFunction_Object = MibTableColumn
changePhysicalPortServiceCapLaserOffDelayFunction = _ChangePhysicalPortServiceCapLaserOffDelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 23),
    _ChangePhysicalPortServiceCapLaserOffDelayFunction_Type()
)
changePhysicalPortServiceCapLaserOffDelayFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapLaserOffDelayFunction.setStatus("current")
_ChangePhysicalPortServiceCapAutoPTassignment_Type = FspR7ManualAutoCaps
_ChangePhysicalPortServiceCapAutoPTassignment_Object = MibTableColumn
changePhysicalPortServiceCapAutoPTassignment = _ChangePhysicalPortServiceCapAutoPTassignment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 24),
    _ChangePhysicalPortServiceCapAutoPTassignment_Type()
)
changePhysicalPortServiceCapAutoPTassignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapAutoPTassignment.setStatus("current")
_ChangePhysicalPortServiceCapTributarySlotMethod_Type = FspR7ManualAutoCaps
_ChangePhysicalPortServiceCapTributarySlotMethod_Object = MibTableColumn
changePhysicalPortServiceCapTributarySlotMethod = _ChangePhysicalPortServiceCapTributarySlotMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 25),
    _ChangePhysicalPortServiceCapTributarySlotMethod_Type()
)
changePhysicalPortServiceCapTributarySlotMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTributarySlotMethod.setStatus("current")
_ChangePhysicalPortServiceCapOpticalSetPoint_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapOpticalSetPoint_Object = MibTableColumn
changePhysicalPortServiceCapOpticalSetPoint = _ChangePhysicalPortServiceCapOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 26),
    _ChangePhysicalPortServiceCapOpticalSetPoint_Type()
)
changePhysicalPortServiceCapOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapOpticalSetPoint.setUnits("0.1 dBm")
_ChangePhysicalPortServiceCapOpuPayloadType_Type = FspR7OpuPayloadTypeCaps
_ChangePhysicalPortServiceCapOpuPayloadType_Object = MibTableColumn
changePhysicalPortServiceCapOpuPayloadType = _ChangePhysicalPortServiceCapOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 27),
    _ChangePhysicalPortServiceCapOpuPayloadType_Type()
)
changePhysicalPortServiceCapOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapOpuPayloadType.setStatus("current")
_ChangePhysicalPortServiceCapSigDegThresSonetLine_Type = FspR7BERThresholdCaps
_ChangePhysicalPortServiceCapSigDegThresSonetLine_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresSonetLine = _ChangePhysicalPortServiceCapSigDegThresSonetLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 28),
    _ChangePhysicalPortServiceCapSigDegThresSonetLine_Type()
)
changePhysicalPortServiceCapSigDegThresSonetLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSonetLine.setStatus("current")
_ChangePhysicalPortServiceCapSigDegThresSdhMs_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThresSdhMs_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresSdhMs = _ChangePhysicalPortServiceCapSigDegThresSdhMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 29),
    _ChangePhysicalPortServiceCapSigDegThresSdhMs_Type()
)
changePhysicalPortServiceCapSigDegThresSdhMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSdhMs.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSdhMs.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresOtu_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOtu_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresOtu = _ChangePhysicalPortServiceCapSigDegThresOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 30),
    _ChangePhysicalPortServiceCapSigDegThresOtu_Type()
)
changePhysicalPortServiceCapSigDegThresOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOtu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOtu.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresOdu_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOdu_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresOdu = _ChangePhysicalPortServiceCapSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 31),
    _ChangePhysicalPortServiceCapSigDegThresOdu_Type()
)
changePhysicalPortServiceCapSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOdu.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThreshold_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThreshold_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThreshold = _ChangePhysicalPortServiceCapSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 32),
    _ChangePhysicalPortServiceCapSigDegThreshold_Type()
)
changePhysicalPortServiceCapSigDegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThreshold.setStatus("current")
_ChangePhysicalPortServiceCapSigDegPcslThreshold_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPcslThreshold_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPcslThreshold = _ChangePhysicalPortServiceCapSigDegPcslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 33),
    _ChangePhysicalPortServiceCapSigDegPcslThreshold_Type()
)
changePhysicalPortServiceCapSigDegPcslThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPcslThreshold.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPcslThreshold.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresSonetSection_Type = FspR7BERThresholdSectionCaps
_ChangePhysicalPortServiceCapSigDegThresSonetSection_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresSonetSection = _ChangePhysicalPortServiceCapSigDegThresSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 34),
    _ChangePhysicalPortServiceCapSigDegThresSonetSection_Type()
)
changePhysicalPortServiceCapSigDegThresSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSonetSection.setStatus("current")
_ChangePhysicalPortServiceCapSigDegThresSdhSection_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThresSdhSection_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresSdhSection = _ChangePhysicalPortServiceCapSigDegThresSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 35),
    _ChangePhysicalPortServiceCapSigDegThresSdhSection_Type()
)
changePhysicalPortServiceCapSigDegThresSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresSdhSection.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmA = _ChangePhysicalPortServiceCapSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 36),
    _ChangePhysicalPortServiceCapSigDegThresOduTcmA_Type()
)
changePhysicalPortServiceCapSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmA.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmB = _ChangePhysicalPortServiceCapSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 37),
    _ChangePhysicalPortServiceCapSigDegThresOduTcmB_Type()
)
changePhysicalPortServiceCapSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmB.setUnits("%")
_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Type = FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmC = _ChangePhysicalPortServiceCapSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 38),
    _ChangePhysicalPortServiceCapSigDegThresOduTcmC_Type()
)
changePhysicalPortServiceCapSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegThresOduTcmC.setUnits("%")
_ChangePhysicalPortServiceCapSignalDegradePeriod_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSignalDegradePeriod_Object = MibTableColumn
changePhysicalPortServiceCapSignalDegradePeriod = _ChangePhysicalPortServiceCapSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 39),
    _ChangePhysicalPortServiceCapSignalDegradePeriod_Type()
)
changePhysicalPortServiceCapSignalDegradePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSignalDegradePeriod.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodOdu_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOdu_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOdu = _ChangePhysicalPortServiceCapSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 40),
    _ChangePhysicalPortServiceCapSigDegPeriodOdu_Type()
)
changePhysicalPortServiceCapSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOdu.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodOtu_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOtu_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOtu = _ChangePhysicalPortServiceCapSigDegPeriodOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 41),
    _ChangePhysicalPortServiceCapSigDegPeriodOtu_Type()
)
changePhysicalPortServiceCapSigDegPeriodOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOtu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOtu.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodIntegration = _ChangePhysicalPortServiceCapSigDegPeriodIntegration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 42),
    _ChangePhysicalPortServiceCapSigDegPeriodIntegration_Type()
)
changePhysicalPortServiceCapSigDegPeriodIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodIntegration.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodIntegration.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodSdhSection = _ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 43),
    _ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Type()
)
changePhysicalPortServiceCapSigDegPeriodSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodSdhSection.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmA = _ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 44),
    _ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Type()
)
changePhysicalPortServiceCapSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmA.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmB = _ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 45),
    _ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Type()
)
changePhysicalPortServiceCapSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmB.setUnits("s")
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmC = _ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 46),
    _ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Type()
)
changePhysicalPortServiceCapSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapSigDegPeriodOduTcmC.setUnits("s")
_ChangePhysicalPortServiceCapOtnStuffing_Type = FspR7StuffCaps
_ChangePhysicalPortServiceCapOtnStuffing_Object = MibTableColumn
changePhysicalPortServiceCapOtnStuffing = _ChangePhysicalPortServiceCapOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 47),
    _ChangePhysicalPortServiceCapOtnStuffing_Type()
)
changePhysicalPortServiceCapOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapOtnStuffing.setStatus("current")
_ChangePhysicalPortServiceCapTcmALevel_Type = OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmALevel_Object = MibTableColumn
changePhysicalPortServiceCapTcmALevel = _ChangePhysicalPortServiceCapTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 48),
    _ChangePhysicalPortServiceCapTcmALevel_Type()
)
changePhysicalPortServiceCapTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTcmALevel.setStatus("current")
_ChangePhysicalPortServiceCapTcmBLevel_Type = OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmBLevel_Object = MibTableColumn
changePhysicalPortServiceCapTcmBLevel = _ChangePhysicalPortServiceCapTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 49),
    _ChangePhysicalPortServiceCapTcmBLevel_Type()
)
changePhysicalPortServiceCapTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTcmBLevel.setStatus("current")
_ChangePhysicalPortServiceCapTcmCLevel_Type = OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmCLevel_Object = MibTableColumn
changePhysicalPortServiceCapTcmCLevel = _ChangePhysicalPortServiceCapTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 50),
    _ChangePhysicalPortServiceCapTcmCLevel_Type()
)
changePhysicalPortServiceCapTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTcmCLevel.setStatus("current")
_ChangePhysicalPortServiceCapTerminationLevel_Type = OhTerminationLevelCaps
_ChangePhysicalPortServiceCapTerminationLevel_Object = MibTableColumn
changePhysicalPortServiceCapTerminationLevel = _ChangePhysicalPortServiceCapTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 51),
    _ChangePhysicalPortServiceCapTerminationLevel_Type()
)
changePhysicalPortServiceCapTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTerminationLevel.setStatus("current")
_ChangePhysicalPortServiceCapTimingSource_Type = SonetTimingSourceCaps
_ChangePhysicalPortServiceCapTimingSource_Object = MibTableColumn
changePhysicalPortServiceCapTimingSource = _ChangePhysicalPortServiceCapTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 52),
    _ChangePhysicalPortServiceCapTimingSource_Type()
)
changePhysicalPortServiceCapTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimingSource.setStatus("current")
_ChangePhysicalPortServiceCapTimModeOdu_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeOdu_Object = MibTableColumn
changePhysicalPortServiceCapTimModeOdu = _ChangePhysicalPortServiceCapTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 53),
    _ChangePhysicalPortServiceCapTimModeOdu_Type()
)
changePhysicalPortServiceCapTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeOdu.setStatus("current")
_ChangePhysicalPortServiceCapTimModeOtu_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeOtu_Object = MibTableColumn
changePhysicalPortServiceCapTimModeOtu = _ChangePhysicalPortServiceCapTimModeOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 54),
    _ChangePhysicalPortServiceCapTimModeOtu_Type()
)
changePhysicalPortServiceCapTimModeOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeOtu.setStatus("current")
_ChangePhysicalPortServiceCapTimModeSonetSection_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeSonetSection_Object = MibTableColumn
changePhysicalPortServiceCapTimModeSonetSection = _ChangePhysicalPortServiceCapTimModeSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 55),
    _ChangePhysicalPortServiceCapTimModeSonetSection_Type()
)
changePhysicalPortServiceCapTimModeSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeSonetSection.setStatus("current")
_ChangePhysicalPortServiceCapTimModeOduTcmA_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmA = _ChangePhysicalPortServiceCapTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 56),
    _ChangePhysicalPortServiceCapTimModeOduTcmA_Type()
)
changePhysicalPortServiceCapTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeOduTcmA.setStatus("current")
_ChangePhysicalPortServiceCapTimModeOduTcmB_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmB = _ChangePhysicalPortServiceCapTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 57),
    _ChangePhysicalPortServiceCapTimModeOduTcmB_Type()
)
changePhysicalPortServiceCapTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeOduTcmB.setStatus("current")
_ChangePhysicalPortServiceCapTimModeOduTcmC_Type = TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmC = _ChangePhysicalPortServiceCapTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 58),
    _ChangePhysicalPortServiceCapTimModeOduTcmC_Type()
)
changePhysicalPortServiceCapTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTimModeOduTcmC.setStatus("current")
_ChangePhysicalPortServiceCapTraceFormSonetSection_Type = SonetTraceFormCaps
_ChangePhysicalPortServiceCapTraceFormSonetSection_Object = MibTableColumn
changePhysicalPortServiceCapTraceFormSonetSection = _ChangePhysicalPortServiceCapTraceFormSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 59),
    _ChangePhysicalPortServiceCapTraceFormSonetSection_Type()
)
changePhysicalPortServiceCapTraceFormSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceFormSonetSection.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedSonetSection = _ChangePhysicalPortServiceCapTraceExpectedSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 60),
    _ChangePhysicalPortServiceCapTraceExpectedSonetSection_Type()
)
changePhysicalPortServiceCapTraceExpectedSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedSonetSection.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSonetSection = _ChangePhysicalPortServiceCapTraceTransmitSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 61),
    _ChangePhysicalPortServiceCapTraceTransmitSonetSection_Type()
)
changePhysicalPortServiceCapTraceTransmitSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSonetSection.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedOtu_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedOtu_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedOtu = _ChangePhysicalPortServiceCapTraceExpectedOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 62),
    _ChangePhysicalPortServiceCapTraceExpectedOtu_Type()
)
changePhysicalPortServiceCapTraceExpectedOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedOtu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOtu = _ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 63),
    _ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Type()
)
changePhysicalPortServiceCapTraceTransmitSapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSapiOtu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOtu = _ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 64),
    _ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Type()
)
changePhysicalPortServiceCapTraceTransmitDapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitDapiOtu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOtu = _ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 65),
    _ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Type()
)
changePhysicalPortServiceCapTraceTransmitOpspOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitOpspOtu.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedOdu_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedOdu_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedOdu = _ChangePhysicalPortServiceCapTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 66),
    _ChangePhysicalPortServiceCapTraceExpectedOdu_Type()
)
changePhysicalPortServiceCapTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedOdu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOdu = _ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 67),
    _ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Type()
)
changePhysicalPortServiceCapTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSapiOdu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOdu = _ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 68),
    _ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Type()
)
changePhysicalPortServiceCapTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitDapiOdu.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOdu = _ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 69),
    _ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Type()
)
changePhysicalPortServiceCapTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitOpspOdu.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmA = _ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 70),
    _ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Type()
)
changePhysicalPortServiceCapTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedOduTcmA.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmA = _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 71),
    _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Type()
)
changePhysicalPortServiceCapTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSapiOduTcmA.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmA = _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 72),
    _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Type()
)
changePhysicalPortServiceCapTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitDapiOduTcmA.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmA = _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 73),
    _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Type()
)
changePhysicalPortServiceCapTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitOpspOduTcmA.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmB = _ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 74),
    _ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Type()
)
changePhysicalPortServiceCapTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedOduTcmB.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmB = _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 75),
    _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Type()
)
changePhysicalPortServiceCapTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSapiOduTcmB.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmB = _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 76),
    _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Type()
)
changePhysicalPortServiceCapTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitDapiOduTcmB.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmB = _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 77),
    _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Type()
)
changePhysicalPortServiceCapTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitOpspOduTcmB.setStatus("current")
_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Type = Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmC = _ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 78),
    _ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Type()
)
changePhysicalPortServiceCapTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceExpectedOduTcmC.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmC = _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 79),
    _ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Type()
)
changePhysicalPortServiceCapTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitSapiOduTcmC.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmC = _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 80),
    _ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Type()
)
changePhysicalPortServiceCapTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitDapiOduTcmC.setStatus("current")
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Type = Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Object = MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmC = _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 81),
    _ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Type()
)
changePhysicalPortServiceCapTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTraceTransmitOpspOduTcmC.setStatus("current")
_ChangePhysicalPortServiceCapTxOffDelay_Type = FspR7EnableDisableCaps
_ChangePhysicalPortServiceCapTxOffDelay_Object = MibTableColumn
changePhysicalPortServiceCapTxOffDelay = _ChangePhysicalPortServiceCapTxOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 82),
    _ChangePhysicalPortServiceCapTxOffDelay_Type()
)
changePhysicalPortServiceCapTxOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOffDelay.setStatus("current")
_ChangePhysicalPortServiceCapVoaMode_Type = FspR7VoaModeCaps
_ChangePhysicalPortServiceCapVoaMode_Object = MibTableColumn
changePhysicalPortServiceCapVoaMode = _ChangePhysicalPortServiceCapVoaMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 83),
    _ChangePhysicalPortServiceCapVoaMode_Type()
)
changePhysicalPortServiceCapVoaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapVoaMode.setStatus("current")
_ChangePhysicalPortServiceCapVoaSetpoint_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapVoaSetpoint_Object = MibTableColumn
changePhysicalPortServiceCapVoaSetpoint = _ChangePhysicalPortServiceCapVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 84),
    _ChangePhysicalPortServiceCapVoaSetpoint_Type()
)
changePhysicalPortServiceCapVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapVoaSetpoint.setUnits("0.1 dB")
_ChangePhysicalPortServiceCapTxOffOnTm_Type = FspR7TxOffOnTmCaps
_ChangePhysicalPortServiceCapTxOffOnTm_Object = MibTableColumn
changePhysicalPortServiceCapTxOffOnTm = _ChangePhysicalPortServiceCapTxOffOnTm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 85),
    _ChangePhysicalPortServiceCapTxOffOnTm_Type()
)
changePhysicalPortServiceCapTxOffOnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOffOnTm.setStatus("current")
_ChangePhysicalPortServiceCapTxOffTimer_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapTxOffTimer_Object = MibTableColumn
changePhysicalPortServiceCapTxOffTimer = _ChangePhysicalPortServiceCapTxOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 86),
    _ChangePhysicalPortServiceCapTxOffTimer_Type()
)
changePhysicalPortServiceCapTxOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOffTimer.setUnits("ms")
_ChangePhysicalPortServiceCapTxOnTimer_Type = FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapTxOnTimer_Object = MibTableColumn
changePhysicalPortServiceCapTxOnTimer = _ChangePhysicalPortServiceCapTxOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 1, 1, 87),
    _ChangePhysicalPortServiceCapTxOnTimer_Type()
)
changePhysicalPortServiceCapTxOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceCapTxOnTimer.setUnits("ms")
_EndOfChangePhysicalPortServiceCapTable_Type = Integer32
_EndOfChangePhysicalPortServiceCapTable_Object = MibScalar
endOfChangePhysicalPortServiceCapTable = _EndOfChangePhysicalPortServiceCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 2),
    _EndOfChangePhysicalPortServiceCapTable_Type()
)
endOfChangePhysicalPortServiceCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfChangePhysicalPortServiceCapTable.setStatus("current")
_EndOfChangeServiceCap_Type = Integer32
_EndOfChangeServiceCap_Object = MibScalar
endOfChangeServiceCap = _EndOfChangeServiceCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 5, 10000),
    _EndOfChangeServiceCap_Type()
)
endOfChangeServiceCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfChangeServiceCap.setStatus("current")
_ProtectionCap_ObjectIdentity = ObjectIdentity
protectionCap = _ProtectionCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6)
)
_FfpCapTable_Object = MibTable
ffpCapTable = _FfpCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2)
)
if mibBuilder.loadTexts:
    ffpCapTable.setStatus("current")
_FfpCapEntry_Object = MibTableRow
ffpCapEntry = _FfpCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1)
)
ffpCapEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFfpShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpClassName"),
)
if mibBuilder.loadTexts:
    ffpCapEntry.setStatus("current")
_FfpCapRowStatus_Type = FspR7RowStatusCaps
_FfpCapRowStatus_Object = MibTableColumn
ffpCapRowStatus = _FfpCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 1),
    _FfpCapRowStatus_Type()
)
ffpCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapRowStatus.setStatus("current")
_FfpCapCreationMethod_Type = FfpTypeCaps
_FfpCapCreationMethod_Object = MibTableColumn
ffpCapCreationMethod = _FfpCapCreationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 2),
    _FfpCapCreationMethod_Type()
)
ffpCapCreationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapCreationMethod.setStatus("current")
_FfpCapSDswitching_Type = EnableStateCaps
_FfpCapSDswitching_Object = MibTableColumn
ffpCapSDswitching = _FfpCapSDswitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 3),
    _FfpCapSDswitching_Type()
)
ffpCapSDswitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapSDswitching.setStatus("current")
_FfpCapHoldOffTime_Type = ApsHoldoffTimeCaps
_FfpCapHoldOffTime_Object = MibTableColumn
ffpCapHoldOffTime = _FfpCapHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 4),
    _FfpCapHoldOffTime_Type()
)
ffpCapHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapHoldOffTime.setStatus("current")
_FfpCapProtectionMech_Type = ProtectionMechCaps
_FfpCapProtectionMech_Object = MibTableColumn
ffpCapProtectionMech = _FfpCapProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 5),
    _FfpCapProtectionMech_Type()
)
ffpCapProtectionMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapProtectionMech.setStatus("current")
_FfpCapWorkingAid_Type = SnmpAdminString
_FfpCapWorkingAid_Object = MibTableColumn
ffpCapWorkingAid = _FfpCapWorkingAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 6),
    _FfpCapWorkingAid_Type()
)
ffpCapWorkingAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapWorkingAid.setStatus("current")
_FfpCapProtectionAid_Type = SnmpAdminString
_FfpCapProtectionAid_Object = MibTableColumn
ffpCapProtectionAid = _FfpCapProtectionAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 7),
    _FfpCapProtectionAid_Type()
)
ffpCapProtectionAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapProtectionAid.setStatus("current")
_FfpCapSignalDegradeSwitching_Type = EnableStateCaps
_FfpCapSignalDegradeSwitching_Object = MibTableColumn
ffpCapSignalDegradeSwitching = _FfpCapSignalDegradeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 8),
    _FfpCapSignalDegradeSwitching_Type()
)
ffpCapSignalDegradeSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapSignalDegradeSwitching.setStatus("current")
_FfpCapFarEndIp_Type = FspR7YesNo
_FfpCapFarEndIp_Object = MibTableColumn
ffpCapFarEndIp = _FfpCapFarEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 9),
    _FfpCapFarEndIp_Type()
)
ffpCapFarEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapFarEndIp.setStatus("current")
_FfpCapPeerAid_Type = SnmpAdminString
_FfpCapPeerAid_Object = MibTableColumn
ffpCapPeerAid = _FfpCapPeerAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 10),
    _FfpCapPeerAid_Type()
)
ffpCapPeerAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapPeerAid.setStatus("current")
_FfpCapApsType_Type = ApsTypeCaps
_FfpCapApsType_Object = MibTableColumn
ffpCapApsType = _FfpCapApsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 11),
    _FfpCapApsType_Type()
)
ffpCapApsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapApsType.setStatus("current")
_FfpCapRevertMode_Type = ApsRevertModeCaps
_FfpCapRevertMode_Object = MibTableColumn
ffpCapRevertMode = _FfpCapRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 12),
    _FfpCapRevertMode_Type()
)
ffpCapRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapRevertMode.setStatus("current")
_FfpCapWaitToRestore_Type = FspR7Unsigned32Caps
_FfpCapWaitToRestore_Object = MibTableColumn
ffpCapWaitToRestore = _FfpCapWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 13),
    _FfpCapWaitToRestore_Type()
)
ffpCapWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    ffpCapWaitToRestore.setUnits("min")
_FfpCapDirection_Type = ApsDirectionCaps
_FfpCapDirection_Object = MibTableColumn
ffpCapDirection = _FfpCapDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 2, 1, 14),
    _FfpCapDirection_Type()
)
ffpCapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpCapDirection.setStatus("current")
_EndOfFfpCapTable_Type = Integer32
_EndOfFfpCapTable_Object = MibScalar
endOfFfpCapTable = _EndOfFfpCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 3),
    _EndOfFfpCapTable_Type()
)
endOfFfpCapTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFfpCapTable.setStatus("current")
_EndOfProtectionCap_Type = Integer32
_EndOfProtectionCap_Object = MibScalar
endOfProtectionCap = _EndOfProtectionCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 7, 6, 10000),
    _EndOfProtectionCap_Type()
)
endOfProtectionCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfProtectionCap.setStatus("current")
_ConformanceCap_ObjectIdentity = ObjectIdentity
conformanceCap = _ConformanceCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 10)
)
_CompliancesCap_ObjectIdentity = ObjectIdentity
compliancesCap = _CompliancesCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 10, 1)
)
_GroupsCap_ObjectIdentity = ObjectIdentity
groupsCap = _GroupsCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 10, 2)
)

# Managed Objects groups

objectGroupCap = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 10, 2, 1)
)
objectGroupCap.setObjects(
      *(("ADVA-FSPR7-CAP-MIB", "crossConnectionCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapAdmin"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapRedLineState"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapConn"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapAlias"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapPathNode"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapTunnelAid"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapRedLineState"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapConn"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapCrsType"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapAlias"),
        ("ADVA-FSPR7-CAP-MIB", "crossOpticalLineCapTunnelAid"),
        ("ADVA-FSPR7-CAP-MIB", "crossConnectionCapType"),
        ("ADVA-FSPR7-CAP-MIB", "physicalPortCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "physicalPortCapType"),
        ("ADVA-FSPR7-CAP-MIB", "physicalPortCapAdmin"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapChannelBand"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapType"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapAlias"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapAdmin"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapEqlzAdmin"),
        ("ADVA-FSPR7-CAP-MIB", "virtualPortCapInitEqlz"),
        ("ADVA-FSPR7-CAP-MIB", "optThresholdConfigCapLowConfig"),
        ("ADVA-FSPR7-CAP-MIB", "optThresholdConfigCapHighConfig"),
        ("ADVA-FSPR7-CAP-MIB", "oprThresholdConfigCapLowConfig"),
        ("ADVA-FSPR7-CAP-MIB", "oprThresholdConfigCapHighConfig"),
        ("ADVA-FSPR7-CAP-MIB", "terminationPointCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "terminationPointCapAdmin"),
        ("ADVA-FSPR7-CAP-MIB", "terminationPointCapFiberDetect"),
        ("ADVA-FSPR7-CAP-MIB", "terminationPointCapAlias"),
        ("ADVA-FSPR7-CAP-MIB", "connectionCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "connectionCapType"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapRowStatus"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapType"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapTransmitChannel"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapChannelBandwith"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapAlias"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapFarEndLocation"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapBitrate"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMaxChromDisperRcv"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMaxBitErrorRate"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapSourceProfile"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapFecType"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapLineCoding"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapFrameFormat"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapOpticalPowerTx"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapOsnrTransmit"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapPmdTransmit"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapChromDisperTx"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMinOsnrRcv"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMinOptPowerRcv"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMaxOptPowerRcv"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMaxPmdRcv"),
        ("ADVA-FSPR7-CAP-MIB", "externalPortCapMinChromDisperRcv"))
)
if mibBuilder.loadTexts:
    objectGroupCap.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

complianceCap = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 9, 10, 1, 1)
)
if mibBuilder.loadTexts:
    complianceCap.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSPR7-CAP-MIB",
    **{"advaFspR7Cap": advaFspR7Cap,
       "managementCap": managementCap,
       "specificMgmtCap": specificMgmtCap,
       "crossConnectionCapTable": crossConnectionCapTable,
       "crossConnectionCapEntry": crossConnectionCapEntry,
       "crossConnectionCapRowStatus": crossConnectionCapRowStatus,
       "crossConnectionCapAdmin": crossConnectionCapAdmin,
       "crossConnectionCapRedLineState": crossConnectionCapRedLineState,
       "crossConnectionCapConn": crossConnectionCapConn,
       "crossConnectionCapAlias": crossConnectionCapAlias,
       "crossConnectionCapPathNode": crossConnectionCapPathNode,
       "crossConnectionCapTunnelAid": crossConnectionCapTunnelAid,
       "crossConnectionCapType": crossConnectionCapType,
       "crossConnectionCapCrsFunction": crossConnectionCapCrsFunction,
       "crossConnectionCapCrsFromAidTwo": crossConnectionCapCrsFromAidTwo,
       "crossConnectionCapCrsToAidTwo": crossConnectionCapCrsToAidTwo,
       "crossConnectionCapCrsMcAidList": crossConnectionCapCrsMcAidList,
       "crossConnectionCapCrsContAidList": crossConnectionCapCrsContAidList,
       "crossConnectionCapCrsContAidListTwo": crossConnectionCapCrsContAidListTwo,
       "crossOpticalLineCapTable": crossOpticalLineCapTable,
       "crossOpticalLineCapEntry": crossOpticalLineCapEntry,
       "crossOpticalLineCapRowStatus": crossOpticalLineCapRowStatus,
       "crossOpticalLineCapRedLineState": crossOpticalLineCapRedLineState,
       "crossOpticalLineCapConn": crossOpticalLineCapConn,
       "crossOpticalLineCapCrsType": crossOpticalLineCapCrsType,
       "crossOpticalLineCapAlias": crossOpticalLineCapAlias,
       "crossOpticalLineCapTunnelAid": crossOpticalLineCapTunnelAid,
       "endOfCrossOpticalLineCapTable": endOfCrossOpticalLineCapTable,
       "crossDcnCapTable": crossDcnCapTable,
       "crossDcnCapEntry": crossDcnCapEntry,
       "crossDcnCapRowStatus": crossDcnCapRowStatus,
       "crossDcnCapType": crossDcnCapType,
       "crossDcnCapLink": crossDcnCapLink,
       "crossDcnCapEcc": crossDcnCapEcc,
       "endOfCrossDcnCapTable": endOfCrossDcnCapTable,
       "endOfSpecificMgmtCap": endOfSpecificMgmtCap,
       "eqptMgmtCap": eqptMgmtCap,
       "shelfCapTable": shelfCapTable,
       "shelfCapEntry": shelfCapEntry,
       "shelfCapRowStatus": shelfCapRowStatus,
       "shelfCapPsuOutputPower": shelfCapPsuOutputPower,
       "shelfCapType": shelfCapType,
       "shelfCapRack": shelfCapRack,
       "shelfCapSupply": shelfCapSupply,
       "shelfCapBandProvision": shelfCapBandProvision,
       "shelfCapAdmin": shelfCapAdmin,
       "shelfCapRackNumber": shelfCapRackNumber,
       "shelfCapRackOrder": shelfCapRackOrder,
       "shelfCapAlias": shelfCapAlias,
       "shelfCapSlot": shelfCapSlot,
       "endOfShelfCapTable": endOfShelfCapTable,
       "fanCapTable": fanCapTable,
       "fanCapEntry": fanCapEntry,
       "fanCapRowStatus": fanCapRowStatus,
       "fanCapForceDestroy": fanCapForceDestroy,
       "fanCapAdmin": fanCapAdmin,
       "fanCapType": fanCapType,
       "fanCapAlias": fanCapAlias,
       "fanCapOutputReset": fanCapOutputReset,
       "endOfFanCapTable": endOfFanCapTable,
       "plugCapTable": plugCapTable,
       "plugCapEntry": plugCapEntry,
       "plugCapRowStatus": plugCapRowStatus,
       "plugCapConnector": plugCapConnector,
       "plugCapType": plugCapType,
       "plugCapReach": plugCapReach,
       "plugCapLoopbackAttenuation": plugCapLoopbackAttenuation,
       "plugCapTransmitChannel": plugCapTransmitChannel,
       "plugCapAlias": plugCapAlias,
       "plugCapLaneGroup": plugCapLaneGroup,
       "plugCapMaxDataRate": plugCapMaxDataRate,
       "plugCapThirdPartyUsage": plugCapThirdPartyUsage,
       "plugCapAdmin": plugCapAdmin,
       "plugCapBidirectionalChannel": plugCapBidirectionalChannel,
       "plugCapChannelSpacingProvision": plugCapChannelSpacingProvision,
       "endOfPlugCapTable": endOfPlugCapTable,
       "moduleCapTable": moduleCapTable,
       "moduleCapEntry": moduleCapEntry,
       "moduleCapRowStatus": moduleCapRowStatus,
       "moduleCapForceDestroy": moduleCapForceDestroy,
       "moduleCapPsuOutputPower": moduleCapPsuOutputPower,
       "moduleCapPower": moduleCapPower,
       "moduleCapReach": moduleCapReach,
       "moduleCapInitEqlz": moduleCapInitEqlz,
       "moduleCapLanAid": moduleCapLanAid,
       "moduleCapType": moduleCapType,
       "moduleCapMapping": moduleCapMapping,
       "moduleCapGainRange": moduleCapGainRange,
       "moduleCapSfProvision": moduleCapSfProvision,
       "moduleCapCapabilityLevelProvision": moduleCapCapabilityLevelProvision,
       "moduleCapDCFiberType": moduleCapDCFiberType,
       "moduleCapChannelsProvision": moduleCapChannelsProvision,
       "moduleCapFiberDetect": moduleCapFiberDetect,
       "moduleCapSupply": moduleCapSupply,
       "moduleCapGroup": moduleCapGroup,
       "moduleCapDeploy": moduleCapDeploy,
       "moduleCapLagSysPrio": moduleCapLagSysPrio,
       "moduleCapTransmitChannel": moduleCapTransmitChannel,
       "moduleCapBand": moduleCapBand,
       "moduleCapTrafficDirection": moduleCapTrafficDirection,
       "moduleCapIpAddr": moduleCapIpAddr,
       "moduleCapDispersionCompensation": moduleCapDispersionCompensation,
       "moduleCapActivateDetect": moduleCapActivateDetect,
       "moduleCapOscUsage": moduleCapOscUsage,
       "moduleCapAdmin": moduleCapAdmin,
       "moduleCapScrambling": moduleCapScrambling,
       "moduleCapChannelsNumber": moduleCapChannelsNumber,
       "moduleCapChannelSpacingProvision": moduleCapChannelSpacingProvision,
       "moduleCapMode": moduleCapMode,
       "moduleCapSubBandProvision": moduleCapSubBandProvision,
       "moduleCapAlias": moduleCapAlias,
       "moduleCapFiberType": moduleCapFiberType,
       "moduleCapChannelSpacing": moduleCapChannelSpacing,
       "moduleCapOutputReset": moduleCapOutputReset,
       "moduleCapRoadmNumber": moduleCapRoadmNumber,
       "moduleCapTopology": moduleCapTopology,
       "moduleCapForceConfig": moduleCapForceConfig,
       "moduleCapMuxMethod": moduleCapMuxMethod,
       "moduleCapNdpCleanup": moduleCapNdpCleanup,
       "moduleCapRstp": moduleCapRstp,
       "moduleCapRemoteReset": moduleCapRemoteReset,
       "endOfModuleCap": endOfModuleCap,
       "protectionCableCapTable": protectionCableCapTable,
       "protectionCableCapEntry": protectionCableCapEntry,
       "protectionCableCapRowStatus": protectionCableCapRowStatus,
       "protectionCableCapType": protectionCableCapType,
       "endOfProtectionCableCap": endOfProtectionCableCap,
       "filterCableCapTable": filterCableCapTable,
       "filterCableCapEntry": filterCableCapEntry,
       "filterCableCapRowStatus": filterCableCapRowStatus,
       "filterCableCapType": filterCableCapType,
       "endOfFilterCableCap": endOfFilterCableCap,
       "endOfEqptMgmCap": endOfEqptMgmCap,
       "facilityMgmtCap": facilityMgmtCap,
       "physicalPortCapTable": physicalPortCapTable,
       "physicalPortCapEntry": physicalPortCapEntry,
       "physicalPortCapRowStatus": physicalPortCapRowStatus,
       "physicalPortCapType": physicalPortCapType,
       "physicalPortCapAdmin": physicalPortCapAdmin,
       "physicalPortCapAlias": physicalPortCapAlias,
       "physicalPortCapAlsMode": physicalPortCapAlsMode,
       "physicalPortCapAutoThresReset": physicalPortCapAutoThresReset,
       "physicalPortCapAutonegotiation": physicalPortCapAutonegotiation,
       "physicalPortCapBehaviour": physicalPortCapBehaviour,
       "physicalPortCapDispertionConfig": physicalPortCapDispertionConfig,
       "physicalPortCapDispersionSetting": physicalPortCapDispersionSetting,
       "physicalPortCapDispersionMode": physicalPortCapDispersionMode,
       "physicalPortCapChannelProv": physicalPortCapChannelProv,
       "physicalPortCapWdmRxChannel": physicalPortCapWdmRxChannel,
       "physicalPortCapCodeGain": physicalPortCapCodeGain,
       "physicalPortCapXfpDecisionThres": physicalPortCapXfpDecisionThres,
       "physicalPortCapDisparityCorrection": physicalPortCapDisparityCorrection,
       "physicalPortCapEqlzAdmin": physicalPortCapEqlzAdmin,
       "physicalPortCapErrorForwarding": physicalPortCapErrorForwarding,
       "physicalPortCapFecType": physicalPortCapFecType,
       "physicalPortCapFarEndCommunication": physicalPortCapFarEndCommunication,
       "physicalPortCapFlowControl": physicalPortCapFlowControl,
       "physicalPortCapForceLaserOn": physicalPortCapForceLaserOn,
       "physicalPortCapInhibitSwitchToProt": physicalPortCapInhibitSwitchToProt,
       "physicalPortCapInhibitSwitchToWork": physicalPortCapInhibitSwitchToWork,
       "physicalPortCapLaneChannelSetting": physicalPortCapLaneChannelSetting,
       "physicalPortCapLoopConfig": physicalPortCapLoopConfig,
       "physicalPortCapLaserDelayTimer": physicalPortCapLaserDelayTimer,
       "physicalPortCapLaserOffTimer": physicalPortCapLaserOffTimer,
       "physicalPortCapLaserOnTimer": physicalPortCapLaserOnTimer,
       "physicalPortCapLaserOffDelayFunction": physicalPortCapLaserOffDelayFunction,
       "physicalPortCapAutoPTassignment": physicalPortCapAutoPTassignment,
       "physicalPortCapTributarySlotMethod": physicalPortCapTributarySlotMethod,
       "physicalPortCapInitiateEqualization": physicalPortCapInitiateEqualization,
       "physicalPortCapLossAttenuation": physicalPortCapLossAttenuation,
       "physicalPortCapOpticalSetPoint": physicalPortCapOpticalSetPoint,
       "physicalPortCapDataLayerPmReset": physicalPortCapDataLayerPmReset,
       "physicalPortCapPrbsPmReset": physicalPortCapPrbsPmReset,
       "physicalPortCapTestPrbsRcvMode": physicalPortCapTestPrbsRcvMode,
       "physicalPortCapTestPrbsTrmtMode": physicalPortCapTestPrbsTrmtMode,
       "physicalPortCapSwitchCommand": physicalPortCapSwitchCommand,
       "physicalPortCapOpuPayloadType": physicalPortCapOpuPayloadType,
       "physicalPortCapSigDegThresSonetLine": physicalPortCapSigDegThresSonetLine,
       "physicalPortCapSigDegThresSdhMs": physicalPortCapSigDegThresSdhMs,
       "physicalPortCapSigDegThresOtu": physicalPortCapSigDegThresOtu,
       "physicalPortCapSigDegThresOdu": physicalPortCapSigDegThresOdu,
       "physicalPortCapSigDegThreshold": physicalPortCapSigDegThreshold,
       "physicalPortCapSigDegPcslThreshold": physicalPortCapSigDegPcslThreshold,
       "physicalPortCapSigDegThresSonetSection": physicalPortCapSigDegThresSonetSection,
       "physicalPortCapSigDegThresSdhSection": physicalPortCapSigDegThresSdhSection,
       "physicalPortCapSigDegThresOduTcmA": physicalPortCapSigDegThresOduTcmA,
       "physicalPortCapSigDegThresOduTcmB": physicalPortCapSigDegThresOduTcmB,
       "physicalPortCapSigDegThresOduTcmC": physicalPortCapSigDegThresOduTcmC,
       "physicalPortCapSignalDegradePeriod": physicalPortCapSignalDegradePeriod,
       "physicalPortCapSigDegPeriodOdu": physicalPortCapSigDegPeriodOdu,
       "physicalPortCapSigDegPeriodOtu": physicalPortCapSigDegPeriodOtu,
       "physicalPortCapSigDegPeriodIntegration": physicalPortCapSigDegPeriodIntegration,
       "physicalPortCapSigDegPeriodSdhSection": physicalPortCapSigDegPeriodSdhSection,
       "physicalPortCapSigDegPeriodOduTcmA": physicalPortCapSigDegPeriodOduTcmA,
       "physicalPortCapSigDegPeriodOduTcmB": physicalPortCapSigDegPeriodOduTcmB,
       "physicalPortCapSigDegPeriodOduTcmC": physicalPortCapSigDegPeriodOduTcmC,
       "physicalPortCapOtnStuffing": physicalPortCapOtnStuffing,
       "physicalPortCapTcmALevel": physicalPortCapTcmALevel,
       "physicalPortCapTcmBLevel": physicalPortCapTcmBLevel,
       "physicalPortCapTcmCLevel": physicalPortCapTcmCLevel,
       "physicalPortCapTerminationLevel": physicalPortCapTerminationLevel,
       "physicalPortCapTimingSource": physicalPortCapTimingSource,
       "physicalPortCapTimModeOdu": physicalPortCapTimModeOdu,
       "physicalPortCapTimModeOtu": physicalPortCapTimModeOtu,
       "physicalPortCapTimModeSonetSection": physicalPortCapTimModeSonetSection,
       "physicalPortCapTimModeOduTcmA": physicalPortCapTimModeOduTcmA,
       "physicalPortCapTimModeOduTcmB": physicalPortCapTimModeOduTcmB,
       "physicalPortCapTimModeOduTcmC": physicalPortCapTimModeOduTcmC,
       "physicalPortCapTraceFormSonetSection": physicalPortCapTraceFormSonetSection,
       "physicalPortCapTraceExpectedSonetSection": physicalPortCapTraceExpectedSonetSection,
       "physicalPortCapTraceTransmitSonetSection": physicalPortCapTraceTransmitSonetSection,
       "physicalPortCapTraceExpectedOtu": physicalPortCapTraceExpectedOtu,
       "physicalPortCapTraceTransmitSapiOtu": physicalPortCapTraceTransmitSapiOtu,
       "physicalPortCapTraceTransmitDapiOtu": physicalPortCapTraceTransmitDapiOtu,
       "physicalPortCapTraceTransmitOpspOtu": physicalPortCapTraceTransmitOpspOtu,
       "physicalPortCapTraceExpectedOdu": physicalPortCapTraceExpectedOdu,
       "physicalPortCapTraceTransmitSapiOdu": physicalPortCapTraceTransmitSapiOdu,
       "physicalPortCapTraceTransmitDapiOdu": physicalPortCapTraceTransmitDapiOdu,
       "physicalPortCapTraceTransmitOpspOdu": physicalPortCapTraceTransmitOpspOdu,
       "physicalPortCapTraceExpectedOduTcmA": physicalPortCapTraceExpectedOduTcmA,
       "physicalPortCapTraceTransmitSapiOduTcmA": physicalPortCapTraceTransmitSapiOduTcmA,
       "physicalPortCapTraceTransmitDapiOduTcmA": physicalPortCapTraceTransmitDapiOduTcmA,
       "physicalPortCapTraceTransmitOpspOduTcmA": physicalPortCapTraceTransmitOpspOduTcmA,
       "physicalPortCapTraceExpectedOduTcmB": physicalPortCapTraceExpectedOduTcmB,
       "physicalPortCapTraceTransmitSapiOduTcmB": physicalPortCapTraceTransmitSapiOduTcmB,
       "physicalPortCapTraceTransmitDapiOduTcmB": physicalPortCapTraceTransmitDapiOduTcmB,
       "physicalPortCapTraceTransmitOpspOduTcmB": physicalPortCapTraceTransmitOpspOduTcmB,
       "physicalPortCapTraceExpectedOduTcmC": physicalPortCapTraceExpectedOduTcmC,
       "physicalPortCapTraceTransmitSapiOduTcmC": physicalPortCapTraceTransmitSapiOduTcmC,
       "physicalPortCapTraceTransmitDapiOduTcmC": physicalPortCapTraceTransmitDapiOduTcmC,
       "physicalPortCapTraceTransmitOpspOduTcmC": physicalPortCapTraceTransmitOpspOduTcmC,
       "physicalPortCapTurnupConfig": physicalPortCapTurnupConfig,
       "physicalPortCapTxOffDelay": physicalPortCapTxOffDelay,
       "physicalPortCapVoaMode": physicalPortCapVoaMode,
       "physicalPortCapVoaSetpoint": physicalPortCapVoaSetpoint,
       "physicalPortCapLagPrio": physicalPortCapLagPrio,
       "physicalPortCapMaxFrameSize": physicalPortCapMaxFrameSize,
       "physicalPortCapPayload": physicalPortCapPayload,
       "physicalPortCapPortMode": physicalPortCapPortMode,
       "physicalPortCapPortRole": physicalPortCapPortRole,
       "physicalPortCapPriority": physicalPortCapPriority,
       "physicalPortCapPvid": physicalPortCapPvid,
       "physicalPortCapStagType": physicalPortCapStagType,
       "physicalPortCapUtag": physicalPortCapUtag,
       "physicalPortCapVethAid": physicalPortCapVethAid,
       "physicalPortCapRedLineState": physicalPortCapRedLineState,
       "physicalPortCapTunnelAid": physicalPortCapTunnelAid,
       "physicalPortCapRateLimit": physicalPortCapRateLimit,
       "physicalPortCapTxOffOnTm": physicalPortCapTxOffOnTm,
       "physicalPortCapTxOffTimer": physicalPortCapTxOffTimer,
       "physicalPortCapTxOnTimer": physicalPortCapTxOnTimer,
       "virtualPortCapTable": virtualPortCapTable,
       "virtualPortCapEntry": virtualPortCapEntry,
       "virtualPortCapRowStatus": virtualPortCapRowStatus,
       "virtualPortCapChannelBand": virtualPortCapChannelBand,
       "virtualPortCapType": virtualPortCapType,
       "virtualPortCapAlias": virtualPortCapAlias,
       "virtualPortCapAdmin": virtualPortCapAdmin,
       "virtualPortCapEqlzAdmin": virtualPortCapEqlzAdmin,
       "virtualPortCapInitEqlz": virtualPortCapInitEqlz,
       "virtualPortCapLacpMode": virtualPortCapLacpMode,
       "virtualPortCapLacpTimeout": virtualPortCapLacpTimeout,
       "virtualPortCapLagActivePorts": virtualPortCapLagActivePorts,
       "virtualPortCapMaxFrameSize": virtualPortCapMaxFrameSize,
       "virtualPortCapPortMode": virtualPortCapPortMode,
       "virtualPortCapDataLayerPmReset": virtualPortCapDataLayerPmReset,
       "virtualPortCapPortRole": virtualPortCapPortRole,
       "virtualPortCapLagPortType": virtualPortCapLagPortType,
       "virtualPortCapPriority": virtualPortCapPriority,
       "virtualPortCapPvid": virtualPortCapPvid,
       "virtualPortCapRevertiveMode": virtualPortCapRevertiveMode,
       "virtualPortCapStagType": virtualPortCapStagType,
       "virtualPortCapUtag": virtualPortCapUtag,
       "virtualPortCapBundle": virtualPortCapBundle,
       "virtualPortCapSwitchCommand": virtualPortCapSwitchCommand,
       "virtualPortCapInhibitSwitchToWork": virtualPortCapInhibitSwitchToWork,
       "virtualPortCapInhibitSwitchToProt": virtualPortCapInhibitSwitchToProt,
       "virtualPortCapOduTribPortNo": virtualPortCapOduTribPortNo,
       "virtualPortCapOduTribTimeSlottNo": virtualPortCapOduTribTimeSlottNo,
       "virtualPortCapSigDegThresOdu": virtualPortCapSigDegThresOdu,
       "virtualPortCapSigDegPeriodOdu": virtualPortCapSigDegPeriodOdu,
       "virtualPortCapTraceExpectedOdu": virtualPortCapTraceExpectedOdu,
       "virtualPortCapTraceTransmitSapiOdu": virtualPortCapTraceTransmitSapiOdu,
       "virtualPortCapTraceTransmitDapiOdu": virtualPortCapTraceTransmitDapiOdu,
       "virtualPortCapTraceTransmitOpspOdu": virtualPortCapTraceTransmitOpspOdu,
       "virtualPortCapTimModeOdu": virtualPortCapTimModeOdu,
       "virtualPortCapSigDegThresOduTcmA": virtualPortCapSigDegThresOduTcmA,
       "virtualPortCapSigDegPeriodOduTcmA": virtualPortCapSigDegPeriodOduTcmA,
       "virtualPortCapSigDegThresOduTcmB": virtualPortCapSigDegThresOduTcmB,
       "virtualPortCapSigDegPeriodOduTcmB": virtualPortCapSigDegPeriodOduTcmB,
       "virtualPortCapSigDegThresOduTcmC": virtualPortCapSigDegThresOduTcmC,
       "virtualPortCapSigDegPeriodOduTcmC": virtualPortCapSigDegPeriodOduTcmC,
       "virtualPortCapTcmALevel": virtualPortCapTcmALevel,
       "virtualPortCapTcmBLevel": virtualPortCapTcmBLevel,
       "virtualPortCapTcmCLevel": virtualPortCapTcmCLevel,
       "virtualPortCapTraceTransmitSapiOduTcmA": virtualPortCapTraceTransmitSapiOduTcmA,
       "virtualPortCapTraceTransmitDapiOduTcmA": virtualPortCapTraceTransmitDapiOduTcmA,
       "virtualPortCapTraceTransmitOpspOduTcmA": virtualPortCapTraceTransmitOpspOduTcmA,
       "virtualPortCapTraceExpectedOduTcmA": virtualPortCapTraceExpectedOduTcmA,
       "virtualPortCapTimModeOduTcmA": virtualPortCapTimModeOduTcmA,
       "virtualPortCapTraceExpectedOduTcmB": virtualPortCapTraceExpectedOduTcmB,
       "virtualPortCapTraceTransmitSapiOduTcmB": virtualPortCapTraceTransmitSapiOduTcmB,
       "virtualPortCapTraceTransmitDapiOduTcmB": virtualPortCapTraceTransmitDapiOduTcmB,
       "virtualPortCapTraceTransmitOpspOduTcmB": virtualPortCapTraceTransmitOpspOduTcmB,
       "virtualPortCapTimModeOduTcmB": virtualPortCapTimModeOduTcmB,
       "virtualPortCapTraceExpectedOduTcmC": virtualPortCapTraceExpectedOduTcmC,
       "virtualPortCapTraceTransmitSapiOduTcmC": virtualPortCapTraceTransmitSapiOduTcmC,
       "virtualPortCapTraceTransmitDapiOduTcmC": virtualPortCapTraceTransmitDapiOduTcmC,
       "virtualPortCapTraceTransmitOpspOduTcmC": virtualPortCapTraceTransmitOpspOduTcmC,
       "virtualPortCapTimModeOduTcmC": virtualPortCapTimModeOduTcmC,
       "virtualPortCapTerminationLevel": virtualPortCapTerminationLevel,
       "virtualPortCapLoopConfig": virtualPortCapLoopConfig,
       "virtualPortCapVcType": virtualPortCapVcType,
       "virtualPortCapCir": virtualPortCapCir,
       "virtualPortCapOpuPayloadType": virtualPortCapOpuPayloadType,
       "virtualPortCapOtnStuffing": virtualPortCapOtnStuffing,
       "virtualPortCapRedLineState": virtualPortCapRedLineState,
       "virtualPortCapTunnelAid": virtualPortCapTunnelAid,
       "virtualPortCapTrafficDirection": virtualPortCapTrafficDirection,
       "virtualPortCapChannelId": virtualPortCapChannelId,
       "endOfVirtualPortCapTable": endOfVirtualPortCapTable,
       "endOfFacilityMgmtCap": endOfFacilityMgmtCap,
       "dcnMgmtCap": dcnMgmtCap,
       "linkCapTable": linkCapTable,
       "linkCapEntry": linkCapEntry,
       "linkCapRowStatus": linkCapRowStatus,
       "linkCapType": linkCapType,
       "linkCapAdmin": linkCapAdmin,
       "linkCapAlias": linkCapAlias,
       "linkCapAuthString": linkCapAuthString,
       "linkCapProxyArp": linkCapProxyArp,
       "linkCapOspf": linkCapOspf,
       "linkCapBaud": linkCapBaud,
       "linkCapAuthType": linkCapAuthType,
       "linkCapIpType": linkCapIpType,
       "linkCapMetric": linkCapMetric,
       "linkCapAreaAid": linkCapAreaAid,
       "linkCapNearEndIp": linkCapNearEndIp,
       "linkCapBitrate": linkCapBitrate,
       "linkCapIPv6Type": linkCapIPv6Type,
       "linkCapNendIPv6": linkCapNendIPv6,
       "endOfLinkCapTable": endOfLinkCapTable,
       "scCapTable": scCapTable,
       "scCapEntry": scCapEntry,
       "scCapRowStatus": scCapRowStatus,
       "scCapType": scCapType,
       "scCapAdmin": scCapAdmin,
       "scCapAlias": scCapAlias,
       "scCapAuthString": scCapAuthString,
       "scCapOspf": scCapOspf,
       "scCapAuthType": scCapAuthType,
       "scCapIpType": scCapIpType,
       "scCapMetric": scCapMetric,
       "scCapAreaAid": scCapAreaAid,
       "scCapAlsMode": scCapAlsMode,
       "scCapSigDegThresReceiver": scCapSigDegThresReceiver,
       "scCapAutonegotiation": scCapAutonegotiation,
       "scCapBitrate": scCapBitrate,
       "scCapDuplex": scCapDuplex,
       "scCapAttGradientTh": scCapAttGradientTh,
       "scCapIpAddr": scCapIpAddr,
       "scCapLanAid": scCapLanAid,
       "scCapIpMask": scCapIpMask,
       "scCapDataLayerPmReset": scCapDataLayerPmReset,
       "scCapPriority": scCapPriority,
       "scCapIPv6": scCapIPv6,
       "scCapIPv6PrefixLen": scCapIPv6PrefixLen,
       "scCapIpMode": scCapIpMode,
       "scCapGatewayProxyArp": scCapGatewayProxyArp,
       "endOfScCapTable": endOfScCapTable,
       "lanCapTable": lanCapTable,
       "lanCapEntry": lanCapEntry,
       "lanCapRowStatus": lanCapRowStatus,
       "lanCapType": lanCapType,
       "lanCapAdmin": lanCapAdmin,
       "lanCapAlias": lanCapAlias,
       "lanCapAuthString": lanCapAuthString,
       "lanCapOspf": lanCapOspf,
       "lanCapAuthType": lanCapAuthType,
       "lanCapIpType": lanCapIpType,
       "lanCapMetric": lanCapMetric,
       "lanCapAreaAid": lanCapAreaAid,
       "lanCapIpAddr": lanCapIpAddr,
       "lanCapIpMask": lanCapIpMask,
       "lanCapPriority": lanCapPriority,
       "lanCapIPv6": lanCapIPv6,
       "lanCapIPv6PrefixLen": lanCapIPv6PrefixLen,
       "lanCapIpMode": lanCapIpMode,
       "endOfLanCapTable": endOfLanCapTable,
       "eccCapTable": eccCapTable,
       "eccCapEntry": eccCapEntry,
       "eccCapRowStatus": eccCapRowStatus,
       "eccCapType": eccCapType,
       "eccCapAdmin": eccCapAdmin,
       "eccCapAlias": eccCapAlias,
       "eccCapLanAid": eccCapLanAid,
       "eccCapExternalVid": eccCapExternalVid,
       "endOfEccCapTable": endOfEccCapTable,
       "endOfDcnMgmtCap": endOfDcnMgmtCap,
       "opticalMuxMgmtCap": opticalMuxMgmtCap,
       "opticalMuxCapTable": opticalMuxCapTable,
       "opticalMuxCapEntry": opticalMuxCapEntry,
       "opticalMuxCapRowStatus": opticalMuxCapRowStatus,
       "opticalMuxCapPumpPower": opticalMuxCapPumpPower,
       "opticalMuxCapInhibitSwitchToWork": opticalMuxCapInhibitSwitchToWork,
       "opticalMuxCapForceLaserOn": opticalMuxCapForceLaserOn,
       "opticalMuxCapAseTabCreation": opticalMuxCapAseTabCreation,
       "opticalMuxCapOpticalSetPoint": opticalMuxCapOpticalSetPoint,
       "opticalMuxCapInitiateEqualization": opticalMuxCapInitiateEqualization,
       "opticalMuxCapTilt": opticalMuxCapTilt,
       "opticalMuxCapOscOpticalSetpoint": opticalMuxCapOscOpticalSetpoint,
       "opticalMuxCapOffset": opticalMuxCapOffset,
       "opticalMuxCapSwitchCommand": opticalMuxCapSwitchCommand,
       "opticalMuxCapAlsMode": opticalMuxCapAlsMode,
       "opticalMuxCapType": opticalMuxCapType,
       "opticalMuxCapAttenuationGradient": opticalMuxCapAttenuationGradient,
       "opticalMuxCapInhibitSwitchToProt": opticalMuxCapInhibitSwitchToProt,
       "opticalMuxCapVariableGain": opticalMuxCapVariableGain,
       "opticalMuxCapAdmin": opticalMuxCapAdmin,
       "opticalMuxCapTimePeriod": opticalMuxCapTimePeriod,
       "opticalMuxCapSigDegThresReceiver": opticalMuxCapSigDegThresReceiver,
       "opticalMuxCapAlias": opticalMuxCapAlias,
       "opticalMuxCapDataLayerPmReset": opticalMuxCapDataLayerPmReset,
       "opticalMuxCapGain": opticalMuxCapGain,
       "opticalMuxCapEdfaPwrOut": opticalMuxCapEdfaPwrOut,
       "opticalMuxCapVoaSetpoint": opticalMuxCapVoaSetpoint,
       "opticalMuxCapFiberBrand": opticalMuxCapFiberBrand,
       "opticalMuxCapTiltSet": opticalMuxCapTiltSet,
       "opticalMuxCapForceFwdAsePilotOn": opticalMuxCapForceFwdAsePilotOn,
       "opticalMuxCapBandProvision": opticalMuxCapBandProvision,
       "opticalMuxCapOffsetHigh": opticalMuxCapOffsetHigh,
       "opticalMuxCapOffsetLow": opticalMuxCapOffsetLow,
       "opticalMuxCapOptUpdate": opticalMuxCapOptUpdate,
       "endOfOpticalMuxCapTable": endOfOpticalMuxCapTable,
       "endOfOpticalMuxMgmtCap": endOfOpticalMuxMgmtCap,
       "shelfConnMgmtCap": shelfConnMgmtCap,
       "shelfConnCapTable": shelfConnCapTable,
       "shelfConnCapEntry": shelfConnCapEntry,
       "shelfConnCapRowStatus": shelfConnCapRowStatus,
       "shelfConnCapAdmin": shelfConnCapAdmin,
       "shelfConnCapAlias": shelfConnCapAlias,
       "shelfConnCapFacilityType": shelfConnCapFacilityType,
       "endOfShelfConnCapTable": endOfShelfConnCapTable,
       "endOfShelfConnMgmtCap": endOfShelfConnMgmtCap,
       "envMgmtCap": envMgmtCap,
       "envPortCapTable": envPortCapTable,
       "envPortCapEntry": envPortCapEntry,
       "envPortCapRowStatus": envPortCapRowStatus,
       "envPortCapTelemetry": envPortCapTelemetry,
       "envPortCapFacilityType": envPortCapFacilityType,
       "envPortCapTifAlarmType": envPortCapTifAlarmType,
       "envPortCapTifAlarmMessage": envPortCapTifAlarmMessage,
       "envPortCapInvertTifInputLogic": envPortCapInvertTifInputLogic,
       "endOfEnvPortCapTable": endOfEnvPortCapTable,
       "endOfEnvMgmtCap": endOfEnvMgmtCap,
       "containerMgmtCap": containerMgmtCap,
       "containerCapTable": containerCapTable,
       "containerCapEntry": containerCapEntry,
       "containerCapRowStatus": containerCapRowStatus,
       "containerCapFacilityType": containerCapFacilityType,
       "endOfContainerCapTable": endOfContainerCapTable,
       "endOfContainerMgmtCap": endOfContainerMgmtCap,
       "opticalLineMgmtCap": opticalLineMgmtCap,
       "opticalLineCapTable": opticalLineCapTable,
       "opticalLineCapEntry": opticalLineCapEntry,
       "opticalLineCapRowStatus": opticalLineCapRowStatus,
       "opticalLineCapTxLineAttenuation": opticalLineCapTxLineAttenuation,
       "opticalLineCapRxLineAttenuation": opticalLineCapRxLineAttenuation,
       "opticalLineCapAlias": opticalLineCapAlias,
       "opticalLineCapFarEndLocation": opticalLineCapFarEndLocation,
       "endOfOpticalLineCapTable": endOfOpticalLineCapTable,
       "endOfOpticalLineMgmtCap": endOfOpticalLineMgmtCap,
       "endOfManagementCap": endOfManagementCap,
       "performanceCap": performanceCap,
       "performanceFacilityCap": performanceFacilityCap,
       "performanceFacilityThresholdCap": performanceFacilityThresholdCap,
       "optThresholdConfigCapTable": optThresholdConfigCapTable,
       "optThresholdConfigCapEntry": optThresholdConfigCapEntry,
       "optThresholdConfigCapLowConfig": optThresholdConfigCapLowConfig,
       "optThresholdConfigCapHighConfig": optThresholdConfigCapHighConfig,
       "oprThresholdConfigCapTable": oprThresholdConfigCapTable,
       "oprThresholdConfigCapEntry": oprThresholdConfigCapEntry,
       "oprThresholdConfigCapLowConfig": oprThresholdConfigCapLowConfig,
       "oprThresholdConfigCapHighConfig": oprThresholdConfigCapHighConfig,
       "endOfOprThresholdConfigCapTable": endOfOprThresholdConfigCapTable,
       "endOfPerformanceFacilityThresholdCap": endOfPerformanceFacilityThresholdCap,
       "endOfPerformanceFacilityCap": endOfPerformanceFacilityCap,
       "pmEqptCap": pmEqptCap,
       "pmDcnCap": pmDcnCap,
       "pmDcnDataCap": pmDcnDataCap,
       "pmDcnPhysicalCap": pmDcnPhysicalCap,
       "pmDcnPhysThresholdCap": pmDcnPhysThresholdCap,
       "dcnPhysThresholdCapTable": dcnPhysThresholdCapTable,
       "dcnPhysThresholdCapEntry": dcnPhysThresholdCapEntry,
       "dcnPhysThresholdCapOprLow": dcnPhysThresholdCapOprLow,
       "dcnPhysThresholdCapOprHigh": dcnPhysThresholdCapOprHigh,
       "dcnPhysThresholdCapAttRcvLow": dcnPhysThresholdCapAttRcvLow,
       "dcnPhysThresholdCapAttRcvHigh": dcnPhysThresholdCapAttRcvHigh,
       "endOfDcnPhysThresholdCapTable": endOfDcnPhysThresholdCapTable,
       "endOfPmDcnPhysThresholdCap": endOfPmDcnPhysThresholdCap,
       "endOfPmDcnPhysicalCap": endOfPmDcnPhysicalCap,
       "endOfPmDcnCap": endOfPmDcnCap,
       "pmFacilityCap": pmFacilityCap,
       "pmFacilityDataCap": pmFacilityDataCap,
       "pmFacilityDataThresholdCap": pmFacilityDataThresholdCap,
       "oduFacilityDataThresholdCapTable": oduFacilityDataThresholdCapTable,
       "oduFacilityDataThresholdCapEntry": oduFacilityDataThresholdCapEntry,
       "oduFacilityDataThresholdCapESHighThres15min": oduFacilityDataThresholdCapESHighThres15min,
       "oduFacilityDataThresholdCapESHighThres1day": oduFacilityDataThresholdCapESHighThres1day,
       "oduFacilityDataThresholdCapSESHighThres15min": oduFacilityDataThresholdCapSESHighThres15min,
       "oduFacilityDataThresholdCapSESHighThres1day": oduFacilityDataThresholdCapSESHighThres1day,
       "oduFacilityDataThresholdCapBbeHighThres15min": oduFacilityDataThresholdCapBbeHighThres15min,
       "oduFacilityDataThresholdCapBbeHighThres1day": oduFacilityDataThresholdCapBbeHighThres1day,
       "oduFacilityDataThresholdCapUASHighThres15min": oduFacilityDataThresholdCapUASHighThres15min,
       "oduFacilityDataThresholdCapUASHighThres1day": oduFacilityDataThresholdCapUASHighThres1day,
       "endOfOduFacilityDataThresholdCapTable": endOfOduFacilityDataThresholdCapTable,
       "tcmAFacilityDataThresholdCapTable": tcmAFacilityDataThresholdCapTable,
       "tcmAFacilityDataThresholdCapEntry": tcmAFacilityDataThresholdCapEntry,
       "tcmAFacilityDataThresholdCapESHighThres15min": tcmAFacilityDataThresholdCapESHighThres15min,
       "tcmAFacilityDataThresholdCapESHighThres1day": tcmAFacilityDataThresholdCapESHighThres1day,
       "tcmAFacilityDataThresholdCapSESHighThres15min": tcmAFacilityDataThresholdCapSESHighThres15min,
       "tcmAFacilityDataThresholdCapSESHighThres1day": tcmAFacilityDataThresholdCapSESHighThres1day,
       "tcmAFacilityDataThresholdCapBbeHighThres15min": tcmAFacilityDataThresholdCapBbeHighThres15min,
       "tcmAFacilityDataThresholdCapBbeHighThres1day": tcmAFacilityDataThresholdCapBbeHighThres1day,
       "tcmAFacilityDataThresholdCapUASHighThres15min": tcmAFacilityDataThresholdCapUASHighThres15min,
       "tcmAFacilityDataThresholdCapUASHighThres1day": tcmAFacilityDataThresholdCapUASHighThres1day,
       "endOfTcmAFacilityDataThresholdCapTable": endOfTcmAFacilityDataThresholdCapTable,
       "tcmBFacilityDataThresholdCapTable": tcmBFacilityDataThresholdCapTable,
       "tcmBFacilityDataThresholdCapEntry": tcmBFacilityDataThresholdCapEntry,
       "tcmBFacilityDataThresholdCapBESHighThres15min": tcmBFacilityDataThresholdCapBESHighThres15min,
       "tcmBFacilityDataThresholdCapESHighThres1day": tcmBFacilityDataThresholdCapESHighThres1day,
       "tcmBFacilityDataThresholdCapSESHighThres15min": tcmBFacilityDataThresholdCapSESHighThres15min,
       "tcmBFacilityDataThresholdCapSESHighThres1day": tcmBFacilityDataThresholdCapSESHighThres1day,
       "tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min": tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min,
       "tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day": tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day,
       "tcmBFacilityDataThresholdCapUASHighThres15min": tcmBFacilityDataThresholdCapUASHighThres15min,
       "tcmBFacilityDataThresholdCapUASHighThres1day": tcmBFacilityDataThresholdCapUASHighThres1day,
       "endOfTcmBFacilityDataThresholdCapTable": endOfTcmBFacilityDataThresholdCapTable,
       "tcmCFacilityDataThresholdCapTable": tcmCFacilityDataThresholdCapTable,
       "tcmCFacilityDataThresholdCapEntry": tcmCFacilityDataThresholdCapEntry,
       "tcmCFacilityDataThresholdCapBESHighThres15min": tcmCFacilityDataThresholdCapBESHighThres15min,
       "tcmCFacilityDataThresholdCapESHighThres1day": tcmCFacilityDataThresholdCapESHighThres1day,
       "tcmCFacilityDataThresholdCapSESHighThres15min": tcmCFacilityDataThresholdCapSESHighThres15min,
       "tcmCFacilityDataThresholdCapSESHighThres1day": tcmCFacilityDataThresholdCapSESHighThres1day,
       "tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min": tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min,
       "tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day": tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day,
       "tcmCFacilityDataThresholdCapUASHighThres15min": tcmCFacilityDataThresholdCapUASHighThres15min,
       "tcmCFacilityDataThresholdCapUASHighThres1day": tcmCFacilityDataThresholdCapUASHighThres1day,
       "endOfTcmCFacilityDataThresholdCapTable": endOfTcmCFacilityDataThresholdCapTable,
       "otuFacilityDataThresholdCapTable": otuFacilityDataThresholdCapTable,
       "otuFacilityDataThresholdCapEntry": otuFacilityDataThresholdCapEntry,
       "otuFacilityDataThresholdCapESHighThres15min": otuFacilityDataThresholdCapESHighThres15min,
       "otuFacilityDataThresholdCapESHighThres1day": otuFacilityDataThresholdCapESHighThres1day,
       "otuFacilityDataThresholdCapSESHighThres15min": otuFacilityDataThresholdCapSESHighThres15min,
       "otuFacilityDataThresholdCapSESHighThres1day": otuFacilityDataThresholdCapSESHighThres1day,
       "otuFacilityDataThresholdCapBbeHighThres15min": otuFacilityDataThresholdCapBbeHighThres15min,
       "otuFacilityDataThresholdCapBbeHighThres1day": otuFacilityDataThresholdCapBbeHighThres1day,
       "otuFacilityDataThresholdCapUASHighThres15min": otuFacilityDataThresholdCapUASHighThres15min,
       "otuFacilityDataThresholdCapUASHighThres1day": otuFacilityDataThresholdCapUASHighThres1day,
       "endOfOtuFacilityDataThresholdCapTable": endOfOtuFacilityDataThresholdCapTable,
       "otuFecFacilityDataThresholdCapTable": otuFecFacilityDataThresholdCapTable,
       "otuFecFacilityDataThresholdCapEntry": otuFecFacilityDataThresholdCapEntry,
       "otuFecFacilityDataThresholdCapESHighThres15min": otuFecFacilityDataThresholdCapESHighThres15min,
       "otuFecFacilityDataThresholdCapESHighThres1day": otuFecFacilityDataThresholdCapESHighThres1day,
       "otuFecFacilityDataThresholdCapSESHighThres15min": otuFecFacilityDataThresholdCapSESHighThres15min,
       "otuFecFacilityDataThresholdCapSESHighThres1day": otuFecFacilityDataThresholdCapSESHighThres1day,
       "otuFecFacilityDataThresholdCapUBEHighThres15min": otuFecFacilityDataThresholdCapUBEHighThres15min,
       "otuFecFacilityDataThresholdCapUBEHighThres1day": otuFecFacilityDataThresholdCapUBEHighThres1day,
       "otuFecFacilityDataThresholdCapCErrHighThres15min": otuFecFacilityDataThresholdCapCErrHighThres15min,
       "otuFecFacilityDataThresholdCapCErrHighThres1day": otuFecFacilityDataThresholdCapCErrHighThres1day,
       "otuFecFacilityDataThresholdCapBERCErrHighThres15min": otuFecFacilityDataThresholdCapBERCErrHighThres15min,
       "otuFecFacilityDataThresholdCapBERCErrHighThres1day": otuFecFacilityDataThresholdCapBERCErrHighThres1day,
       "endOfOtuFecFacilityDataThresholdCapTable": endOfOtuFecFacilityDataThresholdCapTable,
       "fecFacilityDataThresholdCapTable": fecFacilityDataThresholdCapTable,
       "fecFacilityDataThresholdCapEntry": fecFacilityDataThresholdCapEntry,
       "fecFacilityDataThresholdCapCEHighThres15min": fecFacilityDataThresholdCapCEHighThres15min,
       "fecFacilityDataThresholdCapCEHighThres1day": fecFacilityDataThresholdCapCEHighThres1day,
       "fecFacilityDataThresholdCapUBEHighThres15min": fecFacilityDataThresholdCapUBEHighThres15min,
       "fecFacilityDataThresholdCapUBEHighThres1day": fecFacilityDataThresholdCapUBEHighThres1day,
       "endOfFecFacilityDataThresholdCapTable": endOfFecFacilityDataThresholdCapTable,
       "pcs2FacilityDataThresholdCapTable": pcs2FacilityDataThresholdCapTable,
       "pcs2FacilityDataThresholdCapEntry": pcs2FacilityDataThresholdCapEntry,
       "pcs2FacilityDataThresholdCapESHighThres15min": pcs2FacilityDataThresholdCapESHighThres15min,
       "pcs2FacilityDataThresholdCapESHighThres1day": pcs2FacilityDataThresholdCapESHighThres1day,
       "pcs2FacilityDataThresholdCapDEHighThres15min": pcs2FacilityDataThresholdCapDEHighThres15min,
       "pcs2FacilityDataThresholdCapDEHighThres1day": pcs2FacilityDataThresholdCapDEHighThres1day,
       "pcs2FacilityDataThresholdCapCVHighThres15min": pcs2FacilityDataThresholdCapCVHighThres15min,
       "pcs2FacilityDataThresholdCapCVHighThres1day": pcs2FacilityDataThresholdCapCVHighThres1day,
       "endOfPcs2FacilityDataThresholdCapTable": endOfPcs2FacilityDataThresholdCapTable,
       "lFacilityDataThresholdCapTable": lFacilityDataThresholdCapTable,
       "lFacilityDataThresholdCapEntry": lFacilityDataThresholdCapEntry,
       "lFacilityDataThresholdCapESHighThres15min": lFacilityDataThresholdCapESHighThres15min,
       "lFacilityDataThresholdCapESHighThres1day": lFacilityDataThresholdCapESHighThres1day,
       "lFacilityDataThresholdCapSESHighThres15min": lFacilityDataThresholdCapSESHighThres15min,
       "lFacilityDataThresholdCapSESHighThres1day": lFacilityDataThresholdCapSESHighThres1day,
       "lFacilityDataThresholdCapUASHighThres15min": lFacilityDataThresholdCapUASHighThres15min,
       "lFacilityDataThresholdCapUASSHighThres1day": lFacilityDataThresholdCapUASSHighThres1day,
       "lFacilityDataThresholdCapCVHighThres15min": lFacilityDataThresholdCapCVHighThres15min,
       "lFacilityDataThresholdCapCVSHighThres1day": lFacilityDataThresholdCapCVSHighThres1day,
       "endOfLFacilityDataThresholdCapTable": endOfLFacilityDataThresholdCapTable,
       "sFacilityDataThresholdCapTable": sFacilityDataThresholdCapTable,
       "sFacilityDataThresholdCapEntry": sFacilityDataThresholdCapEntry,
       "sFacilityDataThresholdCapESHighThres15min": sFacilityDataThresholdCapESHighThres15min,
       "sFacilityDataThresholdCapESHighThres1day": sFacilityDataThresholdCapESHighThres1day,
       "sFacilityDataThresholdCapSESHighThres15min": sFacilityDataThresholdCapSESHighThres15min,
       "sFacilityDataThresholdCapSESHighThres1day": sFacilityDataThresholdCapSESHighThres1day,
       "sFacilityDataThresholdCapSEFSHighThres15min": sFacilityDataThresholdCapSEFSHighThres15min,
       "sFacilityDataThresholdCapSEFSHighThres1day": sFacilityDataThresholdCapSEFSHighThres1day,
       "sFacilityDataThresholdCapCVHighThres15min": sFacilityDataThresholdCapCVHighThres15min,
       "sFacilityDataThresholdCapCVHighThres1day": sFacilityDataThresholdCapCVHighThres1day,
       "endOfSFacilityDataThresholdCapTable": endOfSFacilityDataThresholdCapTable,
       "endOfPmFacilityDataThresholdCap": endOfPmFacilityDataThresholdCap,
       "endOfPmFacilityDataCap": endOfPmFacilityDataCap,
       "pmFacilityPhysicalCap": pmFacilityPhysicalCap,
       "pmFacilityPhysValueCap": pmFacilityPhysValueCap,
       "pmFacilityPhysThresholdCap": pmFacilityPhysThresholdCap,
       "facilityPhysThresholdCapTable": facilityPhysThresholdCapTable,
       "facilityPhysThresholdCapEntry": facilityPhysThresholdCapEntry,
       "facilityPhysThresholdCapOpticalInputPwrLow": facilityPhysThresholdCapOpticalInputPwrLow,
       "facilityPhysThresholdCapOpticalInputPwrHigh": facilityPhysThresholdCapOpticalInputPwrHigh,
       "facilityPhysThresholdCapConfigurableOpticalOutputPwrLow": facilityPhysThresholdCapConfigurableOpticalOutputPwrLow,
       "facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh": facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh,
       "facilityPhysThresholdCapRoundTripDelayLowThres": facilityPhysThresholdCapRoundTripDelayLowThres,
       "facilityPhysThresholdCapRoundTripDelayHighThres": facilityPhysThresholdCapRoundTripDelayHighThres,
       "facilityPhysThresholdCapLatencyLowThres": facilityPhysThresholdCapLatencyLowThres,
       "facilityPhysThresholdCapLatencyHighThres": facilityPhysThresholdCapLatencyHighThres,
       "facilityPhysThresholdCapChromaticDispersionHigh": facilityPhysThresholdCapChromaticDispersionHigh,
       "facilityPhysThresholdCapChromaticDispersionLow": facilityPhysThresholdCapChromaticDispersionLow,
       "facilityPhysThresholdCapCarrierFreqOffsetLow": facilityPhysThresholdCapCarrierFreqOffsetLow,
       "facilityPhysThresholdCapCarrierFreqOffsetHigh": facilityPhysThresholdCapCarrierFreqOffsetHigh,
       "facilityPhysThresholdCapLogicalLanesSkewHigh": facilityPhysThresholdCapLogicalLanesSkewHigh,
       "facilityPhysThresholdCapDispersionCompensationLowThres": facilityPhysThresholdCapDispersionCompensationLowThres,
       "facilityPhysThresholdCapDispersionCompensationHighThres": facilityPhysThresholdCapDispersionCompensationHighThres,
       "facilityPhysThresholdCapSignalToNoiseRatioLow": facilityPhysThresholdCapSignalToNoiseRatioLow,
       "facilityPhysThresholdCapDifferentialGroupDelayHigh": facilityPhysThresholdCapDifferentialGroupDelayHigh,
       "endOfFacilityPhysThresholdCapTable": endOfFacilityPhysThresholdCapTable,
       "endOfPmFacilityPhysThresholdCap": endOfPmFacilityPhysThresholdCap,
       "endOfPmFacilityPhysicalCap": endOfPmFacilityPhysicalCap,
       "endOfPmFacilityCap": endOfPmFacilityCap,
       "pmTerminPointCap": pmTerminPointCap,
       "pmOptMuxCap": pmOptMuxCap,
       "pmOptMuxDataCap": pmOptMuxDataCap,
       "pmOptMuxPhysicalCap": pmOptMuxPhysicalCap,
       "pmOptMuxPhysValueCap": pmOptMuxPhysValueCap,
       "pmOptMuxPhysThresholdCap": pmOptMuxPhysThresholdCap,
       "optMuxPhysThresholdCapTable": optMuxPhysThresholdCapTable,
       "optMuxPhysThresholdCapEntry": optMuxPhysThresholdCapEntry,
       "optMuxPhysThresholdCapBrtxHighConfig": optMuxPhysThresholdCapBrtxHighConfig,
       "optMuxPhysThresholdCapBrPwrReceivedHighThres": optMuxPhysThresholdCapBrPwrReceivedHighThres,
       "optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh": optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh,
       "optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow": optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow,
       "optMuxPhysThresholdCapOscPwrRcvHighThres": optMuxPhysThresholdCapOscPwrRcvHighThres,
       "optMuxPhysThresholdCapOscPwrRcvLowThres": optMuxPhysThresholdCapOscPwrRcvLowThres,
       "optMuxPhysThresholdCapOpticalInputPwrHigh": optMuxPhysThresholdCapOpticalInputPwrHigh,
       "optMuxPhysThresholdCapOpticalInputPwrLow": optMuxPhysThresholdCapOpticalInputPwrLow,
       "optMuxPhysThresholdCapAttRxHigh": optMuxPhysThresholdCapAttRxHigh,
       "optMuxPhysThresholdCapAttRxLow": optMuxPhysThresholdCapAttRxLow,
       "optMuxPhysThresholdCapAttTxHigh": optMuxPhysThresholdCapAttTxHigh,
       "optMuxPhysThresholdCapAttTxLow": optMuxPhysThresholdCapAttTxLow,
       "endOfOptMuxPhysThresholdCapTable": endOfOptMuxPhysThresholdCapTable,
       "endOfPmOptMuxPhysThresholdCap": endOfPmOptMuxPhysThresholdCap,
       "featureSpecificCap": featureSpecificCap,
       "fiberMapCap": fiberMapCap,
       "terminationPointCapTable": terminationPointCapTable,
       "terminationPointCapEntry": terminationPointCapEntry,
       "terminationPointCapRowStatus": terminationPointCapRowStatus,
       "terminationPointCapAdmin": terminationPointCapAdmin,
       "terminationPointCapFiberDetect": terminationPointCapFiberDetect,
       "terminationPointCapAlias": terminationPointCapAlias,
       "connectionCapTable": connectionCapTable,
       "connectionCapEntry": connectionCapEntry,
       "connectionCapRowStatus": connectionCapRowStatus,
       "connectionCapType": connectionCapType,
       "endOfConnectionCapTable": endOfConnectionCapTable,
       "endOfFiberMapCap": endOfFiberMapCap,
       "eciCap": eciCap,
       "externalPortCapTable": externalPortCapTable,
       "externalPortCapEntry": externalPortCapEntry,
       "externalPortCapRowStatus": externalPortCapRowStatus,
       "externalPortCapType": externalPortCapType,
       "externalPortCapTransmitChannel": externalPortCapTransmitChannel,
       "externalPortCapChannelBandwith": externalPortCapChannelBandwith,
       "externalPortCapAlias": externalPortCapAlias,
       "externalPortCapFarEndLocation": externalPortCapFarEndLocation,
       "externalPortCapBitrate": externalPortCapBitrate,
       "externalPortCapFecType": externalPortCapFecType,
       "externalPortCapLineCoding": externalPortCapLineCoding,
       "externalPortCapFrameFormat": externalPortCapFrameFormat,
       "externalPortCapOpticalPowerTx": externalPortCapOpticalPowerTx,
       "externalPortCapOsnrTransmit": externalPortCapOsnrTransmit,
       "externalPortCapPmdTransmit": externalPortCapPmdTransmit,
       "externalPortCapChromDisperTx": externalPortCapChromDisperTx,
       "externalPortCapMinOsnrRcv": externalPortCapMinOsnrRcv,
       "externalPortCapMinOptPowerRcv": externalPortCapMinOptPowerRcv,
       "externalPortCapMaxOptPowerRcv": externalPortCapMaxOptPowerRcv,
       "externalPortCapMaxPmdRcv": externalPortCapMaxPmdRcv,
       "externalPortCapMinChromDisperRcv": externalPortCapMinChromDisperRcv,
       "externalPortCapMaxChromDisperRcv": externalPortCapMaxChromDisperRcv,
       "externalPortCapMaxBitErrorRate": externalPortCapMaxBitErrorRate,
       "externalPortCapSourceProfile": externalPortCapSourceProfile,
       "endOfExternalPortCapTable": endOfExternalPortCapTable,
       "endOfEciCap": endOfEciCap,
       "changeServiceCap": changeServiceCap,
       "changePhysicalPortServiceCapTable": changePhysicalPortServiceCapTable,
       "changePhysicalPortServiceCapEntry": changePhysicalPortServiceCapEntry,
       "changePhysicalPortServiceCapRowStatus": changePhysicalPortServiceCapRowStatus,
       "changePhysicalPortServiceCapType": changePhysicalPortServiceCapType,
       "changePhysicalPortServiceCapAdmin": changePhysicalPortServiceCapAdmin,
       "changePhysicalPortServiceCapAlias": changePhysicalPortServiceCapAlias,
       "changePhysicalPortServiceCapAlsMode": changePhysicalPortServiceCapAlsMode,
       "changePhysicalPortServiceCapBehaviour": changePhysicalPortServiceCapBehaviour,
       "changePhysicalPortServiceCapDispersionSetting": changePhysicalPortServiceCapDispersionSetting,
       "changePhysicalPortServiceCapDispersionMode": changePhysicalPortServiceCapDispersionMode,
       "changePhysicalPortServiceCapChannelProv": changePhysicalPortServiceCapChannelProv,
       "changePhysicalPortServiceCapWdmRxChannel": changePhysicalPortServiceCapWdmRxChannel,
       "changePhysicalPortServiceCapCodeGain": changePhysicalPortServiceCapCodeGain,
       "changePhysicalPortServiceCapXfpDecisionThres": changePhysicalPortServiceCapXfpDecisionThres,
       "changePhysicalPortServiceCapDisparityCorrection": changePhysicalPortServiceCapDisparityCorrection,
       "changePhysicalPortServiceCapEqlzAdmin": changePhysicalPortServiceCapEqlzAdmin,
       "changePhysicalPortServiceCapErrorForwarding": changePhysicalPortServiceCapErrorForwarding,
       "changePhysicalPortServiceCapFecType": changePhysicalPortServiceCapFecType,
       "changePhysicalPortServiceCapFarEndCommunication": changePhysicalPortServiceCapFarEndCommunication,
       "changePhysicalPortServiceCapFlowControl": changePhysicalPortServiceCapFlowControl,
       "changePhysicalPortServiceCapLaneChannelSetting": changePhysicalPortServiceCapLaneChannelSetting,
       "changePhysicalPortServiceCapLaserDelayTimer": changePhysicalPortServiceCapLaserDelayTimer,
       "changePhysicalPortServiceCapLaserOffTimer": changePhysicalPortServiceCapLaserOffTimer,
       "changePhysicalPortServiceCapLaserOnTimer": changePhysicalPortServiceCapLaserOnTimer,
       "changePhysicalPortServiceCapLaserOffDelayFunction": changePhysicalPortServiceCapLaserOffDelayFunction,
       "changePhysicalPortServiceCapAutoPTassignment": changePhysicalPortServiceCapAutoPTassignment,
       "changePhysicalPortServiceCapTributarySlotMethod": changePhysicalPortServiceCapTributarySlotMethod,
       "changePhysicalPortServiceCapOpticalSetPoint": changePhysicalPortServiceCapOpticalSetPoint,
       "changePhysicalPortServiceCapOpuPayloadType": changePhysicalPortServiceCapOpuPayloadType,
       "changePhysicalPortServiceCapSigDegThresSonetLine": changePhysicalPortServiceCapSigDegThresSonetLine,
       "changePhysicalPortServiceCapSigDegThresSdhMs": changePhysicalPortServiceCapSigDegThresSdhMs,
       "changePhysicalPortServiceCapSigDegThresOtu": changePhysicalPortServiceCapSigDegThresOtu,
       "changePhysicalPortServiceCapSigDegThresOdu": changePhysicalPortServiceCapSigDegThresOdu,
       "changePhysicalPortServiceCapSigDegThreshold": changePhysicalPortServiceCapSigDegThreshold,
       "changePhysicalPortServiceCapSigDegPcslThreshold": changePhysicalPortServiceCapSigDegPcslThreshold,
       "changePhysicalPortServiceCapSigDegThresSonetSection": changePhysicalPortServiceCapSigDegThresSonetSection,
       "changePhysicalPortServiceCapSigDegThresSdhSection": changePhysicalPortServiceCapSigDegThresSdhSection,
       "changePhysicalPortServiceCapSigDegThresOduTcmA": changePhysicalPortServiceCapSigDegThresOduTcmA,
       "changePhysicalPortServiceCapSigDegThresOduTcmB": changePhysicalPortServiceCapSigDegThresOduTcmB,
       "changePhysicalPortServiceCapSigDegThresOduTcmC": changePhysicalPortServiceCapSigDegThresOduTcmC,
       "changePhysicalPortServiceCapSignalDegradePeriod": changePhysicalPortServiceCapSignalDegradePeriod,
       "changePhysicalPortServiceCapSigDegPeriodOdu": changePhysicalPortServiceCapSigDegPeriodOdu,
       "changePhysicalPortServiceCapSigDegPeriodOtu": changePhysicalPortServiceCapSigDegPeriodOtu,
       "changePhysicalPortServiceCapSigDegPeriodIntegration": changePhysicalPortServiceCapSigDegPeriodIntegration,
       "changePhysicalPortServiceCapSigDegPeriodSdhSection": changePhysicalPortServiceCapSigDegPeriodSdhSection,
       "changePhysicalPortServiceCapSigDegPeriodOduTcmA": changePhysicalPortServiceCapSigDegPeriodOduTcmA,
       "changePhysicalPortServiceCapSigDegPeriodOduTcmB": changePhysicalPortServiceCapSigDegPeriodOduTcmB,
       "changePhysicalPortServiceCapSigDegPeriodOduTcmC": changePhysicalPortServiceCapSigDegPeriodOduTcmC,
       "changePhysicalPortServiceCapOtnStuffing": changePhysicalPortServiceCapOtnStuffing,
       "changePhysicalPortServiceCapTcmALevel": changePhysicalPortServiceCapTcmALevel,
       "changePhysicalPortServiceCapTcmBLevel": changePhysicalPortServiceCapTcmBLevel,
       "changePhysicalPortServiceCapTcmCLevel": changePhysicalPortServiceCapTcmCLevel,
       "changePhysicalPortServiceCapTerminationLevel": changePhysicalPortServiceCapTerminationLevel,
       "changePhysicalPortServiceCapTimingSource": changePhysicalPortServiceCapTimingSource,
       "changePhysicalPortServiceCapTimModeOdu": changePhysicalPortServiceCapTimModeOdu,
       "changePhysicalPortServiceCapTimModeOtu": changePhysicalPortServiceCapTimModeOtu,
       "changePhysicalPortServiceCapTimModeSonetSection": changePhysicalPortServiceCapTimModeSonetSection,
       "changePhysicalPortServiceCapTimModeOduTcmA": changePhysicalPortServiceCapTimModeOduTcmA,
       "changePhysicalPortServiceCapTimModeOduTcmB": changePhysicalPortServiceCapTimModeOduTcmB,
       "changePhysicalPortServiceCapTimModeOduTcmC": changePhysicalPortServiceCapTimModeOduTcmC,
       "changePhysicalPortServiceCapTraceFormSonetSection": changePhysicalPortServiceCapTraceFormSonetSection,
       "changePhysicalPortServiceCapTraceExpectedSonetSection": changePhysicalPortServiceCapTraceExpectedSonetSection,
       "changePhysicalPortServiceCapTraceTransmitSonetSection": changePhysicalPortServiceCapTraceTransmitSonetSection,
       "changePhysicalPortServiceCapTraceExpectedOtu": changePhysicalPortServiceCapTraceExpectedOtu,
       "changePhysicalPortServiceCapTraceTransmitSapiOtu": changePhysicalPortServiceCapTraceTransmitSapiOtu,
       "changePhysicalPortServiceCapTraceTransmitDapiOtu": changePhysicalPortServiceCapTraceTransmitDapiOtu,
       "changePhysicalPortServiceCapTraceTransmitOpspOtu": changePhysicalPortServiceCapTraceTransmitOpspOtu,
       "changePhysicalPortServiceCapTraceExpectedOdu": changePhysicalPortServiceCapTraceExpectedOdu,
       "changePhysicalPortServiceCapTraceTransmitSapiOdu": changePhysicalPortServiceCapTraceTransmitSapiOdu,
       "changePhysicalPortServiceCapTraceTransmitDapiOdu": changePhysicalPortServiceCapTraceTransmitDapiOdu,
       "changePhysicalPortServiceCapTraceTransmitOpspOdu": changePhysicalPortServiceCapTraceTransmitOpspOdu,
       "changePhysicalPortServiceCapTraceExpectedOduTcmA": changePhysicalPortServiceCapTraceExpectedOduTcmA,
       "changePhysicalPortServiceCapTraceTransmitSapiOduTcmA": changePhysicalPortServiceCapTraceTransmitSapiOduTcmA,
       "changePhysicalPortServiceCapTraceTransmitDapiOduTcmA": changePhysicalPortServiceCapTraceTransmitDapiOduTcmA,
       "changePhysicalPortServiceCapTraceTransmitOpspOduTcmA": changePhysicalPortServiceCapTraceTransmitOpspOduTcmA,
       "changePhysicalPortServiceCapTraceExpectedOduTcmB": changePhysicalPortServiceCapTraceExpectedOduTcmB,
       "changePhysicalPortServiceCapTraceTransmitSapiOduTcmB": changePhysicalPortServiceCapTraceTransmitSapiOduTcmB,
       "changePhysicalPortServiceCapTraceTransmitDapiOduTcmB": changePhysicalPortServiceCapTraceTransmitDapiOduTcmB,
       "changePhysicalPortServiceCapTraceTransmitOpspOduTcmB": changePhysicalPortServiceCapTraceTransmitOpspOduTcmB,
       "changePhysicalPortServiceCapTraceExpectedOduTcmC": changePhysicalPortServiceCapTraceExpectedOduTcmC,
       "changePhysicalPortServiceCapTraceTransmitSapiOduTcmC": changePhysicalPortServiceCapTraceTransmitSapiOduTcmC,
       "changePhysicalPortServiceCapTraceTransmitDapiOduTcmC": changePhysicalPortServiceCapTraceTransmitDapiOduTcmC,
       "changePhysicalPortServiceCapTraceTransmitOpspOduTcmC": changePhysicalPortServiceCapTraceTransmitOpspOduTcmC,
       "changePhysicalPortServiceCapTxOffDelay": changePhysicalPortServiceCapTxOffDelay,
       "changePhysicalPortServiceCapVoaMode": changePhysicalPortServiceCapVoaMode,
       "changePhysicalPortServiceCapVoaSetpoint": changePhysicalPortServiceCapVoaSetpoint,
       "changePhysicalPortServiceCapTxOffOnTm": changePhysicalPortServiceCapTxOffOnTm,
       "changePhysicalPortServiceCapTxOffTimer": changePhysicalPortServiceCapTxOffTimer,
       "changePhysicalPortServiceCapTxOnTimer": changePhysicalPortServiceCapTxOnTimer,
       "endOfChangePhysicalPortServiceCapTable": endOfChangePhysicalPortServiceCapTable,
       "endOfChangeServiceCap": endOfChangeServiceCap,
       "protectionCap": protectionCap,
       "ffpCapTable": ffpCapTable,
       "ffpCapEntry": ffpCapEntry,
       "ffpCapRowStatus": ffpCapRowStatus,
       "ffpCapCreationMethod": ffpCapCreationMethod,
       "ffpCapSDswitching": ffpCapSDswitching,
       "ffpCapHoldOffTime": ffpCapHoldOffTime,
       "ffpCapProtectionMech": ffpCapProtectionMech,
       "ffpCapWorkingAid": ffpCapWorkingAid,
       "ffpCapProtectionAid": ffpCapProtectionAid,
       "ffpCapSignalDegradeSwitching": ffpCapSignalDegradeSwitching,
       "ffpCapFarEndIp": ffpCapFarEndIp,
       "ffpCapPeerAid": ffpCapPeerAid,
       "ffpCapApsType": ffpCapApsType,
       "ffpCapRevertMode": ffpCapRevertMode,
       "ffpCapWaitToRestore": ffpCapWaitToRestore,
       "ffpCapDirection": ffpCapDirection,
       "endOfFfpCapTable": endOfFfpCapTable,
       "endOfProtectionCap": endOfProtectionCap,
       "conformanceCap": conformanceCap,
       "compliancesCap": compliancesCap,
       "complianceCap": complianceCap,
       "groupsCap": groupsCap,
       "objectGroupCap": objectGroupCap}
)
