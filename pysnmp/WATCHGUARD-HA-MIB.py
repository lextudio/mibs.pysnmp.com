# SNMP MIB module (WATCHGUARD-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-HA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:32 2024
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

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgHAMIB_ObjectIdentity = ObjectIdentity
wgHAMIB = _WgHAMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6)
)
if mibBuilder.loadTexts:
    wgHAMIB.setStatus("current")
_WgHALocal_ObjectIdentity = ObjectIdentity
wgHALocal = _WgHALocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1)
)
if mibBuilder.loadTexts:
    wgHALocal.setStatus("current")


class _WgHAStatus_Type(Integer32):
    """Custom type wgHAStatus based on Integer32"""
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


_WgHAStatus_Type.__name__ = "Integer32"
_WgHAStatus_Object = MibScalar
wgHAStatus = _WgHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1, 1),
    _WgHAStatus_Type()
)
wgHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAStatus.setStatus("current")


class _WgHAPeerStatus_Type(Integer32):
    """Custom type wgHAPeerStatus based on Integer32"""
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


_WgHAPeerStatus_Type.__name__ = "Integer32"
_WgHAPeerStatus_Object = MibScalar
wgHAPeerStatus = _WgHAPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1, 2),
    _WgHAPeerStatus_Type()
)
wgHAPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerStatus.setStatus("current")
_WgHALastDBSyncTime_Type = DateAndTime
_WgHALastDBSyncTime_Object = MibScalar
wgHALastDBSyncTime = _WgHALastDBSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1, 3),
    _WgHALastDBSyncTime_Type()
)
wgHALastDBSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHALastDBSyncTime.setStatus("current")


class _WgHAError_Type(Integer32):
    """Custom type wgHAError based on Integer32"""
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


_WgHAError_Type.__name__ = "Integer32"
_WgHAError_Object = MibScalar
wgHAError = _WgHAError_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1, 4),
    _WgHAError_Type()
)
wgHAError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAError.setStatus("current")


class _WgHAPeerError_Type(Integer32):
    """Custom type wgHAPeerError based on Integer32"""
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


_WgHAPeerError_Type.__name__ = "Integer32"
_WgHAPeerError_Object = MibScalar
wgHAPeerError = _WgHAPeerError_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 1, 5),
    _WgHAPeerError_Type()
)
wgHAPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerError.setStatus("current")
_WgHAPeer_ObjectIdentity = ObjectIdentity
wgHAPeer = _WgHAPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2)
)
if mibBuilder.loadTexts:
    wgHAPeer.setStatus("current")
_WgHAPeerSerialNumber_Type = OctetString
_WgHAPeerSerialNumber_Object = MibScalar
wgHAPeerSerialNumber = _WgHAPeerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 1),
    _WgHAPeerSerialNumber_Type()
)
wgHAPeerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSerialNumber.setStatus("current")
_WgHAPeerLastDBSyncTime_Type = DateAndTime
_WgHAPeerLastDBSyncTime_Object = MibScalar
wgHAPeerLastDBSyncTime = _WgHAPeerLastDBSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 2),
    _WgHAPeerLastDBSyncTime_Type()
)
wgHAPeerLastDBSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerLastDBSyncTime.setStatus("current")
_WgHAPeerDevice_ObjectIdentity = ObjectIdentity
wgHAPeerDevice = _WgHAPeerDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wgHAPeerDevice.setStatus("current")
_WgHAPeerIfNumber_Type = Unsigned32
_WgHAPeerIfNumber_Object = MibScalar
wgHAPeerIfNumber = _WgHAPeerIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 1),
    _WgHAPeerIfNumber_Type()
)
wgHAPeerIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerIfNumber.setStatus("current")
_WgHAPeerIfTable_Object = MibTable
wgHAPeerIfTable = _WgHAPeerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wgHAPeerIfTable.setStatus("current")
_WgHAPeerIfEntry_Object = MibTableRow
wgHAPeerIfEntry = _WgHAPeerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 2, 1)
)
wgHAPeerIfEntry.setIndexNames(
    (0, "WATCHGUARD-HA-MIB", "wgHAPeerIfIndex"),
)
if mibBuilder.loadTexts:
    wgHAPeerIfEntry.setStatus("current")
_WgHAPeerIfIndex_Type = Unsigned32
_WgHAPeerIfIndex_Object = MibTableColumn
wgHAPeerIfIndex = _WgHAPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 2, 1, 1),
    _WgHAPeerIfIndex_Type()
)
wgHAPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerIfIndex.setStatus("current")
_WgHAPeerIfIpAddr_Type = IpAddress
_WgHAPeerIfIpAddr_Object = MibTableColumn
wgHAPeerIfIpAddr = _WgHAPeerIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 2, 1, 4),
    _WgHAPeerIfIpAddr_Type()
)
wgHAPeerIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerIfIpAddr.setStatus("current")


class _WgHAPeerIfLinkStatus_Type(Integer32):
    """Custom type wgHAPeerIfLinkStatus based on Integer32"""
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


_WgHAPeerIfLinkStatus_Type.__name__ = "Integer32"
_WgHAPeerIfLinkStatus_Object = MibTableColumn
wgHAPeerIfLinkStatus = _WgHAPeerIfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 3, 2, 1, 9),
    _WgHAPeerIfLinkStatus_Type()
)
wgHAPeerIfLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerIfLinkStatus.setStatus("current")
_WgHAPeerCounters_ObjectIdentity = ObjectIdentity
wgHAPeerCounters = _WgHAPeerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4)
)
if mibBuilder.loadTexts:
    wgHAPeerCounters.setStatus("current")
_WgHAPeerSystemCpuUtil_Type = Gauge32
_WgHAPeerSystemCpuUtil_Object = MibScalar
wgHAPeerSystemCpuUtil = _WgHAPeerSystemCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 1),
    _WgHAPeerSystemCpuUtil_Type()
)
wgHAPeerSystemCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemCpuUtil.setStatus("current")
_WgHAPeerSystemTotalSendBytes_Type = Counter64
_WgHAPeerSystemTotalSendBytes_Object = MibScalar
wgHAPeerSystemTotalSendBytes = _WgHAPeerSystemTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 2),
    _WgHAPeerSystemTotalSendBytes_Type()
)
wgHAPeerSystemTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemTotalSendBytes.setStatus("current")
_WgHAPeerSystemTotalRecvBytes_Type = Counter64
_WgHAPeerSystemTotalRecvBytes_Object = MibScalar
wgHAPeerSystemTotalRecvBytes = _WgHAPeerSystemTotalRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 3),
    _WgHAPeerSystemTotalRecvBytes_Type()
)
wgHAPeerSystemTotalRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemTotalRecvBytes.setStatus("current")
_WgHAPeerSystemTotalSendPackets_Type = Counter64
_WgHAPeerSystemTotalSendPackets_Object = MibScalar
wgHAPeerSystemTotalSendPackets = _WgHAPeerSystemTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 4),
    _WgHAPeerSystemTotalSendPackets_Type()
)
wgHAPeerSystemTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemTotalSendPackets.setStatus("current")
_WgHAPeerSystemTotalRecvPackets_Type = Counter64
_WgHAPeerSystemTotalRecvPackets_Object = MibScalar
wgHAPeerSystemTotalRecvPackets = _WgHAPeerSystemTotalRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 5),
    _WgHAPeerSystemTotalRecvPackets_Type()
)
wgHAPeerSystemTotalRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemTotalRecvPackets.setStatus("current")
_WgHAPeerSystemStreamReqTotal_Type = Counter64
_WgHAPeerSystemStreamReqTotal_Object = MibScalar
wgHAPeerSystemStreamReqTotal = _WgHAPeerSystemStreamReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 6),
    _WgHAPeerSystemStreamReqTotal_Type()
)
wgHAPeerSystemStreamReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemStreamReqTotal.setStatus("current")
_WgHAPeerSystemStreamReqDrop_Type = Counter64
_WgHAPeerSystemStreamReqDrop_Object = MibScalar
wgHAPeerSystemStreamReqDrop = _WgHAPeerSystemStreamReqDrop_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 7),
    _WgHAPeerSystemStreamReqDrop_Type()
)
wgHAPeerSystemStreamReqDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemStreamReqDrop.setStatus("current")
_WgHAPeerSystemCurrIpsecTunnels_Type = Counter64
_WgHAPeerSystemCurrIpsecTunnels_Object = MibScalar
wgHAPeerSystemCurrIpsecTunnels = _WgHAPeerSystemCurrIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 8),
    _WgHAPeerSystemCurrIpsecTunnels_Type()
)
wgHAPeerSystemCurrIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemCurrIpsecTunnels.setStatus("current")
_WgHAPeerSystemCpuUtil1_Type = Gauge32
_WgHAPeerSystemCpuUtil1_Object = MibScalar
wgHAPeerSystemCpuUtil1 = _WgHAPeerSystemCpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 9),
    _WgHAPeerSystemCpuUtil1_Type()
)
wgHAPeerSystemCpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemCpuUtil1.setStatus("current")
_WgHAPeerSystemCpuUtil5_Type = Gauge32
_WgHAPeerSystemCpuUtil5_Object = MibScalar
wgHAPeerSystemCpuUtil5 = _WgHAPeerSystemCpuUtil5_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 10),
    _WgHAPeerSystemCpuUtil5_Type()
)
wgHAPeerSystemCpuUtil5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemCpuUtil5.setStatus("current")
_WgHAPeerSystemCpuUtil15_Type = Gauge32
_WgHAPeerSystemCpuUtil15_Object = MibScalar
wgHAPeerSystemCpuUtil15 = _WgHAPeerSystemCpuUtil15_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 6, 2, 4, 11),
    _WgHAPeerSystemCpuUtil15_Type()
)
wgHAPeerSystemCpuUtil15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgHAPeerSystemCpuUtil15.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-HA-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgHAMIB": wgHAMIB,
       "wgHALocal": wgHALocal,
       "wgHAStatus": wgHAStatus,
       "wgHAPeerStatus": wgHAPeerStatus,
       "wgHALastDBSyncTime": wgHALastDBSyncTime,
       "wgHAError": wgHAError,
       "wgHAPeerError": wgHAPeerError,
       "wgHAPeer": wgHAPeer,
       "wgHAPeerSerialNumber": wgHAPeerSerialNumber,
       "wgHAPeerLastDBSyncTime": wgHAPeerLastDBSyncTime,
       "wgHAPeerDevice": wgHAPeerDevice,
       "wgHAPeerIfNumber": wgHAPeerIfNumber,
       "wgHAPeerIfTable": wgHAPeerIfTable,
       "wgHAPeerIfEntry": wgHAPeerIfEntry,
       "wgHAPeerIfIndex": wgHAPeerIfIndex,
       "wgHAPeerIfIpAddr": wgHAPeerIfIpAddr,
       "wgHAPeerIfLinkStatus": wgHAPeerIfLinkStatus,
       "wgHAPeerCounters": wgHAPeerCounters,
       "wgHAPeerSystemCpuUtil": wgHAPeerSystemCpuUtil,
       "wgHAPeerSystemTotalSendBytes": wgHAPeerSystemTotalSendBytes,
       "wgHAPeerSystemTotalRecvBytes": wgHAPeerSystemTotalRecvBytes,
       "wgHAPeerSystemTotalSendPackets": wgHAPeerSystemTotalSendPackets,
       "wgHAPeerSystemTotalRecvPackets": wgHAPeerSystemTotalRecvPackets,
       "wgHAPeerSystemStreamReqTotal": wgHAPeerSystemStreamReqTotal,
       "wgHAPeerSystemStreamReqDrop": wgHAPeerSystemStreamReqDrop,
       "wgHAPeerSystemCurrIpsecTunnels": wgHAPeerSystemCurrIpsecTunnels,
       "wgHAPeerSystemCpuUtil1": wgHAPeerSystemCpuUtil1,
       "wgHAPeerSystemCpuUtil5": wgHAPeerSystemCpuUtil5,
       "wgHAPeerSystemCpuUtil15": wgHAPeerSystemCpuUtil15}
)
