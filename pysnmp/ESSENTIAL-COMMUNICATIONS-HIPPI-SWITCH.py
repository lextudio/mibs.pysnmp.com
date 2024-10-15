# SNMP MIB module (ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:51 2024
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

(ecExperimental,) = mibBuilder.importSymbols(
    "ESSENTIAL-COMMUNICATIONS-GLOBAL-REG",
    "ecExperimental")

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

_EssentialCommunications_ObjectIdentity = ObjectIdentity
essentialCommunications = _EssentialCommunications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159)
)
_EcRoot_ObjectIdentity = ObjectIdentity
ecRoot = _EcRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1)
)
_EcProducts_ObjectIdentity = ObjectIdentity
ecProducts = _EcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3)
)
_HippiSwitchMIBv103_ObjectIdentity = ObjectIdentity
hippiSwitchMIBv103 = _HippiSwitchMIBv103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1)
)
_SwitchObjs_ObjectIdentity = ObjectIdentity
switchObjs = _SwitchObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1)
)
_SwitchDescription_Type = DisplayString
_SwitchDescription_Object = MibScalar
switchDescription = _SwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 1),
    _SwitchDescription_Type()
)
switchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDescription.setStatus("mandatory")
_SwitchNumOfPorts_Type = Gauge32
_SwitchNumOfPorts_Object = MibScalar
switchNumOfPorts = _SwitchNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 2),
    _SwitchNumOfPorts_Type()
)
switchNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumOfPorts.setStatus("mandatory")
_SccDescription_Type = DisplayString
_SccDescription_Object = MibScalar
sccDescription = _SccDescription_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 3),
    _SccDescription_Type()
)
sccDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccDescription.setStatus("mandatory")
_SccDateTime_Type = DisplayString
_SccDateTime_Object = MibScalar
sccDateTime = _SccDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 4),
    _SccDateTime_Type()
)
sccDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sccDateTime.setStatus("mandatory")


class _SccAdminStatus_Type(Integer32):
    """Custom type sccAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("up", 1))
    )


_SccAdminStatus_Type.__name__ = "Integer32"
_SccAdminStatus_Object = MibScalar
sccAdminStatus = _SccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 5),
    _SccAdminStatus_Type()
)
sccAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sccAdminStatus.setStatus("mandatory")


class _SccOperStatus_Type(Integer32):
    """Custom type sccOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("reseting", 2),
          ("up", 1))
    )


_SccOperStatus_Type.__name__ = "Integer32"
_SccOperStatus_Object = MibScalar
sccOperStatus = _SccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 6),
    _SccOperStatus_Type()
)
sccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccOperStatus.setStatus("mandatory")
_BackPlaneTable_Object = MibTable
backPlaneTable = _BackPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    backPlaneTable.setStatus("mandatory")
_BackPlaneEntry_Object = MibTableRow
backPlaneEntry = _BackPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1)
)
backPlaneEntry.setIndexNames(
    (0, "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH", "backPlaneIndex"),
)
if mibBuilder.loadTexts:
    backPlaneEntry.setStatus("mandatory")
_BackPlaneIndex_Type = Gauge32
_BackPlaneIndex_Object = MibTableColumn
backPlaneIndex = _BackPlaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 1),
    _BackPlaneIndex_Type()
)
backPlaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    backPlaneIndex.setStatus("mandatory")
_BackPlaneNumber_Type = Gauge32
_BackPlaneNumber_Object = MibTableColumn
backPlaneNumber = _BackPlaneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 2),
    _BackPlaneNumber_Type()
)
backPlaneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneNumber.setStatus("mandatory")


class _BackPlaneCard_Type(Integer32):
    """Custom type backPlaneCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("parallel", 2),
          ("serial", 3),
          ("unknown", 1))
    )


_BackPlaneCard_Type.__name__ = "Integer32"
_BackPlaneCard_Object = MibTableColumn
backPlaneCard = _BackPlaneCard_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 3),
    _BackPlaneCard_Type()
)
backPlaneCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneCard.setStatus("mandatory")
_MICPowerUpInitError_Type = Gauge32
_MICPowerUpInitError_Object = MibTableColumn
mICPowerUpInitError = _MICPowerUpInitError_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 4),
    _MICPowerUpInitError_Type()
)
mICPowerUpInitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICPowerUpInitError.setStatus("mandatory")
_MICHippiParityBurstError_Type = Gauge32
_MICHippiParityBurstError_Object = MibTableColumn
mICHippiParityBurstError = _MICHippiParityBurstError_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 5),
    _MICHippiParityBurstError_Type()
)
mICHippiParityBurstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICHippiParityBurstError.setStatus("mandatory")
_MICLinkReady_Type = Gauge32
_MICLinkReady_Object = MibTableColumn
mICLinkReady = _MICLinkReady_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 6),
    _MICLinkReady_Type()
)
mICLinkReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICLinkReady.setStatus("mandatory")
_MICSourceInterconnect_Type = Gauge32
_MICSourceInterconnect_Object = MibTableColumn
mICSourceInterconnect = _MICSourceInterconnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 7),
    _MICSourceInterconnect_Type()
)
mICSourceInterconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceInterconnect.setStatus("mandatory")
_MICSourceRequest_Type = Gauge32
_MICSourceRequest_Object = MibTableColumn
mICSourceRequest = _MICSourceRequest_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 8),
    _MICSourceRequest_Type()
)
mICSourceRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceRequest.setStatus("mandatory")
_MICSourceConnect_Type = Gauge32
_MICSourceConnect_Object = MibTableColumn
mICSourceConnect = _MICSourceConnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 9),
    _MICSourceConnect_Type()
)
mICSourceConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceConnect.setStatus("mandatory")
_MICSourceLastConnectAttempt_Type = Gauge32
_MICSourceLastConnectAttempt_Object = MibTableColumn
mICSourceLastConnectAttempt = _MICSourceLastConnectAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 10),
    _MICSourceLastConnectAttempt_Type()
)
mICSourceLastConnectAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceLastConnectAttempt.setStatus("mandatory")
_MICDestinationInterconnect_Type = Gauge32
_MICDestinationInterconnect_Object = MibTableColumn
mICDestinationInterconnect = _MICDestinationInterconnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 11),
    _MICDestinationInterconnect_Type()
)
mICDestinationInterconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationInterconnect.setStatus("mandatory")
_MICDestinationRequest_Type = Gauge32
_MICDestinationRequest_Object = MibTableColumn
mICDestinationRequest = _MICDestinationRequest_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 12),
    _MICDestinationRequest_Type()
)
mICDestinationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationRequest.setStatus("mandatory")
_MICDestinationConnect_Type = Gauge32
_MICDestinationConnect_Object = MibTableColumn
mICDestinationConnect = _MICDestinationConnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 13),
    _MICDestinationConnect_Type()
)
mICDestinationConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationConnect.setStatus("mandatory")
_MICByteCounterOverflow_Type = Gauge32
_MICByteCounterOverflow_Object = MibTableColumn
mICByteCounterOverflow = _MICByteCounterOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 14),
    _MICByteCounterOverflow_Type()
)
mICByteCounterOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICByteCounterOverflow.setStatus("mandatory")
_MICNumberOfBytes_Type = Gauge32
_MICNumberOfBytes_Object = MibTableColumn
mICNumberOfBytes = _MICNumberOfBytes_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 15),
    _MICNumberOfBytes_Type()
)
mICNumberOfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICNumberOfBytes.setStatus("mandatory")
_MICNumberOfPackets_Type = Gauge32
_MICNumberOfPackets_Object = MibTableColumn
mICNumberOfPackets = _MICNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 16),
    _MICNumberOfPackets_Type()
)
mICNumberOfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICNumberOfPackets.setStatus("mandatory")
_MICConnectsSuccessful_Type = Gauge32
_MICConnectsSuccessful_Object = MibTableColumn
mICConnectsSuccessful = _MICConnectsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 7, 1, 17),
    _MICConnectsSuccessful_Type()
)
mICConnectsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICConnectsSuccessful.setStatus("mandatory")
_SourceRouteTable_Object = MibTable
sourceRouteTable = _SourceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sourceRouteTable.setStatus("mandatory")
_SourceRouteEntry_Object = MibTableRow
sourceRouteEntry = _SourceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 8, 1)
)
sourceRouteEntry.setIndexNames(
    (0, "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH", "srcIndex"),
)
if mibBuilder.loadTexts:
    sourceRouteEntry.setStatus("mandatory")
_SrcIndex_Type = Gauge32
_SrcIndex_Object = MibTableColumn
srcIndex = _SrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 8, 1, 1),
    _SrcIndex_Type()
)
srcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIndex.setStatus("mandatory")
_SrcRoute_Type = DisplayString
_SrcRoute_Object = MibTableColumn
srcRoute = _SrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 8, 1, 2),
    _SrcRoute_Type()
)
srcRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRoute.setStatus("mandatory")
_SrcWriteRow_Type = DisplayString
_SrcWriteRow_Object = MibScalar
srcWriteRow = _SrcWriteRow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 9),
    _SrcWriteRow_Type()
)
srcWriteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcWriteRow.setStatus("mandatory")
_DestRouteTable_Object = MibTable
destRouteTable = _DestRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    destRouteTable.setStatus("mandatory")
_DestRouteEntry_Object = MibTableRow
destRouteEntry = _DestRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 10, 1)
)
destRouteEntry.setIndexNames(
    (0, "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH", "destIndex"),
)
if mibBuilder.loadTexts:
    destRouteEntry.setStatus("mandatory")
_DestIndex_Type = Gauge32
_DestIndex_Object = MibTableColumn
destIndex = _DestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 10, 1, 1),
    _DestIndex_Type()
)
destIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destIndex.setStatus("mandatory")
_DestRoute_Type = DisplayString
_DestRoute_Object = MibTableColumn
destRoute = _DestRoute_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 10, 1, 2),
    _DestRoute_Type()
)
destRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destRoute.setStatus("mandatory")
_DestWriteRow_Type = DisplayString
_DestWriteRow_Object = MibScalar
destWriteRow = _DestWriteRow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 11),
    _DestWriteRow_Type()
)
destWriteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destWriteRow.setStatus("mandatory")
_HuntGroupTable_Object = MibTable
huntGroupTable = _HuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    huntGroupTable.setStatus("mandatory")
_HuntGroupEntry_Object = MibTableRow
huntGroupEntry = _HuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 12, 1)
)
huntGroupEntry.setIndexNames(
    (0, "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH", "hg"),
)
if mibBuilder.loadTexts:
    huntGroupEntry.setStatus("mandatory")
_Hg_Type = Gauge32
_Hg_Object = MibTableColumn
hg = _Hg_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 12, 1, 1),
    _Hg_Type()
)
hg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hg.setStatus("mandatory")
_HgOutPortList_Type = DisplayString
_HgOutPortList_Object = MibTableColumn
hgOutPortList = _HgOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 12, 1, 2),
    _HgOutPortList_Type()
)
hgOutPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgOutPortList.setStatus("mandatory")
_HgLWriteRow_Type = DisplayString
_HgLWriteRow_Object = MibScalar
hgLWriteRow = _HgLWriteRow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 13),
    _HgLWriteRow_Type()
)
hgLWriteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgLWriteRow.setStatus("mandatory")
_HuntGroupOrderTable_Object = MibTable
huntGroupOrderTable = _HuntGroupOrderTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    huntGroupOrderTable.setStatus("mandatory")
_HuntGroupOrderEntry_Object = MibTableRow
huntGroupOrderEntry = _HuntGroupOrderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 14, 1)
)
huntGroupOrderEntry.setIndexNames(
    (0, "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH", "hg"),
)
if mibBuilder.loadTexts:
    huntGroupOrderEntry.setStatus("mandatory")
_HgOrderIndex_Type = Gauge32
_HgOrderIndex_Object = MibTableColumn
hgOrderIndex = _HgOrderIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 14, 1, 1),
    _HgOrderIndex_Type()
)
hgOrderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgOrderIndex.setStatus("mandatory")
_HgOrderList_Type = DisplayString
_HgOrderList_Object = MibTableColumn
hgOrderList = _HgOrderList_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 14, 1, 2),
    _HgOrderList_Type()
)
hgOrderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgOrderList.setStatus("mandatory")
_HgOWriteRow_Type = DisplayString
_HgOWriteRow_Object = MibScalar
hgOWriteRow = _HgOWriteRow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 15),
    _HgOWriteRow_Type()
)
hgOWriteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgOWriteRow.setStatus("mandatory")


class _HgSaveRestore_Type(Integer32):
    """Custom type hgSaveRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 2),
          ("save", 1))
    )


_HgSaveRestore_Type.__name__ = "Integer32"
_HgSaveRestore_Object = MibScalar
hgSaveRestore = _HgSaveRestore_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 16),
    _HgSaveRestore_Type()
)
hgSaveRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgSaveRestore.setStatus("mandatory")


class _RoutesSaveRestore_Type(Integer32):
    """Custom type routesSaveRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 2),
          ("save", 1))
    )


_RoutesSaveRestore_Type.__name__ = "Integer32"
_RoutesSaveRestore_Object = MibScalar
routesSaveRestore = _RoutesSaveRestore_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 1, 1, 17),
    _RoutesSaveRestore_Type()
)
routesSaveRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routesSaveRestore.setStatus("mandatory")
_EcExperimental_ObjectIdentity = ObjectIdentity
ecExperimental = _EcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 6)
)
_HippiSwitchMIB_ObjectIdentity = ObjectIdentity
hippiSwitchMIB = _HippiSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESSENTIAL-COMMUNICATIONS-HIPPI-SWITCH",
    **{"essentialCommunications": essentialCommunications,
       "ecRoot": ecRoot,
       "ecProducts": ecProducts,
       "hippiSwitchMIBv103": hippiSwitchMIBv103,
       "switchObjs": switchObjs,
       "switchDescription": switchDescription,
       "switchNumOfPorts": switchNumOfPorts,
       "sccDescription": sccDescription,
       "sccDateTime": sccDateTime,
       "sccAdminStatus": sccAdminStatus,
       "sccOperStatus": sccOperStatus,
       "backPlaneTable": backPlaneTable,
       "backPlaneEntry": backPlaneEntry,
       "backPlaneIndex": backPlaneIndex,
       "backPlaneNumber": backPlaneNumber,
       "backPlaneCard": backPlaneCard,
       "mICPowerUpInitError": mICPowerUpInitError,
       "mICHippiParityBurstError": mICHippiParityBurstError,
       "mICLinkReady": mICLinkReady,
       "mICSourceInterconnect": mICSourceInterconnect,
       "mICSourceRequest": mICSourceRequest,
       "mICSourceConnect": mICSourceConnect,
       "mICSourceLastConnectAttempt": mICSourceLastConnectAttempt,
       "mICDestinationInterconnect": mICDestinationInterconnect,
       "mICDestinationRequest": mICDestinationRequest,
       "mICDestinationConnect": mICDestinationConnect,
       "mICByteCounterOverflow": mICByteCounterOverflow,
       "mICNumberOfBytes": mICNumberOfBytes,
       "mICNumberOfPackets": mICNumberOfPackets,
       "mICConnectsSuccessful": mICConnectsSuccessful,
       "sourceRouteTable": sourceRouteTable,
       "sourceRouteEntry": sourceRouteEntry,
       "srcIndex": srcIndex,
       "srcRoute": srcRoute,
       "srcWriteRow": srcWriteRow,
       "destRouteTable": destRouteTable,
       "destRouteEntry": destRouteEntry,
       "destIndex": destIndex,
       "destRoute": destRoute,
       "destWriteRow": destWriteRow,
       "huntGroupTable": huntGroupTable,
       "huntGroupEntry": huntGroupEntry,
       "hg": hg,
       "hgOutPortList": hgOutPortList,
       "hgLWriteRow": hgLWriteRow,
       "huntGroupOrderTable": huntGroupOrderTable,
       "huntGroupOrderEntry": huntGroupOrderEntry,
       "hgOrderIndex": hgOrderIndex,
       "hgOrderList": hgOrderList,
       "hgOWriteRow": hgOWriteRow,
       "hgSaveRestore": hgSaveRestore,
       "routesSaveRestore": routesSaveRestore,
       "ecExperimental": ecExperimental,
       "hippiSwitchMIB": hippiSwitchMIB}
)
