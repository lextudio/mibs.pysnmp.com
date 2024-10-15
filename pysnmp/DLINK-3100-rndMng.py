# SNMP MIB module (DLINK-3100-rndMng) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-rndMng
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:37 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rndMng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1)
)
rndMng.setRevisions(
        ("2009-02-24 00:00",
         "2007-10-24 00:00",
         "2006-06-20 00:00",
         "2004-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RndSysId_Type = Integer32
_RndSysId_Object = MibScalar
rndSysId = _RndSysId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 1),
    _RndSysId_Type()
)
rndSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSysId.setStatus("current")


class _RndAction_Type(Integer32):
    """Custom type rndAction based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("backupArpTab", 16),
          ("backupIPRoutingTab", 13),
          ("backupIPXRipTab", 17),
          ("backupIPXSAPTab", 18),
          ("backupLanTab", 15),
          ("backupNetworkTab", 14),
          ("backupSPFRoutingTab", 12),
          ("copyStartupToRunning", 25),
          ("deleteArpTab", 8),
          ("deleteDynamicLanTab", 23),
          ("deleteLanTab", 7),
          ("deleteNetworkTab", 3),
          ("deleteRouteTab", 10),
          ("deleteRoutingTab", 5),
          ("deleteZeroHopRoutingAllocTab", 21),
          ("eraseRunningCDB", 24),
          ("eraseStartupCDB", 20),
          ("none", 26),
          ("reset", 1),
          ("resetStartupCDB", 19),
          ("resetToFactoryDefaults", 27),
          ("sendArpTab", 9),
          ("sendLanTab", 6),
          ("sendNetworkTab", 2),
          ("sendRouteTab", 11),
          ("sendRoutingTab", 4),
          ("slipDisconnect", 22))
    )


_RndAction_Type.__name__ = "Integer32"
_RndAction_Object = MibScalar
rndAction = _RndAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 2),
    _RndAction_Type()
)
rndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAction.setStatus("current")
_RndFileName_Type = OctetString
_RndFileName_Object = MibScalar
rndFileName = _RndFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 3),
    _RndFileName_Type()
)
rndFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFileName.setStatus("current")


class _RlSnmpVersionSupported_Type(OctetString):
    """Custom type rlSnmpVersionSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlSnmpVersionSupported_Type.__name__ = "OctetString"
_RlSnmpVersionSupported_Object = MibScalar
rlSnmpVersionSupported = _RlSnmpVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 4),
    _RlSnmpVersionSupported_Type()
)
rlSnmpVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpVersionSupported.setStatus("current")
_RlSnmpMibVersion_Type = Integer32
_RlSnmpMibVersion_Object = MibScalar
rlSnmpMibVersion = _RlSnmpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 5),
    _RlSnmpMibVersion_Type()
)
rlSnmpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpMibVersion.setStatus("current")


class _RlCpuUtilEnable_Type(TruthValue):
    """Custom type rlCpuUtilEnable based on TruthValue"""


_RlCpuUtilEnable_Object = MibScalar
rlCpuUtilEnable = _RlCpuUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 6),
    _RlCpuUtilEnable_Type()
)
rlCpuUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCpuUtilEnable.setStatus("current")


class _RlCpuUtilDuringLastSecond_Type(Integer32):
    """Custom type rlCpuUtilDuringLastSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLastSecond_Type.__name__ = "Integer32"
_RlCpuUtilDuringLastSecond_Object = MibScalar
rlCpuUtilDuringLastSecond = _RlCpuUtilDuringLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 7),
    _RlCpuUtilDuringLastSecond_Type()
)
rlCpuUtilDuringLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLastSecond.setStatus("current")


class _RlCpuUtilDuringLastMinute_Type(Integer32):
    """Custom type rlCpuUtilDuringLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLastMinute_Type.__name__ = "Integer32"
_RlCpuUtilDuringLastMinute_Object = MibScalar
rlCpuUtilDuringLastMinute = _RlCpuUtilDuringLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 8),
    _RlCpuUtilDuringLastMinute_Type()
)
rlCpuUtilDuringLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLastMinute.setStatus("current")


class _RlCpuUtilDuringLast5Minutes_Type(Integer32):
    """Custom type rlCpuUtilDuringLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_RlCpuUtilDuringLast5Minutes_Type.__name__ = "Integer32"
_RlCpuUtilDuringLast5Minutes_Object = MibScalar
rlCpuUtilDuringLast5Minutes = _RlCpuUtilDuringLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 9),
    _RlCpuUtilDuringLast5Minutes_Type()
)
rlCpuUtilDuringLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCpuUtilDuringLast5Minutes.setStatus("current")
_RlRebootDelay_Type = TimeTicks
_RlRebootDelay_Object = MibScalar
rlRebootDelay = _RlRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 10),
    _RlRebootDelay_Type()
)
rlRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRebootDelay.setStatus("current")
_RlGroupManagement_ObjectIdentity = ObjectIdentity
rlGroupManagement = _RlGroupManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11)
)


class _RlGroupMngQuery_Type(Integer32):
    """Custom type rlGroupMngQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("query", 1))
    )


_RlGroupMngQuery_Type.__name__ = "Integer32"
_RlGroupMngQuery_Object = MibScalar
rlGroupMngQuery = _RlGroupMngQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 1),
    _RlGroupMngQuery_Type()
)
rlGroupMngQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGroupMngQuery.setStatus("current")


class _RlGroupMngQueryPeriod_Type(Integer32):
    """Custom type rlGroupMngQueryPeriod based on Integer32"""
    defaultValue = 0


_RlGroupMngQueryPeriod_Object = MibScalar
rlGroupMngQueryPeriod = _RlGroupMngQueryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 2),
    _RlGroupMngQueryPeriod_Type()
)
rlGroupMngQueryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGroupMngQueryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngQueryPeriod.setUnits("seconds")
_RlGroupMngLastUpdate_Type = TimeTicks
_RlGroupMngLastUpdate_Object = MibScalar
rlGroupMngLastUpdate = _RlGroupMngLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 3),
    _RlGroupMngLastUpdate_Type()
)
rlGroupMngLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngLastUpdate.setStatus("current")
_RlGroupMngDevicesTable_Object = MibTable
rlGroupMngDevicesTable = _RlGroupMngDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4)
)
if mibBuilder.loadTexts:
    rlGroupMngDevicesTable.setStatus("current")
_RlGroupMngDeviceEntry_Object = MibTableRow
rlGroupMngDeviceEntry = _RlGroupMngDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1)
)
rlGroupMngDeviceEntry.setIndexNames(
    (0, "DLINK-3100-rndMng", "rlGroupMngDeviceIdType"),
    (0, "DLINK-3100-rndMng", "rlGroupMngDeviceId"),
    (0, "DLINK-3100-rndMng", "rlGroupMngSubdevice"),
)
if mibBuilder.loadTexts:
    rlGroupMngDeviceEntry.setStatus("current")
_RlGroupMngDeviceIdType_Type = InetAddressType
_RlGroupMngDeviceIdType_Object = MibTableColumn
rlGroupMngDeviceIdType = _RlGroupMngDeviceIdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 1),
    _RlGroupMngDeviceIdType_Type()
)
rlGroupMngDeviceIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngDeviceIdType.setStatus("current")
_RlGroupMngDeviceId_Type = InetAddress
_RlGroupMngDeviceId_Object = MibTableColumn
rlGroupMngDeviceId = _RlGroupMngDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 2),
    _RlGroupMngDeviceId_Type()
)
rlGroupMngDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngDeviceId.setStatus("current")
_RlGroupMngSubdevice_Type = Integer32
_RlGroupMngSubdevice_Object = MibTableColumn
rlGroupMngSubdevice = _RlGroupMngSubdevice_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 3),
    _RlGroupMngSubdevice_Type()
)
rlGroupMngSubdevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGroupMngSubdevice.setStatus("current")
_RlGroupMngDeviceDescription_Type = DisplayString
_RlGroupMngDeviceDescription_Object = MibTableColumn
rlGroupMngDeviceDescription = _RlGroupMngDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 4),
    _RlGroupMngDeviceDescription_Type()
)
rlGroupMngDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceDescription.setStatus("current")
_RlGroupMngGroupMngEnabled_Type = TruthValue
_RlGroupMngGroupMngEnabled_Object = MibTableColumn
rlGroupMngGroupMngEnabled = _RlGroupMngGroupMngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 5),
    _RlGroupMngGroupMngEnabled_Type()
)
rlGroupMngGroupMngEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngGroupMngEnabled.setStatus("current")
_RlGroupMngGroupLLDPDeviceId_Type = DisplayString
_RlGroupMngGroupLLDPDeviceId_Object = MibTableColumn
rlGroupMngGroupLLDPDeviceId = _RlGroupMngGroupLLDPDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 6),
    _RlGroupMngGroupLLDPDeviceId_Type()
)
rlGroupMngGroupLLDPDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngGroupLLDPDeviceId.setStatus("current")
_RlGroupMngDeviceVendor_Type = DisplayString
_RlGroupMngDeviceVendor_Object = MibTableColumn
rlGroupMngDeviceVendor = _RlGroupMngDeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 7),
    _RlGroupMngDeviceVendor_Type()
)
rlGroupMngDeviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceVendor.setStatus("current")
_RlGroupMngDeviceAdvertisedCachingTime_Type = Integer32
_RlGroupMngDeviceAdvertisedCachingTime_Object = MibTableColumn
rlGroupMngDeviceAdvertisedCachingTime = _RlGroupMngDeviceAdvertisedCachingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 8),
    _RlGroupMngDeviceAdvertisedCachingTime_Type()
)
rlGroupMngDeviceAdvertisedCachingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceAdvertisedCachingTime.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngDeviceAdvertisedCachingTime.setUnits("seconds")
_RlGroupMngDeviceLocationURL_Type = DisplayString
_RlGroupMngDeviceLocationURL_Object = MibTableColumn
rlGroupMngDeviceLocationURL = _RlGroupMngDeviceLocationURL_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 9),
    _RlGroupMngDeviceLocationURL_Type()
)
rlGroupMngDeviceLocationURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLocationURL.setStatus("current")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLocationURL.setUnits("seconds")
_RlGroupMngDeviceLastSeen_Type = TimeTicks
_RlGroupMngDeviceLastSeen_Object = MibTableColumn
rlGroupMngDeviceLastSeen = _RlGroupMngDeviceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 11, 4, 1, 10),
    _RlGroupMngDeviceLastSeen_Type()
)
rlGroupMngDeviceLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGroupMngDeviceLastSeen.setStatus("current")
_RlRunningCDBequalToStartupCDB_Type = TruthValue
_RlRunningCDBequalToStartupCDB_Object = MibScalar
rlRunningCDBequalToStartupCDB = _RlRunningCDBequalToStartupCDB_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 1, 13),
    _RlRunningCDBequalToStartupCDB_Type()
)
rlRunningCDBequalToStartupCDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRunningCDBequalToStartupCDB.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-rndMng",
    **{"rndMng": rndMng,
       "rndSysId": rndSysId,
       "rndAction": rndAction,
       "rndFileName": rndFileName,
       "rlSnmpVersionSupported": rlSnmpVersionSupported,
       "rlSnmpMibVersion": rlSnmpMibVersion,
       "rlCpuUtilEnable": rlCpuUtilEnable,
       "rlCpuUtilDuringLastSecond": rlCpuUtilDuringLastSecond,
       "rlCpuUtilDuringLastMinute": rlCpuUtilDuringLastMinute,
       "rlCpuUtilDuringLast5Minutes": rlCpuUtilDuringLast5Minutes,
       "rlRebootDelay": rlRebootDelay,
       "rlGroupManagement": rlGroupManagement,
       "rlGroupMngQuery": rlGroupMngQuery,
       "rlGroupMngQueryPeriod": rlGroupMngQueryPeriod,
       "rlGroupMngLastUpdate": rlGroupMngLastUpdate,
       "rlGroupMngDevicesTable": rlGroupMngDevicesTable,
       "rlGroupMngDeviceEntry": rlGroupMngDeviceEntry,
       "rlGroupMngDeviceIdType": rlGroupMngDeviceIdType,
       "rlGroupMngDeviceId": rlGroupMngDeviceId,
       "rlGroupMngSubdevice": rlGroupMngSubdevice,
       "rlGroupMngDeviceDescription": rlGroupMngDeviceDescription,
       "rlGroupMngGroupMngEnabled": rlGroupMngGroupMngEnabled,
       "rlGroupMngGroupLLDPDeviceId": rlGroupMngGroupLLDPDeviceId,
       "rlGroupMngDeviceVendor": rlGroupMngDeviceVendor,
       "rlGroupMngDeviceAdvertisedCachingTime": rlGroupMngDeviceAdvertisedCachingTime,
       "rlGroupMngDeviceLocationURL": rlGroupMngDeviceLocationURL,
       "rlGroupMngDeviceLastSeen": rlGroupMngDeviceLastSeen,
       "rlRunningCDBequalToStartupCDB": rlRunningCDBequalToStartupCDB}
)
