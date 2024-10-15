# SNMP MIB module (MLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:32 2024
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

(rsMLB,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rsMLB")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsMLBApplicationServersTable_Object = MibTable
rsMLBApplicationServersTable = _RsMLBApplicationServersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1)
)
if mibBuilder.loadTexts:
    rsMLBApplicationServersTable.setStatus("mandatory")
_RsMLBApplicationServerEntry_Object = MibTableRow
rsMLBApplicationServerEntry = _RsMLBApplicationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1)
)
rsMLBApplicationServerEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBServerAddr"),
)
if mibBuilder.loadTexts:
    rsMLBApplicationServerEntry.setStatus("mandatory")
_RsMLBServerAddr_Type = IpAddress
_RsMLBServerAddr_Object = MibTableColumn
rsMLBServerAddr = _RsMLBServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 1),
    _RsMLBServerAddr_Type()
)
rsMLBServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerAddr.setStatus("mandatory")


class _RsMLBServerName_Type(DisplayString):
    """Custom type rsMLBServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsMLBServerName_Type.__name__ = "DisplayString"
_RsMLBServerName_Object = MibTableColumn
rsMLBServerName = _RsMLBServerName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 2),
    _RsMLBServerName_Type()
)
rsMLBServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerName.setStatus("mandatory")


class _RsMLBServerOperStatus_Type(Integer32):
    """Custom type rsMLBServerOperStatus based on Integer32"""
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


_RsMLBServerOperStatus_Type.__name__ = "Integer32"
_RsMLBServerOperStatus_Object = MibTableColumn
rsMLBServerOperStatus = _RsMLBServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 3),
    _RsMLBServerOperStatus_Type()
)
rsMLBServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerOperStatus.setStatus("mandatory")


class _RsMLBServerWeight_Type(Integer32):
    """Custom type rsMLBServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsMLBServerWeight_Type.__name__ = "Integer32"
_RsMLBServerWeight_Object = MibTableColumn
rsMLBServerWeight = _RsMLBServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 4),
    _RsMLBServerWeight_Type()
)
rsMLBServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerWeight.setStatus("mandatory")
_RsMLBServerAttachedUsersNumber_Type = Integer32
_RsMLBServerAttachedUsersNumber_Object = MibTableColumn
rsMLBServerAttachedUsersNumber = _RsMLBServerAttachedUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 5),
    _RsMLBServerAttachedUsersNumber_Type()
)
rsMLBServerAttachedUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerAttachedUsersNumber.setStatus("mandatory")
_RsMLBServerPeakLoad_Type = Integer32
_RsMLBServerPeakLoad_Object = MibTableColumn
rsMLBServerPeakLoad = _RsMLBServerPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 6),
    _RsMLBServerPeakLoad_Type()
)
rsMLBServerPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerPeakLoad.setStatus("mandatory")
_RsMLBServerFramesRate_Type = Integer32
_RsMLBServerFramesRate_Object = MibTableColumn
rsMLBServerFramesRate = _RsMLBServerFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 7),
    _RsMLBServerFramesRate_Type()
)
rsMLBServerFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerFramesRate.setStatus("mandatory")
_RsMLBServerFramesLoad_Type = Counter32
_RsMLBServerFramesLoad_Object = MibTableColumn
rsMLBServerFramesLoad = _RsMLBServerFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 8),
    _RsMLBServerFramesLoad_Type()
)
rsMLBServerFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerFramesLoad.setStatus("mandatory")


class _RsMLBServerStatus_Type(Integer32):
    """Custom type rsMLBServerStatus based on Integer32"""
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


_RsMLBServerStatus_Type.__name__ = "Integer32"
_RsMLBServerStatus_Object = MibTableColumn
rsMLBServerStatus = _RsMLBServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 9),
    _RsMLBServerStatus_Type()
)
rsMLBServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerStatus.setStatus("mandatory")


class _RsMLBServerOperMode_Type(Integer32):
    """Custom type rsMLBServerOperMode based on Integer32"""
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


_RsMLBServerOperMode_Type.__name__ = "Integer32"
_RsMLBServerOperMode_Object = MibTableColumn
rsMLBServerOperMode = _RsMLBServerOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 10),
    _RsMLBServerOperMode_Type()
)
rsMLBServerOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerOperMode.setStatus("mandatory")
_RsMLBServerConnectionLimit_Type = Integer32
_RsMLBServerConnectionLimit_Object = MibTableColumn
rsMLBServerConnectionLimit = _RsMLBServerConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 11),
    _RsMLBServerConnectionLimit_Type()
)
rsMLBServerConnectionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerConnectionLimit.setStatus("mandatory")


class _RsMLBServerAdminStatus_Type(Integer32):
    """Custom type rsMLBServerAdminStatus based on Integer32"""
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


_RsMLBServerAdminStatus_Type.__name__ = "Integer32"
_RsMLBServerAdminStatus_Object = MibTableColumn
rsMLBServerAdminStatus = _RsMLBServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 12),
    _RsMLBServerAdminStatus_Type()
)
rsMLBServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerAdminStatus.setStatus("mandatory")


class _RsMLBServerType_Type(Integer32):
    """Custom type rsMLBServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nextHopRouter", 2),
          ("regular", 1))
    )


_RsMLBServerType_Type.__name__ = "Integer32"
_RsMLBServerType_Object = MibTableColumn
rsMLBServerType = _RsMLBServerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 13),
    _RsMLBServerType_Type()
)
rsMLBServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerType.setStatus("mandatory")


class _RsMLBServerMacStatus_Type(Integer32):
    """Custom type rsMLBServerMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("found", 1),
          ("notFound", 2))
    )


_RsMLBServerMacStatus_Type.__name__ = "Integer32"
_RsMLBServerMacStatus_Object = MibTableColumn
rsMLBServerMacStatus = _RsMLBServerMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 14),
    _RsMLBServerMacStatus_Type()
)
rsMLBServerMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerMacStatus.setStatus("mandatory")
_RsMLBServerPortNumber_Type = Integer32
_RsMLBServerPortNumber_Object = MibTableColumn
rsMLBServerPortNumber = _RsMLBServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 15),
    _RsMLBServerPortNumber_Type()
)
rsMLBServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerPortNumber.setStatus("mandatory")
_RsMLBServerPeakBytesLoad_Type = Integer32
_RsMLBServerPeakBytesLoad_Object = MibTableColumn
rsMLBServerPeakBytesLoad = _RsMLBServerPeakBytesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 16),
    _RsMLBServerPeakBytesLoad_Type()
)
rsMLBServerPeakBytesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerPeakBytesLoad.setStatus("mandatory")
_RsMLBServerBytesRate_Type = Integer32
_RsMLBServerBytesRate_Object = MibTableColumn
rsMLBServerBytesRate = _RsMLBServerBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 17),
    _RsMLBServerBytesRate_Type()
)
rsMLBServerBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerBytesRate.setStatus("mandatory")
_RsMLBServerBytesLoad_Type = Counter32
_RsMLBServerBytesLoad_Object = MibTableColumn
rsMLBServerBytesLoad = _RsMLBServerBytesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 18),
    _RsMLBServerBytesLoad_Type()
)
rsMLBServerBytesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerBytesLoad.setStatus("mandatory")
_RsMLBServerRecoveryTime_Type = Integer32
_RsMLBServerRecoveryTime_Object = MibTableColumn
rsMLBServerRecoveryTime = _RsMLBServerRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 19),
    _RsMLBServerRecoveryTime_Type()
)
rsMLBServerRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerRecoveryTime.setStatus("mandatory")
_RsMLBServerWarmUpTime_Type = Integer32
_RsMLBServerWarmUpTime_Object = MibTableColumn
rsMLBServerWarmUpTime = _RsMLBServerWarmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 20),
    _RsMLBServerWarmUpTime_Type()
)
rsMLBServerWarmUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerWarmUpTime.setStatus("mandatory")
_RsMLBServerTotalFramesLoad_Type = Counter32
_RsMLBServerTotalFramesLoad_Object = MibTableColumn
rsMLBServerTotalFramesLoad = _RsMLBServerTotalFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 21),
    _RsMLBServerTotalFramesLoad_Type()
)
rsMLBServerTotalFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBServerTotalFramesLoad.setStatus("mandatory")


class _RsMLBServerProximityCheck_Type(Integer32):
    """Custom type rsMLBServerProximityCheck based on Integer32"""
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


_RsMLBServerProximityCheck_Type.__name__ = "Integer32"
_RsMLBServerProximityCheck_Object = MibTableColumn
rsMLBServerProximityCheck = _RsMLBServerProximityCheck_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 1, 22),
    _RsMLBServerProximityCheck_Type()
)
rsMLBServerProximityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBServerProximityCheck.setStatus("mandatory")
_RsMLBdummy1_Type = Integer32
_RsMLBdummy1_Object = MibScalar
rsMLBdummy1 = _RsMLBdummy1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 1, 2),
    _RsMLBdummy1_Type()
)
rsMLBdummy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy1.setStatus("mandatory")


class _RsMLBAdminStatus_Type(Integer32):
    """Custom type rsMLBAdminStatus based on Integer32"""
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


_RsMLBAdminStatus_Type.__name__ = "Integer32"
_RsMLBAdminStatus_Object = MibScalar
rsMLBAdminStatus = _RsMLBAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 2),
    _RsMLBAdminStatus_Type()
)
rsMLBAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBAdminStatus.setStatus("mandatory")
_RsMLBClientsLifeTime_Type = Integer32
_RsMLBClientsLifeTime_Object = MibScalar
rsMLBClientsLifeTime = _RsMLBClientsLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 3),
    _RsMLBClientsLifeTime_Type()
)
rsMLBClientsLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBClientsLifeTime.setStatus("mandatory")


class _RsMLBDispatchMethod_Type(Integer32):
    """Custom type rsMLBDispatchMethod based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cyclic", 1),
          ("leastBytesNumber", 8),
          ("leastTraffic", 2),
          ("leastUsersNumber", 3),
          ("nt-1", 4),
          ("nt-2", 5),
          ("private-1", 6),
          ("private-2", 7))
    )


_RsMLBDispatchMethod_Type.__name__ = "Integer32"
_RsMLBDispatchMethod_Object = MibScalar
rsMLBDispatchMethod = _RsMLBDispatchMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 4),
    _RsMLBDispatchMethod_Type()
)
rsMLBDispatchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDispatchMethod.setStatus("mandatory")


class _RsMLBCheckConnectivityStatus_Type(Integer32):
    """Custom type rsMLBCheckConnectivityStatus based on Integer32"""
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


_RsMLBCheckConnectivityStatus_Type.__name__ = "Integer32"
_RsMLBCheckConnectivityStatus_Object = MibScalar
rsMLBCheckConnectivityStatus = _RsMLBCheckConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 5),
    _RsMLBCheckConnectivityStatus_Type()
)
rsMLBCheckConnectivityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBCheckConnectivityStatus.setStatus("mandatory")
_RsMLBCheckConnectivityMethod_Type = Integer32
_RsMLBCheckConnectivityMethod_Object = MibScalar
rsMLBCheckConnectivityMethod = _RsMLBCheckConnectivityMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 6),
    _RsMLBCheckConnectivityMethod_Type()
)
rsMLBCheckConnectivityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBCheckConnectivityMethod.setStatus("mandatory")


class _RsMLBCheckConnectivityInterval_Type(Integer32):
    """Custom type rsMLBCheckConnectivityInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsMLBCheckConnectivityInterval_Type.__name__ = "Integer32"
_RsMLBCheckConnectivityInterval_Object = MibScalar
rsMLBCheckConnectivityInterval = _RsMLBCheckConnectivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 7),
    _RsMLBCheckConnectivityInterval_Type()
)
rsMLBCheckConnectivityInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBCheckConnectivityInterval.setStatus("mandatory")


class _RsMLBCheckConnectivityRetries_Type(Integer32):
    """Custom type rsMLBCheckConnectivityRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RsMLBCheckConnectivityRetries_Type.__name__ = "Integer32"
_RsMLBCheckConnectivityRetries_Object = MibScalar
rsMLBCheckConnectivityRetries = _RsMLBCheckConnectivityRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 8),
    _RsMLBCheckConnectivityRetries_Type()
)
rsMLBCheckConnectivityRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBCheckConnectivityRetries.setStatus("mandatory")
_RsMLBClientsConnectDenials_Type = Counter32
_RsMLBClientsConnectDenials_Object = MibScalar
rsMLBClientsConnectDenials = _RsMLBClientsConnectDenials_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 9),
    _RsMLBClientsConnectDenials_Type()
)
rsMLBClientsConnectDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBClientsConnectDenials.setStatus("mandatory")
_RsMLBClientsTable_Object = MibTable
rsMLBClientsTable = _RsMLBClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10)
)
if mibBuilder.loadTexts:
    rsMLBClientsTable.setStatus("mandatory")
_RsMLBClientEntry_Object = MibTableRow
rsMLBClientEntry = _RsMLBClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1)
)
rsMLBClientEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBClientAddr"),
    (0, "MLB-MIB", "rsMLBDestinationAddr"),
)
if mibBuilder.loadTexts:
    rsMLBClientEntry.setStatus("mandatory")
_RsMLBClientAddr_Type = IpAddress
_RsMLBClientAddr_Object = MibTableColumn
rsMLBClientAddr = _RsMLBClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 1),
    _RsMLBClientAddr_Type()
)
rsMLBClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBClientAddr.setStatus("mandatory")
_RsMLBDestinationAddr_Type = IpAddress
_RsMLBDestinationAddr_Object = MibTableColumn
rsMLBDestinationAddr = _RsMLBDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 2),
    _RsMLBDestinationAddr_Type()
)
rsMLBDestinationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDestinationAddr.setStatus("mandatory")
_RsMLBAttachedServerAddr_Type = IpAddress
_RsMLBAttachedServerAddr_Object = MibTableColumn
rsMLBAttachedServerAddr = _RsMLBAttachedServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 3),
    _RsMLBAttachedServerAddr_Type()
)
rsMLBAttachedServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBAttachedServerAddr.setStatus("mandatory")
_RsMLBClientLastActivityTime_Type = Integer32
_RsMLBClientLastActivityTime_Object = MibTableColumn
rsMLBClientLastActivityTime = _RsMLBClientLastActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 4),
    _RsMLBClientLastActivityTime_Type()
)
rsMLBClientLastActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBClientLastActivityTime.setStatus("mandatory")
_RsMLBClientAttachmentTime_Type = Integer32
_RsMLBClientAttachmentTime_Object = MibTableColumn
rsMLBClientAttachmentTime = _RsMLBClientAttachmentTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 5),
    _RsMLBClientAttachmentTime_Type()
)
rsMLBClientAttachmentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBClientAttachmentTime.setStatus("mandatory")


class _RsMLBClientStatus_Type(Integer32):
    """Custom type rsMLBClientStatus based on Integer32"""
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


_RsMLBClientStatus_Type.__name__ = "Integer32"
_RsMLBClientStatus_Object = MibTableColumn
rsMLBClientStatus = _RsMLBClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 1, 6),
    _RsMLBClientStatus_Type()
)
rsMLBClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBClientStatus.setStatus("mandatory")
_RsMLBdummy2_Type = Integer32
_RsMLBdummy2_Object = MibScalar
rsMLBdummy2 = _RsMLBdummy2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 10, 2),
    _RsMLBdummy2_Type()
)
rsMLBdummy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy2.setStatus("mandatory")


class _RsMLBSessionTracking_Type(Integer32):
    """Custom type rsMLBSessionTracking based on Integer32"""
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


_RsMLBSessionTracking_Type.__name__ = "Integer32"
_RsMLBSessionTracking_Object = MibScalar
rsMLBSessionTracking = _RsMLBSessionTracking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 11),
    _RsMLBSessionTracking_Type()
)
rsMLBSessionTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSessionTracking.setStatus("mandatory")
_RsMLBRemoteConnectivityTable_Object = MibTable
rsMLBRemoteConnectivityTable = _RsMLBRemoteConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12)
)
if mibBuilder.loadTexts:
    rsMLBRemoteConnectivityTable.setStatus("mandatory")
_RsMLBRemoteConnectivityEntry_Object = MibTableRow
rsMLBRemoteConnectivityEntry = _RsMLBRemoteConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 1)
)
rsMLBRemoteConnectivityEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBRmtConSrvrAddr"),
    (0, "MLB-MIB", "rsMLBRmtConIpAddr"),
)
if mibBuilder.loadTexts:
    rsMLBRemoteConnectivityEntry.setStatus("mandatory")
_RsMLBRmtConSrvrAddr_Type = IpAddress
_RsMLBRmtConSrvrAddr_Object = MibTableColumn
rsMLBRmtConSrvrAddr = _RsMLBRmtConSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 1, 1),
    _RsMLBRmtConSrvrAddr_Type()
)
rsMLBRmtConSrvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRmtConSrvrAddr.setStatus("mandatory")
_RsMLBRmtConIpAddr_Type = IpAddress
_RsMLBRmtConIpAddr_Object = MibTableColumn
rsMLBRmtConIpAddr = _RsMLBRmtConIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 1, 2),
    _RsMLBRmtConIpAddr_Type()
)
rsMLBRmtConIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRmtConIpAddr.setStatus("mandatory")


class _RsMLBRmtConStatus_Type(Integer32):
    """Custom type rsMLBRmtConStatus based on Integer32"""
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


_RsMLBRmtConStatus_Type.__name__ = "Integer32"
_RsMLBRmtConStatus_Object = MibTableColumn
rsMLBRmtConStatus = _RsMLBRmtConStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 1, 3),
    _RsMLBRmtConStatus_Type()
)
rsMLBRmtConStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBRmtConStatus.setStatus("mandatory")


class _RsMLBRmtConOperStatus_Type(Integer32):
    """Custom type rsMLBRmtConOperStatus based on Integer32"""
    defaultValue = 1

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


_RsMLBRmtConOperStatus_Type.__name__ = "Integer32"
_RsMLBRmtConOperStatus_Object = MibTableColumn
rsMLBRmtConOperStatus = _RsMLBRmtConOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 1, 4),
    _RsMLBRmtConOperStatus_Type()
)
rsMLBRmtConOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRmtConOperStatus.setStatus("mandatory")
_RsMLBdummy3_Type = Integer32
_RsMLBdummy3_Object = MibScalar
rsMLBdummy3 = _RsMLBdummy3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 12, 2),
    _RsMLBdummy3_Type()
)
rsMLBdummy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy3.setStatus("mandatory")


class _RsMLBClientTableMode_Type(Integer32):
    """Custom type rsMLBClientTableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 1),
          ("layer4", 2))
    )


_RsMLBClientTableMode_Type.__name__ = "Integer32"
_RsMLBClientTableMode_Object = MibScalar
rsMLBClientTableMode = _RsMLBClientTableMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 13),
    _RsMLBClientTableMode_Type()
)
rsMLBClientTableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBClientTableMode.setStatus("mandatory")
_RsMLBRulesTable_Object = MibTable
rsMLBRulesTable = _RsMLBRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14)
)
if mibBuilder.loadTexts:
    rsMLBRulesTable.setStatus("mandatory")
_RsMLBRulesEntry_Object = MibTableRow
rsMLBRulesEntry = _RsMLBRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14, 1)
)
rsMLBRulesEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBRulesPortNumber"),
)
if mibBuilder.loadTexts:
    rsMLBRulesEntry.setStatus("mandatory")
_RsMLBRulesPortNumber_Type = Integer32
_RsMLBRulesPortNumber_Object = MibTableColumn
rsMLBRulesPortNumber = _RsMLBRulesPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14, 1, 1),
    _RsMLBRulesPortNumber_Type()
)
rsMLBRulesPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRulesPortNumber.setStatus("mandatory")
_RsMLBRulesLeavingPort_Type = Integer32
_RsMLBRulesLeavingPort_Object = MibTableColumn
rsMLBRulesLeavingPort = _RsMLBRulesLeavingPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14, 1, 2),
    _RsMLBRulesLeavingPort_Type()
)
rsMLBRulesLeavingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBRulesLeavingPort.setStatus("mandatory")
_RsMLBRulesNumOfServers_Type = Integer32
_RsMLBRulesNumOfServers_Object = MibTableColumn
rsMLBRulesNumOfServers = _RsMLBRulesNumOfServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14, 1, 3),
    _RsMLBRulesNumOfServers_Type()
)
rsMLBRulesNumOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRulesNumOfServers.setStatus("mandatory")
_RsMLBdummy4_Type = Integer32
_RsMLBdummy4_Object = MibScalar
rsMLBdummy4 = _RsMLBdummy4_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 14, 2),
    _RsMLBdummy4_Type()
)
rsMLBdummy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy4.setStatus("mandatory")


class _RsMLBTranslateOutBoundMode_Type(Integer32):
    """Custom type rsMLBTranslateOutBoundMode based on Integer32"""
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


_RsMLBTranslateOutBoundMode_Type.__name__ = "Integer32"
_RsMLBTranslateOutBoundMode_Object = MibScalar
rsMLBTranslateOutBoundMode = _RsMLBTranslateOutBoundMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 15),
    _RsMLBTranslateOutBoundMode_Type()
)
rsMLBTranslateOutBoundMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBTranslateOutBoundMode.setStatus("mandatory")
_RsMLBVirtualIPTable_Object = MibTable
rsMLBVirtualIPTable = _RsMLBVirtualIPTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16)
)
if mibBuilder.loadTexts:
    rsMLBVirtualIPTable.setStatus("mandatory")
_RsMLBVirtualIPEntry_Object = MibTableRow
rsMLBVirtualIPEntry = _RsMLBVirtualIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16, 1)
)
rsMLBVirtualIPEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBVirtualIPAddress"),
)
if mibBuilder.loadTexts:
    rsMLBVirtualIPEntry.setStatus("mandatory")
_RsMLBVirtualIPAddress_Type = IpAddress
_RsMLBVirtualIPAddress_Object = MibTableColumn
rsMLBVirtualIPAddress = _RsMLBVirtualIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16, 1, 1),
    _RsMLBVirtualIPAddress_Type()
)
rsMLBVirtualIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBVirtualIPAddress.setStatus("mandatory")


class _RsMLBVirtualMode_Type(Integer32):
    """Custom type rsMLBVirtualMode based on Integer32"""
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


_RsMLBVirtualMode_Type.__name__ = "Integer32"
_RsMLBVirtualMode_Object = MibTableColumn
rsMLBVirtualMode = _RsMLBVirtualMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16, 1, 2),
    _RsMLBVirtualMode_Type()
)
rsMLBVirtualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBVirtualMode.setStatus("mandatory")


class _RsMLBVirtualStatus_Type(Integer32):
    """Custom type rsMLBVirtualStatus based on Integer32"""
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


_RsMLBVirtualStatus_Type.__name__ = "Integer32"
_RsMLBVirtualStatus_Object = MibTableColumn
rsMLBVirtualStatus = _RsMLBVirtualStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16, 1, 3),
    _RsMLBVirtualStatus_Type()
)
rsMLBVirtualStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBVirtualStatus.setStatus("mandatory")
_RsMLBdummy5_Type = Integer32
_RsMLBdummy5_Object = MibScalar
rsMLBdummy5 = _RsMLBdummy5_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 16, 2),
    _RsMLBdummy5_Type()
)
rsMLBdummy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy5.setStatus("mandatory")
_RsMLBMappedIPTable_Object = MibTable
rsMLBMappedIPTable = _RsMLBMappedIPTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17)
)
if mibBuilder.loadTexts:
    rsMLBMappedIPTable.setStatus("mandatory")
_RsMLBMappedIPEntry_Object = MibTableRow
rsMLBMappedIPEntry = _RsMLBMappedIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 1)
)
rsMLBMappedIPEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBMappedVirtualAddress"),
    (0, "MLB-MIB", "rsMLBMappedFirewallIP"),
)
if mibBuilder.loadTexts:
    rsMLBMappedIPEntry.setStatus("mandatory")
_RsMLBMappedVirtualAddress_Type = IpAddress
_RsMLBMappedVirtualAddress_Object = MibTableColumn
rsMLBMappedVirtualAddress = _RsMLBMappedVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 1, 1),
    _RsMLBMappedVirtualAddress_Type()
)
rsMLBMappedVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBMappedVirtualAddress.setStatus("mandatory")
_RsMLBMappedFirewallIP_Type = IpAddress
_RsMLBMappedFirewallIP_Object = MibTableColumn
rsMLBMappedFirewallIP = _RsMLBMappedFirewallIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 1, 2),
    _RsMLBMappedFirewallIP_Type()
)
rsMLBMappedFirewallIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBMappedFirewallIP.setStatus("mandatory")
_RsMLBMappedFirewallNAT_Type = IpAddress
_RsMLBMappedFirewallNAT_Object = MibTableColumn
rsMLBMappedFirewallNAT = _RsMLBMappedFirewallNAT_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 1, 3),
    _RsMLBMappedFirewallNAT_Type()
)
rsMLBMappedFirewallNAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBMappedFirewallNAT.setStatus("mandatory")


class _RsMLBMappedStatus_Type(Integer32):
    """Custom type rsMLBMappedStatus based on Integer32"""
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


_RsMLBMappedStatus_Type.__name__ = "Integer32"
_RsMLBMappedStatus_Object = MibTableColumn
rsMLBMappedStatus = _RsMLBMappedStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 1, 4),
    _RsMLBMappedStatus_Type()
)
rsMLBMappedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBMappedStatus.setStatus("mandatory")
_RsMLBdummy6_Type = Integer32
_RsMLBdummy6_Object = MibScalar
rsMLBdummy6 = _RsMLBdummy6_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 17, 2),
    _RsMLBdummy6_Type()
)
rsMLBdummy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy6.setStatus("mandatory")
_RsMLBVirtualConnectivityIP_Type = IpAddress
_RsMLBVirtualConnectivityIP_Object = MibScalar
rsMLBVirtualConnectivityIP = _RsMLBVirtualConnectivityIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 18),
    _RsMLBVirtualConnectivityIP_Type()
)
rsMLBVirtualConnectivityIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBVirtualConnectivityIP.setStatus("mandatory")


class _RsMLBVirtualConnectivityMode_Type(Integer32):
    """Custom type rsMLBVirtualConnectivityMode based on Integer32"""
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


_RsMLBVirtualConnectivityMode_Type.__name__ = "Integer32"
_RsMLBVirtualConnectivityMode_Object = MibScalar
rsMLBVirtualConnectivityMode = _RsMLBVirtualConnectivityMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 19),
    _RsMLBVirtualConnectivityMode_Type()
)
rsMLBVirtualConnectivityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBVirtualConnectivityMode.setStatus("mandatory")


class _RsMLBRemoveEntryAtSessionEnd_Type(Integer32):
    """Custom type rsMLBRemoveEntryAtSessionEnd based on Integer32"""
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


_RsMLBRemoveEntryAtSessionEnd_Type.__name__ = "Integer32"
_RsMLBRemoveEntryAtSessionEnd_Object = MibScalar
rsMLBRemoveEntryAtSessionEnd = _RsMLBRemoveEntryAtSessionEnd_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 20),
    _RsMLBRemoveEntryAtSessionEnd_Type()
)
rsMLBRemoveEntryAtSessionEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBRemoveEntryAtSessionEnd.setStatus("mandatory")


class _RsMLBFirewallPortID_Type(Integer32):
    """Custom type rsMLBFirewallPortID based on Integer32"""
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


_RsMLBFirewallPortID_Type.__name__ = "Integer32"
_RsMLBFirewallPortID_Object = MibScalar
rsMLBFirewallPortID = _RsMLBFirewallPortID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 21),
    _RsMLBFirewallPortID_Type()
)
rsMLBFirewallPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBFirewallPortID.setStatus("mandatory")
_RsMLBSubnetGroupTable_Object = MibTable
rsMLBSubnetGroupTable = _RsMLBSubnetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23)
)
if mibBuilder.loadTexts:
    rsMLBSubnetGroupTable.setStatus("mandatory")
_RsMLBSubnetGroupEntry_Object = MibTableRow
rsMLBSubnetGroupEntry = _RsMLBSubnetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1)
)
rsMLBSubnetGroupEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBDestSubnetAddr"),
    (0, "MLB-MIB", "rsMLBDestSubnetMask"),
    (0, "MLB-MIB", "rsMLBSubnetSrvrAddr"),
)
if mibBuilder.loadTexts:
    rsMLBSubnetGroupEntry.setStatus("mandatory")
_RsMLBDestSubnetAddr_Type = IpAddress
_RsMLBDestSubnetAddr_Object = MibTableColumn
rsMLBDestSubnetAddr = _RsMLBDestSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1, 1),
    _RsMLBDestSubnetAddr_Type()
)
rsMLBDestSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBDestSubnetAddr.setStatus("mandatory")
_RsMLBDestSubnetMask_Type = IpAddress
_RsMLBDestSubnetMask_Object = MibTableColumn
rsMLBDestSubnetMask = _RsMLBDestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1, 2),
    _RsMLBDestSubnetMask_Type()
)
rsMLBDestSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBDestSubnetMask.setStatus("mandatory")
_RsMLBSubnetSrvrAddr_Type = IpAddress
_RsMLBSubnetSrvrAddr_Object = MibTableColumn
rsMLBSubnetSrvrAddr = _RsMLBSubnetSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1, 3),
    _RsMLBSubnetSrvrAddr_Type()
)
rsMLBSubnetSrvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBSubnetSrvrAddr.setStatus("mandatory")


class _RsMLBSubnetSrvrStatus_Type(Integer32):
    """Custom type rsMLBSubnetSrvrStatus based on Integer32"""
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


_RsMLBSubnetSrvrStatus_Type.__name__ = "Integer32"
_RsMLBSubnetSrvrStatus_Object = MibTableColumn
rsMLBSubnetSrvrStatus = _RsMLBSubnetSrvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1, 4),
    _RsMLBSubnetSrvrStatus_Type()
)
rsMLBSubnetSrvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSubnetSrvrStatus.setStatus("mandatory")


class _RsMLBSubnetSrvrOperMode_Type(Integer32):
    """Custom type rsMLBSubnetSrvrOperMode based on Integer32"""
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


_RsMLBSubnetSrvrOperMode_Type.__name__ = "Integer32"
_RsMLBSubnetSrvrOperMode_Object = MibTableColumn
rsMLBSubnetSrvrOperMode = _RsMLBSubnetSrvrOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 1, 5),
    _RsMLBSubnetSrvrOperMode_Type()
)
rsMLBSubnetSrvrOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSubnetSrvrOperMode.setStatus("mandatory")
_RsMLBdummy8_Type = Integer32
_RsMLBdummy8_Object = MibScalar
rsMLBdummy8 = _RsMLBdummy8_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 23, 2),
    _RsMLBdummy8_Type()
)
rsMLBdummy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy8.setStatus("mandatory")
_RsMLBApplicationPortGroupTable_Object = MibTable
rsMLBApplicationPortGroupTable = _RsMLBApplicationPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24)
)
if mibBuilder.loadTexts:
    rsMLBApplicationPortGroupTable.setStatus("mandatory")
_RsMLBApplPortGroupEntry_Object = MibTableRow
rsMLBApplPortGroupEntry = _RsMLBApplPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 1)
)
rsMLBApplPortGroupEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBApplPort"),
    (0, "MLB-MIB", "rsMLBApplPortSrvrAddr"),
)
if mibBuilder.loadTexts:
    rsMLBApplPortGroupEntry.setStatus("mandatory")
_RsMLBApplPort_Type = Integer32
_RsMLBApplPort_Object = MibTableColumn
rsMLBApplPort = _RsMLBApplPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 1, 1),
    _RsMLBApplPort_Type()
)
rsMLBApplPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBApplPort.setStatus("mandatory")
_RsMLBApplPortSrvrAddr_Type = IpAddress
_RsMLBApplPortSrvrAddr_Object = MibTableColumn
rsMLBApplPortSrvrAddr = _RsMLBApplPortSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 1, 2),
    _RsMLBApplPortSrvrAddr_Type()
)
rsMLBApplPortSrvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBApplPortSrvrAddr.setStatus("mandatory")


class _RsMLBApplPortSrvrStatus_Type(Integer32):
    """Custom type rsMLBApplPortSrvrStatus based on Integer32"""
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


_RsMLBApplPortSrvrStatus_Type.__name__ = "Integer32"
_RsMLBApplPortSrvrStatus_Object = MibTableColumn
rsMLBApplPortSrvrStatus = _RsMLBApplPortSrvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 1, 3),
    _RsMLBApplPortSrvrStatus_Type()
)
rsMLBApplPortSrvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBApplPortSrvrStatus.setStatus("mandatory")


class _RsMLBApplPortSrvrOperMode_Type(Integer32):
    """Custom type rsMLBApplPortSrvrOperMode based on Integer32"""
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


_RsMLBApplPortSrvrOperMode_Type.__name__ = "Integer32"
_RsMLBApplPortSrvrOperMode_Object = MibTableColumn
rsMLBApplPortSrvrOperMode = _RsMLBApplPortSrvrOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 1, 4),
    _RsMLBApplPortSrvrOperMode_Type()
)
rsMLBApplPortSrvrOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBApplPortSrvrOperMode.setStatus("mandatory")
_RsMLBdummy9_Type = Integer32
_RsMLBdummy9_Object = MibScalar
rsMLBdummy9 = _RsMLBdummy9_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 24, 2),
    _RsMLBdummy9_Type()
)
rsMLBdummy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy9.setStatus("mandatory")
_RsMLBSrcSbntGroupTable_Object = MibTable
rsMLBSrcSbntGroupTable = _RsMLBSrcSbntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25)
)
if mibBuilder.loadTexts:
    rsMLBSrcSbntGroupTable.setStatus("mandatory")
_RsMLBSrcSbntGroupEntry_Object = MibTableRow
rsMLBSrcSbntGroupEntry = _RsMLBSrcSbntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1)
)
rsMLBSrcSbntGroupEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBSrcSbntAddr"),
    (0, "MLB-MIB", "rsMLBSrcSbntMask"),
    (0, "MLB-MIB", "rsMLBSrcSbntSrvrAddr"),
)
if mibBuilder.loadTexts:
    rsMLBSrcSbntGroupEntry.setStatus("mandatory")
_RsMLBSrcSbntAddr_Type = IpAddress
_RsMLBSrcSbntAddr_Object = MibTableColumn
rsMLBSrcSbntAddr = _RsMLBSrcSbntAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1, 1),
    _RsMLBSrcSbntAddr_Type()
)
rsMLBSrcSbntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBSrcSbntAddr.setStatus("mandatory")
_RsMLBSrcSbntMask_Type = IpAddress
_RsMLBSrcSbntMask_Object = MibTableColumn
rsMLBSrcSbntMask = _RsMLBSrcSbntMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1, 2),
    _RsMLBSrcSbntMask_Type()
)
rsMLBSrcSbntMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBSrcSbntMask.setStatus("mandatory")
_RsMLBSrcSbntSrvrAddr_Type = IpAddress
_RsMLBSrcSbntSrvrAddr_Object = MibTableColumn
rsMLBSrcSbntSrvrAddr = _RsMLBSrcSbntSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1, 3),
    _RsMLBSrcSbntSrvrAddr_Type()
)
rsMLBSrcSbntSrvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBSrcSbntSrvrAddr.setStatus("mandatory")


class _RsMLBSrcSbntSrvrStatus_Type(Integer32):
    """Custom type rsMLBSrcSbntSrvrStatus based on Integer32"""
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


_RsMLBSrcSbntSrvrStatus_Type.__name__ = "Integer32"
_RsMLBSrcSbntSrvrStatus_Object = MibTableColumn
rsMLBSrcSbntSrvrStatus = _RsMLBSrcSbntSrvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1, 4),
    _RsMLBSrcSbntSrvrStatus_Type()
)
rsMLBSrcSbntSrvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSrcSbntSrvrStatus.setStatus("mandatory")


class _RsMLBSrcSbntSrvrOperMode_Type(Integer32):
    """Custom type rsMLBSrcSbntSrvrOperMode based on Integer32"""
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


_RsMLBSrcSbntSrvrOperMode_Type.__name__ = "Integer32"
_RsMLBSrcSbntSrvrOperMode_Object = MibTableColumn
rsMLBSrcSbntSrvrOperMode = _RsMLBSrcSbntSrvrOperMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 1, 5),
    _RsMLBSrcSbntSrvrOperMode_Type()
)
rsMLBSrcSbntSrvrOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSrcSbntSrvrOperMode.setStatus("mandatory")
_RsMLBdummy10_Type = Integer32
_RsMLBdummy10_Object = MibScalar
rsMLBdummy10 = _RsMLBdummy10_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 25, 2),
    _RsMLBdummy10_Type()
)
rsMLBdummy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy10.setStatus("mandatory")
_RsMLBNatTable_Object = MibTable
rsMLBNatTable = _RsMLBNatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26)
)
if mibBuilder.loadTexts:
    rsMLBNatTable.setStatus("mandatory")
_RsMLBNatEntry_Object = MibTableRow
rsMLBNatEntry = _RsMLBNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 1)
)
rsMLBNatEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBNatRouterAddress"),
    (0, "MLB-MIB", "rsMLBNatAddress"),
)
if mibBuilder.loadTexts:
    rsMLBNatEntry.setStatus("mandatory")
_RsMLBNatRouterAddress_Type = IpAddress
_RsMLBNatRouterAddress_Object = MibTableColumn
rsMLBNatRouterAddress = _RsMLBNatRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 1, 1),
    _RsMLBNatRouterAddress_Type()
)
rsMLBNatRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBNatRouterAddress.setStatus("mandatory")
_RsMLBNatAddress_Type = IpAddress
_RsMLBNatAddress_Object = MibTableColumn
rsMLBNatAddress = _RsMLBNatAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 1, 2),
    _RsMLBNatAddress_Type()
)
rsMLBNatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBNatAddress.setStatus("mandatory")


class _RsMLBNatStatus_Type(Integer32):
    """Custom type rsMLBNatStatus based on Integer32"""
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


_RsMLBNatStatus_Type.__name__ = "Integer32"
_RsMLBNatStatus_Object = MibTableColumn
rsMLBNatStatus = _RsMLBNatStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 1, 3),
    _RsMLBNatStatus_Type()
)
rsMLBNatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBNatStatus.setStatus("mandatory")


class _RsMLBNatMode_Type(Integer32):
    """Custom type rsMLBNatMode based on Integer32"""
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


_RsMLBNatMode_Type.__name__ = "Integer32"
_RsMLBNatMode_Object = MibTableColumn
rsMLBNatMode = _RsMLBNatMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 1, 4),
    _RsMLBNatMode_Type()
)
rsMLBNatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBNatMode.setStatus("mandatory")
_RsMLBdummy11_Type = Integer32
_RsMLBdummy11_Object = MibScalar
rsMLBdummy11 = _RsMLBdummy11_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 26, 2),
    _RsMLBdummy11_Type()
)
rsMLBdummy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy11.setStatus("mandatory")


class _RsMLBFpNatStatus_Type(Integer32):
    """Custom type rsMLBFpNatStatus based on Integer32"""
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


_RsMLBFpNatStatus_Type.__name__ = "Integer32"
_RsMLBFpNatStatus_Object = MibScalar
rsMLBFpNatStatus = _RsMLBFpNatStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 27),
    _RsMLBFpNatStatus_Type()
)
rsMLBFpNatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBFpNatStatus.setStatus("mandatory")
_RsMLBStaticNatTable_Object = MibTable
rsMLBStaticNatTable = _RsMLBStaticNatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28)
)
if mibBuilder.loadTexts:
    rsMLBStaticNatTable.setStatus("mandatory")
_RsMLBStaticNatEntry_Object = MibTableRow
rsMLBStaticNatEntry = _RsMLBStaticNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1)
)
rsMLBStaticNatEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBStaticNatLclServerAddress"),
    (0, "MLB-MIB", "rsMLBStaticNatRouterAddress"),
)
if mibBuilder.loadTexts:
    rsMLBStaticNatEntry.setStatus("mandatory")
_RsMLBStaticNatLclServerAddress_Type = IpAddress
_RsMLBStaticNatLclServerAddress_Object = MibTableColumn
rsMLBStaticNatLclServerAddress = _RsMLBStaticNatLclServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1, 1),
    _RsMLBStaticNatLclServerAddress_Type()
)
rsMLBStaticNatLclServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBStaticNatLclServerAddress.setStatus("mandatory")
_RsMLBStaticNatRouterAddress_Type = IpAddress
_RsMLBStaticNatRouterAddress_Object = MibTableColumn
rsMLBStaticNatRouterAddress = _RsMLBStaticNatRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1, 2),
    _RsMLBStaticNatRouterAddress_Type()
)
rsMLBStaticNatRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBStaticNatRouterAddress.setStatus("mandatory")
_RsMLBStaticNatAddress_Type = IpAddress
_RsMLBStaticNatAddress_Object = MibTableColumn
rsMLBStaticNatAddress = _RsMLBStaticNatAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1, 3),
    _RsMLBStaticNatAddress_Type()
)
rsMLBStaticNatAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticNatAddress.setStatus("mandatory")


class _RsMLBStaticNatStatus_Type(Integer32):
    """Custom type rsMLBStaticNatStatus based on Integer32"""
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


_RsMLBStaticNatStatus_Type.__name__ = "Integer32"
_RsMLBStaticNatStatus_Object = MibTableColumn
rsMLBStaticNatStatus = _RsMLBStaticNatStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1, 4),
    _RsMLBStaticNatStatus_Type()
)
rsMLBStaticNatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticNatStatus.setStatus("mandatory")


class _RsMLBStaticNatMode_Type(Integer32):
    """Custom type rsMLBStaticNatMode based on Integer32"""
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


_RsMLBStaticNatMode_Type.__name__ = "Integer32"
_RsMLBStaticNatMode_Object = MibTableColumn
rsMLBStaticNatMode = _RsMLBStaticNatMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 1, 5),
    _RsMLBStaticNatMode_Type()
)
rsMLBStaticNatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticNatMode.setStatus("mandatory")
_RsMLBdummy12_Type = Integer32
_RsMLBdummy12_Object = MibScalar
rsMLBdummy12 = _RsMLBdummy12_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 28, 2),
    _RsMLBdummy12_Type()
)
rsMLBdummy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy12.setStatus("mandatory")
_RsMLBProximity_ObjectIdentity = ObjectIdentity
rsMLBProximity = _RsMLBProximity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29)
)
_RsMLBStaticProximityTable_Object = MibTable
rsMLBStaticProximityTable = _RsMLBStaticProximityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1)
)
if mibBuilder.loadTexts:
    rsMLBStaticProximityTable.setStatus("mandatory")
_RsMLBStaticProximityEntry_Object = MibTableRow
rsMLBStaticProximityEntry = _RsMLBStaticProximityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1)
)
rsMLBStaticProximityEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBStaticProximityRangeFrom"),
)
if mibBuilder.loadTexts:
    rsMLBStaticProximityEntry.setStatus("mandatory")
_RsMLBStaticProximityRangeFrom_Type = IpAddress
_RsMLBStaticProximityRangeFrom_Object = MibTableColumn
rsMLBStaticProximityRangeFrom = _RsMLBStaticProximityRangeFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 1),
    _RsMLBStaticProximityRangeFrom_Type()
)
rsMLBStaticProximityRangeFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBStaticProximityRangeFrom.setStatus("mandatory")
_RsMLBStaticProximityRangeTo_Type = IpAddress
_RsMLBStaticProximityRangeTo_Object = MibTableColumn
rsMLBStaticProximityRangeTo = _RsMLBStaticProximityRangeTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 2),
    _RsMLBStaticProximityRangeTo_Type()
)
rsMLBStaticProximityRangeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticProximityRangeTo.setStatus("mandatory")


class _RsMLBStaticProximityStatus_Type(Integer32):
    """Custom type rsMLBStaticProximityStatus based on Integer32"""
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


_RsMLBStaticProximityStatus_Type.__name__ = "Integer32"
_RsMLBStaticProximityStatus_Object = MibTableColumn
rsMLBStaticProximityStatus = _RsMLBStaticProximityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 3),
    _RsMLBStaticProximityStatus_Type()
)
rsMLBStaticProximityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticProximityStatus.setStatus("mandatory")
_RsMLBStaticProximityServer1_Type = IpAddress
_RsMLBStaticProximityServer1_Object = MibTableColumn
rsMLBStaticProximityServer1 = _RsMLBStaticProximityServer1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 4),
    _RsMLBStaticProximityServer1_Type()
)
rsMLBStaticProximityServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticProximityServer1.setStatus("mandatory")
_RsMLBStaticProximityServer2_Type = IpAddress
_RsMLBStaticProximityServer2_Object = MibTableColumn
rsMLBStaticProximityServer2 = _RsMLBStaticProximityServer2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 5),
    _RsMLBStaticProximityServer2_Type()
)
rsMLBStaticProximityServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticProximityServer2.setStatus("mandatory")
_RsMLBStaticProximityServer3_Type = IpAddress
_RsMLBStaticProximityServer3_Object = MibTableColumn
rsMLBStaticProximityServer3 = _RsMLBStaticProximityServer3_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 1, 1, 6),
    _RsMLBStaticProximityServer3_Type()
)
rsMLBStaticProximityServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBStaticProximityServer3.setStatus("mandatory")


class _RsMLBProximityOperationMode_Type(Integer32):
    """Custom type rsMLBProximityOperationMode based on Integer32"""
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
        *(("fullProximityBoth", 5),
          ("fullProximityInbound", 3),
          ("fullProximityOutbound", 4),
          ("noProximity", 1),
          ("staticProximity", 2))
    )


_RsMLBProximityOperationMode_Type.__name__ = "Integer32"
_RsMLBProximityOperationMode_Object = MibScalar
rsMLBProximityOperationMode = _RsMLBProximityOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 2),
    _RsMLBProximityOperationMode_Type()
)
rsMLBProximityOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityOperationMode.setStatus("mandatory")
_RsMLBProximityMainDNS_Type = IpAddress
_RsMLBProximityMainDNS_Object = MibScalar
rsMLBProximityMainDNS = _RsMLBProximityMainDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 3),
    _RsMLBProximityMainDNS_Type()
)
rsMLBProximityMainDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityMainDNS.setStatus("mandatory")
_RsMLBProximityBackupDNS_Type = IpAddress
_RsMLBProximityBackupDNS_Object = MibScalar
rsMLBProximityBackupDNS = _RsMLBProximityBackupDNS_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 4),
    _RsMLBProximityBackupDNS_Type()
)
rsMLBProximityBackupDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityBackupDNS.setStatus("mandatory")
_RsMLBProximityAgingPeriod_Type = Integer32
_RsMLBProximityAgingPeriod_Object = MibScalar
rsMLBProximityAgingPeriod = _RsMLBProximityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 5),
    _RsMLBProximityAgingPeriod_Type()
)
rsMLBProximityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityAgingPeriod.setStatus("mandatory")


class _RsMLBProximityRetries_Type(Integer32):
    """Custom type rsMLBProximityRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RsMLBProximityRetries_Type.__name__ = "Integer32"
_RsMLBProximityRetries_Object = MibScalar
rsMLBProximityRetries = _RsMLBProximityRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 6),
    _RsMLBProximityRetries_Type()
)
rsMLBProximityRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityRetries.setStatus("mandatory")


class _RsMLBProximityTimeout_Type(Integer32):
    """Custom type rsMLBProximityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsMLBProximityTimeout_Type.__name__ = "Integer32"
_RsMLBProximityTimeout_Object = MibScalar
rsMLBProximityTimeout = _RsMLBProximityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 7),
    _RsMLBProximityTimeout_Type()
)
rsMLBProximityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityTimeout.setStatus("mandatory")
_RsMLBProximityTuning_ObjectIdentity = ObjectIdentity
rsMLBProximityTuning = _RsMLBProximityTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 8)
)
_RsMLBMaxDynEntries_Type = Integer32
_RsMLBMaxDynEntries_Object = MibScalar
rsMLBMaxDynEntries = _RsMLBMaxDynEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 8, 1),
    _RsMLBMaxDynEntries_Type()
)
rsMLBMaxDynEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBMaxDynEntries.setStatus("mandatory")
_RsMLBMaxDynEntriesAfterReset_Type = Integer32
_RsMLBMaxDynEntriesAfterReset_Object = MibScalar
rsMLBMaxDynEntriesAfterReset = _RsMLBMaxDynEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 8, 2),
    _RsMLBMaxDynEntriesAfterReset_Type()
)
rsMLBMaxDynEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBMaxDynEntriesAfterReset.setStatus("mandatory")


class _RsMLBProximityHopsWeight_Type(Integer32):
    """Custom type rsMLBProximityHopsWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsMLBProximityHopsWeight_Type.__name__ = "Integer32"
_RsMLBProximityHopsWeight_Object = MibScalar
rsMLBProximityHopsWeight = _RsMLBProximityHopsWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 9),
    _RsMLBProximityHopsWeight_Type()
)
rsMLBProximityHopsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityHopsWeight.setStatus("mandatory")


class _RsMLBProximityLatencyWeight_Type(Integer32):
    """Custom type rsMLBProximityLatencyWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsMLBProximityLatencyWeight_Type.__name__ = "Integer32"
_RsMLBProximityLatencyWeight_Object = MibScalar
rsMLBProximityLatencyWeight = _RsMLBProximityLatencyWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 10),
    _RsMLBProximityLatencyWeight_Type()
)
rsMLBProximityLatencyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityLatencyWeight.setStatus("mandatory")


class _RsMLBProximityLoadWeight_Type(Integer32):
    """Custom type rsMLBProximityLoadWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsMLBProximityLoadWeight_Type.__name__ = "Integer32"
_RsMLBProximityLoadWeight_Object = MibScalar
rsMLBProximityLoadWeight = _RsMLBProximityLoadWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 11),
    _RsMLBProximityLoadWeight_Type()
)
rsMLBProximityLoadWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBProximityLoadWeight.setStatus("mandatory")
_RsMLBPrxyCheckFPIPTable_Object = MibTable
rsMLBPrxyCheckFPIPTable = _RsMLBPrxyCheckFPIPTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12)
)
if mibBuilder.loadTexts:
    rsMLBPrxyCheckFPIPTable.setStatus("mandatory")
_RsMLBPrxyCheckFPIPEntry_Object = MibTableRow
rsMLBPrxyCheckFPIPEntry = _RsMLBPrxyCheckFPIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12, 1)
)
rsMLBPrxyCheckFPIPEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBRouterAddr"),
)
if mibBuilder.loadTexts:
    rsMLBPrxyCheckFPIPEntry.setStatus("mandatory")
_RsMLBRouterAddr_Type = IpAddress
_RsMLBRouterAddr_Object = MibTableColumn
rsMLBRouterAddr = _RsMLBRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12, 1, 1),
    _RsMLBRouterAddr_Type()
)
rsMLBRouterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBRouterAddr.setStatus("mandatory")
_RsMLBFPIPAddr_Type = IpAddress
_RsMLBFPIPAddr_Object = MibTableColumn
rsMLBFPIPAddr = _RsMLBFPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12, 1, 2),
    _RsMLBFPIPAddr_Type()
)
rsMLBFPIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBFPIPAddr.setStatus("mandatory")


class _RsMLBPrxyCheckFPIPStatus_Type(Integer32):
    """Custom type rsMLBPrxyCheckFPIPStatus based on Integer32"""
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


_RsMLBPrxyCheckFPIPStatus_Type.__name__ = "Integer32"
_RsMLBPrxyCheckFPIPStatus_Object = MibTableColumn
rsMLBPrxyCheckFPIPStatus = _RsMLBPrxyCheckFPIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12, 1, 4),
    _RsMLBPrxyCheckFPIPStatus_Type()
)
rsMLBPrxyCheckFPIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBPrxyCheckFPIPStatus.setStatus("mandatory")
_RsMLBdummy15_Type = Integer32
_RsMLBdummy15_Object = MibScalar
rsMLBdummy15 = _RsMLBdummy15_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 29, 12, 2),
    _RsMLBdummy15_Type()
)
rsMLBdummy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy15.setStatus("mandatory")
_RsMLBDNS_ObjectIdentity = ObjectIdentity
rsMLBDNS = _RsMLBDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30)
)
_RsMLBDNSURLtoIPTable_Object = MibTable
rsMLBDNSURLtoIPTable = _RsMLBDNSURLtoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1)
)
if mibBuilder.loadTexts:
    rsMLBDNSURLtoIPTable.setStatus("mandatory")
_RsMLBURLtoIPEntry_Object = MibTableRow
rsMLBURLtoIPEntry = _RsMLBURLtoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1, 1)
)
rsMLBURLtoIPEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBURL"),
)
if mibBuilder.loadTexts:
    rsMLBURLtoIPEntry.setStatus("mandatory")


class _RsMLBURL_Type(DisplayString):
    """Custom type rsMLBURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_RsMLBURL_Type.__name__ = "DisplayString"
_RsMLBURL_Object = MibTableColumn
rsMLBURL = _RsMLBURL_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1, 1, 1),
    _RsMLBURL_Type()
)
rsMLBURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBURL.setStatus("mandatory")
_RsMLBURLLocDeviceIP_Type = IpAddress
_RsMLBURLLocDeviceIP_Object = MibTableColumn
rsMLBURLLocDeviceIP = _RsMLBURLLocDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1, 1, 2),
    _RsMLBURLLocDeviceIP_Type()
)
rsMLBURLLocDeviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBURLLocDeviceIP.setStatus("mandatory")


class _RsMLBURLStatus_Type(Integer32):
    """Custom type rsMLBURLStatus based on Integer32"""
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


_RsMLBURLStatus_Type.__name__ = "Integer32"
_RsMLBURLStatus_Object = MibTableColumn
rsMLBURLStatus = _RsMLBURLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1, 1, 3),
    _RsMLBURLStatus_Type()
)
rsMLBURLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBURLStatus.setStatus("mandatory")
_RsMLBdummy13_Type = Integer32
_RsMLBdummy13_Object = MibScalar
rsMLBdummy13 = _RsMLBdummy13_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 1, 2),
    _RsMLBdummy13_Type()
)
rsMLBdummy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy13.setStatus("mandatory")
_RsMLBDNSttl_Type = Integer32
_RsMLBDNSttl_Object = MibScalar
rsMLBDNSttl = _RsMLBDNSttl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 2),
    _RsMLBDNSttl_Type()
)
rsMLBDNSttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDNSttl.setStatus("mandatory")


class _RsMLBDNSTwoAnswers_Type(Integer32):
    """Custom type rsMLBDNSTwoAnswers based on Integer32"""
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


_RsMLBDNSTwoAnswers_Type.__name__ = "Integer32"
_RsMLBDNSTwoAnswers_Object = MibScalar
rsMLBDNSTwoAnswers = _RsMLBDNSTwoAnswers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 3),
    _RsMLBDNSTwoAnswers_Type()
)
rsMLBDNSTwoAnswers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDNSTwoAnswers.setStatus("mandatory")
_RsMLBDNSVirtualTable_Object = MibTable
rsMLBDNSVirtualTable = _RsMLBDNSVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4)
)
if mibBuilder.loadTexts:
    rsMLBDNSVirtualTable.setStatus("mandatory")
_RsMLBDNSVirtualEntry_Object = MibTableRow
rsMLBDNSVirtualEntry = _RsMLBDNSVirtualEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4, 1)
)
rsMLBDNSVirtualEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBDNSVirtualIP"),
)
if mibBuilder.loadTexts:
    rsMLBDNSVirtualEntry.setStatus("mandatory")
_RsMLBDNSVirtualIP_Type = IpAddress
_RsMLBDNSVirtualIP_Object = MibTableColumn
rsMLBDNSVirtualIP = _RsMLBDNSVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4, 1, 1),
    _RsMLBDNSVirtualIP_Type()
)
rsMLBDNSVirtualIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBDNSVirtualIP.setStatus("mandatory")


class _RsMLBDNSVirIPMode_Type(Integer32):
    """Custom type rsMLBDNSVirIPMode based on Integer32"""
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


_RsMLBDNSVirIPMode_Type.__name__ = "Integer32"
_RsMLBDNSVirIPMode_Object = MibTableColumn
rsMLBDNSVirIPMode = _RsMLBDNSVirIPMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4, 1, 2),
    _RsMLBDNSVirIPMode_Type()
)
rsMLBDNSVirIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDNSVirIPMode.setStatus("mandatory")


class _RsMLBDNSStatus_Type(Integer32):
    """Custom type rsMLBDNSStatus based on Integer32"""
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


_RsMLBDNSStatus_Type.__name__ = "Integer32"
_RsMLBDNSStatus_Object = MibTableColumn
rsMLBDNSStatus = _RsMLBDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4, 1, 3),
    _RsMLBDNSStatus_Type()
)
rsMLBDNSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBDNSStatus.setStatus("mandatory")
_RsMLBdummy14_Type = Integer32
_RsMLBdummy14_Object = MibScalar
rsMLBdummy14 = _RsMLBdummy14_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 30, 4, 2),
    _RsMLBdummy14_Type()
)
rsMLBdummy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy14.setStatus("mandatory")


class _RsMLBSrcPortInClientHash_Type(Integer32):
    """Custom type rsMLBSrcPortInClientHash based on Integer32"""
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


_RsMLBSrcPortInClientHash_Type.__name__ = "Integer32"
_RsMLBSrcPortInClientHash_Object = MibScalar
rsMLBSrcPortInClientHash = _RsMLBSrcPortInClientHash_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 31),
    _RsMLBSrcPortInClientHash_Type()
)
rsMLBSrcPortInClientHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBSrcPortInClientHash.setStatus("mandatory")
_RsMLBAgingTimeTable_Object = MibTable
rsMLBAgingTimeTable = _RsMLBAgingTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32)
)
if mibBuilder.loadTexts:
    rsMLBAgingTimeTable.setStatus("mandatory")
_RsMLBAgingTimeEntry_Object = MibTableRow
rsMLBAgingTimeEntry = _RsMLBAgingTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32, 1)
)
rsMLBAgingTimeEntry.setIndexNames(
    (0, "MLB-MIB", "rsMLBAgingTimeApplPort"),
)
if mibBuilder.loadTexts:
    rsMLBAgingTimeEntry.setStatus("mandatory")
_RsMLBAgingTimeApplPort_Type = Integer32
_RsMLBAgingTimeApplPort_Object = MibTableColumn
rsMLBAgingTimeApplPort = _RsMLBAgingTimeApplPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32, 1, 1),
    _RsMLBAgingTimeApplPort_Type()
)
rsMLBAgingTimeApplPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBAgingTimeApplPort.setStatus("mandatory")


class _RsMLBAgingTime_Type(Integer32):
    """Custom type rsMLBAgingTime based on Integer32"""
    defaultValue = 60


_RsMLBAgingTime_Object = MibTableColumn
rsMLBAgingTime = _RsMLBAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32, 1, 2),
    _RsMLBAgingTime_Type()
)
rsMLBAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBAgingTime.setStatus("mandatory")


class _RsMLBAgingTimeStatus_Type(Integer32):
    """Custom type rsMLBAgingTimeStatus based on Integer32"""
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


_RsMLBAgingTimeStatus_Type.__name__ = "Integer32"
_RsMLBAgingTimeStatus_Object = MibTableColumn
rsMLBAgingTimeStatus = _RsMLBAgingTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32, 1, 3),
    _RsMLBAgingTimeStatus_Type()
)
rsMLBAgingTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMLBAgingTimeStatus.setStatus("mandatory")
_RsMLBdummy16_Type = Integer32
_RsMLBdummy16_Object = MibScalar
rsMLBdummy16 = _RsMLBdummy16_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38, 32, 2),
    _RsMLBdummy16_Type()
)
rsMLBdummy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMLBdummy16.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MLB-MIB",
    **{"rsMLBApplicationServersTable": rsMLBApplicationServersTable,
       "rsMLBApplicationServerEntry": rsMLBApplicationServerEntry,
       "rsMLBServerAddr": rsMLBServerAddr,
       "rsMLBServerName": rsMLBServerName,
       "rsMLBServerOperStatus": rsMLBServerOperStatus,
       "rsMLBServerWeight": rsMLBServerWeight,
       "rsMLBServerAttachedUsersNumber": rsMLBServerAttachedUsersNumber,
       "rsMLBServerPeakLoad": rsMLBServerPeakLoad,
       "rsMLBServerFramesRate": rsMLBServerFramesRate,
       "rsMLBServerFramesLoad": rsMLBServerFramesLoad,
       "rsMLBServerStatus": rsMLBServerStatus,
       "rsMLBServerOperMode": rsMLBServerOperMode,
       "rsMLBServerConnectionLimit": rsMLBServerConnectionLimit,
       "rsMLBServerAdminStatus": rsMLBServerAdminStatus,
       "rsMLBServerType": rsMLBServerType,
       "rsMLBServerMacStatus": rsMLBServerMacStatus,
       "rsMLBServerPortNumber": rsMLBServerPortNumber,
       "rsMLBServerPeakBytesLoad": rsMLBServerPeakBytesLoad,
       "rsMLBServerBytesRate": rsMLBServerBytesRate,
       "rsMLBServerBytesLoad": rsMLBServerBytesLoad,
       "rsMLBServerRecoveryTime": rsMLBServerRecoveryTime,
       "rsMLBServerWarmUpTime": rsMLBServerWarmUpTime,
       "rsMLBServerTotalFramesLoad": rsMLBServerTotalFramesLoad,
       "rsMLBServerProximityCheck": rsMLBServerProximityCheck,
       "rsMLBdummy1": rsMLBdummy1,
       "rsMLBAdminStatus": rsMLBAdminStatus,
       "rsMLBClientsLifeTime": rsMLBClientsLifeTime,
       "rsMLBDispatchMethod": rsMLBDispatchMethod,
       "rsMLBCheckConnectivityStatus": rsMLBCheckConnectivityStatus,
       "rsMLBCheckConnectivityMethod": rsMLBCheckConnectivityMethod,
       "rsMLBCheckConnectivityInterval": rsMLBCheckConnectivityInterval,
       "rsMLBCheckConnectivityRetries": rsMLBCheckConnectivityRetries,
       "rsMLBClientsConnectDenials": rsMLBClientsConnectDenials,
       "rsMLBClientsTable": rsMLBClientsTable,
       "rsMLBClientEntry": rsMLBClientEntry,
       "rsMLBClientAddr": rsMLBClientAddr,
       "rsMLBDestinationAddr": rsMLBDestinationAddr,
       "rsMLBAttachedServerAddr": rsMLBAttachedServerAddr,
       "rsMLBClientLastActivityTime": rsMLBClientLastActivityTime,
       "rsMLBClientAttachmentTime": rsMLBClientAttachmentTime,
       "rsMLBClientStatus": rsMLBClientStatus,
       "rsMLBdummy2": rsMLBdummy2,
       "rsMLBSessionTracking": rsMLBSessionTracking,
       "rsMLBRemoteConnectivityTable": rsMLBRemoteConnectivityTable,
       "rsMLBRemoteConnectivityEntry": rsMLBRemoteConnectivityEntry,
       "rsMLBRmtConSrvrAddr": rsMLBRmtConSrvrAddr,
       "rsMLBRmtConIpAddr": rsMLBRmtConIpAddr,
       "rsMLBRmtConStatus": rsMLBRmtConStatus,
       "rsMLBRmtConOperStatus": rsMLBRmtConOperStatus,
       "rsMLBdummy3": rsMLBdummy3,
       "rsMLBClientTableMode": rsMLBClientTableMode,
       "rsMLBRulesTable": rsMLBRulesTable,
       "rsMLBRulesEntry": rsMLBRulesEntry,
       "rsMLBRulesPortNumber": rsMLBRulesPortNumber,
       "rsMLBRulesLeavingPort": rsMLBRulesLeavingPort,
       "rsMLBRulesNumOfServers": rsMLBRulesNumOfServers,
       "rsMLBdummy4": rsMLBdummy4,
       "rsMLBTranslateOutBoundMode": rsMLBTranslateOutBoundMode,
       "rsMLBVirtualIPTable": rsMLBVirtualIPTable,
       "rsMLBVirtualIPEntry": rsMLBVirtualIPEntry,
       "rsMLBVirtualIPAddress": rsMLBVirtualIPAddress,
       "rsMLBVirtualMode": rsMLBVirtualMode,
       "rsMLBVirtualStatus": rsMLBVirtualStatus,
       "rsMLBdummy5": rsMLBdummy5,
       "rsMLBMappedIPTable": rsMLBMappedIPTable,
       "rsMLBMappedIPEntry": rsMLBMappedIPEntry,
       "rsMLBMappedVirtualAddress": rsMLBMappedVirtualAddress,
       "rsMLBMappedFirewallIP": rsMLBMappedFirewallIP,
       "rsMLBMappedFirewallNAT": rsMLBMappedFirewallNAT,
       "rsMLBMappedStatus": rsMLBMappedStatus,
       "rsMLBdummy6": rsMLBdummy6,
       "rsMLBVirtualConnectivityIP": rsMLBVirtualConnectivityIP,
       "rsMLBVirtualConnectivityMode": rsMLBVirtualConnectivityMode,
       "rsMLBRemoveEntryAtSessionEnd": rsMLBRemoveEntryAtSessionEnd,
       "rsMLBFirewallPortID": rsMLBFirewallPortID,
       "rsMLBSubnetGroupTable": rsMLBSubnetGroupTable,
       "rsMLBSubnetGroupEntry": rsMLBSubnetGroupEntry,
       "rsMLBDestSubnetAddr": rsMLBDestSubnetAddr,
       "rsMLBDestSubnetMask": rsMLBDestSubnetMask,
       "rsMLBSubnetSrvrAddr": rsMLBSubnetSrvrAddr,
       "rsMLBSubnetSrvrStatus": rsMLBSubnetSrvrStatus,
       "rsMLBSubnetSrvrOperMode": rsMLBSubnetSrvrOperMode,
       "rsMLBdummy8": rsMLBdummy8,
       "rsMLBApplicationPortGroupTable": rsMLBApplicationPortGroupTable,
       "rsMLBApplPortGroupEntry": rsMLBApplPortGroupEntry,
       "rsMLBApplPort": rsMLBApplPort,
       "rsMLBApplPortSrvrAddr": rsMLBApplPortSrvrAddr,
       "rsMLBApplPortSrvrStatus": rsMLBApplPortSrvrStatus,
       "rsMLBApplPortSrvrOperMode": rsMLBApplPortSrvrOperMode,
       "rsMLBdummy9": rsMLBdummy9,
       "rsMLBSrcSbntGroupTable": rsMLBSrcSbntGroupTable,
       "rsMLBSrcSbntGroupEntry": rsMLBSrcSbntGroupEntry,
       "rsMLBSrcSbntAddr": rsMLBSrcSbntAddr,
       "rsMLBSrcSbntMask": rsMLBSrcSbntMask,
       "rsMLBSrcSbntSrvrAddr": rsMLBSrcSbntSrvrAddr,
       "rsMLBSrcSbntSrvrStatus": rsMLBSrcSbntSrvrStatus,
       "rsMLBSrcSbntSrvrOperMode": rsMLBSrcSbntSrvrOperMode,
       "rsMLBdummy10": rsMLBdummy10,
       "rsMLBNatTable": rsMLBNatTable,
       "rsMLBNatEntry": rsMLBNatEntry,
       "rsMLBNatRouterAddress": rsMLBNatRouterAddress,
       "rsMLBNatAddress": rsMLBNatAddress,
       "rsMLBNatStatus": rsMLBNatStatus,
       "rsMLBNatMode": rsMLBNatMode,
       "rsMLBdummy11": rsMLBdummy11,
       "rsMLBFpNatStatus": rsMLBFpNatStatus,
       "rsMLBStaticNatTable": rsMLBStaticNatTable,
       "rsMLBStaticNatEntry": rsMLBStaticNatEntry,
       "rsMLBStaticNatLclServerAddress": rsMLBStaticNatLclServerAddress,
       "rsMLBStaticNatRouterAddress": rsMLBStaticNatRouterAddress,
       "rsMLBStaticNatAddress": rsMLBStaticNatAddress,
       "rsMLBStaticNatStatus": rsMLBStaticNatStatus,
       "rsMLBStaticNatMode": rsMLBStaticNatMode,
       "rsMLBdummy12": rsMLBdummy12,
       "rsMLBProximity": rsMLBProximity,
       "rsMLBStaticProximityTable": rsMLBStaticProximityTable,
       "rsMLBStaticProximityEntry": rsMLBStaticProximityEntry,
       "rsMLBStaticProximityRangeFrom": rsMLBStaticProximityRangeFrom,
       "rsMLBStaticProximityRangeTo": rsMLBStaticProximityRangeTo,
       "rsMLBStaticProximityStatus": rsMLBStaticProximityStatus,
       "rsMLBStaticProximityServer1": rsMLBStaticProximityServer1,
       "rsMLBStaticProximityServer2": rsMLBStaticProximityServer2,
       "rsMLBStaticProximityServer3": rsMLBStaticProximityServer3,
       "rsMLBProximityOperationMode": rsMLBProximityOperationMode,
       "rsMLBProximityMainDNS": rsMLBProximityMainDNS,
       "rsMLBProximityBackupDNS": rsMLBProximityBackupDNS,
       "rsMLBProximityAgingPeriod": rsMLBProximityAgingPeriod,
       "rsMLBProximityRetries": rsMLBProximityRetries,
       "rsMLBProximityTimeout": rsMLBProximityTimeout,
       "rsMLBProximityTuning": rsMLBProximityTuning,
       "rsMLBMaxDynEntries": rsMLBMaxDynEntries,
       "rsMLBMaxDynEntriesAfterReset": rsMLBMaxDynEntriesAfterReset,
       "rsMLBProximityHopsWeight": rsMLBProximityHopsWeight,
       "rsMLBProximityLatencyWeight": rsMLBProximityLatencyWeight,
       "rsMLBProximityLoadWeight": rsMLBProximityLoadWeight,
       "rsMLBPrxyCheckFPIPTable": rsMLBPrxyCheckFPIPTable,
       "rsMLBPrxyCheckFPIPEntry": rsMLBPrxyCheckFPIPEntry,
       "rsMLBRouterAddr": rsMLBRouterAddr,
       "rsMLBFPIPAddr": rsMLBFPIPAddr,
       "rsMLBPrxyCheckFPIPStatus": rsMLBPrxyCheckFPIPStatus,
       "rsMLBdummy15": rsMLBdummy15,
       "rsMLBDNS": rsMLBDNS,
       "rsMLBDNSURLtoIPTable": rsMLBDNSURLtoIPTable,
       "rsMLBURLtoIPEntry": rsMLBURLtoIPEntry,
       "rsMLBURL": rsMLBURL,
       "rsMLBURLLocDeviceIP": rsMLBURLLocDeviceIP,
       "rsMLBURLStatus": rsMLBURLStatus,
       "rsMLBdummy13": rsMLBdummy13,
       "rsMLBDNSttl": rsMLBDNSttl,
       "rsMLBDNSTwoAnswers": rsMLBDNSTwoAnswers,
       "rsMLBDNSVirtualTable": rsMLBDNSVirtualTable,
       "rsMLBDNSVirtualEntry": rsMLBDNSVirtualEntry,
       "rsMLBDNSVirtualIP": rsMLBDNSVirtualIP,
       "rsMLBDNSVirIPMode": rsMLBDNSVirIPMode,
       "rsMLBDNSStatus": rsMLBDNSStatus,
       "rsMLBdummy14": rsMLBdummy14,
       "rsMLBSrcPortInClientHash": rsMLBSrcPortInClientHash,
       "rsMLBAgingTimeTable": rsMLBAgingTimeTable,
       "rsMLBAgingTimeEntry": rsMLBAgingTimeEntry,
       "rsMLBAgingTimeApplPort": rsMLBAgingTimeApplPort,
       "rsMLBAgingTime": rsMLBAgingTime,
       "rsMLBAgingTimeStatus": rsMLBAgingTimeStatus,
       "rsMLBdummy16": rsMLBdummy16}
)
