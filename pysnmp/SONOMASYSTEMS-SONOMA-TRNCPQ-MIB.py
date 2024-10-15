# SNMP MIB module (SONOMASYSTEMS-SONOMA-TRNCPQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-TRNCPQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:48 2024
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

(sonomaLAN,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaLAN")


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaTokenRing_ObjectIdentity = ObjectIdentity
sonomaTokenRing = _SonomaTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2)
)
_TokenRingAdapterGroup_ObjectIdentity = ObjectIdentity
tokenRingAdapterGroup = _TokenRingAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1)
)
_TrnCpqGroup_ObjectIdentity = ObjectIdentity
trnCpqGroup = _TrnCpqGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1)
)
_TrnCpqAdapterTable_Object = MibTable
trnCpqAdapterTable = _TrnCpqAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trnCpqAdapterTable.setStatus("mandatory")
_TrnCpqAdapterEntry_Object = MibTableRow
trnCpqAdapterEntry = _TrnCpqAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1)
)
trnCpqAdapterEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqAdapterIndex"),
)
if mibBuilder.loadTexts:
    trnCpqAdapterEntry.setStatus("mandatory")
_TrnCpqAdapterIndex_Type = Integer32
_TrnCpqAdapterIndex_Object = MibTableColumn
trnCpqAdapterIndex = _TrnCpqAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 1),
    _TrnCpqAdapterIndex_Type()
)
trnCpqAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapterIndex.setStatus("mandatory")


class _TrnCpqAdapterCheckState_Type(Integer32):
    """Custom type trnCpqAdapterCheckState based on Integer32"""
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("adapterOutput", 17),
          ("adapterParity", 2),
          ("adapterProcessComplete", 18),
          ("arithmeticFault", 4),
          ("dioParity", 6),
          ("dmaBus", 8),
          ("dmaParity", 7),
          ("dmaTimeout", 9),
          ("illegalMAC", 5),
          ("illegalOpCode", 3),
          ("invalidINTR", 12),
          ("invalidXOP", 11),
          ("noErrors", 1),
          ("phtxHalt", 15),
          ("phtxRun", 16),
          ("ramFailure", 14),
          ("registerParity", 13),
          ("unknown", 10))
    )


_TrnCpqAdapterCheckState_Type.__name__ = "Integer32"
_TrnCpqAdapterCheckState_Object = MibTableColumn
trnCpqAdapterCheckState = _TrnCpqAdapterCheckState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 2),
    _TrnCpqAdapterCheckState_Type()
)
trnCpqAdapterCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapterCheckState.setStatus("mandatory")


class _TrnCpqAdapterOpenInWrapMode_Type(Integer32):
    """Custom type trnCpqAdapterOpenInWrapMode based on Integer32"""
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


_TrnCpqAdapterOpenInWrapMode_Type.__name__ = "Integer32"
_TrnCpqAdapterOpenInWrapMode_Object = MibTableColumn
trnCpqAdapterOpenInWrapMode = _TrnCpqAdapterOpenInWrapMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 3),
    _TrnCpqAdapterOpenInWrapMode_Type()
)
trnCpqAdapterOpenInWrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trnCpqAdapterOpenInWrapMode.setStatus("mandatory")


class _TrnCpqAdapterEarlyTokenRelease_Type(Integer32):
    """Custom type trnCpqAdapterEarlyTokenRelease based on Integer32"""
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


_TrnCpqAdapterEarlyTokenRelease_Type.__name__ = "Integer32"
_TrnCpqAdapterEarlyTokenRelease_Object = MibTableColumn
trnCpqAdapterEarlyTokenRelease = _TrnCpqAdapterEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 4),
    _TrnCpqAdapterEarlyTokenRelease_Type()
)
trnCpqAdapterEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trnCpqAdapterEarlyTokenRelease.setStatus("mandatory")
_TrnCpqAdapterGroupAddress_Type = PhysAddress
_TrnCpqAdapterGroupAddress_Object = MibTableColumn
trnCpqAdapterGroupAddress = _TrnCpqAdapterGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 5),
    _TrnCpqAdapterGroupAddress_Type()
)
trnCpqAdapterGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trnCpqAdapterGroupAddress.setStatus("mandatory")


class _TrnCpqRingSpeedDetect_Type(Integer32):
    """Custom type trnCpqRingSpeedDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_TrnCpqRingSpeedDetect_Type.__name__ = "Integer32"
_TrnCpqRingSpeedDetect_Object = MibTableColumn
trnCpqRingSpeedDetect = _TrnCpqRingSpeedDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 6),
    _TrnCpqRingSpeedDetect_Type()
)
trnCpqRingSpeedDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trnCpqRingSpeedDetect.setStatus("mandatory")


class _TrnCpqMtu_Type(Integer32):
    """Custom type trnCpqMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 17952),
    )


_TrnCpqMtu_Type.__name__ = "Integer32"
_TrnCpqMtu_Object = MibTableColumn
trnCpqMtu = _TrnCpqMtu_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 1, 1, 7),
    _TrnCpqMtu_Type()
)
trnCpqMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trnCpqMtu.setStatus("mandatory")
_TrnCpqAdapterCheckStatsTable_Object = MibTable
trnCpqAdapterCheckStatsTable = _TrnCpqAdapterCheckStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trnCpqAdapterCheckStatsTable.setStatus("mandatory")
_TrnCpqAdapterCheckStatsEntry_Object = MibTableRow
trnCpqAdapterCheckStatsEntry = _TrnCpqAdapterCheckStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1)
)
trnCpqAdapterCheckStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqAdapterCheckStatsIndex"),
)
if mibBuilder.loadTexts:
    trnCpqAdapterCheckStatsEntry.setStatus("mandatory")
_TrnCpqAdapterCheckStatsIndex_Type = Integer32
_TrnCpqAdapterCheckStatsIndex_Object = MibTableColumn
trnCpqAdapterCheckStatsIndex = _TrnCpqAdapterCheckStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 1),
    _TrnCpqAdapterCheckStatsIndex_Type()
)
trnCpqAdapterCheckStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapterCheckStatsIndex.setStatus("mandatory")
_TrnCpqAdapParityErrors_Type = Counter32
_TrnCpqAdapParityErrors_Object = MibTableColumn
trnCpqAdapParityErrors = _TrnCpqAdapParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 2),
    _TrnCpqAdapParityErrors_Type()
)
trnCpqAdapParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapParityErrors.setStatus("mandatory")
_TrnCpqIllOpCodeErrors_Type = Counter32
_TrnCpqIllOpCodeErrors_Object = MibTableColumn
trnCpqIllOpCodeErrors = _TrnCpqIllOpCodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 3),
    _TrnCpqIllOpCodeErrors_Type()
)
trnCpqIllOpCodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqIllOpCodeErrors.setStatus("mandatory")
_TrnCpqArithFaultErrors_Type = Counter32
_TrnCpqArithFaultErrors_Object = MibTableColumn
trnCpqArithFaultErrors = _TrnCpqArithFaultErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 4),
    _TrnCpqArithFaultErrors_Type()
)
trnCpqArithFaultErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqArithFaultErrors.setStatus("mandatory")
_TrnCpqIllMemErrors_Type = Counter32
_TrnCpqIllMemErrors_Object = MibTableColumn
trnCpqIllMemErrors = _TrnCpqIllMemErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 5),
    _TrnCpqIllMemErrors_Type()
)
trnCpqIllMemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqIllMemErrors.setStatus("mandatory")
_TrnCpqDIOParityErrors_Type = Counter32
_TrnCpqDIOParityErrors_Object = MibTableColumn
trnCpqDIOParityErrors = _TrnCpqDIOParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 6),
    _TrnCpqDIOParityErrors_Type()
)
trnCpqDIOParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqDIOParityErrors.setStatus("mandatory")
_TrnCpqDMAParityErrors_Type = Counter32
_TrnCpqDMAParityErrors_Object = MibTableColumn
trnCpqDMAParityErrors = _TrnCpqDMAParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 7),
    _TrnCpqDMAParityErrors_Type()
)
trnCpqDMAParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqDMAParityErrors.setStatus("mandatory")
_TrnCpqDMABusErrors_Type = Counter32
_TrnCpqDMABusErrors_Object = MibTableColumn
trnCpqDMABusErrors = _TrnCpqDMABusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 8),
    _TrnCpqDMABusErrors_Type()
)
trnCpqDMABusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqDMABusErrors.setStatus("mandatory")
_TrnCpqDMATimeoutErrors_Type = Counter32
_TrnCpqDMATimeoutErrors_Object = MibTableColumn
trnCpqDMATimeoutErrors = _TrnCpqDMATimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 9),
    _TrnCpqDMATimeoutErrors_Type()
)
trnCpqDMATimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqDMATimeoutErrors.setStatus("mandatory")
_TrnCpqInvIntrErrors_Type = Counter32
_TrnCpqInvIntrErrors_Object = MibTableColumn
trnCpqInvIntrErrors = _TrnCpqInvIntrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 10),
    _TrnCpqInvIntrErrors_Type()
)
trnCpqInvIntrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInvIntrErrors.setStatus("mandatory")
_TrnCpqInvXOPErrors_Type = Counter32
_TrnCpqInvXOPErrors_Object = MibTableColumn
trnCpqInvXOPErrors = _TrnCpqInvXOPErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 11),
    _TrnCpqInvXOPErrors_Type()
)
trnCpqInvXOPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInvXOPErrors.setStatus("mandatory")
_TrnCpqRegParityErrors_Type = Counter32
_TrnCpqRegParityErrors_Object = MibTableColumn
trnCpqRegParityErrors = _TrnCpqRegParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 12),
    _TrnCpqRegParityErrors_Type()
)
trnCpqRegParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqRegParityErrors.setStatus("mandatory")
_TrnCpqRAMFailErrors_Type = Counter32
_TrnCpqRAMFailErrors_Object = MibTableColumn
trnCpqRAMFailErrors = _TrnCpqRAMFailErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 13),
    _TrnCpqRAMFailErrors_Type()
)
trnCpqRAMFailErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqRAMFailErrors.setStatus("mandatory")
_TrnCpqPHTxHaltErrors_Type = Counter32
_TrnCpqPHTxHaltErrors_Object = MibTableColumn
trnCpqPHTxHaltErrors = _TrnCpqPHTxHaltErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 14),
    _TrnCpqPHTxHaltErrors_Type()
)
trnCpqPHTxHaltErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqPHTxHaltErrors.setStatus("mandatory")
_TrnCpqPHTxRunErrors_Type = Counter32
_TrnCpqPHTxRunErrors_Object = MibTableColumn
trnCpqPHTxRunErrors = _TrnCpqPHTxRunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 2, 1, 15),
    _TrnCpqPHTxRunErrors_Type()
)
trnCpqPHTxRunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqPHTxRunErrors.setStatus("mandatory")
_TrnCpqBUDStatsTable_Object = MibTable
trnCpqBUDStatsTable = _TrnCpqBUDStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trnCpqBUDStatsTable.setStatus("mandatory")
_TrnCpqBUDStatsEntry_Object = MibTableRow
trnCpqBUDStatsEntry = _TrnCpqBUDStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1)
)
trnCpqBUDStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqBUDStatsIndex"),
)
if mibBuilder.loadTexts:
    trnCpqBUDStatsEntry.setStatus("mandatory")
_TrnCpqBUDStatsIndex_Type = Integer32
_TrnCpqBUDStatsIndex_Object = MibTableColumn
trnCpqBUDStatsIndex = _TrnCpqBUDStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 1),
    _TrnCpqBUDStatsIndex_Type()
)
trnCpqBUDStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqBUDStatsIndex.setStatus("mandatory")
_TrnCpqInitialTestErrors_Type = Counter32
_TrnCpqInitialTestErrors_Object = MibTableColumn
trnCpqInitialTestErrors = _TrnCpqInitialTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 2),
    _TrnCpqInitialTestErrors_Type()
)
trnCpqInitialTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitialTestErrors.setStatus("mandatory")
_TrnCpqChecksumErrors_Type = Counter32
_TrnCpqChecksumErrors_Object = MibTableColumn
trnCpqChecksumErrors = _TrnCpqChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 3),
    _TrnCpqChecksumErrors_Type()
)
trnCpqChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqChecksumErrors.setStatus("mandatory")
_TrnCpqAdapterRAMErrors_Type = Counter32
_TrnCpqAdapterRAMErrors_Object = MibTableColumn
trnCpqAdapterRAMErrors = _TrnCpqAdapterRAMErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 4),
    _TrnCpqAdapterRAMErrors_Type()
)
trnCpqAdapterRAMErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapterRAMErrors.setStatus("mandatory")
_TrnCpqInstructionTestErrors_Type = Counter32
_TrnCpqInstructionTestErrors_Object = MibTableColumn
trnCpqInstructionTestErrors = _TrnCpqInstructionTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 5),
    _TrnCpqInstructionTestErrors_Type()
)
trnCpqInstructionTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInstructionTestErrors.setStatus("mandatory")
_TrnCpqCtxtorIntrTestErrors_Type = Counter32
_TrnCpqCtxtorIntrTestErrors_Object = MibTableColumn
trnCpqCtxtorIntrTestErrors = _TrnCpqCtxtorIntrTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 6),
    _TrnCpqCtxtorIntrTestErrors_Type()
)
trnCpqCtxtorIntrTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqCtxtorIntrTestErrors.setStatus("mandatory")
_TrnCpqProtocolHandlerHWErrors_Type = Counter32
_TrnCpqProtocolHandlerHWErrors_Object = MibTableColumn
trnCpqProtocolHandlerHWErrors = _TrnCpqProtocolHandlerHWErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 7),
    _TrnCpqProtocolHandlerHWErrors_Type()
)
trnCpqProtocolHandlerHWErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqProtocolHandlerHWErrors.setStatus("mandatory")
_TrnCpqSystemInterfaceRegErrors_Type = Counter32
_TrnCpqSystemInterfaceRegErrors_Object = MibTableColumn
trnCpqSystemInterfaceRegErrors = _TrnCpqSystemInterfaceRegErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 3, 1, 8),
    _TrnCpqSystemInterfaceRegErrors_Type()
)
trnCpqSystemInterfaceRegErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqSystemInterfaceRegErrors.setStatus("mandatory")
_TrnCpqInitStatsTable_Object = MibTable
trnCpqInitStatsTable = _TrnCpqInitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    trnCpqInitStatsTable.setStatus("mandatory")
_TrnCpqInitStatsEntry_Object = MibTableRow
trnCpqInitStatsEntry = _TrnCpqInitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1)
)
trnCpqInitStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqInitStatsIndex"),
)
if mibBuilder.loadTexts:
    trnCpqInitStatsEntry.setStatus("mandatory")
_TrnCpqInitStatsIndex_Type = Integer32
_TrnCpqInitStatsIndex_Object = MibTableColumn
trnCpqInitStatsIndex = _TrnCpqInitStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 1),
    _TrnCpqInitStatsIndex_Type()
)
trnCpqInitStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitStatsIndex.setStatus("mandatory")
_TrnCpqInvInitBlocksErrors_Type = Counter32
_TrnCpqInvInitBlocksErrors_Object = MibTableColumn
trnCpqInvInitBlocksErrors = _TrnCpqInvInitBlocksErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 2),
    _TrnCpqInvInitBlocksErrors_Type()
)
trnCpqInvInitBlocksErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInvInitBlocksErrors.setStatus("mandatory")
_TrnCpqInvInitOptionsErrors_Type = Counter32
_TrnCpqInvInitOptionsErrors_Object = MibTableColumn
trnCpqInvInitOptionsErrors = _TrnCpqInvInitOptionsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 3),
    _TrnCpqInvInitOptionsErrors_Type()
)
trnCpqInvInitOptionsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInvInitOptionsErrors.setStatus("mandatory")
_TrnCpqNoResourcesErrors_Type = Counter32
_TrnCpqNoResourcesErrors_Object = MibTableColumn
trnCpqNoResourcesErrors = _TrnCpqNoResourcesErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 4),
    _TrnCpqNoResourcesErrors_Type()
)
trnCpqNoResourcesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqNoResourcesErrors.setStatus("mandatory")
_TrnCpqInitAddressErrors_Type = Counter32
_TrnCpqInitAddressErrors_Object = MibTableColumn
trnCpqInitAddressErrors = _TrnCpqInitAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 5),
    _TrnCpqInitAddressErrors_Type()
)
trnCpqInitAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitAddressErrors.setStatus("mandatory")
_TrnCpqInitDIOParityErrors_Type = Counter32
_TrnCpqInitDIOParityErrors_Object = MibTableColumn
trnCpqInitDIOParityErrors = _TrnCpqInitDIOParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 6),
    _TrnCpqInitDIOParityErrors_Type()
)
trnCpqInitDIOParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitDIOParityErrors.setStatus("mandatory")
_TrnCpqInitDMAParityErrors_Type = Counter32
_TrnCpqInitDMAParityErrors_Object = MibTableColumn
trnCpqInitDMAParityErrors = _TrnCpqInitDMAParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 7),
    _TrnCpqInitDMAParityErrors_Type()
)
trnCpqInitDMAParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitDMAParityErrors.setStatus("mandatory")
_TrnCpqInitDMABusErrors_Type = Counter32
_TrnCpqInitDMABusErrors_Object = MibTableColumn
trnCpqInitDMABusErrors = _TrnCpqInitDMABusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 8),
    _TrnCpqInitDMABusErrors_Type()
)
trnCpqInitDMABusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitDMABusErrors.setStatus("mandatory")
_TrnCpqInitDMATimeoutErrors_Type = Counter32
_TrnCpqInitDMATimeoutErrors_Object = MibTableColumn
trnCpqInitDMATimeoutErrors = _TrnCpqInitDMATimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 9),
    _TrnCpqInitDMATimeoutErrors_Type()
)
trnCpqInitDMATimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitDMATimeoutErrors.setStatus("mandatory")
_TrnCpqInitDMADataErrors_Type = Counter32
_TrnCpqInitDMADataErrors_Object = MibTableColumn
trnCpqInitDMADataErrors = _TrnCpqInitDMADataErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 10),
    _TrnCpqInitDMADataErrors_Type()
)
trnCpqInitDMADataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqInitDMADataErrors.setStatus("mandatory")
_TrnCpqAdapterCheckErrors_Type = Counter32
_TrnCpqAdapterCheckErrors_Object = MibTableColumn
trnCpqAdapterCheckErrors = _TrnCpqAdapterCheckErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 4, 1, 11),
    _TrnCpqAdapterCheckErrors_Type()
)
trnCpqAdapterCheckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapterCheckErrors.setStatus("mandatory")
_TrnCpqMiscStatsTable_Object = MibTable
trnCpqMiscStatsTable = _TrnCpqMiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    trnCpqMiscStatsTable.setStatus("mandatory")
_TrnCpqMiscStatsEntry_Object = MibTableRow
trnCpqMiscStatsEntry = _TrnCpqMiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1)
)
trnCpqMiscStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB", "trnCpqMiscStatsIndex"),
)
if mibBuilder.loadTexts:
    trnCpqMiscStatsEntry.setStatus("mandatory")
_TrnCpqMiscStatsIndex_Type = Integer32
_TrnCpqMiscStatsIndex_Object = MibTableColumn
trnCpqMiscStatsIndex = _TrnCpqMiscStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 1),
    _TrnCpqMiscStatsIndex_Type()
)
trnCpqMiscStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqMiscStatsIndex.setStatus("mandatory")
_TrnCpqCounterOverflowErrors_Type = Counter32
_TrnCpqCounterOverflowErrors_Object = MibTableColumn
trnCpqCounterOverflowErrors = _TrnCpqCounterOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 2),
    _TrnCpqCounterOverflowErrors_Type()
)
trnCpqCounterOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqCounterOverflowErrors.setStatus("mandatory")
_TrnCpqAutoRemovalErrors_Type = Counter32
_TrnCpqAutoRemovalErrors_Object = MibTableColumn
trnCpqAutoRemovalErrors = _TrnCpqAutoRemovalErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 3),
    _TrnCpqAutoRemovalErrors_Type()
)
trnCpqAutoRemovalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAutoRemovalErrors.setStatus("mandatory")
_TrnCpqFrameBigErrors_Type = Counter32
_TrnCpqFrameBigErrors_Object = MibTableColumn
trnCpqFrameBigErrors = _TrnCpqFrameBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 4),
    _TrnCpqFrameBigErrors_Type()
)
trnCpqFrameBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqFrameBigErrors.setStatus("mandatory")
_TrnCpqNoHostBufErrors_Type = Counter32
_TrnCpqNoHostBufErrors_Object = MibTableColumn
trnCpqNoHostBufErrors = _TrnCpqNoHostBufErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 5),
    _TrnCpqNoHostBufErrors_Type()
)
trnCpqNoHostBufErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqNoHostBufErrors.setStatus("mandatory")
_TrnCpqAddressErrors_Type = Counter32
_TrnCpqAddressErrors_Object = MibTableColumn
trnCpqAddressErrors = _TrnCpqAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 6),
    _TrnCpqAddressErrors_Type()
)
trnCpqAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAddressErrors.setStatus("mandatory")
_TrnCpqAdapNotInsertedErrors_Type = Counter32
_TrnCpqAdapNotInsertedErrors_Object = MibTableColumn
trnCpqAdapNotInsertedErrors = _TrnCpqAdapNotInsertedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 7),
    _TrnCpqAdapNotInsertedErrors_Type()
)
trnCpqAdapNotInsertedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqAdapNotInsertedErrors.setStatus("mandatory")
_TrnCpqMiscRcvErrors_Type = Counter32
_TrnCpqMiscRcvErrors_Object = MibTableColumn
trnCpqMiscRcvErrors = _TrnCpqMiscRcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 8),
    _TrnCpqMiscRcvErrors_Type()
)
trnCpqMiscRcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqMiscRcvErrors.setStatus("mandatory")
_TrnCpqNoOfLinkResets_Type = Counter32
_TrnCpqNoOfLinkResets_Object = MibTableColumn
trnCpqNoOfLinkResets = _TrnCpqNoOfLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 9),
    _TrnCpqNoOfLinkResets_Type()
)
trnCpqNoOfLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqNoOfLinkResets.setStatus("mandatory")


class _TrnCpqLastLinkResetReason_Type(Integer32):
    """Custom type trnCpqLastLinkResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deviceError", 3),
          ("management", 2),
          ("noReason", 1))
    )


_TrnCpqLastLinkResetReason_Type.__name__ = "Integer32"
_TrnCpqLastLinkResetReason_Object = MibTableColumn
trnCpqLastLinkResetReason = _TrnCpqLastLinkResetReason_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 10),
    _TrnCpqLastLinkResetReason_Type()
)
trnCpqLastLinkResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqLastLinkResetReason.setStatus("mandatory")
_TrnCpqTimeSinceLastLinkReset_Type = TimeTicks
_TrnCpqTimeSinceLastLinkReset_Object = MibTableColumn
trnCpqTimeSinceLastLinkReset = _TrnCpqTimeSinceLastLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 5, 2, 1, 1, 5, 1, 11),
    _TrnCpqTimeSinceLastLinkReset_Type()
)
trnCpqTimeSinceLastLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trnCpqTimeSinceLastLinkReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-TRNCPQ-MIB",
    **{"PhysAddress": PhysAddress,
       "sonomaTokenRing": sonomaTokenRing,
       "tokenRingAdapterGroup": tokenRingAdapterGroup,
       "trnCpqGroup": trnCpqGroup,
       "trnCpqAdapterTable": trnCpqAdapterTable,
       "trnCpqAdapterEntry": trnCpqAdapterEntry,
       "trnCpqAdapterIndex": trnCpqAdapterIndex,
       "trnCpqAdapterCheckState": trnCpqAdapterCheckState,
       "trnCpqAdapterOpenInWrapMode": trnCpqAdapterOpenInWrapMode,
       "trnCpqAdapterEarlyTokenRelease": trnCpqAdapterEarlyTokenRelease,
       "trnCpqAdapterGroupAddress": trnCpqAdapterGroupAddress,
       "trnCpqRingSpeedDetect": trnCpqRingSpeedDetect,
       "trnCpqMtu": trnCpqMtu,
       "trnCpqAdapterCheckStatsTable": trnCpqAdapterCheckStatsTable,
       "trnCpqAdapterCheckStatsEntry": trnCpqAdapterCheckStatsEntry,
       "trnCpqAdapterCheckStatsIndex": trnCpqAdapterCheckStatsIndex,
       "trnCpqAdapParityErrors": trnCpqAdapParityErrors,
       "trnCpqIllOpCodeErrors": trnCpqIllOpCodeErrors,
       "trnCpqArithFaultErrors": trnCpqArithFaultErrors,
       "trnCpqIllMemErrors": trnCpqIllMemErrors,
       "trnCpqDIOParityErrors": trnCpqDIOParityErrors,
       "trnCpqDMAParityErrors": trnCpqDMAParityErrors,
       "trnCpqDMABusErrors": trnCpqDMABusErrors,
       "trnCpqDMATimeoutErrors": trnCpqDMATimeoutErrors,
       "trnCpqInvIntrErrors": trnCpqInvIntrErrors,
       "trnCpqInvXOPErrors": trnCpqInvXOPErrors,
       "trnCpqRegParityErrors": trnCpqRegParityErrors,
       "trnCpqRAMFailErrors": trnCpqRAMFailErrors,
       "trnCpqPHTxHaltErrors": trnCpqPHTxHaltErrors,
       "trnCpqPHTxRunErrors": trnCpqPHTxRunErrors,
       "trnCpqBUDStatsTable": trnCpqBUDStatsTable,
       "trnCpqBUDStatsEntry": trnCpqBUDStatsEntry,
       "trnCpqBUDStatsIndex": trnCpqBUDStatsIndex,
       "trnCpqInitialTestErrors": trnCpqInitialTestErrors,
       "trnCpqChecksumErrors": trnCpqChecksumErrors,
       "trnCpqAdapterRAMErrors": trnCpqAdapterRAMErrors,
       "trnCpqInstructionTestErrors": trnCpqInstructionTestErrors,
       "trnCpqCtxtorIntrTestErrors": trnCpqCtxtorIntrTestErrors,
       "trnCpqProtocolHandlerHWErrors": trnCpqProtocolHandlerHWErrors,
       "trnCpqSystemInterfaceRegErrors": trnCpqSystemInterfaceRegErrors,
       "trnCpqInitStatsTable": trnCpqInitStatsTable,
       "trnCpqInitStatsEntry": trnCpqInitStatsEntry,
       "trnCpqInitStatsIndex": trnCpqInitStatsIndex,
       "trnCpqInvInitBlocksErrors": trnCpqInvInitBlocksErrors,
       "trnCpqInvInitOptionsErrors": trnCpqInvInitOptionsErrors,
       "trnCpqNoResourcesErrors": trnCpqNoResourcesErrors,
       "trnCpqInitAddressErrors": trnCpqInitAddressErrors,
       "trnCpqInitDIOParityErrors": trnCpqInitDIOParityErrors,
       "trnCpqInitDMAParityErrors": trnCpqInitDMAParityErrors,
       "trnCpqInitDMABusErrors": trnCpqInitDMABusErrors,
       "trnCpqInitDMATimeoutErrors": trnCpqInitDMATimeoutErrors,
       "trnCpqInitDMADataErrors": trnCpqInitDMADataErrors,
       "trnCpqAdapterCheckErrors": trnCpqAdapterCheckErrors,
       "trnCpqMiscStatsTable": trnCpqMiscStatsTable,
       "trnCpqMiscStatsEntry": trnCpqMiscStatsEntry,
       "trnCpqMiscStatsIndex": trnCpqMiscStatsIndex,
       "trnCpqCounterOverflowErrors": trnCpqCounterOverflowErrors,
       "trnCpqAutoRemovalErrors": trnCpqAutoRemovalErrors,
       "trnCpqFrameBigErrors": trnCpqFrameBigErrors,
       "trnCpqNoHostBufErrors": trnCpqNoHostBufErrors,
       "trnCpqAddressErrors": trnCpqAddressErrors,
       "trnCpqAdapNotInsertedErrors": trnCpqAdapNotInsertedErrors,
       "trnCpqMiscRcvErrors": trnCpqMiscRcvErrors,
       "trnCpqNoOfLinkResets": trnCpqNoOfLinkResets,
       "trnCpqLastLinkResetReason": trnCpqLastLinkResetReason,
       "trnCpqTimeSinceLastLinkReset": trnCpqTimeSinceLastLinkReset}
)
