# SNMP MIB module (BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BFD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:10 2024
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

(BfdCtrlDestPortNumberTC,
 BfdCtrlSourcePortNumberTC,
 BfdIntervalTC,
 BfdMultiplierTC,
 BfdSessIndexTC) = mibBuilder.importSymbols(
    "BFD-TC-STD-MIB",
    "BfdCtrlDestPortNumberTC",
    "BfdCtrlSourcePortNumberTC",
    "BfdIntervalTC",
    "BfdMultiplierTC",
    "BfdSessIndexTC")

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "IndexIntegerNextFree")

(IANAbfdDiagTC,
 IANAbfdSessAuthenticationKeyTC,
 IANAbfdSessAuthenticationTypeTC,
 IANAbfdSessOperModeTC,
 IANAbfdSessStateTC,
 IANAbfdSessTypeTC) = mibBuilder.importSymbols(
    "IANA-BFD-TC-STD-MIB",
    "IANAbfdDiagTC",
    "IANAbfdSessAuthenticationKeyTC",
    "IANAbfdSessAuthenticationTypeTC",
    "IANAbfdSessOperModeTC",
    "IANAbfdSessStateTC",
    "IANAbfdSessTypeTC")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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
    (1, 3, 6, 1, 2, 1, 222)
)
bfdMIB.setRevisions(
        ("2014-08-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BfdNotifications_ObjectIdentity = ObjectIdentity
bfdNotifications = _BfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 0)
)
_BfdObjects_ObjectIdentity = ObjectIdentity
bfdObjects = _BfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 1)
)
_BfdScalarObjects_ObjectIdentity = ObjectIdentity
bfdScalarObjects = _BfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 1, 1)
)


class _BfdAdminStatus_Type(Integer32):
    """Custom type bfdAdminStatus based on Integer32"""
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
        *(("adminDown", 3),
          ("disabled", 2),
          ("down", 4),
          ("enabled", 1))
    )


_BfdAdminStatus_Type.__name__ = "Integer32"
_BfdAdminStatus_Object = MibScalar
bfdAdminStatus = _BfdAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 1, 1),
    _BfdAdminStatus_Type()
)
bfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdAdminStatus.setStatus("current")


class _BfdOperStatus_Type(Integer32):
    """Custom type bfdOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 3),
          ("down", 2),
          ("up", 1))
    )


_BfdOperStatus_Type.__name__ = "Integer32"
_BfdOperStatus_Object = MibScalar
bfdOperStatus = _BfdOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 1, 2),
    _BfdOperStatus_Type()
)
bfdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdOperStatus.setStatus("current")


class _BfdNotificationsEnable_Type(TruthValue):
    """Custom type bfdNotificationsEnable based on TruthValue"""


_BfdNotificationsEnable_Object = MibScalar
bfdNotificationsEnable = _BfdNotificationsEnable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 1, 3),
    _BfdNotificationsEnable_Type()
)
bfdNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdNotificationsEnable.setStatus("current")


class _BfdSessIndexNext_Type(IndexIntegerNextFree):
    """Custom type bfdSessIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BfdSessIndexNext_Type.__name__ = "IndexIntegerNextFree"
_BfdSessIndexNext_Object = MibScalar
bfdSessIndexNext = _BfdSessIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 1, 4),
    _BfdSessIndexNext_Type()
)
bfdSessIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessIndexNext.setStatus("current")
_BfdSessTable_Object = MibTable
bfdSessTable = _BfdSessTable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2)
)
if mibBuilder.loadTexts:
    bfdSessTable.setStatus("current")
_BfdSessEntry_Object = MibTableRow
bfdSessEntry = _BfdSessEntry_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1)
)
bfdSessEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessIndex"),
)
if mibBuilder.loadTexts:
    bfdSessEntry.setStatus("current")
_BfdSessIndex_Type = BfdSessIndexTC
_BfdSessIndex_Object = MibTableColumn
bfdSessIndex = _BfdSessIndex_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 1),
    _BfdSessIndex_Type()
)
bfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfdSessIndex.setStatus("current")


class _BfdSessVersionNumber_Type(Unsigned32):
    """Custom type bfdSessVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BfdSessVersionNumber_Type.__name__ = "Unsigned32"
_BfdSessVersionNumber_Object = MibTableColumn
bfdSessVersionNumber = _BfdSessVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 2),
    _BfdSessVersionNumber_Type()
)
bfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessVersionNumber.setStatus("current")
_BfdSessType_Type = IANAbfdSessTypeTC
_BfdSessType_Object = MibTableColumn
bfdSessType = _BfdSessType_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 3),
    _BfdSessType_Type()
)
bfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessType.setStatus("current")


class _BfdSessDiscriminator_Type(Unsigned32):
    """Custom type bfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BfdSessDiscriminator_Type.__name__ = "Unsigned32"
_BfdSessDiscriminator_Object = MibTableColumn
bfdSessDiscriminator = _BfdSessDiscriminator_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 4),
    _BfdSessDiscriminator_Type()
)
bfdSessDiscriminator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDiscriminator.setStatus("current")


class _BfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type bfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_BfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_BfdSessRemoteDiscr_Object = MibTableColumn
bfdSessRemoteDiscr = _BfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 5),
    _BfdSessRemoteDiscr_Type()
)
bfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessRemoteDiscr.setStatus("current")


class _BfdSessDestinationUdpPort_Type(BfdCtrlDestPortNumberTC):
    """Custom type bfdSessDestinationUdpPort based on BfdCtrlDestPortNumberTC"""
    defaultValue = 0


_BfdSessDestinationUdpPort_Object = MibTableColumn
bfdSessDestinationUdpPort = _BfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 6),
    _BfdSessDestinationUdpPort_Type()
)
bfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDestinationUdpPort.setStatus("current")


class _BfdSessSourceUdpPort_Type(BfdCtrlSourcePortNumberTC):
    """Custom type bfdSessSourceUdpPort based on BfdCtrlSourcePortNumberTC"""
    defaultValue = 0


_BfdSessSourceUdpPort_Object = MibTableColumn
bfdSessSourceUdpPort = _BfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 7),
    _BfdSessSourceUdpPort_Type()
)
bfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessSourceUdpPort.setStatus("current")


class _BfdSessEchoSourceUdpPort_Type(InetPortNumber):
    """Custom type bfdSessEchoSourceUdpPort based on InetPortNumber"""
    defaultValue = 0


_BfdSessEchoSourceUdpPort_Object = MibTableColumn
bfdSessEchoSourceUdpPort = _BfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 8),
    _BfdSessEchoSourceUdpPort_Type()
)
bfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessEchoSourceUdpPort.setStatus("current")


class _BfdSessAdminStatus_Type(Integer32):
    """Custom type bfdSessAdminStatus based on Integer32"""
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
        *(("adminDown", 3),
          ("disabled", 2),
          ("down", 4),
          ("enabled", 1))
    )


_BfdSessAdminStatus_Type.__name__ = "Integer32"
_BfdSessAdminStatus_Object = MibTableColumn
bfdSessAdminStatus = _BfdSessAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 9),
    _BfdSessAdminStatus_Type()
)
bfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAdminStatus.setStatus("current")


class _BfdSessOperStatus_Type(Integer32):
    """Custom type bfdSessOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 3),
          ("down", 2),
          ("up", 1))
    )


_BfdSessOperStatus_Type.__name__ = "Integer32"
_BfdSessOperStatus_Object = MibTableColumn
bfdSessOperStatus = _BfdSessOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 10),
    _BfdSessOperStatus_Type()
)
bfdSessOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessOperStatus.setStatus("current")
_BfdSessState_Type = IANAbfdSessStateTC
_BfdSessState_Object = MibTableColumn
bfdSessState = _BfdSessState_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 11),
    _BfdSessState_Type()
)
bfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessState.setStatus("current")
_BfdSessRemoteHeardFlag_Type = TruthValue
_BfdSessRemoteHeardFlag_Object = MibTableColumn
bfdSessRemoteHeardFlag = _BfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 12),
    _BfdSessRemoteHeardFlag_Type()
)
bfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessRemoteHeardFlag.setStatus("current")
_BfdSessDiag_Type = IANAbfdDiagTC
_BfdSessDiag_Object = MibTableColumn
bfdSessDiag = _BfdSessDiag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 13),
    _BfdSessDiag_Type()
)
bfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessDiag.setStatus("current")
_BfdSessOperMode_Type = IANAbfdSessOperModeTC
_BfdSessOperMode_Object = MibTableColumn
bfdSessOperMode = _BfdSessOperMode_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 14),
    _BfdSessOperMode_Type()
)
bfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessOperMode.setStatus("current")


class _BfdSessDemandModeDesiredFlag_Type(TruthValue):
    """Custom type bfdSessDemandModeDesiredFlag based on TruthValue"""


_BfdSessDemandModeDesiredFlag_Object = MibTableColumn
bfdSessDemandModeDesiredFlag = _BfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 15),
    _BfdSessDemandModeDesiredFlag_Type()
)
bfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDemandModeDesiredFlag.setStatus("current")


class _BfdSessControlPlaneIndepFlag_Type(TruthValue):
    """Custom type bfdSessControlPlaneIndepFlag based on TruthValue"""


_BfdSessControlPlaneIndepFlag_Object = MibTableColumn
bfdSessControlPlaneIndepFlag = _BfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 16),
    _BfdSessControlPlaneIndepFlag_Type()
)
bfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessControlPlaneIndepFlag.setStatus("current")


class _BfdSessMultipointFlag_Type(TruthValue):
    """Custom type bfdSessMultipointFlag based on TruthValue"""


_BfdSessMultipointFlag_Object = MibTableColumn
bfdSessMultipointFlag = _BfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 17),
    _BfdSessMultipointFlag_Type()
)
bfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessMultipointFlag.setStatus("current")
_BfdSessInterface_Type = InterfaceIndexOrZero
_BfdSessInterface_Object = MibTableColumn
bfdSessInterface = _BfdSessInterface_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 18),
    _BfdSessInterface_Type()
)
bfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessInterface.setStatus("current")
_BfdSessSrcAddrType_Type = InetAddressType
_BfdSessSrcAddrType_Object = MibTableColumn
bfdSessSrcAddrType = _BfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 19),
    _BfdSessSrcAddrType_Type()
)
bfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessSrcAddrType.setStatus("current")


class _BfdSessSrcAddr_Type(InetAddress):
    """Custom type bfdSessSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BfdSessSrcAddr_Type.__name__ = "InetAddress"
_BfdSessSrcAddr_Object = MibTableColumn
bfdSessSrcAddr = _BfdSessSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 20),
    _BfdSessSrcAddr_Type()
)
bfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessSrcAddr.setStatus("current")
_BfdSessDstAddrType_Type = InetAddressType
_BfdSessDstAddrType_Object = MibTableColumn
bfdSessDstAddrType = _BfdSessDstAddrType_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 21),
    _BfdSessDstAddrType_Type()
)
bfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDstAddrType.setStatus("current")


class _BfdSessDstAddr_Type(InetAddress):
    """Custom type bfdSessDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BfdSessDstAddr_Type.__name__ = "InetAddress"
_BfdSessDstAddr_Object = MibTableColumn
bfdSessDstAddr = _BfdSessDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 22),
    _BfdSessDstAddr_Type()
)
bfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDstAddr.setStatus("current")


class _BfdSessGTSM_Type(TruthValue):
    """Custom type bfdSessGTSM based on TruthValue"""


_BfdSessGTSM_Object = MibTableColumn
bfdSessGTSM = _BfdSessGTSM_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 23),
    _BfdSessGTSM_Type()
)
bfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessGTSM.setStatus("current")


class _BfdSessGTSMTTL_Type(Unsigned32):
    """Custom type bfdSessGTSMTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_BfdSessGTSMTTL_Object = MibTableColumn
bfdSessGTSMTTL = _BfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 24),
    _BfdSessGTSMTTL_Type()
)
bfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessGTSMTTL.setStatus("current")
_BfdSessDesiredMinTxInterval_Type = BfdIntervalTC
_BfdSessDesiredMinTxInterval_Object = MibTableColumn
bfdSessDesiredMinTxInterval = _BfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 25),
    _BfdSessDesiredMinTxInterval_Type()
)
bfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDesiredMinTxInterval.setStatus("current")
_BfdSessReqMinRxInterval_Type = BfdIntervalTC
_BfdSessReqMinRxInterval_Object = MibTableColumn
bfdSessReqMinRxInterval = _BfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 26),
    _BfdSessReqMinRxInterval_Type()
)
bfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessReqMinRxInterval.setStatus("current")
_BfdSessReqMinEchoRxInterval_Type = BfdIntervalTC
_BfdSessReqMinEchoRxInterval_Object = MibTableColumn
bfdSessReqMinEchoRxInterval = _BfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 27),
    _BfdSessReqMinEchoRxInterval_Type()
)
bfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessReqMinEchoRxInterval.setStatus("current")
_BfdSessDetectMult_Type = BfdMultiplierTC
_BfdSessDetectMult_Object = MibTableColumn
bfdSessDetectMult = _BfdSessDetectMult_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 28),
    _BfdSessDetectMult_Type()
)
bfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessDetectMult.setStatus("current")
_BfdSessNegotiatedInterval_Type = BfdIntervalTC
_BfdSessNegotiatedInterval_Object = MibTableColumn
bfdSessNegotiatedInterval = _BfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 29),
    _BfdSessNegotiatedInterval_Type()
)
bfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessNegotiatedInterval.setStatus("current")
_BfdSessNegotiatedEchoInterval_Type = BfdIntervalTC
_BfdSessNegotiatedEchoInterval_Object = MibTableColumn
bfdSessNegotiatedEchoInterval = _BfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 30),
    _BfdSessNegotiatedEchoInterval_Type()
)
bfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessNegotiatedEchoInterval.setStatus("current")
_BfdSessNegotiatedDetectMult_Type = BfdMultiplierTC
_BfdSessNegotiatedDetectMult_Object = MibTableColumn
bfdSessNegotiatedDetectMult = _BfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 31),
    _BfdSessNegotiatedDetectMult_Type()
)
bfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessNegotiatedDetectMult.setStatus("current")


class _BfdSessAuthPresFlag_Type(TruthValue):
    """Custom type bfdSessAuthPresFlag based on TruthValue"""


_BfdSessAuthPresFlag_Object = MibTableColumn
bfdSessAuthPresFlag = _BfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 32),
    _BfdSessAuthPresFlag_Type()
)
bfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthPresFlag.setStatus("current")


class _BfdSessAuthenticationType_Type(IANAbfdSessAuthenticationTypeTC):
    """Custom type bfdSessAuthenticationType based on IANAbfdSessAuthenticationTypeTC"""


_BfdSessAuthenticationType_Object = MibTableColumn
bfdSessAuthenticationType = _BfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 33),
    _BfdSessAuthenticationType_Type()
)
bfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthenticationType.setStatus("current")


class _BfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type bfdSessAuthenticationKeyID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_BfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_BfdSessAuthenticationKeyID_Object = MibTableColumn
bfdSessAuthenticationKeyID = _BfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 34),
    _BfdSessAuthenticationKeyID_Type()
)
bfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthenticationKeyID.setStatus("current")
_BfdSessAuthenticationKey_Type = IANAbfdSessAuthenticationKeyTC
_BfdSessAuthenticationKey_Object = MibTableColumn
bfdSessAuthenticationKey = _BfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 35),
    _BfdSessAuthenticationKey_Type()
)
bfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessAuthenticationKey.setStatus("current")
_BfdSessStorageType_Type = StorageType
_BfdSessStorageType_Object = MibTableColumn
bfdSessStorageType = _BfdSessStorageType_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 36),
    _BfdSessStorageType_Type()
)
bfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessStorageType.setStatus("current")
_BfdSessRowStatus_Type = RowStatus
_BfdSessRowStatus_Object = MibTableColumn
bfdSessRowStatus = _BfdSessRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 37),
    _BfdSessRowStatus_Type()
)
bfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bfdSessRowStatus.setStatus("current")
_BfdSessPerfTable_Object = MibTable
bfdSessPerfTable = _BfdSessPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3)
)
if mibBuilder.loadTexts:
    bfdSessPerfTable.setStatus("current")
_BfdSessPerfEntry_Object = MibTableRow
bfdSessPerfEntry = _BfdSessPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bfdSessPerfEntry.setStatus("current")
_BfdSessPerfCtrlPktIn_Type = Counter32
_BfdSessPerfCtrlPktIn_Object = MibTableColumn
bfdSessPerfCtrlPktIn = _BfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 1),
    _BfdSessPerfCtrlPktIn_Type()
)
bfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktIn.setStatus("current")
_BfdSessPerfCtrlPktOut_Type = Counter32
_BfdSessPerfCtrlPktOut_Object = MibTableColumn
bfdSessPerfCtrlPktOut = _BfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 2),
    _BfdSessPerfCtrlPktOut_Type()
)
bfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktOut.setStatus("current")
_BfdSessPerfCtrlPktDrop_Type = Counter32
_BfdSessPerfCtrlPktDrop_Object = MibTableColumn
bfdSessPerfCtrlPktDrop = _BfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 3),
    _BfdSessPerfCtrlPktDrop_Type()
)
bfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktDrop.setStatus("current")
_BfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_BfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
bfdSessPerfCtrlPktDropLastTime = _BfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 4),
    _BfdSessPerfCtrlPktDropLastTime_Type()
)
bfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktDropLastTime.setStatus("current")
_BfdSessPerfEchoPktIn_Type = Counter32
_BfdSessPerfEchoPktIn_Object = MibTableColumn
bfdSessPerfEchoPktIn = _BfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 5),
    _BfdSessPerfEchoPktIn_Type()
)
bfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktIn.setStatus("current")
_BfdSessPerfEchoPktOut_Type = Counter32
_BfdSessPerfEchoPktOut_Object = MibTableColumn
bfdSessPerfEchoPktOut = _BfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 6),
    _BfdSessPerfEchoPktOut_Type()
)
bfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktOut.setStatus("current")
_BfdSessPerfEchoPktDrop_Type = Counter32
_BfdSessPerfEchoPktDrop_Object = MibTableColumn
bfdSessPerfEchoPktDrop = _BfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 7),
    _BfdSessPerfEchoPktDrop_Type()
)
bfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktDrop.setStatus("current")
_BfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_BfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
bfdSessPerfEchoPktDropLastTime = _BfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 8),
    _BfdSessPerfEchoPktDropLastTime_Type()
)
bfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktDropLastTime.setStatus("current")
_BfdSessUpTime_Type = TimeStamp
_BfdSessUpTime_Object = MibTableColumn
bfdSessUpTime = _BfdSessUpTime_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 9),
    _BfdSessUpTime_Type()
)
bfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessUpTime.setStatus("current")
_BfdSessPerfLastSessDownTime_Type = TimeStamp
_BfdSessPerfLastSessDownTime_Object = MibTableColumn
bfdSessPerfLastSessDownTime = _BfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 10),
    _BfdSessPerfLastSessDownTime_Type()
)
bfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfLastSessDownTime.setStatus("current")
_BfdSessPerfLastCommLostDiag_Type = IANAbfdDiagTC
_BfdSessPerfLastCommLostDiag_Object = MibTableColumn
bfdSessPerfLastCommLostDiag = _BfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 11),
    _BfdSessPerfLastCommLostDiag_Type()
)
bfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfLastCommLostDiag.setStatus("current")
_BfdSessPerfSessUpCount_Type = Counter32
_BfdSessPerfSessUpCount_Object = MibTableColumn
bfdSessPerfSessUpCount = _BfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 12),
    _BfdSessPerfSessUpCount_Type()
)
bfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfSessUpCount.setStatus("current")
_BfdSessPerfDiscTime_Type = TimeStamp
_BfdSessPerfDiscTime_Object = MibTableColumn
bfdSessPerfDiscTime = _BfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 13),
    _BfdSessPerfDiscTime_Type()
)
bfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfDiscTime.setStatus("current")
_BfdSessPerfCtrlPktInHC_Type = Counter64
_BfdSessPerfCtrlPktInHC_Object = MibTableColumn
bfdSessPerfCtrlPktInHC = _BfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 14),
    _BfdSessPerfCtrlPktInHC_Type()
)
bfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktInHC.setStatus("current")
_BfdSessPerfCtrlPktOutHC_Type = Counter64
_BfdSessPerfCtrlPktOutHC_Object = MibTableColumn
bfdSessPerfCtrlPktOutHC = _BfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 15),
    _BfdSessPerfCtrlPktOutHC_Type()
)
bfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktOutHC.setStatus("current")
_BfdSessPerfCtrlPktDropHC_Type = Counter64
_BfdSessPerfCtrlPktDropHC_Object = MibTableColumn
bfdSessPerfCtrlPktDropHC = _BfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 16),
    _BfdSessPerfCtrlPktDropHC_Type()
)
bfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfCtrlPktDropHC.setStatus("current")
_BfdSessPerfEchoPktInHC_Type = Counter64
_BfdSessPerfEchoPktInHC_Object = MibTableColumn
bfdSessPerfEchoPktInHC = _BfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 17),
    _BfdSessPerfEchoPktInHC_Type()
)
bfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktInHC.setStatus("current")
_BfdSessPerfEchoPktOutHC_Type = Counter64
_BfdSessPerfEchoPktOutHC_Object = MibTableColumn
bfdSessPerfEchoPktOutHC = _BfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 18),
    _BfdSessPerfEchoPktOutHC_Type()
)
bfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktOutHC.setStatus("current")
_BfdSessPerfEchoPktDropHC_Type = Counter64
_BfdSessPerfEchoPktDropHC_Object = MibTableColumn
bfdSessPerfEchoPktDropHC = _BfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 19),
    _BfdSessPerfEchoPktDropHC_Type()
)
bfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessPerfEchoPktDropHC.setStatus("current")
_BfdSessDiscMapTable_Object = MibTable
bfdSessDiscMapTable = _BfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 4)
)
if mibBuilder.loadTexts:
    bfdSessDiscMapTable.setStatus("current")
_BfdSessDiscMapEntry_Object = MibTableRow
bfdSessDiscMapEntry = _BfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 4, 1)
)
bfdSessDiscMapEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    bfdSessDiscMapEntry.setStatus("current")
_BfdSessDiscMapIndex_Type = BfdSessIndexTC
_BfdSessDiscMapIndex_Object = MibTableColumn
bfdSessDiscMapIndex = _BfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 4, 1, 1),
    _BfdSessDiscMapIndex_Type()
)
bfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessDiscMapIndex.setStatus("current")
_BfdSessIpMapTable_Object = MibTable
bfdSessIpMapTable = _BfdSessIpMapTable_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 5)
)
if mibBuilder.loadTexts:
    bfdSessIpMapTable.setStatus("current")
_BfdSessIpMapEntry_Object = MibTableRow
bfdSessIpMapEntry = _BfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 5, 1)
)
bfdSessIpMapEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessInterface"),
    (0, "BFD-STD-MIB", "bfdSessSrcAddrType"),
    (0, "BFD-STD-MIB", "bfdSessSrcAddr"),
    (0, "BFD-STD-MIB", "bfdSessDstAddrType"),
    (0, "BFD-STD-MIB", "bfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    bfdSessIpMapEntry.setStatus("current")
_BfdSessIpMapIndex_Type = BfdSessIndexTC
_BfdSessIpMapIndex_Object = MibTableColumn
bfdSessIpMapIndex = _BfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 222, 1, 5, 1, 1),
    _BfdSessIpMapIndex_Type()
)
bfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessIpMapIndex.setStatus("current")
_BfdConformance_ObjectIdentity = ObjectIdentity
bfdConformance = _BfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 2)
)
_BfdGroups_ObjectIdentity = ObjectIdentity
bfdGroups = _BfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 2, 1)
)
_BfdCompliances_ObjectIdentity = ObjectIdentity
bfdCompliances = _BfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 222, 2, 2)
)
bfdSessEntry.registerAugmentions(
    ("BFD-STD-MIB",
     "bfdSessPerfEntry")
)
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())

# Managed Objects groups

bfdSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 222, 2, 1, 1)
)
bfdSessionGroup.setObjects(
      *(("BFD-STD-MIB", "bfdAdminStatus"),
        ("BFD-STD-MIB", "bfdOperStatus"),
        ("BFD-STD-MIB", "bfdNotificationsEnable"),
        ("BFD-STD-MIB", "bfdSessVersionNumber"),
        ("BFD-STD-MIB", "bfdSessType"),
        ("BFD-STD-MIB", "bfdSessIndexNext"),
        ("BFD-STD-MIB", "bfdSessDiscriminator"),
        ("BFD-STD-MIB", "bfdSessDestinationUdpPort"),
        ("BFD-STD-MIB", "bfdSessSourceUdpPort"),
        ("BFD-STD-MIB", "bfdSessEchoSourceUdpPort"),
        ("BFD-STD-MIB", "bfdSessAdminStatus"),
        ("BFD-STD-MIB", "bfdSessOperStatus"),
        ("BFD-STD-MIB", "bfdSessOperMode"),
        ("BFD-STD-MIB", "bfdSessDemandModeDesiredFlag"),
        ("BFD-STD-MIB", "bfdSessControlPlaneIndepFlag"),
        ("BFD-STD-MIB", "bfdSessMultipointFlag"),
        ("BFD-STD-MIB", "bfdSessInterface"),
        ("BFD-STD-MIB", "bfdSessSrcAddrType"),
        ("BFD-STD-MIB", "bfdSessSrcAddr"),
        ("BFD-STD-MIB", "bfdSessDstAddrType"),
        ("BFD-STD-MIB", "bfdSessDstAddr"),
        ("BFD-STD-MIB", "bfdSessGTSM"),
        ("BFD-STD-MIB", "bfdSessGTSMTTL"),
        ("BFD-STD-MIB", "bfdSessDesiredMinTxInterval"),
        ("BFD-STD-MIB", "bfdSessReqMinRxInterval"),
        ("BFD-STD-MIB", "bfdSessReqMinEchoRxInterval"),
        ("BFD-STD-MIB", "bfdSessDetectMult"),
        ("BFD-STD-MIB", "bfdSessAuthPresFlag"),
        ("BFD-STD-MIB", "bfdSessAuthenticationType"),
        ("BFD-STD-MIB", "bfdSessAuthenticationKeyID"),
        ("BFD-STD-MIB", "bfdSessAuthenticationKey"),
        ("BFD-STD-MIB", "bfdSessStorageType"),
        ("BFD-STD-MIB", "bfdSessRowStatus"))
)
if mibBuilder.loadTexts:
    bfdSessionGroup.setStatus("current")

bfdSessionReadOnlyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 222, 2, 1, 2)
)
bfdSessionReadOnlyGroup.setObjects(
      *(("BFD-STD-MIB", "bfdSessRemoteDiscr"),
        ("BFD-STD-MIB", "bfdSessState"),
        ("BFD-STD-MIB", "bfdSessRemoteHeardFlag"),
        ("BFD-STD-MIB", "bfdSessDiag"),
        ("BFD-STD-MIB", "bfdSessNegotiatedInterval"),
        ("BFD-STD-MIB", "bfdSessNegotiatedEchoInterval"),
        ("BFD-STD-MIB", "bfdSessNegotiatedDetectMult"),
        ("BFD-STD-MIB", "bfdSessDiscMapIndex"),
        ("BFD-STD-MIB", "bfdSessIpMapIndex"))
)
if mibBuilder.loadTexts:
    bfdSessionReadOnlyGroup.setStatus("current")

bfdSessionPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 222, 2, 1, 3)
)
bfdSessionPerfGroup.setObjects(
      *(("BFD-STD-MIB", "bfdSessPerfCtrlPktIn"),
        ("BFD-STD-MIB", "bfdSessPerfCtrlPktOut"),
        ("BFD-STD-MIB", "bfdSessPerfCtrlPktDrop"),
        ("BFD-STD-MIB", "bfdSessPerfCtrlPktDropLastTime"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktIn"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktOut"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktDrop"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktDropLastTime"),
        ("BFD-STD-MIB", "bfdSessUpTime"),
        ("BFD-STD-MIB", "bfdSessPerfLastSessDownTime"),
        ("BFD-STD-MIB", "bfdSessPerfLastCommLostDiag"),
        ("BFD-STD-MIB", "bfdSessPerfSessUpCount"),
        ("BFD-STD-MIB", "bfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    bfdSessionPerfGroup.setStatus("current")

bfdSessionPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 222, 2, 1, 4)
)
bfdSessionPerfHCGroup.setObjects(
      *(("BFD-STD-MIB", "bfdSessPerfCtrlPktInHC"),
        ("BFD-STD-MIB", "bfdSessPerfCtrlPktOutHC"),
        ("BFD-STD-MIB", "bfdSessPerfCtrlPktDropHC"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktInHC"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktOutHC"),
        ("BFD-STD-MIB", "bfdSessPerfEchoPktDropHC"))
)
if mibBuilder.loadTexts:
    bfdSessionPerfHCGroup.setStatus("current")


# Notification objects

bfdSessUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 222, 0, 1)
)
bfdSessUp.setObjects(
      *(("BFD-STD-MIB", "bfdSessDiag"),
        ("BFD-STD-MIB", "bfdSessDiag"))
)
if mibBuilder.loadTexts:
    bfdSessUp.setStatus(
        "current"
    )

bfdSessDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 222, 0, 2)
)
bfdSessDown.setObjects(
      *(("BFD-STD-MIB", "bfdSessDiag"),
        ("BFD-STD-MIB", "bfdSessDiag"))
)
if mibBuilder.loadTexts:
    bfdSessDown.setStatus(
        "current"
    )


# Notifications groups

bfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 222, 2, 1, 5)
)
bfdNotificationGroup.setObjects(
      *(("BFD-STD-MIB", "bfdSessUp"),
        ("BFD-STD-MIB", "bfdSessDown"))
)
if mibBuilder.loadTexts:
    bfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bfdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 222, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bfdModuleFullCompliance.setStatus(
        "current"
    )

bfdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 222, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bfdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BFD-STD-MIB",
    **{"bfdMIB": bfdMIB,
       "bfdNotifications": bfdNotifications,
       "bfdSessUp": bfdSessUp,
       "bfdSessDown": bfdSessDown,
       "bfdObjects": bfdObjects,
       "bfdScalarObjects": bfdScalarObjects,
       "bfdAdminStatus": bfdAdminStatus,
       "bfdOperStatus": bfdOperStatus,
       "bfdNotificationsEnable": bfdNotificationsEnable,
       "bfdSessIndexNext": bfdSessIndexNext,
       "bfdSessTable": bfdSessTable,
       "bfdSessEntry": bfdSessEntry,
       "bfdSessIndex": bfdSessIndex,
       "bfdSessVersionNumber": bfdSessVersionNumber,
       "bfdSessType": bfdSessType,
       "bfdSessDiscriminator": bfdSessDiscriminator,
       "bfdSessRemoteDiscr": bfdSessRemoteDiscr,
       "bfdSessDestinationUdpPort": bfdSessDestinationUdpPort,
       "bfdSessSourceUdpPort": bfdSessSourceUdpPort,
       "bfdSessEchoSourceUdpPort": bfdSessEchoSourceUdpPort,
       "bfdSessAdminStatus": bfdSessAdminStatus,
       "bfdSessOperStatus": bfdSessOperStatus,
       "bfdSessState": bfdSessState,
       "bfdSessRemoteHeardFlag": bfdSessRemoteHeardFlag,
       "bfdSessDiag": bfdSessDiag,
       "bfdSessOperMode": bfdSessOperMode,
       "bfdSessDemandModeDesiredFlag": bfdSessDemandModeDesiredFlag,
       "bfdSessControlPlaneIndepFlag": bfdSessControlPlaneIndepFlag,
       "bfdSessMultipointFlag": bfdSessMultipointFlag,
       "bfdSessInterface": bfdSessInterface,
       "bfdSessSrcAddrType": bfdSessSrcAddrType,
       "bfdSessSrcAddr": bfdSessSrcAddr,
       "bfdSessDstAddrType": bfdSessDstAddrType,
       "bfdSessDstAddr": bfdSessDstAddr,
       "bfdSessGTSM": bfdSessGTSM,
       "bfdSessGTSMTTL": bfdSessGTSMTTL,
       "bfdSessDesiredMinTxInterval": bfdSessDesiredMinTxInterval,
       "bfdSessReqMinRxInterval": bfdSessReqMinRxInterval,
       "bfdSessReqMinEchoRxInterval": bfdSessReqMinEchoRxInterval,
       "bfdSessDetectMult": bfdSessDetectMult,
       "bfdSessNegotiatedInterval": bfdSessNegotiatedInterval,
       "bfdSessNegotiatedEchoInterval": bfdSessNegotiatedEchoInterval,
       "bfdSessNegotiatedDetectMult": bfdSessNegotiatedDetectMult,
       "bfdSessAuthPresFlag": bfdSessAuthPresFlag,
       "bfdSessAuthenticationType": bfdSessAuthenticationType,
       "bfdSessAuthenticationKeyID": bfdSessAuthenticationKeyID,
       "bfdSessAuthenticationKey": bfdSessAuthenticationKey,
       "bfdSessStorageType": bfdSessStorageType,
       "bfdSessRowStatus": bfdSessRowStatus,
       "bfdSessPerfTable": bfdSessPerfTable,
       "bfdSessPerfEntry": bfdSessPerfEntry,
       "bfdSessPerfCtrlPktIn": bfdSessPerfCtrlPktIn,
       "bfdSessPerfCtrlPktOut": bfdSessPerfCtrlPktOut,
       "bfdSessPerfCtrlPktDrop": bfdSessPerfCtrlPktDrop,
       "bfdSessPerfCtrlPktDropLastTime": bfdSessPerfCtrlPktDropLastTime,
       "bfdSessPerfEchoPktIn": bfdSessPerfEchoPktIn,
       "bfdSessPerfEchoPktOut": bfdSessPerfEchoPktOut,
       "bfdSessPerfEchoPktDrop": bfdSessPerfEchoPktDrop,
       "bfdSessPerfEchoPktDropLastTime": bfdSessPerfEchoPktDropLastTime,
       "bfdSessUpTime": bfdSessUpTime,
       "bfdSessPerfLastSessDownTime": bfdSessPerfLastSessDownTime,
       "bfdSessPerfLastCommLostDiag": bfdSessPerfLastCommLostDiag,
       "bfdSessPerfSessUpCount": bfdSessPerfSessUpCount,
       "bfdSessPerfDiscTime": bfdSessPerfDiscTime,
       "bfdSessPerfCtrlPktInHC": bfdSessPerfCtrlPktInHC,
       "bfdSessPerfCtrlPktOutHC": bfdSessPerfCtrlPktOutHC,
       "bfdSessPerfCtrlPktDropHC": bfdSessPerfCtrlPktDropHC,
       "bfdSessPerfEchoPktInHC": bfdSessPerfEchoPktInHC,
       "bfdSessPerfEchoPktOutHC": bfdSessPerfEchoPktOutHC,
       "bfdSessPerfEchoPktDropHC": bfdSessPerfEchoPktDropHC,
       "bfdSessDiscMapTable": bfdSessDiscMapTable,
       "bfdSessDiscMapEntry": bfdSessDiscMapEntry,
       "bfdSessDiscMapIndex": bfdSessDiscMapIndex,
       "bfdSessIpMapTable": bfdSessIpMapTable,
       "bfdSessIpMapEntry": bfdSessIpMapEntry,
       "bfdSessIpMapIndex": bfdSessIpMapIndex,
       "bfdConformance": bfdConformance,
       "bfdGroups": bfdGroups,
       "bfdSessionGroup": bfdSessionGroup,
       "bfdSessionReadOnlyGroup": bfdSessionReadOnlyGroup,
       "bfdSessionPerfGroup": bfdSessionPerfGroup,
       "bfdSessionPerfHCGroup": bfdSessionPerfHCGroup,
       "bfdNotificationGroup": bfdNotificationGroup,
       "bfdCompliances": bfdCompliances,
       "bfdModuleFullCompliance": bfdModuleFullCompliance,
       "bfdModuleReadOnlyCompliance": bfdModuleReadOnlyCompliance}
)
