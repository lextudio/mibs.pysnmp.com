# SNMP MIB module (Wellfleet-ISDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ISDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:33 2024
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

(wfIsdbGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIsdbGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIsdbCfgTable_Object = MibTable
wfIsdbCfgTable = _WfIsdbCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1)
)
if mibBuilder.loadTexts:
    wfIsdbCfgTable.setStatus("mandatory")
_WfIsdbCfgEntry_Object = MibTableRow
wfIsdbCfgEntry = _WfIsdbCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1)
)
wfIsdbCfgEntry.setIndexNames(
    (0, "Wellfleet-ISDB-MIB", "wfIsdbCfgSlot"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbCfgConnector"),
)
if mibBuilder.loadTexts:
    wfIsdbCfgEntry.setStatus("mandatory")


class _WfIsdbCfgDelete_Type(Integer32):
    """Custom type wfIsdbCfgDelete based on Integer32"""
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


_WfIsdbCfgDelete_Type.__name__ = "Integer32"
_WfIsdbCfgDelete_Object = MibTableColumn
wfIsdbCfgDelete = _WfIsdbCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 1),
    _WfIsdbCfgDelete_Type()
)
wfIsdbCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgDelete.setStatus("mandatory")


class _WfIsdbCfgDisable_Type(Integer32):
    """Custom type wfIsdbCfgDisable based on Integer32"""
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


_WfIsdbCfgDisable_Type.__name__ = "Integer32"
_WfIsdbCfgDisable_Object = MibTableColumn
wfIsdbCfgDisable = _WfIsdbCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 2),
    _WfIsdbCfgDisable_Type()
)
wfIsdbCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgDisable.setStatus("mandatory")


class _WfIsdbCfgState_Type(Integer32):
    """Custom type wfIsdbCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfIsdbCfgState_Type.__name__ = "Integer32"
_WfIsdbCfgState_Object = MibTableColumn
wfIsdbCfgState = _WfIsdbCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 3),
    _WfIsdbCfgState_Type()
)
wfIsdbCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbCfgState.setStatus("mandatory")
_WfIsdbCfgSlot_Type = Integer32
_WfIsdbCfgSlot_Object = MibTableColumn
wfIsdbCfgSlot = _WfIsdbCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 4),
    _WfIsdbCfgSlot_Type()
)
wfIsdbCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbCfgSlot.setStatus("mandatory")
_WfIsdbCfgConnector_Type = Integer32
_WfIsdbCfgConnector_Object = MibTableColumn
wfIsdbCfgConnector = _WfIsdbCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 5),
    _WfIsdbCfgConnector_Type()
)
wfIsdbCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbCfgConnector.setStatus("mandatory")
_WfIsdbCfgCircuit_Type = Integer32
_WfIsdbCfgCircuit_Object = MibTableColumn
wfIsdbCfgCircuit = _WfIsdbCfgCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 6),
    _WfIsdbCfgCircuit_Type()
)
wfIsdbCfgCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgCircuit.setStatus("mandatory")
_WfIsdbCfgLogFilter_Type = Integer32
_WfIsdbCfgLogFilter_Object = MibTableColumn
wfIsdbCfgLogFilter = _WfIsdbCfgLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 7),
    _WfIsdbCfgLogFilter_Type()
)
wfIsdbCfgLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgLogFilter.setStatus("mandatory")


class _WfIsdbCfgPollInterval_Type(Integer32):
    """Custom type wfIsdbCfgPollInterval based on Integer32"""
    defaultValue = 5


_WfIsdbCfgPollInterval_Object = MibTableColumn
wfIsdbCfgPollInterval = _WfIsdbCfgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 8),
    _WfIsdbCfgPollInterval_Type()
)
wfIsdbCfgPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgPollInterval.setStatus("mandatory")


class _WfIsdbCfgAutoRestart_Type(Integer32):
    """Custom type wfIsdbCfgAutoRestart based on Integer32"""
    defaultValue = 1


_WfIsdbCfgAutoRestart_Object = MibTableColumn
wfIsdbCfgAutoRestart = _WfIsdbCfgAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 9),
    _WfIsdbCfgAutoRestart_Type()
)
wfIsdbCfgAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgAutoRestart.setStatus("mandatory")


class _WfIsdbCfgAutoUld_Type(Integer32):
    """Custom type wfIsdbCfgAutoUld based on Integer32"""
    defaultValue = 0


_WfIsdbCfgAutoUld_Object = MibTableColumn
wfIsdbCfgAutoUld = _WfIsdbCfgAutoUld_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 10),
    _WfIsdbCfgAutoUld_Type()
)
wfIsdbCfgAutoUld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgAutoUld.setStatus("mandatory")


class _WfIsdbCfgUldVolume_Type(Integer32):
    """Custom type wfIsdbCfgUldVolume based on Integer32"""
    defaultValue = 1


_WfIsdbCfgUldVolume_Object = MibTableColumn
wfIsdbCfgUldVolume = _WfIsdbCfgUldVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 11),
    _WfIsdbCfgUldVolume_Type()
)
wfIsdbCfgUldVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbCfgUldVolume.setStatus("mandatory")
_WfIsdbImageVersion_Type = Integer32
_WfIsdbImageVersion_Object = MibTableColumn
wfIsdbImageVersion = _WfIsdbImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 12),
    _WfIsdbImageVersion_Type()
)
wfIsdbImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbImageVersion.setStatus("mandatory")
_WfIsdbImageDate_Type = DisplayString
_WfIsdbImageDate_Object = MibTableColumn
wfIsdbImageDate = _WfIsdbImageDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 13),
    _WfIsdbImageDate_Type()
)
wfIsdbImageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbImageDate.setStatus("mandatory")
_WfIsdbDiagVersion_Type = OctetString
_WfIsdbDiagVersion_Object = MibTableColumn
wfIsdbDiagVersion = _WfIsdbDiagVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 14),
    _WfIsdbDiagVersion_Type()
)
wfIsdbDiagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbDiagVersion.setStatus("mandatory")
_WfIsdbDiagDate_Type = DisplayString
_WfIsdbDiagDate_Object = MibTableColumn
wfIsdbDiagDate = _WfIsdbDiagDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 1, 1, 15),
    _WfIsdbDiagDate_Type()
)
wfIsdbDiagDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbDiagDate.setStatus("mandatory")
_WfIsdbStatTable_Object = MibTable
wfIsdbStatTable = _WfIsdbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2)
)
if mibBuilder.loadTexts:
    wfIsdbStatTable.setStatus("mandatory")
_WfIsdbStatEntry_Object = MibTableRow
wfIsdbStatEntry = _WfIsdbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1)
)
wfIsdbStatEntry.setIndexNames(
    (0, "Wellfleet-ISDB-MIB", "wfIsdbStatSlot"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbStatConnector"),
)
if mibBuilder.loadTexts:
    wfIsdbStatEntry.setStatus("mandatory")


class _WfIsdbStatState_Type(Integer32):
    """Custom type wfIsdbStatState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfIsdbStatState_Type.__name__ = "Integer32"
_WfIsdbStatState_Object = MibTableColumn
wfIsdbStatState = _WfIsdbStatState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 1),
    _WfIsdbStatState_Type()
)
wfIsdbStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatState.setStatus("mandatory")
_WfIsdbStatSlot_Type = Integer32
_WfIsdbStatSlot_Object = MibTableColumn
wfIsdbStatSlot = _WfIsdbStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 2),
    _WfIsdbStatSlot_Type()
)
wfIsdbStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatSlot.setStatus("mandatory")
_WfIsdbStatConnector_Type = Integer32
_WfIsdbStatConnector_Object = MibTableColumn
wfIsdbStatConnector = _WfIsdbStatConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 3),
    _WfIsdbStatConnector_Type()
)
wfIsdbStatConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatConnector.setStatus("mandatory")
_WfIsdbStatVersion_Type = Integer32
_WfIsdbStatVersion_Object = MibTableColumn
wfIsdbStatVersion = _WfIsdbStatVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 4),
    _WfIsdbStatVersion_Type()
)
wfIsdbStatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatVersion.setStatus("mandatory")
_WfIsdbStatCurrentConnCount_Type = Counter32
_WfIsdbStatCurrentConnCount_Object = MibTableColumn
wfIsdbStatCurrentConnCount = _WfIsdbStatCurrentConnCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 5),
    _WfIsdbStatCurrentConnCount_Type()
)
wfIsdbStatCurrentConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatCurrentConnCount.setStatus("mandatory")
_WfIsdbStatTotalConnCount_Type = Counter32
_WfIsdbStatTotalConnCount_Object = MibTableColumn
wfIsdbStatTotalConnCount = _WfIsdbStatTotalConnCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 6),
    _WfIsdbStatTotalConnCount_Type()
)
wfIsdbStatTotalConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTotalConnCount.setStatus("mandatory")
_WfIsdbStatStartCount_Type = Counter32
_WfIsdbStatStartCount_Object = MibTableColumn
wfIsdbStatStartCount = _WfIsdbStatStartCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 7),
    _WfIsdbStatStartCount_Type()
)
wfIsdbStatStartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatStartCount.setStatus("mandatory")
_WfIsdbStatCpuIdleCurrent_Type = Integer32
_WfIsdbStatCpuIdleCurrent_Object = MibTableColumn
wfIsdbStatCpuIdleCurrent = _WfIsdbStatCpuIdleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 8),
    _WfIsdbStatCpuIdleCurrent_Type()
)
wfIsdbStatCpuIdleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatCpuIdleCurrent.setStatus("mandatory")
_WfIsdbStatCpuIdleTotal_Type = Integer32
_WfIsdbStatCpuIdleTotal_Object = MibTableColumn
wfIsdbStatCpuIdleTotal = _WfIsdbStatCpuIdleTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 9),
    _WfIsdbStatCpuIdleTotal_Type()
)
wfIsdbStatCpuIdleTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatCpuIdleTotal.setStatus("mandatory")
_WfIsdbStatMemoryFree_Type = Integer32
_WfIsdbStatMemoryFree_Object = MibTableColumn
wfIsdbStatMemoryFree = _WfIsdbStatMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 10),
    _WfIsdbStatMemoryFree_Type()
)
wfIsdbStatMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatMemoryFree.setStatus("mandatory")
_WfIsdbStatMemoryLargestBlock_Type = Integer32
_WfIsdbStatMemoryLargestBlock_Object = MibTableColumn
wfIsdbStatMemoryLargestBlock = _WfIsdbStatMemoryLargestBlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 11),
    _WfIsdbStatMemoryLargestBlock_Type()
)
wfIsdbStatMemoryLargestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatMemoryLargestBlock.setStatus("mandatory")
_WfIsdbStatTaskCount_Type = Counter32
_WfIsdbStatTaskCount_Object = MibTableColumn
wfIsdbStatTaskCount = _WfIsdbStatTaskCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 12),
    _WfIsdbStatTaskCount_Type()
)
wfIsdbStatTaskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTaskCount.setStatus("mandatory")
_WfIsdbStatMsgQueueLacks_Type = Counter32
_WfIsdbStatMsgQueueLacks_Object = MibTableColumn
wfIsdbStatMsgQueueLacks = _WfIsdbStatMsgQueueLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 13),
    _WfIsdbStatMsgQueueLacks_Type()
)
wfIsdbStatMsgQueueLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatMsgQueueLacks.setStatus("mandatory")
_WfIsdbStatHardwareTimeouts_Type = Counter32
_WfIsdbStatHardwareTimeouts_Object = MibTableColumn
wfIsdbStatHardwareTimeouts = _WfIsdbStatHardwareTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 14),
    _WfIsdbStatHardwareTimeouts_Type()
)
wfIsdbStatHardwareTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatHardwareTimeouts.setStatus("mandatory")
_WfIsdbStatAlarmCount_Type = Counter32
_WfIsdbStatAlarmCount_Object = MibTableColumn
wfIsdbStatAlarmCount = _WfIsdbStatAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 15),
    _WfIsdbStatAlarmCount_Type()
)
wfIsdbStatAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAlarmCount.setStatus("mandatory")
_WfIsdbStatAuthorUnknown_Type = Counter32
_WfIsdbStatAuthorUnknown_Object = MibTableColumn
wfIsdbStatAuthorUnknown = _WfIsdbStatAuthorUnknown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 16),
    _WfIsdbStatAuthorUnknown_Type()
)
wfIsdbStatAuthorUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAuthorUnknown.setStatus("mandatory")
_WfIsdbStatAv1Ints_Type = Counter32
_WfIsdbStatAv1Ints_Object = MibTableColumn
wfIsdbStatAv1Ints = _WfIsdbStatAv1Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 17),
    _WfIsdbStatAv1Ints_Type()
)
wfIsdbStatAv1Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv1Ints.setStatus("mandatory")
_WfIsdbStatAv2Ints_Type = Counter32
_WfIsdbStatAv2Ints_Object = MibTableColumn
wfIsdbStatAv2Ints = _WfIsdbStatAv2Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 18),
    _WfIsdbStatAv2Ints_Type()
)
wfIsdbStatAv2Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv2Ints.setStatus("mandatory")
_WfIsdbStatAv3Ints_Type = Counter32
_WfIsdbStatAv3Ints_Object = MibTableColumn
wfIsdbStatAv3Ints = _WfIsdbStatAv3Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 19),
    _WfIsdbStatAv3Ints_Type()
)
wfIsdbStatAv3Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv3Ints.setStatus("mandatory")
_WfIsdbStatAv4Ints_Type = Counter32
_WfIsdbStatAv4Ints_Object = MibTableColumn
wfIsdbStatAv4Ints = _WfIsdbStatAv4Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 20),
    _WfIsdbStatAv4Ints_Type()
)
wfIsdbStatAv4Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv4Ints.setStatus("mandatory")
_WfIsdbStatAv5Ints_Type = Counter32
_WfIsdbStatAv5Ints_Object = MibTableColumn
wfIsdbStatAv5Ints = _WfIsdbStatAv5Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 21),
    _WfIsdbStatAv5Ints_Type()
)
wfIsdbStatAv5Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv5Ints.setStatus("mandatory")
_WfIsdbStatAv6Ints_Type = Counter32
_WfIsdbStatAv6Ints_Object = MibTableColumn
wfIsdbStatAv6Ints = _WfIsdbStatAv6Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 22),
    _WfIsdbStatAv6Ints_Type()
)
wfIsdbStatAv6Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv6Ints.setStatus("mandatory")
_WfIsdbStatAv7Ints_Type = Counter32
_WfIsdbStatAv7Ints_Object = MibTableColumn
wfIsdbStatAv7Ints = _WfIsdbStatAv7Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 23),
    _WfIsdbStatAv7Ints_Type()
)
wfIsdbStatAv7Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatAv7Ints.setStatus("mandatory")
_WfIsdbStatScc3Ints_Type = Counter32
_WfIsdbStatScc3Ints_Object = MibTableColumn
wfIsdbStatScc3Ints = _WfIsdbStatScc3Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 24),
    _WfIsdbStatScc3Ints_Type()
)
wfIsdbStatScc3Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatScc3Ints.setStatus("mandatory")
_WfIsdbStatErrorInts_Type = Counter32
_WfIsdbStatErrorInts_Object = MibTableColumn
wfIsdbStatErrorInts = _WfIsdbStatErrorInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 25),
    _WfIsdbStatErrorInts_Type()
)
wfIsdbStatErrorInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatErrorInts.setStatus("mandatory")
_WfIsdbStatTimer1Ints_Type = Counter32
_WfIsdbStatTimer1Ints_Object = MibTableColumn
wfIsdbStatTimer1Ints = _WfIsdbStatTimer1Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 26),
    _WfIsdbStatTimer1Ints_Type()
)
wfIsdbStatTimer1Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTimer1Ints.setStatus("mandatory")
_WfIsdbStatTimer2Ints_Type = Counter32
_WfIsdbStatTimer2Ints_Object = MibTableColumn
wfIsdbStatTimer2Ints = _WfIsdbStatTimer2Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 27),
    _WfIsdbStatTimer2Ints_Type()
)
wfIsdbStatTimer2Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTimer2Ints.setStatus("mandatory")
_WfIsdbStatTimer3Ints_Type = Counter32
_WfIsdbStatTimer3Ints_Object = MibTableColumn
wfIsdbStatTimer3Ints = _WfIsdbStatTimer3Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 28),
    _WfIsdbStatTimer3Ints_Type()
)
wfIsdbStatTimer3Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTimer3Ints.setStatus("mandatory")
_WfIsdbStatTimer4Ints_Type = Counter32
_WfIsdbStatTimer4Ints_Object = MibTableColumn
wfIsdbStatTimer4Ints = _WfIsdbStatTimer4Ints_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 29),
    _WfIsdbStatTimer4Ints_Type()
)
wfIsdbStatTimer4Ints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTimer4Ints.setStatus("mandatory")
_WfIsdbStatBusErrors_Type = Counter32
_WfIsdbStatBusErrors_Object = MibTableColumn
wfIsdbStatBusErrors = _WfIsdbStatBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 30),
    _WfIsdbStatBusErrors_Type()
)
wfIsdbStatBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatBusErrors.setStatus("mandatory")
_WfIsdbStatRxFrames_Type = Counter32
_WfIsdbStatRxFrames_Object = MibTableColumn
wfIsdbStatRxFrames = _WfIsdbStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 31),
    _WfIsdbStatRxFrames_Type()
)
wfIsdbStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxFrames.setStatus("mandatory")
_WfIsdbStatRxOctets_Type = Counter32
_WfIsdbStatRxOctets_Object = MibTableColumn
wfIsdbStatRxOctets = _WfIsdbStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 32),
    _WfIsdbStatRxOctets_Type()
)
wfIsdbStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxOctets.setStatus("mandatory")
_WfIsdbStatRxLacks_Type = Counter32
_WfIsdbStatRxLacks_Object = MibTableColumn
wfIsdbStatRxLacks = _WfIsdbStatRxLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 33),
    _WfIsdbStatRxLacks_Type()
)
wfIsdbStatRxLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxLacks.setStatus("mandatory")
_WfIsdbStatRxDataLinkMsgLacks_Type = Counter32
_WfIsdbStatRxDataLinkMsgLacks_Object = MibTableColumn
wfIsdbStatRxDataLinkMsgLacks = _WfIsdbStatRxDataLinkMsgLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 34),
    _WfIsdbStatRxDataLinkMsgLacks_Type()
)
wfIsdbStatRxDataLinkMsgLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxDataLinkMsgLacks.setStatus("mandatory")
_WfIsdbStatRxManagementMsgLacks_Type = Counter32
_WfIsdbStatRxManagementMsgLacks_Object = MibTableColumn
wfIsdbStatRxManagementMsgLacks = _WfIsdbStatRxManagementMsgLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 35),
    _WfIsdbStatRxManagementMsgLacks_Type()
)
wfIsdbStatRxManagementMsgLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxManagementMsgLacks.setStatus("mandatory")
_WfIsdbStatRxBadFrames_Type = Counter32
_WfIsdbStatRxBadFrames_Object = MibTableColumn
wfIsdbStatRxBadFrames = _WfIsdbStatRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 36),
    _WfIsdbStatRxBadFrames_Type()
)
wfIsdbStatRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxBadFrames.setStatus("mandatory")
_WfIsdbStatRxOverFlows_Type = Counter32
_WfIsdbStatRxOverFlows_Object = MibTableColumn
wfIsdbStatRxOverFlows = _WfIsdbStatRxOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 37),
    _WfIsdbStatRxOverFlows_Type()
)
wfIsdbStatRxOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxOverFlows.setStatus("mandatory")
_WfIsdbStatRxRunts_Type = Counter32
_WfIsdbStatRxRunts_Object = MibTableColumn
wfIsdbStatRxRunts = _WfIsdbStatRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 38),
    _WfIsdbStatRxRunts_Type()
)
wfIsdbStatRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxRunts.setStatus("mandatory")
_WfIsdbStatRxLargeFrames_Type = Counter32
_WfIsdbStatRxLargeFrames_Object = MibTableColumn
wfIsdbStatRxLargeFrames = _WfIsdbStatRxLargeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 39),
    _WfIsdbStatRxLargeFrames_Type()
)
wfIsdbStatRxLargeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxLargeFrames.setStatus("mandatory")
_WfIsdbStatRxSmallFrames_Type = Counter32
_WfIsdbStatRxSmallFrames_Object = MibTableColumn
wfIsdbStatRxSmallFrames = _WfIsdbStatRxSmallFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 40),
    _WfIsdbStatRxSmallFrames_Type()
)
wfIsdbStatRxSmallFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxSmallFrames.setStatus("mandatory")
_WfIsdbStatRxIncompleteFrames_Type = Counter32
_WfIsdbStatRxIncompleteFrames_Object = MibTableColumn
wfIsdbStatRxIncompleteFrames = _WfIsdbStatRxIncompleteFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 41),
    _WfIsdbStatRxIncompleteFrames_Type()
)
wfIsdbStatRxIncompleteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxIncompleteFrames.setStatus("mandatory")
_WfIsdbStatRxInts_Type = Counter32
_WfIsdbStatRxInts_Object = MibTableColumn
wfIsdbStatRxInts = _WfIsdbStatRxInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 42),
    _WfIsdbStatRxInts_Type()
)
wfIsdbStatRxInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxInts.setStatus("mandatory")
_WfIsdbStatRxDataLinkFrames_Type = Counter32
_WfIsdbStatRxDataLinkFrames_Object = MibTableColumn
wfIsdbStatRxDataLinkFrames = _WfIsdbStatRxDataLinkFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 43),
    _WfIsdbStatRxDataLinkFrames_Type()
)
wfIsdbStatRxDataLinkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxDataLinkFrames.setStatus("mandatory")
_WfIsdbStatRxDataLinkDiscards_Type = Counter32
_WfIsdbStatRxDataLinkDiscards_Object = MibTableColumn
wfIsdbStatRxDataLinkDiscards = _WfIsdbStatRxDataLinkDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 44),
    _WfIsdbStatRxDataLinkDiscards_Type()
)
wfIsdbStatRxDataLinkDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxDataLinkDiscards.setStatus("mandatory")
_WfIsdbStatRxManagementFrames_Type = Counter32
_WfIsdbStatRxManagementFrames_Object = MibTableColumn
wfIsdbStatRxManagementFrames = _WfIsdbStatRxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 45),
    _WfIsdbStatRxManagementFrames_Type()
)
wfIsdbStatRxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxManagementFrames.setStatus("mandatory")
_WfIsdbStatRxUnknownFrames_Type = Counter32
_WfIsdbStatRxUnknownFrames_Object = MibTableColumn
wfIsdbStatRxUnknownFrames = _WfIsdbStatRxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 46),
    _WfIsdbStatRxUnknownFrames_Type()
)
wfIsdbStatRxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatRxUnknownFrames.setStatus("mandatory")
_WfIsdbStatTxFrames_Type = Counter32
_WfIsdbStatTxFrames_Object = MibTableColumn
wfIsdbStatTxFrames = _WfIsdbStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 47),
    _WfIsdbStatTxFrames_Type()
)
wfIsdbStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxFrames.setStatus("mandatory")
_WfIsdbStatTxOctets_Type = Counter32
_WfIsdbStatTxOctets_Object = MibTableColumn
wfIsdbStatTxOctets = _WfIsdbStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 48),
    _WfIsdbStatTxOctets_Type()
)
wfIsdbStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxOctets.setStatus("mandatory")
_WfIsdbStatTxLacks_Type = Counter32
_WfIsdbStatTxLacks_Object = MibTableColumn
wfIsdbStatTxLacks = _WfIsdbStatTxLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 49),
    _WfIsdbStatTxLacks_Type()
)
wfIsdbStatTxLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxLacks.setStatus("mandatory")
_WfIsdbStatTxUnderFlows_Type = Counter32
_WfIsdbStatTxUnderFlows_Object = MibTableColumn
wfIsdbStatTxUnderFlows = _WfIsdbStatTxUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 50),
    _WfIsdbStatTxUnderFlows_Type()
)
wfIsdbStatTxUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxUnderFlows.setStatus("mandatory")
_WfIsdbStatTxAbortedFrames_Type = Counter32
_WfIsdbStatTxAbortedFrames_Object = MibTableColumn
wfIsdbStatTxAbortedFrames = _WfIsdbStatTxAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 51),
    _WfIsdbStatTxAbortedFrames_Type()
)
wfIsdbStatTxAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxAbortedFrames.setStatus("mandatory")
_WfIsdbStatTxMsgs_Type = Counter32
_WfIsdbStatTxMsgs_Object = MibTableColumn
wfIsdbStatTxMsgs = _WfIsdbStatTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 52),
    _WfIsdbStatTxMsgs_Type()
)
wfIsdbStatTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxMsgs.setStatus("mandatory")
_WfIsdbStatTxLargeMsgs_Type = Counter32
_WfIsdbStatTxLargeMsgs_Object = MibTableColumn
wfIsdbStatTxLargeMsgs = _WfIsdbStatTxLargeMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 53),
    _WfIsdbStatTxLargeMsgs_Type()
)
wfIsdbStatTxLargeMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxLargeMsgs.setStatus("mandatory")
_WfIsdbStatTxSmallMsgs_Type = Counter32
_WfIsdbStatTxSmallMsgs_Object = MibTableColumn
wfIsdbStatTxSmallMsgs = _WfIsdbStatTxSmallMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 54),
    _WfIsdbStatTxSmallMsgs_Type()
)
wfIsdbStatTxSmallMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxSmallMsgs.setStatus("mandatory")
_WfIsdbStatTxInts_Type = Counter32
_WfIsdbStatTxInts_Object = MibTableColumn
wfIsdbStatTxInts = _WfIsdbStatTxInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 55),
    _WfIsdbStatTxInts_Type()
)
wfIsdbStatTxInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxInts.setStatus("mandatory")
_WfIsdbStatTxDataLinkFrames_Type = Counter32
_WfIsdbStatTxDataLinkFrames_Object = MibTableColumn
wfIsdbStatTxDataLinkFrames = _WfIsdbStatTxDataLinkFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 56),
    _WfIsdbStatTxDataLinkFrames_Type()
)
wfIsdbStatTxDataLinkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxDataLinkFrames.setStatus("mandatory")
_WfIsdbStatTxManagementFrames_Type = Counter32
_WfIsdbStatTxManagementFrames_Object = MibTableColumn
wfIsdbStatTxManagementFrames = _WfIsdbStatTxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 57),
    _WfIsdbStatTxManagementFrames_Type()
)
wfIsdbStatTxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxManagementFrames.setStatus("mandatory")
_WfIsdbStatTxUnknownFrames_Type = Counter32
_WfIsdbStatTxUnknownFrames_Object = MibTableColumn
wfIsdbStatTxUnknownFrames = _WfIsdbStatTxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 2, 1, 58),
    _WfIsdbStatTxUnknownFrames_Type()
)
wfIsdbStatTxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbStatTxUnknownFrames.setStatus("mandatory")
_WfIsdbPortDefaultCfgTable_Object = MibTable
wfIsdbPortDefaultCfgTable = _WfIsdbPortDefaultCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3)
)
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgTable.setStatus("mandatory")
_WfIsdbPortDefaultCfgEntry_Object = MibTableRow
wfIsdbPortDefaultCfgEntry = _WfIsdbPortDefaultCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1)
)
wfIsdbPortDefaultCfgEntry.setIndexNames(
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortDefaultCfgSlot"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortDefaultCfgConnector"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortDefaultCfgNumber"),
)
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgEntry.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDelete_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDelete based on Integer32"""
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


_WfIsdbPortDefaultCfgDelete_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDelete_Object = MibTableColumn
wfIsdbPortDefaultCfgDelete = _WfIsdbPortDefaultCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 1),
    _WfIsdbPortDefaultCfgDelete_Type()
)
wfIsdbPortDefaultCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDelete.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDisable_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDisable based on Integer32"""
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


_WfIsdbPortDefaultCfgDisable_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDisable_Object = MibTableColumn
wfIsdbPortDefaultCfgDisable = _WfIsdbPortDefaultCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 2),
    _WfIsdbPortDefaultCfgDisable_Type()
)
wfIsdbPortDefaultCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDisable.setStatus("mandatory")


class _WfIsdbPortDefaultCfgState_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfIsdbPortDefaultCfgState_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgState_Object = MibTableColumn
wfIsdbPortDefaultCfgState = _WfIsdbPortDefaultCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 3),
    _WfIsdbPortDefaultCfgState_Type()
)
wfIsdbPortDefaultCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgState.setStatus("mandatory")
_WfIsdbPortDefaultCfgSlot_Type = Integer32
_WfIsdbPortDefaultCfgSlot_Object = MibTableColumn
wfIsdbPortDefaultCfgSlot = _WfIsdbPortDefaultCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 4),
    _WfIsdbPortDefaultCfgSlot_Type()
)
wfIsdbPortDefaultCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgSlot.setStatus("mandatory")
_WfIsdbPortDefaultCfgConnector_Type = Integer32
_WfIsdbPortDefaultCfgConnector_Object = MibTableColumn
wfIsdbPortDefaultCfgConnector = _WfIsdbPortDefaultCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 5),
    _WfIsdbPortDefaultCfgConnector_Type()
)
wfIsdbPortDefaultCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgConnector.setStatus("mandatory")
_WfIsdbPortDefaultCfgNumber_Type = Integer32
_WfIsdbPortDefaultCfgNumber_Object = MibTableColumn
wfIsdbPortDefaultCfgNumber = _WfIsdbPortDefaultCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 6),
    _WfIsdbPortDefaultCfgNumber_Type()
)
wfIsdbPortDefaultCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgNumber.setStatus("mandatory")


class _WfIsdbPortDefaultCfgBaudRate_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgBaudRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("baudrate1200b", 1200),
          ("baudrate19200b", 19200),
          ("baudrate2400b", 2400),
          ("baudrate300b", 300),
          ("baudrate4800b", 4800),
          ("baudrate9600b", 9600))
    )


_WfIsdbPortDefaultCfgBaudRate_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgBaudRate_Object = MibTableColumn
wfIsdbPortDefaultCfgBaudRate = _WfIsdbPortDefaultCfgBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 7),
    _WfIsdbPortDefaultCfgBaudRate_Type()
)
wfIsdbPortDefaultCfgBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgBaudRate.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDataBits_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDataBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_WfIsdbPortDefaultCfgDataBits_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDataBits_Object = MibTableColumn
wfIsdbPortDefaultCfgDataBits = _WfIsdbPortDefaultCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 8),
    _WfIsdbPortDefaultCfgDataBits_Type()
)
wfIsdbPortDefaultCfgDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDataBits.setStatus("mandatory")


class _WfIsdbPortDefaultCfgParity_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_WfIsdbPortDefaultCfgParity_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgParity_Object = MibTableColumn
wfIsdbPortDefaultCfgParity = _WfIsdbPortDefaultCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 9),
    _WfIsdbPortDefaultCfgParity_Type()
)
wfIsdbPortDefaultCfgParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgParity.setStatus("mandatory")


class _WfIsdbPortDefaultCfgStopBits_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgStopBits based on Integer32"""
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
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_WfIsdbPortDefaultCfgStopBits_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgStopBits_Object = MibTableColumn
wfIsdbPortDefaultCfgStopBits = _WfIsdbPortDefaultCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 10),
    _WfIsdbPortDefaultCfgStopBits_Type()
)
wfIsdbPortDefaultCfgStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgStopBits.setStatus("mandatory")


class _WfIsdbPortDefaultCfgCts_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgCts based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followFlowControl", 3),
          ("followRTS", 4))
    )


_WfIsdbPortDefaultCfgCts_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgCts_Object = MibTableColumn
wfIsdbPortDefaultCfgCts = _WfIsdbPortDefaultCfgCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 11),
    _WfIsdbPortDefaultCfgCts_Type()
)
wfIsdbPortDefaultCfgCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgCts.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDsr_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDsr based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followDTR", 3),
          ("toggleOnDisconnect", 4))
    )


_WfIsdbPortDefaultCfgDsr_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDsr_Object = MibTableColumn
wfIsdbPortDefaultCfgDsr = _WfIsdbPortDefaultCfgDsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 12),
    _WfIsdbPortDefaultCfgDsr_Type()
)
wfIsdbPortDefaultCfgDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDsr.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDcd_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDcd based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followDTR", 3),
          ("followVC", 4))
    )


_WfIsdbPortDefaultCfgDcd_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDcd_Object = MibTableColumn
wfIsdbPortDefaultCfgDcd = _WfIsdbPortDefaultCfgDcd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 13),
    _WfIsdbPortDefaultCfgDcd_Type()
)
wfIsdbPortDefaultCfgDcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDcd.setStatus("mandatory")


class _WfIsdbPortDefaultCfgPrompt_Type(DisplayString):
    """Custom type wfIsdbPortDefaultCfgPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WfIsdbPortDefaultCfgPrompt_Type.__name__ = "DisplayString"
_WfIsdbPortDefaultCfgPrompt_Object = MibTableColumn
wfIsdbPortDefaultCfgPrompt = _WfIsdbPortDefaultCfgPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 14),
    _WfIsdbPortDefaultCfgPrompt_Type()
)
wfIsdbPortDefaultCfgPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgPrompt.setStatus("mandatory")


class _WfIsdbPortDefaultCfgCommandParser_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgCommandParser based on Integer32"""
    defaultValue = 3

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
        *(("loopback", 4),
          ("menu", 1),
          ("test", 2),
          ("x25pad", 3))
    )


_WfIsdbPortDefaultCfgCommandParser_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgCommandParser_Object = MibTableColumn
wfIsdbPortDefaultCfgCommandParser = _WfIsdbPortDefaultCfgCommandParser_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 15),
    _WfIsdbPortDefaultCfgCommandParser_Type()
)
wfIsdbPortDefaultCfgCommandParser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgCommandParser.setStatus("mandatory")


class _WfIsdbPortDefaultCfgInactivityTimeOut_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgInactivityTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfIsdbPortDefaultCfgInactivityTimeOut_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgInactivityTimeOut_Object = MibTableColumn
wfIsdbPortDefaultCfgInactivityTimeOut = _WfIsdbPortDefaultCfgInactivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 16),
    _WfIsdbPortDefaultCfgInactivityTimeOut_Type()
)
wfIsdbPortDefaultCfgInactivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgInactivityTimeOut.setStatus("mandatory")


class _WfIsdbPortDefaultCfgRxQueueSize_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgRxQueueSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_WfIsdbPortDefaultCfgRxQueueSize_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgRxQueueSize_Object = MibTableColumn
wfIsdbPortDefaultCfgRxQueueSize = _WfIsdbPortDefaultCfgRxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 17),
    _WfIsdbPortDefaultCfgRxQueueSize_Type()
)
wfIsdbPortDefaultCfgRxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgRxQueueSize.setStatus("mandatory")


class _WfIsdbPortDefaultCfgTxQueueSize_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgTxQueueSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_WfIsdbPortDefaultCfgTxQueueSize_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgTxQueueSize_Object = MibTableColumn
wfIsdbPortDefaultCfgTxQueueSize = _WfIsdbPortDefaultCfgTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 18),
    _WfIsdbPortDefaultCfgTxQueueSize_Type()
)
wfIsdbPortDefaultCfgTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgTxQueueSize.setStatus("mandatory")


class _WfIsdbPortDefaultCfgRxXoff_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgRxXoff based on Integer32"""
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


_WfIsdbPortDefaultCfgRxXoff_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgRxXoff_Object = MibTableColumn
wfIsdbPortDefaultCfgRxXoff = _WfIsdbPortDefaultCfgRxXoff_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 19),
    _WfIsdbPortDefaultCfgRxXoff_Type()
)
wfIsdbPortDefaultCfgRxXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgRxXoff.setStatus("mandatory")


class _WfIsdbPortDefaultCfgTxXoff_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgTxXoff based on Integer32"""
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


_WfIsdbPortDefaultCfgTxXoff_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgTxXoff_Object = MibTableColumn
wfIsdbPortDefaultCfgTxXoff = _WfIsdbPortDefaultCfgTxXoff_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 20),
    _WfIsdbPortDefaultCfgTxXoff_Type()
)
wfIsdbPortDefaultCfgTxXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgTxXoff.setStatus("mandatory")


class _WfIsdbPortDefaultCfgDtrAction_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgDtrAction based on Integer32"""
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


_WfIsdbPortDefaultCfgDtrAction_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgDtrAction_Object = MibTableColumn
wfIsdbPortDefaultCfgDtrAction = _WfIsdbPortDefaultCfgDtrAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 21),
    _WfIsdbPortDefaultCfgDtrAction_Type()
)
wfIsdbPortDefaultCfgDtrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgDtrAction.setStatus("mandatory")


class _WfIsdbPortDefaultCfgRxXoffAction_Type(Integer32):
    """Custom type wfIsdbPortDefaultCfgRxXoffAction based on Integer32"""
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


_WfIsdbPortDefaultCfgRxXoffAction_Type.__name__ = "Integer32"
_WfIsdbPortDefaultCfgRxXoffAction_Object = MibTableColumn
wfIsdbPortDefaultCfgRxXoffAction = _WfIsdbPortDefaultCfgRxXoffAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 3, 1, 22),
    _WfIsdbPortDefaultCfgRxXoffAction_Type()
)
wfIsdbPortDefaultCfgRxXoffAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIsdbPortDefaultCfgRxXoffAction.setStatus("mandatory")
_WfIsdbPortCurrentCfgTable_Object = MibTable
wfIsdbPortCurrentCfgTable = _WfIsdbPortCurrentCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4)
)
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgTable.setStatus("mandatory")
_WfIsdbPortCurrentCfgEntry_Object = MibTableRow
wfIsdbPortCurrentCfgEntry = _WfIsdbPortCurrentCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1)
)
wfIsdbPortCurrentCfgEntry.setIndexNames(
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortCurrentCfgSlot"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortCurrentCfgConnector"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortCurrentCfgNumber"),
)
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgEntry.setStatus("mandatory")


class _WfIsdbPortCurrentCfgState_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfIsdbPortCurrentCfgState_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgState_Object = MibTableColumn
wfIsdbPortCurrentCfgState = _WfIsdbPortCurrentCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 1),
    _WfIsdbPortCurrentCfgState_Type()
)
wfIsdbPortCurrentCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgState.setStatus("mandatory")
_WfIsdbPortCurrentCfgSlot_Type = Integer32
_WfIsdbPortCurrentCfgSlot_Object = MibTableColumn
wfIsdbPortCurrentCfgSlot = _WfIsdbPortCurrentCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 2),
    _WfIsdbPortCurrentCfgSlot_Type()
)
wfIsdbPortCurrentCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgSlot.setStatus("mandatory")
_WfIsdbPortCurrentCfgConnector_Type = Integer32
_WfIsdbPortCurrentCfgConnector_Object = MibTableColumn
wfIsdbPortCurrentCfgConnector = _WfIsdbPortCurrentCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 3),
    _WfIsdbPortCurrentCfgConnector_Type()
)
wfIsdbPortCurrentCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgConnector.setStatus("mandatory")
_WfIsdbPortCurrentCfgNumber_Type = Integer32
_WfIsdbPortCurrentCfgNumber_Object = MibTableColumn
wfIsdbPortCurrentCfgNumber = _WfIsdbPortCurrentCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 4),
    _WfIsdbPortCurrentCfgNumber_Type()
)
wfIsdbPortCurrentCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgNumber.setStatus("mandatory")


class _WfIsdbPortCurrentCfgBaudRate_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("baudrate1200b", 1200),
          ("baudrate19200b", 19200),
          ("baudrate2400b", 2400),
          ("baudrate300b", 300),
          ("baudrate4800b", 4800),
          ("baudrate9600b", 9600))
    )


_WfIsdbPortCurrentCfgBaudRate_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgBaudRate_Object = MibTableColumn
wfIsdbPortCurrentCfgBaudRate = _WfIsdbPortCurrentCfgBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 5),
    _WfIsdbPortCurrentCfgBaudRate_Type()
)
wfIsdbPortCurrentCfgBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgBaudRate.setStatus("mandatory")


class _WfIsdbPortCurrentCfgDataBits_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_WfIsdbPortCurrentCfgDataBits_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgDataBits_Object = MibTableColumn
wfIsdbPortCurrentCfgDataBits = _WfIsdbPortCurrentCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 6),
    _WfIsdbPortCurrentCfgDataBits_Type()
)
wfIsdbPortCurrentCfgDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgDataBits.setStatus("mandatory")


class _WfIsdbPortCurrentCfgParity_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_WfIsdbPortCurrentCfgParity_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgParity_Object = MibTableColumn
wfIsdbPortCurrentCfgParity = _WfIsdbPortCurrentCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 7),
    _WfIsdbPortCurrentCfgParity_Type()
)
wfIsdbPortCurrentCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgParity.setStatus("mandatory")


class _WfIsdbPortCurrentCfgStopBits_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_WfIsdbPortCurrentCfgStopBits_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgStopBits_Object = MibTableColumn
wfIsdbPortCurrentCfgStopBits = _WfIsdbPortCurrentCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 8),
    _WfIsdbPortCurrentCfgStopBits_Type()
)
wfIsdbPortCurrentCfgStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgStopBits.setStatus("mandatory")


class _WfIsdbPortCurrentCfgCts_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgCts based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followFlowControl", 3),
          ("followRTS", 4))
    )


_WfIsdbPortCurrentCfgCts_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgCts_Object = MibTableColumn
wfIsdbPortCurrentCfgCts = _WfIsdbPortCurrentCfgCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 9),
    _WfIsdbPortCurrentCfgCts_Type()
)
wfIsdbPortCurrentCfgCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgCts.setStatus("mandatory")


class _WfIsdbPortCurrentCfgDsr_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgDsr based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followDTR", 3),
          ("toggleOnDisconnect", 4))
    )


_WfIsdbPortCurrentCfgDsr_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgDsr_Object = MibTableColumn
wfIsdbPortCurrentCfgDsr = _WfIsdbPortCurrentCfgDsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 10),
    _WfIsdbPortCurrentCfgDsr_Type()
)
wfIsdbPortCurrentCfgDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgDsr.setStatus("mandatory")


class _WfIsdbPortCurrentCfgDcd_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgDcd based on Integer32"""
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
        *(("alwaysOff", 2),
          ("alwaysOn", 1),
          ("followDTR", 3),
          ("followVC", 4))
    )


_WfIsdbPortCurrentCfgDcd_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgDcd_Object = MibTableColumn
wfIsdbPortCurrentCfgDcd = _WfIsdbPortCurrentCfgDcd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 11),
    _WfIsdbPortCurrentCfgDcd_Type()
)
wfIsdbPortCurrentCfgDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgDcd.setStatus("mandatory")


class _WfIsdbPortCurrentCfgPrompt_Type(DisplayString):
    """Custom type wfIsdbPortCurrentCfgPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WfIsdbPortCurrentCfgPrompt_Type.__name__ = "DisplayString"
_WfIsdbPortCurrentCfgPrompt_Object = MibTableColumn
wfIsdbPortCurrentCfgPrompt = _WfIsdbPortCurrentCfgPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 12),
    _WfIsdbPortCurrentCfgPrompt_Type()
)
wfIsdbPortCurrentCfgPrompt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgPrompt.setStatus("mandatory")


class _WfIsdbPortCurrentCfgCommandParser_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgCommandParser based on Integer32"""
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
        *(("loopback", 4),
          ("menu", 1),
          ("test", 2),
          ("x25pad", 3))
    )


_WfIsdbPortCurrentCfgCommandParser_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgCommandParser_Object = MibTableColumn
wfIsdbPortCurrentCfgCommandParser = _WfIsdbPortCurrentCfgCommandParser_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 13),
    _WfIsdbPortCurrentCfgCommandParser_Type()
)
wfIsdbPortCurrentCfgCommandParser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgCommandParser.setStatus("mandatory")


class _WfIsdbPortCurrentCfgInactivityTimeout_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfIsdbPortCurrentCfgInactivityTimeout_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgInactivityTimeout_Object = MibTableColumn
wfIsdbPortCurrentCfgInactivityTimeout = _WfIsdbPortCurrentCfgInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 14),
    _WfIsdbPortCurrentCfgInactivityTimeout_Type()
)
wfIsdbPortCurrentCfgInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgInactivityTimeout.setStatus("mandatory")


class _WfIsdbPortCurrentCfgRxQueueSize_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgRxQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_WfIsdbPortCurrentCfgRxQueueSize_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgRxQueueSize_Object = MibTableColumn
wfIsdbPortCurrentCfgRxQueueSize = _WfIsdbPortCurrentCfgRxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 15),
    _WfIsdbPortCurrentCfgRxQueueSize_Type()
)
wfIsdbPortCurrentCfgRxQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgRxQueueSize.setStatus("mandatory")


class _WfIsdbPortCurrentCfgTxQueueSize_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgTxQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_WfIsdbPortCurrentCfgTxQueueSize_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgTxQueueSize_Object = MibTableColumn
wfIsdbPortCurrentCfgTxQueueSize = _WfIsdbPortCurrentCfgTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 16),
    _WfIsdbPortCurrentCfgTxQueueSize_Type()
)
wfIsdbPortCurrentCfgTxQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgTxQueueSize.setStatus("mandatory")


class _WfIsdbPortCurrentCfgRxXoff_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgRxXoff based on Integer32"""
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


_WfIsdbPortCurrentCfgRxXoff_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgRxXoff_Object = MibTableColumn
wfIsdbPortCurrentCfgRxXoff = _WfIsdbPortCurrentCfgRxXoff_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 17),
    _WfIsdbPortCurrentCfgRxXoff_Type()
)
wfIsdbPortCurrentCfgRxXoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgRxXoff.setStatus("mandatory")


class _WfIsdbPortCurrentCfgTxXoff_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgTxXoff based on Integer32"""
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


_WfIsdbPortCurrentCfgTxXoff_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgTxXoff_Object = MibTableColumn
wfIsdbPortCurrentCfgTxXoff = _WfIsdbPortCurrentCfgTxXoff_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 18),
    _WfIsdbPortCurrentCfgTxXoff_Type()
)
wfIsdbPortCurrentCfgTxXoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgTxXoff.setStatus("mandatory")


class _WfIsdbPortCurrentCfgDtrAction_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgDtrAction based on Integer32"""
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


_WfIsdbPortCurrentCfgDtrAction_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgDtrAction_Object = MibTableColumn
wfIsdbPortCurrentCfgDtrAction = _WfIsdbPortCurrentCfgDtrAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 19),
    _WfIsdbPortCurrentCfgDtrAction_Type()
)
wfIsdbPortCurrentCfgDtrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgDtrAction.setStatus("mandatory")


class _WfIsdbPortCurrentCfgRxXoffAction_Type(Integer32):
    """Custom type wfIsdbPortCurrentCfgRxXoffAction based on Integer32"""
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


_WfIsdbPortCurrentCfgRxXoffAction_Type.__name__ = "Integer32"
_WfIsdbPortCurrentCfgRxXoffAction_Object = MibTableColumn
wfIsdbPortCurrentCfgRxXoffAction = _WfIsdbPortCurrentCfgRxXoffAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 4, 1, 20),
    _WfIsdbPortCurrentCfgRxXoffAction_Type()
)
wfIsdbPortCurrentCfgRxXoffAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortCurrentCfgRxXoffAction.setStatus("mandatory")
_WfIsdbPortStatTable_Object = MibTable
wfIsdbPortStatTable = _WfIsdbPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5)
)
if mibBuilder.loadTexts:
    wfIsdbPortStatTable.setStatus("mandatory")
_WfIsdbPortStatEntry_Object = MibTableRow
wfIsdbPortStatEntry = _WfIsdbPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1)
)
wfIsdbPortStatEntry.setIndexNames(
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortStatSlot"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortStatConnector"),
    (0, "Wellfleet-ISDB-MIB", "wfIsdbPortStatNumber"),
)
if mibBuilder.loadTexts:
    wfIsdbPortStatEntry.setStatus("mandatory")


class _WfIsdbPortStatState_Type(Integer32):
    """Custom type wfIsdbPortStatState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfIsdbPortStatState_Type.__name__ = "Integer32"
_WfIsdbPortStatState_Object = MibTableColumn
wfIsdbPortStatState = _WfIsdbPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 1),
    _WfIsdbPortStatState_Type()
)
wfIsdbPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatState.setStatus("mandatory")
_WfIsdbPortStatSlot_Type = Integer32
_WfIsdbPortStatSlot_Object = MibTableColumn
wfIsdbPortStatSlot = _WfIsdbPortStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 2),
    _WfIsdbPortStatSlot_Type()
)
wfIsdbPortStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatSlot.setStatus("mandatory")
_WfIsdbPortStatConnector_Type = Integer32
_WfIsdbPortStatConnector_Object = MibTableColumn
wfIsdbPortStatConnector = _WfIsdbPortStatConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 3),
    _WfIsdbPortStatConnector_Type()
)
wfIsdbPortStatConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatConnector.setStatus("mandatory")
_WfIsdbPortStatNumber_Type = Integer32
_WfIsdbPortStatNumber_Object = MibTableColumn
wfIsdbPortStatNumber = _WfIsdbPortStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 4),
    _WfIsdbPortStatNumber_Type()
)
wfIsdbPortStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatNumber.setStatus("mandatory")
_WfIsdbPortStatRxOctets_Type = Counter32
_WfIsdbPortStatRxOctets_Object = MibTableColumn
wfIsdbPortStatRxOctets = _WfIsdbPortStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 5),
    _WfIsdbPortStatRxOctets_Type()
)
wfIsdbPortStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxOctets.setStatus("mandatory")
_WfIsdbPortStatRxLacks_Type = Counter32
_WfIsdbPortStatRxLacks_Object = MibTableColumn
wfIsdbPortStatRxLacks = _WfIsdbPortStatRxLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 6),
    _WfIsdbPortStatRxLacks_Type()
)
wfIsdbPortStatRxLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxLacks.setStatus("mandatory")
_WfIsdbPortStatRxWaits_Type = Counter32
_WfIsdbPortStatRxWaits_Object = MibTableColumn
wfIsdbPortStatRxWaits = _WfIsdbPortStatRxWaits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 7),
    _WfIsdbPortStatRxWaits_Type()
)
wfIsdbPortStatRxWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxWaits.setStatus("mandatory")
_WfIsdbPortStatTxOctets_Type = Counter32
_WfIsdbPortStatTxOctets_Object = MibTableColumn
wfIsdbPortStatTxOctets = _WfIsdbPortStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 8),
    _WfIsdbPortStatTxOctets_Type()
)
wfIsdbPortStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxOctets.setStatus("mandatory")
_WfIsdbPortStatTxLacks_Type = Counter32
_WfIsdbPortStatTxLacks_Object = MibTableColumn
wfIsdbPortStatTxLacks = _WfIsdbPortStatTxLacks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 9),
    _WfIsdbPortStatTxLacks_Type()
)
wfIsdbPortStatTxLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxLacks.setStatus("mandatory")
_WfIsdbPortStatTxWaits_Type = Counter32
_WfIsdbPortStatTxWaits_Object = MibTableColumn
wfIsdbPortStatTxWaits = _WfIsdbPortStatTxWaits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 10),
    _WfIsdbPortStatTxWaits_Type()
)
wfIsdbPortStatTxWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxWaits.setStatus("mandatory")
_WfIsdbPortStatBreaksDetected_Type = Counter32
_WfIsdbPortStatBreaksDetected_Object = MibTableColumn
wfIsdbPortStatBreaksDetected = _WfIsdbPortStatBreaksDetected_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 11),
    _WfIsdbPortStatBreaksDetected_Type()
)
wfIsdbPortStatBreaksDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatBreaksDetected.setStatus("mandatory")
_WfIsdbPortStatParityErrors_Type = Counter32
_WfIsdbPortStatParityErrors_Object = MibTableColumn
wfIsdbPortStatParityErrors = _WfIsdbPortStatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 12),
    _WfIsdbPortStatParityErrors_Type()
)
wfIsdbPortStatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatParityErrors.setStatus("mandatory")
_WfIsdbPortStatFramingErrors_Type = Counter32
_WfIsdbPortStatFramingErrors_Object = MibTableColumn
wfIsdbPortStatFramingErrors = _WfIsdbPortStatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 13),
    _WfIsdbPortStatFramingErrors_Type()
)
wfIsdbPortStatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatFramingErrors.setStatus("mandatory")
_WfIsdbPortStatOverrunErrors_Type = Counter32
_WfIsdbPortStatOverrunErrors_Object = MibTableColumn
wfIsdbPortStatOverrunErrors = _WfIsdbPortStatOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 14),
    _WfIsdbPortStatOverrunErrors_Type()
)
wfIsdbPortStatOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatOverrunErrors.setStatus("mandatory")


class _WfIsdbPortStatCtsState_Type(Integer32):
    """Custom type wfIsdbPortStatCtsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatCtsState_Type.__name__ = "Integer32"
_WfIsdbPortStatCtsState_Object = MibTableColumn
wfIsdbPortStatCtsState = _WfIsdbPortStatCtsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 15),
    _WfIsdbPortStatCtsState_Type()
)
wfIsdbPortStatCtsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatCtsState.setStatus("mandatory")
_WfIsdbPortStatCtsTransitions_Type = Counter32
_WfIsdbPortStatCtsTransitions_Object = MibTableColumn
wfIsdbPortStatCtsTransitions = _WfIsdbPortStatCtsTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 16),
    _WfIsdbPortStatCtsTransitions_Type()
)
wfIsdbPortStatCtsTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatCtsTransitions.setStatus("mandatory")


class _WfIsdbPortStatRtsState_Type(Integer32):
    """Custom type wfIsdbPortStatRtsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatRtsState_Type.__name__ = "Integer32"
_WfIsdbPortStatRtsState_Object = MibTableColumn
wfIsdbPortStatRtsState = _WfIsdbPortStatRtsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 17),
    _WfIsdbPortStatRtsState_Type()
)
wfIsdbPortStatRtsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRtsState.setStatus("mandatory")
_WfIsdbPortStatRtsTransitions_Type = Counter32
_WfIsdbPortStatRtsTransitions_Object = MibTableColumn
wfIsdbPortStatRtsTransitions = _WfIsdbPortStatRtsTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 18),
    _WfIsdbPortStatRtsTransitions_Type()
)
wfIsdbPortStatRtsTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRtsTransitions.setStatus("mandatory")


class _WfIsdbPortStatDsrState_Type(Integer32):
    """Custom type wfIsdbPortStatDsrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatDsrState_Type.__name__ = "Integer32"
_WfIsdbPortStatDsrState_Object = MibTableColumn
wfIsdbPortStatDsrState = _WfIsdbPortStatDsrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 19),
    _WfIsdbPortStatDsrState_Type()
)
wfIsdbPortStatDsrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDsrState.setStatus("mandatory")
_WfIsdbPortStatDsrTransitions_Type = Counter32
_WfIsdbPortStatDsrTransitions_Object = MibTableColumn
wfIsdbPortStatDsrTransitions = _WfIsdbPortStatDsrTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 20),
    _WfIsdbPortStatDsrTransitions_Type()
)
wfIsdbPortStatDsrTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDsrTransitions.setStatus("mandatory")


class _WfIsdbPortStatDcdState_Type(Integer32):
    """Custom type wfIsdbPortStatDcdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatDcdState_Type.__name__ = "Integer32"
_WfIsdbPortStatDcdState_Object = MibTableColumn
wfIsdbPortStatDcdState = _WfIsdbPortStatDcdState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 21),
    _WfIsdbPortStatDcdState_Type()
)
wfIsdbPortStatDcdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDcdState.setStatus("mandatory")
_WfIsdbPortStatDcdTransitions_Type = Counter32
_WfIsdbPortStatDcdTransitions_Object = MibTableColumn
wfIsdbPortStatDcdTransitions = _WfIsdbPortStatDcdTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 22),
    _WfIsdbPortStatDcdTransitions_Type()
)
wfIsdbPortStatDcdTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDcdTransitions.setStatus("mandatory")


class _WfIsdbPortStatDtrState_Type(Integer32):
    """Custom type wfIsdbPortStatDtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatDtrState_Type.__name__ = "Integer32"
_WfIsdbPortStatDtrState_Object = MibTableColumn
wfIsdbPortStatDtrState = _WfIsdbPortStatDtrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 23),
    _WfIsdbPortStatDtrState_Type()
)
wfIsdbPortStatDtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDtrState.setStatus("mandatory")
_WfIsdbPortStatDtrTransitions_Type = Counter32
_WfIsdbPortStatDtrTransitions_Object = MibTableColumn
wfIsdbPortStatDtrTransitions = _WfIsdbPortStatDtrTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 24),
    _WfIsdbPortStatDtrTransitions_Type()
)
wfIsdbPortStatDtrTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatDtrTransitions.setStatus("mandatory")
_WfIsdbPortStatRxInts_Type = Counter32
_WfIsdbPortStatRxInts_Object = MibTableColumn
wfIsdbPortStatRxInts = _WfIsdbPortStatRxInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 25),
    _WfIsdbPortStatRxInts_Type()
)
wfIsdbPortStatRxInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxInts.setStatus("mandatory")
_WfIsdbPortStatTxInts_Type = Counter32
_WfIsdbPortStatTxInts_Object = MibTableColumn
wfIsdbPortStatTxInts = _WfIsdbPortStatTxInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 26),
    _WfIsdbPortStatTxInts_Type()
)
wfIsdbPortStatTxInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxInts.setStatus("mandatory")
_WfIsdbPortStatModemInts_Type = Counter32
_WfIsdbPortStatModemInts_Object = MibTableColumn
wfIsdbPortStatModemInts = _WfIsdbPortStatModemInts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 27),
    _WfIsdbPortStatModemInts_Type()
)
wfIsdbPortStatModemInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatModemInts.setStatus("mandatory")
_WfIsdbPortStatSpecialCharCount_Type = Counter32
_WfIsdbPortStatSpecialCharCount_Object = MibTableColumn
wfIsdbPortStatSpecialCharCount = _WfIsdbPortStatSpecialCharCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 28),
    _WfIsdbPortStatSpecialCharCount_Type()
)
wfIsdbPortStatSpecialCharCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatSpecialCharCount.setStatus("mandatory")


class _WfIsdbPortStatRxState_Type(Integer32):
    """Custom type wfIsdbPortStatRxState based on Integer32"""
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


_WfIsdbPortStatRxState_Type.__name__ = "Integer32"
_WfIsdbPortStatRxState_Object = MibTableColumn
wfIsdbPortStatRxState = _WfIsdbPortStatRxState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 29),
    _WfIsdbPortStatRxState_Type()
)
wfIsdbPortStatRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxState.setStatus("mandatory")


class _WfIsdbPortStatRxFlowState_Type(Integer32):
    """Custom type wfIsdbPortStatRxFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatRxFlowState_Type.__name__ = "Integer32"
_WfIsdbPortStatRxFlowState_Object = MibTableColumn
wfIsdbPortStatRxFlowState = _WfIsdbPortStatRxFlowState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 30),
    _WfIsdbPortStatRxFlowState_Type()
)
wfIsdbPortStatRxFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatRxFlowState.setStatus("mandatory")


class _WfIsdbPortStatTxState_Type(Integer32):
    """Custom type wfIsdbPortStatTxState based on Integer32"""
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


_WfIsdbPortStatTxState_Type.__name__ = "Integer32"
_WfIsdbPortStatTxState_Object = MibTableColumn
wfIsdbPortStatTxState = _WfIsdbPortStatTxState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 31),
    _WfIsdbPortStatTxState_Type()
)
wfIsdbPortStatTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxState.setStatus("mandatory")


class _WfIsdbPortStatTxFlowState_Type(Integer32):
    """Custom type wfIsdbPortStatTxFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("off", 2),
          ("on", 1))
    )


_WfIsdbPortStatTxFlowState_Type.__name__ = "Integer32"
_WfIsdbPortStatTxFlowState_Object = MibTableColumn
wfIsdbPortStatTxFlowState = _WfIsdbPortStatTxFlowState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33, 5, 1, 32),
    _WfIsdbPortStatTxFlowState_Type()
)
wfIsdbPortStatTxFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIsdbPortStatTxFlowState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ISDB-MIB",
    **{"wfIsdbCfgTable": wfIsdbCfgTable,
       "wfIsdbCfgEntry": wfIsdbCfgEntry,
       "wfIsdbCfgDelete": wfIsdbCfgDelete,
       "wfIsdbCfgDisable": wfIsdbCfgDisable,
       "wfIsdbCfgState": wfIsdbCfgState,
       "wfIsdbCfgSlot": wfIsdbCfgSlot,
       "wfIsdbCfgConnector": wfIsdbCfgConnector,
       "wfIsdbCfgCircuit": wfIsdbCfgCircuit,
       "wfIsdbCfgLogFilter": wfIsdbCfgLogFilter,
       "wfIsdbCfgPollInterval": wfIsdbCfgPollInterval,
       "wfIsdbCfgAutoRestart": wfIsdbCfgAutoRestart,
       "wfIsdbCfgAutoUld": wfIsdbCfgAutoUld,
       "wfIsdbCfgUldVolume": wfIsdbCfgUldVolume,
       "wfIsdbImageVersion": wfIsdbImageVersion,
       "wfIsdbImageDate": wfIsdbImageDate,
       "wfIsdbDiagVersion": wfIsdbDiagVersion,
       "wfIsdbDiagDate": wfIsdbDiagDate,
       "wfIsdbStatTable": wfIsdbStatTable,
       "wfIsdbStatEntry": wfIsdbStatEntry,
       "wfIsdbStatState": wfIsdbStatState,
       "wfIsdbStatSlot": wfIsdbStatSlot,
       "wfIsdbStatConnector": wfIsdbStatConnector,
       "wfIsdbStatVersion": wfIsdbStatVersion,
       "wfIsdbStatCurrentConnCount": wfIsdbStatCurrentConnCount,
       "wfIsdbStatTotalConnCount": wfIsdbStatTotalConnCount,
       "wfIsdbStatStartCount": wfIsdbStatStartCount,
       "wfIsdbStatCpuIdleCurrent": wfIsdbStatCpuIdleCurrent,
       "wfIsdbStatCpuIdleTotal": wfIsdbStatCpuIdleTotal,
       "wfIsdbStatMemoryFree": wfIsdbStatMemoryFree,
       "wfIsdbStatMemoryLargestBlock": wfIsdbStatMemoryLargestBlock,
       "wfIsdbStatTaskCount": wfIsdbStatTaskCount,
       "wfIsdbStatMsgQueueLacks": wfIsdbStatMsgQueueLacks,
       "wfIsdbStatHardwareTimeouts": wfIsdbStatHardwareTimeouts,
       "wfIsdbStatAlarmCount": wfIsdbStatAlarmCount,
       "wfIsdbStatAuthorUnknown": wfIsdbStatAuthorUnknown,
       "wfIsdbStatAv1Ints": wfIsdbStatAv1Ints,
       "wfIsdbStatAv2Ints": wfIsdbStatAv2Ints,
       "wfIsdbStatAv3Ints": wfIsdbStatAv3Ints,
       "wfIsdbStatAv4Ints": wfIsdbStatAv4Ints,
       "wfIsdbStatAv5Ints": wfIsdbStatAv5Ints,
       "wfIsdbStatAv6Ints": wfIsdbStatAv6Ints,
       "wfIsdbStatAv7Ints": wfIsdbStatAv7Ints,
       "wfIsdbStatScc3Ints": wfIsdbStatScc3Ints,
       "wfIsdbStatErrorInts": wfIsdbStatErrorInts,
       "wfIsdbStatTimer1Ints": wfIsdbStatTimer1Ints,
       "wfIsdbStatTimer2Ints": wfIsdbStatTimer2Ints,
       "wfIsdbStatTimer3Ints": wfIsdbStatTimer3Ints,
       "wfIsdbStatTimer4Ints": wfIsdbStatTimer4Ints,
       "wfIsdbStatBusErrors": wfIsdbStatBusErrors,
       "wfIsdbStatRxFrames": wfIsdbStatRxFrames,
       "wfIsdbStatRxOctets": wfIsdbStatRxOctets,
       "wfIsdbStatRxLacks": wfIsdbStatRxLacks,
       "wfIsdbStatRxDataLinkMsgLacks": wfIsdbStatRxDataLinkMsgLacks,
       "wfIsdbStatRxManagementMsgLacks": wfIsdbStatRxManagementMsgLacks,
       "wfIsdbStatRxBadFrames": wfIsdbStatRxBadFrames,
       "wfIsdbStatRxOverFlows": wfIsdbStatRxOverFlows,
       "wfIsdbStatRxRunts": wfIsdbStatRxRunts,
       "wfIsdbStatRxLargeFrames": wfIsdbStatRxLargeFrames,
       "wfIsdbStatRxSmallFrames": wfIsdbStatRxSmallFrames,
       "wfIsdbStatRxIncompleteFrames": wfIsdbStatRxIncompleteFrames,
       "wfIsdbStatRxInts": wfIsdbStatRxInts,
       "wfIsdbStatRxDataLinkFrames": wfIsdbStatRxDataLinkFrames,
       "wfIsdbStatRxDataLinkDiscards": wfIsdbStatRxDataLinkDiscards,
       "wfIsdbStatRxManagementFrames": wfIsdbStatRxManagementFrames,
       "wfIsdbStatRxUnknownFrames": wfIsdbStatRxUnknownFrames,
       "wfIsdbStatTxFrames": wfIsdbStatTxFrames,
       "wfIsdbStatTxOctets": wfIsdbStatTxOctets,
       "wfIsdbStatTxLacks": wfIsdbStatTxLacks,
       "wfIsdbStatTxUnderFlows": wfIsdbStatTxUnderFlows,
       "wfIsdbStatTxAbortedFrames": wfIsdbStatTxAbortedFrames,
       "wfIsdbStatTxMsgs": wfIsdbStatTxMsgs,
       "wfIsdbStatTxLargeMsgs": wfIsdbStatTxLargeMsgs,
       "wfIsdbStatTxSmallMsgs": wfIsdbStatTxSmallMsgs,
       "wfIsdbStatTxInts": wfIsdbStatTxInts,
       "wfIsdbStatTxDataLinkFrames": wfIsdbStatTxDataLinkFrames,
       "wfIsdbStatTxManagementFrames": wfIsdbStatTxManagementFrames,
       "wfIsdbStatTxUnknownFrames": wfIsdbStatTxUnknownFrames,
       "wfIsdbPortDefaultCfgTable": wfIsdbPortDefaultCfgTable,
       "wfIsdbPortDefaultCfgEntry": wfIsdbPortDefaultCfgEntry,
       "wfIsdbPortDefaultCfgDelete": wfIsdbPortDefaultCfgDelete,
       "wfIsdbPortDefaultCfgDisable": wfIsdbPortDefaultCfgDisable,
       "wfIsdbPortDefaultCfgState": wfIsdbPortDefaultCfgState,
       "wfIsdbPortDefaultCfgSlot": wfIsdbPortDefaultCfgSlot,
       "wfIsdbPortDefaultCfgConnector": wfIsdbPortDefaultCfgConnector,
       "wfIsdbPortDefaultCfgNumber": wfIsdbPortDefaultCfgNumber,
       "wfIsdbPortDefaultCfgBaudRate": wfIsdbPortDefaultCfgBaudRate,
       "wfIsdbPortDefaultCfgDataBits": wfIsdbPortDefaultCfgDataBits,
       "wfIsdbPortDefaultCfgParity": wfIsdbPortDefaultCfgParity,
       "wfIsdbPortDefaultCfgStopBits": wfIsdbPortDefaultCfgStopBits,
       "wfIsdbPortDefaultCfgCts": wfIsdbPortDefaultCfgCts,
       "wfIsdbPortDefaultCfgDsr": wfIsdbPortDefaultCfgDsr,
       "wfIsdbPortDefaultCfgDcd": wfIsdbPortDefaultCfgDcd,
       "wfIsdbPortDefaultCfgPrompt": wfIsdbPortDefaultCfgPrompt,
       "wfIsdbPortDefaultCfgCommandParser": wfIsdbPortDefaultCfgCommandParser,
       "wfIsdbPortDefaultCfgInactivityTimeOut": wfIsdbPortDefaultCfgInactivityTimeOut,
       "wfIsdbPortDefaultCfgRxQueueSize": wfIsdbPortDefaultCfgRxQueueSize,
       "wfIsdbPortDefaultCfgTxQueueSize": wfIsdbPortDefaultCfgTxQueueSize,
       "wfIsdbPortDefaultCfgRxXoff": wfIsdbPortDefaultCfgRxXoff,
       "wfIsdbPortDefaultCfgTxXoff": wfIsdbPortDefaultCfgTxXoff,
       "wfIsdbPortDefaultCfgDtrAction": wfIsdbPortDefaultCfgDtrAction,
       "wfIsdbPortDefaultCfgRxXoffAction": wfIsdbPortDefaultCfgRxXoffAction,
       "wfIsdbPortCurrentCfgTable": wfIsdbPortCurrentCfgTable,
       "wfIsdbPortCurrentCfgEntry": wfIsdbPortCurrentCfgEntry,
       "wfIsdbPortCurrentCfgState": wfIsdbPortCurrentCfgState,
       "wfIsdbPortCurrentCfgSlot": wfIsdbPortCurrentCfgSlot,
       "wfIsdbPortCurrentCfgConnector": wfIsdbPortCurrentCfgConnector,
       "wfIsdbPortCurrentCfgNumber": wfIsdbPortCurrentCfgNumber,
       "wfIsdbPortCurrentCfgBaudRate": wfIsdbPortCurrentCfgBaudRate,
       "wfIsdbPortCurrentCfgDataBits": wfIsdbPortCurrentCfgDataBits,
       "wfIsdbPortCurrentCfgParity": wfIsdbPortCurrentCfgParity,
       "wfIsdbPortCurrentCfgStopBits": wfIsdbPortCurrentCfgStopBits,
       "wfIsdbPortCurrentCfgCts": wfIsdbPortCurrentCfgCts,
       "wfIsdbPortCurrentCfgDsr": wfIsdbPortCurrentCfgDsr,
       "wfIsdbPortCurrentCfgDcd": wfIsdbPortCurrentCfgDcd,
       "wfIsdbPortCurrentCfgPrompt": wfIsdbPortCurrentCfgPrompt,
       "wfIsdbPortCurrentCfgCommandParser": wfIsdbPortCurrentCfgCommandParser,
       "wfIsdbPortCurrentCfgInactivityTimeout": wfIsdbPortCurrentCfgInactivityTimeout,
       "wfIsdbPortCurrentCfgRxQueueSize": wfIsdbPortCurrentCfgRxQueueSize,
       "wfIsdbPortCurrentCfgTxQueueSize": wfIsdbPortCurrentCfgTxQueueSize,
       "wfIsdbPortCurrentCfgRxXoff": wfIsdbPortCurrentCfgRxXoff,
       "wfIsdbPortCurrentCfgTxXoff": wfIsdbPortCurrentCfgTxXoff,
       "wfIsdbPortCurrentCfgDtrAction": wfIsdbPortCurrentCfgDtrAction,
       "wfIsdbPortCurrentCfgRxXoffAction": wfIsdbPortCurrentCfgRxXoffAction,
       "wfIsdbPortStatTable": wfIsdbPortStatTable,
       "wfIsdbPortStatEntry": wfIsdbPortStatEntry,
       "wfIsdbPortStatState": wfIsdbPortStatState,
       "wfIsdbPortStatSlot": wfIsdbPortStatSlot,
       "wfIsdbPortStatConnector": wfIsdbPortStatConnector,
       "wfIsdbPortStatNumber": wfIsdbPortStatNumber,
       "wfIsdbPortStatRxOctets": wfIsdbPortStatRxOctets,
       "wfIsdbPortStatRxLacks": wfIsdbPortStatRxLacks,
       "wfIsdbPortStatRxWaits": wfIsdbPortStatRxWaits,
       "wfIsdbPortStatTxOctets": wfIsdbPortStatTxOctets,
       "wfIsdbPortStatTxLacks": wfIsdbPortStatTxLacks,
       "wfIsdbPortStatTxWaits": wfIsdbPortStatTxWaits,
       "wfIsdbPortStatBreaksDetected": wfIsdbPortStatBreaksDetected,
       "wfIsdbPortStatParityErrors": wfIsdbPortStatParityErrors,
       "wfIsdbPortStatFramingErrors": wfIsdbPortStatFramingErrors,
       "wfIsdbPortStatOverrunErrors": wfIsdbPortStatOverrunErrors,
       "wfIsdbPortStatCtsState": wfIsdbPortStatCtsState,
       "wfIsdbPortStatCtsTransitions": wfIsdbPortStatCtsTransitions,
       "wfIsdbPortStatRtsState": wfIsdbPortStatRtsState,
       "wfIsdbPortStatRtsTransitions": wfIsdbPortStatRtsTransitions,
       "wfIsdbPortStatDsrState": wfIsdbPortStatDsrState,
       "wfIsdbPortStatDsrTransitions": wfIsdbPortStatDsrTransitions,
       "wfIsdbPortStatDcdState": wfIsdbPortStatDcdState,
       "wfIsdbPortStatDcdTransitions": wfIsdbPortStatDcdTransitions,
       "wfIsdbPortStatDtrState": wfIsdbPortStatDtrState,
       "wfIsdbPortStatDtrTransitions": wfIsdbPortStatDtrTransitions,
       "wfIsdbPortStatRxInts": wfIsdbPortStatRxInts,
       "wfIsdbPortStatTxInts": wfIsdbPortStatTxInts,
       "wfIsdbPortStatModemInts": wfIsdbPortStatModemInts,
       "wfIsdbPortStatSpecialCharCount": wfIsdbPortStatSpecialCharCount,
       "wfIsdbPortStatRxState": wfIsdbPortStatRxState,
       "wfIsdbPortStatRxFlowState": wfIsdbPortStatRxFlowState,
       "wfIsdbPortStatTxState": wfIsdbPortStatTxState,
       "wfIsdbPortStatTxFlowState": wfIsdbPortStatTxFlowState}
)
