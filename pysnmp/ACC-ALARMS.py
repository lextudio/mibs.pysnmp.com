# SNMP MIB module (ACC-ALARMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ALARMS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:43 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccAlarms_ObjectIdentity = ObjectIdentity
accAlarms = _AccAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53)
)
_AccAlarmTable_Object = MibTable
accAlarmTable = _AccAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1)
)
if mibBuilder.loadTexts:
    accAlarmTable.setStatus("mandatory")
_AccAlarmEntry_Object = MibTableRow
accAlarmEntry = _AccAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1)
)
accAlarmEntry.setIndexNames(
    (0, "ACC-ALARMS", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accAlarmEntry.setStatus("mandatory")
_AccAlarmSeqNum_Type = Integer32
_AccAlarmSeqNum_Object = MibTableColumn
accAlarmSeqNum = _AccAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 1),
    _AccAlarmSeqNum_Type()
)
accAlarmSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSeqNum.setStatus("mandatory")


class _AccAlarmAck_Type(Integer32):
    """Custom type accAlarmAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccAlarmAck_Type.__name__ = "Integer32"
_AccAlarmAck_Object = MibTableColumn
accAlarmAck = _AccAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 3),
    _AccAlarmAck_Type()
)
accAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAlarmAck.setStatus("mandatory")


class _AccAlarmPriority_Type(Integer32):
    """Custom type accAlarmPriority based on Integer32"""
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
        *(("cri", 4),
          ("dia", 1),
          ("maj", 3),
          ("min", 2))
    )


_AccAlarmPriority_Type.__name__ = "Integer32"
_AccAlarmPriority_Object = MibTableColumn
accAlarmPriority = _AccAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 4),
    _AccAlarmPriority_Type()
)
accAlarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmPriority.setStatus("mandatory")
_AccAlarmDescription_Type = DisplayString
_AccAlarmDescription_Object = MibTableColumn
accAlarmDescription = _AccAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 5),
    _AccAlarmDescription_Type()
)
accAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmDescription.setStatus("mandatory")
_AccAlarmSubCode_Type = OctetString
_AccAlarmSubCode_Object = MibTableColumn
accAlarmSubCode = _AccAlarmSubCode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 6),
    _AccAlarmSubCode_Type()
)
accAlarmSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSubCode.setStatus("mandatory")
_AccAlarmParameter_Type = OctetString
_AccAlarmParameter_Object = MibTableColumn
accAlarmParameter = _AccAlarmParameter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 7),
    _AccAlarmParameter_Type()
)
accAlarmParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmParameter.setStatus("mandatory")
_AccAlarmDateY2K_Type = OctetString
_AccAlarmDateY2K_Object = MibTableColumn
accAlarmDateY2K = _AccAlarmDateY2K_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 8),
    _AccAlarmDateY2K_Type()
)
accAlarmDateY2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmDateY2K.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccAlarmSumTable_Object = MibTable
accAlarmSumTable = _AccAlarmSumTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2)
)
if mibBuilder.loadTexts:
    accAlarmSumTable.setStatus("mandatory")
_AccAlarmSumEntry_Object = MibTableRow
accAlarmSumEntry = _AccAlarmSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1)
)
accAlarmSumEntry.setIndexNames(
    (0, "ACC-ALARMS", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    accAlarmSumEntry.setStatus("mandatory")
_AccAlarmSumCriOuts_Type = Counter32
_AccAlarmSumCriOuts_Object = MibTableColumn
accAlarmSumCriOuts = _AccAlarmSumCriOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 2),
    _AccAlarmSumCriOuts_Type()
)
accAlarmSumCriOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumCriOuts.setStatus("mandatory")
_AccAlarmSumCriTots_Type = Counter32
_AccAlarmSumCriTots_Object = MibTableColumn
accAlarmSumCriTots = _AccAlarmSumCriTots_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 3),
    _AccAlarmSumCriTots_Type()
)
accAlarmSumCriTots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumCriTots.setStatus("mandatory")
_AccAlarmSumMajOuts_Type = Counter32
_AccAlarmSumMajOuts_Object = MibTableColumn
accAlarmSumMajOuts = _AccAlarmSumMajOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 4),
    _AccAlarmSumMajOuts_Type()
)
accAlarmSumMajOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumMajOuts.setStatus("mandatory")
_AccAlarmSumMajTots_Type = Counter32
_AccAlarmSumMajTots_Object = MibTableColumn
accAlarmSumMajTots = _AccAlarmSumMajTots_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 5),
    _AccAlarmSumMajTots_Type()
)
accAlarmSumMajTots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumMajTots.setStatus("mandatory")
_AccAlarmSumMinOuts_Type = Counter32
_AccAlarmSumMinOuts_Object = MibTableColumn
accAlarmSumMinOuts = _AccAlarmSumMinOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 6),
    _AccAlarmSumMinOuts_Type()
)
accAlarmSumMinOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumMinOuts.setStatus("mandatory")
_AccAlarmSumMinTots_Type = Counter32
_AccAlarmSumMinTots_Object = MibTableColumn
accAlarmSumMinTots = _AccAlarmSumMinTots_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 7),
    _AccAlarmSumMinTots_Type()
)
accAlarmSumMinTots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumMinTots.setStatus("mandatory")
_AccAlarmSumDiaTots_Type = Counter32
_AccAlarmSumDiaTots_Object = MibTableColumn
accAlarmSumDiaTots = _AccAlarmSumDiaTots_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 8),
    _AccAlarmSumDiaTots_Type()
)
accAlarmSumDiaTots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumDiaTots.setStatus("mandatory")
_AccAlarmSumDateY2K_Type = OctetString
_AccAlarmSumDateY2K_Object = MibTableColumn
accAlarmSumDateY2K = _AccAlarmSumDateY2K_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 9),
    _AccAlarmSumDateY2K_Type()
)
accAlarmSumDateY2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmSumDateY2K.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 2, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_AccAlarmTableAckTimers_Type = Counter32
_AccAlarmTableAckTimers_Object = MibScalar
accAlarmTableAckTimers = _AccAlarmTableAckTimers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 3),
    _AccAlarmTableAckTimers_Type()
)
accAlarmTableAckTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmTableAckTimers.setStatus("mandatory")
_AccAlarmTableClrTimers_Type = Counter32
_AccAlarmTableClrTimers_Object = MibScalar
accAlarmTableClrTimers = _AccAlarmTableClrTimers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 4),
    _AccAlarmTableClrTimers_Type()
)
accAlarmTableClrTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmTableClrTimers.setStatus("mandatory")
_AccAlarmTableSavTimers_Type = Counter32
_AccAlarmTableSavTimers_Object = MibScalar
accAlarmTableSavTimers = _AccAlarmTableSavTimers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 53, 5),
    _AccAlarmTableSavTimers_Type()
)
accAlarmTableSavTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAlarmTableSavTimers.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ALARMS",
    **{"accAlarms": accAlarms,
       "accAlarmTable": accAlarmTable,
       "accAlarmEntry": accAlarmEntry,
       "accAlarmSeqNum": accAlarmSeqNum,
       "accAlarmAck": accAlarmAck,
       "accAlarmPriority": accAlarmPriority,
       "accAlarmDescription": accAlarmDescription,
       "accAlarmSubCode": accAlarmSubCode,
       "accAlarmParameter": accAlarmParameter,
       "accAlarmDateY2K": accAlarmDateY2K,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accAlarmSumTable": accAlarmSumTable,
       "accAlarmSumEntry": accAlarmSumEntry,
       "accAlarmSumCriOuts": accAlarmSumCriOuts,
       "accAlarmSumCriTots": accAlarmSumCriTots,
       "accAlarmSumMajOuts": accAlarmSumMajOuts,
       "accAlarmSumMajTots": accAlarmSumMajTots,
       "accAlarmSumMinOuts": accAlarmSumMinOuts,
       "accAlarmSumMinTots": accAlarmSumMinTots,
       "accAlarmSumDiaTots": accAlarmSumDiaTots,
       "accAlarmSumDateY2K": accAlarmSumDateY2K,
       "pysmiFakeCol2": pysmiFakeCol2,
       "accAlarmTableAckTimers": accAlarmTableAckTimers,
       "accAlarmTableClrTimers": accAlarmTableClrTimers,
       "accAlarmTableSavTimers": accAlarmTableSavTimers}
)
