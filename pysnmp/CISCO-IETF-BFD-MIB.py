# SNMP MIB module (CISCO-IETF-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:27 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoIetfBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137)
)
ciscoIetfBfdMIB.setRevisions(
        ("2011-03-14 00:00",
         "2010-02-18 00:00",
         "2008-04-24 00:00",
         "2007-06-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoBfdSessIndexTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CiscoBfdInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CiscoBfdDiag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("administrativelyDown", 7),
          ("concatenatedPathDown", 6),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("forwardingPlaneReset", 4),
          ("neighborSignaledSessionDown", 3),
          ("noDiagnostic", 0),
          ("pathDown", 5),
          ("reverseConcatenatedPathDown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBfdNotifications_ObjectIdentity = ObjectIdentity
ciscoBfdNotifications = _CiscoBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 0)
)
_CiscoBfdObjects_ObjectIdentity = ObjectIdentity
ciscoBfdObjects = _CiscoBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1)
)
_CiscoBfdScalarObjects_ObjectIdentity = ObjectIdentity
ciscoBfdScalarObjects = _CiscoBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 1)
)


class _CiscoBfdAdminStatus_Type(Integer32):
    """Custom type ciscoBfdAdminStatus based on Integer32"""
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


_CiscoBfdAdminStatus_Type.__name__ = "Integer32"
_CiscoBfdAdminStatus_Object = MibScalar
ciscoBfdAdminStatus = _CiscoBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 1, 1),
    _CiscoBfdAdminStatus_Type()
)
ciscoBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoBfdAdminStatus.setStatus("current")


class _CiscoBfdVersionNumber_Type(Unsigned32):
    """Custom type ciscoBfdVersionNumber based on Unsigned32"""
    defaultValue = 0


_CiscoBfdVersionNumber_Object = MibScalar
ciscoBfdVersionNumber = _CiscoBfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 1, 3),
    _CiscoBfdVersionNumber_Type()
)
ciscoBfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdVersionNumber.setStatus("current")


class _CiscoBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type ciscoBfdSessNotificationsEnable based on TruthValue"""


_CiscoBfdSessNotificationsEnable_Object = MibScalar
ciscoBfdSessNotificationsEnable = _CiscoBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 1, 4),
    _CiscoBfdSessNotificationsEnable_Type()
)
ciscoBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoBfdSessNotificationsEnable.setStatus("current")
_CiscoBfdSessTable_Object = MibTable
ciscoBfdSessTable = _CiscoBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoBfdSessTable.setStatus("current")
_CiscoBfdSessEntry_Object = MibTableRow
ciscoBfdSessEntry = _CiscoBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1)
)
ciscoBfdSessEntry.setIndexNames(
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessIndex"),
)
if mibBuilder.loadTexts:
    ciscoBfdSessEntry.setStatus("current")
_CiscoBfdSessIndex_Type = CiscoBfdSessIndexTC
_CiscoBfdSessIndex_Object = MibTableColumn
ciscoBfdSessIndex = _CiscoBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 1),
    _CiscoBfdSessIndex_Type()
)
ciscoBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoBfdSessIndex.setStatus("current")
_CiscoBfdSessApplicationId_Type = Unsigned32
_CiscoBfdSessApplicationId_Object = MibTableColumn
ciscoBfdSessApplicationId = _CiscoBfdSessApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 2),
    _CiscoBfdSessApplicationId_Type()
)
ciscoBfdSessApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessApplicationId.setStatus("current")


class _CiscoBfdSessDiscriminator_Type(Unsigned32):
    """Custom type ciscoBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_CiscoBfdSessDiscriminator_Object = MibTableColumn
ciscoBfdSessDiscriminator = _CiscoBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 3),
    _CiscoBfdSessDiscriminator_Type()
)
ciscoBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessDiscriminator.setStatus("current")


class _CiscoBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type ciscoBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiscoBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_CiscoBfdSessRemoteDiscr_Object = MibTableColumn
ciscoBfdSessRemoteDiscr = _CiscoBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 4),
    _CiscoBfdSessRemoteDiscr_Type()
)
ciscoBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessRemoteDiscr.setStatus("current")


class _CiscoBfdSessUdpPort_Type(InetPortNumber):
    """Custom type ciscoBfdSessUdpPort based on InetPortNumber"""
    defaultValue = 0


_CiscoBfdSessUdpPort_Object = MibTableColumn
ciscoBfdSessUdpPort = _CiscoBfdSessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 5),
    _CiscoBfdSessUdpPort_Type()
)
ciscoBfdSessUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessUdpPort.setStatus("current")


class _CiscoBfdSessState_Type(Integer32):
    """Custom type ciscoBfdSessState based on Integer32"""
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
        *(("adminDown", 1),
          ("down", 2),
          ("failing", 5),
          ("init", 3),
          ("up", 4))
    )


_CiscoBfdSessState_Type.__name__ = "Integer32"
_CiscoBfdSessState_Object = MibTableColumn
ciscoBfdSessState = _CiscoBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 6),
    _CiscoBfdSessState_Type()
)
ciscoBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessState.setStatus("current")
_CiscoBfdSessRemoteHeardFlag_Type = TruthValue
_CiscoBfdSessRemoteHeardFlag_Object = MibTableColumn
ciscoBfdSessRemoteHeardFlag = _CiscoBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 7),
    _CiscoBfdSessRemoteHeardFlag_Type()
)
ciscoBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessRemoteHeardFlag.setStatus("current")
_CiscoBfdSessDiag_Type = CiscoBfdDiag
_CiscoBfdSessDiag_Object = MibTableColumn
ciscoBfdSessDiag = _CiscoBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 8),
    _CiscoBfdSessDiag_Type()
)
ciscoBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessDiag.setStatus("current")


class _CiscoBfdSessOperMode_Type(Integer32):
    """Custom type ciscoBfdSessOperMode based on Integer32"""
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


_CiscoBfdSessOperMode_Type.__name__ = "Integer32"
_CiscoBfdSessOperMode_Object = MibTableColumn
ciscoBfdSessOperMode = _CiscoBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 9),
    _CiscoBfdSessOperMode_Type()
)
ciscoBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessOperMode.setStatus("current")


class _CiscoBfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type ciscoBfdSessDemandModeDesiredFlag based on TruthValue"""


_CiscoBfdSessDemandModeDesiredFlag_Object = MibTableColumn
ciscoBfdSessDemandModeDesiredFlag = _CiscoBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 10),
    _CiscoBfdSessDemandModeDesiredFlag_Type()
)
ciscoBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessDemandModeDesiredFlag.setStatus("current")


class _CiscoBfdSessEchoFuncModeDesiredFlag_Type(TruthValue):
    """Custom type ciscoBfdSessEchoFuncModeDesiredFlag based on TruthValue"""


_CiscoBfdSessEchoFuncModeDesiredFlag_Object = MibTableColumn
ciscoBfdSessEchoFuncModeDesiredFlag = _CiscoBfdSessEchoFuncModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 11),
    _CiscoBfdSessEchoFuncModeDesiredFlag_Type()
)
ciscoBfdSessEchoFuncModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessEchoFuncModeDesiredFlag.setStatus("current")


class _CiscoBfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type ciscoBfdSessControlPlanIndepFlag based on TruthValue"""


_CiscoBfdSessControlPlanIndepFlag_Object = MibTableColumn
ciscoBfdSessControlPlanIndepFlag = _CiscoBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 12),
    _CiscoBfdSessControlPlanIndepFlag_Type()
)
ciscoBfdSessControlPlanIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessControlPlanIndepFlag.setStatus("current")
_CiscoBfdSessAddrType_Type = InetAddressType
_CiscoBfdSessAddrType_Object = MibTableColumn
ciscoBfdSessAddrType = _CiscoBfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 13),
    _CiscoBfdSessAddrType_Type()
)
ciscoBfdSessAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessAddrType.setStatus("current")
_CiscoBfdSessAddr_Type = InetAddress
_CiscoBfdSessAddr_Object = MibTableColumn
ciscoBfdSessAddr = _CiscoBfdSessAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 14),
    _CiscoBfdSessAddr_Type()
)
ciscoBfdSessAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessAddr.setStatus("current")
_CiscoBfdSessDesiredMinTxInterval_Type = CiscoBfdInterval
_CiscoBfdSessDesiredMinTxInterval_Object = MibTableColumn
ciscoBfdSessDesiredMinTxInterval = _CiscoBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 15),
    _CiscoBfdSessDesiredMinTxInterval_Type()
)
ciscoBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessDesiredMinTxInterval.setStatus("current")
_CiscoBfdSessReqMinRxInterval_Type = CiscoBfdInterval
_CiscoBfdSessReqMinRxInterval_Object = MibTableColumn
ciscoBfdSessReqMinRxInterval = _CiscoBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 16),
    _CiscoBfdSessReqMinRxInterval_Type()
)
ciscoBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessReqMinRxInterval.setStatus("current")
_CiscoBfdSessReqMinEchoRxInterval_Type = CiscoBfdInterval
_CiscoBfdSessReqMinEchoRxInterval_Object = MibTableColumn
ciscoBfdSessReqMinEchoRxInterval = _CiscoBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 17),
    _CiscoBfdSessReqMinEchoRxInterval_Type()
)
ciscoBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessReqMinEchoRxInterval.setStatus("current")
_CiscoBfdSessDetectMult_Type = Unsigned32
_CiscoBfdSessDetectMult_Object = MibTableColumn
ciscoBfdSessDetectMult = _CiscoBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 18),
    _CiscoBfdSessDetectMult_Type()
)
ciscoBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessDetectMult.setStatus("current")
_CiscoBfdSessStorType_Type = StorageType
_CiscoBfdSessStorType_Object = MibTableColumn
ciscoBfdSessStorType = _CiscoBfdSessStorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 19),
    _CiscoBfdSessStorType_Type()
)
ciscoBfdSessStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessStorType.setStatus("current")
_CiscoBfdSessRowStatus_Type = RowStatus
_CiscoBfdSessRowStatus_Object = MibTableColumn
ciscoBfdSessRowStatus = _CiscoBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 20),
    _CiscoBfdSessRowStatus_Type()
)
ciscoBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessRowStatus.setStatus("current")


class _CiscoBfdSessAuthPresFlag_Type(TruthValue):
    """Custom type ciscoBfdSessAuthPresFlag based on TruthValue"""


_CiscoBfdSessAuthPresFlag_Object = MibTableColumn
ciscoBfdSessAuthPresFlag = _CiscoBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 21),
    _CiscoBfdSessAuthPresFlag_Type()
)
ciscoBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessAuthPresFlag.setStatus("current")


class _CiscoBfdSessAuthenticationType_Type(Integer32):
    """Custom type ciscoBfdSessAuthenticationType based on Integer32"""
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


_CiscoBfdSessAuthenticationType_Type.__name__ = "Integer32"
_CiscoBfdSessAuthenticationType_Object = MibTableColumn
ciscoBfdSessAuthenticationType = _CiscoBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 22),
    _CiscoBfdSessAuthenticationType_Type()
)
ciscoBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoBfdSessAuthenticationType.setStatus("current")


class _CiscoBfdSessVersionNumber_Type(Unsigned32):
    """Custom type ciscoBfdSessVersionNumber based on Unsigned32"""
    defaultValue = 0


_CiscoBfdSessVersionNumber_Object = MibTableColumn
ciscoBfdSessVersionNumber = _CiscoBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 23),
    _CiscoBfdSessVersionNumber_Type()
)
ciscoBfdSessVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessVersionNumber.setStatus("current")


class _CiscoBfdSessType_Type(Integer32):
    """Custom type ciscoBfdSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiHop", 2),
          ("singleHop", 1))
    )


_CiscoBfdSessType_Type.__name__ = "Integer32"
_CiscoBfdSessType_Object = MibTableColumn
ciscoBfdSessType = _CiscoBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 24),
    _CiscoBfdSessType_Type()
)
ciscoBfdSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessType.setStatus("current")
_CiscoBfdSessInterface_Type = InterfaceIndex
_CiscoBfdSessInterface_Object = MibTableColumn
ciscoBfdSessInterface = _CiscoBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 2, 1, 25),
    _CiscoBfdSessInterface_Type()
)
ciscoBfdSessInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessInterface.setStatus("current")
_CiscoBfdSessPerfTable_Object = MibTable
ciscoBfdSessPerfTable = _CiscoBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoBfdSessPerfTable.setStatus("current")
_CiscoBfdSessPerfEntry_Object = MibTableRow
ciscoBfdSessPerfEntry = _CiscoBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoBfdSessPerfEntry.setStatus("current")
_CiscoBfdSessPerfPktIn_Type = Counter32
_CiscoBfdSessPerfPktIn_Object = MibTableColumn
ciscoBfdSessPerfPktIn = _CiscoBfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 1),
    _CiscoBfdSessPerfPktIn_Type()
)
ciscoBfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfPktIn.setStatus("current")
_CiscoBfdSessPerfPktOut_Type = Counter32
_CiscoBfdSessPerfPktOut_Object = MibTableColumn
ciscoBfdSessPerfPktOut = _CiscoBfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 2),
    _CiscoBfdSessPerfPktOut_Type()
)
ciscoBfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfPktOut.setStatus("current")
_CiscoBfdSessUpTime_Type = TimeStamp
_CiscoBfdSessUpTime_Object = MibTableColumn
ciscoBfdSessUpTime = _CiscoBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 3),
    _CiscoBfdSessUpTime_Type()
)
ciscoBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessUpTime.setStatus("current")
_CiscoBfdSessPerfLastSessDownTime_Type = TimeStamp
_CiscoBfdSessPerfLastSessDownTime_Object = MibTableColumn
ciscoBfdSessPerfLastSessDownTime = _CiscoBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 4),
    _CiscoBfdSessPerfLastSessDownTime_Type()
)
ciscoBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfLastSessDownTime.setStatus("current")
_CiscoBfdSessPerfLastCommLostDiag_Type = CiscoBfdDiag
_CiscoBfdSessPerfLastCommLostDiag_Object = MibTableColumn
ciscoBfdSessPerfLastCommLostDiag = _CiscoBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 5),
    _CiscoBfdSessPerfLastCommLostDiag_Type()
)
ciscoBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfLastCommLostDiag.setStatus("current")
_CiscoBfdSessPerfSessUpCount_Type = Counter32
_CiscoBfdSessPerfSessUpCount_Object = MibTableColumn
ciscoBfdSessPerfSessUpCount = _CiscoBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 6),
    _CiscoBfdSessPerfSessUpCount_Type()
)
ciscoBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfSessUpCount.setStatus("current")
_CiscoBfdSessPerfDiscTime_Type = TimeStamp
_CiscoBfdSessPerfDiscTime_Object = MibTableColumn
ciscoBfdSessPerfDiscTime = _CiscoBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 7),
    _CiscoBfdSessPerfDiscTime_Type()
)
ciscoBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfDiscTime.setStatus("current")
_CiscoBfdSessPerfPktInHC_Type = Counter64
_CiscoBfdSessPerfPktInHC_Object = MibTableColumn
ciscoBfdSessPerfPktInHC = _CiscoBfdSessPerfPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 8),
    _CiscoBfdSessPerfPktInHC_Type()
)
ciscoBfdSessPerfPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfPktInHC.setStatus("current")
_CiscoBfdSessPerfPktOutHC_Type = Counter64
_CiscoBfdSessPerfPktOutHC_Object = MibTableColumn
ciscoBfdSessPerfPktOutHC = _CiscoBfdSessPerfPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 3, 1, 9),
    _CiscoBfdSessPerfPktOutHC_Type()
)
ciscoBfdSessPerfPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessPerfPktOutHC.setStatus("current")
_CiscoBfdSessMapTable_Object = MibTable
ciscoBfdSessMapTable = _CiscoBfdSessMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoBfdSessMapTable.setStatus("current")
_CiscoBfdSessMapEntry_Object = MibTableRow
ciscoBfdSessMapEntry = _CiscoBfdSessMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 4, 1)
)
ciscoBfdSessMapEntry.setIndexNames(
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessApplicationId"),
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessDiscriminator"),
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessAddrType"),
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessAddr"),
)
if mibBuilder.loadTexts:
    ciscoBfdSessMapEntry.setStatus("current")
_CiscoBfdSessMapBfdIndex_Type = CiscoBfdSessIndexTC
_CiscoBfdSessMapBfdIndex_Object = MibTableColumn
ciscoBfdSessMapBfdIndex = _CiscoBfdSessMapBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 4, 1, 1),
    _CiscoBfdSessMapBfdIndex_Type()
)
ciscoBfdSessMapBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessMapBfdIndex.setStatus("current")
_CiscoBfdSessDiscMapTable_Object = MibTable
ciscoBfdSessDiscMapTable = _CiscoBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoBfdSessDiscMapTable.setStatus("current")
_CiscoBfdSessDiscMapEntry_Object = MibTableRow
ciscoBfdSessDiscMapEntry = _CiscoBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 5, 1)
)
ciscoBfdSessDiscMapEntry.setIndexNames(
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    ciscoBfdSessDiscMapEntry.setStatus("current")
_CiscoBfdSessDiscMapIndex_Type = CiscoBfdSessIndexTC
_CiscoBfdSessDiscMapIndex_Object = MibTableColumn
ciscoBfdSessDiscMapIndex = _CiscoBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 5, 1, 1),
    _CiscoBfdSessDiscMapIndex_Type()
)
ciscoBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessDiscMapIndex.setStatus("current")
_CiscoBfdSessIpMapTable_Object = MibTable
ciscoBfdSessIpMapTable = _CiscoBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoBfdSessIpMapTable.setStatus("current")
_CiscoBfdSessIpMapEntry_Object = MibTableRow
ciscoBfdSessIpMapEntry = _CiscoBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 6, 1)
)
ciscoBfdSessIpMapEntry.setIndexNames(
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessInterface"),
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessAddrType"),
    (0, "CISCO-IETF-BFD-MIB", "ciscoBfdSessAddr"),
)
if mibBuilder.loadTexts:
    ciscoBfdSessIpMapEntry.setStatus("current")
_CiscoBfdSessIpMapIndex_Type = CiscoBfdSessIndexTC
_CiscoBfdSessIpMapIndex_Object = MibTableColumn
ciscoBfdSessIpMapIndex = _CiscoBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 1, 6, 1, 1),
    _CiscoBfdSessIpMapIndex_Type()
)
ciscoBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBfdSessIpMapIndex.setStatus("current")
_CiscoBfdConformance_ObjectIdentity = ObjectIdentity
ciscoBfdConformance = _CiscoBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3)
)
_CiscoBfdGroups_ObjectIdentity = ObjectIdentity
ciscoBfdGroups = _CiscoBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1)
)
_CiscoBfdCompliances_ObjectIdentity = ObjectIdentity
ciscoBfdCompliances = _CiscoBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 2)
)
ciscoBfdSessEntry.registerAugmentions(
    ("CISCO-IETF-BFD-MIB",
     "ciscoBfdSessPerfEntry")
)
ciscoBfdSessPerfEntry.setIndexNames(*ciscoBfdSessEntry.getIndexNames())

# Managed Objects groups

ciscoBfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 1)
)
ciscoBfdSessionGroup.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessNotificationsEnable"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdAdminStatus"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdVersionNumber"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessApplicationId"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiscriminator"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAddrType"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAddr"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRemoteDiscr"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessUdpPort"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessState"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRemoteHeardFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessOperMode"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDemandModeDesiredFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessEchoFuncModeDesiredFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessControlPlanIndepFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDesiredMinTxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessReqMinRxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessReqMinEchoRxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDetectMult"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessStorType"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRowStatus"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessMapBfdIndex"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAuthPresFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAuthenticationType"))
)
if mibBuilder.loadTexts:
    ciscoBfdSessionGroup.setStatus("deprecated")

ciscoBfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 2)
)
ciscoBfdSessionPerfGroup.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfPktIn"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfPktOut"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessUpTime"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfLastSessDownTime"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfLastCommLostDiag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfSessUpCount"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    ciscoBfdSessionPerfGroup.setStatus("current")

ciscoBfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 3)
)
ciscoBfdSessionPerfHCGroup.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfPktInHC"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessPerfPktOutHC"))
)
if mibBuilder.loadTexts:
    ciscoBfdSessionPerfHCGroup.setStatus("current")

ciscoBfdSession0304Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 5)
)
ciscoBfdSession0304Group.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessNotificationsEnable"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdAdminStatus"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiscriminator"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAddrType"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAddr"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRemoteDiscr"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessUdpPort"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessState"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRemoteHeardFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessOperMode"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDemandModeDesiredFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessEchoFuncModeDesiredFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessControlPlanIndepFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDesiredMinTxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessReqMinRxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessReqMinEchoRxInterval"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDetectMult"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessStorType"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessRowStatus"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAuthPresFlag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessAuthenticationType"))
)
if mibBuilder.loadTexts:
    ciscoBfdSession0304Group.setStatus("current")

ciscoBfdSession03Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 6)
)
ciscoBfdSession03Group.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdVersionNumber"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessApplicationId"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessMapBfdIndex"))
)
if mibBuilder.loadTexts:
    ciscoBfdSession03Group.setStatus("current")

ciscoBfdSession04Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 7)
)
ciscoBfdSession04Group.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessVersionNumber"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessType"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessInterface"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiscMapIndex"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    ciscoBfdSession04Group.setStatus("current")


# Notification objects

ciscoBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 0, 1)
)
ciscoBfdSessUp.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"))
)
if mibBuilder.loadTexts:
    ciscoBfdSessUp.setStatus(
        "current"
    )

ciscoBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 0, 2)
)
ciscoBfdSessDown.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDiag"))
)
if mibBuilder.loadTexts:
    ciscoBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

ciscoBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 1, 4)
)
ciscoBfdNotificationGroup.setObjects(
      *(("CISCO-IETF-BFD-MIB", "ciscoBfdSessUp"),
        ("CISCO-IETF-BFD-MIB", "ciscoBfdSessDown"))
)
if mibBuilder.loadTexts:
    ciscoBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoBfdModuleFullCompliance.setStatus(
        "deprecated"
    )

ciscoBfdModuleFullComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 137, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoBfdModuleFullComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-BFD-MIB",
    **{"CiscoBfdSessIndexTC": CiscoBfdSessIndexTC,
       "CiscoBfdInterval": CiscoBfdInterval,
       "CiscoBfdDiag": CiscoBfdDiag,
       "ciscoIetfBfdMIB": ciscoIetfBfdMIB,
       "ciscoBfdNotifications": ciscoBfdNotifications,
       "ciscoBfdSessUp": ciscoBfdSessUp,
       "ciscoBfdSessDown": ciscoBfdSessDown,
       "ciscoBfdObjects": ciscoBfdObjects,
       "ciscoBfdScalarObjects": ciscoBfdScalarObjects,
       "ciscoBfdAdminStatus": ciscoBfdAdminStatus,
       "ciscoBfdVersionNumber": ciscoBfdVersionNumber,
       "ciscoBfdSessNotificationsEnable": ciscoBfdSessNotificationsEnable,
       "ciscoBfdSessTable": ciscoBfdSessTable,
       "ciscoBfdSessEntry": ciscoBfdSessEntry,
       "ciscoBfdSessIndex": ciscoBfdSessIndex,
       "ciscoBfdSessApplicationId": ciscoBfdSessApplicationId,
       "ciscoBfdSessDiscriminator": ciscoBfdSessDiscriminator,
       "ciscoBfdSessRemoteDiscr": ciscoBfdSessRemoteDiscr,
       "ciscoBfdSessUdpPort": ciscoBfdSessUdpPort,
       "ciscoBfdSessState": ciscoBfdSessState,
       "ciscoBfdSessRemoteHeardFlag": ciscoBfdSessRemoteHeardFlag,
       "ciscoBfdSessDiag": ciscoBfdSessDiag,
       "ciscoBfdSessOperMode": ciscoBfdSessOperMode,
       "ciscoBfdSessDemandModeDesiredFlag": ciscoBfdSessDemandModeDesiredFlag,
       "ciscoBfdSessEchoFuncModeDesiredFlag": ciscoBfdSessEchoFuncModeDesiredFlag,
       "ciscoBfdSessControlPlanIndepFlag": ciscoBfdSessControlPlanIndepFlag,
       "ciscoBfdSessAddrType": ciscoBfdSessAddrType,
       "ciscoBfdSessAddr": ciscoBfdSessAddr,
       "ciscoBfdSessDesiredMinTxInterval": ciscoBfdSessDesiredMinTxInterval,
       "ciscoBfdSessReqMinRxInterval": ciscoBfdSessReqMinRxInterval,
       "ciscoBfdSessReqMinEchoRxInterval": ciscoBfdSessReqMinEchoRxInterval,
       "ciscoBfdSessDetectMult": ciscoBfdSessDetectMult,
       "ciscoBfdSessStorType": ciscoBfdSessStorType,
       "ciscoBfdSessRowStatus": ciscoBfdSessRowStatus,
       "ciscoBfdSessAuthPresFlag": ciscoBfdSessAuthPresFlag,
       "ciscoBfdSessAuthenticationType": ciscoBfdSessAuthenticationType,
       "ciscoBfdSessVersionNumber": ciscoBfdSessVersionNumber,
       "ciscoBfdSessType": ciscoBfdSessType,
       "ciscoBfdSessInterface": ciscoBfdSessInterface,
       "ciscoBfdSessPerfTable": ciscoBfdSessPerfTable,
       "ciscoBfdSessPerfEntry": ciscoBfdSessPerfEntry,
       "ciscoBfdSessPerfPktIn": ciscoBfdSessPerfPktIn,
       "ciscoBfdSessPerfPktOut": ciscoBfdSessPerfPktOut,
       "ciscoBfdSessUpTime": ciscoBfdSessUpTime,
       "ciscoBfdSessPerfLastSessDownTime": ciscoBfdSessPerfLastSessDownTime,
       "ciscoBfdSessPerfLastCommLostDiag": ciscoBfdSessPerfLastCommLostDiag,
       "ciscoBfdSessPerfSessUpCount": ciscoBfdSessPerfSessUpCount,
       "ciscoBfdSessPerfDiscTime": ciscoBfdSessPerfDiscTime,
       "ciscoBfdSessPerfPktInHC": ciscoBfdSessPerfPktInHC,
       "ciscoBfdSessPerfPktOutHC": ciscoBfdSessPerfPktOutHC,
       "ciscoBfdSessMapTable": ciscoBfdSessMapTable,
       "ciscoBfdSessMapEntry": ciscoBfdSessMapEntry,
       "ciscoBfdSessMapBfdIndex": ciscoBfdSessMapBfdIndex,
       "ciscoBfdSessDiscMapTable": ciscoBfdSessDiscMapTable,
       "ciscoBfdSessDiscMapEntry": ciscoBfdSessDiscMapEntry,
       "ciscoBfdSessDiscMapIndex": ciscoBfdSessDiscMapIndex,
       "ciscoBfdSessIpMapTable": ciscoBfdSessIpMapTable,
       "ciscoBfdSessIpMapEntry": ciscoBfdSessIpMapEntry,
       "ciscoBfdSessIpMapIndex": ciscoBfdSessIpMapIndex,
       "ciscoBfdConformance": ciscoBfdConformance,
       "ciscoBfdGroups": ciscoBfdGroups,
       "ciscoBfdSessionGroup": ciscoBfdSessionGroup,
       "ciscoBfdSessionPerfGroup": ciscoBfdSessionPerfGroup,
       "ciscoBfdSessionPerfHCGroup": ciscoBfdSessionPerfHCGroup,
       "ciscoBfdNotificationGroup": ciscoBfdNotificationGroup,
       "ciscoBfdSession0304Group": ciscoBfdSession0304Group,
       "ciscoBfdSession03Group": ciscoBfdSession03Group,
       "ciscoBfdSession04Group": ciscoBfdSession04Group,
       "ciscoBfdCompliances": ciscoBfdCompliances,
       "ciscoBfdModuleFullCompliance": ciscoBfdModuleFullCompliance,
       "ciscoBfdModuleFullComplianceRev2": ciscoBfdModuleFullComplianceRev2}
)
