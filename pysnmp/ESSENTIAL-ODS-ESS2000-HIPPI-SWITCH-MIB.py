# SNMP MIB module (ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:52 2024
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
_Ess2000MIB_ObjectIdentity = ObjectIdentity
ess2000MIB = _Ess2000MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 1)
)
_SwitchDescription_Type = DisplayString
_SwitchDescription_Object = MibScalar
switchDescription = _SwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 1, 1),
    _SwitchDescription_Type()
)
switchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDescription.setStatus("mandatory")
_SwitchNumOfPorts_Type = Gauge32
_SwitchNumOfPorts_Object = MibScalar
switchNumOfPorts = _SwitchNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 1, 2),
    _SwitchNumOfPorts_Type()
)
switchNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumOfPorts.setStatus("mandatory")


class _SwitchSensors_Type(DisplayString):
    """Custom type switchSensors based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SwitchSensors_Type.__name__ = "DisplayString"
_SwitchSensors_Object = MibScalar
switchSensors = _SwitchSensors_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 1, 3),
    _SwitchSensors_Type()
)
switchSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchSensors.setStatus("mandatory")
_SwitchControlCard_ObjectIdentity = ObjectIdentity
switchControlCard = _SwitchControlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 2)
)
_SccDescription_Type = DisplayString
_SccDescription_Object = MibScalar
sccDescription = _SccDescription_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 2, 1),
    _SccDescription_Type()
)
sccDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccDescription.setStatus("mandatory")
_SccDateTime_Type = DisplayString
_SccDateTime_Object = MibScalar
sccDateTime = _SccDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 2, 2),
    _SccDateTime_Type()
)
sccDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sccDateTime.setStatus("mandatory")
_SccAdminStatus_Type = Integer32
_SccAdminStatus_Object = MibScalar
sccAdminStatus = _SccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 2, 3),
    _SccAdminStatus_Type()
)
sccAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sccAdminStatus.setStatus("mandatory")
_SccOperStatus_Type = Integer32
_SccOperStatus_Object = MibScalar
sccOperStatus = _SccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 2, 4),
    _SccOperStatus_Type()
)
sccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccOperStatus.setStatus("mandatory")
_MediaInterfaceCards_ObjectIdentity = ObjectIdentity
mediaInterfaceCards = _MediaInterfaceCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3)
)
_BackPlaneTable_Object = MibTable
backPlaneTable = _BackPlaneTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    backPlaneTable.setStatus("mandatory")
_BackPlaneEntry_Object = MibTableRow
backPlaneEntry = _BackPlaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1)
)
backPlaneEntry.setIndexNames(
    (0, "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "backPlaneIndex"),
)
if mibBuilder.loadTexts:
    backPlaneEntry.setStatus("mandatory")
_BackPlaneIndex_Type = Gauge32
_BackPlaneIndex_Object = MibTableColumn
backPlaneIndex = _BackPlaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 1),
    _BackPlaneIndex_Type()
)
backPlaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    backPlaneIndex.setStatus("mandatory")
_BackPlaneNumber_Type = Gauge32
_BackPlaneNumber_Object = MibTableColumn
backPlaneNumber = _BackPlaneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 2),
    _BackPlaneNumber_Type()
)
backPlaneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneNumber.setStatus("mandatory")
_BackPlaneCard_Type = Integer32
_BackPlaneCard_Object = MibTableColumn
backPlaneCard = _BackPlaneCard_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 3),
    _BackPlaneCard_Type()
)
backPlaneCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backPlaneCard.setStatus("mandatory")
_MICPowerUpInitError_Type = Gauge32
_MICPowerUpInitError_Object = MibTableColumn
mICPowerUpInitError = _MICPowerUpInitError_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 4),
    _MICPowerUpInitError_Type()
)
mICPowerUpInitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICPowerUpInitError.setStatus("mandatory")
_MICHippiParityBurstError_Type = Integer32
_MICHippiParityBurstError_Object = MibTableColumn
mICHippiParityBurstError = _MICHippiParityBurstError_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 5),
    _MICHippiParityBurstError_Type()
)
mICHippiParityBurstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICHippiParityBurstError.setStatus("mandatory")
_MICLinkReady_Type = Gauge32
_MICLinkReady_Object = MibTableColumn
mICLinkReady = _MICLinkReady_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 6),
    _MICLinkReady_Type()
)
mICLinkReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICLinkReady.setStatus("mandatory")
_MICSourceInterconnect_Type = Gauge32
_MICSourceInterconnect_Object = MibTableColumn
mICSourceInterconnect = _MICSourceInterconnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 7),
    _MICSourceInterconnect_Type()
)
mICSourceInterconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceInterconnect.setStatus("mandatory")
_MICSourceRequest_Type = Gauge32
_MICSourceRequest_Object = MibTableColumn
mICSourceRequest = _MICSourceRequest_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 8),
    _MICSourceRequest_Type()
)
mICSourceRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceRequest.setStatus("mandatory")
_MICSourceConnect_Type = Gauge32
_MICSourceConnect_Object = MibTableColumn
mICSourceConnect = _MICSourceConnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 9),
    _MICSourceConnect_Type()
)
mICSourceConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceConnect.setStatus("mandatory")
_MICSourceLastConnectAttempt_Type = Integer32
_MICSourceLastConnectAttempt_Object = MibTableColumn
mICSourceLastConnectAttempt = _MICSourceLastConnectAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 10),
    _MICSourceLastConnectAttempt_Type()
)
mICSourceLastConnectAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICSourceLastConnectAttempt.setStatus("mandatory")
_MICDestinationInterconnect_Type = Gauge32
_MICDestinationInterconnect_Object = MibTableColumn
mICDestinationInterconnect = _MICDestinationInterconnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 11),
    _MICDestinationInterconnect_Type()
)
mICDestinationInterconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationInterconnect.setStatus("mandatory")
_MICDestinationRequest_Type = Gauge32
_MICDestinationRequest_Object = MibTableColumn
mICDestinationRequest = _MICDestinationRequest_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 12),
    _MICDestinationRequest_Type()
)
mICDestinationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationRequest.setStatus("mandatory")
_MICDestinationConnect_Type = Gauge32
_MICDestinationConnect_Object = MibTableColumn
mICDestinationConnect = _MICDestinationConnect_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 13),
    _MICDestinationConnect_Type()
)
mICDestinationConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICDestinationConnect.setStatus("mandatory")
_MICByteCounterOverflow_Type = Gauge32
_MICByteCounterOverflow_Object = MibTableColumn
mICByteCounterOverflow = _MICByteCounterOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 14),
    _MICByteCounterOverflow_Type()
)
mICByteCounterOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICByteCounterOverflow.setStatus("mandatory")
_MICNumberOfBytes_Type = Gauge32
_MICNumberOfBytes_Object = MibTableColumn
mICNumberOfBytes = _MICNumberOfBytes_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 15),
    _MICNumberOfBytes_Type()
)
mICNumberOfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICNumberOfBytes.setStatus("mandatory")
_MICNumberOfPackets_Type = Gauge32
_MICNumberOfPackets_Object = MibTableColumn
mICNumberOfPackets = _MICNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 16),
    _MICNumberOfPackets_Type()
)
mICNumberOfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICNumberOfPackets.setStatus("mandatory")
_MICConnectsSuccessful_Type = Gauge32
_MICConnectsSuccessful_Object = MibTableColumn
mICConnectsSuccessful = _MICConnectsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 3, 1, 1, 17),
    _MICConnectsSuccessful_Type()
)
mICConnectsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICConnectsSuccessful.setStatus("mandatory")
_SourceRoutes_ObjectIdentity = ObjectIdentity
sourceRoutes = _SourceRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4)
)
_SrcRouteTable_Object = MibTable
srcRouteTable = _SrcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    srcRouteTable.setStatus("mandatory")
_SrcRouteEntry_Object = MibTableRow
srcRouteEntry = _SrcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 1, 1)
)
srcRouteEntry.setIndexNames(
    (0, "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "srcIndex"),
)
if mibBuilder.loadTexts:
    srcRouteEntry.setStatus("mandatory")
_SrcIndex_Type = Gauge32
_SrcIndex_Object = MibTableColumn
srcIndex = _SrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 1, 1, 1),
    _SrcIndex_Type()
)
srcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIndex.setStatus("mandatory")


class _SrcRouteInPortAccess_Type(DisplayString):
    """Custom type srcRouteInPortAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SrcRouteInPortAccess_Type.__name__ = "DisplayString"
_SrcRouteInPortAccess_Object = MibTableColumn
srcRouteInPortAccess = _SrcRouteInPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 1, 1, 2),
    _SrcRouteInPortAccess_Type()
)
srcRouteInPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRouteInPortAccess.setStatus("mandatory")


class _SrcRouteOutPortAccess_Type(DisplayString):
    """Custom type srcRouteOutPortAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SrcRouteOutPortAccess_Type.__name__ = "DisplayString"
_SrcRouteOutPortAccess_Object = MibTableColumn
srcRouteOutPortAccess = _SrcRouteOutPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 1, 1, 3),
    _SrcRouteOutPortAccess_Type()
)
srcRouteOutPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRouteOutPortAccess.setStatus("mandatory")
_SrcRouteWrite_Type = DisplayString
_SrcRouteWrite_Object = MibScalar
srcRouteWrite = _SrcRouteWrite_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 2),
    _SrcRouteWrite_Type()
)
srcRouteWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcRouteWrite.setStatus("mandatory")
_SrcSaveRestore_Type = Integer32
_SrcSaveRestore_Object = MibScalar
srcSaveRestore = _SrcSaveRestore_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 4, 3),
    _SrcSaveRestore_Type()
)
srcSaveRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcSaveRestore.setStatus("mandatory")
_LogicalAddressRoutes_ObjectIdentity = ObjectIdentity
logicalAddressRoutes = _LogicalAddressRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5)
)
_DestRouteTable_Object = MibTable
destRouteTable = _DestRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    destRouteTable.setStatus("mandatory")
_DestRouteEntry_Object = MibTableRow
destRouteEntry = _DestRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 1, 1)
)
destRouteEntry.setIndexNames(
    (0, "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "destIndex"),
)
if mibBuilder.loadTexts:
    destRouteEntry.setStatus("mandatory")
_DestIndex_Type = Gauge32
_DestIndex_Object = MibTableColumn
destIndex = _DestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 1, 1, 1),
    _DestIndex_Type()
)
destIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destIndex.setStatus("mandatory")


class _DestRoute_Type(DisplayString):
    """Custom type destRoute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_DestRoute_Type.__name__ = "DisplayString"
_DestRoute_Object = MibTableColumn
destRoute = _DestRoute_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 1, 1, 2),
    _DestRoute_Type()
)
destRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destRoute.setStatus("mandatory")
_DestRouteWrite_Type = DisplayString
_DestRouteWrite_Object = MibScalar
destRouteWrite = _DestRouteWrite_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 2),
    _DestRouteWrite_Type()
)
destRouteWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destRouteWrite.setStatus("mandatory")
_PathRouteTable_Object = MibTable
pathRouteTable = _PathRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    pathRouteTable.setStatus("mandatory")
_PathRouteEntry_Object = MibTableRow
pathRouteEntry = _PathRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 3, 1)
)
pathRouteEntry.setIndexNames(
    (0, "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "pathIndex"),
)
if mibBuilder.loadTexts:
    pathRouteEntry.setStatus("mandatory")
_PathIndex_Type = Gauge32
_PathIndex_Object = MibTableColumn
pathIndex = _PathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 3, 1, 1),
    _PathIndex_Type()
)
pathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathIndex.setStatus("mandatory")


class _PathRoute_Type(DisplayString):
    """Custom type pathRoute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_PathRoute_Type.__name__ = "DisplayString"
_PathRoute_Object = MibTableColumn
pathRoute = _PathRoute_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 3, 1, 2),
    _PathRoute_Type()
)
pathRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathRoute.setStatus("mandatory")
_PathRouteWrite_Type = DisplayString
_PathRouteWrite_Object = MibScalar
pathRouteWrite = _PathRouteWrite_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 4),
    _PathRouteWrite_Type()
)
pathRouteWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathRouteWrite.setStatus("mandatory")
_RoutesSaveRestore_Type = Integer32
_RoutesSaveRestore_Object = MibScalar
routesSaveRestore = _RoutesSaveRestore_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 5),
    _RoutesSaveRestore_Type()
)
routesSaveRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routesSaveRestore.setStatus("mandatory")
_RouteDisable_Type = DisplayString
_RouteDisable_Object = MibScalar
routeDisable = _RouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 5, 6),
    _RouteDisable_Type()
)
routeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDisable.setStatus("mandatory")
_HuntGroups_ObjectIdentity = ObjectIdentity
huntGroups = _HuntGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6)
)
_HGTable_Object = MibTable
hGTable = _HGTable_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hGTable.setStatus("mandatory")
_HGEntry_Object = MibTableRow
hGEntry = _HGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 1, 1)
)
hGEntry.setIndexNames(
    (0, "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "hg"),
)
if mibBuilder.loadTexts:
    hGEntry.setStatus("mandatory")
_Hg_Type = Gauge32
_Hg_Object = MibTableColumn
hg = _Hg_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 1, 1, 1),
    _Hg_Type()
)
hg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hg.setStatus("mandatory")


class _HgList_Type(DisplayString):
    """Custom type hgList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HgList_Type.__name__ = "DisplayString"
_HgList_Object = MibTableColumn
hgList = _HgList_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 1, 1, 2),
    _HgList_Type()
)
hgList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgList.setStatus("mandatory")
_HgWrite_Type = DisplayString
_HgWrite_Object = MibScalar
hgWrite = _HgWrite_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 2),
    _HgWrite_Type()
)
hgWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgWrite.setStatus("mandatory")
_HgSaveRestore_Type = Integer32
_HgSaveRestore_Object = MibScalar
hgSaveRestore = _HgSaveRestore_Object(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 6, 3),
    _HgSaveRestore_Type()
)
hgSaveRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hgSaveRestore.setStatus("mandatory")
_SwitchEvents_ObjectIdentity = ObjectIdentity
switchEvents = _SwitchEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 7)
)
_EcExperimental_ObjectIdentity = ObjectIdentity
ecExperimental = _EcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 6)
)

# Managed Objects groups


# Notification objects

switchSensorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3, 2, 7, 0, 1)
)
switchSensorWarning.setObjects(
    ("ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB", "switchSensors")
)
if mibBuilder.loadTexts:
    switchSensorWarning.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESSENTIAL-ODS-ESS2000-HIPPI-SWITCH-MIB",
    **{"essentialCommunications": essentialCommunications,
       "ecRoot": ecRoot,
       "ecProducts": ecProducts,
       "ess2000MIB": ess2000MIB,
       "switch": switch,
       "switchDescription": switchDescription,
       "switchNumOfPorts": switchNumOfPorts,
       "switchSensors": switchSensors,
       "switchControlCard": switchControlCard,
       "sccDescription": sccDescription,
       "sccDateTime": sccDateTime,
       "sccAdminStatus": sccAdminStatus,
       "sccOperStatus": sccOperStatus,
       "mediaInterfaceCards": mediaInterfaceCards,
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
       "sourceRoutes": sourceRoutes,
       "srcRouteTable": srcRouteTable,
       "srcRouteEntry": srcRouteEntry,
       "srcIndex": srcIndex,
       "srcRouteInPortAccess": srcRouteInPortAccess,
       "srcRouteOutPortAccess": srcRouteOutPortAccess,
       "srcRouteWrite": srcRouteWrite,
       "srcSaveRestore": srcSaveRestore,
       "logicalAddressRoutes": logicalAddressRoutes,
       "destRouteTable": destRouteTable,
       "destRouteEntry": destRouteEntry,
       "destIndex": destIndex,
       "destRoute": destRoute,
       "destRouteWrite": destRouteWrite,
       "pathRouteTable": pathRouteTable,
       "pathRouteEntry": pathRouteEntry,
       "pathIndex": pathIndex,
       "pathRoute": pathRoute,
       "pathRouteWrite": pathRouteWrite,
       "routesSaveRestore": routesSaveRestore,
       "routeDisable": routeDisable,
       "huntGroups": huntGroups,
       "hGTable": hGTable,
       "hGEntry": hGEntry,
       "hg": hg,
       "hgList": hgList,
       "hgWrite": hgWrite,
       "hgSaveRestore": hgSaveRestore,
       "switchEvents": switchEvents,
       "switchSensorWarning": switchSensorWarning,
       "ecExperimental": ecExperimental}
)
