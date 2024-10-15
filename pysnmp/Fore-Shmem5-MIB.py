# SNMP MIB module (Fore-Shmem5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Shmem5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:15 2024
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

(EntryStatus,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "EntryStatus")

(AAL5CountingMode,
 shmem) = mibBuilder.importSymbols(
    "Fore-Switch-MIB",
    "AAL5CountingMode",
    "shmem")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

shmem5Group = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetmodShmem5Table_Object = MibTable
netmodShmem5Table = _NetmodShmem5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1)
)
if mibBuilder.loadTexts:
    netmodShmem5Table.setStatus("current")
_NetmodShmem5Entry_Object = MibTableRow
netmodShmem5Entry = _NetmodShmem5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1)
)
netmodShmem5Entry.setIndexNames(
    (0, "Fore-Shmem5-MIB", "nShmem5Index"),
)
if mibBuilder.loadTexts:
    netmodShmem5Entry.setStatus("current")
_NShmem5Index_Type = Integer32
_NShmem5Index_Object = MibTableColumn
nShmem5Index = _NShmem5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 1),
    _NShmem5Index_Type()
)
nShmem5Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem5Index.setStatus("current")
_NShmem5CellMemorySize_Type = Integer32
_NShmem5CellMemorySize_Object = MibTableColumn
nShmem5CellMemorySize = _NShmem5CellMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 2),
    _NShmem5CellMemorySize_Type()
)
nShmem5CellMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5CellMemorySize.setStatus("current")
_NShmem5TableMemorySize_Type = Integer32
_NShmem5TableMemorySize_Object = MibTableColumn
nShmem5TableMemorySize = _NShmem5TableMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 3),
    _NShmem5TableMemorySize_Type()
)
nShmem5TableMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5TableMemorySize.setStatus("current")
_NShmem5SchedulerMemorySize_Type = Integer32
_NShmem5SchedulerMemorySize_Object = MibTableColumn
nShmem5SchedulerMemorySize = _NShmem5SchedulerMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 4),
    _NShmem5SchedulerMemorySize_Type()
)
nShmem5SchedulerMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5SchedulerMemorySize.setStatus("current")
_NShmem5SharedMemorySize_Type = Integer32
_NShmem5SharedMemorySize_Object = MibTableColumn
nShmem5SharedMemorySize = _NShmem5SharedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 5),
    _NShmem5SharedMemorySize_Type()
)
nShmem5SharedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5SharedMemorySize.setStatus("current")
_NShmem5DupListUsed_Type = Gauge32
_NShmem5DupListUsed_Object = MibTableColumn
nShmem5DupListUsed = _NShmem5DupListUsed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 6),
    _NShmem5DupListUsed_Type()
)
nShmem5DupListUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5DupListUsed.setStatus("current")
_NShmem5CurrMcastConns_Type = Gauge32
_NShmem5CurrMcastConns_Object = MibTableColumn
nShmem5CurrMcastConns = _NShmem5CurrMcastConns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 7),
    _NShmem5CurrMcastConns_Type()
)
nShmem5CurrMcastConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5CurrMcastConns.setStatus("current")
_NShmem5CurrUcastConns_Type = Gauge32
_NShmem5CurrUcastConns_Object = MibTableColumn
nShmem5CurrUcastConns = _NShmem5CurrUcastConns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 8),
    _NShmem5CurrUcastConns_Type()
)
nShmem5CurrUcastConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5CurrUcastConns.setStatus("current")
_NShmem5CellsBuffered_Type = Gauge32
_NShmem5CellsBuffered_Object = MibTableColumn
nShmem5CellsBuffered = _NShmem5CellsBuffered_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 9),
    _NShmem5CellsBuffered_Type()
)
nShmem5CellsBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5CellsBuffered.setStatus("current")
_NShmem5DuplicationListSize_Type = Integer32
_NShmem5DuplicationListSize_Object = MibTableColumn
nShmem5DuplicationListSize = _NShmem5DuplicationListSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 11),
    _NShmem5DuplicationListSize_Type()
)
nShmem5DuplicationListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5DuplicationListSize.setStatus("current")
_NShmem5McastConns_Type = Integer32
_NShmem5McastConns_Object = MibTableColumn
nShmem5McastConns = _NShmem5McastConns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 12),
    _NShmem5McastConns_Type()
)
nShmem5McastConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nShmem5McastConns.setStatus("current")
_NShmem5UcastConns_Type = Integer32
_NShmem5UcastConns_Object = MibTableColumn
nShmem5UcastConns = _NShmem5UcastConns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 13),
    _NShmem5UcastConns_Type()
)
nShmem5UcastConns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5UcastConns.setStatus("current")
_NShmem5ConfEfciOn_Type = Integer32
_NShmem5ConfEfciOn_Object = MibTableColumn
nShmem5ConfEfciOn = _NShmem5ConfEfciOn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 14),
    _NShmem5ConfEfciOn_Type()
)
nShmem5ConfEfciOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5ConfEfciOn.setStatus("current")
_NShmem5ConfEfciOff_Type = Integer32
_NShmem5ConfEfciOff_Object = MibTableColumn
nShmem5ConfEfciOff = _NShmem5ConfEfciOff_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 15),
    _NShmem5ConfEfciOff_Type()
)
nShmem5ConfEfciOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5ConfEfciOff.setStatus("current")


class _NShmem5AAL5CountingMode_Type(AAL5CountingMode):
    """Custom type nShmem5AAL5CountingMode based on AAL5CountingMode"""


_NShmem5AAL5CountingMode_Object = MibTableColumn
nShmem5AAL5CountingMode = _NShmem5AAL5CountingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 16),
    _NShmem5AAL5CountingMode_Type()
)
nShmem5AAL5CountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5AAL5CountingMode.setStatus("current")


class _NShmem5AAl5CountingModeOverride_Type(Integer32):
    """Custom type nShmem5AAl5CountingModeOverride based on Integer32"""
    defaultValue = 2

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


_NShmem5AAl5CountingModeOverride_Type.__name__ = "Integer32"
_NShmem5AAl5CountingModeOverride_Object = MibTableColumn
nShmem5AAl5CountingModeOverride = _NShmem5AAl5CountingModeOverride_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 17),
    _NShmem5AAl5CountingModeOverride_Type()
)
nShmem5AAl5CountingModeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5AAl5CountingModeOverride.setStatus("current")


class _NShmem5OverbookingHw_Type(Integer32):
    """Custom type nShmem5OverbookingHw based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NShmem5OverbookingHw_Type.__name__ = "Integer32"
_NShmem5OverbookingHw_Object = MibTableColumn
nShmem5OverbookingHw = _NShmem5OverbookingHw_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 1, 1, 18),
    _NShmem5OverbookingHw_Type()
)
nShmem5OverbookingHw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5OverbookingHw.setStatus("current")
_BufferClassShmem5Table_Object = MibTable
bufferClassShmem5Table = _BufferClassShmem5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2)
)
if mibBuilder.loadTexts:
    bufferClassShmem5Table.setStatus("current")
_BufferClassShmem5Entry_Object = MibTableRow
bufferClassShmem5Entry = _BufferClassShmem5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1)
)
bufferClassShmem5Entry.setIndexNames(
    (0, "Fore-Shmem5-MIB", "bcShmem5Index"),
    (0, "Fore-Shmem5-MIB", "bcShmem5BufferClassIndex"),
)
if mibBuilder.loadTexts:
    bufferClassShmem5Entry.setStatus("current")
_BcShmem5Index_Type = Integer32
_BcShmem5Index_Object = MibTableColumn
bcShmem5Index = _BcShmem5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 1),
    _BcShmem5Index_Type()
)
bcShmem5Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcShmem5Index.setStatus("current")
_BcShmem5BufferClassIndex_Type = Integer32
_BcShmem5BufferClassIndex_Object = MibTableColumn
bcShmem5BufferClassIndex = _BcShmem5BufferClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 2),
    _BcShmem5BufferClassIndex_Type()
)
bcShmem5BufferClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcShmem5BufferClassIndex.setStatus("current")
_BcShmem5Status_Type = EntryStatus
_BcShmem5Status_Object = MibTableColumn
bcShmem5Status = _BcShmem5Status_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 3),
    _BcShmem5Status_Type()
)
bcShmem5Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcShmem5Status.setStatus("current")
_BcShmem5Name_Type = DisplayString
_BcShmem5Name_Object = MibTableColumn
bcShmem5Name = _BcShmem5Name_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 4),
    _BcShmem5Name_Type()
)
bcShmem5Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcShmem5Name.setStatus("current")


class _BcShmem5EpdThreshold_Type(Integer32):
    """Custom type bcShmem5EpdThreshold based on Integer32"""
    defaultValue = 90


_BcShmem5EpdThreshold_Object = MibTableColumn
bcShmem5EpdThreshold = _BcShmem5EpdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 2, 1, 5),
    _BcShmem5EpdThreshold_Type()
)
bcShmem5EpdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcShmem5EpdThreshold.setStatus("current")
_BufferClassAssignShmem5Table_Object = MibTable
bufferClassAssignShmem5Table = _BufferClassAssignShmem5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3)
)
if mibBuilder.loadTexts:
    bufferClassAssignShmem5Table.setStatus("current")
_BufferClassAssignShmem5Entry_Object = MibTableRow
bufferClassAssignShmem5Entry = _BufferClassAssignShmem5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1)
)
bufferClassAssignShmem5Entry.setIndexNames(
    (0, "Fore-Shmem5-MIB", "bcaShmem5Index"),
    (0, "Fore-Shmem5-MIB", "bcaShmem5ServCategory"),
    (0, "Fore-Shmem5-MIB", "bcaShmem5ServSubCategory"),
)
if mibBuilder.loadTexts:
    bufferClassAssignShmem5Entry.setStatus("current")
_BcaShmem5Index_Type = Integer32
_BcaShmem5Index_Object = MibTableColumn
bcaShmem5Index = _BcaShmem5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 1),
    _BcaShmem5Index_Type()
)
bcaShmem5Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcaShmem5Index.setStatus("current")
_BcaShmem5ServCategory_Type = Integer32
_BcaShmem5ServCategory_Object = MibTableColumn
bcaShmem5ServCategory = _BcaShmem5ServCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 2),
    _BcaShmem5ServCategory_Type()
)
bcaShmem5ServCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcaShmem5ServCategory.setStatus("current")
_BcaShmem5ServSubCategory_Type = Integer32
_BcaShmem5ServSubCategory_Object = MibTableColumn
bcaShmem5ServSubCategory = _BcaShmem5ServSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 3),
    _BcaShmem5ServSubCategory_Type()
)
bcaShmem5ServSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcaShmem5ServSubCategory.setStatus("current")
_BcaShmem5Status_Type = EntryStatus
_BcaShmem5Status_Object = MibTableColumn
bcaShmem5Status = _BcaShmem5Status_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 4),
    _BcaShmem5Status_Type()
)
bcaShmem5Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcaShmem5Status.setStatus("current")
_BcaShmem5BuffClass_Type = Integer32
_BcaShmem5BuffClass_Object = MibTableColumn
bcaShmem5BuffClass = _BcaShmem5BuffClass_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 3, 1, 5),
    _BcaShmem5BuffClass_Type()
)
bcaShmem5BuffClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcaShmem5BuffClass.setStatus("current")
_IfBufferClassShmem5Table_Object = MibTable
ifBufferClassShmem5Table = _IfBufferClassShmem5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4)
)
if mibBuilder.loadTexts:
    ifBufferClassShmem5Table.setStatus("current")
_IfBufferClassShmem5Entry_Object = MibTableRow
ifBufferClassShmem5Entry = _IfBufferClassShmem5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1)
)
ifBufferClassShmem5Entry.setIndexNames(
    (0, "Fore-Shmem5-MIB", "ibShmem5Index"),
    (0, "Fore-Shmem5-MIB", "ibShmem5If"),
    (0, "Fore-Shmem5-MIB", "ibShmem5Buffer"),
)
if mibBuilder.loadTexts:
    ifBufferClassShmem5Entry.setStatus("current")
_IbShmem5Index_Type = Integer32
_IbShmem5Index_Object = MibTableColumn
ibShmem5Index = _IbShmem5Index_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 1),
    _IbShmem5Index_Type()
)
ibShmem5Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibShmem5Index.setStatus("current")
_IbShmem5If_Type = Integer32
_IbShmem5If_Object = MibTableColumn
ibShmem5If = _IbShmem5If_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 2),
    _IbShmem5If_Type()
)
ibShmem5If.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibShmem5If.setStatus("current")
_IbShmem5Buffer_Type = Integer32
_IbShmem5Buffer_Object = MibTableColumn
ibShmem5Buffer = _IbShmem5Buffer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 3),
    _IbShmem5Buffer_Type()
)
ibShmem5Buffer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibShmem5Buffer.setStatus("current")
_IbShmem5Qsize_Type = Integer32
_IbShmem5Qsize_Object = MibTableColumn
ibShmem5Qsize = _IbShmem5Qsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 4),
    _IbShmem5Qsize_Type()
)
ibShmem5Qsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibShmem5Qsize.setStatus("current")
_IbShmem5CLP01Thresh_Type = Integer32
_IbShmem5CLP01Thresh_Object = MibTableColumn
ibShmem5CLP01Thresh = _IbShmem5CLP01Thresh_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 5),
    _IbShmem5CLP01Thresh_Type()
)
ibShmem5CLP01Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibShmem5CLP01Thresh.setStatus("current")
_IbShmem5CLP1Thresh_Type = Integer32
_IbShmem5CLP1Thresh_Object = MibTableColumn
ibShmem5CLP1Thresh = _IbShmem5CLP1Thresh_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 6),
    _IbShmem5CLP1Thresh_Type()
)
ibShmem5CLP1Thresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibShmem5CLP1Thresh.setStatus("current")
_IbShmem5TxCells_Type = Counter32
_IbShmem5TxCells_Object = MibTableColumn
ibShmem5TxCells = _IbShmem5TxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 7),
    _IbShmem5TxCells_Type()
)
ibShmem5TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5TxCells.setStatus("current")
_IbShmem5CLP01Loss_Type = Counter32
_IbShmem5CLP01Loss_Object = MibTableColumn
ibShmem5CLP01Loss = _IbShmem5CLP01Loss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 8),
    _IbShmem5CLP01Loss_Type()
)
ibShmem5CLP01Loss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5CLP01Loss.setStatus("current")
_IbShmem5CLP1Loss_Type = Counter32
_IbShmem5CLP1Loss_Object = MibTableColumn
ibShmem5CLP1Loss = _IbShmem5CLP1Loss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 9),
    _IbShmem5CLP1Loss_Type()
)
ibShmem5CLP1Loss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5CLP1Loss.setStatus("current")
_IbShmem5EPDLoss_Type = Counter32
_IbShmem5EPDLoss_Object = MibTableColumn
ibShmem5EPDLoss = _IbShmem5EPDLoss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 10),
    _IbShmem5EPDLoss_Type()
)
ibShmem5EPDLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5EPDLoss.setStatus("current")
_IbShmem5PPDLoss_Type = Counter32
_IbShmem5PPDLoss_Object = MibTableColumn
ibShmem5PPDLoss = _IbShmem5PPDLoss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 11),
    _IbShmem5PPDLoss_Type()
)
ibShmem5PPDLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5PPDLoss.setStatus("current")
_IbShmem5OverflowLoss_Type = Counter32
_IbShmem5OverflowLoss_Object = MibTableColumn
ibShmem5OverflowLoss = _IbShmem5OverflowLoss_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 12),
    _IbShmem5OverflowLoss_Type()
)
ibShmem5OverflowLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5OverflowLoss.setStatus("current")
_IbShmem5CurrentQsize_Type = Gauge32
_IbShmem5CurrentQsize_Object = MibTableColumn
ibShmem5CurrentQsize = _IbShmem5CurrentQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 13),
    _IbShmem5CurrentQsize_Type()
)
ibShmem5CurrentQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5CurrentQsize.setStatus("current")
_IbShmem5MaxQsize_Type = Gauge32
_IbShmem5MaxQsize_Object = MibTableColumn
ibShmem5MaxQsize = _IbShmem5MaxQsize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 14),
    _IbShmem5MaxQsize_Type()
)
ibShmem5MaxQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5MaxQsize.setStatus("current")
_IbShmem5IfName_Type = DisplayString
_IbShmem5IfName_Object = MibTableColumn
ibShmem5IfName = _IbShmem5IfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 4, 1, 15),
    _IbShmem5IfName_Type()
)
ibShmem5IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibShmem5IfName.setStatus("current")
_NetmodShmem5CustomBCSTable_Object = MibTable
netmodShmem5CustomBCSTable = _NetmodShmem5CustomBCSTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5)
)
if mibBuilder.loadTexts:
    netmodShmem5CustomBCSTable.setStatus("current")
_NetmodShmem5CustomBCSEntry_Object = MibTableRow
netmodShmem5CustomBCSEntry = _NetmodShmem5CustomBCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1)
)
netmodShmem5CustomBCSEntry.setIndexNames(
    (0, "Fore-Shmem5-MIB", "nShmem5CustomBCSIndex"),
    (0, "Fore-Shmem5-MIB", "nShmem5CustomBCSValue"),
)
if mibBuilder.loadTexts:
    netmodShmem5CustomBCSEntry.setStatus("current")
_NShmem5CustomBCSIndex_Type = Integer32
_NShmem5CustomBCSIndex_Object = MibTableColumn
nShmem5CustomBCSIndex = _NShmem5CustomBCSIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 1),
    _NShmem5CustomBCSIndex_Type()
)
nShmem5CustomBCSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem5CustomBCSIndex.setStatus("current")
_NShmem5CustomBCSValue_Type = Integer32
_NShmem5CustomBCSValue_Object = MibTableColumn
nShmem5CustomBCSValue = _NShmem5CustomBCSValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 2),
    _NShmem5CustomBCSValue_Type()
)
nShmem5CustomBCSValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nShmem5CustomBCSValue.setStatus("current")
_NShmem5CustomBCSWeight_Type = Integer32
_NShmem5CustomBCSWeight_Object = MibTableColumn
nShmem5CustomBCSWeight = _NShmem5CustomBCSWeight_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 3),
    _NShmem5CustomBCSWeight_Type()
)
nShmem5CustomBCSWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5CustomBCSWeight.setStatus("current")
_NShmem5CustomBCSBuffer_Type = Integer32
_NShmem5CustomBCSBuffer_Object = MibTableColumn
nShmem5CustomBCSBuffer = _NShmem5CustomBCSBuffer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 4),
    _NShmem5CustomBCSBuffer_Type()
)
nShmem5CustomBCSBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5CustomBCSBuffer.setStatus("current")
_NShmem5CustomBCSRowStatus_Type = RowStatus
_NShmem5CustomBCSRowStatus_Object = MibTableColumn
nShmem5CustomBCSRowStatus = _NShmem5CustomBCSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 5, 1, 5),
    _NShmem5CustomBCSRowStatus_Type()
)
nShmem5CustomBCSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5CustomBCSRowStatus.setStatus("current")
_NetmodShmem5CustomBCSGroup_ObjectIdentity = ObjectIdentity
netmodShmem5CustomBCSGroup = _NetmodShmem5CustomBCSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 6)
)


class _NShmem5CustomBCSState_Type(Integer32):
    """Custom type nShmem5CustomBCSState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NShmem5CustomBCSState_Type.__name__ = "Integer32"
_NShmem5CustomBCSState_Object = MibScalar
nShmem5CustomBCSState = _NShmem5CustomBCSState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 5, 13, 6, 1),
    _NShmem5CustomBCSState_Type()
)
nShmem5CustomBCSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nShmem5CustomBCSState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Shmem5-MIB",
    **{"shmem5Group": shmem5Group,
       "netmodShmem5Table": netmodShmem5Table,
       "netmodShmem5Entry": netmodShmem5Entry,
       "nShmem5Index": nShmem5Index,
       "nShmem5CellMemorySize": nShmem5CellMemorySize,
       "nShmem5TableMemorySize": nShmem5TableMemorySize,
       "nShmem5SchedulerMemorySize": nShmem5SchedulerMemorySize,
       "nShmem5SharedMemorySize": nShmem5SharedMemorySize,
       "nShmem5DupListUsed": nShmem5DupListUsed,
       "nShmem5CurrMcastConns": nShmem5CurrMcastConns,
       "nShmem5CurrUcastConns": nShmem5CurrUcastConns,
       "nShmem5CellsBuffered": nShmem5CellsBuffered,
       "nShmem5DuplicationListSize": nShmem5DuplicationListSize,
       "nShmem5McastConns": nShmem5McastConns,
       "nShmem5UcastConns": nShmem5UcastConns,
       "nShmem5ConfEfciOn": nShmem5ConfEfciOn,
       "nShmem5ConfEfciOff": nShmem5ConfEfciOff,
       "nShmem5AAL5CountingMode": nShmem5AAL5CountingMode,
       "nShmem5AAl5CountingModeOverride": nShmem5AAl5CountingModeOverride,
       "nShmem5OverbookingHw": nShmem5OverbookingHw,
       "bufferClassShmem5Table": bufferClassShmem5Table,
       "bufferClassShmem5Entry": bufferClassShmem5Entry,
       "bcShmem5Index": bcShmem5Index,
       "bcShmem5BufferClassIndex": bcShmem5BufferClassIndex,
       "bcShmem5Status": bcShmem5Status,
       "bcShmem5Name": bcShmem5Name,
       "bcShmem5EpdThreshold": bcShmem5EpdThreshold,
       "bufferClassAssignShmem5Table": bufferClassAssignShmem5Table,
       "bufferClassAssignShmem5Entry": bufferClassAssignShmem5Entry,
       "bcaShmem5Index": bcaShmem5Index,
       "bcaShmem5ServCategory": bcaShmem5ServCategory,
       "bcaShmem5ServSubCategory": bcaShmem5ServSubCategory,
       "bcaShmem5Status": bcaShmem5Status,
       "bcaShmem5BuffClass": bcaShmem5BuffClass,
       "ifBufferClassShmem5Table": ifBufferClassShmem5Table,
       "ifBufferClassShmem5Entry": ifBufferClassShmem5Entry,
       "ibShmem5Index": ibShmem5Index,
       "ibShmem5If": ibShmem5If,
       "ibShmem5Buffer": ibShmem5Buffer,
       "ibShmem5Qsize": ibShmem5Qsize,
       "ibShmem5CLP01Thresh": ibShmem5CLP01Thresh,
       "ibShmem5CLP1Thresh": ibShmem5CLP1Thresh,
       "ibShmem5TxCells": ibShmem5TxCells,
       "ibShmem5CLP01Loss": ibShmem5CLP01Loss,
       "ibShmem5CLP1Loss": ibShmem5CLP1Loss,
       "ibShmem5EPDLoss": ibShmem5EPDLoss,
       "ibShmem5PPDLoss": ibShmem5PPDLoss,
       "ibShmem5OverflowLoss": ibShmem5OverflowLoss,
       "ibShmem5CurrentQsize": ibShmem5CurrentQsize,
       "ibShmem5MaxQsize": ibShmem5MaxQsize,
       "ibShmem5IfName": ibShmem5IfName,
       "netmodShmem5CustomBCSTable": netmodShmem5CustomBCSTable,
       "netmodShmem5CustomBCSEntry": netmodShmem5CustomBCSEntry,
       "nShmem5CustomBCSIndex": nShmem5CustomBCSIndex,
       "nShmem5CustomBCSValue": nShmem5CustomBCSValue,
       "nShmem5CustomBCSWeight": nShmem5CustomBCSWeight,
       "nShmem5CustomBCSBuffer": nShmem5CustomBCSBuffer,
       "nShmem5CustomBCSRowStatus": nShmem5CustomBCSRowStatus,
       "netmodShmem5CustomBCSGroup": netmodShmem5CustomBCSGroup,
       "nShmem5CustomBCSState": nShmem5CustomBCSState}
)
