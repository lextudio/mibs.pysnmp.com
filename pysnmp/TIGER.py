# SNMP MIB module (TIGER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIGER
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:47 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class TigerDateAndTime(DisplayString):
    """Custom type TigerDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ngcan_ObjectIdentity = ObjectIdentity
ngcan = _Ngcan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978)
)
_Tiger_ObjectIdentity = ObjectIdentity
tiger = _Tiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2)
)
_GeneralTiger_ObjectIdentity = ObjectIdentity
generalTiger = _GeneralTiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1)
)
_IfTStack_ObjectIdentity = ObjectIdentity
ifTStack = _IfTStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1)
)
_IfTStackTable_Object = MibTable
ifTStackTable = _IfTStackTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ifTStackTable.setStatus("mandatory")
_IfTStackEntry_Object = MibTableRow
ifTStackEntry = _IfTStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1, 1)
)
ifTStackEntry.setIndexNames(
    (0, "TIGER", "ifTStackIndex"),
)
if mibBuilder.loadTexts:
    ifTStackEntry.setStatus("mandatory")
_IfTStackIndex_Type = Integer32
_IfTStackIndex_Object = MibTableColumn
ifTStackIndex = _IfTStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1, 1, 1),
    _IfTStackIndex_Type()
)
ifTStackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTStackIndex.setStatus("mandatory")
_IfTStackHigherLayer_Type = Integer32
_IfTStackHigherLayer_Object = MibTableColumn
ifTStackHigherLayer = _IfTStackHigherLayer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1, 1, 2),
    _IfTStackHigherLayer_Type()
)
ifTStackHigherLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTStackHigherLayer.setStatus("mandatory")
_IfTStackLowerLayer_Type = Integer32
_IfTStackLowerLayer_Object = MibTableColumn
ifTStackLowerLayer = _IfTStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1, 1, 3),
    _IfTStackLowerLayer_Type()
)
ifTStackLowerLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTStackLowerLayer.setStatus("mandatory")
_IfTStackStatus_Type = RowStatus
_IfTStackStatus_Object = MibTableColumn
ifTStackStatus = _IfTStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 1, 1, 1, 4),
    _IfTStackStatus_Type()
)
ifTStackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTStackStatus.setStatus("mandatory")
_Tsystem_ObjectIdentity = ObjectIdentity
tsystem = _Tsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2)
)
_TigSystemDate_Type = TigerDateAndTime
_TigSystemDate_Object = MibScalar
tigSystemDate = _TigSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 1),
    _TigSystemDate_Type()
)
tigSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigSystemDate.setStatus("mandatory")


class _TigSystemExceptionEcho_Type(Integer32):
    """Custom type tigSystemExceptionEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TigSystemExceptionEcho_Type.__name__ = "Integer32"
_TigSystemExceptionEcho_Object = MibScalar
tigSystemExceptionEcho = _TigSystemExceptionEcho_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 2),
    _TigSystemExceptionEcho_Type()
)
tigSystemExceptionEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigSystemExceptionEcho.setStatus("mandatory")


class _TigSystemExceptionLogging_Type(Integer32):
    """Custom type tigSystemExceptionLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TigSystemExceptionLogging_Type.__name__ = "Integer32"
_TigSystemExceptionLogging_Object = MibScalar
tigSystemExceptionLogging = _TigSystemExceptionLogging_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 3),
    _TigSystemExceptionLogging_Type()
)
tigSystemExceptionLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigSystemExceptionLogging.setStatus("mandatory")


class _TigSystemExceptionSaveLog_Type(Integer32):
    """Custom type tigSystemExceptionSaveLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TigSystemExceptionSaveLog_Type.__name__ = "Integer32"
_TigSystemExceptionSaveLog_Object = MibScalar
tigSystemExceptionSaveLog = _TigSystemExceptionSaveLog_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 4),
    _TigSystemExceptionSaveLog_Type()
)
tigSystemExceptionSaveLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigSystemExceptionSaveLog.setStatus("mandatory")
_TigPCMCIATable_Object = MibTable
tigPCMCIATable = _TigPCMCIATable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tigPCMCIATable.setStatus("mandatory")
_TigPCMCIAEntry_Object = MibTableRow
tigPCMCIAEntry = _TigPCMCIAEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5, 1)
)
tigPCMCIAEntry.setIndexNames(
    (0, "TIGER", "tigPCMCIASlot"),
)
if mibBuilder.loadTexts:
    tigPCMCIAEntry.setStatus("mandatory")


class _TigPCMCIASlot_Type(Integer32):
    """Custom type tigPCMCIASlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TigPCMCIASlot_Type.__name__ = "Integer32"
_TigPCMCIASlot_Object = MibTableColumn
tigPCMCIASlot = _TigPCMCIASlot_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5, 1, 1),
    _TigPCMCIASlot_Type()
)
tigPCMCIASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigPCMCIASlot.setStatus("mandatory")
_TigPCMCIAIf_Type = InterfaceIndex
_TigPCMCIAIf_Object = MibTableColumn
tigPCMCIAIf = _TigPCMCIAIf_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5, 1, 2),
    _TigPCMCIAIf_Type()
)
tigPCMCIAIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPCMCIAIf.setStatus("mandatory")


class _TigTokenRingSpeed_Type(Integer32):
    """Custom type tigTokenRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four", 1),
          ("sixteen", 2))
    )


_TigTokenRingSpeed_Type.__name__ = "Integer32"
_TigTokenRingSpeed_Object = MibTableColumn
tigTokenRingSpeed = _TigTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5, 1, 3),
    _TigTokenRingSpeed_Type()
)
tigTokenRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigTokenRingSpeed.setStatus("mandatory")


class _TigPCMCIAType_Type(Integer32):
    """Custom type tigPCMCIAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem", 2),
          ("token-ring", 1))
    )


_TigPCMCIAType_Type.__name__ = "Integer32"
_TigPCMCIAType_Object = MibTableColumn
tigPCMCIAType = _TigPCMCIAType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 5, 1, 4),
    _TigPCMCIAType_Type()
)
tigPCMCIAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPCMCIAType.setStatus("mandatory")


class _TigConfigFile_Type(OctetString):
    """Custom type tigConfigFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TigConfigFile_Type.__name__ = "OctetString"
_TigConfigFile_Object = MibScalar
tigConfigFile = _TigConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 6),
    _TigConfigFile_Type()
)
tigConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigConfigFile.setStatus("mandatory")


class _TigRestartReason_Type(Integer32):
    """Custom type tigRestartReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("config-fail", 4),
          ("double-bus-fault", 6),
          ("fatal-exception", 7),
          ("other", 5),
          ("power", 1),
          ("reboot-command", 8),
          ("reset-button", 2),
          ("watchdog", 3))
    )


_TigRestartReason_Type.__name__ = "Integer32"
_TigRestartReason_Object = MibScalar
tigRestartReason = _TigRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 7),
    _TigRestartReason_Type()
)
tigRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigRestartReason.setStatus("mandatory")


class _TigClearStats_Type(Integer32):
    """Custom type tigClearStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("cleared", 2),
          ("cleared-confirmed", 3))
    )


_TigClearStats_Type.__name__ = "Integer32"
_TigClearStats_Object = MibScalar
tigClearStats = _TigClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 8),
    _TigClearStats_Type()
)
tigClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigClearStats.setStatus("mandatory")
_TigClearStatsTime_Type = TimeTicks
_TigClearStatsTime_Object = MibScalar
tigClearStatsTime = _TigClearStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 9),
    _TigClearStatsTime_Type()
)
tigClearStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigClearStatsTime.setStatus("mandatory")


class _TigCpuTrapControl_Type(Integer32):
    """Custom type tigCpuTrapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TigCpuTrapControl_Type.__name__ = "Integer32"
_TigCpuTrapControl_Object = MibScalar
tigCpuTrapControl = _TigCpuTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 10),
    _TigCpuTrapControl_Type()
)
tigCpuTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigCpuTrapControl.setStatus("mandatory")


class _TigCpuIdleState_Type(Integer32):
    """Custom type tigCpuIdleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("idle", 1))
    )


_TigCpuIdleState_Type.__name__ = "Integer32"
_TigCpuIdleState_Object = MibScalar
tigCpuIdleState = _TigCpuIdleState_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 11),
    _TigCpuIdleState_Type()
)
tigCpuIdleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigCpuIdleState.setStatus("mandatory")
_TigSystemSerialNum_Type = Integer32
_TigSystemSerialNum_Object = MibScalar
tigSystemSerialNum = _TigSystemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 12),
    _TigSystemSerialNum_Type()
)
tigSystemSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigSystemSerialNum.setStatus("mandatory")


class _TigDomainName_Type(OctetString):
    """Custom type tigDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TigDomainName_Type.__name__ = "OctetString"
_TigDomainName_Object = MibScalar
tigDomainName = _TigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 2, 13),
    _TigDomainName_Type()
)
tigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigDomainName.setStatus("mandatory")
_Buffers_ObjectIdentity = ObjectIdentity
buffers = _Buffers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3)
)


class _TigPoolNumEntries_Type(Integer32):
    """Custom type tigPoolNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TigPoolNumEntries_Type.__name__ = "Integer32"
_TigPoolNumEntries_Object = MibScalar
tigPoolNumEntries = _TigPoolNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 1),
    _TigPoolNumEntries_Type()
)
tigPoolNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigPoolNumEntries.setStatus("mandatory")
_TigPoolTable_Object = MibTable
tigPoolTable = _TigPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tigPoolTable.setStatus("mandatory")
_TigPoolEntry_Object = MibTableRow
tigPoolEntry = _TigPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1)
)
tigPoolEntry.setIndexNames(
    (0, "TIGER", "tigPoolIndex"),
)
if mibBuilder.loadTexts:
    tigPoolEntry.setStatus("mandatory")
_TigPoolIndex_Type = Integer32
_TigPoolIndex_Object = MibTableColumn
tigPoolIndex = _TigPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 1),
    _TigPoolIndex_Type()
)
tigPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolIndex.setStatus("mandatory")
_TigPoolSize_Type = Integer32
_TigPoolSize_Object = MibTableColumn
tigPoolSize = _TigPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 2),
    _TigPoolSize_Type()
)
tigPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolSize.setStatus("mandatory")
_TigPoolBufSize_Type = Integer32
_TigPoolBufSize_Object = MibTableColumn
tigPoolBufSize = _TigPoolBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 3),
    _TigPoolBufSize_Type()
)
tigPoolBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolBufSize.setStatus("mandatory")


class _TigPoolLowThreshold_Type(Integer32):
    """Custom type tigPoolLowThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TigPoolLowThreshold_Type.__name__ = "Integer32"
_TigPoolLowThreshold_Object = MibTableColumn
tigPoolLowThreshold = _TigPoolLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 4),
    _TigPoolLowThreshold_Type()
)
tigPoolLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolLowThreshold.setStatus("mandatory")


class _TigPoolHighThreshold_Type(Integer32):
    """Custom type tigPoolHighThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TigPoolHighThreshold_Type.__name__ = "Integer32"
_TigPoolHighThreshold_Object = MibTableColumn
tigPoolHighThreshold = _TigPoolHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 5),
    _TigPoolHighThreshold_Type()
)
tigPoolHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolHighThreshold.setStatus("mandatory")
_TigPoolFree_Type = Integer32
_TigPoolFree_Object = MibTableColumn
tigPoolFree = _TigPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 6),
    _TigPoolFree_Type()
)
tigPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigPoolFree.setStatus("mandatory")


class _TigPoolCommandStatus_Type(Integer32):
    """Custom type tigPoolCommandStatus based on Integer32"""
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
        *(("create", 2),
          ("created", 3),
          ("failed", 4),
          ("notInUse", 1))
    )


_TigPoolCommandStatus_Type.__name__ = "Integer32"
_TigPoolCommandStatus_Object = MibTableColumn
tigPoolCommandStatus = _TigPoolCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 7),
    _TigPoolCommandStatus_Type()
)
tigPoolCommandStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolCommandStatus.setStatus("mandatory")
_TigPoolAllocationFailures_Type = Counter32
_TigPoolAllocationFailures_Object = MibTableColumn
tigPoolAllocationFailures = _TigPoolAllocationFailures_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 8),
    _TigPoolAllocationFailures_Type()
)
tigPoolAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigPoolAllocationFailures.setStatus("mandatory")


class _TigPoolTrapControl_Type(Integer32):
    """Custom type tigPoolTrapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TigPoolTrapControl_Type.__name__ = "Integer32"
_TigPoolTrapControl_Object = MibTableColumn
tigPoolTrapControl = _TigPoolTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 9),
    _TigPoolTrapControl_Type()
)
tigPoolTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tigPoolTrapControl.setStatus("mandatory")


class _TigPoolTrapStatus_Type(Integer32):
    """Custom type tigPoolTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("recovery", 2))
    )


_TigPoolTrapStatus_Type.__name__ = "Integer32"
_TigPoolTrapStatus_Object = MibTableColumn
tigPoolTrapStatus = _TigPoolTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 3, 2, 1, 10),
    _TigPoolTrapStatus_Type()
)
tigPoolTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tigPoolTrapStatus.setStatus("mandatory")
_GeneralTraps_ObjectIdentity = ObjectIdentity
generalTraps = _GeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 4)
)
_Autif_ObjectIdentity = ObjectIdentity
autif = _Autif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5)
)


class _AutifNumEntries_Type(Integer32):
    """Custom type autifNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AutifNumEntries_Type.__name__ = "Integer32"
_AutifNumEntries_Object = MibScalar
autifNumEntries = _AutifNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 1),
    _AutifNumEntries_Type()
)
autifNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifNumEntries.setStatus("mandatory")
_AutifTable_Object = MibTable
autifTable = _AutifTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    autifTable.setStatus("mandatory")
_AutifEntry_Object = MibTableRow
autifEntry = _AutifEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1)
)
autifEntry.setIndexNames(
    (0, "TIGER", "autifIndex"),
)
if mibBuilder.loadTexts:
    autifEntry.setStatus("mandatory")
_AutifIndex_Type = Integer32
_AutifIndex_Object = MibTableColumn
autifIndex = _AutifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 1),
    _AutifIndex_Type()
)
autifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifIndex.setStatus("mandatory")


class _AutifService_Type(Integer32):
    """Custom type autifService based on Integer32"""
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
        *(("continental", 4),
          ("dlsw", 5),
          ("listener", 6),
          ("matip", 7),
          ("ofep-sabre", 8),
          ("ofep-sabre-listener", 9),
          ("system-1", 3),
          ("tcp", 2),
          ("udp", 1))
    )


_AutifService_Type.__name__ = "Integer32"
_AutifService_Object = MibTableColumn
autifService = _AutifService_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 2),
    _AutifService_Type()
)
autifService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifService.setStatus("mandatory")
_AutifRemAddress_Type = IpAddress
_AutifRemAddress_Object = MibTableColumn
autifRemAddress = _AutifRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 3),
    _AutifRemAddress_Type()
)
autifRemAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifRemAddress.setStatus("mandatory")


class _AutifLocalPort_Type(Integer32):
    """Custom type autifLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AutifLocalPort_Type.__name__ = "Integer32"
_AutifLocalPort_Object = MibTableColumn
autifLocalPort = _AutifLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 4),
    _AutifLocalPort_Type()
)
autifLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifLocalPort.setStatus("mandatory")


class _AutifRemotePort_Type(Integer32):
    """Custom type autifRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AutifRemotePort_Type.__name__ = "Integer32"
_AutifRemotePort_Object = MibTableColumn
autifRemotePort = _AutifRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 5),
    _AutifRemotePort_Type()
)
autifRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifRemotePort.setStatus("mandatory")


class _AutifRxBufSize_Type(Integer32):
    """Custom type autifRxBufSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AutifRxBufSize_Type.__name__ = "Integer32"
_AutifRxBufSize_Object = MibTableColumn
autifRxBufSize = _AutifRxBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 6),
    _AutifRxBufSize_Type()
)
autifRxBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifRxBufSize.setStatus("mandatory")


class _AutifTxBufSize_Type(Integer32):
    """Custom type autifTxBufSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AutifTxBufSize_Type.__name__ = "Integer32"
_AutifTxBufSize_Object = MibTableColumn
autifTxBufSize = _AutifTxBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 7),
    _AutifTxBufSize_Type()
)
autifTxBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifTxBufSize.setStatus("mandatory")


class _AutifSockQueueSize_Type(Integer32):
    """Custom type autifSockQueueSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AutifSockQueueSize_Type.__name__ = "Integer32"
_AutifSockQueueSize_Object = MibTableColumn
autifSockQueueSize = _AutifSockQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 8),
    _AutifSockQueueSize_Type()
)
autifSockQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifSockQueueSize.setStatus("mandatory")


class _AutifTypeAQueueSize_Type(Integer32):
    """Custom type autifTypeAQueueSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AutifTypeAQueueSize_Type.__name__ = "Integer32"
_AutifTypeAQueueSize_Object = MibTableColumn
autifTypeAQueueSize = _AutifTypeAQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 9),
    _AutifTypeAQueueSize_Type()
)
autifTypeAQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifTypeAQueueSize.setStatus("mandatory")


class _AutifTypeAMaxMsgSize_Type(Integer32):
    """Custom type autifTypeAMaxMsgSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AutifTypeAMaxMsgSize_Type.__name__ = "Integer32"
_AutifTypeAMaxMsgSize_Object = MibTableColumn
autifTypeAMaxMsgSize = _AutifTypeAMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 10),
    _AutifTypeAMaxMsgSize_Type()
)
autifTypeAMaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifTypeAMaxMsgSize.setStatus("mandatory")
_AutifInOctets_Type = Counter32
_AutifInOctets_Object = MibTableColumn
autifInOctets = _AutifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 11),
    _AutifInOctets_Type()
)
autifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInOctets.setStatus("mandatory")
_AutifInUcastPkts_Type = Counter32
_AutifInUcastPkts_Object = MibTableColumn
autifInUcastPkts = _AutifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 12),
    _AutifInUcastPkts_Type()
)
autifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInUcastPkts.setStatus("mandatory")
_AutifInNUcastPkts_Type = Counter32
_AutifInNUcastPkts_Object = MibTableColumn
autifInNUcastPkts = _AutifInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 13),
    _AutifInNUcastPkts_Type()
)
autifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInNUcastPkts.setStatus("mandatory")
_AutifInDiscards_Type = Counter32
_AutifInDiscards_Object = MibTableColumn
autifInDiscards = _AutifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 14),
    _AutifInDiscards_Type()
)
autifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInDiscards.setStatus("mandatory")
_AutifInErrors_Type = Counter32
_AutifInErrors_Object = MibTableColumn
autifInErrors = _AutifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 15),
    _AutifInErrors_Type()
)
autifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInErrors.setStatus("mandatory")
_AutifInUnknownProtos_Type = Counter32
_AutifInUnknownProtos_Object = MibTableColumn
autifInUnknownProtos = _AutifInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 16),
    _AutifInUnknownProtos_Type()
)
autifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifInUnknownProtos.setStatus("mandatory")
_AutifOutOctets_Type = Counter32
_AutifOutOctets_Object = MibTableColumn
autifOutOctets = _AutifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 17),
    _AutifOutOctets_Type()
)
autifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifOutOctets.setStatus("mandatory")
_AutifOutUcastPkts_Type = Counter32
_AutifOutUcastPkts_Object = MibTableColumn
autifOutUcastPkts = _AutifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 18),
    _AutifOutUcastPkts_Type()
)
autifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifOutUcastPkts.setStatus("mandatory")
_AutifOutNUcastPkts_Type = Counter32
_AutifOutNUcastPkts_Object = MibTableColumn
autifOutNUcastPkts = _AutifOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 19),
    _AutifOutNUcastPkts_Type()
)
autifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifOutNUcastPkts.setStatus("mandatory")
_AutifOutDiscards_Type = Counter32
_AutifOutDiscards_Object = MibTableColumn
autifOutDiscards = _AutifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 20),
    _AutifOutDiscards_Type()
)
autifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifOutDiscards.setStatus("mandatory")
_AutifOutErrors_Type = Counter32
_AutifOutErrors_Object = MibTableColumn
autifOutErrors = _AutifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 21),
    _AutifOutErrors_Type()
)
autifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifOutErrors.setStatus("mandatory")


class _AutifIA_Type(OctetString):
    """Custom type autifIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AutifIA_Type.__name__ = "OctetString"
_AutifIA_Object = MibTableColumn
autifIA = _AutifIA_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 22),
    _AutifIA_Type()
)
autifIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifIA.setStatus("mandatory")
_AutifAliasAddress_Type = IpAddress
_AutifAliasAddress_Object = MibTableColumn
autifAliasAddress = _AutifAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 23),
    _AutifAliasAddress_Type()
)
autifAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifAliasAddress.setStatus("mandatory")


class _AutifSockPrecedence_Type(Integer32):
    """Custom type autifSockPrecedence based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("flash", 4),
          ("flash-override", 5),
          ("immediate", 3),
          ("internetwork-control", 7),
          ("network-control", 8),
          ("priority", 2),
          ("routine", 1))
    )


_AutifSockPrecedence_Type.__name__ = "Integer32"
_AutifSockPrecedence_Object = MibTableColumn
autifSockPrecedence = _AutifSockPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 24),
    _AutifSockPrecedence_Type()
)
autifSockPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifSockPrecedence.setStatus("mandatory")


class _AutifDestAddrType_Type(Integer32):
    """Custom type autifDestAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("none", 1))
    )


_AutifDestAddrType_Type.__name__ = "Integer32"
_AutifDestAddrType_Object = MibTableColumn
autifDestAddrType = _AutifDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 25),
    _AutifDestAddrType_Type()
)
autifDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifDestAddrType.setStatus("mandatory")
_AutifSockOptions_Type = Integer32
_AutifSockOptions_Object = MibTableColumn
autifSockOptions = _AutifSockOptions_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 26),
    _AutifSockOptions_Type()
)
autifSockOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifSockOptions.setStatus("mandatory")


class _AutifLNIA_Type(OctetString):
    """Custom type autifLNIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutifLNIA_Type.__name__ = "OctetString"
_AutifLNIA_Object = MibTableColumn
autifLNIA = _AutifLNIA_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 27),
    _AutifLNIA_Type()
)
autifLNIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifLNIA.setStatus("mandatory")


class _AutifLBName_Type(OctetString):
    """Custom type autifLBName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_AutifLBName_Type.__name__ = "OctetString"
_AutifLBName_Object = MibTableColumn
autifLBName = _AutifLBName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 28),
    _AutifLBName_Type()
)
autifLBName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifLBName.setStatus("mandatory")


class _AutifOFEPKeepAliveTimeout_Type(Integer32):
    """Custom type autifOFEPKeepAliveTimeout based on Integer32"""
    defaultValue = 150


_AutifOFEPKeepAliveTimeout_Object = MibTableColumn
autifOFEPKeepAliveTimeout = _AutifOFEPKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 29),
    _AutifOFEPKeepAliveTimeout_Type()
)
autifOFEPKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifOFEPKeepAliveTimeout.setStatus("mandatory")


class _AutifUserIdleTimeout_Type(Integer32):
    """Custom type autifUserIdleTimeout based on Integer32"""
    defaultValue = 0


_AutifUserIdleTimeout_Object = MibTableColumn
autifUserIdleTimeout = _AutifUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 30),
    _AutifUserIdleTimeout_Type()
)
autifUserIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifUserIdleTimeout.setStatus("mandatory")
_AutifXlatToSocket_Type = Integer32
_AutifXlatToSocket_Object = MibTableColumn
autifXlatToSocket = _AutifXlatToSocket_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 31),
    _AutifXlatToSocket_Type()
)
autifXlatToSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifXlatToSocket.setStatus("mandatory")
_AutifXlatFromSocket_Type = Integer32
_AutifXlatFromSocket_Object = MibTableColumn
autifXlatFromSocket = _AutifXlatFromSocket_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 32),
    _AutifXlatFromSocket_Type()
)
autifXlatFromSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autifXlatFromSocket.setStatus("mandatory")
_AutifRealToVTRoutingErrors_Type = Counter32
_AutifRealToVTRoutingErrors_Object = MibTableColumn
autifRealToVTRoutingErrors = _AutifRealToVTRoutingErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 33),
    _AutifRealToVTRoutingErrors_Type()
)
autifRealToVTRoutingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifRealToVTRoutingErrors.setStatus("mandatory")
_AutifVTToRealRoutingErrors_Type = Counter32
_AutifVTToRealRoutingErrors_Object = MibTableColumn
autifVTToRealRoutingErrors = _AutifVTToRealRoutingErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 34),
    _AutifVTToRealRoutingErrors_Type()
)
autifVTToRealRoutingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifVTToRealRoutingErrors.setStatus("mandatory")
_AutifRealToVTHashDepth_Type = Counter32
_AutifRealToVTHashDepth_Object = MibTableColumn
autifRealToVTHashDepth = _AutifRealToVTHashDepth_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 5, 2, 1, 35),
    _AutifRealToVTHashDepth_Type()
)
autifRealToVTHashDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autifRealToVTHashDepth.setStatus("mandatory")
_Apath_ObjectIdentity = ObjectIdentity
apath = _Apath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6)
)
_ApathNumEntries_Type = NonNegativeInteger
_ApathNumEntries_Object = MibScalar
apathNumEntries = _ApathNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 1),
    _ApathNumEntries_Type()
)
apathNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apathNumEntries.setStatus("mandatory")
_ApathTable_Object = MibTable
apathTable = _ApathTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    apathTable.setStatus("mandatory")
_ApathEntry_Object = MibTableRow
apathEntry = _ApathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1)
)
apathEntry.setIndexNames(
    (0, "TIGER", "apathIndex"),
)
if mibBuilder.loadTexts:
    apathEntry.setStatus("mandatory")


class _ApathIndex_Type(Integer32):
    """Custom type apathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApathIndex_Type.__name__ = "Integer32"
_ApathIndex_Object = MibTableColumn
apathIndex = _ApathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 1),
    _ApathIndex_Type()
)
apathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathIndex.setStatus("mandatory")


class _ApathType_Type(Integer32):
    """Custom type apathType based on Integer32"""
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
        *(("primary", 1),
          ("primary-mute", 3),
          ("primary-mute-xlat", 4),
          ("secondary", 2))
    )


_ApathType_Type.__name__ = "Integer32"
_ApathType_Object = MibTableColumn
apathType = _ApathType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 2),
    _ApathType_Type()
)
apathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathType.setStatus("mandatory")


class _ApathIdleTimerMax_Type(Integer32):
    """Custom type apathIdleTimerMax based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathIdleTimerMax_Type.__name__ = "Integer32"
_ApathIdleTimerMax_Object = MibTableColumn
apathIdleTimerMax = _ApathIdleTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 3),
    _ApathIdleTimerMax_Type()
)
apathIdleTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathIdleTimerMax.setStatus("mandatory")


class _ApathResponseTimerMax_Type(Integer32):
    """Custom type apathResponseTimerMax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApathResponseTimerMax_Type.__name__ = "Integer32"
_ApathResponseTimerMax_Object = MibTableColumn
apathResponseTimerMax = _ApathResponseTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 4),
    _ApathResponseTimerMax_Type()
)
apathResponseTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathResponseTimerMax.setStatus("mandatory")


class _ApathRetryCounterMax_Type(Integer32):
    """Custom type apathRetryCounterMax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApathRetryCounterMax_Type.__name__ = "Integer32"
_ApathRetryCounterMax_Object = MibTableColumn
apathRetryCounterMax = _ApathRetryCounterMax_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 5),
    _ApathRetryCounterMax_Type()
)
apathRetryCounterMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathRetryCounterMax.setStatus("mandatory")


class _ApathEndUserStatusEnable_Type(Integer32):
    """Custom type apathEndUserStatusEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApathEndUserStatusEnable_Type.__name__ = "Integer32"
_ApathEndUserStatusEnable_Object = MibTableColumn
apathEndUserStatusEnable = _ApathEndUserStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 6),
    _ApathEndUserStatusEnable_Type()
)
apathEndUserStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathEndUserStatusEnable.setStatus("mandatory")


class _ApathTrafficIdleTimer_Type(Integer32):
    """Custom type apathTrafficIdleTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApathTrafficIdleTimer_Type.__name__ = "Integer32"
_ApathTrafficIdleTimer_Object = MibTableColumn
apathTrafficIdleTimer = _ApathTrafficIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 7),
    _ApathTrafficIdleTimer_Type()
)
apathTrafficIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathTrafficIdleTimer.setStatus("mandatory")


class _ApathConnectTimerMax_Type(Integer32):
    """Custom type apathConnectTimerMax based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathConnectTimerMax_Type.__name__ = "Integer32"
_ApathConnectTimerMax_Object = MibTableColumn
apathConnectTimerMax = _ApathConnectTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 8),
    _ApathConnectTimerMax_Type()
)
apathConnectTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathConnectTimerMax.setStatus("mandatory")


class _ApathPathUpMsg_Type(OctetString):
    """Custom type apathPathUpMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApathPathUpMsg_Type.__name__ = "OctetString"
_ApathPathUpMsg_Object = MibTableColumn
apathPathUpMsg = _ApathPathUpMsg_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 2, 1, 9),
    _ApathPathUpMsg_Type()
)
apathPathUpMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathPathUpMsg.setStatus("mandatory")
_ApathUserNumEntries_Type = NonNegativeInteger
_ApathUserNumEntries_Object = MibScalar
apathUserNumEntries = _ApathUserNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 3),
    _ApathUserNumEntries_Type()
)
apathUserNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apathUserNumEntries.setStatus("mandatory")
_ApathUserTable_Object = MibTable
apathUserTable = _ApathUserTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    apathUserTable.setStatus("mandatory")
_ApathUserEntry_Object = MibTableRow
apathUserEntry = _ApathUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1)
)
apathUserEntry.setIndexNames(
    (0, "TIGER", "apathUserIndex"),
)
if mibBuilder.loadTexts:
    apathUserEntry.setStatus("mandatory")


class _ApathUserIndex_Type(Integer32):
    """Custom type apathUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApathUserIndex_Type.__name__ = "Integer32"
_ApathUserIndex_Object = MibTableColumn
apathUserIndex = _ApathUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 1),
    _ApathUserIndex_Type()
)
apathUserIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserIndex.setStatus("mandatory")


class _ApathUserApathOperation_Type(Integer32):
    """Custom type apathUserApathOperation based on Integer32"""
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
        *(("avoidSwitching", 3),
          ("mainPrefered", 1),
          ("switchToBestPath", 2))
    )


_ApathUserApathOperation_Type.__name__ = "Integer32"
_ApathUserApathOperation_Object = MibTableColumn
apathUserApathOperation = _ApathUserApathOperation_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 2),
    _ApathUserApathOperation_Type()
)
apathUserApathOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserApathOperation.setStatus("mandatory")


class _ApathUserMainApathIndex_Type(Integer32):
    """Custom type apathUserMainApathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathUserMainApathIndex_Type.__name__ = "Integer32"
_ApathUserMainApathIndex_Object = MibTableColumn
apathUserMainApathIndex = _ApathUserMainApathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 3),
    _ApathUserMainApathIndex_Type()
)
apathUserMainApathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserMainApathIndex.setStatus("mandatory")


class _ApathUserAlt1ApathIndex_Type(Integer32):
    """Custom type apathUserAlt1ApathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathUserAlt1ApathIndex_Type.__name__ = "Integer32"
_ApathUserAlt1ApathIndex_Object = MibTableColumn
apathUserAlt1ApathIndex = _ApathUserAlt1ApathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 4),
    _ApathUserAlt1ApathIndex_Type()
)
apathUserAlt1ApathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserAlt1ApathIndex.setStatus("mandatory")


class _ApathUserAlt2ApathIndex_Type(Integer32):
    """Custom type apathUserAlt2ApathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathUserAlt2ApathIndex_Type.__name__ = "Integer32"
_ApathUserAlt2ApathIndex_Object = MibTableColumn
apathUserAlt2ApathIndex = _ApathUserAlt2ApathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 5),
    _ApathUserAlt2ApathIndex_Type()
)
apathUserAlt2ApathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserAlt2ApathIndex.setStatus("mandatory")


class _ApathUserAlt3ApathIndex_Type(Integer32):
    """Custom type apathUserAlt3ApathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApathUserAlt3ApathIndex_Type.__name__ = "Integer32"
_ApathUserAlt3ApathIndex_Object = MibTableColumn
apathUserAlt3ApathIndex = _ApathUserAlt3ApathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 6),
    _ApathUserAlt3ApathIndex_Type()
)
apathUserAlt3ApathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserAlt3ApathIndex.setStatus("mandatory")


class _ApathUserType_Type(Integer32):
    """Custom type apathUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alc", 1),
          ("u100", 2),
          ("x2x", 3))
    )


_ApathUserType_Type.__name__ = "Integer32"
_ApathUserType_Object = MibTableColumn
apathUserType = _ApathUserType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 7),
    _ApathUserType_Type()
)
apathUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserType.setStatus("mandatory")


class _ApathUserDevStatusEnable_Type(Integer32):
    """Custom type apathUserDevStatusEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApathUserDevStatusEnable_Type.__name__ = "Integer32"
_ApathUserDevStatusEnable_Object = MibTableColumn
apathUserDevStatusEnable = _ApathUserDevStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 10),
    _ApathUserDevStatusEnable_Type()
)
apathUserDevStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserDevStatusEnable.setStatus("mandatory")


class _ApathUserAuxilliaryInfo_Type(OctetString):
    """Custom type apathUserAuxilliaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ApathUserAuxilliaryInfo_Type.__name__ = "OctetString"
_ApathUserAuxilliaryInfo_Object = MibTableColumn
apathUserAuxilliaryInfo = _ApathUserAuxilliaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 6, 4, 1, 11),
    _ApathUserAuxilliaryInfo_Type()
)
apathUserAuxilliaryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apathUserAuxilliaryInfo.setStatus("mandatory")
_Svcmsg_ObjectIdentity = ObjectIdentity
svcmsg = _Svcmsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7)
)
_SvcmsgNumEntries_Type = NonNegativeInteger
_SvcmsgNumEntries_Object = MibScalar
svcmsgNumEntries = _SvcmsgNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 1),
    _SvcmsgNumEntries_Type()
)
svcmsgNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcmsgNumEntries.setStatus("mandatory")
_SvcmsgTable_Object = MibTable
svcmsgTable = _SvcmsgTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    svcmsgTable.setStatus("mandatory")
_SvcmsgEntry_Object = MibTableRow
svcmsgEntry = _SvcmsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1)
)
svcmsgEntry.setIndexNames(
    (0, "TIGER", "svcmsgIndex"),
)
if mibBuilder.loadTexts:
    svcmsgEntry.setStatus("mandatory")


class _SvcmsgIndex_Type(Integer32):
    """Custom type svcmsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SvcmsgIndex_Type.__name__ = "Integer32"
_SvcmsgIndex_Object = MibTableColumn
svcmsgIndex = _SvcmsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 1),
    _SvcmsgIndex_Type()
)
svcmsgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgIndex.setStatus("mandatory")


class _SvcmsgDescription_Type(OctetString):
    """Custom type svcmsgDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDescription_Type.__name__ = "OctetString"
_SvcmsgDescription_Object = MibTableColumn
svcmsgDescription = _SvcmsgDescription_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 2),
    _SvcmsgDescription_Type()
)
svcmsgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDescription.setStatus("mandatory")


class _SvcmsgNetDown_Type(OctetString):
    """Custom type svcmsgNetDown based on OctetString"""
    defaultValue = OctetString("Network Down")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgNetDown_Type.__name__ = "OctetString"
_SvcmsgNetDown_Object = MibTableColumn
svcmsgNetDown = _SvcmsgNetDown_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 3),
    _SvcmsgNetDown_Type()
)
svcmsgNetDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgNetDown.setStatus("mandatory")


class _SvcmsgNetUp_Type(OctetString):
    """Custom type svcmsgNetUp based on OctetString"""
    defaultValue = OctetString("Network Up")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgNetUp_Type.__name__ = "OctetString"
_SvcmsgNetUp_Object = MibTableColumn
svcmsgNetUp = _SvcmsgNetUp_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 4),
    _SvcmsgNetUp_Type()
)
svcmsgNetUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgNetUp.setStatus("mandatory")


class _SvcmsgConnecting_Type(OctetString):
    """Custom type svcmsgConnecting based on OctetString"""
    defaultValue = OctetString("Connecting")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgConnecting_Type.__name__ = "OctetString"
_SvcmsgConnecting_Object = MibTableColumn
svcmsgConnecting = _SvcmsgConnecting_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 5),
    _SvcmsgConnecting_Type()
)
svcmsgConnecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgConnecting.setStatus("mandatory")


class _SvcmsgConnected_Type(OctetString):
    """Custom type svcmsgConnected based on OctetString"""
    defaultValue = OctetString("Connected")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgConnected_Type.__name__ = "OctetString"
_SvcmsgConnected_Object = MibTableColumn
svcmsgConnected = _SvcmsgConnected_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 6),
    _SvcmsgConnected_Type()
)
svcmsgConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgConnected.setStatus("mandatory")


class _SvcmsgIdle_Type(OctetString):
    """Custom type svcmsgIdle based on OctetString"""
    defaultValue = OctetString("Idle")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgIdle_Type.__name__ = "OctetString"
_SvcmsgIdle_Object = MibTableColumn
svcmsgIdle = _SvcmsgIdle_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 7),
    _SvcmsgIdle_Type()
)
svcmsgIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgIdle.setStatus("mandatory")


class _SvcmsgDisconnecting_Type(OctetString):
    """Custom type svcmsgDisconnecting based on OctetString"""
    defaultValue = OctetString("Disconnecting")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDisconnecting_Type.__name__ = "OctetString"
_SvcmsgDisconnecting_Object = MibTableColumn
svcmsgDisconnecting = _SvcmsgDisconnecting_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 8),
    _SvcmsgDisconnecting_Type()
)
svcmsgDisconnecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDisconnecting.setStatus("mandatory")


class _SvcmsgDisconnected_Type(OctetString):
    """Custom type svcmsgDisconnected based on OctetString"""
    defaultValue = OctetString("Disconnected")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDisconnected_Type.__name__ = "OctetString"
_SvcmsgDisconnected_Object = MibTableColumn
svcmsgDisconnected = _SvcmsgDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 9),
    _SvcmsgDisconnected_Type()
)
svcmsgDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDisconnected.setStatus("mandatory")


class _SvcmsgDiscRestart_Type(OctetString):
    """Custom type svcmsgDiscRestart based on OctetString"""
    defaultValue = OctetString("Disconnected/Restart")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscRestart_Type.__name__ = "OctetString"
_SvcmsgDiscRestart_Object = MibTableColumn
svcmsgDiscRestart = _SvcmsgDiscRestart_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 10),
    _SvcmsgDiscRestart_Type()
)
svcmsgDiscRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscRestart.setStatus("mandatory")


class _SvcmsgDiscUser_Type(OctetString):
    """Custom type svcmsgDiscUser based on OctetString"""
    defaultValue = OctetString("Disconnected/User")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscUser_Type.__name__ = "OctetString"
_SvcmsgDiscUser_Object = MibTableColumn
svcmsgDiscUser = _SvcmsgDiscUser_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 11),
    _SvcmsgDiscUser_Type()
)
svcmsgDiscUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscUser.setStatus("mandatory")


class _SvcmsgDiscMgmt_Type(OctetString):
    """Custom type svcmsgDiscMgmt based on OctetString"""
    defaultValue = OctetString("Disconnected/Mgmt")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscMgmt_Type.__name__ = "OctetString"
_SvcmsgDiscMgmt_Object = MibTableColumn
svcmsgDiscMgmt = _SvcmsgDiscMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 12),
    _SvcmsgDiscMgmt_Type()
)
svcmsgDiscMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscMgmt.setStatus("mandatory")


class _SvcmsgDiscBusy_Type(OctetString):
    """Custom type svcmsgDiscBusy based on OctetString"""
    defaultValue = OctetString("Disconnected/Busy")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscBusy_Type.__name__ = "OctetString"
_SvcmsgDiscBusy_Object = MibTableColumn
svcmsgDiscBusy = _SvcmsgDiscBusy_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 13),
    _SvcmsgDiscBusy_Type()
)
svcmsgDiscBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscBusy.setStatus("mandatory")


class _SvcmsgDiscRPErr_Type(OctetString):
    """Custom type svcmsgDiscRPErr based on OctetString"""
    defaultValue = OctetString("Disconnected/Remote Procedure Error")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscRPErr_Type.__name__ = "OctetString"
_SvcmsgDiscRPErr_Object = MibTableColumn
svcmsgDiscRPErr = _SvcmsgDiscRPErr_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 14),
    _SvcmsgDiscRPErr_Type()
)
svcmsgDiscRPErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscRPErr.setStatus("mandatory")


class _SvcmsgDiscLPErr_Type(OctetString):
    """Custom type svcmsgDiscLPErr based on OctetString"""
    defaultValue = OctetString("Disconnected/Local Procedure Error")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscLPErr_Type.__name__ = "OctetString"
_SvcmsgDiscLPErr_Object = MibTableColumn
svcmsgDiscLPErr = _SvcmsgDiscLPErr_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 15),
    _SvcmsgDiscLPErr_Type()
)
svcmsgDiscLPErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscLPErr.setStatus("mandatory")


class _SvcmsgDiscCongest_Type(OctetString):
    """Custom type svcmsgDiscCongest based on OctetString"""
    defaultValue = OctetString("Disconnected/Congestion")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscCongest_Type.__name__ = "OctetString"
_SvcmsgDiscCongest_Object = MibTableColumn
svcmsgDiscCongest = _SvcmsgDiscCongest_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 16),
    _SvcmsgDiscCongest_Type()
)
svcmsgDiscCongest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscCongest.setStatus("mandatory")


class _SvcmsgDiscNotOb_Type(OctetString):
    """Custom type svcmsgDiscNotOb based on OctetString"""
    defaultValue = OctetString("Disconnected/Not Obtainable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscNotOb_Type.__name__ = "OctetString"
_SvcmsgDiscNotOb_Object = MibTableColumn
svcmsgDiscNotOb = _SvcmsgDiscNotOb_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 17),
    _SvcmsgDiscNotOb_Type()
)
svcmsgDiscNotOb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscNotOb.setStatus("mandatory")


class _SvcmsgDiscOutOrder_Type(OctetString):
    """Custom type svcmsgDiscOutOrder based on OctetString"""
    defaultValue = OctetString("Disconnected/Out of Order")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscOutOrder_Type.__name__ = "OctetString"
_SvcmsgDiscOutOrder_Object = MibTableColumn
svcmsgDiscOutOrder = _SvcmsgDiscOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 18),
    _SvcmsgDiscOutOrder_Type()
)
svcmsgDiscOutOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscOutOrder.setStatus("mandatory")


class _SvcmsgDiscInvFac_Type(OctetString):
    """Custom type svcmsgDiscInvFac based on OctetString"""
    defaultValue = OctetString("Disconnected/Invalid Facility")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscInvFac_Type.__name__ = "OctetString"
_SvcmsgDiscInvFac_Object = MibTableColumn
svcmsgDiscInvFac = _SvcmsgDiscInvFac_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 19),
    _SvcmsgDiscInvFac_Type()
)
svcmsgDiscInvFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscInvFac.setStatus("mandatory")


class _SvcmsgDiscAcsBar_Type(OctetString):
    """Custom type svcmsgDiscAcsBar based on OctetString"""
    defaultValue = OctetString("Disconnected/Access Barred")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscAcsBar_Type.__name__ = "OctetString"
_SvcmsgDiscAcsBar_Object = MibTableColumn
svcmsgDiscAcsBar = _SvcmsgDiscAcsBar_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 20),
    _SvcmsgDiscAcsBar_Type()
)
svcmsgDiscAcsBar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscAcsBar.setStatus("mandatory")


class _SvcmsgDiscRvsCharge_Type(OctetString):
    """Custom type svcmsgDiscRvsCharge based on OctetString"""
    defaultValue = OctetString("Disconnected/Reverse Charge not accepted")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscRvsCharge_Type.__name__ = "OctetString"
_SvcmsgDiscRvsCharge_Object = MibTableColumn
svcmsgDiscRvsCharge = _SvcmsgDiscRvsCharge_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 21),
    _SvcmsgDiscRvsCharge_Type()
)
svcmsgDiscRvsCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscRvsCharge.setStatus("mandatory")


class _SvcmsgDiscIncDest_Type(OctetString):
    """Custom type svcmsgDiscIncDest based on OctetString"""
    defaultValue = OctetString("Disconnected/Invalid Destination")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscIncDest_Type.__name__ = "OctetString"
_SvcmsgDiscIncDest_Object = MibTableColumn
svcmsgDiscIncDest = _SvcmsgDiscIncDest_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 22),
    _SvcmsgDiscIncDest_Type()
)
svcmsgDiscIncDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscIncDest.setStatus("mandatory")


class _SvcmsgDiscNoTraf_Type(OctetString):
    """Custom type svcmsgDiscNoTraf based on OctetString"""
    defaultValue = OctetString("Disconnected/No Traffic")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgDiscNoTraf_Type.__name__ = "OctetString"
_SvcmsgDiscNoTraf_Object = MibTableColumn
svcmsgDiscNoTraf = _SvcmsgDiscNoTraf_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 23),
    _SvcmsgDiscNoTraf_Type()
)
svcmsgDiscNoTraf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgDiscNoTraf.setStatus("mandatory")


class _SvcmsgUpAgain_Type(OctetString):
    """Custom type svcmsgUpAgain based on OctetString"""
    defaultValue = OctetString("Up Again")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgUpAgain_Type.__name__ = "OctetString"
_SvcmsgUpAgain_Object = MibTableColumn
svcmsgUpAgain = _SvcmsgUpAgain_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 24),
    _SvcmsgUpAgain_Type()
)
svcmsgUpAgain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgUpAgain.setStatus("mandatory")


class _SvcmsgNoRoute_Type(OctetString):
    """Custom type svcmsgNoRoute based on OctetString"""
    defaultValue = OctetString("No Route To Host")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgNoRoute_Type.__name__ = "OctetString"
_SvcmsgNoRoute_Object = MibTableColumn
svcmsgNoRoute = _SvcmsgNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 25),
    _SvcmsgNoRoute_Type()
)
svcmsgNoRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgNoRoute.setStatus("mandatory")


class _SvcmsgOverLength_Type(OctetString):
    """Custom type svcmsgOverLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgOverLength_Type.__name__ = "OctetString"
_SvcmsgOverLength_Object = MibTableColumn
svcmsgOverLength = _SvcmsgOverLength_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 26),
    _SvcmsgOverLength_Type()
)
svcmsgOverLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgOverLength.setStatus("mandatory")


class _SvcmsgCongestion_Type(OctetString):
    """Custom type svcmsgCongestion based on OctetString"""
    defaultValue = OctetString("Congestion")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgCongestion_Type.__name__ = "OctetString"
_SvcmsgCongestion_Object = MibTableColumn
svcmsgCongestion = _SvcmsgCongestion_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 27),
    _SvcmsgCongestion_Type()
)
svcmsgCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgCongestion.setStatus("mandatory")


class _SvcmsgHostUnreach_Type(OctetString):
    """Custom type svcmsgHostUnreach based on OctetString"""
    defaultValue = OctetString("Host Unreachable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgHostUnreach_Type.__name__ = "OctetString"
_SvcmsgHostUnreach_Object = MibTableColumn
svcmsgHostUnreach = _SvcmsgHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 28),
    _SvcmsgHostUnreach_Type()
)
svcmsgHostUnreach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgHostUnreach.setStatus("mandatory")


class _SvcmsgZeroLength_Type(OctetString):
    """Custom type svcmsgZeroLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcmsgZeroLength_Type.__name__ = "OctetString"
_SvcmsgZeroLength_Object = MibTableColumn
svcmsgZeroLength = _SvcmsgZeroLength_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 7, 2, 1, 29),
    _SvcmsgZeroLength_Type()
)
svcmsgZeroLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcmsgZeroLength.setStatus("mandatory")
_Bootp_ObjectIdentity = ObjectIdentity
bootp = _Bootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8)
)
_BootpNumEntries_Type = NonNegativeInteger
_BootpNumEntries_Object = MibScalar
bootpNumEntries = _BootpNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 1),
    _BootpNumEntries_Type()
)
bootpNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpNumEntries.setStatus("mandatory")
_BootpTable_Object = MibTable
bootpTable = _BootpTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    bootpTable.setStatus("mandatory")
_BootpEntry_Object = MibTableRow
bootpEntry = _BootpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1)
)
bootpEntry.setIndexNames(
    (0, "TIGER", "bootpIndex"),
)
if mibBuilder.loadTexts:
    bootpEntry.setStatus("mandatory")


class _BootpIndex_Type(Integer32):
    """Custom type bootpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_BootpIndex_Type.__name__ = "Integer32"
_BootpIndex_Object = MibTableColumn
bootpIndex = _BootpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 1),
    _BootpIndex_Type()
)
bootpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIndex.setStatus("mandatory")


class _BootpServerName_Type(OctetString):
    """Custom type bootpServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootpServerName_Type.__name__ = "OctetString"
_BootpServerName_Object = MibTableColumn
bootpServerName = _BootpServerName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 2),
    _BootpServerName_Type()
)
bootpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpServerName.setStatus("mandatory")


class _BootpUserName_Type(OctetString):
    """Custom type bootpUserName based on OctetString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootpUserName_Type.__name__ = "OctetString"
_BootpUserName_Object = MibTableColumn
bootpUserName = _BootpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 3),
    _BootpUserName_Type()
)
bootpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpUserName.setStatus("mandatory")


class _BootpPassword_Type(OctetString):
    """Custom type bootpPassword based on OctetString"""
    defaultValue = OctetString("guest")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootpPassword_Type.__name__ = "OctetString"
_BootpPassword_Object = MibTableColumn
bootpPassword = _BootpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 4),
    _BootpPassword_Type()
)
bootpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpPassword.setStatus("mandatory")


class _BootpRemoteFile_Type(OctetString):
    """Custom type bootpRemoteFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootpRemoteFile_Type.__name__ = "OctetString"
_BootpRemoteFile_Object = MibTableColumn
bootpRemoteFile = _BootpRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 5),
    _BootpRemoteFile_Type()
)
bootpRemoteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpRemoteFile.setStatus("mandatory")


class _BootpLocalFile_Type(OctetString):
    """Custom type bootpLocalFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootpLocalFile_Type.__name__ = "OctetString"
_BootpLocalFile_Object = MibTableColumn
bootpLocalFile = _BootpLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 8, 2, 1, 6),
    _BootpLocalFile_Type()
)
bootpLocalFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpLocalFile.setStatus("mandatory")
_Mount_ObjectIdentity = ObjectIdentity
mount = _Mount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9)
)
_MountNumEntries_Type = NonNegativeInteger
_MountNumEntries_Object = MibScalar
mountNumEntries = _MountNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 1),
    _MountNumEntries_Type()
)
mountNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountNumEntries.setStatus("mandatory")
_MountTable_Object = MibTable
mountTable = _MountTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    mountTable.setStatus("mandatory")
_MountEntry_Object = MibTableRow
mountEntry = _MountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1)
)
mountEntry.setIndexNames(
    (0, "TIGER", "mountIndex"),
)
if mibBuilder.loadTexts:
    mountEntry.setStatus("mandatory")


class _MountIndex_Type(Integer32):
    """Custom type mountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MountIndex_Type.__name__ = "Integer32"
_MountIndex_Object = MibTableColumn
mountIndex = _MountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1, 1),
    _MountIndex_Type()
)
mountIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mountIndex.setStatus("mandatory")


class _MountRemotePath_Type(OctetString):
    """Custom type mountRemotePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MountRemotePath_Type.__name__ = "OctetString"
_MountRemotePath_Object = MibTableColumn
mountRemotePath = _MountRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1, 2),
    _MountRemotePath_Type()
)
mountRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mountRemotePath.setStatus("mandatory")


class _MountLocalPath_Type(OctetString):
    """Custom type mountLocalPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MountLocalPath_Type.__name__ = "OctetString"
_MountLocalPath_Object = MibTableColumn
mountLocalPath = _MountLocalPath_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1, 3),
    _MountLocalPath_Type()
)
mountLocalPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mountLocalPath.setStatus("mandatory")


class _MountMode_Type(Integer32):
    """Custom type mountMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_MountMode_Type.__name__ = "Integer32"
_MountMode_Object = MibTableColumn
mountMode = _MountMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1, 4),
    _MountMode_Type()
)
mountMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mountMode.setStatus("mandatory")


class _MountRemoteInfo_Type(Integer32):
    """Custom type mountRemoteInfo based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("connected-NoAccess", 5),
          ("connected-ReadOnly", 6),
          ("connected-ReadWrite", 8),
          ("connected-WriteOnly", 7),
          ("notConnected-NoAccess", 1),
          ("notConnected-ReadOnly", 2),
          ("notConnected-ReadWrite", 4),
          ("notConnected-WriteOnly", 3))
    )


_MountRemoteInfo_Type.__name__ = "Integer32"
_MountRemoteInfo_Object = MibTableColumn
mountRemoteInfo = _MountRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 9, 2, 1, 5),
    _MountRemoteInfo_Type()
)
mountRemoteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountRemoteInfo.setStatus("mandatory")
_DnsRes_ObjectIdentity = ObjectIdentity
dnsRes = _DnsRes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10)
)
_DnsResLocalResolves_Type = Counter32
_DnsResLocalResolves_Object = MibScalar
dnsResLocalResolves = _DnsResLocalResolves_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 1),
    _DnsResLocalResolves_Type()
)
dnsResLocalResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResLocalResolves.setStatus("mandatory")
_DnsResCacheFull_Type = Counter32
_DnsResCacheFull_Object = MibScalar
dnsResCacheFull = _DnsResCacheFull_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 2),
    _DnsResCacheFull_Type()
)
dnsResCacheFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheFull.setStatus("mandatory")
_DnsResQueueFull_Type = Counter32
_DnsResQueueFull_Object = MibScalar
dnsResQueueFull = _DnsResQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 3),
    _DnsResQueueFull_Type()
)
dnsResQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResQueueFull.setStatus("mandatory")


class _DnsResClearCache_Type(Integer32):
    """Custom type dnsResClearCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_DnsResClearCache_Type.__name__ = "Integer32"
_DnsResClearCache_Object = MibScalar
dnsResClearCache = _DnsResClearCache_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 4),
    _DnsResClearCache_Type()
)
dnsResClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResClearCache.setStatus("mandatory")


class _DnsResConfigMaxCnames_Type(Integer32):
    """Custom type dnsResConfigMaxCnames based on Integer32"""
    defaultValue = 16


_DnsResConfigMaxCnames_Object = MibScalar
dnsResConfigMaxCnames = _DnsResConfigMaxCnames_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 5),
    _DnsResConfigMaxCnames_Type()
)
dnsResConfigMaxCnames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResConfigMaxCnames.setStatus("mandatory")
_DnsResNumHosts_Type = NonNegativeInteger
_DnsResNumHosts_Object = MibScalar
dnsResNumHosts = _DnsResNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 6),
    _DnsResNumHosts_Type()
)
dnsResNumHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNumHosts.setStatus("mandatory")
_DnsResTable_Object = MibTable
dnsResTable = _DnsResTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7)
)
if mibBuilder.loadTexts:
    dnsResTable.setStatus("mandatory")
_DnsResEntry_Object = MibTableRow
dnsResEntry = _DnsResEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1)
)
dnsResEntry.setIndexNames(
    (0, "TIGER", "dnsResServerIP"),
)
if mibBuilder.loadTexts:
    dnsResEntry.setStatus("mandatory")
_DnsResServerIP_Type = IpAddress
_DnsResServerIP_Object = MibTableColumn
dnsResServerIP = _DnsResServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 1),
    _DnsResServerIP_Type()
)
dnsResServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResServerIP.setStatus("mandatory")


class _DnsResServerName_Type(OctetString):
    """Custom type dnsResServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DnsResServerName_Type.__name__ = "OctetString"
_DnsResServerName_Object = MibTableColumn
dnsResServerName = _DnsResServerName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 2),
    _DnsResServerName_Type()
)
dnsResServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResServerName.setStatus("mandatory")
_DnsResQueriesSent_Type = Counter32
_DnsResQueriesSent_Object = MibTableColumn
dnsResQueriesSent = _DnsResQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 3),
    _DnsResQueriesSent_Type()
)
dnsResQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResQueriesSent.setStatus("mandatory")
_DnsResSendErrors_Type = Counter32
_DnsResSendErrors_Object = MibTableColumn
dnsResSendErrors = _DnsResSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 4),
    _DnsResSendErrors_Type()
)
dnsResSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResSendErrors.setStatus("mandatory")
_DnsResGoodResponses_Type = Counter32
_DnsResGoodResponses_Object = MibTableColumn
dnsResGoodResponses = _DnsResGoodResponses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 5),
    _DnsResGoodResponses_Type()
)
dnsResGoodResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResGoodResponses.setStatus("mandatory")
_DnsResTimeouts_Type = Counter32
_DnsResTimeouts_Object = MibTableColumn
dnsResTimeouts = _DnsResTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 6),
    _DnsResTimeouts_Type()
)
dnsResTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResTimeouts.setStatus("mandatory")
_DnsResBadResponses_Type = Counter32
_DnsResBadResponses_Object = MibTableColumn
dnsResBadResponses = _DnsResBadResponses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 7),
    _DnsResBadResponses_Type()
)
dnsResBadResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResBadResponses.setStatus("mandatory")


class _DnsResCmd_Type(Integer32):
    """Custom type dnsResCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("noop", 1))
    )


_DnsResCmd_Type.__name__ = "Integer32"
_DnsResCmd_Object = MibTableColumn
dnsResCmd = _DnsResCmd_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 7, 1, 8),
    _DnsResCmd_Type()
)
dnsResCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResCmd.setStatus("mandatory")


class _DnsResCacheNumEntries_Type(Integer32):
    """Custom type dnsResCacheNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DnsResCacheNumEntries_Type.__name__ = "Integer32"
_DnsResCacheNumEntries_Object = MibScalar
dnsResCacheNumEntries = _DnsResCacheNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 8),
    _DnsResCacheNumEntries_Type()
)
dnsResCacheNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheNumEntries.setStatus("mandatory")
_DnsResCacheTable_Object = MibTable
dnsResCacheTable = _DnsResCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9)
)
if mibBuilder.loadTexts:
    dnsResCacheTable.setStatus("mandatory")
_DnsResCacheEntry_Object = MibTableRow
dnsResCacheEntry = _DnsResCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1)
)
dnsResCacheEntry.setIndexNames(
    (0, "TIGER", "dnsResCacheIpAddress"),
)
if mibBuilder.loadTexts:
    dnsResCacheEntry.setStatus("mandatory")


class _DnsResCacheHostName_Type(OctetString):
    """Custom type dnsResCacheHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DnsResCacheHostName_Type.__name__ = "OctetString"
_DnsResCacheHostName_Object = MibTableColumn
dnsResCacheHostName = _DnsResCacheHostName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1, 1),
    _DnsResCacheHostName_Type()
)
dnsResCacheHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheHostName.setStatus("mandatory")
_DnsResCacheIpAddress_Type = IpAddress
_DnsResCacheIpAddress_Object = MibTableColumn
dnsResCacheIpAddress = _DnsResCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1, 2),
    _DnsResCacheIpAddress_Type()
)
dnsResCacheIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheIpAddress.setStatus("mandatory")
_DnsResCacheRRTTL_Type = Gauge32
_DnsResCacheRRTTL_Object = MibTableColumn
dnsResCacheRRTTL = _DnsResCacheRRTTL_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1, 3),
    _DnsResCacheRRTTL_Type()
)
dnsResCacheRRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRTTL.setStatus("mandatory")
_DnsResCacheRRElapsedTTL_Type = Gauge32
_DnsResCacheRRElapsedTTL_Object = MibTableColumn
dnsResCacheRRElapsedTTL = _DnsResCacheRRElapsedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1, 4),
    _DnsResCacheRRElapsedTTL_Type()
)
dnsResCacheRRElapsedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRElapsedTTL.setStatus("mandatory")
_DnsResCacheRRSource_Type = IpAddress
_DnsResCacheRRSource_Object = MibTableColumn
dnsResCacheRRSource = _DnsResCacheRRSource_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 10, 9, 1, 5),
    _DnsResCacheRRSource_Type()
)
dnsResCacheRRSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRSource.setStatus("mandatory")
_Vt_ObjectIdentity = ObjectIdentity
vt = _Vt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11)
)
_VtTable_Object = MibTable
vtTable = _VtTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    vtTable.setStatus("mandatory")
_VtEntry_Object = MibTableRow
vtEntry = _VtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1)
)
vtEntry.setIndexNames(
    (0, "TIGER", "vtAutifIndex"),
    (0, "TIGER", "vtRealLnIaTa"),
)
if mibBuilder.loadTexts:
    vtEntry.setStatus("mandatory")
_VtAutifIndex_Type = Integer32
_VtAutifIndex_Object = MibTableColumn
vtAutifIndex = _VtAutifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 1),
    _VtAutifIndex_Type()
)
vtAutifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtAutifIndex.setStatus("mandatory")


class _VtRealLnIaTa_Type(OctetString):
    """Custom type vtRealLnIaTa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VtRealLnIaTa_Type.__name__ = "OctetString"
_VtRealLnIaTa_Object = MibTableColumn
vtRealLnIaTa = _VtRealLnIaTa_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 2),
    _VtRealLnIaTa_Type()
)
vtRealLnIaTa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtRealLnIaTa.setStatus("mandatory")


class _VtLnIaTa_Type(OctetString):
    """Custom type vtLnIaTa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VtLnIaTa_Type.__name__ = "OctetString"
_VtLnIaTa_Object = MibTableColumn
vtLnIaTa = _VtLnIaTa_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 3),
    _VtLnIaTa_Type()
)
vtLnIaTa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtLnIaTa.setStatus("mandatory")


class _VtOptionsDOD_Type(Integer32):
    """Custom type vtOptionsDOD based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect-always", 1),
          ("connect-on-data", 2))
    )


_VtOptionsDOD_Type.__name__ = "Integer32"
_VtOptionsDOD_Object = MibTableColumn
vtOptionsDOD = _VtOptionsDOD_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 4),
    _VtOptionsDOD_Type()
)
vtOptionsDOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtOptionsDOD.setStatus("mandatory")


class _VtOptionsPrinter_Type(Integer32):
    """Custom type vtOptionsPrinter based on Integer32"""
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
        *(("free", 3),
          ("printer", 2),
          ("terminal", 1))
    )


_VtOptionsPrinter_Type.__name__ = "Integer32"
_VtOptionsPrinter_Object = MibTableColumn
vtOptionsPrinter = _VtOptionsPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 5),
    _VtOptionsPrinter_Type()
)
vtOptionsPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtOptionsPrinter.setStatus("mandatory")


class _VtOptionsClass_Type(Integer32):
    """Custom type vtOptionsClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("by-class", 2),
          ("by-lniata", 1))
    )


_VtOptionsClass_Type.__name__ = "Integer32"
_VtOptionsClass_Object = MibTableColumn
vtOptionsClass = _VtOptionsClass_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 6),
    _VtOptionsClass_Type()
)
vtOptionsClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtOptionsClass.setStatus("mandatory")


class _VtCommand_Type(Integer32):
    """Custom type vtCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_VtCommand_Type.__name__ = "Integer32"
_VtCommand_Object = MibTableColumn
vtCommand = _VtCommand_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 7),
    _VtCommand_Type()
)
vtCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtCommand.setStatus("mandatory")


class _VtClassName_Type(OctetString):
    """Custom type vtClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VtClassName_Type.__name__ = "OctetString"
_VtClassName_Object = MibTableColumn
vtClassName = _VtClassName_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 8),
    _VtClassName_Type()
)
vtClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtClassName.setStatus("mandatory")


class _VtState_Type(Integer32):
    """Custom type vtState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("vts-con-lb", 3),
          ("vts-con-ofep", 7),
          ("vts-dod-wait", 2),
          ("vts-gen-fail", 6),
          ("vts-init", 1),
          ("vts-lb-config", 5),
          ("vts-lb-dialog", 4),
          ("vts-ofep-config", 9),
          ("vts-ofep-dialog", 8),
          ("vts-ofep-shutdown", 11),
          ("vts-ofep-up", 10))
    )


_VtState_Type.__name__ = "Integer32"
_VtState_Object = MibTableColumn
vtState = _VtState_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 9),
    _VtState_Type()
)
vtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtState.setStatus("mandatory")


class _VtFailReason_Type(Integer32):
    """Custom type vtFailReason based on Integer32"""
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
        *(("vte-cap-off", 9),
          ("vte-deactivate", 8),
          ("vte-err-gen", 1),
          ("vte-err-idle-timeout", 7),
          ("vte-err-ka-timeout", 4),
          ("vte-err-lb", 5),
          ("vte-err-ofep", 6),
          ("vte-err-sock-down", 2),
          ("vte-err-timeout", 3))
    )


_VtFailReason_Type.__name__ = "Integer32"
_VtFailReason_Object = MibTableColumn
vtFailReason = _VtFailReason_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 10),
    _VtFailReason_Type()
)
vtFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtFailReason.setStatus("mandatory")


class _VtFailString_Type(OctetString):
    """Custom type vtFailString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_VtFailString_Type.__name__ = "OctetString"
_VtFailString_Object = MibTableColumn
vtFailString = _VtFailString_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 11),
    _VtFailString_Type()
)
vtFailString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtFailString.setStatus("mandatory")


class _VtLBToken_Type(OctetString):
    """Custom type vtLBToken based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VtLBToken_Type.__name__ = "OctetString"
_VtLBToken_Object = MibTableColumn
vtLBToken = _VtLBToken_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 12),
    _VtLBToken_Type()
)
vtLBToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtLBToken.setStatus("mandatory")


class _VtCommandStatus_Type(Integer32):
    """Custom type vtCommandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("ready", 1))
    )


_VtCommandStatus_Type.__name__ = "Integer32"
_VtCommandStatus_Object = MibTableColumn
vtCommandStatus = _VtCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 13),
    _VtCommandStatus_Type()
)
vtCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtCommandStatus.setStatus("mandatory")
_VtLBRequests_Type = Counter32
_VtLBRequests_Object = MibTableColumn
vtLBRequests = _VtLBRequests_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 14),
    _VtLBRequests_Type()
)
vtLBRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtLBRequests.setStatus("mandatory")
_VtLBErrorResponses_Type = Counter32
_VtLBErrorResponses_Object = MibTableColumn
vtLBErrorResponses = _VtLBErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 15),
    _VtLBErrorResponses_Type()
)
vtLBErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtLBErrorResponses.setStatus("mandatory")
_VtLBTimeouts_Type = Counter32
_VtLBTimeouts_Object = MibTableColumn
vtLBTimeouts = _VtLBTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 16),
    _VtLBTimeouts_Type()
)
vtLBTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtLBTimeouts.setStatus("mandatory")
_VtOFEPRequests_Type = Counter32
_VtOFEPRequests_Object = MibTableColumn
vtOFEPRequests = _VtOFEPRequests_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 17),
    _VtOFEPRequests_Type()
)
vtOFEPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPRequests.setStatus("mandatory")
_VtOFEPErrorResponses_Type = Counter32
_VtOFEPErrorResponses_Object = MibTableColumn
vtOFEPErrorResponses = _VtOFEPErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 18),
    _VtOFEPErrorResponses_Type()
)
vtOFEPErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPErrorResponses.setStatus("mandatory")
_VtOFEPTimeouts_Type = Counter32
_VtOFEPTimeouts_Object = MibTableColumn
vtOFEPTimeouts = _VtOFEPTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 19),
    _VtOFEPTimeouts_Type()
)
vtOFEPTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPTimeouts.setStatus("mandatory")
_VtOFEPKeepAliveTimeouts_Type = Counter32
_VtOFEPKeepAliveTimeouts_Object = MibTableColumn
vtOFEPKeepAliveTimeouts = _VtOFEPKeepAliveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 20),
    _VtOFEPKeepAliveTimeouts_Type()
)
vtOFEPKeepAliveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPKeepAliveTimeouts.setStatus("mandatory")
_VtOFEPReassemblyFailures_Type = Counter32
_VtOFEPReassemblyFailures_Object = MibTableColumn
vtOFEPReassemblyFailures = _VtOFEPReassemblyFailures_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 21),
    _VtOFEPReassemblyFailures_Type()
)
vtOFEPReassemblyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPReassemblyFailures.setStatus("mandatory")
_VtOFEPUserEnquiries_Type = Counter32
_VtOFEPUserEnquiries_Object = MibTableColumn
vtOFEPUserEnquiries = _VtOFEPUserEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 22),
    _VtOFEPUserEnquiries_Type()
)
vtOFEPUserEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPUserEnquiries.setStatus("mandatory")
_VtOFEPUserResponses_Type = Counter32
_VtOFEPUserResponses_Object = MibTableColumn
vtOFEPUserResponses = _VtOFEPUserResponses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 23),
    _VtOFEPUserResponses_Type()
)
vtOFEPUserResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPUserResponses.setStatus("mandatory")
_VtOFEPUserInDiscards_Type = Counter32
_VtOFEPUserInDiscards_Object = MibTableColumn
vtOFEPUserInDiscards = _VtOFEPUserInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 24),
    _VtOFEPUserInDiscards_Type()
)
vtOFEPUserInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPUserInDiscards.setStatus("mandatory")
_VtOFEPUserOutDiscards_Type = Counter32
_VtOFEPUserOutDiscards_Object = MibTableColumn
vtOFEPUserOutDiscards = _VtOFEPUserOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 25),
    _VtOFEPUserOutDiscards_Type()
)
vtOFEPUserOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPUserOutDiscards.setStatus("mandatory")
_VtOFEPKeepAlives_Type = Counter32
_VtOFEPKeepAlives_Object = MibTableColumn
vtOFEPKeepAlives = _VtOFEPKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 11, 1, 1, 26),
    _VtOFEPKeepAlives_Type()
)
vtOFEPKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtOFEPKeepAlives.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tigPool = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 4, 0, 1)
)
tigPool.setObjects(
      *(("TIGER", "tigPoolIndex"),
        ("TIGER", "tigPoolTrapStatus"),
        ("TIGER", "tigPoolFree"))
)
if mibBuilder.loadTexts:
    tigPool.setStatus(
        ""
    )

tigRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 4, 0, 2)
)
tigRestart.setObjects(
      *(("TIGER", "tigRestartReason"),
        ("TIGER", "tigSystemDate"))
)
if mibBuilder.loadTexts:
    tigRestart.setStatus(
        ""
    )

tigIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 1, 4, 0, 3)
)
tigIdle.setObjects(
    ("TIGER", "tigCpuIdleState")
)
if mibBuilder.loadTexts:
    tigIdle.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIGER",
    **{"NonNegativeInteger": NonNegativeInteger,
       "InterfaceIndex": InterfaceIndex,
       "TigerDateAndTime": TigerDateAndTime,
       "ngcan": ngcan,
       "tiger": tiger,
       "generalTiger": generalTiger,
       "ifTStack": ifTStack,
       "ifTStackTable": ifTStackTable,
       "ifTStackEntry": ifTStackEntry,
       "ifTStackIndex": ifTStackIndex,
       "ifTStackHigherLayer": ifTStackHigherLayer,
       "ifTStackLowerLayer": ifTStackLowerLayer,
       "ifTStackStatus": ifTStackStatus,
       "tsystem": tsystem,
       "tigSystemDate": tigSystemDate,
       "tigSystemExceptionEcho": tigSystemExceptionEcho,
       "tigSystemExceptionLogging": tigSystemExceptionLogging,
       "tigSystemExceptionSaveLog": tigSystemExceptionSaveLog,
       "tigPCMCIATable": tigPCMCIATable,
       "tigPCMCIAEntry": tigPCMCIAEntry,
       "tigPCMCIASlot": tigPCMCIASlot,
       "tigPCMCIAIf": tigPCMCIAIf,
       "tigTokenRingSpeed": tigTokenRingSpeed,
       "tigPCMCIAType": tigPCMCIAType,
       "tigConfigFile": tigConfigFile,
       "tigRestartReason": tigRestartReason,
       "tigClearStats": tigClearStats,
       "tigClearStatsTime": tigClearStatsTime,
       "tigCpuTrapControl": tigCpuTrapControl,
       "tigCpuIdleState": tigCpuIdleState,
       "tigSystemSerialNum": tigSystemSerialNum,
       "tigDomainName": tigDomainName,
       "buffers": buffers,
       "tigPoolNumEntries": tigPoolNumEntries,
       "tigPoolTable": tigPoolTable,
       "tigPoolEntry": tigPoolEntry,
       "tigPoolIndex": tigPoolIndex,
       "tigPoolSize": tigPoolSize,
       "tigPoolBufSize": tigPoolBufSize,
       "tigPoolLowThreshold": tigPoolLowThreshold,
       "tigPoolHighThreshold": tigPoolHighThreshold,
       "tigPoolFree": tigPoolFree,
       "tigPoolCommandStatus": tigPoolCommandStatus,
       "tigPoolAllocationFailures": tigPoolAllocationFailures,
       "tigPoolTrapControl": tigPoolTrapControl,
       "tigPoolTrapStatus": tigPoolTrapStatus,
       "generalTraps": generalTraps,
       "tigPool": tigPool,
       "tigRestart": tigRestart,
       "tigIdle": tigIdle,
       "autif": autif,
       "autifNumEntries": autifNumEntries,
       "autifTable": autifTable,
       "autifEntry": autifEntry,
       "autifIndex": autifIndex,
       "autifService": autifService,
       "autifRemAddress": autifRemAddress,
       "autifLocalPort": autifLocalPort,
       "autifRemotePort": autifRemotePort,
       "autifRxBufSize": autifRxBufSize,
       "autifTxBufSize": autifTxBufSize,
       "autifSockQueueSize": autifSockQueueSize,
       "autifTypeAQueueSize": autifTypeAQueueSize,
       "autifTypeAMaxMsgSize": autifTypeAMaxMsgSize,
       "autifInOctets": autifInOctets,
       "autifInUcastPkts": autifInUcastPkts,
       "autifInNUcastPkts": autifInNUcastPkts,
       "autifInDiscards": autifInDiscards,
       "autifInErrors": autifInErrors,
       "autifInUnknownProtos": autifInUnknownProtos,
       "autifOutOctets": autifOutOctets,
       "autifOutUcastPkts": autifOutUcastPkts,
       "autifOutNUcastPkts": autifOutNUcastPkts,
       "autifOutDiscards": autifOutDiscards,
       "autifOutErrors": autifOutErrors,
       "autifIA": autifIA,
       "autifAliasAddress": autifAliasAddress,
       "autifSockPrecedence": autifSockPrecedence,
       "autifDestAddrType": autifDestAddrType,
       "autifSockOptions": autifSockOptions,
       "autifLNIA": autifLNIA,
       "autifLBName": autifLBName,
       "autifOFEPKeepAliveTimeout": autifOFEPKeepAliveTimeout,
       "autifUserIdleTimeout": autifUserIdleTimeout,
       "autifXlatToSocket": autifXlatToSocket,
       "autifXlatFromSocket": autifXlatFromSocket,
       "autifRealToVTRoutingErrors": autifRealToVTRoutingErrors,
       "autifVTToRealRoutingErrors": autifVTToRealRoutingErrors,
       "autifRealToVTHashDepth": autifRealToVTHashDepth,
       "apath": apath,
       "apathNumEntries": apathNumEntries,
       "apathTable": apathTable,
       "apathEntry": apathEntry,
       "apathIndex": apathIndex,
       "apathType": apathType,
       "apathIdleTimerMax": apathIdleTimerMax,
       "apathResponseTimerMax": apathResponseTimerMax,
       "apathRetryCounterMax": apathRetryCounterMax,
       "apathEndUserStatusEnable": apathEndUserStatusEnable,
       "apathTrafficIdleTimer": apathTrafficIdleTimer,
       "apathConnectTimerMax": apathConnectTimerMax,
       "apathPathUpMsg": apathPathUpMsg,
       "apathUserNumEntries": apathUserNumEntries,
       "apathUserTable": apathUserTable,
       "apathUserEntry": apathUserEntry,
       "apathUserIndex": apathUserIndex,
       "apathUserApathOperation": apathUserApathOperation,
       "apathUserMainApathIndex": apathUserMainApathIndex,
       "apathUserAlt1ApathIndex": apathUserAlt1ApathIndex,
       "apathUserAlt2ApathIndex": apathUserAlt2ApathIndex,
       "apathUserAlt3ApathIndex": apathUserAlt3ApathIndex,
       "apathUserType": apathUserType,
       "apathUserDevStatusEnable": apathUserDevStatusEnable,
       "apathUserAuxilliaryInfo": apathUserAuxilliaryInfo,
       "svcmsg": svcmsg,
       "svcmsgNumEntries": svcmsgNumEntries,
       "svcmsgTable": svcmsgTable,
       "svcmsgEntry": svcmsgEntry,
       "svcmsgIndex": svcmsgIndex,
       "svcmsgDescription": svcmsgDescription,
       "svcmsgNetDown": svcmsgNetDown,
       "svcmsgNetUp": svcmsgNetUp,
       "svcmsgConnecting": svcmsgConnecting,
       "svcmsgConnected": svcmsgConnected,
       "svcmsgIdle": svcmsgIdle,
       "svcmsgDisconnecting": svcmsgDisconnecting,
       "svcmsgDisconnected": svcmsgDisconnected,
       "svcmsgDiscRestart": svcmsgDiscRestart,
       "svcmsgDiscUser": svcmsgDiscUser,
       "svcmsgDiscMgmt": svcmsgDiscMgmt,
       "svcmsgDiscBusy": svcmsgDiscBusy,
       "svcmsgDiscRPErr": svcmsgDiscRPErr,
       "svcmsgDiscLPErr": svcmsgDiscLPErr,
       "svcmsgDiscCongest": svcmsgDiscCongest,
       "svcmsgDiscNotOb": svcmsgDiscNotOb,
       "svcmsgDiscOutOrder": svcmsgDiscOutOrder,
       "svcmsgDiscInvFac": svcmsgDiscInvFac,
       "svcmsgDiscAcsBar": svcmsgDiscAcsBar,
       "svcmsgDiscRvsCharge": svcmsgDiscRvsCharge,
       "svcmsgDiscIncDest": svcmsgDiscIncDest,
       "svcmsgDiscNoTraf": svcmsgDiscNoTraf,
       "svcmsgUpAgain": svcmsgUpAgain,
       "svcmsgNoRoute": svcmsgNoRoute,
       "svcmsgOverLength": svcmsgOverLength,
       "svcmsgCongestion": svcmsgCongestion,
       "svcmsgHostUnreach": svcmsgHostUnreach,
       "svcmsgZeroLength": svcmsgZeroLength,
       "bootp": bootp,
       "bootpNumEntries": bootpNumEntries,
       "bootpTable": bootpTable,
       "bootpEntry": bootpEntry,
       "bootpIndex": bootpIndex,
       "bootpServerName": bootpServerName,
       "bootpUserName": bootpUserName,
       "bootpPassword": bootpPassword,
       "bootpRemoteFile": bootpRemoteFile,
       "bootpLocalFile": bootpLocalFile,
       "mount": mount,
       "mountNumEntries": mountNumEntries,
       "mountTable": mountTable,
       "mountEntry": mountEntry,
       "mountIndex": mountIndex,
       "mountRemotePath": mountRemotePath,
       "mountLocalPath": mountLocalPath,
       "mountMode": mountMode,
       "mountRemoteInfo": mountRemoteInfo,
       "dnsRes": dnsRes,
       "dnsResLocalResolves": dnsResLocalResolves,
       "dnsResCacheFull": dnsResCacheFull,
       "dnsResQueueFull": dnsResQueueFull,
       "dnsResClearCache": dnsResClearCache,
       "dnsResConfigMaxCnames": dnsResConfigMaxCnames,
       "dnsResNumHosts": dnsResNumHosts,
       "dnsResTable": dnsResTable,
       "dnsResEntry": dnsResEntry,
       "dnsResServerIP": dnsResServerIP,
       "dnsResServerName": dnsResServerName,
       "dnsResQueriesSent": dnsResQueriesSent,
       "dnsResSendErrors": dnsResSendErrors,
       "dnsResGoodResponses": dnsResGoodResponses,
       "dnsResTimeouts": dnsResTimeouts,
       "dnsResBadResponses": dnsResBadResponses,
       "dnsResCmd": dnsResCmd,
       "dnsResCacheNumEntries": dnsResCacheNumEntries,
       "dnsResCacheTable": dnsResCacheTable,
       "dnsResCacheEntry": dnsResCacheEntry,
       "dnsResCacheHostName": dnsResCacheHostName,
       "dnsResCacheIpAddress": dnsResCacheIpAddress,
       "dnsResCacheRRTTL": dnsResCacheRRTTL,
       "dnsResCacheRRElapsedTTL": dnsResCacheRRElapsedTTL,
       "dnsResCacheRRSource": dnsResCacheRRSource,
       "vt": vt,
       "vtTable": vtTable,
       "vtEntry": vtEntry,
       "vtAutifIndex": vtAutifIndex,
       "vtRealLnIaTa": vtRealLnIaTa,
       "vtLnIaTa": vtLnIaTa,
       "vtOptionsDOD": vtOptionsDOD,
       "vtOptionsPrinter": vtOptionsPrinter,
       "vtOptionsClass": vtOptionsClass,
       "vtCommand": vtCommand,
       "vtClassName": vtClassName,
       "vtState": vtState,
       "vtFailReason": vtFailReason,
       "vtFailString": vtFailString,
       "vtLBToken": vtLBToken,
       "vtCommandStatus": vtCommandStatus,
       "vtLBRequests": vtLBRequests,
       "vtLBErrorResponses": vtLBErrorResponses,
       "vtLBTimeouts": vtLBTimeouts,
       "vtOFEPRequests": vtOFEPRequests,
       "vtOFEPErrorResponses": vtOFEPErrorResponses,
       "vtOFEPTimeouts": vtOFEPTimeouts,
       "vtOFEPKeepAliveTimeouts": vtOFEPKeepAliveTimeouts,
       "vtOFEPReassemblyFailures": vtOFEPReassemblyFailures,
       "vtOFEPUserEnquiries": vtOFEPUserEnquiries,
       "vtOFEPUserResponses": vtOFEPUserResponses,
       "vtOFEPUserInDiscards": vtOFEPUserInDiscards,
       "vtOFEPUserOutDiscards": vtOFEPUserOutDiscards,
       "vtOFEPKeepAlives": vtOFEPKeepAlives}
)
