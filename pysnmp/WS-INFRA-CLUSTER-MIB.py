# SNMP MIB module (WS-INFRA-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:25 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wsInfraCluster,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraCluster")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsInfraClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1)
)
wsInfraClusterMIB.setRevisions(
        ("2008-08-08 09:46",
         "2008-06-17 17:13",
         "2008-04-29 10:13",
         "2007-06-26 13:26",
         "2007-06-26 12:15",
         "2006-05-24 13:58",
         "2005-12-27 14:05",
         "2005-12-16 12:29",
         "2005-09-12 20:39",
         "2005-08-17 13:25",
         "2005-08-15 16:27",
         "2005-08-15 14:20",
         "2005-08-11 18:53",
         "2005-07-07 18:36",
         "2005-07-07 16:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraClusterSwitchIP_Type = IpAddress
_WsInfraClusterSwitchIP_Object = MibScalar
wsInfraClusterSwitchIP = _WsInfraClusterSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 1),
    _WsInfraClusterSwitchIP_Type()
)
wsInfraClusterSwitchIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterSwitchIP.setStatus("current")


class _WsInfraClusterEnable_Type(Integer32):
    """Custom type wsInfraClusterEnable based on Integer32"""
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


_WsInfraClusterEnable_Type.__name__ = "Integer32"
_WsInfraClusterEnable_Object = MibScalar
wsInfraClusterEnable = _WsInfraClusterEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 2),
    _WsInfraClusterEnable_Type()
)
wsInfraClusterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterEnable.setStatus("current")


class _WsInfraClusterMode_Type(Integer32):
    """Custom type wsInfraClusterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_WsInfraClusterMode_Type.__name__ = "Integer32"
_WsInfraClusterMode_Object = MibScalar
wsInfraClusterMode = _WsInfraClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 3),
    _WsInfraClusterMode_Type()
)
wsInfraClusterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterMode.setStatus("current")


class _WsInfraClusterId_Type(Unsigned32):
    """Custom type wsInfraClusterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsInfraClusterId_Type.__name__ = "Unsigned32"
_WsInfraClusterId_Object = MibScalar
wsInfraClusterId = _WsInfraClusterId_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 4),
    _WsInfraClusterId_Type()
)
wsInfraClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterId.setStatus("current")


class _WsInfraClusterDiscoveryInterval_Type(Unsigned32):
    """Custom type wsInfraClusterDiscoveryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_WsInfraClusterDiscoveryInterval_Type.__name__ = "Unsigned32"
_WsInfraClusterDiscoveryInterval_Object = MibScalar
wsInfraClusterDiscoveryInterval = _WsInfraClusterDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 5),
    _WsInfraClusterDiscoveryInterval_Type()
)
wsInfraClusterDiscoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDiscoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraClusterDiscoveryInterval.setUnits("seconds")


class _WsInfraClusterHoldInterval_Type(Unsigned32):
    """Custom type wsInfraClusterHoldInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsInfraClusterHoldInterval_Type.__name__ = "Unsigned32"
_WsInfraClusterHoldInterval_Object = MibScalar
wsInfraClusterHoldInterval = _WsInfraClusterHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 6),
    _WsInfraClusterHoldInterval_Type()
)
wsInfraClusterHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterHoldInterval.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraClusterHoldInterval.setUnits("seconds")


class _WsInfraClusterHBInterval_Type(Unsigned32):
    """Custom type wsInfraClusterHBInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WsInfraClusterHBInterval_Type.__name__ = "Unsigned32"
_WsInfraClusterHBInterval_Object = MibScalar
wsInfraClusterHBInterval = _WsInfraClusterHBInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 7),
    _WsInfraClusterHBInterval_Type()
)
wsInfraClusterHBInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterHBInterval.setStatus("current")


class _WsInfraClusterHandleSTP_Type(Integer32):
    """Custom type wsInfraClusterHandleSTP based on Integer32"""
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


_WsInfraClusterHandleSTP_Type.__name__ = "Integer32"
_WsInfraClusterHandleSTP_Object = MibScalar
wsInfraClusterHandleSTP = _WsInfraClusterHandleSTP_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 8),
    _WsInfraClusterHandleSTP_Type()
)
wsInfraClusterHandleSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterHandleSTP.setStatus("current")


class _WsInfraClusterSwitchState_Type(Integer32):
    """Custom type wsInfraClusterSwitchState based on Integer32"""
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
        *(("disabled", 1),
          ("discovery", 3),
          ("online", 4),
          ("startup", 2))
    )


_WsInfraClusterSwitchState_Type.__name__ = "Integer32"
_WsInfraClusterSwitchState_Object = MibScalar
wsInfraClusterSwitchState = _WsInfraClusterSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 9),
    _WsInfraClusterSwitchState_Type()
)
wsInfraClusterSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterSwitchState.setStatus("current")


class _WsInfraClusterLicNum_Type(Unsigned32):
    """Custom type wsInfraClusterLicNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraClusterLicNum_Type.__name__ = "Unsigned32"
_WsInfraClusterLicNum_Object = MibScalar
wsInfraClusterLicNum = _WsInfraClusterLicNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 10),
    _WsInfraClusterLicNum_Type()
)
wsInfraClusterLicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterLicNum.setStatus("current")


class _WsInfraClusterInstalledLicNum_Type(Unsigned32):
    """Custom type wsInfraClusterInstalledLicNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraClusterInstalledLicNum_Type.__name__ = "Unsigned32"
_WsInfraClusterInstalledLicNum_Object = MibScalar
wsInfraClusterInstalledLicNum = _WsInfraClusterInstalledLicNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 11),
    _WsInfraClusterInstalledLicNum_Type()
)
wsInfraClusterInstalledLicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterInstalledLicNum.setStatus("current")
_WsInfraClusterApCnt_Type = Unsigned32
_WsInfraClusterApCnt_Object = MibScalar
wsInfraClusterApCnt = _WsInfraClusterApCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 12),
    _WsInfraClusterApCnt_Type()
)
wsInfraClusterApCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterApCnt.setStatus("current")
_WsInfraClusterVersion_Type = DisplayString
_WsInfraClusterVersion_Object = MibScalar
wsInfraClusterVersion = _WsInfraClusterVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 13),
    _WsInfraClusterVersion_Type()
)
wsInfraClusterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterVersion.setStatus("current")
_WsInfraClusterHistory_ObjectIdentity = ObjectIdentity
wsInfraClusterHistory = _WsInfraClusterHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14)
)
_WsInfraClusterHistoryTable_Object = MibTable
wsInfraClusterHistoryTable = _WsInfraClusterHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1)
)
if mibBuilder.loadTexts:
    wsInfraClusterHistoryTable.setStatus("current")
_WsInfraClusterHistoryEntry_Object = MibTableRow
wsInfraClusterHistoryEntry = _WsInfraClusterHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1)
)
wsInfraClusterHistoryEntry.setIndexNames(
    (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryIndex"),
)
if mibBuilder.loadTexts:
    wsInfraClusterHistoryEntry.setStatus("current")


class _WsInfraClusterHistoryIndex_Type(Unsigned32):
    """Custom type wsInfraClusterHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsInfraClusterHistoryIndex_Type.__name__ = "Unsigned32"
_WsInfraClusterHistoryIndex_Object = MibTableColumn
wsInfraClusterHistoryIndex = _WsInfraClusterHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 1),
    _WsInfraClusterHistoryIndex_Type()
)
wsInfraClusterHistoryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraClusterHistoryIndex.setStatus("current")


class _WsInfraClusterHistoryState_Type(Integer32):
    """Custom type wsInfraClusterHistoryState based on Integer32"""
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
        *(("disabled", 1),
          ("discovery", 3),
          ("online", 4),
          ("startup", 2))
    )


_WsInfraClusterHistoryState_Type.__name__ = "Integer32"
_WsInfraClusterHistoryState_Object = MibTableColumn
wsInfraClusterHistoryState = _WsInfraClusterHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 2),
    _WsInfraClusterHistoryState_Type()
)
wsInfraClusterHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterHistoryState.setStatus("current")
_WsInfraClusterHistoryTime_Type = DateAndTime
_WsInfraClusterHistoryTime_Object = MibTableColumn
wsInfraClusterHistoryTime = _WsInfraClusterHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 3),
    _WsInfraClusterHistoryTime_Type()
)
wsInfraClusterHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterHistoryTime.setStatus("current")


class _WsInfraClusterHistoryEventTrigger_Type(Integer32):
    """Custom type wsInfraClusterHistoryEventTrigger based on Integer32"""
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
          ("discoveryDone", 4),
          ("enable", 1),
          ("startupDone", 3))
    )


_WsInfraClusterHistoryEventTrigger_Type.__name__ = "Integer32"
_WsInfraClusterHistoryEventTrigger_Object = MibTableColumn
wsInfraClusterHistoryEventTrigger = _WsInfraClusterHistoryEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 4),
    _WsInfraClusterHistoryEventTrigger_Type()
)
wsInfraClusterHistoryEventTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterHistoryEventTrigger.setStatus("current")
_WsInfraClusterHistoryDesc_Type = DisplayString
_WsInfraClusterHistoryDesc_Object = MibTableColumn
wsInfraClusterHistoryDesc = _WsInfraClusterHistoryDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 14, 1, 1, 5),
    _WsInfraClusterHistoryDesc_Type()
)
wsInfraClusterHistoryDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterHistoryDesc.setStatus("current")
_WsInfraClusterConfig_ObjectIdentity = ObjectIdentity
wsInfraClusterConfig = _WsInfraClusterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15)
)
_WsInfraClusterConfigTable_Object = MibTable
wsInfraClusterConfigTable = _WsInfraClusterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1)
)
if mibBuilder.loadTexts:
    wsInfraClusterConfigTable.setStatus("current")
_WsInfraClusterConfigEntry_Object = MibTableRow
wsInfraClusterConfigEntry = _WsInfraClusterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1)
)
wsInfraClusterConfigEntry.setIndexNames(
    (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"),
    (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"),
)
if mibBuilder.loadTexts:
    wsInfraClusterConfigEntry.setStatus("current")


class _WsInfraClusterConfigIndex_Type(Integer32):
    """Custom type wsInfraClusterConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WsInfraClusterConfigIndex_Type.__name__ = "Integer32"
_WsInfraClusterConfigIndex_Object = MibTableColumn
wsInfraClusterConfigIndex = _WsInfraClusterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 1),
    _WsInfraClusterConfigIndex_Type()
)
wsInfraClusterConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterConfigIndex.setStatus("current")
_WsInfraClusterMemberIpAddr_Type = IpAddress
_WsInfraClusterMemberIpAddr_Object = MibTableColumn
wsInfraClusterMemberIpAddr = _WsInfraClusterMemberIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 2),
    _WsInfraClusterMemberIpAddr_Type()
)
wsInfraClusterMemberIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterMemberIpAddr.setStatus("current")
_WsInfraClusterCfgRowStatus_Type = RowStatus
_WsInfraClusterCfgRowStatus_Object = MibTableColumn
wsInfraClusterCfgRowStatus = _WsInfraClusterCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 3),
    _WsInfraClusterCfgRowStatus_Type()
)
wsInfraClusterCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsInfraClusterCfgRowStatus.setStatus("current")
_WsInfraClustertNumHBSent_Type = Unsigned32
_WsInfraClustertNumHBSent_Object = MibTableColumn
wsInfraClustertNumHBSent = _WsInfraClustertNumHBSent_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 4),
    _WsInfraClustertNumHBSent_Type()
)
wsInfraClustertNumHBSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClustertNumHBSent.setStatus("current")
_WsInfraClusterNumHBRcvd_Type = Unsigned32
_WsInfraClusterNumHBRcvd_Object = MibTableColumn
wsInfraClusterNumHBRcvd = _WsInfraClusterNumHBRcvd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 5),
    _WsInfraClusterNumHBRcvd_Type()
)
wsInfraClusterNumHBRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumHBRcvd.setStatus("current")
_WsInfraClusterLastSeen_Type = DateAndTime
_WsInfraClusterLastSeen_Object = MibTableColumn
wsInfraClusterLastSeen = _WsInfraClusterLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 6),
    _WsInfraClusterLastSeen_Type()
)
wsInfraClusterLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterLastSeen.setStatus("current")
_WsInfraClusterFirstSeen_Type = DateAndTime
_WsInfraClusterFirstSeen_Object = MibTableColumn
wsInfraClusterFirstSeen = _WsInfraClusterFirstSeen_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 7),
    _WsInfraClusterFirstSeen_Type()
)
wsInfraClusterFirstSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterFirstSeen.setStatus("current")
_WsInfraClusterNumUpdMesgSent_Type = Unsigned32
_WsInfraClusterNumUpdMesgSent_Object = MibTableColumn
wsInfraClusterNumUpdMesgSent = _WsInfraClusterNumUpdMesgSent_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 8),
    _WsInfraClusterNumUpdMesgSent_Type()
)
wsInfraClusterNumUpdMesgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumUpdMesgSent.setStatus("current")
_WsInfraClusterNumUpdMesgRecd_Type = Unsigned32
_WsInfraClusterNumUpdMesgRecd_Object = MibTableColumn
wsInfraClusterNumUpdMesgRecd = _WsInfraClusterNumUpdMesgRecd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 9),
    _WsInfraClusterNumUpdMesgRecd_Type()
)
wsInfraClusterNumUpdMesgRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumUpdMesgRecd.setStatus("current")


class _WsInfraClusterStatus_Type(Integer32):
    """Custom type wsInfraClusterStatus based on Integer32"""
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
        *(("peerConfigured", 1),
          ("peerEstablished", 5),
          ("peerInvalid", 2),
          ("peerNotSeen", 4),
          ("peerSeen", 3))
    )


_WsInfraClusterStatus_Type.__name__ = "Integer32"
_WsInfraClusterStatus_Object = MibTableColumn
wsInfraClusterStatus = _WsInfraClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 10),
    _WsInfraClusterStatus_Type()
)
wsInfraClusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterStatus.setStatus("current")
_WsInfraClusterAdoptionCnt_Type = Unsigned32
_WsInfraClusterAdoptionCnt_Object = MibTableColumn
wsInfraClusterAdoptionCnt = _WsInfraClusterAdoptionCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 11),
    _WsInfraClusterAdoptionCnt_Type()
)
wsInfraClusterAdoptionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterAdoptionCnt.setStatus("current")


class _WsInfraClusterSwitchMode_Type(Integer32):
    """Custom type wsInfraClusterSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_WsInfraClusterSwitchMode_Type.__name__ = "Integer32"
_WsInfraClusterSwitchMode_Object = MibTableColumn
wsInfraClusterSwitchMode = _WsInfraClusterSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 12),
    _WsInfraClusterSwitchMode_Type()
)
wsInfraClusterSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterSwitchMode.setStatus("current")


class _WsInfraClusterInstalLicValue_Type(Unsigned32):
    """Custom type wsInfraClusterInstalLicValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraClusterInstalLicValue_Type.__name__ = "Unsigned32"
_WsInfraClusterInstalLicValue_Object = MibTableColumn
wsInfraClusterInstalLicValue = _WsInfraClusterInstalLicValue_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 13),
    _WsInfraClusterInstalLicValue_Type()
)
wsInfraClusterInstalLicValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterInstalLicValue.setStatus("current")
_WsInfraClusterUptime_Type = DateAndTime
_WsInfraClusterUptime_Object = MibTableColumn
wsInfraClusterUptime = _WsInfraClusterUptime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 14),
    _WsInfraClusterUptime_Type()
)
wsInfraClusterUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterUptime.setStatus("current")
_WsInfraClusterNumMusAdopted_Type = Unsigned32
_WsInfraClusterNumMusAdopted_Object = MibTableColumn
wsInfraClusterNumMusAdopted = _WsInfraClusterNumMusAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 15),
    _WsInfraClusterNumMusAdopted_Type()
)
wsInfraClusterNumMusAdopted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumMusAdopted.setStatus("current")
_WsInfraClusterNumRadiosAdopted_Type = Unsigned32
_WsInfraClusterNumRadiosAdopted_Object = MibTableColumn
wsInfraClusterNumRadiosAdopted = _WsInfraClusterNumRadiosAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 16),
    _WsInfraClusterNumRadiosAdopted_Type()
)
wsInfraClusterNumRadiosAdopted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumRadiosAdopted.setStatus("current")
_WsInfraClusterNumSelfHealingRadios_Type = Unsigned32
_WsInfraClusterNumSelfHealingRadios_Object = MibTableColumn
wsInfraClusterNumSelfHealingRadios = _WsInfraClusterNumSelfHealingRadios_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 17),
    _WsInfraClusterNumSelfHealingRadios_Type()
)
wsInfraClusterNumSelfHealingRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumSelfHealingRadios.setStatus("current")
_WsInfraClusterNumRogueAps_Type = Unsigned32
_WsInfraClusterNumRogueAps_Object = MibTableColumn
wsInfraClusterNumRogueAps = _WsInfraClusterNumRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 18),
    _WsInfraClusterNumRogueAps_Type()
)
wsInfraClusterNumRogueAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterNumRogueAps.setStatus("current")
_WsInfraClusterCfgRunningImgVer_Type = DisplayString
_WsInfraClusterCfgRunningImgVer_Object = MibTableColumn
wsInfraClusterCfgRunningImgVer = _WsInfraClusterCfgRunningImgVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 19),
    _WsInfraClusterCfgRunningImgVer_Type()
)
wsInfraClusterCfgRunningImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterCfgRunningImgVer.setStatus("current")
_WsInfraClusterCfgPortAdoptionCapacity_Type = Unsigned32
_WsInfraClusterCfgPortAdoptionCapacity_Object = MibTableColumn
wsInfraClusterCfgPortAdoptionCapacity = _WsInfraClusterCfgPortAdoptionCapacity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 1, 1, 20),
    _WsInfraClusterCfgPortAdoptionCapacity_Type()
)
wsInfraClusterCfgPortAdoptionCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterCfgPortAdoptionCapacity.setStatus("current")
_WsInfraClusterPeerStatTable_Object = MibTable
wsInfraClusterPeerStatTable = _WsInfraClusterPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2)
)
if mibBuilder.loadTexts:
    wsInfraClusterPeerStatTable.setStatus("obsolete")
_WsInfraClusterPeerStatEntry_Object = MibTableRow
wsInfraClusterPeerStatEntry = _WsInfraClusterPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2, 1)
)
wsInfraClusterPeerStatEntry.setIndexNames(
    (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"),
    (0, "WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"),
)
if mibBuilder.loadTexts:
    wsInfraClusterPeerStatEntry.setStatus("obsolete")
_WsInfraClusterStatNumHBSent_Type = Unsigned32
_WsInfraClusterStatNumHBSent_Object = MibTableColumn
wsInfraClusterStatNumHBSent = _WsInfraClusterStatNumHBSent_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 15, 2, 1, 1),
    _WsInfraClusterStatNumHBSent_Type()
)
wsInfraClusterStatNumHBSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterStatNumHBSent.setStatus("obsolete")


class _WsInfraClusterUpAndFullyConnected_Type(Integer32):
    """Custom type wsInfraClusterUpAndFullyConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WsInfraClusterUpAndFullyConnected_Type.__name__ = "Integer32"
_WsInfraClusterUpAndFullyConnected_Object = MibScalar
wsInfraClusterUpAndFullyConnected = _WsInfraClusterUpAndFullyConnected_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 16),
    _WsInfraClusterUpAndFullyConnected_Type()
)
wsInfraClusterUpAndFullyConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterUpAndFullyConnected.setStatus("current")
_WsInfraClusterTotalApsAdopted_Type = Integer32
_WsInfraClusterTotalApsAdopted_Object = MibScalar
wsInfraClusterTotalApsAdopted = _WsInfraClusterTotalApsAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 17),
    _WsInfraClusterTotalApsAdopted_Type()
)
wsInfraClusterTotalApsAdopted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalApsAdopted.setStatus("current")
_WsInfraClusterTotalRadiosAdopted_Type = Integer32
_WsInfraClusterTotalRadiosAdopted_Object = MibScalar
wsInfraClusterTotalRadiosAdopted = _WsInfraClusterTotalRadiosAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 18),
    _WsInfraClusterTotalRadiosAdopted_Type()
)
wsInfraClusterTotalRadiosAdopted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalRadiosAdopted.setStatus("current")
_WsInfraClusterTotalMusAssociated_Type = Integer32
_WsInfraClusterTotalMusAssociated_Object = MibScalar
wsInfraClusterTotalMusAssociated = _WsInfraClusterTotalMusAssociated_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 19),
    _WsInfraClusterTotalMusAssociated_Type()
)
wsInfraClusterTotalMusAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalMusAssociated.setStatus("current")
_WsInfraClusterTotalRogueAps_Type = Integer32
_WsInfraClusterTotalRogueAps_Object = MibScalar
wsInfraClusterTotalRogueAps = _WsInfraClusterTotalRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 20),
    _WsInfraClusterTotalRogueAps_Type()
)
wsInfraClusterTotalRogueAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalRogueAps.setStatus("current")
_WsInfraClusterTotalPortAdoptionCapacity_Type = Integer32
_WsInfraClusterTotalPortAdoptionCapacity_Object = MibScalar
wsInfraClusterTotalPortAdoptionCapacity = _WsInfraClusterTotalPortAdoptionCapacity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 21),
    _WsInfraClusterTotalPortAdoptionCapacity_Type()
)
wsInfraClusterTotalPortAdoptionCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalPortAdoptionCapacity.setStatus("current")
_WsInfraClusterTotalSelfHealingRadios_Type = Integer32
_WsInfraClusterTotalSelfHealingRadios_Object = MibScalar
wsInfraClusterTotalSelfHealingRadios = _WsInfraClusterTotalSelfHealingRadios_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 22),
    _WsInfraClusterTotalSelfHealingRadios_Type()
)
wsInfraClusterTotalSelfHealingRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterTotalSelfHealingRadios.setStatus("current")
_WsInfraClusterMusAdoptedCnt_Type = Integer32
_WsInfraClusterMusAdoptedCnt_Object = MibScalar
wsInfraClusterMusAdoptedCnt = _WsInfraClusterMusAdoptedCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 23),
    _WsInfraClusterMusAdoptedCnt_Type()
)
wsInfraClusterMusAdoptedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterMusAdoptedCnt.setStatus("current")
_WsInfraClusterRadiosAdoptedCnt_Type = Integer32
_WsInfraClusterRadiosAdoptedCnt_Object = MibScalar
wsInfraClusterRadiosAdoptedCnt = _WsInfraClusterRadiosAdoptedCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 24),
    _WsInfraClusterRadiosAdoptedCnt_Type()
)
wsInfraClusterRadiosAdoptedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterRadiosAdoptedCnt.setStatus("current")
_WsInfraClusterSelfHealingRadioCnt_Type = Integer32
_WsInfraClusterSelfHealingRadioCnt_Object = MibScalar
wsInfraClusterSelfHealingRadioCnt = _WsInfraClusterSelfHealingRadioCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 25),
    _WsInfraClusterSelfHealingRadioCnt_Type()
)
wsInfraClusterSelfHealingRadioCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterSelfHealingRadioCnt.setStatus("current")
_WsInfraClusterRogueApCnt_Type = Integer32
_WsInfraClusterRogueApCnt_Object = MibScalar
wsInfraClusterRogueApCnt = _WsInfraClusterRogueApCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 26),
    _WsInfraClusterRogueApCnt_Type()
)
wsInfraClusterRogueApCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterRogueApCnt.setStatus("current")
_WsInfraClusterRunningImgVer_Type = DisplayString
_WsInfraClusterRunningImgVer_Object = MibScalar
wsInfraClusterRunningImgVer = _WsInfraClusterRunningImgVer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 27),
    _WsInfraClusterRunningImgVer_Type()
)
wsInfraClusterRunningImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterRunningImgVer.setStatus("current")
_WsInfraClusterPortAdoptionCapacity_Type = Integer32
_WsInfraClusterPortAdoptionCapacity_Object = MibScalar
wsInfraClusterPortAdoptionCapacity = _WsInfraClusterPortAdoptionCapacity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 28),
    _WsInfraClusterPortAdoptionCapacity_Type()
)
wsInfraClusterPortAdoptionCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterPortAdoptionCapacity.setStatus("current")


class _WsInfraClusterAutoRevert_Type(Integer32):
    """Custom type wsInfraClusterAutoRevert based on Integer32"""
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


_WsInfraClusterAutoRevert_Type.__name__ = "Integer32"
_WsInfraClusterAutoRevert_Object = MibScalar
wsInfraClusterAutoRevert = _WsInfraClusterAutoRevert_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 29),
    _WsInfraClusterAutoRevert_Type()
)
wsInfraClusterAutoRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterAutoRevert.setStatus("current")


class _WsInfraClusterAutoRevertDelay_Type(Unsigned32):
    """Custom type wsInfraClusterAutoRevertDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_WsInfraClusterAutoRevertDelay_Type.__name__ = "Unsigned32"
_WsInfraClusterAutoRevertDelay_Object = MibScalar
wsInfraClusterAutoRevertDelay = _WsInfraClusterAutoRevertDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 30),
    _WsInfraClusterAutoRevertDelay_Type()
)
wsInfraClusterAutoRevertDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterAutoRevertDelay.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraClusterAutoRevertDelay.setUnits("minutes")


class _WsInfraClusterManualRevert_Type(Integer32):
    """Custom type wsInfraClusterManualRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("manualRevertNow", 1)
    )


_WsInfraClusterManualRevert_Type.__name__ = "Integer32"
_WsInfraClusterManualRevert_Object = MibScalar
wsInfraClusterManualRevert = _WsInfraClusterManualRevert_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 31),
    _WsInfraClusterManualRevert_Type()
)
wsInfraClusterManualRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterManualRevert.setStatus("current")


class _WsInfraClusterDhcpRedundancy_Type(Integer32):
    """Custom type wsInfraClusterDhcpRedundancy based on Integer32"""
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


_WsInfraClusterDhcpRedundancy_Type.__name__ = "Integer32"
_WsInfraClusterDhcpRedundancy_Object = MibScalar
wsInfraClusterDhcpRedundancy = _WsInfraClusterDhcpRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 32),
    _WsInfraClusterDhcpRedundancy_Type()
)
wsInfraClusterDhcpRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDhcpRedundancy.setStatus("current")


class _WsInfraClusterActiveDhcpServerSwitch_Type(DisplayString):
    """Custom type wsInfraClusterActiveDhcpServerSwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WsInfraClusterActiveDhcpServerSwitch_Type.__name__ = "DisplayString"
_WsInfraClusterActiveDhcpServerSwitch_Object = MibScalar
wsInfraClusterActiveDhcpServerSwitch = _WsInfraClusterActiveDhcpServerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 33),
    _WsInfraClusterActiveDhcpServerSwitch_Type()
)
wsInfraClusterActiveDhcpServerSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraClusterActiveDhcpServerSwitch.setStatus("current")


class _WsInfraClusterResetActiveDhcpServer_Type(Integer32):
    """Custom type wsInfraClusterResetActiveDhcpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetActiveDhcpServer", 1)
    )


_WsInfraClusterResetActiveDhcpServer_Type.__name__ = "Integer32"
_WsInfraClusterResetActiveDhcpServer_Object = MibScalar
wsInfraClusterResetActiveDhcpServer = _WsInfraClusterResetActiveDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 34),
    _WsInfraClusterResetActiveDhcpServer_Type()
)
wsInfraClusterResetActiveDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterResetActiveDhcpServer.setStatus("current")
_WsInfraCriticalResourceIp_Type = IpAddress
_WsInfraCriticalResourceIp_Object = MibScalar
wsInfraCriticalResourceIp = _WsInfraCriticalResourceIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 35),
    _WsInfraCriticalResourceIp_Type()
)
wsInfraCriticalResourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraCriticalResourceIp.setStatus("current")
_WsInfraClusterDynApLoadBal_ObjectIdentity = ObjectIdentity
wsInfraClusterDynApLoadBal = _WsInfraClusterDynApLoadBal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36)
)
_WsInfraClusterDynApLoadBalEnable_Type = TruthValue
_WsInfraClusterDynApLoadBalEnable_Object = MibScalar
wsInfraClusterDynApLoadBalEnable = _WsInfraClusterDynApLoadBalEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 1),
    _WsInfraClusterDynApLoadBalEnable_Type()
)
wsInfraClusterDynApLoadBalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalEnable.setStatus("current")


class _WsInfraClusterDynApLoadBalApproach_Type(Integer32):
    """Custom type wsInfraClusterDynApLoadBalApproach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("runtime", 2),
          ("schedule", 1))
    )


_WsInfraClusterDynApLoadBalApproach_Type.__name__ = "Integer32"
_WsInfraClusterDynApLoadBalApproach_Object = MibScalar
wsInfraClusterDynApLoadBalApproach = _WsInfraClusterDynApLoadBalApproach_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 2),
    _WsInfraClusterDynApLoadBalApproach_Type()
)
wsInfraClusterDynApLoadBalApproach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalApproach.setStatus("current")
_WsInfraClusterDynApLoadBalSched_ObjectIdentity = ObjectIdentity
wsInfraClusterDynApLoadBalSched = _WsInfraClusterDynApLoadBalSched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3)
)
_WsInfraClusterDynApLoadBalSchedStartTime_Type = DateAndTime
_WsInfraClusterDynApLoadBalSchedStartTime_Object = MibScalar
wsInfraClusterDynApLoadBalSchedStartTime = _WsInfraClusterDynApLoadBalSchedStartTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3, 1),
    _WsInfraClusterDynApLoadBalSchedStartTime_Type()
)
wsInfraClusterDynApLoadBalSchedStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalSchedStartTime.setStatus("current")


class _WsInfraClusterDynApLoadBalSchedInterval_Type(Unsigned32):
    """Custom type wsInfraClusterDynApLoadBalSchedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_WsInfraClusterDynApLoadBalSchedInterval_Type.__name__ = "Unsigned32"
_WsInfraClusterDynApLoadBalSchedInterval_Object = MibScalar
wsInfraClusterDynApLoadBalSchedInterval = _WsInfraClusterDynApLoadBalSchedInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 3, 2),
    _WsInfraClusterDynApLoadBalSchedInterval_Type()
)
wsInfraClusterDynApLoadBalSchedInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalSchedInterval.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalSchedInterval.setUnits("days")
_WsInfraClusterDynApLoadBalStart_Type = DoActionNow
_WsInfraClusterDynApLoadBalStart_Object = MibScalar
wsInfraClusterDynApLoadBalStart = _WsInfraClusterDynApLoadBalStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 4),
    _WsInfraClusterDynApLoadBalStart_Type()
)
wsInfraClusterDynApLoadBalStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalStart.setStatus("current")


class _WsInfraClusterDynApLoadBalMUThrshld_Type(Integer32):
    """Custom type wsInfraClusterDynApLoadBalMUThrshld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_WsInfraClusterDynApLoadBalMUThrshld_Type.__name__ = "Integer32"
_WsInfraClusterDynApLoadBalMUThrshld_Object = MibScalar
wsInfraClusterDynApLoadBalMUThrshld = _WsInfraClusterDynApLoadBalMUThrshld_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 36, 5),
    _WsInfraClusterDynApLoadBalMUThrshld_Type()
)
wsInfraClusterDynApLoadBalMUThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalMUThrshld.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraClusterDynApLoadBalMUThrshld.setUnits("MUs")


class _WsInfraClusterLicensingAlgorithm_Type(Integer32):
    """Custom type wsInfraClusterLicensingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregation", 2),
          ("max", 1))
    )


_WsInfraClusterLicensingAlgorithm_Type.__name__ = "Integer32"
_WsInfraClusterLicensingAlgorithm_Object = MibScalar
wsInfraClusterLicensingAlgorithm = _WsInfraClusterLicensingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 37),
    _WsInfraClusterLicensingAlgorithm_Type()
)
wsInfraClusterLicensingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraClusterLicensingAlgorithm.setStatus("current")
_WsInfrastructureMIBConformance_ObjectIdentity = ObjectIdentity
wsInfrastructureMIBConformance = _WsInfrastructureMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100)
)
_WsInfrastructureMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfrastructureMIBCompliances = _WsInfrastructureMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 1)
)
_WsInfrastructureMIBGroups_ObjectIdentity = ObjectIdentity
wsInfrastructureMIBGroups = _WsInfrastructureMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2)
)

# Managed Objects groups

wsInfrastructureMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2, 1)
)
wsInfrastructureMIBGroup.setObjects(
      *(("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchIP"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterEnable"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMode"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterId"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHBInterval"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHandleSTP"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchState"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLicNum"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterInstalledLicNum"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterApCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterVersion"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryIndex"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryState"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryTime"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryEventTrigger"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHistoryDesc"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgRowStatus"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMemberIpAddr"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterHoldInterval"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDiscoveryInterval"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterUpAndFullyConnected"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalApsAdopted"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalRadiosAdopted"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalMusAssociated"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalRogueAps"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalPortAdoptionCapacity"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterTotalSelfHealingRadios"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterMusAdoptedCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRadiosAdoptedCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSelfHealingRadioCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRogueApCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterRunningImgVer"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterPortAdoptionCapacity"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterConfigIndex"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAutoRevert"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAutoRevertDelay"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterResetActiveDhcpServer"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterActiveDhcpServerSwitch"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDhcpRedundancy"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraCriticalResourceIp"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalEnable"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalApproach"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalMUThrshld"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalStart"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLicensingAlgorithm"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterManualRevert"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClustertNumHBSent"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumHBRcvd"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterLastSeen"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterFirstSeen"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumUpdMesgSent"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumUpdMesgRecd"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterStatus"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterAdoptionCnt"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterSwitchMode"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterInstalLicValue"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterUptime"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumMusAdopted"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumRadiosAdopted"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumSelfHealingRadios"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterNumRogueAps"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgRunningImgVer"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterCfgPortAdoptionCapacity"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalSchedStartTime"),
        ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterDynApLoadBalSchedInterval"))
)
if mibBuilder.loadTexts:
    wsInfrastructureMIBGroup.setStatus("current")

wsInfrastructureMIBObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 2, 2)
)
wsInfrastructureMIBObsoleteGroup.setObjects(
    ("WS-INFRA-CLUSTER-MIB", "wsInfraClusterStatNumHBSent")
)
if mibBuilder.loadTexts:
    wsInfrastructureMIBObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfrastructureMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfrastructureMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-CLUSTER-MIB",
    **{"wsInfraClusterMIB": wsInfraClusterMIB,
       "wsInfraClusterSwitchIP": wsInfraClusterSwitchIP,
       "wsInfraClusterEnable": wsInfraClusterEnable,
       "wsInfraClusterMode": wsInfraClusterMode,
       "wsInfraClusterId": wsInfraClusterId,
       "wsInfraClusterDiscoveryInterval": wsInfraClusterDiscoveryInterval,
       "wsInfraClusterHoldInterval": wsInfraClusterHoldInterval,
       "wsInfraClusterHBInterval": wsInfraClusterHBInterval,
       "wsInfraClusterHandleSTP": wsInfraClusterHandleSTP,
       "wsInfraClusterSwitchState": wsInfraClusterSwitchState,
       "wsInfraClusterLicNum": wsInfraClusterLicNum,
       "wsInfraClusterInstalledLicNum": wsInfraClusterInstalledLicNum,
       "wsInfraClusterApCnt": wsInfraClusterApCnt,
       "wsInfraClusterVersion": wsInfraClusterVersion,
       "wsInfraClusterHistory": wsInfraClusterHistory,
       "wsInfraClusterHistoryTable": wsInfraClusterHistoryTable,
       "wsInfraClusterHistoryEntry": wsInfraClusterHistoryEntry,
       "wsInfraClusterHistoryIndex": wsInfraClusterHistoryIndex,
       "wsInfraClusterHistoryState": wsInfraClusterHistoryState,
       "wsInfraClusterHistoryTime": wsInfraClusterHistoryTime,
       "wsInfraClusterHistoryEventTrigger": wsInfraClusterHistoryEventTrigger,
       "wsInfraClusterHistoryDesc": wsInfraClusterHistoryDesc,
       "wsInfraClusterConfig": wsInfraClusterConfig,
       "wsInfraClusterConfigTable": wsInfraClusterConfigTable,
       "wsInfraClusterConfigEntry": wsInfraClusterConfigEntry,
       "wsInfraClusterConfigIndex": wsInfraClusterConfigIndex,
       "wsInfraClusterMemberIpAddr": wsInfraClusterMemberIpAddr,
       "wsInfraClusterCfgRowStatus": wsInfraClusterCfgRowStatus,
       "wsInfraClustertNumHBSent": wsInfraClustertNumHBSent,
       "wsInfraClusterNumHBRcvd": wsInfraClusterNumHBRcvd,
       "wsInfraClusterLastSeen": wsInfraClusterLastSeen,
       "wsInfraClusterFirstSeen": wsInfraClusterFirstSeen,
       "wsInfraClusterNumUpdMesgSent": wsInfraClusterNumUpdMesgSent,
       "wsInfraClusterNumUpdMesgRecd": wsInfraClusterNumUpdMesgRecd,
       "wsInfraClusterStatus": wsInfraClusterStatus,
       "wsInfraClusterAdoptionCnt": wsInfraClusterAdoptionCnt,
       "wsInfraClusterSwitchMode": wsInfraClusterSwitchMode,
       "wsInfraClusterInstalLicValue": wsInfraClusterInstalLicValue,
       "wsInfraClusterUptime": wsInfraClusterUptime,
       "wsInfraClusterNumMusAdopted": wsInfraClusterNumMusAdopted,
       "wsInfraClusterNumRadiosAdopted": wsInfraClusterNumRadiosAdopted,
       "wsInfraClusterNumSelfHealingRadios": wsInfraClusterNumSelfHealingRadios,
       "wsInfraClusterNumRogueAps": wsInfraClusterNumRogueAps,
       "wsInfraClusterCfgRunningImgVer": wsInfraClusterCfgRunningImgVer,
       "wsInfraClusterCfgPortAdoptionCapacity": wsInfraClusterCfgPortAdoptionCapacity,
       "wsInfraClusterPeerStatTable": wsInfraClusterPeerStatTable,
       "wsInfraClusterPeerStatEntry": wsInfraClusterPeerStatEntry,
       "wsInfraClusterStatNumHBSent": wsInfraClusterStatNumHBSent,
       "wsInfraClusterUpAndFullyConnected": wsInfraClusterUpAndFullyConnected,
       "wsInfraClusterTotalApsAdopted": wsInfraClusterTotalApsAdopted,
       "wsInfraClusterTotalRadiosAdopted": wsInfraClusterTotalRadiosAdopted,
       "wsInfraClusterTotalMusAssociated": wsInfraClusterTotalMusAssociated,
       "wsInfraClusterTotalRogueAps": wsInfraClusterTotalRogueAps,
       "wsInfraClusterTotalPortAdoptionCapacity": wsInfraClusterTotalPortAdoptionCapacity,
       "wsInfraClusterTotalSelfHealingRadios": wsInfraClusterTotalSelfHealingRadios,
       "wsInfraClusterMusAdoptedCnt": wsInfraClusterMusAdoptedCnt,
       "wsInfraClusterRadiosAdoptedCnt": wsInfraClusterRadiosAdoptedCnt,
       "wsInfraClusterSelfHealingRadioCnt": wsInfraClusterSelfHealingRadioCnt,
       "wsInfraClusterRogueApCnt": wsInfraClusterRogueApCnt,
       "wsInfraClusterRunningImgVer": wsInfraClusterRunningImgVer,
       "wsInfraClusterPortAdoptionCapacity": wsInfraClusterPortAdoptionCapacity,
       "wsInfraClusterAutoRevert": wsInfraClusterAutoRevert,
       "wsInfraClusterAutoRevertDelay": wsInfraClusterAutoRevertDelay,
       "wsInfraClusterManualRevert": wsInfraClusterManualRevert,
       "wsInfraClusterDhcpRedundancy": wsInfraClusterDhcpRedundancy,
       "wsInfraClusterActiveDhcpServerSwitch": wsInfraClusterActiveDhcpServerSwitch,
       "wsInfraClusterResetActiveDhcpServer": wsInfraClusterResetActiveDhcpServer,
       "wsInfraCriticalResourceIp": wsInfraCriticalResourceIp,
       "wsInfraClusterDynApLoadBal": wsInfraClusterDynApLoadBal,
       "wsInfraClusterDynApLoadBalEnable": wsInfraClusterDynApLoadBalEnable,
       "wsInfraClusterDynApLoadBalApproach": wsInfraClusterDynApLoadBalApproach,
       "wsInfraClusterDynApLoadBalSched": wsInfraClusterDynApLoadBalSched,
       "wsInfraClusterDynApLoadBalSchedStartTime": wsInfraClusterDynApLoadBalSchedStartTime,
       "wsInfraClusterDynApLoadBalSchedInterval": wsInfraClusterDynApLoadBalSchedInterval,
       "wsInfraClusterDynApLoadBalStart": wsInfraClusterDynApLoadBalStart,
       "wsInfraClusterDynApLoadBalMUThrshld": wsInfraClusterDynApLoadBalMUThrshld,
       "wsInfraClusterLicensingAlgorithm": wsInfraClusterLicensingAlgorithm,
       "wsInfrastructureMIBConformance": wsInfrastructureMIBConformance,
       "wsInfrastructureMIBCompliances": wsInfrastructureMIBCompliances,
       "wsInfrastructureMIBCompliance": wsInfrastructureMIBCompliance,
       "wsInfrastructureMIBGroups": wsInfrastructureMIBGroups,
       "wsInfrastructureMIBGroup": wsInfrastructureMIBGroup,
       "wsInfrastructureMIBObsoleteGroup": wsInfrastructureMIBObsoleteGroup}
)
