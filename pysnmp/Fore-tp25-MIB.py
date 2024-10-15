# SNMP MIB module (Fore-tp25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-tp25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:24 2024
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

foreTP25Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tp25ConfGroup_ObjectIdentity = ObjectIdentity
tp25ConfGroup = _Tp25ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1)
)
_Tp25ConfTable_Object = MibTable
tp25ConfTable = _Tp25ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tp25ConfTable.setStatus("current")
_Tp25ConfEntry_Object = MibTableRow
tp25ConfEntry = _Tp25ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1)
)
tp25ConfEntry.setIndexNames(
    (0, "Fore-tp25-MIB", "tp25ConfBoard"),
    (0, "Fore-tp25-MIB", "tp25ConfModule"),
    (0, "Fore-tp25-MIB", "tp25ConfPort"),
)
if mibBuilder.loadTexts:
    tp25ConfEntry.setStatus("current")
_Tp25ConfBoard_Type = Integer32
_Tp25ConfBoard_Object = MibTableColumn
tp25ConfBoard = _Tp25ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 1),
    _Tp25ConfBoard_Type()
)
tp25ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ConfBoard.setStatus("current")
_Tp25ConfModule_Type = Integer32
_Tp25ConfModule_Object = MibTableColumn
tp25ConfModule = _Tp25ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 2),
    _Tp25ConfModule_Type()
)
tp25ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ConfModule.setStatus("current")
_Tp25ConfPort_Type = Integer32
_Tp25ConfPort_Object = MibTableColumn
tp25ConfPort = _Tp25ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 3),
    _Tp25ConfPort_Type()
)
tp25ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ConfPort.setStatus("current")


class _Tp25MediaType_Type(Integer32):
    """Custom type tp25MediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tp25FTP", 3),
          ("tp25STP", 2),
          ("tp25UTP", 1))
    )


_Tp25MediaType_Type.__name__ = "Integer32"
_Tp25MediaType_Object = MibTableColumn
tp25MediaType = _Tp25MediaType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 4),
    _Tp25MediaType_Type()
)
tp25MediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25MediaType.setStatus("current")


class _Tp25LoopbackConfig_Type(Integer32):
    """Custom type tp25LoopbackConfig based on Integer32"""
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
        *(("tp25DiagLoop", 2),
          ("tp25LineLoop", 3),
          ("tp25NoLoop", 1))
    )


_Tp25LoopbackConfig_Type.__name__ = "Integer32"
_Tp25LoopbackConfig_Object = MibTableColumn
tp25LoopbackConfig = _Tp25LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 5),
    _Tp25LoopbackConfig_Type()
)
tp25LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp25LoopbackConfig.setStatus("current")


class _Tp25RxTiming_Type(Integer32):
    """Custom type tp25RxTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tp25NoTimingPresent", 1),
          ("tp25TimingPresent", 2))
    )


_Tp25RxTiming_Type.__name__ = "Integer32"
_Tp25RxTiming_Object = MibTableColumn
tp25RxTiming = _Tp25RxTiming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 6),
    _Tp25RxTiming_Type()
)
tp25RxTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25RxTiming.setStatus("current")
_Tp25StatsGroup_ObjectIdentity = ObjectIdentity
tp25StatsGroup = _Tp25StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2)
)
_Tp25ErrorTable_Object = MibTable
tp25ErrorTable = _Tp25ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    tp25ErrorTable.setStatus("current")
_Tp25ErrorEntry_Object = MibTableRow
tp25ErrorEntry = _Tp25ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1)
)
tp25ErrorEntry.setIndexNames(
    (0, "Fore-tp25-MIB", "tp25ErrorBoard"),
    (0, "Fore-tp25-MIB", "tp25ErrorModule"),
    (0, "Fore-tp25-MIB", "tp25ErrorPort"),
)
if mibBuilder.loadTexts:
    tp25ErrorEntry.setStatus("current")
_Tp25ErrorBoard_Type = Integer32
_Tp25ErrorBoard_Object = MibTableColumn
tp25ErrorBoard = _Tp25ErrorBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 1),
    _Tp25ErrorBoard_Type()
)
tp25ErrorBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ErrorBoard.setStatus("current")
_Tp25ErrorModule_Type = Integer32
_Tp25ErrorModule_Object = MibTableColumn
tp25ErrorModule = _Tp25ErrorModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 2),
    _Tp25ErrorModule_Type()
)
tp25ErrorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ErrorModule.setStatus("current")
_Tp25ErrorPort_Type = Integer32
_Tp25ErrorPort_Object = MibTableColumn
tp25ErrorPort = _Tp25ErrorPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 3),
    _Tp25ErrorPort_Type()
)
tp25ErrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ErrorPort.setStatus("current")
_Tp25ErrorSymbol_Type = Counter32
_Tp25ErrorSymbol_Object = MibTableColumn
tp25ErrorSymbol = _Tp25ErrorSymbol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 4),
    _Tp25ErrorSymbol_Type()
)
tp25ErrorSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25ErrorSymbol.setStatus("current")
_Tp25AtmTable_Object = MibTable
tp25AtmTable = _Tp25AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    tp25AtmTable.setStatus("current")
_Tp25AtmEntry_Object = MibTableRow
tp25AtmEntry = _Tp25AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1)
)
tp25AtmEntry.setIndexNames(
    (0, "Fore-tp25-MIB", "tp25AtmBoard"),
    (0, "Fore-tp25-MIB", "tp25AtmModule"),
    (0, "Fore-tp25-MIB", "tp25AtmPort"),
)
if mibBuilder.loadTexts:
    tp25AtmEntry.setStatus("current")
_Tp25AtmBoard_Type = Integer32
_Tp25AtmBoard_Object = MibTableColumn
tp25AtmBoard = _Tp25AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 1),
    _Tp25AtmBoard_Type()
)
tp25AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmBoard.setStatus("current")
_Tp25AtmModule_Type = Integer32
_Tp25AtmModule_Object = MibTableColumn
tp25AtmModule = _Tp25AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 2),
    _Tp25AtmModule_Type()
)
tp25AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmModule.setStatus("current")
_Tp25AtmPort_Type = Integer32
_Tp25AtmPort_Object = MibTableColumn
tp25AtmPort = _Tp25AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 3),
    _Tp25AtmPort_Type()
)
tp25AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmPort.setStatus("current")
_Tp25AtmHCSs_Type = Counter32
_Tp25AtmHCSs_Object = MibTableColumn
tp25AtmHCSs = _Tp25AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 4),
    _Tp25AtmHCSs_Type()
)
tp25AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmHCSs.setStatus("current")
_Tp25AtmRxCells_Type = Counter32
_Tp25AtmRxCells_Object = MibTableColumn
tp25AtmRxCells = _Tp25AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 5),
    _Tp25AtmRxCells_Type()
)
tp25AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmRxCells.setStatus("current")
_Tp25AtmTxCells_Type = Counter32
_Tp25AtmTxCells_Object = MibTableColumn
tp25AtmTxCells = _Tp25AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 6),
    _Tp25AtmTxCells_Type()
)
tp25AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp25AtmTxCells.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-tp25-MIB",
    **{"foreTP25Module": foreTP25Module,
       "tp25ConfGroup": tp25ConfGroup,
       "tp25ConfTable": tp25ConfTable,
       "tp25ConfEntry": tp25ConfEntry,
       "tp25ConfBoard": tp25ConfBoard,
       "tp25ConfModule": tp25ConfModule,
       "tp25ConfPort": tp25ConfPort,
       "tp25MediaType": tp25MediaType,
       "tp25LoopbackConfig": tp25LoopbackConfig,
       "tp25RxTiming": tp25RxTiming,
       "tp25StatsGroup": tp25StatsGroup,
       "tp25ErrorTable": tp25ErrorTable,
       "tp25ErrorEntry": tp25ErrorEntry,
       "tp25ErrorBoard": tp25ErrorBoard,
       "tp25ErrorModule": tp25ErrorModule,
       "tp25ErrorPort": tp25ErrorPort,
       "tp25ErrorSymbol": tp25ErrorSymbol,
       "tp25AtmTable": tp25AtmTable,
       "tp25AtmEntry": tp25AtmEntry,
       "tp25AtmBoard": tp25AtmBoard,
       "tp25AtmModule": tp25AtmModule,
       "tp25AtmPort": tp25AtmPort,
       "tp25AtmHCSs": tp25AtmHCSs,
       "tp25AtmRxCells": tp25AtmRxCells,
       "tp25AtmTxCells": tp25AtmTxCells}
)
