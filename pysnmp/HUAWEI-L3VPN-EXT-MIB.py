# SNMP MIB module (HUAWEI-L3VPN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L3VPN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:29 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hwL3vpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL3vpnStatMibObjects_ObjectIdentity = ObjectIdentity
hwL3vpnStatMibObjects = _HwL3vpnStatMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1)
)
_HwL3vpnStatisticsTable_Object = MibTable
hwL3vpnStatisticsTable = _HwL3vpnStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1)
)
if mibBuilder.loadTexts:
    hwL3vpnStatisticsTable.setStatus("current")
_HwL3vpnStatisticsEntry_Object = MibTableRow
hwL3vpnStatisticsEntry = _HwL3vpnStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1)
)
hwL3vpnStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnVrfIndex"),
)
if mibBuilder.loadTexts:
    hwL3vpnStatisticsEntry.setStatus("current")
_HwL3vpnVrfIndex_Type = Unsigned32
_HwL3vpnVrfIndex_Object = MibTableColumn
hwL3vpnVrfIndex = _HwL3vpnVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 1),
    _HwL3vpnVrfIndex_Type()
)
hwL3vpnVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnVrfIndex.setStatus("current")


class _HwL3vpnStatEnable_Type(EnabledStatus):
    """Custom type hwL3vpnStatEnable based on EnabledStatus"""


_HwL3vpnStatEnable_Object = MibTableColumn
hwL3vpnStatEnable = _HwL3vpnStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 2),
    _HwL3vpnStatEnable_Type()
)
hwL3vpnStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL3vpnStatEnable.setStatus("current")


class _HwL3vpnVrfName_Type(DisplayString):
    """Custom type hwL3vpnVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL3vpnVrfName_Type.__name__ = "DisplayString"
_HwL3vpnVrfName_Object = MibTableColumn
hwL3vpnVrfName = _HwL3vpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 3),
    _HwL3vpnVrfName_Type()
)
hwL3vpnVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnVrfName.setStatus("current")
_HwL3vpnStatInTrafficRate_Type = Gauge32
_HwL3vpnStatInTrafficRate_Object = MibTableColumn
hwL3vpnStatInTrafficRate = _HwL3vpnStatInTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 4),
    _HwL3vpnStatInTrafficRate_Type()
)
hwL3vpnStatInTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInTrafficRate.setStatus("current")
_HwL3vpnStatOutTrafficRate_Type = Gauge32
_HwL3vpnStatOutTrafficRate_Object = MibTableColumn
hwL3vpnStatOutTrafficRate = _HwL3vpnStatOutTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 5),
    _HwL3vpnStatOutTrafficRate_Type()
)
hwL3vpnStatOutTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutTrafficRate.setStatus("current")
_HwL3vpnStatInPacketsRate_Type = Gauge32
_HwL3vpnStatInPacketsRate_Object = MibTableColumn
hwL3vpnStatInPacketsRate = _HwL3vpnStatInPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 6),
    _HwL3vpnStatInPacketsRate_Type()
)
hwL3vpnStatInPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInPacketsRate.setStatus("current")
_HwL3vpnStatOutPacketsRate_Type = Gauge32
_HwL3vpnStatOutPacketsRate_Object = MibTableColumn
hwL3vpnStatOutPacketsRate = _HwL3vpnStatOutPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 7),
    _HwL3vpnStatOutPacketsRate_Type()
)
hwL3vpnStatOutPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutPacketsRate.setStatus("current")
_HwL3vpnStatInBytes_Type = Counter64
_HwL3vpnStatInBytes_Object = MibTableColumn
hwL3vpnStatInBytes = _HwL3vpnStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 8),
    _HwL3vpnStatInBytes_Type()
)
hwL3vpnStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInBytes.setStatus("current")
_HwL3vpnStatOutBytes_Type = Counter64
_HwL3vpnStatOutBytes_Object = MibTableColumn
hwL3vpnStatOutBytes = _HwL3vpnStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 9),
    _HwL3vpnStatOutBytes_Type()
)
hwL3vpnStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutBytes.setStatus("current")
_HwL3vpnStatInPackets_Type = Counter64
_HwL3vpnStatInPackets_Object = MibTableColumn
hwL3vpnStatInPackets = _HwL3vpnStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 10),
    _HwL3vpnStatInPackets_Type()
)
hwL3vpnStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInPackets.setStatus("current")
_HwL3vpnStatOutPackets_Type = Counter64
_HwL3vpnStatOutPackets_Object = MibTableColumn
hwL3vpnStatOutPackets = _HwL3vpnStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 11),
    _HwL3vpnStatOutPackets_Type()
)
hwL3vpnStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutPackets.setStatus("current")
_HwL3vpnStatInUnicastPackets_Type = Counter64
_HwL3vpnStatInUnicastPackets_Object = MibTableColumn
hwL3vpnStatInUnicastPackets = _HwL3vpnStatInUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 12),
    _HwL3vpnStatInUnicastPackets_Type()
)
hwL3vpnStatInUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInUnicastPackets.setStatus("current")
_HwL3vpnStatOutUnicastPackets_Type = Counter64
_HwL3vpnStatOutUnicastPackets_Object = MibTableColumn
hwL3vpnStatOutUnicastPackets = _HwL3vpnStatOutUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 13),
    _HwL3vpnStatOutUnicastPackets_Type()
)
hwL3vpnStatOutUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutUnicastPackets.setStatus("current")
_HwL3vpnStatInMulticastPackets_Type = Counter64
_HwL3vpnStatInMulticastPackets_Object = MibTableColumn
hwL3vpnStatInMulticastPackets = _HwL3vpnStatInMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 14),
    _HwL3vpnStatInMulticastPackets_Type()
)
hwL3vpnStatInMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInMulticastPackets.setStatus("current")
_HwL3vpnStatOutMulticastPackets_Type = Counter64
_HwL3vpnStatOutMulticastPackets_Object = MibTableColumn
hwL3vpnStatOutMulticastPackets = _HwL3vpnStatOutMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 15),
    _HwL3vpnStatOutMulticastPackets_Type()
)
hwL3vpnStatOutMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutMulticastPackets.setStatus("current")
_HwL3vpnStatInBroadcastPackets_Type = Counter64
_HwL3vpnStatInBroadcastPackets_Object = MibTableColumn
hwL3vpnStatInBroadcastPackets = _HwL3vpnStatInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 16),
    _HwL3vpnStatInBroadcastPackets_Type()
)
hwL3vpnStatInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatInBroadcastPackets.setStatus("current")
_HwL3vpnStatOutBroadcastPackets_Type = Counter64
_HwL3vpnStatOutBroadcastPackets_Object = MibTableColumn
hwL3vpnStatOutBroadcastPackets = _HwL3vpnStatOutBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 17),
    _HwL3vpnStatOutBroadcastPackets_Type()
)
hwL3vpnStatOutBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatOutBroadcastPackets.setStatus("current")
_HwL3vpnStatResetTime_Type = DateAndTime
_HwL3vpnStatResetTime_Object = MibTableColumn
hwL3vpnStatResetTime = _HwL3vpnStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 18),
    _HwL3vpnStatResetTime_Type()
)
hwL3vpnStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatResetTime.setStatus("current")


class _HwL3vpnStatResetStatistic_Type(Integer32):
    """Custom type hwL3vpnStatResetStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistic", 1)
    )


_HwL3vpnStatResetStatistic_Type.__name__ = "Integer32"
_HwL3vpnStatResetStatistic_Object = MibTableColumn
hwL3vpnStatResetStatistic = _HwL3vpnStatResetStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 1, 1, 19),
    _HwL3vpnStatResetStatistic_Type()
)
hwL3vpnStatResetStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL3vpnStatResetStatistic.setStatus("current")
_HwL3vpnQosStatisticsTable_Object = MibTable
hwL3vpnQosStatisticsTable = _HwL3vpnQosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2)
)
if mibBuilder.loadTexts:
    hwL3vpnQosStatisticsTable.setStatus("current")
_HwL3vpnQosStatisticsEntry_Object = MibTableRow
hwL3vpnQosStatisticsEntry = _HwL3vpnQosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1)
)
hwL3vpnQosStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatVrfIndex"),
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatQueueID"),
)
if mibBuilder.loadTexts:
    hwL3vpnQosStatisticsEntry.setStatus("current")
_HwL3vpnQosStatVrfIndex_Type = Unsigned32
_HwL3vpnQosStatVrfIndex_Object = MibTableColumn
hwL3vpnQosStatVrfIndex = _HwL3vpnQosStatVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 1),
    _HwL3vpnQosStatVrfIndex_Type()
)
hwL3vpnQosStatVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnQosStatVrfIndex.setStatus("current")


class _HwL3vpnQosStatQueueID_Type(Integer32):
    """Custom type hwL3vpnQosStatQueueID based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwL3vpnQosStatQueueID_Type.__name__ = "Integer32"
_HwL3vpnQosStatQueueID_Object = MibTableColumn
hwL3vpnQosStatQueueID = _HwL3vpnQosStatQueueID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 2),
    _HwL3vpnQosStatQueueID_Type()
)
hwL3vpnQosStatQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnQosStatQueueID.setStatus("current")
_HwL3vpnQosStatPassPackets_Type = Counter64
_HwL3vpnQosStatPassPackets_Object = MibTableColumn
hwL3vpnQosStatPassPackets = _HwL3vpnQosStatPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 3),
    _HwL3vpnQosStatPassPackets_Type()
)
hwL3vpnQosStatPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatPassPackets.setStatus("current")
_HwL3vpnQosStatPassBytes_Type = Counter64
_HwL3vpnQosStatPassBytes_Object = MibTableColumn
hwL3vpnQosStatPassBytes = _HwL3vpnQosStatPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 4),
    _HwL3vpnQosStatPassBytes_Type()
)
hwL3vpnQosStatPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatPassBytes.setStatus("current")
_HwL3vpnQosStatDiscardPackets_Type = Counter64
_HwL3vpnQosStatDiscardPackets_Object = MibTableColumn
hwL3vpnQosStatDiscardPackets = _HwL3vpnQosStatDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 5),
    _HwL3vpnQosStatDiscardPackets_Type()
)
hwL3vpnQosStatDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatDiscardPackets.setStatus("current")
_HwL3vpnQosStatDiscardBytes_Type = Counter64
_HwL3vpnQosStatDiscardBytes_Object = MibTableColumn
hwL3vpnQosStatDiscardBytes = _HwL3vpnQosStatDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 6),
    _HwL3vpnQosStatDiscardBytes_Type()
)
hwL3vpnQosStatDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatDiscardBytes.setStatus("current")
_HwL3vpnQosStatPassPacketsRate_Type = Counter64
_HwL3vpnQosStatPassPacketsRate_Object = MibTableColumn
hwL3vpnQosStatPassPacketsRate = _HwL3vpnQosStatPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 7),
    _HwL3vpnQosStatPassPacketsRate_Type()
)
hwL3vpnQosStatPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatPassPacketsRate.setStatus("current")
_HwL3vpnQosStatPassBytesRate_Type = Counter64
_HwL3vpnQosStatPassBytesRate_Object = MibTableColumn
hwL3vpnQosStatPassBytesRate = _HwL3vpnQosStatPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 8),
    _HwL3vpnQosStatPassBytesRate_Type()
)
hwL3vpnQosStatPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatPassBytesRate.setStatus("current")
_HwL3vpnQosStatDiscardPacketsRate_Type = Counter64
_HwL3vpnQosStatDiscardPacketsRate_Object = MibTableColumn
hwL3vpnQosStatDiscardPacketsRate = _HwL3vpnQosStatDiscardPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 9),
    _HwL3vpnQosStatDiscardPacketsRate_Type()
)
hwL3vpnQosStatDiscardPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatDiscardPacketsRate.setStatus("current")
_HwL3vpnQosStatDiscardBytesRate_Type = Counter64
_HwL3vpnQosStatDiscardBytesRate_Object = MibTableColumn
hwL3vpnQosStatDiscardBytesRate = _HwL3vpnQosStatDiscardBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 2, 1, 10),
    _HwL3vpnQosStatDiscardBytesRate_Type()
)
hwL3vpnQosStatDiscardBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnQosStatDiscardBytesRate.setStatus("current")
_HwL3vpnPeerStatisticsTable_Object = MibTable
hwL3vpnPeerStatisticsTable = _HwL3vpnPeerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3)
)
if mibBuilder.loadTexts:
    hwL3vpnPeerStatisticsTable.setStatus("current")
_HwL3vpnPeerStatisticsEntry_Object = MibTableRow
hwL3vpnPeerStatisticsEntry = _HwL3vpnPeerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1)
)
hwL3vpnPeerStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerVrfIndex"),
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatPeerAddress"),
)
if mibBuilder.loadTexts:
    hwL3vpnPeerStatisticsEntry.setStatus("current")
_HwL3vpnPeerVrfIndex_Type = Unsigned32
_HwL3vpnPeerVrfIndex_Object = MibTableColumn
hwL3vpnPeerVrfIndex = _HwL3vpnPeerVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 1),
    _HwL3vpnPeerVrfIndex_Type()
)
hwL3vpnPeerVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnPeerVrfIndex.setStatus("current")
_HwL3vpnPeerStatPeerAddress_Type = IpAddress
_HwL3vpnPeerStatPeerAddress_Object = MibTableColumn
hwL3vpnPeerStatPeerAddress = _HwL3vpnPeerStatPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 2),
    _HwL3vpnPeerStatPeerAddress_Type()
)
hwL3vpnPeerStatPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatPeerAddress.setStatus("current")


class _HwL3vpnPeerStatEnable_Type(EnabledStatus):
    """Custom type hwL3vpnPeerStatEnable based on EnabledStatus"""


_HwL3vpnPeerStatEnable_Object = MibTableColumn
hwL3vpnPeerStatEnable = _HwL3vpnPeerStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 3),
    _HwL3vpnPeerStatEnable_Type()
)
hwL3vpnPeerStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatEnable.setStatus("current")


class _HwL3vpnPeerStatResetStatistic_Type(Integer32):
    """Custom type hwL3vpnPeerStatResetStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistic", 1)
    )


_HwL3vpnPeerStatResetStatistic_Type.__name__ = "Integer32"
_HwL3vpnPeerStatResetStatistic_Object = MibTableColumn
hwL3vpnPeerStatResetStatistic = _HwL3vpnPeerStatResetStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 4),
    _HwL3vpnPeerStatResetStatistic_Type()
)
hwL3vpnPeerStatResetStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatResetStatistic.setStatus("current")


class _HwL3vpnPeerVrfName_Type(DisplayString):
    """Custom type hwL3vpnPeerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL3vpnPeerVrfName_Type.__name__ = "DisplayString"
_HwL3vpnPeerVrfName_Object = MibTableColumn
hwL3vpnPeerVrfName = _HwL3vpnPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 5),
    _HwL3vpnPeerVrfName_Type()
)
hwL3vpnPeerVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerVrfName.setStatus("current")
_HwL3vpnPeerStatResetTime_Type = DateAndTime
_HwL3vpnPeerStatResetTime_Object = MibTableColumn
hwL3vpnPeerStatResetTime = _HwL3vpnPeerStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 6),
    _HwL3vpnPeerStatResetTime_Type()
)
hwL3vpnPeerStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatResetTime.setStatus("current")
_HwL3vpnPeerStatQosPacketsRate_Type = Counter64
_HwL3vpnPeerStatQosPacketsRate_Object = MibTableColumn
hwL3vpnPeerStatQosPacketsRate = _HwL3vpnPeerStatQosPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 7),
    _HwL3vpnPeerStatQosPacketsRate_Type()
)
hwL3vpnPeerStatQosPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatQosPacketsRate.setStatus("current")
_HwL3vpnPeerStatQosBytesRate_Type = Counter64
_HwL3vpnPeerStatQosBytesRate_Object = MibTableColumn
hwL3vpnPeerStatQosBytesRate = _HwL3vpnPeerStatQosBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 8),
    _HwL3vpnPeerStatQosBytesRate_Type()
)
hwL3vpnPeerStatQosBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatQosBytesRate.setStatus("current")
_HwL3vpnPeerStatQosPackets_Type = Counter64
_HwL3vpnPeerStatQosPackets_Object = MibTableColumn
hwL3vpnPeerStatQosPackets = _HwL3vpnPeerStatQosPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 9),
    _HwL3vpnPeerStatQosPackets_Type()
)
hwL3vpnPeerStatQosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatQosPackets.setStatus("current")
_HwL3vpnPeerStatQosBytes_Type = Counter64
_HwL3vpnPeerStatQosBytes_Object = MibTableColumn
hwL3vpnPeerStatQosBytes = _HwL3vpnPeerStatQosBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 3, 1, 10),
    _HwL3vpnPeerStatQosBytes_Type()
)
hwL3vpnPeerStatQosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerStatQosBytes.setStatus("current")
_HwL3vpnPeerQosStatisticsTable_Object = MibTable
hwL3vpnPeerQosStatisticsTable = _HwL3vpnPeerQosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4)
)
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatisticsTable.setStatus("current")
_HwL3vpnPeerQosStatisticsEntry_Object = MibTableRow
hwL3vpnPeerQosStatisticsEntry = _HwL3vpnPeerQosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1)
)
hwL3vpnPeerQosStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatVrfIndex"),
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatPeerAddress"),
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatQueueID"),
)
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatisticsEntry.setStatus("current")
_HwL3vpnPeerQosStatVrfIndex_Type = Unsigned32
_HwL3vpnPeerQosStatVrfIndex_Object = MibTableColumn
hwL3vpnPeerQosStatVrfIndex = _HwL3vpnPeerQosStatVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 1),
    _HwL3vpnPeerQosStatVrfIndex_Type()
)
hwL3vpnPeerQosStatVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatVrfIndex.setStatus("current")
_HwL3vpnPeerQosStatPeerAddress_Type = IpAddress
_HwL3vpnPeerQosStatPeerAddress_Object = MibTableColumn
hwL3vpnPeerQosStatPeerAddress = _HwL3vpnPeerQosStatPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 2),
    _HwL3vpnPeerQosStatPeerAddress_Type()
)
hwL3vpnPeerQosStatPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatPeerAddress.setStatus("current")


class _HwL3vpnPeerQosStatQueueID_Type(Integer32):
    """Custom type hwL3vpnPeerQosStatQueueID based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwL3vpnPeerQosStatQueueID_Type.__name__ = "Integer32"
_HwL3vpnPeerQosStatQueueID_Object = MibTableColumn
hwL3vpnPeerQosStatQueueID = _HwL3vpnPeerQosStatQueueID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 3),
    _HwL3vpnPeerQosStatQueueID_Type()
)
hwL3vpnPeerQosStatQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatQueueID.setStatus("current")
_HwL3vpnPeerQosStatPassPackets_Type = Counter64
_HwL3vpnPeerQosStatPassPackets_Object = MibTableColumn
hwL3vpnPeerQosStatPassPackets = _HwL3vpnPeerQosStatPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 4),
    _HwL3vpnPeerQosStatPassPackets_Type()
)
hwL3vpnPeerQosStatPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatPassPackets.setStatus("current")
_HwL3vpnPeerQosStatPassBytes_Type = Counter64
_HwL3vpnPeerQosStatPassBytes_Object = MibTableColumn
hwL3vpnPeerQosStatPassBytes = _HwL3vpnPeerQosStatPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 5),
    _HwL3vpnPeerQosStatPassBytes_Type()
)
hwL3vpnPeerQosStatPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatPassBytes.setStatus("current")
_HwL3vpnPeerQosStatDiscardPackets_Type = Counter64
_HwL3vpnPeerQosStatDiscardPackets_Object = MibTableColumn
hwL3vpnPeerQosStatDiscardPackets = _HwL3vpnPeerQosStatDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 6),
    _HwL3vpnPeerQosStatDiscardPackets_Type()
)
hwL3vpnPeerQosStatDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatDiscardPackets.setStatus("current")
_HwL3vpnPeerQosStatDiscardBytes_Type = Counter64
_HwL3vpnPeerQosStatDiscardBytes_Object = MibTableColumn
hwL3vpnPeerQosStatDiscardBytes = _HwL3vpnPeerQosStatDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 7),
    _HwL3vpnPeerQosStatDiscardBytes_Type()
)
hwL3vpnPeerQosStatDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatDiscardBytes.setStatus("current")
_HwL3vpnPeerQosStatPassPacketsRate_Type = Counter64
_HwL3vpnPeerQosStatPassPacketsRate_Object = MibTableColumn
hwL3vpnPeerQosStatPassPacketsRate = _HwL3vpnPeerQosStatPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 8),
    _HwL3vpnPeerQosStatPassPacketsRate_Type()
)
hwL3vpnPeerQosStatPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatPassPacketsRate.setStatus("current")
_HwL3vpnPeerQosStatPassBytesRate_Type = Counter64
_HwL3vpnPeerQosStatPassBytesRate_Object = MibTableColumn
hwL3vpnPeerQosStatPassBytesRate = _HwL3vpnPeerQosStatPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 9),
    _HwL3vpnPeerQosStatPassBytesRate_Type()
)
hwL3vpnPeerQosStatPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatPassBytesRate.setStatus("current")
_HwL3vpnPeerQosStatDiscardPacketsRate_Type = Counter64
_HwL3vpnPeerQosStatDiscardPacketsRate_Object = MibTableColumn
hwL3vpnPeerQosStatDiscardPacketsRate = _HwL3vpnPeerQosStatDiscardPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 10),
    _HwL3vpnPeerQosStatDiscardPacketsRate_Type()
)
hwL3vpnPeerQosStatDiscardPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatDiscardPacketsRate.setStatus("current")
_HwL3vpnPeerQosStatDiscardBytesRate_Type = Counter64
_HwL3vpnPeerQosStatDiscardBytesRate_Object = MibTableColumn
hwL3vpnPeerQosStatDiscardBytesRate = _HwL3vpnPeerQosStatDiscardBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 4, 1, 11),
    _HwL3vpnPeerQosStatDiscardBytesRate_Type()
)
hwL3vpnPeerQosStatDiscardBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatDiscardBytesRate.setStatus("current")
_HwL3vpnStatMapTable_Object = MibTable
hwL3vpnStatMapTable = _HwL3vpnStatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 5)
)
if mibBuilder.loadTexts:
    hwL3vpnStatMapTable.setStatus("current")
_HwL3vpnStatMapEntry_Object = MibTableRow
hwL3vpnStatMapEntry = _HwL3vpnStatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 5, 1)
)
hwL3vpnStatMapEntry.setIndexNames(
    (0, "HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatMapVrfName"),
)
if mibBuilder.loadTexts:
    hwL3vpnStatMapEntry.setStatus("current")


class _HwL3vpnStatMapVrfName_Type(DisplayString):
    """Custom type hwL3vpnStatMapVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL3vpnStatMapVrfName_Type.__name__ = "DisplayString"
_HwL3vpnStatMapVrfName_Object = MibTableColumn
hwL3vpnStatMapVrfName = _HwL3vpnStatMapVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 5, 1, 1),
    _HwL3vpnStatMapVrfName_Type()
)
hwL3vpnStatMapVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnStatMapVrfName.setStatus("current")
_HwL3vpnStatMapVrfIndex_Type = Unsigned32
_HwL3vpnStatMapVrfIndex_Object = MibTableColumn
hwL3vpnStatMapVrfIndex = _HwL3vpnStatMapVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 1, 5, 1, 2),
    _HwL3vpnStatMapVrfIndex_Type()
)
hwL3vpnStatMapVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3vpnStatMapVrfIndex.setStatus("current")
_HwL3vpnConformance_ObjectIdentity = ObjectIdentity
hwL3vpnConformance = _HwL3vpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2)
)
_HwL3vpnGroups_ObjectIdentity = ObjectIdentity
hwL3vpnGroups = _HwL3vpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1)
)
_HwL3vpnCompliances_ObjectIdentity = ObjectIdentity
hwL3vpnCompliances = _HwL3vpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 2)
)

# Managed Objects groups

hwL3vpnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1, 1)
)
hwL3vpnStatisticsGroup.setObjects(
      *(("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatEnable"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnVrfName"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInTrafficRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutTrafficRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInUnicastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutUnicastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInMulticastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutMulticastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatInBroadcastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatOutBroadcastPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatResetTime"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatResetStatistic"))
)
if mibBuilder.loadTexts:
    hwL3vpnStatisticsGroup.setStatus("current")

hwL3vpnQosStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1, 2)
)
hwL3vpnQosStatisticsGroup.setObjects(
      *(("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatPassPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatPassBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatDiscardPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatDiscardBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatPassPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatPassBytesRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatDiscardPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnQosStatDiscardBytesRate"))
)
if mibBuilder.loadTexts:
    hwL3vpnQosStatisticsGroup.setStatus("current")

hwL3vpnPeerStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1, 3)
)
hwL3vpnPeerStatisticsGroup.setObjects(
      *(("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatEnable"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatResetStatistic"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerVrfName"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatResetTime"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatQosPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatQosBytesRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatQosPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerStatQosBytes"))
)
if mibBuilder.loadTexts:
    hwL3vpnPeerStatisticsGroup.setStatus("current")

hwL3vpnPeerQosStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1, 4)
)
hwL3vpnPeerQosStatisticsGroup.setObjects(
      *(("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatPassPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatPassBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatDiscardPackets"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatDiscardBytes"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatPassPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatPassBytesRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatDiscardPacketsRate"),
        ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnPeerQosStatDiscardBytesRate"))
)
if mibBuilder.loadTexts:
    hwL3vpnPeerQosStatisticsGroup.setStatus("current")

hwL3vpnStatMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 1, 5)
)
hwL3vpnStatMapGroup.setObjects(
    ("HUAWEI-L3VPN-EXT-MIB", "hwL3vpnStatMapVrfIndex")
)
if mibBuilder.loadTexts:
    hwL3vpnStatMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwL3vpnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 150, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwL3vpnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L3VPN-EXT-MIB",
    **{"hwL3vpn": hwL3vpn,
       "hwL3vpnStatMibObjects": hwL3vpnStatMibObjects,
       "hwL3vpnStatisticsTable": hwL3vpnStatisticsTable,
       "hwL3vpnStatisticsEntry": hwL3vpnStatisticsEntry,
       "hwL3vpnVrfIndex": hwL3vpnVrfIndex,
       "hwL3vpnStatEnable": hwL3vpnStatEnable,
       "hwL3vpnVrfName": hwL3vpnVrfName,
       "hwL3vpnStatInTrafficRate": hwL3vpnStatInTrafficRate,
       "hwL3vpnStatOutTrafficRate": hwL3vpnStatOutTrafficRate,
       "hwL3vpnStatInPacketsRate": hwL3vpnStatInPacketsRate,
       "hwL3vpnStatOutPacketsRate": hwL3vpnStatOutPacketsRate,
       "hwL3vpnStatInBytes": hwL3vpnStatInBytes,
       "hwL3vpnStatOutBytes": hwL3vpnStatOutBytes,
       "hwL3vpnStatInPackets": hwL3vpnStatInPackets,
       "hwL3vpnStatOutPackets": hwL3vpnStatOutPackets,
       "hwL3vpnStatInUnicastPackets": hwL3vpnStatInUnicastPackets,
       "hwL3vpnStatOutUnicastPackets": hwL3vpnStatOutUnicastPackets,
       "hwL3vpnStatInMulticastPackets": hwL3vpnStatInMulticastPackets,
       "hwL3vpnStatOutMulticastPackets": hwL3vpnStatOutMulticastPackets,
       "hwL3vpnStatInBroadcastPackets": hwL3vpnStatInBroadcastPackets,
       "hwL3vpnStatOutBroadcastPackets": hwL3vpnStatOutBroadcastPackets,
       "hwL3vpnStatResetTime": hwL3vpnStatResetTime,
       "hwL3vpnStatResetStatistic": hwL3vpnStatResetStatistic,
       "hwL3vpnQosStatisticsTable": hwL3vpnQosStatisticsTable,
       "hwL3vpnQosStatisticsEntry": hwL3vpnQosStatisticsEntry,
       "hwL3vpnQosStatVrfIndex": hwL3vpnQosStatVrfIndex,
       "hwL3vpnQosStatQueueID": hwL3vpnQosStatQueueID,
       "hwL3vpnQosStatPassPackets": hwL3vpnQosStatPassPackets,
       "hwL3vpnQosStatPassBytes": hwL3vpnQosStatPassBytes,
       "hwL3vpnQosStatDiscardPackets": hwL3vpnQosStatDiscardPackets,
       "hwL3vpnQosStatDiscardBytes": hwL3vpnQosStatDiscardBytes,
       "hwL3vpnQosStatPassPacketsRate": hwL3vpnQosStatPassPacketsRate,
       "hwL3vpnQosStatPassBytesRate": hwL3vpnQosStatPassBytesRate,
       "hwL3vpnQosStatDiscardPacketsRate": hwL3vpnQosStatDiscardPacketsRate,
       "hwL3vpnQosStatDiscardBytesRate": hwL3vpnQosStatDiscardBytesRate,
       "hwL3vpnPeerStatisticsTable": hwL3vpnPeerStatisticsTable,
       "hwL3vpnPeerStatisticsEntry": hwL3vpnPeerStatisticsEntry,
       "hwL3vpnPeerVrfIndex": hwL3vpnPeerVrfIndex,
       "hwL3vpnPeerStatPeerAddress": hwL3vpnPeerStatPeerAddress,
       "hwL3vpnPeerStatEnable": hwL3vpnPeerStatEnable,
       "hwL3vpnPeerStatResetStatistic": hwL3vpnPeerStatResetStatistic,
       "hwL3vpnPeerVrfName": hwL3vpnPeerVrfName,
       "hwL3vpnPeerStatResetTime": hwL3vpnPeerStatResetTime,
       "hwL3vpnPeerStatQosPacketsRate": hwL3vpnPeerStatQosPacketsRate,
       "hwL3vpnPeerStatQosBytesRate": hwL3vpnPeerStatQosBytesRate,
       "hwL3vpnPeerStatQosPackets": hwL3vpnPeerStatQosPackets,
       "hwL3vpnPeerStatQosBytes": hwL3vpnPeerStatQosBytes,
       "hwL3vpnPeerQosStatisticsTable": hwL3vpnPeerQosStatisticsTable,
       "hwL3vpnPeerQosStatisticsEntry": hwL3vpnPeerQosStatisticsEntry,
       "hwL3vpnPeerQosStatVrfIndex": hwL3vpnPeerQosStatVrfIndex,
       "hwL3vpnPeerQosStatPeerAddress": hwL3vpnPeerQosStatPeerAddress,
       "hwL3vpnPeerQosStatQueueID": hwL3vpnPeerQosStatQueueID,
       "hwL3vpnPeerQosStatPassPackets": hwL3vpnPeerQosStatPassPackets,
       "hwL3vpnPeerQosStatPassBytes": hwL3vpnPeerQosStatPassBytes,
       "hwL3vpnPeerQosStatDiscardPackets": hwL3vpnPeerQosStatDiscardPackets,
       "hwL3vpnPeerQosStatDiscardBytes": hwL3vpnPeerQosStatDiscardBytes,
       "hwL3vpnPeerQosStatPassPacketsRate": hwL3vpnPeerQosStatPassPacketsRate,
       "hwL3vpnPeerQosStatPassBytesRate": hwL3vpnPeerQosStatPassBytesRate,
       "hwL3vpnPeerQosStatDiscardPacketsRate": hwL3vpnPeerQosStatDiscardPacketsRate,
       "hwL3vpnPeerQosStatDiscardBytesRate": hwL3vpnPeerQosStatDiscardBytesRate,
       "hwL3vpnStatMapTable": hwL3vpnStatMapTable,
       "hwL3vpnStatMapEntry": hwL3vpnStatMapEntry,
       "hwL3vpnStatMapVrfName": hwL3vpnStatMapVrfName,
       "hwL3vpnStatMapVrfIndex": hwL3vpnStatMapVrfIndex,
       "hwL3vpnConformance": hwL3vpnConformance,
       "hwL3vpnGroups": hwL3vpnGroups,
       "hwL3vpnStatisticsGroup": hwL3vpnStatisticsGroup,
       "hwL3vpnQosStatisticsGroup": hwL3vpnQosStatisticsGroup,
       "hwL3vpnPeerStatisticsGroup": hwL3vpnPeerStatisticsGroup,
       "hwL3vpnPeerQosStatisticsGroup": hwL3vpnPeerQosStatisticsGroup,
       "hwL3vpnStatMapGroup": hwL3vpnStatMapGroup,
       "hwL3vpnCompliances": hwL3vpnCompliances,
       "hwL3vpnCompliance": hwL3vpnCompliance}
)
