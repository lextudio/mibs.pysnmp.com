# SNMP MIB module (TAVVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TAVVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:55 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tavve_ObjectIdentity = ObjectIdentity
tavve = _Tavve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1)
)
_EventWatch_ObjectIdentity = ObjectIdentity
eventWatch = _EventWatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1)
)
_TscEwSourceNode_Type = DisplayString
_TscEwSourceNode_Object = MibScalar
tscEwSourceNode = _TscEwSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 1),
    _TscEwSourceNode_Type()
)
tscEwSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwSourceNode.setStatus("optional")
_TscEwFaultAddr_Type = DisplayString
_TscEwFaultAddr_Object = MibScalar
tscEwFaultAddr = _TscEwFaultAddr_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 2),
    _TscEwFaultAddr_Type()
)
tscEwFaultAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwFaultAddr.setStatus("optional")
_TscEwFaultTimes_Type = DisplayString
_TscEwFaultTimes_Object = MibScalar
tscEwFaultTimes = _TscEwFaultTimes_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 3),
    _TscEwFaultTimes_Type()
)
tscEwFaultTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwFaultTimes.setStatus("optional")
_TscEwSourceAddr_Type = DisplayString
_TscEwSourceAddr_Object = MibScalar
tscEwSourceAddr = _TscEwSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 6),
    _TscEwSourceAddr_Type()
)
tscEwSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwSourceAddr.setStatus("optional")
_TscEwGroupName_Type = DisplayString
_TscEwGroupName_Object = MibScalar
tscEwGroupName = _TscEwGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 7),
    _TscEwGroupName_Type()
)
tscEwGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwGroupName.setStatus("optional")
_TscEwSourceName_Type = DisplayString
_TscEwSourceName_Object = MibScalar
tscEwSourceName = _TscEwSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 8),
    _TscEwSourceName_Type()
)
tscEwSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwSourceName.setStatus("optional")
_TscEwSourceProtocol_Type = DisplayString
_TscEwSourceProtocol_Object = MibScalar
tscEwSourceProtocol = _TscEwSourceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 9),
    _TscEwSourceProtocol_Type()
)
tscEwSourceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwSourceProtocol.setStatus("optional")
_TscEwFaultName_Type = DisplayString
_TscEwFaultName_Object = MibScalar
tscEwFaultName = _TscEwFaultName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 10),
    _TscEwFaultName_Type()
)
tscEwFaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwFaultName.setStatus("optional")
_TscEwFaultProtocol_Type = DisplayString
_TscEwFaultProtocol_Object = MibScalar
tscEwFaultProtocol = _TscEwFaultProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 11),
    _TscEwFaultProtocol_Type()
)
tscEwFaultProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwFaultProtocol.setStatus("optional")
_TscEwUserThreshold_Type = Integer32
_TscEwUserThreshold_Object = MibScalar
tscEwUserThreshold = _TscEwUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 12),
    _TscEwUserThreshold_Type()
)
tscEwUserThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwUserThreshold.setStatus("optional")
_TscEwSlaValue_Type = Integer32
_TscEwSlaValue_Object = MibScalar
tscEwSlaValue = _TscEwSlaValue_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 13),
    _TscEwSlaValue_Type()
)
tscEwSlaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwSlaValue.setStatus("optional")
_TscEwReportHost_Type = DisplayString
_TscEwReportHost_Object = MibScalar
tscEwReportHost = _TscEwReportHost_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 14),
    _TscEwReportHost_Type()
)
tscEwReportHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwReportHost.setStatus("optional")
_TscEwDownTime_Type = Integer32
_TscEwDownTime_Object = MibScalar
tscEwDownTime = _TscEwDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 15),
    _TscEwDownTime_Type()
)
tscEwDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwDownTime.setStatus("optional")
_TscEwEventTime_Type = Integer32
_TscEwEventTime_Object = MibScalar
tscEwEventTime = _TscEwEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 16),
    _TscEwEventTime_Type()
)
tscEwEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwEventTime.setStatus("optional")
_TscEwDescr_Type = DisplayString
_TscEwDescr_Object = MibScalar
tscEwDescr = _TscEwDescr_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 17),
    _TscEwDescr_Type()
)
tscEwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscEwDescr.setStatus("optional")
_Tcpdmon_ObjectIdentity = ObjectIdentity
tcpdmon = _Tcpdmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 2)
)
_TscTcpSourceNode_Type = DisplayString
_TscTcpSourceNode_Object = MibScalar
tscTcpSourceNode = _TscTcpSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 2, 1),
    _TscTcpSourceNode_Type()
)
tscTcpSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscTcpSourceNode.setStatus("optional")
_TscTCPPortName_Type = DisplayString
_TscTCPPortName_Object = MibScalar
tscTCPPortName = _TscTCPPortName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 2, 2),
    _TscTCPPortName_Type()
)
tscTCPPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscTCPPortName.setStatus("optional")
_TscTCPPortNumber_Type = DisplayString
_TscTCPPortNumber_Object = MibScalar
tscTCPPortNumber = _TscTCPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 2, 3),
    _TscTCPPortNumber_Type()
)
tscTCPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscTCPPortNumber.setStatus("optional")
_TscTCPTime_Type = DisplayString
_TscTCPTime_Object = MibScalar
tscTCPTime = _TscTCPTime_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 2, 4),
    _TscTCPTime_Type()
)
tscTCPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscTCPTime.setStatus("optional")
_Ciscotrap_ObjectIdentity = ObjectIdentity
ciscotrap = _Ciscotrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3)
)
_TscCtLogMessage_Type = DisplayString
_TscCtLogMessage_Object = MibScalar
tscCtLogMessage = _TscCtLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 1),
    _TscCtLogMessage_Type()
)
tscCtLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscCtLogMessage.setStatus("optional")
_TscCtFacility_Type = DisplayString
_TscCtFacility_Object = MibScalar
tscCtFacility = _TscCtFacility_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 2),
    _TscCtFacility_Type()
)
tscCtFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscCtFacility.setStatus("optional")
_TscCtSeverity_Type = DisplayString
_TscCtSeverity_Object = MibScalar
tscCtSeverity = _TscCtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 3),
    _TscCtSeverity_Type()
)
tscCtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscCtSeverity.setStatus("optional")
_TscCtMnemonic_Type = DisplayString
_TscCtMnemonic_Object = MibScalar
tscCtMnemonic = _TscCtMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 4),
    _TscCtMnemonic_Type()
)
tscCtMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscCtMnemonic.setStatus("optional")
_TscCtMessage_Type = DisplayString
_TscCtMessage_Object = MibScalar
tscCtMessage = _TscCtMessage_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 5),
    _TscCtMessage_Type()
)
tscCtMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscCtMessage.setStatus("optional")
_Wwwmon_ObjectIdentity = ObjectIdentity
wwwmon = _Wwwmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4)
)
_WwwmonServerName_Type = DisplayString
_WwwmonServerName_Object = MibScalar
wwwmonServerName = _WwwmonServerName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 1),
    _WwwmonServerName_Type()
)
wwwmonServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwmonServerName.setStatus("optional")
_WwwmonServerPort_Type = Integer32
_WwwmonServerPort_Object = MibScalar
wwwmonServerPort = _WwwmonServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 2),
    _WwwmonServerPort_Type()
)
wwwmonServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwmonServerPort.setStatus("optional")
_WwwmonServerURL_Type = DisplayString
_WwwmonServerURL_Object = MibScalar
wwwmonServerURL = _WwwmonServerURL_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 3),
    _WwwmonServerURL_Type()
)
wwwmonServerURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwmonServerURL.setStatus("optional")
_WwwmonServerStatus_Type = DisplayString
_WwwmonServerStatus_Object = MibScalar
wwwmonServerStatus = _WwwmonServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 4),
    _WwwmonServerStatus_Type()
)
wwwmonServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwmonServerStatus.setStatus("optional")
_Agentmon_ObjectIdentity = ObjectIdentity
agentmon = _Agentmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 5)
)
_Remote_ObjectIdentity = ObjectIdentity
remote = _Remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6)
)
_TscRemoteSourceNode_Type = DisplayString
_TscRemoteSourceNode_Object = MibScalar
tscRemoteSourceNode = _TscRemoteSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 1),
    _TscRemoteSourceNode_Type()
)
tscRemoteSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteSourceNode.setStatus("optional")
_TscRemoteValue_Type = Integer32
_TscRemoteValue_Object = MibScalar
tscRemoteValue = _TscRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 2),
    _TscRemoteValue_Type()
)
tscRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteValue.setStatus("optional")
_TscRemoteThreshold_Type = Integer32
_TscRemoteThreshold_Object = MibScalar
tscRemoteThreshold = _TscRemoteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 3),
    _TscRemoteThreshold_Type()
)
tscRemoteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteThreshold.setStatus("optional")
_TscRemoteRearm_Type = Integer32
_TscRemoteRearm_Object = MibScalar
tscRemoteRearm = _TscRemoteRearm_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 4),
    _TscRemoteRearm_Type()
)
tscRemoteRearm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteRearm.setStatus("optional")
_TscRemoteSourceAddr_Type = DisplayString
_TscRemoteSourceAddr_Object = MibScalar
tscRemoteSourceAddr = _TscRemoteSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 5),
    _TscRemoteSourceAddr_Type()
)
tscRemoteSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteSourceAddr.setStatus("optional")
_TscRemoteName_Type = DisplayString
_TscRemoteName_Object = MibScalar
tscRemoteName = _TscRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 6),
    _TscRemoteName_Type()
)
tscRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteName.setStatus("optional")
_TscRemoteSourceNode2_Type = DisplayString
_TscRemoteSourceNode2_Object = MibScalar
tscRemoteSourceNode2 = _TscRemoteSourceNode2_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 7),
    _TscRemoteSourceNode2_Type()
)
tscRemoteSourceNode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteSourceNode2.setStatus("optional")
_TscRemoteSourceProtocol_Type = DisplayString
_TscRemoteSourceProtocol_Object = MibScalar
tscRemoteSourceProtocol = _TscRemoteSourceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 8),
    _TscRemoteSourceProtocol_Type()
)
tscRemoteSourceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteSourceProtocol.setStatus("optional")
_TscRemoteProcName_Type = DisplayString
_TscRemoteProcName_Object = MibScalar
tscRemoteProcName = _TscRemoteProcName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 9),
    _TscRemoteProcName_Type()
)
tscRemoteProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteProcName.setStatus("optional")
_TscRemoteFsDevice_Type = DisplayString
_TscRemoteFsDevice_Object = MibScalar
tscRemoteFsDevice = _TscRemoteFsDevice_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 10),
    _TscRemoteFsDevice_Type()
)
tscRemoteFsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteFsDevice.setStatus("optional")
_TscRemoteFsName_Type = DisplayString
_TscRemoteFsName_Object = MibScalar
tscRemoteFsName = _TscRemoteFsName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 11),
    _TscRemoteFsName_Type()
)
tscRemoteFsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteFsName.setStatus("optional")
_TscRemoteIfIndex_Type = DisplayString
_TscRemoteIfIndex_Object = MibScalar
tscRemoteIfIndex = _TscRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 12),
    _TscRemoteIfIndex_Type()
)
tscRemoteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteIfIndex.setStatus("optional")
_TscRemoteChassis_Type = DisplayString
_TscRemoteChassis_Object = MibScalar
tscRemoteChassis = _TscRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 13),
    _TscRemoteChassis_Type()
)
tscRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteChassis.setStatus("optional")
_TscRemoteSlot_Type = DisplayString
_TscRemoteSlot_Object = MibScalar
tscRemoteSlot = _TscRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 14),
    _TscRemoteSlot_Type()
)
tscRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteSlot.setStatus("optional")
_TscRemotePosition_Type = DisplayString
_TscRemotePosition_Object = MibScalar
tscRemotePosition = _TscRemotePosition_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 15),
    _TscRemotePosition_Type()
)
tscRemotePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemotePosition.setStatus("optional")
_TscRemoteDescription_Type = DisplayString
_TscRemoteDescription_Object = MibScalar
tscRemoteDescription = _TscRemoteDescription_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 16),
    _TscRemoteDescription_Type()
)
tscRemoteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteDescription.setStatus("optional")
_TscRemoteRecno_Type = DisplayString
_TscRemoteRecno_Object = MibScalar
tscRemoteRecno = _TscRemoteRecno_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 17),
    _TscRemoteRecno_Type()
)
tscRemoteRecno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteRecno.setStatus("optional")
_TscRemoteOldValue_Type = Integer32
_TscRemoteOldValue_Object = MibScalar
tscRemoteOldValue = _TscRemoteOldValue_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 18),
    _TscRemoteOldValue_Type()
)
tscRemoteOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteOldValue.setStatus("optional")
_TscRemoteTrapOID_Type = DisplayString
_TscRemoteTrapOID_Object = MibScalar
tscRemoteTrapOID = _TscRemoteTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 19),
    _TscRemoteTrapOID_Type()
)
tscRemoteTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTrapOID.setStatus("optional")
_TscRemoteTrapGeneric_Type = DisplayString
_TscRemoteTrapGeneric_Object = MibScalar
tscRemoteTrapGeneric = _TscRemoteTrapGeneric_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 20),
    _TscRemoteTrapGeneric_Type()
)
tscRemoteTrapGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTrapGeneric.setStatus("optional")
_TscRemoteTrapSpecific_Type = DisplayString
_TscRemoteTrapSpecific_Object = MibScalar
tscRemoteTrapSpecific = _TscRemoteTrapSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 21),
    _TscRemoteTrapSpecific_Type()
)
tscRemoteTrapSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTrapSpecific.setStatus("optional")
_TscRemoteTrapTimestamp_Type = DisplayString
_TscRemoteTrapTimestamp_Object = MibScalar
tscRemoteTrapTimestamp = _TscRemoteTrapTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 22),
    _TscRemoteTrapTimestamp_Type()
)
tscRemoteTrapTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTrapTimestamp.setStatus("optional")
_TscRemoteTrapCommunity_Type = DisplayString
_TscRemoteTrapCommunity_Object = MibScalar
tscRemoteTrapCommunity = _TscRemoteTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 23),
    _TscRemoteTrapCommunity_Type()
)
tscRemoteTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTrapCommunity.setStatus("optional")
_TscRemoteTimestamp_Type = DisplayString
_TscRemoteTimestamp_Object = MibScalar
tscRemoteTimestamp = _TscRemoteTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 24),
    _TscRemoteTimestamp_Type()
)
tscRemoteTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteTimestamp.setStatus("optional")
_TscRemoteDomain_Type = DisplayString
_TscRemoteDomain_Object = MibScalar
tscRemoteDomain = _TscRemoteDomain_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 25),
    _TscRemoteDomain_Type()
)
tscRemoteDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscRemoteDomain.setStatus("optional")
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 7)
)
_Portmon_ObjectIdentity = ObjectIdentity
portmon = _Portmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8)
)
_TscPmOldValue_Type = DisplayString
_TscPmOldValue_Object = MibScalar
tscPmOldValue = _TscPmOldValue_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 1),
    _TscPmOldValue_Type()
)
tscPmOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmOldValue.setStatus("optional")
_TscPmValue_Type = DisplayString
_TscPmValue_Object = MibScalar
tscPmValue = _TscPmValue_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 2),
    _TscPmValue_Type()
)
tscPmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmValue.setStatus("optional")
_TscPmIndex_Type = Integer32
_TscPmIndex_Object = MibScalar
tscPmIndex = _TscPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 3),
    _TscPmIndex_Type()
)
tscPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmIndex.setStatus("optional")
_TscPmChassis_Type = Integer32
_TscPmChassis_Object = MibScalar
tscPmChassis = _TscPmChassis_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 4),
    _TscPmChassis_Type()
)
tscPmChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmChassis.setStatus("optional")
_TscPmSlot_Type = Integer32
_TscPmSlot_Object = MibScalar
tscPmSlot = _TscPmSlot_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 5),
    _TscPmSlot_Type()
)
tscPmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmSlot.setStatus("optional")
_TscPmPos_Type = Integer32
_TscPmPos_Object = MibScalar
tscPmPos = _TscPmPos_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 6),
    _TscPmPos_Type()
)
tscPmPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmPos.setStatus("optional")
_TscPmStatus_Type = DisplayString
_TscPmStatus_Object = MibScalar
tscPmStatus = _TscPmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 7),
    _TscPmStatus_Type()
)
tscPmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmStatus.setStatus("optional")
_TscPmName_Type = DisplayString
_TscPmName_Object = MibScalar
tscPmName = _TscPmName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 8),
    _TscPmName_Type()
)
tscPmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmName.setStatus("optional")
_TscPmTime_Type = DisplayString
_TscPmTime_Object = MibScalar
tscPmTime = _TscPmTime_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 9),
    _TscPmTime_Type()
)
tscPmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscPmTime.setStatus("optional")
_Syslogtrap_ObjectIdentity = ObjectIdentity
syslogtrap = _Syslogtrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9)
)
_TscSltLogMessage_Type = DisplayString
_TscSltLogMessage_Object = MibScalar
tscSltLogMessage = _TscSltLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 1),
    _TscSltLogMessage_Type()
)
tscSltLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscSltLogMessage.setStatus("optional")
_TscSltFacility_Type = DisplayString
_TscSltFacility_Object = MibScalar
tscSltFacility = _TscSltFacility_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 2),
    _TscSltFacility_Type()
)
tscSltFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscSltFacility.setStatus("optional")
_TscSltPid_Type = Integer32
_TscSltPid_Object = MibScalar
tscSltPid = _TscSltPid_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 3),
    _TscSltPid_Type()
)
tscSltPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscSltPid.setStatus("optional")
_TscSltHostname_Type = DisplayString
_TscSltHostname_Object = MibScalar
tscSltHostname = _TscSltHostname_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 4),
    _TscSltHostname_Type()
)
tscSltHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscSltHostname.setStatus("optional")
_TscSltMessage_Type = DisplayString
_TscSltMessage_Object = MibScalar
tscSltMessage = _TscSltMessage_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 5),
    _TscSltMessage_Type()
)
tscSltMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscSltMessage.setStatus("optional")
_Atmmon_ObjectIdentity = ObjectIdentity
atmmon = _Atmmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10)
)
_TscAtmmonSourceNode_Type = DisplayString
_TscAtmmonSourceNode_Object = MibScalar
tscAtmmonSourceNode = _TscAtmmonSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 1),
    _TscAtmmonSourceNode_Type()
)
tscAtmmonSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscAtmmonSourceNode.setStatus("optional")
_TscAtmmonIfIndex_Type = Integer32
_TscAtmmonIfIndex_Object = MibScalar
tscAtmmonIfIndex = _TscAtmmonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 2),
    _TscAtmmonIfIndex_Type()
)
tscAtmmonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscAtmmonIfIndex.setStatus("optional")
_TscAtmmonifName_Type = DisplayString
_TscAtmmonifName_Object = MibScalar
tscAtmmonifName = _TscAtmmonifName_Object(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 3),
    _TscAtmmonifName_Type()
)
tscAtmmonifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscAtmmonifName.setStatus("optional")
_Xmon_ObjectIdentity = ObjectIdentity
xmon = _Xmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 12)
)
_Custom_ObjectIdentity = ObjectIdentity
custom = _Custom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 1, 2)
)
_Agents_ObjectIdentity = ObjectIdentity
agents = _Agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2668, 2)
)

# Managed Objects groups


# Notification objects

tscEwSourceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 1)
)
tscEwSourceDown.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"),
        ("TAVVE-MIB", "tscEwDescr"))
)
if mibBuilder.loadTexts:
    tscEwSourceDown.setStatus(
        ""
    )

tscEwInferredDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 2)
)
tscEwInferredDown.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwSourceNode"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwInferredDown.setStatus(
        ""
    )

tscEwSourceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 3)
)
tscEwSourceUp.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwSourceUp.setStatus(
        ""
    )

tscEwInferredUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 4)
)
tscEwInferredUp.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwSourceNode"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwInferredUp.setStatus(
        ""
    )

tscEwNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 5)
)
tscEwNodeDown.setObjects(
      *(("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwNodeDown.setStatus(
        ""
    )

tscEwNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 6)
)
tscEwNodeUp.setObjects(
      *(("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwNodeUp.setStatus(
        ""
    )

tscEwSlaThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 7)
)
tscEwSlaThres.setObjects(
      *(("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwUserThreshold"),
        ("TAVVE-MIB", "tscEwSlaValue"))
)
if mibBuilder.loadTexts:
    tscEwSlaThres.setStatus(
        ""
    )

tscEwRemoteSourceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 11)
)
tscEwRemoteSourceDown.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteSourceDown.setStatus(
        ""
    )

tscEwRemoteInferredDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 12)
)
tscEwRemoteInferredDown.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwSourceNode"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteInferredDown.setStatus(
        ""
    )

tscEwRemoteSourceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 13)
)
tscEwRemoteSourceUp.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwDownTime"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteSourceUp.setStatus(
        ""
    )

tscEwRemoteInferredUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 14)
)
tscEwRemoteInferredUp.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwSourceNode"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwDownTime"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteInferredUp.setStatus(
        ""
    )

tscEwRemoteNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 15)
)
tscEwRemoteNodeDown.setObjects(
      *(("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteNodeDown.setStatus(
        ""
    )

tscEwRemoteNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 16)
)
tscEwRemoteNodeUp.setObjects(
      *(("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscEwRemoteNodeUp.setStatus(
        ""
    )

tscEwTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 91)
)
tscEwTestTrap.setObjects(
      *(("TAVVE-MIB", "tscEwEventTime"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwDescr"))
)
if mibBuilder.loadTexts:
    tscEwTestTrap.setStatus(
        ""
    )

tscEwTestTrapRecv = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 1, 0, 92)
)
tscEwTestTrapRecv.setObjects(
      *(("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwSourceProtocol"),
        ("TAVVE-MIB", "tscEwSourceName"),
        ("TAVVE-MIB", "tscEwSourceAddr"),
        ("TAVVE-MIB", "tscEwEventTime"),
        ("TAVVE-MIB", "tscEwDescr"))
)
if mibBuilder.loadTexts:
    tscEwTestTrapRecv.setStatus(
        ""
    )

tscCtSeverity0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 10)
)
tscCtSeverity0.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity0.setStatus(
        ""
    )

tscCtSeverity1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 11)
)
tscCtSeverity1.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity1.setStatus(
        ""
    )

tscCtSeverity2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 12)
)
tscCtSeverity2.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity2.setStatus(
        ""
    )

tscCtSeverity3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 13)
)
tscCtSeverity3.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity3.setStatus(
        ""
    )

tscCtSeverity4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 14)
)
tscCtSeverity4.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity4.setStatus(
        ""
    )

tscCtSeverity5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 15)
)
tscCtSeverity5.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity5.setStatus(
        ""
    )

tscCtSeverity6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 16)
)
tscCtSeverity6.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity6.setStatus(
        ""
    )

tscCtSeverity7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 17)
)
tscCtSeverity7.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity7.setStatus(
        ""
    )

tscCtSeverity8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 3, 0, 18)
)
tscCtSeverity8.setObjects(
      *(("TAVVE-MIB", "tscCtLogMessage"),
        ("TAVVE-MIB", "tscCtFacility"),
        ("TAVVE-MIB", "tscCtSeverity"),
        ("TAVVE-MIB", "tscCtMnemonic"),
        ("TAVVE-MIB", "tscCtMessage"))
)
if mibBuilder.loadTexts:
    tscCtSeverity8.setStatus(
        ""
    )

wwwmonUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 101)
)
wwwmonUp.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonUp.setStatus(
        ""
    )

wwwmonTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 102)
)
wwwmonTimeout.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonTimeout.setStatus(
        ""
    )

wwwmonRefd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 103)
)
wwwmonRefd.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonRefd.setStatus(
        ""
    )

wwwmonUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 104)
)
wwwmonUnknown.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonUnknown.setStatus(
        ""
    )

wwwmonBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 105)
)
wwwmonBusy.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonBusy.setStatus(
        ""
    )

wwwmonInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 106)
)
wwwmonInfo.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonInfo.setStatus(
        ""
    )

wwwmonRedirect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 107)
)
wwwmonRedirect.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonRedirect.setStatus(
        ""
    )

wwwmonClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 108)
)
wwwmonClient.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonClient.setStatus(
        ""
    )

wwwmonServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 4, 0, 109)
)
wwwmonServer.setObjects(
      *(("TAVVE-MIB", "wwwmonServerName"),
        ("TAVVE-MIB", "wwwmonServerPort"),
        ("TAVVE-MIB", "wwwmonServerURL"),
        ("TAVVE-MIB", "wwwmonServerStatus"))
)
if mibBuilder.loadTexts:
    wwwmonServer.setStatus(
        ""
    )

tscIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 1)
)
tscIfDown.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteSourceProtocol"),
        ("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteIfIndex"))
)
if mibBuilder.loadTexts:
    tscIfDown.setStatus(
        ""
    )

tscIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 2)
)
tscIfUp.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteSourceProtocol"),
        ("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteIfIndex"))
)
if mibBuilder.loadTexts:
    tscIfUp.setStatus(
        ""
    )

tscIfLatThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 3)
)
tscIfLatThreshold.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteThreshold"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscIfLatThreshold.setStatus(
        ""
    )

tscIfLatRearm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 4)
)
tscIfLatRearm.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRearm"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscIfLatRearm.setStatus(
        ""
    )

tscIfUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 5)
)
tscIfUnknown.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteSourceProtocol"),
        ("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteIfIndex"))
)
if mibBuilder.loadTexts:
    tscIfUnknown.setStatus(
        ""
    )

tscNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 6)
)
tscNodeDown.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeDown.setStatus(
        ""
    )

tscNodeMarginal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 7)
)
tscNodeMarginal.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeMarginal.setStatus(
        ""
    )

tscNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 8)
)
tscNodeUp.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeUp.setStatus(
        ""
    )

tscNodeUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 9)
)
tscNodeUnknown.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeUnknown.setStatus(
        ""
    )

tscNewNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 10)
)
tscNewNode.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNewNode.setStatus(
        ""
    )

tscNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 11)
)
tscNameChange.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceNode2"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNameChange.setStatus(
        ""
    )

tscIfDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 12)
)
tscIfDelete.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteSourceProtocol"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscIfDelete.setStatus(
        ""
    )

tscNodeAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 13)
)
tscNodeAdded.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeAdded.setStatus(
        ""
    )

tscInterfaceAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 14)
)
tscInterfaceAdded.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscInterfaceAdded.setStatus(
        ""
    )

tscNodeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 15)
)
tscNodeDeleted.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscNodeDeleted.setStatus(
        ""
    )

tscInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 16)
)
tscInterfaceDeleted.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscInterfaceDeleted.setStatus(
        ""
    )

tscHostnameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 17)
)
tscHostnameChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteOldValue"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscHostnameChanged.setStatus(
        ""
    )

tscSysObjectIDChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 18)
)
tscSysObjectIDChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscSysObjectIDChanged.setStatus(
        ""
    )

tscProcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 21)
)
tscProcFail.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteProcName"))
)
if mibBuilder.loadTexts:
    tscProcFail.setStatus(
        ""
    )

tscProcStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 22)
)
tscProcStop.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteProcName"))
)
if mibBuilder.loadTexts:
    tscProcStop.setStatus(
        ""
    )

tscProcStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 23)
)
tscProcStart.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteProcName"))
)
if mibBuilder.loadTexts:
    tscProcStart.setStatus(
        ""
    )

tscFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 24)
)
tscFsFull.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteFsDevice"),
        ("TAVVE-MIB", "tscRemoteFsName"),
        ("TAVVE-MIB", "tscRemoteValue"))
)
if mibBuilder.loadTexts:
    tscFsFull.setStatus(
        ""
    )

tscVoidWarranty = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 25)
)
tscVoidWarranty.setObjects(
    ("TAVVE-MIB", "tscRemoteName")
)
if mibBuilder.loadTexts:
    tscVoidWarranty.setStatus(
        ""
    )

tscSysNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 26)
)
tscSysNameChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteOldValue"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscSysNameChanged.setStatus(
        ""
    )

tscSysDescrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 27)
)
tscSysDescrChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteOldValue"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscSysDescrChanged.setStatus(
        ""
    )

tscSysLocationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 28)
)
tscSysLocationChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteOldValue"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscSysLocationChanged.setStatus(
        ""
    )

tscSysContactChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 29)
)
tscSysContactChanged.setObjects(
      *(("TAVVE-MIB", "tscRemoteOldValue"),
        ("TAVVE-MIB", "tscRemoteValue"),
        ("TAVVE-MIB", "tscRemoteRecno"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscSysContactChanged.setStatus(
        ""
    )

tscManage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 50)
)
tscManage.setObjects(
    ("TAVVE-MIB", "tscRemoteSourceNode")
)
if mibBuilder.loadTexts:
    tscManage.setStatus(
        ""
    )

tscUnmanage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 51)
)
tscUnmanage.setObjects(
    ("TAVVE-MIB", "tscRemoteSourceNode")
)
if mibBuilder.loadTexts:
    tscUnmanage.setStatus(
        ""
    )

tscIfManage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 52)
)
tscIfManage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteDescription"))
)
if mibBuilder.loadTexts:
    tscIfManage.setStatus(
        ""
    )

tscIfUnmanage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 53)
)
tscIfUnmanage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteDescription"))
)
if mibBuilder.loadTexts:
    tscIfUnmanage.setStatus(
        ""
    )

tscNetManage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 54)
)
tscNetManage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteDescription"))
)
if mibBuilder.loadTexts:
    tscNetManage.setStatus(
        ""
    )

tscNetUnmanage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 55)
)
tscNetUnmanage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteDescription"))
)
if mibBuilder.loadTexts:
    tscNetUnmanage.setStatus(
        ""
    )

tscPortManage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 56)
)
tscPortManage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteChassis"),
        ("TAVVE-MIB", "tscRemoteSlot"),
        ("TAVVE-MIB", "tscRemotePosition"))
)
if mibBuilder.loadTexts:
    tscPortManage.setStatus(
        ""
    )

tscPortUnmanage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 57)
)
tscPortUnmanage.setObjects(
      *(("TAVVE-MIB", "tscRemoteIfIndex"),
        ("TAVVE-MIB", "tscRemoteChassis"),
        ("TAVVE-MIB", "tscRemoteSlot"),
        ("TAVVE-MIB", "tscRemotePosition"))
)
if mibBuilder.loadTexts:
    tscPortUnmanage.setStatus(
        ""
    )

tscFwdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 60)
)
tscFwdTrap.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteSourceAddr"),
        ("TAVVE-MIB", "tscRemoteTrapOID"),
        ("TAVVE-MIB", "tscRemoteTrapGeneric"),
        ("TAVVE-MIB", "tscRemoteTrapSpecific"),
        ("TAVVE-MIB", "tscRemoteTrapTimestamp"),
        ("TAVVE-MIB", "tscRemoteTrapCommunity"),
        ("TAVVE-MIB", "tscRemoteDescription"),
        ("TAVVE-MIB", "tscRemoteValue"))
)
if mibBuilder.loadTexts:
    tscFwdTrap.setStatus(
        ""
    )

tscRedPeerAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 61)
)
tscRedPeerAdd.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteDomain"),
        ("TAVVE-MIB", "tscRemoteTimestamp"))
)
if mibBuilder.loadTexts:
    tscRedPeerAdd.setStatus(
        ""
    )

tscRedPeerRm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 62)
)
tscRedPeerRm.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteDomain"),
        ("TAVVE-MIB", "tscRemoteTimestamp"))
)
if mibBuilder.loadTexts:
    tscRedPeerRm.setStatus(
        ""
    )

tscRedPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 63)
)
tscRedPeerUp.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteDomain"),
        ("TAVVE-MIB", "tscRemoteTimestamp"))
)
if mibBuilder.loadTexts:
    tscRedPeerUp.setStatus(
        ""
    )

tscRedPeerUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 64)
)
tscRedPeerUnavail.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteDomain"),
        ("TAVVE-MIB", "tscRemoteTimestamp"))
)
if mibBuilder.loadTexts:
    tscRedPeerUnavail.setStatus(
        ""
    )

tscRedPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 65)
)
tscRedPeerDown.setObjects(
      *(("TAVVE-MIB", "tscRemoteName"),
        ("TAVVE-MIB", "tscRemoteSourceNode"),
        ("TAVVE-MIB", "tscRemoteDomain"),
        ("TAVVE-MIB", "tscRemoteTimestamp"))
)
if mibBuilder.loadTexts:
    tscRedPeerDown.setStatus(
        ""
    )

tscRemoteNoStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 68)
)
tscRemoteNoStatus.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscRemoteNoStatus.setStatus(
        ""
    )

tscRemoteAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 6, 0, 69)
)
tscRemoteAlive.setObjects(
      *(("TAVVE-MIB", "tscEwFaultAddr"),
        ("TAVVE-MIB", "tscEwFaultName"),
        ("TAVVE-MIB", "tscEwFaultProtocol"),
        ("TAVVE-MIB", "tscEwGroupName"),
        ("TAVVE-MIB", "tscEwReportHost"),
        ("TAVVE-MIB", "tscEwEventTime"))
)
if mibBuilder.loadTexts:
    tscRemoteAlive.setStatus(
        ""
    )

tscPmNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 1)
)
tscPmNameChange.setObjects(
      *(("TAVVE-MIB", "tscPmOldValue"),
        ("TAVVE-MIB", "tscPmValue"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmNameChange.setStatus(
        ""
    )

tscPmTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 2)
)
tscPmTypeChange.setObjects(
      *(("TAVVE-MIB", "tscPmOldValue"),
        ("TAVVE-MIB", "tscPmValue"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmTypeChange.setStatus(
        ""
    )

tscPmSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 3)
)
tscPmSpeedChange.setObjects(
      *(("TAVVE-MIB", "tscPmOldValue"),
        ("TAVVE-MIB", "tscPmValue"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmSpeedChange.setStatus(
        ""
    )

tscPmDuplexChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 4)
)
tscPmDuplexChange.setObjects(
      *(("TAVVE-MIB", "tscPmOldValue"),
        ("TAVVE-MIB", "tscPmValue"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmDuplexChange.setStatus(
        ""
    )

tscPmVlanChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 5)
)
tscPmVlanChange.setObjects(
      *(("TAVVE-MIB", "tscPmOldValue"),
        ("TAVVE-MIB", "tscPmValue"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmVlanChange.setStatus(
        ""
    )

tscPmNewPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 100)
)
tscPmNewPort.setObjects(
      *(("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"))
)
if mibBuilder.loadTexts:
    tscPmNewPort.setStatus(
        ""
    )

tscPmPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 101)
)
tscPmPortFault.setObjects(
      *(("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"),
        ("TAVVE-MIB", "tscPmStatus"),
        ("TAVVE-MIB", "tscPmName"),
        ("TAVVE-MIB", "tscPmTime"))
)
if mibBuilder.loadTexts:
    tscPmPortFault.setStatus(
        ""
    )

tscPmPortRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 102)
)
tscPmPortRestored.setObjects(
      *(("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"),
        ("TAVVE-MIB", "tscPmStatus"),
        ("TAVVE-MIB", "tscPmName"),
        ("TAVVE-MIB", "tscPmTime"))
)
if mibBuilder.loadTexts:
    tscPmPortRestored.setStatus(
        ""
    )

tscPmPortUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 103)
)
tscPmPortUnknown.setObjects(
      *(("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"),
        ("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmStatus"),
        ("TAVVE-MIB", "tscPmName"),
        ("TAVVE-MIB", "tscPmTime"))
)
if mibBuilder.loadTexts:
    tscPmPortUnknown.setStatus(
        ""
    )

tscPmPortDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 8, 0, 104)
)
tscPmPortDeleted.setObjects(
      *(("TAVVE-MIB", "tscPmIndex"),
        ("TAVVE-MIB", "tscPmChassis"),
        ("TAVVE-MIB", "tscPmSlot"),
        ("TAVVE-MIB", "tscPmPos"),
        ("TAVVE-MIB", "tscRemoteName"))
)
if mibBuilder.loadTexts:
    tscPmPortDeleted.setStatus(
        ""
    )

tscSltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 9, 0, 1)
)
tscSltTrap.setObjects(
      *(("TAVVE-MIB", "tscSltLogMessage"),
        ("TAVVE-MIB", "tscSltFacility"),
        ("TAVVE-MIB", "tscSltPid"),
        ("TAVVE-MIB", "tscSltHostname"),
        ("TAVVE-MIB", "tscSltMessage"))
)
if mibBuilder.loadTexts:
    tscSltTrap.setStatus(
        ""
    )

tscAtmIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 0, 101)
)
tscAtmIfDown.setObjects(
      *(("TAVVE-MIB", "tscAtmmonIfIndex"),
        ("TAVVE-MIB", "tscAtmmonSourceNode"),
        ("TAVVE-MIB", "tscAtmmonifName"))
)
if mibBuilder.loadTexts:
    tscAtmIfDown.setStatus(
        ""
    )

tscAtmIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 0, 102)
)
tscAtmIfUp.setObjects(
      *(("TAVVE-MIB", "tscAtmmonIfIndex"),
        ("TAVVE-MIB", "tscAtmmonSourceNode"),
        ("TAVVE-MIB", "tscAtmmonifName"))
)
if mibBuilder.loadTexts:
    tscAtmIfUp.setStatus(
        ""
    )

tscAtmIfUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2668, 1, 1, 10, 0, 103)
)
tscAtmIfUnknown.setObjects(
      *(("TAVVE-MIB", "tscAtmmonIfIndex"),
        ("TAVVE-MIB", "tscAtmmonSourceNode"),
        ("TAVVE-MIB", "tscAtmmonifName"))
)
if mibBuilder.loadTexts:
    tscAtmIfUnknown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAVVE-MIB",
    **{"tavve": tavve,
       "traps": traps,
       "products": products,
       "eventWatch": eventWatch,
       "tscEwSourceDown": tscEwSourceDown,
       "tscEwInferredDown": tscEwInferredDown,
       "tscEwSourceUp": tscEwSourceUp,
       "tscEwInferredUp": tscEwInferredUp,
       "tscEwNodeDown": tscEwNodeDown,
       "tscEwNodeUp": tscEwNodeUp,
       "tscEwSlaThres": tscEwSlaThres,
       "tscEwRemoteSourceDown": tscEwRemoteSourceDown,
       "tscEwRemoteInferredDown": tscEwRemoteInferredDown,
       "tscEwRemoteSourceUp": tscEwRemoteSourceUp,
       "tscEwRemoteInferredUp": tscEwRemoteInferredUp,
       "tscEwRemoteNodeDown": tscEwRemoteNodeDown,
       "tscEwRemoteNodeUp": tscEwRemoteNodeUp,
       "tscEwTestTrap": tscEwTestTrap,
       "tscEwTestTrapRecv": tscEwTestTrapRecv,
       "tscEwSourceNode": tscEwSourceNode,
       "tscEwFaultAddr": tscEwFaultAddr,
       "tscEwFaultTimes": tscEwFaultTimes,
       "tscEwSourceAddr": tscEwSourceAddr,
       "tscEwGroupName": tscEwGroupName,
       "tscEwSourceName": tscEwSourceName,
       "tscEwSourceProtocol": tscEwSourceProtocol,
       "tscEwFaultName": tscEwFaultName,
       "tscEwFaultProtocol": tscEwFaultProtocol,
       "tscEwUserThreshold": tscEwUserThreshold,
       "tscEwSlaValue": tscEwSlaValue,
       "tscEwReportHost": tscEwReportHost,
       "tscEwDownTime": tscEwDownTime,
       "tscEwEventTime": tscEwEventTime,
       "tscEwDescr": tscEwDescr,
       "tcpdmon": tcpdmon,
       "tscTcpSourceNode": tscTcpSourceNode,
       "tscTCPPortName": tscTCPPortName,
       "tscTCPPortNumber": tscTCPPortNumber,
       "tscTCPTime": tscTCPTime,
       "ciscotrap": ciscotrap,
       "tscCtSeverity0": tscCtSeverity0,
       "tscCtSeverity1": tscCtSeverity1,
       "tscCtSeverity2": tscCtSeverity2,
       "tscCtSeverity3": tscCtSeverity3,
       "tscCtSeverity4": tscCtSeverity4,
       "tscCtSeverity5": tscCtSeverity5,
       "tscCtSeverity6": tscCtSeverity6,
       "tscCtSeverity7": tscCtSeverity7,
       "tscCtSeverity8": tscCtSeverity8,
       "tscCtLogMessage": tscCtLogMessage,
       "tscCtFacility": tscCtFacility,
       "tscCtSeverity": tscCtSeverity,
       "tscCtMnemonic": tscCtMnemonic,
       "tscCtMessage": tscCtMessage,
       "wwwmon": wwwmon,
       "wwwmonUp": wwwmonUp,
       "wwwmonTimeout": wwwmonTimeout,
       "wwwmonRefd": wwwmonRefd,
       "wwwmonUnknown": wwwmonUnknown,
       "wwwmonBusy": wwwmonBusy,
       "wwwmonInfo": wwwmonInfo,
       "wwwmonRedirect": wwwmonRedirect,
       "wwwmonClient": wwwmonClient,
       "wwwmonServer": wwwmonServer,
       "wwwmonServerName": wwwmonServerName,
       "wwwmonServerPort": wwwmonServerPort,
       "wwwmonServerURL": wwwmonServerURL,
       "wwwmonServerStatus": wwwmonServerStatus,
       "agentmon": agentmon,
       "remote": remote,
       "tscIfDown": tscIfDown,
       "tscIfUp": tscIfUp,
       "tscIfLatThreshold": tscIfLatThreshold,
       "tscIfLatRearm": tscIfLatRearm,
       "tscIfUnknown": tscIfUnknown,
       "tscNodeDown": tscNodeDown,
       "tscNodeMarginal": tscNodeMarginal,
       "tscNodeUp": tscNodeUp,
       "tscNodeUnknown": tscNodeUnknown,
       "tscNewNode": tscNewNode,
       "tscNameChange": tscNameChange,
       "tscIfDelete": tscIfDelete,
       "tscNodeAdded": tscNodeAdded,
       "tscInterfaceAdded": tscInterfaceAdded,
       "tscNodeDeleted": tscNodeDeleted,
       "tscInterfaceDeleted": tscInterfaceDeleted,
       "tscHostnameChanged": tscHostnameChanged,
       "tscSysObjectIDChanged": tscSysObjectIDChanged,
       "tscProcFail": tscProcFail,
       "tscProcStop": tscProcStop,
       "tscProcStart": tscProcStart,
       "tscFsFull": tscFsFull,
       "tscVoidWarranty": tscVoidWarranty,
       "tscSysNameChanged": tscSysNameChanged,
       "tscSysDescrChanged": tscSysDescrChanged,
       "tscSysLocationChanged": tscSysLocationChanged,
       "tscSysContactChanged": tscSysContactChanged,
       "tscManage": tscManage,
       "tscUnmanage": tscUnmanage,
       "tscIfManage": tscIfManage,
       "tscIfUnmanage": tscIfUnmanage,
       "tscNetManage": tscNetManage,
       "tscNetUnmanage": tscNetUnmanage,
       "tscPortManage": tscPortManage,
       "tscPortUnmanage": tscPortUnmanage,
       "tscFwdTrap": tscFwdTrap,
       "tscRedPeerAdd": tscRedPeerAdd,
       "tscRedPeerRm": tscRedPeerRm,
       "tscRedPeerUp": tscRedPeerUp,
       "tscRedPeerUnavail": tscRedPeerUnavail,
       "tscRedPeerDown": tscRedPeerDown,
       "tscRemoteNoStatus": tscRemoteNoStatus,
       "tscRemoteAlive": tscRemoteAlive,
       "tscRemoteSourceNode": tscRemoteSourceNode,
       "tscRemoteValue": tscRemoteValue,
       "tscRemoteThreshold": tscRemoteThreshold,
       "tscRemoteRearm": tscRemoteRearm,
       "tscRemoteSourceAddr": tscRemoteSourceAddr,
       "tscRemoteName": tscRemoteName,
       "tscRemoteSourceNode2": tscRemoteSourceNode2,
       "tscRemoteSourceProtocol": tscRemoteSourceProtocol,
       "tscRemoteProcName": tscRemoteProcName,
       "tscRemoteFsDevice": tscRemoteFsDevice,
       "tscRemoteFsName": tscRemoteFsName,
       "tscRemoteIfIndex": tscRemoteIfIndex,
       "tscRemoteChassis": tscRemoteChassis,
       "tscRemoteSlot": tscRemoteSlot,
       "tscRemotePosition": tscRemotePosition,
       "tscRemoteDescription": tscRemoteDescription,
       "tscRemoteRecno": tscRemoteRecno,
       "tscRemoteOldValue": tscRemoteOldValue,
       "tscRemoteTrapOID": tscRemoteTrapOID,
       "tscRemoteTrapGeneric": tscRemoteTrapGeneric,
       "tscRemoteTrapSpecific": tscRemoteTrapSpecific,
       "tscRemoteTrapTimestamp": tscRemoteTrapTimestamp,
       "tscRemoteTrapCommunity": tscRemoteTrapCommunity,
       "tscRemoteTimestamp": tscRemoteTimestamp,
       "tscRemoteDomain": tscRemoteDomain,
       "global": _pysmi_global,
       "portmon": portmon,
       "tscPmNameChange": tscPmNameChange,
       "tscPmTypeChange": tscPmTypeChange,
       "tscPmSpeedChange": tscPmSpeedChange,
       "tscPmDuplexChange": tscPmDuplexChange,
       "tscPmVlanChange": tscPmVlanChange,
       "tscPmNewPort": tscPmNewPort,
       "tscPmPortFault": tscPmPortFault,
       "tscPmPortRestored": tscPmPortRestored,
       "tscPmPortUnknown": tscPmPortUnknown,
       "tscPmPortDeleted": tscPmPortDeleted,
       "tscPmOldValue": tscPmOldValue,
       "tscPmValue": tscPmValue,
       "tscPmIndex": tscPmIndex,
       "tscPmChassis": tscPmChassis,
       "tscPmSlot": tscPmSlot,
       "tscPmPos": tscPmPos,
       "tscPmStatus": tscPmStatus,
       "tscPmName": tscPmName,
       "tscPmTime": tscPmTime,
       "syslogtrap": syslogtrap,
       "tscSltTrap": tscSltTrap,
       "tscSltLogMessage": tscSltLogMessage,
       "tscSltFacility": tscSltFacility,
       "tscSltPid": tscSltPid,
       "tscSltHostname": tscSltHostname,
       "tscSltMessage": tscSltMessage,
       "atmmon": atmmon,
       "tscAtmIfDown": tscAtmIfDown,
       "tscAtmIfUp": tscAtmIfUp,
       "tscAtmIfUnknown": tscAtmIfUnknown,
       "tscAtmmonSourceNode": tscAtmmonSourceNode,
       "tscAtmmonIfIndex": tscAtmmonIfIndex,
       "tscAtmmonifName": tscAtmmonifName,
       "xmon": xmon,
       "custom": custom,
       "agents": agents}
)
