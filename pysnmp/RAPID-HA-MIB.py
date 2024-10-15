# SNMP MIB module (RAPID-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-HA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:36 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6)
)
rsInfoModule.setRevisions(
        ("2002-11-01 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsHAMIB_ObjectIdentity = ObjectIdentity
rsHAMIB = _RsHAMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6)
)
if mibBuilder.loadTexts:
    rsHAMIB.setStatus("current")
_RsHALocal_ObjectIdentity = ObjectIdentity
rsHALocal = _RsHALocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1)
)
if mibBuilder.loadTexts:
    rsHALocal.setStatus("current")


class _RsHAStatus_Type(Integer32):
    """Custom type rsHAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("aa-primary-ative", 4),
          ("aa-primary-takeover", 6),
          ("aa-secondary-active", 5),
          ("aa-secondary-takeover", 7),
          ("admin", 9),
          ("as-primary-active", 2),
          ("as-secondary-active", 3),
          ("disabled", 0),
          ("failed", 10),
          ("standby", 8),
          ("unavailable", 11),
          ("unknown", 1))
    )


_RsHAStatus_Type.__name__ = "Integer32"
_RsHAStatus_Object = MibScalar
rsHAStatus = _RsHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 1),
    _RsHAStatus_Type()
)
rsHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAStatus.setStatus("current")


class _RsHAPeerStatus_Type(Integer32):
    """Custom type rsHAPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("admin", 3),
          ("failed", 4),
          ("standby", 2),
          ("unavailable", 0))
    )


_RsHAPeerStatus_Type.__name__ = "Integer32"
_RsHAPeerStatus_Object = MibScalar
rsHAPeerStatus = _RsHAPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 2),
    _RsHAPeerStatus_Type()
)
rsHAPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerStatus.setStatus("current")
_RsHALastDBSyncTime_Type = DateAndTime
_RsHALastDBSyncTime_Object = MibScalar
rsHALastDBSyncTime = _RsHALastDBSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 3),
    _RsHALastDBSyncTime_Type()
)
rsHALastDBSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHALastDBSyncTime.setStatus("current")


class _RsHAError_Type(Integer32):
    """Custom type rsHAError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("admin-command-failed", 10),
          ("config-sync-failed", 14),
          ("detect-ha-error", 11),
          ("forced-fail", 5),
          ("hotsync-failed", 13),
          ("invalid-ha-role", 6),
          ("link-down", 7),
          ("lost-mia-heartbeat", 8),
          ("mia-not-responding", 9),
          ("mismatched-database", 3),
          ("mismatched-ha-id", 1),
          ("mismatched-hardware", 4),
          ("mismatched-software", 2),
          ("no-error", 0),
          ("unavailable", 12))
    )


_RsHAError_Type.__name__ = "Integer32"
_RsHAError_Object = MibScalar
rsHAError = _RsHAError_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 4),
    _RsHAError_Type()
)
rsHAError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAError.setStatus("current")


class _RsHAPeerError_Type(Integer32):
    """Custom type rsHAPeerError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("admin-command-failed", 10),
          ("config-sync-failed", 14),
          ("detect-ha-error", 11),
          ("forced-fail", 5),
          ("hotsync-failed", 13),
          ("invalid-ha-role", 6),
          ("link-down", 7),
          ("lost-mia-heartbeat", 8),
          ("mia-not-responding", 9),
          ("mismatched-database", 3),
          ("mismatched-ha-id", 1),
          ("mismatched-hardware", 4),
          ("mismatched-software", 2),
          ("no-error", 0),
          ("unavailable", 12))
    )


_RsHAPeerError_Type.__name__ = "Integer32"
_RsHAPeerError_Object = MibScalar
rsHAPeerError = _RsHAPeerError_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 5),
    _RsHAPeerError_Type()
)
rsHAPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerError.setStatus("current")
_RsHAPeer_ObjectIdentity = ObjectIdentity
rsHAPeer = _RsHAPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2)
)
if mibBuilder.loadTexts:
    rsHAPeer.setStatus("current")
_RsHAPeerSerialNumber_Type = OctetString
_RsHAPeerSerialNumber_Object = MibScalar
rsHAPeerSerialNumber = _RsHAPeerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 1),
    _RsHAPeerSerialNumber_Type()
)
rsHAPeerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSerialNumber.setStatus("current")
_RsHAPeerLastDBSyncTime_Type = DateAndTime
_RsHAPeerLastDBSyncTime_Object = MibScalar
rsHAPeerLastDBSyncTime = _RsHAPeerLastDBSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 2),
    _RsHAPeerLastDBSyncTime_Type()
)
rsHAPeerLastDBSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerLastDBSyncTime.setStatus("current")
_RsHAPeerDevice_ObjectIdentity = ObjectIdentity
rsHAPeerDevice = _RsHAPeerDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    rsHAPeerDevice.setStatus("current")
_RsHAPeerIfNumber_Type = Unsigned32
_RsHAPeerIfNumber_Object = MibScalar
rsHAPeerIfNumber = _RsHAPeerIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 1),
    _RsHAPeerIfNumber_Type()
)
rsHAPeerIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerIfNumber.setStatus("current")
_RsHAPeerIfTable_Object = MibTable
rsHAPeerIfTable = _RsHAPeerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rsHAPeerIfTable.setStatus("current")
_RsHAPeerIfEntry_Object = MibTableRow
rsHAPeerIfEntry = _RsHAPeerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1)
)
rsHAPeerIfEntry.setIndexNames(
    (0, "RAPID-HA-MIB", "rsHAPeerIfIndex"),
)
if mibBuilder.loadTexts:
    rsHAPeerIfEntry.setStatus("current")
_RsHAPeerIfIndex_Type = Unsigned32
_RsHAPeerIfIndex_Object = MibTableColumn
rsHAPeerIfIndex = _RsHAPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 1),
    _RsHAPeerIfIndex_Type()
)
rsHAPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerIfIndex.setStatus("current")
_RsHAPeerIfIpAddr_Type = IpAddress
_RsHAPeerIfIpAddr_Object = MibTableColumn
rsHAPeerIfIpAddr = _RsHAPeerIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 4),
    _RsHAPeerIfIpAddr_Type()
)
rsHAPeerIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerIfIpAddr.setStatus("current")


class _RsHAPeerIfLinkStatus_Type(Integer32):
    """Custom type rsHAPeerIfLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("other", 2),
          ("up", 1))
    )


_RsHAPeerIfLinkStatus_Type.__name__ = "Integer32"
_RsHAPeerIfLinkStatus_Object = MibTableColumn
rsHAPeerIfLinkStatus = _RsHAPeerIfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 9),
    _RsHAPeerIfLinkStatus_Type()
)
rsHAPeerIfLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerIfLinkStatus.setStatus("current")
_RsHAPeerCounters_ObjectIdentity = ObjectIdentity
rsHAPeerCounters = _RsHAPeerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4)
)
if mibBuilder.loadTexts:
    rsHAPeerCounters.setStatus("current")
_RsHAPeerSystemCpuUtil_Type = Gauge32
_RsHAPeerSystemCpuUtil_Object = MibScalar
rsHAPeerSystemCpuUtil = _RsHAPeerSystemCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 1),
    _RsHAPeerSystemCpuUtil_Type()
)
rsHAPeerSystemCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemCpuUtil.setStatus("current")
_RsHAPeerSystemTotalSendBytes_Type = Counter64
_RsHAPeerSystemTotalSendBytes_Object = MibScalar
rsHAPeerSystemTotalSendBytes = _RsHAPeerSystemTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 2),
    _RsHAPeerSystemTotalSendBytes_Type()
)
rsHAPeerSystemTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemTotalSendBytes.setStatus("current")
_RsHAPeerSystemTotalRecvBytes_Type = Counter64
_RsHAPeerSystemTotalRecvBytes_Object = MibScalar
rsHAPeerSystemTotalRecvBytes = _RsHAPeerSystemTotalRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 3),
    _RsHAPeerSystemTotalRecvBytes_Type()
)
rsHAPeerSystemTotalRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemTotalRecvBytes.setStatus("current")
_RsHAPeerSystemTotalSendPackets_Type = Counter64
_RsHAPeerSystemTotalSendPackets_Object = MibScalar
rsHAPeerSystemTotalSendPackets = _RsHAPeerSystemTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 4),
    _RsHAPeerSystemTotalSendPackets_Type()
)
rsHAPeerSystemTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemTotalSendPackets.setStatus("current")
_RsHAPeerSystemTotalRecvPackets_Type = Counter64
_RsHAPeerSystemTotalRecvPackets_Object = MibScalar
rsHAPeerSystemTotalRecvPackets = _RsHAPeerSystemTotalRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 5),
    _RsHAPeerSystemTotalRecvPackets_Type()
)
rsHAPeerSystemTotalRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemTotalRecvPackets.setStatus("current")
_RsHAPeerSystemStreamReqTotal_Type = Counter64
_RsHAPeerSystemStreamReqTotal_Object = MibScalar
rsHAPeerSystemStreamReqTotal = _RsHAPeerSystemStreamReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 6),
    _RsHAPeerSystemStreamReqTotal_Type()
)
rsHAPeerSystemStreamReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemStreamReqTotal.setStatus("current")
_RsHAPeerSystemStreamReqDrop_Type = Counter64
_RsHAPeerSystemStreamReqDrop_Object = MibScalar
rsHAPeerSystemStreamReqDrop = _RsHAPeerSystemStreamReqDrop_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 7),
    _RsHAPeerSystemStreamReqDrop_Type()
)
rsHAPeerSystemStreamReqDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemStreamReqDrop.setStatus("current")
_RsHAPeerSystemCurrIpsecTunnels_Type = Counter64
_RsHAPeerSystemCurrIpsecTunnels_Object = MibScalar
rsHAPeerSystemCurrIpsecTunnels = _RsHAPeerSystemCurrIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 8),
    _RsHAPeerSystemCurrIpsecTunnels_Type()
)
rsHAPeerSystemCurrIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemCurrIpsecTunnels.setStatus("current")
_RsHAPeerSystemCpuUtil1_Type = Gauge32
_RsHAPeerSystemCpuUtil1_Object = MibScalar
rsHAPeerSystemCpuUtil1 = _RsHAPeerSystemCpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 9),
    _RsHAPeerSystemCpuUtil1_Type()
)
rsHAPeerSystemCpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemCpuUtil1.setStatus("current")
_RsHAPeerSystemCpuUtil5_Type = Gauge32
_RsHAPeerSystemCpuUtil5_Object = MibScalar
rsHAPeerSystemCpuUtil5 = _RsHAPeerSystemCpuUtil5_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 10),
    _RsHAPeerSystemCpuUtil5_Type()
)
rsHAPeerSystemCpuUtil5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemCpuUtil5.setStatus("current")
_RsHAPeerSystemCpuUtil15_Type = Gauge32
_RsHAPeerSystemCpuUtil15_Object = MibScalar
rsHAPeerSystemCpuUtil15 = _RsHAPeerSystemCpuUtil15_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 11),
    _RsHAPeerSystemCpuUtil15_Type()
)
rsHAPeerSystemCpuUtil15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHAPeerSystemCpuUtil15.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-HA-MIB",
    **{"rsInfoModule": rsInfoModule,
       "rsHAMIB": rsHAMIB,
       "rsHALocal": rsHALocal,
       "rsHAStatus": rsHAStatus,
       "rsHAPeerStatus": rsHAPeerStatus,
       "rsHALastDBSyncTime": rsHALastDBSyncTime,
       "rsHAError": rsHAError,
       "rsHAPeerError": rsHAPeerError,
       "rsHAPeer": rsHAPeer,
       "rsHAPeerSerialNumber": rsHAPeerSerialNumber,
       "rsHAPeerLastDBSyncTime": rsHAPeerLastDBSyncTime,
       "rsHAPeerDevice": rsHAPeerDevice,
       "rsHAPeerIfNumber": rsHAPeerIfNumber,
       "rsHAPeerIfTable": rsHAPeerIfTable,
       "rsHAPeerIfEntry": rsHAPeerIfEntry,
       "rsHAPeerIfIndex": rsHAPeerIfIndex,
       "rsHAPeerIfIpAddr": rsHAPeerIfIpAddr,
       "rsHAPeerIfLinkStatus": rsHAPeerIfLinkStatus,
       "rsHAPeerCounters": rsHAPeerCounters,
       "rsHAPeerSystemCpuUtil": rsHAPeerSystemCpuUtil,
       "rsHAPeerSystemTotalSendBytes": rsHAPeerSystemTotalSendBytes,
       "rsHAPeerSystemTotalRecvBytes": rsHAPeerSystemTotalRecvBytes,
       "rsHAPeerSystemTotalSendPackets": rsHAPeerSystemTotalSendPackets,
       "rsHAPeerSystemTotalRecvPackets": rsHAPeerSystemTotalRecvPackets,
       "rsHAPeerSystemStreamReqTotal": rsHAPeerSystemStreamReqTotal,
       "rsHAPeerSystemStreamReqDrop": rsHAPeerSystemStreamReqDrop,
       "rsHAPeerSystemCurrIpsecTunnels": rsHAPeerSystemCurrIpsecTunnels,
       "rsHAPeerSystemCpuUtil1": rsHAPeerSystemCpuUtil1,
       "rsHAPeerSystemCpuUtil5": rsHAPeerSystemCpuUtil5,
       "rsHAPeerSystemCpuUtil15": rsHAPeerSystemCpuUtil15}
)
