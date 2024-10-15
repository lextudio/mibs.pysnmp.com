# SNMP MIB module (HPICF-IPSLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-IPSLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:17 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

hpicfIpSla = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127)
)
hpicfIpSla.setRevisions(
        ("2016-11-10 00:00",
         "2016-10-20 00:00",
         "2016-10-05 00:00",
         "2016-09-29 00:00",
         "2016-09-15 00:00",
         "2016-07-25 00:00",
         "2016-07-07 00:00",
         "2016-06-20 00:00",
         "2016-03-14 00:00",
         "2016-02-16 00:00",
         "2015-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfIpSlaNotifications_ObjectIdentity = ObjectIdentity
hpicfIpSlaNotifications = _HpicfIpSlaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 0)
)
_HpicfIpSlaObjects_ObjectIdentity = ObjectIdentity
hpicfIpSlaObjects = _HpicfIpSlaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1)
)
_HpicfIpSlaTable_Object = MibTable
hpicfIpSlaTable = _HpicfIpSlaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpSlaTable.setStatus("current")
_HpicfIpSlaEntry_Object = MibTableRow
hpicfIpSlaEntry = _HpicfIpSlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1)
)
hpicfIpSlaEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaEntry.setStatus("current")


class _HpicfIpSlaID_Type(Integer32):
    """Custom type hpicfIpSlaID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfIpSlaID_Type.__name__ = "Integer32"
_HpicfIpSlaID_Object = MibTableColumn
hpicfIpSlaID = _HpicfIpSlaID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 1),
    _HpicfIpSlaID_Type()
)
hpicfIpSlaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaID.setStatus("current")


class _HpicfIpSlaType_Type(Integer32):
    """Custom type hpicfIpSlaType based on Integer32"""
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
        *(("dhcp", 6),
          ("dns", 7),
          ("icmpEcho", 1),
          ("tcpConnect", 5),
          ("udpEcho", 2),
          ("udpJitter", 3),
          ("udpJitterVoIP", 4))
    )


_HpicfIpSlaType_Type.__name__ = "Integer32"
_HpicfIpSlaType_Object = MibTableColumn
hpicfIpSlaType = _HpicfIpSlaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 2),
    _HpicfIpSlaType_Type()
)
hpicfIpSlaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaType.setStatus("current")


class _HpicfIpSlaAdminState_Type(Integer32):
    """Custom type hpicfIpSlaAdminState based on Integer32"""
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


_HpicfIpSlaAdminState_Type.__name__ = "Integer32"
_HpicfIpSlaAdminState_Object = MibTableColumn
hpicfIpSlaAdminState = _HpicfIpSlaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 3),
    _HpicfIpSlaAdminState_Type()
)
hpicfIpSlaAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAdminState.setStatus("current")
_HpicfIpSlaSourceAddressType_Type = InetAddressType
_HpicfIpSlaSourceAddressType_Object = MibTableColumn
hpicfIpSlaSourceAddressType = _HpicfIpSlaSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 4),
    _HpicfIpSlaSourceAddressType_Type()
)
hpicfIpSlaSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSourceAddressType.setStatus("current")
_HpicfIpSlaSourceAddress_Type = InetAddress
_HpicfIpSlaSourceAddress_Object = MibTableColumn
hpicfIpSlaSourceAddress = _HpicfIpSlaSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 5),
    _HpicfIpSlaSourceAddress_Type()
)
hpicfIpSlaSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSourceAddress.setStatus("current")
_HpicfIpSlaL4SourcePort_Type = InetPortNumber
_HpicfIpSlaL4SourcePort_Object = MibTableColumn
hpicfIpSlaL4SourcePort = _HpicfIpSlaL4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 6),
    _HpicfIpSlaL4SourcePort_Type()
)
hpicfIpSlaL4SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaL4SourcePort.setStatus("current")
_HpicfIpSlaSourceInterface_Type = InterfaceIndexOrZero
_HpicfIpSlaSourceInterface_Object = MibTableColumn
hpicfIpSlaSourceInterface = _HpicfIpSlaSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 7),
    _HpicfIpSlaSourceInterface_Type()
)
hpicfIpSlaSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSourceInterface.setStatus("current")
_HpicfIpSlaDestAddressType_Type = InetAddressType
_HpicfIpSlaDestAddressType_Object = MibTableColumn
hpicfIpSlaDestAddressType = _HpicfIpSlaDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 8),
    _HpicfIpSlaDestAddressType_Type()
)
hpicfIpSlaDestAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaDestAddressType.setStatus("current")
_HpicfIpSlaDestAddress_Type = InetAddress
_HpicfIpSlaDestAddress_Object = MibTableColumn
hpicfIpSlaDestAddress = _HpicfIpSlaDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 9),
    _HpicfIpSlaDestAddress_Type()
)
hpicfIpSlaDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaDestAddress.setStatus("current")
_HpicfIpSlaL4DestPort_Type = InetPortNumber
_HpicfIpSlaL4DestPort_Object = MibTableColumn
hpicfIpSlaL4DestPort = _HpicfIpSlaL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 10),
    _HpicfIpSlaL4DestPort_Type()
)
hpicfIpSlaL4DestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaL4DestPort.setStatus("current")
_HpicfIpSlaRowStatus_Type = RowStatus
_HpicfIpSlaRowStatus_Object = MibTableColumn
hpicfIpSlaRowStatus = _HpicfIpSlaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 1, 1, 11),
    _HpicfIpSlaRowStatus_Type()
)
hpicfIpSlaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaRowStatus.setStatus("current")
_HpicfIpSlaAttrTable_Object = MibTable
hpicfIpSlaAttrTable = _HpicfIpSlaAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfIpSlaAttrTable.setStatus("current")
_HpicfIpSlaAttrEntry_Object = MibTableRow
hpicfIpSlaAttrEntry = _HpicfIpSlaAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1)
)
hpicfIpSlaAttrEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaAttrEntry.setStatus("current")
_HpicfIpSlaSchedStartTime_Type = DateAndTime
_HpicfIpSlaSchedStartTime_Object = MibTableColumn
hpicfIpSlaSchedStartTime = _HpicfIpSlaSchedStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 1),
    _HpicfIpSlaSchedStartTime_Type()
)
hpicfIpSlaSchedStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSchedStartTime.setStatus("current")
_HpicfIpSlaSchedEndTime_Type = DateAndTime
_HpicfIpSlaSchedEndTime_Object = MibTableColumn
hpicfIpSlaSchedEndTime = _HpicfIpSlaSchedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 2),
    _HpicfIpSlaSchedEndTime_Type()
)
hpicfIpSlaSchedEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSchedEndTime.setStatus("current")


class _HpicfIpSlaSchedFreq_Type(Unsigned32):
    """Custom type hpicfIpSlaSchedFreq based on Unsigned32"""
    defaultValue = 60


_HpicfIpSlaSchedFreq_Object = MibTableColumn
hpicfIpSlaSchedFreq = _HpicfIpSlaSchedFreq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 3),
    _HpicfIpSlaSchedFreq_Type()
)
hpicfIpSlaSchedFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSchedFreq.setStatus("current")
_HpicfIpSlaSchedRepeat_Type = Unsigned32
_HpicfIpSlaSchedRepeat_Object = MibTableColumn
hpicfIpSlaSchedRepeat = _HpicfIpSlaSchedRepeat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 4),
    _HpicfIpSlaSchedRepeat_Type()
)
hpicfIpSlaSchedRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaSchedRepeat.setStatus("current")


class _HpicfIpSlaAttrTOS_Type(Unsigned32):
    """Custom type hpicfIpSlaAttrTOS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfIpSlaAttrTOS_Type.__name__ = "Unsigned32"
_HpicfIpSlaAttrTOS_Object = MibTableColumn
hpicfIpSlaAttrTOS = _HpicfIpSlaAttrTOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 5),
    _HpicfIpSlaAttrTOS_Type()
)
hpicfIpSlaAttrTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrTOS.setStatus("current")


class _HpicfIpSlaAttrHistorySize_Type(Unsigned32):
    """Custom type hpicfIpSlaAttrHistorySize based on Unsigned32"""
    defaultValue = 25


_HpicfIpSlaAttrHistorySize_Object = MibTableColumn
hpicfIpSlaAttrHistorySize = _HpicfIpSlaAttrHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 6),
    _HpicfIpSlaAttrHistorySize_Type()
)
hpicfIpSlaAttrHistorySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrHistorySize.setStatus("current")


class _HpicfIpSlaAttrPayloadSize_Type(Unsigned32):
    """Custom type hpicfIpSlaAttrPayloadSize based on Unsigned32"""
    defaultValue = 0


_HpicfIpSlaAttrPayloadSize_Object = MibTableColumn
hpicfIpSlaAttrPayloadSize = _HpicfIpSlaAttrPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 7),
    _HpicfIpSlaAttrPayloadSize_Type()
)
hpicfIpSlaAttrPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrPayloadSize.setStatus("current")


class _HpicfIpSlaAttrNumPkts_Type(Unsigned32):
    """Custom type hpicfIpSlaAttrNumPkts based on Unsigned32"""
    defaultValue = 10


_HpicfIpSlaAttrNumPkts_Object = MibTableColumn
hpicfIpSlaAttrNumPkts = _HpicfIpSlaAttrNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 8),
    _HpicfIpSlaAttrNumPkts_Type()
)
hpicfIpSlaAttrNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrNumPkts.setStatus("current")
_HpicfIpSlaAttrPktInterval_Type = Unsigned32
_HpicfIpSlaAttrPktInterval_Object = MibTableColumn
hpicfIpSlaAttrPktInterval = _HpicfIpSlaAttrPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 9),
    _HpicfIpSlaAttrPktInterval_Type()
)
hpicfIpSlaAttrPktInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrPktInterval.setStatus("current")
_HpicfIpSlaAttrRowStatus_Type = RowStatus
_HpicfIpSlaAttrRowStatus_Object = MibTableColumn
hpicfIpSlaAttrRowStatus = _HpicfIpSlaAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 10),
    _HpicfIpSlaAttrRowStatus_Type()
)
hpicfIpSlaAttrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrRowStatus.setStatus("current")


class _HpicfIpSlaAttrCodecType_Type(Integer32):
    """Custom type hpicfIpSlaAttrCodecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711u", 2),
          ("g729a", 3))
    )


_HpicfIpSlaAttrCodecType_Type.__name__ = "Integer32"
_HpicfIpSlaAttrCodecType_Object = MibTableColumn
hpicfIpSlaAttrCodecType = _HpicfIpSlaAttrCodecType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 11),
    _HpicfIpSlaAttrCodecType_Type()
)
hpicfIpSlaAttrCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrCodecType.setStatus("current")


class _HpicfIpSlaAttrAdvntgFactr_Type(Unsigned32):
    """Custom type hpicfIpSlaAttrAdvntgFactr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HpicfIpSlaAttrAdvntgFactr_Type.__name__ = "Unsigned32"
_HpicfIpSlaAttrAdvntgFactr_Object = MibTableColumn
hpicfIpSlaAttrAdvntgFactr = _HpicfIpSlaAttrAdvntgFactr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 2, 1, 12),
    _HpicfIpSlaAttrAdvntgFactr_Type()
)
hpicfIpSlaAttrAdvntgFactr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaAttrAdvntgFactr.setStatus("current")
_HpicfIpSlaThrTable_Object = MibTable
hpicfIpSlaThrTable = _HpicfIpSlaThrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfIpSlaThrTable.setStatus("current")
_HpicfIpSlaThrEntry_Object = MibTableRow
hpicfIpSlaThrEntry = _HpicfIpSlaThrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1)
)
hpicfIpSlaThrEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaThrMetricType"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaThrEntry.setStatus("current")


class _HpicfIpSlaThrMetricType_Type(Integer32):
    """Custom type hpicfIpSlaThrMetricType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsJitterPos", 10),
          ("dstTosrcTime", 4),
          ("icpif", 6),
          ("jitter", 2),
          ("mos", 5),
          ("packetLoss", 7),
          ("rtt", 1),
          ("sdJitterPos", 9),
          ("srcTodstTime", 3),
          ("testCompletion", 8))
    )


_HpicfIpSlaThrMetricType_Type.__name__ = "Integer32"
_HpicfIpSlaThrMetricType_Object = MibTableColumn
hpicfIpSlaThrMetricType = _HpicfIpSlaThrMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 1),
    _HpicfIpSlaThrMetricType_Type()
)
hpicfIpSlaThrMetricType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaThrMetricType.setStatus("current")
_HpicfIpSlaThrUpper_Type = Integer32
_HpicfIpSlaThrUpper_Object = MibTableColumn
hpicfIpSlaThrUpper = _HpicfIpSlaThrUpper_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 2),
    _HpicfIpSlaThrUpper_Type()
)
hpicfIpSlaThrUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrUpper.setStatus("current")
_HpicfIpSlaThrLower_Type = Integer32
_HpicfIpSlaThrLower_Object = MibTableColumn
hpicfIpSlaThrLower = _HpicfIpSlaThrLower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 3),
    _HpicfIpSlaThrLower_Type()
)
hpicfIpSlaThrLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrLower.setStatus("current")


class _HpicfIpSlaThrType_Type(Integer32):
    """Custom type hpicfIpSlaThrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregated", 3),
          ("consecutive", 2),
          ("immediate", 1))
    )


_HpicfIpSlaThrType_Type.__name__ = "Integer32"
_HpicfIpSlaThrType_Object = MibTableColumn
hpicfIpSlaThrType = _HpicfIpSlaThrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 4),
    _HpicfIpSlaThrType_Type()
)
hpicfIpSlaThrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrType.setStatus("current")
_HpicfIpSlaThrCount_Type = Unsigned32
_HpicfIpSlaThrCount_Object = MibTableColumn
hpicfIpSlaThrCount = _HpicfIpSlaThrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 5),
    _HpicfIpSlaThrCount_Type()
)
hpicfIpSlaThrCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrCount.setStatus("current")


class _HpicfIpSlaThrAction_Type(Integer32):
    """Custom type hpicfIpSlaThrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 2),
          ("none", 0),
          ("trap", 1),
          ("trapAndLog", 3))
    )


_HpicfIpSlaThrAction_Type.__name__ = "Integer32"
_HpicfIpSlaThrAction_Object = MibTableColumn
hpicfIpSlaThrAction = _HpicfIpSlaThrAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 6),
    _HpicfIpSlaThrAction_Type()
)
hpicfIpSlaThrAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrAction.setStatus("current")
_HpicfIpSlaThrRowStatus_Type = RowStatus
_HpicfIpSlaThrRowStatus_Object = MibTableColumn
hpicfIpSlaThrRowStatus = _HpicfIpSlaThrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 3, 1, 7),
    _HpicfIpSlaThrRowStatus_Type()
)
hpicfIpSlaThrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaThrRowStatus.setStatus("current")
_HpicfIpSlaRespTable_Object = MibTable
hpicfIpSlaRespTable = _HpicfIpSlaRespTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespTable.setStatus("current")
_HpicfIpSlaRespEntry_Object = MibTableRow
hpicfIpSlaRespEntry = _HpicfIpSlaRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1)
)
hpicfIpSlaRespEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaRespType"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaRespAddress"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaRespL4Port"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespEntry.setStatus("current")


class _HpicfIpSlaRespType_Type(Integer32):
    """Custom type hpicfIpSlaRespType based on Integer32"""
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
        *(("tcpConnect", 4),
          ("udpEcho", 1),
          ("udpJitter", 2),
          ("udpJitterVoIP", 3))
    )


_HpicfIpSlaRespType_Type.__name__ = "Integer32"
_HpicfIpSlaRespType_Object = MibTableColumn
hpicfIpSlaRespType = _HpicfIpSlaRespType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1, 1),
    _HpicfIpSlaRespType_Type()
)
hpicfIpSlaRespType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaRespType.setStatus("current")
_HpicfIpSlaRespAddressType_Type = InetAddressType
_HpicfIpSlaRespAddressType_Object = MibTableColumn
hpicfIpSlaRespAddressType = _HpicfIpSlaRespAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1, 2),
    _HpicfIpSlaRespAddressType_Type()
)
hpicfIpSlaRespAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaRespAddressType.setStatus("current")
_HpicfIpSlaRespAddress_Type = InetAddress
_HpicfIpSlaRespAddress_Object = MibTableColumn
hpicfIpSlaRespAddress = _HpicfIpSlaRespAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1, 3),
    _HpicfIpSlaRespAddress_Type()
)
hpicfIpSlaRespAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaRespAddress.setStatus("current")
_HpicfIpSlaRespL4Port_Type = InetPortNumber
_HpicfIpSlaRespL4Port_Object = MibTableColumn
hpicfIpSlaRespL4Port = _HpicfIpSlaRespL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1, 4),
    _HpicfIpSlaRespL4Port_Type()
)
hpicfIpSlaRespL4Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaRespL4Port.setStatus("current")
_HpicfIpSlaRespRowStatus_Type = RowStatus
_HpicfIpSlaRespRowStatus_Object = MibTableColumn
hpicfIpSlaRespRowStatus = _HpicfIpSlaRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 4, 1, 5),
    _HpicfIpSlaRespRowStatus_Type()
)
hpicfIpSlaRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaRespRowStatus.setStatus("current")
_HpicfIpSlaMsgTable_Object = MibTable
hpicfIpSlaMsgTable = _HpicfIpSlaMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfIpSlaMsgTable.setStatus("current")
_HpicfIpSlaMsgEntry_Object = MibTableRow
hpicfIpSlaMsgEntry = _HpicfIpSlaMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1)
)
hpicfIpSlaMsgEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaMsgEntry.setStatus("current")
_HpicfIpSlaMsgLastProbeRcvd_Type = Unsigned32
_HpicfIpSlaMsgLastProbeRcvd_Object = MibTableColumn
hpicfIpSlaMsgLastProbeRcvd = _HpicfIpSlaMsgLastProbeRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 1),
    _HpicfIpSlaMsgLastProbeRcvd_Type()
)
hpicfIpSlaMsgLastProbeRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgLastProbeRcvd.setStatus("current")
_HpicfIpSlaMsgLastClrRec_Type = Unsigned32
_HpicfIpSlaMsgLastClrRec_Object = MibTableColumn
hpicfIpSlaMsgLastClrRec = _HpicfIpSlaMsgLastClrRec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 2),
    _HpicfIpSlaMsgLastClrRec_Type()
)
hpicfIpSlaMsgLastClrRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgLastClrRec.setStatus("current")
_HpicfIpSlaMsgSuccProbe_Type = Unsigned32
_HpicfIpSlaMsgSuccProbe_Object = MibTableColumn
hpicfIpSlaMsgSuccProbe = _HpicfIpSlaMsgSuccProbe_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 3),
    _HpicfIpSlaMsgSuccProbe_Type()
)
hpicfIpSlaMsgSuccProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgSuccProbe.setStatus("current")
_HpicfIpSlaMsgIntErr_Type = Unsigned32
_HpicfIpSlaMsgIntErr_Object = MibTableColumn
hpicfIpSlaMsgIntErr = _HpicfIpSlaMsgIntErr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 4),
    _HpicfIpSlaMsgIntErr_Type()
)
hpicfIpSlaMsgIntErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgIntErr.setStatus("current")
_HpicfIpSlaMsgLocIntfDown_Type = Unsigned32
_HpicfIpSlaMsgLocIntfDown_Object = MibTableColumn
hpicfIpSlaMsgLocIntfDown = _HpicfIpSlaMsgLocIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 5),
    _HpicfIpSlaMsgLocIntfDown_Type()
)
hpicfIpSlaMsgLocIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgLocIntfDown.setStatus("current")
_HpicfIpSlaMsgResTimeout_Type = Unsigned32
_HpicfIpSlaMsgResTimeout_Object = MibTableColumn
hpicfIpSlaMsgResTimeout = _HpicfIpSlaMsgResTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 6),
    _HpicfIpSlaMsgResTimeout_Type()
)
hpicfIpSlaMsgResTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgResTimeout.setStatus("current")
_HpicfIpSlaMsgDNSFormatErr_Type = Unsigned32
_HpicfIpSlaMsgDNSFormatErr_Object = MibTableColumn
hpicfIpSlaMsgDNSFormatErr = _HpicfIpSlaMsgDNSFormatErr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 7),
    _HpicfIpSlaMsgDNSFormatErr_Type()
)
hpicfIpSlaMsgDNSFormatErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDNSFormatErr.setStatus("current")
_HpicfIpSlaMsgServerFaild_Type = Unsigned32
_HpicfIpSlaMsgServerFaild_Object = MibTableColumn
hpicfIpSlaMsgServerFaild = _HpicfIpSlaMsgServerFaild_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 8),
    _HpicfIpSlaMsgServerFaild_Type()
)
hpicfIpSlaMsgServerFaild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgServerFaild.setStatus("current")
_HpicfIpSlaMsgDomainNotExist_Type = Unsigned32
_HpicfIpSlaMsgDomainNotExist_Object = MibTableColumn
hpicfIpSlaMsgDomainNotExist = _HpicfIpSlaMsgDomainNotExist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 9),
    _HpicfIpSlaMsgDomainNotExist_Type()
)
hpicfIpSlaMsgDomainNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDomainNotExist.setStatus("current")
_HpicfIpSlaMsgFunctnNotImpl_Type = Unsigned32
_HpicfIpSlaMsgFunctnNotImpl_Object = MibTableColumn
hpicfIpSlaMsgFunctnNotImpl = _HpicfIpSlaMsgFunctnNotImpl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 10),
    _HpicfIpSlaMsgFunctnNotImpl_Type()
)
hpicfIpSlaMsgFunctnNotImpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgFunctnNotImpl.setStatus("current")
_HpicfIpSlaMsgServerRefusd_Type = Unsigned32
_HpicfIpSlaMsgServerRefusd_Object = MibTableColumn
hpicfIpSlaMsgServerRefusd = _HpicfIpSlaMsgServerRefusd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 11),
    _HpicfIpSlaMsgServerRefusd_Type()
)
hpicfIpSlaMsgServerRefusd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgServerRefusd.setStatus("current")
_HpicfIpSlaMsgNameNotExist_Type = Unsigned32
_HpicfIpSlaMsgNameNotExist_Object = MibTableColumn
hpicfIpSlaMsgNameNotExist = _HpicfIpSlaMsgNameNotExist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 12),
    _HpicfIpSlaMsgNameNotExist_Type()
)
hpicfIpSlaMsgNameNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNameNotExist.setStatus("current")
_HpicfIpSlaMsgRRsetNotExist_Type = Unsigned32
_HpicfIpSlaMsgRRsetNotExist_Object = MibTableColumn
hpicfIpSlaMsgRRsetNotExist = _HpicfIpSlaMsgRRsetNotExist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 13),
    _HpicfIpSlaMsgRRsetNotExist_Type()
)
hpicfIpSlaMsgRRsetNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgRRsetNotExist.setStatus("current")
_HpicfIpSlaMsgServerNotInZone_Type = Unsigned32
_HpicfIpSlaMsgServerNotInZone_Object = MibTableColumn
hpicfIpSlaMsgServerNotInZone = _HpicfIpSlaMsgServerNotInZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 14),
    _HpicfIpSlaMsgServerNotInZone_Type()
)
hpicfIpSlaMsgServerNotInZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgServerNotInZone.setStatus("current")
_HpicfIpSlaMsgNameNotInZone_Type = Unsigned32
_HpicfIpSlaMsgNameNotInZone_Object = MibTableColumn
hpicfIpSlaMsgNameNotInZone = _HpicfIpSlaMsgNameNotInZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 15),
    _HpicfIpSlaMsgNameNotInZone_Type()
)
hpicfIpSlaMsgNameNotInZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNameNotInZone.setStatus("current")
_HpicfIpSlaMsgDHCPFaildResln_Type = Unsigned32
_HpicfIpSlaMsgDHCPFaildResln_Object = MibTableColumn
hpicfIpSlaMsgDHCPFaildResln = _HpicfIpSlaMsgDHCPFaildResln_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 16),
    _HpicfIpSlaMsgDHCPFaildResln_Type()
)
hpicfIpSlaMsgDHCPFaildResln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDHCPFaildResln.setStatus("current")
_HpicfIpSlaMsgOffrNotRecvd_Type = Unsigned32
_HpicfIpSlaMsgOffrNotRecvd_Object = MibTableColumn
hpicfIpSlaMsgOffrNotRecvd = _HpicfIpSlaMsgOffrNotRecvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 17),
    _HpicfIpSlaMsgOffrNotRecvd_Type()
)
hpicfIpSlaMsgOffrNotRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgOffrNotRecvd.setStatus("current")
_HpicfIpSlaMsgNACKRecvd_Type = Unsigned32
_HpicfIpSlaMsgNACKRecvd_Object = MibTableColumn
hpicfIpSlaMsgNACKRecvd = _HpicfIpSlaMsgNACKRecvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 18),
    _HpicfIpSlaMsgNACKRecvd_Type()
)
hpicfIpSlaMsgNACKRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNACKRecvd.setStatus("current")
_HpicfIpSlaMsgThrHitRTT_Type = Unsigned32
_HpicfIpSlaMsgThrHitRTT_Object = MibTableColumn
hpicfIpSlaMsgThrHitRTT = _HpicfIpSlaMsgThrHitRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 19),
    _HpicfIpSlaMsgThrHitRTT_Type()
)
hpicfIpSlaMsgThrHitRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitRTT.setStatus("current")
_HpicfIpSlaMsgStatus_Type = Unsigned32
_HpicfIpSlaMsgStatus_Object = MibTableColumn
hpicfIpSlaMsgStatus = _HpicfIpSlaMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 20),
    _HpicfIpSlaMsgStatus_Type()
)
hpicfIpSlaMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgStatus.setStatus("current")
_HpicfIpSlaMsgNxtSched_Type = Unsigned32
_HpicfIpSlaMsgNxtSched_Object = MibTableColumn
hpicfIpSlaMsgNxtSched = _HpicfIpSlaMsgNxtSched_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 21),
    _HpicfIpSlaMsgNxtSched_Type()
)
hpicfIpSlaMsgNxtSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNxtSched.setStatus("current")
_HpicfIpSlaMsgThrHitPostvSDAvg_Type = Unsigned32
_HpicfIpSlaMsgThrHitPostvSDAvg_Object = MibTableColumn
hpicfIpSlaMsgThrHitPostvSDAvg = _HpicfIpSlaMsgThrHitPostvSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 22),
    _HpicfIpSlaMsgThrHitPostvSDAvg_Type()
)
hpicfIpSlaMsgThrHitPostvSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitPostvSDAvg.setStatus("current")
_HpicfIpSlaMsgThrHitPostvDSAvg_Type = Unsigned32
_HpicfIpSlaMsgThrHitPostvDSAvg_Object = MibTableColumn
hpicfIpSlaMsgThrHitPostvDSAvg = _HpicfIpSlaMsgThrHitPostvDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 23),
    _HpicfIpSlaMsgThrHitPostvDSAvg_Type()
)
hpicfIpSlaMsgThrHitPostvDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitPostvDSAvg.setStatus("current")
_HpicfIpSlaMsgThrHitOneWayDSAvg_Type = Unsigned32
_HpicfIpSlaMsgThrHitOneWayDSAvg_Object = MibTableColumn
hpicfIpSlaMsgThrHitOneWayDSAvg = _HpicfIpSlaMsgThrHitOneWayDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 24),
    _HpicfIpSlaMsgThrHitOneWayDSAvg_Type()
)
hpicfIpSlaMsgThrHitOneWayDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitOneWayDSAvg.setStatus("current")
_HpicfIpSlaMsgThrHitOneWaySDAvg_Type = Unsigned32
_HpicfIpSlaMsgThrHitOneWaySDAvg_Object = MibTableColumn
hpicfIpSlaMsgThrHitOneWaySDAvg = _HpicfIpSlaMsgThrHitOneWaySDAvg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 25),
    _HpicfIpSlaMsgThrHitOneWaySDAvg_Type()
)
hpicfIpSlaMsgThrHitOneWaySDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitOneWaySDAvg.setStatus("current")
_HpicfIpSlaMsgThrHitAvgICPIF_Type = Unsigned32
_HpicfIpSlaMsgThrHitAvgICPIF_Object = MibTableColumn
hpicfIpSlaMsgThrHitAvgICPIF = _HpicfIpSlaMsgThrHitAvgICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 26),
    _HpicfIpSlaMsgThrHitAvgICPIF_Type()
)
hpicfIpSlaMsgThrHitAvgICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitAvgICPIF.setStatus("current")
_HpicfIpSlaMsgThrHitAvgMOS_Type = Unsigned32
_HpicfIpSlaMsgThrHitAvgMOS_Object = MibTableColumn
hpicfIpSlaMsgThrHitAvgMOS = _HpicfIpSlaMsgThrHitAvgMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 27),
    _HpicfIpSlaMsgThrHitAvgMOS_Type()
)
hpicfIpSlaMsgThrHitAvgMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitAvgMOS.setStatus("current")
_HpicfIpSlaMsgNameServUnreach_Type = Unsigned32
_HpicfIpSlaMsgNameServUnreach_Object = MibTableColumn
hpicfIpSlaMsgNameServUnreach = _HpicfIpSlaMsgNameServUnreach_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 28),
    _HpicfIpSlaMsgNameServUnreach_Type()
)
hpicfIpSlaMsgNameServUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNameServUnreach.setStatus("current")
_HpicfIpSlaMsgDHCPReleaseErr_Type = Unsigned32
_HpicfIpSlaMsgDHCPReleaseErr_Object = MibTableColumn
hpicfIpSlaMsgDHCPReleaseErr = _HpicfIpSlaMsgDHCPReleaseErr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 29),
    _HpicfIpSlaMsgDHCPReleaseErr_Type()
)
hpicfIpSlaMsgDHCPReleaseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDHCPReleaseErr.setStatus("current")
_HpicfIpSlaMsgThrHitPktLoss_Type = Unsigned32
_HpicfIpSlaMsgThrHitPktLoss_Object = MibTableColumn
hpicfIpSlaMsgThrHitPktLoss = _HpicfIpSlaMsgThrHitPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 30),
    _HpicfIpSlaMsgThrHitPktLoss_Type()
)
hpicfIpSlaMsgThrHitPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgThrHitPktLoss.setStatus("current")
_HpicfIpSlaMsgDstUnreach_Type = Unsigned32
_HpicfIpSlaMsgDstUnreach_Object = MibTableColumn
hpicfIpSlaMsgDstUnreach = _HpicfIpSlaMsgDstUnreach_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 31),
    _HpicfIpSlaMsgDstUnreach_Type()
)
hpicfIpSlaMsgDstUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDstUnreach.setStatus("current")
_HpicfIpSlaMsgProbeSkpd_Type = Unsigned32
_HpicfIpSlaMsgProbeSkpd_Object = MibTableColumn
hpicfIpSlaMsgProbeSkpd = _HpicfIpSlaMsgProbeSkpd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 32),
    _HpicfIpSlaMsgProbeSkpd_Type()
)
hpicfIpSlaMsgProbeSkpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgProbeSkpd.setStatus("current")
_HpicfIpSlaMsgDNSResolnFailed_Type = Unsigned32
_HpicfIpSlaMsgDNSResolnFailed_Object = MibTableColumn
hpicfIpSlaMsgDNSResolnFailed = _HpicfIpSlaMsgDNSResolnFailed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 33),
    _HpicfIpSlaMsgDNSResolnFailed_Type()
)
hpicfIpSlaMsgDNSResolnFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgDNSResolnFailed.setStatus("current")
_HpicfIpSlaMsgNoRoutetoTgt_Type = Unsigned32
_HpicfIpSlaMsgNoRoutetoTgt_Object = MibTableColumn
hpicfIpSlaMsgNoRoutetoTgt = _HpicfIpSlaMsgNoRoutetoTgt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 34),
    _HpicfIpSlaMsgNoRoutetoTgt_Type()
)
hpicfIpSlaMsgNoRoutetoTgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNoRoutetoTgt.setStatus("current")
_HpicfIpSlaMsgUnbleToConctHost_Type = Unsigned32
_HpicfIpSlaMsgUnbleToConctHost_Object = MibTableColumn
hpicfIpSlaMsgUnbleToConctHost = _HpicfIpSlaMsgUnbleToConctHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 35),
    _HpicfIpSlaMsgUnbleToConctHost_Type()
)
hpicfIpSlaMsgUnbleToConctHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgUnbleToConctHost.setStatus("current")
_HpicfIpSlaMsgSuccConnection_Type = Unsigned32
_HpicfIpSlaMsgSuccConnection_Object = MibTableColumn
hpicfIpSlaMsgSuccConnection = _HpicfIpSlaMsgSuccConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 36),
    _HpicfIpSlaMsgSuccConnection_Type()
)
hpicfIpSlaMsgSuccConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgSuccConnection.setStatus("current")
_HpicfIpSlaMsgPossTrailDropped_Type = Unsigned32
_HpicfIpSlaMsgPossTrailDropped_Object = MibTableColumn
hpicfIpSlaMsgPossTrailDropped = _HpicfIpSlaMsgPossTrailDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 37),
    _HpicfIpSlaMsgPossTrailDropped_Type()
)
hpicfIpSlaMsgPossTrailDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgPossTrailDropped.setStatus("current")
_HpicfIpSlaMsgNoRespFrmTgt_Type = Unsigned32
_HpicfIpSlaMsgNoRespFrmTgt_Object = MibTableColumn
hpicfIpSlaMsgNoRespFrmTgt = _HpicfIpSlaMsgNoRespFrmTgt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 38),
    _HpicfIpSlaMsgNoRespFrmTgt_Type()
)
hpicfIpSlaMsgNoRespFrmTgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgNoRespFrmTgt.setStatus("current")
_HpicfIpSlaMsgProbeRespRecvd_Type = Unsigned32
_HpicfIpSlaMsgProbeRespRecvd_Object = MibTableColumn
hpicfIpSlaMsgProbeRespRecvd = _HpicfIpSlaMsgProbeRespRecvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 5, 1, 39),
    _HpicfIpSlaMsgProbeRespRecvd_Type()
)
hpicfIpSlaMsgProbeRespRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaMsgProbeRespRecvd.setStatus("current")
_HpicfIpSlaHistTable_Object = MibTable
hpicfIpSlaHistTable = _HpicfIpSlaHistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistTable.setStatus("current")
_HpicfIpSlaHistEntry_Object = MibTableRow
hpicfIpSlaHistEntry = _HpicfIpSlaHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1)
)
hpicfIpSlaHistEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistEntry.setStatus("current")
_HpicfIpSlaHistMinRTT_Type = Unsigned32
_HpicfIpSlaHistMinRTT_Object = MibTableColumn
hpicfIpSlaHistMinRTT = _HpicfIpSlaHistMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 1),
    _HpicfIpSlaHistMinRTT_Type()
)
hpicfIpSlaHistMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinRTT.setStatus("current")
_HpicfIpSlaHistMaxRTT_Type = Unsigned32
_HpicfIpSlaHistMaxRTT_Object = MibTableColumn
hpicfIpSlaHistMaxRTT = _HpicfIpSlaHistMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 2),
    _HpicfIpSlaHistMaxRTT_Type()
)
hpicfIpSlaHistMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxRTT.setStatus("current")
_HpicfIpSlaHistAvgRTT_Type = Unsigned32
_HpicfIpSlaHistAvgRTT_Object = MibTableColumn
hpicfIpSlaHistAvgRTT = _HpicfIpSlaHistAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 3),
    _HpicfIpSlaHistAvgRTT_Type()
)
hpicfIpSlaHistAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgRTT.setStatus("current")
_HpicfIpSlaHistTotalRTT_Type = Unsigned32
_HpicfIpSlaHistTotalRTT_Object = MibTableColumn
hpicfIpSlaHistTotalRTT = _HpicfIpSlaHistTotalRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 4),
    _HpicfIpSlaHistTotalRTT_Type()
)
hpicfIpSlaHistTotalRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistTotalRTT.setStatus("current")
_HpicfIpSlaHistRTT2_Type = Unsigned32
_HpicfIpSlaHistRTT2_Object = MibTableColumn
hpicfIpSlaHistRTT2 = _HpicfIpSlaHistRTT2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 5),
    _HpicfIpSlaHistRTT2_Type()
)
hpicfIpSlaHistRTT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistRTT2.setStatus("current")
_HpicfIpSlaHistNumOfRTT_Type = Unsigned32
_HpicfIpSlaHistNumOfRTT_Object = MibTableColumn
hpicfIpSlaHistNumOfRTT = _HpicfIpSlaHistNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 6),
    _HpicfIpSlaHistNumOfRTT_Type()
)
hpicfIpSlaHistNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfRTT.setStatus("current")
_HpicfIpSlaHistProbID_Type = Unsigned32
_HpicfIpSlaHistProbID_Object = MibTableColumn
hpicfIpSlaHistProbID = _HpicfIpSlaHistProbID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 7),
    _HpicfIpSlaHistProbID_Type()
)
hpicfIpSlaHistProbID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistProbID.setStatus("current")
_HpicfIpSlaHistLastSuccProbTime_Type = Unsigned32
_HpicfIpSlaHistLastSuccProbTime_Object = MibTableColumn
hpicfIpSlaHistLastSuccProbTime = _HpicfIpSlaHistLastSuccProbTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 8),
    _HpicfIpSlaHistLastSuccProbTime_Type()
)
hpicfIpSlaHistLastSuccProbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistLastSuccProbTime.setStatus("current")
_HpicfIpSlaHistPacketLoss_Type = Unsigned32
_HpicfIpSlaHistPacketLoss_Object = MibTableColumn
hpicfIpSlaHistPacketLoss = _HpicfIpSlaHistPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 9),
    _HpicfIpSlaHistPacketLoss_Type()
)
hpicfIpSlaHistPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistPacketLoss.setStatus("current")
_HpicfIpSlaHistSentPktNum_Type = Unsigned32
_HpicfIpSlaHistSentPktNum_Object = MibTableColumn
hpicfIpSlaHistSentPktNum = _HpicfIpSlaHistSentPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 10),
    _HpicfIpSlaHistSentPktNum_Type()
)
hpicfIpSlaHistSentPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSentPktNum.setStatus("current")
_HpicfIpSlaHistRecvdPktNum_Type = Unsigned32
_HpicfIpSlaHistRecvdPktNum_Object = MibTableColumn
hpicfIpSlaHistRecvdPktNum = _HpicfIpSlaHistRecvdPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 11),
    _HpicfIpSlaHistRecvdPktNum_Type()
)
hpicfIpSlaHistRecvdPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistRecvdPktNum.setStatus("current")
_HpicfIpSlaHistMinStoDPostv_Type = Unsigned32
_HpicfIpSlaHistMinStoDPostv_Object = MibTableColumn
hpicfIpSlaHistMinStoDPostv = _HpicfIpSlaHistMinStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 12),
    _HpicfIpSlaHistMinStoDPostv_Type()
)
hpicfIpSlaHistMinStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinStoDPostv.setStatus("current")
_HpicfIpSlaHistMaxStoDPostv_Type = Unsigned32
_HpicfIpSlaHistMaxStoDPostv_Object = MibTableColumn
hpicfIpSlaHistMaxStoDPostv = _HpicfIpSlaHistMaxStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 13),
    _HpicfIpSlaHistMaxStoDPostv_Type()
)
hpicfIpSlaHistMaxStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxStoDPostv.setStatus("current")
_HpicfIpSlaHistNumOfPosSD_Type = Unsigned32
_HpicfIpSlaHistNumOfPosSD_Object = MibTableColumn
hpicfIpSlaHistNumOfPosSD = _HpicfIpSlaHistNumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 14),
    _HpicfIpSlaHistNumOfPosSD_Type()
)
hpicfIpSlaHistNumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfPosSD.setStatus("current")
_HpicfIpSlaHistSumOfPosSD_Type = Unsigned32
_HpicfIpSlaHistSumOfPosSD_Object = MibTableColumn
hpicfIpSlaHistSumOfPosSD = _HpicfIpSlaHistSumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 15),
    _HpicfIpSlaHistSumOfPosSD_Type()
)
hpicfIpSlaHistSumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumOfPosSD.setStatus("current")
_HpicfIpSlaHistAvgStoDPostv_Type = Unsigned32
_HpicfIpSlaHistAvgStoDPostv_Object = MibTableColumn
hpicfIpSlaHistAvgStoDPostv = _HpicfIpSlaHistAvgStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 16),
    _HpicfIpSlaHistAvgStoDPostv_Type()
)
hpicfIpSlaHistAvgStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgStoDPostv.setStatus("current")
_HpicfIpSlaHistSum2PositivesSD_Type = Unsigned32
_HpicfIpSlaHistSum2PositivesSD_Object = MibTableColumn
hpicfIpSlaHistSum2PositivesSD = _HpicfIpSlaHistSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 17),
    _HpicfIpSlaHistSum2PositivesSD_Type()
)
hpicfIpSlaHistSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2PositivesSD.setStatus("current")
_HpicfIpSlaHistMinDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistMinDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistMinDtoSPostv = _HpicfIpSlaHistMinDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 18),
    _HpicfIpSlaHistMinDtoSPostv_Type()
)
hpicfIpSlaHistMinDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinDtoSPostv.setStatus("current")
_HpicfIpSlaHistMaxDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistMaxDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistMaxDtoSPostv = _HpicfIpSlaHistMaxDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 19),
    _HpicfIpSlaHistMaxDtoSPostv_Type()
)
hpicfIpSlaHistMaxDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxDtoSPostv.setStatus("current")
_HpicfIpSlaHistNumOfPosDS_Type = Unsigned32
_HpicfIpSlaHistNumOfPosDS_Object = MibTableColumn
hpicfIpSlaHistNumOfPosDS = _HpicfIpSlaHistNumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 20),
    _HpicfIpSlaHistNumOfPosDS_Type()
)
hpicfIpSlaHistNumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfPosDS.setStatus("current")
_HpicfIpSlaHistSumOfPosDS_Type = Unsigned32
_HpicfIpSlaHistSumOfPosDS_Object = MibTableColumn
hpicfIpSlaHistSumOfPosDS = _HpicfIpSlaHistSumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 21),
    _HpicfIpSlaHistSumOfPosDS_Type()
)
hpicfIpSlaHistSumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumOfPosDS.setStatus("current")
_HpicfIpSlaHistAvgDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistAvgDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistAvgDtoSPostv = _HpicfIpSlaHistAvgDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 22),
    _HpicfIpSlaHistAvgDtoSPostv_Type()
)
hpicfIpSlaHistAvgDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgDtoSPostv.setStatus("current")
_HpicfIpSlaHistSum2PositivesDS_Type = Unsigned32
_HpicfIpSlaHistSum2PositivesDS_Object = MibTableColumn
hpicfIpSlaHistSum2PositivesDS = _HpicfIpSlaHistSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 23),
    _HpicfIpSlaHistSum2PositivesDS_Type()
)
hpicfIpSlaHistSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2PositivesDS.setStatus("current")
_HpicfIpSlaHistMinStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistMinStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistMinStoDNegtv = _HpicfIpSlaHistMinStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 24),
    _HpicfIpSlaHistMinStoDNegtv_Type()
)
hpicfIpSlaHistMinStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinStoDNegtv.setStatus("current")
_HpicfIpSlaHistMaxStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistMaxStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistMaxStoDNegtv = _HpicfIpSlaHistMaxStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 25),
    _HpicfIpSlaHistMaxStoDNegtv_Type()
)
hpicfIpSlaHistMaxStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxStoDNegtv.setStatus("current")
_HpicfIpSlaHistNumOfNegSD_Type = Unsigned32
_HpicfIpSlaHistNumOfNegSD_Object = MibTableColumn
hpicfIpSlaHistNumOfNegSD = _HpicfIpSlaHistNumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 26),
    _HpicfIpSlaHistNumOfNegSD_Type()
)
hpicfIpSlaHistNumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfNegSD.setStatus("current")
_HpicfIpSlaHistSumOfNegSD_Type = Unsigned32
_HpicfIpSlaHistSumOfNegSD_Object = MibTableColumn
hpicfIpSlaHistSumOfNegSD = _HpicfIpSlaHistSumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 27),
    _HpicfIpSlaHistSumOfNegSD_Type()
)
hpicfIpSlaHistSumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumOfNegSD.setStatus("current")
_HpicfIpSlaHistAvgStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistAvgStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistAvgStoDNegtv = _HpicfIpSlaHistAvgStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 28),
    _HpicfIpSlaHistAvgStoDNegtv_Type()
)
hpicfIpSlaHistAvgStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgStoDNegtv.setStatus("current")
_HpicfIpSlaHistSum2NegativesSD_Type = Unsigned32
_HpicfIpSlaHistSum2NegativesSD_Object = MibTableColumn
hpicfIpSlaHistSum2NegativesSD = _HpicfIpSlaHistSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 29),
    _HpicfIpSlaHistSum2NegativesSD_Type()
)
hpicfIpSlaHistSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2NegativesSD.setStatus("current")
_HpicfIpSlaHistMinDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistMinDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistMinDtoSNegtv = _HpicfIpSlaHistMinDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 30),
    _HpicfIpSlaHistMinDtoSNegtv_Type()
)
hpicfIpSlaHistMinDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinDtoSNegtv.setStatus("current")
_HpicfIpSlaHistMaxDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistMaxDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistMaxDtoSNegtv = _HpicfIpSlaHistMaxDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 31),
    _HpicfIpSlaHistMaxDtoSNegtv_Type()
)
hpicfIpSlaHistMaxDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxDtoSNegtv.setStatus("current")
_HpicfIpSlaHistNumOfNegDS_Type = Unsigned32
_HpicfIpSlaHistNumOfNegDS_Object = MibTableColumn
hpicfIpSlaHistNumOfNegDS = _HpicfIpSlaHistNumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 32),
    _HpicfIpSlaHistNumOfNegDS_Type()
)
hpicfIpSlaHistNumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfNegDS.setStatus("current")
_HpicfIpSlaHistSumOfNegDS_Type = Unsigned32
_HpicfIpSlaHistSumOfNegDS_Object = MibTableColumn
hpicfIpSlaHistSumOfNegDS = _HpicfIpSlaHistSumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 33),
    _HpicfIpSlaHistSumOfNegDS_Type()
)
hpicfIpSlaHistSumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumOfNegDS.setStatus("current")
_HpicfIpSlaHistAvgDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistAvgDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistAvgDtoSNegtv = _HpicfIpSlaHistAvgDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 34),
    _HpicfIpSlaHistAvgDtoSNegtv_Type()
)
hpicfIpSlaHistAvgDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgDtoSNegtv.setStatus("current")
_HpicfIpSlaHistSum2NegativesDS_Type = Unsigned32
_HpicfIpSlaHistSum2NegativesDS_Object = MibTableColumn
hpicfIpSlaHistSum2NegativesDS = _HpicfIpSlaHistSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 35),
    _HpicfIpSlaHistSum2NegativesDS_Type()
)
hpicfIpSlaHistSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2NegativesDS.setStatus("current")
_HpicfIpSlaHistMinStoDDelay_Type = Unsigned32
_HpicfIpSlaHistMinStoDDelay_Object = MibTableColumn
hpicfIpSlaHistMinStoDDelay = _HpicfIpSlaHistMinStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 36),
    _HpicfIpSlaHistMinStoDDelay_Type()
)
hpicfIpSlaHistMinStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinStoDDelay.setStatus("current")
_HpicfIpSlaHistMaxStoDDelay_Type = Unsigned32
_HpicfIpSlaHistMaxStoDDelay_Object = MibTableColumn
hpicfIpSlaHistMaxStoDDelay = _HpicfIpSlaHistMaxStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 37),
    _HpicfIpSlaHistMaxStoDDelay_Type()
)
hpicfIpSlaHistMaxStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxStoDDelay.setStatus("current")
_HpicfIpSlaHistSumStoDDelay_Type = Unsigned32
_HpicfIpSlaHistSumStoDDelay_Object = MibTableColumn
hpicfIpSlaHistSumStoDDelay = _HpicfIpSlaHistSumStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 38),
    _HpicfIpSlaHistSumStoDDelay_Type()
)
hpicfIpSlaHistSumStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumStoDDelay.setStatus("current")
_HpicfIpSlaHistNumOfDelaySD_Type = Unsigned32
_HpicfIpSlaHistNumOfDelaySD_Object = MibTableColumn
hpicfIpSlaHistNumOfDelaySD = _HpicfIpSlaHistNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 39),
    _HpicfIpSlaHistNumOfDelaySD_Type()
)
hpicfIpSlaHistNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfDelaySD.setStatus("current")
_HpicfIpSlaHistSum2DelaySD_Type = Unsigned32
_HpicfIpSlaHistSum2DelaySD_Object = MibTableColumn
hpicfIpSlaHistSum2DelaySD = _HpicfIpSlaHistSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 40),
    _HpicfIpSlaHistSum2DelaySD_Type()
)
hpicfIpSlaHistSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2DelaySD.setStatus("current")
_HpicfIpSlaHistMinDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistMinDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistMinDtoSDelay = _HpicfIpSlaHistMinDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 41),
    _HpicfIpSlaHistMinDtoSDelay_Type()
)
hpicfIpSlaHistMinDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMinDtoSDelay.setStatus("current")
_HpicfIpSlaHistMaxDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistMaxDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistMaxDtoSDelay = _HpicfIpSlaHistMaxDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 42),
    _HpicfIpSlaHistMaxDtoSDelay_Type()
)
hpicfIpSlaHistMaxDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMaxDtoSDelay.setStatus("current")
_HpicfIpSlaHistNumOfDelayDS_Type = Unsigned32
_HpicfIpSlaHistNumOfDelayDS_Object = MibTableColumn
hpicfIpSlaHistNumOfDelayDS = _HpicfIpSlaHistNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 43),
    _HpicfIpSlaHistNumOfDelayDS_Type()
)
hpicfIpSlaHistNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistNumOfDelayDS.setStatus("current")
_HpicfIpSlaHistSumDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistSumDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistSumDtoSDelay = _HpicfIpSlaHistSumDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 44),
    _HpicfIpSlaHistSumDtoSDelay_Type()
)
hpicfIpSlaHistSumDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSumDtoSDelay.setStatus("current")
_HpicfIpSlaHistSum2DelayDS_Type = Unsigned32
_HpicfIpSlaHistSum2DelayDS_Object = MibTableColumn
hpicfIpSlaHistSum2DelayDS = _HpicfIpSlaHistSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 45),
    _HpicfIpSlaHistSum2DelayDS_Type()
)
hpicfIpSlaHistSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSum2DelayDS.setStatus("current")
_HpicfIpSlaHistICPIF_Type = Unsigned32
_HpicfIpSlaHistICPIF_Object = MibTableColumn
hpicfIpSlaHistICPIF = _HpicfIpSlaHistICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 46),
    _HpicfIpSlaHistICPIF_Type()
)
hpicfIpSlaHistICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistICPIF.setStatus("current")
_HpicfIpSlaHistMOS_Type = Unsigned32
_HpicfIpSlaHistMOS_Object = MibTableColumn
hpicfIpSlaHistMOS = _HpicfIpSlaHistMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 47),
    _HpicfIpSlaHistMOS_Type()
)
hpicfIpSlaHistMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistMOS.setStatus("current")
_HpicfIpSlaHistAvgStoDDelay_Type = Unsigned32
_HpicfIpSlaHistAvgStoDDelay_Object = MibTableColumn
hpicfIpSlaHistAvgStoDDelay = _HpicfIpSlaHistAvgStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 48),
    _HpicfIpSlaHistAvgStoDDelay_Type()
)
hpicfIpSlaHistAvgStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgStoDDelay.setStatus("current")
_HpicfIpSlaHistAvgDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistAvgDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistAvgDtoSDelay = _HpicfIpSlaHistAvgDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 6, 1, 49),
    _HpicfIpSlaHistAvgDtoSDelay_Type()
)
hpicfIpSlaHistAvgDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAvgDtoSDelay.setStatus("current")
_HpicfIpSlaHistSummTable_Object = MibTable
hpicfIpSlaHistSummTable = _HpicfIpSlaHistSummTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummTable.setStatus("current")
_HpicfIpSlaHistSummEntry_Object = MibTableRow
hpicfIpSlaHistSummEntry = _HpicfIpSlaHistSummEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1)
)
hpicfIpSlaHistSummEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaHistSummIndx"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummEntry.setStatus("current")


class _HpicfIpSlaHistSummIndx_Type(Integer32):
    """Custom type hpicfIpSlaHistSummIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HpicfIpSlaHistSummIndx_Type.__name__ = "Integer32"
_HpicfIpSlaHistSummIndx_Object = MibTableColumn
hpicfIpSlaHistSummIndx = _HpicfIpSlaHistSummIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 1),
    _HpicfIpSlaHistSummIndx_Type()
)
hpicfIpSlaHistSummIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummIndx.setStatus("current")
_HpicfIpSlaHistSummStartTime_Type = Unsigned32
_HpicfIpSlaHistSummStartTime_Object = MibTableColumn
hpicfIpSlaHistSummStartTime = _HpicfIpSlaHistSummStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 2),
    _HpicfIpSlaHistSummStartTime_Type()
)
hpicfIpSlaHistSummStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummStartTime.setStatus("current")
_HpicfIpSlaHistSummStatus_Type = Unsigned32
_HpicfIpSlaHistSummStatus_Object = MibTableColumn
hpicfIpSlaHistSummStatus = _HpicfIpSlaHistSummStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 3),
    _HpicfIpSlaHistSummStatus_Type()
)
hpicfIpSlaHistSummStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummStatus.setStatus("current")
_HpicfIpSlaHistSummRTT_Type = Unsigned32
_HpicfIpSlaHistSummRTT_Object = MibTableColumn
hpicfIpSlaHistSummRTT = _HpicfIpSlaHistSummRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 4),
    _HpicfIpSlaHistSummRTT_Type()
)
hpicfIpSlaHistSummRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummRTT.setStatus("current")
_HpicfIpSlaHistSummResolvdIP_Type = Unsigned32
_HpicfIpSlaHistSummResolvdIP_Object = MibTableColumn
hpicfIpSlaHistSummResolvdIP = _HpicfIpSlaHistSummResolvdIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 5),
    _HpicfIpSlaHistSummResolvdIP_Type()
)
hpicfIpSlaHistSummResolvdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummResolvdIP.setStatus("current")
_HpicfIpSlaHistSummDescription_Type = Unsigned32
_HpicfIpSlaHistSummDescription_Object = MibTableColumn
hpicfIpSlaHistSummDescription = _HpicfIpSlaHistSummDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 6),
    _HpicfIpSlaHistSummDescription_Type()
)
hpicfIpSlaHistSummDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummDescription.setStatus("current")
_HpicfIpSlaHistSummStoDDelay_Type = Unsigned32
_HpicfIpSlaHistSummStoDDelay_Object = MibTableColumn
hpicfIpSlaHistSummStoDDelay = _HpicfIpSlaHistSummStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 7),
    _HpicfIpSlaHistSummStoDDelay_Type()
)
hpicfIpSlaHistSummStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummStoDDelay.setStatus("current")
_HpicfIpSlaHistSummDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistSummDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistSummDtoSDelay = _HpicfIpSlaHistSummDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 7, 1, 8),
    _HpicfIpSlaHistSummDtoSDelay_Type()
)
hpicfIpSlaHistSummDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummDtoSDelay.setStatus("current")
_HpicfIpSlaHistAggrTable_Object = MibTable
hpicfIpSlaHistAggrTable = _HpicfIpSlaHistAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrTable.setStatus("current")
_HpicfIpSlaHistAggrEntry_Object = MibTableRow
hpicfIpSlaHistAggrEntry = _HpicfIpSlaHistAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1)
)
hpicfIpSlaHistAggrEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaID"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrEntry.setStatus("current")
_HpicfIpSlaHistAggrMinRTT_Type = Unsigned32
_HpicfIpSlaHistAggrMinRTT_Object = MibTableColumn
hpicfIpSlaHistAggrMinRTT = _HpicfIpSlaHistAggrMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 1),
    _HpicfIpSlaHistAggrMinRTT_Type()
)
hpicfIpSlaHistAggrMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinRTT.setStatus("current")
_HpicfIpSlaHistAggrMaxRTT_Type = Unsigned32
_HpicfIpSlaHistAggrMaxRTT_Object = MibTableColumn
hpicfIpSlaHistAggrMaxRTT = _HpicfIpSlaHistAggrMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 2),
    _HpicfIpSlaHistAggrMaxRTT_Type()
)
hpicfIpSlaHistAggrMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxRTT.setStatus("current")
_HpicfIpSlaHistAggrNumOfRTT_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfRTT_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfRTT = _HpicfIpSlaHistAggrNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 3),
    _HpicfIpSlaHistAggrNumOfRTT_Type()
)
hpicfIpSlaHistAggrNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfRTT.setStatus("current")
_HpicfIpSlaHistAggrAvgRTT_Type = Unsigned32
_HpicfIpSlaHistAggrAvgRTT_Object = MibTableColumn
hpicfIpSlaHistAggrAvgRTT = _HpicfIpSlaHistAggrAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 4),
    _HpicfIpSlaHistAggrAvgRTT_Type()
)
hpicfIpSlaHistAggrAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrAvgRTT.setStatus("current")
_HpicfIpSlaHistAggrTotalRTT_Type = Unsigned32
_HpicfIpSlaHistAggrTotalRTT_Object = MibTableColumn
hpicfIpSlaHistAggrTotalRTT = _HpicfIpSlaHistAggrTotalRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 5),
    _HpicfIpSlaHistAggrTotalRTT_Type()
)
hpicfIpSlaHistAggrTotalRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrTotalRTT.setStatus("current")
_HpicfIpSlaHistAggrRTT2_Type = Unsigned32
_HpicfIpSlaHistAggrRTT2_Object = MibTableColumn
hpicfIpSlaHistAggrRTT2 = _HpicfIpSlaHistAggrRTT2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 6),
    _HpicfIpSlaHistAggrRTT2_Type()
)
hpicfIpSlaHistAggrRTT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrRTT2.setStatus("current")
_HpicfIpSlaHistAggrFrstProbStTime_Type = Unsigned32
_HpicfIpSlaHistAggrFrstProbStTime_Object = MibTableColumn
hpicfIpSlaHistAggrFrstProbStTime = _HpicfIpSlaHistAggrFrstProbStTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 7),
    _HpicfIpSlaHistAggrFrstProbStTime_Type()
)
hpicfIpSlaHistAggrFrstProbStTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrFrstProbStTime.setStatus("current")
_HpicfIpSlaHistAggrProbFailReason_Type = Unsigned32
_HpicfIpSlaHistAggrProbFailReason_Object = MibTableColumn
hpicfIpSlaHistAggrProbFailReason = _HpicfIpSlaHistAggrProbFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 8),
    _HpicfIpSlaHistAggrProbFailReason_Type()
)
hpicfIpSlaHistAggrProbFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrProbFailReason.setStatus("current")
_HpicfIpSlaHistAggrPacketLoss_Type = Unsigned32
_HpicfIpSlaHistAggrPacketLoss_Object = MibTableColumn
hpicfIpSlaHistAggrPacketLoss = _HpicfIpSlaHistAggrPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 9),
    _HpicfIpSlaHistAggrPacketLoss_Type()
)
hpicfIpSlaHistAggrPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrPacketLoss.setStatus("current")
_HpicfIpSlaHistAggrSentPktNum_Type = Unsigned32
_HpicfIpSlaHistAggrSentPktNum_Object = MibTableColumn
hpicfIpSlaHistAggrSentPktNum = _HpicfIpSlaHistAggrSentPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 10),
    _HpicfIpSlaHistAggrSentPktNum_Type()
)
hpicfIpSlaHistAggrSentPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSentPktNum.setStatus("current")
_HpicfIpSlaHistAggrRecvdPktNum_Type = Unsigned32
_HpicfIpSlaHistAggrRecvdPktNum_Object = MibTableColumn
hpicfIpSlaHistAggrRecvdPktNum = _HpicfIpSlaHistAggrRecvdPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 11),
    _HpicfIpSlaHistAggrRecvdPktNum_Type()
)
hpicfIpSlaHistAggrRecvdPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrRecvdPktNum.setStatus("current")
_HpicfIpSlaHistAggrMinStoDPostv_Type = Unsigned32
_HpicfIpSlaHistAggrMinStoDPostv_Object = MibTableColumn
hpicfIpSlaHistAggrMinStoDPostv = _HpicfIpSlaHistAggrMinStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 12),
    _HpicfIpSlaHistAggrMinStoDPostv_Type()
)
hpicfIpSlaHistAggrMinStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinStoDPostv.setStatus("current")
_HpicfIpSlaHistAggrMaxStoDPostv_Type = Unsigned32
_HpicfIpSlaHistAggrMaxStoDPostv_Object = MibTableColumn
hpicfIpSlaHistAggrMaxStoDPostv = _HpicfIpSlaHistAggrMaxStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 13),
    _HpicfIpSlaHistAggrMaxStoDPostv_Type()
)
hpicfIpSlaHistAggrMaxStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxStoDPostv.setStatus("current")
_HpicfIpSlaHistAggrNumOfPosSD_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfPosSD_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfPosSD = _HpicfIpSlaHistAggrNumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 14),
    _HpicfIpSlaHistAggrNumOfPosSD_Type()
)
hpicfIpSlaHistAggrNumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfPosSD.setStatus("current")
_HpicfIpSlaHistAggrSumOfPosSD_Type = Unsigned32
_HpicfIpSlaHistAggrSumOfPosSD_Object = MibTableColumn
hpicfIpSlaHistAggrSumOfPosSD = _HpicfIpSlaHistAggrSumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 15),
    _HpicfIpSlaHistAggrSumOfPosSD_Type()
)
hpicfIpSlaHistAggrSumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumOfPosSD.setStatus("current")
_HpicfIpSlaHistAggrAvgStoDPostv_Type = Unsigned32
_HpicfIpSlaHistAggrAvgStoDPostv_Object = MibTableColumn
hpicfIpSlaHistAggrAvgStoDPostv = _HpicfIpSlaHistAggrAvgStoDPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 16),
    _HpicfIpSlaHistAggrAvgStoDPostv_Type()
)
hpicfIpSlaHistAggrAvgStoDPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrAvgStoDPostv.setStatus("current")
_HpicfIpSlaHistAggrSum2PostvSD_Type = Unsigned32
_HpicfIpSlaHistAggrSum2PostvSD_Object = MibTableColumn
hpicfIpSlaHistAggrSum2PostvSD = _HpicfIpSlaHistAggrSum2PostvSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 17),
    _HpicfIpSlaHistAggrSum2PostvSD_Type()
)
hpicfIpSlaHistAggrSum2PostvSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2PostvSD.setStatus("current")
_HpicfIpSlaHistAggrMinDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistAggrMinDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistAggrMinDtoSPostv = _HpicfIpSlaHistAggrMinDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 18),
    _HpicfIpSlaHistAggrMinDtoSPostv_Type()
)
hpicfIpSlaHistAggrMinDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinDtoSPostv.setStatus("current")
_HpicfIpSlaHistAggrMaxDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistAggrMaxDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistAggrMaxDtoSPostv = _HpicfIpSlaHistAggrMaxDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 19),
    _HpicfIpSlaHistAggrMaxDtoSPostv_Type()
)
hpicfIpSlaHistAggrMaxDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxDtoSPostv.setStatus("current")
_HpicfIpSlaHistAggrNumOfPosDS_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfPosDS_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfPosDS = _HpicfIpSlaHistAggrNumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 20),
    _HpicfIpSlaHistAggrNumOfPosDS_Type()
)
hpicfIpSlaHistAggrNumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfPosDS.setStatus("current")
_HpicfIpSlaHistAggrSumOfPosDS_Type = Unsigned32
_HpicfIpSlaHistAggrSumOfPosDS_Object = MibTableColumn
hpicfIpSlaHistAggrSumOfPosDS = _HpicfIpSlaHistAggrSumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 21),
    _HpicfIpSlaHistAggrSumOfPosDS_Type()
)
hpicfIpSlaHistAggrSumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumOfPosDS.setStatus("current")
_HpicfIpSlaHistAggrAvgDtoSPostv_Type = Unsigned32
_HpicfIpSlaHistAggrAvgDtoSPostv_Object = MibTableColumn
hpicfIpSlaHistAggrAvgDtoSPostv = _HpicfIpSlaHistAggrAvgDtoSPostv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 22),
    _HpicfIpSlaHistAggrAvgDtoSPostv_Type()
)
hpicfIpSlaHistAggrAvgDtoSPostv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrAvgDtoSPostv.setStatus("current")
_HpicfIpSlaHistAggrSum2PostvDS_Type = Unsigned32
_HpicfIpSlaHistAggrSum2PostvDS_Object = MibTableColumn
hpicfIpSlaHistAggrSum2PostvDS = _HpicfIpSlaHistAggrSum2PostvDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 23),
    _HpicfIpSlaHistAggrSum2PostvDS_Type()
)
hpicfIpSlaHistAggrSum2PostvDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2PostvDS.setStatus("current")
_HpicfIpSlaHistAggrMinStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrMinStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrMinStoDNegtv = _HpicfIpSlaHistAggrMinStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 24),
    _HpicfIpSlaHistAggrMinStoDNegtv_Type()
)
hpicfIpSlaHistAggrMinStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinStoDNegtv.setStatus("current")
_HpicfIpSlaHistAggrMaxStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrMaxStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrMaxStoDNegtv = _HpicfIpSlaHistAggrMaxStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 25),
    _HpicfIpSlaHistAggrMaxStoDNegtv_Type()
)
hpicfIpSlaHistAggrMaxStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxStoDNegtv.setStatus("current")
_HpicfIpSlaHistAggrNumOfNegSD_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfNegSD_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfNegSD = _HpicfIpSlaHistAggrNumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 26),
    _HpicfIpSlaHistAggrNumOfNegSD_Type()
)
hpicfIpSlaHistAggrNumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfNegSD.setStatus("current")
_HpicfIpSlaHistAggrSumOfNegSD_Type = Unsigned32
_HpicfIpSlaHistAggrSumOfNegSD_Object = MibTableColumn
hpicfIpSlaHistAggrSumOfNegSD = _HpicfIpSlaHistAggrSumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 27),
    _HpicfIpSlaHistAggrSumOfNegSD_Type()
)
hpicfIpSlaHistAggrSumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumOfNegSD.setStatus("current")
_HpicfIpSlaHistAggrAvgStoDNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrAvgStoDNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrAvgStoDNegtv = _HpicfIpSlaHistAggrAvgStoDNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 28),
    _HpicfIpSlaHistAggrAvgStoDNegtv_Type()
)
hpicfIpSlaHistAggrAvgStoDNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrAvgStoDNegtv.setStatus("current")
_HpicfIpSlaHistAggrSum2NegtvSD_Type = Unsigned32
_HpicfIpSlaHistAggrSum2NegtvSD_Object = MibTableColumn
hpicfIpSlaHistAggrSum2NegtvSD = _HpicfIpSlaHistAggrSum2NegtvSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 29),
    _HpicfIpSlaHistAggrSum2NegtvSD_Type()
)
hpicfIpSlaHistAggrSum2NegtvSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2NegtvSD.setStatus("current")
_HpicfIpSlaHistAggrMinDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrMinDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrMinDtoSNegtv = _HpicfIpSlaHistAggrMinDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 30),
    _HpicfIpSlaHistAggrMinDtoSNegtv_Type()
)
hpicfIpSlaHistAggrMinDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinDtoSNegtv.setStatus("current")
_HpicfIpSlaHistAggrMaxDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrMaxDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrMaxDtoSNegtv = _HpicfIpSlaHistAggrMaxDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 31),
    _HpicfIpSlaHistAggrMaxDtoSNegtv_Type()
)
hpicfIpSlaHistAggrMaxDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxDtoSNegtv.setStatus("current")
_HpicfIpSlaHistAggrNumOfNegDS_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfNegDS_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfNegDS = _HpicfIpSlaHistAggrNumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 32),
    _HpicfIpSlaHistAggrNumOfNegDS_Type()
)
hpicfIpSlaHistAggrNumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfNegDS.setStatus("current")
_HpicfIpSlaHistAggrSumOfNegDS_Type = Unsigned32
_HpicfIpSlaHistAggrSumOfNegDS_Object = MibTableColumn
hpicfIpSlaHistAggrSumOfNegDS = _HpicfIpSlaHistAggrSumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 33),
    _HpicfIpSlaHistAggrSumOfNegDS_Type()
)
hpicfIpSlaHistAggrSumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumOfNegDS.setStatus("current")
_HpicfIpSlaHistAggrAvgDtoSNegtv_Type = Unsigned32
_HpicfIpSlaHistAggrAvgDtoSNegtv_Object = MibTableColumn
hpicfIpSlaHistAggrAvgDtoSNegtv = _HpicfIpSlaHistAggrAvgDtoSNegtv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 34),
    _HpicfIpSlaHistAggrAvgDtoSNegtv_Type()
)
hpicfIpSlaHistAggrAvgDtoSNegtv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrAvgDtoSNegtv.setStatus("current")
_HpicfIpSlaHistAggrSum2NegtvDS_Type = Unsigned32
_HpicfIpSlaHistAggrSum2NegtvDS_Object = MibTableColumn
hpicfIpSlaHistAggrSum2NegtvDS = _HpicfIpSlaHistAggrSum2NegtvDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 35),
    _HpicfIpSlaHistAggrSum2NegtvDS_Type()
)
hpicfIpSlaHistAggrSum2NegtvDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2NegtvDS.setStatus("current")
_HpicfIpSlaHistAggrMinStoDDelay_Type = Unsigned32
_HpicfIpSlaHistAggrMinStoDDelay_Object = MibTableColumn
hpicfIpSlaHistAggrMinStoDDelay = _HpicfIpSlaHistAggrMinStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 36),
    _HpicfIpSlaHistAggrMinStoDDelay_Type()
)
hpicfIpSlaHistAggrMinStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinStoDDelay.setStatus("current")
_HpicfIpSlaHistAggrMaxStoDDelay_Type = Unsigned32
_HpicfIpSlaHistAggrMaxStoDDelay_Object = MibTableColumn
hpicfIpSlaHistAggrMaxStoDDelay = _HpicfIpSlaHistAggrMaxStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 37),
    _HpicfIpSlaHistAggrMaxStoDDelay_Type()
)
hpicfIpSlaHistAggrMaxStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxStoDDelay.setStatus("current")
_HpicfIpSlaHistAggrSumStoDDelay_Type = Unsigned32
_HpicfIpSlaHistAggrSumStoDDelay_Object = MibTableColumn
hpicfIpSlaHistAggrSumStoDDelay = _HpicfIpSlaHistAggrSumStoDDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 38),
    _HpicfIpSlaHistAggrSumStoDDelay_Type()
)
hpicfIpSlaHistAggrSumStoDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumStoDDelay.setStatus("current")
_HpicfIpSlaHistAggrNumOfDelaySD_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfDelaySD_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfDelaySD = _HpicfIpSlaHistAggrNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 39),
    _HpicfIpSlaHistAggrNumOfDelaySD_Type()
)
hpicfIpSlaHistAggrNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfDelaySD.setStatus("current")
_HpicfIpSlaHistAggrSum2DelaySD_Type = Unsigned32
_HpicfIpSlaHistAggrSum2DelaySD_Object = MibTableColumn
hpicfIpSlaHistAggrSum2DelaySD = _HpicfIpSlaHistAggrSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 40),
    _HpicfIpSlaHistAggrSum2DelaySD_Type()
)
hpicfIpSlaHistAggrSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2DelaySD.setStatus("current")
_HpicfIpSlaHistAggrMinDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistAggrMinDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistAggrMinDtoSDelay = _HpicfIpSlaHistAggrMinDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 41),
    _HpicfIpSlaHistAggrMinDtoSDelay_Type()
)
hpicfIpSlaHistAggrMinDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinDtoSDelay.setStatus("current")
_HpicfIpSlaHistAggrMaxDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistAggrMaxDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistAggrMaxDtoSDelay = _HpicfIpSlaHistAggrMaxDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 42),
    _HpicfIpSlaHistAggrMaxDtoSDelay_Type()
)
hpicfIpSlaHistAggrMaxDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxDtoSDelay.setStatus("current")
_HpicfIpSlaHistAggrNumOfDelayDS_Type = Unsigned32
_HpicfIpSlaHistAggrNumOfDelayDS_Object = MibTableColumn
hpicfIpSlaHistAggrNumOfDelayDS = _HpicfIpSlaHistAggrNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 43),
    _HpicfIpSlaHistAggrNumOfDelayDS_Type()
)
hpicfIpSlaHistAggrNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrNumOfDelayDS.setStatus("current")
_HpicfIpSlaHistAggrSumDtoSDelay_Type = Unsigned32
_HpicfIpSlaHistAggrSumDtoSDelay_Object = MibTableColumn
hpicfIpSlaHistAggrSumDtoSDelay = _HpicfIpSlaHistAggrSumDtoSDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 44),
    _HpicfIpSlaHistAggrSumDtoSDelay_Type()
)
hpicfIpSlaHistAggrSumDtoSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSumDtoSDelay.setStatus("current")
_HpicfIpSlaHistAggrSum2DelayDS_Type = Unsigned32
_HpicfIpSlaHistAggrSum2DelayDS_Object = MibTableColumn
hpicfIpSlaHistAggrSum2DelayDS = _HpicfIpSlaHistAggrSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 45),
    _HpicfIpSlaHistAggrSum2DelayDS_Type()
)
hpicfIpSlaHistAggrSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrSum2DelayDS.setStatus("current")
_HpicfIpSlaHistAggrMinICPIF_Type = Unsigned32
_HpicfIpSlaHistAggrMinICPIF_Object = MibTableColumn
hpicfIpSlaHistAggrMinICPIF = _HpicfIpSlaHistAggrMinICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 46),
    _HpicfIpSlaHistAggrMinICPIF_Type()
)
hpicfIpSlaHistAggrMinICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinICPIF.setStatus("current")
_HpicfIpSlaHistAggrMaxICPIF_Type = Unsigned32
_HpicfIpSlaHistAggrMaxICPIF_Object = MibTableColumn
hpicfIpSlaHistAggrMaxICPIF = _HpicfIpSlaHistAggrMaxICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 47),
    _HpicfIpSlaHistAggrMaxICPIF_Type()
)
hpicfIpSlaHistAggrMaxICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxICPIF.setStatus("current")
_HpicfIpSlaHistAggrMinMOS_Type = Unsigned32
_HpicfIpSlaHistAggrMinMOS_Object = MibTableColumn
hpicfIpSlaHistAggrMinMOS = _HpicfIpSlaHistAggrMinMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 48),
    _HpicfIpSlaHistAggrMinMOS_Type()
)
hpicfIpSlaHistAggrMinMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMinMOS.setStatus("current")
_HpicfIpSlaHistAggrMaxMOS_Type = Unsigned32
_HpicfIpSlaHistAggrMaxMOS_Object = MibTableColumn
hpicfIpSlaHistAggrMaxMOS = _HpicfIpSlaHistAggrMaxMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 8, 1, 49),
    _HpicfIpSlaHistAggrMaxMOS_Type()
)
hpicfIpSlaHistAggrMaxMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrMaxMOS.setStatus("current")
_HpicfIpSlaRespResultTable_Object = MibTable
hpicfIpSlaRespResultTable = _HpicfIpSlaRespResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespResultTable.setStatus("current")
_HpicfIpSlaRespResultEntry_Object = MibTableRow
hpicfIpSlaRespResultEntry = _HpicfIpSlaRespResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 9, 1)
)
hpicfIpSlaRespResultEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespType"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespAddress"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespL4Port"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespSrcAddress"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespResultEntry.setStatus("current")
_HpicfIpSlaRespStatus_Type = Unsigned32
_HpicfIpSlaRespStatus_Object = MibTableColumn
hpicfIpSlaRespStatus = _HpicfIpSlaRespStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 9, 1, 1),
    _HpicfIpSlaRespStatus_Type()
)
hpicfIpSlaRespStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaRespStatus.setStatus("current")
_HpicfIpSlaRespnumPktRcvd_Type = Unsigned32
_HpicfIpSlaRespnumPktRcvd_Object = MibTableColumn
hpicfIpSlaRespnumPktRcvd = _HpicfIpSlaRespnumPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 9, 1, 2),
    _HpicfIpSlaRespnumPktRcvd_Type()
)
hpicfIpSlaRespnumPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaRespnumPktRcvd.setStatus("current")
_HpicfIpSlaRespNumPktRespnd_Type = Unsigned32
_HpicfIpSlaRespNumPktRespnd_Object = MibTableColumn
hpicfIpSlaRespNumPktRespnd = _HpicfIpSlaRespNumPktRespnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 9, 1, 3),
    _HpicfIpSlaRespNumPktRespnd_Type()
)
hpicfIpSlaRespNumPktRespnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpSlaRespNumPktRespnd.setStatus("current")
_HpicfIpSlaJitterRespTable_Object = MibTable
hpicfIpSlaJitterRespTable = _HpicfIpSlaJitterRespTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespTable.setStatus("current")
_HpicfIpSlaJitterRespEntry_Object = MibTableRow
hpicfIpSlaJitterRespEntry = _HpicfIpSlaJitterRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1)
)
hpicfIpSlaJitterRespEntry.setIndexNames(
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespType"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespAddress"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespL4Port"),
    (0, "HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespSrcAddress"),
)
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespEntry.setStatus("current")


class _HpicfIpSlaJitterRespType_Type(Integer32):
    """Custom type hpicfIpSlaJitterRespType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udpJitter", 2),
          ("udpJitterVoIP", 3))
    )


_HpicfIpSlaJitterRespType_Type.__name__ = "Integer32"
_HpicfIpSlaJitterRespType_Object = MibTableColumn
hpicfIpSlaJitterRespType = _HpicfIpSlaJitterRespType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 1),
    _HpicfIpSlaJitterRespType_Type()
)
hpicfIpSlaJitterRespType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespType.setStatus("current")
_HpicfIpSlaJitterRespAddressType_Type = InetAddressType
_HpicfIpSlaJitterRespAddressType_Object = MibTableColumn
hpicfIpSlaJitterRespAddressType = _HpicfIpSlaJitterRespAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 2),
    _HpicfIpSlaJitterRespAddressType_Type()
)
hpicfIpSlaJitterRespAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespAddressType.setStatus("current")
_HpicfIpSlaJitterRespAddress_Type = InetAddress
_HpicfIpSlaJitterRespAddress_Object = MibTableColumn
hpicfIpSlaJitterRespAddress = _HpicfIpSlaJitterRespAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 3),
    _HpicfIpSlaJitterRespAddress_Type()
)
hpicfIpSlaJitterRespAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespAddress.setStatus("current")
_HpicfIpSlaJitterRespL4Port_Type = InetPortNumber
_HpicfIpSlaJitterRespL4Port_Object = MibTableColumn
hpicfIpSlaJitterRespL4Port = _HpicfIpSlaJitterRespL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 4),
    _HpicfIpSlaJitterRespL4Port_Type()
)
hpicfIpSlaJitterRespL4Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespL4Port.setStatus("current")
_HpicfIpSlaJitterRespSrcAddrType_Type = InetAddressType
_HpicfIpSlaJitterRespSrcAddrType_Object = MibTableColumn
hpicfIpSlaJitterRespSrcAddrType = _HpicfIpSlaJitterRespSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 5),
    _HpicfIpSlaJitterRespSrcAddrType_Type()
)
hpicfIpSlaJitterRespSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespSrcAddrType.setStatus("current")
_HpicfIpSlaJitterRespSrcAddress_Type = InetAddress
_HpicfIpSlaJitterRespSrcAddress_Object = MibTableColumn
hpicfIpSlaJitterRespSrcAddress = _HpicfIpSlaJitterRespSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 6),
    _HpicfIpSlaJitterRespSrcAddress_Type()
)
hpicfIpSlaJitterRespSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespSrcAddress.setStatus("current")
_HpicfIpSlaJitterRespRowStatus_Type = RowStatus
_HpicfIpSlaJitterRespRowStatus_Object = MibTableColumn
hpicfIpSlaJitterRespRowStatus = _HpicfIpSlaJitterRespRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 1, 10, 1, 7),
    _HpicfIpSlaJitterRespRowStatus_Type()
)
hpicfIpSlaJitterRespRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespRowStatus.setStatus("current")
_HpicfIpSlaConformance_ObjectIdentity = ObjectIdentity
hpicfIpSlaConformance = _HpicfIpSlaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2)
)
_HpicfIpSlaGroups_ObjectIdentity = ObjectIdentity
hpicfIpSlaGroups = _HpicfIpSlaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1)
)
_HpicfIpSlaCompliances_ObjectIdentity = ObjectIdentity
hpicfIpSlaCompliances = _HpicfIpSlaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 2)
)

# Managed Objects groups

hpicfIpSlaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 1)
)
hpicfIpSlaGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAdminState"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSourceAddressType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSourceAddress"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaL4SourcePort"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSourceInterface"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaDestAddressType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaDestAddress"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaL4DestPort"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaGroup.setStatus("current")

hpicfIpSlaAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 2)
)
hpicfIpSlaAttrGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaSchedStartTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedEndTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedFreq"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedRepeat"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrTOS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrHistorySize"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrPayloadSize"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrNumPkts"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrPktInterval"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaAttrGroup.setStatus("deprecated")

hpicfIpSlaThrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 3)
)
hpicfIpSlaThrGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaThrUpper"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThrLower"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThrType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThrCount"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThrAction"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThrRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaThrGroup.setStatus("current")

hpicfIpSlaRespGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 4)
)
hpicfIpSlaRespGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaRespAddressType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaRespRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespGroup.setStatus("current")

hpicfIpSlaMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 6)
)
hpicfIpSlaMsgGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaMsgLastProbeRcvd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgLastClrRec"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgSuccProbe"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgIntErr"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgLocIntfDown"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgResTimeout"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDNSFormatErr"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgServerFaild"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDomainNotExist"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgFunctnNotImpl"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgServerRefusd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNameNotExist"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgRRsetNotExist"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgServerNotInZone"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNameNotInZone"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDHCPFaildResln"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgOffrNotRecvd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNACKRecvd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgStatus"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNxtSched"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitPostvSDAvg"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitPostvDSAvg"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitOneWayDSAvg"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitOneWaySDAvg"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitAvgICPIF"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitAvgMOS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNameServUnreach"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDHCPReleaseErr"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgThrHitPktLoss"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDstUnreach"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgProbeSkpd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgDNSResolnFailed"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNoRoutetoTgt"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgUnbleToConctHost"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgSuccConnection"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgPossTrailDropped"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgNoRespFrmTgt"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaMsgProbeRespRecvd"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaMsgGroup.setStatus("current")

hpicfIpSlaHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 7)
)
hpicfIpSlaHistGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistTotalRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistRTT2"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistProbID"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistLastSuccProbTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistPacketLoss"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSentPktNum"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistRecvdPktNum"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfPosSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumOfPosSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2PositivesSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfPosDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumOfPosDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2PositivesDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfNegSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumOfNegSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2NegativesSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfNegDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumOfNegDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2NegativesDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfDelaySD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2DelaySD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMinDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMaxDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistNumOfDelayDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSumDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSum2DelayDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistICPIF"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistMOS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAvgDtoSDelay"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistGroup.setStatus("current")

hpicfIpSlaHistSummGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 8)
)
hpicfIpSlaHistSummGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummStartTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummStatus"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummResolvdIP"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummDescription"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistSummDtoSDelay"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistSummGroup.setStatus("current")

hpicfIpSlaAttrGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 9)
)
hpicfIpSlaAttrGroup1.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaSchedStartTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedEndTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedFreq"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaSchedRepeat"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrTOS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrHistorySize"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrPayloadSize"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrNumPkts"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrPktInterval"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrRowStatus"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrCodecType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaAttrAdvntgFactr"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaAttrGroup1.setStatus("current")

hpicfIpSlaHistAggrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 10)
)
hpicfIpSlaHistAggrGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrAvgRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrTotalRTT"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrRTT2"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrFrstProbStTime"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrProbFailReason"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrPacketLoss"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSentPktNum"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrRecvdPktNum"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfPosSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumOfPosSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrAvgStoDPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2PostvSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfPosDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumOfPosDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrAvgDtoSPostv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2PostvDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfNegSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumOfNegSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrAvgStoDNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2NegtvSD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfNegDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumOfNegDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrAvgDtoSNegtv"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2NegtvDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumStoDDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfDelaySD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2DelaySD"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrNumOfDelayDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSumDtoSDelay"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrSum2DelayDS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinICPIF"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxICPIF"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMinMOS"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaHistAggrMaxMOS"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaHistAggrGroup.setStatus("current")

hpicfIpSlaRespResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 11)
)
hpicfIpSlaRespResultGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaRespStatus"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaRespnumPktRcvd"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaRespNumPktRespnd"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaRespResultGroup.setStatus("current")

hpicfIpSlaJitterRespGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 12)
)
hpicfIpSlaJitterRespGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespAddressType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespSrcAddrType"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaJitterRespRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaJitterRespGroup.setStatus("current")


# Notification objects

hpicfIpSlaThresholdexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 0, 1)
)
hpicfIpSlaThresholdexceeded.setObjects(
    ("HPICF-IPSLA-MIB", "hpicfIpSlaThrUpper")
)
if mibBuilder.loadTexts:
    hpicfIpSlaThresholdexceeded.setStatus(
        "current"
    )

hpicfIpSlaTestCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 0, 2)
)
hpicfIpSlaTestCompletion.setObjects(
    ("HPICF-IPSLA-MIB", "hpicfIpSlaThrType")
)
if mibBuilder.loadTexts:
    hpicfIpSlaTestCompletion.setStatus(
        "current"
    )

hpicfIpSlaThresholdPktLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 0, 3)
)
hpicfIpSlaThresholdPktLoss.setObjects(
    ("HPICF-IPSLA-MIB", "hpicfIpSlaThrCount")
)
if mibBuilder.loadTexts:
    hpicfIpSlaThresholdPktLoss.setStatus(
        "current"
    )


# Notifications groups

hpicfIpSlaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 1, 5)
)
hpicfIpSlaNotificationsGroup.setObjects(
      *(("HPICF-IPSLA-MIB", "hpicfIpSlaThresholdexceeded"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaTestCompletion"),
        ("HPICF-IPSLA-MIB", "hpicfIpSlaThresholdPktLoss"))
)
if mibBuilder.loadTexts:
    hpicfIpSlaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfIpSlaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIpSlaCompliance.setStatus(
        "deprecated"
    )

hpicfIpSlaCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfIpSlaCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-IPSLA-MIB",
    **{"hpicfIpSla": hpicfIpSla,
       "hpicfIpSlaNotifications": hpicfIpSlaNotifications,
       "hpicfIpSlaThresholdexceeded": hpicfIpSlaThresholdexceeded,
       "hpicfIpSlaTestCompletion": hpicfIpSlaTestCompletion,
       "hpicfIpSlaThresholdPktLoss": hpicfIpSlaThresholdPktLoss,
       "hpicfIpSlaObjects": hpicfIpSlaObjects,
       "hpicfIpSlaTable": hpicfIpSlaTable,
       "hpicfIpSlaEntry": hpicfIpSlaEntry,
       "hpicfIpSlaID": hpicfIpSlaID,
       "hpicfIpSlaType": hpicfIpSlaType,
       "hpicfIpSlaAdminState": hpicfIpSlaAdminState,
       "hpicfIpSlaSourceAddressType": hpicfIpSlaSourceAddressType,
       "hpicfIpSlaSourceAddress": hpicfIpSlaSourceAddress,
       "hpicfIpSlaL4SourcePort": hpicfIpSlaL4SourcePort,
       "hpicfIpSlaSourceInterface": hpicfIpSlaSourceInterface,
       "hpicfIpSlaDestAddressType": hpicfIpSlaDestAddressType,
       "hpicfIpSlaDestAddress": hpicfIpSlaDestAddress,
       "hpicfIpSlaL4DestPort": hpicfIpSlaL4DestPort,
       "hpicfIpSlaRowStatus": hpicfIpSlaRowStatus,
       "hpicfIpSlaAttrTable": hpicfIpSlaAttrTable,
       "hpicfIpSlaAttrEntry": hpicfIpSlaAttrEntry,
       "hpicfIpSlaSchedStartTime": hpicfIpSlaSchedStartTime,
       "hpicfIpSlaSchedEndTime": hpicfIpSlaSchedEndTime,
       "hpicfIpSlaSchedFreq": hpicfIpSlaSchedFreq,
       "hpicfIpSlaSchedRepeat": hpicfIpSlaSchedRepeat,
       "hpicfIpSlaAttrTOS": hpicfIpSlaAttrTOS,
       "hpicfIpSlaAttrHistorySize": hpicfIpSlaAttrHistorySize,
       "hpicfIpSlaAttrPayloadSize": hpicfIpSlaAttrPayloadSize,
       "hpicfIpSlaAttrNumPkts": hpicfIpSlaAttrNumPkts,
       "hpicfIpSlaAttrPktInterval": hpicfIpSlaAttrPktInterval,
       "hpicfIpSlaAttrRowStatus": hpicfIpSlaAttrRowStatus,
       "hpicfIpSlaAttrCodecType": hpicfIpSlaAttrCodecType,
       "hpicfIpSlaAttrAdvntgFactr": hpicfIpSlaAttrAdvntgFactr,
       "hpicfIpSlaThrTable": hpicfIpSlaThrTable,
       "hpicfIpSlaThrEntry": hpicfIpSlaThrEntry,
       "hpicfIpSlaThrMetricType": hpicfIpSlaThrMetricType,
       "hpicfIpSlaThrUpper": hpicfIpSlaThrUpper,
       "hpicfIpSlaThrLower": hpicfIpSlaThrLower,
       "hpicfIpSlaThrType": hpicfIpSlaThrType,
       "hpicfIpSlaThrCount": hpicfIpSlaThrCount,
       "hpicfIpSlaThrAction": hpicfIpSlaThrAction,
       "hpicfIpSlaThrRowStatus": hpicfIpSlaThrRowStatus,
       "hpicfIpSlaRespTable": hpicfIpSlaRespTable,
       "hpicfIpSlaRespEntry": hpicfIpSlaRespEntry,
       "hpicfIpSlaRespType": hpicfIpSlaRespType,
       "hpicfIpSlaRespAddressType": hpicfIpSlaRespAddressType,
       "hpicfIpSlaRespAddress": hpicfIpSlaRespAddress,
       "hpicfIpSlaRespL4Port": hpicfIpSlaRespL4Port,
       "hpicfIpSlaRespRowStatus": hpicfIpSlaRespRowStatus,
       "hpicfIpSlaMsgTable": hpicfIpSlaMsgTable,
       "hpicfIpSlaMsgEntry": hpicfIpSlaMsgEntry,
       "hpicfIpSlaMsgLastProbeRcvd": hpicfIpSlaMsgLastProbeRcvd,
       "hpicfIpSlaMsgLastClrRec": hpicfIpSlaMsgLastClrRec,
       "hpicfIpSlaMsgSuccProbe": hpicfIpSlaMsgSuccProbe,
       "hpicfIpSlaMsgIntErr": hpicfIpSlaMsgIntErr,
       "hpicfIpSlaMsgLocIntfDown": hpicfIpSlaMsgLocIntfDown,
       "hpicfIpSlaMsgResTimeout": hpicfIpSlaMsgResTimeout,
       "hpicfIpSlaMsgDNSFormatErr": hpicfIpSlaMsgDNSFormatErr,
       "hpicfIpSlaMsgServerFaild": hpicfIpSlaMsgServerFaild,
       "hpicfIpSlaMsgDomainNotExist": hpicfIpSlaMsgDomainNotExist,
       "hpicfIpSlaMsgFunctnNotImpl": hpicfIpSlaMsgFunctnNotImpl,
       "hpicfIpSlaMsgServerRefusd": hpicfIpSlaMsgServerRefusd,
       "hpicfIpSlaMsgNameNotExist": hpicfIpSlaMsgNameNotExist,
       "hpicfIpSlaMsgRRsetNotExist": hpicfIpSlaMsgRRsetNotExist,
       "hpicfIpSlaMsgServerNotInZone": hpicfIpSlaMsgServerNotInZone,
       "hpicfIpSlaMsgNameNotInZone": hpicfIpSlaMsgNameNotInZone,
       "hpicfIpSlaMsgDHCPFaildResln": hpicfIpSlaMsgDHCPFaildResln,
       "hpicfIpSlaMsgOffrNotRecvd": hpicfIpSlaMsgOffrNotRecvd,
       "hpicfIpSlaMsgNACKRecvd": hpicfIpSlaMsgNACKRecvd,
       "hpicfIpSlaMsgThrHitRTT": hpicfIpSlaMsgThrHitRTT,
       "hpicfIpSlaMsgStatus": hpicfIpSlaMsgStatus,
       "hpicfIpSlaMsgNxtSched": hpicfIpSlaMsgNxtSched,
       "hpicfIpSlaMsgThrHitPostvSDAvg": hpicfIpSlaMsgThrHitPostvSDAvg,
       "hpicfIpSlaMsgThrHitPostvDSAvg": hpicfIpSlaMsgThrHitPostvDSAvg,
       "hpicfIpSlaMsgThrHitOneWayDSAvg": hpicfIpSlaMsgThrHitOneWayDSAvg,
       "hpicfIpSlaMsgThrHitOneWaySDAvg": hpicfIpSlaMsgThrHitOneWaySDAvg,
       "hpicfIpSlaMsgThrHitAvgICPIF": hpicfIpSlaMsgThrHitAvgICPIF,
       "hpicfIpSlaMsgThrHitAvgMOS": hpicfIpSlaMsgThrHitAvgMOS,
       "hpicfIpSlaMsgNameServUnreach": hpicfIpSlaMsgNameServUnreach,
       "hpicfIpSlaMsgDHCPReleaseErr": hpicfIpSlaMsgDHCPReleaseErr,
       "hpicfIpSlaMsgThrHitPktLoss": hpicfIpSlaMsgThrHitPktLoss,
       "hpicfIpSlaMsgDstUnreach": hpicfIpSlaMsgDstUnreach,
       "hpicfIpSlaMsgProbeSkpd": hpicfIpSlaMsgProbeSkpd,
       "hpicfIpSlaMsgDNSResolnFailed": hpicfIpSlaMsgDNSResolnFailed,
       "hpicfIpSlaMsgNoRoutetoTgt": hpicfIpSlaMsgNoRoutetoTgt,
       "hpicfIpSlaMsgUnbleToConctHost": hpicfIpSlaMsgUnbleToConctHost,
       "hpicfIpSlaMsgSuccConnection": hpicfIpSlaMsgSuccConnection,
       "hpicfIpSlaMsgPossTrailDropped": hpicfIpSlaMsgPossTrailDropped,
       "hpicfIpSlaMsgNoRespFrmTgt": hpicfIpSlaMsgNoRespFrmTgt,
       "hpicfIpSlaMsgProbeRespRecvd": hpicfIpSlaMsgProbeRespRecvd,
       "hpicfIpSlaHistTable": hpicfIpSlaHistTable,
       "hpicfIpSlaHistEntry": hpicfIpSlaHistEntry,
       "hpicfIpSlaHistMinRTT": hpicfIpSlaHistMinRTT,
       "hpicfIpSlaHistMaxRTT": hpicfIpSlaHistMaxRTT,
       "hpicfIpSlaHistAvgRTT": hpicfIpSlaHistAvgRTT,
       "hpicfIpSlaHistTotalRTT": hpicfIpSlaHistTotalRTT,
       "hpicfIpSlaHistRTT2": hpicfIpSlaHistRTT2,
       "hpicfIpSlaHistNumOfRTT": hpicfIpSlaHistNumOfRTT,
       "hpicfIpSlaHistProbID": hpicfIpSlaHistProbID,
       "hpicfIpSlaHistLastSuccProbTime": hpicfIpSlaHistLastSuccProbTime,
       "hpicfIpSlaHistPacketLoss": hpicfIpSlaHistPacketLoss,
       "hpicfIpSlaHistSentPktNum": hpicfIpSlaHistSentPktNum,
       "hpicfIpSlaHistRecvdPktNum": hpicfIpSlaHistRecvdPktNum,
       "hpicfIpSlaHistMinStoDPostv": hpicfIpSlaHistMinStoDPostv,
       "hpicfIpSlaHistMaxStoDPostv": hpicfIpSlaHistMaxStoDPostv,
       "hpicfIpSlaHistNumOfPosSD": hpicfIpSlaHistNumOfPosSD,
       "hpicfIpSlaHistSumOfPosSD": hpicfIpSlaHistSumOfPosSD,
       "hpicfIpSlaHistAvgStoDPostv": hpicfIpSlaHistAvgStoDPostv,
       "hpicfIpSlaHistSum2PositivesSD": hpicfIpSlaHistSum2PositivesSD,
       "hpicfIpSlaHistMinDtoSPostv": hpicfIpSlaHistMinDtoSPostv,
       "hpicfIpSlaHistMaxDtoSPostv": hpicfIpSlaHistMaxDtoSPostv,
       "hpicfIpSlaHistNumOfPosDS": hpicfIpSlaHistNumOfPosDS,
       "hpicfIpSlaHistSumOfPosDS": hpicfIpSlaHistSumOfPosDS,
       "hpicfIpSlaHistAvgDtoSPostv": hpicfIpSlaHistAvgDtoSPostv,
       "hpicfIpSlaHistSum2PositivesDS": hpicfIpSlaHistSum2PositivesDS,
       "hpicfIpSlaHistMinStoDNegtv": hpicfIpSlaHistMinStoDNegtv,
       "hpicfIpSlaHistMaxStoDNegtv": hpicfIpSlaHistMaxStoDNegtv,
       "hpicfIpSlaHistNumOfNegSD": hpicfIpSlaHistNumOfNegSD,
       "hpicfIpSlaHistSumOfNegSD": hpicfIpSlaHistSumOfNegSD,
       "hpicfIpSlaHistAvgStoDNegtv": hpicfIpSlaHistAvgStoDNegtv,
       "hpicfIpSlaHistSum2NegativesSD": hpicfIpSlaHistSum2NegativesSD,
       "hpicfIpSlaHistMinDtoSNegtv": hpicfIpSlaHistMinDtoSNegtv,
       "hpicfIpSlaHistMaxDtoSNegtv": hpicfIpSlaHistMaxDtoSNegtv,
       "hpicfIpSlaHistNumOfNegDS": hpicfIpSlaHistNumOfNegDS,
       "hpicfIpSlaHistSumOfNegDS": hpicfIpSlaHistSumOfNegDS,
       "hpicfIpSlaHistAvgDtoSNegtv": hpicfIpSlaHistAvgDtoSNegtv,
       "hpicfIpSlaHistSum2NegativesDS": hpicfIpSlaHistSum2NegativesDS,
       "hpicfIpSlaHistMinStoDDelay": hpicfIpSlaHistMinStoDDelay,
       "hpicfIpSlaHistMaxStoDDelay": hpicfIpSlaHistMaxStoDDelay,
       "hpicfIpSlaHistSumStoDDelay": hpicfIpSlaHistSumStoDDelay,
       "hpicfIpSlaHistNumOfDelaySD": hpicfIpSlaHistNumOfDelaySD,
       "hpicfIpSlaHistSum2DelaySD": hpicfIpSlaHistSum2DelaySD,
       "hpicfIpSlaHistMinDtoSDelay": hpicfIpSlaHistMinDtoSDelay,
       "hpicfIpSlaHistMaxDtoSDelay": hpicfIpSlaHistMaxDtoSDelay,
       "hpicfIpSlaHistNumOfDelayDS": hpicfIpSlaHistNumOfDelayDS,
       "hpicfIpSlaHistSumDtoSDelay": hpicfIpSlaHistSumDtoSDelay,
       "hpicfIpSlaHistSum2DelayDS": hpicfIpSlaHistSum2DelayDS,
       "hpicfIpSlaHistICPIF": hpicfIpSlaHistICPIF,
       "hpicfIpSlaHistMOS": hpicfIpSlaHistMOS,
       "hpicfIpSlaHistAvgStoDDelay": hpicfIpSlaHistAvgStoDDelay,
       "hpicfIpSlaHistAvgDtoSDelay": hpicfIpSlaHistAvgDtoSDelay,
       "hpicfIpSlaHistSummTable": hpicfIpSlaHistSummTable,
       "hpicfIpSlaHistSummEntry": hpicfIpSlaHistSummEntry,
       "hpicfIpSlaHistSummIndx": hpicfIpSlaHistSummIndx,
       "hpicfIpSlaHistSummStartTime": hpicfIpSlaHistSummStartTime,
       "hpicfIpSlaHistSummStatus": hpicfIpSlaHistSummStatus,
       "hpicfIpSlaHistSummRTT": hpicfIpSlaHistSummRTT,
       "hpicfIpSlaHistSummResolvdIP": hpicfIpSlaHistSummResolvdIP,
       "hpicfIpSlaHistSummDescription": hpicfIpSlaHistSummDescription,
       "hpicfIpSlaHistSummStoDDelay": hpicfIpSlaHistSummStoDDelay,
       "hpicfIpSlaHistSummDtoSDelay": hpicfIpSlaHistSummDtoSDelay,
       "hpicfIpSlaHistAggrTable": hpicfIpSlaHistAggrTable,
       "hpicfIpSlaHistAggrEntry": hpicfIpSlaHistAggrEntry,
       "hpicfIpSlaHistAggrMinRTT": hpicfIpSlaHistAggrMinRTT,
       "hpicfIpSlaHistAggrMaxRTT": hpicfIpSlaHistAggrMaxRTT,
       "hpicfIpSlaHistAggrNumOfRTT": hpicfIpSlaHistAggrNumOfRTT,
       "hpicfIpSlaHistAggrAvgRTT": hpicfIpSlaHistAggrAvgRTT,
       "hpicfIpSlaHistAggrTotalRTT": hpicfIpSlaHistAggrTotalRTT,
       "hpicfIpSlaHistAggrRTT2": hpicfIpSlaHistAggrRTT2,
       "hpicfIpSlaHistAggrFrstProbStTime": hpicfIpSlaHistAggrFrstProbStTime,
       "hpicfIpSlaHistAggrProbFailReason": hpicfIpSlaHistAggrProbFailReason,
       "hpicfIpSlaHistAggrPacketLoss": hpicfIpSlaHistAggrPacketLoss,
       "hpicfIpSlaHistAggrSentPktNum": hpicfIpSlaHistAggrSentPktNum,
       "hpicfIpSlaHistAggrRecvdPktNum": hpicfIpSlaHistAggrRecvdPktNum,
       "hpicfIpSlaHistAggrMinStoDPostv": hpicfIpSlaHistAggrMinStoDPostv,
       "hpicfIpSlaHistAggrMaxStoDPostv": hpicfIpSlaHistAggrMaxStoDPostv,
       "hpicfIpSlaHistAggrNumOfPosSD": hpicfIpSlaHistAggrNumOfPosSD,
       "hpicfIpSlaHistAggrSumOfPosSD": hpicfIpSlaHistAggrSumOfPosSD,
       "hpicfIpSlaHistAggrAvgStoDPostv": hpicfIpSlaHistAggrAvgStoDPostv,
       "hpicfIpSlaHistAggrSum2PostvSD": hpicfIpSlaHistAggrSum2PostvSD,
       "hpicfIpSlaHistAggrMinDtoSPostv": hpicfIpSlaHistAggrMinDtoSPostv,
       "hpicfIpSlaHistAggrMaxDtoSPostv": hpicfIpSlaHistAggrMaxDtoSPostv,
       "hpicfIpSlaHistAggrNumOfPosDS": hpicfIpSlaHistAggrNumOfPosDS,
       "hpicfIpSlaHistAggrSumOfPosDS": hpicfIpSlaHistAggrSumOfPosDS,
       "hpicfIpSlaHistAggrAvgDtoSPostv": hpicfIpSlaHistAggrAvgDtoSPostv,
       "hpicfIpSlaHistAggrSum2PostvDS": hpicfIpSlaHistAggrSum2PostvDS,
       "hpicfIpSlaHistAggrMinStoDNegtv": hpicfIpSlaHistAggrMinStoDNegtv,
       "hpicfIpSlaHistAggrMaxStoDNegtv": hpicfIpSlaHistAggrMaxStoDNegtv,
       "hpicfIpSlaHistAggrNumOfNegSD": hpicfIpSlaHistAggrNumOfNegSD,
       "hpicfIpSlaHistAggrSumOfNegSD": hpicfIpSlaHistAggrSumOfNegSD,
       "hpicfIpSlaHistAggrAvgStoDNegtv": hpicfIpSlaHistAggrAvgStoDNegtv,
       "hpicfIpSlaHistAggrSum2NegtvSD": hpicfIpSlaHistAggrSum2NegtvSD,
       "hpicfIpSlaHistAggrMinDtoSNegtv": hpicfIpSlaHistAggrMinDtoSNegtv,
       "hpicfIpSlaHistAggrMaxDtoSNegtv": hpicfIpSlaHistAggrMaxDtoSNegtv,
       "hpicfIpSlaHistAggrNumOfNegDS": hpicfIpSlaHistAggrNumOfNegDS,
       "hpicfIpSlaHistAggrSumOfNegDS": hpicfIpSlaHistAggrSumOfNegDS,
       "hpicfIpSlaHistAggrAvgDtoSNegtv": hpicfIpSlaHistAggrAvgDtoSNegtv,
       "hpicfIpSlaHistAggrSum2NegtvDS": hpicfIpSlaHistAggrSum2NegtvDS,
       "hpicfIpSlaHistAggrMinStoDDelay": hpicfIpSlaHistAggrMinStoDDelay,
       "hpicfIpSlaHistAggrMaxStoDDelay": hpicfIpSlaHistAggrMaxStoDDelay,
       "hpicfIpSlaHistAggrSumStoDDelay": hpicfIpSlaHistAggrSumStoDDelay,
       "hpicfIpSlaHistAggrNumOfDelaySD": hpicfIpSlaHistAggrNumOfDelaySD,
       "hpicfIpSlaHistAggrSum2DelaySD": hpicfIpSlaHistAggrSum2DelaySD,
       "hpicfIpSlaHistAggrMinDtoSDelay": hpicfIpSlaHistAggrMinDtoSDelay,
       "hpicfIpSlaHistAggrMaxDtoSDelay": hpicfIpSlaHistAggrMaxDtoSDelay,
       "hpicfIpSlaHistAggrNumOfDelayDS": hpicfIpSlaHistAggrNumOfDelayDS,
       "hpicfIpSlaHistAggrSumDtoSDelay": hpicfIpSlaHistAggrSumDtoSDelay,
       "hpicfIpSlaHistAggrSum2DelayDS": hpicfIpSlaHistAggrSum2DelayDS,
       "hpicfIpSlaHistAggrMinICPIF": hpicfIpSlaHistAggrMinICPIF,
       "hpicfIpSlaHistAggrMaxICPIF": hpicfIpSlaHistAggrMaxICPIF,
       "hpicfIpSlaHistAggrMinMOS": hpicfIpSlaHistAggrMinMOS,
       "hpicfIpSlaHistAggrMaxMOS": hpicfIpSlaHistAggrMaxMOS,
       "hpicfIpSlaRespResultTable": hpicfIpSlaRespResultTable,
       "hpicfIpSlaRespResultEntry": hpicfIpSlaRespResultEntry,
       "hpicfIpSlaRespStatus": hpicfIpSlaRespStatus,
       "hpicfIpSlaRespnumPktRcvd": hpicfIpSlaRespnumPktRcvd,
       "hpicfIpSlaRespNumPktRespnd": hpicfIpSlaRespNumPktRespnd,
       "hpicfIpSlaJitterRespTable": hpicfIpSlaJitterRespTable,
       "hpicfIpSlaJitterRespEntry": hpicfIpSlaJitterRespEntry,
       "hpicfIpSlaJitterRespType": hpicfIpSlaJitterRespType,
       "hpicfIpSlaJitterRespAddressType": hpicfIpSlaJitterRespAddressType,
       "hpicfIpSlaJitterRespAddress": hpicfIpSlaJitterRespAddress,
       "hpicfIpSlaJitterRespL4Port": hpicfIpSlaJitterRespL4Port,
       "hpicfIpSlaJitterRespSrcAddrType": hpicfIpSlaJitterRespSrcAddrType,
       "hpicfIpSlaJitterRespSrcAddress": hpicfIpSlaJitterRespSrcAddress,
       "hpicfIpSlaJitterRespRowStatus": hpicfIpSlaJitterRespRowStatus,
       "hpicfIpSlaConformance": hpicfIpSlaConformance,
       "hpicfIpSlaGroups": hpicfIpSlaGroups,
       "hpicfIpSlaGroup": hpicfIpSlaGroup,
       "hpicfIpSlaAttrGroup": hpicfIpSlaAttrGroup,
       "hpicfIpSlaThrGroup": hpicfIpSlaThrGroup,
       "hpicfIpSlaRespGroup": hpicfIpSlaRespGroup,
       "hpicfIpSlaNotificationsGroup": hpicfIpSlaNotificationsGroup,
       "hpicfIpSlaMsgGroup": hpicfIpSlaMsgGroup,
       "hpicfIpSlaHistGroup": hpicfIpSlaHistGroup,
       "hpicfIpSlaHistSummGroup": hpicfIpSlaHistSummGroup,
       "hpicfIpSlaAttrGroup1": hpicfIpSlaAttrGroup1,
       "hpicfIpSlaHistAggrGroup": hpicfIpSlaHistAggrGroup,
       "hpicfIpSlaRespResultGroup": hpicfIpSlaRespResultGroup,
       "hpicfIpSlaJitterRespGroup": hpicfIpSlaJitterRespGroup,
       "hpicfIpSlaCompliances": hpicfIpSlaCompliances,
       "hpicfIpSlaCompliance": hpicfIpSlaCompliance,
       "hpicfIpSlaCompliance1": hpicfIpSlaCompliance1}
)
