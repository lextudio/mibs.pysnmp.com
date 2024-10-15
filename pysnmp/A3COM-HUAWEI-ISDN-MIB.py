# SNMP MIB module (A3COM-HUAWEI-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:13 2024
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

(mlsr,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "mlsr")

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

hwIsdnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwIsdnMibObjects_ObjectIdentity = ObjectIdentity
hwIsdnMibObjects = _HwIsdnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1)
)
_IsdnChannelB_ObjectIdentity = ObjectIdentity
isdnChannelB = _IsdnChannelB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1)
)
_HwChanbIsdnTable_Object = MibTable
hwChanbIsdnTable = _HwChanbIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwChanbIsdnTable.setStatus("current")
_HwChanbIsdnEntry_Object = MibTableRow
hwChanbIsdnEntry = _HwChanbIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1)
)
hwChanbIsdnEntry.setIndexNames(
    (0, "A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnIf"),
)
if mibBuilder.loadTexts:
    hwChanbIsdnEntry.setStatus("current")
_HwChanbIsdnIf_Type = Integer32
_HwChanbIsdnIf_Object = MibTableColumn
hwChanbIsdnIf = _HwChanbIsdnIf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 1),
    _HwChanbIsdnIf_Type()
)
hwChanbIsdnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnIf.setStatus("current")


class _HwChanbIsdnPermit_Type(Integer32):
    """Custom type hwChanbIsdnPermit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callBidirection", 3),
          ("callIn", 2),
          ("callOut", 1))
    )


_HwChanbIsdnPermit_Type.__name__ = "Integer32"
_HwChanbIsdnPermit_Object = MibTableColumn
hwChanbIsdnPermit = _HwChanbIsdnPermit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 2),
    _HwChanbIsdnPermit_Type()
)
hwChanbIsdnPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnPermit.setStatus("current")
_HwChanbIsdnAddr_Type = DisplayString
_HwChanbIsdnAddr_Object = MibTableColumn
hwChanbIsdnAddr = _HwChanbIsdnAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 3),
    _HwChanbIsdnAddr_Type()
)
hwChanbIsdnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnAddr.setStatus("current")
_HwChanbIsdnCallerAddr_Type = DisplayString
_HwChanbIsdnCallerAddr_Object = MibTableColumn
hwChanbIsdnCallerAddr = _HwChanbIsdnCallerAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 4),
    _HwChanbIsdnCallerAddr_Type()
)
hwChanbIsdnCallerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallerAddr.setStatus("current")


class _HwChanbIsdnCallType_Type(Integer32):
    """Custom type hwChanbIsdnCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("call", 1),
          ("nocall", 0))
    )


_HwChanbIsdnCallType_Type.__name__ = "Integer32"
_HwChanbIsdnCallType_Object = MibTableColumn
hwChanbIsdnCallType = _HwChanbIsdnCallType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 5),
    _HwChanbIsdnCallType_Type()
)
hwChanbIsdnCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallType.setStatus("current")


class _HwChanbIsdnInfoType_Type(Integer32):
    """Custom type hwChanbIsdnInfoType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("restrictDigit", 5),
          ("speech", 2),
          ("swithchedPacket", 9),
          ("unknown", 1),
          ("unrestrDigit", 3),
          ("unrestrDigit56", 4),
          ("video", 8))
    )


_HwChanbIsdnInfoType_Type.__name__ = "Integer32"
_HwChanbIsdnInfoType_Object = MibTableColumn
hwChanbIsdnInfoType = _HwChanbIsdnInfoType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 6),
    _HwChanbIsdnInfoType_Type()
)
hwChanbIsdnInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnInfoType.setStatus("current")


class _HwChanbIsdnState_Type(Integer32):
    """Custom type hwChanbIsdnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connecting", 2),
          ("idle", 1))
    )


_HwChanbIsdnState_Type.__name__ = "Integer32"
_HwChanbIsdnState_Object = MibTableColumn
hwChanbIsdnState = _HwChanbIsdnState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 7),
    _HwChanbIsdnState_Type()
)
hwChanbIsdnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnState.setStatus("current")
_HwChanbIsdnCallFreeReason_Type = DisplayString
_HwChanbIsdnCallFreeReason_Object = MibTableColumn
hwChanbIsdnCallFreeReason = _HwChanbIsdnCallFreeReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 8),
    _HwChanbIsdnCallFreeReason_Type()
)
hwChanbIsdnCallFreeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallFreeReason.setStatus("current")
_HwChanbIsdnCallFreeCode_Type = Integer32
_HwChanbIsdnCallFreeCode_Object = MibTableColumn
hwChanbIsdnCallFreeCode = _HwChanbIsdnCallFreeCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 9),
    _HwChanbIsdnCallFreeCode_Type()
)
hwChanbIsdnCallFreeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallFreeCode.setStatus("current")
_HwChanbIsdnCallAccept_Type = Counter32
_HwChanbIsdnCallAccept_Object = MibTableColumn
hwChanbIsdnCallAccept = _HwChanbIsdnCallAccept_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 10),
    _HwChanbIsdnCallAccept_Type()
)
hwChanbIsdnCallAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallAccept.setStatus("current")
_HwChanbIsdnCallReject_Type = Counter32
_HwChanbIsdnCallReject_Object = MibTableColumn
hwChanbIsdnCallReject = _HwChanbIsdnCallReject_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 11),
    _HwChanbIsdnCallReject_Type()
)
hwChanbIsdnCallReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallReject.setStatus("current")
_HwChanbIsdnCallSuccess_Type = Counter32
_HwChanbIsdnCallSuccess_Object = MibTableColumn
hwChanbIsdnCallSuccess = _HwChanbIsdnCallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 12),
    _HwChanbIsdnCallSuccess_Type()
)
hwChanbIsdnCallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallSuccess.setStatus("current")
_HwChanbIsdnCallFailure_Type = Counter32
_HwChanbIsdnCallFailure_Object = MibTableColumn
hwChanbIsdnCallFailure = _HwChanbIsdnCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 13),
    _HwChanbIsdnCallFailure_Type()
)
hwChanbIsdnCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnCallFailure.setStatus("current")


class _HwChanbIsdnMaxKeepTime_Type(Integer32):
    """Custom type hwChanbIsdnMaxKeepTime based on Integer32"""
    defaultValue = 2147483647


_HwChanbIsdnMaxKeepTime_Object = MibTableColumn
hwChanbIsdnMaxKeepTime = _HwChanbIsdnMaxKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 14),
    _HwChanbIsdnMaxKeepTime_Type()
)
hwChanbIsdnMaxKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnMaxKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    hwChanbIsdnMaxKeepTime.setUnits("milliseconds")
_HwChanbIsdnLastKeepTime_Type = Integer32
_HwChanbIsdnLastKeepTime_Object = MibTableColumn
hwChanbIsdnLastKeepTime = _HwChanbIsdnLastKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 15),
    _HwChanbIsdnLastKeepTime_Type()
)
hwChanbIsdnLastKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnLastKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    hwChanbIsdnLastKeepTime.setUnits("milliseconds")
_HwChanbIsdnLastCallTime_Type = TimeStamp
_HwChanbIsdnLastCallTime_Object = MibTableColumn
hwChanbIsdnLastCallTime = _HwChanbIsdnLastCallTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 1, 1, 16),
    _HwChanbIsdnLastCallTime_Type()
)
hwChanbIsdnLastCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChanbIsdnLastCallTime.setStatus("current")


class _HwChanbTrapEnable_Type(Integer32):
    """Custom type hwChanbTrapEnable based on Integer32"""
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


_HwChanbTrapEnable_Type.__name__ = "Integer32"
_HwChanbTrapEnable_Object = MibScalar
hwChanbTrapEnable = _HwChanbTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 1, 2),
    _HwChanbTrapEnable_Type()
)
hwChanbTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwChanbTrapEnable.setStatus("current")
_IsdnQ931_ObjectIdentity = ObjectIdentity
isdnQ931 = _IsdnQ931_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2)
)
_HwQ931IsdnControl_ObjectIdentity = ObjectIdentity
hwQ931IsdnControl = _HwQ931IsdnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 1)
)


class _HwQ931CallSetupTrapEnable_Type(Integer32):
    """Custom type hwQ931CallSetupTrapEnable based on Integer32"""
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


_HwQ931CallSetupTrapEnable_Type.__name__ = "Integer32"
_HwQ931CallSetupTrapEnable_Object = MibScalar
hwQ931CallSetupTrapEnable = _HwQ931CallSetupTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 1, 1),
    _HwQ931CallSetupTrapEnable_Type()
)
hwQ931CallSetupTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQ931CallSetupTrapEnable.setStatus("current")


class _HwQ931CallClearTrapEnable_Type(Integer32):
    """Custom type hwQ931CallClearTrapEnable based on Integer32"""
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


_HwQ931CallClearTrapEnable_Type.__name__ = "Integer32"
_HwQ931CallClearTrapEnable_Object = MibScalar
hwQ931CallClearTrapEnable = _HwQ931CallClearTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 1, 2),
    _HwQ931CallClearTrapEnable_Type()
)
hwQ931CallClearTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQ931CallClearTrapEnable.setStatus("current")
_HwQ931IsdnTable_Object = MibTable
hwQ931IsdnTable = _HwQ931IsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwQ931IsdnTable.setStatus("current")
_HwQ931IsdnEntry_Object = MibTableRow
hwQ931IsdnEntry = _HwQ931IsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1)
)
hwQ931IsdnEntry.setIndexNames(
    (0, "A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnOpIndex"),
)
if mibBuilder.loadTexts:
    hwQ931IsdnEntry.setStatus("current")
_HwQ931IsdnOpIndex_Type = Integer32
_HwQ931IsdnOpIndex_Object = MibTableColumn
hwQ931IsdnOpIndex = _HwQ931IsdnOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 1),
    _HwQ931IsdnOpIndex_Type()
)
hwQ931IsdnOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwQ931IsdnOpIndex.setStatus("current")
_HwQ931IsdnLastCalled_Type = DisplayString
_HwQ931IsdnLastCalled_Object = MibTableColumn
hwQ931IsdnLastCalled = _HwQ931IsdnLastCalled_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 2),
    _HwQ931IsdnLastCalled_Type()
)
hwQ931IsdnLastCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnLastCalled.setStatus("current")
_HwQ931IsdnLastCalling_Type = DisplayString
_HwQ931IsdnLastCalling_Object = MibTableColumn
hwQ931IsdnLastCalling = _HwQ931IsdnLastCalling_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 3),
    _HwQ931IsdnLastCalling_Type()
)
hwQ931IsdnLastCalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnLastCalling.setStatus("current")


class _HwQ931IsdnLastCauseDisc_Type(Integer32):
    """Custom type hwQ931IsdnLastCauseDisc based on Integer32"""
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
        *(("netOutofOrder", 6),
          ("noRouteToDest", 4),
          ("noRouteToTransNet", 3),
          ("normCallClr", 2),
          ("switchEquCongest", 5),
          ("unknown", 1))
    )


_HwQ931IsdnLastCauseDisc_Type.__name__ = "Integer32"
_HwQ931IsdnLastCauseDisc_Object = MibTableColumn
hwQ931IsdnLastCauseDisc = _HwQ931IsdnLastCauseDisc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 4),
    _HwQ931IsdnLastCauseDisc_Type()
)
hwQ931IsdnLastCauseDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnLastCauseDisc.setStatus("current")


class _HwQ931IsdnCallDirection_Type(Integer32):
    """Custom type hwQ931IsdnCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_HwQ931IsdnCallDirection_Type.__name__ = "Integer32"
_HwQ931IsdnCallDirection_Object = MibTableColumn
hwQ931IsdnCallDirection = _HwQ931IsdnCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 5),
    _HwQ931IsdnCallDirection_Type()
)
hwQ931IsdnCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnCallDirection.setStatus("current")
_HwQ931IsdnCallTimeOpen_Type = DateAndTime
_HwQ931IsdnCallTimeOpen_Object = MibTableColumn
hwQ931IsdnCallTimeOpen = _HwQ931IsdnCallTimeOpen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 6),
    _HwQ931IsdnCallTimeOpen_Type()
)
hwQ931IsdnCallTimeOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnCallTimeOpen.setStatus("current")
_HwQ931IsdnCallTimeClose_Type = DateAndTime
_HwQ931IsdnCallTimeClose_Object = MibTableColumn
hwQ931IsdnCallTimeClose = _HwQ931IsdnCallTimeClose_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 2, 2, 1, 7),
    _HwQ931IsdnCallTimeClose_Type()
)
hwQ931IsdnCallTimeClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQ931IsdnCallTimeClose.setStatus("current")
_HwIsdnLapd_ObjectIdentity = ObjectIdentity
hwIsdnLapd = _HwIsdnLapd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3)
)
_HwLapdIsdnTable_Object = MibTable
hwLapdIsdnTable = _HwLapdIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwLapdIsdnTable.setStatus("current")
_HwLapdIsdnEntry_Object = MibTableRow
hwLapdIsdnEntry = _HwLapdIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1, 1)
)
hwLapdIsdnEntry.setIndexNames(
    (0, "A3COM-HUAWEI-ISDN-MIB", "hwLapdIsdnIf"),
)
if mibBuilder.loadTexts:
    hwLapdIsdnEntry.setStatus("current")
_HwLapdIsdnIf_Type = Integer32
_HwLapdIsdnIf_Object = MibTableColumn
hwLapdIsdnIf = _HwLapdIsdnIf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1, 1, 1),
    _HwLapdIsdnIf_Type()
)
hwLapdIsdnIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLapdIsdnIf.setStatus("current")


class _HwLapdIsdnProtocol_Type(Integer32):
    """Custom type hwLapdIsdnProtocol based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 5),
          ("att", 8),
          ("dss1", 1),
          ("ess5", 4),
          ("etsi", 3),
          ("ni", 9),
          ("ni2", 6),
          ("ntt", 7),
          ("qsig", 2))
    )


_HwLapdIsdnProtocol_Type.__name__ = "Integer32"
_HwLapdIsdnProtocol_Object = MibTableColumn
hwLapdIsdnProtocol = _HwLapdIsdnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1, 1, 2),
    _HwLapdIsdnProtocol_Type()
)
hwLapdIsdnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLapdIsdnProtocol.setStatus("current")


class _HwLapdIsdnIfMode_Type(Integer32):
    """Custom type hwLapdIsdnIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 2),
          ("userSide", 1))
    )


_HwLapdIsdnIfMode_Type.__name__ = "Integer32"
_HwLapdIsdnIfMode_Object = MibTableColumn
hwLapdIsdnIfMode = _HwLapdIsdnIfMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1, 1, 3),
    _HwLapdIsdnIfMode_Type()
)
hwLapdIsdnIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLapdIsdnIfMode.setStatus("current")


class _HwLapdIsdnLinkStatus_Type(Integer32):
    """Custom type hwLapdIsdnLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("l1Active", 2),
          ("l2Active", 3))
    )


_HwLapdIsdnLinkStatus_Type.__name__ = "Integer32"
_HwLapdIsdnLinkStatus_Object = MibTableColumn
hwLapdIsdnLinkStatus = _HwLapdIsdnLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 1, 1, 4),
    _HwLapdIsdnLinkStatus_Type()
)
hwLapdIsdnLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLapdIsdnLinkStatus.setStatus("current")
_HwLapdIsdnControl_ObjectIdentity = ObjectIdentity
hwLapdIsdnControl = _HwLapdIsdnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 2)
)


class _HwLapdStatusTrapEnable_Type(Integer32):
    """Custom type hwLapdStatusTrapEnable based on Integer32"""
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


_HwLapdStatusTrapEnable_Type.__name__ = "Integer32"
_HwLapdStatusTrapEnable_Object = MibScalar
hwLapdStatusTrapEnable = _HwLapdStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 1, 3, 2, 1),
    _HwLapdStatusTrapEnable_Type()
)
hwLapdStatusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLapdStatusTrapEnable.setStatus("current")
_HwIsdnMibTraps_ObjectIdentity = ObjectIdentity
hwIsdnMibTraps = _HwIsdnMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 2)
)

# Managed Objects groups


# Notification objects

hwChanbIsdnCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 2, 1)
)
hwChanbIsdnCall.setObjects(
      *(("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnIf"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnAddr"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnCallType"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnCallerAddr"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnInfoType"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnLastKeepTime"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnCallFreeReason"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwChanbIsdnCallFreeCode"))
)
if mibBuilder.loadTexts:
    hwChanbIsdnCall.setStatus(
        "current"
    )

hwQ931IsdnCallSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 2, 2)
)
hwQ931IsdnCallSetup.setObjects(
      *(("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnOpIndex"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnLastCalled"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnLastCalling"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnCallDirection"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnCallTimeOpen"))
)
if mibBuilder.loadTexts:
    hwQ931IsdnCallSetup.setStatus(
        "current"
    )

hwQ931IsdnCallClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 2, 3)
)
hwQ931IsdnCallClear.setObjects(
      *(("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnOpIndex"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnLastCalled"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnLastCalling"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnLastCauseDisc"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnCallDirection"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnCallTimeOpen"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwQ931IsdnCallTimeClose"))
)
if mibBuilder.loadTexts:
    hwQ931IsdnCallClear.setStatus(
        "current"
    )

hwLapdIsdnStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 9, 2, 4)
)
hwLapdIsdnStatusChange.setObjects(
      *(("A3COM-HUAWEI-ISDN-MIB", "hwLapdIsdnIf"),
        ("A3COM-HUAWEI-ISDN-MIB", "hwLapdIsdnLinkStatus"))
)
if mibBuilder.loadTexts:
    hwLapdIsdnStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-ISDN-MIB",
    **{"hwIsdnMib": hwIsdnMib,
       "hwIsdnMibObjects": hwIsdnMibObjects,
       "isdnChannelB": isdnChannelB,
       "hwChanbIsdnTable": hwChanbIsdnTable,
       "hwChanbIsdnEntry": hwChanbIsdnEntry,
       "hwChanbIsdnIf": hwChanbIsdnIf,
       "hwChanbIsdnPermit": hwChanbIsdnPermit,
       "hwChanbIsdnAddr": hwChanbIsdnAddr,
       "hwChanbIsdnCallerAddr": hwChanbIsdnCallerAddr,
       "hwChanbIsdnCallType": hwChanbIsdnCallType,
       "hwChanbIsdnInfoType": hwChanbIsdnInfoType,
       "hwChanbIsdnState": hwChanbIsdnState,
       "hwChanbIsdnCallFreeReason": hwChanbIsdnCallFreeReason,
       "hwChanbIsdnCallFreeCode": hwChanbIsdnCallFreeCode,
       "hwChanbIsdnCallAccept": hwChanbIsdnCallAccept,
       "hwChanbIsdnCallReject": hwChanbIsdnCallReject,
       "hwChanbIsdnCallSuccess": hwChanbIsdnCallSuccess,
       "hwChanbIsdnCallFailure": hwChanbIsdnCallFailure,
       "hwChanbIsdnMaxKeepTime": hwChanbIsdnMaxKeepTime,
       "hwChanbIsdnLastKeepTime": hwChanbIsdnLastKeepTime,
       "hwChanbIsdnLastCallTime": hwChanbIsdnLastCallTime,
       "hwChanbTrapEnable": hwChanbTrapEnable,
       "isdnQ931": isdnQ931,
       "hwQ931IsdnControl": hwQ931IsdnControl,
       "hwQ931CallSetupTrapEnable": hwQ931CallSetupTrapEnable,
       "hwQ931CallClearTrapEnable": hwQ931CallClearTrapEnable,
       "hwQ931IsdnTable": hwQ931IsdnTable,
       "hwQ931IsdnEntry": hwQ931IsdnEntry,
       "hwQ931IsdnOpIndex": hwQ931IsdnOpIndex,
       "hwQ931IsdnLastCalled": hwQ931IsdnLastCalled,
       "hwQ931IsdnLastCalling": hwQ931IsdnLastCalling,
       "hwQ931IsdnLastCauseDisc": hwQ931IsdnLastCauseDisc,
       "hwQ931IsdnCallDirection": hwQ931IsdnCallDirection,
       "hwQ931IsdnCallTimeOpen": hwQ931IsdnCallTimeOpen,
       "hwQ931IsdnCallTimeClose": hwQ931IsdnCallTimeClose,
       "hwIsdnLapd": hwIsdnLapd,
       "hwLapdIsdnTable": hwLapdIsdnTable,
       "hwLapdIsdnEntry": hwLapdIsdnEntry,
       "hwLapdIsdnIf": hwLapdIsdnIf,
       "hwLapdIsdnProtocol": hwLapdIsdnProtocol,
       "hwLapdIsdnIfMode": hwLapdIsdnIfMode,
       "hwLapdIsdnLinkStatus": hwLapdIsdnLinkStatus,
       "hwLapdIsdnControl": hwLapdIsdnControl,
       "hwLapdStatusTrapEnable": hwLapdStatusTrapEnable,
       "hwIsdnMibTraps": hwIsdnMibTraps,
       "hwChanbIsdnCall": hwChanbIsdnCall,
       "hwQ931IsdnCallSetup": hwQ931IsdnCallSetup,
       "hwQ931IsdnCallClear": hwQ931IsdnCallClear,
       "hwLapdIsdnStatusChange": hwLapdIsdnStatusChange}
)
