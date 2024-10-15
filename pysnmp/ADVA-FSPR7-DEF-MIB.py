# SNMP MIB module (ADVA-FSPR7-DEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADVA-FSPR7-DEF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:44 2024
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
 entityOptLineClassName,
 entityOptLineIndexNo1,
 entityOpticalMuxClassName,
 entityOpticalMuxExtNo,
 entityOpticalMuxPortNo,
 entityOpticalMuxShelfNo,
 entityOpticalMuxSlotNo,
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
    "entityOptLineClassName",
    "entityOptLineIndexNo1",
    "entityOpticalMuxClassName",
    "entityOpticalMuxExtNo",
    "entityOpticalMuxPortNo",
    "entityOpticalMuxShelfNo",
    "entityOpticalMuxSlotNo",
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

(ApsRevertMode,
 ApsType,
 FfpType,
 FspR7APSCommand,
 FspR7AdminState,
 FspR7AlsMode,
 FspR7AseTabOpr,
 FspR7AutoThresReset,
 FspR7BERThreshold,
 FspR7BERThresholdSection,
 FspR7Baund,
 FspR7BidirectionalChannel,
 FspR7Bitrate,
 FspR7CapInventory,
 FspR7ChannelBandwidth,
 FspR7ChannelIdentifier,
 FspR7ChannelSpacing,
 FspR7CodeGain,
 FspR7Conn,
 FspR7ConnectorType,
 FspR7CpAuthType,
 FspR7DCFiberType,
 FspR7DeploymentScenario,
 FspR7DisableEnable,
 FspR7DispersionCompensation,
 FspR7DispersionConfig,
 FspR7DispersionModes,
 FspR7EdfaOutputPowerRating,
 FspR7EnableDisable,
 FspR7EqlzAdminState,
 FspR7ErrorFwdMode,
 FspR7FecType,
 FspR7FiberBrand,
 FspR7FiberDetect,
 FspR7FlowControlMode,
 FspR7ForceConfig,
 FspR7FrameFormat,
 FspR7FunctionCrs,
 FspR7Gain,
 FspR7GainRange,
 FspR7IPv6Type,
 FspR7InitEqualization,
 FspR7InterfaceType,
 FspR7InvertTelemetryInputLogic,
 FspR7IpMode,
 FspR7IpType,
 FspR7LacpMode,
 FspR7LacpTimeout,
 FspR7LagPortType,
 FspR7LaneGroupInventory,
 FspR7LaserDelayTimer,
 FspR7LaserForcedOperation,
 FspR7LineCoding,
 FspR7LossAttenuation,
 FspR7ManualAuto,
 FspR7Mapping,
 FspR7MaxBitErrorRate,
 FspR7MuxMethod,
 FspR7NdpCleanup,
 FspR7NoYes,
 FspR7NumberOfChannels,
 FspR7NumberOfChannelsProv,
 FspR7OptUpdate,
 FspR7OpticalBand,
 FspR7OpticalFiberType,
 FspR7OpticalGroup,
 FspR7OpticalInterfaceReach,
 FspR7OpticalSubBand,
 FspR7OpuPayloadType,
 FspR7OscUsage,
 FspR7OspfMode,
 FspR7OtdrPeriod,
 FspR7PRBSTest,
 FspR7PathNode,
 FspR7PlugDataRate,
 FspR7PmReset,
 FspR7PortBehaviour,
 FspR7PortMode,
 FspR7PortRole,
 FspR7PrbsPmReset,
 FspR7ProtectionType,
 FspR7PsuOutputPower,
 FspR7RedLinedState,
 FspR7RlsMan,
 FspR7RoadmNumber,
 FspR7RowStatus,
 FspR7Scrambling,
 FspR7SingleFiberLocation,
 FspR7SnmpHexString,
 FspR7SnmpLongString,
 FspR7Stuff,
 FspR7SupplyType,
 FspR7TelemetryOutput,
 FspR7TifOutputReset,
 FspR7TiltSet,
 FspR7Topology,
 FspR7TrafficDirection,
 FspR7TransmissionMode,
 FspR7TurnupConfig,
 FspR7TxOffOnTm,
 FspR7TypeConnection,
 FspR7TypeCrs,
 FspR7Unsigned32Caps,
 FspR7UntaggedFrames,
 FspR7VoaMode,
 FspR7XfpDecisionThres,
 FspR7YesNo) = mibBuilder.importSymbols(
    "ADVA-FSPR7-TC-MIB",
    "ApsRevertMode",
    "ApsType",
    "FfpType",
    "FspR7APSCommand",
    "FspR7AdminState",
    "FspR7AlsMode",
    "FspR7AseTabOpr",
    "FspR7AutoThresReset",
    "FspR7BERThreshold",
    "FspR7BERThresholdSection",
    "FspR7Baund",
    "FspR7BidirectionalChannel",
    "FspR7Bitrate",
    "FspR7CapInventory",
    "FspR7ChannelBandwidth",
    "FspR7ChannelIdentifier",
    "FspR7ChannelSpacing",
    "FspR7CodeGain",
    "FspR7Conn",
    "FspR7ConnectorType",
    "FspR7CpAuthType",
    "FspR7DCFiberType",
    "FspR7DeploymentScenario",
    "FspR7DisableEnable",
    "FspR7DispersionCompensation",
    "FspR7DispersionConfig",
    "FspR7DispersionModes",
    "FspR7EdfaOutputPowerRating",
    "FspR7EnableDisable",
    "FspR7EqlzAdminState",
    "FspR7ErrorFwdMode",
    "FspR7FecType",
    "FspR7FiberBrand",
    "FspR7FiberDetect",
    "FspR7FlowControlMode",
    "FspR7ForceConfig",
    "FspR7FrameFormat",
    "FspR7FunctionCrs",
    "FspR7Gain",
    "FspR7GainRange",
    "FspR7IPv6Type",
    "FspR7InitEqualization",
    "FspR7InterfaceType",
    "FspR7InvertTelemetryInputLogic",
    "FspR7IpMode",
    "FspR7IpType",
    "FspR7LacpMode",
    "FspR7LacpTimeout",
    "FspR7LagPortType",
    "FspR7LaneGroupInventory",
    "FspR7LaserDelayTimer",
    "FspR7LaserForcedOperation",
    "FspR7LineCoding",
    "FspR7LossAttenuation",
    "FspR7ManualAuto",
    "FspR7Mapping",
    "FspR7MaxBitErrorRate",
    "FspR7MuxMethod",
    "FspR7NdpCleanup",
    "FspR7NoYes",
    "FspR7NumberOfChannels",
    "FspR7NumberOfChannelsProv",
    "FspR7OptUpdate",
    "FspR7OpticalBand",
    "FspR7OpticalFiberType",
    "FspR7OpticalGroup",
    "FspR7OpticalInterfaceReach",
    "FspR7OpticalSubBand",
    "FspR7OpuPayloadType",
    "FspR7OscUsage",
    "FspR7OspfMode",
    "FspR7OtdrPeriod",
    "FspR7PRBSTest",
    "FspR7PathNode",
    "FspR7PlugDataRate",
    "FspR7PmReset",
    "FspR7PortBehaviour",
    "FspR7PortMode",
    "FspR7PortRole",
    "FspR7PrbsPmReset",
    "FspR7ProtectionType",
    "FspR7PsuOutputPower",
    "FspR7RedLinedState",
    "FspR7RlsMan",
    "FspR7RoadmNumber",
    "FspR7RowStatus",
    "FspR7Scrambling",
    "FspR7SingleFiberLocation",
    "FspR7SnmpHexString",
    "FspR7SnmpLongString",
    "FspR7Stuff",
    "FspR7SupplyType",
    "FspR7TelemetryOutput",
    "FspR7TifOutputReset",
    "FspR7TiltSet",
    "FspR7Topology",
    "FspR7TrafficDirection",
    "FspR7TransmissionMode",
    "FspR7TurnupConfig",
    "FspR7TxOffOnTm",
    "FspR7TypeConnection",
    "FspR7TypeCrs",
    "FspR7Unsigned32Caps",
    "FspR7UntaggedFrames",
    "FspR7VoaMode",
    "FspR7XfpDecisionThres",
    "FspR7YesNo")

(ApsDirection,
 ApsHoldoffTime,
 EnableState,
 EthDuplexMode,
 FspR7EquipmentType,
 LoopConfig,
 OhTerminationLevel,
 OtnPayloadType,
 OtnTcmLevel,
 ProtectionMech,
 SonetTimingSource,
 SonetTraceForm,
 TimMode,
 VirtualContainerType,
 fspR7) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "ApsDirection",
    "ApsHoldoffTime",
    "EnableState",
    "EthDuplexMode",
    "FspR7EquipmentType",
    "LoopConfig",
    "OhTerminationLevel",
    "OtnPayloadType",
    "OtnTcmLevel",
    "ProtectionMech",
    "SonetTimingSource",
    "SonetTraceForm",
    "TimMode",
    "VirtualContainerType",
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

advaFspR7Def = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10)
)
advaFspR7Def.setRevisions(
        ("2014-10-15 00:00",
         "2014-09-29 00:00",
         "2013-12-04 00:00",
         "2013-08-20 00:00",
         "2011-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ManagementDef_ObjectIdentity = ObjectIdentity
managementDef = _ManagementDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3)
)
_SpecificMgmtDef_ObjectIdentity = ObjectIdentity
specificMgmtDef = _SpecificMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2)
)
_CrossConnectionDefTable_Object = MibTable
crossConnectionDefTable = _CrossConnectionDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6)
)
if mibBuilder.loadTexts:
    crossConnectionDefTable.setStatus("current")
_CrossConnectionDefEntry_Object = MibTableRow
crossConnectionDefEntry = _CrossConnectionDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1)
)
crossConnectionDefEntry.setIndexNames(
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
    crossConnectionDefEntry.setStatus("current")
_CrossConnectionDefRowStatus_Type = FspR7RowStatus
_CrossConnectionDefRowStatus_Object = MibTableColumn
crossConnectionDefRowStatus = _CrossConnectionDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 1),
    _CrossConnectionDefRowStatus_Type()
)
crossConnectionDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefRowStatus.setStatus("current")
_CrossConnectionDefAdmin_Type = FspR7AdminState
_CrossConnectionDefAdmin_Object = MibTableColumn
crossConnectionDefAdmin = _CrossConnectionDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 2),
    _CrossConnectionDefAdmin_Type()
)
crossConnectionDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefAdmin.setStatus("current")
_CrossConnectionDefRedLineState_Type = FspR7RedLinedState
_CrossConnectionDefRedLineState_Object = MibTableColumn
crossConnectionDefRedLineState = _CrossConnectionDefRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 3),
    _CrossConnectionDefRedLineState_Type()
)
crossConnectionDefRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefRedLineState.setStatus("current")
_CrossConnectionDefConn_Type = FspR7Conn
_CrossConnectionDefConn_Object = MibTableColumn
crossConnectionDefConn = _CrossConnectionDefConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 4),
    _CrossConnectionDefConn_Type()
)
crossConnectionDefConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefConn.setStatus("current")
_CrossConnectionDefAlias_Type = SnmpAdminString
_CrossConnectionDefAlias_Object = MibTableColumn
crossConnectionDefAlias = _CrossConnectionDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 5),
    _CrossConnectionDefAlias_Type()
)
crossConnectionDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefAlias.setStatus("current")
_CrossConnectionDefPathNode_Type = FspR7PathNode
_CrossConnectionDefPathNode_Object = MibTableColumn
crossConnectionDefPathNode = _CrossConnectionDefPathNode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 6),
    _CrossConnectionDefPathNode_Type()
)
crossConnectionDefPathNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefPathNode.setStatus("current")
_CrossConnectionDefTunnelAid_Type = SnmpAdminString
_CrossConnectionDefTunnelAid_Object = MibTableColumn
crossConnectionDefTunnelAid = _CrossConnectionDefTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 7),
    _CrossConnectionDefTunnelAid_Type()
)
crossConnectionDefTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefTunnelAid.setStatus("current")
_CrossConnectionDefType_Type = FspR7InterfaceType
_CrossConnectionDefType_Object = MibTableColumn
crossConnectionDefType = _CrossConnectionDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 8),
    _CrossConnectionDefType_Type()
)
crossConnectionDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefType.setStatus("current")
_CrossConnectionDefCrsFunction_Type = FspR7FunctionCrs
_CrossConnectionDefCrsFunction_Object = MibTableColumn
crossConnectionDefCrsFunction = _CrossConnectionDefCrsFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 6, 1, 9),
    _CrossConnectionDefCrsFunction_Type()
)
crossConnectionDefCrsFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionDefCrsFunction.setStatus("current")
_CrossOpticalLineDefTable_Object = MibTable
crossOpticalLineDefTable = _CrossOpticalLineDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7)
)
if mibBuilder.loadTexts:
    crossOpticalLineDefTable.setStatus("current")
_CrossOpticalLineDefEntry_Object = MibTableRow
crossOpticalLineDefEntry = _CrossOpticalLineDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1)
)
crossOpticalLineDefEntry.setIndexNames(
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
    crossOpticalLineDefEntry.setStatus("current")
_CrossOpticalLineDefRowStatus_Type = FspR7RowStatus
_CrossOpticalLineDefRowStatus_Object = MibTableColumn
crossOpticalLineDefRowStatus = _CrossOpticalLineDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 1),
    _CrossOpticalLineDefRowStatus_Type()
)
crossOpticalLineDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefRowStatus.setStatus("current")
_CrossOpticalLineDefRedLineState_Type = FspR7RedLinedState
_CrossOpticalLineDefRedLineState_Object = MibTableColumn
crossOpticalLineDefRedLineState = _CrossOpticalLineDefRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 2),
    _CrossOpticalLineDefRedLineState_Type()
)
crossOpticalLineDefRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefRedLineState.setStatus("current")
_CrossOpticalLineDefConn_Type = FspR7Conn
_CrossOpticalLineDefConn_Object = MibTableColumn
crossOpticalLineDefConn = _CrossOpticalLineDefConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 3),
    _CrossOpticalLineDefConn_Type()
)
crossOpticalLineDefConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefConn.setStatus("current")
_CrossOpticalLineDefCrsType_Type = FspR7TypeCrs
_CrossOpticalLineDefCrsType_Object = MibTableColumn
crossOpticalLineDefCrsType = _CrossOpticalLineDefCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 4),
    _CrossOpticalLineDefCrsType_Type()
)
crossOpticalLineDefCrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefCrsType.setStatus("current")
_CrossOpticalLineDefAlias_Type = SnmpAdminString
_CrossOpticalLineDefAlias_Object = MibTableColumn
crossOpticalLineDefAlias = _CrossOpticalLineDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 5),
    _CrossOpticalLineDefAlias_Type()
)
crossOpticalLineDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefAlias.setStatus("current")
_CrossOpticalLineDefTunnelAid_Type = SnmpAdminString
_CrossOpticalLineDefTunnelAid_Object = MibTableColumn
crossOpticalLineDefTunnelAid = _CrossOpticalLineDefTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 7, 1, 6),
    _CrossOpticalLineDefTunnelAid_Type()
)
crossOpticalLineDefTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossOpticalLineDefTunnelAid.setStatus("current")
_EndOfCrossOpticalLineDefTable_Type = Integer32
_EndOfCrossOpticalLineDefTable_Object = MibScalar
endOfCrossOpticalLineDefTable = _EndOfCrossOpticalLineDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 8),
    _EndOfCrossOpticalLineDefTable_Type()
)
endOfCrossOpticalLineDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfCrossOpticalLineDefTable.setStatus("current")
_CrossDcnDefTable_Object = MibTable
crossDcnDefTable = _CrossDcnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9)
)
if mibBuilder.loadTexts:
    crossDcnDefTable.setStatus("current")
_CrossDcnDefEntry_Object = MibTableRow
crossDcnDefEntry = _CrossDcnDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9, 1)
)
crossDcnDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityCrossDcnClassName"),
)
if mibBuilder.loadTexts:
    crossDcnDefEntry.setStatus("current")
_CrossDcnDefRowStatus_Type = RowStatus
_CrossDcnDefRowStatus_Object = MibTableColumn
crossDcnDefRowStatus = _CrossDcnDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9, 1, 1),
    _CrossDcnDefRowStatus_Type()
)
crossDcnDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnDefRowStatus.setStatus("current")
_CrossDcnDefType_Type = FspR7TypeConnection
_CrossDcnDefType_Object = MibTableColumn
crossDcnDefType = _CrossDcnDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9, 1, 2),
    _CrossDcnDefType_Type()
)
crossDcnDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnDefType.setStatus("current")
_CrossDcnDefLink_Type = SnmpAdminString
_CrossDcnDefLink_Object = MibTableColumn
crossDcnDefLink = _CrossDcnDefLink_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9, 1, 3),
    _CrossDcnDefLink_Type()
)
crossDcnDefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnDefLink.setStatus("current")
_CrossDcnDefEcc_Type = SnmpAdminString
_CrossDcnDefEcc_Object = MibTableColumn
crossDcnDefEcc = _CrossDcnDefEcc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 9, 1, 4),
    _CrossDcnDefEcc_Type()
)
crossDcnDefEcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossDcnDefEcc.setStatus("current")
_EndOfCrossDcnDefTable_Type = Integer32
_EndOfCrossDcnDefTable_Object = MibScalar
endOfCrossDcnDefTable = _EndOfCrossDcnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 10),
    _EndOfCrossDcnDefTable_Type()
)
endOfCrossDcnDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfCrossDcnDefTable.setStatus("current")
_EndOfSpecificMgmtDef_Type = Integer32
_EndOfSpecificMgmtDef_Object = MibScalar
endOfSpecificMgmtDef = _EndOfSpecificMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 2, 10000),
    _EndOfSpecificMgmtDef_Type()
)
endOfSpecificMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfSpecificMgmtDef.setStatus("current")
_EqptMgmtDef_ObjectIdentity = ObjectIdentity
eqptMgmtDef = _EqptMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3)
)
_ShelfDefTable_Object = MibTable
shelfDefTable = _ShelfDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1)
)
if mibBuilder.loadTexts:
    shelfDefTable.setStatus("current")
_ShelfDefEntry_Object = MibTableRow
shelfDefEntry = _ShelfDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1)
)
shelfDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    shelfDefEntry.setStatus("current")
_ShelfDefRowStatus_Type = RowStatus
_ShelfDefRowStatus_Object = MibTableColumn
shelfDefRowStatus = _ShelfDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 1),
    _ShelfDefRowStatus_Type()
)
shelfDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefRowStatus.setStatus("current")
_ShelfDefPsuOutputPower_Type = FspR7PsuOutputPower
_ShelfDefPsuOutputPower_Object = MibTableColumn
shelfDefPsuOutputPower = _ShelfDefPsuOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 2),
    _ShelfDefPsuOutputPower_Type()
)
shelfDefPsuOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefPsuOutputPower.setStatus("current")
_ShelfDefType_Type = FspR7EquipmentType
_ShelfDefType_Object = MibTableColumn
shelfDefType = _ShelfDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 3),
    _ShelfDefType_Type()
)
shelfDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefType.setStatus("current")
_ShelfDefRack_Type = SnmpAdminString
_ShelfDefRack_Object = MibTableColumn
shelfDefRack = _ShelfDefRack_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 4),
    _ShelfDefRack_Type()
)
shelfDefRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefRack.setStatus("current")
_ShelfDefSupply_Type = FspR7SupplyType
_ShelfDefSupply_Object = MibTableColumn
shelfDefSupply = _ShelfDefSupply_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 5),
    _ShelfDefSupply_Type()
)
shelfDefSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefSupply.setStatus("current")
_ShelfDefBandProvision_Type = FspR7OpticalBand
_ShelfDefBandProvision_Object = MibTableColumn
shelfDefBandProvision = _ShelfDefBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 6),
    _ShelfDefBandProvision_Type()
)
shelfDefBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefBandProvision.setStatus("current")
_ShelfDefAdmin_Type = FspR7AdminState
_ShelfDefAdmin_Object = MibTableColumn
shelfDefAdmin = _ShelfDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 7),
    _ShelfDefAdmin_Type()
)
shelfDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefAdmin.setStatus("current")


class _ShelfDefRackNumber_Type(Unsigned32):
    """Custom type shelfDefRackNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ShelfDefRackNumber_Type.__name__ = "Unsigned32"
_ShelfDefRackNumber_Object = MibTableColumn
shelfDefRackNumber = _ShelfDefRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 8),
    _ShelfDefRackNumber_Type()
)
shelfDefRackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefRackNumber.setStatus("current")


class _ShelfDefRackOrder_Type(Unsigned32):
    """Custom type shelfDefRackOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_ShelfDefRackOrder_Type.__name__ = "Unsigned32"
_ShelfDefRackOrder_Object = MibTableColumn
shelfDefRackOrder = _ShelfDefRackOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 9),
    _ShelfDefRackOrder_Type()
)
shelfDefRackOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefRackOrder.setStatus("current")
_ShelfDefAlias_Type = SnmpAdminString
_ShelfDefAlias_Object = MibTableColumn
shelfDefAlias = _ShelfDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 10),
    _ShelfDefAlias_Type()
)
shelfDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefAlias.setStatus("current")


class _ShelfDefSlot_Type(Unsigned32):
    """Custom type shelfDefSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_ShelfDefSlot_Type.__name__ = "Unsigned32"
_ShelfDefSlot_Object = MibTableColumn
shelfDefSlot = _ShelfDefSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 1, 1, 11),
    _ShelfDefSlot_Type()
)
shelfDefSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDefSlot.setStatus("current")
_EndOfShelfDefTable_Type = Integer32
_EndOfShelfDefTable_Object = MibScalar
endOfShelfDefTable = _EndOfShelfDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 2),
    _EndOfShelfDefTable_Type()
)
endOfShelfDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfDefTable.setStatus("current")
_FanDefTable_Object = MibTable
fanDefTable = _FanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3)
)
if mibBuilder.loadTexts:
    fanDefTable.setStatus("current")
_FanDefEntry_Object = MibTableRow
fanDefEntry = _FanDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1)
)
fanDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    fanDefEntry.setStatus("current")
_FanDefRowStatus_Type = RowStatus
_FanDefRowStatus_Object = MibTableColumn
fanDefRowStatus = _FanDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1, 1),
    _FanDefRowStatus_Type()
)
fanDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDefRowStatus.setStatus("current")
_FanDefAdmin_Type = FspR7AdminState
_FanDefAdmin_Object = MibTableColumn
fanDefAdmin = _FanDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1, 2),
    _FanDefAdmin_Type()
)
fanDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDefAdmin.setStatus("current")
_FanDefType_Type = FspR7EquipmentType
_FanDefType_Object = MibTableColumn
fanDefType = _FanDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1, 3),
    _FanDefType_Type()
)
fanDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDefType.setStatus("current")
_FanDefAlias_Type = SnmpAdminString
_FanDefAlias_Object = MibTableColumn
fanDefAlias = _FanDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1, 4),
    _FanDefAlias_Type()
)
fanDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDefAlias.setStatus("current")
_FanDefOutputReset_Type = FspR7TifOutputReset
_FanDefOutputReset_Object = MibTableColumn
fanDefOutputReset = _FanDefOutputReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 3, 1, 5),
    _FanDefOutputReset_Type()
)
fanDefOutputReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDefOutputReset.setStatus("current")
_EndOfFanDefTable_Type = Integer32
_EndOfFanDefTable_Object = MibScalar
endOfFanDefTable = _EndOfFanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 4),
    _EndOfFanDefTable_Type()
)
endOfFanDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFanDefTable.setStatus("current")
_PlugDefTable_Object = MibTable
plugDefTable = _PlugDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5)
)
if mibBuilder.loadTexts:
    plugDefTable.setStatus("current")
_PlugDefEntry_Object = MibTableRow
plugDefEntry = _PlugDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1)
)
plugDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    plugDefEntry.setStatus("current")
_PlugDefRowStatus_Type = RowStatus
_PlugDefRowStatus_Object = MibTableColumn
plugDefRowStatus = _PlugDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 1),
    _PlugDefRowStatus_Type()
)
plugDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefRowStatus.setStatus("current")
_PlugDefConnector_Type = FspR7ConnectorType
_PlugDefConnector_Object = MibTableColumn
plugDefConnector = _PlugDefConnector_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 2),
    _PlugDefConnector_Type()
)
plugDefConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefConnector.setStatus("current")
_PlugDefType_Type = FspR7EquipmentType
_PlugDefType_Object = MibTableColumn
plugDefType = _PlugDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 3),
    _PlugDefType_Type()
)
plugDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefType.setStatus("current")
_PlugDefReach_Type = FspR7OpticalInterfaceReach
_PlugDefReach_Object = MibTableColumn
plugDefReach = _PlugDefReach_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 4),
    _PlugDefReach_Type()
)
plugDefReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefReach.setStatus("current")


class _PlugDefLoopbackAttenuation_Type(Unsigned32):
    """Custom type plugDefLoopbackAttenuation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_PlugDefLoopbackAttenuation_Type.__name__ = "Unsigned32"
_PlugDefLoopbackAttenuation_Object = MibTableColumn
plugDefLoopbackAttenuation = _PlugDefLoopbackAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 5),
    _PlugDefLoopbackAttenuation_Type()
)
plugDefLoopbackAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefLoopbackAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    plugDefLoopbackAttenuation.setUnits("0.1 dB")
_PlugDefTransmitChannel_Type = FspR7ChannelIdentifier
_PlugDefTransmitChannel_Object = MibTableColumn
plugDefTransmitChannel = _PlugDefTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 6),
    _PlugDefTransmitChannel_Type()
)
plugDefTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefTransmitChannel.setStatus("current")
_PlugDefAlias_Type = SnmpAdminString
_PlugDefAlias_Object = MibTableColumn
plugDefAlias = _PlugDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 7),
    _PlugDefAlias_Type()
)
plugDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefAlias.setStatus("current")
_PlugDefLaneGroup_Type = FspR7LaneGroupInventory
_PlugDefLaneGroup_Object = MibTableColumn
plugDefLaneGroup = _PlugDefLaneGroup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 8),
    _PlugDefLaneGroup_Type()
)
plugDefLaneGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefLaneGroup.setStatus("current")
_PlugDefMaxDataRate_Type = FspR7PlugDataRate
_PlugDefMaxDataRate_Object = MibTableColumn
plugDefMaxDataRate = _PlugDefMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 9),
    _PlugDefMaxDataRate_Type()
)
plugDefMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefMaxDataRate.setStatus("current")
_PlugDefThirdPartyUsage_Type = EnableState
_PlugDefThirdPartyUsage_Object = MibTableColumn
plugDefThirdPartyUsage = _PlugDefThirdPartyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 10),
    _PlugDefThirdPartyUsage_Type()
)
plugDefThirdPartyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefThirdPartyUsage.setStatus("current")
_PlugDefAdmin_Type = FspR7AdminState
_PlugDefAdmin_Object = MibTableColumn
plugDefAdmin = _PlugDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 11),
    _PlugDefAdmin_Type()
)
plugDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefAdmin.setStatus("current")
_PlugDefBidirectionalChannel_Type = FspR7BidirectionalChannel
_PlugDefBidirectionalChannel_Object = MibTableColumn
plugDefBidirectionalChannel = _PlugDefBidirectionalChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 12),
    _PlugDefBidirectionalChannel_Type()
)
plugDefBidirectionalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefBidirectionalChannel.setStatus("current")
_PlugDefChannelSpacingProvision_Type = FspR7ChannelSpacing
_PlugDefChannelSpacingProvision_Object = MibTableColumn
plugDefChannelSpacingProvision = _PlugDefChannelSpacingProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 5, 1, 13),
    _PlugDefChannelSpacingProvision_Type()
)
plugDefChannelSpacingProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugDefChannelSpacingProvision.setStatus("current")
_EndOfPlugDefTable_Type = Integer32
_EndOfPlugDefTable_Object = MibScalar
endOfPlugDefTable = _EndOfPlugDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 6),
    _EndOfPlugDefTable_Type()
)
endOfPlugDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPlugDefTable.setStatus("current")
_ModuleDefTable_Object = MibTable
moduleDefTable = _ModuleDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7)
)
if mibBuilder.loadTexts:
    moduleDefTable.setStatus("current")
_ModuleDefEntry_Object = MibTableRow
moduleDefEntry = _ModuleDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1)
)
moduleDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    moduleDefEntry.setStatus("current")
_ModuleDefRowStatus_Type = RowStatus
_ModuleDefRowStatus_Object = MibTableColumn
moduleDefRowStatus = _ModuleDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 1),
    _ModuleDefRowStatus_Type()
)
moduleDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefRowStatus.setStatus("current")
_ModuleDefPsuOutputPower_Type = FspR7PsuOutputPower
_ModuleDefPsuOutputPower_Object = MibTableColumn
moduleDefPsuOutputPower = _ModuleDefPsuOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 2),
    _ModuleDefPsuOutputPower_Type()
)
moduleDefPsuOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefPsuOutputPower.setStatus("current")
_ModuleDefPower_Type = FspR7EdfaOutputPowerRating
_ModuleDefPower_Object = MibTableColumn
moduleDefPower = _ModuleDefPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 3),
    _ModuleDefPower_Type()
)
moduleDefPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefPower.setStatus("current")
_ModuleDefReach_Type = FspR7OpticalInterfaceReach
_ModuleDefReach_Object = MibTableColumn
moduleDefReach = _ModuleDefReach_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 4),
    _ModuleDefReach_Type()
)
moduleDefReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefReach.setStatus("current")
_ModuleDefInitEqlz_Type = FspR7InitEqualization
_ModuleDefInitEqlz_Object = MibTableColumn
moduleDefInitEqlz = _ModuleDefInitEqlz_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 5),
    _ModuleDefInitEqlz_Type()
)
moduleDefInitEqlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefInitEqlz.setStatus("current")
_ModuleDefLanAid_Type = SnmpAdminString
_ModuleDefLanAid_Object = MibTableColumn
moduleDefLanAid = _ModuleDefLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 6),
    _ModuleDefLanAid_Type()
)
moduleDefLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefLanAid.setStatus("current")
_ModuleDefType_Type = FspR7EquipmentType
_ModuleDefType_Object = MibTableColumn
moduleDefType = _ModuleDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 7),
    _ModuleDefType_Type()
)
moduleDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefType.setStatus("current")
_ModuleDefMapping_Type = FspR7Mapping
_ModuleDefMapping_Object = MibTableColumn
moduleDefMapping = _ModuleDefMapping_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 8),
    _ModuleDefMapping_Type()
)
moduleDefMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefMapping.setStatus("current")
_ModuleDefGainRange_Type = FspR7GainRange
_ModuleDefGainRange_Object = MibTableColumn
moduleDefGainRange = _ModuleDefGainRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 9),
    _ModuleDefGainRange_Type()
)
moduleDefGainRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefGainRange.setStatus("current")
_ModuleDefSfProvision_Type = FspR7SingleFiberLocation
_ModuleDefSfProvision_Object = MibTableColumn
moduleDefSfProvision = _ModuleDefSfProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 10),
    _ModuleDefSfProvision_Type()
)
moduleDefSfProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefSfProvision.setStatus("current")
_ModuleDefCapabilityLevelProvision_Type = FspR7CapInventory
_ModuleDefCapabilityLevelProvision_Object = MibTableColumn
moduleDefCapabilityLevelProvision = _ModuleDefCapabilityLevelProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 11),
    _ModuleDefCapabilityLevelProvision_Type()
)
moduleDefCapabilityLevelProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefCapabilityLevelProvision.setStatus("current")
_ModuleDefDCFiberType_Type = FspR7DCFiberType
_ModuleDefDCFiberType_Object = MibTableColumn
moduleDefDCFiberType = _ModuleDefDCFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 12),
    _ModuleDefDCFiberType_Type()
)
moduleDefDCFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefDCFiberType.setStatus("current")
_ModuleDefChannelsProvision_Type = FspR7NumberOfChannelsProv
_ModuleDefChannelsProvision_Object = MibTableColumn
moduleDefChannelsProvision = _ModuleDefChannelsProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 13),
    _ModuleDefChannelsProvision_Type()
)
moduleDefChannelsProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefChannelsProvision.setStatus("current")
_ModuleDefFiberDetect_Type = FspR7FiberDetect
_ModuleDefFiberDetect_Object = MibTableColumn
moduleDefFiberDetect = _ModuleDefFiberDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 14),
    _ModuleDefFiberDetect_Type()
)
moduleDefFiberDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefFiberDetect.setStatus("current")
_ModuleDefSupply_Type = FspR7SupplyType
_ModuleDefSupply_Object = MibTableColumn
moduleDefSupply = _ModuleDefSupply_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 15),
    _ModuleDefSupply_Type()
)
moduleDefSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefSupply.setStatus("current")
_ModuleDefGroup_Type = FspR7OpticalGroup
_ModuleDefGroup_Object = MibTableColumn
moduleDefGroup = _ModuleDefGroup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 16),
    _ModuleDefGroup_Type()
)
moduleDefGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefGroup.setStatus("current")
_ModuleDefDeploy_Type = FspR7DeploymentScenario
_ModuleDefDeploy_Object = MibTableColumn
moduleDefDeploy = _ModuleDefDeploy_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 17),
    _ModuleDefDeploy_Type()
)
moduleDefDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefDeploy.setStatus("current")


class _ModuleDefLagSysPrio_Type(Unsigned32):
    """Custom type moduleDefLagSysPrio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleDefLagSysPrio_Type.__name__ = "Unsigned32"
_ModuleDefLagSysPrio_Object = MibTableColumn
moduleDefLagSysPrio = _ModuleDefLagSysPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 18),
    _ModuleDefLagSysPrio_Type()
)
moduleDefLagSysPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefLagSysPrio.setStatus("current")
_ModuleDefTransmitChannel_Type = FspR7ChannelIdentifier
_ModuleDefTransmitChannel_Object = MibTableColumn
moduleDefTransmitChannel = _ModuleDefTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 19),
    _ModuleDefTransmitChannel_Type()
)
moduleDefTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefTransmitChannel.setStatus("current")
_ModuleDefBand_Type = FspR7OpticalBand
_ModuleDefBand_Object = MibTableColumn
moduleDefBand = _ModuleDefBand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 20),
    _ModuleDefBand_Type()
)
moduleDefBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefBand.setStatus("current")
_ModuleDefTrafficDirection_Type = FspR7TrafficDirection
_ModuleDefTrafficDirection_Object = MibTableColumn
moduleDefTrafficDirection = _ModuleDefTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 21),
    _ModuleDefTrafficDirection_Type()
)
moduleDefTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefTrafficDirection.setStatus("current")
_ModuleDefIpAddr_Type = IpAddress
_ModuleDefIpAddr_Object = MibTableColumn
moduleDefIpAddr = _ModuleDefIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 22),
    _ModuleDefIpAddr_Type()
)
moduleDefIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefIpAddr.setStatus("current")
_ModuleDefDispersionCompensation_Type = FspR7DispersionCompensation
_ModuleDefDispersionCompensation_Object = MibTableColumn
moduleDefDispersionCompensation = _ModuleDefDispersionCompensation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 23),
    _ModuleDefDispersionCompensation_Type()
)
moduleDefDispersionCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefDispersionCompensation.setStatus("current")
_ModuleDefActivateDetect_Type = FspR7YesNo
_ModuleDefActivateDetect_Object = MibTableColumn
moduleDefActivateDetect = _ModuleDefActivateDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 24),
    _ModuleDefActivateDetect_Type()
)
moduleDefActivateDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefActivateDetect.setStatus("current")
_ModuleDefOscUsage_Type = FspR7OscUsage
_ModuleDefOscUsage_Object = MibTableColumn
moduleDefOscUsage = _ModuleDefOscUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 25),
    _ModuleDefOscUsage_Type()
)
moduleDefOscUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefOscUsage.setStatus("current")
_ModuleDefAdmin_Type = FspR7AdminState
_ModuleDefAdmin_Object = MibTableColumn
moduleDefAdmin = _ModuleDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 26),
    _ModuleDefAdmin_Type()
)
moduleDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefAdmin.setStatus("current")
_ModuleDefScrambling_Type = FspR7Scrambling
_ModuleDefScrambling_Object = MibTableColumn
moduleDefScrambling = _ModuleDefScrambling_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 27),
    _ModuleDefScrambling_Type()
)
moduleDefScrambling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefScrambling.setStatus("current")
_ModuleDefChannelsNumber_Type = FspR7NumberOfChannels
_ModuleDefChannelsNumber_Object = MibTableColumn
moduleDefChannelsNumber = _ModuleDefChannelsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 28),
    _ModuleDefChannelsNumber_Type()
)
moduleDefChannelsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefChannelsNumber.setStatus("current")
_ModuleDefChannelSpacingProvision_Type = FspR7ChannelSpacing
_ModuleDefChannelSpacingProvision_Object = MibTableColumn
moduleDefChannelSpacingProvision = _ModuleDefChannelSpacingProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 29),
    _ModuleDefChannelSpacingProvision_Type()
)
moduleDefChannelSpacingProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefChannelSpacingProvision.setStatus("current")
_ModuleDefMode_Type = FspR7TransmissionMode
_ModuleDefMode_Object = MibTableColumn
moduleDefMode = _ModuleDefMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 30),
    _ModuleDefMode_Type()
)
moduleDefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefMode.setStatus("current")
_ModuleDefSubBandProvision_Type = FspR7OpticalSubBand
_ModuleDefSubBandProvision_Object = MibTableColumn
moduleDefSubBandProvision = _ModuleDefSubBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 31),
    _ModuleDefSubBandProvision_Type()
)
moduleDefSubBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefSubBandProvision.setStatus("current")
_ModuleDefAlias_Type = SnmpAdminString
_ModuleDefAlias_Object = MibTableColumn
moduleDefAlias = _ModuleDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 32),
    _ModuleDefAlias_Type()
)
moduleDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefAlias.setStatus("current")
_ModuleDefFiberType_Type = FspR7OpticalFiberType
_ModuleDefFiberType_Object = MibTableColumn
moduleDefFiberType = _ModuleDefFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 33),
    _ModuleDefFiberType_Type()
)
moduleDefFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefFiberType.setStatus("current")
_ModuleDefChannelSpacing_Type = FspR7ChannelSpacing
_ModuleDefChannelSpacing_Object = MibTableColumn
moduleDefChannelSpacing = _ModuleDefChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 34),
    _ModuleDefChannelSpacing_Type()
)
moduleDefChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefChannelSpacing.setStatus("current")
_ModuleDefOutputReset_Type = FspR7TifOutputReset
_ModuleDefOutputReset_Object = MibTableColumn
moduleDefOutputReset = _ModuleDefOutputReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 35),
    _ModuleDefOutputReset_Type()
)
moduleDefOutputReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefOutputReset.setStatus("current")
_ModuleDefRoadmNumber_Type = FspR7RoadmNumber
_ModuleDefRoadmNumber_Object = MibTableColumn
moduleDefRoadmNumber = _ModuleDefRoadmNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 36),
    _ModuleDefRoadmNumber_Type()
)
moduleDefRoadmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefRoadmNumber.setStatus("current")
_ModuleDefTopology_Type = FspR7Topology
_ModuleDefTopology_Object = MibTableColumn
moduleDefTopology = _ModuleDefTopology_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 37),
    _ModuleDefTopology_Type()
)
moduleDefTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefTopology.setStatus("current")
_ModuleDefForceConfig_Type = FspR7ForceConfig
_ModuleDefForceConfig_Object = MibTableColumn
moduleDefForceConfig = _ModuleDefForceConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 38),
    _ModuleDefForceConfig_Type()
)
moduleDefForceConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefForceConfig.setStatus("current")
_ModuleDefMuxMethod_Type = FspR7MuxMethod
_ModuleDefMuxMethod_Object = MibTableColumn
moduleDefMuxMethod = _ModuleDefMuxMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 39),
    _ModuleDefMuxMethod_Type()
)
moduleDefMuxMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefMuxMethod.setStatus("current")
_ModuleDefNdpCleanup_Type = FspR7NdpCleanup
_ModuleDefNdpCleanup_Object = MibTableColumn
moduleDefNdpCleanup = _ModuleDefNdpCleanup_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 40),
    _ModuleDefNdpCleanup_Type()
)
moduleDefNdpCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefNdpCleanup.setStatus("current")
_ModuleDefRstp_Type = FspR7EnableDisable
_ModuleDefRstp_Object = MibTableColumn
moduleDefRstp = _ModuleDefRstp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 41),
    _ModuleDefRstp_Type()
)
moduleDefRstp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefRstp.setStatus("current")
_ModuleDefRemoteReset_Type = FspR7RlsMan
_ModuleDefRemoteReset_Object = MibTableColumn
moduleDefRemoteReset = _ModuleDefRemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 7, 1, 42),
    _ModuleDefRemoteReset_Type()
)
moduleDefRemoteReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDefRemoteReset.setStatus("current")
_EndOfModuleDefTable_Type = Integer32
_EndOfModuleDefTable_Object = MibScalar
endOfModuleDefTable = _EndOfModuleDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 8),
    _EndOfModuleDefTable_Type()
)
endOfModuleDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfModuleDefTable.setStatus("current")
_EndOfEqptMgmtDef_Type = Integer32
_EndOfEqptMgmtDef_Object = MibScalar
endOfEqptMgmtDef = _EndOfEqptMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 3, 10000),
    _EndOfEqptMgmtDef_Type()
)
endOfEqptMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEqptMgmtDef.setStatus("current")
_FacilityMgmtDef_ObjectIdentity = ObjectIdentity
facilityMgmtDef = _FacilityMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4)
)
_PhysicalPortDefTable_Object = MibTable
physicalPortDefTable = _PhysicalPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1)
)
if mibBuilder.loadTexts:
    physicalPortDefTable.setStatus("current")
_PhysicalPortDefEntry_Object = MibTableRow
physicalPortDefEntry = _PhysicalPortDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1)
)
physicalPortDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    physicalPortDefEntry.setStatus("current")
_PhysicalPortDefRowStatus_Type = RowStatus
_PhysicalPortDefRowStatus_Object = MibTableColumn
physicalPortDefRowStatus = _PhysicalPortDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 1),
    _PhysicalPortDefRowStatus_Type()
)
physicalPortDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefRowStatus.setStatus("current")
_PhysicalPortDefType_Type = FspR7InterfaceType
_PhysicalPortDefType_Object = MibTableColumn
physicalPortDefType = _PhysicalPortDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 2),
    _PhysicalPortDefType_Type()
)
physicalPortDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefType.setStatus("current")
_PhysicalPortDefAdmin_Type = FspR7AdminState
_PhysicalPortDefAdmin_Object = MibTableColumn
physicalPortDefAdmin = _PhysicalPortDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 3),
    _PhysicalPortDefAdmin_Type()
)
physicalPortDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAdmin.setStatus("current")
_PhysicalPortDefAlias_Type = SnmpAdminString
_PhysicalPortDefAlias_Object = MibTableColumn
physicalPortDefAlias = _PhysicalPortDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 4),
    _PhysicalPortDefAlias_Type()
)
physicalPortDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAlias.setStatus("current")
_PhysicalPortDefAlsMode_Type = FspR7AlsMode
_PhysicalPortDefAlsMode_Object = MibTableColumn
physicalPortDefAlsMode = _PhysicalPortDefAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 5),
    _PhysicalPortDefAlsMode_Type()
)
physicalPortDefAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAlsMode.setStatus("current")
_PhysicalPortDefAutoThresReset_Type = FspR7AutoThresReset
_PhysicalPortDefAutoThresReset_Object = MibTableColumn
physicalPortDefAutoThresReset = _PhysicalPortDefAutoThresReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 6),
    _PhysicalPortDefAutoThresReset_Type()
)
physicalPortDefAutoThresReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAutoThresReset.setStatus("current")
_PhysicalPortDefAutonegotiation_Type = EnableState
_PhysicalPortDefAutonegotiation_Object = MibTableColumn
physicalPortDefAutonegotiation = _PhysicalPortDefAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 7),
    _PhysicalPortDefAutonegotiation_Type()
)
physicalPortDefAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAutonegotiation.setStatus("current")
_PhysicalPortDefBehaviour_Type = FspR7PortBehaviour
_PhysicalPortDefBehaviour_Object = MibTableColumn
physicalPortDefBehaviour = _PhysicalPortDefBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 8),
    _PhysicalPortDefBehaviour_Type()
)
physicalPortDefBehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefBehaviour.setStatus("current")
_PhysicalPortDefDispertionConfig_Type = FspR7DispersionConfig
_PhysicalPortDefDispertionConfig_Object = MibTableColumn
physicalPortDefDispertionConfig = _PhysicalPortDefDispertionConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 9),
    _PhysicalPortDefDispertionConfig_Type()
)
physicalPortDefDispertionConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefDispertionConfig.setStatus("current")


class _PhysicalPortDefDispersionSetting_Type(Integer32):
    """Custom type physicalPortDefDispersionSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50000, 50000),
    )


_PhysicalPortDefDispersionSetting_Type.__name__ = "Integer32"
_PhysicalPortDefDispersionSetting_Object = MibTableColumn
physicalPortDefDispersionSetting = _PhysicalPortDefDispersionSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 10),
    _PhysicalPortDefDispersionSetting_Type()
)
physicalPortDefDispersionSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefDispersionSetting.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefDispersionSetting.setUnits("ps/nm")
_PhysicalPortDefDispersionMode_Type = FspR7DispersionModes
_PhysicalPortDefDispersionMode_Object = MibTableColumn
physicalPortDefDispersionMode = _PhysicalPortDefDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 11),
    _PhysicalPortDefDispersionMode_Type()
)
physicalPortDefDispersionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefDispersionMode.setStatus("current")
_PhysicalPortDefChannelProv_Type = FspR7ChannelIdentifier
_PhysicalPortDefChannelProv_Object = MibTableColumn
physicalPortDefChannelProv = _PhysicalPortDefChannelProv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 12),
    _PhysicalPortDefChannelProv_Type()
)
physicalPortDefChannelProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefChannelProv.setStatus("current")
_PhysicalPortDefWdmRxChannel_Type = FspR7ChannelIdentifier
_PhysicalPortDefWdmRxChannel_Object = MibTableColumn
physicalPortDefWdmRxChannel = _PhysicalPortDefWdmRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 13),
    _PhysicalPortDefWdmRxChannel_Type()
)
physicalPortDefWdmRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefWdmRxChannel.setStatus("current")
_PhysicalPortDefCodeGain_Type = FspR7CodeGain
_PhysicalPortDefCodeGain_Object = MibTableColumn
physicalPortDefCodeGain = _PhysicalPortDefCodeGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 14),
    _PhysicalPortDefCodeGain_Type()
)
physicalPortDefCodeGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefCodeGain.setStatus("current")
_PhysicalPortDefXfpDecisionThres_Type = FspR7XfpDecisionThres
_PhysicalPortDefXfpDecisionThres_Object = MibTableColumn
physicalPortDefXfpDecisionThres = _PhysicalPortDefXfpDecisionThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 15),
    _PhysicalPortDefXfpDecisionThres_Type()
)
physicalPortDefXfpDecisionThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefXfpDecisionThres.setStatus("current")
_PhysicalPortDefDisparityCorrection_Type = EnableState
_PhysicalPortDefDisparityCorrection_Object = MibTableColumn
physicalPortDefDisparityCorrection = _PhysicalPortDefDisparityCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 16),
    _PhysicalPortDefDisparityCorrection_Type()
)
physicalPortDefDisparityCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefDisparityCorrection.setStatus("current")
_PhysicalPortDefEqlzAdmin_Type = FspR7EqlzAdminState
_PhysicalPortDefEqlzAdmin_Object = MibTableColumn
physicalPortDefEqlzAdmin = _PhysicalPortDefEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 17),
    _PhysicalPortDefEqlzAdmin_Type()
)
physicalPortDefEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefEqlzAdmin.setStatus("current")
_PhysicalPortDefErrorForwarding_Type = FspR7ErrorFwdMode
_PhysicalPortDefErrorForwarding_Object = MibTableColumn
physicalPortDefErrorForwarding = _PhysicalPortDefErrorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 18),
    _PhysicalPortDefErrorForwarding_Type()
)
physicalPortDefErrorForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefErrorForwarding.setStatus("current")
_PhysicalPortDefFecType_Type = FspR7FecType
_PhysicalPortDefFecType_Object = MibTableColumn
physicalPortDefFecType = _PhysicalPortDefFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 19),
    _PhysicalPortDefFecType_Type()
)
physicalPortDefFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefFecType.setStatus("current")
_PhysicalPortDefFarEndCommunication_Type = FspR7YesNo
_PhysicalPortDefFarEndCommunication_Object = MibTableColumn
physicalPortDefFarEndCommunication = _PhysicalPortDefFarEndCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 20),
    _PhysicalPortDefFarEndCommunication_Type()
)
physicalPortDefFarEndCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefFarEndCommunication.setStatus("current")
_PhysicalPortDefFlowControl_Type = FspR7FlowControlMode
_PhysicalPortDefFlowControl_Object = MibTableColumn
physicalPortDefFlowControl = _PhysicalPortDefFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 21),
    _PhysicalPortDefFlowControl_Type()
)
physicalPortDefFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefFlowControl.setStatus("current")
_PhysicalPortDefForceLaserOn_Type = FspR7LaserForcedOperation
_PhysicalPortDefForceLaserOn_Object = MibTableColumn
physicalPortDefForceLaserOn = _PhysicalPortDefForceLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 22),
    _PhysicalPortDefForceLaserOn_Type()
)
physicalPortDefForceLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefForceLaserOn.setStatus("current")
_PhysicalPortDefInhibitSwitchToProt_Type = FspR7YesNo
_PhysicalPortDefInhibitSwitchToProt_Object = MibTableColumn
physicalPortDefInhibitSwitchToProt = _PhysicalPortDefInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 23),
    _PhysicalPortDefInhibitSwitchToProt_Type()
)
physicalPortDefInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefInhibitSwitchToProt.setStatus("current")
_PhysicalPortDefInhibitSwitchToWork_Type = FspR7YesNo
_PhysicalPortDefInhibitSwitchToWork_Object = MibTableColumn
physicalPortDefInhibitSwitchToWork = _PhysicalPortDefInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 24),
    _PhysicalPortDefInhibitSwitchToWork_Type()
)
physicalPortDefInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefInhibitSwitchToWork.setStatus("current")
_PhysicalPortDefLaneChannelSetting_Type = FspR7ChannelIdentifier
_PhysicalPortDefLaneChannelSetting_Object = MibTableColumn
physicalPortDefLaneChannelSetting = _PhysicalPortDefLaneChannelSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 25),
    _PhysicalPortDefLaneChannelSetting_Type()
)
physicalPortDefLaneChannelSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLaneChannelSetting.setStatus("current")
_PhysicalPortDefLoopConfig_Type = LoopConfig
_PhysicalPortDefLoopConfig_Object = MibTableColumn
physicalPortDefLoopConfig = _PhysicalPortDefLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 26),
    _PhysicalPortDefLoopConfig_Type()
)
physicalPortDefLoopConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLoopConfig.setStatus("current")
_PhysicalPortDefLaserDelayTimer_Type = FspR7LaserDelayTimer
_PhysicalPortDefLaserDelayTimer_Object = MibTableColumn
physicalPortDefLaserDelayTimer = _PhysicalPortDefLaserDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 27),
    _PhysicalPortDefLaserDelayTimer_Type()
)
physicalPortDefLaserDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLaserDelayTimer.setStatus("current")


class _PhysicalPortDefLaserOffTimer_Type(Unsigned32):
    """Custom type physicalPortDefLaserOffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PhysicalPortDefLaserOffTimer_Type.__name__ = "Unsigned32"
_PhysicalPortDefLaserOffTimer_Object = MibTableColumn
physicalPortDefLaserOffTimer = _PhysicalPortDefLaserOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 28),
    _PhysicalPortDefLaserOffTimer_Type()
)
physicalPortDefLaserOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLaserOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefLaserOffTimer.setUnits("ms")


class _PhysicalPortDefLaserOnTimer_Type(Unsigned32):
    """Custom type physicalPortDefLaserOnTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PhysicalPortDefLaserOnTimer_Type.__name__ = "Unsigned32"
_PhysicalPortDefLaserOnTimer_Object = MibTableColumn
physicalPortDefLaserOnTimer = _PhysicalPortDefLaserOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 29),
    _PhysicalPortDefLaserOnTimer_Type()
)
physicalPortDefLaserOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLaserOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefLaserOnTimer.setUnits("ms")
_PhysicalPortDefLaserOffDelayFunction_Type = EnableState
_PhysicalPortDefLaserOffDelayFunction_Object = MibTableColumn
physicalPortDefLaserOffDelayFunction = _PhysicalPortDefLaserOffDelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 30),
    _PhysicalPortDefLaserOffDelayFunction_Type()
)
physicalPortDefLaserOffDelayFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLaserOffDelayFunction.setStatus("current")
_PhysicalPortDefAutoPTassignment_Type = FspR7ManualAuto
_PhysicalPortDefAutoPTassignment_Object = MibTableColumn
physicalPortDefAutoPTassignment = _PhysicalPortDefAutoPTassignment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 31),
    _PhysicalPortDefAutoPTassignment_Type()
)
physicalPortDefAutoPTassignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefAutoPTassignment.setStatus("current")
_PhysicalPortDefTributarySlotMethod_Type = FspR7ManualAuto
_PhysicalPortDefTributarySlotMethod_Object = MibTableColumn
physicalPortDefTributarySlotMethod = _PhysicalPortDefTributarySlotMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 32),
    _PhysicalPortDefTributarySlotMethod_Type()
)
physicalPortDefTributarySlotMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTributarySlotMethod.setStatus("current")
_PhysicalPortDefInitiateEqualization_Type = FspR7InitEqualization
_PhysicalPortDefInitiateEqualization_Object = MibTableColumn
physicalPortDefInitiateEqualization = _PhysicalPortDefInitiateEqualization_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 33),
    _PhysicalPortDefInitiateEqualization_Type()
)
physicalPortDefInitiateEqualization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefInitiateEqualization.setStatus("current")
_PhysicalPortDefLossAttenuation_Type = FspR7LossAttenuation
_PhysicalPortDefLossAttenuation_Object = MibTableColumn
physicalPortDefLossAttenuation = _PhysicalPortDefLossAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 34),
    _PhysicalPortDefLossAttenuation_Type()
)
physicalPortDefLossAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLossAttenuation.setStatus("current")


class _PhysicalPortDefOpticalSetPoint_Type(Integer32):
    """Custom type physicalPortDefOpticalSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 50),
    )


_PhysicalPortDefOpticalSetPoint_Type.__name__ = "Integer32"
_PhysicalPortDefOpticalSetPoint_Object = MibTableColumn
physicalPortDefOpticalSetPoint = _PhysicalPortDefOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 35),
    _PhysicalPortDefOpticalSetPoint_Type()
)
physicalPortDefOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefOpticalSetPoint.setUnits("0.1 dBm")
_PhysicalPortDefDataLayerPmReset_Type = FspR7PmReset
_PhysicalPortDefDataLayerPmReset_Object = MibTableColumn
physicalPortDefDataLayerPmReset = _PhysicalPortDefDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 36),
    _PhysicalPortDefDataLayerPmReset_Type()
)
physicalPortDefDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefDataLayerPmReset.setStatus("current")
_PhysicalPortDefPrbsPmReset_Type = FspR7PrbsPmReset
_PhysicalPortDefPrbsPmReset_Object = MibTableColumn
physicalPortDefPrbsPmReset = _PhysicalPortDefPrbsPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 37),
    _PhysicalPortDefPrbsPmReset_Type()
)
physicalPortDefPrbsPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPrbsPmReset.setStatus("current")
_PhysicalPortDefTestPrbsRcvMode_Type = FspR7PRBSTest
_PhysicalPortDefTestPrbsRcvMode_Object = MibTableColumn
physicalPortDefTestPrbsRcvMode = _PhysicalPortDefTestPrbsRcvMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 38),
    _PhysicalPortDefTestPrbsRcvMode_Type()
)
physicalPortDefTestPrbsRcvMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTestPrbsRcvMode.setStatus("current")
_PhysicalPortDefTestPrbsTrmtMode_Type = FspR7PRBSTest
_PhysicalPortDefTestPrbsTrmtMode_Object = MibTableColumn
physicalPortDefTestPrbsTrmtMode = _PhysicalPortDefTestPrbsTrmtMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 39),
    _PhysicalPortDefTestPrbsTrmtMode_Type()
)
physicalPortDefTestPrbsTrmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTestPrbsTrmtMode.setStatus("current")
_PhysicalPortDefSwitchCommand_Type = FspR7APSCommand
_PhysicalPortDefSwitchCommand_Object = MibTableColumn
physicalPortDefSwitchCommand = _PhysicalPortDefSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 40),
    _PhysicalPortDefSwitchCommand_Type()
)
physicalPortDefSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSwitchCommand.setStatus("current")
_PhysicalPortDefOpuPayloadType_Type = FspR7OpuPayloadType
_PhysicalPortDefOpuPayloadType_Object = MibTableColumn
physicalPortDefOpuPayloadType = _PhysicalPortDefOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 41),
    _PhysicalPortDefOpuPayloadType_Type()
)
physicalPortDefOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefOpuPayloadType.setStatus("current")
_PhysicalPortDefSigDegThresSonetLine_Type = FspR7BERThreshold
_PhysicalPortDefSigDegThresSonetLine_Object = MibTableColumn
physicalPortDefSigDegThresSonetLine = _PhysicalPortDefSigDegThresSonetLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 42),
    _PhysicalPortDefSigDegThresSonetLine_Type()
)
physicalPortDefSigDegThresSonetLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSonetLine.setStatus("current")


class _PhysicalPortDefSigDegThresSdhMs_Type(Unsigned32):
    """Custom type physicalPortDefSigDegThresSdhMs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresSdhMs_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegThresSdhMs_Object = MibTableColumn
physicalPortDefSigDegThresSdhMs = _PhysicalPortDefSigDegThresSdhMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 43),
    _PhysicalPortDefSigDegThresSdhMs_Type()
)
physicalPortDefSigDegThresSdhMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSdhMs.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSdhMs.setUnits("%")


class _PhysicalPortDefSigDegThresOtu_Type(Integer32):
    """Custom type physicalPortDefSigDegThresOtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresOtu_Type.__name__ = "Integer32"
_PhysicalPortDefSigDegThresOtu_Object = MibTableColumn
physicalPortDefSigDegThresOtu = _PhysicalPortDefSigDegThresOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 44),
    _PhysicalPortDefSigDegThresOtu_Type()
)
physicalPortDefSigDegThresOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOtu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOtu.setUnits("%")


class _PhysicalPortDefSigDegThresOdu_Type(Integer32):
    """Custom type physicalPortDefSigDegThresOdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresOdu_Type.__name__ = "Integer32"
_PhysicalPortDefSigDegThresOdu_Object = MibTableColumn
physicalPortDefSigDegThresOdu = _PhysicalPortDefSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 45),
    _PhysicalPortDefSigDegThresOdu_Type()
)
physicalPortDefSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOdu.setUnits("%")


class _PhysicalPortDefSigDegThreshold_Type(Unsigned32):
    """Custom type physicalPortDefSigDegThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PhysicalPortDefSigDegThreshold_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegThreshold_Object = MibTableColumn
physicalPortDefSigDegThreshold = _PhysicalPortDefSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 46),
    _PhysicalPortDefSigDegThreshold_Type()
)
physicalPortDefSigDegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThreshold.setStatus("current")


class _PhysicalPortDefSigDegPcslThreshold_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPcslThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegPcslThreshold_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPcslThreshold_Object = MibTableColumn
physicalPortDefSigDegPcslThreshold = _PhysicalPortDefSigDegPcslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 47),
    _PhysicalPortDefSigDegPcslThreshold_Type()
)
physicalPortDefSigDegPcslThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPcslThreshold.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPcslThreshold.setUnits("%")
_PhysicalPortDefSigDegThresSonetSection_Type = FspR7BERThresholdSection
_PhysicalPortDefSigDegThresSonetSection_Object = MibTableColumn
physicalPortDefSigDegThresSonetSection = _PhysicalPortDefSigDegThresSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 48),
    _PhysicalPortDefSigDegThresSonetSection_Type()
)
physicalPortDefSigDegThresSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSonetSection.setStatus("current")


class _PhysicalPortDefSigDegThresSdhSection_Type(Unsigned32):
    """Custom type physicalPortDefSigDegThresSdhSection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresSdhSection_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegThresSdhSection_Object = MibTableColumn
physicalPortDefSigDegThresSdhSection = _PhysicalPortDefSigDegThresSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 49),
    _PhysicalPortDefSigDegThresSdhSection_Type()
)
physicalPortDefSigDegThresSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresSdhSection.setUnits("%")


class _PhysicalPortDefSigDegThresOduTcmA_Type(Integer32):
    """Custom type physicalPortDefSigDegThresOduTcmA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresOduTcmA_Type.__name__ = "Integer32"
_PhysicalPortDefSigDegThresOduTcmA_Object = MibTableColumn
physicalPortDefSigDegThresOduTcmA = _PhysicalPortDefSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 50),
    _PhysicalPortDefSigDegThresOduTcmA_Type()
)
physicalPortDefSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmA.setUnits("%")


class _PhysicalPortDefSigDegThresOduTcmB_Type(Integer32):
    """Custom type physicalPortDefSigDegThresOduTcmB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresOduTcmB_Type.__name__ = "Integer32"
_PhysicalPortDefSigDegThresOduTcmB_Object = MibTableColumn
physicalPortDefSigDegThresOduTcmB = _PhysicalPortDefSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 51),
    _PhysicalPortDefSigDegThresOduTcmB_Type()
)
physicalPortDefSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmB.setUnits("%")


class _PhysicalPortDefSigDegThresOduTcmC_Type(Integer32):
    """Custom type physicalPortDefSigDegThresOduTcmC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PhysicalPortDefSigDegThresOduTcmC_Type.__name__ = "Integer32"
_PhysicalPortDefSigDegThresOduTcmC_Object = MibTableColumn
physicalPortDefSigDegThresOduTcmC = _PhysicalPortDefSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 52),
    _PhysicalPortDefSigDegThresOduTcmC_Type()
)
physicalPortDefSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegThresOduTcmC.setUnits("%")


class _PhysicalPortDefSignalDegradePeriod_Type(Unsigned32):
    """Custom type physicalPortDefSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSignalDegradePeriod_Type.__name__ = "Unsigned32"
_PhysicalPortDefSignalDegradePeriod_Object = MibTableColumn
physicalPortDefSignalDegradePeriod = _PhysicalPortDefSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 53),
    _PhysicalPortDefSignalDegradePeriod_Type()
)
physicalPortDefSignalDegradePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSignalDegradePeriod.setUnits("s")


class _PhysicalPortDefSigDegPeriodOdu_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodOdu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodOdu_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodOdu_Object = MibTableColumn
physicalPortDefSigDegPeriodOdu = _PhysicalPortDefSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 54),
    _PhysicalPortDefSigDegPeriodOdu_Type()
)
physicalPortDefSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOdu.setUnits("s")


class _PhysicalPortDefSigDegPeriodOtu_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodOtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodOtu_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodOtu_Object = MibTableColumn
physicalPortDefSigDegPeriodOtu = _PhysicalPortDefSigDegPeriodOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 55),
    _PhysicalPortDefSigDegPeriodOtu_Type()
)
physicalPortDefSigDegPeriodOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOtu.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOtu.setUnits("s")


class _PhysicalPortDefSigDegPeriodIntegration_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodIntegration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PhysicalPortDefSigDegPeriodIntegration_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodIntegration_Object = MibTableColumn
physicalPortDefSigDegPeriodIntegration = _PhysicalPortDefSigDegPeriodIntegration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 56),
    _PhysicalPortDefSigDegPeriodIntegration_Type()
)
physicalPortDefSigDegPeriodIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodIntegration.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodIntegration.setUnits("s")


class _PhysicalPortDefSigDegPeriodSdhSection_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodSdhSection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodSdhSection_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodSdhSection_Object = MibTableColumn
physicalPortDefSigDegPeriodSdhSection = _PhysicalPortDefSigDegPeriodSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 57),
    _PhysicalPortDefSigDegPeriodSdhSection_Type()
)
physicalPortDefSigDegPeriodSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodSdhSection.setUnits("s")


class _PhysicalPortDefSigDegPeriodOduTcmA_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodOduTcmA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodOduTcmA_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodOduTcmA_Object = MibTableColumn
physicalPortDefSigDegPeriodOduTcmA = _PhysicalPortDefSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 58),
    _PhysicalPortDefSigDegPeriodOduTcmA_Type()
)
physicalPortDefSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmA.setUnits("s")


class _PhysicalPortDefSigDegPeriodOduTcmB_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodOduTcmB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodOduTcmB_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodOduTcmB_Object = MibTableColumn
physicalPortDefSigDegPeriodOduTcmB = _PhysicalPortDefSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 59),
    _PhysicalPortDefSigDegPeriodOduTcmB_Type()
)
physicalPortDefSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmB.setUnits("s")


class _PhysicalPortDefSigDegPeriodOduTcmC_Type(Unsigned32):
    """Custom type physicalPortDefSigDegPeriodOduTcmC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PhysicalPortDefSigDegPeriodOduTcmC_Type.__name__ = "Unsigned32"
_PhysicalPortDefSigDegPeriodOduTcmC_Object = MibTableColumn
physicalPortDefSigDegPeriodOduTcmC = _PhysicalPortDefSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 60),
    _PhysicalPortDefSigDegPeriodOduTcmC_Type()
)
physicalPortDefSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefSigDegPeriodOduTcmC.setUnits("s")
_PhysicalPortDefOtnStuffing_Type = FspR7Stuff
_PhysicalPortDefOtnStuffing_Object = MibTableColumn
physicalPortDefOtnStuffing = _PhysicalPortDefOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 61),
    _PhysicalPortDefOtnStuffing_Type()
)
physicalPortDefOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefOtnStuffing.setStatus("current")
_PhysicalPortDefTcmALevel_Type = OtnTcmLevel
_PhysicalPortDefTcmALevel_Object = MibTableColumn
physicalPortDefTcmALevel = _PhysicalPortDefTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 62),
    _PhysicalPortDefTcmALevel_Type()
)
physicalPortDefTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTcmALevel.setStatus("current")
_PhysicalPortDefTcmBLevel_Type = OtnTcmLevel
_PhysicalPortDefTcmBLevel_Object = MibTableColumn
physicalPortDefTcmBLevel = _PhysicalPortDefTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 63),
    _PhysicalPortDefTcmBLevel_Type()
)
physicalPortDefTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTcmBLevel.setStatus("current")
_PhysicalPortDefTcmCLevel_Type = OtnTcmLevel
_PhysicalPortDefTcmCLevel_Object = MibTableColumn
physicalPortDefTcmCLevel = _PhysicalPortDefTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 64),
    _PhysicalPortDefTcmCLevel_Type()
)
physicalPortDefTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTcmCLevel.setStatus("current")
_PhysicalPortDefTerminationLevel_Type = OhTerminationLevel
_PhysicalPortDefTerminationLevel_Object = MibTableColumn
physicalPortDefTerminationLevel = _PhysicalPortDefTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 65),
    _PhysicalPortDefTerminationLevel_Type()
)
physicalPortDefTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTerminationLevel.setStatus("current")
_PhysicalPortDefTimingSource_Type = SonetTimingSource
_PhysicalPortDefTimingSource_Object = MibTableColumn
physicalPortDefTimingSource = _PhysicalPortDefTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 66),
    _PhysicalPortDefTimingSource_Type()
)
physicalPortDefTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimingSource.setStatus("current")
_PhysicalPortDefTimModeOdu_Type = TimMode
_PhysicalPortDefTimModeOdu_Object = MibTableColumn
physicalPortDefTimModeOdu = _PhysicalPortDefTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 67),
    _PhysicalPortDefTimModeOdu_Type()
)
physicalPortDefTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeOdu.setStatus("current")
_PhysicalPortDefTimModeOtu_Type = TimMode
_PhysicalPortDefTimModeOtu_Object = MibTableColumn
physicalPortDefTimModeOtu = _PhysicalPortDefTimModeOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 68),
    _PhysicalPortDefTimModeOtu_Type()
)
physicalPortDefTimModeOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeOtu.setStatus("current")
_PhysicalPortDefTimModeSonetSection_Type = TimMode
_PhysicalPortDefTimModeSonetSection_Object = MibTableColumn
physicalPortDefTimModeSonetSection = _PhysicalPortDefTimModeSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 69),
    _PhysicalPortDefTimModeSonetSection_Type()
)
physicalPortDefTimModeSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeSonetSection.setStatus("current")
_PhysicalPortDefTimModeOduTcmA_Type = TimMode
_PhysicalPortDefTimModeOduTcmA_Object = MibTableColumn
physicalPortDefTimModeOduTcmA = _PhysicalPortDefTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 70),
    _PhysicalPortDefTimModeOduTcmA_Type()
)
physicalPortDefTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeOduTcmA.setStatus("current")
_PhysicalPortDefTimModeOduTcmB_Type = TimMode
_PhysicalPortDefTimModeOduTcmB_Object = MibTableColumn
physicalPortDefTimModeOduTcmB = _PhysicalPortDefTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 71),
    _PhysicalPortDefTimModeOduTcmB_Type()
)
physicalPortDefTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeOduTcmB.setStatus("current")
_PhysicalPortDefTimModeOduTcmC_Type = TimMode
_PhysicalPortDefTimModeOduTcmC_Object = MibTableColumn
physicalPortDefTimModeOduTcmC = _PhysicalPortDefTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 72),
    _PhysicalPortDefTimModeOduTcmC_Type()
)
physicalPortDefTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTimModeOduTcmC.setStatus("current")
_PhysicalPortDefTraceFormSonetSection_Type = SonetTraceForm
_PhysicalPortDefTraceFormSonetSection_Object = MibTableColumn
physicalPortDefTraceFormSonetSection = _PhysicalPortDefTraceFormSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 73),
    _PhysicalPortDefTraceFormSonetSection_Type()
)
physicalPortDefTraceFormSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceFormSonetSection.setStatus("current")


class _PhysicalPortDefTraceExpectedSonetSection_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedSonetSection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_PhysicalPortDefTraceExpectedSonetSection_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedSonetSection_Object = MibTableColumn
physicalPortDefTraceExpectedSonetSection = _PhysicalPortDefTraceExpectedSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 74),
    _PhysicalPortDefTraceExpectedSonetSection_Type()
)
physicalPortDefTraceExpectedSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedSonetSection.setStatus("current")


class _PhysicalPortDefTraceTransmitSonetSection_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSonetSection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_PhysicalPortDefTraceTransmitSonetSection_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSonetSection_Object = MibTableColumn
physicalPortDefTraceTransmitSonetSection = _PhysicalPortDefTraceTransmitSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 75),
    _PhysicalPortDefTraceTransmitSonetSection_Type()
)
physicalPortDefTraceTransmitSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSonetSection.setStatus("current")


class _PhysicalPortDefTraceExpectedOtu_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceExpectedOtu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedOtu_Object = MibTableColumn
physicalPortDefTraceExpectedOtu = _PhysicalPortDefTraceExpectedOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 76),
    _PhysicalPortDefTraceExpectedOtu_Type()
)
physicalPortDefTraceExpectedOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedOtu.setStatus("current")


class _PhysicalPortDefTraceTransmitSapiOtu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSapiOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitSapiOtu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSapiOtu_Object = MibTableColumn
physicalPortDefTraceTransmitSapiOtu = _PhysicalPortDefTraceTransmitSapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 77),
    _PhysicalPortDefTraceTransmitSapiOtu_Type()
)
physicalPortDefTraceTransmitSapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSapiOtu.setStatus("current")


class _PhysicalPortDefTraceTransmitDapiOtu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitDapiOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitDapiOtu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitDapiOtu_Object = MibTableColumn
physicalPortDefTraceTransmitDapiOtu = _PhysicalPortDefTraceTransmitDapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 78),
    _PhysicalPortDefTraceTransmitDapiOtu_Type()
)
physicalPortDefTraceTransmitDapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitDapiOtu.setStatus("current")


class _PhysicalPortDefTraceTransmitOpspOtu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitOpspOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalPortDefTraceTransmitOpspOtu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitOpspOtu_Object = MibTableColumn
physicalPortDefTraceTransmitOpspOtu = _PhysicalPortDefTraceTransmitOpspOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 79),
    _PhysicalPortDefTraceTransmitOpspOtu_Type()
)
physicalPortDefTraceTransmitOpspOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitOpspOtu.setStatus("current")


class _PhysicalPortDefTraceExpectedOdu_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceExpectedOdu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedOdu_Object = MibTableColumn
physicalPortDefTraceExpectedOdu = _PhysicalPortDefTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 80),
    _PhysicalPortDefTraceExpectedOdu_Type()
)
physicalPortDefTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedOdu.setStatus("current")


class _PhysicalPortDefTraceTransmitSapiOdu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitSapiOdu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSapiOdu_Object = MibTableColumn
physicalPortDefTraceTransmitSapiOdu = _PhysicalPortDefTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 81),
    _PhysicalPortDefTraceTransmitSapiOdu_Type()
)
physicalPortDefTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSapiOdu.setStatus("current")


class _PhysicalPortDefTraceTransmitDapiOdu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitDapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitDapiOdu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitDapiOdu_Object = MibTableColumn
physicalPortDefTraceTransmitDapiOdu = _PhysicalPortDefTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 82),
    _PhysicalPortDefTraceTransmitDapiOdu_Type()
)
physicalPortDefTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitDapiOdu.setStatus("current")


class _PhysicalPortDefTraceTransmitOpspOdu_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitOpspOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalPortDefTraceTransmitOpspOdu_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitOpspOdu_Object = MibTableColumn
physicalPortDefTraceTransmitOpspOdu = _PhysicalPortDefTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 83),
    _PhysicalPortDefTraceTransmitOpspOdu_Type()
)
physicalPortDefTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitOpspOdu.setStatus("current")


class _PhysicalPortDefTraceExpectedOduTcmA_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceExpectedOduTcmA_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedOduTcmA_Object = MibTableColumn
physicalPortDefTraceExpectedOduTcmA = _PhysicalPortDefTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 84),
    _PhysicalPortDefTraceExpectedOduTcmA_Type()
)
physicalPortDefTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedOduTcmA.setStatus("current")


class _PhysicalPortDefTraceTransmitSapiOduTcmA_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitSapiOduTcmA_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSapiOduTcmA_Object = MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmA = _PhysicalPortDefTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 85),
    _PhysicalPortDefTraceTransmitSapiOduTcmA_Type()
)
physicalPortDefTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSapiOduTcmA.setStatus("current")


class _PhysicalPortDefTraceTransmitDapiOduTcmA_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitDapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitDapiOduTcmA_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitDapiOduTcmA_Object = MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmA = _PhysicalPortDefTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 86),
    _PhysicalPortDefTraceTransmitDapiOduTcmA_Type()
)
physicalPortDefTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitDapiOduTcmA.setStatus("current")


class _PhysicalPortDefTraceTransmitOpspOduTcmA_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitOpspOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalPortDefTraceTransmitOpspOduTcmA_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitOpspOduTcmA_Object = MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmA = _PhysicalPortDefTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 87),
    _PhysicalPortDefTraceTransmitOpspOduTcmA_Type()
)
physicalPortDefTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitOpspOduTcmA.setStatus("current")


class _PhysicalPortDefTraceExpectedOduTcmB_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceExpectedOduTcmB_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedOduTcmB_Object = MibTableColumn
physicalPortDefTraceExpectedOduTcmB = _PhysicalPortDefTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 88),
    _PhysicalPortDefTraceExpectedOduTcmB_Type()
)
physicalPortDefTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedOduTcmB.setStatus("current")


class _PhysicalPortDefTraceTransmitSapiOduTcmB_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitSapiOduTcmB_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSapiOduTcmB_Object = MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmB = _PhysicalPortDefTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 89),
    _PhysicalPortDefTraceTransmitSapiOduTcmB_Type()
)
physicalPortDefTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSapiOduTcmB.setStatus("current")


class _PhysicalPortDefTraceTransmitDapiOduTcmB_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitDapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitDapiOduTcmB_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitDapiOduTcmB_Object = MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmB = _PhysicalPortDefTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 90),
    _PhysicalPortDefTraceTransmitDapiOduTcmB_Type()
)
physicalPortDefTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitDapiOduTcmB.setStatus("current")


class _PhysicalPortDefTraceTransmitOpspOduTcmB_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitOpspOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalPortDefTraceTransmitOpspOduTcmB_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitOpspOduTcmB_Object = MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmB = _PhysicalPortDefTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 91),
    _PhysicalPortDefTraceTransmitOpspOduTcmB_Type()
)
physicalPortDefTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitOpspOduTcmB.setStatus("current")


class _PhysicalPortDefTraceExpectedOduTcmC_Type(OctetString):
    """Custom type physicalPortDefTraceExpectedOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceExpectedOduTcmC_Type.__name__ = "OctetString"
_PhysicalPortDefTraceExpectedOduTcmC_Object = MibTableColumn
physicalPortDefTraceExpectedOduTcmC = _PhysicalPortDefTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 92),
    _PhysicalPortDefTraceExpectedOduTcmC_Type()
)
physicalPortDefTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceExpectedOduTcmC.setStatus("current")


class _PhysicalPortDefTraceTransmitSapiOduTcmC_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitSapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitSapiOduTcmC_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitSapiOduTcmC_Object = MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmC = _PhysicalPortDefTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 93),
    _PhysicalPortDefTraceTransmitSapiOduTcmC_Type()
)
physicalPortDefTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitSapiOduTcmC.setStatus("current")


class _PhysicalPortDefTraceTransmitDapiOduTcmC_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitDapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PhysicalPortDefTraceTransmitDapiOduTcmC_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitDapiOduTcmC_Object = MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmC = _PhysicalPortDefTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 94),
    _PhysicalPortDefTraceTransmitDapiOduTcmC_Type()
)
physicalPortDefTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitDapiOduTcmC.setStatus("current")


class _PhysicalPortDefTraceTransmitOpspOduTcmC_Type(OctetString):
    """Custom type physicalPortDefTraceTransmitOpspOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalPortDefTraceTransmitOpspOduTcmC_Type.__name__ = "OctetString"
_PhysicalPortDefTraceTransmitOpspOduTcmC_Object = MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmC = _PhysicalPortDefTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 95),
    _PhysicalPortDefTraceTransmitOpspOduTcmC_Type()
)
physicalPortDefTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTraceTransmitOpspOduTcmC.setStatus("current")
_PhysicalPortDefTurnupConfig_Type = FspR7TurnupConfig
_PhysicalPortDefTurnupConfig_Object = MibTableColumn
physicalPortDefTurnupConfig = _PhysicalPortDefTurnupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 96),
    _PhysicalPortDefTurnupConfig_Type()
)
physicalPortDefTurnupConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTurnupConfig.setStatus("current")
_PhysicalPortDefTxOffDelay_Type = FspR7EnableDisable
_PhysicalPortDefTxOffDelay_Object = MibTableColumn
physicalPortDefTxOffDelay = _PhysicalPortDefTxOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 97),
    _PhysicalPortDefTxOffDelay_Type()
)
physicalPortDefTxOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTxOffDelay.setStatus("current")
_PhysicalPortDefVoaMode_Type = FspR7VoaMode
_PhysicalPortDefVoaMode_Object = MibTableColumn
physicalPortDefVoaMode = _PhysicalPortDefVoaMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 98),
    _PhysicalPortDefVoaMode_Type()
)
physicalPortDefVoaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefVoaMode.setStatus("current")


class _PhysicalPortDefVoaSetpoint_Type(Unsigned32):
    """Custom type physicalPortDefVoaSetpoint based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PhysicalPortDefVoaSetpoint_Type.__name__ = "Unsigned32"
_PhysicalPortDefVoaSetpoint_Object = MibTableColumn
physicalPortDefVoaSetpoint = _PhysicalPortDefVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 99),
    _PhysicalPortDefVoaSetpoint_Type()
)
physicalPortDefVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefVoaSetpoint.setUnits("0.1 dB")


class _PhysicalPortDefLagPrio_Type(Unsigned32):
    """Custom type physicalPortDefLagPrio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhysicalPortDefLagPrio_Type.__name__ = "Unsigned32"
_PhysicalPortDefLagPrio_Object = MibTableColumn
physicalPortDefLagPrio = _PhysicalPortDefLagPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 100),
    _PhysicalPortDefLagPrio_Type()
)
physicalPortDefLagPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefLagPrio.setStatus("current")


class _PhysicalPortDefMaxFrameSize_Type(Unsigned32):
    """Custom type physicalPortDefMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_PhysicalPortDefMaxFrameSize_Type.__name__ = "Unsigned32"
_PhysicalPortDefMaxFrameSize_Object = MibTableColumn
physicalPortDefMaxFrameSize = _PhysicalPortDefMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 101),
    _PhysicalPortDefMaxFrameSize_Type()
)
physicalPortDefMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefMaxFrameSize.setStatus("current")
_PhysicalPortDefPayload_Type = OtnPayloadType
_PhysicalPortDefPayload_Object = MibTableColumn
physicalPortDefPayload = _PhysicalPortDefPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 102),
    _PhysicalPortDefPayload_Type()
)
physicalPortDefPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPayload.setStatus("current")
_PhysicalPortDefPortMode_Type = FspR7PortMode
_PhysicalPortDefPortMode_Object = MibTableColumn
physicalPortDefPortMode = _PhysicalPortDefPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 103),
    _PhysicalPortDefPortMode_Type()
)
physicalPortDefPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPortMode.setStatus("current")
_PhysicalPortDefPortRole_Type = FspR7PortRole
_PhysicalPortDefPortRole_Object = MibTableColumn
physicalPortDefPortRole = _PhysicalPortDefPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 104),
    _PhysicalPortDefPortRole_Type()
)
physicalPortDefPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPortRole.setStatus("current")


class _PhysicalPortDefPriority_Type(Unsigned32):
    """Custom type physicalPortDefPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PhysicalPortDefPriority_Type.__name__ = "Unsigned32"
_PhysicalPortDefPriority_Object = MibTableColumn
physicalPortDefPriority = _PhysicalPortDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 105),
    _PhysicalPortDefPriority_Type()
)
physicalPortDefPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPriority.setStatus("current")


class _PhysicalPortDefPvid_Type(Unsigned32):
    """Custom type physicalPortDefPvid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PhysicalPortDefPvid_Type.__name__ = "Unsigned32"
_PhysicalPortDefPvid_Object = MibTableColumn
physicalPortDefPvid = _PhysicalPortDefPvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 106),
    _PhysicalPortDefPvid_Type()
)
physicalPortDefPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefPvid.setStatus("current")
_PhysicalPortDefStagType_Type = FspR7SnmpHexString
_PhysicalPortDefStagType_Object = MibTableColumn
physicalPortDefStagType = _PhysicalPortDefStagType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 107),
    _PhysicalPortDefStagType_Type()
)
physicalPortDefStagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefStagType.setStatus("current")
_PhysicalPortDefUtag_Type = FspR7UntaggedFrames
_PhysicalPortDefUtag_Object = MibTableColumn
physicalPortDefUtag = _PhysicalPortDefUtag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 108),
    _PhysicalPortDefUtag_Type()
)
physicalPortDefUtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefUtag.setStatus("current")
_PhysicalPortDefVethAid_Type = SnmpAdminString
_PhysicalPortDefVethAid_Object = MibTableColumn
physicalPortDefVethAid = _PhysicalPortDefVethAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 109),
    _PhysicalPortDefVethAid_Type()
)
physicalPortDefVethAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefVethAid.setStatus("current")
_PhysicalPortDefRedLineState_Type = FspR7RedLinedState
_PhysicalPortDefRedLineState_Object = MibTableColumn
physicalPortDefRedLineState = _PhysicalPortDefRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 110),
    _PhysicalPortDefRedLineState_Type()
)
physicalPortDefRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefRedLineState.setStatus("current")
_PhysicalPortDefTunnelAid_Type = SnmpAdminString
_PhysicalPortDefTunnelAid_Object = MibTableColumn
physicalPortDefTunnelAid = _PhysicalPortDefTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 111),
    _PhysicalPortDefTunnelAid_Type()
)
physicalPortDefTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTunnelAid.setStatus("current")
_PhysicalPortDefRateLimit_Type = FspR7DisableEnable
_PhysicalPortDefRateLimit_Object = MibTableColumn
physicalPortDefRateLimit = _PhysicalPortDefRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 112),
    _PhysicalPortDefRateLimit_Type()
)
physicalPortDefRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefRateLimit.setStatus("current")
_PhysicalPortDefTxOffOnTm_Type = FspR7TxOffOnTm
_PhysicalPortDefTxOffOnTm_Object = MibTableColumn
physicalPortDefTxOffOnTm = _PhysicalPortDefTxOffOnTm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 113),
    _PhysicalPortDefTxOffOnTm_Type()
)
physicalPortDefTxOffOnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTxOffOnTm.setStatus("current")


class _PhysicalPortDefTxOffTimer_Type(Unsigned32):
    """Custom type physicalPortDefTxOffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PhysicalPortDefTxOffTimer_Type.__name__ = "Unsigned32"
_PhysicalPortDefTxOffTimer_Object = MibTableColumn
physicalPortDefTxOffTimer = _PhysicalPortDefTxOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 114),
    _PhysicalPortDefTxOffTimer_Type()
)
physicalPortDefTxOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTxOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefTxOffTimer.setUnits("ms")


class _PhysicalPortDefTxOnTimer_Type(Unsigned32):
    """Custom type physicalPortDefTxOnTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PhysicalPortDefTxOnTimer_Type.__name__ = "Unsigned32"
_PhysicalPortDefTxOnTimer_Object = MibTableColumn
physicalPortDefTxOnTimer = _PhysicalPortDefTxOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 1, 1, 115),
    _PhysicalPortDefTxOnTimer_Type()
)
physicalPortDefTxOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortDefTxOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    physicalPortDefTxOnTimer.setUnits("ms")
_VirtualPortDefTable_Object = MibTable
virtualPortDefTable = _VirtualPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2)
)
if mibBuilder.loadTexts:
    virtualPortDefTable.setStatus("current")
_VirtualPortDefEntry_Object = MibTableRow
virtualPortDefEntry = _VirtualPortDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1)
)
virtualPortDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    virtualPortDefEntry.setStatus("current")
_VirtualPortDefRowStatus_Type = RowStatus
_VirtualPortDefRowStatus_Object = MibTableColumn
virtualPortDefRowStatus = _VirtualPortDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 1),
    _VirtualPortDefRowStatus_Type()
)
virtualPortDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefRowStatus.setStatus("current")
_VirtualPortDefChannelBand_Type = FspR7ChannelBandwidth
_VirtualPortDefChannelBand_Object = MibTableColumn
virtualPortDefChannelBand = _VirtualPortDefChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 2),
    _VirtualPortDefChannelBand_Type()
)
virtualPortDefChannelBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefChannelBand.setStatus("current")
_VirtualPortDefType_Type = FspR7InterfaceType
_VirtualPortDefType_Object = MibTableColumn
virtualPortDefType = _VirtualPortDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 3),
    _VirtualPortDefType_Type()
)
virtualPortDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefType.setStatus("current")
_VirtualPortDefAlias_Type = SnmpAdminString
_VirtualPortDefAlias_Object = MibTableColumn
virtualPortDefAlias = _VirtualPortDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 4),
    _VirtualPortDefAlias_Type()
)
virtualPortDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefAlias.setStatus("current")
_VirtualPortDefAdmin_Type = FspR7AdminState
_VirtualPortDefAdmin_Object = MibTableColumn
virtualPortDefAdmin = _VirtualPortDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 5),
    _VirtualPortDefAdmin_Type()
)
virtualPortDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefAdmin.setStatus("current")
_VirtualPortDefEqlzAdmin_Type = FspR7EqlzAdminState
_VirtualPortDefEqlzAdmin_Object = MibTableColumn
virtualPortDefEqlzAdmin = _VirtualPortDefEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 6),
    _VirtualPortDefEqlzAdmin_Type()
)
virtualPortDefEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefEqlzAdmin.setStatus("current")
_VirtualPortDefInitEqlz_Type = FspR7InitEqualization
_VirtualPortDefInitEqlz_Object = MibTableColumn
virtualPortDefInitEqlz = _VirtualPortDefInitEqlz_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 7),
    _VirtualPortDefInitEqlz_Type()
)
virtualPortDefInitEqlz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefInitEqlz.setStatus("current")
_VirtualPortDefLacpMode_Type = FspR7LacpMode
_VirtualPortDefLacpMode_Object = MibTableColumn
virtualPortDefLacpMode = _VirtualPortDefLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 8),
    _VirtualPortDefLacpMode_Type()
)
virtualPortDefLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefLacpMode.setStatus("current")
_VirtualPortDefLacpTimeout_Type = FspR7LacpTimeout
_VirtualPortDefLacpTimeout_Object = MibTableColumn
virtualPortDefLacpTimeout = _VirtualPortDefLacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 9),
    _VirtualPortDefLacpTimeout_Type()
)
virtualPortDefLacpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefLacpTimeout.setStatus("current")


class _VirtualPortDefLagActivePorts_Type(Unsigned32):
    """Custom type virtualPortDefLagActivePorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_VirtualPortDefLagActivePorts_Type.__name__ = "Unsigned32"
_VirtualPortDefLagActivePorts_Object = MibTableColumn
virtualPortDefLagActivePorts = _VirtualPortDefLagActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 10),
    _VirtualPortDefLagActivePorts_Type()
)
virtualPortDefLagActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefLagActivePorts.setStatus("current")


class _VirtualPortDefMaxFrameSize_Type(Unsigned32):
    """Custom type virtualPortDefMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_VirtualPortDefMaxFrameSize_Type.__name__ = "Unsigned32"
_VirtualPortDefMaxFrameSize_Object = MibTableColumn
virtualPortDefMaxFrameSize = _VirtualPortDefMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 11),
    _VirtualPortDefMaxFrameSize_Type()
)
virtualPortDefMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefMaxFrameSize.setStatus("current")
_VirtualPortDefPortMode_Type = FspR7PortMode
_VirtualPortDefPortMode_Object = MibTableColumn
virtualPortDefPortMode = _VirtualPortDefPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 12),
    _VirtualPortDefPortMode_Type()
)
virtualPortDefPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefPortMode.setStatus("current")
_VirtualPortDefDataLayerPmReset_Type = FspR7PmReset
_VirtualPortDefDataLayerPmReset_Object = MibTableColumn
virtualPortDefDataLayerPmReset = _VirtualPortDefDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 13),
    _VirtualPortDefDataLayerPmReset_Type()
)
virtualPortDefDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefDataLayerPmReset.setStatus("current")
_VirtualPortDefPortRole_Type = FspR7PortRole
_VirtualPortDefPortRole_Object = MibTableColumn
virtualPortDefPortRole = _VirtualPortDefPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 14),
    _VirtualPortDefPortRole_Type()
)
virtualPortDefPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefPortRole.setStatus("current")
_VirtualPortDefLagPortType_Type = FspR7LagPortType
_VirtualPortDefLagPortType_Object = MibTableColumn
virtualPortDefLagPortType = _VirtualPortDefLagPortType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 15),
    _VirtualPortDefLagPortType_Type()
)
virtualPortDefLagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefLagPortType.setStatus("current")


class _VirtualPortDefPriority_Type(Unsigned32):
    """Custom type virtualPortDefPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VirtualPortDefPriority_Type.__name__ = "Unsigned32"
_VirtualPortDefPriority_Object = MibTableColumn
virtualPortDefPriority = _VirtualPortDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 16),
    _VirtualPortDefPriority_Type()
)
virtualPortDefPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefPriority.setStatus("current")


class _VirtualPortDefPvid_Type(Unsigned32):
    """Custom type virtualPortDefPvid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VirtualPortDefPvid_Type.__name__ = "Unsigned32"
_VirtualPortDefPvid_Object = MibTableColumn
virtualPortDefPvid = _VirtualPortDefPvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 17),
    _VirtualPortDefPvid_Type()
)
virtualPortDefPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefPvid.setStatus("current")
_VirtualPortDefRevertiveMode_Type = ApsRevertMode
_VirtualPortDefRevertiveMode_Object = MibTableColumn
virtualPortDefRevertiveMode = _VirtualPortDefRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 18),
    _VirtualPortDefRevertiveMode_Type()
)
virtualPortDefRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefRevertiveMode.setStatus("current")
_VirtualPortDefStagType_Type = FspR7SnmpHexString
_VirtualPortDefStagType_Object = MibTableColumn
virtualPortDefStagType = _VirtualPortDefStagType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 19),
    _VirtualPortDefStagType_Type()
)
virtualPortDefStagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefStagType.setStatus("current")
_VirtualPortDefUtag_Type = FspR7UntaggedFrames
_VirtualPortDefUtag_Object = MibTableColumn
virtualPortDefUtag = _VirtualPortDefUtag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 20),
    _VirtualPortDefUtag_Type()
)
virtualPortDefUtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefUtag.setStatus("current")
_VirtualPortDefBundle_Type = FspR7SnmpLongString
_VirtualPortDefBundle_Object = MibTableColumn
virtualPortDefBundle = _VirtualPortDefBundle_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 21),
    _VirtualPortDefBundle_Type()
)
virtualPortDefBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefBundle.setStatus("current")
_VirtualPortDefSwitchCommand_Type = FspR7APSCommand
_VirtualPortDefSwitchCommand_Object = MibTableColumn
virtualPortDefSwitchCommand = _VirtualPortDefSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 22),
    _VirtualPortDefSwitchCommand_Type()
)
virtualPortDefSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSwitchCommand.setStatus("current")
_VirtualPortDefInhibitSwitchToWork_Type = FspR7YesNo
_VirtualPortDefInhibitSwitchToWork_Object = MibTableColumn
virtualPortDefInhibitSwitchToWork = _VirtualPortDefInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 23),
    _VirtualPortDefInhibitSwitchToWork_Type()
)
virtualPortDefInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefInhibitSwitchToWork.setStatus("current")
_VirtualPortDefInhibitSwitchToProt_Type = FspR7YesNo
_VirtualPortDefInhibitSwitchToProt_Object = MibTableColumn
virtualPortDefInhibitSwitchToProt = _VirtualPortDefInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 24),
    _VirtualPortDefInhibitSwitchToProt_Type()
)
virtualPortDefInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefInhibitSwitchToProt.setStatus("current")
_VirtualPortDefOduTribPortNo_Type = SnmpAdminString
_VirtualPortDefOduTribPortNo_Object = MibTableColumn
virtualPortDefOduTribPortNo = _VirtualPortDefOduTribPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 25),
    _VirtualPortDefOduTribPortNo_Type()
)
virtualPortDefOduTribPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefOduTribPortNo.setStatus("current")
_VirtualPortDefOduTribTimeSlottNo_Type = SnmpAdminString
_VirtualPortDefOduTribTimeSlottNo_Object = MibTableColumn
virtualPortDefOduTribTimeSlottNo = _VirtualPortDefOduTribTimeSlottNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 26),
    _VirtualPortDefOduTribTimeSlottNo_Type()
)
virtualPortDefOduTribTimeSlottNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefOduTribTimeSlottNo.setStatus("current")


class _VirtualPortDefSigDegThresOdu_Type(Integer32):
    """Custom type virtualPortDefSigDegThresOdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualPortDefSigDegThresOdu_Type.__name__ = "Integer32"
_VirtualPortDefSigDegThresOdu_Object = MibTableColumn
virtualPortDefSigDegThresOdu = _VirtualPortDefSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 27),
    _VirtualPortDefSigDegThresOdu_Type()
)
virtualPortDefSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOdu.setUnits("%")


class _VirtualPortDefSigDegPeriodOdu_Type(Unsigned32):
    """Custom type virtualPortDefSigDegPeriodOdu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VirtualPortDefSigDegPeriodOdu_Type.__name__ = "Unsigned32"
_VirtualPortDefSigDegPeriodOdu_Object = MibTableColumn
virtualPortDefSigDegPeriodOdu = _VirtualPortDefSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 28),
    _VirtualPortDefSigDegPeriodOdu_Type()
)
virtualPortDefSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOdu.setUnits("s")


class _VirtualPortDefTraceExpectedOdu_Type(OctetString):
    """Custom type virtualPortDefTraceExpectedOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceExpectedOdu_Type.__name__ = "OctetString"
_VirtualPortDefTraceExpectedOdu_Object = MibTableColumn
virtualPortDefTraceExpectedOdu = _VirtualPortDefTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 29),
    _VirtualPortDefTraceExpectedOdu_Type()
)
virtualPortDefTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceExpectedOdu.setStatus("current")


class _VirtualPortDefTraceTransmitSapiOdu_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitSapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitSapiOdu_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitSapiOdu_Object = MibTableColumn
virtualPortDefTraceTransmitSapiOdu = _VirtualPortDefTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 30),
    _VirtualPortDefTraceTransmitSapiOdu_Type()
)
virtualPortDefTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitSapiOdu.setStatus("current")


class _VirtualPortDefTraceTransmitDapiOdu_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitDapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitDapiOdu_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitDapiOdu_Object = MibTableColumn
virtualPortDefTraceTransmitDapiOdu = _VirtualPortDefTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 31),
    _VirtualPortDefTraceTransmitDapiOdu_Type()
)
virtualPortDefTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitDapiOdu.setStatus("current")


class _VirtualPortDefTraceTransmitOpspOdu_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitOpspOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VirtualPortDefTraceTransmitOpspOdu_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitOpspOdu_Object = MibTableColumn
virtualPortDefTraceTransmitOpspOdu = _VirtualPortDefTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 32),
    _VirtualPortDefTraceTransmitOpspOdu_Type()
)
virtualPortDefTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitOpspOdu.setStatus("current")
_VirtualPortDefTimModeOdu_Type = TimMode
_VirtualPortDefTimModeOdu_Object = MibTableColumn
virtualPortDefTimModeOdu = _VirtualPortDefTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 33),
    _VirtualPortDefTimModeOdu_Type()
)
virtualPortDefTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTimModeOdu.setStatus("current")


class _VirtualPortDefSigDegThresOduTcmA_Type(Integer32):
    """Custom type virtualPortDefSigDegThresOduTcmA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualPortDefSigDegThresOduTcmA_Type.__name__ = "Integer32"
_VirtualPortDefSigDegThresOduTcmA_Object = MibTableColumn
virtualPortDefSigDegThresOduTcmA = _VirtualPortDefSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 34),
    _VirtualPortDefSigDegThresOduTcmA_Type()
)
virtualPortDefSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmA.setUnits("%")


class _VirtualPortDefSigDegPeriodOduTcmA_Type(Unsigned32):
    """Custom type virtualPortDefSigDegPeriodOduTcmA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VirtualPortDefSigDegPeriodOduTcmA_Type.__name__ = "Unsigned32"
_VirtualPortDefSigDegPeriodOduTcmA_Object = MibTableColumn
virtualPortDefSigDegPeriodOduTcmA = _VirtualPortDefSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 35),
    _VirtualPortDefSigDegPeriodOduTcmA_Type()
)
virtualPortDefSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmA.setUnits("s")


class _VirtualPortDefSigDegThresOduTcmB_Type(Integer32):
    """Custom type virtualPortDefSigDegThresOduTcmB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualPortDefSigDegThresOduTcmB_Type.__name__ = "Integer32"
_VirtualPortDefSigDegThresOduTcmB_Object = MibTableColumn
virtualPortDefSigDegThresOduTcmB = _VirtualPortDefSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 36),
    _VirtualPortDefSigDegThresOduTcmB_Type()
)
virtualPortDefSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmB.setUnits("%")


class _VirtualPortDefSigDegPeriodOduTcmB_Type(Unsigned32):
    """Custom type virtualPortDefSigDegPeriodOduTcmB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VirtualPortDefSigDegPeriodOduTcmB_Type.__name__ = "Unsigned32"
_VirtualPortDefSigDegPeriodOduTcmB_Object = MibTableColumn
virtualPortDefSigDegPeriodOduTcmB = _VirtualPortDefSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 37),
    _VirtualPortDefSigDegPeriodOduTcmB_Type()
)
virtualPortDefSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmB.setUnits("s")


class _VirtualPortDefSigDegThresOduTcmC_Type(Integer32):
    """Custom type virtualPortDefSigDegThresOduTcmC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VirtualPortDefSigDegThresOduTcmC_Type.__name__ = "Integer32"
_VirtualPortDefSigDegThresOduTcmC_Object = MibTableColumn
virtualPortDefSigDegThresOduTcmC = _VirtualPortDefSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 38),
    _VirtualPortDefSigDegThresOduTcmC_Type()
)
virtualPortDefSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegThresOduTcmC.setUnits("%")


class _VirtualPortDefSigDegPeriodOduTcmC_Type(Unsigned32):
    """Custom type virtualPortDefSigDegPeriodOduTcmC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VirtualPortDefSigDegPeriodOduTcmC_Type.__name__ = "Unsigned32"
_VirtualPortDefSigDegPeriodOduTcmC_Object = MibTableColumn
virtualPortDefSigDegPeriodOduTcmC = _VirtualPortDefSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 39),
    _VirtualPortDefSigDegPeriodOduTcmC_Type()
)
virtualPortDefSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefSigDegPeriodOduTcmC.setUnits("s")
_VirtualPortDefTcmALevel_Type = OtnTcmLevel
_VirtualPortDefTcmALevel_Object = MibTableColumn
virtualPortDefTcmALevel = _VirtualPortDefTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 40),
    _VirtualPortDefTcmALevel_Type()
)
virtualPortDefTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTcmALevel.setStatus("current")
_VirtualPortDefTcmBLevel_Type = OtnTcmLevel
_VirtualPortDefTcmBLevel_Object = MibTableColumn
virtualPortDefTcmBLevel = _VirtualPortDefTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 41),
    _VirtualPortDefTcmBLevel_Type()
)
virtualPortDefTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTcmBLevel.setStatus("current")
_VirtualPortDefTcmCLevel_Type = OtnTcmLevel
_VirtualPortDefTcmCLevel_Object = MibTableColumn
virtualPortDefTcmCLevel = _VirtualPortDefTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 42),
    _VirtualPortDefTcmCLevel_Type()
)
virtualPortDefTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTcmCLevel.setStatus("current")


class _VirtualPortDefTraceTransmitSapiOduTcmA_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitSapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitSapiOduTcmA_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitSapiOduTcmA_Object = MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmA = _VirtualPortDefTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 43),
    _VirtualPortDefTraceTransmitSapiOduTcmA_Type()
)
virtualPortDefTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitSapiOduTcmA.setStatus("current")


class _VirtualPortDefTraceTransmitDapiOduTcmA_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitDapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitDapiOduTcmA_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitDapiOduTcmA_Object = MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmA = _VirtualPortDefTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 44),
    _VirtualPortDefTraceTransmitDapiOduTcmA_Type()
)
virtualPortDefTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitDapiOduTcmA.setStatus("current")


class _VirtualPortDefTraceTransmitOpspOduTcmA_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitOpspOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VirtualPortDefTraceTransmitOpspOduTcmA_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitOpspOduTcmA_Object = MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmA = _VirtualPortDefTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 45),
    _VirtualPortDefTraceTransmitOpspOduTcmA_Type()
)
virtualPortDefTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitOpspOduTcmA.setStatus("current")


class _VirtualPortDefTraceExpectedOduTcmA_Type(OctetString):
    """Custom type virtualPortDefTraceExpectedOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceExpectedOduTcmA_Type.__name__ = "OctetString"
_VirtualPortDefTraceExpectedOduTcmA_Object = MibTableColumn
virtualPortDefTraceExpectedOduTcmA = _VirtualPortDefTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 46),
    _VirtualPortDefTraceExpectedOduTcmA_Type()
)
virtualPortDefTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceExpectedOduTcmA.setStatus("current")
_VirtualPortDefTimModeOduTcmA_Type = TimMode
_VirtualPortDefTimModeOduTcmA_Object = MibTableColumn
virtualPortDefTimModeOduTcmA = _VirtualPortDefTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 47),
    _VirtualPortDefTimModeOduTcmA_Type()
)
virtualPortDefTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTimModeOduTcmA.setStatus("current")


class _VirtualPortDefTraceExpectedOduTcmB_Type(OctetString):
    """Custom type virtualPortDefTraceExpectedOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceExpectedOduTcmB_Type.__name__ = "OctetString"
_VirtualPortDefTraceExpectedOduTcmB_Object = MibTableColumn
virtualPortDefTraceExpectedOduTcmB = _VirtualPortDefTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 48),
    _VirtualPortDefTraceExpectedOduTcmB_Type()
)
virtualPortDefTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceExpectedOduTcmB.setStatus("current")


class _VirtualPortDefTraceTransmitSapiOduTcmB_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitSapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitSapiOduTcmB_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitSapiOduTcmB_Object = MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmB = _VirtualPortDefTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 49),
    _VirtualPortDefTraceTransmitSapiOduTcmB_Type()
)
virtualPortDefTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitSapiOduTcmB.setStatus("current")


class _VirtualPortDefTraceTransmitDapiOduTcmB_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitDapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitDapiOduTcmB_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitDapiOduTcmB_Object = MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmB = _VirtualPortDefTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 50),
    _VirtualPortDefTraceTransmitDapiOduTcmB_Type()
)
virtualPortDefTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitDapiOduTcmB.setStatus("current")


class _VirtualPortDefTraceTransmitOpspOduTcmB_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitOpspOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VirtualPortDefTraceTransmitOpspOduTcmB_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitOpspOduTcmB_Object = MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmB = _VirtualPortDefTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 51),
    _VirtualPortDefTraceTransmitOpspOduTcmB_Type()
)
virtualPortDefTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitOpspOduTcmB.setStatus("current")
_VirtualPortDefTimModeOduTcmB_Type = TimMode
_VirtualPortDefTimModeOduTcmB_Object = MibTableColumn
virtualPortDefTimModeOduTcmB = _VirtualPortDefTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 52),
    _VirtualPortDefTimModeOduTcmB_Type()
)
virtualPortDefTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTimModeOduTcmB.setStatus("current")


class _VirtualPortDefTraceExpectedOduTcmC_Type(OctetString):
    """Custom type virtualPortDefTraceExpectedOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceExpectedOduTcmC_Type.__name__ = "OctetString"
_VirtualPortDefTraceExpectedOduTcmC_Object = MibTableColumn
virtualPortDefTraceExpectedOduTcmC = _VirtualPortDefTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 53),
    _VirtualPortDefTraceExpectedOduTcmC_Type()
)
virtualPortDefTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceExpectedOduTcmC.setStatus("current")


class _VirtualPortDefTraceTransmitSapiOduTcmC_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitSapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitSapiOduTcmC_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitSapiOduTcmC_Object = MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmC = _VirtualPortDefTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 54),
    _VirtualPortDefTraceTransmitSapiOduTcmC_Type()
)
virtualPortDefTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitSapiOduTcmC.setStatus("current")


class _VirtualPortDefTraceTransmitDapiOduTcmC_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitDapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VirtualPortDefTraceTransmitDapiOduTcmC_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitDapiOduTcmC_Object = MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmC = _VirtualPortDefTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 55),
    _VirtualPortDefTraceTransmitDapiOduTcmC_Type()
)
virtualPortDefTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitDapiOduTcmC.setStatus("current")


class _VirtualPortDefTraceTransmitOpspOduTcmC_Type(OctetString):
    """Custom type virtualPortDefTraceTransmitOpspOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VirtualPortDefTraceTransmitOpspOduTcmC_Type.__name__ = "OctetString"
_VirtualPortDefTraceTransmitOpspOduTcmC_Object = MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmC = _VirtualPortDefTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 56),
    _VirtualPortDefTraceTransmitOpspOduTcmC_Type()
)
virtualPortDefTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTraceTransmitOpspOduTcmC.setStatus("current")
_VirtualPortDefTimModeOduTcmC_Type = TimMode
_VirtualPortDefTimModeOduTcmC_Object = MibTableColumn
virtualPortDefTimModeOduTcmC = _VirtualPortDefTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 57),
    _VirtualPortDefTimModeOduTcmC_Type()
)
virtualPortDefTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTimModeOduTcmC.setStatus("current")
_VirtualPortDefTerminationLevel_Type = OhTerminationLevel
_VirtualPortDefTerminationLevel_Object = MibTableColumn
virtualPortDefTerminationLevel = _VirtualPortDefTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 58),
    _VirtualPortDefTerminationLevel_Type()
)
virtualPortDefTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTerminationLevel.setStatus("current")
_VirtualPortDefLoopConfig_Type = LoopConfig
_VirtualPortDefLoopConfig_Object = MibTableColumn
virtualPortDefLoopConfig = _VirtualPortDefLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 59),
    _VirtualPortDefLoopConfig_Type()
)
virtualPortDefLoopConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefLoopConfig.setStatus("current")
_VirtualPortDefVcType_Type = VirtualContainerType
_VirtualPortDefVcType_Object = MibTableColumn
virtualPortDefVcType = _VirtualPortDefVcType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 60),
    _VirtualPortDefVcType_Type()
)
virtualPortDefVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefVcType.setStatus("current")
_VirtualPortDefCir_Type = Unsigned32
_VirtualPortDefCir_Object = MibTableColumn
virtualPortDefCir = _VirtualPortDefCir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 61),
    _VirtualPortDefCir_Type()
)
virtualPortDefCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefCir.setStatus("current")
if mibBuilder.loadTexts:
    virtualPortDefCir.setUnits("Mbps")
_VirtualPortDefOpuPayloadType_Type = FspR7OpuPayloadType
_VirtualPortDefOpuPayloadType_Object = MibTableColumn
virtualPortDefOpuPayloadType = _VirtualPortDefOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 62),
    _VirtualPortDefOpuPayloadType_Type()
)
virtualPortDefOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefOpuPayloadType.setStatus("current")
_VirtualPortDefOtnStuffing_Type = FspR7Stuff
_VirtualPortDefOtnStuffing_Object = MibTableColumn
virtualPortDefOtnStuffing = _VirtualPortDefOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 63),
    _VirtualPortDefOtnStuffing_Type()
)
virtualPortDefOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefOtnStuffing.setStatus("current")
_VirtualPortDefRedLineState_Type = FspR7RedLinedState
_VirtualPortDefRedLineState_Object = MibTableColumn
virtualPortDefRedLineState = _VirtualPortDefRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 64),
    _VirtualPortDefRedLineState_Type()
)
virtualPortDefRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefRedLineState.setStatus("current")
_VirtualPortDefTunnelAid_Type = SnmpAdminString
_VirtualPortDefTunnelAid_Object = MibTableColumn
virtualPortDefTunnelAid = _VirtualPortDefTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 2, 1, 65),
    _VirtualPortDefTunnelAid_Type()
)
virtualPortDefTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPortDefTunnelAid.setStatus("current")
_EndOfVirtualPortDefTable_Type = Integer32
_EndOfVirtualPortDefTable_Object = MibScalar
endOfVirtualPortDefTable = _EndOfVirtualPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 3),
    _EndOfVirtualPortDefTable_Type()
)
endOfVirtualPortDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfVirtualPortDefTable.setStatus("current")
_EndOfFacilityMgmtDef_Type = Integer32
_EndOfFacilityMgmtDef_Object = MibScalar
endOfFacilityMgmtDef = _EndOfFacilityMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 4, 10000),
    _EndOfFacilityMgmtDef_Type()
)
endOfFacilityMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFacilityMgmtDef.setStatus("current")
_DcnMgmtDef_ObjectIdentity = ObjectIdentity
dcnMgmtDef = _DcnMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5)
)
_LinkDefTable_Object = MibTable
linkDefTable = _LinkDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1)
)
if mibBuilder.loadTexts:
    linkDefTable.setStatus("current")
_LinkDefEntry_Object = MibTableRow
linkDefEntry = _LinkDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1)
)
linkDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    linkDefEntry.setStatus("current")
_LinkDefRowStatus_Type = RowStatus
_LinkDefRowStatus_Object = MibTableColumn
linkDefRowStatus = _LinkDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 1),
    _LinkDefRowStatus_Type()
)
linkDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefRowStatus.setStatus("current")
_LinkDefType_Type = FspR7InterfaceType
_LinkDefType_Object = MibTableColumn
linkDefType = _LinkDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 2),
    _LinkDefType_Type()
)
linkDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefType.setStatus("current")
_LinkDefAdmin_Type = FspR7AdminState
_LinkDefAdmin_Object = MibTableColumn
linkDefAdmin = _LinkDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 3),
    _LinkDefAdmin_Type()
)
linkDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefAdmin.setStatus("current")
_LinkDefAlias_Type = SnmpAdminString
_LinkDefAlias_Object = MibTableColumn
linkDefAlias = _LinkDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 4),
    _LinkDefAlias_Type()
)
linkDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefAlias.setStatus("current")
_LinkDefAuthString_Type = SnmpAdminString
_LinkDefAuthString_Object = MibTableColumn
linkDefAuthString = _LinkDefAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 5),
    _LinkDefAuthString_Type()
)
linkDefAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefAuthString.setStatus("current")
_LinkDefProxyArp_Type = FspR7NoYes
_LinkDefProxyArp_Object = MibTableColumn
linkDefProxyArp = _LinkDefProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 6),
    _LinkDefProxyArp_Type()
)
linkDefProxyArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefProxyArp.setStatus("current")
_LinkDefOspf_Type = FspR7OspfMode
_LinkDefOspf_Object = MibTableColumn
linkDefOspf = _LinkDefOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 7),
    _LinkDefOspf_Type()
)
linkDefOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefOspf.setStatus("current")
_LinkDefBaud_Type = FspR7Baund
_LinkDefBaud_Object = MibTableColumn
linkDefBaud = _LinkDefBaud_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 8),
    _LinkDefBaud_Type()
)
linkDefBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefBaud.setStatus("current")
_LinkDefAuthType_Type = FspR7CpAuthType
_LinkDefAuthType_Object = MibTableColumn
linkDefAuthType = _LinkDefAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 9),
    _LinkDefAuthType_Type()
)
linkDefAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefAuthType.setStatus("current")
_LinkDefIpType_Type = FspR7IpType
_LinkDefIpType_Object = MibTableColumn
linkDefIpType = _LinkDefIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 10),
    _LinkDefIpType_Type()
)
linkDefIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefIpType.setStatus("current")


class _LinkDefMetric_Type(Unsigned32):
    """Custom type linkDefMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LinkDefMetric_Type.__name__ = "Unsigned32"
_LinkDefMetric_Object = MibTableColumn
linkDefMetric = _LinkDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 11),
    _LinkDefMetric_Type()
)
linkDefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefMetric.setStatus("current")
_LinkDefAreaAid_Type = SnmpAdminString
_LinkDefAreaAid_Object = MibTableColumn
linkDefAreaAid = _LinkDefAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 12),
    _LinkDefAreaAid_Type()
)
linkDefAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefAreaAid.setStatus("current")
_LinkDefNearEndIp_Type = IpAddress
_LinkDefNearEndIp_Object = MibTableColumn
linkDefNearEndIp = _LinkDefNearEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 13),
    _LinkDefNearEndIp_Type()
)
linkDefNearEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefNearEndIp.setStatus("current")


class _LinkDefBitrate_Type(Unsigned32):
    """Custom type linkDefBitrate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13702),
    )


_LinkDefBitrate_Type.__name__ = "Unsigned32"
_LinkDefBitrate_Object = MibTableColumn
linkDefBitrate = _LinkDefBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 14),
    _LinkDefBitrate_Type()
)
linkDefBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefBitrate.setStatus("current")
if mibBuilder.loadTexts:
    linkDefBitrate.setUnits("kbps")
_LinkDefIPv6Type_Type = FspR7IPv6Type
_LinkDefIPv6Type_Object = MibTableColumn
linkDefIPv6Type = _LinkDefIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 15),
    _LinkDefIPv6Type_Type()
)
linkDefIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefIPv6Type.setStatus("current")
_LinkDefNendIPv6_Type = SnmpAdminString
_LinkDefNendIPv6_Object = MibTableColumn
linkDefNendIPv6 = _LinkDefNendIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 1, 1, 16),
    _LinkDefNendIPv6_Type()
)
linkDefNendIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDefNendIPv6.setStatus("current")
_EndOfLinkDefTable_Type = Integer32
_EndOfLinkDefTable_Object = MibScalar
endOfLinkDefTable = _EndOfLinkDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 2),
    _EndOfLinkDefTable_Type()
)
endOfLinkDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfLinkDefTable.setStatus("current")
_ScDefTable_Object = MibTable
scDefTable = _ScDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3)
)
if mibBuilder.loadTexts:
    scDefTable.setStatus("current")
_ScDefEntry_Object = MibTableRow
scDefEntry = _ScDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1)
)
scDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    scDefEntry.setStatus("current")
_ScDefRowStatus_Type = RowStatus
_ScDefRowStatus_Object = MibTableColumn
scDefRowStatus = _ScDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 1),
    _ScDefRowStatus_Type()
)
scDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefRowStatus.setStatus("current")
_ScDefType_Type = FspR7InterfaceType
_ScDefType_Object = MibTableColumn
scDefType = _ScDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 2),
    _ScDefType_Type()
)
scDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefType.setStatus("current")
_ScDefAdmin_Type = FspR7AdminState
_ScDefAdmin_Object = MibTableColumn
scDefAdmin = _ScDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 3),
    _ScDefAdmin_Type()
)
scDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAdmin.setStatus("current")
_ScDefAlias_Type = SnmpAdminString
_ScDefAlias_Object = MibTableColumn
scDefAlias = _ScDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 4),
    _ScDefAlias_Type()
)
scDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAlias.setStatus("current")
_ScDefAuthString_Type = SnmpAdminString
_ScDefAuthString_Object = MibTableColumn
scDefAuthString = _ScDefAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 5),
    _ScDefAuthString_Type()
)
scDefAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAuthString.setStatus("current")
_ScDefOspf_Type = FspR7OspfMode
_ScDefOspf_Object = MibTableColumn
scDefOspf = _ScDefOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 6),
    _ScDefOspf_Type()
)
scDefOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefOspf.setStatus("current")
_ScDefAuthType_Type = FspR7CpAuthType
_ScDefAuthType_Object = MibTableColumn
scDefAuthType = _ScDefAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 7),
    _ScDefAuthType_Type()
)
scDefAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAuthType.setStatus("current")
_ScDefIpType_Type = FspR7IpType
_ScDefIpType_Object = MibTableColumn
scDefIpType = _ScDefIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 8),
    _ScDefIpType_Type()
)
scDefIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIpType.setStatus("current")


class _ScDefMetric_Type(Unsigned32):
    """Custom type scDefMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScDefMetric_Type.__name__ = "Unsigned32"
_ScDefMetric_Object = MibTableColumn
scDefMetric = _ScDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 9),
    _ScDefMetric_Type()
)
scDefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefMetric.setStatus("current")
_ScDefAreaAid_Type = SnmpAdminString
_ScDefAreaAid_Object = MibTableColumn
scDefAreaAid = _ScDefAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 10),
    _ScDefAreaAid_Type()
)
scDefAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAreaAid.setStatus("current")
_ScDefAlsMode_Type = FspR7AlsMode
_ScDefAlsMode_Object = MibTableColumn
scDefAlsMode = _ScDefAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 11),
    _ScDefAlsMode_Type()
)
scDefAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAlsMode.setStatus("current")
_ScDefSigDegThresReceiver_Type = Unsigned32
_ScDefSigDegThresReceiver_Object = MibTableColumn
scDefSigDegThresReceiver = _ScDefSigDegThresReceiver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 12),
    _ScDefSigDegThresReceiver_Type()
)
scDefSigDegThresReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefSigDegThresReceiver.setStatus("current")
if mibBuilder.loadTexts:
    scDefSigDegThresReceiver.setUnits("0.1 dB")
_ScDefAutonegotiation_Type = EnableState
_ScDefAutonegotiation_Object = MibTableColumn
scDefAutonegotiation = _ScDefAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 13),
    _ScDefAutonegotiation_Type()
)
scDefAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAutonegotiation.setStatus("current")
_ScDefBitrate_Type = FspR7Bitrate
_ScDefBitrate_Object = MibTableColumn
scDefBitrate = _ScDefBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 14),
    _ScDefBitrate_Type()
)
scDefBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefBitrate.setStatus("current")
_ScDefDuplex_Type = EthDuplexMode
_ScDefDuplex_Object = MibTableColumn
scDefDuplex = _ScDefDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 15),
    _ScDefDuplex_Type()
)
scDefDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefDuplex.setStatus("current")


class _ScDefAttGradientTh_Type(Unsigned32):
    """Custom type scDefAttGradientTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ScDefAttGradientTh_Type.__name__ = "Unsigned32"
_ScDefAttGradientTh_Object = MibTableColumn
scDefAttGradientTh = _ScDefAttGradientTh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 16),
    _ScDefAttGradientTh_Type()
)
scDefAttGradientTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefAttGradientTh.setStatus("current")
if mibBuilder.loadTexts:
    scDefAttGradientTh.setUnits("0.1 dB/min")
_ScDefIpAddr_Type = IpAddress
_ScDefIpAddr_Object = MibTableColumn
scDefIpAddr = _ScDefIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 17),
    _ScDefIpAddr_Type()
)
scDefIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIpAddr.setStatus("current")
_ScDefLanAid_Type = SnmpAdminString
_ScDefLanAid_Object = MibTableColumn
scDefLanAid = _ScDefLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 18),
    _ScDefLanAid_Type()
)
scDefLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefLanAid.setStatus("current")
_ScDefIpMask_Type = IpAddress
_ScDefIpMask_Object = MibTableColumn
scDefIpMask = _ScDefIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 19),
    _ScDefIpMask_Type()
)
scDefIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIpMask.setStatus("current")
_ScDefDataLayerPmReset_Type = FspR7PmReset
_ScDefDataLayerPmReset_Object = MibTableColumn
scDefDataLayerPmReset = _ScDefDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 20),
    _ScDefDataLayerPmReset_Type()
)
scDefDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefDataLayerPmReset.setStatus("current")


class _ScDefPriority_Type(Unsigned32):
    """Custom type scDefPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ScDefPriority_Type.__name__ = "Unsigned32"
_ScDefPriority_Object = MibTableColumn
scDefPriority = _ScDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 21),
    _ScDefPriority_Type()
)
scDefPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefPriority.setStatus("current")
_ScDefIPv6_Type = SnmpAdminString
_ScDefIPv6_Object = MibTableColumn
scDefIPv6 = _ScDefIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 22),
    _ScDefIPv6_Type()
)
scDefIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIPv6.setStatus("current")


class _ScDefIPv6PrefixLen_Type(Unsigned32):
    """Custom type scDefIPv6PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ScDefIPv6PrefixLen_Type.__name__ = "Unsigned32"
_ScDefIPv6PrefixLen_Object = MibTableColumn
scDefIPv6PrefixLen = _ScDefIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 23),
    _ScDefIPv6PrefixLen_Type()
)
scDefIPv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIPv6PrefixLen.setStatus("current")
_ScDefIpMode_Type = FspR7IpMode
_ScDefIpMode_Object = MibTableColumn
scDefIpMode = _ScDefIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 24),
    _ScDefIpMode_Type()
)
scDefIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefIpMode.setStatus("current")
_ScDefGatewayProxyArp_Type = FspR7EnableDisable
_ScDefGatewayProxyArp_Object = MibTableColumn
scDefGatewayProxyArp = _ScDefGatewayProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 3, 1, 25),
    _ScDefGatewayProxyArp_Type()
)
scDefGatewayProxyArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDefGatewayProxyArp.setStatus("current")
_EndOfScDefTable_Type = Integer32
_EndOfScDefTable_Object = MibScalar
endOfScDefTable = _EndOfScDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 4),
    _EndOfScDefTable_Type()
)
endOfScDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfScDefTable.setStatus("current")
_LanDefTable_Object = MibTable
lanDefTable = _LanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5)
)
if mibBuilder.loadTexts:
    lanDefTable.setStatus("current")
_LanDefEntry_Object = MibTableRow
lanDefEntry = _LanDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1)
)
lanDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    lanDefEntry.setStatus("current")
_LanDefRowStatus_Type = RowStatus
_LanDefRowStatus_Object = MibTableColumn
lanDefRowStatus = _LanDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 1),
    _LanDefRowStatus_Type()
)
lanDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefRowStatus.setStatus("current")
_LanDefType_Type = FspR7InterfaceType
_LanDefType_Object = MibTableColumn
lanDefType = _LanDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 2),
    _LanDefType_Type()
)
lanDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefType.setStatus("current")
_LanDefAdmin_Type = FspR7AdminState
_LanDefAdmin_Object = MibTableColumn
lanDefAdmin = _LanDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 3),
    _LanDefAdmin_Type()
)
lanDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefAdmin.setStatus("current")
_LanDefAlias_Type = SnmpAdminString
_LanDefAlias_Object = MibTableColumn
lanDefAlias = _LanDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 4),
    _LanDefAlias_Type()
)
lanDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefAlias.setStatus("current")
_LanDefAuthString_Type = SnmpAdminString
_LanDefAuthString_Object = MibTableColumn
lanDefAuthString = _LanDefAuthString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 5),
    _LanDefAuthString_Type()
)
lanDefAuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefAuthString.setStatus("current")
_LanDefOspf_Type = FspR7OspfMode
_LanDefOspf_Object = MibTableColumn
lanDefOspf = _LanDefOspf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 6),
    _LanDefOspf_Type()
)
lanDefOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefOspf.setStatus("current")
_LanDefAuthType_Type = FspR7CpAuthType
_LanDefAuthType_Object = MibTableColumn
lanDefAuthType = _LanDefAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 7),
    _LanDefAuthType_Type()
)
lanDefAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefAuthType.setStatus("current")
_LanDefIpType_Type = FspR7IpType
_LanDefIpType_Object = MibTableColumn
lanDefIpType = _LanDefIpType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 8),
    _LanDefIpType_Type()
)
lanDefIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIpType.setStatus("current")


class _LanDefMetric_Type(Unsigned32):
    """Custom type lanDefMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LanDefMetric_Type.__name__ = "Unsigned32"
_LanDefMetric_Object = MibTableColumn
lanDefMetric = _LanDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 9),
    _LanDefMetric_Type()
)
lanDefMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefMetric.setStatus("current")
_LanDefAreaAid_Type = SnmpAdminString
_LanDefAreaAid_Object = MibTableColumn
lanDefAreaAid = _LanDefAreaAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 10),
    _LanDefAreaAid_Type()
)
lanDefAreaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefAreaAid.setStatus("current")
_LanDefIpAddr_Type = IpAddress
_LanDefIpAddr_Object = MibTableColumn
lanDefIpAddr = _LanDefIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 11),
    _LanDefIpAddr_Type()
)
lanDefIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIpAddr.setStatus("current")
_LanDefIpMask_Type = IpAddress
_LanDefIpMask_Object = MibTableColumn
lanDefIpMask = _LanDefIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 12),
    _LanDefIpMask_Type()
)
lanDefIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIpMask.setStatus("current")


class _LanDefPriority_Type(Unsigned32):
    """Custom type lanDefPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LanDefPriority_Type.__name__ = "Unsigned32"
_LanDefPriority_Object = MibTableColumn
lanDefPriority = _LanDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 13),
    _LanDefPriority_Type()
)
lanDefPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefPriority.setStatus("current")
_LanDefIPv6_Type = SnmpAdminString
_LanDefIPv6_Object = MibTableColumn
lanDefIPv6 = _LanDefIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 14),
    _LanDefIPv6_Type()
)
lanDefIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIPv6.setStatus("current")


class _LanDefIPv6PrefixLen_Type(Unsigned32):
    """Custom type lanDefIPv6PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_LanDefIPv6PrefixLen_Type.__name__ = "Unsigned32"
_LanDefIPv6PrefixLen_Object = MibTableColumn
lanDefIPv6PrefixLen = _LanDefIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 15),
    _LanDefIPv6PrefixLen_Type()
)
lanDefIPv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIPv6PrefixLen.setStatus("current")
_LanDefIpMode_Type = FspR7IpMode
_LanDefIpMode_Object = MibTableColumn
lanDefIpMode = _LanDefIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 5, 1, 16),
    _LanDefIpMode_Type()
)
lanDefIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefIpMode.setStatus("current")
_EndOfLanDefTable_Type = Integer32
_EndOfLanDefTable_Object = MibScalar
endOfLanDefTable = _EndOfLanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 6),
    _EndOfLanDefTable_Type()
)
endOfLanDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfLanDefTable.setStatus("current")
_EccDefTable_Object = MibTable
eccDefTable = _EccDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7)
)
if mibBuilder.loadTexts:
    eccDefTable.setStatus("current")
_EccDefEntry_Object = MibTableRow
eccDefEntry = _EccDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1)
)
eccDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityDcnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityDcnClassName"),
)
if mibBuilder.loadTexts:
    eccDefEntry.setStatus("current")
_EccDefRowStatus_Type = RowStatus
_EccDefRowStatus_Object = MibTableColumn
eccDefRowStatus = _EccDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 1),
    _EccDefRowStatus_Type()
)
eccDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefRowStatus.setStatus("current")
_EccDefType_Type = FspR7InterfaceType
_EccDefType_Object = MibTableColumn
eccDefType = _EccDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 2),
    _EccDefType_Type()
)
eccDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefType.setStatus("current")
_EccDefAdmin_Type = FspR7AdminState
_EccDefAdmin_Object = MibTableColumn
eccDefAdmin = _EccDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 3),
    _EccDefAdmin_Type()
)
eccDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefAdmin.setStatus("current")
_EccDefAlias_Type = SnmpAdminString
_EccDefAlias_Object = MibTableColumn
eccDefAlias = _EccDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 4),
    _EccDefAlias_Type()
)
eccDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefAlias.setStatus("current")
_EccDefLanAid_Type = SnmpAdminString
_EccDefLanAid_Object = MibTableColumn
eccDefLanAid = _EccDefLanAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 5),
    _EccDefLanAid_Type()
)
eccDefLanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefLanAid.setStatus("current")


class _EccDefExternalVid_Type(Unsigned32):
    """Custom type eccDefExternalVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EccDefExternalVid_Type.__name__ = "Unsigned32"
_EccDefExternalVid_Object = MibTableColumn
eccDefExternalVid = _EccDefExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 7, 1, 6),
    _EccDefExternalVid_Type()
)
eccDefExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eccDefExternalVid.setStatus("current")
_EndOfEccDefTable_Type = Integer32
_EndOfEccDefTable_Object = MibScalar
endOfEccDefTable = _EndOfEccDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 8),
    _EndOfEccDefTable_Type()
)
endOfEccDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEccDefTable.setStatus("current")
_EndOfDcnMgmtDef_Type = Integer32
_EndOfDcnMgmtDef_Object = MibScalar
endOfDcnMgmtDef = _EndOfDcnMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 5, 10000),
    _EndOfDcnMgmtDef_Type()
)
endOfDcnMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfDcnMgmtDef.setStatus("current")
_OpticalMuxMgmtDef_ObjectIdentity = ObjectIdentity
opticalMuxMgmtDef = _OpticalMuxMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6)
)
_OpticalMuxDefTable_Object = MibTable
opticalMuxDefTable = _OpticalMuxDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1)
)
if mibBuilder.loadTexts:
    opticalMuxDefTable.setStatus("current")
_OpticalMuxDefEntry_Object = MibTableRow
opticalMuxDefEntry = _OpticalMuxDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1)
)
opticalMuxDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityOpticalMuxClassName"),
)
if mibBuilder.loadTexts:
    opticalMuxDefEntry.setStatus("current")
_OpticalMuxDefRowStatus_Type = RowStatus
_OpticalMuxDefRowStatus_Object = MibTableColumn
opticalMuxDefRowStatus = _OpticalMuxDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 1),
    _OpticalMuxDefRowStatus_Type()
)
opticalMuxDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefRowStatus.setStatus("current")


class _OpticalMuxDefPumpPower_Type(Integer32):
    """Custom type opticalMuxDefPumpPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(115, 138),
    )


_OpticalMuxDefPumpPower_Type.__name__ = "Integer32"
_OpticalMuxDefPumpPower_Object = MibTableColumn
opticalMuxDefPumpPower = _OpticalMuxDefPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 2),
    _OpticalMuxDefPumpPower_Type()
)
opticalMuxDefPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefPumpPower.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefPumpPower.setUnits("0.2 dBm")
_OpticalMuxDefInhibitSwitchToWork_Type = FspR7YesNo
_OpticalMuxDefInhibitSwitchToWork_Object = MibTableColumn
opticalMuxDefInhibitSwitchToWork = _OpticalMuxDefInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 3),
    _OpticalMuxDefInhibitSwitchToWork_Type()
)
opticalMuxDefInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefInhibitSwitchToWork.setStatus("current")
_OpticalMuxDefForceLaserOn_Type = FspR7LaserForcedOperation
_OpticalMuxDefForceLaserOn_Object = MibTableColumn
opticalMuxDefForceLaserOn = _OpticalMuxDefForceLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 4),
    _OpticalMuxDefForceLaserOn_Type()
)
opticalMuxDefForceLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefForceLaserOn.setStatus("current")
_OpticalMuxDefAseTabCreation_Type = FspR7AseTabOpr
_OpticalMuxDefAseTabCreation_Object = MibTableColumn
opticalMuxDefAseTabCreation = _OpticalMuxDefAseTabCreation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 5),
    _OpticalMuxDefAseTabCreation_Type()
)
opticalMuxDefAseTabCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefAseTabCreation.setStatus("current")


class _OpticalMuxDefOpticalSetPoint_Type(Integer32):
    """Custom type opticalMuxDefOpticalSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 50),
    )


_OpticalMuxDefOpticalSetPoint_Type.__name__ = "Integer32"
_OpticalMuxDefOpticalSetPoint_Object = MibTableColumn
opticalMuxDefOpticalSetPoint = _OpticalMuxDefOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 6),
    _OpticalMuxDefOpticalSetPoint_Type()
)
opticalMuxDefOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefOpticalSetPoint.setUnits("0.1 dBm")
_OpticalMuxDefInitiateEqualization_Type = FspR7InitEqualization
_OpticalMuxDefInitiateEqualization_Object = MibTableColumn
opticalMuxDefInitiateEqualization = _OpticalMuxDefInitiateEqualization_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 7),
    _OpticalMuxDefInitiateEqualization_Type()
)
opticalMuxDefInitiateEqualization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefInitiateEqualization.setStatus("current")


class _OpticalMuxDefTilt_Type(Integer32):
    """Custom type opticalMuxDefTilt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 0),
    )


_OpticalMuxDefTilt_Type.__name__ = "Integer32"
_OpticalMuxDefTilt_Object = MibTableColumn
opticalMuxDefTilt = _OpticalMuxDefTilt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 8),
    _OpticalMuxDefTilt_Type()
)
opticalMuxDefTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefTilt.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefTilt.setUnits("0.1 dB")


class _OpticalMuxDefOscOpticalSetpoint_Type(Integer32):
    """Custom type opticalMuxDefOscOpticalSetpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 50),
    )


_OpticalMuxDefOscOpticalSetpoint_Type.__name__ = "Integer32"
_OpticalMuxDefOscOpticalSetpoint_Object = MibTableColumn
opticalMuxDefOscOpticalSetpoint = _OpticalMuxDefOscOpticalSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 9),
    _OpticalMuxDefOscOpticalSetpoint_Type()
)
opticalMuxDefOscOpticalSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOscOpticalSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefOscOpticalSetpoint.setUnits("0.1 dBm")


class _OpticalMuxDefOffset_Type(Integer32):
    """Custom type opticalMuxDefOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_OpticalMuxDefOffset_Type.__name__ = "Integer32"
_OpticalMuxDefOffset_Object = MibTableColumn
opticalMuxDefOffset = _OpticalMuxDefOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 10),
    _OpticalMuxDefOffset_Type()
)
opticalMuxDefOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOffset.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefOffset.setUnits("0.1 dB")
_OpticalMuxDefSwitchCommand_Type = FspR7APSCommand
_OpticalMuxDefSwitchCommand_Object = MibTableColumn
opticalMuxDefSwitchCommand = _OpticalMuxDefSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 11),
    _OpticalMuxDefSwitchCommand_Type()
)
opticalMuxDefSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefSwitchCommand.setStatus("current")
_OpticalMuxDefAlsMode_Type = FspR7AlsMode
_OpticalMuxDefAlsMode_Object = MibTableColumn
opticalMuxDefAlsMode = _OpticalMuxDefAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 12),
    _OpticalMuxDefAlsMode_Type()
)
opticalMuxDefAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefAlsMode.setStatus("current")
_OpticalMuxDefType_Type = FspR7InterfaceType
_OpticalMuxDefType_Object = MibTableColumn
opticalMuxDefType = _OpticalMuxDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 13),
    _OpticalMuxDefType_Type()
)
opticalMuxDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefType.setStatus("current")


class _OpticalMuxDefAttenuationGradient_Type(Unsigned32):
    """Custom type opticalMuxDefAttenuationGradient based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_OpticalMuxDefAttenuationGradient_Type.__name__ = "Unsigned32"
_OpticalMuxDefAttenuationGradient_Object = MibTableColumn
opticalMuxDefAttenuationGradient = _OpticalMuxDefAttenuationGradient_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 14),
    _OpticalMuxDefAttenuationGradient_Type()
)
opticalMuxDefAttenuationGradient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefAttenuationGradient.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefAttenuationGradient.setUnits("0.1 dB/min")
_OpticalMuxDefInhibitSwitchToProt_Type = FspR7YesNo
_OpticalMuxDefInhibitSwitchToProt_Object = MibTableColumn
opticalMuxDefInhibitSwitchToProt = _OpticalMuxDefInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 15),
    _OpticalMuxDefInhibitSwitchToProt_Type()
)
opticalMuxDefInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefInhibitSwitchToProt.setStatus("current")


class _OpticalMuxDefVariableGain_Type(Unsigned32):
    """Custom type opticalMuxDefVariableGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350),
    )


_OpticalMuxDefVariableGain_Type.__name__ = "Unsigned32"
_OpticalMuxDefVariableGain_Object = MibTableColumn
opticalMuxDefVariableGain = _OpticalMuxDefVariableGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 16),
    _OpticalMuxDefVariableGain_Type()
)
opticalMuxDefVariableGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefVariableGain.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefVariableGain.setUnits("0.1 dB")
_OpticalMuxDefAdmin_Type = FspR7AdminState
_OpticalMuxDefAdmin_Object = MibTableColumn
opticalMuxDefAdmin = _OpticalMuxDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 17),
    _OpticalMuxDefAdmin_Type()
)
opticalMuxDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefAdmin.setStatus("current")
_OpticalMuxDefTimePeriod_Type = FspR7OtdrPeriod
_OpticalMuxDefTimePeriod_Object = MibTableColumn
opticalMuxDefTimePeriod = _OpticalMuxDefTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 18),
    _OpticalMuxDefTimePeriod_Type()
)
opticalMuxDefTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefTimePeriod.setStatus("current")
_OpticalMuxDefSigDegThresReceiver_Type = Unsigned32
_OpticalMuxDefSigDegThresReceiver_Object = MibTableColumn
opticalMuxDefSigDegThresReceiver = _OpticalMuxDefSigDegThresReceiver_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 19),
    _OpticalMuxDefSigDegThresReceiver_Type()
)
opticalMuxDefSigDegThresReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefSigDegThresReceiver.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefSigDegThresReceiver.setUnits("0.1 dB")
_OpticalMuxDefAlias_Type = SnmpAdminString
_OpticalMuxDefAlias_Object = MibTableColumn
opticalMuxDefAlias = _OpticalMuxDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 20),
    _OpticalMuxDefAlias_Type()
)
opticalMuxDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefAlias.setStatus("current")
_OpticalMuxDefDataLayerPmReset_Type = FspR7PmReset
_OpticalMuxDefDataLayerPmReset_Object = MibTableColumn
opticalMuxDefDataLayerPmReset = _OpticalMuxDefDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 21),
    _OpticalMuxDefDataLayerPmReset_Type()
)
opticalMuxDefDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefDataLayerPmReset.setStatus("current")
_OpticalMuxDefGain_Type = FspR7Gain
_OpticalMuxDefGain_Object = MibTableColumn
opticalMuxDefGain = _OpticalMuxDefGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 22),
    _OpticalMuxDefGain_Type()
)
opticalMuxDefGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefGain.setStatus("current")
_OpticalMuxDefEdfaPwrOut_Type = FspR7EdfaOutputPowerRating
_OpticalMuxDefEdfaPwrOut_Object = MibTableColumn
opticalMuxDefEdfaPwrOut = _OpticalMuxDefEdfaPwrOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 23),
    _OpticalMuxDefEdfaPwrOut_Type()
)
opticalMuxDefEdfaPwrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefEdfaPwrOut.setStatus("current")


class _OpticalMuxDefVoaSetpoint_Type(Unsigned32):
    """Custom type opticalMuxDefVoaSetpoint based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OpticalMuxDefVoaSetpoint_Type.__name__ = "Unsigned32"
_OpticalMuxDefVoaSetpoint_Object = MibTableColumn
opticalMuxDefVoaSetpoint = _OpticalMuxDefVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 24),
    _OpticalMuxDefVoaSetpoint_Type()
)
opticalMuxDefVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefVoaSetpoint.setUnits("0.1 dB")
_OpticalMuxDefFiberBrand_Type = FspR7FiberBrand
_OpticalMuxDefFiberBrand_Object = MibTableColumn
opticalMuxDefFiberBrand = _OpticalMuxDefFiberBrand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 25),
    _OpticalMuxDefFiberBrand_Type()
)
opticalMuxDefFiberBrand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefFiberBrand.setStatus("current")
_OpticalMuxDefTiltSet_Type = FspR7TiltSet
_OpticalMuxDefTiltSet_Object = MibTableColumn
opticalMuxDefTiltSet = _OpticalMuxDefTiltSet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 26),
    _OpticalMuxDefTiltSet_Type()
)
opticalMuxDefTiltSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefTiltSet.setStatus("current")
_OpticalMuxDefForceFwdAsePilotOn_Type = FspR7LaserForcedOperation
_OpticalMuxDefForceFwdAsePilotOn_Object = MibTableColumn
opticalMuxDefForceFwdAsePilotOn = _OpticalMuxDefForceFwdAsePilotOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 27),
    _OpticalMuxDefForceFwdAsePilotOn_Type()
)
opticalMuxDefForceFwdAsePilotOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefForceFwdAsePilotOn.setStatus("current")
_OpticalMuxDefBandProvision_Type = FspR7OpticalBand
_OpticalMuxDefBandProvision_Object = MibTableColumn
opticalMuxDefBandProvision = _OpticalMuxDefBandProvision_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 28),
    _OpticalMuxDefBandProvision_Type()
)
opticalMuxDefBandProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefBandProvision.setStatus("current")


class _OpticalMuxDefOffsetHigh_Type(Integer32):
    """Custom type opticalMuxDefOffsetHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 210),
    )


_OpticalMuxDefOffsetHigh_Type.__name__ = "Integer32"
_OpticalMuxDefOffsetHigh_Object = MibTableColumn
opticalMuxDefOffsetHigh = _OpticalMuxDefOffsetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 29),
    _OpticalMuxDefOffsetHigh_Type()
)
opticalMuxDefOffsetHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOffsetHigh.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefOffsetHigh.setUnits("0.1 dBm")


class _OpticalMuxDefOffsetLow_Type(Integer32):
    """Custom type opticalMuxDefOffsetLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 210),
    )


_OpticalMuxDefOffsetLow_Type.__name__ = "Integer32"
_OpticalMuxDefOffsetLow_Object = MibTableColumn
opticalMuxDefOffsetLow = _OpticalMuxDefOffsetLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 30),
    _OpticalMuxDefOffsetLow_Type()
)
opticalMuxDefOffsetLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOffsetLow.setStatus("current")
if mibBuilder.loadTexts:
    opticalMuxDefOffsetLow.setUnits("0.1 dBm")
_OpticalMuxDefOptUpdate_Type = FspR7OptUpdate
_OpticalMuxDefOptUpdate_Object = MibTableColumn
opticalMuxDefOptUpdate = _OpticalMuxDefOptUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 1, 1, 31),
    _OpticalMuxDefOptUpdate_Type()
)
opticalMuxDefOptUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalMuxDefOptUpdate.setStatus("current")
_EndOfOpticalMuxDefTable_Type = Integer32
_EndOfOpticalMuxDefTable_Object = MibScalar
endOfOpticalMuxDefTable = _EndOfOpticalMuxDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 2),
    _EndOfOpticalMuxDefTable_Type()
)
endOfOpticalMuxDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalMuxDefTable.setStatus("current")
_EndOfOpticalMuxMgmtDef_Type = Integer32
_EndOfOpticalMuxMgmtDef_Object = MibScalar
endOfOpticalMuxMgmtDef = _EndOfOpticalMuxMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 6, 10000),
    _EndOfOpticalMuxMgmtDef_Type()
)
endOfOpticalMuxMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalMuxMgmtDef.setStatus("current")
_ShelfConnMgmtDef_ObjectIdentity = ObjectIdentity
shelfConnMgmtDef = _ShelfConnMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7)
)
_ShelfConnDefTable_Object = MibTable
shelfConnDefTable = _ShelfConnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1)
)
if mibBuilder.loadTexts:
    shelfConnDefTable.setStatus("current")
_ShelfConnDefEntry_Object = MibTableRow
shelfConnDefEntry = _ShelfConnDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1, 1)
)
shelfConnDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityShelfConnShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityShelfConnClassName"),
)
if mibBuilder.loadTexts:
    shelfConnDefEntry.setStatus("current")
_ShelfConnDefRowStatus_Type = RowStatus
_ShelfConnDefRowStatus_Object = MibTableColumn
shelfConnDefRowStatus = _ShelfConnDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1, 1, 1),
    _ShelfConnDefRowStatus_Type()
)
shelfConnDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnDefRowStatus.setStatus("current")
_ShelfConnDefAdmin_Type = FspR7AdminState
_ShelfConnDefAdmin_Object = MibTableColumn
shelfConnDefAdmin = _ShelfConnDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1, 1, 2),
    _ShelfConnDefAdmin_Type()
)
shelfConnDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnDefAdmin.setStatus("current")
_ShelfConnDefAlias_Type = SnmpAdminString
_ShelfConnDefAlias_Object = MibTableColumn
shelfConnDefAlias = _ShelfConnDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1, 1, 3),
    _ShelfConnDefAlias_Type()
)
shelfConnDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnDefAlias.setStatus("current")
_ShelfConnDefFacilityType_Type = FspR7InterfaceType
_ShelfConnDefFacilityType_Object = MibTableColumn
shelfConnDefFacilityType = _ShelfConnDefFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 1, 1, 4),
    _ShelfConnDefFacilityType_Type()
)
shelfConnDefFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfConnDefFacilityType.setStatus("current")
_EndOfShelfConnDefTable_Type = Integer32
_EndOfShelfConnDefTable_Object = MibScalar
endOfShelfConnDefTable = _EndOfShelfConnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 2),
    _EndOfShelfConnDefTable_Type()
)
endOfShelfConnDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfConnDefTable.setStatus("current")
_EndOfShelfConnMgmtDef_Type = Integer32
_EndOfShelfConnMgmtDef_Object = MibScalar
endOfShelfConnMgmtDef = _EndOfShelfConnMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 7, 10000),
    _EndOfShelfConnMgmtDef_Type()
)
endOfShelfConnMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfShelfConnMgmtDef.setStatus("current")
_EnvMgmtDef_ObjectIdentity = ObjectIdentity
envMgmtDef = _EnvMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8)
)
_EnvPortDefTable_Object = MibTable
envPortDefTable = _EnvPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1)
)
if mibBuilder.loadTexts:
    envPortDefTable.setStatus("current")
_EnvPortDefEntry_Object = MibTableRow
envPortDefEntry = _EnvPortDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1)
)
envPortDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityEqptShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityEqptClassName"),
)
if mibBuilder.loadTexts:
    envPortDefEntry.setStatus("current")
_EnvPortDefRowStatus_Type = RowStatus
_EnvPortDefRowStatus_Object = MibTableColumn
envPortDefRowStatus = _EnvPortDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 1),
    _EnvPortDefRowStatus_Type()
)
envPortDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefRowStatus.setStatus("current")
_EnvPortDefTelemetry_Type = FspR7TelemetryOutput
_EnvPortDefTelemetry_Object = MibTableColumn
envPortDefTelemetry = _EnvPortDefTelemetry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 2),
    _EnvPortDefTelemetry_Type()
)
envPortDefTelemetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefTelemetry.setStatus("current")
_EnvPortDefFacilityType_Type = FspR7InterfaceType
_EnvPortDefFacilityType_Object = MibTableColumn
envPortDefFacilityType = _EnvPortDefFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 3),
    _EnvPortDefFacilityType_Type()
)
envPortDefFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefFacilityType.setStatus("current")
_EnvPortDefTifAlarmType_Type = SnmpAdminString
_EnvPortDefTifAlarmType_Object = MibTableColumn
envPortDefTifAlarmType = _EnvPortDefTifAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 4),
    _EnvPortDefTifAlarmType_Type()
)
envPortDefTifAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefTifAlarmType.setStatus("current")
_EnvPortDefTifAlarmMessage_Type = SnmpAdminString
_EnvPortDefTifAlarmMessage_Object = MibTableColumn
envPortDefTifAlarmMessage = _EnvPortDefTifAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 5),
    _EnvPortDefTifAlarmMessage_Type()
)
envPortDefTifAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefTifAlarmMessage.setStatus("current")
_EnvPortDefInvertTifInputLogic_Type = FspR7InvertTelemetryInputLogic
_EnvPortDefInvertTifInputLogic_Object = MibTableColumn
envPortDefInvertTifInputLogic = _EnvPortDefInvertTifInputLogic_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 1, 1, 6),
    _EnvPortDefInvertTifInputLogic_Type()
)
envPortDefInvertTifInputLogic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPortDefInvertTifInputLogic.setStatus("current")
_EndOfEnvPortDefTable_Type = Integer32
_EndOfEnvPortDefTable_Object = MibScalar
endOfEnvPortDefTable = _EndOfEnvPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 2),
    _EndOfEnvPortDefTable_Type()
)
endOfEnvPortDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEnvPortDefTable.setStatus("current")
_EndOfEnvMgmtDef_Type = Integer32
_EndOfEnvMgmtDef_Object = MibScalar
endOfEnvMgmtDef = _EndOfEnvMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 8, 10000),
    _EndOfEnvMgmtDef_Type()
)
endOfEnvMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEnvMgmtDef.setStatus("current")
_ContainerMgmtDef_ObjectIdentity = ObjectIdentity
containerMgmtDef = _ContainerMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9)
)
_ContainerDefTable_Object = MibTable
containerDefTable = _ContainerDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 1)
)
if mibBuilder.loadTexts:
    containerDefTable.setStatus("current")
_ContainerDefEntry_Object = MibTableRow
containerDefEntry = _ContainerDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 1, 1)
)
containerDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityContainerShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityContainerClassName"),
)
if mibBuilder.loadTexts:
    containerDefEntry.setStatus("current")
_ContainerDefRowStatus_Type = RowStatus
_ContainerDefRowStatus_Object = MibTableColumn
containerDefRowStatus = _ContainerDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 1, 1, 1),
    _ContainerDefRowStatus_Type()
)
containerDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerDefRowStatus.setStatus("current")
_ContainerDefFacilityType_Type = FspR7InterfaceType
_ContainerDefFacilityType_Object = MibTableColumn
containerDefFacilityType = _ContainerDefFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 1, 1, 2),
    _ContainerDefFacilityType_Type()
)
containerDefFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    containerDefFacilityType.setStatus("current")
_EndOfContainerDefTable_Type = Integer32
_EndOfContainerDefTable_Object = MibScalar
endOfContainerDefTable = _EndOfContainerDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 2),
    _EndOfContainerDefTable_Type()
)
endOfContainerDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfContainerDefTable.setStatus("current")
_EndOfContainerMgmtDef_Type = Integer32
_EndOfContainerMgmtDef_Object = MibScalar
endOfContainerMgmtDef = _EndOfContainerMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 9, 10000),
    _EndOfContainerMgmtDef_Type()
)
endOfContainerMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfContainerMgmtDef.setStatus("current")
_OpticalLineMgmtDef_ObjectIdentity = ObjectIdentity
opticalLineMgmtDef = _OpticalLineMgmtDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10)
)
_OpticalLineDefTable_Object = MibTable
opticalLineDefTable = _OpticalLineDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1)
)
if mibBuilder.loadTexts:
    opticalLineDefTable.setStatus("current")
_OpticalLineDefEntry_Object = MibTableRow
opticalLineDefEntry = _OpticalLineDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1)
)
opticalLineDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityOptLineClassName"),
)
if mibBuilder.loadTexts:
    opticalLineDefEntry.setStatus("current")
_OpticalLineDefRowStatus_Type = RowStatus
_OpticalLineDefRowStatus_Object = MibTableColumn
opticalLineDefRowStatus = _OpticalLineDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1, 1),
    _OpticalLineDefRowStatus_Type()
)
opticalLineDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineDefRowStatus.setStatus("current")
_OpticalLineDefTxLineAttenuation_Type = Integer32
_OpticalLineDefTxLineAttenuation_Object = MibTableColumn
opticalLineDefTxLineAttenuation = _OpticalLineDefTxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1, 2),
    _OpticalLineDefTxLineAttenuation_Type()
)
opticalLineDefTxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineDefTxLineAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    opticalLineDefTxLineAttenuation.setUnits("0.1 dB")
_OpticalLineDefRxLineAttenuation_Type = Integer32
_OpticalLineDefRxLineAttenuation_Object = MibTableColumn
opticalLineDefRxLineAttenuation = _OpticalLineDefRxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1, 3),
    _OpticalLineDefRxLineAttenuation_Type()
)
opticalLineDefRxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineDefRxLineAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    opticalLineDefRxLineAttenuation.setUnits("0.1 dB")
_OpticalLineDefAlias_Type = SnmpAdminString
_OpticalLineDefAlias_Object = MibTableColumn
opticalLineDefAlias = _OpticalLineDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1, 4),
    _OpticalLineDefAlias_Type()
)
opticalLineDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineDefAlias.setStatus("current")
_OpticalLineDefFarEndLocation_Type = SnmpAdminString
_OpticalLineDefFarEndLocation_Object = MibTableColumn
opticalLineDefFarEndLocation = _OpticalLineDefFarEndLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 1, 1, 5),
    _OpticalLineDefFarEndLocation_Type()
)
opticalLineDefFarEndLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalLineDefFarEndLocation.setStatus("current")
_EndOfOpticalLineDefTable_Type = Integer32
_EndOfOpticalLineDefTable_Object = MibScalar
endOfOpticalLineDefTable = _EndOfOpticalLineDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 2),
    _EndOfOpticalLineDefTable_Type()
)
endOfOpticalLineDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalLineDefTable.setStatus("current")
_EndOfOpticalLineMgmtDef_Type = Integer32
_EndOfOpticalLineMgmtDef_Object = MibScalar
endOfOpticalLineMgmtDef = _EndOfOpticalLineMgmtDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 3, 10, 10000),
    _EndOfOpticalLineMgmtDef_Type()
)
endOfOpticalLineMgmtDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOpticalLineMgmtDef.setStatus("current")
_PerformanceDef_ObjectIdentity = ObjectIdentity
performanceDef = _PerformanceDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6)
)
_PerformanceFacilityDef_ObjectIdentity = ObjectIdentity
performanceFacilityDef = _PerformanceFacilityDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4)
)
_PerformanceFacilityThresholdDef_ObjectIdentity = ObjectIdentity
performanceFacilityThresholdDef = _PerformanceFacilityThresholdDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1)
)
_OptThresholdConfigDefTable_Object = MibTable
optThresholdConfigDefTable = _OptThresholdConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    optThresholdConfigDefTable.setStatus("current")
_OptThresholdConfigDefEntry_Object = MibTableRow
optThresholdConfigDefEntry = _OptThresholdConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 1, 1)
)
optThresholdConfigDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    optThresholdConfigDefEntry.setStatus("current")


class _OptThresholdConfigDefLowConfig_Type(Integer32):
    """Custom type optThresholdConfigDefLowConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 300),
    )


_OptThresholdConfigDefLowConfig_Type.__name__ = "Integer32"
_OptThresholdConfigDefLowConfig_Object = MibTableColumn
optThresholdConfigDefLowConfig = _OptThresholdConfigDefLowConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 1, 1, 1),
    _OptThresholdConfigDefLowConfig_Type()
)
optThresholdConfigDefLowConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optThresholdConfigDefLowConfig.setStatus("current")
if mibBuilder.loadTexts:
    optThresholdConfigDefLowConfig.setUnits("0.1 dBm")


class _OptThresholdConfigDefHighConfig_Type(Integer32):
    """Custom type optThresholdConfigDefHighConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 300),
    )


_OptThresholdConfigDefHighConfig_Type.__name__ = "Integer32"
_OptThresholdConfigDefHighConfig_Object = MibTableColumn
optThresholdConfigDefHighConfig = _OptThresholdConfigDefHighConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 1, 1, 2),
    _OptThresholdConfigDefHighConfig_Type()
)
optThresholdConfigDefHighConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optThresholdConfigDefHighConfig.setStatus("current")
if mibBuilder.loadTexts:
    optThresholdConfigDefHighConfig.setUnits("0.1 dBm")
_OprThresholdConfigDefTable_Object = MibTable
oprThresholdConfigDefTable = _OprThresholdConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    oprThresholdConfigDefTable.setStatus("current")
_OprThresholdConfigDefEntry_Object = MibTableRow
oprThresholdConfigDefEntry = _OprThresholdConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 2, 1)
)
oprThresholdConfigDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    oprThresholdConfigDefEntry.setStatus("current")


class _OprThresholdConfigDefLowConfig_Type(Integer32):
    """Custom type oprThresholdConfigDefLowConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-450, 260),
    )


_OprThresholdConfigDefLowConfig_Type.__name__ = "Integer32"
_OprThresholdConfigDefLowConfig_Object = MibTableColumn
oprThresholdConfigDefLowConfig = _OprThresholdConfigDefLowConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 2, 1, 1),
    _OprThresholdConfigDefLowConfig_Type()
)
oprThresholdConfigDefLowConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oprThresholdConfigDefLowConfig.setStatus("current")
if mibBuilder.loadTexts:
    oprThresholdConfigDefLowConfig.setUnits("0.1 dBm")


class _OprThresholdConfigDefHighConfig_Type(Integer32):
    """Custom type oprThresholdConfigDefHighConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-450, 260),
    )


_OprThresholdConfigDefHighConfig_Type.__name__ = "Integer32"
_OprThresholdConfigDefHighConfig_Object = MibTableColumn
oprThresholdConfigDefHighConfig = _OprThresholdConfigDefHighConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 2, 1, 2),
    _OprThresholdConfigDefHighConfig_Type()
)
oprThresholdConfigDefHighConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oprThresholdConfigDefHighConfig.setStatus("current")
if mibBuilder.loadTexts:
    oprThresholdConfigDefHighConfig.setUnits("0.1 dBm")
_EndOfOprThresholdConfigDefTable_Type = Integer32
_EndOfOprThresholdConfigDefTable_Object = MibScalar
endOfOprThresholdConfigDefTable = _EndOfOprThresholdConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 3),
    _EndOfOprThresholdConfigDefTable_Type()
)
endOfOprThresholdConfigDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfOprThresholdConfigDefTable.setStatus("current")
_EndOfPerformanceFacilityThresholdDef_Type = Integer32
_EndOfPerformanceFacilityThresholdDef_Object = MibScalar
endOfPerformanceFacilityThresholdDef = _EndOfPerformanceFacilityThresholdDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 6, 4, 1, 10000),
    _EndOfPerformanceFacilityThresholdDef_Type()
)
endOfPerformanceFacilityThresholdDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfPerformanceFacilityThresholdDef.setStatus("current")
_FeatureSpecificDef_ObjectIdentity = ObjectIdentity
featureSpecificDef = _FeatureSpecificDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7)
)
_FiberMapDef_ObjectIdentity = ObjectIdentity
fiberMapDef = _FiberMapDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1)
)
_TerminationPointDefTable_Object = MibTable
terminationPointDefTable = _TerminationPointDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1)
)
if mibBuilder.loadTexts:
    terminationPointDefTable.setStatus("current")
_TerminationPointDefEntry_Object = MibTableRow
terminationPointDefEntry = _TerminationPointDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1, 1)
)
terminationPointDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo1"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo2"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo3"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointIndexNo4"),
    (0, "ADVA-FSPR7-MIB", "entityTerminPointClassName"),
)
if mibBuilder.loadTexts:
    terminationPointDefEntry.setStatus("current")
_TerminationPointDefRowStatus_Type = RowStatus
_TerminationPointDefRowStatus_Object = MibTableColumn
terminationPointDefRowStatus = _TerminationPointDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1, 1, 1),
    _TerminationPointDefRowStatus_Type()
)
terminationPointDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointDefRowStatus.setStatus("current")
_TerminationPointDefAdmin_Type = FspR7AdminState
_TerminationPointDefAdmin_Object = MibTableColumn
terminationPointDefAdmin = _TerminationPointDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1, 1, 2),
    _TerminationPointDefAdmin_Type()
)
terminationPointDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointDefAdmin.setStatus("current")
_TerminationPointDefFiberDetect_Type = FspR7FiberDetect
_TerminationPointDefFiberDetect_Object = MibTableColumn
terminationPointDefFiberDetect = _TerminationPointDefFiberDetect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1, 1, 3),
    _TerminationPointDefFiberDetect_Type()
)
terminationPointDefFiberDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointDefFiberDetect.setStatus("current")
_TerminationPointDefAlias_Type = SnmpAdminString
_TerminationPointDefAlias_Object = MibTableColumn
terminationPointDefAlias = _TerminationPointDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 1, 1, 4),
    _TerminationPointDefAlias_Type()
)
terminationPointDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminationPointDefAlias.setStatus("current")
_ConnectionDefTable_Object = MibTable
connectionDefTable = _ConnectionDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 2)
)
if mibBuilder.loadTexts:
    connectionDefTable.setStatus("current")
_ConnectionDefEntry_Object = MibTableRow
connectionDefEntry = _ConnectionDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 2, 1)
)
connectionDefEntry.setIndexNames(
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
    connectionDefEntry.setStatus("current")
_ConnectionDefRowStatus_Type = FspR7RowStatus
_ConnectionDefRowStatus_Object = MibTableColumn
connectionDefRowStatus = _ConnectionDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 2, 1, 1),
    _ConnectionDefRowStatus_Type()
)
connectionDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionDefRowStatus.setStatus("current")
_ConnectionDefType_Type = FspR7TypeConnection
_ConnectionDefType_Object = MibTableColumn
connectionDefType = _ConnectionDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 2, 1, 2),
    _ConnectionDefType_Type()
)
connectionDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionDefType.setStatus("current")
_EndOfConnectionDefTable_Type = Integer32
_EndOfConnectionDefTable_Object = MibScalar
endOfConnectionDefTable = _EndOfConnectionDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 3),
    _EndOfConnectionDefTable_Type()
)
endOfConnectionDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfConnectionDefTable.setStatus("current")
_EndOfFiberMapDef_Type = Integer32
_EndOfFiberMapDef_Object = MibScalar
endOfFiberMapDef = _EndOfFiberMapDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 1, 10000),
    _EndOfFiberMapDef_Type()
)
endOfFiberMapDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFiberMapDef.setStatus("current")
_EciDef_ObjectIdentity = ObjectIdentity
eciDef = _EciDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3)
)
_ExternalPortDefTable_Object = MibTable
externalPortDefTable = _ExternalPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1)
)
if mibBuilder.loadTexts:
    externalPortDefTable.setStatus("current")
_ExternalPortDefEntry_Object = MibTableRow
externalPortDefEntry = _ExternalPortDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1)
)
externalPortDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityExternalPortShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityExternalPortClassName"),
)
if mibBuilder.loadTexts:
    externalPortDefEntry.setStatus("current")
_ExternalPortDefRowStatus_Type = FspR7RowStatus
_ExternalPortDefRowStatus_Object = MibTableColumn
externalPortDefRowStatus = _ExternalPortDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 1),
    _ExternalPortDefRowStatus_Type()
)
externalPortDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefRowStatus.setStatus("current")
_ExternalPortDefType_Type = FspR7InterfaceType
_ExternalPortDefType_Object = MibTableColumn
externalPortDefType = _ExternalPortDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 2),
    _ExternalPortDefType_Type()
)
externalPortDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefType.setStatus("current")
_ExternalPortDefTransmitChannel_Type = FspR7ChannelIdentifier
_ExternalPortDefTransmitChannel_Object = MibTableColumn
externalPortDefTransmitChannel = _ExternalPortDefTransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 3),
    _ExternalPortDefTransmitChannel_Type()
)
externalPortDefTransmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefTransmitChannel.setStatus("current")
_ExternalPortDefChannelBandwith_Type = FspR7ChannelBandwidth
_ExternalPortDefChannelBandwith_Object = MibTableColumn
externalPortDefChannelBandwith = _ExternalPortDefChannelBandwith_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 4),
    _ExternalPortDefChannelBandwith_Type()
)
externalPortDefChannelBandwith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefChannelBandwith.setStatus("current")
_ExternalPortDefAlias_Type = SnmpAdminString
_ExternalPortDefAlias_Object = MibTableColumn
externalPortDefAlias = _ExternalPortDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 5),
    _ExternalPortDefAlias_Type()
)
externalPortDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefAlias.setStatus("current")
_ExternalPortDefFarEndLocation_Type = SnmpAdminString
_ExternalPortDefFarEndLocation_Object = MibTableColumn
externalPortDefFarEndLocation = _ExternalPortDefFarEndLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 6),
    _ExternalPortDefFarEndLocation_Type()
)
externalPortDefFarEndLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefFarEndLocation.setStatus("current")
_ExternalPortDefBitrate_Type = Unsigned32
_ExternalPortDefBitrate_Object = MibTableColumn
externalPortDefBitrate = _ExternalPortDefBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 7),
    _ExternalPortDefBitrate_Type()
)
externalPortDefBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefBitrate.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefBitrate.setUnits("Mbps")
_ExternalPortDefFecType_Type = FspR7FecType
_ExternalPortDefFecType_Object = MibTableColumn
externalPortDefFecType = _ExternalPortDefFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 8),
    _ExternalPortDefFecType_Type()
)
externalPortDefFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefFecType.setStatus("current")
_ExternalPortDefLineCoding_Type = FspR7LineCoding
_ExternalPortDefLineCoding_Object = MibTableColumn
externalPortDefLineCoding = _ExternalPortDefLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 9),
    _ExternalPortDefLineCoding_Type()
)
externalPortDefLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefLineCoding.setStatus("current")
_ExternalPortDefFrameFormat_Type = FspR7FrameFormat
_ExternalPortDefFrameFormat_Object = MibTableColumn
externalPortDefFrameFormat = _ExternalPortDefFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 10),
    _ExternalPortDefFrameFormat_Type()
)
externalPortDefFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefFrameFormat.setStatus("current")


class _ExternalPortDefOpticalPowerTx_Type(Integer32):
    """Custom type externalPortDefOpticalPowerTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9900, 600),
    )


_ExternalPortDefOpticalPowerTx_Type.__name__ = "Integer32"
_ExternalPortDefOpticalPowerTx_Object = MibTableColumn
externalPortDefOpticalPowerTx = _ExternalPortDefOpticalPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 11),
    _ExternalPortDefOpticalPowerTx_Type()
)
externalPortDefOpticalPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefOpticalPowerTx.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefOpticalPowerTx.setUnits("0.1 dBm")


class _ExternalPortDefOsnrTransmit_Type(Unsigned32):
    """Custom type externalPortDefOsnrTransmit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 58),
    )


_ExternalPortDefOsnrTransmit_Type.__name__ = "Unsigned32"
_ExternalPortDefOsnrTransmit_Object = MibTableColumn
externalPortDefOsnrTransmit = _ExternalPortDefOsnrTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 12),
    _ExternalPortDefOsnrTransmit_Type()
)
externalPortDefOsnrTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefOsnrTransmit.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefOsnrTransmit.setUnits("dB")


class _ExternalPortDefPmdTransmit_Type(Unsigned32):
    """Custom type externalPortDefPmdTransmit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ExternalPortDefPmdTransmit_Type.__name__ = "Unsigned32"
_ExternalPortDefPmdTransmit_Object = MibTableColumn
externalPortDefPmdTransmit = _ExternalPortDefPmdTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 13),
    _ExternalPortDefPmdTransmit_Type()
)
externalPortDefPmdTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefPmdTransmit.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefPmdTransmit.setUnits("ps")


class _ExternalPortDefChromDisperTx_Type(Integer32):
    """Custom type externalPortDefChromDisperTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60000, 60000),
    )


_ExternalPortDefChromDisperTx_Type.__name__ = "Integer32"
_ExternalPortDefChromDisperTx_Object = MibTableColumn
externalPortDefChromDisperTx = _ExternalPortDefChromDisperTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 14),
    _ExternalPortDefChromDisperTx_Type()
)
externalPortDefChromDisperTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefChromDisperTx.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefChromDisperTx.setUnits("ps/nm")


class _ExternalPortDefMinOsnrRcv_Type(Unsigned32):
    """Custom type externalPortDefMinOsnrRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 58),
    )


_ExternalPortDefMinOsnrRcv_Type.__name__ = "Unsigned32"
_ExternalPortDefMinOsnrRcv_Object = MibTableColumn
externalPortDefMinOsnrRcv = _ExternalPortDefMinOsnrRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 15),
    _ExternalPortDefMinOsnrRcv_Type()
)
externalPortDefMinOsnrRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMinOsnrRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMinOsnrRcv.setUnits("dB")


class _ExternalPortDefMinOptPowerRcv_Type(Integer32):
    """Custom type externalPortDefMinOptPowerRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2500, 0),
    )


_ExternalPortDefMinOptPowerRcv_Type.__name__ = "Integer32"
_ExternalPortDefMinOptPowerRcv_Object = MibTableColumn
externalPortDefMinOptPowerRcv = _ExternalPortDefMinOptPowerRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 16),
    _ExternalPortDefMinOptPowerRcv_Type()
)
externalPortDefMinOptPowerRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMinOptPowerRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMinOptPowerRcv.setUnits("0.1 dBm")


class _ExternalPortDefMaxOptPowerRcv_Type(Integer32):
    """Custom type externalPortDefMaxOptPowerRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_ExternalPortDefMaxOptPowerRcv_Type.__name__ = "Integer32"
_ExternalPortDefMaxOptPowerRcv_Object = MibTableColumn
externalPortDefMaxOptPowerRcv = _ExternalPortDefMaxOptPowerRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 17),
    _ExternalPortDefMaxOptPowerRcv_Type()
)
externalPortDefMaxOptPowerRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMaxOptPowerRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMaxOptPowerRcv.setUnits("0.1 dBm")


class _ExternalPortDefMaxPmdRcv_Type(Unsigned32):
    """Custom type externalPortDefMaxPmdRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ExternalPortDefMaxPmdRcv_Type.__name__ = "Unsigned32"
_ExternalPortDefMaxPmdRcv_Object = MibTableColumn
externalPortDefMaxPmdRcv = _ExternalPortDefMaxPmdRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 18),
    _ExternalPortDefMaxPmdRcv_Type()
)
externalPortDefMaxPmdRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMaxPmdRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMaxPmdRcv.setUnits("ps")


class _ExternalPortDefMinChromDisperRcv_Type(Integer32):
    """Custom type externalPortDefMinChromDisperRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60000, 60000),
    )


_ExternalPortDefMinChromDisperRcv_Type.__name__ = "Integer32"
_ExternalPortDefMinChromDisperRcv_Object = MibTableColumn
externalPortDefMinChromDisperRcv = _ExternalPortDefMinChromDisperRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 19),
    _ExternalPortDefMinChromDisperRcv_Type()
)
externalPortDefMinChromDisperRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMinChromDisperRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMinChromDisperRcv.setUnits("ps/nm")


class _ExternalPortDefMaxChromDisperRcv_Type(Integer32):
    """Custom type externalPortDefMaxChromDisperRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60000, 60000),
    )


_ExternalPortDefMaxChromDisperRcv_Type.__name__ = "Integer32"
_ExternalPortDefMaxChromDisperRcv_Object = MibTableColumn
externalPortDefMaxChromDisperRcv = _ExternalPortDefMaxChromDisperRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 20),
    _ExternalPortDefMaxChromDisperRcv_Type()
)
externalPortDefMaxChromDisperRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMaxChromDisperRcv.setStatus("current")
if mibBuilder.loadTexts:
    externalPortDefMaxChromDisperRcv.setUnits("ps/nm")
_ExternalPortDefMaxBitErrorRate_Type = FspR7MaxBitErrorRate
_ExternalPortDefMaxBitErrorRate_Object = MibTableColumn
externalPortDefMaxBitErrorRate = _ExternalPortDefMaxBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 21),
    _ExternalPortDefMaxBitErrorRate_Type()
)
externalPortDefMaxBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefMaxBitErrorRate.setStatus("current")
_ExternalPortDefSourceProfile_Type = SnmpAdminString
_ExternalPortDefSourceProfile_Object = MibTableColumn
externalPortDefSourceProfile = _ExternalPortDefSourceProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 1, 1, 22),
    _ExternalPortDefSourceProfile_Type()
)
externalPortDefSourceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortDefSourceProfile.setStatus("current")
_EndOfExternalPortDefTable_Type = Integer32
_EndOfExternalPortDefTable_Object = MibScalar
endOfExternalPortDefTable = _EndOfExternalPortDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 2),
    _EndOfExternalPortDefTable_Type()
)
endOfExternalPortDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfExternalPortDefTable.setStatus("current")
_EndOfEciDef_Type = Integer32
_EndOfEciDef_Object = MibScalar
endOfEciDef = _EndOfEciDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 3, 10000),
    _EndOfEciDef_Type()
)
endOfEciDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfEciDef.setStatus("current")
_ChangeServiceDef_ObjectIdentity = ObjectIdentity
changeServiceDef = _ChangeServiceDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5)
)
_ChangePhysicalPortServiceDefTable_Object = MibTable
changePhysicalPortServiceDefTable = _ChangePhysicalPortServiceDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1)
)
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTable.setStatus("current")
_ChangePhysicalPortServiceDefEntry_Object = MibTableRow
changePhysicalPortServiceDefEntry = _ChangePhysicalPortServiceDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1)
)
changePhysicalPortServiceDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFacilityShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilitySlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFacilityClassName"),
)
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefEntry.setStatus("current")
_ChangePhysicalPortServiceDefRowStatus_Type = RowStatus
_ChangePhysicalPortServiceDefRowStatus_Object = MibTableColumn
changePhysicalPortServiceDefRowStatus = _ChangePhysicalPortServiceDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 1),
    _ChangePhysicalPortServiceDefRowStatus_Type()
)
changePhysicalPortServiceDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefRowStatus.setStatus("current")
_ChangePhysicalPortServiceDefType_Type = FspR7InterfaceType
_ChangePhysicalPortServiceDefType_Object = MibTableColumn
changePhysicalPortServiceDefType = _ChangePhysicalPortServiceDefType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 2),
    _ChangePhysicalPortServiceDefType_Type()
)
changePhysicalPortServiceDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefType.setStatus("current")
_ChangePhysicalPortServiceDefAdmin_Type = FspR7AdminState
_ChangePhysicalPortServiceDefAdmin_Object = MibTableColumn
changePhysicalPortServiceDefAdmin = _ChangePhysicalPortServiceDefAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 3),
    _ChangePhysicalPortServiceDefAdmin_Type()
)
changePhysicalPortServiceDefAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefAdmin.setStatus("current")
_ChangePhysicalPortServiceDefAlias_Type = SnmpAdminString
_ChangePhysicalPortServiceDefAlias_Object = MibTableColumn
changePhysicalPortServiceDefAlias = _ChangePhysicalPortServiceDefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 4),
    _ChangePhysicalPortServiceDefAlias_Type()
)
changePhysicalPortServiceDefAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefAlias.setStatus("current")
_ChangePhysicalPortServiceDefAlsMode_Type = FspR7AlsMode
_ChangePhysicalPortServiceDefAlsMode_Object = MibTableColumn
changePhysicalPortServiceDefAlsMode = _ChangePhysicalPortServiceDefAlsMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 5),
    _ChangePhysicalPortServiceDefAlsMode_Type()
)
changePhysicalPortServiceDefAlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefAlsMode.setStatus("current")
_ChangePhysicalPortServiceDefBehaviour_Type = FspR7PortBehaviour
_ChangePhysicalPortServiceDefBehaviour_Object = MibTableColumn
changePhysicalPortServiceDefBehaviour = _ChangePhysicalPortServiceDefBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 6),
    _ChangePhysicalPortServiceDefBehaviour_Type()
)
changePhysicalPortServiceDefBehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefBehaviour.setStatus("current")


class _ChangePhysicalPortServiceDefDispersionSetting_Type(Integer32):
    """Custom type changePhysicalPortServiceDefDispersionSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50000, 50000),
    )


_ChangePhysicalPortServiceDefDispersionSetting_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefDispersionSetting_Object = MibTableColumn
changePhysicalPortServiceDefDispersionSetting = _ChangePhysicalPortServiceDefDispersionSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 7),
    _ChangePhysicalPortServiceDefDispersionSetting_Type()
)
changePhysicalPortServiceDefDispersionSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefDispersionSetting.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefDispersionSetting.setUnits("ps/nm")
_ChangePhysicalPortServiceDefDispersionMode_Type = FspR7DispersionModes
_ChangePhysicalPortServiceDefDispersionMode_Object = MibTableColumn
changePhysicalPortServiceDefDispersionMode = _ChangePhysicalPortServiceDefDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 8),
    _ChangePhysicalPortServiceDefDispersionMode_Type()
)
changePhysicalPortServiceDefDispersionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefDispersionMode.setStatus("current")
_ChangePhysicalPortServiceDefChannelProv_Type = FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefChannelProv_Object = MibTableColumn
changePhysicalPortServiceDefChannelProv = _ChangePhysicalPortServiceDefChannelProv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 9),
    _ChangePhysicalPortServiceDefChannelProv_Type()
)
changePhysicalPortServiceDefChannelProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefChannelProv.setStatus("current")
_ChangePhysicalPortServiceDefWdmRxChannel_Type = FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefWdmRxChannel_Object = MibTableColumn
changePhysicalPortServiceDefWdmRxChannel = _ChangePhysicalPortServiceDefWdmRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 10),
    _ChangePhysicalPortServiceDefWdmRxChannel_Type()
)
changePhysicalPortServiceDefWdmRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefWdmRxChannel.setStatus("current")
_ChangePhysicalPortServiceDefCodeGain_Type = FspR7CodeGain
_ChangePhysicalPortServiceDefCodeGain_Object = MibTableColumn
changePhysicalPortServiceDefCodeGain = _ChangePhysicalPortServiceDefCodeGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 11),
    _ChangePhysicalPortServiceDefCodeGain_Type()
)
changePhysicalPortServiceDefCodeGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefCodeGain.setStatus("current")
_ChangePhysicalPortServiceDefXfpDecisionThres_Type = FspR7XfpDecisionThres
_ChangePhysicalPortServiceDefXfpDecisionThres_Object = MibTableColumn
changePhysicalPortServiceDefXfpDecisionThres = _ChangePhysicalPortServiceDefXfpDecisionThres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 12),
    _ChangePhysicalPortServiceDefXfpDecisionThres_Type()
)
changePhysicalPortServiceDefXfpDecisionThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefXfpDecisionThres.setStatus("current")
_ChangePhysicalPortServiceDefDisparityCorrection_Type = EnableState
_ChangePhysicalPortServiceDefDisparityCorrection_Object = MibTableColumn
changePhysicalPortServiceDefDisparityCorrection = _ChangePhysicalPortServiceDefDisparityCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 13),
    _ChangePhysicalPortServiceDefDisparityCorrection_Type()
)
changePhysicalPortServiceDefDisparityCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefDisparityCorrection.setStatus("current")
_ChangePhysicalPortServiceDefEqlzAdmin_Type = FspR7EqlzAdminState
_ChangePhysicalPortServiceDefEqlzAdmin_Object = MibTableColumn
changePhysicalPortServiceDefEqlzAdmin = _ChangePhysicalPortServiceDefEqlzAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 14),
    _ChangePhysicalPortServiceDefEqlzAdmin_Type()
)
changePhysicalPortServiceDefEqlzAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefEqlzAdmin.setStatus("current")
_ChangePhysicalPortServiceDefErrorForwarding_Type = FspR7ErrorFwdMode
_ChangePhysicalPortServiceDefErrorForwarding_Object = MibTableColumn
changePhysicalPortServiceDefErrorForwarding = _ChangePhysicalPortServiceDefErrorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 15),
    _ChangePhysicalPortServiceDefErrorForwarding_Type()
)
changePhysicalPortServiceDefErrorForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefErrorForwarding.setStatus("current")
_ChangePhysicalPortServiceDefFecType_Type = FspR7FecType
_ChangePhysicalPortServiceDefFecType_Object = MibTableColumn
changePhysicalPortServiceDefFecType = _ChangePhysicalPortServiceDefFecType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 16),
    _ChangePhysicalPortServiceDefFecType_Type()
)
changePhysicalPortServiceDefFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefFecType.setStatus("current")
_ChangePhysicalPortServiceDefFarEndCommunication_Type = FspR7YesNo
_ChangePhysicalPortServiceDefFarEndCommunication_Object = MibTableColumn
changePhysicalPortServiceDefFarEndCommunication = _ChangePhysicalPortServiceDefFarEndCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 17),
    _ChangePhysicalPortServiceDefFarEndCommunication_Type()
)
changePhysicalPortServiceDefFarEndCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefFarEndCommunication.setStatus("current")
_ChangePhysicalPortServiceDefFlowControl_Type = FspR7FlowControlMode
_ChangePhysicalPortServiceDefFlowControl_Object = MibTableColumn
changePhysicalPortServiceDefFlowControl = _ChangePhysicalPortServiceDefFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 18),
    _ChangePhysicalPortServiceDefFlowControl_Type()
)
changePhysicalPortServiceDefFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefFlowControl.setStatus("current")
_ChangePhysicalPortServiceDefLaneChannelSetting_Type = FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefLaneChannelSetting_Object = MibTableColumn
changePhysicalPortServiceDefLaneChannelSetting = _ChangePhysicalPortServiceDefLaneChannelSetting_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 19),
    _ChangePhysicalPortServiceDefLaneChannelSetting_Type()
)
changePhysicalPortServiceDefLaneChannelSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaneChannelSetting.setStatus("current")
_ChangePhysicalPortServiceDefLaserDelayTimer_Type = FspR7LaserDelayTimer
_ChangePhysicalPortServiceDefLaserDelayTimer_Object = MibTableColumn
changePhysicalPortServiceDefLaserDelayTimer = _ChangePhysicalPortServiceDefLaserDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 20),
    _ChangePhysicalPortServiceDefLaserDelayTimer_Type()
)
changePhysicalPortServiceDefLaserDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserDelayTimer.setStatus("current")


class _ChangePhysicalPortServiceDefLaserOffTimer_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefLaserOffTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ChangePhysicalPortServiceDefLaserOffTimer_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefLaserOffTimer_Object = MibTableColumn
changePhysicalPortServiceDefLaserOffTimer = _ChangePhysicalPortServiceDefLaserOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 21),
    _ChangePhysicalPortServiceDefLaserOffTimer_Type()
)
changePhysicalPortServiceDefLaserOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserOffTimer.setUnits("ms")


class _ChangePhysicalPortServiceDefLaserOnTimer_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefLaserOnTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ChangePhysicalPortServiceDefLaserOnTimer_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefLaserOnTimer_Object = MibTableColumn
changePhysicalPortServiceDefLaserOnTimer = _ChangePhysicalPortServiceDefLaserOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 22),
    _ChangePhysicalPortServiceDefLaserOnTimer_Type()
)
changePhysicalPortServiceDefLaserOnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserOnTimer.setUnits("ms")
_ChangePhysicalPortServiceDefLaserOffDelayFunction_Type = EnableState
_ChangePhysicalPortServiceDefLaserOffDelayFunction_Object = MibTableColumn
changePhysicalPortServiceDefLaserOffDelayFunction = _ChangePhysicalPortServiceDefLaserOffDelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 23),
    _ChangePhysicalPortServiceDefLaserOffDelayFunction_Type()
)
changePhysicalPortServiceDefLaserOffDelayFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefLaserOffDelayFunction.setStatus("current")
_ChangePhysicalPortServiceDefAutoPTassignment_Type = FspR7ManualAuto
_ChangePhysicalPortServiceDefAutoPTassignment_Object = MibTableColumn
changePhysicalPortServiceDefAutoPTassignment = _ChangePhysicalPortServiceDefAutoPTassignment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 24),
    _ChangePhysicalPortServiceDefAutoPTassignment_Type()
)
changePhysicalPortServiceDefAutoPTassignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefAutoPTassignment.setStatus("current")
_ChangePhysicalPortServiceDefTributarySlotMethod_Type = FspR7ManualAuto
_ChangePhysicalPortServiceDefTributarySlotMethod_Object = MibTableColumn
changePhysicalPortServiceDefTributarySlotMethod = _ChangePhysicalPortServiceDefTributarySlotMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 25),
    _ChangePhysicalPortServiceDefTributarySlotMethod_Type()
)
changePhysicalPortServiceDefTributarySlotMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTributarySlotMethod.setStatus("current")


class _ChangePhysicalPortServiceDefOpticalSetPoint_Type(Integer32):
    """Custom type changePhysicalPortServiceDefOpticalSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 50),
    )


_ChangePhysicalPortServiceDefOpticalSetPoint_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefOpticalSetPoint_Object = MibTableColumn
changePhysicalPortServiceDefOpticalSetPoint = _ChangePhysicalPortServiceDefOpticalSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 26),
    _ChangePhysicalPortServiceDefOpticalSetPoint_Type()
)
changePhysicalPortServiceDefOpticalSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefOpticalSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefOpticalSetPoint.setUnits("0.1 dBm")
_ChangePhysicalPortServiceDefOpuPayloadType_Type = FspR7OpuPayloadType
_ChangePhysicalPortServiceDefOpuPayloadType_Object = MibTableColumn
changePhysicalPortServiceDefOpuPayloadType = _ChangePhysicalPortServiceDefOpuPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 27),
    _ChangePhysicalPortServiceDefOpuPayloadType_Type()
)
changePhysicalPortServiceDefOpuPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefOpuPayloadType.setStatus("current")
_ChangePhysicalPortServiceDefSigDegThresSonetLine_Type = FspR7BERThreshold
_ChangePhysicalPortServiceDefSigDegThresSonetLine_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresSonetLine = _ChangePhysicalPortServiceDefSigDegThresSonetLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 28),
    _ChangePhysicalPortServiceDefSigDegThresSonetLine_Type()
)
changePhysicalPortServiceDefSigDegThresSonetLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSonetLine.setStatus("current")


class _ChangePhysicalPortServiceDefSigDegThresSdhMs_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegThresSdhMs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresSdhMs_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegThresSdhMs_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresSdhMs = _ChangePhysicalPortServiceDefSigDegThresSdhMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 29),
    _ChangePhysicalPortServiceDefSigDegThresSdhMs_Type()
)
changePhysicalPortServiceDefSigDegThresSdhMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSdhMs.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSdhMs.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThresOtu_Type(Integer32):
    """Custom type changePhysicalPortServiceDefSigDegThresOtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresOtu_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefSigDegThresOtu_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresOtu = _ChangePhysicalPortServiceDefSigDegThresOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 30),
    _ChangePhysicalPortServiceDefSigDegThresOtu_Type()
)
changePhysicalPortServiceDefSigDegThresOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOtu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOtu.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThresOdu_Type(Integer32):
    """Custom type changePhysicalPortServiceDefSigDegThresOdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresOdu_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefSigDegThresOdu_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresOdu = _ChangePhysicalPortServiceDefSigDegThresOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 31),
    _ChangePhysicalPortServiceDefSigDegThresOdu_Type()
)
changePhysicalPortServiceDefSigDegThresOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOdu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOdu.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThreshold_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ChangePhysicalPortServiceDefSigDegThreshold_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegThreshold_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThreshold = _ChangePhysicalPortServiceDefSigDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 32),
    _ChangePhysicalPortServiceDefSigDegThreshold_Type()
)
changePhysicalPortServiceDefSigDegThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThreshold.setStatus("current")


class _ChangePhysicalPortServiceDefSigDegPcslThreshold_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPcslThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegPcslThreshold_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPcslThreshold_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPcslThreshold = _ChangePhysicalPortServiceDefSigDegPcslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 33),
    _ChangePhysicalPortServiceDefSigDegPcslThreshold_Type()
)
changePhysicalPortServiceDefSigDegPcslThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPcslThreshold.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPcslThreshold.setUnits("%")
_ChangePhysicalPortServiceDefSigDegThresSonetSection_Type = FspR7BERThresholdSection
_ChangePhysicalPortServiceDefSigDegThresSonetSection_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresSonetSection = _ChangePhysicalPortServiceDefSigDegThresSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 34),
    _ChangePhysicalPortServiceDefSigDegThresSonetSection_Type()
)
changePhysicalPortServiceDefSigDegThresSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSonetSection.setStatus("current")


class _ChangePhysicalPortServiceDefSigDegThresSdhSection_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegThresSdhSection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresSdhSection_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegThresSdhSection_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresSdhSection = _ChangePhysicalPortServiceDefSigDegThresSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 35),
    _ChangePhysicalPortServiceDefSigDegThresSdhSection_Type()
)
changePhysicalPortServiceDefSigDegThresSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresSdhSection.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type(Integer32):
    """Custom type changePhysicalPortServiceDefSigDegThresOduTcmA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmA = _ChangePhysicalPortServiceDefSigDegThresOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 36),
    _ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type()
)
changePhysicalPortServiceDefSigDegThresOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmA.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type(Integer32):
    """Custom type changePhysicalPortServiceDefSigDegThresOduTcmB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmB = _ChangePhysicalPortServiceDefSigDegThresOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 37),
    _ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type()
)
changePhysicalPortServiceDefSigDegThresOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmB.setUnits("%")


class _ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type(Integer32):
    """Custom type changePhysicalPortServiceDefSigDegThresOduTcmC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type.__name__ = "Integer32"
_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmC = _ChangePhysicalPortServiceDefSigDegThresOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 38),
    _ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type()
)
changePhysicalPortServiceDefSigDegThresOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegThresOduTcmC.setUnits("%")


class _ChangePhysicalPortServiceDefSignalDegradePeriod_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSignalDegradePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSignalDegradePeriod_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSignalDegradePeriod_Object = MibTableColumn
changePhysicalPortServiceDefSignalDegradePeriod = _ChangePhysicalPortServiceDefSignalDegradePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 39),
    _ChangePhysicalPortServiceDefSignalDegradePeriod_Type()
)
changePhysicalPortServiceDefSignalDegradePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSignalDegradePeriod.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSignalDegradePeriod.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodOdu_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodOdu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodOdu_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodOdu_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOdu = _ChangePhysicalPortServiceDefSigDegPeriodOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 40),
    _ChangePhysicalPortServiceDefSigDegPeriodOdu_Type()
)
changePhysicalPortServiceDefSigDegPeriodOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOdu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOdu.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodOtu_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodOtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodOtu_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodOtu_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOtu = _ChangePhysicalPortServiceDefSigDegPeriodOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 41),
    _ChangePhysicalPortServiceDefSigDegPeriodOtu_Type()
)
changePhysicalPortServiceDefSigDegPeriodOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOtu.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOtu.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodIntegration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodIntegration = _ChangePhysicalPortServiceDefSigDegPeriodIntegration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 42),
    _ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type()
)
changePhysicalPortServiceDefSigDegPeriodIntegration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodIntegration.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodIntegration.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodSdhSection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodSdhSection = _ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 43),
    _ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type()
)
changePhysicalPortServiceDefSigDegPeriodSdhSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodSdhSection.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodSdhSection.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodOduTcmA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmA = _ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 44),
    _ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type()
)
changePhysicalPortServiceDefSigDegPeriodOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmA.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmA.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodOduTcmB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmB = _ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 45),
    _ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type()
)
changePhysicalPortServiceDefSigDegPeriodOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmB.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmB.setUnits("s")


class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefSigDegPeriodOduTcmC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmC = _ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 46),
    _ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type()
)
changePhysicalPortServiceDefSigDegPeriodOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmC.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefSigDegPeriodOduTcmC.setUnits("s")
_ChangePhysicalPortServiceDefOtnStuffing_Type = FspR7Stuff
_ChangePhysicalPortServiceDefOtnStuffing_Object = MibTableColumn
changePhysicalPortServiceDefOtnStuffing = _ChangePhysicalPortServiceDefOtnStuffing_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 47),
    _ChangePhysicalPortServiceDefOtnStuffing_Type()
)
changePhysicalPortServiceDefOtnStuffing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefOtnStuffing.setStatus("current")
_ChangePhysicalPortServiceDefTcmALevel_Type = OtnTcmLevel
_ChangePhysicalPortServiceDefTcmALevel_Object = MibTableColumn
changePhysicalPortServiceDefTcmALevel = _ChangePhysicalPortServiceDefTcmALevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 48),
    _ChangePhysicalPortServiceDefTcmALevel_Type()
)
changePhysicalPortServiceDefTcmALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTcmALevel.setStatus("current")
_ChangePhysicalPortServiceDefTcmBLevel_Type = OtnTcmLevel
_ChangePhysicalPortServiceDefTcmBLevel_Object = MibTableColumn
changePhysicalPortServiceDefTcmBLevel = _ChangePhysicalPortServiceDefTcmBLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 49),
    _ChangePhysicalPortServiceDefTcmBLevel_Type()
)
changePhysicalPortServiceDefTcmBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTcmBLevel.setStatus("current")
_ChangePhysicalPortServiceDefTcmCLevel_Type = OtnTcmLevel
_ChangePhysicalPortServiceDefTcmCLevel_Object = MibTableColumn
changePhysicalPortServiceDefTcmCLevel = _ChangePhysicalPortServiceDefTcmCLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 50),
    _ChangePhysicalPortServiceDefTcmCLevel_Type()
)
changePhysicalPortServiceDefTcmCLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTcmCLevel.setStatus("current")
_ChangePhysicalPortServiceDefTerminationLevel_Type = OhTerminationLevel
_ChangePhysicalPortServiceDefTerminationLevel_Object = MibTableColumn
changePhysicalPortServiceDefTerminationLevel = _ChangePhysicalPortServiceDefTerminationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 51),
    _ChangePhysicalPortServiceDefTerminationLevel_Type()
)
changePhysicalPortServiceDefTerminationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTerminationLevel.setStatus("current")
_ChangePhysicalPortServiceDefTimingSource_Type = SonetTimingSource
_ChangePhysicalPortServiceDefTimingSource_Object = MibTableColumn
changePhysicalPortServiceDefTimingSource = _ChangePhysicalPortServiceDefTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 52),
    _ChangePhysicalPortServiceDefTimingSource_Type()
)
changePhysicalPortServiceDefTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimingSource.setStatus("current")
_ChangePhysicalPortServiceDefTimModeOdu_Type = TimMode
_ChangePhysicalPortServiceDefTimModeOdu_Object = MibTableColumn
changePhysicalPortServiceDefTimModeOdu = _ChangePhysicalPortServiceDefTimModeOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 53),
    _ChangePhysicalPortServiceDefTimModeOdu_Type()
)
changePhysicalPortServiceDefTimModeOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeOdu.setStatus("current")
_ChangePhysicalPortServiceDefTimModeOtu_Type = TimMode
_ChangePhysicalPortServiceDefTimModeOtu_Object = MibTableColumn
changePhysicalPortServiceDefTimModeOtu = _ChangePhysicalPortServiceDefTimModeOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 54),
    _ChangePhysicalPortServiceDefTimModeOtu_Type()
)
changePhysicalPortServiceDefTimModeOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeOtu.setStatus("current")
_ChangePhysicalPortServiceDefTimModeSonetSection_Type = TimMode
_ChangePhysicalPortServiceDefTimModeSonetSection_Object = MibTableColumn
changePhysicalPortServiceDefTimModeSonetSection = _ChangePhysicalPortServiceDefTimModeSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 55),
    _ChangePhysicalPortServiceDefTimModeSonetSection_Type()
)
changePhysicalPortServiceDefTimModeSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeSonetSection.setStatus("current")
_ChangePhysicalPortServiceDefTimModeOduTcmA_Type = TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmA = _ChangePhysicalPortServiceDefTimModeOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 56),
    _ChangePhysicalPortServiceDefTimModeOduTcmA_Type()
)
changePhysicalPortServiceDefTimModeOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeOduTcmA.setStatus("current")
_ChangePhysicalPortServiceDefTimModeOduTcmB_Type = TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmB = _ChangePhysicalPortServiceDefTimModeOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 57),
    _ChangePhysicalPortServiceDefTimModeOduTcmB_Type()
)
changePhysicalPortServiceDefTimModeOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeOduTcmB.setStatus("current")
_ChangePhysicalPortServiceDefTimModeOduTcmC_Type = TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmC = _ChangePhysicalPortServiceDefTimModeOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 58),
    _ChangePhysicalPortServiceDefTimModeOduTcmC_Type()
)
changePhysicalPortServiceDefTimModeOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTimModeOduTcmC.setStatus("current")
_ChangePhysicalPortServiceDefTraceFormSonetSection_Type = SonetTraceForm
_ChangePhysicalPortServiceDefTraceFormSonetSection_Object = MibTableColumn
changePhysicalPortServiceDefTraceFormSonetSection = _ChangePhysicalPortServiceDefTraceFormSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 59),
    _ChangePhysicalPortServiceDefTraceFormSonetSection_Type()
)
changePhysicalPortServiceDefTraceFormSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceFormSonetSection.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedSonetSection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedSonetSection = _ChangePhysicalPortServiceDefTraceExpectedSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 60),
    _ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type()
)
changePhysicalPortServiceDefTraceExpectedSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedSonetSection.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSonetSection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSonetSection = _ChangePhysicalPortServiceDefTraceTransmitSonetSection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 61),
    _ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type()
)
changePhysicalPortServiceDefTraceTransmitSonetSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSonetSection.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedOtu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceExpectedOtu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedOtu_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedOtu = _ChangePhysicalPortServiceDefTraceExpectedOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 62),
    _ChangePhysicalPortServiceDefTraceExpectedOtu_Type()
)
changePhysicalPortServiceDefTraceExpectedOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedOtu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSapiOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOtu = _ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 63),
    _ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type()
)
changePhysicalPortServiceDefTraceTransmitSapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSapiOtu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitDapiOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOtu = _ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 64),
    _ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type()
)
changePhysicalPortServiceDefTraceTransmitDapiOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitDapiOtu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitOpspOtu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOtu = _ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 65),
    _ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type()
)
changePhysicalPortServiceDefTraceTransmitOpspOtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitOpspOtu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedOdu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceExpectedOdu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedOdu_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedOdu = _ChangePhysicalPortServiceDefTraceExpectedOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 66),
    _ChangePhysicalPortServiceDefTraceExpectedOdu_Type()
)
changePhysicalPortServiceDefTraceExpectedOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedOdu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOdu = _ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 67),
    _ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type()
)
changePhysicalPortServiceDefTraceTransmitSapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSapiOdu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitDapiOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOdu = _ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 68),
    _ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type()
)
changePhysicalPortServiceDefTraceTransmitDapiOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitDapiOdu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitOpspOdu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOdu = _ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 69),
    _ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type()
)
changePhysicalPortServiceDefTraceTransmitOpspOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitOpspOdu.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmA = _ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 70),
    _ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type()
)
changePhysicalPortServiceDefTraceExpectedOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedOduTcmA.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmA = _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 71),
    _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type()
)
changePhysicalPortServiceDefTraceTransmitSapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSapiOduTcmA.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitDapiOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmA = _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 72),
    _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type()
)
changePhysicalPortServiceDefTraceTransmitDapiOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitDapiOduTcmA.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitOpspOduTcmA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmA = _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 73),
    _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type()
)
changePhysicalPortServiceDefTraceTransmitOpspOduTcmA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitOpspOduTcmA.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmB = _ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 74),
    _ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type()
)
changePhysicalPortServiceDefTraceExpectedOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedOduTcmB.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmB = _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 75),
    _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type()
)
changePhysicalPortServiceDefTraceTransmitSapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSapiOduTcmB.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitDapiOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmB = _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 76),
    _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type()
)
changePhysicalPortServiceDefTraceTransmitDapiOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitDapiOduTcmB.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitOpspOduTcmB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmB = _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 77),
    _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type()
)
changePhysicalPortServiceDefTraceTransmitOpspOduTcmB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitOpspOduTcmB.setStatus("current")


class _ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceExpectedOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmC = _ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 78),
    _ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type()
)
changePhysicalPortServiceDefTraceExpectedOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceExpectedOduTcmC.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitSapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmC = _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 79),
    _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type()
)
changePhysicalPortServiceDefTraceTransmitSapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitSapiOduTcmC.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitDapiOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmC = _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 80),
    _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type()
)
changePhysicalPortServiceDefTraceTransmitDapiOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitDapiOduTcmC.setStatus("current")


class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type(OctetString):
    """Custom type changePhysicalPortServiceDefTraceTransmitOpspOduTcmC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type.__name__ = "OctetString"
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Object = MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmC = _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 81),
    _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type()
)
changePhysicalPortServiceDefTraceTransmitOpspOduTcmC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTraceTransmitOpspOduTcmC.setStatus("current")
_ChangePhysicalPortServiceDefTxOffDelay_Type = FspR7EnableDisable
_ChangePhysicalPortServiceDefTxOffDelay_Object = MibTableColumn
changePhysicalPortServiceDefTxOffDelay = _ChangePhysicalPortServiceDefTxOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 82),
    _ChangePhysicalPortServiceDefTxOffDelay_Type()
)
changePhysicalPortServiceDefTxOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefTxOffDelay.setStatus("current")
_ChangePhysicalPortServiceDefVoaMode_Type = FspR7VoaMode
_ChangePhysicalPortServiceDefVoaMode_Object = MibTableColumn
changePhysicalPortServiceDefVoaMode = _ChangePhysicalPortServiceDefVoaMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 83),
    _ChangePhysicalPortServiceDefVoaMode_Type()
)
changePhysicalPortServiceDefVoaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefVoaMode.setStatus("current")


class _ChangePhysicalPortServiceDefVoaSetpoint_Type(Unsigned32):
    """Custom type changePhysicalPortServiceDefVoaSetpoint based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ChangePhysicalPortServiceDefVoaSetpoint_Type.__name__ = "Unsigned32"
_ChangePhysicalPortServiceDefVoaSetpoint_Object = MibTableColumn
changePhysicalPortServiceDefVoaSetpoint = _ChangePhysicalPortServiceDefVoaSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 1, 1, 84),
    _ChangePhysicalPortServiceDefVoaSetpoint_Type()
)
changePhysicalPortServiceDefVoaSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefVoaSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    changePhysicalPortServiceDefVoaSetpoint.setUnits("0.1 dB")
_EndOfChangePhysicalPortServiceDefTable_Type = Integer32
_EndOfChangePhysicalPortServiceDefTable_Object = MibScalar
endOfChangePhysicalPortServiceDefTable = _EndOfChangePhysicalPortServiceDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 2),
    _EndOfChangePhysicalPortServiceDefTable_Type()
)
endOfChangePhysicalPortServiceDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfChangePhysicalPortServiceDefTable.setStatus("current")
_EndOfChangeServiceDef_Type = Integer32
_EndOfChangeServiceDef_Object = MibScalar
endOfChangeServiceDef = _EndOfChangeServiceDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 5, 10000),
    _EndOfChangeServiceDef_Type()
)
endOfChangeServiceDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfChangeServiceDef.setStatus("current")
_ProtectionDef_ObjectIdentity = ObjectIdentity
protectionDef = _ProtectionDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6)
)
_FfpDefTable_Object = MibTable
ffpDefTable = _FfpDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2)
)
if mibBuilder.loadTexts:
    ffpDefTable.setStatus("current")
_FfpDefEntry_Object = MibTableRow
ffpDefEntry = _FfpDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1)
)
ffpDefEntry.setIndexNames(
    (0, "ADVA-FSPR7-MIB", "entityFfpShelfNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpSlotNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpPortNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpExtNo"),
    (0, "ADVA-FSPR7-MIB", "entityFfpClassName"),
)
if mibBuilder.loadTexts:
    ffpDefEntry.setStatus("current")
_FfpDefRowStatus_Type = RowStatus
_FfpDefRowStatus_Object = MibTableColumn
ffpDefRowStatus = _FfpDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 1),
    _FfpDefRowStatus_Type()
)
ffpDefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefRowStatus.setStatus("current")
_FfpDefCreationMethod_Type = FfpType
_FfpDefCreationMethod_Object = MibTableColumn
ffpDefCreationMethod = _FfpDefCreationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 2),
    _FfpDefCreationMethod_Type()
)
ffpDefCreationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefCreationMethod.setStatus("current")
_FfpDefSDswitching_Type = EnableState
_FfpDefSDswitching_Object = MibTableColumn
ffpDefSDswitching = _FfpDefSDswitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 3),
    _FfpDefSDswitching_Type()
)
ffpDefSDswitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefSDswitching.setStatus("current")
_FfpDefHoldOffTime_Type = ApsHoldoffTime
_FfpDefHoldOffTime_Object = MibTableColumn
ffpDefHoldOffTime = _FfpDefHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 4),
    _FfpDefHoldOffTime_Type()
)
ffpDefHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefHoldOffTime.setStatus("current")
_FfpDefProtectionMech_Type = ProtectionMech
_FfpDefProtectionMech_Object = MibTableColumn
ffpDefProtectionMech = _FfpDefProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 5),
    _FfpDefProtectionMech_Type()
)
ffpDefProtectionMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefProtectionMech.setStatus("current")
_FfpDefWorkingAid_Type = SnmpAdminString
_FfpDefWorkingAid_Object = MibTableColumn
ffpDefWorkingAid = _FfpDefWorkingAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 6),
    _FfpDefWorkingAid_Type()
)
ffpDefWorkingAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefWorkingAid.setStatus("current")
_FfpDefProtectionAid_Type = SnmpAdminString
_FfpDefProtectionAid_Object = MibTableColumn
ffpDefProtectionAid = _FfpDefProtectionAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 7),
    _FfpDefProtectionAid_Type()
)
ffpDefProtectionAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefProtectionAid.setStatus("current")
_FfpDefSignalDegradeSwitching_Type = EnableState
_FfpDefSignalDegradeSwitching_Object = MibTableColumn
ffpDefSignalDegradeSwitching = _FfpDefSignalDegradeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 8),
    _FfpDefSignalDegradeSwitching_Type()
)
ffpDefSignalDegradeSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefSignalDegradeSwitching.setStatus("current")
_FfpDefSignalFailureSwitching_Type = EnableState
_FfpDefSignalFailureSwitching_Object = MibTableColumn
ffpDefSignalFailureSwitching = _FfpDefSignalFailureSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 9),
    _FfpDefSignalFailureSwitching_Type()
)
ffpDefSignalFailureSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefSignalFailureSwitching.setStatus("current")
_FfpDefFarEndIp_Type = IpAddress
_FfpDefFarEndIp_Object = MibTableColumn
ffpDefFarEndIp = _FfpDefFarEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 10),
    _FfpDefFarEndIp_Type()
)
ffpDefFarEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefFarEndIp.setStatus("current")
_FfpDefPeerAid_Type = SnmpAdminString
_FfpDefPeerAid_Object = MibTableColumn
ffpDefPeerAid = _FfpDefPeerAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 11),
    _FfpDefPeerAid_Type()
)
ffpDefPeerAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefPeerAid.setStatus("current")
_FfpDefApsType_Type = ApsType
_FfpDefApsType_Object = MibTableColumn
ffpDefApsType = _FfpDefApsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 12),
    _FfpDefApsType_Type()
)
ffpDefApsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefApsType.setStatus("current")
_FfpDefRevertMode_Type = ApsRevertMode
_FfpDefRevertMode_Object = MibTableColumn
ffpDefRevertMode = _FfpDefRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 13),
    _FfpDefRevertMode_Type()
)
ffpDefRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefRevertMode.setStatus("current")


class _FfpDefWaitToRestore_Type(Unsigned32):
    """Custom type ffpDefWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_FfpDefWaitToRestore_Type.__name__ = "Unsigned32"
_FfpDefWaitToRestore_Object = MibTableColumn
ffpDefWaitToRestore = _FfpDefWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 14),
    _FfpDefWaitToRestore_Type()
)
ffpDefWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    ffpDefWaitToRestore.setUnits("min")
_FfpDefDirection_Type = ApsDirection
_FfpDefDirection_Object = MibTableColumn
ffpDefDirection = _FfpDefDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 15),
    _FfpDefDirection_Type()
)
ffpDefDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefDirection.setStatus("current")
_FfpDefProtectionType_Type = FspR7ProtectionType
_FfpDefProtectionType_Object = MibTableColumn
ffpDefProtectionType = _FfpDefProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 2, 1, 16),
    _FfpDefProtectionType_Type()
)
ffpDefProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffpDefProtectionType.setStatus("current")
_EndOfFfpDefTable_Type = Integer32
_EndOfFfpDefTable_Object = MibScalar
endOfFfpDefTable = _EndOfFfpDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 3),
    _EndOfFfpDefTable_Type()
)
endOfFfpDefTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfFfpDefTable.setStatus("current")
_EndOfProtectionDef_Type = Integer32
_EndOfProtectionDef_Object = MibScalar
endOfProtectionDef = _EndOfProtectionDef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 7, 6, 10000),
    _EndOfProtectionDef_Type()
)
endOfProtectionDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfProtectionDef.setStatus("current")
_ConformanceDef_ObjectIdentity = ObjectIdentity
conformanceDef = _ConformanceDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 10)
)
_CompliancesDef_ObjectIdentity = ObjectIdentity
compliancesDef = _CompliancesDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 10, 1)
)
_GroupsDef_ObjectIdentity = ObjectIdentity
groupsDef = _GroupsDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 10, 2)
)

# Managed Objects groups

objectGroupDef = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 10, 2, 1)
)
objectGroupDef.setObjects(
      *(("ADVA-FSPR7-DEF-MIB", "crossConnectionDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefAdmin"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefRedLineState"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefConn"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefAlias"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefPathNode"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefTunnelAid"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefRedLineState"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefConn"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefCrsType"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefAlias"),
        ("ADVA-FSPR7-DEF-MIB", "crossOpticalLineDefTunnelAid"),
        ("ADVA-FSPR7-DEF-MIB", "crossConnectionDefType"),
        ("ADVA-FSPR7-DEF-MIB", "physicalPortDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "physicalPortDefType"),
        ("ADVA-FSPR7-DEF-MIB", "physicalPortDefAdmin"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefChannelBand"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefType"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefAlias"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefAdmin"),
        ("ADVA-FSPR7-DEF-MIB", "virtualPortDefEqlzAdmin"),
        ("ADVA-FSPR7-DEF-MIB", "connectionDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "connectionDefType"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefRowStatus"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefType"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefTransmitChannel"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefChannelBandwith"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefAlias"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefFarEndLocation"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefBitrate"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMaxChromDisperRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMaxBitErrorRate"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefFecType"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefLineCoding"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefFrameFormat"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefOpticalPowerTx"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefOsnrTransmit"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefPmdTransmit"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefChromDisperTx"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMinOsnrRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMinOptPowerRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMaxOptPowerRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMaxPmdRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefMinChromDisperRcv"),
        ("ADVA-FSPR7-DEF-MIB", "externalPortDefSourceProfile"))
)
if mibBuilder.loadTexts:
    objectGroupDef.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

complianceDef = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 10, 10, 1, 1)
)
if mibBuilder.loadTexts:
    complianceDef.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSPR7-DEF-MIB",
    **{"advaFspR7Def": advaFspR7Def,
       "managementDef": managementDef,
       "specificMgmtDef": specificMgmtDef,
       "crossConnectionDefTable": crossConnectionDefTable,
       "crossConnectionDefEntry": crossConnectionDefEntry,
       "crossConnectionDefRowStatus": crossConnectionDefRowStatus,
       "crossConnectionDefAdmin": crossConnectionDefAdmin,
       "crossConnectionDefRedLineState": crossConnectionDefRedLineState,
       "crossConnectionDefConn": crossConnectionDefConn,
       "crossConnectionDefAlias": crossConnectionDefAlias,
       "crossConnectionDefPathNode": crossConnectionDefPathNode,
       "crossConnectionDefTunnelAid": crossConnectionDefTunnelAid,
       "crossConnectionDefType": crossConnectionDefType,
       "crossConnectionDefCrsFunction": crossConnectionDefCrsFunction,
       "crossOpticalLineDefTable": crossOpticalLineDefTable,
       "crossOpticalLineDefEntry": crossOpticalLineDefEntry,
       "crossOpticalLineDefRowStatus": crossOpticalLineDefRowStatus,
       "crossOpticalLineDefRedLineState": crossOpticalLineDefRedLineState,
       "crossOpticalLineDefConn": crossOpticalLineDefConn,
       "crossOpticalLineDefCrsType": crossOpticalLineDefCrsType,
       "crossOpticalLineDefAlias": crossOpticalLineDefAlias,
       "crossOpticalLineDefTunnelAid": crossOpticalLineDefTunnelAid,
       "endOfCrossOpticalLineDefTable": endOfCrossOpticalLineDefTable,
       "crossDcnDefTable": crossDcnDefTable,
       "crossDcnDefEntry": crossDcnDefEntry,
       "crossDcnDefRowStatus": crossDcnDefRowStatus,
       "crossDcnDefType": crossDcnDefType,
       "crossDcnDefLink": crossDcnDefLink,
       "crossDcnDefEcc": crossDcnDefEcc,
       "endOfCrossDcnDefTable": endOfCrossDcnDefTable,
       "endOfSpecificMgmtDef": endOfSpecificMgmtDef,
       "eqptMgmtDef": eqptMgmtDef,
       "shelfDefTable": shelfDefTable,
       "shelfDefEntry": shelfDefEntry,
       "shelfDefRowStatus": shelfDefRowStatus,
       "shelfDefPsuOutputPower": shelfDefPsuOutputPower,
       "shelfDefType": shelfDefType,
       "shelfDefRack": shelfDefRack,
       "shelfDefSupply": shelfDefSupply,
       "shelfDefBandProvision": shelfDefBandProvision,
       "shelfDefAdmin": shelfDefAdmin,
       "shelfDefRackNumber": shelfDefRackNumber,
       "shelfDefRackOrder": shelfDefRackOrder,
       "shelfDefAlias": shelfDefAlias,
       "shelfDefSlot": shelfDefSlot,
       "endOfShelfDefTable": endOfShelfDefTable,
       "fanDefTable": fanDefTable,
       "fanDefEntry": fanDefEntry,
       "fanDefRowStatus": fanDefRowStatus,
       "fanDefAdmin": fanDefAdmin,
       "fanDefType": fanDefType,
       "fanDefAlias": fanDefAlias,
       "fanDefOutputReset": fanDefOutputReset,
       "endOfFanDefTable": endOfFanDefTable,
       "plugDefTable": plugDefTable,
       "plugDefEntry": plugDefEntry,
       "plugDefRowStatus": plugDefRowStatus,
       "plugDefConnector": plugDefConnector,
       "plugDefType": plugDefType,
       "plugDefReach": plugDefReach,
       "plugDefLoopbackAttenuation": plugDefLoopbackAttenuation,
       "plugDefTransmitChannel": plugDefTransmitChannel,
       "plugDefAlias": plugDefAlias,
       "plugDefLaneGroup": plugDefLaneGroup,
       "plugDefMaxDataRate": plugDefMaxDataRate,
       "plugDefThirdPartyUsage": plugDefThirdPartyUsage,
       "plugDefAdmin": plugDefAdmin,
       "plugDefBidirectionalChannel": plugDefBidirectionalChannel,
       "plugDefChannelSpacingProvision": plugDefChannelSpacingProvision,
       "endOfPlugDefTable": endOfPlugDefTable,
       "moduleDefTable": moduleDefTable,
       "moduleDefEntry": moduleDefEntry,
       "moduleDefRowStatus": moduleDefRowStatus,
       "moduleDefPsuOutputPower": moduleDefPsuOutputPower,
       "moduleDefPower": moduleDefPower,
       "moduleDefReach": moduleDefReach,
       "moduleDefInitEqlz": moduleDefInitEqlz,
       "moduleDefLanAid": moduleDefLanAid,
       "moduleDefType": moduleDefType,
       "moduleDefMapping": moduleDefMapping,
       "moduleDefGainRange": moduleDefGainRange,
       "moduleDefSfProvision": moduleDefSfProvision,
       "moduleDefCapabilityLevelProvision": moduleDefCapabilityLevelProvision,
       "moduleDefDCFiberType": moduleDefDCFiberType,
       "moduleDefChannelsProvision": moduleDefChannelsProvision,
       "moduleDefFiberDetect": moduleDefFiberDetect,
       "moduleDefSupply": moduleDefSupply,
       "moduleDefGroup": moduleDefGroup,
       "moduleDefDeploy": moduleDefDeploy,
       "moduleDefLagSysPrio": moduleDefLagSysPrio,
       "moduleDefTransmitChannel": moduleDefTransmitChannel,
       "moduleDefBand": moduleDefBand,
       "moduleDefTrafficDirection": moduleDefTrafficDirection,
       "moduleDefIpAddr": moduleDefIpAddr,
       "moduleDefDispersionCompensation": moduleDefDispersionCompensation,
       "moduleDefActivateDetect": moduleDefActivateDetect,
       "moduleDefOscUsage": moduleDefOscUsage,
       "moduleDefAdmin": moduleDefAdmin,
       "moduleDefScrambling": moduleDefScrambling,
       "moduleDefChannelsNumber": moduleDefChannelsNumber,
       "moduleDefChannelSpacingProvision": moduleDefChannelSpacingProvision,
       "moduleDefMode": moduleDefMode,
       "moduleDefSubBandProvision": moduleDefSubBandProvision,
       "moduleDefAlias": moduleDefAlias,
       "moduleDefFiberType": moduleDefFiberType,
       "moduleDefChannelSpacing": moduleDefChannelSpacing,
       "moduleDefOutputReset": moduleDefOutputReset,
       "moduleDefRoadmNumber": moduleDefRoadmNumber,
       "moduleDefTopology": moduleDefTopology,
       "moduleDefForceConfig": moduleDefForceConfig,
       "moduleDefMuxMethod": moduleDefMuxMethod,
       "moduleDefNdpCleanup": moduleDefNdpCleanup,
       "moduleDefRstp": moduleDefRstp,
       "moduleDefRemoteReset": moduleDefRemoteReset,
       "endOfModuleDefTable": endOfModuleDefTable,
       "endOfEqptMgmtDef": endOfEqptMgmtDef,
       "facilityMgmtDef": facilityMgmtDef,
       "physicalPortDefTable": physicalPortDefTable,
       "physicalPortDefEntry": physicalPortDefEntry,
       "physicalPortDefRowStatus": physicalPortDefRowStatus,
       "physicalPortDefType": physicalPortDefType,
       "physicalPortDefAdmin": physicalPortDefAdmin,
       "physicalPortDefAlias": physicalPortDefAlias,
       "physicalPortDefAlsMode": physicalPortDefAlsMode,
       "physicalPortDefAutoThresReset": physicalPortDefAutoThresReset,
       "physicalPortDefAutonegotiation": physicalPortDefAutonegotiation,
       "physicalPortDefBehaviour": physicalPortDefBehaviour,
       "physicalPortDefDispertionConfig": physicalPortDefDispertionConfig,
       "physicalPortDefDispersionSetting": physicalPortDefDispersionSetting,
       "physicalPortDefDispersionMode": physicalPortDefDispersionMode,
       "physicalPortDefChannelProv": physicalPortDefChannelProv,
       "physicalPortDefWdmRxChannel": physicalPortDefWdmRxChannel,
       "physicalPortDefCodeGain": physicalPortDefCodeGain,
       "physicalPortDefXfpDecisionThres": physicalPortDefXfpDecisionThres,
       "physicalPortDefDisparityCorrection": physicalPortDefDisparityCorrection,
       "physicalPortDefEqlzAdmin": physicalPortDefEqlzAdmin,
       "physicalPortDefErrorForwarding": physicalPortDefErrorForwarding,
       "physicalPortDefFecType": physicalPortDefFecType,
       "physicalPortDefFarEndCommunication": physicalPortDefFarEndCommunication,
       "physicalPortDefFlowControl": physicalPortDefFlowControl,
       "physicalPortDefForceLaserOn": physicalPortDefForceLaserOn,
       "physicalPortDefInhibitSwitchToProt": physicalPortDefInhibitSwitchToProt,
       "physicalPortDefInhibitSwitchToWork": physicalPortDefInhibitSwitchToWork,
       "physicalPortDefLaneChannelSetting": physicalPortDefLaneChannelSetting,
       "physicalPortDefLoopConfig": physicalPortDefLoopConfig,
       "physicalPortDefLaserDelayTimer": physicalPortDefLaserDelayTimer,
       "physicalPortDefLaserOffTimer": physicalPortDefLaserOffTimer,
       "physicalPortDefLaserOnTimer": physicalPortDefLaserOnTimer,
       "physicalPortDefLaserOffDelayFunction": physicalPortDefLaserOffDelayFunction,
       "physicalPortDefAutoPTassignment": physicalPortDefAutoPTassignment,
       "physicalPortDefTributarySlotMethod": physicalPortDefTributarySlotMethod,
       "physicalPortDefInitiateEqualization": physicalPortDefInitiateEqualization,
       "physicalPortDefLossAttenuation": physicalPortDefLossAttenuation,
       "physicalPortDefOpticalSetPoint": physicalPortDefOpticalSetPoint,
       "physicalPortDefDataLayerPmReset": physicalPortDefDataLayerPmReset,
       "physicalPortDefPrbsPmReset": physicalPortDefPrbsPmReset,
       "physicalPortDefTestPrbsRcvMode": physicalPortDefTestPrbsRcvMode,
       "physicalPortDefTestPrbsTrmtMode": physicalPortDefTestPrbsTrmtMode,
       "physicalPortDefSwitchCommand": physicalPortDefSwitchCommand,
       "physicalPortDefOpuPayloadType": physicalPortDefOpuPayloadType,
       "physicalPortDefSigDegThresSonetLine": physicalPortDefSigDegThresSonetLine,
       "physicalPortDefSigDegThresSdhMs": physicalPortDefSigDegThresSdhMs,
       "physicalPortDefSigDegThresOtu": physicalPortDefSigDegThresOtu,
       "physicalPortDefSigDegThresOdu": physicalPortDefSigDegThresOdu,
       "physicalPortDefSigDegThreshold": physicalPortDefSigDegThreshold,
       "physicalPortDefSigDegPcslThreshold": physicalPortDefSigDegPcslThreshold,
       "physicalPortDefSigDegThresSonetSection": physicalPortDefSigDegThresSonetSection,
       "physicalPortDefSigDegThresSdhSection": physicalPortDefSigDegThresSdhSection,
       "physicalPortDefSigDegThresOduTcmA": physicalPortDefSigDegThresOduTcmA,
       "physicalPortDefSigDegThresOduTcmB": physicalPortDefSigDegThresOduTcmB,
       "physicalPortDefSigDegThresOduTcmC": physicalPortDefSigDegThresOduTcmC,
       "physicalPortDefSignalDegradePeriod": physicalPortDefSignalDegradePeriod,
       "physicalPortDefSigDegPeriodOdu": physicalPortDefSigDegPeriodOdu,
       "physicalPortDefSigDegPeriodOtu": physicalPortDefSigDegPeriodOtu,
       "physicalPortDefSigDegPeriodIntegration": physicalPortDefSigDegPeriodIntegration,
       "physicalPortDefSigDegPeriodSdhSection": physicalPortDefSigDegPeriodSdhSection,
       "physicalPortDefSigDegPeriodOduTcmA": physicalPortDefSigDegPeriodOduTcmA,
       "physicalPortDefSigDegPeriodOduTcmB": physicalPortDefSigDegPeriodOduTcmB,
       "physicalPortDefSigDegPeriodOduTcmC": physicalPortDefSigDegPeriodOduTcmC,
       "physicalPortDefOtnStuffing": physicalPortDefOtnStuffing,
       "physicalPortDefTcmALevel": physicalPortDefTcmALevel,
       "physicalPortDefTcmBLevel": physicalPortDefTcmBLevel,
       "physicalPortDefTcmCLevel": physicalPortDefTcmCLevel,
       "physicalPortDefTerminationLevel": physicalPortDefTerminationLevel,
       "physicalPortDefTimingSource": physicalPortDefTimingSource,
       "physicalPortDefTimModeOdu": physicalPortDefTimModeOdu,
       "physicalPortDefTimModeOtu": physicalPortDefTimModeOtu,
       "physicalPortDefTimModeSonetSection": physicalPortDefTimModeSonetSection,
       "physicalPortDefTimModeOduTcmA": physicalPortDefTimModeOduTcmA,
       "physicalPortDefTimModeOduTcmB": physicalPortDefTimModeOduTcmB,
       "physicalPortDefTimModeOduTcmC": physicalPortDefTimModeOduTcmC,
       "physicalPortDefTraceFormSonetSection": physicalPortDefTraceFormSonetSection,
       "physicalPortDefTraceExpectedSonetSection": physicalPortDefTraceExpectedSonetSection,
       "physicalPortDefTraceTransmitSonetSection": physicalPortDefTraceTransmitSonetSection,
       "physicalPortDefTraceExpectedOtu": physicalPortDefTraceExpectedOtu,
       "physicalPortDefTraceTransmitSapiOtu": physicalPortDefTraceTransmitSapiOtu,
       "physicalPortDefTraceTransmitDapiOtu": physicalPortDefTraceTransmitDapiOtu,
       "physicalPortDefTraceTransmitOpspOtu": physicalPortDefTraceTransmitOpspOtu,
       "physicalPortDefTraceExpectedOdu": physicalPortDefTraceExpectedOdu,
       "physicalPortDefTraceTransmitSapiOdu": physicalPortDefTraceTransmitSapiOdu,
       "physicalPortDefTraceTransmitDapiOdu": physicalPortDefTraceTransmitDapiOdu,
       "physicalPortDefTraceTransmitOpspOdu": physicalPortDefTraceTransmitOpspOdu,
       "physicalPortDefTraceExpectedOduTcmA": physicalPortDefTraceExpectedOduTcmA,
       "physicalPortDefTraceTransmitSapiOduTcmA": physicalPortDefTraceTransmitSapiOduTcmA,
       "physicalPortDefTraceTransmitDapiOduTcmA": physicalPortDefTraceTransmitDapiOduTcmA,
       "physicalPortDefTraceTransmitOpspOduTcmA": physicalPortDefTraceTransmitOpspOduTcmA,
       "physicalPortDefTraceExpectedOduTcmB": physicalPortDefTraceExpectedOduTcmB,
       "physicalPortDefTraceTransmitSapiOduTcmB": physicalPortDefTraceTransmitSapiOduTcmB,
       "physicalPortDefTraceTransmitDapiOduTcmB": physicalPortDefTraceTransmitDapiOduTcmB,
       "physicalPortDefTraceTransmitOpspOduTcmB": physicalPortDefTraceTransmitOpspOduTcmB,
       "physicalPortDefTraceExpectedOduTcmC": physicalPortDefTraceExpectedOduTcmC,
       "physicalPortDefTraceTransmitSapiOduTcmC": physicalPortDefTraceTransmitSapiOduTcmC,
       "physicalPortDefTraceTransmitDapiOduTcmC": physicalPortDefTraceTransmitDapiOduTcmC,
       "physicalPortDefTraceTransmitOpspOduTcmC": physicalPortDefTraceTransmitOpspOduTcmC,
       "physicalPortDefTurnupConfig": physicalPortDefTurnupConfig,
       "physicalPortDefTxOffDelay": physicalPortDefTxOffDelay,
       "physicalPortDefVoaMode": physicalPortDefVoaMode,
       "physicalPortDefVoaSetpoint": physicalPortDefVoaSetpoint,
       "physicalPortDefLagPrio": physicalPortDefLagPrio,
       "physicalPortDefMaxFrameSize": physicalPortDefMaxFrameSize,
       "physicalPortDefPayload": physicalPortDefPayload,
       "physicalPortDefPortMode": physicalPortDefPortMode,
       "physicalPortDefPortRole": physicalPortDefPortRole,
       "physicalPortDefPriority": physicalPortDefPriority,
       "physicalPortDefPvid": physicalPortDefPvid,
       "physicalPortDefStagType": physicalPortDefStagType,
       "physicalPortDefUtag": physicalPortDefUtag,
       "physicalPortDefVethAid": physicalPortDefVethAid,
       "physicalPortDefRedLineState": physicalPortDefRedLineState,
       "physicalPortDefTunnelAid": physicalPortDefTunnelAid,
       "physicalPortDefRateLimit": physicalPortDefRateLimit,
       "physicalPortDefTxOffOnTm": physicalPortDefTxOffOnTm,
       "physicalPortDefTxOffTimer": physicalPortDefTxOffTimer,
       "physicalPortDefTxOnTimer": physicalPortDefTxOnTimer,
       "virtualPortDefTable": virtualPortDefTable,
       "virtualPortDefEntry": virtualPortDefEntry,
       "virtualPortDefRowStatus": virtualPortDefRowStatus,
       "virtualPortDefChannelBand": virtualPortDefChannelBand,
       "virtualPortDefType": virtualPortDefType,
       "virtualPortDefAlias": virtualPortDefAlias,
       "virtualPortDefAdmin": virtualPortDefAdmin,
       "virtualPortDefEqlzAdmin": virtualPortDefEqlzAdmin,
       "virtualPortDefInitEqlz": virtualPortDefInitEqlz,
       "virtualPortDefLacpMode": virtualPortDefLacpMode,
       "virtualPortDefLacpTimeout": virtualPortDefLacpTimeout,
       "virtualPortDefLagActivePorts": virtualPortDefLagActivePorts,
       "virtualPortDefMaxFrameSize": virtualPortDefMaxFrameSize,
       "virtualPortDefPortMode": virtualPortDefPortMode,
       "virtualPortDefDataLayerPmReset": virtualPortDefDataLayerPmReset,
       "virtualPortDefPortRole": virtualPortDefPortRole,
       "virtualPortDefLagPortType": virtualPortDefLagPortType,
       "virtualPortDefPriority": virtualPortDefPriority,
       "virtualPortDefPvid": virtualPortDefPvid,
       "virtualPortDefRevertiveMode": virtualPortDefRevertiveMode,
       "virtualPortDefStagType": virtualPortDefStagType,
       "virtualPortDefUtag": virtualPortDefUtag,
       "virtualPortDefBundle": virtualPortDefBundle,
       "virtualPortDefSwitchCommand": virtualPortDefSwitchCommand,
       "virtualPortDefInhibitSwitchToWork": virtualPortDefInhibitSwitchToWork,
       "virtualPortDefInhibitSwitchToProt": virtualPortDefInhibitSwitchToProt,
       "virtualPortDefOduTribPortNo": virtualPortDefOduTribPortNo,
       "virtualPortDefOduTribTimeSlottNo": virtualPortDefOduTribTimeSlottNo,
       "virtualPortDefSigDegThresOdu": virtualPortDefSigDegThresOdu,
       "virtualPortDefSigDegPeriodOdu": virtualPortDefSigDegPeriodOdu,
       "virtualPortDefTraceExpectedOdu": virtualPortDefTraceExpectedOdu,
       "virtualPortDefTraceTransmitSapiOdu": virtualPortDefTraceTransmitSapiOdu,
       "virtualPortDefTraceTransmitDapiOdu": virtualPortDefTraceTransmitDapiOdu,
       "virtualPortDefTraceTransmitOpspOdu": virtualPortDefTraceTransmitOpspOdu,
       "virtualPortDefTimModeOdu": virtualPortDefTimModeOdu,
       "virtualPortDefSigDegThresOduTcmA": virtualPortDefSigDegThresOduTcmA,
       "virtualPortDefSigDegPeriodOduTcmA": virtualPortDefSigDegPeriodOduTcmA,
       "virtualPortDefSigDegThresOduTcmB": virtualPortDefSigDegThresOduTcmB,
       "virtualPortDefSigDegPeriodOduTcmB": virtualPortDefSigDegPeriodOduTcmB,
       "virtualPortDefSigDegThresOduTcmC": virtualPortDefSigDegThresOduTcmC,
       "virtualPortDefSigDegPeriodOduTcmC": virtualPortDefSigDegPeriodOduTcmC,
       "virtualPortDefTcmALevel": virtualPortDefTcmALevel,
       "virtualPortDefTcmBLevel": virtualPortDefTcmBLevel,
       "virtualPortDefTcmCLevel": virtualPortDefTcmCLevel,
       "virtualPortDefTraceTransmitSapiOduTcmA": virtualPortDefTraceTransmitSapiOduTcmA,
       "virtualPortDefTraceTransmitDapiOduTcmA": virtualPortDefTraceTransmitDapiOduTcmA,
       "virtualPortDefTraceTransmitOpspOduTcmA": virtualPortDefTraceTransmitOpspOduTcmA,
       "virtualPortDefTraceExpectedOduTcmA": virtualPortDefTraceExpectedOduTcmA,
       "virtualPortDefTimModeOduTcmA": virtualPortDefTimModeOduTcmA,
       "virtualPortDefTraceExpectedOduTcmB": virtualPortDefTraceExpectedOduTcmB,
       "virtualPortDefTraceTransmitSapiOduTcmB": virtualPortDefTraceTransmitSapiOduTcmB,
       "virtualPortDefTraceTransmitDapiOduTcmB": virtualPortDefTraceTransmitDapiOduTcmB,
       "virtualPortDefTraceTransmitOpspOduTcmB": virtualPortDefTraceTransmitOpspOduTcmB,
       "virtualPortDefTimModeOduTcmB": virtualPortDefTimModeOduTcmB,
       "virtualPortDefTraceExpectedOduTcmC": virtualPortDefTraceExpectedOduTcmC,
       "virtualPortDefTraceTransmitSapiOduTcmC": virtualPortDefTraceTransmitSapiOduTcmC,
       "virtualPortDefTraceTransmitDapiOduTcmC": virtualPortDefTraceTransmitDapiOduTcmC,
       "virtualPortDefTraceTransmitOpspOduTcmC": virtualPortDefTraceTransmitOpspOduTcmC,
       "virtualPortDefTimModeOduTcmC": virtualPortDefTimModeOduTcmC,
       "virtualPortDefTerminationLevel": virtualPortDefTerminationLevel,
       "virtualPortDefLoopConfig": virtualPortDefLoopConfig,
       "virtualPortDefVcType": virtualPortDefVcType,
       "virtualPortDefCir": virtualPortDefCir,
       "virtualPortDefOpuPayloadType": virtualPortDefOpuPayloadType,
       "virtualPortDefOtnStuffing": virtualPortDefOtnStuffing,
       "virtualPortDefRedLineState": virtualPortDefRedLineState,
       "virtualPortDefTunnelAid": virtualPortDefTunnelAid,
       "endOfVirtualPortDefTable": endOfVirtualPortDefTable,
       "endOfFacilityMgmtDef": endOfFacilityMgmtDef,
       "dcnMgmtDef": dcnMgmtDef,
       "linkDefTable": linkDefTable,
       "linkDefEntry": linkDefEntry,
       "linkDefRowStatus": linkDefRowStatus,
       "linkDefType": linkDefType,
       "linkDefAdmin": linkDefAdmin,
       "linkDefAlias": linkDefAlias,
       "linkDefAuthString": linkDefAuthString,
       "linkDefProxyArp": linkDefProxyArp,
       "linkDefOspf": linkDefOspf,
       "linkDefBaud": linkDefBaud,
       "linkDefAuthType": linkDefAuthType,
       "linkDefIpType": linkDefIpType,
       "linkDefMetric": linkDefMetric,
       "linkDefAreaAid": linkDefAreaAid,
       "linkDefNearEndIp": linkDefNearEndIp,
       "linkDefBitrate": linkDefBitrate,
       "linkDefIPv6Type": linkDefIPv6Type,
       "linkDefNendIPv6": linkDefNendIPv6,
       "endOfLinkDefTable": endOfLinkDefTable,
       "scDefTable": scDefTable,
       "scDefEntry": scDefEntry,
       "scDefRowStatus": scDefRowStatus,
       "scDefType": scDefType,
       "scDefAdmin": scDefAdmin,
       "scDefAlias": scDefAlias,
       "scDefAuthString": scDefAuthString,
       "scDefOspf": scDefOspf,
       "scDefAuthType": scDefAuthType,
       "scDefIpType": scDefIpType,
       "scDefMetric": scDefMetric,
       "scDefAreaAid": scDefAreaAid,
       "scDefAlsMode": scDefAlsMode,
       "scDefSigDegThresReceiver": scDefSigDegThresReceiver,
       "scDefAutonegotiation": scDefAutonegotiation,
       "scDefBitrate": scDefBitrate,
       "scDefDuplex": scDefDuplex,
       "scDefAttGradientTh": scDefAttGradientTh,
       "scDefIpAddr": scDefIpAddr,
       "scDefLanAid": scDefLanAid,
       "scDefIpMask": scDefIpMask,
       "scDefDataLayerPmReset": scDefDataLayerPmReset,
       "scDefPriority": scDefPriority,
       "scDefIPv6": scDefIPv6,
       "scDefIPv6PrefixLen": scDefIPv6PrefixLen,
       "scDefIpMode": scDefIpMode,
       "scDefGatewayProxyArp": scDefGatewayProxyArp,
       "endOfScDefTable": endOfScDefTable,
       "lanDefTable": lanDefTable,
       "lanDefEntry": lanDefEntry,
       "lanDefRowStatus": lanDefRowStatus,
       "lanDefType": lanDefType,
       "lanDefAdmin": lanDefAdmin,
       "lanDefAlias": lanDefAlias,
       "lanDefAuthString": lanDefAuthString,
       "lanDefOspf": lanDefOspf,
       "lanDefAuthType": lanDefAuthType,
       "lanDefIpType": lanDefIpType,
       "lanDefMetric": lanDefMetric,
       "lanDefAreaAid": lanDefAreaAid,
       "lanDefIpAddr": lanDefIpAddr,
       "lanDefIpMask": lanDefIpMask,
       "lanDefPriority": lanDefPriority,
       "lanDefIPv6": lanDefIPv6,
       "lanDefIPv6PrefixLen": lanDefIPv6PrefixLen,
       "lanDefIpMode": lanDefIpMode,
       "endOfLanDefTable": endOfLanDefTable,
       "eccDefTable": eccDefTable,
       "eccDefEntry": eccDefEntry,
       "eccDefRowStatus": eccDefRowStatus,
       "eccDefType": eccDefType,
       "eccDefAdmin": eccDefAdmin,
       "eccDefAlias": eccDefAlias,
       "eccDefLanAid": eccDefLanAid,
       "eccDefExternalVid": eccDefExternalVid,
       "endOfEccDefTable": endOfEccDefTable,
       "endOfDcnMgmtDef": endOfDcnMgmtDef,
       "opticalMuxMgmtDef": opticalMuxMgmtDef,
       "opticalMuxDefTable": opticalMuxDefTable,
       "opticalMuxDefEntry": opticalMuxDefEntry,
       "opticalMuxDefRowStatus": opticalMuxDefRowStatus,
       "opticalMuxDefPumpPower": opticalMuxDefPumpPower,
       "opticalMuxDefInhibitSwitchToWork": opticalMuxDefInhibitSwitchToWork,
       "opticalMuxDefForceLaserOn": opticalMuxDefForceLaserOn,
       "opticalMuxDefAseTabCreation": opticalMuxDefAseTabCreation,
       "opticalMuxDefOpticalSetPoint": opticalMuxDefOpticalSetPoint,
       "opticalMuxDefInitiateEqualization": opticalMuxDefInitiateEqualization,
       "opticalMuxDefTilt": opticalMuxDefTilt,
       "opticalMuxDefOscOpticalSetpoint": opticalMuxDefOscOpticalSetpoint,
       "opticalMuxDefOffset": opticalMuxDefOffset,
       "opticalMuxDefSwitchCommand": opticalMuxDefSwitchCommand,
       "opticalMuxDefAlsMode": opticalMuxDefAlsMode,
       "opticalMuxDefType": opticalMuxDefType,
       "opticalMuxDefAttenuationGradient": opticalMuxDefAttenuationGradient,
       "opticalMuxDefInhibitSwitchToProt": opticalMuxDefInhibitSwitchToProt,
       "opticalMuxDefVariableGain": opticalMuxDefVariableGain,
       "opticalMuxDefAdmin": opticalMuxDefAdmin,
       "opticalMuxDefTimePeriod": opticalMuxDefTimePeriod,
       "opticalMuxDefSigDegThresReceiver": opticalMuxDefSigDegThresReceiver,
       "opticalMuxDefAlias": opticalMuxDefAlias,
       "opticalMuxDefDataLayerPmReset": opticalMuxDefDataLayerPmReset,
       "opticalMuxDefGain": opticalMuxDefGain,
       "opticalMuxDefEdfaPwrOut": opticalMuxDefEdfaPwrOut,
       "opticalMuxDefVoaSetpoint": opticalMuxDefVoaSetpoint,
       "opticalMuxDefFiberBrand": opticalMuxDefFiberBrand,
       "opticalMuxDefTiltSet": opticalMuxDefTiltSet,
       "opticalMuxDefForceFwdAsePilotOn": opticalMuxDefForceFwdAsePilotOn,
       "opticalMuxDefBandProvision": opticalMuxDefBandProvision,
       "opticalMuxDefOffsetHigh": opticalMuxDefOffsetHigh,
       "opticalMuxDefOffsetLow": opticalMuxDefOffsetLow,
       "opticalMuxDefOptUpdate": opticalMuxDefOptUpdate,
       "endOfOpticalMuxDefTable": endOfOpticalMuxDefTable,
       "endOfOpticalMuxMgmtDef": endOfOpticalMuxMgmtDef,
       "shelfConnMgmtDef": shelfConnMgmtDef,
       "shelfConnDefTable": shelfConnDefTable,
       "shelfConnDefEntry": shelfConnDefEntry,
       "shelfConnDefRowStatus": shelfConnDefRowStatus,
       "shelfConnDefAdmin": shelfConnDefAdmin,
       "shelfConnDefAlias": shelfConnDefAlias,
       "shelfConnDefFacilityType": shelfConnDefFacilityType,
       "endOfShelfConnDefTable": endOfShelfConnDefTable,
       "endOfShelfConnMgmtDef": endOfShelfConnMgmtDef,
       "envMgmtDef": envMgmtDef,
       "envPortDefTable": envPortDefTable,
       "envPortDefEntry": envPortDefEntry,
       "envPortDefRowStatus": envPortDefRowStatus,
       "envPortDefTelemetry": envPortDefTelemetry,
       "envPortDefFacilityType": envPortDefFacilityType,
       "envPortDefTifAlarmType": envPortDefTifAlarmType,
       "envPortDefTifAlarmMessage": envPortDefTifAlarmMessage,
       "envPortDefInvertTifInputLogic": envPortDefInvertTifInputLogic,
       "endOfEnvPortDefTable": endOfEnvPortDefTable,
       "endOfEnvMgmtDef": endOfEnvMgmtDef,
       "containerMgmtDef": containerMgmtDef,
       "containerDefTable": containerDefTable,
       "containerDefEntry": containerDefEntry,
       "containerDefRowStatus": containerDefRowStatus,
       "containerDefFacilityType": containerDefFacilityType,
       "endOfContainerDefTable": endOfContainerDefTable,
       "endOfContainerMgmtDef": endOfContainerMgmtDef,
       "opticalLineMgmtDef": opticalLineMgmtDef,
       "opticalLineDefTable": opticalLineDefTable,
       "opticalLineDefEntry": opticalLineDefEntry,
       "opticalLineDefRowStatus": opticalLineDefRowStatus,
       "opticalLineDefTxLineAttenuation": opticalLineDefTxLineAttenuation,
       "opticalLineDefRxLineAttenuation": opticalLineDefRxLineAttenuation,
       "opticalLineDefAlias": opticalLineDefAlias,
       "opticalLineDefFarEndLocation": opticalLineDefFarEndLocation,
       "endOfOpticalLineDefTable": endOfOpticalLineDefTable,
       "endOfOpticalLineMgmtDef": endOfOpticalLineMgmtDef,
       "performanceDef": performanceDef,
       "performanceFacilityDef": performanceFacilityDef,
       "performanceFacilityThresholdDef": performanceFacilityThresholdDef,
       "optThresholdConfigDefTable": optThresholdConfigDefTable,
       "optThresholdConfigDefEntry": optThresholdConfigDefEntry,
       "optThresholdConfigDefLowConfig": optThresholdConfigDefLowConfig,
       "optThresholdConfigDefHighConfig": optThresholdConfigDefHighConfig,
       "oprThresholdConfigDefTable": oprThresholdConfigDefTable,
       "oprThresholdConfigDefEntry": oprThresholdConfigDefEntry,
       "oprThresholdConfigDefLowConfig": oprThresholdConfigDefLowConfig,
       "oprThresholdConfigDefHighConfig": oprThresholdConfigDefHighConfig,
       "endOfOprThresholdConfigDefTable": endOfOprThresholdConfigDefTable,
       "endOfPerformanceFacilityThresholdDef": endOfPerformanceFacilityThresholdDef,
       "featureSpecificDef": featureSpecificDef,
       "fiberMapDef": fiberMapDef,
       "terminationPointDefTable": terminationPointDefTable,
       "terminationPointDefEntry": terminationPointDefEntry,
       "terminationPointDefRowStatus": terminationPointDefRowStatus,
       "terminationPointDefAdmin": terminationPointDefAdmin,
       "terminationPointDefFiberDetect": terminationPointDefFiberDetect,
       "terminationPointDefAlias": terminationPointDefAlias,
       "connectionDefTable": connectionDefTable,
       "connectionDefEntry": connectionDefEntry,
       "connectionDefRowStatus": connectionDefRowStatus,
       "connectionDefType": connectionDefType,
       "endOfConnectionDefTable": endOfConnectionDefTable,
       "endOfFiberMapDef": endOfFiberMapDef,
       "eciDef": eciDef,
       "externalPortDefTable": externalPortDefTable,
       "externalPortDefEntry": externalPortDefEntry,
       "externalPortDefRowStatus": externalPortDefRowStatus,
       "externalPortDefType": externalPortDefType,
       "externalPortDefTransmitChannel": externalPortDefTransmitChannel,
       "externalPortDefChannelBandwith": externalPortDefChannelBandwith,
       "externalPortDefAlias": externalPortDefAlias,
       "externalPortDefFarEndLocation": externalPortDefFarEndLocation,
       "externalPortDefBitrate": externalPortDefBitrate,
       "externalPortDefFecType": externalPortDefFecType,
       "externalPortDefLineCoding": externalPortDefLineCoding,
       "externalPortDefFrameFormat": externalPortDefFrameFormat,
       "externalPortDefOpticalPowerTx": externalPortDefOpticalPowerTx,
       "externalPortDefOsnrTransmit": externalPortDefOsnrTransmit,
       "externalPortDefPmdTransmit": externalPortDefPmdTransmit,
       "externalPortDefChromDisperTx": externalPortDefChromDisperTx,
       "externalPortDefMinOsnrRcv": externalPortDefMinOsnrRcv,
       "externalPortDefMinOptPowerRcv": externalPortDefMinOptPowerRcv,
       "externalPortDefMaxOptPowerRcv": externalPortDefMaxOptPowerRcv,
       "externalPortDefMaxPmdRcv": externalPortDefMaxPmdRcv,
       "externalPortDefMinChromDisperRcv": externalPortDefMinChromDisperRcv,
       "externalPortDefMaxChromDisperRcv": externalPortDefMaxChromDisperRcv,
       "externalPortDefMaxBitErrorRate": externalPortDefMaxBitErrorRate,
       "externalPortDefSourceProfile": externalPortDefSourceProfile,
       "endOfExternalPortDefTable": endOfExternalPortDefTable,
       "endOfEciDef": endOfEciDef,
       "changeServiceDef": changeServiceDef,
       "changePhysicalPortServiceDefTable": changePhysicalPortServiceDefTable,
       "changePhysicalPortServiceDefEntry": changePhysicalPortServiceDefEntry,
       "changePhysicalPortServiceDefRowStatus": changePhysicalPortServiceDefRowStatus,
       "changePhysicalPortServiceDefType": changePhysicalPortServiceDefType,
       "changePhysicalPortServiceDefAdmin": changePhysicalPortServiceDefAdmin,
       "changePhysicalPortServiceDefAlias": changePhysicalPortServiceDefAlias,
       "changePhysicalPortServiceDefAlsMode": changePhysicalPortServiceDefAlsMode,
       "changePhysicalPortServiceDefBehaviour": changePhysicalPortServiceDefBehaviour,
       "changePhysicalPortServiceDefDispersionSetting": changePhysicalPortServiceDefDispersionSetting,
       "changePhysicalPortServiceDefDispersionMode": changePhysicalPortServiceDefDispersionMode,
       "changePhysicalPortServiceDefChannelProv": changePhysicalPortServiceDefChannelProv,
       "changePhysicalPortServiceDefWdmRxChannel": changePhysicalPortServiceDefWdmRxChannel,
       "changePhysicalPortServiceDefCodeGain": changePhysicalPortServiceDefCodeGain,
       "changePhysicalPortServiceDefXfpDecisionThres": changePhysicalPortServiceDefXfpDecisionThres,
       "changePhysicalPortServiceDefDisparityCorrection": changePhysicalPortServiceDefDisparityCorrection,
       "changePhysicalPortServiceDefEqlzAdmin": changePhysicalPortServiceDefEqlzAdmin,
       "changePhysicalPortServiceDefErrorForwarding": changePhysicalPortServiceDefErrorForwarding,
       "changePhysicalPortServiceDefFecType": changePhysicalPortServiceDefFecType,
       "changePhysicalPortServiceDefFarEndCommunication": changePhysicalPortServiceDefFarEndCommunication,
       "changePhysicalPortServiceDefFlowControl": changePhysicalPortServiceDefFlowControl,
       "changePhysicalPortServiceDefLaneChannelSetting": changePhysicalPortServiceDefLaneChannelSetting,
       "changePhysicalPortServiceDefLaserDelayTimer": changePhysicalPortServiceDefLaserDelayTimer,
       "changePhysicalPortServiceDefLaserOffTimer": changePhysicalPortServiceDefLaserOffTimer,
       "changePhysicalPortServiceDefLaserOnTimer": changePhysicalPortServiceDefLaserOnTimer,
       "changePhysicalPortServiceDefLaserOffDelayFunction": changePhysicalPortServiceDefLaserOffDelayFunction,
       "changePhysicalPortServiceDefAutoPTassignment": changePhysicalPortServiceDefAutoPTassignment,
       "changePhysicalPortServiceDefTributarySlotMethod": changePhysicalPortServiceDefTributarySlotMethod,
       "changePhysicalPortServiceDefOpticalSetPoint": changePhysicalPortServiceDefOpticalSetPoint,
       "changePhysicalPortServiceDefOpuPayloadType": changePhysicalPortServiceDefOpuPayloadType,
       "changePhysicalPortServiceDefSigDegThresSonetLine": changePhysicalPortServiceDefSigDegThresSonetLine,
       "changePhysicalPortServiceDefSigDegThresSdhMs": changePhysicalPortServiceDefSigDegThresSdhMs,
       "changePhysicalPortServiceDefSigDegThresOtu": changePhysicalPortServiceDefSigDegThresOtu,
       "changePhysicalPortServiceDefSigDegThresOdu": changePhysicalPortServiceDefSigDegThresOdu,
       "changePhysicalPortServiceDefSigDegThreshold": changePhysicalPortServiceDefSigDegThreshold,
       "changePhysicalPortServiceDefSigDegPcslThreshold": changePhysicalPortServiceDefSigDegPcslThreshold,
       "changePhysicalPortServiceDefSigDegThresSonetSection": changePhysicalPortServiceDefSigDegThresSonetSection,
       "changePhysicalPortServiceDefSigDegThresSdhSection": changePhysicalPortServiceDefSigDegThresSdhSection,
       "changePhysicalPortServiceDefSigDegThresOduTcmA": changePhysicalPortServiceDefSigDegThresOduTcmA,
       "changePhysicalPortServiceDefSigDegThresOduTcmB": changePhysicalPortServiceDefSigDegThresOduTcmB,
       "changePhysicalPortServiceDefSigDegThresOduTcmC": changePhysicalPortServiceDefSigDegThresOduTcmC,
       "changePhysicalPortServiceDefSignalDegradePeriod": changePhysicalPortServiceDefSignalDegradePeriod,
       "changePhysicalPortServiceDefSigDegPeriodOdu": changePhysicalPortServiceDefSigDegPeriodOdu,
       "changePhysicalPortServiceDefSigDegPeriodOtu": changePhysicalPortServiceDefSigDegPeriodOtu,
       "changePhysicalPortServiceDefSigDegPeriodIntegration": changePhysicalPortServiceDefSigDegPeriodIntegration,
       "changePhysicalPortServiceDefSigDegPeriodSdhSection": changePhysicalPortServiceDefSigDegPeriodSdhSection,
       "changePhysicalPortServiceDefSigDegPeriodOduTcmA": changePhysicalPortServiceDefSigDegPeriodOduTcmA,
       "changePhysicalPortServiceDefSigDegPeriodOduTcmB": changePhysicalPortServiceDefSigDegPeriodOduTcmB,
       "changePhysicalPortServiceDefSigDegPeriodOduTcmC": changePhysicalPortServiceDefSigDegPeriodOduTcmC,
       "changePhysicalPortServiceDefOtnStuffing": changePhysicalPortServiceDefOtnStuffing,
       "changePhysicalPortServiceDefTcmALevel": changePhysicalPortServiceDefTcmALevel,
       "changePhysicalPortServiceDefTcmBLevel": changePhysicalPortServiceDefTcmBLevel,
       "changePhysicalPortServiceDefTcmCLevel": changePhysicalPortServiceDefTcmCLevel,
       "changePhysicalPortServiceDefTerminationLevel": changePhysicalPortServiceDefTerminationLevel,
       "changePhysicalPortServiceDefTimingSource": changePhysicalPortServiceDefTimingSource,
       "changePhysicalPortServiceDefTimModeOdu": changePhysicalPortServiceDefTimModeOdu,
       "changePhysicalPortServiceDefTimModeOtu": changePhysicalPortServiceDefTimModeOtu,
       "changePhysicalPortServiceDefTimModeSonetSection": changePhysicalPortServiceDefTimModeSonetSection,
       "changePhysicalPortServiceDefTimModeOduTcmA": changePhysicalPortServiceDefTimModeOduTcmA,
       "changePhysicalPortServiceDefTimModeOduTcmB": changePhysicalPortServiceDefTimModeOduTcmB,
       "changePhysicalPortServiceDefTimModeOduTcmC": changePhysicalPortServiceDefTimModeOduTcmC,
       "changePhysicalPortServiceDefTraceFormSonetSection": changePhysicalPortServiceDefTraceFormSonetSection,
       "changePhysicalPortServiceDefTraceExpectedSonetSection": changePhysicalPortServiceDefTraceExpectedSonetSection,
       "changePhysicalPortServiceDefTraceTransmitSonetSection": changePhysicalPortServiceDefTraceTransmitSonetSection,
       "changePhysicalPortServiceDefTraceExpectedOtu": changePhysicalPortServiceDefTraceExpectedOtu,
       "changePhysicalPortServiceDefTraceTransmitSapiOtu": changePhysicalPortServiceDefTraceTransmitSapiOtu,
       "changePhysicalPortServiceDefTraceTransmitDapiOtu": changePhysicalPortServiceDefTraceTransmitDapiOtu,
       "changePhysicalPortServiceDefTraceTransmitOpspOtu": changePhysicalPortServiceDefTraceTransmitOpspOtu,
       "changePhysicalPortServiceDefTraceExpectedOdu": changePhysicalPortServiceDefTraceExpectedOdu,
       "changePhysicalPortServiceDefTraceTransmitSapiOdu": changePhysicalPortServiceDefTraceTransmitSapiOdu,
       "changePhysicalPortServiceDefTraceTransmitDapiOdu": changePhysicalPortServiceDefTraceTransmitDapiOdu,
       "changePhysicalPortServiceDefTraceTransmitOpspOdu": changePhysicalPortServiceDefTraceTransmitOpspOdu,
       "changePhysicalPortServiceDefTraceExpectedOduTcmA": changePhysicalPortServiceDefTraceExpectedOduTcmA,
       "changePhysicalPortServiceDefTraceTransmitSapiOduTcmA": changePhysicalPortServiceDefTraceTransmitSapiOduTcmA,
       "changePhysicalPortServiceDefTraceTransmitDapiOduTcmA": changePhysicalPortServiceDefTraceTransmitDapiOduTcmA,
       "changePhysicalPortServiceDefTraceTransmitOpspOduTcmA": changePhysicalPortServiceDefTraceTransmitOpspOduTcmA,
       "changePhysicalPortServiceDefTraceExpectedOduTcmB": changePhysicalPortServiceDefTraceExpectedOduTcmB,
       "changePhysicalPortServiceDefTraceTransmitSapiOduTcmB": changePhysicalPortServiceDefTraceTransmitSapiOduTcmB,
       "changePhysicalPortServiceDefTraceTransmitDapiOduTcmB": changePhysicalPortServiceDefTraceTransmitDapiOduTcmB,
       "changePhysicalPortServiceDefTraceTransmitOpspOduTcmB": changePhysicalPortServiceDefTraceTransmitOpspOduTcmB,
       "changePhysicalPortServiceDefTraceExpectedOduTcmC": changePhysicalPortServiceDefTraceExpectedOduTcmC,
       "changePhysicalPortServiceDefTraceTransmitSapiOduTcmC": changePhysicalPortServiceDefTraceTransmitSapiOduTcmC,
       "changePhysicalPortServiceDefTraceTransmitDapiOduTcmC": changePhysicalPortServiceDefTraceTransmitDapiOduTcmC,
       "changePhysicalPortServiceDefTraceTransmitOpspOduTcmC": changePhysicalPortServiceDefTraceTransmitOpspOduTcmC,
       "changePhysicalPortServiceDefTxOffDelay": changePhysicalPortServiceDefTxOffDelay,
       "changePhysicalPortServiceDefVoaMode": changePhysicalPortServiceDefVoaMode,
       "changePhysicalPortServiceDefVoaSetpoint": changePhysicalPortServiceDefVoaSetpoint,
       "endOfChangePhysicalPortServiceDefTable": endOfChangePhysicalPortServiceDefTable,
       "endOfChangeServiceDef": endOfChangeServiceDef,
       "protectionDef": protectionDef,
       "ffpDefTable": ffpDefTable,
       "ffpDefEntry": ffpDefEntry,
       "ffpDefRowStatus": ffpDefRowStatus,
       "ffpDefCreationMethod": ffpDefCreationMethod,
       "ffpDefSDswitching": ffpDefSDswitching,
       "ffpDefHoldOffTime": ffpDefHoldOffTime,
       "ffpDefProtectionMech": ffpDefProtectionMech,
       "ffpDefWorkingAid": ffpDefWorkingAid,
       "ffpDefProtectionAid": ffpDefProtectionAid,
       "ffpDefSignalDegradeSwitching": ffpDefSignalDegradeSwitching,
       "ffpDefSignalFailureSwitching": ffpDefSignalFailureSwitching,
       "ffpDefFarEndIp": ffpDefFarEndIp,
       "ffpDefPeerAid": ffpDefPeerAid,
       "ffpDefApsType": ffpDefApsType,
       "ffpDefRevertMode": ffpDefRevertMode,
       "ffpDefWaitToRestore": ffpDefWaitToRestore,
       "ffpDefDirection": ffpDefDirection,
       "ffpDefProtectionType": ffpDefProtectionType,
       "endOfFfpDefTable": endOfFfpDefTable,
       "endOfProtectionDef": endOfProtectionDef,
       "conformanceDef": conformanceDef,
       "compliancesDef": compliancesDef,
       "complianceDef": complianceDef,
       "groupsDef": groupsDef,
       "objectGroupDef": objectGroupDef}
)
