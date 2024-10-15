# SNMP MIB module (HH3C-BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-BFD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:31 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hh3cBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72)
)
hh3cBfdMIB.setRevisions(
        ("2014-01-17 12:00",
         "2006-05-16 12:00")
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
    displayHint = "d"
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

_Hh3cBfdNotifications_ObjectIdentity = ObjectIdentity
hh3cBfdNotifications = _Hh3cBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0)
)
_Hh3cBfdObjects_ObjectIdentity = ObjectIdentity
hh3cBfdObjects = _Hh3cBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1)
)
_Hh3cBfdGlobalObjects_ObjectIdentity = ObjectIdentity
hh3cBfdGlobalObjects = _Hh3cBfdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 1)
)


class _Hh3cBfdVersionNumber_Type(Unsigned32):
    """Custom type hh3cBfdVersionNumber based on Unsigned32"""
    defaultValue = 1


_Hh3cBfdVersionNumber_Object = MibScalar
hh3cBfdVersionNumber = _Hh3cBfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 1, 1),
    _Hh3cBfdVersionNumber_Type()
)
hh3cBfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdVersionNumber.setStatus("current")


class _Hh3cBfdSysInitMode_Type(Integer32):
    """Custom type hh3cBfdSysInitMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_Hh3cBfdSysInitMode_Type.__name__ = "Integer32"
_Hh3cBfdSysInitMode_Object = MibScalar
hh3cBfdSysInitMode = _Hh3cBfdSysInitMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 1, 2),
    _Hh3cBfdSysInitMode_Type()
)
hh3cBfdSysInitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBfdSysInitMode.setStatus("current")


class _Hh3cBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type hh3cBfdSessNotificationsEnable based on TruthValue"""


_Hh3cBfdSessNotificationsEnable_Object = MibScalar
hh3cBfdSessNotificationsEnable = _Hh3cBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 1, 3),
    _Hh3cBfdSessNotificationsEnable_Type()
)
hh3cBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBfdSessNotificationsEnable.setStatus("current")


class _Hh3cBfdSessNumberLimit_Type(Unsigned32):
    """Custom type hh3cBfdSessNumberLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cBfdSessNumberLimit_Type.__name__ = "Unsigned32"
_Hh3cBfdSessNumberLimit_Object = MibScalar
hh3cBfdSessNumberLimit = _Hh3cBfdSessNumberLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 1, 4),
    _Hh3cBfdSessNumberLimit_Type()
)
hh3cBfdSessNumberLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessNumberLimit.setStatus("current")
_Hh3cBfdIfTable_Object = MibTable
hh3cBfdIfTable = _Hh3cBfdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cBfdIfTable.setStatus("current")
_Hh3cBfdIfEntry_Object = MibTableRow
hh3cBfdIfEntry = _Hh3cBfdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1)
)
hh3cBfdIfEntry.setIndexNames(
    (0, "HH3C-BFD-STD-MIB", "hh3cBfdIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cBfdIfEntry.setStatus("current")
_Hh3cBfdIfIndex_Type = InterfaceIndex
_Hh3cBfdIfIndex_Object = MibTableColumn
hh3cBfdIfIndex = _Hh3cBfdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1, 1),
    _Hh3cBfdIfIndex_Type()
)
hh3cBfdIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBfdIfIndex.setStatus("current")
_Hh3cBfdIfDesiredMinTxInterval_Type = BfdInterval
_Hh3cBfdIfDesiredMinTxInterval_Object = MibTableColumn
hh3cBfdIfDesiredMinTxInterval = _Hh3cBfdIfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1, 2),
    _Hh3cBfdIfDesiredMinTxInterval_Type()
)
hh3cBfdIfDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBfdIfDesiredMinTxInterval.setStatus("current")
_Hh3cBfdIfDesiredMinRxInterval_Type = BfdInterval
_Hh3cBfdIfDesiredMinRxInterval_Object = MibTableColumn
hh3cBfdIfDesiredMinRxInterval = _Hh3cBfdIfDesiredMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1, 3),
    _Hh3cBfdIfDesiredMinRxInterval_Type()
)
hh3cBfdIfDesiredMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBfdIfDesiredMinRxInterval.setStatus("current")
_Hh3cBfdIfDetectMult_Type = Unsigned32
_Hh3cBfdIfDetectMult_Object = MibTableColumn
hh3cBfdIfDetectMult = _Hh3cBfdIfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1, 4),
    _Hh3cBfdIfDetectMult_Type()
)
hh3cBfdIfDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBfdIfDetectMult.setStatus("current")


class _Hh3cBfdIfAuthType_Type(Integer32):
    """Custom type hh3cBfdIfAuthType based on Integer32"""
    defaultValue = 1

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
        *(("md5", 3),
          ("mmd5", 4),
          ("msha1", 6),
          ("none", 1),
          ("sha1", 5),
          ("simple", 2))
    )


_Hh3cBfdIfAuthType_Type.__name__ = "Integer32"
_Hh3cBfdIfAuthType_Object = MibTableColumn
hh3cBfdIfAuthType = _Hh3cBfdIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 2, 1, 5),
    _Hh3cBfdIfAuthType_Type()
)
hh3cBfdIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdIfAuthType.setStatus("current")
_Hh3cBfdSessTable_Object = MibTable
hh3cBfdSessTable = _Hh3cBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cBfdSessTable.setStatus("current")
_Hh3cBfdSessEntry_Object = MibTableRow
hh3cBfdSessEntry = _Hh3cBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1)
)
hh3cBfdSessEntry.setIndexNames(
    (0, "HH3C-BFD-STD-MIB", "hh3cBfdSessIfIndex"),
    (0, "HH3C-BFD-STD-MIB", "hh3cBfdSessIndex"),
)
if mibBuilder.loadTexts:
    hh3cBfdSessEntry.setStatus("current")
_Hh3cBfdSessIfIndex_Type = InterfaceIndex
_Hh3cBfdSessIfIndex_Object = MibTableColumn
hh3cBfdSessIfIndex = _Hh3cBfdSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 1),
    _Hh3cBfdSessIfIndex_Type()
)
hh3cBfdSessIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBfdSessIfIndex.setStatus("current")
_Hh3cBfdSessIndex_Type = BfdSessIndexTC
_Hh3cBfdSessIndex_Object = MibTableColumn
hh3cBfdSessIndex = _Hh3cBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 2),
    _Hh3cBfdSessIndex_Type()
)
hh3cBfdSessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBfdSessIndex.setStatus("current")


class _Hh3cBfdSessAppSupportId_Type(Bits):
    """Custom type hh3cBfdSessAppSupportId based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("isis", 2),
          ("mpls", 4),
          ("none", 0),
          ("ospf", 1))
    )

_Hh3cBfdSessAppSupportId_Type.__name__ = "Bits"
_Hh3cBfdSessAppSupportId_Object = MibTableColumn
hh3cBfdSessAppSupportId = _Hh3cBfdSessAppSupportId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 3),
    _Hh3cBfdSessAppSupportId_Type()
)
hh3cBfdSessAppSupportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessAppSupportId.setStatus("current")


class _Hh3cBfdSessLocalDiscr_Type(Unsigned32):
    """Custom type hh3cBfdSessLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cBfdSessLocalDiscr_Type.__name__ = "Unsigned32"
_Hh3cBfdSessLocalDiscr_Object = MibTableColumn
hh3cBfdSessLocalDiscr = _Hh3cBfdSessLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 4),
    _Hh3cBfdSessLocalDiscr_Type()
)
hh3cBfdSessLocalDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessLocalDiscr.setStatus("current")


class _Hh3cBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type hh3cBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_Hh3cBfdSessRemoteDiscr_Object = MibTableColumn
hh3cBfdSessRemoteDiscr = _Hh3cBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 5),
    _Hh3cBfdSessRemoteDiscr_Type()
)
hh3cBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessRemoteDiscr.setStatus("current")


class _Hh3cBfdSessDstPort_Type(InetPortNumber):
    """Custom type hh3cBfdSessDstPort based on InetPortNumber"""
    defaultValue = 3784


_Hh3cBfdSessDstPort_Object = MibTableColumn
hh3cBfdSessDstPort = _Hh3cBfdSessDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 6),
    _Hh3cBfdSessDstPort_Type()
)
hh3cBfdSessDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessDstPort.setStatus("current")


class _Hh3cBfdSessOperMode_Type(Integer32):
    """Custom type hh3cBfdSessOperMode based on Integer32"""
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
        *(("asyncModeWEchoFun", 3),
          ("asynchModeWOEchoFun", 1),
          ("demandModeWEchoFunction", 4),
          ("demandModeWOEchoFunction", 2))
    )


_Hh3cBfdSessOperMode_Type.__name__ = "Integer32"
_Hh3cBfdSessOperMode_Object = MibTableColumn
hh3cBfdSessOperMode = _Hh3cBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 7),
    _Hh3cBfdSessOperMode_Type()
)
hh3cBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessOperMode.setStatus("current")
_Hh3cBfdSessAddrType_Type = InetAddressType
_Hh3cBfdSessAddrType_Object = MibTableColumn
hh3cBfdSessAddrType = _Hh3cBfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 8),
    _Hh3cBfdSessAddrType_Type()
)
hh3cBfdSessAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessAddrType.setStatus("current")
_Hh3cBfdSessLocalAddr_Type = InetAddress
_Hh3cBfdSessLocalAddr_Object = MibTableColumn
hh3cBfdSessLocalAddr = _Hh3cBfdSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 9),
    _Hh3cBfdSessLocalAddr_Type()
)
hh3cBfdSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessLocalAddr.setStatus("current")
_Hh3cBfdSessRemoteAddr_Type = InetAddress
_Hh3cBfdSessRemoteAddr_Object = MibTableColumn
hh3cBfdSessRemoteAddr = _Hh3cBfdSessRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 10),
    _Hh3cBfdSessRemoteAddr_Type()
)
hh3cBfdSessRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessRemoteAddr.setStatus("current")


class _Hh3cBfdSessLocalDiag_Type(BfdDiag):
    """Custom type hh3cBfdSessLocalDiag based on BfdDiag"""


_Hh3cBfdSessLocalDiag_Object = MibTableColumn
hh3cBfdSessLocalDiag = _Hh3cBfdSessLocalDiag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 11),
    _Hh3cBfdSessLocalDiag_Type()
)
hh3cBfdSessLocalDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessLocalDiag.setStatus("current")


class _Hh3cBfdSessState_Type(Integer32):
    """Custom type hh3cBfdSessState based on Integer32"""
    defaultValue = 1

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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )


_Hh3cBfdSessState_Type.__name__ = "Integer32"
_Hh3cBfdSessState_Object = MibTableColumn
hh3cBfdSessState = _Hh3cBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 12),
    _Hh3cBfdSessState_Type()
)
hh3cBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessState.setStatus("current")


class _Hh3cBfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type hh3cBfdSessControlPlanIndepFlag based on TruthValue"""


_Hh3cBfdSessControlPlanIndepFlag_Object = MibTableColumn
hh3cBfdSessControlPlanIndepFlag = _Hh3cBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 13),
    _Hh3cBfdSessControlPlanIndepFlag_Type()
)
hh3cBfdSessControlPlanIndepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessControlPlanIndepFlag.setStatus("current")


class _Hh3cBfdSessAuthFlag_Type(TruthValue):
    """Custom type hh3cBfdSessAuthFlag based on TruthValue"""


_Hh3cBfdSessAuthFlag_Object = MibTableColumn
hh3cBfdSessAuthFlag = _Hh3cBfdSessAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 14),
    _Hh3cBfdSessAuthFlag_Type()
)
hh3cBfdSessAuthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessAuthFlag.setStatus("current")


class _Hh3cBfdSessDemandModeFlag_Type(TruthValue):
    """Custom type hh3cBfdSessDemandModeFlag based on TruthValue"""


_Hh3cBfdSessDemandModeFlag_Object = MibTableColumn
hh3cBfdSessDemandModeFlag = _Hh3cBfdSessDemandModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 3, 1, 15),
    _Hh3cBfdSessDemandModeFlag_Type()
)
hh3cBfdSessDemandModeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessDemandModeFlag.setStatus("current")
_Hh3cBfdSessStatTable_Object = MibTable
hh3cBfdSessStatTable = _Hh3cBfdSessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cBfdSessStatTable.setStatus("current")
_Hh3cBfdSessStatEntry_Object = MibTableRow
hh3cBfdSessStatEntry = _Hh3cBfdSessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cBfdSessStatEntry.setStatus("current")
_Hh3cBfdSessStatPktInHC_Type = Counter64
_Hh3cBfdSessStatPktInHC_Object = MibTableColumn
hh3cBfdSessStatPktInHC = _Hh3cBfdSessStatPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1, 1),
    _Hh3cBfdSessStatPktInHC_Type()
)
hh3cBfdSessStatPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessStatPktInHC.setStatus("current")
_Hh3cBfdSessStatPktOutHC_Type = Counter64
_Hh3cBfdSessStatPktOutHC_Object = MibTableColumn
hh3cBfdSessStatPktOutHC = _Hh3cBfdSessStatPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1, 2),
    _Hh3cBfdSessStatPktOutHC_Type()
)
hh3cBfdSessStatPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessStatPktOutHC.setStatus("current")
_Hh3cBfdSessStatDownCount_Type = Counter32
_Hh3cBfdSessStatDownCount_Object = MibTableColumn
hh3cBfdSessStatDownCount = _Hh3cBfdSessStatDownCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1, 3),
    _Hh3cBfdSessStatDownCount_Type()
)
hh3cBfdSessStatDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessStatDownCount.setStatus("current")
_Hh3cBfdSessStatPktDiscard_Type = Counter64
_Hh3cBfdSessStatPktDiscard_Object = MibTableColumn
hh3cBfdSessStatPktDiscard = _Hh3cBfdSessStatPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1, 4),
    _Hh3cBfdSessStatPktDiscard_Type()
)
hh3cBfdSessStatPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessStatPktDiscard.setStatus("current")
_Hh3cBfdSessStatPktLost_Type = Counter64
_Hh3cBfdSessStatPktLost_Object = MibTableColumn
hh3cBfdSessStatPktLost = _Hh3cBfdSessStatPktLost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 4, 1, 5),
    _Hh3cBfdSessStatPktLost_Type()
)
hh3cBfdSessStatPktLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessStatPktLost.setStatus("current")
_Hh3cBfdSessPerfTable_Object = MibTable
hh3cBfdSessPerfTable = _Hh3cBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cBfdSessPerfTable.setStatus("current")
_Hh3cBfdSessPerfEntry_Object = MibTableRow
hh3cBfdSessPerfEntry = _Hh3cBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cBfdSessPerfEntry.setStatus("current")
_Hh3cBfdSessPerfCreatTime_Type = TimeStamp
_Hh3cBfdSessPerfCreatTime_Object = MibTableColumn
hh3cBfdSessPerfCreatTime = _Hh3cBfdSessPerfCreatTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 5, 1, 1),
    _Hh3cBfdSessPerfCreatTime_Type()
)
hh3cBfdSessPerfCreatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessPerfCreatTime.setStatus("current")
_Hh3cBfdSessPerfLastUpTime_Type = TimeStamp
_Hh3cBfdSessPerfLastUpTime_Object = MibTableColumn
hh3cBfdSessPerfLastUpTime = _Hh3cBfdSessPerfLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 5, 1, 2),
    _Hh3cBfdSessPerfLastUpTime_Type()
)
hh3cBfdSessPerfLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessPerfLastUpTime.setStatus("current")
_Hh3cBfdSessPerfLastDownTime_Type = TimeStamp
_Hh3cBfdSessPerfLastDownTime_Object = MibTableColumn
hh3cBfdSessPerfLastDownTime = _Hh3cBfdSessPerfLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 1, 5, 1, 3),
    _Hh3cBfdSessPerfLastDownTime_Type()
)
hh3cBfdSessPerfLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBfdSessPerfLastDownTime.setStatus("current")
_Hh3cBfdConformance_ObjectIdentity = ObjectIdentity
hh3cBfdConformance = _Hh3cBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 2)
)
hh3cBfdSessEntry.registerAugmentions(
    ("HH3C-BFD-STD-MIB",
     "hh3cBfdSessStatEntry")
)
hh3cBfdSessStatEntry.setIndexNames(*hh3cBfdSessEntry.getIndexNames())
hh3cBfdSessEntry.registerAugmentions(
    ("HH3C-BFD-STD-MIB",
     "hh3cBfdSessPerfEntry")
)
hh3cBfdSessPerfEntry.setIndexNames(*hh3cBfdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cBfdSessStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0, 1)
)
hh3cBfdSessStateChange.setObjects(
      *(("HH3C-BFD-STD-MIB", "hh3cBfdSessIfIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessState"))
)
if mibBuilder.loadTexts:
    hh3cBfdSessStateChange.setStatus(
        "current"
    )

hh3cBfdSessAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0, 2)
)
hh3cBfdSessAuthFail.setObjects(
    ("HH3C-BFD-STD-MIB", "hh3cBfdIfIndex")
)
if mibBuilder.loadTexts:
    hh3cBfdSessAuthFail.setStatus(
        "current"
    )

hh3cBfdSessStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0, 3)
)
hh3cBfdSessStateUp.setObjects(
      *(("HH3C-BFD-STD-MIB", "hh3cBfdSessIfIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessState"))
)
if mibBuilder.loadTexts:
    hh3cBfdSessStateUp.setStatus(
        "current"
    )

hh3cBfdSessStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0, 4)
)
hh3cBfdSessStateDown.setObjects(
      *(("HH3C-BFD-STD-MIB", "hh3cBfdSessIfIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessIndex"),
        ("HH3C-BFD-STD-MIB", "hh3cBfdSessState"))
)
if mibBuilder.loadTexts:
    hh3cBfdSessStateDown.setStatus(
        "current"
    )

hh3cBfdSessReachLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72, 0, 5)
)
hh3cBfdSessReachLimit.setObjects(
    ("HH3C-BFD-STD-MIB", "hh3cBfdSessNumberLimit")
)
if mibBuilder.loadTexts:
    hh3cBfdSessReachLimit.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BFD-STD-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "hh3cBfdMIB": hh3cBfdMIB,
       "hh3cBfdNotifications": hh3cBfdNotifications,
       "hh3cBfdSessStateChange": hh3cBfdSessStateChange,
       "hh3cBfdSessAuthFail": hh3cBfdSessAuthFail,
       "hh3cBfdSessStateUp": hh3cBfdSessStateUp,
       "hh3cBfdSessStateDown": hh3cBfdSessStateDown,
       "hh3cBfdSessReachLimit": hh3cBfdSessReachLimit,
       "hh3cBfdObjects": hh3cBfdObjects,
       "hh3cBfdGlobalObjects": hh3cBfdGlobalObjects,
       "hh3cBfdVersionNumber": hh3cBfdVersionNumber,
       "hh3cBfdSysInitMode": hh3cBfdSysInitMode,
       "hh3cBfdSessNotificationsEnable": hh3cBfdSessNotificationsEnable,
       "hh3cBfdSessNumberLimit": hh3cBfdSessNumberLimit,
       "hh3cBfdIfTable": hh3cBfdIfTable,
       "hh3cBfdIfEntry": hh3cBfdIfEntry,
       "hh3cBfdIfIndex": hh3cBfdIfIndex,
       "hh3cBfdIfDesiredMinTxInterval": hh3cBfdIfDesiredMinTxInterval,
       "hh3cBfdIfDesiredMinRxInterval": hh3cBfdIfDesiredMinRxInterval,
       "hh3cBfdIfDetectMult": hh3cBfdIfDetectMult,
       "hh3cBfdIfAuthType": hh3cBfdIfAuthType,
       "hh3cBfdSessTable": hh3cBfdSessTable,
       "hh3cBfdSessEntry": hh3cBfdSessEntry,
       "hh3cBfdSessIfIndex": hh3cBfdSessIfIndex,
       "hh3cBfdSessIndex": hh3cBfdSessIndex,
       "hh3cBfdSessAppSupportId": hh3cBfdSessAppSupportId,
       "hh3cBfdSessLocalDiscr": hh3cBfdSessLocalDiscr,
       "hh3cBfdSessRemoteDiscr": hh3cBfdSessRemoteDiscr,
       "hh3cBfdSessDstPort": hh3cBfdSessDstPort,
       "hh3cBfdSessOperMode": hh3cBfdSessOperMode,
       "hh3cBfdSessAddrType": hh3cBfdSessAddrType,
       "hh3cBfdSessLocalAddr": hh3cBfdSessLocalAddr,
       "hh3cBfdSessRemoteAddr": hh3cBfdSessRemoteAddr,
       "hh3cBfdSessLocalDiag": hh3cBfdSessLocalDiag,
       "hh3cBfdSessState": hh3cBfdSessState,
       "hh3cBfdSessControlPlanIndepFlag": hh3cBfdSessControlPlanIndepFlag,
       "hh3cBfdSessAuthFlag": hh3cBfdSessAuthFlag,
       "hh3cBfdSessDemandModeFlag": hh3cBfdSessDemandModeFlag,
       "hh3cBfdSessStatTable": hh3cBfdSessStatTable,
       "hh3cBfdSessStatEntry": hh3cBfdSessStatEntry,
       "hh3cBfdSessStatPktInHC": hh3cBfdSessStatPktInHC,
       "hh3cBfdSessStatPktOutHC": hh3cBfdSessStatPktOutHC,
       "hh3cBfdSessStatDownCount": hh3cBfdSessStatDownCount,
       "hh3cBfdSessStatPktDiscard": hh3cBfdSessStatPktDiscard,
       "hh3cBfdSessStatPktLost": hh3cBfdSessStatPktLost,
       "hh3cBfdSessPerfTable": hh3cBfdSessPerfTable,
       "hh3cBfdSessPerfEntry": hh3cBfdSessPerfEntry,
       "hh3cBfdSessPerfCreatTime": hh3cBfdSessPerfCreatTime,
       "hh3cBfdSessPerfLastUpTime": hh3cBfdSessPerfLastUpTime,
       "hh3cBfdSessPerfLastDownTime": hh3cBfdSessPerfLastDownTime,
       "hh3cBfdConformance": hh3cBfdConformance}
)
