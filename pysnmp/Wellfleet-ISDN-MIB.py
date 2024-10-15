# SNMP MIB module (Wellfleet-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:34 2024
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

(wfIsdnGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIsdnGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfModemIfTable_Object = MibTable
wfModemIfTable = _WfModemIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1)
)
if mibBuilder.loadTexts:
    wfModemIfTable.setStatus("mandatory")
_WfModemIfEntry_Object = MibTableRow
wfModemIfEntry = _WfModemIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1)
)
wfModemIfEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfModemIfSlot"),
    (0, "Wellfleet-ISDN-MIB", "wfModemIfConnector"),
)
if mibBuilder.loadTexts:
    wfModemIfEntry.setStatus("mandatory")


class _WfModemIfDelete_Type(Integer32):
    """Custom type wfModemIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfModemIfDelete_Type.__name__ = "Integer32"
_WfModemIfDelete_Object = MibTableColumn
wfModemIfDelete = _WfModemIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 1),
    _WfModemIfDelete_Type()
)
wfModemIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfDelete.setStatus("mandatory")


class _WfModemIfSlot_Type(Integer32):
    """Custom type wfModemIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfModemIfSlot_Type.__name__ = "Integer32"
_WfModemIfSlot_Object = MibTableColumn
wfModemIfSlot = _WfModemIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 2),
    _WfModemIfSlot_Type()
)
wfModemIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfSlot.setStatus("mandatory")


class _WfModemIfConnectStatus_Type(Integer32):
    """Custom type wfModemIfConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_WfModemIfConnectStatus_Type.__name__ = "Integer32"
_WfModemIfConnectStatus_Object = MibTableColumn
wfModemIfConnectStatus = _WfModemIfConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 3),
    _WfModemIfConnectStatus_Type()
)
wfModemIfConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfConnectStatus.setStatus("mandatory")


class _WfModemIfConnector_Type(Integer32):
    """Custom type wfModemIfConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfModemIfConnector_Type.__name__ = "Integer32"
_WfModemIfConnector_Object = MibTableColumn
wfModemIfConnector = _WfModemIfConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 4),
    _WfModemIfConnector_Type()
)
wfModemIfConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfConnector.setStatus("mandatory")


class _WfModemIfCct_Type(Integer32):
    """Custom type wfModemIfCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfModemIfCct_Type.__name__ = "Integer32"
_WfModemIfCct_Object = MibTableColumn
wfModemIfCct = _WfModemIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 5),
    _WfModemIfCct_Type()
)
wfModemIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfCct.setStatus("mandatory")


class _WfModemIfConnectWhen_Type(Integer32):
    """Custom type wfModemIfConnectWhen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("enable", 2))
    )


_WfModemIfConnectWhen_Type.__name__ = "Integer32"
_WfModemIfConnectWhen_Object = MibTableColumn
wfModemIfConnectWhen = _WfModemIfConnectWhen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 6),
    _WfModemIfConnectWhen_Type()
)
wfModemIfConnectWhen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfConnectWhen.setStatus("mandatory")


class _WfModemIfConnectionTime_Type(Integer32):
    """Custom type wfModemIfConnectionTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfModemIfConnectionTime_Type.__name__ = "Integer32"
_WfModemIfConnectionTime_Object = MibTableColumn
wfModemIfConnectionTime = _WfModemIfConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 7),
    _WfModemIfConnectionTime_Type()
)
wfModemIfConnectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfConnectionTime.setStatus("mandatory")


class _WfModemIfMinDurationTime_Type(Integer32):
    """Custom type wfModemIfMinDurationTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfModemIfMinDurationTime_Type.__name__ = "Integer32"
_WfModemIfMinDurationTime_Object = MibTableColumn
wfModemIfMinDurationTime = _WfModemIfMinDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 8),
    _WfModemIfMinDurationTime_Type()
)
wfModemIfMinDurationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfMinDurationTime.setStatus("mandatory")


class _WfModemIfInactivityTime_Type(Integer32):
    """Custom type wfModemIfInactivityTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_WfModemIfInactivityTime_Type.__name__ = "Integer32"
_WfModemIfInactivityTime_Object = MibTableColumn
wfModemIfInactivityTime = _WfModemIfInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 9),
    _WfModemIfInactivityTime_Type()
)
wfModemIfInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfInactivityTime.setStatus("mandatory")


class _WfModemIfRetryDelayTime_Type(Integer32):
    """Custom type wfModemIfRetryDelayTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("default", 3)
    )


_WfModemIfRetryDelayTime_Type.__name__ = "Integer32"
_WfModemIfRetryDelayTime_Object = MibTableColumn
wfModemIfRetryDelayTime = _WfModemIfRetryDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 10),
    _WfModemIfRetryDelayTime_Type()
)
wfModemIfRetryDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfRetryDelayTime.setStatus("mandatory")


class _WfModemIfLineBandwidth_Type(Integer32):
    """Custom type wfModemIfLineBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64,
              384,
              1536)
        )
    )
    namedValues = NamedValues(
        *(("bw1536k", 1536),
          ("bw484k", 384),
          ("bw56k", 56),
          ("bw64k", 64))
    )


_WfModemIfLineBandwidth_Type.__name__ = "Integer32"
_WfModemIfLineBandwidth_Object = MibTableColumn
wfModemIfLineBandwidth = _WfModemIfLineBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 11),
    _WfModemIfLineBandwidth_Type()
)
wfModemIfLineBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfLineBandwidth.setStatus("mandatory")


class _WfModemIfChanAggrMax_Type(Integer32):
    """Custom type wfModemIfChanAggrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfModemIfChanAggrMax_Type.__name__ = "Integer32"
_WfModemIfChanAggrMax_Object = MibTableColumn
wfModemIfChanAggrMax = _WfModemIfChanAggrMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 12),
    _WfModemIfChanAggrMax_Type()
)
wfModemIfChanAggrMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfChanAggrMax.setStatus("mandatory")


class _WfModemIfChanAggrMin_Type(Integer32):
    """Custom type wfModemIfChanAggrMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfModemIfChanAggrMin_Type.__name__ = "Integer32"
_WfModemIfChanAggrMin_Object = MibTableColumn
wfModemIfChanAggrMin = _WfModemIfChanAggrMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 13),
    _WfModemIfChanAggrMin_Type()
)
wfModemIfChanAggrMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfChanAggrMin.setStatus("mandatory")


class _WfModemIfChanMgmt_Type(Integer32):
    """Custom type wfModemIfChanMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deltamgmt", 3),
          ("disablemgmt", 1),
          ("minmgmt", 2))
    )


_WfModemIfChanMgmt_Type.__name__ = "Integer32"
_WfModemIfChanMgmt_Object = MibTableColumn
wfModemIfChanMgmt = _WfModemIfChanMgmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 14),
    _WfModemIfChanMgmt_Type()
)
wfModemIfChanMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfChanMgmt.setStatus("mandatory")


class _WfModemIfRestrictType_Type(Integer32):
    """Custom type wfModemIfRestrictType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("calls", 1)
    )


_WfModemIfRestrictType_Type.__name__ = "Integer32"
_WfModemIfRestrictType_Object = MibTableColumn
wfModemIfRestrictType = _WfModemIfRestrictType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 15),
    _WfModemIfRestrictType_Type()
)
wfModemIfRestrictType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfRestrictType.setStatus("mandatory")


class _WfModemIfDialRetryCount_Type(Integer32):
    """Custom type wfModemIfDialRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfModemIfDialRetryCount_Type.__name__ = "Integer32"
_WfModemIfDialRetryCount_Object = MibTableColumn
wfModemIfDialRetryCount = _WfModemIfDialRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 16),
    _WfModemIfDialRetryCount_Type()
)
wfModemIfDialRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfDialRetryCount.setStatus("mandatory")
_WfModemIfRetries_Type = Counter32
_WfModemIfRetries_Object = MibTableColumn
wfModemIfRetries = _WfModemIfRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 17),
    _WfModemIfRetries_Type()
)
wfModemIfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfRetries.setStatus("mandatory")


class _WfModemIfForceDial_Type(Integer32):
    """Custom type wfModemIfForceDial based on Integer32"""
    defaultValue = 2

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


_WfModemIfForceDial_Type.__name__ = "Integer32"
_WfModemIfForceDial_Object = MibTableColumn
wfModemIfForceDial = _WfModemIfForceDial_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 18),
    _WfModemIfForceDial_Type()
)
wfModemIfForceDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfForceDial.setStatus("mandatory")


class _WfModemIfForceHangup_Type(Integer32):
    """Custom type wfModemIfForceHangup based on Integer32"""
    defaultValue = 2

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


_WfModemIfForceHangup_Type.__name__ = "Integer32"
_WfModemIfForceHangup_Object = MibTableColumn
wfModemIfForceHangup = _WfModemIfForceHangup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 19),
    _WfModemIfForceHangup_Type()
)
wfModemIfForceHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfForceHangup.setStatus("mandatory")
_WfModemIfBringUpHour_Type = Integer32
_WfModemIfBringUpHour_Object = MibTableColumn
wfModemIfBringUpHour = _WfModemIfBringUpHour_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 20),
    _WfModemIfBringUpHour_Type()
)
wfModemIfBringUpHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfBringUpHour.setStatus("mandatory")
_WfModemIfBringUpMinute_Type = Integer32
_WfModemIfBringUpMinute_Object = MibTableColumn
wfModemIfBringUpMinute = _WfModemIfBringUpMinute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 21),
    _WfModemIfBringUpMinute_Type()
)
wfModemIfBringUpMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfBringUpMinute.setStatus("mandatory")
_WfModemIfTakeDownHour_Type = Integer32
_WfModemIfTakeDownHour_Object = MibTableColumn
wfModemIfTakeDownHour = _WfModemIfTakeDownHour_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 22),
    _WfModemIfTakeDownHour_Type()
)
wfModemIfTakeDownHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfTakeDownHour.setStatus("mandatory")
_WfModemIfTakeDownMinute_Type = Integer32
_WfModemIfTakeDownMinute_Object = MibTableColumn
wfModemIfTakeDownMinute = _WfModemIfTakeDownMinute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 23),
    _WfModemIfTakeDownMinute_Type()
)
wfModemIfTakeDownMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfTakeDownMinute.setStatus("mandatory")
_WfModemIfConnectRmtStationNum_Type = DisplayString
_WfModemIfConnectRmtStationNum_Object = MibTableColumn
wfModemIfConnectRmtStationNum = _WfModemIfConnectRmtStationNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 24),
    _WfModemIfConnectRmtStationNum_Type()
)
wfModemIfConnectRmtStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfConnectRmtStationNum.setStatus("mandatory")
_WfModemIfConnectSubAddr_Type = DisplayString
_WfModemIfConnectSubAddr_Object = MibTableColumn
wfModemIfConnectSubAddr = _WfModemIfConnectSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 25),
    _WfModemIfConnectSubAddr_Type()
)
wfModemIfConnectSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfConnectSubAddr.setStatus("mandatory")


class _WfModemIfMediaType_Type(Integer32):
    """Custom type wfModemIfMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hayes", 3),
          ("raisedtr", 1),
          ("v25bis", 2))
    )


_WfModemIfMediaType_Type.__name__ = "Integer32"
_WfModemIfMediaType_Object = MibTableColumn
wfModemIfMediaType = _WfModemIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 26),
    _WfModemIfMediaType_Type()
)
wfModemIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIfMediaType.setStatus("mandatory")


class _WfModemIfUpperLayerTimeOut_Type(Integer32):
    """Custom type wfModemIfUpperLayerTimeOut based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfModemIfUpperLayerTimeOut_Type.__name__ = "Integer32"
_WfModemIfUpperLayerTimeOut_Object = MibTableColumn
wfModemIfUpperLayerTimeOut = _WfModemIfUpperLayerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 27),
    _WfModemIfUpperLayerTimeOut_Type()
)
wfModemIfUpperLayerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfUpperLayerTimeOut.setStatus("mandatory")


class _WfModemIfRingIndicator_Type(Integer32):
    """Custom type wfModemIfRingIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfModemIfRingIndicator_Type.__name__ = "Integer32"
_WfModemIfRingIndicator_Object = MibTableColumn
wfModemIfRingIndicator = _WfModemIfRingIndicator_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 28),
    _WfModemIfRingIndicator_Type()
)
wfModemIfRingIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfRingIndicator.setStatus("mandatory")


class _WfModemIfFsmDebug_Type(Integer32):
    """Custom type wfModemIfFsmDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfModemIfFsmDebug_Type.__name__ = "Integer32"
_WfModemIfFsmDebug_Object = MibTableColumn
wfModemIfFsmDebug = _WfModemIfFsmDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 1, 1, 29),
    _WfModemIfFsmDebug_Type()
)
wfModemIfFsmDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemIfFsmDebug.setStatus("mandatory")
_WfIsdnMsgCtrTable_Object = MibTable
wfIsdnMsgCtrTable = _WfIsdnMsgCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4)
)
if mibBuilder.loadTexts:
    wfIsdnMsgCtrTable.setStatus("mandatory")
_WfIsdnMsgCtrEntry_Object = MibTableRow
wfIsdnMsgCtrEntry = _WfIsdnMsgCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1)
)
wfIsdnMsgCtrEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnMsgCtrSlot"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnMsgCtrDslID"),
)
if mibBuilder.loadTexts:
    wfIsdnMsgCtrEntry.setStatus("mandatory")
_WfIsdnMsgCtrSlot_Type = Integer32
_WfIsdnMsgCtrSlot_Object = MibTableColumn
wfIsdnMsgCtrSlot = _WfIsdnMsgCtrSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 1),
    _WfIsdnMsgCtrSlot_Type()
)
wfIsdnMsgCtrSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnMsgCtrSlot.setStatus("mandatory")
_WfIsdnMsgCtrDslID_Type = Integer32
_WfIsdnMsgCtrDslID_Object = MibTableColumn
wfIsdnMsgCtrDslID = _WfIsdnMsgCtrDslID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 2),
    _WfIsdnMsgCtrDslID_Type()
)
wfIsdnMsgCtrDslID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnMsgCtrDslID.setStatus("mandatory")
_WfIsdnMsgCallProcInd_Type = Counter32
_WfIsdnMsgCallProcInd_Object = MibTableColumn
wfIsdnMsgCallProcInd = _WfIsdnMsgCallProcInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 3),
    _WfIsdnMsgCallProcInd_Type()
)
wfIsdnMsgCallProcInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgCallProcInd.setStatus("mandatory")
_WfIsdnMsgClearConf_Type = Counter32
_WfIsdnMsgClearConf_Object = MibTableColumn
wfIsdnMsgClearConf = _WfIsdnMsgClearConf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 4),
    _WfIsdnMsgClearConf_Type()
)
wfIsdnMsgClearConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgClearConf.setStatus("mandatory")
_WfIsdnMsgClearInd_Type = Counter32
_WfIsdnMsgClearInd_Object = MibTableColumn
wfIsdnMsgClearInd = _WfIsdnMsgClearInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 5),
    _WfIsdnMsgClearInd_Type()
)
wfIsdnMsgClearInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgClearInd.setStatus("mandatory")
_WfIsdnMsgConnectInd_Type = Counter32
_WfIsdnMsgConnectInd_Object = MibTableColumn
wfIsdnMsgConnectInd = _WfIsdnMsgConnectInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 6),
    _WfIsdnMsgConnectInd_Type()
)
wfIsdnMsgConnectInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgConnectInd.setStatus("mandatory")
_WfIsdnMsgSetupInd_Type = Counter32
_WfIsdnMsgSetupInd_Object = MibTableColumn
wfIsdnMsgSetupInd = _WfIsdnMsgSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 7),
    _WfIsdnMsgSetupInd_Type()
)
wfIsdnMsgSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgSetupInd.setStatus("mandatory")
_WfIsdnMsgRegisterConf_Type = Counter32
_WfIsdnMsgRegisterConf_Object = MibTableColumn
wfIsdnMsgRegisterConf = _WfIsdnMsgRegisterConf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 8),
    _WfIsdnMsgRegisterConf_Type()
)
wfIsdnMsgRegisterConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgRegisterConf.setStatus("mandatory")
_WfIsdnMsgMgmtInd_Type = Counter32
_WfIsdnMsgMgmtInd_Object = MibTableColumn
wfIsdnMsgMgmtInd = _WfIsdnMsgMgmtInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 9),
    _WfIsdnMsgMgmtInd_Type()
)
wfIsdnMsgMgmtInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgMgmtInd.setStatus("mandatory")
_WfIsdnMsgDiscInd_Type = Counter32
_WfIsdnMsgDiscInd_Object = MibTableColumn
wfIsdnMsgDiscInd = _WfIsdnMsgDiscInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 10),
    _WfIsdnMsgDiscInd_Type()
)
wfIsdnMsgDiscInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgDiscInd.setStatus("mandatory")
_WfIsdnMsgActInd_Type = Counter32
_WfIsdnMsgActInd_Object = MibTableColumn
wfIsdnMsgActInd = _WfIsdnMsgActInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 11),
    _WfIsdnMsgActInd_Type()
)
wfIsdnMsgActInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgActInd.setStatus("mandatory")
_WfIsdnMsgDeactInd_Type = Counter32
_WfIsdnMsgDeactInd_Object = MibTableColumn
wfIsdnMsgDeactInd = _WfIsdnMsgDeactInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 12),
    _WfIsdnMsgDeactInd_Type()
)
wfIsdnMsgDeactInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgDeactInd.setStatus("mandatory")
_WfIsdnMsgConnectConf_Type = Counter32
_WfIsdnMsgConnectConf_Object = MibTableColumn
wfIsdnMsgConnectConf = _WfIsdnMsgConnectConf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 13),
    _WfIsdnMsgConnectConf_Type()
)
wfIsdnMsgConnectConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgConnectConf.setStatus("mandatory")
_WfIsdnMsgAlertReq_Type = Counter32
_WfIsdnMsgAlertReq_Object = MibTableColumn
wfIsdnMsgAlertReq = _WfIsdnMsgAlertReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 14),
    _WfIsdnMsgAlertReq_Type()
)
wfIsdnMsgAlertReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgAlertReq.setStatus("mandatory")
_WfIsdnMsgCallProcReq_Type = Counter32
_WfIsdnMsgCallProcReq_Object = MibTableColumn
wfIsdnMsgCallProcReq = _WfIsdnMsgCallProcReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 15),
    _WfIsdnMsgCallProcReq_Type()
)
wfIsdnMsgCallProcReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgCallProcReq.setStatus("mandatory")
_WfIsdnMsgClearReq_Type = Counter32
_WfIsdnMsgClearReq_Object = MibTableColumn
wfIsdnMsgClearReq = _WfIsdnMsgClearReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 16),
    _WfIsdnMsgClearReq_Type()
)
wfIsdnMsgClearReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgClearReq.setStatus("mandatory")
_WfIsdnMsgConnectReq_Type = Counter32
_WfIsdnMsgConnectReq_Object = MibTableColumn
wfIsdnMsgConnectReq = _WfIsdnMsgConnectReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 17),
    _WfIsdnMsgConnectReq_Type()
)
wfIsdnMsgConnectReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgConnectReq.setStatus("mandatory")
_WfIsdnMsgSetupReq_Type = Counter32
_WfIsdnMsgSetupReq_Object = MibTableColumn
wfIsdnMsgSetupReq = _WfIsdnMsgSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 18),
    _WfIsdnMsgSetupReq_Type()
)
wfIsdnMsgSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgSetupReq.setStatus("mandatory")
_WfIsdnMsgMgmtReq_Type = Counter32
_WfIsdnMsgMgmtReq_Object = MibTableColumn
wfIsdnMsgMgmtReq = _WfIsdnMsgMgmtReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 19),
    _WfIsdnMsgMgmtReq_Type()
)
wfIsdnMsgMgmtReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgMgmtReq.setStatus("mandatory")
_WfIsdnMsgDiscReq_Type = Counter32
_WfIsdnMsgDiscReq_Object = MibTableColumn
wfIsdnMsgDiscReq = _WfIsdnMsgDiscReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 20),
    _WfIsdnMsgDiscReq_Type()
)
wfIsdnMsgDiscReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgDiscReq.setStatus("mandatory")
_WfIsdnMsgActReq_Type = Counter32
_WfIsdnMsgActReq_Object = MibTableColumn
wfIsdnMsgActReq = _WfIsdnMsgActReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 21),
    _WfIsdnMsgActReq_Type()
)
wfIsdnMsgActReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgActReq.setStatus("mandatory")
_WfIsdnMsgDeactReq_Type = Counter32
_WfIsdnMsgDeactReq_Object = MibTableColumn
wfIsdnMsgDeactReq = _WfIsdnMsgDeactReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 22),
    _WfIsdnMsgDeactReq_Type()
)
wfIsdnMsgDeactReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgDeactReq.setStatus("mandatory")
_WfIsdnMsgAlertInd_Type = Counter32
_WfIsdnMsgAlertInd_Object = MibTableColumn
wfIsdnMsgAlertInd = _WfIsdnMsgAlertInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 23),
    _WfIsdnMsgAlertInd_Type()
)
wfIsdnMsgAlertInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgAlertInd.setStatus("mandatory")
_WfIsdnMsgInfoInd_Type = Counter32
_WfIsdnMsgInfoInd_Object = MibTableColumn
wfIsdnMsgInfoInd = _WfIsdnMsgInfoInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 4, 1, 24),
    _WfIsdnMsgInfoInd_Type()
)
wfIsdnMsgInfoInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnMsgInfoInd.setStatus("mandatory")
_WfIsdnHostActionTable_Object = MibTable
wfIsdnHostActionTable = _WfIsdnHostActionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5)
)
if mibBuilder.loadTexts:
    wfIsdnHostActionTable.setStatus("mandatory")
_WfIsdnHostActionEntry_Object = MibTableRow
wfIsdnHostActionEntry = _WfIsdnHostActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1)
)
wfIsdnHostActionEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnHostActSlot"),
)
if mibBuilder.loadTexts:
    wfIsdnHostActionEntry.setStatus("mandatory")
_WfIsdnHostActSlot_Type = Integer32
_WfIsdnHostActSlot_Object = MibTableColumn
wfIsdnHostActSlot = _WfIsdnHostActSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 1),
    _WfIsdnHostActSlot_Type()
)
wfIsdnHostActSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnHostActSlot.setStatus("mandatory")
_WfIsdnHostActDslId_Type = Integer32
_WfIsdnHostActDslId_Object = MibTableColumn
wfIsdnHostActDslId = _WfIsdnHostActDslId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 2),
    _WfIsdnHostActDslId_Type()
)
wfIsdnHostActDslId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActDslId.setStatus("mandatory")
_WfIsdnHostActCallID_Type = Integer32
_WfIsdnHostActCallID_Object = MibTableColumn
wfIsdnHostActCallID = _WfIsdnHostActCallID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 3),
    _WfIsdnHostActCallID_Type()
)
wfIsdnHostActCallID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCallID.setStatus("mandatory")


class _WfIsdnHostActMsgType_Type(Integer32):
    """Custom type wfIsdnHostActMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              28,
              50,
              82,
              83)
        )
    )
    namedValues = NamedValues(
        *(("activate", 82),
          ("deactivate", 83),
          ("disc", 50),
          ("info", 15),
          ("setup", 28))
    )


_WfIsdnHostActMsgType_Type.__name__ = "Integer32"
_WfIsdnHostActMsgType_Object = MibTableColumn
wfIsdnHostActMsgType = _WfIsdnHostActMsgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 4),
    _WfIsdnHostActMsgType_Type()
)
wfIsdnHostActMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActMsgType.setStatus("mandatory")


class _WfIsdnHostActCalledPtyType_Type(Integer32):
    """Custom type wfIsdnHostActCalledPtyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intl", 1),
          ("loc", 4),
          ("nat", 2))
    )


_WfIsdnHostActCalledPtyType_Type.__name__ = "Integer32"
_WfIsdnHostActCalledPtyType_Object = MibTableColumn
wfIsdnHostActCalledPtyType = _WfIsdnHostActCalledPtyType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 5),
    _WfIsdnHostActCalledPtyType_Type()
)
wfIsdnHostActCalledPtyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCalledPtyType.setStatus("mandatory")


class _WfIsdnHostActCalledPtyPlan_Type(Integer32):
    """Custom type wfIsdnHostActCalledPtyPlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("pvt", 9),
          ("tele", 2))
    )


_WfIsdnHostActCalledPtyPlan_Type.__name__ = "Integer32"
_WfIsdnHostActCalledPtyPlan_Object = MibTableColumn
wfIsdnHostActCalledPtyPlan = _WfIsdnHostActCalledPtyPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 6),
    _WfIsdnHostActCalledPtyPlan_Type()
)
wfIsdnHostActCalledPtyPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCalledPtyPlan.setStatus("mandatory")
_WfIsdnHostActCalledPtyNum_Type = OctetString
_WfIsdnHostActCalledPtyNum_Object = MibTableColumn
wfIsdnHostActCalledPtyNum = _WfIsdnHostActCalledPtyNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 7),
    _WfIsdnHostActCalledPtyNum_Type()
)
wfIsdnHostActCalledPtyNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCalledPtyNum.setStatus("mandatory")


class _WfIsdnHostActCallingPtyType_Type(Integer32):
    """Custom type wfIsdnHostActCallingPtyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intl", 1),
          ("loc", 4),
          ("nat", 2))
    )


_WfIsdnHostActCallingPtyType_Type.__name__ = "Integer32"
_WfIsdnHostActCallingPtyType_Object = MibTableColumn
wfIsdnHostActCallingPtyType = _WfIsdnHostActCallingPtyType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 8),
    _WfIsdnHostActCallingPtyType_Type()
)
wfIsdnHostActCallingPtyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCallingPtyType.setStatus("mandatory")


class _WfIsdnHostActCallingPtyPlan_Type(Integer32):
    """Custom type wfIsdnHostActCallingPtyPlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("pvt", 9),
          ("tele", 2))
    )


_WfIsdnHostActCallingPtyPlan_Type.__name__ = "Integer32"
_WfIsdnHostActCallingPtyPlan_Object = MibTableColumn
wfIsdnHostActCallingPtyPlan = _WfIsdnHostActCallingPtyPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 9),
    _WfIsdnHostActCallingPtyPlan_Type()
)
wfIsdnHostActCallingPtyPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCallingPtyPlan.setStatus("mandatory")
_WfIsdnHostActCallingPtyNum_Type = OctetString
_WfIsdnHostActCallingPtyNum_Object = MibTableColumn
wfIsdnHostActCallingPtyNum = _WfIsdnHostActCallingPtyNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 10),
    _WfIsdnHostActCallingPtyNum_Type()
)
wfIsdnHostActCallingPtyNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCallingPtyNum.setStatus("mandatory")


class _WfIsdnHostActCallingPtyPres_Type(Integer32):
    """Custom type wfIsdnHostActCallingPtyPres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rest", 1),
          ("unavl", 2))
    )


_WfIsdnHostActCallingPtyPres_Type.__name__ = "Integer32"
_WfIsdnHostActCallingPtyPres_Object = MibTableColumn
wfIsdnHostActCallingPtyPres = _WfIsdnHostActCallingPtyPres_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 11),
    _WfIsdnHostActCallingPtyPres_Type()
)
wfIsdnHostActCallingPtyPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCallingPtyPres.setStatus("mandatory")
_WfIsdnHostActChanPrefBit_Type = Integer32
_WfIsdnHostActChanPrefBit_Object = MibTableColumn
wfIsdnHostActChanPrefBit = _WfIsdnHostActChanPrefBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 12),
    _WfIsdnHostActChanPrefBit_Type()
)
wfIsdnHostActChanPrefBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActChanPrefBit.setStatus("mandatory")


class _WfIsdnHostActChanSelection_Type(Integer32):
    """Custom type wfIsdnHostActChanSelection based on Integer32"""
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
        *(("channel", 3),
          ("channelb1", 1),
          ("channelb2", 2))
    )


_WfIsdnHostActChanSelection_Type.__name__ = "Integer32"
_WfIsdnHostActChanSelection_Object = MibTableColumn
wfIsdnHostActChanSelection = _WfIsdnHostActChanSelection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 13),
    _WfIsdnHostActChanSelection_Type()
)
wfIsdnHostActChanSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActChanSelection.setStatus("mandatory")


class _WfIsdnHostActCauseCode_Type(Integer32):
    """Custom type wfIsdnHostActCauseCode based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              21,
              31,
              54)
        )
    )
    namedValues = NamedValues(
        *(("barred", 54),
          ("normal", 16),
          ("rejected", 21),
          ("unspecified", 31))
    )


_WfIsdnHostActCauseCode_Type.__name__ = "Integer32"
_WfIsdnHostActCauseCode_Object = MibTableColumn
wfIsdnHostActCauseCode = _WfIsdnHostActCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 14),
    _WfIsdnHostActCauseCode_Type()
)
wfIsdnHostActCauseCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCauseCode.setStatus("mandatory")


class _WfIsdnHostActTransferCap_Type(Integer32):
    """Custom type wfIsdnHostActTransferCap based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 9),
          ("unrestricted", 8))
    )


_WfIsdnHostActTransferCap_Type.__name__ = "Integer32"
_WfIsdnHostActTransferCap_Object = MibTableColumn
wfIsdnHostActTransferCap = _WfIsdnHostActTransferCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 15),
    _WfIsdnHostActTransferCap_Type()
)
wfIsdnHostActTransferCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActTransferCap.setStatus("mandatory")


class _WfIsdnHostActCldSadType_Type(Integer32):
    """Custom type wfIsdnHostActCldSadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("user", 2)
    )


_WfIsdnHostActCldSadType_Type.__name__ = "Integer32"
_WfIsdnHostActCldSadType_Object = MibTableColumn
wfIsdnHostActCldSadType = _WfIsdnHostActCldSadType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 16),
    _WfIsdnHostActCldSadType_Type()
)
wfIsdnHostActCldSadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCldSadType.setStatus("mandatory")
_WfIsdnHostActCldSadNum_Type = OctetString
_WfIsdnHostActCldSadNum_Object = MibTableColumn
wfIsdnHostActCldSadNum = _WfIsdnHostActCldSadNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 17),
    _WfIsdnHostActCldSadNum_Type()
)
wfIsdnHostActCldSadNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCldSadNum.setStatus("mandatory")


class _WfIsdnHostActClgSadType_Type(Integer32):
    """Custom type wfIsdnHostActClgSadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("user", 2)
    )


_WfIsdnHostActClgSadType_Type.__name__ = "Integer32"
_WfIsdnHostActClgSadType_Object = MibTableColumn
wfIsdnHostActClgSadType = _WfIsdnHostActClgSadType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 18),
    _WfIsdnHostActClgSadType_Type()
)
wfIsdnHostActClgSadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActClgSadType.setStatus("mandatory")
_WfIsdnHostActClgSadNum_Type = OctetString
_WfIsdnHostActClgSadNum_Object = MibTableColumn
wfIsdnHostActClgSadNum = _WfIsdnHostActClgSadNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 19),
    _WfIsdnHostActClgSadNum_Type()
)
wfIsdnHostActClgSadNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActClgSadNum.setStatus("mandatory")


class _WfIsdnHostActCldSadPres_Type(Integer32):
    """Custom type wfIsdnHostActCldSadPres based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_WfIsdnHostActCldSadPres_Type.__name__ = "Integer32"
_WfIsdnHostActCldSadPres_Object = MibTableColumn
wfIsdnHostActCldSadPres = _WfIsdnHostActCldSadPres_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 20),
    _WfIsdnHostActCldSadPres_Type()
)
wfIsdnHostActCldSadPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActCldSadPres.setStatus("mandatory")


class _WfIsdnHostActClgSadPres_Type(Integer32):
    """Custom type wfIsdnHostActClgSadPres based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_WfIsdnHostActClgSadPres_Type.__name__ = "Integer32"
_WfIsdnHostActClgSadPres_Object = MibTableColumn
wfIsdnHostActClgSadPres = _WfIsdnHostActClgSadPres_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 5, 1, 21),
    _WfIsdnHostActClgSadPres_Type()
)
wfIsdnHostActClgSadPres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnHostActClgSadPres.setStatus("mandatory")
_WfIsdnSwitchCfgTable_Object = MibTable
wfIsdnSwitchCfgTable = _WfIsdnSwitchCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6)
)
if mibBuilder.loadTexts:
    wfIsdnSwitchCfgTable.setStatus("mandatory")
_WfIsdnSwitchCfgEntry_Object = MibTableRow
wfIsdnSwitchCfgEntry = _WfIsdnSwitchCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1)
)
wfIsdnSwitchCfgEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnSwitchCfgSlot"),
)
if mibBuilder.loadTexts:
    wfIsdnSwitchCfgEntry.setStatus("mandatory")


class _WfIsdnSwitchCfgDelete_Type(Integer32):
    """Custom type wfIsdnSwitchCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIsdnSwitchCfgDelete_Type.__name__ = "Integer32"
_WfIsdnSwitchCfgDelete_Object = MibTableColumn
wfIsdnSwitchCfgDelete = _WfIsdnSwitchCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 1),
    _WfIsdnSwitchCfgDelete_Type()
)
wfIsdnSwitchCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchCfgDelete.setStatus("mandatory")


class _WfIsdnSwitchCfgSlot_Type(Integer32):
    """Custom type wfIsdnSwitchCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfIsdnSwitchCfgSlot_Type.__name__ = "Integer32"
_WfIsdnSwitchCfgSlot_Object = MibTableColumn
wfIsdnSwitchCfgSlot = _WfIsdnSwitchCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 2),
    _WfIsdnSwitchCfgSlot_Type()
)
wfIsdnSwitchCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnSwitchCfgSlot.setStatus("mandatory")


class _WfIsdnSwitchCfgType_Type(Integer32):
    """Custom type wfIsdnSwitchCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              10,
              11,
              12,
              14,
              15,
              17,
              18,
              20,
              21,
              22,
              27,
              29)
        )
    )
    namedValues = NamedValues(
        *(("bri5ess", 4),
          ("bridms100", 7),
          ("brikdd", 11),
          ("brinet3", 1),
          ("brini1", 15),
          ("brintt", 12),
          ("briswissnet3", 2),
          ("brits013", 14),
          ("brivn3", 10),
          ("pri4ess", 17),
          ("pri5ess", 18),
          ("pridms100", 20),
          ("prikdd", 21),
          ("prinet5", 27),
          ("printt", 22),
          ("prits014", 29))
    )


_WfIsdnSwitchCfgType_Type.__name__ = "Integer32"
_WfIsdnSwitchCfgType_Object = MibTableColumn
wfIsdnSwitchCfgType = _WfIsdnSwitchCfgType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 3),
    _WfIsdnSwitchCfgType_Type()
)
wfIsdnSwitchCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchCfgType.setStatus("mandatory")
_WfIsdnSwitchTestMode_Type = Integer32
_WfIsdnSwitchTestMode_Object = MibTableColumn
wfIsdnSwitchTestMode = _WfIsdnSwitchTestMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 4),
    _WfIsdnSwitchTestMode_Type()
)
wfIsdnSwitchTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchTestMode.setStatus("mandatory")


class _WfIsdnSwitchIncomingFilter_Type(Integer32):
    """Custom type wfIsdnSwitchIncomingFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdnSwitchIncomingFilter_Type.__name__ = "Integer32"
_WfIsdnSwitchIncomingFilter_Object = MibTableColumn
wfIsdnSwitchIncomingFilter = _WfIsdnSwitchIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 5),
    _WfIsdnSwitchIncomingFilter_Type()
)
wfIsdnSwitchIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchIncomingFilter.setStatus("mandatory")


class _WfIsdnSwitchTraceFacility_Type(Integer32):
    """Custom type wfIsdnSwitchTraceFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_WfIsdnSwitchTraceFacility_Type.__name__ = "Integer32"
_WfIsdnSwitchTraceFacility_Object = MibTableColumn
wfIsdnSwitchTraceFacility = _WfIsdnSwitchTraceFacility_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 6),
    _WfIsdnSwitchTraceFacility_Type()
)
wfIsdnSwitchTraceFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchTraceFacility.setStatus("mandatory")
_WfIsdnSwitchScreenedCalls_Type = Counter32
_WfIsdnSwitchScreenedCalls_Object = MibTableColumn
wfIsdnSwitchScreenedCalls = _WfIsdnSwitchScreenedCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 7),
    _WfIsdnSwitchScreenedCalls_Type()
)
wfIsdnSwitchScreenedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnSwitchScreenedCalls.setStatus("mandatory")


class _WfIsdnSwitchSendingComplete_Type(Integer32):
    """Custom type wfIsdnSwitchSendingComplete based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnSwitchSendingComplete_Type.__name__ = "Integer32"
_WfIsdnSwitchSendingComplete_Object = MibTableColumn
wfIsdnSwitchSendingComplete = _WfIsdnSwitchSendingComplete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 8),
    _WfIsdnSwitchSendingComplete_Type()
)
wfIsdnSwitchSendingComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchSendingComplete.setStatus("mandatory")


class _WfIsdnSwitchGlobalRateAdaption_Type(Integer32):
    """Custom type wfIsdnSwitchGlobalRateAdaption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56", 2),
          ("rate64", 1))
    )


_WfIsdnSwitchGlobalRateAdaption_Type.__name__ = "Integer32"
_WfIsdnSwitchGlobalRateAdaption_Object = MibTableColumn
wfIsdnSwitchGlobalRateAdaption = _WfIsdnSwitchGlobalRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 9),
    _WfIsdnSwitchGlobalRateAdaption_Type()
)
wfIsdnSwitchGlobalRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchGlobalRateAdaption.setStatus("mandatory")


class _WfIsdnSwitchX25D_Type(Integer32):
    """Custom type wfIsdnSwitchX25D based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnSwitchX25D_Type.__name__ = "Integer32"
_WfIsdnSwitchX25D_Object = MibTableColumn
wfIsdnSwitchX25D = _WfIsdnSwitchX25D_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 10),
    _WfIsdnSwitchX25D_Type()
)
wfIsdnSwitchX25D.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchX25D.setStatus("mandatory")


class _WfIsdnSwitchAllowedScreeningBits_Type(Integer32):
    """Custom type wfIsdnSwitchAllowedScreeningBits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WfIsdnSwitchAllowedScreeningBits_Type.__name__ = "Integer32"
_WfIsdnSwitchAllowedScreeningBits_Object = MibTableColumn
wfIsdnSwitchAllowedScreeningBits = _WfIsdnSwitchAllowedScreeningBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 11),
    _WfIsdnSwitchAllowedScreeningBits_Type()
)
wfIsdnSwitchAllowedScreeningBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchAllowedScreeningBits.setStatus("mandatory")


class _WfIsdnSwitchPreauthTodCheck_Type(Integer32):
    """Custom type wfIsdnSwitchPreauthTodCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnSwitchPreauthTodCheck_Type.__name__ = "Integer32"
_WfIsdnSwitchPreauthTodCheck_Object = MibTableColumn
wfIsdnSwitchPreauthTodCheck = _WfIsdnSwitchPreauthTodCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 6, 1, 12),
    _WfIsdnSwitchPreauthTodCheck_Type()
)
wfIsdnSwitchPreauthTodCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSwitchPreauthTodCheck.setStatus("mandatory")
_WfIsdnCallInfoTable_Object = MibTable
wfIsdnCallInfoTable = _WfIsdnCallInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7)
)
if mibBuilder.loadTexts:
    wfIsdnCallInfoTable.setStatus("mandatory")
_WfIsdnCallInfoEntry_Object = MibTableRow
wfIsdnCallInfoEntry = _WfIsdnCallInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1)
)
wfIsdnCallInfoEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnCallInfoSlot"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnCallInfoDslID"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnCallInfoCallID"),
)
if mibBuilder.loadTexts:
    wfIsdnCallInfoEntry.setStatus("mandatory")
_WfIsdnCallInfoSlot_Type = Integer32
_WfIsdnCallInfoSlot_Object = MibTableColumn
wfIsdnCallInfoSlot = _WfIsdnCallInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 1),
    _WfIsdnCallInfoSlot_Type()
)
wfIsdnCallInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoSlot.setStatus("mandatory")
_WfIsdnCallInfoDslID_Type = Integer32
_WfIsdnCallInfoDslID_Object = MibTableColumn
wfIsdnCallInfoDslID = _WfIsdnCallInfoDslID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 2),
    _WfIsdnCallInfoDslID_Type()
)
wfIsdnCallInfoDslID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoDslID.setStatus("mandatory")
_WfIsdnCallInfoCallID_Type = Integer32
_WfIsdnCallInfoCallID_Object = MibTableColumn
wfIsdnCallInfoCallID = _WfIsdnCallInfoCallID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 3),
    _WfIsdnCallInfoCallID_Type()
)
wfIsdnCallInfoCallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCallID.setStatus("mandatory")
_WfIsdnCallInfoBChannel_Type = Integer32
_WfIsdnCallInfoBChannel_Object = MibTableColumn
wfIsdnCallInfoBChannel = _WfIsdnCallInfoBChannel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 4),
    _WfIsdnCallInfoBChannel_Type()
)
wfIsdnCallInfoBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoBChannel.setStatus("mandatory")
_WfIsdnCallInfoCallState_Type = Integer32
_WfIsdnCallInfoCallState_Object = MibTableColumn
wfIsdnCallInfoCallState = _WfIsdnCallInfoCallState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 5),
    _WfIsdnCallInfoCallState_Type()
)
wfIsdnCallInfoCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCallState.setStatus("mandatory")


class _WfIsdnCallInfoTransferCap_Type(Integer32):
    """Custom type wfIsdnCallInfoTransferCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("rdi", 9),
          ("udi", 8))
    )


_WfIsdnCallInfoTransferCap_Type.__name__ = "Integer32"
_WfIsdnCallInfoTransferCap_Object = MibTableColumn
wfIsdnCallInfoTransferCap = _WfIsdnCallInfoTransferCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 6),
    _WfIsdnCallInfoTransferCap_Type()
)
wfIsdnCallInfoTransferCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoTransferCap.setStatus("mandatory")
_WfIsdnCallInfoCalledPtyNum_Type = DisplayString
_WfIsdnCallInfoCalledPtyNum_Object = MibTableColumn
wfIsdnCallInfoCalledPtyNum = _WfIsdnCallInfoCalledPtyNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 7),
    _WfIsdnCallInfoCalledPtyNum_Type()
)
wfIsdnCallInfoCalledPtyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCalledPtyNum.setStatus("mandatory")
_WfIsdnCallInfoCallingPtyNum_Type = DisplayString
_WfIsdnCallInfoCallingPtyNum_Object = MibTableColumn
wfIsdnCallInfoCallingPtyNum = _WfIsdnCallInfoCallingPtyNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 8),
    _WfIsdnCallInfoCallingPtyNum_Type()
)
wfIsdnCallInfoCallingPtyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCallingPtyNum.setStatus("mandatory")
_WfIsdnCallInfoDuration_Type = Integer32
_WfIsdnCallInfoDuration_Object = MibTableColumn
wfIsdnCallInfoDuration = _WfIsdnCallInfoDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 9),
    _WfIsdnCallInfoDuration_Type()
)
wfIsdnCallInfoDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoDuration.setStatus("mandatory")
_WfIsdnCallInfoConnectTime_Type = Integer32
_WfIsdnCallInfoConnectTime_Object = MibTableColumn
wfIsdnCallInfoConnectTime = _WfIsdnCallInfoConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 10),
    _WfIsdnCallInfoConnectTime_Type()
)
wfIsdnCallInfoConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoConnectTime.setStatus("mandatory")
_WfIsdnCallInfoRateAdaption_Type = Integer32
_WfIsdnCallInfoRateAdaption_Object = MibTableColumn
wfIsdnCallInfoRateAdaption = _WfIsdnCallInfoRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 11),
    _WfIsdnCallInfoRateAdaption_Type()
)
wfIsdnCallInfoRateAdaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoRateAdaption.setStatus("mandatory")
_WfIsdnCallInfoCalledPtySub_Type = DisplayString
_WfIsdnCallInfoCalledPtySub_Object = MibTableColumn
wfIsdnCallInfoCalledPtySub = _WfIsdnCallInfoCalledPtySub_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 12),
    _WfIsdnCallInfoCalledPtySub_Type()
)
wfIsdnCallInfoCalledPtySub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCalledPtySub.setStatus("mandatory")
_WfIsdnCallInfoCallingPtySub_Type = DisplayString
_WfIsdnCallInfoCallingPtySub_Object = MibTableColumn
wfIsdnCallInfoCallingPtySub = _WfIsdnCallInfoCallingPtySub_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 13),
    _WfIsdnCallInfoCallingPtySub_Type()
)
wfIsdnCallInfoCallingPtySub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCallingPtySub.setStatus("mandatory")


class _WfIsdnCallInfoChanType_Type(Integer32):
    """Custom type wfIsdnCallInfoChanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bchannel", 1),
          ("multirate", 2))
    )


_WfIsdnCallInfoChanType_Type.__name__ = "Integer32"
_WfIsdnCallInfoChanType_Object = MibTableColumn
wfIsdnCallInfoChanType = _WfIsdnCallInfoChanType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 14),
    _WfIsdnCallInfoChanType_Type()
)
wfIsdnCallInfoChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoChanType.setStatus("mandatory")
_WfIsdnCallInfoAggrChanCnt_Type = Integer32
_WfIsdnCallInfoAggrChanCnt_Object = MibTableColumn
wfIsdnCallInfoAggrChanCnt = _WfIsdnCallInfoAggrChanCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 15),
    _WfIsdnCallInfoAggrChanCnt_Type()
)
wfIsdnCallInfoAggrChanCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoAggrChanCnt.setStatus("mandatory")
_WfIsdnCallInfoTimeslotMask_Type = Integer32
_WfIsdnCallInfoTimeslotMask_Object = MibTableColumn
wfIsdnCallInfoTimeslotMask = _WfIsdnCallInfoTimeslotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 16),
    _WfIsdnCallInfoTimeslotMask_Type()
)
wfIsdnCallInfoTimeslotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnCallInfoTimeslotMask.setStatus("mandatory")
_WfIsdnCallInfoCct_Type = Integer32
_WfIsdnCallInfoCct_Object = MibTableColumn
wfIsdnCallInfoCct = _WfIsdnCallInfoCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 7, 1, 17),
    _WfIsdnCallInfoCct_Type()
)
wfIsdnCallInfoCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnCallInfoCct.setStatus("mandatory")
_WfIsdnBriInterfaceTable_Object = MibTable
wfIsdnBriInterfaceTable = _WfIsdnBriInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9)
)
if mibBuilder.loadTexts:
    wfIsdnBriInterfaceTable.setStatus("mandatory")
_WfIsdnBriInterfaceEntry_Object = MibTableRow
wfIsdnBriInterfaceEntry = _WfIsdnBriInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1)
)
wfIsdnBriInterfaceEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnBriSlot"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnBriConnector"),
)
if mibBuilder.loadTexts:
    wfIsdnBriInterfaceEntry.setStatus("mandatory")


class _WfIsdnBriDelete_Type(Integer32):
    """Custom type wfIsdnBriDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIsdnBriDelete_Type.__name__ = "Integer32"
_WfIsdnBriDelete_Object = MibTableColumn
wfIsdnBriDelete = _WfIsdnBriDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 1),
    _WfIsdnBriDelete_Type()
)
wfIsdnBriDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriDelete.setStatus("mandatory")


class _WfIsdnBriDisable_Type(Integer32):
    """Custom type wfIsdnBriDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnBriDisable_Type.__name__ = "Integer32"
_WfIsdnBriDisable_Object = MibTableColumn
wfIsdnBriDisable = _WfIsdnBriDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 2),
    _WfIsdnBriDisable_Type()
)
wfIsdnBriDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriDisable.setStatus("mandatory")


class _WfIsdnBriState_Type(Integer32):
    """Custom type wfIsdnBriState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 20),
          ("ubcwaiting", 10),
          ("up", 1))
    )


_WfIsdnBriState_Type.__name__ = "Integer32"
_WfIsdnBriState_Object = MibTableColumn
wfIsdnBriState = _WfIsdnBriState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 3),
    _WfIsdnBriState_Type()
)
wfIsdnBriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriState.setStatus("mandatory")
_WfIsdnBriSlot_Type = Integer32
_WfIsdnBriSlot_Object = MibTableColumn
wfIsdnBriSlot = _WfIsdnBriSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 4),
    _WfIsdnBriSlot_Type()
)
wfIsdnBriSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriSlot.setStatus("mandatory")


class _WfIsdnBriConnector_Type(Integer32):
    """Custom type wfIsdnBriConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfIsdnBriConnector_Type.__name__ = "Integer32"
_WfIsdnBriConnector_Object = MibTableColumn
wfIsdnBriConnector = _WfIsdnBriConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 5),
    _WfIsdnBriConnector_Type()
)
wfIsdnBriConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriConnector.setStatus("mandatory")


class _WfIsdnBriCct_Type(Integer32):
    """Custom type wfIsdnBriCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIsdnBriCct_Type.__name__ = "Integer32"
_WfIsdnBriCct_Object = MibTableColumn
wfIsdnBriCct = _WfIsdnBriCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 6),
    _WfIsdnBriCct_Type()
)
wfIsdnBriCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriCct.setStatus("mandatory")
_WfIsdnBriDslId_Type = Integer32
_WfIsdnBriDslId_Object = MibTableColumn
wfIsdnBriDslId = _WfIsdnBriDslId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 7),
    _WfIsdnBriDslId_Type()
)
wfIsdnBriDslId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriDslId.setStatus("mandatory")
_WfIsdnBriLineNumber_Type = Integer32
_WfIsdnBriLineNumber_Object = MibTableColumn
wfIsdnBriLineNumber = _WfIsdnBriLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 8),
    _WfIsdnBriLineNumber_Type()
)
wfIsdnBriLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriLineNumber.setStatus("mandatory")


class _WfIsdnBriModule_Type(Integer32):
    """Custom type wfIsdnBriModule based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfIsdnBriModule_Type.__name__ = "Integer32"
_WfIsdnBriModule_Object = MibTableColumn
wfIsdnBriModule = _WfIsdnBriModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 9),
    _WfIsdnBriModule_Type()
)
wfIsdnBriModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriModule.setStatus("mandatory")


class _WfIsdnBriActualConnector_Type(Integer32):
    """Custom type wfIsdnBriActualConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfIsdnBriActualConnector_Type.__name__ = "Integer32"
_WfIsdnBriActualConnector_Object = MibTableColumn
wfIsdnBriActualConnector = _WfIsdnBriActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 10),
    _WfIsdnBriActualConnector_Type()
)
wfIsdnBriActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriActualConnector.setStatus("mandatory")


class _WfIsdnBriTeState_Type(Integer32):
    """Custom type wfIsdnBriTeState based on Integer32"""
    defaultValue = 1

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
        *(("activated", 7),
          ("awaitsignal", 4),
          ("deactivated", 3),
          ("identifyinput", 5),
          ("inactive", 1),
          ("lostframing", 8),
          ("sensing", 2),
          ("synchronized", 6))
    )


_WfIsdnBriTeState_Type.__name__ = "Integer32"
_WfIsdnBriTeState_Object = MibTableColumn
wfIsdnBriTeState = _WfIsdnBriTeState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 11),
    _WfIsdnBriTeState_Type()
)
wfIsdnBriTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTeState.setStatus("mandatory")


class _WfIsdnBriMtu_Type(Integer32):
    """Custom type wfIsdnBriMtu based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1024),
    )


_WfIsdnBriMtu_Type.__name__ = "Integer32"
_WfIsdnBriMtu_Object = MibTableColumn
wfIsdnBriMtu = _WfIsdnBriMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 12),
    _WfIsdnBriMtu_Type()
)
wfIsdnBriMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriMtu.setStatus("mandatory")


class _WfIsdnBriBChanLoop_Type(Integer32):
    """Custom type wfIsdnBriBChanLoop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnBriBChanLoop_Type.__name__ = "Integer32"
_WfIsdnBriBChanLoop_Object = MibTableColumn
wfIsdnBriBChanLoop = _WfIsdnBriBChanLoop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 13),
    _WfIsdnBriBChanLoop_Type()
)
wfIsdnBriBChanLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriBChanLoop.setStatus("mandatory")


class _WfIsdnBriTimer3Tmo_Type(Integer32):
    """Custom type wfIsdnBriTimer3Tmo based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfIsdnBriTimer3Tmo_Type.__name__ = "Integer32"
_WfIsdnBriTimer3Tmo_Object = MibTableColumn
wfIsdnBriTimer3Tmo = _WfIsdnBriTimer3Tmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 14),
    _WfIsdnBriTimer3Tmo_Type()
)
wfIsdnBriTimer3Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriTimer3Tmo.setStatus("mandatory")


class _WfIsdnBriTimer4Tmo_Type(Integer32):
    """Custom type wfIsdnBriTimer4Tmo based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000),
    )


_WfIsdnBriTimer4Tmo_Type.__name__ = "Integer32"
_WfIsdnBriTimer4Tmo_Object = MibTableColumn
wfIsdnBriTimer4Tmo = _WfIsdnBriTimer4Tmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 15),
    _WfIsdnBriTimer4Tmo_Type()
)
wfIsdnBriTimer4Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriTimer4Tmo.setStatus("mandatory")
_WfIsdnBriRxOctets_Type = Counter32
_WfIsdnBriRxOctets_Object = MibTableColumn
wfIsdnBriRxOctets = _WfIsdnBriRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 16),
    _WfIsdnBriRxOctets_Type()
)
wfIsdnBriRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxOctets.setStatus("mandatory")
_WfIsdnBriRxFrames_Type = Counter32
_WfIsdnBriRxFrames_Object = MibTableColumn
wfIsdnBriRxFrames = _WfIsdnBriRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 17),
    _WfIsdnBriRxFrames_Type()
)
wfIsdnBriRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxFrames.setStatus("mandatory")
_WfIsdnBriTxOctets_Type = Counter32
_WfIsdnBriTxOctets_Object = MibTableColumn
wfIsdnBriTxOctets = _WfIsdnBriTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 18),
    _WfIsdnBriTxOctets_Type()
)
wfIsdnBriTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxOctets.setStatus("mandatory")
_WfIsdnBriTxFrames_Type = Counter32
_WfIsdnBriTxFrames_Object = MibTableColumn
wfIsdnBriTxFrames = _WfIsdnBriTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 19),
    _WfIsdnBriTxFrames_Type()
)
wfIsdnBriTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxFrames.setStatus("mandatory")
_WfIsdnBriRxErrors_Type = Counter32
_WfIsdnBriRxErrors_Object = MibTableColumn
wfIsdnBriRxErrors = _WfIsdnBriRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 20),
    _WfIsdnBriRxErrors_Type()
)
wfIsdnBriRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxErrors.setStatus("mandatory")
_WfIsdnBriTxErrors_Type = Counter32
_WfIsdnBriTxErrors_Object = MibTableColumn
wfIsdnBriTxErrors = _WfIsdnBriTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 21),
    _WfIsdnBriTxErrors_Type()
)
wfIsdnBriTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxErrors.setStatus("mandatory")
_WfIsdnBriRxLackRescs_Type = Counter32
_WfIsdnBriRxLackRescs_Object = MibTableColumn
wfIsdnBriRxLackRescs = _WfIsdnBriRxLackRescs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 22),
    _WfIsdnBriRxLackRescs_Type()
)
wfIsdnBriRxLackRescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxLackRescs.setStatus("mandatory")
_WfIsdnBriTxLackRescs_Type = Counter32
_WfIsdnBriTxLackRescs_Object = MibTableColumn
wfIsdnBriTxLackRescs = _WfIsdnBriTxLackRescs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 23),
    _WfIsdnBriTxLackRescs_Type()
)
wfIsdnBriTxLackRescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxLackRescs.setStatus("mandatory")
_WfIsdnBriTxUnderFlows_Type = Counter32
_WfIsdnBriTxUnderFlows_Object = MibTableColumn
wfIsdnBriTxUnderFlows = _WfIsdnBriTxUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 24),
    _WfIsdnBriTxUnderFlows_Type()
)
wfIsdnBriTxUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxUnderFlows.setStatus("mandatory")
_WfIsdnBriTxDChanCollisions_Type = Counter32
_WfIsdnBriTxDChanCollisions_Object = MibTableColumn
wfIsdnBriTxDChanCollisions = _WfIsdnBriTxDChanCollisions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 25),
    _WfIsdnBriTxDChanCollisions_Type()
)
wfIsdnBriTxDChanCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTxDChanCollisions.setStatus("mandatory")
_WfIsdnBriRxOverFlows_Type = Counter32
_WfIsdnBriRxOverFlows_Object = MibTableColumn
wfIsdnBriRxOverFlows = _WfIsdnBriRxOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 26),
    _WfIsdnBriRxOverFlows_Type()
)
wfIsdnBriRxOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxOverFlows.setStatus("mandatory")
_WfIsdnBriRxTooLongFrames_Type = Counter32
_WfIsdnBriRxTooLongFrames_Object = MibTableColumn
wfIsdnBriRxTooLongFrames = _WfIsdnBriRxTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 27),
    _WfIsdnBriRxTooLongFrames_Type()
)
wfIsdnBriRxTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxTooLongFrames.setStatus("mandatory")
_WfIsdnBriRxBadCrcs_Type = Counter32
_WfIsdnBriRxBadCrcs_Object = MibTableColumn
wfIsdnBriRxBadCrcs = _WfIsdnBriRxBadCrcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 28),
    _WfIsdnBriRxBadCrcs_Type()
)
wfIsdnBriRxBadCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxBadCrcs.setStatus("mandatory")
_WfIsdnBriRxAborts_Type = Counter32
_WfIsdnBriRxAborts_Object = MibTableColumn
wfIsdnBriRxAborts = _WfIsdnBriRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 29),
    _WfIsdnBriRxAborts_Type()
)
wfIsdnBriRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxAborts.setStatus("mandatory")
_WfIsdnBriRxReplenMisses_Type = Counter32
_WfIsdnBriRxReplenMisses_Object = MibTableColumn
wfIsdnBriRxReplenMisses = _WfIsdnBriRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 30),
    _WfIsdnBriRxReplenMisses_Type()
)
wfIsdnBriRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriRxReplenMisses.setStatus("mandatory")
_WfIsdnBriTimer3Timeouts_Type = Counter32
_WfIsdnBriTimer3Timeouts_Object = MibTableColumn
wfIsdnBriTimer3Timeouts = _WfIsdnBriTimer3Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 31),
    _WfIsdnBriTimer3Timeouts_Type()
)
wfIsdnBriTimer3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTimer3Timeouts.setStatus("mandatory")
_WfIsdnBriTimer4Timeouts_Type = Counter32
_WfIsdnBriTimer4Timeouts_Object = MibTableColumn
wfIsdnBriTimer4Timeouts = _WfIsdnBriTimer4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 32),
    _WfIsdnBriTimer4Timeouts_Type()
)
wfIsdnBriTimer4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriTimer4Timeouts.setStatus("mandatory")


class _WfIsdnBriLineType_Type(Integer32):
    """Custom type wfIsdnBriLineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mtp", 2),
          ("ptp", 1))
    )


_WfIsdnBriLineType_Type.__name__ = "Integer32"
_WfIsdnBriLineType_Object = MibTableColumn
wfIsdnBriLineType = _WfIsdnBriLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 33),
    _WfIsdnBriLineType_Type()
)
wfIsdnBriLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriLineType.setStatus("mandatory")


class _WfIsdnBriMode_Type(Integer32):
    """Custom type wfIsdnBriMode based on Integer32"""
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
        *(("dialup", 1),
          ("floatb", 3),
          ("leased", 2))
    )


_WfIsdnBriMode_Type.__name__ = "Integer32"
_WfIsdnBriMode_Object = MibTableColumn
wfIsdnBriMode = _WfIsdnBriMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 34),
    _WfIsdnBriMode_Type()
)
wfIsdnBriMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriMode.setStatus("mandatory")


class _WfIsdnBriInterfaceType_Type(Integer32):
    """Custom type wfIsdnBriInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isdns", 1),
          ("isdnu", 2))
    )


_WfIsdnBriInterfaceType_Type.__name__ = "Integer32"
_WfIsdnBriInterfaceType_Object = MibTableColumn
wfIsdnBriInterfaceType = _WfIsdnBriInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 35),
    _WfIsdnBriInterfaceType_Type()
)
wfIsdnBriInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriInterfaceType.setStatus("mandatory")


class _WfIsdnBriNtState_Type(Integer32):
    """Custom type wfIsdnBriNtState based on Integer32"""
    defaultValue = 6

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
        *(("activated", 7),
          ("alerting", 2),
          ("deactivated", 6),
          ("error", 9),
          ("fullreset", 1),
          ("pendreceivereset", 10),
          ("receivereset", 3),
          ("synchronized1", 4),
          ("synchronized2", 5),
          ("test", 8))
    )


_WfIsdnBriNtState_Type.__name__ = "Integer32"
_WfIsdnBriNtState_Object = MibTableColumn
wfIsdnBriNtState = _WfIsdnBriNtState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 36),
    _WfIsdnBriNtState_Type()
)
wfIsdnBriNtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBriNtState.setStatus("mandatory")


class _WfIsdnBriTimerM4Tmo_Type(Integer32):
    """Custom type wfIsdnBriTimerM4Tmo based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfIsdnBriTimerM4Tmo_Type.__name__ = "Integer32"
_WfIsdnBriTimerM4Tmo_Object = MibTableColumn
wfIsdnBriTimerM4Tmo = _WfIsdnBriTimerM4Tmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 37),
    _WfIsdnBriTimerM4Tmo_Type()
)
wfIsdnBriTimerM4Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriTimerM4Tmo.setStatus("mandatory")


class _WfIsdnBriTimerM6Tmo_Type(Integer32):
    """Custom type wfIsdnBriTimerM6Tmo based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfIsdnBriTimerM6Tmo_Type.__name__ = "Integer32"
_WfIsdnBriTimerM6Tmo_Object = MibTableColumn
wfIsdnBriTimerM6Tmo = _WfIsdnBriTimerM6Tmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 38),
    _WfIsdnBriTimerM6Tmo_Type()
)
wfIsdnBriTimerM6Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriTimerM6Tmo.setStatus("mandatory")


class _WfIsdnBriX25D_Type(Integer32):
    """Custom type wfIsdnBriX25D based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnBriX25D_Type.__name__ = "Integer32"
_WfIsdnBriX25D_Object = MibTableColumn
wfIsdnBriX25D = _WfIsdnBriX25D_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 39),
    _WfIsdnBriX25D_Type()
)
wfIsdnBriX25D.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriX25D.setStatus("mandatory")


class _WfIsdnBriX25DTeiType_Type(Integer32):
    """Custom type wfIsdnBriX25DTeiType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_WfIsdnBriX25DTeiType_Type.__name__ = "Integer32"
_WfIsdnBriX25DTeiType_Object = MibTableColumn
wfIsdnBriX25DTeiType = _WfIsdnBriX25DTeiType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 40),
    _WfIsdnBriX25DTeiType_Type()
)
wfIsdnBriX25DTeiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriX25DTeiType.setStatus("mandatory")


class _WfIsdnBriX25DTeiValue_Type(Integer32):
    """Custom type wfIsdnBriX25DTeiValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfIsdnBriX25DTeiValue_Type.__name__ = "Integer32"
_WfIsdnBriX25DTeiValue_Object = MibTableColumn
wfIsdnBriX25DTeiValue = _WfIsdnBriX25DTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 9, 1, 41),
    _WfIsdnBriX25DTeiValue_Type()
)
wfIsdnBriX25DTeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBriX25DTeiValue.setStatus("mandatory")
_WfIsdnBChanInterfaceTable_Object = MibTable
wfIsdnBChanInterfaceTable = _WfIsdnBChanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10)
)
if mibBuilder.loadTexts:
    wfIsdnBChanInterfaceTable.setStatus("mandatory")
_WfIsdnBChanInterfaceEntry_Object = MibTableRow
wfIsdnBChanInterfaceEntry = _WfIsdnBChanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1)
)
wfIsdnBChanInterfaceEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnBChanLineNumber"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnBChanIndex"),
)
if mibBuilder.loadTexts:
    wfIsdnBChanInterfaceEntry.setStatus("mandatory")


class _WfIsdnBChanDelete_Type(Integer32):
    """Custom type wfIsdnBChanDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIsdnBChanDelete_Type.__name__ = "Integer32"
_WfIsdnBChanDelete_Object = MibTableColumn
wfIsdnBChanDelete = _WfIsdnBChanDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 1),
    _WfIsdnBChanDelete_Type()
)
wfIsdnBChanDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanDelete.setStatus("mandatory")
_WfIsdnBChanLineNumber_Type = Integer32
_WfIsdnBChanLineNumber_Object = MibTableColumn
wfIsdnBChanLineNumber = _WfIsdnBChanLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 2),
    _WfIsdnBChanLineNumber_Type()
)
wfIsdnBChanLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBChanLineNumber.setStatus("mandatory")


class _WfIsdnBChanIndex_Type(Integer32):
    """Custom type wfIsdnBChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfIsdnBChanIndex_Type.__name__ = "Integer32"
_WfIsdnBChanIndex_Object = MibTableColumn
wfIsdnBChanIndex = _WfIsdnBChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 3),
    _WfIsdnBChanIndex_Type()
)
wfIsdnBChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBChanIndex.setStatus("mandatory")


class _WfIsdnBChanDisable_Type(Integer32):
    """Custom type wfIsdnBChanDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIsdnBChanDisable_Type.__name__ = "Integer32"
_WfIsdnBChanDisable_Object = MibTableColumn
wfIsdnBChanDisable = _WfIsdnBChanDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 4),
    _WfIsdnBChanDisable_Type()
)
wfIsdnBChanDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanDisable.setStatus("mandatory")


class _WfIsdnBChanState_Type(Integer32):
    """Custom type wfIsdnBChanState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIsdnBChanState_Type.__name__ = "Integer32"
_WfIsdnBChanState_Object = MibTableColumn
wfIsdnBChanState = _WfIsdnBChanState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 5),
    _WfIsdnBChanState_Type()
)
wfIsdnBChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBChanState.setStatus("mandatory")


class _WfIsdnBChanCct_Type(Integer32):
    """Custom type wfIsdnBChanCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIsdnBChanCct_Type.__name__ = "Integer32"
_WfIsdnBChanCct_Object = MibTableColumn
wfIsdnBChanCct = _WfIsdnBChanCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 6),
    _WfIsdnBChanCct_Type()
)
wfIsdnBChanCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanCct.setStatus("mandatory")


class _WfIsdnBChanWanProtocol_Type(Integer32):
    """Custom type wfIsdnBChanWanProtocol based on Integer32"""
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
        *(("framerelay", 2),
          ("ppp", 1),
          ("x25", 3))
    )


_WfIsdnBChanWanProtocol_Type.__name__ = "Integer32"
_WfIsdnBChanWanProtocol_Object = MibTableColumn
wfIsdnBChanWanProtocol = _WfIsdnBChanWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 7),
    _WfIsdnBChanWanProtocol_Type()
)
wfIsdnBChanWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanWanProtocol.setStatus("mandatory")


class _WfIsdnBChanBackupPool_Type(Integer32):
    """Custom type wfIsdnBChanBackupPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfIsdnBChanBackupPool_Type.__name__ = "Integer32"
_WfIsdnBChanBackupPool_Object = MibTableColumn
wfIsdnBChanBackupPool = _WfIsdnBChanBackupPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 8),
    _WfIsdnBChanBackupPool_Type()
)
wfIsdnBChanBackupPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanBackupPool.setStatus("mandatory")


class _WfIsdnBChanDemandPool_Type(Integer32):
    """Custom type wfIsdnBChanDemandPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfIsdnBChanDemandPool_Type.__name__ = "Integer32"
_WfIsdnBChanDemandPool_Object = MibTableColumn
wfIsdnBChanDemandPool = _WfIsdnBChanDemandPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 9),
    _WfIsdnBChanDemandPool_Type()
)
wfIsdnBChanDemandPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanDemandPool.setStatus("mandatory")
_WfIsdnBChanDirectoryNum_Type = DisplayString
_WfIsdnBChanDirectoryNum_Object = MibTableColumn
wfIsdnBChanDirectoryNum = _WfIsdnBChanDirectoryNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 10),
    _WfIsdnBChanDirectoryNum_Type()
)
wfIsdnBChanDirectoryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanDirectoryNum.setStatus("mandatory")
_WfIsdnBChanSpid_Type = DisplayString
_WfIsdnBChanSpid_Object = MibTableColumn
wfIsdnBChanSpid = _WfIsdnBChanSpid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 11),
    _WfIsdnBChanSpid_Type()
)
wfIsdnBChanSpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanSpid.setStatus("mandatory")


class _WfIsdnBChanActiveCct_Type(Integer32):
    """Custom type wfIsdnBChanActiveCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIsdnBChanActiveCct_Type.__name__ = "Integer32"
_WfIsdnBChanActiveCct_Object = MibTableColumn
wfIsdnBChanActiveCct = _WfIsdnBChanActiveCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 12),
    _WfIsdnBChanActiveCct_Type()
)
wfIsdnBChanActiveCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnBChanActiveCct.setStatus("mandatory")


class _WfIsdnBChanPriority_Type(Integer32):
    """Custom type wfIsdnBChanPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WfIsdnBChanPriority_Type.__name__ = "Integer32"
_WfIsdnBChanPriority_Object = MibTableColumn
wfIsdnBChanPriority = _WfIsdnBChanPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 13),
    _WfIsdnBChanPriority_Type()
)
wfIsdnBChanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBChanPriority.setStatus("mandatory")


class _WfIsdnBchanMultilineMode_Type(Integer32):
    """Custom type wfIsdnBchanMultilineMode based on Integer32"""
    defaultValue = 1

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
        *(("master", 2),
          ("secondary", 4),
          ("slave", 3),
          ("standard", 1))
    )


_WfIsdnBchanMultilineMode_Type.__name__ = "Integer32"
_WfIsdnBchanMultilineMode_Object = MibTableColumn
wfIsdnBchanMultilineMode = _WfIsdnBchanMultilineMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 10, 1, 14),
    _WfIsdnBchanMultilineMode_Type()
)
wfIsdnBchanMultilineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnBchanMultilineMode.setStatus("mandatory")
_WfIsdnPoolTable_Object = MibTable
wfIsdnPoolTable = _WfIsdnPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11)
)
if mibBuilder.loadTexts:
    wfIsdnPoolTable.setStatus("mandatory")
_WfIsdnPoolEntry_Object = MibTableRow
wfIsdnPoolEntry = _WfIsdnPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1)
)
wfIsdnPoolEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnPoolType"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnPoolLineNumber"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnPoolId"),
)
if mibBuilder.loadTexts:
    wfIsdnPoolEntry.setStatus("mandatory")


class _WfIsdnPoolDelete_Type(Integer32):
    """Custom type wfIsdnPoolDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIsdnPoolDelete_Type.__name__ = "Integer32"
_WfIsdnPoolDelete_Object = MibTableColumn
wfIsdnPoolDelete = _WfIsdnPoolDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 1),
    _WfIsdnPoolDelete_Type()
)
wfIsdnPoolDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnPoolDelete.setStatus("mandatory")


class _WfIsdnPoolType_Type(Integer32):
    """Custom type wfIsdnPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("bandwidth", 3),
          ("demand", 1))
    )


_WfIsdnPoolType_Type.__name__ = "Integer32"
_WfIsdnPoolType_Object = MibTableColumn
wfIsdnPoolType = _WfIsdnPoolType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 2),
    _WfIsdnPoolType_Type()
)
wfIsdnPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnPoolType.setStatus("mandatory")
_WfIsdnPoolLineNumber_Type = Integer32
_WfIsdnPoolLineNumber_Object = MibTableColumn
wfIsdnPoolLineNumber = _WfIsdnPoolLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 3),
    _WfIsdnPoolLineNumber_Type()
)
wfIsdnPoolLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnPoolLineNumber.setStatus("mandatory")
_WfIsdnPoolId_Type = Integer32
_WfIsdnPoolId_Object = MibTableColumn
wfIsdnPoolId = _WfIsdnPoolId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 4),
    _WfIsdnPoolId_Type()
)
wfIsdnPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnPoolId.setStatus("mandatory")


class _WfIsdnPoolChannelCnt_Type(Integer32):
    """Custom type wfIsdnPoolChannelCnt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfIsdnPoolChannelCnt_Type.__name__ = "Integer32"
_WfIsdnPoolChannelCnt_Object = MibTableColumn
wfIsdnPoolChannelCnt = _WfIsdnPoolChannelCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 5),
    _WfIsdnPoolChannelCnt_Type()
)
wfIsdnPoolChannelCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnPoolChannelCnt.setStatus("mandatory")


class _WfIsdnPoolPriority_Type(Integer32):
    """Custom type wfIsdnPoolPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WfIsdnPoolPriority_Type.__name__ = "Integer32"
_WfIsdnPoolPriority_Object = MibTableColumn
wfIsdnPoolPriority = _WfIsdnPoolPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 6),
    _WfIsdnPoolPriority_Type()
)
wfIsdnPoolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnPoolPriority.setStatus("mandatory")
_WfIsdnPoolChannelInUse_Type = Integer32
_WfIsdnPoolChannelInUse_Object = MibTableColumn
wfIsdnPoolChannelInUse = _WfIsdnPoolChannelInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 11, 1, 7),
    _WfIsdnPoolChannelInUse_Type()
)
wfIsdnPoolChannelInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnPoolChannelInUse.setStatus("mandatory")
_WfIsdnLocalPhoneNumTable_Object = MibTable
wfIsdnLocalPhoneNumTable = _WfIsdnLocalPhoneNumTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12)
)
if mibBuilder.loadTexts:
    wfIsdnLocalPhoneNumTable.setStatus("mandatory")
_WfIsdnLocalPhoneNumEntry_Object = MibTableRow
wfIsdnLocalPhoneNumEntry = _WfIsdnLocalPhoneNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1)
)
wfIsdnLocalPhoneNumEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfIsdnLocalPhoneNumLineNum"),
    (0, "Wellfleet-ISDN-MIB", "wfIsdnLocalPhoneNumIndex"),
)
if mibBuilder.loadTexts:
    wfIsdnLocalPhoneNumEntry.setStatus("mandatory")


class _WfIsdnLocalPhoneNumDelete_Type(Integer32):
    """Custom type wfIsdnLocalPhoneNumDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIsdnLocalPhoneNumDelete_Type.__name__ = "Integer32"
_WfIsdnLocalPhoneNumDelete_Object = MibTableColumn
wfIsdnLocalPhoneNumDelete = _WfIsdnLocalPhoneNumDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 1),
    _WfIsdnLocalPhoneNumDelete_Type()
)
wfIsdnLocalPhoneNumDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalPhoneNumDelete.setStatus("mandatory")
_WfIsdnLocalPhoneNumLineNum_Type = Integer32
_WfIsdnLocalPhoneNumLineNum_Object = MibTableColumn
wfIsdnLocalPhoneNumLineNum = _WfIsdnLocalPhoneNumLineNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 2),
    _WfIsdnLocalPhoneNumLineNum_Type()
)
wfIsdnLocalPhoneNumLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnLocalPhoneNumLineNum.setStatus("mandatory")


class _WfIsdnLocalPhoneNumIndex_Type(Integer32):
    """Custom type wfIsdnLocalPhoneNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfIsdnLocalPhoneNumIndex_Type.__name__ = "Integer32"
_WfIsdnLocalPhoneNumIndex_Object = MibTableColumn
wfIsdnLocalPhoneNumIndex = _WfIsdnLocalPhoneNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 3),
    _WfIsdnLocalPhoneNumIndex_Type()
)
wfIsdnLocalPhoneNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnLocalPhoneNumIndex.setStatus("mandatory")
_WfIsdnLocalDirectoryNum_Type = DisplayString
_WfIsdnLocalDirectoryNum_Object = MibTableColumn
wfIsdnLocalDirectoryNum = _WfIsdnLocalDirectoryNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 4),
    _WfIsdnLocalDirectoryNum_Type()
)
wfIsdnLocalDirectoryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalDirectoryNum.setStatus("mandatory")
_WfIsdnLocalSubAddr_Type = DisplayString
_WfIsdnLocalSubAddr_Object = MibTableColumn
wfIsdnLocalSubAddr = _WfIsdnLocalSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 5),
    _WfIsdnLocalSubAddr_Type()
)
wfIsdnLocalSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalSubAddr.setStatus("mandatory")
_WfIsdnLocalSpid_Type = DisplayString
_WfIsdnLocalSpid_Object = MibTableColumn
wfIsdnLocalSpid = _WfIsdnLocalSpid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 6),
    _WfIsdnLocalSpid_Type()
)
wfIsdnLocalSpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalSpid.setStatus("mandatory")


class _WfIsdnLocalAssignedChannel_Type(Integer32):
    """Custom type wfIsdnLocalAssignedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_WfIsdnLocalAssignedChannel_Type.__name__ = "Integer32"
_WfIsdnLocalAssignedChannel_Object = MibTableColumn
wfIsdnLocalAssignedChannel = _WfIsdnLocalAssignedChannel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 7),
    _WfIsdnLocalAssignedChannel_Type()
)
wfIsdnLocalAssignedChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalAssignedChannel.setStatus("mandatory")


class _WfIsdnLocalSpidStatus_Type(Integer32):
    """Custom type wfIsdnLocalSpidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("rejected", 2))
    )


_WfIsdnLocalSpidStatus_Type.__name__ = "Integer32"
_WfIsdnLocalSpidStatus_Object = MibTableColumn
wfIsdnLocalSpidStatus = _WfIsdnLocalSpidStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 8),
    _WfIsdnLocalSpidStatus_Type()
)
wfIsdnLocalSpidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdnLocalSpidStatus.setStatus("mandatory")


class _WfIsdnLocalDirectoryNumType_Type(Integer32):
    """Custom type wfIsdnLocalDirectoryNumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              48,
              64,
              96)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 96),
          ("international", 16),
          ("national", 32),
          ("specific", 48),
          ("subscriber", 64),
          ("unknown", 1))
    )


_WfIsdnLocalDirectoryNumType_Type.__name__ = "Integer32"
_WfIsdnLocalDirectoryNumType_Object = MibTableColumn
wfIsdnLocalDirectoryNumType = _WfIsdnLocalDirectoryNumType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 9),
    _WfIsdnLocalDirectoryNumType_Type()
)
wfIsdnLocalDirectoryNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalDirectoryNumType.setStatus("mandatory")


class _WfIsdnLocalDirectoryNumPlan_Type(Integer32):
    """Custom type wfIsdnLocalDirectoryNumPlan based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              8,
              9,
              16)
        )
    )
    namedValues = NamedValues(
        *(("private", 9),
          ("standard", 8),
          ("telephony", 1),
          ("telex", 4),
          ("unknown", 16),
          ("x121", 3))
    )


_WfIsdnLocalDirectoryNumPlan_Type.__name__ = "Integer32"
_WfIsdnLocalDirectoryNumPlan_Object = MibTableColumn
wfIsdnLocalDirectoryNumPlan = _WfIsdnLocalDirectoryNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 10),
    _WfIsdnLocalDirectoryNumPlan_Type()
)
wfIsdnLocalDirectoryNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnLocalDirectoryNumPlan.setStatus("mandatory")


class _WfIsdnSpidRetries_Type(Integer32):
    """Custom type wfIsdnSpidRetries based on Integer32"""
    defaultValue = 20


_WfIsdnSpidRetries_Object = MibTableColumn
wfIsdnSpidRetries = _WfIsdnSpidRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 11),
    _WfIsdnSpidRetries_Type()
)
wfIsdnSpidRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSpidRetries.setStatus("mandatory")


class _WfIsdnSpidRetryAttempts_Type(Integer32):
    """Custom type wfIsdnSpidRetryAttempts based on Integer32"""
    defaultValue = 0


_WfIsdnSpidRetryAttempts_Object = MibTableColumn
wfIsdnSpidRetryAttempts = _WfIsdnSpidRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 12),
    _WfIsdnSpidRetryAttempts_Type()
)
wfIsdnSpidRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSpidRetryAttempts.setStatus("mandatory")


class _WfIsdnSpidRetryTimer_Type(Integer32):
    """Custom type wfIsdnSpidRetryTimer based on Integer32"""
    defaultValue = 60


_WfIsdnSpidRetryTimer_Object = MibTableColumn
wfIsdnSpidRetryTimer = _WfIsdnSpidRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 13),
    _WfIsdnSpidRetryTimer_Type()
)
wfIsdnSpidRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSpidRetryTimer.setStatus("mandatory")


class _WfIsdnSpidResetBri_Type(Integer32):
    """Custom type wfIsdnSpidResetBri based on Integer32"""
    defaultValue = 0


_WfIsdnSpidResetBri_Object = MibTableColumn
wfIsdnSpidResetBri = _WfIsdnSpidResetBri_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 12, 1, 14),
    _WfIsdnSpidResetBri_Type()
)
wfIsdnSpidResetBri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdnSpidResetBri.setStatus("mandatory")
_WfModemCommandTable_Object = MibTable
wfModemCommandTable = _WfModemCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13)
)
if mibBuilder.loadTexts:
    wfModemCommandTable.setStatus("mandatory")
_WfModemCommandEntry_Object = MibTableRow
wfModemCommandEntry = _WfModemCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13, 1)
)
wfModemCommandEntry.setIndexNames(
    (0, "Wellfleet-ISDN-MIB", "wfModemCommandSlot"),
    (0, "Wellfleet-ISDN-MIB", "wfModemCommandConnector"),
)
if mibBuilder.loadTexts:
    wfModemCommandEntry.setStatus("mandatory")


class _WfModemCommandDelete_Type(Integer32):
    """Custom type wfModemCommandDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfModemCommandDelete_Type.__name__ = "Integer32"
_WfModemCommandDelete_Object = MibTableColumn
wfModemCommandDelete = _WfModemCommandDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13, 1, 1),
    _WfModemCommandDelete_Type()
)
wfModemCommandDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCommandDelete.setStatus("mandatory")


class _WfModemCommandSlot_Type(Integer32):
    """Custom type wfModemCommandSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfModemCommandSlot_Type.__name__ = "Integer32"
_WfModemCommandSlot_Object = MibTableColumn
wfModemCommandSlot = _WfModemCommandSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13, 1, 2),
    _WfModemCommandSlot_Type()
)
wfModemCommandSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemCommandSlot.setStatus("mandatory")


class _WfModemCommandConnector_Type(Integer32):
    """Custom type wfModemCommandConnector based on Integer32"""
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
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WfModemCommandConnector_Type.__name__ = "Integer32"
_WfModemCommandConnector_Object = MibTableColumn
wfModemCommandConnector = _WfModemCommandConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13, 1, 3),
    _WfModemCommandConnector_Type()
)
wfModemCommandConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemCommandConnector.setStatus("mandatory")
_WfModemCommandString_Type = DisplayString
_WfModemCommandString_Object = MibTableColumn
wfModemCommandString = _WfModemCommandString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8, 13, 1, 4),
    _WfModemCommandString_Type()
)
wfModemCommandString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCommandString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ISDN-MIB",
    **{"wfModemIfTable": wfModemIfTable,
       "wfModemIfEntry": wfModemIfEntry,
       "wfModemIfDelete": wfModemIfDelete,
       "wfModemIfSlot": wfModemIfSlot,
       "wfModemIfConnectStatus": wfModemIfConnectStatus,
       "wfModemIfConnector": wfModemIfConnector,
       "wfModemIfCct": wfModemIfCct,
       "wfModemIfConnectWhen": wfModemIfConnectWhen,
       "wfModemIfConnectionTime": wfModemIfConnectionTime,
       "wfModemIfMinDurationTime": wfModemIfMinDurationTime,
       "wfModemIfInactivityTime": wfModemIfInactivityTime,
       "wfModemIfRetryDelayTime": wfModemIfRetryDelayTime,
       "wfModemIfLineBandwidth": wfModemIfLineBandwidth,
       "wfModemIfChanAggrMax": wfModemIfChanAggrMax,
       "wfModemIfChanAggrMin": wfModemIfChanAggrMin,
       "wfModemIfChanMgmt": wfModemIfChanMgmt,
       "wfModemIfRestrictType": wfModemIfRestrictType,
       "wfModemIfDialRetryCount": wfModemIfDialRetryCount,
       "wfModemIfRetries": wfModemIfRetries,
       "wfModemIfForceDial": wfModemIfForceDial,
       "wfModemIfForceHangup": wfModemIfForceHangup,
       "wfModemIfBringUpHour": wfModemIfBringUpHour,
       "wfModemIfBringUpMinute": wfModemIfBringUpMinute,
       "wfModemIfTakeDownHour": wfModemIfTakeDownHour,
       "wfModemIfTakeDownMinute": wfModemIfTakeDownMinute,
       "wfModemIfConnectRmtStationNum": wfModemIfConnectRmtStationNum,
       "wfModemIfConnectSubAddr": wfModemIfConnectSubAddr,
       "wfModemIfMediaType": wfModemIfMediaType,
       "wfModemIfUpperLayerTimeOut": wfModemIfUpperLayerTimeOut,
       "wfModemIfRingIndicator": wfModemIfRingIndicator,
       "wfModemIfFsmDebug": wfModemIfFsmDebug,
       "wfIsdnMsgCtrTable": wfIsdnMsgCtrTable,
       "wfIsdnMsgCtrEntry": wfIsdnMsgCtrEntry,
       "wfIsdnMsgCtrSlot": wfIsdnMsgCtrSlot,
       "wfIsdnMsgCtrDslID": wfIsdnMsgCtrDslID,
       "wfIsdnMsgCallProcInd": wfIsdnMsgCallProcInd,
       "wfIsdnMsgClearConf": wfIsdnMsgClearConf,
       "wfIsdnMsgClearInd": wfIsdnMsgClearInd,
       "wfIsdnMsgConnectInd": wfIsdnMsgConnectInd,
       "wfIsdnMsgSetupInd": wfIsdnMsgSetupInd,
       "wfIsdnMsgRegisterConf": wfIsdnMsgRegisterConf,
       "wfIsdnMsgMgmtInd": wfIsdnMsgMgmtInd,
       "wfIsdnMsgDiscInd": wfIsdnMsgDiscInd,
       "wfIsdnMsgActInd": wfIsdnMsgActInd,
       "wfIsdnMsgDeactInd": wfIsdnMsgDeactInd,
       "wfIsdnMsgConnectConf": wfIsdnMsgConnectConf,
       "wfIsdnMsgAlertReq": wfIsdnMsgAlertReq,
       "wfIsdnMsgCallProcReq": wfIsdnMsgCallProcReq,
       "wfIsdnMsgClearReq": wfIsdnMsgClearReq,
       "wfIsdnMsgConnectReq": wfIsdnMsgConnectReq,
       "wfIsdnMsgSetupReq": wfIsdnMsgSetupReq,
       "wfIsdnMsgMgmtReq": wfIsdnMsgMgmtReq,
       "wfIsdnMsgDiscReq": wfIsdnMsgDiscReq,
       "wfIsdnMsgActReq": wfIsdnMsgActReq,
       "wfIsdnMsgDeactReq": wfIsdnMsgDeactReq,
       "wfIsdnMsgAlertInd": wfIsdnMsgAlertInd,
       "wfIsdnMsgInfoInd": wfIsdnMsgInfoInd,
       "wfIsdnHostActionTable": wfIsdnHostActionTable,
       "wfIsdnHostActionEntry": wfIsdnHostActionEntry,
       "wfIsdnHostActSlot": wfIsdnHostActSlot,
       "wfIsdnHostActDslId": wfIsdnHostActDslId,
       "wfIsdnHostActCallID": wfIsdnHostActCallID,
       "wfIsdnHostActMsgType": wfIsdnHostActMsgType,
       "wfIsdnHostActCalledPtyType": wfIsdnHostActCalledPtyType,
       "wfIsdnHostActCalledPtyPlan": wfIsdnHostActCalledPtyPlan,
       "wfIsdnHostActCalledPtyNum": wfIsdnHostActCalledPtyNum,
       "wfIsdnHostActCallingPtyType": wfIsdnHostActCallingPtyType,
       "wfIsdnHostActCallingPtyPlan": wfIsdnHostActCallingPtyPlan,
       "wfIsdnHostActCallingPtyNum": wfIsdnHostActCallingPtyNum,
       "wfIsdnHostActCallingPtyPres": wfIsdnHostActCallingPtyPres,
       "wfIsdnHostActChanPrefBit": wfIsdnHostActChanPrefBit,
       "wfIsdnHostActChanSelection": wfIsdnHostActChanSelection,
       "wfIsdnHostActCauseCode": wfIsdnHostActCauseCode,
       "wfIsdnHostActTransferCap": wfIsdnHostActTransferCap,
       "wfIsdnHostActCldSadType": wfIsdnHostActCldSadType,
       "wfIsdnHostActCldSadNum": wfIsdnHostActCldSadNum,
       "wfIsdnHostActClgSadType": wfIsdnHostActClgSadType,
       "wfIsdnHostActClgSadNum": wfIsdnHostActClgSadNum,
       "wfIsdnHostActCldSadPres": wfIsdnHostActCldSadPres,
       "wfIsdnHostActClgSadPres": wfIsdnHostActClgSadPres,
       "wfIsdnSwitchCfgTable": wfIsdnSwitchCfgTable,
       "wfIsdnSwitchCfgEntry": wfIsdnSwitchCfgEntry,
       "wfIsdnSwitchCfgDelete": wfIsdnSwitchCfgDelete,
       "wfIsdnSwitchCfgSlot": wfIsdnSwitchCfgSlot,
       "wfIsdnSwitchCfgType": wfIsdnSwitchCfgType,
       "wfIsdnSwitchTestMode": wfIsdnSwitchTestMode,
       "wfIsdnSwitchIncomingFilter": wfIsdnSwitchIncomingFilter,
       "wfIsdnSwitchTraceFacility": wfIsdnSwitchTraceFacility,
       "wfIsdnSwitchScreenedCalls": wfIsdnSwitchScreenedCalls,
       "wfIsdnSwitchSendingComplete": wfIsdnSwitchSendingComplete,
       "wfIsdnSwitchGlobalRateAdaption": wfIsdnSwitchGlobalRateAdaption,
       "wfIsdnSwitchX25D": wfIsdnSwitchX25D,
       "wfIsdnSwitchAllowedScreeningBits": wfIsdnSwitchAllowedScreeningBits,
       "wfIsdnSwitchPreauthTodCheck": wfIsdnSwitchPreauthTodCheck,
       "wfIsdnCallInfoTable": wfIsdnCallInfoTable,
       "wfIsdnCallInfoEntry": wfIsdnCallInfoEntry,
       "wfIsdnCallInfoSlot": wfIsdnCallInfoSlot,
       "wfIsdnCallInfoDslID": wfIsdnCallInfoDslID,
       "wfIsdnCallInfoCallID": wfIsdnCallInfoCallID,
       "wfIsdnCallInfoBChannel": wfIsdnCallInfoBChannel,
       "wfIsdnCallInfoCallState": wfIsdnCallInfoCallState,
       "wfIsdnCallInfoTransferCap": wfIsdnCallInfoTransferCap,
       "wfIsdnCallInfoCalledPtyNum": wfIsdnCallInfoCalledPtyNum,
       "wfIsdnCallInfoCallingPtyNum": wfIsdnCallInfoCallingPtyNum,
       "wfIsdnCallInfoDuration": wfIsdnCallInfoDuration,
       "wfIsdnCallInfoConnectTime": wfIsdnCallInfoConnectTime,
       "wfIsdnCallInfoRateAdaption": wfIsdnCallInfoRateAdaption,
       "wfIsdnCallInfoCalledPtySub": wfIsdnCallInfoCalledPtySub,
       "wfIsdnCallInfoCallingPtySub": wfIsdnCallInfoCallingPtySub,
       "wfIsdnCallInfoChanType": wfIsdnCallInfoChanType,
       "wfIsdnCallInfoAggrChanCnt": wfIsdnCallInfoAggrChanCnt,
       "wfIsdnCallInfoTimeslotMask": wfIsdnCallInfoTimeslotMask,
       "wfIsdnCallInfoCct": wfIsdnCallInfoCct,
       "wfIsdnBriInterfaceTable": wfIsdnBriInterfaceTable,
       "wfIsdnBriInterfaceEntry": wfIsdnBriInterfaceEntry,
       "wfIsdnBriDelete": wfIsdnBriDelete,
       "wfIsdnBriDisable": wfIsdnBriDisable,
       "wfIsdnBriState": wfIsdnBriState,
       "wfIsdnBriSlot": wfIsdnBriSlot,
       "wfIsdnBriConnector": wfIsdnBriConnector,
       "wfIsdnBriCct": wfIsdnBriCct,
       "wfIsdnBriDslId": wfIsdnBriDslId,
       "wfIsdnBriLineNumber": wfIsdnBriLineNumber,
       "wfIsdnBriModule": wfIsdnBriModule,
       "wfIsdnBriActualConnector": wfIsdnBriActualConnector,
       "wfIsdnBriTeState": wfIsdnBriTeState,
       "wfIsdnBriMtu": wfIsdnBriMtu,
       "wfIsdnBriBChanLoop": wfIsdnBriBChanLoop,
       "wfIsdnBriTimer3Tmo": wfIsdnBriTimer3Tmo,
       "wfIsdnBriTimer4Tmo": wfIsdnBriTimer4Tmo,
       "wfIsdnBriRxOctets": wfIsdnBriRxOctets,
       "wfIsdnBriRxFrames": wfIsdnBriRxFrames,
       "wfIsdnBriTxOctets": wfIsdnBriTxOctets,
       "wfIsdnBriTxFrames": wfIsdnBriTxFrames,
       "wfIsdnBriRxErrors": wfIsdnBriRxErrors,
       "wfIsdnBriTxErrors": wfIsdnBriTxErrors,
       "wfIsdnBriRxLackRescs": wfIsdnBriRxLackRescs,
       "wfIsdnBriTxLackRescs": wfIsdnBriTxLackRescs,
       "wfIsdnBriTxUnderFlows": wfIsdnBriTxUnderFlows,
       "wfIsdnBriTxDChanCollisions": wfIsdnBriTxDChanCollisions,
       "wfIsdnBriRxOverFlows": wfIsdnBriRxOverFlows,
       "wfIsdnBriRxTooLongFrames": wfIsdnBriRxTooLongFrames,
       "wfIsdnBriRxBadCrcs": wfIsdnBriRxBadCrcs,
       "wfIsdnBriRxAborts": wfIsdnBriRxAborts,
       "wfIsdnBriRxReplenMisses": wfIsdnBriRxReplenMisses,
       "wfIsdnBriTimer3Timeouts": wfIsdnBriTimer3Timeouts,
       "wfIsdnBriTimer4Timeouts": wfIsdnBriTimer4Timeouts,
       "wfIsdnBriLineType": wfIsdnBriLineType,
       "wfIsdnBriMode": wfIsdnBriMode,
       "wfIsdnBriInterfaceType": wfIsdnBriInterfaceType,
       "wfIsdnBriNtState": wfIsdnBriNtState,
       "wfIsdnBriTimerM4Tmo": wfIsdnBriTimerM4Tmo,
       "wfIsdnBriTimerM6Tmo": wfIsdnBriTimerM6Tmo,
       "wfIsdnBriX25D": wfIsdnBriX25D,
       "wfIsdnBriX25DTeiType": wfIsdnBriX25DTeiType,
       "wfIsdnBriX25DTeiValue": wfIsdnBriX25DTeiValue,
       "wfIsdnBChanInterfaceTable": wfIsdnBChanInterfaceTable,
       "wfIsdnBChanInterfaceEntry": wfIsdnBChanInterfaceEntry,
       "wfIsdnBChanDelete": wfIsdnBChanDelete,
       "wfIsdnBChanLineNumber": wfIsdnBChanLineNumber,
       "wfIsdnBChanIndex": wfIsdnBChanIndex,
       "wfIsdnBChanDisable": wfIsdnBChanDisable,
       "wfIsdnBChanState": wfIsdnBChanState,
       "wfIsdnBChanCct": wfIsdnBChanCct,
       "wfIsdnBChanWanProtocol": wfIsdnBChanWanProtocol,
       "wfIsdnBChanBackupPool": wfIsdnBChanBackupPool,
       "wfIsdnBChanDemandPool": wfIsdnBChanDemandPool,
       "wfIsdnBChanDirectoryNum": wfIsdnBChanDirectoryNum,
       "wfIsdnBChanSpid": wfIsdnBChanSpid,
       "wfIsdnBChanActiveCct": wfIsdnBChanActiveCct,
       "wfIsdnBChanPriority": wfIsdnBChanPriority,
       "wfIsdnBchanMultilineMode": wfIsdnBchanMultilineMode,
       "wfIsdnPoolTable": wfIsdnPoolTable,
       "wfIsdnPoolEntry": wfIsdnPoolEntry,
       "wfIsdnPoolDelete": wfIsdnPoolDelete,
       "wfIsdnPoolType": wfIsdnPoolType,
       "wfIsdnPoolLineNumber": wfIsdnPoolLineNumber,
       "wfIsdnPoolId": wfIsdnPoolId,
       "wfIsdnPoolChannelCnt": wfIsdnPoolChannelCnt,
       "wfIsdnPoolPriority": wfIsdnPoolPriority,
       "wfIsdnPoolChannelInUse": wfIsdnPoolChannelInUse,
       "wfIsdnLocalPhoneNumTable": wfIsdnLocalPhoneNumTable,
       "wfIsdnLocalPhoneNumEntry": wfIsdnLocalPhoneNumEntry,
       "wfIsdnLocalPhoneNumDelete": wfIsdnLocalPhoneNumDelete,
       "wfIsdnLocalPhoneNumLineNum": wfIsdnLocalPhoneNumLineNum,
       "wfIsdnLocalPhoneNumIndex": wfIsdnLocalPhoneNumIndex,
       "wfIsdnLocalDirectoryNum": wfIsdnLocalDirectoryNum,
       "wfIsdnLocalSubAddr": wfIsdnLocalSubAddr,
       "wfIsdnLocalSpid": wfIsdnLocalSpid,
       "wfIsdnLocalAssignedChannel": wfIsdnLocalAssignedChannel,
       "wfIsdnLocalSpidStatus": wfIsdnLocalSpidStatus,
       "wfIsdnLocalDirectoryNumType": wfIsdnLocalDirectoryNumType,
       "wfIsdnLocalDirectoryNumPlan": wfIsdnLocalDirectoryNumPlan,
       "wfIsdnSpidRetries": wfIsdnSpidRetries,
       "wfIsdnSpidRetryAttempts": wfIsdnSpidRetryAttempts,
       "wfIsdnSpidRetryTimer": wfIsdnSpidRetryTimer,
       "wfIsdnSpidResetBri": wfIsdnSpidResetBri,
       "wfModemCommandTable": wfModemCommandTable,
       "wfModemCommandEntry": wfModemCommandEntry,
       "wfModemCommandDelete": wfModemCommandDelete,
       "wfModemCommandSlot": wfModemCommandSlot,
       "wfModemCommandConnector": wfModemCommandConnector,
       "wfModemCommandString": wfModemCommandString}
)
