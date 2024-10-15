# SNMP MIB module (HPN-ICF-BFD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-BFD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:31 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72)
)
hpnicfBfdMIB.setRevisions(
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

_HpnicfBfdNotifications_ObjectIdentity = ObjectIdentity
hpnicfBfdNotifications = _HpnicfBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0)
)
_HpnicfBfdObjects_ObjectIdentity = ObjectIdentity
hpnicfBfdObjects = _HpnicfBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1)
)
_HpnicfBfdGlobalObjects_ObjectIdentity = ObjectIdentity
hpnicfBfdGlobalObjects = _HpnicfBfdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1)
)


class _HpnicfBfdVersionNumber_Type(Unsigned32):
    """Custom type hpnicfBfdVersionNumber based on Unsigned32"""
    defaultValue = 1


_HpnicfBfdVersionNumber_Object = MibScalar
hpnicfBfdVersionNumber = _HpnicfBfdVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 1),
    _HpnicfBfdVersionNumber_Type()
)
hpnicfBfdVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdVersionNumber.setStatus("current")


class _HpnicfBfdSysInitMode_Type(Integer32):
    """Custom type hpnicfBfdSysInitMode based on Integer32"""
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


_HpnicfBfdSysInitMode_Type.__name__ = "Integer32"
_HpnicfBfdSysInitMode_Object = MibScalar
hpnicfBfdSysInitMode = _HpnicfBfdSysInitMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 2),
    _HpnicfBfdSysInitMode_Type()
)
hpnicfBfdSysInitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBfdSysInitMode.setStatus("current")


class _HpnicfBfdSessNotificationsEnable_Type(TruthValue):
    """Custom type hpnicfBfdSessNotificationsEnable based on TruthValue"""


_HpnicfBfdSessNotificationsEnable_Object = MibScalar
hpnicfBfdSessNotificationsEnable = _HpnicfBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 3),
    _HpnicfBfdSessNotificationsEnable_Type()
)
hpnicfBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBfdSessNotificationsEnable.setStatus("current")


class _HpnicfBfdSessNumberLimit_Type(Unsigned32):
    """Custom type hpnicfBfdSessNumberLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfBfdSessNumberLimit_Type.__name__ = "Unsigned32"
_HpnicfBfdSessNumberLimit_Object = MibScalar
hpnicfBfdSessNumberLimit = _HpnicfBfdSessNumberLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 1, 4),
    _HpnicfBfdSessNumberLimit_Type()
)
hpnicfBfdSessNumberLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessNumberLimit.setStatus("current")
_HpnicfBfdIfTable_Object = MibTable
hpnicfBfdIfTable = _HpnicfBfdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfBfdIfTable.setStatus("current")
_HpnicfBfdIfEntry_Object = MibTableRow
hpnicfBfdIfEntry = _HpnicfBfdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1)
)
hpnicfBfdIfEntry.setIndexNames(
    (0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfBfdIfEntry.setStatus("current")
_HpnicfBfdIfIndex_Type = InterfaceIndex
_HpnicfBfdIfIndex_Object = MibTableColumn
hpnicfBfdIfIndex = _HpnicfBfdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 1),
    _HpnicfBfdIfIndex_Type()
)
hpnicfBfdIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfBfdIfIndex.setStatus("current")
_HpnicfBfdIfDesiredMinTxInterval_Type = BfdInterval
_HpnicfBfdIfDesiredMinTxInterval_Object = MibTableColumn
hpnicfBfdIfDesiredMinTxInterval = _HpnicfBfdIfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 2),
    _HpnicfBfdIfDesiredMinTxInterval_Type()
)
hpnicfBfdIfDesiredMinTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBfdIfDesiredMinTxInterval.setStatus("current")
_HpnicfBfdIfDesiredMinRxInterval_Type = BfdInterval
_HpnicfBfdIfDesiredMinRxInterval_Object = MibTableColumn
hpnicfBfdIfDesiredMinRxInterval = _HpnicfBfdIfDesiredMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 3),
    _HpnicfBfdIfDesiredMinRxInterval_Type()
)
hpnicfBfdIfDesiredMinRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBfdIfDesiredMinRxInterval.setStatus("current")
_HpnicfBfdIfDetectMult_Type = Unsigned32
_HpnicfBfdIfDetectMult_Object = MibTableColumn
hpnicfBfdIfDetectMult = _HpnicfBfdIfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 4),
    _HpnicfBfdIfDetectMult_Type()
)
hpnicfBfdIfDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBfdIfDetectMult.setStatus("current")


class _HpnicfBfdIfAuthType_Type(Integer32):
    """Custom type hpnicfBfdIfAuthType based on Integer32"""
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


_HpnicfBfdIfAuthType_Type.__name__ = "Integer32"
_HpnicfBfdIfAuthType_Object = MibTableColumn
hpnicfBfdIfAuthType = _HpnicfBfdIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 2, 1, 5),
    _HpnicfBfdIfAuthType_Type()
)
hpnicfBfdIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdIfAuthType.setStatus("current")
_HpnicfBfdSessTable_Object = MibTable
hpnicfBfdSessTable = _HpnicfBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfBfdSessTable.setStatus("current")
_HpnicfBfdSessEntry_Object = MibTableRow
hpnicfBfdSessEntry = _HpnicfBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1)
)
hpnicfBfdSessEntry.setIndexNames(
    (0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"),
    (0, "HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"),
)
if mibBuilder.loadTexts:
    hpnicfBfdSessEntry.setStatus("current")
_HpnicfBfdSessIfIndex_Type = InterfaceIndex
_HpnicfBfdSessIfIndex_Object = MibTableColumn
hpnicfBfdSessIfIndex = _HpnicfBfdSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 1),
    _HpnicfBfdSessIfIndex_Type()
)
hpnicfBfdSessIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfBfdSessIfIndex.setStatus("current")
_HpnicfBfdSessIndex_Type = BfdSessIndexTC
_HpnicfBfdSessIndex_Object = MibTableColumn
hpnicfBfdSessIndex = _HpnicfBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 2),
    _HpnicfBfdSessIndex_Type()
)
hpnicfBfdSessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfBfdSessIndex.setStatus("current")


class _HpnicfBfdSessAppSupportId_Type(Bits):
    """Custom type hpnicfBfdSessAppSupportId based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("isis", 2),
          ("mpls", 4),
          ("none", 0),
          ("ospf", 1))
    )

_HpnicfBfdSessAppSupportId_Type.__name__ = "Bits"
_HpnicfBfdSessAppSupportId_Object = MibTableColumn
hpnicfBfdSessAppSupportId = _HpnicfBfdSessAppSupportId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 3),
    _HpnicfBfdSessAppSupportId_Type()
)
hpnicfBfdSessAppSupportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessAppSupportId.setStatus("current")


class _HpnicfBfdSessLocalDiscr_Type(Unsigned32):
    """Custom type hpnicfBfdSessLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfBfdSessLocalDiscr_Type.__name__ = "Unsigned32"
_HpnicfBfdSessLocalDiscr_Object = MibTableColumn
hpnicfBfdSessLocalDiscr = _HpnicfBfdSessLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 4),
    _HpnicfBfdSessLocalDiscr_Type()
)
hpnicfBfdSessLocalDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessLocalDiscr.setStatus("current")


class _HpnicfBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type hpnicfBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_HpnicfBfdSessRemoteDiscr_Object = MibTableColumn
hpnicfBfdSessRemoteDiscr = _HpnicfBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 5),
    _HpnicfBfdSessRemoteDiscr_Type()
)
hpnicfBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessRemoteDiscr.setStatus("current")


class _HpnicfBfdSessDstPort_Type(InetPortNumber):
    """Custom type hpnicfBfdSessDstPort based on InetPortNumber"""
    defaultValue = 3784


_HpnicfBfdSessDstPort_Object = MibTableColumn
hpnicfBfdSessDstPort = _HpnicfBfdSessDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 6),
    _HpnicfBfdSessDstPort_Type()
)
hpnicfBfdSessDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessDstPort.setStatus("current")


class _HpnicfBfdSessOperMode_Type(Integer32):
    """Custom type hpnicfBfdSessOperMode based on Integer32"""
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


_HpnicfBfdSessOperMode_Type.__name__ = "Integer32"
_HpnicfBfdSessOperMode_Object = MibTableColumn
hpnicfBfdSessOperMode = _HpnicfBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 7),
    _HpnicfBfdSessOperMode_Type()
)
hpnicfBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessOperMode.setStatus("current")
_HpnicfBfdSessAddrType_Type = InetAddressType
_HpnicfBfdSessAddrType_Object = MibTableColumn
hpnicfBfdSessAddrType = _HpnicfBfdSessAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 8),
    _HpnicfBfdSessAddrType_Type()
)
hpnicfBfdSessAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessAddrType.setStatus("current")
_HpnicfBfdSessLocalAddr_Type = InetAddress
_HpnicfBfdSessLocalAddr_Object = MibTableColumn
hpnicfBfdSessLocalAddr = _HpnicfBfdSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 9),
    _HpnicfBfdSessLocalAddr_Type()
)
hpnicfBfdSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessLocalAddr.setStatus("current")
_HpnicfBfdSessRemoteAddr_Type = InetAddress
_HpnicfBfdSessRemoteAddr_Object = MibTableColumn
hpnicfBfdSessRemoteAddr = _HpnicfBfdSessRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 10),
    _HpnicfBfdSessRemoteAddr_Type()
)
hpnicfBfdSessRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessRemoteAddr.setStatus("current")


class _HpnicfBfdSessLocalDiag_Type(BfdDiag):
    """Custom type hpnicfBfdSessLocalDiag based on BfdDiag"""


_HpnicfBfdSessLocalDiag_Object = MibTableColumn
hpnicfBfdSessLocalDiag = _HpnicfBfdSessLocalDiag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 11),
    _HpnicfBfdSessLocalDiag_Type()
)
hpnicfBfdSessLocalDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessLocalDiag.setStatus("current")


class _HpnicfBfdSessState_Type(Integer32):
    """Custom type hpnicfBfdSessState based on Integer32"""
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


_HpnicfBfdSessState_Type.__name__ = "Integer32"
_HpnicfBfdSessState_Object = MibTableColumn
hpnicfBfdSessState = _HpnicfBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 12),
    _HpnicfBfdSessState_Type()
)
hpnicfBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessState.setStatus("current")


class _HpnicfBfdSessControlPlanIndepFlag_Type(TruthValue):
    """Custom type hpnicfBfdSessControlPlanIndepFlag based on TruthValue"""


_HpnicfBfdSessControlPlanIndepFlag_Object = MibTableColumn
hpnicfBfdSessControlPlanIndepFlag = _HpnicfBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 13),
    _HpnicfBfdSessControlPlanIndepFlag_Type()
)
hpnicfBfdSessControlPlanIndepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessControlPlanIndepFlag.setStatus("current")


class _HpnicfBfdSessAuthFlag_Type(TruthValue):
    """Custom type hpnicfBfdSessAuthFlag based on TruthValue"""


_HpnicfBfdSessAuthFlag_Object = MibTableColumn
hpnicfBfdSessAuthFlag = _HpnicfBfdSessAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 14),
    _HpnicfBfdSessAuthFlag_Type()
)
hpnicfBfdSessAuthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessAuthFlag.setStatus("current")


class _HpnicfBfdSessDemandModeFlag_Type(TruthValue):
    """Custom type hpnicfBfdSessDemandModeFlag based on TruthValue"""


_HpnicfBfdSessDemandModeFlag_Object = MibTableColumn
hpnicfBfdSessDemandModeFlag = _HpnicfBfdSessDemandModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 3, 1, 15),
    _HpnicfBfdSessDemandModeFlag_Type()
)
hpnicfBfdSessDemandModeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessDemandModeFlag.setStatus("current")
_HpnicfBfdSessStatTable_Object = MibTable
hpnicfBfdSessStatTable = _HpnicfBfdSessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfBfdSessStatTable.setStatus("current")
_HpnicfBfdSessStatEntry_Object = MibTableRow
hpnicfBfdSessStatEntry = _HpnicfBfdSessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfBfdSessStatEntry.setStatus("current")
_HpnicfBfdSessStatPktInHC_Type = Counter64
_HpnicfBfdSessStatPktInHC_Object = MibTableColumn
hpnicfBfdSessStatPktInHC = _HpnicfBfdSessStatPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 1),
    _HpnicfBfdSessStatPktInHC_Type()
)
hpnicfBfdSessStatPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessStatPktInHC.setStatus("current")
_HpnicfBfdSessStatPktOutHC_Type = Counter64
_HpnicfBfdSessStatPktOutHC_Object = MibTableColumn
hpnicfBfdSessStatPktOutHC = _HpnicfBfdSessStatPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 2),
    _HpnicfBfdSessStatPktOutHC_Type()
)
hpnicfBfdSessStatPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessStatPktOutHC.setStatus("current")
_HpnicfBfdSessStatDownCount_Type = Counter32
_HpnicfBfdSessStatDownCount_Object = MibTableColumn
hpnicfBfdSessStatDownCount = _HpnicfBfdSessStatDownCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 3),
    _HpnicfBfdSessStatDownCount_Type()
)
hpnicfBfdSessStatDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessStatDownCount.setStatus("current")
_HpnicfBfdSessStatPktDiscard_Type = Counter64
_HpnicfBfdSessStatPktDiscard_Object = MibTableColumn
hpnicfBfdSessStatPktDiscard = _HpnicfBfdSessStatPktDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 4),
    _HpnicfBfdSessStatPktDiscard_Type()
)
hpnicfBfdSessStatPktDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessStatPktDiscard.setStatus("current")
_HpnicfBfdSessStatPktLost_Type = Counter64
_HpnicfBfdSessStatPktLost_Object = MibTableColumn
hpnicfBfdSessStatPktLost = _HpnicfBfdSessStatPktLost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 4, 1, 5),
    _HpnicfBfdSessStatPktLost_Type()
)
hpnicfBfdSessStatPktLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessStatPktLost.setStatus("current")
_HpnicfBfdSessPerfTable_Object = MibTable
hpnicfBfdSessPerfTable = _HpnicfBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfBfdSessPerfTable.setStatus("current")
_HpnicfBfdSessPerfEntry_Object = MibTableRow
hpnicfBfdSessPerfEntry = _HpnicfBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfBfdSessPerfEntry.setStatus("current")
_HpnicfBfdSessPerfCreatTime_Type = TimeStamp
_HpnicfBfdSessPerfCreatTime_Object = MibTableColumn
hpnicfBfdSessPerfCreatTime = _HpnicfBfdSessPerfCreatTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 1),
    _HpnicfBfdSessPerfCreatTime_Type()
)
hpnicfBfdSessPerfCreatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessPerfCreatTime.setStatus("current")
_HpnicfBfdSessPerfLastUpTime_Type = TimeStamp
_HpnicfBfdSessPerfLastUpTime_Object = MibTableColumn
hpnicfBfdSessPerfLastUpTime = _HpnicfBfdSessPerfLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 2),
    _HpnicfBfdSessPerfLastUpTime_Type()
)
hpnicfBfdSessPerfLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessPerfLastUpTime.setStatus("current")
_HpnicfBfdSessPerfLastDownTime_Type = TimeStamp
_HpnicfBfdSessPerfLastDownTime_Object = MibTableColumn
hpnicfBfdSessPerfLastDownTime = _HpnicfBfdSessPerfLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 1, 5, 1, 3),
    _HpnicfBfdSessPerfLastDownTime_Type()
)
hpnicfBfdSessPerfLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBfdSessPerfLastDownTime.setStatus("current")
_HpnicfBfdConformance_ObjectIdentity = ObjectIdentity
hpnicfBfdConformance = _HpnicfBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 2)
)
hpnicfBfdSessEntry.registerAugmentions(
    ("HPN-ICF-BFD-STD-MIB",
     "hpnicfBfdSessStatEntry")
)
hpnicfBfdSessStatEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())
hpnicfBfdSessEntry.registerAugmentions(
    ("HPN-ICF-BFD-STD-MIB",
     "hpnicfBfdSessPerfEntry")
)
hpnicfBfdSessPerfEntry.setIndexNames(*hpnicfBfdSessEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hpnicfBfdSessStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 1)
)
hpnicfBfdSessStateChange.setObjects(
      *(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
)
if mibBuilder.loadTexts:
    hpnicfBfdSessStateChange.setStatus(
        "current"
    )

hpnicfBfdSessAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 2)
)
hpnicfBfdSessAuthFail.setObjects(
    ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdIfIndex")
)
if mibBuilder.loadTexts:
    hpnicfBfdSessAuthFail.setStatus(
        "current"
    )

hpnicfBfdSessStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 3)
)
hpnicfBfdSessStateUp.setObjects(
      *(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
)
if mibBuilder.loadTexts:
    hpnicfBfdSessStateUp.setStatus(
        "current"
    )

hpnicfBfdSessStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 4)
)
hpnicfBfdSessStateDown.setObjects(
      *(("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIfIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessIndex"),
        ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessState"))
)
if mibBuilder.loadTexts:
    hpnicfBfdSessStateDown.setStatus(
        "current"
    )

hpnicfBfdSessReachLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72, 0, 5)
)
hpnicfBfdSessReachLimit.setObjects(
    ("HPN-ICF-BFD-STD-MIB", "hpnicfBfdSessNumberLimit")
)
if mibBuilder.loadTexts:
    hpnicfBfdSessReachLimit.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-BFD-STD-MIB",
    **{"BfdSessIndexTC": BfdSessIndexTC,
       "BfdInterval": BfdInterval,
       "BfdDiag": BfdDiag,
       "hpnicfBfdMIB": hpnicfBfdMIB,
       "hpnicfBfdNotifications": hpnicfBfdNotifications,
       "hpnicfBfdSessStateChange": hpnicfBfdSessStateChange,
       "hpnicfBfdSessAuthFail": hpnicfBfdSessAuthFail,
       "hpnicfBfdSessStateUp": hpnicfBfdSessStateUp,
       "hpnicfBfdSessStateDown": hpnicfBfdSessStateDown,
       "hpnicfBfdSessReachLimit": hpnicfBfdSessReachLimit,
       "hpnicfBfdObjects": hpnicfBfdObjects,
       "hpnicfBfdGlobalObjects": hpnicfBfdGlobalObjects,
       "hpnicfBfdVersionNumber": hpnicfBfdVersionNumber,
       "hpnicfBfdSysInitMode": hpnicfBfdSysInitMode,
       "hpnicfBfdSessNotificationsEnable": hpnicfBfdSessNotificationsEnable,
       "hpnicfBfdSessNumberLimit": hpnicfBfdSessNumberLimit,
       "hpnicfBfdIfTable": hpnicfBfdIfTable,
       "hpnicfBfdIfEntry": hpnicfBfdIfEntry,
       "hpnicfBfdIfIndex": hpnicfBfdIfIndex,
       "hpnicfBfdIfDesiredMinTxInterval": hpnicfBfdIfDesiredMinTxInterval,
       "hpnicfBfdIfDesiredMinRxInterval": hpnicfBfdIfDesiredMinRxInterval,
       "hpnicfBfdIfDetectMult": hpnicfBfdIfDetectMult,
       "hpnicfBfdIfAuthType": hpnicfBfdIfAuthType,
       "hpnicfBfdSessTable": hpnicfBfdSessTable,
       "hpnicfBfdSessEntry": hpnicfBfdSessEntry,
       "hpnicfBfdSessIfIndex": hpnicfBfdSessIfIndex,
       "hpnicfBfdSessIndex": hpnicfBfdSessIndex,
       "hpnicfBfdSessAppSupportId": hpnicfBfdSessAppSupportId,
       "hpnicfBfdSessLocalDiscr": hpnicfBfdSessLocalDiscr,
       "hpnicfBfdSessRemoteDiscr": hpnicfBfdSessRemoteDiscr,
       "hpnicfBfdSessDstPort": hpnicfBfdSessDstPort,
       "hpnicfBfdSessOperMode": hpnicfBfdSessOperMode,
       "hpnicfBfdSessAddrType": hpnicfBfdSessAddrType,
       "hpnicfBfdSessLocalAddr": hpnicfBfdSessLocalAddr,
       "hpnicfBfdSessRemoteAddr": hpnicfBfdSessRemoteAddr,
       "hpnicfBfdSessLocalDiag": hpnicfBfdSessLocalDiag,
       "hpnicfBfdSessState": hpnicfBfdSessState,
       "hpnicfBfdSessControlPlanIndepFlag": hpnicfBfdSessControlPlanIndepFlag,
       "hpnicfBfdSessAuthFlag": hpnicfBfdSessAuthFlag,
       "hpnicfBfdSessDemandModeFlag": hpnicfBfdSessDemandModeFlag,
       "hpnicfBfdSessStatTable": hpnicfBfdSessStatTable,
       "hpnicfBfdSessStatEntry": hpnicfBfdSessStatEntry,
       "hpnicfBfdSessStatPktInHC": hpnicfBfdSessStatPktInHC,
       "hpnicfBfdSessStatPktOutHC": hpnicfBfdSessStatPktOutHC,
       "hpnicfBfdSessStatDownCount": hpnicfBfdSessStatDownCount,
       "hpnicfBfdSessStatPktDiscard": hpnicfBfdSessStatPktDiscard,
       "hpnicfBfdSessStatPktLost": hpnicfBfdSessStatPktLost,
       "hpnicfBfdSessPerfTable": hpnicfBfdSessPerfTable,
       "hpnicfBfdSessPerfEntry": hpnicfBfdSessPerfEntry,
       "hpnicfBfdSessPerfCreatTime": hpnicfBfdSessPerfCreatTime,
       "hpnicfBfdSessPerfLastUpTime": hpnicfBfdSessPerfLastUpTime,
       "hpnicfBfdSessPerfLastDownTime": hpnicfBfdSessPerfLastDownTime,
       "hpnicfBfdConformance": hpnicfBfdConformance}
)
