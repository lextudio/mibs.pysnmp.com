# SNMP MIB module (WSD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WSD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:33 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rndErrorDesc,
 rndErrorSeverity,
 rsNWSD,
 rsServerDispatcher,
 rsWSDThresholdWarnings) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsNWSD",
    "rsServerDispatcher",
    "rsWSDThresholdWarnings")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsWSDApplicationServersTable_Object = MibTable
rsWSDApplicationServersTable = _RsWSDApplicationServersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11)
)
if mibBuilder.loadTexts:
    rsWSDApplicationServersTable.setStatus("mandatory")
_RsWSDApplicationServerEntry_Object = MibTableRow
rsWSDApplicationServerEntry = _RsWSDApplicationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1)
)
rsWSDApplicationServerEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDAddr"),
    (0, "WSD-MIB", "rsWSDServerAddr"),
)
if mibBuilder.loadTexts:
    rsWSDApplicationServerEntry.setStatus("mandatory")
_RsWSDAddr_Type = IpAddress
_RsWSDAddr_Object = MibTableColumn
rsWSDAddr = _RsWSDAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 1),
    _RsWSDAddr_Type()
)
rsWSDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDAddr.setStatus("mandatory")
_RsWSDServerAddr_Type = IpAddress
_RsWSDServerAddr_Object = MibTableColumn
rsWSDServerAddr = _RsWSDServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 2),
    _RsWSDServerAddr_Type()
)
rsWSDServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerAddr.setStatus("mandatory")


class _RsWSDServerName_Type(DisplayString):
    """Custom type rsWSDServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsWSDServerName_Type.__name__ = "DisplayString"
_RsWSDServerName_Object = MibTableColumn
rsWSDServerName = _RsWSDServerName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 3),
    _RsWSDServerName_Type()
)
rsWSDServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerName.setStatus("mandatory")


class _RsWSDServerOperStatus_Type(Integer32):
    """Custom type rsWSDServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("noNewSessions", 3),
          ("notInService", 2))
    )


_RsWSDServerOperStatus_Type.__name__ = "Integer32"
_RsWSDServerOperStatus_Object = MibTableColumn
rsWSDServerOperStatus = _RsWSDServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 4),
    _RsWSDServerOperStatus_Type()
)
rsWSDServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerOperStatus.setStatus("mandatory")


class _RsWSDServerWeight_Type(Integer32):
    """Custom type rsWSDServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsWSDServerWeight_Type.__name__ = "Integer32"
_RsWSDServerWeight_Object = MibTableColumn
rsWSDServerWeight = _RsWSDServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 5),
    _RsWSDServerWeight_Type()
)
rsWSDServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerWeight.setStatus("mandatory")
_RsWSDServerAttachedUsersNumber_Type = Integer32
_RsWSDServerAttachedUsersNumber_Object = MibTableColumn
rsWSDServerAttachedUsersNumber = _RsWSDServerAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 6),
    _RsWSDServerAttachedUsersNumber_Type()
)
rsWSDServerAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerAttachedUsersNumber.setStatus("mandatory")
_RsWSDServerPeakLoad_Type = Integer32
_RsWSDServerPeakLoad_Object = MibTableColumn
rsWSDServerPeakLoad = _RsWSDServerPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 7),
    _RsWSDServerPeakLoad_Type()
)
rsWSDServerPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerPeakLoad.setStatus("mandatory")
_RsWSDServerFramesRate_Type = Integer32
_RsWSDServerFramesRate_Object = MibTableColumn
rsWSDServerFramesRate = _RsWSDServerFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 8),
    _RsWSDServerFramesRate_Type()
)
rsWSDServerFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerFramesRate.setStatus("mandatory")
_RsWSDServerFramesLoad_Type = Counter32
_RsWSDServerFramesLoad_Object = MibTableColumn
rsWSDServerFramesLoad = _RsWSDServerFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 9),
    _RsWSDServerFramesLoad_Type()
)
rsWSDServerFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDServerFramesLoad.setStatus("mandatory")


class _RsWSDServerStatus_Type(Integer32):
    """Custom type rsWSDServerStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDServerStatus_Type.__name__ = "Integer32"
_RsWSDServerStatus_Object = MibTableColumn
rsWSDServerStatus = _RsWSDServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 10),
    _RsWSDServerStatus_Type()
)
rsWSDServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerStatus.setStatus("mandatory")


class _RsWSDServerOperMode_Type(Integer32):
    """Custom type rsWSDServerOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("regular", 1))
    )


_RsWSDServerOperMode_Type.__name__ = "Integer32"
_RsWSDServerOperMode_Object = MibTableColumn
rsWSDServerOperMode = _RsWSDServerOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 11),
    _RsWSDServerOperMode_Type()
)
rsWSDServerOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerOperMode.setStatus("mandatory")


class _RsWSDMultiplexedServerPort_Type(Integer32):
    """Custom type rsWSDMultiplexedServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsWSDMultiplexedServerPort_Type.__name__ = "Integer32"
_RsWSDMultiplexedServerPort_Object = MibTableColumn
rsWSDMultiplexedServerPort = _RsWSDMultiplexedServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 12),
    _RsWSDMultiplexedServerPort_Type()
)
rsWSDMultiplexedServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMultiplexedServerPort.setStatus("mandatory")


class _RsWSDServerType_Type(Integer32):
    """Custom type rsWSDServerType based on Integer32"""
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
        *(("distributed", 2),
          ("localFarm", 5),
          ("loopback", 4),
          ("regular", 1),
          ("remote", 3))
    )


_RsWSDServerType_Type.__name__ = "Integer32"
_RsWSDServerType_Object = MibTableColumn
rsWSDServerType = _RsWSDServerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 13),
    _RsWSDServerType_Type()
)
rsWSDServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerType.setStatus("mandatory")
_RsWSDServerConnectionLimit_Type = Integer32
_RsWSDServerConnectionLimit_Object = MibTableColumn
rsWSDServerConnectionLimit = _RsWSDServerConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 14),
    _RsWSDServerConnectionLimit_Type()
)
rsWSDServerConnectionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerConnectionLimit.setStatus("mandatory")


class _RsWSDServerAdminStatus_Type(Integer32):
    """Custom type rsWSDServerAdminStatus based on Integer32"""
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
          ("enable", 1),
          ("shutdown", 3))
    )


_RsWSDServerAdminStatus_Type.__name__ = "Integer32"
_RsWSDServerAdminStatus_Object = MibTableColumn
rsWSDServerAdminStatus = _RsWSDServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 15),
    _RsWSDServerAdminStatus_Type()
)
rsWSDServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerAdminStatus.setStatus("mandatory")
_RsWSDServerBandWidth_Type = Integer32
_RsWSDServerBandWidth_Object = MibTableColumn
rsWSDServerBandWidth = _RsWSDServerBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 16),
    _RsWSDServerBandWidth_Type()
)
rsWSDServerBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerBandWidth.setStatus("mandatory")
_RsWSDServerCckID_Type = Integer32
_RsWSDServerCckID_Object = MibTableColumn
rsWSDServerCckID = _RsWSDServerCckID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 17),
    _RsWSDServerCckID_Type()
)
rsWSDServerCckID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerCckID.setStatus("mandatory")


class _RsWSDServerRedirectTo_Type(DisplayString):
    """Custom type rsWSDServerRedirectTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDServerRedirectTo_Type.__name__ = "DisplayString"
_RsWSDServerRedirectTo_Object = MibTableColumn
rsWSDServerRedirectTo = _RsWSDServerRedirectTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 18),
    _RsWSDServerRedirectTo_Type()
)
rsWSDServerRedirectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerRedirectTo.setStatus("mandatory")


class _RsWSDServerClientNATStatus_Type(Integer32):
    """Custom type rsWSDServerClientNATStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDServerClientNATStatus_Type.__name__ = "Integer32"
_RsWSDServerClientNATStatus_Object = MibTableColumn
rsWSDServerClientNATStatus = _RsWSDServerClientNATStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 1, 19),
    _RsWSDServerClientNATStatus_Type()
)
rsWSDServerClientNATStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServerClientNATStatus.setStatus("mandatory")
_RsWSDdummy1_Type = Integer32
_RsWSDdummy1_Object = MibScalar
rsWSDdummy1 = _RsWSDdummy1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 11, 2),
    _RsWSDdummy1_Type()
)
rsWSDdummy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy1.setStatus("mandatory")
_RsWSDFarmTable_Object = MibTable
rsWSDFarmTable = _RsWSDFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13)
)
if mibBuilder.loadTexts:
    rsWSDFarmTable.setStatus("mandatory")
_RsWSDFarmEntry_Object = MibTableRow
rsWSDFarmEntry = _RsWSDFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1)
)
rsWSDFarmEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDFarmAddress"),
)
if mibBuilder.loadTexts:
    rsWSDFarmEntry.setStatus("mandatory")
_RsWSDFarmAddress_Type = IpAddress
_RsWSDFarmAddress_Object = MibTableColumn
rsWSDFarmAddress = _RsWSDFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 1),
    _RsWSDFarmAddress_Type()
)
rsWSDFarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFarmAddress.setStatus("mandatory")


class _RsWSDFarmName_Type(DisplayString):
    """Custom type rsWSDFarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_RsWSDFarmName_Type.__name__ = "DisplayString"
_RsWSDFarmName_Object = MibTableColumn
rsWSDFarmName = _RsWSDFarmName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 2),
    _RsWSDFarmName_Type()
)
rsWSDFarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmName.setStatus("mandatory")


class _RsWSDAdminStatus_Type(Integer32):
    """Custom type rsWSDAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDAdminStatus_Type.__name__ = "Integer32"
_RsWSDAdminStatus_Object = MibTableColumn
rsWSDAdminStatus = _RsWSDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 3),
    _RsWSDAdminStatus_Type()
)
rsWSDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAdminStatus.setStatus("mandatory")
_RsWSDClientsLifeTime_Type = Integer32
_RsWSDClientsLifeTime_Object = MibTableColumn
rsWSDClientsLifeTime = _RsWSDClientsLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 4),
    _RsWSDClientsLifeTime_Type()
)
rsWSDClientsLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientsLifeTime.setStatus("mandatory")


class _RsWSDDispatchMethod_Type(Integer32):
    """Custom type rsWSDDispatchMethod based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cyclic", 1),
          ("leastTraffic", 2),
          ("leastTrafficLocal", 4),
          ("leastUsersNumber", 3),
          ("leastUsersNumberLocal", 5),
          ("nt-1", 6),
          ("nt-2", 7),
          ("private-1", 8),
          ("private-2", 9),
          ("static", 11),
          ("weightedCyclic", 10))
    )


_RsWSDDispatchMethod_Type.__name__ = "Integer32"
_RsWSDDispatchMethod_Object = MibTableColumn
rsWSDDispatchMethod = _RsWSDDispatchMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 5),
    _RsWSDDispatchMethod_Type()
)
rsWSDDispatchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDispatchMethod.setStatus("mandatory")


class _RsWSDCheckConnectivityStatus_Type(Integer32):
    """Custom type rsWSDCheckConnectivityStatus based on Integer32"""
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
        *(("disable", 2),
          ("http", 3),
          ("ping", 1),
          ("tcp", 4),
          ("udp", 5))
    )


_RsWSDCheckConnectivityStatus_Type.__name__ = "Integer32"
_RsWSDCheckConnectivityStatus_Object = MibTableColumn
rsWSDCheckConnectivityStatus = _RsWSDCheckConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 6),
    _RsWSDCheckConnectivityStatus_Type()
)
rsWSDCheckConnectivityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCheckConnectivityStatus.setStatus("mandatory")
_RsWSDCheckConnectivityMethod_Type = Integer32
_RsWSDCheckConnectivityMethod_Object = MibTableColumn
rsWSDCheckConnectivityMethod = _RsWSDCheckConnectivityMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 7),
    _RsWSDCheckConnectivityMethod_Type()
)
rsWSDCheckConnectivityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCheckConnectivityMethod.setStatus("mandatory")


class _RsWSDCheckConnectivityInterval_Type(Integer32):
    """Custom type rsWSDCheckConnectivityInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsWSDCheckConnectivityInterval_Type.__name__ = "Integer32"
_RsWSDCheckConnectivityInterval_Object = MibTableColumn
rsWSDCheckConnectivityInterval = _RsWSDCheckConnectivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 8),
    _RsWSDCheckConnectivityInterval_Type()
)
rsWSDCheckConnectivityInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCheckConnectivityInterval.setStatus("mandatory")


class _RsWSDCheckConnectivityRetries_Type(Integer32):
    """Custom type rsWSDCheckConnectivityRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RsWSDCheckConnectivityRetries_Type.__name__ = "Integer32"
_RsWSDCheckConnectivityRetries_Object = MibTableColumn
rsWSDCheckConnectivityRetries = _RsWSDCheckConnectivityRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 9),
    _RsWSDCheckConnectivityRetries_Type()
)
rsWSDCheckConnectivityRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCheckConnectivityRetries.setStatus("mandatory")
_RsWSDClientsConnectDenials_Type = Counter32
_RsWSDClientsConnectDenials_Object = MibTableColumn
rsWSDClientsConnectDenials = _RsWSDClientsConnectDenials_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 10),
    _RsWSDClientsConnectDenials_Type()
)
rsWSDClientsConnectDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientsConnectDenials.setStatus("mandatory")


class _RsWSDFarmStatus_Type(Integer32):
    """Custom type rsWSDFarmStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDFarmStatus_Type.__name__ = "Integer32"
_RsWSDFarmStatus_Object = MibTableColumn
rsWSDFarmStatus = _RsWSDFarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 11),
    _RsWSDFarmStatus_Type()
)
rsWSDFarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmStatus.setStatus("mandatory")


class _RsWSDMultiplexedFarmPort_Type(Integer32):
    """Custom type rsWSDMultiplexedFarmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsWSDMultiplexedFarmPort_Type.__name__ = "Integer32"
_RsWSDMultiplexedFarmPort_Object = MibTableColumn
rsWSDMultiplexedFarmPort = _RsWSDMultiplexedFarmPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 12),
    _RsWSDMultiplexedFarmPort_Type()
)
rsWSDMultiplexedFarmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMultiplexedFarmPort.setStatus("mandatory")
_RsWSDFarmDistThreshold_Type = Integer32
_RsWSDFarmDistThreshold_Object = MibTableColumn
rsWSDFarmDistThreshold = _RsWSDFarmDistThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 13),
    _RsWSDFarmDistThreshold_Type()
)
rsWSDFarmDistThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmDistThreshold.setStatus("mandatory")
_RsWSDFarmTrafficThreshold_Type = Integer32
_RsWSDFarmTrafficThreshold_Object = MibTableColumn
rsWSDFarmTrafficThreshold = _RsWSDFarmTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 14),
    _RsWSDFarmTrafficThreshold_Type()
)
rsWSDFarmTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmTrafficThreshold.setStatus("mandatory")


class _RsWSDFarmRedirectionMode_Type(Integer32):
    """Custom type rsWSDFarmRedirectionMode based on Integer32"""
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
        *(("dnsRedirection", 5),
          ("dnsReevaluationRedirection", 6),
          ("httpAndTriangleRedirection", 4),
          ("httpRedirection", 1),
          ("noRedirection", 3),
          ("triangleRedirection", 2))
    )


_RsWSDFarmRedirectionMode_Type.__name__ = "Integer32"
_RsWSDFarmRedirectionMode_Object = MibTableColumn
rsWSDFarmRedirectionMode = _RsWSDFarmRedirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 15),
    _RsWSDFarmRedirectionMode_Type()
)
rsWSDFarmRedirectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmRedirectionMode.setStatus("mandatory")


class _RsNsdFarmRegister_Type(Integer32):
    """Custom type rsNsdFarmRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsNsdFarmRegister_Type.__name__ = "Integer32"
_RsNsdFarmRegister_Object = MibTableColumn
rsNsdFarmRegister = _RsNsdFarmRegister_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 16),
    _RsNsdFarmRegister_Type()
)
rsNsdFarmRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNsdFarmRegister.setStatus("mandatory")


class _RsWSDFarmMode_Type(Integer32):
    """Custom type rsWSDFarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("regular", 1))
    )


_RsWSDFarmMode_Type.__name__ = "Integer32"
_RsWSDFarmMode_Object = MibTableColumn
rsWSDFarmMode = _RsWSDFarmMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 17),
    _RsWSDFarmMode_Type()
)
rsWSDFarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmMode.setStatus("mandatory")
_RsWSDExtendedConnectivityCheckInterval_Type = Integer32
_RsWSDExtendedConnectivityCheckInterval_Object = MibTableColumn
rsWSDExtendedConnectivityCheckInterval = _RsWSDExtendedConnectivityCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 18),
    _RsWSDExtendedConnectivityCheckInterval_Type()
)
rsWSDExtendedConnectivityCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDExtendedConnectivityCheckInterval.setStatus("mandatory")


class _RsWSDConnectivityCheckUrl_Type(DisplayString):
    """Custom type rsWSDConnectivityCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDConnectivityCheckUrl_Type.__name__ = "DisplayString"
_RsWSDConnectivityCheckUrl_Object = MibTableColumn
rsWSDConnectivityCheckUrl = _RsWSDConnectivityCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 19),
    _RsWSDConnectivityCheckUrl_Type()
)
rsWSDConnectivityCheckUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDConnectivityCheckUrl.setStatus("mandatory")


class _RsWSDFarmClientMode_Type(Integer32):
    """Custom type rsWSDFarmClientMode based on Integer32"""
    defaultValue = 1

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
        *(("entryPerSession", 2),
          ("regular", 1),
          ("removeEntryAtSessionEnd", 4),
          ("removeEntryAtSessionEndForServerPerSession", 5),
          ("serverPerSession", 3))
    )


_RsWSDFarmClientMode_Type.__name__ = "Integer32"
_RsWSDFarmClientMode_Object = MibTableColumn
rsWSDFarmClientMode = _RsWSDFarmClientMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 20),
    _RsWSDFarmClientMode_Type()
)
rsWSDFarmClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmClientMode.setStatus("mandatory")


class _RsWSDDNSRedir2ndMode_Type(Integer32):
    """Custom type rsWSDDNSRedir2ndMode based on Integer32"""
    defaultValue = 1

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
        *(("dnsOnly", 4),
          ("http", 2),
          ("httpAndTriangle", 1),
          ("triangulation", 3))
    )


_RsWSDDNSRedir2ndMode_Type.__name__ = "Integer32"
_RsWSDDNSRedir2ndMode_Object = MibTableColumn
rsWSDDNSRedir2ndMode = _RsWSDDNSRedir2ndMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 21),
    _RsWSDDNSRedir2ndMode_Type()
)
rsWSDDNSRedir2ndMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDNSRedir2ndMode.setStatus("mandatory")


class _RsWSDFarmHttpRedirectionMode_Type(Integer32):
    """Custom type rsWSDFarmHttpRedirectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipMode", 1),
          ("nameMode", 2))
    )


_RsWSDFarmHttpRedirectionMode_Type.__name__ = "Integer32"
_RsWSDFarmHttpRedirectionMode_Object = MibTableColumn
rsWSDFarmHttpRedirectionMode = _RsWSDFarmHttpRedirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 22),
    _RsWSDFarmHttpRedirectionMode_Type()
)
rsWSDFarmHttpRedirectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmHttpRedirectionMode.setStatus("mandatory")


class _RsWSDFarmOperStatus_Type(Integer32):
    """Custom type rsWSDFarmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_RsWSDFarmOperStatus_Type.__name__ = "Integer32"
_RsWSDFarmOperStatus_Object = MibTableColumn
rsWSDFarmOperStatus = _RsWSDFarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 23),
    _RsWSDFarmOperStatus_Type()
)
rsWSDFarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFarmOperStatus.setStatus("mandatory")
_RsWSDFarmBandWidth_Type = Integer32
_RsWSDFarmBandWidth_Object = MibTableColumn
rsWSDFarmBandWidth = _RsWSDFarmBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 24),
    _RsWSDFarmBandWidth_Type()
)
rsWSDFarmBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmBandWidth.setStatus("mandatory")


class _RsWSDFarmCookieKey_Type(DisplayString):
    """Custom type rsWSDFarmCookieKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsWSDFarmCookieKey_Type.__name__ = "DisplayString"
_RsWSDFarmCookieKey_Object = MibTableColumn
rsWSDFarmCookieKey = _RsWSDFarmCookieKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 25),
    _RsWSDFarmCookieKey_Type()
)
rsWSDFarmCookieKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmCookieKey.setStatus("mandatory")


class _RsWSDConnCheckUserName_Type(DisplayString):
    """Custom type rsWSDConnCheckUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsWSDConnCheckUserName_Type.__name__ = "DisplayString"
_RsWSDConnCheckUserName_Object = MibTableColumn
rsWSDConnCheckUserName = _RsWSDConnCheckUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 26),
    _RsWSDConnCheckUserName_Type()
)
rsWSDConnCheckUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDConnCheckUserName.setStatus("mandatory")


class _RsWSDConnCheckPassword_Type(DisplayString):
    """Custom type rsWSDConnCheckPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsWSDConnCheckPassword_Type.__name__ = "DisplayString"
_RsWSDConnCheckPassword_Object = MibTableColumn
rsWSDConnCheckPassword = _RsWSDConnCheckPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 1, 27),
    _RsWSDConnCheckPassword_Type()
)
rsWSDConnCheckPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDConnCheckPassword.setStatus("mandatory")
_RsWSDdummy3_Type = Integer32
_RsWSDdummy3_Object = MibScalar
rsWSDdummy3 = _RsWSDdummy3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 13, 2),
    _RsWSDdummy3_Type()
)
rsWSDdummy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy3.setStatus("mandatory")
_RsWSDClientsTable_Object = MibTable
rsWSDClientsTable = _RsWSDClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14)
)
if mibBuilder.loadTexts:
    rsWSDClientsTable.setStatus("mandatory")
_RsWSDClientEntry_Object = MibTableRow
rsWSDClientEntry = _RsWSDClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1)
)
rsWSDClientEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDFarmAddr"),
    (0, "WSD-MIB", "rsWSDClientAddr"),
)
if mibBuilder.loadTexts:
    rsWSDClientEntry.setStatus("mandatory")
_RsWSDFarmAddr_Type = IpAddress
_RsWSDFarmAddr_Object = MibTableColumn
rsWSDFarmAddr = _RsWSDFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 1),
    _RsWSDFarmAddr_Type()
)
rsWSDFarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFarmAddr.setStatus("mandatory")
_RsWSDClientAddr_Type = IpAddress
_RsWSDClientAddr_Object = MibTableColumn
rsWSDClientAddr = _RsWSDClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 2),
    _RsWSDClientAddr_Type()
)
rsWSDClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientAddr.setStatus("mandatory")
_RsWSDAttachedServerAddr_Type = IpAddress
_RsWSDAttachedServerAddr_Object = MibTableColumn
rsWSDAttachedServerAddr = _RsWSDAttachedServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 3),
    _RsWSDAttachedServerAddr_Type()
)
rsWSDAttachedServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAttachedServerAddr.setStatus("mandatory")
_RsWSDClientLastActivityTime_Type = Integer32
_RsWSDClientLastActivityTime_Object = MibTableColumn
rsWSDClientLastActivityTime = _RsWSDClientLastActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 4),
    _RsWSDClientLastActivityTime_Type()
)
rsWSDClientLastActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientLastActivityTime.setStatus("mandatory")
_RsWSDClientAttachmentTime_Type = Integer32
_RsWSDClientAttachmentTime_Object = MibTableColumn
rsWSDClientAttachmentTime = _RsWSDClientAttachmentTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 5),
    _RsWSDClientAttachmentTime_Type()
)
rsWSDClientAttachmentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientAttachmentTime.setStatus("mandatory")


class _RsWSDClientType_Type(Integer32):
    """Custom type rsWSDClientType based on Integer32"""
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
        *(("clientnat", 4),
          ("dynamic", 1),
          ("nat", 3),
          ("static", 2))
    )


_RsWSDClientType_Type.__name__ = "Integer32"
_RsWSDClientType_Object = MibTableColumn
rsWSDClientType = _RsWSDClientType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 6),
    _RsWSDClientType_Type()
)
rsWSDClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientType.setStatus("mandatory")
_RsWSDClientStatus_Type = RowStatus
_RsWSDClientStatus_Object = MibTableColumn
rsWSDClientStatus = _RsWSDClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 1, 7),
    _RsWSDClientStatus_Type()
)
rsWSDClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientStatus.setStatus("mandatory")
_RsWSDdummy4_Type = Integer32
_RsWSDdummy4_Object = MibScalar
rsWSDdummy4 = _RsWSDdummy4_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 14, 2),
    _RsWSDdummy4_Type()
)
rsWSDdummy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy4.setStatus("mandatory")
_RsWSDLoadReportTable_Object = MibTable
rsWSDLoadReportTable = _RsWSDLoadReportTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17)
)
if mibBuilder.loadTexts:
    rsWSDLoadReportTable.setStatus("mandatory")
_RsWSDLoadReportEntry_Object = MibTableRow
rsWSDLoadReportEntry = _RsWSDLoadReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1)
)
rsWSDLoadReportEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDReportFarmAddress"),
    (0, "WSD-MIB", "rsWSDReportDstFarmAddress"),
    (0, "WSD-MIB", "rsWSDReportLclSuperFarmAddr"),
)
if mibBuilder.loadTexts:
    rsWSDLoadReportEntry.setStatus("mandatory")
_RsWSDReportFarmAddress_Type = IpAddress
_RsWSDReportFarmAddress_Object = MibTableColumn
rsWSDReportFarmAddress = _RsWSDReportFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 1),
    _RsWSDReportFarmAddress_Type()
)
rsWSDReportFarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDReportFarmAddress.setStatus("mandatory")
_RsWSDReportDstFarmAddress_Type = IpAddress
_RsWSDReportDstFarmAddress_Object = MibTableColumn
rsWSDReportDstFarmAddress = _RsWSDReportDstFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 2),
    _RsWSDReportDstFarmAddress_Type()
)
rsWSDReportDstFarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDReportDstFarmAddress.setStatus("mandatory")
_RsWSDReportLclSuperFarmAddr_Type = IpAddress
_RsWSDReportLclSuperFarmAddr_Object = MibTableColumn
rsWSDReportLclSuperFarmAddr = _RsWSDReportLclSuperFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 3),
    _RsWSDReportLclSuperFarmAddr_Type()
)
rsWSDReportLclSuperFarmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportLclSuperFarmAddr.setStatus("mandatory")
_RsWSDReportDstIpAddress_Type = IpAddress
_RsWSDReportDstIpAddress_Object = MibTableColumn
rsWSDReportDstIpAddress = _RsWSDReportDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 4),
    _RsWSDReportDstIpAddress_Type()
)
rsWSDReportDstIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportDstIpAddress.setStatus("mandatory")
_RsWSDReportMapFarmAddress_Type = IpAddress
_RsWSDReportMapFarmAddress_Object = MibTableColumn
rsWSDReportMapFarmAddress = _RsWSDReportMapFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 5),
    _RsWSDReportMapFarmAddress_Type()
)
rsWSDReportMapFarmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportMapFarmAddress.setStatus("mandatory")
_RsWSDReportStatus_Type = RowStatus
_RsWSDReportStatus_Object = MibTableColumn
rsWSDReportStatus = _RsWSDReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 6),
    _RsWSDReportStatus_Type()
)
rsWSDReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportStatus.setStatus("mandatory")
_RsWSDReportRdnDstIpAddr_Type = IpAddress
_RsWSDReportRdnDstIpAddr_Object = MibTableColumn
rsWSDReportRdnDstIpAddr = _RsWSDReportRdnDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 7),
    _RsWSDReportRdnDstIpAddr_Type()
)
rsWSDReportRdnDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportRdnDstIpAddr.setStatus("mandatory")
_RsWSDReportDstSuperFarmAddr_Type = IpAddress
_RsWSDReportDstSuperFarmAddr_Object = MibTableColumn
rsWSDReportDstSuperFarmAddr = _RsWSDReportDstSuperFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 1, 8),
    _RsWSDReportDstSuperFarmAddr_Type()
)
rsWSDReportDstSuperFarmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDReportDstSuperFarmAddr.setStatus("mandatory")
_RsWSDdummy6_Type = Integer32
_RsWSDdummy6_Object = MibScalar
rsWSDdummy6 = _RsWSDdummy6_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 17, 2),
    _RsWSDdummy6_Type()
)
rsWSDdummy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy6.setStatus("mandatory")
_RsWSDFarmMappingTable_Object = MibTable
rsWSDFarmMappingTable = _RsWSDFarmMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18)
)
if mibBuilder.loadTexts:
    rsWSDFarmMappingTable.setStatus("mandatory")
_RsWSDFarmMappingEntry_Object = MibTableRow
rsWSDFarmMappingEntry = _RsWSDFarmMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1)
)
rsWSDFarmMappingEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDMappingAddress"),
)
if mibBuilder.loadTexts:
    rsWSDFarmMappingEntry.setStatus("mandatory")
_RsWSDMappingAddress_Type = IpAddress
_RsWSDMappingAddress_Object = MibTableColumn
rsWSDMappingAddress = _RsWSDMappingAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1, 1),
    _RsWSDMappingAddress_Type()
)
rsWSDMappingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMappingAddress.setStatus("mandatory")
_RsWSDMappingFarmAddress_Type = IpAddress
_RsWSDMappingFarmAddress_Object = MibTableColumn
rsWSDMappingFarmAddress = _RsWSDMappingFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1, 2),
    _RsWSDMappingFarmAddress_Type()
)
rsWSDMappingFarmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMappingFarmAddress.setStatus("mandatory")
_RsWSDOriginalAddress_Type = IpAddress
_RsWSDOriginalAddress_Object = MibTableColumn
rsWSDOriginalAddress = _RsWSDOriginalAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1, 3),
    _RsWSDOriginalAddress_Type()
)
rsWSDOriginalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDOriginalAddress.setStatus("mandatory")


class _RsWSDMappingAdminStatus_Type(Integer32):
    """Custom type rsWSDMappingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDMappingAdminStatus_Type.__name__ = "Integer32"
_RsWSDMappingAdminStatus_Object = MibTableColumn
rsWSDMappingAdminStatus = _RsWSDMappingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1, 4),
    _RsWSDMappingAdminStatus_Type()
)
rsWSDMappingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMappingAdminStatus.setStatus("mandatory")
_RsWSDMappingStatus_Type = RowStatus
_RsWSDMappingStatus_Object = MibTableColumn
rsWSDMappingStatus = _RsWSDMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 1, 5),
    _RsWSDMappingStatus_Type()
)
rsWSDMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMappingStatus.setStatus("mandatory")
_RsWSDdummy7_Type = Integer32
_RsWSDdummy7_Object = MibScalar
rsWSDdummy7 = _RsWSDdummy7_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 18, 2),
    _RsWSDdummy7_Type()
)
rsWSDdummy7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy7.setStatus("mandatory")
_RsWSDLoadReportInterval_Type = Integer32
_RsWSDLoadReportInterval_Object = MibScalar
rsWSDLoadReportInterval = _RsWSDLoadReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 24),
    _RsWSDLoadReportInterval_Type()
)
rsWSDLoadReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDLoadReportInterval.setStatus("mandatory")
_RsWSDLoadReportTimeout_Type = Integer32
_RsWSDLoadReportTimeout_Object = MibScalar
rsWSDLoadReportTimeout = _RsWSDLoadReportTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 25),
    _RsWSDLoadReportTimeout_Type()
)
rsWSDLoadReportTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDLoadReportTimeout.setStatus("mandatory")
_RsWSDPortFarmTable_Object = MibTable
rsWSDPortFarmTable = _RsWSDPortFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30)
)
if mibBuilder.loadTexts:
    rsWSDPortFarmTable.setStatus("mandatory")
_RsWSDPortFarmEntry_Object = MibTableRow
rsWSDPortFarmEntry = _RsWSDPortFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1)
)
rsWSDPortFarmEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDPortMainAddress"),
    (0, "WSD-MIB", "rsWSDPortNumber"),
)
if mibBuilder.loadTexts:
    rsWSDPortFarmEntry.setStatus("mandatory")
_RsWSDPortMainAddress_Type = IpAddress
_RsWSDPortMainAddress_Object = MibTableColumn
rsWSDPortMainAddress = _RsWSDPortMainAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1, 1),
    _RsWSDPortMainAddress_Type()
)
rsWSDPortMainAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortMainAddress.setStatus("mandatory")
_RsWSDPortNumber_Type = Integer32
_RsWSDPortNumber_Object = MibTableColumn
rsWSDPortNumber = _RsWSDPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1, 2),
    _RsWSDPortNumber_Type()
)
rsWSDPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortNumber.setStatus("mandatory")
_RsWSDPortFarmAddress_Type = IpAddress
_RsWSDPortFarmAddress_Object = MibTableColumn
rsWSDPortFarmAddress = _RsWSDPortFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1, 3),
    _RsWSDPortFarmAddress_Type()
)
rsWSDPortFarmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPortFarmAddress.setStatus("mandatory")
_RsWSDPortFarmStatus_Type = RowStatus
_RsWSDPortFarmStatus_Object = MibTableColumn
rsWSDPortFarmStatus = _RsWSDPortFarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1, 4),
    _RsWSDPortFarmStatus_Type()
)
rsWSDPortFarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPortFarmStatus.setStatus("mandatory")


class _RsWSDPortFarmHeader_Type(DisplayString):
    """Custom type rsWSDPortFarmHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_RsWSDPortFarmHeader_Type.__name__ = "DisplayString"
_RsWSDPortFarmHeader_Object = MibTableColumn
rsWSDPortFarmHeader = _RsWSDPortFarmHeader_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 1, 5),
    _RsWSDPortFarmHeader_Type()
)
rsWSDPortFarmHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPortFarmHeader.setStatus("mandatory")
_RsWSDdummy10_Type = Integer32
_RsWSDdummy10_Object = MibScalar
rsWSDdummy10 = _RsWSDdummy10_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 30, 2),
    _RsWSDdummy10_Type()
)
rsWSDdummy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy10.setStatus("mandatory")
_RsWSDProximity_ObjectIdentity = ObjectIdentity
rsWSDProximity = _RsWSDProximity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32)
)
_RsWSDStaticProximityTable_Object = MibTable
rsWSDStaticProximityTable = _RsWSDStaticProximityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1)
)
if mibBuilder.loadTexts:
    rsWSDStaticProximityTable.setStatus("mandatory")
_RsWSDStaticProximityEntry_Object = MibTableRow
rsWSDStaticProximityEntry = _RsWSDStaticProximityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1)
)
rsWSDStaticProximityEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDStaticProximityFarmAddress"),
    (0, "WSD-MIB", "rsWSDStaticProximityRangeFrom"),
)
if mibBuilder.loadTexts:
    rsWSDStaticProximityEntry.setStatus("mandatory")
_RsWSDStaticProximityFarmAddress_Type = IpAddress
_RsWSDStaticProximityFarmAddress_Object = MibTableColumn
rsWSDStaticProximityFarmAddress = _RsWSDStaticProximityFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 1),
    _RsWSDStaticProximityFarmAddress_Type()
)
rsWSDStaticProximityFarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDStaticProximityFarmAddress.setStatus("mandatory")
_RsWSDStaticProximityRangeFrom_Type = IpAddress
_RsWSDStaticProximityRangeFrom_Object = MibTableColumn
rsWSDStaticProximityRangeFrom = _RsWSDStaticProximityRangeFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 2),
    _RsWSDStaticProximityRangeFrom_Type()
)
rsWSDStaticProximityRangeFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDStaticProximityRangeFrom.setStatus("mandatory")
_RsWSDStaticProximityRangeTo_Type = IpAddress
_RsWSDStaticProximityRangeTo_Object = MibTableColumn
rsWSDStaticProximityRangeTo = _RsWSDStaticProximityRangeTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 3),
    _RsWSDStaticProximityRangeTo_Type()
)
rsWSDStaticProximityRangeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticProximityRangeTo.setStatus("mandatory")


class _RsWSDStaticProximityStatus_Type(Integer32):
    """Custom type rsWSDStaticProximityStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDStaticProximityStatus_Type.__name__ = "Integer32"
_RsWSDStaticProximityStatus_Object = MibTableColumn
rsWSDStaticProximityStatus = _RsWSDStaticProximityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 4),
    _RsWSDStaticProximityStatus_Type()
)
rsWSDStaticProximityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticProximityStatus.setStatus("mandatory")
_RsWSDStaticProximityServer1_Type = IpAddress
_RsWSDStaticProximityServer1_Object = MibTableColumn
rsWSDStaticProximityServer1 = _RsWSDStaticProximityServer1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 5),
    _RsWSDStaticProximityServer1_Type()
)
rsWSDStaticProximityServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticProximityServer1.setStatus("mandatory")
_RsWSDStaticProximityServer2_Type = IpAddress
_RsWSDStaticProximityServer2_Object = MibTableColumn
rsWSDStaticProximityServer2 = _RsWSDStaticProximityServer2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 6),
    _RsWSDStaticProximityServer2_Type()
)
rsWSDStaticProximityServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticProximityServer2.setStatus("mandatory")
_RsWSDStaticProximityServer3_Type = IpAddress
_RsWSDStaticProximityServer3_Object = MibTableColumn
rsWSDStaticProximityServer3 = _RsWSDStaticProximityServer3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 1, 1, 7),
    _RsWSDStaticProximityServer3_Type()
)
rsWSDStaticProximityServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticProximityServer3.setStatus("mandatory")


class _RsWSDProximityOperationMode_Type(Integer32):
    """Custom type rsWSDProximityOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullProximity", 3),
          ("noProximity", 1),
          ("staticProximity", 2))
    )


_RsWSDProximityOperationMode_Type.__name__ = "Integer32"
_RsWSDProximityOperationMode_Object = MibScalar
rsWSDProximityOperationMode = _RsWSDProximityOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 2),
    _RsWSDProximityOperationMode_Type()
)
rsWSDProximityOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityOperationMode.setStatus("mandatory")
_RsWSDProximityMainDNS_Type = IpAddress
_RsWSDProximityMainDNS_Object = MibScalar
rsWSDProximityMainDNS = _RsWSDProximityMainDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 3),
    _RsWSDProximityMainDNS_Type()
)
rsWSDProximityMainDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityMainDNS.setStatus("mandatory")
_RsWSDProximityBackupDNS_Type = IpAddress
_RsWSDProximityBackupDNS_Object = MibScalar
rsWSDProximityBackupDNS = _RsWSDProximityBackupDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 4),
    _RsWSDProximityBackupDNS_Type()
)
rsWSDProximityBackupDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityBackupDNS.setStatus("mandatory")
_RsWSDProximityAgingPeriod_Type = Integer32
_RsWSDProximityAgingPeriod_Object = MibScalar
rsWSDProximityAgingPeriod = _RsWSDProximityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 5),
    _RsWSDProximityAgingPeriod_Type()
)
rsWSDProximityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityAgingPeriod.setStatus("mandatory")


class _RsWSDProximityClientMode_Type(Integer32):
    """Custom type rsWSDProximityClientMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDProximityClientMode_Type.__name__ = "Integer32"
_RsWSDProximityClientMode_Object = MibScalar
rsWSDProximityClientMode = _RsWSDProximityClientMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 6),
    _RsWSDProximityClientMode_Type()
)
rsWSDProximityClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityClientMode.setStatus("mandatory")


class _RsWSDProximityRetries_Type(Integer32):
    """Custom type rsWSDProximityRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RsWSDProximityRetries_Type.__name__ = "Integer32"
_RsWSDProximityRetries_Object = MibScalar
rsWSDProximityRetries = _RsWSDProximityRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 7),
    _RsWSDProximityRetries_Type()
)
rsWSDProximityRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityRetries.setStatus("mandatory")


class _RsWSDProximityTimeout_Type(Integer32):
    """Custom type rsWSDProximityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsWSDProximityTimeout_Type.__name__ = "Integer32"
_RsWSDProximityTimeout_Object = MibScalar
rsWSDProximityTimeout = _RsWSDProximityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 8),
    _RsWSDProximityTimeout_Type()
)
rsWSDProximityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityTimeout.setStatus("mandatory")
_RsWSDProximityTuning_ObjectIdentity = ObjectIdentity
rsWSDProximityTuning = _RsWSDProximityTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 9)
)
_RsWSDMaxDynEntries_Type = Integer32
_RsWSDMaxDynEntries_Object = MibScalar
rsWSDMaxDynEntries = _RsWSDMaxDynEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 9, 1),
    _RsWSDMaxDynEntries_Type()
)
rsWSDMaxDynEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMaxDynEntries.setStatus("mandatory")
_RsWSDMaxDynEntriesAfterReset_Type = Integer32
_RsWSDMaxDynEntriesAfterReset_Object = MibScalar
rsWSDMaxDynEntriesAfterReset = _RsWSDMaxDynEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 9, 2),
    _RsWSDMaxDynEntriesAfterReset_Type()
)
rsWSDMaxDynEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMaxDynEntriesAfterReset.setStatus("mandatory")


class _RsWSDPrxBasicCheckMethod_Type(Integer32):
    """Custom type rsWSDPrxBasicCheckMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDPrxBasicCheckMethod_Type.__name__ = "Integer32"
_RsWSDPrxBasicCheckMethod_Object = MibScalar
rsWSDPrxBasicCheckMethod = _RsWSDPrxBasicCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 10),
    _RsWSDPrxBasicCheckMethod_Type()
)
rsWSDPrxBasicCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrxBasicCheckMethod.setStatus("mandatory")


class _RsWSDPrxAdvancedCheckMethod_Type(Integer32):
    """Custom type rsWSDPrxAdvancedCheckMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDPrxAdvancedCheckMethod_Type.__name__ = "Integer32"
_RsWSDPrxAdvancedCheckMethod_Object = MibScalar
rsWSDPrxAdvancedCheckMethod = _RsWSDPrxAdvancedCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 11),
    _RsWSDPrxAdvancedCheckMethod_Type()
)
rsWSDPrxAdvancedCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrxAdvancedCheckMethod.setStatus("mandatory")


class _RsWSDPrxApplIndpndCheckMethod_Type(Integer32):
    """Custom type rsWSDPrxApplIndpndCheckMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDPrxApplIndpndCheckMethod_Type.__name__ = "Integer32"
_RsWSDPrxApplIndpndCheckMethod_Object = MibScalar
rsWSDPrxApplIndpndCheckMethod = _RsWSDPrxApplIndpndCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 12),
    _RsWSDPrxApplIndpndCheckMethod_Type()
)
rsWSDPrxApplIndpndCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrxApplIndpndCheckMethod.setStatus("mandatory")


class _RsWSDPrxApplAwareCheckMethod_Type(Integer32):
    """Custom type rsWSDPrxApplAwareCheckMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDPrxApplAwareCheckMethod_Type.__name__ = "Integer32"
_RsWSDPrxApplAwareCheckMethod_Object = MibScalar
rsWSDPrxApplAwareCheckMethod = _RsWSDPrxApplAwareCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 32, 13),
    _RsWSDPrxApplAwareCheckMethod_Type()
)
rsWSDPrxApplAwareCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrxApplAwareCheckMethod.setStatus("mandatory")
_RsNWSDProximity_ObjectIdentity = ObjectIdentity
rsNWSDProximity = _RsNWSDProximity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1)
)


class _RsWSDProximityHopsWeight_Type(Integer32):
    """Custom type rsWSDProximityHopsWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityHopsWeight_Type.__name__ = "Integer32"
_RsWSDProximityHopsWeight_Object = MibScalar
rsWSDProximityHopsWeight = _RsWSDProximityHopsWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 1),
    _RsWSDProximityHopsWeight_Type()
)
rsWSDProximityHopsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityHopsWeight.setStatus("mandatory")


class _RsWSDProximityLatencyWeight_Type(Integer32):
    """Custom type rsWSDProximityLatencyWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityLatencyWeight_Type.__name__ = "Integer32"
_RsWSDProximityLatencyWeight_Object = MibScalar
rsWSDProximityLatencyWeight = _RsWSDProximityLatencyWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 2),
    _RsWSDProximityLatencyWeight_Type()
)
rsWSDProximityLatencyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityLatencyWeight.setStatus("mandatory")


class _RsWSDProximityLoadWeight_Type(Integer32):
    """Custom type rsWSDProximityLoadWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityLoadWeight_Type.__name__ = "Integer32"
_RsWSDProximityLoadWeight_Object = MibScalar
rsWSDProximityLoadWeight = _RsWSDProximityLoadWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 3),
    _RsWSDProximityLoadWeight_Type()
)
rsWSDProximityLoadWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityLoadWeight.setStatus("mandatory")


class _RsWSDProximityMirrorPercentage_Type(Integer32):
    """Custom type rsWSDProximityMirrorPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityMirrorPercentage_Type.__name__ = "Integer32"
_RsWSDProximityMirrorPercentage_Object = MibScalar
rsWSDProximityMirrorPercentage = _RsWSDProximityMirrorPercentage_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 4),
    _RsWSDProximityMirrorPercentage_Type()
)
rsWSDProximityMirrorPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityMirrorPercentage.setStatus("mandatory")
_RsWSDProximityMirrorPollingTime_Type = Integer32
_RsWSDProximityMirrorPollingTime_Object = MibScalar
rsWSDProximityMirrorPollingTime = _RsWSDProximityMirrorPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 5),
    _RsWSDProximityMirrorPollingTime_Type()
)
rsWSDProximityMirrorPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityMirrorPollingTime.setStatus("mandatory")
_RsWSDDNSttl_Type = Integer32
_RsWSDDNSttl_Object = MibScalar
rsWSDDNSttl = _RsWSDDNSttl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 2),
    _RsWSDDNSttl_Type()
)
rsWSDDNSttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDNSttl.setStatus("mandatory")
_RsWSDURLSuperFarmTable_Object = MibTable
rsWSDURLSuperFarmTable = _RsWSDURLSuperFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3)
)
if mibBuilder.loadTexts:
    rsWSDURLSuperFarmTable.setStatus("mandatory")
_RsWSDURLSuperFarmEntry_Object = MibTableRow
rsWSDURLSuperFarmEntry = _RsWSDURLSuperFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1)
)
rsWSDURLSuperFarmEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDURL"),
)
if mibBuilder.loadTexts:
    rsWSDURLSuperFarmEntry.setStatus("mandatory")
_RsWSDURLFarmAddress_Type = IpAddress
_RsWSDURLFarmAddress_Object = MibTableColumn
rsWSDURLFarmAddress = _RsWSDURLFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 1),
    _RsWSDURLFarmAddress_Type()
)
rsWSDURLFarmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLFarmAddress.setStatus("mandatory")


class _RsWSDURL_Type(DisplayString):
    """Custom type rsWSDURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RsWSDURL_Type.__name__ = "DisplayString"
_RsWSDURL_Object = MibTableColumn
rsWSDURL = _RsWSDURL_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 2),
    _RsWSDURL_Type()
)
rsWSDURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURL.setStatus("mandatory")
_RsWSDURLStatus_Type = RowStatus
_RsWSDURLStatus_Object = MibTableColumn
rsWSDURLStatus = _RsWSDURLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 3),
    _RsWSDURLStatus_Type()
)
rsWSDURLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLStatus.setStatus("mandatory")
_RsWSDMainVirtualDNS_Type = IpAddress
_RsWSDMainVirtualDNS_Object = MibScalar
rsWSDMainVirtualDNS = _RsWSDMainVirtualDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 4),
    _RsWSDMainVirtualDNS_Type()
)
rsWSDMainVirtualDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMainVirtualDNS.setStatus("mandatory")
_RsWSDBackupVirtualDNS_Type = IpAddress
_RsWSDBackupVirtualDNS_Object = MibScalar
rsWSDBackupVirtualDNS = _RsWSDBackupVirtualDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 5),
    _RsWSDBackupVirtualDNS_Type()
)
rsWSDBackupVirtualDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDBackupVirtualDNS.setStatus("mandatory")


class _RsWSDProximityMirrorProtocolMode_Type(Integer32):
    """Custom type rsWSDProximityMirrorProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDProximityMirrorProtocolMode_Type.__name__ = "Integer32"
_RsWSDProximityMirrorProtocolMode_Object = MibScalar
rsWSDProximityMirrorProtocolMode = _RsWSDProximityMirrorProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 7),
    _RsWSDProximityMirrorProtocolMode_Type()
)
rsWSDProximityMirrorProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityMirrorProtocolMode.setStatus("mandatory")


class _RsWSDTwoDNSAnswers_Type(Integer32):
    """Custom type rsWSDTwoDNSAnswers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDTwoDNSAnswers_Type.__name__ = "Integer32"
_RsWSDTwoDNSAnswers_Object = MibScalar
rsWSDTwoDNSAnswers = _RsWSDTwoDNSAnswers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 10),
    _RsWSDTwoDNSAnswers_Type()
)
rsWSDTwoDNSAnswers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTwoDNSAnswers.setStatus("mandatory")
_RsWSDStatisticsDstIpAddr_Type = IpAddress
_RsWSDStatisticsDstIpAddr_Object = MibScalar
rsWSDStatisticsDstIpAddr = _RsWSDStatisticsDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 11),
    _RsWSDStatisticsDstIpAddr_Type()
)
rsWSDStatisticsDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStatisticsDstIpAddr.setStatus("mandatory")


class _RsWSDStatisticsReportingMode_Type(Integer32):
    """Custom type rsWSDStatisticsReportingMode based on Integer32"""
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
        *(("disable", 2),
          ("full", 1),
          ("general", 3),
          ("health", 4))
    )


_RsWSDStatisticsReportingMode_Type.__name__ = "Integer32"
_RsWSDStatisticsReportingMode_Object = MibScalar
rsWSDStatisticsReportingMode = _RsWSDStatisticsReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 12),
    _RsWSDStatisticsReportingMode_Type()
)
rsWSDStatisticsReportingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStatisticsReportingMode.setStatus("mandatory")
_RsWSDGeneralStatisticsPollingTime_Type = Integer32
_RsWSDGeneralStatisticsPollingTime_Object = MibScalar
rsWSDGeneralStatisticsPollingTime = _RsWSDGeneralStatisticsPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 13),
    _RsWSDGeneralStatisticsPollingTime_Type()
)
rsWSDGeneralStatisticsPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDGeneralStatisticsPollingTime.setStatus("mandatory")
_RsWSDHealthStatisticsPollingTime_Type = Integer32
_RsWSDHealthStatisticsPollingTime_Object = MibScalar
rsWSDHealthStatisticsPollingTime = _RsWSDHealthStatisticsPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 14),
    _RsWSDHealthStatisticsPollingTime_Type()
)
rsWSDHealthStatisticsPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHealthStatisticsPollingTime.setStatus("mandatory")
_RsWSDAcceptableHTTPCodesTable_Object = MibTable
rsWSDAcceptableHTTPCodesTable = _RsWSDAcceptableHTTPCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 15)
)
if mibBuilder.loadTexts:
    rsWSDAcceptableHTTPCodesTable.setStatus("mandatory")
_RsWSDAcceptableHTTPCodeEntry_Object = MibTableRow
rsWSDAcceptableHTTPCodeEntry = _RsWSDAcceptableHTTPCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 15, 1)
)
rsWSDAcceptableHTTPCodeEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDAcceptableHTTPCodeFarm"),
    (0, "WSD-MIB", "rsWSDAcceptableHTTPCode"),
)
if mibBuilder.loadTexts:
    rsWSDAcceptableHTTPCodeEntry.setStatus("mandatory")
_RsWSDAcceptableHTTPCodeFarm_Type = IpAddress
_RsWSDAcceptableHTTPCodeFarm_Object = MibTableColumn
rsWSDAcceptableHTTPCodeFarm = _RsWSDAcceptableHTTPCodeFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 15, 1, 1),
    _RsWSDAcceptableHTTPCodeFarm_Type()
)
rsWSDAcceptableHTTPCodeFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAcceptableHTTPCodeFarm.setStatus("mandatory")
_RsWSDAcceptableHTTPCode_Type = Integer32
_RsWSDAcceptableHTTPCode_Object = MibTableColumn
rsWSDAcceptableHTTPCode = _RsWSDAcceptableHTTPCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 15, 1, 2),
    _RsWSDAcceptableHTTPCode_Type()
)
rsWSDAcceptableHTTPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAcceptableHTTPCode.setStatus("mandatory")
_RsWSDAcceptableHTTPCodeStatus_Type = RowStatus
_RsWSDAcceptableHTTPCodeStatus_Object = MibTableColumn
rsWSDAcceptableHTTPCodeStatus = _RsWSDAcceptableHTTPCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 15, 1, 3),
    _RsWSDAcceptableHTTPCodeStatus_Type()
)
rsWSDAcceptableHTTPCodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAcceptableHTTPCodeStatus.setStatus("mandatory")


class _RsWSDTotalNumberOfClients_Type(OctetString):
    """Custom type rsWSDTotalNumberOfClients based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsWSDTotalNumberOfClients_Type.__name__ = "OctetString"
_RsWSDTotalNumberOfClients_Object = MibScalar
rsWSDTotalNumberOfClients = _RsWSDTotalNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 16),
    _RsWSDTotalNumberOfClients_Type()
)
rsWSDTotalNumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDTotalNumberOfClients.setStatus("mandatory")
_RsWSDCurrentNumberOfClients_Type = Integer32
_RsWSDCurrentNumberOfClients_Object = MibScalar
rsWSDCurrentNumberOfClients = _RsWSDCurrentNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 17),
    _RsWSDCurrentNumberOfClients_Type()
)
rsWSDCurrentNumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDCurrentNumberOfClients.setStatus("mandatory")


class _RsWSDFramesLoadInBytes_Type(OctetString):
    """Custom type rsWSDFramesLoadInBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsWSDFramesLoadInBytes_Type.__name__ = "OctetString"
_RsWSDFramesLoadInBytes_Object = MibScalar
rsWSDFramesLoadInBytes = _RsWSDFramesLoadInBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 18),
    _RsWSDFramesLoadInBytes_Type()
)
rsWSDFramesLoadInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFramesLoadInBytes.setStatus("mandatory")
_RsWSDRedundancyFailed_Type = Integer32
_RsWSDRedundancyFailed_Object = MibScalar
rsWSDRedundancyFailed = _RsWSDRedundancyFailed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 19),
    _RsWSDRedundancyFailed_Type()
)
rsWSDRedundancyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDRedundancyFailed.setStatus("mandatory")
_RsWSDRedundancyTakeOver_Type = Integer32
_RsWSDRedundancyTakeOver_Object = MibScalar
rsWSDRedundancyTakeOver = _RsWSDRedundancyTakeOver_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 20),
    _RsWSDRedundancyTakeOver_Type()
)
rsWSDRedundancyTakeOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDRedundancyTakeOver.setStatus("mandatory")
_RsWSDDynamicProximityTableFilledUp_Type = Integer32
_RsWSDDynamicProximityTableFilledUp_Object = MibScalar
rsWSDDynamicProximityTableFilledUp = _RsWSDDynamicProximityTableFilledUp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 21),
    _RsWSDDynamicProximityTableFilledUp_Type()
)
rsWSDDynamicProximityTableFilledUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDDynamicProximityTableFilledUp.setStatus("mandatory")
_RsWSDClientTableFilledUp_Type = Integer32
_RsWSDClientTableFilledUp_Object = MibScalar
rsWSDClientTableFilledUp = _RsWSDClientTableFilledUp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 22),
    _RsWSDClientTableFilledUp_Type()
)
rsWSDClientTableFilledUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientTableFilledUp.setStatus("mandatory")
_RsWSDSSFTable_Object = MibTable
rsWSDSSFTable = _RsWSDSSFTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23)
)
if mibBuilder.loadTexts:
    rsWSDSSFTable.setStatus("mandatory")
_RsWSDSSFEntry_Object = MibTableRow
rsWSDSSFEntry = _RsWSDSSFEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1)
)
rsWSDSSFEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDSSFName"),
)
if mibBuilder.loadTexts:
    rsWSDSSFEntry.setStatus("mandatory")


class _RsWSDSSFName_Type(DisplayString):
    """Custom type rsWSDSSFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDSSFName_Type.__name__ = "DisplayString"
_RsWSDSSFName_Object = MibTableColumn
rsWSDSSFName = _RsWSDSSFName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 1),
    _RsWSDSSFName_Type()
)
rsWSDSSFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFName.setStatus("mandatory")


class _RsWSDSSFStatus_Type(Integer32):
    """Custom type rsWSDSSFStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDSSFStatus_Type.__name__ = "Integer32"
_RsWSDSSFStatus_Object = MibTableColumn
rsWSDSSFStatus = _RsWSDSSFStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 2),
    _RsWSDSSFStatus_Type()
)
rsWSDSSFStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFStatus.setStatus("mandatory")


class _RsWSDSSFCheckMethod_Type(Integer32):
    """Custom type rsWSDSSFCheckMethod based on Integer32"""
    defaultValue = 2

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
        *(("disable", 1),
          ("oAS", 4),
          ("oDB", 5),
          ("ping", 2),
          ("tcp", 3))
    )


_RsWSDSSFCheckMethod_Type.__name__ = "Integer32"
_RsWSDSSFCheckMethod_Object = MibTableColumn
rsWSDSSFCheckMethod = _RsWSDSSFCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 3),
    _RsWSDSSFCheckMethod_Type()
)
rsWSDSSFCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFCheckMethod.setStatus("mandatory")


class _RsWSDSSFCheckInterval_Type(Integer32):
    """Custom type rsWSDSSFCheckInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsWSDSSFCheckInterval_Type.__name__ = "Integer32"
_RsWSDSSFCheckInterval_Object = MibTableColumn
rsWSDSSFCheckInterval = _RsWSDSSFCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 4),
    _RsWSDSSFCheckInterval_Type()
)
rsWSDSSFCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFCheckInterval.setStatus("mandatory")


class _RsWSDSSFCheckRetries_Type(Integer32):
    """Custom type rsWSDSSFCheckRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RsWSDSSFCheckRetries_Type.__name__ = "Integer32"
_RsWSDSSFCheckRetries_Object = MibTableColumn
rsWSDSSFCheckRetries = _RsWSDSSFCheckRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 5),
    _RsWSDSSFCheckRetries_Type()
)
rsWSDSSFCheckRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFCheckRetries.setStatus("mandatory")


class _RsWSDSSFCheckPort_Type(Integer32):
    """Custom type rsWSDSSFCheckPort based on Integer32"""
    defaultValue = 80


_RsWSDSSFCheckPort_Object = MibTableColumn
rsWSDSSFCheckPort = _RsWSDSSFCheckPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 6),
    _RsWSDSSFCheckPort_Type()
)
rsWSDSSFCheckPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFCheckPort.setStatus("mandatory")


class _RsWSDSSFCheckCommunity_Type(DisplayString):
    """Custom type rsWSDSSFCheckCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDSSFCheckCommunity_Type.__name__ = "DisplayString"
_RsWSDSSFCheckCommunity_Object = MibTableColumn
rsWSDSSFCheckCommunity = _RsWSDSSFCheckCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 7),
    _RsWSDSSFCheckCommunity_Type()
)
rsWSDSSFCheckCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFCheckCommunity.setStatus("mandatory")


class _RsWSDSSFMode_Type(Integer32):
    """Custom type rsWSDSSFMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inclusive", 1),
          ("singleFailure", 2))
    )


_RsWSDSSFMode_Type.__name__ = "Integer32"
_RsWSDSSFMode_Object = MibTableColumn
rsWSDSSFMode = _RsWSDSSFMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 8),
    _RsWSDSSFMode_Type()
)
rsWSDSSFMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFMode.setStatus("mandatory")


class _RsWSDSSFOperStatus_Type(Integer32):
    """Custom type rsWSDSSFOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_RsWSDSSFOperStatus_Type.__name__ = "Integer32"
_RsWSDSSFOperStatus_Object = MibTableColumn
rsWSDSSFOperStatus = _RsWSDSSFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 9),
    _RsWSDSSFOperStatus_Type()
)
rsWSDSSFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSSFOperStatus.setStatus("mandatory")
_RsWSDSSFId_Type = Integer32
_RsWSDSSFId_Object = MibTableColumn
rsWSDSSFId = _RsWSDSSFId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 23, 1, 10),
    _RsWSDSSFId_Type()
)
rsWSDSSFId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFId.setStatus("mandatory")
_RsWSDSecondaryServerTable_Object = MibTable
rsWSDSecondaryServerTable = _RsWSDSecondaryServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24)
)
if mibBuilder.loadTexts:
    rsWSDSecondaryServerTable.setStatus("mandatory")
_RsWSDSecondaryServerEntry_Object = MibTableRow
rsWSDSecondaryServerEntry = _RsWSDSecondaryServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1)
)
rsWSDSecondaryServerEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDSecondaryServerSSFName"),
    (0, "WSD-MIB", "rsWSDSecondaryServerAddr"),
)
if mibBuilder.loadTexts:
    rsWSDSecondaryServerEntry.setStatus("mandatory")


class _RsWSDSecondaryServerSSFName_Type(DisplayString):
    """Custom type rsWSDSecondaryServerSSFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDSecondaryServerSSFName_Type.__name__ = "DisplayString"
_RsWSDSecondaryServerSSFName_Object = MibTableColumn
rsWSDSecondaryServerSSFName = _RsWSDSecondaryServerSSFName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1, 1),
    _RsWSDSecondaryServerSSFName_Type()
)
rsWSDSecondaryServerSSFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSecondaryServerSSFName.setStatus("mandatory")
_RsWSDSecondaryServerAddr_Type = IpAddress
_RsWSDSecondaryServerAddr_Object = MibTableColumn
rsWSDSecondaryServerAddr = _RsWSDSecondaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1, 2),
    _RsWSDSecondaryServerAddr_Type()
)
rsWSDSecondaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSecondaryServerAddr.setStatus("mandatory")


class _RsWSDSecondaryServerStatus_Type(Integer32):
    """Custom type rsWSDSecondaryServerStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDSecondaryServerStatus_Type.__name__ = "Integer32"
_RsWSDSecondaryServerStatus_Object = MibTableColumn
rsWSDSecondaryServerStatus = _RsWSDSecondaryServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1, 3),
    _RsWSDSecondaryServerStatus_Type()
)
rsWSDSecondaryServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSecondaryServerStatus.setStatus("mandatory")


class _RsWSDSecondaryServerOperStatus_Type(Integer32):
    """Custom type rsWSDSecondaryServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_RsWSDSecondaryServerOperStatus_Type.__name__ = "Integer32"
_RsWSDSecondaryServerOperStatus_Object = MibTableColumn
rsWSDSecondaryServerOperStatus = _RsWSDSecondaryServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1, 4),
    _RsWSDSecondaryServerOperStatus_Type()
)
rsWSDSecondaryServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSecondaryServerOperStatus.setStatus("mandatory")
_RsWSDSecondaryServerId_Type = Integer32
_RsWSDSecondaryServerId_Object = MibTableColumn
rsWSDSecondaryServerId = _RsWSDSecondaryServerId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 24, 1, 5),
    _RsWSDSecondaryServerId_Type()
)
rsWSDSecondaryServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSecondaryServerId.setStatus("mandatory")
_RsWSDSSFFarmTable_Object = MibTable
rsWSDSSFFarmTable = _RsWSDSSFFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25)
)
if mibBuilder.loadTexts:
    rsWSDSSFFarmTable.setStatus("mandatory")
_RsWSDSSFFarmEntry_Object = MibTableRow
rsWSDSSFFarmEntry = _RsWSDSSFFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25, 1)
)
rsWSDSSFFarmEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDSSFFarmSSFName"),
    (0, "WSD-MIB", "rsWSDSSFFarmAddr"),
)
if mibBuilder.loadTexts:
    rsWSDSSFFarmEntry.setStatus("mandatory")


class _RsWSDSSFFarmSSFName_Type(DisplayString):
    """Custom type rsWSDSSFFarmSSFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDSSFFarmSSFName_Type.__name__ = "DisplayString"
_RsWSDSSFFarmSSFName_Object = MibTableColumn
rsWSDSSFFarmSSFName = _RsWSDSSFFarmSSFName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25, 1, 1),
    _RsWSDSSFFarmSSFName_Type()
)
rsWSDSSFFarmSSFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFFarmSSFName.setStatus("mandatory")
_RsWSDSSFFarmAddr_Type = IpAddress
_RsWSDSSFFarmAddr_Object = MibTableColumn
rsWSDSSFFarmAddr = _RsWSDSSFFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25, 1, 2),
    _RsWSDSSFFarmAddr_Type()
)
rsWSDSSFFarmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFFarmAddr.setStatus("mandatory")


class _RsWSDSSFFarmStatus_Type(Integer32):
    """Custom type rsWSDSSFFarmStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDSSFFarmStatus_Type.__name__ = "Integer32"
_RsWSDSSFFarmStatus_Object = MibTableColumn
rsWSDSSFFarmStatus = _RsWSDSSFFarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25, 1, 3),
    _RsWSDSSFFarmStatus_Type()
)
rsWSDSSFFarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFFarmStatus.setStatus("mandatory")
_RsWSDSSFFarmId_Type = Integer32
_RsWSDSSFFarmId_Object = MibTableColumn
rsWSDSSFFarmId = _RsWSDSSFFarmId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 25, 1, 4),
    _RsWSDSSFFarmId_Type()
)
rsWSDSSFFarmId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFFarmId.setStatus("mandatory")
_RsWSDClientGroupingMask_Type = IpAddress
_RsWSDClientGroupingMask_Object = MibScalar
rsWSDClientGroupingMask = _RsWSDClientGroupingMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 26),
    _RsWSDClientGroupingMask_Type()
)
rsWSDClientGroupingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientGroupingMask.setStatus("mandatory")
_RsWSDSSFServerTable_Object = MibTable
rsWSDSSFServerTable = _RsWSDSSFServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27)
)
if mibBuilder.loadTexts:
    rsWSDSSFServerTable.setStatus("mandatory")
_RsWSDSSFServerEntry_Object = MibTableRow
rsWSDSSFServerEntry = _RsWSDSSFServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1)
)
rsWSDSSFServerEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDSSFServerSSFName"),
    (0, "WSD-MIB", "rsWSDSSFServerFarmAddr"),
    (0, "WSD-MIB", "rsWSDSSFServerSrvrAddr"),
)
if mibBuilder.loadTexts:
    rsWSDSSFServerEntry.setStatus("mandatory")


class _RsWSDSSFServerSSFName_Type(DisplayString):
    """Custom type rsWSDSSFServerSSFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDSSFServerSSFName_Type.__name__ = "DisplayString"
_RsWSDSSFServerSSFName_Object = MibTableColumn
rsWSDSSFServerSSFName = _RsWSDSSFServerSSFName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1, 1),
    _RsWSDSSFServerSSFName_Type()
)
rsWSDSSFServerSSFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFServerSSFName.setStatus("mandatory")
_RsWSDSSFServerFarmAddr_Type = IpAddress
_RsWSDSSFServerFarmAddr_Object = MibTableColumn
rsWSDSSFServerFarmAddr = _RsWSDSSFServerFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1, 2),
    _RsWSDSSFServerFarmAddr_Type()
)
rsWSDSSFServerFarmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFServerFarmAddr.setStatus("mandatory")
_RsWSDSSFServerSrvrAddr_Type = IpAddress
_RsWSDSSFServerSrvrAddr_Object = MibTableColumn
rsWSDSSFServerSrvrAddr = _RsWSDSSFServerSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1, 3),
    _RsWSDSSFServerSrvrAddr_Type()
)
rsWSDSSFServerSrvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFServerSrvrAddr.setStatus("mandatory")


class _RsWSDSSFServerStatus_Type(Integer32):
    """Custom type rsWSDSSFServerStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDSSFServerStatus_Type.__name__ = "Integer32"
_RsWSDSSFServerStatus_Object = MibTableColumn
rsWSDSSFServerStatus = _RsWSDSSFServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1, 4),
    _RsWSDSSFServerStatus_Type()
)
rsWSDSSFServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFServerStatus.setStatus("mandatory")
_RsWSDSSFServerId_Type = Integer32
_RsWSDSSFServerId_Object = MibTableColumn
rsWSDSSFServerId = _RsWSDSSFServerId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 27, 1, 5),
    _RsWSDSSFServerId_Type()
)
rsWSDSSFServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSSFServerId.setStatus("mandatory")
_RsWSDHTTPContentCheckTable_Object = MibTable
rsWSDHTTPContentCheckTable = _RsWSDHTTPContentCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28)
)
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckTable.setStatus("mandatory")
_RsWSDHTTPContentCheckEntry_Object = MibTableRow
rsWSDHTTPContentCheckEntry = _RsWSDHTTPContentCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28, 1)
)
rsWSDHTTPContentCheckEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDHTTPContentCheckFarm"),
)
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckEntry.setStatus("mandatory")
_RsWSDHTTPContentCheckFarm_Type = IpAddress
_RsWSDHTTPContentCheckFarm_Object = MibTableColumn
rsWSDHTTPContentCheckFarm = _RsWSDHTTPContentCheckFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28, 1, 1),
    _RsWSDHTTPContentCheckFarm_Type()
)
rsWSDHTTPContentCheckFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckFarm.setStatus("mandatory")


class _RsWSDHTTPContentCheckString_Type(DisplayString):
    """Custom type rsWSDHTTPContentCheckString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RsWSDHTTPContentCheckString_Type.__name__ = "DisplayString"
_RsWSDHTTPContentCheckString_Object = MibTableColumn
rsWSDHTTPContentCheckString = _RsWSDHTTPContentCheckString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28, 1, 2),
    _RsWSDHTTPContentCheckString_Type()
)
rsWSDHTTPContentCheckString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckString.setStatus("mandatory")


class _RsWSDHTTPContentCheckMode_Type(Integer32):
    """Custom type rsWSDHTTPContentCheckMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stringExists", 1),
          ("stringIsAbsent", 2))
    )


_RsWSDHTTPContentCheckMode_Type.__name__ = "Integer32"
_RsWSDHTTPContentCheckMode_Object = MibTableColumn
rsWSDHTTPContentCheckMode = _RsWSDHTTPContentCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28, 1, 3),
    _RsWSDHTTPContentCheckMode_Type()
)
rsWSDHTTPContentCheckMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckMode.setStatus("mandatory")
_RsWSDHTTPContentCheckStatus_Type = RowStatus
_RsWSDHTTPContentCheckStatus_Object = MibTableColumn
rsWSDHTTPContentCheckStatus = _RsWSDHTTPContentCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 28, 1, 4),
    _RsWSDHTTPContentCheckStatus_Type()
)
rsWSDHTTPContentCheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHTTPContentCheckStatus.setStatus("mandatory")
_RsNWSDStats_ObjectIdentity = ObjectIdentity
rsNWSDStats = _RsNWSDStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29)
)


class _RsWSDTotalDNSReqCounter_Type(OctetString):
    """Custom type rsWSDTotalDNSReqCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsWSDTotalDNSReqCounter_Type.__name__ = "OctetString"
_RsWSDTotalDNSReqCounter_Object = MibScalar
rsWSDTotalDNSReqCounter = _RsWSDTotalDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 1),
    _RsWSDTotalDNSReqCounter_Type()
)
rsWSDTotalDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDTotalDNSReqCounter.setStatus("mandatory")


class _RsWSDAnsweredDNSReqCounter_Type(OctetString):
    """Custom type rsWSDAnsweredDNSReqCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsWSDAnsweredDNSReqCounter_Type.__name__ = "OctetString"
_RsWSDAnsweredDNSReqCounter_Object = MibScalar
rsWSDAnsweredDNSReqCounter = _RsWSDAnsweredDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 2),
    _RsWSDAnsweredDNSReqCounter_Type()
)
rsWSDAnsweredDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDAnsweredDNSReqCounter.setStatus("mandatory")


class _RsWSDBadDNSReqCounter_Type(OctetString):
    """Custom type rsWSDBadDNSReqCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsWSDBadDNSReqCounter_Type.__name__ = "OctetString"
_RsWSDBadDNSReqCounter_Object = MibScalar
rsWSDBadDNSReqCounter = _RsWSDBadDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 3),
    _RsWSDBadDNSReqCounter_Type()
)
rsWSDBadDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDBadDNSReqCounter.setStatus("mandatory")
_RsWSDTotalDNSReqLastSecCounter_Type = Integer32
_RsWSDTotalDNSReqLastSecCounter_Object = MibScalar
rsWSDTotalDNSReqLastSecCounter = _RsWSDTotalDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 4),
    _RsWSDTotalDNSReqLastSecCounter_Type()
)
rsWSDTotalDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDTotalDNSReqLastSecCounter.setStatus("mandatory")
_RsWSDAnsweredDNSReqLastSecCounter_Type = Integer32
_RsWSDAnsweredDNSReqLastSecCounter_Object = MibScalar
rsWSDAnsweredDNSReqLastSecCounter = _RsWSDAnsweredDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 5),
    _RsWSDAnsweredDNSReqLastSecCounter_Type()
)
rsWSDAnsweredDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDAnsweredDNSReqLastSecCounter.setStatus("mandatory")
_RsWSDBadDNSReqLastSecCounter_Type = Integer32
_RsWSDBadDNSReqLastSecCounter_Object = MibScalar
rsWSDBadDNSReqLastSecCounter = _RsWSDBadDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 6),
    _RsWSDBadDNSReqLastSecCounter_Type()
)
rsWSDBadDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDBadDNSReqLastSecCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsTable_Object = MibTable
rsNWSDFarmStatisticsTable = _RsNWSDFarmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7)
)
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTable.setStatus("mandatory")
_RsNWSDFarmStatisticsEntry_Object = MibTableRow
rsNWSDFarmStatisticsEntry = _RsNWSDFarmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1)
)
rsNWSDFarmStatisticsEntry.setIndexNames(
    (0, "WSD-MIB", "rsNWSDFarmStatisticsAddress"),
)
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsEntry.setStatus("mandatory")
_RsNWSDFarmStatisticsAddress_Type = IpAddress
_RsNWSDFarmStatisticsAddress_Object = MibTableColumn
rsNWSDFarmStatisticsAddress = _RsNWSDFarmStatisticsAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 1),
    _RsNWSDFarmStatisticsAddress_Type()
)
rsNWSDFarmStatisticsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsAddress.setStatus("mandatory")
_RsNWSDFarmStatisticsAttachedUsersNumber_Type = Integer32
_RsNWSDFarmStatisticsAttachedUsersNumber_Object = MibTableColumn
rsNWSDFarmStatisticsAttachedUsersNumber = _RsNWSDFarmStatisticsAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 2),
    _RsNWSDFarmStatisticsAttachedUsersNumber_Type()
)
rsNWSDFarmStatisticsAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsAttachedUsersNumber.setStatus("mandatory")


class _RsNWSDFarmStatisticsTotalAttachedUsersNumber_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsTotalAttachedUsersNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsTotalAttachedUsersNumber_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsTotalAttachedUsersNumber_Object = MibTableColumn
rsNWSDFarmStatisticsTotalAttachedUsersNumber = _RsNWSDFarmStatisticsTotalAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 3),
    _RsNWSDFarmStatisticsTotalAttachedUsersNumber_Type()
)
rsNWSDFarmStatisticsTotalAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalAttachedUsersNumber.setStatus("mandatory")
_RsNWSDFarmStatisticsPeakLoad_Type = Integer32
_RsNWSDFarmStatisticsPeakLoad_Object = MibTableColumn
rsNWSDFarmStatisticsPeakLoad = _RsNWSDFarmStatisticsPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 4),
    _RsNWSDFarmStatisticsPeakLoad_Type()
)
rsNWSDFarmStatisticsPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsPeakLoad.setStatus("mandatory")


class _RsNWSDFarmStatisticsFramesLoad_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsFramesLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsFramesLoad_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsFramesLoad_Object = MibTableColumn
rsNWSDFarmStatisticsFramesLoad = _RsNWSDFarmStatisticsFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 5),
    _RsNWSDFarmStatisticsFramesLoad_Type()
)
rsNWSDFarmStatisticsFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsFramesLoad.setStatus("mandatory")
_RsNWSDFarmStatisticsFramesRate_Type = Integer32
_RsNWSDFarmStatisticsFramesRate_Object = MibTableColumn
rsNWSDFarmStatisticsFramesRate = _RsNWSDFarmStatisticsFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 6),
    _RsNWSDFarmStatisticsFramesRate_Type()
)
rsNWSDFarmStatisticsFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsFramesRate.setStatus("mandatory")


class _RsNWSDFarmStatisticsFramesLoadInBytes_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsFramesLoadInBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsFramesLoadInBytes_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsFramesLoadInBytes_Object = MibTableColumn
rsNWSDFarmStatisticsFramesLoadInBytes = _RsNWSDFarmStatisticsFramesLoadInBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 7),
    _RsNWSDFarmStatisticsFramesLoadInBytes_Type()
)
rsNWSDFarmStatisticsFramesLoadInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsFramesLoadInBytes.setStatus("mandatory")
_RsNWSDFarmStatisticsFramesRateInBytes_Type = Counter32
_RsNWSDFarmStatisticsFramesRateInBytes_Object = MibTableColumn
rsNWSDFarmStatisticsFramesRateInBytes = _RsNWSDFarmStatisticsFramesRateInBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 8),
    _RsNWSDFarmStatisticsFramesRateInBytes_Type()
)
rsNWSDFarmStatisticsFramesRateInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsFramesRateInBytes.setStatus("mandatory")
_RsNWSDFarmStatisticsBackupServerUsed_Type = Integer32
_RsNWSDFarmStatisticsBackupServerUsed_Object = MibTableColumn
rsNWSDFarmStatisticsBackupServerUsed = _RsNWSDFarmStatisticsBackupServerUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 9),
    _RsNWSDFarmStatisticsBackupServerUsed_Type()
)
rsNWSDFarmStatisticsBackupServerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsBackupServerUsed.setStatus("mandatory")
_RsNWSDFarmStatisticsDistThresholdReached_Type = Integer32
_RsNWSDFarmStatisticsDistThresholdReached_Object = MibTableColumn
rsNWSDFarmStatisticsDistThresholdReached = _RsNWSDFarmStatisticsDistThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 10),
    _RsNWSDFarmStatisticsDistThresholdReached_Type()
)
rsNWSDFarmStatisticsDistThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsDistThresholdReached.setStatus("mandatory")
_RsNWSDFarmStatisticsCapacityThresholdReached_Type = Integer32
_RsNWSDFarmStatisticsCapacityThresholdReached_Object = MibTableColumn
rsNWSDFarmStatisticsCapacityThresholdReached = _RsNWSDFarmStatisticsCapacityThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 11),
    _RsNWSDFarmStatisticsCapacityThresholdReached_Type()
)
rsNWSDFarmStatisticsCapacityThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsCapacityThresholdReached.setStatus("mandatory")
_RsNWSDFarmStatisticsTotalDNSReqCounter_Type = Counter32
_RsNWSDFarmStatisticsTotalDNSReqCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalDNSReqCounter = _RsNWSDFarmStatisticsTotalDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 12),
    _RsNWSDFarmStatisticsTotalDNSReqCounter_Type()
)
rsNWSDFarmStatisticsTotalDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalDNSReqCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsTotalDNSReqLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsTotalDNSReqLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalDNSReqLastSecCounter = _RsNWSDFarmStatisticsTotalDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 13),
    _RsNWSDFarmStatisticsTotalDNSReqLastSecCounter_Type()
)
rsNWSDFarmStatisticsTotalDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalDNSReqLastSecCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter_Type = Counter32
_RsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter = _RsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 14),
    _RsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter_Type()
)
rsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter = _RsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 15),
    _RsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter_Type()
)
rsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsRedirectedDNSReqCounter_Type = Counter32
_RsNWSDFarmStatisticsRedirectedDNSReqCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedDNSReqCounter = _RsNWSDFarmStatisticsRedirectedDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 16),
    _RsNWSDFarmStatisticsRedirectedDNSReqCounter_Type()
)
rsNWSDFarmStatisticsRedirectedDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedDNSReqCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter = _RsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 17),
    _RsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter_Type()
)
rsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsTotalHTTPSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsTotalHTTPSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsTotalHTTPSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsTotalHTTPSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalHTTPSessionsCounter = _RsNWSDFarmStatisticsTotalHTTPSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 18),
    _RsNWSDFarmStatisticsTotalHTTPSessionsCounter_Type()
)
rsNWSDFarmStatisticsTotalHTTPSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalHTTPSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter = _RsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 19),
    _RsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsLocalHTTPSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsLocalHTTPSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsLocalHTTPSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsLocalHTTPSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalHTTPSessionsCounter = _RsNWSDFarmStatisticsLocalHTTPSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 20),
    _RsNWSDFarmStatisticsLocalHTTPSessionsCounter_Type()
)
rsNWSDFarmStatisticsLocalHTTPSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalHTTPSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter = _RsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 21),
    _RsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsRedirectedHTTPSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsRedirectedHTTPSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsRedirectedHTTPSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter = _RsNWSDFarmStatisticsRedirectedHTTPSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 22),
    _RsNWSDFarmStatisticsRedirectedHTTPSessionsCounter_Type()
)
rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter = _RsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 23),
    _RsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsTotalTriangSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsTotalTriangSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsTotalTriangSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsTotalTriangSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalTriangSessionsCounter = _RsNWSDFarmStatisticsTotalTriangSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 24),
    _RsNWSDFarmStatisticsTotalTriangSessionsCounter_Type()
)
rsNWSDFarmStatisticsTotalTriangSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalTriangSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter = _RsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 25),
    _RsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsLocalTriangSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsLocalTriangSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsLocalTriangSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsLocalTriangSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalTriangSessionsCounter = _RsNWSDFarmStatisticsLocalTriangSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 26),
    _RsNWSDFarmStatisticsLocalTriangSessionsCounter_Type()
)
rsNWSDFarmStatisticsLocalTriangSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalTriangSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter = _RsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 27),
    _RsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDFarmStatisticsRedirectedTriangSessionsCounter_Type(OctetString):
    """Custom type rsNWSDFarmStatisticsRedirectedTriangSessionsCounter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDFarmStatisticsRedirectedTriangSessionsCounter_Type.__name__ = "OctetString"
_RsNWSDFarmStatisticsRedirectedTriangSessionsCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedTriangSessionsCounter = _RsNWSDFarmStatisticsRedirectedTriangSessionsCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 28),
    _RsNWSDFarmStatisticsRedirectedTriangSessionsCounter_Type()
)
rsNWSDFarmStatisticsRedirectedTriangSessionsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedTriangSessionsCounter.setStatus("mandatory")
_RsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter_Type = Counter32
_RsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter_Object = MibTableColumn
rsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter = _RsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 7, 1, 29),
    _RsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter_Type()
)
rsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter.setStatus("mandatory")
_RsNWSDServerStatisticsTable_Object = MibTable
rsNWSDServerStatisticsTable = _RsNWSDServerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8)
)
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsTable.setStatus("mandatory")
_RsNWSDServerStatisticsEntry_Object = MibTableRow
rsNWSDServerStatisticsEntry = _RsNWSDServerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1)
)
rsNWSDServerStatisticsEntry.setIndexNames(
    (0, "WSD-MIB", "rsNWSDServerStatisticsFarmAddr"),
    (0, "WSD-MIB", "rsNWSDServerStatisticsServerAddr"),
)
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsEntry.setStatus("mandatory")
_RsNWSDServerStatisticsFarmAddr_Type = IpAddress
_RsNWSDServerStatisticsFarmAddr_Object = MibTableColumn
rsNWSDServerStatisticsFarmAddr = _RsNWSDServerStatisticsFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 1),
    _RsNWSDServerStatisticsFarmAddr_Type()
)
rsNWSDServerStatisticsFarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsFarmAddr.setStatus("mandatory")
_RsNWSDServerStatisticsServerAddr_Type = IpAddress
_RsNWSDServerStatisticsServerAddr_Object = MibTableColumn
rsNWSDServerStatisticsServerAddr = _RsNWSDServerStatisticsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 2),
    _RsNWSDServerStatisticsServerAddr_Type()
)
rsNWSDServerStatisticsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsServerAddr.setStatus("mandatory")
_RsNWSDServerStatisticsAttachedUsersNumber_Type = Integer32
_RsNWSDServerStatisticsAttachedUsersNumber_Object = MibTableColumn
rsNWSDServerStatisticsAttachedUsersNumber = _RsNWSDServerStatisticsAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 3),
    _RsNWSDServerStatisticsAttachedUsersNumber_Type()
)
rsNWSDServerStatisticsAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsAttachedUsersNumber.setStatus("mandatory")
_RsNWSDServerStatisticsPeakLoad_Type = Integer32
_RsNWSDServerStatisticsPeakLoad_Object = MibTableColumn
rsNWSDServerStatisticsPeakLoad = _RsNWSDServerStatisticsPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 4),
    _RsNWSDServerStatisticsPeakLoad_Type()
)
rsNWSDServerStatisticsPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsPeakLoad.setStatus("mandatory")
_RsNWSDServerStatisticsFramesRate_Type = Integer32
_RsNWSDServerStatisticsFramesRate_Object = MibTableColumn
rsNWSDServerStatisticsFramesRate = _RsNWSDServerStatisticsFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 5),
    _RsNWSDServerStatisticsFramesRate_Type()
)
rsNWSDServerStatisticsFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsFramesRate.setStatus("mandatory")


class _RsNWSDServerStatisticsFramesLoad_Type(OctetString):
    """Custom type rsNWSDServerStatisticsFramesLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDServerStatisticsFramesLoad_Type.__name__ = "OctetString"
_RsNWSDServerStatisticsFramesLoad_Object = MibTableColumn
rsNWSDServerStatisticsFramesLoad = _RsNWSDServerStatisticsFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 6),
    _RsNWSDServerStatisticsFramesLoad_Type()
)
rsNWSDServerStatisticsFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsFramesLoad.setStatus("mandatory")


class _RsNWSDServerStatisticsTotalAttachedUsersNumber_Type(OctetString):
    """Custom type rsNWSDServerStatisticsTotalAttachedUsersNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDServerStatisticsTotalAttachedUsersNumber_Type.__name__ = "OctetString"
_RsNWSDServerStatisticsTotalAttachedUsersNumber_Object = MibTableColumn
rsNWSDServerStatisticsTotalAttachedUsersNumber = _RsNWSDServerStatisticsTotalAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 7),
    _RsNWSDServerStatisticsTotalAttachedUsersNumber_Type()
)
rsNWSDServerStatisticsTotalAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsTotalAttachedUsersNumber.setStatus("mandatory")


class _RsNWSDServerStatisticsFramesLoadInBytes_Type(OctetString):
    """Custom type rsNWSDServerStatisticsFramesLoadInBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDServerStatisticsFramesLoadInBytes_Type.__name__ = "OctetString"
_RsNWSDServerStatisticsFramesLoadInBytes_Object = MibTableColumn
rsNWSDServerStatisticsFramesLoadInBytes = _RsNWSDServerStatisticsFramesLoadInBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 8),
    _RsNWSDServerStatisticsFramesLoadInBytes_Type()
)
rsNWSDServerStatisticsFramesLoadInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsFramesLoadInBytes.setStatus("mandatory")
_RsNWSDServerStatisticsFramesRateInBytes_Type = Counter32
_RsNWSDServerStatisticsFramesRateInBytes_Object = MibTableColumn
rsNWSDServerStatisticsFramesRateInBytes = _RsNWSDServerStatisticsFramesRateInBytes_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 9),
    _RsNWSDServerStatisticsFramesRateInBytes_Type()
)
rsNWSDServerStatisticsFramesRateInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsFramesRateInBytes.setStatus("mandatory")
_RsNWSDServerStatisticsConnectivityCheckFailed_Type = Integer32
_RsNWSDServerStatisticsConnectivityCheckFailed_Object = MibTableColumn
rsNWSDServerStatisticsConnectivityCheckFailed = _RsNWSDServerStatisticsConnectivityCheckFailed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 10),
    _RsNWSDServerStatisticsConnectivityCheckFailed_Type()
)
rsNWSDServerStatisticsConnectivityCheckFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsConnectivityCheckFailed.setStatus("mandatory")
_RsNWSDServerStatisticsConnectionLimitReached_Type = Integer32
_RsNWSDServerStatisticsConnectionLimitReached_Object = MibTableColumn
rsNWSDServerStatisticsConnectionLimitReached = _RsNWSDServerStatisticsConnectionLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 11),
    _RsNWSDServerStatisticsConnectionLimitReached_Type()
)
rsNWSDServerStatisticsConnectionLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsConnectionLimitReached.setStatus("mandatory")
_RsNWSDServerStatisticsAnsweredDNSReqCounter_Type = Counter32
_RsNWSDServerStatisticsAnsweredDNSReqCounter_Object = MibTableColumn
rsNWSDServerStatisticsAnsweredDNSReqCounter = _RsNWSDServerStatisticsAnsweredDNSReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 12),
    _RsNWSDServerStatisticsAnsweredDNSReqCounter_Type()
)
rsNWSDServerStatisticsAnsweredDNSReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsAnsweredDNSReqCounter.setStatus("mandatory")
_RsNWSDServerStatisticsAnsweredDNSReqLastSecCounter_Type = Counter32
_RsNWSDServerStatisticsAnsweredDNSReqLastSecCounter_Object = MibTableColumn
rsNWSDServerStatisticsAnsweredDNSReqLastSecCounter = _RsNWSDServerStatisticsAnsweredDNSReqLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 13),
    _RsNWSDServerStatisticsAnsweredDNSReqLastSecCounter_Type()
)
rsNWSDServerStatisticsAnsweredDNSReqLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsAnsweredDNSReqLastSecCounter.setStatus("mandatory")


class _RsNWSDServerStatisticsRedirectedHTTPSessions_Type(OctetString):
    """Custom type rsNWSDServerStatisticsRedirectedHTTPSessions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDServerStatisticsRedirectedHTTPSessions_Type.__name__ = "OctetString"
_RsNWSDServerStatisticsRedirectedHTTPSessions_Object = MibTableColumn
rsNWSDServerStatisticsRedirectedHTTPSessions = _RsNWSDServerStatisticsRedirectedHTTPSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 14),
    _RsNWSDServerStatisticsRedirectedHTTPSessions_Type()
)
rsNWSDServerStatisticsRedirectedHTTPSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsRedirectedHTTPSessions.setStatus("mandatory")
_RsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter_Type = Counter32
_RsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter_Object = MibTableColumn
rsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter = _RsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 15),
    _RsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter_Type()
)
rsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter.setStatus("mandatory")


class _RsNWSDServerStatisticsRedirectedTriangSessions_Type(OctetString):
    """Custom type rsNWSDServerStatisticsRedirectedTriangSessions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RsNWSDServerStatisticsRedirectedTriangSessions_Type.__name__ = "OctetString"
_RsNWSDServerStatisticsRedirectedTriangSessions_Object = MibTableColumn
rsNWSDServerStatisticsRedirectedTriangSessions = _RsNWSDServerStatisticsRedirectedTriangSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 16),
    _RsNWSDServerStatisticsRedirectedTriangSessions_Type()
)
rsNWSDServerStatisticsRedirectedTriangSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsRedirectedTriangSessions.setStatus("mandatory")
_RsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount_Type = Counter32
_RsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount_Object = MibTableColumn
rsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount = _RsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 29, 8, 1, 17),
    _RsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount_Type()
)
rsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount.setStatus("mandatory")
_RsWSDCookieTable_Object = MibTable
rsWSDCookieTable = _RsWSDCookieTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30)
)
if mibBuilder.loadTexts:
    rsWSDCookieTable.setStatus("mandatory")
_RsWSDCookieTableEntry_Object = MibTableRow
rsWSDCookieTableEntry = _RsWSDCookieTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30, 1)
)
rsWSDCookieTableEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDCookieFarm"),
    (0, "WSD-MIB", "rsWSDCookieValue"),
)
if mibBuilder.loadTexts:
    rsWSDCookieTableEntry.setStatus("mandatory")
_RsWSDCookieFarm_Type = IpAddress
_RsWSDCookieFarm_Object = MibTableColumn
rsWSDCookieFarm = _RsWSDCookieFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30, 1, 1),
    _RsWSDCookieFarm_Type()
)
rsWSDCookieFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCookieFarm.setStatus("mandatory")


class _RsWSDCookieValue_Type(DisplayString):
    """Custom type rsWSDCookieValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RsWSDCookieValue_Type.__name__ = "DisplayString"
_RsWSDCookieValue_Object = MibTableColumn
rsWSDCookieValue = _RsWSDCookieValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30, 1, 2),
    _RsWSDCookieValue_Type()
)
rsWSDCookieValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCookieValue.setStatus("mandatory")
_RsWSDCookieServer_Type = IpAddress
_RsWSDCookieServer_Object = MibTableColumn
rsWSDCookieServer = _RsWSDCookieServer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30, 1, 3),
    _RsWSDCookieServer_Type()
)
rsWSDCookieServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCookieServer.setStatus("mandatory")
_RsWSDCookieStatus_Type = RowStatus
_RsWSDCookieStatus_Object = MibTableColumn
rsWSDCookieStatus = _RsWSDCookieStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 30, 1, 4),
    _RsWSDCookieStatus_Type()
)
rsWSDCookieStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCookieStatus.setStatus("mandatory")


class _RsWSDTrackUDPSessionsMode_Type(Integer32):
    """Custom type rsWSDTrackUDPSessionsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDTrackUDPSessionsMode_Type.__name__ = "Integer32"
_RsWSDTrackUDPSessionsMode_Object = MibScalar
rsWSDTrackUDPSessionsMode = _RsWSDTrackUDPSessionsMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 31),
    _RsWSDTrackUDPSessionsMode_Type()
)
rsWSDTrackUDPSessionsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTrackUDPSessionsMode.setStatus("mandatory")


class _RsWSDTrackSSLIDinSelectServerMode_Type(Integer32):
    """Custom type rsWSDTrackSSLIDinSelectServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDTrackSSLIDinSelectServerMode_Type.__name__ = "Integer32"
_RsWSDTrackSSLIDinSelectServerMode_Object = MibScalar
rsWSDTrackSSLIDinSelectServerMode = _RsWSDTrackSSLIDinSelectServerMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 32),
    _RsWSDTrackSSLIDinSelectServerMode_Type()
)
rsWSDTrackSSLIDinSelectServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTrackSSLIDinSelectServerMode.setStatus("mandatory")
_RsWSDTuning_ObjectIdentity = ObjectIdentity
rsWSDTuning = _RsWSDTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33)
)
_RsWSDMaxURLEntriesTuning_ObjectIdentity = ObjectIdentity
rsWSDMaxURLEntriesTuning = _RsWSDMaxURLEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 1)
)
_RsWSDMaxURLEntries_Type = Integer32
_RsWSDMaxURLEntries_Object = MibScalar
rsWSDMaxURLEntries = _RsWSDMaxURLEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 1, 1),
    _RsWSDMaxURLEntries_Type()
)
rsWSDMaxURLEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMaxURLEntries.setStatus("mandatory")
_RsWSDMaxURLEntriesAfterReset_Type = Integer32
_RsWSDMaxURLEntriesAfterReset_Object = MibScalar
rsWSDMaxURLEntriesAfterReset = _RsWSDMaxURLEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 1, 2),
    _RsWSDMaxURLEntriesAfterReset_Type()
)
rsWSDMaxURLEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMaxURLEntriesAfterReset.setStatus("mandatory")
_RsWSDMaxRequestEntriesTuning_ObjectIdentity = ObjectIdentity
rsWSDMaxRequestEntriesTuning = _RsWSDMaxRequestEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 2)
)
_RsWSDMaxRequestEntries_Type = Integer32
_RsWSDMaxRequestEntries_Object = MibScalar
rsWSDMaxRequestEntries = _RsWSDMaxRequestEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 2, 1),
    _RsWSDMaxRequestEntries_Type()
)
rsWSDMaxRequestEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMaxRequestEntries.setStatus("mandatory")
_RsWSDMaxRequestEntriesAfterReset_Type = Integer32
_RsWSDMaxRequestEntriesAfterReset_Object = MibScalar
rsWSDMaxRequestEntriesAfterReset = _RsWSDMaxRequestEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 2, 2),
    _RsWSDMaxRequestEntriesAfterReset_Type()
)
rsWSDMaxRequestEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMaxRequestEntriesAfterReset.setStatus("mandatory")
_RsWSDMaxSSLEntriesTuning_ObjectIdentity = ObjectIdentity
rsWSDMaxSSLEntriesTuning = _RsWSDMaxSSLEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 3)
)
_RsWSDMaxSSLEntries_Type = Integer32
_RsWSDMaxSSLEntries_Object = MibScalar
rsWSDMaxSSLEntries = _RsWSDMaxSSLEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 3, 1),
    _RsWSDMaxSSLEntries_Type()
)
rsWSDMaxSSLEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMaxSSLEntries.setStatus("mandatory")
_RsWSDMaxSSLEntriesAfterReset_Type = Integer32
_RsWSDMaxSSLEntriesAfterReset_Object = MibScalar
rsWSDMaxSSLEntriesAfterReset = _RsWSDMaxSSLEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 33, 3, 2),
    _RsWSDMaxSSLEntriesAfterReset_Type()
)
rsWSDMaxSSLEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMaxSSLEntriesAfterReset.setStatus("mandatory")
_RsWSDTweaks_ObjectIdentity = ObjectIdentity
rsWSDTweaks = _RsWSDTweaks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34)
)


class _RsWSDMaintainURLSFPersistency_Type(Integer32):
    """Custom type rsWSDMaintainURLSFPersistency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDMaintainURLSFPersistency_Type.__name__ = "Integer32"
_RsWSDMaintainURLSFPersistency_Object = MibScalar
rsWSDMaintainURLSFPersistency = _RsWSDMaintainURLSFPersistency_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 1),
    _RsWSDMaintainURLSFPersistency_Type()
)
rsWSDMaintainURLSFPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMaintainURLSFPersistency.setStatus("mandatory")


class _RsWSDAllowAnyAppPortForCookies_Type(Integer32):
    """Custom type rsWSDAllowAnyAppPortForCookies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDAllowAnyAppPortForCookies_Type.__name__ = "Integer32"
_RsWSDAllowAnyAppPortForCookies_Object = MibScalar
rsWSDAllowAnyAppPortForCookies = _RsWSDAllowAnyAppPortForCookies_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 2),
    _RsWSDAllowAnyAppPortForCookies_Type()
)
rsWSDAllowAnyAppPortForCookies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDAllowAnyAppPortForCookies.setStatus("mandatory")


class _RsWSDSrcPortInClientHash_Type(Integer32):
    """Custom type rsWSDSrcPortInClientHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDSrcPortInClientHash_Type.__name__ = "Integer32"
_RsWSDSrcPortInClientHash_Object = MibScalar
rsWSDSrcPortInClientHash = _RsWSDSrcPortInClientHash_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 3),
    _RsWSDSrcPortInClientHash_Type()
)
rsWSDSrcPortInClientHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSrcPortInClientHash.setStatus("mandatory")


class _RsWSDUserDefinedTimeoutAfterTCPFailure_Type(Integer32):
    """Custom type rsWSDUserDefinedTimeoutAfterTCPFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDUserDefinedTimeoutAfterTCPFailure_Type.__name__ = "Integer32"
_RsWSDUserDefinedTimeoutAfterTCPFailure_Object = MibScalar
rsWSDUserDefinedTimeoutAfterTCPFailure = _RsWSDUserDefinedTimeoutAfterTCPFailure_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 4),
    _RsWSDUserDefinedTimeoutAfterTCPFailure_Type()
)
rsWSDUserDefinedTimeoutAfterTCPFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUserDefinedTimeoutAfterTCPFailure.setStatus("mandatory")


class _RsWSDNoSlashAfterGET_Type(Integer32):
    """Custom type rsWSDNoSlashAfterGET based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDNoSlashAfterGET_Type.__name__ = "Integer32"
_RsWSDNoSlashAfterGET_Object = MibScalar
rsWSDNoSlashAfterGET = _RsWSDNoSlashAfterGET_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 5),
    _RsWSDNoSlashAfterGET_Type()
)
rsWSDNoSlashAfterGET.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNoSlashAfterGET.setStatus("mandatory")


class _RsWSDTimeoutForSYN_Type(Integer32):
    """Custom type rsWSDTimeoutForSYN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsWSDTimeoutForSYN_Type.__name__ = "Integer32"
_RsWSDTimeoutForSYN_Object = MibScalar
rsWSDTimeoutForSYN = _RsWSDTimeoutForSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 6),
    _RsWSDTimeoutForSYN_Type()
)
rsWSDTimeoutForSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTimeoutForSYN.setStatus("mandatory")
_RsWSDSpecificNATAddress_Type = IpAddress
_RsWSDSpecificNATAddress_Object = MibScalar
rsWSDSpecificNATAddress = _RsWSDSpecificNATAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 7),
    _RsWSDSpecificNATAddress_Type()
)
rsWSDSpecificNATAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSpecificNATAddress.setStatus("mandatory")


class _RsWSDExtendedCheckHostMode_Type(Integer32):
    """Custom type rsWSDExtendedCheckHostMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipMode", 1),
          ("nameMode", 2))
    )


_RsWSDExtendedCheckHostMode_Type.__name__ = "Integer32"
_RsWSDExtendedCheckHostMode_Object = MibScalar
rsWSDExtendedCheckHostMode = _RsWSDExtendedCheckHostMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 8),
    _RsWSDExtendedCheckHostMode_Type()
)
rsWSDExtendedCheckHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDExtendedCheckHostMode.setStatus("mandatory")


class _RsWSDExtendedLRPSecurity_Type(Integer32):
    """Custom type rsWSDExtendedLRPSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDExtendedLRPSecurity_Type.__name__ = "Integer32"
_RsWSDExtendedLRPSecurity_Object = MibScalar
rsWSDExtendedLRPSecurity = _RsWSDExtendedLRPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 9),
    _RsWSDExtendedLRPSecurity_Type()
)
rsWSDExtendedLRPSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDExtendedLRPSecurity.setStatus("mandatory")


class _RsWSDURLCookies_Type(Integer32):
    """Custom type rsWSDURLCookies based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDURLCookies_Type.__name__ = "Integer32"
_RsWSDURLCookies_Object = MibScalar
rsWSDURLCookies = _RsWSDURLCookies_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 10),
    _RsWSDURLCookies_Type()
)
rsWSDURLCookies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLCookies.setStatus("mandatory")


class _RsWSDURLTableLookupPrecedence_Type(Integer32):
    """Custom type rsWSDURLTableLookupPrecedence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileType", 2),
          ("url", 1))
    )


_RsWSDURLTableLookupPrecedence_Type.__name__ = "Integer32"
_RsWSDURLTableLookupPrecedence_Object = MibScalar
rsWSDURLTableLookupPrecedence = _RsWSDURLTableLookupPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 34, 11),
    _RsWSDURLTableLookupPrecedence_Type()
)
rsWSDURLTableLookupPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLTableLookupPrecedence.setStatus("mandatory")
_RsWSDExtendedFarmTable_Object = MibTable
rsWSDExtendedFarmTable = _RsWSDExtendedFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35)
)
if mibBuilder.loadTexts:
    rsWSDExtendedFarmTable.setStatus("mandatory")
_RsWSDExtendedFarmEntry_Object = MibTableRow
rsWSDExtendedFarmEntry = _RsWSDExtendedFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1)
)
rsWSDExtendedFarmEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDExtendedFarmAddress"),
)
if mibBuilder.loadTexts:
    rsWSDExtendedFarmEntry.setStatus("mandatory")
_RsWSDExtendedFarmAddress_Type = IpAddress
_RsWSDExtendedFarmAddress_Object = MibTableColumn
rsWSDExtendedFarmAddress = _RsWSDExtendedFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 1),
    _RsWSDExtendedFarmAddress_Type()
)
rsWSDExtendedFarmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDExtendedFarmAddress.setStatus("mandatory")


class _RsWSDExtendedFarmHttpsType_Type(Integer32):
    """Custom type rsWSDExtendedFarmHttpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("httpsonly", 2),
          ("regular", 1))
    )


_RsWSDExtendedFarmHttpsType_Type.__name__ = "Integer32"
_RsWSDExtendedFarmHttpsType_Object = MibTableColumn
rsWSDExtendedFarmHttpsType = _RsWSDExtendedFarmHttpsType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 2),
    _RsWSDExtendedFarmHttpsType_Type()
)
rsWSDExtendedFarmHttpsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDExtendedFarmHttpsType.setStatus("mandatory")


class _RsWSDConnCheckSecret_Type(DisplayString):
    """Custom type rsWSDConnCheckSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsWSDConnCheckSecret_Type.__name__ = "DisplayString"
_RsWSDConnCheckSecret_Object = MibTableColumn
rsWSDConnCheckSecret = _RsWSDConnCheckSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 3),
    _RsWSDConnCheckSecret_Type()
)
rsWSDConnCheckSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDConnCheckSecret.setStatus("mandatory")


class _RsWSDOverLoadStatus_Type(Integer32):
    """Custom type rsWSDOverLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDOverLoadStatus_Type.__name__ = "Integer32"
_RsWSDOverLoadStatus_Object = MibTableColumn
rsWSDOverLoadStatus = _RsWSDOverLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 4),
    _RsWSDOverLoadStatus_Type()
)
rsWSDOverLoadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDOverLoadStatus.setStatus("mandatory")


class _RsWSDFarmURLCookies_Type(Integer32):
    """Custom type rsWSDFarmURLCookies based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDFarmURLCookies_Type.__name__ = "Integer32"
_RsWSDFarmURLCookies_Object = MibTableColumn
rsWSDFarmURLCookies = _RsWSDFarmURLCookies_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 5),
    _RsWSDFarmURLCookies_Type()
)
rsWSDFarmURLCookies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmURLCookies.setStatus("mandatory")
_RsWSDExtendedFarmNATRangeIPFrom_Type = IpAddress
_RsWSDExtendedFarmNATRangeIPFrom_Object = MibTableColumn
rsWSDExtendedFarmNATRangeIPFrom = _RsWSDExtendedFarmNATRangeIPFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 35, 1, 6),
    _RsWSDExtendedFarmNATRangeIPFrom_Type()
)
rsWSDExtendedFarmNATRangeIPFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDExtendedFarmNATRangeIPFrom.setStatus("mandatory")
_RsWSDNHRTable_Object = MibTable
rsWSDNHRTable = _RsWSDNHRTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36)
)
if mibBuilder.loadTexts:
    rsWSDNHRTable.setStatus("mandatory")
_RsWSDNHREntry_Object = MibTableRow
rsWSDNHREntry = _RsWSDNHREntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1)
)
rsWSDNHREntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDNHRNHRIP"),
)
if mibBuilder.loadTexts:
    rsWSDNHREntry.setStatus("mandatory")
_RsWSDNHRNHRIP_Type = IpAddress
_RsWSDNHRNHRIP_Object = MibTableColumn
rsWSDNHRNHRIP = _RsWSDNHRNHRIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 1),
    _RsWSDNHRNHRIP_Type()
)
rsWSDNHRNHRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNHRNHRIP.setStatus("mandatory")
_RsWSDNHRDestinationMAC_Type = PhysAddress
_RsWSDNHRDestinationMAC_Object = MibTableColumn
rsWSDNHRDestinationMAC = _RsWSDNHRDestinationMAC_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 2),
    _RsWSDNHRDestinationMAC_Type()
)
rsWSDNHRDestinationMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNHRDestinationMAC.setStatus("mandatory")
_RsWSDNHRSourceMAC_Type = PhysAddress
_RsWSDNHRSourceMAC_Object = MibTableColumn
rsWSDNHRSourceMAC = _RsWSDNHRSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 3),
    _RsWSDNHRSourceMAC_Type()
)
rsWSDNHRSourceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNHRSourceMAC.setStatus("mandatory")
_RsWSDNHRPhysicalPortNumber_Type = Integer32
_RsWSDNHRPhysicalPortNumber_Object = MibTableColumn
rsWSDNHRPhysicalPortNumber = _RsWSDNHRPhysicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 4),
    _RsWSDNHRPhysicalPortNumber_Type()
)
rsWSDNHRPhysicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNHRPhysicalPortNumber.setStatus("mandatory")


class _RsWSDNHRAdminStatus_Type(Integer32):
    """Custom type rsWSDNHRAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDNHRAdminStatus_Type.__name__ = "Integer32"
_RsWSDNHRAdminStatus_Object = MibTableColumn
rsWSDNHRAdminStatus = _RsWSDNHRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 5),
    _RsWSDNHRAdminStatus_Type()
)
rsWSDNHRAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRAdminStatus.setStatus("mandatory")


class _RsWSDNHROperStatus_Type(Integer32):
    """Custom type rsWSDNHROperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_RsWSDNHROperStatus_Type.__name__ = "Integer32"
_RsWSDNHROperStatus_Object = MibTableColumn
rsWSDNHROperStatus = _RsWSDNHROperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 6),
    _RsWSDNHROperStatus_Type()
)
rsWSDNHROperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNHROperStatus.setStatus("mandatory")
_RsWSDNHRPathHealthCheckIP_Type = IpAddress
_RsWSDNHRPathHealthCheckIP_Object = MibTableColumn
rsWSDNHRPathHealthCheckIP = _RsWSDNHRPathHealthCheckIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 7),
    _RsWSDNHRPathHealthCheckIP_Type()
)
rsWSDNHRPathHealthCheckIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRPathHealthCheckIP.setStatus("mandatory")


class _RsWSDNHRCheckMethod_Type(Integer32):
    """Custom type rsWSDNHRCheckMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("ping", 1))
    )


_RsWSDNHRCheckMethod_Type.__name__ = "Integer32"
_RsWSDNHRCheckMethod_Object = MibTableColumn
rsWSDNHRCheckMethod = _RsWSDNHRCheckMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 8),
    _RsWSDNHRCheckMethod_Type()
)
rsWSDNHRCheckMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRCheckMethod.setStatus("mandatory")


class _RsWSDNHRCheckInterval_Type(Integer32):
    """Custom type rsWSDNHRCheckInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsWSDNHRCheckInterval_Type.__name__ = "Integer32"
_RsWSDNHRCheckInterval_Object = MibTableColumn
rsWSDNHRCheckInterval = _RsWSDNHRCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 9),
    _RsWSDNHRCheckInterval_Type()
)
rsWSDNHRCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRCheckInterval.setStatus("mandatory")


class _RsWSDNRHCheckRetries_Type(Integer32):
    """Custom type rsWSDNRHCheckRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsWSDNRHCheckRetries_Type.__name__ = "Integer32"
_RsWSDNRHCheckRetries_Object = MibTableColumn
rsWSDNRHCheckRetries = _RsWSDNRHCheckRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 10),
    _RsWSDNRHCheckRetries_Type()
)
rsWSDNRHCheckRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNRHCheckRetries.setStatus("mandatory")
_RsWSDNHRRowStatus_Type = RowStatus
_RsWSDNHRRowStatus_Object = MibTableColumn
rsWSDNHRRowStatus = _RsWSDNHRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 11),
    _RsWSDNHRRowStatus_Type()
)
rsWSDNHRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRRowStatus.setStatus("mandatory")
_RsWSDNHRTag_Type = Integer32
_RsWSDNHRTag_Object = MibTableColumn
rsWSDNHRTag = _RsWSDNHRTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 36, 1, 12),
    _RsWSDNHRTag_Type()
)
rsWSDNHRTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNHRTag.setStatus("mandatory")
_RsWSDVIPNHRTable_Object = MibTable
rsWSDVIPNHRTable = _RsWSDVIPNHRTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37)
)
if mibBuilder.loadTexts:
    rsWSDVIPNHRTable.setStatus("mandatory")
_RsWSDVIPNHREntry_Object = MibTableRow
rsWSDVIPNHREntry = _RsWSDVIPNHREntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1)
)
rsWSDVIPNHREntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDVIPNHRVIP"),
)
if mibBuilder.loadTexts:
    rsWSDVIPNHREntry.setStatus("mandatory")
_RsWSDVIPNHRVIP_Type = IpAddress
_RsWSDVIPNHRVIP_Object = MibTableColumn
rsWSDVIPNHRVIP = _RsWSDVIPNHRVIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 1),
    _RsWSDVIPNHRVIP_Type()
)
rsWSDVIPNHRVIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDVIPNHRVIP.setStatus("mandatory")
_RsWSDVIPNHRNHRIP_Type = IpAddress
_RsWSDVIPNHRNHRIP_Object = MibTableColumn
rsWSDVIPNHRNHRIP = _RsWSDVIPNHRNHRIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 2),
    _RsWSDVIPNHRNHRIP_Type()
)
rsWSDVIPNHRNHRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRNHRIP.setStatus("mandatory")
_RsWSDVIPNHRBackupNHRIP_Type = IpAddress
_RsWSDVIPNHRBackupNHRIP_Object = MibTableColumn
rsWSDVIPNHRBackupNHRIP = _RsWSDVIPNHRBackupNHRIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 3),
    _RsWSDVIPNHRBackupNHRIP_Type()
)
rsWSDVIPNHRBackupNHRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRBackupNHRIP.setStatus("mandatory")


class _RsWSDVIPNHRNoRouteAction_Type(Integer32):
    """Custom type rsWSDVIPNHRNoRouteAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("useFFT", 2))
    )


_RsWSDVIPNHRNoRouteAction_Type.__name__ = "Integer32"
_RsWSDVIPNHRNoRouteAction_Object = MibTableColumn
rsWSDVIPNHRNoRouteAction = _RsWSDVIPNHRNoRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 4),
    _RsWSDVIPNHRNoRouteAction_Type()
)
rsWSDVIPNHRNoRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRNoRouteAction.setStatus("mandatory")
_RsWSDVIPNHRRowStatus_Type = RowStatus
_RsWSDVIPNHRRowStatus_Object = MibTableColumn
rsWSDVIPNHRRowStatus = _RsWSDVIPNHRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 5),
    _RsWSDVIPNHRRowStatus_Type()
)
rsWSDVIPNHRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRRowStatus.setStatus("mandatory")


class _RsWSDVIPNHRNHRWeight_Type(Integer32):
    """Custom type rsWSDVIPNHRNHRWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDVIPNHRNHRWeight_Type.__name__ = "Integer32"
_RsWSDVIPNHRNHRWeight_Object = MibTableColumn
rsWSDVIPNHRNHRWeight = _RsWSDVIPNHRNHRWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 6),
    _RsWSDVIPNHRNHRWeight_Type()
)
rsWSDVIPNHRNHRWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRNHRWeight.setStatus("mandatory")


class _RsWSDVIPNHRBackupWeight_Type(Integer32):
    """Custom type rsWSDVIPNHRBackupWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDVIPNHRBackupWeight_Type.__name__ = "Integer32"
_RsWSDVIPNHRBackupWeight_Object = MibTableColumn
rsWSDVIPNHRBackupWeight = _RsWSDVIPNHRBackupWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 7),
    _RsWSDVIPNHRBackupWeight_Type()
)
rsWSDVIPNHRBackupWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRBackupWeight.setStatus("mandatory")


class _RsWSDVIPNHRAdminLoadSharing_Type(Integer32):
    """Custom type rsWSDVIPNHRAdminLoadSharing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDVIPNHRAdminLoadSharing_Type.__name__ = "Integer32"
_RsWSDVIPNHRAdminLoadSharing_Object = MibTableColumn
rsWSDVIPNHRAdminLoadSharing = _RsWSDVIPNHRAdminLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 37, 1, 8),
    _RsWSDVIPNHRAdminLoadSharing_Type()
)
rsWSDVIPNHRAdminLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVIPNHRAdminLoadSharing.setStatus("mandatory")
_RsWSDTokenTable_Object = MibTable
rsWSDTokenTable = _RsWSDTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38)
)
if mibBuilder.loadTexts:
    rsWSDTokenTable.setStatus("mandatory")
_RsWSDTokenTableEntry_Object = MibTableRow
rsWSDTokenTableEntry = _RsWSDTokenTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1)
)
rsWSDTokenTableEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDToken"),
)
if mibBuilder.loadTexts:
    rsWSDTokenTableEntry.setStatus("mandatory")


class _RsWSDToken_Type(DisplayString):
    """Custom type rsWSDToken based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RsWSDToken_Type.__name__ = "DisplayString"
_RsWSDToken_Object = MibTableColumn
rsWSDToken = _RsWSDToken_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1, 1),
    _RsWSDToken_Type()
)
rsWSDToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDToken.setStatus("mandatory")
_RsWSDTokenFarmMap_Type = IpAddress
_RsWSDTokenFarmMap_Object = MibTableColumn
rsWSDTokenFarmMap = _RsWSDTokenFarmMap_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1, 2),
    _RsWSDTokenFarmMap_Type()
)
rsWSDTokenFarmMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTokenFarmMap.setStatus("mandatory")
_RsWSDTokenFarm_Type = IpAddress
_RsWSDTokenFarm_Object = MibTableColumn
rsWSDTokenFarm = _RsWSDTokenFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1, 3),
    _RsWSDTokenFarm_Type()
)
rsWSDTokenFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTokenFarm.setStatus("mandatory")


class _RsWSDTokenDefault_Type(Integer32):
    """Custom type rsWSDTokenDefault based on Integer32"""
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
        *(("alwaysDefault", 4),
          ("noHeaderField", 3),
          ("noToken", 2),
          ("notDefault", 1))
    )


_RsWSDTokenDefault_Type.__name__ = "Integer32"
_RsWSDTokenDefault_Object = MibTableColumn
rsWSDTokenDefault = _RsWSDTokenDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1, 4),
    _RsWSDTokenDefault_Type()
)
rsWSDTokenDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTokenDefault.setStatus("mandatory")
_RsWSDTokenStatus_Type = RowStatus
_RsWSDTokenStatus_Object = MibTableColumn
rsWSDTokenStatus = _RsWSDTokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 38, 1, 5),
    _RsWSDTokenStatus_Type()
)
rsWSDTokenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTokenStatus.setStatus("mandatory")
_RsWSDVirtualDNSTable_Object = MibTable
rsWSDVirtualDNSTable = _RsWSDVirtualDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 39)
)
if mibBuilder.loadTexts:
    rsWSDVirtualDNSTable.setStatus("mandatory")
_RsWSDVirtualDNSTableEntry_Object = MibTableRow
rsWSDVirtualDNSTableEntry = _RsWSDVirtualDNSTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 39, 1)
)
rsWSDVirtualDNSTableEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDVirtualDNSAddress"),
)
if mibBuilder.loadTexts:
    rsWSDVirtualDNSTableEntry.setStatus("mandatory")
_RsWSDVirtualDNSAddress_Type = IpAddress
_RsWSDVirtualDNSAddress_Object = MibTableColumn
rsWSDVirtualDNSAddress = _RsWSDVirtualDNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 39, 1, 1),
    _RsWSDVirtualDNSAddress_Type()
)
rsWSDVirtualDNSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDVirtualDNSAddress.setStatus("mandatory")


class _RsWSDVirtualDNSRedunType_Type(Integer32):
    """Custom type rsWSDVirtualDNSRedunType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_RsWSDVirtualDNSRedunType_Type.__name__ = "Integer32"
_RsWSDVirtualDNSRedunType_Object = MibTableColumn
rsWSDVirtualDNSRedunType = _RsWSDVirtualDNSRedunType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 39, 1, 2),
    _RsWSDVirtualDNSRedunType_Type()
)
rsWSDVirtualDNSRedunType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVirtualDNSRedunType.setStatus("mandatory")
_RsWSDVirtualDNSStatus_Type = RowStatus
_RsWSDVirtualDNSStatus_Object = MibTableColumn
rsWSDVirtualDNSStatus = _RsWSDVirtualDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 39, 1, 3),
    _RsWSDVirtualDNSStatus_Type()
)
rsWSDVirtualDNSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVirtualDNSStatus.setStatus("mandatory")
_RsWSDClientNAT_ObjectIdentity = ObjectIdentity
rsWSDClientNAT = _RsWSDClientNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40)
)
_RsWSDClientNATRangeTable_Object = MibTable
rsWSDClientNATRangeTable = _RsWSDClientNATRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 1)
)
if mibBuilder.loadTexts:
    rsWSDClientNATRangeTable.setStatus("mandatory")
_RsWSDClientNATRangeIPEntry_Object = MibTableRow
rsWSDClientNATRangeIPEntry = _RsWSDClientNATRangeIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 1, 1)
)
rsWSDClientNATRangeIPEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDClientNATRangeIPFrom"),
)
if mibBuilder.loadTexts:
    rsWSDClientNATRangeIPEntry.setStatus("mandatory")
_RsWSDClientNATRangeIPFrom_Type = IpAddress
_RsWSDClientNATRangeIPFrom_Object = MibTableColumn
rsWSDClientNATRangeIPFrom = _RsWSDClientNATRangeIPFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 1, 1, 1),
    _RsWSDClientNATRangeIPFrom_Type()
)
rsWSDClientNATRangeIPFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDClientNATRangeIPFrom.setStatus("mandatory")
_RsWSDClientNATRangeIPTo_Type = IpAddress
_RsWSDClientNATRangeIPTo_Object = MibTableColumn
rsWSDClientNATRangeIPTo = _RsWSDClientNATRangeIPTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 1, 1, 2),
    _RsWSDClientNATRangeIPTo_Type()
)
rsWSDClientNATRangeIPTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientNATRangeIPTo.setStatus("mandatory")
_RsWSDClientNATRangeIPStatus_Type = RowStatus
_RsWSDClientNATRangeIPStatus_Object = MibTableColumn
rsWSDClientNATRangeIPStatus = _RsWSDClientNATRangeIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 1, 1, 3),
    _RsWSDClientNATRangeIPStatus_Type()
)
rsWSDClientNATRangeIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientNATRangeIPStatus.setStatus("mandatory")
_RsWSDNATRangeTable_Object = MibTable
rsWSDNATRangeTable = _RsWSDNATRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 2)
)
if mibBuilder.loadTexts:
    rsWSDNATRangeTable.setStatus("mandatory")
_RsWSDNATRangeIPEntry_Object = MibTableRow
rsWSDNATRangeIPEntry = _RsWSDNATRangeIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 2, 1)
)
rsWSDNATRangeIPEntry.setIndexNames(
    (0, "WSD-MIB", "rsWSDNATRangeIPFrom"),
)
if mibBuilder.loadTexts:
    rsWSDNATRangeIPEntry.setStatus("mandatory")
_RsWSDNATRangeIPFrom_Type = IpAddress
_RsWSDNATRangeIPFrom_Object = MibTableColumn
rsWSDNATRangeIPFrom = _RsWSDNATRangeIPFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 2, 1, 1),
    _RsWSDNATRangeIPFrom_Type()
)
rsWSDNATRangeIPFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNATRangeIPFrom.setStatus("mandatory")
_RsWSDNATRangeIPTo_Type = IpAddress
_RsWSDNATRangeIPTo_Object = MibTableColumn
rsWSDNATRangeIPTo = _RsWSDNATRangeIPTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 2, 1, 2),
    _RsWSDNATRangeIPTo_Type()
)
rsWSDNATRangeIPTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNATRangeIPTo.setStatus("mandatory")
_RsWSDNATRangeStatus_Type = RowStatus
_RsWSDNATRangeStatus_Object = MibTableColumn
rsWSDNATRangeStatus = _RsWSDNATRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 2, 1, 3),
    _RsWSDNATRangeStatus_Type()
)
rsWSDNATRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNATRangeStatus.setStatus("mandatory")


class _RsWSDClientNATStatus_Type(Integer32):
    """Custom type rsWSDClientNATStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDClientNATStatus_Type.__name__ = "Integer32"
_RsWSDClientNATStatus_Object = MibScalar
rsWSDClientNATStatus = _RsWSDClientNATStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 40, 3),
    _RsWSDClientNATStatus_Type()
)
rsWSDClientNATStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientNATStatus.setStatus("mandatory")


class _RsWSDSessionChaining_Type(Integer32):
    """Custom type rsWSDSessionChaining based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsWSDSessionChaining_Type.__name__ = "Integer32"
_RsWSDSessionChaining_Object = MibScalar
rsWSDSessionChaining = _RsWSDSessionChaining_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 41),
    _RsWSDSessionChaining_Type()
)
rsWSDSessionChaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSessionChaining.setStatus("mandatory")


class _RsWSDClientTableSizeThresh_Type(Integer32):
    """Custom type rsWSDClientTableSizeThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDClientTableSizeThresh_Type.__name__ = "Integer32"
_RsWSDClientTableSizeThresh_Object = MibScalar
rsWSDClientTableSizeThresh = _RsWSDClientTableSizeThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 3),
    _RsWSDClientTableSizeThresh_Type()
)
rsWSDClientTableSizeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientTableSizeThresh.setStatus("mandatory")


class _RsWSDLogicServConnectLimitThresh_Type(Integer32):
    """Custom type rsWSDLogicServConnectLimitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDLogicServConnectLimitThresh_Type.__name__ = "Integer32"
_RsWSDLogicServConnectLimitThresh_Object = MibScalar
rsWSDLogicServConnectLimitThresh = _RsWSDLogicServConnectLimitThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 4),
    _RsWSDLogicServConnectLimitThresh_Type()
)
rsWSDLogicServConnectLimitThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDLogicServConnectLimitThresh.setStatus("mandatory")


class _RsWSDPhysServConnectLimitThresh_Type(Integer32):
    """Custom type rsWSDPhysServConnectLimitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDPhysServConnectLimitThresh_Type.__name__ = "Integer32"
_RsWSDPhysServConnectLimitThresh_Object = MibScalar
rsWSDPhysServConnectLimitThresh = _RsWSDPhysServConnectLimitThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 5),
    _RsWSDPhysServConnectLimitThresh_Type()
)
rsWSDPhysServConnectLimitThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPhysServConnectLimitThresh.setStatus("mandatory")


class _RsWSDFarmCapacityLimitThresh_Type(Integer32):
    """Custom type rsWSDFarmCapacityLimitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDFarmCapacityLimitThresh_Type.__name__ = "Integer32"
_RsWSDFarmCapacityLimitThresh_Object = MibScalar
rsWSDFarmCapacityLimitThresh = _RsWSDFarmCapacityLimitThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 6),
    _RsWSDFarmCapacityLimitThresh_Type()
)
rsWSDFarmCapacityLimitThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmCapacityLimitThresh.setStatus("mandatory")


class _RsWSDServBandwidthLimitThresh_Type(Integer32):
    """Custom type rsWSDServBandwidthLimitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDServBandwidthLimitThresh_Type.__name__ = "Integer32"
_RsWSDServBandwidthLimitThresh_Object = MibScalar
rsWSDServBandwidthLimitThresh = _RsWSDServBandwidthLimitThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 7),
    _RsWSDServBandwidthLimitThresh_Type()
)
rsWSDServBandwidthLimitThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDServBandwidthLimitThresh.setStatus("mandatory")


class _RsWSDFarmBandwidthLimitThresh_Type(Integer32):
    """Custom type rsWSDFarmBandwidthLimitThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDFarmBandwidthLimitThresh_Type.__name__ = "Integer32"
_RsWSDFarmBandwidthLimitThresh_Object = MibScalar
rsWSDFarmBandwidthLimitThresh = _RsWSDFarmBandwidthLimitThresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 8),
    _RsWSDFarmBandwidthLimitThresh_Type()
)
rsWSDFarmBandwidthLimitThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDFarmBandwidthLimitThresh.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsWSDTWTClientTableSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 1)
)
rsWSDTWTClientTableSize.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTClientTableSize.setStatus(
        ""
    )

rsWSDTWTLogicServConnectLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 2)
)
rsWSDTWTLogicServConnectLimit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTLogicServConnectLimit.setStatus(
        ""
    )

rsWSDTWTPhyServConnectLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 3)
)
rsWSDTWTPhyServConnectLimit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTPhyServConnectLimit.setStatus(
        ""
    )

rsWSDTWTFarmCapacityLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 4)
)
rsWSDTWTFarmCapacityLimit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTFarmCapacityLimit.setStatus(
        ""
    )

rsWSDTWTServBandwidthLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 5)
)
rsWSDTWTServBandwidthLimit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTServBandwidthLimit.setStatus(
        ""
    )

rsWSDTWTFarmBandwidthLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 0, 6)
)
rsWSDTWTFarmBandwidthLimit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDTWTFarmBandwidthLimit.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WSD-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsWSDApplicationServersTable": rsWSDApplicationServersTable,
       "rsWSDApplicationServerEntry": rsWSDApplicationServerEntry,
       "rsWSDAddr": rsWSDAddr,
       "rsWSDServerAddr": rsWSDServerAddr,
       "rsWSDServerName": rsWSDServerName,
       "rsWSDServerOperStatus": rsWSDServerOperStatus,
       "rsWSDServerWeight": rsWSDServerWeight,
       "rsWSDServerAttachedUsersNumber": rsWSDServerAttachedUsersNumber,
       "rsWSDServerPeakLoad": rsWSDServerPeakLoad,
       "rsWSDServerFramesRate": rsWSDServerFramesRate,
       "rsWSDServerFramesLoad": rsWSDServerFramesLoad,
       "rsWSDServerStatus": rsWSDServerStatus,
       "rsWSDServerOperMode": rsWSDServerOperMode,
       "rsWSDMultiplexedServerPort": rsWSDMultiplexedServerPort,
       "rsWSDServerType": rsWSDServerType,
       "rsWSDServerConnectionLimit": rsWSDServerConnectionLimit,
       "rsWSDServerAdminStatus": rsWSDServerAdminStatus,
       "rsWSDServerBandWidth": rsWSDServerBandWidth,
       "rsWSDServerCckID": rsWSDServerCckID,
       "rsWSDServerRedirectTo": rsWSDServerRedirectTo,
       "rsWSDServerClientNATStatus": rsWSDServerClientNATStatus,
       "rsWSDdummy1": rsWSDdummy1,
       "rsWSDFarmTable": rsWSDFarmTable,
       "rsWSDFarmEntry": rsWSDFarmEntry,
       "rsWSDFarmAddress": rsWSDFarmAddress,
       "rsWSDFarmName": rsWSDFarmName,
       "rsWSDAdminStatus": rsWSDAdminStatus,
       "rsWSDClientsLifeTime": rsWSDClientsLifeTime,
       "rsWSDDispatchMethod": rsWSDDispatchMethod,
       "rsWSDCheckConnectivityStatus": rsWSDCheckConnectivityStatus,
       "rsWSDCheckConnectivityMethod": rsWSDCheckConnectivityMethod,
       "rsWSDCheckConnectivityInterval": rsWSDCheckConnectivityInterval,
       "rsWSDCheckConnectivityRetries": rsWSDCheckConnectivityRetries,
       "rsWSDClientsConnectDenials": rsWSDClientsConnectDenials,
       "rsWSDFarmStatus": rsWSDFarmStatus,
       "rsWSDMultiplexedFarmPort": rsWSDMultiplexedFarmPort,
       "rsWSDFarmDistThreshold": rsWSDFarmDistThreshold,
       "rsWSDFarmTrafficThreshold": rsWSDFarmTrafficThreshold,
       "rsWSDFarmRedirectionMode": rsWSDFarmRedirectionMode,
       "rsNsdFarmRegister": rsNsdFarmRegister,
       "rsWSDFarmMode": rsWSDFarmMode,
       "rsWSDExtendedConnectivityCheckInterval": rsWSDExtendedConnectivityCheckInterval,
       "rsWSDConnectivityCheckUrl": rsWSDConnectivityCheckUrl,
       "rsWSDFarmClientMode": rsWSDFarmClientMode,
       "rsWSDDNSRedir2ndMode": rsWSDDNSRedir2ndMode,
       "rsWSDFarmHttpRedirectionMode": rsWSDFarmHttpRedirectionMode,
       "rsWSDFarmOperStatus": rsWSDFarmOperStatus,
       "rsWSDFarmBandWidth": rsWSDFarmBandWidth,
       "rsWSDFarmCookieKey": rsWSDFarmCookieKey,
       "rsWSDConnCheckUserName": rsWSDConnCheckUserName,
       "rsWSDConnCheckPassword": rsWSDConnCheckPassword,
       "rsWSDdummy3": rsWSDdummy3,
       "rsWSDClientsTable": rsWSDClientsTable,
       "rsWSDClientEntry": rsWSDClientEntry,
       "rsWSDFarmAddr": rsWSDFarmAddr,
       "rsWSDClientAddr": rsWSDClientAddr,
       "rsWSDAttachedServerAddr": rsWSDAttachedServerAddr,
       "rsWSDClientLastActivityTime": rsWSDClientLastActivityTime,
       "rsWSDClientAttachmentTime": rsWSDClientAttachmentTime,
       "rsWSDClientType": rsWSDClientType,
       "rsWSDClientStatus": rsWSDClientStatus,
       "rsWSDdummy4": rsWSDdummy4,
       "rsWSDLoadReportTable": rsWSDLoadReportTable,
       "rsWSDLoadReportEntry": rsWSDLoadReportEntry,
       "rsWSDReportFarmAddress": rsWSDReportFarmAddress,
       "rsWSDReportDstFarmAddress": rsWSDReportDstFarmAddress,
       "rsWSDReportLclSuperFarmAddr": rsWSDReportLclSuperFarmAddr,
       "rsWSDReportDstIpAddress": rsWSDReportDstIpAddress,
       "rsWSDReportMapFarmAddress": rsWSDReportMapFarmAddress,
       "rsWSDReportStatus": rsWSDReportStatus,
       "rsWSDReportRdnDstIpAddr": rsWSDReportRdnDstIpAddr,
       "rsWSDReportDstSuperFarmAddr": rsWSDReportDstSuperFarmAddr,
       "rsWSDdummy6": rsWSDdummy6,
       "rsWSDFarmMappingTable": rsWSDFarmMappingTable,
       "rsWSDFarmMappingEntry": rsWSDFarmMappingEntry,
       "rsWSDMappingAddress": rsWSDMappingAddress,
       "rsWSDMappingFarmAddress": rsWSDMappingFarmAddress,
       "rsWSDOriginalAddress": rsWSDOriginalAddress,
       "rsWSDMappingAdminStatus": rsWSDMappingAdminStatus,
       "rsWSDMappingStatus": rsWSDMappingStatus,
       "rsWSDdummy7": rsWSDdummy7,
       "rsWSDLoadReportInterval": rsWSDLoadReportInterval,
       "rsWSDLoadReportTimeout": rsWSDLoadReportTimeout,
       "rsWSDPortFarmTable": rsWSDPortFarmTable,
       "rsWSDPortFarmEntry": rsWSDPortFarmEntry,
       "rsWSDPortMainAddress": rsWSDPortMainAddress,
       "rsWSDPortNumber": rsWSDPortNumber,
       "rsWSDPortFarmAddress": rsWSDPortFarmAddress,
       "rsWSDPortFarmStatus": rsWSDPortFarmStatus,
       "rsWSDPortFarmHeader": rsWSDPortFarmHeader,
       "rsWSDdummy10": rsWSDdummy10,
       "rsWSDProximity": rsWSDProximity,
       "rsWSDStaticProximityTable": rsWSDStaticProximityTable,
       "rsWSDStaticProximityEntry": rsWSDStaticProximityEntry,
       "rsWSDStaticProximityFarmAddress": rsWSDStaticProximityFarmAddress,
       "rsWSDStaticProximityRangeFrom": rsWSDStaticProximityRangeFrom,
       "rsWSDStaticProximityRangeTo": rsWSDStaticProximityRangeTo,
       "rsWSDStaticProximityStatus": rsWSDStaticProximityStatus,
       "rsWSDStaticProximityServer1": rsWSDStaticProximityServer1,
       "rsWSDStaticProximityServer2": rsWSDStaticProximityServer2,
       "rsWSDStaticProximityServer3": rsWSDStaticProximityServer3,
       "rsWSDProximityOperationMode": rsWSDProximityOperationMode,
       "rsWSDProximityMainDNS": rsWSDProximityMainDNS,
       "rsWSDProximityBackupDNS": rsWSDProximityBackupDNS,
       "rsWSDProximityAgingPeriod": rsWSDProximityAgingPeriod,
       "rsWSDProximityClientMode": rsWSDProximityClientMode,
       "rsWSDProximityRetries": rsWSDProximityRetries,
       "rsWSDProximityTimeout": rsWSDProximityTimeout,
       "rsWSDProximityTuning": rsWSDProximityTuning,
       "rsWSDMaxDynEntries": rsWSDMaxDynEntries,
       "rsWSDMaxDynEntriesAfterReset": rsWSDMaxDynEntriesAfterReset,
       "rsWSDPrxBasicCheckMethod": rsWSDPrxBasicCheckMethod,
       "rsWSDPrxAdvancedCheckMethod": rsWSDPrxAdvancedCheckMethod,
       "rsWSDPrxApplIndpndCheckMethod": rsWSDPrxApplIndpndCheckMethod,
       "rsWSDPrxApplAwareCheckMethod": rsWSDPrxApplAwareCheckMethod,
       "rsWSDTWTClientTableSize": rsWSDTWTClientTableSize,
       "rsWSDTWTLogicServConnectLimit": rsWSDTWTLogicServConnectLimit,
       "rsWSDTWTPhyServConnectLimit": rsWSDTWTPhyServConnectLimit,
       "rsWSDTWTFarmCapacityLimit": rsWSDTWTFarmCapacityLimit,
       "rsWSDTWTServBandwidthLimit": rsWSDTWTServBandwidthLimit,
       "rsWSDTWTFarmBandwidthLimit": rsWSDTWTFarmBandwidthLimit,
       "rsNWSDProximity": rsNWSDProximity,
       "rsWSDProximityHopsWeight": rsWSDProximityHopsWeight,
       "rsWSDProximityLatencyWeight": rsWSDProximityLatencyWeight,
       "rsWSDProximityLoadWeight": rsWSDProximityLoadWeight,
       "rsWSDProximityMirrorPercentage": rsWSDProximityMirrorPercentage,
       "rsWSDProximityMirrorPollingTime": rsWSDProximityMirrorPollingTime,
       "rsWSDDNSttl": rsWSDDNSttl,
       "rsWSDURLSuperFarmTable": rsWSDURLSuperFarmTable,
       "rsWSDURLSuperFarmEntry": rsWSDURLSuperFarmEntry,
       "rsWSDURLFarmAddress": rsWSDURLFarmAddress,
       "rsWSDURL": rsWSDURL,
       "rsWSDURLStatus": rsWSDURLStatus,
       "rsWSDMainVirtualDNS": rsWSDMainVirtualDNS,
       "rsWSDBackupVirtualDNS": rsWSDBackupVirtualDNS,
       "rsWSDProximityMirrorProtocolMode": rsWSDProximityMirrorProtocolMode,
       "rsWSDTwoDNSAnswers": rsWSDTwoDNSAnswers,
       "rsWSDStatisticsDstIpAddr": rsWSDStatisticsDstIpAddr,
       "rsWSDStatisticsReportingMode": rsWSDStatisticsReportingMode,
       "rsWSDGeneralStatisticsPollingTime": rsWSDGeneralStatisticsPollingTime,
       "rsWSDHealthStatisticsPollingTime": rsWSDHealthStatisticsPollingTime,
       "rsWSDAcceptableHTTPCodesTable": rsWSDAcceptableHTTPCodesTable,
       "rsWSDAcceptableHTTPCodeEntry": rsWSDAcceptableHTTPCodeEntry,
       "rsWSDAcceptableHTTPCodeFarm": rsWSDAcceptableHTTPCodeFarm,
       "rsWSDAcceptableHTTPCode": rsWSDAcceptableHTTPCode,
       "rsWSDAcceptableHTTPCodeStatus": rsWSDAcceptableHTTPCodeStatus,
       "rsWSDTotalNumberOfClients": rsWSDTotalNumberOfClients,
       "rsWSDCurrentNumberOfClients": rsWSDCurrentNumberOfClients,
       "rsWSDFramesLoadInBytes": rsWSDFramesLoadInBytes,
       "rsWSDRedundancyFailed": rsWSDRedundancyFailed,
       "rsWSDRedundancyTakeOver": rsWSDRedundancyTakeOver,
       "rsWSDDynamicProximityTableFilledUp": rsWSDDynamicProximityTableFilledUp,
       "rsWSDClientTableFilledUp": rsWSDClientTableFilledUp,
       "rsWSDSSFTable": rsWSDSSFTable,
       "rsWSDSSFEntry": rsWSDSSFEntry,
       "rsWSDSSFName": rsWSDSSFName,
       "rsWSDSSFStatus": rsWSDSSFStatus,
       "rsWSDSSFCheckMethod": rsWSDSSFCheckMethod,
       "rsWSDSSFCheckInterval": rsWSDSSFCheckInterval,
       "rsWSDSSFCheckRetries": rsWSDSSFCheckRetries,
       "rsWSDSSFCheckPort": rsWSDSSFCheckPort,
       "rsWSDSSFCheckCommunity": rsWSDSSFCheckCommunity,
       "rsWSDSSFMode": rsWSDSSFMode,
       "rsWSDSSFOperStatus": rsWSDSSFOperStatus,
       "rsWSDSSFId": rsWSDSSFId,
       "rsWSDSecondaryServerTable": rsWSDSecondaryServerTable,
       "rsWSDSecondaryServerEntry": rsWSDSecondaryServerEntry,
       "rsWSDSecondaryServerSSFName": rsWSDSecondaryServerSSFName,
       "rsWSDSecondaryServerAddr": rsWSDSecondaryServerAddr,
       "rsWSDSecondaryServerStatus": rsWSDSecondaryServerStatus,
       "rsWSDSecondaryServerOperStatus": rsWSDSecondaryServerOperStatus,
       "rsWSDSecondaryServerId": rsWSDSecondaryServerId,
       "rsWSDSSFFarmTable": rsWSDSSFFarmTable,
       "rsWSDSSFFarmEntry": rsWSDSSFFarmEntry,
       "rsWSDSSFFarmSSFName": rsWSDSSFFarmSSFName,
       "rsWSDSSFFarmAddr": rsWSDSSFFarmAddr,
       "rsWSDSSFFarmStatus": rsWSDSSFFarmStatus,
       "rsWSDSSFFarmId": rsWSDSSFFarmId,
       "rsWSDClientGroupingMask": rsWSDClientGroupingMask,
       "rsWSDSSFServerTable": rsWSDSSFServerTable,
       "rsWSDSSFServerEntry": rsWSDSSFServerEntry,
       "rsWSDSSFServerSSFName": rsWSDSSFServerSSFName,
       "rsWSDSSFServerFarmAddr": rsWSDSSFServerFarmAddr,
       "rsWSDSSFServerSrvrAddr": rsWSDSSFServerSrvrAddr,
       "rsWSDSSFServerStatus": rsWSDSSFServerStatus,
       "rsWSDSSFServerId": rsWSDSSFServerId,
       "rsWSDHTTPContentCheckTable": rsWSDHTTPContentCheckTable,
       "rsWSDHTTPContentCheckEntry": rsWSDHTTPContentCheckEntry,
       "rsWSDHTTPContentCheckFarm": rsWSDHTTPContentCheckFarm,
       "rsWSDHTTPContentCheckString": rsWSDHTTPContentCheckString,
       "rsWSDHTTPContentCheckMode": rsWSDHTTPContentCheckMode,
       "rsWSDHTTPContentCheckStatus": rsWSDHTTPContentCheckStatus,
       "rsNWSDStats": rsNWSDStats,
       "rsWSDTotalDNSReqCounter": rsWSDTotalDNSReqCounter,
       "rsWSDAnsweredDNSReqCounter": rsWSDAnsweredDNSReqCounter,
       "rsWSDBadDNSReqCounter": rsWSDBadDNSReqCounter,
       "rsWSDTotalDNSReqLastSecCounter": rsWSDTotalDNSReqLastSecCounter,
       "rsWSDAnsweredDNSReqLastSecCounter": rsWSDAnsweredDNSReqLastSecCounter,
       "rsWSDBadDNSReqLastSecCounter": rsWSDBadDNSReqLastSecCounter,
       "rsNWSDFarmStatisticsTable": rsNWSDFarmStatisticsTable,
       "rsNWSDFarmStatisticsEntry": rsNWSDFarmStatisticsEntry,
       "rsNWSDFarmStatisticsAddress": rsNWSDFarmStatisticsAddress,
       "rsNWSDFarmStatisticsAttachedUsersNumber": rsNWSDFarmStatisticsAttachedUsersNumber,
       "rsNWSDFarmStatisticsTotalAttachedUsersNumber": rsNWSDFarmStatisticsTotalAttachedUsersNumber,
       "rsNWSDFarmStatisticsPeakLoad": rsNWSDFarmStatisticsPeakLoad,
       "rsNWSDFarmStatisticsFramesLoad": rsNWSDFarmStatisticsFramesLoad,
       "rsNWSDFarmStatisticsFramesRate": rsNWSDFarmStatisticsFramesRate,
       "rsNWSDFarmStatisticsFramesLoadInBytes": rsNWSDFarmStatisticsFramesLoadInBytes,
       "rsNWSDFarmStatisticsFramesRateInBytes": rsNWSDFarmStatisticsFramesRateInBytes,
       "rsNWSDFarmStatisticsBackupServerUsed": rsNWSDFarmStatisticsBackupServerUsed,
       "rsNWSDFarmStatisticsDistThresholdReached": rsNWSDFarmStatisticsDistThresholdReached,
       "rsNWSDFarmStatisticsCapacityThresholdReached": rsNWSDFarmStatisticsCapacityThresholdReached,
       "rsNWSDFarmStatisticsTotalDNSReqCounter": rsNWSDFarmStatisticsTotalDNSReqCounter,
       "rsNWSDFarmStatisticsTotalDNSReqLastSecCounter": rsNWSDFarmStatisticsTotalDNSReqLastSecCounter,
       "rsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter": rsNWSDFarmStatisticsLocalyAnsweredDNSReqCounter,
       "rsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter": rsNWSDFarmStatisticsLocalyAnsweredDNSReqLastSecCounter,
       "rsNWSDFarmStatisticsRedirectedDNSReqCounter": rsNWSDFarmStatisticsRedirectedDNSReqCounter,
       "rsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter": rsNWSDFarmStatisticsRedirectedDNSReqLastSecCounter,
       "rsNWSDFarmStatisticsTotalHTTPSessionsCounter": rsNWSDFarmStatisticsTotalHTTPSessionsCounter,
       "rsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter": rsNWSDFarmStatisticsTotalHTTPSessionsLastSecCounter,
       "rsNWSDFarmStatisticsLocalHTTPSessionsCounter": rsNWSDFarmStatisticsLocalHTTPSessionsCounter,
       "rsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter": rsNWSDFarmStatisticsLocalHTTPSessionsLastSecCounter,
       "rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter": rsNWSDFarmStatisticsRedirectedHTTPSessionsCounter,
       "rsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter": rsNWSDFarmStatisticsRedirectedHTTPSessionsLastSecCounter,
       "rsNWSDFarmStatisticsTotalTriangSessionsCounter": rsNWSDFarmStatisticsTotalTriangSessionsCounter,
       "rsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter": rsNWSDFarmStatisticsTotalTriangSessionsLastSecCounter,
       "rsNWSDFarmStatisticsLocalTriangSessionsCounter": rsNWSDFarmStatisticsLocalTriangSessionsCounter,
       "rsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter": rsNWSDFarmStatisticsLocalTriangSessionsLastSecCounter,
       "rsNWSDFarmStatisticsRedirectedTriangSessionsCounter": rsNWSDFarmStatisticsRedirectedTriangSessionsCounter,
       "rsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter": rsNWSDFarmStatisticsRedirectedTriangSessionsLastSecCounter,
       "rsNWSDServerStatisticsTable": rsNWSDServerStatisticsTable,
       "rsNWSDServerStatisticsEntry": rsNWSDServerStatisticsEntry,
       "rsNWSDServerStatisticsFarmAddr": rsNWSDServerStatisticsFarmAddr,
       "rsNWSDServerStatisticsServerAddr": rsNWSDServerStatisticsServerAddr,
       "rsNWSDServerStatisticsAttachedUsersNumber": rsNWSDServerStatisticsAttachedUsersNumber,
       "rsNWSDServerStatisticsPeakLoad": rsNWSDServerStatisticsPeakLoad,
       "rsNWSDServerStatisticsFramesRate": rsNWSDServerStatisticsFramesRate,
       "rsNWSDServerStatisticsFramesLoad": rsNWSDServerStatisticsFramesLoad,
       "rsNWSDServerStatisticsTotalAttachedUsersNumber": rsNWSDServerStatisticsTotalAttachedUsersNumber,
       "rsNWSDServerStatisticsFramesLoadInBytes": rsNWSDServerStatisticsFramesLoadInBytes,
       "rsNWSDServerStatisticsFramesRateInBytes": rsNWSDServerStatisticsFramesRateInBytes,
       "rsNWSDServerStatisticsConnectivityCheckFailed": rsNWSDServerStatisticsConnectivityCheckFailed,
       "rsNWSDServerStatisticsConnectionLimitReached": rsNWSDServerStatisticsConnectionLimitReached,
       "rsNWSDServerStatisticsAnsweredDNSReqCounter": rsNWSDServerStatisticsAnsweredDNSReqCounter,
       "rsNWSDServerStatisticsAnsweredDNSReqLastSecCounter": rsNWSDServerStatisticsAnsweredDNSReqLastSecCounter,
       "rsNWSDServerStatisticsRedirectedHTTPSessions": rsNWSDServerStatisticsRedirectedHTTPSessions,
       "rsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter": rsNWSDServerStatisticsRedirectedHTTPSessionsLastSecCounter,
       "rsNWSDServerStatisticsRedirectedTriangSessions": rsNWSDServerStatisticsRedirectedTriangSessions,
       "rsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount": rsNWSDServerStatisticsRedirectedTriangSessionsLastSecCount,
       "rsWSDCookieTable": rsWSDCookieTable,
       "rsWSDCookieTableEntry": rsWSDCookieTableEntry,
       "rsWSDCookieFarm": rsWSDCookieFarm,
       "rsWSDCookieValue": rsWSDCookieValue,
       "rsWSDCookieServer": rsWSDCookieServer,
       "rsWSDCookieStatus": rsWSDCookieStatus,
       "rsWSDTrackUDPSessionsMode": rsWSDTrackUDPSessionsMode,
       "rsWSDTrackSSLIDinSelectServerMode": rsWSDTrackSSLIDinSelectServerMode,
       "rsWSDTuning": rsWSDTuning,
       "rsWSDMaxURLEntriesTuning": rsWSDMaxURLEntriesTuning,
       "rsWSDMaxURLEntries": rsWSDMaxURLEntries,
       "rsWSDMaxURLEntriesAfterReset": rsWSDMaxURLEntriesAfterReset,
       "rsWSDMaxRequestEntriesTuning": rsWSDMaxRequestEntriesTuning,
       "rsWSDMaxRequestEntries": rsWSDMaxRequestEntries,
       "rsWSDMaxRequestEntriesAfterReset": rsWSDMaxRequestEntriesAfterReset,
       "rsWSDMaxSSLEntriesTuning": rsWSDMaxSSLEntriesTuning,
       "rsWSDMaxSSLEntries": rsWSDMaxSSLEntries,
       "rsWSDMaxSSLEntriesAfterReset": rsWSDMaxSSLEntriesAfterReset,
       "rsWSDTweaks": rsWSDTweaks,
       "rsWSDMaintainURLSFPersistency": rsWSDMaintainURLSFPersistency,
       "rsWSDAllowAnyAppPortForCookies": rsWSDAllowAnyAppPortForCookies,
       "rsWSDSrcPortInClientHash": rsWSDSrcPortInClientHash,
       "rsWSDUserDefinedTimeoutAfterTCPFailure": rsWSDUserDefinedTimeoutAfterTCPFailure,
       "rsWSDNoSlashAfterGET": rsWSDNoSlashAfterGET,
       "rsWSDTimeoutForSYN": rsWSDTimeoutForSYN,
       "rsWSDSpecificNATAddress": rsWSDSpecificNATAddress,
       "rsWSDExtendedCheckHostMode": rsWSDExtendedCheckHostMode,
       "rsWSDExtendedLRPSecurity": rsWSDExtendedLRPSecurity,
       "rsWSDURLCookies": rsWSDURLCookies,
       "rsWSDURLTableLookupPrecedence": rsWSDURLTableLookupPrecedence,
       "rsWSDExtendedFarmTable": rsWSDExtendedFarmTable,
       "rsWSDExtendedFarmEntry": rsWSDExtendedFarmEntry,
       "rsWSDExtendedFarmAddress": rsWSDExtendedFarmAddress,
       "rsWSDExtendedFarmHttpsType": rsWSDExtendedFarmHttpsType,
       "rsWSDConnCheckSecret": rsWSDConnCheckSecret,
       "rsWSDOverLoadStatus": rsWSDOverLoadStatus,
       "rsWSDFarmURLCookies": rsWSDFarmURLCookies,
       "rsWSDExtendedFarmNATRangeIPFrom": rsWSDExtendedFarmNATRangeIPFrom,
       "rsWSDNHRTable": rsWSDNHRTable,
       "rsWSDNHREntry": rsWSDNHREntry,
       "rsWSDNHRNHRIP": rsWSDNHRNHRIP,
       "rsWSDNHRDestinationMAC": rsWSDNHRDestinationMAC,
       "rsWSDNHRSourceMAC": rsWSDNHRSourceMAC,
       "rsWSDNHRPhysicalPortNumber": rsWSDNHRPhysicalPortNumber,
       "rsWSDNHRAdminStatus": rsWSDNHRAdminStatus,
       "rsWSDNHROperStatus": rsWSDNHROperStatus,
       "rsWSDNHRPathHealthCheckIP": rsWSDNHRPathHealthCheckIP,
       "rsWSDNHRCheckMethod": rsWSDNHRCheckMethod,
       "rsWSDNHRCheckInterval": rsWSDNHRCheckInterval,
       "rsWSDNRHCheckRetries": rsWSDNRHCheckRetries,
       "rsWSDNHRRowStatus": rsWSDNHRRowStatus,
       "rsWSDNHRTag": rsWSDNHRTag,
       "rsWSDVIPNHRTable": rsWSDVIPNHRTable,
       "rsWSDVIPNHREntry": rsWSDVIPNHREntry,
       "rsWSDVIPNHRVIP": rsWSDVIPNHRVIP,
       "rsWSDVIPNHRNHRIP": rsWSDVIPNHRNHRIP,
       "rsWSDVIPNHRBackupNHRIP": rsWSDVIPNHRBackupNHRIP,
       "rsWSDVIPNHRNoRouteAction": rsWSDVIPNHRNoRouteAction,
       "rsWSDVIPNHRRowStatus": rsWSDVIPNHRRowStatus,
       "rsWSDVIPNHRNHRWeight": rsWSDVIPNHRNHRWeight,
       "rsWSDVIPNHRBackupWeight": rsWSDVIPNHRBackupWeight,
       "rsWSDVIPNHRAdminLoadSharing": rsWSDVIPNHRAdminLoadSharing,
       "rsWSDTokenTable": rsWSDTokenTable,
       "rsWSDTokenTableEntry": rsWSDTokenTableEntry,
       "rsWSDToken": rsWSDToken,
       "rsWSDTokenFarmMap": rsWSDTokenFarmMap,
       "rsWSDTokenFarm": rsWSDTokenFarm,
       "rsWSDTokenDefault": rsWSDTokenDefault,
       "rsWSDTokenStatus": rsWSDTokenStatus,
       "rsWSDVirtualDNSTable": rsWSDVirtualDNSTable,
       "rsWSDVirtualDNSTableEntry": rsWSDVirtualDNSTableEntry,
       "rsWSDVirtualDNSAddress": rsWSDVirtualDNSAddress,
       "rsWSDVirtualDNSRedunType": rsWSDVirtualDNSRedunType,
       "rsWSDVirtualDNSStatus": rsWSDVirtualDNSStatus,
       "rsWSDClientNAT": rsWSDClientNAT,
       "rsWSDClientNATRangeTable": rsWSDClientNATRangeTable,
       "rsWSDClientNATRangeIPEntry": rsWSDClientNATRangeIPEntry,
       "rsWSDClientNATRangeIPFrom": rsWSDClientNATRangeIPFrom,
       "rsWSDClientNATRangeIPTo": rsWSDClientNATRangeIPTo,
       "rsWSDClientNATRangeIPStatus": rsWSDClientNATRangeIPStatus,
       "rsWSDNATRangeTable": rsWSDNATRangeTable,
       "rsWSDNATRangeIPEntry": rsWSDNATRangeIPEntry,
       "rsWSDNATRangeIPFrom": rsWSDNATRangeIPFrom,
       "rsWSDNATRangeIPTo": rsWSDNATRangeIPTo,
       "rsWSDNATRangeStatus": rsWSDNATRangeStatus,
       "rsWSDClientNATStatus": rsWSDClientNATStatus,
       "rsWSDSessionChaining": rsWSDSessionChaining,
       "rsWSDClientTableSizeThresh": rsWSDClientTableSizeThresh,
       "rsWSDLogicServConnectLimitThresh": rsWSDLogicServConnectLimitThresh,
       "rsWSDPhysServConnectLimitThresh": rsWSDPhysServConnectLimitThresh,
       "rsWSDFarmCapacityLimitThresh": rsWSDFarmCapacityLimitThresh,
       "rsWSDServBandwidthLimitThresh": rsWSDServBandwidthLimitThresh,
       "rsWSDFarmBandwidthLimitThresh": rsWSDFarmBandwidthLimitThresh}
)
