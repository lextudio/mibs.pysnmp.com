# SNMP MIB module (Wellfleet-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:55 2024
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

(wfPppGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfPppGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfPppLineTable_Object = MibTable
wfPppLineTable = _WfPppLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1)
)
if mibBuilder.loadTexts:
    wfPppLineTable.setStatus("mandatory")
_WfPppLineEntry_Object = MibTableRow
wfPppLineEntry = _WfPppLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1)
)
wfPppLineEntry.setIndexNames(
    (0, "Wellfleet-PPP-MIB", "wfPppLineLineNumber"),
    (0, "Wellfleet-PPP-MIB", "wfPppLineLLIndex"),
)
if mibBuilder.loadTexts:
    wfPppLineEntry.setStatus("mandatory")


class _WfPppLineDelete_Type(Integer32):
    """Custom type wfPppLineDelete based on Integer32"""
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


_WfPppLineDelete_Type.__name__ = "Integer32"
_WfPppLineDelete_Object = MibTableColumn
wfPppLineDelete = _WfPppLineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 1),
    _WfPppLineDelete_Type()
)
wfPppLineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineDelete.setStatus("mandatory")


class _WfPppLineDisable_Type(Integer32):
    """Custom type wfPppLineDisable based on Integer32"""
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


_WfPppLineDisable_Type.__name__ = "Integer32"
_WfPppLineDisable_Object = MibTableColumn
wfPppLineDisable = _WfPppLineDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 2),
    _WfPppLineDisable_Type()
)
wfPppLineDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineDisable.setStatus("mandatory")


class _WfPppLineState_Type(Integer32):
    """Custom type wfPppLineState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("loopedback", 4),
          ("notpresent", 20),
          ("up", 1))
    )


_WfPppLineState_Type.__name__ = "Integer32"
_WfPppLineState_Object = MibTableColumn
wfPppLineState = _WfPppLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 3),
    _WfPppLineState_Type()
)
wfPppLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineState.setStatus("mandatory")
_WfPppLineLineNumber_Type = Integer32
_WfPppLineLineNumber_Object = MibTableColumn
wfPppLineLineNumber = _WfPppLineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 4),
    _WfPppLineLineNumber_Type()
)
wfPppLineLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLineNumber.setStatus("mandatory")
_WfPppLineLLIndex_Type = Integer32
_WfPppLineLLIndex_Object = MibTableColumn
wfPppLineLLIndex = _WfPppLineLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 5),
    _WfPppLineLLIndex_Type()
)
wfPppLineLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLLIndex.setStatus("mandatory")


class _WfPppLineLcpCurrentState_Type(Integer32):
    """Custom type wfPppLineLcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppLineLcpCurrentState_Type.__name__ = "Integer32"
_WfPppLineLcpCurrentState_Object = MibTableColumn
wfPppLineLcpCurrentState = _WfPppLineLcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 6),
    _WfPppLineLcpCurrentState_Type()
)
wfPppLineLcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLcpCurrentState.setStatus("mandatory")


class _WfPppLineRestartTimer_Type(Integer32):
    """Custom type wfPppLineRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfPppLineRestartTimer_Type.__name__ = "Integer32"
_WfPppLineRestartTimer_Object = MibTableColumn
wfPppLineRestartTimer = _WfPppLineRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 7),
    _WfPppLineRestartTimer_Type()
)
wfPppLineRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineRestartTimer.setStatus("mandatory")
_WfPppLineEchoRequestFreq_Type = Integer32
_WfPppLineEchoRequestFreq_Object = MibTableColumn
wfPppLineEchoRequestFreq = _WfPppLineEchoRequestFreq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 8),
    _WfPppLineEchoRequestFreq_Type()
)
wfPppLineEchoRequestFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineEchoRequestFreq.setStatus("mandatory")


class _WfPppLineEchoReplyLoss_Type(Integer32):
    """Custom type wfPppLineEchoReplyLoss based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfPppLineEchoReplyLoss_Type.__name__ = "Integer32"
_WfPppLineEchoReplyLoss_Object = MibTableColumn
wfPppLineEchoReplyLoss = _WfPppLineEchoReplyLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 9),
    _WfPppLineEchoReplyLoss_Type()
)
wfPppLineEchoReplyLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineEchoReplyLoss.setStatus("mandatory")


class _WfPppLineMaxConfReq_Type(Integer32):
    """Custom type wfPppLineMaxConfReq based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WfPppLineMaxConfReq_Type.__name__ = "Integer32"
_WfPppLineMaxConfReq_Object = MibTableColumn
wfPppLineMaxConfReq = _WfPppLineMaxConfReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 10),
    _WfPppLineMaxConfReq_Type()
)
wfPppLineMaxConfReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineMaxConfReq.setStatus("mandatory")


class _WfPppLineMaxTermReq_Type(Integer32):
    """Custom type wfPppLineMaxTermReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfPppLineMaxTermReq_Type.__name__ = "Integer32"
_WfPppLineMaxTermReq_Object = MibTableColumn
wfPppLineMaxTermReq = _WfPppLineMaxTermReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 11),
    _WfPppLineMaxTermReq_Type()
)
wfPppLineMaxTermReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineMaxTermReq.setStatus("mandatory")


class _WfPppLineMaxConfFail_Type(Integer32):
    """Custom type wfPppLineMaxConfFail based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfPppLineMaxConfFail_Type.__name__ = "Integer32"
_WfPppLineMaxConfFail_Object = MibTableColumn
wfPppLineMaxConfFail = _WfPppLineMaxConfFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 12),
    _WfPppLineMaxConfFail_Type()
)
wfPppLineMaxConfFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineMaxConfFail.setStatus("mandatory")
_WfPppLineMagicNumber_Type = Counter32
_WfPppLineMagicNumber_Object = MibTableColumn
wfPppLineMagicNumber = _WfPppLineMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 13),
    _WfPppLineMagicNumber_Type()
)
wfPppLineMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineMagicNumber.setStatus("mandatory")
_WfPppLineMru_Type = Integer32
_WfPppLineMru_Object = MibTableColumn
wfPppLineMru = _WfPppLineMru_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 14),
    _WfPppLineMru_Type()
)
wfPppLineMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineMru.setStatus("mandatory")


class _WfPppLineLocalAuthProtocol_Type(Integer32):
    """Custom type wfPppLineLocalAuthProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              49187,
              49699)
        )
    )
    namedValues = NamedValues(
        *(("chap", 49699),
          ("none", 1),
          ("passauth", 49187))
    )


_WfPppLineLocalAuthProtocol_Type.__name__ = "Integer32"
_WfPppLineLocalAuthProtocol_Object = MibTableColumn
wfPppLineLocalAuthProtocol = _WfPppLineLocalAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 15),
    _WfPppLineLocalAuthProtocol_Type()
)
wfPppLineLocalAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineLocalAuthProtocol.setStatus("mandatory")


class _WfPppLineRemoteAuthProtocol_Type(Integer32):
    """Custom type wfPppLineRemoteAuthProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              49187)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("passauth", 49187))
    )


_WfPppLineRemoteAuthProtocol_Type.__name__ = "Integer32"
_WfPppLineRemoteAuthProtocol_Object = MibTableColumn
wfPppLineRemoteAuthProtocol = _WfPppLineRemoteAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 16),
    _WfPppLineRemoteAuthProtocol_Type()
)
wfPppLineRemoteAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineRemoteAuthProtocol.setStatus("mandatory")
_WfPppLineLocalPapId_Type = DisplayString
_WfPppLineLocalPapId_Object = MibTableColumn
wfPppLineLocalPapId = _WfPppLineLocalPapId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 17),
    _WfPppLineLocalPapId_Type()
)
wfPppLineLocalPapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineLocalPapId.setStatus("mandatory")
_WfPppLineLocalPapPassword_Type = DisplayString
_WfPppLineLocalPapPassword_Object = MibTableColumn
wfPppLineLocalPapPassword = _WfPppLineLocalPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 18),
    _WfPppLineLocalPapPassword_Type()
)
wfPppLineLocalPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineLocalPapPassword.setStatus("mandatory")
_WfPppLineRemotePapId_Type = DisplayString
_WfPppLineRemotePapId_Object = MibTableColumn
wfPppLineRemotePapId = _WfPppLineRemotePapId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 19),
    _WfPppLineRemotePapId_Type()
)
wfPppLineRemotePapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineRemotePapId.setStatus("mandatory")
_WfPppLineRemotePapPassword_Type = DisplayString
_WfPppLineRemotePapPassword_Object = MibTableColumn
wfPppLineRemotePapPassword = _WfPppLineRemotePapPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 20),
    _WfPppLineRemotePapPassword_Type()
)
wfPppLineRemotePapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineRemotePapPassword.setStatus("mandatory")


class _WfPppLineLQProtocol_Type(Integer32):
    """Custom type wfPppLineLQProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              49189)
        )
    )
    namedValues = NamedValues(
        *(("linkqr", 49189),
          ("none", 1))
    )


_WfPppLineLQProtocol_Type.__name__ = "Integer32"
_WfPppLineLQProtocol_Object = MibTableColumn
wfPppLineLQProtocol = _WfPppLineLQProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 21),
    _WfPppLineLQProtocol_Type()
)
wfPppLineLQProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineLQProtocol.setStatus("mandatory")


class _WfPppLineDisableRemoteLQRTimer_Type(Integer32):
    """Custom type wfPppLineDisableRemoteLQRTimer based on Integer32"""
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


_WfPppLineDisableRemoteLQRTimer_Type.__name__ = "Integer32"
_WfPppLineDisableRemoteLQRTimer_Object = MibTableColumn
wfPppLineDisableRemoteLQRTimer = _WfPppLineDisableRemoteLQRTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 22),
    _WfPppLineDisableRemoteLQRTimer_Type()
)
wfPppLineDisableRemoteLQRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineDisableRemoteLQRTimer.setStatus("mandatory")


class _WfPppLineCfgLQRRptPrd_Type(Integer32):
    """Custom type wfPppLineCfgLQRRptPrd based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfPppLineCfgLQRRptPrd_Type.__name__ = "Integer32"
_WfPppLineCfgLQRRptPrd_Object = MibTableColumn
wfPppLineCfgLQRRptPrd = _WfPppLineCfgLQRRptPrd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 23),
    _WfPppLineCfgLQRRptPrd_Type()
)
wfPppLineCfgLQRRptPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineCfgLQRRptPrd.setStatus("mandatory")
_WfPppLineLQRRptPrd_Type = Integer32
_WfPppLineLQRRptPrd_Object = MibTableColumn
wfPppLineLQRRptPrd = _WfPppLineLQRRptPrd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 24),
    _WfPppLineLQRRptPrd_Type()
)
wfPppLineLQRRptPrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLQRRptPrd.setStatus("mandatory")


class _WfPppLineCfgInboundQuality_Type(Integer32):
    """Custom type wfPppLineCfgInboundQuality based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfPppLineCfgInboundQuality_Type.__name__ = "Integer32"
_WfPppLineCfgInboundQuality_Object = MibTableColumn
wfPppLineCfgInboundQuality = _WfPppLineCfgInboundQuality_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 25),
    _WfPppLineCfgInboundQuality_Type()
)
wfPppLineCfgInboundQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineCfgInboundQuality.setStatus("mandatory")
_WfPppLineInboundQuality_Type = Integer32
_WfPppLineInboundQuality_Object = MibTableColumn
wfPppLineInboundQuality = _WfPppLineInboundQuality_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 26),
    _WfPppLineInboundQuality_Type()
)
wfPppLineInboundQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineInboundQuality.setStatus("mandatory")


class _WfPppLineCfgOutboundQuality_Type(Integer32):
    """Custom type wfPppLineCfgOutboundQuality based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfPppLineCfgOutboundQuality_Type.__name__ = "Integer32"
_WfPppLineCfgOutboundQuality_Object = MibTableColumn
wfPppLineCfgOutboundQuality = _WfPppLineCfgOutboundQuality_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 27),
    _WfPppLineCfgOutboundQuality_Type()
)
wfPppLineCfgOutboundQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineCfgOutboundQuality.setStatus("mandatory")
_WfPppLineOutboundQuality_Type = Integer32
_WfPppLineOutboundQuality_Object = MibTableColumn
wfPppLineOutboundQuality = _WfPppLineOutboundQuality_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 28),
    _WfPppLineOutboundQuality_Type()
)
wfPppLineOutboundQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineOutboundQuality.setStatus("mandatory")
_WfPppLineOutLQRs_Type = Counter32
_WfPppLineOutLQRs_Object = MibTableColumn
wfPppLineOutLQRs = _WfPppLineOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 29),
    _WfPppLineOutLQRs_Type()
)
wfPppLineOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineOutLQRs.setStatus("mandatory")
_WfPppLineInLQRs_Type = Counter32
_WfPppLineInLQRs_Object = MibTableColumn
wfPppLineInLQRs = _WfPppLineInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 30),
    _WfPppLineInLQRs_Type()
)
wfPppLineInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineInLQRs.setStatus("mandatory")
_WfPppLineChapSecret_Type = DisplayString
_WfPppLineChapSecret_Object = MibTableColumn
wfPppLineChapSecret = _WfPppLineChapSecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 31),
    _WfPppLineChapSecret_Type()
)
wfPppLineChapSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineChapSecret.setStatus("mandatory")


class _WfPppLinePapFallbackDisable_Type(Integer32):
    """Custom type wfPppLinePapFallbackDisable based on Integer32"""
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


_WfPppLinePapFallbackDisable_Type.__name__ = "Integer32"
_WfPppLinePapFallbackDisable_Object = MibTableColumn
wfPppLinePapFallbackDisable = _WfPppLinePapFallbackDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 32),
    _WfPppLinePapFallbackDisable_Type()
)
wfPppLinePapFallbackDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLinePapFallbackDisable.setStatus("mandatory")
_WfPppLineChapLocalName_Type = DisplayString
_WfPppLineChapLocalName_Object = MibTableColumn
wfPppLineChapLocalName = _WfPppLineChapLocalName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 33),
    _WfPppLineChapLocalName_Type()
)
wfPppLineChapLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineChapLocalName.setStatus("mandatory")
_WfPppLineChapRemoteName_Type = DisplayString
_WfPppLineChapRemoteName_Object = MibTableColumn
wfPppLineChapRemoteName = _WfPppLineChapRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 34),
    _WfPppLineChapRemoteName_Type()
)
wfPppLineChapRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineChapRemoteName.setStatus("mandatory")
_WfPppLineChapPeriodicTimer_Type = Integer32
_WfPppLineChapPeriodicTimer_Object = MibTableColumn
wfPppLineChapPeriodicTimer = _WfPppLineChapPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 35),
    _WfPppLineChapPeriodicTimer_Type()
)
wfPppLineChapPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineChapPeriodicTimer.setStatus("mandatory")
_WfPppLineBadPackets_Type = Counter32
_WfPppLineBadPackets_Object = MibTableColumn
wfPppLineBadPackets = _WfPppLineBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 36),
    _WfPppLineBadPackets_Type()
)
wfPppLineBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineBadPackets.setStatus("mandatory")
_WfPppLineLastBadPacket_Type = OctetString
_WfPppLineLastBadPacket_Object = MibTableColumn
wfPppLineLastBadPacket = _WfPppLineLastBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 37),
    _WfPppLineLastBadPacket_Type()
)
wfPppLineLastBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLastBadPacket.setStatus("mandatory")
_WfPppLineLevelPktsIn_Type = Counter32
_WfPppLineLevelPktsIn_Object = MibTableColumn
wfPppLineLevelPktsIn = _WfPppLineLevelPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 38),
    _WfPppLineLevelPktsIn_Type()
)
wfPppLineLevelPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLevelPktsIn.setStatus("mandatory")


class _WfPppLineAllowPapReject_Type(Integer32):
    """Custom type wfPppLineAllowPapReject based on Integer32"""
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


_WfPppLineAllowPapReject_Type.__name__ = "Integer32"
_WfPppLineAllowPapReject_Object = MibTableColumn
wfPppLineAllowPapReject = _WfPppLineAllowPapReject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 39),
    _WfPppLineAllowPapReject_Type()
)
wfPppLineAllowPapReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineAllowPapReject.setStatus("mandatory")


class _WfPppLineActiveCct_Type(Integer32):
    """Custom type wfPppLineActiveCct based on Integer32"""
    defaultValue = 65535


_WfPppLineActiveCct_Object = MibTableColumn
wfPppLineActiveCct = _WfPppLineActiveCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 40),
    _WfPppLineActiveCct_Type()
)
wfPppLineActiveCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineActiveCct.setStatus("mandatory")


class _WfPppLineCfgAsyncMap_Type(Gauge32):
    """Custom type wfPppLineCfgAsyncMap based on Gauge32"""
    defaultValue = 655360


_WfPppLineCfgAsyncMap_Object = MibTableColumn
wfPppLineCfgAsyncMap = _WfPppLineCfgAsyncMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 41),
    _WfPppLineCfgAsyncMap_Type()
)
wfPppLineCfgAsyncMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineCfgAsyncMap.setStatus("mandatory")
_WfPppLineActualAsyncMap_Type = Gauge32
_WfPppLineActualAsyncMap_Object = MibTableColumn
wfPppLineActualAsyncMap = _WfPppLineActualAsyncMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 42),
    _WfPppLineActualAsyncMap_Type()
)
wfPppLineActualAsyncMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineActualAsyncMap.setStatus("mandatory")


class _WfPppLineAuthTimer_Type(Integer32):
    """Custom type wfPppLineAuthTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfPppLineAuthTimer_Type.__name__ = "Integer32"
_WfPppLineAuthTimer_Object = MibTableColumn
wfPppLineAuthTimer = _WfPppLineAuthTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 43),
    _WfPppLineAuthTimer_Type()
)
wfPppLineAuthTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineAuthTimer.setStatus("mandatory")


class _WfPppLineConvergenceTimer_Type(Integer32):
    """Custom type wfPppLineConvergenceTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_WfPppLineConvergenceTimer_Type.__name__ = "Integer32"
_WfPppLineConvergenceTimer_Object = MibTableColumn
wfPppLineConvergenceTimer = _WfPppLineConvergenceTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 44),
    _WfPppLineConvergenceTimer_Type()
)
wfPppLineConvergenceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineConvergenceTimer.setStatus("mandatory")


class _WfPppLineMagicNumDisable_Type(Integer32):
    """Custom type wfPppLineMagicNumDisable based on Integer32"""
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


_WfPppLineMagicNumDisable_Type.__name__ = "Integer32"
_WfPppLineMagicNumDisable_Object = MibTableColumn
wfPppLineMagicNumDisable = _WfPppLineMagicNumDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 45),
    _WfPppLineMagicNumDisable_Type()
)
wfPppLineMagicNumDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineMagicNumDisable.setStatus("mandatory")


class _WfPppLineMyLinkDiscr_Type(Integer32):
    """Custom type wfPppLineMyLinkDiscr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfPppLineMyLinkDiscr_Type.__name__ = "Integer32"
_WfPppLineMyLinkDiscr_Object = MibTableColumn
wfPppLineMyLinkDiscr = _WfPppLineMyLinkDiscr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 46),
    _WfPppLineMyLinkDiscr_Type()
)
wfPppLineMyLinkDiscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineMyLinkDiscr.setStatus("mandatory")


class _WfPppLinePeerLinkDiscr_Type(Integer32):
    """Custom type wfPppLinePeerLinkDiscr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfPppLinePeerLinkDiscr_Type.__name__ = "Integer32"
_WfPppLinePeerLinkDiscr_Object = MibTableColumn
wfPppLinePeerLinkDiscr = _WfPppLinePeerLinkDiscr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 47),
    _WfPppLinePeerLinkDiscr_Type()
)
wfPppLinePeerLinkDiscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLinePeerLinkDiscr.setStatus("mandatory")


class _WfPppLineCfgMru_Type(Integer32):
    """Custom type wfPppLineCfgMru based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4600),
    )


_WfPppLineCfgMru_Type.__name__ = "Integer32"
_WfPppLineCfgMru_Object = MibTableColumn
wfPppLineCfgMru = _WfPppLineCfgMru_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 48),
    _WfPppLineCfgMru_Type()
)
wfPppLineCfgMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineCfgMru.setStatus("mandatory")


class _WfPppLineRfc1661Compliance_Type(Integer32):
    """Custom type wfPppLineRfc1661Compliance based on Integer32"""
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


_WfPppLineRfc1661Compliance_Type.__name__ = "Integer32"
_WfPppLineRfc1661Compliance_Object = MibTableColumn
wfPppLineRfc1661Compliance = _WfPppLineRfc1661Compliance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 49),
    _WfPppLineRfc1661Compliance_Type()
)
wfPppLineRfc1661Compliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppLineRfc1661Compliance.setStatus("mandatory")


class _WfPppLineLqmCurrentState_Type(Integer32):
    """Custom type wfPppLineLqmCurrentState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfPppLineLqmCurrentState_Type.__name__ = "Integer32"
_WfPppLineLqmCurrentState_Object = MibTableColumn
wfPppLineLqmCurrentState = _WfPppLineLqmCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 1, 1, 50),
    _WfPppLineLqmCurrentState_Type()
)
wfPppLineLqmCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppLineLqmCurrentState.setStatus("mandatory")
_WfPppCircuitTable_Object = MibTable
wfPppCircuitTable = _WfPppCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2)
)
if mibBuilder.loadTexts:
    wfPppCircuitTable.setStatus("mandatory")
_WfPppCircuitEntry_Object = MibTableRow
wfPppCircuitEntry = _WfPppCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1)
)
wfPppCircuitEntry.setIndexNames(
    (0, "Wellfleet-PPP-MIB", "wfPppCircuitID"),
)
if mibBuilder.loadTexts:
    wfPppCircuitEntry.setStatus("mandatory")


class _WfPppCircuitDelete_Type(Integer32):
    """Custom type wfPppCircuitDelete based on Integer32"""
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


_WfPppCircuitDelete_Type.__name__ = "Integer32"
_WfPppCircuitDelete_Object = MibTableColumn
wfPppCircuitDelete = _WfPppCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 1),
    _WfPppCircuitDelete_Type()
)
wfPppCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitDelete.setStatus("mandatory")


class _WfPppCircuitState_Type(Integer32):
    """Custom type wfPppCircuitState based on Integer32"""
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


_WfPppCircuitState_Type.__name__ = "Integer32"
_WfPppCircuitState_Object = MibTableColumn
wfPppCircuitState = _WfPppCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 2),
    _WfPppCircuitState_Type()
)
wfPppCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitState.setStatus("mandatory")


class _WfPppCircuitIpcpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitIpcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitIpcpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitIpcpCurrentState_Object = MibTableColumn
wfPppCircuitIpcpCurrentState = _WfPppCircuitIpcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 3),
    _WfPppCircuitIpcpCurrentState_Type()
)
wfPppCircuitIpcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpcpCurrentState.setStatus("mandatory")


class _WfPppCircuitOsinlcpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitOsinlcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitOsinlcpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitOsinlcpCurrentState_Object = MibTableColumn
wfPppCircuitOsinlcpCurrentState = _WfPppCircuitOsinlcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 4),
    _WfPppCircuitOsinlcpCurrentState_Type()
)
wfPppCircuitOsinlcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitOsinlcpCurrentState.setStatus("mandatory")


class _WfPppCircuitXnscpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitXnscpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitXnscpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitXnscpCurrentState_Object = MibTableColumn
wfPppCircuitXnscpCurrentState = _WfPppCircuitXnscpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 5),
    _WfPppCircuitXnscpCurrentState_Type()
)
wfPppCircuitXnscpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitXnscpCurrentState.setStatus("mandatory")


class _WfPppCircuitDncpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitDncpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitDncpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitDncpCurrentState_Object = MibTableColumn
wfPppCircuitDncpCurrentState = _WfPppCircuitDncpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 6),
    _WfPppCircuitDncpCurrentState_Type()
)
wfPppCircuitDncpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitDncpCurrentState.setStatus("mandatory")


class _WfPppCircuitAtcpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitAtcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitAtcpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitAtcpCurrentState_Object = MibTableColumn
wfPppCircuitAtcpCurrentState = _WfPppCircuitAtcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 7),
    _WfPppCircuitAtcpCurrentState_Type()
)
wfPppCircuitAtcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitAtcpCurrentState.setStatus("mandatory")


class _WfPppCircuitIpxcpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitIpxcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitIpxcpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitIpxcpCurrentState_Object = MibTableColumn
wfPppCircuitIpxcpCurrentState = _WfPppCircuitIpxcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 8),
    _WfPppCircuitIpxcpCurrentState_Type()
)
wfPppCircuitIpxcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpxcpCurrentState.setStatus("mandatory")


class _WfPppCircuitBncpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitBncpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitBncpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitBncpCurrentState_Object = MibTableColumn
wfPppCircuitBncpCurrentState = _WfPppCircuitBncpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 9),
    _WfPppCircuitBncpCurrentState_Type()
)
wfPppCircuitBncpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBncpCurrentState.setStatus("mandatory")


class _WfPppCircuitVncpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitVncpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitVncpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitVncpCurrentState_Object = MibTableColumn
wfPppCircuitVncpCurrentState = _WfPppCircuitVncpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 10),
    _WfPppCircuitVncpCurrentState_Type()
)
wfPppCircuitVncpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitVncpCurrentState.setStatus("mandatory")


class _WfPppCircuitID_Type(Integer32):
    """Custom type wfPppCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfPppCircuitID_Type.__name__ = "Integer32"
_WfPppCircuitID_Object = MibTableColumn
wfPppCircuitID = _WfPppCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 11),
    _WfPppCircuitID_Type()
)
wfPppCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitID.setStatus("mandatory")


class _WfPppCircuitIpDisable_Type(Integer32):
    """Custom type wfPppCircuitIpDisable based on Integer32"""
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


_WfPppCircuitIpDisable_Type.__name__ = "Integer32"
_WfPppCircuitIpDisable_Object = MibTableColumn
wfPppCircuitIpDisable = _WfPppCircuitIpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 12),
    _WfPppCircuitIpDisable_Type()
)
wfPppCircuitIpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitIpDisable.setStatus("mandatory")


class _WfPppCircuitOsinlDisable_Type(Integer32):
    """Custom type wfPppCircuitOsinlDisable based on Integer32"""
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


_WfPppCircuitOsinlDisable_Type.__name__ = "Integer32"
_WfPppCircuitOsinlDisable_Object = MibTableColumn
wfPppCircuitOsinlDisable = _WfPppCircuitOsinlDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 13),
    _WfPppCircuitOsinlDisable_Type()
)
wfPppCircuitOsinlDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitOsinlDisable.setStatus("mandatory")


class _WfPppCircuitXnsDisable_Type(Integer32):
    """Custom type wfPppCircuitXnsDisable based on Integer32"""
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


_WfPppCircuitXnsDisable_Type.__name__ = "Integer32"
_WfPppCircuitXnsDisable_Object = MibTableColumn
wfPppCircuitXnsDisable = _WfPppCircuitXnsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 14),
    _WfPppCircuitXnsDisable_Type()
)
wfPppCircuitXnsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitXnsDisable.setStatus("mandatory")


class _WfPppCircuitDecnetDisable_Type(Integer32):
    """Custom type wfPppCircuitDecnetDisable based on Integer32"""
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


_WfPppCircuitDecnetDisable_Type.__name__ = "Integer32"
_WfPppCircuitDecnetDisable_Object = MibTableColumn
wfPppCircuitDecnetDisable = _WfPppCircuitDecnetDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 15),
    _WfPppCircuitDecnetDisable_Type()
)
wfPppCircuitDecnetDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitDecnetDisable.setStatus("mandatory")


class _WfPppCircuitAppletalkDisable_Type(Integer32):
    """Custom type wfPppCircuitAppletalkDisable based on Integer32"""
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


_WfPppCircuitAppletalkDisable_Type.__name__ = "Integer32"
_WfPppCircuitAppletalkDisable_Object = MibTableColumn
wfPppCircuitAppletalkDisable = _WfPppCircuitAppletalkDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 16),
    _WfPppCircuitAppletalkDisable_Type()
)
wfPppCircuitAppletalkDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitAppletalkDisable.setStatus("mandatory")


class _WfPppCircuitIpxDisable_Type(Integer32):
    """Custom type wfPppCircuitIpxDisable based on Integer32"""
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


_WfPppCircuitIpxDisable_Type.__name__ = "Integer32"
_WfPppCircuitIpxDisable_Object = MibTableColumn
wfPppCircuitIpxDisable = _WfPppCircuitIpxDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 17),
    _WfPppCircuitIpxDisable_Type()
)
wfPppCircuitIpxDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitIpxDisable.setStatus("mandatory")


class _WfPppCircuitBridgeDisable_Type(Integer32):
    """Custom type wfPppCircuitBridgeDisable based on Integer32"""
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


_WfPppCircuitBridgeDisable_Type.__name__ = "Integer32"
_WfPppCircuitBridgeDisable_Object = MibTableColumn
wfPppCircuitBridgeDisable = _WfPppCircuitBridgeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 18),
    _WfPppCircuitBridgeDisable_Type()
)
wfPppCircuitBridgeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitBridgeDisable.setStatus("mandatory")


class _WfPppCircuitVinesDisable_Type(Integer32):
    """Custom type wfPppCircuitVinesDisable based on Integer32"""
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


_WfPppCircuitVinesDisable_Type.__name__ = "Integer32"
_WfPppCircuitVinesDisable_Object = MibTableColumn
wfPppCircuitVinesDisable = _WfPppCircuitVinesDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 19),
    _WfPppCircuitVinesDisable_Type()
)
wfPppCircuitVinesDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitVinesDisable.setStatus("mandatory")
_WfPppCircuitCfgLocalIpAddr_Type = IpAddress
_WfPppCircuitCfgLocalIpAddr_Object = MibTableColumn
wfPppCircuitCfgLocalIpAddr = _WfPppCircuitCfgLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 20),
    _WfPppCircuitCfgLocalIpAddr_Type()
)
wfPppCircuitCfgLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgLocalIpAddr.setStatus("mandatory")
_WfPppCircuitLocalIpAddr_Type = IpAddress
_WfPppCircuitLocalIpAddr_Object = MibTableColumn
wfPppCircuitLocalIpAddr = _WfPppCircuitLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 21),
    _WfPppCircuitLocalIpAddr_Type()
)
wfPppCircuitLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitLocalIpAddr.setStatus("mandatory")
_WfPppCircuitCfgRemoteIpAddr_Type = IpAddress
_WfPppCircuitCfgRemoteIpAddr_Object = MibTableColumn
wfPppCircuitCfgRemoteIpAddr = _WfPppCircuitCfgRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 22),
    _WfPppCircuitCfgRemoteIpAddr_Type()
)
wfPppCircuitCfgRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgRemoteIpAddr.setStatus("mandatory")
_WfPppCircuitRemoteIpAddr_Type = IpAddress
_WfPppCircuitRemoteIpAddr_Object = MibTableColumn
wfPppCircuitRemoteIpAddr = _WfPppCircuitRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 23),
    _WfPppCircuitRemoteIpAddr_Type()
)
wfPppCircuitRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitRemoteIpAddr.setStatus("mandatory")
_WfPppCircuitCfgIpxNetworkNumber_Type = OctetString
_WfPppCircuitCfgIpxNetworkNumber_Object = MibTableColumn
wfPppCircuitCfgIpxNetworkNumber = _WfPppCircuitCfgIpxNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 24),
    _WfPppCircuitCfgIpxNetworkNumber_Type()
)
wfPppCircuitCfgIpxNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgIpxNetworkNumber.setStatus("mandatory")
_WfPppCircuitIpxNetworkNumber_Type = OctetString
_WfPppCircuitIpxNetworkNumber_Object = MibTableColumn
wfPppCircuitIpxNetworkNumber = _WfPppCircuitIpxNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 25),
    _WfPppCircuitIpxNetworkNumber_Type()
)
wfPppCircuitIpxNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpxNetworkNumber.setStatus("mandatory")
_WfPppCircuitIpxRemoteNodeNumber_Type = OctetString
_WfPppCircuitIpxRemoteNodeNumber_Object = MibTableColumn
wfPppCircuitIpxRemoteNodeNumber = _WfPppCircuitIpxRemoteNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 26),
    _WfPppCircuitIpxRemoteNodeNumber_Type()
)
wfPppCircuitIpxRemoteNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitIpxRemoteNodeNumber.setStatus("mandatory")


class _WfPppCircuitCfgIpxRoutingProtocol_Type(Integer32):
    """Custom type wfPppCircuitCfgIpxRoutingProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ripsap", 2)
    )


_WfPppCircuitCfgIpxRoutingProtocol_Type.__name__ = "Integer32"
_WfPppCircuitCfgIpxRoutingProtocol_Object = MibTableColumn
wfPppCircuitCfgIpxRoutingProtocol = _WfPppCircuitCfgIpxRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 27),
    _WfPppCircuitCfgIpxRoutingProtocol_Type()
)
wfPppCircuitCfgIpxRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgIpxRoutingProtocol.setStatus("mandatory")
_WfPppCircuitIpxRoutingProtocol_Type = Integer32
_WfPppCircuitIpxRoutingProtocol_Object = MibTableColumn
wfPppCircuitIpxRoutingProtocol = _WfPppCircuitIpxRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 28),
    _WfPppCircuitIpxRoutingProtocol_Type()
)
wfPppCircuitIpxRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpxRoutingProtocol.setStatus("mandatory")
_WfPppCircuitLocalIpxRouterName_Type = DisplayString
_WfPppCircuitLocalIpxRouterName_Object = MibTableColumn
wfPppCircuitLocalIpxRouterName = _WfPppCircuitLocalIpxRouterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 29),
    _WfPppCircuitLocalIpxRouterName_Type()
)
wfPppCircuitLocalIpxRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitLocalIpxRouterName.setStatus("mandatory")
_WfPppCircuitRemoteIpxRouterName_Type = DisplayString
_WfPppCircuitRemoteIpxRouterName_Object = MibTableColumn
wfPppCircuitRemoteIpxRouterName = _WfPppCircuitRemoteIpxRouterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 30),
    _WfPppCircuitRemoteIpxRouterName_Type()
)
wfPppCircuitRemoteIpxRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitRemoteIpxRouterName.setStatus("mandatory")


class _WfPppCircuitIpxConfigComplete_Type(Integer32):
    """Custom type wfPppCircuitIpxConfigComplete based on Integer32"""
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


_WfPppCircuitIpxConfigComplete_Type.__name__ = "Integer32"
_WfPppCircuitIpxConfigComplete_Object = MibTableColumn
wfPppCircuitIpxConfigComplete = _WfPppCircuitIpxConfigComplete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 31),
    _WfPppCircuitIpxConfigComplete_Type()
)
wfPppCircuitIpxConfigComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpxConfigComplete.setStatus("mandatory")
_WfPppCircuitCfgAtNetwork_Type = Integer32
_WfPppCircuitCfgAtNetwork_Object = MibTableColumn
wfPppCircuitCfgAtNetwork = _WfPppCircuitCfgAtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 32),
    _WfPppCircuitCfgAtNetwork_Type()
)
wfPppCircuitCfgAtNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgAtNetwork.setStatus("mandatory")
_WfPppCircuitAtNetwork_Type = Integer32
_WfPppCircuitAtNetwork_Object = MibTableColumn
wfPppCircuitAtNetwork = _WfPppCircuitAtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 33),
    _WfPppCircuitAtNetwork_Type()
)
wfPppCircuitAtNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitAtNetwork.setStatus("mandatory")
_WfPppCircuitCfgLocalAtNode_Type = Integer32
_WfPppCircuitCfgLocalAtNode_Object = MibTableColumn
wfPppCircuitCfgLocalAtNode = _WfPppCircuitCfgLocalAtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 34),
    _WfPppCircuitCfgLocalAtNode_Type()
)
wfPppCircuitCfgLocalAtNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgLocalAtNode.setStatus("mandatory")
_WfPppCircuitLocalAtNode_Type = Integer32
_WfPppCircuitLocalAtNode_Object = MibTableColumn
wfPppCircuitLocalAtNode = _WfPppCircuitLocalAtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 35),
    _WfPppCircuitLocalAtNode_Type()
)
wfPppCircuitLocalAtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitLocalAtNode.setStatus("mandatory")
_WfPppCircuitCfgRemoteAtNode_Type = Integer32
_WfPppCircuitCfgRemoteAtNode_Object = MibTableColumn
wfPppCircuitCfgRemoteAtNode = _WfPppCircuitCfgRemoteAtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 36),
    _WfPppCircuitCfgRemoteAtNode_Type()
)
wfPppCircuitCfgRemoteAtNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgRemoteAtNode.setStatus("mandatory")
_WfPppCircuitRemoteAtNode_Type = Integer32
_WfPppCircuitRemoteAtNode_Object = MibTableColumn
wfPppCircuitRemoteAtNode = _WfPppCircuitRemoteAtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 37),
    _WfPppCircuitRemoteAtNode_Type()
)
wfPppCircuitRemoteAtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitRemoteAtNode.setStatus("mandatory")


class _WfPppCircuitCfgAtRoutingProtocol_Type(Integer32):
    """Custom type wfPppCircuitCfgAtRoutingProtocol based on Integer32"""
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
        *(("abgp", 3),
          ("aurp", 2),
          ("rtmp", 1))
    )


_WfPppCircuitCfgAtRoutingProtocol_Type.__name__ = "Integer32"
_WfPppCircuitCfgAtRoutingProtocol_Object = MibTableColumn
wfPppCircuitCfgAtRoutingProtocol = _WfPppCircuitCfgAtRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 38),
    _WfPppCircuitCfgAtRoutingProtocol_Type()
)
wfPppCircuitCfgAtRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgAtRoutingProtocol.setStatus("mandatory")
_WfPppCircuitAtRoutingProtocol_Type = Integer32
_WfPppCircuitAtRoutingProtocol_Object = MibTableColumn
wfPppCircuitAtRoutingProtocol = _WfPppCircuitAtRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 39),
    _WfPppCircuitAtRoutingProtocol_Type()
)
wfPppCircuitAtRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitAtRoutingProtocol.setStatus("mandatory")


class _WfPppCircuitCfgBridgeEnet_Type(Integer32):
    """Custom type wfPppCircuitCfgBridgeEnet based on Integer32"""
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


_WfPppCircuitCfgBridgeEnet_Type.__name__ = "Integer32"
_WfPppCircuitCfgBridgeEnet_Object = MibTableColumn
wfPppCircuitCfgBridgeEnet = _WfPppCircuitCfgBridgeEnet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 40),
    _WfPppCircuitCfgBridgeEnet_Type()
)
wfPppCircuitCfgBridgeEnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgBridgeEnet.setStatus("mandatory")


class _WfPppCircuitBridgeEnet_Type(Integer32):
    """Custom type wfPppCircuitBridgeEnet based on Integer32"""
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


_WfPppCircuitBridgeEnet_Type.__name__ = "Integer32"
_WfPppCircuitBridgeEnet_Object = MibTableColumn
wfPppCircuitBridgeEnet = _WfPppCircuitBridgeEnet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 41),
    _WfPppCircuitBridgeEnet_Type()
)
wfPppCircuitBridgeEnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBridgeEnet.setStatus("mandatory")


class _WfPppCircuitCfgBridgeFddi_Type(Integer32):
    """Custom type wfPppCircuitCfgBridgeFddi based on Integer32"""
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


_WfPppCircuitCfgBridgeFddi_Type.__name__ = "Integer32"
_WfPppCircuitCfgBridgeFddi_Object = MibTableColumn
wfPppCircuitCfgBridgeFddi = _WfPppCircuitCfgBridgeFddi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 42),
    _WfPppCircuitCfgBridgeFddi_Type()
)
wfPppCircuitCfgBridgeFddi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgBridgeFddi.setStatus("mandatory")


class _WfPppCircuitBridgeFddi_Type(Integer32):
    """Custom type wfPppCircuitBridgeFddi based on Integer32"""
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


_WfPppCircuitBridgeFddi_Type.__name__ = "Integer32"
_WfPppCircuitBridgeFddi_Object = MibTableColumn
wfPppCircuitBridgeFddi = _WfPppCircuitBridgeFddi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 43),
    _WfPppCircuitBridgeFddi_Type()
)
wfPppCircuitBridgeFddi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBridgeFddi.setStatus("mandatory")


class _WfPppCircuitCfgBridgeTokenRing_Type(Integer32):
    """Custom type wfPppCircuitCfgBridgeTokenRing based on Integer32"""
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


_WfPppCircuitCfgBridgeTokenRing_Type.__name__ = "Integer32"
_WfPppCircuitCfgBridgeTokenRing_Object = MibTableColumn
wfPppCircuitCfgBridgeTokenRing = _WfPppCircuitCfgBridgeTokenRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 44),
    _WfPppCircuitCfgBridgeTokenRing_Type()
)
wfPppCircuitCfgBridgeTokenRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgBridgeTokenRing.setStatus("mandatory")


class _WfPppCircuitBridgeTokenRing_Type(Integer32):
    """Custom type wfPppCircuitBridgeTokenRing based on Integer32"""
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


_WfPppCircuitBridgeTokenRing_Type.__name__ = "Integer32"
_WfPppCircuitBridgeTokenRing_Object = MibTableColumn
wfPppCircuitBridgeTokenRing = _WfPppCircuitBridgeTokenRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 45),
    _WfPppCircuitBridgeTokenRing_Type()
)
wfPppCircuitBridgeTokenRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBridgeTokenRing.setStatus("mandatory")
_WfPppCircuitBadPackets_Type = Counter32
_WfPppCircuitBadPackets_Object = MibTableColumn
wfPppCircuitBadPackets = _WfPppCircuitBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 46),
    _WfPppCircuitBadPackets_Type()
)
wfPppCircuitBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBadPackets.setStatus("mandatory")
_WfPppCircuitLastBadPacket_Type = OctetString
_WfPppCircuitLastBadPacket_Object = MibTableColumn
wfPppCircuitLastBadPacket = _WfPppCircuitLastBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 47),
    _WfPppCircuitLastBadPacket_Type()
)
wfPppCircuitLastBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitLastBadPacket.setStatus("mandatory")


class _WfPppCircuitCcpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitCcpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitCcpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitCcpCurrentState_Object = MibTableColumn
wfPppCircuitCcpCurrentState = _WfPppCircuitCcpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 48),
    _WfPppCircuitCcpCurrentState_Type()
)
wfPppCircuitCcpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitCcpCurrentState.setStatus("mandatory")


class _WfPppCircuitCcpDisable_Type(Integer32):
    """Custom type wfPppCircuitCcpDisable based on Integer32"""
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


_WfPppCircuitCcpDisable_Type.__name__ = "Integer32"
_WfPppCircuitCcpDisable_Object = MibTableColumn
wfPppCircuitCcpDisable = _WfPppCircuitCcpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 49),
    _WfPppCircuitCcpDisable_Type()
)
wfPppCircuitCcpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCcpDisable.setStatus("mandatory")


class _WfPppCircuitPppMode_Type(Integer32):
    """Custom type wfPppCircuitPppMode based on Integer32"""
    defaultValue = 1

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
        *(("dynamic-monitor", 5),
          ("monitor", 4),
          ("multilink", 3),
          ("nego", 2),
          ("normal", 1))
    )


_WfPppCircuitPppMode_Type.__name__ = "Integer32"
_WfPppCircuitPppMode_Object = MibTableColumn
wfPppCircuitPppMode = _WfPppCircuitPppMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 50),
    _WfPppCircuitPppMode_Type()
)
wfPppCircuitPppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitPppMode.setStatus("mandatory")


class _WfPppCircuitMLFragPerm_Type(Integer32):
    """Custom type wfPppCircuitMLFragPerm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permitted", 1),
          ("prohibited", 2))
    )


_WfPppCircuitMLFragPerm_Type.__name__ = "Integer32"
_WfPppCircuitMLFragPerm_Object = MibTableColumn
wfPppCircuitMLFragPerm = _WfPppCircuitMLFragPerm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 51),
    _WfPppCircuitMLFragPerm_Type()
)
wfPppCircuitMLFragPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMLFragPerm.setStatus("mandatory")


class _WfPppCircuitExamPeriod_Type(Integer32):
    """Custom type wfPppCircuitExamPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_WfPppCircuitExamPeriod_Type.__name__ = "Integer32"
_WfPppCircuitExamPeriod_Object = MibTableColumn
wfPppCircuitExamPeriod = _WfPppCircuitExamPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 52),
    _WfPppCircuitExamPeriod_Type()
)
wfPppCircuitExamPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitExamPeriod.setStatus("mandatory")


class _WfPppCircuitFullThreshold_Type(Integer32):
    """Custom type wfPppCircuitFullThreshold based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfPppCircuitFullThreshold_Type.__name__ = "Integer32"
_WfPppCircuitFullThreshold_Object = MibTableColumn
wfPppCircuitFullThreshold = _WfPppCircuitFullThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 53),
    _WfPppCircuitFullThreshold_Type()
)
wfPppCircuitFullThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitFullThreshold.setStatus("mandatory")


class _WfPppCircuitPeriodsCng_Type(Integer32):
    """Custom type wfPppCircuitPeriodsCng based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfPppCircuitPeriodsCng_Type.__name__ = "Integer32"
_WfPppCircuitPeriodsCng_Object = MibTableColumn
wfPppCircuitPeriodsCng = _WfPppCircuitPeriodsCng_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 54),
    _WfPppCircuitPeriodsCng_Type()
)
wfPppCircuitPeriodsCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitPeriodsCng.setStatus("mandatory")
_WfPppCircuitPrefBwSlot_Type = Integer32
_WfPppCircuitPrefBwSlot_Object = MibTableColumn
wfPppCircuitPrefBwSlot = _WfPppCircuitPrefBwSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 55),
    _WfPppCircuitPrefBwSlot_Type()
)
wfPppCircuitPrefBwSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitPrefBwSlot.setStatus("mandatory")
_WfPppCircuitResvBwSlot_Type = Integer32
_WfPppCircuitResvBwSlot_Object = MibTableColumn
wfPppCircuitResvBwSlot = _WfPppCircuitResvBwSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 56),
    _WfPppCircuitResvBwSlot_Type()
)
wfPppCircuitResvBwSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitResvBwSlot.setStatus("mandatory")


class _WfPppCircuitMLFragTriggerSize_Type(Integer32):
    """Custom type wfPppCircuitMLFragTriggerSize based on Integer32"""
    defaultValue = 256


_WfPppCircuitMLFragTriggerSize_Object = MibTableColumn
wfPppCircuitMLFragTriggerSize = _WfPppCircuitMLFragTriggerSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 57),
    _WfPppCircuitMLFragTriggerSize_Type()
)
wfPppCircuitMLFragTriggerSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMLFragTriggerSize.setStatus("mandatory")


class _WfPppCircuitMaxLinks_Type(Integer32):
    """Custom type wfPppCircuitMaxLinks based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WfPppCircuitMaxLinks_Type.__name__ = "Integer32"
_WfPppCircuitMaxLinks_Object = MibTableColumn
wfPppCircuitMaxLinks = _WfPppCircuitMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 58),
    _WfPppCircuitMaxLinks_Type()
)
wfPppCircuitMaxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMaxLinks.setStatus("mandatory")


class _WfPppCircuitRecoverThreshold_Type(Integer32):
    """Custom type wfPppCircuitRecoverThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfPppCircuitRecoverThreshold_Type.__name__ = "Integer32"
_WfPppCircuitRecoverThreshold_Object = MibTableColumn
wfPppCircuitRecoverThreshold = _WfPppCircuitRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 59),
    _WfPppCircuitRecoverThreshold_Type()
)
wfPppCircuitRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitRecoverThreshold.setStatus("mandatory")


class _WfPppCircuitPeriodsUnCng_Type(Integer32):
    """Custom type wfPppCircuitPeriodsUnCng based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfPppCircuitPeriodsUnCng_Type.__name__ = "Integer32"
_WfPppCircuitPeriodsUnCng_Object = MibTableColumn
wfPppCircuitPeriodsUnCng = _WfPppCircuitPeriodsUnCng_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 60),
    _WfPppCircuitPeriodsUnCng_Type()
)
wfPppCircuitPeriodsUnCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitPeriodsUnCng.setStatus("mandatory")
_WfPppCircuitHistory_Type = DisplayString
_WfPppCircuitHistory_Object = MibTableColumn
wfPppCircuitHistory = _WfPppCircuitHistory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 61),
    _WfPppCircuitHistory_Type()
)
wfPppCircuitHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitHistory.setStatus("mandatory")
_WfPppCircuitDebugFlag_Type = Integer32
_WfPppCircuitDebugFlag_Object = MibTableColumn
wfPppCircuitDebugFlag = _WfPppCircuitDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 62),
    _WfPppCircuitDebugFlag_Type()
)
wfPppCircuitDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitDebugFlag.setStatus("mandatory")


class _WfPppCircuitActualMode_Type(Integer32):
    """Custom type wfPppCircuitActualMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 20),
          ("monitor", 4),
          ("multilink", 3),
          ("normal", 1))
    )


_WfPppCircuitActualMode_Type.__name__ = "Integer32"
_WfPppCircuitActualMode_Object = MibTableColumn
wfPppCircuitActualMode = _WfPppCircuitActualMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 63),
    _WfPppCircuitActualMode_Type()
)
wfPppCircuitActualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitActualMode.setStatus("mandatory")


class _WfPppCircuitMaxBuffers_Type(Integer32):
    """Custom type wfPppCircuitMaxBuffers based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_WfPppCircuitMaxBuffers_Type.__name__ = "Integer32"
_WfPppCircuitMaxBuffers_Object = MibTableColumn
wfPppCircuitMaxBuffers = _WfPppCircuitMaxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 64),
    _WfPppCircuitMaxBuffers_Type()
)
wfPppCircuitMaxBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMaxBuffers.setStatus("mandatory")


class _WfPppCircuitLinksConfigured_Type(Integer32):
    """Custom type wfPppCircuitLinksConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WfPppCircuitLinksConfigured_Type.__name__ = "Integer32"
_WfPppCircuitLinksConfigured_Object = MibTableColumn
wfPppCircuitLinksConfigured = _WfPppCircuitLinksConfigured_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 65),
    _WfPppCircuitLinksConfigured_Type()
)
wfPppCircuitLinksConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitLinksConfigured.setStatus("mandatory")


class _WfPppCircuitBacpDisable_Type(Integer32):
    """Custom type wfPppCircuitBacpDisable based on Integer32"""
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


_WfPppCircuitBacpDisable_Type.__name__ = "Integer32"
_WfPppCircuitBacpDisable_Object = MibTableColumn
wfPppCircuitBacpDisable = _WfPppCircuitBacpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 66),
    _WfPppCircuitBacpDisable_Type()
)
wfPppCircuitBacpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitBacpDisable.setStatus("mandatory")


class _WfPppCircuitBacpCurrentState_Type(Integer32):
    """Custom type wfPppCircuitBacpCurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitBacpCurrentState_Type.__name__ = "Integer32"
_WfPppCircuitBacpCurrentState_Object = MibTableColumn
wfPppCircuitBacpCurrentState = _WfPppCircuitBacpCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 67),
    _WfPppCircuitBacpCurrentState_Type()
)
wfPppCircuitBacpCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitBacpCurrentState.setStatus("mandatory")


class _WfPppCircuitBacpNoPhoneNum_Type(Integer32):
    """Custom type wfPppCircuitBacpNoPhoneNum based on Integer32"""
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


_WfPppCircuitBacpNoPhoneNum_Type.__name__ = "Integer32"
_WfPppCircuitBacpNoPhoneNum_Object = MibTableColumn
wfPppCircuitBacpNoPhoneNum = _WfPppCircuitBacpNoPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 68),
    _WfPppCircuitBacpNoPhoneNum_Type()
)
wfPppCircuitBacpNoPhoneNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitBacpNoPhoneNum.setStatus("mandatory")


class _WfPppCircuitIpv6Disable_Type(Integer32):
    """Custom type wfPppCircuitIpv6Disable based on Integer32"""
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


_WfPppCircuitIpv6Disable_Type.__name__ = "Integer32"
_WfPppCircuitIpv6Disable_Object = MibTableColumn
wfPppCircuitIpv6Disable = _WfPppCircuitIpv6Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 69),
    _WfPppCircuitIpv6Disable_Type()
)
wfPppCircuitIpv6Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitIpv6Disable.setStatus("mandatory")


class _WfPppCircuitIpv6CurrentState_Type(Integer32):
    """Custom type wfPppCircuitIpv6CurrentState based on Integer32"""
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
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_WfPppCircuitIpv6CurrentState_Type.__name__ = "Integer32"
_WfPppCircuitIpv6CurrentState_Object = MibTableColumn
wfPppCircuitIpv6CurrentState = _WfPppCircuitIpv6CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 70),
    _WfPppCircuitIpv6CurrentState_Type()
)
wfPppCircuitIpv6CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitIpv6CurrentState.setStatus("mandatory")


class _WfPppCircuitCcpType_Type(Integer32):
    """Custom type wfPppCircuitCcpType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccp", 2),
          ("ilccp", 1))
    )


_WfPppCircuitCcpType_Type.__name__ = "Integer32"
_WfPppCircuitCcpType_Object = MibTableColumn
wfPppCircuitCcpType = _WfPppCircuitCcpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 71),
    _WfPppCircuitCcpType_Type()
)
wfPppCircuitCcpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCcpType.setStatus("mandatory")


class _WfPppCircuitCfgCcpOptions_Type(Integer32):
    """Custom type wfPppCircuitCfgCcpOptions based on Integer32"""
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
        *(("all", 1),
          ("oui-wcp", 2),
          ("staclzs", 3))
    )


_WfPppCircuitCfgCcpOptions_Type.__name__ = "Integer32"
_WfPppCircuitCfgCcpOptions_Object = MibTableColumn
wfPppCircuitCfgCcpOptions = _WfPppCircuitCfgCcpOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 72),
    _WfPppCircuitCfgCcpOptions_Type()
)
wfPppCircuitCfgCcpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitCfgCcpOptions.setStatus("mandatory")


class _WfPppCircuitCcpOptions_Type(Integer32):
    """Custom type wfPppCircuitCcpOptions based on Integer32"""
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
        *(("none", 1),
          ("oui-wcp", 2),
          ("staclzs", 3))
    )


_WfPppCircuitCcpOptions_Type.__name__ = "Integer32"
_WfPppCircuitCcpOptions_Object = MibTableColumn
wfPppCircuitCcpOptions = _WfPppCircuitCcpOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 73),
    _WfPppCircuitCcpOptions_Type()
)
wfPppCircuitCcpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppCircuitCcpOptions.setStatus("mandatory")


class _WfPppCircuitStacLZSCheckMode_Type(Integer32):
    """Custom type wfPppCircuitStacLZSCheckMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mode0", 1),
          ("mode3", 4))
    )


_WfPppCircuitStacLZSCheckMode_Type.__name__ = "Integer32"
_WfPppCircuitStacLZSCheckMode_Object = MibTableColumn
wfPppCircuitStacLZSCheckMode = _WfPppCircuitStacLZSCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 74),
    _WfPppCircuitStacLZSCheckMode_Type()
)
wfPppCircuitStacLZSCheckMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitStacLZSCheckMode.setStatus("mandatory")


class _WfPppCircuitMLFragStrict_Type(Integer32):
    """Custom type wfPppCircuitMLFragStrict based on Integer32"""
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


_WfPppCircuitMLFragStrict_Type.__name__ = "Integer32"
_WfPppCircuitMLFragStrict_Object = MibTableColumn
wfPppCircuitMLFragStrict = _WfPppCircuitMLFragStrict_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 75),
    _WfPppCircuitMLFragStrict_Type()
)
wfPppCircuitMLFragStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMLFragStrict.setStatus("mandatory")


class _WfPppCircuitLampreyCompDisable_Type(Integer32):
    """Custom type wfPppCircuitLampreyCompDisable based on Integer32"""
    defaultValue = 99

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
              10,
              11,
              12,
              13,
              14,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 99),
          ("slot1", 1),
          ("slot10", 10),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8),
          ("slot9", 9))
    )


_WfPppCircuitLampreyCompDisable_Type.__name__ = "Integer32"
_WfPppCircuitLampreyCompDisable_Object = MibTableColumn
wfPppCircuitLampreyCompDisable = _WfPppCircuitLampreyCompDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 76),
    _WfPppCircuitLampreyCompDisable_Type()
)
wfPppCircuitLampreyCompDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitLampreyCompDisable.setStatus("mandatory")


class _WfPppCircuitMsgLevel_Type(Integer32):
    """Custom type wfPppCircuitMsgLevel based on Integer32"""
    defaultValue = 917504

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              131072,
              262144,
              524288,
              917504,
              1048576,
              2031616)
        )
    )
    namedValues = NamedValues(
        *(("all", 2031616),
          ("debug", 65536),
          ("fault", 524288),
          ("info", 131072),
          ("infofaultwarning", 917504),
          ("trace", 1048576),
          ("warning", 262144))
    )


_WfPppCircuitMsgLevel_Type.__name__ = "Integer32"
_WfPppCircuitMsgLevel_Object = MibTableColumn
wfPppCircuitMsgLevel = _WfPppCircuitMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 77),
    _WfPppCircuitMsgLevel_Type()
)
wfPppCircuitMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitMsgLevel.setStatus("mandatory")


class _WfPppCircuitType_Type(Integer32):
    """Custom type wfPppCircuitType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("l2tp", 2),
          ("leased", 3),
          ("unknown", 9))
    )


_WfPppCircuitType_Type.__name__ = "Integer32"
_WfPppCircuitType_Object = MibTableColumn
wfPppCircuitType = _WfPppCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 78),
    _WfPppCircuitType_Type()
)
wfPppCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitType.setStatus("mandatory")


class _WfPppCircuitWRCompatability_Type(Integer32):
    """Custom type wfPppCircuitWRCompatability based on Integer32"""
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


_WfPppCircuitWRCompatability_Type.__name__ = "Integer32"
_WfPppCircuitWRCompatability_Object = MibTableColumn
wfPppCircuitWRCompatability = _WfPppCircuitWRCompatability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 2, 1, 79),
    _WfPppCircuitWRCompatability_Type()
)
wfPppCircuitWRCompatability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppCircuitWRCompatability.setStatus("mandatory")
_WfPppWhoamiTable_Object = MibTable
wfPppWhoamiTable = _WfPppWhoamiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3)
)
if mibBuilder.loadTexts:
    wfPppWhoamiTable.setStatus("mandatory")
_WfPppWhoamiEntry_Object = MibTableRow
wfPppWhoamiEntry = _WfPppWhoamiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1)
)
wfPppWhoamiEntry.setIndexNames(
    (0, "Wellfleet-PPP-MIB", "wfPppWhoamiName"),
)
if mibBuilder.loadTexts:
    wfPppWhoamiEntry.setStatus("mandatory")


class _WfPppWhoamiDelete_Type(Integer32):
    """Custom type wfPppWhoamiDelete based on Integer32"""
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


_WfPppWhoamiDelete_Type.__name__ = "Integer32"
_WfPppWhoamiDelete_Object = MibTableColumn
wfPppWhoamiDelete = _WfPppWhoamiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 1),
    _WfPppWhoamiDelete_Type()
)
wfPppWhoamiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppWhoamiDelete.setStatus("mandatory")
_WfPppWhoamiName_Type = DisplayString
_WfPppWhoamiName_Object = MibTableColumn
wfPppWhoamiName = _WfPppWhoamiName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 2),
    _WfPppWhoamiName_Type()
)
wfPppWhoamiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppWhoamiName.setStatus("mandatory")
_WfPppWhoamiCircuit_Type = Integer32
_WfPppWhoamiCircuit_Object = MibTableColumn
wfPppWhoamiCircuit = _WfPppWhoamiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 3),
    _WfPppWhoamiCircuit_Type()
)
wfPppWhoamiCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppWhoamiCircuit.setStatus("mandatory")
_WfPppWhoamiSecret_Type = DisplayString
_WfPppWhoamiSecret_Object = MibTableColumn
wfPppWhoamiSecret = _WfPppWhoamiSecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 4),
    _WfPppWhoamiSecret_Type()
)
wfPppWhoamiSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppWhoamiSecret.setStatus("mandatory")
_WfPppWhoamiPapPassword_Type = DisplayString
_WfPppWhoamiPapPassword_Object = MibTableColumn
wfPppWhoamiPapPassword = _WfPppWhoamiPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 5),
    _WfPppWhoamiPapPassword_Type()
)
wfPppWhoamiPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppWhoamiPapPassword.setStatus("mandatory")
_WfPppWhoamiCctGrp_Type = Integer32
_WfPppWhoamiCctGrp_Object = MibTableColumn
wfPppWhoamiCctGrp = _WfPppWhoamiCctGrp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 3, 1, 6),
    _WfPppWhoamiCctGrp_Type()
)
wfPppWhoamiCctGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppWhoamiCctGrp.setStatus("mandatory")
_WfPppMlStatsTable_Object = MibTable
wfPppMlStatsTable = _WfPppMlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4)
)
if mibBuilder.loadTexts:
    wfPppMlStatsTable.setStatus("mandatory")
_WfPppMlStatsEntry_Object = MibTableRow
wfPppMlStatsEntry = _WfPppMlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1)
)
wfPppMlStatsEntry.setIndexNames(
    (0, "Wellfleet-PPP-MIB", "wfPppMlStatsCircuitID"),
)
if mibBuilder.loadTexts:
    wfPppMlStatsEntry.setStatus("mandatory")


class _WfPppMlStatsDelete_Type(Integer32):
    """Custom type wfPppMlStatsDelete based on Integer32"""
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


_WfPppMlStatsDelete_Type.__name__ = "Integer32"
_WfPppMlStatsDelete_Object = MibTableColumn
wfPppMlStatsDelete = _WfPppMlStatsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 1),
    _WfPppMlStatsDelete_Type()
)
wfPppMlStatsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppMlStatsDelete.setStatus("mandatory")


class _WfPppMlStatsCircuitID_Type(Integer32):
    """Custom type wfPppMlStatsCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfPppMlStatsCircuitID_Type.__name__ = "Integer32"
_WfPppMlStatsCircuitID_Object = MibTableColumn
wfPppMlStatsCircuitID = _WfPppMlStatsCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 2),
    _WfPppMlStatsCircuitID_Type()
)
wfPppMlStatsCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsCircuitID.setStatus("mandatory")
_WfPppMlStatsHomeSlot_Type = Integer32
_WfPppMlStatsHomeSlot_Object = MibTableColumn
wfPppMlStatsHomeSlot = _WfPppMlStatsHomeSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 3),
    _WfPppMlStatsHomeSlot_Type()
)
wfPppMlStatsHomeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsHomeSlot.setStatus("mandatory")
_WfPppMlStatsLineCnt_Type = Gauge32
_WfPppMlStatsLineCnt_Object = MibTableColumn
wfPppMlStatsLineCnt = _WfPppMlStatsLineCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 4),
    _WfPppMlStatsLineCnt_Type()
)
wfPppMlStatsLineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsLineCnt.setStatus("mandatory")
_WfPppMlStatsBundleSpd_Type = Gauge32
_WfPppMlStatsBundleSpd_Object = MibTableColumn
wfPppMlStatsBundleSpd = _WfPppMlStatsBundleSpd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 5),
    _WfPppMlStatsBundleSpd_Type()
)
wfPppMlStatsBundleSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsBundleSpd.setStatus("mandatory")
_WfPppMlStatsMrru_Type = Gauge32
_WfPppMlStatsMrru_Object = MibTableColumn
wfPppMlStatsMrru = _WfPppMlStatsMrru_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 6),
    _WfPppMlStatsMrru_Type()
)
wfPppMlStatsMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsMrru.setStatus("mandatory")
_WfPppMlStatsEndptDisc_Type = OctetString
_WfPppMlStatsEndptDisc_Object = MibTableColumn
wfPppMlStatsEndptDisc = _WfPppMlStatsEndptDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 7),
    _WfPppMlStatsEndptDisc_Type()
)
wfPppMlStatsEndptDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsEndptDisc.setStatus("mandatory")
_WfPppMlStatsTxOctets_Type = Counter32
_WfPppMlStatsTxOctets_Object = MibTableColumn
wfPppMlStatsTxOctets = _WfPppMlStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 8),
    _WfPppMlStatsTxOctets_Type()
)
wfPppMlStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsTxOctets.setStatus("mandatory")
_WfPppMlStatsTxPkts_Type = Counter32
_WfPppMlStatsTxPkts_Object = MibTableColumn
wfPppMlStatsTxPkts = _WfPppMlStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 9),
    _WfPppMlStatsTxPkts_Type()
)
wfPppMlStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsTxPkts.setStatus("mandatory")
_WfPppMlStatsAvgTxListLen_Type = Gauge32
_WfPppMlStatsAvgTxListLen_Object = MibTableColumn
wfPppMlStatsAvgTxListLen = _WfPppMlStatsAvgTxListLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 10),
    _WfPppMlStatsAvgTxListLen_Type()
)
wfPppMlStatsAvgTxListLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsAvgTxListLen.setStatus("mandatory")
_WfPppMlStatsRxOctets_Type = Counter32
_WfPppMlStatsRxOctets_Object = MibTableColumn
wfPppMlStatsRxOctets = _WfPppMlStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 11),
    _WfPppMlStatsRxOctets_Type()
)
wfPppMlStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsRxOctets.setStatus("mandatory")
_WfPppMlStatsRxPkts_Type = Counter32
_WfPppMlStatsRxPkts_Object = MibTableColumn
wfPppMlStatsRxPkts = _WfPppMlStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 12),
    _WfPppMlStatsRxPkts_Type()
)
wfPppMlStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsRxPkts.setStatus("mandatory")
_WfPppMlStatsReasmFails_Type = Counter32
_WfPppMlStatsReasmFails_Object = MibTableColumn
wfPppMlStatsReasmFails = _WfPppMlStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 13),
    _WfPppMlStatsReasmFails_Type()
)
wfPppMlStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsReasmFails.setStatus("mandatory")
_WfPppMlStatsSeqNumberLost_Type = Counter32
_WfPppMlStatsSeqNumberLost_Object = MibTableColumn
wfPppMlStatsSeqNumberLost = _WfPppMlStatsSeqNumberLost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 14),
    _WfPppMlStatsSeqNumberLost_Type()
)
wfPppMlStatsSeqNumberLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsSeqNumberLost.setStatus("mandatory")
_WfPppMlStatsSeqNumberArrivedLate_Type = Counter32
_WfPppMlStatsSeqNumberArrivedLate_Object = MibTableColumn
wfPppMlStatsSeqNumberArrivedLate = _WfPppMlStatsSeqNumberArrivedLate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 15),
    _WfPppMlStatsSeqNumberArrivedLate_Type()
)
wfPppMlStatsSeqNumberArrivedLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsSeqNumberArrivedLate.setStatus("mandatory")
_WfPppMlStatsReSeqBufferCnt_Type = Gauge32
_WfPppMlStatsReSeqBufferCnt_Object = MibTableColumn
wfPppMlStatsReSeqBufferCnt = _WfPppMlStatsReSeqBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 16),
    _WfPppMlStatsReSeqBufferCnt_Type()
)
wfPppMlStatsReSeqBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsReSeqBufferCnt.setStatus("mandatory")
_WfPppMlStatsReSeqBufferMax_Type = Counter32
_WfPppMlStatsReSeqBufferMax_Object = MibTableColumn
wfPppMlStatsReSeqBufferMax = _WfPppMlStatsReSeqBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 17),
    _WfPppMlStatsReSeqBufferMax_Type()
)
wfPppMlStatsReSeqBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsReSeqBufferMax.setStatus("mandatory")
_WfPppMlStatsExceededBufferMax_Type = Counter32
_WfPppMlStatsExceededBufferMax_Object = MibTableColumn
wfPppMlStatsExceededBufferMax = _WfPppMlStatsExceededBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 18),
    _WfPppMlStatsExceededBufferMax_Type()
)
wfPppMlStatsExceededBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsExceededBufferMax.setStatus("mandatory")
_WfPppMlStatsLinkIdleEvents_Type = Counter32
_WfPppMlStatsLinkIdleEvents_Object = MibTableColumn
wfPppMlStatsLinkIdleEvents = _WfPppMlStatsLinkIdleEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 19),
    _WfPppMlStatsLinkIdleEvents_Type()
)
wfPppMlStatsLinkIdleEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsLinkIdleEvents.setStatus("mandatory")


class _WfPppMlStatsCalcPercent_Type(Integer32):
    """Custom type wfPppMlStatsCalcPercent based on Integer32"""
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


_WfPppMlStatsCalcPercent_Type.__name__ = "Integer32"
_WfPppMlStatsCalcPercent_Object = MibTableColumn
wfPppMlStatsCalcPercent = _WfPppMlStatsCalcPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 20),
    _WfPppMlStatsCalcPercent_Type()
)
wfPppMlStatsCalcPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppMlStatsCalcPercent.setStatus("mandatory")
_WfPppMlStatsDebug_Type = Integer32
_WfPppMlStatsDebug_Object = MibTableColumn
wfPppMlStatsDebug = _WfPppMlStatsDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 21),
    _WfPppMlStatsDebug_Type()
)
wfPppMlStatsDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppMlStatsDebug.setStatus("mandatory")
_WfPppMlStatsReassmBufferCnt_Type = Gauge32
_WfPppMlStatsReassmBufferCnt_Object = MibTableColumn
wfPppMlStatsReassmBufferCnt = _WfPppMlStatsReassmBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 22),
    _WfPppMlStatsReassmBufferCnt_Type()
)
wfPppMlStatsReassmBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsReassmBufferCnt.setStatus("mandatory")
_WfPppMlStatsReassmBufferMax_Type = Counter32
_WfPppMlStatsReassmBufferMax_Object = MibTableColumn
wfPppMlStatsReassmBufferMax = _WfPppMlStatsReassmBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 23),
    _WfPppMlStatsReassmBufferMax_Type()
)
wfPppMlStatsReassmBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsReassmBufferMax.setStatus("mandatory")
_WfPppMlStatsNumPktsFragmented_Type = Counter32
_WfPppMlStatsNumPktsFragmented_Object = MibTableColumn
wfPppMlStatsNumPktsFragmented = _WfPppMlStatsNumPktsFragmented_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 24),
    _WfPppMlStatsNumPktsFragmented_Type()
)
wfPppMlStatsNumPktsFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsNumPktsFragmented.setStatus("mandatory")
_WfPppMlStatsPQHiXmits_Type = Counter32
_WfPppMlStatsPQHiXmits_Object = MibTableColumn
wfPppMlStatsPQHiXmits = _WfPppMlStatsPQHiXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 25),
    _WfPppMlStatsPQHiXmits_Type()
)
wfPppMlStatsPQHiXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQHiXmits.setStatus("mandatory")
_WfPppMlStatsPQNormalXmits_Type = Counter32
_WfPppMlStatsPQNormalXmits_Object = MibTableColumn
wfPppMlStatsPQNormalXmits = _WfPppMlStatsPQNormalXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 26),
    _WfPppMlStatsPQNormalXmits_Type()
)
wfPppMlStatsPQNormalXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQNormalXmits.setStatus("mandatory")
_WfPppMlStatsPQLoXmits_Type = Counter32
_WfPppMlStatsPQLoXmits_Object = MibTableColumn
wfPppMlStatsPQLoXmits = _WfPppMlStatsPQLoXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 27),
    _WfPppMlStatsPQLoXmits_Type()
)
wfPppMlStatsPQLoXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQLoXmits.setStatus("mandatory")
_WfPppMlStatsPQHiClippedPkts_Type = Counter32
_WfPppMlStatsPQHiClippedPkts_Object = MibTableColumn
wfPppMlStatsPQHiClippedPkts = _WfPppMlStatsPQHiClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 28),
    _WfPppMlStatsPQHiClippedPkts_Type()
)
wfPppMlStatsPQHiClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQHiClippedPkts.setStatus("mandatory")
_WfPppMlStatsPQNormalClippedPkts_Type = Counter32
_WfPppMlStatsPQNormalClippedPkts_Object = MibTableColumn
wfPppMlStatsPQNormalClippedPkts = _WfPppMlStatsPQNormalClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 29),
    _WfPppMlStatsPQNormalClippedPkts_Type()
)
wfPppMlStatsPQNormalClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQNormalClippedPkts.setStatus("mandatory")
_WfPppMlStatsPQLoClippedPkts_Type = Counter32
_WfPppMlStatsPQLoClippedPkts_Object = MibTableColumn
wfPppMlStatsPQLoClippedPkts = _WfPppMlStatsPQLoClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 30),
    _WfPppMlStatsPQLoClippedPkts_Type()
)
wfPppMlStatsPQLoClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQLoClippedPkts.setStatus("mandatory")
_WfPppMlStatsPQIntrQHighWaterPkts_Type = Gauge32
_WfPppMlStatsPQIntrQHighWaterPkts_Object = MibTableColumn
wfPppMlStatsPQIntrQHighWaterPkts = _WfPppMlStatsPQIntrQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 31),
    _WfPppMlStatsPQIntrQHighWaterPkts_Type()
)
wfPppMlStatsPQIntrQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQIntrQHighWaterPkts.setStatus("mandatory")
_WfPppMlStatsPQHiQHighWaterPkts_Type = Gauge32
_WfPppMlStatsPQHiQHighWaterPkts_Object = MibTableColumn
wfPppMlStatsPQHiQHighWaterPkts = _WfPppMlStatsPQHiQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 32),
    _WfPppMlStatsPQHiQHighWaterPkts_Type()
)
wfPppMlStatsPQHiQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQHiQHighWaterPkts.setStatus("mandatory")
_WfPppMlStatsPQNormalQHighWaterPkts_Type = Gauge32
_WfPppMlStatsPQNormalQHighWaterPkts_Object = MibTableColumn
wfPppMlStatsPQNormalQHighWaterPkts = _WfPppMlStatsPQNormalQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 33),
    _WfPppMlStatsPQNormalQHighWaterPkts_Type()
)
wfPppMlStatsPQNormalQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQNormalQHighWaterPkts.setStatus("mandatory")
_WfPppMlStatsPQLoQHighWaterPkts_Type = Gauge32
_WfPppMlStatsPQLoQHighWaterPkts_Object = MibTableColumn
wfPppMlStatsPQLoQHighWaterPkts = _WfPppMlStatsPQLoQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 34),
    _WfPppMlStatsPQLoQHighWaterPkts_Type()
)
wfPppMlStatsPQLoQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQLoQHighWaterPkts.setStatus("mandatory")
_WfPppMlStatsPQHighWaterPktsClear_Type = Integer32
_WfPppMlStatsPQHighWaterPktsClear_Object = MibTableColumn
wfPppMlStatsPQHighWaterPktsClear = _WfPppMlStatsPQHighWaterPktsClear_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 35),
    _WfPppMlStatsPQHighWaterPktsClear_Type()
)
wfPppMlStatsPQHighWaterPktsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppMlStatsPQHighWaterPktsClear.setStatus("mandatory")
_WfPppMlStatsPQDroppedPkts_Type = Counter32
_WfPppMlStatsPQDroppedPkts_Object = MibTableColumn
wfPppMlStatsPQDroppedPkts = _WfPppMlStatsPQDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 36),
    _WfPppMlStatsPQDroppedPkts_Type()
)
wfPppMlStatsPQDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQDroppedPkts.setStatus("mandatory")
_WfPppMlStatsPQLargePkts_Type = Counter32
_WfPppMlStatsPQLargePkts_Object = MibTableColumn
wfPppMlStatsPQLargePkts = _WfPppMlStatsPQLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 37),
    _WfPppMlStatsPQLargePkts_Type()
)
wfPppMlStatsPQLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQLargePkts.setStatus("mandatory")
_WfPppMlStatsPQHiTotalOctets_Type = Counter32
_WfPppMlStatsPQHiTotalOctets_Object = MibTableColumn
wfPppMlStatsPQHiTotalOctets = _WfPppMlStatsPQHiTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 38),
    _WfPppMlStatsPQHiTotalOctets_Type()
)
wfPppMlStatsPQHiTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQHiTotalOctets.setStatus("mandatory")
_WfPppMlStatsPQNormalTotalOctets_Type = Counter32
_WfPppMlStatsPQNormalTotalOctets_Object = MibTableColumn
wfPppMlStatsPQNormalTotalOctets = _WfPppMlStatsPQNormalTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 39),
    _WfPppMlStatsPQNormalTotalOctets_Type()
)
wfPppMlStatsPQNormalTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQNormalTotalOctets.setStatus("mandatory")
_WfPppMlStatsPQLoTotalOctets_Type = Counter32
_WfPppMlStatsPQLoTotalOctets_Object = MibTableColumn
wfPppMlStatsPQLoTotalOctets = _WfPppMlStatsPQLoTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 40),
    _WfPppMlStatsPQLoTotalOctets_Type()
)
wfPppMlStatsPQLoTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQLoTotalOctets.setStatus("mandatory")
_WfPppMlStatsPQPktsNotQueued_Type = Counter32
_WfPppMlStatsPQPktsNotQueued_Object = MibTableColumn
wfPppMlStatsPQPktsNotQueued = _WfPppMlStatsPQPktsNotQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 4, 1, 41),
    _WfPppMlStatsPQPktsNotQueued_Type()
)
wfPppMlStatsPQPktsNotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppMlStatsPQPktsNotQueued.setStatus("mandatory")
_WfPppBapStatsTable_Object = MibTable
wfPppBapStatsTable = _WfPppBapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5)
)
if mibBuilder.loadTexts:
    wfPppBapStatsTable.setStatus("mandatory")
_WfPppBapStatsEntry_Object = MibTableRow
wfPppBapStatsEntry = _WfPppBapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1)
)
wfPppBapStatsEntry.setIndexNames(
    (0, "Wellfleet-PPP-MIB", "wfPppBapStatsCircuitID"),
)
if mibBuilder.loadTexts:
    wfPppBapStatsEntry.setStatus("mandatory")


class _WfPppBapStatsDelete_Type(Integer32):
    """Custom type wfPppBapStatsDelete based on Integer32"""
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


_WfPppBapStatsDelete_Type.__name__ = "Integer32"
_WfPppBapStatsDelete_Object = MibTableColumn
wfPppBapStatsDelete = _WfPppBapStatsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 1),
    _WfPppBapStatsDelete_Type()
)
wfPppBapStatsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPppBapStatsDelete.setStatus("mandatory")


class _WfPppBapStatsCircuitID_Type(Integer32):
    """Custom type wfPppBapStatsCircuitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfPppBapStatsCircuitID_Type.__name__ = "Integer32"
_WfPppBapStatsCircuitID_Object = MibTableColumn
wfPppBapStatsCircuitID = _WfPppBapStatsCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 2),
    _WfPppBapStatsCircuitID_Type()
)
wfPppBapStatsCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapStatsCircuitID.setStatus("mandatory")
_WfPppBapCallReqTx_Type = Counter32
_WfPppBapCallReqTx_Object = MibTableColumn
wfPppBapCallReqTx = _WfPppBapCallReqTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 3),
    _WfPppBapCallReqTx_Type()
)
wfPppBapCallReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallReqTx.setStatus("mandatory")
_WfPppBapCallRespAckTx_Type = Counter32
_WfPppBapCallRespAckTx_Object = MibTableColumn
wfPppBapCallRespAckTx = _WfPppBapCallRespAckTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 4),
    _WfPppBapCallRespAckTx_Type()
)
wfPppBapCallRespAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespAckTx.setStatus("mandatory")
_WfPppBapCallRespNakTx_Type = Counter32
_WfPppBapCallRespNakTx_Object = MibTableColumn
wfPppBapCallRespNakTx = _WfPppBapCallRespNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 5),
    _WfPppBapCallRespNakTx_Type()
)
wfPppBapCallRespNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespNakTx.setStatus("mandatory")
_WfPppBapCallRespFullNakTx_Type = Counter32
_WfPppBapCallRespFullNakTx_Object = MibTableColumn
wfPppBapCallRespFullNakTx = _WfPppBapCallRespFullNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 6),
    _WfPppBapCallRespFullNakTx_Type()
)
wfPppBapCallRespFullNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespFullNakTx.setStatus("mandatory")
_WfPppBapCallRespRejTx_Type = Counter32
_WfPppBapCallRespRejTx_Object = MibTableColumn
wfPppBapCallRespRejTx = _WfPppBapCallRespRejTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 7),
    _WfPppBapCallRespRejTx_Type()
)
wfPppBapCallRespRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespRejTx.setStatus("mandatory")
_WfPppBapCallbackReqTx_Type = Counter32
_WfPppBapCallbackReqTx_Object = MibTableColumn
wfPppBapCallbackReqTx = _WfPppBapCallbackReqTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 8),
    _WfPppBapCallbackReqTx_Type()
)
wfPppBapCallbackReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackReqTx.setStatus("mandatory")
_WfPppBapCallbackRespAckTx_Type = Counter32
_WfPppBapCallbackRespAckTx_Object = MibTableColumn
wfPppBapCallbackRespAckTx = _WfPppBapCallbackRespAckTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 9),
    _WfPppBapCallbackRespAckTx_Type()
)
wfPppBapCallbackRespAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespAckTx.setStatus("mandatory")
_WfPppBapCallbackRespNakTx_Type = Counter32
_WfPppBapCallbackRespNakTx_Object = MibTableColumn
wfPppBapCallbackRespNakTx = _WfPppBapCallbackRespNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 10),
    _WfPppBapCallbackRespNakTx_Type()
)
wfPppBapCallbackRespNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespNakTx.setStatus("mandatory")
_WfPppBapCallbackRespFullNakTx_Type = Counter32
_WfPppBapCallbackRespFullNakTx_Object = MibTableColumn
wfPppBapCallbackRespFullNakTx = _WfPppBapCallbackRespFullNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 11),
    _WfPppBapCallbackRespFullNakTx_Type()
)
wfPppBapCallbackRespFullNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespFullNakTx.setStatus("mandatory")
_WfPppBapCallbackRespRejTx_Type = Counter32
_WfPppBapCallbackRespRejTx_Object = MibTableColumn
wfPppBapCallbackRespRejTx = _WfPppBapCallbackRespRejTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 12),
    _WfPppBapCallbackRespRejTx_Type()
)
wfPppBapCallbackRespRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespRejTx.setStatus("mandatory")
_WfPppBapLdQueryReqTx_Type = Counter32
_WfPppBapLdQueryReqTx_Object = MibTableColumn
wfPppBapLdQueryReqTx = _WfPppBapLdQueryReqTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 13),
    _WfPppBapLdQueryReqTx_Type()
)
wfPppBapLdQueryReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryReqTx.setStatus("mandatory")
_WfPppBapLdQueryRespAckTx_Type = Counter32
_WfPppBapLdQueryRespAckTx_Object = MibTableColumn
wfPppBapLdQueryRespAckTx = _WfPppBapLdQueryRespAckTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 14),
    _WfPppBapLdQueryRespAckTx_Type()
)
wfPppBapLdQueryRespAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespAckTx.setStatus("mandatory")
_WfPppBapLdQueryRespNakTx_Type = Counter32
_WfPppBapLdQueryRespNakTx_Object = MibTableColumn
wfPppBapLdQueryRespNakTx = _WfPppBapLdQueryRespNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 15),
    _WfPppBapLdQueryRespNakTx_Type()
)
wfPppBapLdQueryRespNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespNakTx.setStatus("mandatory")
_WfPppBapLdQueryRespFullNakTx_Type = Counter32
_WfPppBapLdQueryRespFullNakTx_Object = MibTableColumn
wfPppBapLdQueryRespFullNakTx = _WfPppBapLdQueryRespFullNakTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 16),
    _WfPppBapLdQueryRespFullNakTx_Type()
)
wfPppBapLdQueryRespFullNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespFullNakTx.setStatus("mandatory")
_WfPppBapCallStatusIndFailTx_Type = Counter32
_WfPppBapCallStatusIndFailTx_Object = MibTableColumn
wfPppBapCallStatusIndFailTx = _WfPppBapCallStatusIndFailTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 17),
    _WfPppBapCallStatusIndFailTx_Type()
)
wfPppBapCallStatusIndFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusIndFailTx.setStatus("mandatory")
_WfPppBapCallStatusIndSuccessTx_Type = Counter32
_WfPppBapCallStatusIndSuccessTx_Object = MibTableColumn
wfPppBapCallStatusIndSuccessTx = _WfPppBapCallStatusIndSuccessTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 18),
    _WfPppBapCallStatusIndSuccessTx_Type()
)
wfPppBapCallStatusIndSuccessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusIndSuccessTx.setStatus("mandatory")
_WfPppBapCallStatusRespTx_Type = Counter32
_WfPppBapCallStatusRespTx_Object = MibTableColumn
wfPppBapCallStatusRespTx = _WfPppBapCallStatusRespTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 19),
    _WfPppBapCallStatusRespTx_Type()
)
wfPppBapCallStatusRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusRespTx.setStatus("mandatory")
_WfPppBapCallReqRx_Type = Counter32
_WfPppBapCallReqRx_Object = MibTableColumn
wfPppBapCallReqRx = _WfPppBapCallReqRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 20),
    _WfPppBapCallReqRx_Type()
)
wfPppBapCallReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallReqRx.setStatus("mandatory")
_WfPppBapCallRespAckRx_Type = Counter32
_WfPppBapCallRespAckRx_Object = MibTableColumn
wfPppBapCallRespAckRx = _WfPppBapCallRespAckRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 21),
    _WfPppBapCallRespAckRx_Type()
)
wfPppBapCallRespAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespAckRx.setStatus("mandatory")
_WfPppBapCallRespNakRx_Type = Counter32
_WfPppBapCallRespNakRx_Object = MibTableColumn
wfPppBapCallRespNakRx = _WfPppBapCallRespNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 22),
    _WfPppBapCallRespNakRx_Type()
)
wfPppBapCallRespNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespNakRx.setStatus("mandatory")
_WfPppBapCallRespFullNakRx_Type = Counter32
_WfPppBapCallRespFullNakRx_Object = MibTableColumn
wfPppBapCallRespFullNakRx = _WfPppBapCallRespFullNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 23),
    _WfPppBapCallRespFullNakRx_Type()
)
wfPppBapCallRespFullNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespFullNakRx.setStatus("mandatory")
_WfPppBapCallRespRejRx_Type = Counter32
_WfPppBapCallRespRejRx_Object = MibTableColumn
wfPppBapCallRespRejRx = _WfPppBapCallRespRejRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 24),
    _WfPppBapCallRespRejRx_Type()
)
wfPppBapCallRespRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallRespRejRx.setStatus("mandatory")
_WfPppBapCallbackReqRx_Type = Counter32
_WfPppBapCallbackReqRx_Object = MibTableColumn
wfPppBapCallbackReqRx = _WfPppBapCallbackReqRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 25),
    _WfPppBapCallbackReqRx_Type()
)
wfPppBapCallbackReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackReqRx.setStatus("mandatory")
_WfPppBapCallbackRespAckRx_Type = Counter32
_WfPppBapCallbackRespAckRx_Object = MibTableColumn
wfPppBapCallbackRespAckRx = _WfPppBapCallbackRespAckRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 26),
    _WfPppBapCallbackRespAckRx_Type()
)
wfPppBapCallbackRespAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespAckRx.setStatus("mandatory")
_WfPppBapCallbackRespNakRx_Type = Counter32
_WfPppBapCallbackRespNakRx_Object = MibTableColumn
wfPppBapCallbackRespNakRx = _WfPppBapCallbackRespNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 27),
    _WfPppBapCallbackRespNakRx_Type()
)
wfPppBapCallbackRespNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespNakRx.setStatus("mandatory")
_WfPppBapCallbackRespFullNakRx_Type = Counter32
_WfPppBapCallbackRespFullNakRx_Object = MibTableColumn
wfPppBapCallbackRespFullNakRx = _WfPppBapCallbackRespFullNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 28),
    _WfPppBapCallbackRespFullNakRx_Type()
)
wfPppBapCallbackRespFullNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespFullNakRx.setStatus("mandatory")
_WfPppBapCallbackRespRejRx_Type = Counter32
_WfPppBapCallbackRespRejRx_Object = MibTableColumn
wfPppBapCallbackRespRejRx = _WfPppBapCallbackRespRejRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 29),
    _WfPppBapCallbackRespRejRx_Type()
)
wfPppBapCallbackRespRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackRespRejRx.setStatus("mandatory")
_WfPppBapLdQueryReqRx_Type = Counter32
_WfPppBapLdQueryReqRx_Object = MibTableColumn
wfPppBapLdQueryReqRx = _WfPppBapLdQueryReqRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 30),
    _WfPppBapLdQueryReqRx_Type()
)
wfPppBapLdQueryReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryReqRx.setStatus("mandatory")
_WfPppBapLdQueryRespAckRx_Type = Counter32
_WfPppBapLdQueryRespAckRx_Object = MibTableColumn
wfPppBapLdQueryRespAckRx = _WfPppBapLdQueryRespAckRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 31),
    _WfPppBapLdQueryRespAckRx_Type()
)
wfPppBapLdQueryRespAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespAckRx.setStatus("mandatory")
_WfPppBapLdQueryRespNakRx_Type = Counter32
_WfPppBapLdQueryRespNakRx_Object = MibTableColumn
wfPppBapLdQueryRespNakRx = _WfPppBapLdQueryRespNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 32),
    _WfPppBapLdQueryRespNakRx_Type()
)
wfPppBapLdQueryRespNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespNakRx.setStatus("mandatory")
_WfPppBapLdQueryRespFullNakRx_Type = Counter32
_WfPppBapLdQueryRespFullNakRx_Object = MibTableColumn
wfPppBapLdQueryRespFullNakRx = _WfPppBapLdQueryRespFullNakRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 33),
    _WfPppBapLdQueryRespFullNakRx_Type()
)
wfPppBapLdQueryRespFullNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapLdQueryRespFullNakRx.setStatus("mandatory")
_WfPppBapCallStatusIndFailRx_Type = Counter32
_WfPppBapCallStatusIndFailRx_Object = MibTableColumn
wfPppBapCallStatusIndFailRx = _WfPppBapCallStatusIndFailRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 34),
    _WfPppBapCallStatusIndFailRx_Type()
)
wfPppBapCallStatusIndFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusIndFailRx.setStatus("mandatory")
_WfPppBapCallStatusIndSuccessRx_Type = Counter32
_WfPppBapCallStatusIndSuccessRx_Object = MibTableColumn
wfPppBapCallStatusIndSuccessRx = _WfPppBapCallStatusIndSuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 35),
    _WfPppBapCallStatusIndSuccessRx_Type()
)
wfPppBapCallStatusIndSuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusIndSuccessRx.setStatus("mandatory")
_WfPppBapCallStatusRespRx_Type = Counter32
_WfPppBapCallStatusRespRx_Object = MibTableColumn
wfPppBapCallStatusRespRx = _WfPppBapCallStatusRespRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 36),
    _WfPppBapCallStatusRespRx_Type()
)
wfPppBapCallStatusRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallStatusRespRx.setStatus("mandatory")
_WfPppBapCallReqRespDiscardRx_Type = Counter32
_WfPppBapCallReqRespDiscardRx_Object = MibTableColumn
wfPppBapCallReqRespDiscardRx = _WfPppBapCallReqRespDiscardRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 37),
    _WfPppBapCallReqRespDiscardRx_Type()
)
wfPppBapCallReqRespDiscardRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallReqRespDiscardRx.setStatus("mandatory")
_WfPppBapCallbackReqRespDiscardRx_Type = Counter32
_WfPppBapCallbackReqRespDiscardRx_Object = MibTableColumn
wfPppBapCallbackReqRespDiscardRx = _WfPppBapCallbackReqRespDiscardRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2, 5, 1, 38),
    _WfPppBapCallbackReqRespDiscardRx_Type()
)
wfPppBapCallbackReqRespDiscardRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPppBapCallbackReqRespDiscardRx.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PPP-MIB",
    **{"wfPppLineTable": wfPppLineTable,
       "wfPppLineEntry": wfPppLineEntry,
       "wfPppLineDelete": wfPppLineDelete,
       "wfPppLineDisable": wfPppLineDisable,
       "wfPppLineState": wfPppLineState,
       "wfPppLineLineNumber": wfPppLineLineNumber,
       "wfPppLineLLIndex": wfPppLineLLIndex,
       "wfPppLineLcpCurrentState": wfPppLineLcpCurrentState,
       "wfPppLineRestartTimer": wfPppLineRestartTimer,
       "wfPppLineEchoRequestFreq": wfPppLineEchoRequestFreq,
       "wfPppLineEchoReplyLoss": wfPppLineEchoReplyLoss,
       "wfPppLineMaxConfReq": wfPppLineMaxConfReq,
       "wfPppLineMaxTermReq": wfPppLineMaxTermReq,
       "wfPppLineMaxConfFail": wfPppLineMaxConfFail,
       "wfPppLineMagicNumber": wfPppLineMagicNumber,
       "wfPppLineMru": wfPppLineMru,
       "wfPppLineLocalAuthProtocol": wfPppLineLocalAuthProtocol,
       "wfPppLineRemoteAuthProtocol": wfPppLineRemoteAuthProtocol,
       "wfPppLineLocalPapId": wfPppLineLocalPapId,
       "wfPppLineLocalPapPassword": wfPppLineLocalPapPassword,
       "wfPppLineRemotePapId": wfPppLineRemotePapId,
       "wfPppLineRemotePapPassword": wfPppLineRemotePapPassword,
       "wfPppLineLQProtocol": wfPppLineLQProtocol,
       "wfPppLineDisableRemoteLQRTimer": wfPppLineDisableRemoteLQRTimer,
       "wfPppLineCfgLQRRptPrd": wfPppLineCfgLQRRptPrd,
       "wfPppLineLQRRptPrd": wfPppLineLQRRptPrd,
       "wfPppLineCfgInboundQuality": wfPppLineCfgInboundQuality,
       "wfPppLineInboundQuality": wfPppLineInboundQuality,
       "wfPppLineCfgOutboundQuality": wfPppLineCfgOutboundQuality,
       "wfPppLineOutboundQuality": wfPppLineOutboundQuality,
       "wfPppLineOutLQRs": wfPppLineOutLQRs,
       "wfPppLineInLQRs": wfPppLineInLQRs,
       "wfPppLineChapSecret": wfPppLineChapSecret,
       "wfPppLinePapFallbackDisable": wfPppLinePapFallbackDisable,
       "wfPppLineChapLocalName": wfPppLineChapLocalName,
       "wfPppLineChapRemoteName": wfPppLineChapRemoteName,
       "wfPppLineChapPeriodicTimer": wfPppLineChapPeriodicTimer,
       "wfPppLineBadPackets": wfPppLineBadPackets,
       "wfPppLineLastBadPacket": wfPppLineLastBadPacket,
       "wfPppLineLevelPktsIn": wfPppLineLevelPktsIn,
       "wfPppLineAllowPapReject": wfPppLineAllowPapReject,
       "wfPppLineActiveCct": wfPppLineActiveCct,
       "wfPppLineCfgAsyncMap": wfPppLineCfgAsyncMap,
       "wfPppLineActualAsyncMap": wfPppLineActualAsyncMap,
       "wfPppLineAuthTimer": wfPppLineAuthTimer,
       "wfPppLineConvergenceTimer": wfPppLineConvergenceTimer,
       "wfPppLineMagicNumDisable": wfPppLineMagicNumDisable,
       "wfPppLineMyLinkDiscr": wfPppLineMyLinkDiscr,
       "wfPppLinePeerLinkDiscr": wfPppLinePeerLinkDiscr,
       "wfPppLineCfgMru": wfPppLineCfgMru,
       "wfPppLineRfc1661Compliance": wfPppLineRfc1661Compliance,
       "wfPppLineLqmCurrentState": wfPppLineLqmCurrentState,
       "wfPppCircuitTable": wfPppCircuitTable,
       "wfPppCircuitEntry": wfPppCircuitEntry,
       "wfPppCircuitDelete": wfPppCircuitDelete,
       "wfPppCircuitState": wfPppCircuitState,
       "wfPppCircuitIpcpCurrentState": wfPppCircuitIpcpCurrentState,
       "wfPppCircuitOsinlcpCurrentState": wfPppCircuitOsinlcpCurrentState,
       "wfPppCircuitXnscpCurrentState": wfPppCircuitXnscpCurrentState,
       "wfPppCircuitDncpCurrentState": wfPppCircuitDncpCurrentState,
       "wfPppCircuitAtcpCurrentState": wfPppCircuitAtcpCurrentState,
       "wfPppCircuitIpxcpCurrentState": wfPppCircuitIpxcpCurrentState,
       "wfPppCircuitBncpCurrentState": wfPppCircuitBncpCurrentState,
       "wfPppCircuitVncpCurrentState": wfPppCircuitVncpCurrentState,
       "wfPppCircuitID": wfPppCircuitID,
       "wfPppCircuitIpDisable": wfPppCircuitIpDisable,
       "wfPppCircuitOsinlDisable": wfPppCircuitOsinlDisable,
       "wfPppCircuitXnsDisable": wfPppCircuitXnsDisable,
       "wfPppCircuitDecnetDisable": wfPppCircuitDecnetDisable,
       "wfPppCircuitAppletalkDisable": wfPppCircuitAppletalkDisable,
       "wfPppCircuitIpxDisable": wfPppCircuitIpxDisable,
       "wfPppCircuitBridgeDisable": wfPppCircuitBridgeDisable,
       "wfPppCircuitVinesDisable": wfPppCircuitVinesDisable,
       "wfPppCircuitCfgLocalIpAddr": wfPppCircuitCfgLocalIpAddr,
       "wfPppCircuitLocalIpAddr": wfPppCircuitLocalIpAddr,
       "wfPppCircuitCfgRemoteIpAddr": wfPppCircuitCfgRemoteIpAddr,
       "wfPppCircuitRemoteIpAddr": wfPppCircuitRemoteIpAddr,
       "wfPppCircuitCfgIpxNetworkNumber": wfPppCircuitCfgIpxNetworkNumber,
       "wfPppCircuitIpxNetworkNumber": wfPppCircuitIpxNetworkNumber,
       "wfPppCircuitIpxRemoteNodeNumber": wfPppCircuitIpxRemoteNodeNumber,
       "wfPppCircuitCfgIpxRoutingProtocol": wfPppCircuitCfgIpxRoutingProtocol,
       "wfPppCircuitIpxRoutingProtocol": wfPppCircuitIpxRoutingProtocol,
       "wfPppCircuitLocalIpxRouterName": wfPppCircuitLocalIpxRouterName,
       "wfPppCircuitRemoteIpxRouterName": wfPppCircuitRemoteIpxRouterName,
       "wfPppCircuitIpxConfigComplete": wfPppCircuitIpxConfigComplete,
       "wfPppCircuitCfgAtNetwork": wfPppCircuitCfgAtNetwork,
       "wfPppCircuitAtNetwork": wfPppCircuitAtNetwork,
       "wfPppCircuitCfgLocalAtNode": wfPppCircuitCfgLocalAtNode,
       "wfPppCircuitLocalAtNode": wfPppCircuitLocalAtNode,
       "wfPppCircuitCfgRemoteAtNode": wfPppCircuitCfgRemoteAtNode,
       "wfPppCircuitRemoteAtNode": wfPppCircuitRemoteAtNode,
       "wfPppCircuitCfgAtRoutingProtocol": wfPppCircuitCfgAtRoutingProtocol,
       "wfPppCircuitAtRoutingProtocol": wfPppCircuitAtRoutingProtocol,
       "wfPppCircuitCfgBridgeEnet": wfPppCircuitCfgBridgeEnet,
       "wfPppCircuitBridgeEnet": wfPppCircuitBridgeEnet,
       "wfPppCircuitCfgBridgeFddi": wfPppCircuitCfgBridgeFddi,
       "wfPppCircuitBridgeFddi": wfPppCircuitBridgeFddi,
       "wfPppCircuitCfgBridgeTokenRing": wfPppCircuitCfgBridgeTokenRing,
       "wfPppCircuitBridgeTokenRing": wfPppCircuitBridgeTokenRing,
       "wfPppCircuitBadPackets": wfPppCircuitBadPackets,
       "wfPppCircuitLastBadPacket": wfPppCircuitLastBadPacket,
       "wfPppCircuitCcpCurrentState": wfPppCircuitCcpCurrentState,
       "wfPppCircuitCcpDisable": wfPppCircuitCcpDisable,
       "wfPppCircuitPppMode": wfPppCircuitPppMode,
       "wfPppCircuitMLFragPerm": wfPppCircuitMLFragPerm,
       "wfPppCircuitExamPeriod": wfPppCircuitExamPeriod,
       "wfPppCircuitFullThreshold": wfPppCircuitFullThreshold,
       "wfPppCircuitPeriodsCng": wfPppCircuitPeriodsCng,
       "wfPppCircuitPrefBwSlot": wfPppCircuitPrefBwSlot,
       "wfPppCircuitResvBwSlot": wfPppCircuitResvBwSlot,
       "wfPppCircuitMLFragTriggerSize": wfPppCircuitMLFragTriggerSize,
       "wfPppCircuitMaxLinks": wfPppCircuitMaxLinks,
       "wfPppCircuitRecoverThreshold": wfPppCircuitRecoverThreshold,
       "wfPppCircuitPeriodsUnCng": wfPppCircuitPeriodsUnCng,
       "wfPppCircuitHistory": wfPppCircuitHistory,
       "wfPppCircuitDebugFlag": wfPppCircuitDebugFlag,
       "wfPppCircuitActualMode": wfPppCircuitActualMode,
       "wfPppCircuitMaxBuffers": wfPppCircuitMaxBuffers,
       "wfPppCircuitLinksConfigured": wfPppCircuitLinksConfigured,
       "wfPppCircuitBacpDisable": wfPppCircuitBacpDisable,
       "wfPppCircuitBacpCurrentState": wfPppCircuitBacpCurrentState,
       "wfPppCircuitBacpNoPhoneNum": wfPppCircuitBacpNoPhoneNum,
       "wfPppCircuitIpv6Disable": wfPppCircuitIpv6Disable,
       "wfPppCircuitIpv6CurrentState": wfPppCircuitIpv6CurrentState,
       "wfPppCircuitCcpType": wfPppCircuitCcpType,
       "wfPppCircuitCfgCcpOptions": wfPppCircuitCfgCcpOptions,
       "wfPppCircuitCcpOptions": wfPppCircuitCcpOptions,
       "wfPppCircuitStacLZSCheckMode": wfPppCircuitStacLZSCheckMode,
       "wfPppCircuitMLFragStrict": wfPppCircuitMLFragStrict,
       "wfPppCircuitLampreyCompDisable": wfPppCircuitLampreyCompDisable,
       "wfPppCircuitMsgLevel": wfPppCircuitMsgLevel,
       "wfPppCircuitType": wfPppCircuitType,
       "wfPppCircuitWRCompatability": wfPppCircuitWRCompatability,
       "wfPppWhoamiTable": wfPppWhoamiTable,
       "wfPppWhoamiEntry": wfPppWhoamiEntry,
       "wfPppWhoamiDelete": wfPppWhoamiDelete,
       "wfPppWhoamiName": wfPppWhoamiName,
       "wfPppWhoamiCircuit": wfPppWhoamiCircuit,
       "wfPppWhoamiSecret": wfPppWhoamiSecret,
       "wfPppWhoamiPapPassword": wfPppWhoamiPapPassword,
       "wfPppWhoamiCctGrp": wfPppWhoamiCctGrp,
       "wfPppMlStatsTable": wfPppMlStatsTable,
       "wfPppMlStatsEntry": wfPppMlStatsEntry,
       "wfPppMlStatsDelete": wfPppMlStatsDelete,
       "wfPppMlStatsCircuitID": wfPppMlStatsCircuitID,
       "wfPppMlStatsHomeSlot": wfPppMlStatsHomeSlot,
       "wfPppMlStatsLineCnt": wfPppMlStatsLineCnt,
       "wfPppMlStatsBundleSpd": wfPppMlStatsBundleSpd,
       "wfPppMlStatsMrru": wfPppMlStatsMrru,
       "wfPppMlStatsEndptDisc": wfPppMlStatsEndptDisc,
       "wfPppMlStatsTxOctets": wfPppMlStatsTxOctets,
       "wfPppMlStatsTxPkts": wfPppMlStatsTxPkts,
       "wfPppMlStatsAvgTxListLen": wfPppMlStatsAvgTxListLen,
       "wfPppMlStatsRxOctets": wfPppMlStatsRxOctets,
       "wfPppMlStatsRxPkts": wfPppMlStatsRxPkts,
       "wfPppMlStatsReasmFails": wfPppMlStatsReasmFails,
       "wfPppMlStatsSeqNumberLost": wfPppMlStatsSeqNumberLost,
       "wfPppMlStatsSeqNumberArrivedLate": wfPppMlStatsSeqNumberArrivedLate,
       "wfPppMlStatsReSeqBufferCnt": wfPppMlStatsReSeqBufferCnt,
       "wfPppMlStatsReSeqBufferMax": wfPppMlStatsReSeqBufferMax,
       "wfPppMlStatsExceededBufferMax": wfPppMlStatsExceededBufferMax,
       "wfPppMlStatsLinkIdleEvents": wfPppMlStatsLinkIdleEvents,
       "wfPppMlStatsCalcPercent": wfPppMlStatsCalcPercent,
       "wfPppMlStatsDebug": wfPppMlStatsDebug,
       "wfPppMlStatsReassmBufferCnt": wfPppMlStatsReassmBufferCnt,
       "wfPppMlStatsReassmBufferMax": wfPppMlStatsReassmBufferMax,
       "wfPppMlStatsNumPktsFragmented": wfPppMlStatsNumPktsFragmented,
       "wfPppMlStatsPQHiXmits": wfPppMlStatsPQHiXmits,
       "wfPppMlStatsPQNormalXmits": wfPppMlStatsPQNormalXmits,
       "wfPppMlStatsPQLoXmits": wfPppMlStatsPQLoXmits,
       "wfPppMlStatsPQHiClippedPkts": wfPppMlStatsPQHiClippedPkts,
       "wfPppMlStatsPQNormalClippedPkts": wfPppMlStatsPQNormalClippedPkts,
       "wfPppMlStatsPQLoClippedPkts": wfPppMlStatsPQLoClippedPkts,
       "wfPppMlStatsPQIntrQHighWaterPkts": wfPppMlStatsPQIntrQHighWaterPkts,
       "wfPppMlStatsPQHiQHighWaterPkts": wfPppMlStatsPQHiQHighWaterPkts,
       "wfPppMlStatsPQNormalQHighWaterPkts": wfPppMlStatsPQNormalQHighWaterPkts,
       "wfPppMlStatsPQLoQHighWaterPkts": wfPppMlStatsPQLoQHighWaterPkts,
       "wfPppMlStatsPQHighWaterPktsClear": wfPppMlStatsPQHighWaterPktsClear,
       "wfPppMlStatsPQDroppedPkts": wfPppMlStatsPQDroppedPkts,
       "wfPppMlStatsPQLargePkts": wfPppMlStatsPQLargePkts,
       "wfPppMlStatsPQHiTotalOctets": wfPppMlStatsPQHiTotalOctets,
       "wfPppMlStatsPQNormalTotalOctets": wfPppMlStatsPQNormalTotalOctets,
       "wfPppMlStatsPQLoTotalOctets": wfPppMlStatsPQLoTotalOctets,
       "wfPppMlStatsPQPktsNotQueued": wfPppMlStatsPQPktsNotQueued,
       "wfPppBapStatsTable": wfPppBapStatsTable,
       "wfPppBapStatsEntry": wfPppBapStatsEntry,
       "wfPppBapStatsDelete": wfPppBapStatsDelete,
       "wfPppBapStatsCircuitID": wfPppBapStatsCircuitID,
       "wfPppBapCallReqTx": wfPppBapCallReqTx,
       "wfPppBapCallRespAckTx": wfPppBapCallRespAckTx,
       "wfPppBapCallRespNakTx": wfPppBapCallRespNakTx,
       "wfPppBapCallRespFullNakTx": wfPppBapCallRespFullNakTx,
       "wfPppBapCallRespRejTx": wfPppBapCallRespRejTx,
       "wfPppBapCallbackReqTx": wfPppBapCallbackReqTx,
       "wfPppBapCallbackRespAckTx": wfPppBapCallbackRespAckTx,
       "wfPppBapCallbackRespNakTx": wfPppBapCallbackRespNakTx,
       "wfPppBapCallbackRespFullNakTx": wfPppBapCallbackRespFullNakTx,
       "wfPppBapCallbackRespRejTx": wfPppBapCallbackRespRejTx,
       "wfPppBapLdQueryReqTx": wfPppBapLdQueryReqTx,
       "wfPppBapLdQueryRespAckTx": wfPppBapLdQueryRespAckTx,
       "wfPppBapLdQueryRespNakTx": wfPppBapLdQueryRespNakTx,
       "wfPppBapLdQueryRespFullNakTx": wfPppBapLdQueryRespFullNakTx,
       "wfPppBapCallStatusIndFailTx": wfPppBapCallStatusIndFailTx,
       "wfPppBapCallStatusIndSuccessTx": wfPppBapCallStatusIndSuccessTx,
       "wfPppBapCallStatusRespTx": wfPppBapCallStatusRespTx,
       "wfPppBapCallReqRx": wfPppBapCallReqRx,
       "wfPppBapCallRespAckRx": wfPppBapCallRespAckRx,
       "wfPppBapCallRespNakRx": wfPppBapCallRespNakRx,
       "wfPppBapCallRespFullNakRx": wfPppBapCallRespFullNakRx,
       "wfPppBapCallRespRejRx": wfPppBapCallRespRejRx,
       "wfPppBapCallbackReqRx": wfPppBapCallbackReqRx,
       "wfPppBapCallbackRespAckRx": wfPppBapCallbackRespAckRx,
       "wfPppBapCallbackRespNakRx": wfPppBapCallbackRespNakRx,
       "wfPppBapCallbackRespFullNakRx": wfPppBapCallbackRespFullNakRx,
       "wfPppBapCallbackRespRejRx": wfPppBapCallbackRespRejRx,
       "wfPppBapLdQueryReqRx": wfPppBapLdQueryReqRx,
       "wfPppBapLdQueryRespAckRx": wfPppBapLdQueryRespAckRx,
       "wfPppBapLdQueryRespNakRx": wfPppBapLdQueryRespNakRx,
       "wfPppBapLdQueryRespFullNakRx": wfPppBapLdQueryRespFullNakRx,
       "wfPppBapCallStatusIndFailRx": wfPppBapCallStatusIndFailRx,
       "wfPppBapCallStatusIndSuccessRx": wfPppBapCallStatusIndSuccessRx,
       "wfPppBapCallStatusRespRx": wfPppBapCallStatusRespRx,
       "wfPppBapCallReqRespDiscardRx": wfPppBapCallReqRespDiscardRx,
       "wfPppBapCallbackReqRespDiscardRx": wfPppBapCallbackReqRespDiscardRx}
)
