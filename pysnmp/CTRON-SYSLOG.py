# SNMP MIB module (CTRON-SYSLOG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SYSLOG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:47 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_AapsLog_ObjectIdentity = ObjectIdentity
aapsLog = _AapsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9)
)
_LogWindow_ObjectIdentity = ObjectIdentity
logWindow = _LogWindow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1)
)
_LogWindowTable_Object = MibTable
logWindowTable = _LogWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 1)
)
if mibBuilder.loadTexts:
    logWindowTable.setStatus("mandatory")
_LogWindowEntry_Object = MibTableRow
logWindowEntry = _LogWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 1, 1)
)
logWindowEntry.setIndexNames(
    (0, "CTRON-SYSLOG", "ltIndex"),
)
if mibBuilder.loadTexts:
    logWindowEntry.setStatus("mandatory")
_LtIndex_Type = Integer32
_LtIndex_Object = MibTableColumn
ltIndex = _LtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 1, 1, 1),
    _LtIndex_Type()
)
ltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltIndex.setStatus("mandatory")


class _LtLogString_Type(DisplayString):
    """Custom type ltLogString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_LtLogString_Type.__name__ = "DisplayString"
_LtLogString_Object = MibTableColumn
ltLogString = _LtLogString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 1, 1, 2),
    _LtLogString_Type()
)
ltLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltLogString.setStatus("mandatory")


class _LtWindowOperation_Type(Integer32):
    """Custom type ltWindowOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pageDown", 4),
          ("pageUp", 3),
          ("refresh", 2))
    )


_LtWindowOperation_Type.__name__ = "Integer32"
_LtWindowOperation_Object = MibScalar
ltWindowOperation = _LtWindowOperation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 2),
    _LtWindowOperation_Type()
)
ltWindowOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltWindowOperation.setStatus("mandatory")


class _LtWindowReset_Type(Integer32):
    """Custom type ltWindowReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("toLogEnd", 3),
          ("toLogStart", 2))
    )


_LtWindowReset_Type.__name__ = "Integer32"
_LtWindowReset_Object = MibScalar
ltWindowReset = _LtWindowReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 3),
    _LtWindowReset_Type()
)
ltWindowReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltWindowReset.setStatus("mandatory")


class _LtClientMatchString_Type(DisplayString):
    """Custom type ltClientMatchString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LtClientMatchString_Type.__name__ = "DisplayString"
_LtClientMatchString_Object = MibScalar
ltClientMatchString = _LtClientMatchString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 4),
    _LtClientMatchString_Type()
)
ltClientMatchString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltClientMatchString.setStatus("mandatory")


class _LtEventMatchString_Type(DisplayString):
    """Custom type ltEventMatchString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LtEventMatchString_Type.__name__ = "DisplayString"
_LtEventMatchString_Object = MibScalar
ltEventMatchString = _LtEventMatchString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 1, 5),
    _LtEventMatchString_Type()
)
ltEventMatchString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltEventMatchString.setStatus("mandatory")
_ServerConfig_ObjectIdentity = ObjectIdentity
serverConfig = _ServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 2)
)


class _ScAutoFreeze_Type(Integer32):
    """Custom type scAutoFreeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_ScAutoFreeze_Type.__name__ = "Integer32"
_ScAutoFreeze_Object = MibScalar
scAutoFreeze = _ScAutoFreeze_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 2, 1),
    _ScAutoFreeze_Type()
)
scAutoFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scAutoFreeze.setStatus("mandatory")


class _ScAdminStatus_Type(Integer32):
    """Custom type scAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disableLogging", 2),
          ("enableLogging", 3),
          ("reset", 5))
    )


_ScAdminStatus_Type.__name__ = "Integer32"
_ScAdminStatus_Object = MibScalar
scAdminStatus = _ScAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 2, 2),
    _ScAdminStatus_Type()
)
scAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scAdminStatus.setStatus("mandatory")
_ScLastChange_Type = TimeTicks
_ScLastChange_Object = MibScalar
scLastChange = _ScLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 2, 3),
    _ScLastChange_Type()
)
scLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scLastChange.setStatus("mandatory")
_ClientConfigTable_Object = MibTable
clientConfigTable = _ClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3)
)
if mibBuilder.loadTexts:
    clientConfigTable.setStatus("mandatory")
_ClientConfigEntry_Object = MibTableRow
clientConfigEntry = _ClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1)
)
clientConfigEntry.setIndexNames(
    (0, "CTRON-SYSLOG", "ccClientID"),
)
if mibBuilder.loadTexts:
    clientConfigEntry.setStatus("mandatory")
_CcClientID_Type = Integer32
_CcClientID_Object = MibTableColumn
ccClientID = _CcClientID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 1),
    _CcClientID_Type()
)
ccClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccClientID.setStatus("mandatory")


class _CcClientName_Type(DisplayString):
    """Custom type ccClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CcClientName_Type.__name__ = "DisplayString"
_CcClientName_Object = MibTableColumn
ccClientName = _CcClientName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 2),
    _CcClientName_Type()
)
ccClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccClientName.setStatus("mandatory")


class _CcClientPersistent_Type(Integer32):
    """Custom type ccClientPersistent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientPersistent_Type.__name__ = "Integer32"
_CcClientPersistent_Object = MibTableColumn
ccClientPersistent = _CcClientPersistent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 3),
    _CcClientPersistent_Type()
)
ccClientPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientPersistent.setStatus("mandatory")


class _CcClientLogStatus_Type(Integer32):
    """Custom type ccClientLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientLogStatus_Type.__name__ = "Integer32"
_CcClientLogStatus_Object = MibTableColumn
ccClientLogStatus = _CcClientLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 4),
    _CcClientLogStatus_Type()
)
ccClientLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientLogStatus.setStatus("mandatory")


class _CcClientDisplayStatus_Type(Integer32):
    """Custom type ccClientDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientDisplayStatus_Type.__name__ = "Integer32"
_CcClientDisplayStatus_Object = MibTableColumn
ccClientDisplayStatus = _CcClientDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 5),
    _CcClientDisplayStatus_Type()
)
ccClientDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientDisplayStatus.setStatus("mandatory")


class _CcClientFreezeLogStatus_Type(Integer32):
    """Custom type ccClientFreezeLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientFreezeLogStatus_Type.__name__ = "Integer32"
_CcClientFreezeLogStatus_Object = MibTableColumn
ccClientFreezeLogStatus = _CcClientFreezeLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 6),
    _CcClientFreezeLogStatus_Type()
)
ccClientFreezeLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientFreezeLogStatus.setStatus("mandatory")


class _CcClientFreezeDisplayStatus_Type(Integer32):
    """Custom type ccClientFreezeDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientFreezeDisplayStatus_Type.__name__ = "Integer32"
_CcClientFreezeDisplayStatus_Object = MibTableColumn
ccClientFreezeDisplayStatus = _CcClientFreezeDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 7),
    _CcClientFreezeDisplayStatus_Type()
)
ccClientFreezeDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientFreezeDisplayStatus.setStatus("mandatory")


class _CcClientErrorLogStatus_Type(Integer32):
    """Custom type ccClientErrorLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientErrorLogStatus_Type.__name__ = "Integer32"
_CcClientErrorLogStatus_Object = MibTableColumn
ccClientErrorLogStatus = _CcClientErrorLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 8),
    _CcClientErrorLogStatus_Type()
)
ccClientErrorLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientErrorLogStatus.setStatus("mandatory")


class _CcClientErrorDisplayStatus_Type(Integer32):
    """Custom type ccClientErrorDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientErrorDisplayStatus_Type.__name__ = "Integer32"
_CcClientErrorDisplayStatus_Object = MibTableColumn
ccClientErrorDisplayStatus = _CcClientErrorDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 9),
    _CcClientErrorDisplayStatus_Type()
)
ccClientErrorDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientErrorDisplayStatus.setStatus("mandatory")


class _CcClientCriticalLogStatus_Type(Integer32):
    """Custom type ccClientCriticalLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientCriticalLogStatus_Type.__name__ = "Integer32"
_CcClientCriticalLogStatus_Object = MibTableColumn
ccClientCriticalLogStatus = _CcClientCriticalLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 10),
    _CcClientCriticalLogStatus_Type()
)
ccClientCriticalLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientCriticalLogStatus.setStatus("mandatory")


class _CcClientCriticalDisplayStatus_Type(Integer32):
    """Custom type ccClientCriticalDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientCriticalDisplayStatus_Type.__name__ = "Integer32"
_CcClientCriticalDisplayStatus_Object = MibTableColumn
ccClientCriticalDisplayStatus = _CcClientCriticalDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 11),
    _CcClientCriticalDisplayStatus_Type()
)
ccClientCriticalDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientCriticalDisplayStatus.setStatus("mandatory")


class _CcClientStatusLogStatus_Type(Integer32):
    """Custom type ccClientStatusLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientStatusLogStatus_Type.__name__ = "Integer32"
_CcClientStatusLogStatus_Object = MibTableColumn
ccClientStatusLogStatus = _CcClientStatusLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 12),
    _CcClientStatusLogStatus_Type()
)
ccClientStatusLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientStatusLogStatus.setStatus("mandatory")


class _CcClientStatusDisplayStatus_Type(Integer32):
    """Custom type ccClientStatusDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientStatusDisplayStatus_Type.__name__ = "Integer32"
_CcClientStatusDisplayStatus_Object = MibTableColumn
ccClientStatusDisplayStatus = _CcClientStatusDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 13),
    _CcClientStatusDisplayStatus_Type()
)
ccClientStatusDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientStatusDisplayStatus.setStatus("mandatory")


class _CcClientInfoLogStatus_Type(Integer32):
    """Custom type ccClientInfoLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientInfoLogStatus_Type.__name__ = "Integer32"
_CcClientInfoLogStatus_Object = MibTableColumn
ccClientInfoLogStatus = _CcClientInfoLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 14),
    _CcClientInfoLogStatus_Type()
)
ccClientInfoLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientInfoLogStatus.setStatus("mandatory")


class _CcClientInfoDisplayStatus_Type(Integer32):
    """Custom type ccClientInfoDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientInfoDisplayStatus_Type.__name__ = "Integer32"
_CcClientInfoDisplayStatus_Object = MibTableColumn
ccClientInfoDisplayStatus = _CcClientInfoDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 15),
    _CcClientInfoDisplayStatus_Type()
)
ccClientInfoDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientInfoDisplayStatus.setStatus("mandatory")


class _CcClientDebugLogStatus_Type(Integer32):
    """Custom type ccClientDebugLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientDebugLogStatus_Type.__name__ = "Integer32"
_CcClientDebugLogStatus_Object = MibTableColumn
ccClientDebugLogStatus = _CcClientDebugLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 16),
    _CcClientDebugLogStatus_Type()
)
ccClientDebugLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientDebugLogStatus.setStatus("mandatory")


class _CcClientDebugDisplayStatus_Type(Integer32):
    """Custom type ccClientDebugDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CcClientDebugDisplayStatus_Type.__name__ = "Integer32"
_CcClientDebugDisplayStatus_Object = MibTableColumn
ccClientDebugDisplayStatus = _CcClientDebugDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 3, 1, 17),
    _CcClientDebugDisplayStatus_Type()
)
ccClientDebugDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccClientDebugDisplayStatus.setStatus("mandatory")
_RecoveredLogTable_Object = MibTable
recoveredLogTable = _RecoveredLogTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 4)
)
if mibBuilder.loadTexts:
    recoveredLogTable.setStatus("mandatory")
_RecoveredLogTableEntry_Object = MibTableRow
recoveredLogTableEntry = _RecoveredLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 4, 1)
)
recoveredLogTableEntry.setIndexNames(
    (0, "CTRON-SYSLOG", "rlIndex"),
)
if mibBuilder.loadTexts:
    recoveredLogTableEntry.setStatus("mandatory")
_RlIndex_Type = Integer32
_RlIndex_Object = MibTableColumn
rlIndex = _RlIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 4, 1, 1),
    _RlIndex_Type()
)
rlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIndex.setStatus("mandatory")


class _RlLogString_Type(DisplayString):
    """Custom type rlLogString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(200, 200),
    )


_RlLogString_Type.__name__ = "DisplayString"
_RlLogString_Object = MibTableColumn
rlLogString = _RlLogString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 9, 4, 1, 2),
    _RlLogString_Type()
)
rlLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLogString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SYSLOG",
    **{"ctSSA": ctSSA,
       "aapsLog": aapsLog,
       "logWindow": logWindow,
       "logWindowTable": logWindowTable,
       "logWindowEntry": logWindowEntry,
       "ltIndex": ltIndex,
       "ltLogString": ltLogString,
       "ltWindowOperation": ltWindowOperation,
       "ltWindowReset": ltWindowReset,
       "ltClientMatchString": ltClientMatchString,
       "ltEventMatchString": ltEventMatchString,
       "serverConfig": serverConfig,
       "scAutoFreeze": scAutoFreeze,
       "scAdminStatus": scAdminStatus,
       "scLastChange": scLastChange,
       "clientConfigTable": clientConfigTable,
       "clientConfigEntry": clientConfigEntry,
       "ccClientID": ccClientID,
       "ccClientName": ccClientName,
       "ccClientPersistent": ccClientPersistent,
       "ccClientLogStatus": ccClientLogStatus,
       "ccClientDisplayStatus": ccClientDisplayStatus,
       "ccClientFreezeLogStatus": ccClientFreezeLogStatus,
       "ccClientFreezeDisplayStatus": ccClientFreezeDisplayStatus,
       "ccClientErrorLogStatus": ccClientErrorLogStatus,
       "ccClientErrorDisplayStatus": ccClientErrorDisplayStatus,
       "ccClientCriticalLogStatus": ccClientCriticalLogStatus,
       "ccClientCriticalDisplayStatus": ccClientCriticalDisplayStatus,
       "ccClientStatusLogStatus": ccClientStatusLogStatus,
       "ccClientStatusDisplayStatus": ccClientStatusDisplayStatus,
       "ccClientInfoLogStatus": ccClientInfoLogStatus,
       "ccClientInfoDisplayStatus": ccClientInfoDisplayStatus,
       "ccClientDebugLogStatus": ccClientDebugLogStatus,
       "ccClientDebugDisplayStatus": ccClientDebugDisplayStatus,
       "recoveredLogTable": recoveredLogTable,
       "recoveredLogTableEntry": recoveredLogTableEntry,
       "rlIndex": rlIndex,
       "rlLogString": rlLogString}
)
