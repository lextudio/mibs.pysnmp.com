# SNMP MIB module (Wellfleet-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:57 2024
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

(wfRadiusGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfRadiusGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRadiusTable_Object = MibTable
wfRadiusTable = _WfRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1)
)
if mibBuilder.loadTexts:
    wfRadiusTable.setStatus("mandatory")
_WfRadiusEntry_Object = MibTableRow
wfRadiusEntry = _WfRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1)
)
wfRadiusEntry.setIndexNames(
    (0, "Wellfleet-RADIUS-MIB", "wfRadiusSlot"),
)
if mibBuilder.loadTexts:
    wfRadiusEntry.setStatus("mandatory")


class _WfRadiusDelete_Type(Integer32):
    """Custom type wfRadiusDelete based on Integer32"""
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


_WfRadiusDelete_Type.__name__ = "Integer32"
_WfRadiusDelete_Object = MibTableColumn
wfRadiusDelete = _WfRadiusDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 1),
    _WfRadiusDelete_Type()
)
wfRadiusDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusDelete.setStatus("mandatory")


class _WfRadiusAuthDisable_Type(Integer32):
    """Custom type wfRadiusAuthDisable based on Integer32"""
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


_WfRadiusAuthDisable_Type.__name__ = "Integer32"
_WfRadiusAuthDisable_Object = MibTableColumn
wfRadiusAuthDisable = _WfRadiusAuthDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 2),
    _WfRadiusAuthDisable_Type()
)
wfRadiusAuthDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusAuthDisable.setStatus("mandatory")


class _WfRadiusAcctDisable_Type(Integer32):
    """Custom type wfRadiusAcctDisable based on Integer32"""
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


_WfRadiusAcctDisable_Type.__name__ = "Integer32"
_WfRadiusAcctDisable_Object = MibTableColumn
wfRadiusAcctDisable = _WfRadiusAcctDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 3),
    _WfRadiusAcctDisable_Type()
)
wfRadiusAcctDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusAcctDisable.setStatus("mandatory")
_WfRadiusSlot_Type = Integer32
_WfRadiusSlot_Object = MibTableColumn
wfRadiusSlot = _WfRadiusSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 4),
    _WfRadiusSlot_Type()
)
wfRadiusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusSlot.setStatus("mandatory")
_WfRadiusClientIpAddress_Type = IpAddress
_WfRadiusClientIpAddress_Object = MibTableColumn
wfRadiusClientIpAddress = _WfRadiusClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 5),
    _WfRadiusClientIpAddress_Type()
)
wfRadiusClientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusClientIpAddress.setStatus("mandatory")


class _WfRadiusAcctDirection_Type(Integer32):
    """Custom type wfRadiusAcctDirection based on Integer32"""
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
          ("incoming", 2),
          ("outgoing", 3))
    )


_WfRadiusAcctDirection_Type.__name__ = "Integer32"
_WfRadiusAcctDirection_Object = MibTableColumn
wfRadiusAcctDirection = _WfRadiusAcctDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 6),
    _WfRadiusAcctDirection_Type()
)
wfRadiusAcctDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusAcctDirection.setStatus("mandatory")


class _WfRadiusDebugMsgLevel_Type(Integer32):
    """Custom type wfRadiusDebugMsgLevel based on Integer32"""
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
        *(("nodebug", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfRadiusDebugMsgLevel_Type.__name__ = "Integer32"
_WfRadiusDebugMsgLevel_Object = MibTableColumn
wfRadiusDebugMsgLevel = _WfRadiusDebugMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 7),
    _WfRadiusDebugMsgLevel_Type()
)
wfRadiusDebugMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusDebugMsgLevel.setStatus("mandatory")


class _WfRadiusCfgMask_Type(Integer32):
    """Custom type wfRadiusCfgMask based on Integer32"""
    defaultValue = 0


_WfRadiusCfgMask_Object = MibTableColumn
wfRadiusCfgMask = _WfRadiusCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 8),
    _WfRadiusCfgMask_Type()
)
wfRadiusCfgMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusCfgMask.setStatus("mandatory")
_WfRadiusServerTable_Object = MibTable
wfRadiusServerTable = _WfRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2)
)
if mibBuilder.loadTexts:
    wfRadiusServerTable.setStatus("mandatory")
_WfRadiusServerEntry_Object = MibTableRow
wfRadiusServerEntry = _WfRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1)
)
wfRadiusServerEntry.setIndexNames(
    (0, "Wellfleet-RADIUS-MIB", "wfRadiusServerIpAddress"),
)
if mibBuilder.loadTexts:
    wfRadiusServerEntry.setStatus("mandatory")


class _WfRadiusServerDelete_Type(Integer32):
    """Custom type wfRadiusServerDelete based on Integer32"""
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


_WfRadiusServerDelete_Type.__name__ = "Integer32"
_WfRadiusServerDelete_Object = MibTableColumn
wfRadiusServerDelete = _WfRadiusServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 1),
    _WfRadiusServerDelete_Type()
)
wfRadiusServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerDelete.setStatus("mandatory")


class _WfRadiusServerDisable_Type(Integer32):
    """Custom type wfRadiusServerDisable based on Integer32"""
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


_WfRadiusServerDisable_Type.__name__ = "Integer32"
_WfRadiusServerDisable_Object = MibTableColumn
wfRadiusServerDisable = _WfRadiusServerDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 2),
    _WfRadiusServerDisable_Type()
)
wfRadiusServerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerDisable.setStatus("mandatory")
_WfRadiusServerIpAddress_Type = IpAddress
_WfRadiusServerIpAddress_Object = MibTableColumn
wfRadiusServerIpAddress = _WfRadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 3),
    _WfRadiusServerIpAddress_Type()
)
wfRadiusServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusServerIpAddress.setStatus("mandatory")


class _WfRadiusServerMode_Type(Integer32):
    """Custom type wfRadiusServerMode based on Integer32"""
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
        *(("acctonly", 2),
          ("authonly", 1),
          ("both", 3))
    )


_WfRadiusServerMode_Type.__name__ = "Integer32"
_WfRadiusServerMode_Object = MibTableColumn
wfRadiusServerMode = _WfRadiusServerMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 4),
    _WfRadiusServerMode_Type()
)
wfRadiusServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerMode.setStatus("mandatory")


class _WfRadiusServerAuthState_Type(Integer32):
    """Custom type wfRadiusServerAuthState based on Integer32"""
    defaultValue = 1

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


_WfRadiusServerAuthState_Type.__name__ = "Integer32"
_WfRadiusServerAuthState_Object = MibTableColumn
wfRadiusServerAuthState = _WfRadiusServerAuthState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 5),
    _WfRadiusServerAuthState_Type()
)
wfRadiusServerAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusServerAuthState.setStatus("mandatory")


class _WfRadiusServerAuthUdpPort_Type(Integer32):
    """Custom type wfRadiusServerAuthUdpPort based on Integer32"""
    defaultValue = 1645


_WfRadiusServerAuthUdpPort_Object = MibTableColumn
wfRadiusServerAuthUdpPort = _WfRadiusServerAuthUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 6),
    _WfRadiusServerAuthUdpPort_Type()
)
wfRadiusServerAuthUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerAuthUdpPort.setStatus("mandatory")


class _WfRadiusServerAuthType_Type(Integer32):
    """Custom type wfRadiusServerAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("primary", 1))
    )


_WfRadiusServerAuthType_Type.__name__ = "Integer32"
_WfRadiusServerAuthType_Object = MibTableColumn
wfRadiusServerAuthType = _WfRadiusServerAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 7),
    _WfRadiusServerAuthType_Type()
)
wfRadiusServerAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerAuthType.setStatus("mandatory")


class _WfRadiusServerAcctState_Type(Integer32):
    """Custom type wfRadiusServerAcctState based on Integer32"""
    defaultValue = 1

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


_WfRadiusServerAcctState_Type.__name__ = "Integer32"
_WfRadiusServerAcctState_Object = MibTableColumn
wfRadiusServerAcctState = _WfRadiusServerAcctState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 8),
    _WfRadiusServerAcctState_Type()
)
wfRadiusServerAcctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusServerAcctState.setStatus("mandatory")


class _WfRadiusServerAcctUdpPort_Type(Integer32):
    """Custom type wfRadiusServerAcctUdpPort based on Integer32"""
    defaultValue = 1646


_WfRadiusServerAcctUdpPort_Object = MibTableColumn
wfRadiusServerAcctUdpPort = _WfRadiusServerAcctUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 9),
    _WfRadiusServerAcctUdpPort_Type()
)
wfRadiusServerAcctUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerAcctUdpPort.setStatus("mandatory")


class _WfRadiusServerAcctType_Type(Integer32):
    """Custom type wfRadiusServerAcctType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("primary", 1))
    )


_WfRadiusServerAcctType_Type.__name__ = "Integer32"
_WfRadiusServerAcctType_Object = MibTableColumn
wfRadiusServerAcctType = _WfRadiusServerAcctType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 10),
    _WfRadiusServerAcctType_Type()
)
wfRadiusServerAcctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerAcctType.setStatus("mandatory")
_WfRadiusPrimarySecret_Type = DisplayString
_WfRadiusPrimarySecret_Object = MibTableColumn
wfRadiusPrimarySecret = _WfRadiusPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 11),
    _WfRadiusPrimarySecret_Type()
)
wfRadiusPrimarySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusPrimarySecret.setStatus("mandatory")


class _WfRadiusServerResponseTimeout_Type(Integer32):
    """Custom type wfRadiusServerResponseTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfRadiusServerResponseTimeout_Type.__name__ = "Integer32"
_WfRadiusServerResponseTimeout_Object = MibTableColumn
wfRadiusServerResponseTimeout = _WfRadiusServerResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 12),
    _WfRadiusServerResponseTimeout_Type()
)
wfRadiusServerResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerResponseTimeout.setStatus("mandatory")


class _WfRadiusServerRetryMax_Type(Integer32):
    """Custom type wfRadiusServerRetryMax based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfRadiusServerRetryMax_Type.__name__ = "Integer32"
_WfRadiusServerRetryMax_Object = MibTableColumn
wfRadiusServerRetryMax = _WfRadiusServerRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 13),
    _WfRadiusServerRetryMax_Type()
)
wfRadiusServerRetryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerRetryMax.setStatus("mandatory")


class _WfRadiusServerResetTimer_Type(Integer32):
    """Custom type wfRadiusServerResetTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfRadiusServerResetTimer_Type.__name__ = "Integer32"
_WfRadiusServerResetTimer_Object = MibTableColumn
wfRadiusServerResetTimer = _WfRadiusServerResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 14),
    _WfRadiusServerResetTimer_Type()
)
wfRadiusServerResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerResetTimer.setStatus("mandatory")


class _WfRadiusServerAutomaticReset_Type(Integer32):
    """Custom type wfRadiusServerAutomaticReset based on Integer32"""
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


_WfRadiusServerAutomaticReset_Type.__name__ = "Integer32"
_WfRadiusServerAutomaticReset_Object = MibTableColumn
wfRadiusServerAutomaticReset = _WfRadiusServerAutomaticReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 15),
    _WfRadiusServerAutomaticReset_Type()
)
wfRadiusServerAutomaticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRadiusServerAutomaticReset.setStatus("mandatory")
_WfRadiusStatsTable_Object = MibTable
wfRadiusStatsTable = _WfRadiusStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3)
)
if mibBuilder.loadTexts:
    wfRadiusStatsTable.setStatus("mandatory")
_WfRadiusStatsEntry_Object = MibTableRow
wfRadiusStatsEntry = _WfRadiusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1)
)
wfRadiusStatsEntry.setIndexNames(
    (0, "Wellfleet-RADIUS-MIB", "wfRadiusStatsSlot"),
    (0, "Wellfleet-RADIUS-MIB", "wfRadiusStatsIpAddress"),
)
if mibBuilder.loadTexts:
    wfRadiusStatsEntry.setStatus("mandatory")
_WfRadiusStatsIpAddress_Type = IpAddress
_WfRadiusStatsIpAddress_Object = MibTableColumn
wfRadiusStatsIpAddress = _WfRadiusStatsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 1),
    _WfRadiusStatsIpAddress_Type()
)
wfRadiusStatsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsIpAddress.setStatus("mandatory")
_WfRadiusStatsSlot_Type = Integer32
_WfRadiusStatsSlot_Object = MibTableColumn
wfRadiusStatsSlot = _WfRadiusStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 2),
    _WfRadiusStatsSlot_Type()
)
wfRadiusStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsSlot.setStatus("mandatory")
_WfRadiusStatsAuthReqCount_Type = Integer32
_WfRadiusStatsAuthReqCount_Object = MibTableColumn
wfRadiusStatsAuthReqCount = _WfRadiusStatsAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 3),
    _WfRadiusStatsAuthReqCount_Type()
)
wfRadiusStatsAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthReqCount.setStatus("mandatory")
_WfRadiusStatsAuthReqOutstanding_Type = Integer32
_WfRadiusStatsAuthReqOutstanding_Object = MibTableColumn
wfRadiusStatsAuthReqOutstanding = _WfRadiusStatsAuthReqOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 4),
    _WfRadiusStatsAuthReqOutstanding_Type()
)
wfRadiusStatsAuthReqOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthReqOutstanding.setStatus("mandatory")
_WfRadiusStatsAuthRespSucc_Type = Integer32
_WfRadiusStatsAuthRespSucc_Object = MibTableColumn
wfRadiusStatsAuthRespSucc = _WfRadiusStatsAuthRespSucc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 5),
    _WfRadiusStatsAuthRespSucc_Type()
)
wfRadiusStatsAuthRespSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthRespSucc.setStatus("mandatory")
_WfRadiusStatsAuthRespFail_Type = Integer32
_WfRadiusStatsAuthRespFail_Object = MibTableColumn
wfRadiusStatsAuthRespFail = _WfRadiusStatsAuthRespFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 6),
    _WfRadiusStatsAuthRespFail_Type()
)
wfRadiusStatsAuthRespFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthRespFail.setStatus("mandatory")
_WfRadiusStatsAuthNoResp_Type = Integer32
_WfRadiusStatsAuthNoResp_Object = MibTableColumn
wfRadiusStatsAuthNoResp = _WfRadiusStatsAuthNoResp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 7),
    _WfRadiusStatsAuthNoResp_Type()
)
wfRadiusStatsAuthNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthNoResp.setStatus("mandatory")
_WfRadiusStatsAuthRespInvalid_Type = Integer32
_WfRadiusStatsAuthRespInvalid_Object = MibTableColumn
wfRadiusStatsAuthRespInvalid = _WfRadiusStatsAuthRespInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 8),
    _WfRadiusStatsAuthRespInvalid_Type()
)
wfRadiusStatsAuthRespInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthRespInvalid.setStatus("mandatory")
_WfRadiusStatsAuthRespTimeouts_Type = Integer32
_WfRadiusStatsAuthRespTimeouts_Object = MibTableColumn
wfRadiusStatsAuthRespTimeouts = _WfRadiusStatsAuthRespTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 9),
    _WfRadiusStatsAuthRespTimeouts_Type()
)
wfRadiusStatsAuthRespTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthRespTimeouts.setStatus("mandatory")
_WfRadiusStatsAuthAltServerRetries_Type = Integer32
_WfRadiusStatsAuthAltServerRetries_Object = MibTableColumn
wfRadiusStatsAuthAltServerRetries = _WfRadiusStatsAuthAltServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 10),
    _WfRadiusStatsAuthAltServerRetries_Type()
)
wfRadiusStatsAuthAltServerRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAuthAltServerRetries.setStatus("mandatory")
_WfRadiusStatsAcctReqStart_Type = Counter32
_WfRadiusStatsAcctReqStart_Object = MibTableColumn
wfRadiusStatsAcctReqStart = _WfRadiusStatsAcctReqStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 11),
    _WfRadiusStatsAcctReqStart_Type()
)
wfRadiusStatsAcctReqStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctReqStart.setStatus("mandatory")
_WfRadiusStatsAcctReqStop_Type = Counter32
_WfRadiusStatsAcctReqStop_Object = MibTableColumn
wfRadiusStatsAcctReqStop = _WfRadiusStatsAcctReqStop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 12),
    _WfRadiusStatsAcctReqStop_Type()
)
wfRadiusStatsAcctReqStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctReqStop.setStatus("mandatory")
_WfRadiusStatsAcctRespTimeouts_Type = Counter32
_WfRadiusStatsAcctRespTimeouts_Object = MibTableColumn
wfRadiusStatsAcctRespTimeouts = _WfRadiusStatsAcctRespTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 13),
    _WfRadiusStatsAcctRespTimeouts_Type()
)
wfRadiusStatsAcctRespTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctRespTimeouts.setStatus("mandatory")
_WfRadiusStatsAcctRespFailed_Type = Counter32
_WfRadiusStatsAcctRespFailed_Object = MibTableColumn
wfRadiusStatsAcctRespFailed = _WfRadiusStatsAcctRespFailed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 14),
    _WfRadiusStatsAcctRespFailed_Type()
)
wfRadiusStatsAcctRespFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctRespFailed.setStatus("mandatory")
_WfRadiusStatsAcctAltServerRetries_Type = Counter32
_WfRadiusStatsAcctAltServerRetries_Object = MibTableColumn
wfRadiusStatsAcctAltServerRetries = _WfRadiusStatsAcctAltServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 15),
    _WfRadiusStatsAcctAltServerRetries_Type()
)
wfRadiusStatsAcctAltServerRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctAltServerRetries.setStatus("mandatory")
_WfRadiusStatsAcctResponse_Type = Counter32
_WfRadiusStatsAcctResponse_Object = MibTableColumn
wfRadiusStatsAcctResponse = _WfRadiusStatsAcctResponse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 16),
    _WfRadiusStatsAcctResponse_Type()
)
wfRadiusStatsAcctResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRadiusStatsAcctResponse.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RADIUS-MIB",
    **{"wfRadiusTable": wfRadiusTable,
       "wfRadiusEntry": wfRadiusEntry,
       "wfRadiusDelete": wfRadiusDelete,
       "wfRadiusAuthDisable": wfRadiusAuthDisable,
       "wfRadiusAcctDisable": wfRadiusAcctDisable,
       "wfRadiusSlot": wfRadiusSlot,
       "wfRadiusClientIpAddress": wfRadiusClientIpAddress,
       "wfRadiusAcctDirection": wfRadiusAcctDirection,
       "wfRadiusDebugMsgLevel": wfRadiusDebugMsgLevel,
       "wfRadiusCfgMask": wfRadiusCfgMask,
       "wfRadiusServerTable": wfRadiusServerTable,
       "wfRadiusServerEntry": wfRadiusServerEntry,
       "wfRadiusServerDelete": wfRadiusServerDelete,
       "wfRadiusServerDisable": wfRadiusServerDisable,
       "wfRadiusServerIpAddress": wfRadiusServerIpAddress,
       "wfRadiusServerMode": wfRadiusServerMode,
       "wfRadiusServerAuthState": wfRadiusServerAuthState,
       "wfRadiusServerAuthUdpPort": wfRadiusServerAuthUdpPort,
       "wfRadiusServerAuthType": wfRadiusServerAuthType,
       "wfRadiusServerAcctState": wfRadiusServerAcctState,
       "wfRadiusServerAcctUdpPort": wfRadiusServerAcctUdpPort,
       "wfRadiusServerAcctType": wfRadiusServerAcctType,
       "wfRadiusPrimarySecret": wfRadiusPrimarySecret,
       "wfRadiusServerResponseTimeout": wfRadiusServerResponseTimeout,
       "wfRadiusServerRetryMax": wfRadiusServerRetryMax,
       "wfRadiusServerResetTimer": wfRadiusServerResetTimer,
       "wfRadiusServerAutomaticReset": wfRadiusServerAutomaticReset,
       "wfRadiusStatsTable": wfRadiusStatsTable,
       "wfRadiusStatsEntry": wfRadiusStatsEntry,
       "wfRadiusStatsIpAddress": wfRadiusStatsIpAddress,
       "wfRadiusStatsSlot": wfRadiusStatsSlot,
       "wfRadiusStatsAuthReqCount": wfRadiusStatsAuthReqCount,
       "wfRadiusStatsAuthReqOutstanding": wfRadiusStatsAuthReqOutstanding,
       "wfRadiusStatsAuthRespSucc": wfRadiusStatsAuthRespSucc,
       "wfRadiusStatsAuthRespFail": wfRadiusStatsAuthRespFail,
       "wfRadiusStatsAuthNoResp": wfRadiusStatsAuthNoResp,
       "wfRadiusStatsAuthRespInvalid": wfRadiusStatsAuthRespInvalid,
       "wfRadiusStatsAuthRespTimeouts": wfRadiusStatsAuthRespTimeouts,
       "wfRadiusStatsAuthAltServerRetries": wfRadiusStatsAuthAltServerRetries,
       "wfRadiusStatsAcctReqStart": wfRadiusStatsAcctReqStart,
       "wfRadiusStatsAcctReqStop": wfRadiusStatsAcctReqStop,
       "wfRadiusStatsAcctRespTimeouts": wfRadiusStatsAcctRespTimeouts,
       "wfRadiusStatsAcctRespFailed": wfRadiusStatsAcctRespFailed,
       "wfRadiusStatsAcctAltServerRetries": wfRadiusStatsAcctAltServerRetries,
       "wfRadiusStatsAcctResponse": wfRadiusStatsAcctResponse}
)
