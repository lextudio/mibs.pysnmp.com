# SNMP MIB module (Fore-J2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-J2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:07 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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

foreJ2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_J2ConfGroup_ObjectIdentity = ObjectIdentity
j2ConfGroup = _J2ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1)
)
_J2ConfTable_Object = MibTable
j2ConfTable = _J2ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    j2ConfTable.setStatus("current")
_J2ConfEntry_Object = MibTableRow
j2ConfEntry = _J2ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1)
)
j2ConfEntry.setIndexNames(
    (0, "Fore-J2-MIB", "j2ConfBoard"),
    (0, "Fore-J2-MIB", "j2ConfModule"),
    (0, "Fore-J2-MIB", "j2ConfPort"),
)
if mibBuilder.loadTexts:
    j2ConfEntry.setStatus("current")
_J2ConfBoard_Type = Integer32
_J2ConfBoard_Object = MibTableColumn
j2ConfBoard = _J2ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 1),
    _J2ConfBoard_Type()
)
j2ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ConfBoard.setStatus("current")
_J2ConfModule_Type = Integer32
_J2ConfModule_Object = MibTableColumn
j2ConfModule = _J2ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 2),
    _J2ConfModule_Type()
)
j2ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ConfModule.setStatus("current")
_J2ConfPort_Type = Integer32
_J2ConfPort_Object = MibTableColumn
j2ConfPort = _J2ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 3),
    _J2ConfPort_Type()
)
j2ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ConfPort.setStatus("current")


class _J2LineLength_Type(Integer32):
    """Custom type j2LineLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("j2LongLine", 2),
          ("j2ShortLine", 1))
    )


_J2LineLength_Type.__name__ = "Integer32"
_J2LineLength_Object = MibTableColumn
j2LineLength = _J2LineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 4),
    _J2LineLength_Type()
)
j2LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    j2LineLength.setStatus("current")


class _J2LoopbackConfig_Type(Integer32):
    """Custom type j2LoopbackConfig based on Integer32"""
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
        *(("j2DiagLoop", 3),
          ("j2LineLoop", 2),
          ("j2NoLoop", 1),
          ("j2OtherLoop", 4))
    )


_J2LoopbackConfig_Type.__name__ = "Integer32"
_J2LoopbackConfig_Object = MibTableColumn
j2LoopbackConfig = _J2LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 5),
    _J2LoopbackConfig_Type()
)
j2LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    j2LoopbackConfig.setStatus("current")


class _J2TxClockSource_Type(Integer32):
    """Custom type j2TxClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("rxTiming", 1))
    )


_J2TxClockSource_Type.__name__ = "Integer32"
_J2TxClockSource_Object = MibTableColumn
j2TxClockSource = _J2TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 6),
    _J2TxClockSource_Type()
)
j2TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    j2TxClockSource.setStatus("current")


class _J2LineStatus_Type(Integer32):
    """Custom type j2LineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_J2LineStatus_Type.__name__ = "Integer32"
_J2LineStatus_Object = MibTableColumn
j2LineStatus = _J2LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 7),
    _J2LineStatus_Type()
)
j2LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2LineStatus.setStatus("current")


class _J2IdleUnassignedCells_Type(Integer32):
    """Custom type j2IdleUnassignedCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("unassigned", 1))
    )


_J2IdleUnassignedCells_Type.__name__ = "Integer32"
_J2IdleUnassignedCells_Object = MibTableColumn
j2IdleUnassignedCells = _J2IdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 8),
    _J2IdleUnassignedCells_Type()
)
j2IdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    j2IdleUnassignedCells.setStatus("current")
_J2StatsGroup_ObjectIdentity = ObjectIdentity
j2StatsGroup = _J2StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2)
)
_J2ErrorTable_Object = MibTable
j2ErrorTable = _J2ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    j2ErrorTable.setStatus("current")
_J2ErrorEntry_Object = MibTableRow
j2ErrorEntry = _J2ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1)
)
j2ErrorEntry.setIndexNames(
    (0, "Fore-J2-MIB", "j2ErrorBoard"),
    (0, "Fore-J2-MIB", "j2ErrorModule"),
    (0, "Fore-J2-MIB", "j2ErrorPort"),
)
if mibBuilder.loadTexts:
    j2ErrorEntry.setStatus("current")
_J2ErrorBoard_Type = Integer32
_J2ErrorBoard_Object = MibTableColumn
j2ErrorBoard = _J2ErrorBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 1),
    _J2ErrorBoard_Type()
)
j2ErrorBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ErrorBoard.setStatus("current")
_J2ErrorModule_Type = Integer32
_J2ErrorModule_Object = MibTableColumn
j2ErrorModule = _J2ErrorModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 2),
    _J2ErrorModule_Type()
)
j2ErrorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ErrorModule.setStatus("current")
_J2ErrorPort_Type = Integer32
_J2ErrorPort_Object = MibTableColumn
j2ErrorPort = _J2ErrorPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 3),
    _J2ErrorPort_Type()
)
j2ErrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2ErrorPort.setStatus("current")
_J2B8ZSCodingErrors_Type = Counter32
_J2B8ZSCodingErrors_Object = MibTableColumn
j2B8ZSCodingErrors = _J2B8ZSCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 4),
    _J2B8ZSCodingErrors_Type()
)
j2B8ZSCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2B8ZSCodingErrors.setStatus("current")
_J2CRC5Errors_Type = Counter32
_J2CRC5Errors_Object = MibTableColumn
j2CRC5Errors = _J2CRC5Errors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 5),
    _J2CRC5Errors_Type()
)
j2CRC5Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2CRC5Errors.setStatus("current")
_J2FramingErrors_Type = Counter32
_J2FramingErrors_Object = MibTableColumn
j2FramingErrors = _J2FramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 6),
    _J2FramingErrors_Type()
)
j2FramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2FramingErrors.setStatus("current")
_J2RxLossOfFrame_Type = Counter32
_J2RxLossOfFrame_Object = MibTableColumn
j2RxLossOfFrame = _J2RxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 7),
    _J2RxLossOfFrame_Type()
)
j2RxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2RxLossOfFrame.setStatus("current")
_J2RxLossOfClock_Type = Counter32
_J2RxLossOfClock_Object = MibTableColumn
j2RxLossOfClock = _J2RxLossOfClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 8),
    _J2RxLossOfClock_Type()
)
j2RxLossOfClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2RxLossOfClock.setStatus("current")
_J2RxAIS_Type = Counter32
_J2RxAIS_Object = MibTableColumn
j2RxAIS = _J2RxAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 9),
    _J2RxAIS_Type()
)
j2RxAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2RxAIS.setStatus("current")
_J2TxLossOfClock_Type = Counter32
_J2TxLossOfClock_Object = MibTableColumn
j2TxLossOfClock = _J2TxLossOfClock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 10),
    _J2TxLossOfClock_Type()
)
j2TxLossOfClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2TxLossOfClock.setStatus("current")
_J2RxRemoteAIS_Type = Counter32
_J2RxRemoteAIS_Object = MibTableColumn
j2RxRemoteAIS = _J2RxRemoteAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 11),
    _J2RxRemoteAIS_Type()
)
j2RxRemoteAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2RxRemoteAIS.setStatus("current")
_J2RxLossOfSignal_Type = Counter32
_J2RxLossOfSignal_Object = MibTableColumn
j2RxLossOfSignal = _J2RxLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 12),
    _J2RxLossOfSignal_Type()
)
j2RxLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2RxLossOfSignal.setStatus("current")
_J2AtmTable_Object = MibTable
j2AtmTable = _J2AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    j2AtmTable.setStatus("current")
_J2AtmEntry_Object = MibTableRow
j2AtmEntry = _J2AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1)
)
j2AtmEntry.setIndexNames(
    (0, "Fore-J2-MIB", "j2AtmBoard"),
    (0, "Fore-J2-MIB", "j2AtmModule"),
    (0, "Fore-J2-MIB", "j2AtmPort"),
)
if mibBuilder.loadTexts:
    j2AtmEntry.setStatus("current")
_J2AtmBoard_Type = Integer32
_J2AtmBoard_Object = MibTableColumn
j2AtmBoard = _J2AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 1),
    _J2AtmBoard_Type()
)
j2AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmBoard.setStatus("current")
_J2AtmModule_Type = Integer32
_J2AtmModule_Object = MibTableColumn
j2AtmModule = _J2AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 2),
    _J2AtmModule_Type()
)
j2AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmModule.setStatus("current")
_J2AtmPort_Type = Integer32
_J2AtmPort_Object = MibTableColumn
j2AtmPort = _J2AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 3),
    _J2AtmPort_Type()
)
j2AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmPort.setStatus("current")
_J2AtmHCSs_Type = Counter32
_J2AtmHCSs_Object = MibTableColumn
j2AtmHCSs = _J2AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 4),
    _J2AtmHCSs_Type()
)
j2AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmHCSs.setStatus("current")
_J2AtmRxCells_Type = Counter32
_J2AtmRxCells_Object = MibTableColumn
j2AtmRxCells = _J2AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 5),
    _J2AtmRxCells_Type()
)
j2AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmRxCells.setStatus("current")
_J2AtmTxCells_Type = Counter32
_J2AtmTxCells_Object = MibTableColumn
j2AtmTxCells = _J2AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 6),
    _J2AtmTxCells_Type()
)
j2AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmTxCells.setStatus("current")
_J2AtmLCDs_Type = Counter32
_J2AtmLCDs_Object = MibTableColumn
j2AtmLCDs = _J2AtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 7),
    _J2AtmLCDs_Type()
)
j2AtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    j2AtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-J2-MIB",
    **{"foreJ2": foreJ2,
       "j2ConfGroup": j2ConfGroup,
       "j2ConfTable": j2ConfTable,
       "j2ConfEntry": j2ConfEntry,
       "j2ConfBoard": j2ConfBoard,
       "j2ConfModule": j2ConfModule,
       "j2ConfPort": j2ConfPort,
       "j2LineLength": j2LineLength,
       "j2LoopbackConfig": j2LoopbackConfig,
       "j2TxClockSource": j2TxClockSource,
       "j2LineStatus": j2LineStatus,
       "j2IdleUnassignedCells": j2IdleUnassignedCells,
       "j2StatsGroup": j2StatsGroup,
       "j2ErrorTable": j2ErrorTable,
       "j2ErrorEntry": j2ErrorEntry,
       "j2ErrorBoard": j2ErrorBoard,
       "j2ErrorModule": j2ErrorModule,
       "j2ErrorPort": j2ErrorPort,
       "j2B8ZSCodingErrors": j2B8ZSCodingErrors,
       "j2CRC5Errors": j2CRC5Errors,
       "j2FramingErrors": j2FramingErrors,
       "j2RxLossOfFrame": j2RxLossOfFrame,
       "j2RxLossOfClock": j2RxLossOfClock,
       "j2RxAIS": j2RxAIS,
       "j2TxLossOfClock": j2TxLossOfClock,
       "j2RxRemoteAIS": j2RxRemoteAIS,
       "j2RxLossOfSignal": j2RxLossOfSignal,
       "j2AtmTable": j2AtmTable,
       "j2AtmEntry": j2AtmEntry,
       "j2AtmBoard": j2AtmBoard,
       "j2AtmModule": j2AtmModule,
       "j2AtmPort": j2AtmPort,
       "j2AtmHCSs": j2AtmHCSs,
       "j2AtmRxCells": j2AtmRxCells,
       "j2AtmTxCells": j2AtmTxCells,
       "j2AtmLCDs": j2AtmLCDs}
)
