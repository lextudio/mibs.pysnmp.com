# SNMP MIB module (HH3C-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:41 2024
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

(hh3cmlsr,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cmlsr")

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

hh3cIsdnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIsdnMibObjects_ObjectIdentity = ObjectIdentity
hh3cIsdnMibObjects = _Hh3cIsdnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1)
)
_Hh3cisdnChannelB_ObjectIdentity = ObjectIdentity
hh3cisdnChannelB = _Hh3cisdnChannelB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1)
)
_Hh3cChanbIsdnTable_Object = MibTable
hh3cChanbIsdnTable = _Hh3cChanbIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cChanbIsdnTable.setStatus("current")
_Hh3cChanbIsdnEntry_Object = MibTableRow
hh3cChanbIsdnEntry = _Hh3cChanbIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1)
)
hh3cChanbIsdnEntry.setIndexNames(
    (0, "HH3C-ISDN-MIB", "hh3cChanbIsdnIf"),
)
if mibBuilder.loadTexts:
    hh3cChanbIsdnEntry.setStatus("current")
_Hh3cChanbIsdnIf_Type = Integer32
_Hh3cChanbIsdnIf_Object = MibTableColumn
hh3cChanbIsdnIf = _Hh3cChanbIsdnIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 1),
    _Hh3cChanbIsdnIf_Type()
)
hh3cChanbIsdnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnIf.setStatus("current")


class _Hh3cChanbIsdnPermit_Type(Integer32):
    """Custom type hh3cChanbIsdnPermit based on Integer32"""
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


_Hh3cChanbIsdnPermit_Type.__name__ = "Integer32"
_Hh3cChanbIsdnPermit_Object = MibTableColumn
hh3cChanbIsdnPermit = _Hh3cChanbIsdnPermit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 2),
    _Hh3cChanbIsdnPermit_Type()
)
hh3cChanbIsdnPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnPermit.setStatus("current")
_Hh3cChanbIsdnAddr_Type = DisplayString
_Hh3cChanbIsdnAddr_Object = MibTableColumn
hh3cChanbIsdnAddr = _Hh3cChanbIsdnAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 3),
    _Hh3cChanbIsdnAddr_Type()
)
hh3cChanbIsdnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnAddr.setStatus("current")
_Hh3cChanbIsdnCallerAddr_Type = DisplayString
_Hh3cChanbIsdnCallerAddr_Object = MibTableColumn
hh3cChanbIsdnCallerAddr = _Hh3cChanbIsdnCallerAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 4),
    _Hh3cChanbIsdnCallerAddr_Type()
)
hh3cChanbIsdnCallerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallerAddr.setStatus("current")


class _Hh3cChanbIsdnCallType_Type(Integer32):
    """Custom type hh3cChanbIsdnCallType based on Integer32"""
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


_Hh3cChanbIsdnCallType_Type.__name__ = "Integer32"
_Hh3cChanbIsdnCallType_Object = MibTableColumn
hh3cChanbIsdnCallType = _Hh3cChanbIsdnCallType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 5),
    _Hh3cChanbIsdnCallType_Type()
)
hh3cChanbIsdnCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallType.setStatus("current")


class _Hh3cChanbIsdnInfoType_Type(Integer32):
    """Custom type hh3cChanbIsdnInfoType based on Integer32"""
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


_Hh3cChanbIsdnInfoType_Type.__name__ = "Integer32"
_Hh3cChanbIsdnInfoType_Object = MibTableColumn
hh3cChanbIsdnInfoType = _Hh3cChanbIsdnInfoType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 6),
    _Hh3cChanbIsdnInfoType_Type()
)
hh3cChanbIsdnInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnInfoType.setStatus("current")


class _Hh3cChanbIsdnState_Type(Integer32):
    """Custom type hh3cChanbIsdnState based on Integer32"""
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


_Hh3cChanbIsdnState_Type.__name__ = "Integer32"
_Hh3cChanbIsdnState_Object = MibTableColumn
hh3cChanbIsdnState = _Hh3cChanbIsdnState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 7),
    _Hh3cChanbIsdnState_Type()
)
hh3cChanbIsdnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnState.setStatus("current")
_Hh3cChanbIsdnCallFreeReason_Type = DisplayString
_Hh3cChanbIsdnCallFreeReason_Object = MibTableColumn
hh3cChanbIsdnCallFreeReason = _Hh3cChanbIsdnCallFreeReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 8),
    _Hh3cChanbIsdnCallFreeReason_Type()
)
hh3cChanbIsdnCallFreeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallFreeReason.setStatus("current")
_Hh3cChanbIsdnCallFreeCode_Type = Integer32
_Hh3cChanbIsdnCallFreeCode_Object = MibTableColumn
hh3cChanbIsdnCallFreeCode = _Hh3cChanbIsdnCallFreeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 9),
    _Hh3cChanbIsdnCallFreeCode_Type()
)
hh3cChanbIsdnCallFreeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallFreeCode.setStatus("current")
_Hh3cChanbIsdnCallAccept_Type = Counter32
_Hh3cChanbIsdnCallAccept_Object = MibTableColumn
hh3cChanbIsdnCallAccept = _Hh3cChanbIsdnCallAccept_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 10),
    _Hh3cChanbIsdnCallAccept_Type()
)
hh3cChanbIsdnCallAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallAccept.setStatus("current")
_Hh3cChanbIsdnCallReject_Type = Counter32
_Hh3cChanbIsdnCallReject_Object = MibTableColumn
hh3cChanbIsdnCallReject = _Hh3cChanbIsdnCallReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 11),
    _Hh3cChanbIsdnCallReject_Type()
)
hh3cChanbIsdnCallReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallReject.setStatus("current")
_Hh3cChanbIsdnCallSuccess_Type = Counter32
_Hh3cChanbIsdnCallSuccess_Object = MibTableColumn
hh3cChanbIsdnCallSuccess = _Hh3cChanbIsdnCallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 12),
    _Hh3cChanbIsdnCallSuccess_Type()
)
hh3cChanbIsdnCallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallSuccess.setStatus("current")
_Hh3cChanbIsdnCallFailure_Type = Counter32
_Hh3cChanbIsdnCallFailure_Object = MibTableColumn
hh3cChanbIsdnCallFailure = _Hh3cChanbIsdnCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 13),
    _Hh3cChanbIsdnCallFailure_Type()
)
hh3cChanbIsdnCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnCallFailure.setStatus("current")


class _Hh3cChanbIsdnMaxKeepTime_Type(Integer32):
    """Custom type hh3cChanbIsdnMaxKeepTime based on Integer32"""
    defaultValue = 2147483647


_Hh3cChanbIsdnMaxKeepTime_Object = MibTableColumn
hh3cChanbIsdnMaxKeepTime = _Hh3cChanbIsdnMaxKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 14),
    _Hh3cChanbIsdnMaxKeepTime_Type()
)
hh3cChanbIsdnMaxKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnMaxKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cChanbIsdnMaxKeepTime.setUnits("milliseconds")
_Hh3cChanbIsdnLastKeepTime_Type = Integer32
_Hh3cChanbIsdnLastKeepTime_Object = MibTableColumn
hh3cChanbIsdnLastKeepTime = _Hh3cChanbIsdnLastKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 15),
    _Hh3cChanbIsdnLastKeepTime_Type()
)
hh3cChanbIsdnLastKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnLastKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cChanbIsdnLastKeepTime.setUnits("milliseconds")
_Hh3cChanbIsdnLastCallTime_Type = TimeStamp
_Hh3cChanbIsdnLastCallTime_Object = MibTableColumn
hh3cChanbIsdnLastCallTime = _Hh3cChanbIsdnLastCallTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 1, 1, 16),
    _Hh3cChanbIsdnLastCallTime_Type()
)
hh3cChanbIsdnLastCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cChanbIsdnLastCallTime.setStatus("current")


class _Hh3cChanbTrapEnable_Type(Integer32):
    """Custom type hh3cChanbTrapEnable based on Integer32"""
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


_Hh3cChanbTrapEnable_Type.__name__ = "Integer32"
_Hh3cChanbTrapEnable_Object = MibScalar
hh3cChanbTrapEnable = _Hh3cChanbTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 1, 2),
    _Hh3cChanbTrapEnable_Type()
)
hh3cChanbTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cChanbTrapEnable.setStatus("current")
_Hh3cisdnQ931_ObjectIdentity = ObjectIdentity
hh3cisdnQ931 = _Hh3cisdnQ931_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2)
)
_Hh3cQ931IsdnControl_ObjectIdentity = ObjectIdentity
hh3cQ931IsdnControl = _Hh3cQ931IsdnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 1)
)


class _Hh3cQ931CallSetupTrapEnable_Type(Integer32):
    """Custom type hh3cQ931CallSetupTrapEnable based on Integer32"""
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


_Hh3cQ931CallSetupTrapEnable_Type.__name__ = "Integer32"
_Hh3cQ931CallSetupTrapEnable_Object = MibScalar
hh3cQ931CallSetupTrapEnable = _Hh3cQ931CallSetupTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 1, 1),
    _Hh3cQ931CallSetupTrapEnable_Type()
)
hh3cQ931CallSetupTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQ931CallSetupTrapEnable.setStatus("current")


class _Hh3cQ931CallClearTrapEnable_Type(Integer32):
    """Custom type hh3cQ931CallClearTrapEnable based on Integer32"""
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


_Hh3cQ931CallClearTrapEnable_Type.__name__ = "Integer32"
_Hh3cQ931CallClearTrapEnable_Object = MibScalar
hh3cQ931CallClearTrapEnable = _Hh3cQ931CallClearTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 1, 2),
    _Hh3cQ931CallClearTrapEnable_Type()
)
hh3cQ931CallClearTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQ931CallClearTrapEnable.setStatus("current")
_Hh3cQ931IsdnTable_Object = MibTable
hh3cQ931IsdnTable = _Hh3cQ931IsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cQ931IsdnTable.setStatus("current")
_Hh3cQ931IsdnEntry_Object = MibTableRow
hh3cQ931IsdnEntry = _Hh3cQ931IsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1)
)
hh3cQ931IsdnEntry.setIndexNames(
    (0, "HH3C-ISDN-MIB", "hh3cQ931IsdnOpIndex"),
)
if mibBuilder.loadTexts:
    hh3cQ931IsdnEntry.setStatus("current")
_Hh3cQ931IsdnOpIndex_Type = Integer32
_Hh3cQ931IsdnOpIndex_Object = MibTableColumn
hh3cQ931IsdnOpIndex = _Hh3cQ931IsdnOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 1),
    _Hh3cQ931IsdnOpIndex_Type()
)
hh3cQ931IsdnOpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cQ931IsdnOpIndex.setStatus("current")
_Hh3cQ931IsdnLastCalled_Type = DisplayString
_Hh3cQ931IsdnLastCalled_Object = MibTableColumn
hh3cQ931IsdnLastCalled = _Hh3cQ931IsdnLastCalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 2),
    _Hh3cQ931IsdnLastCalled_Type()
)
hh3cQ931IsdnLastCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnLastCalled.setStatus("current")
_Hh3cQ931IsdnLastCalling_Type = DisplayString
_Hh3cQ931IsdnLastCalling_Object = MibTableColumn
hh3cQ931IsdnLastCalling = _Hh3cQ931IsdnLastCalling_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 3),
    _Hh3cQ931IsdnLastCalling_Type()
)
hh3cQ931IsdnLastCalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnLastCalling.setStatus("current")


class _Hh3cQ931IsdnLastCauseDisc_Type(Integer32):
    """Custom type hh3cQ931IsdnLastCauseDisc based on Integer32"""
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


_Hh3cQ931IsdnLastCauseDisc_Type.__name__ = "Integer32"
_Hh3cQ931IsdnLastCauseDisc_Object = MibTableColumn
hh3cQ931IsdnLastCauseDisc = _Hh3cQ931IsdnLastCauseDisc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 4),
    _Hh3cQ931IsdnLastCauseDisc_Type()
)
hh3cQ931IsdnLastCauseDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnLastCauseDisc.setStatus("current")


class _Hh3cQ931IsdnCallDirection_Type(Integer32):
    """Custom type hh3cQ931IsdnCallDirection based on Integer32"""
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


_Hh3cQ931IsdnCallDirection_Type.__name__ = "Integer32"
_Hh3cQ931IsdnCallDirection_Object = MibTableColumn
hh3cQ931IsdnCallDirection = _Hh3cQ931IsdnCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 5),
    _Hh3cQ931IsdnCallDirection_Type()
)
hh3cQ931IsdnCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnCallDirection.setStatus("current")
_Hh3cQ931IsdnCallTimeOpen_Type = DateAndTime
_Hh3cQ931IsdnCallTimeOpen_Object = MibTableColumn
hh3cQ931IsdnCallTimeOpen = _Hh3cQ931IsdnCallTimeOpen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 6),
    _Hh3cQ931IsdnCallTimeOpen_Type()
)
hh3cQ931IsdnCallTimeOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnCallTimeOpen.setStatus("current")
_Hh3cQ931IsdnCallTimeClose_Type = DateAndTime
_Hh3cQ931IsdnCallTimeClose_Object = MibTableColumn
hh3cQ931IsdnCallTimeClose = _Hh3cQ931IsdnCallTimeClose_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 2, 2, 1, 7),
    _Hh3cQ931IsdnCallTimeClose_Type()
)
hh3cQ931IsdnCallTimeClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQ931IsdnCallTimeClose.setStatus("current")
_Hh3cIsdnLapd_ObjectIdentity = ObjectIdentity
hh3cIsdnLapd = _Hh3cIsdnLapd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3)
)
_Hh3cLapdIsdnTable_Object = MibTable
hh3cLapdIsdnTable = _Hh3cLapdIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cLapdIsdnTable.setStatus("current")
_Hh3cLapdIsdnEntry_Object = MibTableRow
hh3cLapdIsdnEntry = _Hh3cLapdIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1, 1)
)
hh3cLapdIsdnEntry.setIndexNames(
    (0, "HH3C-ISDN-MIB", "hh3cLapdIsdnIf"),
)
if mibBuilder.loadTexts:
    hh3cLapdIsdnEntry.setStatus("current")
_Hh3cLapdIsdnIf_Type = Integer32
_Hh3cLapdIsdnIf_Object = MibTableColumn
hh3cLapdIsdnIf = _Hh3cLapdIsdnIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1, 1, 1),
    _Hh3cLapdIsdnIf_Type()
)
hh3cLapdIsdnIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLapdIsdnIf.setStatus("current")


class _Hh3cLapdIsdnProtocol_Type(Integer32):
    """Custom type hh3cLapdIsdnProtocol based on Integer32"""
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


_Hh3cLapdIsdnProtocol_Type.__name__ = "Integer32"
_Hh3cLapdIsdnProtocol_Object = MibTableColumn
hh3cLapdIsdnProtocol = _Hh3cLapdIsdnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1, 1, 2),
    _Hh3cLapdIsdnProtocol_Type()
)
hh3cLapdIsdnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLapdIsdnProtocol.setStatus("current")


class _Hh3cLapdIsdnIfMode_Type(Integer32):
    """Custom type hh3cLapdIsdnIfMode based on Integer32"""
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


_Hh3cLapdIsdnIfMode_Type.__name__ = "Integer32"
_Hh3cLapdIsdnIfMode_Object = MibTableColumn
hh3cLapdIsdnIfMode = _Hh3cLapdIsdnIfMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1, 1, 3),
    _Hh3cLapdIsdnIfMode_Type()
)
hh3cLapdIsdnIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLapdIsdnIfMode.setStatus("current")


class _Hh3cLapdIsdnLinkStatus_Type(Integer32):
    """Custom type hh3cLapdIsdnLinkStatus based on Integer32"""
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


_Hh3cLapdIsdnLinkStatus_Type.__name__ = "Integer32"
_Hh3cLapdIsdnLinkStatus_Object = MibTableColumn
hh3cLapdIsdnLinkStatus = _Hh3cLapdIsdnLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 1, 1, 4),
    _Hh3cLapdIsdnLinkStatus_Type()
)
hh3cLapdIsdnLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLapdIsdnLinkStatus.setStatus("current")
_Hh3cLapdIsdnControl_ObjectIdentity = ObjectIdentity
hh3cLapdIsdnControl = _Hh3cLapdIsdnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 2)
)


class _Hh3cLapdStatusTrapEnable_Type(Integer32):
    """Custom type hh3cLapdStatusTrapEnable based on Integer32"""
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


_Hh3cLapdStatusTrapEnable_Type.__name__ = "Integer32"
_Hh3cLapdStatusTrapEnable_Object = MibScalar
hh3cLapdStatusTrapEnable = _Hh3cLapdStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 1, 3, 2, 1),
    _Hh3cLapdStatusTrapEnable_Type()
)
hh3cLapdStatusTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLapdStatusTrapEnable.setStatus("current")
_Hh3cIsdnMibTraps_ObjectIdentity = ObjectIdentity
hh3cIsdnMibTraps = _Hh3cIsdnMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 2)
)

# Managed Objects groups


# Notification objects

hh3cChanbIsdnCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 2, 1)
)
hh3cChanbIsdnCall.setObjects(
      *(("HH3C-ISDN-MIB", "hh3cChanbIsdnIf"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnAddr"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnCallType"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnCallerAddr"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnInfoType"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnLastKeepTime"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnCallFreeReason"),
        ("HH3C-ISDN-MIB", "hh3cChanbIsdnCallFreeCode"))
)
if mibBuilder.loadTexts:
    hh3cChanbIsdnCall.setStatus(
        "current"
    )

hh3cQ931IsdnCallSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 2, 2)
)
hh3cQ931IsdnCallSetup.setObjects(
      *(("HH3C-ISDN-MIB", "hh3cQ931IsdnOpIndex"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnLastCalled"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnLastCalling"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnCallDirection"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnCallTimeOpen"))
)
if mibBuilder.loadTexts:
    hh3cQ931IsdnCallSetup.setStatus(
        "current"
    )

hh3cQ931IsdnCallClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 2, 3)
)
hh3cQ931IsdnCallClear.setObjects(
      *(("HH3C-ISDN-MIB", "hh3cQ931IsdnOpIndex"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnLastCalled"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnLastCalling"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnLastCauseDisc"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnCallDirection"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnCallTimeOpen"),
        ("HH3C-ISDN-MIB", "hh3cQ931IsdnCallTimeClose"))
)
if mibBuilder.loadTexts:
    hh3cQ931IsdnCallClear.setStatus(
        "current"
    )

hh3cLapdIsdnStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9, 2, 4)
)
hh3cLapdIsdnStatusChange.setObjects(
      *(("HH3C-ISDN-MIB", "hh3cLapdIsdnIf"),
        ("HH3C-ISDN-MIB", "hh3cLapdIsdnLinkStatus"))
)
if mibBuilder.loadTexts:
    hh3cLapdIsdnStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ISDN-MIB",
    **{"hh3cIsdnMib": hh3cIsdnMib,
       "hh3cIsdnMibObjects": hh3cIsdnMibObjects,
       "hh3cisdnChannelB": hh3cisdnChannelB,
       "hh3cChanbIsdnTable": hh3cChanbIsdnTable,
       "hh3cChanbIsdnEntry": hh3cChanbIsdnEntry,
       "hh3cChanbIsdnIf": hh3cChanbIsdnIf,
       "hh3cChanbIsdnPermit": hh3cChanbIsdnPermit,
       "hh3cChanbIsdnAddr": hh3cChanbIsdnAddr,
       "hh3cChanbIsdnCallerAddr": hh3cChanbIsdnCallerAddr,
       "hh3cChanbIsdnCallType": hh3cChanbIsdnCallType,
       "hh3cChanbIsdnInfoType": hh3cChanbIsdnInfoType,
       "hh3cChanbIsdnState": hh3cChanbIsdnState,
       "hh3cChanbIsdnCallFreeReason": hh3cChanbIsdnCallFreeReason,
       "hh3cChanbIsdnCallFreeCode": hh3cChanbIsdnCallFreeCode,
       "hh3cChanbIsdnCallAccept": hh3cChanbIsdnCallAccept,
       "hh3cChanbIsdnCallReject": hh3cChanbIsdnCallReject,
       "hh3cChanbIsdnCallSuccess": hh3cChanbIsdnCallSuccess,
       "hh3cChanbIsdnCallFailure": hh3cChanbIsdnCallFailure,
       "hh3cChanbIsdnMaxKeepTime": hh3cChanbIsdnMaxKeepTime,
       "hh3cChanbIsdnLastKeepTime": hh3cChanbIsdnLastKeepTime,
       "hh3cChanbIsdnLastCallTime": hh3cChanbIsdnLastCallTime,
       "hh3cChanbTrapEnable": hh3cChanbTrapEnable,
       "hh3cisdnQ931": hh3cisdnQ931,
       "hh3cQ931IsdnControl": hh3cQ931IsdnControl,
       "hh3cQ931CallSetupTrapEnable": hh3cQ931CallSetupTrapEnable,
       "hh3cQ931CallClearTrapEnable": hh3cQ931CallClearTrapEnable,
       "hh3cQ931IsdnTable": hh3cQ931IsdnTable,
       "hh3cQ931IsdnEntry": hh3cQ931IsdnEntry,
       "hh3cQ931IsdnOpIndex": hh3cQ931IsdnOpIndex,
       "hh3cQ931IsdnLastCalled": hh3cQ931IsdnLastCalled,
       "hh3cQ931IsdnLastCalling": hh3cQ931IsdnLastCalling,
       "hh3cQ931IsdnLastCauseDisc": hh3cQ931IsdnLastCauseDisc,
       "hh3cQ931IsdnCallDirection": hh3cQ931IsdnCallDirection,
       "hh3cQ931IsdnCallTimeOpen": hh3cQ931IsdnCallTimeOpen,
       "hh3cQ931IsdnCallTimeClose": hh3cQ931IsdnCallTimeClose,
       "hh3cIsdnLapd": hh3cIsdnLapd,
       "hh3cLapdIsdnTable": hh3cLapdIsdnTable,
       "hh3cLapdIsdnEntry": hh3cLapdIsdnEntry,
       "hh3cLapdIsdnIf": hh3cLapdIsdnIf,
       "hh3cLapdIsdnProtocol": hh3cLapdIsdnProtocol,
       "hh3cLapdIsdnIfMode": hh3cLapdIsdnIfMode,
       "hh3cLapdIsdnLinkStatus": hh3cLapdIsdnLinkStatus,
       "hh3cLapdIsdnControl": hh3cLapdIsdnControl,
       "hh3cLapdStatusTrapEnable": hh3cLapdStatusTrapEnable,
       "hh3cIsdnMibTraps": hh3cIsdnMibTraps,
       "hh3cChanbIsdnCall": hh3cChanbIsdnCall,
       "hh3cQ931IsdnCallSetup": hh3cQ931IsdnCallSetup,
       "hh3cQ931IsdnCallClear": hh3cQ931IsdnCallClear,
       "hh3cLapdIsdnStatusChange": hh3cLapdIsdnStatusChange}
)
