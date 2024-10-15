# SNMP MIB module (HPNSAEVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAEVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:21 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaEventLog_ObjectIdentity = ObjectIdentity
hpnsaEventLog = _HpnsaEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19)
)
_HpnsaEventLogRev_ObjectIdentity = ObjectIdentity
hpnsaEventLogRev = _HpnsaEventLogRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 1)
)


class _HpnsaEventLogMibRevMajor_Type(Integer32):
    """Custom type hpnsaEventLogMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEventLogMibRevMajor_Type.__name__ = "Integer32"
_HpnsaEventLogMibRevMajor_Object = MibScalar
hpnsaEventLogMibRevMajor = _HpnsaEventLogMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 1, 1),
    _HpnsaEventLogMibRevMajor_Type()
)
hpnsaEventLogMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogMibRevMajor.setStatus("mandatory")


class _HpnsaEventLogMibRevMinor_Type(Integer32):
    """Custom type hpnsaEventLogMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEventLogMibRevMinor_Type.__name__ = "Integer32"
_HpnsaEventLogMibRevMinor_Object = MibScalar
hpnsaEventLogMibRevMinor = _HpnsaEventLogMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 1, 2),
    _HpnsaEventLogMibRevMinor_Type()
)
hpnsaEventLogMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogMibRevMinor.setStatus("mandatory")
_HpnsaEventLogAgentInfo_ObjectIdentity = ObjectIdentity
hpnsaEventLogAgentInfo = _HpnsaEventLogAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2)
)
_HpnsaEventLogAgentTable_Object = MibTable
hpnsaEventLogAgentTable = _HpnsaEventLogAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaEventLogAgentTable.setStatus("mandatory")
_HpnsaEventLogAgentEntry_Object = MibTableRow
hpnsaEventLogAgentEntry = _HpnsaEventLogAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1, 1)
)
hpnsaEventLogAgentEntry.setIndexNames(
    (0, "HPNSAEVENT-MIB", "hpnsaEventLogAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEventLogAgentEntry.setStatus("mandatory")


class _HpnsaEventLogAgentIndex_Type(Integer32):
    """Custom type hpnsaEventLogAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEventLogAgentIndex_Type.__name__ = "Integer32"
_HpnsaEventLogAgentIndex_Object = MibTableColumn
hpnsaEventLogAgentIndex = _HpnsaEventLogAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1, 1, 1),
    _HpnsaEventLogAgentIndex_Type()
)
hpnsaEventLogAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogAgentIndex.setStatus("mandatory")


class _HpnsaEventLogAgentName_Type(DisplayString):
    """Custom type hpnsaEventLogAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogAgentName_Type.__name__ = "DisplayString"
_HpnsaEventLogAgentName_Object = MibTableColumn
hpnsaEventLogAgentName = _HpnsaEventLogAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1, 1, 2),
    _HpnsaEventLogAgentName_Type()
)
hpnsaEventLogAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogAgentName.setStatus("mandatory")


class _HpnsaEventLogAgentVersion_Type(DisplayString):
    """Custom type hpnsaEventLogAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaEventLogAgentVersion_Type.__name__ = "DisplayString"
_HpnsaEventLogAgentVersion_Object = MibTableColumn
hpnsaEventLogAgentVersion = _HpnsaEventLogAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1, 1, 3),
    _HpnsaEventLogAgentVersion_Type()
)
hpnsaEventLogAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogAgentVersion.setStatus("mandatory")


class _HpnsaEventLogAgentDate_Type(OctetString):
    """Custom type hpnsaEventLogAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogAgentDate_Type.__name__ = "OctetString"
_HpnsaEventLogAgentDate_Object = MibTableColumn
hpnsaEventLogAgentDate = _HpnsaEventLogAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 2, 1, 1, 4),
    _HpnsaEventLogAgentDate_Type()
)
hpnsaEventLogAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogAgentDate.setStatus("mandatory")
_HpnsaEventAgentCfgInfo_ObjectIdentity = ObjectIdentity
hpnsaEventAgentCfgInfo = _HpnsaEventAgentCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 3)
)
_HpnsaEventCfgTable_Object = MibTable
hpnsaEventCfgTable = _HpnsaEventCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaEventCfgTable.setStatus("mandatory")
_HpnsaEventCfgTableEntry_Object = MibTableRow
hpnsaEventCfgTableEntry = _HpnsaEventCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 3, 1, 1)
)
hpnsaEventCfgTableEntry.setIndexNames(
    (0, "HPNSAEVENT-MIB", "hpnsaEventLogRecType"),
)
if mibBuilder.loadTexts:
    hpnsaEventCfgTableEntry.setStatus("mandatory")


class _HpnsaEventLogRecType_Type(Integer32):
    """Custom type hpnsaEventLogRecType based on Integer32"""
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
              16,
              17,
              20,
              21,
              22,
              23,
              33,
              34,
              35,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              247,
              248)
        )
    )
    namedValues = NamedValues(
        *(("controlBoardPowerCycle", 143),
          ("controlBoardReset", 142),
          ("cpuCardMissing", 144),
          ("cpuDeconfigured", 128),
          ("cpuPciFanRestored", 133),
          ("cpuPciMultipleFanError", 132),
          ("cpuPciSingleFanError", 131),
          ("cpuReconfigured", 138),
          ("errorBusTimeout", 4),
          ("errorCpuFailure", 11),
          ("errorECCMultipleBit", 34),
          ("errorECCSingleBit", 33),
          ("errorEccMultipleBit", 2),
          ("errorEccSingleBit", 1),
          ("errorFailsafeTimeout", 12),
          ("errorIOChannelCheck", 5),
          ("errorPCISystem", 21),
          ("errorPOSTMemoryResize", 35),
          ("errorParityMemory", 3),
          ("errorPciParity", 9),
          ("errorPciSystem", 10),
          ("errorPost", 8),
          ("errorPostMemoryResize", 7),
          ("errorSoftwareNMI", 6),
          ("errorSystemLimitExceeded", 16),
          ("frontPanelNMI", 130),
          ("infoAsynchronousSystemReset", 17),
          ("infoErrorLoggingDisabled", 14),
          ("infoHotSwapModule", 248),
          ("infoRedundantPowerSupply", 247),
          ("infoSingleBitErrorDisabled", 13),
          ("infoSystemReconfig", 20),
          ("logAreaReset", 22),
          ("memoryFanRestored", 137),
          ("memoryMultipleFanError", 136),
          ("memorySingleFanError", 135),
          ("p6ECCError", 129),
          ("powerSupplyEvent", 139),
          ("powerSupplyInserted", 141),
          ("powerSupplyRemoved", 140),
          ("systemRebooted", 23),
          ("voltageRegulatingMonitorFailure", 145),
          ("watchdogTimerReset", 134))
    )


_HpnsaEventLogRecType_Type.__name__ = "Integer32"
_HpnsaEventLogRecType_Object = MibTableColumn
hpnsaEventLogRecType = _HpnsaEventLogRecType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 3, 1, 1, 1),
    _HpnsaEventLogRecType_Type()
)
hpnsaEventLogRecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogRecType.setStatus("mandatory")


class _HpnsaEventLogRecTrapEnable_Type(Integer32):
    """Custom type hpnsaEventLogRecTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisabled", 1),
          ("trapEnabled", 2))
    )


_HpnsaEventLogRecTrapEnable_Type.__name__ = "Integer32"
_HpnsaEventLogRecTrapEnable_Object = MibTableColumn
hpnsaEventLogRecTrapEnable = _HpnsaEventLogRecTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 3, 1, 1, 2),
    _HpnsaEventLogRecTrapEnable_Type()
)
hpnsaEventLogRecTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEventLogRecTrapEnable.setStatus("mandatory")
_HpnsaEventLogPresenceId_ObjectIdentity = ObjectIdentity
hpnsaEventLogPresenceId = _HpnsaEventLogPresenceId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4)
)


class _HpnsaEccPresent_Type(Integer32):
    """Custom type hpnsaEccPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaEccPresent_Type.__name__ = "Integer32"
_HpnsaEccPresent_Object = MibScalar
hpnsaEccPresent = _HpnsaEccPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4, 1),
    _HpnsaEccPresent_Type()
)
hpnsaEccPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEccPresent.setStatus("mandatory")


class _HpnsaPostPresent_Type(Integer32):
    """Custom type hpnsaPostPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaPostPresent_Type.__name__ = "Integer32"
_HpnsaPostPresent_Object = MibScalar
hpnsaPostPresent = _HpnsaPostPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4, 2),
    _HpnsaPostPresent_Type()
)
hpnsaPostPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPostPresent.setStatus("mandatory")


class _HpnsaTempVoltagePresent_Type(Integer32):
    """Custom type hpnsaTempVoltagePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaTempVoltagePresent_Type.__name__ = "Integer32"
_HpnsaTempVoltagePresent_Object = MibScalar
hpnsaTempVoltagePresent = _HpnsaTempVoltagePresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4, 3),
    _HpnsaTempVoltagePresent_Type()
)
hpnsaTempVoltagePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTempVoltagePresent.setStatus("mandatory")


class _HpnsaASRPresent_Type(Integer32):
    """Custom type hpnsaASRPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaASRPresent_Type.__name__ = "Integer32"
_HpnsaASRPresent_Object = MibScalar
hpnsaASRPresent = _HpnsaASRPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4, 4),
    _HpnsaASRPresent_Type()
)
hpnsaASRPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRPresent.setStatus("mandatory")


class _HpnsaNMIPresent_Type(Integer32):
    """Custom type hpnsaNMIPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaNMIPresent_Type.__name__ = "Integer32"
_HpnsaNMIPresent_Object = MibScalar
hpnsaNMIPresent = _HpnsaNMIPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 4, 5),
    _HpnsaNMIPresent_Type()
)
hpnsaNMIPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaNMIPresent.setStatus("mandatory")
_HpnsaEventLogStatistics_ObjectIdentity = ObjectIdentity
hpnsaEventLogStatistics = _HpnsaEventLogStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5)
)


class _HpnsaEventLogPercentFull_Type(Integer32):
    """Custom type hpnsaEventLogPercentFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnsaEventLogPercentFull_Type.__name__ = "Integer32"
_HpnsaEventLogPercentFull_Object = MibScalar
hpnsaEventLogPercentFull = _HpnsaEventLogPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 1),
    _HpnsaEventLogPercentFull_Type()
)
hpnsaEventLogPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogPercentFull.setStatus("mandatory")


class _HpnsaEventLogLastErasedDate_Type(OctetString):
    """Custom type hpnsaEventLogLastErasedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogLastErasedDate_Type.__name__ = "OctetString"
_HpnsaEventLogLastErasedDate_Object = MibScalar
hpnsaEventLogLastErasedDate = _HpnsaEventLogLastErasedDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 2),
    _HpnsaEventLogLastErasedDate_Type()
)
hpnsaEventLogLastErasedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLastErasedDate.setStatus("mandatory")
_HpnsaEventLogErasures_Type = Counter32
_HpnsaEventLogErasures_Object = MibScalar
hpnsaEventLogErasures = _HpnsaEventLogErasures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 3),
    _HpnsaEventLogErasures_Type()
)
hpnsaEventLogErasures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogErasures.setStatus("mandatory")


class _HpnsaEventLogEraseLog_Type(Integer32):
    """Custom type hpnsaEventLogEraseLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1234
        )
    )
    namedValues = NamedValues(
        ("eraseLogNow", 1234)
    )


_HpnsaEventLogEraseLog_Type.__name__ = "Integer32"
_HpnsaEventLogEraseLog_Object = MibScalar
hpnsaEventLogEraseLog = _HpnsaEventLogEraseLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 4),
    _HpnsaEventLogEraseLog_Type()
)
hpnsaEventLogEraseLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEventLogEraseLog.setStatus("mandatory")
_HpnsaEventLogTable_Object = MibTable
hpnsaEventLogTable = _HpnsaEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5)
)
if mibBuilder.loadTexts:
    hpnsaEventLogTable.setStatus("mandatory")
_HpnsaEventLogTableEntry_Object = MibTableRow
hpnsaEventLogTableEntry = _HpnsaEventLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1)
)
hpnsaEventLogTableEntry.setIndexNames(
    (0, "HPNSAEVENT-MIB", "hpnsaEventLogTableIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEventLogTableEntry.setStatus("mandatory")
_HpnsaEventLogTableIndex_Type = Integer32
_HpnsaEventLogTableIndex_Object = MibTableColumn
hpnsaEventLogTableIndex = _HpnsaEventLogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 1),
    _HpnsaEventLogTableIndex_Type()
)
hpnsaEventLogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogTableIndex.setStatus("mandatory")


class _HpnsaEventLogEntryDate_Type(OctetString):
    """Custom type hpnsaEventLogEntryDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogEntryDate_Type.__name__ = "OctetString"
_HpnsaEventLogEntryDate_Object = MibTableColumn
hpnsaEventLogEntryDate = _HpnsaEventLogEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 2),
    _HpnsaEventLogEntryDate_Type()
)
hpnsaEventLogEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryDate.setStatus("mandatory")


class _HpnsaEventLogEntryDescr_Type(DisplayString):
    """Custom type hpnsaEventLogEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryDescr_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryDescr_Object = MibTableColumn
hpnsaEventLogEntryDescr = _HpnsaEventLogEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 3),
    _HpnsaEventLogEntryDescr_Type()
)
hpnsaEventLogEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryDescr.setStatus("mandatory")


class _HpnsaEventLogEntryTrapID_Type(DisplayString):
    """Custom type hpnsaEventLogEntryTrapID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryTrapID_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryTrapID_Object = MibTableColumn
hpnsaEventLogEntryTrapID = _HpnsaEventLogEntryTrapID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 4),
    _HpnsaEventLogEntryTrapID_Type()
)
hpnsaEventLogEntryTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryTrapID.setStatus("mandatory")


class _HpnsaEventLogEntryVB1_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB1_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB1_Object = MibTableColumn
hpnsaEventLogEntryVB1 = _HpnsaEventLogEntryVB1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 5),
    _HpnsaEventLogEntryVB1_Type()
)
hpnsaEventLogEntryVB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB1.setStatus("mandatory")


class _HpnsaEventLogEntryVB2_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB2_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB2_Object = MibTableColumn
hpnsaEventLogEntryVB2 = _HpnsaEventLogEntryVB2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 6),
    _HpnsaEventLogEntryVB2_Type()
)
hpnsaEventLogEntryVB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB2.setStatus("mandatory")


class _HpnsaEventLogEntryVB3_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB3_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB3_Object = MibTableColumn
hpnsaEventLogEntryVB3 = _HpnsaEventLogEntryVB3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 7),
    _HpnsaEventLogEntryVB3_Type()
)
hpnsaEventLogEntryVB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB3.setStatus("mandatory")


class _HpnsaEventLogEntryVB4_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB4_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB4_Object = MibTableColumn
hpnsaEventLogEntryVB4 = _HpnsaEventLogEntryVB4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 8),
    _HpnsaEventLogEntryVB4_Type()
)
hpnsaEventLogEntryVB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB4.setStatus("mandatory")


class _HpnsaEventLogEntryVB5_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB5_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB5_Object = MibTableColumn
hpnsaEventLogEntryVB5 = _HpnsaEventLogEntryVB5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 9),
    _HpnsaEventLogEntryVB5_Type()
)
hpnsaEventLogEntryVB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB5.setStatus("mandatory")


class _HpnsaEventLogEntryVB6_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB6_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB6_Object = MibTableColumn
hpnsaEventLogEntryVB6 = _HpnsaEventLogEntryVB6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 10),
    _HpnsaEventLogEntryVB6_Type()
)
hpnsaEventLogEntryVB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB6.setStatus("mandatory")


class _HpnsaEventLogEntryVB7_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB7_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB7_Object = MibTableColumn
hpnsaEventLogEntryVB7 = _HpnsaEventLogEntryVB7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 11),
    _HpnsaEventLogEntryVB7_Type()
)
hpnsaEventLogEntryVB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB7.setStatus("mandatory")


class _HpnsaEventLogEntryVB8_Type(DisplayString):
    """Custom type hpnsaEventLogEntryVB8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryVB8_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryVB8_Object = MibTableColumn
hpnsaEventLogEntryVB8 = _HpnsaEventLogEntryVB8_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 12),
    _HpnsaEventLogEntryVB8_Type()
)
hpnsaEventLogEntryVB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryVB8.setStatus("mandatory")


class _HpnsaEventLogEntryAdvisory_Type(DisplayString):
    """Custom type hpnsaEventLogEntryAdvisory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_HpnsaEventLogEntryAdvisory_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryAdvisory_Object = MibTableColumn
hpnsaEventLogEntryAdvisory = _HpnsaEventLogEntryAdvisory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 13),
    _HpnsaEventLogEntryAdvisory_Type()
)
hpnsaEventLogEntryAdvisory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryAdvisory.setStatus("mandatory")


class _HpnsaEventLogEntryReportEntity_Type(DisplayString):
    """Custom type hpnsaEventLogEntryReportEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntryReportEntity_Type.__name__ = "DisplayString"
_HpnsaEventLogEntryReportEntity_Object = MibTableColumn
hpnsaEventLogEntryReportEntity = _HpnsaEventLogEntryReportEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 14),
    _HpnsaEventLogEntryReportEntity_Type()
)
hpnsaEventLogEntryReportEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryReportEntity.setStatus("mandatory")


class _HpnsaEventLogEntrySeverity_Type(DisplayString):
    """Custom type hpnsaEventLogEntrySeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogEntrySeverity_Type.__name__ = "DisplayString"
_HpnsaEventLogEntrySeverity_Object = MibTableColumn
hpnsaEventLogEntrySeverity = _HpnsaEventLogEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 15),
    _HpnsaEventLogEntrySeverity_Type()
)
hpnsaEventLogEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntrySeverity.setStatus("mandatory")


class _HpnsaEventLogEntryStatus_Type(Integer32):
    """Custom type hpnsaEventLogEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("caution", 9),
          ("critical", 15),
          ("infoWithAlert", 3),
          ("informational", 2),
          ("repaired", 6))
    )


_HpnsaEventLogEntryStatus_Type.__name__ = "Integer32"
_HpnsaEventLogEntryStatus_Object = MibTableColumn
hpnsaEventLogEntryStatus = _HpnsaEventLogEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 16),
    _HpnsaEventLogEntryStatus_Type()
)
hpnsaEventLogEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryStatus.setStatus("mandatory")
_HpnsaEventLogEntryInfo_Type = Integer32
_HpnsaEventLogEntryInfo_Object = MibTableColumn
hpnsaEventLogEntryInfo = _HpnsaEventLogEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 17),
    _HpnsaEventLogEntryInfo_Type()
)
hpnsaEventLogEntryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryInfo.setStatus("mandatory")


class _HpnsaEventLogEntryUpdateTime_Type(OctetString):
    """Custom type hpnsaEventLogEntryUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogEntryUpdateTime_Type.__name__ = "OctetString"
_HpnsaEventLogEntryUpdateTime_Object = MibTableColumn
hpnsaEventLogEntryUpdateTime = _HpnsaEventLogEntryUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 5, 1, 18),
    _HpnsaEventLogEntryUpdateTime_Type()
)
hpnsaEventLogEntryUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogEntryUpdateTime.setStatus("mandatory")
_HpnsaEventLogNumberOfEvents_Type = Integer32
_HpnsaEventLogNumberOfEvents_Object = MibScalar
hpnsaEventLogNumberOfEvents = _HpnsaEventLogNumberOfEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 6),
    _HpnsaEventLogNumberOfEvents_Type()
)
hpnsaEventLogNumberOfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogNumberOfEvents.setStatus("mandatory")


class _HpnsaEventLogAggregationStatus_Type(Integer32):
    """Custom type hpnsaEventLogAggregationStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_HpnsaEventLogAggregationStatus_Type.__name__ = "Integer32"
_HpnsaEventLogAggregationStatus_Object = MibScalar
hpnsaEventLogAggregationStatus = _HpnsaEventLogAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 7),
    _HpnsaEventLogAggregationStatus_Type()
)
hpnsaEventLogAggregationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogAggregationStatus.setStatus("mandatory")
_HpnsaEventLogLocalTable_Object = MibTable
hpnsaEventLogLocalTable = _HpnsaEventLogLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8)
)
if mibBuilder.loadTexts:
    hpnsaEventLogLocalTable.setStatus("mandatory")
_HpnsaEventLogLocalTableEntry_Object = MibTableRow
hpnsaEventLogLocalTableEntry = _HpnsaEventLogLocalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1)
)
hpnsaEventLogLocalTableEntry.setIndexNames(
    (0, "HPNSAEVENT-MIB", "hpnsaEventLogTableIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEventLogLocalTableEntry.setStatus("mandatory")
_HpnsaEventLogLocalTableIndex_Type = Integer32
_HpnsaEventLogLocalTableIndex_Object = MibTableColumn
hpnsaEventLogLocalTableIndex = _HpnsaEventLogLocalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 1),
    _HpnsaEventLogLocalTableIndex_Type()
)
hpnsaEventLogLocalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalTableIndex.setStatus("mandatory")


class _HpnsaEventLogLocalEntryDate_Type(OctetString):
    """Custom type hpnsaEventLogLocalEntryDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogLocalEntryDate_Type.__name__ = "OctetString"
_HpnsaEventLogLocalEntryDate_Object = MibTableColumn
hpnsaEventLogLocalEntryDate = _HpnsaEventLogLocalEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 2),
    _HpnsaEventLogLocalEntryDate_Type()
)
hpnsaEventLogLocalEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryDate.setStatus("mandatory")


class _HpnsaEventLogLocalEntryDescr_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryDescr_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryDescr_Object = MibTableColumn
hpnsaEventLogLocalEntryDescr = _HpnsaEventLogLocalEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 3),
    _HpnsaEventLogLocalEntryDescr_Type()
)
hpnsaEventLogLocalEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryDescr.setStatus("mandatory")


class _HpnsaEventLogLocalEntryTrapID_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryTrapID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryTrapID_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryTrapID_Object = MibTableColumn
hpnsaEventLogLocalEntryTrapID = _HpnsaEventLogLocalEntryTrapID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 4),
    _HpnsaEventLogLocalEntryTrapID_Type()
)
hpnsaEventLogLocalEntryTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryTrapID.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB1_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB1_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB1_Object = MibTableColumn
hpnsaEventLogLocalEntryVB1 = _HpnsaEventLogLocalEntryVB1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 5),
    _HpnsaEventLogLocalEntryVB1_Type()
)
hpnsaEventLogLocalEntryVB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB1.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB2_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB2_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB2_Object = MibTableColumn
hpnsaEventLogLocalEntryVB2 = _HpnsaEventLogLocalEntryVB2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 6),
    _HpnsaEventLogLocalEntryVB2_Type()
)
hpnsaEventLogLocalEntryVB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB2.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB3_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB3_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB3_Object = MibTableColumn
hpnsaEventLogLocalEntryVB3 = _HpnsaEventLogLocalEntryVB3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 7),
    _HpnsaEventLogLocalEntryVB3_Type()
)
hpnsaEventLogLocalEntryVB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB3.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB4_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB4_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB4_Object = MibTableColumn
hpnsaEventLogLocalEntryVB4 = _HpnsaEventLogLocalEntryVB4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 8),
    _HpnsaEventLogLocalEntryVB4_Type()
)
hpnsaEventLogLocalEntryVB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB4.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB5_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB5_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB5_Object = MibTableColumn
hpnsaEventLogLocalEntryVB5 = _HpnsaEventLogLocalEntryVB5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 9),
    _HpnsaEventLogLocalEntryVB5_Type()
)
hpnsaEventLogLocalEntryVB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB5.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB6_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB6_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB6_Object = MibTableColumn
hpnsaEventLogLocalEntryVB6 = _HpnsaEventLogLocalEntryVB6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 10),
    _HpnsaEventLogLocalEntryVB6_Type()
)
hpnsaEventLogLocalEntryVB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB6.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB7_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB7_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB7_Object = MibTableColumn
hpnsaEventLogLocalEntryVB7 = _HpnsaEventLogLocalEntryVB7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 11),
    _HpnsaEventLogLocalEntryVB7_Type()
)
hpnsaEventLogLocalEntryVB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB7.setStatus("mandatory")


class _HpnsaEventLogLocalEntryVB8_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryVB8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryVB8_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryVB8_Object = MibTableColumn
hpnsaEventLogLocalEntryVB8 = _HpnsaEventLogLocalEntryVB8_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 12),
    _HpnsaEventLogLocalEntryVB8_Type()
)
hpnsaEventLogLocalEntryVB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryVB8.setStatus("mandatory")


class _HpnsaEventLogLocalEntryAdvisory_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryAdvisory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_HpnsaEventLogLocalEntryAdvisory_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryAdvisory_Object = MibTableColumn
hpnsaEventLogLocalEntryAdvisory = _HpnsaEventLogLocalEntryAdvisory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 13),
    _HpnsaEventLogLocalEntryAdvisory_Type()
)
hpnsaEventLogLocalEntryAdvisory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryAdvisory.setStatus("mandatory")


class _HpnsaEventLogLocalEntryReportEntity_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntryReportEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntryReportEntity_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntryReportEntity_Object = MibTableColumn
hpnsaEventLogLocalEntryReportEntity = _HpnsaEventLogLocalEntryReportEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 14),
    _HpnsaEventLogLocalEntryReportEntity_Type()
)
hpnsaEventLogLocalEntryReportEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryReportEntity.setStatus("mandatory")


class _HpnsaEventLogLocalEntrySeverity_Type(DisplayString):
    """Custom type hpnsaEventLogLocalEntrySeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaEventLogLocalEntrySeverity_Type.__name__ = "DisplayString"
_HpnsaEventLogLocalEntrySeverity_Object = MibTableColumn
hpnsaEventLogLocalEntrySeverity = _HpnsaEventLogLocalEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 15),
    _HpnsaEventLogLocalEntrySeverity_Type()
)
hpnsaEventLogLocalEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntrySeverity.setStatus("mandatory")


class _HpnsaEventLogLocalEntryStatus_Type(Integer32):
    """Custom type hpnsaEventLogLocalEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("caution", 9),
          ("critical", 15),
          ("infoWithAlert", 3),
          ("informational", 2),
          ("repaired", 6))
    )


_HpnsaEventLogLocalEntryStatus_Type.__name__ = "Integer32"
_HpnsaEventLogLocalEntryStatus_Object = MibTableColumn
hpnsaEventLogLocalEntryStatus = _HpnsaEventLogLocalEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 16),
    _HpnsaEventLogLocalEntryStatus_Type()
)
hpnsaEventLogLocalEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryStatus.setStatus("mandatory")
_HpnsaEventLogLocalEntryInfo_Type = Integer32
_HpnsaEventLogLocalEntryInfo_Object = MibTableColumn
hpnsaEventLogLocalEntryInfo = _HpnsaEventLogLocalEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 17),
    _HpnsaEventLogLocalEntryInfo_Type()
)
hpnsaEventLogLocalEntryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryInfo.setStatus("mandatory")


class _HpnsaEventLogLocalEntryUpdateTime_Type(OctetString):
    """Custom type hpnsaEventLogLocalEntryUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaEventLogLocalEntryUpdateTime_Type.__name__ = "OctetString"
_HpnsaEventLogLocalEntryUpdateTime_Object = MibTableColumn
hpnsaEventLogLocalEntryUpdateTime = _HpnsaEventLogLocalEntryUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 8, 1, 18),
    _HpnsaEventLogLocalEntryUpdateTime_Type()
)
hpnsaEventLogLocalEntryUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogLocalEntryUpdateTime.setStatus("mandatory")
_HpnsaEventLogNumOfLocalEvents_Type = Integer32
_HpnsaEventLogNumOfLocalEvents_Object = MibScalar
hpnsaEventLogNumOfLocalEvents = _HpnsaEventLogNumOfLocalEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 5, 9),
    _HpnsaEventLogNumOfLocalEvents_Type()
)
hpnsaEventLogNumOfLocalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEventLogNumOfLocalEvents.setStatus("mandatory")
_HpnsaEventCustomerAcknowledgeActions_ObjectIdentity = ObjectIdentity
hpnsaEventCustomerAcknowledgeActions = _HpnsaEventCustomerAcknowledgeActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 6)
)


class _HpnsaEventClearLEDs_Type(Integer32):
    """Custom type hpnsaEventClearLEDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearAttentionLED", 1)
    )


_HpnsaEventClearLEDs_Type.__name__ = "Integer32"
_HpnsaEventClearLEDs_Object = MibScalar
hpnsaEventClearLEDs = _HpnsaEventClearLEDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 19, 6, 1),
    _HpnsaEventClearLEDs_Type()
)
hpnsaEventClearLEDs.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hpnsaEventClearLEDs.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAEVENT-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaEventLog": hpnsaEventLog,
       "hpnsaEventLogRev": hpnsaEventLogRev,
       "hpnsaEventLogMibRevMajor": hpnsaEventLogMibRevMajor,
       "hpnsaEventLogMibRevMinor": hpnsaEventLogMibRevMinor,
       "hpnsaEventLogAgentInfo": hpnsaEventLogAgentInfo,
       "hpnsaEventLogAgentTable": hpnsaEventLogAgentTable,
       "hpnsaEventLogAgentEntry": hpnsaEventLogAgentEntry,
       "hpnsaEventLogAgentIndex": hpnsaEventLogAgentIndex,
       "hpnsaEventLogAgentName": hpnsaEventLogAgentName,
       "hpnsaEventLogAgentVersion": hpnsaEventLogAgentVersion,
       "hpnsaEventLogAgentDate": hpnsaEventLogAgentDate,
       "hpnsaEventAgentCfgInfo": hpnsaEventAgentCfgInfo,
       "hpnsaEventCfgTable": hpnsaEventCfgTable,
       "hpnsaEventCfgTableEntry": hpnsaEventCfgTableEntry,
       "hpnsaEventLogRecType": hpnsaEventLogRecType,
       "hpnsaEventLogRecTrapEnable": hpnsaEventLogRecTrapEnable,
       "hpnsaEventLogPresenceId": hpnsaEventLogPresenceId,
       "hpnsaEccPresent": hpnsaEccPresent,
       "hpnsaPostPresent": hpnsaPostPresent,
       "hpnsaTempVoltagePresent": hpnsaTempVoltagePresent,
       "hpnsaASRPresent": hpnsaASRPresent,
       "hpnsaNMIPresent": hpnsaNMIPresent,
       "hpnsaEventLogStatistics": hpnsaEventLogStatistics,
       "hpnsaEventLogPercentFull": hpnsaEventLogPercentFull,
       "hpnsaEventLogLastErasedDate": hpnsaEventLogLastErasedDate,
       "hpnsaEventLogErasures": hpnsaEventLogErasures,
       "hpnsaEventLogEraseLog": hpnsaEventLogEraseLog,
       "hpnsaEventLogTable": hpnsaEventLogTable,
       "hpnsaEventLogTableEntry": hpnsaEventLogTableEntry,
       "hpnsaEventLogTableIndex": hpnsaEventLogTableIndex,
       "hpnsaEventLogEntryDate": hpnsaEventLogEntryDate,
       "hpnsaEventLogEntryDescr": hpnsaEventLogEntryDescr,
       "hpnsaEventLogEntryTrapID": hpnsaEventLogEntryTrapID,
       "hpnsaEventLogEntryVB1": hpnsaEventLogEntryVB1,
       "hpnsaEventLogEntryVB2": hpnsaEventLogEntryVB2,
       "hpnsaEventLogEntryVB3": hpnsaEventLogEntryVB3,
       "hpnsaEventLogEntryVB4": hpnsaEventLogEntryVB4,
       "hpnsaEventLogEntryVB5": hpnsaEventLogEntryVB5,
       "hpnsaEventLogEntryVB6": hpnsaEventLogEntryVB6,
       "hpnsaEventLogEntryVB7": hpnsaEventLogEntryVB7,
       "hpnsaEventLogEntryVB8": hpnsaEventLogEntryVB8,
       "hpnsaEventLogEntryAdvisory": hpnsaEventLogEntryAdvisory,
       "hpnsaEventLogEntryReportEntity": hpnsaEventLogEntryReportEntity,
       "hpnsaEventLogEntrySeverity": hpnsaEventLogEntrySeverity,
       "hpnsaEventLogEntryStatus": hpnsaEventLogEntryStatus,
       "hpnsaEventLogEntryInfo": hpnsaEventLogEntryInfo,
       "hpnsaEventLogEntryUpdateTime": hpnsaEventLogEntryUpdateTime,
       "hpnsaEventLogNumberOfEvents": hpnsaEventLogNumberOfEvents,
       "hpnsaEventLogAggregationStatus": hpnsaEventLogAggregationStatus,
       "hpnsaEventLogLocalTable": hpnsaEventLogLocalTable,
       "hpnsaEventLogLocalTableEntry": hpnsaEventLogLocalTableEntry,
       "hpnsaEventLogLocalTableIndex": hpnsaEventLogLocalTableIndex,
       "hpnsaEventLogLocalEntryDate": hpnsaEventLogLocalEntryDate,
       "hpnsaEventLogLocalEntryDescr": hpnsaEventLogLocalEntryDescr,
       "hpnsaEventLogLocalEntryTrapID": hpnsaEventLogLocalEntryTrapID,
       "hpnsaEventLogLocalEntryVB1": hpnsaEventLogLocalEntryVB1,
       "hpnsaEventLogLocalEntryVB2": hpnsaEventLogLocalEntryVB2,
       "hpnsaEventLogLocalEntryVB3": hpnsaEventLogLocalEntryVB3,
       "hpnsaEventLogLocalEntryVB4": hpnsaEventLogLocalEntryVB4,
       "hpnsaEventLogLocalEntryVB5": hpnsaEventLogLocalEntryVB5,
       "hpnsaEventLogLocalEntryVB6": hpnsaEventLogLocalEntryVB6,
       "hpnsaEventLogLocalEntryVB7": hpnsaEventLogLocalEntryVB7,
       "hpnsaEventLogLocalEntryVB8": hpnsaEventLogLocalEntryVB8,
       "hpnsaEventLogLocalEntryAdvisory": hpnsaEventLogLocalEntryAdvisory,
       "hpnsaEventLogLocalEntryReportEntity": hpnsaEventLogLocalEntryReportEntity,
       "hpnsaEventLogLocalEntrySeverity": hpnsaEventLogLocalEntrySeverity,
       "hpnsaEventLogLocalEntryStatus": hpnsaEventLogLocalEntryStatus,
       "hpnsaEventLogLocalEntryInfo": hpnsaEventLogLocalEntryInfo,
       "hpnsaEventLogLocalEntryUpdateTime": hpnsaEventLogLocalEntryUpdateTime,
       "hpnsaEventLogNumOfLocalEvents": hpnsaEventLogNumOfLocalEvents,
       "hpnsaEventCustomerAcknowledgeActions": hpnsaEventCustomerAcknowledgeActions,
       "hpnsaEventClearLEDs": hpnsaEventClearLEDs}
)
