# SNMP MIB module (H3C-BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-BFD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:56 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72)
)
h3cBfdMIB.setRevisions(
        ("2006-05-16 12:00",)
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

_H3cBfdNotifications_ObjectIdentity = ObjectIdentity
h3cBfdNotifications = _H3cBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0)
)
_H3cBfdObjects_ObjectIdentity = ObjectIdentity
h3cBfdObjects = _H3cBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1)
)
_H3cBfdGlobalObjects_ObjectIdentity = ObjectIdentity
h3cBfdGlobalObjects = _H3cBfdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1)
)


class _H3cBfdVersionNumber_Type(Unsigned32):
    """Custom type h3cBfdVersionNumber based on Unsigned32"""
    defaultValue = 1


_H3cBfdVersionNumber_Object = MibScalar
h3cBfdVersionNumber = _H3cBfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 1),
    _H3cBfdVersionNumber_Type()
)
h3cBfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdVersionNumber.setStatus("current")


class _H3cBfdSysInitMode_Type(Integer32):
    """Custom type h3cBfdSysInitMode based on Integer32"""
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


_H3cBfdSysInitMode_Type.__name__ = "Integer32"
_H3cBfdSysInitMode_Object = MibScalar
h3cBfdSysInitMode = _H3cBfdSysInitMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 2),
    _H3cBfdSysInitMode_Type()
)
h3cBfdSysInitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBfdSysInitMode.setStatus("current")


class _H3cBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type h3cBfdSessNotificationsEnable based on TruthValue"""


_H3cBfdSessNotificationsEnable_Object = MibScalar
h3cBfdSessNotificationsEnable = _H3cBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 3),
    _H3cBfdSessNotificationsEnable_Type()
)
h3cBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBfdSessNotificationsEnable.setStatus("current")
_H3cBfdIfTable_Object = MibTable
h3cBfdIfTable = _H3cBfdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2)
)
if mibBuilder.loadTexts:
    h3cBfdIfTable.setStatus("current")
_H3cBfdIfEntry_Object = MibTableRow
h3cBfdIfEntry = _H3cBfdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1)
)
h3cBfdIfEntry.setIndexNames(
    (0, "H3C-BFD-STD-MIB", "h3cBfdIfIndex"),
)
if mibBuilder.loadTexts:
    h3cBfdIfEntry.setStatus("current")
_H3cBfdIfIndex_Type = InterfaceIndex
_H3cBfdIfIndex_Object = MibTableColumn
h3cBfdIfIndex = _H3cBfdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 1),
    _H3cBfdIfIndex_Type()
)
h3cBfdIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cBfdIfIndex.setStatus("current")
_H3cBfdIfDesiredMinTxInterval_Type = BfdInterval
_H3cBfdIfDesiredMinTxInterval_Object = MibTableColumn
h3cBfdIfDesiredMinTxInterval = _H3cBfdIfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 2),
    _H3cBfdIfDesiredMinTxInterval_Type()
)
h3cBfdIfDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBfdIfDesiredMinTxInterval.setStatus("current")
_H3cBfdIfDesiredMinRxInterval_Type = BfdInterval
_H3cBfdIfDesiredMinRxInterval_Object = MibTableColumn
h3cBfdIfDesiredMinRxInterval = _H3cBfdIfDesiredMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 3),
    _H3cBfdIfDesiredMinRxInterval_Type()
)
h3cBfdIfDesiredMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBfdIfDesiredMinRxInterval.setStatus("current")
_H3cBfdIfDetectMult_Type = Unsigned32
_H3cBfdIfDetectMult_Object = MibTableColumn
h3cBfdIfDetectMult = _H3cBfdIfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 4),
    _H3cBfdIfDetectMult_Type()
)
h3cBfdIfDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBfdIfDetectMult.setStatus("current")


class _H3cBfdIfAuthType_Type(Integer32):
    """Custom type h3cBfdIfAuthType based on Integer32"""
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


_H3cBfdIfAuthType_Type.__name__ = "Integer32"
_H3cBfdIfAuthType_Object = MibTableColumn
h3cBfdIfAuthType = _H3cBfdIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 5),
    _H3cBfdIfAuthType_Type()
)
h3cBfdIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdIfAuthType.setStatus("current")
_H3cBfdSessTable_Object = MibTable
h3cBfdSessTable = _H3cBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    h3cBfdSessTable.setStatus("current")
_H3cBfdSessEntry_Object = MibTableRow
h3cBfdSessEntry = _H3cBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1)
)
h3cBfdSessEntry.setIndexNames(
    (0, "H3C-BFD-STD-MIB", "h3cBfdSessIfIndex"),
    (0, "H3C-BFD-STD-MIB", "h3cBfdSessIndex"),
)
if mibBuilder.loadTexts:
    h3cBfdSessEntry.setStatus("current")
_H3cBfdSessIfIndex_Type = InterfaceIndex
_H3cBfdSessIfIndex_Object = MibTableColumn
h3cBfdSessIfIndex = _H3cBfdSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 1),
    _H3cBfdSessIfIndex_Type()
)
h3cBfdSessIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cBfdSessIfIndex.setStatus("current")
_H3cBfdSessIndex_Type = BfdSessIndexTC
_H3cBfdSessIndex_Object = MibTableColumn
h3cBfdSessIndex = _H3cBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 2),
    _H3cBfdSessIndex_Type()
)
h3cBfdSessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cBfdSessIndex.setStatus("current")


class _H3cBfdSessAppSupportId_Type(Bits):
    """Custom type h3cBfdSessAppSupportId based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("isis", 2),
          ("mpls", 4),
          ("none", 0),
          ("ospf", 1))
    )

_H3cBfdSessAppSupportId_Type.__name__ = "Bits"
_H3cBfdSessAppSupportId_Object = MibTableColumn
h3cBfdSessAppSupportId = _H3cBfdSessAppSupportId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 3),
    _H3cBfdSessAppSupportId_Type()
)
h3cBfdSessAppSupportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessAppSupportId.setStatus("current")


class _H3cBfdSessLocalDiscr_Type(Unsigned32):
    """Custom type h3cBfdSessLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cBfdSessLocalDiscr_Type.__name__ = "Unsigned32"
_H3cBfdSessLocalDiscr_Object = MibTableColumn
h3cBfdSessLocalDiscr = _H3cBfdSessLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 4),
    _H3cBfdSessLocalDiscr_Type()
)
h3cBfdSessLocalDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessLocalDiscr.setStatus("current")


class _H3cBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type h3cBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_H3cBfdSessRemoteDiscr_Object = MibTableColumn
h3cBfdSessRemoteDiscr = _H3cBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 5),
    _H3cBfdSessRemoteDiscr_Type()
)
h3cBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessRemoteDiscr.setStatus("current")


class _H3cBfdSessDstPort_Type(InetPortNumber):
    """Custom type h3cBfdSessDstPort based on InetPortNumber"""
    defaultValue = 3784


_H3cBfdSessDstPort_Object = MibTableColumn
h3cBfdSessDstPort = _H3cBfdSessDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 6),
    _H3cBfdSessDstPort_Type()
)
h3cBfdSessDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessDstPort.setStatus("current")


class _H3cBfdSessOperMode_Type(Integer32):
    """Custom type h3cBfdSessOperMode based on Integer32"""
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


_H3cBfdSessOperMode_Type.__name__ = "Integer32"
_H3cBfdSessOperMode_Object = MibTableColumn
h3cBfdSessOperMode = _H3cBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 7),
    _H3cBfdSessOperMode_Type()
)
h3cBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessOperMode.setStatus("current")
_H3cBfdSessAddrType_Type = InetAddressType
_H3cBfdSessAddrType_Object = MibTableColumn
h3cBfdSessAddrType = _H3cBfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 8),
    _H3cBfdSessAddrType_Type()
)
h3cBfdSessAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessAddrType.setStatus("current")
_H3cBfdSessLocalAddr_Type = InetAddress
_H3cBfdSessLocalAddr_Object = MibTableColumn
h3cBfdSessLocalAddr = _H3cBfdSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 9),
    _H3cBfdSessLocalAddr_Type()
)
h3cBfdSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessLocalAddr.setStatus("current")
_H3cBfdSessRemoteAddr_Type = InetAddress
_H3cBfdSessRemoteAddr_Object = MibTableColumn
h3cBfdSessRemoteAddr = _H3cBfdSessRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 10),
    _H3cBfdSessRemoteAddr_Type()
)
h3cBfdSessRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessRemoteAddr.setStatus("current")


class _H3cBfdSessLocalDiag_Type(BfdDiag):
    """Custom type h3cBfdSessLocalDiag based on BfdDiag"""


_H3cBfdSessLocalDiag_Object = MibTableColumn
h3cBfdSessLocalDiag = _H3cBfdSessLocalDiag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 11),
    _H3cBfdSessLocalDiag_Type()
)
h3cBfdSessLocalDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessLocalDiag.setStatus("current")


class _H3cBfdSessState_Type(Integer32):
    """Custom type h3cBfdSessState based on Integer32"""
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


_H3cBfdSessState_Type.__name__ = "Integer32"
_H3cBfdSessState_Object = MibTableColumn
h3cBfdSessState = _H3cBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 12),
    _H3cBfdSessState_Type()
)
h3cBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessState.setStatus("current")


class _H3cBfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type h3cBfdSessControlPlanIndepFlag based on TruthValue"""


_H3cBfdSessControlPlanIndepFlag_Object = MibTableColumn
h3cBfdSessControlPlanIndepFlag = _H3cBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 13),
    _H3cBfdSessControlPlanIndepFlag_Type()
)
h3cBfdSessControlPlanIndepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessControlPlanIndepFlag.setStatus("current")


class _H3cBfdSessAuthFlag_Type(TruthValue):
    """Custom type h3cBfdSessAuthFlag based on TruthValue"""


_H3cBfdSessAuthFlag_Object = MibTableColumn
h3cBfdSessAuthFlag = _H3cBfdSessAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 14),
    _H3cBfdSessAuthFlag_Type()
)
h3cBfdSessAuthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessAuthFlag.setStatus("current")


class _H3cBfdSessDemandModeFlag_Type(TruthValue):
    """Custom type h3cBfdSessDemandModeFlag based on TruthValue"""


_H3cBfdSessDemandModeFlag_Object = MibTableColumn
h3cBfdSessDemandModeFlag = _H3cBfdSessDemandModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 15),
    _H3cBfdSessDemandModeFlag_Type()
)
h3cBfdSessDemandModeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessDemandModeFlag.setStatus("current")
_H3cBfdSessStatTable_Object = MibTable
h3cBfdSessStatTable = _H3cBfdSessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4)
)
if mibBuilder.loadTexts:
    h3cBfdSessStatTable.setStatus("current")
_H3cBfdSessStatEntry_Object = MibTableRow
h3cBfdSessStatEntry = _H3cBfdSessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cBfdSessStatEntry.setStatus("current")
_H3cBfdSessStatPktInHC_Type = Counter64
_H3cBfdSessStatPktInHC_Object = MibTableColumn
h3cBfdSessStatPktInHC = _H3cBfdSessStatPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 1),
    _H3cBfdSessStatPktInHC_Type()
)
h3cBfdSessStatPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessStatPktInHC.setStatus("current")
_H3cBfdSessStatPktOutHC_Type = Counter64
_H3cBfdSessStatPktOutHC_Object = MibTableColumn
h3cBfdSessStatPktOutHC = _H3cBfdSessStatPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 2),
    _H3cBfdSessStatPktOutHC_Type()
)
h3cBfdSessStatPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessStatPktOutHC.setStatus("current")
_H3cBfdSessStatDownCount_Type = Counter32
_H3cBfdSessStatDownCount_Object = MibTableColumn
h3cBfdSessStatDownCount = _H3cBfdSessStatDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 3),
    _H3cBfdSessStatDownCount_Type()
)
h3cBfdSessStatDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessStatDownCount.setStatus("current")
_H3cBfdSessStatPktDiscard_Type = Counter64
_H3cBfdSessStatPktDiscard_Object = MibTableColumn
h3cBfdSessStatPktDiscard = _H3cBfdSessStatPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 4),
    _H3cBfdSessStatPktDiscard_Type()
)
h3cBfdSessStatPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessStatPktDiscard.setStatus("current")
_H3cBfdSessStatPktLost_Type = Counter64
_H3cBfdSessStatPktLost_Object = MibTableColumn
h3cBfdSessStatPktLost = _H3cBfdSessStatPktLost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 5),
    _H3cBfdSessStatPktLost_Type()
)
h3cBfdSessStatPktLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessStatPktLost.setStatus("current")
_H3cBfdSessPerfTable_Object = MibTable
h3cBfdSessPerfTable = _H3cBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    h3cBfdSessPerfTable.setStatus("current")
_H3cBfdSessPerfEntry_Object = MibTableRow
h3cBfdSessPerfEntry = _H3cBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cBfdSessPerfEntry.setStatus("current")
_H3cBfdSessPerfCreatTime_Type = TimeStamp
_H3cBfdSessPerfCreatTime_Object = MibTableColumn
h3cBfdSessPerfCreatTime = _H3cBfdSessPerfCreatTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 1),
    _H3cBfdSessPerfCreatTime_Type()
)
h3cBfdSessPerfCreatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessPerfCreatTime.setStatus("current")
_H3cBfdSessPerfLastUpTime_Type = TimeStamp
_H3cBfdSessPerfLastUpTime_Object = MibTableColumn
h3cBfdSessPerfLastUpTime = _H3cBfdSessPerfLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 2),
    _H3cBfdSessPerfLastUpTime_Type()
)
h3cBfdSessPerfLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessPerfLastUpTime.setStatus("current")
_H3cBfdSessPerfLastDownTime_Type = TimeStamp
_H3cBfdSessPerfLastDownTime_Object = MibTableColumn
h3cBfdSessPerfLastDownTime = _H3cBfdSessPerfLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 3),
    _H3cBfdSessPerfLastDownTime_Type()
)
h3cBfdSessPerfLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBfdSessPerfLastDownTime.setStatus("current")
_H3cBfdConformance_ObjectIdentity = ObjectIdentity
h3cBfdConformance = _H3cBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 2)
)
h3cBfdSessEntry.registerAugmentions(
    ("H3C-BFD-STD-MIB",
     "h3cBfdSessStatEntry")
)
h3cBfdSessStatEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())
h3cBfdSessEntry.registerAugmentions(
    ("H3C-BFD-STD-MIB",
     "h3cBfdSessPerfEntry")
)
h3cBfdSessPerfEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

h3cBfdSessStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0, 1)
)
h3cBfdSessStateChange.setObjects(
      *(("H3C-BFD-STD-MIB", "h3cBfdSessIfIndex"),
        ("H3C-BFD-STD-MIB", "h3cBfdSessIndex"),
        ("H3C-BFD-STD-MIB", "h3cBfdSessState"))
)
if mibBuilder.loadTexts:
    h3cBfdSessStateChange.setStatus(
        "current"
    )

h3cBfdSessAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0, 2)
)
h3cBfdSessAuthFail.setObjects(
    ("H3C-BFD-STD-MIB", "h3cBfdIfIndex")
)
if mibBuilder.loadTexts:
    h3cBfdSessAuthFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-BFD-STD-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "h3cBfdMIB": h3cBfdMIB,
       "h3cBfdNotifications": h3cBfdNotifications,
       "h3cBfdSessStateChange": h3cBfdSessStateChange,
       "h3cBfdSessAuthFail": h3cBfdSessAuthFail,
       "h3cBfdObjects": h3cBfdObjects,
       "h3cBfdGlobalObjects": h3cBfdGlobalObjects,
       "h3cBfdVersionNumber": h3cBfdVersionNumber,
       "h3cBfdSysInitMode": h3cBfdSysInitMode,
       "h3cBfdSessNotificationsEnable": h3cBfdSessNotificationsEnable,
       "h3cBfdIfTable": h3cBfdIfTable,
       "h3cBfdIfEntry": h3cBfdIfEntry,
       "h3cBfdIfIndex": h3cBfdIfIndex,
       "h3cBfdIfDesiredMinTxInterval": h3cBfdIfDesiredMinTxInterval,
       "h3cBfdIfDesiredMinRxInterval": h3cBfdIfDesiredMinRxInterval,
       "h3cBfdIfDetectMult": h3cBfdIfDetectMult,
       "h3cBfdIfAuthType": h3cBfdIfAuthType,
       "h3cBfdSessTable": h3cBfdSessTable,
       "h3cBfdSessEntry": h3cBfdSessEntry,
       "h3cBfdSessIfIndex": h3cBfdSessIfIndex,
       "h3cBfdSessIndex": h3cBfdSessIndex,
       "h3cBfdSessAppSupportId": h3cBfdSessAppSupportId,
       "h3cBfdSessLocalDiscr": h3cBfdSessLocalDiscr,
       "h3cBfdSessRemoteDiscr": h3cBfdSessRemoteDiscr,
       "h3cBfdSessDstPort": h3cBfdSessDstPort,
       "h3cBfdSessOperMode": h3cBfdSessOperMode,
       "h3cBfdSessAddrType": h3cBfdSessAddrType,
       "h3cBfdSessLocalAddr": h3cBfdSessLocalAddr,
       "h3cBfdSessRemoteAddr": h3cBfdSessRemoteAddr,
       "h3cBfdSessLocalDiag": h3cBfdSessLocalDiag,
       "h3cBfdSessState": h3cBfdSessState,
       "h3cBfdSessControlPlanIndepFlag": h3cBfdSessControlPlanIndepFlag,
       "h3cBfdSessAuthFlag": h3cBfdSessAuthFlag,
       "h3cBfdSessDemandModeFlag": h3cBfdSessDemandModeFlag,
       "h3cBfdSessStatTable": h3cBfdSessStatTable,
       "h3cBfdSessStatEntry": h3cBfdSessStatEntry,
       "h3cBfdSessStatPktInHC": h3cBfdSessStatPktInHC,
       "h3cBfdSessStatPktOutHC": h3cBfdSessStatPktOutHC,
       "h3cBfdSessStatDownCount": h3cBfdSessStatDownCount,
       "h3cBfdSessStatPktDiscard": h3cBfdSessStatPktDiscard,
       "h3cBfdSessStatPktLost": h3cBfdSessStatPktLost,
       "h3cBfdSessPerfTable": h3cBfdSessPerfTable,
       "h3cBfdSessPerfEntry": h3cBfdSessPerfEntry,
       "h3cBfdSessPerfCreatTime": h3cBfdSessPerfCreatTime,
       "h3cBfdSessPerfLastUpTime": h3cBfdSessPerfLastUpTime,
       "h3cBfdSessPerfLastDownTime": h3cBfdSessPerfLastDownTime,
       "h3cBfdConformance": h3cBfdConformance}
)
