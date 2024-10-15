# SNMP MIB module (Zhone-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Zhone-PTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(zhoneGroups,
 zhoneModules,
 zhonePtp,
 zhoneShelfSlotGroup) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneGroups",
    "zhoneModules",
    "zhonePtp",
    "zhoneShelfSlotGroup")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhonePtpModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 119)
)
zhonePtpModule.setRevisions(
        ("2013-05-09 15:15",
         "2012-01-13 14:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhonePtpObjectID_ObjectIdentity = ObjectIdentity
zhonePtpObjectID = _ZhonePtpObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1)
)
_ZhonePtpConfigTable_Object = MibTable
zhonePtpConfigTable = _ZhonePtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1)
)
if mibBuilder.loadTexts:
    zhonePtpConfigTable.setStatus("current")
_ZhonePtpConfigEntry_Object = MibTableRow
zhonePtpConfigEntry = _ZhonePtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1)
)
zhonePtpConfigEntry.setIndexNames(
    (0, "Zhone-PTP-MIB", "zhonePtpConfigIfIndex"),
)
if mibBuilder.loadTexts:
    zhonePtpConfigEntry.setStatus("current")
_ZhonePtpConfigIfIndex_Type = InterfaceIndex
_ZhonePtpConfigIfIndex_Object = MibTableColumn
zhonePtpConfigIfIndex = _ZhonePtpConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 1),
    _ZhonePtpConfigIfIndex_Type()
)
zhonePtpConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhonePtpConfigIfIndex.setStatus("current")


class _ZhonePtpConfigClockMode_Type(Integer32):
    """Custom type zhonePtpConfigClockMode based on Integer32"""
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
        *(("boundary", 3),
          ("forward", 5),
          ("master", 1),
          ("slave", 2),
          ("transparent", 4))
    )


_ZhonePtpConfigClockMode_Type.__name__ = "Integer32"
_ZhonePtpConfigClockMode_Object = MibTableColumn
zhonePtpConfigClockMode = _ZhonePtpConfigClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 2),
    _ZhonePtpConfigClockMode_Type()
)
zhonePtpConfigClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigClockMode.setStatus("current")


class _ZhonePtpConfigSyncMsgInterval_Type(Integer32):
    """Custom type zhonePtpConfigSyncMsgInterval based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_ZhonePtpConfigSyncMsgInterval_Type.__name__ = "Integer32"
_ZhonePtpConfigSyncMsgInterval_Object = MibTableColumn
zhonePtpConfigSyncMsgInterval = _ZhonePtpConfigSyncMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 3),
    _ZhonePtpConfigSyncMsgInterval_Type()
)
zhonePtpConfigSyncMsgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigSyncMsgInterval.setStatus("current")


class _ZhonePtpConfigAnnounceInterval_Type(Integer32):
    """Custom type zhonePtpConfigAnnounceInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_ZhonePtpConfigAnnounceInterval_Type.__name__ = "Integer32"
_ZhonePtpConfigAnnounceInterval_Object = MibTableColumn
zhonePtpConfigAnnounceInterval = _ZhonePtpConfigAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 4),
    _ZhonePtpConfigAnnounceInterval_Type()
)
zhonePtpConfigAnnounceInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigAnnounceInterval.setStatus("current")


class _ZhonePtpConfigDelayReqInterval_Type(Integer32):
    """Custom type zhonePtpConfigDelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_ZhonePtpConfigDelayReqInterval_Type.__name__ = "Integer32"
_ZhonePtpConfigDelayReqInterval_Object = MibTableColumn
zhonePtpConfigDelayReqInterval = _ZhonePtpConfigDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 5),
    _ZhonePtpConfigDelayReqInterval_Type()
)
zhonePtpConfigDelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigDelayReqInterval.setStatus("current")


class _ZhonePtpConfigDomain1MS_Type(Unsigned32):
    """Custom type zhonePtpConfigDomain1MS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePtpConfigDomain1MS_Type.__name__ = "Unsigned32"
_ZhonePtpConfigDomain1MS_Object = MibTableColumn
zhonePtpConfigDomain1MS = _ZhonePtpConfigDomain1MS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 6),
    _ZhonePtpConfigDomain1MS_Type()
)
zhonePtpConfigDomain1MS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigDomain1MS.setStatus("current")


class _ZhonePtpConfigVariance_Type(Unsigned32):
    """Custom type zhonePtpConfigVariance based on Unsigned32"""
    defaultValue = 32767

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhonePtpConfigVariance_Type.__name__ = "Unsigned32"
_ZhonePtpConfigVariance_Object = MibTableColumn
zhonePtpConfigVariance = _ZhonePtpConfigVariance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 7),
    _ZhonePtpConfigVariance_Type()
)
zhonePtpConfigVariance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigVariance.setStatus("current")


class _ZhonePtpConfigPriority1_Type(Unsigned32):
    """Custom type zhonePtpConfigPriority1 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePtpConfigPriority1_Type.__name__ = "Unsigned32"
_ZhonePtpConfigPriority1_Object = MibTableColumn
zhonePtpConfigPriority1 = _ZhonePtpConfigPriority1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 8),
    _ZhonePtpConfigPriority1_Type()
)
zhonePtpConfigPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigPriority1.setStatus("current")


class _ZhonePtpConfigPriority2_Type(Unsigned32):
    """Custom type zhonePtpConfigPriority2 based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePtpConfigPriority2_Type.__name__ = "Unsigned32"
_ZhonePtpConfigPriority2_Object = MibTableColumn
zhonePtpConfigPriority2 = _ZhonePtpConfigPriority2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 9),
    _ZhonePtpConfigPriority2_Type()
)
zhonePtpConfigPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigPriority2.setStatus("current")


class _ZhonePtpConfigDomain2M_Type(Integer32):
    """Custom type zhonePtpConfigDomain2M based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePtpConfigDomain2M_Type.__name__ = "Integer32"
_ZhonePtpConfigDomain2M_Object = MibTableColumn
zhonePtpConfigDomain2M = _ZhonePtpConfigDomain2M_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 10),
    _ZhonePtpConfigDomain2M_Type()
)
zhonePtpConfigDomain2M.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigDomain2M.setStatus("current")
_ZhonePtpConfigRowStatus_Type = ZhoneRowStatus
_ZhonePtpConfigRowStatus_Object = MibTableColumn
zhonePtpConfigRowStatus = _ZhonePtpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 11),
    _ZhonePtpConfigRowStatus_Type()
)
zhonePtpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigRowStatus.setStatus("current")
_ZhonePtpConfigIpIfIndex_Type = InterfaceIndex
_ZhonePtpConfigIpIfIndex_Object = MibTableColumn
zhonePtpConfigIpIfIndex = _ZhonePtpConfigIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 12),
    _ZhonePtpConfigIpIfIndex_Type()
)
zhonePtpConfigIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigIpIfIndex.setStatus("current")


class _ZhonePtpConfigAcceptableMaster1_Type(IpAddress):
    """Custom type zhonePtpConfigAcceptableMaster1 based on IpAddress"""
    defaultHexValue = "00000000"


_ZhonePtpConfigAcceptableMaster1_Object = MibTableColumn
zhonePtpConfigAcceptableMaster1 = _ZhonePtpConfigAcceptableMaster1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 13),
    _ZhonePtpConfigAcceptableMaster1_Type()
)
zhonePtpConfigAcceptableMaster1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigAcceptableMaster1.setStatus("current")


class _ZhonePtpConfigAcceptableMaster2_Type(IpAddress):
    """Custom type zhonePtpConfigAcceptableMaster2 based on IpAddress"""
    defaultHexValue = "00000000"


_ZhonePtpConfigAcceptableMaster2_Object = MibTableColumn
zhonePtpConfigAcceptableMaster2 = _ZhonePtpConfigAcceptableMaster2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 1, 1, 14),
    _ZhonePtpConfigAcceptableMaster2_Type()
)
zhonePtpConfigAcceptableMaster2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePtpConfigAcceptableMaster2.setStatus("current")
_ZhonePtpStatusTable_Object = MibTable
zhonePtpStatusTable = _ZhonePtpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2)
)
if mibBuilder.loadTexts:
    zhonePtpStatusTable.setStatus("current")
_ZhonePtpStatusEntry_Object = MibTableRow
zhonePtpStatusEntry = _ZhonePtpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1)
)
zhonePtpStatusEntry.setIndexNames(
    (0, "Zhone-PTP-MIB", "zhonePtpConfigIfIndex"),
)
if mibBuilder.loadTexts:
    zhonePtpStatusEntry.setStatus("current")
_ZhonePtpStatusMacAddress_Type = MacAddress
_ZhonePtpStatusMacAddress_Object = MibTableColumn
zhonePtpStatusMacAddress = _ZhonePtpStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1, 1),
    _ZhonePtpStatusMacAddress_Type()
)
zhonePtpStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePtpStatusMacAddress.setStatus("current")


class _ZhonePtpConfigTimeSource_Type(Integer32):
    """Custom type zhonePtpConfigTimeSource based on Integer32"""
    defaultValue = 8

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
        *(("atom", 1),
          ("gps", 2),
          ("handSet", 6),
          ("internalOscillator", 8),
          ("ntp", 5),
          ("other", 7),
          ("ptp", 4),
          ("radio", 3))
    )


_ZhonePtpConfigTimeSource_Type.__name__ = "Integer32"
_ZhonePtpConfigTimeSource_Object = MibTableColumn
zhonePtpConfigTimeSource = _ZhonePtpConfigTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1, 2),
    _ZhonePtpConfigTimeSource_Type()
)
zhonePtpConfigTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePtpConfigTimeSource.setStatus("current")


class _ZhonePtpConfigClockStratum_Type(Integer32):
    """Custom type zhonePtpConfigClockStratum based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bestClockStratumThatCanBeSlave", 4),
          ("defaultStratum", 7),
          ("force", 1),
          ("primaryReference", 2),
          ("secondaryReference", 3),
          ("stratum3", 5),
          ("stratum4", 6))
    )


_ZhonePtpConfigClockStratum_Type.__name__ = "Integer32"
_ZhonePtpConfigClockStratum_Object = MibTableColumn
zhonePtpConfigClockStratum = _ZhonePtpConfigClockStratum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1, 3),
    _ZhonePtpConfigClockStratum_Type()
)
zhonePtpConfigClockStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePtpConfigClockStratum.setStatus("current")


class _ZhonePtpConfigClockAccuracy_Type(Integer32):
    """Custom type zhonePtpConfigClockAccuracy based on Integer32"""
    defaultValue = 19

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
              19)
        )
    )
    namedValues = NamedValues(
        *(("accUnknown", 19),
          ("gT10S", 18),
          ("mSec1", 10),
          ("mSec10", 12),
          ("mSec100", 14),
          ("mSec25", 13),
          ("mSec250", 15),
          ("mSec2point5", 11),
          ("nSec100", 2),
          ("nSec25", 1),
          ("nSec250", 3),
          ("sec1", 16),
          ("sec10", 17),
          ("uSec1", 4),
          ("uSec10", 6),
          ("uSec100", 8),
          ("uSec25", 7),
          ("uSec250", 9),
          ("uSec2point5", 5))
    )


_ZhonePtpConfigClockAccuracy_Type.__name__ = "Integer32"
_ZhonePtpConfigClockAccuracy_Object = MibTableColumn
zhonePtpConfigClockAccuracy = _ZhonePtpConfigClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1, 4),
    _ZhonePtpConfigClockAccuracy_Type()
)
zhonePtpConfigClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePtpConfigClockAccuracy.setStatus("current")


class _ZhonePtpStatusTxMode_Type(Integer32):
    """Custom type zhonePtpStatusTxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiOnly", 3),
          ("standard", 1),
          ("uniOnly", 2))
    )


_ZhonePtpStatusTxMode_Type.__name__ = "Integer32"
_ZhonePtpStatusTxMode_Object = MibTableColumn
zhonePtpStatusTxMode = _ZhonePtpStatusTxMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 17, 1, 2, 1, 5),
    _ZhonePtpStatusTxMode_Type()
)
zhonePtpStatusTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePtpStatusTxMode.setStatus("current")

# Managed Objects groups

zhonePtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 52)
)
zhonePtpGroup.setObjects(
      *(("Zhone-PTP-MIB", "zhonePtpConfigClockMode"),
        ("Zhone-PTP-MIB", "zhonePtpConfigIpIfIndex"),
        ("Zhone-PTP-MIB", "zhonePtpConfigSyncMsgInterval"),
        ("Zhone-PTP-MIB", "zhonePtpConfigAnnounceInterval"),
        ("Zhone-PTP-MIB", "zhonePtpConfigDelayReqInterval"),
        ("Zhone-PTP-MIB", "zhonePtpConfigTimeSource"),
        ("Zhone-PTP-MIB", "zhonePtpConfigClockStratum"),
        ("Zhone-PTP-MIB", "zhonePtpConfigClockAccuracy"),
        ("Zhone-PTP-MIB", "zhonePtpConfigVariance"),
        ("Zhone-PTP-MIB", "zhonePtpConfigPriority1"),
        ("Zhone-PTP-MIB", "zhonePtpConfigPriority2"),
        ("Zhone-PTP-MIB", "zhonePtpConfigRowStatus"),
        ("Zhone-PTP-MIB", "zhonePtpStatusTxMode"),
        ("Zhone-PTP-MIB", "zhonePtpStatusMacAddress"),
        ("Zhone-PTP-MIB", "zhonePtpConfigDomain2M"),
        ("Zhone-PTP-MIB", "zhonePtpConfigDomain1MS"),
        ("Zhone-PTP-MIB", "zhonePtpConfigAcceptableMaster1"),
        ("Zhone-PTP-MIB", "zhonePtpConfigAcceptableMaster2"))
)
if mibBuilder.loadTexts:
    zhonePtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Zhone-PTP-MIB",
    **{"zhonePtpObjectID": zhonePtpObjectID,
       "zhonePtpConfigTable": zhonePtpConfigTable,
       "zhonePtpConfigEntry": zhonePtpConfigEntry,
       "zhonePtpConfigIfIndex": zhonePtpConfigIfIndex,
       "zhonePtpConfigClockMode": zhonePtpConfigClockMode,
       "zhonePtpConfigSyncMsgInterval": zhonePtpConfigSyncMsgInterval,
       "zhonePtpConfigAnnounceInterval": zhonePtpConfigAnnounceInterval,
       "zhonePtpConfigDelayReqInterval": zhonePtpConfigDelayReqInterval,
       "zhonePtpConfigDomain1MS": zhonePtpConfigDomain1MS,
       "zhonePtpConfigVariance": zhonePtpConfigVariance,
       "zhonePtpConfigPriority1": zhonePtpConfigPriority1,
       "zhonePtpConfigPriority2": zhonePtpConfigPriority2,
       "zhonePtpConfigDomain2M": zhonePtpConfigDomain2M,
       "zhonePtpConfigRowStatus": zhonePtpConfigRowStatus,
       "zhonePtpConfigIpIfIndex": zhonePtpConfigIpIfIndex,
       "zhonePtpConfigAcceptableMaster1": zhonePtpConfigAcceptableMaster1,
       "zhonePtpConfigAcceptableMaster2": zhonePtpConfigAcceptableMaster2,
       "zhonePtpStatusTable": zhonePtpStatusTable,
       "zhonePtpStatusEntry": zhonePtpStatusEntry,
       "zhonePtpStatusMacAddress": zhonePtpStatusMacAddress,
       "zhonePtpConfigTimeSource": zhonePtpConfigTimeSource,
       "zhonePtpConfigClockStratum": zhonePtpConfigClockStratum,
       "zhonePtpConfigClockAccuracy": zhonePtpConfigClockAccuracy,
       "zhonePtpStatusTxMode": zhonePtpStatusTxMode,
       "zhonePtpModule": zhonePtpModule,
       "zhonePtpGroup": zhonePtpGroup}
)
