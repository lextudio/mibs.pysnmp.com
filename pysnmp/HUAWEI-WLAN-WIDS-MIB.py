# SNMP MIB module (HUAWEI-WLAN-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-WIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:46 2024
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

(hwApIndex,
 hwApMac,
 hwApType) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-DEVICE-MIB",
    "hwApIndex",
    "hwApMac",
    "hwApType")

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwWlanWids = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8)
)
hwWlanWids.setRevisions(
        ("2014-05-04 16:00",
         "2013-09-04 10:22",
         "2013-05-21 15:40",
         "2012-05-10 00:00",
         "2012-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWlanWidsNotifications_ObjectIdentity = ObjectIdentity
hwWlanWidsNotifications = _HwWlanWidsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1)
)
_HwWlanWidsNotify_ObjectIdentity = ObjectIdentity
hwWlanWidsNotify = _HwWlanWidsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1)
)
_HwWlanWidsNotifyObjects_ObjectIdentity = ObjectIdentity
hwWlanWidsNotifyObjects = _HwWlanWidsNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2)
)
_HwWlanObjWidsRogueDevMAC_Type = MacAddress
_HwWlanObjWidsRogueDevMAC_Object = MibScalar
hwWlanObjWidsRogueDevMAC = _HwWlanObjWidsRogueDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 1),
    _HwWlanObjWidsRogueDevMAC_Type()
)
hwWlanObjWidsRogueDevMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsRogueDevMAC.setStatus("current")
_HwWlanObjWidsRogueDevType_Type = Integer32
_HwWlanObjWidsRogueDevType_Object = MibScalar
hwWlanObjWidsRogueDevType = _HwWlanObjWidsRogueDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 2),
    _HwWlanObjWidsRogueDevType_Type()
)
hwWlanObjWidsRogueDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsRogueDevType.setStatus("current")
_HwWlanObjWidsRogueDevChannel_Type = Integer32
_HwWlanObjWidsRogueDevChannel_Object = MibScalar
hwWlanObjWidsRogueDevChannel = _HwWlanObjWidsRogueDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 3),
    _HwWlanObjWidsRogueDevChannel_Type()
)
hwWlanObjWidsRogueDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsRogueDevChannel.setStatus("current")
_HwWlanObjWidsRogueDevRSSI_Type = Integer32
_HwWlanObjWidsRogueDevRSSI_Object = MibScalar
hwWlanObjWidsRogueDevRSSI = _HwWlanObjWidsRogueDevRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 4),
    _HwWlanObjWidsRogueDevRSSI_Type()
)
hwWlanObjWidsRogueDevRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsRogueDevRSSI.setStatus("current")
_HwWlanObjWidsRogueDevSSID_Type = OctetString
_HwWlanObjWidsRogueDevSSID_Object = MibScalar
hwWlanObjWidsRogueDevSSID = _HwWlanObjWidsRogueDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 5),
    _HwWlanObjWidsRogueDevSSID_Type()
)
hwWlanObjWidsRogueDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsRogueDevSSID.setStatus("current")
_HwWlanObjWidsDetAPID_Type = Integer32
_HwWlanObjWidsDetAPID_Object = MibScalar
hwWlanObjWidsDetAPID = _HwWlanObjWidsDetAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 6),
    _HwWlanObjWidsDetAPID_Type()
)
hwWlanObjWidsDetAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetAPID.setStatus("current")
_HwWlanObjWidsDetRadioId_Type = Integer32
_HwWlanObjWidsDetRadioId_Object = MibScalar
hwWlanObjWidsDetRadioId = _HwWlanObjWidsDetRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 7),
    _HwWlanObjWidsDetRadioId_Type()
)
hwWlanObjWidsDetRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetRadioId.setStatus("current")
_HwWlanObjWidsDetAPChannel_Type = Integer32
_HwWlanObjWidsDetAPChannel_Object = MibScalar
hwWlanObjWidsDetAPChannel = _HwWlanObjWidsDetAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 8),
    _HwWlanObjWidsDetAPChannel_Type()
)
hwWlanObjWidsDetAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetAPChannel.setStatus("current")
_HwWlanObjWidsDetAPMAC_Type = MacAddress
_HwWlanObjWidsDetAPMAC_Object = MibScalar
hwWlanObjWidsDetAPMAC = _HwWlanObjWidsDetAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 9),
    _HwWlanObjWidsDetAPMAC_Type()
)
hwWlanObjWidsDetAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetAPMAC.setStatus("current")
_HwWlanObjWidsDetAPIP_Type = IpAddress
_HwWlanObjWidsDetAPIP_Object = MibScalar
hwWlanObjWidsDetAPIP = _HwWlanObjWidsDetAPIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 10),
    _HwWlanObjWidsDetAPIP_Type()
)
hwWlanObjWidsDetAPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetAPIP.setStatus("current")
_HwWlanObjWidsNonWifiDeviceType_Type = Integer32
_HwWlanObjWidsNonWifiDeviceType_Object = MibScalar
hwWlanObjWidsNonWifiDeviceType = _HwWlanObjWidsNonWifiDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 11),
    _HwWlanObjWidsNonWifiDeviceType_Type()
)
hwWlanObjWidsNonWifiDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsNonWifiDeviceType.setStatus("current")
_HwWlanObjWidsNonWifiInterChannel_Type = OctetString
_HwWlanObjWidsNonWifiInterChannel_Object = MibScalar
hwWlanObjWidsNonWifiInterChannel = _HwWlanObjWidsNonWifiInterChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 12),
    _HwWlanObjWidsNonWifiInterChannel_Type()
)
hwWlanObjWidsNonWifiInterChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsNonWifiInterChannel.setStatus("current")
_HwWlanObjWidsNonWifiRssi_Type = OctetString
_HwWlanObjWidsNonWifiRssi_Object = MibScalar
hwWlanObjWidsNonWifiRssi = _HwWlanObjWidsNonWifiRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 13),
    _HwWlanObjWidsNonWifiRssi_Type()
)
hwWlanObjWidsNonWifiRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsNonWifiRssi.setStatus("current")
_HwWlanObjWidsDetAPName_Type = OctetString
_HwWlanObjWidsDetAPName_Object = MibScalar
hwWlanObjWidsDetAPName = _HwWlanObjWidsDetAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 14),
    _HwWlanObjWidsDetAPName_Type()
)
hwWlanObjWidsDetAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetAPName.setStatus("current")
_HwWlanObjWidsDetRadioType_Type = Integer32
_HwWlanObjWidsDetRadioType_Object = MibScalar
hwWlanObjWidsDetRadioType = _HwWlanObjWidsDetRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 15),
    _HwWlanObjWidsDetRadioType_Type()
)
hwWlanObjWidsDetRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanObjWidsDetRadioType.setStatus("current")
_HwWlanObjWidsAttackDevMAC_Type = MacAddress
_HwWlanObjWidsAttackDevMAC_Object = MibScalar
hwWlanObjWidsAttackDevMAC = _HwWlanObjWidsAttackDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 16),
    _HwWlanObjWidsAttackDevMAC_Type()
)
hwWlanObjWidsAttackDevMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsAttackDevMAC.setStatus("current")
_HwWlanObjWidsAttackType_Type = Integer32
_HwWlanObjWidsAttackType_Object = MibScalar
hwWlanObjWidsAttackType = _HwWlanObjWidsAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 17),
    _HwWlanObjWidsAttackType_Type()
)
hwWlanObjWidsAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsAttackType.setStatus("current")
_HwWlanObjWidsAttackTypeStr_Type = OctetString
_HwWlanObjWidsAttackTypeStr_Object = MibScalar
hwWlanObjWidsAttackTypeStr = _HwWlanObjWidsAttackTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 2, 18),
    _HwWlanObjWidsAttackTypeStr_Type()
)
hwWlanObjWidsAttackTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanObjWidsAttackTypeStr.setStatus("current")
_HwWlanWidsGloablOpt_ObjectIdentity = ObjectIdentity
hwWlanWidsGloablOpt = _HwWlanWidsGloablOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2)
)
_HwWidsResetDetDevTableAll_Type = Integer32
_HwWidsResetDetDevTableAll_Object = MibScalar
hwWidsResetDetDevTableAll = _HwWidsResetDetDevTableAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 1),
    _HwWidsResetDetDevTableAll_Type()
)
hwWidsResetDetDevTableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetDetDevTableAll.setStatus("current")
_HwWidsResetDetDevTableByType_Type = Integer32
_HwWidsResetDetDevTableByType_Object = MibScalar
hwWidsResetDetDevTableByType = _HwWidsResetDetDevTableByType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 2),
    _HwWidsResetDetDevTableByType_Type()
)
hwWidsResetDetDevTableByType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetDetDevTableByType.setStatus("current")
_HwWidsResetRogueHistoryAll_Type = Integer32
_HwWidsResetRogueHistoryAll_Object = MibScalar
hwWidsResetRogueHistoryAll = _HwWidsResetRogueHistoryAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 3),
    _HwWidsResetRogueHistoryAll_Type()
)
hwWidsResetRogueHistoryAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetRogueHistoryAll.setStatus("current")
_HwWidsResetRogueHistoryByDevType_Type = Integer32
_HwWidsResetRogueHistoryByDevType_Object = MibScalar
hwWidsResetRogueHistoryByDevType = _HwWidsResetRogueHistoryByDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 4),
    _HwWidsResetRogueHistoryByDevType_Type()
)
hwWidsResetRogueHistoryByDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetRogueHistoryByDevType.setStatus("current")
_HwWidsResetAttackDev_Type = Integer32
_HwWidsResetAttackDev_Object = MibScalar
hwWidsResetAttackDev = _HwWidsResetAttackDev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 5),
    _HwWidsResetAttackDev_Type()
)
hwWidsResetAttackDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetAttackDev.setStatus("current")
_HwWidsResetAttackStat_Type = Integer32
_HwWidsResetAttackStat_Object = MibScalar
hwWidsResetAttackStat = _HwWidsResetAttackStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 6),
    _HwWidsResetAttackStat_Type()
)
hwWidsResetAttackStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetAttackStat.setStatus("current")
_HwWidsResetDynamicBlacklist_Type = Integer32
_HwWidsResetDynamicBlacklist_Object = MibScalar
hwWidsResetDynamicBlacklist = _HwWidsResetDynamicBlacklist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 7),
    _HwWidsResetDynamicBlacklist_Type()
)
hwWidsResetDynamicBlacklist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetDynamicBlacklist.setStatus("current")
_HwWidsResetDynamicBlacklistMac_Type = MacAddress
_HwWidsResetDynamicBlacklistMac_Object = MibScalar
hwWidsResetDynamicBlacklistMac = _HwWidsResetDynamicBlacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 8),
    _HwWidsResetDynamicBlacklistMac_Type()
)
hwWidsResetDynamicBlacklistMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetDynamicBlacklistMac.setStatus("current")
_HwWidsResetAttackHistory_Type = Integer32
_HwWidsResetAttackHistory_Object = MibScalar
hwWidsResetAttackHistory = _HwWidsResetAttackHistory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 2, 9),
    _HwWidsResetAttackHistory_Type()
)
hwWidsResetAttackHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWidsResetAttackHistory.setStatus("current")
_HwWidsDetDevTable_Object = MibTable
hwWidsDetDevTable = _HwWidsDetDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3)
)
if mibBuilder.loadTexts:
    hwWidsDetDevTable.setStatus("current")
_HwWidsDetDevEntry_Object = MibTableRow
hwWidsDetDevEntry = _HwWidsDetDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1)
)
hwWidsDetDevEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMac"),
)
if mibBuilder.loadTexts:
    hwWidsDetDevEntry.setStatus("current")
_HwWidsDetDevMac_Type = MacAddress
_HwWidsDetDevMac_Object = MibTableColumn
hwWidsDetDevMac = _HwWidsDetDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 1),
    _HwWidsDetDevMac_Type()
)
hwWidsDetDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetDevMac.setStatus("current")
_HwWidsDetDevType_Type = Integer32
_HwWidsDetDevType_Object = MibTableColumn
hwWidsDetDevType = _HwWidsDetDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 2),
    _HwWidsDetDevType_Type()
)
hwWidsDetDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevType.setStatus("current")
_HwWidsDetDevRssi_Type = Integer32
_HwWidsDetDevRssi_Object = MibTableColumn
hwWidsDetDevRssi = _HwWidsDetDevRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 3),
    _HwWidsDetDevRssi_Type()
)
hwWidsDetDevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevRssi.setStatus("current")
_HwWidsDetDevChannel_Type = Integer32
_HwWidsDetDevChannel_Object = MibTableColumn
hwWidsDetDevChannel = _HwWidsDetDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 4),
    _HwWidsDetDevChannel_Type()
)
hwWidsDetDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevChannel.setStatus("current")
_HwWidsDetDevSSID_Type = OctetString
_HwWidsDetDevSSID_Object = MibTableColumn
hwWidsDetDevSSID = _HwWidsDetDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 5),
    _HwWidsDetDevSSID_Type()
)
hwWidsDetDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevSSID.setStatus("current")
_HwWidsDetDevRogue_Type = Integer32
_HwWidsDetDevRogue_Object = MibTableColumn
hwWidsDetDevRogue = _HwWidsDetDevRogue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 6),
    _HwWidsDetDevRogue_Type()
)
hwWidsDetDevRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevRogue.setStatus("current")
_HwWidsDetDevLastTime_Type = Unsigned32
_HwWidsDetDevLastTime_Object = MibTableColumn
hwWidsDetDevLastTime = _HwWidsDetDevLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 7),
    _HwWidsDetDevLastTime_Type()
)
hwWidsDetDevLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevLastTime.setStatus("current")


class _HwWidsDetDevIsCountermeasuresed_Type(Integer32):
    """Custom type hwWidsDetDevIsCountermeasuresed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disbale", 1),
          ("enable", 2))
    )


_HwWidsDetDevIsCountermeasuresed_Type.__name__ = "Integer32"
_HwWidsDetDevIsCountermeasuresed_Object = MibTableColumn
hwWidsDetDevIsCountermeasuresed = _HwWidsDetDevIsCountermeasuresed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 8),
    _HwWidsDetDevIsCountermeasuresed_Type()
)
hwWidsDetDevIsCountermeasuresed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevIsCountermeasuresed.setStatus("current")
_HwWidsDetDevInterference_Type = Integer32
_HwWidsDetDevInterference_Object = MibTableColumn
hwWidsDetDevInterference = _HwWidsDetDevInterference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 9),
    _HwWidsDetDevInterference_Type()
)
hwWidsDetDevInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevInterference.setStatus("current")
_HwWidsDetDevBSSID_Type = MacAddress
_HwWidsDetDevBSSID_Object = MibTableColumn
hwWidsDetDevBSSID = _HwWidsDetDevBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 10),
    _HwWidsDetDevBSSID_Type()
)
hwWidsDetDevBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevBSSID.setStatus("current")
_HwWidsDetDevFirstDetTime_Type = Unsigned32
_HwWidsDetDevFirstDetTime_Object = MibTableColumn
hwWidsDetDevFirstDetTime = _HwWidsDetDevFirstDetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 3, 1, 11),
    _HwWidsDetDevFirstDetTime_Type()
)
hwWidsDetDevFirstDetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevFirstDetTime.setStatus("current")
_HwWidsDetDevMonitorTable_Object = MibTable
hwWidsDetDevMonitorTable = _HwWidsDetDevMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4)
)
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorTable.setStatus("current")
_HwWidsDetDevMonitorEntry_Object = MibTableRow
hwWidsDetDevMonitorEntry = _HwWidsDetDevMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1)
)
hwWidsDetDevMonitorEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMac"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApID"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApRadioID"),
)
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorEntry.setStatus("current")
_HwWidsDetDevMonitorApID_Type = Integer32
_HwWidsDetDevMonitorApID_Object = MibTableColumn
hwWidsDetDevMonitorApID = _HwWidsDetDevMonitorApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 1),
    _HwWidsDetDevMonitorApID_Type()
)
hwWidsDetDevMonitorApID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApID.setStatus("current")
_HwWidsDetDevMonitorApRadioID_Type = Integer32
_HwWidsDetDevMonitorApRadioID_Object = MibTableColumn
hwWidsDetDevMonitorApRadioID = _HwWidsDetDevMonitorApRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 2),
    _HwWidsDetDevMonitorApRadioID_Type()
)
hwWidsDetDevMonitorApRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApRadioID.setStatus("current")
_HwWidsDetDevMonitorApMAC_Type = MacAddress
_HwWidsDetDevMonitorApMAC_Object = MibTableColumn
hwWidsDetDevMonitorApMAC = _HwWidsDetDevMonitorApMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 3),
    _HwWidsDetDevMonitorApMAC_Type()
)
hwWidsDetDevMonitorApMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApMAC.setStatus("current")
_HwWidsDetDevMonitorApIP_Type = IpAddress
_HwWidsDetDevMonitorApIP_Object = MibTableColumn
hwWidsDetDevMonitorApIP = _HwWidsDetDevMonitorApIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 4),
    _HwWidsDetDevMonitorApIP_Type()
)
hwWidsDetDevMonitorApIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApIP.setStatus("current")
_HwWidsDetDevMonitorApChannel_Type = Integer32
_HwWidsDetDevMonitorApChannel_Object = MibTableColumn
hwWidsDetDevMonitorApChannel = _HwWidsDetDevMonitorApChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 5),
    _HwWidsDetDevMonitorApChannel_Type()
)
hwWidsDetDevMonitorApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApChannel.setStatus("current")
_HwWidsDetDevMonitorApRssi_Type = Integer32
_HwWidsDetDevMonitorApRssi_Object = MibTableColumn
hwWidsDetDevMonitorApRssi = _HwWidsDetDevMonitorApRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 6),
    _HwWidsDetDevMonitorApRssi_Type()
)
hwWidsDetDevMonitorApRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApRssi.setStatus("current")
_HwWidsDetDevMonitorApLastDetTime_Type = Unsigned32
_HwWidsDetDevMonitorApLastDetTime_Object = MibTableColumn
hwWidsDetDevMonitorApLastDetTime = _HwWidsDetDevMonitorApLastDetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 7),
    _HwWidsDetDevMonitorApLastDetTime_Type()
)
hwWidsDetDevMonitorApLastDetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApLastDetTime.setStatus("current")


class _HwWidsDetDevMonitorApCountermeasuresDev_Type(Integer32):
    """Custom type hwWidsDetDevMonitorApCountermeasuresDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWidsDetDevMonitorApCountermeasuresDev_Type.__name__ = "Integer32"
_HwWidsDetDevMonitorApCountermeasuresDev_Object = MibTableColumn
hwWidsDetDevMonitorApCountermeasuresDev = _HwWidsDetDevMonitorApCountermeasuresDev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 8),
    _HwWidsDetDevMonitorApCountermeasuresDev_Type()
)
hwWidsDetDevMonitorApCountermeasuresDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorApCountermeasuresDev.setStatus("current")
_HwWidsDetDevMonitorDetAtt_Type = Integer32
_HwWidsDetDevMonitorDetAtt_Object = MibTableColumn
hwWidsDetDevMonitorDetAtt = _HwWidsDetDevMonitorDetAtt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 4, 1, 9),
    _HwWidsDetDevMonitorDetAtt_Type()
)
hwWidsDetDevMonitorDetAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorDetAtt.setStatus("current")
_HwWidsRogueHistoryTable_Object = MibTable
hwWidsRogueHistoryTable = _HwWidsRogueHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5)
)
if mibBuilder.loadTexts:
    hwWidsRogueHistoryTable.setStatus("current")
_HwWidsRogueHistoryEntry_Object = MibTableRow
hwWidsRogueHistoryEntry = _HwWidsRogueHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1)
)
hwWidsRogueHistoryEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevMac"),
)
if mibBuilder.loadTexts:
    hwWidsRogueHistoryEntry.setStatus("current")
_HwWidsRogueDevMac_Type = MacAddress
_HwWidsRogueDevMac_Object = MibTableColumn
hwWidsRogueDevMac = _HwWidsRogueDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 1),
    _HwWidsRogueDevMac_Type()
)
hwWidsRogueDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsRogueDevMac.setStatus("current")
_HwWidsRogueDevType_Type = Integer32
_HwWidsRogueDevType_Object = MibTableColumn
hwWidsRogueDevType = _HwWidsRogueDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 2),
    _HwWidsRogueDevType_Type()
)
hwWidsRogueDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsRogueDevType.setStatus("current")
_HwWidsRogueDevRssi_Type = Integer32
_HwWidsRogueDevRssi_Object = MibTableColumn
hwWidsRogueDevRssi = _HwWidsRogueDevRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 3),
    _HwWidsRogueDevRssi_Type()
)
hwWidsRogueDevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsRogueDevRssi.setStatus("current")
_HwWidsRogueDevChannel_Type = Integer32
_HwWidsRogueDevChannel_Object = MibTableColumn
hwWidsRogueDevChannel = _HwWidsRogueDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 4),
    _HwWidsRogueDevChannel_Type()
)
hwWidsRogueDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsRogueDevChannel.setStatus("current")
_HwWidsRogueDevSSID_Type = OctetString
_HwWidsRogueDevSSID_Object = MibTableColumn
hwWidsRogueDevSSID = _HwWidsRogueDevSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 5),
    _HwWidsRogueDevSSID_Type()
)
hwWidsRogueDevSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsRogueDevSSID.setStatus("current")
_HwWidsRogueDevLastTime_Type = Unsigned32
_HwWidsRogueDevLastTime_Object = MibTableColumn
hwWidsRogueDevLastTime = _HwWidsRogueDevLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 5, 1, 6),
    _HwWidsRogueDevLastTime_Type()
)
hwWidsRogueDevLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsRogueDevLastTime.setStatus("current")
_HwSsidWhitelistTable_Object = MibTable
hwSsidWhitelistTable = _HwSsidWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 6)
)
if mibBuilder.loadTexts:
    hwSsidWhitelistTable.setStatus("current")
_HwSsidWhitelistEntry_Object = MibTableRow
hwSsidWhitelistEntry = _HwSsidWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 6, 1)
)
hwSsidWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwSsidWhitelistSsid"),
)
if mibBuilder.loadTexts:
    hwSsidWhitelistEntry.setStatus("current")
_HwSsidWhitelistSsid_Type = OctetString
_HwSsidWhitelistSsid_Object = MibTableColumn
hwSsidWhitelistSsid = _HwSsidWhitelistSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 6, 1, 1),
    _HwSsidWhitelistSsid_Type()
)
hwSsidWhitelistSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSsidWhitelistSsid.setStatus("current")
_HwSsidWhitelisttRowStatus_Type = RowStatus
_HwSsidWhitelisttRowStatus_Object = MibTableColumn
hwSsidWhitelisttRowStatus = _HwSsidWhitelisttRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 6, 1, 2),
    _HwSsidWhitelisttRowStatus_Type()
)
hwSsidWhitelisttRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSsidWhitelisttRowStatus.setStatus("current")
_HwWidsDetNonWifiDevTable_Object = MibTable
hwWidsDetNonWifiDevTable = _HwWidsDetNonWifiDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7)
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevTable.setStatus("current")
_HwWidsDetNonWifiDevEntry_Object = MibTableRow
hwWidsDetNonWifiDevEntry = _HwWidsDetNonWifiDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1)
)
hwWidsDetNonWifiDevEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevMonitorApMac"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevMonitorRadioId"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiType"),
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevEntry.setStatus("current")
_HwWidsDetNonWifiDevMonitorApMac_Type = MacAddress
_HwWidsDetNonWifiDevMonitorApMac_Object = MibTableColumn
hwWidsDetNonWifiDevMonitorApMac = _HwWidsDetNonWifiDevMonitorApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 1),
    _HwWidsDetNonWifiDevMonitorApMac_Type()
)
hwWidsDetNonWifiDevMonitorApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevMonitorApMac.setStatus("current")
_HwWidsDetNonWifiDevMonitorRadioId_Type = Integer32
_HwWidsDetNonWifiDevMonitorRadioId_Object = MibTableColumn
hwWidsDetNonWifiDevMonitorRadioId = _HwWidsDetNonWifiDevMonitorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 2),
    _HwWidsDetNonWifiDevMonitorRadioId_Type()
)
hwWidsDetNonWifiDevMonitorRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevMonitorRadioId.setStatus("current")
_HwWidsDetNonWifiType_Type = Integer32
_HwWidsDetNonWifiType_Object = MibTableColumn
hwWidsDetNonWifiType = _HwWidsDetNonWifiType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 3),
    _HwWidsDetNonWifiType_Type()
)
hwWidsDetNonWifiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiType.setStatus("current")
_HwWidsDetNonWifiRssi_Type = OctetString
_HwWidsDetNonWifiRssi_Object = MibTableColumn
hwWidsDetNonWifiRssi = _HwWidsDetNonWifiRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 4),
    _HwWidsDetNonWifiRssi_Type()
)
hwWidsDetNonWifiRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiRssi.setStatus("current")
_HwWidsDetNonWifiFrequencyType_Type = Integer32
_HwWidsDetNonWifiFrequencyType_Object = MibTableColumn
hwWidsDetNonWifiFrequencyType = _HwWidsDetNonWifiFrequencyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 5),
    _HwWidsDetNonWifiFrequencyType_Type()
)
hwWidsDetNonWifiFrequencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiFrequencyType.setStatus("current")
_HwWidsDetNonWifiChannel_Type = OctetString
_HwWidsDetNonWifiChannel_Object = MibTableColumn
hwWidsDetNonWifiChannel = _HwWidsDetNonWifiChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 6),
    _HwWidsDetNonWifiChannel_Type()
)
hwWidsDetNonWifiChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiChannel.setStatus("current")
_HwWidsDetNonWifiDevLastTime_Type = Integer32
_HwWidsDetNonWifiDevLastTime_Object = MibTableColumn
hwWidsDetNonWifiDevLastTime = _HwWidsDetNonWifiDevLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 7),
    _HwWidsDetNonWifiDevLastTime_Type()
)
hwWidsDetNonWifiDevLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevLastTime.setStatus("current")
_HwWidsDetNonWifiCenterFrequency_Type = Integer32
_HwWidsDetNonWifiCenterFrequency_Object = MibTableColumn
hwWidsDetNonWifiCenterFrequency = _HwWidsDetNonWifiCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 8),
    _HwWidsDetNonWifiCenterFrequency_Type()
)
hwWidsDetNonWifiCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiCenterFrequency.setStatus("current")
_HwWidsDetNonWifiBandwidth_Type = Integer32
_HwWidsDetNonWifiBandwidth_Object = MibTableColumn
hwWidsDetNonWifiBandwidth = _HwWidsDetNonWifiBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 9),
    _HwWidsDetNonWifiBandwidth_Type()
)
hwWidsDetNonWifiBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiBandwidth.setStatus("current")
_HwWidsDetNonWifiDutycycle_Type = Integer32
_HwWidsDetNonWifiDutycycle_Object = MibTableColumn
hwWidsDetNonWifiDutycycle = _HwWidsDetNonWifiDutycycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 10),
    _HwWidsDetNonWifiDutycycle_Type()
)
hwWidsDetNonWifiDutycycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDutycycle.setStatus("current")
_HwWidsDetNonWifiInterferenceLevel_Type = Integer32
_HwWidsDetNonWifiInterferenceLevel_Object = MibTableColumn
hwWidsDetNonWifiInterferenceLevel = _HwWidsDetNonWifiInterferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 11),
    _HwWidsDetNonWifiInterferenceLevel_Type()
)
hwWidsDetNonWifiInterferenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiInterferenceLevel.setStatus("current")
_HwWidsDetNonWifiDevMonitorAPName_Type = OctetString
_HwWidsDetNonWifiDevMonitorAPName_Object = MibTableColumn
hwWidsDetNonWifiDevMonitorAPName = _HwWidsDetNonWifiDevMonitorAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 12),
    _HwWidsDetNonWifiDevMonitorAPName_Type()
)
hwWidsDetNonWifiDevMonitorAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevMonitorAPName.setStatus("current")
_HwWidsDetNonWifiDevMonitorAPID_Type = Integer32
_HwWidsDetNonWifiDevMonitorAPID_Object = MibTableColumn
hwWidsDetNonWifiDevMonitorAPID = _HwWidsDetNonWifiDevMonitorAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 13),
    _HwWidsDetNonWifiDevMonitorAPID_Type()
)
hwWidsDetNonWifiDevMonitorAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevMonitorAPID.setStatus("current")
_HwWidsDetNonWifiDevRadioType_Type = Integer32
_HwWidsDetNonWifiDevRadioType_Object = MibTableColumn
hwWidsDetNonWifiDevRadioType = _HwWidsDetNonWifiDevRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 14),
    _HwWidsDetNonWifiDevRadioType_Type()
)
hwWidsDetNonWifiDevRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevRadioType.setStatus("current")
_HwWidsDetNonWifiDevMonitorAPChannel_Type = Integer32
_HwWidsDetNonWifiDevMonitorAPChannel_Object = MibTableColumn
hwWidsDetNonWifiDevMonitorAPChannel = _HwWidsDetNonWifiDevMonitorAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 15),
    _HwWidsDetNonWifiDevMonitorAPChannel_Type()
)
hwWidsDetNonWifiDevMonitorAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevMonitorAPChannel.setStatus("current")
_HwWidsDetNonWifiDevFirstTime_Type = Integer32
_HwWidsDetNonWifiDevFirstTime_Object = MibTableColumn
hwWidsDetNonWifiDevFirstTime = _HwWidsDetNonWifiDevFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 7, 1, 16),
    _HwWidsDetNonWifiDevFirstTime_Type()
)
hwWidsDetNonWifiDevFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevFirstTime.setStatus("current")
_HwWidsAttackHistoryTable_Object = MibTable
hwWidsAttackHistoryTable = _HwWidsAttackHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8)
)
if mibBuilder.loadTexts:
    hwWidsAttackHistoryTable.setStatus("current")
_HwWidsAttackHistoryEntry_Object = MibTableRow
hwWidsAttackHistoryEntry = _HwWidsAttackHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1)
)
hwWidsAttackHistoryEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistorySeq"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistorySubSeq"),
)
if mibBuilder.loadTexts:
    hwWidsAttackHistoryEntry.setStatus("current")
_HwWidsAttackHistorySeq_Type = Unsigned32
_HwWidsAttackHistorySeq_Object = MibTableColumn
hwWidsAttackHistorySeq = _HwWidsAttackHistorySeq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 1),
    _HwWidsAttackHistorySeq_Type()
)
hwWidsAttackHistorySeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsAttackHistorySeq.setStatus("current")
_HwWidsAttackHistorySubSeq_Type = Unsigned32
_HwWidsAttackHistorySubSeq_Object = MibTableColumn
hwWidsAttackHistorySubSeq = _HwWidsAttackHistorySubSeq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 2),
    _HwWidsAttackHistorySubSeq_Type()
)
hwWidsAttackHistorySubSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsAttackHistorySubSeq.setStatus("current")
_HwWidsAttackHistoryDevMac_Type = MacAddress
_HwWidsAttackHistoryDevMac_Object = MibTableColumn
hwWidsAttackHistoryDevMac = _HwWidsAttackHistoryDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 3),
    _HwWidsAttackHistoryDevMac_Type()
)
hwWidsAttackHistoryDevMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryDevMac.setStatus("current")
_HwWidsAttackHistoryDevType_Type = Integer32
_HwWidsAttackHistoryDevType_Object = MibTableColumn
hwWidsAttackHistoryDevType = _HwWidsAttackHistoryDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 4),
    _HwWidsAttackHistoryDevType_Type()
)
hwWidsAttackHistoryDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryDevType.setStatus("current")
_HwWidsAttackHistoryRssi_Type = Integer32
_HwWidsAttackHistoryRssi_Object = MibTableColumn
hwWidsAttackHistoryRssi = _HwWidsAttackHistoryRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 5),
    _HwWidsAttackHistoryRssi_Type()
)
hwWidsAttackHistoryRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryRssi.setStatus("current")
_HwWidsAttackHistoryChannel_Type = Integer32
_HwWidsAttackHistoryChannel_Object = MibTableColumn
hwWidsAttackHistoryChannel = _HwWidsAttackHistoryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 6),
    _HwWidsAttackHistoryChannel_Type()
)
hwWidsAttackHistoryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryChannel.setStatus("current")
_HwWidsAttackHistoryAttackType_Type = Integer32
_HwWidsAttackHistoryAttackType_Object = MibTableColumn
hwWidsAttackHistoryAttackType = _HwWidsAttackHistoryAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 7),
    _HwWidsAttackHistoryAttackType_Type()
)
hwWidsAttackHistoryAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryAttackType.setStatus("current")
_HwWidsAttackHistoryPacketBmp1_Type = Integer32
_HwWidsAttackHistoryPacketBmp1_Object = MibTableColumn
hwWidsAttackHistoryPacketBmp1 = _HwWidsAttackHistoryPacketBmp1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 8),
    _HwWidsAttackHistoryPacketBmp1_Type()
)
hwWidsAttackHistoryPacketBmp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryPacketBmp1.setStatus("current")
_HwWidsAttackHistoryPacketBmp2_Type = Integer32
_HwWidsAttackHistoryPacketBmp2_Object = MibTableColumn
hwWidsAttackHistoryPacketBmp2 = _HwWidsAttackHistoryPacketBmp2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 9),
    _HwWidsAttackHistoryPacketBmp2_Type()
)
hwWidsAttackHistoryPacketBmp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryPacketBmp2.setStatus("current")
_HwWidsAttackHistorySSID_Type = OctetString
_HwWidsAttackHistorySSID_Object = MibTableColumn
hwWidsAttackHistorySSID = _HwWidsAttackHistorySSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 10),
    _HwWidsAttackHistorySSID_Type()
)
hwWidsAttackHistorySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistorySSID.setStatus("current")
_HwWidsAttackHistoryDetTime_Type = Unsigned32
_HwWidsAttackHistoryDetTime_Object = MibTableColumn
hwWidsAttackHistoryDetTime = _HwWidsAttackHistoryDetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 11),
    _HwWidsAttackHistoryDetTime_Type()
)
hwWidsAttackHistoryDetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryDetTime.setStatus("current")
_HwWidsAttackHistoryDetectorApId_Type = Integer32
_HwWidsAttackHistoryDetectorApId_Object = MibTableColumn
hwWidsAttackHistoryDetectorApId = _HwWidsAttackHistoryDetectorApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 8, 1, 12),
    _HwWidsAttackHistoryDetectorApId_Type()
)
hwWidsAttackHistoryDetectorApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackHistoryDetectorApId.setStatus("current")
_HwWidsEnableAPTable_Object = MibTable
hwWidsEnableAPTable = _HwWidsEnableAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9)
)
if mibBuilder.loadTexts:
    hwWidsEnableAPTable.setStatus("current")
_HwWidsEnableAPEntry_Object = MibTableRow
hwWidsEnableAPEntry = _HwWidsEnableAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9, 1)
)
hwWidsEnableAPEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsEnableAPID"),
)
if mibBuilder.loadTexts:
    hwWidsEnableAPEntry.setStatus("current")
_HwWidsEnableAPID_Type = Integer32
_HwWidsEnableAPID_Object = MibTableColumn
hwWidsEnableAPID = _HwWidsEnableAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9, 1, 1),
    _HwWidsEnableAPID_Type()
)
hwWidsEnableAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsEnableAPID.setStatus("current")
_HwWidsEnableDevDetSwitch_Type = Integer32
_HwWidsEnableDevDetSwitch_Object = MibTableColumn
hwWidsEnableDevDetSwitch = _HwWidsEnableDevDetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9, 1, 2),
    _HwWidsEnableDevDetSwitch_Type()
)
hwWidsEnableDevDetSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsEnableDevDetSwitch.setStatus("current")
_HwWidsEnableAttackDetSwitch_Type = Integer32
_HwWidsEnableAttackDetSwitch_Object = MibTableColumn
hwWidsEnableAttackDetSwitch = _HwWidsEnableAttackDetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9, 1, 3),
    _HwWidsEnableAttackDetSwitch_Type()
)
hwWidsEnableAttackDetSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsEnableAttackDetSwitch.setStatus("current")
_HwWidsEnableAPName_Type = OctetString
_HwWidsEnableAPName_Object = MibTableColumn
hwWidsEnableAPName = _HwWidsEnableAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 9, 1, 4),
    _HwWidsEnableAPName_Type()
)
hwWidsEnableAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsEnableAPName.setStatus("current")
_HwWidsAttackStatTable_ObjectIdentity = ObjectIdentity
hwWidsAttackStatTable = _HwWidsAttackStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10)
)
_HwWidsAttackStatProbeRequestFloodAttack_Type = Unsigned32
_HwWidsAttackStatProbeRequestFloodAttack_Object = MibScalar
hwWidsAttackStatProbeRequestFloodAttack = _HwWidsAttackStatProbeRequestFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 1),
    _HwWidsAttackStatProbeRequestFloodAttack_Type()
)
hwWidsAttackStatProbeRequestFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatProbeRequestFloodAttack.setStatus("current")
_HwWidsAttackStatAuthRequestFloodAttack_Type = Unsigned32
_HwWidsAttackStatAuthRequestFloodAttack_Object = MibScalar
hwWidsAttackStatAuthRequestFloodAttack = _HwWidsAttackStatAuthRequestFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 2),
    _HwWidsAttackStatAuthRequestFloodAttack_Type()
)
hwWidsAttackStatAuthRequestFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatAuthRequestFloodAttack.setStatus("current")
_HwWidsAttackStatDeAuthenFloodAttack_Type = Unsigned32
_HwWidsAttackStatDeAuthenFloodAttack_Object = MibScalar
hwWidsAttackStatDeAuthenFloodAttack = _HwWidsAttackStatDeAuthenFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 3),
    _HwWidsAttackStatDeAuthenFloodAttack_Type()
)
hwWidsAttackStatDeAuthenFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatDeAuthenFloodAttack.setStatus("current")
_HwWidsAttackStatAssocReqFloodAttack_Type = Unsigned32
_HwWidsAttackStatAssocReqFloodAttack_Object = MibScalar
hwWidsAttackStatAssocReqFloodAttack = _HwWidsAttackStatAssocReqFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 4),
    _HwWidsAttackStatAssocReqFloodAttack_Type()
)
hwWidsAttackStatAssocReqFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatAssocReqFloodAttack.setStatus("current")
_HwWidsAttackStatDisassocReqFloodAttack_Type = Unsigned32
_HwWidsAttackStatDisassocReqFloodAttack_Object = MibScalar
hwWidsAttackStatDisassocReqFloodAttack = _HwWidsAttackStatDisassocReqFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 5),
    _HwWidsAttackStatDisassocReqFloodAttack_Type()
)
hwWidsAttackStatDisassocReqFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatDisassocReqFloodAttack.setStatus("current")
_HwWidsAttackStatReassocReqFloodAttack_Type = Unsigned32
_HwWidsAttackStatReassocReqFloodAttack_Object = MibScalar
hwWidsAttackStatReassocReqFloodAttack = _HwWidsAttackStatReassocReqFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 6),
    _HwWidsAttackStatReassocReqFloodAttack_Type()
)
hwWidsAttackStatReassocReqFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatReassocReqFloodAttack.setStatus("current")
_HwWidsAttackStatActionFloodAttack_Type = Unsigned32
_HwWidsAttackStatActionFloodAttack_Object = MibScalar
hwWidsAttackStatActionFloodAttack = _HwWidsAttackStatActionFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 7),
    _HwWidsAttackStatActionFloodAttack_Type()
)
hwWidsAttackStatActionFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatActionFloodAttack.setStatus("current")
_HwWidsAttackStatNullDataFloodAttack_Type = Unsigned32
_HwWidsAttackStatNullDataFloodAttack_Object = MibScalar
hwWidsAttackStatNullDataFloodAttack = _HwWidsAttackStatNullDataFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 8),
    _HwWidsAttackStatNullDataFloodAttack_Type()
)
hwWidsAttackStatNullDataFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatNullDataFloodAttack.setStatus("current")
_HwWidsAttackStatWeakIvAttack_Type = Unsigned32
_HwWidsAttackStatWeakIvAttack_Object = MibScalar
hwWidsAttackStatWeakIvAttack = _HwWidsAttackStatWeakIvAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 9),
    _HwWidsAttackStatWeakIvAttack_Type()
)
hwWidsAttackStatWeakIvAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatWeakIvAttack.setStatus("current")
_HwWidsAttackStatDeauthSpoofAttack_Type = Unsigned32
_HwWidsAttackStatDeauthSpoofAttack_Object = MibScalar
hwWidsAttackStatDeauthSpoofAttack = _HwWidsAttackStatDeauthSpoofAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 10),
    _HwWidsAttackStatDeauthSpoofAttack_Type()
)
hwWidsAttackStatDeauthSpoofAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatDeauthSpoofAttack.setStatus("current")
_HwWidsAttackStatDisassocSpoofAttack_Type = Unsigned32
_HwWidsAttackStatDisassocSpoofAttack_Object = MibScalar
hwWidsAttackStatDisassocSpoofAttack = _HwWidsAttackStatDisassocSpoofAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 11),
    _HwWidsAttackStatDisassocSpoofAttack_Type()
)
hwWidsAttackStatDisassocSpoofAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatDisassocSpoofAttack.setStatus("current")
_HwWidsAttackStatWepShareKeyAttack_Type = Unsigned32
_HwWidsAttackStatWepShareKeyAttack_Object = MibScalar
hwWidsAttackStatWepShareKeyAttack = _HwWidsAttackStatWepShareKeyAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 12),
    _HwWidsAttackStatWepShareKeyAttack_Type()
)
hwWidsAttackStatWepShareKeyAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatWepShareKeyAttack.setStatus("current")
_HwWidsAttackStatWpaAttack_Type = Unsigned32
_HwWidsAttackStatWpaAttack_Object = MibScalar
hwWidsAttackStatWpaAttack = _HwWidsAttackStatWpaAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 13),
    _HwWidsAttackStatWpaAttack_Type()
)
hwWidsAttackStatWpaAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatWpaAttack.setStatus("current")
_HwWidsAttackStatWpa2Attack_Type = Unsigned32
_HwWidsAttackStatWpa2Attack_Object = MibScalar
hwWidsAttackStatWpa2Attack = _HwWidsAttackStatWpa2Attack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 14),
    _HwWidsAttackStatWpa2Attack_Type()
)
hwWidsAttackStatWpa2Attack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatWpa2Attack.setStatus("current")
_HwWidsAttackStatWapiAttack_Type = Unsigned32
_HwWidsAttackStatWapiAttack_Object = MibScalar
hwWidsAttackStatWapiAttack = _HwWidsAttackStatWapiAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 15),
    _HwWidsAttackStatWapiAttack_Type()
)
hwWidsAttackStatWapiAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatWapiAttack.setStatus("current")
_HwWidsAttackStatStartTime_Type = Unsigned32
_HwWidsAttackStatStartTime_Object = MibScalar
hwWidsAttackStatStartTime = _HwWidsAttackStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 16),
    _HwWidsAttackStatStartTime_Type()
)
hwWidsAttackStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatStartTime.setStatus("current")
_HwWidsAttackStatEAPOLStartFloodAttack_Type = Unsigned32
_HwWidsAttackStatEAPOLStartFloodAttack_Object = MibScalar
hwWidsAttackStatEAPOLStartFloodAttack = _HwWidsAttackStatEAPOLStartFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 17),
    _HwWidsAttackStatEAPOLStartFloodAttack_Type()
)
hwWidsAttackStatEAPOLStartFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatEAPOLStartFloodAttack.setStatus("current")
_HwWidsAttackStatEAPOLLogoffFloodAttack_Type = Unsigned32
_HwWidsAttackStatEAPOLLogoffFloodAttack_Object = MibScalar
hwWidsAttackStatEAPOLLogoffFloodAttack = _HwWidsAttackStatEAPOLLogoffFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 18),
    _HwWidsAttackStatEAPOLLogoffFloodAttack_Type()
)
hwWidsAttackStatEAPOLLogoffFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatEAPOLLogoffFloodAttack.setStatus("current")
_HwWidsAttackStatNullQosFloodAttack_Type = Unsigned32
_HwWidsAttackStatNullQosFloodAttack_Object = MibScalar
hwWidsAttackStatNullQosFloodAttack = _HwWidsAttackStatNullQosFloodAttack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 10, 19),
    _HwWidsAttackStatNullQosFloodAttack_Type()
)
hwWidsAttackStatNullQosFloodAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackStatNullQosFloodAttack.setStatus("current")
_HwWidsDynamicBlacklistTable_Object = MibTable
hwWidsDynamicBlacklistTable = _HwWidsDynamicBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11)
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistTable.setStatus("current")
_HwWidsDynamicBlacklistEntry_Object = MibTableRow
hwWidsDynamicBlacklistEntry = _HwWidsDynamicBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1)
)
hwWidsDynamicBlacklistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistDevMac"),
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistEntry.setStatus("current")
_HwWidsDynamicBlacklistDevMac_Type = MacAddress
_HwWidsDynamicBlacklistDevMac_Object = MibTableColumn
hwWidsDynamicBlacklistDevMac = _HwWidsDynamicBlacklistDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 1),
    _HwWidsDynamicBlacklistDevMac_Type()
)
hwWidsDynamicBlacklistDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistDevMac.setStatus("current")
_HwWidsDynamicBlacklistDevType_Type = Integer32
_HwWidsDynamicBlacklistDevType_Object = MibTableColumn
hwWidsDynamicBlacklistDevType = _HwWidsDynamicBlacklistDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 2),
    _HwWidsDynamicBlacklistDevType_Type()
)
hwWidsDynamicBlacklistDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistDevType.setStatus("current")
_HwWidsDynamicBlacklistDevAttackType_Type = Integer32
_HwWidsDynamicBlacklistDevAttackType_Object = MibTableColumn
hwWidsDynamicBlacklistDevAttackType = _HwWidsDynamicBlacklistDevAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 3),
    _HwWidsDynamicBlacklistDevAttackType_Type()
)
hwWidsDynamicBlacklistDevAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistDevAttackType.setStatus("current")
_HwWidsDynamicBlacklistAttackPacketBmp1_Type = Integer32
_HwWidsDynamicBlacklistAttackPacketBmp1_Object = MibTableColumn
hwWidsDynamicBlacklistAttackPacketBmp1 = _HwWidsDynamicBlacklistAttackPacketBmp1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 4),
    _HwWidsDynamicBlacklistAttackPacketBmp1_Type()
)
hwWidsDynamicBlacklistAttackPacketBmp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAttackPacketBmp1.setStatus("current")
_HwWidsDynamicBlacklistAttackPacketBmp2_Type = Integer32
_HwWidsDynamicBlacklistAttackPacketBmp2_Object = MibTableColumn
hwWidsDynamicBlacklistAttackPacketBmp2 = _HwWidsDynamicBlacklistAttackPacketBmp2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 5),
    _HwWidsDynamicBlacklistAttackPacketBmp2_Type()
)
hwWidsDynamicBlacklistAttackPacketBmp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAttackPacketBmp2.setStatus("current")
_HwWidsDynamicBlacklistLastTime_Type = Unsigned32
_HwWidsDynamicBlacklistLastTime_Object = MibTableColumn
hwWidsDynamicBlacklistLastTime = _HwWidsDynamicBlacklistLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 11, 1, 6),
    _HwWidsDynamicBlacklistLastTime_Type()
)
hwWidsDynamicBlacklistLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistLastTime.setStatus("current")
_HwWidsDynamicBlacklistAPTable_Object = MibTable
hwWidsDynamicBlacklistAPTable = _HwWidsDynamicBlacklistAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12)
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAPTable.setStatus("current")
_HwWidsDynamicBlacklistAPEntry_Object = MibTableRow
hwWidsDynamicBlacklistAPEntry = _HwWidsDynamicBlacklistAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1)
)
hwWidsDynamicBlacklistAPEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistDevMac"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistApID"),
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAPEntry.setStatus("current")
_HwWidsDynamicBlacklistApID_Type = Integer32
_HwWidsDynamicBlacklistApID_Object = MibTableColumn
hwWidsDynamicBlacklistApID = _HwWidsDynamicBlacklistApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1, 1),
    _HwWidsDynamicBlacklistApID_Type()
)
hwWidsDynamicBlacklistApID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistApID.setStatus("current")
_HwWidsDynamicBlacklistAPMac_Type = MacAddress
_HwWidsDynamicBlacklistAPMac_Object = MibTableColumn
hwWidsDynamicBlacklistAPMac = _HwWidsDynamicBlacklistAPMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1, 2),
    _HwWidsDynamicBlacklistAPMac_Type()
)
hwWidsDynamicBlacklistAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAPMac.setStatus("current")
_HwWidsDynamicBlacklistApIP_Type = IpAddress
_HwWidsDynamicBlacklistApIP_Object = MibTableColumn
hwWidsDynamicBlacklistApIP = _HwWidsDynamicBlacklistApIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1, 3),
    _HwWidsDynamicBlacklistApIP_Type()
)
hwWidsDynamicBlacklistApIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistApIP.setStatus("current")
_HwWidsDynamicBlacklistAttackType_Type = Integer32
_HwWidsDynamicBlacklistAttackType_Object = MibTableColumn
hwWidsDynamicBlacklistAttackType = _HwWidsDynamicBlacklistAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1, 4),
    _HwWidsDynamicBlacklistAttackType_Type()
)
hwWidsDynamicBlacklistAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAttackType.setStatus("current")
_HwWidsDynamicBlacklistAPLastTime_Type = Unsigned32
_HwWidsDynamicBlacklistAPLastTime_Object = MibTableColumn
hwWidsDynamicBlacklistAPLastTime = _HwWidsDynamicBlacklistAPLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 12, 1, 5),
    _HwWidsDynamicBlacklistAPLastTime_Type()
)
hwWidsDynamicBlacklistAPLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAPLastTime.setStatus("current")
_HwWlanWidsObjects_ObjectIdentity = ObjectIdentity
hwWlanWidsObjects = _HwWlanWidsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13)
)
_HwWidsDetNonWifiDevHistTable_Object = MibTable
hwWidsDetNonWifiDevHistTable = _HwWidsDetNonWifiDevHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1)
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevHistTable.setStatus("current")
_HwWidsDetNonWifiDevHistEntry_Object = MibTableRow
hwWidsDetNonWifiDevHistEntry = _HwWidsDetNonWifiDevHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1)
)
hwWidsDetNonWifiDevHistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistIndex"),
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevHistEntry.setStatus("current")
_HwWidsDetNonWifiHistIndex_Type = Integer32
_HwWidsDetNonWifiHistIndex_Object = MibTableColumn
hwWidsDetNonWifiHistIndex = _HwWidsDetNonWifiHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 1),
    _HwWidsDetNonWifiHistIndex_Type()
)
hwWidsDetNonWifiHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistIndex.setStatus("current")
_HwWidsDetNonWifiHistMonitorApMac_Type = MacAddress
_HwWidsDetNonWifiHistMonitorApMac_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorApMac = _HwWidsDetNonWifiHistMonitorApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 2),
    _HwWidsDetNonWifiHistMonitorApMac_Type()
)
hwWidsDetNonWifiHistMonitorApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorApMac.setStatus("current")
_HwWidsDetNonWifiHistMonitorAPName_Type = OctetString
_HwWidsDetNonWifiHistMonitorAPName_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorAPName = _HwWidsDetNonWifiHistMonitorAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 3),
    _HwWidsDetNonWifiHistMonitorAPName_Type()
)
hwWidsDetNonWifiHistMonitorAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorAPName.setStatus("current")
_HwWidsDetNonWifiHistMonitorAPID_Type = Integer32
_HwWidsDetNonWifiHistMonitorAPID_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorAPID = _HwWidsDetNonWifiHistMonitorAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 4),
    _HwWidsDetNonWifiHistMonitorAPID_Type()
)
hwWidsDetNonWifiHistMonitorAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorAPID.setStatus("current")
_HwWidsDetNonWifiHistMonitorRadioId_Type = Integer32
_HwWidsDetNonWifiHistMonitorRadioId_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorRadioId = _HwWidsDetNonWifiHistMonitorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 5),
    _HwWidsDetNonWifiHistMonitorRadioId_Type()
)
hwWidsDetNonWifiHistMonitorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorRadioId.setStatus("current")
_HwWidsDetNonWifiHistMonitorRadioType_Type = Integer32
_HwWidsDetNonWifiHistMonitorRadioType_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorRadioType = _HwWidsDetNonWifiHistMonitorRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 6),
    _HwWidsDetNonWifiHistMonitorRadioType_Type()
)
hwWidsDetNonWifiHistMonitorRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorRadioType.setStatus("current")
_HwWidsDetNonWifiHistMonitorAPChannel_Type = Integer32
_HwWidsDetNonWifiHistMonitorAPChannel_Object = MibTableColumn
hwWidsDetNonWifiHistMonitorAPChannel = _HwWidsDetNonWifiHistMonitorAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 7),
    _HwWidsDetNonWifiHistMonitorAPChannel_Type()
)
hwWidsDetNonWifiHistMonitorAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistMonitorAPChannel.setStatus("current")
_HwWidsDetNonWifiHistDevType_Type = Integer32
_HwWidsDetNonWifiHistDevType_Object = MibTableColumn
hwWidsDetNonWifiHistDevType = _HwWidsDetNonWifiHistDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 8),
    _HwWidsDetNonWifiHistDevType_Type()
)
hwWidsDetNonWifiHistDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistDevType.setStatus("current")
_HwWidsDetNonWifiHistRssi_Type = OctetString
_HwWidsDetNonWifiHistRssi_Object = MibTableColumn
hwWidsDetNonWifiHistRssi = _HwWidsDetNonWifiHistRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 9),
    _HwWidsDetNonWifiHistRssi_Type()
)
hwWidsDetNonWifiHistRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistRssi.setStatus("current")
_HwWidsDetNonWifiHistFrequencyType_Type = Integer32
_HwWidsDetNonWifiHistFrequencyType_Object = MibTableColumn
hwWidsDetNonWifiHistFrequencyType = _HwWidsDetNonWifiHistFrequencyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 10),
    _HwWidsDetNonWifiHistFrequencyType_Type()
)
hwWidsDetNonWifiHistFrequencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistFrequencyType.setStatus("current")
_HwWidsDetNonWifiHistChannel_Type = OctetString
_HwWidsDetNonWifiHistChannel_Object = MibTableColumn
hwWidsDetNonWifiHistChannel = _HwWidsDetNonWifiHistChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 11),
    _HwWidsDetNonWifiHistChannel_Type()
)
hwWidsDetNonWifiHistChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistChannel.setStatus("current")
_HwWidsDetNonWifiHistDevLastTime_Type = Integer32
_HwWidsDetNonWifiHistDevLastTime_Object = MibTableColumn
hwWidsDetNonWifiHistDevLastTime = _HwWidsDetNonWifiHistDevLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 12),
    _HwWidsDetNonWifiHistDevLastTime_Type()
)
hwWidsDetNonWifiHistDevLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistDevLastTime.setStatus("current")
_HwWidsDetNonWifiHistCenterFrequency_Type = Integer32
_HwWidsDetNonWifiHistCenterFrequency_Object = MibTableColumn
hwWidsDetNonWifiHistCenterFrequency = _HwWidsDetNonWifiHistCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 13),
    _HwWidsDetNonWifiHistCenterFrequency_Type()
)
hwWidsDetNonWifiHistCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistCenterFrequency.setStatus("current")
_HwWidsDetNonWifiHistBandwidth_Type = Integer32
_HwWidsDetNonWifiHistBandwidth_Object = MibTableColumn
hwWidsDetNonWifiHistBandwidth = _HwWidsDetNonWifiHistBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 14),
    _HwWidsDetNonWifiHistBandwidth_Type()
)
hwWidsDetNonWifiHistBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistBandwidth.setStatus("current")
_HwWidsDetNonWifiHistDutycycle_Type = Integer32
_HwWidsDetNonWifiHistDutycycle_Object = MibTableColumn
hwWidsDetNonWifiHistDutycycle = _HwWidsDetNonWifiHistDutycycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 15),
    _HwWidsDetNonWifiHistDutycycle_Type()
)
hwWidsDetNonWifiHistDutycycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistDutycycle.setStatus("current")
_HwWidsDetNonWifiHistInterferenceLevel_Type = Integer32
_HwWidsDetNonWifiHistInterferenceLevel_Object = MibTableColumn
hwWidsDetNonWifiHistInterferenceLevel = _HwWidsDetNonWifiHistInterferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 16),
    _HwWidsDetNonWifiHistInterferenceLevel_Type()
)
hwWidsDetNonWifiHistInterferenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistInterferenceLevel.setStatus("current")
_HwWidsDetNonWifiHistDevFirstTime_Type = Integer32
_HwWidsDetNonWifiHistDevFirstTime_Object = MibTableColumn
hwWidsDetNonWifiHistDevFirstTime = _HwWidsDetNonWifiHistDevFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 1, 1, 17),
    _HwWidsDetNonWifiHistDevFirstTime_Type()
)
hwWidsDetNonWifiHistDevFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsDetNonWifiHistDevFirstTime.setStatus("current")
_HwWidsAttDevTable_Object = MibTable
hwWidsAttDevTable = _HwWidsAttDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2)
)
if mibBuilder.loadTexts:
    hwWidsAttDevTable.setStatus("current")
_HwWidsAttDevEntry_Object = MibTableRow
hwWidsAttDevEntry = _HwWidsAttDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1)
)
hwWidsAttDevEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevMac"),
)
if mibBuilder.loadTexts:
    hwWidsAttDevEntry.setStatus("current")
_HwWidsAttackDevMac_Type = MacAddress
_HwWidsAttackDevMac_Object = MibTableColumn
hwWidsAttackDevMac = _HwWidsAttackDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 1),
    _HwWidsAttackDevMac_Type()
)
hwWidsAttackDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsAttackDevMac.setStatus("current")
_HwWidsAttackDevChannel_Type = Integer32
_HwWidsAttackDevChannel_Object = MibTableColumn
hwWidsAttackDevChannel = _HwWidsAttackDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 2),
    _HwWidsAttackDevChannel_Type()
)
hwWidsAttackDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDevChannel.setStatus("current")
_HwWidsAttackDevRssi_Type = Integer32
_HwWidsAttackDevRssi_Object = MibTableColumn
hwWidsAttackDevRssi = _HwWidsAttackDevRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 3),
    _HwWidsAttackDevRssi_Type()
)
hwWidsAttackDevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDevRssi.setStatus("current")
_HwWidsAttackDevLastAttType_Type = Unsigned32
_HwWidsAttackDevLastAttType_Object = MibTableColumn
hwWidsAttackDevLastAttType = _HwWidsAttackDevLastAttType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 4),
    _HwWidsAttackDevLastAttType_Type()
)
hwWidsAttackDevLastAttType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDevLastAttType.setStatus("current")
_HwWidsAttackDevLastPacketBmp_Type = Unsigned32
_HwWidsAttackDevLastPacketBmp_Object = MibTableColumn
hwWidsAttackDevLastPacketBmp = _HwWidsAttackDevLastPacketBmp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 5),
    _HwWidsAttackDevLastPacketBmp_Type()
)
hwWidsAttackDevLastPacketBmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDevLastPacketBmp.setStatus("current")
_HwWidsAttackDevLastDetTime_Type = Unsigned32
_HwWidsAttackDevLastDetTime_Object = MibTableColumn
hwWidsAttackDevLastDetTime = _HwWidsAttackDevLastDetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 2, 1, 6),
    _HwWidsAttackDevLastDetTime_Type()
)
hwWidsAttackDevLastDetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDevLastDetTime.setStatus("current")
_HwWidsAttackDetorTable_Object = MibTable
hwWidsAttackDetorTable = _HwWidsAttackDetorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3)
)
if mibBuilder.loadTexts:
    hwWidsAttackDetorTable.setStatus("current")
_HwWidsAttackDetorEntry_Object = MibTableRow
hwWidsAttackDetorEntry = _HwWidsAttackDetorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1)
)
hwWidsAttackDetorEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevMac"),
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorApID"),
)
if mibBuilder.loadTexts:
    hwWidsAttackDetorEntry.setStatus("current")
_HwWidsAttackDetorApID_Type = Unsigned32
_HwWidsAttackDetorApID_Object = MibTableColumn
hwWidsAttackDetorApID = _HwWidsAttackDetorApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 1),
    _HwWidsAttackDetorApID_Type()
)
hwWidsAttackDetorApID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsAttackDetorApID.setStatus("current")
_HwWidsAttackDetorAttTypeBmp_Type = Unsigned32
_HwWidsAttackDetorAttTypeBmp_Object = MibTableColumn
hwWidsAttackDetorAttTypeBmp = _HwWidsAttackDetorAttTypeBmp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 2),
    _HwWidsAttackDetorAttTypeBmp_Type()
)
hwWidsAttackDetorAttTypeBmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorAttTypeBmp.setStatus("current")
_HwWidsAttackDetorPacketBmpFlood_Type = Unsigned32
_HwWidsAttackDetorPacketBmpFlood_Object = MibTableColumn
hwWidsAttackDetorPacketBmpFlood = _HwWidsAttackDetorPacketBmpFlood_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 3),
    _HwWidsAttackDetorPacketBmpFlood_Type()
)
hwWidsAttackDetorPacketBmpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorPacketBmpFlood.setStatus("current")
_HwWidsAttackDetorPacketBmpSpoof_Type = Unsigned32
_HwWidsAttackDetorPacketBmpSpoof_Object = MibTableColumn
hwWidsAttackDetorPacketBmpSpoof = _HwWidsAttackDetorPacketBmpSpoof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 4),
    _HwWidsAttackDetorPacketBmpSpoof_Type()
)
hwWidsAttackDetorPacketBmpSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorPacketBmpSpoof.setStatus("current")
_HwWidsAttackDetorFirstDetTimeFlood_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeFlood_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeFlood = _HwWidsAttackDetorFirstDetTimeFlood_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 5),
    _HwWidsAttackDetorFirstDetTimeFlood_Type()
)
hwWidsAttackDetorFirstDetTimeFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeFlood.setStatus("current")
_HwWidsAttackDetorFirstDetTimeSpoof_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeSpoof_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeSpoof = _HwWidsAttackDetorFirstDetTimeSpoof_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 6),
    _HwWidsAttackDetorFirstDetTimeSpoof_Type()
)
hwWidsAttackDetorFirstDetTimeSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeSpoof.setStatus("current")
_HwWidsAttackDetorFirstDetTimeWeakIv_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeWeakIv_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeWeakIv = _HwWidsAttackDetorFirstDetTimeWeakIv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 7),
    _HwWidsAttackDetorFirstDetTimeWeakIv_Type()
)
hwWidsAttackDetorFirstDetTimeWeakIv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeWeakIv.setStatus("current")
_HwWidsAttackDetorFirstDetTimeWep_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeWep_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeWep = _HwWidsAttackDetorFirstDetTimeWep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 8),
    _HwWidsAttackDetorFirstDetTimeWep_Type()
)
hwWidsAttackDetorFirstDetTimeWep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeWep.setStatus("current")
_HwWidsAttackDetorFirstDetTimeWpa_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeWpa_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeWpa = _HwWidsAttackDetorFirstDetTimeWpa_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 9),
    _HwWidsAttackDetorFirstDetTimeWpa_Type()
)
hwWidsAttackDetorFirstDetTimeWpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeWpa.setStatus("current")
_HwWidsAttackDetorFirstDetTimeWpa2_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeWpa2_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeWpa2 = _HwWidsAttackDetorFirstDetTimeWpa2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 10),
    _HwWidsAttackDetorFirstDetTimeWpa2_Type()
)
hwWidsAttackDetorFirstDetTimeWpa2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeWpa2.setStatus("current")
_HwWidsAttackDetorFirstDetTimeWapi_Type = Unsigned32
_HwWidsAttackDetorFirstDetTimeWapi_Object = MibTableColumn
hwWidsAttackDetorFirstDetTimeWapi = _HwWidsAttackDetorFirstDetTimeWapi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 3, 1, 11),
    _HwWidsAttackDetorFirstDetTimeWapi_Type()
)
hwWidsAttackDetorFirstDetTimeWapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWidsAttackDetorFirstDetTimeWapi.setStatus("current")
_HwOuiWhitelistTable_Object = MibTable
hwOuiWhitelistTable = _HwOuiWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 4)
)
if mibBuilder.loadTexts:
    hwOuiWhitelistTable.setStatus("current")
_HwOuiWhitelistEntry_Object = MibTableRow
hwOuiWhitelistEntry = _HwOuiWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 4, 1)
)
hwOuiWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwOuiWhitelistOui"),
)
if mibBuilder.loadTexts:
    hwOuiWhitelistEntry.setStatus("current")
_HwOuiWhitelistOui_Type = OctetString
_HwOuiWhitelistOui_Object = MibTableColumn
hwOuiWhitelistOui = _HwOuiWhitelistOui_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 4, 1, 1),
    _HwOuiWhitelistOui_Type()
)
hwOuiWhitelistOui.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOuiWhitelistOui.setStatus("current")
_HwOuiWhitelistRowStatus_Type = RowStatus
_HwOuiWhitelistRowStatus_Object = MibTableColumn
hwOuiWhitelistRowStatus = _HwOuiWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 4, 1, 2),
    _HwOuiWhitelistRowStatus_Type()
)
hwOuiWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOuiWhitelistRowStatus.setStatus("current")
_HwMacAddressWhitelistTable_Object = MibTable
hwMacAddressWhitelistTable = _HwMacAddressWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 5)
)
if mibBuilder.loadTexts:
    hwMacAddressWhitelistTable.setStatus("current")
_HwMacAddressWhitelistEntry_Object = MibTableRow
hwMacAddressWhitelistEntry = _HwMacAddressWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 5, 1)
)
hwMacAddressWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwMacAddressWhitelistMacAddress"),
)
if mibBuilder.loadTexts:
    hwMacAddressWhitelistEntry.setStatus("current")
_HwMacAddressWhitelistMacAddress_Type = MacAddress
_HwMacAddressWhitelistMacAddress_Object = MibTableColumn
hwMacAddressWhitelistMacAddress = _HwMacAddressWhitelistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 5, 1, 1),
    _HwMacAddressWhitelistMacAddress_Type()
)
hwMacAddressWhitelistMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacAddressWhitelistMacAddress.setStatus("current")
_HwMacAddressWhitelistRowStatus_Type = RowStatus
_HwMacAddressWhitelistRowStatus_Object = MibTableColumn
hwMacAddressWhitelistRowStatus = _HwMacAddressWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 5, 1, 2),
    _HwMacAddressWhitelistRowStatus_Type()
)
hwMacAddressWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacAddressWhitelistRowStatus.setStatus("current")
_HwWidsSpoofSsidRuleListTable_Object = MibTable
hwWidsSpoofSsidRuleListTable = _HwWidsSpoofSsidRuleListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 6)
)
if mibBuilder.loadTexts:
    hwWidsSpoofSsidRuleListTable.setStatus("current")
_HwWidsSpoofSsidRuleListEntry_Object = MibTableRow
hwWidsSpoofSsidRuleListEntry = _HwWidsSpoofSsidRuleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 6, 1)
)
hwWidsSpoofSsidRuleListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-WIDS-MIB", "hwWidsSpoofSsidRule"),
)
if mibBuilder.loadTexts:
    hwWidsSpoofSsidRuleListEntry.setStatus("current")
_HwWidsSpoofSsidRule_Type = OctetString
_HwWidsSpoofSsidRule_Object = MibTableColumn
hwWidsSpoofSsidRule = _HwWidsSpoofSsidRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 6, 1, 1),
    _HwWidsSpoofSsidRule_Type()
)
hwWidsSpoofSsidRule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWidsSpoofSsidRule.setStatus("current")
_HwWidsSpoofSsidRuleListRowStatus_Type = RowStatus
_HwWidsSpoofSsidRuleListRowStatus_Object = MibTableColumn
hwWidsSpoofSsidRuleListRowStatus = _HwWidsSpoofSsidRuleListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 13, 6, 1, 2),
    _HwWidsSpoofSsidRuleListRowStatus_Type()
)
hwWidsSpoofSsidRuleListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWidsSpoofSsidRuleListRowStatus.setStatus("current")
_HwWlanWidsConformance_ObjectIdentity = ObjectIdentity
hwWlanWidsConformance = _HwWlanWidsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14)
)
_HwWlanWidsCompliances_ObjectIdentity = ObjectIdentity
hwWlanWidsCompliances = _HwWlanWidsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 1)
)
_HwWlanWidsObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanWidsObjectGroups = _HwWlanWidsObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2)
)

# Managed Objects groups

hwWlanWidsMIBNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 1)
)
hwWlanWidsMIBNotifyObjectGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevRSSI"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPIP"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiDeviceType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiInterChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPName"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsMIBNotifyObjectGroup.setStatus("current")

hwWlanWidsGlobalOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 3)
)
hwWlanWidsGlobalOptGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetDetDevTableAll"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetDetDevTableByType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetRogueHistoryAll"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetRogueHistoryByDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetAttackDev"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetAttackStat"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetDynamicBlacklist"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetDynamicBlacklistMac"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsResetAttackHistory"))
)
if mibBuilder.loadTexts:
    hwWlanWidsGlobalOptGroup.setStatus("current")

hwWidsDetDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 4)
)
hwWidsDetDevGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevRogue"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevLastTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevIsCountermeasuresed"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevInterference"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevBSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevFirstDetTime"))
)
if mibBuilder.loadTexts:
    hwWidsDetDevGroup.setStatus("current")

hwWidsDetDevMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 5)
)
hwWidsDetDevMonitorGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApIP"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApLastDetTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorApCountermeasuresDev"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetDevMonitorDetAtt"))
)
if mibBuilder.loadTexts:
    hwWidsDetDevMonitorGroup.setStatus("current")

hwWidsRogueHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 6)
)
hwWidsRogueHistoryGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsRogueDevLastTime"))
)
if mibBuilder.loadTexts:
    hwWidsRogueHistoryGroup.setStatus("current")

hwSsidWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 7)
)
hwSsidWhitelistGroup.setObjects(
    ("HUAWEI-WLAN-WIDS-MIB", "hwSsidWhitelisttRowStatus")
)
if mibBuilder.loadTexts:
    hwSsidWhitelistGroup.setStatus("current")

hwWidsDetNonWifiDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 8)
)
hwWidsDetNonWifiDevGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiFrequencyType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevLastTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiCenterFrequency"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiBandwidth"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDutycycle"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiInterferenceLevel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevMonitorAPName"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevMonitorAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevRadioType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevMonitorAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiDevFirstTime"))
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevGroup.setStatus("current")

hwWidsAttackHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 9)
)
hwWidsAttackHistoryGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryDevMac"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryPacketBmp1"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryPacketBmp2"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistorySSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryDetTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackHistoryDetectorApId"))
)
if mibBuilder.loadTexts:
    hwWidsAttackHistoryGroup.setStatus("current")

hwWidsEnableAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 10)
)
hwWidsEnableAPGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsEnableDevDetSwitch"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsEnableAttackDetSwitch"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsEnableAPName"))
)
if mibBuilder.loadTexts:
    hwWidsEnableAPGroup.setStatus("current")

hwWidsAttackStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 11)
)
hwWidsAttackStatGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatProbeRequestFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatAuthRequestFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatDeAuthenFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatAssocReqFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatDisassocReqFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatReassocReqFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatActionFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatNullDataFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatWeakIvAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatDeauthSpoofAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatDisassocSpoofAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatWepShareKeyAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatWpaAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatWpa2Attack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatWapiAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatStartTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatEAPOLStartFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatEAPOLLogoffFloodAttack"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackStatNullQosFloodAttack"))
)
if mibBuilder.loadTexts:
    hwWidsAttackStatGroup.setStatus("current")

hwWidsDynamicBlacklistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 12)
)
hwWidsDynamicBlacklistGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistDevAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistAttackPacketBmp1"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistAttackPacketBmp2"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistLastTime"))
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistGroup.setStatus("current")

hwWidsDynamicBlacklistAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 13)
)
hwWidsDynamicBlacklistAPGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistAPMac"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistApIP"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDynamicBlacklistAPLastTime"))
)
if mibBuilder.loadTexts:
    hwWidsDynamicBlacklistAPGroup.setStatus("current")

hwWidsDetNonWifiDevHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 14)
)
hwWidsDetNonWifiDevHistGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorApMac"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorAPName"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorRadioType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistMonitorAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistFrequencyType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistDevLastTime"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistCenterFrequency"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistBandwidth"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistDutycycle"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistInterferenceLevel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsDetNonWifiHistDevFirstTime"))
)
if mibBuilder.loadTexts:
    hwWidsDetNonWifiDevHistGroup.setStatus("current")

hwWidsAttackDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 15)
)
hwWidsAttackDevGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevLastAttType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevLastPacketBmp"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDevLastDetTime"))
)
if mibBuilder.loadTexts:
    hwWidsAttackDevGroup.setStatus("current")

hwWidsAttackDetorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 16)
)
hwWidsAttackDetorGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorPacketBmpFlood"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorPacketBmpSpoof"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeFlood"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeSpoof"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeWeakIv"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeWep"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeWpa"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeWpa2"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorFirstDetTimeWapi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWidsAttackDetorAttTypeBmp"))
)
if mibBuilder.loadTexts:
    hwWidsAttackDetorGroup.setStatus("current")

hwWidsOuiWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 17)
)
hwWidsOuiWhitelistGroup.setObjects(
    ("HUAWEI-WLAN-WIDS-MIB", "hwOuiWhitelistRowStatus")
)
if mibBuilder.loadTexts:
    hwWidsOuiWhitelistGroup.setStatus("current")

hwWidsMacAddressWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 18)
)
hwWidsMacAddressWhitelistGroup.setObjects(
    ("HUAWEI-WLAN-WIDS-MIB", "hwMacAddressWhitelistRowStatus")
)
if mibBuilder.loadTexts:
    hwWidsMacAddressWhitelistGroup.setStatus("current")

hwWidsSpoofSsidRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 19)
)
hwWidsSpoofSsidRuleGroup.setObjects(
    ("HUAWEI-WLAN-WIDS-MIB", "hwWidsSpoofSsidRuleListRowStatus")
)
if mibBuilder.loadTexts:
    hwWidsSpoofSsidRuleGroup.setStatus("current")


# Notification objects

hwWlanWidsRougeDevDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 1)
)
hwWlanWidsRougeDevDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevRSSI"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPIP"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"))
)
if mibBuilder.loadTexts:
    hwWlanWidsRougeDevDetectedNotify.setStatus(
        "current"
    )

hwWlanWidsRougeDevClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 2)
)
hwWlanWidsRougeDevClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevRSSI"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsRogueDevSSID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPIP"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"))
)
if mibBuilder.loadTexts:
    hwWlanWidsRougeDevClearNotify.setStatus(
        "current"
    )

hwWlanWidsNonWifiDetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 3)
)
hwWlanWidsNonWifiDetNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPName"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiDeviceType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiInterChannel"))
)
if mibBuilder.loadTexts:
    hwWlanWidsNonWifiDetNotify.setStatus(
        "current"
    )

hwWlanWidsNonWifiClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 4)
)
hwWlanWidsNonWifiClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPID"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPName"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioId"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetRadioType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiDeviceType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiRssi"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsNonWifiInterChannel"))
)
if mibBuilder.loadTexts:
    hwWlanWidsNonWifiClearNotify.setStatus(
        "current"
    )

hwWlanWidsFloodAttackDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 5)
)
hwWlanWidsFloodAttackDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsFloodAttackDetectedNotify.setStatus(
        "current"
    )

hwWlanWidsFloodAttackClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 6)
)
hwWlanWidsFloodAttackClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsFloodAttackClearNotify.setStatus(
        "current"
    )

hwWlanWidsSpoofAttackDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 7)
)
hwWlanWidsSpoofAttackDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsSpoofAttackDetectedNotify.setStatus(
        "current"
    )

hwWlanWidsSpoofAttackClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 8)
)
hwWlanWidsSpoofAttackClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsSpoofAttackClearNotify.setStatus(
        "current"
    )

hwWlanWidsWeakIvAttackDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 9)
)
hwWlanWidsWeakIvAttackDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsWeakIvAttackDetectedNotify.setStatus(
        "current"
    )

hwWlanWidsWeakIvAttackClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 10)
)
hwWlanWidsWeakIvAttackClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsWeakIvAttackClearNotify.setStatus(
        "current"
    )

hwWlanWidsPSKAttackDetectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 11)
)
hwWlanWidsPSKAttackDetectedNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsPSKAttackDetectedNotify.setStatus(
        "current"
    )

hwWlanWidsPSKAttackClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 1, 1, 12)
)
hwWlanWidsPSKAttackClearNotify.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackDevMAC"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsDetAPChannel"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackType"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanObjWidsAttackTypeStr"))
)
if mibBuilder.loadTexts:
    hwWlanWidsPSKAttackClearNotify.setStatus(
        "current"
    )


# Notifications groups

hwWlanWidsMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 2, 2)
)
hwWlanWidsMIBNotifyGroup.setObjects(
      *(("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsRougeDevDetectedNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsRougeDevClearNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsNonWifiDetNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsNonWifiClearNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsFloodAttackDetectedNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsFloodAttackClearNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsSpoofAttackDetectedNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsSpoofAttackClearNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsWeakIvAttackDetectedNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsWeakIvAttackClearNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsPSKAttackDetectedNotify"),
        ("HUAWEI-WLAN-WIDS-MIB", "hwWlanWidsPSKAttackClearNotify"))
)
if mibBuilder.loadTexts:
    hwWlanWidsMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwWlanWidsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 8, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanWidsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-WIDS-MIB",
    **{"hwWlanWids": hwWlanWids,
       "hwWlanWidsNotifications": hwWlanWidsNotifications,
       "hwWlanWidsNotify": hwWlanWidsNotify,
       "hwWlanWidsRougeDevDetectedNotify": hwWlanWidsRougeDevDetectedNotify,
       "hwWlanWidsRougeDevClearNotify": hwWlanWidsRougeDevClearNotify,
       "hwWlanWidsNonWifiDetNotify": hwWlanWidsNonWifiDetNotify,
       "hwWlanWidsNonWifiClearNotify": hwWlanWidsNonWifiClearNotify,
       "hwWlanWidsFloodAttackDetectedNotify": hwWlanWidsFloodAttackDetectedNotify,
       "hwWlanWidsFloodAttackClearNotify": hwWlanWidsFloodAttackClearNotify,
       "hwWlanWidsSpoofAttackDetectedNotify": hwWlanWidsSpoofAttackDetectedNotify,
       "hwWlanWidsSpoofAttackClearNotify": hwWlanWidsSpoofAttackClearNotify,
       "hwWlanWidsWeakIvAttackDetectedNotify": hwWlanWidsWeakIvAttackDetectedNotify,
       "hwWlanWidsWeakIvAttackClearNotify": hwWlanWidsWeakIvAttackClearNotify,
       "hwWlanWidsPSKAttackDetectedNotify": hwWlanWidsPSKAttackDetectedNotify,
       "hwWlanWidsPSKAttackClearNotify": hwWlanWidsPSKAttackClearNotify,
       "hwWlanWidsNotifyObjects": hwWlanWidsNotifyObjects,
       "hwWlanObjWidsRogueDevMAC": hwWlanObjWidsRogueDevMAC,
       "hwWlanObjWidsRogueDevType": hwWlanObjWidsRogueDevType,
       "hwWlanObjWidsRogueDevChannel": hwWlanObjWidsRogueDevChannel,
       "hwWlanObjWidsRogueDevRSSI": hwWlanObjWidsRogueDevRSSI,
       "hwWlanObjWidsRogueDevSSID": hwWlanObjWidsRogueDevSSID,
       "hwWlanObjWidsDetAPID": hwWlanObjWidsDetAPID,
       "hwWlanObjWidsDetRadioId": hwWlanObjWidsDetRadioId,
       "hwWlanObjWidsDetAPChannel": hwWlanObjWidsDetAPChannel,
       "hwWlanObjWidsDetAPMAC": hwWlanObjWidsDetAPMAC,
       "hwWlanObjWidsDetAPIP": hwWlanObjWidsDetAPIP,
       "hwWlanObjWidsNonWifiDeviceType": hwWlanObjWidsNonWifiDeviceType,
       "hwWlanObjWidsNonWifiInterChannel": hwWlanObjWidsNonWifiInterChannel,
       "hwWlanObjWidsNonWifiRssi": hwWlanObjWidsNonWifiRssi,
       "hwWlanObjWidsDetAPName": hwWlanObjWidsDetAPName,
       "hwWlanObjWidsDetRadioType": hwWlanObjWidsDetRadioType,
       "hwWlanObjWidsAttackDevMAC": hwWlanObjWidsAttackDevMAC,
       "hwWlanObjWidsAttackType": hwWlanObjWidsAttackType,
       "hwWlanObjWidsAttackTypeStr": hwWlanObjWidsAttackTypeStr,
       "hwWlanWidsGloablOpt": hwWlanWidsGloablOpt,
       "hwWidsResetDetDevTableAll": hwWidsResetDetDevTableAll,
       "hwWidsResetDetDevTableByType": hwWidsResetDetDevTableByType,
       "hwWidsResetRogueHistoryAll": hwWidsResetRogueHistoryAll,
       "hwWidsResetRogueHistoryByDevType": hwWidsResetRogueHistoryByDevType,
       "hwWidsResetAttackDev": hwWidsResetAttackDev,
       "hwWidsResetAttackStat": hwWidsResetAttackStat,
       "hwWidsResetDynamicBlacklist": hwWidsResetDynamicBlacklist,
       "hwWidsResetDynamicBlacklistMac": hwWidsResetDynamicBlacklistMac,
       "hwWidsResetAttackHistory": hwWidsResetAttackHistory,
       "hwWidsDetDevTable": hwWidsDetDevTable,
       "hwWidsDetDevEntry": hwWidsDetDevEntry,
       "hwWidsDetDevMac": hwWidsDetDevMac,
       "hwWidsDetDevType": hwWidsDetDevType,
       "hwWidsDetDevRssi": hwWidsDetDevRssi,
       "hwWidsDetDevChannel": hwWidsDetDevChannel,
       "hwWidsDetDevSSID": hwWidsDetDevSSID,
       "hwWidsDetDevRogue": hwWidsDetDevRogue,
       "hwWidsDetDevLastTime": hwWidsDetDevLastTime,
       "hwWidsDetDevIsCountermeasuresed": hwWidsDetDevIsCountermeasuresed,
       "hwWidsDetDevInterference": hwWidsDetDevInterference,
       "hwWidsDetDevBSSID": hwWidsDetDevBSSID,
       "hwWidsDetDevFirstDetTime": hwWidsDetDevFirstDetTime,
       "hwWidsDetDevMonitorTable": hwWidsDetDevMonitorTable,
       "hwWidsDetDevMonitorEntry": hwWidsDetDevMonitorEntry,
       "hwWidsDetDevMonitorApID": hwWidsDetDevMonitorApID,
       "hwWidsDetDevMonitorApRadioID": hwWidsDetDevMonitorApRadioID,
       "hwWidsDetDevMonitorApMAC": hwWidsDetDevMonitorApMAC,
       "hwWidsDetDevMonitorApIP": hwWidsDetDevMonitorApIP,
       "hwWidsDetDevMonitorApChannel": hwWidsDetDevMonitorApChannel,
       "hwWidsDetDevMonitorApRssi": hwWidsDetDevMonitorApRssi,
       "hwWidsDetDevMonitorApLastDetTime": hwWidsDetDevMonitorApLastDetTime,
       "hwWidsDetDevMonitorApCountermeasuresDev": hwWidsDetDevMonitorApCountermeasuresDev,
       "hwWidsDetDevMonitorDetAtt": hwWidsDetDevMonitorDetAtt,
       "hwWidsRogueHistoryTable": hwWidsRogueHistoryTable,
       "hwWidsRogueHistoryEntry": hwWidsRogueHistoryEntry,
       "hwWidsRogueDevMac": hwWidsRogueDevMac,
       "hwWidsRogueDevType": hwWidsRogueDevType,
       "hwWidsRogueDevRssi": hwWidsRogueDevRssi,
       "hwWidsRogueDevChannel": hwWidsRogueDevChannel,
       "hwWidsRogueDevSSID": hwWidsRogueDevSSID,
       "hwWidsRogueDevLastTime": hwWidsRogueDevLastTime,
       "hwSsidWhitelistTable": hwSsidWhitelistTable,
       "hwSsidWhitelistEntry": hwSsidWhitelistEntry,
       "hwSsidWhitelistSsid": hwSsidWhitelistSsid,
       "hwSsidWhitelisttRowStatus": hwSsidWhitelisttRowStatus,
       "hwWidsDetNonWifiDevTable": hwWidsDetNonWifiDevTable,
       "hwWidsDetNonWifiDevEntry": hwWidsDetNonWifiDevEntry,
       "hwWidsDetNonWifiDevMonitorApMac": hwWidsDetNonWifiDevMonitorApMac,
       "hwWidsDetNonWifiDevMonitorRadioId": hwWidsDetNonWifiDevMonitorRadioId,
       "hwWidsDetNonWifiType": hwWidsDetNonWifiType,
       "hwWidsDetNonWifiRssi": hwWidsDetNonWifiRssi,
       "hwWidsDetNonWifiFrequencyType": hwWidsDetNonWifiFrequencyType,
       "hwWidsDetNonWifiChannel": hwWidsDetNonWifiChannel,
       "hwWidsDetNonWifiDevLastTime": hwWidsDetNonWifiDevLastTime,
       "hwWidsDetNonWifiCenterFrequency": hwWidsDetNonWifiCenterFrequency,
       "hwWidsDetNonWifiBandwidth": hwWidsDetNonWifiBandwidth,
       "hwWidsDetNonWifiDutycycle": hwWidsDetNonWifiDutycycle,
       "hwWidsDetNonWifiInterferenceLevel": hwWidsDetNonWifiInterferenceLevel,
       "hwWidsDetNonWifiDevMonitorAPName": hwWidsDetNonWifiDevMonitorAPName,
       "hwWidsDetNonWifiDevMonitorAPID": hwWidsDetNonWifiDevMonitorAPID,
       "hwWidsDetNonWifiDevRadioType": hwWidsDetNonWifiDevRadioType,
       "hwWidsDetNonWifiDevMonitorAPChannel": hwWidsDetNonWifiDevMonitorAPChannel,
       "hwWidsDetNonWifiDevFirstTime": hwWidsDetNonWifiDevFirstTime,
       "hwWidsAttackHistoryTable": hwWidsAttackHistoryTable,
       "hwWidsAttackHistoryEntry": hwWidsAttackHistoryEntry,
       "hwWidsAttackHistorySeq": hwWidsAttackHistorySeq,
       "hwWidsAttackHistorySubSeq": hwWidsAttackHistorySubSeq,
       "hwWidsAttackHistoryDevMac": hwWidsAttackHistoryDevMac,
       "hwWidsAttackHistoryDevType": hwWidsAttackHistoryDevType,
       "hwWidsAttackHistoryRssi": hwWidsAttackHistoryRssi,
       "hwWidsAttackHistoryChannel": hwWidsAttackHistoryChannel,
       "hwWidsAttackHistoryAttackType": hwWidsAttackHistoryAttackType,
       "hwWidsAttackHistoryPacketBmp1": hwWidsAttackHistoryPacketBmp1,
       "hwWidsAttackHistoryPacketBmp2": hwWidsAttackHistoryPacketBmp2,
       "hwWidsAttackHistorySSID": hwWidsAttackHistorySSID,
       "hwWidsAttackHistoryDetTime": hwWidsAttackHistoryDetTime,
       "hwWidsAttackHistoryDetectorApId": hwWidsAttackHistoryDetectorApId,
       "hwWidsEnableAPTable": hwWidsEnableAPTable,
       "hwWidsEnableAPEntry": hwWidsEnableAPEntry,
       "hwWidsEnableAPID": hwWidsEnableAPID,
       "hwWidsEnableDevDetSwitch": hwWidsEnableDevDetSwitch,
       "hwWidsEnableAttackDetSwitch": hwWidsEnableAttackDetSwitch,
       "hwWidsEnableAPName": hwWidsEnableAPName,
       "hwWidsAttackStatTable": hwWidsAttackStatTable,
       "hwWidsAttackStatProbeRequestFloodAttack": hwWidsAttackStatProbeRequestFloodAttack,
       "hwWidsAttackStatAuthRequestFloodAttack": hwWidsAttackStatAuthRequestFloodAttack,
       "hwWidsAttackStatDeAuthenFloodAttack": hwWidsAttackStatDeAuthenFloodAttack,
       "hwWidsAttackStatAssocReqFloodAttack": hwWidsAttackStatAssocReqFloodAttack,
       "hwWidsAttackStatDisassocReqFloodAttack": hwWidsAttackStatDisassocReqFloodAttack,
       "hwWidsAttackStatReassocReqFloodAttack": hwWidsAttackStatReassocReqFloodAttack,
       "hwWidsAttackStatActionFloodAttack": hwWidsAttackStatActionFloodAttack,
       "hwWidsAttackStatNullDataFloodAttack": hwWidsAttackStatNullDataFloodAttack,
       "hwWidsAttackStatWeakIvAttack": hwWidsAttackStatWeakIvAttack,
       "hwWidsAttackStatDeauthSpoofAttack": hwWidsAttackStatDeauthSpoofAttack,
       "hwWidsAttackStatDisassocSpoofAttack": hwWidsAttackStatDisassocSpoofAttack,
       "hwWidsAttackStatWepShareKeyAttack": hwWidsAttackStatWepShareKeyAttack,
       "hwWidsAttackStatWpaAttack": hwWidsAttackStatWpaAttack,
       "hwWidsAttackStatWpa2Attack": hwWidsAttackStatWpa2Attack,
       "hwWidsAttackStatWapiAttack": hwWidsAttackStatWapiAttack,
       "hwWidsAttackStatStartTime": hwWidsAttackStatStartTime,
       "hwWidsAttackStatEAPOLStartFloodAttack": hwWidsAttackStatEAPOLStartFloodAttack,
       "hwWidsAttackStatEAPOLLogoffFloodAttack": hwWidsAttackStatEAPOLLogoffFloodAttack,
       "hwWidsAttackStatNullQosFloodAttack": hwWidsAttackStatNullQosFloodAttack,
       "hwWidsDynamicBlacklistTable": hwWidsDynamicBlacklistTable,
       "hwWidsDynamicBlacklistEntry": hwWidsDynamicBlacklistEntry,
       "hwWidsDynamicBlacklistDevMac": hwWidsDynamicBlacklistDevMac,
       "hwWidsDynamicBlacklistDevType": hwWidsDynamicBlacklistDevType,
       "hwWidsDynamicBlacklistDevAttackType": hwWidsDynamicBlacklistDevAttackType,
       "hwWidsDynamicBlacklistAttackPacketBmp1": hwWidsDynamicBlacklistAttackPacketBmp1,
       "hwWidsDynamicBlacklistAttackPacketBmp2": hwWidsDynamicBlacklistAttackPacketBmp2,
       "hwWidsDynamicBlacklistLastTime": hwWidsDynamicBlacklistLastTime,
       "hwWidsDynamicBlacklistAPTable": hwWidsDynamicBlacklistAPTable,
       "hwWidsDynamicBlacklistAPEntry": hwWidsDynamicBlacklistAPEntry,
       "hwWidsDynamicBlacklistApID": hwWidsDynamicBlacklistApID,
       "hwWidsDynamicBlacklistAPMac": hwWidsDynamicBlacklistAPMac,
       "hwWidsDynamicBlacklistApIP": hwWidsDynamicBlacklistApIP,
       "hwWidsDynamicBlacklistAttackType": hwWidsDynamicBlacklistAttackType,
       "hwWidsDynamicBlacklistAPLastTime": hwWidsDynamicBlacklistAPLastTime,
       "hwWlanWidsObjects": hwWlanWidsObjects,
       "hwWidsDetNonWifiDevHistTable": hwWidsDetNonWifiDevHistTable,
       "hwWidsDetNonWifiDevHistEntry": hwWidsDetNonWifiDevHistEntry,
       "hwWidsDetNonWifiHistIndex": hwWidsDetNonWifiHistIndex,
       "hwWidsDetNonWifiHistMonitorApMac": hwWidsDetNonWifiHistMonitorApMac,
       "hwWidsDetNonWifiHistMonitorAPName": hwWidsDetNonWifiHistMonitorAPName,
       "hwWidsDetNonWifiHistMonitorAPID": hwWidsDetNonWifiHistMonitorAPID,
       "hwWidsDetNonWifiHistMonitorRadioId": hwWidsDetNonWifiHistMonitorRadioId,
       "hwWidsDetNonWifiHistMonitorRadioType": hwWidsDetNonWifiHistMonitorRadioType,
       "hwWidsDetNonWifiHistMonitorAPChannel": hwWidsDetNonWifiHistMonitorAPChannel,
       "hwWidsDetNonWifiHistDevType": hwWidsDetNonWifiHistDevType,
       "hwWidsDetNonWifiHistRssi": hwWidsDetNonWifiHistRssi,
       "hwWidsDetNonWifiHistFrequencyType": hwWidsDetNonWifiHistFrequencyType,
       "hwWidsDetNonWifiHistChannel": hwWidsDetNonWifiHistChannel,
       "hwWidsDetNonWifiHistDevLastTime": hwWidsDetNonWifiHistDevLastTime,
       "hwWidsDetNonWifiHistCenterFrequency": hwWidsDetNonWifiHistCenterFrequency,
       "hwWidsDetNonWifiHistBandwidth": hwWidsDetNonWifiHistBandwidth,
       "hwWidsDetNonWifiHistDutycycle": hwWidsDetNonWifiHistDutycycle,
       "hwWidsDetNonWifiHistInterferenceLevel": hwWidsDetNonWifiHistInterferenceLevel,
       "hwWidsDetNonWifiHistDevFirstTime": hwWidsDetNonWifiHistDevFirstTime,
       "hwWidsAttDevTable": hwWidsAttDevTable,
       "hwWidsAttDevEntry": hwWidsAttDevEntry,
       "hwWidsAttackDevMac": hwWidsAttackDevMac,
       "hwWidsAttackDevChannel": hwWidsAttackDevChannel,
       "hwWidsAttackDevRssi": hwWidsAttackDevRssi,
       "hwWidsAttackDevLastAttType": hwWidsAttackDevLastAttType,
       "hwWidsAttackDevLastPacketBmp": hwWidsAttackDevLastPacketBmp,
       "hwWidsAttackDevLastDetTime": hwWidsAttackDevLastDetTime,
       "hwWidsAttackDetorTable": hwWidsAttackDetorTable,
       "hwWidsAttackDetorEntry": hwWidsAttackDetorEntry,
       "hwWidsAttackDetorApID": hwWidsAttackDetorApID,
       "hwWidsAttackDetorAttTypeBmp": hwWidsAttackDetorAttTypeBmp,
       "hwWidsAttackDetorPacketBmpFlood": hwWidsAttackDetorPacketBmpFlood,
       "hwWidsAttackDetorPacketBmpSpoof": hwWidsAttackDetorPacketBmpSpoof,
       "hwWidsAttackDetorFirstDetTimeFlood": hwWidsAttackDetorFirstDetTimeFlood,
       "hwWidsAttackDetorFirstDetTimeSpoof": hwWidsAttackDetorFirstDetTimeSpoof,
       "hwWidsAttackDetorFirstDetTimeWeakIv": hwWidsAttackDetorFirstDetTimeWeakIv,
       "hwWidsAttackDetorFirstDetTimeWep": hwWidsAttackDetorFirstDetTimeWep,
       "hwWidsAttackDetorFirstDetTimeWpa": hwWidsAttackDetorFirstDetTimeWpa,
       "hwWidsAttackDetorFirstDetTimeWpa2": hwWidsAttackDetorFirstDetTimeWpa2,
       "hwWidsAttackDetorFirstDetTimeWapi": hwWidsAttackDetorFirstDetTimeWapi,
       "hwOuiWhitelistTable": hwOuiWhitelistTable,
       "hwOuiWhitelistEntry": hwOuiWhitelistEntry,
       "hwOuiWhitelistOui": hwOuiWhitelistOui,
       "hwOuiWhitelistRowStatus": hwOuiWhitelistRowStatus,
       "hwMacAddressWhitelistTable": hwMacAddressWhitelistTable,
       "hwMacAddressWhitelistEntry": hwMacAddressWhitelistEntry,
       "hwMacAddressWhitelistMacAddress": hwMacAddressWhitelistMacAddress,
       "hwMacAddressWhitelistRowStatus": hwMacAddressWhitelistRowStatus,
       "hwWidsSpoofSsidRuleListTable": hwWidsSpoofSsidRuleListTable,
       "hwWidsSpoofSsidRuleListEntry": hwWidsSpoofSsidRuleListEntry,
       "hwWidsSpoofSsidRule": hwWidsSpoofSsidRule,
       "hwWidsSpoofSsidRuleListRowStatus": hwWidsSpoofSsidRuleListRowStatus,
       "hwWlanWidsConformance": hwWlanWidsConformance,
       "hwWlanWidsCompliances": hwWlanWidsCompliances,
       "hwWlanWidsCompliance": hwWlanWidsCompliance,
       "hwWlanWidsObjectGroups": hwWlanWidsObjectGroups,
       "hwWlanWidsMIBNotifyObjectGroup": hwWlanWidsMIBNotifyObjectGroup,
       "hwWlanWidsMIBNotifyGroup": hwWlanWidsMIBNotifyGroup,
       "hwWlanWidsGlobalOptGroup": hwWlanWidsGlobalOptGroup,
       "hwWidsDetDevGroup": hwWidsDetDevGroup,
       "hwWidsDetDevMonitorGroup": hwWidsDetDevMonitorGroup,
       "hwWidsRogueHistoryGroup": hwWidsRogueHistoryGroup,
       "hwSsidWhitelistGroup": hwSsidWhitelistGroup,
       "hwWidsDetNonWifiDevGroup": hwWidsDetNonWifiDevGroup,
       "hwWidsAttackHistoryGroup": hwWidsAttackHistoryGroup,
       "hwWidsEnableAPGroup": hwWidsEnableAPGroup,
       "hwWidsAttackStatGroup": hwWidsAttackStatGroup,
       "hwWidsDynamicBlacklistGroup": hwWidsDynamicBlacklistGroup,
       "hwWidsDynamicBlacklistAPGroup": hwWidsDynamicBlacklistAPGroup,
       "hwWidsDetNonWifiDevHistGroup": hwWidsDetNonWifiDevHistGroup,
       "hwWidsAttackDevGroup": hwWidsAttackDevGroup,
       "hwWidsAttackDetorGroup": hwWidsAttackDetorGroup,
       "hwWidsOuiWhitelistGroup": hwWidsOuiWhitelistGroup,
       "hwWidsMacAddressWhitelistGroup": hwWidsMacAddressWhitelistGroup,
       "hwWidsSpoofSsidRuleGroup": hwWidsSpoofSsidRuleGroup}
)
