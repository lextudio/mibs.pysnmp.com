# SNMP MIB module (HUAWEI-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:43 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180)
)
hwAlarmMIB.setRevisions(
        ("2013-10-28 09:43",
         "2013-10-18 16:43",
         "2009-12-05 11:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwAlarmObjects_ObjectIdentity = ObjectIdentity
hwAlarmObjects = _HwAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1)
)
_HwSnmpTargetAddrExtTable_Object = MibTable
hwSnmpTargetAddrExtTable = _HwSnmpTargetAddrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1)
)
if mibBuilder.loadTexts:
    hwSnmpTargetAddrExtTable.setStatus("current")
_HwSnmpTargetAddrExtEntry_Object = MibTableRow
hwSnmpTargetAddrExtEntry = _HwSnmpTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1)
)
hwSnmpTargetAddrExtEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
)
if mibBuilder.loadTexts:
    hwSnmpTargetAddrExtEntry.setStatus("current")


class _HwSnmpTargetAddrExtIndex_Type(OctetString):
    """Custom type hwSnmpTargetAddrExtIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwSnmpTargetAddrExtIndex_Type.__name__ = "OctetString"
_HwSnmpTargetAddrExtIndex_Object = MibTableColumn
hwSnmpTargetAddrExtIndex = _HwSnmpTargetAddrExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 1),
    _HwSnmpTargetAddrExtIndex_Type()
)
hwSnmpTargetAddrExtIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSnmpTargetAddrExtIndex.setStatus("current")


class _HwSnmpTargetSlaveAddressList_Type(OctetString):
    """Custom type hwSnmpTargetSlaveAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSnmpTargetSlaveAddressList_Type.__name__ = "OctetString"
_HwSnmpTargetSlaveAddressList_Object = MibTableColumn
hwSnmpTargetSlaveAddressList = _HwSnmpTargetSlaveAddressList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 2),
    _HwSnmpTargetSlaveAddressList_Type()
)
hwSnmpTargetSlaveAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSnmpTargetSlaveAddressList.setStatus("current")


class _HwSnmpTargetAddrReliability_Type(Integer32):
    """Custom type hwSnmpTargetAddrReliability based on Integer32"""
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


_HwSnmpTargetAddrReliability_Type.__name__ = "Integer32"
_HwSnmpTargetAddrReliability_Object = MibTableColumn
hwSnmpTargetAddrReliability = _HwSnmpTargetAddrReliability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 3),
    _HwSnmpTargetAddrReliability_Type()
)
hwSnmpTargetAddrReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnmpTargetAddrReliability.setStatus("current")


class _HwSnmpTargetAddrAlarmReliability_Type(Integer32):
    """Custom type hwSnmpTargetAddrAlarmReliability based on Integer32"""
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


_HwSnmpTargetAddrAlarmReliability_Type.__name__ = "Integer32"
_HwSnmpTargetAddrAlarmReliability_Object = MibTableColumn
hwSnmpTargetAddrAlarmReliability = _HwSnmpTargetAddrAlarmReliability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 4),
    _HwSnmpTargetAddrAlarmReliability_Type()
)
hwSnmpTargetAddrAlarmReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnmpTargetAddrAlarmReliability.setStatus("current")


class _HwSnmpTargetAddrEventReliability_Type(Integer32):
    """Custom type hwSnmpTargetAddrEventReliability based on Integer32"""
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


_HwSnmpTargetAddrEventReliability_Type.__name__ = "Integer32"
_HwSnmpTargetAddrEventReliability_Object = MibTableColumn
hwSnmpTargetAddrEventReliability = _HwSnmpTargetAddrEventReliability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 5),
    _HwSnmpTargetAddrEventReliability_Type()
)
hwSnmpTargetAddrEventReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnmpTargetAddrEventReliability.setStatus("current")
_HwSnmpTargetAddrExtRowStatus_Type = RowStatus
_HwSnmpTargetAddrExtRowStatus_Object = MibTableColumn
hwSnmpTargetAddrExtRowStatus = _HwSnmpTargetAddrExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 6),
    _HwSnmpTargetAddrExtRowStatus_Type()
)
hwSnmpTargetAddrExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSnmpTargetAddrExtRowStatus.setStatus("current")
_HwMinAlarmSyncIndex_Type = Integer32
_HwMinAlarmSyncIndex_Object = MibScalar
hwMinAlarmSyncIndex = _HwMinAlarmSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 2),
    _HwMinAlarmSyncIndex_Type()
)
hwMinAlarmSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinAlarmSyncIndex.setStatus("current")
_HwMaxAlarmSyncIndex_Type = Integer32
_HwMaxAlarmSyncIndex_Object = MibScalar
hwMaxAlarmSyncIndex = _HwMaxAlarmSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 3),
    _HwMaxAlarmSyncIndex_Type()
)
hwMaxAlarmSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxAlarmSyncIndex.setStatus("current")
_HwAlarmSyncTable_Object = MibTable
hwAlarmSyncTable = _HwAlarmSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4)
)
if mibBuilder.loadTexts:
    hwAlarmSyncTable.setStatus("current")
_HwAlarmSyncEntry_Object = MibTableRow
hwAlarmSyncEntry = _HwAlarmSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1)
)
hwAlarmSyncEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
    (0, "HUAWEI-ALARM-MIB", "hwAlarmSyncIndex"),
)
if mibBuilder.loadTexts:
    hwAlarmSyncEntry.setStatus("current")


class _HwAlarmSyncIndex_Type(Unsigned32):
    """Custom type hwAlarmSyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwAlarmSyncIndex_Type.__name__ = "Unsigned32"
_HwAlarmSyncIndex_Object = MibTableColumn
hwAlarmSyncIndex = _HwAlarmSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 1),
    _HwAlarmSyncIndex_Type()
)
hwAlarmSyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmSyncIndex.setStatus("current")
_HwAlarmSyncId_Type = Counter64
_HwAlarmSyncId_Object = MibTableColumn
hwAlarmSyncId = _HwAlarmSyncId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 2),
    _HwAlarmSyncId_Type()
)
hwAlarmSyncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmSyncId.setStatus("current")


class _HwAlarmSyncPara_Type(OctetString):
    """Custom type hwAlarmSyncPara based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_HwAlarmSyncPara_Type.__name__ = "OctetString"
_HwAlarmSyncPara_Object = MibTableColumn
hwAlarmSyncPara = _HwAlarmSyncPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 3),
    _HwAlarmSyncPara_Type()
)
hwAlarmSyncPara.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmSyncPara.setStatus("current")


class _HwMinEventSyncIndex_Type(Unsigned32):
    """Custom type hwMinEventSyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwMinEventSyncIndex_Type.__name__ = "Unsigned32"
_HwMinEventSyncIndex_Object = MibScalar
hwMinEventSyncIndex = _HwMinEventSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 5),
    _HwMinEventSyncIndex_Type()
)
hwMinEventSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinEventSyncIndex.setStatus("current")


class _HwMaxEventSyncIndex_Type(Unsigned32):
    """Custom type hwMaxEventSyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwMaxEventSyncIndex_Type.__name__ = "Unsigned32"
_HwMaxEventSyncIndex_Object = MibScalar
hwMaxEventSyncIndex = _HwMaxEventSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 6),
    _HwMaxEventSyncIndex_Type()
)
hwMaxEventSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxEventSyncIndex.setStatus("current")
_HwEventSyncTable_Object = MibTable
hwEventSyncTable = _HwEventSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7)
)
if mibBuilder.loadTexts:
    hwEventSyncTable.setStatus("current")
_HwEventSyncEntry_Object = MibTableRow
hwEventSyncEntry = _HwEventSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1)
)
hwEventSyncEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
    (0, "HUAWEI-ALARM-MIB", "hwEventSyncIndex"),
)
if mibBuilder.loadTexts:
    hwEventSyncEntry.setStatus("current")


class _HwEventSyncIndex_Type(Unsigned32):
    """Custom type hwEventSyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwEventSyncIndex_Type.__name__ = "Unsigned32"
_HwEventSyncIndex_Object = MibTableColumn
hwEventSyncIndex = _HwEventSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 1),
    _HwEventSyncIndex_Type()
)
hwEventSyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEventSyncIndex.setStatus("current")
_HwEventSyncId_Type = Counter64
_HwEventSyncId_Object = MibTableColumn
hwEventSyncId = _HwEventSyncId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 2),
    _HwEventSyncId_Type()
)
hwEventSyncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventSyncId.setStatus("current")


class _HwEventSyncPara_Type(OctetString):
    """Custom type hwEventSyncPara based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_HwEventSyncPara_Type.__name__ = "OctetString"
_HwEventSyncPara_Object = MibTableColumn
hwEventSyncPara = _HwEventSyncPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 3),
    _HwEventSyncPara_Type()
)
hwEventSyncPara.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventSyncPara.setStatus("current")
_HwAlarmActiveTable_Object = MibTable
hwAlarmActiveTable = _HwAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8)
)
if mibBuilder.loadTexts:
    hwAlarmActiveTable.setStatus("current")
_HwAlarmActiveEntry_Object = MibTableRow
hwAlarmActiveEntry = _HwAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1)
)
hwAlarmActiveEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
    (0, "HUAWEI-ALARM-MIB", "hwActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    hwAlarmActiveEntry.setStatus("current")


class _HwActiveAlarmIndex_Type(Unsigned32):
    """Custom type hwActiveAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwActiveAlarmIndex_Type.__name__ = "Unsigned32"
_HwActiveAlarmIndex_Object = MibTableColumn
hwActiveAlarmIndex = _HwActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 1),
    _HwActiveAlarmIndex_Type()
)
hwActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwActiveAlarmIndex.setStatus("current")
_HwActiveAlarmId_Type = Counter64
_HwActiveAlarmId_Object = MibTableColumn
hwActiveAlarmId = _HwActiveAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 2),
    _HwActiveAlarmId_Type()
)
hwActiveAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwActiveAlarmId.setStatus("current")


class _HwActiveAlarmPara_Type(OctetString):
    """Custom type hwActiveAlarmPara based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_HwActiveAlarmPara_Type.__name__ = "OctetString"
_HwActiveAlarmPara_Object = MibTableColumn
hwActiveAlarmPara = _HwActiveAlarmPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 3),
    _HwActiveAlarmPara_Type()
)
hwActiveAlarmPara.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwActiveAlarmPara.setStatus("current")
_HwActiveAlarmRowStatus_Type = RowStatus
_HwActiveAlarmRowStatus_Object = MibTableColumn
hwActiveAlarmRowStatus = _HwActiveAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 4),
    _HwActiveAlarmRowStatus_Type()
)
hwActiveAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwActiveAlarmRowStatus.setStatus("current")
_HwEventTable_Object = MibTable
hwEventTable = _HwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9)
)
if mibBuilder.loadTexts:
    hwEventTable.setStatus("current")
_HwEventEntry_Object = MibTableRow
hwEventEntry = _HwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1)
)
hwEventEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
    (0, "HUAWEI-ALARM-MIB", "hwEventIndex"),
)
if mibBuilder.loadTexts:
    hwEventEntry.setStatus("current")


class _HwEventIndex_Type(Unsigned32):
    """Custom type hwEventIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwEventIndex_Type.__name__ = "Unsigned32"
_HwEventIndex_Object = MibTableColumn
hwEventIndex = _HwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 1),
    _HwEventIndex_Type()
)
hwEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEventIndex.setStatus("current")
_HwEventId_Type = Counter64
_HwEventId_Object = MibTableColumn
hwEventId = _HwEventId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 2),
    _HwEventId_Type()
)
hwEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventId.setStatus("current")


class _HwEventPara_Type(OctetString):
    """Custom type hwEventPara based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_HwEventPara_Type.__name__ = "OctetString"
_HwEventPara_Object = MibTableColumn
hwEventPara = _HwEventPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 3),
    _HwEventPara_Type()
)
hwEventPara.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventPara.setStatus("current")
_HwEventRowStatus_Type = RowStatus
_HwEventRowStatus_Object = MibTableColumn
hwEventRowStatus = _HwEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 4),
    _HwEventRowStatus_Type()
)
hwEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEventRowStatus.setStatus("current")
_HwAlarmDateAndTime_Type = DateAndTime
_HwAlarmDateAndTime_Object = MibScalar
hwAlarmDateAndTime = _HwAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 18),
    _HwAlarmDateAndTime_Type()
)
hwAlarmDateAndTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmDateAndTime.setStatus("current")


class _HwAlarmOrEventFlag_Type(Integer32):
    """Custom type hwAlarmOrEventFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("event", 2))
    )


_HwAlarmOrEventFlag_Type.__name__ = "Integer32"
_HwAlarmOrEventFlag_Object = MibScalar
hwAlarmOrEventFlag = _HwAlarmOrEventFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 19),
    _HwAlarmOrEventFlag_Type()
)
hwAlarmOrEventFlag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmOrEventFlag.setStatus("current")


class _HwAlarmReasonInfo_Type(OctetString):
    """Custom type hwAlarmReasonInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwAlarmReasonInfo_Type.__name__ = "OctetString"
_HwAlarmReasonInfo_Object = MibScalar
hwAlarmReasonInfo = _HwAlarmReasonInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 20),
    _HwAlarmReasonInfo_Type()
)
hwAlarmReasonInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmReasonInfo.setStatus("current")


class _HwAlarmSeverity_Type(Integer32):
    """Custom type hwAlarmSeverity based on Integer32"""
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
        *(("cleared", 6),
          ("critical", 1),
          ("indeterminate", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_HwAlarmSeverity_Type.__name__ = "Integer32"
_HwAlarmSeverity_Object = MibScalar
hwAlarmSeverity = _HwAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 25),
    _HwAlarmSeverity_Type()
)
hwAlarmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmSeverity.setStatus("current")
_HwSnmpTargetSyncIndexTable_Object = MibTable
hwSnmpTargetSyncIndexTable = _HwSnmpTargetSyncIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28)
)
if mibBuilder.loadTexts:
    hwSnmpTargetSyncIndexTable.setStatus("current")
_HwSnmpTargetSyncIndexEntry_Object = MibTableRow
hwSnmpTargetSyncIndexEntry = _HwSnmpTargetSyncIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1)
)
hwSnmpTargetSyncIndexEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
)
if mibBuilder.loadTexts:
    hwSnmpTargetSyncIndexEntry.setStatus("current")
_HwMinAlmSyncIndex_Type = Unsigned32
_HwMinAlmSyncIndex_Object = MibTableColumn
hwMinAlmSyncIndex = _HwMinAlmSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 1),
    _HwMinAlmSyncIndex_Type()
)
hwMinAlmSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinAlmSyncIndex.setStatus("current")
_HwMaxAlmSyncIndex_Type = Unsigned32
_HwMaxAlmSyncIndex_Object = MibTableColumn
hwMaxAlmSyncIndex = _HwMaxAlmSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 2),
    _HwMaxAlmSyncIndex_Type()
)
hwMaxAlmSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxAlmSyncIndex.setStatus("current")
_HwMinEvtSyncIndex_Type = Unsigned32
_HwMinEvtSyncIndex_Object = MibTableColumn
hwMinEvtSyncIndex = _HwMinEvtSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 3),
    _HwMinEvtSyncIndex_Type()
)
hwMinEvtSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMinEvtSyncIndex.setStatus("current")
_HwMaxEvtSyncIndex_Type = Unsigned32
_HwMaxEvtSyncIndex_Object = MibTableColumn
hwMaxEvtSyncIndex = _HwMaxEvtSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 4),
    _HwMaxEvtSyncIndex_Type()
)
hwMaxEvtSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxEvtSyncIndex.setStatus("current")
_HwAlarmActiveVsTable_Object = MibTable
hwAlarmActiveVsTable = _HwAlarmActiveVsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31)
)
if mibBuilder.loadTexts:
    hwAlarmActiveVsTable.setStatus("current")
_HwAlarmActiveVsEntry_Object = MibTableRow
hwAlarmActiveVsEntry = _HwAlarmActiveVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31, 1)
)
if mibBuilder.loadTexts:
    hwAlarmActiveVsEntry.setStatus("current")
_HwAlarmActiveVsId_Type = Unsigned32
_HwAlarmActiveVsId_Object = MibTableColumn
hwAlarmActiveVsId = _HwAlarmActiveVsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31, 1, 9),
    _HwAlarmActiveVsId_Type()
)
hwAlarmActiveVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmActiveVsId.setStatus("current")
_HwEventVsTable_Object = MibTable
hwEventVsTable = _HwEventVsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33)
)
if mibBuilder.loadTexts:
    hwEventVsTable.setStatus("current")
_HwEventVsEntry_Object = MibTableRow
hwEventVsEntry = _HwEventVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33, 1)
)
if mibBuilder.loadTexts:
    hwEventVsEntry.setStatus("current")
_HwEventVsId_Type = Unsigned32
_HwEventVsId_Object = MibTableColumn
hwEventVsId = _HwEventVsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33, 1, 9),
    _HwEventVsId_Type()
)
hwEventVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventVsId.setStatus("current")
_HwAlarmSyncVsTable_Object = MibTable
hwAlarmSyncVsTable = _HwAlarmSyncVsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36)
)
if mibBuilder.loadTexts:
    hwAlarmSyncVsTable.setStatus("current")
_HwAlarmSyncVsEntry_Object = MibTableRow
hwAlarmSyncVsEntry = _HwAlarmSyncVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36, 1)
)
if mibBuilder.loadTexts:
    hwAlarmSyncVsEntry.setStatus("current")
_HwAlarmSyncVsId_Type = Unsigned32
_HwAlarmSyncVsId_Object = MibTableColumn
hwAlarmSyncVsId = _HwAlarmSyncVsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36, 1, 3),
    _HwAlarmSyncVsId_Type()
)
hwAlarmSyncVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmSyncVsId.setStatus("current")
_HwEventSyncVsTable_Object = MibTable
hwEventSyncVsTable = _HwEventSyncVsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39)
)
if mibBuilder.loadTexts:
    hwEventSyncVsTable.setStatus("current")
_HwEventSyncVsEntry_Object = MibTableRow
hwEventSyncVsEntry = _HwEventSyncVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39, 1)
)
if mibBuilder.loadTexts:
    hwEventSyncVsEntry.setStatus("current")
_HwEvevtSyncVsId_Type = Unsigned32
_HwEvevtSyncVsId_Object = MibTableColumn
hwEvevtSyncVsId = _HwEvevtSyncVsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39, 1, 3),
    _HwEvevtSyncVsId_Type()
)
hwEvevtSyncVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEvevtSyncVsId.setStatus("current")
_HwAlarmNotifications_ObjectIdentity = ObjectIdentity
hwAlarmNotifications = _HwAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2)
)
_HwAlarmConformance_ObjectIdentity = ObjectIdentity
hwAlarmConformance = _HwAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3)
)
_HwAlarmCompliances_ObjectIdentity = ObjectIdentity
hwAlarmCompliances = _HwAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 1)
)
_HwAlarmGroups_ObjectIdentity = ObjectIdentity
hwAlarmGroups = _HwAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2)
)
_HwAlarmConfig_ObjectIdentity = ObjectIdentity
hwAlarmConfig = _HwAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5)
)
_HwAlarmAttr_ObjectIdentity = ObjectIdentity
hwAlarmAttr = _HwAlarmAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1)
)
_HwAlarmAttrTable_Object = MibTable
hwAlarmAttrTable = _HwAlarmAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwAlarmAttrTable.setStatus("current")
_HwAlarmAttrEntry_Object = MibTableRow
hwAlarmAttrEntry = _HwAlarmAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1)
)
hwAlarmAttrEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwAlarmName"),
)
if mibBuilder.loadTexts:
    hwAlarmAttrEntry.setStatus("current")


class _HwAlarmName_Type(OctetString):
    """Custom type hwAlarmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAlarmName_Type.__name__ = "OctetString"
_HwAlarmName_Object = MibTableColumn
hwAlarmName = _HwAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1, 1),
    _HwAlarmName_Type()
)
hwAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmName.setStatus("current")


class _HwAlarmAttrSeverity_Type(Integer32):
    """Custom type hwAlarmAttrSeverity based on Integer32"""
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
        *(("cleared", 6),
          ("critical", 1),
          ("indeterminate", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_HwAlarmAttrSeverity_Type.__name__ = "Integer32"
_HwAlarmAttrSeverity_Object = MibTableColumn
hwAlarmAttrSeverity = _HwAlarmAttrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1, 2),
    _HwAlarmAttrSeverity_Type()
)
hwAlarmAttrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmAttrSeverity.setStatus("current")
_HwAlarmMask_ObjectIdentity = ObjectIdentity
hwAlarmMask = _HwAlarmMask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3)
)
_HwAlarmMaskBasedOnIfnameTable_Object = MibTable
hwAlarmMaskBasedOnIfnameTable = _HwAlarmMaskBasedOnIfnameTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1)
)
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnIfnameTable.setStatus("current")
_HwAlarmMaskBasedOnIfnameEntry_Object = MibTableRow
hwAlarmMaskBasedOnIfnameEntry = _HwAlarmMaskBasedOnIfnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1)
)
hwAlarmMaskBasedOnIfnameEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwAlarmMaskIfName"),
)
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnIfnameEntry.setStatus("current")
_HwAlarmMaskIfName_Type = OctetString
_HwAlarmMaskIfName_Object = MibTableColumn
hwAlarmMaskIfName = _HwAlarmMaskIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1, 1),
    _HwAlarmMaskIfName_Type()
)
hwAlarmMaskIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmMaskIfName.setStatus("current")
_HwAlarmMaskBasedOnIfnameRowStatus_Type = RowStatus
_HwAlarmMaskBasedOnIfnameRowStatus_Object = MibTableColumn
hwAlarmMaskBasedOnIfnameRowStatus = _HwAlarmMaskBasedOnIfnameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1, 51),
    _HwAlarmMaskBasedOnIfnameRowStatus_Type()
)
hwAlarmMaskBasedOnIfnameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnIfnameRowStatus.setStatus("current")
_HwAlarmMaskBasedOnEntityTable_Object = MibTable
hwAlarmMaskBasedOnEntityTable = _HwAlarmMaskBasedOnEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2)
)
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnEntityTable.setStatus("current")
_HwAlarmMaskBasedOnEntityEntry_Object = MibTableRow
hwAlarmMaskBasedOnEntityEntry = _HwAlarmMaskBasedOnEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1)
)
hwAlarmMaskBasedOnEntityEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwAlarmMaskEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnEntityEntry.setStatus("current")
_HwAlarmMaskEntPhysicalIndex_Type = Integer32
_HwAlarmMaskEntPhysicalIndex_Object = MibTableColumn
hwAlarmMaskEntPhysicalIndex = _HwAlarmMaskEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 1),
    _HwAlarmMaskEntPhysicalIndex_Type()
)
hwAlarmMaskEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmMaskEntPhysicalIndex.setStatus("current")
_HwAlarmMaskEntPhysicalName_Type = OctetString
_HwAlarmMaskEntPhysicalName_Object = MibTableColumn
hwAlarmMaskEntPhysicalName = _HwAlarmMaskEntPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 2),
    _HwAlarmMaskEntPhysicalName_Type()
)
hwAlarmMaskEntPhysicalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmMaskEntPhysicalName.setStatus("current")
_HwAlarmMaskBasedOnEntityRowStatus_Type = RowStatus
_HwAlarmMaskBasedOnEntityRowStatus_Object = MibTableColumn
hwAlarmMaskBasedOnEntityRowStatus = _HwAlarmMaskBasedOnEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 51),
    _HwAlarmMaskBasedOnEntityRowStatus_Type()
)
hwAlarmMaskBasedOnEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAlarmMaskBasedOnEntityRowStatus.setStatus("current")
_HwAlarmDelay_ObjectIdentity = ObjectIdentity
hwAlarmDelay = _HwAlarmDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4)
)


class _HwAlarmDelaySuppressionEnable_Type(Integer32):
    """Custom type hwAlarmDelaySuppressionEnable based on Integer32"""
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


_HwAlarmDelaySuppressionEnable_Type.__name__ = "Integer32"
_HwAlarmDelaySuppressionEnable_Object = MibScalar
hwAlarmDelaySuppressionEnable = _HwAlarmDelaySuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 1),
    _HwAlarmDelaySuppressionEnable_Type()
)
hwAlarmDelaySuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmDelaySuppressionEnable.setStatus("current")
_HwAlarmDelaySuppressionTable_Object = MibTable
hwAlarmDelaySuppressionTable = _HwAlarmDelaySuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2)
)
if mibBuilder.loadTexts:
    hwAlarmDelaySuppressionTable.setStatus("current")
_HwAlarmDelaySuppressionEntry_Object = MibTableRow
hwAlarmDelaySuppressionEntry = _HwAlarmDelaySuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1)
)
hwAlarmDelaySuppressionEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwAlarmName"),
)
if mibBuilder.loadTexts:
    hwAlarmDelaySuppressionEntry.setStatus("current")


class _HwAlarmDelaySuppressionCausePersistPeriod_Type(Integer32):
    """Custom type hwAlarmDelaySuppressionCausePersistPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwAlarmDelaySuppressionCausePersistPeriod_Type.__name__ = "Integer32"
_HwAlarmDelaySuppressionCausePersistPeriod_Object = MibTableColumn
hwAlarmDelaySuppressionCausePersistPeriod = _HwAlarmDelaySuppressionCausePersistPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1, 1),
    _HwAlarmDelaySuppressionCausePersistPeriod_Type()
)
hwAlarmDelaySuppressionCausePersistPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmDelaySuppressionCausePersistPeriod.setStatus("current")


class _HwAlarmDelaySuppressionClearPersistPeriod_Type(Integer32):
    """Custom type hwAlarmDelaySuppressionClearPersistPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwAlarmDelaySuppressionClearPersistPeriod_Type.__name__ = "Integer32"
_HwAlarmDelaySuppressionClearPersistPeriod_Object = MibTableColumn
hwAlarmDelaySuppressionClearPersistPeriod = _HwAlarmDelaySuppressionClearPersistPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1, 2),
    _HwAlarmDelaySuppressionClearPersistPeriod_Type()
)
hwAlarmDelaySuppressionClearPersistPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmDelaySuppressionClearPersistPeriod.setStatus("current")
_HwAlarmCorrAnalyze_ObjectIdentity = ObjectIdentity
hwAlarmCorrAnalyze = _HwAlarmCorrAnalyze_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5)
)


class _HwAlarmCorrAnalyzeSuppressionEnable_Type(Integer32):
    """Custom type hwAlarmCorrAnalyzeSuppressionEnable based on Integer32"""
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


_HwAlarmCorrAnalyzeSuppressionEnable_Type.__name__ = "Integer32"
_HwAlarmCorrAnalyzeSuppressionEnable_Object = MibScalar
hwAlarmCorrAnalyzeSuppressionEnable = _HwAlarmCorrAnalyzeSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 1),
    _HwAlarmCorrAnalyzeSuppressionEnable_Type()
)
hwAlarmCorrAnalyzeSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionEnable.setStatus("current")


class _HwAlarmCorrAnalyzeSuppressionRootCauseIndication_Type(Integer32):
    """Custom type hwAlarmCorrAnalyzeSuppressionRootCauseIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 0),
          ("nonrootcause", 2),
          ("rootcause", 1))
    )


_HwAlarmCorrAnalyzeSuppressionRootCauseIndication_Type.__name__ = "Integer32"
_HwAlarmCorrAnalyzeSuppressionRootCauseIndication_Object = MibScalar
hwAlarmCorrAnalyzeSuppressionRootCauseIndication = _HwAlarmCorrAnalyzeSuppressionRootCauseIndication_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 2),
    _HwAlarmCorrAnalyzeSuppressionRootCauseIndication_Type()
)
hwAlarmCorrAnalyzeSuppressionRootCauseIndication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionRootCauseIndication.setStatus("current")
_HwAlarmCorrAnalyzeSuppressionParentSequence_Type = OctetString
_HwAlarmCorrAnalyzeSuppressionParentSequence_Object = MibScalar
hwAlarmCorrAnalyzeSuppressionParentSequence = _HwAlarmCorrAnalyzeSuppressionParentSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 3),
    _HwAlarmCorrAnalyzeSuppressionParentSequence_Type()
)
hwAlarmCorrAnalyzeSuppressionParentSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionParentSequence.setStatus("current")
_HwAlarmCorrAnalyzeSuppressionTable_Object = MibTable
hwAlarmCorrAnalyzeSuppressionTable = _HwAlarmCorrAnalyzeSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4)
)
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionTable.setStatus("current")
_HwAlarmCorrAnalyzeSuppressionEntry_Object = MibTableRow
hwAlarmCorrAnalyzeSuppressionEntry = _HwAlarmCorrAnalyzeSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4, 1)
)
hwAlarmCorrAnalyzeSuppressionEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"),
)
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionEntry.setStatus("current")


class _HwAlarmCorrAnalyzeSuppressionStatus_Type(Integer32):
    """Custom type hwAlarmCorrAnalyzeSuppressionStatus based on Integer32"""
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


_HwAlarmCorrAnalyzeSuppressionStatus_Type.__name__ = "Integer32"
_HwAlarmCorrAnalyzeSuppressionStatus_Object = MibTableColumn
hwAlarmCorrAnalyzeSuppressionStatus = _HwAlarmCorrAnalyzeSuppressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4, 1, 1),
    _HwAlarmCorrAnalyzeSuppressionStatus_Type()
)
hwAlarmCorrAnalyzeSuppressionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAlarmCorrAnalyzeSuppressionStatus.setStatus("current")
_HwEventConfig_ObjectIdentity = ObjectIdentity
hwEventConfig = _HwEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6)
)
_HwEventAttr_ObjectIdentity = ObjectIdentity
hwEventAttr = _HwEventAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1)
)
_HwEventAttrTable_Object = MibTable
hwEventAttrTable = _HwEventAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwEventAttrTable.setStatus("current")
_HwEventAttrEntry_Object = MibTableRow
hwEventAttrEntry = _HwEventAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1)
)
hwEventAttrEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwEventName"),
)
if mibBuilder.loadTexts:
    hwEventAttrEntry.setStatus("current")


class _HwEventName_Type(OctetString):
    """Custom type hwEventName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwEventName_Type.__name__ = "OctetString"
_HwEventName_Object = MibTableColumn
hwEventName = _HwEventName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1, 1),
    _HwEventName_Type()
)
hwEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventName.setStatus("current")


class _HwEventAttrSeverity_Type(Integer32):
    """Custom type hwEventAttrSeverity based on Integer32"""
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
        *(("cleared", 6),
          ("critical", 1),
          ("indeterminate", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_HwEventAttrSeverity_Type.__name__ = "Integer32"
_HwEventAttrSeverity_Object = MibTableColumn
hwEventAttrSeverity = _HwEventAttrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1, 2),
    _HwEventAttrSeverity_Type()
)
hwEventAttrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEventAttrSeverity.setStatus("current")
_HwEventDelay_ObjectIdentity = ObjectIdentity
hwEventDelay = _HwEventDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4)
)


class _HwEventDelaySuppressionEnable_Type(Integer32):
    """Custom type hwEventDelaySuppressionEnable based on Integer32"""
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


_HwEventDelaySuppressionEnable_Type.__name__ = "Integer32"
_HwEventDelaySuppressionEnable_Object = MibScalar
hwEventDelaySuppressionEnable = _HwEventDelaySuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 1),
    _HwEventDelaySuppressionEnable_Type()
)
hwEventDelaySuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEventDelaySuppressionEnable.setStatus("current")
_HwEventDelaySuppressionTable_Object = MibTable
hwEventDelaySuppressionTable = _HwEventDelaySuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2)
)
if mibBuilder.loadTexts:
    hwEventDelaySuppressionTable.setStatus("current")
_HwEventDelaySuppressionEntry_Object = MibTableRow
hwEventDelaySuppressionEntry = _HwEventDelaySuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2, 1)
)
hwEventDelaySuppressionEntry.setIndexNames(
    (0, "HUAWEI-ALARM-MIB", "hwEventName"),
)
if mibBuilder.loadTexts:
    hwEventDelaySuppressionEntry.setStatus("current")


class _HwEventDelaySuppressionCausePersistPeriod_Type(Integer32):
    """Custom type hwEventDelaySuppressionCausePersistPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwEventDelaySuppressionCausePersistPeriod_Type.__name__ = "Integer32"
_HwEventDelaySuppressionCausePersistPeriod_Object = MibTableColumn
hwEventDelaySuppressionCausePersistPeriod = _HwEventDelaySuppressionCausePersistPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2, 1, 1),
    _HwEventDelaySuppressionCausePersistPeriod_Type()
)
hwEventDelaySuppressionCausePersistPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEventDelaySuppressionCausePersistPeriod.setStatus("current")
hwAlarmActiveEntry.registerAugmentions(
    ("HUAWEI-ALARM-MIB",
     "hwAlarmActiveVsEntry")
)
hwAlarmActiveVsEntry.setIndexNames(*hwAlarmActiveEntry.getIndexNames())
hwEventEntry.registerAugmentions(
    ("HUAWEI-ALARM-MIB",
     "hwEventVsEntry")
)
hwEventVsEntry.setIndexNames(*hwEventEntry.getIndexNames())
hwAlarmSyncEntry.registerAugmentions(
    ("HUAWEI-ALARM-MIB",
     "hwAlarmSyncVsEntry")
)
hwAlarmSyncVsEntry.setIndexNames(*hwAlarmSyncEntry.getIndexNames())
hwEventSyncEntry.registerAugmentions(
    ("HUAWEI-ALARM-MIB",
     "hwEventSyncVsEntry")
)
hwEventSyncVsEntry.setIndexNames(*hwEventSyncEntry.getIndexNames())

# Managed Objects groups

hwAlarmReliabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 1)
)
hwAlarmReliabilityGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwSnmpTargetSlaveAddressList"),
        ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrEventReliability"),
        ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrAlarmReliability"),
        ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrReliability"),
        ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtRowStatus"))
)
if mibBuilder.loadTexts:
    hwAlarmReliabilityGroup.setStatus("current")

hwActiveInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 7)
)
hwActiveInfoGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwActiveAlarmId"),
        ("HUAWEI-ALARM-MIB", "hwActiveAlarmPara"),
        ("HUAWEI-ALARM-MIB", "hwEventRowStatus"),
        ("HUAWEI-ALARM-MIB", "hwActiveAlarmRowStatus"),
        ("HUAWEI-ALARM-MIB", "hwEventId"),
        ("HUAWEI-ALARM-MIB", "hwEventPara"))
)
if mibBuilder.loadTexts:
    hwActiveInfoGroup.setStatus("current")

hwTrapInfoSyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 8)
)
hwTrapInfoSyncGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwMinAlarmSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwMaxAlarmSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwAlarmSyncId"),
        ("HUAWEI-ALARM-MIB", "hwAlarmSyncPara"),
        ("HUAWEI-ALARM-MIB", "hwMinEventSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwMaxEventSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwEventSyncId"),
        ("HUAWEI-ALARM-MIB", "hwEventSyncPara"),
        ("HUAWEI-ALARM-MIB", "hwAlarmDateAndTime"),
        ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionRootCauseIndication"),
        ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionParentSequence"),
        ("HUAWEI-ALARM-MIB", "hwAlarmReasonInfo"),
        ("HUAWEI-ALARM-MIB", "hwAlarmSeverity"),
        ("HUAWEI-ALARM-MIB", "hwAlarmOrEventFlag"))
)
if mibBuilder.loadTexts:
    hwTrapInfoSyncGroup.setStatus("current")

hwActiveInfoVsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 9)
)
hwActiveInfoVsGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwAlarmActiveVsId"),
        ("HUAWEI-ALARM-MIB", "hwEventVsId"))
)
if mibBuilder.loadTexts:
    hwActiveInfoVsGroup.setStatus("current")

hwTrapSyncVsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 10)
)
hwTrapSyncVsGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwAlarmSyncVsId"),
        ("HUAWEI-ALARM-MIB", "hwEvevtSyncVsId"),
        ("HUAWEI-ALARM-MIB", "hwMinAlmSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwMaxAlmSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwMinEvtSyncIndex"),
        ("HUAWEI-ALARM-MIB", "hwMaxEvtSyncIndex"))
)
if mibBuilder.loadTexts:
    hwTrapSyncVsGroup.setStatus("current")

hwTrapSuppressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 12)
)
hwTrapSuppressionGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionEnable"),
        ("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionCausePersistPeriod"),
        ("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionClearPersistPeriod"),
        ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionEnable"),
        ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionStatus"),
        ("HUAWEI-ALARM-MIB", "hwEventDelaySuppressionEnable"),
        ("HUAWEI-ALARM-MIB", "hwEventDelaySuppressionCausePersistPeriod"))
)
if mibBuilder.loadTexts:
    hwTrapSuppressionGroup.setStatus("current")

hwTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 13)
)
hwTrapInfoGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwAlarmAttrSeverity"),
        ("HUAWEI-ALARM-MIB", "hwEventAttrSeverity"))
)
if mibBuilder.loadTexts:
    hwTrapInfoGroup.setStatus("current")


# Notification objects

hwAlarmTargetHostDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2, 1)
)
hwAlarmTargetHostDel.setObjects(
    ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex")
)
if mibBuilder.loadTexts:
    hwAlarmTargetHostDel.setStatus(
        "current"
    )

hwAlarmStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2, 2)
)
if mibBuilder.loadTexts:
    hwAlarmStorm.setStatus(
        "current"
    )


# Notifications groups

hwAlarmTrapInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 11)
)
hwAlarmTrapInfoGroup.setObjects(
      *(("HUAWEI-ALARM-MIB", "hwAlarmTargetHostDel"),
        ("HUAWEI-ALARM-MIB", "hwAlarmStorm"))
)
if mibBuilder.loadTexts:
    hwAlarmTrapInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ALARM-MIB",
    **{"hwAlarmMIB": hwAlarmMIB,
       "hwAlarmObjects": hwAlarmObjects,
       "hwSnmpTargetAddrExtTable": hwSnmpTargetAddrExtTable,
       "hwSnmpTargetAddrExtEntry": hwSnmpTargetAddrExtEntry,
       "hwSnmpTargetAddrExtIndex": hwSnmpTargetAddrExtIndex,
       "hwSnmpTargetSlaveAddressList": hwSnmpTargetSlaveAddressList,
       "hwSnmpTargetAddrReliability": hwSnmpTargetAddrReliability,
       "hwSnmpTargetAddrAlarmReliability": hwSnmpTargetAddrAlarmReliability,
       "hwSnmpTargetAddrEventReliability": hwSnmpTargetAddrEventReliability,
       "hwSnmpTargetAddrExtRowStatus": hwSnmpTargetAddrExtRowStatus,
       "hwMinAlarmSyncIndex": hwMinAlarmSyncIndex,
       "hwMaxAlarmSyncIndex": hwMaxAlarmSyncIndex,
       "hwAlarmSyncTable": hwAlarmSyncTable,
       "hwAlarmSyncEntry": hwAlarmSyncEntry,
       "hwAlarmSyncIndex": hwAlarmSyncIndex,
       "hwAlarmSyncId": hwAlarmSyncId,
       "hwAlarmSyncPara": hwAlarmSyncPara,
       "hwMinEventSyncIndex": hwMinEventSyncIndex,
       "hwMaxEventSyncIndex": hwMaxEventSyncIndex,
       "hwEventSyncTable": hwEventSyncTable,
       "hwEventSyncEntry": hwEventSyncEntry,
       "hwEventSyncIndex": hwEventSyncIndex,
       "hwEventSyncId": hwEventSyncId,
       "hwEventSyncPara": hwEventSyncPara,
       "hwAlarmActiveTable": hwAlarmActiveTable,
       "hwAlarmActiveEntry": hwAlarmActiveEntry,
       "hwActiveAlarmIndex": hwActiveAlarmIndex,
       "hwActiveAlarmId": hwActiveAlarmId,
       "hwActiveAlarmPara": hwActiveAlarmPara,
       "hwActiveAlarmRowStatus": hwActiveAlarmRowStatus,
       "hwEventTable": hwEventTable,
       "hwEventEntry": hwEventEntry,
       "hwEventIndex": hwEventIndex,
       "hwEventId": hwEventId,
       "hwEventPara": hwEventPara,
       "hwEventRowStatus": hwEventRowStatus,
       "hwAlarmDateAndTime": hwAlarmDateAndTime,
       "hwAlarmOrEventFlag": hwAlarmOrEventFlag,
       "hwAlarmReasonInfo": hwAlarmReasonInfo,
       "hwAlarmSeverity": hwAlarmSeverity,
       "hwSnmpTargetSyncIndexTable": hwSnmpTargetSyncIndexTable,
       "hwSnmpTargetSyncIndexEntry": hwSnmpTargetSyncIndexEntry,
       "hwMinAlmSyncIndex": hwMinAlmSyncIndex,
       "hwMaxAlmSyncIndex": hwMaxAlmSyncIndex,
       "hwMinEvtSyncIndex": hwMinEvtSyncIndex,
       "hwMaxEvtSyncIndex": hwMaxEvtSyncIndex,
       "hwAlarmActiveVsTable": hwAlarmActiveVsTable,
       "hwAlarmActiveVsEntry": hwAlarmActiveVsEntry,
       "hwAlarmActiveVsId": hwAlarmActiveVsId,
       "hwEventVsTable": hwEventVsTable,
       "hwEventVsEntry": hwEventVsEntry,
       "hwEventVsId": hwEventVsId,
       "hwAlarmSyncVsTable": hwAlarmSyncVsTable,
       "hwAlarmSyncVsEntry": hwAlarmSyncVsEntry,
       "hwAlarmSyncVsId": hwAlarmSyncVsId,
       "hwEventSyncVsTable": hwEventSyncVsTable,
       "hwEventSyncVsEntry": hwEventSyncVsEntry,
       "hwEvevtSyncVsId": hwEvevtSyncVsId,
       "hwAlarmNotifications": hwAlarmNotifications,
       "hwAlarmTargetHostDel": hwAlarmTargetHostDel,
       "hwAlarmStorm": hwAlarmStorm,
       "hwAlarmConformance": hwAlarmConformance,
       "hwAlarmCompliances": hwAlarmCompliances,
       "hwAlarmCompliance": hwAlarmCompliance,
       "hwAlarmGroups": hwAlarmGroups,
       "hwAlarmReliabilityGroup": hwAlarmReliabilityGroup,
       "hwActiveInfoGroup": hwActiveInfoGroup,
       "hwTrapInfoSyncGroup": hwTrapInfoSyncGroup,
       "hwActiveInfoVsGroup": hwActiveInfoVsGroup,
       "hwTrapSyncVsGroup": hwTrapSyncVsGroup,
       "hwAlarmTrapInfoGroup": hwAlarmTrapInfoGroup,
       "hwTrapSuppressionGroup": hwTrapSuppressionGroup,
       "hwTrapInfoGroup": hwTrapInfoGroup,
       "hwAlarmConfig": hwAlarmConfig,
       "hwAlarmAttr": hwAlarmAttr,
       "hwAlarmAttrTable": hwAlarmAttrTable,
       "hwAlarmAttrEntry": hwAlarmAttrEntry,
       "hwAlarmName": hwAlarmName,
       "hwAlarmAttrSeverity": hwAlarmAttrSeverity,
       "hwAlarmMask": hwAlarmMask,
       "hwAlarmMaskBasedOnIfnameTable": hwAlarmMaskBasedOnIfnameTable,
       "hwAlarmMaskBasedOnIfnameEntry": hwAlarmMaskBasedOnIfnameEntry,
       "hwAlarmMaskIfName": hwAlarmMaskIfName,
       "hwAlarmMaskBasedOnIfnameRowStatus": hwAlarmMaskBasedOnIfnameRowStatus,
       "hwAlarmMaskBasedOnEntityTable": hwAlarmMaskBasedOnEntityTable,
       "hwAlarmMaskBasedOnEntityEntry": hwAlarmMaskBasedOnEntityEntry,
       "hwAlarmMaskEntPhysicalIndex": hwAlarmMaskEntPhysicalIndex,
       "hwAlarmMaskEntPhysicalName": hwAlarmMaskEntPhysicalName,
       "hwAlarmMaskBasedOnEntityRowStatus": hwAlarmMaskBasedOnEntityRowStatus,
       "hwAlarmDelay": hwAlarmDelay,
       "hwAlarmDelaySuppressionEnable": hwAlarmDelaySuppressionEnable,
       "hwAlarmDelaySuppressionTable": hwAlarmDelaySuppressionTable,
       "hwAlarmDelaySuppressionEntry": hwAlarmDelaySuppressionEntry,
       "hwAlarmDelaySuppressionCausePersistPeriod": hwAlarmDelaySuppressionCausePersistPeriod,
       "hwAlarmDelaySuppressionClearPersistPeriod": hwAlarmDelaySuppressionClearPersistPeriod,
       "hwAlarmCorrAnalyze": hwAlarmCorrAnalyze,
       "hwAlarmCorrAnalyzeSuppressionEnable": hwAlarmCorrAnalyzeSuppressionEnable,
       "hwAlarmCorrAnalyzeSuppressionRootCauseIndication": hwAlarmCorrAnalyzeSuppressionRootCauseIndication,
       "hwAlarmCorrAnalyzeSuppressionParentSequence": hwAlarmCorrAnalyzeSuppressionParentSequence,
       "hwAlarmCorrAnalyzeSuppressionTable": hwAlarmCorrAnalyzeSuppressionTable,
       "hwAlarmCorrAnalyzeSuppressionEntry": hwAlarmCorrAnalyzeSuppressionEntry,
       "hwAlarmCorrAnalyzeSuppressionStatus": hwAlarmCorrAnalyzeSuppressionStatus,
       "hwEventConfig": hwEventConfig,
       "hwEventAttr": hwEventAttr,
       "hwEventAttrTable": hwEventAttrTable,
       "hwEventAttrEntry": hwEventAttrEntry,
       "hwEventName": hwEventName,
       "hwEventAttrSeverity": hwEventAttrSeverity,
       "hwEventDelay": hwEventDelay,
       "hwEventDelaySuppressionEnable": hwEventDelaySuppressionEnable,
       "hwEventDelaySuppressionTable": hwEventDelaySuppressionTable,
       "hwEventDelaySuppressionEntry": hwEventDelaySuppressionEntry,
       "hwEventDelaySuppressionCausePersistPeriod": hwEventDelaySuppressionCausePersistPeriod}
)
