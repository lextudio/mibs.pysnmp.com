# SNMP MIB module (DLGSRPRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLGSRPRF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:38 2024
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

(dlgPerformanceInfo,) = mibBuilder.importSymbols(
    "DLGC-GLOBAL-REG",
    "dlgPerformanceInfo")

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

_DlgPiSram_ObjectIdentity = ObjectIdentity
dlgPiSram = _DlgPiSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1)
)
_DlgPsStatsEnableMask_Type = Integer32
_DlgPsStatsEnableMask_Object = MibScalar
dlgPsStatsEnableMask = _DlgPsStatsEnableMask_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 1),
    _DlgPsStatsEnableMask_Type()
)
dlgPsStatsEnableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgPsStatsEnableMask.setStatus("mandatory")


class _DlgPsPollingInterval_Type(Integer32):
    """Custom type dlgPsPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgPsPollingInterval_Type.__name__ = "Integer32"
_DlgPsPollingInterval_Object = MibScalar
dlgPsPollingInterval = _DlgPsPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 2),
    _DlgPsPollingInterval_Type()
)
dlgPsPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgPsPollingInterval.setStatus("mandatory")
_DlgPsElapsedTime_Type = Integer32
_DlgPsElapsedTime_Object = MibScalar
dlgPsElapsedTime = _DlgPsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 3),
    _DlgPsElapsedTime_Type()
)
dlgPsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsElapsedTime.setStatus("mandatory")
_DlgPsCurrentStats_ObjectIdentity = ObjectIdentity
dlgPsCurrentStats = _DlgPsCurrentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4)
)
_DlgPsCurrentInterrupts_Type = Counter32
_DlgPsCurrentInterrupts_Object = MibScalar
dlgPsCurrentInterrupts = _DlgPsCurrentInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 1),
    _DlgPsCurrentInterrupts_Type()
)
dlgPsCurrentInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentInterrupts.setStatus("mandatory")
_DlgPsCurrentDrvCommands_Type = Counter32
_DlgPsCurrentDrvCommands_Object = MibScalar
dlgPsCurrentDrvCommands = _DlgPsCurrentDrvCommands_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 2),
    _DlgPsCurrentDrvCommands_Type()
)
dlgPsCurrentDrvCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentDrvCommands.setStatus("mandatory")
_DlgPsCurrentFWCommands_Type = Counter32
_DlgPsCurrentFWCommands_Object = MibScalar
dlgPsCurrentFWCommands = _DlgPsCurrentFWCommands_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 3),
    _DlgPsCurrentFWCommands_Type()
)
dlgPsCurrentFWCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentFWCommands.setStatus("mandatory")
_DlgPsCurrentUnSolEvents_Type = Counter32
_DlgPsCurrentUnSolEvents_Object = MibScalar
dlgPsCurrentUnSolEvents = _DlgPsCurrentUnSolEvents_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 4),
    _DlgPsCurrentUnSolEvents_Type()
)
dlgPsCurrentUnSolEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentUnSolEvents.setStatus("mandatory")
_DlgPsCurrentBytesRead_Type = Counter32
_DlgPsCurrentBytesRead_Object = MibScalar
dlgPsCurrentBytesRead = _DlgPsCurrentBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 5),
    _DlgPsCurrentBytesRead_Type()
)
dlgPsCurrentBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentBytesRead.setStatus("mandatory")
_DlgPsCurrentBytesWritten_Type = Counter32
_DlgPsCurrentBytesWritten_Object = MibScalar
dlgPsCurrentBytesWritten = _DlgPsCurrentBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 6),
    _DlgPsCurrentBytesWritten_Type()
)
dlgPsCurrentBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentBytesWritten.setStatus("mandatory")
_DlgPsCurrentLostMsgToFW_Type = Counter32
_DlgPsCurrentLostMsgToFW_Object = MibScalar
dlgPsCurrentLostMsgToFW = _DlgPsCurrentLostMsgToFW_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 7),
    _DlgPsCurrentLostMsgToFW_Type()
)
dlgPsCurrentLostMsgToFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentLostMsgToFW.setStatus("mandatory")
_DlgPsCurrentLostMsgFromFW_Type = Counter32
_DlgPsCurrentLostMsgFromFW_Object = MibScalar
dlgPsCurrentLostMsgFromFW = _DlgPsCurrentLostMsgFromFW_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 8),
    _DlgPsCurrentLostMsgFromFW_Type()
)
dlgPsCurrentLostMsgFromFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentLostMsgFromFW.setStatus("mandatory")
_DlgPsCurrentFWErrorMsgs_Type = Counter32
_DlgPsCurrentFWErrorMsgs_Object = MibScalar
dlgPsCurrentFWErrorMsgs = _DlgPsCurrentFWErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 9),
    _DlgPsCurrentFWErrorMsgs_Type()
)
dlgPsCurrentFWErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentFWErrorMsgs.setStatus("mandatory")
_DlgPsCurrentDrvErrorMsgs_Type = Counter32
_DlgPsCurrentDrvErrorMsgs_Object = MibScalar
dlgPsCurrentDrvErrorMsgs = _DlgPsCurrentDrvErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 10),
    _DlgPsCurrentDrvErrorMsgs_Type()
)
dlgPsCurrentDrvErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsCurrentDrvErrorMsgs.setStatus("mandatory")
_DlgPsTotalStats_ObjectIdentity = ObjectIdentity
dlgPsTotalStats = _DlgPsTotalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5)
)
_DlgPsTotalInterrupts_Type = Counter32
_DlgPsTotalInterrupts_Object = MibScalar
dlgPsTotalInterrupts = _DlgPsTotalInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 1),
    _DlgPsTotalInterrupts_Type()
)
dlgPsTotalInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalInterrupts.setStatus("mandatory")
_DlgPsTotalDrvCommands_Type = Counter32
_DlgPsTotalDrvCommands_Object = MibScalar
dlgPsTotalDrvCommands = _DlgPsTotalDrvCommands_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 2),
    _DlgPsTotalDrvCommands_Type()
)
dlgPsTotalDrvCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalDrvCommands.setStatus("mandatory")
_DlgPsTotalFWCommands_Type = Counter32
_DlgPsTotalFWCommands_Object = MibScalar
dlgPsTotalFWCommands = _DlgPsTotalFWCommands_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 3),
    _DlgPsTotalFWCommands_Type()
)
dlgPsTotalFWCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalFWCommands.setStatus("mandatory")
_DlgPsTotalUnSolEvents_Type = Counter32
_DlgPsTotalUnSolEvents_Object = MibScalar
dlgPsTotalUnSolEvents = _DlgPsTotalUnSolEvents_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 4),
    _DlgPsTotalUnSolEvents_Type()
)
dlgPsTotalUnSolEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalUnSolEvents.setStatus("mandatory")
_DlgPsTotalBytesRead_Type = Counter32
_DlgPsTotalBytesRead_Object = MibScalar
dlgPsTotalBytesRead = _DlgPsTotalBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 5),
    _DlgPsTotalBytesRead_Type()
)
dlgPsTotalBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalBytesRead.setStatus("mandatory")
_DlgPsTotalBytesWritten_Type = Counter32
_DlgPsTotalBytesWritten_Object = MibScalar
dlgPsTotalBytesWritten = _DlgPsTotalBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 6),
    _DlgPsTotalBytesWritten_Type()
)
dlgPsTotalBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalBytesWritten.setStatus("mandatory")
_DlgPsTotalLostMsgToFW_Type = Counter32
_DlgPsTotalLostMsgToFW_Object = MibScalar
dlgPsTotalLostMsgToFW = _DlgPsTotalLostMsgToFW_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 7),
    _DlgPsTotalLostMsgToFW_Type()
)
dlgPsTotalLostMsgToFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalLostMsgToFW.setStatus("mandatory")
_DlgPsTotalLostMsgFromFW_Type = Counter32
_DlgPsTotalLostMsgFromFW_Object = MibScalar
dlgPsTotalLostMsgFromFW = _DlgPsTotalLostMsgFromFW_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 8),
    _DlgPsTotalLostMsgFromFW_Type()
)
dlgPsTotalLostMsgFromFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalLostMsgFromFW.setStatus("mandatory")
_DlgPsTotalFWErrorMsgs_Type = Counter32
_DlgPsTotalFWErrorMsgs_Object = MibScalar
dlgPsTotalFWErrorMsgs = _DlgPsTotalFWErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 9),
    _DlgPsTotalFWErrorMsgs_Type()
)
dlgPsTotalFWErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalFWErrorMsgs.setStatus("mandatory")
_DlgPsTotalDrvErrorMsgs_Type = Counter32
_DlgPsTotalDrvErrorMsgs_Object = MibScalar
dlgPsTotalDrvErrorMsgs = _DlgPsTotalDrvErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 10),
    _DlgPsTotalDrvErrorMsgs_Type()
)
dlgPsTotalDrvErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPsTotalDrvErrorMsgs.setStatus("mandatory")
_DlgPiSramMibRev_ObjectIdentity = ObjectIdentity
dlgPiSramMibRev = _DlgPiSramMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6)
)


class _DlgPiSramMibRevMajor_Type(Integer32):
    """Custom type dlgPiSramMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlgPiSramMibRevMajor_Type.__name__ = "Integer32"
_DlgPiSramMibRevMajor_Object = MibScalar
dlgPiSramMibRevMajor = _DlgPiSramMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6, 1),
    _DlgPiSramMibRevMajor_Type()
)
dlgPiSramMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPiSramMibRevMajor.setStatus("mandatory")


class _DlgPiSramMibRevMinor_Type(Integer32):
    """Custom type dlgPiSramMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgPiSramMibRevMinor_Type.__name__ = "Integer32"
_DlgPiSramMibRevMinor_Object = MibScalar
dlgPiSramMibRevMinor = _DlgPiSramMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6, 2),
    _DlgPiSramMibRevMinor_Type()
)
dlgPiSramMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgPiSramMibRevMinor.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLGSRPRF-MIB",
    **{"dlgPiSram": dlgPiSram,
       "dlgPsStatsEnableMask": dlgPsStatsEnableMask,
       "dlgPsPollingInterval": dlgPsPollingInterval,
       "dlgPsElapsedTime": dlgPsElapsedTime,
       "dlgPsCurrentStats": dlgPsCurrentStats,
       "dlgPsCurrentInterrupts": dlgPsCurrentInterrupts,
       "dlgPsCurrentDrvCommands": dlgPsCurrentDrvCommands,
       "dlgPsCurrentFWCommands": dlgPsCurrentFWCommands,
       "dlgPsCurrentUnSolEvents": dlgPsCurrentUnSolEvents,
       "dlgPsCurrentBytesRead": dlgPsCurrentBytesRead,
       "dlgPsCurrentBytesWritten": dlgPsCurrentBytesWritten,
       "dlgPsCurrentLostMsgToFW": dlgPsCurrentLostMsgToFW,
       "dlgPsCurrentLostMsgFromFW": dlgPsCurrentLostMsgFromFW,
       "dlgPsCurrentFWErrorMsgs": dlgPsCurrentFWErrorMsgs,
       "dlgPsCurrentDrvErrorMsgs": dlgPsCurrentDrvErrorMsgs,
       "dlgPsTotalStats": dlgPsTotalStats,
       "dlgPsTotalInterrupts": dlgPsTotalInterrupts,
       "dlgPsTotalDrvCommands": dlgPsTotalDrvCommands,
       "dlgPsTotalFWCommands": dlgPsTotalFWCommands,
       "dlgPsTotalUnSolEvents": dlgPsTotalUnSolEvents,
       "dlgPsTotalBytesRead": dlgPsTotalBytesRead,
       "dlgPsTotalBytesWritten": dlgPsTotalBytesWritten,
       "dlgPsTotalLostMsgToFW": dlgPsTotalLostMsgToFW,
       "dlgPsTotalLostMsgFromFW": dlgPsTotalLostMsgFromFW,
       "dlgPsTotalFWErrorMsgs": dlgPsTotalFWErrorMsgs,
       "dlgPsTotalDrvErrorMsgs": dlgPsTotalDrvErrorMsgs,
       "dlgPiSramMibRev": dlgPiSramMibRev,
       "dlgPiSramMibRevMajor": dlgPiSramMibRevMajor,
       "dlgPiSramMibRevMinor": dlgPiSramMibRevMinor}
)
