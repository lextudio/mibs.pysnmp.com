# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DCX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-DCX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:14 2024
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

(CucsAdaptorLinkState,
 CucsDcxAdminState,
 CucsDcxNsAllocStatus,
 CucsDcxOperState,
 CucsDcxProtState,
 CucsDcxState,
 CucsDcxVIfProtRole,
 CucsDpsecForgedTransmit,
 CucsFabricTrafficDirection,
 CucsFsmLifecycle,
 CucsNetworkConnectionType,
 CucsNetworkLocale,
 CucsNetworkPortRole,
 CucsNetworkPortType,
 CucsNetworkSide,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsNwctrlAdminState,
 CucsNwctrlLinkFailAction,
 CucsNwctrlLldpAdminStateBitmask,
 CucsNwctrlRegistrationMode,
 CucsQosHostControl,
 CucsVnicInstantiation) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAdaptorLinkState",
    "CucsDcxAdminState",
    "CucsDcxNsAllocStatus",
    "CucsDcxOperState",
    "CucsDcxProtState",
    "CucsDcxState",
    "CucsDcxVIfProtRole",
    "CucsDpsecForgedTransmit",
    "CucsFabricTrafficDirection",
    "CucsFsmLifecycle",
    "CucsNetworkConnectionType",
    "CucsNetworkLocale",
    "CucsNetworkPortRole",
    "CucsNetworkPortType",
    "CucsNetworkSide",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
    "CucsNwctrlAdminState",
    "CucsNwctrlLinkFailAction",
    "CucsNwctrlLldpAdminStateBitmask",
    "CucsNwctrlRegistrationMode",
    "CucsQosHostControl",
    "CucsVnicInstantiation")

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

cucsDcxObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDcxNsTable_Object = MibTable
cucsDcxNsTable = _CucsDcxNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cucsDcxNsTable.setStatus("current")
_CucsDcxNsEntry_Object = MibTableRow
cucsDcxNsEntry = _CucsDcxNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1)
)
cucsDcxNsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxNsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxNsEntry.setStatus("current")
_CucsDcxNsInstanceId_Type = CucsManagedObjectId
_CucsDcxNsInstanceId_Object = MibTableColumn
cucsDcxNsInstanceId = _CucsDcxNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 1),
    _CucsDcxNsInstanceId_Type()
)
cucsDcxNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxNsInstanceId.setStatus("current")
_CucsDcxNsDn_Type = CucsManagedObjectDn
_CucsDcxNsDn_Object = MibTableColumn
cucsDcxNsDn = _CucsDcxNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 2),
    _CucsDcxNsDn_Type()
)
cucsDcxNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsDn.setStatus("current")
_CucsDcxNsRn_Type = SnmpAdminString
_CucsDcxNsRn_Object = MibTableColumn
cucsDcxNsRn = _CucsDcxNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 3),
    _CucsDcxNsRn_Type()
)
cucsDcxNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsRn.setStatus("current")
_CucsDcxNsAllocStatus_Type = CucsDcxNsAllocStatus
_CucsDcxNsAllocStatus_Object = MibTableColumn
cucsDcxNsAllocStatus = _CucsDcxNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 4),
    _CucsDcxNsAllocStatus_Type()
)
cucsDcxNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsAllocStatus.setStatus("current")
_CucsDcxNsSide_Type = CucsNetworkSide
_CucsDcxNsSide_Object = MibTableColumn
cucsDcxNsSide = _CucsDcxNsSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 5),
    _CucsDcxNsSide_Type()
)
cucsDcxNsSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsSide.setStatus("current")
_CucsDcxNsSize_Type = Gauge32
_CucsDcxNsSize_Object = MibTableColumn
cucsDcxNsSize = _CucsDcxNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 6),
    _CucsDcxNsSize_Type()
)
cucsDcxNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsSize.setStatus("current")
_CucsDcxNsSwitchId_Type = CucsNetworkSwitchId
_CucsDcxNsSwitchId_Object = MibTableColumn
cucsDcxNsSwitchId = _CucsDcxNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 7),
    _CucsDcxNsSwitchId_Type()
)
cucsDcxNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsSwitchId.setStatus("current")
_CucsDcxNsUsed_Type = Gauge32
_CucsDcxNsUsed_Object = MibTableColumn
cucsDcxNsUsed = _CucsDcxNsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 8),
    _CucsDcxNsUsed_Type()
)
cucsDcxNsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxNsUsed.setStatus("current")
_CucsDcxUniverseTable_Object = MibTable
cucsDcxUniverseTable = _CucsDcxUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cucsDcxUniverseTable.setStatus("current")
_CucsDcxUniverseEntry_Object = MibTableRow
cucsDcxUniverseEntry = _CucsDcxUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1)
)
cucsDcxUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxUniverseEntry.setStatus("current")
_CucsDcxUniverseInstanceId_Type = CucsManagedObjectId
_CucsDcxUniverseInstanceId_Object = MibTableColumn
cucsDcxUniverseInstanceId = _CucsDcxUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 1),
    _CucsDcxUniverseInstanceId_Type()
)
cucsDcxUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxUniverseInstanceId.setStatus("current")
_CucsDcxUniverseDn_Type = CucsManagedObjectDn
_CucsDcxUniverseDn_Object = MibTableColumn
cucsDcxUniverseDn = _CucsDcxUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 2),
    _CucsDcxUniverseDn_Type()
)
cucsDcxUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxUniverseDn.setStatus("current")
_CucsDcxUniverseRn_Type = SnmpAdminString
_CucsDcxUniverseRn_Object = MibTableColumn
cucsDcxUniverseRn = _CucsDcxUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 3),
    _CucsDcxUniverseRn_Type()
)
cucsDcxUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxUniverseRn.setStatus("current")
_CucsDcxVIfTable_Object = MibTable
cucsDcxVIfTable = _CucsDcxVIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3)
)
if mibBuilder.loadTexts:
    cucsDcxVIfTable.setStatus("current")
_CucsDcxVIfEntry_Object = MibTableRow
cucsDcxVIfEntry = _CucsDcxVIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1)
)
cucsDcxVIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxVIfEntry.setStatus("current")
_CucsDcxVIfInstanceId_Type = CucsManagedObjectId
_CucsDcxVIfInstanceId_Object = MibTableColumn
cucsDcxVIfInstanceId = _CucsDcxVIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 1),
    _CucsDcxVIfInstanceId_Type()
)
cucsDcxVIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxVIfInstanceId.setStatus("current")
_CucsDcxVIfDn_Type = CucsManagedObjectDn
_CucsDcxVIfDn_Object = MibTableColumn
cucsDcxVIfDn = _CucsDcxVIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 2),
    _CucsDcxVIfDn_Type()
)
cucsDcxVIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfDn.setStatus("current")
_CucsDcxVIfRn_Type = SnmpAdminString
_CucsDcxVIfRn_Object = MibTableColumn
cucsDcxVIfRn = _CucsDcxVIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 3),
    _CucsDcxVIfRn_Type()
)
cucsDcxVIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfRn.setStatus("current")
_CucsDcxVIfAdminState_Type = CucsDcxAdminState
_CucsDcxVIfAdminState_Object = MibTableColumn
cucsDcxVIfAdminState = _CucsDcxVIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 4),
    _CucsDcxVIfAdminState_Type()
)
cucsDcxVIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfAdminState.setStatus("current")
_CucsDcxVIfCookie_Type = Unsigned64
_CucsDcxVIfCookie_Object = MibTableColumn
cucsDcxVIfCookie = _CucsDcxVIfCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 5),
    _CucsDcxVIfCookie_Type()
)
cucsDcxVIfCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfCookie.setStatus("current")
_CucsDcxVIfEpDn_Type = SnmpAdminString
_CucsDcxVIfEpDn_Object = MibTableColumn
cucsDcxVIfEpDn = _CucsDcxVIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 6),
    _CucsDcxVIfEpDn_Type()
)
cucsDcxVIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfEpDn.setStatus("current")
_CucsDcxVIfId_Type = Gauge32
_CucsDcxVIfId_Object = MibTableColumn
cucsDcxVIfId = _CucsDcxVIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 7),
    _CucsDcxVIfId_Type()
)
cucsDcxVIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfId.setStatus("current")
_CucsDcxVIfIfRole_Type = CucsNetworkPortRole
_CucsDcxVIfIfRole_Object = MibTableColumn
cucsDcxVIfIfRole = _CucsDcxVIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 8),
    _CucsDcxVIfIfRole_Type()
)
cucsDcxVIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfIfRole.setStatus("current")
_CucsDcxVIfIfType_Type = CucsNetworkPortType
_CucsDcxVIfIfType_Object = MibTableColumn
cucsDcxVIfIfType = _CucsDcxVIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 9),
    _CucsDcxVIfIfType_Type()
)
cucsDcxVIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfIfType.setStatus("current")
_CucsDcxVIfInstType_Type = CucsVnicInstantiation
_CucsDcxVIfInstType_Object = MibTableColumn
cucsDcxVIfInstType = _CucsDcxVIfInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 10),
    _CucsDcxVIfInstType_Type()
)
cucsDcxVIfInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfInstType.setStatus("current")
_CucsDcxVIfLc_Type = CucsFsmLifecycle
_CucsDcxVIfLc_Object = MibTableColumn
cucsDcxVIfLc = _CucsDcxVIfLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 11),
    _CucsDcxVIfLc_Type()
)
cucsDcxVIfLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfLc.setStatus("current")
_CucsDcxVIfLinkState_Type = CucsAdaptorLinkState
_CucsDcxVIfLinkState_Object = MibTableColumn
cucsDcxVIfLinkState = _CucsDcxVIfLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 12),
    _CucsDcxVIfLinkState_Type()
)
cucsDcxVIfLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfLinkState.setStatus("current")
_CucsDcxVIfLocale_Type = CucsNetworkLocale
_CucsDcxVIfLocale_Object = MibTableColumn
cucsDcxVIfLocale = _CucsDcxVIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 13),
    _CucsDcxVIfLocale_Type()
)
cucsDcxVIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfLocale.setStatus("current")
_CucsDcxVIfName_Type = SnmpAdminString
_CucsDcxVIfName_Object = MibTableColumn
cucsDcxVIfName = _CucsDcxVIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 14),
    _CucsDcxVIfName_Type()
)
cucsDcxVIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfName.setStatus("current")
_CucsDcxVIfOperState_Type = CucsDcxOperState
_CucsDcxVIfOperState_Object = MibTableColumn
cucsDcxVIfOperState = _CucsDcxVIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 15),
    _CucsDcxVIfOperState_Type()
)
cucsDcxVIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfOperState.setStatus("current")
_CucsDcxVIfPeerDn_Type = SnmpAdminString
_CucsDcxVIfPeerDn_Object = MibTableColumn
cucsDcxVIfPeerDn = _CucsDcxVIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 16),
    _CucsDcxVIfPeerDn_Type()
)
cucsDcxVIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfPeerDn.setStatus("current")
_CucsDcxVIfProtPeerId_Type = Gauge32
_CucsDcxVIfProtPeerId_Object = MibTableColumn
cucsDcxVIfProtPeerId = _CucsDcxVIfProtPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 17),
    _CucsDcxVIfProtPeerId_Type()
)
cucsDcxVIfProtPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfProtPeerId.setStatus("current")
_CucsDcxVIfProtRole_Type = CucsDcxVIfProtRole
_CucsDcxVIfProtRole_Object = MibTableColumn
cucsDcxVIfProtRole = _CucsDcxVIfProtRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 18),
    _CucsDcxVIfProtRole_Type()
)
cucsDcxVIfProtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfProtRole.setStatus("current")
_CucsDcxVIfProtState_Type = CucsDcxProtState
_CucsDcxVIfProtState_Object = MibTableColumn
cucsDcxVIfProtState = _CucsDcxVIfProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 19),
    _CucsDcxVIfProtState_Type()
)
cucsDcxVIfProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfProtState.setStatus("current")
_CucsDcxVIfQosControl_Type = CucsQosHostControl
_CucsDcxVIfQosControl_Object = MibTableColumn
cucsDcxVIfQosControl = _CucsDcxVIfQosControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 20),
    _CucsDcxVIfQosControl_Type()
)
cucsDcxVIfQosControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfQosControl.setStatus("current")
_CucsDcxVIfState_Type = CucsDcxState
_CucsDcxVIfState_Object = MibTableColumn
cucsDcxVIfState = _CucsDcxVIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 21),
    _CucsDcxVIfState_Type()
)
cucsDcxVIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfState.setStatus("current")
_CucsDcxVIfSwitchId_Type = CucsNetworkSwitchId
_CucsDcxVIfSwitchId_Object = MibTableColumn
cucsDcxVIfSwitchId = _CucsDcxVIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 22),
    _CucsDcxVIfSwitchId_Type()
)
cucsDcxVIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfSwitchId.setStatus("current")
_CucsDcxVIfTag_Type = Gauge32
_CucsDcxVIfTag_Object = MibTableColumn
cucsDcxVIfTag = _CucsDcxVIfTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 23),
    _CucsDcxVIfTag_Type()
)
cucsDcxVIfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfTag.setStatus("current")
_CucsDcxVIfTransport_Type = CucsNetworkTransport
_CucsDcxVIfTransport_Object = MibTableColumn
cucsDcxVIfTransport = _CucsDcxVIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 24),
    _CucsDcxVIfTransport_Type()
)
cucsDcxVIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfTransport.setStatus("current")
_CucsDcxVIfType_Type = CucsNetworkConnectionType
_CucsDcxVIfType_Object = MibTableColumn
cucsDcxVIfType = _CucsDcxVIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 25),
    _CucsDcxVIfType_Type()
)
cucsDcxVIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVIfType.setStatus("current")
_CucsDcxVcTable_Object = MibTable
cucsDcxVcTable = _CucsDcxVcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4)
)
if mibBuilder.loadTexts:
    cucsDcxVcTable.setStatus("current")
_CucsDcxVcEntry_Object = MibTableRow
cucsDcxVcEntry = _CucsDcxVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1)
)
cucsDcxVcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxVcEntry.setStatus("current")
_CucsDcxVcInstanceId_Type = CucsManagedObjectId
_CucsDcxVcInstanceId_Object = MibTableColumn
cucsDcxVcInstanceId = _CucsDcxVcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 1),
    _CucsDcxVcInstanceId_Type()
)
cucsDcxVcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxVcInstanceId.setStatus("current")
_CucsDcxVcDn_Type = CucsManagedObjectDn
_CucsDcxVcDn_Object = MibTableColumn
cucsDcxVcDn = _CucsDcxVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 2),
    _CucsDcxVcDn_Type()
)
cucsDcxVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcDn.setStatus("current")
_CucsDcxVcRn_Type = SnmpAdminString
_CucsDcxVcRn_Object = MibTableColumn
cucsDcxVcRn = _CucsDcxVcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 3),
    _CucsDcxVcRn_Type()
)
cucsDcxVcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcRn.setStatus("current")
_CucsDcxVcAdminState_Type = CucsDcxAdminState
_CucsDcxVcAdminState_Object = MibTableColumn
cucsDcxVcAdminState = _CucsDcxVcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 4),
    _CucsDcxVcAdminState_Type()
)
cucsDcxVcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcAdminState.setStatus("current")
_CucsDcxVcBorderPortId_Type = Gauge32
_CucsDcxVcBorderPortId_Object = MibTableColumn
cucsDcxVcBorderPortId = _CucsDcxVcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 5),
    _CucsDcxVcBorderPortId_Type()
)
cucsDcxVcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcBorderPortId.setStatus("current")
_CucsDcxVcBorderSlotId_Type = Gauge32
_CucsDcxVcBorderSlotId_Object = MibTableColumn
cucsDcxVcBorderSlotId = _CucsDcxVcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 6),
    _CucsDcxVcBorderSlotId_Type()
)
cucsDcxVcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcBorderSlotId.setStatus("current")
_CucsDcxVcCdp_Type = CucsNwctrlAdminState
_CucsDcxVcCdp_Object = MibTableColumn
cucsDcxVcCdp = _CucsDcxVcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 8),
    _CucsDcxVcCdp_Type()
)
cucsDcxVcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcCdp.setStatus("current")
_CucsDcxVcCookie_Type = Unsigned64
_CucsDcxVcCookie_Object = MibTableColumn
cucsDcxVcCookie = _CucsDcxVcCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 9),
    _CucsDcxVcCookie_Type()
)
cucsDcxVcCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcCookie.setStatus("current")
_CucsDcxVcCos_Type = Gauge32
_CucsDcxVcCos_Object = MibTableColumn
cucsDcxVcCos = _CucsDcxVcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 10),
    _CucsDcxVcCos_Type()
)
cucsDcxVcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcCos.setStatus("current")
_CucsDcxVcDerivedFromId_Type = Gauge32
_CucsDcxVcDerivedFromId_Object = MibTableColumn
cucsDcxVcDerivedFromId = _CucsDcxVcDerivedFromId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 11),
    _CucsDcxVcDerivedFromId_Type()
)
cucsDcxVcDerivedFromId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcDerivedFromId.setStatus("current")
_CucsDcxVcEncap_Type = Gauge32
_CucsDcxVcEncap_Object = MibTableColumn
cucsDcxVcEncap = _CucsDcxVcEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 12),
    _CucsDcxVcEncap_Type()
)
cucsDcxVcEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcEncap.setStatus("current")
_CucsDcxVcFcoeId_Type = Gauge32
_CucsDcxVcFcoeId_Object = MibTableColumn
cucsDcxVcFcoeId = _CucsDcxVcFcoeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 13),
    _CucsDcxVcFcoeId_Type()
)
cucsDcxVcFcoeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcFcoeId.setStatus("current")
_CucsDcxVcFltAggr_Type = Unsigned64
_CucsDcxVcFltAggr_Object = MibTableColumn
cucsDcxVcFltAggr = _CucsDcxVcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 14),
    _CucsDcxVcFltAggr_Type()
)
cucsDcxVcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcFltAggr.setStatus("current")
_CucsDcxVcForgeMac_Type = CucsDpsecForgedTransmit
_CucsDcxVcForgeMac_Object = MibTableColumn
cucsDcxVcForgeMac = _CucsDcxVcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 15),
    _CucsDcxVcForgeMac_Type()
)
cucsDcxVcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcForgeMac.setStatus("current")
_CucsDcxVcId_Type = Gauge32
_CucsDcxVcId_Object = MibTableColumn
cucsDcxVcId = _CucsDcxVcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 16),
    _CucsDcxVcId_Type()
)
cucsDcxVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcId.setStatus("current")
_CucsDcxVcInstType_Type = CucsVnicInstantiation
_CucsDcxVcInstType_Object = MibTableColumn
cucsDcxVcInstType = _CucsDcxVcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 17),
    _CucsDcxVcInstType_Type()
)
cucsDcxVcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcInstType.setStatus("current")
_CucsDcxVcLc_Type = CucsFsmLifecycle
_CucsDcxVcLc_Object = MibTableColumn
cucsDcxVcLc = _CucsDcxVcLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 18),
    _CucsDcxVcLc_Type()
)
cucsDcxVcLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcLc.setStatus("current")
_CucsDcxVcLinkState_Type = CucsAdaptorLinkState
_CucsDcxVcLinkState_Object = MibTableColumn
cucsDcxVcLinkState = _CucsDcxVcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 19),
    _CucsDcxVcLinkState_Type()
)
cucsDcxVcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcLinkState.setStatus("current")
_CucsDcxVcLocale_Type = CucsNetworkLocale
_CucsDcxVcLocale_Object = MibTableColumn
cucsDcxVcLocale = _CucsDcxVcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 20),
    _CucsDcxVcLocale_Type()
)
cucsDcxVcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcLocale.setStatus("current")
_CucsDcxVcMonTrafDir_Type = CucsFabricTrafficDirection
_CucsDcxVcMonTrafDir_Object = MibTableColumn
cucsDcxVcMonTrafDir = _CucsDcxVcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 21),
    _CucsDcxVcMonTrafDir_Type()
)
cucsDcxVcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcMonTrafDir.setStatus("current")
_CucsDcxVcName_Type = SnmpAdminString
_CucsDcxVcName_Object = MibTableColumn
cucsDcxVcName = _CucsDcxVcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 22),
    _CucsDcxVcName_Type()
)
cucsDcxVcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcName.setStatus("current")
_CucsDcxVcOperBorderPortId_Type = Gauge32
_CucsDcxVcOperBorderPortId_Object = MibTableColumn
cucsDcxVcOperBorderPortId = _CucsDcxVcOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 23),
    _CucsDcxVcOperBorderPortId_Type()
)
cucsDcxVcOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcOperBorderPortId.setStatus("current")
_CucsDcxVcOperBorderSlotId_Type = Gauge32
_CucsDcxVcOperBorderSlotId_Object = MibTableColumn
cucsDcxVcOperBorderSlotId = _CucsDcxVcOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 24),
    _CucsDcxVcOperBorderSlotId_Type()
)
cucsDcxVcOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcOperBorderSlotId.setStatus("current")
_CucsDcxVcOperState_Type = CucsDcxOperState
_CucsDcxVcOperState_Object = MibTableColumn
cucsDcxVcOperState = _CucsDcxVcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 25),
    _CucsDcxVcOperState_Type()
)
cucsDcxVcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcOperState.setStatus("current")
_CucsDcxVcProtState_Type = CucsDcxProtState
_CucsDcxVcProtState_Object = MibTableColumn
cucsDcxVcProtState = _CucsDcxVcProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 26),
    _CucsDcxVcProtState_Type()
)
cucsDcxVcProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcProtState.setStatus("current")
_CucsDcxVcQosPolicyId_Type = SnmpAdminString
_CucsDcxVcQosPolicyId_Object = MibTableColumn
cucsDcxVcQosPolicyId = _CucsDcxVcQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 27),
    _CucsDcxVcQosPolicyId_Type()
)
cucsDcxVcQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcQosPolicyId.setStatus("current")
_CucsDcxVcRole_Type = CucsNetworkPortRole
_CucsDcxVcRole_Object = MibTableColumn
cucsDcxVcRole = _CucsDcxVcRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 29),
    _CucsDcxVcRole_Type()
)
cucsDcxVcRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcRole.setStatus("current")
_CucsDcxVcState_Type = CucsDcxState
_CucsDcxVcState_Object = MibTableColumn
cucsDcxVcState = _CucsDcxVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 30),
    _CucsDcxVcState_Type()
)
cucsDcxVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcState.setStatus("current")
_CucsDcxVcStateQual_Type = SnmpAdminString
_CucsDcxVcStateQual_Object = MibTableColumn
cucsDcxVcStateQual = _CucsDcxVcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 31),
    _CucsDcxVcStateQual_Type()
)
cucsDcxVcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcStateQual.setStatus("current")
_CucsDcxVcSwitchId_Type = CucsNetworkSwitchId
_CucsDcxVcSwitchId_Object = MibTableColumn
cucsDcxVcSwitchId = _CucsDcxVcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 32),
    _CucsDcxVcSwitchId_Type()
)
cucsDcxVcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcSwitchId.setStatus("current")
_CucsDcxVcTag_Type = Gauge32
_CucsDcxVcTag_Object = MibTableColumn
cucsDcxVcTag = _CucsDcxVcTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 33),
    _CucsDcxVcTag_Type()
)
cucsDcxVcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcTag.setStatus("current")
_CucsDcxVcTransport_Type = CucsNetworkTransport
_CucsDcxVcTransport_Object = MibTableColumn
cucsDcxVcTransport = _CucsDcxVcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 34),
    _CucsDcxVcTransport_Type()
)
cucsDcxVcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcTransport.setStatus("current")
_CucsDcxVcType_Type = CucsNetworkConnectionType
_CucsDcxVcType_Object = MibTableColumn
cucsDcxVcType = _CucsDcxVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 35),
    _CucsDcxVcType_Type()
)
cucsDcxVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcType.setStatus("current")
_CucsDcxVcUplinkFailAction_Type = CucsNwctrlLinkFailAction
_CucsDcxVcUplinkFailAction_Object = MibTableColumn
cucsDcxVcUplinkFailAction = _CucsDcxVcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 36),
    _CucsDcxVcUplinkFailAction_Type()
)
cucsDcxVcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcUplinkFailAction.setStatus("current")
_CucsDcxVcVnic_Type = SnmpAdminString
_CucsDcxVcVnic_Object = MibTableColumn
cucsDcxVcVnic = _CucsDcxVcVnic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 37),
    _CucsDcxVcVnic_Type()
)
cucsDcxVcVnic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcVnic.setStatus("current")
_CucsDcxVcPeerId_Type = Gauge32
_CucsDcxVcPeerId_Object = MibTableColumn
cucsDcxVcPeerId = _CucsDcxVcPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 38),
    _CucsDcxVcPeerId_Type()
)
cucsDcxVcPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcPeerId.setStatus("current")
_CucsDcxVcQosPolicyDn_Type = SnmpAdminString
_CucsDcxVcQosPolicyDn_Object = MibTableColumn
cucsDcxVcQosPolicyDn = _CucsDcxVcQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 39),
    _CucsDcxVcQosPolicyDn_Type()
)
cucsDcxVcQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcQosPolicyDn.setStatus("current")
_CucsDcxVcMacRegisterMode_Type = CucsNwctrlRegistrationMode
_CucsDcxVcMacRegisterMode_Object = MibTableColumn
cucsDcxVcMacRegisterMode = _CucsDcxVcMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 40),
    _CucsDcxVcMacRegisterMode_Type()
)
cucsDcxVcMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcMacRegisterMode.setStatus("current")
_CucsDcxVcBorderVfcId_Type = Gauge32
_CucsDcxVcBorderVfcId_Object = MibTableColumn
cucsDcxVcBorderVfcId = _CucsDcxVcBorderVfcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 41),
    _CucsDcxVcBorderVfcId_Type()
)
cucsDcxVcBorderVfcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcBorderVfcId.setStatus("current")
_CucsDcxVcLldp_Type = CucsNwctrlLldpAdminStateBitmask
_CucsDcxVcLldp_Object = MibTableColumn
cucsDcxVcLldp = _CucsDcxVcLldp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 42),
    _CucsDcxVcLldp_Type()
)
cucsDcxVcLldp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcLldp.setStatus("current")
_CucsDcxVcBorderAggrPortId_Type = Gauge32
_CucsDcxVcBorderAggrPortId_Object = MibTableColumn
cucsDcxVcBorderAggrPortId = _CucsDcxVcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 43),
    _CucsDcxVcBorderAggrPortId_Type()
)
cucsDcxVcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcBorderAggrPortId.setStatus("current")
_CucsDcxVcOperBorderAggrPortId_Type = Gauge32
_CucsDcxVcOperBorderAggrPortId_Object = MibTableColumn
cucsDcxVcOperBorderAggrPortId = _CucsDcxVcOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 44),
    _CucsDcxVcOperBorderAggrPortId_Type()
)
cucsDcxVcOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVcOperBorderAggrPortId.setStatus("current")
_CucsDcxVifEpTable_Object = MibTable
cucsDcxVifEpTable = _CucsDcxVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5)
)
if mibBuilder.loadTexts:
    cucsDcxVifEpTable.setStatus("current")
_CucsDcxVifEpEntry_Object = MibTableRow
cucsDcxVifEpEntry = _CucsDcxVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1)
)
cucsDcxVifEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxVifEpEntry.setStatus("current")
_CucsDcxVifEpInstanceId_Type = CucsManagedObjectId
_CucsDcxVifEpInstanceId_Object = MibTableColumn
cucsDcxVifEpInstanceId = _CucsDcxVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 1),
    _CucsDcxVifEpInstanceId_Type()
)
cucsDcxVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxVifEpInstanceId.setStatus("current")
_CucsDcxVifEpDn_Type = CucsManagedObjectDn
_CucsDcxVifEpDn_Object = MibTableColumn
cucsDcxVifEpDn = _CucsDcxVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 2),
    _CucsDcxVifEpDn_Type()
)
cucsDcxVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVifEpDn.setStatus("current")
_CucsDcxVifEpRn_Type = SnmpAdminString
_CucsDcxVifEpRn_Object = MibTableColumn
cucsDcxVifEpRn = _CucsDcxVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 3),
    _CucsDcxVifEpRn_Type()
)
cucsDcxVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVifEpRn.setStatus("current")
_CucsDcxVifEpId_Type = Gauge32
_CucsDcxVifEpId_Object = MibTableColumn
cucsDcxVifEpId = _CucsDcxVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 4),
    _CucsDcxVifEpId_Type()
)
cucsDcxVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxVifEpId.setStatus("current")
_CucsDcxFcoeVifEpTable_Object = MibTable
cucsDcxFcoeVifEpTable = _CucsDcxFcoeVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6)
)
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpTable.setStatus("current")
_CucsDcxFcoeVifEpEntry_Object = MibTableRow
cucsDcxFcoeVifEpEntry = _CucsDcxFcoeVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1)
)
cucsDcxFcoeVifEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxFcoeVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpEntry.setStatus("current")
_CucsDcxFcoeVifEpInstanceId_Type = CucsManagedObjectId
_CucsDcxFcoeVifEpInstanceId_Object = MibTableColumn
cucsDcxFcoeVifEpInstanceId = _CucsDcxFcoeVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 1),
    _CucsDcxFcoeVifEpInstanceId_Type()
)
cucsDcxFcoeVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpInstanceId.setStatus("current")
_CucsDcxFcoeVifEpDn_Type = CucsManagedObjectDn
_CucsDcxFcoeVifEpDn_Object = MibTableColumn
cucsDcxFcoeVifEpDn = _CucsDcxFcoeVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 2),
    _CucsDcxFcoeVifEpDn_Type()
)
cucsDcxFcoeVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpDn.setStatus("current")
_CucsDcxFcoeVifEpRn_Type = SnmpAdminString
_CucsDcxFcoeVifEpRn_Object = MibTableColumn
cucsDcxFcoeVifEpRn = _CucsDcxFcoeVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 3),
    _CucsDcxFcoeVifEpRn_Type()
)
cucsDcxFcoeVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpRn.setStatus("current")
_CucsDcxFcoeVifEpId_Type = Gauge32
_CucsDcxFcoeVifEpId_Object = MibTableColumn
cucsDcxFcoeVifEpId = _CucsDcxFcoeVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 4),
    _CucsDcxFcoeVifEpId_Type()
)
cucsDcxFcoeVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDcxFcoeVifEpId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DCX-MIB",
    **{"cucsDcxObjects": cucsDcxObjects,
       "cucsDcxNsTable": cucsDcxNsTable,
       "cucsDcxNsEntry": cucsDcxNsEntry,
       "cucsDcxNsInstanceId": cucsDcxNsInstanceId,
       "cucsDcxNsDn": cucsDcxNsDn,
       "cucsDcxNsRn": cucsDcxNsRn,
       "cucsDcxNsAllocStatus": cucsDcxNsAllocStatus,
       "cucsDcxNsSide": cucsDcxNsSide,
       "cucsDcxNsSize": cucsDcxNsSize,
       "cucsDcxNsSwitchId": cucsDcxNsSwitchId,
       "cucsDcxNsUsed": cucsDcxNsUsed,
       "cucsDcxUniverseTable": cucsDcxUniverseTable,
       "cucsDcxUniverseEntry": cucsDcxUniverseEntry,
       "cucsDcxUniverseInstanceId": cucsDcxUniverseInstanceId,
       "cucsDcxUniverseDn": cucsDcxUniverseDn,
       "cucsDcxUniverseRn": cucsDcxUniverseRn,
       "cucsDcxVIfTable": cucsDcxVIfTable,
       "cucsDcxVIfEntry": cucsDcxVIfEntry,
       "cucsDcxVIfInstanceId": cucsDcxVIfInstanceId,
       "cucsDcxVIfDn": cucsDcxVIfDn,
       "cucsDcxVIfRn": cucsDcxVIfRn,
       "cucsDcxVIfAdminState": cucsDcxVIfAdminState,
       "cucsDcxVIfCookie": cucsDcxVIfCookie,
       "cucsDcxVIfEpDn": cucsDcxVIfEpDn,
       "cucsDcxVIfId": cucsDcxVIfId,
       "cucsDcxVIfIfRole": cucsDcxVIfIfRole,
       "cucsDcxVIfIfType": cucsDcxVIfIfType,
       "cucsDcxVIfInstType": cucsDcxVIfInstType,
       "cucsDcxVIfLc": cucsDcxVIfLc,
       "cucsDcxVIfLinkState": cucsDcxVIfLinkState,
       "cucsDcxVIfLocale": cucsDcxVIfLocale,
       "cucsDcxVIfName": cucsDcxVIfName,
       "cucsDcxVIfOperState": cucsDcxVIfOperState,
       "cucsDcxVIfPeerDn": cucsDcxVIfPeerDn,
       "cucsDcxVIfProtPeerId": cucsDcxVIfProtPeerId,
       "cucsDcxVIfProtRole": cucsDcxVIfProtRole,
       "cucsDcxVIfProtState": cucsDcxVIfProtState,
       "cucsDcxVIfQosControl": cucsDcxVIfQosControl,
       "cucsDcxVIfState": cucsDcxVIfState,
       "cucsDcxVIfSwitchId": cucsDcxVIfSwitchId,
       "cucsDcxVIfTag": cucsDcxVIfTag,
       "cucsDcxVIfTransport": cucsDcxVIfTransport,
       "cucsDcxVIfType": cucsDcxVIfType,
       "cucsDcxVcTable": cucsDcxVcTable,
       "cucsDcxVcEntry": cucsDcxVcEntry,
       "cucsDcxVcInstanceId": cucsDcxVcInstanceId,
       "cucsDcxVcDn": cucsDcxVcDn,
       "cucsDcxVcRn": cucsDcxVcRn,
       "cucsDcxVcAdminState": cucsDcxVcAdminState,
       "cucsDcxVcBorderPortId": cucsDcxVcBorderPortId,
       "cucsDcxVcBorderSlotId": cucsDcxVcBorderSlotId,
       "cucsDcxVcCdp": cucsDcxVcCdp,
       "cucsDcxVcCookie": cucsDcxVcCookie,
       "cucsDcxVcCos": cucsDcxVcCos,
       "cucsDcxVcDerivedFromId": cucsDcxVcDerivedFromId,
       "cucsDcxVcEncap": cucsDcxVcEncap,
       "cucsDcxVcFcoeId": cucsDcxVcFcoeId,
       "cucsDcxVcFltAggr": cucsDcxVcFltAggr,
       "cucsDcxVcForgeMac": cucsDcxVcForgeMac,
       "cucsDcxVcId": cucsDcxVcId,
       "cucsDcxVcInstType": cucsDcxVcInstType,
       "cucsDcxVcLc": cucsDcxVcLc,
       "cucsDcxVcLinkState": cucsDcxVcLinkState,
       "cucsDcxVcLocale": cucsDcxVcLocale,
       "cucsDcxVcMonTrafDir": cucsDcxVcMonTrafDir,
       "cucsDcxVcName": cucsDcxVcName,
       "cucsDcxVcOperBorderPortId": cucsDcxVcOperBorderPortId,
       "cucsDcxVcOperBorderSlotId": cucsDcxVcOperBorderSlotId,
       "cucsDcxVcOperState": cucsDcxVcOperState,
       "cucsDcxVcProtState": cucsDcxVcProtState,
       "cucsDcxVcQosPolicyId": cucsDcxVcQosPolicyId,
       "cucsDcxVcRole": cucsDcxVcRole,
       "cucsDcxVcState": cucsDcxVcState,
       "cucsDcxVcStateQual": cucsDcxVcStateQual,
       "cucsDcxVcSwitchId": cucsDcxVcSwitchId,
       "cucsDcxVcTag": cucsDcxVcTag,
       "cucsDcxVcTransport": cucsDcxVcTransport,
       "cucsDcxVcType": cucsDcxVcType,
       "cucsDcxVcUplinkFailAction": cucsDcxVcUplinkFailAction,
       "cucsDcxVcVnic": cucsDcxVcVnic,
       "cucsDcxVcPeerId": cucsDcxVcPeerId,
       "cucsDcxVcQosPolicyDn": cucsDcxVcQosPolicyDn,
       "cucsDcxVcMacRegisterMode": cucsDcxVcMacRegisterMode,
       "cucsDcxVcBorderVfcId": cucsDcxVcBorderVfcId,
       "cucsDcxVcLldp": cucsDcxVcLldp,
       "cucsDcxVcBorderAggrPortId": cucsDcxVcBorderAggrPortId,
       "cucsDcxVcOperBorderAggrPortId": cucsDcxVcOperBorderAggrPortId,
       "cucsDcxVifEpTable": cucsDcxVifEpTable,
       "cucsDcxVifEpEntry": cucsDcxVifEpEntry,
       "cucsDcxVifEpInstanceId": cucsDcxVifEpInstanceId,
       "cucsDcxVifEpDn": cucsDcxVifEpDn,
       "cucsDcxVifEpRn": cucsDcxVifEpRn,
       "cucsDcxVifEpId": cucsDcxVifEpId,
       "cucsDcxFcoeVifEpTable": cucsDcxFcoeVifEpTable,
       "cucsDcxFcoeVifEpEntry": cucsDcxFcoeVifEpEntry,
       "cucsDcxFcoeVifEpInstanceId": cucsDcxFcoeVifEpInstanceId,
       "cucsDcxFcoeVifEpDn": cucsDcxFcoeVifEpDn,
       "cucsDcxFcoeVifEpRn": cucsDcxFcoeVifEpRn,
       "cucsDcxFcoeVifEpId": cucsDcxFcoeVifEpId}
)
