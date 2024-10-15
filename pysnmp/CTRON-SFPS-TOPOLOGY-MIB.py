# SNMP MIB module (CTRON-SFPS-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:34 2024
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

(sfpsDapiNvramStats,
 sfpsDirLockConfig,
 sfpsDirLockStats,
 sfpsDirRestriction,
 sfpsDirViolation,
 sfpsDirViolationAPI,
 sfpsDirViolationDeltaAPI,
 sfpsESPTopologyAgent,
 sfpsNeighborEvents,
 sfpsRATopAgentPortTableAPIIn,
 sfpsRATopAgentPortTableAPIOut,
 sfpsRATopologyAgent,
 sfpsRestrictedMobility,
 sfpsRestrictedMobilityAPI,
 sfpsServiceCenter,
 sfpsTAPITestIn,
 sfpsTAPITestOut,
 sfpsTPMPortTableAPIIn,
 sfpsTPMPortTableAPIOut,
 sfpsTopologyAgentCommon,
 sfpsTopologyFCL,
 sfpsTopologyPortManager,
 sfpsTopologyServerPortEventRelay,
 sfpsTopologyServerTest,
 sfpsTopologyServerTestIn,
 sfpsTopologyVNSNeighbors,
 sfpsVLANTopAgentPortTableAPIIn,
 sfpsVLANTopologyAgent,
 sfpsVMTopologyServer) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsDapiNvramStats",
    "sfpsDirLockConfig",
    "sfpsDirLockStats",
    "sfpsDirRestriction",
    "sfpsDirViolation",
    "sfpsDirViolationAPI",
    "sfpsDirViolationDeltaAPI",
    "sfpsESPTopologyAgent",
    "sfpsNeighborEvents",
    "sfpsRATopAgentPortTableAPIIn",
    "sfpsRATopAgentPortTableAPIOut",
    "sfpsRATopologyAgent",
    "sfpsRestrictedMobility",
    "sfpsRestrictedMobilityAPI",
    "sfpsServiceCenter",
    "sfpsTAPITestIn",
    "sfpsTAPITestOut",
    "sfpsTPMPortTableAPIIn",
    "sfpsTPMPortTableAPIOut",
    "sfpsTopologyAgentCommon",
    "sfpsTopologyFCL",
    "sfpsTopologyPortManager",
    "sfpsTopologyServerPortEventRelay",
    "sfpsTopologyServerTest",
    "sfpsTopologyServerTestIn",
    "sfpsTopologyVNSNeighbors",
    "sfpsVLANTopAgentPortTableAPIIn",
    "sfpsVLANTopologyAgent",
    "sfpsVMTopologyServer")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsServiceCenterTopologyTable_Object = MibTable
sfpsServiceCenterTopologyTable = _SfpsServiceCenterTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyTable.setStatus("mandatory")
_SfpsServiceCenterTopologyEntry_Object = MibTableRow
sfpsServiceCenterTopologyEntry = _SfpsServiceCenterTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1)
)
sfpsServiceCenterTopologyEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsServiceCenterTopologyHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyEntry.setStatus("mandatory")
_SfpsServiceCenterTopologyHashLeaf_Type = HexInteger
_SfpsServiceCenterTopologyHashLeaf_Object = MibTableColumn
sfpsServiceCenterTopologyHashLeaf = _SfpsServiceCenterTopologyHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 1),
    _SfpsServiceCenterTopologyHashLeaf_Type()
)
sfpsServiceCenterTopologyHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyHashLeaf.setStatus("mandatory")
_SfpsServiceCenterTopologyMetric_Type = Integer32
_SfpsServiceCenterTopologyMetric_Object = MibTableColumn
sfpsServiceCenterTopologyMetric = _SfpsServiceCenterTopologyMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 2),
    _SfpsServiceCenterTopologyMetric_Type()
)
sfpsServiceCenterTopologyMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyMetric.setStatus("mandatory")
_SfpsServiceCenterTopologyName_Type = DisplayString
_SfpsServiceCenterTopologyName_Object = MibTableColumn
sfpsServiceCenterTopologyName = _SfpsServiceCenterTopologyName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 3),
    _SfpsServiceCenterTopologyName_Type()
)
sfpsServiceCenterTopologyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyName.setStatus("mandatory")


class _SfpsServiceCenterTopologyOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterTopologyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsServiceCenterTopologyOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterTopologyOperStatus_Object = MibTableColumn
sfpsServiceCenterTopologyOperStatus = _SfpsServiceCenterTopologyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 4),
    _SfpsServiceCenterTopologyOperStatus_Type()
)
sfpsServiceCenterTopologyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyOperStatus.setStatus("mandatory")


class _SfpsServiceCenterTopologyAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterTopologyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SfpsServiceCenterTopologyAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterTopologyAdminStatus_Object = MibTableColumn
sfpsServiceCenterTopologyAdminStatus = _SfpsServiceCenterTopologyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 5),
    _SfpsServiceCenterTopologyAdminStatus_Type()
)
sfpsServiceCenterTopologyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyAdminStatus.setStatus("mandatory")
_SfpsServiceCenterTopologyStatusTime_Type = TimeTicks
_SfpsServiceCenterTopologyStatusTime_Object = MibTableColumn
sfpsServiceCenterTopologyStatusTime = _SfpsServiceCenterTopologyStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 6),
    _SfpsServiceCenterTopologyStatusTime_Type()
)
sfpsServiceCenterTopologyStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyStatusTime.setStatus("mandatory")
_SfpsServiceCenterTopologyRequests_Type = Integer32
_SfpsServiceCenterTopologyRequests_Object = MibTableColumn
sfpsServiceCenterTopologyRequests = _SfpsServiceCenterTopologyRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 7),
    _SfpsServiceCenterTopologyRequests_Type()
)
sfpsServiceCenterTopologyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyRequests.setStatus("mandatory")
_SfpsServiceCenterTopologyResponses_Type = Integer32
_SfpsServiceCenterTopologyResponses_Object = MibTableColumn
sfpsServiceCenterTopologyResponses = _SfpsServiceCenterTopologyResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 8, 1, 8),
    _SfpsServiceCenterTopologyResponses_Type()
)
sfpsServiceCenterTopologyResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterTopologyResponses.setStatus("mandatory")
_SfpsHistoryTopologyServerTable_Object = MibTable
sfpsHistoryTopologyServerTable = _SfpsHistoryTopologyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7)
)
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerTable.setStatus("mandatory")
_SfpsHistoryTopologyServerEntry_Object = MibTableRow
sfpsHistoryTopologyServerEntry = _SfpsHistoryTopologyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1)
)
sfpsHistoryTopologyServerEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsHistoryTopologyServerIndex"),
)
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerEntry.setStatus("mandatory")
_SfpsHistoryTopologyServerIndex_Type = Integer32
_SfpsHistoryTopologyServerIndex_Object = MibTableColumn
sfpsHistoryTopologyServerIndex = _SfpsHistoryTopologyServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 1),
    _SfpsHistoryTopologyServerIndex_Type()
)
sfpsHistoryTopologyServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerIndex.setStatus("mandatory")
_SfpsHistoryTopologyServerLogicalPort_Type = Integer32
_SfpsHistoryTopologyServerLogicalPort_Object = MibTableColumn
sfpsHistoryTopologyServerLogicalPort = _SfpsHistoryTopologyServerLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 2),
    _SfpsHistoryTopologyServerLogicalPort_Type()
)
sfpsHistoryTopologyServerLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerLogicalPort.setStatus("mandatory")
_SfpsHistoryTopologyServerSwitchID_Type = OctetString
_SfpsHistoryTopologyServerSwitchID_Object = MibTableColumn
sfpsHistoryTopologyServerSwitchID = _SfpsHistoryTopologyServerSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 3),
    _SfpsHistoryTopologyServerSwitchID_Type()
)
sfpsHistoryTopologyServerSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerSwitchID.setStatus("mandatory")


class _SfpsHistoryTopologyServerEvent_Type(Integer32):
    """Custom type sfpsHistoryTopologyServerEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("agingNghLoss", 4),
          ("crossedPortNghLoss", 9),
          ("duplicateNghLoss", 6),
          ("foundNeighbor", 1),
          ("functionalLevelNghLoss", 10),
          ("loopedPortNhgLoss", 8),
          ("optionsGain", 2),
          ("optionsLoss", 3),
          ("portDownNghLoss", 5),
          ("sequenceNumberReset", 13),
          ("subtractPortNghLoss", 7),
          ("twoWayCommLoss", 12),
          ("versionedPortNghLoss", 11))
    )


_SfpsHistoryTopologyServerEvent_Type.__name__ = "Integer32"
_SfpsHistoryTopologyServerEvent_Object = MibTableColumn
sfpsHistoryTopologyServerEvent = _SfpsHistoryTopologyServerEvent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 4),
    _SfpsHistoryTopologyServerEvent_Type()
)
sfpsHistoryTopologyServerEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerEvent.setStatus("mandatory")
_SfpsHistoryTopologyServerSwitchIP_Type = IpAddress
_SfpsHistoryTopologyServerSwitchIP_Object = MibTableColumn
sfpsHistoryTopologyServerSwitchIP = _SfpsHistoryTopologyServerSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 5),
    _SfpsHistoryTopologyServerSwitchIP_Type()
)
sfpsHistoryTopologyServerSwitchIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerSwitchIP.setStatus("mandatory")
_SfpsHistoryTopologyServerChassisMAC_Type = SfpsAddress
_SfpsHistoryTopologyServerChassisMAC_Object = MibTableColumn
sfpsHistoryTopologyServerChassisMAC = _SfpsHistoryTopologyServerChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 6),
    _SfpsHistoryTopologyServerChassisMAC_Type()
)
sfpsHistoryTopologyServerChassisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerChassisMAC.setStatus("mandatory")
_SfpsHistoryTopologyServerChassisIP_Type = IpAddress
_SfpsHistoryTopologyServerChassisIP_Object = MibTableColumn
sfpsHistoryTopologyServerChassisIP = _SfpsHistoryTopologyServerChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 7),
    _SfpsHistoryTopologyServerChassisIP_Type()
)
sfpsHistoryTopologyServerChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerChassisIP.setStatus("mandatory")
_SfpsHistoryTopologyServerAgent_Type = DisplayString
_SfpsHistoryTopologyServerAgent_Object = MibTableColumn
sfpsHistoryTopologyServerAgent = _SfpsHistoryTopologyServerAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 8),
    _SfpsHistoryTopologyServerAgent_Type()
)
sfpsHistoryTopologyServerAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerAgent.setStatus("mandatory")
_SfpsHistoryTopologyServerDeltaOptionsMask_Type = Integer32
_SfpsHistoryTopologyServerDeltaOptionsMask_Object = MibTableColumn
sfpsHistoryTopologyServerDeltaOptionsMask = _SfpsHistoryTopologyServerDeltaOptionsMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 9),
    _SfpsHistoryTopologyServerDeltaOptionsMask_Type()
)
sfpsHistoryTopologyServerDeltaOptionsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerDeltaOptionsMask.setStatus("mandatory")
_SfpsHistoryTopologyServerCurrentOptionsMask_Type = Integer32
_SfpsHistoryTopologyServerCurrentOptionsMask_Object = MibTableColumn
sfpsHistoryTopologyServerCurrentOptionsMask = _SfpsHistoryTopologyServerCurrentOptionsMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 10),
    _SfpsHistoryTopologyServerCurrentOptionsMask_Type()
)
sfpsHistoryTopologyServerCurrentOptionsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerCurrentOptionsMask.setStatus("mandatory")
_SfpsHistoryTopologyServerFCL_Type = Integer32
_SfpsHistoryTopologyServerFCL_Object = MibTableColumn
sfpsHistoryTopologyServerFCL = _SfpsHistoryTopologyServerFCL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 11),
    _SfpsHistoryTopologyServerFCL_Type()
)
sfpsHistoryTopologyServerFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerFCL.setStatus("mandatory")
_SfpsHistoryTopologyServerSysTime_Type = TimeTicks
_SfpsHistoryTopologyServerSysTime_Object = MibTableColumn
sfpsHistoryTopologyServerSysTime = _SfpsHistoryTopologyServerSysTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7, 7, 1, 12),
    _SfpsHistoryTopologyServerSysTime_Type()
)
sfpsHistoryTopologyServerSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsHistoryTopologyServerSysTime.setStatus("mandatory")
_SfpsTPMPortTable_Object = MibTable
sfpsTPMPortTable = _SfpsTPMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsTPMPortTable.setStatus("mandatory")
_SfpsTPMPortEntry_Object = MibTableRow
sfpsTPMPortEntry = _SfpsTPMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1)
)
sfpsTPMPortEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsTPMPortLogicalPort"),
)
if mibBuilder.loadTexts:
    sfpsTPMPortEntry.setStatus("mandatory")
_SfpsTPMPortLogicalPort_Type = Integer32
_SfpsTPMPortLogicalPort_Object = MibTableColumn
sfpsTPMPortLogicalPort = _SfpsTPMPortLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 1),
    _SfpsTPMPortLogicalPort_Type()
)
sfpsTPMPortLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortLogicalPort.setStatus("mandatory")


class _SfpsTPMPortMediaType_Type(Integer32):
    """Custom type sfpsTPMPortMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("atm-encap", 9),
          ("atm-forum-lec", 12),
          ("atm-forum-pvc", 13),
          ("atm-forum-svc", 14),
          ("atm-lec", 3),
          ("atm-pvc", 10),
          ("ethernet", 1),
          ("fddi", 2),
          ("hcp", 7),
          ("hdp", 8),
          ("inb", 6),
          ("token-ring", 4),
          ("unknown", 11),
          ("wan", 5))
    )


_SfpsTPMPortMediaType_Type.__name__ = "Integer32"
_SfpsTPMPortMediaType_Object = MibTableColumn
sfpsTPMPortMediaType = _SfpsTPMPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 2),
    _SfpsTPMPortMediaType_Type()
)
sfpsTPMPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortMediaType.setStatus("mandatory")
_SfpsTPMPortTopologyAgent_Type = DisplayString
_SfpsTPMPortTopologyAgent_Object = MibTableColumn
sfpsTPMPortTopologyAgent = _SfpsTPMPortTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 3),
    _SfpsTPMPortTopologyAgent_Type()
)
sfpsTPMPortTopologyAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortTopologyAgent.setStatus("mandatory")
_SfpsTPMPortVlanAttributes_Type = Integer32
_SfpsTPMPortVlanAttributes_Object = MibTableColumn
sfpsTPMPortVlanAttributes = _SfpsTPMPortVlanAttributes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 8),
    _SfpsTPMPortVlanAttributes_Type()
)
sfpsTPMPortVlanAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortVlanAttributes.setStatus("mandatory")
_SfpsTPMPortNVRAMStatus_Type = Integer32
_SfpsTPMPortNVRAMStatus_Object = MibTableColumn
sfpsTPMPortNVRAMStatus = _SfpsTPMPortNVRAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 9),
    _SfpsTPMPortNVRAMStatus_Type()
)
sfpsTPMPortNVRAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortNVRAMStatus.setStatus("mandatory")
_SfpsTPMPortCorePortVID_Type = Integer32
_SfpsTPMPortCorePortVID_Object = MibTableColumn
sfpsTPMPortCorePortVID = _SfpsTPMPortCorePortVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 1, 1, 10),
    _SfpsTPMPortCorePortVID_Type()
)
sfpsTPMPortCorePortVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortCorePortVID.setStatus("mandatory")


class _SfpsTPMPortTableAPIInVerb_Type(Integer32):
    """Custom type sfpsTPMPortTableAPIInVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("getPortInfo", 3),
          ("other", 1))
    )


_SfpsTPMPortTableAPIInVerb_Type.__name__ = "Integer32"
_SfpsTPMPortTableAPIInVerb_Object = MibScalar
sfpsTPMPortTableAPIInVerb = _SfpsTPMPortTableAPIInVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 1),
    _SfpsTPMPortTableAPIInVerb_Type()
)
sfpsTPMPortTableAPIInVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInVerb.setStatus("mandatory")
_SfpsTPMPortTableAPIInLogicalPort_Type = Integer32
_SfpsTPMPortTableAPIInLogicalPort_Object = MibScalar
sfpsTPMPortTableAPIInLogicalPort = _SfpsTPMPortTableAPIInLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 2),
    _SfpsTPMPortTableAPIInLogicalPort_Type()
)
sfpsTPMPortTableAPIInLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInLogicalPort.setStatus("mandatory")
_SfpsTPMPortTableAPIInTopologyAgent_Type = Integer32
_SfpsTPMPortTableAPIInTopologyAgent_Object = MibScalar
sfpsTPMPortTableAPIInTopologyAgent = _SfpsTPMPortTableAPIInTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 3),
    _SfpsTPMPortTableAPIInTopologyAgent_Type()
)
sfpsTPMPortTableAPIInTopologyAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInTopologyAgent.setStatus("mandatory")


class _SfpsTPMPortTableAPIInAdminPortUp_Type(Integer32):
    """Custom type sfpsTPMPortTableAPIInAdminPortUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsTPMPortTableAPIInAdminPortUp_Type.__name__ = "Integer32"
_SfpsTPMPortTableAPIInAdminPortUp_Object = MibScalar
sfpsTPMPortTableAPIInAdminPortUp = _SfpsTPMPortTableAPIInAdminPortUp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 4),
    _SfpsTPMPortTableAPIInAdminPortUp_Type()
)
sfpsTPMPortTableAPIInAdminPortUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInAdminPortUp.setStatus("mandatory")


class _SfpsTPMPortTableAPIInAdminPortDown_Type(Integer32):
    """Custom type sfpsTPMPortTableAPIInAdminPortDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsTPMPortTableAPIInAdminPortDown_Type.__name__ = "Integer32"
_SfpsTPMPortTableAPIInAdminPortDown_Object = MibScalar
sfpsTPMPortTableAPIInAdminPortDown = _SfpsTPMPortTableAPIInAdminPortDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 5),
    _SfpsTPMPortTableAPIInAdminPortDown_Type()
)
sfpsTPMPortTableAPIInAdminPortDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInAdminPortDown.setStatus("mandatory")
_SfpsTPMPortTableAPIInCorePortVID_Type = Integer32
_SfpsTPMPortTableAPIInCorePortVID_Object = MibScalar
sfpsTPMPortTableAPIInCorePortVID = _SfpsTPMPortTableAPIInCorePortVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2, 6),
    _SfpsTPMPortTableAPIInCorePortVID_Type()
)
sfpsTPMPortTableAPIInCorePortVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIInCorePortVID.setStatus("mandatory")
_SfpsTPMPortTableAPIOutLogicalPort_Type = Integer32
_SfpsTPMPortTableAPIOutLogicalPort_Object = MibScalar
sfpsTPMPortTableAPIOutLogicalPort = _SfpsTPMPortTableAPIOutLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 3, 1),
    _SfpsTPMPortTableAPIOutLogicalPort_Type()
)
sfpsTPMPortTableAPIOutLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIOutLogicalPort.setStatus("mandatory")
_SfpsTPMPortTableAPIOutTopologyAgent_Type = Integer32
_SfpsTPMPortTableAPIOutTopologyAgent_Object = MibScalar
sfpsTPMPortTableAPIOutTopologyAgent = _SfpsTPMPortTableAPIOutTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 3, 2),
    _SfpsTPMPortTableAPIOutTopologyAgent_Type()
)
sfpsTPMPortTableAPIOutTopologyAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTPMPortTableAPIOutTopologyAgent.setStatus("mandatory")
_SfpsCommonNeighborTable_Object = MibTable
sfpsCommonNeighborTable = _SfpsCommonNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsCommonNeighborTable.setStatus("mandatory")
_SfpsCommonNeighborEntry_Object = MibTableRow
sfpsCommonNeighborEntry = _SfpsCommonNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1)
)
sfpsCommonNeighborEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsCommonNeighborLogicalPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsCommonNeighborSwitchID"),
)
if mibBuilder.loadTexts:
    sfpsCommonNeighborEntry.setStatus("mandatory")
_SfpsCommonNeighborLogicalPort_Type = Integer32
_SfpsCommonNeighborLogicalPort_Object = MibTableColumn
sfpsCommonNeighborLogicalPort = _SfpsCommonNeighborLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 1),
    _SfpsCommonNeighborLogicalPort_Type()
)
sfpsCommonNeighborLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborLogicalPort.setStatus("mandatory")
_SfpsCommonNeighborSwitchID_Type = DisplayString
_SfpsCommonNeighborSwitchID_Object = MibTableColumn
sfpsCommonNeighborSwitchID = _SfpsCommonNeighborSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 2),
    _SfpsCommonNeighborSwitchID_Type()
)
sfpsCommonNeighborSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSwitchID.setStatus("mandatory")
_SfpsCommonNeighborSwitchIP_Type = IpAddress
_SfpsCommonNeighborSwitchIP_Object = MibTableColumn
sfpsCommonNeighborSwitchIP = _SfpsCommonNeighborSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 3),
    _SfpsCommonNeighborSwitchIP_Type()
)
sfpsCommonNeighborSwitchIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSwitchIP.setStatus("mandatory")
_SfpsCommonNeighborSwitchMAC_Type = SfpsAddress
_SfpsCommonNeighborSwitchMAC_Object = MibTableColumn
sfpsCommonNeighborSwitchMAC = _SfpsCommonNeighborSwitchMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 4),
    _SfpsCommonNeighborSwitchMAC_Type()
)
sfpsCommonNeighborSwitchMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSwitchMAC.setStatus("mandatory")


class _SfpsCommonNeighborSwitchType_Type(Integer32):
    """Custom type sfpsCommonNeighborSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 2),
          ("vns", 1))
    )


_SfpsCommonNeighborSwitchType_Type.__name__ = "Integer32"
_SfpsCommonNeighborSwitchType_Object = MibTableColumn
sfpsCommonNeighborSwitchType = _SfpsCommonNeighborSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 5),
    _SfpsCommonNeighborSwitchType_Type()
)
sfpsCommonNeighborSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSwitchType.setStatus("mandatory")
_SfpsCommonNeighborHellosReceived_Type = Integer32
_SfpsCommonNeighborHellosReceived_Object = MibTableColumn
sfpsCommonNeighborHellosReceived = _SfpsCommonNeighborHellosReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 6),
    _SfpsCommonNeighborHellosReceived_Type()
)
sfpsCommonNeighborHellosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborHellosReceived.setStatus("mandatory")
_SfpsCommonNeighborFirstHeard_Type = TimeTicks
_SfpsCommonNeighborFirstHeard_Object = MibTableColumn
sfpsCommonNeighborFirstHeard = _SfpsCommonNeighborFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 7),
    _SfpsCommonNeighborFirstHeard_Type()
)
sfpsCommonNeighborFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborFirstHeard.setStatus("mandatory")
_SfpsCommonNeighborLastHeard_Type = TimeTicks
_SfpsCommonNeighborLastHeard_Object = MibTableColumn
sfpsCommonNeighborLastHeard = _SfpsCommonNeighborLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 8),
    _SfpsCommonNeighborLastHeard_Type()
)
sfpsCommonNeighborLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborLastHeard.setStatus("mandatory")
_SfpsCommonNeighborReceiveFrequency_Type = Integer32
_SfpsCommonNeighborReceiveFrequency_Object = MibTableColumn
sfpsCommonNeighborReceiveFrequency = _SfpsCommonNeighborReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 9),
    _SfpsCommonNeighborReceiveFrequency_Type()
)
sfpsCommonNeighborReceiveFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborReceiveFrequency.setStatus("mandatory")
_SfpsCommonNeighborTopologyAgent_Type = DisplayString
_SfpsCommonNeighborTopologyAgent_Object = MibTableColumn
sfpsCommonNeighborTopologyAgent = _SfpsCommonNeighborTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 10),
    _SfpsCommonNeighborTopologyAgent_Type()
)
sfpsCommonNeighborTopologyAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborTopologyAgent.setStatus("mandatory")
_SfpsCommonNeighborChassisMAC_Type = SfpsAddress
_SfpsCommonNeighborChassisMAC_Object = MibTableColumn
sfpsCommonNeighborChassisMAC = _SfpsCommonNeighborChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 11),
    _SfpsCommonNeighborChassisMAC_Type()
)
sfpsCommonNeighborChassisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborChassisMAC.setStatus("mandatory")


class _SfpsCommonNeighborCommState_Type(Integer32):
    """Custom type sfpsCommonNeighborCommState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("oneWay", 2),
          ("twoWay", 3))
    )


_SfpsCommonNeighborCommState_Type.__name__ = "Integer32"
_SfpsCommonNeighborCommState_Object = MibTableColumn
sfpsCommonNeighborCommState = _SfpsCommonNeighborCommState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 12),
    _SfpsCommonNeighborCommState_Type()
)
sfpsCommonNeighborCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborCommState.setStatus("mandatory")


class _SfpsCommonNeighborNotifyState_Type(Integer32):
    """Custom type sfpsCommonNeighborNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("notified", 3),
          ("unNotified", 2))
    )


_SfpsCommonNeighborNotifyState_Type.__name__ = "Integer32"
_SfpsCommonNeighborNotifyState_Object = MibTableColumn
sfpsCommonNeighborNotifyState = _SfpsCommonNeighborNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 13),
    _SfpsCommonNeighborNotifyState_Type()
)
sfpsCommonNeighborNotifyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborNotifyState.setStatus("mandatory")
_SfpsCommonNeighborTwoWayLossCount_Type = Integer32
_SfpsCommonNeighborTwoWayLossCount_Object = MibTableColumn
sfpsCommonNeighborTwoWayLossCount = _SfpsCommonNeighborTwoWayLossCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 14),
    _SfpsCommonNeighborTwoWayLossCount_Type()
)
sfpsCommonNeighborTwoWayLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborTwoWayLossCount.setStatus("mandatory")
_SfpsCommonNeighborTwoWayLossTime_Type = TimeTicks
_SfpsCommonNeighborTwoWayLossTime_Object = MibTableColumn
sfpsCommonNeighborTwoWayLossTime = _SfpsCommonNeighborTwoWayLossTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 15),
    _SfpsCommonNeighborTwoWayLossTime_Type()
)
sfpsCommonNeighborTwoWayLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborTwoWayLossTime.setStatus("mandatory")
_SfpsCommonNeighborSeqNumLossCount_Type = Integer32
_SfpsCommonNeighborSeqNumLossCount_Object = MibTableColumn
sfpsCommonNeighborSeqNumLossCount = _SfpsCommonNeighborSeqNumLossCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 16),
    _SfpsCommonNeighborSeqNumLossCount_Type()
)
sfpsCommonNeighborSeqNumLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSeqNumLossCount.setStatus("mandatory")
_SfpsCommonNeighborSeqNumLossTime_Type = TimeTicks
_SfpsCommonNeighborSeqNumLossTime_Object = MibTableColumn
sfpsCommonNeighborSeqNumLossTime = _SfpsCommonNeighborSeqNumLossTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 17),
    _SfpsCommonNeighborSeqNumLossTime_Type()
)
sfpsCommonNeighborSeqNumLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSeqNumLossTime.setStatus("mandatory")
_SfpsCommonNeighborFalseAgingCount_Type = Integer32
_SfpsCommonNeighborFalseAgingCount_Object = MibTableColumn
sfpsCommonNeighborFalseAgingCount = _SfpsCommonNeighborFalseAgingCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 18),
    _SfpsCommonNeighborFalseAgingCount_Type()
)
sfpsCommonNeighborFalseAgingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborFalseAgingCount.setStatus("mandatory")
_SfpsCommonNeighborFalseAgingTime_Type = TimeTicks
_SfpsCommonNeighborFalseAgingTime_Object = MibTableColumn
sfpsCommonNeighborFalseAgingTime = _SfpsCommonNeighborFalseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 19),
    _SfpsCommonNeighborFalseAgingTime_Type()
)
sfpsCommonNeighborFalseAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborFalseAgingTime.setStatus("mandatory")
_SfpsCommonNeighborChassisIP_Type = IpAddress
_SfpsCommonNeighborChassisIP_Object = MibTableColumn
sfpsCommonNeighborChassisIP = _SfpsCommonNeighborChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 20),
    _SfpsCommonNeighborChassisIP_Type()
)
sfpsCommonNeighborChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborChassisIP.setStatus("mandatory")
_SfpsCommonNeighborFCL_Type = HexInteger
_SfpsCommonNeighborFCL_Object = MibTableColumn
sfpsCommonNeighborFCL = _SfpsCommonNeighborFCL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 21),
    _SfpsCommonNeighborFCL_Type()
)
sfpsCommonNeighborFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborFCL.setStatus("mandatory")
_SfpsCommonNeighborOptionsMask_Type = Integer32
_SfpsCommonNeighborOptionsMask_Object = MibTableColumn
sfpsCommonNeighborOptionsMask = _SfpsCommonNeighborOptionsMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 22),
    _SfpsCommonNeighborOptionsMask_Type()
)
sfpsCommonNeighborOptionsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborOptionsMask.setStatus("mandatory")


class _SfpsCommonNeighborRcvdPortState_Type(Integer32):
    """Custom type sfpsCommonNeighborRcvdPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("accessOnly", 11),
          ("downlingFlood", 19),
          ("fclStandby", 14),
          ("flood", 17),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgnt", 4),
          ("hybrid", 8),
          ("loopStandby", 15),
          ("network", 3),
          ("networkOnly", 10),
          ("other", 1),
          ("raPrimary", 12),
          ("raStandby", 16),
          ("standBy", 9),
          ("unknown", 6),
          ("unknown-ra-standy", 20),
          ("uplink", 13),
          ("uplinkFlood", 18))
    )


_SfpsCommonNeighborRcvdPortState_Type.__name__ = "Integer32"
_SfpsCommonNeighborRcvdPortState_Object = MibTableColumn
sfpsCommonNeighborRcvdPortState = _SfpsCommonNeighborRcvdPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 23),
    _SfpsCommonNeighborRcvdPortState_Type()
)
sfpsCommonNeighborRcvdPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborRcvdPortState.setStatus("mandatory")


class _SfpsCommonNeighborSendPortState_Type(Integer32):
    """Custom type sfpsCommonNeighborSendPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("accessOnly", 11),
          ("downlingFlood", 19),
          ("fclStandby", 14),
          ("flood", 17),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgnt", 4),
          ("hybrid", 8),
          ("loopStandby", 15),
          ("network", 3),
          ("networkOnly", 10),
          ("other", 1),
          ("raPrimary", 12),
          ("raStandby", 16),
          ("standBy", 9),
          ("unknown", 6),
          ("unknown-ra-standy", 20),
          ("uplink", 13),
          ("uplinkFlood", 18))
    )


_SfpsCommonNeighborSendPortState_Type.__name__ = "Integer32"
_SfpsCommonNeighborSendPortState_Object = MibTableColumn
sfpsCommonNeighborSendPortState = _SfpsCommonNeighborSendPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 24),
    _SfpsCommonNeighborSendPortState_Type()
)
sfpsCommonNeighborSendPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborSendPortState.setStatus("mandatory")


class _SfpsCommonNeighborCompatibility_Type(Integer32):
    """Custom type sfpsCommonNeighborCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("notCompatible", 2),
          ("unknown", 3))
    )


_SfpsCommonNeighborCompatibility_Type.__name__ = "Integer32"
_SfpsCommonNeighborCompatibility_Object = MibTableColumn
sfpsCommonNeighborCompatibility = _SfpsCommonNeighborCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 25),
    _SfpsCommonNeighborCompatibility_Type()
)
sfpsCommonNeighborCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborCompatibility.setStatus("mandatory")
_SfpsCommonNeighborCorePortVID_Type = Integer32
_SfpsCommonNeighborCorePortVID_Object = MibTableColumn
sfpsCommonNeighborCorePortVID = _SfpsCommonNeighborCorePortVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 1, 1, 26),
    _SfpsCommonNeighborCorePortVID_Type()
)
sfpsCommonNeighborCorePortVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCommonNeighborCorePortVID.setStatus("mandatory")
_SfpsIncompatibleNeighborTable_Object = MibTable
sfpsIncompatibleNeighborTable = _SfpsIncompatibleNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2)
)
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborTable.setStatus("mandatory")
_SfpsIncompatibleNeighborEntry_Object = MibTableRow
sfpsIncompatibleNeighborEntry = _SfpsIncompatibleNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1)
)
sfpsIncompatibleNeighborEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsIncompatibleNeighborLogicalPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsIncompatibleNeighborSwitchID"),
)
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborEntry.setStatus("mandatory")
_SfpsIncompatibleNeighborLogicalPort_Type = Integer32
_SfpsIncompatibleNeighborLogicalPort_Object = MibTableColumn
sfpsIncompatibleNeighborLogicalPort = _SfpsIncompatibleNeighborLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 1),
    _SfpsIncompatibleNeighborLogicalPort_Type()
)
sfpsIncompatibleNeighborLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborLogicalPort.setStatus("mandatory")
_SfpsIncompatibleNeighborSwitchID_Type = DisplayString
_SfpsIncompatibleNeighborSwitchID_Object = MibTableColumn
sfpsIncompatibleNeighborSwitchID = _SfpsIncompatibleNeighborSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 2),
    _SfpsIncompatibleNeighborSwitchID_Type()
)
sfpsIncompatibleNeighborSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSwitchID.setStatus("mandatory")
_SfpsIncompatibleNeighborSwitchIP_Type = IpAddress
_SfpsIncompatibleNeighborSwitchIP_Object = MibTableColumn
sfpsIncompatibleNeighborSwitchIP = _SfpsIncompatibleNeighborSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 3),
    _SfpsIncompatibleNeighborSwitchIP_Type()
)
sfpsIncompatibleNeighborSwitchIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSwitchIP.setStatus("mandatory")
_SfpsIncompatibleNeighborSwitchMAC_Type = SfpsAddress
_SfpsIncompatibleNeighborSwitchMAC_Object = MibTableColumn
sfpsIncompatibleNeighborSwitchMAC = _SfpsIncompatibleNeighborSwitchMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 4),
    _SfpsIncompatibleNeighborSwitchMAC_Type()
)
sfpsIncompatibleNeighborSwitchMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSwitchMAC.setStatus("mandatory")


class _SfpsIncompatibleNeighborSwitchType_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 2),
          ("vns", 1))
    )


_SfpsIncompatibleNeighborSwitchType_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborSwitchType_Object = MibTableColumn
sfpsIncompatibleNeighborSwitchType = _SfpsIncompatibleNeighborSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 5),
    _SfpsIncompatibleNeighborSwitchType_Type()
)
sfpsIncompatibleNeighborSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSwitchType.setStatus("mandatory")
_SfpsIncompatibleNeighborHellosReceived_Type = Integer32
_SfpsIncompatibleNeighborHellosReceived_Object = MibTableColumn
sfpsIncompatibleNeighborHellosReceived = _SfpsIncompatibleNeighborHellosReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 6),
    _SfpsIncompatibleNeighborHellosReceived_Type()
)
sfpsIncompatibleNeighborHellosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborHellosReceived.setStatus("mandatory")
_SfpsIncompatibleNeighborFirstHeard_Type = TimeTicks
_SfpsIncompatibleNeighborFirstHeard_Object = MibTableColumn
sfpsIncompatibleNeighborFirstHeard = _SfpsIncompatibleNeighborFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 7),
    _SfpsIncompatibleNeighborFirstHeard_Type()
)
sfpsIncompatibleNeighborFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborFirstHeard.setStatus("mandatory")
_SfpsIncompatibleNeighborLastHeard_Type = TimeTicks
_SfpsIncompatibleNeighborLastHeard_Object = MibTableColumn
sfpsIncompatibleNeighborLastHeard = _SfpsIncompatibleNeighborLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 8),
    _SfpsIncompatibleNeighborLastHeard_Type()
)
sfpsIncompatibleNeighborLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborLastHeard.setStatus("mandatory")
_SfpsIncompatibleNeighborReceiveFrequency_Type = Integer32
_SfpsIncompatibleNeighborReceiveFrequency_Object = MibTableColumn
sfpsIncompatibleNeighborReceiveFrequency = _SfpsIncompatibleNeighborReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 9),
    _SfpsIncompatibleNeighborReceiveFrequency_Type()
)
sfpsIncompatibleNeighborReceiveFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborReceiveFrequency.setStatus("mandatory")
_SfpsIncompatibleNeighborTopologyAgent_Type = DisplayString
_SfpsIncompatibleNeighborTopologyAgent_Object = MibTableColumn
sfpsIncompatibleNeighborTopologyAgent = _SfpsIncompatibleNeighborTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 10),
    _SfpsIncompatibleNeighborTopologyAgent_Type()
)
sfpsIncompatibleNeighborTopologyAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborTopologyAgent.setStatus("mandatory")
_SfpsIncompatibleNeighborChassisMAC_Type = SfpsAddress
_SfpsIncompatibleNeighborChassisMAC_Object = MibTableColumn
sfpsIncompatibleNeighborChassisMAC = _SfpsIncompatibleNeighborChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 11),
    _SfpsIncompatibleNeighborChassisMAC_Type()
)
sfpsIncompatibleNeighborChassisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborChassisMAC.setStatus("mandatory")


class _SfpsIncompatibleNeighborCommState_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborCommState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("oneWay", 2),
          ("twoWay", 3))
    )


_SfpsIncompatibleNeighborCommState_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborCommState_Object = MibTableColumn
sfpsIncompatibleNeighborCommState = _SfpsIncompatibleNeighborCommState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 12),
    _SfpsIncompatibleNeighborCommState_Type()
)
sfpsIncompatibleNeighborCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborCommState.setStatus("mandatory")


class _SfpsIncompatibleNeighborNotifyState_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("notified", 3),
          ("unNotified", 2))
    )


_SfpsIncompatibleNeighborNotifyState_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborNotifyState_Object = MibTableColumn
sfpsIncompatibleNeighborNotifyState = _SfpsIncompatibleNeighborNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 13),
    _SfpsIncompatibleNeighborNotifyState_Type()
)
sfpsIncompatibleNeighborNotifyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborNotifyState.setStatus("mandatory")
_SfpsIncompatibleNeighborTwoWayLossCount_Type = Integer32
_SfpsIncompatibleNeighborTwoWayLossCount_Object = MibTableColumn
sfpsIncompatibleNeighborTwoWayLossCount = _SfpsIncompatibleNeighborTwoWayLossCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 14),
    _SfpsIncompatibleNeighborTwoWayLossCount_Type()
)
sfpsIncompatibleNeighborTwoWayLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborTwoWayLossCount.setStatus("mandatory")
_SfpsIncompatibleNeighborTwoWayLossTime_Type = TimeTicks
_SfpsIncompatibleNeighborTwoWayLossTime_Object = MibTableColumn
sfpsIncompatibleNeighborTwoWayLossTime = _SfpsIncompatibleNeighborTwoWayLossTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 15),
    _SfpsIncompatibleNeighborTwoWayLossTime_Type()
)
sfpsIncompatibleNeighborTwoWayLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborTwoWayLossTime.setStatus("mandatory")
_SfpsIncompatibleNeighborSeqNumLossCount_Type = Integer32
_SfpsIncompatibleNeighborSeqNumLossCount_Object = MibTableColumn
sfpsIncompatibleNeighborSeqNumLossCount = _SfpsIncompatibleNeighborSeqNumLossCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 16),
    _SfpsIncompatibleNeighborSeqNumLossCount_Type()
)
sfpsIncompatibleNeighborSeqNumLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSeqNumLossCount.setStatus("mandatory")
_SfpsIncompatibleNeighborSeqNumLossTime_Type = TimeTicks
_SfpsIncompatibleNeighborSeqNumLossTime_Object = MibTableColumn
sfpsIncompatibleNeighborSeqNumLossTime = _SfpsIncompatibleNeighborSeqNumLossTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 17),
    _SfpsIncompatibleNeighborSeqNumLossTime_Type()
)
sfpsIncompatibleNeighborSeqNumLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborSeqNumLossTime.setStatus("mandatory")
_SfpsIncompatibleNeighborFalseAgingCount_Type = Integer32
_SfpsIncompatibleNeighborFalseAgingCount_Object = MibTableColumn
sfpsIncompatibleNeighborFalseAgingCount = _SfpsIncompatibleNeighborFalseAgingCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 18),
    _SfpsIncompatibleNeighborFalseAgingCount_Type()
)
sfpsIncompatibleNeighborFalseAgingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborFalseAgingCount.setStatus("mandatory")
_SfpsIncompatibleNeighborFalseAgingTime_Type = TimeTicks
_SfpsIncompatibleNeighborFalseAgingTime_Object = MibTableColumn
sfpsIncompatibleNeighborFalseAgingTime = _SfpsIncompatibleNeighborFalseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 19),
    _SfpsIncompatibleNeighborFalseAgingTime_Type()
)
sfpsIncompatibleNeighborFalseAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborFalseAgingTime.setStatus("mandatory")
_SfpsIncompatibleNeighborChassisIP_Type = IpAddress
_SfpsIncompatibleNeighborChassisIP_Object = MibTableColumn
sfpsIncompatibleNeighborChassisIP = _SfpsIncompatibleNeighborChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 20),
    _SfpsIncompatibleNeighborChassisIP_Type()
)
sfpsIncompatibleNeighborChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborChassisIP.setStatus("mandatory")
_SfpsIncompatibleNeighborFCL_Type = HexInteger
_SfpsIncompatibleNeighborFCL_Object = MibTableColumn
sfpsIncompatibleNeighborFCL = _SfpsIncompatibleNeighborFCL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 21),
    _SfpsIncompatibleNeighborFCL_Type()
)
sfpsIncompatibleNeighborFCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborFCL.setStatus("mandatory")
_SfpsIncompatibleNeighborOptionsMask_Type = Integer32
_SfpsIncompatibleNeighborOptionsMask_Object = MibTableColumn
sfpsIncompatibleNeighborOptionsMask = _SfpsIncompatibleNeighborOptionsMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 22),
    _SfpsIncompatibleNeighborOptionsMask_Type()
)
sfpsIncompatibleNeighborOptionsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborOptionsMask.setStatus("mandatory")


class _SfpsIncompatibleNeighborLocalPortState_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborLocalPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgnt", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsIncompatibleNeighborLocalPortState_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborLocalPortState_Object = MibTableColumn
sfpsIncompatibleNeighborLocalPortState = _SfpsIncompatibleNeighborLocalPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 23),
    _SfpsIncompatibleNeighborLocalPortState_Type()
)
sfpsIncompatibleNeighborLocalPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborLocalPortState.setStatus("mandatory")


class _SfpsIncompatibleNeighborRemotePortState_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborRemotePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgnt", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsIncompatibleNeighborRemotePortState_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborRemotePortState_Object = MibTableColumn
sfpsIncompatibleNeighborRemotePortState = _SfpsIncompatibleNeighborRemotePortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 24),
    _SfpsIncompatibleNeighborRemotePortState_Type()
)
sfpsIncompatibleNeighborRemotePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborRemotePortState.setStatus("mandatory")


class _SfpsIncompatibleNeighborCompatibility_Type(Integer32):
    """Custom type sfpsIncompatibleNeighborCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("notCompatible", 2),
          ("unknown", 3))
    )


_SfpsIncompatibleNeighborCompatibility_Type.__name__ = "Integer32"
_SfpsIncompatibleNeighborCompatibility_Object = MibTableColumn
sfpsIncompatibleNeighborCompatibility = _SfpsIncompatibleNeighborCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2, 2, 1, 25),
    _SfpsIncompatibleNeighborCompatibility_Type()
)
sfpsIncompatibleNeighborCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIncompatibleNeighborCompatibility.setStatus("mandatory")
_SfpsVLANTopAgentNeighborTable_Object = MibTable
sfpsVLANTopAgentNeighborTable = _SfpsVLANTopAgentNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsVLANTopAgentNeighborTable.setStatus("mandatory")
_SfpsVLANTopAgentNeighborEntry_Object = MibTableRow
sfpsVLANTopAgentNeighborEntry = _SfpsVLANTopAgentNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 1, 1)
)
sfpsVLANTopAgentNeighborEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsVLANTopAgentNeighborInPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsVLANTopAgentNeighborSwitchID"),
)
if mibBuilder.loadTexts:
    sfpsVLANTopAgentNeighborEntry.setStatus("mandatory")
_SfpsVLANTopAgentNeighborInPort_Type = Integer32
_SfpsVLANTopAgentNeighborInPort_Object = MibTableColumn
sfpsVLANTopAgentNeighborInPort = _SfpsVLANTopAgentNeighborInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 1, 1, 1),
    _SfpsVLANTopAgentNeighborInPort_Type()
)
sfpsVLANTopAgentNeighborInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentNeighborInPort.setStatus("mandatory")
_SfpsVLANTopAgentNeighborSwitchID_Type = DisplayString
_SfpsVLANTopAgentNeighborSwitchID_Object = MibTableColumn
sfpsVLANTopAgentNeighborSwitchID = _SfpsVLANTopAgentNeighborSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 1, 1, 2),
    _SfpsVLANTopAgentNeighborSwitchID_Type()
)
sfpsVLANTopAgentNeighborSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentNeighborSwitchID.setStatus("mandatory")
_SfpsVLANTopAgentNeighborOptions_Type = Integer32
_SfpsVLANTopAgentNeighborOptions_Object = MibTableColumn
sfpsVLANTopAgentNeighborOptions = _SfpsVLANTopAgentNeighborOptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 1, 1, 3),
    _SfpsVLANTopAgentNeighborOptions_Type()
)
sfpsVLANTopAgentNeighborOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentNeighborOptions.setStatus("mandatory")
_SfpsVLANTopAgentPortTable_Object = MibTable
sfpsVLANTopAgentPortTable = _SfpsVLANTopAgentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTable.setStatus("mandatory")
_SfpsVLANTopAgentPortEntry_Object = MibTableRow
sfpsVLANTopAgentPortEntry = _SfpsVLANTopAgentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1)
)
sfpsVLANTopAgentPortEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsVLANTopAgentPortPort"),
)
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortEntry.setStatus("mandatory")
_SfpsVLANTopAgentPortPort_Type = Integer32
_SfpsVLANTopAgentPortPort_Object = MibTableColumn
sfpsVLANTopAgentPortPort = _SfpsVLANTopAgentPortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 1),
    _SfpsVLANTopAgentPortPort_Type()
)
sfpsVLANTopAgentPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortPort.setStatus("mandatory")


class _SfpsVLANTopAgentPortHelloVersion_Type(Integer32):
    """Custom type sfpsVLANTopAgentPortHelloVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version2", 2),
          ("version3", 3),
          ("version4", 4),
          ("versionOther", 1))
    )


_SfpsVLANTopAgentPortHelloVersion_Type.__name__ = "Integer32"
_SfpsVLANTopAgentPortHelloVersion_Object = MibTableColumn
sfpsVLANTopAgentPortHelloVersion = _SfpsVLANTopAgentPortHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 2),
    _SfpsVLANTopAgentPortHelloVersion_Type()
)
sfpsVLANTopAgentPortHelloVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortHelloVersion.setStatus("mandatory")
_SfpsVLANTopAgentPortSendFrequency_Type = Integer32
_SfpsVLANTopAgentPortSendFrequency_Object = MibTableColumn
sfpsVLANTopAgentPortSendFrequency = _SfpsVLANTopAgentPortSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 3),
    _SfpsVLANTopAgentPortSendFrequency_Type()
)
sfpsVLANTopAgentPortSendFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortSendFrequency.setStatus("mandatory")
_SfpsVLANTopAgentPortRecvFrequency_Type = Integer32
_SfpsVLANTopAgentPortRecvFrequency_Object = MibTableColumn
sfpsVLANTopAgentPortRecvFrequency = _SfpsVLANTopAgentPortRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 4),
    _SfpsVLANTopAgentPortRecvFrequency_Type()
)
sfpsVLANTopAgentPortRecvFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortRecvFrequency.setStatus("mandatory")
_SfpsVLANTopAgentPortPortOptions_Type = Integer32
_SfpsVLANTopAgentPortPortOptions_Object = MibTableColumn
sfpsVLANTopAgentPortPortOptions = _SfpsVLANTopAgentPortPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 5),
    _SfpsVLANTopAgentPortPortOptions_Type()
)
sfpsVLANTopAgentPortPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortPortOptions.setStatus("mandatory")


class _SfpsVLANTopAgentPortNVRAMStatus_Type(Integer32):
    """Custom type sfpsVLANTopAgentPortNVRAMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SfpsVLANTopAgentPortNVRAMStatus_Type.__name__ = "Integer32"
_SfpsVLANTopAgentPortNVRAMStatus_Object = MibTableColumn
sfpsVLANTopAgentPortNVRAMStatus = _SfpsVLANTopAgentPortNVRAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 2, 1, 6),
    _SfpsVLANTopAgentPortNVRAMStatus_Type()
)
sfpsVLANTopAgentPortNVRAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortNVRAMStatus.setStatus("mandatory")


class _SfpsVLANTopAgentPortTableAPIInVerb_Type(Integer32):
    """Custom type sfpsVLANTopAgentPortTableAPIInVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("other", 1))
    )


_SfpsVLANTopAgentPortTableAPIInVerb_Type.__name__ = "Integer32"
_SfpsVLANTopAgentPortTableAPIInVerb_Object = MibScalar
sfpsVLANTopAgentPortTableAPIInVerb = _SfpsVLANTopAgentPortTableAPIInVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3, 1),
    _SfpsVLANTopAgentPortTableAPIInVerb_Type()
)
sfpsVLANTopAgentPortTableAPIInVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTableAPIInVerb.setStatus("mandatory")
_SfpsVLANTopAgentPortTableAPIInLogicalPort_Type = Integer32
_SfpsVLANTopAgentPortTableAPIInLogicalPort_Object = MibScalar
sfpsVLANTopAgentPortTableAPIInLogicalPort = _SfpsVLANTopAgentPortTableAPIInLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3, 2),
    _SfpsVLANTopAgentPortTableAPIInLogicalPort_Type()
)
sfpsVLANTopAgentPortTableAPIInLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTableAPIInLogicalPort.setStatus("mandatory")
_SfpsVLANTopAgentPortTableAPIInHelloVersion_Type = Integer32
_SfpsVLANTopAgentPortTableAPIInHelloVersion_Object = MibScalar
sfpsVLANTopAgentPortTableAPIInHelloVersion = _SfpsVLANTopAgentPortTableAPIInHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3, 3),
    _SfpsVLANTopAgentPortTableAPIInHelloVersion_Type()
)
sfpsVLANTopAgentPortTableAPIInHelloVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTableAPIInHelloVersion.setStatus("mandatory")
_SfpsVLANTopAgentPortTableAPIInSendFrequency_Type = Integer32
_SfpsVLANTopAgentPortTableAPIInSendFrequency_Object = MibScalar
sfpsVLANTopAgentPortTableAPIInSendFrequency = _SfpsVLANTopAgentPortTableAPIInSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3, 4),
    _SfpsVLANTopAgentPortTableAPIInSendFrequency_Type()
)
sfpsVLANTopAgentPortTableAPIInSendFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTableAPIInSendFrequency.setStatus("mandatory")
_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Type = Integer32
_SfpsVLANTopAgentPortTableAPIInRecvFrequency_Object = MibScalar
sfpsVLANTopAgentPortTableAPIInRecvFrequency = _SfpsVLANTopAgentPortTableAPIInRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3, 5),
    _SfpsVLANTopAgentPortTableAPIInRecvFrequency_Type()
)
sfpsVLANTopAgentPortTableAPIInRecvFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVLANTopAgentPortTableAPIInRecvFrequency.setStatus("mandatory")
_SfpsRATopAgentNeighborTable_Object = MibTable
sfpsRATopAgentNeighborTable = _SfpsRATopAgentNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborTable.setStatus("mandatory")
_SfpsRATopAgentNeighborEntry_Object = MibTableRow
sfpsRATopAgentNeighborEntry = _SfpsRATopAgentNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1)
)
sfpsRATopAgentNeighborEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRATopAgentNeighborInPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRATopAgentNeighborSwitchID"),
)
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborEntry.setStatus("mandatory")
_SfpsRATopAgentNeighborInPort_Type = Integer32
_SfpsRATopAgentNeighborInPort_Object = MibTableColumn
sfpsRATopAgentNeighborInPort = _SfpsRATopAgentNeighborInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 1),
    _SfpsRATopAgentNeighborInPort_Type()
)
sfpsRATopAgentNeighborInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborInPort.setStatus("mandatory")
_SfpsRATopAgentNeighborSwitchID_Type = OctetString
_SfpsRATopAgentNeighborSwitchID_Object = MibTableColumn
sfpsRATopAgentNeighborSwitchID = _SfpsRATopAgentNeighborSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 2),
    _SfpsRATopAgentNeighborSwitchID_Type()
)
sfpsRATopAgentNeighborSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborSwitchID.setStatus("mandatory")
_SfpsRATopAgentNeighborPriority_Type = Integer32
_SfpsRATopAgentNeighborPriority_Object = MibTableColumn
sfpsRATopAgentNeighborPriority = _SfpsRATopAgentNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 3),
    _SfpsRATopAgentNeighborPriority_Type()
)
sfpsRATopAgentNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborPriority.setStatus("mandatory")
_SfpsRATopAgentNeighborNetworkPort_Type = Integer32
_SfpsRATopAgentNeighborNetworkPort_Object = MibTableColumn
sfpsRATopAgentNeighborNetworkPort = _SfpsRATopAgentNeighborNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 4),
    _SfpsRATopAgentNeighborNetworkPort_Type()
)
sfpsRATopAgentNeighborNetworkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborNetworkPort.setStatus("mandatory")
_SfpsRATopAgentNeighborCallTag_Type = Integer32
_SfpsRATopAgentNeighborCallTag_Object = MibTableColumn
sfpsRATopAgentNeighborCallTag = _SfpsRATopAgentNeighborCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 5),
    _SfpsRATopAgentNeighborCallTag_Type()
)
sfpsRATopAgentNeighborCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborCallTag.setStatus("mandatory")
_SfpsRATopAgentNeighborNetHellosRcvd_Type = Integer32
_SfpsRATopAgentNeighborNetHellosRcvd_Object = MibTableColumn
sfpsRATopAgentNeighborNetHellosRcvd = _SfpsRATopAgentNeighborNetHellosRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 6),
    _SfpsRATopAgentNeighborNetHellosRcvd_Type()
)
sfpsRATopAgentNeighborNetHellosRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborNetHellosRcvd.setStatus("mandatory")
_SfpsRATopAgentNeighborSeqNumMismatch_Type = Integer32
_SfpsRATopAgentNeighborSeqNumMismatch_Object = MibTableColumn
sfpsRATopAgentNeighborSeqNumMismatch = _SfpsRATopAgentNeighborSeqNumMismatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 7),
    _SfpsRATopAgentNeighborSeqNumMismatch_Type()
)
sfpsRATopAgentNeighborSeqNumMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborSeqNumMismatch.setStatus("mandatory")
_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Type = Integer32
_SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Object = MibTableColumn
sfpsRATopAgentNeighborNetHelloAgeTimeOuts = _SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 8),
    _SfpsRATopAgentNeighborNetHelloAgeTimeOuts_Type()
)
sfpsRATopAgentNeighborNetHelloAgeTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborNetHelloAgeTimeOuts.setStatus("mandatory")
_SfpsRATopAgentNeighborNetHelloNetPortLosses_Type = Integer32
_SfpsRATopAgentNeighborNetHelloNetPortLosses_Object = MibTableColumn
sfpsRATopAgentNeighborNetHelloNetPortLosses = _SfpsRATopAgentNeighborNetHelloNetPortLosses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 9),
    _SfpsRATopAgentNeighborNetHelloNetPortLosses_Type()
)
sfpsRATopAgentNeighborNetHelloNetPortLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborNetHelloNetPortLosses.setStatus("mandatory")
_SfpsRATopAgentNeighborNetHelloNetPortChanges_Type = Integer32
_SfpsRATopAgentNeighborNetHelloNetPortChanges_Object = MibTableColumn
sfpsRATopAgentNeighborNetHelloNetPortChanges = _SfpsRATopAgentNeighborNetHelloNetPortChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 1, 1, 10),
    _SfpsRATopAgentNeighborNetHelloNetPortChanges_Type()
)
sfpsRATopAgentNeighborNetHelloNetPortChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentNeighborNetHelloNetPortChanges.setStatus("mandatory")
_SfpsRATopAgentPortTable_Object = MibTable
sfpsRATopAgentPortTable = _SfpsRATopAgentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTable.setStatus("mandatory")
_SfpsRATopAgentPortEntry_Object = MibTableRow
sfpsRATopAgentPortEntry = _SfpsRATopAgentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1)
)
sfpsRATopAgentPortEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRATopAgentPortLogicalPort"),
)
if mibBuilder.loadTexts:
    sfpsRATopAgentPortEntry.setStatus("mandatory")
_SfpsRATopAgentPortLogicalPort_Type = Integer32
_SfpsRATopAgentPortLogicalPort_Object = MibTableColumn
sfpsRATopAgentPortLogicalPort = _SfpsRATopAgentPortLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 1),
    _SfpsRATopAgentPortLogicalPort_Type()
)
sfpsRATopAgentPortLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortLogicalPort.setStatus("mandatory")


class _SfpsRATopAgentPortHelloVersion_Type(Integer32):
    """Custom type sfpsRATopAgentPortHelloVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_SfpsRATopAgentPortHelloVersion_Type.__name__ = "Integer32"
_SfpsRATopAgentPortHelloVersion_Object = MibTableColumn
sfpsRATopAgentPortHelloVersion = _SfpsRATopAgentPortHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 2),
    _SfpsRATopAgentPortHelloVersion_Type()
)
sfpsRATopAgentPortHelloVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortHelloVersion.setStatus("mandatory")
_SfpsRATopAgentPortSendFrequency_Type = Integer32
_SfpsRATopAgentPortSendFrequency_Object = MibTableColumn
sfpsRATopAgentPortSendFrequency = _SfpsRATopAgentPortSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 3),
    _SfpsRATopAgentPortSendFrequency_Type()
)
sfpsRATopAgentPortSendFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortSendFrequency.setStatus("mandatory")
_SfpsRATopAgentPortRecvFrequency_Type = Integer32
_SfpsRATopAgentPortRecvFrequency_Object = MibTableColumn
sfpsRATopAgentPortRecvFrequency = _SfpsRATopAgentPortRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 4),
    _SfpsRATopAgentPortRecvFrequency_Type()
)
sfpsRATopAgentPortRecvFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortRecvFrequency.setStatus("mandatory")
_SfpsRATopAgentPortPriority_Type = Integer32
_SfpsRATopAgentPortPriority_Object = MibTableColumn
sfpsRATopAgentPortPriority = _SfpsRATopAgentPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 5),
    _SfpsRATopAgentPortPriority_Type()
)
sfpsRATopAgentPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortPriority.setStatus("mandatory")


class _SfpsRATopAgentPortPortState_Type(Integer32):
    """Custom type sfpsRATopAgentPortPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("added", 1),
          ("backup", 5),
          ("backupWait", 9),
          ("deleted", 8),
          ("down", 6),
          ("halted", 7),
          ("init", 2),
          ("poised", 3),
          ("primary", 4))
    )


_SfpsRATopAgentPortPortState_Type.__name__ = "Integer32"
_SfpsRATopAgentPortPortState_Object = MibTableColumn
sfpsRATopAgentPortPortState = _SfpsRATopAgentPortPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 6),
    _SfpsRATopAgentPortPortState_Type()
)
sfpsRATopAgentPortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortPortState.setStatus("mandatory")
_SfpsRATopAgentPortPrimarySwitch_Type = SfpsAddress
_SfpsRATopAgentPortPrimarySwitch_Object = MibTableColumn
sfpsRATopAgentPortPrimarySwitch = _SfpsRATopAgentPortPrimarySwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 7),
    _SfpsRATopAgentPortPrimarySwitch_Type()
)
sfpsRATopAgentPortPrimarySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortPrimarySwitch.setStatus("mandatory")
_SfpsRATopAgentPortNetHelloRecvFreq_Type = Integer32
_SfpsRATopAgentPortNetHelloRecvFreq_Object = MibTableColumn
sfpsRATopAgentPortNetHelloRecvFreq = _SfpsRATopAgentPortNetHelloRecvFreq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 8),
    _SfpsRATopAgentPortNetHelloRecvFreq_Type()
)
sfpsRATopAgentPortNetHelloRecvFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortNetHelloRecvFreq.setStatus("mandatory")
_SfpsRATopAgentPortStateChangeCount_Type = Integer32
_SfpsRATopAgentPortStateChangeCount_Object = MibTableColumn
sfpsRATopAgentPortStateChangeCount = _SfpsRATopAgentPortStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 9),
    _SfpsRATopAgentPortStateChangeCount_Type()
)
sfpsRATopAgentPortStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortStateChangeCount.setStatus("mandatory")


class _SfpsRATopAgentPortNVRAMStatus_Type(Integer32):
    """Custom type sfpsRATopAgentPortNVRAMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_SfpsRATopAgentPortNVRAMStatus_Type.__name__ = "Integer32"
_SfpsRATopAgentPortNVRAMStatus_Object = MibTableColumn
sfpsRATopAgentPortNVRAMStatus = _SfpsRATopAgentPortNVRAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 2, 1, 10),
    _SfpsRATopAgentPortNVRAMStatus_Type()
)
sfpsRATopAgentPortNVRAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortNVRAMStatus.setStatus("mandatory")


class _SfpsRATopAgentPortTableAPIInVerb_Type(Integer32):
    """Custom type sfpsRATopAgentPortTableAPIInVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("getPortInfo", 3),
          ("other", 1))
    )


_SfpsRATopAgentPortTableAPIInVerb_Type.__name__ = "Integer32"
_SfpsRATopAgentPortTableAPIInVerb_Object = MibScalar
sfpsRATopAgentPortTableAPIInVerb = _SfpsRATopAgentPortTableAPIInVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 1),
    _SfpsRATopAgentPortTableAPIInVerb_Type()
)
sfpsRATopAgentPortTableAPIInVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInVerb.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInLogicalPort_Type = Integer32
_SfpsRATopAgentPortTableAPIInLogicalPort_Object = MibScalar
sfpsRATopAgentPortTableAPIInLogicalPort = _SfpsRATopAgentPortTableAPIInLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 2),
    _SfpsRATopAgentPortTableAPIInLogicalPort_Type()
)
sfpsRATopAgentPortTableAPIInLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInLogicalPort.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInHelloVersion_Type = Integer32
_SfpsRATopAgentPortTableAPIInHelloVersion_Object = MibScalar
sfpsRATopAgentPortTableAPIInHelloVersion = _SfpsRATopAgentPortTableAPIInHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 3),
    _SfpsRATopAgentPortTableAPIInHelloVersion_Type()
)
sfpsRATopAgentPortTableAPIInHelloVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInHelloVersion.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInSendFrequency_Type = Integer32
_SfpsRATopAgentPortTableAPIInSendFrequency_Object = MibScalar
sfpsRATopAgentPortTableAPIInSendFrequency = _SfpsRATopAgentPortTableAPIInSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 4),
    _SfpsRATopAgentPortTableAPIInSendFrequency_Type()
)
sfpsRATopAgentPortTableAPIInSendFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInSendFrequency.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInRecvFrequency_Type = Integer32
_SfpsRATopAgentPortTableAPIInRecvFrequency_Object = MibScalar
sfpsRATopAgentPortTableAPIInRecvFrequency = _SfpsRATopAgentPortTableAPIInRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 5),
    _SfpsRATopAgentPortTableAPIInRecvFrequency_Type()
)
sfpsRATopAgentPortTableAPIInRecvFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInRecvFrequency.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInPriority_Type = Integer32
_SfpsRATopAgentPortTableAPIInPriority_Object = MibScalar
sfpsRATopAgentPortTableAPIInPriority = _SfpsRATopAgentPortTableAPIInPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 6),
    _SfpsRATopAgentPortTableAPIInPriority_Type()
)
sfpsRATopAgentPortTableAPIInPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInPriority.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Type = Integer32
_SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Object = MibScalar
sfpsRATopAgentPortTableAPIInNetHelloRecvFreq = _SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3, 7),
    _SfpsRATopAgentPortTableAPIInNetHelloRecvFreq_Type()
)
sfpsRATopAgentPortTableAPIInNetHelloRecvFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIInNetHelloRecvFreq.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutLogicalPort_Type = Integer32
_SfpsRATopAgentPortTableAPIOutLogicalPort_Object = MibScalar
sfpsRATopAgentPortTableAPIOutLogicalPort = _SfpsRATopAgentPortTableAPIOutLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 1),
    _SfpsRATopAgentPortTableAPIOutLogicalPort_Type()
)
sfpsRATopAgentPortTableAPIOutLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutLogicalPort.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutHelloVersion_Type = Integer32
_SfpsRATopAgentPortTableAPIOutHelloVersion_Object = MibScalar
sfpsRATopAgentPortTableAPIOutHelloVersion = _SfpsRATopAgentPortTableAPIOutHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 2),
    _SfpsRATopAgentPortTableAPIOutHelloVersion_Type()
)
sfpsRATopAgentPortTableAPIOutHelloVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutHelloVersion.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutSendFrequency_Type = Integer32
_SfpsRATopAgentPortTableAPIOutSendFrequency_Object = MibScalar
sfpsRATopAgentPortTableAPIOutSendFrequency = _SfpsRATopAgentPortTableAPIOutSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 3),
    _SfpsRATopAgentPortTableAPIOutSendFrequency_Type()
)
sfpsRATopAgentPortTableAPIOutSendFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutSendFrequency.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutRecvFrequency_Type = Integer32
_SfpsRATopAgentPortTableAPIOutRecvFrequency_Object = MibScalar
sfpsRATopAgentPortTableAPIOutRecvFrequency = _SfpsRATopAgentPortTableAPIOutRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 4),
    _SfpsRATopAgentPortTableAPIOutRecvFrequency_Type()
)
sfpsRATopAgentPortTableAPIOutRecvFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutRecvFrequency.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutPriority_Type = Integer32
_SfpsRATopAgentPortTableAPIOutPriority_Object = MibScalar
sfpsRATopAgentPortTableAPIOutPriority = _SfpsRATopAgentPortTableAPIOutPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 5),
    _SfpsRATopAgentPortTableAPIOutPriority_Type()
)
sfpsRATopAgentPortTableAPIOutPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutPriority.setStatus("mandatory")


class _SfpsRATopAgentPortTableAPIOutPortState_Type(Integer32):
    """Custom type sfpsRATopAgentPortTableAPIOutPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("added", 1),
          ("backup", 5),
          ("backupWait", 9),
          ("deleted", 8),
          ("down", 6),
          ("halted", 7),
          ("init", 2),
          ("poised", 3),
          ("primary", 4))
    )


_SfpsRATopAgentPortTableAPIOutPortState_Type.__name__ = "Integer32"
_SfpsRATopAgentPortTableAPIOutPortState_Object = MibScalar
sfpsRATopAgentPortTableAPIOutPortState = _SfpsRATopAgentPortTableAPIOutPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 6),
    _SfpsRATopAgentPortTableAPIOutPortState_Type()
)
sfpsRATopAgentPortTableAPIOutPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutPortState.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Type = SfpsAddress
_SfpsRATopAgentPortTableAPIOutPrimarySwitch_Object = MibScalar
sfpsRATopAgentPortTableAPIOutPrimarySwitch = _SfpsRATopAgentPortTableAPIOutPrimarySwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 7),
    _SfpsRATopAgentPortTableAPIOutPrimarySwitch_Type()
)
sfpsRATopAgentPortTableAPIOutPrimarySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutPrimarySwitch.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Type = Integer32
_SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Object = MibScalar
sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq = _SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 8),
    _SfpsRATopAgentPortTableAPIOutNetHelloRecvFreq_Type()
)
sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq.setStatus("mandatory")
_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Type = Integer32
_SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Object = MibScalar
sfpsRATopAgentPortTableAPIOutPortStateChangeCount = _SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4, 9),
    _SfpsRATopAgentPortTableAPIOutPortStateChangeCount_Type()
)
sfpsRATopAgentPortTableAPIOutPortStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRATopAgentPortTableAPIOutPortStateChangeCount.setStatus("mandatory")
_SfpsESPTopAgentPortTable_Object = MibTable
sfpsESPTopAgentPortTable = _SfpsESPTopAgentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2)
)
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortTable.setStatus("mandatory")
_SfpsESPTopAgentPortEntry_Object = MibTableRow
sfpsESPTopAgentPortEntry = _SfpsESPTopAgentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2, 1)
)
sfpsESPTopAgentPortEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsESPTopAgentPortPort"),
)
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortEntry.setStatus("mandatory")
_SfpsESPTopAgentPortPort_Type = Integer32
_SfpsESPTopAgentPortPort_Object = MibTableColumn
sfpsESPTopAgentPortPort = _SfpsESPTopAgentPortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2, 1, 1),
    _SfpsESPTopAgentPortPort_Type()
)
sfpsESPTopAgentPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortPort.setStatus("mandatory")


class _SfpsESPTopAgentPortHelloVersion_Type(Integer32):
    """Custom type sfpsESPTopAgentPortHelloVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version2", 2),
          ("version3", 3),
          ("version4", 4),
          ("versionOther", 1))
    )


_SfpsESPTopAgentPortHelloVersion_Type.__name__ = "Integer32"
_SfpsESPTopAgentPortHelloVersion_Object = MibTableColumn
sfpsESPTopAgentPortHelloVersion = _SfpsESPTopAgentPortHelloVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2, 1, 2),
    _SfpsESPTopAgentPortHelloVersion_Type()
)
sfpsESPTopAgentPortHelloVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortHelloVersion.setStatus("mandatory")
_SfpsESPTopAgentPortSendFrequency_Type = Integer32
_SfpsESPTopAgentPortSendFrequency_Object = MibTableColumn
sfpsESPTopAgentPortSendFrequency = _SfpsESPTopAgentPortSendFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2, 1, 3),
    _SfpsESPTopAgentPortSendFrequency_Type()
)
sfpsESPTopAgentPortSendFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortSendFrequency.setStatus("mandatory")
_SfpsESPTopAgentPortRecvFrequency_Type = Integer32
_SfpsESPTopAgentPortRecvFrequency_Object = MibTableColumn
sfpsESPTopAgentPortRecvFrequency = _SfpsESPTopAgentPortRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3, 2, 1, 4),
    _SfpsESPTopAgentPortRecvFrequency_Type()
)
sfpsESPTopAgentPortRecvFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsESPTopAgentPortRecvFrequency.setStatus("mandatory")
_SfpsVMTopServerDeltaTable_Object = MibTable
sfpsVMTopServerDeltaTable = _SfpsVMTopServerDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaTable.setStatus("mandatory")
_SfpsVMTopServerDeltaEntry_Object = MibTableRow
sfpsVMTopServerDeltaEntry = _SfpsVMTopServerDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1)
)
sfpsVMTopServerDeltaEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsVMTopServerDeltaIndex"),
)
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaEntry.setStatus("mandatory")
_SfpsVMTopServerDeltaIndex_Type = Integer32
_SfpsVMTopServerDeltaIndex_Object = MibTableColumn
sfpsVMTopServerDeltaIndex = _SfpsVMTopServerDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 1),
    _SfpsVMTopServerDeltaIndex_Type()
)
sfpsVMTopServerDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaIndex.setStatus("mandatory")
_SfpsVMTopServerDeltaInPort_Type = Integer32
_SfpsVMTopServerDeltaInPort_Object = MibTableColumn
sfpsVMTopServerDeltaInPort = _SfpsVMTopServerDeltaInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 2),
    _SfpsVMTopServerDeltaInPort_Type()
)
sfpsVMTopServerDeltaInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaInPort.setStatus("mandatory")
_SfpsVMTopServerDeltaSwitchID_Type = DisplayString
_SfpsVMTopServerDeltaSwitchID_Object = MibTableColumn
sfpsVMTopServerDeltaSwitchID = _SfpsVMTopServerDeltaSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 3),
    _SfpsVMTopServerDeltaSwitchID_Type()
)
sfpsVMTopServerDeltaSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaSwitchID.setStatus("mandatory")


class _SfpsVMTopServerDeltaState_Type(Integer32):
    """Custom type sfpsVMTopServerDeltaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("added", 2),
          ("deleted", 3),
          ("other", 1))
    )


_SfpsVMTopServerDeltaState_Type.__name__ = "Integer32"
_SfpsVMTopServerDeltaState_Object = MibTableColumn
sfpsVMTopServerDeltaState = _SfpsVMTopServerDeltaState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 4),
    _SfpsVMTopServerDeltaState_Type()
)
sfpsVMTopServerDeltaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaState.setStatus("mandatory")
_SfpsVMTopServerDeltaIPAddress_Type = IpAddress
_SfpsVMTopServerDeltaIPAddress_Object = MibTableColumn
sfpsVMTopServerDeltaIPAddress = _SfpsVMTopServerDeltaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 5),
    _SfpsVMTopServerDeltaIPAddress_Type()
)
sfpsVMTopServerDeltaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaIPAddress.setStatus("mandatory")
_SfpsVMTopServerDeltaAgent_Type = DisplayString
_SfpsVMTopServerDeltaAgent_Object = MibTableColumn
sfpsVMTopServerDeltaAgent = _SfpsVMTopServerDeltaAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 1, 1, 6),
    _SfpsVMTopServerDeltaAgent_Type()
)
sfpsVMTopServerDeltaAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaAgent.setStatus("mandatory")
_SfpsVMTopServerDeltaCount_Type = Integer32
_SfpsVMTopServerDeltaCount_Object = MibScalar
sfpsVMTopServerDeltaCount = _SfpsVMTopServerDeltaCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 2),
    _SfpsVMTopServerDeltaCount_Type()
)
sfpsVMTopServerDeltaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerDeltaCount.setStatus("mandatory")


class _SfpsVMTopServerTableLock_Type(Integer32):
    """Custom type sfpsVMTopServerTableLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_SfpsVMTopServerTableLock_Type.__name__ = "Integer32"
_SfpsVMTopServerTableLock_Object = MibScalar
sfpsVMTopServerTableLock = _SfpsVMTopServerTableLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 3),
    _SfpsVMTopServerTableLock_Type()
)
sfpsVMTopServerTableLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVMTopServerTableLock.setStatus("mandatory")


class _SfpsVMTopServerPortChange_Type(Integer32):
    """Custom type sfpsVMTopServerPortChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPortChange", 1),
          ("portChange", 2))
    )


_SfpsVMTopServerPortChange_Type.__name__ = "Integer32"
_SfpsVMTopServerPortChange_Object = MibScalar
sfpsVMTopServerPortChange = _SfpsVMTopServerPortChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 4),
    _SfpsVMTopServerPortChange_Type()
)
sfpsVMTopServerPortChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerPortChange.setStatus("mandatory")


class _SfpsVMTopServerTableFull_Type(Integer32):
    """Custom type sfpsVMTopServerTableFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tableFull", 1),
          ("tableNotFull", 2))
    )


_SfpsVMTopServerTableFull_Type.__name__ = "Integer32"
_SfpsVMTopServerTableFull_Object = MibScalar
sfpsVMTopServerTableFull = _SfpsVMTopServerTableFull_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 5),
    _SfpsVMTopServerTableFull_Type()
)
sfpsVMTopServerTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVMTopServerTableFull.setStatus("mandatory")
_SfpsVMTopServerChangeCnt_Type = Integer32
_SfpsVMTopServerChangeCnt_Object = MibScalar
sfpsVMTopServerChangeCnt = _SfpsVMTopServerChangeCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1, 6),
    _SfpsVMTopServerChangeCnt_Type()
)
sfpsVMTopServerChangeCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVMTopServerChangeCnt.setStatus("mandatory")


class _SfpsTAPITestInVerb_Type(Integer32):
    """Custom type sfpsTAPITestInVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("changePortAccess", 5),
          ("disableAccessPortOnly", 17),
          ("enableAccessPortOnly", 16),
          ("getLogicalINBNetworkPortMask", 14),
          ("getLogicalNetworkPortMask", 11),
          ("getLogicalSameFCLPortMask", 19),
          ("getNeighborFCL", 20),
          ("getPhysicalINBNetworkPortMask", 15),
          ("getPhysicalNetworkPortMask", 12),
          ("getPhysicalPortDownPortMask", 18),
          ("getPhysicalStandByPortMask", 13),
          ("getPortNeighbors", 9),
          ("getTotalNeighbors", 10),
          ("other", 1),
          ("portDown", 4),
          ("portUp", 3),
          ("resolveBaseMACToPorts", 7),
          ("resolveINBNeighbor", 8),
          ("resolvePortNameToPort", 6))
    )


_SfpsTAPITestInVerb_Type.__name__ = "Integer32"
_SfpsTAPITestInVerb_Object = MibScalar
sfpsTAPITestInVerb = _SfpsTAPITestInVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 1),
    _SfpsTAPITestInVerb_Type()
)
sfpsTAPITestInVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInVerb.setStatus("mandatory")
_SfpsTAPITestInLogicalPort_Type = Integer32
_SfpsTAPITestInLogicalPort_Object = MibScalar
sfpsTAPITestInLogicalPort = _SfpsTAPITestInLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 2),
    _SfpsTAPITestInLogicalPort_Type()
)
sfpsTAPITestInLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInLogicalPort.setStatus("mandatory")
_SfpsTAPITestInSwitchID_Type = DisplayString
_SfpsTAPITestInSwitchID_Object = MibScalar
sfpsTAPITestInSwitchID = _SfpsTAPITestInSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 3),
    _SfpsTAPITestInSwitchID_Type()
)
sfpsTAPITestInSwitchID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInSwitchID.setStatus("mandatory")
_SfpsTAPITestInMAC_Type = DisplayString
_SfpsTAPITestInMAC_Object = MibScalar
sfpsTAPITestInMAC = _SfpsTAPITestInMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 4),
    _SfpsTAPITestInMAC_Type()
)
sfpsTAPITestInMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInMAC.setStatus("mandatory")


class _SfpsTAPITestInPortTypeState_Type(Integer32):
    """Custom type sfpsTAPITestInPortTypeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgmt", 4),
          ("hybrid", 8),
          ("network", 3),
          ("networkOnly", 10),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsTAPITestInPortTypeState_Type.__name__ = "Integer32"
_SfpsTAPITestInPortTypeState_Object = MibScalar
sfpsTAPITestInPortTypeState = _SfpsTAPITestInPortTypeState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 5),
    _SfpsTAPITestInPortTypeState_Type()
)
sfpsTAPITestInPortTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInPortTypeState.setStatus("mandatory")
_SfpsTAPITestInTopologyAgentID_Type = Integer32
_SfpsTAPITestInTopologyAgentID_Object = MibScalar
sfpsTAPITestInTopologyAgentID = _SfpsTAPITestInTopologyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 6),
    _SfpsTAPITestInTopologyAgentID_Type()
)
sfpsTAPITestInTopologyAgentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInTopologyAgentID.setStatus("mandatory")
_SfpsTAPITestInUNIT321_Type = Integer32
_SfpsTAPITestInUNIT321_Object = MibScalar
sfpsTAPITestInUNIT321 = _SfpsTAPITestInUNIT321_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1, 7),
    _SfpsTAPITestInUNIT321_Type()
)
sfpsTAPITestInUNIT321.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestInUNIT321.setStatus("mandatory")
_SfpsTAPITestOutOutputInteger_Type = Integer32
_SfpsTAPITestOutOutputInteger_Object = MibScalar
sfpsTAPITestOutOutputInteger = _SfpsTAPITestOutOutputInteger_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 2, 1),
    _SfpsTAPITestOutOutputInteger_Type()
)
sfpsTAPITestOutOutputInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestOutOutputInteger.setStatus("mandatory")
_SfpsTAPITestOutOutPutString_Type = DisplayString
_SfpsTAPITestOutOutPutString_Object = MibScalar
sfpsTAPITestOutOutPutString = _SfpsTAPITestOutOutPutString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 2, 2),
    _SfpsTAPITestOutOutPutString_Type()
)
sfpsTAPITestOutOutPutString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTAPITestOutOutPutString.setStatus("mandatory")


class _SfpsTopologyServerTestInVerb_Type(Integer32):
    """Custom type sfpsTopologyServerTestInVerb based on Integer32"""
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
        *(("add", 2),
          ("clear", 3),
          ("foundEvent", 5),
          ("lostEvent", 4),
          ("other", 1),
          ("portEvent", 6))
    )


_SfpsTopologyServerTestInVerb_Type.__name__ = "Integer32"
_SfpsTopologyServerTestInVerb_Object = MibScalar
sfpsTopologyServerTestInVerb = _SfpsTopologyServerTestInVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 1, 1),
    _SfpsTopologyServerTestInVerb_Type()
)
sfpsTopologyServerTestInVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestInVerb.setStatus("mandatory")
_SfpsTopologyServerTestInServer_Type = DisplayString
_SfpsTopologyServerTestInServer_Object = MibScalar
sfpsTopologyServerTestInServer = _SfpsTopologyServerTestInServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 1, 2),
    _SfpsTopologyServerTestInServer_Type()
)
sfpsTopologyServerTestInServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestInServer.setStatus("mandatory")
_SfpsTopologyServerTestInNumberOfRelays_Type = Integer32
_SfpsTopologyServerTestInNumberOfRelays_Object = MibScalar
sfpsTopologyServerTestInNumberOfRelays = _SfpsTopologyServerTestInNumberOfRelays_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 1, 3),
    _SfpsTopologyServerTestInNumberOfRelays_Type()
)
sfpsTopologyServerTestInNumberOfRelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestInNumberOfRelays.setStatus("mandatory")
_SfpsTopologyServerTestTable_Object = MibTable
sfpsTopologyServerTestTable = _SfpsTopologyServerTestTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2)
)
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTable.setStatus("mandatory")
_SfpsTopologyServerTestEntry_Object = MibTableRow
sfpsTopologyServerTestEntry = _SfpsTopologyServerTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1)
)
sfpsTopologyServerTestEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsTopologyServerTestRelayNumber"),
)
if mibBuilder.loadTexts:
    sfpsTopologyServerTestEntry.setStatus("mandatory")
_SfpsTopologyServerTestRelayNumber_Type = Integer32
_SfpsTopologyServerTestRelayNumber_Object = MibTableColumn
sfpsTopologyServerTestRelayNumber = _SfpsTopologyServerTestRelayNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 1),
    _SfpsTopologyServerTestRelayNumber_Type()
)
sfpsTopologyServerTestRelayNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestRelayNumber.setStatus("mandatory")


class _SfpsTopologyServerTestServerFlavor_Type(Integer32):
    """Custom type sfpsTopologyServerTestServerFlavor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 2),
          ("vns", 1))
    )


_SfpsTopologyServerTestServerFlavor_Type.__name__ = "Integer32"
_SfpsTopologyServerTestServerFlavor_Object = MibTableColumn
sfpsTopologyServerTestServerFlavor = _SfpsTopologyServerTestServerFlavor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 2),
    _SfpsTopologyServerTestServerFlavor_Type()
)
sfpsTopologyServerTestServerFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestServerFlavor.setStatus("mandatory")
_SfpsTopologyServerTestPortNumber_Type = Integer32
_SfpsTopologyServerTestPortNumber_Object = MibTableColumn
sfpsTopologyServerTestPortNumber = _SfpsTopologyServerTestPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 3),
    _SfpsTopologyServerTestPortNumber_Type()
)
sfpsTopologyServerTestPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestPortNumber.setStatus("mandatory")
_SfpsTopologyServerTestPortName_Type = DisplayString
_SfpsTopologyServerTestPortName_Object = MibTableColumn
sfpsTopologyServerTestPortName = _SfpsTopologyServerTestPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 4),
    _SfpsTopologyServerTestPortName_Type()
)
sfpsTopologyServerTestPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestPortName.setStatus("mandatory")
_SfpsTopologyServerTestIpAddr_Type = DisplayString
_SfpsTopologyServerTestIpAddr_Object = MibTableColumn
sfpsTopologyServerTestIpAddr = _SfpsTopologyServerTestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 5),
    _SfpsTopologyServerTestIpAddr_Type()
)
sfpsTopologyServerTestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestIpAddr.setStatus("mandatory")


class _SfpsTopologyServerTestLostPort_Type(Integer32):
    """Custom type sfpsTopologyServerTestLostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsTopologyServerTestLostPort_Type.__name__ = "Integer32"
_SfpsTopologyServerTestLostPort_Object = MibTableColumn
sfpsTopologyServerTestLostPort = _SfpsTopologyServerTestLostPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 6),
    _SfpsTopologyServerTestLostPort_Type()
)
sfpsTopologyServerTestLostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestLostPort.setStatus("mandatory")


class _SfpsTopologyServerTestOldState_Type(Integer32):
    """Custom type sfpsTopologyServerTestOldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgmt", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsTopologyServerTestOldState_Type.__name__ = "Integer32"
_SfpsTopologyServerTestOldState_Object = MibTableColumn
sfpsTopologyServerTestOldState = _SfpsTopologyServerTestOldState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 7),
    _SfpsTopologyServerTestOldState_Type()
)
sfpsTopologyServerTestOldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestOldState.setStatus("mandatory")


class _SfpsTopologyServerTestNewState_Type(Integer32):
    """Custom type sfpsTopologyServerTestNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostCtrl", 5),
          ("hostMgmt", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsTopologyServerTestNewState_Type.__name__ = "Integer32"
_SfpsTopologyServerTestNewState_Object = MibTableColumn
sfpsTopologyServerTestNewState = _SfpsTopologyServerTestNewState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 8),
    _SfpsTopologyServerTestNewState_Type()
)
sfpsTopologyServerTestNewState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestNewState.setStatus("mandatory")
_SfpsTopologyServerTestTopologyAgent_Type = DisplayString
_SfpsTopologyServerTestTopologyAgent_Object = MibTableColumn
sfpsTopologyServerTestTopologyAgent = _SfpsTopologyServerTestTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 2, 1, 9),
    _SfpsTopologyServerTestTopologyAgent_Type()
)
sfpsTopologyServerTestTopologyAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopologyAgent.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayTable_Object = MibTable
sfpsTopologyServerTestTopRelayTable = _SfpsTopologyServerTestTopRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3)
)
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayTable.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayEntry_Object = MibTableRow
sfpsTopologyServerTestTopRelayEntry = _SfpsTopologyServerTestTopRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1)
)
sfpsTopologyServerTestTopRelayEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsTopologyServerTestTopRelayRelayNumber"),
)
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayEntry.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayRelayNumber_Type = Integer32
_SfpsTopologyServerTestTopRelayRelayNumber_Object = MibTableColumn
sfpsTopologyServerTestTopRelayRelayNumber = _SfpsTopologyServerTestTopRelayRelayNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 1),
    _SfpsTopologyServerTestTopRelayRelayNumber_Type()
)
sfpsTopologyServerTestTopRelayRelayNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayRelayNumber.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayEvent_Type = Integer32
_SfpsTopologyServerTestTopRelayEvent_Object = MibTableColumn
sfpsTopologyServerTestTopRelayEvent = _SfpsTopologyServerTestTopRelayEvent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 2),
    _SfpsTopologyServerTestTopRelayEvent_Type()
)
sfpsTopologyServerTestTopRelayEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayEvent.setStatus("mandatory")


class _SfpsTopologyServerTestTopRelayDeltaOptions_Type(Integer32):
    """Custom type sfpsTopologyServerTestTopRelayDeltaOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("agingNghLoss", 4),
          ("crossedPortNghLoss", 9),
          ("duplicateNghLoss", 6),
          ("foundNeighbor", 1),
          ("functionalLevelNghLoss", 10),
          ("loopedPortNghLoss", 8),
          ("optionsGain", 2),
          ("optionsLoss", 3),
          ("portDownNghLoss", 5),
          ("subtractPortNghLoss", 7),
          ("twoWayCommLoss", 12),
          ("versionedPortNghLoss", 11))
    )


_SfpsTopologyServerTestTopRelayDeltaOptions_Type.__name__ = "Integer32"
_SfpsTopologyServerTestTopRelayDeltaOptions_Object = MibTableColumn
sfpsTopologyServerTestTopRelayDeltaOptions = _SfpsTopologyServerTestTopRelayDeltaOptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 3),
    _SfpsTopologyServerTestTopRelayDeltaOptions_Type()
)
sfpsTopologyServerTestTopRelayDeltaOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayDeltaOptions.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayCurrentOptions_Type = Integer32
_SfpsTopologyServerTestTopRelayCurrentOptions_Object = MibTableColumn
sfpsTopologyServerTestTopRelayCurrentOptions = _SfpsTopologyServerTestTopRelayCurrentOptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 4),
    _SfpsTopologyServerTestTopRelayCurrentOptions_Type()
)
sfpsTopologyServerTestTopRelayCurrentOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayCurrentOptions.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayLogicalPort_Type = Integer32
_SfpsTopologyServerTestTopRelayLogicalPort_Object = MibTableColumn
sfpsTopologyServerTestTopRelayLogicalPort = _SfpsTopologyServerTestTopRelayLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 5),
    _SfpsTopologyServerTestTopRelayLogicalPort_Type()
)
sfpsTopologyServerTestTopRelayLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayLogicalPort.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayPortName_Type = OctetString
_SfpsTopologyServerTestTopRelayPortName_Object = MibTableColumn
sfpsTopologyServerTestTopRelayPortName = _SfpsTopologyServerTestTopRelayPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 6),
    _SfpsTopologyServerTestTopRelayPortName_Type()
)
sfpsTopologyServerTestTopRelayPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayPortName.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayIPAddr_Type = IpAddress
_SfpsTopologyServerTestTopRelayIPAddr_Object = MibTableColumn
sfpsTopologyServerTestTopRelayIPAddr = _SfpsTopologyServerTestTopRelayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 7),
    _SfpsTopologyServerTestTopRelayIPAddr_Type()
)
sfpsTopologyServerTestTopRelayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayIPAddr.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayChassisMAC_Type = SfpsAddress
_SfpsTopologyServerTestTopRelayChassisMAC_Object = MibTableColumn
sfpsTopologyServerTestTopRelayChassisMAC = _SfpsTopologyServerTestTopRelayChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 8),
    _SfpsTopologyServerTestTopRelayChassisMAC_Type()
)
sfpsTopologyServerTestTopRelayChassisMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayChassisMAC.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayChassisIP_Type = IpAddress
_SfpsTopologyServerTestTopRelayChassisIP_Object = MibTableColumn
sfpsTopologyServerTestTopRelayChassisIP = _SfpsTopologyServerTestTopRelayChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 9),
    _SfpsTopologyServerTestTopRelayChassisIP_Type()
)
sfpsTopologyServerTestTopRelayChassisIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayChassisIP.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayFLevel_Type = Integer32
_SfpsTopologyServerTestTopRelayFLevel_Object = MibTableColumn
sfpsTopologyServerTestTopRelayFLevel = _SfpsTopologyServerTestTopRelayFLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 10),
    _SfpsTopologyServerTestTopRelayFLevel_Type()
)
sfpsTopologyServerTestTopRelayFLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayFLevel.setStatus("mandatory")
_SfpsTopologyServerTestTopRelayTopologyAgent_Type = OctetString
_SfpsTopologyServerTestTopRelayTopologyAgent_Object = MibTableColumn
sfpsTopologyServerTestTopRelayTopologyAgent = _SfpsTopologyServerTestTopRelayTopologyAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 3, 1, 11),
    _SfpsTopologyServerTestTopRelayTopologyAgent_Type()
)
sfpsTopologyServerTestTopRelayTopologyAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerTestTopRelayTopologyAgent.setStatus("mandatory")
_SfpsTopologyServerPortEventRelayLogicalPort_Type = Integer32
_SfpsTopologyServerPortEventRelayLogicalPort_Object = MibScalar
sfpsTopologyServerPortEventRelayLogicalPort = _SfpsTopologyServerPortEventRelayLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 4, 1),
    _SfpsTopologyServerPortEventRelayLogicalPort_Type()
)
sfpsTopologyServerPortEventRelayLogicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerPortEventRelayLogicalPort.setStatus("mandatory")


class _SfpsTopologyServerPortEventRelayOldState_Type(Integer32):
    """Custom type sfpsTopologyServerPortEventRelayOldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAcces", 7),
          ("hostCtrl", 5),
          ("hostMgmt", 4),
          ("network", 3),
          ("networkOnly", 10),
          ("other", 1),
          ("standBy", 8),
          ("unknown", 6))
    )


_SfpsTopologyServerPortEventRelayOldState_Type.__name__ = "Integer32"
_SfpsTopologyServerPortEventRelayOldState_Object = MibScalar
sfpsTopologyServerPortEventRelayOldState = _SfpsTopologyServerPortEventRelayOldState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 4, 2),
    _SfpsTopologyServerPortEventRelayOldState_Type()
)
sfpsTopologyServerPortEventRelayOldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerPortEventRelayOldState.setStatus("mandatory")


class _SfpsTopologyServerPortEventRelayNewState_Type(Integer32):
    """Custom type sfpsTopologyServerPortEventRelayNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAcces", 7),
          ("hostCtrl", 5),
          ("hostMgmt", 4),
          ("network", 3),
          ("networkOnly", 10),
          ("other", 1),
          ("standBy", 8),
          ("unknown", 6))
    )


_SfpsTopologyServerPortEventRelayNewState_Type.__name__ = "Integer32"
_SfpsTopologyServerPortEventRelayNewState_Object = MibScalar
sfpsTopologyServerPortEventRelayNewState = _SfpsTopologyServerPortEventRelayNewState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 4, 3),
    _SfpsTopologyServerPortEventRelayNewState_Type()
)
sfpsTopologyServerPortEventRelayNewState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTopologyServerPortEventRelayNewState.setStatus("mandatory")
_SfpsNeighborEventsFoundEvents_Type = Integer32
_SfpsNeighborEventsFoundEvents_Object = MibScalar
sfpsNeighborEventsFoundEvents = _SfpsNeighborEventsFoundEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 6, 1, 1),
    _SfpsNeighborEventsFoundEvents_Type()
)
sfpsNeighborEventsFoundEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNeighborEventsFoundEvents.setStatus("mandatory")
_SfpsNeighborEventsLostEvents_Type = Integer32
_SfpsNeighborEventsLostEvents_Object = MibScalar
sfpsNeighborEventsLostEvents = _SfpsNeighborEventsLostEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 6, 1, 2),
    _SfpsNeighborEventsLostEvents_Type()
)
sfpsNeighborEventsLostEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNeighborEventsLostEvents.setStatus("mandatory")
_SfpsTopologyFCLTable_Object = MibTable
sfpsTopologyFCLTable = _SfpsTopologyFCLTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1)
)
if mibBuilder.loadTexts:
    sfpsTopologyFCLTable.setStatus("mandatory")
_SfpsTopologyFCLEntry_Object = MibTableRow
sfpsTopologyFCLEntry = _SfpsTopologyFCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1, 1)
)
sfpsTopologyFCLEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsTopologyFCLFunctionalLevel"),
)
if mibBuilder.loadTexts:
    sfpsTopologyFCLEntry.setStatus("mandatory")
_SfpsTopologyFCLFunctionalLevel_Type = Integer32
_SfpsTopologyFCLFunctionalLevel_Object = MibTableColumn
sfpsTopologyFCLFunctionalLevel = _SfpsTopologyFCLFunctionalLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1, 1, 1),
    _SfpsTopologyFCLFunctionalLevel_Type()
)
sfpsTopologyFCLFunctionalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyFCLFunctionalLevel.setStatus("mandatory")


class _SfpsTopologyFCLCompatability_Type(Integer32):
    """Custom type sfpsTopologyFCLCompatability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatable", 1),
          ("notCompatable", 2))
    )


_SfpsTopologyFCLCompatability_Type.__name__ = "Integer32"
_SfpsTopologyFCLCompatability_Object = MibTableColumn
sfpsTopologyFCLCompatability = _SfpsTopologyFCLCompatability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1, 1, 2),
    _SfpsTopologyFCLCompatability_Type()
)
sfpsTopologyFCLCompatability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyFCLCompatability.setStatus("mandatory")


class _SfpsTopologyFCLThisPortState_Type(Integer32):
    """Custom type sfpsTopologyFCLThisPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostControl", 5),
          ("hostManagement", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsTopologyFCLThisPortState_Type.__name__ = "Integer32"
_SfpsTopologyFCLThisPortState_Object = MibTableColumn
sfpsTopologyFCLThisPortState = _SfpsTopologyFCLThisPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1, 1, 3),
    _SfpsTopologyFCLThisPortState_Type()
)
sfpsTopologyFCLThisPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyFCLThisPortState.setStatus("mandatory")


class _SfpsTopologyFCLSendPortState_Type(Integer32):
    """Custom type sfpsTopologyFCLSendPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("goingToAccess", 7),
          ("hostControl", 5),
          ("hostManagement", 4),
          ("hybrid", 8),
          ("network", 3),
          ("other", 1),
          ("standBy", 9),
          ("unknown", 6))
    )


_SfpsTopologyFCLSendPortState_Type.__name__ = "Integer32"
_SfpsTopologyFCLSendPortState_Object = MibTableColumn
sfpsTopologyFCLSendPortState = _SfpsTopologyFCLSendPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7, 1, 1, 4),
    _SfpsTopologyFCLSendPortState_Type()
)
sfpsTopologyFCLSendPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyFCLSendPortState.setStatus("mandatory")
_SfpsDirViolationTable_Object = MibTable
sfpsDirViolationTable = _SfpsDirViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsDirViolationTable.setStatus("mandatory")
_SfpsDirViolationEntry_Object = MibTableRow
sfpsDirViolationEntry = _SfpsDirViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1)
)
sfpsDirViolationEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsDirViolationHash"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsDirViolationHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsDirViolationEntry.setStatus("mandatory")
_SfpsDirViolationHash_Type = Integer32
_SfpsDirViolationHash_Object = MibTableColumn
sfpsDirViolationHash = _SfpsDirViolationHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 1),
    _SfpsDirViolationHash_Type()
)
sfpsDirViolationHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationHash.setStatus("mandatory")
_SfpsDirViolationHashIndex_Type = Integer32
_SfpsDirViolationHashIndex_Object = MibTableColumn
sfpsDirViolationHashIndex = _SfpsDirViolationHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 2),
    _SfpsDirViolationHashIndex_Type()
)
sfpsDirViolationHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationHashIndex.setStatus("mandatory")


class _SfpsDirViolationType_Type(Integer32):
    """Custom type sfpsDirViolationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipInvalid", 4),
          ("ipNotLearned", 3),
          ("restrictMobility", 5),
          ("restrictPort", 2),
          ("sapDisabled", 7),
          ("userLock", 1),
          ("userLockSamePort", 6))
    )


_SfpsDirViolationType_Type.__name__ = "Integer32"
_SfpsDirViolationType_Object = MibTableColumn
sfpsDirViolationType = _SfpsDirViolationType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 3),
    _SfpsDirViolationType_Type()
)
sfpsDirViolationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationType.setStatus("mandatory")
_SfpsDirViolationSrcPort_Type = Integer32
_SfpsDirViolationSrcPort_Object = MibTableColumn
sfpsDirViolationSrcPort = _SfpsDirViolationSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 4),
    _SfpsDirViolationSrcPort_Type()
)
sfpsDirViolationSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationSrcPort.setStatus("mandatory")


class _SfpsDirViolationAOType_Type(Integer32):
    """Custom type sfpsDirViolationAOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("aoAtDDP", 11),
          ("aoEmpty", 12),
          ("aoHostName", 14),
          ("aoInetIP", 7),
          ("aoInetIPMask", 16),
          ("aoInetRIP", 9),
          ("aoInetRPC", 8),
          ("aoInetUDP", 5),
          ("aoInetYP", 4),
          ("aoIpxIpx", 6),
          ("aoIpxRIP", 3),
          ("aoIpxSap", 2),
          ("aoMacDX", 1),
          ("aoMacDXMcast", 10),
          ("aoNetBiosName", 15),
          ("aoVlan", 13))
    )


_SfpsDirViolationAOType_Type.__name__ = "Integer32"
_SfpsDirViolationAOType_Object = MibTableColumn
sfpsDirViolationAOType = _SfpsDirViolationAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 5),
    _SfpsDirViolationAOType_Type()
)
sfpsDirViolationAOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationAOType.setStatus("mandatory")
_SfpsDirViolationAOValue_Type = DisplayString
_SfpsDirViolationAOValue_Object = MibTableColumn
sfpsDirViolationAOValue = _SfpsDirViolationAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 6),
    _SfpsDirViolationAOValue_Type()
)
sfpsDirViolationAOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationAOValue.setStatus("mandatory")
_SfpsDirViolationLocalPort_Type = Integer32
_SfpsDirViolationLocalPort_Object = MibTableColumn
sfpsDirViolationLocalPort = _SfpsDirViolationLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 7),
    _SfpsDirViolationLocalPort_Type()
)
sfpsDirViolationLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationLocalPort.setStatus("mandatory")
_SfpsDirViolationCount_Type = Integer32
_SfpsDirViolationCount_Object = MibTableColumn
sfpsDirViolationCount = _SfpsDirViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 8),
    _SfpsDirViolationCount_Type()
)
sfpsDirViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationCount.setStatus("mandatory")
_SfpsDirViolationLastSeen_Type = TimeTicks
_SfpsDirViolationLastSeen_Object = MibTableColumn
sfpsDirViolationLastSeen = _SfpsDirViolationLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 9),
    _SfpsDirViolationLastSeen_Type()
)
sfpsDirViolationLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationLastSeen.setStatus("mandatory")
_SfpsDirViolationFirstSeen_Type = TimeTicks
_SfpsDirViolationFirstSeen_Object = MibTableColumn
sfpsDirViolationFirstSeen = _SfpsDirViolationFirstSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 10),
    _SfpsDirViolationFirstSeen_Type()
)
sfpsDirViolationFirstSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationFirstSeen.setStatus("mandatory")
_SfpsDirViolationSrcMac_Type = OctetString
_SfpsDirViolationSrcMac_Object = MibTableColumn
sfpsDirViolationSrcMac = _SfpsDirViolationSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 11),
    _SfpsDirViolationSrcMac_Type()
)
sfpsDirViolationSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationSrcMac.setStatus("mandatory")
_SfpsDirViolationCPId_Type = OctetString
_SfpsDirViolationCPId_Object = MibTableColumn
sfpsDirViolationCPId = _SfpsDirViolationCPId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 1, 1, 12),
    _SfpsDirViolationCPId_Type()
)
sfpsDirViolationCPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationCPId.setStatus("mandatory")


class _SfpsDirViolationAPIVerb_Type(Integer32):
    """Custom type sfpsDirViolationAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("other", 1),
          ("reset", 4))
    )


_SfpsDirViolationAPIVerb_Type.__name__ = "Integer32"
_SfpsDirViolationAPIVerb_Object = MibScalar
sfpsDirViolationAPIVerb = _SfpsDirViolationAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 1),
    _SfpsDirViolationAPIVerb_Type()
)
sfpsDirViolationAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationAPIVerb.setStatus("mandatory")


class _SfpsDirViolationAPIViolType_Type(Integer32):
    """Custom type sfpsDirViolationAPIViolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("restrictPort", 2))
    )


_SfpsDirViolationAPIViolType_Type.__name__ = "Integer32"
_SfpsDirViolationAPIViolType_Object = MibScalar
sfpsDirViolationAPIViolType = _SfpsDirViolationAPIViolType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 2),
    _SfpsDirViolationAPIViolType_Type()
)
sfpsDirViolationAPIViolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationAPIViolType.setStatus("mandatory")
_SfpsDirViolationAPISourcePort_Type = Integer32
_SfpsDirViolationAPISourcePort_Object = MibScalar
sfpsDirViolationAPISourcePort = _SfpsDirViolationAPISourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 3),
    _SfpsDirViolationAPISourcePort_Type()
)
sfpsDirViolationAPISourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationAPISourcePort.setStatus("mandatory")
_SfpsDirViolationAPIAOType_Type = DisplayString
_SfpsDirViolationAPIAOType_Object = MibScalar
sfpsDirViolationAPIAOType = _SfpsDirViolationAPIAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 4),
    _SfpsDirViolationAPIAOType_Type()
)
sfpsDirViolationAPIAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationAPIAOType.setStatus("mandatory")
_SfpsDirViolationAPIAOValue_Type = DisplayString
_SfpsDirViolationAPIAOValue_Object = MibScalar
sfpsDirViolationAPIAOValue = _SfpsDirViolationAPIAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 5),
    _SfpsDirViolationAPIAOValue_Type()
)
sfpsDirViolationAPIAOValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationAPIAOValue.setStatus("mandatory")
_SfpsDirViolationAPIChangeCount_Type = Integer32
_SfpsDirViolationAPIChangeCount_Object = MibScalar
sfpsDirViolationAPIChangeCount = _SfpsDirViolationAPIChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 6),
    _SfpsDirViolationAPIChangeCount_Type()
)
sfpsDirViolationAPIChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationAPIChangeCount.setStatus("mandatory")
_SfpsDirViolationAPICPId_Type = DisplayString
_SfpsDirViolationAPICPId_Object = MibScalar
sfpsDirViolationAPICPId = _SfpsDirViolationAPICPId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2, 7),
    _SfpsDirViolationAPICPId_Type()
)
sfpsDirViolationAPICPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationAPICPId.setStatus("mandatory")
_SfpsDirViolationDeltaTable_Object = MibTable
sfpsDirViolationDeltaTable = _SfpsDirViolationDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3)
)
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaTable.setStatus("mandatory")
_SfpsDirViolationDeltaEntry_Object = MibTableRow
sfpsDirViolationDeltaEntry = _SfpsDirViolationDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1)
)
sfpsDirViolationDeltaEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsDirViolationDeltaIndex"),
)
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaEntry.setStatus("mandatory")
_SfpsDirViolationDeltaIndex_Type = Integer32
_SfpsDirViolationDeltaIndex_Object = MibTableColumn
sfpsDirViolationDeltaIndex = _SfpsDirViolationDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1, 1),
    _SfpsDirViolationDeltaIndex_Type()
)
sfpsDirViolationDeltaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaIndex.setStatus("mandatory")
_SfpsDirViolationDeltaSrcPort_Type = Integer32
_SfpsDirViolationDeltaSrcPort_Object = MibTableColumn
sfpsDirViolationDeltaSrcPort = _SfpsDirViolationDeltaSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1, 2),
    _SfpsDirViolationDeltaSrcPort_Type()
)
sfpsDirViolationDeltaSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaSrcPort.setStatus("mandatory")


class _SfpsDirViolationDeltaAOType_Type(Integer32):
    """Custom type sfpsDirViolationDeltaAOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("aoAtDDP", 11),
          ("aoEmpty", 12),
          ("aoHostName", 14),
          ("aoInetIP", 7),
          ("aoInetIPMask", 16),
          ("aoInetRIP", 9),
          ("aoInetRPC", 8),
          ("aoInetUDP", 5),
          ("aoInetYP", 4),
          ("aoIpxIpx", 6),
          ("aoIpxRIP", 3),
          ("aoIpxSap", 2),
          ("aoMacDX", 1),
          ("aoMacDXMcast", 10),
          ("aoNetBiosName", 15),
          ("aoVlan", 13))
    )


_SfpsDirViolationDeltaAOType_Type.__name__ = "Integer32"
_SfpsDirViolationDeltaAOType_Object = MibTableColumn
sfpsDirViolationDeltaAOType = _SfpsDirViolationDeltaAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1, 3),
    _SfpsDirViolationDeltaAOType_Type()
)
sfpsDirViolationDeltaAOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaAOType.setStatus("mandatory")
_SfpsDirViolationDeltaAOValue_Type = Integer32
_SfpsDirViolationDeltaAOValue_Object = MibTableColumn
sfpsDirViolationDeltaAOValue = _SfpsDirViolationDeltaAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1, 4),
    _SfpsDirViolationDeltaAOValue_Type()
)
sfpsDirViolationDeltaAOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaAOValue.setStatus("mandatory")


class _SfpsDirViolationDeltaEntryType_Type(Integer32):
    """Custom type sfpsDirViolationDeltaEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("added", 2),
          ("deleted", 3),
          ("other", 1))
    )


_SfpsDirViolationDeltaEntryType_Type.__name__ = "Integer32"
_SfpsDirViolationDeltaEntryType_Object = MibTableColumn
sfpsDirViolationDeltaEntryType = _SfpsDirViolationDeltaEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 3, 1, 5),
    _SfpsDirViolationDeltaEntryType_Type()
)
sfpsDirViolationDeltaEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaEntryType.setStatus("mandatory")
_SfpsDirViolationDeltaAPINumEntries_Type = Integer32
_SfpsDirViolationDeltaAPINumEntries_Object = MibScalar
sfpsDirViolationDeltaAPINumEntries = _SfpsDirViolationDeltaAPINumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 4, 1),
    _SfpsDirViolationDeltaAPINumEntries_Type()
)
sfpsDirViolationDeltaAPINumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaAPINumEntries.setStatus("mandatory")


class _SfpsDirViolationDeltaAPIVerb_Type(Integer32):
    """Custom type sfpsDirViolationDeltaAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_SfpsDirViolationDeltaAPIVerb_Type.__name__ = "Integer32"
_SfpsDirViolationDeltaAPIVerb_Object = MibScalar
sfpsDirViolationDeltaAPIVerb = _SfpsDirViolationDeltaAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 4, 2),
    _SfpsDirViolationDeltaAPIVerb_Type()
)
sfpsDirViolationDeltaAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirViolationDeltaAPIVerb.setStatus("mandatory")
_SfpsRestrictedPortTable_Object = MibTable
sfpsRestrictedPortTable = _SfpsRestrictedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsRestrictedPortTable.setStatus("mandatory")
_SfpsRestrictedPortEntry_Object = MibTableRow
sfpsRestrictedPortEntry = _SfpsRestrictedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1, 1)
)
sfpsRestrictedPortEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedPortPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedPortHash"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedPortHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsRestrictedPortEntry.setStatus("mandatory")
_SfpsRestrictedPortPort_Type = Integer32
_SfpsRestrictedPortPort_Object = MibTableColumn
sfpsRestrictedPortPort = _SfpsRestrictedPortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1, 1, 1),
    _SfpsRestrictedPortPort_Type()
)
sfpsRestrictedPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedPortPort.setStatus("mandatory")
_SfpsRestrictedPortHash_Type = Integer32
_SfpsRestrictedPortHash_Object = MibTableColumn
sfpsRestrictedPortHash = _SfpsRestrictedPortHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1, 1, 2),
    _SfpsRestrictedPortHash_Type()
)
sfpsRestrictedPortHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedPortHash.setStatus("mandatory")
_SfpsRestrictedPortHashIndex_Type = Integer32
_SfpsRestrictedPortHashIndex_Object = MibTableColumn
sfpsRestrictedPortHashIndex = _SfpsRestrictedPortHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1, 1, 3),
    _SfpsRestrictedPortHashIndex_Type()
)
sfpsRestrictedPortHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedPortHashIndex.setStatus("mandatory")
_SfpsRestrictedPortSrcMac_Type = DisplayString
_SfpsRestrictedPortSrcMac_Object = MibTableColumn
sfpsRestrictedPortSrcMac = _SfpsRestrictedPortSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2, 1, 1, 4),
    _SfpsRestrictedPortSrcMac_Type()
)
sfpsRestrictedPortSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedPortSrcMac.setStatus("mandatory")


class _SfpsDirLockConfigUserLocking_Type(Integer32):
    """Custom type sfpsDirLockConfigUserLocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SfpsDirLockConfigUserLocking_Type.__name__ = "Integer32"
_SfpsDirLockConfigUserLocking_Object = MibScalar
sfpsDirLockConfigUserLocking = _SfpsDirLockConfigUserLocking_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 3, 1),
    _SfpsDirLockConfigUserLocking_Type()
)
sfpsDirLockConfigUserLocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirLockConfigUserLocking.setStatus("mandatory")


class _SfpsDirLockConfigRestrictedPort_Type(Integer32):
    """Custom type sfpsDirLockConfigRestrictedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SfpsDirLockConfigRestrictedPort_Type.__name__ = "Integer32"
_SfpsDirLockConfigRestrictedPort_Object = MibScalar
sfpsDirLockConfigRestrictedPort = _SfpsDirLockConfigRestrictedPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 3, 2),
    _SfpsDirLockConfigRestrictedPort_Type()
)
sfpsDirLockConfigRestrictedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirLockConfigRestrictedPort.setStatus("mandatory")


class _SfpsDirLockConfigRouterPortLock_Type(Integer32):
    """Custom type sfpsDirLockConfigRouterPortLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SfpsDirLockConfigRouterPortLock_Type.__name__ = "Integer32"
_SfpsDirLockConfigRouterPortLock_Object = MibScalar
sfpsDirLockConfigRouterPortLock = _SfpsDirLockConfigRouterPortLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 3, 3),
    _SfpsDirLockConfigRouterPortLock_Type()
)
sfpsDirLockConfigRouterPortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirLockConfigRouterPortLock.setStatus("mandatory")


class _SfpsDirLockConfigRAPortLock_Type(Integer32):
    """Custom type sfpsDirLockConfigRAPortLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SfpsDirLockConfigRAPortLock_Type.__name__ = "Integer32"
_SfpsDirLockConfigRAPortLock_Object = MibScalar
sfpsDirLockConfigRAPortLock = _SfpsDirLockConfigRAPortLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 3, 4),
    _SfpsDirLockConfigRAPortLock_Type()
)
sfpsDirLockConfigRAPortLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockConfigRAPortLock.setStatus("mandatory")
_SfpsDirLockStatsNumViolators_Type = Integer32
_SfpsDirLockStatsNumViolators_Object = MibScalar
sfpsDirLockStatsNumViolators = _SfpsDirLockStatsNumViolators_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 1),
    _SfpsDirLockStatsNumViolators_Type()
)
sfpsDirLockStatsNumViolators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsNumViolators.setStatus("mandatory")
_SfpsDirLockStatsNumNodeLocked_Type = Integer32
_SfpsDirLockStatsNumNodeLocked_Object = MibScalar
sfpsDirLockStatsNumNodeLocked = _SfpsDirLockStatsNumNodeLocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 2),
    _SfpsDirLockStatsNumNodeLocked_Type()
)
sfpsDirLockStatsNumNodeLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsNumNodeLocked.setStatus("mandatory")
_SfpsDirLockStatsNumAliasLocked_Type = Integer32
_SfpsDirLockStatsNumAliasLocked_Object = MibScalar
sfpsDirLockStatsNumAliasLocked = _SfpsDirLockStatsNumAliasLocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 3),
    _SfpsDirLockStatsNumAliasLocked_Type()
)
sfpsDirLockStatsNumAliasLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsNumAliasLocked.setStatus("mandatory")
_SfpsDirLockStatsNumRestrictedPort_Type = Integer32
_SfpsDirLockStatsNumRestrictedPort_Object = MibScalar
sfpsDirLockStatsNumRestrictedPort = _SfpsDirLockStatsNumRestrictedPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 4),
    _SfpsDirLockStatsNumRestrictedPort_Type()
)
sfpsDirLockStatsNumRestrictedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsNumRestrictedPort.setStatus("mandatory")
_SfpsDirLockStatsNumRestrictMob_Type = Integer32
_SfpsDirLockStatsNumRestrictMob_Object = MibScalar
sfpsDirLockStatsNumRestrictMob = _SfpsDirLockStatsNumRestrictMob_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 5),
    _SfpsDirLockStatsNumRestrictMob_Type()
)
sfpsDirLockStatsNumRestrictMob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsNumRestrictMob.setStatus("mandatory")
_SfpsDirLockStatsViolationTblSize_Type = Integer32
_SfpsDirLockStatsViolationTblSize_Object = MibScalar
sfpsDirLockStatsViolationTblSize = _SfpsDirLockStatsViolationTblSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 6),
    _SfpsDirLockStatsViolationTblSize_Type()
)
sfpsDirLockStatsViolationTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsViolationTblSize.setStatus("mandatory")
_SfpsDirLockStatsRestrictPortTblSize_Type = Integer32
_SfpsDirLockStatsRestrictPortTblSize_Object = MibScalar
sfpsDirLockStatsRestrictPortTblSize = _SfpsDirLockStatsRestrictPortTblSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 7),
    _SfpsDirLockStatsRestrictPortTblSize_Type()
)
sfpsDirLockStatsRestrictPortTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsRestrictPortTblSize.setStatus("mandatory")
_SfpsDirLockStatsRestrictMobTblSize_Type = Integer32
_SfpsDirLockStatsRestrictMobTblSize_Object = MibScalar
sfpsDirLockStatsRestrictMobTblSize = _SfpsDirLockStatsRestrictMobTblSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4, 8),
    _SfpsDirLockStatsRestrictMobTblSize_Type()
)
sfpsDirLockStatsRestrictMobTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirLockStatsRestrictMobTblSize.setStatus("mandatory")
_SfpsRestrictedMobilityTable_Object = MibTable
sfpsRestrictedMobilityTable = _SfpsRestrictedMobilityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityTable.setStatus("mandatory")
_SfpsRestrictedMobilityEntry_Object = MibTableRow
sfpsRestrictedMobilityEntry = _SfpsRestrictedMobilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1)
)
sfpsRestrictedMobilityEntry.setIndexNames(
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedMobilityHash"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedMobilityPort"),
    (0, "CTRON-SFPS-TOPOLOGY-MIB", "sfpsRestrictedMobilityHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityEntry.setStatus("mandatory")
_SfpsRestrictedMobilityHash_Type = Integer32
_SfpsRestrictedMobilityHash_Object = MibTableColumn
sfpsRestrictedMobilityHash = _SfpsRestrictedMobilityHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1, 1),
    _SfpsRestrictedMobilityHash_Type()
)
sfpsRestrictedMobilityHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityHash.setStatus("mandatory")
_SfpsRestrictedMobilityPort_Type = Integer32
_SfpsRestrictedMobilityPort_Object = MibTableColumn
sfpsRestrictedMobilityPort = _SfpsRestrictedMobilityPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1, 2),
    _SfpsRestrictedMobilityPort_Type()
)
sfpsRestrictedMobilityPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityPort.setStatus("mandatory")
_SfpsRestrictedMobilityHashIndex_Type = Integer32
_SfpsRestrictedMobilityHashIndex_Object = MibTableColumn
sfpsRestrictedMobilityHashIndex = _SfpsRestrictedMobilityHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1, 3),
    _SfpsRestrictedMobilityHashIndex_Type()
)
sfpsRestrictedMobilityHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityHashIndex.setStatus("mandatory")
_SfpsRestrictedMobilitySrcMac_Type = OctetString
_SfpsRestrictedMobilitySrcMac_Object = MibTableColumn
sfpsRestrictedMobilitySrcMac = _SfpsRestrictedMobilitySrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1, 4),
    _SfpsRestrictedMobilitySrcMac_Type()
)
sfpsRestrictedMobilitySrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilitySrcMac.setStatus("mandatory")
_SfpsRestrictedMobilitySwitch_Type = SfpsAddress
_SfpsRestrictedMobilitySwitch_Object = MibTableColumn
sfpsRestrictedMobilitySwitch = _SfpsRestrictedMobilitySwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 1, 1, 5),
    _SfpsRestrictedMobilitySwitch_Type()
)
sfpsRestrictedMobilitySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilitySwitch.setStatus("mandatory")


class _SfpsRestrictedMobilityAPIVerb_Type(Integer32):
    """Custom type sfpsRestrictedMobilityAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("other", 1),
          ("reset", 4))
    )


_SfpsRestrictedMobilityAPIVerb_Type.__name__ = "Integer32"
_SfpsRestrictedMobilityAPIVerb_Object = MibScalar
sfpsRestrictedMobilityAPIVerb = _SfpsRestrictedMobilityAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 2, 1),
    _SfpsRestrictedMobilityAPIVerb_Type()
)
sfpsRestrictedMobilityAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityAPIVerb.setStatus("mandatory")
_SfpsRestrictedMobilityAPISourcePort_Type = Integer32
_SfpsRestrictedMobilityAPISourcePort_Object = MibScalar
sfpsRestrictedMobilityAPISourcePort = _SfpsRestrictedMobilityAPISourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 2, 2),
    _SfpsRestrictedMobilityAPISourcePort_Type()
)
sfpsRestrictedMobilityAPISourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityAPISourcePort.setStatus("mandatory")
_SfpsRestrictedMobilityAPISrcMac_Type = SfpsAddress
_SfpsRestrictedMobilityAPISrcMac_Object = MibScalar
sfpsRestrictedMobilityAPISrcMac = _SfpsRestrictedMobilityAPISrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 2, 3),
    _SfpsRestrictedMobilityAPISrcMac_Type()
)
sfpsRestrictedMobilityAPISrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityAPISrcMac.setStatus("mandatory")
_SfpsRestrictedMobilityAPISwitch_Type = SfpsAddress
_SfpsRestrictedMobilityAPISwitch_Object = MibScalar
sfpsRestrictedMobilityAPISwitch = _SfpsRestrictedMobilityAPISwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 2, 4),
    _SfpsRestrictedMobilityAPISwitch_Type()
)
sfpsRestrictedMobilityAPISwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsRestrictedMobilityAPISwitch.setStatus("mandatory")


class _SfpsDapiNvramStatsVerb_Type(Integer32):
    """Custom type sfpsDapiNvramStatsVerb based on Integer32"""
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
        *(("clearAllEntries", 2),
          ("clearAllLimitMobility", 6),
          ("clearAllPortUnblock", 5),
          ("clearAllSrcUnblock", 4),
          ("clearAllUserLock", 3),
          ("other", 1))
    )


_SfpsDapiNvramStatsVerb_Type.__name__ = "Integer32"
_SfpsDapiNvramStatsVerb_Object = MibScalar
sfpsDapiNvramStatsVerb = _SfpsDapiNvramStatsVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 1),
    _SfpsDapiNvramStatsVerb_Type()
)
sfpsDapiNvramStatsVerb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsVerb.setStatus("mandatory")
_SfpsDapiNvramStatsTotalEntries_Type = Integer32
_SfpsDapiNvramStatsTotalEntries_Object = MibScalar
sfpsDapiNvramStatsTotalEntries = _SfpsDapiNvramStatsTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 2),
    _SfpsDapiNvramStatsTotalEntries_Type()
)
sfpsDapiNvramStatsTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsTotalEntries.setStatus("mandatory")
_SfpsDapiNvramStatsMacEntries_Type = Integer32
_SfpsDapiNvramStatsMacEntries_Object = MibScalar
sfpsDapiNvramStatsMacEntries = _SfpsDapiNvramStatsMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 3),
    _SfpsDapiNvramStatsMacEntries_Type()
)
sfpsDapiNvramStatsMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsMacEntries.setStatus("mandatory")
_SfpsDapiNvramStatsAliasEntries_Type = Integer32
_SfpsDapiNvramStatsAliasEntries_Object = MibScalar
sfpsDapiNvramStatsAliasEntries = _SfpsDapiNvramStatsAliasEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 4),
    _SfpsDapiNvramStatsAliasEntries_Type()
)
sfpsDapiNvramStatsAliasEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsAliasEntries.setStatus("mandatory")
_SfpsDapiNvramStatsMaxEntries_Type = Integer32
_SfpsDapiNvramStatsMaxEntries_Object = MibScalar
sfpsDapiNvramStatsMaxEntries = _SfpsDapiNvramStatsMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 5),
    _SfpsDapiNvramStatsMaxEntries_Type()
)
sfpsDapiNvramStatsMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsMaxEntries.setStatus("mandatory")
_SfpsDapiNvramStatsNvramUsed_Type = Integer32
_SfpsDapiNvramStatsNvramUsed_Object = MibScalar
sfpsDapiNvramStatsNvramUsed = _SfpsDapiNvramStatsNvramUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16, 6),
    _SfpsDapiNvramStatsNvramUsed_Type()
)
sfpsDapiNvramStatsNvramUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDapiNvramStatsNvramUsed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-TOPOLOGY-MIB",
    **{"HexInteger": HexInteger,
       "SfpsAddress": SfpsAddress,
       "sfpsServiceCenterTopologyTable": sfpsServiceCenterTopologyTable,
       "sfpsServiceCenterTopologyEntry": sfpsServiceCenterTopologyEntry,
       "sfpsServiceCenterTopologyHashLeaf": sfpsServiceCenterTopologyHashLeaf,
       "sfpsServiceCenterTopologyMetric": sfpsServiceCenterTopologyMetric,
       "sfpsServiceCenterTopologyName": sfpsServiceCenterTopologyName,
       "sfpsServiceCenterTopologyOperStatus": sfpsServiceCenterTopologyOperStatus,
       "sfpsServiceCenterTopologyAdminStatus": sfpsServiceCenterTopologyAdminStatus,
       "sfpsServiceCenterTopologyStatusTime": sfpsServiceCenterTopologyStatusTime,
       "sfpsServiceCenterTopologyRequests": sfpsServiceCenterTopologyRequests,
       "sfpsServiceCenterTopologyResponses": sfpsServiceCenterTopologyResponses,
       "sfpsHistoryTopologyServerTable": sfpsHistoryTopologyServerTable,
       "sfpsHistoryTopologyServerEntry": sfpsHistoryTopologyServerEntry,
       "sfpsHistoryTopologyServerIndex": sfpsHistoryTopologyServerIndex,
       "sfpsHistoryTopologyServerLogicalPort": sfpsHistoryTopologyServerLogicalPort,
       "sfpsHistoryTopologyServerSwitchID": sfpsHistoryTopologyServerSwitchID,
       "sfpsHistoryTopologyServerEvent": sfpsHistoryTopologyServerEvent,
       "sfpsHistoryTopologyServerSwitchIP": sfpsHistoryTopologyServerSwitchIP,
       "sfpsHistoryTopologyServerChassisMAC": sfpsHistoryTopologyServerChassisMAC,
       "sfpsHistoryTopologyServerChassisIP": sfpsHistoryTopologyServerChassisIP,
       "sfpsHistoryTopologyServerAgent": sfpsHistoryTopologyServerAgent,
       "sfpsHistoryTopologyServerDeltaOptionsMask": sfpsHistoryTopologyServerDeltaOptionsMask,
       "sfpsHistoryTopologyServerCurrentOptionsMask": sfpsHistoryTopologyServerCurrentOptionsMask,
       "sfpsHistoryTopologyServerFCL": sfpsHistoryTopologyServerFCL,
       "sfpsHistoryTopologyServerSysTime": sfpsHistoryTopologyServerSysTime,
       "sfpsTPMPortTable": sfpsTPMPortTable,
       "sfpsTPMPortEntry": sfpsTPMPortEntry,
       "sfpsTPMPortLogicalPort": sfpsTPMPortLogicalPort,
       "sfpsTPMPortMediaType": sfpsTPMPortMediaType,
       "sfpsTPMPortTopologyAgent": sfpsTPMPortTopologyAgent,
       "sfpsTPMPortVlanAttributes": sfpsTPMPortVlanAttributes,
       "sfpsTPMPortNVRAMStatus": sfpsTPMPortNVRAMStatus,
       "sfpsTPMPortCorePortVID": sfpsTPMPortCorePortVID,
       "sfpsTPMPortTableAPIInVerb": sfpsTPMPortTableAPIInVerb,
       "sfpsTPMPortTableAPIInLogicalPort": sfpsTPMPortTableAPIInLogicalPort,
       "sfpsTPMPortTableAPIInTopologyAgent": sfpsTPMPortTableAPIInTopologyAgent,
       "sfpsTPMPortTableAPIInAdminPortUp": sfpsTPMPortTableAPIInAdminPortUp,
       "sfpsTPMPortTableAPIInAdminPortDown": sfpsTPMPortTableAPIInAdminPortDown,
       "sfpsTPMPortTableAPIInCorePortVID": sfpsTPMPortTableAPIInCorePortVID,
       "sfpsTPMPortTableAPIOutLogicalPort": sfpsTPMPortTableAPIOutLogicalPort,
       "sfpsTPMPortTableAPIOutTopologyAgent": sfpsTPMPortTableAPIOutTopologyAgent,
       "sfpsCommonNeighborTable": sfpsCommonNeighborTable,
       "sfpsCommonNeighborEntry": sfpsCommonNeighborEntry,
       "sfpsCommonNeighborLogicalPort": sfpsCommonNeighborLogicalPort,
       "sfpsCommonNeighborSwitchID": sfpsCommonNeighborSwitchID,
       "sfpsCommonNeighborSwitchIP": sfpsCommonNeighborSwitchIP,
       "sfpsCommonNeighborSwitchMAC": sfpsCommonNeighborSwitchMAC,
       "sfpsCommonNeighborSwitchType": sfpsCommonNeighborSwitchType,
       "sfpsCommonNeighborHellosReceived": sfpsCommonNeighborHellosReceived,
       "sfpsCommonNeighborFirstHeard": sfpsCommonNeighborFirstHeard,
       "sfpsCommonNeighborLastHeard": sfpsCommonNeighborLastHeard,
       "sfpsCommonNeighborReceiveFrequency": sfpsCommonNeighborReceiveFrequency,
       "sfpsCommonNeighborTopologyAgent": sfpsCommonNeighborTopologyAgent,
       "sfpsCommonNeighborChassisMAC": sfpsCommonNeighborChassisMAC,
       "sfpsCommonNeighborCommState": sfpsCommonNeighborCommState,
       "sfpsCommonNeighborNotifyState": sfpsCommonNeighborNotifyState,
       "sfpsCommonNeighborTwoWayLossCount": sfpsCommonNeighborTwoWayLossCount,
       "sfpsCommonNeighborTwoWayLossTime": sfpsCommonNeighborTwoWayLossTime,
       "sfpsCommonNeighborSeqNumLossCount": sfpsCommonNeighborSeqNumLossCount,
       "sfpsCommonNeighborSeqNumLossTime": sfpsCommonNeighborSeqNumLossTime,
       "sfpsCommonNeighborFalseAgingCount": sfpsCommonNeighborFalseAgingCount,
       "sfpsCommonNeighborFalseAgingTime": sfpsCommonNeighborFalseAgingTime,
       "sfpsCommonNeighborChassisIP": sfpsCommonNeighborChassisIP,
       "sfpsCommonNeighborFCL": sfpsCommonNeighborFCL,
       "sfpsCommonNeighborOptionsMask": sfpsCommonNeighborOptionsMask,
       "sfpsCommonNeighborRcvdPortState": sfpsCommonNeighborRcvdPortState,
       "sfpsCommonNeighborSendPortState": sfpsCommonNeighborSendPortState,
       "sfpsCommonNeighborCompatibility": sfpsCommonNeighborCompatibility,
       "sfpsCommonNeighborCorePortVID": sfpsCommonNeighborCorePortVID,
       "sfpsIncompatibleNeighborTable": sfpsIncompatibleNeighborTable,
       "sfpsIncompatibleNeighborEntry": sfpsIncompatibleNeighborEntry,
       "sfpsIncompatibleNeighborLogicalPort": sfpsIncompatibleNeighborLogicalPort,
       "sfpsIncompatibleNeighborSwitchID": sfpsIncompatibleNeighborSwitchID,
       "sfpsIncompatibleNeighborSwitchIP": sfpsIncompatibleNeighborSwitchIP,
       "sfpsIncompatibleNeighborSwitchMAC": sfpsIncompatibleNeighborSwitchMAC,
       "sfpsIncompatibleNeighborSwitchType": sfpsIncompatibleNeighborSwitchType,
       "sfpsIncompatibleNeighborHellosReceived": sfpsIncompatibleNeighborHellosReceived,
       "sfpsIncompatibleNeighborFirstHeard": sfpsIncompatibleNeighborFirstHeard,
       "sfpsIncompatibleNeighborLastHeard": sfpsIncompatibleNeighborLastHeard,
       "sfpsIncompatibleNeighborReceiveFrequency": sfpsIncompatibleNeighborReceiveFrequency,
       "sfpsIncompatibleNeighborTopologyAgent": sfpsIncompatibleNeighborTopologyAgent,
       "sfpsIncompatibleNeighborChassisMAC": sfpsIncompatibleNeighborChassisMAC,
       "sfpsIncompatibleNeighborCommState": sfpsIncompatibleNeighborCommState,
       "sfpsIncompatibleNeighborNotifyState": sfpsIncompatibleNeighborNotifyState,
       "sfpsIncompatibleNeighborTwoWayLossCount": sfpsIncompatibleNeighborTwoWayLossCount,
       "sfpsIncompatibleNeighborTwoWayLossTime": sfpsIncompatibleNeighborTwoWayLossTime,
       "sfpsIncompatibleNeighborSeqNumLossCount": sfpsIncompatibleNeighborSeqNumLossCount,
       "sfpsIncompatibleNeighborSeqNumLossTime": sfpsIncompatibleNeighborSeqNumLossTime,
       "sfpsIncompatibleNeighborFalseAgingCount": sfpsIncompatibleNeighborFalseAgingCount,
       "sfpsIncompatibleNeighborFalseAgingTime": sfpsIncompatibleNeighborFalseAgingTime,
       "sfpsIncompatibleNeighborChassisIP": sfpsIncompatibleNeighborChassisIP,
       "sfpsIncompatibleNeighborFCL": sfpsIncompatibleNeighborFCL,
       "sfpsIncompatibleNeighborOptionsMask": sfpsIncompatibleNeighborOptionsMask,
       "sfpsIncompatibleNeighborLocalPortState": sfpsIncompatibleNeighborLocalPortState,
       "sfpsIncompatibleNeighborRemotePortState": sfpsIncompatibleNeighborRemotePortState,
       "sfpsIncompatibleNeighborCompatibility": sfpsIncompatibleNeighborCompatibility,
       "sfpsVLANTopAgentNeighborTable": sfpsVLANTopAgentNeighborTable,
       "sfpsVLANTopAgentNeighborEntry": sfpsVLANTopAgentNeighborEntry,
       "sfpsVLANTopAgentNeighborInPort": sfpsVLANTopAgentNeighborInPort,
       "sfpsVLANTopAgentNeighborSwitchID": sfpsVLANTopAgentNeighborSwitchID,
       "sfpsVLANTopAgentNeighborOptions": sfpsVLANTopAgentNeighborOptions,
       "sfpsVLANTopAgentPortTable": sfpsVLANTopAgentPortTable,
       "sfpsVLANTopAgentPortEntry": sfpsVLANTopAgentPortEntry,
       "sfpsVLANTopAgentPortPort": sfpsVLANTopAgentPortPort,
       "sfpsVLANTopAgentPortHelloVersion": sfpsVLANTopAgentPortHelloVersion,
       "sfpsVLANTopAgentPortSendFrequency": sfpsVLANTopAgentPortSendFrequency,
       "sfpsVLANTopAgentPortRecvFrequency": sfpsVLANTopAgentPortRecvFrequency,
       "sfpsVLANTopAgentPortPortOptions": sfpsVLANTopAgentPortPortOptions,
       "sfpsVLANTopAgentPortNVRAMStatus": sfpsVLANTopAgentPortNVRAMStatus,
       "sfpsVLANTopAgentPortTableAPIInVerb": sfpsVLANTopAgentPortTableAPIInVerb,
       "sfpsVLANTopAgentPortTableAPIInLogicalPort": sfpsVLANTopAgentPortTableAPIInLogicalPort,
       "sfpsVLANTopAgentPortTableAPIInHelloVersion": sfpsVLANTopAgentPortTableAPIInHelloVersion,
       "sfpsVLANTopAgentPortTableAPIInSendFrequency": sfpsVLANTopAgentPortTableAPIInSendFrequency,
       "sfpsVLANTopAgentPortTableAPIInRecvFrequency": sfpsVLANTopAgentPortTableAPIInRecvFrequency,
       "sfpsRATopAgentNeighborTable": sfpsRATopAgentNeighborTable,
       "sfpsRATopAgentNeighborEntry": sfpsRATopAgentNeighborEntry,
       "sfpsRATopAgentNeighborInPort": sfpsRATopAgentNeighborInPort,
       "sfpsRATopAgentNeighborSwitchID": sfpsRATopAgentNeighborSwitchID,
       "sfpsRATopAgentNeighborPriority": sfpsRATopAgentNeighborPriority,
       "sfpsRATopAgentNeighborNetworkPort": sfpsRATopAgentNeighborNetworkPort,
       "sfpsRATopAgentNeighborCallTag": sfpsRATopAgentNeighborCallTag,
       "sfpsRATopAgentNeighborNetHellosRcvd": sfpsRATopAgentNeighborNetHellosRcvd,
       "sfpsRATopAgentNeighborSeqNumMismatch": sfpsRATopAgentNeighborSeqNumMismatch,
       "sfpsRATopAgentNeighborNetHelloAgeTimeOuts": sfpsRATopAgentNeighborNetHelloAgeTimeOuts,
       "sfpsRATopAgentNeighborNetHelloNetPortLosses": sfpsRATopAgentNeighborNetHelloNetPortLosses,
       "sfpsRATopAgentNeighborNetHelloNetPortChanges": sfpsRATopAgentNeighborNetHelloNetPortChanges,
       "sfpsRATopAgentPortTable": sfpsRATopAgentPortTable,
       "sfpsRATopAgentPortEntry": sfpsRATopAgentPortEntry,
       "sfpsRATopAgentPortLogicalPort": sfpsRATopAgentPortLogicalPort,
       "sfpsRATopAgentPortHelloVersion": sfpsRATopAgentPortHelloVersion,
       "sfpsRATopAgentPortSendFrequency": sfpsRATopAgentPortSendFrequency,
       "sfpsRATopAgentPortRecvFrequency": sfpsRATopAgentPortRecvFrequency,
       "sfpsRATopAgentPortPriority": sfpsRATopAgentPortPriority,
       "sfpsRATopAgentPortPortState": sfpsRATopAgentPortPortState,
       "sfpsRATopAgentPortPrimarySwitch": sfpsRATopAgentPortPrimarySwitch,
       "sfpsRATopAgentPortNetHelloRecvFreq": sfpsRATopAgentPortNetHelloRecvFreq,
       "sfpsRATopAgentPortStateChangeCount": sfpsRATopAgentPortStateChangeCount,
       "sfpsRATopAgentPortNVRAMStatus": sfpsRATopAgentPortNVRAMStatus,
       "sfpsRATopAgentPortTableAPIInVerb": sfpsRATopAgentPortTableAPIInVerb,
       "sfpsRATopAgentPortTableAPIInLogicalPort": sfpsRATopAgentPortTableAPIInLogicalPort,
       "sfpsRATopAgentPortTableAPIInHelloVersion": sfpsRATopAgentPortTableAPIInHelloVersion,
       "sfpsRATopAgentPortTableAPIInSendFrequency": sfpsRATopAgentPortTableAPIInSendFrequency,
       "sfpsRATopAgentPortTableAPIInRecvFrequency": sfpsRATopAgentPortTableAPIInRecvFrequency,
       "sfpsRATopAgentPortTableAPIInPriority": sfpsRATopAgentPortTableAPIInPriority,
       "sfpsRATopAgentPortTableAPIInNetHelloRecvFreq": sfpsRATopAgentPortTableAPIInNetHelloRecvFreq,
       "sfpsRATopAgentPortTableAPIOutLogicalPort": sfpsRATopAgentPortTableAPIOutLogicalPort,
       "sfpsRATopAgentPortTableAPIOutHelloVersion": sfpsRATopAgentPortTableAPIOutHelloVersion,
       "sfpsRATopAgentPortTableAPIOutSendFrequency": sfpsRATopAgentPortTableAPIOutSendFrequency,
       "sfpsRATopAgentPortTableAPIOutRecvFrequency": sfpsRATopAgentPortTableAPIOutRecvFrequency,
       "sfpsRATopAgentPortTableAPIOutPriority": sfpsRATopAgentPortTableAPIOutPriority,
       "sfpsRATopAgentPortTableAPIOutPortState": sfpsRATopAgentPortTableAPIOutPortState,
       "sfpsRATopAgentPortTableAPIOutPrimarySwitch": sfpsRATopAgentPortTableAPIOutPrimarySwitch,
       "sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq": sfpsRATopAgentPortTableAPIOutNetHelloRecvFreq,
       "sfpsRATopAgentPortTableAPIOutPortStateChangeCount": sfpsRATopAgentPortTableAPIOutPortStateChangeCount,
       "sfpsESPTopAgentPortTable": sfpsESPTopAgentPortTable,
       "sfpsESPTopAgentPortEntry": sfpsESPTopAgentPortEntry,
       "sfpsESPTopAgentPortPort": sfpsESPTopAgentPortPort,
       "sfpsESPTopAgentPortHelloVersion": sfpsESPTopAgentPortHelloVersion,
       "sfpsESPTopAgentPortSendFrequency": sfpsESPTopAgentPortSendFrequency,
       "sfpsESPTopAgentPortRecvFrequency": sfpsESPTopAgentPortRecvFrequency,
       "sfpsVMTopServerDeltaTable": sfpsVMTopServerDeltaTable,
       "sfpsVMTopServerDeltaEntry": sfpsVMTopServerDeltaEntry,
       "sfpsVMTopServerDeltaIndex": sfpsVMTopServerDeltaIndex,
       "sfpsVMTopServerDeltaInPort": sfpsVMTopServerDeltaInPort,
       "sfpsVMTopServerDeltaSwitchID": sfpsVMTopServerDeltaSwitchID,
       "sfpsVMTopServerDeltaState": sfpsVMTopServerDeltaState,
       "sfpsVMTopServerDeltaIPAddress": sfpsVMTopServerDeltaIPAddress,
       "sfpsVMTopServerDeltaAgent": sfpsVMTopServerDeltaAgent,
       "sfpsVMTopServerDeltaCount": sfpsVMTopServerDeltaCount,
       "sfpsVMTopServerTableLock": sfpsVMTopServerTableLock,
       "sfpsVMTopServerPortChange": sfpsVMTopServerPortChange,
       "sfpsVMTopServerTableFull": sfpsVMTopServerTableFull,
       "sfpsVMTopServerChangeCnt": sfpsVMTopServerChangeCnt,
       "sfpsTAPITestInVerb": sfpsTAPITestInVerb,
       "sfpsTAPITestInLogicalPort": sfpsTAPITestInLogicalPort,
       "sfpsTAPITestInSwitchID": sfpsTAPITestInSwitchID,
       "sfpsTAPITestInMAC": sfpsTAPITestInMAC,
       "sfpsTAPITestInPortTypeState": sfpsTAPITestInPortTypeState,
       "sfpsTAPITestInTopologyAgentID": sfpsTAPITestInTopologyAgentID,
       "sfpsTAPITestInUNIT321": sfpsTAPITestInUNIT321,
       "sfpsTAPITestOutOutputInteger": sfpsTAPITestOutOutputInteger,
       "sfpsTAPITestOutOutPutString": sfpsTAPITestOutOutPutString,
       "sfpsTopologyServerTestInVerb": sfpsTopologyServerTestInVerb,
       "sfpsTopologyServerTestInServer": sfpsTopologyServerTestInServer,
       "sfpsTopologyServerTestInNumberOfRelays": sfpsTopologyServerTestInNumberOfRelays,
       "sfpsTopologyServerTestTable": sfpsTopologyServerTestTable,
       "sfpsTopologyServerTestEntry": sfpsTopologyServerTestEntry,
       "sfpsTopologyServerTestRelayNumber": sfpsTopologyServerTestRelayNumber,
       "sfpsTopologyServerTestServerFlavor": sfpsTopologyServerTestServerFlavor,
       "sfpsTopologyServerTestPortNumber": sfpsTopologyServerTestPortNumber,
       "sfpsTopologyServerTestPortName": sfpsTopologyServerTestPortName,
       "sfpsTopologyServerTestIpAddr": sfpsTopologyServerTestIpAddr,
       "sfpsTopologyServerTestLostPort": sfpsTopologyServerTestLostPort,
       "sfpsTopologyServerTestOldState": sfpsTopologyServerTestOldState,
       "sfpsTopologyServerTestNewState": sfpsTopologyServerTestNewState,
       "sfpsTopologyServerTestTopologyAgent": sfpsTopologyServerTestTopologyAgent,
       "sfpsTopologyServerTestTopRelayTable": sfpsTopologyServerTestTopRelayTable,
       "sfpsTopologyServerTestTopRelayEntry": sfpsTopologyServerTestTopRelayEntry,
       "sfpsTopologyServerTestTopRelayRelayNumber": sfpsTopologyServerTestTopRelayRelayNumber,
       "sfpsTopologyServerTestTopRelayEvent": sfpsTopologyServerTestTopRelayEvent,
       "sfpsTopologyServerTestTopRelayDeltaOptions": sfpsTopologyServerTestTopRelayDeltaOptions,
       "sfpsTopologyServerTestTopRelayCurrentOptions": sfpsTopologyServerTestTopRelayCurrentOptions,
       "sfpsTopologyServerTestTopRelayLogicalPort": sfpsTopologyServerTestTopRelayLogicalPort,
       "sfpsTopologyServerTestTopRelayPortName": sfpsTopologyServerTestTopRelayPortName,
       "sfpsTopologyServerTestTopRelayIPAddr": sfpsTopologyServerTestTopRelayIPAddr,
       "sfpsTopologyServerTestTopRelayChassisMAC": sfpsTopologyServerTestTopRelayChassisMAC,
       "sfpsTopologyServerTestTopRelayChassisIP": sfpsTopologyServerTestTopRelayChassisIP,
       "sfpsTopologyServerTestTopRelayFLevel": sfpsTopologyServerTestTopRelayFLevel,
       "sfpsTopologyServerTestTopRelayTopologyAgent": sfpsTopologyServerTestTopRelayTopologyAgent,
       "sfpsTopologyServerPortEventRelayLogicalPort": sfpsTopologyServerPortEventRelayLogicalPort,
       "sfpsTopologyServerPortEventRelayOldState": sfpsTopologyServerPortEventRelayOldState,
       "sfpsTopologyServerPortEventRelayNewState": sfpsTopologyServerPortEventRelayNewState,
       "sfpsNeighborEventsFoundEvents": sfpsNeighborEventsFoundEvents,
       "sfpsNeighborEventsLostEvents": sfpsNeighborEventsLostEvents,
       "sfpsTopologyFCLTable": sfpsTopologyFCLTable,
       "sfpsTopologyFCLEntry": sfpsTopologyFCLEntry,
       "sfpsTopologyFCLFunctionalLevel": sfpsTopologyFCLFunctionalLevel,
       "sfpsTopologyFCLCompatability": sfpsTopologyFCLCompatability,
       "sfpsTopologyFCLThisPortState": sfpsTopologyFCLThisPortState,
       "sfpsTopologyFCLSendPortState": sfpsTopologyFCLSendPortState,
       "sfpsDirViolationTable": sfpsDirViolationTable,
       "sfpsDirViolationEntry": sfpsDirViolationEntry,
       "sfpsDirViolationHash": sfpsDirViolationHash,
       "sfpsDirViolationHashIndex": sfpsDirViolationHashIndex,
       "sfpsDirViolationType": sfpsDirViolationType,
       "sfpsDirViolationSrcPort": sfpsDirViolationSrcPort,
       "sfpsDirViolationAOType": sfpsDirViolationAOType,
       "sfpsDirViolationAOValue": sfpsDirViolationAOValue,
       "sfpsDirViolationLocalPort": sfpsDirViolationLocalPort,
       "sfpsDirViolationCount": sfpsDirViolationCount,
       "sfpsDirViolationLastSeen": sfpsDirViolationLastSeen,
       "sfpsDirViolationFirstSeen": sfpsDirViolationFirstSeen,
       "sfpsDirViolationSrcMac": sfpsDirViolationSrcMac,
       "sfpsDirViolationCPId": sfpsDirViolationCPId,
       "sfpsDirViolationAPIVerb": sfpsDirViolationAPIVerb,
       "sfpsDirViolationAPIViolType": sfpsDirViolationAPIViolType,
       "sfpsDirViolationAPISourcePort": sfpsDirViolationAPISourcePort,
       "sfpsDirViolationAPIAOType": sfpsDirViolationAPIAOType,
       "sfpsDirViolationAPIAOValue": sfpsDirViolationAPIAOValue,
       "sfpsDirViolationAPIChangeCount": sfpsDirViolationAPIChangeCount,
       "sfpsDirViolationAPICPId": sfpsDirViolationAPICPId,
       "sfpsDirViolationDeltaTable": sfpsDirViolationDeltaTable,
       "sfpsDirViolationDeltaEntry": sfpsDirViolationDeltaEntry,
       "sfpsDirViolationDeltaIndex": sfpsDirViolationDeltaIndex,
       "sfpsDirViolationDeltaSrcPort": sfpsDirViolationDeltaSrcPort,
       "sfpsDirViolationDeltaAOType": sfpsDirViolationDeltaAOType,
       "sfpsDirViolationDeltaAOValue": sfpsDirViolationDeltaAOValue,
       "sfpsDirViolationDeltaEntryType": sfpsDirViolationDeltaEntryType,
       "sfpsDirViolationDeltaAPINumEntries": sfpsDirViolationDeltaAPINumEntries,
       "sfpsDirViolationDeltaAPIVerb": sfpsDirViolationDeltaAPIVerb,
       "sfpsRestrictedPortTable": sfpsRestrictedPortTable,
       "sfpsRestrictedPortEntry": sfpsRestrictedPortEntry,
       "sfpsRestrictedPortPort": sfpsRestrictedPortPort,
       "sfpsRestrictedPortHash": sfpsRestrictedPortHash,
       "sfpsRestrictedPortHashIndex": sfpsRestrictedPortHashIndex,
       "sfpsRestrictedPortSrcMac": sfpsRestrictedPortSrcMac,
       "sfpsDirLockConfigUserLocking": sfpsDirLockConfigUserLocking,
       "sfpsDirLockConfigRestrictedPort": sfpsDirLockConfigRestrictedPort,
       "sfpsDirLockConfigRouterPortLock": sfpsDirLockConfigRouterPortLock,
       "sfpsDirLockConfigRAPortLock": sfpsDirLockConfigRAPortLock,
       "sfpsDirLockStatsNumViolators": sfpsDirLockStatsNumViolators,
       "sfpsDirLockStatsNumNodeLocked": sfpsDirLockStatsNumNodeLocked,
       "sfpsDirLockStatsNumAliasLocked": sfpsDirLockStatsNumAliasLocked,
       "sfpsDirLockStatsNumRestrictedPort": sfpsDirLockStatsNumRestrictedPort,
       "sfpsDirLockStatsNumRestrictMob": sfpsDirLockStatsNumRestrictMob,
       "sfpsDirLockStatsViolationTblSize": sfpsDirLockStatsViolationTblSize,
       "sfpsDirLockStatsRestrictPortTblSize": sfpsDirLockStatsRestrictPortTblSize,
       "sfpsDirLockStatsRestrictMobTblSize": sfpsDirLockStatsRestrictMobTblSize,
       "sfpsRestrictedMobilityTable": sfpsRestrictedMobilityTable,
       "sfpsRestrictedMobilityEntry": sfpsRestrictedMobilityEntry,
       "sfpsRestrictedMobilityHash": sfpsRestrictedMobilityHash,
       "sfpsRestrictedMobilityPort": sfpsRestrictedMobilityPort,
       "sfpsRestrictedMobilityHashIndex": sfpsRestrictedMobilityHashIndex,
       "sfpsRestrictedMobilitySrcMac": sfpsRestrictedMobilitySrcMac,
       "sfpsRestrictedMobilitySwitch": sfpsRestrictedMobilitySwitch,
       "sfpsRestrictedMobilityAPIVerb": sfpsRestrictedMobilityAPIVerb,
       "sfpsRestrictedMobilityAPISourcePort": sfpsRestrictedMobilityAPISourcePort,
       "sfpsRestrictedMobilityAPISrcMac": sfpsRestrictedMobilityAPISrcMac,
       "sfpsRestrictedMobilityAPISwitch": sfpsRestrictedMobilityAPISwitch,
       "sfpsDapiNvramStatsVerb": sfpsDapiNvramStatsVerb,
       "sfpsDapiNvramStatsTotalEntries": sfpsDapiNvramStatsTotalEntries,
       "sfpsDapiNvramStatsMacEntries": sfpsDapiNvramStatsMacEntries,
       "sfpsDapiNvramStatsAliasEntries": sfpsDapiNvramStatsAliasEntries,
       "sfpsDapiNvramStatsMaxEntries": sfpsDapiNvramStatsMaxEntries,
       "sfpsDapiNvramStatsNvramUsed": sfpsDapiNvramStatsNvramUsed}
)
