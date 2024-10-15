# SNMP MIB module (SHIVA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:12 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Shiva_ObjectIdentity = ObjectIdentity
shiva = _Shiva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166)
)
_SSystems_ObjectIdentity = ObjectIdentity
sSystems = _SSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 1)
)
_MessageLog_ObjectIdentity = ObjectIdentity
messageLog = _MessageLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 1, 1)
)
_MLogEntryCount_Type = Integer32
_MLogEntryCount_Object = MibScalar
mLogEntryCount = _MLogEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 1),
    _MLogEntryCount_Type()
)
mLogEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogEntryCount.setStatus("mandatory")


class _MLogNewMessageTrapEnable_Type(Integer32):
    """Custom type mLogNewMessageTrapEnable based on Integer32"""
    defaultValue = 1

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
        *(("alert", 3),
          ("crit", 4),
          ("debug", 9),
          ("disabled", 1),
          ("emerg", 2),
          ("err", 5),
          ("info", 8),
          ("notice", 7),
          ("warning", 6))
    )


_MLogNewMessageTrapEnable_Type.__name__ = "Integer32"
_MLogNewMessageTrapEnable_Object = MibScalar
mLogNewMessageTrapEnable = _MLogNewMessageTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 2),
    _MLogNewMessageTrapEnable_Type()
)
mLogNewMessageTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLogNewMessageTrapEnable.setStatus("mandatory")
_MLogBuffer_Object = MibTable
mLogBuffer = _MLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mLogBuffer.setStatus("mandatory")
_MLogMessage_Object = MibTableRow
mLogMessage = _MLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1)
)
mLogMessage.setIndexNames(
    (0, "SHIVA-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    mLogMessage.setStatus("mandatory")
_MLogTimeStamp_Type = TimeTicks
_MLogTimeStamp_Object = MibTableColumn
mLogTimeStamp = _MLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 1),
    _MLogTimeStamp_Type()
)
mLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogTimeStamp.setStatus("mandatory")


class _MLogPriority_Type(Integer32):
    """Custom type mLogPriority based on Integer32"""
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
        *(("alert", 3),
          ("crit", 4),
          ("debug", 9),
          ("emerg", 2),
          ("err", 5),
          ("info", 8),
          ("not-possible", 1),
          ("notice", 7),
          ("warning", 6))
    )


_MLogPriority_Type.__name__ = "Integer32"
_MLogPriority_Object = MibTableColumn
mLogPriority = _MLogPriority_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 2),
    _MLogPriority_Type()
)
mLogPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogPriority.setStatus("mandatory")
_MLogMessageText_Type = DisplayString
_MLogMessageText_Object = MibTableColumn
mLogMessageText = _MLogMessageText_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 3),
    _MLogMessageText_Type()
)
mLogMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogMessageText.setStatus("mandatory")
_MLogTimeOfDay_Type = Integer32
_MLogTimeOfDay_Object = MibTableColumn
mLogTimeOfDay = _MLogTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4),
    _MLogTimeOfDay_Type()
)
mLogTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogTimeOfDay.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_Scc_ObjectIdentity = ObjectIdentity
scc = _Scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 1, 2)
)
_SccTable_Object = MibTable
sccTable = _SccTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sccTable.setStatus("mandatory")
_SccEntry_Object = MibTableRow
sccEntry = _SccEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1)
)
sccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sccEntry.setStatus("mandatory")
_SccInterrupts_Type = Counter32
_SccInterrupts_Object = MibTableColumn
sccInterrupts = _SccInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 1),
    _SccInterrupts_Type()
)
sccInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccInterrupts.setStatus("mandatory")
_SccAborts_Type = Counter32
_SccAborts_Object = MibTableColumn
sccAborts = _SccAborts_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 2),
    _SccAborts_Type()
)
sccAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccAborts.setStatus("mandatory")
_SccSpuriousInts_Type = Counter32
_SccSpuriousInts_Object = MibTableColumn
sccSpuriousInts = _SccSpuriousInts_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 3),
    _SccSpuriousInts_Type()
)
sccSpuriousInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccSpuriousInts.setStatus("mandatory")
_SccDeferTimeouts_Type = Counter32
_SccDeferTimeouts_Object = MibTableColumn
sccDeferTimeouts = _SccDeferTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 4),
    _SccDeferTimeouts_Type()
)
sccDeferTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccDeferTimeouts.setStatus("mandatory")
_SccOverruns_Type = Counter32
_SccOverruns_Object = MibTableColumn
sccOverruns = _SccOverruns_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 5),
    _SccOverruns_Type()
)
sccOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccOverruns.setStatus("mandatory")
_SccUnderruns_Type = Counter32
_SccUnderruns_Object = MibTableColumn
sccUnderruns = _SccUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 6),
    _SccUnderruns_Type()
)
sccUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccUnderruns.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2)
)
_Fastpath_ObjectIdentity = ObjectIdentity
fastpath = _Fastpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1)
)
_FpBuffer_ObjectIdentity = ObjectIdentity
fpBuffer = _FpBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1)
)
_BufferSize_Type = Integer32
_BufferSize_Object = MibScalar
bufferSize = _BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 1),
    _BufferSize_Type()
)
bufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSize.setStatus("mandatory")
_BufferAvail_Type = Integer32
_BufferAvail_Object = MibScalar
bufferAvail = _BufferAvail_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 2),
    _BufferAvail_Type()
)
bufferAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferAvail.setStatus("mandatory")
_BufferDrops_Type = Counter32
_BufferDrops_Object = MibScalar
bufferDrops = _BufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 3),
    _BufferDrops_Type()
)
bufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferDrops.setStatus("mandatory")
_BufferTypeTable_Object = MibTable
bufferTypeTable = _BufferTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    bufferTypeTable.setStatus("mandatory")
_BufferTypeEntry_Object = MibTableRow
bufferTypeEntry = _BufferTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1)
)
bufferTypeEntry.setIndexNames(
    (0, "SHIVA-MIB", "bufferTypeIndex"),
)
if mibBuilder.loadTexts:
    bufferTypeEntry.setStatus("mandatory")
_BufferTypeIndex_Type = Integer32
_BufferTypeIndex_Object = MibTableColumn
bufferTypeIndex = _BufferTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 1),
    _BufferTypeIndex_Type()
)
bufferTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeIndex.setStatus("mandatory")


class _BufferTypeType_Type(Integer32):
    """Custom type bufferTypeType based on Integer32"""
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
        *(("arp", 5),
          ("data", 6),
          ("erbf", 7),
          ("etbf", 8),
          ("ethernet", 4),
          ("free", 2),
          ("localtalk", 3),
          ("malloc", 9),
          ("other", 1))
    )


_BufferTypeType_Type.__name__ = "Integer32"
_BufferTypeType_Object = MibTableColumn
bufferTypeType = _BufferTypeType_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 2),
    _BufferTypeType_Type()
)
bufferTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeType.setStatus("mandatory")
_BufferTypeDescr_Type = DisplayString
_BufferTypeDescr_Object = MibTableColumn
bufferTypeDescr = _BufferTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 3),
    _BufferTypeDescr_Type()
)
bufferTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeDescr.setStatus("mandatory")
_BufferTypeCount_Type = Integer32
_BufferTypeCount_Object = MibTableColumn
bufferTypeCount = _BufferTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 4),
    _BufferTypeCount_Type()
)
bufferTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeCount.setStatus("mandatory")
_BufferTypeDrops_Type = Integer32
_BufferTypeDrops_Object = MibTableColumn
bufferTypeDrops = _BufferTypeDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 5),
    _BufferTypeDrops_Type()
)
bufferTypeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeDrops.setStatus("mandatory")
_BufferTypeRequests_Type = Integer32
_BufferTypeRequests_Object = MibTableColumn
bufferTypeRequests = _BufferTypeRequests_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 6),
    _BufferTypeRequests_Type()
)
bufferTypeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeRequests.setStatus("mandatory")
_BufferTypeMaximum_Type = Integer32
_BufferTypeMaximum_Object = MibTableColumn
bufferTypeMaximum = _BufferTypeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 7),
    _BufferTypeMaximum_Type()
)
bufferTypeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeMaximum.setStatus("mandatory")
_FpConf_ObjectIdentity = ObjectIdentity
fpConf = _FpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2)
)
_ConfReboot_Type = TimeTicks
_ConfReboot_Object = MibScalar
confReboot = _ConfReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 1),
    _ConfReboot_Type()
)
confReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confReboot.setStatus("mandatory")


class _ConfCheckSum_Type(Integer32):
    """Custom type confCheckSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ConfCheckSum_Type.__name__ = "Integer32"
_ConfCheckSum_Object = MibScalar
confCheckSum = _ConfCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 2),
    _ConfCheckSum_Type()
)
confCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confCheckSum.setStatus("mandatory")


class _CodeCheckSum_Type(Integer32):
    """Custom type codeCheckSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CodeCheckSum_Type.__name__ = "Integer32"
_CodeCheckSum_Object = MibScalar
codeCheckSum = _CodeCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 3),
    _CodeCheckSum_Type()
)
codeCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codeCheckSum.setStatus("mandatory")
_PromVersion_Type = Integer32
_PromVersion_Object = MibScalar
promVersion = _PromVersion_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 4),
    _PromVersion_Type()
)
promVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVersion.setStatus("mandatory")
_HwStatus_Type = Integer32
_HwStatus_Object = MibScalar
hwStatus = _HwStatus_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 5),
    _HwStatus_Type()
)
hwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatus.setStatus("mandatory")


class _ConfWhyReboot_Type(Integer32):
    """Custom type confWhyReboot based on Integer32"""
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
        *(("config", 5),
          ("firmware", 3),
          ("hardware", 2),
          ("other", 1),
          ("software", 4))
    )


_ConfWhyReboot_Type.__name__ = "Integer32"
_ConfWhyReboot_Object = MibScalar
confWhyReboot = _ConfWhyReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 6),
    _ConfWhyReboot_Type()
)
confWhyReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confWhyReboot.setStatus("mandatory")
_ConfWhoReboot_Type = DisplayString
_ConfWhoReboot_Object = MibScalar
confWhoReboot = _ConfWhoReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 7),
    _ConfWhoReboot_Type()
)
confWhoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confWhoReboot.setStatus("mandatory")
_ConfRebootComment_Type = DisplayString
_ConfRebootComment_Object = MibScalar
confRebootComment = _ConfRebootComment_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 8),
    _ConfRebootComment_Type()
)
confRebootComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRebootComment.setStatus("mandatory")


class _ConfHowReboot_Type(Integer32):
    """Custom type confHowReboot based on Integer32"""
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
        *(("bootprom", 5),
          ("go", 2),
          ("pause", 3),
          ("reset", 4),
          ("restart", 1))
    )


_ConfHowReboot_Type.__name__ = "Integer32"
_ConfHowReboot_Object = MibScalar
confHowReboot = _ConfHowReboot_Object(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 9),
    _ConfHowReboot_Type()
)
confHowReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confHowReboot.setStatus("mandatory")
_K_star_ObjectIdentity = ObjectIdentity
k_star = _K_star_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 1, 3)
)
_NmV32e_ObjectIdentity = ObjectIdentity
nmV32e = _NmV32e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 2, 2)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 3)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4)
)
_TBap_ObjectIdentity = ObjectIdentity
tBap = _TBap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4, 1)
)
_TATalk_ObjectIdentity = ObjectIdentity
tATalk = _TATalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4, 2)
)
_TRTMPEntryTimeouts_Type = Integer32
_TRTMPEntryTimeouts_Object = MibScalar
tRTMPEntryTimeouts = _TRTMPEntryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 1),
    _TRTMPEntryTimeouts_Type()
)
tRTMPEntryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryTimeouts.setStatus("mandatory")
_TRTMPEntryDeletes_Type = Integer32
_TRTMPEntryDeletes_Object = MibScalar
tRTMPEntryDeletes = _TRTMPEntryDeletes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 2),
    _TRTMPEntryDeletes_Type()
)
tRTMPEntryDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryDeletes.setStatus("mandatory")
_TRTMPEntryEqualReplaces_Type = Integer32
_TRTMPEntryEqualReplaces_Object = MibScalar
tRTMPEntryEqualReplaces = _TRTMPEntryEqualReplaces_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 3),
    _TRTMPEntryEqualReplaces_Type()
)
tRTMPEntryEqualReplaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryEqualReplaces.setStatus("mandatory")
_TRTMPEntryBetterReplaces_Type = Integer32
_TRTMPEntryBetterReplaces_Object = MibScalar
tRTMPEntryBetterReplaces = _TRTMPEntryBetterReplaces_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 4),
    _TRTMPEntryBetterReplaces_Type()
)
tRTMPEntryBetterReplaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryBetterReplaces.setStatus("mandatory")
_TRTMPEntryAdds_Type = Integer32
_TRTMPEntryAdds_Object = MibScalar
tRTMPEntryAdds = _TRTMPEntryAdds_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 5),
    _TRTMPEntryAdds_Type()
)
tRTMPEntryAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryAdds.setStatus("mandatory")


class _TRTMPZeroCounters_Type(Integer32):
    """Custom type tRTMPZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("zero", 1)
    )


_TRTMPZeroCounters_Type.__name__ = "Integer32"
_TRTMPZeroCounters_Object = MibScalar
tRTMPZeroCounters = _TRTMPZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 6),
    _TRTMPZeroCounters_Type()
)
tRTMPZeroCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tRTMPZeroCounters.setStatus("mandatory")
_TZIPDeletes_Type = Integer32
_TZIPDeletes_Object = MibScalar
tZIPDeletes = _TZIPDeletes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 7),
    _TZIPDeletes_Type()
)
tZIPDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tZIPDeletes.setStatus("mandatory")
_TZIPAdds_Type = Integer32
_TZIPAdds_Object = MibScalar
tZIPAdds = _TZIPAdds_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 8),
    _TZIPAdds_Type()
)
tZIPAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tZIPAdds.setStatus("mandatory")


class _TZIPZeroCounters_Type(Integer32):
    """Custom type tZIPZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("zero", 1)
    )


_TZIPZeroCounters_Type.__name__ = "Integer32"
_TZIPZeroCounters_Object = MibScalar
tZIPZeroCounters = _TZIPZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 9),
    _TZIPZeroCounters_Type()
)
tZIPZeroCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tZIPZeroCounters.setStatus("mandatory")


class _TAARPClearCache_Type(Integer32):
    """Custom type tAARPClearCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TAARPClearCache_Type.__name__ = "Integer32"
_TAARPClearCache_Object = MibScalar
tAARPClearCache = _TAARPClearCache_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 10),
    _TAARPClearCache_Type()
)
tAARPClearCache.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tAARPClearCache.setStatus("mandatory")


class _TKIPRoutesValid_Type(Integer32):
    """Custom type tKIPRoutesValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TKIPRoutesValid_Type.__name__ = "Integer32"
_TKIPRoutesValid_Object = MibScalar
tKIPRoutesValid = _TKIPRoutesValid_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 11),
    _TKIPRoutesValid_Type()
)
tKIPRoutesValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tKIPRoutesValid.setStatus("mandatory")
_TIP_ObjectIdentity = ObjectIdentity
tIP = _TIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4, 3)
)


class _TARPClearCache_Type(Integer32):
    """Custom type tARPClearCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TARPClearCache_Type.__name__ = "Integer32"
_TARPClearCache_Object = MibScalar
tARPClearCache = _TARPClearCache_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 1),
    _TARPClearCache_Type()
)
tARPClearCache.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tARPClearCache.setStatus("mandatory")


class _TIPClearRoutingTable_Type(Integer32):
    """Custom type tIPClearRoutingTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TIPClearRoutingTable_Type.__name__ = "Integer32"
_TIPClearRoutingTable_Object = MibScalar
tIPClearRoutingTable = _TIPClearRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 2),
    _TIPClearRoutingTable_Type()
)
tIPClearRoutingTable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tIPClearRoutingTable.setStatus("mandatory")
_TCommunity_ObjectIdentity = ObjectIdentity
tCommunity = _TCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4, 4)
)


class _TCommunityTrapHostType_Type(Integer32):
    """Custom type tCommunityTrapHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("unconfigured", 1))
    )


_TCommunityTrapHostType_Type.__name__ = "Integer32"
_TCommunityTrapHostType_Object = MibScalar
tCommunityTrapHostType = _TCommunityTrapHostType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 1),
    _TCommunityTrapHostType_Type()
)
tCommunityTrapHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapHostType.setStatus("mandatory")
_TCommunityTrapHostAddress_Type = OctetString
_TCommunityTrapHostAddress_Object = MibScalar
tCommunityTrapHostAddress = _TCommunityTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 2),
    _TCommunityTrapHostAddress_Type()
)
tCommunityTrapHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapHostAddress.setStatus("mandatory")


class _TCommunitySetHostType_Type(Integer32):
    """Custom type tCommunitySetHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("unconfigured", 1))
    )


_TCommunitySetHostType_Type.__name__ = "Integer32"
_TCommunitySetHostType_Object = MibScalar
tCommunitySetHostType = _TCommunitySetHostType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 3),
    _TCommunitySetHostType_Type()
)
tCommunitySetHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunitySetHostType.setStatus("mandatory")
_TCommunitySetHostAddress_Type = OctetString
_TCommunitySetHostAddress_Object = MibScalar
tCommunitySetHostAddress = _TCommunitySetHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 4),
    _TCommunitySetHostAddress_Type()
)
tCommunitySetHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunitySetHostAddress.setStatus("mandatory")
_TCommunityList_Object = MibTable
tCommunityList = _TCommunityList_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5)
)
if mibBuilder.loadTexts:
    tCommunityList.setStatus("mandatory")
_TCommunityEntry_Object = MibTableRow
tCommunityEntry = _TCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1)
)
tCommunityEntry.setIndexNames(
    (0, "SHIVA-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    tCommunityEntry.setStatus("mandatory")
_TCommunityName_Type = DisplayString
_TCommunityName_Object = MibTableColumn
tCommunityName = _TCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 1),
    _TCommunityName_Type()
)
tCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityName.setStatus("mandatory")


class _TCommunityAccess_Type(Integer32):
    """Custom type tCommunityAccess based on Integer32"""
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
        *(("clear-statistics", 3),
          ("configure", 4),
          ("no-access", 1),
          ("read-only-access", 2))
    )


_TCommunityAccess_Type.__name__ = "Integer32"
_TCommunityAccess_Object = MibTableColumn
tCommunityAccess = _TCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 2),
    _TCommunityAccess_Type()
)
tCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityAccess.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_TEther_ObjectIdentity = ObjectIdentity
tEther = _TEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 166, 4, 5)
)
_TEtherTable_Object = MibTable
tEtherTable = _TEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tEtherTable.setStatus("mandatory")
_TEtherEntry_Object = MibTableRow
tEtherEntry = _TEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1)
)
tEtherEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tEtherEntry.setStatus("mandatory")
_EtherCRCErrors_Type = Counter32
_EtherCRCErrors_Object = MibTableColumn
etherCRCErrors = _EtherCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 1),
    _EtherCRCErrors_Type()
)
etherCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCRCErrors.setStatus("mandatory")
_EtherAlignErrors_Type = Counter32
_EtherAlignErrors_Object = MibTableColumn
etherAlignErrors = _EtherAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 2),
    _EtherAlignErrors_Type()
)
etherAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherAlignErrors.setStatus("mandatory")
_EtherResourceErrors_Type = Counter32
_EtherResourceErrors_Object = MibTableColumn
etherResourceErrors = _EtherResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 3),
    _EtherResourceErrors_Type()
)
etherResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherResourceErrors.setStatus("mandatory")
_EtherOverrunErrors_Type = Counter32
_EtherOverrunErrors_Object = MibTableColumn
etherOverrunErrors = _EtherOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 4),
    _EtherOverrunErrors_Type()
)
etherOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOverrunErrors.setStatus("mandatory")
_EtherInPackets_Type = Counter32
_EtherInPackets_Object = MibTableColumn
etherInPackets = _EtherInPackets_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 5),
    _EtherInPackets_Type()
)
etherInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInPackets.setStatus("mandatory")
_EtherOutPackets_Type = Counter32
_EtherOutPackets_Object = MibTableColumn
etherOutPackets = _EtherOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 6),
    _EtherOutPackets_Type()
)
etherOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutPackets.setStatus("mandatory")
_EtherBadTransmits_Type = Counter32
_EtherBadTransmits_Object = MibTableColumn
etherBadTransmits = _EtherBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 7),
    _EtherBadTransmits_Type()
)
etherBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBadTransmits.setStatus("mandatory")
_EtherOversizeFrames_Type = Counter32
_EtherOversizeFrames_Object = MibTableColumn
etherOversizeFrames = _EtherOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 8),
    _EtherOversizeFrames_Type()
)
etherOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOversizeFrames.setStatus("mandatory")
_EtherSpurRUReadys_Type = Counter32
_EtherSpurRUReadys_Object = MibTableColumn
etherSpurRUReadys = _EtherSpurRUReadys_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 9),
    _EtherSpurRUReadys_Type()
)
etherSpurRUReadys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurRUReadys.setStatus("mandatory")
_EtherSpurCUActives_Type = Counter32
_EtherSpurCUActives_Object = MibTableColumn
etherSpurCUActives = _EtherSpurCUActives_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 10),
    _EtherSpurCUActives_Type()
)
etherSpurCUActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurCUActives.setStatus("mandatory")
_EtherSpurUnknowns_Type = Counter32
_EtherSpurUnknowns_Object = MibTableColumn
etherSpurUnknowns = _EtherSpurUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 11),
    _EtherSpurUnknowns_Type()
)
etherSpurUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurUnknowns.setStatus("mandatory")
_EtherBcastDrops_Type = Counter32
_EtherBcastDrops_Object = MibTableColumn
etherBcastDrops = _EtherBcastDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 12),
    _EtherBcastDrops_Type()
)
etherBcastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBcastDrops.setStatus("mandatory")
_EtherReceiverRestarts_Type = Counter32
_EtherReceiverRestarts_Object = MibTableColumn
etherReceiverRestarts = _EtherReceiverRestarts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 13),
    _EtherReceiverRestarts_Type()
)
etherReceiverRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReceiverRestarts.setStatus("mandatory")
_EtherReinterrupts_Type = Counter32
_EtherReinterrupts_Object = MibTableColumn
etherReinterrupts = _EtherReinterrupts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 14),
    _EtherReinterrupts_Type()
)
etherReinterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReinterrupts.setStatus("mandatory")
_EtherBufferReroutes_Type = Counter32
_EtherBufferReroutes_Object = MibTableColumn
etherBufferReroutes = _EtherBufferReroutes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 15),
    _EtherBufferReroutes_Type()
)
etherBufferReroutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferReroutes.setStatus("mandatory")
_EtherBufferDrops_Type = Counter32
_EtherBufferDrops_Object = MibTableColumn
etherBufferDrops = _EtherBufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 16),
    _EtherBufferDrops_Type()
)
etherBufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferDrops.setStatus("mandatory")
_EtherCollisions_Type = Counter32
_EtherCollisions_Object = MibTableColumn
etherCollisions = _EtherCollisions_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 17),
    _EtherCollisions_Type()
)
etherCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCollisions.setStatus("mandatory")
_EtherDefers_Type = Counter32
_EtherDefers_Object = MibTableColumn
etherDefers = _EtherDefers_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 18),
    _EtherDefers_Type()
)
etherDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDefers.setStatus("mandatory")
_EtherDMAUnderruns_Type = Counter32
_EtherDMAUnderruns_Object = MibTableColumn
etherDMAUnderruns = _EtherDMAUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 19),
    _EtherDMAUnderruns_Type()
)
etherDMAUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDMAUnderruns.setStatus("mandatory")
_EtherMaxCollisions_Type = Counter32
_EtherMaxCollisions_Object = MibTableColumn
etherMaxCollisions = _EtherMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 20),
    _EtherMaxCollisions_Type()
)
etherMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMaxCollisions.setStatus("mandatory")
_EtherNoCarriers_Type = Counter32
_EtherNoCarriers_Object = MibTableColumn
etherNoCarriers = _EtherNoCarriers_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 21),
    _EtherNoCarriers_Type()
)
etherNoCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCarriers.setStatus("mandatory")
_EtherNoCTSs_Type = Counter32
_EtherNoCTSs_Object = MibTableColumn
etherNoCTSs = _EtherNoCTSs_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 22),
    _EtherNoCTSs_Type()
)
etherNoCTSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCTSs.setStatus("mandatory")
_EtherNoSQEs_Type = Counter32
_EtherNoSQEs_Object = MibTableColumn
etherNoSQEs = _EtherNoSQEs_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 23),
    _EtherNoSQEs_Type()
)
etherNoSQEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoSQEs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-MIB",
    **{"shiva": shiva,
       "sSystems": sSystems,
       "messageLog": messageLog,
       "mLogEntryCount": mLogEntryCount,
       "mLogNewMessageTrapEnable": mLogNewMessageTrapEnable,
       "mLogBuffer": mLogBuffer,
       "mLogMessage": mLogMessage,
       "mLogTimeStamp": mLogTimeStamp,
       "mLogPriority": mLogPriority,
       "mLogMessageText": mLogMessageText,
       "mLogTimeOfDay": mLogTimeOfDay,
       "pysmiFakeCol1": pysmiFakeCol1,
       "scc": scc,
       "sccTable": sccTable,
       "sccEntry": sccEntry,
       "sccInterrupts": sccInterrupts,
       "sccAborts": sccAborts,
       "sccSpuriousInts": sccSpuriousInts,
       "sccDeferTimeouts": sccDeferTimeouts,
       "sccOverruns": sccOverruns,
       "sccUnderruns": sccUnderruns,
       "products": products,
       "fastpath": fastpath,
       "fpBuffer": fpBuffer,
       "bufferSize": bufferSize,
       "bufferAvail": bufferAvail,
       "bufferDrops": bufferDrops,
       "bufferTypeTable": bufferTypeTable,
       "bufferTypeEntry": bufferTypeEntry,
       "bufferTypeIndex": bufferTypeIndex,
       "bufferTypeType": bufferTypeType,
       "bufferTypeDescr": bufferTypeDescr,
       "bufferTypeCount": bufferTypeCount,
       "bufferTypeDrops": bufferTypeDrops,
       "bufferTypeRequests": bufferTypeRequests,
       "bufferTypeMaximum": bufferTypeMaximum,
       "fpConf": fpConf,
       "confReboot": confReboot,
       "confCheckSum": confCheckSum,
       "codeCheckSum": codeCheckSum,
       "promVersion": promVersion,
       "hwStatus": hwStatus,
       "confWhyReboot": confWhyReboot,
       "confWhoReboot": confWhoReboot,
       "confRebootComment": confRebootComment,
       "confHowReboot": confHowReboot,
       "k-star": k_star,
       "nmV32e": nmV32e,
       "protocols": protocols,
       "temporary": temporary,
       "tBap": tBap,
       "tATalk": tATalk,
       "tRTMPEntryTimeouts": tRTMPEntryTimeouts,
       "tRTMPEntryDeletes": tRTMPEntryDeletes,
       "tRTMPEntryEqualReplaces": tRTMPEntryEqualReplaces,
       "tRTMPEntryBetterReplaces": tRTMPEntryBetterReplaces,
       "tRTMPEntryAdds": tRTMPEntryAdds,
       "tRTMPZeroCounters": tRTMPZeroCounters,
       "tZIPDeletes": tZIPDeletes,
       "tZIPAdds": tZIPAdds,
       "tZIPZeroCounters": tZIPZeroCounters,
       "tAARPClearCache": tAARPClearCache,
       "tKIPRoutesValid": tKIPRoutesValid,
       "tIP": tIP,
       "tARPClearCache": tARPClearCache,
       "tIPClearRoutingTable": tIPClearRoutingTable,
       "tCommunity": tCommunity,
       "tCommunityTrapHostType": tCommunityTrapHostType,
       "tCommunityTrapHostAddress": tCommunityTrapHostAddress,
       "tCommunitySetHostType": tCommunitySetHostType,
       "tCommunitySetHostAddress": tCommunitySetHostAddress,
       "tCommunityList": tCommunityList,
       "tCommunityEntry": tCommunityEntry,
       "tCommunityName": tCommunityName,
       "tCommunityAccess": tCommunityAccess,
       "pysmiFakeCol2": pysmiFakeCol2,
       "tEther": tEther,
       "tEtherTable": tEtherTable,
       "tEtherEntry": tEtherEntry,
       "etherCRCErrors": etherCRCErrors,
       "etherAlignErrors": etherAlignErrors,
       "etherResourceErrors": etherResourceErrors,
       "etherOverrunErrors": etherOverrunErrors,
       "etherInPackets": etherInPackets,
       "etherOutPackets": etherOutPackets,
       "etherBadTransmits": etherBadTransmits,
       "etherOversizeFrames": etherOversizeFrames,
       "etherSpurRUReadys": etherSpurRUReadys,
       "etherSpurCUActives": etherSpurCUActives,
       "etherSpurUnknowns": etherSpurUnknowns,
       "etherBcastDrops": etherBcastDrops,
       "etherReceiverRestarts": etherReceiverRestarts,
       "etherReinterrupts": etherReinterrupts,
       "etherBufferReroutes": etherBufferReroutes,
       "etherBufferDrops": etherBufferDrops,
       "etherCollisions": etherCollisions,
       "etherDefers": etherDefers,
       "etherDMAUnderruns": etherDMAUnderruns,
       "etherMaxCollisions": etherMaxCollisions,
       "etherNoCarriers": etherNoCarriers,
       "etherNoCTSs": etherNoCTSs,
       "etherNoSQEs": etherNoSQEs}
)
