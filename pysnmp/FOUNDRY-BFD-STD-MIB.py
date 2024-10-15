# SNMP MIB module (FOUNDRY-BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-BFD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:39 2024
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

(bfd,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "bfd")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

bfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1)
)
bfdMIB.setRevisions(
        ("2005-08-22 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdSessIndexTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BfdInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BfdDiag(Integer32, TextualConvention):
    status = "current"
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
        *(("administrativelyDown", 8),
          ("concatenatedPathDown", 7),
          ("controlDetectionTimeExpired", 2),
          ("echoFunctionFailed", 3),
          ("forwardingPlaneReset", 5),
          ("neighborSignaledSessionDown", 4),
          ("noDiagnostic", 1),
          ("pathDown", 6),
          ("reverseConcatenatedPathDown", 9))
    )



# MIB Managed Objects in the order of their OIDs

_BfdNotifications_ObjectIdentity = ObjectIdentity
bfdNotifications = _BfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0)
)
_BfdObjects_ObjectIdentity = ObjectIdentity
bfdObjects = _BfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1)
)
_BfdScalarObjects_ObjectIdentity = ObjectIdentity
bfdScalarObjects = _BfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1)
)


class _BfdAdminStatus_Type(Integer32):
    """Custom type bfdAdminStatus based on Integer32"""
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


_BfdAdminStatus_Type.__name__ = "Integer32"
_BfdAdminStatus_Object = MibScalar
bfdAdminStatus = _BfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 1),
    _BfdAdminStatus_Type()
)
bfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdAdminStatus.setStatus("current")


class _BfdVersionNumber_Type(Unsigned32):
    """Custom type bfdVersionNumber based on Unsigned32"""
    defaultValue = 0


_BfdVersionNumber_Object = MibScalar
bfdVersionNumber = _BfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 3),
    _BfdVersionNumber_Type()
)
bfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdVersionNumber.setStatus("current")


class _BfdSessNotificationsEnable_Type(TruthValue):
    """Custom type bfdSessNotificationsEnable based on TruthValue"""


_BfdSessNotificationsEnable_Object = MibScalar
bfdSessNotificationsEnable = _BfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 4),
    _BfdSessNotificationsEnable_Type()
)
bfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessNotificationsEnable.setStatus("current")
_BfdSessTable_Object = MibTable
bfdSessTable = _BfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bfdSessTable.setStatus("current")
_BfdSessEntry_Object = MibTableRow
bfdSessEntry = _BfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1)
)
bfdSessEntry.setIndexNames(
    (0, "FOUNDRY-BFD-STD-MIB", "bfdSessIndex"),
)
if mibBuilder.loadTexts:
    bfdSessEntry.setStatus("current")
_BfdSessIndex_Type = BfdSessIndexTC
_BfdSessIndex_Object = MibTableColumn
bfdSessIndex = _BfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 1),
    _BfdSessIndex_Type()
)
bfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessIndex.setStatus("current")
_BfdSessApplicationId_Type = Unsigned32
_BfdSessApplicationId_Object = MibTableColumn
bfdSessApplicationId = _BfdSessApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 2),
    _BfdSessApplicationId_Type()
)
bfdSessApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessApplicationId.setStatus("current")


class _BfdSessDiscriminator_Type(Unsigned32):
    """Custom type bfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BfdSessDiscriminator_Type.__name__ = "Unsigned32"
_BfdSessDiscriminator_Object = MibTableColumn
bfdSessDiscriminator = _BfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 3),
    _BfdSessDiscriminator_Type()
)
bfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessDiscriminator.setStatus("current")


class _BfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type bfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_BfdSessRemoteDiscr_Object = MibTableColumn
bfdSessRemoteDiscr = _BfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 4),
    _BfdSessRemoteDiscr_Type()
)
bfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessRemoteDiscr.setStatus("current")


class _BfdSessUdpPort_Type(InetPortNumber):
    """Custom type bfdSessUdpPort based on InetPortNumber"""
    defaultValue = 0


_BfdSessUdpPort_Object = MibTableColumn
bfdSessUdpPort = _BfdSessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 5),
    _BfdSessUdpPort_Type()
)
bfdSessUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessUdpPort.setStatus("current")


class _BfdSessState_Type(Integer32):
    """Custom type bfdSessState based on Integer32"""
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4))
    )


_BfdSessState_Type.__name__ = "Integer32"
_BfdSessState_Object = MibTableColumn
bfdSessState = _BfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 6),
    _BfdSessState_Type()
)
bfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessState.setStatus("current")
_BfdSessRemoteHeardFlag_Type = TruthValue
_BfdSessRemoteHeardFlag_Object = MibTableColumn
bfdSessRemoteHeardFlag = _BfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 7),
    _BfdSessRemoteHeardFlag_Type()
)
bfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessRemoteHeardFlag.setStatus("current")
_BfdSessDiag_Type = Unsigned32
_BfdSessDiag_Object = MibTableColumn
bfdSessDiag = _BfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 8),
    _BfdSessDiag_Type()
)
bfdSessDiag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bfdSessDiag.setStatus("current")


class _BfdSessOperMode_Type(Integer32):
    """Custom type bfdSessOperMode based on Integer32"""
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
        *(("asyncModeWEchoFun", 1),
          ("asynchModeWOEchoFun", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4))
    )


_BfdSessOperMode_Type.__name__ = "Integer32"
_BfdSessOperMode_Object = MibTableColumn
bfdSessOperMode = _BfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 9),
    _BfdSessOperMode_Type()
)
bfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessOperMode.setStatus("current")


class _BfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type bfdSessDemandModeDesiredFlag based on TruthValue"""


_BfdSessDemandModeDesiredFlag_Object = MibTableColumn
bfdSessDemandModeDesiredFlag = _BfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 10),
    _BfdSessDemandModeDesiredFlag_Type()
)
bfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDemandModeDesiredFlag.setStatus("current")


class _BfdSessEchoFuncModeDesiredFlag_Type(TruthValue):
    """Custom type bfdSessEchoFuncModeDesiredFlag based on TruthValue"""


_BfdSessEchoFuncModeDesiredFlag_Object = MibTableColumn
bfdSessEchoFuncModeDesiredFlag = _BfdSessEchoFuncModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 11),
    _BfdSessEchoFuncModeDesiredFlag_Type()
)
bfdSessEchoFuncModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessEchoFuncModeDesiredFlag.setStatus("current")


class _BfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type bfdSessControlPlanIndepFlag based on TruthValue"""


_BfdSessControlPlanIndepFlag_Object = MibTableColumn
bfdSessControlPlanIndepFlag = _BfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 12),
    _BfdSessControlPlanIndepFlag_Type()
)
bfdSessControlPlanIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessControlPlanIndepFlag.setStatus("current")
_BfdSessAddrType_Type = InetAddressType
_BfdSessAddrType_Object = MibTableColumn
bfdSessAddrType = _BfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 13),
    _BfdSessAddrType_Type()
)
bfdSessAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAddrType.setStatus("current")
_BfdSessAddr_Type = InetAddress
_BfdSessAddr_Object = MibTableColumn
bfdSessAddr = _BfdSessAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 14),
    _BfdSessAddr_Type()
)
bfdSessAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAddr.setStatus("current")
_BfdSessDesiredMinTxInterval_Type = BfdInterval
_BfdSessDesiredMinTxInterval_Object = MibTableColumn
bfdSessDesiredMinTxInterval = _BfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 15),
    _BfdSessDesiredMinTxInterval_Type()
)
bfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDesiredMinTxInterval.setStatus("current")
_BfdSessReqMinRxInterval_Type = BfdInterval
_BfdSessReqMinRxInterval_Object = MibTableColumn
bfdSessReqMinRxInterval = _BfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 16),
    _BfdSessReqMinRxInterval_Type()
)
bfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessReqMinRxInterval.setStatus("current")
_BfdSessReqMinEchoRxInterval_Type = BfdInterval
_BfdSessReqMinEchoRxInterval_Object = MibTableColumn
bfdSessReqMinEchoRxInterval = _BfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 17),
    _BfdSessReqMinEchoRxInterval_Type()
)
bfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessReqMinEchoRxInterval.setStatus("current")
_BfdSessDetectMult_Type = Unsigned32
_BfdSessDetectMult_Object = MibTableColumn
bfdSessDetectMult = _BfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 18),
    _BfdSessDetectMult_Type()
)
bfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDetectMult.setStatus("current")
_BfdSessStorType_Type = StorageType
_BfdSessStorType_Object = MibTableColumn
bfdSessStorType = _BfdSessStorType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 19),
    _BfdSessStorType_Type()
)
bfdSessStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessStorType.setStatus("current")
_BfdSessRowStatus_Type = RowStatus
_BfdSessRowStatus_Object = MibTableColumn
bfdSessRowStatus = _BfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 20),
    _BfdSessRowStatus_Type()
)
bfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessRowStatus.setStatus("current")


class _BfdSessAuthPresFlag_Type(TruthValue):
    """Custom type bfdSessAuthPresFlag based on TruthValue"""


_BfdSessAuthPresFlag_Object = MibTableColumn
bfdSessAuthPresFlag = _BfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 21),
    _BfdSessAuthPresFlag_Type()
)
bfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthPresFlag.setStatus("current")


class _BfdSessAuthenticationType_Type(Integer32):
    """Custom type bfdSessAuthenticationType based on Integer32"""
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
        *(("keyedMD5", 2),
          ("keyedSHA1", 4),
          ("meticulousKeyedMD5", 3),
          ("meticulousKeyedSHA1", 5),
          ("simplePassword", 1))
    )


_BfdSessAuthenticationType_Type.__name__ = "Integer32"
_BfdSessAuthenticationType_Object = MibTableColumn
bfdSessAuthenticationType = _BfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 22),
    _BfdSessAuthenticationType_Type()
)
bfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthenticationType.setStatus("current")
_BfdSessPerfTable_Object = MibTable
bfdSessPerfTable = _BfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bfdSessPerfTable.setStatus("current")
_BfdSessPerfEntry_Object = MibTableRow
bfdSessPerfEntry = _BfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bfdSessPerfEntry.setStatus("current")
_BfdSessPerfPktIn_Type = Counter32
_BfdSessPerfPktIn_Object = MibTableColumn
bfdSessPerfPktIn = _BfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 1),
    _BfdSessPerfPktIn_Type()
)
bfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfPktIn.setStatus("current")
_BfdSessPerfPktOut_Type = Counter32
_BfdSessPerfPktOut_Object = MibTableColumn
bfdSessPerfPktOut = _BfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 2),
    _BfdSessPerfPktOut_Type()
)
bfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfPktOut.setStatus("current")
_BfdSessPerfUpTime_Type = TimeStamp
_BfdSessPerfUpTime_Object = MibTableColumn
bfdSessPerfUpTime = _BfdSessPerfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 3),
    _BfdSessPerfUpTime_Type()
)
bfdSessPerfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfUpTime.setStatus("current")
_BfdSessPerfLastSessDownTime_Type = TimeStamp
_BfdSessPerfLastSessDownTime_Object = MibTableColumn
bfdSessPerfLastSessDownTime = _BfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 4),
    _BfdSessPerfLastSessDownTime_Type()
)
bfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfLastSessDownTime.setStatus("current")
_BfdSessPerfLastCommLostDiag_Type = BfdDiag
_BfdSessPerfLastCommLostDiag_Object = MibTableColumn
bfdSessPerfLastCommLostDiag = _BfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 5),
    _BfdSessPerfLastCommLostDiag_Type()
)
bfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfLastCommLostDiag.setStatus("current")
_BfdSessPerfSessUpCount_Type = Counter32
_BfdSessPerfSessUpCount_Object = MibTableColumn
bfdSessPerfSessUpCount = _BfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 6),
    _BfdSessPerfSessUpCount_Type()
)
bfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfSessUpCount.setStatus("current")
_BfdSessPerfDiscTime_Type = TimeStamp
_BfdSessPerfDiscTime_Object = MibTableColumn
bfdSessPerfDiscTime = _BfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 7),
    _BfdSessPerfDiscTime_Type()
)
bfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfDiscTime.setStatus("current")
_BfdSessPerfPktInHC_Type = Counter64
_BfdSessPerfPktInHC_Object = MibTableColumn
bfdSessPerfPktInHC = _BfdSessPerfPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 8),
    _BfdSessPerfPktInHC_Type()
)
bfdSessPerfPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfPktInHC.setStatus("current")
_BfdSessPerfPktOutHC_Type = Counter64
_BfdSessPerfPktOutHC_Object = MibTableColumn
bfdSessPerfPktOutHC = _BfdSessPerfPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 9),
    _BfdSessPerfPktOutHC_Type()
)
bfdSessPerfPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfPktOutHC.setStatus("current")
_BfdSessMapTable_Object = MibTable
bfdSessMapTable = _BfdSessMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    bfdSessMapTable.setStatus("current")
_BfdSessMapEntry_Object = MibTableRow
bfdSessMapEntry = _BfdSessMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4, 1)
)
bfdSessMapEntry.setIndexNames(
    (0, "FOUNDRY-BFD-STD-MIB", "bfdSessApplicationId"),
    (0, "FOUNDRY-BFD-STD-MIB", "bfdSessDiscriminator"),
    (0, "FOUNDRY-BFD-STD-MIB", "bfdSessAddrType"),
    (0, "FOUNDRY-BFD-STD-MIB", "bfdSessAddr"),
)
if mibBuilder.loadTexts:
    bfdSessMapEntry.setStatus("current")
_BfdSessMapBfdIndex_Type = BfdSessIndexTC
_BfdSessMapBfdIndex_Object = MibTableColumn
bfdSessMapBfdIndex = _BfdSessMapBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4, 1, 1),
    _BfdSessMapBfdIndex_Type()
)
bfdSessMapBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessMapBfdIndex.setStatus("current")
_BfdConformance_ObjectIdentity = ObjectIdentity
bfdConformance = _BfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3)
)
_BfdGroups_ObjectIdentity = ObjectIdentity
bfdGroups = _BfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1)
)
_BfdCompliances_ObjectIdentity = ObjectIdentity
bfdCompliances = _BfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 2)
)
bfdSessEntry.registerAugmentions(
    ("FOUNDRY-BFD-STD-MIB",
     "bfdSessPerfEntry")
)
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())

# Managed Objects groups

bfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 1)
)
bfdSessionGroup.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessNotificationsEnable"),
        ("FOUNDRY-BFD-STD-MIB", "bfdAdminStatus"),
        ("FOUNDRY-BFD-STD-MIB", "bfdVersionNumber"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessApplicationId"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDiscriminator"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessAddrType"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessAddr"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessRemoteDiscr"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessUdpPort"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessState"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessRemoteHeardFlag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessOperMode"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDemandModeDesiredFlag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessEchoFuncModeDesiredFlag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessControlPlanIndepFlag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDesiredMinTxInterval"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessReqMinRxInterval"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessReqMinEchoRxInterval"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDetectMult"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessStorType"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessRowStatus"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessMapBfdIndex"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessAuthPresFlag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessAuthenticationType"))
)
if mibBuilder.loadTexts:
    bfdSessionGroup.setStatus("current")

bfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 2)
)
bfdSessionPerfGroup.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktIn"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktOut"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfUpTime"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfLastSessDownTime"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfLastCommLostDiag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfSessUpCount"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    bfdSessionPerfGroup.setStatus("current")

bfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 3)
)
bfdSessionPerfHCGroup.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktInHC"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktOutHC"))
)
if mibBuilder.loadTexts:
    bfdSessionPerfHCGroup.setStatus("current")


# Notification objects

bfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0, 1)
)
bfdSessUp.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"))
)
if mibBuilder.loadTexts:
    bfdSessUp.setStatus(
        "current"
    )

bfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0, 2)
)
bfdSessDown.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"))
)
if mibBuilder.loadTexts:
    bfdSessDown.setStatus(
        "current"
    )


# Notifications groups

bfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 4)
)
bfdNotificationGroup.setObjects(
      *(("FOUNDRY-BFD-STD-MIB", "bfdSessUp"),
        ("FOUNDRY-BFD-STD-MIB", "bfdSessDown"))
)
if mibBuilder.loadTexts:
    bfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bfdModuleFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-BFD-STD-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "bfdMIB": bfdMIB,
       "bfdNotifications": bfdNotifications,
       "bfdSessUp": bfdSessUp,
       "bfdSessDown": bfdSessDown,
       "bfdObjects": bfdObjects,
       "bfdScalarObjects": bfdScalarObjects,
       "bfdAdminStatus": bfdAdminStatus,
       "bfdVersionNumber": bfdVersionNumber,
       "bfdSessNotificationsEnable": bfdSessNotificationsEnable,
       "bfdSessTable": bfdSessTable,
       "bfdSessEntry": bfdSessEntry,
       "bfdSessIndex": bfdSessIndex,
       "bfdSessApplicationId": bfdSessApplicationId,
       "bfdSessDiscriminator": bfdSessDiscriminator,
       "bfdSessRemoteDiscr": bfdSessRemoteDiscr,
       "bfdSessUdpPort": bfdSessUdpPort,
       "bfdSessState": bfdSessState,
       "bfdSessRemoteHeardFlag": bfdSessRemoteHeardFlag,
       "bfdSessDiag": bfdSessDiag,
       "bfdSessOperMode": bfdSessOperMode,
       "bfdSessDemandModeDesiredFlag": bfdSessDemandModeDesiredFlag,
       "bfdSessEchoFuncModeDesiredFlag": bfdSessEchoFuncModeDesiredFlag,
       "bfdSessControlPlanIndepFlag": bfdSessControlPlanIndepFlag,
       "bfdSessAddrType": bfdSessAddrType,
       "bfdSessAddr": bfdSessAddr,
       "bfdSessDesiredMinTxInterval": bfdSessDesiredMinTxInterval,
       "bfdSessReqMinRxInterval": bfdSessReqMinRxInterval,
       "bfdSessReqMinEchoRxInterval": bfdSessReqMinEchoRxInterval,
       "bfdSessDetectMult": bfdSessDetectMult,
       "bfdSessStorType": bfdSessStorType,
       "bfdSessRowStatus": bfdSessRowStatus,
       "bfdSessAuthPresFlag": bfdSessAuthPresFlag,
       "bfdSessAuthenticationType": bfdSessAuthenticationType,
       "bfdSessPerfTable": bfdSessPerfTable,
       "bfdSessPerfEntry": bfdSessPerfEntry,
       "bfdSessPerfPktIn": bfdSessPerfPktIn,
       "bfdSessPerfPktOut": bfdSessPerfPktOut,
       "bfdSessPerfUpTime": bfdSessPerfUpTime,
       "bfdSessPerfLastSessDownTime": bfdSessPerfLastSessDownTime,
       "bfdSessPerfLastCommLostDiag": bfdSessPerfLastCommLostDiag,
       "bfdSessPerfSessUpCount": bfdSessPerfSessUpCount,
       "bfdSessPerfDiscTime": bfdSessPerfDiscTime,
       "bfdSessPerfPktInHC": bfdSessPerfPktInHC,
       "bfdSessPerfPktOutHC": bfdSessPerfPktOutHC,
       "bfdSessMapTable": bfdSessMapTable,
       "bfdSessMapEntry": bfdSessMapEntry,
       "bfdSessMapBfdIndex": bfdSessMapBfdIndex,
       "bfdConformance": bfdConformance,
       "bfdGroups": bfdGroups,
       "bfdSessionGroup": bfdSessionGroup,
       "bfdSessionPerfGroup": bfdSessionPerfGroup,
       "bfdSessionPerfHCGroup": bfdSessionPerfHCGroup,
       "bfdNotificationGroup": bfdNotificationGroup,
       "bfdCompliances": bfdCompliances,
       "bfdModuleFullCompliance": bfdModuleFullCompliance}
)
